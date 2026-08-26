"""
patch_L247_4_repair.py -- the L-247 repair, all five rows.

Run:  save into the repo root (the folder holding constants_new.py),
      open in VS Code, click Run.
      Or:  python patch_L247_4_repair.py

Built on cf588f1f6e0847653f6493985e5857a908fb0943
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Evidence: documentation/CONVERGENCE_L247_sgr_a_constants.md, over three
returns in documentation/worksheets/ from Claude Opus 5, GPT-5.6-sol
and Gemini 2.5 Pro. Two rulings by Tony, 2026-08-25: the most recent
publication is authoritative with previous values noted, and the solar
mass is derived from the IAU-exact GM rather than corrected in place.

WHAT CHANGES, AND WHAT MOVES

  GRAVITATIONAL_CONSTANT_SI  value unchanged. Gains CODATA 2022 and
                             three cross-check legs.
  GM_SUN_SI                  NEW primary. IAU 2015 Resolution B3, exact
                             by definition.
  SOLAR_MASS_KG              1.989e30 -> GM_SUN_SI / GRAVITATIONAL_
                             CONSTANT_SI = 1.9884098707e30. Moves
                             -0.0297%.
  PARSEC_TO_AU               206265.0 -> 206264.806247096. Moves
                             -9.4e-07 relative.
  SGR_A_MASS_SOLAR           4.154e6 -> 4.297e6 (GRAVITY 2022). Moves
                             +3.44%.
  SGR_A_DISTANCE_PC          NEW primary, 8277.0 pc, the quantity the
                             paper actually publishes.
  SGR_A_DISTANCE_LY          26670.0 -> derived, 26995.96 ly. Moves
                             +326 ly.

WHY THE FILE NOW HOLDS BOTH GM AND THE MASS

  The kilogram mass of the Sun is not measured. What is fixed is the
  product, and the IAU declares it exact. Before this patch the file
  held G and a rounded mass whose product was 0.030% off that exact
  quantity -- implicitly, where nothing watched it. Deriving the mass
  makes the product exact by construction and it cannot drift when
  CODATA next moves G. The same shape is applied to the distance: the
  published quantity is parsecs, so parsecs is what the file stores and
  light-years is what it derives.

  Both derived lines are NAME = EXPR over tracked names, which
  constants_change_report.py reads as DERIVED since patch_L248_1.

ONE VALUE ENTERS ON A SINGLE LEG

  4.297e6 was reached by the GPT return only. The Claude return noted
  that a 2022 successor exists without giving its numbers, and the
  Gemini return gave the 2022 distance in prose but not the mass. The
  annotation reflects that exactly: one # Cross-checked: line, and a
  # Review-note: saying a second leg is owed. Do not read the single
  leg as an oversight -- it is the state.

WHAT IS PERMANENT
  The constants and their annotations. The script is one-shot.

AFTER THIS RUN, in order:
  1. python constants_change_report.py

     EXIT 1 IS THE CORRECT RESULT HERE, and the run was read before
     this patch was delivered, so what it prints is stated rather than
     predicted:

       - PARSEC_TO_AU and SGR_A_MASS_SOLAR report AMBIGUOUS. git puts
         the whole Sgr A* block in one hunk at --unified=6, two values
         moved inside it, and the tool refuses to credit one provenance
         edit to either. That is the tool working; it is also why the
         run exits 1.
       - SOLAR_MASS_KG and SGR_A_DISTANCE_LY each report TWICE, once as
         REMOVED (the old literal) and once as DERIVED (the new
         expression). Both statements are true and the constants are
         not deleted. The tool keeps numeric and derived lines in
         separate buckets, so a name that crosses from one to the other
         appears in both.
       - GM_SUN_SI and SGR_A_DISTANCE_PC report NEW.

     What WOULD be a failure: 'VALUE MOVED ALONE' anywhere, or either
     derived line landing in the 'not understood' bucket.
  2. python maintenance_run.py
  3. Regenerate the Sgr A* views and hover the black hole marker
     (Mode 5). Expect 4.297 million solar masses and 26,996
     light-years. S4714's periapsis speed moves 8.24% -> 8.38% of c,
     which still renders as the 8% five prose strings state.

Success: one "ok" line per edit, then "patch applied".
Failure: a single "ERROR:" or "ANCHOR FAIL" line; nothing is written.
"""

import hashlib
import os
import sys

BASES = {
    'constants_new.py': 'bcd38f0e22d8a98f5c0b52738ec9c812',
    'sgr_a_star_data.py': 'e10cbdeccc443dff762eb6fe1bd0682d',
}

WORKSHEETS = os.path.join('documentation', 'worksheets')

# Every worksheet an annotation below names must exist. An annotation
# pointing at a plausible filename is cite-to-clear in the annotation's
# own format.
CITED_WORKSHEETS = (
    'worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md',
    'worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md',
    'worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md',
)


# ======================================================================
# constants_new.py
# ======================================================================

CN_HEADER_OLD = b"""# SAGITTARIUS A* AND GALACTIC-SCALE CONSTANTS
# Migrated 2026-08-25 from sgr_a_star_data.py under L-247. The values
# are unchanged; what changed is that there is now one of each.
"""

CN_HEADER_NEW = b"""# SAGITTARIUS A* AND GALACTIC-SCALE CONSTANTS
# Migrated 2026-08-25 from sgr_a_star_data.py under L-247, then sourced
# and repaired the same day against three independent returns
# (documentation/CONVERGENCE_L247_sgr_a_constants.md).
#
# Epoch policy, Tony's ruling 2026-08-25: the most recent publication
# that reports a value AS A RESULT is authoritative, and the value it
# replaces is recorded rather than overwritten. A later paper that
# merely carries the quantity as a fit parameter or quotes it in
# passing does not supersede the paper that measured it.
"""

CN_G_OLD = b"""GRAVITATIONAL_CONSTANT_SI = 6.67430e-11
# Note: units m^3 kg^-1 s^-2.
# Review-note: no source line travelled with this value from
#              sgr_a_star_data.py, where it carried only a units
#              comment. Routed to L-247 for a dispatch. Not cited here,
#              because a citation written to fill the gap would be a
#              provenance claim nobody checked.
"""

CN_G_NEW = b"""GRAVITATIONAL_CONSTANT_SI = 6.67430e-11
# Note: units m^3 kg^-1 s^-2. Measured, not exact: the relative standard
#       uncertainty is 2.2e-05, so a bare literal reads as more precise
#       than the quantity is.
# Source: CODATA 2022 -- Mohr, Newell, Taylor & Tiesinga (2025),
#         Rev. Mod. Phys. 97, 025002, doi:10.1103/RevModPhys.97.025002.
#         Published as 6.67430(15)e-11.
# Cross-checked: Claude 2026-08-25 -- CODATA 2022 (worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)
# Cross-checked: GPT 2026-08-25 -- CODATA 2022 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Cross-checked: Gemini 2026-08-25 -- CODATA 2018/2022 (worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)
# Note: the three legs agree on the value digit for digit and differ
#       only on which adjustment to name. The 2022 adjustment took in no
#       new competitive datum for G, so 2018 and 2022 publish the same
#       central value; 2022 is named here as the current authority.
"""

CN_MASS_OLD = b"""SOLAR_MASS_KG = 1.989e30
# Review-note: no source line travelled with this value. Routed to
#              L-247.
"""

CN_MASS_NEW = b"""GM_SUN_SI = 1.3271244e20
# Note: the nominal solar mass parameter, units m^3 s^-2. EXACT by
#       definition -- it is a conversion constant, not a measurement of
#       the Sun.
# Source: IAU 2015 Resolution B3, published as Prsa et al. (2016),
#         AJ 152, 41, doi:10.3847/0004-6256/152/2/41.
# Cross-checked: Claude 2026-08-25 -- IAU 2015 B3 (worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)
# Cross-checked: GPT 2026-08-25 -- IAU 2015 B3 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Cross-checked: Gemini 2026-08-25 -- IAU 2015 B3 (worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)

SOLAR_MASS_KG = GM_SUN_SI / GRAVITATIONAL_CONSTANT_SI
# Derived: 1.3271244e20 / 6.67430e-11 = 1.9884098707e30 kg.
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

CN_PARSEC_OLD = b"""PARSEC_TO_AU = 206265.0
# Review-note: no source line travelled with this value. It is the
#              small-angle arcseconds-per-radian figure and is used as a
#              bare literal in exoplanet_coordinates.py, swept to this
#              name by L-247. Routed for a dispatch.
"""

CN_PARSEC_NEW = b"""PARSEC_TO_AU = 206264.806247096
# Note: DEFINED, not measured. One parsec is the distance at which one
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
# Cross-checked: Claude 2026-08-25 -- IAU 2015 B2 (worksheet_claude-opus-5_L247_sgr_a_constants_20260825.md)
# Cross-checked: GPT 2026-08-25 -- IAU 2015 B2 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Cross-checked: Gemini 2026-08-25 -- IAU 2015 B2 (worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md)
# Note: written as a literal rather than as 648000.0/math.pi, following
#       SPEED_OF_LIGHT_KM_S, which is equally exact by definition and
#       equally written out. A math.pi expression would also be
#       unreadable to constants_change_report.py's DERIVED case, which
#       accepts only names tracked in this file.
# Note: this value carries the whole star pipeline once L-248 lands.
#       PARSEC_TO_AU / AU_PER_LIGHT_YEAR is 3.2615637772 with the exact
#       parsec and was 3.2615668 with the rounded one; the literal
#       3.26156 that L-248 sweeps is closer to the first.
"""

CN_SGRMASS_OLD = b"""SGR_A_MASS_SOLAR = 4.154e6
# Source: GRAVITY Collaboration 2019
# Review-note: the attribution above travelled with the value as an
#              inline comment and is carried here verbatim. It names no
#              paper, DOI or table, so it is a lead rather than a
#              citation. Routed to L-247.
"""

CN_SGRMASS_NEW = b"""SGR_A_MASS_SOLAR = 4.297e6
# Source: GRAVITY Collaboration (2022), "Mass distribution in the
#         Galactic Center based on interferometric astrometry of
#         multiple stellar orbits", A&A 657, L12,
#         doi:10.1051/0004-6361/202142465. Published as
#         4.297 +/- 0.012 (stat) +/- 0.040 (sys) e6 solar masses.
# Cross-checked: GPT 2026-08-25 -- GRAVITY Collaboration 2022 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
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

CN_DIST_OLD = b"""SGR_A_DISTANCE_LY = 26670.0
# Review-note: no source line travelled with this value. It was restated
#              as prose in two hover strings, which now derive from it.
#              Routed to L-247.
"""

CN_DIST_NEW = b"""SGR_A_DISTANCE_PC = 8277.0
# Note: parsecs is what the primary publications actually report. This
#       file stores the published quantity and derives the display one,
#       the same shape as GM_SUN_SI above.
# Source: GRAVITY Collaboration (2022), A&A 657, L12,
#         doi:10.1051/0004-6361/202142465. Published as
#         R_0 = 8277 +/- 9 (stat) pc, with a stated systematic near
#         30 pc.
# Cross-checked: GPT 2026-08-25 -- GRAVITY Collaboration 2022 (worksheet_gpt-5.6-sol_L247_sgr_a_constants_20260825.md)
# Review-note: the Gemini return states the same 8277 +/- 9 (stat)
#              +/- 30 (sys) pc in its Findings prose, attributing it to
#              "GRAVITY 2021" rather than 2022. Not counted as a second
#              leg here: it is prose rather than a verdicted row, and
#              the year disagrees with the journal reference. A second
#              leg is owed on this row too.
# Note: paired with SGR_A_MASS_SOLAR -- see the note on that row.

SGR_A_DISTANCE_LY = SGR_A_DISTANCE_PC * PARSEC_TO_AU / AU_PER_LIGHT_YEAR
# Derived: 8277 pc x 3.2615637772 ly/pc = 26995.963 light-years.
# Derived+: Previous hardcoded value was 26670.0, which is the 2019
#           R_0 of 8178 pc converted (26673.07) and rounded to four
#           significant figures. Inverted, 26670.0 ly is 8177.06 pc,
#           which matches no column of the 2019 Table 1.
# Note: the trailing .0 on the old literal asserted 0.1 ly against a
#       real uncertainty near 100 ly, overstated by three orders of
#       magnitude. Deriving removes the claim rather than restating it.
"""

CN_STAMP_OLD = b"""Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: 14
remaining CENTER_BODY_RADII bodies promoted to named constants; value
and citation carried forward unchanged from each dict entry)
"""

CN_STAMP_NEW = b"""Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162: 14
remaining CENTER_BODY_RADII bodies promoted to named constants; value
and citation carried forward unchanged from each dict entry)
Module updated: August 25, 2026 with Anthropic's Claude Opus 5 (L-247:
the five migrated Sgr A* and galactic-scale constants sourced against
three independent returns. GM_SUN_SI and SGR_A_DISTANCE_PC added as
sourced primaries; SOLAR_MASS_KG and SGR_A_DISTANCE_LY derived from
them; PARSEC_TO_AU given its exact definitional value; SGR_A_MASS_SOLAR
advanced from the 2019 to the 2022 GRAVITY determination under the
epoch policy recorded in the section header)
"""


# ======================================================================
# sgr_a_star_data.py -- the correction does not travel on its own
# ======================================================================

SD_CALC_OLD = b"""        # Calculation: with SGR_A_MASS_SOLAR = 4.154e6, Kepler's third law
        #              gives P = 11.1 yr for a = 800, against the 12.0 yr
        #              stored below. A 12.0 yr period needs a = 842 AU,
        #              which puts periapsis at 12.6. So 800 satisfies the
        #              periapsis label and not the period.
"""

SD_CALC_NEW = b"""        # Calculation: with SGR_A_MASS_SOLAR = 4.297e6, Kepler's third law
        #              gives P = 10.9 yr for a = 800, against the 12.0 yr
        #              stored below. A 12.0 yr period needs a = 852 AU,
        #              which puts periapsis at 12.8. So 800 satisfies the
        #              periapsis label and not the period.
        # Corrected: read 4.154e6 / 11.1 yr / 842 AU until 2026-08-25,
        #            when L-247 advanced the black hole mass to the 2022
        #            GRAVITY value. The gap this comment describes did
        #            not close; it widened slightly.
"""

SD_STAMP_OLD = b"""Module updated: April 15, 2026 with Anthropic's Claude Opus 4.6
\"\"\"
"""

SD_STAMP_NEW = b"""Module updated: April 15, 2026 with Anthropic's Claude Opus 4.6
Module updated: August 25, 2026 with Anthropic's Claude Opus 5 (L-247:
the S4714 Kepler note recomputed against the 2022 black hole mass)
\"\"\"
"""


EDITS = {
    'constants_new.py': [
        (CN_DIST_OLD, CN_DIST_NEW, 'SGR_A_DISTANCE_PC added, LY derived'),
        (CN_SGRMASS_OLD, CN_SGRMASS_NEW, 'SGR_A_MASS_SOLAR -> GRAVITY 2022'),
        (CN_PARSEC_OLD, CN_PARSEC_NEW, 'PARSEC_TO_AU -> exact definitional value'),
        (CN_MASS_OLD, CN_MASS_NEW, 'GM_SUN_SI added, SOLAR_MASS_KG derived'),
        (CN_G_OLD, CN_G_NEW, 'GRAVITATIONAL_CONSTANT_SI sourced (value unchanged)'),
        (CN_HEADER_OLD, CN_HEADER_NEW, 'section header: epoch policy'),
        (CN_STAMP_OLD, CN_STAMP_NEW, 'docstring: currency stamp'),
    ],
    'sgr_a_star_data.py': [
        (SD_CALC_OLD, SD_CALC_NEW, 'S4714 Kepler note recomputed'),
        (SD_STAMP_OLD, SD_STAMP_NEW, 'docstring: currency stamp'),
    ],
}


def fail(msg):
    print('ERROR: ' + msg)
    sys.exit(1)


def main():
    if not os.path.isdir(WORKSHEETS):
        fail('%s not found. Run this from the repo root.' % WORKSHEETS)

    # Worksheet first, annotation second. Every file a # Cross-checked:
    # line names must be on disk before the line is written.
    for name in CITED_WORKSHEETS:
        path = os.path.join(WORKSHEETS, name)
        if not os.path.exists(path):
            fail('%s does not exist. An annotation naming a worksheet '
                 'that is not there is cite-to-clear.' % path)
    print('ok  all 3 cited worksheets present in %s' % WORKSHEETS)

    staged = {}
    for filename, edits in EDITS.items():
        if not os.path.exists(filename):
            fail('%s not found. Run this from the repo root.' % filename)
        with open(filename, 'rb') as handle:
            data = handle.read()

        is_crlf = data.count(b'\r\n') > 0
        fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if fp != BASES[filename]:
            print('ERROR: BASE MOVED -- %s' % filename)
            print('  expected content fingerprint %s' % BASES[filename])
            print('  found                        %s' % fp)
            sys.exit(1)
        print('base ok  %-22s (%s)  %d bytes'
              % (filename, 'CRLF' if is_crlf else 'LF', len(data)))

        out = data
        for old, new, label in edits:
            o, n = old, new
            if is_crlf:
                o = o.replace(b'\n', b'\r\n')
                n = n.replace(b'\n', b'\r\n')
            bad = sorted({b for b in n if b > 127})
            if bad:
                fail('non-ASCII in inserted text (%s): %r' % (label, bad))
            count = out.count(o)
            if count != 1:
                print('ANCHOR FAIL (%d matches, expected 1) in %s: %s'
                      % (count, filename, label))
                print('  nothing written to any file.')
                sys.exit(1)
            out = out.replace(o, n)
            print('ok  %-22s %s' % (filename, label))
        staged[filename] = (data, out, is_crlf)

    # Post-conditions on constants_new.py, asserted before any write.
    text = staged['constants_new.py'][1].replace(b'\r\n', b'\n')
    for token, want in (
            (b'\nGM_SUN_SI = 1.3271244e20\n', 1),
            (b'\nSOLAR_MASS_KG = GM_SUN_SI / GRAVITATIONAL_CONSTANT_SI\n', 1),
            (b'\nSGR_A_DISTANCE_PC = 8277.0\n', 1),
            (b'\nSGR_A_DISTANCE_LY = SGR_A_DISTANCE_PC * PARSEC_TO_AU'
             b' / AU_PER_LIGHT_YEAR\n', 1),
            (b'\nSGR_A_MASS_SOLAR = 4.297e6\n', 1),
            (b'\nPARSEC_TO_AU = 206264.806247096\n', 1),
            (b'1.989e30\n', 0),
            (b'\nSGR_A_DISTANCE_LY = 26670.0\n', 0)):
        got = text.count(token)
        if got != want:
            fail('post-check: %r appears %d time(s), expected %d'
                 % (token[:60], got, want))
    print('ok  post-check: two new primaries, two new derivations, no '
          'stale literal')

    # A derived name must be DEFINED before it is USED. This is the one
    # ordering error the anchors cannot catch, and it is an ImportError
    # at runtime rather than a wrong number.
    for parent, child in ((b'GM_SUN_SI = ', b'SOLAR_MASS_KG = GM_SUN_SI'),
                          (b'PARSEC_TO_AU = 2062', b'SGR_A_DISTANCE_LY = '),
                          (b'AU_PER_LIGHT_YEAR = ', b'SGR_A_DISTANCE_LY = '),
                          (b'SGR_A_DISTANCE_PC = ', b'SGR_A_DISTANCE_LY = ')):
        if text.find(parent) > text.find(child):
            fail('post-check: %r is defined after it is used by %r'
                 % (parent, child))
    print('ok  post-check: every parent is defined above its derivation')

    for filename, (data, out, is_crlf) in staged.items():
        with open(filename, 'wb') as handle:
            handle.write(out)
        print('patch applied  %-22s %+d bytes  (%s)'
              % (filename, len(out) - len(data), 'CRLF' if is_crlf else 'LF'))

    print('')
    print('NEXT, in order:')
    print('  1. python constants_change_report.py')
    print('     EXIT 1 IS CORRECT here. PARSEC_TO_AU and')
    print('     SGR_A_MASS_SOLAR report AMBIGUOUS -- two values moved')
    print('     inside one git hunk, so the tool credits neither with')
    print('     the provenance edit. SOLAR_MASS_KG and')
    print('     SGR_A_DISTANCE_LY each report twice, REMOVED then')
    print('     DERIVED; both are true and neither is deleted.')
    print("     A 'VALUE MOVED ALONE' would be this patch failing.")
    print('  2. python maintenance_run.py')
    print('  3. Mode 5: regenerate the Sgr A* views and hover the black')
    print('     hole marker. Expect 4.297 million solar masses and')
    print('     26,996 light-years.')
    print('')
    print('OWED, and stated so it is not mistaken for finished:')
    print('  SGR_A_MASS_SOLAR and SGR_A_DISTANCE_PC each carry ONE')
    print('  cross-check leg. A second independent leg is owed on both.')


if __name__ == '__main__':
    main()
