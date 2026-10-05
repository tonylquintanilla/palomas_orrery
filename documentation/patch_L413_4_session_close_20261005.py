#!/usr/bin/env python3
"""
patch_L413_4_session_close_20261005.py -- ORRERY repo. Closes the session
of 2026-10-05: the ledger, Where We Are, this session's record and the
handoff for the Horizons check. It replaces patch_L413_3, which refused
and wrote nothing; delete that one.

Built on orrery d9f47a875 (Tony's push of the four build patches) at
https://github.com/tonylquintanilla/palomas_orrery, over 72e3b558
(gallery ed48d078ceb639f5f98f13f4c6abc129f722c566 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io was read,
not changed).

WHY patch_L413_3 REFUSED (L-419)
    It checked documentation/WHERE_WE_ARE.md by a fingerprint of the whole
    file, and your "-- done" marks changed the fingerprint. That broke
    your rule of 2026-10-03: a patch checks a document you annotate only
    at the lines it edits. This one does not fingerprint either of your
    documents. The ledger is matched only at the lines it edits. Where We
    Are is rewritten whole, as at every session's end, but first every
    line you changed since d9f47a87 is copied, word for word, into this
    session's handoff, and printed here. It refuses only if the file is
    not the October 4 Where We Are it replaces.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. Then follow the NEXT steps.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md   opens L-416, L-417, L-418 and L-419, and
        closes L-416 and L-417 on your runs; records your rulings on
        L-349, L-292, L-369, L-410 and L-395, and your look; closes L-389
        on your reading; L-413's progress; L-300's button; the stamp.
    documentation/WHERE_WE_ARE.md   rewritten, your notes carried first.
    documentation/HANDOFF_L413_earth_orrery_patch_20261005.md   new: this
        session's record, with your run notes answered.
    documentation/HANDOFF_L395_horizons_check_design_20261005.md   new.

SUCCESS looks like: one "ok" line per edit, a line saying how many of
your lines were carried, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import difflib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
WWA_MARKER = "Last updated: October 4, 2026, end of the day's third session."
NEXT = ["1. Move this script into documentation/, and delete patch_L413_3",
        "   from the root folder (it wrote nothing).",
        "2. Run orrery_maintenance_run.py. Every gating checker passes; its",
        "   Ledger index step moves L-389, L-416 and L-417 to the closed",
        "   section.",
        "3. Commit and push.",
        "4. When convenient: the teal-circle line, in the \"Ecliptic",
        "   Coordinates (J2000)\" box at the plot's left."]

WWA_PATH = 'documentation/WHERE_WE_ARE.md'
WWA_BASE = ('<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->\n'
      '# Where We Are\n'
      '\n'
      "Last updated: October 4, 2026, end of the day's third session. -- **Tony**: notes 10/5/26 -- \n"
      '- Written at orrery 41c1ca7a and gallery e7ef96eb.\n'
      '- This session was a ledger sweep: no code changed. A Fable session\n'
      '  ran its own sweep beside it, and both were checked against the code.\n'
      '\n'
      '> **READ THIS FIRST**\n'
      '>\n'
      '> **Changed this session:**\n'
      "> - Earth's old items are now one ordered list, in the order you\n"
      ">   confirmed. They come before the rest of the Sun's list.\n"
      '> - Seven ledger items closed because their work was already done: the\n'
      '>   licenses, the skill-header check, the galactic tide, the\n'
      ">   magnetotail's length, Earth's magnetosphere model, Earth in the\n"
      ">   website's builder, and the magnetosphere's unused tooltip copy.\n"
      '> - The four Earth numbers the scanner calls uncited are cited. The\n'
      ">   scanner looks one line short of one source, and doesn't count a\n"
      '>   written "declared" reason. That is now its own item.\n'
      '> - Your notes on this page are in the ledger, so they survive this\n'
      '>   rewrite.\n'
      '> - Patches now convert Windows line endings to the standard LF and say\n'
      '>   so, as you remembered the rule. The patch skill had said both.\n'
      '> - The 22 older files stored with Windows line endings are converted\n'
      '>   to LF, in a commit of their own. That item is off the backlog.\n'
      '>\n'
      '> **Do next:**\n'
      "> - *Your ruling on the inner belt's wording, then Earth's orrery\n"
      '>   patch.*\n'
      '>\n'
      '> **Needs you now:** -- done\n'
      '> - *Run the ledger patch, then the maintenance run, and push.*\n'
      "> - *Reinstall the patch skill and update the Project's instructions.*\n"
      '\n'
      'How to read the marks:\n'
      '- *Italic* lines are the must-reads.\n'
      '- **>> UPDATED THIS SESSION** beside a heading means that section\n'
      '  changed in the latest session.\n'
      '- "<< new this session" beside a road stage marks a change to the road.\n'
      '- Sections without a mark are as they were.\n'
      "- The marks are cleared and reset at every session's update, so they\n"
      '  always mean "new since you last read this."\n'
      '\n'
      '## The goal\n'
      '\n'
      "- Paloma's Orrery on the web.\n"
      '- The website does what the desktop orrery does, in the browser, from\n'
      '  data fetched from JPL each night, so a visitor never waits on JPL.\n'
      '- Anyone can open it, with nothing to install.\n'
      '- Built from the same code and the same checked numbers as the desktop\n'
      '  orrery.\n'
      '- The one real limit: the browser can show only the dates the saved\n'
      '  data covers.\n'
      '- Saved data covering one orbit of each body is enough, as you decided.\n'
      '- Within that range, a visitor will be able to choose a date, and\n'
      '  perhaps play time forward.\n'
      '\n'
      '## The road  **>> UPDATED THIS SESSION**\n'
      '\n'
      "  1. [done]   The Sun's room is live on the website.\n"
      "  2. [done]   Earth's room is live, with every number traced to its source.\n"
      '  3. [done]   The numbers come from one place: the orrery feeds the\n'
      '              website, and nothing is typed twice.\n'
      '  4. [done]   The Solar System room becomes a second way in: all the\n'
      '              planets, a drawer to pick them, and a way into each\n'
      "              body's own room.\n"
      "  5. [NOW]    *Earth's old items are finished, in the order you\n"
      '              confirmed.* << new this session: the first of the\n'
      "              room-by-room ledger cleanups you asked for. Each room's\n"
      '              old items are grouped by the files the work opens, and\n'
      '              only what the room shows is in scope.\n'
      "  6. [next]   The Sun's numbers get the same checking Earth's got: the\n"
      "              Sun's list, from its opening view. << moved this session:\n"
      "              after Earth's list. The distance cards are done.\n"
      "  7. [next]   The website's checks get a short list of their own, so a\n"
      "              new room or a moved front door can't break unnoticed.\n"
      '              << new this session.\n'
      '  8. [next]   A bare interactive.html link opens the Solar System room,\n'
      "              and the Explorer gets its own address. The lobby's wide\n"
      '              Solar System card, its first half, is done.\n'
      "  9. [later]  The rest of the orrery's objects come to the website --\n"
      '              dwarf planets, asteroids, moons -- through the same\n'
      "              connection that now carries the room's eleven bodies,\n"
      '              checked against JPL Horizons.\n'
      ' 10. [later]  Encounters: comets and spacecraft shown at the dates\n'
      '              that matter.\n'
      ' 11. [later]  The planets get their details -- layers, rings, magnetic\n'
      '              fields -- Jupiter and Saturn first.\n'
      ' 12. [goal]   The website does what the desktop orrery does, from data\n'
      '              fetched from JPL each night, with a date to choose and\n'
      '              time to play within the range the data covers.\n'
      '\n'
      '## Right now  **>> UPDATED THIS SESSION**\n'
      '\n'
      "- Earth's magnetosphere is drawn from published models in both the\n"
      '  orrery and the website.\n'
      '  - One question was never answered: because Earth moves along its\n'
      '    orbit, the solar wind hits it slightly from the side, so the nose\n'
      '    should turn about 4 degrees. Neither drawing does, and neither says\n'
      '    so. It now waits with live solar wind, which sets that angle.\n'
      "- The website draws Earth's geocorona, its faint hydrogen halo. The\n"
      "  orrery only mentions it in a hover; drawing it is Earth's list, item 1.\n"
      "- The website's magnetotail hover already prints the 220 Earth radii\n"
      '  the spacecraft reached.\n'
      "- The website does not draw Earth's magnetic dipole cone; the orrery\n"
      '  does. Whether the website should is now a design question.\n'
      '- On the Sun: the distance cards are built on both sites, and the\n'
      '  Roche limit is drawn at 3.45 solar radii, described as "about 3".\n'
      '- The ledger holds 241 open items after the seven closes.\n'
      '\n'
      '## The next three steps  **>> UPDATED THIS SESSION**\n'
      '\n'
      "1. *Your ruling on the inner belt's wording.*\n"
      '   - It says "where the measured particle flux peaks".\n'
      '   - Once you rule, the new wording travels in both patches below.\n'
      "2. Earth's orrery patch, then your look on the screen.\n"
      '   - The geocorona drawn as its own shell.\n'
      "   - Earth's tilt read from the stored number in five places.\n"
      '   - The atmosphere shells measured from the same radius as the crust.\n'
      "3. Earth's website patch, then your look on the phone.\n"
      "   - The inner belt's wording.\n"
      "   - The saved Earth test scene re-recorded from today's data.\n"
      '   - The collapsed-features check added to the maintenance run. It\n'
      '     passes today, so it cannot block a push.\n'
      '\n'
      '## Waiting on you  **>> UPDATED THIS SESSION**\n'
      '\n'
      'Now: -- done\n'
      '- Run the ledger patch, then orrery_maintenance_run.py, and push.\n'
      '- Reinstall safe-file-editing in Settings > Skills, and replace the\n'
      "  Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.80.\n"
      '\n'
      'At the next design talk:\n'
      '- The fuzzy outer corona, designed together with the dust cloud.\n'
      '- Moving the highlighted row to the top of the list.\n'
      "- GO's arrow, only if the text box stays in the centre, as you ruled.\n"
      "  If it can't, no arrow.\n"
      "- Earth's design talks, the belts' shape first.\n"
      '\n'
      "Decisions from the Fable sweep, one at a time when you're ready:\n"
      '- Whether items inside an ordered list need RICE scores at all.\n'
      '- A handful of scores it proposes.\n'
      '\n'
      'Not urgent, in your order:\n'
      "1. The full check of the orrery's object list against JPL Horizons.\n"
      '2. Whether the editor should also edit the words on the Solar System\n'
      "   room's rows.\n"
      '3. Choosing a date, and animation.\n'
      '4. The scattered disk, with the Kuiper belt in the Solar System room.\n'
      '   It is not the fuzzy boundary idea: the disk is a population of icy\n'
      '   bodies, the fuzzy boundary is a way of drawing an edge. When the\n'
      '   disk is designed, its edges would likely be drawn that way.\n'
      '\n'
      '## Where the details are  **>> UPDATED THIS SESSION**\n'
      '\n'
      '- Every item, done and open: `LEDGER_CONSOLIDATED.md`\n'
      "  - This session: L-413 (Earth's list), L-414 (the scanner's window),\n"
      '    L-415 (line endings), L-133 (the 22 older files, converted and closed).\n'
      '    Closed: L-409, L-407, L-350, L-406, L-305, L-234, L-383.\n'
      "  - The Sun's list: L-412.\n"
      '- The reasoning behind the order:\n'
      '  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
      '- The latest session records:\n'
      '  `documentation/HANDOFF_L413_ledger_sweep_and_earth_list_20261004.md`,\n'
      "  and Fable's sweep, `documentation/LEDGER_SWEEP_review_20261004.md`\n")

WWA_NEW = ('<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, rewritten in place; read it at the end of every session. -->\n'
      '# Where We Are\n'
      '\n'
      'Last updated: October 5, 2026, end of the session held mostly from\n'
      'your phone.\n'
      '- Written at orrery d9f47a87 and gallery ed48d078, after your runs.\n'
      '\n'
      '> **READ THIS FIRST**\n'
      '>\n'
      '> **Changed this session:**\n'
      "> - Earth's orrery patch is in: the geocorona has its own shell,\n"
      '>   Earth\'s tilt is said in words where "23.4" was typed, and the inner\n'
      '>   belt\'s words say "near the measured proton flux peak", as you ruled.\n'
      '> - The atmosphere and low Earth orbit heights stay measured from the\n'
      '>   equatorial radius, as you clarified. Notes on those rows now say why.\n'
      '> - Every step of both maintenance runs gets a dashboard button: eleven\n'
      '>   new ones.\n'
      "> - The skill check now enforces Anthropic's written limits on a\n"
      ">   skill's name and description.\n"
      '> - Six long skills now open with a list of their contents, kept true by\n'
      '>   that check, and their old history moved to its own file.\n'
      ">   provenance-discipline's rules now come before its long procedures.\n"
      '> - The check of the object list against JPL Horizons has its own\n'
      '>   handoff, for a fresh session.\n'
      '>\n'
      '> **Do next:**\n'
      '> - *The website patch for Earth, or the Horizons design round, in the\n'
      '>   order you choose.*\n'
      '>\n'
      '> **Needs you now:**\n'
      '> - *Look at the "Ecliptic Coordinates (J2000)" box at the plot\'s left:\n'
      '>   its teal-circle line. The rest of your look was correct.*\n'
      '> - *Whether to write the annotation rule into the ledger skill now.*\n'
      '\n'
      'How to read the marks:\n'
      '- *Italic* lines are the must-reads.\n'
      '- **>> UPDATED THIS SESSION** beside a heading means that section\n'
      '  changed in the latest session.\n'
      '- "<< new this session" beside a road stage marks a change to the road.\n'
      '- Sections without a mark are as they were.\n'
      "- The marks are cleared and reset at every session's update, so they\n"
      '  always mean "new since you last read this."\n'
      '\n'
      '## The goal\n'
      '\n'
      "- Paloma's Orrery on the web.\n"
      '- The website does what the desktop orrery does, in the browser, from\n'
      '  data fetched from JPL each night, so a visitor never waits on JPL.\n'
      '- Anyone can open it, with nothing to install.\n'
      '- Built from the same code and the same checked numbers as the desktop\n'
      '  orrery.\n'
      '- The one real limit: the browser can show only the dates the saved\n'
      '  data covers.\n'
      '- Saved data covering one orbit of each body is enough, as you decided.\n'
      '- Within that range, a visitor will be able to choose a date, and\n'
      '  perhaps play time forward.\n'
      '\n'
      '## The road  **>> UPDATED THIS SESSION**\n'
      '\n'
      "  1. [done]   The Sun's room is live on the website.\n"
      "  2. [done]   Earth's room is live, with every number traced to its source.\n"
      '  3. [done]   The numbers come from one place: the orrery feeds the\n'
      '              website, and nothing is typed twice.\n'
      '  4. [done]   The Solar System room becomes a second way in: all the\n'
      '              planets, a drawer to pick them, and a way into each\n'
      "              body's own room.\n"
      "  5. [NOW]    *Earth's old items are finished, in the order you\n"
      '              confirmed.* << this session: the orrery patch is built;\n'
      '              the website patch and the design talks remain.\n'
      "  6. [next]   The Sun's numbers get the same checking Earth's got: the\n"
      "              Sun's list, from its opening view.\n"
      '  7. [next]   The served objects are checked against JPL Horizons, the\n'
      '              way the numbers are checked against their sources.\n'
      '              << new this session: moved up from "not urgent", because\n'
      '              it verifies what the website already serves.\n'
      "  8. [next]   The website's checks get a short list of their own, so a\n"
      "              new room or a moved front door can't break unnoticed.\n"
      '  9. [next]   A bare interactive.html link opens the Solar System room,\n'
      "              and the Explorer gets its own address. The lobby's wide\n"
      '              Solar System card, its first half, is done.\n'
      " 10. [later]  The rest of the orrery's objects come to the website --\n"
      '              dwarf planets, asteroids, moons -- through the same\n'
      "              connection that now carries the room's eleven bodies,\n"
      '              checked against JPL Horizons.\n'
      ' 11. [later]  Encounters: comets and spacecraft shown at the dates\n'
      '              that matter.\n'
      ' 12. [later]  The planets get their details -- layers, rings, magnetic\n'
      '              fields -- Jupiter and Saturn first.\n'
      ' 13. [goal]   The website does what the desktop orrery does, from data\n'
      '              fetched from JPL each night, with a date to choose and\n'
      '              time to play within the range the data covers.\n'
      '\n'
      '## Right now  **>> UPDATED THIS SESSION**\n'
      '\n'
      "- Earth's orrery patch is in, and your look found it correct.\n"
      '  - A new checkbox, "-- Exosphere (Geocorona)", draws a faint shell at\n'
      "    100 Earth radii, in the website's colour, with the words you\n"
      '    approved.\n'
      '  - The two coordinate hovers, the Celestial Sphere tooltip and the\n'
      '    coordinate guide say "Earth\'s axial tilt" instead of typing 23.4.\n'
      "    Earth's rotation-axis hover already gives the angle for the date.\n"
      '  - The Upper Atmosphere tooltip said the layer reaches 1,000 km; it\n'
      "    now shows the hover's words, which say 600 km, the height drawn.\n"
      '- The website still says the inner belt sits "where the measured\n'
      '  particle flux peaks", and it says the same of Jupiter\'s belts, whose\n'
      '  distances have no source. The website patch fixes both.\n'
      '- The skills: each long one opens with its contents, and the check\n'
      '  fails if a list stops matching its headings. Five skills are still\n'
      "  longer than Anthropic's 500-line guideline; splitting\n"
      "  provenance-discipline's two long procedures into separate files is\n"
      '  recorded, not scheduled.\n'
      '- This chat cannot reach JPL. The Horizons check will run on your\n'
      "  machine, unless you allow JPL in this chat's network settings.\n"
      '- My closing patch refused to rewrite this page because of your\n'
      '  "-- done" marks. That broke your rule that you can annotate the\n'
      '  documents; the new closing patch keeps your notes instead.\n'
      '- The ledger holds 242 open items: L-418 and L-419 opened; L-389, L-416\n'
      '  and L-417 closed.\n'
      '\n'
      '## The next three steps  **>> UPDATED THIS SESSION**\n'
      '\n'
      "1. *Your look at the coordinate box's teal-circle line.*\n"
      "2. Earth's website patch, then your look on the phone.\n"
      '   - The inner belt\'s words, and no "measured" claim for Jupiter\'s.\n'
      '   - The geocorona note corrected.\n'
      "   - The saved Earth test scene re-recorded from today's data.\n"
      "   - The collapsed-features check added to the website's maintenance\n"
      '     run, with its own button.\n'
      '3. The Horizons check: a design round first, in a fresh session, from\n'
      '   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.\n'
      '\n'
      '## Waiting on you  **>> UPDATED THIS SESSION**\n'
      '\n'
      'Now:\n'
      "- The coordinate box's teal-circle line, in the orrery.\n"
      '- Whether the rule "a patch checks a document you annotate only at the\n'
      '  lines it edits" goes into the ledger skill now, at the cost of one\n'
      '  more reinstall, or with the next skill change.\n'
      '\n'
      'At the Horizons design round:\n'
      '- What Horizons can confirm, what counts as agreement, where the check\n'
      '  runs and how often, and what to do with pinned comet records.\n'
      '- Whether this chat should be allowed to reach JPL.\n'
      '\n'
      'At the next design talk:\n'
      '- The fuzzy outer corona, designed together with the dust cloud. The\n'
      '  exosphere is now a candidate for the same treatment.\n'
      '- Moving the highlighted row to the top of the list.\n'
      "- GO's arrow, only if the text box stays in the centre, as you ruled.\n"
      "  If it can't, no arrow.\n"
      "- Earth's design talks, the belts' shape first.\n"
      '\n'
      "Decisions from the Fable sweep, one at a time when you're ready:\n"
      '- Whether items inside an ordered list need RICE scores at all.\n'
      '- A handful of scores it proposes.\n'
      '\n'
      'Not urgent, in your order:\n'
      '1. Whether the editor should also edit the words on the Solar System\n'
      "   room's rows.\n"
      '2. Choosing a date, and animation.\n'
      '3. The scattered disk, with the Kuiper belt in the Solar System room.\n'
      '   It is not the fuzzy boundary idea: the disk is a population of icy\n'
      '   bodies, the fuzzy boundary is a way of drawing an edge. When the\n'
      '   disk is designed, its edges would likely be drawn that way.\n'
      '\n'
      '## Where the details are  **>> UPDATED THIS SESSION**\n'
      '\n'
      '- Every item, done and open: `LEDGER_CONSOLIDATED.md`\n'
      "  - This session: L-413 (Earth's list, the orrery patch), L-418 (the\n"
      "    skills' contents and histories), L-419 (your notes in documents),\n"
      '    L-395 (the Horizons check moved up). Closed: L-389, L-416 (dashboard\n'
      '    buttons), L-417 (the skill limits).\n'
      '- Your run record for this session:\n'
      '  `documentation/WHERE_WE_ARE_10-5-26_1627_run_record.md`\n'
      "  - The Sun's list: L-412.\n"
      "- The skills' old version history: `documentation/SKILL_HISTORIES.md`\n"
      '- The reasoning behind the order:\n'
      '  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
      '- The latest session records:\n'
      '  `documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`, and for\n'
      '  the next round, `documentation/HANDOFF_L395_horizons_check_design_20261005.md`\n')

HANDOFF_PATH = 'documentation/HANDOFF_L413_earth_orrery_patch_20261005.md'
HANDOFF = ("<!-- Doc-Kind: hand | Session record: Earth's orrery patch, the dashboard buttons, the skill limits and the skills' contents lists (L-413, L-416, L-417, L-418), 2026-10-05. -->\n"
      "# Handoff: Earth's orrery patch, and the skills made readable\n"
      '\n'
      'Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6 at\n'
      'https://github.com/tonylquintanilla/palomas_orrery and gallery\n'
      '624aa94557e16956b2fe022a467936ae2ccf3406 at\n'
      'https://github.com/tonylquintanilla/tonyquintanilla.github.io. Pushed\n'
      'at: orrery d9f47a875 (the four build patches) and gallery\n'
      'ed48d078ceb639f5f98f13f4c6abc129f722c566 (patch_L416_2), by Tony on\n'
      '2026-10-05; this record is carried by patch_L413_4, built on d9f47a87.\n'
      "Written October 5, 2026, with Anthropic's Claude Opus 5.5, mostly from\n"
      "Tony's phone.\n"
      '\n'
      '## What was done [verified @ orrery d9f47a87, gallery ed48d078]\n'
      '\n'
      'Orrery, to run in this order from the repo root, each moved into\n'
      'documentation/ before the maintenance run:\n'
      '1. `patch_L413_2_earth_orrery_20261005.py` -- the geocorona shell and\n'
      "   its checkbox (L-292); Earth's tilt said in words in four places and\n"
      '   the star background reading the frame angle (L-369); notes on the\n'
      "   atmosphere and LEO rows (L-389); the inner belt's words (L-349);\n"
      "   the Upper Atmosphere tooltip showing its hover's words.\n"
      '2. `patch_L416_1_dashboard_buttons_20261005.py` -- eleven buttons, so\n'
      '   every step of both maintenance runs has one.\n'
      '3. `patch_L417_1_skill_install_limits_20261005.py` -- the Skill\n'
      "   headers check enforces Anthropic's documented limits.\n"
      '4. `patch_L418_1_skill_contents_and_histories_20261005.py` -- six skills\n'
      '   open with a contents list; history moved to\n'
      '   documentation/SKILL_HISTORIES.md; protocol v3.81.\n'
      '5. `patch_L413_4_session_close_20261005.py` -- this record, the\n'
      '   Horizons handoff, the ledger, Where We Are. It replaces\n'
      '   patch_L413_3, which refused and wrote nothing (L-419).\n'
      'Gallery: `patch_L416_2_offline_check_wrapper_20261005.py` --\n'
      'documentation/run_offline_check.py.\n'
      '\n'
      'Tony ran the four build patches and the gallery patch and pushed both\n'
      'repos. His orrery maintenance run passed 20 of 20 gating checkers with\n'
      'the scanner at 296; his gallery offline run passed 23 of 23. Claude\n'
      'compared the pushed dashboard, wrapper and six skills with the tested\n'
      'copies: identical.\n'
      '\n'
      "## Tony's run record and notes, 2026-10-05\n"
      '\n'
      'Kept whole at `documentation/WHERE_WE_ARE_10-5-26_1627_run_record.md`.\n'
      'His notes in it, each answered:\n'
      '- On the Earth look: "unclear what the hover teal line refers to.\n'
      '  otherwise correct." The teal-circle line is in the "Ecliptic\n'
      '  Coordinates (J2000)" box at the plot\'s left, a box and not a hover;\n'
      '  the step named it wrongly. The rest of the look is confirmed.\n'
      '- On "then the gallery patch, which Claude builds after the push":\n'
      '  "unclear, what \'after the push\' means since i already have the\n'
      '  patch." Two gallery patches were in play: patch_L416_2, the wrapper,\n'
      "  which Tony had; and Earth's website patch, which is not built. The\n"
      '  step meant the second.\n'
      '- On the dashboard buttons: "please check. i cannot tell mode 5." The\n'
      '  pushed dashboard is byte for byte the tested one, where all 92\n'
      '  buttons found their scripts.\n'
      '- On patch_L413_3: "refused. I am not sure why ... i though\n'
      '  annotations would not be refused." It guarded Where We Are by a\n'
      "  whole-file fingerprint, against Tony's rule of 2026-10-03; his\n"
      '  "-- done" marks tripped it. L-419.\n'
      '- "Reinstall the six skills ... -- done"; pushed orrery d9f47a875,\n'
      '  gallery ed48d078.\n'
      '\n'
      "## Tony's notes found in Where We Are when patch_L413_4 ran\n"
      '\n'
      'The lines below differed from the page at d9f47a87 when the patch\n'
      'rewrote it, carried here word for word so nothing he wrote is lost:\n'
      '\n'
      '{TONY_NOTES}\n'
      '\n'
      'The page at d9f47a87 itself carried three: the header dated "-- **Tony**:\n'
      'notes 10/5/26 --", and "-- done" on Needs you now and on Waiting on\n'
      "you, both meaning the October 4 session's runs were done.\n"
      '\n'
      "## Tony's rulings and confirmations, 2026-10-05\n"
      '\n'
      '- L-349, the inner belt\'s words, "confirmed as recommended".\n'
      "- The orrery patch's words: the geocorona shell, Earth's tilt in\n"
      '  words, the Upper Atmosphere tooltip. "Approved."\n'
      '- The exosphere is a candidate for fuzzy boundaries (L-410).\n'
      '- L-389: the crust ruling of 2026-09-28 was about drawing a sphere;\n'
      '  the equatorial radius stays the standard Earth radius, so heights\n'
      '  stay measured from it. Claude had overstated the ruling; Tony\n'
      '  corrected it.\n'
      '- L-416: every maintenance-run step gets a dashboard button.\n'
      "- L-417: Sonnet's skill-limit check rebuilt to project rules, without\n"
      '  its 950-character warning.\n'
      '- L-418: contents lists, three version entries, provenance-discipline\n'
      '  in tier order, all six long skills including gallery-cache-builder.\n'
      '- L-395: the Horizons check is verification of what is served; it gets\n'
      '  a fresh session with its own handoff,\n'
      '  `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.\n'
      '\n'
      '## Discrepancies surfaced\n'
      '\n'
      '- The website\'s belt hover prints "where the measured particle flux\n'
      '  peaks" for any belt with no band, including Jupiter\'s, whose\n'
      '  distances are typed with no source. Recorded on L-349.\n'
      "- The website's geocorona note says the orrery has no shell of its own;\n"
      '  false after patch 1. For the website patch.\n'
      "- Claude's first count of missing buttons was nine; matching against\n"
      "  the runners' own lists found eleven.\n"
      '\n'
      '## The website patch, not built this session\n'
      '\n'
      'Planned, and left for a session at the machine because it needs care\n'
      'this one could not give it from the phone:\n'
      "- L-349 on the website: Tony's words for Earth's inner belt; the\n"
      '  "measured" wording printed only for a belt whose row has a source,\n'
      "  so Jupiter's belts make no claim. The approved words name protons,\n"
      '  which is true of this belt only: the next session decides how the\n'
      '  renderer knows that (a served field, or a rule on the row), and asks\n'
      '  Tony if it needs a choice.\n'
      '- The geocorona note: remove the sentence that patch 1 makes false.\n'
      '- L-379: re-record documentation/payload_earth_scene.json from the\n'
      '  current cache; the overlays retire. Read which smoke suites pin\n'
      "  hover lines (smoke_display_figures.js's acceptance table does)\n"
      '  before changing a word.\n'
      '- L-300: register sweep_collapsed_features.py in\n'
      '  gallery_maintenance_run.py, and give it a dashboard button.\n'
      "Then Tony's look on the phone.\n"
      '\n'
      '## Tony-actions, rolled up\n'
      '\n'
      '(do)\n'
      '- Delete patch_L413_3 from the orrery root; it wrote nothing.\n'
      '- Run patch_L413_4, move it into documentation/, run\n'
      '  orrery_maintenance_run.py, commit and push.\n'
      '- Look at the "Ecliptic Coordinates (J2000)" box at the plot\'s left:\n'
      '  its teal-circle line.\n'
      '\n'
      '(decide)\n'
      '- L-419: when to write the annotation rule into\n'
      '  ledger-and-session-records (one more reinstall).\n'
      '\n'
      '## Next session\n'
      '\n'
      '- Confirms its loaded copies read provenance-discipline 2.26,\n'
      '  interactive-exhibit 1.11, safe-file-editing 1.13,\n'
      '  orrery-coding-conventions 1.10, ledger-and-session-records 1.15 and\n'
      '  gallery-cache-builder 1.7, each opening with its contents list.\n'
      '- Then the website patch above, or the Horizons design round, in\n'
      "  Tony's order.\n")

NEW_FILES = {
  'documentation/HANDOFF_L395_horizons_check_design_20261005.md':
    ("<!-- Doc-Kind: hand | Handoff for a fresh session: design, then the first discovery run, of the check of the orrery's object list against JPL Horizons (L-395). -->\n"
      '# Handoff: checking the object list against JPL Horizons (L-395)\n'
      '\n'
      'Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6 at\n'
      'https://github.com/tonylquintanilla/palomas_orrery and gallery\n'
      '624aa94557e16956b2fe022a467936ae2ccf3406 at\n'
      'https://github.com/tonylquintanilla/tonyquintanilla.github.io. Pushed\n'
      "at: Tony's push of this session's closing patch, which carries this\n"
      'file. The receiving session pulls both repos at HEAD and reads L-395\n'
      'in LEDGER_CONSOLIDATED.md before anything else here.\n'
      '\n'
      'Type: DESIGN, then DISCOVERY. Audience: a session inside this Project,\n'
      'which has the protocol and the installed skills. Skills to load:\n'
      'horizons-orbital-mechanics, provenance-discipline (2.26 if reinstalled),\n'
      'ledger-and-session-records (1.15 if reinstalled). Written October 5,\n'
      "2026, with Anthropic's Claude Opus 5.5.\n"
      '\n'
      '## Why this, and why now\n'
      '\n'
      '- Tony, 2026-10-05: it matters "because like our other accuracy\n'
      '  disciplines this is about verification of information we are\n'
      '  serving."\n'
      '- The website serves eleven bodies whose identity facts are copies of\n'
      "  the orrery's object list (`OBJECT_DEFINITIONS` in\n"
      '  `celestial_objects.py`): the Sun, the eight planets, Pluto and\n'
      "  Apophis. The copy is checked against the list (L-395's first build,\n"
      '  2026-10-01). The list itself is checked against nothing.\n'
      '- So the check is in scope under The Braid: it is bounded to what the\n'
      '  website serves today, and it terminates.\n'
      '\n'
      "## What is settled (Tony's rulings, on L-395)\n"
      '\n'
      "- The orrery's object list is the one definition of each object; the\n"
      '  website keeps copies written by `tools/mirror_objects.py` from\n'
      '  `data/objects_export.json`, and a check fails on any difference.\n'
      '- Horizons is the outside authority. The list can go stale -- legacy\n'
      "  entries, the orrery's own evolution, errors -- so the check compares\n"
      '  the list with Horizons, not only the website with the list (Tony,\n'
      '  2026-09-29).\n'
      '- Simple errors a check finds are fixed and reported; anything with a\n'
      '  choice in it comes to Tony (provenance-discipline, A Simple Error a\n'
      '  Check Finds Is Fixed and Reported).\n'
      '- Discovery before remediation: the first run lists every disagreement\n'
      '  and fixes nothing except simple errors, reported.\n'
      '\n'
      '## What is open: the design round, in this order\n'
      '\n'
      '1. What Horizons can confirm for an entry: that its id resolves to\n'
      "   exactly one object; that object's name and designation; its kind.\n"
      "   And what it cannot: the project's modelling choices, such as\n"
      '   drawing Pluto about the Pluto-Charon barycentre.\n'
      '2. Which fields are compared, and what counts as agreement. Apophis is\n'
      '   the worked case: `2004 MN4` and `99942` name one Horizons record.\n'
      '3. Where the check runs, and its cadence. It needs the network, so\n'
      '   when it cannot reach Horizons it says so and never passes. It\n'
      '   records the date each object was last confirmed, the way a\n'
      '   constants row records who read its source, and re-confirms on a\n'
      '   cadence rather than querying every object on every run.\n'
      '4. Pinned records (Halley `90000030`, Encke `90000091`): flagged when\n'
      '   JPL has a newer solution, for Tony to decide. Not among the eleven,\n'
      '   so this may wait for stage 9; the design should say.\n'
      '5. What the first run prints: every disagreement by name, the object\n'
      "   and the field, with Horizons' answer beside the list's.\n"
      '\n'
      '## One practical fact, found 2026-10-05\n'
      '\n'
      "- This chat's sandbox cannot reach JPL: a Horizons API query was\n"
      '  refused with `x-deny-reason: host_not_allowed`. So either the check\n'
      "  runs on Tony's machine, like the cache builder, or Tony adds\n"
      "  `ssd.jpl.nasa.gov` to the chat's allowed domains so a session can\n"
      '  run the discovery pass itself. That is a (decide) for the design\n'
      '  round, not before it.\n'
      '\n'
      '## Not in scope\n'
      '\n'
      '- The other 171 entries of the list (road stage 9), except as the\n'
      '  design says the check will reach them later.\n'
      "- Fields the list lacks (a moon's parent, a clean kind for comets):\n"
      '  recorded on L-395, its own round.\n'
      '- The numbers inside descriptions: L-403.\n'
      '\n'
      '## Tony-actions\n'
      '\n'
      '(decide)\n'
      '- At the design round: the five questions above, one at a time.\n'
      "- Where the check runs: Tony's machine, or this chat with JPL allowed.\n"),
}

EDITS = {
  'LEDGER_CONSOLIDATED.md': [
    ('header stamp',
      "patch_L133_1), built on patch_L413_1's tree over 41c1ca7a.\n",
      ("patch_L133_1), built on patch_L413_1's tree over 41c1ca7a.\n"
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5\n"
      "(Earth's orrery patch built: L-349 ruled, L-292, L-369 and L-389\n"
      "worked, L-389 closed; L-416, L-417 and L-418 opened; L-395's Horizons\n"
      'check given its own handoff; protocol v3.81 with six skill bumps;\n'
      "L-416 and L-417 closed after Tony's runs; L-419 opened), built on\n"
      'd9f47a87.\n'),
      1),
    ('L-416, L-417, L-418 opened',
      "#### [L-413] Earth's list: the old Earth items, in the order Tony confirmed (Earth room)\n",
      ('#### [L-419] A patch checks a file Tony annotates only at the lines it edits (patches, skills)\n'
      '<!-- L:419 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n'
      "- **Tony's rule, 2026-10-03:** he writes his own notes into handoffs and\n"
      '  Where We Are (run records, pushed SHAs, comments) and will keep doing\n'
      '  so, so a patch checks those files only at the lines it edits, never by\n'
      '  a whole-file fingerprint ("wait, so i can\'t annotate the\n'
      '  documentation??").\n'
      '- **Broken 2026-10-05.** `patch_L413_3_session_close_20261005.py`\n'
      '  guarded `documentation/WHERE_WE_ARE.md` by a whole-file fingerprint\n'
      '  and refused, because Tony had marked two lines "-- done" and dated\n'
      '  the header. Tony: "i thought annotations would not be refused." The\n'
      "  rule lived only in an earlier patch's code and in Claude's memory, not\n"
      '  in a skill, so a later session did not have it.\n'
      '- **Repaired:** `patch_L413_4_session_close_20261005.py` checks only\n'
      '  that the file is the Where We Are it replaces, and carries every line\n'
      "  Tony changed into the session's handoff before rewriting the page.\n"
      '**Gap:** write the rule into ledger-and-session-records (Where We Are,\n'
      "handoffs, the ledger) -- Tony's word on when.\n"
      '**Ref:** `patch_L413_1_ledger_sweep_and_earth_list_20261004.py`\n'
      '(ANCHOR_ONLY); L-396.\n'
      '\n'
      '#### [L-418] Long skills open with their contents, and keep three version entries (skills)\n'
      '<!-- L:418 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n'
      "- **Found 2026-10-05**, reviewing a Claude Sonnet 5.5 session's check of\n"
      "  the skills against Anthropic's limits. Five skills are over\n"
      "  Anthropic's 500-line guideline. Measured: a plain read of a long file\n"
      "  shows its start and its end and leaves out the middle (this chat's\n"
      '  file viewer cuts everything past 16,000 characters from the middle),\n'
      "  and provenance-discipline's first 423 lines were version history, so\n"
      '  a plain read saw history and field notes and none of the rules.\n'
      "- **Tony's rulings, 2026-10-05.** Move the history out; a contents\n"
      '  section at the top ("Would adding a contents section help to find\n'
      '  what you need?"); arrange the sections so more are read whole; do all\n'
      '  five long skills, and gallery-cache-builder too, which is under 500\n'
      '  lines but long enough to be cut ("Do all including gallery cache\n'
      '  builder").\n'
      '- **Built:** `patch_L418_1_skill_contents_and_histories_20261005.py`.\n'
      '  Each of the six opens with a `## Contents` list of its headings;\n'
      '  history older than three entries moved word for word to\n'
      "  `documentation/SKILL_HISTORIES.md`; provenance-discipline's sections\n"
      '  ordered critical, quality, untiered, then Report to the Figures You\n'
      '  Have and the Review-Repair Protocol, then the field notes, every\n'
      "  section's text checked unchanged; `skills_index.py --check` fails a\n"
      '  skill over 500 lines with no list and any list that disagrees with\n'
      '  its headings, shown failing before it was trusted;\n'
      '  ledger-and-session-records gains "A skill keeps three version\n'
      '  entries". Versions: provenance-discipline 2.26, interactive-exhibit\n'
      '  1.11, safe-file-editing 1.13, orrery-coding-conventions 1.10,\n'
      '  ledger-and-session-records 1.15, gallery-cache-builder 1.7; protocol\n'
      '  v3.81.\n'
      '- **Still open, recorded, not scheduled:** moving\n'
      "  provenance-discipline's two long procedures (Review-Repair, 763\n"
      '  lines; Report to the Figures You Have, 631) into reference files\n'
      "  loaded only when needed, Anthropic's pattern. It needs a design talk,\n"
      '  because where a rule lives decides whether it fires.\n'
      '- **Run and pushed, 2026-10-05,** at orrery d9f47a87. Tony reinstalled\n'
      '  the six skills and replaced the Project\'s instructions ("done").\n'
      '**Gap:** the next session confirms its six loaded copies read their new\n'
      'versions and open with their contents; then the split above, when a\n'
      'design talk reaches it.\n'
      '**Ref:** `skills_index.py`; `documentation/SKILL_HISTORIES.md`;\n'
      '`documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`; L-417.\n'
      '\n'
      "#### [L-417] The Skill headers check enforces Anthropic's documented limits (skills, checks)\n"
      '<!-- L:417 status:DONE upd:2026-10-05 section:A flag: rice: -->\n'
      '- **From a Claude Sonnet 5.5 session, 2026-10-05,** which measured the\n'
      "  eleven skills against Anthropic's Skills pages and wrote a patch.\n"
      '  Claude Opus 5.5 read both pages the same day (the overview, "Skill\n'
      '  structure"; the authoring best practices, "YAML frontmatter\n'
      '  requirements" and "Token budgets"): a name of at most 64 characters,\n'
      '  lowercase letters, numbers and hyphens only, never "anthropic" or\n'
      '  "claude"; a description of at most 1024 characters; no XML tag in\n'
      '  either; a body under 500 lines as guidance. All eleven pass the rules.\n'
      '- **Rebuilt to project rules, Tony 2026-10-05 ("Confirmed as\n'
      '  recommended"):** a content fingerprint, LF line endings, the page\n'
      '  actually read as the source, the description measured as YAML reads\n'
      '  it, and no near-the-limit warning, which rested on a chosen number.\n'
      '- **Built:** `patch_L417_1_skill_install_limits_20261005.py`. Each rule\n'
      "  broken is a CONSISTENCY PROBLEM, so the maintenance run's Skill\n"
      '  headers row fails; a long body is a warning. Shown failing on a\n'
      '  made-up skill breaking all four rules.\n'
      '- **Run and pushed, 2026-10-05,** at orrery d9f47a87; Skill headers\n'
      "  passed on Tony's maintenance run.\n"
      '**Gap:** none.\n'
      '**Ref:** `skills_index.py`; L-407; L-418.\n'
      '\n'
      '#### [L-416] Every maintenance-run step has a dashboard button (dashboard, both repos)\n'
      '<!-- L:416 status:DONE upd:2026-10-05 section:A flag: rice: -->\n'
      "- **Tony's question, 2026-10-05:** was the new check added to the runner\n"
      '  and the dashboard? Skill headers (L-407) was in the runner with no\n'
      "  button. Matched against both runners' own lists: eleven steps had\n"
      '  none -- Test Skill Headers in the orrery; in the gallery Arrival,\n'
      '  Daily Run Steps, Display Figures, Earth Scene Geometry, Feature\n'
      '  Renderers, Gallery Module Atlas, Page Framing, Pole of Date, Solar\n'
      '  System Drawer and Sun Shells. (Claude first counted nine.)\n'
      '- **Built:** orrery `patch_L416_1_dashboard_buttons_20261005.py`, the\n'
      "  eleven buttons, and the offline runner's description naming the\n"
      '  Solar System drawer it had left out; gallery\n'
      '  `patch_L416_2_offline_check_wrapper_20261005.py`,\n'
      '  `documentation/run_offline_check.py`, which runs a Node check by its\n'
      "  label from the runner's own list, so the two cannot drift.\n"
      '- **Run and pushed, 2026-10-05:** orrery d9f47a87, gallery ed48d078.\n'
      '  Tony could not judge the buttons by eye ("please check. i cannot tell\n'
      '  mode 5"), so Claude compared the pushed files with the tested ones:\n'
      '  `palomas_orrery_dashboard.py` and `documentation/run_offline_check.py`\n'
      '  are byte for byte what was tested, where all 92 buttons found their\n'
      "  scripts. Tony's gallery maintenance run passed 23 of 23, Daily run\n"
      '  steps and Pole of date among them.\n'
      "**Gap:** none here. L-300's sweep gets its button with the website patch\n"
      'that registers it; that leftover is on L-300.\n'
      '**Ref:** `palomas_orrery_dashboard.py`; gallery\n'
      '`gallery_maintenance_run.py`; L-300.\n'
      '\n'
      "#### [L-413] Earth's list: the old Earth items, in the order Tony confirmed (Earth room)\n"),
      1),
    ('L-413 progress',
      ("**Gap:** Tony's ruling on L-349, then the orrery patch, the website\n"
      'patch, and the design talks in the order above.\n'),
      ('- **2026-10-05, the orrery patch built**:\n'
      "  `patch_L413_2_earth_orrery_20261005.py`, after Tony's rulings on\n"
      "  L-349 and on the patch's words, and his reading of L-389. Item 3,\n"
      '  L-389, became words only and closed. The website patch was left for\n'
      '  a session at the machine; its plan is in\n'
      '  `documentation/HANDOFF_L413_earth_orrery_patch_20261005.md`.\n'
      '- **Run and pushed at d9f47a87.** Tony\'s look: "unclear what the hover\n'
      '  teal line refers to. otherwise correct." The line is in the\n'
      '  "Ecliptic Coordinates (J2000)" box at the plot\'s left, a box and not\n'
      '  a hover; the step had named it wrongly.\n'
      "**Gap:** Tony's look at that box; then the website patch; then the\n"
      'design talks in the order above.\n'),
      1),
    ('L-349 status',
      '<!-- L:349 status:OPEN upd:2026-09-22 section:A flag: rice: -->\n',
      '<!-- L:349 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
      1),
    ('L-349 ruling',
      "**Gap:** Read the inner belt's row, then bring Tony the wording if it needs to change.\n",
      ('- **2026-10-05, the row read and the words ruled.**\n'
      '  `EARTH_VAN_ALLEN_INNER_RADII` is MEASURED, not a declared pick:\n'
      '  Baker et al. (2018) sec. 2, inner-zone PROTON fluxes peak NEAR\n'
      '  geocentric r ~ 1.5 R_E, read from the open full text on 2026-09-21.\n'
      '  So the claim stands and three words tighten. Tony, "Confirmed as\n'
      '  recommended":\n'
      '  - website hover: "Drawn at 1.5 Earth radii from Earth\'s centre, at\n'
      '    the magnetic equator: near where the measured flux of trapped\n'
      '    protons is greatest."\n'
      '  - orrery hover: "...and the brighter ring is near the measured\n'
      '    proton flux peak, 1.5 Earth radii from Earth\'s centre..."\n'
      '  - orrery tooltip: "Inner Van Allen Belt: trapped protons, drawn near\n'
      '    their measured flux peak, 1.5 Earth radii out (Baker et al. 2018)."\n'
      '- **Found:** the website\'s sentence is generic. It prints "where the\n'
      '  measured particle flux peaks" for any belt with no band, Jupiter\'s\n'
      '  included, whose distances (1.5, 3 and 6) are typed with no source\n'
      '  (L-181). The website patch prints the measured wording only for a\n'
      '  belt whose row has a source. The approved words name protons, true\n'
      "  of this belt only, so how the renderer knows that is that patch's\n"
      '  first question.\n'
      '- **Orrery side built** in `patch_L413_2_earth_orrery_20261005.py`, run\n'
      "  and pushed at d9f47a87; Tony's look: correct.\n"
      "**Gap:** the website side, in Earth's website patch (L-413).\n"),
      1),
    ('L-389 closed',
      '<!-- L:389 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n',
      '<!-- L:389 status:DONE upd:2026-10-05 section:A flag: rice: -->\n',
      1),
    ('L-389 reading',
      ("**Gap:** worked by provenance-discipline's rules when the two\n"
      'atmosphere rows are next opened.\n'),
      ("- **2026-10-05, closed by Tony's reading.** Claude proposed measuring\n"
      '  the heights from the mean radius, reading the 2026-09-28 crust ruling\n'
      '  as "depths below the drawn ground are textbook depths". Tony: "all\n'
      '  I said was to draw the crust at the mean radius because we are\n'
      '  drawing a sphere but I said that Re using the equatorial radius\n'
      '  remains the standard measure." So the atmosphere tops and the LEO\n'
      '  edges stay the equatorial radius plus their altitude; the gap above\n'
      '  the drawn crust is the cost of drawing a sphere. Notes on the four\n'
      '  rows, and the frame note corrected so it no longer reads the\n'
      '  consequence as the ruling, in `patch_L413_2_earth_orrery_20261005.py`.\n'
      '  No value moved.\n'
      "**Gap:** none. (Was: worked by provenance-discipline's rules when the\n"
      'two atmosphere rows are next opened.)\n'),
      1),
    ('L-292 status',
      '<!-- L:292 status:OPEN upd:2026-10-04 section:A flag: rice:3/3/75/2 -->\n',
      '<!-- L:292 status:OPEN upd:2026-10-05 section:A flag: rice:3/3/75/2 -->\n',
      1),
    ('L-292 built',
      ("**Gap:** the orrery's exosphere/geocorona shell in\n"
      "`SHELL_CONFIGS['Earth']` at `EARTH_GEOCORONA_RADII`; the other two\n"
      "when a build already has the file open. L-413's orrery patch.\n"),
      ('- **2026-10-05, the orrery half built** in\n'
      "  `patch_L413_2_earth_orrery_20261005.py`: `SHELL_CONFIGS['Earth']\n"
      '  [\'geocorona\']` at `EARTH_GEOCORONA_RADII`, the checkbox "-- Exosphere\n'
      '  (Geocorona)", the website\'s colour and faintness, and the words Tony\n'
      '  approved that day. Tony: the exosphere would be another good\n'
      "  candidate for a fuzzy boundary (L-410). The GPS shell and Earth's\n"
      '  Roche limit stay parked here.\n'
      "  Run and pushed at d9f47a87; Tony's look: correct.\n"
      "**Gap:** the GPS shell and Earth's Roche limit, when a build has the\n"
      "file open. (Was: the orrery's shell at `EARTH_GEOCORONA_RADII`; the\n"
      'other two when a build already has the file open.)\n'),
      1),
    ('L-369 status',
      '<!-- L:369 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n',
      '<!-- L:369 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
      1),
    ('L-369 built',
      '**Gap:** Point each at the store row; the visitor text says "about 23.4" from the row.\n',
      ('- **2026-10-05, built** in `patch_L413_2_earth_orrery_20261005.py`. The\n'
      '  plan to print "about 23.4" from the row could not stand:\n'
      "  `EARTH_OBLIQUITY_J2000_DEG` is the frame's defining angle, not\n"
      "  Earth's tilt, and provenance-discipline's Rule 7 lets no page round\n"
      '  a stored number on its own. Tony approved the words instead: the two\n'
      '  coordinate hovers, the Celestial Sphere tooltip and the coordinate\n'
      '  guide say "Earth\'s axial tilt", the hovers pointing at Earth\'s\n'
      '  rotation-axis hover for the angle of the date. `star_sphere_builder.py`\n'
      '  reads the frame angle from the store, where it typed a shorter copy.\n'
      '  Run and pushed at d9f47a87.\n'
      '**Gap:** Tony\'s look at the "Ecliptic Coordinates (J2000)" box at the\n'
      "plot's left, where the teal-circle line is. (Was: point each at the\n"
      'store row.)\n'),
      1),
    ('L-410 status',
      '<!-- L:410 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n',
      '<!-- L:410 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
      1),
    ('L-410 exosphere',
      "**Gap:** a design talk before any build. The Sun slice's ninth item\n",
      ('- **Tony, 2026-10-05:** "the exosphere would be another good candidate\n'
      '  for a fuzzy boundary" -- Earth\'s geocorona, drawn as a sharp shell at\n'
      '  its detection floor of 100 Earth radii (L-292), has no edge at all.\n'
      "**Gap:** a design talk before any build. The Sun slice's ninth item\n"),
      1),
    ('L-395 status',
      '<!-- L:395 status:OPEN upd:2026-10-01 section:A flag: rice: -->\n',
      '<!-- L:395 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
      1),
    ('L-395 moved up',
      "**Gap:** The first build is done (the room's eleven bodies). Still open:\n",
      ('- **Tony, 2026-10-05:** the Horizons check is important "because like\n'
      '  our other accuracy disciplines this is about verification of\n'
      '  information we are serving." It gets a fresh session with its own\n'
      '  handoff, `documentation/HANDOFF_L395_horizons_check_design_20261005.md`:\n'
      '  the design round first, bounded to the eleven served bodies.\n'
      "- **Found the same day:** this chat's sandbox cannot reach JPL; a\n"
      '  Horizons API query was refused, `x-deny-reason: host_not_allowed`.\n'
      "  The check runs on Tony's machine, or Tony allows `ssd.jpl.nasa.gov`\n"
      "  in the chat's network settings. A (decide) for the design round.\n"
      "**Gap:** The first build is done (the room's eleven bodies). Still open:\n"),
      1),
    ('L-300 status',
      '<!-- L:300 status:OPEN upd:2026-10-04 section:A flag: rice:3/3/90/1 -->\n',
      '<!-- L:300 status:OPEN upd:2026-10-05 section:A flag: rice:3/3/90/1 -->\n',
      1),
    ('L-300 its button',
      '**Gap:** one small patch to `gallery_maintenance_run.py` registering the\n',
      ('- **2026-10-05:** when the sweep is registered, it also gets a dashboard\n'
      '  button (L-416, closed, every step of both runs has one).\n'
      '**Gap:** one small patch to `gallery_maintenance_run.py` registering the\n'),
      1),
  ],
}


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    for path in list(NEW_FILES) + [HANDOFF_PATH]:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If this patch already "
                             "ran, it has nothing left to do. NOTHING was "
                             "written." % path)
    writes = []
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        writes.append((path, text, done, was_crlf))

    current, wwa_crlf = read_lf(WWA_PATH)
    if WWA_MARKER not in current:
        raise SystemExit("ERROR: %s is not the October 4 Where We Are this "
                         "patch replaces. NOTHING was written." % WWA_PATH)
    carried = [line[2:] for line in difflib.ndiff(WWA_BASE.split("\n"),
                                                   current.split("\n"))
               if line.startswith("+ ")]
    if carried:
        block = "\n".join("    " + line for line in carried)
    else:
        block = "    (none: the page was as pushed at d9f47a87)"
    handoff = HANDOFF.replace("{TONY_NOTES}", block)
    writes.append((WWA_PATH, WWA_NEW, ["rewritten whole"], wwa_crlf))
    writes.append((HANDOFF_PATH, handoff, ["created"], False))
    for path in sorted(NEW_FILES):
        writes.append((path, NEW_FILES[path], ["created"], False))

    for path, text, done, was_crlf in writes:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-58s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("carried %d line(s) of yours from Where We Are into the handoff"
          % len(carried))
    for line in carried:
        print("    " + line)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
