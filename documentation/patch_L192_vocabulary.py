"""patch_L192_vocabulary.py -- checker to the settled vocabulary.

RUN COMMAND
-----------
Put this file in the repo root, open it in VS Code, and click Run.

    python patch_L192_vocabulary.py

Run it AFTER patch_skill_2_3_vocabulary.py. The two ship together:
the skill is the producer and the checker is the consumer, and a
producer that moves without its consumer is the drift this project
exists to kill. Archive both to documentation/ afterwards.

WHAT IT CHANGES
---------------
Four edits to worksheet_checker.py.

1. THE REGISTRY SHRINKS FROM TWENTY TOKENS TO SEVEN. Six, plus
   UNSOURCED as a citation token. Measured before deciding: of the
   three tokens earlier prompts commissioned by name, UNSOURCED appears
   ten times, DEAD LINK zero, OUTDATED zero. Every other extra --
   CONFIRMED, NOT FOUND, WRONG VALUE, WRONG CITATION, and a tail of
   one-offs -- was invented by a checker, and nearly all of them sit in
   the Resolution column of the five followup files already going back
   for redo. A translation table for files being re-commissioned is
   maintenance with no reader.

   Cost, measured: four annotations carry an unreadable verdict instead
   of two. Two move to send back, two off conversation.

2. COMPOUND CELLS ARE FLAGGED, NOT SILENTLY TRIMMED. A recognized
   token followed by prose still classifies by the token -- and now
   says so, and carries its remainder. Reading the token and discarding
   the rest is the tool deciding a qualification does not matter, which
   is interpretation by omission.

3. QUOTED EVIDENCE IS DELIMITED AND MARKED. Two live defects in the
   first report drove this. A finding read

       reads NO -- wrong authority -- wrong authority for a value
       that may still be right

   half checker and half template, fused past telling apart. Another
   was cut mid-word at forty characters with no marker. Verdict cells
   are now quoted between guillemets and truncated only at a stated
   limit with an explicit ellipsis.

4. THE NOTES CELL REACHES THE REPORT. It had no reader at all: the
   checker read Notes only to work out which row went with which value
   and never reported a word of it. It is now printed beside each
   routed finding, quoted the same way. The verdict is still decided by
   the token and only the token -- if removing the quoting changed any
   outcome, the rule would already be broken.

WHAT IT DOES NOT CHANGE
-----------------------
Nothing about routing, scoring, or the push gate. No annotation is
edited. The checker still does not write anything but its own report.
"""

import hashlib
import os
import sys

TARGET = 'worksheet_checker.py'

# ---- 1. the registry -----------------------------------------------

ANCHOR_TOKENS = """    'no': (V_REFUTED, SCOPE_EITHER),
    'wrong': (V_REFUTED, SCOPE_EITHER),
    'incorrect': (V_REFUTED, SCOPE_EITHER),
    'wrong value': (V_REFUTED, SCOPE_VALUE),
    'wrong citation': (V_REFUTED, SCOPE_CITATION),

    # UNVERIFIED means nobody looked. NOT FOUND means somebody looked
    # and the source does not publish it. Those are different findings
    # with different owners, and collapsing them would have reported
    # the Bennu row -- "Not checked" -- as a citation defect, which
    # blames the source for work that was never done.
    'unverified': (V_ABSENT, SCOPE_EITHER),
    'not checked': (V_ABSENT, SCOPE_EITHER),
    'n/a': (V_ABSENT, SCOPE_EITHER),
    'unsourced': (V_SOURCE_ABSENT, SCOPE_CITATION),
    'not found': (V_SOURCE_ABSENT, SCOPE_CITATION),

    'derived': (V_DERIVED, SCOPE_EITHER),
}"""

REPLACE_TOKENS = """    'no': (V_REFUTED, SCOPE_EITHER),

    # UNVERIFIED means nobody looked. UNSOURCED means somebody looked
    # and the source does not publish it at all. Those are different
    # findings with different owners, and collapsing them reported the
    # Bennu row -- "Not checked" -- as a citation defect, which blames
    # the source for work that was never done.
    'unverified': (V_ABSENT, SCOPE_EITHER),
    'unsourced': (V_SOURCE_ABSENT, SCOPE_CITATION),

    'derived': (V_DERIVED, SCOPE_EITHER),
}

# WHAT WAS REMOVED, AND WHY IT IS NOT COMING BACK.
#
# An earlier registry read twenty tokens. It was built by measuring the
# corpus rather than by reading the vocabulary, on the reasoning that a
# word the prompts had commissioned should be honored rather than
# refused. That reasoning holds for exactly one word.
#
# Measured across the seventeen cited worksheets: of the three tokens
# earlier prompts named beyond the six, UNSOURCED appears ten times,
# DEAD LINK zero, OUTDATED zero. Everything else -- CONFIRMED (14),
# WRONG CITATION (10), NOT FOUND (7), WRONG VALUE (5), and a tail of
# one-offs like 'thermosphere' and 'see F5' -- was invented at the
# keyboard, and nearly every one sits in the Resolution column of the
# five followup files already going back for redo.
#
# So the translation table would have been maintained for files being
# re-commissioned anyway. WRONG VALUE and WRONG CITATION are the
# clearest case: they exist only because a worksheet had ONE verdict
# column, and the two-column schema states which one is wrong without
# needing a compound word for it.
#
# Anything outside the seven now reads UNREADABLE and goes back. That
# is the intended behaviour, not a gap. (Tony's ruling, 2026-08-13,
# after Fable argued for grandfathering and the measurement showed the
# grandfathered population was being re-commissioned regardless.)"""

# ---- 2. compound flagging + 3. delimited quoting --------------------

ANCHOR_CLASSIFY = """    head = re.split(r'\\s+--\\s+|\\s*;\\s*|\\s*\\(', low)[0].strip().strip('.')
    # Longest token first, so "wrong citation" is never read as "wrong".
    for token in sorted(VERDICT_TOKENS, key=len, reverse=True):
        own, scope = VERDICT_TOKENS[token]
        if head == token or head.startswith(token + ' '):
            return own, text, (default_scope if scope == SCOPE_EITHER
                               else scope)
    return V_UNREADABLE, text, default_scope"""

REPLACE_CLASSIFY = """    head = re.split(r'\\s+--\\s+|\\s*;\\s*|\\s*\\(', low)[0].strip().strip('.')
    # Longest token first, so a two-word token is never read as its
    # first word alone.
    for token in sorted(VERDICT_TOKENS, key=len, reverse=True):
        own, scope = VERDICT_TOKENS[token]
        if head == token or head.startswith(token + ' '):
            return own, text, (default_scope if scope == SCOPE_EITHER
                               else scope)
    return V_UNREADABLE, text, default_scope


def is_compound(cell):
    \"\"\"Does this cell carry a recognized token PLUS other prose?

    Classifying by the leading token and discarding the rest is the
    tool deciding a qualification does not matter, which is
    interpretation by omission. A compound cell is flagged and its
    whole text rides the quoting path, so the qualification reaches a
    reader instead of being trimmed away.
    \"\"\"
    text = strip_cell(cell)
    if not text:
        return False
    low = text.lower().strip().strip('.')
    for token in sorted(VERDICT_TOKENS, key=len, reverse=True):
        if low == token:
            return False
        if low.startswith(token):
            return True
    return False


# Quoting a worksheet is TRANSCRIPTION, not interpretation. The token
# decides; prose informs. That distinction only survives if the quote
# is visibly separated from the tool's own words -- a live finding once
# read "reads NO -- wrong authority -- wrong authority for a value that
# may still be right", half checker and half template, and no reader
# could tell which half was evidence.
QUOTE_LIMIT = 160


def quoted(text):
    \"\"\"A worksheet cell, delimited, and cut only with a visible marker.\"\"\"
    body = strip_cell(text)
    if not body:
        return '(blank)'
    if len(body) > QUOTE_LIMIT:
        body = body[:QUOTE_LIMIT].rstrip() + ' [...]'
    return '<<%s>>' % body"""

# ---- the disposition uses the quoted form --------------------------

ANCHOR_DISPOSE = """    tag = token or 'blank'
    if own in VERDICT_CLEARS:
        return True"""

REPLACE_DISPOSE = """    tag = quoted(token)
    if own in VERDICT_CLEARS:
        return True"""

ANCHOR_UNREADABLE = """        claim.fail('L3', 'UNREADABLE_VERDICT',
                   '%s reads %r%s' % (where, tag[:40], extra), 'SEND BACK')
    return False"""

REPLACE_UNREADABLE = """        claim.fail('L3', 'UNREADABLE_VERDICT',
                   '%s reads %s -- not in the vocabulary%s'
                   % (where, tag, extra), 'SEND BACK')
    return False"""


# ---- 4. the Notes cell reaches the report --------------------------

ANCHOR_NOTES_C = """    table, (line_no, cells), rule = best
    claim.matched_line = line_no
    claim.match_rule = rule"""

REPLACE_NOTES_C = """    table, (line_no, cells), rule = best
    claim.matched_line = line_no
    claim.match_rule = rule
    # Keyed to the MATCHED row and nothing else. No row, no quote -- a
    # tool hunting for a nearby note when the match failed would have
    # crossed from transcription into interpretation.
    claim.notes = table.cell(cells, ROLE_NOTES)"""

ANCHOR_NOTES_S = """        table, line_no, cells, source_cell = hits[0]
        claim.matched_line = line_no"""

REPLACE_NOTES_S = """        table, line_no, cells, source_cell = hits[0]
        claim.matched_line = line_no
        claim.notes = table.cell(cells, ROLE_NOTES)"""

ANCHOR_NOTES_INIT = """        self.route = ''             # SEND BACK / CONVERSATION / ''"""

REPLACE_NOTES_INIT = """        self.route = ''             # SEND BACK / CONVERSATION / ''
        self.notes = ''             # the matched row's Notes, verbatim"""

ANCHOR_REPORT = """    if conversation:
        add('| Where | Value | Worksheet | Row | Finding |')
        add('|---|---|---|---|---|')
        for claim in conversation:
            for layer, code, detail in claim.findings:
                add('| `%s` | %s | `%s` | %s | **%s** -- %s |'
                    % (claim.where, claim.display, claim.worksheet,
                       claim.matched_line or '-', code, detail))"""

REPLACE_REPORT = """    if conversation:
        add('| Where | Value | Worksheet | Row | Finding | '
            'What the checker wrote |')
        add('|---|---|---|---|---|---|')
        for claim in conversation:
            for layer, code, detail in claim.findings:
                add('| `%s` | %s | `%s` | %s | **%s** -- %s | %s |'
                    % (claim.where, claim.display, claim.worksheet,
                       claim.matched_line or '-', code, detail,
                       quoted(claim.notes)))"""

ANCHOR_REPORT_SB = """        for claim in send_back:
            first = claim.findings[0]
            add('| `%s` | %s | %s | `%s` | **%s** -- %s |'
                % (claim.where, claim.display, claim.checker,
                   claim.worksheet, first[1], first[2]))"""

REPLACE_REPORT_SB = """        for claim in send_back:
            first = claim.findings[0]
            add('| `%s` | %s | %s | `%s` | **%s** -- %s | %s |'
                % (claim.where, claim.display, claim.checker,
                   claim.worksheet, first[1], first[2],
                   quoted(claim.notes)))"""

ANCHOR_REPORT_SBH = """        add('| Where | Value | Checker | Worksheet | Finding |')
        add('|---|---|---|---|---|')"""

REPLACE_REPORT_SBH = """        add('| Where | Value | Checker | Worksheet | Finding | '
            'What the checker wrote |')
        add('|---|---|---|---|---|---|')"""


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

    if 'def quoted(' in text:
        print('Already applied. Nothing written.')
        return 0

    # Listed in descending file order so an earlier replacement cannot
    # move a later anchor.
    edits = [
        (ANCHOR_REPORT, REPLACE_REPORT, 'notes column, conversation'),
        (ANCHOR_REPORT_SB, REPLACE_REPORT_SB, 'notes column, send back'),
        (ANCHOR_REPORT_SBH, REPLACE_REPORT_SBH, 'send-back header'),
        (ANCHOR_NOTES_S, REPLACE_NOTES_S, 'capture notes, string path'),
        (ANCHOR_NOTES_C, REPLACE_NOTES_C, 'capture notes, constant path'),
        (ANCHOR_NOTES_INIT, REPLACE_NOTES_INIT, 'notes field'),
        (ANCHOR_UNREADABLE, REPLACE_UNREADABLE, 'unreadable-verdict quote'),
        (ANCHOR_DISPOSE, REPLACE_DISPOSE, 'disposition quoting'),
        (ANCHOR_CLASSIFY, REPLACE_CLASSIFY, 'compound flag and quoting'),
        (ANCHOR_TOKENS, REPLACE_TOKENS, 'registry shrink to seven'),
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
    print('Run test_worksheet_checker.py, then worksheet_checker.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
