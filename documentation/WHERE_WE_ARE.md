<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 4, 2026, end of the lobby-card session -- **Tony**: see notes with -- 
- Written at orrery a841ab6e and gallery d4b408e6.
- The Sun's distance cards are still being built in the other session,
  which updates this page when it ends.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The lobby now opens with a wide Solar System card at the top of
>   Featured: a picture of the room, "The Solar System, live", and a
>   sentence. You checked it on the phone, sideways and on the desktop.
> - The same card comes first on the Solar System door's page.
> - The lobby's doors no longer count rooms under construction, and the
>   empty "solar_system" room is gone.
> - The card's picture is drawn from the room's own data, zoomed to the
>   inner planets, with no grid, as you asked.
>
> **Do next:**
> - *Finish the Sun's distance cards: the website side, in the other
>   session.*
> - *Then the Galactic Plane toggle you asked for.*
>
> **Needs you now:**
> - *Nothing.*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
- "<< new this session" beside a road stage marks a change to the road.
- Sections without a mark are as they were.
- The marks are cleared and reset at every session's update, so they
  always mean "new since you last read this."

## The goal

- Paloma's Orrery on the web.
- The website does what the desktop orrery does, in the browser, from
  data fetched from JPL each night, so a visitor never waits on JPL.
- Anyone can open it, with nothing to install.
- Built from the same code and the same checked numbers as the desktop
  orrery.
- The one real limit: the browser can show only the dates the saved
  data covers.
- Within that range, a visitor will be able to choose a date, and
  perhaps play time forward. -- we determined that one orbit would work. 

## The road  **>> UPDATED THIS SESSION**

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [NOW]    The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room. Built and on the website. Home was
              settled on October 3; it is built next.
  5. [NOW]    *The Sun's numbers get the same checking Earth's got.*
              The 43 drawing numbers are sorted and the galactic tide
              is redrawn. << new this session: the distance cards'
              orrery side is pushed; the website side is being built.
  6. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address.
              << new this session: the first half, the lobby's wide
              Solar System card, is done and on the website.
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 10. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- The lobby opens with the wide Solar System card. Its picture shows
  the Sun and the four inner planets where they were at noon on
  October 4; the room itself always shows now.
- The galactic tide is live, tilted into the galaxy's plane. It is
  drawn between 20,000 and 100,000 AU, the outer Oort cloud's edges.
- The Sun's distance cards: the orrery side is pushed. Until the
  website side lands, the Sun cards print as before, with every digit.
- The Solar System room and its drawer are as they were: Home still
  shows no visible change when it falls back to an earlier body, and
  with the phone sideways an opened row does not fit in the drawer.

## The next three steps  **>> UPDATED THIS SESSION**

1. *The Sun's distance cards, finished on the website,* in the other
   session:
   - Each distance row gets its source's figure count, so the km print
     at that count.
   - Where a source gives a range, the card draws one end and says so,
     as you ruled: for example "Thought to lie between 2,000 and 5,000
     AU; drawn at 2,000."
   - The Heliopause moves to 121 AU, and Gravitational Influence to
     0.65 parsecs: the Sun's Hill radius, calculated.
2. *A Galactic Plane toggle in the Sun room, your idea:* a faint ring
   in the galaxy's plane and the galaxy's pole axis, so the tide's
   tilt and its X can be seen at a glance. You look for the X then.
3. The drawer's small fixes: the info panel's bullet lists, the 1.1
   that should say 1.2, and an opened row made to fit with the phone
   sideways: its Enter button on the name's line, as you chose.
   Then Home as you settled it on October 3.
-- my notes in documentation should not cause a patch to fail. 


## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- Nothing.

At the next design talk:
- Moving the highlighted row to the top of the list.
- An arrow from GO's text box to its body.

Not urgent, in your order:
1. The full check of the orrery's object list against JPL Horizons.
2. Whether the editor should also edit the words on the Solar System
   room's rows.
3. Choosing a date, and animation.
4. New: delete the folder "data/solar-system (1)" in your gallery
   copy, with OneDrive paused, as you did on October 1. Your
   maintenance run found it again. Git ignores it, so it does no harm
   meanwhile.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-363 (the lobby card) and a note on L-216 (the
    stray folder).
  - The other session: L-371 (the Sun's numbers), L-406 and L-407.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session records:
  `documentation/HANDOFF_L363_lobby_card_session_20261004.md`, and
  `documentation/HANDOFF_L406_L407_L371_session_20261003.md`
