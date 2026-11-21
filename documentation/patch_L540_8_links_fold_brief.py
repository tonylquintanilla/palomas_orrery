"""
patch_L540_8_links_fold_brief.py -- places the brief and start prompt for
the Code session that builds the Links fold, and records Tony's ruling of
Nov 21 on L-540 and on Where We Are.

Built on 08656fdc at https://github.com/tonylquintanilla/palomas_orrery
(branch main), after patch_L540_7_close_record.py, with gallery 5a7df273.

RUN COMMAND
    Run patch_L540_7_close_record.py first: this one edits what it wrote.
    Save this file in the orrery folder (palomas_orrery_for_github), open
    it in VS Code and click Run:

        python patch_L540_8_links_fold_brief.py

    Success: two "new" lines, one "ok" line per edit, "patch applied",
    then "ok" for ledger_index.py and the document-caps check.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop, and delete
    the two new documents.
    Once it has run, move it to the documentation folder.

What it changes:
    documentation/COORD_L540_links_fold_brief_20261121.md (new): the
        brief for one Claude Code session in the website.
    documentation/PROMPT_code_L540_links_fold_20261121.md (new): its
        starting prompt, to paste into Claude Code.
    LEDGER_CONSOLIDATED.md: on L-540, Tony's ruling of Nov 21 (a link
        sits in a Links fold beside its body; the Outside Links room
        dropped), and the Gap rewritten.
    documentation/WHERE_WE_ARE.md: the Outside Links step in "Needs you
        now" replaced by starting the Code session.

Written November 21, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

NEW_FILES = [('documentation/COORD_L540_links_fold_brief_20261121.md',
  '<!-- Doc-Kind: hand | Brief for one Claude Code session: a Links fold '
  "beside a body's row, in the Solar System room's drawer and in the "
  'gallery editor (L-540). -->\n'
  "# Brief: a Links fold beside a body's row (L-540)\n"
  '\n'
  'Built on orrery 08656fdc at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'
  'and gallery 5a7df273 at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch '
  'main\n'
  'for both). Written November 21, 2026 by the coordinating session '
  '(Claude\n'
  'Opus 5.5) for ONE Claude Code session in the WEBSITE repository.\n'
  '\n'
  "Read before building, and say back which you read: the website's\n"
  'CLAUDE.md and the files it points to; the skills `interactive-exhibit`\n'
  "(a room's drawer and its folds), `gallery-pipeline` (the gallery "
  'editor\n'
  'and gallery/gallery_metadata.json), `safe-file-editing`, and\n'
  '`ledger-and-session-records` (the closing report). Then this brief, '
  'and\n'
  "L-540 (a reel on a Featured card) in the orrery's "
  'LEDGER_CONSOLIDATED.md,\n'
  'read whole.\n'
  '\n'
  '## 1. The ruling\n'
  '\n'
  'Tony, by voice, November 21, 2026, morning, after the coordinating\n'
  'session had designed an Outside Links ROOM the night before:\n'
  '\n'
  '> "what I was thinking is that outside links should fit like saved '
  'scenes.\n'
  "> Or saved pictures. ... they're like special links but they are "
  'connected\n'
  '> to specific bodies. So, for example, the Instagram reel about ... '
  'the\n'
  "> escapade missions sit under Earth, wouldn't that be the right "
  'setup?"\n'
  '\n'
  "Asked whether ESCAPADE's reel goes under Mars or Earth:\n"
  '\n'
  '> "I think it depends on the encounter. You know, like the Earth '
  'encounter\n'
  '> belongs under Earth, and eventually, when we get to ... the entry, '
  'that\n'
  '> would be Mars."\n'
  '\n'
  'Then, 09:16: "I\'m inclined to do the links fold first so I can clean '
  'up\n'
  'the tree." 09:18: "Yes" to this brief.\n'
  '\n'
  "So: a LINK CARD (a card whose `live` address is another website's,\n"
  'L-540) sits beside the row of the body its subject is about -- for a\n'
  'reel, the body of the encounter it shows -- in a fourth fold, LINKS, as '
  'a\n'
  'scene sits in Scenes and a picture in Saved pictures. The Outside '
  'Links\n'
  'room is DROPPED: it was never made, and no code should look for it '
  'after\n'
  'this session.\n'
  '\n'
  '## 2. What exists at gallery 5a7df273 (read it; do not trust this '
  'list)\n'
  '\n'
  '- `gallery/picture_folds.js`: `foldsFrom` sorts the cards with a place\n'
  '  (`drawer_row`) into folds of three kinds, "scenes", "encounters" and\n'
  '  "pictures"; `foldsAt` gives a row\'s folds in that order; `WORDS` '
  'holds\n'
  "  the visitor's words; `href(v)` gives a live card its own address;\n"
  '  `searchWords` feeds Find; `returnState`/`returnFor` keep the room '
  'for\n'
  '  Back.\n'
  '- `interactive.html`: `ssPictureFold` and `ssPictureFoldOne` draw a '
  'fold\n'
  '  (its head, its line, one link per card, a mark per kind:\n'
  '  SCENE_MARK, ENCOUNTER_MARK, PICTURE_MARK); `ssPicOpen` keeps the '
  'room\n'
  '  for Back before a card opens in the same tab.\n'
  '- `index.html`: a card whose `live` starts with http:// or https:// is\n'
  '  `outside` and `page`; the lobby opens it in a new tab\n'
  '  (`loadVisualization`). Featured is unchanged by this brief.\n'
  '- `tools/drawer_places.py`: `is_scene`, `is_encounter`, `fold_order`,\n'
  "  `places_of`, the editor's view of the drawer. "
  '`tools/gallery_editor.py`:\n'
  "  `DRAWER_FOLDS` (Scenes, Encounters, Saved pictures) draws each row's\n"
  '  folds in the Solar System door; "Lobby only" first, open, for Solar\n'
  "  System cards with no place; `LINKS_ROOM = 'outside_links'`; Card > "
  'New\n'
  '  Link Card... (`_new_link_card`) puts a card in that room if it '
  'exists,\n'
  '  else Storage. A card in the Solar System room already has Places in '
  'the\n'
  '  drawer, Add place... and Remove place.\n'
  '- `tools/link_card.py` and `tools/test_link_card.py` (the gallery '
  "run's\n"
  '  "Link cards" row). Its real-file check REFUSES a link card with a\n'
  '  drawer place; that changes here.\n'
  '- The checks that watch the drawer: '
  '`documentation/smoke_picture_folds.js`\n'
  '  (worked cases and the real files, printed fold by fold),\n'
  '  `tools/test_drawer_places.py`, `tools/test_scene_card.py`, and the\n'
  "  gallery run's walk of the drawer (tools/headless).\n"
  '- The one link card today: `escapade_reel`, room solar_system, no '
  'place,\n'
  '  Featured, under Lobby only.\n'
  '\n'
  '## 3. What to build\n'
  '\n'
  "A. THE ROOM'S DRAWER (website).\n"
  '1. `picture_folds.js`: a fourth kind, "links": a link card (live '
  'address\n'
  "   another website's, by the lobby's own test) with a place goes in "
  'its\n'
  "   row's Links fold; a fold function of its own (as "
  '`encounterFoldFor`);\n'
  '   `foldsAt` order Scenes, Encounters, LINKS, Saved pictures (beside '
  'the\n'
  '   encounter it shows); a count like the others; `searchWords` marks '
  'it,\n'
  "   so Find matches a link's title; a link card with a place is no "
  'longer\n'
  '   a saved picture.\n'
  "2. `WORDS` (words for Tony's phone look, marked so): `links: "
  '"Links"`,\n'
  '   `linksLine: "Each link opens another website in a new tab."`\n'
  '3. `interactive.html`: the Links fold drawn as the others, with a mark '
  'of\n'
  '   its own (LINK_MARK, an arrow leaving a box, in the same 14x12 SVG\n'
  '   style); each entry an `<a>` with `target="_blank"` and\n'
  '   `rel="noopener"`, and NO `ssPicOpen`: nothing kept for Back, since\n'
  '   the room stays open in its own tab.\n'
  '\n'
  'B. THE EDITOR (website).\n'
  '4. `drawer_places.py`: `is_link(card)` (the same test), and '
  '`fold_order`\n'
  "   in the website's order: scenes, encounters, links, pictures.\n"
  "5. `gallery_editor.py`: `DRAWER_FOLDS` gains ('links', 'Links') in "
  'that\n'
  "   order. New Link Card asks WHICH ROW (a list of the drawer's rows, "
  'as\n'
  '   Add place... offers them, plus "no row: Lobby only"); with a row '
  'the\n'
  '   card is saved in room solar_system with that `drawer_row`; with '
  'none,\n'
  '   in Storage, as any new card (Tony, 2026-11-20, 23:23). Remove\n'
  '   `LINKS_ROOM` and its words.\n'
  '6. `link_card.py`: `new_entry` takes the place; its docstring says '
  'where\n'
  "   a link card lives now. `test_link_card.py`: a link card's place "
  'must\n'
  '   name a row the drawer lists (or none); worked case for a new card '
  'with\n'
  '   a place; the self-test still breaks it two ways.\n'
  '\n'
  'C. THE CHECKS.\n'
  '7. `smoke_picture_folds.js`: worked cases for a link with a place (its\n'
  '   fold, its order after Encounters, its count, Find, its href the '
  'live\n'
  '   address) and a link with none (no fold); the real-file print shows '
  'the\n'
  '   Links fold. `test_drawer_places.py`: `is_link` and the new order.\n'
  '8. Run the whole gallery run (`gallery_maintenance_run.py`) before\n'
  "   reporting, and report each row's result by name.\n"
  '\n'
  'D. NOT IN THIS SESSION.\n'
  '- Moving the reel. Tony does it in the editor after the push: select\n'
  '  "ESCAPADE: the twins\' story (Instagram reel)" under Lobby only, Add\n'
  '  place... Earth, Save All, push. Say so in the report; do not edit '
  'his\n'
  '  card file for him.\n'
  '- The lobby, Featured, the encounter player, any skill file. The skill\n'
  '  text for link cards and the Links fold is owed to '
  '`interactive-exhibit`\n'
  '  and `gallery-pipeline` at their next bumps; name what each should '
  'say\n'
  '  in the report, do not edit the skills.\n'
  '- The orrery repository.\n'
  '\n'
  '## 4. Delivery\n'
  '\n'
  '- Work in the website repository only, through the python_work door.\n'
  '  Record its base (`git rev-parse HEAD`, `git ls-remote origin HEAD`) '
  'and\n'
  '  stop if it is not 5a7df273 or a descendant that leaves these files '
  'as\n'
  '  described; name what moved.\n'
  "- Edit the files in Tony's working copy, ASCII and LF, each change\n"
  '  stamped where it is made; Tony commits and pushes. Nothing is pushed\n'
  '  by the session. Each file changed is named in the report.\n'
  "- Tony's phone look after his push: the Earth row's Links fold on his\n"
  '  phone, its words, its mark, and a tap opening the reel in a new tab.\n'
  '  The words are his to change then.\n'
  '\n'
  '## 5. The report\n'
  '\n'
  'Plain words, in this order: what was built, file by file; the gallery\n'
  "run's rows by name with their results; what Tony does next (the push,\n"
  'Add place... Earth on the reel, the phone look); the skill text owed;\n'
  "anything this brief got wrong. It ends with the session's token count "
  'as\n'
  "Claude Code's /cost prints it (Token Economy), and opens with the "
  'anchor\n'
  "line: built on <base SHA> at the website's URL; ready at <new SHA or\n"
  '"not pushed">.\n'),
 ('documentation/PROMPT_code_L540_links_fold_20261121.md',
  '<!-- Doc-Kind: hand | The starting prompt for the Claude Code session '
  'that builds the Links fold (L-540), from its brief. -->\n'
  '# Starting prompt: the Links fold, the Code session\n'
  '\n'
  'Built on orrery 08656fdc at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'
  'and gallery 5a7df273 at\n'
  'https://github.com/tonylquintanilla/tonyquintanilla.github.io. Written\n'
  'Nov 21, 2026 by the coordinating session (Claude Opus 5.5).\n'
  '\n'
  'Open Claude Code in the python_work folder (the door), Opus, high\n'
  'effort, and paste everything below the line.\n'
  '\n'
  '---\n'
  '\n'
  'The work is in the website repository (tonyquintanilla.github.io).\n'
  'Follow its CLAUDE.md from its first step, and record its base.\n'
  '\n'
  'Your brief is documentation/COORD_L540_links_fold_brief_20261121.md in\n'
  'the orrery (palomas_orrery_for_github). Read it whole, then L-540 (a\n'
  "reel on a Featured card) on the orrery's ledger, and say back which\n"
  'rule files and skills you read.\n'
  '\n'
  "Work in two parts. Part 1: the room's drawer and its check (the "
  "brief's\n"
  'A and its part of C). Stop with a report and wait for my go-ahead.\n'
  'Part 2: the editor and its checks (B and the rest of C), then the '
  'whole\n'
  'gallery run, and the closing report the brief asks for. Edit my '
  'working\n'
  'copy; I commit and push.\n'
  '\n'
  'Plain words in every report, one question at most.\n')]

EDITS = [('LEDGER_CONSOLIDATED.md',
  "**Gap:** Tony's do-steps and phone look. The gallery-pipeline skill\n"
  "gains link cards, the Outside Links room and the editor's layout at "
  'its\n'
  'next bump (method, not a ruling).',
  '- **Tony, by voice, Nov 21, morning: a link sits beside its body, and\n'
  '  the Outside Links room is dropped.** "outside links should fit like\n'
  "  saved scenes. Or saved pictures. ... they're like special links but\n"
  '  they are connected to specific bodies. So, for example, the '
  'Instagram\n'
  '  reel about ... the escapade missions sit under Earth"; on Earth or\n'
  '  Mars: "I think it depends on the encounter ... the Earth encounter\n'
  '  belongs under Earth, and eventually, when we get to ... the entry,\n'
  '  that would be Mars." 09:16: "I\'m inclined to do the links fold '
  'first\n'
  '  so I can clean up the tree"; 09:18, "Yes" to a brief. So a link card\n'
  '  sits in a fourth fold, Links, beside the row of the body of the\n'
  "  encounter it shows, in the room's drawer and in the editor. The\n"
  '  do-step above for the Outside Links room is WITHDRAWN (the room was\n'
  '  never made). Brief:\n'
  '  documentation/COORD_L540_links_fold_brief_20261121.md; start prompt:\n'
  '  documentation/PROMPT_code_L540_links_fold_20261121.md, for one '
  'Claude\n'
  '  Code session in the website.\n'
  '**Gap:** the Code session (the Links fold in the drawer and the '
  'editor,\n'
  "New Link Card asking the row), Tony's Add place... Earth on the reel,\n"
  "his phone look, and ESCAPADE's scene remade (L-542). The\n"
  'gallery-pipeline and interactive-exhibit skills gain link cards, the\n'
  "Links fold and the editor's layout at their next bumps (method, not a\n"
  'ruling).'),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) In the gallery editor: New Room... "Outside Links" with '
  "nothing selected, then move the reel's card into it (Move to Room...); "
  'Save All, push, and look on your phone (L-540 (a reel on a Featured '
  'card)).*\n',
  '> - *(do) Start a Claude Code session in the website with '
  'documentation/PROMPT_code_L540_links_fold_20261121.md: the Links fold, '
  'so the reel sits under Earth. The Outside Links room is dropped (L-540 '
  '(a reel on a Featured card)).*\n')]


def main():
    for rel, text in NEW_FILES:
        path = os.path.join(HERE, rel)
        if os.path.exists(path):
            with open(path, 'rb') as f:
                have = f.read().replace(b'\r\n', b'\n')
            if have != text.encode('ascii'):
                print("ERROR: %s already exists and differs from this patch's "
                      "copy (a copy saved from a download?). Delete it and run "
                      "again. NOTHING was written." % rel)
                sys.exit(1)
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "website folder? NOTHING was written." % name)
            sys.exit(1)
        if name not in staged:
            with open(path, 'rb') as f:
                raw = f.read()
            staged[name] = [raw.replace(b'\r\n', b'\n'), b'\r\n' in raw]
        text = staged[name][0]
        o, n = old.encode('ascii'), new.encode('ascii')
        c = text.count(o)
        if c != 1:
            print("ANCHOR FAIL: %s, expected 1 match, found %d: %r\n"
                  "If this patch already ran, there is nothing to do. If "
                  "patch_L540_7_close_record.py has not run, run it first. "
                  "NOTHING was written." % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, old.strip().splitlines()[0][:60]))
    for rel, text in NEW_FILES:
        path = os.path.join(HERE, rel)
        if os.path.exists(path):
            print("ok   %s: already there, identical" % rel)
            continue
        with open(path, 'wb') as f:
            f.write(text.encode('ascii'))
        print("new  %s" % rel)
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, name), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d new files, %d edits in %d files)"
          % (len(NEW_FILES), len(EDITS), len(staged)))
    for tool in (["ledger_index.py"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1500:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "tell the session what it printed." % (' '.join(tool),
                                                        r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))

if __name__ == '__main__':
    main()
