# HANDOFF: L-162 Scope Gaps -- CENTER_BODY_RADII Named Constants

Tony Quintanilla, PE | Claude Sonnet 5 | July 28, 2026

**Built on:** orrery (palomas_orrery) @ `2ad14a881c5f3190b50c41c8ab362aeb3c65c97a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main)

**Type:** DOCUMENTATION (zero code changes, zero ledger edits made this session)

**Companion to:** `LEDGER_CONSOLIDATED.md` [L-162] detail block;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md` sections 3a/4;
`MASTER_PLAN_UPDATE_provenance_and_prep.md` Edit 3;
`MASTER_PLAN_INTERACTIVE_GALLERY.md` section 6;
`REVIEW_provenance_refactor_cluster_scoping.md` (Fable 5, 2026-07-26);
`LEDGER_SESSION_provenance_cluster_formalization.md` (Sonnet 5, 2026-07-27).

## Why this exists

This session opened to execute L-162. Three SHA round trips during the
session (`bdab167` -> `637dd77` -> `2ad14a8`) each landed real parallel-
thread work -- L-163 module atlas refactor, D3 vulnerability-ladder
calibration closing, ledger formalization, a gallery/master-plan update --
but none touched `constants_new.py`'s actual radius data, and none
resolved the two implementation decisions below. Rather than build
against an assumption, this handoff freezes the gap so it survives to
whichever session picks it up next -- this one resuming, or another
thread.

## What's verified, not just claimed

- `constants_new.py` at current HEAD: still exactly 3 named radius
  constants (`SUN_RADIUS_KM`, `EARTH_EQUATORIAL_RADIUS_KM` + polar,
  `JUPITER_EQUATORIAL_RADIUS_KM` + polar). `CENTER_BODY_RADII` still
  hardcodes all three as raw literals rather than referencing them.
  File compiles clean, 0 non-ASCII, confirmed at `2ad14a8`.
- Four independent verification passes now agree on this exact finding:
  this session, Fable 5's 2026-07-26 review, the 2026-07-27 ledger-
  formalization session, and the master plan's own section 6 entry. No
  drift, no disagreement on scope or status.
- **Correction (minor, carried across every doc including the ledger):**
  "15 remaining bodies" should read **14** -- 18 dict keys total, minus
  3 done (Sun/Earth/Jupiter), minus Planet 9 (excluded, deferred to
  L-159) = 14. The named list itself is correct everywhere; only the
  count label is off by one. Not corrected in the ledger yet -- flagging
  here rather than silently editing a shared doc without sign-off.

## The two gaps

Neither the design review, the ledger entry, Fable 5's review, nor the
formalization pass answers either of these. Both need a decision before
any file edit.

**1. Naming convention.** No doc specifies whether the 14 new constants
should be plain (`MARS_RADIUS_KM`, matching `SUN_RADIUS_KM`) or type-
labeled (`MARS_EQUATORIAL_RADIUS_KM`, matching the `EARTH_EQUATORIAL_` /
`_POLAR_` pattern used only where a body has two values). The master
plan's own phrasing -- "matching Sun/Earth/Jupiter's existing pattern" --
leans toward plain, since Sun (a single-value body, like all 14 targets)
carries no type qualifier. Recommendation: plain. But this is Tony's
call, since Fable's Phase 3 pinning engine will reference whatever names
land here.

**2. Sun/Earth/Jupiter's literal duplication.** `CENTER_BODY_RADII['Sun']`
etc. still hardcode `695700` / `6378.137` / `71492` instead of
referencing their own named constants -- the original D5 3-body minimum
never actually landed. Every doc restates this fact; none assigns it.
One new wrinkle found this session: **L-156's own Gap line reads "fix
the `CENTER_BODY_RADII` duplication per L-162 (separate dedicated
session)"** -- worded as if the whole duplication problem, not just the
14-body extension, belongs to L-162. That's in tension with L-162's own
detail block, which scopes to the *remaining* bodies and implies
Sun/Earth/Jupiter are already handled elsewhere. Worth resolving
explicitly rather than inferring either way.

## How this maps onto the ledger and master plan

- **Ledger:** once decided, both resolutions go into L-162's block as a
  `**Note:**` line -- not a rewrite of `**What.**`; the scope stays the
  14 named bodies either way. The note records the naming choice and the
  Sun/Earth/Jupiter call. If the answer to #2 is "fix now," L-156's Gap
  line reads correctly as-is. If "leave for Fable," L-156's Gap line
  should be tightened to say "the 14 remaining bodies" so it stops
  reading as the whole fix.
- **Master plan:** no change needed. Section 6's positioning of L-162 as
  independent prep work, landable any time before or after the scanner
  build, is unaffected by either answer -- this is an in-file naming/
  scope detail, not a sequencing question.

## Next session

Once both are decided: fresh SHA pull (HEAD will likely have moved
again -- three moves in one session already), targeted bottom-up edits
per safe-file-editing discipline (14 new constants in their own
subsection above `CENTER_BODY_RADII`, the dict rewired to reference
them, docstring credit line, `py_compile` / ASCII gate), then an
as-built anchored to the pushed SHA and L-162 flipped to DONE in the
ledger.

**Open questions for Tony (decide):**
1. Plain or type-labeled naming for the 14 new constants?
2. Fix Sun/Earth/Jupiter's literals now, or leave that for Fable's build?

Session recorded July 2026 with Anthropic's Claude Sonnet 5.
