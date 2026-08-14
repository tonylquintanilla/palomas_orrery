"""patch_L192_tests.py -- tests follow the vocabulary ruling.

RUN COMMAND
-----------
Put this file in the repo root, open it in VS Code, and click Run.

    python patch_L192_tests.py

Run it after patch_L192_vocabulary.py. Archive to documentation/ after.

WHAT IT CHANGES
---------------
Two tests asserted that WRONG CITATION and WRONG VALUE classify with a
scope. The 2026-08-13 ruling removed both tokens, so those tests now
fail -- correctly. They are replaced by tests asserting the new rule:
a token outside the seven is UNREADABLE and goes back.

Four tests are added for behaviour that did not exist before: that a
compound cell is detected, that a quote is delimited, that a long quote
is cut with a visible marker, and that UNSOURCED survives as a citation
token while NOT FOUND does not.

The suite goes from 46 checks to 50.
"""

import hashlib
import os
import sys

TARGET = 'test_worksheet_checker.py'

ANCHOR = """    # The whole reason tokens carry a scope. Read as a bare "wrong",
    # this would report a refuted VALUE for a row that says the value
    # may be perfectly right under a different authority.
    own, _tok, scope = wc.classify_verdict('**WRONG CITATION**',
                                           wc.SCOPE_VALUE)
    check('WRONG CITATION is scoped to the citation',
          own == wc.V_REFUTED and scope == wc.SCOPE_CITATION,
          '%s / %s' % (own, scope))

    own, _tok, scope = wc.classify_verdict('**WRONG VALUE**',
                                           wc.SCOPE_CITATION)
    check('WRONG VALUE is scoped to the value',
          own == wc.V_REFUTED and scope == wc.SCOPE_VALUE,
          '%s / %s' % (own, scope))"""

REPLACE = """    # The 2026-08-13 ruling: seven tokens, and a word outside them goes
    # back rather than being translated. WRONG CITATION and WRONG VALUE
    # were invented at the keyboard -- they exist only because a
    # worksheet had one verdict column, and the two-column schema says
    # which one is wrong without a compound word for it.
    own, _tok, _s = wc.classify_verdict('**WRONG CITATION**',
                                        wc.SCOPE_VALUE)
    check('an invented token is UNREADABLE, not translated',
          own == wc.V_UNREADABLE, own)

    own, _tok, _s = wc.classify_verdict('**NOT FOUND**', wc.SCOPE_CITATION)
    check('NOT FOUND is UNREADABLE -- no prompt ever asked for it',
          own == wc.V_UNREADABLE, own)

    # UNSOURCED is the one survivor beyond the six: the tier2 prompt
    # commissioned it by name and ten cells on disk use it.
    own, _tok, scope = wc.classify_verdict('**UNSOURCED**',
                                           wc.SCOPE_VALUE)
    check('UNSOURCED survives, scoped to the citation',
          own == wc.V_SOURCE_ABSENT and scope == wc.SCOPE_CITATION,
          '%s / %s' % (own, scope))

    # A qualification must not be trimmed away in silence.
    check('a token plus prose is flagged compound',
          wc.is_compound('**YES** -- fully confirmed at 3 dp'))
    check('a bare token is not compound',
          not wc.is_compound('**YES**'))

    # Quoting is transcription, and transcription that fuses with the
    # tool's own words is not transcription. A live finding once read
    # "reads NO -- wrong authority -- wrong authority for a value that
    # may still be right" with no way to tell evidence from template.
    quote = wc.quoted('NO -- wrong authority')
    check('a quoted cell is delimited from the tool text',
          quote.startswith('<<') and quote.endswith('>>'), quote)

    long_quote = wc.quoted('x' * (wc.QUOTE_LIMIT + 40))
    check('a long quote is cut with a visible marker',
          '[...]' in long_quote and len(long_quote) < wc.QUOTE_LIMIT + 40,
          len(long_quote))"""


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

    if 'is flagged compound' in text:
        print('Already applied. Nothing written.')
        return 0

    if text.count(ANCHOR) != 1:
        print('STOP: anchor appears %d times, expected once. Nothing '
              'written.' % text.count(ANCHOR))
        return 1

    text = text.replace(ANCHOR, REPLACE, 1)
    print('ok  vocabulary tests follow the ruling')

    with open(TARGET, 'w', encoding='utf-8', newline='\n') as handle:
        handle.write(text)

    after = read(TARGET)
    print('%s: %d bytes, md5 %s'
          % (TARGET, len(after), hashlib.md5(after).hexdigest()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
