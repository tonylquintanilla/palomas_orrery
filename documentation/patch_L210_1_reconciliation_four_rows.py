"""patch_L210_1_reconciliation_four_rows.py

Built on 3586970dd841d5b417f8e6f59de4d3e3d440d001 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5.

Transactional, all-or-nothing, binary I/O. Both targets are pure LF and
pure ASCII at the base SHA and stay that way. Nothing is written unless
every anchor in every file matches exactly once.

WHAT IT DOES -- L-210, the four pilot citation findings, all four
decided by Tony on 2026-08-20 after a Gemini source read
(worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md).

  constants_new.py
    1. EARTH_EQUATORIAL_RADIUS_KM 6378.137 -> 6378.1366. Source moves
       from IAU B3 to IERS Conventions, matching the polar row's shape.
       B3's rounding and the IERS uncertainty go in the Note.
    2. STREAMER_BELT_RADII value HELD at 6.0, restated as an explicit
       drawing choice. DeForest dropped -- its 6 R_sun is a detection
       threshold, and its streamer-belt result (Alfven surface >= 17
       R_sun) belongs to L-209, not here. The unsourced 4-6 R_sun range
       removed; Golub & Pasachoff kept for what it supports.
    3. BENNU_RADIUS_KM 0.246 -> 0.24503, quoting Barnouin et al. 2019.
       The Source+ line crediting OLA with restated radar figures is
       removed. The GPT Cross-checked leg becomes a Resolved leg: GPT
       REFUSED this row in August and the row was corrected in
       response, which is Resolved, not Cross-checked.
    4. HAUMEA_RADIUS_KM 715 -> 798, DERIVED from Ortiz et al. 2017
       semi-axes (the paper publishes no mean radius). The unsourced
       1050x840x537 axes are removed. Lockwood's 715 recorded as the
       older solution.

  test_constants_provenance.py
    5. The Earth pin literal follows the value, and its docstring stops
       attributing it to IAU B3 / WGS-84.
    6. SIX assertions deleted. Each asserts CENTER_BODY_RADII[body] has
       not diverged from its standalone constant -- but the dict HOLDS
       the constant by reference, so every one is x == x and cannot
       fail. They were written for a shadow that does not exist. The
       literal pins beside them are the checks that can actually fail
       and they stay. (Tony's ruling, 2026-08-20.)

  Both files get their currency stamp updated in the same transaction
  (Stamp What You Change, safe-file-editing 1.6).

NOT IN SCOPE, deliberately
  CENTER_MARKER_SIZE carries a GPT cross-check citing the NASA Sun Fact
  Sheet, on a row in no worksheet. Reported, not touched -- no ruling.
  The wider finding (14 of 23 GPT 2026-08-02 legs written over
  refusals that were then acted on) is a handoff note, not an item.

AFTER RUNNING
  python -m py_compile constants_new.py test_constants_provenance.py
  python test_constants_provenance.py     (expect the Earth pin to pass
                                           at the new value)
  python provenance_scanner.py            (Bennu may drop V2 -> V1; that
                                           is the false leg leaving)
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '3586970dd841d5b417f8e6f59de4d3e3d440d001'
WORKSHEET = 'worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md'

CONSTANTS = 'constants_new.py'
TESTS = 'test_constants_provenance.py'

FINGERPRINTS = {
    CONSTANTS: '1a35d258669ecf4adf17341a2386bf1d',
    TESTS: '8fe8716c915bc3d038b7d205751a8c5b',
}

# ------------------------------------------------------------------
# 1 -- EARTH_EQUATORIAL_RADIUS_KM
# ------------------------------------------------------------------

EARTH_OLD = (
    "EARTH_EQUATORIAL_RADIUS_KM = 6378.137\n"
    "# Source: IAU 2015 Resolution B3 -- nominal terrestrial equatorial radius\n"
    "# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
    "# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html\n"
    "# Note: B3 rounds to 6378.1 km; full precision from IERS Conventions\n"
)

EARTH_NEW = (
    "EARTH_EQUATORIAL_RADIUS_KM = 6378.1366\n"
    "# Source: IERS Conventions (2010), Petit & Luzum (eds.), IERS Technical\n"
    "#   Note No. 36, Table 1.1; IAU B3 rounds to 6378.1 km\n"
    "# Ref: Prsa et al. 2016, AJ 152:41 (arXiv:1605.09788)\n"
    "# Also: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html\n"
    "# Note: IERS publishes 6378136.6 +/- 0.1 m. IAU B3's 6.3781e6 m is an\n"
    "#   exact nominal conversion constant, not a measurement, and the two\n"
    "#   differ by 36.6 m.\n"
    "# Resolved: %s constants_new.py::EARTH_EQUATORIAL_RADIUS_KM -- Source\n"
    "#   moved from IAU B3 to IERS and value taken to IERS precision (L-210)\n"
) % WORKSHEET

# ------------------------------------------------------------------
# 2 -- STREAMER_BELT_RADII (value held)
# ------------------------------------------------------------------

STREAMER_OLD = (
    "STREAMER_BELT_RADII = 6.0\n"
    "# Source: Golub & Pasachoff (2010); DeForest, Howard & McComas (2014), ApJ 787:124\n"
    "# See: Eclipse observations; helmet streamers extend 4-6 R_sun\n"
    "# Note: Visualization cutoff at upper end of 4-6 R_sun observed range;\n"
    "#   streamer-belt structure remains observable beyond 6 R_sun.\n"
)

STREAMER_NEW = (
    "STREAMER_BELT_RADII = 6.0\n"
    "# Source: Golub & Pasachoff, \"The Solar Corona\" (2nd ed., 2010) --\n"
    "#   coronal structure bounded at roughly 5-10 R_sun\n"
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
    "# Resolved: %s constants_new.py::STREAMER_BELT_RADII -- value held,\n"
    "#   inverted citation removed, range withdrawn as unsourced (L-210)\n"
) % WORKSHEET

# ------------------------------------------------------------------
# 3 -- BENNU_RADIUS_KM
# ------------------------------------------------------------------

BENNU_OLD = (
    "BENNU_RADIUS_KM = 0.246\n"
    "# Source: Nolan et al. 2013 (radar shape model), mean diameter 492 +/- 20 m\n"
    "# Source+: Confirmed by OSIRIS-REx OLA: mean radius 246 +/- 10 m, V = 0.062 km^3\n"
    "# Corrected 2026-08-02: 0.262 -> 0.246 (prior value matched no published source)\n"
    "# Cross-checked: Claude 2026-08-02 -- Nolan et al. (worksheet_claude_constants_new.md)\n"
    "# Cross-checked: GPT 2026-08-02 -- OSIRIS-REx (constants_new_citation_verification_gpt.md)\n"
)

BENNU_NEW = (
    "BENNU_RADIUS_KM = 0.24503\n"
    "# Source: Barnouin et al. 2019, Nature Geoscience 12:247, Table 1 --\n"
    "#   mean radius 245.03 +/- 0.08 m from OSIRIS-REx OLA and imaging\n"
    "# Note: supersedes the pre-encounter radar shape model of Nolan et al.\n"
    "#   2013, Icarus 226:629 (mean diameter 492 +/- 20 m, implying ~0.246\n"
    "#   km), which this row previously carried. The mission figure is\n"
    "#   independently derived, not a restatement of the radar result.\n"
    "# Corrected 2026-08-02: 0.262 -> 0.246 (prior value matched no published source)\n"
    "# Corrected 2026-08-20: 0.246 -> 0.24503 (OSIRIS-REx supersedes radar)\n"
    "# Cross-checked: Claude 2026-08-02 -- Nolan et al. (worksheet_claude_constants_new.md)\n"
    "# Review-note: a `Cross-checked: GPT 2026-08-02 -- OSIRIS-REx` leg was\n"
    "#   removed here 2026-08-20. GPT REFUSED this row in that worksheet;\n"
    "#   the row was then corrected in response. A verdict that causes an\n"
    "#   edit is Resolved, not Cross-checked -- but Resolved did not exist\n"
    "#   until L-200 (2026-08-17), so there was no correct leg to write at\n"
    "#   the time. Recorded rather than treated as bad faith.\n"
    "# Resolved: %s constants_new.py::BENNU_RADIUS_KM -- value superseded by\n"
    "#   mission data, misattributed OLA confirmation removed (L-210)\n"
) % WORKSHEET

# ------------------------------------------------------------------
# 4 -- HAUMEA_RADIUS_KM
# ------------------------------------------------------------------

HAUMEA_OLD = (
    "HAUMEA_RADIUS_KM = 715\n"
    "# Source: JPL SSD mean radius (Lockwood et al. 2014)\n"
    "# Source+: Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km\n"
    "# Source+: JPL SSD publishes 715; equatorial 870\n"
    "# Corrected 2026-08-02: 816 -> 715 per JPL SSD (prior value matched neither axes nor database)\n"
)

HAUMEA_NEW = (
    "HAUMEA_RADIUS_KM = 798\n"
    "# Source: Ortiz et al. 2017, Nature 550:219 (stellar occultation) --\n"
    "#   semi-axes 1161 +/- 30, 852 +/- 4, 513 +/- 16 km\n"
    "# Derived: volume-equivalent radius (1161 * 852 * 513)^(1/3) = 797.6 km,\n"
    "#   rounded to 798. Ortiz publishes the semi-axes and no mean radius, so\n"
    "#   this value is COMPUTED here rather than quoted.\n"
    "# Note: VISUALIZATION VALUE, and the two shape solutions differ by ~11%%\n"
    "#   in radius. Lockwood et al. 2014, Earth Moon Planets 111:127 publishes\n"
    "#   715 km directly and is what JPL SSD adopted; the 2017 occultation is\n"
    "#   the only direct measurement. 798 is chosen for that reason.\n"
    "# Review-note: an unsourced \"1050x840x537 km -> geometric mean 779.5 km\"\n"
    "#   line was removed 2026-08-20. Those axes match NO published shape\n"
    "#   model -- Lockwood gives 960x770x495, Ortiz 1161x852x513 -- yet the\n"
    "#   779.5 computes correctly FROM them, so valid arithmetic on numbers\n"
    "#   with no source left no trace a reader or scanner could catch.\n"
    "#   Beware also the widespread secondary-source error of reading Ortiz's\n"
    "#   semi-axes as full axes, which halves Haumea to ~399 km.\n"
    "# Corrected 2026-08-02: 816 -> 715 per JPL SSD (prior value matched neither axes nor database)\n"
    "# Corrected 2026-08-20: 715 -> 798 per the 2017 occultation\n"
    "# Resolved: %s constants_new.py::HAUMEA_RADIUS_KM -- moved to the\n"
    "#   occultation solution, unsourced axes removed (L-210)\n"
) % WORKSHEET

# ------------------------------------------------------------------
# 5 -- the Earth pin follows the value
# ------------------------------------------------------------------

PIN_OLD = (
    "def test_center_body_radii_earth():\n"
    "    \"\"\"IAU 2015 nominal equatorial (WGS-84). Hybrid convention: EQUATORIAL not volumetric (6371.0).\"\"\"\n"
    "    assert CENTER_BODY_RADII['Earth'] == 6378.137, \\\n"
    "        f\"CENTER_BODY_RADII['Earth'] = {CENTER_BODY_RADII['Earth']}. \" \\\n"
    "        f\"If this is 6371.0, the pre-April-16 volumetric-mean convention returned.\"\n"
    "    # Cross-check with standalone constant\n"
    "    assert CENTER_BODY_RADII['Earth'] == EARTH_EQUATORIAL_RADIUS_KM, \\\n"
    "        \"CENTER_BODY_RADII['Earth'] and EARTH_EQUATORIAL_RADIUS_KM have diverged\"\n"
)

PIN_NEW = (
    "def test_center_body_radii_earth():\n"
    "    \"\"\"IERS Conventions (2010) equatorial radius. Hybrid convention:\n"
    "    EQUATORIAL not volumetric (6371.0). The literal below is the whole\n"
    "    check -- CENTER_BODY_RADII['Earth'] IS EARTH_EQUATORIAL_RADIUS_KM by\n"
    "    reference, so comparing the two cannot fail and is not attempted.\"\"\"\n"
    "    assert CENTER_BODY_RADII['Earth'] == 6378.1366, \\\n"
    "        f\"CENTER_BODY_RADII['Earth'] = {CENTER_BODY_RADII['Earth']}. \" \\\n"
    "        f\"If this is 6371.0, the pre-April-16 volumetric-mean convention returned.\"\n"
)

# ------------------------------------------------------------------
# 6 -- the five remaining tautologies
# ------------------------------------------------------------------

SUN_TAUT_OLD = (
    "        f\"CENTER_BODY_RADII['Sun'] drifted to {CENTER_BODY_RADII['Sun']}\"\n"
    "    # Cross-check with standalone SUN_RADIUS_KM\n"
    "    assert CENTER_BODY_RADII['Sun'] == SUN_RADIUS_KM, \\\n"
    "        \"CENTER_BODY_RADII['Sun'] and SUN_RADIUS_KM have diverged\"\n"
)

SUN_TAUT_NEW = (
    "        f\"CENTER_BODY_RADII['Sun'] drifted to {CENTER_BODY_RADII['Sun']}\"\n"
)

JUP_TAUT_OLD = (
    "        f\"If this is 69911, the pre-April-16 volumetric-mean convention returned.\"\n"
    "    # Cross-check with standalone constant\n"
    "    assert CENTER_BODY_RADII['Jupiter'] == JUPITER_EQUATORIAL_RADIUS_KM, \\\n"
    "        \"CENTER_BODY_RADII['Jupiter'] and JUPITER_EQUATORIAL_RADIUS_KM have diverged\"\n"
)

JUP_TAUT_NEW = (
    "        f\"If this is 69911, the pre-April-16 volumetric-mean convention returned.\"\n"
)

SECTION9_OLD = (
    "# Checks that constants_new.py internal consistency holds across sections.\n"
    "\n"
    "def test_earth_equatorial_matches_center_body():\n"
    "    \"\"\"EARTH_EQUATORIAL_RADIUS_KM and CENTER_BODY_RADII['Earth'] must agree.\"\"\"\n"
    "    assert EARTH_EQUATORIAL_RADIUS_KM == CENTER_BODY_RADII['Earth'], \\\n"
    "        \"EARTH_EQUATORIAL_RADIUS_KM != CENTER_BODY_RADII['Earth'] -- internal inconsistency\"\n"
    "\n"
    "\n"
    "def test_jupiter_equatorial_matches_center_body():\n"
    "    \"\"\"JUPITER_EQUATORIAL_RADIUS_KM and CENTER_BODY_RADII['Jupiter'] must agree.\"\"\"\n"
    "    assert JUPITER_EQUATORIAL_RADIUS_KM == CENTER_BODY_RADII['Jupiter'], \\\n"
    "        \"JUPITER_EQUATORIAL_RADIUS_KM != CENTER_BODY_RADII['Jupiter'] -- internal inconsistency\"\n"
    "\n"
    "\n"
    "def test_sun_radius_matches_center_body():\n"
    "    \"\"\"SUN_RADIUS_KM and CENTER_BODY_RADII['Sun'] must agree.\"\"\"\n"
    "    assert SUN_RADIUS_KM == CENTER_BODY_RADII['Sun'], \\\n"
    "        \"SUN_RADIUS_KM != CENTER_BODY_RADII['Sun'] -- internal inconsistency\"\n"
    "\n"
    "\n"
    "def test_earth_polar_less_than_equatorial():\n"
)

SECTION9_NEW = (
    "# Checks that constants_new.py internal consistency holds across sections.\n"
    "#\n"
    "# Three tests were DELETED here on 2026-08-20 (L-210, Tony's ruling).\n"
    "# They asserted that EARTH_EQUATORIAL_RADIUS_KM, JUPITER_EQUATORIAL_\n"
    "# RADIUS_KM and SUN_RADIUS_KM each agreed with their CENTER_BODY_RADII\n"
    "# entry. But that dict holds each constant BY REFERENCE, so every one\n"
    "# was x == x: three test names promising a divergence check that could\n"
    "# not fail. They were written for a shadow copy this file does not\n"
    "# have. Two more of the same shape were deleted from Section 8, where\n"
    "# the literal pins beside them are the checks that can actually fail.\n"
    "# Do not restore them: if CENTER_BODY_RADII ever stops referencing the\n"
    "# constants, the fix is to make it reference them again, not to add a\n"
    "# test that watches the copy drift.\n"
    "\n"
    "def test_earth_polar_less_than_equatorial():\n"
)

# ------------------------------------------------------------------
# CURRENCY -- both files
# ------------------------------------------------------------------

CONST_STAMP_OLD = (
    "Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: 14\n"
)

CONST_STAMP_NEW = (
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-210:\n"
    "EARTH_EQUATORIAL_RADIUS_KM to IERS precision, BENNU_RADIUS_KM to the\n"
    "OSIRIS-REx figure, HAUMEA_RADIUS_KM to the 2017 occultation,\n"
    "STREAMER_BELT_RADII held with its unsourced range withdrawn). Built on\n"
    "3586970d.\n"
    "Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: 14\n"
)

EDITS = [
    (CONSTANTS, 'EARTH_EQUATORIAL_RADIUS_KM', EARTH_OLD, EARTH_NEW),
    (CONSTANTS, 'STREAMER_BELT_RADII (value held)', STREAMER_OLD, STREAMER_NEW),
    (CONSTANTS, 'BENNU_RADIUS_KM', BENNU_OLD, BENNU_NEW),
    (CONSTANTS, 'HAUMEA_RADIUS_KM', HAUMEA_OLD, HAUMEA_NEW),
    (CONSTANTS, 'CURRENCY: constants_new docstring', CONST_STAMP_OLD,
     CONST_STAMP_NEW),
    (TESTS, 'Earth pin follows the value', PIN_OLD, PIN_NEW),
    (TESTS, 'delete Sun tautology', SUN_TAUT_OLD, SUN_TAUT_NEW),
    (TESTS, 'delete Jupiter tautology', JUP_TAUT_OLD, JUP_TAUT_NEW),
    (TESTS, 'delete Section 9 tautologies', SECTION9_OLD, SECTION9_NEW),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    for path in (CONSTANTS, TESTS):
        if not os.path.isfile(path):
            fail('%s not found. Run this from the repo root.' % path)

    originals = {}
    for path, expected in FINGERPRINTS.items():
        with open(path, 'rb') as handle:
            data = handle.read()
        actual = hashlib.md5(data).hexdigest()
        if actual != expected:
            fail('%s does not match the base at %s.\n'
                 '  expected md5 %s\n  actual   md5 %s\n'
                 '  Reconcile against HEAD before running this.'
                 % (path, BASE_SHA[:8], expected, actual))
        originals[path] = data
        print('[base ok] %-30s md5 %s' % (path, actual))

    for path, data in originals.items():
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('%s carries non-ASCII at offset %d.' % (path, exc.start))
        print('[ascii ok] %s' % path)

    working = dict((p, d.decode('ascii')) for p, d in originals.items())
    for path, label, old, new in EDITS:
        count = working[path].count(old)
        if count != 1:
            fail('anchor for "%s" in %s matched %d times, expected exactly 1.'
                 % (label, path, count))
        working[path] = working[path].replace(old, new, 1)
        print('[anchor ok] %-34s %s' % (label, path))

    # Permitted losses derived from the edits, never hand-listed.
    allowed = {}
    for path, label, old, new in EDITS:
        gone = set(old.split('\n')) - set(new.split('\n'))
        allowed.setdefault(path, set()).update(l for l in gone if l)
    for path in (CONSTANTS, TESTS):
        before = originals[path].decode('ascii').split('\n')
        after = set(working[path].split('\n'))
        lost = [l for l in before if l and l not in after]
        unexpected = [l for l in lost if l not in allowed.get(path, set())]
        if unexpected:
            fail('%d line(s) of %s would be lost that no edit claims to '
                 'remove. First: %r'
                 % (len(unexpected), path, unexpected[0]))
        print('[loss ok] %-32s %d line(s) removed, all accounted for'
              % (path, len(lost)))

    # The tautologies must actually be gone, and the real pins must stay.
    t = working[TESTS]
    for phrase in ('have diverged', 'internal inconsistency'):
        if phrase in t:
            fail('a tautological assertion survived: %r still present in %s'
                 % (phrase, TESTS))
    for pin in ("CENTER_BODY_RADII['Sun'] == 695700",
                "CENTER_BODY_RADII['Earth'] == 6378.1366",
                "CENTER_BODY_RADII['Jupiter'] == 71492"):
        if pin not in t:
            fail('a literal pin that CAN fail was lost: %r' % pin)
    print('[tautologies gone] 6 removed; 3 literal pins intact')

    # The withdrawn CLAIMS must be gone. Test the exact lines, not the
    # substrings: the Review-note legs quote what was removed on purpose,
    # so a substring test fires on the record of the removal. (Caught by
    # this check on its first run, 2026-08-20.)
    c = working[CONSTANTS]
    withdrawn = [
        "# Source+: Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km",
        "# Source+: JPL SSD publishes 715; equatorial 870",
        "# See: Eclipse observations; helmet streamers extend 4-6 R_sun",
        "# Source+: Confirmed by OSIRIS-REx OLA: mean radius 246 +/- 10 m, V = 0.062 km^3",
        "# Cross-checked: GPT 2026-08-02 -- OSIRIS-REx (constants_new_citation_verification_gpt.md)",
    ]
    for line in withdrawn:
        if line in c:
            fail('a withdrawn line survived in %s: %r' % (CONSTANTS, line))
    # And the DeForest CITATION must be off this row, though the
    # Review-note still names it.
    if 'Source: Golub & Pasachoff (2010); DeForest' in c:
        fail('the DeForest citation is still on the STREAMER_BELT Source line')
    print('[withdrawn claims gone] 5 lines + the DeForest citation; '
          'Review-note records survive')

    for path in (CONSTANTS, TESTS):
        with open(path, 'wb') as handle:
            handle.write(working[path].encode('ascii'))
        print('[written] %s' % path)

    print('')
    print('VALUES CHANGED (3 of 4 rows; STREAMER_BELT_RADII held at 6.0):')
    print('  EARTH_EQUATORIAL_RADIUS_KM  6378.137  -> 6378.1366')
    print('  BENNU_RADIUS_KM             0.246     -> 0.24503')
    print('  HAUMEA_RADIUS_KM            715       -> 798')
    print('')
    print('CURRENCY STAMPS UPDATED (Stamp What You Change):')
    print('  %s -- Module updated line, Claude Opus 5, built on %s'
          % (CONSTANTS, BASE_SHA[:8]))
    print('  %s -- test docstring restated; see Section 9 comment' % TESTS)
    print('')
    print('NEXT:')
    print('  1. python -m py_compile constants_new.py '
          'test_constants_provenance.py')
    print('  2. python test_constants_provenance.py')
    print('  3. python provenance_scanner.py  '
          '(BENNU may drop V2 -> V1 -- that is the false leg leaving)')
    print('  4. File the Gemini return as documentation/worksheets/%s'
          % WORKSHEET)
    print('     -- FOUR Resolved legs now cite it by name.')
    print('  5. Move this script to documentation/')


if __name__ == '__main__':
    main()
