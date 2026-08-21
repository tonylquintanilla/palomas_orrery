"""patch_L210_4_streamer_belt_unsourced.py

Built on 9b9743d300070a69aac11229b9392845edb3488a at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
AFTER patch_L210_3_unwrap_resolved_legs.py has run.

RUN ORDER MATTERS. This patch fingerprints the file as _3 leaves it, so
running it first will abort with a mismatch rather than half-apply.
That ordering is the L-219 gap again -- the naming convention carries
the sequence in the number and nothing enforces it but this note and
the fingerprint. The fingerprint is the part that actually enforces it.

Written August 20, 2026 with Anthropic's Claude Opus 5.

TONY'S RULING, 2026-08-20

Remove the citation. Record 6.0 as an ASSUMPTION until a verified
source is found.

WHY

`STREAMER_BELT_RADII` ended the day citing Golub & Pasachoff for
"coronal structure bounded at roughly 5-10 R_sun" -- and that was the
single weakest return in the nine-source read. Every other source came
back with a figure, an uncertainty and a locatable position. This one
came back with a cavity height near 1 R_sun, a loose corona bound, and
a location given only as "Chapter 1 / Introduction." It did not answer
the question asked, which was the radial extent of helmet streamers.

The read was decisive about what to REMOVE from this row and silent
about what to KEEP. Those are different evidentiary standards: a
removal needs only the ABSENCE of support, while a citation needs its
PRESENCE. We had the first and not the second, and kept citing anyway.

So the row was resting on the one return that failed, while its Note
claimed 6.0 sat inside a range that source bounds. Under the project's
own rule -- a blank with a flag is honest, an unsourced assertion is
not -- the citation goes.

WHAT IT DOES
  1. Removes the `# Source:` / `# Source+:` pair.
  2. Rewrites the Note to say plainly that 6.0 is an ASSUMPTION with no
     verified source, and what would retire it.
  3. Extends the Review-note to record the removal and its reason.
  4. Removes the two `# Cross-checked:` legs. Both cite the citations
     that no longer exist -- Gemini against Golub & Pasachoff, GPT
     against DeForest -- and a cross-check of an absent source grants
     credit for nothing. Their content is preserved in the Review-note
     rather than deleted.

  The value does NOT change. 6.0 renders exactly as before. What
  changes is that the file now says we cannot show where it came from.

EXPECT THE SCANNER TO FLAG THIS ROW. That is the point, not a
regression: an uncited constant SHOULD appear in PROVENANCE_AUDIT.md
as an open Tier-1 finding. It was previously invisible there because
it carried a citation nobody had checked.

The docstring stamp is not touched -- it already names the L-210
reconciliation, and this is that work.

AFTER RUNNING
  python worksheet_checker.py       (Resolved legs: 5 examined, 5 linked)
  python provenance_scanner.py      (expect ONE more Tier-1 finding)
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '9b9743d300070a69aac11229b9392845edb3488a'
TARGET = 'constants_new.py'

# The file AS patch_L210_3 LEAVES IT, not as HEAD has it.
FINGERPRINT_LF = '83fcb0eea33a572ecfa1dc0612e01273'

OLD = (
    "STREAMER_BELT_RADII = 6.0\n"
    "# Source: Golub & Pasachoff, \"The Solar Corona\" (2nd ed., 2010) --\n"
    "# Source+: coronal structure bounded at roughly 5-10 R_sun\n"
    "# Note: VISUALIZATION BOUNDARY, not a physical edge. 6.0 is a drawing\n"
    "#   choice inside the range Golub & Pasachoff bound; streamer-belt\n"
    "#   structure continues beyond it.\n"
    "# Review-note: the previous \"helmet streamers extend 4-6 R_sun\" range\n"
    "#   was removed 2026-08-20 -- an independent source read found it in\n"
    "#   neither cited work. DeForest, Howard & McComas (2014), ApJ 787:124\n"
    "#   was removed with it: its 6 R_sun is the inbound-wave DETECTION\n"
    "#   THRESHOLD, not a streamer extent, and its streamer-belt result is\n"
    "#   an Alfven surface at >= 17 R_sun. That result belongs to\n"
    "#   ALFVEN_SURFACE_RADII (L-209), where it is owed, not to this row.\n"
)

NEW = (
    "STREAMER_BELT_RADII = 6.0\n"
    "# ASSUMPTION -- NO VERIFIED SOURCE (Tony's ruling, 2026-08-20, L-210).\n"
    "# Note: 6.0 R_sun is a VISUALIZATION BOUNDARY carried as a working\n"
    "#   assumption, not a sourced value. It is not a physical edge:\n"
    "#   streamer-belt structure continues beyond whatever radius is\n"
    "#   drawn. The value is unchanged from what this row has always\n"
    "#   rendered; what changed is that the file now says we cannot show\n"
    "#   where it came from. Retire this note by citing a work that\n"
    "#   states a helmet-streamer radial extent, with a locatable\n"
    "#   position in the text -- then the value follows the source\n"
    "#   rather than the source being fitted to the value.\n"
    "# Review-note: this row's entire citation stack was removed on\n"
    "#   2026-08-20 after an independent nine-source read. Recorded here\n"
    "#   because a removal leaves no trace otherwise, and the next reader\n"
    "#   should not have to re-derive why an uncited constant is uncited.\n"
    "#   (a) \"helmet streamers extend 4-6 R_sun\" appeared in neither\n"
    "#   cited work. (b) DeForest, Howard & McComas (2014), ApJ 787:124\n"
    "#   was removed: its 6 R_sun is the inbound-wave DETECTION\n"
    "#   THRESHOLD, not a streamer extent, and its streamer-belt result\n"
    "#   is an Alfven surface at >= 17 R_sun -- a result that belongs to\n"
    "#   ALFVEN_SURFACE_RADII (L-209), where it is owed. (c) Golub &\n"
    "#   Pasachoff, \"The Solar Corona\" (2010) was removed last: asked\n"
    "#   for helmet-streamer extent it returned a cavity height near 1\n"
    "#   R_sun and a loose 5-10 R_sun corona bound, located only as\n"
    "#   \"Chapter 1\" -- the one return in nine that gave no figure, no\n"
    "#   uncertainty and no findable position. (d) The two Cross-checked\n"
    "#   legs went with them: Gemini 2026-08-02 against Golub &\n"
    "#   Pasachoff, GPT 2026-08-02 against DeForest. A cross-check of a\n"
    "#   citation that no longer exists grants credit for nothing.\n"
    "#   The read was decisive about what to REMOVE and silent about what\n"
    "#   to KEEP. Those need different evidence: a removal needs only the\n"
    "#   absence of support, a citation needs its presence.\n"
)

# The two cross-check legs sit below the Resolved leg, which _3 rewrote.
OLD_XC = (
    "# Cross-checked: Gemini 2026-08-02 -- Golub & Pasachoff (worksheet_gemini_constants_remaining.md)\n"
    "# Cross-checked: GPT 2026-08-02 -- DeForest et al. (constants_remaining_independent_verification_gpt.md)\n"
)

NEW_XC = ""

EDITS = [
    ('remove Source, restate Note, extend Review-note', OLD, NEW),
    ('remove the two orphaned Cross-checked legs', OLD_XC, NEW_XC),
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
        fail('%s is not in the state patch_L210_3 leaves it in.\n'
             '  expected md5 %s\n  actual   md5 %s\n'
             '  Run patch_L210_3_unwrap_resolved_legs.py FIRST. If you '
             'already did, something else has moved.'
             % (TARGET, FINGERPRINT_LF, actual))
    print('[base ok] %s  md5 %s  (%s on disk, post-_3 state)'
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

    # The row must now carry NO leg that grants source credit, and must
    # still carry its Resolved leg. Checked by parsing the block, not by
    # trusting that the edits above did what they say.
    block = []
    started = False
    for line in text.split('\n'):
        if line.startswith('STREAMER_BELT_RADII'):
            started = True
            continue
        if started:
            if not line.startswith('#'):
                break
            block.append(line)
    if not block:
        fail('could not read the STREAMER_BELT_RADII comment block back.')

    for banned in ('# Source:', '# Source+:', '# Cross-checked:'):
        offenders = [l for l in block if l.startswith(banned)]
        if offenders:
            fail('%s still present on the row: %r' % (banned, offenders[0]))
    if not any(l.startswith('# Resolved:') for l in block):
        fail('the Resolved leg was lost -- it records why this row is bare.')
    if not any('ASSUMPTION' in l for l in block):
        fail('the assumption declaration is missing.')
    print('[verified] row carries no Source and no Cross-checked leg;')
    print('           Resolved leg intact; assumption declared')

    # Nothing else in the file may lose a citation.
    before_src = lf.decode('ascii').count('\n# Source:')
    after_src = text.count('\n# Source:')
    if before_src - after_src != 1:
        fail('expected exactly 1 Source line to go, %d went.'
             % (before_src - after_src))
    print('[scope ok] exactly one Source line removed file-wide')

    sys.path.insert(0, os.getcwd())
    try:
        import worksheet_keys as wk
    except Exception as exc:
        fail('could not import worksheet_keys to verify: %s' % exc)
    open_label = None
    for number, line in enumerate(text.split('\n'), 1):
        match = wk.LEG_RE.match(line)
        if match:
            open_label = None if match.group(2) else match.group(1)
            continue
        if open_label is not None and wk.continues_a_leg(line):
            fail('unmarked continuation introduced at line %d: %r'
                 % (number, line.strip()))
        open_label = None
    print('[verified] 0 unmarked continuations in the whole file')

    out = text.encode('ascii')
    if ending == b'\r\n':
        out = out.replace(b'\n', b'\r\n')
    with open(TARGET, 'wb') as handle:
        handle.write(out)
    print('[written] %s (%s preserved)'
          % (TARGET, 'CRLF' if ending == b'\r\n' else 'LF'))

    print('')
    print('THE VALUE DID NOT CHANGE. STREAMER_BELT_RADII is still 6.0 and')
    print('renders exactly as before. The row now states that it is an')
    print('assumption rather than implying a provenance it does not have.')
    print('')
    print('EXPECT ONE MORE TIER-1 FINDING from provenance_scanner.py. An')
    print('uncited constant SHOULD appear in the audit. This row was')
    print('invisible there while it carried a citation nobody had checked,')
    print('which is the condition the audit exists to surface.')
    print('')
    print('NEXT:')
    print('  1. python worksheet_checker.py   (5 examined, 5 linked)')
    print('  2. python provenance_scanner.py')
    print('  3. Re-run the maintenance runner')
    print('  4. Move this script to documentation/')


if __name__ == '__main__':
    main()
