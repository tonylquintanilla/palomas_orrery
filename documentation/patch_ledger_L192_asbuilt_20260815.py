"""
patch_ledger_L192_asbuilt_20260815.py

Records the 2026-08-15 build in L-192: worksheet_request_builder.py
(new) and rule 0 in worksheet_checker.py. Two hunks, both inside the
L-192 entry. Nothing else is touched.

The index zone is NOT edited by hand -- run ledger_index.py afterwards
(or maintenance_run.py, which includes it) to regenerate the tables.

Run this AFTER patch_L192_key_rule.py and after saving
worksheet_request_builder.py, so the ledger and the code land together.
The ledger is what the next session reads first; an as-built describing
code that is not in the repo is the stale-erratum class pointed the
other way.

Base fingerprint taken at repo HEAD 87176e9, 2026-08-15.

Run:
    Save into the palomas_orrery repo root, open in VS Code, click Run.
    Then run ledger_index.py the same way.

Success: one "ok" line per hunk, then "patch applied".
Failure: a single ERROR or ANCHOR FAIL line; nothing is written.

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import json
import os
import sys

BASE = {'LEDGER_CONSOLIDATED.md': '7f8935110ebba02f8330b0abf9cde4a0'}

# [line, old, new] per hunk, bottom-up. Literal file text with \\n
# escapes, so the whole patch is readable here.
EDITS = json.loads(r"""
{
 "LEDGER_CONSOLIDATED.md": [
  [
   1587,
   "##### As built, 2026-08-12: the attachment rule (scanner half)",
   "##### As built, 2026-08-15: the request builder and the key rule\n\nBuilt on `87176e9` at https://github.com/tonylquintanilla/palomas_orrery.\nOne build, two consumers, because `worksheet_keys.py` had none: the\nchecker did not import it and `resolve()` was never called on the\nchecking path. Shipping the builder alone would have put keys into\noutgoing worksheets that the returning checker could not read --\nworksheets that look right and check the old way.\n\n- **`worksheet_request_builder.py` (new, ~310 lines).** Reads the\n  annotated corpus through the checker's own `collect_claims()`, mints\n  a key per site through `worksheet_keys`, and emits one pre-printed\n  row per (key, ordinal) with the code value filled in. Measured on the\n  corpus: **65 rows over 65 distinct keys, zero collisions** -- the\n  53 -> 65 figure reproduced from the corpus rather than carried from\n  the ruling. It judges nothing: no verdict token, no route. The\n  checker judges; the builder asks.\n- **Rule 0 in `match_row()`.** An exact key match wins outright. A key\n  the WORKSHEET carries that no longer resolves announces KEY_STALE and\n  does NOT fall through to the fuzzy rules, because falling through\n  hides a rename behind a lucky prose hit. `ROLE_KEY` registered with\n  the `key` and `row key` headers.\n- **The circularity caught in test.** The first implementation resolved\n  the CLAIM's key to decide staleness. That key is minted from today's\n  source moments earlier, so it always resolves -- a check that cannot\n  fail. Corrected to resolve the keys the worksheet carries, which is\n  what a rename looks like from this side.\n- **Two design calls, both stated because neither was ruled.** The\n  citation legs print ABOVE the response table rather than as columns:\n  nine columns is already at the limit of what these worksheets are\n  filled in with, and a leg sitting in a cell invites a verdict token\n  typed beside it, which is the compound answer the checker may not\n  interpret. And the response table keeps the addendum's header text\n  verbatim, so the checker's existing role registry reads it with zero\n  unrecognised columns.\n- **Round trip proven at the format layer,** not assumed: the emitted\n  file was parsed back through `parse_tables()` -- one row table, 65\n  rows, zero unregistered headers, all eight roles resolved, and rule 0\n  binding a row by key.\n- **Tests 61 -> 69.** All six new checks are synthetic ON PURPOSE: no\n  worksheet in the corpus carries a Key column, so the live run cannot\n  reach rule 0 and a green run proves nothing about it. One check is\n  load-bearing -- a stale-key row whose PROSE would match -- and it was\n  mutation-tested by breaking the rule deliberately to confirm it goes\n  red.\n- **A scanner finding from the pre-test, worth recording.** The new\n  module first classified as role `undetermined`, which scored its\n  display-width constant as an uncited physical claim and moved Tier-1\n  206 -> 207. A `Role: devtool` line in the docstring returned it to\n  206. A new dev tool without a role line is scored as though it made\n  claims about the world.\n- **What this does NOT do.** No dispatch. The first dispatch that\n  relies on the Break 5 rule should follow L-195, since a block whose\n  authority is not in its `# Source:` line would be verdicted CITATION\n  RIGHT while the real authority went unchecked.\n\n##### As built, 2026-08-12: the attachment rule (scanner half)"
  ],
  [
   1560,
   "  claims expressible at all, it deletes `match_row()` and the 25\n  UNMATCHED findings that fuzzy binding produced, and a later ordinal\n  shift stops matching its pre-printed value loudly instead of binding\n  to the wrong claim silently.\n",
   "  claims expressible at all, it deletes `match_row()` and the 25\n  UNMATCHED findings that fuzzy binding produced, and a later ordinal\n  shift stops matching its pre-printed value loudly instead of binding\n  to the wrong claim silently.\n- **Builder and key rule built 2026-08-15**, see the as-built below.\n  `match_row()` is NOT deleted: rule 0 sits ahead of the four fuzzy\n  rules rather than replacing them, because 104 annotations still bind\n  through them. That is the transition the sequencing decide below is\n  about, and this build is the first half of it.\n"
  ]
 ]
}
""")


def fingerprint(data):
    return hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()


def main():
    for path in sorted(EDITS):
        if not os.path.exists(path):
            print("ERROR: not found: %s" % path)
            print("       run this from the palomas_orrery repo root.")
            return 1
        with open(path, "rb") as handle:
            data = handle.read()
        got = fingerprint(data)
        if got != BASE[path]:
            print("ERROR: base moved: %s" % path)
            print("       expected %s" % BASE[path])
            print("       found    %s" % got)
            print("       nothing written. Re-pull or re-anchor.")
            return 1
        if b"As built, 2026-08-15: the request builder" in data:
            print("ERROR: this as-built is already present. Nothing written.")
            return 1
        crlf = data.count(b"\r\n") > 0
        for line, old, new in EDITS[path]:
            old_b = old.encode("ascii")
            new_b = new.encode("ascii")
            if crlf:
                old_b = old_b.replace(b"\n", b"\r\n")
                new_b = new_b.replace(b"\n", b"\r\n")
            count = data.count(old_b)
            if count != 1:
                print("ANCHOR FAIL (%d matches): %s near line %d"
                      % (count, path, line))
                print("       nothing written.")
                return 1
            data = data.replace(old_b, new_b)
            print("  ok  %s near line %d" % (path, line))
        with open(path, "wb") as handle:
            handle.write(data)
        print("patch applied: %s (%d bytes)" % (path, len(data)))

    print("")
    print("NEXT: run ledger_index.py to regenerate the index tables.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
