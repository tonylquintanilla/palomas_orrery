<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

Last updated: October 6, 2026, end of the Earth website session.
- Written at orrery e7073fce and gallery 38f1e7b0, after your runs of
  the website patch and of the galactic-plane and panel-colour patches.

> **READ THIS FIRST**
>
> **Changed this session:**
> - Earth's website patch is live, and your look on the phone found it
>   correct. The inner belt says "trapped protons", in your words, and
>   Jupiter's belts no longer claim a measured distance.
> - The saved Earth scene the checks use is re-recorded from the real
>   data, with a tool that can remake it. That showed two hovers on the
>   live site were already too tall for the phone; with your approved
>   changes all three tall ones fit.
> - A search of both rooms found 17 facts typed in the code instead of
>   served with their sources. You ruled they are fixed now, as part of
>   finishing the Earth and Sun rooms. The plan is written down for a
>   fresh session.
> - A written rule now says code may type only words about our picture;
>   facts, papers and sources are served.
> - In the orrery, from a session of its own: the Celestial Grid draws
>   the galactic plane, a violet circle, with its poles, and the Star
>   Background marks Sagittarius A*, the galaxy's centre.
> - The desktop orrery opens on Linux and macOS again: its panels use
>   one grey, gray90, that every system knows.
>
> **Do next:**
> - *The typed facts, in a fresh session, from the plan written today.*
>
> **Needs you now:**
> - *Run this closing patch in the orrery repo, reinstall
>   interactive-exhibit, and replace the Project's instructions with
>   v3.84.*

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
              confirmed.* << this session: the website patch is live;
              the typed facts are the last part, with the design talks.
  6. [next]   The facts typed in the Earth and Sun rooms' code move into
              the served data, with their sources. << new this session
  7. [next]   The Sun's numbers get the same checking Earth's got: the
              Sun's list, from its opening view.
  8. [next]   The served objects are checked against JPL Horizons, the
              way the numbers are checked against their sources.
  9. [next]   The website's checks get a short list of their own, so a
              new room or a moved front door can't break unnoticed.
 10. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address. The lobby's wide
              Solar System card, its first half, is done.
 11. [later]  The rest of the orrery's objects come to the website --
              dwarf planets, asteroids, moons -- through the same
              connection that now carries the room's eleven bodies,
              checked against JPL Horizons.
 12. [later]  Encounters: comets and spacecraft shown at the dates
              that matter.
 13. [later]  The planets get their details -- layers, rings, magnetic
              fields -- Jupiter and Saturn first.
 14. [goal]   The website does what the desktop orrery does, from data
              fetched from JPL each night, with a date to choose and
              time to play within the range the data covers.

## Right now  **>> UPDATED THIS SESSION**

- Earth's website patch is live: 24 of 24 checks after the cache build,
  and your look on the phone found it correct.
  - The inner belt reads in your approved words, and the word
    "protons" comes from the served data, not the code.
  - Jupiter's three belts say only where they are drawn.
  - The geocorona note no longer says the orrery lacks its shell.
  - The collapsed-features check now runs in the website's maintenance
    run, so it counts 24, with its own dashboard button.
- The saved Earth scene was five weeks old. A new tool remakes it the
  way the page makes it, and the checks now see the live site as it is.
  - Seen that way, the rotation axis hover was 21 lines and the outer
    belt's 18, on the live site, over the phone's 17-line limit.
  - Your approved changes bring all three tall hovers to 17: the axis's
    layout, and one shorter sentence on both belts.
- The 17 typed facts: 13 in Earth's room, 4 in the Sun's. Most are
  already backed by a served source and only need moving; six need a
  source found and read, or removal with the gap noted.
- Jupiter's inner belt isn't in a website room yet, so its new words
  wait for a Jupiter room; the orrery's are correct, as you saw.
- The galactic plane in the orrery is in, and you found it good. Your
  two requests are recorded with it: the galactic tide is very faint
  and its X can't be made out, and the coordinate circles' descriptions
  could move to hover markers on the circles.
- The panels' grey: a shade darker than before, the grey of January to
  June. A look on Windows, and a run on a Mac when convenient.
- The skill copies this session loaded all matched the repo, and the
  ones you reinstalled read their new versions.

## The next three steps  **>> UPDATED THIS SESSION**

1. *Your run of this closing patch, and the reinstall.*
2. The typed facts move into the served data, in a fresh session, from
   `documentation/MANIFEST_L421_typed_facts_20261006.md`.
3. The Horizons check's design round, in its own session, from
   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- Run this closing patch, run orrery_maintenance_run.py, commit and
  push.
- Reinstall interactive-exhibit (1.12) and replace the Project's
  instructions with PROJECT_INSTRUCTIONS.md, now v3.84.
- A look at the orrery's panels on Windows; a Mac run when convenient.

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
  - This session: L-413 (Earth's list), L-349 (the belt's words),
    L-379 (the saved scene), L-300 (the collapsed-features check), L-292
    (the geocorona note), L-421 (the typed facts, opened). Closed: L-349
    (the belt's words), L-300 (the collapsed-features check), L-369
    (Earth's tilt in words), L-415 and L-419 (skill rules confirmed).
  - L-418 stays open only for splitting provenance-discipline's two
    long procedures into their own files.
  - The galactic plane: L-420; the panel colour: L-027; their record:
    `documentation/HANDOFF_L420_galactic_plane_20261006.md`.
- The plan for the typed facts:
  `documentation/MANIFEST_L421_typed_facts_20261006.md`
- This session's record:
  `documentation/HANDOFF_L413_earth_website_20261006.md`
- The skills' old version history: `documentation/SKILL_HISTORIES.md`
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- For the Horizons round:
  `documentation/HANDOFF_L395_horizons_check_design_20261005.md`
