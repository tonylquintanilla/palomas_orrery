"""patch_L395_7_records_20261010.py -- the close of the L-395 build: the
ledger, Tony's page, the build record, the dashboard's Horizons buttons,
ledger-and-session-records 1.19, horizons-orbital-mechanics 1.2 and
protocol v3.90.

Built on orrery 32619f8d6ac4cd0806da3ea8e7442f04ceea0ecd at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-10-26_1426_run_record.md"), with gallery
a7d1a542ae5b6d26dc3c658c339fcf721d181780 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily run
again to check"). Written October 10, 2026 with Anthropic's Claude Opus
5.5.

HOW TO RUN
    The patch sits in the orrery repo's ROOT folder (the folder that
    holds LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run. Or,
    from a terminal in that folder:
        python patch_L395_7_records_20261010.py
    Success prints one "ok" line per edit, then "patch applied". The
    steps after it are printed at the end.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md -- header stamp; L-395 (the Horizons check):
        the build, Tony's first live run, the comets' names, the
        findings, the Gap narrowed, the pause note struck; L-414 (the
        scanner's window) closed on the 2.28 read-back.
    documentation/WHERE_WE_ARE.md -- by section, never below the
        run-record marker: the date, the box, road stage 8 done, Settled,
        Signals, Where the details are.
    documentation/HANDOFF_L395_horizons_check_build_20261010.md --
        created: the build record, with the four Mode 5 checks.
    palomas_orrery_dashboard.py -- Horizons Check in the Daily Run
        group; Horizons Check Suite and Horizons Confirmations in the
        gallery checks; fixed in passing, the Daily Run's and the cache
        builder's words still telling you to pause OneDrive, and Daily
        Run Steps' "three scripts".
    skills/ledger-and-session-records/SKILL.md -- 1.18 -> 1.19: Tony's
        Local Folders. Its v1.16 entry moves to
        documentation/SKILL_HISTORIES.md.
    skills/horizons-orbital-mechanics/SKILL.md -- 1.1 -> 1.2: Checking
        an Entry Against JPL, and two corrected pinning lines.
    PROJECT_INSTRUCTIONS.md -- v3.89 -> v3.90; v3.87 moves down to
        documentation/PROJECT_INSTRUCTIONS_HISTORY.md.

SAFETY
    Each file is checked only at the lines this patch edits: every
    anchor must match exactly once, and a moved entry must arrive word
    for word. If any check fails, NOTHING is written. A file found with
    Windows line endings is matched after turning them into LF and
    written back LF, and the patch says so. Undo after a run is Discard
    Changes in GitHub Desktop (and delete the new handoff).
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header stamp',
     'built on a6678b0f.\nReview and RICE update Tony 6-21-2026\n',
     "built on a6678b0f.\nModule updated: October 10, 2026 with Anthropic's Claude Opus 5.5\n(L-395 built: the Horizons check, Daily Run step 2, its first live run\n13 of 13; Encke's list entry; Halley keyed; L-414 closed on the 2.28\nread-back; ledger-and-session-records 1.19, horizons-orbital-mechanics\n1.2, protocol v3.90), built on 32619f8d.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-414 closed',
     '**Gap:** Tony\'s run. The maintenance run should end on "GATE PATH: 0\nTIER-1 -- the push gate holds" and "21 of 21 gating checkers passed".\nThen this item closes.\n',
     '- **Closed 2026-10-10** in the L-395 build session (Claude Opus 5.5),\n  whose first reply read back its loaded provenance-discipline as 2.28,\n  matching the manifest: the obligation this item carried is\n  discharged. That session\'s maintenance run on a copy at ca5bbe12\n  plus its patch, and Tony\'s own run of 2026-10-10 (his copy\n  `documentation/WHERE_WE_ARE_10-10-26_1426_run_record.md`), both end\n  on "21 of 21 gating checkers passed" with the scanner row "0 TIER-1\n  -- the push gate holds". Loose ends were re-homed when they were\n  found: CENTER_BODY_RADII to L-427, the two marker sizes to L-372,\n  the solar-wind rows to L-314, the status reading to L-351.\n**Gap:** none. DONE 2026-10-10.\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-414 status',
     '<!-- L:414 status:PENDING-GATE upd:2026-10-09 section:A flag: rice: -->',
     '<!-- L:414 status:DONE upd:2026-10-10 section:A flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-395 date',
     '<!-- L:395 status:OPEN upd:2026-10-08 section:A flag: rice: -->',
     '<!-- L:395 status:OPEN upd:2026-10-10 section:A flag: rice: -->'),
    ('LEDGER_CONSOLIDATED.md', 'L-395 the build and its first live run',
     '  is no longer only "say 24 hours": ask Tony then whether the pause\n  step becomes optional or goes.\n**Gap:** The first build is done (the room\'s eleven bodies). Still open:\nthe Horizons cross-check, designed 2026-10-07 and built next from\n`documentation/DESIGN_L395_horizons_check_20261007.md` (its first run\nlists and fixes nothing except simple errors, reported); Encke\'s list\nentry; fields the list lacks (a moon\'s parent, a\nclean kind); the remaining served objects; L-391 to L-394. The numbers\nin the other descriptions are L-403.\n',
     '  is no longer only "say 24 hours": ask Tony then whether the pause\n  step becomes optional or goes. ANSWERED 2026-10-10 before this\n  build reached it: Tony retired the pause ("the retry is\n  sufficient"), and gallery patch_L429_3 took the step out of\n  `daily_run.py` (L-216, L-429). Struck here.\n- **2026-10-10, the Horizons check built** (Claude Opus 5.5, from\n  `documentation/HANDOFF_L395_horizons_check_build_brief_20261010.md`;\n  record `documentation/HANDOFF_L395_horizons_check_build_20261010.md`).\n  - Orrery, `patch_L395_5_horizons_name_and_encke_20261010.py`:\n    `horizons_name`, JPL\'s exact name, on the thirteen keyed entries;\n    Halley keyed (`halley`) with Tony\'s words of 2026-10-08 and NASA\'s\n    1P/Halley page; Encke\'s own entry (`encke`, record 90000091,\n    "2P/Encke") with a checkbox under Halley\'s and INFO[\'Encke\']; the\n    export carries `horizons_name` and `object_type` and refuses a\n    keyed entry without a `horizons_name`, shown failing on a planted\n    entry. Fixed in passing: the two s-acute letters of "Wierzchos" in\n    `info_dictionary.py`, the file\'s only non-ASCII. Pushed in d83cc5e.\n  - Gallery, `patch_L395_6_horizons_check_gallery_20261010.py`:\n    `tools/horizons_check.py` (Daily Run step 2, before the cache\n    builder), `tools/check_horizons_confirmations.py` and\n    `tools/test_horizons_check.py` (two gating rows of the maintenance\n    run), `documentation/horizons_answers_L395.json` (the tests\'\n    answers, each with its source); Encke\'s wrong "2022-epoch" note\n    gone. The tests catch, by entry and field, a wrong id, either wrong\n    index, a name off by one letter, a stale pin, a record number given\n    to another comet, a wrong barycentre type, JPL unreachable and an\n    answer that is not JPL\'s; the offline checker fails on a\n    confirmation deleted, one overdue and one changed. Pushed in\n    4a34221 and a7d1a54.\n  - Tested in the sandbox, which cannot reach JPL: the orrery window\n    headless with Encke ticked (JPL asked for record 90000091 as a\n    small body; Encke, its orbit and its tail drawn), the orrery\n    maintenance run 21 of 21, the gallery\'s 26 rows with the two\n    expected reds.\n- **Tony\'s runs, 2026-10-10**, from his copy\n  `documentation/WHERE_WE_ARE_10-10-26_1426_run_record.md`: the orrery\n  maintenance run "21 of 21 gating checkers passed"; the gallery run\n  before the Daily Run, the two expected reds ("Horizons\n  confirmations", "Cache in step" on the two comets\' names); then the\n  Daily Run, whose step 2 was the check\'s FIRST LIVE RUN: "Examined 13\n  entries: 13 due, 26 queries asked of JPL", every entry "agrees",\n  Halley\'s pin "the newest of 30", Encke\'s "the newest of 61" with\n  solution date 2026-Oct-09_14:41:02, and "HORIZONS CHECK: PASS -- 13\n  checked today, 0 not due". After its cache build: "26 of 26 gating\n  checkers passed"; the live run "2 of 2". Tony: "correct."\n- **Ruled 2026-10-10:** the website\'s names for the two comets.\n  Asked whether the website should show "Halley and Encke" (the list\'s\n  names) or "1P/Halley and 2P/Encke", Tony chose "Halley and Encke\n  (Recommended)". JPL\'s form stays in `horizons_name`.\n- **Found re-fetching JPL\'s answers, 2026-10-10** (through the chat\'s\n  web-fetch tool, fields compared, not bytes): record 90004956 held\n  MAPS (C/2026 A1) on 2026-10-07 and PANSTARRS (C/2025 Y3) on\n  2026-10-10, MAPS having moved to 90004957 -- a recent comet\'s record\n  number is not stable (the orrery finds MAPS by designation, so it is\n  unaffected; it is a test case now). JPL re-solved Encke\'s record on\n  2026-10-09. The recorded "sstr=9" answer is identical to the\n  major-body-only answer and is probably a paste slip: live, "9" also\n  finds asteroid 9 Metis, so the design\'s note that it found no\n  asteroid was wrong; the check searches each index apart and is\n  unaffected. horizons-orbital-mechanics 1.2 records all three.\n**Gap:** The check is built and runs every day. Still open: fields the\nlist lacks (a moon\'s parent, a clean kind); the remaining served\nobjects (moon, io, titan, pluto, charon, voyager_1, which have no key\nyet); the display-name rename; MAPS and 3I/ATLAS checked live when\nserved; L-391 to L-394. The numbers in the other descriptions are\nL-403. Tony\'s look at Encke and Halley in the orrery\'s window (four\nchecks in the build record).\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-395 Ref',
     '**Ref:** `documentation/DESIGN_L395_horizons_check_20261007.md`; `documentation/HORIZONS_ANSWERS_L395_20261007.md`; `celestial_objects.py`;',
     '**Ref:** `documentation/DESIGN_L395_horizons_check_20261007.md`; `documentation/HORIZONS_ANSWERS_L395_20261007.md`; `documentation/HANDOFF_L395_horizons_check_build_20261010.md`; gallery `tools/horizons_check.py`, `tools/check_horizons_confirmations.py`, `tools/test_horizons_check.py`, `data/horizons_confirmations.json`; `celestial_objects.py`;'),
    ('palomas_orrery_dashboard.py', 'stamp',
     'Collapsed Features under the gallery checks, in alphabetical place,\nfor the checker the gallery runner gained that day; the offline\nrunner\'s description names it.\n"""',
     'Collapsed Features under the gallery checks, in alphabetical place,\nfor the checker the gallery runner gained that day; the offline\nrunner\'s description names it.\nOctober 10, 2026 with Anthropic\'s Claude Opus 5.5 (L-395), on Tony\'s\nrequest: Horizons Check in the Daily Run group, after the guest book,\nas the Daily Run\'s step 2; Horizons Check Suite and Horizons\nConfirmations under the gallery checks, in alphabetical place; the\noffline runner\'s description names both. Fixed in passing, because they\nno longer said what the code does: the Daily Run button and the cache\nbuilder\'s routine still told Tony to pause OneDrive (retired 2026-10-10,\nL-216), Daily Run Steps still said three scripts, and Objects Export\ndid not name the export\'s two new fields.\n"""'),
    ('palomas_orrery_dashboard.py', 'Daily Run: words',
     '         "(L-281, Tony\'s design of 2026-09-27). First the Guest Book "\n         "Updater: approve or decline each new message, and write entries "\n         "or replies if you like. Then it asks you to pause OneDrive and "\n         "note the time, and runs the Gallery Cache Builder; type s at "\n         "that question to skip the build today. Then the Gallery "\n         "Maintenance Run, offline, which the builder\'s own next steps "\n         "ask for before a commit. A step that reports a problem does not "\n         "stop the next one. It ends with one summary naming each step\'s "\n         "result and what is left for you: commit and push in GitHub "\n         "Desktop, the live maintenance run, and resuming OneDrive. It "\n         "opens by saying when the last cache build was, so a missed day "\n         "shows. It never commits or pushes. Everything indented below is "\n         "included in it and can still be run on its own.",',
     '         "(L-281, Tony\'s design of 2026-09-27). First the Guest Book "\n         "Updater: approve or decline each new message, and write entries "\n         "or replies if you like. Then the Horizons Check: JPL confirms "\n         "the website\'s objects that are due (L-395). Then the Gallery "\n         "Cache Builder, with no OneDrive pause since 2026-10-10 (L-216: "\n         "the retry is sufficient). Then the Gallery Maintenance Run, "\n         "offline, which the builder\'s own next steps ask for before a "\n         "commit. A step that reports a problem does not stop the next "\n         "one. It ends with one summary naming each step\'s result and "\n         "what is left for you: commit and push in GitHub Desktop, and "\n         "the live maintenance run. It opens by saying when the last "\n         "cache build was, so a missed day shows. It never commits or "\n         "pushes. Everything indented below is included in it and can "\n         "still be run on its own.",'),
    ('palomas_orrery_dashboard.py', 'Daily Run: the Horizons Check button',
     '         "tools/guestbook_local.json, which git ignores.",\n         GALLERY_REPO_DIR,\n         True,\n         None,\n         True),\n',
     '         "tools/guestbook_local.json, which git ignores.",\n         GALLERY_REPO_DIR,\n         True,\n         None,\n         True),\n        ("Horizons Check",\n         os.path.join("tools", "horizons_check.py"),\n         "The Daily Run\'s second step (L-395). Asks JPL Horizons whether "\n         "each object the website takes from the orrery\'s list is still "\n         "the object the list says -- the same id, the same index, JPL\'s "\n         "exact name -- for the entries that are due: each every 30 days, "\n         "and at once after its entry changes. A pinned comet record "\n         "(Halley, Encke) must still be JPL\'s newest. One line per entry; "\n         "for each disagreement the list\'s value, JPL\'s value and the "\n         "query to paste into a browser. Records each confirmation in "\n         "data/horizons_confirmations.json and never edits the list. "\n         "Needs the internet; if JPL cannot be reached it says so and "\n         "asks nothing more. Runs from the gallery repo ROOT.",\n         GALLERY_REPO_DIR,\n         True,\n         None,\n         True),\n'),
    ('palomas_orrery_dashboard.py', 'cache builder: the routine without the pause',
     '         "THE ROUTINE (L-216). Pause OneDrive syncing and NOTE THE TIME -- "\n         "a pause lasts 2 hours -- then run the build. It ends with a "\n',
     '         "THE ROUTINE (L-216). Run the build: no OneDrive pause since "\n         "2026-10-10, the retry is sufficient. It ends with a "\n'),
    ('palomas_orrery_dashboard.py', 'Daily Run group: the maintenance run is step 4',
     '         "The Daily Run\'s third step: the same button as Gallery "\n',
     '         "The Daily Run\'s fourth step: the same button as Gallery "\n'),
    ('palomas_orrery_dashboard.py', 'offline runner names the two Horizons rows',
     '        "the config mirror check, the pointer join, cache in step, the "\n        "collapsed-features sweep, the "\n',
     '        "the config mirror check, the Horizons check suite, Horizons "\n        "confirmations, the pointer join, cache in step, the "\n        "collapsed-features sweep, the "\n'),
    ('palomas_orrery_dashboard.py', 'Objects Export: the two new fields',
     '         "name for it, with its name, Horizons id, id type, description "\n         "(without its opening \\"Horizons:\\" sentence) and NASA link. The "\n         "website pulls this file and never reads orrery source (L-395). "\n         "Lists every number in an exported description. Writes nothing if "\n         "an entry writes a field twice or a key repeats.",',
     '         "name for it, with its name, Horizons id, JPL\'s exact name, id "\n         "type, object type, description (without its opening "\n         "\\"Horizons:\\" sentence) and NASA link. The website pulls this "\n         "file and never reads orrery source (L-395). Lists every number in "\n         "an exported description. Writes nothing if an entry writes a "\n         "field twice, a key repeats, or a keyed entry has no JPL name.",'),
    ('palomas_orrery_dashboard.py', 'Daily Run Steps: four scripts',
     '        "daily_run.py --check: fails if any of the three scripts the "\n',
     '        "daily_run.py --check: fails if any of the four scripts the "\n'),
    ('palomas_orrery_dashboard.py', 'gallery checks: the two Horizons buttons',
     '        ("Hover Budget",\n        os.path.join("documentation", "run_hover_budget.py"),',
     '        ("Horizons Check Suite",\n        os.path.join("tools", "test_horizons_check.py"),\n        "The Horizons check on JPL\'s recorded answers, with no network "\n        "(documentation/horizons_answers_L395.json, each answer with its "\n        "source): every served entry agrees, and each planted mistake -- a "\n        "wrong id, the wrong index, a name off by one letter, a stale pin, "\n        "a record number JPL gave to another comet, JPL unreachable -- is "\n        "caught by name (L-395). GATES the gallery runner.",\n        GALLERY_REPO_DIR,\n        True,\n        None,\n        True),\n        ("Horizons Confirmations",\n        os.path.join("tools", "check_horizons_confirmations.py"),\n        "Reads data/horizons_confirmations.json offline and fails on any "\n        "served object never confirmed against JPL, confirmed 30 or more "\n        "days ago, or changed since it was confirmed -- so a Horizons "\n        "Check that stopped running shows (L-395). GATES the gallery "\n        "runner.",\n        GALLERY_REPO_DIR,\n        True,\n        None,\n        True),\n        ("Hover Budget",\n        os.path.join("documentation", "run_hover_budget.py"),'),
    ('skills/ledger-and-session-records/SKILL.md', 'version line 1.19',
     "Skill version: 1.18 | 2026-10-08, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ b0b3df82. v1.18 (L-418) records two conventions the",
     'Skill version: 1.19 | 2026-10-10, with Anthropic\'s Claude Opus 5.5, at\npalomas_orrery @ 32619f8d. v1.19 (L-395), on Tony\'s request: Tony\'s\nLocal Folders, under Where a File Goes, names the two repositories\'\nfolders on his machine, so a session linked to it saves a patch where\nhe runs it. Tony, 2026-10-10: "palomas_orrery_for_github is the repo\nfolder."\nEarlier: 1.18 | 2026-10-08, with Anthropic\'s Claude Opus 5.5, at\npalomas_orrery @ b0b3df82. v1.18 (L-418) records two conventions the'),
    ('skills/ledger-and-session-records/SKILL.md', 'the v1.16 entry moves out',
     "Earlier: 1.16 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ d9f47a87. v1.16 (L-419) adds one rule under Where We\nAre -- Tony's page: a patch checks a document Tony annotates (this\npage, the handoffs, the ledger) only at the lines it edits, and a\nrewrite of the page carries his notes into the handoff first. The\nrule had lived only in one patch's code and was broken the same day.\n",
     ''),
    ('skills/ledger-and-session-records/SKILL.md', 'older-entries line',
     'Older entries are in documentation/SKILL_HISTORIES.md, moved there\non 2026-10-05 (L-418), 2026-10-07 (L-422) and 2026-10-08 (L-418).',
     'Older entries are in documentation/SKILL_HISTORIES.md, moved there\non 2026-10-05 (L-418), 2026-10-07 (L-422), 2026-10-08 (L-418) and\n2026-10-10 (L-395).'),
    ('skills/ledger-and-session-records/SKILL.md', 'contents: the new heading',
     '- Where a File Goes [QUALITY]\n- Handoff Structure (the load-bearing lines)',
     "- Where a File Goes [QUALITY]\n  - Tony's Local Folders [QUALITY]\n- Handoff Structure (the load-bearing lines)"),
    ('skills/ledger-and-session-records/SKILL.md', "Tony's Local Folders",
     'finished" cut would have sent the worksheets themselves the other\nway.)\n\n## Handoff Structure (the load-bearing lines)',
     'finished" cut would have sent the worksheets themselves the other\nway.)\n\n### Tony\'s Local Folders [QUALITY]\n\nBoth repositories are clones on Tony\'s Windows machine, under\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\` (Tony, 2026-10-10):\n\n- orrery: `palomas_orrery_for_github\\`. The folders named `orrery` and\n  `palomas_orrery` beside it are not the repository.\n- gallery: `tonyquintanilla.github.io\\`\n\nWhen the session is linked to his computer, a patch is saved straight\ninto that repository\'s root folder, and Tony runs it there from VS\nCode. When it is not linked, the patch goes as an attachment and Tony\nsaves it there. Either way the patch still checks the files it edits,\nso a copy saved in the wrong folder refuses rather than editing it.\n\n(Tony\'s request, 2026-10-10, after a session had held a patch back\nbecause three folders could have been the orrery: "palomas_orrery_for_github\nis the repo folder.")\n\n## Handoff Structure (the load-bearing lines)'),
    ('skills/horizons-orbital-mechanics/SKILL.md', 'version line 1.2',
     'Skill version: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12\nSource: project_instructions_v3_29.md Part 3 + Part 5 technical lessons.',
     "Skill version: 1.2 | 2026-10-10, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 32619f8d and gallery @ a7d1a542. v1.2 (L-395) adds\nChecking an Entry Against JPL, what the Horizons check's build learned:\nJPL's Lookup cannot see record numbers; a bare number also finds\nasteroids and spacecraft, so an entry is found in three steps; JPL\nre-solves a record in place; and a recent comet's record number can be\ngiven to another comet. It corrects two lines under Small-Body Record\nPinning: Encke's pin now lives in the orrery's list, and what a pin\ndoes not follow is a NEWER record, not a new solution.\nEarlier: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12\nSource: project_instructions_v3_29.md Part 3 + Part 5 technical lessons."),
    ('skills/horizons-orbital-mechanics/SKILL.md', "pinning: Encke's pin in the list",
     "  needed. Halley id='90000030' (celestial_objects.py); Encke '90000091'\n  (gallery objects_config.json). Proven live 2026-07-11.\n- Cost of pinning: a pinned record does NOT auto-track a future JPL\n  solution update. Recheck pinned records periodically, like any frozen\n  upstream identifier.",
     "  needed. Halley id='90000030' and Encke '90000091', both in\n  celestial_objects.py since 2026-10-10 (L-395). Proven live 2026-07-11.\n- Cost of pinning: JPL re-solves a record IN PLACE (Encke's 90000091\n  took new solutions on 2026-10-01 and 2026-10-09 under the same\n  number), so a pin fixes the apparition, not the numbers. What a pin\n  does not follow is a NEWER record, which JPL adds for a new\n  apparition. The gallery's Horizons check (tools/horizons_check.py,\n  the Daily Run's step 2) confirms every 30 days that each pin is still\n  the newest record for its comet and reports a newer one for Tony; it\n  never re-pins."),
    ('skills/horizons-orbital-mechanics/SKILL.md', 'Checking an Entry Against JPL',
     '## Reference Frame Diagnostic\n',
     '## Checking an Entry Against JPL (L-395)\n\nLearned building the Horizons check, 2026-10-07 to 2026-10-10. The\ndesign and every answer it rests on are in the orrery\'s documentation/:\nDESIGN_L395_horizons_check_20261007.md and\nHORIZONS_ANSWERS_L395_20261007.md.\n\n- Two services. The Lookup (`api/horizons_lookup.api`) turns a name or\n  number into the objects it matches. Horizons\' main service\n  (`api/horizons.api`) answers about one record (COMMAND=\'<record>\') or\n  lists every record for a designation (COMMAND=\'DES=<desig>;\').\n- The Lookup cannot see record numbers: "90000030" and "90000091" both\n  give "no matches found". A pinned record is checked through the main\n  service.\n- A bare number is ambiguous. "499" also finds asteroid 499 Venusia;\n  "9" finds the Pluto barycentre, asteroid 9 Metis and spacecraft with\n  9 in their names. So an entry is found in three steps: search the\n  index its id_type points at (group=mb for a blank, group=sb for\n  "smallbody"); keep the match whose primary SPKID (major bodies) or\n  primary designation (small bodies) equals the id; exactly one must\n  remain. The other index must find nothing, or the id_type is wrong.\n- JPL\'s names are not the orrery\'s. A comet carries its designation in\n  brackets ("MAPS (C/2026 A1)", "ATLAS (C/2025 N1)"); the main service\n  names a pinned periodic record "1P/Halley". The list keeps JPL\'s exact\n  form in `horizons_name` and its own in `name`.\n- A RECENT comet\'s record number is not stable. 90004956 held MAPS\n  (C/2026 A1) on 2026-10-07 and another comet, PANSTARRS (C/2025 Y3),\n  on 2026-10-10; MAPS had moved to 90004957. Halley\'s and Encke\'s\n  numbers did not move. So find a comet with a single record by its\n  designation, as the orrery finds MAPS, and pin a record number only\n  for a periodic comet with many records, where the designation alone\n  is ambiguous. A pin is checked by its record\'s name as well as its\n  number, which is how a record that changed hands shows.\n- Read JPL\'s live answers, not its documentation\'s examples: the\n  Lookup\'s documentation gives Apophis\'s primary SPKID as 2099942,\n  while the live answer is 20099942, with 2099942 an older alias.\n\n## Reference Frame Diagnostic\n'),
    ('PROJECT_INSTRUCTIONS.md', 'header stamp',
     'Tony Quintanilla, PE | Claude | v3.89 | October 10, 2026\n',
     'Tony Quintanilla, PE | Claude | v3.90 | October 10, 2026\n'),
    ('PROJECT_INSTRUCTIONS.md', 'SHA anchor',
     'Cut from a6678b0f at https://github.com/tonylquintanilla/palomas_orrery\n',
     'Cut from 32619f8d at https://github.com/tonylquintanilla/palomas_orrery\n'),
    ('PROJECT_INSTRUCTIONS.md', 'v3.90 entry',
     'v3.89 (October 10, 2026): No rule changed in this document. TWO\n',
     'v3.90 (October 10, 2026): No rule changed in this document. TWO\nskills, one version each: ledger-and-session-records 1.18 -> 1.19 and\nhorizons-orbital-mechanics 1.1 -> 1.2 (L-395). TONY\'S FOLDERS ARE\nNAMED, AND A COMET\'S RECORD NUMBER IS NOT A NAME.\n\nWHAT PROMPTED IT. The Horizons check was built and ran live for the\nfirst time: 13 of 13 served objects agree with JPL. Two things came out\nof the session. Tony asked that his local folders be written into the\nhandoff skill, after a session had held a patch back because three\nfolders could have been the orrery: "palomas_orrery_for_github is the\nrepo folder." And re-fetching JPL\'s answers showed record 90004956\nholding MAPS on 2026-10-07 and another comet three days later.\n\nWHAT CHANGED. ledger-and-session-records gains Tony\'s Local Folders,\nunder Where a File Goes. horizons-orbital-mechanics gains Checking an\nEntry Against JPL: the Lookup cannot see record numbers, the three-step\nfind, JPL\'s names, a recent comet\'s record number moving, and live\nanswers over documented ones; and two corrected lines under Small-Body\nRecord Pinning. The brief for this build asked for at most one skill\nversion; Tony\'s request made it two. Their v1.16 entry (the ledger\nskill) moved to documentation/SKILL_HISTORIES.md, by the three-entry\nrule; the Horizons skill had one entry.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copies read\nledger-and-session-records 1.19 and horizons-orbital-mechanics 1.2\nbefore ledger or Horizons work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.87 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\nv3.89 (October 10, 2026): No rule changed in this document. TWO\n'),
    ('PROJECT_INSTRUCTIONS.md', 'v3.87 moves out',
     "v3.87 (October 9, 2026): No rule changed in this document. ONE\nskill bump, one version (L-414): provenance-discipline 2.27 -> 2.28.\nTHE SCANNER READS A ROW'S OWN COMMENT BLOCK, AND PRINTS THE GATE BY\nNAME.\n\nWHAT PROMPTED IT. The scanner read a constant's sources through a\nfixed window, 30 lines above and 15 below. In constants_new.py, where\nrows sit with no blank line between them, it failed both ways: it\nmissed EARTH_MEAN_RADIUS_KM's own Source line 16 lines down\n(2026-10-04), and when the planted-fault run of 2026-10-09 removed the\nthermopause row's Source lines it credited the stratopause row's\ninstead. It scored three declared rows as uncited measurements. And no\ntool printed the push gate's own figure: the console said its count\nwas not the gate and named nothing.\n\nWHAT CHANGED. provenance-discipline, under Scanner Mechanics and The\nGoal State: a constants_new.py row is read through its own comment\nrun; a declared row with its reason written down is named and never\nTier-1; the gate path is read from data/constants_export.json and\ndata/objects_export.json and printed by name, on the console, in the\naudit and in the run history. provenance_scanner.py and\nprovenance_history.py build it; test_row_run.py pins it, and\norrery_maintenance_run.py runs those pins and quotes the GATE PATH\nline. Measured at aa46bb10: whole-tree Tier-1 296 to 293; gate path 4\nto 0, the four being the scanner's own faults. CENTER_BODY_RADII\nentered Tier-1 off the gate path (L-427).\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nprovenance-discipline 2.28 before any provenance work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.84 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n",
     ''),
    ('documentation/PROJECT_INSTRUCTIONS_HISTORY.md', 'receives v3.87',
     '\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n',
     "\nv3.87 (October 9, 2026): No rule changed in this document. ONE\nskill bump, one version (L-414): provenance-discipline 2.27 -> 2.28.\nTHE SCANNER READS A ROW'S OWN COMMENT BLOCK, AND PRINTS THE GATE BY\nNAME.\n\nWHAT PROMPTED IT. The scanner read a constant's sources through a\nfixed window, 30 lines above and 15 below. In constants_new.py, where\nrows sit with no blank line between them, it failed both ways: it\nmissed EARTH_MEAN_RADIUS_KM's own Source line 16 lines down\n(2026-10-04), and when the planted-fault run of 2026-10-09 removed the\nthermopause row's Source lines it credited the stratopause row's\ninstead. It scored three declared rows as uncited measurements. And no\ntool printed the push gate's own figure: the console said its count\nwas not the gate and named nothing.\n\nWHAT CHANGED. provenance-discipline, under Scanner Mechanics and The\nGoal State: a constants_new.py row is read through its own comment\nrun; a declared row with its reason written down is named and never\nTier-1; the gate path is read from data/constants_export.json and\ndata/objects_export.json and printed by name, on the console, in the\naudit and in the run history. provenance_scanner.py and\nprovenance_history.py build it; test_row_run.py pins it, and\norrery_maintenance_run.py runs those pins and quotes the GATE PATH\nline. Measured at aa46bb10: whole-tree Tier-1 296 to 293; gate path 4\nto 0, the four being the scanner's own faults. CENTER_BODY_RADII\nentered Tier-1 off the gate path (L-427).\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nprovenance-discipline 2.28 before any provenance work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.84 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n(Moved down from the resident protocol on 2026-10-10 when\nv3.90 made a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n"),
    ('documentation/SKILL_HISTORIES.md', "receives the ledger skill's v1.16 entry",
     '\n## gallery-cache-builder\n',
     "\nThe skill's v1.16 entry, moved here word for word on 2026-10-10 when\nv1.19 made a fourth entry (L-395):\nEarlier: 1.16 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ d9f47a87. v1.16 (L-419) adds one rule under Where We\nAre -- Tony's page: a patch checks a document Tony annotates (this\npage, the handoffs, the ledger) only at the lines it edits, and a\nrewrite of the page carries his notes into the handoff first. The\nrule had lived only in one patch's code and was broken the same day.\n\n## gallery-cache-builder\n"),
    ('documentation/WHERE_WE_ARE.md', 'date line',
     "Last updated: October 10, 2026, at the lobby's third round.\n- Written at orrery a6678b0 and gallery cb9038c, before your runs.",
     'Last updated: October 10, 2026, at the Horizons check build.\n- Written at orrery 32619f8 and gallery a7d1a54, after your runs.'),
    ('documentation/WHERE_WE_ARE.md', 'the box',
     "> **Changed since you last read this:**\n> - L-429 (the room button on the row): Go To sits in the middle of\n>   every room's list, the room button after it; long names wrap.\n> - Artifact 1 passes again; the Daily Run no longer pauses OneDrive.\n>   L-428 (the lobby's way in) is closed.\n>\n> **Do next:** *as you confirmed: the typed facts (the inner Oort\n> cloud, then the check); the Horizons check build; the Sun's list\n> from item 3.*\n>\n> **Needs you now:**\n> - *Gallery: run patch_L429_3, the maintenance run, push; look on the\n>   phone. Orrery: run patch_L429_4, the maintenance run, push.*\n> - Upload interactive-exhibit (1.14) and gallery-cache-builder (1.8);\n>   the Project's instructions to v3.89.\n",
     "> **Changed since you last read this:**\n> - The Daily Run checks the website's objects against JPL (step 2).\n>   First run: all 13 agree, both comet pins the newest. L-395 (the\n>   Horizons check).\n> - Encke has its own entry and checkbox in the orrery; the website\n>   says Halley and Encke. L-414 (the scanner's window) is closed.\n>\n> **Do next:** *the typed facts: the inner Oort cloud, then the check\n> (L-421, the typed facts); then the Sun's list from item 3.*\n>\n> **Needs you now:**\n> - *Orrery: run patch_L395_7, the maintenance run, push.*\n> - Upload ledger-and-session-records (1.19) and\n>   horizons-orbital-mechanics (1.2); the Project's instructions to v3.90.\n> - *Look at Encke and Halley in the orrery window: four checks in\n>   the build record.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'road stage 8',
     '  8.   [next]  The served objects are checked against JPL Horizons.\n               Designed and recorded; build next, with Encke added\n               and Halley checked too.\n',
     '  8.   [done]  The served objects are checked against JPL Horizons\n               every day, in the Daily Run. << moved this session\n'),
    ('documentation/WHERE_WE_ARE.md', "settled: the comets' names",
     "  room's list: Go To in the middle, then the room's button. (Oct 10)\n",
     '  room\'s list: Go To in the middle, then the room\'s button. (Oct 10)\n- Website names: Halley and Encke; JPL\'s "1P/Halley" stays in the list. (Oct 10)\n'),
    ('documentation/WHERE_WE_ARE.md', 'signals',
     '- Last cache build: 20261010T135737Z, ok, no retry.\n- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  a6678b0. Whole tree: 293.',
     '- Last cache build: 20261010T221109Z, ok, no retry; the one before retried once.\n- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at\n  32619f8. Whole tree: 293.'),
    ('documentation/WHERE_WE_ARE.md', 'where the details are',
     "- The lobby, the room button: L-428, L-429; `HANDOFF_L429_round3_20261010.md`\n- Scanner window: L-414 (the scanner's window), L-427 (rows a neighbour\n  had credited); `documentation/HANDOFF_L414_scanner_window_20261009.md`\n",
     '- The lobby, the room button: L-428, L-429; `HANDOFF_L429_round3_20261010.md`\n'),
    ('documentation/WHERE_WE_ARE.md', 'where the details are: the Horizons check',
     '  the hand run), L-412 (the RICE ruling), L-395 (the Horizons check,\n  designed). Open for build: L-421 (the typed facts).',
     '  the hand run), L-412 (the RICE ruling), L-395 (the Horizons check,\n  built). Open for build: L-421 (the typed facts).'),
    ('documentation/WHERE_WE_ARE.md', 'where the details are: the build record',
     '- The Horizons check design:\n  `documentation/DESIGN_L395_horizons_check_20261007.md`',
     '- The Horizons check: design\n  `documentation/DESIGN_L395_horizons_check_20261007.md`; record\n  `documentation/HANDOFF_L395_horizons_check_build_20261010.md`'),
]

HANDOFF_PATH = 'documentation/HANDOFF_L395_horizons_check_build_20261010.md'
HANDOFF = '<!-- Doc-Kind: hand | Build record for L-395, the Horizons check: the orrery\'s list gains JPL\'s exact names, Halley keyed, Encke\'s own entry; the gallery\'s live check as Daily Run step 2, its offline checker and tests; Tony\'s first live run, 13 of 13. Written October 10, 2026. -->\n# Handoff: L-395, the Horizons check, built\n\nBuilt on orrery ca5bbe12cb8f1c48b134f6aadaa700d45ae9e39d ("L427\nrecords") at https://github.com/tonylquintanilla/palomas_orrery and\ngallery 050637c3688e1bfcff81848ad4780b8a9e975a9e ("daily run again") at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io, both\npinned with `git ls-remote` at the session\'s start.\nMiddle push (the orrery half): orrery d83cc5e ("L395 horizons name and\nencke"), then 32619f8d with Tony\'s run record.\nGallery pushed at 4a34221 and a7d1a542 ("daily run again to check").\nThis record lands with `patch_L395_7_records_20261010.py`, built on\norrery 32619f8d; its push is the next commit.\n\n- Type: BUILD, two repos. From\n  `documentation/HANDOFF_L395_horizons_check_build_brief_20261010.md`.\n- Skills loaded, read back in the first reply, each matching the\n  manifest of protocol v3.89: provenance-discipline 2.28 (L-414 closes\n  on it), gallery-cache-builder 1.8, horizons-orbital-mechanics 1.1,\n  safe-file-editing 1.13, agentic-pre-test 1.3,\n  ledger-and-session-records 1.18.\n- Ledger: L-395 (the Horizons check) gains the build, the first live\n  run, the comets\' names and three findings; L-414 (the scanner\'s\n  window) closes.\n\nSession written October 2026 with Anthropic\'s Claude Opus 5.5.\n\n## Read this first\n\n- *The Daily Run\'s step 2 asks JPL Horizons about each object the\n  website serves. Its first live run: 13 of 13 agree; Halley\'s and\n  Encke\'s pinned records are JPL\'s newest.*\n- *Encke has its own entry in the orrery\'s list, and a checkbox under\n  Halley\'s.*\n- *Still to do: Tony\'s look at Encke and Halley in the orrery window\n  (section 6).*\n\n## 1. The orrery half\n\n`patch_L395_5_horizons_name_and_encke_20261010.py`, run by Tony and\npushed in d83cc5e.\n\n- `celestial_objects.py`: `horizons_name`, JPL\'s exact name, on the\n  thirteen keyed entries (Sun, Mercury, Venus, Earth, Mars, Jupiter,\n  Saturn, Uranus, Neptune, "Pluto Barycenter", "99942 Apophis",\n  "1P/Halley", "2P/Encke"). `name` is untouched everywhere.\n- Halley: key `halley`; Tony\'s words of 2026-10-08; NASA\'s 1P/Halley\n  page.\n- Encke: a new entry, key `encke`, record 90000091, id_type smallbody,\n  with Tony\'s words and NASA\'s 2P/Encke page. Nothing else in the\n  orrery looked Encke up by name except `celestial_coordinates.py`,\n  which already had a row for it.\n- `palomas_orrery.py`: `comet_encke_var` and an "Encke\n  (1786-present, periodic)" checkbox, perihelion "October 22, 2023".\n  Both dates come from JPL\'s answers G4 and G3.\n- `info_dictionary.py`: INFO[\'Encke\'], the checkbox\'s tooltip. Fixed in\n  passing: the file\'s only non-ASCII, the s-acute of "Wierzchos", twice.\n- `export_objects.py` and `test_objects_export.py`: the export carries\n  `horizons_name` and `object_type`; a keyed entry without a\n  `horizons_name` is refused, and the test\'s self-test shows that\n  refusal before it trusts a pass.\n- Encke draws in the default goldenrod: `constants_new.py` has no\n  Encke colour and the patch did not touch the store.\n\n## 2. The gallery half\n\n`patch_L395_6_horizons_check_gallery_20261010.py`, run by Tony and\npushed in 4a34221 and a7d1a542.\n\n- `tools/horizons_check.py`: the live check, the Daily Run\'s step 2.\n  It reads the pulled `data/objects_export.json`, finds each entry in\n  the three steps of the design, checks a pinned record through\n  Horizons\' main service, and records each confirmation in\n  `data/horizons_confirmations.json`. One query at a time with a pause;\n  after the first failure it asks JPL nothing more that run.\n- `tools/check_horizons_confirmations.py`: offline, gating; fails on an\n  entry never confirmed, 30 days old, or changed since confirmed.\n- `tools/test_horizons_check.py`: offline, gating, 36 checks on\n  `documentation/horizons_answers_L395.json`.\n- `daily_run.py`: four steps. `gallery_maintenance_run.py`: two rows.\n- `data/objects_config.json`: Encke\'s note no longer says "2022-epoch".\n- The website\'s names for the two comets became "Halley" and "Encke"\n  through the objects mirror, by Tony\'s ruling (section 4).\n\n## 3. Verification\n\n- In the sandbox, on copies:\n  - the orrery window headless with Encke ticked, through the real\n    plot_objects(): JPL was asked for record 90000091 as a small body,\n    and Encke, its Keplerian orbit and its tail were drawn;\n  - a planted entry with no `horizons_name`: the test and the export\n    both fail, naming Earth;\n  - the orrery maintenance run 21 of 21, gate path 0 Tier-1 on 13\n    served objects (it was 11);\n  - every patch twice (the second refuses) and on a CRLF copy;\n  - the gallery maintenance run: the two expected reds only, "Horizons\n    confirmations" and "Cache in step".\n- The sandbox cannot reach JPL. The chat\'s web-fetch tool can, so JPL\'s\n  answers were re-fetched on 2026-10-10, fields compared rather than\n  bytes. 25 of 28 read the same; the three differences are section 5.\n  Fifteen answers the tests needed and the design had not fetched were\n  fetched the same way; the fixture names each answer\'s source.\n- Tony\'s runs, from `documentation/WHERE_WE_ARE_10-10-26_1426_run_record.md`:\n  the orrery run "21 of 21 gating checkers passed"; the gallery\'s two\n  expected reds; then the Daily Run\'s step 2, the first live run,\n  "Examined 13 entries: 13 due, 26 queries asked of JPL", every entry\n  "agrees", "HORIZONS CHECK: PASS -- 13 checked today, 0 not due";\n  after its build "26 of 26 gating checkers passed"; the live run "2 of\n  2". Tony: "correct."\n\n## 4. Ruled this session\n\n- The website\'s names for the two comets: "Halley and Encke\n  (Recommended)", over "1P/Halley and 2P/Encke". Neither name was shown\n  on a page at the time.\n- Tony\'s local folders go into the handoff skill:\n  "palomas_orrery_for_github is the repo folder." Recorded in\n  ledger-and-session-records 1.19.\n- Tony asked for the Horizons checks on the dashboard; patch_L395_7\n  adds the three buttons.\n\n## 5. Found, and where each went\n\n- A recent comet\'s record number is not stable: 90004956 held MAPS on\n  2026-10-07 and PANSTARRS (C/2025 Y3) on 2026-10-10, with MAPS at\n  90004957. The orrery finds MAPS by designation and is unaffected. A\n  test case now; horizons-orbital-mechanics 1.2.\n- JPL re-solved Encke\'s record on 2026-10-09 under the same number.\n  horizons-orbital-mechanics 1.2.\n- The recorded "sstr=9" answer is identical to the major-body-only one,\n  probably a paste slip: live, "9" also finds asteroid 9 Metis. The\n  design\'s line that "9" found no asteroid was wrong. The check is\n  unaffected. On L-395.\n- The dashboard still told Tony to pause OneDrive. Fixed in passing by\n  patch_L395_7.\n\n## 6. Mode 5, Tony\'s look in the orrery window\n\n1. Under Comets, below Halley: "Encke (1786-present, periodic)"; its\n   tooltip reads "Horizons: 2P/Encke. A short-period comet whose dust\n   trail is the source of the Taurid meteor showers." and "Perihelion:\n   October 22, 2023".\n2. Tick only Encke, centre on the Sun, today, plot: its marker, orbit\n   and tail. The marker is goldenrod, the default; a colour of its own\n   is one line in `constants_new.py` if wanted.\n3. Go: Perihelion under Encke frames the October 2023 perihelion. Needs\n   the internet; not testable in the sandbox.\n4. Halley\'s hover shows its new words and NASA\'s 1P/Halley link.\n\n## 7. Tony\'s steps\n\n1. **(do)** Run `patch_L395_7_records_20261010.py` in the orrery root,\n   then `orrery_maintenance_run.py`; move the patch into\n   `documentation/`; commit and push.\n2. **(do)** Upload ledger-and-session-records and\n   horizons-orbital-mechanics (each its SKILL.md); replace the\n   Project\'s instructions with `PROJECT_INSTRUCTIONS.md` (v3.90).\n3. **(do)** The Mode 5 look, section 6.\n\n## 8. What travels\n\n- ledger-and-session-records went to 1.19 and horizons-orbital-mechanics\n  to 1.2 in a session that loaded 1.18 and 1.1. The next session\n  confirms its loaded copies read 1.19 and 1.2 before ledger or Horizons\n  work.\n- The brief asked for at most one skill version this session; Tony\'s\n  request for his folders made it two.\n- Next on the road: the typed facts, the inner Oort cloud first (L-421),\n  from `documentation/HANDOFF_L421_oort_orrery_build_brief_20261009.md`.\n'
V387 = "v3.87 (October 9, 2026): No rule changed in this document. ONE\nskill bump, one version (L-414): provenance-discipline 2.27 -> 2.28.\nTHE SCANNER READS A ROW'S OWN COMMENT BLOCK, AND PRINTS THE GATE BY\nNAME.\n\nWHAT PROMPTED IT. The scanner read a constant's sources through a\nfixed window, 30 lines above and 15 below. In constants_new.py, where\nrows sit with no blank line between them, it failed both ways: it\nmissed EARTH_MEAN_RADIUS_KM's own Source line 16 lines down\n(2026-10-04), and when the planted-fault run of 2026-10-09 removed the\nthermopause row's Source lines it credited the stratopause row's\ninstead. It scored three declared rows as uncited measurements. And no\ntool printed the push gate's own figure: the console said its count\nwas not the gate and named nothing.\n\nWHAT CHANGED. provenance-discipline, under Scanner Mechanics and The\nGoal State: a constants_new.py row is read through its own comment\nrun; a declared row with its reason written down is named and never\nTier-1; the gate path is read from data/constants_export.json and\ndata/objects_export.json and printed by name, on the console, in the\naudit and in the run history. provenance_scanner.py and\nprovenance_history.py build it; test_row_run.py pins it, and\norrery_maintenance_run.py runs those pins and quotes the GATE PATH\nline. Measured at aa46bb10: whole-tree Tier-1 296 to 293; gate path 4\nto 0, the four being the scanner's own faults. CENTER_BODY_RADII\nentered Tier-1 off the gate path (L-427).\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nprovenance-discipline 2.28 before any provenance work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.84 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n"
OLD116 = "Earlier: 1.16 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ d9f47a87. v1.16 (L-419) adds one rule under Where We\nAre -- Tony's page: a patch checks a document Tony annotates (this\npage, the handoffs, the ledger) only at the lines it edits, and a\nrewrite of the page carries his notes into the handoff first. The\nrule had lived only in one patch's code and was broken the same day.\n"
MARKER = b"--- Your run record below this line"


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is not needed.")
    sys.exit(1)


def full(path):
    return os.path.join(ROOT, *path.split("/"))


def main():
    if not os.path.exists(full("LEDGER_CONSOLIDATED.md")):
        fail("LEDGER_CONSOLIDATED.md is not in this folder. Save the patch "
             "in the orrery repo's root folder.")
    texts, crlf = {}, []
    for path, _, _, _ in EDITS:
        if path not in texts:
            if not os.path.exists(full(path)):
                fail("%s not found." % path)
            raw = open(full(path), "rb").read()
            if b"\r\n" in raw:
                crlf.append(path)
            texts[path] = raw.replace(b"\r\n", b"\n")
    if b"<!-- L:414 status:DONE" in texts["LEDGER_CONSOLIDATED.md"]:
        print("already applied: L-414 is already closed. Nothing written.")
        return 0
    if os.path.exists(full(HANDOFF_PATH)):
        fail("%s already exists." % HANDOFF_PATH)
    page = "documentation/WHERE_WE_ARE.md"
    if texts[page].count(MARKER) != 1:
        fail("WHERE_WE_ARE.md: the run-record marker was not found once.")
    below = texts[page][texts[page].index(MARKER):]
    for path, label, old, new in EDITS:
        o, n = old.encode("ascii"), new.encode("ascii")
        count = texts[path].count(o)
        if count != 1:
            fail("ANCHOR FAIL %s -- %s: expected 1 match, found %d. Has "
                 "that part changed since 32619f8d?" % (path, label, count))
        texts[path] = texts[path].replace(o, n)
        print("ok  %-48s %s" % (path, label))
    if texts[page][texts[page].index(MARKER):] != below:
        fail("WHERE_WE_ARE.md: an edit reached below the run-record marker.")
    v387 = V387.encode("ascii")
    if (texts["PROJECT_INSTRUCTIONS.md"].count(v387) != 0 or
            texts["documentation/PROJECT_INSTRUCTIONS_HISTORY.md"].count(
                v387) != 1):
        fail("v3.87 did not move word for word.")
    print("ok  v3.87 moved to the history, word for word")
    o116 = OLD116.encode("ascii")
    if (texts["skills/ledger-and-session-records/SKILL.md"].count(o116)
            != 0 or texts["documentation/SKILL_HISTORIES.md"].count(o116)
            != 1):
        fail("the ledger skill's v1.16 entry did not move word for word.")
    print("ok  ledger-and-session-records v1.16 moved, word for word")
    for path, data in texts.items():
        bad = sum(1 for ch in data if ch > 127)
        if bad:
            fail("%s would hold %d non-ASCII byte(s)." % (path, bad))
    for path, data in texts.items():
        with open(full(path), "wb") as handle:
            handle.write(data)
    with open(full(HANDOFF_PATH), "wb") as handle:
        handle.write(HANDOFF.encode("ascii"))
    print("ok  %s created" % HANDOFF_PATH)
    for path in crlf:
        print("note: %s was CRLF in the working copy; written LF" % path)
    above = texts[page][:texts[page].index(MARKER)].count(b"\n")
    print("note: WHERE_WE_ARE.md has %d lines above the run-record marker "
          "(the cap is 130)" % above)
    print("stamps updated: the ledger header; both skills' version lines; "
          "PROJECT_INSTRUCTIONS.md header and anchor; the dashboard's "
          "docstring; WHERE_WE_ARE.md date line")
    print("patch applied: %d edits in %d files, and the build record."
          % (len(EDITS), len(texts)))
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py -- it writes both skills' "
          "manifest rows and the ledger skill's read plan, and rebuilds the "
          "ledger's index. Expect 21 of 21.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Upload the two skills' SKILL.md (Settings > Skills): "
          "ledger-and-session-records and horizons-orbital-mechanics; and "
          "replace the Project's instructions with PROJECT_INSTRUCTIONS.md "
          "(now v3.90).")
    print("  4. The Mode 5 look at Encke and Halley in the orrery window, "
          "when you like: four checks in the build record.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
