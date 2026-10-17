<!-- Doc-Kind: hand | Earth's first design talk (zero code), October 16, 2026: Tony's rulings on the belts' shape (L-330), the eight held sentences (L-451), the website's notes beside a citation (L-452, with L-450), the run records (L-449), and the magnetosphere's aberration (L-314), each in his words, with the options he declined. -->
# Design record: Earth's design talk, round 1

Built on orrery 48c84c3 ("Update WHERE_WE_ARE_10-16-26_1708_run_record.md")
at https://github.com/tonylquintanilla/palomas_orrery, and gallery 2090a8b
("patch km radius label") at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

- Type: DESIGN SESSION, zero code. October 16, 2026, 21:38 to 22:20
  Chicago time, Tony on the chat, Claude linked to his machine.
- Brief: `documentation/HANDOFF_earth_design_talk_brief_20261016.md`
  (Claude Fable 5.1), read in full from Tony's folder before the talk;
  the ledger blocks L-330, L-451, L-452, L-450, L-449 and L-413 read at
  orrery 48c84c3; L-314 read when the aberration was taken up.
- Skills confirmed at load against the manifest of v3.101:
  interactive-exhibit 1.16 (this discharges v3.101's obligation) and
  ledger-and-session-records 1.21. horizons-orbital-mechanics 1.8 still
  travels; nothing here fired it.
- Companion: the build brief,
  `documentation/HANDOFF_earth_round1_build_brief_20261016.md`. The
  rulings reach the ledger through `patch_earth_round1_close_20261016.py`.

Tony's words are quoted as he typed them in the chat (curly quotes
made straight). Where Claude's reading of a ruling went beyond his
words, it says so.

## 0. Found before the talk: L-330's premise was out of date

The brief asked whether the belts' hover still printed the typed 0.5
Earth radii as "Band thickness". It does not, and the belts are no
longer drawn as one ring at the peak. Since L-322 Stage D (orrery patches
D8 and D9, 2026-09-25; gallery patch 3, 2026-09-26) both instruments
draw each belt as evenly spaced flat rings from its served inner edge to
its served outer edge, in the equatorial plane, the peak ring brighter
(`earth_visualization_shells.py`, `_even_belt_rings`;
`gallery/feature_renderers.js`, `evenBeltRings` and `renderBelts`,
"the typed 0.5 belt thickness fallback is gone"). L-330's "gap" bullet
describes the drawing before that.

So the talk's question became the belts' CURVE, not their width: each
belt is a flat washer lying in the equator.

A correction to the brief, said in the talk: a dipole drawn centred on
the spin axis does NOT show the South Atlantic Anomaly. The anomaly
comes from the field's tilt and offset, which is L-375's talk. What the
curved shape teaches is that trapped particles follow field lines to
high latitudes, where those lines meet the ground.

## 1. The belts' shape (L-330)

**Question:** which shape goes to a throwaway render in the orrery for
Tony's look.

Options put: keep today's flat bands; A, both belts curved as the space
between two dipole field lines from the served edges; C, outer belt
curved, inner belt flat (Claude's recommendation, rendering A and C
together); B, a doughnut tube, which Claude advised dropping because its
height would be a number nobody measured.

**Tony:** "Let's start with A and see where we take it."

So A, both belts curved, goes to the render. C stays the fallback if the
inner belt is unreadable where its field line meets the ground near 17
degrees latitude; the outer belt's lines meet it near 55 and 68 degrees.

**Question:** how the peak is marked once the belts are curved. Options
put: a bright ring in the equator only (where the peak is measured;
Claude's recommendation); the whole peak field line brightened (declined
by Claude: along one field line the particles are densest at the
equator and fewer reach high latitudes, so an evenly bright line says
the opposite); or no peak mark.

**Tony:** "Thought: what about a density field similar to the sun's
streamer belt?"

Claude's answer: it fits the physics better than rings, it marks the
peak by itself (the dots thickest at the peak in the equator, thinning
across the belt and up each field line), and it eases the inner belt's
readability near the ground. Its costs: the fade is not measured and
the hover says so, as the streamer belt's does ("Its warp and width are
drawn to show the shape, not measured."); random scatter falls under
Tony's L-434 ruling (scattered dots are placed by the orrery and stored
for the website), which makes the build larger; more dots on the phone.
Options put: a density field on a regular pattern thinning by a
formula; a density field with random scatter; rings along the field
lines. Claude recommended the regular pattern with the rings beside it.

**Tony:** "As recommended", then: "Wait I thought the comparison was a
formula and the random scatter."

**RULING:** the throwaway render draws both belts curved along dipole
field lines (option A), as a DENSITY FIELD, two ways side by side:

1. dots on a regular pattern that thins by a formula (stays "a few
   numbers and a formula": each instrument draws it itself);
2. dots scattered at random, like the streamer belt (if chosen, L-434's
   stored drawing: the orrery places the dots, the website draws them
   as given).

The rings version drops out. The peak is where the dots are thickest,
in the equator; no separate peak line is ruled. Tony's look at the
render decides between 1 and 2, and whether the inner belt reads or
falls back to C.

Declined, and why: the flat bands (teach the width, not the curve);
C as the first render (Tony chose to start from A); B (an unmeasured
height); the rings (Tony's correction: the comparison is the two
density fields).

## 2. The eight sentences the Typed facts check holds open (L-451)

Recommendations put, one line each: serve 1 to 5 with their rows'
sources; allow 6; reword 7 to "Where that is so, the text beside it
says so." and allow it, since "Nobody has measured those" is a claim
about the world with no source; cut 8, since curved belts no longer
"sit in" the plane.

**Tony:** "Confirmed as recommended" (his item 3 in the reply,
answering question 3).

**RULING:**
1. Tilt (the Earth-Moon barycentre's orbit, JPL Horizons): SERVE, with
   the pole-of-date source already served.
2. "Earth turns once every # hours measured against the stars.": SERVE,
   with the rotation row's source.
3. The magnetotail sentence: SERVE, with the tail rows' source.
4. "...the real boundary... within # Earth radii of this model.": SERVE,
   with the Shue row's source.
5. "...the real shock... within # Earth radii of this model.": SERVE,
   with the Jelinek row's source.
6. The Sun room's "Some of what you see is drawn to show a shape rather
   than measured...": ALLOW, a sentence about the picture.
7. The Sun room's "Nobody has measured those, and where that is so, the
   text says so.": REWORD to "Where that is so, the text beside it says
   so." and ALLOW (how to use the page).
8. Earth's "The radiation belts sit in Earth's equatorial plane, the
   daily average of the tilted magnetic equator they follow.": CUT.
   Nothing is lost: the belts' served `hovers_plane` already says the
   plane and the daily average, with the tilt row's source (read at
   gallery 2090a8b), and the curved build rewrites the belts' hover.

## 3. The website's notes beside a citation (L-452, with L-450)

The rule put, two versions differing only on where a locator goes: A,
keep the locator in the website's note; B, move it into the orrery's
citation and strike it from the note (Claude's recommendation). Both
struck a note that only repeats its citation, and kept project names
and dates out of what a visitor reads.

**Tony:** "Wording that is relevant to the citation should be moved to
the store.  Notes should be dropped unless they are drawing choices."

**RULING (a rule, not 35 rulings):**
- Any wording in a website note that bears on its citation (a locator,
  what the cited value is, an edition, a date of observation) moves
  into the store, `constants_new.py`, on that row: into its `# Source:`
  text if it is part of the citation, otherwise into the row's other
  comment lines (L-450's own rule for store notes).
- A website note (`source_note`) is kept only when it describes a
  DRAWING CHOICE. Every other note is dropped.
- This is stricter than B: B kept a note explaining what the number is
  for; under Tony's rule that wording goes to the store or is dropped.
- Claude's reading, said in the talk and not contradicted: the rule
  also covers the Crust's served `note`, which describes a drawing
  choice (drawn at Earth's mean radius) and so stays, with its
  attribution "(Tony, 2026-09-28)" taken out.
- The edited notes and citations come to Tony as a list before
  anything ships (unchanged from the brief).
- Method, so it goes into interactive-exhibit at the build's bump: the
  skill's description of `source_note` narrows from "the website's own
  words about a citation" to a drawing choice beside a citation.

## 4. The build's run records (L-449)

Options put: keep every record (about 1 KB each, a third of a megabyte
a year; Claude's recommendation while the loss is unexplained); keep a
limit such as the last 30 (deliberate deletions make an accidental one
look normal).

**Tony:** "For the purpose of explanation, confirmed. Otherwise what is
gained by storing?"

Claude's answer: very little. Nothing reads the records; each Daily
Run's push commits that night's record, so git keeps every one even if
the folder held only the latest; the folder adds only the convenience of
looking back without git history. The case for keeping them is that a
full folder is what shows a loss. Proposed: keep every record until the
cause is found, then a deliberate limit, its number set then, with the
builder naming each record it removes.

**Tony:** "Yes"

**RULING:** keep every record until the cause of the loss is found.
Then the builder moves to a deliberate limit, the number set at that
time, and names each record it removes. The check (the builder prints
what it carried; the Daily Run stops on a loss, naming each record)
goes in the build either way, as the brief said.

## 5. The magnetosphere's aberration (L-314; taken up after the agenda)

**Tony:** "Yes let's include the aberration"

What was put: both fits are made in aberrated frames, the nose turned
about 4.3 degrees toward Earth's motion; at the drawn scale that is
about three quarters of an Earth radius sideways at the nose and about
seven, a hundred Earth radii down the tail. The 4.3 comes from the
declared 400 km/s, whose row reads "a nominal speed whose reason is NOT
YET WRITTEN". Options: apply it now; draw unturned and say so in a
served hover sentence (Claude's recommendation).

**Tony:** "What's the cost of L314?" Answered: its own design talk, then
a build of two or three patches; a feed the builder has never read
(NOAA SWPC's DSCOVR solar wind, addresses recorded from memory, to be
confirmed); a day's range rather than a spot value; a declared helium
share; guards on every value; two checks reworked (the derived-figures
test and the drift checker's units); the website only, as written.

**Tony:** "Don't we already turn I believe Neptune's?" Answered, from
the code at both HEADs: no instrument applies the aberration to any
planet. Neptune's magnetosphere is turned for its field's 47 degree
tilt and offset (`neptune_visualization_shells.py`), and every planet's
faces the Sun's actual direction (`rotate_to_sunward`); neither is the
solar wind's slant.

**Tony:** "What's the source of 400, the mean?" Answered: none. The row
records it as declared with its reason not yet written; Shue's 410 km/s
(p. 17,694) is one January 1997 event. Whether 400 km/s is the long-term
mean at Earth was not settled from a source in the talk. A third option
was added: source a typical speed first, then apply the turn.

**Tony:** "Unturned until we can design the solar wind fetch"

**RULING:** Earth's magnetopause and bow shock stay drawn along the
Sun-Earth line, unturned, in both instruments. Each hover gains one
served sentence saying so: the shape is drawn along the Sun-Earth line,
and the real nose is turned a few degrees toward Earth's motion,
depending on the solar wind's speed. Its source is the Shue and Jelinek
rows (the fits' aberrated frames); it carries no typed number. The turn
is applied when L-314's solar wind fetch is designed. Declined: apply
it now from the 400 (an unsourced speed setting a drawn angle); source a
typical speed first (Tony preferred to wait for the live wind).

## 6. Where each ruling goes

- Decisions to the ledger, by `patch_earth_round1_close_20261016.py`:
  L-330, L-451, L-452, L-450, L-449, L-314, L-413; Where We Are.
- Method to skills, at the build's bump (One Session, One Bump):
  interactive-exhibit (the `source_note` rule; the belts' density field
  under the served-data contract), gallery-cache-builder (the run
  records kept until the loss is explained; the shrink check).
- The work: the build brief.

Record written October 16, 2026 with Anthropic's Claude Opus 5.5.
