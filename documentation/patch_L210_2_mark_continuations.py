"""patch_L210_2_mark_continuations.py

Built on eee4cc61a66607c2533549361c11be6af0aec15d at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5.

Runs AFTER patch_L210_1_reconciliation_four_rows.py. Repairs a defect
that patch introduced.

WHAT WENT WRONG

patch_L210_1 wrapped four `# Source:` legs and one `# Derived:` leg
onto padded second lines with no continuation marker. Under L-195 a
citation that continues on the next line must name the leg it
continues -- `# Source+:` under `# Source:` -- and the request builder
REFUSES to write a request while any unmarked continuation exists,
because that text is joined nowhere and printed nowhere.

So `test_worksheet_request_builder.py` failed on the corpus check, and
it was right to. Six lines, not the four the failure message named:
the report shows one per row, and the Derived leg contributed two more
that no message mentioned. Fixing only the reported four would have
left the check red and looked like the fix had failed.

Also repaired: patch_L210_1's currency stamp ran to five lines, three
of which carry numbers. constants_change_report.py reported them as
"changed line(s) that carry a number but match no shape this tool
reads" and declined to check them -- the blind spot announcing itself,
exactly as designed. The stamp collapses to one line it can parse.

NOT REPAIRED, on purpose. The multi-line `# Note:` and
`# Review-note:` bodies are left alone. `Note` is not in the builder's
leg vocabulary today, so those lines close the run rather than
continuing it and no marker is valid on them yet -- writing `Note+:`
now would be silently DROPPED, which is the L-214 bug itself. They
become unmarked continuations the moment L-214 admits `Note` to
CONTEXT_LEGS. That is a build-order dependency, recorded here and
owed to L-214.

WHAT IT DOES
  constants_new.py
    1-4. `#   <text>` -> `# Source+: <text>` under EARTH_EQUATORIAL_
         RADIUS_KM, STREAMER_BELT_RADII, BENNU_RADIUS_KM and
         HAUMEA_RADIUS_KM.
    5.   Two `#   <text>` -> `# Derived+: <text>` under
         HAUMEA_RADIUS_KM.
    6.   The five-line Module updated stamp becomes one line.

CRLF NOTE. This patch reads and writes binary and preserves whatever
line endings the working copy has. patch_L210_1 did not need that
because both its targets were LF on disk; the ledger, next door, is
CRLF, which is how the sibling patch aborted.

AFTER RUNNING
  python test_worksheet_request_builder.py   (expect 63 of 63)
  python test_constants_provenance.py        (expect 15 of 15)
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = 'eee4cc61a66607c2533549361c11be6af0aec15d'
CONSTANTS = 'constants_new.py'

# md5 of the LF form at BASE_SHA. A CRLF working copy is normalised
# before this is computed, so either checkout matches.
FINGERPRINT_LF = '382c5bb825b7de1f120f90d4ff44b4ac'

EDITS = [
    ('EARTH: mark the Source continuation',
     "# Source: IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical\n"
     "#   Note No. 36, Table 1.1; IAU B3 rounds to 6378.1 km\n",
     "# Source: IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical\n"
     "# Source+: Note No. 36, Table 1.1; IAU B3 rounds to 6378.1 km\n"),

    ('STREAMER: mark the Source continuation',
     "# Source: Golub & Pasachoff, \"The Solar Corona\" (2nd ed., 2010) --\n"
     "#   coronal structure bounded at roughly 5-10 R_sun\n",
     "# Source: Golub & Pasachoff, \"The Solar Corona\" (2nd ed., 2010) --\n"
     "# Source+: coronal structure bounded at roughly 5-10 R_sun\n"),

    ('BENNU: mark the Source continuation',
     "# Source: Barnouin et al. 2019, Nature Geoscience 12:247, Table 1 --\n"
     "#   mean radius 245.03 +/- 0.08 m from OSIRIS-REx OLA and imaging\n",
     "# Source: Barnouin et al. 2019, Nature Geoscience 12:247, Table 1 --\n"
     "# Source+: mean radius 245.03 +/- 0.08 m from OSIRIS-REx OLA and imaging\n"),

    ('HAUMEA: mark the Source and Derived continuations',
     "# Source: Ortiz et al. 2017, Nature 550:219 (stellar occultation) --\n"
     "#   semi-axes 1161 +/- 30, 852 +/- 4, 513 +/- 16 km\n"
     "# Derived: volume-equivalent radius (1161 * 852 * 513)^(1/3) = 797.6 km,\n"
     "#   rounded to 798. Ortiz publishes the semi-axes and no mean radius, so\n"
     "#   this value is COMPUTED here rather than quoted.\n",
     "# Source: Ortiz et al. 2017, Nature 550:219 (stellar occultation) --\n"
     "# Source+: semi-axes 1161 +/- 30, 852 +/- 4, 513 +/- 16 km\n"
     "# Derived: volume-equivalent radius (1161 * 852 * 513)^(1/3) = 797.6 km,\n"
     "# Derived+: rounded to 798. Ortiz publishes the semi-axes and no mean\n"
     "# Derived+: radius, so this value is COMPUTED here rather than quoted.\n"),

    ('CURRENCY: collapse the stamp to one parseable line',
     "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-210:\n"
     "EARTH_EQUATORIAL_RADIUS_KM to IERS precision, BENNU_RADIUS_KM to the\n"
     "OSIRIS-REx figure, HAUMEA_RADIUS_KM to the 2017 occultation,\n"
     "STREAMER_BELT_RADII held with its unsourced range withdrawn). Built on\n"
     "3586970d.\n",
     "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-210 "
     "reconciliation; see the Resolved legs on the affected rows)\n"),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    if not os.path.isfile(CONSTANTS):
        fail('%s not found. Run this from the repo root.' % CONSTANTS)

    with open(CONSTANTS, 'rb') as handle:
        raw = handle.read()

    crlf = b'\r\n' in raw
    lf_bytes = raw.replace(b'\r\n', b'\n')
    print('[line endings] working copy is %s' % ('CRLF' if crlf else 'LF'))

    actual = hashlib.md5(lf_bytes).hexdigest()
    if actual != FINGERPRINT_LF:
        fail('%s does not match the base at %s (compared in LF form, so a '
             'CRLF checkout is not the cause).\n'
             '  expected md5 %s\n  actual   md5 %s\n'
             '  Did patch_L210_1 run? This patch repairs its output.'
             % (CONSTANTS, BASE_SHA[:8], FINGERPRINT_LF, actual))
    print('[base ok] %s  md5 %s (LF form)' % (CONSTANTS, actual))

    try:
        text = lf_bytes.decode('ascii')
    except UnicodeDecodeError as exc:
        fail('%s carries non-ASCII at offset %d.' % (CONSTANTS, exc.start))
    print('[ascii ok] %s' % CONSTANTS)

    for label, old, new in EDITS:
        count = text.count(old)
        if count != 1:
            fail('anchor for "%s" matched %d times, expected exactly 1.'
                 % (label, count))
        text = text.replace(old, new, 1)
        print('[anchor ok] %s' % label)

    # THE CHECK THAT MATTERS: re-run the project's own detector over the
    # patched text and require ZERO unmarked continuations. Not a count
    # of what this patch touched -- the whole file, so a seventh case
    # nobody reported cannot slip through.
    sys.path.insert(0, os.getcwd())
    try:
        import worksheet_keys as wk
    except Exception as exc:
        fail('could not import worksheet_keys to verify the result: %s' % exc)

    offenders = []
    open_label = None
    for number, line in enumerate(text.split('\n'), 1):
        match = wk.LEG_RE.match(line)
        if match:
            open_label = None if match.group(2) else match.group(1)
            continue
        if open_label is not None and wk.continues_a_leg(line):
            offenders.append((number, open_label, line.strip()))
            continue
        open_label = None

    if offenders:
        print('')
        print('%d unmarked continuation(s) REMAIN:' % len(offenders))
        for number, label, line in offenders:
            print('  %5d under %-9s %s' % (number, label, line[:60]))
        fail('the repair is incomplete. Nothing written.')
    print('[verified] 0 unmarked continuations in the whole file')

    out = text.encode('ascii')
    if crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(CONSTANTS, 'wb') as handle:
        handle.write(out)
    print('[written] %s (%s preserved)' % (CONSTANTS, 'CRLF' if crlf else 'LF'))

    print('')
    print('NO VALUE CHANGED. This patch touches citation legs and one '
          'docstring line only.')
    print('')
    print('CURRENCY STAMP UPDATED (Stamp What You Change):')
    print('  %s -- Module updated line collapsed to one line, so '
          'constants_change_report.py can parse it' % CONSTANTS)
    print('')
    print('NEXT:')
    print('  1. python test_worksheet_request_builder.py   (expect 63 of 63)')
    print('  2. python test_constants_provenance.py        (expect 15 of 15)')
    print('  3. Re-run the maintenance runner')
    print('  4. Move this script to documentation/')
    print('')
    print('STILL EXPECTED TO REPORT, and not a defect: '
          'constants_change_report.py calls BENNU_RADIUS_KM and '
          'HAUMEA_RADIUS_KM AMBIGUOUS. Three values moved in one commit '
          'with provenance edits beside them, and the tool correctly '
          'declines to guess which edit documents which value.')


if __name__ == '__main__':
    main()
