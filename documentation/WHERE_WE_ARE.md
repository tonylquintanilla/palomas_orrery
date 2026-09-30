<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: September 30, 2026
- Written at orrery 5db8bbe0 plus this session's closing patch, and
  gallery 0f513fd5.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The order of work is settled.
> - First, the Solar System room is finished.
> - Then the Sun's numbers are checked.
> - Then the Solar System room becomes the website's home page.
> - After that: the orrery's other objects, then encounters, then the
>   planets' details.
> - This page is new, and every session now ends by updating it.
>
> **Do next:**
> - *A short design talk about the Solar System room's drawer, one
>   question at a time.*
>
> **Needs you now:**
> - *Reinstall ledger-and-session-records from skills/ to Settings >
>   Skills.*
> - *Replace the Project's instructions in claude.ai with the new
>   PROJECT_INSTRUCTIONS.md (v3.74).*

How to read the marks:
- *Italic* lines are the must-reads.
- **>> UPDATED THIS SESSION** beside a heading means that section
  changed in the latest session.
- Sections without it are as they were.
- The marks are cleared and reset at every session's update, so they
  always mean "new since you last read this."

## The goal

- Paloma's Orrery on the web.
- Anyone can open interactive rooms of the solar system in a browser,
  with nothing to install.
- Built from the same code and the same checked numbers as the desktop
  orrery.

## The road  **>> UPDATED THIS SESSION**

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [NOW]    *The Solar System room becomes the front door: all the
              planets, a drawer to pick them, and a way into each
              body's own room.*
  5. [next]   The Sun's numbers get the same checking Earth's got.
                                                    << moved this session
  6. [next]   The front door becomes the page the website opens on.
                                                    << new this session
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- from the orrery's own
              object list, checked against JPL Horizons.
                                                    << new this session
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.                          << moved this session
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.   << moved this session
 10. [goal]   The orrery's own Python runs in the browser.

## Right now  **>> UPDATED THIS SESSION**

- The first half of the Solar System room is finished.
- It shows the Sun, Earth, Jupiter, Saturn and the asteroid Apophis
  where they are at the moment you open it.
- The plan for the second half is written down and agreed.
- Nothing is being built today.

## The next three steps  **>> UPDATED THIS SESSION**

1. *A short design talk about the room's drawer, one question at a
   time.*
2. Mercury, Venus, Mars, Uranus and Neptune are added to the website's
   data.
   - Claude writes the patch.
   - You run it and rebuild the cache.
3. The drawer and the opening view are built.
   - You check them on your phone and desktop.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- *Reinstall ledger-and-session-records from skills/ to Settings >
  Skills.*
- *Replace the Project's instructions with the new
  PROJECT_INSTRUCTIONS.md (v3.74).*

At the design talk (step 1 above):
- Whether ticking a planet in the drawer also opens its row.
- Whether Apophis keeps a row until the near-Earth asteroids get their
  own design.

Not urgent:
- How wide the Sun's opening view is in the orrery.
- Whether Earth's atmosphere is measured from the equator or from the
  average radius.

## Where the details are

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - Ledger numbers such as L-363 are the handles.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record:
  `documentation/HANDOFF_L363_three_strands_integrated_20260929.md`
