# PREDESIGN HANDOFF -- Feature/Constant Unification and Cross-Repo Provenance

**Built on `24452442aaa64393066cac9d9b5885a763c0a76a`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Gallery repo pinned separately at
`e7e8c5efbe8350e9cca900bafed7bcc8b44529e3`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).**

Verify both HEADs before reviewing. If either has moved, trace the delta first.

**Type:** PREDESIGN / DESIGN REVIEW REQUEST. Zero code delivered. Nothing
here has been built.
**Prepared:** August 6, 2026 by Claude Opus 5 (orchestrating instance),
Tony Quintanilla integrator.
**Reviewer:** Claude Fable 5.
**Companion:** `documentation/HANDOFF_next_session_masterplan_v16.md`
(the session this grew out of); `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`
at v16.

---

## Who you are writing for

Tony Quintanilla, PE, is a retired civil and environmental engineer, an
artist, and an anthropologist. He is **not a professional programmer and
not a formally trained astronomer.** He builds Paloma's Orrery through
conversational AI collaboration and holds sole commit authority and final
judgment on every integration decision.

The codebase's structure, docstrings, and engineering discipline are the
product of iterative collaboration with Claude, not something Tony wrote
unassisted. Reading the code cold, you will reasonably infer a skilled
programmer authored it. Do not let code quality substitute for this
framing.

What Tony does own and drive personally is the workflow: the protocol,
master planning, design handoffs, build oversight, as-built verification,
the ledger, and the inter-model relay you are part of. Mechanism-level
novice status is not the same as passive.

Practical consequences for anything you recommend:

- He runs Python by opening a file in VS Code and clicking Run, and works
  through GitHub Desktop. As of protocol v3.34 that is a **preference
  where practical, not a prohibition** -- a terminal step is a fallback,
  not forbidden. The standing obligation: do not hand over an operation
  outside his known working set without explaining what it does and what
  could go wrong.
- Unpack technical jargon on first use. Do not assume a programmer's or
  an astronomer's fluency lands.
- Deliverables are runnable transactional patch scripts, not diffs or
  complete-file rewrites.

---

## The question, in one paragraph

Feature geometry -- planetary ring radii, radiation belt extents,
atmosphere shell bounds -- currently lives inline inside four Plotly
rendering modules in the orrery repo, and a hand-seeded copy of some of
those values lives in a frozen JSON file in the gallery repo, where it
feeds the served cache that the interactive gallery actually renders.
There is no generator, no sync test, and no per-value provenance on the
gallery side. We want to unify the store, carry provenance as data rather
than as comments, derive display text from the stored values, and
automate the cross-repo handoff. We want your review of that architecture
before any of it is built, and your ruling recommendation on one open
fork.

---

## Evidence -- the chain of custody, traced

Every claim in this section was verified against the two repos at the
anchors above. Where something is inferred rather than measured, it says
so.

### Where the numbers actually live

The ring radii exist in exactly four Python files in the orrery repo:
`jupiter_`, `saturn_`, `uranus_`, `neptune_visualization_shells.py`.
`grep -rl inner_radius_km --include=*.py` returns those four and nothing
else. Scope: 37 entries total (Jupiter 5, Saturn 8, Uranus 12,
Neptune 12), one `*_params` dict per module.

They are **not** in `shell_configs.py`. That file has a `ring_system`
key but no numeric radii.

### The orrery has an exporter, and it does not export the values

`export_orbit_cache.py` contains `write_feature_configs()`, which does:

```python
from shell_configs import SHELL_CONFIGS
...
configs[name] = {'renderer': cfg.get('renderer', cfg.get('type', 'unknown'))}
```

Renderer name only. No radii, no thicknesses. The module header states
the obstacle: importing the shell configs pulls Plotly in with them. The
physics lives inside GUI rendering code, so the values cannot be read
without dragging the whole drawing stack along. That is almost certainly
why only the names made it across.

### Nothing writes the gallery's config

`data/objects_config.json` in the gallery repo carries full numeric
feature values -- Jupiter's four rings, Saturn's seven, Earth's
atmosphere shells and Van Allen belts. Grepping both repos, every
reference to that file is a **reader**: the cache builder, the assembler's
catalog, two tests. There is no generator anywhere.

`git log --follow` on that file returns **one commit**. It was seeded once
and has never been edited.

### Its self-description overstates its own provenance

The file's `_comment` says its fields were *"carried from
`export_orbit_cache.py` TEST_OBJECTS @ orrery `4e2629c`."* But
`TEST_OBJECTS` carries feature **names** only --
`["magnetosphere", "ring_system"]` -- never values. The numeric values
have no traced path from any orrery source.

The file has a repo-level `attribution` key (`"Data: JPL/NASA Horizons"`)
and **no per-value source fields at all**.

### Two different files are named feature_configs.json

The orrery exporter writes one (renderer names). The gallery builder
writes another (full values, assembled from `objects_config.json`). Same
filename, different repos, different content, no relationship.

### The current state of the copies

Jupiter's ring radii and Saturn's A/B/F ring radii **currently agree**
between the orrery modules and the gallery JSON. There is no drift today.

There is also no mechanism preventing it. The builder pins a provenance
base at orrery `4e2629c`; current orrery HEAD is `24452442`, and the pin
has not been re-cut. "Kept in sync on change" is a promise with no test
behind it.

Batch 2 of the L-156 provenance cross-check is scheduled to move Saturn's
values. When it does, nothing will carry the correction across.

### The nightly build does not refresh feature geometry, and cannot

This is the finding that makes the staleness risk concrete rather than
theoretical, and it is easy to miss because the pipeline looks healthy.

The nightly builder handles two classes of data differently:

- **Positions** are fetched fresh from JPL Horizons every night, per
  object, with an explicit canonical center. Genuinely current.
- **Feature geometry** is read from `objects_config.json` and passed
  straight through. The assembly step is literally
  `features_out[slug] = feats`, copied verbatim from the config object.
  `_validate_feature_shapes()` checks the SHAPE of the dict, never the
  values. Grepping the builder for any Horizons call touching features,
  rings, belts, or shells returns nothing.

Run the builder every night for a year and not one ring radius changes.

Horizons could not supply these values in any case. A ring's outer radius
is not an ephemeris quantity -- it is a physical extent measured from
spacecraft data and published in literature, which is exactly the class
of value the L-156 provenance cross-check exists to verify.

**Why this makes the problem worse rather than better.** A nightly
pipeline that succeeds is actively misleading here. The build runs, the
atomic swap completes, timestamps update, the cache is new. Every signal
says fresh. One class of data inside that fresh cache is frozen at a seed
from months earlier, and the success signal offers no way to tell. A
correctly-functioning pipeline will never surface this on its own, which
is why the staleness check has to compare against something outside the
artifact.

### The failure class this repeats

L-182 (closed August 5, 2026): a cross-check derived the correct Mars
Hill sphere value, but its patch reached only the shell module;
`shell_configs.py` never received it. A later consistency pass then
harmonized the module **toward the uncorrected copy**, erasing the fix.
Mode 5 caught it. The general form recorded in the master plan at v16: a
correction that reaches one copy of a two-copy pair is worse than no
correction, because the next consistency pass harmonizes toward the copy
that was missed.

The gallery config is the same shape, one repo boundary further out.

### A fourth duplication, inside the shell modules

Jupiter's main ring entry, verbatim:

```python
'inner_radius_km': 122500,
'outer_radius_km': 129000,
'description': (
    "It extends from about 122,500 km to 129,000 km "
    "from Jupiter's center.<br>"
)
```

The number is data and prose in the same dict. Three such restatements in
Jupiter alone. (The `<br>` is a separate known bug -- the Tk GUI renders
it as literal markup; `\n` is the canonical form.)

### The store split is already arbitrary

`constants_new.py` already holds feature geometry:

```
CHROMOSPHERE_RADII = 1.1
INNER_CORONA_RADII = 3
OUTER_CORONA_RADII = 50
ROCHE_LIMIT_RADII = 3.45
ALFVEN_SURFACE_RADII = 18.8
TERMINATION_SHOCK_AU = 94
HELIOPAUSE_RADII = 26148
```

Solar shell geometry went into the constants store; planetary ring
geometry stayed inline in the rendering modules. There is no principle
behind which went where. It also already handles nested dicts with
per-entry citations (`CENTER_BODY_RADII`, `KNOWN_ORBITAL_PERIODS`).

### Unification alone does not fix drift, and we can prove it

Two open ledger items are drift **inside `constants_new.py` today**:

- **L-179** -- `GRAVITATIONAL_INFLUENCE_AU = 150000` while citations and
  display text say 126,000 AU.
- **L-180** -- the solar chromosphere carrying three inconsistent extents
  across modules.

Both live in the unified store already. So moving rings there inherits
the same failure mode unless display text is **derived** from the stored
value rather than typed beside it.

---

## What Tony has already ruled -- do not relitigate

These are settled. Review them for consequences you can see and we
cannot, but do not re-open them as questions.

1. **Architecture before Batch 2.** A deliberate reversal of the earlier
   "clear all provenance batches before Artifact 2" instruction.
2. **No parallel pipeline.** Feature values join `constants_new.py`. They
   do not get a sibling module. Tony caught this directly when an earlier
   draft proposed a separate feature layer.
3. **One pass for the citation-form migration**, bounded to the constants
   store (36 `# Source:` comments in `constants_new.py`, plus whatever
   migrates in).
4. **Description interpolation ships in this build**, not as a follow-on.
   Tony's reasoning, and it doubles as an acceptance test: *"this should
   be minor if the architecture is right."* If the Mode 5 verification
   surface turns out large, that is evidence the architecture is wrong,
   not evidence the scope was too big.
5. **L-181 is reframed** from "build a new single-source-of-truth constant
   layer" to "complete the existing one."

---

## The proposed architecture

One pipeline, one convention, content tagged rather than separated.

### 1. One store

Ring, belt, and shell geometry move into `constants_new.py` alongside the
solar shell values already there. The four `*_visualization_shells.py`
modules stop holding numbers and reference them instead.

### 2. Three zones per entry

Drawn from the existing structure, which already makes this distinction
in a comment. Jupiter's `ring_params` carries a block citation over the
geometry and then an explicit carve-out:

> *Colors below are selected by the developer for visual distinction, not
> verified against the cited source... they are not part of what this
> citation sources (Tony's call, July 16, 2026; L-124).*

That ruling is currently prose no tool can read. In a data layer it
becomes enforceable:

- **Physics** -- `inner_radius_km`, `outer_radius_km`, `thickness_km`,
  each carrying a `source` field. This is what the scanner reads, what
  the cross-check verifies, and what hover text quotes.
- **Presentation** -- color, opacity, display name. Explicitly marked
  uncited.
- **Description** -- prose with the numeric spans interpolated from the
  physics fields, so a number exists in exactly one place.

### 3. Provenance as data, not comments

A `# Source:` comment cannot be read at runtime; comments do not survive
parsing. Tony wants hover text to quote its verified source alongside the
value, so his Mode 5 visual verification can audit provenance at the
render instead of by tracing files. That requires the source to be a data
field.

The scanner's own docstring already lists this as a deferred fix, item 6:

> *Dict values with inline `'source'` keys not recognized as citations...
> Future fix: extend SOURCE_PATTERNS to recognize `'source': '...'`*

So this is a scoped change the scanner authors already anticipated, not a
novel invention.

The boundary that keeps it from becoming a second convention: **cited
physical values live in the store, and the store carries source as data.**
Nothing outside the store should hold cited physical values at all --
that is what L-181 is for. Comments elsewhere are provenance on things
that are not physical constants, which is a different job.

### 4. Derivation, not annotation

Every displayed number -- hover text, descriptions, and the illustrated
dimensions of L-176 -- is interpolated from the stored value at render
time. Example of the change in form:

```python
# before
"It extends from about 122,500 km to 129,000 km from Jupiter's center."

# after
"It extends from about {inner_radius_km:,} km to "
"{outer_radius_km:,} km from Jupiter's center."
```

A mistyped field name then fails loudly at render rather than silently
printing a stale number.

### 5. One export, automated

The exporter reads `constants_new.py` rather than four shell modules --
which is also what makes it possible at all, since the constants store
does not pull Plotly. It emits values **with their source strings
attached**, plus the orrery source SHA and a content hash.

The gallery's `objects_config.json` stops being an authored file and
becomes a derived one, carrying the orrery source SHA and a content hash.

**A caution on what a content hash actually buys, because an earlier
draft of this document overstated it.** A hash of the artifact recorded
alongside the artifact detects corruption and botched transfer. It does
NOT detect staleness: a forgotten regeneration leaves the file and its
fingerprint both old and perfectly consistent with each other, so the
gate passes and the build serves stale values. To detect staleness the
check must compare against something that MOVES when the orrery moves.
See Open Question 1.

Two hard requirements on the exporter itself:

- **Abort on a missing source.** The exporter must REFUSE to emit any
  physics field lacking a non-empty source string -- an abort at
  generation time, not a warning in a log. Fix the producer.
- **Presence is not truth.** This architecture transports provenance
  faithfully; it does not verify it. A wrong source in the store
  propagates into the gallery, the served cache, and the hover text, now
  looking authoritative in three more places than before. Only the
  competitive cross-check makes a source TRUE. This design makes sources
  present, consistent, and visible, which is a different guarantee.

---

## Open question 1 (PRIMARY) -- push or pull across the repo boundary?

**This is the fork Tony has explicitly handed to you for review.** He has
not ruled on it. Both cases stated as fairly as we can.

### Push

The orrery generates the artifact; Tony commits it into the gallery repo.

- Preserves the gallery repo's self-containment at build time. The cache
  builder's docstring states this as a design decision: *"No orrery
  imports; hard-won fetch specifics are COPIED WITH PROVENANCE from the
  orrery and kept in sync on change."*
- Aligns with the protocol's Orrery/Assembler separation, which treats
  the assembler's independence as load-bearing rather than incidental:
  the assembler exists to reconstruct correctly, later, alone, with no
  live connection.
- Cost: a human step between two repos. A fingerprint gate turns a
  corrupted or botched transfer into a loud failure, but does NOT catch a
  forgotten regeneration -- see the staleness argument below.

### Pull

The gallery builder fetches the orrery's generated artifact by raw URL,
pinned to a SHA, at build time.

- Zero duplication. One file, one repo, no copy to keep honest. This is
  the thing Tony actually asked for: *"avoid duplication that may drift."*
- The builder already requires network access (JPL Horizons), so the
  network dependency is not new in kind.
- SHA-pinning the fetch is the same anchor discipline the protocol
  already runs on.
- Cost: the gallery build now depends on the orrery repo being reachable
  and correct. A gallery build can fail for an orrery-side reason. It
  trades the self-containment that the assembler architecture was
  deliberately built to have.

**The staleness argument, which weakens the push case substantially.**
Work through the push variants that would genuinely detect an
out-of-date artifact:

- Record the orrery SHA in the artifact and compare it to orrery HEAD --
  requires reaching the orrery repo at build time.
- Have an orrery-side test regenerate and diff against the committed
  gallery copy -- requires reaching the gallery repo from the orrery, the
  same crossing in the opposite direction.
- Compare the source file's hash at orrery HEAD -- one raw fetch, which
  is close to what pull does anyway.

So every push variant that actually closes staleness ends up making the
same network call pull makes, while still carrying a second copy on disk.
At that point pull is simpler and strictly smaller.

The one property push still buys is reproducibility: last month's cache
can be rebuilt from last month's committed artifact. Pull with a
SHA-pinned fetch gives that too, but a pinned SHA is stale by
construction, while a pull tracking HEAD is not pinned. That tension does
not resolve cleanly in either direction and is a good target for your
review.

**What we want from you:** a recommendation with reasoning, and
specifically whether the self-containment property is load-bearing for
reasons beyond the ones stated -- offline builds, GitHub Actions, future
contributors, disaster recovery, or anything the two repos' actual
structure implies that we have not seen.

The orchestrating instance's initial lean was push with a fingerprint
gate. That lean was formed before the staleness analysis above, which the
instance then had to withdraw as overstated. Treat it as a discarded
first opinion, not a position to defend. Tony's own framing of the
requirement is "avoid duplication that may drift," which points at pull;
the protocol's treatment of the assembler's independence points at push.
That is the genuine tension.

---

## Open question 2 -- have we found all the stores?

`info_dictionary.py` carries 62 `# Source:` comments across 2,248 lines.
Its docstring says it was *"Split from constants_new.py to separate
narrative content (fact-checked) from numeric constants (source-cited)."*
So it is the prose store, deliberately, not a third numeric store.

But its prose contains numeric claims, and the derivation rule in section
4 says display text should interpolate rather than restate. Two things we
want checked across the codebase:

- Does the interpolation rule extend to `info_dictionary.py`'s INFO
  strings, and if so, what is the real scope?
- Are there other stores of cited physical values that neither
  `constants_new.py` nor the four shell modules account for? This is the
  kind of question a bounded session cannot answer well and a large-context
  audit can.

Relevant: `info_dictionary.py` is one of three orrery modules that
`gallery_studio.py` imports directly (the others are `visualization_utils`
and `celestial_objects`). Those imports are **function-local**, buried
inside function bodies rather than at module top, so a header-only import
walk misses all three. That matters for anyone computing a build path
from the import graph.

---

## Open question 3 -- consumer breakage

Moving 37 feature entries out of four rendering modules into
`constants_new.py`, and migrating 36 citations from comment form to data
form, both touch consumers we may not have enumerated.

Specific things worth your cross-codebase view:

- Every consumer of the four `*_params` dicts. Are they all in the shell
  modules themselves, or does anything else read them?
- Whether the scanner's `SOURCE_PATTERNS` extension has hidden
  dependencies. The provenance-discipline skill warns that scanner changes
  behave like shared-CI changes with family-wide ripple -- extending the
  unit vocabulary once exposed a pre-existing Tier-1 in `star_notes.py`
  that had been invisible.
- Whether any description string resists mechanical interpolation --
  prose where the number is embedded in a way that a format field cannot
  cleanly replace (ranges, approximations, rounded restatements that
  deliberately differ from the stored precision).
- The parallel-pipeline check: `plot_objects` and `animate_objects` are a
  known recurring failure class where a fix lands in one and not the
  other. Confirm both would be covered.

---

## Open question 4 -- source discipline in the assembler

**Tony's ruling, August 6, 2026: the same source discipline applies to
the assembler's own constants, even though there are only a few.**

Framing this correctly matters, because an earlier draft of this document
got it wrong in both directions. The assembler reads DATA -- positions,
orbital elements, feature configs -- from the served cache and never
authors any of it. That model is correct. But the assembler also performs
arithmetic (client-side Kepler propagation, km-to-AU conversion), and
arithmetic needs constants that do not arrive in any cache file.

Current state in the gallery repo at `e7e8c5e`:

```
gallery/assembler/render_orbits.py:41         AU_KM = 149597870.7      uncited
gallery/assembler/render_objects.py:20        AU_KM = 149597870.7      uncited
gallery/assembler/tests/test_artifact1_earth.py:43  AU_KM = 149597870.7  uncited
gallery/assembler/render_orbits.py:42         K_GAUSS = 0.01720209895  uncited
tools/inspect_staging.py:63                   _JD_UNIX_EPOCH = 2440587.5  uncited
tools/gallery_cache_builder.py:90             KM_PER_AU = 149597870.7  CITED
```

Total `# Source:` citations in the entire gallery repo: four.

The correct pattern already exists there, at
`tools/gallery_cache_builder.py:89`:

```python
# Source: constants_new.py:47 (orrery 4e2629c) -- IAU km per AU.
KM_PER_AU = 149597870.7
```

A cross-repo citation naming the file, the line, and the source SHA. That
is the shape the whole architecture in this document is reaching for, and
someone already wrote it by hand, once.

**Two notes on what this is and is not.**

It is NOT evidence bearing on the push/pull fork. These values are exact
by definition (IAU 2012) or conventional, so they do not drift, and an
earlier draft leaned on them as fork evidence incorrectly. Do not weigh
them there.

It IS a claim about the physical world, and therefore in scope for the
discipline regardless of stability. The reasoning error worth avoiding is
substituting "will this drift?" for "is this a claim?" -- stability makes
a value easy to source, not exempt from sourcing. A reader meeting an
uncited number cannot tell a deliberate skip from an unchecked one.

`No Shadow Constants` [CRITICAL] normally prescribes deleting the local
copy and importing the real one. **That remedy is unavailable across the
repo boundary** if self-containment is preserved -- which is the one
place these constants do touch Open Question 1, though weakly. Under
push, the line-89 cross-repo citation is the available remedy and has to
be applied by hand. Under pull, some of these could plausibly ride along
in the same generated artifact as the feature values.

Worth your view on whether that changes the calculus, and on whether
there are other originated values in the gallery repo this enumeration
missed.

---

## What NOT to do

- Do not propose complete-file rewrites. Deliverables in this project are
  runnable transactional patch scripts with anchor verification.
- Do not relitigate the five settled rulings above.
- Do not treat "the values currently agree" as evidence the problem is
  theoretical. The absence of a mechanism is the finding.
- Do not recommend adding a `# Source:` comment to resolve a structural
  problem. Cite-to-clear is a [CRITICAL] violation in this project: a
  citation asserting a provenance that does not exist is worse than no
  citation, because it suppresses the suspicion that would catch it.

---

## Materials

Read these before answering. Several were omitted from a prior audit
prompt and the omission produced a correct finding with a backwards
diagnosis -- that was the orchestrating Claude's error, not the
reviewer's.

**Orrery repo, at `24452442`:**
- `constants_new.py` (the target store; 844 lines, 36 `# Source:` comments)
- `jupiter_visualization_shells.py`, `saturn_visualization_shells.py`,
  `uranus_visualization_shells.py`, `neptune_visualization_shells.py`
  (the 37 feature entries)
- `shell_configs.py` (23 Tier-1 findings; on the interactive build path)
- `export_orbit_cache.py` (`write_feature_configs()`, the exporter that
  does not export)
- `provenance_scanner.py` (SOURCE_PATTERNS; deferred fix item 6 in the
  docstring)
- `info_dictionary.py` (the prose store)
- `LEDGER_CONSOLIDATED.md` -- items L-124, L-154, L-156, L-176, L-177,
  L-179, L-180, L-181, L-182
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` at v16, and its
  summary companion
- `PROJECT_INSTRUCTIONS.md` at v3.34
- `skills/provenance-discipline/SKILL.md` v1.7,
  `skills/orrery-coding-conventions/SKILL.md` v1.3,
  `skills/ledger-and-session-records/SKILL.md` v1.5

**Cross-check worksheets** -- the L-156 Phase 2 Batch 1 competitive
cross-check materials under `documentation/`. Include these. A prior
audit diagnosed the direction of the Mars contradiction backwards
specifically because the worksheets were not supplied.

**Gallery repo, at `e7e8c5e`:**
- `data/objects_config.json` (the frozen seed)
- `tools/gallery_cache_builder.py` (the consumer; its docstring states
  the no-orrery-imports design decision)
- `tools/gallery_studio.py` (the three function-local orrery imports)
- `gallery/assembler/catalog.py`, `resolver.py`, `cache_reader.py`

---

## Note on scanner coverage

The provenance scanner has never been run against the gallery repo. Its
domain classification reports `gallery: 0 findings`, which the
provenance-discipline skill explicitly warns must not be read as "the
gallery has no provenance debt" -- it means the gallery is not scanned
from the orrery repo. Tony has offered to run the scanner and
`module_atlas.py` in the gallery repo. If your review would benefit from
that output, say so and it will be produced.

Note also that the scanner reads `.py` files only
(`if not fname.endswith('.py'): continue`), so `objects_config.json` is
invisible to it in either repo. Whether provenance should extend into
config JSON is a live question this architecture partly answers and
partly defers.

---

*Predesign handoff prepared August 6, 2026 with Anthropic's Claude Opus 5,
built on `24452442aaa64393066cac9d9b5885a763c0a76a` at
https://github.com/tonylquintanilla/palomas_orrery and
`e7e8c5efbe8350e9cca900bafed7bcc8b44529e3` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
