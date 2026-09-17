#!/usr/bin/env python3
"""
patch_L322_3_design_round_ledger_20260916.py -- ORRERY repo.

Run: save this file in the ORRERY repo root (next to LEDGER_CONSOLIDATED.md),
open it in VS Code and click Run.  Or:  python patch_L322_3_design_round_ledger_20260916.py

Built on orrery 6f124a79d828f99ccb760c4158742f2240024825
at https://github.com/tonylquintanilla/palomas_orrery

WHAT IT DOES (one file, LEDGER_CONSOLIDATED.md, all-or-nothing):

  L-322  the design round of 2026-09-16 (evening) is recorded: (a), (b),
         (c) and (e) are RULED, in Tony's words where he gave them. The
         old Gap paragraph is kept as history under a heading that says
         every question in it is now ruled, and a NEW Gap names the build
         that remains. No status or RICE change; upd already reads
         2026-09-16.

THEN (Tony): python ledger_index.py LEDGER_CONSOLIDATED.md TWICE
(expect OK: 330 both times; no new item is added). Commit with the
handoff and the three archived patch scripts.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'LEDGER_CONSOLIDATED.md'
FP_EXPECTED = 'a3876099fcea828dbf67b500acaae332'
ZONE = (b'<!-- INDEX:START', b'<!-- INDEX:END -->')

NOTE = b"""**Note (2026-09-16, evening) -- the design round is COMPLETE. (a), (b),
(c) and (e) are RULED; (d) was ruled earlier the same evening (L-335).**
Zero code. The four rulings, in Tony's words where he gave them:
(c)+(e), one question -- WHERE the dimensional check runs and WHAT it is
built from. The check lives in the ORRERY runner (rulings 4 and 6
together). It checks DERIVED rows only, because a bare literal asserts
its unit and nothing in the file can contradict it: it works out the
unit of the expression from the units of the inputs and compares that
to the row's `# Unit:` line. It is built with ASTROPY INSIDE THE CHECK,
floats staying in the store (the second of the two shapes named in the
Gap below), each `# Unit:` token defined with `def_unit` from the token
table; `l_shell` is its own irreducible unit, which compares with
nothing, as the 2026-09-14 ruling wants. The one rule the check must
carry by hand either way: dividing by the constant that DEFINES a unit
is a CONVERSION into that unit, not a cancellation --
`EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM` is km/km to any
dimensional tool and `r_earth` to the store, so the token table records
each token's dimension AND its defining constant, and the check reads
the table. Tony: "i'll go with your recommendation. i can't decide on
how to handle the python. i am just saying that we should use
dimensional analysis to confirm that we are using the right units."
(a) The five served values outside the store MOVE INTO IT. Measured at
gallery `72a49552`: 70 served pointers, 65 into `constants_new.py`, 5
elsewhere -- `planet_poles` for the Sun, Earth, Jupiter and Saturn in
`idealized_orbits.py` (IAU 2018 pole directions, sourced on the dict),
and the galactic tide's default radius of 50000 AU as a function
argument in `solar_visualization_shells.py`. `planet_poles` becomes a
dict in the store with a dict-level Status line; the tide radius
becomes a named constant the function reads. The move is an import
change in two files plus the pointer strings, taken in the Earth and Sun
slices with the smoke suites run before and after, because the Sun and
Earth poles draw two closed rooms' axes. Tony: "this will be a
recurring issue. migrating constants into the store always carries some
risk, but it is manageable and necessary to have a single source of
truth. an exception would need to be more than mode 5 verification."
(b) The check a bare literal gets is TONY'S READ, with a written scope
and a mark on the row. Scope: any measured row whose value is DRAWN in
a published exhibit, and any row that feeds such a row. Record: one
line, `# Read: <page or table>, <date>, <reader>`, written at the row's
slice visit beside `# Unit:`, `# Status:` and `# Figures:`, when a human
has read the source against the row. It is a field like the other
three; a checker can count which drawn rows carry it. The fourteen
magnetosphere rows already have a dated, per-row read record
(`documentation/L305_gap1_read_record_20260911.md`), a MODEL's read of
Tony's PDFs; their line names the model. The worksheet schema column
saying whether a verdict is Tony's or a model's was promised for the
skill's next bump on 2026-09-11 and did not ride 2.13; it waits for
2.14. **Lesson, Tony's, same evening:** Claude turned a passing remark
of Tony's -- a digit once read from a zoomed page image -- into an
unrecorded verification failure and spent a round searching the repo
and past chats for the row. There was no failed check. "If there's no
failed check what is the problem? We are chasing our tails!" A remark
is not a defect; a hunt needs a failing check to chase.
(d) is L-335: the eight rules are in provenance-discipline 2.13.
WHAT THE ITEM NOW IS: a build, in ruling 3's order and the 2026-09-14
slicing -- the MECHANISM whole (export generator with `value`, `unit`,
`figures` per row and the bytes-hash of `constants_new.py`; the hash
checker in the orrery runner; the join check that every pointer
resolves to a row BY NAME; the dimensional check above; the token
table, one entry per token with dimension and defining constant,
replacing `SCALAR_UNITS`), then the STORE in slices, Earth first, each
row visited once for `# Unit:`, `# Status:`, `# Figures:` and, where a
human has read it, `# Read:`; `test_derived_figures.py` rewritten to
Rule 8 in the Earth slice; the five outside values moved in their
bodies' slices. The next session opens on the mechanism, after
confirming provenance-discipline 2.13 loaded.
"""

EDITS = [
(b"""**Gap:** the whole item, in ruling 3's order. Still open and NOT ruled:
(a) the five non-top-level served values""",
NOTE + b"""**Gap (as the design round left it on 2026-09-14; every question below
is now RULED, see the Note above, and the text is kept as the reasoning
record):** the whole item, in ruling 3's order. Open then and NOT
ruled: (a) the five non-top-level served values"""),
(b"""format should change at all.
**Tony-action (do):** commit
""",
b"""format should change at all.
**Gap (current, 2026-09-16):** the build named at the end of the Note
above -- mechanism whole, then the Earth slice. Nothing in this item is
awaiting a ruling.
**Tony-action (do):** commit
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
    print('edited: L-322 (design-round note; old Gap kept as history; new Gap)')
    print('patch applied. NEXT: python ledger_index.py LEDGER_CONSOLIDATED.md -- twice.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
