# FABLE REVIEW ROUND 2 -- Feature-Data Transport

**Built on `754f46b1c1459ea79101fa224687e56a51d4fc96`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Gallery repo pinned separately at
`61a78c00668573dbff111ec9f10a96b1cd2fdc35`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).**

Verify both HEADs before reviewing. If either has moved, trace the delta.

**Type:** DESIGN REVIEW, round 2. Zero code delivered.
**Prepared:** August 6, 2026 by Claude Opus 5, Tony Quintanilla integrator.
**Reviewer:** Claude Fable 5.
**Follows:** `documentation/PREDESIGN_HANDOFF_feature_constant_unification.md`
(round 1) and `documentation/FABLE_REVIEW_feature_constant_unification.md`
(your round 1 review, anchored at orrery `ee0da47c` / gallery `61a78c0`).

---

## Repo state -- read this first

**NOTHING FROM THIS DESIGN CYCLE HAS BEEN PATCHED.** At `754f46b`:

- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` is at **v16**.
- `LEDGER_CONSOLIDATED.md` has **no L-186 or L-187**, and L-181 does not
  carry the Track 0 promotion.
- Two patch scripts are committed and unrun: `patch_masterplan_v17.py`
  and `patch_ledger_fable_review_v2.py`. Their edit lists are the
  proposal; the repo shows the pre-proposal state.

Both scripts predate the transport revision described below, so their
transport wording is already stale. Read them for the Track 0 structure,
the exit checklist, and the ledger dispositions -- not for the transport
recommendation.

---

## Who you are writing for

Tony Quintanilla, PE -- a retired civil and environmental engineer,
artist, and anthropologist. He is **not a professional programmer and not
a formally trained astronomer.** He builds Paloma's Orrery through
conversational AI collaboration and holds sole commit authority and final
judgment. The codebase's structure and discipline are the product of that
collaboration; do not read code quality as evidence of his personal
programming fluency.

He runs Python by opening a file in VS Code and clicking Run, and works
through GitHub Desktop. Protocol v3.34 makes that a preference where
practical, not a prohibition. Unpack jargon on first use -- this session
repeatedly failed that test and Tony had to ask each time. Deliverables
are runnable transactional patch scripts.

---

## Why this round exists, and what it says about round 1

Your round 1 review was sound. Every finding in it verified independently
at your anchors, including the four the handoff's evidence chain missed.

But the transport half rested on premises this session supplied and never
checked. Tony removed three of them by asking plain questions. They are
recorded here because the pattern matters more than any single error:
**each was Claude reading code and treating that as knowing the system.**

**Premise 1 -- "the exporter."** Both the round 1 handoff and your review
wrote it as though pointing at something live. It is not.
`export_orbit_cache.py` is a dormant Phase 1b seeding tool: nothing calls
or imports it, all four tooling maps classify it `dev_tools`, and the
gallery references it only as a historical porting source at orrery
`4e2629c`. Your verdict states every piece "extends a pattern that
already exists in the codebase rather than inventing one" -- true for the
store, the three zones, and the citation form, but the exporter was
entirely new.

**Premise 2 -- that derived constants are a problem.** After premise 1
fell, this session proposed having the builder parse `constants_new.py`
with Python's `ast` module and read values without executing the file.
It then found that 7 of 46 assignments are not literal:
`SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU`, and
`CENTER_BODY_RADII = {'Sun': SUN_RADIUS_KM, ...}` (L-162, July 29). This
was written up as a complication in the store. Tony's correction: those
are not duplicates. `SOLAR_RADIUS_AU` has 11 consumer files; deleting it
would push the arithmetic into 11 places. A derived value cannot disagree
with its primary. The store's own docstring already states the rule --
"Derived values are computed from primary constants, never hardcoded
independently."

**Premise 3 -- that the gallery cannot execute the file.** This was the
load-bearing one and was never checked. `constants_new.py` imports
exactly two things: `numpy` and `datetime`. `datetime` is standard
library, and the gallery builder already imports `astroquery` and
`astropy`, both of which hard-depend on numpy. **The gallery environment
already has everything the file needs.** Tony's question was "it's just
arithmetic in the python code, easy" -- and it is, the moment you stop
refusing to run Python.

The `ast` approach came from copying a constraint that belongs to
`provenance_scanner.py`, which must never execute the code it audits. The
builder has no such constraint.

---

## The proposal now

**The nightly builder fetches `constants_new.py` at the orrery HEAD SHA,
imports it, reads the feature values, validates them, and writes them
into the staging cache under the existing atomic-swap semantics.**

1. `git ls-remote` the orrery; record the HEAD SHA.
2. Fetch `constants_new.py` as text at that SHA (not at `main` blind).
3. Write it into the existing per-run staging area and import it. Python
   evaluates all derivation natively -- `SOLAR_RADIUS_AU`,
   `CENTER_BODY_RADII`, anything nested, anything added later.
4. Read the feature values and their `source` fields. Validate: shape,
   source presence on every physics field, and unit-sanity range checks.
5. Write into the staging cache, recording the orrery SHA. Commit with
   the rest of the nightly output.
6. On unreachable, unimportable, or invalid: quarantine, keep serving the
   last committed copy, warn loudly with the SHA lag visible.

**What Tony does: nothing.** He edits a constant, commits, pushes -- the
workflow he has today. No exporter, no new file to run, no scheduled job
committing into the repo where he holds sole commit authority.

**Why this does not violate "No orrery imports."** The builder's
docstring states that design decision, and its spirit is *do not couple
the gallery to the orrery's module graph*. `constants_new.py` is a leaf:
numpy and `datetime`, nothing else. No Plotly, no shell modules, no
`palomas_orrery`. This is materially different from
`export_orbit_cache.py`, where importing `SHELL_CONFIGS` drags Plotly
along -- the specific obstacle that stopped the original exporter from
carrying values across. We recommend updating the docstring wording
rather than leaving a rule that now reads broader than intended.

---

## What we want from you

**Q1 -- Is fetch-and-import sound, and what does it cost that we have not
priced?** The obvious concern is executing fetched code. Our read: this
is Tony's own repo, at a pinned SHA, fetched by his own builder, running
on his own machine -- not an untrusted source in any meaningful sense.
Say so if you disagree, and say specifically what you would guard.

**Q2 -- Does the leaf claim hold, and will it keep holding?**
`constants_new.py` imports only numpy and `datetime` today. Is anything
in Track 0's scope likely to add an import? If the store later grows a
dependency the gallery lacks, the import fails at build time and
quarantines -- a loud failure, but worth knowing whether that is likely
or merely theoretical.

**Q3 -- Does this preserve the fallback property you valued in round 1?**
Your case for vendored pull rested partly on the committed copy: an
unreachable orrery falls back to last night. Step 5 commits the derived
values, so we believe it survives. Confirm or correct.

**Q4 -- What breaks that we have not seen?** Round 1 found four things
the evidence chain missed, and that was its main value. Aim at the same
target. Concretely: are there feature values, or values feature data will
depend on, that this transport cannot carry correctly?

**Q5 -- Does the Track 0 exit checklist hold?** It is in
`patch_ledger_fable_review_v2.py`, in the L-181 additions: no hand step,
abort on missing source, unit-sanity range checking, and the
store-to-builder coupling documented on both sides. Two specific
questions. Is unit-sanity the right guard for its class -- shape
validation and source-presence validation both PASS on a value whose
units changed, so neither catches a km-to-AU slip? And is "documented in
three places" sufficient for the coupling, or does it need a mechanical
check rather than three notes? Note that fetch-and-import weakens the
coupling considerably compared to `ast` extraction: the builder now reads
NAMES, not structures, so renames still break it while nesting and shape
changes do not.

**Q6 -- Sequencing.** The proposal builds the transport AFTER Track 0
settles the store, on the grounds that Track 0 is itself a restructure.
Fetch-and-import may weaken that argument, being far less
shape-sensitive. Any case for building it earlier to de-risk the design?

**Q7 -- Anything else in your round 1 review that the removed premises
invalidate.** You are better placed than we are to see what leaned on
them.

---

## What NOT to do

- Do not re-litigate the architecture. One store, three zones, provenance
  as data, derivation instead of annotation -- endorsed in round 1,
  ratified by Tony. This round is transport only.
- Do not re-litigate the ordering ruling (Track 0 scaffolding, then Track
  1 provenance batches, then Track 2 Artifact 2). Settled August 6.
  Reasoning: a golden artifact is fingerprinted, so locking one on values
  not yet sourced and derived means redoing the lock rather than editing
  a number.
- Do not propose complete-file rewrites.
- Do not recommend a `# Source:` comment as a fix for a structural
  problem. Cite-to-clear is [CRITICAL] in this project.

---

## Materials

**Orrery, at `754f46b`:**
- `constants_new.py` -- the store. Note lines 46-47 (the only imports),
  the derived values at 111, 115, 138, 145, and `CENTER_BODY_RADII` at
  362.
- `patch_masterplan_v17.py`, `patch_ledger_fable_review_v2.py` -- Track 0
  structure and ledger dispositions. Transport wording is stale.
- `export_orbit_cache.py` -- the dormant tool, for the record.
- `provenance_scanner.py` -- line 899 onward, for contrast: a tool that
  must not execute what it audits.
- `jupiter_`/`saturn_`/`uranus_`/`neptune_visualization_shells.py` -- the
  37 feature entries and the module-level `*_info` strings you found.
- `documentation/PREDESIGN_HANDOFF_feature_constant_unification.md`
- `documentation/FABLE_REVIEW_feature_constant_unification.md` -- yours.
- `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` at v16.
- `LEDGER_CONSOLIDATED.md` -- L-176, L-179, L-180, L-181, L-182, L-184,
  L-185.
- `skills/provenance-discipline/SKILL.md` v1.7,
  `skills/gallery-cache-builder/SKILL.md` v1.2,
  `skills/ledger-and-session-records/SKILL.md` v1.5
- The L-156 cross-check worksheets under `documentation/`.

**Gallery, at `61a78c0`:**
- `tools/gallery_cache_builder.py` -- the consumer. Its docstring carries
  the "No orrery imports" decision; `derive_served()` at line 1008 and
  the staging / atomic-swap machinery are where this would land.
- `data/objects_config.json` -- the frozen seed, one commit in its
  history.
- `MODULE_ATLAS.md` / `MODULE_INDEX.md` -- 24 modules, regenerated Aug 6.
- `gallery/assembler/render_orbits.py`, `resolver.py`, `cache_reader.py`.

---

*Round 2 review prompt prepared August 6, 2026 with Anthropic's Claude
Opus 5, built on `754f46b1c1459ea79101fa224687e56a51d4fc96` at
https://github.com/tonylquintanilla/palomas_orrery and
`61a78c00668573dbff111ec9f10a96b1cd2fdc35` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
