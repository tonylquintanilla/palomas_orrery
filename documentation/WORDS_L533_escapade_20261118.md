<!-- Doc-Kind: hand | The words for ESCAPADE's path (L-533): each craft's description and link, the loiter's sentence in the Solar System room's text box, and the two colours; for Tony's approval before they are final. -->
# ESCAPADE's path: the words, for your approval

Tony Quintanilla, PE | Claude Opus 5.5 (Claude Code) | November 18, 2026

Built on orrery 00c89ef0bf7a4e71f991d58f35299bb6291a5f0c at
https://github.com/tonylquintanilla/palomas_orrery and website
1d3090bc1c8dc95108572e8929a488cd1b19981f at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, plus this
session's uncommitted edits.

From the brief `COORD_L533_escapade_path_brief_20261118.md`, section 7.

**APPROVED, Nov 18, 2026, evening (Tony, in chat): "Approved, with two
changes."** Both made, and the words below are as written in the files:
1. "The loiter sentence starts at launch, not the plan's first whole
   day: 'From its launch on 13 November 2025 until its flyby of Earth on
   7 November 2026, ...' (Gold's 9 November), the launch day read from
   JPL's first position, never typed." The plan now asks JPL for the
   path's first position where a loiter begins on the path's first day
   (`path_plan.first_position`) and serves it on the event as `launch`:
   13 November 2025 for both craft.
2. "The description: 'contributes to the loss of its atmosphere', not
   'drives'. NASA's page says the interaction is 'contributing to the
   planet's atmospheric loss'."
The room prints a date as "14 November 2025". American spelling in our
sentences; NASA's words as NASA wrote them.

## In one look

| # | Where | Proposal |
|---|---|---|
| 1 | The i panel: each craft's description | one of NASA's two identical craft, launched Nov 13, 2025; what the twins will study at Mars |
| 2 | The i panel: each craft's link | NASA's ESCAPADE mission page |
| 3 | The text box: a new loiter sentence | "From its launch on 13 November 2025 until its flyby of Earth on 7 November 2026, it flew wide loops near Earth, around the point called L2." |
| 4 | The colours | Blue blue, Gold gold, the orrery's own |

## 1. Each craft's description (the i panel, and the orrery's hover)

Now (placeholder in the files): "ESCAPADE-Blue, one of two twin
spacecraft launched on November 13, 2025, on their way to Mars (JPL's
data sheet)."

Proposed, the orrery's `mission_info` after its opening "Horizons: -9."
(the website drops that opening and prints the id on its own line):

"ESCAPADE-Blue is one of NASA's two identical ESCAPADE spacecraft,
launched on November 13, 2025. At Mars the twins will fly in formation
to study how the solar wind interacts with the planet's magnetic
environment and contributes to the loss of its atmosphere."

The same for ESCAPADE-Gold, its own name first ("Horizons: -10.").

- Sources, both read this session:
  - NASA's mission page, https://science.nasa.gov/mission/escapade/:
    "ESCAPADE will use two identical spacecraft to investigate how the
    solar wind interacts with Mars' magnetic environment"; "ESCAPADE
    launched from Cape Canaveral, Florida, on Nov. 13, 2025."
  - NASA's article of 2026-11-09,
    https://science.nasa.gov/science-research/heliophysics/nasas-escapade-completes-powered-earth-flybys-now-en-route-to-mars/:
    the twins "will fly in formation", and the article names "atmospheric
    loss at Mars".
- Nothing here says which craft did what. Neither NASA page calls the
  craft Blue or Gold. Which flew past Earth first, and which reaches
  Mars first, is in the plan alone (JPL's positions): Blue's flyby
  2026-11-07, Gold's 2026-11-09; Gold's arrival 2027-09-07, Blue's
  2027-09-09. Say if you want those in the description too; they would
  be typed dates, so I left them out.

## 2. Each craft's link

Now: the mission's site at Berkeley, https://escapade.ssl.berkeley.edu/.

Proposed, and already written: NASA's mission page,
https://science.nasa.gov/mission/escapade/, by the exhibit skill's rule
for a link (NASA's page when it is specific to the thing). Both craft
share it.

## 3. The loiter's sentence (the text box, a new line)

Now: nothing. The box says where the craft is, and that its path is
solid where flown and dashed ahead.

Proposed, after the path sentence:

"From its launch on 13 November 2025 until its flyby of Earth on 7
November 2026, it flew wide loops near Earth, around the point called
L2." (Blue)

"From its launch on 13 November 2025 until its flyby of Earth on 9
November 2026, it flew wide loops near Earth, around the point called
L2." (Gold)

- What a visitor sees, as you asked: a year of wide loops near Earth,
  around L2, before the flyby. The dates come from the plan, so the
  sentence never types one. A loiter with no flyby (none today) would
  read "From <day> to <day>, it flew wide loops near Earth, around the
  point called L1" (or L2).
- NOT "kidney-bean" (your note of Nov 18): NASA's phrase describes the
  loop seen from a frame that turns with Earth, and no room shows that
  view.
- L2 is named in words only, as you ruled: no room draws it yet (L-297,
  the ten Lagrange points, the next round).
- An option, if you want the visitor told where L2 is: add "about a
  million miles from Earth", NASA's own words in the article above
  ("a place in space about a million miles from Earth"). I left it out:
  the room prints kilometres, and the sentence reads whole without it.

## 4. The colours

ESCAPADE-Blue blue, ESCAPADE-Gold gold: the orrery's own colours, in
both the orrery (`constants_new.py`) and the website
(`gallery/assembler/presentation.py`). They're for your eye (Mode 5), at
the phone look.

## What I need

Nothing more: approved with the two changes above.
