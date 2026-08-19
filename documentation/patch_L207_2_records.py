"""patch_L207_2_records.py -- L-207. Close the item, archive the script.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root, open it in VS Code,
and click Run. It takes no arguments.

    python patch_L207_2_records.py

Then run, and it is NOT optional:

    python ledger_index.py

The index rebuild is what moves the L-207 block out of the open
section and into the closed one, and what rewrites the index table row
from OPEN to DONE. Skipping it leaves the table advertising an open
item that is finished.

Success: one `ok` line per change, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and nothing is
written or moved.

WHAT IT DOES
------------
1. Marks L-207 DONE and writes its as-built record: what shipped, what
   the first run measured, and the one thing that could not be
   verified from inside the session that made it.
2. Moves patch_L207_1_citation_prompt.py from the repo root into
   documentation/, where every run patch is archived once it has run.
   The script is one-shot by construction -- it guards on a
   fingerprint of a tree that stopped existing the moment it succeeded
   -- so keeping it is for the record, not for reuse.
3. Normalizes the ledger's 123 pre-existing non-ASCII characters to
   ASCII in passing, and prints both what it fixed and what it left.
   Fix In Passing, Report It: the convention is already ruled, the
   file is already fingerprinted and being edited here, and every
   substitution is mechanical. A dedicated sweep for 123 characters
   is never going to be scheduled on its own.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable; the ledger record it writes is not, and
neither is the ASCII normalization.

Written August 2026 with Anthropic's Claude Opus 5. Built on
c5c0102ee5f02cc31c5012d00464404e26021e23 at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import shutil
import sys


BASE = {
    'LEDGER_CONSOLIDATED.md': '5a97f86d2d39622124b2d29be118a527',
}

SCRIPT = 'patch_L207_1_citation_prompt.py'
ARCHIVE = os.path.join('documentation', SCRIPT)


# The transliterations this project's ASCII prose already uses. Written
# as escapes on purpose: a script that repairs a Unicode character has
# to carry that character to match on it, and a deliverable that fails
# the gate it enforces is not a deliverable. Measured against the
# ledger at c5c0102: these ten cover all 123 occurrences, and the run
# prints the residual either way.
ASCII_SWEEP = {
    '\u2014': '--',        # em dash
    '\u2013': '-',         # en dash
    '\u2192': '->',        # right arrow
    '\u00a7': 'section ',  # section sign
    '\u2032': "'",         # prime
    '\u00b1': '+/-',       # plus-minus
    '\u00d7': 'x',         # multiplication sign
    '\u2248': '~',         # almost equal
    '\u2713': '[x]',       # check mark
    '\u2264': '<=',        # less than or equal
}


STATUS_OLD = ("<!-- L:207 status:OPEN upd:2026-08-18 section:A flag: "
              "rice:3/3/85/1 -->\n")
STATUS_NEW = ("<!-- L:207 status:DONE upd:2026-08-18 section:C flag: "
              "rice:3/3/85/1 -->\n")

# The index table row. ledger_index.py rebuilds this table, so this
# edit only keeps the file self-consistent between now and that run.
ROW_OLD = ("| ! | L-207 | The citation prompt -- the checker asks the "
           "fuzzy question | OPEN | 7.6 | 2026-08-18 |\n")
ROW_NEW = ("|  | L-207 | The citation prompt -- the checker asks the "
           "fuzzy question | DONE | 7.6 | 2026-08-18 |\n")

TAIL_OLD = ("**Note:** RICE is Claude's proposal, unratified.\n"
            "**Gap:** unbuilt. Full detail in\n"
            "`documentation/DESIGN_20260818_citation_prompt.md`.\n"
            "**Ref:** L-192 (the checker); L-200 (the leg that records "
            "what a\nverdict caused); L-202 (the JSON schema it "
            "reads).\n")

AS_BUILT = """- **As built, 2026-08-18** (`patch_L207_1_citation_prompt`). The
  checker writes `documentation/prompts/citation_review.jsonl` on
  every run: a header carrying the anchor SHA, the key format, the
  question, the answer fields, the verdict vocabulary read from
  `VERDICT_TOKENS` rather than retyped, and the counts of what was
  left out; then one row per key. Hooked into `run()` after the
  routing file, counted in `counts`, and printed in the detail block
  whether or not it found anything.
- **One row per KEY, not per annotation** -- a decision the design
  note did not settle and the hash did. Two checkers over one site
  would otherwise produce two rows sharing a key and a hash, which is
  a hash identifying nothing. Grouped, the two sources sit side by
  side and a disagreement between responders is visible without a
  mechanism for it. Measured on the first run: 53 rows carrying 81
  responder legs, 27 of them with two responders.
- **The leg parser moved** (Tony's ruling, 2026-08-18: move it and
  get one parser). `legs_of` and its regexes went from
  `worksheet_request_builder.py` to `worksheet_keys.py`, the module
  both tools already import. The move was forced by direction: the
  checker cannot import the builder because the builder imports the
  checker. The builder keeps the old names as ALIASES, and
  `test_worksheet_request_builder.py` pins `b.legs_of is wk.legs_of`
  so a later local copy goes red rather than quietly answering the
  same question twice. Proved behaviour-neutral by building the same
  23-row pilot request before and after the move: byte-identical,
  including all 153 continuation joins.
- **What the first run measured.** 53 rows, 81 legs, 41 annotations
  that matched no row and are counted rather than dropped, 0 matched
  rows carrying no citation material. Routing unchanged at 68 of 110
  routed and 8 clean; Tier-1 unchanged at 289. The maintenance runner
  read 11 of 11 gating checkers green.
- **Determinism is the point and it is tested.** Rows sorted by key,
  responses sorted inside a row, keys sorted inside every object, no
  timestamp anywhere. Two consecutive runs produce byte-identical
  files, so `git` reporting no change IS the statement that a citation
  review is reproducible. The anchor moves only when HEAD does, which
  is why the committed artifact reads `731066f4` -- the tree it was
  built from, one commit behind the commit that landed it.
- **Three mutations prove the new checks can fail.** Dropping the
  per-key grouping, making the writer a no-op that reports success,
  and re-forking the parser into a local copy that behaves
  identically. The last is visible only to the identity pin, which is
  why the identity pin exists.
- **The skill moved with it.** `provenance-discipline` 2.4 -> 2.5 adds
  Extend a Boundary Before Adding a Path, the rule the 2026-08-18
  external review proposed and Tony adopted; L-207 was checked against
  it rather than assumed to pass. Marked QUALITY, not CRITICAL: it was
  adopted from a prediction and the tiers move on evidence. The edit
  was verified as a PURE ADDITION by stripping the new section back
  out and comparing to 2.4 byte for byte -- the check that was missing
  the day a skill rebuild deleted its own version block.
- **Carried, because it cannot be cleared here.** The 2.5 reinstall
  landed in the account during the session that made it, and a running
  conversation serves the copy it loaded. The NEXT session confirms
  its loaded `provenance-discipline` reads 2.5 before doing provenance
  work.
"""

TAIL_NEW = (AS_BUILT
            + "**Note:** RICE is Claude's proposal, unratified.\n"
              "**Ref:** L-192 (the checker); L-200 (the leg that "
              "records what a\nverdict caused); L-202 (the JSON schema "
              "it reads); L-206 (the return\nfilenames a review will "
              "come back under); `documentation/\n"
              "DESIGN_20260818_citation_prompt.md`; "
              "`documentation/patch_L207_1_\ncitation_prompt.py`.\n")

EDITS = [
    ('LEDGER_CONSOLIDATED.md', [
        (STATUS_OLD, STATUS_NEW),
        (ROW_OLD, ROW_NEW),
        (TAIL_OLD, TAIL_NEW),
    ]),
]


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(message):
    print('ERROR: %s' % message)
    print('Nothing was written.')
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    for name, expected in sorted(BASE.items()):
        if not os.path.isfile(name):
            return fail('%s not found. Save this script in the repo '
                        'root and run it there.' % name)
        with open(name, 'rb') as handle:
            found = fingerprint(handle.read())
        if found != expected:
            return fail('%s has moved since this patch was built '
                        '(expected %s, found %s).'
                        % (name, expected, found))

    if not os.path.isfile(SCRIPT):
        return fail('%s is not in the repo root. If it was already '
                    'archived, delete the move step and re-run.' % SCRIPT)
    if os.path.exists(ARCHIVE):
        return fail('%s already exists. Nothing was moved.' % ARCHIVE)

    # THE ENCODING GATE, SCOPED THE WAY THE CONVENTION SAYS.
    #
    # Hard-fail on non-ASCII this patch would INSERT. Fix what is
    # already there, because all three conditions hold: ASCII-only is
    # already ruled, the file is already being edited by this patch
    # and fingerprinted, and every substitution below is mechanical.
    # A dedicated sweep for 123 characters would never be scheduled,
    # and the fingerprint plus the all-or-nothing harness are exactly
    # what makes the fix safe -- conditions that will not recur more
    # cheaply than right now.
    #
    # Then print BOTH facts, because they are different: what was
    # normalized, and what was left. A patch that fixes some and not
    # all has to say which, or the next session reads a clean run as
    # a clean file.
    for _name, edits in EDITS:
        for _anchor, replacement in edits:
            try:
                replacement.encode('ascii')
            except UnicodeEncodeError as exc:
                return fail('this patch would insert non-ASCII text: %s'
                            % exc)

    staged = {}
    for name, edits in EDITS:
        with open(name, 'rb') as handle:
            data = handle.read()
        crlf = data.count(b'\r\n') > 0
        for anchor, replacement in edits:
            old = anchor.encode('ascii')
            new = replacement.encode('ascii')
            if crlf:
                old = old.replace(b'\n', b'\r\n')
                new = new.replace(b'\n', b'\r\n')
            count = data.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d '
                      'for %r' % (name, count, anchor[:70]))
                print('Nothing was written.')
                return 1
            data = data.replace(old, new)
        # Swept AFTER the anchored edits, so every anchor matched the
        # file's original bytes.
        text = data.decode('utf-8')
        had = sum(1 for char in text if ord(char) > 127)
        for bad, good in sorted(ASCII_SWEEP.items()):
            text = text.replace(bad, good)
        left = [char for char in text if ord(char) > 127]
        data = text.encode('utf-8')
        if had:
            print('  note %s had %d non-ASCII character(s); %d '
                  'normalized to ASCII in passing'
                  % (name, had, had - len(left)))
        # Printed whether or not anything is left. Silence about the
        # residual is how a partial sweep gets read as a clean file.
        print('  note %s still holds %d non-ASCII character(s) this '
              'patch did not reach%s'
              % (name, len(left),
                 (': ' + ' '.join(sorted(set(left)))) if left else ''))
        staged[name] = data

    for name, data in sorted(staged.items()):
        with open(name, 'wb') as handle:
            handle.write(data)
        print('  ok  %s (%d bytes)' % (name, len(data)))

    shutil.move(SCRIPT, ARCHIVE)
    print('  ok  moved %s -> %s' % (SCRIPT, ARCHIVE))

    print('patch applied')
    print('')
    print('NOW RUN, and it is not optional:')
    print('  python ledger_index.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
