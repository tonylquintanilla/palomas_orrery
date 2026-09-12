"""
patch_L305_magnetosphere_constants.py - L-305 Gap item 4, and the checker.

Run it:
    Save this file into the ORRERY repo root, together with
    test_status_lines.py, open it in VS Code and click Run.

FOUR files change, all or nothing. If any check below fails, NOTHING is
written to any of them.

  constants_new.py
    - Adds L-305's fifteen new rows: three declared solar wind
      conditions, Shue et al. (1998)'s eight magnetopause coefficients,
      Jelinek et al. (2012)'s three bow shock parameters, and the bow
      shock cut angle.
    - Supersedes EARTH_MAGNETOPAUSE_STANDOFF_RADII, 10.0 -> the Shue
      value at the declared conditions, and EARTH_BOW_SHOCK_STANDOFF_RADII,
      12.5 -> Jelinek's eq. 14 written as an EXPRESSION over the new
      constants rather than as a typed number.
    - Removes the bow shock's Lugaz-midpoint derivation, the Farris &
      Russell "Model form" miscitation, and the stale Note saying the
      shell's 15 R_E is a migration item.
    - Gives every row it writes a "# Unit:" line (L-322 ruling 1) and a
      "# Status:" line.
    - Fix in passing: RADIATIVE_ZONE_AU's existing status line reads
      "measured" with no rung, which the grammar requires. Its own block
      carries a Source and no cross-check, so the rung is V_SOURCED.
      Only the rung is added; whether "measured" is the right KIND for a
      row that multiplies a sourced literal by another constant is left
      for L-322's walk.

  earth_visualization_shells.py, shell_configs.py
    - Six hover and tooltip quotes interpolate the two standoffs with
      ":g", which prints six significant figures. The superseded values
      would read 10.2519 and 13.5117; both rows say to report 10.25 and
      13.51. ":.4g" prints exactly that. No words change.

  orrery_maintenance_run.py
    - Wires test_status_lines.py into the CHECKERS list.

It is one-shot. Each file is guarded by a fingerprint of its
LF-normalised content, so a second run aborts and writes nothing.

Undo is Discard Changes in GitHub Desktop.

Module created: September 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import py_compile
import sys
import tempfile

OLD_BLOCK = '''EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.0
# Source: Shue, J.-H. et al. (1998), "Magnetopause location under extreme
# Source+: solar wind conditions", J. Geophys. Res. 103, 17691-17700,
# Source+: doi:10.1029/98JA01103 -- r0 = 10.22 + 1.29 tanh(0.184(Bz+8.14))
# Source+: x Dp^(-1/6.6), which is 10.2 R_E at Bz = 0 nT, Dp = 2 nPa.
# Source+: Lugaz et al. (2016), doi:10.1038/ncomms13001 -- typical subsolar
# Source+: magnetopause 9-11 R_E.
# Note: the nominal quiet-time standoff. Under storm compression it can
# Note+: fall inside geostationary orbit (6.6 R_E); the drawn shape is
# Note+: the quiet one.

EARTH_BOW_SHOCK_STANDOFF_RADII = 12.5
# Source: Lugaz, N. et al. (2016), "Earth's magnetosphere and outer
# Source+: radiation belt under sub-Alfvenic solar wind", Nat. Commun. 7,
# Source+: 13001, doi:10.1038/ncomms13001 -- under normal solar wind the
# Source+: bow shock forms at a subsolar distance of 11-14 R_E.
# Derived: midpoint of the sourced 11-14 R_E range.
# Note: the orrery's bow shock conic stands off at 15 R_E, a textbook
# Note+: figure its own code comment already flags against the measured
# Note+: 11-14. The store holds the measured value; the shell's 15 is a
# Note+: migration item. Model form: Farris & Russell (1994), J. Geophys.
# Note+: Res. 99, 17681, doi:10.1029/94JA01020.
'''

NEW_BLOCK = '''# --- magnetosphere: two published models, L-305 (2026-09-12) ----------------
# The magnetopause is Shue et al. (1998), the bow shock is Jelinek et al.
# (2012). They are separate fits in separate frames -- Shue in aberrated GSM,
# Jelinek in aberrated GSE -- and both are rotationally symmetric about the
# aberrated Sun-Earth line, so the two frames share the X axis and nothing
# drawn depends on the difference. Do not "fix" a frame mismatch here; there
# is none to fix. The two models disagree about the magnetopause nose by
# about 1 R_E (Shue 10.25, Jelinek 11.24), which is inside Shue's own fit
# scatter of 1.23 R_E, and the hovers say so rather than letting the pair
# read as one measurement.
#
# The declared conditions come first because the standoffs are evaluated at
# them. L-314 replaces all three with a measured feed.

EARTH_SOLAR_WIND_PRESSURE_NPA = 2.0
# Unit: npa
# Status: declared pending 2026-09-12 -- L-314
# Declared: the solar wind dynamic pressure both fits are evaluated at.
# Declared+: Shue et al. (1998) p. 17,695 uses Dp = 2 nPa as an average
# Declared+: value, which is the paper's own reason for this pick. It sits
# Declared+: inside Shue's fitted range (0.5 to 8.5 nPa, p. 17,693) and
# Declared+: inside Jelinek's recommended range (0.6 to 11 nPa, conclusion
# Declared+: para. 30).
# Note: Shue's Dp includes the helium contribution by the factor
# Note+: (1 + 0.04 N_alpha), where N_alpha is the He++ concentration as a
# Note+: PERCENTAGE, 4 percent being used when it is missing -- so a factor
# Note+: of 1.16, not 1.0016 (fig. 1 caption, p. 17,692). A feed reporting
# Note+: proton density alone inherits that assumption. See L-314.

EARTH_SOLAR_WIND_BZ_NT = 0.0
# Unit: nt
# Status: declared pending 2026-09-12 -- L-314
# Declared: a neutral midpoint chosen here, NOT a figure from the paper.
# Declared+: Shue's own averages are +/- 4 nT, northward and southward taken
# Declared+: separately (p. 17,695). Zero is the unloaded case the drawn
# Declared+: shape shows, and it sits inside the fitted range
# Declared+: -18 nT < Bz < 15 nT (p. 17,693).

EARTH_SOLAR_WIND_SPEED_KM_S = 400.0
# Unit: km_s
# Status: declared pending 2026-09-12 -- L-314
# Declared: a nominal speed whose reason is NOT YET WRITTEN, and that is the
# Declared+: honest state of this row. The 410 km/s on Shue p. 17,694 is the
# Declared+: speed during one January 1997 event and does not source a
# Declared+: nominal figure.
# Note: neither standoff depends on this. It sets the aberration angle,
# Note+: atan(v_orbit / v_sw), about 4.3 degrees at this value.

EARTH_MAGNETOPAUSE_SHUE_A1_RADII = 10.22
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue, J.-H., Song, P., Russell, C. T., Steinberg, J. T., Chao,
# Source+: J. K., Zastenker, G., Vaisberg, O. L., Kokubun, S., Singer, H. J.,
# Source+: Detman, T. R. and Kawano, H. (1998), "Magnetopause location under
# Source+: extreme solar wind conditions", J. Geophys. Res. 103(A8),
# Source+: 17691-17700, doi:10.1029/98JA01103 -- Table 1 "After Fit" row a1,
# Source+: p. 17,698: 10.22 +/- 0.10 R_E. The leading term of eq. 10.
# Access: open full text, https://doi.org/10.1029/98JA01103, read from the
# Access+: PDF 2026-09-11. Sandbox fetches of the DOI page are refused by bot
# Access+: detection, which is not a paywall; the download was Tony's.
# Record: documentation/L305_gap1_read_record_20260911.md
# Note: eq. 10, p. 17,697, is the standoff --
# Note+: r0 = {a1 + a2 tanh[a3 (Bz + a4)]} Dp^(-1/a5), with Bz in nT, Dp in
# Note+: nPa and r0 in Earth radii. The +/- figures on rows a1 to a8 are
# Note+: standard deviations from 200 Monte Carlo refits (p. 17,698).

EARTH_MAGNETOPAUSE_SHUE_A2_RADII = 1.29
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a2, p. 17,698: 1.29 +/- 0.06 R_E. The amplitude of eq. 10's
# Source+: Bz term.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A3_PER_NT = 0.184
# Unit: per_nt
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a3, p. 17,698: 0.184 +/- 0.007 per nT. The scale inside
# Source+: eq. 10's hyperbolic tangent.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A4_NT = 8.14
# Unit: nt
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a4, p. 17,698: 8.14 +/- 0.39 nT. The Bz offset inside
# Source+: eq. 10's hyperbolic tangent.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A5 = 6.6
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a5, p. 17,698: 6.6 +/- 0.5. The pressure exponent, r0 varying
# Source+: as Dp^(-1/a5).
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Note: the name carries no unit suffix because the value has no unit. The
# Note+: "# Unit:" line above is the declaration; nothing is renamed to suit
# Note+: a reader of names (L-322).

EARTH_MAGNETOPAUSE_SHUE_A6 = 0.58
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a6, p. 17,698: 0.58 +/- 0.01. The leading term of eq. 11.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Note: eq. 11, p. 17,697, is the flaring --
# Note+: alpha = (a6 + a7 Bz) [1 + a8 ln(Dp)], and the surface is then
# Note+: r = r0 [2 / (1 + cos theta)]^alpha, theta measured from the
# Note+: aberrated Sun-Earth line.

EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT = -0.007
# Unit: per_nt
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a7, p. 17,698: -0.007 +/- 0.0005 per nT. Eq. 11 prints it as
# Source+: the subtraction (0.58 - 0.007 Bz); the table carries the sign, so
# Source+: the stored coefficient is negative and adds.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).

EARTH_MAGNETOPAUSE_SHUE_A8 = 0.024
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Shue et al. (1998), doi:10.1029/98JA01103 -- Table 1 "After Fit"
# Source+: row a8, p. 17,698: 0.024 +/- 0.0004. The pressure term of eq. 11.
# Access: open full text, https://doi.org/10.1029/98JA01103 (2026-09-11).
# Note: the Kumar and Pulkkinen EGUsphere preprint (2024-1113) prints this
# Note+: as 0.24. That is a typo in the preprint; the primary says 0.024.
# Note+: Recorded so nobody re-derives the doubt.

EARTH_BOW_SHOCK_JELINEK_R0_RADII = 15.02
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-10 -- open full text
# Source: Jelinek, K., Nemecek, Z. and Safrankova, J. (2012), "A new
# Source+: approach to magnetopause and bow shock modeling based on automated
# Source+: region identification", J. Geophys. Res. 117, A05208,
# Source+: doi:10.1029/2011JA017252 -- eq. 14, p. 5: R_BS = 15.02 p^(-1/6.55),
# Source+: so 15.02 R_E is the bow shock stand-off at p = 1 nPa. Fitted from
# Source+: Themis crossings, in aberrated GSE.
# Access: open full text, https://doi.org/10.1029/2011JA017252, read from the
# Access+: PDF 2026-09-10.
# Record: documentation/L305_gap1_read_record_20260911.md
# Note: the paper states no uncertainty on its six fitted numbers. It gives
# Note+: the scatter of crossings about the model instead -- fig. 7, 0.69 R_E
# Note+: for the bow shock and 0.76 R_E for the magnetopause.
# Note+: Do NOT pick up eqs. 17-18 (12.90 and 14.94). Those are a validation
# Note+: refit against observed crossings (sec. 5.2), not the model, and the
# Note+: two pairs are close enough to be mistaken for one another.

EARTH_BOW_SHOCK_JELINEK_EPS = 6.55
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-10 -- open full text
# Source: Jelinek et al. (2012), doi:10.1029/2011JA017252 -- eq. 14, p. 5:
# Source+: the pressure exponent of R_BS = 15.02 p^(-1/6.55).
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-10).

EARTH_BOW_SHOCK_JELINEK_LAMBDA = 1.17
# Unit: dimensionless
# Status: measured V_SOURCED 2026-09-10 -- open full text
# Source: Jelinek et al. (2012), doi:10.1029/2011JA017252 -- sec. 4, in the
# Source+: text after eq. 11: lambda = 1.17 for the bow shock (1.54 for the
# Source+: magnetopause, which this file does not store because the
# Source+: magnetopause is Shue's).
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-10).
# Note: the per-boundary scaling of the parabolic surface, eqs. 15-16:
# Note+: x = R0 p^(-1/eps) - tau^2 / 2 and
# Note+: R_yz = sqrt(2 R0 p^(-1/eps)) tau / lambda.

EARTH_BOW_SHOCK_CUT_ANGLE_DEG = 105.0
# Unit: deg
# Status: measured V_SOURCED 2026-09-11 -- open full text
# Source: Jelinek et al. (2012), doi:10.1029/2011JA017252 -- sec. 2 para. 9,
# Source+: p. 2: the regions are identified on the whole dayside and toward
# Source+: the flanks within +/- 7 hours of local time about local noon.
# Source+: That envelope is the extent over which the fit is supported.
# Derived: 7 h x 15 deg/h = 105 deg from the nose. The paper gives the
# Derived+: hours; the degrees are this file's conversion, exact by
# Derived+: definition (360 deg / 24 h). Same shape as EARTH_GM_KM3_S2,
# Derived+: which converts IERS's m^3 s^-2 and stays one measured row.
# Access: open full text, https://doi.org/10.1029/2011JA017252 (2026-09-11).
# Note: the drawn bow shock stops here. Beyond it the paraboloid is
# Note+: unsupported -- it reaches 67 R_E at x = -100 R_E -- and the real
# Note+: shock follows a Mach cone the paper does not model. At the declared
# Note+: pressure the cut falls at x = -7.8 R_E, R_yz = 29.0 R_E.

EARTH_MAGNETOPAUSE_STANDOFF_RADII = 10.251872972379905
# Unit: r_earth
# Status: derived 2026-09-12 -- inherits EARTH_MAGNETOPAUSE_SHUE_A1_RADII
# Status+: through EARTH_MAGNETOPAUSE_SHUE_A5, EARTH_SOLAR_WIND_PRESSURE_NPA
# Status+: and EARTH_SOLAR_WIND_BZ_NT
# Derived: Shue eq. 10 at the declared conditions --
# Derived+: (a1 + a2 tanh[a3 (Bz + a4)]) Dp^(-1/a5)
# Derived+: = (10.22 + 1.29 tanh(0.184 x 8.14)) x 2^(-1/6.6)
# Derived+: = 10.251872972379905.
# Derived+: REPORT 10.25. Table 1 gives a1 to +/- 0.10 R_E and a5 to
# Derived+: +/- 0.5, and either one alone moves r0 by about +/- 0.09, so the
# Derived+: fourth figure is the last one the coefficients support.
# Note: typed as a literal rather than written as the expression it is,
# Note+: because the gallery's store parser evaluates only + - * / and **.
# Note+: A tanh assignment is left out of the parsed set, and the drift check
# Note+: then reports the pointer as NOT IN STORE. That is announced rather
# Note+: than silent, but it carries the wrong reason ("not a top-level
# Note+: constant"), it does not gate, and the value stops being compared at
# Note+: all. L-322 retires that parser and this becomes an expression then;
# Note+: the digits here are the expression's own value, so that swap
# Note+: changes nothing.
# Note+: Superseded a typed 10.0 on 2026-09-12 (L-305). The old row's own
# Note+: Source already read 10.2 R_E at these conditions while the value
# Note+: read 10.0 -- a drift inside one row, cleared here.
# Note+: Quiet-time. Under storm compression the magnetopause can fall
# Note+: inside geostationary orbit (6.6 R_E); the drawn shape is the quiet
# Note+: one. Lugaz et al. (2016), doi:10.1038/ncomms13001, gives 9-11 R_E
# Note+: as the typical subsolar distance, which contains this.

EARTH_BOW_SHOCK_STANDOFF_RADII = (
    EARTH_BOW_SHOCK_JELINEK_R0_RADII
    * EARTH_SOLAR_WIND_PRESSURE_NPA ** (-1.0 / EARTH_BOW_SHOCK_JELINEK_EPS))
# Unit: r_earth
# Status: derived 2026-09-12 -- inherits EARTH_BOW_SHOCK_JELINEK_R0_RADII,
# Status+: EARTH_BOW_SHOCK_JELINEK_EPS and EARTH_SOLAR_WIND_PRESSURE_NPA
# Derived: Jelinek eq. 14 at the declared pressure -- 15.02 x 2^(-1/6.55)
# Derived+: = 13.511736110493397. REPORT 13.51: the paper states no
# Derived+: uncertainty on R0 or eps, so what bounds this is the crossing
# Derived+: scatter, 0.69 R_E (fig. 7).
# Note: superseded a typed 12.5 on 2026-09-12 (L-305). Two claims went with
# Note+: it. The value was the midpoint of Lugaz et al. (2016)'s 11-14 R_E,
# Note+: which is not a model; and the shape was cited to Farris & Russell
# Note+: (1994), doi:10.1029/94JA01020, which is a semiempirical relation for
# Note+: the STANDOFF at a given Mach number and takes obstacle shape as an
# Note+: INPUT -- so citing it for a shape was a miscitation. Lugaz's
# Note+: 11-14 R_E survives as a corroborating range and this value sits
# Note+: inside it.
# Note+: The stale Note saying the shell draws 15 R_E is gone too:
# Note+: earth_visualization_shells.py has read this constant since L-291.
'''

STAMP_ANCHOR = """Derived quotients are held at full float precision and REPORTED
to the significant figures their least precise input supports)
\"\"\"
"""

STAMP_NEW = """Derived quotients are held at full float precision and REPORTED
to the significant figures their least precise input supports)
Module updated: September 12, 2026 with Anthropic's Claude Opus 5
(L-305 Gap item 4: Earth's magnetosphere rebuilt on two published
models. Fifteen rows added -- three declared solar wind conditions,
Shue et al. (1998)'s eight magnetopause coefficients, Jelinek et al.
(2012)'s three bow shock parameters and the bow shock cut angle. The
two standoffs are superseded and are now derived from those rows
rather than typed. A Lugaz-midpoint derivation and a Farris & Russell
"Model form" miscitation are removed. Every row written here carries a
"# Unit:" line, the fifteenth comment key, per L-322 ruling 1)
\"\"\"
"""

RADIATIVE_OLD = "# Status: measured 2026-08-29 -- verified against the source\n"
RADIATIVE_NEW = ("# Status: measured V_SOURCED 2026-08-29 -- verified against "
                 "the source\n")

RUNNER_OLD = """    ('Citation inheritance', ['test_citation_inheritance.py'], None),
    ('Scanner recognition 1d/1e', ['test_provenance_1d.py'], None),
"""

RUNNER_NEW = """    ('Citation inheritance', ['test_citation_inheritance.py'], None),
    ('Status lines', ['test_status_lines.py'], None),
    ('Scanner recognition 1d/1e', ['test_provenance_1d.py'], None),
"""

MAGNETOPAUSE_G = "EARTH_MAGNETOPAUSE_STANDOFF_RADII:g}"
MAGNETOPAUSE_4G = "EARTH_MAGNETOPAUSE_STANDOFF_RADII:.4g}"
BOW_SHOCK_G = "EARTH_BOW_SHOCK_STANDOFF_RADII:g}"
BOW_SHOCK_4G = "EARTH_BOW_SHOCK_STANDOFF_RADII:.4g}"

# --- retired claims leaving the four visitor-facing strings (L-305) ---------
# Deletion and correction only. Nothing new is said; the sentences that make
# the new numbers false are removed and two attributions are corrected. The
# rewrite that explains the models is L-305 item 7, after L-321's verdicts.

MAGNETOSPHERE_SRC_OLD = '''                 "Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691; "
                 "Lugaz et al. (2016), Nat. Commun. 7:13001."]'''
MAGNETOSPHERE_SRC_NEW = '''                 "Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691."]'''

BOW_SHOCK_MIDPOINT_OLD = '''                "Drawn at the midpoint of the 11-14 R_E measured under normal solar wind (Lugaz et al. 2016).<br>"
'''
BOW_SHOCK_MIDPOINT_NEW = ""

BOW_SHOCK_SRC_OLD = '''                "Source (standoff): Lugaz et al. (2016), Nat. Commun. 7:13001, doi:10.1038/ncomms13001."]'''
BOW_SHOCK_SRC_NEW = '''                "Source (standoff): Jelinek et al. (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252."]'''

SHELL_COMMENT_OLD = """    # L-291: was a typed 15 R_E (textbook) with a comment conceding the
    # measured 11-14. The store now holds the measured midpoint; see
    # EARTH_BOW_SHOCK_STANDOFF_RADII in constants_new.py for the source.
"""
SHELL_COMMENT_NEW = """    # L-291: was a typed 15 R_E (textbook) with a comment conceding the
    # measured 11-14. L-305: the midpoint is retired; the store now holds
    # Jelinek et al. (2012) eq. 14 at the declared pressure. See
    # EARTH_BOW_SHOCK_STANDOFF_RADII in constants_new.py for the source.
"""

TOOLTIP_SRC_OLD = '''                "Standoffs: Shue et al. (1998); Lugaz et al. (2016).\\n\\n"'''
TOOLTIP_SRC_NEW = '''                "Standoffs: Shue et al. (1998); Jelinek et al. (2012).\\n\\n"'''

# --- currency stamps, one per edited file -----------------------------------

SHELLS_STAMP_OLD = """    much as in code, and a literal in dead code is still a store.
\"\"\"
"""
SHELLS_STAMP_NEW = """    much as in code, and a literal in dead code is still a store.
September 12, 2026 (L-305, Opus 5): the two magnetosphere standoffs are
    superseded in constants_new.py -- Shue et al. (1998) for the
    magnetopause, Jelinek et al. (2012) for the bow shock -- so the six
    quotes of them here round to the reporting figure their rows state,
    the retired Lugaz-midpoint sentence is deleted, and the bow shock's
    source attribution moves from Lugaz to Jelinek. Deletion and
    correction only; the rewrite is item 7.
\"\"\"
"""

CONFIGS_STAMP_OLD = """    Tony's ruling, 2026-09-07.)
\"\"\"
"""
CONFIGS_STAMP_NEW = """    Tony's ruling, 2026-09-07.)
Module updated: September 12, 2026 with Anthropic's Claude Opus 5 (L-305:
    Earth's magnetosphere tooltip quotes the two superseded standoffs at
    the reporting figure their store rows state, and its standoff
    attribution moves from Lugaz to Jelinek.)
\"\"\"
"""

RUNNER_STAMP_OLD = """Module created: August 2026 with Anthropic's Claude Opus 5.
\"\"\"
"""
RUNNER_STAMP_NEW = """Module created: August 2026 with Anthropic's Claude Opus 5.
Module updated: September 2026 with Anthropic's Claude Opus 5 (L-305: the
CHECKERS list gains test_status_lines.py, which enforces the Status Line
grammar on every constants_new.py row that carries one.)
\"\"\"
"""

# filename -> (md5 of LF-normalised content, [(label, old, new, count)])
FILES = [
    ("constants_new.py", "3b4c9d4b4a45d6d9033bae5ee7d3a26d", [
        ("two standoff rows -> 15 new rows plus 2 supersessions",
         OLD_BLOCK, NEW_BLOCK, 1),
        ("module docstring stamp", STAMP_ANCHOR, STAMP_NEW, 1),
        ("RADIATIVE_ZONE_AU status line gains its rung",
         RADIATIVE_OLD, RADIATIVE_NEW, 1),
    ]),
    ("earth_visualization_shells.py", "b960913ae73e1e311976dc0576c11c22", [
        ("magnetopause hover quotes round to 4 figures",
         MAGNETOPAUSE_G, MAGNETOPAUSE_4G, 2),
        ("bow shock hover quotes round to 4 figures",
         BOW_SHOCK_G, BOW_SHOCK_4G, 2),
        ("Lugaz leaves the magnetosphere standoff source line",
         MAGNETOSPHERE_SRC_OLD, MAGNETOSPHERE_SRC_NEW, 1),
        ("the Lugaz-midpoint sentence is deleted from the bow shock hover",
         BOW_SHOCK_MIDPOINT_OLD, BOW_SHOCK_MIDPOINT_NEW, 1),
        ("the bow shock standoff source becomes Jelinek",
         BOW_SHOCK_SRC_OLD, BOW_SHOCK_SRC_NEW, 1),
        ("the stale 'measured midpoint' code comment is corrected",
         SHELL_COMMENT_OLD, SHELL_COMMENT_NEW, 1),
        ("currency stamp", SHELLS_STAMP_OLD, SHELLS_STAMP_NEW, 1),
    ]),
    ("shell_configs.py", "ab8ba1d169ab3a61718d3a0239981a70", [
        ("magnetopause tooltip quote rounds to 4 figures",
         MAGNETOPAUSE_G, MAGNETOPAUSE_4G, 1),
        ("bow shock tooltip quote rounds to 4 figures",
         BOW_SHOCK_G, BOW_SHOCK_4G, 1),
        ("the tooltip standoff attribution becomes Jelinek",
         TOOLTIP_SRC_OLD, TOOLTIP_SRC_NEW, 1),
        ("currency stamp", CONFIGS_STAMP_OLD, CONFIGS_STAMP_NEW, 1),
    ]),
    ("orrery_maintenance_run.py", "6de4c8571a08dec45fc62d51f4ae52ef", [
        ("wire test_status_lines.py into the CHECKERS list",
         RUNNER_OLD, RUNNER_NEW, 1),
        ("currency stamp", RUNNER_STAMP_OLD, RUNNER_STAMP_NEW, 1),
    ]),
]

ABORT = "       NOTHING was written to any file. Undo: Discard Changes."


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    companion = os.path.join(here, "test_status_lines.py")
    if not os.path.exists(companion):
        print("ERROR: test_status_lines.py is not beside this script, and")
        print("       this patch wires the maintenance run to call it. Save")
        print("       both files into the orrery repo root, then run again.")
        print(ABORT)
        return 1

    staged = []
    for name, fingerprint, edits in FILES:
        path = os.path.join(here, name)
        if not os.path.exists(path):
            print("ERROR: %s is not beside this script. Put this file in the"
                  % name)
            print("       orrery repo root and run it there.")
            print(ABORT)
            return 1
        raw = open(path, "rb").read()
        was_crlf = b"\r\n" in raw
        content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
        actual = hashlib.md5(content).hexdigest()
        if actual != fingerprint:
            print("ERROR: base moved. %s content md5 is %s," % (name, actual))
            print("       this patch was built against %s." % fingerprint)
            print(ABORT)
            return 1
        print("ok   %-32s fingerprint matches%s"
              % (name, " [CRLF]" if was_crlf else ""))
        staged.append([path, name, content, was_crlf, edits, len(raw)])

    for entry in staged:
        path, name, content, was_crlf, edits, was_bytes = entry
        out = content
        for label, old, new, expected in edits:
            old_b = old.encode("ascii")
            found = out.count(old_b)
            if found != expected:
                print("ANCHOR FAIL: %s -- %s matched %d times, expected %d."
                      % (name, label, found, expected))
                print(ABORT)
                return 1
            out = out.replace(old_b, new.encode("ascii"))
            print("ok   %-32s %s" % (name, label))
        entry[2] = out

    for path, name, out, was_crlf, edits, was_bytes in staged:
        try:
            out.decode("ascii")
        except UnicodeDecodeError as exc:
            print("ANCHOR FAIL: %s is not ASCII after the edit (%s)."
                  % (name, exc))
            print(ABORT)
            return 1
        probe = os.path.join(tempfile.gettempdir(), "_probe_" + name)
        open(probe, "wb").write(out)
        try:
            py_compile.compile(probe, doraise=True)
        except py_compile.PyCompileError as exc:
            print("ANCHOR FAIL: %s does not compile (%s)." % (name, exc))
            print(ABORT)
            return 1
        finally:
            if os.path.exists(probe):
                os.remove(probe)
    print("ok   encoding gate: all four ASCII clean and compiling")

    for path, name, out, was_crlf, edits, was_bytes in staged:
        final = out.replace(b"\n", b"\r\n") if was_crlf else out
        with open(path, "wb") as handle:
            handle.write(final)
        print("     wrote %-32s %d bytes, was %d"
              % (name, len(final), was_bytes))

    print("")
    print("patch applied to 4 files")
    print("     stamped: all four module docstrings")
    print("")
    print("NEXT: run orrery_maintenance_run.py (Run button). Expect a new")
    print("      'Status lines' row reading 19 checked, 0 failed, and")
    print("      'Constants change' reporting the two standoffs moving,")
    print("      which is this patch. Then commit and push, and report the")
    print("      SHA -- the gallery patch is built against it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
