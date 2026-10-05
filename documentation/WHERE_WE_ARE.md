<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 4, 2026, end of the day's third session.
- Written at orrery 41c1ca7a and gallery e7ef96eb.
- This session was a ledger sweep: no code changed. A Fable session
  ran its own sweep beside it, and both were checked against the code.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Earth's old items are now one ordered list, in the order you
>   confirmed. They come before the rest of the Sun's list.
> - Seven ledger items closed because their work was already done: the
>   licenses, the skill-header check, the galactic tide, the
>   magnetotail's length, Earth's magnetosphere model, Earth in the
>   website's builder, and the magnetosphere's unused tooltip copy.
> - The four Earth numbers the scanner calls uncited are cited. The
>   scanner looks one line short of one source, and doesn't count a
>   written "declared" reason. That is now its own item.
> - Your notes on this page are in the ledger, so they survive this
>   rewrite.
> - Patches now convert Windows line endings to the standard LF and say
>   so, as you remembered the rule. The patch skill had said both.
> - The 22 older files stored with Windows line endings are converted
>   to LF, in a commit of their own. That item is off the backlog.
>
> **Do next:**
> - *Your ruling on the inner belt's wording, then Earth's orrery
>   patch.*
>
> **Needs you now:**
> - *Run the ledger patch, then the maintenance run, and push.*
> - *Reinstall the patch skill and update the Project's instructions.*

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
- Saved data covering one orbit of each body is enough, as you decided.
- Within that range, a visitor will be able to choose a date, and
  perhaps play time forward.

## The road  **>> UPDATED THIS SESSION**

  1. [done]   The Sun's room is live on the website.
  2. [done]   Earth's room is live, with every number traced to its source.
  3. [done]   The numbers come from one place: the orrery feeds the
              website, and nothing is typed twice.
  4. [done]   The Solar System room becomes a second way in: all the
              planets, a drawer to pick them, and a way into each
              body's own room.
  5. [NOW]    *Earth's old items are finished, in the order you
              confirmed.* << new this session: the first of the
              room-by-room ledger cleanups you asked for. Each room's
              old items are grouped by the files the work opens, and
              only what the room shows is in scope.
  6. [next]   The Sun's numbers get the same checking Earth's got: the
              Sun's list, from its opening view. << moved this session:
              after Earth's list. The distance cards are done.
  7. [next]   The website's checks get a short list of their own, so a
              new room or a moved front door can't break unnoticed.
              << new this session.
  8. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address. The lobby's wide
              Solar System card, its first half, is done.
  9. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
 10. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
 11. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 12. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- Earth's magnetosphere is drawn from published models in both the
  orrery and the website.
  - One question was never answered: because Earth moves along its
    orbit, the solar wind hits it slightly from the side, so the nose
    should turn about 4 degrees. Neither drawing does, and neither says
    so. It now waits with live solar wind, which sets that angle.
- The website draws Earth's geocorona, its faint hydrogen halo. The
  orrery only mentions it in a hover; drawing it is Earth's list, item 1.
- The website's magnetotail hover already prints the 220 Earth radii
  the spacecraft reached.
- The website does not draw Earth's magnetic dipole cone; the orrery
  does. Whether the website should is now a design question.
- On the Sun: the distance cards are built on both sites, and the
  Roche limit is drawn at 3.45 solar radii, described as "about 3".
- The ledger holds 241 open items after the seven closes.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Your ruling on the inner belt's wording.*
   - It says "where the measured particle flux peaks".
   - Once you rule, the new wording travels in both patches below.
2. Earth's orrery patch, then your look on the screen.
   - The geocorona drawn as its own shell.
   - Earth's tilt read from the stored number in five places.
   - The atmosphere shells measured from the same radius as the crust.
3. Earth's website patch, then your look on the phone.
   - The inner belt's wording.
   - The saved Earth test scene re-recorded from today's data.
   - The collapsed-features check added to the maintenance run. It
     passes today, so it cannot block a push.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- Run the ledger patch, then orrery_maintenance_run.py, and push.
- Reinstall safe-file-editing in Settings > Skills, and replace the
  Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.80.

At the next design talk:
- The fuzzy outer corona, designed together with the dust cloud.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays in the centre, as you ruled.
  If it can't, no arrow.
- Earth's design talks, the belts' shape first.

Decisions from the Fable sweep, one at a time when you're ready:
- Whether items inside an ordered list need RICE scores at all.
- A handful of scores it proposes.

Not urgent, in your order:
1. The full check of the orrery's object list against JPL Horizons.
2. Whether the editor should also edit the words on the Solar System
   room's rows.
3. Choosing a date, and animation.
4. The scattered disk, with the Kuiper belt in the Solar System room.
   It is not the fuzzy boundary idea: the disk is a population of icy
   bodies, the fuzzy boundary is a way of drawing an edge. When the
   disk is designed, its edges would likely be drawn that way.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-413 (Earth's list), L-414 (the scanner's window),
    L-415 (line endings), L-133 (the 22 older files, converted and closed).
    Closed: L-409, L-407, L-350, L-406, L-305, L-234, L-383.
  - The Sun's list: L-412.
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session records:
  `documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md`,
  and Fable's sweep, `documentation/LEDGER_SWEEP_review_20261004.md`
