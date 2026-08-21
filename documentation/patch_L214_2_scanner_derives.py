"""L-214 patch 2 of 2 -- the scanner derives its record-label names.

Built on dbe50bc9ea23bbd1f1e4e941ef7148d1da8ab554 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES

One file, one idea, behavior-preserving. provenance_scanner.py stops
spelling `cross-checked` and `resolved` as its own string literals and
takes those NAMES from worksheet_keys.RECORD_LEGS, which patch 1 made
the one home for the label vocabulary.

WHAT DOES NOT MOVE

The body grammar stays here. RESOLVED_BODY_RE still enforces
`<worksheet> <key> -- <what> (L-nnn)` with ISO-only dates, and
CROSS_CHECK_DATE_RE still rejects prose dates. Moving those into a
keys module would drag semantics into a place that has no business
holding them. What moves is the label SET; what stays is what a body
is allowed to say. That is the transport/grammar split the Mode 7
review settled on, applied one layer down. (L-214, verified 3586970d.)

The patterns stay case-INSENSITIVE, exactly as they are today. The
scanner's `(?mi)` behaviour is unchanged by this patch; the shared
matcher in worksheet_keys is not relaxed to match it. That asymmetry
was ruled on 2026-08-20 and is not reopened here.

THE GUARD IS THE POINT

Deriving a pattern from a shared name is decorative unless a rename
that fails to reach here can actually fail. So the two names are
checked against RECORD_LEGS at import time, and a name that is no
longer in the registry raises rather than quietly compiling a pattern
for a label nothing writes any more.

HOW TO RUN IT

Open this file in VS Code and press Run, from the repo root. It takes
no arguments and asks no questions. On any failure it writes nothing.

After it runs, the scanner's own recognition pins are the check that
matters: run test_scanner_recognition (or the maintenance run) and
confirm the 27 recognition pins still hold.

Written August 21, 2026 with Anthropic's Claude Opus 5 (L-214).
"""

import hashlib
import os
import sys

PATH = 'provenance_scanner.py'
FINGERPRINT = '73231f9dbb7a0c12e0a1f5f5fdf8aa85'

IMPORT_OLD = """# L-189: run history and run-to-run delta. Informational only --
# nothing imported here touches the exit code.
import provenance_history"""

IMPORT_NEW = """# L-189: run history and run-to-run delta. Informational only --
# nothing imported here touches the exit code.
import provenance_history

# L-214: the label VOCABULARY has one home, and this is not it. The
# names of the record legs come from there; what a record leg's body
# is allowed to say stays here. worksheet_keys imports nothing from
# this module, so the dependency runs one way only.
import worksheet_keys as wk"""

DERIVE_OLD = """CROSS_CHECK_LINE_RE = re.compile(
    r'(?mi)^[ \\t]*#[ \\t]*cross-checked[ \\t]*:(?P<body>[^\\n]*)$')"""

DERIVE_NEW = """# The two record legs this module parses, named from the registry
# rather than spelled again here. The membership check is what makes
# the derivation real: rename a leg in worksheet_keys without updating
# this list and the import fails loudly, where a bare literal would go
# on compiling a pattern for a label nothing writes any more.
RECORD_CROSS_CHECK = 'Cross-checked'
RECORD_RESOLVED = 'Resolved'
for _leg in (RECORD_CROSS_CHECK, RECORD_RESOLVED):
    if _leg not in wk.RECORD_LEGS:
        raise ImportError(
            '%s parses a %r leg, but worksheet_keys.RECORD_LEGS does not '
            'carry that name. One of the two moved without the other.'
            % (__name__, _leg))
del _leg


def _record_line_re(label):
    \"\"\"The line pattern for one record leg, built from its NAME.

    Case-insensitive, as these patterns have always been. The shared
    matcher in worksheet_keys is case-SENSITIVE and is deliberately
    not relaxed to agree: odd spellings are fixed at source instead.
    (Ruled 2026-08-20; see L-214.)
    \"\"\"
    return re.compile(
        r'(?mi)^[ \\t]*#[ \\t]*%s[ \\t]*:(?P<body>[^\\n]*)$'
        % re.escape(label))


CROSS_CHECK_LINE_RE = _record_line_re(RECORD_CROSS_CHECK)"""

RESOLVED_OLD = """RESOLVED_LINE_RE = re.compile(
    r'(?mi)^[ \\t]*#[ \\t]*resolved[ \\t]*:(?P<body>[^\\n]*)$')"""

RESOLVED_NEW = """RESOLVED_LINE_RE = _record_line_re(RECORD_RESOLVED)"""

STAMP_ANCHOR = 'Module updated:'


def die(reason):
    print('')
    print('STOPPED. %s' % reason)
    print('Nothing was written.')
    sys.exit(1)


def swap(text, old, new, where):
    found = text.count(old)
    if found != 1:
        die('anchor for %s matched %d times, expected exactly 1.'
            % (where, found))
    for char in new:
        if ord(char) > 127:
            die('non-ASCII character %r would be inserted into %s.'
                % (char, where))
    return text.replace(old, new, 1)


def main():
    if not os.path.isdir('documentation'):
        die('no documentation/ directory here. Run this from the '
            'palomas_orrery repo root.')
    if not os.path.exists(PATH):
        die('%s not found.' % PATH)

    with open(PATH, 'rb') as handle:
        raw = handle.read()
    if b'\r\n' in raw:
        die('%s has CRLF line endings; this patch expects LF.' % PATH)
    text = raw.decode('utf-8')

    actual = hashlib.md5(text.encode('utf-8')).hexdigest()
    if actual != FINGERPRINT:
        die('%s does not match the file this patch was written against.\n'
            '  expected md5 %s\n  found        %s\n'
            'Re-pull the repo at dbe50bc9, or ask for a patch rebuilt on '
            'the current bytes.' % (PATH, FINGERPRINT, actual))

    out = swap(text, IMPORT_OLD, IMPORT_NEW, 'the import block')
    out = swap(out, DERIVE_OLD, DERIVE_NEW, 'the cross-check pattern')
    out = swap(out, RESOLVED_OLD, RESOLVED_NEW, 'the resolved pattern')

    if STAMP_ANCHOR not in out:
        die('%s carries no currency line to stamp.' % PATH)
    last = out.rindex(STAMP_ANCHOR)
    line_end = out.index('\n', last)
    stamp = ("\nModule updated: August 21, 2026 with Anthropic's "
             "Claude Opus 5 (L-214).")
    out = out[:line_end] + stamp + out[line_end:]

    if out == text:
        die('the file came out identical to its input, which means an '
            'edit silently did nothing.')

    with open(PATH, 'wb') as handle:
        handle.write(out.encode('utf-8'))

    print('%s: 3 edit(s) + 1 currency stamp.' % PATH)
    print('')
    print('  cross-checked / resolved label names now come from '
          'worksheet_keys.RECORD_LEGS.')
    print('  Body grammar (RESOLVED_BODY_RE, CROSS_CHECK_DATE_RE) '
          'unchanged and still here.')
    print('')
    print('NEXT: run the maintenance script. The check that matters is '
          '"Scanner recognition 1d/1e" -- 27 of 27 pins should still '
          'hold, and the Tier-1 count should still read 292.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
