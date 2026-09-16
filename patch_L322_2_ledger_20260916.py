#!/usr/bin/env python3
"""
patch_L322_2_ledger_20260916.py -- ORRERY repo. Run AFTER
patch_L322_1_figures_skill_protocol_20260916.py.

Run: save this file in the ORRERY repo root (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L322_2_ledger_20260916.py

Built on orrery ebdc55cc4668c297d78ff1d46d2880b3cd78635f
at https://github.com/tonylquintanilla/palomas_orrery

WHAT IT DOES (one file, LEDGER_CONSOLIDATED.md, all-or-nothing):

  L-322  a Note recording that (d) is ruled on 2026-09-16 and what the
         Earth-slice walk now writes at each visit; upd date moves.
  L-325  a Note recording that Tony WITHDREW its ruling on 2026-09-16,
         where its residue lives, and one (decide) on closing it; upd
         date moves. Status is NOT changed by this patch.
  L-335  NEW, DONE, section C: the provenance-discipline 2.12 -> 2.13
         bump, in the form L-326 used for 2.12.

THEN (Tony): python ledger_index.py LEDGER_CONSOLIDATED.md TWICE. The
first run files L-335 and regenerates the index; the second prints OK.
The ledger goes in the SAME commit as the skill and the protocol.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
# md5 of LF-normalised content with the INDEX zone removed, because
# ledger_index.py rewrites that zone.
FP_EXPECTED = 'a54ddca28595db5b5746a665afd35c19'
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

EDITS = [

# --- L-322: upd date -----------------------------------------------------
(b"""<!-- L:322 status:OPEN upd:2026-09-12 section:A flag: rice:4/5/70/6 -->""",
 b"""<!-- L:322 status:OPEN upd:2026-09-16 section:A flag: rice:4/5/70/6 -->"""),

# --- L-322: the (d) ruling, before the Ref line --------------------------
(b"""**Ref:** L-305, L-306 (approximations are not promoted), L-314,
""",
b"""**Note (2026-09-16) -- (d) is RULED.** Tony: "confirmed as recommended.
and i withdraw my september 12 ruling as it may be counter productive
given the new procedure." The procedure is the textbook one, in
`documentation/DESIGN_L322_d_significant_figures_20260916.md`, and it
is now in provenance-discipline 2.13 as The Figure Count Is a Declared
Field (L-335). What each row's single visit writes is therefore three
fields: `# Unit:`, `# Status:` and `# Figures:`. Two of the eight rules
changed shape at the withdrawal and the file records the revised form:
the store HOLDS the derivation as an expression and the EXPORT rounds
each value to its declared count, carrying the count beside the value
and the unit; and the checker judges the declaration (a derived row's
count may not exceed the least count among its non-exact named inputs)
rather than recomputing a literal. MEASURED at ebdc55cc, the reason it
was urgent: 27 rows carry a `# Derived:` line -- 21 are expressions, 4
are literals with no Status line, 2 are L-325's literals -- and
`test_derived_figures.py` could see 2 of the 27, because it enumerates
by a Status word. It ran green on those 2. The full 27 are named in the
design file, section 2. Consequences for this item's build, in ruling
3's order: (1) the Earth slice's 12 derived rows (10 interior and
near-space, 2 Hill sphere) get `# Figures:` and stay expressions;
(2) the 5 exact conversions get `# Figures: exact`; (3) L-325's two
literals stay literals until the export lands and revert at their
visit, because the gallery still parses the store today;
(4) `test_derived_figures.py` is rewritten to Rule 8 in the same slice,
enumerating by `# Derived:` and naming NOT YET MIGRATED rows, and its
DERIVATIONS formula table goes; (5) the export (ruling 6) carries
`figures` beside `value` and `unit`, which is a dependency on (c) and
(e), not a ruling on them. (a), (b), (c) and (e) stay open.
**Ref:** L-305, L-306 (approximations are not promoted), L-314,
"""),

# --- L-325: upd date -----------------------------------------------------
(b"""<!-- L:325 status:OPEN upd:2026-09-12 section:A flag: rice:3/3/90/2 -->""",
 b"""<!-- L:325 status:OPEN upd:2026-09-16 section:A flag: rice:3/3/90/2 -->"""),

# --- L-325: the withdrawal, before the Ref line --------------------------
(b"""**Ref:** L-305, L-314, L-322, `constants_new.py`,
`test_derived_figures.py`, `orrery_maintenance_run.py`,
""",
b"""**Note (2026-09-16) -- the RULE is WITHDRAWN by Tony**, in the message
that adopted L-322 (d)'s procedure: "i withdraw my september 12 ruling
as it may be counter productive given the new procedure." Why it is
counter-productive: a literal rounded at rest is a rounded intermediate
for every row that chains from it (EARTH_GEOSTATIONARY_RADII divides a
derived row), and the standard method rounds once, at the end. The
objection that earned the ruling -- sixteen digits copied into a
gallery config -- is answered instead at the export, which rounds to
the declared `# Figures:` count. The skill section landed at 2.12 is
replaced by a WITHDRAWN stub at 2.13. What this item BUILT stays in the
tree for now and is re-homed to L-322's Earth slice: the two literals
revert to expressions when the export lands (the gallery parses the
store until then and cannot evaluate a tanh); `test_derived_figures.py`
is rewritten to judge the declaration rather than recompute a literal,
and its wiring into the runner and the dashboard stays. **Tony-action
(decide):** close this item as SUPERSEDED by L-322 now, or leave it OPEN
until the two rows revert. Neither changes the work.
**Ref:** L-305, L-314, L-322, `constants_new.py`,
`test_derived_figures.py`, `orrery_maintenance_run.py`,
"""),

# --- L-335: new DONE item, before L-326 ----------------------------------
(b"""#### [L-326] provenance-discipline 2.11 -> 2.12, taken before the build it serves
""",
b"""#### [L-335] provenance-discipline 2.12 -> 2.13, taken before the store work it serves
<!-- L:335 status:DONE upd:2026-09-16 section:C flag: rice:3/4/90/2 -->
- **What landed.** L-322 (d), significant figures, ruled by Tony on
  2026-09-16 "as recommended" from
  `documentation/DESIGN_L322_d_significant_figures_20260916.md`. The
  Figure Count Is a Declared Field [QUALITY] joins Report to the Figures
  You Have with eight rules: the `# Figures:` key and its three forms;
  counting a literal by the standard rules; a derived row's count set by
  its least precise measured input (fewest figures for a product or
  quotient, coarsest decimal place for a sum or difference, exact and
  declared numbers skipped); compute from the primaries and round once;
  round half to even; the store holds the derivation and the export
  rounds; a display shows fewer figures, never more; the checker judges
  the declaration and names every derived row it cannot see. The
  reference Tony named is Wikipedia's Significant figures page; the
  engineering standard behind it is ASTM E29.
- **One rule withdrawn.** A Derived Row Stores the Figure Its Sources
  Support [CRITICAL], landed at 2.12 from L-325, is replaced by a stub
  saying it was withdrawn on 2026-09-16 and why. See L-325.
- **One addition beyond the eight rules.** The new section says the
  field works "like `# Unit:`", and the skill had never defined
  `# Unit:` -- L-322 ruling 1 lived only in the ledger. The Status Line
  gains The Unit Field. A convention that is not in the skill does not
  travel (L-317, L-326, now here).
- **Why it was taken first.** v3.55's ordering: the bump precedes the
  Earth-slice walk that writes the field, so the stale-skill gate fires
  on a matching manifest. Protocol entry v3.61.
- **Obligation.** The session that made this bump had loaded 2.12, and
  a reinstall is invisible to the session that makes it. The next
  session confirms its loaded copy reads 2.13 before provenance or
  store work.
- **Ref:** L-322, L-325, L-326, L-327 (Tony's question whether more
  rules are the answer -- this one was asked for by name),
  `skills/provenance-discipline/SKILL.md`,
  `documentation/DESIGN_L322_d_significant_figures_20260916.md`,
  `patch_L322_1_figures_skill_protocol_20260916.py`,
  `patch_L322_2_ledger_20260916.py`.

#### [L-326] provenance-discipline 2.11 -> 2.12, taken before the build it serves
"""),
]


def lf(data):
    return data.replace(b'\r\n', b'\n')


def fingerprint(content):
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    return hashlib.md5(content[:a] + content[b:]).hexdigest()


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print(f'ERROR: {TARGET} not found next to this script. NOTHING was written.')
        return 1
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    content = lf(raw)
    actual = fingerprint(content)
    if actual != FP_EXPECTED:
        print(f'ERROR: {TARGET} is not the file this patch was built against')
        print(f'       expected {FP_EXPECTED}, found {actual}{" [CRLF]" if was_crlf else ""}')
        print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
        return 1
    original = content
    for old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print(f'ANCHOR FAIL: expected 1 match, found {n}: {old[:70]!r}')
            print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        content = content.replace(old, new)
    if any(c > 127 for c in content):
        print('ERROR: the patched ledger would hold non-ASCII bytes. NOTHING was written.')
        return 1
    if content == original:
        print('ERROR: unchanged after edits. NOTHING was written.')
        return 1
    out = content.replace(b'\n', b'\r\n') if was_crlf else content
    with open(path, 'wb') as f:
        f.write(out)
    print(f'ok  {TARGET}  ({len(out)} bytes{", CRLF preserved" if was_crlf else ""})')
    print('edited: L-322 (note, upd), L-325 (note, upd); added: L-335 (DONE, section C)')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md -- twice.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
