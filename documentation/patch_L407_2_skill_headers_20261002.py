#!/usr/bin/env python3
"""
patch_L407_2_skill_headers_20261002.py -- ORRERY repo. A skill's header
is read as YAML, the way Settings reads it, and the two headers that
still fail are fixed.

REPLACES patch_L407_1_skill_headers_20261002.py. That one was built on
orrery 94ff6c68; patch_L406_3 then ran and moved two of the files it
checks, so it refused to run, correctly, writing nothing. This is the
same work rebuilt on today's HEAD. Delete patch_L407_1 if a copy is in
the repo root.

Built on orrery 0a5eea0b0112640c6beea79a580f57184c9e59dd
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 6ba42f024a44c544e4fb7b6d880c485a267f40f2
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
not touched).

WHY. Settings refused interactive-exhibit 1.10 with "malformed YAML
frontmatter". A skill file opens with a short header between two ---
lines, written in YAML. skills_index.py read the same header by looser
rules of its own and built the manifest anyway, and as a generator its
exit code did not count, so the maintenance run passed 19 of 19.
patch_L406_3 fixed that one header. Tony, 2026-10-02: do L-407 now.

WHAT CHANGES
    skills_index.py   reads every header as YAML -- PyYAML where it is
        installed, built-in rules otherwise, and it prints which -- and
        reports a problem, naming the skill, for a header YAML refuses,
        one with no name or description as text, or a value YAML
        silently cuts short at " #" (a comment).
    orrery_maintenance_run.py   runs it with --check as a checker,
        "Skill headers", so a bad header fails the run: 20 gating
        checkers where there were 19.
    skills/earth-system-pipeline/SKILL.md   1.1 -> 1.2: its description
        held ": ", which YAML refuses, so a reinstall would have failed.
        Now quoted. No rule changed.
    skills/provenance-discipline/SKILL.md   2.24 -> 2.25: its
        description held "# Source:", so YAML read only its first 200
        characters, ending "adding or reviewing". The installed skill has
        been chosen by that cut description. Now quoted. No rule changed.
    PROJECT_INSTRUCTIONS.md   v3.79; v3.76 moves to
        documentation/PROJECT_INSTRUCTIONS_HISTORY.md.
    LEDGER_CONSOLIDATED.md   L-407 records the build; L-406 records
        patch 3 and the gallery push, and what is left (the reinstall
        and the Mode 5 look).

CHECKED HERE: the new check run both ways (PyYAML, and with PyYAML
hidden) fails on the two unfixed headers and passes on the fixed ones;
the orrery suite passes, the one Linux-only failure aside (the Windows
colour name in Reset completeness).

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L407_2_skill_headers_20261002.py

PERMANENT, though this script is thrown away: the header check and its
checker row; the two repaired headers.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 2, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

BASE = {'LEDGER_CONSOLIDATED.md': '6e295e5bcd3b44c832e94ad8bf4abab0',
 'PROJECT_INSTRUCTIONS.md': '48444279a6b836da8445d3084b1241ed',
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': '265ebfd34b9cd20b0b2ac9759d9efde7',
 'orrery_maintenance_run.py': 'bb8e540a48bc385b993b0b20beffc58c',
 'skills/earth-system-pipeline/SKILL.md': '66d6d00ba36a9314d479126fdea4b02e',
 'skills/provenance-discipline/SKILL.md': 'af6841936bdcb3bc70befc25e00d1092',
 'skills_index.py': 'e73b13407f4a7bcb03b082e40ad93271'}

EDITS = {'LEDGER_CONSOLIDATED.md': [('L-407 built',
                             "#### [L-407] A skill's header is not checked "
                             'as YAML (orrery, skills)\n'
                             '<!-- L:407 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->\n'
                             '- **Found 2026-10-02** when Settings refused '
                             'interactive-exhibit 1.10\n'
                             '  with "malformed YAML frontmatter" (L-406). '
                             '`skills_index.py` reads\n'
                             "  each skill's header to build the manifest, "
                             'and read the broken one\n'
                             '  without complaint, so the maintenance run '
                             'passed a skill that could\n'
                             '  not be installed: a check that cannot fail '
                             'on the one fault the\n'
                             '  install step enforces.\n'
                             '- **The same check finds a second, older '
                             'case:**\n'
                             '  `skills/earth-system-pipeline/SKILL.md` has '
                             '": " inside its\n'
                             '  description ("displacement): the restraint '
                             'discipline"), which strict\n'
                             '  YAML refuses. Its installed copy matches the '
                             'repo, so Settings\n'
                             '  accepted it once, under whatever parser it '
                             'had then. It loads today;\n'
                             '  a reinstall may fail. Left as it is, since '
                             'changing it means a\n'
                             '  reinstall of a skill nothing else is '
                             'touching.\n'
                             '**Gap:** Make `skills_index.py` parse each '
                             'header as YAML and fail the\n'
                             'run, naming the skill, when one does not parse '
                             'or lacks name and\n'
                             "description; fix earth-system-pipeline's "
                             'description in the same patch\n'
                             "(quote it), with Tony's reinstall.\n"
                             '**Ref:** L-406; `skills_index.py`; '
                             '`skills/*/SKILL.md`.\n'
                             '\n',
                             "#### [L-407] A skill's header is checked as "
                             'YAML (orrery, skills)\n'
                             '<!-- L:407 status:OPEN upd:2026-10-02 '
                             'section:A flag: rice: -->\n'
                             '- **Found 2026-10-02** when Settings refused '
                             'interactive-exhibit 1.10\n'
                             '  with "malformed YAML frontmatter" (L-406). '
                             '`skills_index.py` read each\n'
                             '  header by its own looser rules and built the '
                             'manifest from the broken\n'
                             '  one without complaint; as a generator its '
                             'exit code did not count. A\n'
                             '  check that could not fail on the one fault '
                             'the install step enforces.\n'
                             '- **Tony\'s word, 2026-10-02:** "while we are '
                             "doing this, let's do L407\n"
                             '  too."\n'
                             '- **Built the same day,** '
                             '`patch_L407_2_skill_headers_20261002.py`\n'
                             '  (patch_L407_1, built on 94ff6c68, refused to '
                             'run once patch_L406_3\n'
                             '  had moved the ledger; this one is the same '
                             'work on 0a5eea0b):\n'
                             '  `skills_index.py` reads every header as YAML '
                             '-- PyYAML where it is\n'
                             '  installed, built-in rules otherwise, and it '
                             'prints which -- and fails,\n'
                             '  naming the skill, on a header YAML refuses, '
                             'one with no name or\n'
                             '  description as text, or a value YAML '
                             'silently cuts short at " #".\n'
                             '  `orrery_maintenance_run.py` runs it with '
                             '`--check` as the checker\n'
                             '  Skill headers. Shown failing on the three '
                             'old headers both ways.\n'
                             '- **Two more found by the check, fixed in the '
                             'same patch and\n'
                             "  reported:** earth-system-pipeline's "
                             'description held ": "\n'
                             '  ("displacement): the restraint discipline"), '
                             'which YAML refuses, so\n'
                             '  a reinstall would have failed; '
                             'provenance-discipline\'s held "# Source:\n'
                             '  citations", so YAML read only its first 200 '
                             'characters, ending\n'
                             '  "adding or reviewing" -- the installed skill '
                             'has been chosen by that\n'
                             '  cut description, without the words about '
                             'citations, display strings\n'
                             '  and the push gate. Both descriptions are '
                             'quoted; versions 1.2 and\n'
                             "  2.25, no rule changed. interactive-exhibit's "
                             'header was put back on\n'
                             '  one line by patch_L406_3 (pushed at '
                             '81e19ef), still 1.10.\n'
                             '**Gap:** Tony reinstalls interactive-exhibit, '
                             'earth-system-pipeline and\n'
                             'provenance-discipline and replaces the '
                             "Project's instructions with\n"
                             'v3.79. The next session confirms its loaded '
                             'copies read 1.10, 1.2 and\n'
                             "2.25, and that provenance-discipline's "
                             'description runs past "adding\n'
                             'or reviewing", then closes this item.\n'
                             '**Ref:** L-406; `skills_index.py`; '
                             '`orrery_maintenance_run.py`;\n'
                             '`skills/*/SKILL.md`.\n'
                             '\n'),
                            ('L-406 where it stands',
                             "  skill's header as YAML. The version stays "
                             '1.10, since 1.10 never\n'
                             '  loaded anywhere.\n'
                             '**Gap:** Tony: run patch 3, run '
                             '`orrery_maintenance_run.py`, commit and\n'
                             'push the orrery, and reinstall '
                             'interactive-exhibit 1.10; then patch 2, the '
                             'cache builder, and\n'
                             '`gallery_maintenance_run.py`, commit and push '
                             'the gallery; then look at\n'
                             'the tide on the phone (Mode 5). The next '
                             'session confirms its loaded\n'
                             'interactive-exhibit reads 1.10.\n',
                             "  skill's header as YAML. The version stays "
                             '1.10, since 1.10 never\n'
                             '  loaded anywhere.\n'
                             '- **Patch 3 pushed at orrery 81e19ef; gallery '
                             'patch_L406_2 and the\n'
                             '  cache rebuild pushed at gallery 6ba42f02.**\n'
                             '**Gap:** Tony: reinstall interactive-exhibit '
                             '1.10, and look at the tide\n'
                             'on the phone and in the orrery (Mode 5). The '
                             'next session confirms its\n'
                             'loaded interactive-exhibit reads 1.10.\n')],
 'PROJECT_INSTRUCTIONS.md': [('header v3.79',
                              'Tony Quintanilla, PE | Claude | v3.78 | '
                              'October 2, 2026\n'
                              '\n'
                              'Cut from 5e42b00b at',
                              'Tony Quintanilla, PE | Claude | v3.79 | '
                              'October 2, 2026\n'
                              '\n'
                              'Cut from 0a5eea0b at'),
                             ('v3.79 entry',
                              'that file. An entry lives in exactly one '
                              'place, never both.\n'
                              '\n'
                              'v3.78 (October 2, 2026):',
                              'that file. An entry lives in exactly one '
                              'place, never both.\n'
                              '\n'
                              'v3.79 (October 2, 2026): No rule changed in '
                              'this document. TWO\n'
                              'skill bumps, one version each (L-407): '
                              'earth-system-pipeline 1.1 ->\n'
                              '1.2 and provenance-discipline 2.24 -> 2.25. A '
                              "SKILL'S HEADER IS READ\n"
                              'AS YAML.\n'
                              '\n'
                              'WHAT PROMPTED IT. Settings refused '
                              'interactive-exhibit 1.10 with\n'
                              '"malformed YAML frontmatter": patch_L406_1 '
                              'had put new fires_when words\n'
                              'on a line of their own; patch_L406_3, pushed '
                              'at 81e19ef, put them back\n'
                              'on one line, still 1.10. skills_index.py had '
                              'read the same header by its\n'
                              'own looser rules and built the manifest '
                              'without complaint, and as a\n'
                              'generator its exit code did not count, so the '
                              'maintenance run passed 19\n'
                              'of 19 on a skill that could not be installed. '
                              "Tony's word, 2026-10-02:\n"
                              'do L-407 now.\n'
                              '\n'
                              'WHAT CHANGED. skills_index.py reads every '
                              'header as YAML, with PyYAML\n'
                              'where installed and built-in rules otherwise, '
                              'names which, and fails on\n'
                              'a header YAML refuses, one with no name or '
                              'description as text, or a\n'
                              'value YAML silently cuts short at " #". '
                              'orrery_maintenance_run.py runs\n'
                              'it with --check as the checker Skill headers. '
                              'The check found two more:\n'
                              'earth-system-pipeline\'s description held ": '
                              '", which YAML refuses; and\n'
                              'provenance-discipline\'s held "# Source:", so '
                              'YAML read only its first\n'
                              '200 characters, and the installed skill has '
                              'been chosen by that cut\n'
                              'description. Both descriptions are now '
                              'quoted. No rule in any skill\n'
                              'changed.\n'
                              '\n'
                              'THE OBLIGATION TRAVELS. This session loaded '
                              'interactive-exhibit 1.9,\n'
                              'earth-system-pipeline 1.1 and '
                              'provenance-discipline 2.24. The next\n'
                              'session confirms its loaded copies read 1.10, '
                              '1.2 and 2.25, and that\n'
                              "provenance-discipline's description no longer "
                              'ends at "adding or\n'
                              'reviewing".\n'
                              '\n'
                              'The header stamp and the SHA anchor move with '
                              'this entry.\n'
                              '\n'
                              'Version history: v3.76 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                              'PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'v3.78 (October 2, 2026):'),
                             ('v3.76 leaves the resident three',
                              'v3.76 (October 1, 2026): No rule changed in '
                              'this document. TWO\n'
                              'skill bumps, one version each, for one build '
                              '(L-395):\n'
                              'provenance-discipline 2.23 -> 2.24 and '
                              'interactive-exhibit 1.7 -> 1.8.\n'
                              "THE ORRERY'S OBJECT LIST FEEDS THE WEBSITE.\n"
                              '\n'
                              "WHAT PROMPTED IT. The Solar System room's "
                              'info panel had no description\n'
                              "and no NASA link, and the website's object "
                              'facts were typed by hand\n'
                              "from the orrery's list. Tony's rulings of "
                              '2026-10-01: the website keeps\n'
                              'copies written by a tool and checked (the '
                              'constants pattern); each\n'
                              "served entry gains a 'key' spelled as the "
                              "website's slug; one\n"
                              'description and one link per object, cleaned '
                              'in the orrery; and\n'
                              '"simple errors such as the Apophis naming '
                              'discrepancy should be fixed\n'
                              'and reported."\n'
                              '\n'
                              'WHAT THE SKILLS NOW SAY. '
                              'provenance-discipline gains A Simple Error a\n'
                              'Check Finds Is Fixed and Reported: what '
                              'counts as simple, that the fix\n'
                              'rides the same patch and is named, what comes '
                              'to Tony instead, how a\n'
                              'number in a served description is sourced or '
                              'removed, and how this\n'
                              'sits beside The Braid. interactive-exhibit '
                              "records that a body's name,\n"
                              'Horizons id, description and link on the '
                              'website are copies written by\n'
                              "tools/mirror_objects.py, and what the room's "
                              'panel shows.\n'
                              '\n'
                              'THE BUILD. Orrery patch_L395_1 adds the key, '
                              'export_objects.py and its\n'
                              'check; gallery patch_L395_2 adds the pull, '
                              'the mirror and its suite,\n'
                              "and the panel's words and link.\n"
                              '\n'
                              'THE OBLIGATION TRAVELS. This session loaded '
                              '2.23 and 1.7. The next\n'
                              'session confirms its loaded copies read '
                              'provenance-discipline 2.24 and\n'
                              'interactive-exhibit 1.8 before any provenance '
                              'or exhibit work.\n'
                              '\n'
                              'The header stamp and the SHA anchor move with '
                              'this entry.\n'
                              '\n'
                              'Version history: v3.73 moves down to\n'
                              'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                              'PART 1 to keep three\n'
                              'resident.\n'
                              '\n'
                              'Functional for Claude, readable for human, '
                              'signal preserved.',
                              'Functional for Claude, readable for human, '
                              'signal preserved.')],
 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': [('v3.76 arrives',
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-02 when\n'
                                                    'v3.78 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS '
                                                    'REMOVED',
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-02 when\n'
                                                    'v3.78 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    'v3.76 (October 1, '
                                                    '2026): No rule changed '
                                                    'in this document. TWO\n'
                                                    'skill bumps, one '
                                                    'version each, for one '
                                                    'build (L-395):\n'
                                                    'provenance-discipline '
                                                    '2.23 -> 2.24 and '
                                                    'interactive-exhibit 1.7 '
                                                    '-> 1.8.\n'
                                                    "THE ORRERY'S OBJECT "
                                                    'LIST FEEDS THE '
                                                    'WEBSITE.\n'
                                                    '\n'
                                                    'WHAT PROMPTED IT. The '
                                                    "Solar System room's "
                                                    'info panel had no '
                                                    'description\n'
                                                    'and no NASA link, and '
                                                    "the website's object "
                                                    'facts were typed by '
                                                    'hand\n'
                                                    "from the orrery's list. "
                                                    "Tony's rulings of "
                                                    '2026-10-01: the website '
                                                    'keeps\n'
                                                    'copies written by a '
                                                    'tool and checked (the '
                                                    'constants pattern); '
                                                    'each\n'
                                                    'served entry gains a '
                                                    "'key' spelled as the "
                                                    "website's slug; one\n"
                                                    'description and one '
                                                    'link per object, '
                                                    'cleaned in the orrery; '
                                                    'and\n'
                                                    '"simple errors such as '
                                                    'the Apophis naming '
                                                    'discrepancy should be '
                                                    'fixed\n'
                                                    'and reported."\n'
                                                    '\n'
                                                    'WHAT THE SKILLS NOW '
                                                    'SAY. '
                                                    'provenance-discipline '
                                                    'gains A Simple Error a\n'
                                                    'Check Finds Is Fixed '
                                                    'and Reported: what '
                                                    'counts as simple, that '
                                                    'the fix\n'
                                                    'rides the same patch '
                                                    'and is named, what '
                                                    'comes to Tony instead, '
                                                    'how a\n'
                                                    'number in a served '
                                                    'description is sourced '
                                                    'or removed, and how '
                                                    'this\n'
                                                    'sits beside The Braid. '
                                                    'interactive-exhibit '
                                                    "records that a body's "
                                                    'name,\n'
                                                    'Horizons id, '
                                                    'description and link on '
                                                    'the website are copies '
                                                    'written by\n'
                                                    'tools/mirror_objects.py, '
                                                    "and what the room's "
                                                    'panel shows.\n'
                                                    '\n'
                                                    'THE BUILD. Orrery '
                                                    'patch_L395_1 adds the '
                                                    'key, export_objects.py '
                                                    'and its\n'
                                                    'check; gallery '
                                                    'patch_L395_2 adds the '
                                                    'pull, the mirror and '
                                                    'its suite,\n'
                                                    "and the panel's words "
                                                    'and link.\n'
                                                    '\n'
                                                    'THE OBLIGATION TRAVELS. '
                                                    'This session loaded '
                                                    '2.23 and 1.7. The next\n'
                                                    'session confirms its '
                                                    'loaded copies read '
                                                    'provenance-discipline '
                                                    '2.24 and\n'
                                                    'interactive-exhibit 1.8 '
                                                    'before any provenance '
                                                    'or exhibit work.\n'
                                                    '\n'
                                                    'The header stamp and '
                                                    'the SHA anchor move '
                                                    'with this entry.\n'
                                                    '\n'
                                                    'Version history: v3.73 '
                                                    'moves down to\n'
                                                    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md '
                                                    'PART 1 to keep three\n'
                                                    'resident.\n'
                                                    '\n'
                                                    '(Moved down from the '
                                                    'resident protocol on '
                                                    '2026-10-02 when\n'
                                                    'v3.79 made a fourth '
                                                    'entry.)\n'
                                                    '\n'
                                                    '================================================================\n'
                                                    'PART 2 -- LESSONS '
                                                    'REMOVED')],
 'orrery_maintenance_run.py': [('checker: Skill headers',
                                "    ('Exact rows by the count', "
                                "['exact_rows_report.py', '--check'],\n",
                                "    # L-407 (2026-10-02): every skill's "
                                'header read as YAML, the way the\n'
                                '    # Settings uploader reads it, plus the '
                                "tool's own consistency checks.\n"
                                '    # The same script as the Skill manifest '
                                'generator, run with --check\n'
                                '    # so its failure fails this run; as a '
                                'generator its exit code would\n'
                                '    # not count, which is how a header '
                                'Settings refused passed 19 of 19.\n'
                                "    ('Skill headers', ['skills_index.py', "
                                "'--check'], 'OK:'),\n"
                                "    ('Exact rows by the count', "
                                "['exact_rows_report.py', '--check'],\n")],
 'skills/earth-system-pipeline/SKILL.md': [('description quoted',
                                            'description: Earth System KMZ '
                                            'and climate visualization '
                                            "pipeline for the Paloma's "
                                            'Orrery project. Use for any '
                                            'task touching '
                                            'earth_system_generator.py, '
                                            'earth_system_common.py, '
                                            'food_insecurity_generator.py, '
                                            'the scenarios_* modules '
                                            '(heatwaves, coral bleaching, '
                                            'western heatwave, food '
                                            'insecurity), '
                                            'earth_system_controller.py, or '
                                            'their data sources (ERA5 / '
                                            'Copernicus CDS, Open-Meteo, '
                                            'ERDDAP / Coral Reef Watch, IPC '
                                            'Mapping Tool GeoJSON). Use when '
                                            'building or modifying KMZ '
                                            'layers, Google Earth scenarios, '
                                            'Plotly teasers, '
                                            'intel/legend/encyclopedia '
                                            'cards, or scenario configs -- '
                                            "and for ANY Paloma's Orrery "
                                            'visualization or text where '
                                            'human cost is an element (heat '
                                            'deaths, food insecurity, '
                                            'displacement): the restraint '
                                            'discipline section applies even '
                                            'to prose about these layers. Do '
                                            'not use for projects other than '
                                            "Paloma's Orrery.\n",
                                            'description: "Earth System KMZ '
                                            'and climate visualization '
                                            "pipeline for the Paloma's "
                                            'Orrery project. Use for any '
                                            'task touching '
                                            'earth_system_generator.py, '
                                            'earth_system_common.py, '
                                            'food_insecurity_generator.py, '
                                            'the scenarios_* modules '
                                            '(heatwaves, coral bleaching, '
                                            'western heatwave, food '
                                            'insecurity), '
                                            'earth_system_controller.py, or '
                                            'their data sources (ERA5 / '
                                            'Copernicus CDS, Open-Meteo, '
                                            'ERDDAP / Coral Reef Watch, IPC '
                                            'Mapping Tool GeoJSON). Use when '
                                            'building or modifying KMZ '
                                            'layers, Google Earth scenarios, '
                                            'Plotly teasers, '
                                            'intel/legend/encyclopedia '
                                            'cards, or scenario configs -- '
                                            "and for ANY Paloma's Orrery "
                                            'visualization or text where '
                                            'human cost is an element (heat '
                                            'deaths, food insecurity, '
                                            'displacement): the restraint '
                                            'discipline section applies even '
                                            'to prose about these layers. Do '
                                            'not use for projects other than '
                                            'Paloma\'s Orrery."\n'),
                                           ('version 1.2',
                                            'Skill version: 1.1 | Cut from '
                                            'palomas_orrery @ e83fe9ce | '
                                            '2026-07-12\n',
                                            'Skill version: 1.2 | '
                                            "2026-10-02, with Anthropic's "
                                            'Claude Opus 5.5, from\n'
                                            'palomas_orrery @ 94ff6c68. v1.2 '
                                            '(L-407) changes no rule: the '
                                            "header's\n"
                                            'description is put in quotes, '
                                            'because it holds ": " '
                                            '("displacement):\n'
                                            'the restraint discipline"), '
                                            'which YAML refuses unquoted, so '
                                            'a reinstall\n'
                                            'in Settings would have been '
                                            'refused. Found by the header '
                                            'check\n'
                                            'skills_index.py gained the same '
                                            'day.\n'
                                            'Earlier: 1.1 | Cut from '
                                            'palomas_orrery @ e83fe9ce | '
                                            '2026-07-12\n')],
 'skills/provenance-discipline/SKILL.md': [('description quoted',
                                            'description: Provenance and '
                                            'citation discipline for the '
                                            "Paloma's Orrery project. Use "
                                            'whenever running or discussing '
                                            'provenance_scanner.py, reading '
                                            'PROVENANCE_AUDIT.md, clearing '
                                            'Tier-1 findings, adding or '
                                            'reviewing # Source: citations, '
                                            'editing '
                                            'provenance_exceptions.json, '
                                            'embedding constants or '
                                            'numeric/factual claims in '
                                            'orrery display strings or data '
                                            'modules, or preparing a GitHub '
                                            'push (the gate is Tier-1 = 0 on '
                                            'the active build path, and it '
                                            'binds at EXPORT from the '
                                            'orrery). Also use when '
                                            'composing on-layer or '
                                            'user-facing factual text for '
                                            'any orrery visualization. Do '
                                            'not use for projects other than '
                                            "Paloma's Orrery.\n",
                                            'description: "Provenance and '
                                            'citation discipline for the '
                                            "Paloma's Orrery project. Use "
                                            'whenever running or discussing '
                                            'provenance_scanner.py, reading '
                                            'PROVENANCE_AUDIT.md, clearing '
                                            'Tier-1 findings, adding or '
                                            'reviewing # Source: citations, '
                                            'editing '
                                            'provenance_exceptions.json, '
                                            'embedding constants or '
                                            'numeric/factual claims in '
                                            'orrery display strings or data '
                                            'modules, or preparing a GitHub '
                                            'push (the gate is Tier-1 = 0 on '
                                            'the active build path, and it '
                                            'binds at EXPORT from the '
                                            'orrery). Also use when '
                                            'composing on-layer or '
                                            'user-facing factual text for '
                                            'any orrery visualization. Do '
                                            'not use for projects other than '
                                            'Paloma\'s Orrery."\n'),
                                           ('version 2.25',
                                            'Skill version: 2.24 | Cut from '
                                            'palomas_orrery @ feb5e369 '
                                            '(v2.24),\n',
                                            'Skill version: 2.25 | Cut from '
                                            'palomas_orrery @ 94ff6c68 '
                                            '(v2.25),\n'
                                            '@ feb5e369 (v2.24),\n'),
                                           ('v2.25 paragraph',
                                            'v2.24 settles L-395 with one '
                                            'new section, A Simple Error a '
                                            'Check Finds\n',
                                            'v2.25 (L-407, 2026-10-02) '
                                            "changes no rule: the header's "
                                            'description is\n'
                                            'put in quotes. Unquoted, the " '
                                            '#" in "# Source: citations" '
                                            'started a\n'
                                            'YAML comment, so Settings read '
                                            "only the description's first "
                                            '200\n'
                                            'characters, ending "adding or '
                                            'reviewing", and the words after '
                                            'it --\n'
                                            'citations, '
                                            'provenance_exceptions.json, '
                                            'display strings, the GitHub '
                                            'push\n'
                                            'gate, user-facing factual text '
                                            '-- never reached the '
                                            'description the\n'
                                            'skill is chosen by. Found by '
                                            'the header check '
                                            'skills_index.py gained\n'
                                            'the same day.\n'
                                            'v2.24 settles L-395 with one '
                                            'new section, A Simple Error a '
                                            'Check Finds\n')],
 'skills_index.py': [('docstring: headers checked as YAML',
                      "Module created: July 2026 with Anthropic's Claude "
                      'Fable 5 (L-097,\n'
                      'collegial relay; spec by Claude Opus 4.6, integrated '
                      'by Tony).\n',
                      "Module created: July 2026 with Anthropic's Claude "
                      'Fable 5 (L-097,\n'
                      'collegial relay; spec by Claude Opus 4.6, integrated '
                      'by Tony).\n'
                      '\n'
                      "Module updated: October 2, 2026 with Anthropic's "
                      'Claude Opus 5.5\n'
                      "(L-407: each skill's header is now also read as YAML, "
                      'the way the\n'
                      'Settings uploader reads it, and a header YAML refuses '
                      '-- or one with no\n'
                      'name or description as text -- is a CONSISTENCY '
                      'PROBLEM naming the\n'
                      'skill. On 2026-10-02 Settings refused '
                      'interactive-exhibit 1.10 for\n'
                      '"malformed YAML frontmatter" while this tool, reading '
                      'the header by its\n'
                      'own looser rules, built the manifest from it without '
                      'complaint. PyYAML\n'
                      'does the reading where it is installed; otherwise '
                      'built-in rules check\n'
                      'the faults that occur in these headers -- a bare '
                      'second line, ": " or\n'
                      '" #" inside an unquoted value, a value opening with a '
                      'YAML indicator, an\n'
                      'unclosed quote -- and the output says which of the '
                      'two read them.\n'
                      'orrery_maintenance_run.py runs this tool with --check '
                      'as a checker, so\n'
                      'a bad header fails the run.)\n'),
                     ('check_header: read the header as YAML',
                      'def first_sentence(text, limit=FALLBACK_TRUNC):',
                      'def check_header(lines, label):\n'
                      '    """Read a skill\'s header the way the Settings '
                      'uploader does: as YAML.\n'
                      '\n'
                      '    Returns ([problems], how), how naming what read '
                      'it. PyYAML reads it\n'
                      '    where it is installed. Without PyYAML, built-in '
                      'rules check the\n'
                      '    faults these headers have actually had; they are '
                      'narrower than YAML,\n'
                      '    and the report says so by naming them. L-407, '
                      '2026-10-02.\n'
                      '    """\n'
                      '    end = None\n'
                      '    for i in range(1, len(lines)):\n'
                      "        if lines[i].strip() == '---':\n"
                      '            end = i\n'
                      '            break\n'
                      '    if end is None:\n'
                      '        return [f"{label}: header has no closing '
                      '\'---\'"], \'no header\'\n'
                      '    raw = lines[1:end]\n'
                      '    try:\n'
                      '        import yaml\n'
                      '    except ImportError:\n'
                      '        yaml = None\n'
                      '    if yaml is not None:\n'
                      '        try:\n'
                      "            data = yaml.safe_load('\\n'.join(raw))\n"
                      '        except yaml.YAMLError as exc:\n'
                      "            first = ' '.join(str(exc).split())[:120]\n"
                      '            return [f"{label}: header is not valid '
                      'YAML, so Settings will "\n'
                      '                    f"refuse the file ({first})"], '
                      "'PyYAML'\n"
                      '        problems = []\n'
                      '        if not isinstance(data, dict):\n'
                      '            problems.append(f"{label}: header is YAML '
                      'but not a set of "\n'
                      '                            f"\'key: value\' lines")\n'
                      '        else:\n'
                      "            for key in ('name', 'description'):\n"
                      '                value = data.get(key)\n'
                      '                if not isinstance(value, str) or not '
                      'value.strip():\n'
                      '                    problems.append(f"{label}: header '
                      'has no {key} that "\n'
                      '                                    f"YAML reads as '
                      'text")\n'
                      "        return problems, 'PyYAML'\n"
                      '    problems, entries = [], []\n'
                      '    for n, line in enumerate(raw, 2):\n'
                      '        if not line.strip():\n'
                      '            continue\n'
                      "        if line[0] in ' \\t':\n"
                      '            if entries:\n'
                      "                entries[-1][1] += ' ' + line.strip()\n"
                      '            else:\n'
                      '                problems.append(f"{label}: header '
                      'line {n} is indented "\n'
                      '                                f"with no key above '
                      'it")\n'
                      '            continue\n'
                      "        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*):(?: "
                      "(.*))?$', line)\n"
                      '        if not m:\n'
                      '            problems.append(f"{label}: header line '
                      '{n} is neither "\n'
                      '                            f"\'key: value\' nor '
                      'indented, so YAML reads it "\n'
                      '                            f"as a broken key")\n'
                      '            continue\n'
                      '        entries.append([m.group(1), (m.group(2) or '
                      "'').strip()])\n"
                      '    for key, value in entries:\n'
                      '        if value[:1] in (\'"\', "\'"):\n'
                      '            if len(value) < 2 or value[-1] != '
                      'value[0]:\n'
                      '                problems.append(f"{label}: {key} '
                      'opens a quote it does not "\n'
                      '                                f"close")\n'
                      '            continue\n'
                      '        bad = None\n'
                      "        if ': ' in value or value.endswith(':'):\n"
                      '            bad = "\': \' inside an unquoted value"\n'
                      "        elif ' #' in value:\n"
                      '            bad = "\' #\' inside an unquoted value, '
                      'which YAML reads as a comment"\n'
                      '        elif value[:1] and value[:1] in '
                      "'[]{},&*!|>%@`#':\n"
                      '            bad = "an unquoted value starting with '
                      '%r" % value[:1]\n'
                      "        elif value[:2] in ('- ', '? '):\n"
                      '            bad = "an unquoted value starting with '
                      '%r" % value[:2]\n'
                      '        if bad:\n'
                      '            problems.append(f"{label}: {key} has '
                      '{bad}; quote the value")\n'
                      '    keys = [e[0] for e in entries]\n'
                      "    for key in ('name', 'description'):\n"
                      '        if key not in keys:\n'
                      '            problems.append(f"{label}: header has no '
                      '{key}")\n'
                      "    return problems, 'built-in rules (PyYAML is not "
                      "installed)'\n"
                      '\n'
                      '\n'
                      'def first_sentence(text, limit=FALLBACK_TRUNC):'),
                     ('parse_skill runs the header check',
                      '    if fm is None:\n'
                      '        return None, [f"{skill_dir.name}: '
                      'missing/unterminated frontmatter"], warnings\n',
                      '    if fm is None:\n'
                      '        return None, [f"{skill_dir.name}: '
                      'missing/unterminated frontmatter"], warnings\n'
                      '    header_problems, header_how = check_header(lines, '
                      'skill_dir.name)\n'
                      '    problems.extend(header_problems)\n'),
                     ('record says what read the header',
                      "    return {'name': name, 'version': version, "
                      "'fires_when': fires}, problems, warnings\n",
                      "    return ({'name': name, 'version': version, "
                      "'fires_when': fires,\n"
                      "             'header_how': header_how}, problems, "
                      'warnings)\n'),
                     ('report: how the headers were read',
                      '    if problems:\n'
                      '        print("CONSISTENCY PROBLEMS:")\n',
                      "    hows = sorted(set(r.get('header_how', '?') for r "
                      'in records))\n'
                      '    print(f"Headers: {len(records)} read as YAML by '
                      '{\', \'.join(hows)}.")\n'
                      '    if problems:\n'
                      '        print("CONSISTENCY PROBLEMS:")\n'),
                     ('check_header takes the loose reading',
                      'def check_header(lines, label):',
                      'def check_header(lines, label, loose=None):'),
                     ('PyYAML path: a value cut short is a problem',
                      "            for key in ('name', 'description'):\n"
                      '                value = data.get(key)\n'
                      '                if not isinstance(value, str) or not '
                      'value.strip():\n'
                      '                    problems.append(f"{label}: header '
                      'has no {key} that "\n'
                      '                                    f"YAML reads as '
                      'text")\n'
                      "        return problems, 'PyYAML'",
                      "            for key in ('name', 'description'):\n"
                      '                value = data.get(key)\n'
                      '                if not isinstance(value, str) or not '
                      'value.strip():\n'
                      '                    problems.append(f"{label}: header '
                      'has no {key} that "\n'
                      '                                    f"YAML reads as '
                      'text")\n'
                      '            # A header can be valid YAML and still '
                      'lose words: " #" in an\n'
                      '            # unquoted value starts a comment, and '
                      'the rest of the line is\n'
                      '            # dropped without an error. '
                      "provenance-discipline's\n"
                      '            # description was read as its first 200 '
                      'characters that way\n'
                      '            # until 2026-10-02 (L-407).\n'
                      '            for key, raw_value in (loose or '
                      '{}).items():\n'
                      '                value = data.get(key)\n'
                      '                if (isinstance(value, str) and '
                      'raw_value[:1] not in (\'"\', "\'")\n'
                      "                        and ' '.join(value.split()) "
                      "!= ' '.join(raw_value.split())):\n"
                      '                    problems.append(f"{label}: YAML '
                      'reads {key} as only its "\n'
                      '                                    f"first '
                      '{len(value)} characters of "\n'
                      '                                    '
                      'f"{len(raw_value)} -- \' #\' starts a "\n'
                      '                                    f"comment; quote '
                      'the value")\n'
                      "        return problems, 'PyYAML'"),
                     ("built-in rules: ' #' before ': '",
                      "        if ': ' in value or value.endswith(':'):\n"
                      '            bad = "\': \' inside an unquoted value"\n'
                      "        elif ' #' in value:\n"
                      '            bad = "\' #\' inside an unquoted value, '
                      'which YAML reads as a comment"\n',
                      "        if ' #' in value:\n"
                      '            bad = ("\' #\' inside an unquoted value, '
                      'which YAML reads as the "\n'
                      '                   "start of a comment")\n'
                      "        elif ': ' in value or value.endswith(':'):\n"
                      '            bad = "\': \' inside an unquoted '
                      'value"\n'),
                     ('parse_skill passes the loose reading',
                      '    header_problems, header_how = check_header(lines, '
                      'skill_dir.name)',
                      '    header_problems, header_how = check_header(lines, '
                      'skill_dir.name, fm)')]}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    results = []
    for path in sorted(EDITS):
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       0a5eea0b, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got))
        nl = "\r\n" if b"\r\n" in raw else "\n"
        text = raw.decode("utf-8").replace("\r\n", "\n")
        done = []
        for label, old, new in EDITS[path]:
            if text.count(old) != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, text.count(old)))
            text = text.replace(old, new)
            done.append(label)
        results.append((path, text.replace("\n", nl), done))
    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-46s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py (VS Code, Run). Expect 20 of")
    print("     20 gating checkers -- one more than before: Skill headers.")
    print("  2. Move this script into documentation/; commit and push.")
    print("  3. Settings > Skills: upload these three SKILL.md files again:")
    print("       skills/interactive-exhibit/SKILL.md        (1.10, already")
    print("         fixed by patch_L406_3 -- upload it if it has not gone in)")
    print("       skills/earth-system-pipeline/SKILL.md      (1.2)")
    print("       skills/provenance-discipline/SKILL.md      (2.25)")
    print("  4. Replace the Project's instructions with PROJECT_INSTRUCTIONS.md")
    print("     v3.79.")
    print("  5. Delete patch_L407_1_skill_headers_20261002.py if it is still")
    print("     in the repo root: it never ran and never will.")

if __name__ == "__main__":
    main()
