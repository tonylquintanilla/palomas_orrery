"""
patch_L247_5_annotation_repair.py -- fix my own three defects.

Run:  save into the repo root (the folder holding constants_new.py),
      open in VS Code, click Run.
      Or:  python patch_L247_5_annotation_repair.py

Built on 8847d6be699c49c7e8fa077cc7f1790909c74c47
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHY THIS EXISTS

patch_L247_4 got the VALUES right and the ANNOTATIONS wrong in three
ways. Two checkers caught it, and this is what they caught.

  (1) UNMARKED CONTINUATIONS -- 32 lines across 5 blocks.
      constants_new.py continues an annotation leg with a marked line,
      not indented padding:

          # Source: first line
          # Source+: continues it

      I wrote indented text. The builder dropped it in silence before
      L-195 and reports it now. Those five blocks were invisible to the
      corpus until patch_L247_4 annotated them, which is why this
      passed yesterday and failed today.

  (2) NO Resolved LEG -- PARSEC_TO_AU reported DRIFTED, and the test
      that pins it says read it rather than relax it. Reading it: a
      value moved after a worksheet examined it, and I never wrote the
      leg that says the move WAS that worksheet's answer landing.
      constants_new.py already carries six such legs from L-209/L-210.
      Four values moved; four legs.

  (3) AN ANNOTATION CITING A ROW THAT DOES NOT EXIST --
      SGR_A_DISTANCE_PC carried a # Cross-checked: line naming a
      worksheet whose row is about SGR_A_DISTANCE_LY. The checker
      reported UNMATCHED. That is an annotation asserting a check that
      was not performed on that name, committed by the patch that was
      closing exactly this failure class. It is removed, not reworded.

  (4) Found while fixing the others: # Superseded: is not a label. The
      registry knows Source, Ref, Also, See, Derived, Calculation, Note,
      Cross-checked, Resolved, Removed, Corrected, Review-note. I
      invented one. Its text moves into Review-note, which exists for
      records that are neither a cross-check nor a resolution.

NO VALUE MOVES. Every constant reads exactly what it reads now. This
patch touches comments only, and asserts that.

AFTER THIS RUN, in order:
  1. python maintenance_run.py

     Ran before delivery, so this is stated rather than predicted:

       - Builder marker join returns to GREEN, 76 of 76, and the
         corpus join count rises from 177 to 214.
       - Worksheet checker tests STAYS RED on PARSEC_TO_AU, and a
         Resolved leg does not clear it. That is not this patch
         failing. worksheet_checker.py classes APPROX as INCOMPLETE and
         fires DRIFTED for CONFIRMED and INCOMPLETE alike, so a value
         that moved to the exact number the worksheet supplied still
         reads as drift. Whether that is a fourth outcome is Tony's
         call; see the message this patch shipped with.
       - Constants change still exits 1 until HEAD catches up, for the
         reason patch_L247_4 stated.
       - No value moves, so nothing needs regenerating.

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written.
"""

import hashlib
import os
import sys

TARGET = 'constants_new.py'
BASE_FP = '7a0a0dd12404e6b5ea99465098780cb5'

WS_CLAUDE = 'worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md'
WS_GPT = 'worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md'
WS_GEMINI = 'worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md'


G_OLD = b"""# Note: units m^3 kg^-1 s^-2. Measured, not exact: the relative standard
#       uncertainty is 2.2e-05, so a bare literal reads as more precise
#       than the quantity is.
# Source: CODATA 2022 -- Mohr, Newell, Taylor & Tiesinga (2025),
#         Rev. Mod. Phys. 97, 025002, doi:10.1103/RevModPhys.97.025002.
#         Published as 6.67430(15)e-11.
"""

G_NEW = b"""# Note: units m^3 kg^-1 s^-2. Measured, not exact: the relative standard
# Note+: uncertainty is 2.2e-05, so a bare literal reads as more
# Note+: precise than the quantity is.
# Source: CODATA 2022 -- Mohr, Newell, Taylor & Tiesinga (2025),
# Source+: Rev. Mod. Phys. 97, 025002,
# Source+: doi:10.1103/RevModPhys.97.025002. Published as
# Source+: 6.67430(15)e-11.
"""

G_TAIL_OLD = b"""# Note: the three legs agree on the value digit for digit and differ
#       only on which adjustment to name. The 2022 adjustment took in no
#       new competitive datum for G, so 2018 and 2022 publish the same
#       central value; 2022 is named here as the current authority.
"""

G_TAIL_NEW = b"""# Note: the three legs agree on the value digit for digit and differ
# Note+: only on which adjustment to name. The 2022 adjustment took in
# Note+: no new competitive datum for G, so 2018 and 2022 publish the
# Note+: same central value; 2022 is named here as the current
# Note+: authority.
"""

GM_OLD = b"""# Note: the nominal solar mass parameter, units m^3 s^-2. EXACT by
#       definition -- it is a conversion constant, not a measurement of
#       the Sun.
# Source: IAU 2015 Resolution B3, published as Prsa et al. (2016),
#         AJ 152, 41, doi:10.3847/0004-6256/152/2/41.
"""

GM_NEW = b"""# Note: the nominal solar mass parameter, units m^3 s^-2. EXACT by
# Note+: definition -- it is a conversion constant, not a measurement
# Note+: of the Sun.
# Source: IAU 2015 Resolution B3, published as Prsa et al. (2016),
# Source+: AJ 152, 41, doi:10.3847/0004-6256/152/2/41.
"""

MASS_OLD = b"""# Derived: 1.3271244e20 / 6.67430e-11 = 1.9884098707e30 kg.
# Derived+: Previous hardcoded value was 1.989e30, which is 0.0297%
#           high. It was not a typo. Dividing the same exact GM by the
#           CODATA 1986 G, 6.67259e-11, gives 1.98892e30 -- 1.989e30 to
#           four figures. The number moved because G moved, not because
#           the Sun did.
# Note: written as a derivation rather than as a corrected literal
#       (Tony's ruling, 2026-08-25). The product G x M is known far
#       better than either factor, and this file holds both. Carried as
#       two literals, their product was 1.32751827e20 against a defined
#       1.3271244e20 -- 0.030% off a quantity the IAU declares exact,
#       implicitly, where nothing watched it. Derived, the product is
#       exact by construction and cannot drift when CODATA next moves G.
# Note: the kilogram value still inherits G's 2.2e-05 uncertainty. What
#       the derivation fixes is the PRODUCT, not the precision of the
#       mass.
"""

MASS_NEW = b"""# Derived: 1.3271244e20 / 6.67430e-11 = 1.9884098707e30 kg.
# Derived+: Previous hardcoded value was 1.989e30, which is 0.0297%
# Derived+: high. It was not a typo. Dividing the same exact GM by the
# Derived+: CODATA 1986 G, 6.67259e-11, gives 1.98892e30 -- 1.989e30 to
# Derived+: four figures. The number moved because G moved, not because
# Derived+: the Sun did.
# Resolved: WS_GPT constants_new.py::SOLAR_MASS_KG -- literal replaced by a derivation from the IAU-exact GM, value 1.989e30 to 1.9884098707e30 (L-247)
# Note: written as a derivation rather than as a corrected literal
# Note+: (Tony's ruling, 2026-08-25). The product G x M is known far
# Note+: better than either factor, and this file holds both. Carried
# Note+: as two literals, their product was 1.32751827e20 against a
# Note+: defined 1.3271244e20 -- 0.030% off a quantity the IAU declares
# Note+: exact, implicitly, where nothing watched it. Derived, the
# Note+: product is exact by construction and cannot drift when CODATA
# Note+: next moves G.
# Note: the kilogram value still inherits G's 2.2e-05 uncertainty. What
# Note+: the derivation fixes is the PRODUCT, not the precision of the
# Note+: mass.
"""

PARSEC_OLD = b"""# Note: DEFINED, not measured. One parsec is the distance at which one
#       astronomical unit subtends one arcsecond, so the value is
#       exactly 648000/pi au and no source publishes it as a
#       measurement.
# Derived: 648000 / pi = 206264.80624709636...
# Derived+: Previous hardcoded value was 206265.0 (consistent to 6 sig
#           figs; relative error 9.39e-07). The trailing .0 asserted a
#           tenth-of-an-au precision the number did not have -- the true
#           fourth decimal is 8, not 0.
# Source: IAU 2015 Resolution B2; the exact relation is restated in
#         Prsa et al. (2016), AJ 152, 41,
#         doi:10.3847/0004-6256/152/2/41.
"""

PARSEC_NEW = b"""# Note: DEFINED, not measured. One parsec is the distance at which one
# Note+: astronomical unit subtends one arcsecond, so the value is
# Note+: exactly 648000/pi au and no source publishes it as a
# Note+: measurement.
# Derived: 648000 / pi = 206264.80624709636...
# Derived+: Previous hardcoded value was 206265.0 (consistent to 6 sig
# Derived+: figs; relative error 9.39e-07). The trailing .0 asserted a
# Derived+: tenth-of-an-au precision the number did not have -- the
# Derived+: true fourth decimal is 8, not 0.
# Source: IAU 2015 Resolution B2; the exact relation is restated in
# Source+: Prsa et al. (2016), AJ 152, 41,
# Source+: doi:10.3847/0004-6256/152/2/41.
"""

PARSEC_TAIL_OLD = b"""# Note: written as a literal rather than as 648000.0/math.pi, following
#       SPEED_OF_LIGHT_KM_S, which is equally exact by definition and
#       equally written out. A math.pi expression would also be
#       unreadable to constants_change_report.py's DERIVED case, which
#       accepts only names tracked in this file.
# Note: this value carries the whole star pipeline once L-248 lands.
#       PARSEC_TO_AU / AU_PER_LIGHT_YEAR is 3.2615637772 with the exact
#       parsec and was 3.2615668 with the rounded one; the literal
#       3.26156 that L-248 sweeps is closer to the first.
"""

PARSEC_TAIL_NEW = b"""# Resolved: WS_GPT constants_new.py::PARSEC_TO_AU -- rounded 206265.0 replaced by the exact IAU definition 648000/pi (L-247)
# Note: written as a literal rather than as 648000.0/math.pi, following
# Note+: SPEED_OF_LIGHT_KM_S, which is equally exact by definition and
# Note+: equally written out. A math.pi expression would also be
# Note+: unreadable to constants_change_report.py's DERIVED case, which
# Note+: accepts only names tracked in this file.
# Note: this value carries the whole star pipeline once L-248 lands.
# Note+: PARSEC_TO_AU / AU_PER_LIGHT_YEAR is 3.2615637772 with the
# Note+: exact parsec and was 3.2615668 with the rounded one; the
# Note+: literal 3.26156 that L-248 sweeps is closer to the first.
"""

SGRMASS_OLD = b"""# Source: GRAVITY Collaboration (2022), "Mass distribution in the
#         Galactic Center based on interferometric astrometry of
#         multiple stellar orbits", A&A 657, L12,
#         doi:10.1051/0004-6361/202142465. Published as
#         4.297 +/- 0.012 (stat) +/- 0.040 (sys) e6 solar masses.
# Cross-checked: GPT 2026-08-25 -- GRAVITY Collaboration 2022 (WS_GPT)
# Superseded: 4.154e6, GRAVITY Collaboration (2019), A&A 625, L10,
#             doi:10.1051/0004-6361/201935656, Table 1. Held here until
#             2026-08-25 under a source line reading only "GRAVITY
#             Collaboration 2019", which named no paper, DOI or table.
#             Recorded rather than deleted, per the epoch policy above.
# Review-note: ONE cross-check leg, not two. Of the three returns, only
#              GPT reached the 2022 value; the Claude return noted that
#              a successor exists without giving its numbers, and the
#              Gemini return gave the 2022 distance in prose but not the
#              mass. A second independent leg is owed on this row.
# Note: this value and SGR_A_DISTANCE_PC below came out of the same
#       orbit fit of the same stars and are strongly correlated. If
#       either is ever updated, the other moves in the SAME edit and
#       from the SAME paper. A newer distance beside an older mass is a
#       pair no publication supports, and no single-value check would
#       catch it, because each number would remain individually citable.
"""

SGRMASS_NEW = b"""# Source: GRAVITY Collaboration (2022), "Mass distribution in the
# Source+: Galactic Center based on interferometric astrometry of
# Source+: multiple stellar orbits", A&A 657, L12,
# Source+: doi:10.1051/0004-6361/202142465. Published as
# Source+: 4.297 +/- 0.012 (stat) +/- 0.040 (sys) e6 solar masses.
# Cross-checked: GPT 2026-08-25 -- GRAVITY Collaboration 2022 (WS_GPT)
# Resolved: WS_GPT constants_new.py::SGR_A_MASS_SOLAR -- advanced from the 2019 to the 2022 GRAVITY determination, 4.154e6 to 4.297e6, under the epoch policy above (L-247)
# Review-note: the value this replaces was 4.154e6, GRAVITY
#              Collaboration (2019), A&A 625, L10,
#              doi:10.1051/0004-6361/201935656, Table 1. It was held
#              here until 2026-08-25 under a source line reading only
#              "GRAVITY Collaboration 2019", which named no paper, DOI
#              or table. Recorded rather than deleted, per the epoch
#              policy above.
# Review-note: ONE cross-check leg, not two. Of the three returns, only
#              GPT reached the 2022 value; the Claude return noted that
#              a successor exists without giving its numbers, and the
#              Gemini return gave the 2022 distance in prose but not the
#              mass. A second independent leg is owed on this row.
# Note: this value and SGR_A_DISTANCE_PC below came out of the same
# Note+: orbit fit of the same stars and are strongly correlated. If
# Note+: either is ever updated, the other moves in the SAME edit and
# Note+: from the SAME paper. A newer distance beside an older mass is
# Note+: a pair no publication supports, and no single-value check
# Note+: would catch it, because each number would remain individually
# Note+: citable.
"""

SGRPC_OLD = b"""# Note: parsecs is what the primary publications actually report. This
#       file stores the published quantity and derives the display one,
#       the same shape as GM_SUN_SI above.
# Source: GRAVITY Collaboration (2022), A&A 657, L12,
#         doi:10.1051/0004-6361/202142465. Published as
#         R_0 = 8277 +/- 9 (stat) pc, with a stated systematic near
#         30 pc.
# Cross-checked: GPT 2026-08-25 -- GRAVITY Collaboration 2022 (WS_GPT)
# Review-note: the Gemini return states the same 8277 +/- 9 (stat)
#              +/- 30 (sys) pc in its Findings prose, attributing it to
#              "GRAVITY 2021" rather than 2022. Not counted as a second
#              leg here: it is prose rather than a verdicted row, and
#              the year disagrees with the journal reference. A second
#              leg is owed on this row too.
# Note: paired with SGR_A_MASS_SOLAR -- see the note on that row.
"""

SGRPC_NEW = b"""# Note: parsecs is what the primary publications actually report. This
# Note+: file stores the published quantity and derives the display
# Note+: one, the same shape as GM_SUN_SI above.
# Source: GRAVITY Collaboration (2022), A&A 657, L12,
# Source+: doi:10.1051/0004-6361/202142465. Published as
# Source+: R_0 = 8277 +/- 9 (stat) pc, with a stated systematic near
# Source+: 30 pc.
# Review-note: NO cross-check leg, and the absence is the honest state.
#              A cross-check line naming the GPT worksheet stood here
#              from 2026-08-25 until later the same day, when the
#              checker reported UNMATCHED: no row in that worksheet is
#              about SGR_A_DISTANCE_PC. The worksheet's row 5 is about
#              SGR_A_DISTANCE_LY and the value it examined was 26670.0.
#              This name did not exist when the request went out. The
#              line was removed rather than reworded, because an
#              annotation asserting a check that was not performed on
#              this name is the failure this apparatus exists to catch.
# Review-note: what the returns DO support: the GPT row 5 reached
#              R_0 = 8277 pc from GRAVITY 2022, and the Gemini Findings
#              prose states the same figure while attributing it to
#              "GRAVITY 2021". Neither is a verdicted row about this
#              constant. A dispatch is owed on this name.
# Note: paired with SGR_A_MASS_SOLAR -- see the note on that row.
"""

LY_OLD = b"""# Derived: 8277 pc x 3.2615637772 ly/pc = 26995.963 light-years.
# Derived+: Previous hardcoded value was 26670.0, which is the 2019
#           R_0 of 8178 pc converted (26673.07) and rounded to four
#           significant figures. Inverted, 26670.0 ly is 8177.06 pc,
#           which matches no column of the 2019 Table 1.
# Note: the trailing .0 on the old literal asserted 0.1 ly against a
#       real uncertainty near 100 ly, overstated by three orders of
#       magnitude. Deriving removes the claim rather than restating it.
"""

LY_NEW = b"""# Derived: 8277 pc x 3.2615637772 ly/pc = 26995.963 light-years.
# Derived+: Previous hardcoded value was 26670.0, which is the 2019
# Derived+: R_0 of 8178 pc converted (26673.07) and rounded to four
# Derived+: significant figures. Inverted, 26670.0 ly is 8177.06 pc,
# Derived+: which matches no column of the 2019 Table 1.
# Resolved: WS_GPT constants_new.py::SGR_A_DISTANCE_LY -- 26670.0 literal retired; the value now derives from a sourced SGR_A_DISTANCE_PC at the 2022 R_0 (L-247)
# Note: the trailing .0 on the old literal asserted 0.1 ly against a
# Note+: real uncertainty near 100 ly, overstated by three orders of
# Note+: magnitude. Deriving removes the claim rather than restating
# Note+: it.
"""

STAMP_OLD = b"""advanced from the 2019 to the 2022 GRAVITY determination under the
epoch policy recorded in the section header)
"""

STAMP_NEW = b"""advanced from the 2019 to the 2022 GRAVITY determination under the
epoch policy recorded in the section header)
Module updated: August 25, 2026 with Anthropic's Claude Opus 5 (L-247:
annotation repair only, no value moves -- continuation lines marked,
four Resolved legs added, an invented Superseded label retired into
Review-note, and an UNMATCHED cross-check on SGR_A_DISTANCE_PC removed)
"""

EDITS = [
    (LY_OLD, LY_NEW, 'SGR_A_DISTANCE_LY: markers + Resolved leg'),
    (SGRPC_OLD, SGRPC_NEW, 'SGR_A_DISTANCE_PC: markers, UNMATCHED cross-check removed'),
    (SGRMASS_OLD, SGRMASS_NEW, 'SGR_A_MASS_SOLAR: markers, Resolved leg, Superseded retired'),
    (PARSEC_TAIL_OLD, PARSEC_TAIL_NEW, 'PARSEC_TO_AU: tail markers + Resolved leg'),
    (PARSEC_OLD, PARSEC_NEW, 'PARSEC_TO_AU: head markers'),
    (MASS_OLD, MASS_NEW, 'SOLAR_MASS_KG: markers + Resolved leg'),
    (GM_OLD, GM_NEW, 'GM_SUN_SI: markers'),
    (G_TAIL_OLD, G_TAIL_NEW, 'GRAVITATIONAL_CONSTANT_SI: tail markers'),
    (G_OLD, G_NEW, 'GRAVITATIONAL_CONSTANT_SI: head markers'),
    (STAMP_OLD, STAMP_NEW, 'docstring: currency stamp'),
]

# Every constant assignment that must read exactly the same afterwards.
# This patch touches comments only, and this is how that is asserted
# rather than asserted about.
FROZEN_VALUES = (
    b'\nGRAVITATIONAL_CONSTANT_SI = 6.67430e-11\n',
    b'\nGM_SUN_SI = 1.3271244e20\n',
    b'\nSOLAR_MASS_KG = GM_SUN_SI / GRAVITATIONAL_CONSTANT_SI\n',
    b'\nPARSEC_TO_AU = 206264.806247096\n',
    b'\nSGR_A_MASS_SOLAR = 4.297e6\n',
    b'\nSGR_A_DISTANCE_PC = 8277.0\n',
    b'\nSGR_A_DISTANCE_LY = SGR_A_DISTANCE_PC * PARSEC_TO_AU'
    b' / AU_PER_LIGHT_YEAR\n',
)


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail('%s not found. Run this from the repo root.' % TARGET)

    ws_dir = os.path.join('documentation', 'worksheets')
    for name in (WS_GPT,):
        if not os.path.exists(os.path.join(ws_dir, name)):
            fail('%s missing. A Resolved leg naming it would be '
                 'cite-to-clear.' % name)
    print('ok  worksheet named by the Resolved legs is on disk')

    with open(TARGET, 'rb') as handle:
        data = handle.read()

    is_crlf = data.count(b'\r\n') > 0
    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != BASE_FP:
        print('ERROR: BASE MOVED -- %s' % TARGET)
        print('  expected content fingerprint %s' % BASE_FP)
        print('  found                        %s' % fp)
        sys.exit(1)
    print('base ok  %-20s (%s)  %d bytes'
          % (TARGET, 'CRLF' if is_crlf else 'LF', len(data)))

    out = data
    for old, new, label in EDITS:
        o = old.replace(b'WS_GPT', WS_GPT.encode('ascii'))
        n = new.replace(b'WS_GPT', WS_GPT.encode('ascii'))
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        bad = sorted({b for b in n if b > 127})
        if bad:
            fail('non-ASCII in inserted text (%s): %r' % (label, bad))
        count = out.count(o)
        if count != 1:
            print('ANCHOR FAIL (%d matches, expected 1): %s' % (count, label))
            print('  nothing written.')
            sys.exit(1)
        out = out.replace(o, n)
        print('ok  %s' % label)

    text = out.replace(b'\r\n', b'\n')

    for token in FROZEN_VALUES:
        if text.count(token) != 1:
            fail('post-check: a constant assignment moved -- %r'
                 % token.strip()[:50])
    print('ok  post-check: all 7 constant assignments byte-identical')

    if b'# Superseded:' in text:
        fail('post-check: the invented Superseded label survives')
    for name in (b'PARSEC_TO_AU', b'SOLAR_MASS_KG', b'SGR_A_MASS_SOLAR',
                 b'SGR_A_DISTANCE_LY'):
        needle = b'# Resolved: ' + WS_GPT.encode('ascii') + \
                 b' constants_new.py::' + name + b' --'
        if text.count(needle) != 1:
            fail('post-check: no Resolved leg for %s' % name.decode())
    print('ok  post-check: 4 Resolved legs present, Superseded retired')

    pc_block = text.split(b'\nSGR_A_DISTANCE_PC = 8277.0\n', 1)[1]
    pc_block = pc_block.split(b'\nSGR_A_DISTANCE_LY', 1)[0]
    if b'# Cross-checked:' in pc_block:
        fail('post-check: SGR_A_DISTANCE_PC still carries a cross-check')
    print('ok  post-check: the UNMATCHED cross-check is gone')

    with open(TARGET, 'wb') as handle:
        handle.write(out)
    print('patch applied  %s  %+d bytes  (%s)'
          % (TARGET, len(out) - len(data), 'CRLF' if is_crlf else 'LF'))
    print('')
    print('NEXT: python maintenance_run.py')
    print('  Builder marker join returns to green, 76 of 76.')
    print('  Worksheet checker tests STAYS RED on PARSEC_TO_AU -- a')
    print('  Resolved leg does not clear DRIFTED, and that is a ruling')
    print('  waiting on you, not this patch failing.')
    print('  Constants change still exits 1 until HEAD catches up.')
    print('  No value moves, so nothing needs regenerating.')


if __name__ == '__main__':
    main()
