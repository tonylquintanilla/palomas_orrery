<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 5, 2026, end of the session held mostly from
your phone.
- Written at orrery d9f47a87 and gallery ed48d078, after your runs.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Earth's orrery patch is in: the geocorona has its own shell,
>   Earth's tilt is said in words where "23.4" was typed, and the inner
>   belt's words say "near the measured proton flux peak", as you ruled.
> - The atmosphere and low Earth orbit heights stay measured from the
>   equatorial radius, as you clarified. Notes on those rows now say why.
> - Every step of both maintenance runs gets a dashboard button: eleven
>   new ones.
> - The skill check now enforces Anthropic's written limits on a
>   skill's name and description.
> - Six long skills now open with a list of their contents, kept true by
>   that check, and their old history moved to its own file.
>   provenance-discipline's rules now come before its long procedures.
> - The check of the object list against JPL Horizons has its own
>   handoff, for a fresh session.
> - Your notes in this page, the handoffs and the ledger are protected
>   by a written rule now: a patch checks only the lines it edits.
>
> **Do next:**
> - *The website patch for Earth, or the Horizons design round, in the
>   order you choose.*
>
> **Needs you now:**
> - *Look at the "Ecliptic Coordinates (J2000)" box at the plot's left:
>   its teal-circle line. The rest of your look was correct.*
> - *Run the skill patch, reinstall ledger-and-session-records, and
>   replace the Project's instructions with v3.82.*

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
              confirmed.* << this session: the orrery patch is built;
              the website patch and the design talks remain.
  6. [next]   The Sun's numbers get the same checking Earth's got: the
              Sun's list, from its opening view.
  7. [next]   The served objects are checked against JPL Horizons, the
              way the numbers are checked against their sources.
              << new this session: moved up from "not urgent", because
              it verifies what the website already serves.
  8. [next]   The website's checks get a short list of their own, so a
              new room or a moved front door can't break unnoticed.
  9. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address. The lobby's wide
              Solar System card, its first half, is done.
 10. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
 11. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
 12. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 13. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- Earth's orrery patch is in, and your look found it correct.
  - A new checkbox, "-- Exosphere (Geocorona)", draws a faint shell at
    100 Earth radii, in the website's colour, with the words you
    approved.
  - The two coordinate hovers, the Celestial Sphere tooltip and the
    coordinate guide say "Earth's axial tilt" instead of typing 23.4.
    Earth's rotation-axis hover already gives the angle for the date.
  - The Upper Atmosphere tooltip said the layer reaches 1,000 km; it
    now shows the hover's words, which say 600 km, the height drawn.
- The website still says the inner belt sits "where the measured
  particle flux peaks", and it says the same of Jupiter's belts, whose
  distances have no source. The website patch fixes both.
- The skills: each long one opens with its contents, and the check
  fails if a list stops matching its headings. Five skills are still
  longer than Anthropic's 500-line guideline; splitting
  provenance-discipline's two long procedures into separate files is
  recorded, not scheduled.
- This chat cannot reach JPL. The Horizons check will run on your
  machine, unless you allow JPL in this chat's network settings.
- My closing patch refused to rewrite this page because of your
  "-- done" marks. That broke your rule that you can annotate the
  documents; the new closing patch keeps your notes instead.
- The ledger holds 242 open items: L-418 and L-419 opened; L-389, L-416
  and L-417 closed.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Your look at the coordinate box's teal-circle line.*
2. Earth's website patch, then your look on the phone.
   - The inner belt's words, and no "measured" claim for Jupiter's.
   - The geocorona note corrected.
   - The saved Earth test scene re-recorded from today's data.
   - The collapsed-features check added to the website's maintenance
     run, with its own button.
3. The Horizons check: a design round first, in a fresh session, from
   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- The coordinate box's teal-circle line, in the orrery.
- Run patch_L419_1, reinstall ledger-and-session-records, and replace
  the Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.82.

At the Horizons design round:
- What Horizons can confirm, what counts as agreement, where the check
  runs and how often, and what to do with pinned comet records.
- Whether this chat should be allowed to reach JPL.

At the next design talk:
- The fuzzy outer corona, designed together with the dust cloud. The
  exosphere is now a candidate for the same treatment.
- Moving the highlighted row to the top of the list.
- GO's arrow, only if the text box stays in the centre, as you ruled.
  If it can't, no arrow.
- Earth's design talks, the belts' shape first.

Decisions from the Fable sweep, one at a time when you're ready:
- Whether items inside an ordered list need RICE scores at all.
- A handful of scores it proposes.

Not urgent, in your order:
1. Whether the editor should also edit the words on the Solar System
   room's rows.
2. Choosing a date, and animation.
3. The scattered disk, with the Kuiper belt in the Solar System room.
   It is not the fuzzy boundary idea: the disk is a population of icy
   bodies, the fuzzy boundary is a way of drawing an edge. When the
   disk is designed, its edges would likely be drawn that way.

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - This session: L-413 (Earth's list, the orrery patch), L-418 (the
    skills' contents and histories), L-419 (your notes in documents),
    L-395 (the Horizons check moved up). Closed: L-389, L-416 (dashboard
    buttons), L-417 (the skill limits).
- Your run record for this session:
  `documentation/WHERE_WE_ARE_10-5-26_1627_run_record.md`
  - The Sun's list: L-412.
- The skills' old version history: `documentation/SKILL_HISTORIES.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session records:
  `documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`, and for
  the next round, `documentation/HANDOFF_L395_horizons_check_design_20261005.md`
