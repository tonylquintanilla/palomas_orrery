#!/usr/bin/env python3
"""
Ledger housekeeping patch (2026-06-22). Transactional: every edit asserts its
exact expected match count; ANY drift aborts with no file written. After running,
re-run ledger_index.py and review the diff before committing.
Run from the repo root: python patch_ledger.py
"""
import sys
PATH = sys.argv[1] if len(sys.argv) > 1 else "LEDGER_CONSOLIDATED.md"
text = open(PATH, encoding="utf-8").read()
lines = text.split("\n")
n0 = len(lines)

# ---- 1) Close L-020 (verified this session: all 41 CUSTOM_SHELLS leaves have a tooltip)
meta_old = "<!-- L:020 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:1/2/90/2 -->"
meta_new = "<!-- L:020 status:DONE upd:2026-06-22 section:D.Structural flag: rice:1/2/90/2 -->"
assert lines.count(meta_old) == 1, "L-020 metadata anchor drift"
lines[lines.index(meta_old)] = meta_new

g_anchor = "**Gap:** scan CUSTOM_SHELLS dict; verify tooltip key present and text"
assert lines.count(g_anchor) == 1, "L-020 Gap anchor drift"
g = lines.index(g_anchor)
assert lines[g+1] == "reasonable. Could be scripted. Zero code risk."
assert lines[g+2] == "**Tony:** we have verified the hovertext by mode 5 a number of times. a simple grep could"
assert lines[g+3] == "determine if any were inadvertently missed or misconfigured. "
lines[g:g+4] = [
    "**Gap:** none -- VERIFIED 2026-06-22 (AST walk of CUSTOM_SHELLS @666244f):",
    "11 bodies, 41 leaf shell-configs, all 41 carry a tooltip, zero missing. DONE;",
    "move to section C on next housekeeping relocation.",
]

# ---- 2) Delete resolved **Tony:** annotation lines (exact full-line match + count)
delete_exact = {
    "**Tony:** let's discuss this item and remove from Pending Action section. ": 1,  # L-004 (already DONE/C)
    "**Tony:** protocol v3.28 has been committed to GitHub and can be removed from Pending section. ": 1,  # L-005
    "**Tony:** question to Claude: if this bug is fixed should it remain in the Priority section? ": 1,  # L-010
    "this is a general question about Ledger organization. I see that there are other similar items. ": 1,
    'How are "Gap" items addressed? ': 1,
    "**Tony:** Mode 5 confirmed. Close.": 1,            # L-055
    "**Tony:** Confirmed Mode 5. Close.": 3,            # L-055 x3
    "**Tony:** No recollection of a gap.": 1,           # L-029
    "**Tony:** this item does not have an L-number or header. ": 1,     # C-prose (v23 table)
    "  **Tony:** this item does not have an L-number or header. ": 1,   # C-prose (indented)
    "**Tony:** these items are missing L-numbers and headers. ": 1,     # F-log
}
for s, exp in delete_exact.items():
    got = lines.count(s)
    assert got == exp, f"delete-target count {got} != {exp} for: {s!r}"
removed = sum(delete_exact.values())
lines = [l for l in lines if l not in delete_exact]

out = "\n".join(lines)
# safety: ASCII only, no L-block headers lost
assert all(ord(c) < 128 for c in out), "non-ASCII introduced"
assert out.count("#### [L-") == text.count("#### [L-"), "an L-block header was lost"
open(PATH, "w", encoding="utf-8").write(out)
print(f"OK: L-020 closed; {removed} resolved Tony-notes cleared; lines {n0} -> {len(lines)}")
