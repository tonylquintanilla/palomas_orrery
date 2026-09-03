"""
patch_L279_gallery_assembler_diagnostics.py -- gallery-assembler 1.1 -> 1.2.

Built on palomas_orrery 5b3fb6b439940c17864c9745a71416bc9108ef61 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 4d33c80960595102041de870530ffa8da5bae519.

WHAT IT DOES

  skills/gallery-assembler/SKILL.md
    - version 1.1 -> 1.2
    - `fires_when` widened. "Mode 5 acceptance" reads as accepting
      something FINISHED, which is why it did not fire during a four-hour
      hang investigation on 2026-09-02. It now names the diagnostic case
      in the words Tony would actually use.
    - new section: Mode 5 as MEASUREMENT, not just acceptance. Seven
      rules, every one of them earned by a failure in that session or the
      one before it.
    - new field note: mutating a plot from inside a Plotly event handler.

  LEDGER_CONSOLIDATED.md
    - L-278's Tony-action pointed at gallery-pipeline. It lands here
      instead, so that both halves -- the technical finding and the
      diagnostic discipline -- sit in one skill rather than two. One
      line changes.
    - L-279's open decision is answered and the item is closed.

HOW TO RUN
  Open in VS Code from the ORRERY repo root and press Run. Then run the
  maintenance runner: skills_index.py rebuilds the manifest inside
  PROJECT_INSTRUCTIONS.md, and the row should read 1.2.

  THEN REINSTALL THE SKILL to your account profile (Settings > Skills).
  A running session cannot see a reinstall, so this session cannot
  confirm it. The handoff carries the obligation instead: the next
  session confirms its loaded copy reads 1.2 before gallery work.

GUARDS
  Both files fingerprinted, every anchor verified once before any write,
  all-or-nothing, no .bak. Undo is Discard Changes in GitHub Desktop.

Module created: September 2, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

SKILL = os.path.join('skills', 'gallery-assembler', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

EXPECTED = {
    SKILL:  '931475860c6873715e9e74a6405d1aa8',
    LEDGER: '34aad971a5f880645416411f0ef8d2d6',
}

FIRES_ANCHOR = """fires_when: render_orbits.py, resolver.py, cache_reader.py, propagation math, golden artifact builds, Mode 5 acceptance, orrery/assembler boundary questions
"""

FIRES_NEW = """fires_when: render_orbits.py, resolver.py, cache_reader.py, propagation math, golden artifact builds, Mode 5 acceptance, orrery/assembler boundary questions, AND any time a served page misbehaves and the cause is unknown -- it hangs, it freezes, it is unresponsive, it worked yesterday, a console error appears, or Claude is about to hand Tony a test to run
"""

VERSION_ANCHOR = """Skill version: 1.1 | Cut from gallery @ f83a3abc72c5516e6dc2ad264be53ce95b68cf38 / orrery @ 3398970 | August 5, 2026
"""

VERSION_NEW = """Skill version: 1.2 | Cut from orrery @ 5b3fb6b4 (v1.2),
earlier @ f83a3abc72c5516e6dc2ad264be53ce95b68cf38 (v1.1) | 2026-09-02
v1.2 (L-279) adds Mode 5 as Measurement and the Plotly event-handler
field note, both earned by the 2026-09-02 Sun exhibit hang: eight reads
to attribute a two-line bug, and three wrong readings on the way, every
one of them from inferring the test conditions instead of stating them.
"""

# The file ends WITHOUT a trailing newline, so the anchor must not carry
# one. Caught by the anchor guard on the first throwaway run.
TAIL_ANCHOR = """gate. Don't conflate "the cache is good" with "the render is right":
Pluto/Charon and Moon/Io/Titan are both, as of July 20 2026, in the state of
"data plumbing partially tested, render never attempted." """.rstrip()

TAIL_NEW = '''gate. Don't conflate "the cache is good" with "the render is right":
Pluto/Charon and Moon/Io/Titan are both, as of July 20 2026, in the state of
"data plumbing partially tested, render never attempted."

## Mode 5 as MEASUREMENT, not just acceptance [QUALITY]

The Mode 5 above is ACCEPTANCE: a finished render, does it look right.
This section is the other job Tony's eyes do, and it is a different one.
When a served page misbehaves and neither of us knows why, Tony is not
the judge -- he is the only INSTRUMENT that can observe the failure at
all. Claude cannot open the page, cannot hover it, cannot read its
console. Every trial spends the one resource the project is shortest of,
so a trial that cannot decide anything is worse than no trial.

Seven rules. Each one is here because skipping it cost a round.

**1. State the CONDITIONS, not just the actions.** Every trial names what
is drawn, where the pointer rests, and the exact gesture. A trial that
says only what to click leaves the starting state free, and Tony will
reasonably pick a value that makes the task possible -- emptying the
drawer so the cross markers are visible, for instance. Three readings
were wrong on 2026-09-02 for exactly this, and each was stated
confidently before Tony corrected it.

**2. Start from the FAILING state and subtract.** Trials that start clean
and add cannot separate causes that only appear in a loaded scene. The
first four trials that day all began from a near-empty scene and none of
them could have reproduced the bug.

**3. A diagnostic must not be able to destroy the state it investigates.**
`Plotly.relayout(gd, {hovermode:false})` threw inside Plotly, aborted
partway, and took the scene's `viewInitial` with it -- so the reset
button stopped working and everything after that failed for a reason
that had nothing to do with the bug. Before issuing a console command,
ask what happens if it throws halfway.

**4. Read the reporter's NOTES, not their summary.** "Both hang" and "the
secondary ticks appeared, rotation works, hovertext appears okay, upon
clicking the scene hangs" were in the same message. Only one of them was
the observation. Ticks appearing meant the relayout had COMPLETED, which
reversed the conclusion entirely.

**5. Read stack DEPTH, not only frame names.** `Maximum call stack size
exceeded` on a stack about twenty-five frames deep is not runaway
recursion -- it is a large array applied as function arguments. That tell
was present in the first stack trace and missed twice, and two
hypotheses were chased in the gap.

**6. Confirm the fix LIVE before writing the patch.** A handler can be
replaced from the console in the running page; a relayout can be fired on
a timer. The 2026-09-02 fix was proven that way before a line was
written, which turned a patch-and-see cycle into a patch that was already
known to work.

**7. Every trial names what its outcome RULES OUT.** A trial that only
confirms "yes it still breaks" has bought nothing. If neither outcome
eliminates a candidate, the trial does not go in the list.

The report form asks for the conditions back, not just the verdict --
otherwise rule 1 protects the writing and not the reading.

## Field note: never mutate a plot from inside a Plotly event handler

`Plotly.relayout` called synchronously from `plotly_click` re-enters
Plotly's `layoutReplot` before the click dispatch has returned, and the
page dies with `RangeError: Maximum call stack size exceeded` -- no
rotation, no hover, modebar reset dead, reload the only recovery.

The relayout itself is fine. On 2026-09-02 the identical call completed
cleanly from the console with a tooltip up, with the tooltip dismissed,
and on a timer while the pointer rested on a marker. Only the context
was fatal.

Fix: `setTimeout(fn, 0)` around the mutation, so the dispatch returns
first. Applies to `plotly_click`, `plotly_hover`, `plotly_selected` and
`plotly_relayout` alike.

Two hypotheses died before this one was found, and both are worth
keeping because neither was unreasonable. Hover hit-testing was blamed
first -- `Plotly.Fx.unhover` was tested directly and changed nothing.
Trace size was blamed second, on the ~65,000 argument limit -- the
largest trace in that scene is 4,332 points and the one that hung is 400.

Live example: gallery `6fd6baaf`, `interactive.html`, the `plotly_click`
handler. L-267, L-278.
'''

# --- ledger edits -----------------------------------------------------

L278_ANCHOR = """- Tony-action (do): bump `gallery-pipeline` with this as a field note,
  since it fires on exactly the code that would hit it again.
**Gap:** skill patch not written. The finding lives only here and in
`patch_L267_3`'s comment until it does.
"""

L278_NEW = """- Tony-action: DONE 2026-09-02. Written into `gallery-assembler` 1.2 as
  a field note, not `gallery-pipeline` as first proposed -- L-279 put the
  diagnostic discipline in the same skill, and splitting the technical
  finding from the discipline that found it across two skills is the
  parallel-pipeline anti-pattern in miniature.
"""

L279_ANCHOR = """- Tony-action (decide): where this lands. It is method, so
  Method Belongs to the Skill points at a skill -- but no current skill
  owns diagnostic protocols, and the two readers it protects are the same
  two A Report Names Its Items was written for, which argues for the
  resident protocol instead.
**Gap:** decision, then a patch. Nothing is written anywhere yet.
"""

L279_NEW = """- **DECIDED 2026-09-02, Tony's call: `gallery-assembler`.** Claude had
  proposed an eleventh skill, then extending Mode 5 in the resident
  protocol. Tony pointed at `gallery-assembler`, and its own `fires_when`
  line already said "Mode 5 acceptance" -- the home existed and was not
  used. Claude version-checked that skill on 2026-09-02 and never opened
  it, including at the moment of handing over a patch whose own output
  said "this one needs Mode 5".
- **So the trigger was widened too.** "Mode 5 acceptance" reads as
  accepting something FINISHED, which is why it did not fire while
  chasing a hang. It now names the diagnostic case in the words Tony
  would use: it hangs, it is unresponsive, it worked yesterday.
- **Scope accepted, not solved.** `gallery-assembler` is gallery-side, so
  an orrery-side hang will not reach this section. That is The Braid
  working as intended -- bound it to the current artifact and handle the
  orrery case when there is one.
"""

L279_STATUS_ANCHOR = """<!-- L:279 status:OPEN upd:2026-09-02 section:A flag: rice:3/2/80/1 -->
"""

L279_STATUS_NEW = """<!-- L:279 status:DONE upd:2026-09-02 section:A flag: rice:3/2/80/1 -->
"""


def fail(msg):
    print('')
    print('FAILURE: %s' % msg)
    print('NOTHING was written. No file on disk has changed.')
    print('If a previous run did write, undo is Discard Changes in GitHub Desktop.')
    sys.exit(1)


def read_lf(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return (raw.replace(b'\r\n', b'\n') if was_crlf else raw), was_crlf


EDITS = {
    SKILL: [
        (FIRES_ANCHOR, FIRES_NEW),
        (VERSION_ANCHOR, VERSION_NEW),
        (TAIL_ANCHOR, TAIL_NEW),
    ],
    LEDGER: [
        (L278_ANCHOR, L278_NEW),
        (L279_ANCHOR, L279_NEW),
        (L279_STATUS_ANCHOR, L279_STATUS_NEW),
    ],
}


def main():
    print('patch_L279 -- gallery-assembler 1.1 -> 1.2, diagnostics section')
    print('=' * 64)

    for fn, pairs in EDITS.items():
        for _, new in pairs:
            try:
                new.encode('ascii')
            except UnicodeEncodeError as exc:
                fail('non-ASCII in replacement text for %s: %s' % (fn, exc))

    staged = {}
    for fn, pairs in EDITS.items():
        if not os.path.exists(fn):
            fail('%s not found. Run this from the ORRERY repo root.' % fn)

        content, was_crlf = read_lf(fn)
        actual = hashlib.md5(content).hexdigest()
        if actual != EXPECTED[fn]:
            fail('BASE MOVED for %s.\n  expected %s\n  found    %s\n'
                 '  Built against orrery 5b3fb6b4. A size delta of about one\n'
                 '  byte per line is CRLF, not content.'
                 % (fn, EXPECTED[fn], actual))
        print('  %-38s fingerprint matches%s'
              % (fn, ' [CRLF]' if was_crlf else ''))

        out = content
        for anchor, new in pairs:
            a = anchor.encode('ascii')
            n = out.count(a)
            if n != 1:
                fail('anchor matched %d times (expected 1) in %s:\n    %r'
                     % (n, fn, anchor.strip()[:80]))
            out = out.replace(a, new.encode('ascii'))
        staged[fn] = (out.replace(b'\n', b'\r\n') if was_crlf else out, len(pairs))

    print('  all %d anchors verified'
          % sum(v[1] for v in staged.values()))

    for fn, (data, n_edits) in staged.items():
        with open(fn, 'wb') as f:
            f.write(data)
        print('  wrote %-38s %d edits' % (fn, n_edits))

    # --- Post-conditions, read back from disk -------------------------
    print('')
    print('Post-conditions (read back from disk):')
    skill = read_lf(SKILL)[0].decode('utf-8', 'replace')
    ledger = read_lf(LEDGER)[0].decode('utf-8', 'replace')

    ok = True
    for label, text, needle, want in [
        ('version reads 1.2',      skill,  'Skill version: 1.2 |', True),
        ('version 1.1 line gone',  skill,  'Skill version: 1.1 |', False),
        ('measurement section',    skill,  '## Mode 5 as MEASUREMENT', True),
        ('plotly field note',      skill,  '## Field note: never mutate a plot', True),
        ('trigger widened',        skill,  'a served page misbehaves and the cause is unknown', True),
        ('seven rules present',    skill,  '**7. Every trial names what its outcome RULES OUT.**', True),
        ('L-278 action redirected', ledger, 'Written into `gallery-assembler` 1.2', True),
        ('L-278 old action gone',  ledger, 'bump `gallery-pipeline` with this as a field note', False),
        ('L-279 decided',          ledger, "**DECIDED 2026-09-02, Tony's call: `gallery-assembler`.**", True),
        ('L-279 status DONE',      ledger, '<!-- L:279 status:DONE', True),
        ('L-279 status OPEN gone', ledger, '<!-- L:279 status:OPEN', False),
    ]:
        hit = needle in text
        print('  %-24s %s' % (label, hit == want))
        if hit != want:
            ok = False

    # All seven numbered rules must be present, not just the first and last.
    rules = sum(1 for i in range(1, 8) if ('**%d. ' % i) in skill)
    print('  %-24s %d (want 7)' % ('numbered rules', rules))
    if rules != 7:
        ok = False

    if not ok:
        print('')
        print('POST-CONDITION FAILED. Undo is Discard Changes in GitHub Desktop.')
        sys.exit(1)

    print('')
    print('DONE. gallery-assembler is 1.2 in the REPO.')
    print('')
    print('Two things left, and the second cannot be done from here:')
    print('  1. Run the maintenance runner. skills_index.py rebuilds the')
    print('     manifest in PROJECT_INSTRUCTIONS.md; the row should read 1.2.')
    print('  2. REINSTALL the skill to your account (Settings > Skills).')
    print('     That is the copy Claude actually loads, and a running')
    print('     session cannot see the reinstall. The handoff carries the')
    print('     obligation: the next session confirms its loaded copy reads')
    print('     1.2 before doing gallery work.')


if __name__ == '__main__':
    main()
