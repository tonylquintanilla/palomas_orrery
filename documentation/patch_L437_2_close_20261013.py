"""patch_L437_2_close_20261013.py -- L-437 closed on Tony's run: the
whole-tree Tier-1 total prints with its domains, as predicted.

Built on orrery f59c84b2d00ccdb0d5fb8fcf2c5d075189cf9c72 at
https://github.com/tonylquintanilla/palomas_orrery ("L437 tier 1 L269").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Record: section 11 of documentation/HANDOFF_L437_tier1_by_domain_20261013.md
(added by this patch). Tony's run is read from
documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md.

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L437_2_close_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing. A second run finds its anchors gone and
    writes nothing.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md: L-437 marked DONE (the maintenance run's
      Ledger index then moves it to section C); a Note on L-269 about
      its unrun patch; one stamp line in the header.
    documentation/WHERE_WE_ARE.md: the Signals line only, read from your
      run's audit. Nothing below the run-record marker.
    documentation/HANDOFF_L437_tier1_by_domain_20261013.md: section 11,
      your run and the close.
    No code, skill or protocol changes.

SAFETY
    Every anchor is a line this patch alone changes, matched exactly
    once; nothing is fingerprinted whole, so your notes cannot make it
    refuse. If any check fails, NOTHING is written. A file found with
    Windows line endings is matched after turning them into LF and
    written back LF, and the patch says so. Undo after a run is Discard
    Changes in GitHub Desktop.

Role: patch
Domain: dev_tools
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'
CAP = 130
RUN_RECORD = 'documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md'

L437_CLOSE = '''- **Closed 2026-10-13 on Tony's run** (run record
  `documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`). The patch
  applied: 69 edits in 11 files and 2 new files. The maintenance run
  passed 26 of 26 gating checkers, Domain Split 6 of 6 planted faults.
  The scanner row read "0 TIER-1 -- the push gate holds; Whole tree,
  Tier-1: 281: orrery 116, Earth System 149, stars 13, utilities 2,
  unclassified 1.", as predicted. It rewrote the Skill Manifest to
  provenance-discipline 2.29. Pushed at f59c84b2.
- **Loose ends, re-homed.** The GATING AND REPORT-ONLY count in
  orrery_maintenance_run.py, which reads twenty-five while the run has
  twenty-six gating checkers, went to L-269, whose unrun patch edits
  that sentence (L-269's Note of this date, which also says why that
  patch refuses). L-183's and L-163's lines need no work: no module is
  mapped by hand any more.
- **The obligation travels.** provenance-discipline went to 2.29 in
  this item's patch; this session loaded 2.28. The next session
  confirms its loaded copy reads 2.29 before provenance work.
**Ref:**'''

L269_NOTE = '''- **Note (2026-10-13, from L-437's close):**
  `patch_L269_1_scanner_breakdown_20261013.py` was built on 70202e3b and
  sits unrun in the root at f59c84b2. L-437 (the whole-tree Tier-1 with
  its domains) was run first, so four of its anchors no longer match --
  the maintenance run's docstring end, the Orbit markers row, the
  dashboard's docstring end and the ledger's header stamp -- and it
  refuses and writes nothing. Re-anchored as it is, its whole-tree line
  would print a second copy of the split that L-437 already puts on the
  scanner's row. The half L-437 does not do is the other one: naming
  each file whose Tier-1 rose, in the summary. So the redelivery keeps
  the risen-files half, drops the whole-tree line, and restates the
  GATING AND REPORT-ONLY count, which reads twenty-five while the run
  has twenty-six gating checkers since L-437.

'''

STAMP = '''Module updated: October 13, 2026 with Anthropic's Claude Opus 5.5
(L-437 closed on Tony's run; a Note on L-269's unrun patch), built on
f59c84b2.
'''

SIGNALS_OLD = '''- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 70202e3b).
  Whole tree: 281: orrery 116, Earth System 149, stars 13, utilities 2,
  unclassified 1 (domain-split pre-test; the 1 is unrun patch_L436_1).
'''
SIGNALS_NEW = '''- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, f59c84b2).
  Whole tree: 281: orrery 116, Earth System 149, stars 13, utilities 2,
  unclassified 1 (your run; the 1 is patch_L436_1, still in the root).
'''

HANDOFF_11 = '''## 11. Your run, and the close

Added by `patch_L437_2_close_20261013.py`, built on f59c84b2 (this
build's patch run and pushed).

Read from your run record,
`documentation/WHERE_WE_ARE_10-12-26_2212_run_record.md`:
- The patch applied: 69 edits in 11 files and 2 new files.
- The maintenance run passed 26 of 26 gating checkers. Domain Split:
  "PASS -- 6 of 6 planted faults caught". The scanner row: "0 TIER-1 --
  the push gate holds; Whole tree, Tier-1: 281: orrery 116, Earth System
  149, stars 13, utilities 2, unclassified 1." Exactly as predicted.
- You reinstalled provenance-discipline 2.29, copied the instructions
  to v3.95 and pushed at f59c84b2.

L-437 is DONE. The maintenance run's Ledger index moves its block to
section C.

**The L-269 patch in your root folder will refuse.** It was built on
70202e3b beside this one, and this one ran first. Four of its anchors
moved: the maintenance run's docstring end, the Orbit markers row, the
dashboard's docstring end, and the ledger's header stamp. It writes
nothing when it refuses, so running it is safe, but it does nothing.

Half of it is now a duplicate. It reads the scanner's per-domain
console lines and prints a whole-tree line under the scanner's row;
L-437 already prints that line, on the row itself. The other half --
naming each file whose Tier-1 rose since the previous run -- L-437 does
not do, and it is worth keeping. A note for its session, also on L-269
in the ledger:

    patch_L269_1 refuses at f59c84b2 on four anchors (the maintenance
    run's docstring end, the Orbit markers row, the dashboard's
    docstring end, the ledger's header stamp): L-437 ran first. L-437
    already quotes "Whole tree, Tier-1: 281: orrery 116, ..." on the
    Provenance scanner row. Re-anchor on f59c84b2, keep the risen-files
    lines, drop the whole-tree line, and restate the GATING AND
    REPORT-ONLY count, which says twenty-five while the run has
    twenty-six gating checkers.

The obligation travels: provenance-discipline 2.29 was installed during
this session, which loaded 2.28. The next session confirms its loaded
copy reads 2.29 before provenance work.

For Tony:
- (do) Run `patch_L437_2_close_20261013.py`, then
  `orrery_maintenance_run.py` (it moves L-437 into section C); move the
  patch into `documentation/`; commit and push.
- (do) When you next open the L-269 session, paste it the note above.

'''

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header: one stamp line',
     'Review and RICE update Tony 6-21-2026\n',
     STAMP + 'Review and RICE update Tony 6-21-2026\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-437 title: DONE',
     "#### [L-437] The whole-tree Tier-1 total prints with its domains; a module's domain has one home (provenance tooling)\n",
     "#### [L-437] The whole-tree Tier-1 total prints with its domains; a module's domain has one home (provenance tooling, DONE 2026-10-13)\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-437 status: DONE, section C',
     '<!-- L:437 status:OPEN upd:2026-10-13 section:A flag: rice: -->\n',
     '<!-- L:437 status:DONE upd:2026-10-13 section:C flag: rice: -->\n'),
    ('LEDGER_CONSOLIDATED.md', 'L-437: the run, the loose ends',
     '''**Gap:** Tony runs the patch and the maintenance run; reads the scanner
row and the audit's Priority Summary; pushes. Then DONE.
**Tony-action (do):** run `patch_L437_1_tier1_by_domain_20261013.py`,
then `orrery_maintenance_run.py`; reinstall provenance-discipline 2.29;
copy PROJECT_INSTRUCTIONS.md (v3.95) to the Project's instructions and
to `documentation/project_instructions_v3_95.md`; move the patch into
`documentation/`; commit and push.
**Ref:**''', L437_CLOSE),
    ('LEDGER_CONSOLIDATED.md', 'L-269: a Note on its unrun patch',
     '\n#### [L-281] The guest book: no-account comments, approve-before-show\n',
     '\n' + L269_NOTE.rstrip('\n') + '\n\n#### [L-281] The guest book: no-account comments, approve-before-show\n'),
    ('documentation/WHERE_WE_ARE.md', 'Signals: the Tier-1 line, from your run',
     SIGNALS_OLD, SIGNALS_NEW),
    ('documentation/HANDOFF_L437_tier1_by_domain_20261013.md', 'section 11: your run and the close',
     "Session record written October 2026 with Anthropic's Claude Opus 5.5.\n",
     HANDOFF_11 + "Session record written October 2026 with Anthropic's Claude Opus 5.5.\n"),
]


def apply():
    if not os.path.exists(os.path.join(ROOT, RUN_RECORD)):
        print('ERROR: %s not found in %s. NOTHING was written.' % (RUN_RECORD, ROOT))
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
            if n == 0 and 'status:DONE upd:2026-10-13 section:C' in texts.get('LEDGER_CONSOLIDATED.md', ''):
                print('It looks as though this patch has already run.')
            return None
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-45s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, label, old, new in EDITS:
        if any(ord(c) > 127 for c in new):
            print('ERROR: an edit to %s would add non-ASCII. NOTHING was written.' % f)
            return None
    page = texts['documentation/WHERE_WE_ARE.md']
    above = page[:page.index(MARKER)].count('\n')
    if above > CAP:
        print('ERROR: WHERE_WE_ARE.md would have %d lines above the marker (cap %d). '
              'NOTHING was written.' % (above, CAP))
        return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-55s %s' % (f, label))
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files)' % (len(done), len(texts)))
    print('Stamps updated: the ledger; the handoff gains section 11.')
    print('WHERE_WE_ARE.md: %d lines above the run-record marker (cap %d).' % (above, CAP))
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Its Ledger index moves L-437 into')
    print('     section C. Nothing else should change: every gating checker passes.')
    print('  2. Move this script into documentation/; commit and push.')
    print('  3. patch_L269_1 in this folder will refuse (four anchors moved under it).')
    print('     When you next open its session, paste it the note in section 11 of')
    print('     documentation/HANDOFF_L437_tier1_by_domain_20261013.md.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
