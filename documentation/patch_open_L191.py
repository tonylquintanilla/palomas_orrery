"""
patch_open_L191.py

Opens L-191: display-text duplication across the shell modules. The
solar `<br>` regression is one half of it; Earth's silent duplication is
the other.

Built on 2161b19012bf6e16d9e5d649103ff6feaad2ee9d at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save into the palomas_orrery folder, open in VS Code, click Run.

AFTER RUNNING
    1. Run ledger_index.py (dashboard > Developer Tools).
    2. Commit and push in GitHub Desktop.

SAFETY
    Content-fingerprinted, single-match anchor, line endings preserved.
    Aborts with NOTHING WAS WRITTEN on any mismatch.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import pathlib
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
CONTENT_FINGERPRINT = '93d456dd5e2e4dd3c168ddfee52e2aa9'

EDITS = [
    (
        "open L-191",
        b"**Ref:** L-181 (the enumerated belt/torus surface); L-189 (run history\n"
        b"and the divergence check); L-156 (Batch 2 worksheet).\n"
        b"\n"
        b"## PENDING ACTION (Tony-side)\n",

        b"**Ref:** L-181 (the enumerated belt/torus surface); L-189 (run history\n"
        b"and the divergence check); L-156 (Batch 2 worksheet).\n"
        b"\n"
        b"#### [L-191] Display-text duplication across the shell modules\n"
        b"<!-- L:191 status:OPEN upd:2026-08-07 section:A flag: rice:3/4/70/3 -->\n"
        b"- **Surfaced by Tony's Mode 5 pass, 2026-08-07.** Literal `<br>` tags\n"
        b"  visible in the Tkinter checkbox tooltips for the solar shells. Tony\n"
        b"  then spot-checked the asteroid belt and Earth tooltips, found them\n"
        b"  CLEAN, and ruled: **Mode 5 survey BEFORE the sweep, not after.**\n"
        b"  That ruling is the item's method and it is what produced everything\n"
        b"  below.\n"
        b"\n"
        b"- **ORIGIN, traced not assumed.** On 2025-04-05 (`e3ca900`) the design\n"
        b"  was correct: `gravitational_influence_info` carried `\\n` for the\n"
        b"  Tkinter tooltip and `gravitational_influence_info_hover` carried\n"
        b"  `<br>` for the Plotly hover. Same text, two formats, both in\n"
        b"  `constants_new.py`. The naming still carries that intent. Commit\n"
        b"  `97bbfe3` (2026-05-25, \"sun indicator refactor\") converted `\\n` to\n"
        b"  `<br>` in the tooltip variants as well, collapsing the distinction\n"
        b"  while the names kept implying it held. The regression is 2.5 months\n"
        b"  old.\n"
        b"\n"
        b"- **SCOPE, corrected twice.** A first estimate of \"772 lines across 17\n"
        b"  files\" was WRONG -- it counted every line in that commit gaining a\n"
        b"  `<br>`, which sweeps in the `_info_hover` strings where `<br>` is\n"
        b"  correct. Resolving every name bound to `CreateToolTip` back to its\n"
        b"  definition gives the real figure: **20 affected strings, all in\n"
        b"  `solar_visualization_shells.py`.** Earth (11 tooltip strings) and\n"
        b"  asteroid belt (4) are clean. Grep counted a proxy; the render\n"
        b"  counted the surface.\n"
        b"\n"
        b"- **FOUR PATTERNS EXIST for the same job.** This is the actual finding.\n"
        b"  | Module | Tooltip source | Plot source | State |\n"
        b"  |---|---|---|---|\n"
        b"  | solar | `_info` | `_info_hover` | two copies, FORMAT BUG VISIBLE |\n"
        b"  | earth | `_info` | dict `description` | two copies, correct today, DRIFT-CAPABLE |\n"
        b"  | gas giants | none | `_info` via `.replace()` | one copy, correct |\n"
        b"  | asteroid belt | `_info` | -- | clean |\n"
        b"\n"
        b"- **The gas giant pattern is already the fix.** `shell_configs.py`\n"
        b"  carries 16 sites of the form\n"
        b"  `'hover_text': saturn_core_info.replace('\\n', '<br>')` -- one string\n"
        b"  authored in `\\n`, converted at the Plotly boundary. That IS L-181's\n"
        b"  stated canonical direction, already implemented and working. So this\n"
        b"  item is NOT \"invent a `\\n`-canonical system\"; it is \"bring the other\n"
        b"  modules into the pattern the codebase already uses,\" with a\n"
        b"  reference implementation in the tree.\n"
        b"\n"
        b"- **Why only solar broke.** The May sweep changed source strings in\n"
        b"  many modules. For a module whose config converts at the boundary the\n"
        b"  change is a harmless no-op. Solar has no conversion step -- its\n"
        b"  `_info` copy goes to Tkinter exactly as written. Same edit, two\n"
        b"  consequences, because the modules consume their strings differently.\n"
        b"\n"
        b"- **EARTH IS NOT THE HEALTHY CASE.** Same two-copies structure as\n"
        b"  solar, the duplicate living inside a layer dict rather than under a\n"
        b"  second module-level name. Measured: **6 of 11 tooltip strings\n"
        b"  duplicate a Plotly `description` VERBATIM**, 1 differs\n"
        b"  deliberately, 4 have no plot pair. It looks correct only because\n"
        b"  both copies still agree. Editing one and not the other drifts the\n"
        b"  content SILENTLY -- and unlike solar's visible `<br>`, nothing would\n"
        b"  show it. L-182's shape.\n"
        b"\n"
        b"- **Earth's crust text carries a DESIGN CONSTRAINT on the fix.** Its\n"
        b"  plot description ends with \"(Note: toggle off the crust layer in the\n"
        b"  legend to better see the interior structure.)\" and its tooltip does\n"
        b"  not. That is deliberate, not drift -- a legend instruction that is\n"
        b"  nonsense in a checkbox tooltip. So a naive collapse-to-one-string\n"
        b"  either loses the note or pushes it where it does not belong. The\n"
        b"  unification needs a way to carry SURFACE-SPECIFIC text alongside the\n"
        b"  shared body. Solar does not surface this requirement; Earth does.\n"
        b"  Design against Earth's harder case, not solar's easier one.\n"
        b"\n"
        b"- **Gas giant shells have NO tooltips at all** -- zero `CreateToolTip`\n"
        b"  bindings for any jupiter/saturn/uranus/neptune shell. Related\n"
        b"  measurement: the `'tooltip'` key in `shell_configs.py` is defined\n"
        b"  **126 times and read by nothing**, confirming L-181's \"124 dead\n"
        b"  tooltip fields\" as dead and updating the count. Whether the gas\n"
        b"  giants SHOULD have tooltips is a separate question for Tony.\n"
        b"\n"
        b"- **The shared-fragment pattern from L-179/L-180 is the precondition.**\n"
        b"  One string serving two surfaces means the boundary conversion is a\n"
        b"  one-line change rather than a per-string rewrite.\n"
        b"\n"
        b"**Gap:** TWO JOBS, not one. (1) SOLAR -- visible bug, template exists,\n"
        b"mechanical: delete the 15 `_info_hover` duplicates, author the 18\n"
        b"`_info` strings in `\\n`, add `.replace('\\n', '<br>')` at the solar\n"
        b"entries in `shell_configs.py`. (2) EARTH -- no visible bug, same\n"
        b"duplication, and it is the case that decides the shape of the fix\n"
        b"because of the surface-specific-text requirement. Do the Mode 5\n"
        b"survey first in both cases.\n"
        b"**Ref:** origin `e3ca900` (2025-04-05, correct design), `97bbfe3`\n"
        b"(2026-05-25, the regression); L-181 (canonical `<br>` direction and\n"
        b"the dead tooltip decision); L-190 (tooling reach); L-182 (the silent\n"
        b"drift class Earth sits in).\n"
        b"\n"
        b"## PENDING ACTION (Tony-side)\n",
    ),
]


def main():
    here = pathlib.Path(__file__).parent
    path = here / TARGET
    if not path.exists():
        print(f"MISSING: {TARGET}\nRun from the palomas_orrery folder.")
        print("\nNOTHING WAS WRITTEN.")
        return 1

    data = path.read_bytes()
    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != CONTENT_FINGERPRINT:
        print(f"BASE MOVED: {TARGET}")
        print(f"    expected content MD5 {CONTENT_FINGERPRINT}")
        print(f"    actual   content MD5 {fp}")
        print("    (line endings normalized -- a real content difference.)")
        print("\nNOTHING WAS WRITTEN.")
        return 1

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print(f"  ..  {TARGET}: CRLF file -- anchors translated, endings preserved")

    problems = []
    for label, old, new in EDITS:
        o, n = (old, new)
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = data.count(o)
        if count != 1:
            problems.append(f"ANCHOR {count} MATCHES (expected 1): {label}")
        else:
            data = data.replace(o, n, 1)

    if problems:
        print("\n".join(problems))
        print("\nNOTHING WAS WRITTEN.")
        return 1

    path.write_bytes(data)
    for label, _o, _n in EDITS:
        print(f"  ok  {TARGET} -- {label}")
    print("\npatch applied")
    print("\nNext: run ledger_index.py, then commit and push.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
