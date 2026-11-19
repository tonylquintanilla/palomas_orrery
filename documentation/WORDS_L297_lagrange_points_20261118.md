<!-- Doc-Kind: hand | The words for the Lagrange points (L-297): each point's display name, description, info text and link, the two group names, and the finding that JPL serves no L3 point; for Tony's approval before they enter any file. -->
# The Lagrange points: the words, for your approval

Tony Quintanilla, PE | Claude Opus 5.5 (Claude Code) | November 18, 2026

Built on orrery 53bf24695cb990c490949d333a944558941a9349 at
https://github.com/tonylquintanilla/palomas_orrery and website
133dbd21930d39b66283b820ce71bc705a640855 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Nothing
in either repository is changed yet; this file is the only new one.

From the brief `COORD_L297_lagrange_points_brief_20261118.md`, section
5, steps 1 and 2. Read for it, on 2026-11-18:
- NASA's "What is a Lagrange Point?",
  https://science.nasa.gov/resource/what-is-a-lagrange-point/ (dated
  March 27, 2018; page last updated Nov 01, 2024), whole, every
  paragraph from "What are they?" to the credit to Neil J. Cornish.
- JPL's Lookup for each of the ten ids (group=mb), and JPL's data sheet
  for each from its main service (COMMAND='<id>', MAKE_EPHEM='NO').

## First: JPL serves eight points, not ten

JPL has no record for either L3. The Lookup finds nothing for 3013 or
33. Asked by number, JPL's main service answers with the asteroid of
that number: 3013 is "3013 Dobrovoleva (1979 SD7)" and 33 is
"33 Polyhymnia (A854 UB)". The orrery asks the same way (astroquery,
id_type 'id', now the same as none), so the orrery's checkboxes EM-L3
and L3 have been drawing those two asteroids, about 3.4 AU away, under
the points' names. The orrery's info text for EM-L3 is written as a
JPL data sheet that JPL does not have.

The Horizons check refuses EM-L3 by name, run today on a trial entry:
"no object in either index whose primary id is 3013". So it would have
caught this at keying.

PROPOSED: key the eight JPL serves, and take EM-L3 and L3 out of the
orrery (the two list entries, their checkboxes, their info text and
colors). The website draws eight. NASA's L3 sentence ("NASA is unlikely
to find any use for the L3 point since it remains hidden behind the Sun
at all times.") is then used nowhere. If you would rather keep the two
checkboxes for some later source, say so; they would stay unkeyed and
off by default, and still draw the asteroids until changed.

## In one look

| Key | Display name | JPL's name | JPL's id | Drawn around |
|---|---|---|---|---|
| em_l1 | EM-L1 | EM-L1 | 3011 | Earth |
| em_l2 | EM-L2 | EM-L2 | 3012 | Earth |
| em_l4 | EM-L4 | EM-L4 | 3014 | Earth |
| em_l5 | EM-L5 | EM-L5 | 3015 | Earth |
| semb_l1 | SEMB-L1 | SEMB-L1 | 31 | the Sun |
| semb_l2 | SEMB-L2 | SEMB-L2 | 32 | the Sun |
| semb_l4 | SEMB-L4 | SEMB-L4 | 34 | the Sun |
| semb_l5 | SEMB-L5 | SEMB-L5 | 35 | the Sun |

- The display name is JPL's own name for each point. The Earth-Moon
  four already carry it. The other four change from "L1" to "SEMB-L1"
  and so on, in the orrery too: a bare "L1" beside "EM-L1" near Earth
  does not say which pair it belongs to, and SEMB is JPL's word,
  explained in each description.
- The link for all eight: NASA's page above, with no text fragment on
  the address. The Earth-Moon four drop the hyperphysics page.
- JPL answers every point around Earth, the Sun and the Earth-Moon
  barycenter alike (asked today, 2026-11-18 00:00). Which centre the
  website serves each around is ruling 4 of the brief: Earth for the
  Earth-Moon points, the Sun for the others.

## The group names

- "Earth-Moon Lagrange Points" (the orrery's heading today, unchanged).
- "Sun & Earth-Moon Barycenter Lagrange Points": JPL's form, from its
  data sheets ("Sun & Earth-Moon Barycenter Lagrange 1"). It replaces
  the orrery's "Sun-Earth-Moon Lagrange Points".

## Each point's description

This is `mission_info` in the orrery, shown in its hover; the website
prints it without the opening "Horizons: <id>.", which goes on its own
source line. Our sentences in American spelling; NASA's exactly as NASA
wrote them, whole, nothing cut ("sun" and "earth" lower-case where NASA
has them so).

The pieces, then each point.

- A. Our sentence naming the point (composed, no numbers):
  "<name> is JPL's name for the <JPL's long name> point." The long name
  is JPL's own, from the data sheet's first line: "Earth-Moon
  Lagrange-1", "Sun & Earth-Moon Barycenter Lagrange-2".
- B. For the four SEMB points only, the gloss of JPL's word (composed):
  "The Earth-Moon barycenter is the center of mass of Earth and the
  Moon."
- C. NASA, the page's first sentence: "Lagrange points are positions in
  space where objects sent there tend to stay put."
- D. NASA, for L1 and L2: "The unstable Lagrange points - labeled L1,
  L2 and L3 - lie along the line connecting the two large masses."
- E. NASA, for L4 and L5: "The stable Lagrange points - labeled L4 and
  L5 - form the apex of two equilateral triangles that have the large
  masses at their vertices."

### EM-L1 and EM-L2

"Horizons: 3011. EM-L1 is JPL's name for the Earth-Moon Lagrange-1
point. NASA: "Lagrange points are positions in space where objects sent
there tend to stay put." "The unstable Lagrange points - labeled L1, L2
and L3 - lie along the line connecting the two large masses.""

EM-L2 the same, with 3012, EM-L2 and Lagrange-2.

- GAP: NASA's page has no sentence about the Earth-Moon L1 or L2 in
  particular, and links no NASA page for them. Nothing is typed in its
  place.

### EM-L4 and EM-L5

"Horizons: 3014. EM-L4 is JPL's name for the Earth-Moon Lagrange-4
point. NASA: "Lagrange points are positions in space where objects sent
there tend to stay put." "The stable Lagrange points - labeled L4 and
L5 - form the apex of two equilateral triangles that have the large
masses at their vertices." "In 1956 the Polish astronomer Kordylewski
discovered large concentrations of dust at the Trojan points of the
Earth-Moon system.""

EM-L5 the same, with 3015, EM-L5 and Lagrange-5.

- The last sentence is NASA's only one about the Earth-Moon points. It
  holds a number, 1956, which the export reports; it is NASA's, quoted
  with its page. Drop it if you want the box shorter.
- Not used: NASA's "L4 leads the orbit of earth and L5 follows." It is
  about Earth's orbit, so it is true of SEMB-L4 and SEMB-L5, not of the
  Earth-Moon points.

### SEMB-L1

"Horizons: 31. SEMB-L1 is JPL's name for the Sun & Earth-Moon
Barycenter Lagrange-1 point. The Earth-Moon barycenter is the center of
mass of Earth and the Moon. NASA: "Lagrange points are positions in
space where objects sent there tend to stay put." "The unstable Lagrange
points - labeled L1, L2 and L3 - lie along the line connecting the two
large masses.""

- Left out, my recommendation: NASA's "The L1 point of the Earth-Sun
  system affords an uninterrupted view of the sun and is currently home
  to the Solar and Heliospheric Observatory Satellite SOHO." The
  "currently" is the page's of 2018, and I have no source saying SOHO
  is there today. Say if you want it in.

### SEMB-L2

"Horizons: 32. SEMB-L2 is JPL's name for the Sun & Earth-Moon
Barycenter Lagrange-2 point. The Earth-Moon barycenter is the center of
mass of Earth and the Moon. NASA: "Lagrange points are positions in
space where objects sent there tend to stay put." "The unstable Lagrange
points - labeled L1, L2 and L3 - lie along the line connecting the two
large masses." "L2 is ideal for astronomy because a spacecraft is close
enough to readily communicate with Earth, can keep Sun, Earth and Moon
behind the spacecraft for solar power and (with appropriate shielding)
provides a clear view of deep space for our telescopes.""

- This is the L2 that ESCAPADE's box names.
- Not used: the sentence before it on the page, which calls L2 the
  "future home of the James Webb Space Telescope" (true in 2018, not
  now), and the one after it, which gives a number ("approximately 23
  days") for something no room draws.

### SEMB-L4 and SEMB-L5

"Horizons: 34. SEMB-L4 is JPL's name for the Sun & Earth-Moon
Barycenter Lagrange-4 point. The Earth-Moon barycenter is the center of
mass of Earth and the Moon. NASA: "Lagrange points are positions in
space where objects sent there tend to stay put." "The stable Lagrange
points - labeled L4 and L5 - form the apex of two equilateral triangles
that have the large masses at their vertices. L4 leads the orbit of
earth and L5 follows.""

SEMB-L5 the same, with 35, SEMB-L5 and Lagrange-5.

- An option for SEMB-L4 only, left out: NASA's "In 2010 NASA's WISE
  telescope finally confirmed the first Trojan asteroid (2010 TK7)
  around Earth's leading Lagrange point." Say if you want it.

## Each point's info text (the orrery only)

This is the tooltip over each checkbox in the orrery (`INFO` in
`info_dictionary.py`); the website does not read it. Proposed, for each
of the eight: "Horizons: <id>. JPL: "<JPL's data sheet, as read today>"",
exactly as JPL wrote it, its "Revised:" line first, its numbering as JPL
numbers it (the Earth-Moon L1 and L2 sheets go #1, #2, #4), its spelling
too ("equilibirium" is JPL's).

What changes from today's text:
- The four SEMB sheets were revised by JPL on Mar 23, 2026; today's text
  copies the 2013 sheets. They are read again.
- Today's text adds bullets of its own under the SEMB sheets ("will
  generally track along the Earth-Moon Barycenter's orbit", "more like
  moving targets"), with no source. They come out.
- EM-L5's text names id 3014 on its first line; JPL's sheet says 3015.
  It is re-read, so this is gone.
- EM-L3's and L3's text go with their entries.

## What the export carries for a point (read, for step 4)

- Today a keyed point would be given a period line "Not yet fetched
  from JPL." That is not true of a point, which has no orbit of its own.
  And the period fetch counts a Lagrange point among the types it asks
  JPL a period for, so it would fetch one. PROPOSED: a point serves no
  period, as the Sun and a spacecraft serve none, and the period fetch
  names it and asks nothing.
- The typed span, 1900 to 2050: no live drawing reads it for a point
  (only code marked obsolete since Nov 3 does). JPL's spans, read today:
  1900-01-01 to 2151-01-01 for the Earth-Moon points, 1900-01-02 to
  2150-12-31 for the SEMB points. PROPOSED: the typed span goes, as
  nothing reads it, after a last search for any reader; if one is found,
  it becomes JPL's span with the day it was read.

## What I need

"Approved", or your changes. With it I key the eight, take out the two
L3 entries, and run the maintenance run.

## As approved (Tony, 2026-11-18, night)

"Approved, with three changes." The words above stand, with these:

1. Display names: "Earth-Moon L1", "Earth-Moon L2", "Earth-Moon L4",
   "Earth-Moon L5"; "Earth-Sun L1", "Earth-Sun L2", "Earth-Sun L4",
   "Earth-Sun L5". "Earth-Sun" is NASA's word on the page read ("The L1
   point of the Earth-Sun system", and the same for L2), checked before
   it was used. JPL's names (EM-L1, SEMB-L1 ...) stay in horizons_name
   and on the source line. Groups: "Earth-Moon Lagrange Points" and
   "Earth-Sun Lagrange Points", the orrery's headings too.
2. Sentence A, rewritten since the name shown is not JPL's: "JPL names
   it EM-L1, the Earth-Moon Lagrange-1 point." and "JPL names it
   SEMB-L1, the Sun & Earth-Moon Barycenter Lagrange-1 point." (and so
   on for each). Sentence B stays for the Earth-Sun four.
3. The WISE sentence goes in, for Earth-Sun L4 only. Kordylewski stays
   for Earth-Moon L4 and L5. SOHO and Webb stay out.

The typed span: the last search found a live reader
(path_drawing.entry_span, which bounds the fetch and the animation), so
it is JPL's span, as proposed above, not removed.
