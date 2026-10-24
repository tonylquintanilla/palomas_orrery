<!-- Doc-Kind: hand | Build record: Tony's three readability asks of Oct 24 (bullets in the Solar System room's hovers, JPL Horizons' address in the i panels, the closing paragraph a list with "creator's"); with L-477 to L-480 closed on his look. -->
# Build record: readability, after the phone look of the L-477 build

Tony Quintanilla, PE | Claude Opus 5.5 | October 24, 2026

Built on gallery ea83ef0dfb2d438b3c56e909c8eaaf0ffd538377 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main)
and orrery faa965ed8e7a8e6bff95ff1741eee97b0216f1f2 at
https://github.com/tonylquintanilla/palomas_orrery (branch main). Both read
live with git ls-remote before building.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Two patches: gallery
`patch_L481_1_readability_build_20261024.py` and orrery
`patch_L481_2_records_20261024.py` (the ledger, Where We Are, and this
record).

Companion to: `HANDOFF_L477_build_20261024.md`, the build this follows;
Tony's run record `WHERE_WE_ARE_10-24-26_1140_run_record.md`, his look
of it. Supersedes nothing.

Ledger: L-481 (readability) new and built; L-482 (the Sun and Earth
rooms' Reset) new, a question; L-477, L-478, L-479 and L-480 closed on
his look.

## 1. His look, and what it closed

Every item of the L-477 build read "yes": the drawer and its groups,
Reset and a group's Reset, the count line at the left, Go To fitting the
whole orbit (the trial stands), and About returning to the room. His
"everything is correct" also approves the room's three reworded panel
sentences. L-477 to L-480 close. The Sun and Earth rooms' Reset, which
his ruling did not cover, moves to L-482 for the next design talk.

## 2. What was built (L-481)

His words: "my one suggestion is to add bullets to the sentences in the
hover to improve readability in dense text. i would also suggest adding
the url to the JPL Horizons sources in the info panels. at the bottom of
the panel, the standard paragraph, Part of Paloma's Orrery, revise
"inventor's" to "creator's", and also add bullets to each sentence for
readability."

- **Hover bullets.** In the Solar System room, each line of a body's
  hover after its name starts with a bullet: the distance, its note when
  there is one, the period, the orbit line, and the body's own sentence
  where the room serves one (Pluto's, the Trojans' pair). Sedna's now
  reads:
  - Sedna
  - * 82.8207589 AU from the Sun (12,389,809,180 km)
  - * JPL's own uncertainty for this position is not yet included.
  - * Orbital period: 11,390 years (4,160,000 days), around the solar
    system's center of mass, from JPL Horizons, fetched 2026-10-13.
  - * Orbit: 76.2 to 1,000 AU from the Sun.
  (On the page the asterisk is a round bullet.) One thing worth knowing:
  Plotly, which draws the hovers, understands only eight named symbols
  in its text, and "bull" is not one of them. Written that way the
  hover would have shown "&bull;" as letters. The bullet is written by
  its number instead, which Plotly does convert. That was read from
  Plotly 2.35.2's own code, the version the page loads.
- **JPL Horizons' address.** https://ssd.jpl.nasa.gov/horizons/, the page
  titled "Horizons System", read live on Oct 24. Every source line in an
  i panel that names JPL Horizons now carries it, and the panel makes it
  a link: each body's in the Solar System room, and in the Earth room
  the Sun direction, the Moon's arc and the pole of date. The closing
  paragraphs that name Horizons link it too.
- **The closing paragraph.** In every room, the Explorer's included, it
  is a bulleted list, one sentence to a bullet, and reads "named for the
  creator's daughter".

The Sun and Earth rooms changed only in their panels' text. That was
checked by driving both in the morning's page and this one: every tick,
frame and drawer row identical.

## 3. Checked

- The figures check names all four changes (the bullet entity, the
  address held, the address on the source line, no "inventor's"), and
  goes red on the morning's site on each.
- The headless walk: 108 checks, now holding Sedna's four bullets, its
  source line's address, and the closing paragraph as three bullets with
  "creator's" and the Horizons link.
- The typed-facts check: its lists now carry "creator's" and the three
  Earth source lines with the address.
- The offline maintenance run on a copy: 35 of 35 gating checkers. Its
  five pulls fail only because the sandbox cannot reach GitHub's API.
- The patch: run on a throwaway copy, on a copy with Windows line
  endings, and a second time to see it refuse.

The phone has not seen it.

## 4. The skill

No version this round. The exhibit skill went to 1.22 this morning, and
nothing in it now tells a session to do the wrong thing; the three
changes are descriptions to add. They are carried on L-481 for its next
version. This session read 1.22 from the repo, as it wrote it; the next
session still confirms its loaded copy reads 1.22 before exhibit work.

## 5. Tony-action rollup

- **(do)** Gallery: save `patch_L481_1_readability_build_20261024.py`
  in the gallery folder; run it; run `gallery_maintenance_run.py`; move
  the patch to `documentation\`; commit and push; then
  `gallery_maintenance_run.py --live`.
- **(do)** Orrery: save `patch_L481_2_records_20261024.py` in the orrery
  folder; run it; run `ledger_index.py`; move the patch to
  `documentation\`; commit and push.
- **(do)** Phone look, upright:
  1. In the Solar System room, tap Sedna's name and Go To. Its text box
     shows four bullets under its name.
  2. Tap the i button. Sedna's source line begins "JPL Horizons
     (https://ssd.jpl.nasa.gov/horizons/)", and the address is a link.
  3. At the bottom of the panel, before the About line, the closing
     paragraph is three bullets and says "the creator's daughter".
  4. In the Earth room, name Sun Direction; its source's Horizons
     address is a link too.
- **(decide, at the next design talk)** L-482: whether the Sun and Earth
  rooms' All / none becomes Reset too.

Written October 24, 2026 with Anthropic's Claude Opus 5.5.
