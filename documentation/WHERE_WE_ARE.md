<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 1, 2026, evening
- Written at orrery c12994d2 plus this session's closing patch, and
  gallery 58dd8f25 plus its small patch.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Distances in the Solar System room now show only the figures JPL's
>   own accuracy allows.
> - Pluto, Uranus and Neptune end at ten thousand km. Jupiter and Saturn
>   end at hundreds of km.
> - Apophis keeps its distance and says JPL's own uncertainty is not yet
>   included.
> - A new check guards this in the website's maintenance run, and it
>   gets its own dashboard button.
> - Your idea is recorded: choose a date, or play time forward, over
>   the range the ticked bodies are trusted for.
>
> **Do next:**
> - *Each body gets its NASA description and link, taken from the
>   orrery's own object list.*
>
> **Needs you now:**
> - *Run the small website patch, then this closing patch in the orrery
>   folder, then commit and push both.*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
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
              card in the lobby. The lobby stays the front page.
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- from the orrery's own
              object list, checked against JPL Horizons.
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 10. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night.

## Right now  **>> UPDATED THIS SESSION**

- The Solar System room shows the Sun, all eight planets, Pluto and
  the asteroid Apophis, where they are when you open it.
- Each text box gives the body's distance in AU and in km, with only
  the figures JPL's accuracy and the page's arithmetic allow.
- The digits change from one visit to the next, because the planets
  move: Pluto moves about 4,300 km further out every hour.
- The info panel has no NASA link for a body yet. That is the next step.
- The drawer's new behaviours have not been built yet.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Each body gets its NASA description and link, taken from the
   orrery's own object list.*
   - It starts with a short design talk about that list.
   - Pluto's row links to NASA's Pluto page.
2. The drawer's new behaviours are built.
   - "See more", "Enter the Sun room", tapping a body to find its row,
     and Home remembering what you ticked.
3. You check the room on your phone and desktop.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- *Run patch_L398_3 in the website folder, then commit and push.*
- *Run the closing patch in the orrery folder, then the maintenance
  run, then commit and push.*

At the next design talk:
- What the orrery's object list should hold for each body, and what
  belongs only to the website.

Not urgent:
- Choosing a date, and animation, your idea of today.
  - The range would follow only the bodies you tick, so leaving out
    Mercury or the Moon gives more time.
  - Talked through once the drawer is built.
- Whether a bare interactive.html link should open the Solar System
  room instead of the Explorer.
  - You said "to be determined".
  - It comes up again after the Sun's numbers are done.

## Where the details are

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-363, L-389, L-396, L-398, L-399, L-400, L-401, L-402.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record:
  `documentation/HANDOFF_L398_distance_figures_20261001.md`
