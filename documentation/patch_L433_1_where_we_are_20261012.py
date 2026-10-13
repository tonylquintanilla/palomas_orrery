"""patch_L433_1_where_we_are_20261012.py -- Where We Are, after the six
rulings of October 12, 2026 (L-433 the road; also L-136, L-424, L-425,
the dashboard's labels, the Horizons check's clearing rule).

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery, AS LEFT BY
patch_L401_4_look_close_20261012.py. Run that patch first; this one
refuses until it has. The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 12, 2026 with Anthropic's Claude Fable 5.1.
Record: documentation/DESIGN_rulings_20261012.md.

HOW TO RUN
    From the orrery repo's ROOT folder, after patch_L401_4: open this
    file in VS Code and press Run, or from a terminal in that folder:
        python patch_L433_1_where_we_are_20261012.py
    Success prints one "ok" line per edit, then "patch applied". It
    touches one file and contacts nothing.

WHAT IT CHANGES
    documentation/WHERE_WE_ARE.md, by section, never below the
    run-record marker:
      the header line; the READ THIS FIRST box (six rulings, four
      briefed sessions, what to run); the road (stage 5b added, stages
      7, 13 and 14 reworded to the confirmed order); Settled (four
      lines of Oct 12); Waiting on you (three items decided and
      removed); Where the details are (the record and the four briefs).
    The page stays within its cap: 130 lines above the marker.

SAFETY
    Every anchor must match exactly once and lie above the run-record
    marker, and the brief patch_L401_4 creates must already exist. If
    any check fails, NOTHING is written. A file found with Windows line
    endings is matched after turning them into LF and written back LF,
    and the patch says so. Undo is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join('documentation', 'WHERE_WE_ARE.md')
MARKER = '--- Your run record below this line'
REQUIRES = os.path.join('documentation',
                        'HANDOFF_L395_horizons_check_move_brief_20261012.md')
CAP = 130

EDITS = [
    ('header: Last updated',
     "Last updated: October 12, 2026, at your look at L-401's build 1.\n",
     "Last updated: October 12, 2026, evening: six rulings made in chat.\n"),
    ('box: changed, do next, needs you now',
     "> **Changed since you last read this:**\n"
     "> - L-401 (the distance digits), build 1: your look is done. Three\n"
     ">   fixes from it: the surface line is back for every centre, a planet's\n"
     ">   period no longer names the small-body database, and the sky\n"
     ">   position sits under one heading.\n"
     "> - The Horizons check moves into the orrery's maintenance run, beside\n"
     ">   the export. Its brief is written, for its own session.\n"
     ">\n"
     "> **Do next:** *L-431 (orbital periods) build 2, the drawn orbits and\n"
     "> markers.*\n"
     ">\n"
     "> **Needs you now:**\n"
     "> - *Orrery: run patch_L401_4, the maintenance run; hover Io from\n"
     ">   Jupiter once (the sky heading, the surface line); push.*\n"
     "> - *Decide L-425 (citation location checks): which checks to build,\n"
     ">   on the run's results (on L-425 and in the handoff).*\n",
     "> **Changed since you last read this:**\n"
     "> - L-401 (the distance digits), build 1: your look is done; its\n"
     ">   three fixes are in patch_L401_4.\n"
     "> - Six rulings in chat, away from your machine, clear the design-talk\n"
     ">   list: the road after the rooms, the scattered disk, L-424, L-425,\n"
     ">   the dashboard's labels, the Horizons check's clearing rule.\n"
     ">\n"
     "> **Do next:** *L-431 (orbital periods) build 2, the drawn orbits and\n"
     "> markers; the four briefed sessions beside it, in your order.*\n"
     ">\n"
     "> **Needs you now:**\n"
     "> - *Orrery: run patch_L401_4, then patch_L433_1 (this page), the\n"
     ">   maintenance run; hover Io from Jupiter once; commit the new\n"
     ">   documentation files; push.*\n"),
    ('road: stage 5b added',
     "               remaining items, in your order.* << moved this session\n"
     "  6.   [next]  The typed facts: the inner Oort cloud is drawn on the\n",
     "               remaining items, in your order.* << moved this session\n"
     "  5b.  [NOW]   *The scaffolding checks (L-424, L-425, L-426, the\n"
     "               dashboard) clear beside the slices, not after.* << new\n"
     "  6.   [next]  The typed facts: the inner Oort cloud is drawn on the\n"),
    ('road: stage 7',
     "  7.   [next]  The Sun's numbers get the checking Earth's got.\n",
     "  7.   [next]  The Sun's numbers get the checking Earth's got; the Solar\n"
     "               System room's features close with these rooms. << changed\n"),
    ('road: stages 13 and 14',
     " 13.   [later] The planets get their details, Jupiter and Saturn first;\n"
     "               you lean to the inner planets (L-433).\n"
     " 14.   [later] The Earth System layers; the gallery's cards meanwhile.\n",
     " 13.   [later] The inner planets' rooms (Mercury, Venus, Mars), from the\n"
     "               template; Jupiter and Saturn follow (L-433). << changed\n"
     " 14.   [later] The Earth System layers, beside 13, not after it; the\n"
     "               gallery's cards meanwhile. << changed\n"),
    ('settled: four lines of Oct 12',
     "- The Horizons check lives in the orrery's maintenance run, beside the\n"
     "  export; the website's daily check reads its dates. (Oct 12)\n",
     "- The Horizons check lives in the orrery's maintenance run, beside the\n"
     "  export; the website's daily check reads its dates. A changed sheet\n"
     "  goes red only when the figure a row quotes changed. (Oct 12)\n"
     "- A checker's word names its case: two words for a moved value. The\n"
     "  citation location checks: all three levels now. (Oct 12)\n"
     "- The scattered disk: yes, in the Solar System room, after fuzzy\n"
     "  boundaries. A dashboard button is named what the run prints. (Oct 12)\n"),
    ('waiting: three items decided',
     "At the next design talk:\n"
     "- Your order after the Sun and Earth rooms (L-433), in your words of\n"
     "  Oct 10; the road changes when you confirm it.\n"
     "- L-424 (the checker's one word for two cases): you marked it\n"
     "  \"unclear\" (Oct 10). I explain it in plain words, then you decide.\n"
     "- The scattered disk, with the Kuiper belt (L-136): \"we should\n"
     "  decide this. i lean yes.\" (Oct 10)\n"
     "- The fuzzy outer corona",
     "At the next design talk:\n"
     "- The fuzzy outer corona"),
    ('details: periods and digits, shorter',
     "- Orbital periods: rulings\n"
     "  `documentation/DESIGN_L431_orbital_periods_rulings_20261011.md`;\n"
     "  build 1 `documentation/HANDOFF_L431_period_build1_20261011.md`\n"
     "- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n"
     "  the reviews `REVIEW_L401_distance_digits_comparison_20261011.md`;\n"
     "  build 1 `documentation/HANDOFF_L401_distance_build1_20261012.md`\n",
     "- Orbital periods: `DESIGN_L431_orbital_periods_rulings_20261011.md`;\n"
     "  build 1 `HANDOFF_L431_period_build1_20261011.md`\n"
     "- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;\n"
     "  reviews `REVIEW_L401_..._comparison_20261011.md`; build 1\n"
     "  `HANDOFF_L401_distance_build1_20261012.md`\n"),
    ('details: the record and the briefs',
     "- The citation checks: L-425 (citation location checks), L-426 (the\n"
     "  checker's small-number comparison); `HANDOFF_L418_testing_20261009.md`\n",
     "- Your six rulings of Oct 12: `DESIGN_rulings_20261012.md`; the briefs\n"
     "  `HANDOFF_dashboard_labels_brief_20261012.md` (and its audit),\n"
     "  `..._L425_citation_locations_brief_...`, `..._L424_L426_worksheet_checker_brief_...`\n"),
    ('details: inner Oort cloud, shorter',
     "- The inner Oort cloud: design\n"
     "  `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`; records\n"
     "  `HANDOFF_L421_oort_orrery_20261010.md`, `..._gallery_20261011.md`\n",
     "- The inner Oort cloud: `DESIGN_L421_inner_oort_tilt_20261009.md`;\n"
     "  `HANDOFF_L421_oort_orrery_20261010.md`, `..._gallery_20261011.md`\n"),
]


def main():
    if not os.path.exists(os.path.join(ROOT, REQUIRES)):
        print('ERROR: %s not found. Run patch_L401_4_look_close_20261012.py '
              'first; this patch is built on the page as it leaves it. '
              'NOTHING was written.' % REQUIRES)
        return 1
    path = os.path.join(ROOT, PAGE)
    if not os.path.exists(path):
        print('ERROR: %s not found in %s. NOTHING was written.' % (PAGE, ROOT))
        return 1
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    text = raw.replace(b'\r\n', b'\n').decode('utf-8')
    if MARKER not in text:
        print('ERROR: the run-record marker is missing from %s. NOTHING was written.' % PAGE)
        return 1
    done = []
    for label, old, new in EDITS:
        n = text.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-40s (found %d times, expected 1). NOTHING was written.'
                  % (label, n))
            return 1
        if text.index(old) > text.index(MARKER):
            print('ANCHOR FAIL  %-40s lies below the run-record marker. NOTHING was written.'
                  % label)
            return 1
        if any(ord(c) > 127 for c in new):
            print('ERROR: edit %r would add non-ASCII. NOTHING was written.' % label)
            return 1
        text = text.replace(old, new)
        done.append(label)
    above = text[:text.index(MARKER)].count('\n')
    if above > CAP:
        print('ERROR: the page would have %d lines above the marker; the cap is %d. '
              'NOTHING was written.' % (above, CAP))
        return 1
    with open(path, 'w', encoding='utf-8', newline='') as h:
        h.write(text)
    for label in done:
        print('ok  %-40s' % label)
    if crlf:
        print('note: %s was CRLF in the working copy; written LF' % PAGE)
    print()
    print('patch applied (%d edits in 1 file); %d lines above the marker (cap %d)'
          % (len(done), above, CAP))
    print('Stamp updated: the page\'s "Last updated" line.')
    print()
    print('NEXT:')
    print('  1. Paste this output into your run record.')
    print('  2. Run orrery_maintenance_run.py as patch_L401_4 asked.')
    print('  3. Commit, with the five new files in documentation/ (the rulings')
    print('     record, the audit, the three briefs); move this script and')
    print('     patch_L401_4 into documentation/; push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
