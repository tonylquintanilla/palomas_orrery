"""L-223 patch 1 of 2 -- safe-file-editing gains the paste rule (v1.7).

Built on d424c459ef31dbac23b493e43b0b6ad35bf0d495 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT THIS DOES

Adds one subsection to skills/safe-file-editing/SKILL.md, under the
existing Delivery Format section, and bumps the skill from 1.6 to 1.7.

The rule: an edit to a version-controlled file is delivered as a patch
script, INCLUDING prose, markdown and ledger files -- not as text for
Tony to paste. The reason is not that any particular editor is buggy.
It is that a hand-paste is an unverified transfer: nothing compares
what arrived against what was sent, and no participant in the chain
owns reporting completion. A patch script writes bytes through one
synchronous call that either returns or raises, and then says what it
changed.

WHY IT GOES HERE AND NOT IN THE LEDGER

The dated instance -- what Tony saw in VS Code on 2026-08-21 -- goes
in the ledger as L-223, where a perishable observation belongs. This
is the durable half, and it is written to outlive the editor.

WHAT IT CLOSES

The skill read as though patch discipline were for .py files. It never
said so, but every example was code, and this project had been
hand-editing a 579 KB markdown ledger on that silence.

AFTER IT RUNS -- TWO THINGS, BOTH TONY

  1. (do) Run skills_index.py so the manifest table in
     PROJECT_INSTRUCTIONS.md regenerates and reads 1.7.
  2. (do) Reinstall the skill to the account profile
     (Settings > Skills). The repo copy is not the copy Claude loads.

And one obligation that cannot be discharged here. A mid-session skill
bump is NOT verifiable from inside the session that makes it -- the
loaded copy appears bound when the conversation starts. So this
session's loaded copy still reads 1.6, and the NEXT session confirms
its loaded copy reads 1.7 before doing patch work. That sentence
belongs in the handoff. (Tony's ruling, 2026-08-11.)

HOW TO RUN IT

Save it to the repo root, open it in VS Code, press Run. It takes no
arguments. It writes nothing on any failure.

Written August 21, 2026 with Anthropic's Claude Opus 5 (L-223).
"""

import hashlib
import os
import sys

PATH = os.path.join('skills', 'safe-file-editing', 'SKILL.md')
FINGERPRINT = '3f7b50c3b21d07c265c4d2d13b1d416d'

VERSION_OLD = """Skill version: 1.6 | Cut from palomas_orrery @ ef3bd13 (v1.6), earlier @
50438c6 (v1.5), a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2),
bdaaa0c (v1.1) | August 20, 2026, with Anthropic's Claude Opus 5"""

VERSION_NEW = """Skill version: 1.7 | Cut from palomas_orrery @ d424c459 (v1.7),
earlier @ ef3bd13 (v1.6), 50438c6 (v1.5), a872205 (v1.4), 1ba20c3
(v1.3), 3398970 (v1.2), bdaaa0c (v1.1) | August 21, 2026, with
Anthropic's Claude Opus 5"""

HISTORY_OLD = """v1.6 generalises that section to
every file type, because 1.5's only concrete example was a Python module
docstring and the rule's founding case was stale Markdown headers -- it
would not have fired on the files it was written for."""

HISTORY_NEW = """v1.6 generalises that section to
every file type, because 1.5's only concrete example was a Python module
docstring and the rule's founding case was stale Markdown headers -- it
would not have fired on the files it was written for. v1.7 adds A Paste
Is An Unverified Transfer (L-223), which extends the delivery rule to
prose, markdown and ledger files -- every example in 1.6 was code, and
this project had been hand-editing a 579 KB ledger on that silence."""

ANCHOR = """

## Encoding Gate [QUALITY]"""

INSERT = """

### A Paste Is An Unverified Transfer [QUALITY]

The delivery rule above covers PROSE too -- markdown, documentation,
the ledger. An edit to any version-controlled file is delivered as a
patch script, not as text for Tony to paste into an editor.

The reason is not that any editor is buggy. It is what a paste is.

Text on a clipboard passes through several participants -- the source
application, the OS clipboard, the editor's own paste handling, the
buffer, the save. Not one of them owns reporting the outcome. Nothing
anywhere compares what arrived against what was sent. So a paste that
silently dropped and a paste that landed perfectly produce the same
evidence, which is none. That is true on a good day; a slow or failed
paste only makes the property briefly visible.

A patch script has the opposite shape. The text is already inside the
file when it reaches the machine, having travelled as a file rather
than through the clipboard. The script opens the target, writes bytes
through one synchronous call that either returns or raises, and then
prints what it changed. Success carries evidence.

So: **a document edit is a patch, the same as a code edit.** Anchor on
structure rather than on exact line wrapping when the target is prose
that may have been reflowed -- find the heading, find the next
heading, work between them -- and require every anchor to match
exactly once.

WHEN A HAND EDIT IS UNAVOIDABLE, the human check is to watch until the
text actually appears before clicking or typing anything else, and to
NOT retry on silence. Retrying is the natural response to a paste that
seems not to have happened, and it is how one pending transfer becomes
two. Name this for what it is: a person looking, standing in for a
check the tooling does not perform. It works, and it holds right up
until the session where someone is tired or moving fast. That is the
argument for the patch being the default rather than the fallback.

(Origin: L-223, 2026-08-21. A paste into LEDGER_CONSOLIDATED.md
appeared to do nothing several times, then completed about a minute
later. Tony caught it only because he was comparing the paste against
the copy -- which is this project's own confirming question, asked of
a text editor.)

## Encoding Gate [QUALITY]"""


def die(reason):
    print('')
    print('STOPPED. %s' % reason)
    print('Nothing was written.')
    sys.exit(1)


def swap(text, old, new, where):
    found = text.count(old)
    if found != 1:
        die('anchor for %s matched %d times, expected exactly 1.'
            % (where, found))
    for char in new:
        if ord(char) > 127:
            die('non-ASCII character %r would be inserted into %s.'
                % (char, where))
    return text.replace(old, new, 1)


def main():
    if not os.path.isdir('documentation'):
        die('no documentation/ directory here. Run this from the '
            'palomas_orrery repo root.')
    if not os.path.exists(PATH):
        die('%s not found.' % PATH)

    with open(PATH, 'rb') as handle:
        raw = handle.read()
    if b'\r\n' in raw:
        die('%s has CRLF line endings; this patch expects LF.' % PATH)
    text = raw.decode('utf-8')

    actual = hashlib.md5(text.encode('utf-8')).hexdigest()
    if actual != FINGERPRINT:
        die('%s does not match the file this patch was written '
            'against.\n  expected md5 %s\n  found        %s'
            % (PATH, FINGERPRINT, actual))

    out = swap(text, VERSION_OLD, VERSION_NEW, 'the version line')
    out = swap(out, HISTORY_OLD, HISTORY_NEW, 'the version history')
    out = swap(out, ANCHOR, INSERT, 'the Encoding Gate heading')

    if out == text:
        die('the file came out identical to its input.')

    with open(PATH, 'wb') as handle:
        handle.write(out.encode('utf-8'))

    print('%s: 1.6 -> 1.7' % PATH)
    print('  added: A Paste Is An Unverified Transfer [QUALITY]')
    print('  under: Delivery Format, before the Encoding Gate')
    print('')
    print('NEXT, both yours:')
    print('  (do) run skills_index.py so the manifest reads 1.7')
    print('  (do) reinstall the skill to Settings > Skills')
    print('')
    print('The reinstall CANNOT be verified from inside this session. '
          'The next session confirms its loaded copy reads 1.7 before '
          'doing patch work. That line belongs in the handoff.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
