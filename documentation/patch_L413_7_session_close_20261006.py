#!/usr/bin/env python3
"""
patch_L413_7_session_close_20261006.py -- ORRERY repo. The close of the
Earth website session of 2026-10-06.

Built on orrery e7073fce5cc214836d2175d3f7643ff0855c7064 at
https://github.com/tonylquintanilla/palomas_orrery (gallery
38f1e7b058ac359d5b7806fc3d2fe7da77d48e64 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with
patch_L413_6 run and pushed there). REBUILT: the first copy of this
patch, built on 51436054, refused at the protocol's header line because
a parallel session took v3.83; delete that copy.

HOW TO RUN IT
    Save this file in the ORRERY repo's root folder (the one with
    palomas_orrery.py), open it in VS Code, click Run. It asks nothing.
    Then follow the NEXT steps it prints. It may run before or after the
    gallery patch; the two touch different repos.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md -- L-421 opened (the facts typed in the rooms'
        code); L-349, L-300, L-369, L-415 and L-419 closed; L-379, L-292,
        L-413, L-418 brought up to date; Tony's look on L-420; the stamp.
    skills/interactive-exhibit/SKILL.md -- 1.12: a fact about one feature
        is served with that feature's words, never typed in a renderer.
        Its 1.9 entry moves to documentation/SKILL_HISTORIES.md.
    PROJECT_INSTRUCTIONS.md -- v3.84; v3.81 moves to
        documentation/PROJECT_INSTRUCTIONS_HISTORY.md.
    palomas_orrery_dashboard.py -- the Collapsed Features button (L-300).
    documentation/WHERE_WE_ARE.md -- rewritten.
    documentation/HANDOFF_L413_earth_website_20261006.md -- new.
    documentation/MANIFEST_L421_typed_facts_20261006.md -- new.

YOUR NOTES ARE SAFE (L-419). The ledger, the protocol, the skill and the
other files are checked only at the lines this patch edits. Where We Are
is rewritten whole, so every line of it that differs from the page at
51436054 (unchanged at e7073fce) is first copied word for word into the new handoff, and printed.

SUCCESS looks like: one "ok" line per change, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 6, 2026 with Anthropic's Claude Opus 5.5.
"""

import difflib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
WWA_MARKER = "Last updated: October 5, 2026, end of the session held mostly from"
NEXT = ["1. Move this script into documentation/.",
        "2. Run orrery_maintenance_run.py. Its Ledger index step adds L-421",
        "   and moves the five closed items; its Skill manifest step writes",
        "   interactive-exhibit 1.12 into PROJECT_INSTRUCTIONS.md.",
        "3. Commit and push.",
        "4. Reinstall interactive-exhibit in Settings > Skills (1.12), and",
        "   replace the Project's instructions with PROJECT_INSTRUCTIONS.md,",
        "   now v3.84."]

WWA_PATH = 'documentation/WHERE_WE_ARE.md'
WWA_BASE = ('<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, '
 'rewritten in place; read it at the end of every session. -->\n'
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
 '> - Your notes in this page, the handoffs and the ledger are protected\n'
 '>   by a written rule now: a patch checks only the lines it edits.\n'
 '>\n'
 '> **Do next:**\n'
 '> - *The website patch for Earth, or the Horizons design round, in the\n'
 '>   order you choose.*\n'
 '>\n'
 '> **Needs you now:**\n'
 '> - *Look at the "Ecliptic Coordinates (J2000)" box at the plot\'s left:\n'
 '>   its teal-circle line. The rest of your look was correct.*\n'
 '> - *Run the skill patch, reinstall ledger-and-session-records, and\n'
 ">   replace the Project's instructions with v3.82.*\n"
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
 '- Run patch_L419_1, reinstall ledger-and-session-records, and replace\n'
 "  the Project's instructions with PROJECT_INSTRUCTIONS.md, now v3.82.\n"
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

WWA_NEW = ('<!-- Doc-Kind: hand | Where the project is and where it is going, in plain words. One file, '
 'rewritten in place; read it at the end of every session. -->\n'
 '# Where We Are\n'
 '\n'
 'Last updated: October 6, 2026, end of the Earth website session.\n'
 '- Written at orrery e7073fce and gallery 38f1e7b0, after your runs of\n'
 '  the website patch and of the galactic-plane and panel-colour patches.\n'
 '\n'
 '> **READ THIS FIRST**\n'
 '>\n'
 '> **Changed this session:**\n'
 "> - Earth's website patch is live, and your look on the phone found it\n"
 '>   correct. The inner belt says "trapped protons", in your words, and\n'
 ">   Jupiter's belts no longer claim a measured distance.\n"
 '> - The saved Earth scene the checks use is re-recorded from the real\n'
 '>   data, with a tool that can remake it. That showed two hovers on the\n'
 '>   live site were already too tall for the phone; with your approved\n'
 '>   changes all three tall ones fit.\n'
 '> - A search of both rooms found 17 facts typed in the code instead of\n'
 '>   served with their sources. You ruled they are fixed now, as part of\n'
 '>   finishing the Earth and Sun rooms. The plan is written down for a\n'
 '>   fresh session.\n'
 '> - A written rule now says code may type only words about our picture;\n'
 '>   facts, papers and sources are served.\n'
 '> - In the orrery, from a session of its own: the Celestial Grid draws\n'
 '>   the galactic plane, a violet circle, with its poles, and the Star\n'
 ">   Background marks Sagittarius A*, the galaxy's centre.\n"
 '> - The desktop orrery opens on Linux and macOS again: its panels use\n'
 '>   one grey, gray90, that every system knows.\n'
 '>\n'
 '> **Do next:**\n'
 '> - *The typed facts, in a fresh session, from the plan written today.*\n'
 '>\n'
 '> **Needs you now:**\n'
 '> - *Run this closing patch in the orrery repo, reinstall\n'
 ">   interactive-exhibit, and replace the Project's instructions with\n"
 '>   v3.84.*\n'
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
 '              confirmed.* << this session: the website patch is live;\n'
 '              the typed facts are the last part, with the design talks.\n'
 "  6. [next]   The facts typed in the Earth and Sun rooms' code move into\n"
 '              the served data, with their sources. << new this session\n'
 "  7. [next]   The Sun's numbers get the same checking Earth's got: the\n"
 "              Sun's list, from its opening view.\n"
 '  8. [next]   The served objects are checked against JPL Horizons, the\n'
 '              way the numbers are checked against their sources.\n'
 "  9. [next]   The website's checks get a short list of their own, so a\n"
 "              new room or a moved front door can't break unnoticed.\n"
 ' 10. [next]   A bare interactive.html link opens the Solar System room,\n'
 "              and the Explorer gets its own address. The lobby's wide\n"
 '              Solar System card, its first half, is done.\n'
 " 11. [later]  The rest of the orrery's objects come to the website --\n"
 '              dwarf planets, asteroids, moons -- through the same\n'
 "              connection that now carries the room's eleven bodies,\n"
 '              checked against JPL Horizons.\n'
 ' 12. [later]  Encounters: comets and spacecraft shown at the dates\n'
 '              that matter.\n'
 ' 13. [later]  The planets get their details -- layers, rings, magnetic\n'
 '              fields -- Jupiter and Saturn first.\n'
 ' 14. [goal]   The website does what the desktop orrery does, from data\n'
 '              fetched from JPL each night, with a date to choose and\n'
 '              time to play within the range the data covers.\n'
 '\n'
 '## Right now  **>> UPDATED THIS SESSION**\n'
 '\n'
 "- Earth's website patch is live: 24 of 24 checks after the cache build,\n"
 '  and your look on the phone found it correct.\n'
 '  - The inner belt reads in your approved words, and the word\n'
 '    "protons" comes from the served data, not the code.\n'
 "  - Jupiter's three belts say only where they are drawn.\n"
 '  - The geocorona note no longer says the orrery lacks its shell.\n'
 "  - The collapsed-features check now runs in the website's maintenance\n"
 '    run, so it counts 24, with its own dashboard button.\n'
 '- The saved Earth scene was five weeks old. A new tool remakes it the\n'
 '  way the page makes it, and the checks now see the live site as it is.\n'
 '  - Seen that way, the rotation axis hover was 21 lines and the outer\n'
 "    belt's 18, on the live site, over the phone's 17-line limit.\n"
 "  - Your approved changes bring all three tall hovers to 17: the axis's\n"
 '    layout, and one shorter sentence on both belts.\n'
 "- The 17 typed facts: 13 in Earth's room, 4 in the Sun's. Most are\n"
 '  already backed by a served source and only need moving; six need a\n'
 '  source found and read, or removal with the gap noted.\n'
 "- Jupiter's inner belt isn't in a website room yet, so its new words\n"
 "  wait for a Jupiter room; the orrery's are correct, as you saw.\n"
 '- The galactic plane in the orrery is in, and you found it good. Your\n'
 '  two requests are recorded with it: the galactic tide is very faint\n'
 "  and its X can't be made out, and the coordinate circles' descriptions\n"
 '  could move to hover markers on the circles.\n'
 "- The panels' grey: a shade darker than before, the grey of January to\n"
 '  June. A look on Windows, and a run on a Mac when convenient.\n'
 '- The skill copies this session loaded all matched the repo, and the\n'
 '  ones you reinstalled read their new versions.\n'
 '\n'
 '## The next three steps  **>> UPDATED THIS SESSION**\n'
 '\n'
 '1. *Your run of this closing patch, and the reinstall.*\n'
 '2. The typed facts move into the served data, in a fresh session, from\n'
 '   `documentation/MANIFEST_L421_typed_facts_20261006.md`.\n'
 "3. The Horizons check's design round, in its own session, from\n"
 '   `documentation/HANDOFF_L395_horizons_check_design_20261005.md`.\n'
 '\n'
 '## Waiting on you  **>> UPDATED THIS SESSION**\n'
 '\n'
 'Now:\n'
 '- Run this closing patch, run orrery_maintenance_run.py, commit and\n'
 '  push.\n'
 "- Reinstall interactive-exhibit (1.12) and replace the Project's\n"
 '  instructions with PROJECT_INSTRUCTIONS.md, now v3.84.\n'
 "- A look at the orrery's panels on Windows; a Mac run when convenient.\n"
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
 "  - This session: L-413 (Earth's list), L-349 (the belt's words),\n"
 '    L-379 (the saved scene), L-300 (the collapsed-features check), L-292\n'
 '    (the geocorona note), L-421 (the typed facts, opened). Closed: L-349\n'
 "    (the belt's words), L-300 (the collapsed-features check), L-369\n"
 "    (Earth's tilt in words), L-415 and L-419 (skill rules confirmed).\n"
 "  - L-418 stays open only for splitting provenance-discipline's two\n"
 '    long procedures into their own files.\n'
 '  - The galactic plane: L-420; the panel colour: L-027; their record:\n'
 '    `documentation/HANDOFF_L420_galactic_plane_20261006.md`.\n'
 '- The plan for the typed facts:\n'
 '  `documentation/MANIFEST_L421_typed_facts_20261006.md`\n'
 "- This session's record:\n"
 '  `documentation/HANDOFF_L413_earth_website_20261006.md`\n'
 "- The skills' old version history: `documentation/SKILL_HISTORIES.md`\n"
 '- The reasoning behind the order:\n'
 '  `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n'
 '- For the Horizons round:\n'
 '  `documentation/HANDOFF_L395_horizons_check_design_20261005.md`\n')

HANDOFF_PATH = 'documentation/HANDOFF_L413_earth_website_20261006.md'
HANDOFF = ("<!-- Doc-Kind: hand | Session record: Earth's website patch, the saved Earth scene, three hovers "
 'fitted to the phone, and the typed facts found (L-413, L-349, L-379, L-300, L-421), 2026-10-06. '
 '-->\n'
 "# Handoff: Earth's website patch, and the facts typed in the rooms' code\n"
 '\n'
 'Built on orrery 51436054330aefd6be2a7efd93ebd58f06c4a2d2 and gallery\n'
 'ed48d078ceb639f5f98f13f4c6abc129f722c566; the gallery patch pushed at\n'
 '38f1e7b058ac359d5b7806fc3d2fe7da77d48e64 at\n'
 'https://github.com/tonylquintanilla/tonyquintanilla.github.io; this\n'
 'closing patch rebuilt on orrery e7073fce5cc214836d2175d3f7643ff0855c7064\n'
 'at https://github.com/tonylquintanilla/palomas_orrery, after the first\n'
 "build refused (below). Orrery pushed at: Tony's run record carries it. This\n"
 'record is carried by `patch_L413_7_session_close_20261006.py`. Written\n'
 "October 6, 2026, with Anthropic's Claude Opus 5.5.\n"
 '\n'
 '## Opening checks [verified @ orrery 51436054, gallery ed48d078]\n'
 '\n'
 "- All eleven skills the session loaded were byte for byte the repo's\n"
 '  `skills/` copies, at the versions the last handoff named:\n'
 '  provenance-discipline 2.26, interactive-exhibit 1.11, safe-file-editing\n'
 '  1.13, orrery-coding-conventions 1.10, ledger-and-session-records 1.16,\n'
 '  gallery-cache-builder 1.7, each opening with its contents list.\n'
 "- The protocol in this session's context was already v3.83, from the\n"
 '  parallel L-027 session, while the repo still read v3.82. This session\n'
 '  did not notice the difference. It was the signal that another session\n'
 '  had changed the protocol, and missing it is why the first closing\n'
 '  patch was built on the wrong version.\n'
 "- So L-419 and L-415 close, and L-369 closes on Tony's look of\n"
 '  2026-10-05 ("beautiful"). L-418 does NOT close: its version check is\n'
 "  done, but splitting provenance-discipline's two long procedures is\n"
 '  still open on it.\n'
 '- When the first closing patch was built, orrery HEAD was still\n'
 '  51436054. A parallel session (L-420, then L-027) pushed e7073fce\n'
 '  before Tony ran it, and took protocol v3.83 for agentic-pre-test 1.3.\n'
 "  The first closing patch refused at the protocol's header line and\n"
 '  wrote nothing, as built. This one is rebuilt on e7073fce: the skill\n'
 '  change is v3.84, v3.81 moves down, and Where We Are carries that\n'
 "  session's lines from its handoff.\n"
 '\n'
 '## What was done\n'
 '\n'
 'Gallery, `patch_L413_6_earth_website_20261006.py`, tested whole on a\n'
 'copy of gallery ed48d078 with an imitation cache rebuild: 24 of 24\n'
 'gating checks passed; without the rebuild, "Cache in step" and "Display\n'
 'figures" fail, as they should.\n'
 "- L-349: Earth's inner belt reads in Tony's approved words; the word\n"
 '  "protons" comes from a new served list, `flux_peak_of`, beside the\n'
 "  belts' other words, which `store_writer.py` may edit. A belt says\n"
 '  "measured" only when its row has a source, so Jupiter\'s three belts\n'
 '  make no claim.\n'
 "- L-292: the geocorona note's sentence saying the orrery has no shell of\n"
 '  its own is gone.\n'
 '- L-379: `documentation/payload_earth_scene.json` re-recorded from the\n'
 '  cache of 2026-10-05 by the new `tools/record_earth_scene.py`, which\n'
 "  runs the Earth room's own Python out of `interactive.html`. The cache\n"
 '  pieces three checks laid over the old recording are gone.\n'
 '- Measured on the live scene, three hovers were over the 17-line limit:\n'
 '  the rotation axis at 21 and the outer belt at 18, both already live,\n'
 "  and the inner belt at 18 with the new words. With Tony's approved\n"
 "  changes all three are 17: the axis hover's layout (a doubled break\n"
 '  removed, the tilt sentence re-broken, one empty line gone, no word\n'
 '  changed), and one shorter sentence on both belts.\n'
 '- L-300: the "Collapsed features" checker in `gallery_maintenance_run.py`.\n'
 '- The hover fixture re-recorded as\n'
 '  `documentation/fixture_hovers_L349_on_ed48d078.json`.\n'
 '- Run and pushed at 38f1e7b0: 24 of 24 after the cache build, the swap\n'
 '  absorbing one refused rename. Tony\'s look on the phone: "correct";\n'
 '  "Jupiter inner belt not in the room yet. correct in the orrery." So\n'
 '  L-349 and L-300 close.\n'
 '\n'
 'Orrery, this patch: the dashboard button for the new checker; the rule\n'
 "below into interactive-exhibit 1.12; protocol v3.84; Tony's look at\n"
 'L-420, from his run record, recorded on L-420; the ledger; the\n'
 'manifest; this handoff; Where We Are.\n'
 '\n'
 "## Tony's notes found in Where We Are when this patch ran\n"
 '\n'
 'The lines below differed from the page at 51436054 when the patch\n'
 'rewrote it, carried here word for word so nothing he wrote is lost:\n'
 '\n'
 '{TONY_NOTES}\n'
 '\n'
 "## Tony's rulings, 2026-10-06\n"
 '\n'
 '- The word "protons" is served, not typed, on Claude\'s recommendation;\n'
 '  Tony then set the frame: "I thought the only source of truth is the\n'
 '  constants py and the objects list ... not from the code."\n'
 '- The skill gets the clarification, unless he said otherwise; he did\n'
 '  not.\n'
 '- L-379 done properly, by re-recording the saved scene: "Proceed as\n'
 '  recommended."\n'
 '- The belts\' tilt sentence, approved: "...which turns with Earth and in\n'
 '  2020 was tilted 9.4105 degrees from it, shrinking 0.0493 degrees a\n'
 '  year (IGRF-13 model)." The axis hover\'s layout change, approved.\n'
 '- The typed facts are handled now, not backlogged: "the work is here.\n'
 '  We should handle it now. What we are doing is working to make the\n'
 '  earth and sun slices complete, following the braid." Claude had\n'
 '  proposed a ledger row; that was the Braid read backwards, since these\n'
 '  rooms are the current slice.\n'
 "- The plan for them, including where the drawn guides' words go:\n"
 '  "Approved as recommended." The build moves to a fresh session from\n'
 '  the manifest: "Confirmed as recommended."\n'
 '\n'
 '## Discrepancies surfaced\n'
 '\n'
 '- Claude told Tony the interactive-exhibit skill already required\n'
 '  served words for "protons". It does not: it requires served NUMBERS,\n'
 '  and lets page-level text carry its source in the page. Corrected in\n'
 '  chat; the skill now draws the line (1.12).\n'
 '- Claude first offered "a rule in the page" as an option for the\n'
 "  particle word. Tony's frame ruled it out; it should not have been\n"
 '  offered.\n'
 "- The old saved scene hid two live hovers that were over the phone's\n"
 '  line limit, since the scene had no pole of date and no belt edges.\n'
 "- The discovery's first pass called the magnetopause's and bow shock's\n"
 '  formulas typed. They are served, under `_model`.\n'
 '- `tools/record_earth_scene.py` may duplicate the headless recipe the\n'
 '  skill describes in `tools/headless/`. The manifest asks the building\n'
 '  session to read that first.\n'
 '\n'
 '## Tony-actions, rolled up\n'
 '\n'
 '(do)\n'
 '- Gallery: done, pushed at 38f1e7b0.\n'
 '- Orrery: run `patch_L413_7_session_close_20261006.py`, move it into\n'
 '  `documentation/`, run `orrery_maintenance_run.py`, commit, push.\n'
 '- Reinstall interactive-exhibit (1.12) in Settings > Skills, and replace\n'
 "  the Project's instructions with `PROJECT_INSTRUCTIONS.md`, now v3.84.\n"
 '- The first closing patch, `patch_L413_7` as first delivered, refused\n'
 '  and wrote nothing; delete that copy and run this one.\n'
 '\n'
 '## Next session\n'
 '\n'
 '- Confirms its loaded interactive-exhibit reads 1.12 before any exhibit\n'
 '  work.\n'
 '- Builds the typed-facts move from\n'
 '  `documentation/MANIFEST_L421_typed_facts_20261006.md`. patch_L413_6\n'
 '  landed at gallery 38f1e7b0.\n'
 "- Works L-420's two requests from Tony's look, and closes L-027 on his\n"
 "  look at the panels (that session's handoff).\n"
 '- Where We Are: the Horizons session leaves the page alone this round\n'
 '  and puts its updates in its own handoff; the next rewrite picks them\n'
 '  up from there.\n')

NEW_FILES = {'documentation/MANIFEST_L421_typed_facts_20261006.md': '<!-- Doc-Kind: hand | Build manifest: '
                                                        'move the facts typed in the Earth and Sun '
                                                        "rooms' code into the served data, with "
                                                        'their sources (L-421), 2026-10-06. -->\n'
                                                        '# Build manifest: the facts typed in the '
                                                        "rooms' code (L-421)\n"
                                                        '\n'
                                                        'Written against orrery '
                                                        '51436054330aefd6be2a7efd93ebd58f06c4a2d2 '
                                                        'at\n'
                                                        'https://github.com/tonylquintanilla/palomas_orrery '
                                                        'and gallery\n'
                                                        'ed48d078ceb639f5f98f13f4c6abc129f722c566 '
                                                        'at\n'
                                                        'https://github.com/tonylquintanilla/tonyquintanilla.github.io, '
                                                        'with the\n'
                                                        "gallery's "
                                                        '`patch_L413_6_earth_website_20261006.py`, '
                                                        'which Tony then ran\n'
                                                        'and pushed at gallery '
                                                        '38f1e7b058ac359d5b7806fc3d2fe7da77d48e64, '
                                                        'with his\n'
                                                        'look on the phone "correct". The orrery '
                                                        'has since moved to e7073fce (the\n'
                                                        'galactic plane and the panel colour, no '
                                                        'change to these rooms). October\n'
                                                        "6, 2026, with Anthropic's Claude Opus "
                                                        '5.5.\n'
                                                        '\n'
                                                        'THE BUILDING SESSION FIRST re-reads both '
                                                        "repos' HEAD and confirms\n"
                                                        'patch_L413_6 landed: '
                                                        '`tools/record_earth_scene.py` exists, '
                                                        "Earth's belts\n"
                                                        'in `data/objects_config.json` carry '
                                                        '`flux_peak_of`, and the gallery run\n'
                                                        'counts 24 checkers. It builds on that '
                                                        "HEAD, never on this manifest's\n"
                                                        'base. If patch_L413_6 is not in, stop and '
                                                        'ask.\n'
                                                        '\n'
                                                        '## The goal\n'
                                                        '\n'
                                                        'The Earth and Sun rooms are the current '
                                                        'slice. When this is done, no\n'
                                                        "sentence in either room's hovers or info "
                                                        'panel states something about\n'
                                                        'nature, about a paper, or names a source '
                                                        'unless it is served, with its\n'
                                                        'source, beside the feature it describes. '
                                                        'Tony\'s word, 2026-10-06: "the\n'
                                                        'work is here. We should handle it now," '
                                                        'completing the Earth and Sun\n'
                                                        'slices under the Braid. He approved this '
                                                        'plan "as recommended" the same\n'
                                                        'day.\n'
                                                        '\n'
                                                        '## The rule (written into '
                                                        'interactive-exhibit 1.12 by this '
                                                        'session)\n'
                                                        '\n'
                                                        'Code may type a sentence only when it is '
                                                        'about OUR PICTURE: a drawing\n'
                                                        'choice ("drawn round", "our choice for '
                                                        'the picture"), a frame limit\n'
                                                        '("drawn to the edge of the arrival '
                                                        'frame"), or how to use the page. A\n'
                                                        'sentence about nature, about a paper, or '
                                                        'naming a source is served with\n'
                                                        "its feature's words, with its source, and "
                                                        'the renderer prints what it\n'
                                                        'is given. Where such a fact has no served '
                                                        'row, the fix is a served row.\n'
                                                        '\n'
                                                        '## How the list was found\n'
                                                        '\n'
                                                        'Both rooms were built headless twice, '
                                                        'once as served and once with\n'
                                                        'every served word replaced by a marker. '
                                                        'Any sentence still present\n'
                                                        'without the marker was typed. The first '
                                                        'run missed the `_model` key, so\n'
                                                        "it reported the magnetopause's and bow "
                                                        "shock's formulas as typed; they\n"
                                                        'are served. The survey script is not in '
                                                        'either repo; the building\n'
                                                        'session should turn it into a check (step '
                                                        '7 below).\n'
                                                        '\n'
                                                        '## The items, and the decision for each\n'
                                                        '\n'
                                                        '"Words kept" means Tony\'s existing '
                                                        'wording moves unchanged. Any change\n'
                                                        'of wording is his call before it is '
                                                        'built.\n'
                                                        '\n'
                                                        '| # | Room, feature | Typed now | '
                                                        'Decision |\n'
                                                        '|---|---|---|---|\n'
                                                        '| E1 | Earth, rotation axis (panel '
                                                        'source) | Archinal et al. (2018) citation '
                                                        'for the sense of rotation, in '
                                                        "`earth_geometry.js` | Serve it on Earth's "
                                                        '`orientation` entry, as the source of a '
                                                        'new words row for the sense of rotation. '
                                                        'The citation was read when it was '
                                                        'written; re-read it before serving. |\n'
                                                        '| E2 | Earth, rotation axis (hover) | '
                                                        '"prograde, west to east, '
                                                        'counter-clockwise seen from above the '
                                                        'north pole" | Words kept, served on the '
                                                        'same row as E1. |\n'
                                                        '| E3 | Earth, rotation axis (hover) | '
                                                        '"The axis slowly circles over thousands '
                                                        'of years and nods slightly, so the pole '
                                                        'and the tilt belong to that date." | '
                                                        'Needs a source (precession and nutation; '
                                                        'the IERS Conventions are the likely one). '
                                                        'Serve on `orientation`, or remove and '
                                                        'note the gap. |\n'
                                                        '| E4 | Earth, pole of date (panel source) '
                                                        '| The Horizons query described in '
                                                        '`earth_geometry.js` (quantity 32, target '
                                                        '399; target 3) | The served '
                                                        '`pole_of_date` already carries '
                                                        '`pole_source` and `orbit_source`. Print '
                                                        'those; delete the typed copy. Check the '
                                                        'two say the same before deleting. |\n'
                                                        '| E5 | Earth, geostationary ring (hover) '
                                                        '| "satellites here keep pace with '
                                                        "Earth's turning and hang over one "
                                                        'longitude" | Needs a source for the '
                                                        'definition. Serve as a hover word on the '
                                                        "ring's row, or remove and note. |\n"
                                                        '| E6 | Earth, magnetopause (hover) | '
                                                        '"Shue et al. (1998)"; "as far as the '
                                                        'paper plots its model"; "the model is '
                                                        'symmetric about the Sun line" | The '
                                                        'served source and `_model` already cite '
                                                        'Shue. Serve the sentence as a hover word '
                                                        'with gaps for the served cut angle and '
                                                        'conditions. Words kept. |\n'
                                                        '| E7 | Earth, bow shock (hover) | '
                                                        '"Jelinek et al. (2012)"; "how far round '
                                                        'the crossings the fit was made from '
                                                        'actually reached"; "the fit is symmetric '
                                                        'about the Sun line" | As E6, against the '
                                                        "bow shock's served source. Words kept. |\n"
                                                        '| E8 | Earth, magnetotail (hover) | '
                                                        '"which is how far the spacecraft went"; '
                                                        '"Drawn round, its average shape; at any '
                                                        'moment it is often flattened" | The '
                                                        'served source already names Slavin et al. '
                                                        '(1983) for 220 Earth radii and Sibeck and '
                                                        'Lin (2014) for the flattening. Serve the '
                                                        'sentences as hover words. "Drawn round" '
                                                        'is a drawing choice and may stay typed; '
                                                        'split the sentence there. |\n'
                                                        '| E9 | Earth, outer belt (hover) | "where '
                                                        'the belt is most intense" | The served '
                                                        'source (Li et al. 2025) says it. Serve in '
                                                        "the belts' parallel lists. Words kept. |\n"
                                                        '| E10 | Earth, both belts (hover) | '
                                                        '"2020" and "IGRF-13 model" | The served '
                                                        "tilt's source states both. Serve them as "
                                                        'fields on the `magnetic_tilt` row (an '
                                                        'epoch and a model name), from the orrery '
                                                        'store if the store can hold them. Already '
                                                        "on L-322 as a class; this closes Earth's "
                                                        'case. |\n'
                                                        '| E11 | Earth, terminator (hover) | "The '
                                                        'real terminator sweeps around Earth once '
                                                        'a day"; "the refraction and solar-disc '
                                                        'corrections that define sunrise on the '
                                                        'ground are not applied" | Needs a source '
                                                        'for the sunrise definition (a refraction '
                                                        'and solar-radius convention). The '
                                                        'once-a-day sweep follows from the served '
                                                        'rotation period; say so from the served '
                                                        'row. |\n'
                                                        '| E12 | Earth, Moon arc (hover) | "the '
                                                        "Moon's real path drifts from it as the "
                                                        "Sun and Earth's shape perturb the "
                                                        'two-body orbit" | Needs a source. Serve '
                                                        "on the Moon's own entry in "
                                                        '`data/objects_config.json`, or remove and '
                                                        'note. |\n'
                                                        '| E13 | Earth, Sun direction and '
                                                        'terminator (hover) | "the subsolar point, '
                                                        'where the Sun is overhead" | A '
                                                        'definition. Serve with a glossary source, '
                                                        'or ask Tony whether a definition counts '
                                                        "as the picture's own words. |\n"
                                                        '| S1 | Sun, inner Oort cloud (hover) | '
                                                        '"Drawn flattened toward the ecliptic, as '
                                                        'the inner cloud is thought to be" | The '
                                                        'served note already says the inner cloud '
                                                        'is flattened, with no source. Find one or '
                                                        "remove and note; then serve the hover's "
                                                        'words. "The thickness is chosen for the '
                                                        'picture" stays typed. |\n'
                                                        '| S2 | Sun, outer Oort (clumpy) (hover) | '
                                                        '"where the clumps really are is not '
                                                        'known" | The served note says it. Print '
                                                        'from the served words. |\n'
                                                        '| S3 | Sun, galactic tide (hover) | "how '
                                                        'thick it is at each latitude follows how '
                                                        'strongly the tide pulls there"; "Where '
                                                        'the comets really are is not known" | The '
                                                        'served note says both. Print from the '
                                                        'served words. |\n'
                                                        '| S4 | Sun, streamer belt (hover) | "Its '
                                                        'warp and width are drawn to show the '
                                                        'shape, not measured" | A drawing choice. '
                                                        'Stays typed. |\n'
                                                        '\n'
                                                        "## Where the drawn guides' words go "
                                                        "(Tony's approval, 2026-10-06)\n"
                                                        '\n'
                                                        'The axis, the Sun direction, the '
                                                        "day-night line and the Moon's arc are\n"
                                                        'drawn by `earth_geometry.js` from served '
                                                        'inputs and have no served entry\n'
                                                        'of their own.\n'
                                                        "- The axis: Earth's "
                                                        '`features.orientation` entry, which '
                                                        'already serves\n'
                                                        '  the pole and the rotation period.\n'
                                                        "- The Moon's arc: the Moon's own entry in "
                                                        '`data/objects_config.json`.\n'
                                                        '- The Sun direction and the day-night '
                                                        'line: a new words-only entry on\n'
                                                        '  Earth. The renderers must skip it as '
                                                        'they skip `orientation`, and the\n'
                                                        '  checks that count served groups and '
                                                        'shells must be read for what it\n'
                                                        '  does to them before it is added: '
                                                        '`sweep_collapsed_features.py` (exit 2\n'
                                                        '  on a group it cannot classify), '
                                                        '`tools/check_cache_in_step.py`, the\n'
                                                        '  geometry check\'s "every served group '
                                                        'has a renderer", and the store\n'
                                                        "  writer's allow list.\n"
                                                        '\n'
                                                        '## The mechanism, for the building '
                                                        'session to settle\n'
                                                        '\n'
                                                        '- A served hover word per feature, '
                                                        'printed where the typed sentence\n'
                                                        '  was, with gaps the renderer fills from '
                                                        'served numbers on the same row.\n'
                                                        '  The renderers already fill `{low}`, '
                                                        '`{high}`, `{drawn}` and `{pc}` in\n'
                                                        '  notes (`fillNote`); widening that to '
                                                        'name any numeric row of the same\n'
                                                        '  member is one way. The building session '
                                                        'decides and writes the choice\n'
                                                        '  into interactive-exhibit, since it is '
                                                        'method.\n'
                                                        '- The belts keep their words in parallel '
                                                        'lists, as `flux_peak_of` does.\n'
                                                        '- `tools/store_writer.py` learns every '
                                                        'new word field, and\n'
                                                        '  `tools/exhibit_store_editor.py` shows '
                                                        'them, or says why it does not.\n'
                                                        '- `tools/record_earth_scene.py` was '
                                                        'written this session to remake the\n'
                                                        '  saved Earth scene. interactive-exhibit '
                                                        'already describes a headless\n'
                                                        '  recipe in `tools/headless/`. Read that '
                                                        'first and fold the recorder\n'
                                                        '  into it if it duplicates it.\n'
                                                        '\n'
                                                        '## The steps\n'
                                                        '\n'
                                                        '1. Research: E3, E5, E11, E12, E13 and S1 '
                                                        'each get a source read in\n'
                                                        '   full, or are removed with the gap '
                                                        'noted. No source from memory.\n'
                                                        "2. Orrery store, if E10's epoch and model "
                                                        'become rows: `constants_new.py`,\n'
                                                        '   then the export.\n'
                                                        '3. Gallery config: the new word fields '
                                                        "and the guides' entries, written\n"
                                                        '   by the tools that own them '
                                                        '(`mirror_constants.py` for numbers,\n'
                                                        '   `store_writer.py` for words) or by an '
                                                        'anchored patch edit.\n'
                                                        '4. Renderers: '
                                                        '`gallery/feature_renderers.js` and\n'
                                                        '   `gallery/earth_geometry.js` print the '
                                                        'served words.\n'
                                                        '5. Checks: every check that pins a moved '
                                                        'sentence follows it --\n'
                                                        '   '
                                                        '`documentation/smoke_display_figures.js` '
                                                        '(acceptance lines),\n'
                                                        '   '
                                                        '`documentation/smoke_earth_geometry.js` '
                                                        '(the axis and belt pins),\n'
                                                        '   the hover budget (no hover over 17 '
                                                        'lines). The hover fixture and the\n'
                                                        '   saved Earth scene are re-recorded '
                                                        'after an imitation cache rebuild.\n'
                                                        "6. Tony's look on the phone: both rooms, "
                                                        'every hover that moved.\n'
                                                        '7. The survey becomes a gating check in '
                                                        'the gallery run: it fails on any\n'
                                                        '   typed sentence in either room that is '
                                                        'not on a short, named list of\n'
                                                        '   picture sentences. A check that cannot '
                                                        'fail is not passing, so it is\n'
                                                        '   shown failing first.\n'
                                                        '\n'
                                                        '## What this does not cover\n'
                                                        '\n'
                                                        "- Each room's own description in "
                                                        '`interactive.html`, which the skill\n'
                                                        '  allows as page text with its source in '
                                                        'the page. Not yet read\n'
                                                        '  sentence by sentence; the survey in '
                                                        'step 7 should read it too.\n'
                                                        "- The orrery's own hovers.\n"
                                                        '- Whether the citation in '
                                                        '`data/objects_config.json` and the one '
                                                        'in\n'
                                                        '  `constants_new.py` agree for each '
                                                        'served number. Not yet checked;\n'
                                                        '  recorded on L-421 as its own '
                                                        'question.\n'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('header stamp',
                             'over 51436054.\nReview and RICE update Tony 6-21-2026\n',
                             'over 51436054.\n'
                             "Module updated: October 6, 2026 with Anthropic's Claude Opus 5.5\n"
                             "(Earth's website patch built: L-349, L-379, L-300 and L-292 worked;\n"
                             'L-369, L-415 and L-419 closed; L-421 opened, the typed facts;\n'
                             'interactive-exhibit 1.12, protocol v3.84; L-349, L-300 closed on\n'
                             "Tony's runs; Tony's look at L-420 recorded), built on e7073fce.\n"
                             'Review and RICE update Tony 6-21-2026\n',
                             1),
                            ('L-421 opened',
                             '#### [L-420] The galactic plane',
                             "#### [L-421] Facts typed in the Earth and Sun rooms' code, not "
                             'served with their sources (gallery, words)\n'
                             '<!-- L:421 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n'
                             '- **Found 2026-10-06**, on Tony\'s question: "where are the facts '
                             'for the\n'
                             "  info panel stored, the code itself? Shouldn't the data and sources "
                             'use\n'
                             '  the store?" Both rooms were built headless twice, once as served '
                             'and\n'
                             '  once with every served word replaced by a marker; a sentence '
                             'still\n'
                             "  present was typed. 17 found: 13 in Earth's room (the rotation "
                             'axis,\n'
                             '  the pole of date, the geostationary ring, the magnetopause, the '
                             'bow\n'
                             "  shock, the magnetotail, the belts, the day-night line, the Moon's "
                             'arc,\n'
                             "  the Sun direction) and 4 in the Sun's (the inner and outer Oort "
                             'cloud,\n'
                             '  the galactic tide, the streamer belt). Listed with a decision each '
                             'in\n'
                             '  `documentation/MANIFEST_L421_typed_facts_20261006.md`.\n'
                             "- **Tony's ruling, the same day:** handled now, not backlogged -- "
                             '"the\n'
                             '  work is here. We should handle it now. What we are doing is '
                             'working\n'
                             '  to make the earth and sun slices complete, following the braid."\n'
                             '  Claude had proposed a ledger row; the rooms are the current slice, '
                             'so\n'
                             '  that was the Braid read backwards. The plan, including where the\n'
                             '  drawn guides\' words go, "Approved as recommended"; its build '
                             'moves to\n'
                             '  a fresh session, "Confirmed as recommended".\n'
                             '- **The rule** went into interactive-exhibit 1.12: code types only\n'
                             '  sentences about the picture; a fact about nature, about a paper, '
                             'or a\n'
                             "  source is served with its feature's words.\n"
                             '- **Its own question, not yet checked:** whether the citation in '
                             'the\n'
                             "  gallery's `data/objects_config.json` and the one in "
                             '`constants_new.py`\n'
                             '  agree for each served number. The checks compare the numbers.\n'
                             '**Gap:** the build, from the manifest, in a fresh session; then '
                             "Tony's\n"
                             'look on the phone; then the survey as a gating check.\n'
                             '**Ref:** L-413; L-349 (`flux_peak_of`, the first case); L-322 (the\n'
                             'IGRF epoch, a class); gallery `gallery/feature_renderers.js`,\n'
                             '`gallery/earth_geometry.js`, `data/objects_config.json`;\n'
                             'skills/interactive-exhibit/SKILL.md.\n'
                             '\n'
                             '#### [L-420] The galactic plane',
                             1),
                            ('L-419 closed',
                             '<!-- L:419 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
                             '<!-- L:419 status:DONE upd:2026-10-06 section:A flag: rice: -->\n',
                             1),
                            ('L-419 confirmed',
                             '**Gap:** Tony runs the patch, reinstalls the skill and replaces the\n'
                             "Project's instructions; the next session confirms its loaded copy\n"
                             'reads 1.16.\n',
                             "- **2026-10-06, confirmed and closed.** The session's loaded copy "
                             'read\n'
                             "  ledger-and-session-records 1.16, byte for byte the repo's copy.\n"
                             '**Gap:** none.\n',
                             1),
                            ('L-415 closed',
                             '<!-- L:415 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n',
                             '<!-- L:415 status:DONE upd:2026-10-06 section:A flag: rice: -->\n',
                             1),
                            ('L-415 confirmed',
                             '**Gap:** Tony reinstalls safe-file-editing (Settings > Skills) and\n'
                             "replaces the Project's instructions with v3.80. The next session\n"
                             'confirms its loaded copy reads 1.12 before any patch work, then '
                             'closes\n'
                             'this item.\n',
                             "- **2026-10-06, confirmed and closed.** The session's loaded copy "
                             'read\n'
                             "  safe-file-editing 1.13, which carries 1.12's rule unchanged, byte "
                             'for\n'
                             "  byte the repo's copy.\n"
                             '**Gap:** none.\n',
                             1),
                            ('L-418 versions confirmed',
                             '**Gap:** the next session confirms its six loaded copies read their '
                             'new\n'
                             'versions and open with their contents; then the split above, when a\n'
                             'design talk reaches it.\n',
                             '- **2026-10-06, versions confirmed.** The six loaded copies read\n'
                             '  their new versions, open with their contents, and match the repo\n'
                             '  byte for byte. The item stays open only for the split.\n'
                             '**Gap:** the split above, when a design talk reaches it. (Was: also\n'
                             "the next session's version check, done 2026-10-06.)\n",
                             1),
                            ('L-418 date',
                             '<!-- L:418 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
                             '<!-- L:418 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n',
                             1),
                            ('L-369 closed',
                             '<!-- L:369 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
                             '<!-- L:369 status:DONE upd:2026-10-06 section:A flag: rice: -->\n',
                             1),
                            ("L-369 Tony's look",
                             '**Gap:** Tony\'s look at the "Ecliptic Coordinates (J2000)" box at '
                             'the\n'
                             "plot's left, where the teal-circle line is. (Was: point each at the\n"
                             'store row.)\n',
                             '- **Tony\'s look, 2026-10-05:** the "Ecliptic Coordinates (J2000)"\n'
                             '  box showed the new teal-circle line; Tony: "beautiful". Closed\n'
                             '  2026-10-06.\n'
                             "**Gap:** none. (Was: Tony's look at that box.)\n",
                             1),
                            ("L-420 Tony's look",
                             '**Gap:** Tony runs patch_L420_2, patch_L420_3 and the maintenance '
                             'run,\n'
                             'pushes, and looks (Mode 5): the violet colour, the marker sizes, '
                             'where\n'
                             'the labels sit. Then close.\n',
                             "- **Run and pushed at e7073fce, 2026-10-06.** Tony's look, from his "
                             'run\n'
                             '  record: "looks great. some issues: a) galactic tide is very faint\n'
                             '  and the X is not discernible b) can we move the coordinate circle\n'
                             '  descriptions to hovertext markers on the circles"; and on the\n'
                             '  colour, sizes and labels, "looks good". Recorded by the website\n'
                             "  session's closing patch; the two requests are this item's to "
                             'work.\n'
                             "**Gap:** Tony's two requests above, then close. (Was: Tony's runs "
                             'and\n'
                             'look.)\n',
                             1),
                            ('L-349 website built',
                             "**Gap:** the website side, in Earth's website patch (L-413).\n",
                             '- **2026-10-06, the website side built** in gallery\n'
                             '  `patch_L413_6_earth_website_20261006.py`. The renderer prints\n'
                             '  "measured" only for a belt whose row has a source, and names the\n'
                             '  particles from a new served parallel list, `flux_peak_of`\n'
                             '  ("trapped protons" for the inner belt), on Claude\'s '
                             'recommendation\n'
                             "  and Tony's frame: the facts and sources come from the store, "
                             '"not\n'
                             '  from the code". Jupiter\'s three belts make no claim. Tested '
                             'whole:\n'
                             '  24 of 24.\n'
                             '- **Run and pushed at gallery 38f1e7b0, 2026-10-06:** 24 of 24 '
                             'after\n'
                             '  the cache build. Tony\'s look on the phone: "correct". Jupiter\'s\n'
                             '  inner belt is in no website room yet ("Jupiter inner belt not in\n'
                             '  the room yet. correct in the orrery."); its website words are '
                             'held\n'
                             '  by the hover fixture until a Jupiter room draws them. Closed.\n'
                             '**Gap:** none. (Was: the website side.)\n',
                             1),
                            ('L-349 date',
                             '<!-- L:349 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n',
                             '<!-- L:349 status:DONE upd:2026-10-06 section:A flag: rice: -->\n',
                             1),
                            ('L-379 built',
                             '**Gap:** Recapture the payload from the current cache; the overlays '
                             'then retire.\n',
                             '- **2026-10-06, built** in gallery\n'
                             '  `patch_L413_6_earth_website_20261006.py`. The new\n'
                             "  `tools/record_earth_scene.py` runs the Earth room's own Python, "
                             'read\n'
                             '  out of `interactive.html`, against the served cache, and refuses '
                             'to\n'
                             "  write a recording missing the Sun direction, the Moon's arc or "
                             'the\n'
                             '  pole of date. Re-recorded from the cache of 2026-10-05; the '
                             'overlays\n'
                             '  in the geometry check and the hover budget are gone.\n'
                             '- **What it uncovered:** measured on the live scene, the rotation '
                             'axis\n'
                             "  hover was 21 lines and the outer belt's 18, over the 17-line "
                             'limit,\n'
                             "  both already live. With Tony's approved changes of 2026-10-06 "
                             '(the\n'
                             "  axis's layout, no word changed; one shorter sentence on both "
                             'belts)\n'
                             '  all three tall hovers are 17.\n'
                             '- **Not covered:** `documentation/payload_earth.json`, the older\n'
                             '  fixture of the features alone, still ages; and the recorder may\n'
                             "  duplicate `tools/headless/` (L-421's manifest asks).\n"
                             "- **Run and pushed at gallery 38f1e7b0, 2026-10-06;** Tony's look:\n"
                             '  "correct".\n'
                             '**Gap:** `documentation/payload_earth.json`, the features-only '
                             'fixture,\n'
                             'when a build next opens it. (Was: recapture the payload; the\n'
                             'overlays retire.)\n',
                             1),
                            ('L-379 date',
                             '<!-- L:379 status:OPEN upd:2026-09-28 section:A flag: rice: -->\n',
                             '<!-- L:379 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n',
                             1),
                            ('L-300 built',
                             '**Gap:** one small patch to `gallery_maintenance_run.py` registering '
                             'the\n'
                             'checker; then a run to confirm it appears in the CHECKERS list with '
                             'its\n'
                             "verdict line. Rides L-413's website patch.\n",
                             '- **2026-10-06, built:** the "Collapsed features" checker, in '
                             'gallery\n'
                             '  `patch_L413_6_earth_website_20261006.py`, gating, its verdict the\n'
                             '  count line ("33 stored as themselves, 16 collapsed, 0\n'
                             '  unclassified."); the run counts 24. Its dashboard button,\n'
                             '  "Collapsed Features", in orrery\n'
                             '  `patch_L413_7_session_close_20261006.py`.\n'
                             '- **Run and pushed at gallery 38f1e7b0:** "PASS Collapsed features\n'
                             '  ... 33 stored as themselves, 16 collapsed, 0 unclassified", 24 of\n'
                             "  24. Closed with the button's patch.\n"
                             '**Gap:** none. (Was: register the checker.)\n',
                             1),
                            ('L-300 date',
                             '<!-- L:300 status:OPEN upd:2026-10-05 section:A flag: rice:3/3/90/1 '
                             '-->\n',
                             '<!-- L:300 status:DONE upd:2026-10-06 section:A flag: rice:3/3/90/1 '
                             '-->\n',
                             1),
                            ("L-292 the website's note",
                             "  Run and pushed at d9f47a87; Tony's look: correct.\n"
                             "**Gap:** the GPS shell and Earth's Roche limit, when a build has "
                             'the\n',
                             "  Run and pushed at d9f47a87; Tony's look: correct.\n"
                             "- **2026-10-06:** the website's geocorona note no longer says the\n"
                             '  orrery has no shell of its own (gallery\n'
                             '  `patch_L413_6_earth_website_20261006.py`).\n'
                             "**Gap:** the GPS shell and Earth's Roche limit, when a build has "
                             'the\n',
                             1),
                            ('L-413 progress',
                             "**Gap:** Tony's look at that box; then the website patch; then the\n"
                             'design talks in the order above.\n',
                             '- **Tony\'s look at that box, 2026-10-05:** "beautiful" (L-369 '
                             'closed).\n'
                             '- **2026-10-06, the website patch built:**\n'
                             '  `patch_L413_6_earth_website_20261006.py` (gallery) -- L-349, '
                             'L-379\n'
                             '  and L-300 as planned, the geocorona note (L-292), and three '
                             'hovers\n'
                             "  fitted to the phone's 17-line limit in Tony's approved changes.\n"
                             '  Record: `documentation/HANDOFF_L413_earth_website_20261006.md`.\n'
                             "  Run and pushed at gallery 38f1e7b0; Tony's look on the phone:\n"
                             '  "correct".\n'
                             '- **Added to the list, 2026-10-06:** L-421, the facts typed in the\n'
                             "  rooms' code, on Tony's ruling that it is part of finishing the "
                             'Earth\n'
                             '  and Sun slices.\n'
                             '**Gap:** L-421 from its manifest; then the design talks in the '
                             'order\n'
                             'above.\n',
                             1),
                            ('L-413 date',
                             '<!-- L:413 status:OPEN upd:2026-10-04 section:A flag: rice: -->\n',
                             '<!-- L:413 status:OPEN upd:2026-10-06 section:A flag: rice: -->\n',
                             1)],
 'PROJECT_INSTRUCTIONS.md': [('header stamp',
                              'Tony Quintanilla, PE | Claude | v3.83 | October 6, 2026\n',
                              'Tony Quintanilla, PE | Claude | v3.84 | October 6, 2026\n',
                              1),
                             ('anchor',
                              'Cut from 51436054 at '
                              'https://github.com/tonylquintanilla/palomas_orrery\n',
                              'Cut from e7073fce at '
                              'https://github.com/tonylquintanilla/palomas_orrery\n',
                              1),
                             ('v3.84, and v3.81 moved down',
                              'v3.83 (October 6, 2026): No rule changed in this document. ONE\n',
                              'v3.84 (October 6, 2026): No rule changed in this document. ONE\n'
                              'skill bump, one version (L-421): interactive-exhibit 1.11 -> 1.12. '
                              'A\n'
                              'FACT ABOUT A FEATURE IS SERVED, NOT TYPED.\n'
                              '\n'
                              "WHAT PROMPTED IT. Building Earth's website patch, Claude told Tony "
                              'the\n'
                              'skill already required the inner belt\'s word "protons" to be '
                              'served.\n'
                              'It did not: it required served numbers, and let page text carry '
                              'its\n'
                              'source in the page. Tony: "I thought the only source of truth is '
                              'the\n'
                              'constants py and the objects list ... not from the code." Asked '
                              'then\n'
                              "where the info panel's facts are stored, a search of both rooms "
                              'found\n'
                              '17 facts typed in code. Tony ruled them part of finishing the Earth '
                              'and\n'
                              'Sun slices, "the work is here", not backlog.\n'
                              '\n'
                              'WHAT CHANGED. interactive-exhibit, under Provenance is part of the\n'
                              'build: code may type only sentences about the picture; a fact '
                              'about\n'
                              "nature, about a paper, or a source is served on its feature's row "
                              'and\n'
                              'printed as given. Its v1.9 entry moved to\n'
                              'documentation/SKILL_HISTORIES.md, by the three-entry rule. The 17 '
                              'are\n'
                              'listed in documentation/MANIFEST_L421_typed_facts_20261006.md, for '
                              'a\n'
                              'fresh session to build.\n'
                              '\n'
                              'THE OBLIGATION TRAVELS. A reinstall during a session is not visible '
                              'to\n'
                              'that session. The next session confirms its loaded copy reads\n'
                              'interactive-exhibit 1.12 before any exhibit work.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with this entry.\n'
                              '\n'
                              'Version history: v3.81 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'v3.83 (October 6, 2026): No rule changed in this document. ONE\n',
                              1),
                             ('v3.81 leaves',
                              'v3.81 (October 5, 2026): No rule changed in this document. SIX\n'
                              'skill bumps, one version each (L-418): provenance-discipline 2.25 '
                              '->\n'
                              '2.26, interactive-exhibit 1.10 -> 1.11, safe-file-editing 1.12 ->\n'
                              '1.13, orrery-coding-conventions 1.9 -> 1.10,\n'
                              'ledger-and-session-records 1.14 -> 1.15 and gallery-cache-builder '
                              '1.6\n'
                              '-> 1.7. A LONG SKILL OPENS WITH ITS CONTENTS.\n'
                              '\n'
                              'WHAT PROMPTED IT. A Claude Sonnet 5.5 session checked the skills\n'
                              "against Anthropic's documented limits. All eleven pass the hard "
                              'rules,\n'
                              'which skills_index.py --check now enforces (L-417). Five are over\n'
                              "Anthropic's 500-line guideline, provenance-discipline almost six "
                              'times.\n'
                              'Measured here: a plain read of a file that long shows its start and '
                              'its\n'
                              "end and leaves out the middle, and provenance-discipline's first "
                              '423\n'
                              'lines were version history, so a plain read showed the history and '
                              'the\n'
                              'field notes and none of the rules. Tony asked whether a contents\n'
                              'section would help, and that the sections be arranged so more of '
                              'them\n'
                              'are read whole; then that all five be done, and '
                              'gallery-cache-builder\n'
                              'with them, which is under 500 lines but long enough to be cut the '
                              'same\n'
                              'way.\n'
                              '\n'
                              'WHAT CHANGED. Each of the six opens with a contents list of its\n'
                              'headings, and skills_index.py --check fails a skill over 500 lines '
                              'that\n'
                              'has none, and any skill whose list and headings disagree. Version\n'
                              'history older than three entries moved, word for word, to\n'
                              "documentation/SKILL_HISTORIES.md. provenance-discipline's sections "
                              'are\n'
                              'ordered critical, then quality, then untiered, then its two long\n'
                              "procedures, then the field notes; every section's text was checked\n"
                              'unchanged. One rule is new, in ledger-and-session-records: a skill\n'
                              'keeps three version entries, and a long skill keeps its contents '
                              'list\n'
                              "true. No other skill's rules changed.\n"
                              '\n'
                              "THE OBLIGATION TRAVELS. This session's loaded copies were the "
                              'versions\n'
                              'before these. The next session confirms its loaded copies read\n'
                              'provenance-discipline 2.26, interactive-exhibit 1.11, '
                              'safe-file-editing\n'
                              '1.13, orrery-coding-conventions 1.10, ledger-and-session-records '
                              '1.15\n'
                              'and gallery-cache-builder 1.7, and that each opens with its '
                              'contents.\n'
                              '\n'
                              "STILL OPEN. Moving provenance-discipline's two long procedures "
                              'into\n'
                              'reference files loaded only when needed is recorded on L-418, not\n'
                              'scheduled.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with this entry.\n'
                              '\n'
                              'Version history: v3.78 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'Functional for Claude, readable for human, signal preserved.',
                              'Functional for Claude, readable for human, signal preserved.',
                              1)],
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [('v3.81 arrives',
                                                    '(Moved down from the resident protocol on '
                                                    '2026-10-06 when\n'
                                                    'v3.83 made a fourth entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS REMOVED',
                                                    '(Moved down from the resident protocol on '
                                                    '2026-10-06 when\n'
                                                    'v3.83 made a fourth entry.)\n'
                                                    '\n'
                                                    'v3.81 (October 5, 2026): No rule changed in '
                                                    'this document. SIX\n'
                                                    'skill bumps, one version each (L-418): '
                                                    'provenance-discipline 2.25 ->\n'
                                                    '2.26, interactive-exhibit 1.10 -> 1.11, '
                                                    'safe-file-editing 1.12 ->\n'
                                                    '1.13, orrery-coding-conventions 1.9 -> 1.10,\n'
                                                    'ledger-and-session-records 1.14 -> 1.15 and '
                                                    'gallery-cache-builder 1.6\n'
                                                    '-> 1.7. A LONG SKILL OPENS WITH ITS '
                                                    'CONTENTS.\n'
                                                    '\n'
                                                    'WHAT PROMPTED IT. A Claude Sonnet 5.5 session '
                                                    'checked the skills\n'
                                                    "against Anthropic's documented limits. All "
                                                    'eleven pass the hard rules,\n'
                                                    'which skills_index.py --check now enforces '
                                                    '(L-417). Five are over\n'
                                                    "Anthropic's 500-line guideline, "
                                                    'provenance-discipline almost six times.\n'
                                                    'Measured here: a plain read of a file that '
                                                    'long shows its start and its\n'
                                                    'end and leaves out the middle, and '
                                                    "provenance-discipline's first 423\n"
                                                    'lines were version history, so a plain read '
                                                    'showed the history and the\n'
                                                    'field notes and none of the rules. Tony asked '
                                                    'whether a contents\n'
                                                    'section would help, and that the sections be '
                                                    'arranged so more of them\n'
                                                    'are read whole; then that all five be done, '
                                                    'and gallery-cache-builder\n'
                                                    'with them, which is under 500 lines but long '
                                                    'enough to be cut the same\n'
                                                    'way.\n'
                                                    '\n'
                                                    'WHAT CHANGED. Each of the six opens with a '
                                                    'contents list of its\n'
                                                    'headings, and skills_index.py --check fails a '
                                                    'skill over 500 lines that\n'
                                                    'has none, and any skill whose list and '
                                                    'headings disagree. Version\n'
                                                    'history older than three entries moved, word '
                                                    'for word, to\n'
                                                    'documentation/SKILL_HISTORIES.md. '
                                                    "provenance-discipline's sections are\n"
                                                    'ordered critical, then quality, then '
                                                    'untiered, then its two long\n'
                                                    'procedures, then the field notes; every '
                                                    "section's text was checked\n"
                                                    'unchanged. One rule is new, in '
                                                    'ledger-and-session-records: a skill\n'
                                                    'keeps three version entries, and a long skill '
                                                    'keeps its contents list\n'
                                                    "true. No other skill's rules changed.\n"
                                                    '\n'
                                                    "THE OBLIGATION TRAVELS. This session's loaded "
                                                    'copies were the versions\n'
                                                    'before these. The next session confirms its '
                                                    'loaded copies read\n'
                                                    'provenance-discipline 2.26, '
                                                    'interactive-exhibit 1.11, safe-file-editing\n'
                                                    '1.13, orrery-coding-conventions 1.10, '
                                                    'ledger-and-session-records 1.15\n'
                                                    'and gallery-cache-builder 1.7, and that each '
                                                    'opens with its contents.\n'
                                                    '\n'
                                                    "STILL OPEN. Moving provenance-discipline's "
                                                    'two long procedures into\n'
                                                    'reference files loaded only when needed is '
                                                    'recorded on L-418, not\n'
                                                    'scheduled.\n'
                                                    '\n'
                                                    'The header stamp and the SHA anchor move with '
                                                    'this entry.\n'
                                                    '\n'
                                                    'Version history: v3.78 moves down to\n'
                                                    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                                                    'PART 1 to keep three\n'
                                                    'resident.\n'
                                                    '\n'
                                                    '(Moved down from the resident protocol on '
                                                    '2026-10-06 when\n'
                                                    'v3.84 made a fourth entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS REMOVED',
                                                    1)],
 'documentation/SKILL_HISTORIES.md': [('interactive-exhibit 1.9 moved here',
                                       'the pinned SHAs, not recalled.\n\n## safe-file-editing\n',
                                       'the pinned SHAs, not recalled.\n'
                                       "Earlier: 1.9 | 2026-10-02, with Anthropic's Claude Opus "
                                       '5.5, from\n'
                                       'orrery @ b3cfc780 and gallery @ cfc53490, with gallery '
                                       'patches\n'
                                       'patch_L404_1_rooms_in_store_editor_20261001.py and\n'
                                       'patch_L363_9_room_step3b_drawer_20261002.py. v1.9 (L-405) '
                                       'writes down\n'
                                       "what two builds of one session taught, sorted on Tony's "
                                       'review of\n'
                                       '2026-10-02 into method rather than judgement. The sentence '
                                       'saying every\n'
                                       'reader of data/objects_config.json ignores "rooms" was '
                                       'wrong and is\n'
                                       'corrected. The store writer may change a rooms-section '
                                       "room's `drawn`\n"
                                       'and `highlight`, and the editor lists rooms from both '
                                       'places a room can\n'
                                       "live (L-404). The Solar System room's drawer is recorded "
                                       'as shared\n'
                                       "chrome with four additions, with Tony's framing ruling -- "
                                       'where a body\n'
                                       'is now, plus 20% (L-363 step 3b). And step 4 gains the '
                                       'headless recipe:\n'
                                       "a room's real driver in CPython, the real page in jsdom "
                                       'with a stand-in\n'
                                       'Plotly, and the other rooms compared before and after '
                                       '(tools/headless/).\n'
                                       '\n'
                                       '## safe-file-editing\n',
                                       1)],
 'palomas_orrery_dashboard.py': [('change log',
                                  'description names the Solar System drawer, which it had left '
                                  'out.\n'
                                  '"""\n',
                                  'description names the Solar System drawer, which it had left '
                                  'out.\n'
                                  "October 6, 2026 with Anthropic's Claude Opus 5.5 (L-300): "
                                  'added\n'
                                  'Collapsed Features under the gallery checks, in alphabetical '
                                  'place,\n'
                                  'for the checker the gallery runner gained that day; the '
                                  'offline\n'
                                  "runner's description names it.\n"
                                  '"""\n',
                                  1),
                                 ('offline runner names the sweep',
                                  '        "the config mirror check, the pointer join, cache in '
                                  'step, the "\n',
                                  '        "the config mirror check, the pointer join, cache in '
                                  'step, the "\n'
                                  '        "collapsed-features sweep, the "\n',
                                  1),
                                 ('Collapsed Features button',
                                  '        "it, not by its name.",\n'
                                  '        GALLERY_REPO_DIR,\n'
                                  '        True,\n'
                                  '        None,\n'
                                  '        True),\n'
                                  '        ("Config Mirror -- report only",\n',
                                  '        "it, not by its name.",\n'
                                  '        GALLERY_REPO_DIR,\n'
                                  '        True,\n'
                                  '        None,\n'
                                  '        True),\n'
                                  '        ("Collapsed Features",\n'
                                  '        "sweep_collapsed_features.py",\n'
                                  '        "Sorts every served feature group: a shell stored as '
                                  'itself, or a "\n'
                                  '        "known group collapsed into parallel lists (belts, '
                                  'rings), each "\n'
                                  '        "named. It exits 2 only on a group it cannot classify, '
                                  'which is "\n'
                                  '        "the case that should stop a push. GATES the gallery '
                                  'runner "\n'
                                  '        "(L-300). Runs from the gallery repo ROOT and changes '
                                  'nothing.",\n'
                                  '        GALLERY_REPO_DIR,\n'
                                  '        True,\n'
                                  '        None,\n'
                                  '        True),\n'
                                  '        ("Config Mirror -- report only",\n',
                                  1)],
 'skills/interactive-exhibit/SKILL.md': [('version 1.12, and 1.9 moved down',
                                          "Skill version: 1.11 | 2026-10-05, with Anthropic's "
                                          'Claude Opus 5.5, at\n'
                                          'palomas_orrery @ 72e3b558. v1.11 (L-418) changes no '
                                          'rule. A contents\n'
                                          'list now opens the skill, generated from its headings, '
                                          'and\n'
                                          'skills_index.py --check fails if the two disagree. '
                                          'Version history\n'
                                          'older than the two entries below moved to\n'
                                          'documentation/SKILL_HISTORIES.md. Both because a plain '
                                          'read of a\n'
                                          'long file shows its start and end and leaves out its '
                                          'middle, where\n'
                                          'the rules are (Tony, 2026-10-05).\n'
                                          "Earlier: 1.10 | 2026-10-02, with Anthropic's Claude "
                                          'Opus 5.5, from\n'
                                          'orrery @ 5e42b00b and gallery @ 0ffa4518. v1.10 (L-406) '
                                          'writes down\n'
                                          "Tony's rule for a feature's info link, which lived only "
                                          'on L-265: a\n'
                                          'NASA page where one is specific to the feature, '
                                          'otherwise English\n'
                                          'Wikipedia, with the corona the one named exception. '
                                          'Asked on\n'
                                          '2026-10-02, while the galactic tide was being redrawn, '
                                          'whether the\n'
                                          "skills covered how a feature's hover, info panel and "
                                          'drawing are\n'
                                          'written; the hover and the drawing were covered and the '
                                          'link was not.\n'
                                          'The same day Settings refused the first copy '
                                          '("malformed YAML\n'
                                          'frontmatter"): the new fires_when words sat on a line '
                                          'of their own.\n'
                                          'They are back on the one line, and the version stays '
                                          '1.10, which never\n'
                                          'loaded anywhere (L-406, L-407).\n'
                                          "Earlier: 1.9 | 2026-10-02, with Anthropic's Claude Opus "
                                          '5.5, from\n'
                                          'orrery @ b3cfc780 and gallery @ cfc53490, with gallery '
                                          'patches\n'
                                          'patch_L404_1_rooms_in_store_editor_20261001.py and\n'
                                          'patch_L363_9_room_step3b_drawer_20261002.py. v1.9 '
                                          '(L-405) writes down\n'
                                          "what two builds of one session taught, sorted on Tony's "
                                          'review of\n'
                                          '2026-10-02 into method rather than judgement. The '
                                          'sentence saying every\n'
                                          'reader of data/objects_config.json ignores "rooms" was '
                                          'wrong and is\n'
                                          'corrected. The store writer may change a rooms-section '
                                          "room's `drawn`\n"
                                          'and `highlight`, and the editor lists rooms from both '
                                          'places a room can\n'
                                          "live (L-404). The Solar System room's drawer is "
                                          'recorded as shared\n'
                                          "chrome with four additions, with Tony's framing ruling "
                                          '-- where a body\n'
                                          'is now, plus 20% (L-363 step 3b). And step 4 gains the '
                                          'headless recipe:\n'
                                          "a room's real driver in CPython, the real page in jsdom "
                                          'with a stand-in\n'
                                          'Plotly, and the other rooms compared before and after '
                                          '(tools/headless/).\n',
                                          "Skill version: 1.12 | 2026-10-06, with Anthropic's "
                                          'Claude Opus 5.5, at\n'
                                          'palomas_orrery @ 51436054 and gallery @ ed48d078. v1.12 '
                                          '(L-421, L-349)\n'
                                          'draws the line the provenance rule left open: a fact '
                                          'about one feature\n'
                                          "is served with that feature's words, never typed in a "
                                          'renderer, and\n'
                                          'code may type only sentences about the picture. Found '
                                          'when Claude told\n'
                                          "Tony this skill already required the inner belt's "
                                          '"protons" to be\n'
                                          'served; it required served NUMBERS, and let page text '
                                          'carry its source\n'
                                          'in the page, which Claude read as allowing a typed '
                                          'fact. Tony: "I\n'
                                          'thought the only source of truth is the constants py '
                                          'and the objects\n'
                                          'list ... not from the code." A search the same day '
                                          'found 17 such facts\n'
                                          'in the two rooms '
                                          '(documentation/MANIFEST_L421_typed_facts_20261006.md).\n'
                                          "Earlier: 1.11 | 2026-10-05, with Anthropic's Claude "
                                          'Opus 5.5, at\n'
                                          'palomas_orrery @ 72e3b558. v1.11 (L-418) changes no '
                                          'rule. A contents\n'
                                          'list now opens the skill, generated from its headings, '
                                          'and\n'
                                          'skills_index.py --check fails if the two disagree. '
                                          'Version history\n'
                                          'older than the two entries below moved to\n'
                                          'documentation/SKILL_HISTORIES.md. Both because a plain '
                                          'read of a\n'
                                          'long file shows its start and end and leaves out its '
                                          'middle, where\n'
                                          'the rules are (Tony, 2026-10-05).\n'
                                          "Earlier: 1.10 | 2026-10-02, with Anthropic's Claude "
                                          'Opus 5.5, from\n'
                                          'orrery @ 5e42b00b and gallery @ 0ffa4518. v1.10 (L-406) '
                                          'writes down\n'
                                          "Tony's rule for a feature's info link, which lived only "
                                          'on L-265: a\n'
                                          'NASA page where one is specific to the feature, '
                                          'otherwise English\n'
                                          'Wikipedia, with the corona the one named exception. '
                                          'Asked on\n'
                                          '2026-10-02, while the galactic tide was being redrawn, '
                                          'whether the\n'
                                          "skills covered how a feature's hover, info panel and "
                                          'drawing are\n'
                                          'written; the hover and the drawing were covered and the '
                                          'link was not.\n'
                                          'The same day Settings refused the first copy '
                                          '("malformed YAML\n'
                                          'frontmatter"): the new fires_when words sat on a line '
                                          'of their own.\n'
                                          'They are back on the one line, and the version stays '
                                          '1.10, which never\n'
                                          'loaded anywhere (L-406, L-407).\n',
                                          1),
                                         ('the rule',
                                          '- Text CLAIMS the page makes -- the i-panel copy, the '
                                          'frame note --\n'
                                          '  carry their source in the page itself, because the '
                                          'assembler does not\n'
                                          "  pass through the provenance scanner. The frame note's "
                                          'NAIF citation\n'
                                          '  is the form.\n',
                                          "- Text CLAIMS the page makes about ITSELF -- a room's "
                                          'own i-panel\n'
                                          '  copy, the frame note -- carry their source in the '
                                          'page itself,\n'
                                          '  because the assembler does not pass through the '
                                          'provenance scanner.\n'
                                          "  The frame note's NAIF citation is the form.\n"
                                          '- **A fact about one feature is served with that '
                                          "feature's words,\n"
                                          '  never typed in a renderer** (v1.12, L-421). Code may '
                                          'type a sentence\n'
                                          '  only when it is about the picture: a drawing choice '
                                          '("drawn round",\n'
                                          '  "our choice for the picture"), a frame limit, or how '
                                          'to use the\n'
                                          '  page. A sentence about nature, about a paper, or '
                                          'naming a source --\n'
                                          '  which particles a belt holds, how far a paper plots '
                                          'its model, the\n'
                                          "  paper's name -- is served on the feature's row with "
                                          'its source, and\n'
                                          '  the renderer prints what it is given. Where such a '
                                          'fact has no\n'
                                          '  served row, the fix is a served row, not a typed '
                                          'line. The first\n'
                                          '  case is Earth\'s inner belt: its "trapped protons" is '
                                          'the served\n'
                                          "  `flux_peak_of`, beside the belts' other words. The "
                                          'rest found in the\n'
                                          '  Earth and Sun rooms on 2026-10-06 are listed in\n'
                                          '  '
                                          'documentation/MANIFEST_L421_typed_facts_20261006.md.\n',
                                          1)]}


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
        raise SystemExit("ERROR: %s is not the October 5 Where We Are this "
                         "patch replaces. NOTHING was written." % WWA_PATH)
    carried = [line[2:] for line in difflib.ndiff(WWA_BASE.split("\n"),
                                                   current.split("\n"))
               if line.startswith("+ ")]
    if carried:
        block = "\n".join("    " + line for line in carried)
    else:
        block = "    (none: the page was as pushed at e7073fce)"
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
