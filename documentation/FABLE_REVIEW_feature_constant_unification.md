# FABLE REVIEW -- Feature/Constant Unification and Cross-Repo Provenance

**Built on `ee0da47c483cda02ac035d48ce99bc855a56e03c`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Gallery repo pinned separately at
`61a78c00668573dbff111ec9f10a96b1cd2fdc35`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).**

**Type:** DESIGN REVIEW. Zero code delivered.
**Prepared:** August 6, 2026 by Claude Fable 5, responding to
`PREDESIGN_HANDOFF_feature_constant_unification.md` (anchored at orrery
`24452442` / gallery `e7e8c5e`).
**Reviewer verification:** both HEADs confirmed live via `git ls-remote`.
Deltas from the handoff anchors traced: orrery moved by two commits (the
handoff itself, ledger items L-184/L-185, and a report-only scanner change
-- per-domain console rollup, no scoring behavior change); gallery moved
by one nightly data build plus an atlas regen. Neither delta changes the
substance under review. The gallery delta independently confirms the
handoff's central claim: the 2026-08-06 nightly touched vectors, elements,
and positions and did not touch `objects_config.json` or
`feature_configs.json`.

Skill gate: provenance-discipline 1.7, orrery-coding-conventions 1.3,
ledger-and-session-records 1.5, gallery-cache-builder 1.2,
gallery-assembler 1.1 -- all matching the v3.34 manifest, installed
copies matching repo copies.

---

## Verdict in one paragraph

The architecture is sound and I endorse it: one store, three zones per
entry, provenance as data, derivation instead of annotation, and an
exporter that aborts on a missing source. Every piece extends a pattern
that already exists in the codebase rather than inventing a new one. On
the fork Tony handed me: **I recommend pull, in a specific form -- the
builder fetches the orrery's generated artifact nightly, validates it,
and commits it into the gallery repo alongside the position data it
already commits.** This form keeps everything push was defending
(reproducibility, offline fallback, self-containment where it actually
matters) while eliminating the hand-maintained copy Tony asked to kill.
The reasoning, and one reframe of the self-containment argument, is in
Open Question 1 below. I also found four things the handoff's evidence
chain missed; none changes the architecture, all belong in the build
scope or the ledger.

---

## Open Question 1 (PRIMARY) -- push or pull: PULL, vendored

### The reframe that dissolves most of the tension

The handoff frames pull's cost as trading away the assembler's
self-containment. I checked what that property actually protects, and
the boundary is not where the handoff draws it.

The protocol's Orrery/Assembler section protects the **assembler at
render time**: no live connection, reconstruct correctly, later, alone.
The assembler reads only the served cache. Pull does not touch this. The
network dependency pull adds lives in the **builder at build time** --
and the builder is already network-dependent (JPL Horizons, nightly) and
already commits fetched external data into the repo every night. I
verified this in the gallery delta itself: commit `d131e13` ("data:
nightly 2026-08-06") landed fetched vectors, elements, and positions as
repo content. Feature geometry riding the identical pattern is not a new
kind of dependency; it is the existing pattern applied to one more data
class.

The builder docstring's "No orrery imports" design decision survives
intact: no Python import, no Plotly drag-in. A validated JSON fetch is a
data transfer, which is what the builder already is. I recommend
updating the docstring wording from "COPIED WITH PROVENANCE ... and kept
in sync on change" (a promise with no test, as the handoff proved) to
"feature data pulled nightly as a generated, validated artifact,
orrery SHA recorded per build."

### The recommended mechanics

1. Orrery side: the exporter reads `constants_new.py`, emits
   `feature_configs.json` (or a renamed successor -- see the filename
   collision note below) with per-value `source` fields, the orrery HEAD
   SHA, and a content hash. Abort on any missing source. This artifact
   is committed in the ORRERY repo as part of Tony's normal
   sandbox-test-commit-push loop.
2. Gallery side, nightly: the builder does `git ls-remote` on the orrery
   repo, records the HEAD SHA, fetches the artifact by raw URL **at that
   SHA** (not at "main" blind), validates shape AND source-presence AND
   content hash, then writes it into the staging cache and commits it
   with the rest of the nightly output under the existing atomic-swap /
   quarantine semantics.
3. Failure mode: orrery unreachable or validation fails -> quarantine,
   keep serving the last committed copy, log loudly. Because the last
   good copy is committed, an offline build falls back to it with a
   visible "features stale as of orrery <SHA>" warning.

### Why this beats both plain variants

- Tony's requirement ("avoid duplication that may drift") is met: the
  gallery copy still exists on disk, but it is **generated, validated,
  and refreshed nightly** -- it is a cache entry, not an authored file.
  Drift is bounded at one day and the recorded orrery SHA makes any lag
  visible, which is exactly the property the handoff showed a content
  hash alone cannot provide.
- Push's one surviving advantage -- last month's cache rebuildable from
  last month's committed artifact -- is retained for free, because every
  nightly commit IS a snapshot. The pin-vs-HEAD tension the handoff
  flagged resolves: track HEAD at fetch time, pin by record in git
  history.
- The staleness argument the handoff worked through stands: every push
  variant that detects staleness makes pull's network call anyway. Given
  that, carrying a second HAND-MAINTAINED copy buys nothing. Carrying a
  second GENERATED copy buys reproducibility and offline fallback, which
  is why the vendored form is the right pull.

### Direct answers to the questions asked of me

- Is self-containment load-bearing beyond the stated reasons? For the
  BUILDER, no -- offline builds, GitHub Actions, future contributors,
  and disaster recovery are all served better by the committed-snapshot
  form than by either plain variant, because the fallback copy is in git
  with its provenance recorded. For the ASSEMBLER, yes, fully -- and
  pull as specified never touches it.
- One consequence neither plain variant surfaces: **the two files named
  `feature_configs.json` become three** unless the collision is resolved
  in this build. The orrery exporter writes one (renderer names today,
  full values tomorrow), the gallery builder writes another. Under
  vendored pull the orrery artifact should either replace
  `objects_config.json`'s features block outright or take a distinct
  name (`feature_geometry.json` or similar). Recommend renaming as part
  of the build; same-name-different-content across repos is a standing
  trap for every future session and for the scanner.

---

## Open Question 2 -- have we found all the stores? No; four more surfaces

**(a) The store itself is not a pure store, and the boundary rule as
written would not survive contact with it.** `constants_new.py` at
`ee0da47c` also carries `color_map()` (presentation for every body),
`stellar_class_labels` (GUI layout), and `spectral_subclass_temps` (a
numeric physical claim -- spectral class temperature ranges -- with no
citation of any kind). The proposed rule "cited physical values live in
the store, and the store carries source as data" is currently enforced
outward while the store holds uncited physical values inward.
`spectral_subclass_temps` belongs in the citation-form migration or gets
an explicit presentation carve-out ruling; `color_map` and the label
dicts should be tagged presentation under the same three-zone convention
the feature entries get. The architecture already has the vocabulary for
this; apply it at home first.

**(b) A live proof that the store needs load-time validation.**
`KNOWN_ORBITAL_PERIODS` contains the key `'Phobos'` **twice** (once in
the planets block at 0.319, once in the Mars satellites block at 0.319).
Same value today, so harmless -- but Python silently keeps the last
duplicate, which is precisely the silent-drift class this whole design
exists to kill: two authors, one survives, no warning. Recommend the
build include a small load-time validation pass over the store
(duplicate keys, source presence on physics fields, unit sanity). The
exporter's abort-on-missing-source is generation-time; this is the
matching import-time check, and the duplicate key proves it earns its
place.

**(c) The module-level `*_info` tooltip strings are a fifth restatement
surface the handoff's count missed.** The handoff counted description
fields inside the params dicts. The four shell modules ALSO carry
module-level `*_info` strings imported by `palomas_orrery.py` for the Tk
GUI tooltips -- a different consumer than hover text -- and several
restate stored numbers: Uranus's atmosphere info strings restate
25,559 km four times and do arithmetic in prose ("25,559 + 50 =
25,609 ... fraction ~1.002"); Neptune's Galle ring info restates
"41,900-42,900 km." If interpolation covers the dict descriptions but
not these, the `*_info` strings become the surviving duplicate statement
and the next consistency pass harmonizes toward whichever copy was
missed -- the exact L-182 failure shape. They should be in the
derivation scope or explicitly deferred with a ledger item.

**(d) `info_dictionary.py`: do NOT extend the migration there now.**
The interpolation rule, applied literally, would pull every numeric
claim in 2,248 lines of prose into scope -- a scope explosion that
contradicts settled ruling 3 (one pass, bounded to the store). The
principled boundary: where a number in INFO prose duplicates a stored
constant, interpolate it (it is a two-copy pair at L-182 risk); where a
number exists only in prose, it stays prose with its `# Source:` comment
-- that is provenance on narrative, which the handoff already names as a
different job. The real preparatory task is an enumeration: which
info_dictionary numbers duplicate store constants. That is a one-off
script or scanner extension, and a good ledger item; it is not part of
this build.

---

## Open Question 3 -- consumer breakage: verified low, with two gates

**The 37 entries have zero external consumers of the numbers.** All four
`*_params` dicts are function-local (`ring_params = {` is indented
inside `create_*_ring_system` in every module; verified by grep at
`ee0da47c`). Nothing outside the defining functions can read them.
External references to the shell modules are: feature-name strings
(checkbox `var_suffix` entries in `celestial_objects.py`, Tk IntVars in
`palomas_orrery.py`), the `create_*` functions themselves (dispatched
via `planet_visualization.py` / `orrery_rendering.py`), and the `*_info`
strings. Moving the numbers into `constants_new.py` and referencing them
inside the create functions -- preserving the dict shape the loop
consumes -- breaks nothing outside the four modules.

**Parallel pipelines are covered by construction, gated by the smoke
test.** `plot_objects` and `animate_objects` both reach rings through
the same `create_*` functions; a store-reference change inside those
functions reaches both pipelines through the one shared path. The
live-dispatch smoke test in agentic-pre-test remains the proof at build
time -- covered-by-construction is a code-reading claim, and the render
wins.

**Scanner SOURCE_PATTERNS extension: sequence it as its own step.** The
family-wide-ripple warning is real (the star_notes.py precedent).
Recommend: land the pattern extension alone, run the full scan, diff the
finding set against the prior audit, and attribute any newly-exposed
pre-existing findings to the scanner change BEFORE the citation
migration lands. Otherwise the migration's diff and the scanner's diff
interleave and neither is auditable.

**Prose that resists mechanical interpolation exists; I found three
concrete cases to use as the test set.** (1) Jupiter main ring:
description says "about 30-300 km" thickness while `thickness_km` stores
30 -- a range in prose against a scalar in data. (2) Neptune Galle:
"41,900-42,900 km" where the stored pair is inner/outer radius, so the
prose range is derivable but not by naive field substitution.
(3) Uranus atmosphere info: arithmetic performed in prose. These need a
small schema answer -- an optional range field, or a derived value
computed in code, or a documented per-case carve-out -- not a bigger
pass. This is exactly Tony's acceptance test in miniature: if the schema
absorbs these three cleanly, the architecture is right; if many more
surface, that is the signal.

**Sequencing note on L-179/L-180.** Both are drift inside the store
today. The handoff's own "presence is not truth" warning applies:
migrating and deriving BEFORE those values are settled transports a
known-inconsistent value into the gallery, the served cache, and the
hover text, now looking authoritative. Settle L-179 and L-180 (Tony
decisions) before, or as the first step of, the migration.

---

## Open Question 4 -- assembler source discipline: enumeration incomplete; keep constants in code

**The handoff's enumeration missed four sites, verified at `61a78c0`:**

- `tools/gallery_studio.py` lines 1035, 1051, 5520: three **bare
  literals** `149597870.7` inline in expressions -- not even assigned to
  a named constant. Worse than every enumerated case; violates the
  assign-don't-hardcode house pattern on top of being uncited.
- `tools/gallery_cache_builder.py` lines 127, 135: `2440587.5` used
  inline twice (the docstring at 123 explains it; the citation shape is
  absent).
- `tools/test_gallery_cache_builder_offline.py` line 34:
  `_MOCK_K_GAUSS = 0.01720209895` -- carries an in-repo mirror comment
  ("mirrors render_orbits.py K_GAUSS") but no physical source. A mirror
  note is not a citation; if render_orbits.py's citation lands, the mock
  should point at it explicitly.

**On whether the calculus changes: keep the arithmetic constants in
code; do not put them in the pulled artifact.** The temptation under
vendored pull is to let AU_KM and K_GAUSS ride along as data. I advise
against it. These are exact-by-definition or conventional values; making
the assembler's arithmetic depend on a cache read introduces a new
failure mode (cache unreadable means no math at all) in exchange for
zero drift benefit -- they cannot drift. The line-89 pattern is the
right remedy, applied by hand, one bounded pass over roughly eight
sites: name the bare literals, add the cross-repo citation naming file,
line, and SHA. One refinement: once the vendored artifact exists and
records the orrery SHA per build, new citations can reference "orrery
SHA per feature artifact" rather than a hand-typed SHA that goes stale.

Tony's ruling that the discipline applies regardless of stability is
correctly framed in the handoff and I have nothing to subtract from it:
"is this a claim" is the test, and a reader cannot distinguish a
deliberate skip from an unchecked one.

**Scanner coverage:** yes -- running `provenance_scanner.py` and
`module_atlas.py` in the gallery repo would firm this enumeration up
beyond my grep sweep (the scanner's unit vocabulary is broader than the
three magic numbers I searched for). Useful, not blocking. Note the
scanner's `.py`-only filter means the vendored artifact JSON stays
invisible to it either way; the artifact's own validation gate (source
presence, hash) is the compensating control, which partly answers the
handoff's closing question about provenance extending into config JSON:
extend it via the generator's abort and the builder's validation, not by
teaching the scanner JSON.

---

## Findings summary and suggested dispositions

1. Vendored pull recommended (Q1) -- Tony (decide); feeds L-181 build
   design and unblocks L-184's build-path definition.
2. `feature_configs.json` name collision -- resolve in the build; rename
   the orrery artifact.
3. Store-internal hygiene: `spectral_subclass_temps` uncited,
   `color_map`/labels untagged, `'Phobos'` duplicate key -- fold into
   the L-181 build scope (validation pass + three-zone treatment applied
   to the store itself).
4. `*_info` tooltip strings as fifth restatement surface -- include in
   derivation scope or open a ledger item.
5. info_dictionary interpolation -- defer; open a ledger item for the
   numeric-overlap enumeration.
6. Scanner SOURCE_PATTERNS extension sequenced as its own
   land-scan-diff step before migration.
7. L-179/L-180 settled before migration transports their values.
8. Gallery uncited-constant pass (~8 sites incl. the three
   gallery_studio bare literals) -- bounded hand pass, line-89 pattern;
   candidate merge into L-185.
9. Saturn schema note: the gallery copy drops `thickness_km` for Saturn
   while keeping it for Jupiter -- an artifact of hand-seeding; the
   generated artifact should emit a uniform schema.

*Review prepared August 6, 2026 with Anthropic's Claude Fable 5, built
on `ee0da47c483cda02ac035d48ce99bc855a56e03c` at
https://github.com/tonylquintanilla/palomas_orrery and
`61a78c00668573dbff111ec9f10a96b1cd2fdc35` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
