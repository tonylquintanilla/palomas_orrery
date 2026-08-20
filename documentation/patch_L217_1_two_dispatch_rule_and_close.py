"""Ledger + skill patch -- L-217 closed, provenance-discipline 2.5 -> 2.6.

RUN COMMAND:  python patch_L217_1_two_dispatch_rule_and_close.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md and skills/), open it in VS Code, and click Run.

Built on f603be381d447137a45f59310157391d2ce2ad9a at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES -- two files, all-or-nothing across both.
  Edit 1 -- adds The Two-Dispatch Rule to provenance-discipline, under
            Model Roles in the Competitive Pattern.
  Edit 2 -- bumps that skill 2.5 -> 2.6.
  Edit 3 -- removes the OPEN L-217 block from section A.
  Edit 4 -- inserts the CLOSED L-217 block at the head of section C.

PURE ADDITION CHECK
  Every line of skill 2.5 must still be present in 2.6, the version
  line excepted. A bump that removes anything aborts.

AFTER IT RUNS
  1. Run ledger_index.py the same way, to rebuild the index tables.
  2. Run skills_index.py the same way, to rebuild the Skill Manifest.
  3. (do) Reinstall provenance-discipline at Settings > Skills.
     The NEXT session confirms its loaded copy reads 2.6 before doing
     provenance work. That obligation is in the handoff, not cleared
     here.

WHAT IS PERMANENT
  The script is disposable; the skill section and the closed ledger
  block are not. Archive this file to documentation/ once it has run.

SUCCESS   one 'ok' line per edit, 'pure addition confirmed', then
          'patch applied'.
FAILURE   a single 'ERROR:' or 'ANCHOR FAIL' line; NEITHER file is
          written -- both are staged in memory and committed together.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    SKILL: '64c733ba8026b0a8b7852d3b1e8a330e',
    LEDGER: '88cb9b0c8f0c50c002c08da412217fea',
}

RULE_OLD = b"""### Worksheet Types
"""

RULE_NEW = b"""### The Two-Dispatch Rule [CRITICAL]

When a prompt carries Claude's own proposal AND asks the reviewer for an
independent derivation, the two halves go out as TWO PHYSICAL
DISPATCHES: Part A alone, answer collected, then Part B. A single
document that instructs a model to answer one half before reading the
other is a check that cannot fail -- both halves arrive in one context,
the model cannot comply, and nothing in any answer distinguishes a
reviewer who complied from one who could not.

Stating the instruction anyway is WORSE than omitting it, because the
instruction makes the prompt look controlled. If two dispatches are not
worth the round trip, drop the claim and ask only for critique.

(Origin, L-217, 2026-08-19. The L-214 review prompt asked both legs for
Part A before Part B. Fable disclosed that the ordering was unexecutable
and named it as a check that cannot fail. GPT's answer corroborated it
without meaning to: its Part A opens "my prediction before consulting
the measured result is" and then states the measured result to the
digit. The prompt was authored in the session that dispatched it, so the
resident CRITICAL gate never fired on its own author.)

### Worksheet Types
"""

VERSION_OLD = b"""Skill version: 2.5 | Cut from palomas_orrery @ 731066f (v2.5), earlier
@ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)
| August 18, 2026
"""

VERSION_NEW = b"""Skill version: 2.6 | Cut from palomas_orrery @ f603be3 (v2.6), earlier
@ 731066f (v2.5), @ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0),
@ cdcdb4b (v1.9) | August 19, 2026
v2.6 adds The Two-Dispatch Rule [CRITICAL] under Model Roles in the
Competitive Pattern -- L-217, after a Mode 7 review prompt asked two
model legs to answer Part A before reading Part B, which neither could
do and neither answer could be distinguished on.
"""

L217_OLD = b'#### [L-217] The Part A / Part B dispatch split is a check that cannot fail\n<!-- L:217 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/90/1 -->\n- **Found by the reviewer it was meant to constrain, 2026-08-19.** The\n  L-214 review prompt asked each model leg to answer Part A (derive\n  your own structure) BEFORE reading Part B (critique ours), to stop\n  the reviewer anchoring on Claude\'s proposal. Fable\'s disclosure: the\n  prompt arrives as ONE document in ONE context, so there is no way for\n  a model to write Part A without Part B already read, and NOTHING IN\n  ANY ANSWER DISTINGUISHES A REVIEWER WHO COMPLIED FROM ONE WHO COULD\n  NOT.\n- **The corroboration is in the other leg.** GPT\'s A3 opens with "my\n  prediction before consulting the measured result is" and then states\n  the measured result to the digit. That is the tell. It is not GPT\'s\n  fault -- the instruction asked for something the format made\n  impossible.\n- **This is an instance of the protocol\'s own CRITICAL gate**, A Check\n  That Cannot Fail Is Not Passing, in the dispatch layer rather than in\n  code. The prompt was authored in this session, so the gate did not\n  fire on its own author.\n- **Fable\'s remedy:** two physical dispatches. Part A sent alone,\n  answer collected, THEN Part B sent. Anything less is the ritual\n  without the check.\n- **The related contamination finding, same review.** Fable ran INSIDE\n  the Paloma\'s Orrery project and disclosed it unprompted: it carried\n  resident memory of the protocol and the general state of the\n  provenance work, though not the L-214 design conversation. The\n  fresh-chat-outside-any-project rule exists for exactly this and was\n  not followed for that leg. Its review was still the sharper of the\n  two, which is worth noting and is not a reason to relax the rule.\n**Note:** RICE is Claude\'s proposal, unratified.\n**Gap:** decide whether the two-dispatch protocol becomes standing\npractice for any prompt carrying Claude\'s own proposal, and if so\nrecord it in `provenance-discipline` or\n`ledger-and-session-records` -- whichever fires at dispatch time.\n**Tony-action (decide):** which skill hosts it, or whether a\none-document prompt simply stops claiming the split.\n**Ref:** `documentation/REVIEW_PROMPT_L214_20260819.md` (the prompt\nthat carried the defect); `documentation/L214_REVIEW_RECONCILIATION_\n20260819.md` Part 4; L-214; L-203 (the Visibility Convention, same\nfamily of reasoning).\n\n'

L217_NEW = b'#### [L-217] The Part A / Part B dispatch split is a check that cannot fail\n<!-- L:217 status:DONE upd:2026-08-19 section:C flag: rice:3/3/90/1 -->\n- **Found by the reviewer it was meant to constrain, 2026-08-19.** The\n  L-214 review prompt asked each model leg to answer Part A (derive\n  your own structure) BEFORE reading Part B (critique ours), to stop\n  the reviewer anchoring on Claude\'s proposal. Fable\'s disclosure: the\n  prompt arrives as ONE document in ONE context, so there is no way for\n  a model to write Part A without Part B already read, and NOTHING IN\n  ANY ANSWER DISTINGUISHES A REVIEWER WHO COMPLIED FROM ONE WHO COULD\n  NOT.\n- **The corroboration is in the other leg.** GPT\'s A3 opens with "my\n  prediction before consulting the measured result is" and then states\n  the measured result to the digit. That is the tell. It is not GPT\'s\n  fault -- the instruction asked for something the format made\n  impossible.\n- **This is an instance of the protocol\'s own CRITICAL gate**, A Check\n  That Cannot Fail Is Not Passing, in the dispatch layer rather than in\n  code. The prompt was authored in this session, so the gate did not\n  fire on its own author.\n- **Fable\'s remedy:** two physical dispatches. Part A sent alone,\n  answer collected, THEN Part B sent. Anything less is the ritual\n  without the check.\n- **The related contamination finding, same review.** Fable ran INSIDE\n  the Paloma\'s Orrery project and disclosed it unprompted: it carried\n  resident memory of the protocol and the general state of the\n  provenance work, though not the L-214 design conversation. The\n  fresh-chat-outside-any-project rule exists for exactly this and was\n  not followed for that leg. Its review was still the sharper of the\n  two, which is worth noting and is not a reason to relax the rule.\n**Note:** RICE is Claude\'s proposal, unratified.\n- **CLOSED 2026-08-19. Tony\'s ruling: yes, do it.** The two-dispatch\n  protocol is standing practice for any prompt that carries Claude\'s own\n  proposal alongside a request for an independent derivation. Recorded\n  in `provenance-discipline` 2.6, under Model Roles in the Competitive\n  Pattern, which is the section that already owns Mode 7 dispatch\n  mechanics and the skill that fires at dispatch time. The alternative\n  host, `ledger-and-session-records`, owns document FORMAT (the anchor\n  line, handoff shape); this is dispatch SEQUENCE, so it belongs beside\n  the model-roles table.\n- **What the rule says.** Either send Part A alone, collect the answer,\n  and then send Part B -- or do not claim the split. A single document\n  asking a model to answer one half before reading the other is a check\n  that cannot fail, and stating the instruction is worse than omitting\n  it, because the instruction makes the prompt look controlled.\n- **The obligation this creates.** A mid-session reinstall cannot be\n  verified from inside the session that makes it, so the NEXT session\n  confirms its own loaded copy reads 2.6 before doing provenance work.\n**Ref:** `documentation/REVIEW_PROMPT_L214_20260819.md` (the prompt\nthat carried the defect); `documentation/L214_REVIEW_RECONCILIATION_\n20260819.md` Part 4; L-214; L-203 (the Visibility Convention, same\nfamily of reasoning).\n\n'

SECTION_C_OLD = b"""## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)
"""

SECTION_C_NEW = (b"""## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

""" + L217_NEW.rstrip(b'\n') + b"""
""")

EDITS = [
    (SKILL, 'two-dispatch rule added', RULE_OLD, RULE_NEW),
    (SKILL, 'skill version 2.5 -> 2.6', VERSION_OLD, VERSION_NEW),
    (LEDGER, 'L-217 removed from section A', L217_OLD, b''),
    (LEDGER, 'L-217 inserted into section C', SECTION_C_OLD, SECTION_C_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    blobs = {}
    crlf = {}

    for name in (SKILL, LEDGER):
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print('ERROR: %s not found under this script.' % name)
            print('       Save the script into the repo root.')
            return 1
        with open(path, 'rb') as handle:
            data = handle.read()
        fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if fp != FINGERPRINTS[name]:
            print('ERROR: BASE MOVED for %s' % name)
            print('       expected %s, found %s'
                  % (FINGERPRINTS[name], fp))
            print('       Nothing written to either file.')
            return 1
        blobs[name] = data
        crlf[name] = data.count(b'\r\n') > 0
        print('base %-44s %s  %s'
              % (name, fp, 'CRLF' if crlf[name] else 'LF'))

    original_skill = blobs[SKILL]

    for name, label, old, new in EDITS:
        o, n = old, new
        if crlf[name]:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = blobs[name].count(o)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, found %d'
                  % (label, count))
            print('             Nothing written to either file.')
            return 1
        blobs[name] = blobs[name].replace(o, n)
        print('ok  %s' % label)

    before = original_skill.replace(b'\r\n', b'\n').split(b'\n')
    after = set(blobs[SKILL].replace(b'\r\n', b'\n').split(b'\n'))
    missing = [x for x in before
               if x.strip() and x not in after
               and not x.startswith(b'Skill version: 2.5')
               and not x.startswith(b'@ 6b99ace')
               and not x.startswith(b'| August 18, 2026')]
    if missing:
        print('ERROR: NOT A PURE ADDITION. %d line(s) from 2.5 are gone:'
              % len(missing))
        for x in missing[:10]:
            print('       %s' % x.decode('ascii', 'replace')[:70])
        print('       Nothing written to either file.')
        return 1
    print('pure addition confirmed (%d skill lines checked)' % len(before))

    if blobs[LEDGER].count(b'#### [L-217]') != 1:
        print('ANCHOR FAIL: L-217 appears %d times after the move, '
              'expected 1' % blobs[LEDGER].count(b'#### [L-217]'))
        print('             Nothing written to either file.')
        return 1
    if b'status:OPEN upd:2026-08-19 section:A flag: rice:3/3/90/1' \
            in blobs[LEDGER] and blobs[LEDGER].count(
                b'L:217 status:DONE') != 1:
        print('ANCHOR FAIL: L-217 metadata did not flip to DONE.')
        return 1

    for name in (SKILL, LEDGER):
        with open(os.path.join(here, name), 'wb') as handle:
            handle.write(blobs[name])
    print('patch applied (%d + %d bytes)'
          % (len(blobs[SKILL]), len(blobs[LEDGER])))
    print('')
    print('NEXT: 1. run ledger_index.py')
    print('      2. run skills_index.py')
    print('      3. reinstall provenance-discipline at Settings > Skills')
    return 0


if __name__ == '__main__':
    sys.exit(main())
