# Mode 5 test protocol: the HUD fixes and the Studio live card

Built on gallery `fcdbda8f42ceb408c6186136ba48b1e683628b0d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (main)
and orrery `8b9c9d1570402447419d5462b84b88a0ca8095b1` at
https://github.com/tonylquintanilla/palomas_orrery (main).

Type: TEST PROTOCOL. Written before the Earth exhibit build.
Ledger: L-289 (frame HUD), L-288 (Studio live-scene cards).

---

## Why these five and not others

Earth will inherit the frame HUD, the navigation cluster, the drawer, and
the Studio card action. It will not inherit the Sun's text, its colours,
or its shell set. So the trials below are all on the shared parts. A
defect found after Earth ships costs two fixes instead of one; a defect
in Sun-specific polish costs one either way and can wait.

Two things this protocol deliberately does NOT re-test:

- **Stages A, B and C on a phone.** Already passed, 2026-09-03, iPhone,
  both orientations (L-267). What is untested is whether the HUD, added
  after that pass, survives the controls those stages introduced. That is
  trial 4.
- **The nav cluster itself.** Passed with L-267. Trial 4 uses its buttons
  as a way to stress the HUD, not to judge the buttons.

## Before you start

**Confirm you are looking at the new page.** Open the Sun exhibit and
look at the frame note. If it is open on arrival and has an X in its
corner, your browser is serving the cached old page -- hard-reload, or on
the phone close the tab and reopen. Every trial below is meaningless
against the old bytes, and this is the one tell that does not require
trusting a version string.

**Conditions common to all trials.** The live Sun exhibit at
`interactive.html?exhibit=sun`, no query string beyond that, loaded fresh,
arrival camera untouched, drawer as it arrives (outermost shell focused).
Where a trial changes any of that, it says so.

Record the conditions you actually used, not only the verdict. If you
find yourself changing something to make a trial possible -- emptying the
drawer, turning a shell off, rotating first -- write that down. Three
readings were wrong on 2026-09-02 because the starting state was inferred
rather than stated.

---

## Trial 1 -- arrival state, desktop

**Conditions.** Desktop browser, fresh load, nothing clicked, nothing
rotated.

**Look at three things, in this order:**

1. The frame note. It should be closed. -- correct
2. The grid lines. They should be white. Red, green or blue lines mean
   the colour revert did not take. -- correct
3. The spacing chip against the grid itself. Read two adjacent tick
   numbers on any axis and subtract. That difference should equal the
   number on the chip. The old failure was a grid drawing at 0.2 AU
   while the chip read 0.1 AU. -- correct

**What a pass rules out.** All three fixes are ones that only misbehave
at arrival -- the CSS rule, the grid colour, and the dtick the arrival
layout never set. If arrival is clean, none of the three can be wrong
anywhere else, because everywhere else already set them correctly.

---

## Trial 2 -- the frame note, desktop then phone

**Conditions.** Same arrival state, note closed.

**Desktop, with a mouse.** Rest the pointer on the Aries glyph: the note
opens. Move the pointer off the glyph and onto the note itself: it stays
open. Click the source link in it: the link opens and the page still
responds behind it. Move the pointer away from both: it closes. -- apparently correct. however, i do have a question. the triad seems to be oriented 90 degrees (right handed) from the orientation of the grid. this may be correct but it does not read visually. can you confirm the triad orientation? alternatively, the standard orientation with the x axis pointing towards the camera should be the initial view. 

**Phone, portrait.** Tap the glyph: the note opens. Tap anywhere else on
the page: it closes. There is no X button any more. If you go looking for
one, that is the finding. -- reads like the one on desktop

**What a pass rules out.** That the note is still governed by the Sun
chrome rule that was beating `hidden`. It also confirms the two input
paths were separated correctly -- hover on a mouse, toggle on touch --
rather than one being made to serve both. -- correct 

---

## Trial 3 -- the triad follows the camera

**Conditions.** Arrival state. This is the fix that has never been seen
working, because Plotly reports no camera events during a touch rotation
and the HUD now reads the camera itself once per animation frame.

**Desktop.** Drag to rotate. The triad turns with the grid. (This passed
at `fc8d9fb3`; you are re-confirming it survived the rewrite.) -- correct. the triad is slightly off the same visual frame. not significant as long as the alignment is right. 

**Phone, portrait.** Drag with one finger and watch the triad *during*
the drag, not after you let go. It should turn continuously. A triad that
sits still and then snaps into place when you release is the old
behaviour. -- correct 

**Phone, after an interruption.** Switch to another app, come back, and
drag again. The redraw loop only runs while the page is visible, so a
resumed page is the one place a visibility bug would show. A triad frozen
after the switch is a finding. -- correct

**What a pass rules out.** The per-frame camera read, on both input
methods and across a visibility change. Earth inherits this loop
unchanged, so this is the single most transferable trial in the set. -- correct

---

## Trial 4 -- the HUD survives the page's own controls, phone portrait -- what does HUD stand for?

**Conditions.** Phone, portrait, arrival state. Each action below is
followed by the same three checks, so run them as a loop rather than
reading it as five separate trials.

**After each action, check:** triad still present and still tracking; chip
still present; chip still equal to the grid spacing; note still closed.

**The actions:**

- Press `+` twice. Press `-` twice.
- Press Home.
- Open the drawer, focus a different shell, close the drawer.
- Step forward through the stages and back. -- correct on phone and desktop

**Then, one regression check.** Open the Explorer room. It should look
exactly as it did before -- no triad, no chip, no glyph. The HUD is Sun
chrome today, and confirming Explorer is untouched is also the ground for
the decision below about whether it should get one. -- correct. but i question whether this view should carry the home interactive url. eventually it will be repalced by an actual interactive of the solar system. place holder? alternatives?

**What a pass rules out.** That any existing control tears down the HUD
chrome or leaves the chip disagreeing with a grid the control just
changed. This is the trial Earth depends on most, because Earth arrives
into all four of these controls on day one.

---

## Trial 5 -- Studio's New Interactive Card, end to end

**Conditions.** Gallery Studio open at the repo root, on the desktop.

1. Choose **New Interactive Card**. The scene menu is read out of
   `interactive.html`, so first confirm the Sun scene is listed, with its
   note beside the URL. An empty menu means `live_scene_urls()` is not
   finding the scenes. -- correct. I duplicated the explorer view.
2. Enter a title, a placard of a sentence or two, and one source line.
   Press Create. -- correct 
3. It should name an id and report the card landed in Storage. -- correct and confirmed with Editor
4. Open the gallery editor and move the card to its room. -- done. correct.
5. Open the gallery and tap the card. It should open the Sun exhibit at
   the URL you picked. -- pushed. 

**What to watch for.** A live card is a placard with an Interactive tag
and no picture. If it renders as a picture card with an empty image
frame, that is the finding. Also check that the URL the card opens is the
one you chose in step 1, not a default.

**What a pass rules out.** The whole chain from Studio through
`json_converter.add_live_card` into storage, the editor, and the rendered
grid. Earth's card gets made this way, so a failure here blocks the last
step of the Earth build rather than the first.

---

## Decisions to make while you are looking

These are the L-289 items waiting on your eyes. They are judgment calls,
not pass/fail:

- **Triad size.** Too small to read on a phone, too large on a desktop,
  or right.
- **Triad colours.** They are now the only thing carrying axis identity,
  since the grid went back to white.
- **Whether the Explorer room gets the same HUD.** Trial 4's regression
  check is where you see the alternative.
- **The note's touch behaviour.** Tap-to-toggle with no X was a design
  choice, not a constraint. If it feels wrong on the phone, say so.

## Report form

Copy this back, filled in. The conditions matter as much as the verdict.

```
Date:
Device / browser:
Orientation:
Gallery SHA served:
Cache tell (old page ruled out?):

Trial 1 arrival:        pass / fail --
Trial 2 note:           pass / fail --
Trial 3 triad:          pass / fail --
Trial 4 HUD + controls: pass / fail --
Trial 5 Studio card:    pass / fail --

Conditions I changed, if any:

Notes, in my own words (not a summary):

Decisions:
  triad size:
  triad colours:
  Explorer HUD:
  note on touch:
```

Write the notes as you saw them, before you decide what they mean. On
2026-09-02 the observation that mattered was in the same sentence as the
summary that contradicted it.

## Not in scope

Sun-specific text and placards. Per-body colour choices. Corona shell
hover polish. Anything Earth. A finding in these is worth writing down
but does not gate the Earth build.

## One ledger correction for the next session

L-288's entry still reads as though the Studio action is unbuilt -- its
Gap says "design round, then the Studio action" and it was last touched
2026-09-05. The action exists in `tools/gallery_studio.py` at
`fcdbda8f`: `_new_live_card` at line 6031, wired to a New Interactive
Card button at line 3374. The code at HEAD wins; the entry needs the
build recorded and the design question ("does the card carry a still
image?") marked answered -- it does not; a live card is a placard with
an Interactive tag. Trial 5's result closes the rest.

---

Written September 2026 with Anthropic's Claude Opus 5.
