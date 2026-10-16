#!/usr/bin/env python3
"""
patch_L446_3_daily_run_orrery_20261015.py -- the orrery's half of
L-446 (the Daily Run pulls before it builds, with L-380 and L-388): the
dashboard's buttons, the ledger, Where We Are, gallery-cache-builder
1.10, protocol v3.99, and the build record.

Built on orrery 77245ea87179455bb4794ba7ed8712b98350fdb7 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
95713f4912d3e1863390a246d2ba8004bc7cf4c9 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L446_3_daily_run_orrery_20261015.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions. Run it
    AFTER patch_L446_2 (the website's): Dashboard Parity reads both
    folders and expects the website's new steps.

WHAT IT DOES, all or nothing, in eight files

    palomas_orrery_dashboard.py     Pulls From The Orrery in the Daily
                                    Run group; Pull Failures in the
                                    gallery checks; four scripts; short
                                    lines
    skills/gallery-cache-builder/SKILL.md      1.10: The Daily Run's
                                    Steps; its 1.8 entry moves to
    documentation/SKILL_HISTORIES.md
    PROJECT_INSTRUCTIONS.md         v3.99 entry, header, anchor; v3.96
                                    moves to
    documentation/PROJECT_INSTRUCTIONS_HISTORY.md
    LEDGER_CONSOLIDATED.md          L-446 ruling and build; L-380,
                                    L-388, L-423 notes; header stamp
    documentation/WHERE_WE_ARE.md   above the run-record marker only
    documentation/HANDOFF_L446_daily_run_order_build_20261015.md  NEW

    Code, skill, protocol and history files must be exactly the
    version this was built on (the protocol's generated Skill Manifest
    is not counted: orrery_maintenance_run.py rewrites it). The ledger
    and Where We Are are checked only at the lines edited, so your
    notes anywhere else are kept.

WHAT IT PRINTS

    Success: one "ok" line per file, then "patch applied" and what to
    do next. Failure: one ERROR or ANCHOR FAIL line and "NOTHING was
    written."

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Each file: how it is checked, and its edits as (old, new), bottom-up.
# "whole": the file (outside any generated zone) must be exactly the base.
# "anchors": checked only at the lines edited, so Tony's notes are kept.
# "new": a file this patch adds.
FILES = [
    {
        'path': 'palomas_orrery_dashboard.py',
        'mode': 'whole',
        'base_md5': 'e317f5041460aca28c3f53b0ea5afa19',
        'new_md5': 'ae56dbcae274468f0ebe26871f233775',
        'zone': None,
        'marker': None,
        'cap': None,
        "edits": [
            ('        "Checks the website\'s copy of Earth\'s tilt geometry against the orrery\'s.",\n    ("Gallery -- checks and data",\n',
             '        "Checks the website\'s copy of Earth\'s tilt geometry against the orrery\'s.",\n    ("Gallery -- checks and data",\n     "Pull Failures"):\n        "Proves each pull fails by name with no network, writing nothing.",\n    ("Gallery -- checks and data",\n'),
            ('        "Approve, decline or defer each new guest book message; write entries.",\n    ("Daily Run",\n',
             '        "Approve, decline or defer each new guest book message; write entries.",\n    ("Daily Run",\n     "Pulls From The Orrery"):\n        "Brings the orrery\'s exports in before the build; stops if one fails.",\n    ("Daily Run",\n'),
            ('     "Daily Run -- everything indented below"):\n        "The website\'s daily routine: guest book, JPL check, cache build, checks.",\n    ("Daily Run",\n',
             '     "Daily Run -- everything indented below"):\n        "The website\'s daily routine: guest book, pulls, cache build, checks.",\n    ("Daily Run",\n'),
            ('        "the gallery runner. Runs from the gallery repo ROOT.",\n        GALLERY_REPO_DIR,\n',
             '        "the gallery runner. Runs from the gallery repo ROOT.",\n        GALLERY_REPO_DIR,\n        True,\n        None,\n        True),\n        ("Pull Failures",\n        os.path.join("tools", "test_pull_failures.py"),\n        "Runs each of the three pulls in a throwaway copy with its "\n        "network replaced by one that fails three ways -- the orrery\'s "\n        "HEAD unreachable, its answer unreadable, the file missing at "\n        "HEAD. Each must exit 1, print FAIL naming the address, and leave "\n        "every file as it was; and the mirror after a failed pull must "\n        "not run (L-388, L-446). Plants three faults first, each caught. "\n        "Edits nothing in the repository. GATES the gallery runner.",\n        GALLERY_REPO_DIR,\n'),
            ('        "daily_run.py",\n        "daily_run.py --check: fails if any of the three scripts the "\n        "Daily Run calls is missing, say after a rename, and names it. "\n',
             '        "daily_run.py",\n        "daily_run.py --check: fails if any of the four scripts the "\n        "Daily Run calls is missing, say after a rename, and names it. "\n'),
            ('        "the mirror suite, the store writer and store editor suites, "\n        "the config mirror check, Horizons "\n        "confirmations, the pointer join, cache in step, drawn orbit, the drawings "\n',
             '        "the mirror suite, the store writer and store editor suites, "\n        "the config mirror check, pull failures, Horizons "\n        "confirmations, the pointer join, cache in step, drawn orbit, the drawings "\n'),
            ('         "gallery_maintenance_run.py",\n         "The Daily Run\'s third step: the same button as Gallery "\n         "Maintenance Run -- offline under Gallery -- checks and data, "\n',
             '         "gallery_maintenance_run.py",\n         "The Daily Run\'s fourth step: the same button as Gallery "\n         "Maintenance Run -- offline under Gallery -- checks and data, "\n'),
            ('         True,\n         None,\n         True),\n        ("Cache Builder",\n',
             '         True,\n         None,\n         True),\n        ("Pulls From The Orrery",\n         "gallery_maintenance_run.py",\n         "The Daily Run\'s second step (L-446): gallery_maintenance_run.py "\n         "--pull. Runs only the five pull-and-mirror rows -- Constants "\n         "Export Pull, Config Mirror, Objects Export Pull, Objects Mirror, "\n         "Drawings Pull -- before the Cache Builder, so the build reads "\n         "what the orrery exported today. Everything they bring was "\n         "already checked against JPL in the orrery\'s maintenance run. A "\n         "pull that cannot reach the orrery prints FAIL with the address "\n         "it tried and writes nothing, and the mirror after it does not "\n         "run (L-388). Ends on a line starting \\"=== PULLS:\\" that names "\n         "any row that failed; the Daily Run stops there when one did.",\n         GALLERY_REPO_DIR,\n         True,\n         ["--pull"],\n         True),\n        ("Cache Builder",\n'),
            ('         "offline, which the builder\'s own next steps ask for before a "\n         "commit. A step that reports a problem does not stop the next "\n         "one. It ends with one summary naming each step\'s result and "\n',
             '         "offline, which the builder\'s own next steps ask for before a "\n         "commit; its pull rows print \\"no change\\". Apart from the pulls, "\n         "a step that reports a problem does not stop the next "\n         "one. It ends with one summary naming each step\'s result and "\n'),
            ('         "Updater: approve or decline each new message, and write entries "\n         "or replies if you like. Then the Cache "\n         "Builder, with no OneDrive pause since 2026-10-10 (L-216: "\n',
             '         "Updater: approve or decline each new message, and write entries "\n         "or replies if you like. Then the Pulls From The Orrery: the "\n         "orrery\'s exports and drawings, at its HEAD, copied into the "\n         "website\'s config BEFORE the build, so the build uses what the "\n         "orrery exported today (L-446). If a pull cannot reach the "\n         "orrery, the Daily Run STOPS there and names it: nothing is built "\n         "on yesterday\'s export, and you run it again later (Tony\'s option "\n         "A, 2026-10-15). Then the Cache "\n         "Builder, with no OneDrive pause since 2026-10-10 (L-216: "\n'),
            ('line.\n"""\n',
             'line.\nOctober 15, 2026 with Anthropic\'s Claude Opus 5.5 (L-446, with L-380 and\nL-388): the Daily Run is four steps. Pulls From The Orrery, the website\'s\ngallery_maintenance_run.py --pull, joins the Daily Run group between the\nGuest Book Updater and the Cache Builder, named what the Daily Run prints;\nthe Daily Run button says the pulls run first and that a failed pull\nstops it before the builder (Tony\'s option A of 2026-10-15); Daily Run\nSteps says four scripts; the offline runner\'s Daily Run card says fourth\nstep. Pull Failures, the website\'s new checker, gets its button under the\ngallery checks, in alphabetical place. Each has its short line. Fixed in\npassing: the Daily Run\'s short line still named the JPL check, which left\nit on 2026-10-14.\n"""\n'),
        ],
    },
    {
        'path': 'skills/gallery-cache-builder/SKILL.md',
        'mode': 'whole',
        'base_md5': '711c6aab54866306e358eb57a9a6b3aa',
        'new_md5': '3809ad26a25d435359073ef584497eb7',
        'zone': None,
        'marker': None,
        'cap': None,
        "edits": [
            ("\n`daily_run.py`, Tony's design of 2026-09-27 (L-281), is three steps\nsince 2026-10-14: the guest book updater, this builder with no flags,\nand the gallery maintenance run offline. A step that reports a problem\ndoes not stop the next; nothing in it commits or pushes. The Horizons\ncheck was its step 2 from 2026-10-10 to 2026-10-14 and moved into the\n",
             '\n`daily_run.py`, Tony\'s design of 2026-09-27 (L-281), is FOUR steps\nsince 2026-10-15 (L-446), and the order is the point:\n\n  1. The guest book updater. First, because it needs Tony\'s answers,\n     and what he approves is saved at once.\n  2. The pulls from the orrery: `gallery_maintenance_run.py --pull`,\n     which runs only the five pull-and-mirror rows of its GENERATORS\n     (constants export, config mirror, objects export, objects mirror,\n     drawings). BEFORE the builder, so the build reads what the orrery\n     exported today and the served `frame_constants.orrery_sha` names\n     that export. Until 2026-10-15 the pulls ran only in step 4, after\n     the build, so every build read the previous run\'s pull and its\n     stamp was one step behind (L-380).\n  3. This builder, with no flags.\n  4. The gallery maintenance run, offline. Its pull rows run again and\n     print "no change", which is the proof step 2 did the work.\n\nThe pull list has ONE home, the maintenance run\'s GENERATORS; `--pull`\nreads it through `PULL_ROWS`. Do not add the pulls to `daily_run.py`\'s\nSTEPS as rows of their own: that is a second copy of the list, and five\nmore dashboard buttons for Dashboard Parity to hold.\n\nA PULL THAT CANNOT FETCH FAILS, AND THE DAILY RUN STOPS (Tony\'s option\nA, 2026-10-15). Each pull prints one line starting `FAIL:` naming what\nit could not fetch, from which address and why, writes nothing, and\nexits 1 (L-388; until 2026-10-15 it printed N-A and exited 0, the\nmaintenance run read that as PASS "no change", and the mirror wrote the\nconfig from the old export). The maintenance run does not run a mirror\nwhose pull failed (`FED_BY`): its row is red and names the pull. A\nfailed generator fails the whole run and is named in the summary. And\n`daily_run.py` stops after step 2: the builder and the checks do not\nrun, and the summary quotes `--pull`\'s "=== PULLS:" line. Nothing is\nbuilt on yesterday\'s export; Tony runs it again later. The builder\nneeds the network for Horizons anyway, so a day with no network builds\nnothing either way. Option B -- build on the previous pull and say so\nin red -- was declined. `tools/test_pull_failures.py` ("Pull failures",\ngating) runs each pull with its network replaced by one that fails,\nthree ways, so these branches are tested every day and not only on the\nday the network is down.\n\nApart from the pulls, a step that reports a problem does not stop the\nnext: the guest book\'s problems still do not stop the build. Nothing in\nthe Daily Run commits or pushes. The Horizons\ncheck was its step 2 from 2026-10-10 to 2026-10-14 and moved into the\n'),
            ('Older entries are in documentation/SKILL_HISTORIES.md, moved there\non 2026-10-05 (L-418) and 2026-10-14 (L-431).\n\n',
             'Older entries are in documentation/SKILL_HISTORIES.md, moved there\non 2026-10-05 (L-418), 2026-10-14 (L-431) and 2026-10-15 (L-446).\n\n'),
            ('Run\'s Steps). A config change\'s exceptions now name the period too.\nEarlier: 1.8 | 2026-10-10, with Anthropic\'s Claude Opus 5.5, at\npalomas_orrery @ a6678b0f and gallery @ cb9038cc. v1.8 (L-216) retires\nthe hand routine\'s OneDrive pause, on Tony\'s word of 2026-10-10: "you\ncan remove the pause check from the daily run. the retry is\nsufficient." A session following the old step would have told him to\npause. The skill also gets its read plan, at its next version as Tony\nruled on 2026-10-08 (L-418).\nEarlier: 1.7 | 2026-10-05, with Anthropic\'s Claude Opus 5.5, at\n',
             "Run's Steps). A config change's exceptions now name the period too.\nEarlier: 1.7 | 2026-10-05, with Anthropic's Claude Opus 5.5, at\n"),
            ("\nSkill version: 1.9 | 2026-10-14, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 5cd63cce and gallery @ 4b2b660a. v1.9 (L-431 build 3,\n",
             "\nSkill version: 1.10 | 2026-10-15, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 77245ea8 and gallery @ 95713f49. v1.10 (L-446, with\nL-380 and L-388) records the Daily Run's new order. It is four steps:\nthe pulls from the orrery now run BEFORE the builder, so one Daily Run\ncarries today's export into the build. A pull that cannot reach the\norrery fails by name, its mirror does not run, and the Daily Run stops\nbefore the builder: Tony's option A of 2026-10-15 (The Daily Run's\nSteps).\nEarlier: 1.9 | 2026-10-14, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 5cd63cce and gallery @ 4b2b660a. v1.9 (L-431 build 3,\n"),
            ('\nRead this file in 2 parts: lines 1-269, 270-507.\n\n',
             '\nRead this file in 2 parts: lines 1-271, 272-548.\n\n'),
            ('name: gallery-cache-builder\ndescription: Nightly data-serving pipeline for the Paloma\'s Orrery web gallery (Phase 1b, ledger L-098). Use for any task touching tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, inspect_staging.py, debug_encke_tp.py, gallery_cleanup.py, data/objects_config.json, the data/solar-system/ serving cache (coverage_index.json, feature_configs.json, positions/, raw/), atomic-swap / .prev / .staging_* / .quarantine_* semantics, Guard v2, dry-run / first-build / nightly modes, documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; for the rule that a config change is not deployed until the cache is rebuilt; and whenever a rename or a delete under data/ is refused with "Access is denied" (WinError 5), or the swap log data/cache_swap_log.jsonl is being read or written. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma\'s Orrery.\nfires_when: Nightly builder, atomic swap and its retry/roll-back/swap log, "Access is denied" under data/, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers\n---\n',
             'name: gallery-cache-builder\ndescription: Nightly data-serving pipeline for the Paloma\'s Orrery web gallery (Phase 1b, ledger L-098). Use for any task touching tools/gallery_cache_builder.py, tools/test_gallery_cache_builder_offline.py, inspect_staging.py, debug_encke_tp.py, gallery_cleanup.py, data/objects_config.json, the data/solar-system/ serving cache (coverage_index.json, feature_configs.json, positions/, raw/), atomic-swap / .prev / .staging_* / .quarantine_* semantics, Guard v2, dry-run / first-build / nightly modes, documentation/TESTING_PROTOCOL.md layers, or wiring interactive.html to the served data; for the rule that a config change is not deployed until the cache is rebuilt; and whenever a rename or a delete under data/ is refused with "Access is denied" (WinError 5), or the swap log data/cache_swap_log.jsonl is being read or written; and for daily_run.py\'s order and a failed pull. Do NOT use for the Studio/converter/viewer curation chain (that is gallery-pipeline) or for projects other than Paloma\'s Orrery.\nfires_when: Nightly builder, atomic swap and its retry/roll-back/swap log, "Access is denied" under data/, coverage_index, serving cache, objects_config, dry-run/first-build/nightly, builder testing layers, the Daily\n  Run\'s order and a failed pull\n---\n'),
        ],
    },
    {
        'path': 'documentation/SKILL_HISTORIES.md',
        'mode': 'whole',
        'base_md5': 'b986d177f1237b9ee0b55bf4c49d3d37',
        'new_md5': '64901290f3ee64cb8bdde1550f987f0a',
        'zone': None,
        'marker': None,
        'cap': None,
        "edits": [
            ('(Moved down 2026-10-14, when 1.9 made a fourth entry.)\n\n',
             '(Moved down 2026-10-14, when 1.9 made a fourth entry.)\nEarlier: 1.8 | 2026-10-10, with Anthropic\'s Claude Opus 5.5, at\npalomas_orrery @ a6678b0f and gallery @ cb9038cc. v1.8 (L-216) retires\nthe hand routine\'s OneDrive pause, on Tony\'s word of 2026-10-10: "you\ncan remove the pause check from the daily run. the retry is\nsufficient." A session following the old step would have told him to\npause. The skill also gets its read plan, at its next version as Tony\nruled on 2026-10-08 (L-418).\n(Moved down 2026-10-15, when 1.10 made a fourth entry.)\n\n'),
        ],
    },
    {
        'path': 'PROJECT_INSTRUCTIONS.md',
        'mode': 'whole',
        'base_md5': 'b9fc215e707c2bf152bc01f6356276d6',
        'new_md5': '04f6482cf22c706f29f337a237321d67',
        'zone': ['<!-- SKILL-MANIFEST:START', '<!-- SKILL-MANIFEST:END -->'],
        'marker': None,
        'cap': None,
        "edits": [
            ('\nv3.96 (October 14, 2026): No rule changed in this document. THREE\nskill bumps, one version each (L-431 build 3, with L-395\'s move):\nhorizons-orbital-mechanics 1.5 -> 1.6, gallery-cache-builder 1.8 ->\n1.9, interactive-exhibit 1.14 -> 1.15. THE WEBSITE PRINTS THE ORRERY\'S\nPERIOD, AND THE HORIZONS CHECK LIVES IN THE ORRERY.\n\nWHAT PROMPTED IT. Tony, 2026-10-13: "I\'ve gotten away from the gallery\nwork. What\'s our path back?" L-431\'s third build carries each body\'s\nperiod from the orrery\'s export to every room\'s hover, and draws an\norbit around its period\'s centre. He asked the same day whether the\nHorizons check\'s move (L-395) should ride the build -- yes -- so the\nperiod comparison was written once, where the check now lives.\n\nWHAT CHANGED. horizons-orbital-mechanics gains Where the Check Lives,\nand What It Compares: a generator row of the orrery\'s maintenance run,\nasking JPL only what is due, comparing each fetched period with JPL\'s\nPR within its own error, and re-reading the spacecraft data sheets on\nthe same 30-day cycle; its pinning line no longer puts the check in\nthe website\'s Daily Run. gallery-cache-builder gains The Builder Reads\nthe Period\'s Centre (the served "drawn_orbit" and check #D) and The\nDaily Run\'s Steps (three since the move). interactive-exhibit gains\ntwo provenance bullets: a body\'s period is the orrery\'s, printed as\nserved in one of three forms and read from the config, so it reaches a\nvisitor on the push; the orbit drawn around a period\'s centre is cache\ndata and needs the builder. Each skill\'s oldest entry moved to\ndocumentation/SKILL_HISTORIES.md, by the three-entry rule.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copies read\nhorizons-orbital-mechanics 1.6, gallery-cache-builder 1.9 and\ninteractive-exhibit 1.15 before work that fires them.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.93 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\nFunctional for Claude, readable for human, signal preserved.\n',
             '\nFunctional for Claude, readable for human, signal preserved.\n'),
            ('\nv3.98 (October 15, 2026): No rule changed in this document. ONE\n',
             '\nv3.99 (October 15, 2026): No rule changed in this document. ONE\nskill bump, one version (L-446, with L-380 and L-388):\ngallery-cache-builder 1.9 -> 1.10. THE WEBSITE\'S DAILY RUN PULLS\nBEFORE IT BUILDS.\n\nWHAT PROMPTED IT. Tony, 2026-10-15, after L-444\'s first live run:\n"Wait, shouldn\'t the horizons check come before the cache build?" The\ncheck already runs in the orrery, before the export; what came after\nthe build was the website\'s pull of that export, so each build read\nthe previous run\'s pull. Ruled the same day: the pulls run before the\nbuilder. At the build\'s start Tony chose option A for a pull that\ncannot reach the orrery: the Daily Run stops before the builder.\n\nWHAT CHANGED. gallery-cache-builder rewrites The Daily Run\'s Steps:\nfour steps, the pulls (gallery_maintenance_run.py --pull, reading the\none pull list in its GENERATORS) before the builder; a pull that\ncannot fetch fails by name and its mirror does not run; the Daily Run\nstops there; "Pull failures" tests those branches every run. Its\ndescription and trigger name the Daily Run\'s order. Its v1.8 entry\nmoved to documentation/SKILL_HISTORIES.md, by the three-entry rule.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\ngallery-cache-builder 1.10 before work that fires it. This session\nconfirmed its loaded copies read gallery-cache-builder 1.9,\nsafe-file-editing 1.13, agentic-pre-test 1.3 and\nledger-and-session-records 1.21, as the manifest expected. v3.98\'s\nobligation, horizons-orbital-mechanics 1.7, still travels: no work\nthis session fired that skill.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.96 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\nv3.98 (October 15, 2026): No rule changed in this document. ONE\n'),
            ('\nCut from ffd6c36a at https://github.com/tonylquintanilla/palomas_orrery\n(branch main). Gallery repo: tonyquintanilla/tonyquintanilla.github.io.\n',
             '\nCut from 77245ea8 at https://github.com/tonylquintanilla/palomas_orrery\n(branch main). Gallery repo: tonyquintanilla/tonyquintanilla.github.io.\n'),
            ('PROJECT INSTRUCTIONS\nTony Quintanilla, PE | Claude | v3.98 | October 15, 2026\n\n',
             'PROJECT INSTRUCTIONS\nTony Quintanilla, PE | Claude | v3.99 | October 15, 2026\n\n'),
        ],
    },
    {
        'path': 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md',
        'mode': 'whole',
        'base_md5': 'f2853cd1601d202e246236d1434e57c2',
        'new_md5': '6bd4fee7ba63718f75146a71f2fa36f7',
        'zone': None,
        'marker': None,
        'cap': None,
        "edits": [
            ('v3.98 made a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n',
             'v3.98 made a fourth entry.)\n\nv3.96 (October 14, 2026): No rule changed in this document. THREE\nskill bumps, one version each (L-431 build 3, with L-395\'s move):\nhorizons-orbital-mechanics 1.5 -> 1.6, gallery-cache-builder 1.8 ->\n1.9, interactive-exhibit 1.14 -> 1.15. THE WEBSITE PRINTS THE ORRERY\'S\nPERIOD, AND THE HORIZONS CHECK LIVES IN THE ORRERY.\n\nWHAT PROMPTED IT. Tony, 2026-10-13: "I\'ve gotten away from the gallery\nwork. What\'s our path back?" L-431\'s third build carries each body\'s\nperiod from the orrery\'s export to every room\'s hover, and draws an\norbit around its period\'s centre. He asked the same day whether the\nHorizons check\'s move (L-395) should ride the build -- yes -- so the\nperiod comparison was written once, where the check now lives.\n\nWHAT CHANGED. horizons-orbital-mechanics gains Where the Check Lives,\nand What It Compares: a generator row of the orrery\'s maintenance run,\nasking JPL only what is due, comparing each fetched period with JPL\'s\nPR within its own error, and re-reading the spacecraft data sheets on\nthe same 30-day cycle; its pinning line no longer puts the check in\nthe website\'s Daily Run. gallery-cache-builder gains The Builder Reads\nthe Period\'s Centre (the served "drawn_orbit" and check #D) and The\nDaily Run\'s Steps (three since the move). interactive-exhibit gains\ntwo provenance bullets: a body\'s period is the orrery\'s, printed as\nserved in one of three forms and read from the config, so it reaches a\nvisitor on the push; the orbit drawn around a period\'s centre is cache\ndata and needs the builder. Each skill\'s oldest entry moved to\ndocumentation/SKILL_HISTORIES.md, by the three-entry rule.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copies read\nhorizons-orbital-mechanics 1.6, gallery-cache-builder 1.9 and\ninteractive-exhibit 1.15 before work that fires them.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.93 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n(Moved down from the resident protocol on 2026-10-15 when\nv3.99 made a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n'),
        ],
    },
    {
        'path': 'LEDGER_CONSOLIDATED.md',
        'mode': 'anchors',
        'base_md5': 'a356a5f9261c5a3cd25b7e07b19366b2',
        'new_md5': 'dddb6e8ceae03a2f211ad5ee18052f56',
        'zone': None,
        'marker': None,
        'cap': None,
        "edits": [
            ('  `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.\n- **Found 2026-09-25** at gallery `ce09f789`. The routine builds the\n',
             "  `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.\n- **2026-10-15, built in L-446's build:** the pulls are the Daily Run's\n  step 2, before the builder, so the builder's stamp reads the\n  `data/constants_export.sha` the pull has just written. Read for loose\n  ends: none beyond the Gap. Closes with L-446, on Tony's run.\n- **Found 2026-09-25** at gallery `ce09f789`. The routine builds the\n"),
            ('  `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.\n- **Found 2026-09-28** building the L-345 gallery patch. In a sandbox\n',
             '  `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.\n- **2026-10-15, built in L-446\'s build:** each pull fails by name and\n  exits 1; a mirror after a failed pull does not run; a failed\n  generator fails the run. Shown failing with the network off: in the\n  build sandbox, which GitHub\'s API refuses, the Daily Run stopped\n  after the pulls and every file under `data/` was byte-identical; and\n  "Pull failures" now tests it on every run. Read for loose ends: none\n  beyond the Gap. Closes with L-446, on Tony\'s run.\n- **Found 2026-09-28** building the L-345 gallery patch. In a sandbox\n'),
            ("     Tony's ruling in the coordination session; its brief is written.\n     Done when L-446 closes.\n  3. L-357, stale leftovers: delete the unreferenced hover fixture\n",
             "     Tony's ruling in the coordination session; its brief is written.\n     Built 2026-10-15. Done when L-446 closes.\n  3. L-357, stale leftovers: delete the unreferenced hover fixture\n"),
            ("skills/gallery-cache-builder/SKILL.md, The Daily Run's Steps;\n`documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.\n\n",
             "skills/gallery-cache-builder/SKILL.md, The Daily Run's Steps;\n`documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`;\n`documentation/HANDOFF_L446_daily_run_order_build_20261015.md`.\n\n"),
            ('**Ref:** gallery `daily_run.py`, `gallery_maintenance_run.py`,\n`tools/pull_objects_export.py`, `tools/mirror_objects.py`,\n',
             '**Ref:** gallery `daily_run.py`, `gallery_maintenance_run.py`,\n`tools/test_pull_failures.py`,\n`tools/pull_objects_export.py`, `tools/mirror_objects.py`,\n'),
            ("  the previous pull and say so) and the planted faults.\n**Gap:** a small gallery build, its own session, from the brief: the\npulls and copies ahead of the builder; whether the maintenance run keeps its own pull\nrows (a no-op on a second run) or loses them; the Daily Run's dashboard\ngroup, which Dashboard Parity holds; and one Daily Run showing new\nperiods reaching the website and the orbits drawn around the barycentre\nin a single run.\n**Ref:** gallery `daily_run.py`, `gallery_maintenance_run.py`,\n",
             '  the previous pull and say so) and the planted faults.\n- **Ruled 2026-10-15, at the build session\'s start:** option A. When a\n  pull cannot reach the orrery, the Daily Run STOPS before the builder,\n  names the pull, and the summary says so; nothing is built on\n  yesterday\'s export. Option B (build on the previous pull, named in\n  red) declined. Tony\'s answer to the session\'s one question: "A: Stop\n  before the build (Recommended)". This changes the Daily Run\'s\n  standing rule that a step\'s problem does not stop the next, for the\n  pull step only.\n- **Built 2026-10-15** on orrery 77245ea8 and gallery 95713f49, two\n  patches: `patch_L446_2_daily_run_gallery_20261015.py` (gallery) and\n  `patch_L446_3_daily_run_orrery_20261015.py` (orrery). [verified in a\n  sandbox; Tony\'s run is the proof]\n  - `gallery_maintenance_run.py --pull` runs only the five\n    pull-and-mirror rows, read from GENERATORS through `PULL_ROWS`, so\n    the list keeps one home. `daily_run.py` is four steps: guest book,\n    the pulls, the builder, the offline run.\n  - The three pulls print `FAIL:` with the address they tried and exit\n    1 where they printed N-A and exited 0. A mirror whose pull failed\n    is not run (`FED_BY`) and its row is red, naming the pull.\n  - Beyond the brief, and the same class: a failed GENERATOR now fails\n    the offline run and is named in its summary. Generators were not\n    counted with the checkers, so a red pull row sat above a green "27\n    of 27 passed" and exit 0 -- L-388\'s shape one level up.\n  - New gating checker "Pull failures" (`tools/test_pull_failures.py`):\n    each pull with its network replaced by one that fails three ways,\n    and the run after a failed pull; three faults planted first. Run\n    against the ORIGINAL pulls it fails 9 of 13, so it can fail.\n  - Dashboard: Pulls From The Orrery in the Daily Run group, Pull\n    Failures in the gallery checks; Dashboard Parity 83 steps, PASS.\n  - Sandbox results, which could not reach GitHub\'s API (HTTP 403, a\n    real network-off case): the Daily Run stopped after the pulls, the\n    builder did not run, every file under `data/` byte-identical. With\n    only the HEAD answer stood in for, files fetched from GitHub: the\n    pulls wrote orrery 77245ea\'s SHA, the builder ran after them, the\n    second pass printed "no change" on all five rows, 28 of 28.\n- **Swept for items on the same files** (Cluster the Tail): none other\n  is a small fix on them; nothing carried.\n**Gap:** Tony\'s run: the gallery patch, ONE Daily Run (the pulls run\nfirst; the maintenance run\'s pull rows print "no change"; Cache in\nstep passes in the same run), commit, push, the live run (Export\nfreshness names today\'s orrery HEAD); then the orrery patch and\n`orrery_maintenance_run.py`. Then close this item, L-380 and L-388, and\nL-423\'s item 2, from his run record.\n**Ref:** gallery `daily_run.py`, `gallery_maintenance_run.py`,\n'),
            ('rides L-445; the two briefs written), built on b4105c0.\nReview and RICE update Tony 6-21-2026\n',
             "rides L-445; the two briefs written), built on b4105c0.\nModule updated: October 15, 2026 with Anthropic's Claude Opus 5.5\n(L-446 built: the Daily Run pulls before it builds and stops on a failed\npull, Tony's option A; L-380 and L-388 built with it; gallery-cache-builder\n1.10, protocol v3.99), built on 77245ea8 and gallery 95713f49.\nReview and RICE update Tony 6-21-2026\n"),
        ],
    },
    {
        'path': 'documentation/WHERE_WE_ARE.md',
        'mode': 'anchors',
        'base_md5': 'aff5a39fee7b2cd20986e5b63a130547',
        'new_md5': '7bce545fb7b6d243e69f0cc6d23445c3',
        'zone': None,
        'marker': '--- Your run record below this line',
        'cap': 130,
        "edits": [
            ('  build 1 `HANDOFF_L401_distance_build1_20261012.md`; build 3 parked: L-401.\n- Your notes of Oct 14: `WHERE_WE_ARE_10-14-26_2250_run_record.md`\n- L-421 (typed facts, inner Oort): `MANIFEST_L421_typed_facts_20261006.md`, `HANDOFF_L421_*`\n',
             '  build 1 `HANDOFF_L401_distance_build1_20261012.md`; build 3 parked: L-401.\n- Your notes of Oct 15: `WHERE_WE_ARE_10-15-26_2236_run_record.md`\n- L-421 (typed facts, inner Oort): `MANIFEST_L421_typed_facts_20261006.md`, `HANDOFF_L421_*`\n'),
            ('- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: `HANDOFF_L445_earth_period_brief_20261015.md` and\n  `HANDOFF_L446_daily_run_order_brief_20261015.md`, the two briefs*\n- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n',
             '- Every item: `LEDGER_CONSOLIDATED.md`.\n- *Next: `HANDOFF_L445_earth_period_brief_20261015.md`; the L-446\n  build: `HANDOFF_L446_daily_run_order_build_20261015.md`*\n- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n'),
            ('- Last cache build: 20261016T021807Z, ok, no retry (gallery 95713f4).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 45085c4).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n',
             '- Last cache build: 20261016T021807Z, ok, no retry (gallery 95713f4).\n- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 77245ea).\n  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n'),
            ('  it), then the objects; no batch of objects first. (Oct 15)\n\n',
             '  it), then the objects; no batch of objects first. (Oct 15)\n- A failed pull stops the Daily Run before the build: option A. (Oct 15)\n\n'),
            ("               not Earth's centre.*\n  8c.  [next]  L-446 (the Daily Run's order): the website pulls the\n               orrery's data before it builds; takes in L-380, L-388.\n  9.   [next]  The website's checks, in the order you confirmed:\n",
             "               not Earth's centre.*\n  8c.  [NOW]   *L-446 (the Daily Run's order): built; your one Daily Run\n               is the proof.*  << moved this session\n  9.   [next]  The website's checks, in the order you confirmed:\n"),
            ("               System room's features close with these rooms.\n  8.   [done]  The served objects are checked against JPL Horizons, from\n               the orrery's run; the periods passed live, Oct 14.\n  8a.  [done]  The run fetches each served body's missing period from\n               JPL: L-444 (the missing periods), all eight, Oct 15.\n  8b.  [next]  *L-445 (Earth's period): from the Earth-Moon barycentre,\n",
             "               System room's features close with these rooms.\n  8-8a.[done]  The served objects are checked against JPL from the\n               orrery's run, missing periods fetched first (Oct 14, 15).\n  8b.  [next]  *L-445 (Earth's period): from the Earth-Moon barycentre,\n"),
            ('> **Needs you now:**\n> - *Run patch_L446_1, then the maintenance run; commit; push.*\n\n',
             '> **Needs you now:**\n> - *Run patch_L446_2 (website), the Daily Run once, push; then patch_L446_3.*\n\n'),
            (">\n> **Do next:** *Start the L-445 (Earth's period) build session from\n> its brief; L-446 (the Daily Run's order) from its brief, either order.*\n>\n",
             ">\n> **Do next:** *After your Daily Run, start the L-445 (Earth's period)\n> build session from its brief.*\n>\n"),
            ("> **Changed since you last read this:**\n> - Briefs written for L-445 (Earth's period) and L-446 (the Daily\n>   Run's order); L-446 takes in L-380 and L-388 (the export pull).\n>\n",
             "> **Changed since you last read this:**\n> - L-446 (the Daily Run's order) built: the pulls now run before the\n>   cache build, and a pull that can't reach the orrery stops the run.\n>\n"),
            ('\nLast updated: October 15, 2026, late night: the two briefs written.\n- Written at orrery b4105c0 and gallery 95713f4.\n\n',
             "\nLast updated: October 15, 2026, late night: L-446 (the Daily Run's order) built.\n- Written at orrery 77245ea and gallery 95713f4.\n\n"),
        ],
    },
    {
        'path': 'documentation/HANDOFF_L446_daily_run_order_build_20261015.md',
        'mode': 'new',
        'new_md5': 'c9b3048de62360c4196d843ec7bff954',
        "content": '<!-- Doc-Kind: hand | Build record for L-446: the website\'s Daily Run pulls the orrery\'s exports before it builds the cache, and stops on a failed pull (Tony\'s option A). Takes in L-380 and L-388. Two patches, gallery and orrery. -->\n# Build record: the Daily Run pulls before it builds (L-446, with L-380 and L-388)\n\nBuilt on gallery 95713f4912d3e1863390a246d2ba8004bc7cf4c9 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily\nrun again") and orrery 77245ea87179455bb4794ba7ed8712b98350fdb7 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L445 L446 rulings\nand briefs"; no code moved since the brief\'s b4105c0).\nPushed at: (Tony\'s push; the next session reads it from git).\nTony\'s local folders: orrery\n`C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\`;\ngallery `C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\`.\nWritten October 15, 2026 with Anthropic\'s Claude Opus 5.5.\n\n- Type: BUILD. Two patches: the website\'s (the work) and the orrery\'s\n  (the dashboard, the ledger, Where We Are, the skill, the protocol).\n- From: `documentation/HANDOFF_L446_daily_run_order_brief_20261015.md`.\n- Ledger: L-446, with L-380 and L-388; L-423\'s item 2. All stay OPEN\n  until Tony\'s run; the session that reads his run record closes them.\n\n## 1. The one decision\n\nTony chose option A at the session\'s start: "A: Stop before the build\n(Recommended)". When a pull cannot reach the orrery, the Daily Run stops\nbefore the cache builder and names the pull. Nothing is built on\nyesterday\'s export.\n\n## 2. What was built\n\nThe website (patch_L446_2_daily_run_gallery_20261015.py):\n\n- `daily_run.py` is four steps: the guest book, the pulls from the\n  orrery, the cache builder, the offline maintenance run. If the pulls\n  fail it stops and its summary quotes the line naming which failed.\n- `gallery_maintenance_run.py --pull` runs only the five\n  pull-and-mirror rows. It reads them from GENERATORS, so the list\n  still has one home. Its last line starts "=== PULLS:".\n- The three pulls (`tools/pull_constants_export.py`,\n  `tools/pull_objects_export.py`, `tools/pull_drawings.py`) print a\n  line starting "FAIL:" with the address they tried, and exit 1, where\n  they printed N-A and exited 0.\n- A mirror whose pull failed is not run; its row is red and names the\n  pull.\n- A failed generator now fails the offline run and is named in the\n  summary. This goes one step past the brief. Before, generator rows\n  were not counted, so a red pull sat above "27 of 27 passed" and the\n  run exited 0. That is the same failure L-388 names, one level up.\n- New gating checker "Pull failures", `tools/test_pull_failures.py`.\n\nThe orrery (patch_L446_3_daily_run_orrery_20261015.py):\n\n- Dashboard: Pulls From The Orrery in the Daily Run group; Pull\n  Failures in the gallery checks; Daily Run Steps says four scripts;\n  the Daily Run\'s short line no longer names the JPL check.\n- gallery-cache-builder 1.10: The Daily Run\'s Steps rewritten; its\n  description names the Daily Run. Its 1.8 entry moved to\n  `documentation/SKILL_HISTORIES.md`.\n- Protocol v3.99, with v3.96 moved to\n  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`.\n- The ledger: the ruling and the build on L-446; notes on L-380, L-388\n  and L-423\'s item 2.\n- Where We Are: the box, road stage 8c, one Settled line, the\n  pointers. Nothing below the run-record marker is touched.\n- This record.\n\n## 3. What was tested, in a sandbox\n\nThe sandbox cannot reach GitHub\'s API (it answers HTTP 403). That made\nthe network-off case real rather than staged.\n\n- Network off. The Daily Run stopped after the pulls. The builder did\n  not run. Every file under `data/` was byte-identical before and\n  after. All five pull rows were red, each naming the address or the\n  pull it waited on.\n- Network on. Only the API\'s one answer, the orrery\'s HEAD SHA, was\n  stood in for; the files themselves were fetched from GitHub. The\n  pulls wrote orrery 77245ea\'s SHA; the builder (a stand-in) ran after\n  them; the maintenance run\'s pull rows all printed "no change"; 28 of\n  28 gating checkers passed (27 at the base, plus Pull failures).\n- `daily_run.py --check` with the builder renamed away: "1 of 4 step\n  scripts MISSING", exit 1.\n- Pull failures against the ORIGINAL pulls: 9 of 13 FAILED. So the\n  check can fail.\n- Dashboard Parity: PASS, 83 steps. Against today\'s dashboard it\n  names the two new steps with no button.\n- The dashboard opened headlessly ("Dashboard ready").\n- `skills_index.py --check`: no problems, once the skill\'s description\n  was cut back under Anthropic\'s 1024-character limit; the check\n  caught it at 1044.\n\nThe real cache builder was not run in the sandbox: it needs JPL. Your\nDaily Run is its test.\n\n## 4. The proof on Tony\'s machine\n\n- Run the gallery patch, then the Daily Run once.\n- Watch for: step 2 "Pulls from the orrery" runs before the builder;\n  "=== PULLS: all 5 passed"; in step 4, the five pull rows print "no\n  change"; Cache in step passes in the same run.\n- L-445 (Earth\'s period) is not pushed yet, so this run carries no new\n  period. That makes it the case where the pulls should change only\n  the three SHA files, from 45085c4 to today\'s orrery HEAD.\n- Commit, push, then the live run: Export freshness should name\n  today\'s orrery HEAD.\n- Then the orrery patch and `orrery_maintenance_run.py` (Dashboard\n  parity, the ledger index, the skill manifest), commit, push.\n\n## 5. Loose ends\n\n- L-380 and L-388, read for anything the build does not cover: nothing.\n- Ledger sweep for other open items on these files: none small enough\n  to carry.\n- The obligation: the next session confirms its loaded copy of\n  gallery-cache-builder reads 1.10. v3.98\'s horizons-orbital-mechanics\n  1.7 obligation also still travels.\n\n## 6. Tony\'s actions, all of them\n\n- (do) Save `patch_L446_2_daily_run_gallery_20261015.py` in the\n  website folder and run it.\n- (do) Run the Daily Run once; commit; push; run the live maintenance\n  run.\n- (do) Save `patch_L446_3_daily_run_orrery_20261015.py` in the orrery\n  folder and run it; run `orrery_maintenance_run.py`; commit; push.\n- (do) Move each spent patch into its repository\'s documentation/.\n- (do) Reinstall gallery-cache-builder (1.10) in Settings > Skills;\n  save PROJECT_INSTRUCTIONS.md as\n  `documentation/project_instructions_v3_99.md` and copy it into the\n  Project instructions.\n\nRecord written October 2026 with Anthropic\'s Claude Opus 5.5.\n',
    },
]



def md5(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def outside(text, zone):
    if not zone:
        return text
    i = text.index(zone[0])
    j = text.index(zone[1]) + len(zone[1])
    return text[:i] + text[j:]


def fail(message):
    print(message)
    print("NOTHING was written. Undo is not needed.")
    return 1


def main():
    planned = []
    notes = []
    for f in FILES:
        rel = f["path"]
        path = os.path.join(HERE, *rel.split("/"))
        if f["mode"] == "new":
            if os.path.exists(path):
                with open(path, "rb") as handle:
                    have = handle.read().decode("utf-8").replace("\r\n", "\n")
                if md5(have) == f["new_md5"]:
                    print("ok  %-58s already present, the same" % rel)
                    continue
                return fail("ERROR: %s already exists and differs from what "
                            "this patch adds." % rel)
            planned.append((rel, path, f["content"]))
            print("ok  %-58s new file" % rel)
            continue
        if not os.path.exists(path):
            return fail("ERROR: %s is not here. Save this patch in the "
                        "repository's root folder." % rel)
        with open(path, "rb") as handle:
            raw = handle.read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            return fail("ERROR: %s is not UTF-8." % rel)
        if "\r\n" in text:
            text = text.replace("\r\n", "\n")
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
        if f["mode"] == "whole":
            have = md5(outside(text, f.get("zone")))
            if have == f["new_md5"]:
                return fail("ERROR: %s already carries this patch's change. "
                            "It has run before." % rel)
            if have != f["base_md5"]:
                return fail("ERROR: %s is not the version this patch was "
                            "built on (base moved). Compare it with the "
                            "repository in GitHub Desktop." % rel)
        for n, (old, new) in enumerate(f["edits"], 1):
            count = text.count(old)
            if count != 1:
                first = old.strip().splitlines()[0][:60] if old.strip() else ""
                return fail("ANCHOR FAIL: %s edit %d matched %d times: %r"
                            % (rel, n, count, first))
            if f.get("marker") and text.index(old) > text.index(f["marker"]):
                return fail("ANCHOR FAIL: %s edit %d is below the run-record "
                            "marker; no patch edits there." % (rel, n))
            text = text.replace(old, new)
        if f.get("cap"):
            above = text[:text.index(f["marker"])].count("\n")
            if above > f["cap"]:
                return fail("ERROR: %s would have %d lines above the marker; "
                            "the cap is %d." % (rel, above, f["cap"]))
        if any(ord(c) > 127 for c in text):
            notes.append("note: %s still holds non-ASCII bytes this patch "
                         "did not reach" % rel)
        planned.append((rel, path, text))
        print("ok  %-58s %d edit(s)" % (rel, len(f["edits"])))

    for rel, path, text in planned:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
    for note in notes:
        print(note)
    print("patch applied (%d file(s) written)" % len(planned))
    gallery_test = os.path.join(os.path.dirname(HERE), 'tonyquintanilla.github.io', 'tools', 'test_pull_failures.py')
    if not os.path.exists(gallery_test):
        print('note: the website folder beside this one has no tools/test_pull_failures.py yet.')
        print('      Run patch_L446_2 there first, or Dashboard Parity will report two steps with no button.')
    print('')
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py: it rebuilds the ledger index and')
    print('     the skill manifest (gallery-cache-builder 1.10); Dashboard parity')
    print('     should pass with 83 steps.')
    print('  2. GitHub Desktop: commit and push.')
    print('  3. Reinstall gallery-cache-builder (1.10) in Settings > Skills; save')
    print('     PROJECT_INSTRUCTIONS.md as documentation/project_instructions_v3_99.md')
    print('     and copy it into the Project instructions.')
    return 0


if __name__ == "__main__":
    sys.exit(main())
