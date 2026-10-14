"""patch_L440_2_word_order_search_20261014.py -- L-440 (the dashboard):
the search ignores word order; and the close of L-431 (orbital periods
from JPL), L-395 (the Horizons check's move) and L-440 on Tony's runs and
looks of October 14.

Built on orrery 5ca56dfe18b5cbbaae9a604cf4c195fe3246caae at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-12-26_2212_run_record.md"), read again just before the
build. The gallery is read (by Dashboard parity), not touched: gallery
86ef2df6313f956f5c9e49611e6a2bdd0e95da29 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 14, 2026 with Anthropic's Claude Opus 5.5.
Record: section 9 of documentation/HANDOFF_L431_build3_website_20261014.md
(added by this patch).

HOW TO RUN
    Save it in the orrery repo's ROOT folder, open it in VS Code and press
    Run, or from a terminal in that folder:
        python patch_L440_2_word_order_search_20261014.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing. A second run finds its anchors gone and
    writes nothing.

WHAT IT CHANGES
    palomas_orrery_dashboard.py: the search matches each typed word on its
      own, anywhere on a card, in any order (Tony, 2026-10-14). One word
      finds what it found before; each word added narrows the list. The
      rule is matching_groups(), at module level. Dashboard Parity's card
      and short line say it checks the search too.
    test_dashboard_parity.py: rule 6, the search, tested on the
      dashboard's own matching_groups(): Tony's example in three orders,
      a search that must find nothing, one word against the old search,
      and words added narrowing; a tenth planted fault, the old
      whole-phrase search.
    orrery_maintenance_run.py: the comment on Dashboard parity; the stamp.
    LEDGER_CONSOLIDATED.md: L-431, L-395 and L-440 to DONE, with Tony's
      verdicts quoted from his run record; L-441 opened for the "when"
      index, L-440's later slice; the stamp.
      documentation/WHERE_WE_ARE.md, by section, never below the
      run-record marker. The L-431 handoff gains section 9.
    No skill or protocol version changes.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, no edit lands below the run-record marker,
    and none touches the ledger's index, which the maintenance run
    rewrites. Your notes cannot make it refuse. If any check fails,
    NOTHING is written. A file found with Windows line endings is matched
    after turning them into LF and written back LF, and the patch says
    so. Undo after a run is Discard Changes in GitHub Desktop.

Role: patch
Domain: dev_tools
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'
ZONES = (('<!-- INDEX:START', '<!-- INDEX:END -->'),
         ('<!-- SKILL-MANIFEST:START', '<!-- SKILL-MANIFEST:END -->'))
MUST_EXIST = ('celestial_objects.py', 'LEDGER_CONSOLIDATED.md', 'palomas_orrery_dashboard.py')

EDITS = [
    ('palomas_orrery_dashboard.py', "line 255: October 14, 2026 with Anthropic's Claude Opus",
     (
         'served cache, in alphabetical place, with its short line.\n'
         '"""\n'
     ),
     (
         'served cache, in alphabetical place, with its short line.\n'
         "October 14, 2026 with Anthropic's Claude Opus 5.5 (L-440, Tony's request\n"
         'of the same day: "can we make the dashboard search be word order\n'
         'insensitive? for example: objects export pull = pull objects export"):\n'
         'the search matches each typed word on its own, so a card shows when every\n'
         "word appears somewhere on it -- the group's name, the card's name, its\n"
         'short line or its paragraph -- in any order. One word finds what it found\n'
         'before; each word added narrows the list (Tony: "with order insensitive,\n'
         'i would actually narrow the search but still find results"). Until now\n'
         'the typed text had to appear as one phrase. matching_groups() holds the\n'
         'rule at module level, so Dashboard Parity can test it and plant the old\n'
         'phrase match as a fault.\n'
         '"""\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 1215: "card carries its short line of twelve words ',
     (
         '         "names a row, that every button\'s script is on disk, and that every "\n'
         '         "card carries its short line of twelve words or fewer. It reads "\n'
         '         "both repositories and edits neither. Nine faults are planted "\n'
         '         "first, each caught by name. Ends on \\"DASHBOARD PARITY: PASS\\" "\n'
     ),
     (
         '         "names a row, that every button\'s script is on disk, and that every "\n'
         '         "card carries its short line of twelve words or fewer; and that the "\n'
         '         "search finds a card by its words in any order. It reads "\n'
         '         "both repositories and edits neither. Ten faults are planted "\n'
         '         "first, each caught by name. Ends on \\"DASHBOARD PARITY: PASS\\" "\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 1852: "Checks run steps against buttons by name, an',
     (
         '     "Dashboard Parity"):\n'
         '        "Checks run steps against buttons by name, and every card\'s short line.",\n'
         '    ("Maintenance Run",\n'
     ),
     (
         '     "Dashboard Parity"):\n'
         '        "Checks run steps against buttons, short lines, and the search.",\n'
         '    ("Maintenance Run",\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 1970: def search_words(query):',
     (
         '    return CARD_LINES.get((group_name, label), "")\n'
         '\n'
     ),
     (
         '    return CARD_LINES.get((group_name, label), "")\n'
         '\n'
         '\n'
         'def search_words(query):\n'
         '    """The words of a search, case folded, in the order typed."""\n'
         '    return (query or "").casefold().split()\n'
         '\n'
         '\n'
         'def words_in(words, *texts):\n'
         '    """True when every word appears somewhere in the texts, in any order.\n'
         '\n'
         '    Each word is matched on its own, as a piece of text, so "pull" also\n'
         '    finds "pulls" and the order the words are typed in does not matter\n'
         '    (Tony, 2026-10-14: "objects export pull = pull objects export").\n'
         '    No words matches nothing; the caller shows everything for an empty\n'
         '    box.\n'
         '    """\n'
         '    if not words:\n'
         '        return False\n'
         '    hay = " ".join(t.casefold() for t in texts if t)\n'
         '    return all(w in hay for w in words)\n'
         '\n'
         '\n'
         'def card_matches(query, group_name, entry):\n'
         '    """True when every word of `query` is on the card: its group\'s name,\n'
         '    its own name, its short line (L-440) or its "+ more" paragraph."""\n'
         '    return words_in(search_words(query), group_name, entry[0],\n'
         '                    card_line(group_name, entry[0]), entry[2])\n'
         '\n'
         '\n'
         'def matching_groups(query, groups):\n'
         '    """What a search draws: [(group name, entries)], headings kept.\n'
         '\n'
         '    Each word is matched on its own, anywhere on the card, in any order\n'
         '    (Tony, 2026-10-14). So one word finds exactly what it found before,\n'
         '    and each word added narrows the list rather than emptying it: "I\n'
         '    usually use only one word to avoid getting no results with word\n'
         '    combinations. With order insensitive, I would actually narrow the\n'
         '    search but still find results."\n'
         '\n'
         '    A group whose own name holds every word comes whole: somebody typing\n'
         '    a category name means the category ("stars", 2026-09-19).\n'
         '    """\n'
         '    words = search_words(query)\n'
         '    out = []\n'
         '    for name, entries in groups.items():\n'
         '        if not words or words_in(words, name):\n'
         '            drawn = list(entries)\n'
         '        else:\n'
         '            drawn = filter_entries(\n'
         '                entries, lambda e, g=name: card_matches(query, g, e))\n'
         '        if drawn:\n'
         '            out.append((name, drawn))\n'
         '    return out\n'
         '\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 2472: def _entry_matches(self, group_name, entry, n',
     (
         '\n'
         '    def _entry_matches(self, group_name, entry, needle):\n'
         '        """Name, short line or description contains `needle`, any case.\n'
         '\n'
         '        The short line is searched as well as the paragraph (L-440): it\n'
         '        is the text a card shows, so a word read on a card finds it.\n'
         '        """\n'
         '        return (needle in entry[0].lower()\n'
         '                or needle in card_line(group_name, entry[0]).lower()\n'
         '                or needle in entry[2].lower())\n'
         '\n'
         '    def _render_launch(self, query):\n'
     ),
     (
         '\n'
         '    def _render_launch(self, query):\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 2500: for group_name, entries in LAUNCH_GROUPS.item',
     (
         '\n'
         '        for group_name, entries in LAUNCH_GROUPS.items():\n'
         '            if not needle:\n'
         '                drawn = list(entries)\n'
         '            elif needle in group_name.lower():\n'
         '                # The GROUP NAME counts as a match, and takes the whole\n'
         '                # group with it. Typing "stars" found nothing before\n'
         '                # this: the Stars group exists, but its one button is\n'
         '                # called Star Visualization and no description says\n'
         '                # "stars". Somebody typing a category name means the\n'
         '                # category. (Found by testing, 2026-09-19.)\n'
         '                drawn = list(entries)\n'
         '            else:\n'
         '                drawn = filter_entries(\n'
         '                    entries,\n'
         '                    lambda e, g=group_name: self._entry_matches(g, e, needle))\n'
         '            if not drawn:\n'
         '                continue\n'
         '            shown += sum(1 for e in drawn if not isinstance(e, str))\n'
     ),
     (
         '\n'
         '        # The matching itself is matching_groups(), at module level,\n'
         '        # where Dashboard Parity tests it (L-440, 2026-10-14): each word\n'
         '        # on its own, anywhere on the card, in any order; a group whose\n'
         '        # name holds every word comes whole (the GROUP NAME rule: typing\n'
         '        # "stars" found nothing before it, 2026-09-19).\n'
         '        for group_name, drawn in matching_groups(needle, LAUNCH_GROUPS):\n'
         '            shown += sum(1 for e in drawn if not isinstance(e, str))\n'
     )),
    ('test_dashboard_parity.py', 'line 54: 6. The search finds a card by its words in an',
     (
         '       every line in CARD_LINES belongs to a card.\n'
         '    The few steps a differently named button covers on purpose are in\n'
     ),
     (
         '       every line in CARD_LINES belongs to a card.\n'
         '    6. The search finds a card by its words in any order (Tony,\n'
         '       2026-10-14: "objects export pull = pull objects export"): the\n'
         "       dashboard's own matching_groups(), the function its search box\n"
         '       calls, is asked SEARCH_CASES below and shows what each case says;\n'
         '       one word shows exactly what the old whole-phrase search showed;\n'
         '       and each word added narrows the list, never widens it.\n'
         '    The few steps a differently named button covers on purpose are in\n'
     )),
    ('test_dashboard_parity.py', 'line 65: Before the real comparison it plants nine fau',
     (
         '\n'
         '    Before the real comparison it plants nine faults, one at a time, in\n'
         '    copies of the real lists, and each must be caught by its own kind of\n'
     ),
     (
         '\n'
         '    Before the real comparison it plants ten faults, one at a time, in\n'
         '    copies of the real lists, and each must be caught by its own kind of\n'
     )),
    ('test_dashboard_parity.py', 'line 70: and an unreadable runner.',
     (
         '    twelve words, a line for no card, an indented button naming no step,\n'
         '    and an unreadable runner.\n'
         '\n'
     ),
     (
         '    twelve words, a line for no card, an indented button naming no step,\n'
         '    an unreadable runner, and a search that matches only the whole\n'
         "    phrase, as the dashboard's did until 2026-10-14.\n"
         '\n'
     )),
    ('test_dashboard_parity.py', 'line 77: Module updated: October 14, 2026 with Anthrop',
     (
         "the dashboard's labels, descriptions and findability).\n"
         '"""\n'
     ),
     (
         "the dashboard's labels, descriptions and findability).\n"
         "Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-440,\n"
         "Tony's request of the same day: rule 6, the search finds a card by its\n"
         "words in any order, tested on the dashboard's own card_matches(); a tenth\n"
         'planted fault, the old whole-phrase search, must be caught as SEARCH.)\n'
         '"""\n'
     )),
    ('test_dashboard_parity.py', 'line 122: # Rule 6, the search: (typed, card names that',
     (
         "NODE_RUNNER = 'documentation/run_offline_check.py'\n"
         '\n'
     ),
     (
         "NODE_RUNNER = 'documentation/run_offline_check.py'\n"
         '\n'
         '# Rule 6, the search: (typed, card names that must be shown, "only" when\n'
         "# nothing else may be). The first three are Tony's example of 2026-10-14\n"
         '# in three orders and two cases; the last must show nothing, so a search\n'
         '# that shows everything cannot pass. ONE_WORDS must each show exactly what\n'
         '# the old whole-phrase search showed, and NARROWING each list smaller or\n'
         '# equal as words are added.\n'
         'SEARCH_CASES = (\n'
         "    ('objects export pull', {'Objects Export Pull'}, 'includes'),\n"
         "    ('pull objects export', {'Objects Export Pull'}, 'includes'),\n"
         "    ('Export OBJECTS pull', {'Objects Export Pull'}, 'includes'),\n"
         "    ('pull objects zqxw', set(), 'only'),\n"
         ')\n'
         "ONE_WORDS = ('export', 'horizons', 'stars', 'guest')\n"
         "NARROWING = ('export', 'export pull', 'export pull objects')\n"
         '\n'
     )),
    ('test_dashboard_parity.py', 'line 210: """(LAUNCH_GROUPS, CARD_LINES, SCRIPT_DIR, GA',
     (
         'def read_dashboard(path=DASHBOARD):\n'
         '    """(LAUNCH_GROUPS, CARD_LINES, SCRIPT_DIR, GALLERY_REPO_DIR)."""\n'
         '    saved = {}\n'
     ),
     (
         'def read_dashboard(path=DASHBOARD):\n'
         '    """(LAUNCH_GROUPS, CARD_LINES, SCRIPT_DIR, GALLERY_REPO_DIR,\n'
         '    matching_groups)."""\n'
         '    saved = {}\n'
     )),
    ('test_dashboard_parity.py', "line 231: matches = getattr(module, 'matching_groups', ",
     (
         "        raise Unreadable('%s: no CARD_LINES' % path)\n"
         '    return (module.LAUNCH_GROUPS, lines, module.SCRIPT_DIR,\n'
         '            module.GALLERY_REPO_DIR)\n'
         '\n'
     ),
     (
         "        raise Unreadable('%s: no CARD_LINES' % path)\n"
         "    matches = getattr(module, 'matching_groups', None)\n"
         '    if matches is None:\n'
         "        raise Unreadable('%s: no matching_groups' % path)\n"
         '    return (module.LAUNCH_GROUPS, lines, module.SCRIPT_DIR,\n'
         '            module.GALLERY_REPO_DIR, matches)\n'
         '\n'
     )),
    ('test_dashboard_parity.py', 'line 352: def planted(steps, buttons, lines):',
     (
         '\n'
         'def planted(steps, buttons, lines):\n'
         '    """Nine faults, each required to produce its own kind of finding."""\n'
         '    results = []\n'
     ),
     (
         '\n'
         'def _shown(search, typed, groups):\n'
         '    return sorted(e[0] for _g, drawn in search(typed, groups)\n'
         '                  for e in drawn if not isinstance(e, str))\n'
         '\n'
         '\n'
         'def check_search(groups, search):\n'
         '    """Rule 6: the dashboard\'s matching_groups() against SEARCH_CASES,\n'
         '    ONE_WORDS and NARROWING."""\n'
         '    found = []\n'
         '    for typed, want, how in SEARCH_CASES:\n'
         '        shown = set(_shown(search, typed, groups))\n'
         "        ok = (shown == want) if how == 'only' else (bool(want) and want <= shown)\n"
         '        if not ok:\n'
         '            found.append((\'SEARCH\', \'typing "%s" shows %s; it should show %s%s\'\n'
         "                          % (typed, sorted(shown)[:6] or 'nothing',\n"
         "                             'only ' if how == 'only' else '',\n"
         "                             sorted(want) or 'nothing')))\n"
         '    for word in ONE_WORDS:\n'
         '        if _shown(search, word, groups) != _shown(_phrase_only, word, groups):\n'
         '            found.append((\'SEARCH\', \'one word, "%s", no longer shows what it \'\n'
         "                          'showed before' % word))\n"
         '    sizes = [len(_shown(search, typed, groups)) for typed in NARROWING]\n'
         '    if any(b > a for a, b in zip(sizes, sizes[1:])):\n'
         "        found.append(('SEARCH', 'adding words widened the list: %s'\n"
         '                      % \', \'.join(\'"%s" %d\' % p for p in zip(NARROWING, sizes))))\n'
         '    return found\n'
         '\n'
         '\n'
         'def _phrase_only(query, groups, lines=None):\n'
         '    """The search as it was until 2026-10-14: the typed text as one\n'
         "    phrase, in the group's name (the whole group), or a card's name,\n"
         '    short line or paragraph. Planted, to show rule 6 can fail, and the\n'
         '    yardstick a single word must still match."""\n'
         "    needle = (query or '').strip().lower()\n"
         '    lines = _LINES if lines is None else lines\n'
         '    out = []\n'
         '    for name, entries in groups.items():\n'
         '        if needle in name.lower():\n'
         '            drawn = [e for e in entries if not isinstance(e, str)]\n'
         '        else:\n'
         '            drawn = [e for e in entries if not isinstance(e, str)\n'
         '                     and (needle in e[0].lower() or needle in e[2].lower()\n'
         "                          or needle in lines.get((name, e[0]), '').lower())]\n"
         '        if drawn:\n'
         '            out.append((name, drawn))\n'
         '    return out\n'
         '\n'
         '\n'
         '_LINES = {}\n'
         '\n'
         '\n'
         'def planted(steps, buttons, lines, groups=None):\n'
         '    """Ten faults, each required to produce its own kind of finding."""\n'
         '    results = []\n'
     )),
    ('test_dashboard_parity.py', 'line 408: if groups is not None:',
     (
         "                                                      'no_such_gallery')))\n"
         '    return results\n'
     ),
     (
         "                                                      'no_such_gallery')))\n"
         '    if groups is not None:\n'
         '        got = check_search(groups, _phrase_only)\n'
         "        results.append(('a search matching the whole phrase only', 'SEARCH',\n"
         "                        any(k == 'SEARCH' for k, _t in got)))\n"
         '    return results\n'
     )),
    ('test_dashboard_parity.py', 'line 418: groups, lines, sdir, gdir = read_dashboard()',
     (
         '        steps = read_runs()\n'
         '        groups, lines, sdir, gdir = read_dashboard()\n'
         '    except Unreadable as exc:\n'
     ),
     (
         '        steps = read_runs()\n'
         '        groups, lines, sdir, gdir, matches = read_dashboard()\n'
         '        _LINES.update(lines)\n'
         '    except Unreadable as exc:\n'
     )),
    ('test_dashboard_parity.py', 'line 430: results = planted(steps, buttons, lines)',
     (
         '    caught = 0\n'
         '    results = planted(steps, buttons, lines)\n'
         '    for label, kind, ok in results:\n'
     ),
     (
         '    caught = 0\n'
         '    results = planted(steps, buttons, lines, groups)\n'
         '    for label, kind, ok in results:\n'
     )),
    ('test_dashboard_parity.py', 'line 436: found = compare(steps, buttons, lines)',
     (
         '\n'
         '    found = compare(steps, buttons, lines)\n'
         '    counts = {}\n'
     ),
     (
         '\n'
         '    found = compare(steps, buttons, lines) + check_search(groups, matches)\n'
         '    counts = {}\n'
     )),
    ('test_dashboard_parity.py', "line 467: 'carry a short line' % (caught, total, len(st",
     (
         "          'steps matched to their buttons by name and script; %d cards '\n"
         "          'carry a short line' % (caught, total, len(steps),\n"
         "                                  len(set((b['group'], b['name'])\n"
         '                                          for b in buttons))))\n'
         '    return 0\n'
     ),
     (
         "          'steps matched to their buttons by name and script; %d cards '\n"
         "          'carry a short line; the search finds %d of %d cases in any '\n"
         "          'word order' % (caught, total, len(steps),\n"
         "                          len(set((b['group'], b['name'])\n"
         '                                  for b in buttons)),\n'
         '                          len(SEARCH_CASES), len(SEARCH_CASES)))\n'
         '    return 0\n'
     )),
    ('orrery_maintenance_run.py', 'line 234: Module updated: October 14, 2026 with Anthrop',
     (
         'gating gave on 2026-10-13.)\n'
         '"""\n'
     ),
     (
         'gating gave on 2026-10-13.)\n'
         "Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5 (L-440:\n"
         "the comment on Dashboard parity says it also checks the dashboard's\n"
         'search, word order ignored, with a tenth planted fault.)\n'
         '"""\n'
     )),
    ('orrery_maintenance_run.py', 'line 415: # card its short line; nine faults planted fi',
     (
         '    # has a dashboard button with the same name and script, and every\n'
         '    # card its short line; nine faults planted first, each caught.\n'
         "    ('Dashboard parity', ['test_dashboard_parity.py'],\n"
     ),
     (
         '    # has a dashboard button with the same name and script, and every\n'
         '    # card its short line; and the search finds a card by its words in\n'
         '    # any order (2026-10-14); ten faults planted first, each caught.\n'
         "    ('Dashboard parity', ['test_dashboard_parity.py'],\n"
     )),
    ('LEDGER_CONSOLIDATED.md', 'line 418: Module updated: October 14, 2026 with Anthrop',
     (
         'v3.96), built on 5cd63cce and gallery 4b2b660a.\n'
         'Review and RICE update Tony 6-21-2026\n'
     ),
     (
         'v3.96), built on 5cd63cce and gallery 4b2b660a.\n'
         "Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5\n"
         "(L-431, L-395 and L-440 closed on Tony's runs and looks; the dashboard's\n"
         'search matches each word in any order; L-441 opened for the "when"\n'
         'index), built on 5ca56df.\n'
         'Review and RICE update Tony 6-21-2026\n'
     )),
    ('LEDGER_CONSOLIDATED.md', 'line 1159: #### [L-441] The dashboard\'s "when" index, ge',
     (
         '\n'
         "#### [L-440] The dashboard's labels, short lines and headings, and the parity check (dashboard, both repos)\n"
         '<!-- L:440 status:OPEN upd:2026-10-14 section:A flag: rice: -->\n'
         "- **Tony's request, 2026-10-12**, after confirming every run step has a\n"
     ),
     (
         '\n'
         '#### [L-441] The dashboard\'s "when" index, generated from tags (dashboard)\n'
         '<!-- L:441 status:OPEN upd:2026-10-14 section:A flag: rice: -->\n'
         "- **Opened 2026-10-14, re-homed from L-440 at its close.** Tony's ruling\n"
         "  in the L-440 build session (2026-10-13), on an index of the dashboard's\n"
         '  tools by when each is used: "record for later." If it is built, it is\n'
         '  generated from a tag on each entry, never hand-written.\n'
         '**Gap:** a design talk, when Tony wants it.\n'
         '**Ref:** L-440; `documentation/HANDOFF_L440_dashboard_labels_20261013.md`\n'
         '(sections 2 and 7); `palomas_orrery_dashboard.py`.\n'
         '\n'
         "#### [L-440] The dashboard's labels, short lines and headings, and the parity check (dashboard, both repos)\n"
         '<!-- L:440 status:DONE upd:2026-10-14 section:A flag: rice: -->\n'
         "- **Tony's request, 2026-10-12**, after confirming every run step has a\n"
     )),
    ('LEDGER_CONSOLIDATED.md', "line 1208: **Gap:** Tony's look at the dashboard (the ha",
     (
         '  Parity is the check that it is complete.\n'
         "**Gap:** Tony's look at the dashboard (the handoff, section 6). Later\n"
         'slice, recorded: the "when" index, from per-entry tags.\n'
         '**Ref:** `documentation/HANDOFF_L440_dashboard_labels_20261013.md`;\n'
     ),
     (
         '  Parity is the check that it is complete.\n'
         "- **2026-10-14, Tony's look, and CLOSED.** In his run record\n"
         '  (`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`, at 5ca56df): "looks great. the indentations and expansion and\n'
         '  groupings seem to work well. thanks."\n'
         '- **2026-10-14, the search ignores word order** (Tony, the same day:\n'
         '  "can we make the dashboard search be word order insensitive? for\n'
         '  example: objects export pull = pull objects export"), built by\n'
         '  `patch_L440_2_word_order_search_20261014.py` on 5ca56df. Each typed\n'
         "  word is matched on its own, anywhere on a card (its group's name, its\n"
         '  own name, its short line, its paragraph), in any order. One word finds\n'
         '  exactly what it found before; each word added narrows the list. Tony\n'
         '  chose that over a names-first search, which would have hidden\n'
         '  paragraph matches from a one-word search: "currently i usually use\n'
         '  only one word to avoid getting no results with word combinations.\n'
         '  with order insensitive, i would actually narrow the search but still\n'
         '  find results." The rule is `matching_groups()`, at module level, and\n'
         '  Dashboard Parity tests it as its rule 6, with a tenth planted fault,\n'
         '  the old whole-phrase search.\n'
         '**Gap:** none. Its later slice, the "when" index, is L-441.\n'
         '**Ref:** `documentation/HANDOFF_L440_dashboard_labels_20261013.md`;\n'
     )),
    ('LEDGER_CONSOLIDATED.md', 'line 1609: <!-- L:431 status:PENDING-GATE upd:2026-10-14',
     (
         '#### [L-431] Orbital periods from JPL, for every body, printed by their errors (orrery, provenance)\n'
         '<!-- L:431 status:PENDING-GATE upd:2026-10-14 section:A flag: rice: -->\n'
         "- **Opened 2026-10-10** from Tony's look at Encke: its hover has no\n"
     ),
     (
         '#### [L-431] Orbital periods from JPL, for every body, printed by their errors (orrery, provenance)\n'
         '<!-- L:431 status:DONE upd:2026-10-14 section:A flag: rice: -->\n'
         "- **Opened 2026-10-10** from Tony's look at Encke: its hover has no\n"
     )),
    ('LEDGER_CONSOLIDATED.md', 'line 1944: 3. The website: BUILT and tested offline (202',
     (
         '   barycentre orbits (patch_L431_8, pushed at 4da3d7cc).\n'
         '3. The website: BUILT and tested offline (2026-10-14, above). It\n'
         "   closes at Tony's run (both patches, both maintenance runs, the Daily\n"
         '   Run, the live check) and his look on the phone and the desktop;\n'
         '   the status then goes to DONE with no other change.\n'
         "Loose ends, re-homed at this build: the Pluto-Charon barycentre's own\n"
     ),
     (
         '   barycentre orbits (patch_L431_8, pushed at 4da3d7cc).\n'
         '3. The website: BUILT (2026-10-14, above), RUN and ACCEPTED the same\n'
         '   day; CLOSED.\n'
         "- **2026-10-14, run and accepted.** Tony's run record (`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`, at\n"
         '  5ca56df): patch_L431_11, the orrery maintenance run ("Horizons check\n'
         '  ... PASS -- 3 checked today, 3 queries", JPL\'s own answers for\n'
         '  Mercury, Jupiter and Encke; 30 of 30), pushed at 344ed65;\n'
         "  patch_L431_12 and the website's run (27 of 27); patch_L431_13 and the\n"
         '  orrery run again (30 of 30), pushed at b9aee91; the Daily Run (the\n'
         '  cache swapped in first time; 27 of 27), pushed at 86ef2df. His look:\n'
         '  Mercury and Jupiter "--yes", Mars "-- yes", Pluto\'s barycentre ("not\n'
         '  yet fetched") "-- yes", Earth\'s Sun Direction "-- yes, it says typed\n'
         '  not fetched", Encke and Halley not rows "-- yes", the Moon "-- xyz\n'
         '  position only", the Sun room "-- right". His "yes" on Pluto\'s row\n'
         '  answers the build\'s one question: it ships saying "not yet fetched\n'
         '  from JPL", and the barycentre\'s own period waits for the objects work\n'
         "  (L-433's note). The live check's output is not in the record.\n"
         "Loose ends, re-homed at this build: the Pluto-Charon barycentre's own\n"
     )),
    ('LEDGER_CONSOLIDATED.md', 'line 2807: <!-- L:395 status:PENDING-GATE upd:2026-10-14',
     (
         "#### [L-395] The gallery's objects are hand-copied from the orrery's dictionary: export them, and check them against Horizons (orrery, gallery, objects)\n"
         '<!-- L:395 status:PENDING-GATE upd:2026-10-14 section:A flag: rice: -->\n'
         '- **2026-10-01, design rulings and the first build** [verified: orrery\n'
     ),
     (
         "#### [L-395] The gallery's objects are hand-copied from the orrery's dictionary: export them, and check them against Horizons (orrery, gallery, objects)\n"
         '<!-- L:395 status:DONE upd:2026-10-14 section:A flag: rice: -->\n'
         '- **2026-10-01, design rulings and the first build** [verified: orrery\n'
     )),
    ('LEDGER_CONSOLIDATED.md', 'line 3192: **Gap:** The move is built. It closes when To',
     (
         '    red at day 30 and a push and a pull behind, is not red every cycle.\n'
         "**Gap:** The move is built. It closes when Tony's orrery maintenance\n"
         'run shows "Horizons check" as PASS or NOTHING DUE and the website\'s\n'
         'offline run is green on the pulled export; the status then goes to\n'
         'DONE with no other change.\n'
         'Loose ends, re-homed at this build: the fields the list lacks (a\n'
     ),
     (
         '    red at day 30 and a push and a pull behind, is not red every cycle.\n'
         "- **2026-10-14, CLOSED on Tony's runs** (`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`, at 5ca56df). The\n"
         '  orrery maintenance run\'s Horizons check reached JPL and passed, "PASS\n'
         '  -- 3 checked today, 3 queries" (the three fetched periods, the first\n'
         "  live test of the period comparison and of a small body's COMMAND\n"
         '  sent with %3B); "Horizons confirmations" read "13 of 13 entries and\n'
         '  3 periods confirmed, 26 sheets read". The website\'s offline run read\n'
         '  the dates from the pulled export: "13 of 13 confirmed, and 3\n'
         '  periods, within 30 days".\n'
         '**Gap:** none; the move is built and running.\n'
         'Loose ends, re-homed at this build: the fields the list lacks (a\n'
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 14, 2026: the website p',
     (
         '\n'
         "Last updated: October 14, 2026: the website prints JPL's periods; the Horizons check moved.\n"
         '- Written at orrery 5cd63cce and gallery 4b2b660a.\n'
         '\n'
     ),
     (
         '\n'
         'Last updated: October 14, 2026, evening: periods accepted; three items closed; search.\n'
         '- Written at orrery 5ca56df and gallery 86ef2df.\n'
         '\n'
     )),
    ('documentation/WHERE_WE_ARE.md', "line 10: > - Orbital periods, build 3: the website's h",
     (
         '> **Changed since you last read this:**\n'
         "> - Orbital periods, build 3: the website's hovers print the orrery's\n"
         '>   period, its centre and the date JPL gave it. Built and tested here.\n'
         "> - The Horizons check moved into the orrery's maintenance run, and\n"
         ">   checks each period too. The website's Daily Run is three steps.\n"
         '>\n'
         '> **Do next:** *Run the three patches in the order the handoff gives\n'
         '> (in Where the details are); then the look.*\n'
         '>\n'
         '> **Needs you now:**\n'
         "> - *One question: Pluto-Charon's barycentre has no period from JPL\n"
         '>   yet (the orrery never fetches the barycentre itself), so its row\n'
         '>   says "not yet fetched from JPL". Ship it so, and fetch it later?*\n'
         '\n'
     ),
     (
         '> **Changed since you last read this:**\n'
         '> - Orbital periods are on the website, accepted at your look. L-431\n'
         ">   (periods), L-395 (the check's move) and L-440 (the dashboard) closed.\n"
         '> - The dashboard search: each word on its own, in any order; more\n'
         '>   words narrow the list.\n'
         '>\n'
         "> **Do next:** *The master plan's restamp, from its brief; then the\n"
         '> objects-to-website design session (both in Where the details are).*\n'
         '>\n'
         '> **Needs you now:**\n'
         '> - *Run patch_L440_2, then the maintenance run (Dashboard parity,\n'
         '>   10 of 10 faults caught); try the search; push.*\n'
         '\n'
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 32: dashboard (L-440) built; L-424, L-425, L-426 ',
     (
         '  5b.  [NOW]   The scaffolding checks clear beside the slices: the\n'
         '               dashboard (L-440) built; L-424, L-425, L-426 to come.\n'
         '  6.   [next]  The typed facts: the inner Oort cloud is drawn on the\n'
         '               website too. Left: the check.\n'
         '  6a.  [done]  *Orbital periods from JPL: all three builds; the\n'
         "               website's waits only on your run and your look.*\n"
         '               << moved this session\n'
     ),
     (
         '  5b.  [NOW]   The scaffolding checks clear beside the slices: the\n'
         '               dashboard (L-440) done; L-424, L-425, L-426 to come.\n'
         '  6.   [next]  The typed facts: the inner Oort cloud is drawn on the\n'
         '               website too. Left: the check.\n'
         '  6a.  [done]  *Orbital periods from JPL, in the orrery and on the\n'
         '               website; accepted at your look, Oct 14.*\n'
         '               << moved this session\n'
     )),
    ('documentation/WHERE_WE_ARE.md', "line 41: the orrery's run; your next run is the period",
     (
         '  8.   [done]  The served objects are checked against JPL Horizons, from\n'
         "               the orrery's run; your next run is the periods' first live test.\n"
         '               << moved this session\n'
         "  9.   [next]  The website's checks, in the order you confirmed:\n"
     ),
     (
         '  8.   [done]  The served objects are checked against JPL Horizons, from\n'
         "               the orrery's run; the periods passed live, Oct 14.\n"
         "  9.   [next]  The website's checks, in the order you confirmed:\n"
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 72: - Dashboard search: each word anywhere on a c',
     (
         '  website checks in your six headings; only the orrery opens a console. (Oct 13)\n'
         '- Scattered dots are placed by the orrery and stored for the website;\n'
     ),
     (
         '  website checks in your six headings; only the orrery opens a console. (Oct 13)\n'
         '- Dashboard search: each word anywhere on a card, in any order. (Oct 14)\n'
         '- Pluto-Charon\'s barycentre: "not yet fetched"; its period waits for\n'
         '  the objects work. (Oct 14)\n'
         '- Scattered dots are placed by the orrery and stored for the website;\n'
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 77: - Comets by first apparition, oldest first. A',
     (
         '  drawn orbit and markers alike; typed table last, marked. (Oct 11)\n'
         '- Comets by first apparition, oldest first. A colour tells bodies\n'
         '  apart; not the default goldenrod. (Oct 10)\n'
         '- Fuzzy boundaries come before the Sun and Earth rooms close. Every\n'
         '  new check gets its dashboard button. (Oct 10)\n'
         '- The Hills cloud follows its paper (Fig. 3, its text), cited; to 10,000 AU. (Oct 10)\n'
     ),
     (
         '  drawn orbit and markers alike; typed table last, marked. (Oct 11)\n'
         '- Comets by first apparition, oldest first. Fuzzy boundaries before\n'
         '  the Sun and Earth rooms close. Every new check gets a button. (Oct 10)\n'
         '- The Hills cloud follows its paper (Fig. 3, its text), cited; to 10,000 AU. (Oct 10)\n'
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 88: - Last cache build: 20261014T175225Z, ok, no ',
     (
         'Read from files when this page was written, not typed from memory.\n'
         '- Last cache build: 20261014T175225Z, ok, no retry (gallery 4b2b660a).\n'
         '- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 5cd63cce).\n'
         '  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n'
     ),
     (
         'Read from files when this page was written, not typed from memory.\n'
         '- Last cache build: 20261014T225537Z, ok, no retry (gallery 86ef2df).\n'
         '- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 5ca56df).\n'
         '  Whole tree: 280: orrery 116, Earth System 149, stars 13, utilities 2.\n'
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 93: ## Waiting on you',
     (
         '\n'
         '## Waiting on you\n'
         '\n'
     ),
     (
         '\n'
         '## Waiting on you  **>> UPDATED THIS SESSION**\n'
         '\n'
     )),
    ('documentation/WHERE_WE_ARE.md', 'line 110: 4. The dashboard\'s "when" index: L-441, recor',
     (
         '3. The orrery from your phone: L-436 (away from the machine), an idea.\n'
         '\n'
     ),
     (
         '3. The orrery from your phone: L-436 (away from the machine), an idea.\n'
         '4. The dashboard\'s "when" index: L-441, recorded for later.\n'
         '\n'
     )),
    ('documentation/WHERE_WE_ARE.md', "line 115: - *Build 3 and the check's move, with the run",
     (
         '  typed facts), its check.\n'
         "- *Build 3 and the check's move, with the run order:\n"
         '  `HANDOFF_L431_build3_website_20261014.md`*\n'
         "- Orbital periods: rulings `DESIGN_L431_..._rulings_20261011.md`; build 2's\n"
     ),
     (
         '  typed facts), its check.\n'
         '- *Next: `HANDOFF_master_plan_restamp_brief_20261013.md`, then\n'
         '  `HANDOFF_L438_objects_to_website_brief_20261013.md`*\n'
         "- Build 3 and the check's move: `HANDOFF_L431_build3_website_20261014.md`\n"
         "- Orbital periods: rulings `DESIGN_L431_..._rulings_20261011.md`; build 2's\n"
     )),
    ('documentation/HANDOFF_L431_build3_website_20261014.md', 'line 268: ## 9. After the run (2026-10-14, evening)',
     (
         '\n'
         "Session written October 2026 with Anthropic's Claude Opus 5.5.\n"
     ),
     (
         '\n'
         '## 9. After the run (2026-10-14, evening)\n'
         '\n'
         'Added by `patch_L440_2_word_order_search_20261014.py`, built on orrery\n'
         '5ca56df at https://github.com/tonylquintanilla/palomas_orrery and read\n'
         'against gallery 86ef2df at\n'
         'https://github.com/tonylquintanilla/tonyquintanilla.github.io.\n'
         '\n'
         '- Your run record (`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`\n'
         '  at 5ca56df) shows every step green: the orrery run 30 of 30 twice, the\n'
         "  website's 27 of 27 twice, the cache swapped in first time. The Horizons\n"
         '  check reached JPL and passed for Mercury, Jupiter and Encke: the first\n'
         "  live test of the period comparison, and of Encke's query sent with\n"
         '  %3B.\n'
         "- Your look said yes to every line, Pluto's barycentre included, which\n"
         '  answers section 2: it ships saying "not yet fetched from JPL".\n'
         "- L-431, L-395 and L-440 are closed in the ledger. L-440's later slice,\n"
         '  the dashboard\'s "when" index, is L-441.\n'
         "- The live check's output is not in the record; nothing waits on it.\n"
         '\n'
         "Session written October 2026 with Anthropic's Claude Opus 5.5.\n"
     )),
]

CREATED = {
}



def _zone_hit(text, pos, length):
    spans = []
    for a, b in ZONES:
        if a in text and b in text:
            spans.append((text.index(a), text.index(b) + len(b)))
    if MARKER in text:
        spans.append((text.index(MARKER), len(text)))
    for s, e in spans:
        if pos < e and pos + length > s:
            return True
    return False


def apply():
    print('%s' % os.path.basename(__file__))
    print('Running in: %s' % ROOT)
    print()
    for f in MUST_EXIST:
        if not os.path.exists(os.path.join(ROOT, f)):
            print('ERROR: %s is not here. Save this script in the orrery repo\'s ROOT '
                  'folder and run it there. NOTHING was written.' % f)
            return None
    for f in CREATED:
        if os.path.exists(os.path.join(ROOT, f)):
            print('ERROR: %s already exists; this patch has run. NOTHING was written.' % f)
            return None
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return None
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-45s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            return None
        if _zone_hit(t, t.index(old), len(old)):
            print('ANCHOR FAIL  %-45s %s lies in a generated zone or below the run-record '
                  'marker. NOTHING was written.' % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, t in list(texts.items()) + list(CREATED.items()):
        if any(ord(c) > 127 for c in t):
            print('ERROR: %s would hold non-ASCII after this patch. NOTHING was written.' % f)
            return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, t in CREATED.items():
        d = os.path.dirname(os.path.join(ROOT, f))
        if d and not os.path.isdir(d):
            os.makedirs(d)
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in CREATED:
        print('ok  %-45s created' % f)
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files)' % (len(done), len(texts)))
    print('Stamps updated: the dashboard, Dashboard parity, the maintenance run,')
    print('the ledger, Where We Are.')
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect "Dashboard parity ... PASS --')
    print('     10 of 10 planted faults caught" and every gating checker to pass.')
    print('     "Ledger index" moves L-431, L-395 and L-440 to the closed section.')
    print('  2. Open the dashboard and try the search: "pull objects export" and')
    print('     "objects export pull" both find Objects Export Pull.')
    print('  3. Move this script into documentation/; commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
