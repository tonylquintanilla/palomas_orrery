"""patch_L213_1_orbit_backup_trigger.py -- record the backup finding.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root, open it in VS Code,
and click Run. It takes no arguments.

    python patch_L213_1_orbit_backup_trigger.py

Then run, and it is NOT optional:

    python ledger_index.py

That is what places the L-213 block and puts its row in the index
table.

Success: one `ok` line, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and nothing is
written.

WHAT IT DOES
------------
Adds L-213 as OPEN. Records a finding and NOT a fix: the orbit cache
backup is triggered by module import rather than by a cache write, so
it is rewritten on every maintenance run and can overwrite a good
backup with a corrupted cache. The repair touches palomas_orrery.py
and wants a design pass first, which is Tony's ruling, 2026-08-19.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable; the ledger block is not.

Written August 2026 with Anthropic's Claude Opus 5. Built on
ce9dd81c2562a18673293eed806e24752eb834fd at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import sys


BASE = {
    'LEDGER_CONSOLIDATED.md': 'c7eef28199a932c00e0266c6a4698347',
}

ANCHOR = ("## C. RECONCILED LEDGER -- DONE (closed; for the record, "
          "do not re-do)\n")

BLOCK = """#### [L-213] Orbit cache backup fires on IMPORT, not on cache write
<!-- L:213 status:OPEN upd:2026-08-19 section:A flag: rice:2/3/75/2 -->
- **Found by L-212 on its second day.** The FILES WRITTEN block
  reported `data/orbit_paths_backup.json` rewritten with identical
  bytes on every maintenance run. Tony asked what was triggering it,
  since the intent is for the backup to be rewritten when the CACHE is
  updated.
- **The trigger, traced.** `create_orbit_backup()` is called at MODULE
  LEVEL in `palomas_orrery.py:3649` -- not inside a function, not
  behind an `if __name__` guard. `test_reset_completeness.py:39` does
  `importlib.import_module('palomas_orrery')`, and that test is in the
  maintenance suite. So importing the orrery runs the backup, and the
  suite imports the orrery every run. The cache is never touched; only
  the module is loaded.
- **Why this is more than a pointless rewrite.** The backup is
  `shutil.copy` of `data/orbit_paths.json` over
  `data/orbit_paths_backup.json`, unconditional. If the cache is ever
  corrupted and ANYTHING imports the orrery afterwards -- a GUI
  launch, a test run, a maintenance run -- the good backup is
  overwritten with the corrupted file. The window between corruption
  and loss is one import, and the maintenance suite makes an import
  routine.
- **Nothing has gone wrong yet**, and that is the shape of the risk
  rather than a reason to discount it: the defect costs nothing until
  the cache goes bad once.
- **Two repairs, different sizes.** The SMALL one: make the copy
  conditional on the source differing from the existing backup, which
  stops the rewrite and nothing else. The REAL one: back up when the
  cache is WRITTEN, which means moving the call out of module import
  and next to whatever saves `orbit_paths.json` (see
  `orbit_data_manager.py`, `ORBIT_PATHS_FILE` and the
  `save_orbit_paths` path), and keeping a copy that a later import
  cannot clobber.
- **Design pass first** (Tony, 2026-08-19). This touches
  `palomas_orrery.py`, which is Mode 1 territory -- targeted snippets,
  never a full-file rewrite -- and moving a module-level call changes
  startup behaviour for the GUI as well as the tests. Iterate the
  design in conversation before any code.
- **Confirm the dispatch before editing the leaf.** The same rule that
  opens L-209. `create_orbit_backup()` lives in
  `palomas_orrery_helpers.py:791` and is called from exactly one
  place; check that is still true at the time of the fix rather than
  trusting this note.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unmeasured -- how large the cache is, how often it is written
in a session, and whether any other module-level side effect in
`palomas_orrery.py` fires on the same import. The third question is
the one worth asking early, because a module-level call that runs
during a test suite is a pattern rather than an instance.
**Ref:** L-212 (the block that surfaced it); `palomas_orrery.py:3649`;
`palomas_orrery_helpers.py:791`; `test_reset_completeness.py:39`.

## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)
"""


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(message):
    print('ERROR: %s' % message)
    print('Nothing was written.')
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    name = 'LEDGER_CONSOLIDATED.md'
    if not os.path.isfile(name):
        return fail('%s not found. Save this script in the repo root '
                    'and run it there.' % name)
    with open(name, 'rb') as handle:
        data = handle.read()
    found = fingerprint(data)
    if found != BASE[name]:
        return fail('%s has moved since this patch was built (expected '
                    '%s, found %s).' % (name, BASE[name], found))

    if 'L:213 ' in data.decode('utf-8') or '[L-213]' in data.decode('utf-8'):
        return fail('L-213 is already in use.')

    try:
        BLOCK.encode('ascii')
    except UnicodeEncodeError as exc:
        return fail('this patch would insert non-ASCII text: %s' % exc)

    crlf = data.count(b'\r\n') > 0
    old = ANCHOR.encode('ascii')
    new = BLOCK.encode('ascii')
    if crlf:
        old = old.replace(b'\n', b'\r\n')
        new = new.replace(b'\n', b'\r\n')
    count = data.count(old)
    if count != 1:
        print('ANCHOR FAIL: expected 1 match, found %d' % count)
        print('Nothing was written.')
        return 1
    data = data.replace(old, new)

    with open(name, 'wb') as handle:
        handle.write(data)
    print('  ok  %s (%d bytes, 1 block added)' % (name, len(data)))
    print('patch applied')
    print('')
    print('NOW RUN, and it is not optional:')
    print('  python ledger_index.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
