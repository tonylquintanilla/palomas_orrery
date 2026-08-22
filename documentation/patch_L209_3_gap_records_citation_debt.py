"""
patch_L209_3_gap_records_citation_debt.py

Corrects the **Gap:** on the L-209 detail block in
LEDGER_CONSOLIDATED.md, which reads "none" and predates the obligation
it should be recording.

WHY THIS EXISTS
    L-209's block was last written 2026-08-19. On 2026-08-20, at
    e1c64dc9, DeForest, Howard & McComas (2014) was removed from
    STREAMER_BELT_RADII because its 6 R_sun is an inbound-wave
    detection threshold rather than a streamer extent. That paper's
    actual streamer-belt result -- an Alfven surface at 17 R_sun or
    more -- is a second independent route to ALFVEN_SURFACE_RADII, and
    it landed nowhere.

    So the Gap does not say "nothing is owed." It was written a day
    before anything was owed, and nobody carried the neighbouring row's
    decision back to it. Three stores say the citation is owed and one
    of them is the live code: the streamer row's `# Review-note:` in
    constants_new.py ends "where it is owed".

    This is the same staleness class as the L-210 block corrected
    earlier today at d2e6457a, one item over. That one was stale
    because its own decisions moved past it; this one is stale because
    a NEIGHBOUR's decision created a debt with no route home.

WHAT IT CHANGES  (LEDGER_CONSOLIDATED.md only -- three anchored edits)
    1. Header currency stamp -- a second "Module updated:" line for
       today, carrying its own base SHA. Not merged into this morning's
       L-210 stamp, because the two were built on different bases and a
       stamp that names one SHA for two bases is a false anchor.
    2. L-209 metadata comment -- upd:2026-08-19 -> upd:2026-08-21.
       status stays OPEN; RICE untouched.
    3. **Gap:** and **Ref:** -- Gap becomes two numbered items, the
       citation debt and the unchanged Mode 5 obligation. Ref extended.

WHAT IT DOES NOT DO -- AND THIS IS THE POINT
    It does NOT add the DeForest citation to ALFVEN_SURFACE_RADII.
    The 2026-08-20 blind read is ONE leg from ONE model, and the rule
    that same session wrote into constants_new.py applies here: a
    removal needs only the ABSENCE of support, a citation needs its
    PRESENCE. Landing a citation from the removal worksheet would be
    cite-to-clear. This patch records the debt and names what
    discharges it; a verified read discharges it.

    It also does not touch the generated INDEX zone. Run
    ledger_index.py after.

HOW TO RUN
    Save this file into the SAME folder as LEDGER_CONSOLIDATED.md (the
    repo root), open it in VS Code, and click Run. Or:

        python patch_L209_3_gap_records_citation_debt.py

    Success: one "ok" line per edit, then a verification block where
    every check is read back from disk. Failure: a single ERROR: or
    ANCHOR FAIL line, with nothing written in either case.

    AFTER a successful run:

        python ledger_index.py

    That moves L-209's index row to 2026-08-21. This patch deliberately
    leaves the index alone, which is why the last verification check
    below EXPECTS to still find the old date there.

PERMANENT vs DISPOSABLE
    Disposable. It guards on a fingerprint of a tree that stops
    existing the moment it succeeds, so a second run aborts and writes
    nothing. Archive it to documentation/ once run. The ledger text it
    writes is the permanent half.

Built on 6184b3b910e894784396dea26856f8a178c87bd0 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 21, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"

# md5 of the LF-normalized form at 6184b3b9. Normalized, because Tony's
# working copy is CRLF where the repo is LF and the content is
# identical -- a raw fingerprint would call that BASE MOVED and send
# everyone hunting an edit nobody made. Confirmed this morning: the
# working copy ran 9402 bytes larger on a 9402-line file.
EXPECTED_FP = "cd602d7ef8cfb611809197a867d9998d"


# --------------------------------------------------------------------
# Edit 1 -- second currency stamp for today, with its own base SHA
# --------------------------------------------------------------------

E1_OLD = b"""withdrawn streamer-belt claim marked as withdrawn), built on d2e6457a.
Review and RICE update Tony 6-21-2026
"""

E1_NEW = b"""withdrawn streamer-belt claim marked as withdrawn), built on d2e6457a.
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-209:
Gap corrected -- it recorded "none" a day before the DeForest citation
became owed to that row), built on 6184b3b9.
Review and RICE update Tony 6-21-2026
"""


# --------------------------------------------------------------------
# Edit 2 -- L-209 metadata comment, date only
# --------------------------------------------------------------------

E2_OLD = b"<!-- L:209 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/1 -->"
E2_NEW = b"<!-- L:209 status:OPEN upd:2026-08-21 section:A flag: rice:3/3/85/1 -->"


# --------------------------------------------------------------------
# Edit 3 -- Gap and Ref
#
# One anchor over the contiguous Gap/Ref run. The **Note:** line above
# it is included as leading context only: it is unchanged, and it is
# what makes this anchor unique against the identical Note lines on
# other blocks.
# --------------------------------------------------------------------

E3_OLD = b"""**Note:** RICE is Claude's proposal, unratified.
**Gap:** none. Mode 5 outstanding: the Alfven shell should render one
solar radius larger, still nested inside the 50 R_sun outer corona.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Part 4;
`documentation/worksheets/`
`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl` R12;
L-214 (the builder gap this exposed); L-181 and L-191 (the remaining
shadow constants); L-207 (the run that produced it).
"""

E3_NEW = b"""**Note:** RICE is Claude's proposal, unratified.
**Gap:** two. The first is new, and it was here before this Gap was
corrected on 2026-08-21 -- the Gap read "none" because it was written
2026-08-19, a day before the debt existed.
1. **A CITATION IS OWED to this row.** DeForest, Howard & McComas
   (2014), ApJ 787:124 was removed from `STREAMER_BELT_RADII` on
   2026-08-20 at `e1c64dc9`: its 6 R_sun is the threshold at which
   inbound wave motion first became DETECTABLE, not a streamer extent.
   The paper's actual streamer-belt result -- an Alfven surface at 17
   R_sun or more, and 12.5 or more over the polar coronal holes -- is a
   SECOND independent route to this constant, and it landed nowhere.
   The removal was executed; the rehoming was not. Three stores say it
   is owed and one of them is the live code: the streamer row's
   `# Review-note:` in `constants_new.py` ends "where it is owed".
   **What it is NOT dischargeable from:** the 2026-08-20 reconciliation
   read. That is one blind leg from one model, and the rule the same
   session wrote into `constants_new.py` governs here -- a removal
   needs only the ABSENCE of support, a citation needs its PRESENCE.
   `worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md` item 4
   does quote the abstract and name the location, so the claim is
   CHECKABLE; it has not been CHECKED. Discharge is a verified read of
   the paper, then a leg on `ALFVEN_SURFACE_RADII`. Re-using the
   removal worksheet as that leg would be cite-to-clear.
2. **MODE 5, unchanged and still outstanding.** The Alfven shell should
   render one solar radius larger than before, still nested inside the
   50 R_sun outer corona. Tony's eyes on a plot, not a build.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Part 4;
`documentation/worksheets/`
`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl` R12;
`documentation/worksheets/`
`worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md` item 4
(the checkable, unchecked claim); L-210 (the row DeForest was removed
from, and the same staleness class corrected one item over on
2026-08-21); L-214 (the builder gap this exposed); L-181 and L-191 (the
remaining shadow constants); L-207 (the run that produced it); L-221
(misapplied against this row before the dates were checked -- it
governs a session document contradicting a settled decision, not a
ledger field that predates the event it is silent about).
"""


EDITS = [
    ("1  second currency stamp for today", E1_OLD, E1_NEW),
    ("2  L-209 metadata upd date", E2_OLD, E2_NEW),
    ("3  Gap becomes two items + Ref", E3_OLD, E3_NEW),
]


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Put this script in the same folder as the "
             "ledger (the repo root) and run it again." % TARGET)

    with open(TARGET, "rb") as f:
        data = f.read()

    original_len = len(data)

    # ---- base check, on the normalized form -------------------------
    normalized = data.replace(b"\r\n", b"\n")
    fp = hashlib.md5(normalized).hexdigest()
    if fp != EXPECTED_FP:
        print("ERROR: BASE MOVED. %s is not the file this patch was "
              "built against." % TARGET)
        print("  expected fingerprint : " + EXPECTED_FP)
        print("  this file            : " + fp)
        print("  size                 : %d bytes" % original_len)
        print("  Nothing was written. Likely causes, in order: the")
        print("  ledger was edited since 6184b3b9, ledger_index.py has")
        print("  not been run since the last patch, or this is a")
        print("  different checkout.")
        sys.exit(1)

    is_crlf = data.count(b"\r\n") > 0
    print("base ok: fingerprint %s, %d bytes, line endings %s"
          % (fp, original_len, "CRLF" if is_crlf else "LF"))

    # ---- ASCII gate on what this patch INSERTS ----------------------
    # Hard-fail on non-ASCII we introduce; report, do not fail on, what
    # the file already held -- a gate that fails on somebody else's
    # bytes blocks a correct patch, and one that stays silent is how a
    # convention quietly stops being true.
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

    # ---- apply, all or nothing --------------------------------------
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

    # ---- success carries evidence -----------------------------------
    # Read back from disk, not from the buffer we just wrote. Every
    # check below has a state in which it fails.
    with open(TARGET, "rb") as f:
        readback = f.read().replace(b"\r\n", b"\n")

    checks = [
        ("L-209 metadata reads upd:2026-08-21",
         b"<!-- L:209 status:OPEN upd:2026-08-21", 1),
        ("no L-209 metadata still reads upd:2026-08-19",
         b"<!-- L:209 status:OPEN upd:2026-08-19", 0),
        ("Gap now opens with two items",
         b"**Gap:** two. The first is new", 1),
        ("old 'Gap: none' wording gone from L-209",
         b"**Gap:** none. Mode 5 outstanding", 0),
        ("citation debt names DeForest and the commit",
         b"(2014), ApJ 787:124 was removed from `STREAMER_BELT_RADII` on\n"
         b"   2026-08-20 at `e1c64dc9`", 1),
        ("the non-discharge rule is recorded",
         b"a removal\n   needs only the ABSENCE of support, a citation "
         b"needs its PRESENCE", 1),
        ("Mode 5 obligation preserved, not dropped",
         b"**MODE 5, unchanged and still outstanding.**", 1),
        ("second currency stamp added with its own SHA",
         b"became owed to that row), built on 6184b3b9.", 1),
        ("this morning's L-210 stamp still intact",
         b"withdrawn streamer-belt claim marked as withdrawn), built on "
         b"d2e6457a.", 1),
        ("INDEX zone untouched -- L-209 row still shows 2026-08-19",
         b"| L-209 | ", 1),
    ]

    print("")
    print("verification, %d checks, each read back from disk:" % len(checks))
    failures = 0
    for desc, needle, want in checks:
        got = readback.count(needle)
        mark = "PASS" if got == want else "FAIL"
        if got != want:
            failures += 1
        print("  %s  %s  (found %d, expected %d)" % (mark, desc, got, want))

    # The index row check above only proves the row exists. Prove the
    # DATE in it is still the old one, which is the thing that would
    # silently break if this patch ever reached the generated zone.
    idx_old = readback.count(
        b"| L-209 | ALFVEN_SURFACE_RADII -- origin mismatch, photosphere "
        b"vs Sun centre | OPEN | 7.6 | 2026-08-19 |")
    print("  %s  INDEX row date still 2026-08-19, awaiting ledger_index.py"
          "  (found %d, expected 1)"
          % ("PASS" if idx_old == 1 else "FAIL", idx_old))
    if idx_old != 1:
        failures += 1

    if failures:
        print("")
        print("ERROR: %d verification check(s) failed AFTER writing. The "
              "file on disk is not what this patch intended. Restore "
              "LEDGER_CONSOLIDATED.md from git and report this."
              % failures)
        sys.exit(1)

    print("")
    print("NEXT STEP -- this patch deliberately did not touch the")
    print("generated INDEX zone, which is why the last two checks")
    print("above expect the OLD date there. Regenerate it now:")
    print("")
    print("    python ledger_index.py")
    print("")
    print("Then commit and push, and archive this script to")
    print("documentation/.")


if __name__ == "__main__":
    main()
