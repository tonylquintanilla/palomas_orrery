<!-- Doc-Kind: hand | Every word a visitor will see in the Solar System room after step 3, for Tony to approve before the build. -->
# The Solar System room: every visitor word, for your approval

Built on gallery f6d1ca95d5e6e95b886b6998a3fdf8ea1a5efeb1 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and
orrery 10012821cf6289095912c0a5f2a0ae86d26ce1e1 at
https://github.com/tonylquintanilla/palomas_orrery (L-363, Half 2, step 3).

How to use this page:
- Each item gives the proposed words.
- *Italic* items are the ones that need a choice from you.
- Write your note after the item as `-- **Tony**: ...`, as you did on
  Where We Are, and upload the file back.
- "Unchanged" means a visitor already sees these words today; they are
  here so the list is complete.

## 1. The rows in the drawer

- Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
  - These are the names served from the data, as they are today.
- Apophis, shown only after "See more", between Earth and Mars.
- *Pluto's row.* The data names this object "Pluto-Charon Barycenter",
  as the orrery's own list does.
  - Proposed: the row and the hover both say **Pluto**. -- **Tony**: confirmed
  - The hover adds one line (section 4).
  - The alternative is to show "Pluto-Charon Barycenter" as it is served.

## 2. The drawer's own words

- Header, unchanged: **In this scene -- 2 of 10**.
  - The count is rows ticked out of rows listed. After "See more" it
    reads "of 11".
  - Every room uses this header, including for rows that are not drawn.
- Button, unchanged: **All / none**.
- *The "See more" button at the end of the list.*
  - Proposed: **See more** while Apophis is hidden, **See fewer** once
    it shows. -- **Tony**: confirmed. 
- The closed drawer's handle shows the highlighted body's name, e.g.
  **Earth**. Unchanged.

## 3. A row that has been opened

- *The button in an opened row.*
  - Proposed: **Enter the Sun room** and **Enter the Earth room**. -- **Tony**: confirmed.
- *A row with nothing behind it.*
  - Proposed: **No room or cards yet**, as the design has it. -- **Tony**: confirmed.

## 4. The text box on a body (its hover)

Today each body's box reads, for example:

    Mercury
    r = 0.XXXXXX AU (X.XXXe+07 km)
    x = 0.XXXXXX AU, y = 0.XXXXXX AU, z = 0.XXXXXX AU

- *The distance in km is printed like 5.791e+07.* That is computer
  shorthand for 57,910,000, and your rule of 2026-09-16 is to avoid
  compressed language in hover text. -- **Tony**: i agree that writing out the number is preferred to exponential notation (not computer shorthand)
  - Proposed first two lines:

        Mercury
        0.XXXXXX AU from the Sun (XX.X million km) -- **Tony**: in the above example you could say, 57.91 million km assuming 4 sig figs, but use the actual sig figs

  - Proposed: drop the x, y, z line. It gives the position along the
    room's axes, which says little to a visitor. -- **Tony**: i agree. drop.
  - The alternative is to leave the box as you accepted it in Half 1.
- *Pluto's box adds one line.* Proposed:

        Pluto
        The symbol marks the gravitational center (barycenter) that Pluto and its moon Charon orbit
        together. It lies outside Pluto itself.
        XX.XXXXXX AU from the Sun (X,XXX.X million km) -- **Tony**: confirmed as revised above 

## 5. The source line in the panel (unchanged form)

    JPL Horizons, osculating orbital elements: target 199, centre @sun,
    epoch JD 2461313.5, retrieved 2026-09-30. The position shown is
    worked out from these for the minute under the title.

- Pluto's line will read "target 9". Proposed: add "(the Pluto-Charon
  barycentre)" after it, so the number is not a puzzle. -- **Tony**: "target 9?" we should just cally it Pluto-Charon barycenter. we defined that above. 

## 6. The panel's two paragraphs, rewritten

Proposed, first paragraph (what is drawn):

> The Sun, the eight planets and Pluto, each drawn as its symbol on its
> orbit, where it is now: at the minute you opened this room, as the
> line under the title says. The room opens on the Sun and Earth. Open
> the list below and tick any of the others to add them. Tap a body to
> find its row; tap the row again to see what the gallery holds for it.

Proposed, second paragraph (what is still missing):

> This room is being built up. The asteroids, comets and spacecraft
> join it later, each in its place in the list. Each body's own shells
> -- its atmosphere, rings and magnetic surroundings -- live in that
> body's own room; so far the Sun and Earth have one. The Solar System
> Explorer, the gallery's first room, still shows every planet.
-- **Tony**: i think you can drop the last sentence. the explorer will remain but not as a featured card. the new room will have all the planets, just not date picker. 

Unchanged: the paragraph about Pyodide, and the note at the bottom
naming Paloma and JPL Horizons.
