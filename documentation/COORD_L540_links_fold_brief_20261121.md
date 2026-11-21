<!-- Doc-Kind: hand | Brief for one Claude Code session: a Links fold beside a body's row, in the Solar System room's drawer and in the gallery editor (L-540). -->
# Brief: a Links fold beside a body's row (L-540)

Built on orrery 08656fdc at https://github.com/tonylquintanilla/palomas_orrery
and gallery 5a7df273 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main
for both). Written November 21, 2026 by the coordinating session (Claude
Opus 5.5) for ONE Claude Code session in the WEBSITE repository.

Read before building, and say back which you read: the website's
CLAUDE.md and the files it points to; the skills `interactive-exhibit`
(a room's drawer and its folds), `gallery-pipeline` (the gallery editor
and gallery/gallery_metadata.json), `safe-file-editing`, and
`ledger-and-session-records` (the closing report). Then this brief, and
L-540 (a reel on a Featured card) in the orrery's LEDGER_CONSOLIDATED.md,
read whole.

## 1. The ruling

Tony, by voice, November 21, 2026, morning, after the coordinating
session had designed an Outside Links ROOM the night before:

> "what I was thinking is that outside links should fit like saved scenes.
> Or saved pictures. ... they're like special links but they are connected
> to specific bodies. So, for example, the Instagram reel about ... the
> escapade missions sit under Earth, wouldn't that be the right setup?"

Asked whether ESCAPADE's reel goes under Mars or Earth:

> "I think it depends on the encounter. You know, like the Earth encounter
> belongs under Earth, and eventually, when we get to ... the entry, that
> would be Mars."

Then, 09:16: "I'm inclined to do the links fold first so I can clean up
the tree." 09:18: "Yes" to this brief.

So: a LINK CARD (a card whose `live` address is another website's,
L-540) sits beside the row of the body its subject is about -- for a
reel, the body of the encounter it shows -- in a fourth fold, LINKS, as a
scene sits in Scenes and a picture in Saved pictures. The Outside Links
room is DROPPED: it was never made, and no code should look for it after
this session.

## 2. What exists at gallery 5a7df273 (read it; do not trust this list)

- `gallery/picture_folds.js`: `foldsFrom` sorts the cards with a place
  (`drawer_row`) into folds of three kinds, "scenes", "encounters" and
  "pictures"; `foldsAt` gives a row's folds in that order; `WORDS` holds
  the visitor's words; `href(v)` gives a live card its own address;
  `searchWords` feeds Find; `returnState`/`returnFor` keep the room for
  Back.
- `interactive.html`: `ssPictureFold` and `ssPictureFoldOne` draw a fold
  (its head, its line, one link per card, a mark per kind:
  SCENE_MARK, ENCOUNTER_MARK, PICTURE_MARK); `ssPicOpen` keeps the room
  for Back before a card opens in the same tab.
- `index.html`: a card whose `live` starts with http:// or https:// is
  `outside` and `page`; the lobby opens it in a new tab
  (`loadVisualization`). Featured is unchanged by this brief.
- `tools/drawer_places.py`: `is_scene`, `is_encounter`, `fold_order`,
  `places_of`, the editor's view of the drawer. `tools/gallery_editor.py`:
  `DRAWER_FOLDS` (Scenes, Encounters, Saved pictures) draws each row's
  folds in the Solar System door; "Lobby only" first, open, for Solar
  System cards with no place; `LINKS_ROOM = 'outside_links'`; Card > New
  Link Card... (`_new_link_card`) puts a card in that room if it exists,
  else Storage. A card in the Solar System room already has Places in the
  drawer, Add place... and Remove place.
- `tools/link_card.py` and `tools/test_link_card.py` (the gallery run's
  "Link cards" row). Its real-file check REFUSES a link card with a
  drawer place; that changes here.
- The checks that watch the drawer: `documentation/smoke_picture_folds.js`
  (worked cases and the real files, printed fold by fold),
  `tools/test_drawer_places.py`, `tools/test_scene_card.py`, and the
  gallery run's walk of the drawer (tools/headless).
- The one link card today: `escapade_reel`, room solar_system, no place,
  Featured, under Lobby only.

## 3. What to build

A. THE ROOM'S DRAWER (website).
1. `picture_folds.js`: a fourth kind, "links": a link card (live address
   another website's, by the lobby's own test) with a place goes in its
   row's Links fold; a fold function of its own (as `encounterFoldFor`);
   `foldsAt` order Scenes, Encounters, LINKS, Saved pictures (beside the
   encounter it shows); a count like the others; `searchWords` marks it,
   so Find matches a link's title; a link card with a place is no longer
   a saved picture.
2. `WORDS` (words for Tony's phone look, marked so): `links: "Links"`,
   `linksLine: "Each link opens another website in a new tab."`
3. `interactive.html`: the Links fold drawn as the others, with a mark of
   its own (LINK_MARK, an arrow leaving a box, in the same 14x12 SVG
   style); each entry an `<a>` with `target="_blank"` and
   `rel="noopener"`, and NO `ssPicOpen`: nothing kept for Back, since
   the room stays open in its own tab.

B. THE EDITOR (website).
4. `drawer_places.py`: `is_link(card)` (the same test), and `fold_order`
   in the website's order: scenes, encounters, links, pictures.
5. `gallery_editor.py`: `DRAWER_FOLDS` gains ('links', 'Links') in that
   order. New Link Card asks WHICH ROW (a list of the drawer's rows, as
   Add place... offers them, plus "no row: Lobby only"); with a row the
   card is saved in room solar_system with that `drawer_row`; with none,
   in Storage, as any new card (Tony, 2026-11-20, 23:23). Remove
   `LINKS_ROOM` and its words.
6. `link_card.py`: `new_entry` takes the place; its docstring says where
   a link card lives now. `test_link_card.py`: a link card's place must
   name a row the drawer lists (or none); worked case for a new card with
   a place; the self-test still breaks it two ways.

C. THE CHECKS.
7. `smoke_picture_folds.js`: worked cases for a link with a place (its
   fold, its order after Encounters, its count, Find, its href the live
   address) and a link with none (no fold); the real-file print shows the
   Links fold. `test_drawer_places.py`: `is_link` and the new order.
8. Run the whole gallery run (`gallery_maintenance_run.py`) before
   reporting, and report each row's result by name.

D. NOT IN THIS SESSION.
- Moving the reel. Tony does it in the editor after the push: select
  "ESCAPADE: the twins' story (Instagram reel)" under Lobby only, Add
  place... Earth, Save All, push. Say so in the report; do not edit his
  card file for him.
- The lobby, Featured, the encounter player, any skill file. The skill
  text for link cards and the Links fold is owed to `interactive-exhibit`
  and `gallery-pipeline` at their next bumps; name what each should say
  in the report, do not edit the skills.
- The orrery repository.

## 4. Delivery

- Work in the website repository only, through the python_work door.
  Record its base (`git rev-parse HEAD`, `git ls-remote origin HEAD`) and
  stop if it is not 5a7df273 or a descendant that leaves these files as
  described; name what moved.
- Edit the files in Tony's working copy, ASCII and LF, each change
  stamped where it is made; Tony commits and pushes. Nothing is pushed
  by the session. Each file changed is named in the report.
- Tony's phone look after his push: the Earth row's Links fold on his
  phone, its words, its mark, and a tap opening the reel in a new tab.
  The words are his to change then.

## 5. The report

Plain words, in this order: what was built, file by file; the gallery
run's rows by name with their results; what Tony does next (the push,
Add place... Earth on the reel, the phone look); the skill text owed;
anything this brief got wrong. It ends with the session's token count as
Claude Code's /cost prints it (Token Economy), and opens with the anchor
line: built on <base SHA> at the website's URL; ready at <new SHA or
"not pushed">.
