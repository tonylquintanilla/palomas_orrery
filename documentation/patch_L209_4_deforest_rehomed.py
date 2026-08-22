"""
patch_L209_4_deforest_rehomed.py

Implements the DeForest rehoming ruling on ALFVEN_SURFACE_RADII, and
corrects the figure that ruling has been carrying.

WHY THIS EXISTS
    DeForest, Howard & McComas (2014), ApJ 787:124 was removed from
    STREAMER_BELT_RADII on 2026-08-20 because its 6 R_sun is an
    inbound-wave detection threshold rather than a streamer extent.
    Its actual result -- a lower bound on the Alfven surface -- belongs
    to this row. The removal was executed; the rehoming was not.

THE CORRECTION, AND IT IS THE POINT OF THIS PATCH
    Every document in this project that carries the DeForest result
    states 17 R_sun in the streamer belt and 12.5 over the polar
    coronal holes. The published paper does not say that. It says 15
    and 12, and it says so in three separate places:

      Abstract   "...the Alfven surface is at least 12 solar radii
                 from the Sun over the polar coronal holes and 15
                 solar radii in the streamer belt..."
      Section 5  "...a lower limit for the Alfven surface altitude of
                 15 R_S in the streamer belt and 12 R_S in the coronal
                 hole."
      Section 6  "...the Alfven surface was above 15 R_S in the
                 streamer belt and significantly above 12 R_S in the
                 polar coronal holes."

    The 12.5 / 17 pair appears in the arXiv ABSTRACT METADATA FIELD at
    arxiv.org/abs/1404.3235, which was never updated to match the
    accepted manuscript served at arxiv.org/pdf/1404.3235. NASA ADS
    (2014ApJ...787..124D) carries 12 / 15, and Cranmer et al. 2016,
    ApJ 828:66, citing this paper independently, also states 12 and 15.

    So the number this project has repeated across four documents came
    from a listing page rather than from the paper. Both prior reads
    that reported it -- the 2026-08-18 pilot leg and the 2026-08-20
    blind read -- quoted the arXiv abstract field, which is why they
    agreed. Agreement between two reads of the same wrong page is not
    verification. Sourced from the paper 2026-08-21.

WHAT IT CHANGES  (constants_new.py only -- three anchored edits)
    1. ALFVEN_SURFACE_RADII gains the DeForest leg on `# Also:` and
       `# Also+:` lines -- a 2014 remote lower bound, SUPERSEDED by
       Kasper's 2021 in-situ crossing. It corroborates; it is not the
       source of 19.7 and the annotation says so.
    2. The STREAMER_BELT_RADII `# Review-note:` figure moves from
       ">= 17 R_sun" to ">= 15 R_sun", with the arXiv discrepancy named
       so nobody restores it. Fix In Passing, Report It
       (safe-file-editing 1.4): the file is already fingerprinted, and
       a citation stating a figure its paper does not state is a
       violation of an already-ruled convention.
    3. Currency stamp.

REPORTED, NOT FIXED -- four more sites carry the same 17
    Three are prose and one renders:
      LEDGER_CONSOLIDATED.md L-210 block ("17 R_sun or more")
      documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md line 214
      solar_visualization_shells.py lines 755 and 782 -- HOVER TEXT,
        "Streamer belt: ~17-19 R_sun", which reaches the screen. That
        range traces to neither paper: DeForest bounds it below at 15,
        Kasper measures 19.7. It needs a decision about what the shell
        should say, not a find-and-replace, so it is left alone here.
    The two worksheets that quote 17 are RETURNS and are not edited --
    a record of what a responder said stays what it said.

HOW TO RUN
    Save into the SAME folder as constants_new.py (the repo root),
    open in VS Code, click Run. Or:

        python patch_L209_4_deforest_rehomed.py

    Then, as usual after a constants edit:

        python -m py_compile constants_new.py
        python test_constants_provenance.py
        python provenance_scanner.py

    Nothing is written unless every anchor matches exactly once.

PERMANENT vs DISPOSABLE
    Disposable -- it guards on a fingerprint that stops existing the
    moment it succeeds. Archive to documentation/ once run. The
    annotations are the permanent half.

Built on 6184b3b910e894784396dea26856f8a178c87bd0 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 21, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "constants_new.py"

# md5 of the LF-normalized form at 6184b3b9.
EXPECTED_FP = "acbd7211f55153743f9f047bf6aa3050"


# --------------------------------------------------------------------
# Edit 1 -- currency stamp
# --------------------------------------------------------------------

E1_OLD = b"""Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-210 reconciliation; see the Resolved legs on the affected rows)
"""

E1_NEW = b"""Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-210 reconciliation; see the Resolved legs on the affected rows)
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-209: DeForest 2014 rehomed to ALFVEN_SURFACE_RADII, and its figure corrected from 17 to the published 15 R_sun)
"""


# --------------------------------------------------------------------
# Edit 2 -- the DeForest leg on ALFVEN_SURFACE_RADII
#
# Placed after the `# Also:` NASA link and before `# Corrected:`, so
# the legs stay grouped and the dated record lines stay last.
# --------------------------------------------------------------------

E2_OLD = b"""# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere
# Corrected: 2026-08-19 -- was 18.8, an altitude used as a heliocentric radius.
"""

E2_NEW = b"""# Also: https://www.nasa.gov/feature/goddard/2021/nasa-enters-the-solar-atmosphere
# Also+: DeForest, Howard & McComas (2014), ApJ 787:124 -- the first remote
# Also+: measurement of the Alfven surface, a LOWER BOUND of 15 R_sun in the
# Also+: streamer belt and 12 R_sun over the polar coronal holes, from inbound
# Also+: wave motion in STEREO-A/COR2. It does NOT source the value above: it
# Also+: is a 2014 bound superseded by Kasper's 2021 in-situ crossing, and it
# Also+: is consistent with it (19.7 is above 15). Both of its bounds are
# Also+: INSTRUMENTAL rather than physical -- the paper states the streamer
# Also+: figure is set by the coronagraph's field of view and the polar figure
# Also+: by the noise floor, so the true surface lies somewhere above each.
# Also+: Rehomed here 2026-08-21 from STREAMER_BELT_RADII, where it had been
# Also+: cited for a claim it does not make (L-210).
# Review-note: this row previously would have received "17 R_sun in the
#   streamer belt, 12.5 over the poles". The published paper says 15 and 12,
#   in its abstract, its Section 5 and its Section 6. The 12.5/17 pair is the
#   arXiv ABSTRACT METADATA at arxiv.org/abs/1404.3235, which does not match
#   the accepted manuscript at arxiv.org/pdf/1404.3235; NASA ADS and Cranmer
#   et al. 2016 (ApJ 828:66) both carry 12 and 15. Two earlier reads reported
#   17 because both quoted that same listing page -- agreement between two
#   reads of one wrong page is not verification. Do not "restore" 17.
# Corrected: 2026-08-19 -- was 18.8, an altitude used as a heliocentric radius.
"""


# --------------------------------------------------------------------
# Edit 3 -- the streamer row's Review-note figure (fix in passing)
# --------------------------------------------------------------------

E3_OLD = b"""#   is an Alfven surface at >= 17 R_sun -- a result that belongs to
#   ALFVEN_SURFACE_RADII (L-209), where it is owed. (c) Golub &
"""

E3_NEW = b"""#   is an Alfven surface at >= 15 R_sun -- a result that belongs to
#   ALFVEN_SURFACE_RADII (L-209), where it was rehomed 2026-08-21.
#   That figure read ">= 17" here until 2026-08-21; 17 is the arXiv
#   abstract-metadata value and the published paper says 15. (c) Golub &
"""


EDITS = [
    ("1  currency stamp", E1_OLD, E1_NEW),
    ("2  DeForest leg on ALFVEN_SURFACE_RADII", E2_OLD, E2_NEW),
    ("3  streamer Review-note 17 -> 15 (fix in passing)", E3_OLD, E3_NEW),
]


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Put this script in the same folder as "
             "constants_new.py (the repo root) and run it again." % TARGET)

    with open(TARGET, "rb") as f:
        data = f.read()
    original_len = len(data)

    normalized = data.replace(b"\r\n", b"\n")
    fp = hashlib.md5(normalized).hexdigest()
    if fp != EXPECTED_FP:
        print("ERROR: BASE MOVED. %s is not the file this patch was "
              "built against." % TARGET)
        print("  expected fingerprint : " + EXPECTED_FP)
        print("  this file            : " + fp)
        print("  size                 : %d bytes" % original_len)
        print("  Nothing was written.")
        sys.exit(1)

    is_crlf = data.count(b"\r\n") > 0
    print("base ok: fingerprint %s, %d bytes, line endings %s"
          % (fp, original_len, "CRLF" if is_crlf else "LF"))

    for label, _old, new in EDITS:
        bad = [b for b in new if b > 127]
        if bad:
            fail("edit %s would insert %d non-ASCII byte(s). Refusing."
                 % (label, len(bad)))
    pre_existing = len([b for b in normalized if b > 127])
    if pre_existing:
        print("note: %s already holds %d non-ASCII byte(s) this patch "
              "does not reach" % (TARGET, pre_existing))
    else:
        print("note: %s is ASCII throughout, before and after" % TARGET)

    working = data
    for label, old, new in EDITS:
        o, n = old, new
        if is_crlf:
            o = o.replace(b"\n", b"\r\n")
            n = n.replace(b"\n", b"\r\n")
        count = working.count(o)
        if count != 1:
            print("ANCHOR FAIL on edit %s: expected exactly 1 match, "
                  "found %d." % (label, count))
            print("  anchor began: %r" % o[:70])
            print("  Nothing was written.")
            sys.exit(1)
        working = working.replace(o, n)
        print("ok   edit %s  (+%d bytes)" % (label, len(n) - len(o)))

    with open(TARGET, "wb") as f:
        f.write(working)
    print("patch applied (%d bytes, was %d)" % (len(working), original_len))

    # ---- success carries evidence, read back from disk ---------------
    with open(TARGET, "rb") as f:
        rb = f.read().replace(b"\r\n", b"\n")

    checks = [
        ("DeForest leg present on the Alfven row",
         b"# Also+: DeForest, Howard & McComas (2014), ApJ 787:124", 1),
        ("leg states the PUBLISHED 15 R_sun bound",
         b"a LOWER BOUND of 15 R_sun in the", 1),
        ("leg states it does not source the value",
         b"It does NOT source the value above", 1),
        ("arXiv discrepancy recorded so 17 is not restored",
         b'Do not "restore" 17.', 1),
        ("streamer Review-note now reads 15",
         b"#   is an Alfven surface at >= 15 R_sun", 1),
        ("no '>= 17 R_sun' left anywhere in this file",
         b">= 17 R_sun", 0),
        ("currency stamp added",
         b"Module updated: August 21, 2026 with Anthropic's Claude Opus 5 "
         b"(L-209:", 1),
        ("the 19.7 value is untouched",
         b"ALFVEN_SURFACE_RADII = 19.7", 1),
        ("Kasper Source leg untouched",
         b"# Source: Kasper et al. (2021), Phys. Rev. Lett. 127:255101", 1),
    ]

    print("")
    print("verification, %d checks, each read back from disk:" % len(checks))
    failures = 0
    for desc, needle, want in checks:
        got = rb.count(needle)
        mark = "PASS" if got == want else "FAIL"
        if got != want:
            failures += 1
        print("  %s  %s  (found %d, expected %d)" % (mark, desc, got, want))

    # Compile the result. A comment-only edit cannot break syntax, but a
    # check that cannot fail is not passing -- this one fails if an
    # anchor ever lands mid-statement.
    import py_compile
    try:
        py_compile.compile(TARGET, doraise=True)
        print("  PASS  %s still compiles" % TARGET)
    except Exception as exc:
        print("  FAIL  %s no longer compiles: %s" % (TARGET, exc))
        failures += 1

    if failures:
        print("")
        print("ERROR: %d check(s) failed AFTER writing. Restore "
              "constants_new.py from git and report this." % failures)
        sys.exit(1)

    print("")
    print("NEXT: run test_constants_provenance.py and")
    print("provenance_scanner.py, then commit, push, and archive this")
    print("script to documentation/.")
    print("")
    print("STILL CARRYING 17, reported not fixed -- see the header:")
    print("  LEDGER_CONSOLIDATED.md (L-210 block)")
    print("  documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md:214")
    print("  solar_visualization_shells.py:755,782 -- HOVER TEXT, reaches")
    print("    the screen, and needs a decision rather than a replace.")


if __name__ == "__main__":
    main()
