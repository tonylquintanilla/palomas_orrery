"""patch_L191_1_survey_scope_correction.py

Built on 94ff80f2136ce8458653dca7d6244028e5e246b0 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 24, 2026 with Anthropic's Claude Opus 5.

WHAT THIS IS

A LEDGER patch. It changes no code and does not begin the sweep.
L-191's standing ruling is survey before sweep; the survey has now
happened and two of the item's own measurements turn out to be wrong.
This records that.

WHAT WAS WRONG

L-191 said 20 affected strings, all in solar_visualization_shells.py,
and separately that gas giant shells have NO tooltips at all. Both came
from resolving the tooltip names that appear beside a CreateToolTip
call in source.

Thirty-nine tooltip strings never appear beside that call.
`build_shell_checkboxes()` in celestial_objects.py assembles the name at
run time --

    tooltip_name = f"{body_prefix}_{shell['var_suffix']}_info"

-- from SHELL_DEFINITIONS, and looks it up in a dict the call site
passes as `globals()`. So the name exists only as a formatted string
during execution. A survey reading source finds nothing there and
records zero, which is exactly what the "no tooltips at all" bullet
did. Jupiter alone accounts for ten.

MEASURED TWICE, INDEPENDENTLY

Claude Fable 5 surveyed at `e1c64dc9` on 2026-08-21 and reported 58.
Claude Opus 5 reproduced the count at `94ff80f2` on 2026-08-24, from
the tree as it stands after two further days of work, and also got 58:
39 through the runtime path, 19 in solar.

The reproduction failed on its FIRST attempt and returned 53, because
it resolved strings with ast.literal_eval and skipped four solar
assignments built as f-strings or concatenations -- silently, with a
bare `continue`. Re-measuring from raw source slices instead of
evaluated values reproduced 58. That is the third instance of this
item's own lesson: a proxy for the thing is not the thing, and the
proxy that cannot report what it skipped is the dangerous kind.

STILL OWED, AND SAID SO IN THE TEXT

Two static analyses agreeing is still two static analyses. The render
confirmation -- hover a Jupiter shell checkbox and look for a literal
`<br>` -- has not happened. The patch records 58 as MEASURED, names the
confirmation as outstanding, and does not write it as settled.

WHAT IT DOES
  1. Rewrites the SCOPE bullet: 20 -> 58, with the breakdown by body.
  2. Rewrites the gas-giant bullet, which had the sign inverted.
  3. Adds the runtime-globals mechanism as its own bullet, since it is
     the reason two surveys missed the same 39 strings.
  4. Adds the divergence measurement: 41 of 52 inline hover_text copies
     in shell_configs.py have drifted from their module twin.
  5. Extends the Gap to the corrected scope and names the render check.
  6. Ledger header currency stamp.

AFTER RUNNING
  python ledger_index.py
  Re-run the maintenance runner.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '94ff80f2136ce8458653dca7d6244028e5e246b0'
LEDGER = 'LEDGER_CONSOLIDATED.md'
FINGERPRINT_LF = '4e2843500a9867b2171caa7062907230'

# ------------------------------------------------------------------
# 1 -- the SCOPE bullet
# ------------------------------------------------------------------

SCOPE_OLD = (
    "- **SCOPE, corrected twice.** A first estimate of \"772 lines across 17\n"
    "  files\" was WRONG -- it counted every line in that commit gaining a\n"
    "  `<br>`, which sweeps in the `_info_hover` strings where `<br>` is\n"
    "  correct. Resolving every name bound to `CreateToolTip` back to its\n"
    "  definition gives the real figure: **20 affected strings, all in\n"
    "  `solar_visualization_shells.py`.** Earth (11 tooltip strings) and\n"
    "  asteroid belt (4) are clean. Grep counted a proxy; the render\n"
    "  counted the surface.\n"
)

SCOPE_NEW = (
    "- **SCOPE, corrected three times, and the third correction is the\n"
    "  large one.** A first estimate of \"772 lines across 17 files\" was\n"
    "  WRONG -- it counted every line in the May commit gaining a `<br>`,\n"
    "  which sweeps in the `_info_hover` strings where `<br>` is correct.\n"
    "  Resolving every name bound to `CreateToolTip` back to its\n"
    "  definition then gave 20 affected strings, all in\n"
    "  `solar_visualization_shells.py`. **That figure was also wrong, and\n"
    "  low by more than half. The measured scope is 58 strings across six\n"
    "  bodies** (2026-08-21 survey, reproduced 2026-08-24):\n"
    "\n"
    "  | Source | Strings |\n"
    "  |---|---|\n"
    "  | `solar_visualization_shells.py` (direct call sites) | 19 |\n"
    "  | Jupiter | 10 |\n"
    "  | Saturn | 10 |\n"
    "  | Uranus | 8 |\n"
    "  | Neptune | 8 |\n"
    "  | Planet 9 | 2 |\n"
    "  | Moon | 1 |\n"
    "  | **Total** | **58** |\n"
    "\n"
    "  Earth (11 tooltip strings) and asteroid belt (4) remain clean.\n"
    "  Grep counted a proxy; the render counted the surface -- and the\n"
    "  20 was a third proxy, better than grep and still not the surface.\n"
    "- **MEASURED TWICE, BY TWO MODELS, AND STILL NOT CONFIRMED.** Claude\n"
    "  Fable 5 surveyed at `e1c64dc9` on 2026-08-21 and returned 58. The\n"
    "  count was withheld from that request on purpose so the answer could\n"
    "  disagree with the ledger, and it did. Claude Opus 5 reproduced it\n"
    "  at `94ff80f2` on 2026-08-24 against a tree two days further on, and\n"
    "  also got 58. **Two static analyses agreeing is still two static\n"
    "  analyses.** The render check is owed: hover a Jupiter shell\n"
    "  checkbox and look for a literal `<br>`. Until that happens, 58 is\n"
    "  measured and not confirmed, and this bullet says so rather than\n"
    "  letting agreement stand in for a look.\n"
    "- **The reproduction failed on its first attempt, which is worth\n"
    "  recording because it is this item's own lesson a third time.** It\n"
    "  returned 53. It resolved each string with `ast.literal_eval` and\n"
    "  skipped whatever could not be evaluated -- four solar assignments\n"
    "  built as f-strings or concatenations -- silently, with a bare\n"
    "  `continue` and no report. Re-measuring from raw source SLICES\n"
    "  rather than evaluated VALUES gave 19 solar and reproduced 58. A\n"
    "  proxy that cannot say what it skipped is the dangerous kind.\n"
)

# ------------------------------------------------------------------
# 2 -- the mechanism, as its own bullet
# ------------------------------------------------------------------

MECH_ANCHOR = (
    "- **FOUR PATTERNS EXIST for the same job.** This is the actual finding.\n"
)

MECH_NEW = (
    "- **WHY TWO SURVEYS MISSED THE SAME 39 STRINGS.** They are never\n"
    "  named beside a `CreateToolTip` call. `build_shell_checkboxes()` in\n"
    "  `celestial_objects.py` builds the name at RUN TIME from\n"
    "  `SHELL_DEFINITIONS`,\n"
    "\n"
    "      tooltip_name = f\"{body_prefix}_{shell['var_suffix']}_info\"\n"
    "\n"
    "  and fetches it from a dict the call site passes as `globals()` --\n"
    "  `build_shell_checkboxes('Jupiter', celestial_frame, globals(),\n"
    "  globals(), tk, CreateToolTip)`. The string's name exists only as a\n"
    "  formatted value during execution. A survey that resolves visible\n"
    "  call-site names finds nothing there and records ZERO, which is\n"
    "  precisely what the gas-giant bullet below did. Git history puts\n"
    "  this path live since January 2026, months before the August 7\n"
    "  measurement, so it is a missed surface rather than tree movement.\n"
    "- **FOUR PATTERNS EXIST for the same job.** This is the actual finding.\n"
)

# ------------------------------------------------------------------
# 3 -- the gas giant bullet, inverted
# ------------------------------------------------------------------

GAS_OLD = (
    "- **Gas giant shells have NO tooltips at all** -- zero `CreateToolTip`\n"
    "  bindings for any jupiter/saturn/uranus/neptune shell. Related\n"
)

GAS_NEW = (
    "- **CORRECTED 2026-08-24: gas giant shells DO have tooltips, and they\n"
    "  are most of this item.** This bullet read \"Gas giant shells have NO\n"
    "  tooltips at all -- zero `CreateToolTip` bindings for any\n"
    "  jupiter/saturn/uranus/neptune shell.\" The sign was inverted.\n"
    "  Jupiter has 10 affected strings, Saturn 10, Uranus 8, Neptune 8 --\n"
    "  36 of the 58, in the four bodies the item recorded as having none.\n"
    "  There are indeed zero LITERAL bindings in source; they are all\n"
    "  built at run time, per the mechanism bullet above. \"No binding\n"
    "  visible in source\" and \"no tooltip\" are different claims, and this\n"
    "  bullet reported the first as the second.\n"
    "- The dead-key measurement in the same bullet is UNAFFECTED and\n"
    "  stands. Related\n"
)

# ------------------------------------------------------------------
# 4 -- the divergence measurement
# ------------------------------------------------------------------

DRIFT_ANCHOR = (
    "- **The shared-fragment pattern from L-179/L-180 is the precondition.**\n"
)

DRIFT_NEW = (
    "- **THE DRIFT IS ALREADY REAL, and it is worse than the format bug.**\n"
    "  `shell_configs.py` carries 52 inline `hover_text` literals that\n"
    "  duplicate a module string, alongside the 16 correct\n"
    "  `.replace('\\n', '<br>')` sites. **Only 11 of the 52 still agree\n"
    "  with their module twin. 41 have diverged.** Nothing on screen\n"
    "  reveals it, because each surface renders its own copy correctly.\n"
    "  The visible `<br>` bug is the half that announces itself; this is\n"
    "  the half that does not, and it is four times the size. (Measured\n"
    "  2026-08-21, structural counts reproduced 2026-08-24.)\n"
    "- **The 16 reference-pattern sites are currently NO-OPS.** Their\n"
    "  source strings already carry `<br>`, so `.replace('\\n', '<br>')`\n"
    "  finds nothing to replace. The pattern is correct and the input to\n"
    "  it is not, which is why the gas giants look right in the plot and\n"
    "  wrong in the tooltip.\n"
    "- **Each affected string has exactly ONE live consumer** -- the\n"
    "  tooltip. That makes the mechanical half of the sweep safer than the\n"
    "  scope correction suggests: 58 is a bigger number than 20, but no\n"
    "  string is being read by two places that must stay in step.\n"
    "- **The shared-fragment pattern from L-179/L-180 is the precondition.**\n"
)

# ------------------------------------------------------------------
# 5 -- the Gap
# ------------------------------------------------------------------

GAP_OLD = (
    "**Gap:** TWO JOBS, not one. (1) SOLAR -- visible bug, template exists,\n"
    "mechanical: delete the 15 `_info_hover` duplicates, author the 18\n"
    "`_info` strings in `\\n`, add `.replace('\\n', '<br>')` at the solar\n"
    "entries in `shell_configs.py`. (2) EARTH -- no visible bug, same\n"
    "duplication, and it is the case that decides the shape of the fix\n"
    "because of the surface-specific-text requirement. Do the Mode 5\n"
    "survey first in both cases.\n"
)

GAP_NEW = (
    "**Gap (rewritten 2026-08-24 on the survey):** THREE JOBS, not two,\n"
    "and the first is a look rather than a build.\n"
    "(0) CONFIRM BY RENDER. Hover a Jupiter shell checkbox -- \"-- Core\"\n"
    "will do. A literal `<br>` there confirms the 58 by the surface\n"
    "instead of by two ASTs, and nothing else should move until it does.\n"
    "(1) THE 58, not the 20. Solar's 19 through direct call sites and the\n"
    "39 reached through `build_shell_checkboxes`. Author the `_info`\n"
    "strings in `\\n`, delete the `_info_hover` duplicates, and add\n"
    "`.replace('\\n', '<br>')` at the boundary -- the 16 existing sites are\n"
    "the template and are currently no-ops for want of `\\n` input.\n"
    "(2) EARTH -- no visible bug, same duplication, and still the case\n"
    "that decides the SHAPE of the fix because of the surface-specific\n"
    "text requirement. Design against Earth; apply to all 58.\n"
    "The 41 diverged `hover_text` copies are inside job 2, not a fourth\n"
    "job: the mechanism that stops the drift is the same mechanism that\n"
    "carries surface-specific text.\n"
    "Tony's standing ruling holds throughout -- Mode 5 survey before\n"
    "sweep, and it is what produced the correction above.\n"
)

# ------------------------------------------------------------------
# 6 -- Ref and currency
# ------------------------------------------------------------------

REF_OLD = (
    "**Ref:** origin `e3ca900` (2025-04-05, correct design), `97bbfe3`\n"
    "(2026-05-25, the regression); L-181 (canonical `<br>` direction and\n"
    "the dead tooltip decision); L-190 (tooling reach); L-182 (the silent\n"
    "drift class Earth sits in).\n"
)

REF_NEW = (
    "**Ref:** origin `e3ca900` (2025-04-05, correct design), `97bbfe3`\n"
    "(2026-05-25, the regression); L-181 (canonical `<br>` direction and\n"
    "the dead tooltip decision); L-190 (tooling reach); L-182 (the silent\n"
    "drift class Earth sits in). Survey:\n"
    "`documentation/RELAY_REQUEST_L191_survey_fable_20260820.md` (the\n"
    "request, with the count deliberately withheld),\n"
    "`documentation/RELAY_RESPONSE_L191_survey_fable_20260821.md`,\n"
    "`documentation/l191_inventory.json` and\n"
    "`documentation/l191_cfgmap.json` (row-level evidence).\n"
    "Mechanism: `celestial_objects.py` `build_shell_checkboxes`;\n"
    "`palomas_orrery.py` the `globals()` call sites.\n"
)

STAMP_OLD = (
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-222:\n"
)

STAMP_NEW = (
    "Module updated: August 24, 2026 with Anthropic's Claude Opus 5 (L-191:\n"
    "scope corrected 20 -> 58 on the Fable survey, reproduced\n"
    "independently; gas-giant bullet inverted), built on 94ff80f2.\n"
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-222:\n"
)

EDITS = [
    ('SCOPE bullet: 20 -> 58', SCOPE_OLD, SCOPE_NEW),
    ('runtime-globals mechanism', MECH_ANCHOR, MECH_NEW),
    ('gas-giant bullet, sign inverted', GAS_OLD, GAS_NEW),
    ('drift measurement, 41 of 52', DRIFT_ANCHOR, DRIFT_NEW),
    ('Gap rewritten to three jobs', GAP_OLD, GAP_NEW),
    ('Ref gains the survey artifacts', REF_OLD, REF_NEW),
    ('CURRENCY: ledger header stamp', STAMP_OLD, STAMP_NEW),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    if not os.path.isfile(LEDGER):
        fail('%s not found. Run this from the repo root.' % LEDGER)

    with open(LEDGER, 'rb') as handle:
        raw = handle.read()
    ending = b'\r\n' if b'\r\n' in raw else b'\n'
    lf = raw.replace(b'\r\n', b'\n')

    actual = hashlib.md5(lf).hexdigest()
    if actual != FINGERPRINT_LF:
        fail('%s does not match the base at %s (compared in LF form, so a '
             'CRLF checkout is not the cause).\n'
             '  expected md5 %s\n  actual   md5 %s\n'
             '  The ledger has moved since this patch was written.'
             % (LEDGER, BASE_SHA[:8], FINGERPRINT_LF, actual))
    print('[base ok] %s  md5 %s  (%s on disk)'
          % (LEDGER, actual, 'CRLF' if ending == b'\r\n' else 'LF'))

    try:
        text = lf.decode('ascii')
    except UnicodeDecodeError as exc:
        fail('%s carries non-ASCII at offset %d.' % (LEDGER, exc.start))
    print('[ascii ok] %s' % LEDGER)

    for label, old, new in EDITS:
        count = text.count(old)
        if count != 1:
            fail('anchor for "%s" matched %d times, expected exactly 1.'
                 % (label, count))
        text = text.replace(old, new, 1)
        print('[anchor ok] %s' % label)

    # Nothing outside L-191 and the header may move. Bound the edits by
    # line number: every changed region must fall inside the item, or in
    # the first twenty lines where the stamp lives.
    before = lf.decode('ascii').split('\n')
    after = text.split('\n')
    start = next(i for i, l in enumerate(before) if l.startswith('#### [L-191]'))
    end = next(i for i, l in enumerate(before[start + 1:], start + 1)
               if l.startswith('#### ['))
    for index, line in enumerate(before):
        if index < 20 or start <= index <= end:
            continue
        if line and line not in after:
            fail('a line OUTSIDE L-191 and the header would be lost: %r'
                 % line[:70])
    print('[scope ok] only L-191 (lines %d-%d) and the header stamp changed'
          % (start + 1, end + 1))

    # The corrected claims must be gone and the corrections present.
    for stale in ('**20 affected strings, all in',
                  '- **Gas giant shells have NO tooltips at all** --'):
        if stale in text:
            fail('a corrected claim survived: %r' % stale)
    for fresh in ('58 strings across six', 'build_shell_checkboxes',
                  '41 have diverged', 'Hover a Jupiter shell checkbox'):
        if fresh not in text:
            fail('an intended correction is missing: %r' % fresh)
    print('[claims ok] both wrong figures retired; four corrections present')

    # The render check must be recorded as OWED, not as done. This patch
    # records a measurement, and the honesty of that distinction is the
    # thing most likely to be lost in a later edit.
    if 'measured and not confirmed' not in text:
        fail('the outstanding render confirmation is not stated. 58 must '
             'not be written as settled.')
    print('[honesty ok] 58 recorded as measured, render check named as owed')

    out = text.encode('ascii')
    if ending == b'\r\n':
        out = out.replace(b'\n', b'\r\n')
    with open(LEDGER, 'wb') as handle:
        handle.write(out)
    print('[written] %s (%s preserved)'
          % (LEDGER, 'CRLF' if ending == b'\r\n' else 'LF'))

    print('')
    print('NO CODE CHANGED. This is the survey being recorded, not the')
    print('sweep beginning. L-191 stays OPEN.')
    print('')
    print('STILL OWED, and it is the Gap\'s job 0: hover a Jupiter shell')
    print('checkbox and look for a literal <br>. Two models agreeing on')
    print('58 is two static analyses, not a render.')
    print('')
    print('NEXT:')
    print('  1. python ledger_index.py')
    print('  2. Re-run the maintenance runner')
    print('  3. Move this script to documentation/')


if __name__ == '__main__':
    main()
