<!-- Doc-Kind: hand | Brief for the lobby build: the gallery's front page opens on the Solar System room as the clear starting point (option E of the October 9 design talk), with the words Tony confirmed. One gallery patch, one records patch. Written October 9, 2026. -->
# Handoff: the lobby's starting point (option E), the build brief

Built on gallery 5ec4739b6f160b7f4a455004b2bc5727e61a7815 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run 10-9-26"). Orrery read at aa46bb1 at
https://github.com/tonylquintanilla/palomas_orrery; by the time this
session starts the orrery will be past Tony's L-414 push, so the
session pins both HEADs itself at its start and builds on those.
Written by the Fable 5.1 coordination session of October 9, which read
both repos at HEAD and wrote no patch.

- Type: BUILD, gallery. One gallery patch (index.html,
  gallery/gallery_config.json, gallery/gallery_metadata.json) and one
  records patch in the orrery (the ledger, Tony's page).
- The design is section 11 of the Oort cloud design record of October
  9 (Tony's file; the session asks him its name in documentation/ if
  it is not obvious). Everything below restates what that section
  settled, so this brief stands alone.
- Skills this session fires: gallery-pipeline 1.2 (index.html, the
  cards, gallery_metadata.json, gallery_config.json),
  safe-file-editing 1.13, ledger-and-session-records 1.18. Read back
  each loaded version in the first reply. interactive-exhibit does not
  fire: the lobby is not a room, and interactive.html is not touched.
- The protocol is PROJECT_INSTRUCTIONS.md v3.87 after the L-414 push
  (v3.86 if that push has not landed; say which).

## Read this first

- *A friend shown the site on a phone did not know where to start.
  The fix is one screen: the Solar System room's picture is the way
  in, with one button, before anything else.*
- *The words are confirmed. Nothing in this session asks Tony for new
  words; the two notes in section 3 are shown to him, not asked.*
- *Phone first. The whole first block, title to button, fits a
  phone's first screen (about 844 px tall at 390 wide).*
- *This is a new ledger item, under the lobby's lineage (L-282, the
  lobby as an entrance hall), not part of L-421 (the typed facts) or
  L-363 (the front door). The session opens it.*

## 1. What the lobby does today (read at 5ec4739)

- `renderLobby()` in index.html draws, in order: the welcome title,
  the welcome sentence, the heading "Doors" with three doors (Solar
  System, Earth System Science, Stars), the heading "Featured" with
  wide cards first and then the grid, then the guest book.
- The Solar System card (`solar_system` in gallery_metadata.json) is
  served `wide: true`, `featured: true`, kicker "Start here", title
  "The Solar System, live", description "Turn it, zoom in, and step
  into the rooms of the Sun and Earth. Daily updates from JPL
  Horizons.", picture `gallery/pictures/solar_system_room.jpg`, and
  `live: interactive.html?exhibit=solar-system`. `wideCardHtml()`
  draws it.
- On a phone the three doors fill the first screen and the wide card
  starts below the fold, under "Featured". That is the problem.
- gallery_config.json carries no `sentence` today, so the page serves
  its typed default (`LOBBY_DEFAULT_SENTENCE` in index.html,
  "Explore interactive visualizations of the solar system, stellar
  neighborhoods, exoplanets, and more.").

## 2. Option E, as confirmed (Tony, 2026-10-09 17:23 and 17:25)

The first screen, top to bottom:

1. The welcome title "Paloma's Orrery" (unchanged).
2. The welcome line, served from gallery_config.json `sentence`:
   "The solar system, the Earth and the stars, to explore."
3. The heading "Start with the Solar System, live".
4. The room picture, edge to edge.
5. One sentence under it, the card's served `description`:
   "Today's planets in 3D. Turn it with your finger, tap a planet,
   step into the Sun and Earth."
6. One button, "Enter", opening `interactive.html?exhibit=solar-system`.

Then:

7. The heading "Or explore by subject", with the three doors as they
   are (names, sentences, exhibit counts). The word "Doors" leaves the
   page: a first-time visitor has no way to know what a door is.
8. Featured and the guest book, as now.

Rules for the build:

- The Solar System card is drawn ONCE, as the first block. It no
  longer appears under Featured as well, and it keeps its place first
  on the Solar System door's page.
- The picture, title and sentence come from the card's served fields;
  the welcome line from `sentence` in gallery_config.json. Nothing
  new is typed into index.html except the two headings ("Start with
  the Solar System, live" may itself be the card's served `title`;
  the build decides and says which) and the button's word.
- "Daily updates from JPL Horizons" leaves the card's sentence; the
  room names its source itself.
- The picture stays the one the L-363 session drew (version B, Mars's
  orbit at about 80 percent of the width, no grid).

## 3. Two notes shown to Tony with the result, not asked

- "Turn it with your finger" is phone wording. The desktop turns it
  with a mouse. The build shows Tony the desktop look beside the phone
  look and names this; if he wants a second sentence for desktop, that
  is a follow-up, not a block.
- The button's word is "Enter" unless the build finds a reason to
  show him two.

## 4. Verification before the patch goes to Tony

- Render index.html headless (Playwright is in the sandbox) at 390 x
  844 and at a desktop width, from a throwaway clone with the patch
  applied. Two screenshots to Tony. Pass on the phone: the "Enter"
  button is inside the first 844 px, and nothing from the old layout
  is drawn twice.
- The door counts still print and still match the metadata.
- The Solar System door's page still opens with the wide card first.
- The gallery's own checks that touch the lobby (the framing test of
  L-262 is for rooms; say if nothing covers the lobby, and record it
  on L-423, the website's checks, as a class, not chased).
- Mode 5 is Tony's: his look on the phone after the push, with the
  Home Screen clip's tab closed first so the phone fetches the new
  page.

## 5. The patches and Tony's steps

- The gallery patch, from the gallery repo root, following
  safe-file-editing; filed in the gallery's documentation/ (gallery
  patches live there; records live in the orrery's).
- The orrery records patch: the new item opened with its handle
  printed; L-282 (the lobby) gains one line pointing at it; Tony's
  page by section, every handle labelled, nothing below the marker.
- Tony's steps, printed by each patch: run the gallery patch (VS
  Code, Run), commit and push the gallery, look on the phone; run the
  records patch from the orrery root, run orrery_maintenance_run.py,
  move the script into documentation/, commit and push.
- The handoff: `documentation/HANDOFF_lobby_option_E_20261009.md` in
  the orrery, anchored on both HEADs at start and at close.

## 6. Not this session

- The front-door address change (L-363: a bare interactive.html link
  opens the Solar System room; the Explorer gets its own address).
  That waits for L-423 (the website's checks), as Tony ruled.
- Any change to interactive.html, the rooms, or the drawer.
- The welcome count line, the Featured grid's order, the guest book.

Brief written October 9, 2026, with Anthropic's Claude Fable 5.1.
