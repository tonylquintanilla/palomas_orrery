"""Skill + ledger patch -- safe-file-editing 1.5 -> 1.6. Stamp What You
Change generalised to every file type, not just .py. L-219 rebased to
1.7.

RUN COMMAND:  python patch_L220_2_stamp_all_file_types.py

Save this file into the REPO ROOT (the folder holding
LEDGER_CONSOLIDATED.md and skills/), open it in VS Code, and click Run.

Built on ef3bd13d8582865bec47e6da1d862b28ab745bb6 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES -- two files, all-or-nothing across both.
  Edit 1 -- rewrites the opening of Stamp What You Change so it names
            the currency block for each file type, and carries Tony's
            reason for the rule.
  Edit 2 -- bumps the skill 1.5 -> 1.6 (its own stamp).
  Edit 3 -- records the amendment and the error that prompted it in
            L-220.
  Edit 4 -- rebases L-219's target from 1.6 to 1.7.

WHY 1.6 SO SOON AFTER 1.5
  Tony's ruling: the next session should already hold this discipline
  rather than inherit it as an obligation. The rule's founding case was
  stale .md master-plan headers, and as written in 1.5 its only concrete
  example was a Python module docstring -- so it would not have fired on
  the files it was invented for.

PURE ADDITION CHECK
  Every line of 1.5 must still be present in 1.6, the version block and
  the rewritten opening paragraph excepted. Anything else missing
  aborts.

AFTER IT RUNS
  1. Run ledger_index.py the same way.
  2. Run skills_index.py the same way.
  3. (do) Reinstall safe-file-editing at Settings > Skills. This
     REPLACES the 1.5 obligation in the handoff; the next session
     confirms 1.6, not 1.5.

WHAT IS PERMANENT
  The script is disposable; the skill section and the ledger lines are
  not. Archive this file to documentation/ once it has run.

SUCCESS   one 'ok' line per edit, 'pure addition confirmed', then
          'patch applied'.
FAILURE   a single 'ERROR:' or 'ANCHOR FAIL' line; NEITHER file is
          written.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'safe-file-editing', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    SKILL: '3b8e75b722d53f33582ec53df98ca236',
    LEDGER: '1eb748f17d6b4deed1733afc2e39ad00',
}

OPENING_OLD = b"""A patch that edits a file also updates that file's own currency block,
in the SAME transaction as the body. Whichever of these the file
carries: the version line, the anchor SHA, the history or changelog
paragraph, the date, and -- where the change alters what the file DOES
-- the module description at the top.
"""

OPENING_NEW = b"""A patch that edits a file also updates that file's own currency block,
in the SAME transaction as the body. THIS APPLIES TO EVERY FILE TYPE.
Markdown is not an exception -- it is where the rule was earned.

The currency block is whatever the file carries to say what it is and
when it was last true:

| File | Currency block |
|---|---|
| `.py` module | docstring: the `Module updated: <date> with <model>` line, and the description of what the module does |
| `SKILL.md` | the `Skill version:` line, its cut-from SHA list, the date, and the `vN.M adds...` paragraph |
| plan, handoff, review prompt, manifest | the `Built on <SHA> at <URL>` line and the status or "last updated" line |
| the protocol | its header anchor and version |
| ledger, atlas, any generated file | the header stamp, where one exists and is hand-maintained |

Where the change alters what the file DOES, the description at the top
moves with it -- a module docstring and a master plan's status line do
the same job and go stale the same way.

**Why this is worth the bump it costs** (Tony, 2026-08-20): the
documentation is what keeps the conversation targeted, clear and
trackable. Every session starts cold and reads these headers to work out
what it is looking at. A stale one does not merely misinform -- it costs
the next session the orientation the document exists to give, and the
error compounds because the next session writes its own documents on top
of that misreading.
"""

VERSION_OLD = b"""Skill version: 1.5 | Cut from palomas_orrery @ 50438c6 (v1.5), earlier @
a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2), bdaaa0c (v1.1)
| August 20, 2026, with Anthropic's Claude Opus 5
"""

VERSION_NEW = b"""Skill version: 1.6 | Cut from palomas_orrery @ ef3bd13 (v1.6), earlier @
50438c6 (v1.5), a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2),
bdaaa0c (v1.1) | August 20, 2026, with Anthropic's Claude Opus 5
"""

HISTORY_OLD = b"""following alone. v1.5 adds Stamp What You Change (L-220), after Tony
observed that this project updates bodies more reliably than it updates
anchors, dates and module descriptions.
"""

HISTORY_NEW = b"""following alone. v1.5 adds Stamp What You Change (L-220), after Tony
observed that this project updates bodies more reliably than it updates
anchors, dates and module descriptions. v1.6 generalises that section to
every file type, because 1.5's only concrete example was a Python module
docstring and the rule's founding case was stale Markdown headers -- it
would not have fired on the files it was written for.
"""

L220_OLD = b"""  happens it earns a field note then.
**Note:** RICE is Claude's proposal, unratified.
"""

L220_NEW = b"""  happens it earns a field note then.
- **AMENDED 2026-08-20 in `safe-file-editing` 1.6, same day, on Tony's
  question: "shouldn't the anchoring etc apply to md files too, not just
  py files?"** It should, and 1.5 would not have made a reader think so.
  Its opening sentence was file-agnostic but its only concrete example
  was a Python module docstring, and the skill's own description says
  "especially .py" -- so the rule covered Markdown in principle and
  would not have fired on it in practice, which is the prose form of a
  check that cannot fail. 1.6 names the currency block for each file
  type in a table and says outright that Markdown is where the rule was
  earned.
- **The error that proved it, and it was in the patch that introduced
  the rule.** `patch_L220_1` printed "LEDGER_CONSOLIDATED.md -- no
  currency block of its own." False. The ledger header carries `Module
  updated: June 2026 with Anthropic's Claude Sonnet 4.6, Opus 4.8 +
  Claude Fable 5`, a Consolidated date, and Tony's own RICE review line.
  Claude asserted an absence without looking -- the same shape as the
  truncated-grep false absence in the 2026-08-19 handoff, error 2. The
  ledger's stamp still reads June while the file was edited four times
  on 2026-08-20; whether a nightly-regenerated file should carry a
  hand-maintained stamp at all is left for whoever next touches that
  header.
- **Tony's reason for doing it immediately rather than folding it into
  the next bump.** "The documentation is what keeps our conversation
  targeted, clear and trackable." Recorded in the skill section itself,
  because a rule whose cost is visible and whose reason is not gets
  quietly dropped.
**Note:** RICE is Claude's proposal, unratified.
"""

L219_OLD = b"""which would be 1.6 -- 1.5 is taken by L-220.
"""

L219_NEW = b"""which would be 1.7 -- 1.5 and 1.6 are taken by L-220.
"""

EDITS = [
    (SKILL, 'Stamp What You Change generalised to all file types',
     OPENING_OLD, OPENING_NEW),
    (SKILL, 'skill version 1.5 -> 1.6 (its own stamp)',
     VERSION_OLD, VERSION_NEW),
    (SKILL, 'history paragraph extended', HISTORY_OLD, HISTORY_NEW),
    (LEDGER, 'L-220 amendment recorded', L220_OLD, L220_NEW),
    (LEDGER, 'L-219 rebased to 1.7', L219_OLD, L219_NEW),
]

STAMPS_UPDATED = [
    'skills/safe-file-editing/SKILL.md -- version 1.5 -> 1.6, cut-from '
    'SHA re-pinned to ef3bd13, history paragraph, date, model '
    'attribution',
    'LEDGER_CONSOLIDATED.md -- header stamp NOT touched: this patch does '
    'not change what the ledger is, only its contents, and the stamp '
    'question is recorded in L-220 for whoever next edits that header',
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
            print('       expected %s, found %s' % (FINGERPRINTS[name], fp))
            print('       Nothing written to either file.')
            return 1
        blobs[name] = data
        crlf[name] = data.count(b'\r\n') > 0
        print('base %-40s %s  %s'
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
    expected_gone = (
        b'Skill version: 1.5', b'a872205 (v1.4), 1ba20c3 (v1.3),',
        b'| August 20, 2026, with', b'A patch that edits a file also',
        b'in the SAME transaction as the body. Whichever',
        b'carries: the version line, the anchor SHA,',
        b'paragraph, the date, and -- where the change',
        b'-- the module description at the top.',
        b'observed that this project updates bodies',
        b'anchors, dates and module descriptions.',
    )
    missing = [x for x in before
               if x.strip() and x not in after
               and not any(x.startswith(g) for g in expected_gone)]
    if missing:
        print('ERROR: NOT A PURE ADDITION. %d unexpected line(s) gone:'
              % len(missing))
        for x in missing[:10]:
            print('       %s' % x.decode('ascii', 'replace')[:70])
        print('       Nothing written to either file.')
        return 1
    print('pure addition confirmed (%d skill lines checked)' % len(before))

    for name in (SKILL, LEDGER):
        with open(os.path.join(here, name), 'wb') as handle:
            handle.write(blobs[name])
    print('patch applied (%d + %d bytes)'
          % (len(blobs[SKILL]), len(blobs[LEDGER])))
    print('')
    print('STAMPS UPDATED BY THIS PATCH (per Stamp What You Change):')
    for line in STAMPS_UPDATED:
        print('  %s' % line)
    print('')
    print('NEXT: 1. run ledger_index.py')
    print('      2. run skills_index.py')
    print('      3. reinstall safe-file-editing at Settings > Skills')
    print('         -- the next session confirms 1.6, not 1.5.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
