"""patch_L212_1_files_written.py -- name every file the run wrote.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root, open it in VS Code,
and click Run. It takes no arguments.

    python patch_L212_1_files_written.py

Then run the maintenance runner and read the new block at the bottom:

    python maintenance_run.py

Success: one `ok` line, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and nothing is
written.

WHAT IT DOES
------------
Adds a FILES WRITTEN block to the end of maintenance_run.py's output,
naming every file the run changed.

The gap it closes, in Tony's words: "we list some but not all." True.
The four GENERATORS declare their outputs and their rows name them.
The CHECKERS declare nothing, so five artifacts were being written
every run with nothing on screen saying so:

    WORKSHEET_CHECK.md
    data/worksheet_routed.json
    documentation/prompts/citation_review.jsonl
    PROVENANCE_AUDIT.md
    data/provenance_history.json

MEASURED, NOT DECLARED
----------------------
The obvious fix is to give each checker an output list like the
generators have. This does not do that, on purpose. A declared list is
a second store of a fact the tools already own, and it drifts silently
-- the next artifact somebody adds is invisible again, and nothing
fails to say so. That is the shape of a check that cannot fail.

Instead the runner takes a snapshot of the working tree before the
suite and another after, and reports the difference. A file written by
a tool nobody thought to declare shows up anyway, which is the whole
point.

The cost is measured, not assumed: the stat walk over 1,329 files is
about 0.01 s, and hashing every file at or under 2 MB is about 0.13 s.
Two snapshots cost roughly a third of a second against a run of 100
seconds or more. Fourteen files exceed 2 MB -- bulk climate and ocean
data totalling 218 MB -- and are compared by size and mtime instead of
content. That limitation is PRINTED rather than assumed away.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable; the block it installs is not.

Written August 2026 with Anthropic's Claude Opus 5. Built on
d5814d3af2947fc85e3c786aca174e2a1100507d at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import sys


BASE = {
    'maintenance_run.py': 'f0760be3f24ad116f76bbf1d9eae8356',
}


HELPERS = '''

# ============================================================
# WHAT THE RUN WROTE (L-212)
# ============================================================
#
# The generators declare their outputs and their rows name them. The
# checkers declare nothing, and they write five artifacts between
# them, so a run could rewrite WORKSHEET_CHECK.md, the routing file,
# the citation prompt, PROVENANCE_AUDIT.md and the history file with
# nothing on screen saying so. Tony asked for the missing names.
#
# MEASURED, NOT DECLARED. The obvious fix is an output list per
# checker, matching the generators. That is a second store of a fact
# the tools already own, and it drifts in one direction only: the next
# artifact added is invisible again, and nothing fails to report it.
# Snapshotting the tree instead means a file written by a tool nobody
# declared still appears.
#
# The cost was measured before the design was chosen. A stat walk over
# 1,329 files is about 0.01 s; hashing everything at or under the size
# limit is about 0.13 s. Two snapshots cost roughly a third of a
# second against a run of 100 seconds or more.
#
# THE BLIND SPOT ANNOUNCES ITSELF. Fourteen files exceed the limit --
# bulk climate and ocean data, 218 MB of it -- and are compared by
# size and mtime rather than content, so a same-size edit to one of
# them would be reported as touched rather than written. The summary
# prints that count every run rather than hiding it.

# Files larger than this are compared by size and mtime, not content.
HASH_LIMIT_BYTES = 2 * 1024 * 1024

# Not part of the working tree for this purpose. .git is git's own
# business, __pycache__ is a build product of running the suite at all,
# and a virtualenv is not project state.
SKIP_DIRS = ('.git', '__pycache__', '.venv', 'venv', '.pytest_cache',
             'node_modules')


def tree_snapshot(project_dir):
    """{relative path: (mtime_ns, size, hash or None)} for the tree.

    The hash is LF-normalized, like every other fingerprint in this
    project, because a CRLF working copy is not a content change.
    """
    seen = {}
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = os.path.join(root, name)
            try:
                stat = os.stat(path)
            except OSError:
                continue
            digest = None
            if stat.st_size <= HASH_LIMIT_BYTES:
                try:
                    with open(path, 'rb') as handle:
                        digest = hashlib.md5(
                            handle.read().replace(b'\\r\\n', b'\\n')
                        ).hexdigest()
                except OSError:
                    digest = None
            key = os.path.relpath(path, project_dir).replace(os.sep, '/')
            seen[key] = (stat.st_mtime_ns, stat.st_size, digest)
    return seen


def tree_diff(before, after):
    """(written, created, removed, touched, unhashed).

    `written` changed content. `touched` was rewritten with identical
    bytes, which matters operationally: a real change to
    PROJECT_INSTRUCTIONS.md has to be re-uploaded to the Claude UI and
    an identical rewrite does not. `unhashed` counts files too large to
    compare by content, so the reader knows what the answer does not
    cover.
    """
    written, created, removed, touched = [], [], [], []
    unhashed = 0
    for path, now in sorted(after.items()):
        if now[2] is None:
            unhashed += 1
        was = before.get(path)
        if was is None:
            created.append(path)
            continue
        if now[2] is not None and was[2] is not None:
            if now[2] != was[2]:
                written.append(path)
            elif now[0] != was[0]:
                touched.append(path)
        elif now[1] != was[1]:
            written.append(path)
        elif now[0] != was[0]:
            touched.append(path)
    for path in sorted(before):
        if path not in after:
            removed.append(path)
    return written, created, removed, touched, unhashed


def print_files_written(before, after):
    """Name every file the run changed. Printed on every run."""
    written, created, removed, touched, unhashed = tree_diff(
        before, after)

    print()
    print('FILES WRITTEN THIS RUN')
    print('-' * 70)
    # Success carries evidence: the count of files EXAMINED, not just
    # the count changed. "Nothing written" and "nothing looked at" are
    # the same sentence otherwise.
    print('  %d file(s) examined, %d written, %d created, %d removed, '
          '%d rewritten identically'
          % (len(after), len(written), len(created), len(removed),
             len(touched)))
    for label, paths in (('written', written), ('created', created),
                         ('removed', removed)):
        for path in paths:
            print('    %-9s %s' % (label, path))
    if touched:
        print('    rewritten with identical bytes, no action needed:')
        for path in touched:
            print('      %s' % path)
    if unhashed:
        print('    %d file(s) over %d MB compared by size and mtime '
              'only' % (unhashed, HASH_LIMIT_BYTES // (1024 * 1024)))
    if not (written or created or removed):
        print('    nothing changed on disk')

'''


HOOK_OLD = """    print('=' * 70)
    print('MAINTENANCE RUN -- generators, then checkers (L-188)')
    print('=' * 70)
"""

HOOK_NEW = """    print('=' * 70)
    print('MAINTENANCE RUN -- generators, then checkers (L-188)')
    print('=' * 70)

    # Bracketed around the whole suite, so the report covers every
    # tool rather than the ones that happened to declare an output.
    tree_before = tree_snapshot(project_dir)
"""

TAIL_OLD = """    print('=' * 70)

    # ---- detail for failures only -------------------------------------"""

TAIL_NEW = """    print('=' * 70)

    # ---- what the run wrote (L-212) -----------------------------------
    # After the verdict block, because the verdict is what the push
    # call turns on. Printed whether or not anything changed: a run
    # that wrote nothing should say so rather than leaving the reader
    # to infer it from an absence.
    print_files_written(tree_before, tree_snapshot(project_dir))

    # ---- detail for failures only -------------------------------------"""


EDITS = [
    ('maintenance_run.py', [
        # The helpers go after snapshot(), whose docstring already
        # explains why mtime and content are two facts rather than one.
        ("def last_meaningful_line(text):\n",
         HELPERS.lstrip('\n') + "\ndef last_meaningful_line(text):\n"),
        (HOOK_OLD, HOOK_NEW),
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
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            return fail('%s would hold non-ASCII bytes: %s' % (name, exc))

    for name, data in sorted(staged.items()):
        with open(name, 'wb') as handle:
            handle.write(data)
        print('  ok  %s (%d bytes)' % (name, len(data)))

    print('patch applied')
    print('')
    print('Next: python maintenance_run.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
