#!/usr/bin/env python3
"""
patch_L322_1_figures_skill_protocol_20260916.py -- ORRERY repo.

Run: save this file in the ORRERY repo root (next to PROJECT_INSTRUCTIONS.md),
open it in VS Code and click Run.  Or:  python patch_L322_1_figures_skill_protocol_20260916.py

Built on orrery ebdc55cc4668c297d78ff1d46d2880b3cd78635f
at https://github.com/tonylquintanilla/palomas_orrery
(gallery at 72a49552aa6ba4b21c2f58e3c5fe53f7d198590c
at https://github.com/tonylquintanilla/tonyquintanilla.github.io; no
gallery file is edited).

WHAT IT DOES (three files, all-or-nothing):

  L-322  skills/provenance-discipline/SKILL.md          2.12 -> 2.13
         (d) of L-322 is ruled. Tony's rulings of 2026-09-16:
           - the eight-rule significant-figures procedure in
             documentation/DESIGN_L322_d_significant_figures_20260916.md
             is adopted as recommended, with rules 6 and 8 revised for
             the withdrawal below;
           - his ruling of 2026-09-12 (L-325, "a derived row stores the
             figure its sources support") is WITHDRAWN as counter-
             productive under the new procedure.
         Edits: the version header; a new subsection The Unit Field under
         The Status Line, carrying L-322 ruling 1 into the skill (it lived
         only in the ledger); Report to the Figures You Have gains the
         "# Figures:" field in its example; a new section The Figure
         Count Is a Declared Field [QUALITY] with the eight rules; the
         section A Derived Row Stores the Figure Its Sources Support
         [CRITICAL] is replaced by a WITHDRAWN stub that says why.
  v3.61  PROJECT_INSTRUCTIONS.md gains the version-history entry naming
         the bump and why; header stamp and SHA anchor move with it; the
         v3.58 entry moves down into
         documentation/PROJECT_INSTRUCTIONS_HISTORY.md to keep three
         resident.

WHAT IS PERMANENT: everything above. The script itself is one-shot.

THEN (Tony):
  1. python skills_index.py          (expect: the provenance-discipline
                                      manifest row reads 2.13; it prints
                                      what it read before)
  2. run patch_L322_2_ledger_20260916.py (the ledger half), then
     python ledger_index.py LEDGER_CONSOLIDATED.md TWICE.
  3. Reinstall provenance-discipline at Settings > Skills. The session
     that installs cannot verify it; the next session confirms 2.13
     loaded before provenance or store work.
  4. Commit SKILL.md, PROJECT_INSTRUCTIONS.md, the history file, the
     ledger and the regenerated manifest TOGETHER (the four-step rule:
     a bump is one commit).

The guard on PROJECT_INSTRUCTIONS.md hashes the content OUTSIDE the
SKILL-MANIFEST zone, because skills_index.py rewrites that zone.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

# (path, md5 of LF-normalised content with generated zones removed, [zone markers])
FILES = {
    'skills/provenance-discipline/SKILL.md': ('fbca73ee0d9be1fa726d5c2d7dec6787', None),
    'PROJECT_INSTRUCTIONS.md': ('5b4aadf5a91ce8201edb8e7eab73294c', (b'<!-- SKILL-MANIFEST:START', b'<!-- SKILL-MANIFEST:END -->')),
    'documentation/PROJECT_INSTRUCTIONS_HISTORY.md': ('98d380fc4902359a28ae22c99d4d7d97', None),
}

EDITS = {}

# ----------------------------------------------------------------------
# skills/provenance-discipline/SKILL.md  2.12 -> 2.13
# ----------------------------------------------------------------------
EDITS['skills/provenance-discipline/SKILL.md'] = [

# --- version header -----------------------------------------------------
(b"""Skill version: 2.12 | Cut from palomas_orrery @ bfc0505e (v2.12),
earlier @ 159c5a2c (v2.11), @ 071a0a65 (v2.10),
earlier @ a263f73d (v2.9), @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7),
@ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)
| September 14, 2026
v2.12 adds five rules""",
b"""Skill version: 2.13 | Cut from palomas_orrery @ ebdc55cc (v2.13),
earlier @ bfc0505e (v2.12), @ 159c5a2c (v2.11), @ 071a0a65 (v2.10),
earlier @ a263f73d (v2.9), @ 7f4a2f9f (v2.8), @ 3faa72a0 (v2.7),
@ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9)
| September 16, 2026
v2.13 settles L-322 (d), significant figures, on Tony's rulings of
2026-09-16. The Figure Count Is a Declared Field [QUALITY] joins
Report to the Figures You Have: a "# Figures:" line beside every
value, counted by the standard rules (fewest figures for products
and quotients, coarsest decimal place for sums and differences,
exact and declared numbers never limit a result), computed from the
primary inputs at full precision and rounded ONCE at the reporting
step, half to even. A Derived Row Stores the Figure Its Sources
Support [CRITICAL] is WITHDRAWN on Tony's word of the same day: a
rounded literal at rest is a rounded intermediate for every row that
chains from it, which is the error the procedure exists to prevent.
The store holds the derivation; the export rounds. The Status Line
gains The Unit Field, carrying L-322 ruling 1 into the skill, where
it had not travelled. Handles L-322, L-325, L-335.
v2.12 adds five rules"""),

# --- The Unit Field, under The Status Line ------------------------------
(b"""**Inside a dict, the status line attaches to the DICT when its entries
share one kind and one source**, and an entry that differs carries its
own line, which overrides.""",
b"""### The Unit Field

**A unit is a declared field beside the value, `# Unit:`, never a
suffix on the name.** Two declarations of one fact can disagree, so the
suffix is dropped as a declaration once the field exists. The token
names the QUANTITY, which is what makes comparison possible: `deg`
rather than `dimensionless` for an angle, `l_shell` rather than
`dimensionless` for a McIlwain L, because 105 degrees is not
interchangeable with 105 of anything else. `dimensionless` names no
quantity and retires as a token. The migration is walked by body,
Earth first, and each row is visited once: `# Unit:`, `# Status:` and
`# Figures:` (below) are written at that single visit.

(Tony's rulings, 2026-09-11 and 2026-09-14, recorded on L-322 and until
this version living only there. In engineering he has always used
units, not literals.)

**Inside a dict, the status line attaches to the DICT when its entries
share one kind and one source**, and an entry that differs carries its
own line, which overrides."""),

# --- Report to the Figures You Have: the example gains the field --------
(b"""```python
EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1221.5 / 6378.1366 = 0.19151 -- 5 significant figures, set
# Derived+: by the numerator. Report no more than that.
```

Significant figures govern REPORTING: every quotient stated in a
comment, a hover string or a tooltip, with the figure count named beside
it so the next reader does not re-derive it.""",
b"""```python
EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)
# Derived: 1221.5 / 6378.1366 = 0.19151
```

Significant figures govern REPORTING: every quotient stated in a
comment, a hover string or a tooltip carries no more figures than the
row's `# Figures:` line declares. The count is a field, not prose, so
the next reader does not re-derive it and a checker can read it; the
section below says how the field is written and counted."""),

# --- new section: The Figure Count Is a Declared Field ------------------
(b"""### The Store Carries the Verified Figure [CRITICAL]

**Where a source gives a verified figure more precise than the stored
value, the store carries the verified figure.""",
b"""### The Figure Count Is a Declared Field [QUALITY]

Python can round a number to N figures but cannot count them through
arithmetic, so the count is declared per row, the way the unit is.
These are the textbook rules (Wikipedia, Significant figures; ASTM
E29), written down once so they resolve the same way for every row.

**Rule 1. `# Figures:` is a comment key beside the value.** Three forms:

```
# Figures: 5 -- set by EARTH_INNER_CORE_KM (1221.5, 5)
# Figures: 4 -- source states 4; the trailing zero in 3480 is significant
# Figures: exact -- IAU 2012 definition
```

A derived row names the input that set its count. A measured row
states what the source supports, and says in words whether a trailing
zero counts, because an integer literal cannot. A defined constant says
`exact`. The field is needed because a float cannot hold a significant
trailing zero (13.50 is stored as 13.5) and the export would otherwise
lose the count.

**Rule 2. Counting a literal follows the standard rules.** Non-zero
digits count; zeros between them count; leading zeros never count;
zeros after the decimal point at the end count; trailing zeros in an
integer count only if the source says so. An exact number has unlimited
figures. A DECLARED drawing condition (a chosen solar wind pressure, a
chosen cut angle) is exact for counting: it is a choice, not a
measurement, so all of its digits are known.

**Rule 3. A derived row's count is set by its least precise MEASURED
input.** Products and quotients keep the fewest figures among the
inputs. Sums and differences are good to the coarsest decimal place
among the inputs (`6371.0 - 660` is good to units: 5711). Exact inputs
and declared conditions are skipped when finding the minimum. For a
power, an exponential or another function, the fewest-figures rule is
the default; where the function magnifies the input's uncertainty (an
exponent above one in magnitude), drop a figure and say why on the
row. Where an input carries a stated uncertainty, the uncertainty
decides instead and counting is the fallback.

**Rule 4. Compute from the PRIMARY inputs at full precision; round
once.** A derived row that feeds a second derived row does not chain
through a rounded copy. The second row's `# Derived:` line goes back to
the measured primaries. Rounding an intermediate puts a rounding error
inside the store.

**Rule 5. Round half to even**, implemented as `float("%.*g" % (n, x))`.
This is what Python's `round()` and `%g` already do; the schoolroom
half-away-from-zero is not, so the rule is named to avoid an argument
with the interpreter.

**Rule 6. The store holds the derivation, never a rounded copy.** A
derived row stays an expression at full float precision and follows its
inputs automatically. Rounding happens at the reporting step, and the
EXPORT is a reporting step: it rounds each value to its declared count
and carries the count beside the value and the unit, so the gallery
formats without guessing and no downstream copy holds digits the row
never had. (This is what Tony's 2026-09-12 objection was about --
sixteen digits copied into a gallery config -- and Rule 6 answers it at
the boundary rather than at rest.) The two magnetosphere standoffs
stored as literals under the withdrawn ruling stay literals until the
export lands and the gallery stops parsing the store (L-322 ruling 6);
they revert to expressions at their slice visit.

**Rule 7. The declared count governs reporting; a display may show
fewer, never more.** A hover formats to the served count or to a shorter
readable count; a shorter display is not a precision claim. A display
with more figures than the row declares is the failure.

**Rule 8. The checker reads the field and names every derived row it
cannot see.** `test_derived_figures.py` checks the DECLARATION rather
than a rounded literal: a derived row's count may not exceed the least
count among the non-exact inputs it names, each named input appears in
the expression, and a `# Derived:` row with no `# Figures:` line prints
NOT YET MIGRATED with its name -- a FAIL inside a closed slice, a named
gap outside one. Enumeration is by the `# Derived:` line, not by a
`# Status:` word: at 2.12 the checker found derived rows by Status and
saw 2 of 27.

(Tony's rulings, 2026-09-16, adopting the procedure in
`documentation/DESIGN_L322_d_significant_figures_20260916.md` "as
recommended" and withdrawing the ruling of 2026-09-12 in the same
message. Handle L-322 (d).)

### The Store Carries the Verified Figure [CRITICAL]

**Where a source gives a verified figure more precise than the stored
value, the store carries the verified figure."""),

# --- the withdrawn section becomes a stub -------------------------------
(b"""### A Derived Row Stores the Figure Its Sources Support [CRITICAL]

A derived constant stores the figure its inputs actually support, not
the arithmetic result. Sixteen digits on a value uncertain in the first
decimal is calculator output, not precision. The arithmetic stays
recorded on the row, so it remains auditable, and a check recomputes
the row from the inputs its Status line names and FAILS when the
rounding stops holding.

An expression recomputes silently when an input moves, which is a
published number changing with nobody looking. A literal plus a test
announces instead.

**Scope: this governs rows whose inputs are DECLARED CONSTANTS.** L-314
may serve solar wind speed and pressure from the cache, and a stored
literal guarded by a test that fails every time the wind changes is a
test nobody reads. Re-examine when L-314 is designed.

(Tony's ruling, 2026-09-12, stopping two standoff values from being
copied into the gallery config at full stored precision: "the store
should only carry significant digits not what the calculator
generates." Both rows already declared what to report and stored
something else. Handle L-325; the scope paragraph is his own ledger
note under L-314.)
""",
b"""### A Derived Row Stores the Figure Its Sources Support -- WITHDRAWN

Ruled by Tony on 2026-09-12 (L-325) and WITHDRAWN by him on 2026-09-16
as counter-productive under The Figure Count Is a Declared Field. The
rule said a derived row stores a literal rounded to its declared count,
so that a test could announce when an input moved. Under Rule 4 a
rounded literal at rest is a rounded intermediate for every row that
chains from it, and under Rule 6 the objection that earned the ruling
-- sixteen digits copied into a gallery config -- is answered at the
export instead. The stub stays so a reader who finds L-325 or the two
literal rows knows what happened to the rule.
"""),
]

# ----------------------------------------------------------------------
# PROJECT_INSTRUCTIONS.md  v3.60 -> v3.61
# ----------------------------------------------------------------------
V361_ENTRY = b"""v3.61 (September 16, 2026): No rule changed in this document. ONE
skill bump, taken ahead of the store work it serves.

provenance-discipline 2.12 -> 2.13 (L-335). L-322 (d), significant
figures, is ruled, and one ruling of four days earlier is withdrawn.

THE PROCEDURE IS THE TEXTBOOK ONE, written down once. Tony asked for
standard methods and named the reference. The skill now says: the
figure count is a declared field, "# Figures:", beside every value, the
way the unit is; a literal is counted by the standard rules; a derived
row keeps the fewest figures of its measured inputs for a product or
quotient and the coarsest decimal place for a sum or difference, with
exact and declared numbers never limiting the result; the arithmetic
runs from the primary inputs at full precision and rounds ONCE, half to
even; and the export is where that rounding happens, carrying the count
beside the value so the gallery formats without guessing.

THE RULING WITHDRAWN IS L-325's, that a derived row stores a rounded
literal so a test can announce when an input moves. Tony withdrew it in
the same message that adopted the procedure, because a rounded literal
at rest is a rounded intermediate for every row that chains from it.
The objection that earned the ruling, sixteen digits copied into a
gallery config, is now answered at the export rather than at rest. The
skill keeps a stub where the rule stood, so a reader who meets the two
literal rows knows why they look the way they do.

WHAT MADE IT URGENT was measured, not recalled. The store holds 27
derived rows and the checker could see 2 of them, because it found
derived rows by a word on a Status line that 25 rows do not carry. It
ran green this session on the 2. The skill also disagreed with itself:
one section said a derived row stays an expression and the withdrawn
one said it stores a literal, and 21 rows followed the first while 2
followed the second. Rule 8 has the checker enumerate by the
"# Derived:" line and name every row it cannot judge.

ONE ADDITION BEYOND THE EIGHT RULES. The new section says the figure
field works "like # Unit:", and the skill had never defined "# Unit:";
L-322 ruling 1 lived only in the ledger. The Status Line gains The Unit
Field. A convention that is not in the skill does not travel -- v3.57's
lesson, a third time.

THE ORDERING IS v3.55's: the bump precedes the Earth-slice walk that
writes the field. The obligation travels: this session loaded 2.12, and
a reinstall cannot be verified from inside the session that makes it.
The next session confirms its loaded copy reads 2.13 before provenance
or store work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.58 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

V358_START = b"""v3.58 (September 14, 2026): No rule changed in this document. ONE
skill bump, taken as the session's FIRST action, ahead of the build it
serves.
"""
V358_END = b"""Version history: v3.55 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

Functional for Claude, readable for human, signal preserved.
"""

EDITS['PROJECT_INSTRUCTIONS.md'] = [
(b"""Tony Quintanilla, PE | Claude | v3.60 | September 16, 2026

Cut from d99d8db1 at https://github.com/tonylquintanilla/palomas_orrery
""",
b"""Tony Quintanilla, PE | Claude | v3.61 | September 16, 2026

Cut from ebdc55cc at https://github.com/tonylquintanilla/palomas_orrery
"""),
(b"""v3.60 (September 16, 2026): No rule changed in this document. TWO
skill bumps, taken as the session's first action, ahead of the build
they serve.
""",
V361_ENTRY + b"""v3.60 (September 16, 2026): No rule changed in this document. TWO
skill bumps, taken as the session's first action, ahead of the build
they serve.
"""),
# the v3.58 entry is removed as a SPAN (start anchor .. end anchor) below
]

EDITS['documentation/PROJECT_INSTRUCTIONS_HISTORY.md'] = [
(b"""(Moved down from the resident protocol on 2026-09-16 when v3.60
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
""",
b"""(Moved down from the resident protocol on 2026-09-16 when v3.60
made a fourth entry.)

@@V358@@

(Moved down from the resident protocol on 2026-09-16 when v3.61
made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37
"""),
]


def lf(data):
    return data.replace(b'\r\n', b'\n')


def fingerprint(content, zone):
    if zone:
        a = content.index(zone[0])
        b = content.index(zone[1]) + len(zone[1])
        content = content[:a] + content[b:]
    return hashlib.md5(content).hexdigest()


def main():
    originals = {}
    results = {}
    # 1. read + guard every file before writing any
    for rel, (fp_expected, zone) in FILES.items():
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f'ERROR: {rel} not found next to this script. NOTHING was written.')
            return 1
        raw = open(path, 'rb').read()
        was_crlf = b'\r\n' in raw
        content = lf(raw)
        actual = fingerprint(content, zone)
        if actual != fp_expected:
            print(f'ERROR: {rel} is not the file this patch was built against')
            print(f'       expected {fp_expected}, found {actual}{" [CRLF]" if was_crlf else ""}')
            print('       NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
            return 1
        originals[rel] = (content, was_crlf, actual)

    # 2. apply edits in memory
    for rel, edits in EDITS.items():
        content, was_crlf, _ = originals[rel]
        for old, new in edits:
            n = content.count(old)
            if n != 1:
                print(f'ANCHOR FAIL: {rel}: expected 1 match, found {n}: {old[:70]!r}')
                print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
                return 1
            content = content.replace(old, new)
        results[rel] = content

    # 3. move the v3.58 entry from the protocol into the history file
    proto = results['PROJECT_INSTRUCTIONS.md']
    a = proto.count(V358_START)
    b = proto.count(V358_END)
    if a != 1 or b != 1:
        print(f'ANCHOR FAIL: PROJECT_INSTRUCTIONS.md v3.58 span: start x{a}, end x{b}')
        print('NOTHING was written.')
        return 1
    i = proto.index(V358_START)
    j = proto.index(V358_END) + len(V358_END)
    span = proto[i:j]
    tail = b'\nFunctional for Claude, readable for human, signal preserved.\n'
    assert span.endswith(tail)
    v358 = span[:-len(tail)].rstrip(b'\n') + b'\n'
    results['PROJECT_INSTRUCTIONS.md'] = (proto[:i]
        + b'Functional for Claude, readable for human, signal preserved.\n'
        + proto[j:])
    hist = results['documentation/PROJECT_INSTRUCTIONS_HISTORY.md']
    assert hist.count(b'@@V358@@') == 1
    results['documentation/PROJECT_INSTRUCTIONS_HISTORY.md'] = hist.replace(
        b'@@V358@@\n', v358)

    # 4. encoding gate on what this patch introduces
    for rel, content in results.items():
        bad = [c for c in content if c > 127]
        if bad:
            print(f'ERROR: {rel} would hold {len(bad)} non-ASCII byte(s) after the patch. NOTHING was written.')
            return 1
        if results[rel] == originals[rel][0]:
            print(f'ERROR: {rel} unchanged after edits -- anchors matched but produced no change.')
            return 1

    # 5. write, preserving each file's own line-ending style
    for rel, content in results.items():
        _, was_crlf, _ = originals[rel]
        out = content.replace(b'\n', b'\r\n') if was_crlf else content
        with open(os.path.join(ROOT, rel), 'wb') as f:
            f.write(out)
        print(f'ok  {rel}  ({len(out)} bytes{", CRLF preserved" if was_crlf else ""})')
    print('stamped: skills/provenance-discipline/SKILL.md (2.13, ebdc55cc), '
          'PROJECT_INSTRUCTIONS.md (v3.61, ebdc55cc)')
    print('patch applied. NEXT: python skills_index.py; then '
          'patch_L322_2_ledger_20260916.py and ledger_index.py twice; '
          'then reinstall provenance-discipline; commit everything together.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
