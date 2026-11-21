"""
patch_L529_3_skills_and_protocol.py -- the skill text two builds owe,
in one bump, and the protocol's v3.144: interactive-exhibit 1.44
(encounters, and a card's fold beside a body) and gallery-pipeline 1.3
(the editor's cards), from L-529 (guided encounters) and L-540 (a reel
on a Featured card).

Built on bd70f5844770 at https://github.com/tonylquintanilla/palomas_orrery
(branch main) with Tony's ledger and Where We Are as they stood on his
disk on Nov 21, 14:20 (the Links fold session's records, not yet
pushed), and gallery 828362fd read for the code. Written by the
coordinating session (Claude Fable 5.2) under safe-file-editing 1.14
and ledger-and-session-records 1.23.

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L529_3_skills_and_protocol.py

    Success: one "ok" line per edit, "patch applied", then four tools,
    each printing "ok": skills_index.py, ledger_index.py,
    skills_index.py --check and doc_index.py --caps.
    Failure: an "ERROR:" or "ANCHOR FAIL" line, and NOTHING is written.
    Undo after a success: Discard Changes in GitHub Desktop.
    Once it has run, move it to the documentation folder.

WHY
    By the records skill's binding rule a skill bump travels as four
    steps in one commit: the SKILL.md, skills_index.py, a protocol
    version entry, and the commit. Neither build's brief had its Code
    session write a skill; each listed its rules on the ledger. One
    bump for both, so the skills are reinstalled once.

WHAT IT CHANGES (27 edits, 7 files; no code)
    skills/interactive-exhibit/SKILL.md, 1.43 -> 1.44. Two new rules:
        An encounter is a package played in a room of its own, and A
        card beside a body sits in a fold of its kind. To stay at its
        cap of 738 lines, the 1.41 entry and four field notes of
        September move, word for word, to the histories.
    skills/gallery-pipeline/SKILL.md, 1.2 -> 1.3. One new section, The
        Editor's Cards: scenes, encounters, links, with Tony's ruling
        of Nov 21, 14:17, "In Storage for consistency." To stay at its
        cap of 160 lines, Shared Conventions and seven field notes
        move, word for word, to the histories.
    documentation/SKILL_HISTORIES.md: receives what moved; a new
        section for gallery-pipeline.
    PROJECT_INSTRUCTIONS.md: the v3.144 entry, the header's version,
        date and SHA; v3.141 moves down. skills_index.py then rewrites
        the manifest's two rows and the exhibit skill's read plan.
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md: receives v3.141.
    LEDGER_CONSOLIDATED.md: L-540, Tony's Storage ruling and the skill
        text written; L-529, the skill text written, and the three
        rules that also belong in other skills.
    documentation/WHERE_WE_ARE.md: the header line, and one new line in
        "Needs you now" (the reinstall and the paste). 130 lines above
        the marker, its cap. Nothing below the marker is touched.

NOT in this patch, and why: gallery-cache-builder, safe-file-editing
and horizons-orbital-mechanics. Every rule the encounter's build
learned is in interactive-exhibit 1.44, where an encounter's builder
reads it. Three of them also belong in those skills; each waits for
that skill's next version, named on L-529, so Tony reinstalls two
skills today and not five.

AFTER IT RUNS
    1. (do) Move this file into the documentation folder.
    2. (do) Commit and push the orrery, not while a night is running.
    3. (do) Reinstall two skills, interactive-exhibit and
       gallery-pipeline (Plugins, in the claude.ai sidebar), and paste
       PROJECT_INSTRUCTIONS.md into the Project's instructions on
       claude.ai.

Tested on a copy of the orrery at bd70f584 with the disk's ledger and
page: every edit applied, a second run refused, and the four tools
passed; the exhibit skill ends at 738 lines and the pipeline skill at
160, each at its cap.

Written November 21, 2026 with Anthropic's Claude Fable 5.2.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [('skills/interactive-exhibit/SKILL.md',
  "a Lagrange point's marker and box, a name's side (label_side_for)\n---\n",
  "a Lagrange point's marker and box, a name's side (label_side_for); an "
  'encounter (data/encounters/, tools/encounter_fetch.py, its player); a '
  "card's fold beside a row (Scenes, Encounters, Links)\n"
  '---\n'),
 ('skills/interactive-exhibit/SKILL.md',
  "Skill version: 1.43 | 2026-11-19, with Anthropic's Claude Opus 5.5, at\n",
  "Skill version: 1.44 | 2026-11-21, with Anthropic's Claude Fable 5.2, at\n"
  'palomas_orrery @ bd70f584 and gallery @ 828362fd. v1.44 (L-529, guided\n'
  'encounters; L-540, a reel on a Featured card) adds two rules. AN\n'
  'ENCOUNTER IS A PACKAGE PLAYED IN A ROOM OF ITS OWN: a completed pass,\n'
  'its package fetched by hand, its player, its dates read and never\n'
  'typed. And A CARD BESIDE A BODY SITS IN A FOLD OF ITS KIND: Scenes,\n'
  'Encounters, Links, Saved pictures. Written by the coordinating session\n'
  "from the two builds' ledger notes and the gallery at 828362fd, not by\n"
  'their Code sessions. To stay at the cap, the 1.41 entry and four field\n'
  'notes of September (L-291, L-318) moved out.\n'
  "Earlier: 1.43 | 2026-11-19, with Anthropic's Claude Opus 5.5, at\n"),
 ('skills/interactive-exhibit/SKILL.md',
  "Earlier: 1.41 | 2026-11-11, with Anthropic's Claude Opus 5.5, at\n"
  "palomas_orrery @ 87fb472e and gallery @ e21b6746 (the session's bases;\n"
  "Tony's checkpoint pushes since). v1.41 (L-522, document caps, step 2)\n"
  'SPLITS THE SKILL: the rules stay here; what interactive.html does now\n'
  "moved whole, in its own words, into the gallery's\n"
  'INTERACTIVE_AS_BUILT.md, changed in the commit that changes the page and\n'
  "held to the code by the gallery run's As-built names row\n"
  '(tools/check_as_built_names.py). Each of the six long sections leaves\n'
  'one rule and a pointer, the Provenance rule keeping its rules for new\n'
  'work; the anatomy table, the text box, the readability asks and the\n'
  'headless recipe moved with them; the install confirmations went to\n'
  'documentation/SKILL_HISTORIES.md; fires_when is cut to the phrases that\n'
  'make the skill fire. Every old line was accounted for by script: found\n'
  'once in the skill, the reference or the history, or listed with its\n'
  "reason. SEPARATELY, A CORRECTION (L-523, Tony's word of 2026-11-11):\n"
  '"Touch has no hover" was wrong for a 3D scene. Plotly sends a finger\'s\n'
  "tap 5 px off or more as plotly_hover, so a finger's hover after its tap\n"
  'is that tap and opens what a click opens (gallery/tap_hover.js, the\n'
  "gallery run's Tap hover row); and the widened pick is any finger's, in\n"
  'either orientation (Tony: "Yes, any finger").\n'
  'Older entries are in documentation/SKILL_HISTORIES.md, moved there on\n'
  '2026-10-05 (L-418), 2026-10-10 (L-429)',
  'Older entries are in documentation/SKILL_HISTORIES.md, moved there on\n'
  '2026-10-05 (L-418), 2026-10-10 (L-429)'),
 ('skills/interactive-exhibit/SKILL.md',
  'and 2026-11-11 (L-522) and 2026-11-12 (L-527) and\n2026-11-19 (L-297).\n',
  'and 2026-11-11 (L-522) and 2026-11-12 (L-527) and\n'
  '2026-11-19 (L-297) and 2026-11-21 (L-529).\n'),
 ('skills/interactive-exhibit/SKILL.md',
  "  - One picture: the folds and the view's middle [QUALITY]\n",
  "  - One picture: the folds and the view's middle [QUALITY]\n"
  '  - A card beside a body sits in a fold of its kind [QUALITY]\n'),
 ('skills/interactive-exhibit/SKILL.md',
  '  - A guide asks for one action and waits for it [QUALITY]\n',
  '  - A guide asks for one action and waits for it [QUALITY]\n'
  '  - An encounter is a package played in a room of its own [QUALITY]\n'),
 ('skills/interactive-exhibit/SKILL.md',
  "### The Solar System room's drawer: bodies, not shells [QUALITY]\n",
  '### A card beside a body sits in a fold of its kind [QUALITY]\n'
  'A card placed beside a row (`drawer_row`) is listed under that row in a\n'
  'fold of its kind, in this order: Scenes, Encounters, Links, Saved\n'
  "pictures. A fold is drawn only when it has a card. An encounter's card\n"
  "is marked as one. A link's is known by its address being another\n"
  "website's, by the lobby's own test, and it alone may have no place: it\n"
  "is then in no fold. A tap on a scene or an encounter keeps the room's\n"
  'place for Back; a link opens in a new tab and keeps nothing. Find\n'
  'counts each kind by its own name. The logic is\n'
  "`gallery/picture_folds.js`, held by the run's Picture folds row; the\n"
  'drawer walk is no gate and is kept green all the same (L-521).\n'
  "As built: the gallery's `INTERACTIVE_AS_BUILT.md`.\n"
  '\n'
  "### The Solar System room's drawer: bodies, not shells [QUALITY]\n"),
 ('skills/interactive-exhibit/SKILL.md',
  '### The touch path is not the mouse path [QUALITY]\n',
  '### An encounter is a package played in a room of its own [QUALITY]\n'
  'An encounter is a COMPLETED pass, opened from the fold of the body it\n'
  "is centred on; craft that pass together share one. The body's Hill\n"
  'sphere sets its window and opening view, a craft that loitered at its\n'
  'edge entering at its last crossing inward; each view runs on an even\n'
  'clock (L-529; `documentation/DESIGN_encounters_20261120.md`).\n'
  '- THE PACKAGE lives under `data/encounters/`, written by hand by\n'
  "  `tools/encounter_fetch.py`: JPL's positions and velocities around the\n"
  '  centre, every body at the same moments, so each frame is a moment JPL\n'
  '  was asked for. It refuses a body JPL names otherwise, and a second\n'
  '  run with the same answer writes nothing. The night never runs, swaps\n'
  "  or commits it; the run's Encounters row holds each pass to the plan's\n"
  "  event on the craft's entry.\n"
  "- NOTHING IS TYPED: a pass's date is read from the plan, whose moments\n"
  "  are on JPL's clock (TDB) and are converted before they print as UTC\n"
  '  (L-541); the card names the package, the centre and the craft.\n'
  '- THE PLAYER applies each frame with `Plotly.update`; `Plotly.animate`\n'
  '  redraws a 3D scene whole and resets its camera. A room with no\n'
  "  Pyodide waits for the page's load before it draws. Whatever opens a\n"
  '  text box pauses it. Its button answers the press, not the click.\n'
  '- A NON-ASCII MARK in the page is written as its `\\u` escape, and the\n'
  "  file's bytes are checked: an edit tool wrote raw characters instead.\n"
  "As built: the gallery's `INTERACTIVE_AS_BUILT.md`, Encounters.\n"
  '\n'
  '### The touch path is not the mouse path [QUALITY]\n'),
 ('skills/interactive-exhibit/SKILL.md',
  '- 2026-09-10, L-291 step 7: the first Earth card was a COPY -- Copy\n'
  '  Card to Room on the static Earth-and-Moon portrait, then a live URL\n'
  '  -- made because the Studio button was not found. It kept the\n'
  "  portrait's `sibling` stamp, file and size, and index.html's Featured\n"
  '  rule (a 9:16 card yields to a featured sibling) dropped it from the\n'
  '  DESKTOP lobby while the phone showed it. The handoff written the\n'
  '  night before said step 7 had not started: its session never read the\n'
  "  metadata. A replay of the viewer's rule against the served metadata\n"
  '  predicted both screens before Tony looked, and was right. Fixed by\n'
  "  delete, then Studio, then the editor, in that order. The editor's\n"
  '  Reload from disk existed and was not found either (L-288, L-312).\n'
  '- 2026-09-15, L-318 round 3: a drawer row had two targets, an 18 px box\n'
  "  and a name that did what GO did, and Tony's finger kept landing on\n"
  '  the name of an unticked shell -- the camera moved and nothing drew, a\n'
  '  tap that read as doing nothing. Measured in the page before any\n'
  '  design: every pixel around the box belonged to the name. A one-target\n'
  '  row with no box was proposed and withdrawn once Tony described his\n'
  '  use (tick several, then go to one). Measure before you describe.\n'
  '- 2026-09-15, L-318 round 4: Tony read the orphan words as unnecessary\n'
  '  line breaks. Right about the words; measuring showed they cost one or\n'
  "  two lines per box, and the box's WIDTH was the real height. Line\n"
  "  counts written into the patch's notes before the run disagreed with\n"
  '  the run on every row and were corrected before delivery.\n'
  '- 2026-09-15/16, L-318 rounds 5 and 6: Plotly sometimes drew no arrow\n'
  '  to a mid-screen box, and why was not pinned down; the arrow was\n'
  '  removed on the phone instead. The tap fix went the other way -- the\n'
  "  cause was read from Plotly's source first and worked on the first\n"
  "  phone test. Three of five rounds changed something after Tony's eyes;\n"
  '  the sandbox has no WebGL and no phone, and cannot see any of it.\n'
  '\n'
  '## Install and verify\n',
  '\n## Install and verify\n'),
 ('skills/interactive-exhibit/SKILL.md',
  '1.0 to 1.42: documentation/SKILL_HISTORIES.md, under '
  'interactive-exhibit.\n'
  '1.43 was written on 2026-11-19 by the coordinating session for L-297,\n'
  "from the repo's copy of 1.42; a session that loads the account's copy\n"
  'confirms it reads 1.43 before exhibit work.\n',
  '1.0 to 1.43: documentation/SKILL_HISTORIES.md, under '
  'interactive-exhibit.\n'
  '1.44 was written on 2026-11-21 by the coordinating session for L-529\n'
  "and L-540, from the repo's copy of 1.43; a session that loads the\n"
  "account's copy confirms it reads 1.44 before exhibit work.\n"),
 ('skills/gallery-pipeline/SKILL.md',
  'fires_when: Gallery Studio, json_converter, index.html viewer, gallery '
  'cards\n',
  'fires_when: Gallery Studio, json_converter, index.html viewer, gallery '
  "cards, the gallery editor's scene, encounter and link cards\n"),
 ('skills/gallery-pipeline/SKILL.md',
  'Skill version: 1.2 | Cut from tonyquintanilla.github.io @ 89c8bf30 '
  '(code)\n',
  "Skill version: 1.3 | 2026-11-21, with Anthropic's Claude Fable 5.2, at\n"
  'tonyquintanilla.github.io @ 828362fd and palomas_orrery @ bd70f584.\n'
  "v1.3 (L-540; L-529) adds The Editor's Cards. To stay at the cap, Shared\n"
  'Conventions and seven field notes moved out (SKILL_HISTORIES.md).\n'
  'Earlier: 1.2 | Cut from tonyquintanilla.github.io @ 89c8bf30 (code)\n'),
 ('skills/gallery-pipeline/SKILL.md',
  '## Deployment\n',
  "## The Editor's Cards: scenes, encounters, links\n"
  '\n'
  'A card that is not a saved picture is a scene, an encounter or a link;\n'
  "tools/gallery_editor.py lists them as the website's drawer does.\n"
  "- A SCENE (New Scene, from a room's shared link) sits in the room\n"
  '  solar_system, its places in drawer_row (Scene cards row; L-542).\n'
  "- AN ENCOUNTER's card names its package, its centre and its craft; its\n"
  '  dates are read from the plan, never typed (Encounters row).\n'
  '- A LINK CARD (New Link Card) is one whose address is another\n'
  "  website's. The command asks which row: with a row the card is saved\n"
  '  in the Solar System room beside it; with none it is saved in\n'
  '  Storage, unseen until placed (Tony, 2026-11-21: "In Storage for\n'
  '  consistency."). Link cards, Drawer places and Picture folds rows.\n'
  'The editor holds the card file in memory: after anything else writes\n'
  'it, File > Reload from disk before Save All.\n'
  '\n'
  '## Deployment\n'),
 ('skills/gallery-pipeline/SKILL.md',
  '## Shared Conventions (duplicated deliberately; masters elsewhere)\n'
  '\n'
  '- Credit line on substantive edits (master: orrery-coding-conventions).\n'
  '- ASCII/LF for Python deliverables (master: safe-file-editing).\n'
  '- Distance hover text includes AU alongside km (master:\n'
  "  orrery-coding-conventions); Studio's km-suffix title gate keeps\n"
  '  exact-km / M-km tiers inside the gate with a range-auto fallback.\n'
  '\n'
  '## Field Notes\n',
  '## Field Notes\n'),
 ('skills/gallery-pipeline/SKILL.md',
  "- JS: JSON.stringify(undefined).substring() crashes; guard with || ''.\n"
  '- position: fixed escapes CSS containment; position: absolute stays\n'
  '  inside the parent.\n'
  '- Plotly.js native touch works on mobile without custom code.\n'
  '- D-pad pan arrows: 2D uses Plotly.relayout on axis ranges; 3D shifts\n'
  '  camera eye/center.\n'
  '- DEFAULT_CONFIG changes have wide blast radius',
  '- DEFAULT_CONFIG changes have wide blast radius'),
 ('skills/gallery-pipeline/SKILL.md',
  '- Presets must preserve scenario-specific settings (KMZ link, custom\n'
  '  title) -- presets set general layout only.\n'
  '- Animated plots: strip_hidden_traces requires frame trace-index\n'
  '  remapping, or stripped portrait exports animate the wrong traces.\n'
  '- social_media_export.py is mostly superseded by Studio; its\n'
  '  _parse_hover_html() survives as a shared utility.\n',
  ''),
 ('documentation/SKILL_HISTORIES.md',
  'confirms it reads 1.42 before exhibit work.\n\n## safe-file-editing\n',
  'confirms it reads 1.42 before exhibit work.\n'
  '\n'
  'The 1.41 entry, moved here on 2026-11-21 (L-529), when 1.44 made a\n'
  'fourth resident entry:\n'
  '\n'
  "Earlier: 1.41 | 2026-11-11, with Anthropic's Claude Opus 5.5, at\n"
  "palomas_orrery @ 87fb472e and gallery @ e21b6746 (the session's bases;\n"
  "Tony's checkpoint pushes since). v1.41 (L-522, document caps, step 2)\n"
  'SPLITS THE SKILL: the rules stay here; what interactive.html does now\n'
  "moved whole, in its own words, into the gallery's\n"
  'INTERACTIVE_AS_BUILT.md, changed in the commit that changes the page and\n'
  "held to the code by the gallery run's As-built names row\n"
  '(tools/check_as_built_names.py). Each of the six long sections leaves\n'
  'one rule and a pointer, the Provenance rule keeping its rules for new\n'
  'work; the anatomy table, the text box, the readability asks and the\n'
  'headless recipe moved with them; the install confirmations went to\n'
  'documentation/SKILL_HISTORIES.md; fires_when is cut to the phrases that\n'
  'make the skill fire. Every old line was accounted for by script: found\n'
  'once in the skill, the reference or the history, or listed with its\n'
  "reason. SEPARATELY, A CORRECTION (L-523, Tony's word of 2026-11-11):\n"
  '"Touch has no hover" was wrong for a 3D scene. Plotly sends a finger\'s\n'
  "tap 5 px off or more as plotly_hover, so a finger's hover after its tap\n"
  'is that tap and opens what a click opens (gallery/tap_hover.js, the\n'
  "gallery run's Tap hover row); and the widened pick is any finger's, in\n"
  'either orientation (Tony: "Yes, any finger").\n'
  'Four field notes, moved here on 2026-11-21 (L-529) to keep the skill\n'
  "at its cap; gallery-pipeline's The Editor's Cards now carries the\n"
  "editor's Reload from disk:\n"
  '\n'
  '- 2026-09-10, L-291 step 7: the first Earth card was a COPY -- Copy\n'
  '  Card to Room on the static Earth-and-Moon portrait, then a live URL\n'
  '  -- made because the Studio button was not found. It kept the\n'
  "  portrait's `sibling` stamp, file and size, and index.html's Featured\n"
  '  rule (a 9:16 card yields to a featured sibling) dropped it from the\n'
  '  DESKTOP lobby while the phone showed it. The handoff written the\n'
  '  night before said step 7 had not started: its session never read the\n'
  "  metadata. A replay of the viewer's rule against the served metadata\n"
  '  predicted both screens before Tony looked, and was right. Fixed by\n'
  "  delete, then Studio, then the editor, in that order. The editor's\n"
  '  Reload from disk existed and was not found either (L-288, L-312).\n'
  '- 2026-09-15, L-318 round 3: a drawer row had two targets, an 18 px box\n'
  "  and a name that did what GO did, and Tony's finger kept landing on\n"
  '  the name of an unticked shell -- the camera moved and nothing drew, a\n'
  '  tap that read as doing nothing. Measured in the page before any\n'
  '  design: every pixel around the box belonged to the name. A one-target\n'
  '  row with no box was proposed and withdrawn once Tony described his\n'
  '  use (tick several, then go to one). Measure before you describe.\n'
  '- 2026-09-15, L-318 round 4: Tony read the orphan words as unnecessary\n'
  '  line breaks. Right about the words; measuring showed they cost one or\n'
  "  two lines per box, and the box's WIDTH was the real height. Line\n"
  "  counts written into the patch's notes before the run disagreed with\n"
  '  the run on every row and were corrected before delivery.\n'
  '- 2026-09-15/16, L-318 rounds 5 and 6: Plotly sometimes drew no arrow\n'
  '  to a mid-screen box, and why was not pinned down; the arrow was\n'
  '  removed on the phone instead. The tap fix went the other way -- the\n'
  "  cause was read from Plotly's source first and worked on the first\n"
  "  phone test. Three of five rounds changed something after Tony's eyes;\n"
  '  the sandbox has no WebGL and no phone, and cannot see any of it.\n'
  'The 1.43 install, from Install and verify, 2026-11-21 (L-529):\n'
  '1.43 was written on 2026-11-19 by the coordinating session for L-297,\n'
  "from the repo's copy of 1.42; a session that loads the account's copy\n"
  'confirms it reads 1.43 before exhibit work.\n'
  '\n'
  '## safe-file-editing\n'),
 ('documentation/SKILL_HISTORIES.md',
  '(master: orrery-coding-conventions).\n'
  '- Provenance: Tier-1 = 0 before push; composed text sourced at the\n'
  '  construction site (master: provenance-discipline).\n',
  '(master: orrery-coding-conventions).\n'
  '- Provenance: Tier-1 = 0 before push; composed text sourced at the\n'
  '  construction site (master: provenance-discipline).\n'
  '\n'
  '## gallery-pipeline\n'
  '\n'
  "Moved here on 2026-11-21 (L-540, L-529), when 1.3 added The Editor's\n"
  'Cards and the skill stood at its cap. Shared Conventions, each line\n'
  'held by its master:\n'
  '\n'
  '## Shared Conventions (duplicated deliberately; masters elsewhere)\n'
  '\n'
  '- Credit line on substantive edits (master: orrery-coding-conventions).\n'
  '- ASCII/LF for Python deliverables (master: safe-file-editing).\n'
  '- Distance hover text includes AU alongside km (master:\n'
  "  orrery-coding-conventions); Studio's km-suffix title gate keeps\n"
  '  exact-km / M-km tiers inside the gate with a range-auto fallback.\n'
  '\n'
  'Seven field notes:\n'
  '\n'
  "- JS: JSON.stringify(undefined).substring() crashes; guard with || ''.\n"
  '- position: fixed escapes CSS containment; position: absolute stays\n'
  '  inside the parent.\n'
  '- Plotly.js native touch works on mobile without custom code.\n'
  '- D-pad pan arrows: 2D uses Plotly.relayout on axis ranges; 3D shifts\n'
  '  camera eye/center.\n'
  '- Presets must preserve scenario-specific settings (KMZ link, custom\n'
  '  title) -- presets set general layout only.\n'
  '- Animated plots: strip_hidden_traces requires frame trace-index\n'
  '  remapping, or stripped portrait exports animate the wrong traces.\n'
  '- social_media_export.py is mostly superseded by Studio; its\n'
  '  _parse_hover_html() survives as a shared utility.\n'),
 ('PROJECT_INSTRUCTIONS.md',
  'Tony Quintanilla, PE | Claude | v3.143 | November 19, 2026\n',
  'Tony Quintanilla, PE | Claude | v3.144 | November 21, 2026\n'),
 ('PROJECT_INSTRUCTIONS.md',
  'Cut from 4c44ea87 at https://github.com/tonylquintanilla/palomas_orrery\n',
  'Cut from bd70f584 at '
  'https://github.com/tonylquintanilla/palomas_orrery\n'),
 ('PROJECT_INSTRUCTIONS.md',
  "v3.143 (November 19, 2026): One instruction's wording changed in this\n",
  'v3.144 (November 21, 2026): No rule changed in this document. TWO\n'
  'skill bumps, from L-529 (guided encounters) and L-540 (a reel on a\n'
  "Featured card), by the records skill's binding rule.\n"
  '\n'
  'WHAT PROMPTED IT. Two Claude Code sessions (Claude Opus 5.5), through\n'
  'the python_work door, built in the website: on Nov 20 the first\n'
  "encounter, ESCAPADE's Earth flybys, from Tony's rulings of that day\n"
  '(documentation/DESIGN_encounters_20261120.md), live and looked at on\n'
  'his phone; on Nov 21 the Links fold, pushed at gallery 828362fd.\n'
  'Neither brief had its session write a skill; each session listed the\n'
  'rules it learned on the ledger, and the coordinating session (Claude\n'
  'Fable 5.2) wrote both skills from those notes and the code at that\n'
  'SHA, in one bump, so Tony reinstalls once.\n'
  '\n'
  'WHAT CHANGED. interactive-exhibit 1.43 -> 1.44: An encounter is a\n'
  'package played in a room of its own (a completed pass; its package\n'
  'under data/encounters/, fetched by hand; its dates read from the plan\n'
  "and converted from JPL's clock; its player), and A card beside a body\n"
  'sits in a fold of its kind (Scenes, Encounters, Links, Saved\n'
  'pictures). gallery-pipeline 1.2 -> 1.3, its first bump since July:\n'
  "The Editor's Cards, with Tony's ruling of Nov 21 that a link card made\n"
  'with no row is saved in Storage ("In Storage for consistency."). Each\n'
  'skill stayed at its cap by moving text, word for word, to\n'
  "documentation/SKILL_HISTORIES.md. Three of the encounter build's\n"
  "rules also belong in other skills and wait for those skills' next\n"
  "versions, named on L-529: the plan's clock (horizons-orbital-mechanics,\n"
  'with L-541), the escape rule (safe-file-editing, with L-471) and the\n'
  "package's place (gallery-cache-builder).\n"
  '\n'
  "THE OBLIGATION TRAVELS. This session wrote the two from the repo's\n"
  'copies, 1.43 and 1.2, as the manifest expected. Tony reinstalls both\n'
  '(Plugins, in the claude.ai sidebar) and pastes this version into the\n'
  "Project's instructions on claude.ai; the next session that loads\n"
  'either from the account confirms its copy reads 1.44 or 1.3 before\n'
  'that work.\n'
  '\n'
  'The header stamp and the SHA anchor move with this entry.\n'
  '\n'
  'Version history: v3.141 moves down to\n'
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
  'resident.\n'
  '\n'
  "v3.143 (November 19, 2026): One instruction's wording changed in this\n"),
 ('PROJECT_INSTRUCTIONS.md',
  'v3.141 (November 14, 2026, night): No rule changed in this document.\n'
  'ONE skill bump: earth-system-pipeline 1.2 -> 1.3 (L-001, food\n'
  "insecurity), by the records skill's binding rule, Tony's word of Nov\n"
  '14, 20:04 ("Yes I approve") to\n'
  'documentation/PROPOSAL_earth_system_pipeline_1_3_20261114.md, applied\n'
  "as written but one mark: the description's earth/<id>.html reads\n"
  'earth/[id].html, as skills_index.py refuses a tag there, and so would\n'
  'the reinstall. A LAYER ON THE WEB, AND ITS WALK ON ITS PAGE.\n'
  '\n'
  'WHAT PROMPTED IT. The Claude Code session of Nov 14 (Claude Opus 5.5),\n'
  "through the python_work door, built Sudan's guided walk on orrery\n"
  "594e562c and gallery 09b4b498, from Tony's prompt and\n"
  'documentation/COORD_L001_sudan_walk_brief_20261114.md, in three parts\n'
  'with a report and his reading after each; the skill was applied after\n'
  'his pushes, at orrery 5779e1f0 and gallery 8e24f9d0.\n'
  '\n'
  'WHAT CHANGED. earth-system-pipeline: two new sections. GOOGLE EARTH ON\n'
  "THE WEB: styles at the file's top, no screen overlays, one <div> per\n"
  'line in pop-ups; the phone app cannot switch folders and the web can,\n'
  "so the words promise only where the map opens; the owner's switching is\n"
  "the public view; the page links out. A LAYER'S PAGE AND ITS WALK: the\n"
  "page is the layer's one home, written by its generator; where a visitor\n"
  "needs a route the walk lives there, Google Earth its last step's\n"
  'button; pictures drawn at every build; every figure sourced and checked\n'
  "against the data; the phone-width check and Tony's reading. Under Data\n"
  "Sources, IPC's two exports, joined by name. Respectful awareness (Tony,\n"
  'Nov 14) joins the restraint section, and Source Voice Only gains: no\n'
  'meaning given to the source in words it never uses. The 3+5 card is\n'
  "folded into Architecture as Google Earth Pro's only. To stay at the cap\n"
  'of 199 lines, the 1.2 and 1.1 entries and the Shared Conventions\n'
  'section (each line held by its master) moved to\n'
  'documentation/SKILL_HISTORIES.md.\n'
  '\n'
  'THE OBLIGATION TRAVELS. This session read earth-system-pipeline 1.2\n'
  "from the repo's copy, as a Code session does, as the manifest expected.\n"
  'Tony reinstalls it (Settings > Skills) and pastes this version into the\n'
  "Project's instructions on claude.ai; the next session that loads it\n"
  'from the account confirms its copy reads 1.3 before Earth System work.\n'
  '\n'
  'The header stamp and the SHA anchor move with this entry.\n'
  '\n'
  'Version history: v3.138 moves down to\n'
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
  'resident.\n'
  '\n'
  '\n'
  'Functional for Claude, readable for human, signal preserved.\n',
  '\nFunctional for Claude, readable for human, signal preserved.\n'),
 ('documentation/PROJECT_INSTRUCTIONS_HISTORY.md',
  '(Moved down from the resident protocol on 2026-11-19, when\n'
  'v3.143 made a fourth entry.)\n'
  '\n'
  '================================================================\n'
  'PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n',
  '(Moved down from the resident protocol on 2026-11-19, when\n'
  'v3.143 made a fourth entry.)\n'
  '\n'
  'v3.141 (November 14, 2026, night): No rule changed in this document.\n'
  'ONE skill bump: earth-system-pipeline 1.2 -> 1.3 (L-001, food\n'
  "insecurity), by the records skill's binding rule, Tony's word of Nov\n"
  '14, 20:04 ("Yes I approve") to\n'
  'documentation/PROPOSAL_earth_system_pipeline_1_3_20261114.md, applied\n'
  "as written but one mark: the description's earth/<id>.html reads\n"
  'earth/[id].html, as skills_index.py refuses a tag there, and so would\n'
  'the reinstall. A LAYER ON THE WEB, AND ITS WALK ON ITS PAGE.\n'
  '\n'
  'WHAT PROMPTED IT. The Claude Code session of Nov 14 (Claude Opus 5.5),\n'
  "through the python_work door, built Sudan's guided walk on orrery\n"
  "594e562c and gallery 09b4b498, from Tony's prompt and\n"
  'documentation/COORD_L001_sudan_walk_brief_20261114.md, in three parts\n'
  'with a report and his reading after each; the skill was applied after\n'
  'his pushes, at orrery 5779e1f0 and gallery 8e24f9d0.\n'
  '\n'
  'WHAT CHANGED. earth-system-pipeline: two new sections. GOOGLE EARTH ON\n'
  "THE WEB: styles at the file's top, no screen overlays, one <div> per\n"
  'line in pop-ups; the phone app cannot switch folders and the web can,\n'
  "so the words promise only where the map opens; the owner's switching is\n"
  "the public view; the page links out. A LAYER'S PAGE AND ITS WALK: the\n"
  "page is the layer's one home, written by its generator; where a visitor\n"
  "needs a route the walk lives there, Google Earth its last step's\n"
  'button; pictures drawn at every build; every figure sourced and checked\n'
  "against the data; the phone-width check and Tony's reading. Under Data\n"
  "Sources, IPC's two exports, joined by name. Respectful awareness (Tony,\n"
  'Nov 14) joins the restraint section, and Source Voice Only gains: no\n'
  'meaning given to the source in words it never uses. The 3+5 card is\n'
  "folded into Architecture as Google Earth Pro's only. To stay at the cap\n"
  'of 199 lines, the 1.2 and 1.1 entries and the Shared Conventions\n'
  'section (each line held by its master) moved to\n'
  'documentation/SKILL_HISTORIES.md.\n'
  '\n'
  'THE OBLIGATION TRAVELS. This session read earth-system-pipeline 1.2\n'
  "from the repo's copy, as a Code session does, as the manifest expected.\n"
  'Tony reinstalls it (Settings > Skills) and pastes this version into the\n'
  "Project's instructions on claude.ai; the next session that loads it\n"
  'from the account confirms its copy reads 1.3 before Earth System work.\n'
  '\n'
  'The header stamp and the SHA anchor move with this entry.\n'
  '\n'
  'Version history: v3.138 moves down to\n'
  'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
  'resident.\n'
  '\n'
  '(Moved down from the resident protocol on 2026-11-21, when\n'
  'v3.144 made a fourth entry.)\n'
  '\n'
  '================================================================\n'
  'PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n'),
 ('LEDGER_CONSOLIDATED.md',
  "**Gap:** Tony's push; Add place... Earth on the reel in the editor, Save\n"
  "All, push; his phone look; ESCAPADE's scene remade (L-542). Skill text\n"
  'owed at the next bumps (method, not a ruling): interactive-exhibit, the\n'
  'Links fold (a link card, its place and order, LINK_MARK, the new tab,\n'
  "Find's link count); gallery-pipeline, link cards (New Link Card asking\n"
  "the row, Storage with none) and the editor's Links fold. A card that "
  'plays the reel on the\n',
  '- **Tony, 2026-11-21, 14:17,** asked by the coordinating session (Claude\n'
  '  Fable 5.2) whether a link card made with no row should stay hidden in\n'
  '  Storage until it is placed or show in the lobby, since the brief had\n'
  '  asked for "Lobby only": "In Storage for consistency." New Link\n'
  '  Card\'s "No row (saved in Storage)" stands as built.\n'
  '- **The skill text is written** (patch_L529_3_skills_and_protocol.py,\n'
  '  protocol v3.144): interactive-exhibit 1.44, A card beside a body sits\n'
  "  in a fold of its kind; gallery-pipeline 1.3, The Editor's Cards.\n"
  "**Gap:** Tony's push; Add place... Earth on the reel in the editor, Save\n"
  "All, push; his phone look; ESCAPADE's scene remade (L-542). He\n"
  'reinstalls the two skills and pastes v3.144. A card that plays the reel '
  'on the\n'),
 ('LEDGER_CONSOLIDATED.md',
  "skill text owed: the build's eleven rules above, at\n"
  "interactive-exhibit's next bump, written together with the Links\n"
  "fold's (L-540 (a reel on a Featured card)) so Tony reinstalls once.\n",
  'skill text is written: all eleven rules above are in\n'
  'interactive-exhibit 1.44 (patch_L529_3_skills_and_protocol.py,\n'
  'protocol v3.144), which Tony reinstalls. Three of them also belong\n'
  "elsewhere and wait for those skills' next versions: the plan's clock,\n"
  "horizons-orbital-mechanics, with L-541 (a plan's clock); the escape\n"
  'rule, safe-file-editing, with L-471 (a delivered patch is final); the\n'
  "package's place and the night, gallery-cache-builder.\n"),
 ('documentation/WHERE_WE_ARE.md',
  'Last updated: November 21, 2026, afternoon: the Links fold built, then '
  'the drawer walk brought up to date (Claude Code, Claude Opus 5.5, in the '
  'website).\n',
  'Last updated: November 21, 2026, afternoon: the Links fold built, the '
  'drawer walk brought up to date (Claude Code, Claude Opus 5.5), and the '
  'skills written for both builds (the coordinating session, Claude Fable '
  '5.2).\n'),
 ('documentation/WHERE_WE_ARE.md',
  '> - *(do) Renew palomasorrery.com at Porkbun by 13 Feb 2027 (L-516).*\n',
  '> - *(do) Renew palomasorrery.com at Porkbun by 13 Feb 2027 (L-516).*\n'
  '> - *(do) Reinstall two skills, interactive-exhibit and gallery-pipeline '
  '(Plugins, in the claude.ai sidebar), and paste PROJECT_INSTRUCTIONS.md, '
  "now v3.144, into the Project's instructions (L-529 (guided encounters), "
  'L-540 (a reel on a Featured card)).*\n')]


def main():
    staged = {}
    for name, old, new in EDITS:
        path = os.path.join(HERE, *name.split('/'))
        if not os.path.exists(path):
            print("ERROR: %s not found next to this script. Is it in the "
                  "orrery folder? NOTHING was written." % name)
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
                  "If this patch already ran, there is nothing to do. "
                  "Otherwise the file moved since this was built: tell "
                  "the session. NOTHING was written."
                  % (name, c, old[:70]))
            sys.exit(1)
        staged[name][0] = text.replace(o, n)
        print("ok   %s: %s" % (name, (old.strip().splitlines() or ['(end)'])[0][:56]))
    for name, (text, was_crlf) in staged.items():
        with open(os.path.join(HERE, *name.split('/')), 'wb') as f:
            f.write(text)
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % name)
    print("patch applied (%d edits, %d files)" % (len(EDITS), len(staged)))
    for tool in (["skills_index.py"], ["ledger_index.py"],
                 ["skills_index.py", "--check"], ["doc_index.py", "--caps"]):
        r = subprocess.run([sys.executable] + tool, cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print((r.stdout or '')[-1800:] + (r.stderr or '')[-800:])
            print("ERROR: %s exited %d. The edits above are written; "
                  "Discard Changes in GitHub Desktop undoes them. Tell "
                  "the session what it printed." % (' '.join(tool),
                                                    r.returncode))
            sys.exit(1)
        print("ok   %s" % ' '.join(tool))
    print("")
    print("Do next: move this file into documentation, commit and push")
    print("the orrery, reinstall interactive-exhibit and gallery-pipeline,")
    print("and paste PROJECT_INSTRUCTIONS.md into the Project.")


if __name__ == '__main__':
    main()
