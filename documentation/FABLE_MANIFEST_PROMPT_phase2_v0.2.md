# Manifest request: Phase 2 Assembler — Design Handoff v0.2 (closed)

**To:** Claude Fable
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial relay)
**Attached:** `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.2.md`

## What this is, and how it differs from a review

Claude Opus 4.8 already reviewed the prior version (v0.1) of this handoff —
that review independently re-verified the technical claims, caught two real
errors (a function miscount on our side, a file-citation slip on Opus's
side — worth knowing this project catches mistakes in both directions), and
surfaced three coupled open design questions. All three have since been
resolved through further design conversation; Section 4 of the attached
document explains what dissolved and why.

**This is not another review pass. This is a request to build the design
manifest** — the executable build contract for the Phase 2 solar system
assembler, written against current HEAD. Tony wants this pass to have real
latitude: **full range of decision for innovation and broad reach.** Don't
just transcribe the handoff into contract form. If you see a better
architecture, a missing consideration, an opportunity the handoff's authors
didn't think of, take it — that's the point of asking you specifically for
this pass rather than continuing with the same instance that wrote the
design.

## Session base — re-pin yourself, same discipline as always

Handoff written against orrery HEAD `af58f7f87f609f2a632853f50a362ed3ebb30d49`,
gallery HEAD `a08bdd10769f93d7d42601c76fcc14786251ef05` at the time of
writing. Both have since moved — current as of this prompt: orrery HEAD
`8bce8354b6c9ae37b1e941f536cfc6f0a0a435c8`, gallery HEAD
`e864fd426a6bcffc478fe5ed9452a4dfc9159766` (independently re-verified via
`git ls-remote`, not just carried from Tony's report). That move covers the
Halley add-object work and an L-026 CRLF→LF fix — neither changes anything
this handoff's design conclusions depend on, but re-pin yourself anyway
before relying on any code-level claim; the project's standing rule is that
a matching HEAD is the whole round trip, not something to assume.

## Suggested starting point (not a constraint)

1. Read the attached handoff in full, including Section 4 (what dissolved
   this session) — it's there so you understand *why* the design looks the
   way it does, not just what it concludes. If you disagree with any of
   those resolutions, say so — they're this session's best read, not locked
   in stone.
2. Spot-check a few of the verified claims against current HEAD if anything
   seems surprising or load-bearing enough to matter (the pattern so far:
   independent re-verification has caught something real almost every time
   it's been tried in this project). Use your judgment on how much of this
   is worth your time versus getting to the actual manifest.
3. Build the manifest for the 7 golden artifacts (Section 3) plus L-080's
   co-evolving harness (Section 7). Structure, scope, and level of detail
   are yours to decide — write it the way you'd want to hand it to an
   implementer, since that's what it is.
4. Where the handoff's scope notes something as explicitly excluded (Section
   2's functional boundaries, the deferred L-046/L-104 track) — respect
   those boundaries unless you think there's a real reason not to, in which
   case explain the reason rather than silently expanding scope.

## Conventions in force (same project, same rules)

- Tag claims `[verified @<sha>]` vs `[carried]`.
- Fetched-not-recalled: pull the actual file at the SHA you pinned, don't
  reconstruct from training-data memory of similar codebases.
- ASCII-only, LF line endings for any code fragments or examples.
- Tony is the integrator between AI instances; Sonnet is carrying this
  relay on this side. Flag anything you want routed back for a decision
  rather than deciding it silently on Tony's behalf.

---
Prompt written July 2026 by Claude Sonnet 5 for Tony Quintanilla's Mode 7 relay.
