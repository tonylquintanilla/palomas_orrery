# Manifest request: F1 — Feature-Config Serving Pipeline (build contract for Opus)

**To:** Claude Fable
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial
relay)
**Attached:** `PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md`

## What this is, and how it differs from the earlier ask

You were asked once already, this round, for creative input on one piece
of this problem (`FABLE_PROMPT_served_window_trust_bound_v0.1.md` — the
served-position trust-bound question). That response was reviewed,
independently spot-checked (including one specific numeric claim,
Earth's-Moon evection amplitude/period, verified against a published
source rather than accepted on your word alone), and confirmed point by
point with Tony. It's now folded into the attached handoff as settled
design (§6).

**This is a different ask: build the executable manifest — the build
contract another Claude instance (Opus) will implement code from.** The
*design* is converged (the attached handoff's header says so explicitly:
"Status: CONVERGED — ready for a build manifest"). That means the physics
and the architecture-level decisions (measured error rate over
divergence-from-mean, per-object trust schema, F1a/F1b phasing, the
moon-exclusion rule, the Jupiter feature swap, and so on) aren't up for
re-litigation. **It does not mean transcribe the handoff into contract
form mechanically.**

## Real latitude on the manifest itself — same as last time

**Tony wants this pass to have real latitude: full range of decision for
innovation and broad reach, at the manifest-building level.** If you see a
better implementation architecture for either chunk, a missing
consideration the handoff's authors (Tony and Claude Sonnet 5) didn't think
of, a cleaner way to structure the code than what the handoff's prose
implies, or an opportunity worth taking — take it. Don't just transcribe.
This is the same standing invitation as the Phase 2 assembler manifest
request: the reason to ask you specifically for this pass, rather than
having the same instance that wrote the design also build the contract, is
so a genuinely independent read can catch what a second design pass on the
same instance wouldn't.

The distinction that matters: **settled design decisions** (the physics,
the schema shape, the phasing) aren't open for debate — reopening those
would mean going back to Tony, not deciding it yourself in the manifest.
**How to implement them well** is entirely yours. If a settled decision
looks wrong to you as you build against it, say so explicitly and flag it
for Tony rather than silently working around it or silently overriding it
— but do say so; don't just default to compliance if something looks off.

## Session base — re-pin yourself

Handoff written against orrery HEAD `f961b4424fd633595286c2764a2ebd19df677236`,
gallery HEAD `953c650edc8dbd35ab11ec1720f8283987d63901` — unchanged across
this entire design round (re-confirmed via `git ls-remote` multiple times
during the session, most recently just before v0.4). Re-pin yourself anyway
before relying on any code-level claim — a matching HEAD is the whole
round trip, not something to assume from a report.

## Two independent bite-sized chunks, not one monolith

**Chunk 1 — feature-config porting (handoff §3-5).** `objects_config.json`
edits for Earth, Jupiter, Saturn (plus empty `features: {}` for
Halley/Encke) and the `derive_served` rewrite so `feature_configs.json` is
assembled from config instead of written empty. Every value cited to a
file and line; schema shape and naming convention settled.

**Chunk 2 — F1a trust/served_window (handoff §6).** The measured two-body
error-rate approach (reusing `gallery/assembler/render_orbits.py`'s
already-validated `solve_kepler`/`propagate_marker`), the per-object
`trust` schema, and the pinned interim-minimum rule (exclude only
`category == "moon"`) for the conservative global `served_window`.
Tolerance adopted at 0.5° globally — build against it as given; it's
flagged in the handoff as an estimate to be visually checked once Wave 1
renders, not something to re-derive here, but if you have a genuinely
better way to *apply* it (not a different number, a better mechanism) say
so.

Keep these as separate, independently buildable manifest units — that
split is deliberate scoping, not something to merge away for tidiness.

## Respect these boundaries — scope boundaries, not creativity limits

These are about *what's in scope this pass*, not a constraint on how
creatively you approach what is in scope:

- **F1b** (resolver/cache_reader consuming per-object `trust`, reopening
  Artifact 1's golden fingerprint) is separate, later, deliberately
  scheduled. Leave `resolver.py`/`cache_reader.py` untouched; the new
  `trust` blocks are additive data the current resolver already tolerates
  (its own forward-compatibility warning path ignores unknown fields).
- **The uncertainty-envelope UX** (§6.5) is Mode 5 territory — Tony
  confirms the visual treatment once there's a render to look at. Don't
  build the client-side rendering of this from prose.
- **Close-encounter anchoring for Apophis** (§6.6) is a sharpened
  direction, not a build task this pass.
- **L-119 (event_link)** and **L-123 (info card)** ride the same
  `derive_served` file but are sequenced after this Gap.
- **The sun-oriented feature category** (magnetosphere envelopes/bow
  shocks, sodium tail, comet comae/tails) — needed, not this pass.

## Suggested starting point (not a constraint)

1. Read the attached handoff in full, including the Provenance Discipline
   Notice — it distinguishes live-verified-this-session, independently
   web-verified, and adopted-but-unvalidated-estimate. Carry that honesty
   into the manifest rather than flattening it into uniform confidence.
2. Spot-check anything that seems surprising or load-bearing enough to
   matter — the pattern in this project is that independent
   re-verification catches something real often enough to be worth the
   time.
3. Write the manifest the way you'd want to hand it to an implementer,
   since that's what it is. Structure, level of detail, whether the two
   chunks become one document or two, and any implementation-architecture
   choices within them are yours.

## Ref

`PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md` (attached, full source);
`FABLE_PROMPT_served_window_trust_bound_v0.1.md` (the earlier relay this
round builds on); L-118 (F1, parent ledger item).

---
Prompt written July 2026 with Anthropic's Claude Sonnet 5.
