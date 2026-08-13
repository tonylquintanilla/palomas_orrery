"""Patch: record the L-192 attachment build in the ledger.

Run command:

    python patch_ledger_L192_attachment.py

Save this file into the SAME folder as LEDGER_CONSOLIDATED.md (the repo
root), open it in VS Code, and click Run. Transactional: the edit must
find exactly one anchor or nothing is written.

Afterwards run ledger_index.py so the index table is regenerated. The
L-192 status stays OPEN and its date stays 2026-08-12, so the index row
should come back unchanged -- if it moves, something else did it.

Success prints one `ok` line, then `patch applied (N bytes)`.
Failure prints a single ERROR or ANCHOR FAIL line and writes nothing.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'


ANCHOR = b"""- **Ref:** L-186 (the annotation grammar and the pin retirement it
  replaces); L-188 (the runner it deliberately stays out of); L-156
  Phase 2 (the cross-check batches that produced the worksheets).
"""

ADDITION = b"""
##### As built, 2026-08-12: the attachment rule (scanner half)

Built and pushed at `878e2c9`, audit regenerated at `c5218f6`. The
worksheet checker this item was opened for is NOT built; this is the
prerequisite that surfaced while measuring it.

- **What was wrong.** `score_unit()` counted any cross-check annotation
  inside the citation window (30 lines back, 15 forward for a constant).
  That window is right for a CITATION -- a section header naming a
  source legitimately covers the declarations beneath it -- and wrong
  for an ANNOTATION, which names one checker who verified one value on
  one date. Proximity is not attachment.
- **The case that settles it.** `INNER_LIMIT_OORT_CLOUD_AU` scored the
  cross-checked rung on annotations belonging to the heliopause
  constant above it. The two worksheets those annotations name read
  UNVERIFIED (Claude) and PARTIAL (GPT) for the Oort value. The window
  was converting a recorded non-verification into a top-rung badge --
  wrong-but-cited, produced mechanically.
  `MERCURY_RADIUS_KM` and `VENUS_RADIUS_KM` are the milder form: top
  rung on `MOON_RADIUS_KM`'s annotations, three and six lines below.
- **Ruling (Fable 5, 2026-08-12, Mode 7 relay; Tony ratified).** The
  SCANNER narrows, rather than the checker reporting and leaving
  scoring alone. Two definitions of "which annotations belong to this
  value" would drift apart by construction. The worksheet checker
  consumes the scanner's attachment.
- **The rule.** A module-level unit takes the unbroken comment run
  directly above its own statement plus the one directly below --
  `constants_new.py` writes citations below the declaration, the shells
  modules write them above, and both are correct. A string nested in a
  dict or a function body takes only the run above the ENTRY LINE that
  introduces it, never the literal's own line. A blank line or a line
  of code ends a run. Scope is annotation CREDIT only; citation
  inheritance and the malformation diagnostics keep the wide window.
- **Measured: 50 of 77 units at the cross-checked rung keep it; 27
  drop.** Zero ambiguous runs exist today, so adopting strictness cost
  nothing.
- **An orphan report is part of the rule, not an extra.** An annotation
  whose comment run touches no code is printed with file and line.
  Silence about the unattached is the same failure as silence about the
  unexamined. Four exist: `constants_new.py` 145-146 (SOLAR STRUCTURE)
  and 316-317 (CENTER BODY RADII), both section headers written to
  cover a group.
- **Group annotations are NOT given block grammar** (Fable's
  recommendation, Tony's call). A parser cannot distinguish group
  intent from proximity -- in bytes they are identical. The reason to
  prefer per-value: a block-scope annotation reading "everything below
  checked" would have papered over the two UNVERIFIED Oort rows inside
  its scope. Per-value forces the author to read each row.
- **Backfill is VERDICT-GATED.** Appearing in a worksheet is not a
  passing check. Venus reads YES/YES, Mercury PARTIAL/YES, the Oort
  values UNVERIFIED/PARTIAL. Only a verdict that is a completed check
  earns an annotation; the rest stay at V3 with their state visible.
  Whether PARTIAL counts is open (Tony, decide).
- **Test consequence.** `test_lookback_window_bleed_is_measured` had
  pinned the bleed deliberately, with a note saying that if it ever
  failed the window had changed. It failed. Renamed
  `test_lookback_window_bleed_is_closed`, asserting the opposite, both
  halves still pinned.
- **Corpus measurement, carried for the checker build:** 134 live
  annotations, all 134 parse under the L-186 grammar, 18 distinct
  worksheets named, zero dangling. Of 34 files in
  `documentation/worksheets/`: 18 cited, 9 uncited worksheets, 7 prompt
  files. The existence half is clean; the value half is the build.
- **Method note worth keeping.** Fable's written rule and its own
  measurement script disagreed -- the prose said the entry line, the
  script used the literal's line -- and the independent verification
  leg reproduced the error, because it implemented the same prose and
  read it the same wrong way. The agreement between two implementations
  was reported as confirmation and was not. Caught only by re-reading
  the written rule against the code being produced. Cross-AI
  independence protects against a shared model, not a shared spec.
"""


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print(f"ERROR: {TARGET} not found next to this script ({here})")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    print(f"base fingerprint: {fp}  ({len(data)} bytes)")

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print("note: file uses CRLF; anchors translated")

    old = ANCHOR
    new = ANCHOR + ADDITION
    if is_crlf:
        old = old.replace(b'\n', b'\r\n')
        new = new.replace(b'\n', b'\r\n')

    count = data.count(old)
    if count != 1:
        print(f"ANCHOR FAIL: expected 1 match, got {count}")
        print("nothing written")
        return 1

    staged = data.replace(old, new, 1)
    with open(path, 'wb') as f:
        f.write(staged)

    print("ok  edit 1")
    print(f"patch applied ({len(staged)} bytes)")
    print("")
    print("Next: run ledger_index.py. The L-192 index row should come")
    print("back unchanged -- status OPEN, date 2026-08-12.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
