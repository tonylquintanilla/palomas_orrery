"""
patch_L253_1_d660_note_strip_and_breadcrumb.py -- L-253, repair.

Removes two figures from `constants_new.py` that the citation beside them
does not support, and opens the ledger row that holds them instead.

WHAT WAS WRONG. `EARTH_D660_DEPTH_KM` carries a `# Ref:` to Ishii et al.
(2019), Nature Geoscience 12:869-872. That reference is real, correctly
transcribed, and true of the constant: the 660 km depth. It is NOT the
source of the two figures in the `# Note:` under it. The +/-60 km lateral
variation came from a review paper that was read and not cited; the 750 km
depression beneath cold slabs came from a DIFFERENT Ishii paper, the 2022
Nature one on the akimotoite-bridgmanite transition. Ishii 2019 is about
the discontinuity's SHARPNESS -- it resolves the transition to about 250 m
-- and says nothing about how the depth varies laterally.

So the block reads as though one citation covers all three claims. That is
the wrong-but-cited failure named in the resident protocol: a citation
that passes the check while asserting a provenance that does not exist.

WHAT REPLACES IT. The Note keeps the qualitative statement, which needs no
citation, and loses both numbers. A bare `# Review-note:` points at L-253
by handle only -- no figure, no paper, no URL -- because the scanner's
SOURCE_PATTERNS treat `# Ref:`, a bare URL, `doi`, `arXiv` and agency
names as citations, and citations attach at block level over a 30-line
lookback. A breadcrumb carrying its candidate references would therefore
register as a citation for the constant beside it and make that value look
better sourced than it is: the same defect, rebuilt deliberately.

The figures and both candidate papers live in L-253, which is outside the
audit, searchable by handle, and RICE-scorable against everything else.

RUN COMMAND (save this file into the repo root -- the same folder as
constants_new.py and LEDGER_CONSOLIDATED.md -- open it in VS Code, click
Run, or from a terminal in that folder):

    python patch_L253_1_d660_note_strip_and_breadcrumb.py

Success prints one `ok` line per edit then `patch applied`. Any failure
prints a single ERROR:/ANCHOR FAIL line and writes NOTHING TO EITHER FILE
-- both files are staged in memory and written only after every edit and
every post-condition has passed.

RUN ORDER: ahead of patch_L249_2. Afterwards run ledger_index.py, which
generates L-253's summary row and its RICE score. Do not hand-add the
index row.

PERMANENT: the edits to both files.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
"""

import hashlib
import os
import sys

CONSTANTS = 'constants_new.py'
LEDGER = 'LEDGER_CONSOLIDATED.md'

# md5 of the LF-normalised bases, orrery 41350019fcc1c5eb714418edd725b9c73bb4fcf8
BASE_FP = {
    CONSTANTS: 'b111a7ca64670d6876d637e048a2d4f5',
    LEDGER: '6767c827c4002cc43da11f35cd97a9ef',
}

NOTE_OLD = b'''# Note: a GLOBAL AVERAGE, not a constant depth. The boundary varies by
# Note+: up to about +/-60 km with mantle temperature and is depressed to
# Note+: roughly 750 km beneath cold subducting slabs. That +/-60 km is
# Note+: an order of magnitude larger than any other uncertainty in this
# Note+: stack and it governs how the lower mantle shell may be reported:
# Note+: the sphere is drawn at one radius because a sphere is what the
# Note+: renderer draws, and the hover says the boundary varies.
# Review-note: single leg (Claude, 2026-08-26). A second independent
# Review-note+: cross-check is owed before this row counts as confirmed.
'''

NOTE_NEW = b'''# Note: a GLOBAL AVERAGE, not a constant depth. The boundary is not
# Note+: uniform: it lies deeper where the mantle is colder and shallower
# Note+: where it is warmer. The shell is drawn at one radius because a
# Note+: sphere is what the renderer draws, and no figure for that
# Note+: variation is stated anywhere in this codebase, because none has
# Note+: been sourced.
# Review-note: single leg (Claude, 2026-08-26). A second independent
# Review-note+: cross-check is owed before this row counts as confirmed.
# Review-note+: Two figures for the variation, and the papers that may
# Review-note+: support them, are held in L-253 -- unsourced, unused, and
# Review-note+: deliberately not restated here or the breadcrumb would
# Review-note+: itself read as a citation for this value.
'''

LEDGER_ANCHOR = b'''**Ref:** L-192 (the three outcomes this extends); L-247 (the founding
case); A Check That Cannot Fail Is Not Passing [CRITICAL].

## PENDING ACTION (Tony-side)
'''

LEDGER_NEW = b'''**Ref:** L-192 (the three outcomes this extends); L-247 (the founding
case); A Check That Cannot Fail Is Not Passing [CRITICAL].

#### [L-253] The 660 discontinuity's depth variation -- held unsourced
<!-- L:253 status:OPEN upd:2026-08-26 section:A flag: rice:2/2/60/2 -->
- **This row IS the breadcrumb.** Tony's ruling, 2026-08-26: keep the
  numbers pending sourcing rather than lose them, but keep them out of
  `constants_new.py`, where a `# Ref:` or a bare URL within thirty lines
  registers as a citation for the constant beside it. The ledger holds
  them at no cost to the audit.
- **What was removed from `constants_new.py`,** and why it had to be.
  `EARTH_D660_DEPTH_KM`'s Note stated that the 660-km discontinuity
  varies by up to about +/-60 km and is depressed to roughly 750 km
  beneath cold subducting slabs. The `# Ref:` beside it -- Ishii, T.,
  Huang, R., Myhill, R. et al. (2019), "Sharp 660-km discontinuity
  controlled by extremely narrow binary post-spinel transition", Nature
  Geoscience 12:869-872, doi 10.1038/s41561-019-0452-1 -- is real and
  true of the 660 km depth, and supports NEITHER figure. That paper
  resolves the transition's sharpness to about 250 m. It is not about
  lateral depth variation at all.
- **The two figures, and where each actually came from.**
  - **+/-60 km lateral variation.** Read in a geoneutrino review
    (arXiv:1310.3732), which states the 660 is a broader transition with
    depth variation of 60 km or less. A review is a secondary source for
    a physical claim; sourcing this properly means going to the 660
    topography seismology literature.
  - **Depression to ~750 km beneath cold slabs.** Stated in the abstract
    of a DIFFERENT paper by the same first author: Ishii, T. et al.,
    "Depressed 660-km discontinuity caused by akimotoite-bridgmanite
    transition", Nature (2022), doi 10.1038/s41586-021-04157-z. One fetch
    against a primary source would settle it.
- **Tony's cost ruling, same day.** The orrery draws one radius. A
  published range it does not draw is outside the bound the artifact
  sets on the audit, so adding these as constants would buy three
  permanent rows against nothing rendered. Qualitative prose carries the
  honesty at no audit cost (text-only assertions are L-194, deferred).
  If ONE figure is ever bought, buy the 750: cheapest citation of the
  three, primary source already located, and the only one that teaches
  something the sphere cannot -- it is why subducting slabs stagnate at
  the transition zone instead of sinking straight through.
- **Note:** RICE 2/2/60/2 is Claude's proposed score. Deliberately low
  reach and confidence: nothing renders from it and the second figure's
  sourcing route is not yet known.
  **Tony-action (decide):** confirm or redirect.
**Gap:** neither figure is sourced and neither is used. Closing this
means either sourcing them and deciding they earn a place, or ruling
that the qualitative statement is the final answer and closing the row
as declined. Both are closures; leaving it open is not.
**Ref:** L-249 (the migration that surfaced it); L-194 (text-only
assertions); L-240 (measured vs declared); Fetched vs Recalled and Show
the Envelope of the Unknowable, resident protocol Part 3;
`constants_new.py::EARTH_D660_DEPTH_KM`.

## PENDING ACTION (Tony-side)
'''

DOC_ANCHOR = (b'Review-note, and an UNMATCHED cross-check on '
              b'SGR_A_DISTANCE_PC removed)\n')

DOC_STAMP = (b'Review-note, and an UNMATCHED cross-check on '
             b'SGR_A_DISTANCE_PC removed)\n'
             b'Module updated: August 26, 2026 with Anthropic\'s Claude Opus 5\n'
             b'(L-253: two figures removed from EARTH_D660_DEPTH_KM\'s Note that\n'
             b'the Ishii 2019 reference beside them does not support. The Note\n'
             b'keeps the qualitative statement; the figures and their candidate\n'
             b'papers move to the ledger, which is outside the audit)\n')


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def load(name):
    """Read and verify one target. Returns (data, is_crlf) or (None, None)."""
    if not os.path.exists(name):
        print('ERROR: %s not found. Save this script into the repo root, '
              'beside constants_new.py and LEDGER_CONSOLIDATED.md.' % name)
        return (None, None)
    with open(name, 'rb') as handle:
        data = handle.read()
    fp = fingerprint(data)
    if fp != BASE_FP[name]:
        print('ERROR: BASE MOVED. %s fingerprints %s, expected %s.'
              % (name, fp, BASE_FP[name]))
        print('       Nothing written to either file. If this patch already '
              'ran, that is the expected result of a second run.')
        return (None, None)
    is_crlf = data.count(b'\r\n') > 0
    print('ok   base fingerprint %s (%s, %d bytes, %s)'
          % (fp, name, len(data), 'CRLF' if is_crlf else 'LF'))
    return (data, is_crlf)


def apply_edits(data, is_crlf, edits):
    """Apply anchored edits to one file's bytes. Returns data or None."""
    for label, old, new in edits:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, got %d: %r'
                  % (label, count, old[:60]))
            print('             Nothing written to either file.')
            return None
        data = data.replace(old, new, 1)
        print('ok   %s' % label)
    return data


def main():
    constants, c_crlf = load(CONSTANTS)
    if constants is None:
        return 1
    ledger, l_crlf = load(LEDGER)
    if ledger is None:
        return 1

    constants = apply_edits(constants, c_crlf, [
        ('D660 note -- two unsupported figures removed', NOTE_OLD, NOTE_NEW),
        ('constants docstring stamp', DOC_ANCHOR, DOC_STAMP),
    ])
    if constants is None:
        return 1

    ledger = apply_edits(ledger, l_crlf, [
        ('L-253 detail block', LEDGER_ANCHOR, LEDGER_NEW),
    ])
    if ledger is None:
        return 1

    for raw in (NOTE_NEW, LEDGER_NEW, DOC_STAMP):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    # Post-conditions, read off the staged bytes rather than the literals.
    c_text = constants.decode('ascii').replace('\r\n', '\n')
    l_text = ledger.decode('ascii').replace('\r\n', '\n')

    # The whole point of the patch: neither figure survives in the D660 block.
    start = c_text.index('EARTH_D660_DEPTH_KM = 660.0')
    block = c_text[start:c_text.index('EARTH_LOWER_MANTLE_KM', start)]
    # '60 km' would be the obvious pattern and it is WRONG: it is a
    # substring of the legitimate '660 km'. Match the removed phrasings.
    for figure in ('+/-60', '750'):
        if figure in block:
            print('ERROR: post-condition -- %r still present in the D660 '
                  'block.' % figure)
            return 1
    print('ok   post-condition -- neither unsupported figure survives')

    # And the breadcrumb must not itself be a citation.
    review = '\n'.join(line for line in block.split('\n')
                       if line.startswith('# Review-note'))
    for pattern in ('http', 'doi', 'arXiv', 'Nature', '10.1038'):
        if pattern in review:
            print('ERROR: post-condition -- the Review-note carries %r, '
                  'which the scanner reads as a citation.' % pattern)
            return 1
    if 'L-253' not in review:
        print('ERROR: post-condition -- the Review-note does not name L-253.')
        return 1
    print('ok   post-condition -- breadcrumb names L-253 and cites nothing')

    # Both figures must have landed in the ledger, or they are simply lost.
    row_start = l_text.index('#### [L-253]')
    row = l_text[row_start:l_text.index('## PENDING ACTION', row_start)]
    for figure in ('60 km', '750 km', '10.1038/s41586-021-04157-z',
                   '10.1038/s41561-019-0452-1'):
        if figure not in row:
            print('ERROR: post-condition -- %r did not reach the L-253 row; '
                  'the breadcrumb would be empty.' % figure)
            return 1
    if '<!-- L:253 ' not in row:
        print('ERROR: post-condition -- L-253 has no metadata comment, so '
              'ledger_index.py will not index it.')
        return 1
    print('ok   post-condition -- L-253 holds both figures, both papers, '
          'and its metadata')

    if l_text.count('#### [L-253]') != 1:
        print('ERROR: post-condition -- L-253 appears %d times.'
              % l_text.count('#### [L-253]'))
        return 1
    print('ok   post-condition -- L-253 handle is unique')

    with open(CONSTANTS, 'wb') as handle:
        handle.write(constants)
    with open(LEDGER, 'wb') as handle:
        handle.write(ledger)
    print('patch applied (%s %d bytes, %s %d bytes)'
          % (CONSTANTS, len(constants), LEDGER, len(ledger)))
    print('')
    print('Next: python ledger_index.py  -- it generates L-253\'s summary row')
    print('and RICE score. Then patch_L249_2.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
