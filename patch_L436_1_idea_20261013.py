"""patch_L436_1_idea_20261013.py -- opens L-436, an idea recorded on first
mention: the orrery away from Tony's machine (the linked session from
the phone; why not Pyodide; the two routes that fit).

Built on orrery 28e1b7d at
https://github.com/tonylquintanilla/palomas_orrery ("maintenance", after
L-437's close). Re-anchored 2026-10-13 15:10 from 87a5470: its ledger
header anchor had moved under two L-437 stamps; nothing else changed. The gallery
is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Fable 5.1.
Record: documentation/DESIGN_L436_orrery_away_from_the_machine_20261013.md,
which arrives with this patch and must already be in the folder.

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L436_1_idea_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It
    touches two files and contacts nothing.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md: a new block, L-436, at the end of section
        D.Feature-C (Bucket C, architecture); one stamp line in the
        header. The index zone is left alone; the maintenance run's
        Ledger index rebuilds it.
    documentation/WHERE_WE_ARE.md: one line under "Not urgent, in your
        order", and one under Where the details are; three lines
        shortened elsewhere so the page stays at its 130-line cap.
        Nothing below the run-record marker.

SAFETY
    Other sessions are building beside this one (the dashboard's
    labels; the scaffolding sessions). Every anchor here is a line
    this patch alone changes, matched exactly once; nothing is
    fingerprinted whole. If any anchor fails, NOTHING is written. A
    file found with Windows line endings is matched after turning
    them into LF and written back LF, and the patch says so. Undo is
    Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'
RECORD = os.path.join('documentation',
                      'DESIGN_L436_orrery_away_from_the_machine_20261013.md')
CAP = 130

L436 = '''#### [L-436] The orrery away from the machine: the linked session from the phone; not Pyodide (idea)
<!-- L:436 status:OPEN upd:2026-10-13 section:D.Feature-C flag: rice: -->
- **Opened 2026-10-13 on first mention, an idea and not a plan.** Tony,
  on what drives it: "i am often away from my machine." Three questions
  across 2026-10-12 and 13: could the dashboard be operated from the
  phone through the linked session; could a patch and the maintenance
  run be run that way, stopping at the push; could the orrery itself be
  run from the phone (the Sun, Mercury, Venus, Sedna and Voyager 1 at 0
  hours, the hovers read back); and could the orrery's window be
  converted to Pyodide to run it remotely.
- **What the linked session can do today** (measured in that session):
  read and write files in the repository folder (done: patches and
  briefs saved straight into it on 2026-10-12 and 13); run a command on
  the computer (not yet tried; the first test is the maintenance run
  alone). It cannot click a window, cannot see a render, and the push
  stays in GitHub Desktop by Tony's choice. So "run the patch and the
  maintenance run, stop at the push" works for the mechanical steps;
  the look (Mode 5) and the push wait for the machine.
- **Not Pyodide.** The window is tkinter and would be rebuilt as a page;
  Horizons does not permit a browser page to call it, so a relay would
  be hosted; the caches are hundreds of megabytes read from disk. The
  protocol's own words: the assembler exists because the orrery's Python
  requirement is a wall; the website IS the orrery running remotely,
  and stage 15 of the road is that goal. A port would be a second
  attempt at it with the hard parts left in.
- **Two routes that fit, if taken up:** a headless hover script in the
  orrery (names and a date in; the hovers printed through the same
  dispatch the plot uses; the HTML saved), which the linked session can
  run from the phone, giving the words and digits but not the render;
  and the website's rooms, which already open on the phone and which
  L-431 build 3 and stage 11 are filling.
  **Tony-action (decide, not urgent):** whether the hover script joins
  L-401 build 3's scope or waits. Default: waits; a convenience, not a
  slice.
  **Tony-action (do, when convenient):** the first command from the
  phone, the maintenance run alone, its output read back.
**Gap:** not scoped; an idea on record. Unscored until opened (an item
outside any list gets a coarse score then).
**Ref:** `documentation/DESIGN_L436_orrery_away_from_the_machine_20261013.md`;
PROJECT_INSTRUCTIONS.md, The Orrery and the Assembler; L-401 (build 3's
slices); L-431 (build 3, the website); L-363 (the Solar System room).

'''

EDITS = [
    ('LEDGER_CONSOLIDATED.md', 'header stamp',
     "(L-437 closed on Tony's run; a Note on L-269's unrun patch), built on\nf59c84b2.\nReview and RICE update Tony 6-21-2026\n",
     "(L-437 closed on Tony's run; a Note on L-269's unrun patch), built on\nf59c84b2.\nModule updated: October 13, 2026 with Anthropic's Claude Fable 5.1\n(L-436 opened: the orrery away from the machine, an idea on record),\nbuilt on 28e1b7d.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-436 block at the end of Bucket C',
     "**Gap:** add filedialog.askopenfilename to measure_animation_html.py.\n**Ref:** spun out of L-048 (closed 2026-06-23).\n\n### D.Parked",
     "**Gap:** add filedialog.askopenfilename to measure_animation_html.py.\n**Ref:** spun out of L-048 (closed 2026-06-23).\n\n" + L436 + "### D.Parked"),
    ('documentation/WHERE_WE_ARE.md', 'not urgent: L-436',
     "Not urgent, in your order:\n1. Whether the editor also edits the Solar System room's rows.\n2. Choosing a date, and animation.\n",
     "Not urgent, in your order:\n1. Whether the editor also edits the Solar System room's rows.\n2. Choosing a date, and animation.\n3. The orrery from your phone: L-436 (away from the machine), an idea.\n"),
    ('documentation/WHERE_WE_ARE.md', 'settled: the comets line, three lines to two',
     "- Comets listed by first apparition, oldest first. A colour is a\n  drawing choice, to tell apart bodies drawn together; switch it up\n  from the default goldenrod. (Oct 10)\n",
     "- Comets by first apparition, oldest first. A colour is a drawing\n  choice, to tell bodies apart; not the default goldenrod. (Oct 10)\n"),
    ('documentation/WHERE_WE_ARE.md', 'details: L-436 note, two lines made one',
     "- L-421 (typed facts, inner Oort): `MANIFEST_L421_typed_facts_20261006.md`,\n  `HANDOFF_L421_typed_facts_20261008.md`, `HANDOFF_L421_oort_*`\n",
     "- L-421 (typed facts, inner Oort): `MANIFEST_L421_typed_facts_20261006.md`, `HANDOFF_L421_*`\n- L-436 (away from the machine): `DESIGN_L436_orrery_away_from_the_machine_20261013.md`\n"),
]


def main():
    if not os.path.exists(os.path.join(ROOT, RECORD)):
        print('ERROR: %s not found. Save it beside this patch first. NOTHING was written.' % RECORD)
        return 1
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return 1
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
            if f == 'LEDGER_CONSOLIDATED.md' and '[L-436]' in texts[f]:
                print('ERROR: L-436 is already in the ledger; the handle is taken or this '
                      'patch has run. NOTHING was written.')
                return 1
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-28s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            return 1
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-28s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            return 1
        if any(ord(c) > 127 for c in new):
            print('ERROR: edit %r would add non-ASCII. NOTHING was written.' % label)
            return 1
        texts[f] = t.replace(old, new)
        done.append((f, label))
    page = texts['documentation/WHERE_WE_ARE.md']
    above = page[:page.index(MARKER)].count('\n')
    if above > CAP:
        print('ERROR: the page would have %d lines above the marker; the cap is %d. '
              'NOTHING was written.' % (above, CAP))
        return 1
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-28s %s' % (f, label))
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files); %d lines above the page marker (cap %d)'
          % (len(done), len(texts), above, CAP))
    print('Stamps updated: the ledger header.')
    print()
    print('NEXT:')
    print('  1. Paste this output into your run record.')
    print('  2. Run orrery_maintenance_run.py (the Ledger index rebuilds; L-436 appears')
    print('     in section D.Feature-C with no score).')
    print('  3. Move this script into documentation/; commit with the note; push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
