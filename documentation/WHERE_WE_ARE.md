<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->
# Where We Are

**Tony**: see my notes -- 

Last updated: October 4, 2026, end of both of today's sessions. 
- Written at orrery d7f2a594 and gallery ac81e7ce.
- Two sessions ran today side by side: the Sun's distance cards, and
  the lobby card. This page now covers both.

> **READ THIS FIRST**
>
> **Changed this session:**
> - The Sun's distance cards are built, on the website and in the
>   orrery. Every distance now comes from a source that was opened and
>   read, and prints at the figures that source supports.
> - The heliopause is 121 AU, the termination shock 94.01 AU, and the
>   Sun's gravitational reach is its Hill radius, 0.65 parsecs.
> - The Roche limit is drawn at 3.45 solar radii and described as
>   "about 3", so it doesn't sit on the inner corona.
> - The Sun's remaining work is now one ordered list of ten items. The
>   dust cloud joined it.
> - From the other session: the lobby opens with a wide Solar System
>   card; the drawer's small fixes and Home are built; both
>   repositories now show "MIT license" on GitHub, and the website's
>   content is under CC BY 4.0.
>
> **Do next:**
> - *The Sun's list, from item 3: the orrery's opening view of the Sun,
>   then the Alfven surface's unsourced ranges.* -- updated to cleanup Earth's old items first. 
>
> **Needs you now:**
> - *Run the two small close patches and push.* -- done

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
              body's own room. << new this session: the drawer's
              small fixes and Home are built, and you checked them.
  5. [NOW]    *The Sun's numbers get the same checking Earth's got.*
              << new this session: the distance cards are done. Ten
              items remain, in the order you confirmed.
  6. [next]   A bare interactive.html link opens the Solar System room,
              and the Explorer gets its own address, after the Sun's
              list. << new this session: its first half, the lobby's
              wide Solar System card, is done and on the website. -- add ledger cleanup to the next items following the braid and theme group principles. 
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

- On the phone, the Sun's far shells say their radius in AU, then
  their kilometres, at the figures their sources support.
- Your notes print under the Oort cloud's two edges, Gravitational
  Influence, the outer corona and the streamer belt. Their numbers come
  from the stored rows, not typed into the words.
- The Alfven surface sits inside the outer corona, as you checked.
- The orrery's Sun hovers print the same numbers from the same rows.
- The lobby opens with the wide Solar System card. Its picture shows
  the planets at noon on October 4; the room itself always shows now.
- In the Solar System room's drawer, an opened row fits with the phone
  sideways, and Home backs out to keep every ticked body in view.
- Some kilometre figures look coarse because their source gives one
  figure: 100,000 AU prints as 10,000,000,000,000 km. That is the rule
  you set on September 28, and you kept it.

## The next three steps  **>> UPDATED THIS SESSION**

1. *The orrery's opening view of the Sun.*
   - You decided "photosphere plus 10%".
   - It turned out to be more than one line: the axis length and the
     shells that start switched on both set the width. Proposed to you
     before it is built.
2. The Alfven surface's three unsourced ranges.
   - I read Cranmer et al. (2007). If it states them, they stay with a
     citation; if not, all three go.
   - The streamer belt's tilt with the Sun's equator gets the same
     read.
3. The other typed numbers in the Sun's hovers, one at a time.
   - For example Voyager 2's 84 AU, and the heliopause hover saying
     both Voyagers are still inside, which stopped being true in 2018.

## Waiting on you  **>> UPDATED THIS SESSION**

Now:
- Run the two small close patches (orrery, then website) and push.
- Delete the folder "data/solar-system (1)" in your gallery copy, with
  OneDrive paused, as you did on October 1. Git ignores it, so it does
  no harm meanwhile. -- done

At the next design talk:
- The fuzzy outer corona, designed together with the dust cloud.
- Moving the highlighted row to the top of the list.
- An arrow from GO's text box to its body. -- the problem with this last time is that it moved the text box from the center. the text box needs to remain in the center. if not possible, don't implement the arrow. 

Not urgent, in your order:
1. The full check of the orrery's object list against JPL Horizons.
2. Whether the editor should also edit the words on the Solar System
   room's rows.
3. Choosing a date, and animation.
4. The scattered disk, with the Kuiper belt in the Solar System room. -- is this the fuzzy boundary idea?

## Where the details are  **>> UPDATED THIS SESSION**

- Every item, done and open: `LEDGER_CONSOLIDATED.md`
  - The Sun session: L-371 (the distance cards), L-412 (the Sun's list
    of ten), L-410 (fuzzy boundaries), L-411 (typed numbers), L-131
    (the dust cloud). Closed: L-209, L-224, L-227, L-229.
  - The lobby session: L-363 (the lobby card, the drawer fixes and
    Home), L-409 (the licenses), L-216 (the stray folder).
- The reasoning behind the order:
  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
- The latest session records:
  `documentation/HANDOFF_L371_distance_cards_session_20261004.md`, and
  `documentation/HANDOFF_L363_lobby_card_session_20261004.md`
