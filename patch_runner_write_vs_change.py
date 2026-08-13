"""
patch_runner_write_vs_change.py -- maintenance_run.py reports whether a
generator WROTE a file, separately from whether the content MOVED

Why: skills_index.py rewrites the manifest zone every run whether or not
the bytes move. The file gets a new timestamp, Windows Explorer shows it
as new, and the runner prints "unchanged" because the content hash held.
Both are correct and the screen said nothing about the difference. That
matters operationally -- a REAL change to PROJECT_INSTRUCTIONS.md has to
be uploaded to the Claude UI, and a rewrite with identical bytes does
not.

After this patch the three generator states read:

    Skill manifest    0.1s  rewrote PROJECT_INSTRUCTIONS.md
    Skill manifest    0.1s  unchanged (1 of 1 rewritten, content identical)
    Ledger index      0.2s  unchanged (1 checked, not written)

Three anchored edits, all-or-nothing. Nothing is written unless every
anchor matches exactly once.

  1. fingerprint() -> snapshot(), returning (mtime_ns, content hash)
  2. the generator loop reads both facts
  3. the note distinguishes the three states

Not in scope: the CHECKER delta gap ((do) item 6, filed in L-188), where
a checker's full output prints only on failure. Separate change.

TARGET: maintenance_run.py (path resolved relative to this script, so
save this file at the REPO ROOT).

Built on 173902b3f5c52ccc998cad1102d13d26f2e4c202 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

RUN: save at the repo root, open in VS Code, click Run.
     Equivalent command line: python patch_runner_write_vs_change.py

SUCCESS: one "ok" line per edit, then "patch applied (N bytes)".
FAILURE: a single "ERROR:" or "ANCHOR FAIL" line. Nothing is written
         either way, so it is always safe to re-check and retry.

AFTER RUNNING: python maintenance_run.py
     The Skill manifest row should read "unchanged (1 of 1 rewritten,
     content identical)" on a run where nothing moved. If it reads
     "1 checked, not written" instead, skills_index.py is skipping the
     write when the zone is already correct -- also fine, and now
     visible either way.

Role: patch
Domain: dev_tools

Script created: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'maintenance_run.py'

# md5 of the LF-normalized base content this patch was written against
BASE_FP = 'fab362618ef8e6f84dce085662477234'


EDITS = []

# ---------------------------------------------------------------- 1
EDITS.append((
    b"def fingerprint(path):\n"
    b"    \"\"\"MD5 over LF-normalized content, or None if the file is absent.\n"
    b"\n"
    b"    Normalized because a CRLF working copy is not a content change --\n"
    b"    the same reason the patch scripts fingerprint this way.\n"
    b"    \"\"\"\n"
    b"    if not os.path.exists(path):\n"
    b"        return None\n"
    b"    with open(path, 'rb') as handle:\n"
    b"        return hashlib.md5(handle.read().replace(b'\\r\\n', b'\\n')).hexdigest()\n",

    b"def snapshot(path):\n"
    b"    \"\"\"(mtime_ns, content hash) for a file, or (None, None) if absent.\n"
    b"\n"
    b"    TWO facts, deliberately, because a generator can change one\n"
    b"    without the other. skills_index.py rewrites its manifest zone on\n"
    b"    every run whether or not the bytes move: the mtime advances, the\n"
    b"    hash does not. Windows Explorer shows the first and this runner\n"
    b"    used to report only the second, so a file could look new on disk\n"
    b"    while the screen said 'unchanged' and neither was wrong.\n"
    b"\n"
    b"    The distinction is operational, not cosmetic. A real change to\n"
    b"    PROJECT_INSTRUCTIONS.md has to be re-uploaded to the Claude UI;\n"
    b"    a rewrite with identical bytes does not.\n"
    b"\n"
    b"    The hash is LF-normalized because a CRLF working copy is not a\n"
    b"    content change -- the same reason the patch scripts fingerprint\n"
    b"    this way.\n"
    b"    \"\"\"\n"
    b"    if not os.path.exists(path):\n"
    b"        return (None, None)\n"
    b"    mtime = os.stat(path).st_mtime_ns\n"
    b"    with open(path, 'rb') as handle:\n"
    b"        digest = hashlib.md5(\n"
    b"            handle.read().replace(b'\\r\\n', b'\\n')).hexdigest()\n"
    b"    return (mtime, digest)\n",
))

# ---------------------------------------------------------------- 2
EDITS.append((
    b"        before = dict((path, fingerprint(path)) for path in outputs)\n"
    b"        rc, output, seconds = run_tool(project_dir, argv_tail)\n"
    b"        after = dict((path, fingerprint(path)) for path in outputs)\n"
    b"        moved = [path for path in outputs if before[path] != after[path]]\n",

    b"        before = dict((path, snapshot(path)) for path in outputs)\n"
    b"        rc, output, seconds = run_tool(project_dir, argv_tail)\n"
    b"        after = dict((path, snapshot(path)) for path in outputs)\n"
    b"        moved = [path for path in outputs\n"
    b"                 if before[path][1] != after[path][1]]\n"
    b"        written = [path for path in outputs\n"
    b"                   if before[path][0] != after[path][0]]\n",
))

# ---------------------------------------------------------------- 3
EDITS.append((
    b"        elif moved:\n"
    b"            note = 'rewrote ' + ', '.join(moved)\n"
    b"        else:\n"
    b"            note = 'unchanged'\n",

    b"        elif moved:\n"
    b"            note = 'rewrote ' + ', '.join(moved)\n"
    b"        elif written:\n"
    b"            note = ('unchanged (%d of %d rewritten, content identical)'\n"
    b"                    % (len(written), len(outputs)))\n"
    b"        else:\n"
    b"            note = ('unchanged (%d checked, not written)'\n"
    b"                    % len(outputs))\n",
))


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print('ERROR: target not found: %s' % path)
        print('       save this script at the repo root and run it there')
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    normalized = data.replace(b'\r\n', b'\n')
    fingerprint = hashlib.md5(normalized).hexdigest()
    if fingerprint != BASE_FP:
        print('ERROR: base moved -- expected %s, found %s'
              % (BASE_FP, fingerprint))
        print('       nothing written; re-anchor the patch before retrying')
        return 1

    is_crlf = data.count(b'\r\n') > 0

    # dry pass -- every anchor must match exactly once before anything writes
    for index, (old, _new) in enumerate(EDITS, start=1):
        probe = old.replace(b'\n', b'\r\n') if is_crlf else old
        count = data.count(probe)
        if count != 1:
            print('ANCHOR FAIL: edit %d expected 1 match, got %d' % (index, count))
            print('             first line: %s' % old.split(b'\n')[0][:64])
            print('             nothing written')
            return 1

    for index, (old, new) in enumerate(EDITS, start=1):
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        data = data.replace(old, new, 1)
        print('ok   edit %d' % index)

    with open(path, 'wb') as handle:
        handle.write(data)

    print('patch applied (%d bytes)' % len(data))
    print('')
    print('NEXT: python maintenance_run.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
