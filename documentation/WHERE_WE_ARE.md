<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 1, 2026, afternoon
- Written at orrery 7a47269c plus this session's patch, and gallery
  c48f9a92.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Your notes on this page are recorded in the ledger.
> - The lobby stays the website's front page. The Solar System room's
>   card becomes the top featured card there.
> - The goal now says what the website really does: the orrery's work
>   in a browser, from data fetched from JPL each night.
> - The stray "solar-system (1)" folder is gone. It was most likely a
>   OneDrive copy.
> - Earth's atmosphere is off your list. Its sourcing follows the skill.
> - The orbit markers keep their words. Nothing in the room changes.
>
> **Do next:**
> - *Claude adds JPL's own accuracy to the distance figures, so Pluto,
>   Uranus and Neptune stop showing more figures than JPL knows.*
>
> **Needs you now:**
> - *Run this session's patch in the orrery folder, then the
>   maintenance run, then commit and push.*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
- "<< reworded this session" or "<< new this session" beside a road
  stage means that stage changed.
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

## The road  **>> UPDATED THIS SESSION**

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [NOW]    *The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room.*  << reworded this session
  5. [next]   The Sun's numbers get the same checking Earth's got.
  6. [next]   The Solar System room's card becomes the top featured
              card in the lobby. The lobby stays the front page.
              << new this session
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- from the orrery's own
              object list, checked against JPL Horizons.
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 10. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night.  << reworded this session

## Right now

- The Solar System room shows the Sun, all eight planets, Pluto and
  the asteroid Apophis, where they are when you open it.
- It opens on the Sun and Earth, with Earth's row highlighted.
- The drawer lists every body in order outward from the Sun.
- Each text box gives the body's distance in AU and in km, written out.
- Still to fix: Pluto, Uranus and Neptune show more figures than JPL
  actually knows.
- The drawer's new behaviours have not been built yet.

## The next three steps

1. *The distance figures get JPL's own accuracy.*
   - Claude writes two patches: three accuracy rows for the orrery,
     taken from JPL's own report, and the website change that uses
     them.
   - You run both.
2. Each body gets its NASA description and link, taken from the
   orrery's own object list.
   - Pluto's row links to NASA's Pluto page.
3. The drawer's new behaviours are built.
   - "See more", "Enter the Sun room", tapping a body to find its row,
     and Home remembering what you ticked.
   - You check them on your phone and desktop.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- *Run this session's patch in the orrery folder, then the maintenance
  run, then commit and push.*

At the next design talk:
- Nothing is waiting.

Not urgent:
- Whether a bare interactive.html link should open the Solar System
  room instead of the Explorer.
  - You said "to be determined".
  - It comes up again after the Sun's numbers are done.

## Where the details are

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-363, L-389, L-396, L-398, L-400.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record:
  `documentation/HANDOFF_L363_half2_step3a_20260930.md`
