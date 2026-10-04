<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 3, 2026, end of session
- Written at orrery fd508f9c and gallery 52659e04.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The Sun room's galactic tide is now drawn in the galaxy's plane,
>   sparse at that plane and at its poles. Its words are new, and you
>   saw them right on the phone.
> - Every skill's header is now checked the way Settings reads it.
>   Three were broken; one of them had been cutting
>   provenance-discipline's description short.
> - The sources for the Sun's distance cards are read, and you ruled on
>   how to show the ones given as a range.
> - From your phone afterwards: the Galactic Plane toggle's words,
>   what Home does, and the lobby's new Solar System card.
>
> **Do next:**
> - *Build the Sun's distance cards so every number prints at its
>   source's figures.*
> - *Then the Galactic Plane toggle you asked for.*
>
> **Needs you now:**
> - *Nothing. The skills and instructions were reinstalled and checked
>   on October 3.*

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
  perhaps play time forward.

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
              << new this session: begun. The 43 drawing numbers are
              sorted, the galactic tide is redrawn, and the distance
              cards' sources are read; the build is next.
  6. [next]   The Solar System room's card becomes the top featured
              card in the lobby, full width with a picture of the
              room, and first behind the Solar System door too.
              << new this session: its look chosen on October 3.
              A bare interactive.html link opens
              the Solar System room, and the Explorer gets its own
              address.
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

- The galactic tide is live, tilted into the galaxy's plane. It is
  drawn between 20,000 and 100,000 AU, the outer Oort cloud's edges.
- Fourteen other Sun cards print their km with every digit, such as
  299,195,741,400 km for 2,000 AU. The rows behind them do not yet say
  how many figures their sources give.
- The maintenance run now fails if a skill's header would be refused
  by Settings: 20 checks where there were 19.
- The Solar System room and its drawer are as they were: Home still
  shows no visible change when it falls back to an earlier body.

## The next three steps  **>> UPDATED THIS SESSION**

1. *The Sun's distance cards, built:*
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
   that should say 1.2, and your second look at an opened row.
   Then Home as you settled it on October 3, and the lobby's new
   Solar System card.

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

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-406 (the tide), L-407 (skill headers), L-405
    (done), and the newest notes on L-371 (the Sun's numbers).
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record:
  `documentation/HANDOFF_L406_L407_L371_session_20261003.md`
