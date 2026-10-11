"""patch_L431_2_run_record_notes_20261011.py -- Tony's notes in his run
record of 2026-10-10 and 11, each put on its ledger item; the two
maintenance-run checks that had no dashboard button get one.

Built on orrery 6fc36483ffc630f1f618f60317761add3c7cc4eb at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-10-26_2019_run_record.md"); gallery
fd17abf1cf99169289acfeb0a45f84365265c255 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read, not
touched. Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 11, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    Save this file in the orrery folder named above (the one that holds
    LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run.
    Success prints one "ok" line per edit, then "patch applied". The
    steps after it are printed at the end.

WHAT IT CHANGES
    palomas_orrery_dashboard.py -- two buttons under the orrery's
        checkers, in alphabetical place: Test Hills Cloud Sampler
        (L-421) and Test Scanner Row Run (L-414). Both checks were in the
        maintenance run with no button. Stamped.
    LEDGER_CONSOLIDATED.md -- header stamp; L-433 (the road after the
        Sun and Earth rooms) and L-432 (objects drawn in the default
        goldenrod) opened; Tony's notes added to L-395, L-408, L-410,
        L-416, L-424, L-431 and L-136; three lines owed to skills on
        L-351.
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker. 129 lines above the marker.
    documentation/DESIGN_L431_orbital_periods_20261011.md -- your local
        folders in its header.
    documentation/HANDOFF_L421_oort_orrery_20261010.md -- section 13,
        your notes and where each went.

    This script is the delivery; move it to documentation/ once it has
    run.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once. If any check fails, NOTHING is written. A
    file found with Windows line endings is matched after turning them
    into LF and written back LF, and the patch says so. A file this
    patch would create that is already there with the same content is
    accepted and named; with different content the patch refuses. Undo
    after a run is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = 'documentation/WHERE_WE_ARE.md'
MARKER = b'--- Your run record below this line'

EDITS = [('palomas_orrery_dashboard.py', 'line 1184', '         "Ledger L-156, sub-steps 1d and 1e.",\n         SCRIPT_DIR,\n', '         "Ledger L-156, sub-steps 1d and 1e.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Scanner Row Run",\n         "test_row_run.py",\n         "Pins for the provenance scanner (L-414): a row\'s citation is read "\n         "from its own comment run, declared rows are named as their own "\n         "kind, and the gate-path figure is computed and recorded by name. "\n         "Run after editing provenance_scanner.py.",\n         SCRIPT_DIR,\n'), ('palomas_orrery_dashboard.py', 'line 1132', '         True),\n        ("Test Objects Export",\n', '         True),\n        ("Test Hills Cloud Sampler",\n         "test_hills_cloud_sampler.py",\n         "The Hills cloud\'s three checks, each first shown able to fail: "\n         "four faults are planted (the galactic pole\'s RA and Dec swapped, "\n         "the ecliptic node set to 0, the paper\'s Fig. 3 reading moved, the "\n         "tilt pushed to 60 degrees) and each must be caught, then the real "\n         "rows must pass. Ends on \\"HILLS CLOUD: PASS\\" (L-421).",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Objects Export",\n'), ('palomas_orrery_dashboard.py', 'line 171', 'did not name the export\'s two new fields.\n"""\n', 'did not name the export\'s two new fields.\nOctober 11, 2026 with Anthropic\'s Claude Opus 5.5 (L-416, on Tony\'s\nnote in his run record: "add new checks to the dashboard"): Test Hills\nCloud Sampler (L-421) and Test Scanner Row Run (L-414) under the\norrery\'s checkers, in alphabetical place. Both checkers were in the\nmaintenance run with no button.\n"""\n'), ('LEDGER_CONSOLIDATED.md', 'line 22028', "  when this is designed, L-410's drawing rule applies to it.\n**Gap:** not scoped -- design conversation needed.\n", '  when this is designed, L-410\'s drawing rule applies to it.\n- **Tony, 2026-10-10, in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648), on Where We Are\'s\n  "The scattered disk, with the Kuiper belt": "we should decide this. i\n  lean yes." Moved to the design-talk list.\n**Gap:** not scoped -- design conversation needed.\n'), ('LEDGER_CONSOLIDATED.md', 'line 22016', '#### [L-136] Solar "scattered disk" shell\n<!-- L:136 status:OPEN upd:2026-10-04 section:D.Feature-B flag: rice:2/2/50/2 -->\n- **Idea (Tony, 4/18/26, pre-ledger note).** Add a shell/region for the\n', '#### [L-136] Solar "scattered disk" shell\n<!-- L:136 status:OPEN upd:2026-10-11 section:D.Feature-B flag: rice:2/2/50/2 -->\n- **Idea (Tony, 4/18/26, pre-ledger note).** Add a shell/region for the\n'), ('LEDGER_CONSOLIDATED.md', 'line 20057', "  steps and Pole of date among them.\n**Gap:** none here. L-300's sweep gets its button with the website patch\n", '  steps and Pole of date among them.\n- **2026-10-11, Tony\'s note in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648): "add new\n  checks to the dashboard. this should be part of the skill." Matched\n  again against the orrery runner\'s own list: two checkers had no\n  button -- Hills cloud sampler (L-421, `test_hills_cloud_sampler.py`,\n  whose build of 2026-10-10 missed the button) and Scanner row run\n  (L-414, `test_row_run.py`, 2026-10-09). Both added in\n  `patch_L431_2_run_record_notes_20261011.py`. The gallery runner\'s 27\n  checks all have buttons. The rule is owed to agentic-pre-test\'s next\n  version (L-351). A checker that compares the two lists would make the\n  rule unforgettable; that is a change to a checker, for a session of\n  its own, if Tony wants it.\n**Gap:** none here. L-300\'s sweep gets its button with the website patch\n'), ('LEDGER_CONSOLIDATED.md', 'line 20036', "#### [L-416] Every maintenance-run step has a dashboard button (dashboard, both repos)\n<!-- L:416 status:DONE upd:2026-10-05 section:C flag: rice: -->\n- **Tony's question, 2026-10-05:** was the new check added to the runner\n", "#### [L-416] Every maintenance-run step has a dashboard button (dashboard, both repos)\n<!-- L:416 status:DONE upd:2026-10-11 section:C flag: rice: -->\n- **Tony's question, 2026-10-05:** was the new check added to the runner\n"), ('LEDGER_CONSOLIDATED.md', 'line 3552', "  - interactive-exhibit and the protocol: as above.\n**Gap:** Each lands with its store's next bump.\n", '  - interactive-exhibit and the protocol: as above.\n  - **2026-10-11, from Tony\'s notes in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648):\n    - agentic-pre-test: a new checker in either maintenance run gets\n      its dashboard button in the same patch (Tony: "add new checks to\n      the dashboard. this should be part of the skill."; L-416).\n    - ledger-and-session-records: the handoff header names Tony\'s\n      local folders beside the GitHub anchor (Tony: "the location of\n      the local files should be included in the handoff header along\n      with the github info"). The folders themselves are in the skill\n      since 1.19 (Tony\'s Local Folders); the header line is not.\n    - safe-file-editing: a patch that creates a file accepts one\n      already there with identical content and says so; different\n      content still refuses. Tony: "if i have already downloaded a\n      design document or handoff to documentations/ and the patch\n      creates it again, the patch will refuse. i have to go back and\n      delete the download, then the patch runs."\n      `patch_L431_2_run_record_notes_20261011.py` already works this\n      way.\n**Gap:** Each lands with its store\'s next bump.\n'), ('LEDGER_CONSOLIDATED.md', 'line 3466', '#### [L-351] Rules learned at C2, owed to the next bumps of their stores (skills, protocol)\n<!-- L:351 status:OPEN upd:2026-10-09 section:A flag: rice: -->\n- **Recorded, not built.** A class found while building L-322 Stage C2\n', '#### [L-351] Rules learned at C2, owed to the next bumps of their stores (skills, protocol)\n<!-- L:351 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Recorded, not built.** A class found while building L-322 Stage C2\n'), ('LEDGER_CONSOLIDATED.md', 'line 2296', '    to distinguish objects commonly drawn together". Encke keeps the\n    default goldenrod; no row is owed.\n  - Encke\'s hover has no orbital period, because the typed table never\n', '    to distinguish objects commonly drawn together". Encke keeps the\n    default goldenrod for now. AMENDED 2026-10-11 by Tony\'s note in\n    his run record (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648): "the default color is often goldenrod, but we\n    should switch it up to avoid clashing with nearby objects. small,\n    but it matter for the render." The objects that fall to the\n    default are L-432.\n  - Encke first in the comet list, in the orrery window: "done. looks\n    great." Pushed at d3c4c385.\n  - Encke\'s hover has no orbital period, because the typed table never\n'), ('LEDGER_CONSOLIDATED.md', 'line 1652', "  both.\n**Gap:** Tony's decision above; if yes, a session builds it with a test\n", '  both.\n- **Tony, 2026-10-10, in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648), on the decision:\n  "unclear". It moves to the design-talk list, to be explained there in\n  plain words before he decides.\n**Gap:** Tony\'s decision above; if yes, a session builds it with a test\n'), ('LEDGER_CONSOLIDATED.md', 'line 1628', '#### [L-424] The checker reports one word for two different cases (worksheet checker)\n<!-- L:424 status:OPEN upd:2026-10-09 section:A flag: rice: -->\n- **Found 2026-10-08,** building L-418, while checking the L-252\n', '#### [L-424] The checker reports one word for two different cases (worksheet checker)\n<!-- L:424 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Found 2026-10-08,** building L-418, while checking the L-252\n'), ('LEDGER_CONSOLIDATED.md', 'line 1403', "  fallback; whether it prints at all is the design's question 6.\n**Gap:** the design talk, then the build. Seven questions in the\n", '  fallback; whether it prints at all is the design\'s question 6.\n- **Tony\'s note in his run record of 2026-10-10** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648): "the orbital\n  periods dictionary is hand maintained and instead should be fetched\n  from Horizons along with the other osculating data. however, there is\n  a wrinkle: the center body for the data matters: the sun or the solar\n  barycenter. we should also implement this because it matters for\n  orbital periods, especially highly perturbed ones." On the proposed\n  rule: "for discussion".\n**Gap:** the design talk, then the build. Seven questions in the\n'), ('LEDGER_CONSOLIDATED.md', 'line 1370', '\n#### [L-431] Orbital periods from JPL, for every body, printed by their errors (orrery, provenance)\n', '\n#### [L-433] The road after the Sun and Earth rooms, in Tony\'s words (planning)\n<!-- L:433 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Tony, 2026-10-10, in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648), two notes:\n  - "a couple of things to keep in mind. before we close the sun and\n    earth rooms, i would like to implement fuzzy boundaries. and in the\n    last session we found something important. the orbital periods\n    dictionary is hand maintained and instead should be fetched from\n    Horizons along with the other osculating data." (L-410, L-431.)\n  - "the near term goal is to complete the sun and earth room\n    thoroughly as a template for other body rooms. then add the symbols\n    for most if not all the orrery\'s objects list. then we can decide on\n    priorities. the "golden artifacts" are one path, but not the only\n    one. I would be inclined to work on the inner planets after that.\n    and we should not forget the earth science part."\n- **Against Where We Are\'s road, as it stood at 6fc3648:** the Sun and\n  Earth rooms (stages 5 to 7) and the objects (stage 11) agree. Stage 13\n  reads "The planets get their details, Jupiter and Saturn first";\n  Tony\'s note leans to the inner planets. Stage 14 is the Earth System\n  layers, his "earth science part".\n**Gap:** at the next design talk after the orbital periods: Tony\nconfirms the order, and the road and the master plan\'s critical path\n(`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`, Section 5a) are\nrewritten to it. Until then the road stands, with his lean noted.\n**Ref:** L-410; L-431; L-412; L-413; L-221 (the master plan is the\nroadmap); `documentation/WHERE_WE_ARE.md`.\n\n#### [L-432] Objects drawn in the default goldenrod (orrery, colours)\n<!-- L:432 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Tony, 2026-10-10, in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648): "the color dictionary\n  is a drawing choice and kept by hand. the default color is often\n  goldenrod, but we should switch it up to avoid clashing with nearby\n  objects. small, but it matter for the render."\n- **Discovery, 2026-10-11, at 6fc3648** (a list, nothing fixed; The\n  Braid). `color_map()` in `constants_new.py` returns \'goldenrod\' for a\n  name it does not hold, and the orrery calls it by display name. Of\n  the 191 entries in `celestial_objects.py`, 27 names are not in it:\n  Encke; OSIRISREx, OSIRISAPE, Bennu/OSIRIS; Earth-Moon Barycenter,\n  Patroclus-Menoetius Barycenter, Pluto-Charon Barycenter, Haumea\n  System Barycenter, Eris-Dysnomia Barycenter, Eris/Dysnomia,\n  Gonggong-Xiangliu Barycenter; TRAPPIST-1 and its planets b to h,\n  TOI-1338 A/B, TOI-1338 A (G-type), TOI-1338 B (M-type), TOI-1338 b\n  and c, Proxima Centauri, Proxima Centauri b and d. Encke is seen\n  goldenrod in the render (L-395). The barycentres and the exoplanet\n  systems may be coloured by other code; not traced.\n- A colour is a drawing choice (Tony), so no row needs a source. Each\n  pick is Mode 5: Tony\'s eye on the bodies it is drawn beside.\n**Gap:** trace which of the 27 actually draw goldenrod; then Tony picks\ncolours, Encke first, beside Halley and the other comets.\n**Ref:** `constants_new.py` (`color_map`); `celestial_objects.py`;\nL-395.\n\n#### [L-431] Orbital periods from JPL, for every body, printed by their errors (orrery, provenance)\n'), ('LEDGER_CONSOLIDATED.md', 'line 1180', "  its detection floor of 100 Earth radii (L-292), has no edge at all.\n**Gap:** a design talk before any build. The Sun slice's ninth item\n", '  its detection floor of 100 Earth radii (L-292), has no edge at all.\n- **Tony, 2026-10-10, in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648): "before we close the\n  sun and earth rooms, i would like to implement fuzzy boundaries."\n  So this item belongs to finishing those two rooms (L-433).\n**Gap:** a design talk before any build. The Sun slice\'s ninth item\n'), ('LEDGER_CONSOLIDATED.md', 'line 1157', "#### [L-410] Fuzzy boundaries for edges known only as ranges, the outer corona first (orrery + gallery, the Sun's slice)\n<!-- L:410 status:OPEN upd:2026-10-05 section:A flag: rice: -->\n- **Tony's idea, 2026-10-04**, deciding where the Roche limit is drawn:\n", "#### [L-410] Fuzzy boundaries for edges known only as ranges, the outer corona first (orrery + gallery, the Sun's slice)\n<!-- L:410 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Tony's idea, 2026-10-04**, deciding where the Roche limit is drawn:\n"), ('LEDGER_CONSOLIDATED.md', 'line 1148', "  (L-421); this rides the gallery session that follows it.\n**Gap:** the gallery build, with the inner Oort cloud's gallery side\n", '  (L-421); this rides the gallery session that follows it.\n- **Tony, 2026-10-10, in his run record** (`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md` at 6fc3648), beside "awaits the\n  design talk": "yes. it awaited only for implementation not in\n  principle."\n**Gap:** the gallery build, with the inner Oort cloud\'s gallery side\n'), ('LEDGER_CONSOLIDATED.md', 'line 1077', "#### [L-408] A Galactic Plane toggle in the Sun room (gallery, the Sun's slice)\n<!-- L:408 status:OPEN upd:2026-10-10 section:A flag: rice: -->\n- **Asked 2026-10-03** by Tony, looking for the galactic tide's X on\n", "#### [L-408] A Galactic Plane toggle in the Sun room (gallery, the Sun's slice)\n<!-- L:408 status:OPEN upd:2026-10-11 section:A flag: rice: -->\n- **Asked 2026-10-03** by Tony, looking for the galactic tide's X on\n"), ('LEDGER_CONSOLIDATED.md', 'line 342', 'list), built on 9f154782.\nReview and RICE update Tony 6-21-2026\n', "list), built on 9f154782.\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5\n(Tony's notes in his run record of 2026-10-10 and 11: L-432 and L-433\nopened; L-395, L-408, L-410, L-416, L-424, L-431, L-136 and L-351\nupdated; two dashboard buttons), built on 6fc36483.\nReview and RICE update Tony 6-21-2026\n"), ('documentation/WHERE_WE_ARE.md', 'line 113', '  `documentation/DESIGN_L431_orbital_periods_20261011.md`\n- The typed facts: plan\n', '  `documentation/DESIGN_L431_orbital_periods_20261011.md`\n- Your notes of Oct 10: `WHERE_WE_ARE_10-10-26_2019_run_record.md`\n- The typed facts: plan\n'), ('documentation/WHERE_WE_ARE.md', 'line 105', '2. Choosing a date, and animation.\n3. The scattered disk, with the Kuiper belt. Not the fuzzy-boundary idea.\n\n', '2. Choosing a date, and animation.\n\n'), ('documentation/WHERE_WE_ARE.md', 'line 96', "- The tide's cone and brightness on the phone: L-408 (the galactic\n  plane on the phone). The ring, poles and Sgr A* were ruled Oct 9.\n\nDecisions, one at a time:\n- L-424 (the checker's one word for two cases): whether the\n  checker itself prints two different words.\n\n", "- The tide's cone and brightness on the phone: L-408 (the galactic\n  plane on the phone). The rest is ruled; it waits only on the build.\n\n"), ('documentation/WHERE_WE_ARE.md', 'line 91', '  the typed table, the apsidal markers.*\n- The fuzzy outer corona, with the dust cloud; the exosphere the same way.\n', '  the typed table, the apsidal markers.*\n- Your order after the Sun and Earth rooms (L-433), in your words of\n  Oct 10; the road changes when you confirm it.\n- L-424 (the checker\'s one word for two cases): you marked it\n  "unclear" (Oct 10). I explain it in plain words, then you decide.\n- The scattered disk, with the Kuiper belt (L-136): "we should\n  decide this. i lean yes." (Oct 10)\n- The fuzzy outer corona, with the dust cloud; the exosphere the same way.\n'), ('documentation/WHERE_WE_ARE.md', 'line 81', "Read from files when this page was written, not typed from memory.\n- Last cache build: 20261010T221109Z, ok, no retry; the one before retried once.\n- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  9f15478 (your run of 2026-10-10). Whole tree: 292.\n- This page's date and the ledger's newest stamp: both Oct 11. Agree.\n", "Read from files when this page was written, not typed from memory.\n- Last cache build: 20261011T134230Z, ok, no retry.\n- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  6fc3648 (your run of 2026-10-11). Whole tree: 292.\n- This page's date and the ledger's newest stamp: both Oct 11. Agree.\n"), ('documentation/WHERE_WE_ARE.md', 'line 74', "  harmless; delete by hand. (Oct 8, Oct 10)\n- An object's words in the list carry no numbers unless they come\n  from the store. (Oct 8)\n- Code types only words about our picture; facts are served. (Oct 6)\n\n", '  harmless; delete by hand. (Oct 8, Oct 10)\n\n'), ('documentation/WHERE_WE_ARE.md', 'line 66', "  making; a change to a checker gets its own session. (Oct 8)\n- A long skill gets its reading plan at its next version, not in a\n  bump of its own. (Oct 8)\n- The galactic tide keeps its cone, to show its pull as physics. (Oct 7)\n- No colour or other name that only one system knows. The panels'\n", "  making; a change to a checker gets its own session. (Oct 8)\n- No colour or other name that only one system knows. The panels'\n"), ('documentation/WHERE_WE_ARE.md', 'line 57', '- Comets listed by first apparition, oldest first. A colour is a\n  drawing choice, to tell apart bodies drawn together. (Oct 10)\n- The Hills cloud follows the paper: drawn from its Fig. 3, described\n', '- Comets listed by first apparition, oldest first. A colour is a\n  drawing choice, to tell apart bodies drawn together; switch it up\n  from the default goldenrod. (Oct 10)\n- Fuzzy boundaries come before the Sun and Earth rooms close. Every\n  new check gets its dashboard button. (Oct 10)\n- The Hills cloud follows the paper: drawn from its Fig. 3, described\n'), ('documentation/WHERE_WE_ARE.md', 'line 46', " 12.   [later] Encounters: comets and spacecraft at the dates that matter.\n 13.   [later] The planets get their details, Jupiter and Saturn first.\n 14.   [later] The Earth System layers; the gallery's cards meanwhile.\n", " 12.   [later] Encounters: comets and spacecraft at the dates that matter.\n 13.   [later] The planets get their details, Jupiter and Saturn first;\n               you lean to the inner planets (L-433). << new this session\n 14.   [later] The Earth System layers; the gallery's cards meanwhile.\n"), ('documentation/WHERE_WE_ARE.md', 'line 36', "  6a.  [next]  *Orbital periods from JPL for every body, printed by\n               their errors: design talk first.* << new this session\n  7.   [next]  The Sun's numbers get the checking Earth's got.\n", "  6a.  [next]  *Orbital periods from JPL for every body, printed by\n               their errors: design talk first.*\n  7.   [next]  The Sun's numbers get the checking Earth's got.\n"), ('documentation/WHERE_WE_ARE.md', 'line 20', '> **Needs you now:**\n> - *Orrery: run patch_L431_1, then the maintenance run (22 of 22),\n>   push.*\n', '> **Needs you now:**\n> - *Orrery: run patch_L431_2, then the maintenance run (22 of 22),\n>   push.*\n'), ('documentation/WHERE_WE_ARE.md', 'line 9', "> **Changed since you last read this:**\n> - Your looks: Encke and Halley (four checks) and the Hills cloud\n>   (three) are all correct, as you marked them. Pushed at 9f15478.\n> - Encke moves to the top of the comet list, the oldest first.\n> - Orbital periods: your rulings and JPL's numbers are written up.\n>   Around the Sun, Sedna's period moved 370 years in one year; around\n>   the solar system's centre of mass, 7 days. L-431 (orbital periods).\n>\n", '> **Changed since you last read this:**\n> - Your notes in the run record are in the ledger, each on its item.\n>   Your order after the Sun and Earth rooms: L-433 (the road after).\n> - Two checks had no dashboard button; both have one now.\n> - Objects that fall to the default goldenrod are listed: L-432\n>   (default colours). Encke first.\n> - Orbital periods are written up: L-431 (orbital periods).\n>\n'), ('documentation/WHERE_WE_ARE.md', 'line 3', '\nLast updated: October 11, 2026, at the inner Oort cloud close (orrery).\n- Written at orrery 9f15478 and gallery a7d1a54.\n\n', '\nLast updated: October 11, 2026, after your notes in the run record.\n- Written at orrery 6fc3648 and gallery fd17abf.\n\n'), ('documentation/DESIGN_L431_orbital_periods_20261011.md', 'line 9', '5.5, at the close of the L-421 (the typed facts) orrery session.\n\n', "5.5, at the close of the L-421 (the typed facts) orrery session.\nTony's local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\n\n"), ('documentation/HANDOFF_L421_oort_orrery_20261010.md', 'line 328', '  the L-431 design talk.\n', '  the L-431 design talk.\n\n## 13. Tony\'s notes in the run record, October 11, 2026\n\nBuilt on orrery 6fc36483ffc630f1f618f60317761add3c7cc4eb (Tony\'s push of his run record) at\nhttps://github.com/tonylquintanilla/palomas_orrery and gallery fd17abf\nat https://github.com/tonylquintanilla/tonyquintanilla.github.io.\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nDelivered as `patch_L431_2_run_record_notes_20261011.py`.\n\nTony wrote notes on the page part of his timestamped copy,\n`documentation/WHERE_WE_ARE_10-10-26_2019_run_record.md`, after the\nclose patch had been built. Each went to its item:\n\n- Fuzzy boundaries before the Sun and Earth rooms close: L-410.\n- The road after those rooms, inner planets leaning first, and the\n  earth science part not forgotten: L-433 (new), for the design talk.\n- The orbital periods and the centre: L-431.\n- Colours: switch up the default goldenrod. 27 names fall to it; L-432\n  (new) lists them. Encke\'s line on L-395 is amended.\n- Local folders in the handoff header; a patch refusing a file Tony\n  already downloaded; new checks on the dashboard: owed to three\n  skills\' next versions (L-351). This patch already accepts an\n  identical file, and adds the two missing dashboard buttons (L-416):\n  Test Hills Cloud Sampler, missed by this session\'s build, and Test\n  Scanner Row Run, missed by L-414\'s.\n- L-408: "it awaited only for implementation not in principle."\n- The Oort edge question: settled on 2026-10-09 (the band from 10,000\n  to 20,000 au) and built here; already off the page.\n- L-424: "unclear"; to the design-talk list, to be explained.\n- The scattered disk (L-136): "i lean yes"; to the design-talk list.\n')]

NEW_FILES = {}


def fail(msg):
    print('FAILURE: ' + msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def full(path):
    return os.path.join(ROOT, *path.split('/'))


def non_ascii(data):
    return sum(1 for ch in data if ch > 127)


def main():
    if not os.path.exists(full('LEDGER_CONSOLIDATED.md')):
        fail("LEDGER_CONSOLIDATED.md is not in this folder. Save the patch in "
             "the orrery repo's root folder.")
    ledger = open(full('LEDGER_CONSOLIDATED.md'), 'rb').read()
    if b'<!-- L:433 ' in ledger and b'<!-- L:432 ' in ledger:
        print('already applied: L-432 and L-433 are in the ledger. Nothing written.')
        return 0
    if b'<!-- L:431 ' not in ledger:
        fail('patch_L431_1_close_20261011.py has not run here (L-431 is not in '
             'the ledger). This patch is built on 6fc3648, which holds it.')
    present = []
    for path, content in NEW_FILES.items():
        if os.path.exists(full(path)):
            have = open(full(path), 'rb').read().replace(b'\r\n', b'\n')
            if have == content.encode('ascii'):
                present.append(path)
            else:
                fail('%s already exists with different content. Compare it with '
                     'the one this patch carries before deleting either.' % path)

    texts, crlf = {}, []
    for path, _, _, _ in EDITS:
        if path not in texts:
            if not os.path.exists(full(path)):
                fail('%s not found.' % path)
            raw = open(full(path), 'rb').read()
            if b'\r\n' in raw:
                crlf.append(path)
            texts[path] = raw.replace(b'\r\n', b'\n')
    before = {path: non_ascii(data) for path, data in texts.items()}
    if texts[PAGE].count(MARKER) != 1:
        fail('WHERE_WE_ARE.md: the run-record marker was not found once.')
    below = texts[PAGE][texts[PAGE].index(MARKER):]

    for path, label, old, new in EDITS:
        try:
            o, n = old.encode('ascii'), new.encode('ascii')
        except UnicodeEncodeError:
            fail('%s -- %s: this patch would insert non-ASCII text.' % (path, label))
        count = texts[path].count(o)
        if count != 1:
            fail('ANCHOR FAIL %s -- %s: expected 1 match, found %d. Has that part '
                 'changed since 6fc3648?' % (path, label, count))
        texts[path] = texts[path].replace(o, n)
        print('ok  %-34s %s' % (path, label))
    if texts[PAGE][texts[PAGE].index(MARKER):] != below:
        fail('WHERE_WE_ARE.md: an edit reached below the run-record marker.')
    for path, data in texts.items():
        if path.endswith('.py') and non_ascii(data):
            fail('%s would hold %d non-ASCII byte(s).' % (path, non_ascii(data)))

    for path, data in texts.items():
        with open(full(path), 'wb') as handle:
            handle.write(data)
    for path, content in NEW_FILES.items():
        if path in present:
            print('ok  %-34s already there, identical; left as it is' % path)
            continue
        with open(full(path), 'wb') as handle:
            handle.write(content.encode('ascii'))
        print('ok  %-34s created' % path)
    for path in crlf:
        print('note: %s was CRLF in the working copy; written LF' % path)
    for path, count in before.items():
        if count:
            print('note: %s holds %d non-ASCII byte(s) this patch did not reach '
                  '(Tony\'s notes, if below the run-record marker)' % (path, count))
    above = texts[PAGE][:texts[PAGE].index(MARKER)].count(b'\n')
    print('note: WHERE_WE_ARE.md has %d lines above the run-record marker '
          '(the cap is 130)' % above)
    print('stamps updated: the ledger header; the module docstring of '
          'palomas_orrery_dashboard.py; WHERE_WE_ARE.md date line')
    print('patch applied: %d edits in %d files.' % (len(EDITS), len(texts)))
    print('')
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect "22 of 22 gating checkers '
          'passed" and "GATE PATH: 0 TIER-1 -- the push gate holds". It rebuilds '
          'the ledger index with L-432 and L-433.')
    print('  2. If you like, open the dashboard: Test Hills Cloud Sampler and Test '
          'Scanner Row Run are under the orrery checks; each should end on PASS.')
    print('  3. Move this script into documentation/; commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
