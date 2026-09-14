# Review -- design record rev 2, prompts rev 3, and the L-323 ledger patch

Reviewed against orrery `62ee5149e611e325455e56bb3b09486daeea0040`
(remote HEAD at review time, confirmed by ls-remote) and gallery
`1f44673faf2acd32340bfdd4b524b6c8af5dd376`.

Tony Quintanilla, PE | reply written by Claude Fable 5.1, inside the
Paloma's Orrery Project | 2026-09-12
Skills: provenance-discipline 2.11, safe-file-editing 1.11,
ledger-and-session-records 1.11 -- all matching the manifest.

## Verdict

Proceed. All three documents check out against the repo, and the
patch will apply. Four small things below; none holds the button.

## What I verified, not read

- The four typed extents are exactly where rev 2 says: lines 745, 747
  (`earth_magnetosphere_info`, kilometres) and 892, 896 (`belt_texts`,
  Earth radii) of `earth_visualization_shells.py`; `tail_length` at
  765. The `shell_configs.py` tooltip carries no span in any frame.
  Lugaz appears in no display string at this SHA.
- The measurement correction is right, and it corrects me too. My
  review of revision 1 wrote "the tooltips say kilometres of altitude."
  I took that from the record instead of the file. The revision is
  the first document in this chain to have opened the tooltip on that
  question.
- The patch: the guard fingerprint matches the ledger at this SHA with
  the INDEX zone excluded; the 25-line Gap anchor and the stamp anchor
  each match exactly once; the file is LF; no new block, so 319 holds.
  The required-docs check before writing is the right shape -- a
  ledger cannot name a file that is not there.

## Four things to fix or decide, in order

**1. The peak rows are noted and not disposed of.** Rev 2 says twice
that the store calls the peaks R_E while the sources say L, and then
"What lands" lists only the four edge scalars. Two existing rows get
touched by this slice either way (their Notes lose the span), so the
unit change is forward-going on rows touched, not a sweep. Say whether
the peak rows' unit moves to L in the same patch or is out of the
slice with a reason. Either is fine; silence is not.

**2. "One row for the observed magnetotail extent, as an envelope"
contradicts answer 1.** Ness gives 900 to 1,050 radii. One row holding
a range is the tuple the design just rejected, and a range in the
row's prose is the Note-becomes-store class the design just named.
Two forms are honest: two scalars (`_OBSERVED_NEAR` / `_OBSERVED_FAR`
or similar), or one scalar stated as "observed to at least" with the
crossing's range on its Source line and the row's value the lower
bound. Pick one in the record; prompt 1 row 7's answer may change
which is right, so it can be provisional, but it should be a form and
not "an envelope."

**3. L is a new unit token.** The store's `# Unit:` vocabulary today is
r_earth, dimensionless, per_nt, nt, npa, km_s, deg. L is dimensionless
with a meaning, and the gallery's value/unit/source shape will carry
whatever token the row says. That is L-322 ruling 1's vocabulary
question, not this design's, but the design should name the token it
intends (`l_shell` reads better than `l` for a reader who has not met
McIlwain), so item 7 does not invent it under time pressure.

**4. Still un-homed.** The five deferred checker items from the build
review -- three `test_status_lines.py` rules, the dict blind spot, the
retired Gemini stamp -- are still in no ledger block at this SHA. Not
this patch's job. It is the same floating set as last time, one push
later.

## On the prompts

Rev 3 is ready. The two-job header is the right fix, and the frame
note says exactly what a checker needs and no more. One wording
check: prompt 3 rows 2 and 7 are [CITATION] rows for a peak the string
states in R_E and the sources state in L; the frame note covers it,
but a checker may return PARTIAL on "Citation correct?" for the frame
alone. That is a correct verdict and worth expecting, not a defect.

## The question at the end

Yes, start item 6 while the worksheets are out. It does not wait on
them: the three retired claims in `objects_config.json` are wrong today
regardless of what the checkers return. One boundary: item 6 should
NOT touch the belt `note` fields that repeat the span prose. Those
change at item 7 with the edge rows, and touching them twice is the
double-store failure again.

Written September 2026 with Anthropic's Claude Fable 5.1.
