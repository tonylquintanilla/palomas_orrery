"""patch_L196_14_claim_vocabulary.py -- teach the scanner the units it
was missing, then re-pin everything the change re-points.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
provenance_scanner.py), open it in VS Code, and click Run.

    python patch_L196_14_claim_vocabulary.py

WHAT WAS WRONG
--------------
The scanner finds a numeric claim by matching a number immediately
followed by a unit from a fixed list. That list carried AU, km, solar
radii and Earth radii, but not per-body radii (Mars radii, Mercury
radii, lunar radii), not the spelled-out word kilometers, and it could
not see across an intervening word, so "1.08 million km" failed where
"1.08 km" passed.

The result was ten annotated sites that produced ZERO worksheet rows.
Not one of them was empty: Mars's Hill sphere at 319.2 Mars radii,
Mercury's sodium tail at 120-1,400 Mercury radii, the Moon's Hill
sphere at 60,000 kilometers and 34.53 lunar radii, Venus's Hill sphere
at about 1 million kilometers, and Mars's bow shock at 1.6 Mars radii.
The checker routed those sites; the builder never asked about them.

A second, separate defect sat in the same pattern. It ended with a word
boundary that applied to every alternative including the percent sign.
A word boundary after '%' requires a word character next to it, so
"96% of the sunlight" matched nothing while "96%x" matched. Every
percentage followed by a space or a period was invisible.

WHAT IT DOES
------------
Four changes to the pattern, and nothing else:

  1. Per-body radii, via "<word> radii" and bare "radii".
  2. The spelled-out kilometer / kilometre, singular and plural.
  3. An optional magnitude word -- thousand, million, billion,
     trillion -- between the number and its unit.
  4. The trailing word boundary becomes a negative lookahead for a
     word character, which is what '%' needed and what every other
     alternative already had in effect.

Then EXTRACTOR_VERSION goes 1 -> 2, because the claim ordinal in every
issued key counts claims AFTER this filter runs, so the meaning of
"::c2" changes for any string that gained a claim ahead of an existing
one. Mars's bow shock is the clear case: '15' was claim 1 and is now
claim 2, behind the newly visible '1.6 Mars radii'.

Then documentation/worksheets/L192_extractor_pins.txt is regenerated,
by calling the project's own repin_text() rather than by writing the
file from this script's idea of the format.

MEASURED BEFORE DELIVERY, ON THE WHOLE TREE
-------------------------------------------
  gained   728 matches in 64 files -- percentages, per-body radii,
           spelled kilometres, magnitude phrases, and one surface
           gravity in m/s^2 that the old boundary rejected
  lost      16 matches, every one a false positive: percent-encoded
           URLs ("...sstr=2024%20PT5" read as the claim "2024%") and
           Python format placeholders ("#2 %s spacecraft ...")
  lost real claims: none

  scanner Tier-1     206 -> 289, risen in 23 files
  worksheet checker  59 of 102 routed / 3 clean -> 68 of 110 / 8 clean
  dispatch corpus    64 rows over 42 sites -> 100 rows over 52 sites

The Tier-1 rise is not a regression. Those 83 findings are numeric
claims that were always unsourced and were not being counted, because
the scanner could not see the number at all. The count did not get
worse; it got honest. The push gate reads Tier-1 on the ACTIVE BUILD
PATH, not the tree total, so this does not by itself block a push.

WHY NOW AND NOT LATER
---------------------
No worksheet has ever been issued. None of the 35 worksheets on disk
carries a key. Not one pinned key in L192_key_pins.txt carries an
ordinal. So re-pointing costs nothing today and costs a reissue after
the first dispatch goes out.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the widened pattern, the extractor version bump, and the regenerated
pin file.

SAFETY
------
All-or-nothing with rollback. The two source files are fingerprinted
(CRLF-normalized) and every anchor must match exactly once before
anything is written. The pin file is regenerated afterwards in a
separate interpreter, because the edited modules must be imported
fresh; if that step fails for any reason, all three files are restored
from memory and the run reports the failure.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line, and nothing is left
changed.
"""

import hashlib
import os
import subprocess
import sys


OLD_COMMENT = """# Captures numbers with optional comma separators and decimal parts.
# Comma handling: "31,000 km" is one token, not "31" + "000 km".
"""

NEW_COMMENT = '''# Captures numbers with optional comma separators and decimal parts.
# Comma handling: "31,000 km" is one token, not "31" + "000 km".
#
# WIDENED 2026-08-17 (L-195). Four gaps, each found by a site the
# builder silently produced no row for:
#   - per-body radii. "1.6 Mars radii" was not a claim because only
#     "solar radii" and "Earth radii" were listed by name.
#   - the spelled-out kilometer. Only the abbreviation was listed.
#   - a magnitude word between number and unit. "1.08 million km"
#     failed where "1.08 km" passed.
#   - the trailing \\b applied to '%' as well, and a word boundary
#     after a percent sign requires a word character next to it, so
#     "96% of the sunlight" matched nothing while "96%x" matched. It
#     is now a negative lookahead, which is what the other
#     alternatives already meant.
#
# Measured over the whole tree at the time of the change: 728 matches
# gained, 16 lost, and every one of the 16 was a false positive --
# percent-encoded URLs and %s format placeholders. No real claim was
# lost. EXTRACTOR_VERSION went to 2 with this, because the ordinal in
# an issued key counts claims AFTER this filter runs.
'''

OLD_RE = """NUMERIC_CLAIM_RE = re.compile(
    r'(\\d{1,3}(?:,\\d{3})+(?:\\.\\d+)?|'     # 31,000 or 31,000.5
    r'\\d+(?:\\.\\d+)?(?:[eE][+-]?\\d+)?)'    # 8.33 or 1.5e-3
    r'\\s*'
    r'(degrees?\\s*[CF]\\b|deg\\s*[CF]\\b|\\xb0\\s*[CF]\\b|'
    r'degrees?\\s+(?:Celsius|Fahrenheit)\\b|'
    r'R_sun|AU|km/s|km|m/s|degrees?|deg\\b|arcsec|mas|pc|kpc|Mpc|'
    r'solar radii|Earth (?:masses|radii)|M_sun|M_earth|R_earth|'
    r'ly|light[- ]years?|parsec|'
    r'days?|years?|hours?|minutes?\\b|min\\b|sec\\b|'
    r'K\\b|kelvin|kg\\b|g/cm3|g/cc|'
    r'km/h|mph|people|persons?|percent|%)\\b',
    re.IGNORECASE
)
"""

NEW_RE = """NUMERIC_CLAIM_RE = re.compile(
    r'(\\d{1,3}(?:,\\d{3})+(?:\\.\\d+)?|'     # 31,000 or 31,000.5
    r'\\d+(?:\\.\\d+)?(?:[eE][+-]?\\d+)?)'    # 8.33 or 1.5e-3
    r'(?:\\s*(?:thousand|million|billion|trillion))?'   # 1.08 million km
    r'\\s*'
    r'(degrees?\\s*[CF]|deg\\s*[CF]|\\xb0\\s*[CF]|'
    r'degrees?\\s+(?:Celsius|Fahrenheit)|'
    r'R_sun|AU|km/s|kilometers?|kilometres?|km|m/s|'
    r'degrees?|deg|arcsec|mas|pc|kpc|Mpc|'
    r'solar radii|Earth (?:masses|radii)|M_sun|M_earth|R_earth|'
    r'[A-Za-z]+ radii|radii|'
    r'ly|light[- ]years?|parsec|'
    r'days?|years?|hours?|minutes?|min|sec|'
    r'K|kelvin|kg|g/cm3|g/cc|'
    r'km/h|mph|people|persons?|percent|%)'
    r'(?![A-Za-z0-9_])',
    re.IGNORECASE
)
"""

OLD_VERSION = "EXTRACTOR_VERSION = 1\n"
NEW_VERSION = "EXTRACTOR_VERSION = 2\n"

EDITS = {
    'provenance_scanner.py': {
        'fp': 'ecca453b300fcd6fcede76d866d368a8',
        'edits': [
            (OLD_COMMENT, NEW_COMMENT),
            (OLD_RE, NEW_RE),
        ],
    },
    'worksheet_keys.py': {
        'fp': '77c908b58e2923747506f95a9ee42ec9',
        'edits': [
            (OLD_VERSION, NEW_VERSION),
        ],
    },
}

PIN_FILE = os.path.join('documentation', 'worksheets',
                        'L192_extractor_pins.txt')
PIN_FP = '4530ca540d61570f4a8ffebbbcd322d8'

# Built by concatenation, not by %-formatting: the snippet itself
# contains %d and %s, which an outer format would try to consume.
REPIN = (
    "import test_extractor_pins as t\n"
    "sites = t.parse_sites(t.SITES_DOC)\n"
    "measured, unreadable = t.measure(sites)\n"
    "if unreadable:\n"
    "    raise SystemExit('unreadable modules: ' + repr(unreadable))\n"
    "text = t.repin_text(t.live_header(), measured)\n"
    "open(" + repr(PIN_FILE) + ", 'w', encoding='utf-8', "
    "newline='\\n').write(text)\n"
    "print(str(len(measured)) + ' string sites re-pinned')\n"
)


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile('provenance_scanner.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding provenance_scanner.py).')
        return 1
    if not os.path.isfile(PIN_FILE):
        print('ERROR: %s not found. Nothing written.' % PIN_FILE)
        return 1

    original = {}
    staged = []

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1
        with open(name, 'rb') as handle:
            raw = handle.read()
        original[name] = raw

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. If this patch has already run, '
                  'that is the expected abort -- it is one-shot.')
            return 1

        crlf = b'\r\n' in raw
        text = normalized(raw).decode('utf-8')
        for old, new in spec['edits']:
            count = text.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d.'
                      % (name, count))
                print('       anchor starts: %r' % old[:70])
                print('       Nothing written.')
                return 1
            if non_ascii_count(new):
                print('ERROR: %s -- an inserted block carries non-ASCII. '
                      'Nothing written.' % name)
                return 1
            text = text.replace(old, new)
        out = text.encode('utf-8')
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))

    with open(PIN_FILE, 'rb') as handle:
        original[PIN_FILE] = handle.read()
    pin_fp = hashlib.md5(normalized(original[PIN_FILE])).hexdigest()
    if pin_fp != PIN_FP:
        print('ERROR: %s does not match the base this patch was built '
              'against.' % PIN_FILE)
        print('       expected %s' % PIN_FP)
        print('       found    %s' % pin_fp)
        print('       Nothing written.')
        return 1

    total = 0
    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-34s %d edit(s)' % (name, count))
        total += len(out)

    # The pin file records what the NEW filter keeps, so it has to be
    # built by the edited modules. A fresh interpreter is the only way
    # to import them after this process already imported the old ones.
    result = subprocess.run([sys.executable, '-c', REPIN],
                            capture_output=True, text=True)
    if result.returncode != 0:
        for name in original:
            with open(name, 'wb') as handle:
                handle.write(original[name])
        print('ERROR: re-pinning failed. All files restored, nothing left '
              'changed.')
        print(result.stdout.strip())
        print(result.stderr.strip()[-1500:])
        return 1

    print('ok  %-34s %s' % (PIN_FILE, result.stdout.strip()))
    total += os.path.getsize(PIN_FILE)
    print('patch applied (%d bytes)' % total)
    print('')
    print('Next: run maintenance_run.py. Expect Extractor pins GREEN, '
          'Tier-1 206 -> 289, and the checker at 68 of 110 routed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
