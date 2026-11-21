<!-- Doc-Kind: hand | Design record of the voice talk of Nov 20, 2026 (Tony with Claude Fable 5.2, coordinating session): an encounter as one kind of thing for flybys and destinations, ESCAPADE's Earth flybys the first build; what Tony settled, what the files say differently, and the questions still open. -->
# Design talk: encounters, ESCAPADE's Earth flybys first

Tony Quintanilla, PE | Claude Fable 5.2 (coordinating session) | November 20, 2026, early afternoon, by voice; written up 14:05 to 14:40

Built on orrery c442793a at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery aba9df72 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Nov 20, 14:05.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: DESIGN RECORD (zero code). The items are L-534 (missions by
destination), L-529 (guided encounters) and L-533 (ESCAPADE). The talk
was by voice, and the voice call could not open the files. This record
was written afterwards from the repositories. Section 3 says where the
files disagree with what Claude said on the call. Nothing here is on
the ledger yet; the session's close moves the rulings there.

## 1. Tony's ask

By voice, Nov 20: work on "the rest of the ESCAPADE job", the
destination row and the close-encounter flyby visualization. The
cleanup round goes to Opus in Claude Code.

## 2. What Tony settled in the talk

His words are from the voice transcript, with the fillers taken out.

1. **A destination row is a kind of encounter.** "Maybe this is just a
   type of encounter, not a different kind of visualization."
2. **An arrival is a clean encounter; a long stay is not settled.**
   Juno's years at Jupiter and its passes of the moons: "how would we
   illustrate the rest of it?"
3. **The path is drawn around the centre, and the centre can be a
   moon.** "Not just planet centered, but in some cases, moon centered.
   Artemis II needs a moon centered view."
4. **No date picker.** The window is chosen ahead and the data fetched
   from JPL "as like a preset". This repeats his ruling of Nov 12 on
   L-529.
5. **An animation.** "I really was thinking of an animation", said as
   a design question still to work through, not as a closed ruling.
6. **Everything moves.** "I think everything should move", the Moon
   included.
7. **ESCAPADE's twins together.** "A special case. I think we need to
   treat the twins together": one encounter for Blue and Gold.
8. **Completed encounters only, for now.** "Perhaps we should just
   build completed encounters at this time." The Mars arrival is not
   built yet.
9. **The row's home.** "The right home is the center object of the
   flyby": ESCAPADE's Earth flybys sit in Earth's fold. Claude also
   proposed the dates in the row's name; Tony's answer spoke to the
   home only, so the name is proposed, not ruled.
10. **Destination and purpose.** Tony said the existing encounters
    visualization's info marker and text card already carry them, "at
    the website". See 3.3: the files do not show this for ESCAPADE's
    box, so what he meant is the first open question.

## 3. What the files say

### 3.1 The twins' events, as the orrery's plan holds them

Read from `data/path_plans.json` at orrery c442793a. Every figure is
worked out from JPL by `path_plan.py`; times are UTC; distances are
from the body's centre.

| Craft | Event | Closest | Distance | Speed | The plan's window |
|---|---|---|---|---|---|
| Blue | loiter, Earth-Sun L2 | 2026-03-02 | 506,542 km | | 2025-11-14 to 2026-11-07 10:01; left 2026-11-18 |
| Blue | flyby, Earth | 2026-11-07 10:01 | 8,033.8 km | 10.443 km/s | 08:44 to 11:17, points a minute apart |
| Blue | arrival, Mars | 2027-09-09 00:29 | 3,799.4 km | 4.787 km/s | 2027-09-08 23:09 to 2027-09-09 01:48 |
| Gold | loiter, Earth-Sun L2 | 2026-03-05 | 493,733 km | | 2025-11-14 to 2026-11-09 11:00; left 2026-11-20 |
| Gold | flyby, Earth | 2026-11-09 11:00 | 7,382.6 km | 10.825 km/s | 09:51 to 12:08, points a minute apart |
| Gold | arrival, Mars | 2027-09-07 00:29 | 3,798.8 km | 4.789 km/s | 2027-09-06 23:09 to 2027-09-07 01:48 |

Earth's Hill radius in the plan is 1,483,391 km. A loiter is 60 days
or more within twice that. "Left" is the day the loiter's stretch
ended, the craft passing that distance outbound.

### 3.2 Correction: the plan does not hold an encounter's window

On the call Claude said the plan already knows the window, "the day
the craft enters the body's sphere to the day it leaves". It does not.

- The plan's flyby window is about two and a half hours. It is the
  stretch where the path needs points a minute apart, nothing more.
- ESCAPADE never entered Earth's sphere. It was launched inside it and
  stayed near it for a year. So "the stretch of path inside the body's
  sphere" gives the worked example a window of a year, not a flyby.

The definition in section 4 therefore needs its own rule for the
window. It is open question 3.

### 3.3 Correction: ESCAPADE's box does not name the destination

Read in `interactive.html` at gallery aba9df72. A spacecraft's text
box prints its distance, its path's last day, its loiter sentence and
its dates. The orrery's description goes to the i panel, not the box.
ESCAPADE-Blue's served description reads: "ESCAPADE-Blue is one of
NASA's two identical ESCAPADE spacecraft, launched on November 13,
2025. At Mars the twins will fly in formation to study how the solar
wind interacts with the planet's magnetic environment and contributes
to the loss of its atmosphere."

So L-534's note of Nov 18 still holds: the i panel has the destination
and the purpose, and the box has neither. On the call Claude took
Tony's sentence as closing that miss without being able to check it.
It is not closed on the files.

Tony may have meant something else. The old gallery's encounter
pictures do carry an info marker and a text card, made in the orrery.

### 3.4 Earlier rulings this talk changes

- **Nov 15, 16:07 to 16:16 (L-534).** "add it as a row under mars too
  in addition to the spacecraft drawer"; "Every body. My thinking is
  that the visitor should see Missions as a program and by
  destination."; "There are three paths: paths under spacecraft, paths
  under destinations, encounters at every flyby and destination".
  Points 1 and 8 above fold the second path into the third and build
  only what has happened. The consequence: nothing sits under Mars for
  ESCAPADE until September 2027, and "by destination" has no build.
- **Nov 12, 20:45 (L-529).** "we would also want the viewer to control
  when to move on to the next step after the info card is
  acknowledged." An animation that plays through has to be squared
  with this.

A ruling that is replaced should be replaced knowingly. These are open
questions 2 and 5.

### 3.5 What there is to build on

- **Nothing on the interactive page plays through time today.** Every
  room is drawn at one minute. I found no player in `interactive.html`.
  An animation is the first of its kind there.
- **The old gallery already shows animated encounters**, made in the
  orrery and carded through Studio. Read from
  `gallery/gallery_metadata.json`, among them: "Artemis II - Moon Flyby
  April 2-11, 2026, animated", "Artemis II - Moon Flyby April 6, 2026",
  "Artemis II - Mission April 2-11, 2026", "Psyche - Phobos Flyby
  5-15-26 animated", "Psyche Mission to 16 Psyche 2023 - 2029
  animated". L-529 (Nov 13) has them reviewed and retired once
  encounters live in the interactive site.
- **The orrery animates in steps of an hour at the finest** (its
  window offers "Hours, Days, Weeks, Months or Years"). The plan asks
  for points about 70 to 80 seconds apart at the twins' closest pass.
- **The Moon is served around Earth; the twins are served around the
  Sun only.** The website was built never to change centres by
  subtracting, so the twins have to be asked of JPL around Earth.
- **The live rooms reach 88 days either side of today.** At that
  figure the flybys of Nov 7 and 9 leave the rooms in early February
  2027. An encounter that lasts needs its own stored positions.
- **A saved Scene is an address inside those 88 days**, and the view's
  centre is not in a shared link yet (L-515's leftover).
- **The guide's engine** (`gallery/first_guide.js`): a card that waits
  for one thing, a ring kept on a body, a camera move.
- **Go To on a craft centres on the Sun**, as built (L-479). Tony's
  note of Nov 20: from an Earth-centred view, Go To ESCAPADE leaves
  Earth. An encounter opens centred on its own body, so it does not
  depend on that rule; the note stays its own item.

## 4. The design as it stands

An encounter is a completed pass of a craft by a body. It is stored as
its own package: the positions of the craft, the centre's moons and
anything else in its scene, all asked of JPL around that centre, for a
window chosen ahead. Its row sits in the fold of the body it is
centred on. Opening it shows the scene centred on that body, and the
scene plays through the window with every body moving. ESCAPADE's
twins share one encounter at Earth, the first build.

## 5. Open questions, in the order to ask them

1. **Which card did Tony mean in point 10?** ESCAPADE's box on the
   live page, its i panel, or the old gallery's encounter pictures.
   The answer decides whether his Nov 18 miss is closed.
2. **Are the Nov 15 rulings replaced?** No destination row, and
   nothing under Mars for ESCAPADE until it arrives. If the visitor
   should still see where a mission is going before it gets there,
   that is the craft's box (one line read from the plan's arrival
   event), which is separate from encounters.
3. **The window's rule.** Three candidates. (a) A fixed margin either
   side of the closest passes. (b) The time a craft is inside the
   picture's frame, the frame being the orbit of the centre's farthest
   moon drawn, for Earth the Moon's. (c) The body's Hill sphere, where
   a craft really does come in from outside and leave, as Artemis II
   did at the Moon. Claude's lean is (c) as the rule and (b) for a
   craft that started inside, as ESCAPADE did. The crossing times are
   to be read from JPL before Tony chooses, not estimated.
4. **A still picture first, or the animation at once.** Claude's lean:
   two slices of one build. Slice 1 is the package and its row, drawn
   still: both paths around Earth, the Moon's arc over the window,
   each closest pass labelled with its date. That alone answers Tony's
   miss of the flyby dates, and it puts the Earth-centred data in
   front of his eyes before anything moves. Slice 2 is the player on
   the same package. Tony asked for an animation; this is an order of
   building, not a different end.
5. **How it plays.** Play and pause with a running date is the least.
   Does it stop at each closest pass, show that pass's card, and wait
   for the visitor, as the Nov 12 ruling would have it?
6. **The speed.** The twins drift for days and pass Earth in minutes.
   Played at one even rate, a window of several days gives the closest
   pass a fraction of a second. So either the clock slows near the
   pass, with the running date showing it honestly, or the pass is its
   own closer view at its own rate.
7. **A long stay**, Juno's at Jupiter, and whether a pass of the Sun
   is an encounter at all. Parker's plan has 49 events and
   BepiColombo's 35, most of them passes of the Sun. Not in the first
   build; asked before the second.

For the brief, as method and not Tony's to rule: where an encounter is
defined (the orrery's export, beside the plan's events) and who
fetches it (the website's builder, once); and how a completed
encounter is checked later, because JPL can replace a craft's
predicted path with its measured one for some time after the pass, so
"fetched once and never changes" is too strong.

## 6. Not in the first build

The Mars arrival. Any row under a destination. Long stays. Encounters
for the other 32 paths. The Go To rule. A date picker.

## 7. Tony's answers, in chat, Nov 20, 14:46 to 15:13

Added the same afternoon, after Tony read sections 1 to 6. His words
are quoted as typed.

1. **Question 1, the card (14:46).** "I was saying that from memory."
   So point 10 in section 2 is withdrawn: the box does not name the
   destination, and that stays as it is.
2. **Question 2, Mars (14:46).** "The path ends at Mars. That is
   enough for now." Nothing new goes under Mars, and the Nov 15
   rulings on a destination row wait. "Our part now is the earth
   flyby which can also mention the Mars destination": the flyby's
   card says where the twins are going.
3. **The L2 loiter is an encounter too (14:46).** "And there is also
   the L2 loiter as an encounter." It is the twins' second encounter,
   built after the flyby. Its view is its own question: the loiter
   lasted a year around a point with no mass, and in an Earth-centred
   view that does not turn its loops will not look like NASA's picture
   (Settled, Nov 18).
4. **Question 3, the window and the frame (14:50, 15:01).** Tony, with
   a phone picture of the twins leaving Earth: "Maybe the Hills sphere
   should be the frame?"; then "Yes" to this wording: the body's Hill
   sphere sets the encounter's window and the view it opens on; for a
   craft that loitered at the sphere's edge the window opens at its
   last crossing inward before its pass. For a giant planet the window
   rule holds, and the opening view is settled when such an encounter
   is next, since its moons would be a speck inside its sphere.
5. **The speed is shown (15:07).** "Yes. The orrery has all the data
   frame by frame." Checked: the orrery asks JPL for velocity with
   position, and each frame's hover carries it. The speed shown is
   JPL's, around Earth, not worked out by differencing positions.
6. **Questions 4, 5 and 6, three views (15:13).** "Three works." One
   encounter, three short animations, each on an even clock: the
   whole visit, opening on the Hill sphere, frames about an hour
   apart, each pass marked with its date; Blue's pass close up, a few
   hours around the closest point, frames a minute apart; Gold's pass
   the same. The visitor moves from one to the next when ready, which
   keeps the Nov 12 ruling.

Claude's proposals that rode with "Three works", accepted with the
whole and not ruled one by one:

- The speed sits beside the escape speed at that height in the two
  close views only. At the sphere's edge the Sun's pull makes that
  comparison misleading.
- The player is the plotting library's own play, pause and slider, as
  the orrery and the old gallery use. The builder's first part proves
  one moving scene on the interactive page and reports, because the
  page's boxes and view-centring were built for a still drawing.
- The whole-visit animation is slice 1, the two close passes slice 2.
  This replaces Claude's lean in question 4.
- The words say "powered Earth flybys", NASA's words, not "slingshot"
  or "gravity assist": each pass had an engine burn toward Mars. The
  article is re-read before any word or date is built on it (L-533).
- The sphere of influence is left off the page. It is a calculating
  aid, the site draws JPL's positions and calculates no path, and the
  Hill sphere already does the teaching.

Figures Claude gave in chat from memory, which are NOT sources and go
on no page: a sphere of influence of about 0.9 million km; an escape
speed of about 10 km/s at the twins' closest heights; a window of
about three weeks. The builder reads the crossing times from JPL and
works the escape speed from JPL's figure for Earth's gravity.

For the brief, as method: Earth's Hill radius is held twice, 1,483,391
km in the orrery's plan (worked from JPL) and 235 Earth radii, printed
as 1.5 million km, on the shell the website serves. The brief says
which one bounds the window and which is drawn.

## 8. Still open

- The row's name, proposed with its dates ("ESCAPADE flybys, 7 and 9
  November 2026"), not ruled.
- The words on each view's card.
- Whether Tony first makes the whole-visit view in the desktop orrery
  as a reference picture: Earth at the centre, the Moon and the twins.
- The loiter's view; long stays and passes of the Sun (question 7).
- Tony's note of Nov 20 on Go To from an Earth-centred view.

## 9. Next

The close moves these rulings to L-534, L-529 and L-533 by patch. The
builder's brief is written when its session is next.
