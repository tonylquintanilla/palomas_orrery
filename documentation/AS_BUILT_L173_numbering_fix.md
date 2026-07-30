# AS-BUILT: L-165/L-173 Numbering Collision Fix + Nightly Run Confirmation

Tony Quintanilla, PE | Claude Sonnet 5 | July 29, 2026

**Built on:**
- gallery @ `f4ce24cb68d2aa5834c6abcf98a1d7e0d5a68e8a` (verified: this SHA is
  the tip; `d49fd0b3` "data: nightly 2026-07-28" is its direct parent)
- orrery @ `90d022e4e4b39c19698e6d4ce64087d66ae35ac1`

**Type:** BUILD SESSION (gallery repo) + DOCUMENTATION (orrery ledger).
Folded into this thread per your request to close that parallel track too.

---

## What I verified before touching anything

**The nightly-run good news, independently confirmed, not just trusted:**
commit `d49fd0b3` exists exactly as described -- "data: nightly
2026-07-28", Jul 28 17:00:21 -0500. `coverage_index.json` at that
commit: 12 objects (earth, jupiter, saturn, moon, io, titan, pluto,
charon, apophis, voyager_1, encke, halley), `generated:
2026-07-28T22:00:21` -- matches the commit's local time converted to UTC
exactly. I didn't independently re-derive which object's window
mathematically sets `served_window` (that requires tracing the resolver's
internal vote, which I didn't do), but every other fact in the claim
checks out precisely, including the timestamp match across the timezone
conversion.

**The numbering collision, confirmed exactly:** `gallery_cache_builder.py`
had "L-165" at lines 41, 1195, 1428 as claimed. The test file had it in
**eight** places, not six -- the ledger draft's own "2 new test cases, 6
new checks" is the correct count for the actual assertions; the "six" in
the follow-up comment undercounted by missing the two section-header
comments (`# --- L-165/Option 3: ... ---`) alongside the six `check()`
labels. Minor, doesn't change the fix.

**Max ledger handle confirmed at 172** (matches this thread's own recent
work -- L-170/171/172 opened here), so **L-173** is correct.

## What I did

Renamed `L-165` -> `L-173` in all eleven places across both files
(transactional patch, each anchor asserting exactly one match before
replacing -- pure text, zero behavior change). Then verified:

- Both files `py_compile` clean, ASCII/LF clean.
- **Ran the actual offline test suite: 144 checks, 0 failures** --
  identical to the 144/144 the handoff already reported, confirming the
  rename didn't touch behavior.

Diffs attached (`.patch` files) for both `tools/gallery_cache_builder.py`
and `tools/test_gallery_cache_builder_offline.py`.

## Ledger entry to add (orrery repo)

Paste into `LEDGER_CONSOLIDATED.md`, `### W.Done` or wherever closed
gallery items live (matching L-151's placement):

```
#### [L-173] Post-swap completeness guard -- never commit an unverified promotion
<!-- L:173 status:DONE upd:2026-07-29 section:C flag: rice:3/3/95/1 -->
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
  -- 144/144 total, output matching the sandbox run exactly. Real-world
  exercise: the 2026-07-28 nightly run (`d49fd0b3`) is the first fully
  unattended trigger since the guard went live (2026-07-27) -- ran clean,
  guard did not false-positive, 12 objects served correctly. The one
  originally-open item (a live exercise of the guard) is now closed.
**Gap:** none -- built, tested twice (sandbox + live), deployed
(gallery @f4ce24cb, guard live since fc3a0a68), and now exercised once for
real on a healthy run. A live exercise of an actual FAILURE (not just a
healthy run) remains unobserved -- not a gap in the guard, just something
that hasn't happened yet.
**Ref:** tools/gallery_cache_builder.py (verify_promoted_data,
atomic_swap_dir call site); tools/test_gallery_cache_builder_offline.py;
L-165 (the succession-planning item this was originally, incorrectly,
filed under -- numbering collision corrected 2026-07-29);
documentation/TESTING_PROTOCOL.md.
```

Then run `ledger_index.py`.

## What's still genuinely open (unchanged from the handoff, not touched here)

Per the handoff's own Part 3/Part 5 -- none of this is urgent, none of it
was asked for right now, so I didn't touch it:
- L-165 itself: domain-renewal decision, GitHub Actions migration question
  -- both need a dedicated design session with you, not a quick call.
- L-111's remaining backlog (gap-aware catch-up fix, `--add-object`,
  deferred hardening N7/N8/N10/N11).
- L-154 (the JS feature-rendering layer) -- already tracked in the
  provenance cluster work this thread has been doing; same item, no new
  status here.

---

*Built July 2026 with Anthropic's Claude Sonnet 5.*
