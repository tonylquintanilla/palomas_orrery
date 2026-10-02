<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 1, 2026, late evening
- Written at orrery feb5e369 and gallery 43993b49, plus this session's
  closing patch.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The orrery's object list now feeds the website.
> - Each body in the Solar System room shows NASA's sentence and a
>   "Read more at NASA" link in its info panel.
> - Small errors found on the way were fixed and listed: two broken NASA
>   links, a number with no source, a stray space, a missing full stop.
> - Apophis now uses the orrery's name for it in JPL, 2004 MN4.
> - Five new tools have dashboard buttons.
>
> **Do next:**
> - *The drawer's new behaviours are built.*
>
> **Needs you now:**
> - *Run the closing patch in the orrery folder, then the maintenance
>   run, then commit and push.*
> - *Reinstall two skills: provenance-discipline and
>   interactive-exhibit.*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
- "<< new this session" beside a road stage marks a change to the road.
- Sections without a mark are as they were.
- The marks are cleared and reset at every session's update, so they
  always mean "new since you last read this."

## The goal  **>> UPDATED THIS SESSION**

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
  4. [NOW]    *The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room.*
  5. [next]   The Sun's numbers get the same checking Earth's got.
  6. [next]   The Solar System room's card becomes the top featured
              card in the lobby. A bare interactive.html link opens
              the Solar System room, and the Explorer gets its own
              address. << new this session
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons. << new this session
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 10. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- The Solar System room shows the Sun, all eight planets, Pluto and
  the asteroid Apophis, where they are when you open it.
- Each body's info panel shows a description and a NASA link.
- Those words and links come from the orrery's own object list. The
  website keeps copies, written by a tool, and a check fails if anyone
  edits them by hand.
- The rest of the orrery's objects are not connected yet.
- The drawer's new behaviours have not been built yet.

## The next three steps  **>> UPDATED THIS SESSION**

1. *The drawer's new behaviours are built.*
   - "See more", "Enter the Sun room", tapping a body to find its row,
     and Home remembering what you ticked.
2. You check the room on your phone and desktop.
3. The Sun's numbers get the same checking Earth's got.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- *Run the closing patch in the orrery folder, then the maintenance
  run, then commit and push.*
- *Reinstall provenance-discipline and interactive-exhibit from the
  repo's skills folder.*

At the next design talk:
- Nothing new.

Not urgent:
- Choosing a date, and animation, your idea of October 1.
  - The range would follow only the bodies you tick.
  - Talked through once the drawer is built.
- The full check of the orrery's object list against JPL Horizons.
  - Its first run lists what disagrees; simple errors get fixed and
    listed, the rest come to you.

## Where the details are

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-363, L-395, L-403.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record:
  `documentation/HANDOFF_L395_objects_connection_20261001.md`
