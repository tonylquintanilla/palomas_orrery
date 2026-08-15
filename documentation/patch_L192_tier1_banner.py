"""Reword the scanner's Tier-1 banner so it stops claiming a verdict (L-192).

Domain: dev_tools

WHY THIS PATCH EXISTS

The scanner prints, in this order:

    206 TIER-1 FINDINGS -- PUSH GATE NOT MET
    Informational only. This does not affect the exit code.

Both lines are true and they contradict each other on sight. The
banner is three protocol versions behind its own next sentence: the
push gate moved to the ACTIVE BUILD PATH at provenance-discipline 2.3
(L-184), so a global count of 206 does not mean the gate is unmet. It
means 206 Tier-1 findings exist somewhere in the scanned tree, most of
them off the path the gate judges.

A warning that announces a failure and then says it fails nothing
teaches the reader to skim it. The day it means something, that
reading habit is already trained. This is the normalization-of-
deviance shape, sitting in the routine that runs before every push.

WHY THE FIX IS WORDING AND NOT A NEW NUMBER

The obvious fix -- print the active-build-path count instead -- cannot
be done here, because the scanner does not compute one. There is no
build-path subset in this module; adding one means defining which
modules are on the path, which is a design decision and not a banner
edit.

So the banner does the honest thing instead: it reports the number it
actually has, states that this is not the gate number, and names what
the gate is judged on. That is the blind spot announcing itself rather
than a count standing in for a verdict nobody computed.

The surrounding design comment is left untouched and still holds:
Tier-1 never gets an auto-exit gate at any threshold, because a count
is the wrong thing to judge by. This patch removes a line that read
like the gate that comment forbids.

HOW TO RUN IT

Open in VS Code, press Run. Prints what it found before writing,
writes nothing if any check fails, safe to run twice.

AFTER IT RUNS

Press Run on provenance_scanner.py (or maintenance_run.py) and read
the banner. It should report the count, disclaim the gate, and point
at the audit for the build-path subset.

Patch written August 2026 with Anthropic's Claude Opus 5, built on
92b5bf8f7def1bc384c165eb84224ad1e542125f at
https://github.com/tonylquintanilla/palomas_orrery.
"""

import hashlib
import os
import sys

TARGET = 'provenance_scanner.py'

EXPECTED_FINGERPRINT = '25b2d32420f95316ad73f4adf7cb2207'

# Must match the NEW banner byte-for-byte, case included. An earlier
# draft used lowercase 'not' against a banner that prints 'NOT', so
# the second run fell through to the fingerprint check and reported
# a drifted file instead of an applied patch -- a guard that could
# not succeed, caught by running the patch twice rather than by
# reading it.
ALREADY = b'NOT the push gate'

OLD_BANNER = (
    b'        print(f"  {tier1} TIER-1 FINDINGS -- PUSH GATE NOT MET")\n'
    b'        print()\n'
    b'        print("  Informational only. This does not affect the exit code.")\n'
    b'        print("  Review them before pushing; the call is yours.")\n'
)

NEW_BANNER = (
    b'        print(f"  {tier1} TIER-1 FINDINGS IN THE SCANNED TREE")\n'
    b'        print()\n'
    b'        print("  Informational only. This does not affect the exit code,")\n'
    b'        print("  and it is NOT the push gate. The gate is Tier-1 = 0 on")\n'
    b'        print("  the ACTIVE BUILD PATH (provenance-discipline 2.3,")\n'
    b'        print("  L-184). This line does not compute that subset -- it")\n'
    b'        print("  counts every Tier-1 finding anywhere in the tree, most")\n'
    b'        print("  of them off the path the gate judges. Read")\n'
    b'        print("  PROVENANCE_AUDIT.md for the build-path findings.")\n'
    b'        print("  The call is yours.")\n'
)


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(project_dir, TARGET)

    print('=' * 70)
    print('PATCH: Tier-1 banner wording (L-192)')
    print('=' * 70)

    if not os.path.exists(path):
        print('  STOPPED: %s not found next to this script.' % TARGET)
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    found = fingerprint(data)
    print('  Fingerprint expected: %s' % EXPECTED_FINGERPRINT)
    print('  Fingerprint found:    %s' % found)

    if ALREADY in data:
        print('  STOPPED: the banner already carries the new wording.')
        return 0

    if found != EXPECTED_FINGERPRINT:
        print('  STOPPED: this is not the file the patch was built against.')
        print('  Nothing written. Do not edit the fingerprint to pass.')
        return 1

    newline = b'\r\n' if data.count(b'\r\n') > data.count(b'\n') // 2 \
        else b'\n'
    print('  Line ending:          %r' % newline)

    old = OLD_BANNER
    new = NEW_BANNER
    if newline == b'\r\n':
        old = old.replace(b'\n', b'\r\n')
        new = new.replace(b'\n', b'\r\n')

    matches = data.count(old)
    print('  Anchor matches:       %d (need exactly 1)' % matches)
    if matches != 1:
        print('  STOPPED: nothing written. The banner block did not match')
        print('  as a whole, which means one of its four lines has moved.')
        return 1

    temporary = path + '.patch_tmp'
    with open(temporary, 'wb') as handle:
        handle.write(data.replace(old, new))
    os.replace(temporary, path)

    print('  WROTE: banner reworded, exit code untouched.')
    print()
    print('  Next: press Run on maintenance_run.py and read the banner.')
    print('  It should report a count, disclaim the gate, and point at')
    print('  PROVENANCE_AUDIT.md.')
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
