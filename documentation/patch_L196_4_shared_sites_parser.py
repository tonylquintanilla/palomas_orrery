"""patch_L196_4_shared_sites_parser.py -- L-192 / L-196. Fixes the
extractor-pins break introduced by patch 3.

RUN COMMAND
-----------
Save into the palomas_orrery repo root, open in VS Code, click Run.

    python patch_L196_4_shared_sites_parser.py

Run AFTER patches 1, 2 and 3. It is built against the tree they leave.

WHAT WENT WRONG
---------------
Patch 3 added a RETIRED row to L192_annotated_sites.txt and taught
test_worksheet_keys.py to skip it. It did not check whether anything
else read that file. test_extractor_pins.py does, with its own copy of
the same parsing loop, and it crashed:

    ValueError: invalid literal for int() with base 10: '2026-08-16'

The format has two consumers and each carried its own parser. Teaching
one and not the other is the parallel-pipeline failure the protocol
names: when a violation appears in N consumers of the same producer,
fix the producer.

THE FIX
-------
parse_sites_doc() moves into worksheet_keys.py, which both test files
already import. Both consumers now point at it:

    parse_sites = wk.parse_sites_doc

Patching only test_extractor_pins.py would have unblocked the run in
one line and left the identical landmine for the third consumer -- and
there will be a third, because dispatch reads this corpus.

WHAT IS PERMANENT
-----------------
This script is disposable. What it installs is not: worksheet_keys.py
gains parse_sites_doc() and RETIRED_TAG as the single owner of the
sites-doc format, and two duplicate parsers are deleted.

MUTATION-TESTED
---------------
  a RETIRED row naming a fabricated site
    -> skipped, extractor pins still green (correct: RETIRED rows are
       records, not assertions -- the inverted assertion that gives
       them teeth lives with the key pins)
  the RETIRED tag misspelled as RETIREDX
    -> ValueError, exactly as before the fix (correct: the guard must
       catch the real tag and nothing else, or a typo would silently
       drop a live site)

SAFETY
------
All-or-nothing, fingerprinted, bottom-up, line endings preserved.
Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'worksheet_keys.py': {
        'fp': '0996e182554f4c172c68ceed9cf1d330',
        'edits': [
            (131, 130,
             [
             ],
             [
              '',
              '',
              "RETIRED_TAG = 'RETIRED'",
              '',
              '',
              'def parse_sites_doc(path):',
              '    """[(module, line, label)] from documentation/worksheets/L192_annotated_sites.txt.',
              '',
              '    One parser, because the format has more than one consumer. Both',
              '    test_worksheet_keys.py and test_extractor_pins.py read this file,',
              '    and each carried its own copy of this loop until a RETIRED row was',
              '    added for a deliberately retired key: the copy that had learned the',
              "    tag passed, the copy that had not crashed on int('2026-08-16').",
              '    Fixing the consumer that broke would have left the same landmine',
              '    for the third consumer. (2026-08-16)',
              '',
              '    A RETIRED row records why a site left the corpus and is skipped',
              '    here. The inverted assertion that gives it teeth lives with the',
              '    pins, in test_worksheet_keys.py -- this loader only has to not',
              '    choke on it.',
              '    """',
              '    sites = []',
              "    with open(path, encoding='utf-8') as handle:",
              '        for raw in handle:',
              "            raw = raw.rstrip('\\n')",
              "            if not raw.strip() or raw.startswith('#'):",
              '                continue',
              "            if raw.startswith(RETIRED_TAG + '\\t'):",
              '                continue',
              "            parts = raw.split('\\t')",
              '            if len(parts) >= 3:',
              '                sites.append((parts[0], int(parts[1]), parts[2]))',
              '    return sites',
             ]),
        ],
    },
    'test_worksheet_keys.py': {
        'fp': '71d7857b823243c0084e8f94bf9bec4e',
        'edits': [
            (137, 150,
             [
              'def parse_sites(path):',
              '    sites = []',
              "    with open(path, encoding='utf-8') as handle:",
              '        for raw in handle:',
              '            raw = raw.strip()',
              "            if not raw or raw.startswith('#'):",
              '                continue',
              "            if raw.startswith(RETIRED_TAG + '\\t'):",
              '                continue',
              "            parts = raw.split('\\t')",
              '            if len(parts) < 3:',
              '                continue',
              '            sites.append((parts[0], int(parts[1]), parts[2]))',
              '    return sites',
             ],
             [
              'parse_sites = wk.parse_sites_doc',
             ]),
            (85, 85,
             [
              "RETIRED_TAG = 'RETIRED'",
             ],
             [
              'RETIRED_TAG = wk.RETIRED_TAG',
             ]),
        ],
    },
    'test_extractor_pins.py': {
        'fp': 'abcb868ff942fef8d5bf995155b48087',
        'edits': [
            (68, 78,
             [
              'def parse_sites(path):',
              '    """[(module, line, label)] from the shared corpus list."""',
              '    sites = []',
              "    with open(path, encoding='utf-8') as handle:",
              '        for raw in handle:',
              "            if raw.startswith('#') or not raw.strip():",
              '                continue',
              "            parts = raw.rstrip('\\n').split('\\t')",
              '            if len(parts) >= 3:',
              '                sites.append((parts[0], int(parts[1]), parts[2]))',
              '    return sites',
             ],
             [
              'parse_sites = wk.parse_sites_doc',
             ]),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    if not os.path.isfile('constants_new.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding constants_new.py).')
        return 1

    staged = []
    fixed = []
    total = 0

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written.')
            return 1

        crlf = b'\r\n' in raw
        lines = normalized(raw).decode('utf-8').split('\n')

        # The gate is on what THIS patch introduces. A file that already
        # holds non-ASCII is reported rather than blocked -- blocking on
        # somebody else's bug stops a correct patch, and staying silent
        # about it is how the convention quietly stops being true.
        for _, _, _, new_lines in spec['edits']:
            for line in new_lines:
                try:
                    line.encode('ascii')
                except UnicodeEncodeError:
                    print('ERROR: this patch would insert non-ASCII into '
                          '%s. Nothing written.' % name)
                    print('       %r' % line)
                    return 1
        before = sum(1 for b in bytearray(raw) if b > 127)
        if before:
            fixed.append((name, before))

        for start, end, old, new in spec['edits']:
            if end >= len(lines):
                print('ANCHOR FAIL: %s lines %d-%d run past end of file.'
                      % (name, start + 1, end + 1))
                return 1
            if lines[start:end + 1] != old:
                print('ANCHOR FAIL: %s lines %d-%d do not read as recorded.'
                      % (name, start + 1, end + 1))
                for offset, want in enumerate(old):
                    got = lines[start + offset]
                    if got != want:
                        print('       first difference at line %d'
                              % (start + offset + 1))
                        print('       expected %r' % want)
                        print('       found    %r' % got)
                        break
                print('       Nothing written.')
                return 1
            lines[start:end + 1] = new

        out = '\n'.join(lines).encode('utf-8')
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-36s %d edit(s)' % (name, count))

    for name, before in fixed:
        with open(name, 'rb') as handle:
            after = sum(1 for b in bytearray(handle.read()) if b > 127)
        if after:
            print('note: %s still holds %d non-ASCII byte(s) this patch did '
                  'not reach' % (name, after))
        else:
            print('note: %s had %d non-ASCII byte(s); normalized to ASCII in '
                  'passing' % (name, before))
    print('patch applied (%d bytes, %d edits across %d files)'
          % (total, sum(c for _, _, c in staged), len(staged)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
