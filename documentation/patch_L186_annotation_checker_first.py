"""L-186 -- migrate every Cross-checked annotation to checker-first form.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo ROOT (the folder holding
constants_new.py), open it in VS Code, and click Run.

    python patch_L186_annotation_checker_first.py

WHAT IT DOES
------------
Rewrites all 134 `# Cross-checked:` annotation lines across 8 modules
from

    # Cross-checked: Hauck et al. 2013 via GPT 2026-08-03 (worksheet.md)

to

    # Cross-checked: GPT 2026-08-03 -- Hauck et al. 2013 (worksheet.md)

WHY
---
The old order puts a free-text SOURCE in front of the check date. When
that source carries its own publication year, provenance_scanner.py's
parser takes the year as the check date and everything before it as the
checker identity -- so the model name lands after the parsed date and
never enters the identity at all.

Two annotations by two DIFFERENT models then read as one checker written
twice: `duplicate_identity`, and the claim is scored V3 with the reason
"cross-check incomplete (1/2 models)" when both legs were in fact done.
19 units are in that state right now, against 20 scored correctly.

Checker-first makes the parser's existing rule -- everything before the
date is the checker -- TRUE instead of accidental. No new heuristic is
added anywhere.

The 134 lines are uniform: exactly one ` via `, one full ISO date, and
one `(....md)` parenthetical each. That is what makes this mechanical.
The regex matches only that exact shape, so a line in any other shape is
left alone and shows up in the count check below rather than being
guessed at.

SAFETY
------
- Transactional: every file is transformed in memory and checked first.
  If ANY file's converted count differs from the expected number, or any
  old-form line survives, NOTHING is written to ANY file.
- Base fingerprints are MD5 over LF-normalized content, so a CRLF working
  copy does not read as a moved base.
- Binary-mode I/O throughout; line endings preserved per file.
- Safe to re-run: on an already-patched tree it reports the base has
  moved and writes nothing.

WHAT SUCCESS LOOKS LIKE
-----------------------
One `ok` line per file with its count, then `patch applied` and a byte
count per file. Any `ERROR:` or `COUNT FAIL` line means nothing was
written.

AFTER RUNNING
-------------
Run provenance_scanner.py. Expect the six `duplicate_identity` rows to
be gone and the V2 (cross-checked) unit count to roughly double. Tier-1
should not move.
"""

import hashlib
import os
import re
import sys

# (filename, expected annotation count, md5 of LF-normalized base)
TARGETS = [
    ('constants_new.py',                55, '4bd233e35d8ea4b550b5a592fa8775be'),
    ('eris_visualization_shells.py',     8, 'db67048b8b2df15155ea8645b7b86437'),
    ('mars_visualization_shells.py',     8, 'ff4cb39abad8df62acb326d331e72422'),
    ('mercury_visualization_shells.py', 12, 'e253243024cbc1b726fade49a5041950'),
    ('moon_visualization_shells.py',     9, 'be419d3921944cdd51dd1cbb9b41c47f'),
    ('pluto_visualization_shells.py',   24, 'd855b92c7dcb0ecefceef55af654c35d'),
    ('shell_configs.py',                 4, 'e769fa2cd612a26e001d4c5b8f9a0385'),
    ('venus_visualization_shells.py',   14, '836dd66ddb154eb58f83d33a3d3f36d9'),
]

EXPECTED_TOTAL = 134

# Matches ONLY the old shape: <source> via <model> <ISO date> (<ref>.md)
OLD_FORM = re.compile(
    rb'(?m)^([ \t]*)#[ \t]*Cross-checked:[ \t]*(?P<src>.+?)[ \t]+via[ \t]+'
    rb'(?P<model>[A-Za-z0-9 _.-]+?)[ \t]+'
    rb'(?P<date>(?:19|20)\d{2}-\d{2}-\d{2})'
    rb'[ \t]+(?P<ref>\([^()]*\.md\))[ \t]*$')

# Any annotation line at all, for the residual check.
ANY_ANNOTATION = re.compile(rb'(?mi)^[ \t]*#[ \t]*cross-checked[ \t]*:')

# The new shape, for the read-back check.
NEW_FORM = re.compile(
    rb'(?m)^[ \t]*#[ \t]*Cross-checked:[ \t]*[A-Za-z0-9 _.-]+?[ \t]+'
    rb'(?:19|20)\d{2}-\d{2}-\d{2}[ \t]+--[ \t]+.+?[ \t]+\([^()]*\.md\)[ \t]*$')


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def reorder(match):
    indent = match.group(1)
    src = match.group('src').strip()
    model = match.group('model').strip()
    date = match.group('date')
    ref = match.group('ref')
    return (indent + b'# Cross-checked: ' + model + b' ' + date
            + b' -- ' + src + b' ' + ref)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    blobs = {}
    converted_total = 0

    # ---- pass 1: read, verify base, transform in memory --------------
    for name, expected, base_md5 in TARGETS:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print("ERROR: %s not found. Run this from the repo root."
                  % name)
            sys.exit(1)
        with open(path, 'rb') as handle:
            data = handle.read()

        got = fingerprint(data)
        if got != base_md5:
            print("ERROR: base moved for %s" % name)
            print("       expected %s" % base_md5)
            print("       got      %s" % got)
            print("Nothing written to any file.")
            sys.exit(1)

        new_data, count = OLD_FORM.subn(reorder, data)
        if count != expected:
            print("COUNT FAIL (%s): expected %d annotations, converted %d."
                  % (name, expected, count))
            print("Nothing written to any file.")
            sys.exit(1)

        residual = len(ANY_ANNOTATION.findall(new_data))
        readback = len(NEW_FORM.findall(new_data))
        if residual != readback:
            print("READ-BACK FAIL (%s): %d annotation lines present but "
                  "only %d parse as checker-first."
                  % (name, residual, readback))
            print("Nothing written to any file.")
            sys.exit(1)

        blobs[path] = new_data
        converted_total += count
        print("  ok  %-34s %2d annotations" % (name, count))

    if converted_total != EXPECTED_TOTAL:
        print("COUNT FAIL: expected %d annotations in total, converted %d."
              % (EXPECTED_TOTAL, converted_total))
        print("Nothing written to any file.")
        sys.exit(1)

    # ---- pass 2: write ----------------------------------------------
    for path, data in blobs.items():
        with open(path, 'wb') as handle:
            handle.write(data)

    print()
    print("patch applied -- %d annotations reordered" % converted_total)
    for path, data in sorted(blobs.items()):
        print("  %-38s %d bytes" % (os.path.basename(path), len(data)))
    print()
    print("NEXT: run provenance_scanner.py.")
    print("  expect: the six duplicate_identity rows gone,")
    print("          the cross-checked (V2) unit count roughly doubled,")
    print("          Tier-1 unchanged at 206.")


if __name__ == '__main__':
    main()
