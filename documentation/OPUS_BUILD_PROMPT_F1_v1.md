# Build request: F1 -- Feature-Config Serving Pipeline (implement from manifest)

**To:** Claude Opus
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial relay)
**Attached:** `PHASE2_F1_BUILD_MANIFEST_v2.md`

## What this is

Design is converged, and the build contract is written: implement code
from the attached manifest. This is not a design review and not another
manifest pass -- the manifest itself is the reconciled product of two
independent manifest attempts (Claude Fable and GPT, working from the same
converged handoff), a comparative review that verified one of them caught
a real bug the other missed, and Tony's own corrections to a citation
question the review surfaced along the way. Build from it.

## How the manifest got here (context, not something to re-litigate)

Two independent instances (Fable, GPT) each wrote a manifest from
`PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md`. An independent
comparative review (Claude Sonnet 5, re-verifying claims live against
HEAD rather than trusting either manifest's word) found Fable's manifest
caught a real, verified bug GPT's missed entirely: `propagate_marker`'s
mean motion (`n = K_GAUSS / a**1.5`, `K_GAUSS = sqrt(GM_sun)`) is correct
for heliocentric bodies but wrong by ~3 orders of magnitude for
planetocentric ones (moon, io, titan, charon) -- confirmed by direct
arithmetic against `gallery/assembler/render_orbits.py` live, not taken on
either AI's say-so. The attached v2 manifest is Fable's manifest as base,
with that bug fixed in, GPT's schema-naming catch and stop-condition/
report-template sections grafted in, and one further correction made
after delivery: an earlier draft of section 4.2 mis-stated that Jupiter's
ring colors were "uncited" and should be excluded on that basis. On
inspection, a real citation *does* sit above Jupiter's `ring_params` dict
(`# Source: NASA Jupiter Ring Fact Sheet; Galileo spacecraft data`) --
but Tony judged that citation only ever covered ring geometry, and reading
it as also covering color was an overstatement neither manifest author
nor the reviewer should have made. Section 4.2 in the attached copy has
been rewritten to reflect this correctly: Jupiter's and Saturn's ring/
belt colors are excluded from the served schema, and the source files now
carry in-line comments saying so explicitly (see `jupiter_visualization_
shells.py` `create_jupiter_ring_system` and `saturn_visualization_shells.py`
`create_saturn_ring_system`, both edited July 16, 2026). None of this
changes what you build -- the served schema already excluded these colors
-- but if you happen to read those source citations directly while
working nearby, don't read them as covering color; the in-line comments
now say so.

**Do not re-open the settled design decisions** (the physics, the trust
schema shape, the phasing, the moon-exclusion rule, the Jupiter feature
swap). **How you implement them is yours** -- same standing invitation as
the manifest-authoring pass: if a genuinely better implementation
approach occurs to you within what's in scope, take it; if a settled
decision looks wrong as you build against it, say so explicitly and flag
it for Tony rather than silently working around or overriding it.

## Session base -- re-pin yourself, don't trust this document's numbers

Manifest written against orrery HEAD `13acfcf434f62ad7e9f92253fbf57c21994e362c`,
gallery HEAD `953c650edc8dbd35ab11ec1720f8283987d63901`. Re-confirm both via
`git ls-remote` yourself before relying on any code-level claim in the
manifest -- a matching HEAD is the whole round trip, not something to
assume from a document. **Push the attached manifest to
`documentation/PHASE2_F1_BUILD_MANIFEST_v2.md` before you start if it
isn't already current there** -- the repo's copy at HEAD `13acfcf4` predates
the section 4.2 correction described above; verify you're building from
the attached copy (or a freshly re-pushed one), not a stale repo copy of
the same filename.

## Two independent bite-sized chunks (per the manifest's own split)

**Chunk 1 -- feature-config porting (manifest secs 3-4).** The three
config edits (Earth, Jupiter, Saturn) plus empty `"features": {}` for
Halley/Encke/all other objects, and the `derive_served` rewrite so
`feature_configs.json` is assembled from config instead of written empty.
Every served value traces to a specific file and line in the manifest;
schema shape mirrors each source's own dict shape (see manifest sec 4.1's
"mirror the orrery's own dict shapes" convention -- do not introduce a
`components`/`layers` abstraction the settled convention doesn't call for).

**Chunk 2 -- F1a trust/served_window.** The measured two-body error-rate
approach, with FLAG-2's fix built in from the start this time
(planetocentric mean motion must use the parent body's GM, not the Sun's
-- verify your propagation function branches correctly for moon-category
objects before wiring it into the trust measurement, not after). Pinned
interim-minimum rule: exclude only `category == "moon"`. Tolerance 0.5
deg globally, build against it as given. Partial-measurement-failure
semantics are settled per Tony's explicit call: **any** participating
object's failed measurement nulls the global `served_window` (with a
warning) rather than computing a minimum from survivors only -- a
wrong-but-present number is invisible to the resolver, null is visibly
degraded. Don't reopen this; it was a genuine two-way disagreement
between the source manifests and Tony resolved it directly.

Keep these as separate, independently buildable units, per the manifest's
own scoping -- don't merge them for tidiness.

## Boundaries -- scope limits, not creativity limits

- Leave `resolver.py` / `cache_reader.py` untouched. The new `trust`
  blocks are additive data the current resolver already tolerates.
- The uncertainty-envelope UX (client-side rendering of `trust`/
  `served_window`) is Mode-5 territory -- Tony confirms the visual
  treatment once there's a render to look at. Don't build that from prose.
- Apophis gets a normal (non-anchored) trust measurement this pass --
  close-encounter anchoring is a sharpened direction, not a build task.
- The sun-oriented feature category (magnetosphere envelopes/bow shocks,
  sodium tail, comet comae/tails) is out of scope this pass.
- `event_link` (L-119) and the info-card feature (L-123) ride the same
  `derive_served` file but are sequenced after this Gap -- don't pull them
  in.

## Before you deliver

- Run the manifest's own stop-condition list (sec 5) and produce the
  implementation report per its template (sec 9-10) -- these were GPT's
  contribution to the reconciled manifest and Tony wants them used, not
  just present as reference.
- This project runs an Agentic Pre-Test Protocol before any complete file
  or agentic delivery (py_compile, xvfb headless run on a throwaway copy,
  live-dispatch smoke test for any data-content change) -- load and run it
  if you have access to the skill; if not, at minimum py_compile every
  changed file and describe what you could not runtime-test so Tony knows
  what's still unverified.
- Follow the project's existing coding conventions: the marker/legendgroup/
  hover-text patterns already in use, ASCII-only in delivered code, credit
  line in touched module docstrings (`# Module updated: July 2026 with
  Anthropic's Claude Opus [version]`).
- Cite every served value to its source file and line in your
  implementation report, the way the manifest itself does -- this is a
  data-serving pipeline; provenance discipline applies to what you ship,
  not just to the design documents describing it.

## Ref

`PHASE2_F1_BUILD_MANIFEST_v2.md` (attached, the build contract);
`PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md` (converged design, for
background if needed); `F1_MANIFEST_COMPARATIVE_REVIEW_v1.md` (how the
manifest was reconciled, for background only); L-118 (F1, parent ledger
item); L-124/L-125 (the color-citation correction referenced above, for
background only -- not part of this build).

---
Prompt written July 2026 with Anthropic's Claude Sonnet 5.
