"""
Patch: add "retired handle" reporting to ledger_index.py's generated
summary line (L-168 follow-on -- closes the "count mismatch" question
from the L-166/167/168 renumbering session, July 2026).

What this does:
  - Adds two small helper functions, find_retired_handles() and
    fmt_retired(), just above build_index().
  - Threads a new clause into the generated INDEX summary line reporting
    any handle numbers that have no block between 1 and the highest
    handle in use (e.g. "5 retired (never reused): L-059, L-081-084").
    These are never backfilled or reused -- this only reports them so
    the live+closed count and the max handle number don\'t look like an
    unexplained mismatch.

How to run (VS Code):
  Open this file and press Run. It patches ledger_index.py IN PLACE, in
  the same folder as this script (pass a path as the one argument to
  override). Safe to run twice -- if the patch is already applied, it
  says so and makes no changes.

After running:
  1. Re-run ledger_index.py on LEDGER_CONSOLIDATED.md as usual --
     the new summary line will show the retired-handle clause.
  2. Review the diff in GitHub Desktop, commit, push.

Module updated: July 2026 with Anthropic\'s Claude Sonnet 5.
"""
import sys
from pathlib import Path

EDITS = [
    (
b'def build_index(blocks):\n    # Group ALL blocks (including section C) by their canonical section,',
b'def find_retired_handles(blocks):\n    """Handle numbers with no block, between 1 and the highest handle in\n    use. Under the append-only convention (nothing is ever renumbered),\n    these are almost always a draft handle assigned to something that\n    was superseded before it ever landed -- never reuse them. Reported\n    here so the live+closed count and the max handle number don\'t look\n    like an unexplained mismatch (L-166/167/168 renumbering saga,\n    July 2026)."""\n    used = {int(b[\'L\']) for b in blocks}\n    if not used:\n        return []\n    return [n for n in range(1, max(used) + 1) if n not in used]\n\n\ndef fmt_retired(nums):\n    """Render a sorted list of ints as zero-padded, range-collapsed\n    handles, e.g. [59, 81, 82, 83, 84] -> \'L-059, L-081-084\'."""\n    if not nums:\n        return \'\'\n    ranges = []\n    start = prev = nums[0]\n    for n in nums[1:]:\n        if n == prev + 1:\n            prev = n\n            continue\n        ranges.append((start, prev))\n        start = prev = n\n    ranges.append((start, prev))\n    parts = [f"L-{lo:03d}" if lo == hi else f"L-{lo:03d}-{hi:03d}"\n             for lo, hi in ranges]\n    return \', \'.join(parts)\n\n\ndef build_index(blocks):\n    # Group ALL blocks (including section C) by their canonical section,'
    ),
    (
b'    out.append(f"*{total} live items; {gaps} need attention (`!`); {scored} RICE-scored; "\n               f"{closed_n} closed (section C + {\'/\'.join(sorted(TRACK_DONE_BUCKETS))}). "\n               "Find an `L-0NN` handle (Ctrl+F in VS Code) "\n               "to jump to any item; search `| ! |` to list every gap. See \\"Using and maintaining this "\n               "ledger\\" above for details.*")',
b'    retired = find_retired_handles(blocks)\n    retired_clause = (f" {len(retired)} retired (never reused): {fmt_retired(retired)}."\n                       if retired else "")\n    out.append(f"*{total} live items; {gaps} need attention (`!`); {scored} RICE-scored; "\n               f"{closed_n} closed (section C + {\'/\'.join(sorted(TRACK_DONE_BUCKETS))});"\n               f"{retired_clause} "\n               "Find an `L-0NN` handle (Ctrl+F in VS Code) "\n               "to jump to any item; search `| ! |` to list every gap. See \\"Using and maintaining this "\n               "ledger\\" above for details.*")'
    ),
]

ALREADY_APPLIED_MARKER = b"def find_retired_handles(blocks):"


def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent / "ledger_index.py"
    if not target.exists():
        print(f"ERROR: {target} not found.")
        sys.exit(1)

    content = target.read_bytes()

    if ALREADY_APPLIED_MARKER in content:
        print(f"Already applied -- {target} already has find_retired_handles(). No changes made.")
        return

    for old, new in EDITS:
        n = content.count(old)
        assert n == 1, f"expected 1 match, got {n}, for anchor starting: {old[:60]!r}"
        content = content.replace(old, new)

    target.write_bytes(content)
    print(f"Patched {target} -- retired-handle reporting added to the INDEX summary line.")
    print("Next: re-run ledger_index.py on LEDGER_CONSOLIDATED.md, review the diff, commit+push.")


if __name__ == "__main__":
    main()
