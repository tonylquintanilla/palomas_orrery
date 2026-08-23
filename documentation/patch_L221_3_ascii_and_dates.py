"""patch_L221_3_ascii_and_dates.py

Built on f504c06446edddb19dce0c906b229c96387a8406 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6.
Both confirmed by live git ls-remote.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into documentation/ -- the SAME folder as the two files it
    edits -- open in VS Code, click Run.
    Equivalent command: python patch_L221_3_ascii_and_dates.py
    Both targets are resolved beside this script.

    (patch_L221_2 was written the same way and still got saved to the
    repo root first. It aborted cleanly and said why, which is the
    behaviour that is wanted, but the instruction clearly did not carry.
    Hence the louder note here.)

Transactional, all-or-nothing, binary I/O, two targets. Nothing is
written to EITHER file unless every anchor in BOTH matches exactly once.

WHY THIS PATCH EXISTS -- two corrections to patch_L221_2 and one
carried obligation.

  1. THE ASCII SWEEP THAT SHOULD HAVE BEEN IN PATCH 2.
     Patch 2 reported 23 non-ASCII bytes and declined to sweep them,
     arguing the encoding gate is scoped to delivered code. Tony's
     ruling, 2026-08-23: when a patch is already holding a file open,
     incidental non-ASCII gets fixed. That is what Fix In Passing
     says, and safe-file-editing's Stamp What You Change is explicit
     that markdown is not an exception -- it is where the rule was
     earned. The earlier reading was too narrow.

     22 x U+2032 PRIME and 1 x U+2033 DOUBLE PRIME, all in the
     "B-prime" architecture name. They become ASCII ' and ''.
     Section 5a already spelled the same name B' so this makes the
     document self-consistent rather than imposing a new convention.

  2. THE DATE. Patch 2 stamped its own authorship 2026-08-22
     throughout. It ran on 2026-08-23. The braid was RULED on the
     22nd, so ruling dates stay; but "Last updated", the measurement
     dates and the v19 lineage date were all the 23rd and were wrong.
     Sixteen of the 24 date strings in the file are ruling dates and
     are correct as written. Eight are authorship or measurement
     dates and move to the 23rd. They are separated one by one below
     rather than swept, because the distinction is the whole point.

  3. THE ANCHORS GAIN THEIR PUSHED SHA. v19 was BUILT on 38923c1 and
     PUSHED at f504c064. The handoff convention is "built on <SHA>;
     pushed at <new SHA>" and the built-on half alone leaves a reader
     unable to find the document being described.

  4. THE SUMMARY'S BROKEN POINTER (carried obligation, 2+ sessions).
     MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md line 20 points at
     CRITICAL_PATH_SUMMARY.md. No file of that name has ever existed;
     it is MASTER_PLAN_CRITICAL_PATH_SUMMARY.md. That file is a dated
     snapshot whose own rule is that it does not rewrite its past, so
     its currency block is NOT restamped -- a broken pointer is not an
     overtaken claim, and the correction is recorded in a dated line
     at the foot instead.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. What it installs is permanent: an
  ASCII-clean master plan, honest authorship dates, and a pointer that
  resolves.

AFTER RUNNING
  1. Read the output; every line should say ok.
  2. Commit and push both files.
  3. Move this script to documentation/ if it is not already there.
"""

import hashlib
import os
import sys

BASE_SHA = 'f504c06446edddb19dce0c906b229c96387a8406'
GALLERY_SHA = '02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6'
BUILT_ON = '38923c1'          # what v19 was written against
PUSHED_AT = 'f504c06'         # where v19 landed

HERE = os.path.dirname(os.path.abspath(__file__))

PLAN = 'MASTER_PLAN_INTERACTIVE_GALLERY.md'
SUMMARY = 'MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md'

FINGERPRINTS = {
    PLAN: '716e20fd8965ef82b581fdee8c5457a9',
    SUMMARY: '108897ecbab2e3e20b6f4e9c1045ea14',
}

# The two characters being swept, written as escapes so this script's
# own bytes stay pure ASCII while still matching them.
PRIME = '\u2032'
DOUBLE_PRIME = '\u2033'
EXPECTED_PRIMES = 22
EXPECTED_DOUBLE_PRIMES = 1


# ==================================================================
# ANCHORED EDITS -- run BEFORE the character sweep
# ==================================================================

# --- A1. The one place a straight substitution reads badly ---------
# "B<prime>'s cold-start cost" would become "B''s cold-start cost".
# Reworded to avoid the possessive rather than emitting that.

OLD_A1 = (
    "    confirmed A's parallel-pipeline cost outweighs B" + PRIME + "'s cold-start cost for\n"
)
NEW_A1 = (
    "    confirmed A's parallel-pipeline cost outweighs the B' cold-start cost for\n"
)

# --- A2. Last updated: the patch ran on the 23rd -------------------

OLD_A2 = (
    "**Last updated:** August 22, 2026\n"
)
NEW_A2 = (
    "**Last updated:** August 23, 2026\n"
)

# --- A3. Header base gains the pushed SHA --------------------------

OLD_A3 = (
    "**Base:** orrery @ `38923c1`, gallery @ `493a0bd` (v19; both confirmed\n"
    "against the live remote, not carried forward. Design ratified at orrery\n"
)
NEW_A3 = (
    "**Base:** orrery @ `38923c1`, gallery @ `493a0bd` -- v19 was BUILT on\n"
    "those and PUSHED at orrery `f504c06` / gallery `02aefc0` on 2026-08-23.\n"
    "(Both bases confirmed against the live remote, not carried forward.\n"
    "Design ratified at orrery\n"
)

# --- A4. Section 1 size measurement date ---------------------------

OLD_A4 = (
    "with ~585 MB of headroom (measured at gallery `493a0bd`, 2026-08-22;\n"
)
NEW_A4 = (
    "with ~585 MB of headroom (measured at gallery `493a0bd`, 2026-08-23;\n"
)

# --- A5. The amendment was WRITTEN on the 23rd, RULED on the 22nd ---

OLD_A5 = (
    "**Amended 2026-08-22 at `38923c1` -- the braid.** Provenance stops being\n"
)
NEW_A5 = (
    "**Amended 2026-08-23 at `38923c1`, implementing the braid ruled\n"
    "2026-08-22.** Provenance stops being\n"
)

# --- A6. "Until 2026-08-22" -- the paragraph stood until v19 --------

OLD_A6 = (
    "the ORRERY. Until 2026-08-22 this paragraph drew a second conclusion\n"
    "from it -- that the refactor must PRECEDE the assembler work rather than\n"
    "run beside it -- and that conclusion is withdrawn.\n"
)
NEW_A6 = (
    "the ORRERY. Until v19 this paragraph drew a second conclusion from it --\n"
    "that the refactor must PRECEDE the assembler work rather than run beside\n"
    "it -- and the 2026-08-22 ruling withdrew that conclusion.\n"
)

# --- A7. Saturn belts: measured on the 23rd ------------------------

OLD_A7 = (
    "One precision, measured 2026-08-22: **Saturn has no radiation belts** in\n"
)
NEW_A7 = (
    "One precision, measured 2026-08-23: **Saturn has no radiation belts** in\n"
)

# --- A8. The execution-order heading names the RULING --------------

OLD_A8 = (
    "### The order of execution -- amended 2026-08-22\n"
)
NEW_A8 = (
    "### The order of execution -- the braid, ruled 2026-08-22\n"
)

# --- A9. "You are here" is a reading, taken on the 23rd -------------

OLD_A9 = (
    "### You are here -- 2026-08-22, orrery `38923c1`, gallery `493a0bd`\n"
)
NEW_A9 = (
    "### You are here -- read 2026-08-23 at orrery `38923c1`, gallery `493a0bd`\n"
)

# --- A10. Section 7 decision 12: looked on the 23rd -----------------

OLD_A10 = (
    "    **Resolved by looking, 2026-08-22 at `38923c1`: TWO is right.**\n"
)
NEW_A10 = (
    "    **Resolved by looking, 2026-08-23 at `38923c1`: TWO is right.**\n"
)

# --- A11. Section 7 decision 16: confirmed on the 23rd --------------

OLD_A11 = (
    "    **Confirmed 2026-08-22: FOUR.** `main_ring`, `halo_ring`,\n"
)
NEW_A11 = (
    "    **Confirmed 2026-08-23: FOUR.** `main_ring`, `halo_ring`,\n"
)

# --- A12. AB_FORK_ANALYSIS.md: checked on the 23rd ------------------

OLD_A12 = (
    "  `873c6cd` / `827d0b3` -- **that file is in NEITHER repo as of\n"
    "  2026-08-22**, and no near-match name exists. The lineage entry stays\n"
)
NEW_A12 = (
    "  `873c6cd` / `827d0b3` -- **that file is in NEITHER repo as of\n"
    "  2026-08-23**, and no near-match name exists. The lineage entry stays\n"
)

# --- A13. The v19 lineage entry was written on the 23rd -------------

OLD_A13 = (
    "*New in v19 (August 22, 2026):*\n"
)
NEW_A13 = (
    "*New in v19 (August 23, 2026, implementing the 2026-08-22 ruling):*\n"
)

# --- A14. The skill-list ruling was Tony's, on the 23rd -------------

OLD_A14 = (
    "- **The skill-version list is deleted, not updated** (Tony's ruling,\n"
    "  2026-08-22). The closing block restated ten skill versions by hand and\n"
    "  five had drifted, provenance-discipline worst at 1.8 against an actual\n"
)
NEW_A14 = (
    "- **The skill-version list is deleted, not updated** (Tony's ruling,\n"
    "  2026-08-23). The closing block restated ten skill versions by hand and\n"
    "  five had drifted, provenance-discipline worst at 1.8 against an actual\n"
)

# --- A15. Closing block: same ruling, same date, plus pushed SHA ----

OLD_A15 = (
    "carry ten of them by hand; five had drifted by 2026-08-22 and nothing\n"
)
NEW_A15 = (
    "carry ten of them by hand; five had drifted by 2026-08-23 and nothing\n"
)

OLD_A16 = (
    "Read it there. (Tony's ruling, 2026-08-22: fix the producer, not N\n"
)
NEW_A16 = (
    "Read it there. (Tony's ruling, 2026-08-23: fix the producer, not N\n"
)

OLD_A17 = (
    "Base: orrery @ `38923c1` / gallery @ `493a0bd` (v19, confirmed against\n"
    "the live remote; v17-v18 stood at orrery `ee0da47` / gallery `61a78c0`;\n"
)
NEW_A17 = (
    "Base: orrery @ `38923c1` / gallery @ `493a0bd` -- v19 built on those,\n"
    "pushed at orrery `f504c06` / gallery `02aefc0` on 2026-08-23. (All\n"
    "confirmed against the live remote; v17-v18 stood at orrery `ee0da47` /\n"
    "gallery `61a78c0`;\n"
)

# --- A18. The v19 entry gains the ASCII sweep and the date fix ------

OLD_A18 = (
    "- **An unmatched code fence removed.** The file carried five ``` markers,\n"
    "  an odd count; the last opened a block that never closed.\n"
)
NEW_A18 = (
    "- **An unmatched code fence removed.** The file carried five ``` markers,\n"
    "  an odd count; the last opened a block that never closed.\n"
    "- **The document is now pure ASCII.** 22 U+2032 PRIME and one U+2033\n"
    "  DOUBLE PRIME, all in the B-prime architecture name, became ASCII `'`\n"
    "  and `''`. The first v19 patch reported them and declined to sweep\n"
    "  them, reading the encoding gate as scoped to delivered code. Tony's\n"
    "  ruling, 2026-08-23: a patch already holding a file open fixes\n"
    "  incidental non-ASCII, and markdown is not an exception to Stamp What\n"
    "  You Change. Section 5a already spelled the name `B'`, so this makes\n"
    "  the document self-consistent rather than imposing a new convention.\n"
    "- **Authorship dates corrected.** The first v19 patch stamped itself\n"
    "  2026-08-22 throughout and ran on the 23rd. Ruling dates were right and\n"
    "  stand; the eight authorship and measurement dates moved. Recorded\n"
    "  rather than quietly fixed, because a document about anchors being true\n"
    "  is the wrong place to be casual about which day something happened.\n"
)


PLAN_EDITS = [
    ('A1  B-prime possessive reworded before the sweep', OLD_A1, NEW_A1),
    ('A2  Last updated -> August 23', OLD_A2, NEW_A2),
    ('A3  header base gains the pushed SHA', OLD_A3, NEW_A3),
    ('A4  S1 size measured 2026-08-23', OLD_A4, NEW_A4),
    ('A5  S5a amended 08-23, ruled 08-22', OLD_A5, NEW_A5),
    ('A6  S5a "until v19" rather than a date', OLD_A6, NEW_A6),
    ('A7  Saturn belts measured 2026-08-23', OLD_A7, NEW_A7),
    ('A8  execution-order heading names the ruling', OLD_A8, NEW_A8),
    ('A9  You-are-here is a reading, dated 08-23', OLD_A9, NEW_A9),
    ('A10 S7 d12 resolved 2026-08-23', OLD_A10, NEW_A10),
    ('A11 S7 d16 confirmed 2026-08-23', OLD_A11, NEW_A11),
    ('A12 AB_FORK checked 2026-08-23', OLD_A12, NEW_A12),
    ('A13 v19 lineage entry dated 08-23', OLD_A13, NEW_A13),
    ('A14 skill-list ruling dated 08-23', OLD_A14, NEW_A14),
    ('A15 closing -- drifted by 2026-08-23', OLD_A15, NEW_A15),
    ('A16 closing -- ruling dated 08-23', OLD_A16, NEW_A16),
    ('A17 closing base gains the pushed SHA', OLD_A17, NEW_A17),
    ('A18 v19 entry records the sweep and the date fix', OLD_A18, NEW_A18),
]


# ==================================================================
# THE SUMMARY'S BROKEN POINTER
# ==================================================================

OLD_S1 = (
    "here\" table. CRITICAL_PATH_SUMMARY.md is its readable companion and\n"
)
NEW_S1 = (
    "here\" table. MASTER_PLAN_CRITICAL_PATH_SUMMARY.md is its readable\n"
    "companion and\n"
)

OLD_S2 = (
    "Entry written August 2026 with Anthropic's Claude Opus 5. Updated\n"
    "August 19, 2026, built on 9ffb9b403a7d62090b30a9acf9adbc6180a6baec;\n"
    "gallery at ff18d3e6fa31f70a8f525df471e751d046cf14fa.\n"
)
NEW_S2 = (
    "Entry written August 2026 with Anthropic's Claude Opus 5. Updated\n"
    "August 19, 2026, built on 9ffb9b403a7d62090b30a9acf9adbc6180a6baec;\n"
    "gallery at ff18d3e6fa31f70a8f525df471e751d046cf14fa.\n"
    "\n"
    "[Pointer correction, 2026-08-23 at f504c06446edddb19dce0c906b229c96387a8406:\n"
    "the readable companion named above was written as CRITICAL_PATH_SUMMARY.md.\n"
    "No file of that name has ever existed; it is\n"
    "MASTER_PLAN_CRITICAL_PATH_SUMMARY.md, in documentation/. A broken pointer\n"
    "is not an overtaken claim, so it is corrected in place rather than\n"
    "bracketed, and the dated stamp above is deliberately left as it stood --\n"
    "this document does not restamp itself for a correction to a filename.]\n"
)

SUMMARY_EDITS = [
    ('S1  pointer -> MASTER_PLAN_CRITICAL_PATH_SUMMARY.md', OLD_S1, NEW_S1),
    ('S2  dated correction note, stamp left intact', OLD_S2, NEW_S2),
]


ALL_EDITS = {PLAN: PLAN_EDITS, SUMMARY: SUMMARY_EDITS}


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. BOTH files on disk are untouched.')
    sys.exit(1)


def main():
    print('patch_L221_3_ascii_and_dates.py')
    print('built on %s' % BASE_SHA)
    print('gallery  %s' % GALLERY_SHA)
    print('')

    paths = {}
    originals = {}
    endings = {}

    for name in (PLAN, SUMMARY):
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            fail('%s not found beside this script.\n'
                 '       This script must be saved into documentation/ --\n'
                 '       the same folder as the two files it edits.\n'
                 '       It looked in: %s' % (name, HERE))
        paths[name] = path
        with open(path, 'rb') as handle:
            originals[name] = handle.read()

    # --- Gate 1: are these the files we built against? --------------
    for name in (PLAN, SUMMARY):
        normalized = originals[name].replace(b'\r\n', b'\n')
        got = hashlib.md5(normalized).hexdigest()
        if got != FINGERPRINTS[name]:
            fail('BASE MOVED. %s fingerprints %s; this patch was built '
                 'against %s. Re-pull at HEAD, or ask for a rebuilt patch.'
                 % (name, got, FINGERPRINTS[name]))
        endings[name] = b'\r\n' if b'\r\n' in originals[name] else b'\n'
        print('[base ok]      %-42s %s (%s)'
              % (name, got, 'CRLF' if endings[name] == b'\r\n' else 'LF'))

    # --- Gate 2: no edit may INTRODUCE a non-ASCII character ---------
    for name, edits in ALL_EDITS.items():
        for label, old, new in edits:
            old_n = sum(1 for ch in old if ord(ch) > 127)
            new_n = sum(1 for ch in new if ord(ch) > 127)
            if new_n > old_n:
                fail('edit %s would INTRODUCE %d non-ASCII character(s).'
                     % (label, new_n - old_n))
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[self ok]      this script is pure ASCII (%d bytes)' % len(own))

    working = {}
    for name in (PLAN, SUMMARY):
        working[name] = originals[name].replace(b'\r\n', b'\n').decode('utf-8')

    # --- Gate 3: the sweep count must be exactly what we expect ------
    # Counted BEFORE the anchored edits, since edit A1 removes one.
    primes = working[PLAN].count(PRIME)
    doubles = working[PLAN].count(DOUBLE_PRIME)
    if primes != EXPECTED_PRIMES or doubles != EXPECTED_DOUBLE_PRIMES:
        fail('expected %d PRIME and %d DOUBLE PRIME in %s; found %d and %d. '
             'The file moved -- refusing to sweep blind.'
             % (EXPECTED_PRIMES, EXPECTED_DOUBLE_PRIMES, PLAN,
                primes, doubles))
    print('[sweep scope]  %d PRIME + %d DOUBLE PRIME found, as expected'
          % (primes, doubles))

    # --- Gate 4: every anchor matches exactly once ------------------
    for name in (PLAN, SUMMARY):
        for label, old, new in ALL_EDITS[name]:
            count = working[name].count(old)
            if count != 1:
                fail('ANCHOR FAIL on %s -- expected exactly 1 match, found '
                     '%d. First 70 chars: %r' % (label, count, old[:70]))
            working[name] = working[name].replace(old, new, 1)
            print('[ok]           %s' % label)

    # --- The character sweep, after the anchored edits ---------------
    before = working[PLAN].count(PRIME) + working[PLAN].count(DOUBLE_PRIME)
    working[PLAN] = working[PLAN].replace(DOUBLE_PRIME, "''")
    working[PLAN] = working[PLAN].replace(PRIME, "'")
    remaining = sum(1 for ch in working[PLAN] if ord(ch) > 127)
    if remaining:
        fail('%d non-ASCII character(s) survived the sweep in %s.'
             % (remaining, PLAN))
    print('[swept]        %d character(s) normalized to ASCII; %s is now '
          'pure ASCII' % (before, PLAN))

    for name in (PLAN, SUMMARY):
        left = sum(1 for ch in working[name] if ord(ch) > 127)
        if left:
            fail('%s still holds %d non-ASCII character(s).' % (name, left))
    print('[ascii ok]     both targets are pure ASCII after the patch')

    # --- Gate 5: no line vanishes that no edit claims to rewrite -----
    # The sweep legitimately rewrites every line holding a prime, so
    # those lines are added to the permitted-loss set by the same
    # derivation: a line may vanish if its swept form is present.
    for name in (PLAN, SUMMARY):
        allowed = set()
        for _label, old, new in ALL_EDITS[name]:
            allowed.update(l for l in
                           (set(old.split('\n')) - set(new.split('\n'))) if l)
        after_lines = set(working[name].split('\n'))
        lost = []
        for line in working[name].split('\n'):
            pass
        for line in originals[name].replace(b'\r\n', b'\n').decode(
                'utf-8').split('\n'):
            if not line or line in after_lines:
                continue
            swept = line.replace(DOUBLE_PRIME, "''").replace(PRIME, "'")
            if swept in after_lines or line in allowed:
                continue
            lost.append(line)
        if lost:
            fail('%d line(s) of %s would be lost that neither an edit nor '
                 'the sweep accounts for. First: %r'
                 % (len(lost), name, lost[0]))
        print('[addition ok]  %-42s every rewritten line accounted for'
              % name)

    # --- Write, all or nothing --------------------------------------
    for name in (PLAN, SUMMARY):
        out = working[name].encode('ascii')
        if endings[name] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        with open(paths[name], 'wb') as handle:
            handle.write(out)
        print('[written]      %-42s %d -> %d bytes'
              % (name, len(originals[name]), len(out)))

    print('')
    print('patch applied -- %d edits + the character sweep'
          % (len(PLAN_EDITS) + len(SUMMARY_EDITS)))
    print('')
    print('CURRENCY STAMPS:')
    print('  %s  Last updated -> August 23, 2026; both base lines now carry'
          % PLAN)
    print('    built-on %s AND pushed-at %s.' % (BUILT_ON, PUSHED_AT))
    print('  %s  stamp DELIBERATELY NOT changed -- it is a' % SUMMARY)
    print('    dated snapshot, and a filename correction is not an')
    print('    overtaken claim. Recorded in a dated note at the foot.')
    print('')
    print('note: %s now holds 0 non-ASCII bytes. The 23 reported by' % PLAN)
    print('      patch_L221_2 are swept, per Tony\'s ruling of 2026-08-23.')
    print('')
    print('NEXT:')
    print('  1. Commit and push both files.')
    print('  2. Move this script to documentation/ if it is not there.')
    print('')
    print('STILL OPEN -- ledger edits, not this patch\'s to make:')
    print('  - L-225 has no ledger entry; the highest handle is L-224.')
    print('  - L-154 reads BLOCKED; the plan now makes it the first work.')


if __name__ == '__main__':
    main()
