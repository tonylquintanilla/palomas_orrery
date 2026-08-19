"""patch_L212_2_records.py -- record L-212 in the ledger and handoff.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root, open it in VS Code,
and click Run. It takes no arguments.

    python patch_L212_2_records.py

Then run, and it is NOT optional:

    python ledger_index.py

That is what places the L-212 block in the closed section and puts its
row in the index table.

Success: two `ok` lines, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and nothing is
written.

WHAT IT DOES
------------
1. Adds L-212 to the ledger as DONE, with its as-built record. The
   feature shipped before it was recorded, which is backwards; this
   closes that.
2. Adds two paragraphs to HANDOFF_20260819_pilot_ran.md so the next
   session is not surprised by a block in the runner output that no
   handoff mentions -- and so one wrong claim made in conversation is
   corrected in writing rather than left in the chat.

THE CORRECTION, since it is the part worth reading. On first run in a
sandbox the new block reported `test_output/test_orbit_paths.json` as
REMOVED by the suite, and that was passed to Tony as a finding. It was
not. The sandbox lacks astroquery, so `test_orbit_cache.py` failed and
left the file deleted. On a working machine the same run reports it
rewritten with identical bytes. The tool was right both times; the
reading of it was wrong once.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable; the ledger block and the handoff paragraphs
are not.

Written August 2026 with Anthropic's Claude Opus 5. Built on
d2cb5279f332975ca6aa6458827082b56f9089d3 at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import sys


BASE = {
    'LEDGER_CONSOLIDATED.md':
        'b0836344fc3a1c3471f7ecac397517ed',
    'documentation/HANDOFF_20260819_pilot_ran.md':
        '7a84c9f6b8ec2d890a5293ad5623af48',
}


LEDGER_ANCHOR = ("## C. RECONCILED LEDGER -- DONE (closed; for the "
                 "record, do not re-do)\n")

LEDGER_BLOCK = """## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

#### [L-212] maintenance_run names every file the run wrote
<!-- L:212 status:DONE upd:2026-08-19 section:C flag: rice:2/3/90/1 -->
- **Asked for by Tony, 2026-08-19**, after watching a run: "could we
  list the files that were modified by the run, by name? we list some
  but not all i believe." Correct. The four GENERATORS declare their
  outputs and their rows name them; the CHECKERS declare nothing, and
  five artifacts were being written every run with nothing on screen
  saying so -- `WORKSHEET_CHECK.md`, `data/worksheet_routed.json`,
  `documentation/prompts/citation_review.jsonl`, `PROVENANCE_AUDIT.md`
  and `data/provenance_history.json`.
- **As built** (`patch_L212_1_files_written`). A FILES WRITTEN THIS RUN
  block after the verdict summary, naming every changed file, split
  into written / created / removed / rewritten-with-identical-bytes.
  Printed on every run including one that changes nothing.
- **MEASURED, NOT DECLARED, and that was the design decision.** The
  obvious fix is an output list per checker matching the generators.
  That is a second store of a fact the tools already own, and it drifts
  in one direction only: the next artifact somebody adds is invisible
  again and nothing fails to report it. A tree snapshot before and
  after reports what actually happened, so a file written by a tool
  nobody declared still appears.
- **Cost measured before the design was chosen**, not after. A stat
  walk over 1,329 files is about 0.01 s; hashing everything at or under
  2 MB is about 0.13 s. Two snapshots cost roughly a third of a second
  against a run of 100 seconds or more.
- **The blind spot announces itself.** Files over 2 MB are compared by
  size and mtime rather than content, and the count of them prints
  every run. On Tony's machine that is 22 files; a same-size edit to
  one would read as touched rather than written, and the line saying so
  is what keeps that from being a silent gap.
- **Success carries evidence.** The block prints the number of files
  EXAMINED, not only the number changed. "Nothing was written" and
  "nothing was looked at" are otherwise the same sentence.
- **Found on its first outing**: `data/worksheet_check_state.json`,
  written by the checker every run and named nowhere.
- **A wrong reading, recorded.** The first sandbox run reported
  `test_output/test_orbit_paths.json` as REMOVED and Claude passed that
  to Tony as a finding. It was an artifact of the sandbox lacking
  astroquery, so `test_orbit_cache.py` failed and left the file
  deleted. On a working machine the same run reports it rewritten with
  identical bytes. The tool was right both times; the reading of it was
  wrong once, which is the failure mode a diff tool invites.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-188 (the runner); L-205 (the summary line this sits under);
`documentation/patch_L212_1_files_written.py`.
"""


HANDOFF_ANCHOR = ("**`provenance-discipline` went 2.4 to 2.5**, adding "
                  "Extend a Boundary\nBefore Adding a Path -- the rule "
                  "an external review proposed on\n2026-08-18 and Tony "
                  "adopted. L-207 was the first item checked against\nit "
                  "rather than assumed to pass.\n")

HANDOFF_BLOCK = """**`provenance-discipline` went 2.4 to 2.5**, adding Extend a Boundary
Before Adding a Path -- the rule an external review proposed on
2026-08-18 and Tony adopted. L-207 was the first item checked against
it rather than assumed to pass.

**L-212, added after this handoff was first written.**
`maintenance_run.py` now prints a FILES WRITTEN THIS RUN block naming
every file the suite changed, split into written, created, removed and
rewritten-with-identical-bytes. It measures a tree snapshot before and
after rather than asking each checker to declare its outputs, so an
artifact nobody declared still appears. Expect the block at the bottom
of every run from now on; it is not a new failure mode, it is the
runner saying what it did.

**And a correction that belongs in writing rather than in a chat.** On
its first sandbox run that block reported
`test_output/test_orbit_paths.json` as REMOVED by the suite, and Claude
passed that to Tony as a finding. It was not one: the sandbox lacks
astroquery, `test_orbit_cache.py` failed, and the file was left
deleted. On a working machine the same run reports it rewritten with
identical bytes. The tool was right both times and the reading of it
was wrong once -- which is exactly the failure a diff tool invites, and
worth knowing before the next session reads its first block.
"""


EDITS = [
    ('LEDGER_CONSOLIDATED.md', [(LEDGER_ANCHOR, LEDGER_BLOCK)]),
    ('documentation/HANDOFF_20260819_pilot_ran.md',
     [(HANDOFF_ANCHOR, HANDOFF_BLOCK)]),
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

    with open('LEDGER_CONSOLIDATED.md', 'rb') as handle:
        text = handle.read().decode('utf-8')
    if 'L:212 ' in text or '[L-212]' in text:
        return fail('L-212 is already in use.')

    for _name, edits in EDITS:
        for _anchor, replacement in edits:
            try:
                replacement.encode('ascii')
            except UnicodeEncodeError as exc:
                return fail('this patch would insert non-ASCII: %s' % exc)

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
                      'for %r' % (name, count, anchor[:60]))
                print('Nothing was written.')
                return 1
            data = data.replace(old, new)
        staged[name] = data

    for name, data in sorted(staged.items()):
        with open(name, 'wb') as handle:
            handle.write(data)
        left = sum(1 for byte in data if byte > 127)
        note = ''
        if left:
            note = ('  [note: %d pre-existing non-ASCII byte(s), '
                    'untouched -- prose]' % left)
        print('  ok  %s (%d bytes)%s' % (name, len(data), note))

    print('patch applied')
    print('')
    print('NOW RUN, and it is not optional:')
    print('  python ledger_index.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
