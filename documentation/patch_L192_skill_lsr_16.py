"""ledger-and-session-records 1.5 -> 1.6: where a file goes (L-192).

Domain: dev_tools

WHY THIS PATCH EXISTS

Two data files built this session -- the annotated-site list and the
key pins -- were first placed in documentation/ alongside handoffs and
spent patch scripts. Tony moved them to documentation/worksheets/,
reasoning that they are active rather than archived.

The reasoning is right and the wording needed one correction, which is
what makes this worth a skill entry rather than a folder habit. "Live
versus finished" does not survive contact with what is already in
documentation/worksheets/: the 35 files there are worksheets, and a
worksheet is the most finished thing in the project -- immutable
evidence, fixed at its date, never edited. It sits there anyway.

The distinction that actually holds is READ BY A TOOL versus READ BY A
PERSON. A worksheet is frozen but it is an input. A handoff is frozen
and no code opens it.

That framing matters beyond these two files. The request files the
builder will emit are tool inputs and go to worksheets/; the as-built
that describes them is a record and stays in documentation/. Without a
stated rule the split would be decided per file, by whoever is writing
one, which is how a folder habit becomes a folder mess.

WHAT IT CHANGES

skills/ledger-and-session-records/SKILL.md only:
  1. Version line 1.5 -> 1.6, with the source SHA and the reason.
  2. A new section, "Where a File Goes", after Anchor Requirement.

It does NOT touch the manifest. That is deliberate -- see below.

HOW TO RUN IT

Open in VS Code, press Run. It prints what it found before writing,
and writes nothing if any check fails. Safe to run twice.

THREE STEPS, ONE COMMIT -- the binding rule in the skill itself

  1. (this patch)  bump the version line in SKILL.md
  2. (you)         press Run on skills_index.py, which rewrites the
                   manifest row in PROJECT_INSTRUCTIONS.md and in
                   documentation/project_instructions_v3_39.md
  3. (you)         commit SKILL.md and both protocol copies together

Leaving step 2 to a later checkpoint is what let the manifest
advertise 1.1 against an actual 1.2 for about three weeks.

TWO THINGS THAT FOLLOW AND CANNOT BE DONE HERE

Re-upload PROJECT_INSTRUCTIONS.md to the Claude UI project after step
2, and reinstall the skill to your account profile (Settings >
Skills).

And the obligation for the next session, which belongs in the handoff:
ledger-and-session-records goes to 1.6 in this push; the session that
bumped it had 1.5 loaded; a mid-session reinstall cannot be verified
from inside the session, so the NEXT session confirms its loaded copy
reads 1.6 before doing ledger or handoff work.

Patch written August 2026 with Anthropic's Claude Opus 5, built on
305b2697648590e4a75551c73743abc98bd20c66 at
https://github.com/tonylquintanilla/palomas_orrery.
"""

import hashlib
import os
import sys

TARGET = os.path.join('skills', 'ledger-and-session-records', 'SKILL.md')

EXPECTED_FINGERPRINT = 'ec65a04d4c450eada8c27c4bc74d4b49'

ALREADY = b'Skill version: 1.6'

OLD_VERSION = (b'Skill version: 1.5 | Cut from palomas_orrery @ 3398970 '
               b'| August 5, 2026')

NEW_VERSION = (b'Skill version: 1.6 | Cut from palomas_orrery @ 305b269 '
               b'(v1.6), earlier\n@ 3398970 (v1.5) | August 14, 2026')

ANCHOR_SECTION = b'## Handoff Structure (the load-bearing lines)'

NEW_SECTION = b"""## Where a File Goes [QUALITY]

Two directories, and the test is not how finished the file is.

  documentation/            read by a PERSON, occasionally
  documentation/worksheets/ read by a TOOL, on every run

A worksheet is the most finished thing in the project -- immutable
evidence, fixed at its date, never edited -- and it lives in
worksheets/ because worksheet_checker.py opens it every run. A handoff
is equally frozen and lives in documentation/ because no code opens
it. So "active versus archived" is the wrong cut; "input versus
record" is the right one.

Applied:
- worksheets, request files the builder emits, prompt templates,
  pinned key lists, site lists  -> documentation/worksheets/
- handoffs, as-builts, manifests, design reviews, spent patch scripts,
  archived protocol copies                      -> documentation/

Two consequences worth stating.

A tool input must not be filed by resemblance. The as-built describing
a batch of request files is a record and stays in documentation/, even
though it is about files that live in worksheets/.

A non-.md file is invisible to the checker's loader, which takes only
.md from that directory. That is why a .txt pin list can sit in
worksheets/ without becoming a phantom uncited worksheet -- checked,
not assumed, before the two files were moved there.

(Origin, August 14, 2026: the L-192 site list and key pins were first
written to documentation/ among the handoffs and the roughly one
hundred spent patch scripts. Tony moved them and named the reason. The
wording here is the corrected form of his rule -- his "live versus
finished" cut would have sent the worksheets themselves the other
way.)

"""


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(project_dir, TARGET)

    print('=' * 70)
    print('PATCH: ledger-and-session-records 1.5 -> 1.6 (L-192)')
    print('=' * 70)

    if not os.path.exists(path):
        print('  STOPPED: %s not found.' % TARGET)
        print('  Put this patch in the repo root and run it again.')
        return 1

    with open(path, 'rb') as handle:
        data = handle.read()

    found = fingerprint(data)
    print('  Fingerprint expected: %s' % EXPECTED_FINGERPRINT)
    print('  Fingerprint found:    %s' % found)

    if ALREADY in data:
        print('  STOPPED: the skill already reads 1.6. Nothing to do.')
        return 0

    if found != EXPECTED_FINGERPRINT:
        print('  STOPPED: this is not the file the patch was built against.')
        print('  Nothing written. Do not edit the fingerprint to pass.')
        return 1

    newline = b'\r\n' if data.count(b'\r\n') > data.count(b'\n') // 2 \
        else b'\n'
    print('  Line ending:          %r' % newline)

    edits = [
        (OLD_VERSION, NEW_VERSION),
        (ANCHOR_SECTION, NEW_SECTION + ANCHOR_SECTION),
    ]

    # Stage every edit before writing anything. One anchor matching
    # zero or twice aborts the whole patch with the file untouched.
    staged = data
    for old, new in edits:
        if newline == b'\r\n':
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        matches = staged.count(old)
        print('  Anchor matches:       %d (need exactly 1) -- %s'
              % (matches, old.split(b'\n')[0][:46].decode('ascii', 'replace')))
        if matches != 1:
            print('  STOPPED: nothing written.')
            return 1
        staged = staged.replace(old, new)

    temporary = path + '.patch_tmp'
    with open(temporary, 'wb') as handle:
        handle.write(staged)
    os.replace(temporary, path)

    print('  WROTE: version line bumped, one section added.')
    print()
    print('  NOW DO STEP 2, in this same commit:')
    print('    press Run on skills_index.py, then commit SKILL.md and')
    print('    BOTH protocol copies together.')
    print('  Then re-upload PROJECT_INSTRUCTIONS.md to the Claude UI')
    print('  project and reinstall the skill in Settings > Skills.')
    print('=' * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
