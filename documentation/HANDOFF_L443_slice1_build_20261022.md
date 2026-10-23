<!-- Doc-Kind: hand | Closing report, 2026-10-22, evening: L-443's design session and slice 1's build -- fifty of the orrery's bodies to the Solar System room, in groups that fold open, the comets drawn from today, and a bare interactive.html link opening the room. -->
# Closing report: slice 1 of the objects, designed and built (October 22, 2026)

Built on bfb6c474 at https://github.com/tonylquintanilla/palomas_orrery
and 0bb34344 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main of each). Pushed at: (Tony's pushes, after section 2).

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD (closing report), after a DESIGN SESSION in the same
session. Written October 22, 2026 by Anthropic's Claude Opus 5.5.
Companions: the brief, `HANDOFF_L443_objects_design_brief_rev2_20261022.md`
(Claude Fable 5.1, saved by this close); the design record,
`DESIGN_L443_objects_rulings_20261022.md`; the words you approved,
`WORDS_L443_slice1_20261022.md`; the five readers' results,
`CHECK_L443_*_20261022.md`.

## 1. What came out of it

Each line says whether it was checked here or is a claim until your
runs and your look.

- **Fifty bodies come to the Solar System room**, by JPL's own
  classes: comets 11, near-Earth asteroids 11, main belt 7, Jupiter
  Trojans 5, centaurs 1, trans-Neptunian objects 15. Their orrery
  entries carry a key and JPL's exact name; their descriptions were
  read against pages opened today, or trimmed, by the words list you
  confirmed. Checked here, except JPL's live answers (your orrery run).
- **The drawer has six group rows that fold open** (your option B).
  A group's name folds it; its box ticks all its bodies; its line
  counts them; the asteroid and beyond-Neptune groups list their
  bodies by distance from the Sun on average (semi-major axis), read
  from the served cache. Checked here: the drawer check (with two new
  planted faults) and a headless walk of the real page; the Sun and
  Earth rooms compared old against new, identical. Not seen on a
  phone.
- **Every comet is drawn from today's orbit**, Halley and Encke too,
  and both join the comets group. Checked here on stand-in data; the
  first real build is the test.
- **A bare interactive.html link opens the Solar System room**; the
  Explorer is at `interactive.html?exhibit=solar-system-explorer`, its
  card and the measuring page's back link follow, and Studio's scene
  list offers it. Checked here.
- **A body with a helio_id is served by it** (Eris, Haumea, Makemake,
  Gonggong, Quaoar, Orcus, Patroclus): the export, the period fetch,
  and the orrery's own elements pre-fetch around the Sun now ask the
  same record. Orcus and Patroclus get Pluto's kind of sentence, since
  their shared centre lies outside the bigger body. Checked here; the
  orrery's plot of these seven around the Sun is your look.
- **Three comets re-pinned to JPL's newest record** (Schaumasse 2024,
  Howell 2021, Churyumov-Gerasimenko 2015). Your orrery run confirms.
- **Checks.** Website offline run, in a throwaway copy with a stand-in
  cache: everything passes except the pulls (no GitHub here), the
  Horizons confirmations (until your orrery run confirms the 50) and
  Artifact 1, which fails the same way on the untouched base with the
  same stand-in data. Builder's offline suite 390 of 390. Orrery tests
  for the export, the period fetch and the Horizons check pass; the
  scanner's gate path 0, whole tree 276, unchanged.

## 2. Your run order

The patches refuse to run on files they did not expect, and write
nothing then. Each is run from its repository's root folder in VS Code,
then moved to that repository's documentation/ folder.

In the ORRERY folder:
1. `patch_L443_1_slice1_orrery_20261022.py` -- the 50 entries, the
   export, the period fetch, the pre-fetch, two tests.
2. `patch_L443_3_close_20261022.py` -- this close: the ledger, Where We
   Are, interactive-exhibit 1.21, the protocol (v3.109), this report,
   the design record, the words list, the check files and the brief.
3. The ORRERY maintenance run. It asks JPL about the 50 new bodies, so
   it takes longer than usual: perhaps ten to twenty minutes, with its
   two-second pause between questions. Expect:
   - Period fetch: PASS, naming the bodies it fetched. Gonggong is
     named "not fetched here: on plotting's skip list" (L-470).
   - Horizons check: PASS, or DISAGREES naming a body and the field.
     A DISAGREES on a name is a simple error for the next session: do
     not push past one you do not understand; bring it to me.
   - Skill manifest and ledger index: regenerated.
   Commit and PUSH.

In the WEBSITE folder:
4. `patch_L443_2_slice1_website_20261022.py` -- the 50 config rows,
   the grouped drawer, the comets' anchor, the front door, the checks.
   (Decide section 3 first.)
5. The Daily Run. Its pull brings the new export, the mirror writes
   each new body's description, link and period, and the builder
   fetches the 50. Read two things in the builder's output:
   - the new line `[window] served window: N days either side of today,
     set by <body>`. Today it reads about 88 days, set by Mercury. If a
     new body sets it at a few days, do not push: bring me the line.
   - any `[warn] ... trust measurement failed` or `served_window:
     null`: do not push; bring me the line. A comet whose orbit JPL now
     fits as open would do this.
   Then the offline run: green apart from anything those two lines
   named. Commit, push, and the live run.
6. Reinstall interactive-exhibit 1.21 (Settings > Skills), from the
   orrery's skills/ folder.
7. Your look, on the phone: the Solar System room from a bare
   interactive.html link; See more; open Comets and the Trans-Neptunian
   objects; tick a group's box (the view widens to hold them); hover
   Orcus (the shared-centre sentence), Eris (none) and a comet; Halley
   where it is now; the Explorer from its card.

## 3. One decision before step 4: the info panel's words

The room's i panel described what it held, and two sentences were no
longer true. Proposed, in the website patch:

- Was: "The Sun, the eight planets and Pluto, each drawn as its symbol
  on its orbit, where it is now: at the minute you opened this room, as
  the line under the title says."
  Proposed: "The Sun, the planets, Pluto, and comets and asteroids,
  each drawn as its symbol on its orbit, where it is now: at the minute
  you opened this room, as the line under the title says."
- Was: "Apophis, the first asteroid here, waits under See more; the
  other asteroids, the comets and the spacecraft join later, each in
  its place in the list."
  Proposed: "See more adds the comets and the asteroids, in groups in
  their places along the list. Tap a group's name to open it, or its
  box to draw all of it. The spacecraft join later."

Any word can change before the patch runs.

## 4. Your rulings this session

In your words, in the design record, section 1, and on L-443.

## 5. Found and fixed along the way

- Deep Space 1 flew past comet Borrelly in 2001, not Tempel 2: the
  description and the code comment are corrected.
- Chariklo was called retrograde (JPL: inclination 23.4 degrees), and
  Mani "unnumbered" (307261 Mani). Corrected.
- The orrery drew a body's orbit around the Sun from its own centre's
  record but its marker from its helio_id; both now come from the
  helio_id, as the website serves it.
- The builder now prints the served window's width and the body that
  sets it, so a body that narrows the room for everyone is seen by
  name.
- The headless walk's bullet count had been stale since the i panel
  listed sources (L-456); it now finds the room's own two lists.

## 6. Next session

- **The obligation.** The next session confirms its loaded copy reads
  interactive-exhibit 1.21 before exhibit work.
- **Slice 2: the spacecraft and the 14 comets on open paths**, which
  need the spacecraft's path drawing; with it L-461 (pull matches
  push), which this slice did not build.
- **Carried, not chased:** L-470 (6AC4721, Gonggong's period); two
  gallery-cache-builder sentences for its next version (L-443); the
  walk's Pluto check on stand-in data (L-443).

## 7. Tony-actions, all in one place

- (decide) The info panel's two sentences, section 3, before step 4.
- (do) Section 2, steps 1 to 5, in order.
- (do) Reinstall interactive-exhibit 1.21 (step 6).
- (do) Your look (step 7).
- (do) Three papers into `papers/` (`READING_L456_tony_20261021.md`),
  carried from before.
- (decide, not urgent) 6AC4721: retire or merge it with MAPS (L-470).

## 8. The Settled line this close took off Where We Are

Kept here word for word, to keep the page under its line cap:

- A served number's citation is the orrery's, word for word; the
  website's note only for a drawing choice. Belts: random dots. A lost
  run record stops the Daily Run. Lines past a hover's 17 go to its i
  panel. (Oct 16-17)

Session written October 2026 with Anthropic's Claude Opus 5.5.
