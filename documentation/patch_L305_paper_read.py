"""patch_L305_paper_read.py -- fold the 2026-09-11 paper read into [L-305].

Built on orrery 6c3c8e86cea8506407b37402169c8c121e05be71
at https://github.com/tonylquintanilla/palomas_orrery

RUN:  save this file into the palomas_orrery repo root (the folder that
holds LEDGER_CONSOLIDATED.md), open it in VS Code, click Run.
Equivalent command line: python patch_L305_paper_read.py

Then run ledger_index.py (Run button) and expect the same
"OK: NNN L-blocks parsed, no consistency problems" line as usual.

WHAT IT DOES -- five edits to the [L-305] block only:
  1. stamps the block upd:2026-09-10 -> upd:2026-09-11
  2. corrects the stale "not re-read since" honesty tag
  3. corrects the frame claim (Shue is aberrated GSM, not GSE)
  4. appends a dated bullet group recording the read
  5. marks Gap items (1) and (2) CLOSED in place, numbering preserved

GUARD: fingerprints the ledger's content OUTSIDE the ledger_index.py
INDEX zone, line endings normalised, so it runs on either an LF or a
CRLF working copy and is not defeated by an ledger_index.py run
(safe-file-editing 1.11, A Guard Must Not Fence What a Generator
Rewrites). All or nothing: on any failure NOTHING is written.
"""

import hashlib
import os
import sys

TARGET = "LEDGER_CONSOLIDATED.md"
EXPECT_FP = "23c268e637a4ab87b7090c9e4fb3ab23"
INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

NEW_BULLETS = b"""- **2026-09-11, both papers read from the PDFs: Gap items 1 and 2
  close.** Shue's equations 10 and 11 and Table 1 ("After Fit") are
  confirmed at pp. 17,697-17,698, with the standard deviations from 200
  Monte Carlo refits: a1 10.22 +/- 0.10, a2 1.29 +/- 0.06, a3 0.184
  +/- 0.007, a4 8.14 +/- 0.39, a5 6.6 +/- 0.5, a6 0.58 +/- 0.01,
  a7 -0.007 +/- 0.0005, a8 0.024 +/- 0.0004. Bz in nT, Dp in nPa, r0 in
  R_E, theta the solar zenith angle from the aberrated Sun-Earth line.
  The alpha line previously tagged "not read" matches the paper
  exactly. Jelinek's six values are confirmed at eqs. 13-16 and sec. 4:
  R_MP = 12.82 p^(-1/5.26), R_BS = 15.02 p^(-1/6.55), lambda_MP = 1.54,
  lambda_BS = 1.17. [read from Tony's uploaded PDFs, 2026-09-11]
- **Every computed figure in this item reproduces from the published
  equations.** Recomputed 2026-09-11 from the papers rather than from
  this block: Shue r0 = 10.2519 and alpha = 0.5896 at p = 2 nPa,
  Bz = 0; Shue's cross-section 28.88 R_E at x = -100; Jelinek noses
  13.5117 (bow shock) and 11.2372 (magnetopause); the 105 degree cut at
  x = -7.77, R_yz = 28.99; the Jelinek paraboloids at x = -100 giving
  66.95 (bow shock) and 45.92 (magnetopause). This IS independent of
  the 2026-09-10 read, which had this block open; this one ran from the
  equations. [computed 2026-09-11]
- **Correction: the two fits are NOT in the same frame.** Shue is in
  aberrated GSM (figs. 2 and 4 captions; cylindric symmetry about the
  aberrated Sun-Earth line, p. 17,692). Jelinek is in aberrated GSE
  (sec. 3). The aberration bullet above said both were GSE and is
  corrected in place. It does not change what is drawn -- the two
  frames share the X axis and both surfaces are rotationally symmetric
  about it -- so a later session must not "fix" a frame mismatch that
  has no geometric effect.
- **The Shue validity range is readable in the 1998 paper, so Shue
  (1997) is not needed for it.** P. 17,693 states the fitted ranges as
  -18 nT < Bz < 15 nT and 0.5 nPa < Dp < 8.5 nPa, over the ISEE 1 and
  2, AMPTE/IRM and IMP 8 crossings that the 1998 refit reuses. The
  improved nonlinear forms exist so that extrapolation past that range
  stays physical (figs. 10 and 13 run to 50-60 nPa), which is an
  argument about behaviour and not a wider fitted range. The declared
  conditions p = 2 nPa, Bz = 0 sit inside it.
- **What supports the tail hover's "fitted on near-Earth crossings".**
  The paper states no angular range for its crossings. Fig. 6 evaluates
  the model's own uncertainty against solar zenith angle out to 120
  degrees at Dp = 2 nPa, and the text says that uncertainty rises
  rapidly with the angle (p. 17,695). That supports the hover wording
  already chosen, which carries no number. No number is therefore owed
  and Shue (1997) stays unread with no gap behind it.
- **2 nPa is the paper's own average; Bz = 0 and 400 km/s are not.**
  Shue p. 17,695 uses Dp = 2 nPa as an average value, which is a
  paper-internal reason for the store's declared pressure. Its average
  Bz is +/- 4 nT (northward / southward), not 0, so the store's Bz = 0
  is a neutral midpoint chosen here and its row must say so. The
  410 km/s on p. 17,694 is the speed during one January 1997 event and
  does NOT source a nominal 400 km/s; that reason is still unwritten
  (L-314).
- **Dp includes helium, by the factor (1 + 0.04 N_alpha).** Shue's
  fig. 1 caption (p. 17,692) states that the solar wind dynamic
  pressure includes the helium contribution by a factor
  (1 + 0.04 N_alpha), where N_alpha is the He++ concentration, an
  average value of 4 percent being used when N_alpha is missing.
  N_alpha is a PERCENTAGE, not a fraction: at the paper's own 4 the
  factor is 1.16, which is the four proton masses per helium nucleus
  at 4 percent number density. L-314 derives p from SWPC density and
  speed and inherits this as a declared assumption -- whether that
  feed carries N_alpha decides between a measured correction and the
  4 percent default, and which density it reports is a question for
  that item. [read from the caption, 2026-09-11]
- **Do not pick up Jelinek's equations 17 and 18.** R_MP = 12.90
  p^(-1/4.92) and R_BS = 14.94 p^(-1/6.62) are the validation refit
  against observed crossings (sec. 5.2), not the model. The model is
  eqs. 13-16. The two pairs are close enough to be mistaken for one
  another by a session reading the paper quickly.
- **Shue's own scatter is the larger of the two, which strengthens the
  seam bullet above.** The improved model's standard deviation against
  the observed crossings is 1.23 R_E (p. 17,697); Jelinek's
  magnetopause scatter is 0.76 R_E (fig. 7). So the roughly 1 R_E
  disagreement between the two magnetopause noses sits inside Shue's
  scatter alone.
- **Access routes, for the store rows.** Shue et al. (1998),
  doi:10.1029/98JA01103 -- OPEN FULL TEXT, Tony's download via Wiley
  (Readcube), 2026-09-11; sandbox fetches of the DOI page are refused
  by bot detection, which is not a paywall. Jelinek et al. (2012),
  doi:10.1029/2011JA017252 -- OPEN FULL TEXT, same route, 2026-09-10.
  Ness et al. (1967), doi:10.1029/JZ072i015p03769 -- ABSTRACT, open;
  full text walled (Tony's check, 2026-09-11). Per-row pointers: r0
  from eq. 10 with Table 1 rows a1-a5; alpha from eq. 11 with rows
  a6-a8; Jelinek R0 and eps from eqs. 13-14; lambda from sec. 4; the
  surface from eqs. 15-16; the cut angle from the +/- 7 h local-time
  envelope, sec. 2 para. 9; the 0.6-11 nPa envelope from the
  conclusion, para. 30.
- **Gap item 2, the tail extent: 1,000 R_E is sourced, and the figure
  changes.** Ness, N. F., C. S. Scearce and S. C. Cantarano (1967),
  Probable observations of the geomagnetic tail at 10^3 Earth radii by
  Pioneer 7, J. Geophys. Res. 72(15), 3769-3776,
  doi:10.1029/JZ072i015p03769. The abstract states that Pioneer 7
  passed through the downstream interaction region at 900-1,050 R_E
  (26 September to 3 October 1966); that the field measurements suggest
  certain lines of force there connect to Earth through the tail; that
  a coherent, well-ordered tail with an embedded neutral sheet does NOT
  appear to have been observed; and that the geometry becomes a complex
  set of intermingled filamentary flux tubes at several hundred R_E.
  So "past 1,000 R_E" becomes "to about 1,000 R_E" -- the source is a
  crossing band, not a lower bound -- and the qualifier travels with
  the figure in the hover: the drawn surface stops at the served
  100 R_E, the tail's signature reaches roughly ten times that, and by
  then it is filaments rather than a sheet. The paper's own title says
  "probable". The served magnetotail row's `_declared` 1,000 R_E takes
  this row as its source, declared -> V_SOURCED (abstract, open), with
  the qualifier in the row's note so a later session does not strip it.
  A fuller-text authority restating the Pioneer 7 result would let the
  hover drop "probable"; that is a nicety, not a gap.
"""

EDITS = [
    # 1. stamp the block
    (b"<!-- L:305 status:OPEN upd:2026-09-10 section:A flag: rice:4/4/60/4 -->",
     b"<!-- L:305 status:OPEN upd:2026-09-11 section:A flag: rice:4/4/60/4 -->"),

    # 2. the honesty tag is now stale -- the PDF has been re-read
    (b"Claude Fable 5.1 session, 2026-09-10; not re-read since]",
     b"Claude Fable 5.1 session, 2026-09-10; confirmed against the PDF\n"
     b"  2026-09-11, see the dated group below]"),

    # 3. correct the frame claim in place, visibly
    (b"- **Aberration is applied, declared.** Both fits are in ABERRATED GSE.",
     b"- **Aberration is applied, declared.** Both fits are ABERRATED:\n"
     b"  Shue in aberrated GSM, Jelinek in aberrated GSE (this line read\n"
     b"  \"both fits are in ABERRATED GSE\" until 2026-09-11; see the frame\n"
     b"  correction in the dated group below, which is why it does not\n"
     b"  change the geometry)."),

    # 4. the dated bullet group, immediately before the Gap
    (b"  why the earlier patches refused.\n**Gap:**",
     b"  why the earlier patches refused.\n" + NEW_BULLETS + b"**Gap:**"),

    # 5. Gap items (1) and (2) close; numbering preserved
    (b"""**Gap:** (1) Read Shue et al. (1998) for the alpha line and its three
coefficients, and for the range of the crossings it was fitted on,
before any store name or renderer uses them; confirm Jelinek's six
values and the local-time envelope against the PDF in the same read.
Each row records its equation or table number and its access route.
**Tony-action (do):** keep the Jelinek PDF where that session can read
it. (2) Source the tail extent behind "past 1,000 R_E" (the served
magnetotail row's `_declared` text and L-291's hover requirement), or
remove the figure from both and note the gap. (3) Read""",
     b"""**Gap:** (1) CLOSED 2026-09-11 by the dated group above -- both papers
read from the PDFs, every coefficient confirmed against the published
tables, per-row equation numbers and access routes recorded, and the
figures recomputed from the equations. The **Tony-action (do)** to keep
the Jelinek PDF available is discharged. (2) CLOSED 2026-09-11 -- the
tail extent is sourced to Ness et al. (1967) on the abstract route and
the figure becomes "to about 1,000 R_E" carrying its qualifier, per the
dated group above; the served row's status moves declared -> V_SOURCED
when item (6) writes it. (3) Read"""),
]


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    if not os.path.exists(TARGET):
        fail("%s not found. Run this from the palomas_orrery repo root." % TARGET)

    raw = open(TARGET, "rb").read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    try:
        a = content.index(INDEX_START)
        b = content.index(INDEX_END) + len(INDEX_END)
    except ValueError:
        fail("INDEX zone markers not found in %s." % TARGET)

    fp = hashlib.md5(content[:a] + content[b:]).hexdigest()
    if fp != EXPECT_FP:
        fail("BASE MOVED. Body fingerprint %s, expected %s.\n"
             "         The ledger body outside the INDEX zone has changed "
             "since this patch was built\n"
             "         (an ledger_index.py run alone would NOT do this)."
             % (fp, EXPECT_FP))
    print("ok   base fingerprint matches%s" % (" (the working copy is CRLF)" if was_crlf else ""))

    out = content
    for i, (old, new) in enumerate(EDITS, 1):
        n = out.count(old)
        if n != 1:
            fail("ANCHOR FAIL on edit %d: expected 1 match, got %d.\n"
                 "         %r" % (i, n, old[:70]))
        out = out.replace(old, new)
        print("ok   edit %d applied" % i)

    nonascii = [c for c in out if c > 127]
    if nonascii:
        fail("encoding gate: %d non-ASCII bytes in the result." % len(nonascii))
    print("ok   encoding gate: ASCII clean")

    final = out.replace(b"\n", b"\r\n") if was_crlf else out
    with open(TARGET, "wb") as f:
        f.write(final)
    print("patch applied (%d bytes, was %d)" % (len(final), len(raw)))
    print("")
    print("NEXT: run ledger_index.py (Run button), then commit and push.")


if __name__ == "__main__":
    main()
