<!-- Doc-Kind: hand | Build record: the four rulings of Oct 24 on the drawer's controls, the count line, a far orbit's frame and the About card's return, built in the gallery; with the exhibit skill's 1.22. -->
# Build record: the drawer's controls, the count line, a far orbit's frame

Tony Quintanilla, PE | Claude Opus 5.5 | October 24, 2026

Built on gallery 2c2057d7f11794fe5c2805af955dbc452519c644 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main)
and orrery 82fa04cc634c58544b9a2bb4aeb57310a2000515 at
https://github.com/tonylquintanilla/palomas_orrery (branch main). Both read
live with git ls-remote at the build's start and again before delivery.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD. Two patches: gallery
`patch_L477_2_drawer_view_build_20261024.py` (the build) and orrery
`patch_L477_3_build_records_20261024.py` (the skill, the protocol entry,
the ledger, Where We Are, and this record).

Companion to: `DESIGN_L477_drawer_and_view_rulings_20261024.md`, the
rulings this builds. Supersedes nothing.

Ledger: L-477 (the drawer's controls), L-478 (the count line), L-479 (a
far orbit), L-480 (About's return). Each stays open until Tony's phone
look.

## 1. What was built, by ruling

**L-477, the drawer's controls.** In the Solar System room only:
- See more / See fewer is gone. All six groups are always listed,
  folded shut.
- A group row only folds open or shut. Where a body row has its tick
  box, a group row has its fold arrow. It ticks nothing.
- The top bar's button reads Reset in this room. It puts back what the
  room opened on: Mercury, Venus, Earth and Mars ticked, Earth named,
  every group folded, the opening frame and angle, the drawer closed.
- Inside an open group, once one of its bodies is ticked, "Reset
  <group>" appears and unticks that group's bodies, and no others.
- Nothing ticks many bodies at once.
- `data/objects_config.json`: the six group rows lose `see_more`, and
  the rows' explanation says what the drawer now does.
- The Sun and Earth rooms are unchanged. Their All / none still ticks
  every shell. That was checked by driving both rooms in the old page
  and the new: identical.

**L-478, the count line.** It is now its own element at the lower left,
above the drawer's handle, at the height of the HUD on the right, in the
same type. It hides while the drawer is open.

**L-479, a far orbit's frame (the trial).**
- Go To fits the body's whole drawn orbit, at the room's 20%, and opens
  its text box, the same for every body. Sedna's Go To reaches about
  1,200 AU; Pluto's past 45 AU.
- Ticking, Home and Reset still frame on where the bodies are now.
- Every body's hover now ends with "Orbit: q to Q AU from the Sun.",
  worked out from the served elements. Three significant figures, never
  finer than the body's distance error earns. Examples: Sedna 76.2 to
  1,000; Earth 0.983 to 1.02; Halley 0.571 to 35.1; Mercury 0.307 to
  0.467. The figures check prints all 62.
- The longest body hover is now 10 lines (Orcus), against the 17-line
  ceiling.
- Fixed in passing: a zoom-out tap could make a view smaller when Go To
  had set it wider than the zoom buttons' 5,000 AU cap. No orbit served
  today reaches the cap (the farthest, Hyakutake's, fits in about
  3,500 AU), so this is protection for slice 2's far bodies.

**L-480, About's return.** Closing the About card steps back to the
room when a room's About line opened it. Arriving at the lobby's About
card any other way, closing it stays in the lobby, as before.

## 2. Words for your OK

The room's i panel had to change, because three of its sentences
described controls that are gone. These are visitor words, so they need
your word before they ship. You can approve them on the phone look.

- Was: "Open the list below. Tick a body to draw it, and the view
  widens to hold every body drawn."
  Now: "... to hold every body drawn. Reset puts the room back as you
  found it."
- Was: "Go To takes the view to a body, and Home backs out to hold
  every body you ticked."
  Now: "Go To takes the view to a body's whole orbit, and Home backs
  out to hold every body you ticked."
- Was: "See more adds the comets and the asteroids, in groups in their
  places along the list. Tap a group's name to open it, or its box to
  draw all of it. The spacecraft join later."
  Now: "The comets and the asteroids are in groups in their places
  along the list. Tap a group's name to open it, then tick its bodies
  one at a time. The spacecraft join later."

New button words, from your rulings: "Reset" and "Reset Comets" (or the
group's name). The hover line is the shape you approved: "Orbit: 76.2 to
1,000 AU from the Sun."

## 3. Checked, and how

- The drawer check (`documentation/smoke_solar_system_drawer.js`):
  passes, and goes red on each of seven planted faults (Home ignoring
  ticks, See more come back, a folded group showing its bodies, a
  group's Reset leaving one ticked, a group's Reset reaching outside
  the group, Reset offered while folded, the count line reading one
  axis). It also crashes on the old site, as it should.
- The figures check (`documentation/smoke_solar_system_figures.js`):
  passes, with three new planted faults for the orbit line (four
  figures, the error's place ignored, an open orbit printed).
- The headless walk (`tools/headless/walk_solar_system_drawer.js`): 105
  checks pass on the new page; it goes red on the old one.
- The Sun and Earth rooms (`tools/headless/compare_rooms.js`):
  identical in the old page and the new.
- The offline maintenance run, on a copy: 35 of 35 gating checkers
  pass. Its five pulls fail only because the sandbox cannot reach
  GitHub's API.
- Both patches: run on throwaway copies, again on a copy with Windows
  line endings, and a second time to see them refuse.

The phone has not seen any of it. The sandbox has no WebGL and no
phone.

## 4. Found along the way

- The brief said a view holding Sedna's whole orbit is "about ten
  times wider" than the ticked view; it is about twelve (1,200 AU
  against 99). L-479 carries the corrected figure.
- `tools/store_writer.py` still labels a row "(a See more row)" when a
  row is served `see_more`. No row is served so now, and the drawer
  check fails on one, so the branch is dead and harmless. Left alone.

## 5. Question for the next design talk

Whether the Sun and Earth rooms' All / none becomes Reset too. Your
ruling was the Solar System room's, and those rooms tick shells, not
orbits. On Where We Are's list.

## 6. Settled line removed from Where We Are

The page sits at its 130-line cap, and this patch adds one line to
Waiting on you. Kept here word for word:

    - Gonggong off the skip lists; the maintenance run is its test. (Oct 23)

## 7. Tony-action rollup

- **(do)** Gallery: save `patch_L477_2_drawer_view_build_20261024.py`
  in the gallery folder; run it from VS Code; run
  `gallery_maintenance_run.py`; move the patch to `documentation\`;
  commit and push; then run `gallery_maintenance_run.py --live`.
- **(do)** Orrery: save `patch_L477_3_build_records_20261024.py` in the
  orrery folder; run it; run `skills_index.py`; run `ledger_index.py`;
  move the patch to `documentation\`; commit and push.
- **(do)** Reinstall interactive-exhibit 1.22 (Settings > Skills), from
  `skills\interactive-exhibit\SKILL.md` after the orrery push. The next
  session confirms its loaded copy reads 1.22 before exhibit work.
- **(do)** Copy the protocol (`PROJECT_INSTRUCTIONS.md`, now v3.110)
  into the Project's instructions, as you do after a protocol change.
- **(do, then decide)** The phone look, below; and the three panel
  sentences in section 2.

Phone look, upright, after both pushes:
1. Open the Solar System room fresh and open the drawer. No See more;
   all six groups listed, each with a right-pointing arrow.
2. Tap anywhere on the Comets row. It opens; nothing is ticked.
3. Tick Halley. "Reset Comets" appears under the row. Tap it: Halley is
   unticked; the comets stay open.
4. Tick two bodies anywhere, open a second group, then tap Reset in the
   top bar. The room is as it opened: four planets, groups shut.
5. Open Trans-Neptunian objects and tap Go To on Sedna. The whole orbit
   fits, its text box opens; one tap on the picture closes the box.
6. Zoom in until the count line shows at the lower left. Is it clear of
   the handle below it, and is the Aries mark on the right now uncovered?
7. Tap the i button, then "About Paloma's Orrery", then close the card.
   You should be back in the room.

Written October 24, 2026 with Anthropic's Claude Opus 5.5.
