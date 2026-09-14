"""
patch_L305_item7_belt_rows.py

L-305 item 7, part 1 of 3: the STORE. Writes the Van Allen belt edges and
the observed magnetotail extent into constants_new.py as rows, and
corrects the two peak rows that have been carrying the spans in prose.

WHAT IT DOES (one file: constants_new.py)
  1. EARTH_VAN_ALLEN_INNER_RADII (the inner peak) gains "# Unit: r_earth"
     and a status line, keeps Baker as its source with the frame stated,
     and LOSES the span from its "# Note:" -- the span is now four rows
     of its own. The second reading of 1.5 in L stays, recorded as a
     different frame rather than as agreement.
  2. EARTH_VAN_ALLEN_OUTER_RADII (the outer peak) gains "# Unit: l_shell"
     and "# Status: declared", because 4.5 is the midpoint of an L band
     and a pick from a range is a declared choice. Baker comes OFF this
     row's citation: a checker found his L* = 4.5 is a selected analysis
     location, not a universal peak. His span figure moves to the outer
     edge row, where it belongs.
  3. Four new rows hold the belt edges, in geocentric Earth radii in the
     geomagnetic equatorial plane, each naming the paper its figure
     follows. Tony's ruling of 2026-09-14.
  4. One new row holds the observed magnetotail extent, 220 R_E, read as
     "observed to at least" -- the same form as EARTH_GEOCORONA_RADII,
     which it is inserted above.

WHAT IT DOES NOT DO
  Nothing outside constants_new.py. The hover strings, the info panel and
  the gallery config still hold their typed copies; those are parts 2 and
  3 of item 7. Between this patch and part 2 the strings and the store
  disagree, which is expected and is why the three parts run in one
  sitting.

WHY THESE VALUES
  documentation/DESIGN_a_figure_in_prose_needs_a_home_rev3_20260914.md
  carries the design and the reasoning. The verdicts behind it are in
  documentation/worksheets/ (three legs on worksheet 3, one recheck on
  worksheet 1) and documentation/FINDING_L321_source_recovery_20260913.md.

HOW TO RUN IT (Tony)
  Save this file into the orrery repo root -- the same folder as
  constants_new.py -- open it in VS Code, and click Run.
  Equivalent command: python patch_L305_item7_belt_rows.py

  Success: four "ok" lines, then "patch applied" and a row count.
  Failure: one ERROR or ANCHOR FAIL line. NOTHING is written. Undo is
           Discard Changes in GitHub Desktop.

AFTER IT RUNS
  1. Run test_status_lines.py (Run button). It should report no failures
     and name the new rows among the declared and measured ones.
  2. Run provenance_scanner.py if you want the audit refreshed; this
     patch adds sourced rows, so Tier-1 should not rise.

BASE
  Built on orrery 2f1a0c2f03a15927a6667bf4297f2a07991bfdfe at
  https://github.com/tonylquintanilla/palomas_orrery
  The guard fingerprints the whole file; constants_new.py has no
  generated zone.

Written September 14, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "constants_new.py"
BASE_FP = "a05c0e62ba0fd743549e5a293b14a83c"

# ---------------------------------------------------------------------------
# Edit 1 (lowest in the file): the observed magnetotail extent, inserted
# immediately above EARTH_GEOCORONA_RADII, whose "detected to at least" form
# it follows.
# ---------------------------------------------------------------------------

TAIL_ANCHOR = b"EARTH_GEOCORONA_RADII = 100.0\n"

TAIL_NEW = b'''EARTH_MAGNETOTAIL_OBSERVED_RADII = 220.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- abstract, open
# Source: Slavin, J. A., Tsurutani, B. T., Smith, E. J., Jones, D. E. and
# Source+: Sibeck, D. G. (1983), "Average configuration of the distant (less
# Source+: than 220-earth-radii) magnetotail - Initial ISEE-3 magnetic field
# Source+: results", Geophys. Res. Lett. 10(10), 973-976,
# Source+: doi:10.1029/GL010i010p00973 -- the abstract states that the
# Source+: magnetotail retains much of its near-Earth structure out to
# Source+: X = -220 Earth radii, that flaring ceases at 100-120 R_E, and
# Source+: that the tail diameter settles near 60 R_E.
# Access: abstract, open, https://ntrs.nasa.gov/citations/19830066648
# Access+: (NTRS document 19830066648, read 2026-09-14). The Wiley pages are
# Access+: walled. The NTRS abstract prints "-100 to -1200 earth radii" where
# Access+: -120 is meant.
# Note: read as OBSERVED TO AT LEAST, the same form as EARTH_GEOCORONA_RADII
# Note+: below. 220 R_E is ISEE-3's reach on its first two tail passes, not
# Note+: an edge: the tail kept its near-Earth structure out to the
# Note+: spacecraft's apogee, so the figure is bounded by the orbit.
# Note+: Two further signatures are recorded here so a later session does not
# Note+: read this row as ignorance of them. Both are more distant and less
# Note+: like a tail, which is why neither is the value.
# Note+: Ness, N. F., Scearce, C. S. and Cantarano, S. C. (1967), "Probable
# Note+: observations of the geomagnetic tail at 10^3 Earth radii by Pioneer
# Note+: 7", J. Geophys. Res. 72(15), 3769-3776,
# Note+: doi:10.1029/JZ072i015p03769 -- Pioneer 7 was in the expected tail
# Note+: region at 900 to 1,050 R_E from 26 September to 3 October 1966, with
# Note+: tail-like fields appearing intermittently and no coherent,
# Note+: well-ordered tail observed. The title says "probable". Open as GSFC
# Note+: preprint X-612-67-183,
# Note+: https://ntrs.nasa.gov/citations/19670023428
# Note+: Intriligator, D. S. et al. (1979), Geophys. Res. Lett. 6, 585 --
# Note+: tail-ASSOCIATED phenomena near 3,100 R_E, read by later work as
# Note+: signatures disconnected from Earth rather than a tail. Abstract
# Note+: open, https://ntrs.nasa.gov/citations/19790061874
# Note+: The DRAWN tail length is 100 R_E, a drawing parameter at
# Note+: earth_visualization_shells.py line 765, and it is NOT promoted here
# Note+: (A Drawing Approximation Does Not Promote). It sits inside the
# Note+: coherent range this row records.
# Record: documentation/worksheets/L321_worksheet_1_magnetopause_fable_high_recheck_20260913.md

EARTH_GEOCORONA_RADII = 100.0
'''

# ---------------------------------------------------------------------------
# Edit 2: the four belt edge rows, inserted above the magnetosphere block.
# ---------------------------------------------------------------------------

EDGES_ANCHOR = (
    b"# --- magnetosphere: two published models, L-305 (2026-09-12) "
    b"----------------\n"
)

EDGES_NEW = b'''# --- Van Allen belt edges, L-305 item 7 (2026-09-14) ------------------------
# The spans used to live in each peak row's "# Note:" line, as prose, while
# the hovers, the information panel and the gallery config each typed their
# own copy. A Note became a store. These rows hold the figures instead, so a
# string can interpolate one and a checker can compare them.
#
# FRAME: geocentric, in the geomagnetic equatorial plane. That is the frame
# the cited papers state, and Tony ruled on 2026-09-14 that the store holds
# it. The literature is mixed -- Y. X. Li et al. (2023) states the outer
# span in L shells and Baker et al. (2018) states it both ways -- so "the
# frame the source states" only answers once the row names WHICH source its
# figure follows. Each row does, and the frame travels with it.
#
# Design record:
# documentation/DESIGN_a_figure_in_prose_needs_a_home_rev3_20260914.md

EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE = 1.1
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith, N. P., Horne, R. B., Kersten, T., Fraser, B. J. and
# Source+: Grew, R. S. (2014), "Global morphology and spectral properties of
# Source+: EMIC waves derived from CRRES observations", J. Geophys. Res.
# Source+: Space Physics 119, 5328-5342, doi:10.1002/2014JA020064 --
# Source+: introduction, first paragraph: the inner belt extends from about
# Source+: 1.1 to 2 Earth radii in the geomagnetic equatorial plane.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf
# Access+: (2026-09-13).
# Note: Meredith states this as background and passes it on from Baker et
# Note+: al. (2007), which is the layer below rather than the source.
# Note+: Koskinen and Kilpua (2022) sec. 1.1 corroborate 1.1 to 2 R_E, and
# Note+: are NOT this row's source, because they state it for the inner
# Note+: ELECTRON belt; the same section puts the energetic protons over
# Note+: about 1.1 to 3 R_E, so they cannot carry a hover calling this belt
# Note+: mainly protons. The figure matched and the scope did not.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE = 2.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith et al. (2014), doi:10.1002/2014JA020064 -- introduction,
# Source+: first paragraph, the outer end of the same stated span.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf
# Access+: (2026-09-13).
# Note: two rows rather than a tuple, because provenance is per number and
# Note+: the two edges do not move together. The layer below is Baker et al.
# Note+: (2007), as above.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE = 3.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith et al. (2014), doi:10.1002/2014JA020064 -- introduction,
# Source+: first paragraph: the outer belt extends from 3 to 7 R_E. Li, Tu,
# Source+: Selesnick and Huang (2024), "Modeling the contribution of
# Source+: precipitation loss to a radiation belt electron dropout observed
# Source+: by Van Allen Probes", J. Geophys. Res. Space Physics 129,
# Source+: e2023JA032171, doi:10.1029/2023JA032171 -- introduction, first
# Source+: paragraph, the same span independently.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf and
# Access+: https://par.nsf.gov/servlets/purl/10578577 (2026-09-13).
# Note: the layer below is Paulikas and Blake (1979) with Baker et al.
# Note+: (1986) for Meredith, and Ganushkina et al. (2011) with Van Allen et
# Note+: al. (1958) for Li. Both papers state the span as background.
# Note+: Baker et al. (2018) sec. 2 gives the same inner edge, r ~ 3 R_E
# Note+: from SAMPEX, and reports it reaching L ~ 2.5 under strong driving.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md

EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE = 7.0
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Meredith et al. (2014), doi:10.1002/2014JA020064, and Li, Tu et
# Source+: al. (2024), doi:10.1029/2023JA032171 -- both state the outer belt
# Source+: extending to 7 Earth radii, in their introductions.
# Access: open full text,
# Access+: https://nora.nerc.ac.uk/id/eprint/507469/1/jgra51120.pdf and
# Access+: https://par.nsf.gov/servlets/purl/10578577 (2026-09-13).
# Note: the measuring review disagrees on the outside and the disagreement
# Note+: is recorded rather than resolved by silence. Baker et al. (2018),
# Note+: doi:10.1007/s11214-017-0452-7, sec. 2 and 3.4, puts the outer zone
# Note+: at r ~ 3 to >= 6.5 R_E from SAMPEX and, in L, at about 3.0 to 6.5.
# Note+: Koskinen and Kilpua (2022) sec. 1.1 put the outer reach at 7 to 10
# Note+: R_E, which is why 10.4 R_E is not the physical impossibility one
# Note+: checker called it: the belt's outer edge approaches the
# Note+: magnetopause, and magnetopause shadowing is a standard loss
# Note+: mechanism.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md
# Record: documentation/worksheets/Fable51_medium_citation_worksheet_3_van_allen_belts_RETURN.md

'''

# ---------------------------------------------------------------------------
# Edit 3: the outer peak row.
# ---------------------------------------------------------------------------

OUTER_PEAK_OLD = b'''EARTH_VAN_ALLEN_OUTER_RADII = 4.5
# Source: the CIRBE/REPTile-2 paper above, doi:10.1029/2024JA033504 -- the
# Source+: outer belt is most intense around L = 4 and 5; Kellerman et al.
# Source+: (2014) as cited in "Electron intensity measurements by the
# Source+: Cluster/RAPID/IES instrument in Earth's radiation belts and ring
# Source+: current" (2018, arXiv:1809.00902) -- maximum electron flux at
# Source+: L = 4-5. Midpoint of that band. Baker et al. (2018), above, put
# Source+: the outer zone at r ~ 3 to 6.5 R_E from SAMPEX.
# Note: a peak, not an edge. The outer belt spans roughly L = 3 to 7 and
# Note+: moves with geomagnetic activity; the drawn torus marks the peak.
'''

OUTER_PEAK_NEW = b'''EARTH_VAN_ALLEN_OUTER_RADII = 4.5
# Unit: l_shell
# Status: declared 2026-09-14 -- a pick from a range, L-305 item 7
# Declared: the midpoint of an L band, not a measured peak, and the pick is
# Declared+: ours. Li et al. (2025), "A New Electron and Proton Radiation
# Declared+: Belt Identified by CIRBE/REPTile-2 Measurements After the
# Declared+: Magnetic Super Storm of 10 May 2024", J. Geophys. Res. Space
# Declared+: Physics, doi:10.1029/2024JA033504, sec. 1 -- the outer belt is
# Declared+: most intense around L = 4 and 5. Li et al. (2015),
# Declared+: doi:10.1002/2014JA020777, sec. 1 -- greatest intensity between
# Declared+: 4 and 5 equatorial R_E for electrons above 500 keV.
# Declared+: Kellerman et al. (2014), as reported in "Electron intensity
# Declared+: measurements by the Cluster/RAPID/IES instrument in Earth's
# Declared+: radiation belts and ring current" (2018, arXiv:1809.00902) --
# Declared+: maximum electron flux at L = 4-5. The arXiv paper is the
# Declared+: document opened; Kellerman is the layer below it.
# Access: open full text, https://par.nsf.gov/servlets/purl/10575739
# Access+: (2026-09-13), the same paper Wiley serves.
# Note: a peak, not an edge; the edges are their own rows since 2026-09-14.
# Note+: The unit is L, the McIlwain parameter, because the value is the
# Note+: midpoint of an L band. L equals geocentric distance in Earth radii
# Note+: only where a field line crosses the magnetic equator, so any string
# Note+: printing this row says "at the equator".
# Note+: Baker et al. (2018) was REMOVED from this row's citation on
# Note+: 2026-09-14. His figure 30 uses L* = 4.5 as a selected analysis
# Note+: location and his figure 12 concerns variable peak positions, so
# Note+: neither identifies a universal peak. His span figure is on
# Note+: EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE, which is what it measures.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md
'''

# ---------------------------------------------------------------------------
# Edit 4 (highest in the file): the inner peak row.
# ---------------------------------------------------------------------------

INNER_PEAK_OLD = b'''EARTH_VAN_ALLEN_INNER_RADII = 1.5
# Source: Baker, D. N. et al. (2018), "Space Weather Effects in the
# Source+: Earth's Radiation Belts", Space Sci. Rev. 214:17,
# Source+: doi:10.1007/s11214-017-0452-7 -- inner-zone proton fluxes peak
# Source+: near geocentric r ~ 1.5 R_E. Also "A New Electron and Proton
# Source+: Radiation Belt Identified by CIRBE/REPTile-2 Measurements After
# Source+: the Magnetic Super Storm of 10 May 2024", J. Geophys. Res. Space
# Source+: Physics (2025), doi:10.1029/2024JA033504 -- the inner belt is
# Source+: centred near L = 1.5.
# Note: a peak, not an edge. The inner belt spans roughly L = 1.1 to 2;
# Note+: the drawn torus marks where the flux is greatest.
'''

INNER_PEAK_NEW = b'''EARTH_VAN_ALLEN_INNER_RADII = 1.5
# Unit: r_earth
# Status: measured V_SOURCED 2026-09-14 -- open full text
# Source: Baker, D. N. et al. (2018), "Space Weather Effects in the
# Source+: Earth's Radiation Belts", Space Sci. Rev. 214:17,
# Source+: doi:10.1007/s11214-017-0452-7 -- sec. 2: inner-zone proton fluxes
# Source+: peak near geocentric r ~ 1.5 R_E. Geocentric, equatorial, which
# Source+: is the frame this row is in.
# Access: open full text,
# Access+: https://link.springer.com/article/10.1007/s11214-017-0452-7
# Access+: (2026-09-13).
# Note: a peak, not an edge; the edges are their own rows since 2026-09-14.
# Note+: The drawn torus marks where the flux is greatest.
# Note+: The same number is read a second time in a different frame, kept
# Note+: here as a second reading and not as agreement: Li et al. (2025),
# Note+: doi:10.1029/2024JA033504, centres the inner belt near L = 1.5, and
# Note+: Selesnick et al. (2014), doi:10.1002/2014JA020188 sec. 5, puts the
# Note+: peak near L = 1.5 for 46 and 66 MeV protons against 1.6 for 26 MeV.
# Note+: L and geocentric radii coincide at the magnetic equator, so the
# Note+: agreement here is arithmetic rather than evidence about the frame.
# Record: documentation/worksheets/L321_worksheet_3_van_allen_gemini31pro_20260913.md
'''


def fail(message):
    print("ERROR: " + message)
    sys.exit(1)


def apply_once(data, old, new, label):
    """Replace old with new, requiring exactly one match."""
    count = data.count(old)
    if count != 1:
        print("ANCHOR FAIL: %s matched %d times, expected 1" % (label, count))
        sys.exit(1)
    print("  ok  %s" % label)
    return data.replace(old, new)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    full = os.path.join(here, TARGET)

    if not os.path.exists(full):
        fail("%s not found beside this script. Put this file in the repo "
             "root, next to constants_new.py." % TARGET)

    with open(full, "rb") as handle:
        data = handle.read()

    if b"\r\n" in data:
        fail("%s has CRLF line endings; this patch expects LF." % TARGET)

    fp = hashlib.md5(data).hexdigest()
    if fp != BASE_FP:
        print("ERROR: %s is not the file this patch was built against." % TARGET)
        print("  expected fingerprint %s" % BASE_FP)
        print("  found               %s" % fp)
        print("  Nothing was written. Pull the repo at "
              "2f1a0c2f03a15927a6667bf4297f2a07991bfdfe, or ask for a rebuild "
              "against what you have.")
        sys.exit(1)

    if b"EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE" in data:
        fail("the belt edge rows are already present; this patch has run.")

    # Bottom-up: lowest edit first, so nothing above it has moved.
    data = apply_once(data, TAIL_ANCHOR, TAIL_NEW,
                      "magnetotail row inserted above EARTH_GEOCORONA_RADII")
    data = apply_once(data, EDGES_ANCHOR, EDGES_NEW + EDGES_ANCHOR,
                      "four belt edge rows inserted above the magnetosphere "
                      "block")
    data = apply_once(data, OUTER_PEAK_OLD, OUTER_PEAK_NEW,
                      "EARTH_VAN_ALLEN_OUTER_RADII rewritten (unit l_shell, "
                      "status declared, Baker off the peak)")
    data = apply_once(data, INNER_PEAK_OLD, INNER_PEAK_NEW,
                      "EARTH_VAN_ALLEN_INNER_RADII rewritten (unit r_earth, "
                      "status measured, span removed from the Note)")

    non_ascii = [b for b in bytearray(data) if b > 127]
    if non_ascii:
        fail("the patched text contains %d non-ASCII bytes; refusing to write."
             % len(non_ascii))

    with open(full, "wb") as handle:
        handle.write(data)

    added = [
        "EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE",
        "EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE",
        "EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE",
        "EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE",
        "EARTH_MAGNETOTAIL_OBSERVED_RADII",
    ]
    changed = [
        "EARTH_VAN_ALLEN_INNER_RADII",
        "EARTH_VAN_ALLEN_OUTER_RADII",
    ]
    print("patch applied to %s" % TARGET)
    print("  %d rows added, and they are:" % len(added))
    for name in added:
        print("    %s" % name)
    print("  %d rows changed, and they are:" % len(changed))
    for name in changed:
        print("    %s" % name)
    print("  next: run test_status_lines.py")


if __name__ == "__main__":
    main()
