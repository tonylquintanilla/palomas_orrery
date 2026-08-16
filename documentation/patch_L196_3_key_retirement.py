"""record_key_retirement.py -- L-192 / L-196.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
constants_new.py), open it in VS Code, and click Run.

    python record_key_retirement.py

RUN ORDER: normalize_continuations_stage1.py, then
retire_chromosphere_stylization.py, then this one. It touches none of
the files those two touch, so it will apply whenever -- but the test it
repairs only goes red after the chromosphere patch has run.

WHAT IT DOES
------------
Retiring CHROMOSPHERE_RADII turned test_worksheet_keys.py red, exactly
as designed: a key pinned at an earlier commit stopped resolving. That
is the stale-key detector working. But it cannot tell a deliberate
retirement from an accidental rename, and it should not try.

So the pin file learns the difference. Tony's ruling, 2026-08-16: on
retirement, mark it retired.

A key can leave the corpus two ways and they are different events:

  RENAME      an accident. Must fail loudly. Unchanged.
  RETIREMENT  a decision. Recorded, not deleted.

Deleting the pin line loses why the key vanished. An inert
'# RETIRED ...' comment records it and checks nothing, because
parse_pins already ignores comments -- a check that cannot fail.

So a retired pin INVERTS the assertion:

  live pin     this key MUST still resolve
  retired pin  this key MUST NOT resolve

If a retired key resolves again, either the value came back or the
record is wrong. Both deserve a red run.

Format, tab-separated:

    RETIRED  2026-08-16  L-196  constants_new.py::CHROMOSPHERE_RADII

FILES
-----
  test_worksheet_keys.py                    parse_pins splits live from
                                            retired; check_retired_pins
                                            added; runner reports both
  documentation/worksheets/L192_key_pins.txt        the retired record
  documentation/worksheets/L192_annotated_sites.txt the retired site

MUTATION-TESTED, BOTH DIRECTIONS
--------------------------------
A green retirement check proves nothing on its own -- the retired key
is absent, so the check passes without exercising anything. Both
failure paths were forced in throwaway copies and both go red:

  re-added CHROMOSPHERE_RADII to the source
    -> 'recorded RETIRED 2026-08-16 (L-196) but it resolves again at
        line 175'
  dropped the date and handle columns from the RETIRED line
    -> 'malformed RETIRED line -- want RETIRED<tab>date<tab>handle<tab>key'

SAFETY
------
All-or-nothing. Every file is fingerprinted (CRLF-normalized) before
anything is written, and every replaced block must read exactly as
recorded. Any mismatch aborts with nothing written. Edits apply
bottom-up within each file; each file's own line endings are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'test_worksheet_keys.py': {
        'fp': '5d51c579613145d8a03d72fcaed05214',
        'edits': [
            (268, 269,
             [
              "          '%d pinned keys still resolve.'",
              '          % (len(sites), len(minted), len(pins)))',
             ],
             [
              "          '%d pinned keys still resolve; %d retired keys confirmed gone.'",
              '          % (len(sites), len(minted), len(pins), len(retired)))',
             ]),
            (255, 255,
             [
              "        print('  Pinned keys:       %d' % len(pins))",
             ],
             [
              "        print('  Pinned keys:       %d live, %d retired'",
              '              % (len(pins), len(retired)))',
             ]),
            (254, 253,
             [
             ],
             [
              '        pin_failures += check_retired_pins(retired, sources)',
             ]),
            (249, 249,
             [
              '        pins = parse_pins(pins_path)',
             ],
             [
              '        pins, retired = parse_pins(pins_path)',
             ]),
            (248, 247,
             [
             ],
             [
              '        retired = []',
             ]),
            (101, 100,
             [
             ],
             [
              '                continue',
              "            if raw.startswith(RETIRED_TAG + '\\t'):",
             ]),
            (90, 92,
             [
              "            if raw and not raw.startswith('#'):",
              '                pins.append(raw)',
              '    return pins',
             ],
             [
              "            if not raw or raw.startswith('#'):",
              '                continue',
              "            if raw.startswith(RETIRED_TAG + '\\t'):",
              "                parts = raw.split('\\t')",
              '                if len(parts) < 4:',
              "                    retired.append(('<malformed>', raw, ''))",
              '                    continue',
              '                retired.append((parts[3], parts[1], parts[2]))',
              '                continue',
              '            live.append(raw)',
              '    return live, retired',
              '',
              '',
              'def check_retired_pins(retired, sources):',
              '    """A retired key that still resolves is a failure."""',
              '    failures = []',
              '    for key, when, handle in retired:',
              "        if key == '<malformed>':",
              "            failures.append((when, 'malformed RETIRED line -- want '",
              "                                   'RETIRED<tab>date<tab>handle<tab>key'))",
              '            continue',
              '        resolved, _ = wk.resolve(key, sources)',
              '        if resolved is not None:',
              "            failures.append((key, 'recorded RETIRED %s (%s) but it resolves '",
              "                                  'again at line %s' % (when, handle,",
              '                                                        resolved)))',
              '    return failures',
             ]),
            (86, 86,
             [
              '    pins = []',
             ],
             [
              '    """(live, retired) pins. A retired pin INVERTS the assertion.',
              '',
              '    A key can leave the corpus two ways and they are not the same',
              '    event. A RENAME is an accident and must fail loudly. A RETIREMENT',
              '    is a decision and must be recorded -- deleting the line loses why',
              "    the key vanished, and an inert '# RETIRED' comment records it",
              '    while checking nothing, which is a check that cannot fail.',
              '',
              '    So a retired pin asserts the opposite of a live one: this key must',
              '    NOT resolve. If it resolves again, either the constant came back',
              '    or the retirement record is wrong, and both deserve a red run.',
              '',
              '    Format, tab-separated:  RETIRED  <date>  <handle>  <key>',
              '    """',
              '    live = []',
              '    retired = []',
             ]),
            (85, 84,
             [
             ],
             [
              "RETIRED_TAG = 'RETIRED'",
              '',
              '',
             ]),
        ],
    },
    'documentation/worksheets/L192_key_pins.txt': {
        'fp': 'e50b7d6c85e54b8ad7d984575a18d127',
        'edits': [
            (57, 56,
             [
             ],
             [
              '# RETIRED keys. The assertion INVERTS here: a retired key must NOT',
              '# resolve. A rename is an accident and fails loudly above; a',
              '# retirement is a decision and is recorded rather than deleted, so a',
              '# future stale-key hit on the name reads as expected. If one of these',
              '# resolves again, either the value came back or this record is wrong.',
              '# Format: RETIRED<tab>date<tab>handle<tab>key',
              'RETIRED\t2026-08-16\tL-196\tconstants_new.py::CHROMOSPHERE_RADII',
              '',
             ]),
            (7, 7,
             [
              'constants_new.py::CHROMOSPHERE_RADII',
             ],
             [
             ]),
        ],
    },
    'documentation/worksheets/L192_annotated_sites.txt': {
        'fp': 'aaf16632e4b3167676312c633a3d5cc8',
        'edits': [
            (56, 55,
             [
             ],
             [
              '# RETIRED sites -- skipped by the round trip, kept as the record of',
              '# why the site left the corpus. Format: RETIRED<tab>date<tab>handle<tab>site',
              'RETIRED\t2026-08-16\tL-196\tconstants_new.py\t162\tCHROMOSPHERE_RADII',
              '',
             ]),
            (9, 9,
             [
              'constants_new.py\t162\tCHROMOSPHERE_RADII',
             ],
             [
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
