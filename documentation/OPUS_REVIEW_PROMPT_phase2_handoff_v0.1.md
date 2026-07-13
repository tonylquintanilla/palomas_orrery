# Review request: Phase 2 Assembler — Preliminary Design Handoff v0.1

**To:** Claude Opus
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial relay)
**Attached:** `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.1.md`

## What this is

A preliminary, zero-code design handoff from a Phase 2 planning session
(Paloma's Orrery web gallery project — solar system assembler, the shared
scene-spec → Plotly-figure orchestration layer that will serve both the
desktop Tkinter GUI and the interactive web gallery). Phase 1b (data-serving
pipeline, L-098) is closed; this handoff is the design pass for what comes
next. **This is a review request, not a build request** — do not produce a
manifest as part of this pass. Your review determines whether one gets
written next, and by whom.

## Session base — re-pin yourself, don't trust this line

Written against orrery HEAD `5cbbadab99d2a87b65f988c63069c64d95318688`,
gallery HEAD `a08bdd10769f93d7d42601c76fcc14786251ef05`. Time has passed
between this being written and you reading it — `git ls-remote --symref`
both repos yourself before relying on any code-level claim in the handoff.
If HEAD has moved, re-verify the specific claims below against the new HEAD
rather than assuming they still hold.

## What to actually do

1. Read the attached handoff in full.
2. **Independently re-verify the technical findings**, don't take them on
   the handoff's word — this session's own findings deserve the same
   skepticism the handoff applies to prior sessions' claims:
   - The dead-tkinter-imports finding for L-087 (Section 6): this has
     already been executed (Tony deleted the imports directly). Re-verify
     against current HEAD that the deletion is clean — no new breakage —
     rather than re-litigating whether it was safe to do.
   - The Pluto/Charon dual-fetch claim (Section 2): confirm in
     `orbit_data_manager.py`/`idealized_orbits.py` that Pluto's ID (`999`)
     defaults to `@sun` while the gallery config fetches it at `@9`, and
     that this means the current config captures only the local barycentric
     wobble, not the wide heliocentric anchor. Confirm or refute the
     "needs two composed fetches" conclusion.
   - The Halley apparition reasoning (Section 2): confirm the claim that a
     76-year period means only one apparition record is ever current (no
     live disambiguation search needed, unlike Encke's 3.3-year cadence).
     This is a piece of orbital-mechanics reasoning, not a code fact — sanity
     check it on its merits.
   - The object-cache-expansion procedure (Section 4): spot-check that
     `celestial_objects.py` and `shell_configs.py` really do carry reusable
     data for candidate objects, per the pattern described.
3. **Do NOT silently resolve the open design questions — stress-test them.**
   Present tradeoffs and a recommendation, but flag clearly that these are
   Tony's calls to make, not yours to decide by omission:
   - OQ-4 (Section 3): preset-as-defaults vs. strict vs. preset-wins, for
     encounter-preset expansion.
   - Closeup-view shape (Section 3): nested `closeup` block on one scene
     spec, vs. a small ordered pair of scene specs. Consider implementation
     cost and how it interacts with L-040 (Studio axis/scaling parity,
     still open) before recommending.
   - L-080 scene-equivalence criteria (Section 7): **not just undesigned —
     the handoff was corrected mid-session to show it can't be designed
     yet.** There's no real assembler output to characterize (Phase 0's
     pre-test is mean-element Keplerian math, not assembler output), and
     Section 2's own "no meaningful smaller slice" finding means there's no
     cheap toy output to get first either. Sanity-check this dependency
     claim on its own logic rather than proposing concrete criteria — if
     you disagree that L-080 must wait for real output, say so and why.
     Note also: the build order is now 7 golden artifacts (Section 2),
     ending with Apophis reframed as the close-encounter case — which
     itself depends on OQ-4 and the closeup-view shape being resolved
     first. Sanity-check that dependency chain too.
4. **Conclude with a build-readiness read**, not a decision: is this design
   stable enough to write a manifest against now, or are there enough real
   open questions (OQ-4, closeup shape, L-080 criteria all currently
   unresolved) that a broader adversarial pass — Fable — should happen
   first? Tony and Sonnet are orchestrating this relay on this side; your
   job is to give an honest technical read, not to route the next step
   yourself.

## Conventions in force (same project, same rules)

- Tag claims `[verified @<sha>]` vs `[carried]` per Mode 7 discipline.
- Fetched-not-recalled: don't reconstruct code facts from training-data
  memory of similar projects — pull the actual file at the SHA you pinned.
- If you disagree with a decision already reached in Section 2 ("Decisions
  reached this session"), say so and explain why — those aren't locked, they're
  this session's best read, open to a better one.
- Keep output structured (tables/headers over prose) — this gets read by
  Tony as the interpreter between AI instances, same as prior relays in
  this project.

---
Prompt written July 2026 by Claude Sonnet 5 for Tony Quintanilla's Mode 7 relay.
