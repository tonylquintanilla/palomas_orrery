# Second-pass request: Phase 2 Synthesis Manifest

**To:** Claude Fable 5 and GPT (send to both, same text)
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial relay)
**Attached:** `PHASE2_SYNTHESIS_MANIFEST_v1.md`, `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md`

## What this is

You each independently built a full manifest from the same design handoff
(v0.2) — a deliberate competitive-pattern cross-check. Both were
independently re-verified against current HEAD rather than taken at face
value. That process surfaced real convergence, real divergence, and — in
one case — an error in the verification itself (a claim about
`objects_config.json` carrying an `event_link` field that turned out to be
false on direct check). All of that is recorded and resolved in the
attached synthesis. This is not a third independent build — it merges what
you both got right and resolves what you disagreed on, plus folds in one
substantive design gap (mean-vs-osculating elements) that surfaced *after*
both of you wrote, during a separate design conversation about why Kepler
propagation is even necessary given the served schema.

**This is a request to check the synthesis, not to write another one.**

## Why you're both getting this, not just one of you

The point of asking two independent systems for the same task was to see
where you'd agree and where you wouldn't — that already paid off (Fable's
deeper code-layer verification caught four real gates GPT's manifest
didn't know about; GPT's cleaner module architecture and `AssemblyContext`
proposal improved on Fable's version). The same logic applies here: a
synthesis written by a third party (Sonnet) resolving your disagreement
could itself be wrong, or could resolve something in a way neither of you
actually meant. Read it critically, not as a rubber stamp of your own
prior work.

## What to actually check

1. **Section 1's resolution table** — is it a fair characterization of
   what you each actually argued, or did something get flattened/
   misrepresented in translating your manifest into a table row?
2. **Section 3's date-resolution ruling** (Kepler propagation from
   `M0_deg`/`epoch_jd`, bounded to the freeze window, GPT's "nearest-date"
   model retired) — GPT specifically: does this land correctly given what
   you now know about the served schema (one elements snapshot per object,
   not a position range)? Fable: does the "bounded to the freeze window"
   qualifier adequately address what your own manifest left implicit?
3. **Section 4's gates** (F1/F2/F3/F4) — Fable: is the F2 correction
   (two-step fix, not one-line) fair to what you actually found, or does
   it undersell/oversell the gap? GPT: these facts came from a layer your
   original verification didn't reach — sanity-check them against current
   HEAD yourself rather than accepting them secondhand.
4. **Section 5 (mean elements)** — entirely new since either of you wrote.
   Neither of you addressed this because it wasn't yet a known question.
   Check the mechanism description and the moons-excluded reasoning on
   their technical merits.
5. **Anything from your own manifest that got dropped, weakened, or
   changed without adequate justification.** Say so plainly. A synthesis
   that quietly loses a good idea because it didn't make the merge is a
   failure mode, not a feature.

## Session base — re-pin yourselves

Orrery HEAD `8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8`, gallery HEAD
`e864fd426a6bcffc478fe5ed9452a4dfc9159766`. Verify both are still current
before relying on any code-level claim — re-verify via whatever mechanism
is available to you (`git ls-remote`, a fresh fetch, etc.), don't assume
this prompt's SHAs are still live by the time you read it.

## Conventions in force

- Tag claims `[verified @<sha>]` vs. `[carried]`.
- Fetched-not-recalled: pull actual files, don't reconstruct from training
  data.
- Flag disagreement explicitly rather than silently accepting a resolution
  — that is the entire purpose of this pass.
- Tony and Sonnet are the orchestrators on this relay; route anything you
  want decided back to them rather than deciding it unilaterally on their
  behalf. After this pass, the manifest goes to Opus for implementation.

---
Prompt written July 2026 by Claude Sonnet 5 for Tony Quintanilla's Mode 7 relay.
