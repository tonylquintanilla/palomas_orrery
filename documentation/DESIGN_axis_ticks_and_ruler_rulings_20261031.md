<!-- Doc-Kind: hand | Design record of the Oct 31 talk on the scale marks in the website's rooms: tick marks on the three axis lines, a short ruler in place of the grid chip, Plotly's edge numbers turned off, in every room. Tony's rulings and the one rule; zero code. -->
# Design record: the axis ticks and the ruler (every room of the website)

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session, talk only) | October 31, 2026, 17:12 to 18:04; refined to 20:43; the 20:43 ruling restored November 2, 2026

Built on orrery 341c168d7ab53f5bbd949914ef12750392c35a36 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery c1c578f57f812aa0dcc0f1fec45bab43e7826bd0 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 31, 23:17 UTC. No code
was changed in this talk. The pictures are on a Claude Design canvas,
"Grid labels, opening view" (six artboards over Tony's screenshot of
the Solar System room's opening view, Oct 31, 17:11); the record is
this file, since the canvas is not in a repository.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN SESSION record (zero code). It opens a ledger item at the
next free handle when its brief is written (L-505 at 341c168d; the
shared link's item is queued for the same handle, and whichever brief
is written first takes it). The build is a gallery Code session of
its own, after the week of mornings that follows the nightly run's
first week (Tony: "after the week of mornings unless you want it
sooner" was offered; he did not ask for sooner).

## 1. What prompted it

Tony, Oct 31, 16:58, at his phone look of the belt's row: "the grid
box does not clearly show the grid line labels. the grid AU label
helps. however, we had discussed labeling the inside coordinate lines
not just the edges. let's discuss this option."

The history, from L-289: labels on the inside lines were BUILT on Sept
5 (tick values on all twelve edges of the box) and FAILED Tony's phone
look the same day: scattered, floating beside the camera on nothing,
gone on zoom-out. The cause was structural: text placed as points in
the scene is scenery, shrinking with distance and clipped at the box.
The redesign that day is what the rooms show now: the grid chip
("grid 0.5 AU"), the triad, and Plotly's own tick numbers on the box
edges, which sit off-screen at arrival because the frame is full on
purpose.

## 2. The options shown (the canvas, left to right)

1. Today: chip, triad, edge numbers.
2. Numbers at each grid step along the three axis lines through the
   Sun, as page chrome (projected like the triad; fixed size; hidden
   behind the camera). Twelve labels in the opening view.
3. Plotly's edge numbers, larger and in the axis colour. Helps only
   when a box edge is in view.
4. Option 2 thinned to whole AU, plus option 3.
5. Tony's ask (17:37): no new text; a short tick across each axis line
   at every grid step and a longer one at a major step, in the axis
   colour, in the scene.
6. Tony's ask (17:45): option 5, and the chip replaced by a short
   ruler with the minor and the major tick labelled.

## 3. Rulings, Oct 31

**R1. Tick marks on the three coloured axis lines, in every room**
(17:50, "Confirmed"; 17:57, "This method would apply to all scenes in
the website"). A mark on the axis line at every grid step and a larger
one at every second step, in the axis colour, drawn in the scene so
they turn with the axes. They re-space with the grid on zoom, as the
grid does. Refined 20:20 and 20:43: the marks are MARKERS, not line
segments, and the marker is the X; see section 4.

**R2. The major tick is twice the minor** (18:02 to 18:04). Tony: "On
a map ruler it depends on the number of ticks drawn ... But we are
drawing only two, in this example, 0 (unlabeled), 0.5 au and 1.0 au.
But it could be any scale, 0, 0.2 au, 0.4 au. Or 0, 50 au, 100 au."
Claude had proposed the next power of ten above the step (1, 10, 0.1
AU) at the cost of a varying tick count; Tony's rule keeps one shape
at every zoom, and the ruler's label carries the value. "Confirmed",
18:04.

**R3. The grid chip becomes a short ruler, on a transparent
background** (17:50: "with a transparent background instead of grey.
So it does not obscure the website url"). Three marks: 0 unlabelled,
one step, two steps; the last two labelled with whatever the grid
makes them. Refined 20:22 (Tony: "shouldn't the ruler use the same
style"): the ruler's marks are the SAME SYMBOLS as the axes', a small
x at one step and a larger x at two steps on a short line, in neutral
white since the key stands for all three axes; the 0 end is unmarked.
The labels: "0.5" and "1 AU" at a
0.5 AU grid, "0.2" and "0.4 AU" closer in, "50" and "100 AU" far out.
The ruler is a KEY to the marks on the axes, not a screen length (a
perspective view has no one length); it re-labels with the grid on
zoom, as the chip does today. It sits where the chip sits, clear of
the site's address below it.

**R4. Plotly's numbers on the box edges are turned off** (17:54: "with
a ruler, the edge labels are actually obstructive so remove"). The
grid lines stay. The edge numbers are one layout setting for all three
axes, so every room loses them in the same build that gives every room
the ticks and the ruler; no room is left with a grid and no scale.

## 4. What rides inside the build (method, not rulings)

- The chip opens a note today explaining what an AU is
  (interactive-exhibit 1.27, "the grid chip's AU note"); the ruler
  inherits that tap, so the note does not vanish with the chip.
- The i panel's frame note gains a sentence saying what the ticks and
  the ruler are.
- Whether the Explorer page, at its own address, draws the same frame
  and so gets the ticks and the ruler too is a fact the session reads
  from the code; if it does, it is in the build (R1: every scene).
- Tick length, line weight, label size: Tony's phone (Mode 5), as on
  Sept 6.
- THE RULER'S LABELS CARRY THE UNIT ON BOTH, as Tony wrote them
  (18:02: "0 (unlabeled), 0.5 au and 1.0 au"): "0.5 AU" and "1 AU".
  The canvas's mockup dropped the unit from the minor; the record
  follows Tony's words, and the phone may shorten it if it crowds.
  (Raised by GPT's review, Oct 31, 19:33; already Tony's.)
- HOW A TICK IS ORIENTED IN THREE DIMENSIONS is an implementation
  choice, settled against the render, not a ruling (GPT's review,
  19:33: a mark "across" an axis has a whole plane of directions, and
  the ticks must read as scale marks, not as pieces of grid). The
  coordinating session's suggestion for the brief: the x and y ticks
  lie in the plane of the orbits, each across the other axis, and the
  z ticks lie along x, so that from above the floor reads as a ruler;
  the session reads how the triad and the axis traces are built first,
  and Tony's phone judges.
- From Gemini's review (Tony's relay, Oct 31, 20:17), four
  implementation notes, none a ruling:
  - A FLAT TICK VANISHES EDGE-ON. Ticks lying in the plane of the
    orbits foreshorten to nothing when the scene is viewed along that
    plane, the very view for comparing orbital tilts. Gemini's
    candidate was a small cross; Tony, 20:20: "crosses can be confused
    with the hover crosses. how about small dots the same color as
    the axes, as markers?" Dots were drawn, then set aside at 20:34:
    "the dots can get confused with the celestial objects", and the
    marker table in orrery-coding-conventions says the same: circles
    are reserved for bodies. Triangles are not in Plotly's 3D palette
    (eight shapes: circle, circle-open, cross, diamond, diamond-open,
    square, square-open, x). Of the two shapes the table does not use,
    the filled square and the x, drawn side by side on the canvas,
    RULED 20:43: "let's go with X then. X is simply a graphical marker
    with no render significance like a + while a filled square might
    be used for a render at some point." So (R1 refined): the ticks
    are X MARKS (Plotly marker symbol "x"), in the axis colour, a
    small x at every grid step and a larger x at every second step,
    drawn as markers in the scene with no hover and no legend group,
    and the ruler's key carries the same two. A marker faces the
    screen at a fixed pixel size, so it never foreshortens and never
    shrinks with zoom, and it sits on the axis and turns with it. The
    marker table gains a row: x, "coordinate ticks (the axes' scale
    marks and the ruler)", with the cross row then reading "info
    markers" alone; that is orrery-coding-conventions' next version,
    an orrery session's. Sizes: Tony's phone, with the low camera
    angle on the Mode 5 list.
  - TWO MORE CHECKS MUST KNOW THE TICKS ARE FRAME, NOT FEATURE:
    `documentation/smoke_drawn_ends.js` (every drawing's near and far
    end held to a served row, L-460) and `sweep_collapsed_features.py`
    (every served feature group classified, L-300), beside the three
    named above. The tick traces are named to them as the axes are.
  - CONTRAST OVER BRIGHT SHELLS. With no background, light ruler text
    and lines over the corona or a dense cloud can disappear; a thin
    dark halo (text-shadow) keeps the background clear and the text
    readable. Mode 5.
  - THE UNIT FOLLOWS THE ROOM. The ruler's two labels and its tap note
    print whatever unit that room's grid chip prints today; the session
    reads each room's chip before building (the Sun room's has read AU
    since Sept 5; the Earth room's is read, not assumed).
- The drawer-order, hover-budget and label-words checks must not see
  the ticks as features: the tick traces carry no hover and no
  legendgroup the drawer reads, as the Sept 5 edge-label trace did
  (L-289's build note); the headless recipe (interactive-exhibit 1.29)
  walks the rooms after.
- interactive-exhibit's next version carries R1 to R4 as the frame's
  rule, replacing its grid-chip sentences; that bump is an orrery
  session's, after the build.

## 5. Tony-action rollup

- (do) Commit this record with your next orrery push.
- (decide) Nothing. R1 to R4 are ruled; the rest is the session's.

## 6. Added November 2, 2026: the 20:43 ruling restored

The copy of this record committed on Oct 31 at 20:45 (dc85f372, 171
lines) carried the 20:20 refinement, dots, and not the 20:43 ruling,
x marks. The session that took the ruling wrote it into its own copy
and placed that copy in Tony's folder from a path it had already used
twice that evening; the tool reported success, and the bytes that
arrived were the earlier version. The session read back the size of
its own copy, not the folder's. Nothing else recorded the ruling: the
Oct 31 night handoff only points at this record. So the L-505 brief of
Nov 1 was written from the committed copy and said a plain circle, and
the gallery session of Nov 1 built dots (gallery 7895021). Tony, Nov 2,
08:07, on his phone look: "i thought we were using X not dot."

Restored here, Nov 2, by the coordinating session (Claude Fable 5.1,
orrery fd3551c0 and gallery b7ddf775 read live), from the Oct 31
session's own transcript, word for word: R1's refinement line, the
ruler's same-symbols sentence, and section 4's bullet. The correction
to the build is `COORD_L505_gallery_x_marks_brief_20261102.md`. The
lesson is on the coordination handoff of Nov 2: a file placed in Tony's
folder is read back by size from the folder listing, and a ruling that
changes a record is also stated in the same session's handoff, so a
lost placement has a second store.

Written October 31, 2026, section 6 added November 2, 2026, with Anthropic's Claude Fable 5.1.
