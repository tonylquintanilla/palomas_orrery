"""patch_skill_2_3_vocabulary.py -- provenance-discipline 2.2 -> 2.3.

RUN COMMAND
-----------
Put this file in the repo root, open it in VS Code, and click Run.

    python patch_skill_2_3_vocabulary.py

Then reinstall the skill to your account (Settings > Skills) and run
maintenance_run.py so skills_index.py rebuilds the manifest row in
PROJECT_INSTRUCTIONS.md. Archive this script to documentation/ after.

**The reinstall cannot be verified from inside this session.** The
skill copy a conversation loads is bound when the conversation starts,
so this bump goes into the handoff as an obligation the NEXT session
discharges on load. That is the standing rule and this patch does not
change it.

WHAT IT CHANGES
---------------
Four edits, all in the verdict-vocabulary block, plus the version line.

1. THE SIX TOKENS ARE ASSIGNED TO COLUMNS. The skill already says "two
   verdicts per row, never conflated" and "DERIVED answers the CITATION
   question" -- and then lists all six on one flat line, so the prose
   knows what the vocabulary forgets. The tier2 prompt used APPROX for
   the value question and PARTIAL for the citation question; they were
   never synonyms, and the flat list lost that.

2. UNSOURCED IS RESTORED AS A CITATION TOKEN. The tier2 prompt
   commissioned it by name and the skill later dropped it, so ten cells
   on disk use a word the vocabulary no longer contains. It maps to
   citation-NO with no loss of routing, and it is kept because the
   distinction it carries -- the source does not publish this value, as
   against the source publishes a different one -- is real.

3. THE VOCABULARY GETS A VERSION LINE. Worksheets state which
   vocabulary they were written against, so a tool can tell a
   pre-ruling file from a post-ruling one without guessing from dates.

4. QUOTING RULES FOR EVIDENCE. Tony's question -- who reads the Notes
   column -- had the answer "nothing does." A reason recorded where
   nothing consults it is a record that cannot fail. Quoting is
   transcription and NOT interpretation, but only when four properties
   hold, and two of them were being violated live.

DEAD LINK and OUTDATED were also commissioned by earlier prompts and
are NOT restored: zero cells on disk use either one.
"""

import hashlib
import os
import sys

TARGET = os.path.join('skills', 'provenance-discipline', 'SKILL.md')

ANCHOR_VERSION = 'Skill version: 2.2'
REPLACE_VERSION = 'Skill version: 2.3'

ANCHOR_VOCAB = """A verdict cell carries EXACTLY ONE of these tokens and nothing else,
with the reasoning in Notes:

    YES  NO  PARTIAL  APPROX  DERIVED  UNVERIFIED

Two verdicts per row, never conflated. `Value correct?` asks whether
the number is right; `Citation correct?` asks whether the named source
publishes it. A right number under a wrong authority is value-YES and
citation-NO, and that split is the whole reason for two columns."""

REPLACE_VOCAB = """A verdict cell carries EXACTLY ONE of these tokens and nothing else,
with the reasoning in Notes. **The tokens are scoped to their column.**

    Value correct?     YES  NO  APPROX  UNVERIFIED
    Citation correct?  YES  NO  PARTIAL  DERIVED  UNSOURCED  UNVERIFIED

Two verdicts per row, never conflated. `Value correct?` asks whether
the number is right; `Citation correct?` asks whether the named source
publishes it. A right number under a wrong authority is value-YES and
citation-NO, and that split is the whole reason for two columns.

**The scoping is the substance, not the formatting.** APPROX qualifies
a VALUE -- the number is right to a stated tolerance. PARTIAL qualifies
a CITATION -- the source supports some of what is claimed. They were
commissioned that way and they are not synonyms; listing all of them on
one flat line lost the distinction, and a checker reading the flat list
cannot tell which word answers which question.

UNSOURCED belongs to the citation column: the named source does not
publish this value at all, as against NO, which is the source
publishing a DIFFERENT value. Both send the row to conversation; the
distinction survives because it changes the repair.

**Vocabulary version.** A worksheet states which vocabulary it was
written against, on its own line near the top:

    Vocabulary: v2 (2026-08-13)

Seventeen worksheets on disk predate any settled vocabulary and carry
no such line. A tool reads the line rather than guessing from a date,
and an absent line means pre-v2 -- which is a fact about the file, not
a defect in it."""

ANCHOR_QUOTE = """The distinction matters because the same file can need both: a shell
module's display text needs value verification while its `# Source:`
comments need citation verification."""

REPLACE_QUOTE = """The distinction matters because the same file can need both: a shell
module's display text needs value verification while its `# Source:`
comments need citation verification.

### Quoting a Worksheet Is Transcription, Not Interpretation [CRITICAL]

A verdict token decides. Prose informs. Any tool reporting on a
worksheet may QUOTE what the checker wrote, and may never READ that
prose to decide anything.

The rule exists because of what the alternative turned out to be. Asked
who consults the Notes column, the answer was: nothing. The checker
reads Notes only to work out which row is about which value, and never
reports a word of it. So "the reason goes in Notes" meant the reason
went nowhere -- a record that cannot fail, because nothing opens it.

Quoting is safe when four properties hold. Two of them were being
violated in the L-192 checker's first report, which is how the rule got
written:

1. **Verbatim and DELIMITED.** The quoted cell is visibly separated
   from the tool's own words. Without this they fuse: a real finding
   read `reads NO -- wrong authority -- wrong authority for a value
   that may still be right`, half checker and half template, and no
   reader can tell which half is evidence.
2. **Untruncated**, or cut only at a mechanical limit with an explicit
   marker. A live finding cut mid-word at forty characters --
   `'Partial. Main interaction/loss claims ma'` -- reads as a
   transcription and is not one.
3. **Keyed to the MATCHED row only.** No row, no quote. A tool that
   goes hunting for a nearby note when the match failed has crossed
   into interpretation.
4. **Never fed to a decision.** No verdict, no routing, and no score
   reads quoted prose. If removing the quoting changes any outcome, the
   rule is already broken.

A compound cell -- a recognized token followed by prose -- classifies
by the token, is FLAGGED as compound, and its remainder rides the
quoting path verbatim. Reading the token and discarding the rest is the
tool deciding a qualification does not matter, which is interpretation
by omission."""


def read(path):
    with open(path, 'rb') as handle:
        return handle.read().replace(b'\r\n', b'\n')


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    if not os.path.exists(TARGET):
        print('STOP: %s is not here. Put this script in the repo root.'
              % TARGET)
        return 1

    raw = read(TARGET)
    text = raw.decode('utf-8')
    print('%s: %d bytes, md5 %s'
          % (TARGET, len(raw), hashlib.md5(raw).hexdigest()))

    if 'Skill version: 2.3' in text:
        print('Already applied. Nothing written.')
        return 0

    edits = [
        (ANCHOR_QUOTE, REPLACE_QUOTE, 'quoting section'),
        (ANCHOR_VOCAB, REPLACE_VOCAB, 'column-scoped vocabulary'),
        (ANCHOR_VERSION, REPLACE_VERSION, 'version line'),
    ]

    for anchor, _replacement, label in edits:
        if text.count(anchor) != 1:
            print('STOP: anchor for %s appears %d times, expected once. '
                  'Nothing written.' % (label, text.count(anchor)))
            return 1

    for anchor, replacement, label in edits:
        text = text.replace(anchor, replacement, 1)
        print('ok  %s' % label)

    with open(TARGET, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(text)

    after = read(TARGET)
    print('%s: %d bytes, md5 %s'
          % (TARGET, len(after), hashlib.md5(after).hexdigest()))
    print('')
    print('NEXT, and none of it is optional:')
    print('  1. Reinstall the skill in Settings > Skills.')
    print('  2. Run maintenance_run.py to rebuild the manifest row.')
    print('  3. The reinstall is NOT verifiable from the session that')
    print('     made it. Carry it in the handoff; the next session')
    print('     confirms its loaded copy reads 2.3 on load.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
