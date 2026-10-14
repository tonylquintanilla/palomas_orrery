"""patch_L431_9_close_20261013.py -- closes L-431's build 2 (orbital
periods: the drawn orbits and markers). Records only, no code.

Built on orrery 869b8c228d1c6cd104b50ca25b6056bbdb3e72e0 at
https://github.com/tonylquintanilla/palomas_orrery ("L276 L436").
The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L431_9_close_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md: on L-431, build 2 closed (accepted at your
      look; patch_L431_7 and patch_L431_8 run and pushed); build 3
      pointed at its brief; the line you confirmed, that the website
      needs a barycentre body's Sun-centred elements as well as its
      barycentre ones, which the patch_L431_8 you ran did not carry.
      L-431 stays OPEN. The header stamp.
    documentation/WHERE_WE_ARE.md, by section, never below the
      run-record marker: the header, the box, road stage 6a, and build
      3's brief under Where the details are.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, and no edit lands below the run-record
    marker, so your notes cannot make it refuse. If any check fails,
    NOTHING is written. A file found with Windows line endings is matched
    after turning them into LF and written back LF, and the patch says
    so. Undo after a run is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'line 395: Module updated: October 13, 2026 with Anthro',
     'built on 28e1b7d.\nReview and RICE update Tony 6-21-2026\n',
     "built on 28e1b7d.\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n(L-431: build 2 closed, accepted at Tony's look with its four fixes run;\nbuild 3 briefed), built on 869b8c22.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 1776: - **2026-10-13, build 2 CLOSED.** Accepted a',
     '  One class: what the word "mean" and the epoch field should say.\n**Gap:** three builds, in order (the record\'s section 3):\n',
     '  One class: what the word "mean" and the epoch field should say.\n- **2026-10-13, build 2 CLOSED.** Accepted at Tony\'s look, and all four\n  fixes from his saved plot are in: patch_L431_7 pushed at 400a9615,\n  patch_L431_8 at 4da3d7cc. Tony, closing it: "Build 2 is accepted at\n  my look." Build 3, the website, is briefed in\n  `documentation/HANDOFF_L431_build3_website_brief_20261013.md`\n  (written in the coordination session at 28e1b7d1).\n- **For build 3, confirmed by Tony and not yet in the brief\'s export\n  list.** A body drawn around the barycentre is placed in a Sun-centred\n  scene by pairing its two element sets at one date (horizons-orbital-\n  mechanics, The Drawn Orbit Follows the Period\'s Centre). The orrery\n  fetches its Sun-centred elements every time and keeps the barycentre\n  ones in the period record. So the website needs the Sun-centred\n  elements (or the body\'s Sun-centred position on that date) as well\n  as the barycentre ones, or it cannot place the orbit. Tony,\n  2026-10-13, asked whether the heliocentric data should also be\n  fetched; told it already is and that build 3 must export both:\n  "confirmed." The brief\'s section 2a lists only "the elements around\n  that centre". (This line was in a later copy of patch_L431_8 than the\n  one that ran.)\n**Gap:** three builds, in order (the record\'s section 3):\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 1801: (2026-10-13), and CLOSED: the three findings',
     "   (2026-10-13). The three findings from his saved plot are fixed in\n   patch_L431_7 (run, pushed at 400a9615); the perturbation lines are\n   removed for barycentre orbits in patch_L431_8, which waits for his run.\n3. The website, next: the export carries each period and the elements\n   around its centre; every room's hover prints it and draws the orbit\n   around that centre; the Horizons check compares it.\n",
     "   (2026-10-13), and CLOSED: the three findings from his saved plot\n   (patch_L431_7, pushed at 400a9615) and no perturbation lines for\n   barycentre orbits (patch_L431_8, pushed at 4da3d7cc).\n3. The website, NEXT, briefed in\n   `documentation/HANDOFF_L431_build3_website_brief_20261013.md`: the\n   export carries each period and the elements around its centre, and\n   for a barycentre body the Sun-centred elements too (above); every\n   room's hover prints it and draws the orbit around that centre; the\n   Horizons check compares it.\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 13, 2026, night: orbit',
     'Last updated: October 13, 2026, afternoon: no perturbation lines for Sedna.\n- Written at orrery 400a9615 and gallery 924977a3.\n',
     "Last updated: October 13, 2026, night: orbital periods' build 2 closed.\n- Written at orrery 869b8c22 and gallery 924977a3.\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 10: > - Orbital periods, build 2 (the drawn orbi',
     '> - Your look at the drawn orbits and markers: accepted ("bottom line:\n>   looks good").\n> - Fixes from your saved plot: Encke\'s white arc\'s accuracy line; the\n>   frame fits Sedna (1,030 au, not 1,104); by your ruling, no\n>   perturbation lines for orbits drawn around the barycentre.\n',
     '> - Orbital periods, build 2 (the drawn orbits and markers): accepted\n>   at your look and closed; all four fixes from your plot are in.\n'),
    ('documentation/WHERE_WE_ARE.md', "line 13: > **Do next:** *L-431's website build, from ",
     "> **Do next:** *L-431's website build, and the four briefed sessions\n> beside it, in your order.*\n",
     "> **Do next:** *L-431's website build, from its brief (in Where the\n> details are), and the briefed sessions beside it.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 17: > - *Run patch_L431_9 and the maintenance ru',
     "> - *Run patch_L431_8 and the maintenance run (25 of 25); reinstall\n>   horizons-orbital-mechanics 1.5; the Project's instructions to\n>   v3.94; move both patches into documentation/; push.*\n",
     '> - *Run patch_L431_9 and the maintenance run; move the patch into\n>   documentation/; push.*\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 33: 6a.  [NOW]   *Orbital periods from JPL: buil',
     '  6a.  [NOW]   *Orbital periods from JPL: builds 1 and 2 accepted, the\n               hovers, the drawn orbits and markers; the website next.*\n',
     '  6a.  [NOW]   *Orbital periods from JPL: builds 1 and 2 accepted and\n               closed; build 3, the website, briefed and next.*\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 115: look and fixes `HANDOFF_L431_build2_look_fix',
     '  look and fixes `HANDOFF_L431_build2_look_fixes_20261013.md`\n',
     "  look and fixes `HANDOFF_L431_build2_look_fixes_20261013.md`; build 3's\n  brief `HANDOFF_L431_build3_website_brief_20261013.md`\n"),
]



def apply():
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
            if n == 0 and 'build 2 CLOSED' in t:
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
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files)' % (len(done), len(texts)))
    print('Stamps updated: the ledger.')
    print()
    print('L-431 stays OPEN. Build 2 is closed; build 3, the website, is next, from')
    print('documentation/HANDOFF_L431_build3_website_brief_20261013.md.')
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py; it rebuilds the ledger index.')
    print('  2. Move this script into documentation/; commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
