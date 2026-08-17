"""patch_L196_5_protocol_v340.py -- protocol v3.39 -> v3.40.

RUN COMMAND
-----------
Save into the palomas_orrery repo root, open in VS Code, click Run.

    python patch_L196_5_protocol_v340.py

RUN skills_index.py FIRST, or rather: this is built against the
PROJECT_INSTRUCTIONS.md that skills_index.py produced on 2026-08-16
with orrery-coding-conventions at 1.4 and safe-file-editing at 1.4 in
the manifest zone. If the manifest zone has been regenerated since,
this aborts on the fingerprint and writes nothing.

WHAT IT DOES
------------
Two hunks, both additions:
  - the version line, v3.39 -> v3.40
  - a v3.40 entry appended to the version history

It does NOT touch the SKILL-MANIFEST zone, which skills_index.py owns.

The entry records no change to the protocol's own rules. Two skills
gained conventions this session and the entry says what and why, plus a
process note on the two bad deliveries that preceded the good ones --
recorded because neither was caught by a check, and that is the part
worth keeping.

WHAT IS PERMANENT
-----------------
This script is disposable. The v3.40 entry is not.

VERIFIED BY A CHECK THAT CAN FAIL
---------------------------------
Pure-addition: every one of the 959 lines in the base file is still
present afterwards, except the single version line being replaced. That
check is here because the first attempt at this session's other
document edit was an insert written as a replace, which silently
deleted a header block. 959 lines in, 1022 out, nothing lost.

SAFETY
------
All-or-nothing, fingerprinted, bottom-up, line endings preserved.
Success: one 'ok' line, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'PROJECT_INSTRUCTIONS.md': {
        'fp': '06a62748d5eae04d5e16b60830cfcdd1',
        'edits': [
            (957, 956,
             [
             ],
             [
              "v3.40 (August 16, 2026): No change to the protocol's own rules. Two",
              'skills gained conventions, and both were earned the same way -- a',
              'session hit the problem, Tony ruled, the rule went into the skill that',
              'fires on it rather than into this document.',
              '',
              'safe-file-editing 1.3 -> 1.4, two additions. (1) Fix In Passing, Report',
              'It. Where a patch is already fingerprinting a file and finds a violation',
              'of an ALREADY-RULED convention in it, fix it in the same patch and say',
              'so, rather than noting it and moving on. Origin: a patch touching eight',
              'files blocked itself on two Unicode arrows in a comment that predated',
              "the work by months. Claude's first instinct was to report and leave it,",
              'citing "fix only what asked." Tony\'s ruling: the convention was already',
              'ruled, the file was already fingerprinted, and a separate sweep for two',
              'characters would never be scheduled, so leaving it means it never gets',
              'fixed. The anti-pattern "fix only what asked" guards against is',
              'unreviewed DESIGN change, not mechanical compliance with a standing',
              'rule. The encoding gate was rescoped with it -- hard-fail on non-ASCII',
              'in inserted lines, sweep pre-existing where the conditions hold, and',
              'print which of the two happened, because a gate that fails on somebody',
              "else's bug blocks a correct patch and a gate that stays silent is how a",
              'convention quietly stops being true. (2) Naming and Archiving a Patch',
              'Script: name it patch_<handle>_<what>.py leading with the ledger handle,',
              'number a sequence so sort order carries run order, archive to',
              'documentation/ once run, and state which parts of the change are',
              'permanent when the script is not. That convention was already 96 scripts',
              'deep in documentation/ and written down nowhere, so a session that read',
              'the delivery format still produced three unprefixed scripts and had to',
              'be told.',
              '',
              'orrery-coding-conventions 1.3 -> 1.4, two additions. (1) Marker',
              'Separation for Near-Equal Radii. Where two shells sit within about 10%',
              'of each other, the standing r*1.05 north-pole marker puts both in the',
              'same place and Plotly shows one where the user expects two -- geometry',
              'correct, legend correct, affordance silently absent. The inner shell',
              'keeps the pole; each subsequent shell steps 20 degrees in polar angle at',
              'its own radius. Separate angularly, never radially. Origin: the',
              'chromosphere moved to true physical scale and its marker landed 0.003',
              "solar radii from the photosphere's, about one pixel. The section says",
              'explicitly that this is NOT the May 2026 ring-marker fix, which solved a',
              'collision radially and cannot help at 0.29% -- reaching for it is the',
              'trap. (2) Harvest the Conventions You Find. When you touch a file and',
              'find a convention this skill does not hold, report it in the same',
              'message as the work; do not silently follow it, because following',
              "without naming is how it stays invisible. Promotion is Tony's judgment,",
              'not the finder\'s. Origin: Tony\'s observation that "there are many',
              'unrecorded conventions except in local files," which the patch-script',
              'naming convention had just demonstrated.',
              '',
              'Process note, recorded because it is the reason this entry exists at',
              'all. Both skill files were delivered wrong before they were delivered',
              'right, and neither error was caught by a check. The conventions file was',
              'named for download disambiguation rather than for its destination and',
              'was filed in documentation/, leaving two pushed source comments citing a',
              '20-degree rule that existed in no store the skill loader reads --',
              'cite-to-nonexistent-authority, live in the repo. Then the corrected file',
              'was built by an insert written as a replace, which deleted its own',
              'version block, Source line, criticality note, and the paragraph',
              'recording what v1.2 added. Tony found that by reading the new file',
              'against its sibling. The rebuild added a pure-addition check -- every',
              'line of 1.3 must still be present in 1.4 -- which is the check that',
              'should have run the first time. Deliverables now ship inside a folder',
              'named for their destination.',
              '',
             ]),
            (1, 1,
             [
              'Tony Quintanilla, PE | Claude | v3.39 | August 12, 2026',
             ],
             [
              'Tony Quintanilla, PE | Claude | v3.40 | August 16, 2026',
             ]),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    if not os.path.isfile('PROJECT_INSTRUCTIONS.md'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding PROJECT_INSTRUCTIONS.md).')
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
            if name == 'PROJECT_INSTRUCTIONS.md':
                print('       Most likely cause: the SKILL-MANIFEST zone '
                      'was regenerated after this patch was built. Send '
                      'the current file and it will be rebuilt.')
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
