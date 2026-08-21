"""
patch_L210_6_ledger_block_reconciled.py

Reconciles the L-210 detail block in LEDGER_CONSOLIDATED.md against the
four row decisions that landed on 2026-08-20 in constants_new.py.

WHY THIS EXISTS
    The four rows were decided, patched, tested and pushed on 2026-08-20
    (patches patch_L210_1.._5, commits 762aa5dd and e1c64dc9). The
    ledger block was never updated with them. It still reads
    status:OPEN upd:2026-08-19 and still states, as a live finding, that
    STREAMER_BELT_RADII "cites its paper inverted" -- a session reading
    that an independent nine-source blind read disproved the same day.
    MASTER_PLAN_CRITICAL_PATH_SUMMARY.md corrected itself; the ledger
    did not. The ledger is what a session reads first, so the stale
    claim sits where it does the most damage.

WHAT IT CHANGES  (LEDGER_CONSOLIDATED.md only -- six anchored edits)
    1. Header currency stamp -- a new "Module updated:" line.
    2. L-210 metadata comment -- upd:2026-08-19 -> upd:2026-08-21.
       status stays OPEN and RICE is untouched (see edit 5).
    3. The STREAMER_BELT_RADII bullet -- replaced. The withdrawn claim
       is left VISIBLE and marked withdrawn rather than quietly
       restated, on the reasoning the master plan used for the same
       claim.
    4. A "Resolved 2026-08-20" section inserted before **Note:**,
       recording the four landed rows, their values and their commits.
    5. **Note:** -- discloses that RICE was not re-scored when the four
       rows closed, so the 3.6 in the index still prices the whole
       original item.
    6. **Gap:** and **Ref:** -- Gap narrowed to ARROKOTH_RADIUS_KM,
       which is a watch flag rather than a pending fix. Ref extended.

WHAT IT DOES NOT CHANGE
    - The block title. It still reads "four rows"; renaming it would
      change the generated index row and was not asked for.
    - The status. L-210 stays OPEN because ARROKOTH is unresolved.
    - The RICE field. Re-scoring is Tony's ratification, not a
      mechanical edit; edit 5 discloses the staleness instead.
    - The INDEX zone. Never hand-edited. Run ledger_index.py after.

HOW TO RUN
    Save this file into the SAME folder as LEDGER_CONSOLIDATED.md (the
    repo root), open it in VS Code, and click Run. Or:

        python patch_L210_6_ledger_block_reconciled.py

    Success: one "ok" line per edit, then "patch applied (N bytes)".
    Failure: a single ERROR: or ANCHOR FAIL line. Nothing is written in
    either failure case, so it is always safe to re-check and retry.

    AFTER a successful run, one more step, because this patch
    deliberately does not touch the generated index zone:

        python ledger_index.py

    That is what moves L-210's index row to 2026-08-21.

PERMANENT vs DISPOSABLE
    This script is disposable -- it guards on a fingerprint of a tree
    that stops existing the moment it succeeds, so a second run aborts
    and writes nothing. Archive it to documentation/ once it has run.
    The ledger text it writes is the permanent half.

Built on d2e6457a11086d3042a08af72bd94294e7ec8558 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 21, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"

# md5 of the LF-normalized form at d2e6457a. Normalized, not raw, because
# a Windows working copy can hold CRLF where the repo holds LF with the
# content identical -- a raw fingerprint calls that BASE MOVED and sends
# everyone hunting an edit nobody made.
EXPECTED_FP = "4a7c21bb1f97e40d6b08e599f065c3ad"


# --------------------------------------------------------------------
# Edit 1 -- header currency stamp (Stamp What You Change)
# --------------------------------------------------------------------

E1_OLD = b"""master plan as sequencing authority; L-214 correction and scoping),
built on 3586970d.
Review and RICE update Tony 6-21-2026
"""

E1_NEW = b"""master plan as sequencing authority; L-214 correction and scoping),
built on 3586970d.
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-210:
block reconciled against the four decisions that landed 2026-08-20; the
withdrawn streamer-belt claim marked as withdrawn), built on d2e6457a.
Review and RICE update Tony 6-21-2026
"""


# --------------------------------------------------------------------
# Edit 2 -- L-210 metadata comment, date only
# --------------------------------------------------------------------

E2_OLD = b"<!-- L:210 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/80/2 -->"
E2_NEW = b"<!-- L:210 status:OPEN upd:2026-08-21 section:A flag: rice:3/3/80/2 -->"


# --------------------------------------------------------------------
# Edit 3 -- the streamer bullet, replaced and marked withdrawn
# --------------------------------------------------------------------

E3_OLD = b"""- **`STREAMER_BELT_RADII` -- inverted citation. Take this one first.**
  DeForest, Howard & McComas 2014 does not support "4-6 R_sun" for
  streamers. The paper's 6 R_sun is an INNER bound beyond which
  inbound wave motion was first detected; its streamer-belt result is
  a LOWER bound of 17 R_sun on the Alfven surface, 12.5 over the polar
  holes. A bounding figure was taken from the wrong end of the result,
  and the paper's point is that the structure extends further out, not
  that it stops there. The value 6.0 may survive as a drawing choice
  for the top of the closed helmet structure; the citation does not.
  Note it is the same paper cited on the Alfven row, where it belongs.
"""

E3_NEW = b"""- **`STREAMER_BELT_RADII` -- CLAIM WITHDRAWN 2026-08-20. Row resolved
  as a declared assumption.** This bullet used to say the row cited its
  paper INVERTED -- that DeForest's 6 R_sun was the paper's floor being
  used as a ceiling. That was a session reading written down as a
  finding, and an independent nine-source blind read on 2026-08-20
  found otherwise. DeForest, Howard & McComas 2014 uses 6 R_sun as the
  threshold at which inbound wave motion first became DETECTABLE, which
  is neither a floor nor a ceiling on streamer extent; its actual
  streamer-belt result is an Alfven surface at 17 R_sun or more, and
  that result belongs to L-209. Golub & Pasachoff, asked the same
  question, bound coronal structure loosely at 5-10 R_sun and state no
  4-6 R_sun streamer range at all. So the range in the code was sourced
  to nothing, both citations were removed, and the range was withdrawn.
  Reads two and three then found why nobody could answer it: the
  quantity is not single-valued. Closed helmets reach no higher than
  2-4 R_sun while stalks and boundaries run to roughly 2-10, so 6.0
  sits above the one and inside the other and represents neither.
  **Tony's ruling:** hold 6.0 as a VISUALIZATION ASSUMPTION carrying no
  Source leg, and let the hover text explain the two-part reality. The
  withdrawn wording is left visible above rather than quietly restated,
  for the reason the master plan gives for doing the same: a wrong
  claim in a stored document outlives the conversation it came from,
  because the next reader has nothing else to check it against.
"""


# --------------------------------------------------------------------
# Edits 4, 5, 6 -- resolution record, Note, Gap, Ref
#
# One anchor spanning the block tail, because the three fields are
# contiguous and a single replace over the run is safer than three
# short anchors distinguished only by neighbouring context.
# --------------------------------------------------------------------

E4_OLD = b"""**Note:** RICE is Claude's proposal, unratified.
**Gap:** every item above is a RESPONDER's claim, not a verdict. Each
needs Tony's judgment per row before any patch is written.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Parts 3-4;
L-195 (Shape A swaps); L-209 (the rendering half of the same run).
"""

E4_NEW = b"""**Resolved 2026-08-20 -- four of the five rows above.** Tony ruled per
row. The changes landed in `constants_new.py`, and each of the four
carries a `# Resolved:` annotation naming this handle.
[verified @d2e6457a -- read at HEAD, not carried from a session record]
- `EARTH_EQUATORIAL_RADIUS_KM` 6378.137 -> 6378.1366. Source moved from
  IAU B3 to IERS Conventions (2010), with B3's rounding kept as the
  aside, matching `EARTH_POLAR_RADIUS_KM` directly below it.
- `STREAMER_BELT_RADII` HELD at 6.0. Both citations removed, the 4-6
  R_sun range withdrawn, the row recorded as an explicit assumption.
- `BENNU_RADIUS_KM` 0.246 -> 0.24503, Barnouin et al. 2019. The
  `Source+:` line that credited OSIRIS-REx OLA with Nolan's restated
  radar figures is gone, so the row no longer reads as independent
  confirmation it never received.
- `HAUMEA_RADIUS_KM` 715 -> 798, the Ortiz et al. 2017 occultation. The
  unsourced axes are removed and the volume-equivalent radius is now
  marked DERIVED from the published semi-axes rather than quoted.
Patches `patch_L210_1` through `_5`, archived in `documentation/`, at
`762aa5dd` and `e1c64dc9`. `_5` is the one worth remembering: the
withdrawn "4-6 R_sun" claim was still rendering at ten sites across two
shell modules after the constant had been fixed -- the parallel-pipeline
failure in its plainest form, the constant repaired and the text that
reaches the user not.
**Note:** RICE is Claude's proposal, unratified -- and it was NOT
re-scored when the four rows closed. The 3.6 in the index still prices
the original five-row item rather than the ARROKOTH remainder.
**Gap:** `ARROKOTH_RADIUS_KM` only. It is a WATCH flag, not a pending
fix: the row is not known to be wrong, and a newer New Horizons shape
model moving 9 percent the OTHER way from the 2026-04-15 correction is
a reason to look rather than a reason to edit. The attribution drift is
the firmer half -- the volume figure and the equivalent-sphere phrasing
appear in Amarante & Winter 2022, not in the cited Keane et al. 2022.
Needs a source read before any value moves. **Tony-action (decide):**
dispatch this row, or leave it watched.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Parts 3-4;
`documentation/HANDOFF_20260820_reconciliation_closed.md` (the
decisions, and part 6 on what the streamer row cost);
`documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` (carries the same
correction); L-195 (Shape A swaps); L-209 (the rendering half of the
same run, and the row DeForest's result is owed to); L-221 (the ledger
outranks a session document about a settled decision -- this block was
the counter-case, stale where the session documents were current).
"""


EDITS = [
    ("1  header currency stamp", E1_OLD, E1_NEW),
    ("2  L-210 metadata upd date", E2_OLD, E2_NEW),
    ("3  streamer bullet withdrawn", E3_OLD, E3_NEW),
    ("4  resolution record + Note/Gap/Ref", E4_OLD, E4_NEW),
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
        print("  Nothing was written. The likely causes, in order: the")
        print("  ledger was edited since d2e6457a, or you are running")
        print("  this against a different checkout.")
        sys.exit(1)

    is_crlf = data.count(b"\r\n") > 0
    print("base ok: fingerprint %s, %d bytes, line endings %s"
          % (fp, original_len, "CRLF" if is_crlf else "LF"))

    # ---- ASCII gate on what this patch INSERTS ----------------------
    # Hard-fail on non-ASCII we introduce; report (do not fail on) what
    # the file already held, so somebody else's bytes cannot block a
    # correct patch while still being visible.
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
    # Each check below can fail. Read back from disk rather than
    # trusting the in-memory buffer we just wrote.
    with open(TARGET, "rb") as f:
        readback = f.read().replace(b"\r\n", b"\n")

    checks = [
        ("L-210 metadata reads upd:2026-08-21",
         b"<!-- L:210 status:OPEN upd:2026-08-21", 1),
        ("no L-210 metadata still reads upd:2026-08-19",
         b"<!-- L:210 status:OPEN upd:2026-08-19", 0),
        ("streamer bullet marked CLAIM WITHDRAWN",
         b"STREAMER_BELT_RADII` -- CLAIM WITHDRAWN 2026-08-20", 1),
        ("no surviving 'inverted citation' claim",
         b"inverted citation. Take this one first", 0),
        ("resolution record present",
         b"**Resolved 2026-08-20 -- four of the five rows above.**", 1),
        ("Gap narrowed to ARROKOTH",
         b"**Gap:** `ARROKOTH_RADIUS_KM` only.", 1),
        ("old Gap wording gone",
         b"**Gap:** every item above is a RESPONDER's claim", 0),
        ("header stamp added",
         b"Module updated: August 21, 2026 with Anthropic's Claude Opus 5 "
         b"(L-210:", 1),
        ("INDEX zone untouched -- L-210 row still shows 2026-08-19",
         b"| ! | L-210 | Pilot citation findings -- four rows in "
         b"constants_new.py | OPEN | 3.6 | 2026-08-19 |", 1),
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

    if failures:
        print("")
        print("ERROR: %d verification check(s) failed AFTER writing. The "
              "file on disk is not what this patch intended. Restore "
              "LEDGER_CONSOLIDATED.md from git and report this."
              % failures)
        sys.exit(1)

    print("")
    print("NEXT STEP -- this patch deliberately did not touch the")
    print("generated INDEX zone, which is why the last check above")
    print("expects the OLD date there. Regenerate it now:")
    print("")
    print("    python ledger_index.py")
    print("")
    print("Then commit and push, and archive this script to")
    print("documentation/.")


if __name__ == "__main__":
    main()
