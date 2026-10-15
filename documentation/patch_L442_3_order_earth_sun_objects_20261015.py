#!/usr/bin/env python3
"""
patch_L442_3_order_earth_sun_objects_20261015.py -- Tony's ruling of
2026-10-15 on the order: finish Earth, finish the Sun, then the objects.

Domain: dev_tools
Role: dev_tools

Built on orrery ffd6c36a1546d844987d2b36aaee510225d2d64b at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched.
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN: save this file in the orrery folder
(C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
open it in VS Code and click Run. Run it BEFORE the L-444 build session's
patch: both edit Where We Are, and this one is small.

WHAT IT DOES, in two files, all or nothing:
  LEDGER_CONSOLIDATED.md     L-443 waits for the Earth and Sun slices to
                             close (a Note and its Gap); header stamp
  documentation/WHERE_WE_ARE.md   above the marker only: Do next, road
                             stage 11 back to [later], one Settled line,
                             the Next pointer

It checks each file only at the lines it edits. Every anchor must match
exactly once, or nothing is written.

Undo is Discard Changes in GitHub Desktop.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = 'LEDGER_CONSOLIDATED.md'
WWA = 'documentation/WHERE_WE_ARE.md'
MARKER = '--- Your run record below this line'


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError('missing file: %s' % rel)
    raw = open(path, 'rb').read()
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), (b'\r\n' in raw)


def rep(text, old, new, label, log, fname):
    n = text.count(old)
    if n != 1:
        raise PatchError('ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r'
                         % (fname, label, n, old[:70]))
    log.append('ok  %-14s %s' % (fname, label))
    return text.replace(old, new)


QUOTE = ('"No. Let\'s stick to the pan. Finish earth, finish the sun, proceed\n'
         '  to objects."')

LEDGER_EDITS = [
    ('L-443 waits', '''**Gap:** the design session, from the brief: measure, propose the
slices and the mechanism, and build the first slice only after Tony's
word.''', '''- **Tony's ruling, 2026-10-15, in the coordination session** (asked
  whether to run this item's design session before the Sun's list, to
  size the objects by kind and build one cheap batch first):
  ''' + QUOTE + ''' ("pan" is "plan".) So this item, its design
  session included, waits until Earth's list (L-413) and the Sun's list
  (L-412) are worked through. L-444 (the missing periods) still goes
  first; its brief was already written.
**Gap:** after the Earth and Sun slices close: the design session, from
the brief: measure, propose the slices and the mechanism, and build the
first slice only after Tony's word.'''),
    ('header stamp', 'Review and RICE update Tony 6-21-2026\n',
     '''Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5
(L-443 waits for the Earth and Sun slices, Tony's ruling of the order),
built on ffd6c36a.
Review and RICE update Tony 6-21-2026
'''),
]

WWA_EDITS = [
    ('Do next', '''> **Do next:** *Build L-444 (the missing periods): small, orrery only.
> Then the design session for L-443 (the objects to the website).*''',
     '''> **Do next:** *Build L-444 (the missing periods). Then finish Earth's
> list, then the Sun's; the objects come after (your ruling, Oct 15).*'''),
    ('road: stage 11', ''' 11.   [next]  The rest of the orrery's objects come to the website:
               L-443 (the objects to the website), design first.
''', ''' 11.   [later] The rest of the orrery's objects come to the website:
               L-443 (the objects to the website), after the Sun and
               Earth rooms close.  << moved this session
'''),
    ('settled: the order', '''- Comets by first apparition, oldest first. Fuzzy boundaries before
  the Sun and Earth rooms close. Every new check gets a button. (Oct 10)
''', '''- The order: finish Earth, then the Sun (fuzzy boundaries inside
  it), then the objects; no batch of objects first. (Oct 15)
'''),
    ('details: next', '''- *Next: L-444 (the missing periods) in the ledger, then
  `HANDOFF_L438_objects_to_website_brief_20261013.md`, now L-443*''',
     '''- *Next: `HANDOFF_L444_missing_periods_brief_20261014.md`*'''),
]


def main():
    log = []
    try:
        led, led_crlf = read(LEDGER)
        if '#### [L-443]' not in led or '#### [L-444]' not in led:
            raise PatchError('REFUSED: L-443 and L-444 must exist; run patch_L442_2 first')
        for label, old, new in LEDGER_EDITS:
            led = rep(led, old, new, label, log, 'LEDGER')
        wwa, wwa_crlf = read(WWA)
        if wwa.count(MARKER) != 1:
            raise PatchError('ANCHOR FAIL [WHERE_WE_ARE run-record marker]')
        m = wwa.index(MARKER)
        top, bottom = wwa[:m], wwa[m:]
        for label, old, new in WWA_EDITS:
            top = rep(top, old, new, label, log, 'WHERE_WE_ARE')
        above = top.count('\n')
        if above > 130:
            raise PatchError('WHERE_WE_ARE would stand %d lines above the marker (cap 130)' % above)
        log.append('ok  %-14s %d lines above the marker (cap 130)' % ('WHERE_WE_ARE', above))
        wwa = top + bottom
        for rel, t in ((LEDGER, led), (WWA, wwa)):
            if any(ord(ch) > 127 for ch in t):
                raise PatchError('%s: non-ASCII after the edits' % rel)
    except PatchError as e:
        print('ERROR: %s' % e)
        print('NOTHING was written.')
        sys.exit(1)
    for line in log:
        print(line)
    for rel, t, crlf in ((LEDGER, led, led_crlf), (WWA, wwa, wwa_crlf)):
        open(os.path.join(ROOT, rel), 'wb').write(t.encode('utf-8'))
        if crlf:
            print('note: %s was CRLF in the working copy; written LF' % rel)
    print()
    print('patch applied (%d edits in 2 files)' % len(log))
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py (it rebuilds the ledger index).')
    print('  2. Move this script into documentation/; commit and push.')
    print('  3. Then start the L-444 build session from its prompt.')
    print('Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
