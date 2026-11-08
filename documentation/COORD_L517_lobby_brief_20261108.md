<!-- Doc-Kind: hand | The brief for two Claude Code sessions on the website: L-517 (the lobby for a first-time phone visitor), part 1 the pictures into the drawer, part 2 the lobby. Communication; written once, read by its sessions. -->
# Brief: the lobby for a first-time phone visitor (website)

Built on orrery 7d3e57bab8f7408ae8b12edc5d61a4056358c8b1 at
https://github.com/tonylquintanilla/palomas_orrery
and gallery 23440b799e35ff8ff0ab0dd8405ade3137f33f60 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io
(both branch main, read 2026-11-08, 08:25 Chicago). The rulings this
brief cites are on L-517 in Tony's next orrery push; the session reads
them there. Nightly bot commits since are expected.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD, two Claude Code sessions in the gallery repository, through
the python_work door, one part each, Tony's push and phone look between
them. Written November 8, 2026 with Anthropic's Claude Opus 5.5, the
coordinating session, after the design talk of that morning.

The design canvas, private to Tony: "Lobby: fewer ways in",
https://claude.ai/artifact/6TQPSgyMg1N1XBrYyvioxZ . Board D is the lobby
as ruled; board F sketches the pictures in the drawer. A session that
cannot open it builds from this brief and L-517; the canvas is a picture
of the same words.

ORDER (Tony, Nov 8, 11:03): "I would say the picture first then the
lobby." Part 1 puts the pictures into the drawer; part 2 builds the
lobby. The pictures are in the room before the lobby drops its Solar
System subject row, so they never lose a way in, and no temporary
footer line is needed.

## Start (both parts)

1. Record both bases; say whether either moved past the anchor.
2. Read L-517 (the lobby for a first-time phone visitor) in
   `LEDGER_CONSOLIDATED.md`, and the orrery's
   `documentation/WHERE_WE_ARE.md`.
3. Skills, each against the manifest, by its read plan:
   gallery-pipeline (1.2: index.html, gallery_config.json,
   gallery_metadata.json; part 2 reads it in full, part 1 the parts
   on gallery_metadata.json), interactive-exhibit
   (1.35; part 1 reads it in full, and part 2 the parts on the bare
   interactive.html link and the room list), safe-file-editing (1.14),
   ledger-and-session-records (1.22). interactive-exhibit went to 1.35 on
   Nov 7, night: confirm the copy you load reads 1.35 before work that
   fires it, and stop if it does not.
4. Say what you are about to do in one sentence and wait for Tony.

## Part 1: the pictures beside their rows (the Solar System room's drawer)

Every Solar System card that is not a live view goes into the Solar
System room's drawer, in a fold beside the row of the body it shows
(L-517 rulings 4 and 5). Counted at gallery 23440b79: 23 on a phone
(the "25" of the talk was the subject page's count, which includes the
Sun's and Earth's live views), and three more on a desktop only, the
cards whose shape is "none": Orbital Transformation of Mercury, Earth
Barycenter Shells and Near Earth Asteroids. Count them again at the
session's base.

- WHERE EACH GOES is method. A comet's pictures go beside that comet's
  row (3I/ATLAS beside 3I/ATLAS); a body with no fold of its own (Jupiter,
  Pluto, Mercury) gets one under its row; the Artemis II and Apophis
  pictures go under Earth; a mission's pictures beside that spacecraft's
  row; a picture whose body has no row goes beside the nearest parent
  group's row (Comets, Spacecraft, Asteroids). Solar System Explorer,
  which belongs to no single body, goes beside the root's Sun row.
  Record each card's place once, in one field on its entry in
  `gallery/gallery_metadata.json`, so nothing is typed twice and the
  drawer reads it. The report lists all of them, card by card, row by
  row, for Tony to judge.
- THEY LOOK UNLIKE THE TICKED ROWS. Every other drawer row draws
  something in the scene; these open a page. So: a picture mark on the
  fold, an arrow where a tick box would be, and one line in the fold,
  "Saved pictures: each opens on its own page." (board F). The fold is
  closed when the room opens, and its count shows.
- BACK RETURNS TO THE ROOM, with the room as it was left (the drawer
  open at that fold is enough). Today `po_gallery_from` carries the way
  from the gallery into a room; this is the other direction.
- THE RIGHT SHAPE: a phone opens a card's portrait twin and a desktop
  its landscape one, by the gallery's existing rule (inCurrentMode, the
  phone setting); a "none" card is not offered on a phone.
- FIND finds them: typing a picture's words ("Artemis") opens its fold.
- Each fold leaves its row when the encounter that replaces it is
  built. Say so in the skill.

Skill: part 1 changes interactive-exhibit's drawer rules. The session
may edit the orrery's `skills/interactive-exhibit/SKILL.md`, run
`skills_index.py`, and add the protocol's version entry, for one bump,
1.35 to 1.36. Per the records skill's carried item on L-508: once Tony
has installed a skill or pasted the protocol, any later change to it
gets a new number, even in the same session.

Checks: the gallery maintenance run, green; the drawer walk
(`tools/headless/walk_solar_system_drawer.js`) extended to the picture
folds and shown failing on a planted fault (a picture row with a tick
box, or a fold open when the room opens).

## Part 2: the lobby, and the subject pages collapsed (index.html)

What a phone visitor sees, top to bottom (board D):

1. The site's name, gold, with the About (i) button; under it one line,
   "The solar system, Earth and the nearby stars in 3D, from real science
   data." This replaces the welcome sentence served from
   `gallery/gallery_config.json` ("sentence"); change it there, not in
   the page.
2. The Solar System room's picture (`gallery/pictures/solar_system_room.jpg`),
   edge to edge, as today.
3. A small "SOLAR SYSTEM" kicker, the title "Today's sky, live", the
   sentence "The Sun, the planets, Earth and its Moon. Turn it with your
   finger.", and one Explore button. Picture and button open the room,
   as Enter does today. The title replaces `LOBBY_START_TITLE`; the
   sentence is the start card's served description in
   `gallery/gallery_metadata.json` (card `solar_system`), changed there.
4. "More to explore": two picture strips, each one tap to its subject
   page. Earth System Science, "Our changing climate, from measured
   data.", teal edge; Stars, "Our nearest stars and their planets, in
   3D.", violet edge. The Solar System subject row is not drawn in the
   lobby; its page stays for old links.
5. Featured, exactly as today (L-517 ruling 6; Tony edits it in the
   existing editor).
6. The line about Paloma ("An orrery is a model of the solar system. I
   built this one for my daughter Paloma, whose name is Spanish for
   dove.", served as "name_note"), moved from under the title to just
   above the guest book (L-447's line stays on the page).
7. The guest book, as today.

The two strip pictures: draw them from the site's own cards, with a
small script kept in the gallery's `tools/` beside the other headless
tools, so they can be redrawn. Earth System: one stripe per year, the
mean of each year's monthly anomalies in `gallery/warming_stripes.json`,
with that card's own colour scale and no colour bar. Stars: the stars of
`gallery/3d_stars_distance_20ly_social.json` laid flat (x against y),
on black, with the card's own colours. Save them under
`gallery/pictures/`. They carry no numbers; each one's alt text names
the card it comes from. The coordinator drew both this way on the canvas.

The subject pages (every room screen, all three subjects):

- A room with no cards in the current mode is not listed. Today such a
  room shows greyed as "under construction"; that line goes, and so do
  the "N rooms under construction" counts. A room reappears by itself
  when it gets a card. (L-517 ruling 3.)
- On the Solar System subject page, the heading reads "Solar System
  pictures and animations", and one line under it says what they are:
  "Moments saved from the desktop orrery, each on its own date. For
  where everything is today, open the live sky." The live card stays
  first, titled "Today's sky, live". (Ruling 3, relabel.)
- Elsewhere in the lobby and on these pages, a visitor reads none of
  "exhibits", "rooms" or "live in 3D" where a plain word will do. Keep
  the change to the lobby and the subject pages; the card viewer and
  interactive.html are not part of this.

The desktop: the same order, in one centred column; the build chooses
the width and Tony judges it (Mode 5).

Also in part 2, from Tony's phone look at part 1 (his copy
`WHERE_WE_ARE_11-8-26_1249_run_record.md`): "remove L view from the
mobile. i can't do it in the gallery editor. the landscape view is too
crowded and not readable on the phone." The card is
`pluto_barycenter_system_20260208_1957` (16:9). It and the portrait
`pluto_barycenter_social_view_20260211_0031` are not twins (different
dates, no sibling), so the gallery's rule offers both on a phone. A phone
offers neither the landscape card's row in Pluto's fold nor its card in
the lists; a desktop keeps both cards. The build chooses the means from
what the gallery's rule already reads (inCurrentMode in index.html, its
mirror in gallery/picture_folds.js), not a new store, and names it in the
report.

Checks: the gallery maintenance run, green, read from its output. The
lobby has no checker of its own (L-367 (no checker opens a room) and
L-423 (the website's checks) record the gap); headless shots at 390 x
844 and 1280 x 800 on a throwaway copy, in the report, are the check
this part can show. Name what each shot proves.

## Close (both parts)

As the records skill says: L-517 and Where We Are, section by section;
the report lists every file changed with its edit count, the token count
as Claude Code prints it, Tony's run order, his phone-look list (what to
tap, what he should see), and the Tony-action rollup. Commit and push are
Tony's.
