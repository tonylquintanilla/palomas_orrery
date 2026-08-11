"""
patch_masterplan_ascii.py

Normalizes documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md to ASCII, in
the two parts that need different treatment. Run this AFTER
patch_masterplan_v18.py.

WHAT CHANGES -- 312 characters in three groups

  MECHANICAL (245 characters). One-for-one punctuation replacements:
    em dash U+2014   ->  --        130
    section sign     ->  Section    77   (every one is followed by a
                                          digit, verified, so "Section 3"
                                          reads correctly everywhere)
    right arrow      ->  ->         35
    less-or-equal    ->  <=          2
    en dash          ->  -           1
    check mark       ->  [x]         9   (outside the diagram)
    open circle      ->  [ ]         4   (outside the diagram)
  Plus the CO2 subscript, which is an eighth case with one occurrence.
  The check and circle use the same bracket convention as the redrawn
  diagram, so status glyphs read identically everywhere in the file.

  THE DIAGRAM (65 characters), redrawn rather than substituted. The phase
  dependency chain around line 790 uses box-drawing and status glyphs, and
  its columns are hand-aligned. A one-for-one swap would break the
  alignment because [x] is three characters where a checkmark is one, so
  the connector runs are re-counted to land the labels back on their
  original columns:
    check mark  ->  [x]      circle    ->  [ ]
    horizontal  ->  -        vertical  ->  |
    left arrow  ->  <--
  On the PHASE 0 / 1a / 1b line the glyphs are dropped entirely in favour
  of the words already there, which keeps that row's three columns where
  they were instead of pushing them four characters right.

WHAT IS DELIBERATELY LEFT ALONE -- 27 characters

  The prime and double-prime in B', A', A''. These are NAMES, not
  punctuation: "A/B fork resolved: B-prime" is an architecture identifier
  that appears in SEVEN files across the repo, including
  LEDGER_CONSOLIDATED.md and four design handoffs. Normalizing it here
  alone would leave the master plan spelling it one way and the ledger
  another, and a search for either would miss the other. A repo-wide
  rename is a reasonable job; it is not this job.

  After this patch the file holds exactly 27 non-ASCII characters, all of
  them primes. That number is the check, and it earned its keep: a first
  version of this patch expected 28 and accounted only for the glyphs
  inside the diagram, missing nine check marks and four circles elsewhere
  in the file. The count refused to match and nothing was written.

WHY THIS IS WORTH DOING AT ALL

  Not the console-mangling rule -- a markdown file is never printed to a
  cp1252 console, so that failure does not apply here. The real reason is
  that these documents get carried to other models and pasted between
  tools, which is where encoding actually gets mangled, and an outbound
  document that arrives with replacement characters in it is harder to
  trust than one that does not.

Target file: documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
Built on the OUTPUT of patch_masterplan_v18.py, from
c1ba36e4d8120cdca00f6fb67eb1340de8762782

HOW TO RUN
  Run patch_masterplan_v18.py FIRST. Then save this file in the same
  place (the orrery repo root), open it in VS Code, and click Run.

  Or from a terminal in that folder:  python patch_masterplan_ascii.py

WHAT SUCCESS LOOKS LIKE
  A per-character replacement count, then "ok" for the diagram, then
  "patch applied" and a line confirming 28 non-ASCII characters remain.

WHAT FAILURE LOOKS LIKE
  A single line beginning "ERROR:" or "ANCHOR FAIL:". Nothing is written.
  If you have NOT run patch_masterplan_v18.py yet, this stops with a
  message saying so rather than applying out of order.
"""

import hashlib
import os
import sys

TARGET = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')

# Fingerprint of the file AFTER patch_masterplan_v18.py has run.
BASE_MD5 = '4be4f2b8532b0b95c3f72c271ec24ec8'

# Fingerprint BEFORE v18, so the script can tell "wrong order" apart from
# "unknown file" and say which it is.
PRE_V18_MD5 = 'f1e090f5849c3856868b178bc2a863b2'

MECHANICAL = [
    ('\u2014', '--', 'em dash'),
    ('\u00a7', 'Section ', 'section sign'),
    ('\u2192', '->', 'right arrow'),
    ('\u2264', '<=', 'less-or-equal'),
    ('\u2013', '-', 'en dash'),
    ('\u2082', '2', 'subscript two'),
    ('\u2713', '[x]', 'check mark'),
    ('\u25cb', '[ ]', 'open circle'),
]

# ------------------------------------------------------------------
# The diagram, before and after. Primes are preserved inside it.
# ------------------------------------------------------------------

DIAGRAM_OLD = """PREP (independent, can start now)
  \u2713 LICENSE moved to root
  \u2713 Section W ledger entries
  \u25cb Attribution page \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 4.8 \u2500\u2500\u2192 needed before public pages
  \u25cb Helpers split \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 4.6 \u2500\u2500\u2192 needed before Phase 2

PHASE 0 \u2713 DONE \u2500\u2500\u2500\u2500 PHASE 1a \u2713 COMPLETE \u2500\u2500\u2500\u2500 PHASE 1b
Stack proven         Vocabulary delivered       Data serving pipeline
Arch A proven        (Fable, Jul 4)             Export script + coverage
B\u2032 measured: PASS                               index + serving home
(Jul 6)                                         + slim plotly wheel
                          \u2502
                     PHASE 2 \u25c4\u2500\u2500 Phase 1b + helpers split
                     Solar system assembler (B\u2032)
                     Shared engines in Pyodide
                     + interactive page
                          \u2502
                     PHASE 3
                     Star assembler + star cache format
                          \u2502
                     PHASE 4
                     Hybrid domains
                          \u2502
                     PHASE 5 \u25c4\u2500\u2500 4.8 restraint discipline
                     Earth system"""

DIAGRAM_NEW = """PREP (independent, can start now)
  [x] LICENSE moved to root
  [x] Section W ledger entries
  [ ] Attribution page --------- 4.8 --> needed before public pages
  [ ] Helpers split ------------ 4.6 --> needed before Phase 2

PHASE 0 DONE ------ PHASE 1a COMPLETE ------ PHASE 1b
Stack proven         Vocabulary delivered       Data serving pipeline
Arch A proven        (Fable, Jul 4)             Export script + coverage
B\u2032 measured: PASS                               index + serving home
(Jul 6)                                         + slim plotly wheel
                          |
                     PHASE 2 <-- Phase 1b + helpers split
                     Solar system assembler (B\u2032)
                     Shared engines in Pyodide
                     + interactive page
                          |
                     PHASE 3
                     Star assembler + star cache format
                          |
                     PHASE 4
                     Hybrid domains
                          |
                     PHASE 5 <-- 4.8 restraint discipline
                     Earth system"""

EXPECTED_REMAINING = 27   # 26 primes + 1 double prime, nothing else


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print("ERROR: " + TARGET + " not found.")
        print("       Put this script in the orrery repo root and retry.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp == PRE_V18_MD5:
        print("ERROR: wrong order. This file is still the pre-v18 master")
        print("       plan. Run patch_masterplan_v18.py first, then run")
        print("       this one. Nothing was written.")
        return 1
    if fp != BASE_MD5:
        print("ERROR: base moved. Expected the file as v18 leaves it")
        print("       (" + BASE_MD5 + "),")
        print("       found " + fp + ". Nothing was written.")
        return 1

    text = data.decode('utf-8')
    crlf = '\r\n' in text
    if crlf:
        text = text.replace('\r\n', '\n')

    # --- diagram first, so its own arrows are not pre-converted ---
    n = text.count(DIAGRAM_OLD)
    if n != 1:
        print("ANCHOR FAIL: dependency diagram matched " + str(n) + " times.")
        print("             Nothing was written.")
        return 1
    text = text.replace(DIAGRAM_OLD, DIAGRAM_NEW)
    print("ok   dependency diagram redrawn (columns re-aligned)")

    # --- mechanical replacements ---
    for ch, repl, name in MECHANICAL:
        count = text.count(ch)
        if count:
            text = text.replace(ch, repl)
        print("ok   " + name + ": " + str(count) + " replaced")

    # Section sign leaves a double space if one already followed it.
    text = text.replace('Section  ', 'Section ')

    remaining = sum(1 for c in text if ord(c) > 127)
    if remaining != EXPECTED_REMAINING:
        print("ANCHOR FAIL: expected " + str(EXPECTED_REMAINING)
              + " non-ASCII characters left (the primes), found "
              + str(remaining) + ".")
        print("             Nothing was written.")
        return 1

    if crlf:
        text = text.replace('\n', '\r\n')

    with open(path, 'wb') as f:
        f.write(text.encode('utf-8'))

    print("")
    print("patch applied -- " + TARGET)
    print(str(remaining) + " non-ASCII characters remain, all of them the")
    print("prime in B', A', A''. Left deliberately: it is a name used in")
    print("seven files, and renaming it here alone would split the term.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
