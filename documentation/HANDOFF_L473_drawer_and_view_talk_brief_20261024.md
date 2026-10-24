<!-- Doc-Kind: hand | Brief for a talk-only design session: the five findings of Tony's Oct 23 phone look of the view and drawer build, as three design questions; zero code; ends with a records patch. -->
# Brief: the drawer's controls, the count line, and a far orbit's frame

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 24, 2026

Built on orrery 991425bc89b3be21a794b6d748857e7c36b974c7 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b0f50ce52181154b43dcc384d85bcf0461798fde at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both read live with git ls-remote on the morning of Oct 24.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a DESIGN SESSION (talk only, zero code). The session
ends with one records patch for the orrery, nothing for the website.
The build that follows the rulings is a later session's.

Companion to: Tony's run record copy
`documentation/WHERE_WE_ARE_10-23-26_1402_run_record.md` (his six
answers to the Oct 23 phone checklist, lines 538-546, are the primary
record and are quoted below); `documentation/HANDOFF_L472_session_close_20261023.md`
(the Oct 23 build session's close, in Tony's orrery folder and NOT yet
pushed at 991425b); `documentation/DESIGN_L443_slice2_rulings_20261023.md`
(slice 2, designed and waiting behind this). Supersedes nothing.

Skills this session fires, by name: interactive-exhibit (the drawer,
the HUD, the i panel, the Solar System room's framing; its loaded copy
must read 1.21), ledger-and-session-records (the records patch, Where
We Are; 1.22), and provenance-discipline only if a served number is
quoted into a hover (2.34). No code, so no safe-file-editing and no
agentic-pre-test, except for the records patch itself, which
safe-file-editing governs.

A gloss for a session starting cold. The Solar System room is the
website's page interactive.html opened on its default exhibit. Its
drawer is the list of bodies a visitor ticks to draw. A group row
(Comets, Trans-Neptunian objects, and four more) folds open to list
its bodies. The HUD is the set of small labels over the plot: the
object label at the lower left, the grid chip at the lower right
saying how wide a grid square is, the small x-y-z axes above the chip,
and since Oct 23 the count line above those. The i panel is the
information panel each room opens from its i button.

## 1. Where things stand, verified against the repos

The Oct 23 build landed and works. Halley was never drawn wrong: when
the view is zoomed in, the near end of its orbit and its orbit cross
stay in view while Halley does not, and the cross read as the body.
The fix is a count line that says how many ticked bodies are outside
the view. Built with it: See more at the top of the drawer (L-474) and
an About link at the bottom of every i panel (L-475). L-473 (groups
open unticked) was parked on Oct 23 because Tony had said that
afternoon the comet boxes were empty until he ticked Halley. Gonggong
came off the orrery's skip lists and its period is now JPL's, 548.9
years, on both instruments. Slice 2 of L-443 (the objects to the
website) is designed, not built.

Tony's phone look of the three changes, the same night, confirmed
they work and found five things. The five are in his run record and
nowhere else: not on the ledger, not on Where We Are. The close note
of Oct 23 says "four"; there are five. Two owed mechanical steps are
not this session's: the close note's push, and the live check after
the website push at b0f50ce, which the next Daily Run covers.

## 2. What this session does, in order

1. Session start. Pull both repos at HEAD and record the SHAs. Confirm
   interactive-exhibit reads 1.21. Read the run record copy named
   above before writing anything.
2. The talk: section 4's three questions, one at a time, options with
   their costs, Tony converging. Each round should get simpler. The
   fourth item (the About card's return) is small and can be settled
   in a sentence at the end.
3. One records patch, orrery side: the five findings onto the ledger
   under the next free handles (L-476 was the newest at 991425b), each
   ruling in Tony's words, L-473 reopened or closed by what he rules,
   and Where We Are's box rewritten: what changed, do next (the build
   of what was ruled, then slice 2), needs you now. The page is at its
   130-line cap, so a line comes off for every line that goes on, and
   any Settled line removed is kept word for word at the end of the
   session's design record, as the two slice closes did.
4. A design record, `DESIGN_L473_drawer_and_view_rulings_20261024.md`
   or a name the session prefers, holding the rulings, what was
   measured to put each question, and what the build decides by method.

## 3. The five findings, in Tony's words, with what the code does now

Quoted from the run record copy, lines 538-546. Code read at gallery
b0f50ce, not run.

**1. Three controls doing overlapping jobs.** Tony: "now we have three
options, which are a bit confusing, 'all/none' on the top bar and 'See
more' above the drawers. all/none opens or closes all the objects. see
more, just shows all the objects. thoughts? consider using Design for
a better layout. maybe 'See more objects' on the top bar, and 'Select
all objects/Close all objects' on the line below it? but that is
ackward too. realistically only See more and None will be used."

What the code does: the top bar's All / none button
(`sun-drawer-all`, interactive.html line 1228; `toggleAll` in
gallery/solar_system_drawer.js) ticks every tickable body in the room
if any is off, else unticks them all; the Sun is never touched. See
more / See fewer shows or hides the rows the room marks `see_more`
(the groups and Apophis), without ticking anything. Each open group
also has its own "All / none in Comets" button.

**2. Opening a group selects all its bodies.** Tony: "a similar issue
arises in the group drawers. upon clicking comets or tno drawer all
the objects are selected. one then has to remove them all to select
only one. or the top all/none."

What the code does: a group row has two tap targets. Its box (the
`.pick` span at the row's left) runs `ssGroupTick`, which ticks every
body in the group. Its name runs `ssFold`, which only folds the group
open or shut. On a phone the two are a few millimetres apart. On the
afternoon of Oct 23 Tony saw the comets open unticked; that night he
saw them open ticked. Both are what the code does, depending on where
the thumb lands. The question for the talk is not which happened. It
is whether a group row should have two actions at all.

**3. The count line crowds the right side.** Tony: "correct, but now
the right side is getting crowded. would this line fit above the
object label on the left? maybe with a smaller grid line? or a right
justified grid line?" And on item 4 of his checklist: "mostly,
although the aries symbol is partially covered, that is why i am
thinking we could move the ticked body count to the left side above
the object label."

What the code does: `ssOutsideUpdate` (interactive.html near line
4488) writes the line into `#ss-outside`, placed above the grid chip
at the lower right, in the chip's own type (`.ss-outside`, near line
551). Hidden at zero. The Aries symbol is the vernal-equinox mark on
the small axes above the chip.

**4. Sedna's orbit is cut off.** Tony: "the initial view of the sedna
orbit is cut off. it does show the object but not the entire orbit
which is a closed orbit. one has to zoom out to 200 au to see the
whole orbit. when zooming in to 20 au the orbit is out of sight, not
just the object, because the orbit is so wide, and the 1 ticked body
label does appear."

What the code does, and the numbers: the room frames on how far each
ticked body is from the Sun NOW, times 1.2 (`frameOnPosition: true,
frameMargin: 1.2`, Tony's ruling of 2026-10-02, option B "but with a
buffer of 20%"). Sedna is 82.8 AU out today (coverage_index.json, Oct
22 run), so ticking it gives a box reaching about 99 AU from the Sun
in every direction. Its served
orbit (coverage_index.json at b0f50ce: a = 539.58 AU, e = 0.8588,
from JPL on Oct 24) runs from 76 AU at perihelion to about 1,000 AU at
aphelion. A box that holds the whole orbit is about ten times wider
than the one the rule gives, and about 33 times Neptune's orbit (30
AU); in it the inner planets are a few pixels. This is a consequence
of the Oct 2 ruling, not a bug. Note the orrery's own rule is
different: every orrery view opens on the farthest thing drawn, shell
or orbit, plus 20% (Settled, Oct 18-19). The two instruments frame
differently on purpose, and the talk can keep that or close it.

**5. Closing the About card leaves you in the lobby.** Tony: "correct.
but closing it takes you to the lobby. to get back to the render we
need to use the back button <."

What the code does: the link `mountAboutLink` adds to every i panel
(interactive.html near line 2719) opens `index.html#about`, which is
the lobby page with its About card showing. The card's close button
closes the card and leaves the visitor in the lobby.

## 4. The three design questions, with options and costs

None of the options below is a recommendation. The convergence is
Tony's. Where a question is method rather than judgment, the session
says so and does not escalate it.

### Q1. The drawer's tick model (findings 1 and 2)

What a visitor wants, in Tony's words: "realistically only See more
and None will be used." A visitor opens a group to pick a body or two;
clearing everything is the other common act; ticking all 62 bodies is
rare.

- **A. One action per row, and None.** A group row's only tap opens
  it, unticked. Inside the open group its own "All in Comets" button
  is the one way to tick them all. The top bar's All / none becomes
  None: clear everything but the Sun. See more stays where it is. Cost:
  ticking everything in the room takes six taps instead of one; the
  gain is that nothing happens by accident.
- **B. Keep the box, move it.** The group's box stays but moves to the
  row's right end, away from the name, or shrinks to a smaller target.
  Cost: two actions on one row remain, and the phone finding was about
  exactly that.
- **C. Tony's own sketch, as he gave it.** "See more objects" on the
  top bar; "Select all / Close all" on the line below. He called it
  awkward himself. Listed so the talk can start from it and cut.
- Tony asked to "consider using Design for a better layout." If the
  Artifact tool lists a Design type, the session can mock the drawer
  up there in a few minutes for him to judge on his phone. Mode 5: the
  render decides, not the argument.

### Q2. Where the count line sits (finding 3)

- **A. Left, above the object label.** Tony's suggestion, twice. The
  right side keeps the grid chip and the small axes uncovered. Cost:
  the left already carries the object label and, when a text box is
  open, its text; the session should check on the phone that the
  three do not collide at the longest label (the Explorer's are
  longest).
- **B. Right, but smaller.** A smaller or right-justified grid chip
  makes room. Cost: the chip is already at 11px; smaller is hard to
  read on a phone in daylight.
- This is close to method (where a HUD element goes is
  interactive-exhibit's business), so one phone look at A should
  settle it without a long talk.

### Q3. Framing a far closed orbit (finding 4)

The two rulings in play: the Solar System room frames on a body's
distance now plus 20% (Oct 2); the orrery frames on the farthest
thing drawn, shell or orbit, plus 20% (Settled, Oct 18-19).

- **A. Keep the Oct 2 rule.** A far orbit is cut off until the visitor
  zooms out, and the count line already tells them when a body is out
  of view. Cost: a visitor who ticks Sedna sees a dot and a cut arc and
  may not know the arc is one small part of the orbit.
- **B. Frame on the orbit for a single tick, on position for a group.**
  Ticking one body alone fits its whole orbit; ticking a group fits the
  bodies' positions, as now. Cost: two rules for one button, and
  ticking Sedna alone makes the inner planets a few pixels, which is
  the thing the Oct 2 ruling was chosen to avoid.
- **C. Fit the orbit, but with a ceiling.** Frame on the orbit's extent
  up to some multiple of the farthest planet drawn (Neptune's 30 AU),
  and no wider; past the ceiling the orbit is cut and the count line
  speaks. Cost: a number to choose and to justify, and a cut that
  still happens for Sedna, whose aphelion is 33 Neptunes out.
- **D. A second action.** Keep framing as it is; Go To on a far body
  widens to its whole orbit, or a "Fit orbit" control appears while a
  single far body is ticked. Cost: one more control in a drawer the
  talk's first question is trying to simplify.
- What the hover could say either way: the orbit's near and far
  distances are served numbers (perihelion and aphelion follow from
  the served a and e), so a line such as "orbit from 76 to 1,000 AU"
  could tell a visitor what they are not seeing. If the talk wants
  that, provenance-discipline fires: derived from served elements,
  cited to them, never typed.

### Q4, small. The About card's return (finding 5)

Three shapes; the session can propose one and move on: the card's
Close goes back to the room when the visitor arrived from one (the
browser's history, when the page before was interactive.html); or the
card itself opens over the room, inside interactive.html, as the
shared chrome does; or a "Back to the room" link on the card. This is
mostly method and belongs to interactive-exhibit; it needs Tony's word
only if the session cannot pick.

## 5. What the records patch puts on the ledger

- One item for Q1, carrying findings 1 and 2 together and Tony's
  ruling; L-473 (groups open unticked) is closed into it or reopened
  as it, by what he rules.
- One item for the count line's place (Q2).
- One item for framing a far orbit (Q3), naming the Oct 2 and the Oct
  18-19 rulings it reconciles, and the Sedna numbers above.
- One item for the About card's return (Q4).
- Each in Tony's words from the run record, named by file and line.
- Nothing on slice 2: it is designed and its item stands. The build
  order after this session is: the rulings of this talk, then slice 2.

## 6. Tony-action rollup

- **(do)** Before or after this talk: push the Oct 23 close note
  `HANDOFF_L472_session_close_20261023.md` with the next commit; run
  the Daily Run, which covers the missed live check.
- **(decide)** Q1: the drawer's tick model. Q3: how a far closed orbit
  is framed. Q2 and Q4 if the session cannot settle them by method.
- **(do)** At the session's end, run the records patch, move it to
  documentation/, commit and push. No maintenance run is needed.
- **(do)** After the build session that follows: a phone look of
  whatever was ruled, before slice 2.

Written October 24, 2026 with Anthropic's Claude Fable 5.1, in a
coordinating session.
