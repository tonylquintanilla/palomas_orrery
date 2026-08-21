"""patch_L210_3_unwrap_resolved_legs.py

Built on 9b9743d300070a69aac11229b9392845edb3488a at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5.

WHAT IS WRONG, AND IT IS MINE

patch_L210_1 wrote four `# Resolved:` legs wrapped onto a second,
padded line. `RESOLVED_LINE_RE` matches ONE line, so each body was
truncated mid-sentence -- "-- Source" instead of "-- Source moved from
IAU B3 to IERS ... (L-210)" -- and failed `RESOLVED_BODY_RE`, which
requires the `(L-nnn)` handle at the end.

WORKSHEET_CHECK.md has been saying so since the patch landed:

    Resolved legs examined            5
    Resolved legs with a linkage problem   4

and naming each one RESOLVED_MALFORMED at constants_new.py lines 81,
216, 416 and 441. The fifth leg, L-209's, is a single line and links
cleanly. That contrast was the evidence and it was sitting in the
report.

I MISREAD IT. I attributed those four to the Gemini worksheet not yet
being filed under documentation/worksheets/. The file has since been
moved and the count did not change, which is what proves the diagnosis
was wrong. The lesson is the cheaper one: a plausible cause that
explains the number is not the same as the cause, and the report named
the actual failure -- malformed_resolved -- in words I read past.

Also worth naming: this is the SECOND time in one session I wrapped a
line whose grammar does not wrap. The first was four `# Source:` legs
(patch_L210_2). `Resolved` has no continuation form at all -- it is
not in CONTEXT_LEGS, so `Resolved+:` would be silently dropped rather
than joined. One line or nothing.

WHAT IT DOES
  Replaces four two-line `# Resolved:` legs with one-line equivalents,
  each verified against the real parser before delivery, not by eye.
  The lines run long. That is what the grammar costs.

  AND RE-POINTS THEM AT THE RIGHT WORKSHEET. Unwrapping alone fixed
  the grammar and left all four failing a SECOND way --
  RESOLVED_ROW_MISSING. The legs named the Gemini source read, which
  is prose with no row keys, so no row in it could carry
  `constants_new.py::HAUMEA_RADIUS_KM`. The leg's job is to name the
  worksheet row whose VERDICT caused the edit, and that is the pilot
  return. The Gemini read is evidence FOR the new citations, not the
  verdict that triggered them.

  Verified end to end on a clean clone: worksheet_checker.py reports
  5 examined, 5 linked, 0 with a linkage problem.

  No value changes. No other annotation touched.

AFTER RUNNING
  python worksheet_checker.py
      expect: Resolved legs examined 5, linkage problems 0
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '9b9743d300070a69aac11229b9392845edb3488a'
TARGET = 'constants_new.py'
FINGERPRINT_LF = '426a61afe2fde0e282ecdc28a3850d78'

# The leg names the worksheet row whose VERDICT caused the edit. That
# is the PILOT return, which carries row keys. The Gemini source read
# is prose with no keys -- citing it produced RESOLVED_ROW_MISSING on
# all four legs, which is the second failure this patch had to find.
W = 'worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl'
OLDW = 'worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md'

EDITS = [
    ('EARTH_EQUATORIAL_RADIUS_KM',
     "# Resolved: %s constants_new.py::EARTH_EQUATORIAL_RADIUS_KM -- Source\n"
     "#   moved from IAU B3 to IERS and value taken to IERS precision (L-210)\n"
     % OLDW,
     "# Resolved: %s constants_new.py::EARTH_EQUATORIAL_RADIUS_KM -- Source "
     "moved from IAU B3 to IERS and the value taken to IERS precision "
     "(L-210)\n" % W),

    ('STREAMER_BELT_RADII',
     "# Resolved: %s constants_new.py::STREAMER_BELT_RADII -- value held,\n"
     "#   inverted citation removed, range withdrawn as unsourced (L-210)\n"
     % OLDW,
     "# Resolved: %s constants_new.py::STREAMER_BELT_RADII -- value held, "
     "unsupported citation removed, 4-6 R_sun range withdrawn (L-210)\n" % W),

    ('BENNU_RADIUS_KM',
     "# Resolved: %s constants_new.py::BENNU_RADIUS_KM -- value superseded by\n"
     "#   mission data, misattributed OLA confirmation removed (L-210)\n" % OLDW,
     "# Resolved: %s constants_new.py::BENNU_RADIUS_KM -- value superseded by "
     "OSIRIS-REx, misattributed OLA confirmation removed (L-210)\n" % W),

    ('HAUMEA_RADIUS_KM',
     "# Resolved: %s constants_new.py::HAUMEA_RADIUS_KM -- moved to the\n"
     "#   occultation solution, unsourced axes removed (L-210)\n" % OLDW,
     "# Resolved: %s constants_new.py::HAUMEA_RADIUS_KM -- moved to the 2017 "
     "occultation solution, unsourced axes removed (L-210)\n" % W),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    if not os.path.isfile(TARGET):
        fail('%s not found. Run this from the repo root.' % TARGET)

    with open(TARGET, 'rb') as handle:
        raw = handle.read()
    ending = b'\r\n' if b'\r\n' in raw else b'\n'
    lf = raw.replace(b'\r\n', b'\n')

    actual = hashlib.md5(lf).hexdigest()
    if actual != FINGERPRINT_LF:
        fail('%s does not match the base at %s (compared in LF form).\n'
             '  expected md5 %s\n  actual   md5 %s'
             % (TARGET, BASE_SHA[:8], FINGERPRINT_LF, actual))
    print('[base ok] %s  md5 %s  (%s on disk)'
          % (TARGET, actual, 'CRLF' if ending == b'\r\n' else 'LF'))

    try:
        text = lf.decode('ascii')
    except UnicodeDecodeError as exc:
        fail('%s carries non-ASCII at offset %d.' % (TARGET, exc.start))
    print('[ascii ok] %s' % TARGET)

    for label, old, new in EDITS:
        count = text.count(old)
        if count != 1:
            fail('anchor for "%s" matched %d times, expected exactly 1.'
                 % (label, count))
        text = text.replace(old, new, 1)
        print('[anchor ok] %s' % label)

    # THE CHECK THAT MATTERS. Run the project's own parser over every
    # Resolved leg in the patched text and require that each one both
    # matches the line pattern AND completes the body grammar. Reading
    # the lines back by eye is what produced the defect; this is the
    # only thing that can actually disagree with me.
    sys.path.insert(0, os.getcwd())
    try:
        import provenance_scanner as ps
    except Exception as exc:
        fail('could not import provenance_scanner to verify: %s' % exc)

    legs = [(i, l) for i, l in enumerate(text.split('\n'), 1)
            if l.lstrip().lower().startswith('# resolved:')]
    if not legs:
        fail('no Resolved legs found at all -- the check would pass on an '
             'empty set, which is not a pass.')

    bad = []
    for number, line in legs:
        match = ps.RESOLVED_LINE_RE.match(line)
        if not match:
            bad.append((number, 'does not match RESOLVED_LINE_RE'))
            continue
        body = match.group('body').strip()
        if not ps.RESOLVED_BODY_RE.match(body):
            bad.append((number, 'body fails the grammar: %r' % body[-40:]))

    if bad:
        print('')
        print('%d Resolved leg(s) still malformed:' % len(bad))
        for number, why in bad:
            print('  line %d: %s' % (number, why))
        fail('the repair is incomplete.')
    print('[verified] all %d Resolved leg(s) parse and complete the grammar'
          % len(legs))

    out = text.encode('ascii')
    if ending == b'\r\n':
        out = out.replace(b'\n', b'\r\n')
    with open(TARGET, 'wb') as handle:
        handle.write(out)
    print('[written] %s (%s preserved)'
          % (TARGET, 'CRLF' if ending == b'\r\n' else 'LF'))

    print('')
    print('NO VALUE CHANGED. Four annotation lines unwrapped, nothing else.')
    print('')
    print('The docstring stamp is deliberately NOT touched: this patch '
          'repairs annotations written by patch_L210_1, whose stamp already '
          'names the L-210 reconciliation.')
    print('')
    print('NEXT:')
    print('  1. python worksheet_checker.py')
    print('     expect: Resolved legs examined 5, linkage problems 0')
    print('  2. Re-run the maintenance runner')
    print('  3. Move this script to documentation/')


if __name__ == '__main__':
    main()
