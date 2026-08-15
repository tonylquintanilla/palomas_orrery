"""Re-anchor the August 14 handoff to the real final SHA (L-192).

Domain: dev_tools

WHY THIS PATCH EXISTS

The handoff was written and committed at `92b5bf8`, then the Tier-1
banner patch ran and the result pushed at `65ca311`. So the document
says "pushed at 92b5bf8" while the session actually ended one commit
later, and its (do) item 9 says the banner patch has not been run when
it has.

Neither line was wrong when written. Both are wrong now, which is the
ordinary way a handoff goes stale: the last action of a session happens
after the document describing the session.

WHY IT MATTERS RATHER THAN BEING TIDINESS

The anchor is the whole verification mechanism. A next session pulls at
HEAD, compares against what the handoff claims, and reconciles any
difference before building. A handoff naming the wrong final SHA sends
that session looking for a discrepancy that is not a discrepancy -- or
worse, teaches it that the anchor line is approximate. An approximate
anchor is not an anchor.

WHAT IT CHANGES

Three edits in documentation/HANDOFF_20260814_L192_producer.md:

  1. The opening anchor block: pushed at 92b5bf8 -> 65ca311, with the
     92b5bf8 step kept visible rather than overwritten.
  2. The closing anchor line, same correction.
  3. (do) item 9: rewritten to record that the patch RAN and what the
     runner printed afterwards.

The document is otherwise untouched. In particular the "15 bodies"
correction note in (do) item 10 stays open -- that is a different
document and a separate job.

WHAT IT DELIBERATELY DOES NOT DO

It does not remove item 9. The item is the record that the banner was
found, fixed and verified; deleting it would leave the fix with no
trace in the handoff at all. Process history stays in the record.

HOW TO RUN IT

Open in VS Code, press Run. Prints what it found before writing,
writes nothing if any check fails, safe to run twice.

Patch written August 2026 with Anthropic's Claude Opus 5, built on
65ca311512a5646551a8ed9e385863807809e2e9 at
https://github.com/tonylquintanilla/palomas_orrery.
"""

import hashlib
import os
import sys

TARGET = os.path.join('documentation',
                      'HANDOFF_20260814_L192_producer.md')

EXPECTED_FINGERPRINT = 'fc7ad4f9a8d4fe41b958fe8130546bd5'

ALREADY = b'65ca311512a5646551a8ed9e385863807809e2e9'

OLD_OPENING = (
    b'**Built on `305b2697648590e4a75551c73743abc98bd20c66`, pushed at\n'
    b'`92b5bf8f7def1bc384c165eb84224ad1e542125f`\n'
)

NEW_OPENING = (
    b'**Built on `305b2697648590e4a75551c73743abc98bd20c66`, pushed at\n'
    b'`65ca311512a5646551a8ed9e385863807809e2e9`\n'
    b'(the build landed at `92b5bf8f7def1bc384c165eb84224ad1e542125f`;\n'
    b'the Tier-1 banner patch ran after this document was written and\n'
    b'pushed at `65ca311`, which is where the session actually ends)\n'
)

OLD_CLOSING = (
    b'*Handoff prepared August 2026 with Anthropic\'s Claude Opus 5. Built on\n'
    b'`305b2697648590e4a75551c73743abc98bd20c66` and pushed at\n'
    b'`92b5bf8f7def1bc384c165eb84224ad1e542125f` at\n'
)

NEW_CLOSING = (
    b'*Handoff prepared August 2026 with Anthropic\'s Claude Opus 5. Built on\n'
    b'`305b2697648590e4a75551c73743abc98bd20c66` and pushed at\n'
    b'`65ca311512a5646551a8ed9e385863807809e2e9` at\n'
)

OLD_ITEM_9 = (
    b'9. **Run `patch_L192_tier1_banner.py`.** Delivered, tested, not yet\n'
    b'   run. Reason below.\n'
)

NEW_ITEM_9 = (
    b'9. **CLOSED -- the Tier-1 banner was reworded and verified.** The\n'
    b'   patch ran clean at `65ca311` and the runner now prints `206\n'
    b'   TIER-1 FINDINGS IN THE SCANNED TREE` above `All 11 checkers\n'
    b'   passed`, which no longer contradicts it. Kept here rather than\n'
    b'   deleted: the reason below is why the banner said what it said\n'
    b'   for three protocol versions, and that is worth reading once.\n'
)


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(project_dir, TARGET)

    print('=' * 70)
    print('PATCH: re-anchor the August 14 handoff (L-192)')
    print('=' * 70)

    if not os.path.exists(path):
        print('  STOPPED: %s not found.' % TARGET)
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    found = fingerprint(data)
    print('  Fingerprint expected: %s' % EXPECTED_FINGERPRINT)
    print('  Fingerprint found:    %s' % found)

    if ALREADY in data:
        print('  STOPPED: the handoff already names 65ca311. Nothing to do.')
        return 0

    if found != EXPECTED_FINGERPRINT:
        print('  STOPPED: this is not the file the patch was built against.')
        print('  Nothing written. Do not edit the fingerprint to pass.')
        return 1

    newline = b'\r\n' if data.count(b'\r\n') > data.count(b'\n') // 2 \
        else b'\n'
    print('  Line ending:          %r' % newline)

    edits = [
        ('opening anchor', OLD_OPENING, NEW_OPENING),
        ('closing anchor', OLD_CLOSING, NEW_CLOSING),
        ('(do) item 9', OLD_ITEM_9, NEW_ITEM_9),
    ]

    # Stage every edit before writing anything. One anchor matching
    # zero or twice aborts the whole patch, file untouched.
    staged = data
    for label, old, new in edits:
        if newline == b'\r\n':
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        matches = staged.count(old)
        print('  Anchor matches:       %d (need exactly 1) -- %s'
              % (matches, label))
        if matches != 1:
            print('  STOPPED: nothing written.')
            return 1
        staged = staged.replace(old, new)

    temporary = path + '.patch_tmp'
    with open(temporary, 'wb') as handle:
        handle.write(staged)
    os.replace(temporary, path)

    print('  WROTE: two anchors corrected, item 9 closed.')
    print()
    print('  Note: this commit moves HEAD past 65ca311, so the handoff')
    print('  will again name a SHA one commit behind the tip. That is')
    print('  expected and harmless -- the anchor names where the WORK')
    print('  landed, not where the record of it landed. Do not chase it')
    print('  further.')
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
