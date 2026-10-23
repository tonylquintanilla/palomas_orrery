<!-- Doc-Kind: hand | Brief for the next working session: close the records of the Oct 22 phone look, then design and build the view fix and the drawer changes it found, before slice 2. -->
# Brief: the view fix and the drawer changes, before slice 2

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 23, 2026

Built on orrery e7dad78fa8f14c2cbe21d8ef3b000fdd22c9ca1f at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery b93072ebe1cc2fa5eded45844f9bb4d7b18c1326 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).
Both SHAs read live with git ls-remote on Oct 23; both match Tony's run record.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BRIEF for a DESIGN SESSION, then a BUILD. This coordinating
session wrote no code and changed no file in either repository.

Companion to: `documentation/HANDOFF_L443_slice1_build_20261022.md`
(the slice 1 build and its phone checklist, section 10) and Tony's run
record copy `documentation/WHERE_WE_ARE_10-22-26_2027_run_record.md`,
which holds his answers to that checklist in his own words. Supersedes
nothing.

Skills the next session fires, by name: ledger-and-session-records
(the records patch, Where We Are), interactive-exhibit (the drawer,
the i panel, the Solar System room's framing), gallery-assembler (a
served page misbehaving with the cause unknown: the Halley render),
safe-file-editing (the patch). Before any of that: the loaded copies
must read interactive-exhibit 1.21 and horizons-orbital-mechanics 1.9.
Both were reinstalled on Oct 22 after the session that bumped them, so
no session has yet confirmed what the account actually serves.

## 1. Where things stand, in plain words

Slice 1 of L-443 (the objects to the website) is live. Fifty of the
orrery's bodies are in the Solar System room, in six groups that fold
open in the drawer. The website's live check at b93072e found all 25
served files byte-identical to the push. All 35 offline checkers
passed. This is verified from the run record's pasted output and from
the repo SHAs, not from anyone's claim.

Tony did the phone look the same night, after the closing patch was
written. His ten answers are in the run record copy named above. Seven
were a plain yes. Three found something, and two more notes followed
in the conversation. None of the five has reached the ledger or Where
We Are yet. They exist only in that run record copy and in the chat
that produced them.

The Where We Are page at HEAD still says "Do next: your phone look."
That is now wrong: the look is done. The next session corrects it.

## 2. What the next session does, in order

1. Session start. Pull both repos at HEAD and record the SHAs. Confirm
   the two skill versions above. Read Tony's run record copy before
   writing anything; his answers there are the primary record.
2. A short records patch, orrery side. It moves the five findings onto
   the ledger, as new items with the next free handles (not assigned
   here), and rewrites Where We Are's box: "Changed since you last
   read this" says the phone look is done and what it found; "Do next"
   becomes the view design talk. The road's stage 10-11 line gains
   "the view fix first; then slice 2." Twenty minutes, no code.
3. The view design talk (section 4). Two Tony rulings have to be
   reconciled before any code is written. Then one phone test to
   confirm the diagnosis.
4. The build: the view fix, and the three drawer changes riding with
   it in the same website patch (section 3, items 2 to 4).
5. Slice 2 (the spacecraft and the 14 comets on open paths) comes
   after, on the corrected view. Slice 2 adds exactly the far bodies
   the view bug mis-draws, which is why the fix goes first.

## 3. The five findings, with what the code at HEAD says about each

Tony's words are quoted from the run record copy. The code notes are
from reading gallery b93072e, not from running it; the render decides.

**1. Halley draws in the wrong place when the view is zoomed in.**
Tony: "the orbit of Halley does not look correct. for 'now' halley is
near its apohelion but the render makes it look like it is near
perihelion approaching the orbit of mars. that's not right for today's
date." His screenshot was at a 1 AU grid. Halley is at 35.01 AU today
(coverage_index.json, Oct 22 run). The prior session confirmed the
position is right whenever the box holds it, and wrong only when the
box is smaller than Halley's distance.

Tony's ruling, in the run record: "Always size the view to the
farthest orbit of anything ticked, so a far body is never drawn
outside the box," and, after the prior session's follow-up, "zooming
moves the camera closer and never shrinks the box below what it has
to hold."

What the code says: ticking already frames on the farthest body
ticked. `ssTick` in interactive.html (near line 4516) and
`ssGroupTick` (near line 4559) both end in `sunApplyVisibility(true,
sunOutermostShown())`, and the room's config carries `frameOnPosition:
true, frameMargin: 1.2`. So the first half of Tony's rule is what the
code claims to do today. The zoom buttons are the other half:
`navFrameZoom` (near line 2878) shrinks the axis range by a factor of
1.6 per tap with a floor of 1e-5 AU, and nothing stops it shrinking
below a ticked body's distance. `gallery/far_lines.js` (L-463) cuts a
LINE to the box when its far point is more than 20 half-widths out,
because a phone's graphics chip draws far points at the wrong place;
its own header says "Markers are not touched." Halley's marker at 35
AU in a 1 AU box is 35 half-widths out. The likeliest diagnosis is the
L-463 failure again, for a marker this time. That is a hypothesis for
the session to test, not a finding.

**2. A group should open with its bodies unticked.**
Tony: "i think that when we open a group the specific checkboxes
should be off not on by default. let the user select the bodies to
plot. if they want all they can do that from the none/all button. the
same should apply to all groups, just as we ask the user to tap see
more to see all the special groups."

What the code says: `ssFold` (near line 4577) only flips the fold and
renders; the comment above `ssGroupTick` says a group's name "folds it
open or shut, and moves nothing." Ticking happens only from the group
row's box (the `.pick` span) or its "all" button. So either Tony's tap
on the phone landed on the box rather than the name, or the fold path
ticks on the phone in a way the code reading does not show. The
session checks which, on the phone, before changing code. If the tap
targets are the cause, the fix may be the row's layout, not its logic.

**3. See more / See fewer belongs at the top of the drawer.**
Tony: "Move See more / See fewer to the top of the drawer, where it's
easier to find." Today the button sits between the ticked rows and the
rest (interactive.html near line 4873). A Mode 5 change: Tony judges
the result.

**4. The About link is missing from the i panels.**
Tony: "i cannot find the link to the 'about' page that one accesses by
tapping the i button on the front page, the lobby. this should be on
every info panel at the bottom." The About card is the lobby's
(index.html, `.about-overlay`, `.footer-about-btn`); interactive.html
has no link to it. This is an edit to the Sun's shared chrome (the i
panel), so interactive-exhibit fires, and the link is one line in
every room's panel, not three copies.

**5. Gonggong's skip from the Horizons list needs its discussion.**
Tony: "Gonggong skipped but needs discussion." Already on Where We
Are's design-talk list and on L-470 (entries the website cannot
serve). The method for the decision is in horizons-orbital-mechanics
1.9 (Which Record Serves a Body). It is NOT part of this session's
build; it is listed here so the records patch does not drop it.

## 4. The design talk: two rulings to reconcile

The zoom buttons carry Tony's ruling of 2026-09-03, written into the
code's own comment: "+/- step the FRAME, not the camera. The Sun spans
six orders of magnitude and a camera dolly cannot travel that -- the
near shells vanish into the perspective long before the far ones
arrive, and the grid labels never change." That ruling was made for
the Sun room and is what makes its shells readable across six decades.

Tony's ruling of 2026-10-22, for the Solar System room: zooming moves
the camera closer and never shrinks the box below what it must hold.

Read literally, the two disagree about what the zoom buttons do. They
were made for different rooms and different problems, so the talk's
first question is whether the rule is per room. Three shapes to put in
front of Tony, each with its cost:

- **A. Per room.** The Sun and Earth rooms keep frame zoom as it is.
  The Solar System room's zoom-in has a floor: the farthest ticked
  body's distance times the margin. Below the floor the button does
  nothing. Cost: with Halley ticked, nobody can zoom in to see the
  inner planets at all. With Sedna ticked (at 83 AU today) the inner
  planets are a few pixels, which is the prior session's warning.
- **B. Hybrid.** Frame zoom down to that floor, then the camera moves
  closer. Cost: two mechanisms on one button, and the grid labels stop
  changing once the camera takes over, which is the thing the Sept 3
  ruling was protecting against.
- **C. Treat a far marker as far_lines.js treats a far line.** Leave
  the zoom as it is. A marker more than FAR_FACTOR half-widths outside
  the box is not handed to the chip; the HUD says how many ticked
  bodies are outside the view. Cost: a ticked body can be invisible,
  which Tony's Oct 22 ruling says he does not want. Gain: one rule for
  lines and markers, the Sept 3 ruling untouched, and the smallest
  change.

None of these is a recommendation. The convergence is Tony's. Each
round should get simpler.

**The one phone test before building,** whichever shape wins: tick
Halley with Neptune drawn, confirm it sits at 35 AU; then zoom in by
the buttons to a 1 AU grid and watch where Halley's marker goes, and
whether the orbit line's visible part is the perihelion end cut at the
box. If the marker jumps to the box edge, the diagnosis is confirmed
and the fix is in how a far marker is handed to the chip. If it
stays off-screen and only the cut orbit line misleads, the fix is in
what far_lines.js leaves showing, and Tony's rule still applies but
the cause is different. gallery-assembler's rule applies here: do not
hand Tony a test without having loaded that skill.

## 5. What the records patch puts on the ledger

One item per finding, each a line or two, handles assigned by the
patch from the next free number (L-471 was the last used on Oct 22):

- The view fix: Tony's two-part rule verbatim, the Sept 3 ruling it
  has to be reconciled with, the three shapes above, and the phone
  test. Open; the design talk closes its design half.
- Group rows open unticked: Tony's words; the code-vs-render question
  to settle on the phone first.
- See more at the top of the drawer. Mode 5.
- The About link at the bottom of every i panel.
- Gonggong: no new item; a line on L-470 (entries the website cannot
  serve) saying the discussion is still owed.

Also on the ledger already and not touched by this brief: L-471 (a
delivered patch is final), waiting for safe-file-editing's next bump;
the six comet warnings in the builder (a hover's period around the
barycentre while the orbit is drawn around the Sun), recorded on
L-443 for a later look; L-461 (pull matches push), to build with
slice 2.

## 6. Tony-action rollup

- **(do)** Save this brief in the orrery's documentation/ folder, then
  commit and push. No maintenance run is needed for it.
- **(do)** At the next session's start, open it in the chat as the
  first upload beside your run record copy.
- **(decide)** At the design talk: which of A, B or C, or a fourth
  shape of your own, and whether the rule is per room.
- **(decide)** Whether the three drawer changes ride in the view-fix
  patch or go as their own small patch first. Riding together is one
  run for you; separate is easier to judge one at a time.
- **(do)** The one phone test in section 4, when the session hands it
  to you, before any code is written.

Written October 23, 2026 with Anthropic's Claude Fable 5.1, in a
coordinating session linked to Tony's computer.
