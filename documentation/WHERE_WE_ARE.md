<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 1, 2026
- Written at orrery 10012821 plus this session's closing patch, and
  gallery 432435a8.

> **READ THIS FIRST**
>
> **Changed this session:**
> - All eight planets and Pluto are now in the Solar System room on
>   the website.
> - The room opens on the Sun and Earth. You tick the others in the
>   drawer.
> - Every word a visitor sees in the room is one you approved.
> - Each body's distance is written out in full, with only the figures
>   its accuracy earns.
> - The check comparing the website's data with its settings now
>   covers every body, not just the four with layers.
>
> **Do next:**
> - *Claude adds JPL's own accuracy to the distance figures, so Pluto,
>   Uranus and Neptune stop showing more figures than JPL knows.*
>
> **Needs you now:**
> - *Run this session's closing patch in the orrery folder, then commit
>   and push. Include your fix to the dictionary's duplicated lines.*

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

## The road

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [NOW]    *The Solar System room becomes the front door: all the
              planets, a drawer to pick them, and a way into each
              body's own room.*
  5. [next]   The Sun's numbers get the same checking Earth's got.
  6. [next]   The front door becomes the page the website opens on.
  7. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- from the orrery's own
              object list, checked against JPL Horizons.
  8. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
  9. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 10. [goal]   The orrery's own Python runs in the browser.

## Right now  **>> UPDATED THIS SESSION**

- The Solar System room shows the Sun, all eight planets, Pluto and
  the asteroid Apophis, where they are when you open it.
- It opens on the Sun and Earth, with Earth's row highlighted.
- The drawer lists every body in order outward from the Sun.
- Each text box gives the body's distance in AU and in km, written out.
- Still to fix: Pluto, Uranus and Neptune show more figures than JPL
  actually knows.
- The drawer's new behaviours have not been built yet.

## The next three steps  **>> UPDATED THIS SESSION**

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
- *Run the closing patch in the orrery folder, commit and push.
  Include your fix to the dictionary's duplicated lines.*

At the next design talk:
- Nothing is waiting.

Not urgent:
- A folder named "solar-system (1)" sits in the website's data folder.
  - It looks like a OneDrive copy, and git ignores it.
  - Have a look inside, then delete it.
- Each orbit's small cross now just says "Mercury's orbit" and so on.
  Change the words if you would like others.
- Earth's atmosphere: your note says it depends on the source. Claude
  brings it back when that item is worked.

## Where the details are

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-363, L-392, L-395, L-397, L-398, L-399, L-400.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session record:
  `documentation/HANDOFF_L363_half2_step3a_20260930.md`
