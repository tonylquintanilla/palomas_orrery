Built on:
- orrery: 2ad14a881c5f3190b50c41c8ab362aeb3c65c97a at https://github.com/tonylquintanilla/palomas_orrery
- gallery: fc3a0a68046c5b4c12d30406705e75ae2e5e82ea at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Session: Sonnet 5, spanning 2026-07-21 through 2026-07-28
Ledger handles touched: L-118, L-149, L-151 (closed prior to this handoff's
scope), L-111 (revised), L-165 (opened -- see collision note below), and a
new handle still needed for the completeness guard (see Part 1).

---

# Session Handoff -- Layer 3 completion, deployment-model decision, and succession planning

## Part 0 -- scope of this document

M2 (L-149, L-118) and Layer 1-2 of the testing protocol were already closed
and documented earlier this same session, with their own addendum
(M2_TESTING_PROTOCOL_ADDENDUM.md) and master plan updates. This handoff does
not repeat that -- it picks up from Layer 3 (the nightly Task Scheduler) and
covers everything since: getting it working, a real incident and its fix,
an operational-policy decision that had been sitting open since July 10, and
a new, unresolved design question about long-term site survivability.

## Part 1 -- CORRECTION NEEDED: a ledger numbering collision I introduced

**This should be fixed before anything else, because it's already live in
committed code, not just in conversation.**

L-165 was correctly assigned to "Site continuity if there is no active
administrator (succession / legacy planning)" -- checked against the live
ledger at the time, applied cleanly, confirmed present at current HEAD.

Shortly after, when building the post-swap completeness guard (informally
called "Option 3" through the conversation), I reused "L-165" again in
gallery_cache_builder.py's code comments, its module credit line, and in
the new test case names in test_gallery_cache_builder_offline.py -- without
re-checking the ledger first. That was a mistake on my part. The succession
item legitimately owns L-165; the completeness guard needs its own number.

**The fix, once you have a moment:**
1. Check the live ledger for the current true max L-handle (other sessions
   are actively adding items in parallel -- it was already past L-168 as of
   this handoff, so don't reuse that number either without checking fresh).
2. Add a new ledger entry for the completeness guard under that fresh
   number. Suggested text (renumber the placeholder before using):
   ```
   #### [L-1XX] Post-swap completeness guard -- never commit an unverified promotion
   <!-- L:1XX status:DONE upd:2026-07-27 section:C flag: rice:?/?/?/? -->
   - **Origin.** 2026-07-24: a scheduled (Task Scheduler batch-logon) run's
     atomic swap failed to complete its second half, leaving data/solar-system
     empty. Nothing caught it; a human saw the resulting mass deletion in git
     and reasonably mistook it for routine cleanup (committed and pushed as
     "automatic," reverted after the fact).
   - **What.** Two checks added to run_build(), both after the swap and before
     any commit: (1) the swap call itself is now wrapped in try/except -- if
     it raises, no commit is attempted and the failure is logged clearly;
     (2) even if the swap doesn't raise, verify_promoted_data() reads
     coverage_index.json fresh from disk (not the in-memory copy) and confirms
     the object set and generated timestamp match what was just built. Either
     check failing skips the commit entirely and leaves cleanup to the next
     run's existing recover_incomplete_swap() self-heal.
   - **Verified.** Both failure modes simulated in the offline suite (2 new
     test cases, 6 new checks) and confirmed independently on Tony's machine
     -- 144/144 total, output matching the sandbox run exactly.
   **Gap:** none -- built, tested twice (sandbox + live), deployed
   (gallery @fc3a0a68). One real-world exercise of the guard on an actual
   unattended run is still pending (see Part 3).
   **Ref:** tools/gallery_cache_builder.py (verify_promoted_data,
   atomic_swap_dir call site); tools/test_gallery_cache_builder_offline.py;
   L-165 (the succession-planning item this was originally, incorrectly,
   filed under); documentation/TESTING_PROTOCOL.md.
   ```
3. Do a find-and-replace pass in both `gallery_cache_builder.py` and
   `test_gallery_cache_builder_offline.py`, changing the `L-165` references
   (comments, docstring, credit line, and the 6 test names) to the correct
   new number. Purely textual -- the code's behavior doesn't change, only
   what it's labeled.

## Part 2 -- what closed this session

**Layer 3 (nightly Task Scheduler), fully validated:**
- Task set up correctly: account `tonyq`, daily trigger, `--nightly --commit`,
  start-in = repo root, "Do not start a new instance" concurrency guard.
- Confirmed a Windows Hello PIN cannot be used for "run whether logged on or
  not" -- needs the real account password (confirmed accepted).
- Confirmed Task Scheduler's own native email/message actions are deprecated
  since Windows 8 and don't work -- any alerting has to live in the script
  itself, not a second Task Scheduler action (relevant background for L-165).
- One real incident (2026-07-24): swap failure -> empty data dir -> mistaken
  for a deletion -> committed -> reverted. Root-caused (most likely an
  OneDrive file lock during promotion, same pattern seen -- always benign --
  in every interactive run this week) and now guarded against (Part 1).
- Trigger time moved from noon to 5 PM, matching when the machine is
  reliably on.
- Multiple clean, fully unattended nightly runs since (7/25, 7/26, 7/27),
  each independently verified against the live repo, not just trusted from
  the commit message.

**L-111 (Gallery builder Pass 5) -- deployment model sub-question resolved:**
Revised 2026-07-27: full automatic fetch AND push adopted (superseding the
July 10 "manual push" decision), on the strength of the week's real testing
plus the new completeness guard. **The rest of L-111 is NOT closed** -- see
Part 3. This was checked directly against live ledger text, not assumed.

**L-151 (gallery-assembler skill)** -- confirmed all four "must carry"
points genuinely present in the live skill file; flipped to DONE.

**Two housekeeping fixes** -- `test2.html`'s stale internal filename
references (lines 3 and 22) corrected; `PHASE2_ARTIFACT1_AS_BUILT.md`
section 7 corrected (via a simpler global replace than originally proposed
-- minor side effect noted at the time, not re-litigated here).

## Part 3 -- what remains open

**On L-111 specifically** (checked the complete entry, not just the piece
we were actively discussing):
- **Gap-aware catch-up (correctness).** The nightly fetch uses a fixed
  7-day trailing window anchored to "today." An outage longer than 7 days
  silently and permanently skips the gap days -- no error, no catch-up.
  Explicitly accepted as an open risk when the deployment model was
  revised, not fixed. Real fix: anchor the refresh window to the archive's
  last date instead of a fixed offset.
- **Pass 5, Q1** -- `--add-object <slug>` one-time backfill flag. Untouched,
  unrelated to anything else this session.
- **Deferred hardening** -- N7 (UTC-only date arithmetic, DST immunity), N8,
  N10, N11. None addressed.
- **Cleanup bullet** -- mostly untouched, except "scheduled-task working
  dir" is very likely already satisfied by this week's Task Scheduler setup
  (start-in = repo root, confirmed working) -- worth a quick check-off
  rather than treating as open.
- **Gap section's live-Horizons dependencies** (Tp= header, elements units,
  epoch scale) were probably already settled by this session's extensive
  real-Horizons testing (M2 Steps 1-3) -- worth checking against
  `TESTING_PROTOCOL.md` before assuming this note is still accurate.

**On the completeness guard itself:** built, tested twice, deployed --
but not yet exercised for real by an actual unattended failure. The offline
simulation is strong evidence, not the same as watching it fire live.
Nothing to do here except keep an eye out.

**On L-165 (succession planning) -- genuinely unresolved, bigger scope:**
- Domain renewal decision (pre-pay years in advance vs. accept the free
  `.github.io` URL as a fallback identity) -- a real-world, non-technical
  decision, still pending.
- Whether continued fetching matters enough as part of the legacy to
  justify migrating the nightly builder off Tony's personal laptop and
  onto GitHub Actions -- a genuine open architectural question, not
  started, deliberately left for a dedicated design session (see Part 5).
- The numbering fix in Part 1.

## Part 4 -- how this fits the master plan

**The Task Scheduler/reliability work (Layer 3, L-111, the completeness
guard) is operational hardening of an already-decided architecture, not new
design.** The architecture itself -- nightly fetch, atomic swap, static
JSON serving, the trust/served_window system -- was decided and built back
in Phase 1b/M2, and is already documented in the master plan's SS3a (Data
Serving Architecture). Nothing this week changed that architecture. What
changed is confidence that the *existing* design survives a specific,
real-world failure mode when running unattended, and a settled answer to
an operational policy question (automatic vs. manual push) the original
design had left open. This belongs in SS3a as an addendum/operational note,
not as a new section -- it fills in a detail the architecture always
assumed would eventually need settling, rather than revising the
architecture itself.

**The succession-planning discussion (L-165) is different in kind --
this is preliminary design, not settled architecture.** It surfaces a real,
previously-undiscussed question (what happens to the site with no
administrator, ever again) and reaches one settled structural insight (the
trust/served_window system already provides graceful degradation, which is
genuinely good news requiring no new design) -- but the two live open
questions inside it (domain funding, and whether to migrate the fetch
engine to GitHub Actions) are exploratory, not decided. If the master plan
gets touched for this, it should go in SS7 (Open Decisions) or as a new,
clearly-marked "not yet decided" note near SS3a, not folded into the
architecture sections as if it were settled.

## Part 5 -- Tony-action items, roughly in priority order

1. Fix the L-165 numbering collision (Part 1) -- the only thing here with
   any urgency, since it's sitting in live, committed code.
2. Whenever there's focus time: decide the L-165 domain-renewal approach,
   and whether the GitHub Actions migration is worth pursuing (Part 3/4).
3. Whenever there's focus time: the remaining L-111 backlog (gap-aware
   catch-up fix, `--add-object`, deferred hardening, cleanup) -- none of
   it urgent, all of it real.
4. The still-open, larger item from earlier this session, unrelated to any
   of the above: writing the feature-rendering JS layer (ring/shell/belt
   consumers) that actually unblocks Artifact 2 (Jupiter/Saturn).

Nothing above is blocking anything else. The site is live, current, and
updating on its own every night.

## Ref

M2_TESTING_PROTOCOL_ADDENDUM.md; MASTER_PLAN_INTERACTIVE_GALLERY.md SS3a;
LEDGER_CONSOLIDATED.md (L-111, L-118, L-149, L-151, L-165); PHASE2_F1
handoffs; tools/gallery_cache_builder.py; tools/test_gallery_cache_builder_offline.py.

---

Session written July 2026 with Anthropic's Claude Sonnet 5.
