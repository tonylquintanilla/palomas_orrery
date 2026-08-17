"""patch_L195_1_shape_a_swaps.py -- L-195 Shape A. Put the authority on
the line the worksheet verdicts.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
constants_new.py), open it in VS Code, and click Run.

    python patch_L195_1_shape_a_swaps.py

WHAT IT DOES
------------
L-192's Break 5 ruling makes field 3 of a worksheet row verdict the
`# Source:` line and nothing else. That rule is correct wherever the
Source line names an authority, and silently wrong wherever it names an
EVENT instead: the row reads CITATION RIGHT while the actual authority,
sitting one line down in `# Ref:`, is never checked.

Seven blocks in constants_new.py have that shape. This patch swaps them
-- the authority moves up to `# Source:`, the narrative moves down to
`# See:`, which is already a recognised context leg in the builder
(CONTEXT_LEGS, worksheet_request_builder.py). The responder still reads
the narrative; it is no longer the thing being verdicted.

    OUTER_CORONA_RADII      Mann et al. (2004) is the Source
    STREAMER_BELT_RADII     Golub & Pasachoff (2010); DeForest et al.
    ROCHE_LIMIT_RADII       Murray & Dermott (1999), Sec. 4.6
    ALFVEN_SURFACE_RADII    Kasper et al. (2021)
    TERMINATION_SHOCK_AU    Stone et al. (2005)
    HELIOPAUSE_RADII        Gurnett et al. (2013)
    PARKER_CLOSEST_RADII    the JHUAPL mission page

No value changes. No label is invented. Only which line each existing
body sits on, plus the reordering that keeps `# Source:` first in its
block.

THE TWO THAT ARE NOT A PLAIN LABEL SWAP
---------------------------------------
ROCHE_LIMIT_RADII holds a FORMULA on its Source line, not an event, so
there is nothing to demote to `# See:`. The formula moves to
`# Derived:` -- also an existing context leg -- and the arithmetic stays
where it is on `# Calculation:` and its marked continuation.

OUTER_CORONA_RADII is not in the dispatch corpus (it carries no
`# Cross-checked:` line), so it was not one of the six the ruling named.
It is the identical defect in a file this patch already fingerprints,
which is the Fix In Passing case in safe-file-editing 1.4: the fix is
mechanical, the convention is already ruled, and a dedicated sweep for
one block would never be scheduled. (Tony approved it, 2026-08-17.)

HELIOPAUSE_RADII IS TOUCHED, AND ONLY IN ITS CITATION LEGS
----------------------------------------------------------
The value 26148, its `# Note:` unit conversion, and its
`# Corrected 2026-08-02:` record are all left exactly as they are. This
constant is on record as must-not-send-back -- both August checkers
found and fixed a real error in it -- and nothing here disturbs that.

WHAT THIS DOES NOT FIX
----------------------
ROCHE_LIMIT_RADII's two `# Cross-checked:` lines say "formula verified".
After the swap they no longer name the Source. That is honest and it is
the point: the Murray & Dermott leg has not been cross-checked, and now
the file says so instead of hiding it behind a checked-looking row.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot -- it guards on a fingerprint of
a tree that stops existing the moment it succeeds, so a second run
aborts and writes nothing. What it installs is permanent: seven citation
blocks whose verdicted line carries an authority.

SAFETY
------
All-or-nothing. constants_new.py is fingerprinted (CRLF-normalized) and
every anchor must match exactly once before anything is written. Any
mismatch aborts with nothing written. The file's own line endings are
preserved.

One more guard, ahead of the fingerprint: each edit is checked to be a
RELABEL and nothing else -- strip the leg labels from both sides and the
remaining text must be identical, in any order. A dropped line, an added
word, or a reworded citation aborts the run. See bodies() for why that
check is written structurally instead of as a list of citations.

Success: one 'ok' line, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import re
import sys


TARGET = 'constants_new.py'

# md5 of constants_new.py at ce84f05..98b29f0 (CRLF-normalized). The
# file is unchanged across both; it was last touched before this
# session.
BASE_FP = '3d8c743ac68a15aa7b3825f0ef62936f'

# Bottom-up: highest line numbers first. The harness asserts a unique
# match for each anchor, so order does not affect correctness -- it is
# kept because that is how the convention reads.
EDITS = [

    # --- PARKER_CLOSEST_RADII, line 279 ---
    ("""PARKER_CLOSEST_RADII = 9.86
# Source: Parker Solar Probe perihelion 22, Dec 24, 2024
# Ref: https://parkersolarprobe.jhuapl.edu/The-Mission/index.php
""",
     """PARKER_CLOSEST_RADII = 9.86
# Source: https://parkersolarprobe.jhuapl.edu/The-Mission/index.php
# See: Parker Solar Probe perihelion 22, Dec 24, 2024
"""),

    # --- HELIOPAUSE_RADII, line 237. The Note line is carried only to
    # make the anchor unique; it is written back unchanged. ---
    ("""# Note: This is in solar radii, not AU. 121.6 AU * 149597870.7 / 695700 = 26148 R_sun
# Source: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)
# Ref: Gurnett et al. (2013), Science 341:1489
""",
     """# Note: This is in solar radii, not AU. 121.6 AU * 149597870.7 / 695700 = 26148 R_sun
# Source: Gurnett et al. (2013), Science 341:1489
# See: Voyager 1 crossed heliopause at ~121.6 AU (Aug 2012)
"""),

    # --- TERMINATION_SHOCK_AU, line 230 ---
    ("""TERMINATION_SHOCK_AU = 94
# Source: Voyager 1 crossed at 94 AU (Dec 2004)
# Ref: Stone et al. (2005), Science 309:2017
""",
     """TERMINATION_SHOCK_AU = 94
# Source: Stone et al. (2005), Science 309:2017
# See: Voyager 1 crossed at 94 AU (Dec 2004)
"""),

    # --- ALFVEN_SURFACE_RADII, line 215 ---
    ("""ALFVEN_SURFACE_RADII = 18.8
# Source: Parker Solar Probe first crossing, April 28, 2021
# Ref: Kasper et al. (2021), Phys. Rev. Lett. 127:255101
""",
     """ALFVEN_SURFACE_RADII = 18.8
# Source: Kasper et al. (2021), Phys. Rev. Lett. 127:255101
# See: Parker Solar Probe first crossing, April 28, 2021
"""),

    # --- ROCHE_LIMIT_RADII, line 205. Formula to Derived, not See;
    # the Calculation leg and its marked continuation stay adjacent. ---
    ("""ROCHE_LIMIT_RADII = 3.45
# Source: Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3)
# Calculation: 2.44 * 1.0 * (1408/500)^(1/3) = 3.45 R_sun
# Calculation+: Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3
# Ref: Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
""",
     """ROCHE_LIMIT_RADII = 3.45
# Source: Murray & Dermott, "Solar System Dynamics" (1999), Sec. 4.6
# Derived: Fluid Roche limit formula: d = 2.44 * R * (rho_sun/rho_comet)^(1/3)
# Calculation: 2.44 * 1.0 * (1408/500)^(1/3) = 3.45 R_sun
# Calculation+: Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3
"""),

    # --- STREAMER_BELT_RADII, line 197 ---
    ("""STREAMER_BELT_RADII = 6.0
# Source: Eclipse observations; helmet streamers extend 4-6 R_sun
# Ref: Golub & Pasachoff (2010); DeForest, Howard & McComas (2014), ApJ 787:124
""",
     """STREAMER_BELT_RADII = 6.0
# Source: Golub & Pasachoff (2010); DeForest, Howard & McComas (2014), ApJ 787:124
# See: Eclipse observations; helmet streamers extend 4-6 R_sun
"""),

    # --- OUTER_CORONA_RADII, line 191. Fix in passing; outside the
    # dispatch corpus, identical defect shape. ---
    ("""OUTER_CORONA_RADII = 50
# Source: Various; F-corona envelope extends to ~50 R_sun
# Ref: Mann et al. (2004), A&A 414:1127
""",
     """OUTER_CORONA_RADII = 50
# Source: Mann et al. (2004), A&A 414:1127
# See: Various; F-corona envelope extends to ~50 R_sun
"""),
]


# A leg label: '# Source:', '# Calculation+:', '# See:'. Same shape the
# builder's own OTHER_LABEL_RE uses, so this reads a line the way the
# thing downstream reads it.
LABEL_RE = re.compile(r'^#\s*[A-Za-z][A-Za-z0-9_ /.-]{0,30}\+?:\s*')


def bodies(block):
    """Every line of a block with its leg label stripped, sorted.

    This is the invariant a Shape A swap must hold: the swap RELABELS
    and REORDERS, and does nothing else. Compare the two sides of an
    edit and a dropped line, an added word, or a silently reworded
    citation all show up -- while a label moving from Ref to Source, or
    a line changing position, correctly does not.

    Written this way on purpose. The first version of this guard listed
    the citation bodies by hand and was mutation tested by deleting one
    line from one edit: it passed, because the deleted line was not on
    the list. A check that only fails for the cases someone remembered
    is the shape this project has a gate about.
    """
    out = []
    for line in block.split('\n'):
        if not line.strip():
            continue
        out.append(LABEL_RE.sub('', line).strip())
    return sorted(out)


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile(TARGET):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding %s).' % TARGET)
        return 1

    with open(TARGET, 'rb') as handle:
        raw = handle.read()

    fp = hashlib.md5(normalized(raw)).hexdigest()
    if fp != BASE_FP:
        print('ERROR: %s does not match the base this patch was built '
              'against.' % TARGET)
        print('       expected %s' % BASE_FP)
        print('       found    %s' % fp)
        print('       Nothing written. If this patch has already run, '
              'that is the expected abort -- it is one-shot.')
        return 1

    # Structural check on the edits themselves, before the file is
    # touched. Runs on this script's own contents, so it fires even if
    # the anchors never match.
    checked = 0
    for index, (old, new) in enumerate(EDITS, 1):
        if bodies(old) != bodies(new):
            print('ERROR: edit %d is not a relabel -- its text changed.'
                  % index)
            for line in sorted(set(bodies(old)) ^ set(bodies(new))):
                print('       only on one side: %r' % line[:70])
            print('       Nothing written.')
            return 1
        checked += len(bodies(old))

    crlf = b'\r\n' in raw
    text = normalized(raw).decode('utf-8')

    for old, new in EDITS:
        count = text.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d.'
                  % (TARGET, count))
            print('       anchor starts: %r' % old[:70])
            print('       Nothing written.')
            return 1
        if non_ascii_count(new):
            print('ERROR: %s -- an inserted block carries non-ASCII. '
                  'Nothing written.' % TARGET)
            return 1
        text = text.replace(old, new)

    out = text.encode('utf-8')
    pre_existing = non_ascii_count(text)
    if crlf:
        out = out.replace(b'\n', b'\r\n')

    with open(TARGET, 'wb') as handle:
        handle.write(out)

    print('ok  %-38s %d edit(s), %d line bodies preserved'
          % (TARGET, len(EDITS), checked))
    if pre_existing:
        print('note: %s still holds %d non-ASCII character(s) this patch '
              'did not reach' % (TARGET, pre_existing))
    else:
        print('note: %s is ASCII-clean' % TARGET)
    print('patch applied (%d bytes)' % len(out))
    print('')
    print('Next: run worksheet_request_builder.py (the six corpus rows '
          'should now show the authority in the Source column), then '
          'maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
