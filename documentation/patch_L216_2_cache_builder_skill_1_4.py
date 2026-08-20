"""Skill patch -- gallery-cache-builder 1.3 -> 1.4, adding the
discard-and-re-run recovery rule from L-216.

RUN COMMAND:  python patch_L216_2_cache_builder_skill_1_4.py

Save this file into the REPO ROOT (the folder holding skills/ and
skills_index.py), open it in VS Code, and click Run.

Built on 2f0aabe911d54c834977a22f0b09d9332798b131 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES
  Edit 1 -- adds a Recovery from a failed swap section after Recovery
            ordering.
  Edit 2 -- bumps the version line to 1.4 and re-pins its SHA.

PURE ADDITION CHECK
  Before writing, the script asserts that every line of the 1.3 file is
  still present in the 1.4 file. This exists because a skill rebuild in
  August 2026 was written as a replace instead of an insert and deleted
  its own version block. A bump that removes anything aborts.

AFTER IT RUNS
  1. Run skills_index.py the same way, to regenerate the Skill Manifest
     table in PROJECT_INSTRUCTIONS.md.
  2. (do) Reinstall the skill to your account: Settings > Skills.
     A mid-session reinstall CANNOT be verified from inside the session
     that makes it, so the NEXT session confirms its loaded copy reads
     1.4 before doing gallery-cache-builder work. That obligation goes
     in the handoff, not cleared here.

WHAT IS PERMANENT
  The script is disposable; the skill section it adds is not.
  Archive this file to documentation/ once it has run.

SUCCESS   one 'ok' line per edit, 'pure addition confirmed', then
          'patch applied (N bytes)'.
FAILURE   a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = os.path.join('skills', 'gallery-cache-builder', 'SKILL.md')
BASE_FP = 'd2afcbac3ff8eb662e5ad3e06f407e9e'   # content md5, CRLF-normalized

RECOVERY_OLD = b"""restore the directory. Moving the config out (L-114) closed that; a crash
mid-swap now self-heals on the next run.

## Validation stance
"""

RECOVERY_NEW = b"""restore the directory. Moving the config out (L-114) closed that; a crash
mid-swap now self-heals on the next run.

## Recovery from a failed swap: discard and re-run [QUALITY]

Tony's operational rule, 2026-08-19 (L-216). When a run leaves the gallery
repo showing deletions -- most visibly `data/solar-system/` gone, with
GitHub Desktop reporting deletions and no additions -- DISCARD the changes
in GitHub Desktop and RE-RUN the builder. Discard restores the live tree
from HEAD byte for byte; the re-run builds a fresh generation.

Three conditions make that safe, and they travel WITH the rule because the
rule is only safe while all three hold:

- the live tree is committed, so HEAD has something to restore from;
- the swap is all-or-nothing, so a failed run leaves a COMPLETE `.prev` or
  a complete staging directory and never a mixed one;
- nothing reaches the remote until Tony commits by hand.

Running with `--commit` breaks the third condition and therefore breaks
the rule. Do not use `--commit` while L-216 is open.

What causes it, as far as it is measured: a filesystem lock -- almost
certainly OneDrive -- makes directory renames fail. WHICH of the swap's
three renames the lock catches decides the damage. Catching the `.prev`
cleanup is harmless and self-heals, and it has been happening every night
since 2026-07-21; the roughly 30 `solar-system.quarantine_*` directories
are that, one per night, printing as normal because the builder is built
to survive it. Catching `staging -> live` has no in-run recovery and
leaves the live directory missing. Same cause, different victim.

Two things are NOT established and should not be asserted. Whether the
`staging -> live` rename is exposed to the same lock as the cleanup, or
was unlucky once, is one data point. And the run record is written INSIDE
the generation, so a run whose swap fails strands its own record in a
directory `.gitignore` hides -- meaning the committed history shows no
sign that a run lost its data. Recording the swap OUTCOME outside the
generation comes BEFORE fixing the cause; otherwise every recurrence costs
another evening of inference.

## Validation stance
"""

VERSION_OLD = (b'Skill version: 1.3 | Cut from tonyquintanilla.github.io '
               b'@ 02d7163 (code) and palomas_orrery @ 8e4b5ca (context) '
               b'| 2026-08-11\n')

VERSION_NEW = (b'Skill version: 1.4 | Cut from tonyquintanilla.github.io '
               b'@ 02d7163 (code) and palomas_orrery @ 2f0aabe (context), '
               b'earlier @ 8e4b5ca (v1.3) | 2026-08-19\n'
               b'v1.4 adds Recovery from a failed swap: discard and '
               b're-run -- Tony\'s\noperational rule of 2026-08-19, after a '
               b'nightly run wiped the served tree\nand the ~30 quarantine '
               b'directories turned out to be the same mechanism\nprinting '
               b'harmlessly every night since July 21 (L-216).\n')

EDITS = [
    ('recovery section added', RECOVERY_OLD, RECOVERY_NEW),
    ('version line 1.3 -> 1.4', VERSION_OLD, VERSION_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print('ERROR: %s not found under this script.' % TARGET)
        print('       Save the script into the repo root, next to skills/.')
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if BASE_FP != '__FILL__' and fp != BASE_FP:
        print('ERROR: BASE MOVED. expected %s, found %s' % (BASE_FP, fp))
        print('       Nothing written. Reconcile before re-running.')
        return 1
    print('base fingerprint %s' % fp)

    is_crlf = data.count(b'\r\n') > 0
    print('line endings: %s' % ('CRLF' if is_crlf else 'LF'))

    staged = data
    for name, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = staged.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d'
                  % (name, count))
            print('             Nothing written.')
            return 1
        staged = staged.replace(old, new)
        print('ok  %s' % name)

    before = [line for line in data.replace(b'\r\n', b'\n').split(b'\n')]
    after = set(staged.replace(b'\r\n', b'\n').split(b'\n'))
    missing = [line for line in before
               if line not in after and line.strip()]
    # The version line is the one deliberate replacement.
    missing = [line for line in missing
               if not line.startswith(b'Skill version: 1.3')]
    if missing:
        print('ERROR: NOT A PURE ADDITION. %d line(s) from 1.3 are gone:'
              % len(missing))
        for line in missing[:10]:
            print('       %s' % line.decode('ascii', 'replace')[:70])
        print('       Nothing written.')
        return 1
    print('pure addition confirmed (%d lines checked)' % len(before))

    with open(path, 'wb') as handle:
        handle.write(staged)
    print('patch applied (%d bytes)' % len(staged))
    print('')
    print('NEXT: 1. run skills_index.py to rebuild the Skill Manifest.')
    print('      2. reinstall gallery-cache-builder at Settings > Skills.')
    print('         The next session confirms its loaded copy reads 1.4.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
