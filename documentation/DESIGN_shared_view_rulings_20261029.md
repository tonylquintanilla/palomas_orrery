<!-- Doc-Kind: design | Rulings from the design talk of October 29, 2026 on a shared link that keeps the view: what the address carries, whose moment it is, how it gets there, and how a date picker follows on the same parameter. Zero code. -->
# Design talk: a shared link keeps the view

Tony Quintanilla, PE | Claude Fable 5.1 (coordinating session) | October 29, 2026, 13:05 to 13:20

Built on orrery b3bfab02 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 963500ca at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). Both read live with git ls-remote on Oct 29, 13:20. The address
behaviour described in section 2 was read from the gallery's
interactive.html at efc4ea8f, the night before; the gallery session
running in parallel (L-399, L-502, L-503) did not touch it.

Type: DESIGN RECORD (zero code). The talk ran from Tony's phone while
the gallery Code session of Oct 29 was building. The item has no
handle yet: the gallery session holds L-504 (the orrery's clock); the
session that closes it, or the next records session, opens this one at
the next free handle and points at this file. Until then Where We
Are's design-talk list carries it by name.

## 1. Tony's ask

Oct 28, 19:54, in chat, after his phone look at 2026 ED138 beside
Pluto: "When we compose a scene, like ED138 and Pluto, and we forward
it, is there a way to retain the scene? Currently what is sent is the
solar system room url, not this specific scene. This could be related
to the scene composer."

## 2. What the address does today (read at gallery efc4ea8f)

- interactive.html reads one thing a visitor would notice from its
  address: `?exhibit=` picks the room (solar-system by default).
- Two more parameters exist, `?edge=` and `?axes=`, Mode 5 testing
  knobs for the Sun's axis lines. They are not state.
- Nothing in the address says which bodies are ticked, where the
  camera sits, or what minute the room shows.
- There is no Share button in the page. "Share" on a phone is the
  browser's own, and it sends whatever is in the address bar. So a
  forwarded scene arrives as "the Solar System room" and nothing more.
- The room draws the scene for the minute it was opened (the line
  under the title, "29 Oct 2026, 04:27 UTC") and does not move forward
  while the visitor looks.

## 3. The rulings, in order, Tony's words quoted

1. **What the address carries: the bodies and the moment.** Of three
   layers offered (A the ticked bodies; B the bodies and the camera
   frame; C the bodies and the minute shown), Tony, 13:07: "I agree A
   and C". The frame (B) waits: a frame set on a portrait phone looks
   different on a wide desktop, and Go To already frames a set of
   bodies well. It can be added later if the fit disappoints.

2. **Whose moment: the maker's.** Tony, 13:07: "kept at the time it's
   made not the recipients time." A link opened a week later shows
   the scene at the minute the maker saw, not the opener's now.

3. **How the moment gets into the address: the address mirrors the
   scene (option 1).** Tony, 13:19: "1". The page writes the ticked
   bodies into the address live, as they are ticked and unticked, and
   writes the minute shown once, when the room opens. The browser's
   own Share then sends the scene; nothing new to press. Option 2, a
   Share button in the page that builds the address only when pressed,
   was declined: more to build, a new button in the chrome, and a
   clipboard fallback needed on desktops without a share sheet.

   Clarified at 13:15, after Tony asked what moment option 1 captures:
   the minute shown under the title, fixed when the room opens; the
   bodies part of the address changes with the ticks, the moment part
   does not. (The coordinating session had said "as the clock runs" in
   an earlier message; that was wrong and was corrected in the talk.)

4. **The shared moment is the first form of choosing a date.** Tony,
   13:15: "in the future we could add a date picker instead of
   'now'?" Claude: yes; once the room reads the minute from the
   address, a date picker is another way of setting the same
   parameter, and sharing then carries the picked date for free.
   Tony, 13:17: "Approved." So the build grows toward the date picker
   (Where We Are, not urgent, item 2) without foreclosing it, and
   animation is the picker moving on its own.

## 4. Settled as method, not asked (Tony did not object when told)

- When the minute came from the address, the line under the title
  adds "as shared", and tapping it returns the room to the visitor's
  now and clears the moment from the address.
- A shared moment outside the days the data covers (88 days either
  side of today at this writing, set by Mercury's trusted span) opens
  the room at now and says so in the text box.
- A shared body the room no longer serves is named as missing in the
  text box; the rest of the scene is drawn.
- The same mechanism applies in every room: the Sun's and Earth's
  drawer rows (shells) are listed the same way the Solar System
  room's bodies are, by their keys.

## 5. The address, as it would read

    palomasorrery.com/interactive.html?exhibit=solar-system&show=2026-ed138,pluto&at=2026-10-29T04:27Z

Two parameter names are placeholders for the build to settle: `show`
for the ticked rows, by key, and `at` for the minute, in UTC. Short,
readable, and typeable by hand.

## 6. What rides on it later

- Compositions (L-489): an author's scene is the same address with a
  name and an interpretation added; the visitor's scene made by
  ticking and the author's scene are then one mechanism. L-486 (a view
  carried into a room) and L-488 (the heliopause) sit under L-489 and
  are not changed by this talk.
- The date picker and animation (Where We Are, not urgent, item 2),
  on the `at` parameter.
- **The served window, when the date picker comes** (Tony, 13:27:
  "Confirmed"): the gate is per body, not one window for the room. A
  body is drawn for a chosen date if that date lies inside its own
  trusted span (the builder already measures one per body; today's
  single 88-day window is the shortest of them, Mercury's). A body
  whose span does not reach the date is not drawn; its drawer row says
  "not drawable for this date" and the text box names it. The room's
  single window retires then. This is an assembler change
  (gallery-assembler fires) and belongs to the date picker's build, not
  the shared link's, whose moment is always within the single window.
  Lengthening the inner planets' spans (more than one recipe per body)
  is a later builder question.
- The frame (layer B), if ever wanted, as one more parameter.

## 7. The build, when it comes

A gallery Code session, after L-503 (the belt on the website) closes;
small. interactive-exhibit fires (the room's chrome, what a room opens
on, the arrival block) and gains a sentence on the address parameters
at its next version. Mode 5: Tony ticks a scene on his phone, shares
the link to himself, and opens it on another device; the same bodies
at the same minute, "as shared" under the title, a tap bringing now.

## 8. Tony-action rollup

- (do) Nothing now. Commit this file with the next orrery push.
- (decide) Nothing pending; every question of the talk is ruled above.

Written October 29, 2026 with Anthropic's Claude Fable 5.1.
