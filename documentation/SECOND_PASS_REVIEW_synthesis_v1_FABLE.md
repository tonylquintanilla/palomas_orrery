# Second-Pass Review: Phase 2 Synthesis Manifest v1 -- Fable

**Type:** REVIEW (zero code)
**Author:** Claude Fable 5, Mode 7 collegial relay, July 14, 2026
**Reviewing:** PHASE2_SYNTHESIS_MANIFEST_v1.md, against my own manifest, GPT's
manifest, the v0.2 handoff, MASTER_PLAN v11, and both repos at live HEAD.
**Uploads:** 7 of 7 enumerated and read (both prior manifests, synthesis,
second-pass prompt, handoff v0.2, master plan, first-pass prompt).

## 0. Base re-pin -- the orrery HEAD moved, benignly

- Gallery HEAD: `e864fd426a6bcffc478fe5ed9452a4dfc9159766` -- UNCHANGED,
  matches the prompt. All gallery-layer claims remain live. [verified]
- Orrery HEAD: MOVED from the prompt's `8bce8354` to
  `4c4dc48075f2e4004385bf5ab19b40f0ff2597bc`. Reconciled via the GitHub
  compare API: exactly one commit ("phase 2 manifest v1"), touching only
  `documentation/` -- the two manifests, the synthesis, and the two prompts.
  Zero code files. Every code-level claim verified at `8bce8354` carries to
  `4c4dc480` unchanged; orrery re-verifications below were fetched at
  `4c4dc480` anyway. [verified]
- **Discrepancy, non-blocking:** the second-pass prompt and the synthesis
  both cite `PHASE2_ASSEMBLER_DESIGN_HANDOFF_v0.3.md` as the design source.
  No v0.3 exists in either repo at HEAD, and the upload set contains v0.2
  only. Presumably v0.3 lives on Tony's disk, un-pushed. I reviewed against
  v0.2 plus the synthesis's own account of what v0.3 adds (Sections 8-9 as
  described). If v0.3 contains resolutions beyond what the synthesis
  restates, I have not seen them -- push it or upload it before Opus builds.

## 1. Verdict in one paragraph

The synthesis is substantially correct and better than either source
manifest; I endorse it going to Opus after the items below are resolved. The
F2 correction to my own claim is RIGHT -- I re-verified it against the raw
bytes and the error was mine (Section 3). The date-resolution ruling is the
right model but is not yet implementable as written (Section 4). Section 5's
mean-elements claims all verify at HEAD, and I can strengthen the
moons-excluded reasoning (Section 5). The one thing I push back on hard: the
adopted module layout silently reverses a documented, settled,
three-model-convergence design decision -- feature rendering moved from JS
to Python without the divergence ever appearing in Section 1's table
(Section 2). I think the reversal may actually be the better design under
B-prime, but it must be ruled, not slipped.

## 2. MAJOR FLAG -- the feature-rendering reversal is real, silent, and absent from the resolution table

**The settled record:** master plan v11, Section 3a, schema decisions
(v0.3, three-model convergence, July 7): "Feature rendering: always JS in
interactive layer (both A and B-prime). Python assembler handles orbits
only. Feature configs in separate feature_configs.json." [verified: exact
wording in the uploaded master plan]

**My manifest** followed that record: Python orbits, JS feature renderers
reading feature_configs.json, house conventions translated to JS.

**GPT's manifest** reverses it: `render_features.py` inside the assembler,
"each feature renderer shall return zero or more Plotly traces" (S9), shell
and belt dispatch as Python assembler stages.

**The synthesis** adopted GPT's module layout including `render_features.py
# Shell/belt dispatch` -- i.e., adopted the reversal -- while Section 1's
resolution table does not contain a feature-rendering row at all. The one
place the two manifests contradicted a SETTLED upstream decision is the one
divergence that got flattened out of the record. It also leaves the
synthesis internally inconsistent: F1's fix is still framed around deriving
`feature_configs.json` (a JS-facing sidecar whose entire purpose is the
now-abandoned JS renderer path), and artifact 2's text says features are
"data-driven from objects_config.json," which is the Python-consumer
framing. The two halves belong to different architectures.

**On the merits, I am probably FOR the reversal.** The JS-renderer decision
was made when architecture A (no Python plotly in the browser) was still
live in the calculus. Under B-prime, the assembler builds the complete
figure in Python -- and a JS feature layer alongside it means the house
conventions (single info marker, legendgroups, km+AU hover) get a second
implementation in a second language, which is precisely the
parallel-pipeline drift class the B-prime decision was made to kill. GPT's
instinct here is sound, and the synthesis's adoption is defensible.

**But it must be an explicit ruling, routed to Tony,** because it reverses a
documented three-model convergence -- otherwise the master plan says JS
while the built system does Python, and the project's documented design and
its shipped code diverge at the exact layer the protocol exists to protect.
If ratified, three consequences need one pass each:

1. Master plan Section 3a gets a reconciliation note (the v0.4-style
   pattern already used there for the subtraction retirement).
2. F1's fix is retargeted: feature params still move into
   `objects_config.json` (that half survives either architecture), but the
   served consumer becomes per-object feature params in `coverage_index.json`
   for the Python renderer. `feature_configs.json`'s fate needs a one-line
   ruling: keep emitting it for the static-gallery pre-bake context, or
   retire it explicitly. Do not leave it emitted-but-consumerless.
3. The JS layer shrinks to harvest + bootstrap + Plotly.newPlot -- worth
   saying out loud, since it simplifies B4 considerably.

If Tony instead upholds the settled JS decision, the synthesis's module
layout must drop `render_features.py` and my manifest's Section 5 JS
framing comes back. Either way: rule it, record it.

## 3. F2 correction -- confirmed, accepted, and the method lesson is mine to own

Direct check this pass: `grep -c "event_link" data/objects_config.json`
returns **0**. No object carries the field, Halley included (key sets
enumerated per object to be sure). [verified @e864fd42]

The synthesis's correction is exactly right, and fair -- it neither
undersells nor oversells: the fix is genuinely two-step (add the field to
the config schema, wire the builder pass-through) plus the Layer-1 ride-along
all three documents agree on.

The error's origin is worth recording as a field note, because it is a
verification-method failure of the fetched-not-recalled class: my first-pass
check printed `o.get('event_link')` per object, which renders `None`
identically for a MISSING key and a present-but-null key. The tool I chose
could not distinguish the two states, and I read its output as confirming
the stronger one. The fix is mechanical: when the claim is "field exists,"
grep the raw bytes or enumerate key sets -- never `.get()`. Same lesson
shape as "compile-clean does not mean edited": the check passed while
testing a weaker proposition than the one I asserted. Recommend this lands
in the ledger alongside the build item (candidate for the
provenance-discipline or safe-file-editing field notes).

## 4. Date-resolution ruling -- right model, but the bound is not yet served data

The ruling (Kepler propagation from `M0_deg`/`epoch_jd`; GPT's nearest-date
model retired) is correct, and the retirement reasoning is exactly right:
there is nothing to select from except one elements snapshot for everything
but Voyager. [verified @e864fd42: moons/planets/comets all `positions:
null`] GPT should concede this one -- the nearest-date stage was written
against an imagined schema, not the served one.

To the question directed at me -- does "bounded to the freeze window"
adequately address what my manifest left implicit? **Partially. The
direction is right; the bound is not implementable as written.** The served
schema carries NO validity window for analytic objects: `served_window` is
`null` at HEAD, per-object blocks have no date-range field, and
`freeze_after_days`/`backfill_days` are builder-config concepts that never
reach the served index. [verified @e864fd42] "Reject if the requested epoch
is genuinely out of range" has no served range to test against, and the
assembler must not hardcode the builder's config (unit-is-data spirit: the
bound must arrive as data).

**Minimal fix, one small builder change:** populate the existing
`served_window` field (it is already in the schema, currently null with a
"null = full raw window" comment) as `{start_jd, end_jd}` from the
builder's own backfill/freeze parameters, and let the assembler enforce it
globally. Per-object `epoch_window` is the finer shape if moons want a
tighter bound (below), but global-plus-Mode-5 is a defensible Phase 2 floor.
Route the shape choice to Tony/Opus; the invariant I would hold firm on is
only that THE BOUND IS A SERVED FIELD.

**One honesty item the ruling should carry (Show the Envelope):** for
moons, phase accuracy degrades fastest -- short periods plus real
perturbations mean a position propagated weeks from `epoch_jd` can be
visibly off-phase even when the orbit shape is fine. Nightly rebuilds keep
`epoch_jd` fresh, which contains the problem, but the hover for any
propagated marker should say so: "position computed from osculating
elements at epoch [date]." Silence reads as precision the model does not
have. Cheap, one hover line, and it aligns with GPT's S10 honesty items
(comet hover identifying Tp-anchored analytic geometry -- which the
synthesis should carry explicitly, see Section 6).

**One free invariant the synthesis should keep by name:** for epoch=today
scenes, the engine's propagated marker must match the served `as_of_today`
point within tolerance. That cross-check data ships fresh every night, it
exercises the entire propagation path, and it catches Kepler-solver bugs
with zero additional infrastructure. My manifest had it explicitly; the
synthesis generalized it into "numeric position samples" -- name it.

## 5. Mean elements (new scope) -- all claims verify; the exclusion is even stronger than stated

Verified at orrery HEAD `4c4dc480`:

- The mechanism is exactly as described: unconditional name-keyed
  `ORIGINAL_planetary_params.get(obj_name, {})` lookups in
  `idealized_orbits.py` (lines 5428, 5677, 5743, 6136), importing
  `planetary_params` from `orbital_elements.py`. Curated list, no computed
  threshold. [verified @4c4dc480]
- Halley is a live entry (line 418, with the 90000030 record comment);
  Ikeya-Seki is a live entry (line 576, C/1965 S1-A). [verified @4c4dc480]
- The satellite staleness pattern is real and matches: Moon "Revised
  7-31-2013"; Mimas and Iapetus revised 1-26-2022; Charon "revised 4/3/2024
  post-New Horizons"; Io and Titan carry no revision date. [verified
  @4c4dc480]
- Voyager 1 in `spacecraft_encounters.py` is a commented-out template
  (line 340), confirming artifact 5's scope note. [verified @4c4dc480]

**The moons-excluded ruling has a supporting physics argument the synthesis
does not state, and it makes the exclusion firmer:** satellite "mean
elements" without secular rates are epoch-bound in a way planetary J2000
values are not. Close-in moons have fast nodal and apsidal precession driven
by planetary oblateness (order months-to-years for inner moons; the Moon's
node regresses with an 18.6-year period). A static mean ellipse for a
satellite therefore goes stale on human timescales even when perfectly
transcribed -- the inconsistent-sourcing problem the synthesis cites is
compounded by the data class being intrinsically perishable. Planets do not
have this problem at visual precision. Moons-osculating-only is not just a
data-hygiene call; it is the physically correct one. (Supporting argument,
standard celestial mechanics, not load-bearing -- the synthesis's own
reasoning already suffices.)

**One mechanism under-specification to close before build:** the synthesis
says the served schema gains an optional `mean` block "populated ... from
`orbital_elements.py`" -- but the builder is a standalone gallery tool with
no orrery imports by design. The clean path, consistent with F1's own
pattern: curated mean elements go into `objects_config.json` (or a curated
sibling, same blast-radius rule), each block carrying a source citation
(provenance-discipline: these are transcribed constants -- source-then-cite),
and the builder passes them through verbatim. Recommend stating this
explicitly so Opus does not resolve it by importing orrery code into the
builder.

**Scoping honesty on artifact 4: agreed as written.** Halley is currently
in the long quiet arc between the 1986 and 2061 apparitions; the
mean-vs-osculating divergence this feature exists to teach will not show
dramatically at today's epoch. Build the mechanism, do not claim the demo.

## 6. Section 1 table fairness, and what got dropped

**Fairness to my manifest: yes, with one omission.** Every row that names
me characterizes my position accurately -- including rows resolved against
me (AssemblyContext, view_id, module layout), all three of which I accept;
GPT's context-freeze and closed view enum are genuinely better than what I
had, and the finer module split maps cleanly onto the test layers. The
omission is the missing feature-rendering row (Section 2) -- the table is
fair on everything it contains and silent on the one divergence that
reverses settled design.

One small correction in GPT's favor that I checked rather than assumed:
GPT's "deterministic orthographic camera" is not an invention -- it IS the
desktop convention. `get_default_camera()` returns an orthographic
top-down camera. [verified @4c4dc480] The synthesis carries camera policy
correctly by adopting GPT's presentation layer.

**Dropped or weakened from my manifest -- items I want back or explicitly
ruled out (per the prompt's question 5):**

1. **Disposition of `axes.*`, `sampling.*`, and `window` went unstated.**
   My manifest classified every vocabulary field into
   implemented / known-unimplemented-with-structured-error / unknown-warn.
   The synthesis kept the three-class rule but its spec and its
   known-unimplemented list simply omit these three field families --
   leaving them in an undefined fourth state the rule was designed to
   prevent. Recommendation: EITHER implement `axes.scale_mode` /
   `manual_half_range_au` / `dtick_au` by plumbing them into the single
   axis-policy function GPT's S11 already requires (cheap, closes the
   assembler-side slice of L-040, and the ledger note I proposed still
   applies) OR declare them known-unimplemented. Same explicit choice for
   `sampling.orbital_points` (internal default 360 is fine; then say the
   field is unimplemented) and `window` (full-arc-only Phase 2 is fine;
   then say so -- noting it as a deliberate deviation from the vocabulary,
   where `window.end` is nominally required). Unstated is the only wrong
   answer.
2. **The L-086 attribution gate vanished.** Any publicly reachable
   interactive page needs the inline "Data: JPL/NASA" credit minimum --
   master plan secondary dependency, applied to `interactive.html` at Phase
   0. It applies to the new page identically and belongs in the ship gate
   next to F4. One line.
3. **The as-of-today cross-check invariant** -- generalized away; name it
   (Section 4 above).
4. **Normalized-spec storage.** My OQ-1 ruling had the assembler return its
   normalized spec so golden artifacts are self-describing. AssemblyContext
   carries the resolved spec, which mostly covers it -- but make explicit
   that `scene_spec_hash` in the fingerprint is computed over the
   NORMALIZED spec, or determinism breaks on cosmetically different inputs.

**Dropped or weakened from GPT's manifest that I would restore (reviewing
their side too, since a synthesis losing THEIR good ideas is the same
failure mode):** S10's hover-honesty items -- comet hover identifying the
curve as Tp-anchored analytic geometry, and Voyager hover distinguishing
the live marker from the served historical arc. The synthesis kept the
event-link leave-scene line but dropped these two. They are the hover-layer
form of Show the Envelope and cost one line each. Fold S10 in by reference.

## 7. Summary of asks (in priority order)

1. Feature-rendering reversal: surface it, route it to Tony, and if
   ratified, add the master plan Section 3a reconciliation note and retarget
   F1's consumer + rule feature_configs.json's fate. (Section 2)
2. Date bound: make it a served field (populate `served_window` at
   minimum); keep the propagated-marker hover honesty line; name the
   as_of_today cross-check invariant. (Section 4)
3. Mean-elements sourcing: config-as-source with citations, builder
   pass-through -- never orrery imports in the builder. (Section 5)
4. State dispositions for `axes.*` / `sampling.*` / `window`; restore the
   L-086 ship-gate line; hash the normalized spec; restore GPT's two hover
   honesty items. (Section 6)
5. Record the F2 verification-method lesson in the ledger. (Section 3)
6. Push or upload handoff v0.3 before Opus builds. (Section 0)

Nothing here re-litigates the resolutions that went against my manifest --
those were correctly decided. With items 1-3 resolved and 4-6 penciled in,
this synthesis is the right document to hand to Opus.

---
Review written July 14, 2026 by Anthropic's Claude Fable 5, Mode 7 collegial
relay for Tony Quintanilla. Bases: orrery @4c4dc480 (moved from the prompt's
@8bce8354 by one documentation-only commit, reconciled), gallery @e864fd42
(unchanged). Every code-level claim in this review fetched at those SHAs
this session; my own corrected claim re-verified against raw bytes, not
re-asserted.
