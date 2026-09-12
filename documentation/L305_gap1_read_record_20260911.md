# L-305 Gap item 1 -- the Shue read, and Jelinek confirmed against the PDF

Built on orrery `1fa413d95e3017debe4d78a6e1fd3d62038c2cb8`
at https://github.com/tonylquintanilla/palomas_orrery (read live
2026-09-11; the L-305 block read is the one at that SHA). Gallery
repo not read this session.

Tony Quintanilla, PE | Claude Fable 5.1 | 2026-09-11
Type: READ (zero code). Mobile session; Tony away from his machine.
Both papers read from Tony's uploaded PDFs, not from search snippets.
Skills loaded: none (no file edited, no ledger patch built).

## What this record settles

Gap item 1 of L-305 asked for four things. All four are read.

### 1. Shue et al. (1998), the alpha line -- CONFIRMED, with uncertainties

Source: Shue, J.-H., et al. (1998), Magnetopause location under
extreme solar wind conditions, J. Geophys. Res. 103(A8), 17,691-17,700,
doi:10.1029/98JA01103. Access route: Wiley Online Library via Readcube
(Tony's download, 2026-09-11). Sandbox fetches of the DOI page are
refused (bot detection), same as Jelinek.

Equations 10 and 11, page 17,697, and Table 1, page 17,698:

    r = r0 (2 / (1 + cos theta))^alpha                     (eq. 1)
    r0 = {10.22 + 1.29 tanh[0.184 (Bz + 8.14)]} Dp^(-1/6.6)  (eq. 10)
    alpha = (0.58 - 0.007 Bz) [1 + 0.024 ln(Dp)]             (eq. 11)

Table 1, "After Fit" column, with standard deviations from 200
Monte Carlo refits:

    a1 = 10.22  +/- 0.10     (R_E)
    a2 =  1.29  +/- 0.06     (R_E)
    a3 =  0.184 +/- 0.007    (per nT)
    a4 =  8.14  +/- 0.39     (nT)
    a5 =  6.6   +/- 0.5      (pressure exponent, r0 ~ Dp^(-1/a5))
    a6 =  0.58  +/- 0.01
    a7 = -0.007 +/- 0.0005   (per nT)
    a8 =  0.024 +/- 0.0004

Units: Bz in nT, Dp in nPa, r0 in R_E, theta the solar zenith angle
from the aberrated Sun-Earth line. Frame: aberrated GSM, cylindrically
symmetric about that line (page 17,692). The paper reports a standard
deviation of 1.23 R_E between the analytic surface and the observed
crossings (page 17,697).

The store row for alpha therefore reads eq. 11 / Table 1 rows a6-a8;
the r0 row reads eq. 10 / Table 1 rows a1-a5. The L-305 block's alpha
line, previously tagged "not read", matches the paper exactly.

A secondary source found in search (Kumar and Pulkkinen, EGUsphere
preprint 2024-1113) prints the a8 term as 0.24. That is a typo in the
preprint; the primary says 0.024. Recorded here so nobody re-derives
the doubt.

### 2. Shue's fitting range -- READ, and it is inherited from the 1997 database

The 1998 coefficients come from refitting the SAME crossing database
as Shue et al. (1997) with the new functional forms (page 17,697:
"using all dataset values"). That database is ISEE 1 and 2, AMPTE/IRM
and IMP 8 crossings, and the 1997 model's stated validity is

    -18 nT < Bz < 15 nT,   0.5 nPa < Dp < 8.5 nPa     (page 17,693)

Shue 1998 states no new range of its own. It EXTRAPOLATES the improved
model to Dp = 50-60 nPa in Figures 10 and 13 and argues the new forms
saturate sensibly there, but that is an argument about behaviour, not
a fitted range. So the served validity range for the Shue rows is the
1997 range above, with a note that the nonlinear forms were introduced
precisely so extrapolation beyond it stays physical.

On the zenith-angle extent, which the tail hover needs: the paper does
not state the angular range of the crossings. Figure 6 (page 17,695)
plots the model's own uncertainty out to 120 degrees solar zenith
angle, which is the furthest the authors evaluate it; that is the best
the primary gives, and it supports the L-305 hover wording "fitted on
near-Earth crossings, not the distant tail" without putting a number on
it. If a number is wanted, it has to come from Shue 1997 (Table 1 and
its data description), which is NOT read.

Model conditions of the store (p = 2 nPa, Bz = 0) sit inside the
fitted range. Checked by hand: at those conditions r0 = 10.25 R_E and
alpha = 0.59, which reproduces the two figures L-305 already records.

### 3. Jelinek's six values -- CONFIRMED against the PDF

Source: Jelinek, K., Z. Nemecek, and J. Safrankova (2012), J. Geophys.
Res. 117, A05208, doi:10.1029/2011JA017252. Access route: Wiley via
Readcube (Tony's download, 2026-09-10).

Equations 13-16, page 5 of 8, and the fit text in section 4 (page 4):

    R_MP = 12.82 p^(-1/5.26)          (eq. 13)
    R_BS = 15.02 p^(-1/6.55)          (eq. 14)
    lambda_MP = 1.54, lambda_BS = 1.17  (section 4, text after eq. 11)
    x    = R0 p^(-1/eps) - tau^2 / 2                 (eq. 15)
    R_yz = sqrt(2 R0 p^(-1/eps)) * tau / lambda      (eq. 16)

R0 is the stand-off at p = 1 nPa; p in nPa; frame aberrated GSE,
rotational symmetry about the aberrated x axis assumed (section 3).
No uncertainties are given on these six numbers; the paper gives the
scatter of crossings about the model instead (Fig. 7: standard
deviation 0.69 R_E bow shock, 0.76 R_E magnetopause).

All six match what L-305 recorded from the WDS'10 proceeding. This
read was made with the L-305 block open, so like the 2026-09-10 read
it is a check that the ledger matches the paper, not an independent
transcription. Two reads by two sessions now agree with the PDF.

Checked by hand at p = 2 nPa: R_BS = 13.51 R_E and R_MP = 11.24 R_E,
reproducing L-305's seam figures.

### 4. Jelinek's local-time envelope -- CONFIRMED

Section 2, paragraph 9, page 2: regions identified "on whole dayside
parts of orbits and even toward the flanks in the range of +/- 7 hours
of local time around the local noon." Conclusion, paragraph 30, page
8: models recommended "for the dayside low-latitude region in the range
of solar wind dynamic pressures from 0.6 to 11 nPa." Both as L-305
records them. The 105-degree cut is the +/- 7 h envelope expressed as
an angle from the nose (7 h x 15 deg/h); the paper gives the hours,
the degrees are the store's conversion.

## What this does NOT settle

- Shue 1997 is not read. It is the only place a numeric zenith-angle
  range for the Shue fit would come from.
- Nothing is landed. This file is the read record for the next desk
  session's L-305 patch; the L-315 fingerprint lesson applies to that
  patch (text outside the INDEX zone, line endings normalised).

## Gap item 2 -- the tail extent, CLEARED on the abstract route (later the same day)

Source, found by Tony via a Sonnet search, 2026-09-11: Ness, N. F.,
C. S. Scearce, and S. C. Cantarano (1967), Probable observations of
the geomagnetic tail at 10^3 Earth radii by Pioneer 7, J. Geophys.
Res. 72(15), 3769-3776, doi:10.1029/JZ072i015p03769. Access route:
ABSTRACT, open at https://doi.org/10.1029/JZ072i015p03769; full text
walled (Tony's check from his phone; screenshot on file). The abstract
states the claim with its qualifier, which is what the Access Standard
requires of a partial source.

What the abstract supports: Pioneer 7 crossed the downstream
interaction region at 900-1,050 R_E (26 Sep - 3 Oct 1966); the field
measurements suggest some field lines there still connect to Earth
through the tail; a coherent, well-ordered tail with a neutral sheet
was NOT observed; the tail appears to break into intermingled
filamentary flux tubes by several hundred R_E.

What the hover may therefore say, and what changes:
- "past 1,000 R_E" becomes "to about 1,000 R_E" -- the source is a
  crossing at 900-1,050, not a lower bound.
- The qualifier travels with the figure: signatures connected to Earth
  were found out there, but not a coherent tail; the paper's own title
  says "probable". Show the Envelope: the drawn surface stops at the
  served 100 R_E; the tail's signature reaches roughly ten times that;
  by then it is filaments, not a sheet.
- The served magnetotail row's `_declared` 1,000 R_E gets this row as
  its source, status declared -> V_SOURCED (abstract, open), with the
  qualifier in the row's note so a later session does not strip it.

Not done here: no second, fuller-text authority was sought. One
accessible authority carrying the result clears the standard; a later
open source (a review with the Pioneer 7 result restated) would let
the hover drop "probable", and that is a slice-2 nicety, not a gap.

## For the next desk session

Fold sections 1-4 above into L-305 as a dated bullet, close Gap item 1,
and give each of the eleven store rows (Shue a1-a8, Jelinek R0 / eps /
lambda for the bow shock) its equation or table number and access route
from this record. Tony-action items 1-2 of the 2026-09-10 handoff
(run patch_L321_close.py and ledger_index.py, then push) come first;
this patch chains after them.

Written September 2026 with Anthropic's Claude Fable 5.1.
