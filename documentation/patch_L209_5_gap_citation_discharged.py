"""
patch_L209_5_gap_citation_discharged.py

Closes item 1 of the L-209 Gap. The citation debt it describes was
discharged by patch_L209_4 on the same day, and the Gap has been
contradicting the code ever since.

WHY THIS EXISTS
    patch_L209_3 recorded a real debt: DeForest 2014 had been removed
    from STREAMER_BELT_RADII and never rehomed. patch_L209_4 then paid
    it -- the paper was read at source and the legs landed on
    ALFVEN_SURFACE_RADII. Both ran on 2026-08-21, minutes apart.

    So the Gap is wrong in three specific ways, all verifiable against
    the code at HEAD:
      1. It says a citation is OWED. The `# Also+:` legs are live.
      2. It states the bound as 17 R_sun and 12.5. Those are the arXiv
         abstract-metadata figures the same session replaced; the
         published paper says 15 and 12, and the code now says so.
      3. It quotes the streamer row's `# Review-note:` as ending
         "where it is owed". patch_L209_4 edit 3 changed that string to
         "where it was rehomed 2026-08-21", so the Gap cites text that
         no longer exists.

    Item 2, the Mode 5 obligation, is untouched and remains the only
    open thing on this row.

WHAT IT CHANGES  (LEDGER_CONSOLIDATED.md only -- two anchored edits)
    1. Currency stamp.
    2. Gap item 1 replaced -- the debt recorded as DISCHARGED, with
       what discharged it, the corrected figures, and the arXiv trap
       named so nobody restores 17. The Gap header changes from "two"
       to "one open, one closed" so a scanning reader sees the state
       without reading the body.

    The INDEX zone is untouched. Run ledger_index.py after.

A NOTE ON WHY THIS PATCH EXISTS AT ALL
    Three ledger corrections in two days, all the same shape: a field
    RECITING what the code says, going stale when the code moved. The
    Gaps that have not rotted are the ones that name an open question
    and point at the file. Worth remembering when writing the next one;
    not proposed as a rule on three instances.

HOW TO RUN
    Save into the repo ROOT (beside LEDGER_CONSOLIDATED.md), open in
    VS Code, click Run. Or:

        python patch_L209_5_gap_citation_discharged.py

    Then:

        python ledger_index.py

    Then commit, push, and archive this script to documentation/.

PERMANENT vs DISPOSABLE
    Disposable. The ledger text is the permanent half.

Built on 031f43e7f5e8d811008b2a19eb6f96eb27362abb at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 22, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
EXPECTED_FP = "a749ad234e4ac485abc3cd66f524598b"


E1_OLD = b"""became owed to that row), built on 6184b3b9.
Review and RICE update Tony 6-21-2026
"""

E1_NEW = b"""became owed to that row), built on 6184b3b9.
Module updated: August 22, 2026 with Anthropic's Claude Opus 5 (L-209:
Gap item 1 closed -- the debt it described was discharged the same day
by patch_L209_4), built on 031f43e7.
Review and RICE update Tony 6-21-2026
"""


E2_OLD = b"""**Gap:** two. The first is new, and it was here before this Gap was
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
"""

E2_NEW = b"""**Gap:** one open, one closed. Read item 2; item 1 is kept as record.
1. **CITATION DEBT -- DISCHARGED 2026-08-21.** DeForest, Howard &
   McComas (2014), ApJ 787:124 was removed from `STREAMER_BELT_RADII`
   on 2026-08-20 at `e1c64dc9` -- its 6 R_sun is an inbound-wave
   DETECTION THRESHOLD, not a streamer extent -- and its own result
   belongs to this row. The removal ran; the rehoming did not, and this
   Gap said "none" for a day because it was written before the debt
   existed. `patch_L209_4_deforest_rehomed.py` closed it: the paper was
   read at source, and `# Also+:` legs on `ALFVEN_SURFACE_RADII` now
   carry it as a 2014 remote LOWER BOUND, superseded by Kasper's 2021
   in-situ crossing and consistent with it. Nothing further is owed.
   **The figure changed on the way, and this is the part to remember.**
   This Gap first stated the bound as 17 R_sun in the streamer belt and
   12.5 over the poles. The published paper says 15 and 12, in its
   abstract, its Section 5 and its Section 6. The 12.5/17 pair is the
   arXiv ABSTRACT METADATA at arxiv.org/abs/1404.3235, which does not
   match the accepted manuscript arXiv itself serves as the PDF; NASA
   ADS and Cranmer et al. 2016 (ApJ 828:66) both carry 12 and 15. Two
   earlier reads reported 17 because both quoted that same listing
   page. Agreement between two reads of one wrong page is not
   verification. Do NOT restore 17 anywhere.
   **The rule it tested.** This row is why the discharge needed a real
   read rather than the removal worksheet: a removal needs only the
   ABSENCE of support, a citation needs its PRESENCE. Had the worksheet
   been reused as the leg, 17 would now be in the code.
"""


EDITS = [
    ("1  currency stamp", E1_OLD, E1_NEW),
    ("2  Gap item 1 -> discharged", E2_OLD, E2_NEW),
]


def fail(msg):
    print("ERROR: " + msg)
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run this from the repo root." % TARGET)

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
        print("  Nothing was written. Most likely: ledger_index.py has")
        print("  not been run since the last patch, or the ledger was")
        print("  edited since 031f43e7.")
        sys.exit(1)

    is_crlf = data.count(b"\r\n") > 0
    print("base ok: fingerprint %s, %d bytes, line endings %s"
          % (fp, original_len, "CRLF" if is_crlf else "LF"))

    for label, _old, new in EDITS:
        bad = [b for b in new if b > 127]
        if bad:
            fail("edit %s would insert %d non-ASCII byte(s). Refusing."
                 % (label, len(bad)))
    pre = len([b for b in normalized if b > 127])
    print("note: %s holds %d non-ASCII byte(s) before and after"
          % (TARGET, pre))

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

    with open(TARGET, "rb") as f:
        rb = f.read().replace(b"\r\n", b"\n")

    checks = [
        ("Gap header shows one open, one closed",
         b"**Gap:** one open, one closed.", 1),
        ("item 1 marked DISCHARGED",
         b"1. **CITATION DEBT -- DISCHARGED 2026-08-21.**", 1),
        ("no 'A CITATION IS OWED' left on this row",
         b"**A CITATION IS OWED to this row.**", 0),
        ("the wrong 17/12.5 assertion is gone as a live claim",
         b"an Alfven surface at 17\n   R_sun or more, and 12.5 or more", 0),
        ("published 15 and 12 recorded",
         b"The published paper says 15 and", 1),
        ("arXiv trap named",
         b"Do NOT restore 17 anywhere.", 1),
        ("the stale 'where it is owed' quote is gone",
         b'ends "where it is owed"', 0),
        ("Mode 5 item preserved untouched",
         b"2. **MODE 5, unchanged and still outstanding.**", 1),
        ("currency stamp added",
         b"Module updated: August 22, 2026 with Anthropic's Claude "
         b"Opus 5 (L-209:", 1),
        ("earlier stamps intact",
         b"Module updated: August 21, 2026 with Anthropic's Claude "
         b"Opus 5 (L-209:", 1),
        ("INDEX zone untouched -- L-209 row still shows 2026-08-21",
         b"| L-209 | ALFVEN_SURFACE_RADII -- origin mismatch, photosphere "
         b"vs Sun centre | OPEN | 7.6 | 2026-08-21 |", 1),
    ]

    print("")
    print("verification, %d checks, each read back from disk:" % len(checks))
    failures = 0
    for desc, needle, want in checks:
        got = rb.count(needle)
        if got != want:
            failures += 1
        print("  %s  %s  (found %d, expected %d)"
              % ("PASS" if got == want else "FAIL", desc, got, want))

    if failures:
        print("")
        print("ERROR: %d check(s) failed AFTER writing. Restore "
              "LEDGER_CONSOLIDATED.md from git and report this."
              % failures)
        sys.exit(1)

    print("")
    print("NEXT: python ledger_index.py, then commit, push, and archive")
    print("this script to documentation/.")


if __name__ == "__main__":
    main()
