<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 2, 2026
- Written at orrery b3cfc780 and gallery cfc53490, plus this session's
  two patches.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The Exhibit Store Editor now lists every room, the Solar System
>   room included, and can set what it opens on.
> - The Solar System room's drawer is built: See more, rows that open
>   with a way into the Sun and Earth rooms, and Home remembering what
>   you ticked. Not yet on the website.
> - Your ruling: the room frames where each body is now, plus 20%,
>   not its whole orbit. You also confirmed five smaller calls I had
>   made in the build.
> - The two skills are updated for this work, with a new rule on when
>   a skill gets a new version.
> - The last session's two skill reinstalls are confirmed.
>
> **Do next:**
> - *You check the drawer on your phone, then the desktop.*
>
> **Needs you now:**
> - *Read the room's two new info paragraphs and say if they are right.*
> - *At your machine: two gallery patches, the editor ticks, one orrery
>   patch, then reinstall two skills and the Project's instructions.
>   Each patch prints what to do next.*

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

## The road

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

- The Solar System room shows the Sun, all eight planets, Pluto and
  the asteroid Apophis, where they are when you open it.
- It opens on Earth alone until you tick more in the editor.
- The drawer's new behaviours are built and tested here, not yet on
  the website: See more, rows that open, the Sun's row that cannot be
  unticked, a tap on a body finding its row, and Home remembering.
- The room will frame where each body is now, plus 20%. Pluto's orbit
  runs past the edge until you zoom out.
- Each body's info panel shows a description and a NASA link.
- Those words and links come from the orrery's own object list. The
  website keeps copies, written by a tool, and a check fails if anyone
  edits them by hand.
- The editor can set what any room opens on. It cannot yet change the
  words on the Solar System room's rows, such as Pluto's sentence.
- The rest of the orrery's objects are not connected yet.

## The next three steps  **>> UPDATED THIS SESSION**

1. *You check the drawer on your phone, then the desktop.*
   - Tick and untick bodies, open rows, See more, Enter the Sun room,
     tap a body in the picture, and Home.
2. Whatever your phone shows gets fixed.
3. The Sun's numbers get the same checking Earth's got.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- *The room's two new info paragraphs: right, or reword?*
- *Gallery: run the two patches, in either order. Then open the editor,
  pick solar-system, tick Mercury, Venus and Mars, Save. Then the
  maintenance run, commit and push.*
  - Nothing needs a cache rebuild.
- *Orrery: run the skills-and-ledger patch, then the maintenance run,
  commit and push. Then reinstall interactive-exhibit and
  ledger-and-session-records in Settings > Skills, and replace the
  Project's instructions with the new PROJECT_INSTRUCTIONS.md.*

At the next design talk:
- Nothing new.

Not urgent:
- Choosing a date, and animation, your idea of October 1.
  - The range would follow only the bodies you tick.
  - Talked through once the drawer is built.
- The full check of the orrery's object list against JPL Horizons.
  - Its first run lists what disagrees; simple errors get fixed and
    listed, the rest come to you.
- Whether the editor should also edit the words on the Solar System
  room's rows, such as Pluto's sentence.
  - Today a change to them comes as a patch from a session.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-404, L-405 and L-363.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record: L-404 and the newest note on L-363, in the
  ledger. This session wrote no separate handoff.

===============================================================================

**Tony**: Run record: 

