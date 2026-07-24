Built on:
- orrery: bdab1674d8794c67aeb000ee83176e295565f637 at https://github.com/tonylquintanilla/palomas_orrery
- gallery: c2a323b7cea5c885995b7d4750a06c42383e5605 at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Type: DESIGN SESSION (zero code)
Companion: prep work for the provenance scanner refactor already underway
in PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md (July 22),
DESIGN_HANDOFF_provenance_scoring_and_pinning.md, and
DESIGN_REVIEW_provenance_scoring_and_pinning.md. See Section 12 for the
overlap and dependency this creates.

Ledger handle: L-163 (L-154 through L-162 are already assigned to the
scoring-model/gallery-scanner refactor above; confirmed against
LEDGER_CONSOLIDATED.md at this SHA, highest in use is L-153, and the
three documents above originate L-154 through ~L-162).

---

# ROLE_MAP / Domain Classification Redesign -- Design Handoff

## 1. Problem, verified at HEAD

`ROLE_MAP` in `module_atlas.py` is a hand-maintained dict (94 entries
covering 121 root modules) that has drifted:

- 19 modules fall through to `'other'` silently (not caught by the
  existing `_shells` suffix heuristic): `barycenter_cache_check`,
  `color_map`, `data_inventory`, `earth_system_common`,
  `export_orbit_cache`, `food_insecurity_generator`, `ledger_index`,
  `measure_animation_html`, `measure_perframe_elements`,
  `orrery_rendering`, `provenance_scanner_color_patch`,
  `scenarios_food_insecurity`, `shell_configs`, `skills_index`,
  `smoke_dipole_cone`, `smoke_phase4`, `smoke_rotation_axis`,
  `test_reset_completeness`, `titan_io_probe`.
- Of those, 5 already have claim-shaped content invisible to citation
  scanning per the checked-in `PROVENANCE_AUDIT.md` (July 17, 2026):
  `shell_configs.py` (91 strings), `export_orbit_cache.py` (8),
  `food_insecurity_generator.py`, `orrery_rendering.py`,
  `smoke_rotation_axis.py` (1 each).
- 7 `ROLE_MAP` entries reference files that don't exist in this repo.
  Confirmed this session: 5 are gallery-repo modules that will get their
  own atlas there (`gallery_studio`, `gallery_editor`,
  `gallery_json_fixer`, `json_converter`, `json_gallery`) -- simple
  deletion from this repo's `ROLE_MAP`, no sweep action needed. The
  other 2 are NOT gallery-related: `orrery_integration` (disposition
  unclear -- no matching file, no context found; flag for Tony) and
  `star_visualization_gui_before_pyinstaller_refactor` (confirmed
  superseded -- matches the exact "_before_" pattern surfaced in
  Section 4 below; the file is already gone, only the ghost `ROLE_MAP`
  entry remains).
- 3 consumers import `classify_role`/`ROLE_MAP` directly, not 1:
  `module_atlas.py` (producer), `provenance_scanner.py`, `dep_trace.py`
  (the last has an `except: ROLE_MAP = {}` fallback -- see Section 4a,
  a real gap found this session, not just a defensive no-op).
- Star-related modules (`sgr_a_star_data`, `star_notes`,
  `star_properties`, `star_sphere_builder`, `star_visualization_gui`)
  are already correctly classified -- confirmed clean, not part of the
  gap.

## 2. Precedent this design extends

`ledger_index.py` already solves the same shape of problem for ledger
blocks: reads one structured metadata line per block, auto-fixes what's
mechanically knowable, and flags (report-only: a `problems` list +
`sys.exit(1)`) whatever is a genuine judgment call rather than guessing.
This redesign is that pattern applied to module classification, not a
new invention. (Section 12 notes that the provenance-scoring refactor
already cites this same pattern as precedent for its own new mechanism
-- another reason this design should land clean before that one builds
on it.)

## 3. Core mechanism -- Role

- Every module's docstring carries one explicit line: `Role: <value>`,
  using only the existing 12-value vocabulary (`gui`, `rendering`,
  `rendering/shells`, `computation`, `data`, `cache`, `pipeline`,
  `scenario`, `utility`, `devtool`, `legacy`, `other`).
- `utility` also covers shared exception/infrastructure modules (e.g.
  `errors.py`-style modules) -- confirmed; no 13th role added.
- `__init__.py` package-marker files are exempted from classification
  entirely -- documented exclusion, same move as color values being
  excluded from the provenance audit. Not scored, not flagged.
- A NEW, narrow parser reads `ast.get_docstring(tree)` **raw** and
  regex-matches the `Role:` line. It must NOT reuse the existing
  `get_module_docstring()` -- that function is a cosmetic 300-char
  paragraph-joining purpose-summarizer built for a different job and
  risks mangling or dropping a structured tag.
- Three states, not two:
  1. Valid tag found -> use it.
  2. No tag, but a legacy `ROLE_MAP` entry exists -> N/A after the
     sweep (see Rollout, Section 11) -- this branch is only needed if
     the classifier ever ships before the sweep completes.
  3. No tag, nothing to fall back on -> **`'undetermined'`** (new
     sentinel, distinct from `'other'`, which stays a real,
     deliberately-chosen bucket). Flagged, never guessed.
- Filename heuristics (existing `_shells` suffix; proposed
  `scenarios_*` / `smoke_*` / `test_*` / `measure_*` prefixes) are kept
  as **suggestion-only** -- may populate a candidate role next to a
  flagged/undetermined entry, never silently auto-assign.

## 4. Files verified this session -- archive vs. sweep

Before the sweep touches every docstring, some candidates should be
verified as one-time/superseded and removed to Tony's local archive
instead of being tagged as permanent. Checked repo-wide references for
each rather than going by docstring framing alone:

**Archive candidates (zero live references, confirmed one-time or
orphaned):**

| File | Evidence |
|---|---|
| `provenance_scanner_color_patch.py` | Docstring: "run this once" (July 16, 2026). Zero references anywhere. |
| `smoke_phase4.py` | Zero references anywhere, not even in classification dicts. |
| `smoke_dipole_cone.py` | Only classification-dict mentions, no functional callers. Tied to "Movement 2, June 2026" build verification. |
| `smoke_rotation_axis.py` | Same as above; cross-referenced only by `smoke_dipole_cone.py`'s own docstring, not by any functional caller. |
| `titan_io_probe.py` | Single bare list-comprehension line, no docstring, no function wrapper, zero references. Would produce no output if run. Contrary to the initial hypothesis that this one might be active -- evidence points the other way. Flagged for Tony's own verification in case a fuller version exists elsewhere. |
| `color_map.py` | Zero real callers. The 12 apparent references were a naming collision with an unrelated `color_map` function imported from `constants_new.py`. Matches Tony's own preference for the graphic file over running this script. |
| `barycenter_cache_check.py` | Tiny ad hoc diagnostic (loads `orbit_paths.json`, prints barycenter key info). Zero references, no docstring. |

**Pending external decision -- sweep normally for now, do NOT archive:**

| File | Evidence |
|---|---|
| `test_constants_provenance.py` | L-160 (provenance refactor track) plans to absorb this file's pinning logic into `provenance_scanner.py` and retire the standalone file -- Tony confirmed the intent directly this session. But checked at current HEAD: `provenance_scanner.py` has no `PINNING_MAP`/`run_pinning_checks`, and its own credit line reads "April 2026" -- the absorption target doesn't exist yet. This file is currently the ONLY place that pinning logic lives. Archiving it now would remove the reference implementation the future build needs to migrate from. Tag it `devtool` and sweep normally; do not move it to local archive until L-155/156/160 actually ship and the replacement is verified working. |

**Confirmed to stay (live, permanent infrastructure -- sweep normally):**

| File | Evidence |
|---|---|
| `test_reset_completeness.py` | Wired into the dashboard menu; cross-referenced by comment in `palomas_orrery.py` line 8264. |
| `test_orbit_cache.py` | No mention in the retirement-scoped provenance-refactor documents; comprehensive ongoing suite. |
| `create_cache_backups.py` | Deliberately one-shot-BY-DESIGN manual utility ("run before risky cache operations"), not superseded. |
| `stellar_data_patches.py` | Actively imported by 4 real modules: `hr_diagram_distance.py`, `hr_diagram_apparent_magnitude.py`, `planetarium_apparent_magnitude.py`, `planetarium_distance.py`. |

Net effect on sweep scope: the 3 previously-docstring-less files
(`titan_io_probe.py`, `color_map.py`, `barycenter_cache_check.py`) are
now archive candidates, not "write a docstring for these" -- pending
Tony's confirmation, they likely need NO new docstring at all, just
removal to local archive and a `ROLE_MAP` deletion.

## 4a. dep_trace.py -- gap found, folded into THIS build's scope

`dep_trace.py` stays a separate tool (different job: interactive
visualization vs. a static reference document) and is already
correctly single-sourced in the case that matters -- it imports
`classify_role`/`ROLE_MAP` from `module_atlas.py` first, before any
fallback. But its fallback path (triggered only if that import fails)
has its OWN hardcoded copy of the `_shells` heuristic and its own
silent `'other'` default, baked in locally
(`get_category()`, lines ~156-165). That is the same duplicated-logic
pattern being retired everywhere else in this design.

Decision: fold this into the CURRENT build (role only), not the
deferred domain phase. Drop the local fallback cascade; if
`module_atlas` isn't importable, surface a visible warning instead of
quietly re-deriving a stale, pre-redesign classification. Note
`_ROLE_TO_VISUAL` (the role -> graph color/shape mapping) is a
legitimate, different-purpose local table -- a presentation concern,
not a competing classification -- and stays as-is.

## 5. ROLE_MAP's fate

Kept, but retired as a hand-edited artifact -- regenerated inside
`module_atlas.py` between marker comments, same pattern as
`ledger_index.py`'s INDEX zone and `skills_index.py`'s Skill Manifest
table. Written FROM the docstring tags, never the reverse. `dep_trace.py`
keeps its existing plain-dict fallback path unchanged (see 4a for the
one real gap in it).

## 6. Reporting

Same `problems`-list + exit-code pattern as `ledger_index.py` (console,
visible in VS Code's Run panel), PLUS a visible "UNCATEGORIZED /
UNDETERMINED" section written directly into `MODULE_ATLAS.md` and
`MODULE_INDEX.md` -- required because the atlas is meant to be uploaded
into a fresh Claude session with no access to console output.

## 7. MODULE_INDEX.md is not a 4th consumer

Verified directly: `generate_index(modules, output_path)` reads
`mod['role']` from the same already-scanned list `generate_atlas()`
uses -- it never imports `classify_role`/`ROLE_MAP` itself. Its function
is unchanged by this redesign: light, human-browsable table (name +
docstring description + line count) for reading directly on GitHub,
distinct from `ROLE_MAP` (machine lookup) and `MODULE_ATLAS.md` (deep
reference for AI-session upload). Three outputs, three audiences, no
redundancy.

## 8. Gallery repo -- structural finding + SCAN_PATHS

Zero `.py` files at gallery repo root. All 25 modules live across 4
directories:
- `tools/` (9): `gallery_studio.py`, `gallery_editor.py`,
  `json_converter.py`, `gallery_json_fixer.py`,
  `gallery_cache_builder.py`, `gallery_cleanup.py`,
  `debug_encke_tp.py`, `inspect_staging.py`,
  `test_gallery_cache_builder_offline.py`
- `gallery/assembler/` (11): `render_orbits.py`, `render_objects.py`,
  `render_events.py`, `render_spacecraft.py`, `resolver.py`,
  `cache_reader.py`, `catalog.py`, `models.py`, `errors.py`,
  `assemble.py`, `presentation.py`
- `gallery/assembler/harness/` (2): `fingerprint.py` + `__init__.py`
- `gallery/assembler/tests/` (2): `test_artifact1_earth.py` +
  `__init__.py`

Decision: `module_atlas.py` stays at gallery repo ROOT (not copied into
a subdirectory), gains an explicit path list rather than recursion:

```
SCAN_PATHS = ['tools', 'gallery/assembler',
              'gallery/assembler/harness', 'gallery/assembler/tests']
```

Orrery copy keeps `SCAN_PATHS = ['.']` (unchanged behavior). No CLI
flags -- stays a plain Run-button script, consistent with Tony's
VS Code-only workflow. Checked for name collisions across the 4 paths:
only `__init__.py` (in 3 of them), moot since it's exempted. Any future
collision among real modules should be flagged (report-only), not
silently overwritten -- same move as `ledger_index.py`'s duplicate-handle
check.

## 9. Adjacent finding, out of scope: data_inventory.py

Classifies DATA files (not code) by extension/count/size, peeks schema
of key files, computes GitHub Pages headroom. Zero real programmatic
consumers (the dashboard entry is a launcher menu item; the
`provenance_scanner.py` mention is a string key in ITS OWN separate
'Findings by File Type' dict, unrelated). Its output
(`DATA_INVENTORY.md`) is deliberately never committed to either repo --
emitted to upload only, because the data it inventories is
gitignored/local and would go stale the instant it was checked in.
Already correctly designed: earns tier-1 (fresh-upload) trust per the
protocol's Context Priority, not tier-2 (repo-HEAD). No action needed;
noted for completeness, not part of this redesign.

## 10. Second parallel-list discovery -- Domain classification

`provenance_scanner.py` also carries `MODULE_DOMAIN_MAP` /
`DOMAIN_LABELS` -- a second hand-maintained, name-keyed dict, genuinely
orthogonal to `ROLE_MAP` (Domain answers "what part of the project is
this," not "what does this module do"; it drives report grouping only,
never scanning eligibility). Six existing values: `orrery`,
`earth_science`, `gallery`, `stars`, `utilities`, `dev_tools`. This was
a deliberate, recent, Tony-confirmed decision (F1 provenance-cleanup
groundwork session, July 2026) -- genuinely a different axis, NOT to be
collapsed into role.

It shares `ROLE_MAP`'s exact staleness risk, though, and uses an OLDER,
weaker fallback (silently defaults unmapped modules to `'orrery'`,
tracked separately) that should be upgraded to the same
explicit-tag-or-undetermined discipline as role.

**Decision (mechanism deferred to the provenance scanner refactor):**
extend the docstring convention with a second explicit line,
`Domain: <value>`, parsed by the same raw-docstring mechanism.
`module_atlas.py` becomes the single source for BOTH role and domain;
`provenance_scanner.py` retires `MODULE_DOMAIN_MAP`/`DOMAIN_LABELS` and
imports domain the way it already imports role. This code change is OUT
OF SCOPE for the current sweep/classifier build -- captured here so it
isn't lost, to be picked up during the provenance scanner refactor
(see Section 12 -- that refactor is already substantially designed).

**Scope correction:** `MODULE_DOMAIN_MAP`'s own comment confirms
`provenance_scanner.py` never scans the gallery repo, so this was
originally orrery-only. Gallery-repo docstrings get `Domain:` tags added
NOW anyway, during this same content sweep, rather than requiring a
second full pass later -- but NOT because they feed L-155 (correcting an
assumption made earlier in this design). Checked L-155's actual scope in
full: it is an explicit `PINNING_MAP` table over specific named data
values (radius/geometry constants in `objects_config.json`), AST-
extracted, with no role/domain classification involved at all -- "loud
skip if gallery repo absent." It does not consume module-level domain
tags. The value of tagging gallery modules now is standalone: MODULE_
ATLAS/INDEX grouping, and doing the content work once while every
docstring is already being touched, rather than a second pass later.

**Naming caution:** role uses `utility`/`devtool`; domain uses
`utilities`/`dev_tools` -- close enough to invite a typo between the
two tags. Keep `Role:`/`Domain:` prefixes visually distinct in the
docstring.

## 11. Gallery repo -- Domain vocabulary (confirmed this session)

Applying the orrery's 6-value vocabulary would trivially read `gallery`
for every module (zero discriminating power for a gallery-scoped
scanner). Instead, a gallery-specific 4-value vocabulary was proposed
and confirmed, mirroring the repo's own existing skill boundaries:

| Domain | Modules |
|---|---|
| `gallery_pipeline` | `gallery_studio.py`, `gallery_editor.py`, `json_converter.py`, `gallery_json_fixer.py` |
| `cache_builder` | `gallery_cache_builder.py`, `gallery_cleanup.py` |
| `assembler` | `render_orbits.py`, `render_objects.py`, `render_events.py`, `render_spacecraft.py`, `resolver.py`, `cache_reader.py`, `catalog.py`, `models.py`, `errors.py`, `assemble.py`, `presentation.py` |
| `dev_tools` | `debug_encke_tp.py`, `inspect_staging.py`, `test_gallery_cache_builder_offline.py`, `harness/fingerprint.py`, `tests/test_artifact1_earth.py` |

This mirrors the `gallery-pipeline` / `gallery-cache-builder` /
`gallery-assembler` skills already in place, plus the same `dev_tools`
value already used in the orrery vocabulary, for consistency across
repos.

## 12. Overlap with the provenance scanner refactor (found this session)

While verifying file disposition for Section 4, found
`documentation/MASTER_PLAN_UPDATE_provenance_and_prep.md` (dated today),
which led to three more documents not previously read in this design
thread:

- `PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md` (July 22)
  -- originates L-154 through L-160. Covers a resolver bug fix, physical
  radius source-of-truth, the scanner's scoring/criticality model, and
  the cross-repo gallery scanner (this is almost certainly "the scanner
  for the interactive gallery" Tony referenced -- confirmed by title:
  "Cross-Repo Gallery Scanner").
- `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` (598 lines) and
  `DESIGN_REVIEW_provenance_scoring_and_pinning.md` (282 lines) -- design
  and review of the scoring-model fix.

Two concrete overlap points found (grep-level pass, not a full read --
flagged for further reconciliation before build):

1. The scoring-model design cites *"the same pattern the scanner
   already uses for ROLE_MAP and domain coverage gaps"* as precedent
   for its own new criticality-classification mechanism. Sequencing
   matters: this design's improved pattern (explicit tag, `undetermined`
   sentinel, no silent default) should land before or alongside that
   one, so the precedent being extended is the corrected version.
2. Section D10 of the scoring-model design handoff already decides to
   retire `test_constants_provenance.py` and separately enumerates the
   `ROLE_MAP` entry in `module_atlas.py` and the `MODULE_DOMAIN_MAP`
   entry in the scanner as 2 of 5 cleanup sites for that retirement --
   the same two structures this design also touches.

Ledger handle assigned: **L-163** (see header). Not folded into the
L-155-162 cluster itself, since this design's decisions are separable,
but the Ref section below cross-links both directions and the two
threads should be sequenced/coordinated, not built independently by
different sessions unaware of each other.

## 13. Skills update needed -- larger than first flagged, two skills, two timings

Checked `provenance-discipline` in full this session, not just recalled
from its header -- it carries substantially more ROLE_MAP/MODULE_DOMAIN_MAP
detail than the earlier note credited.

**`ledger-and-session-records`** (Codebase Tooling section) -- small
edit, lands with L-163's build. Currently: "new modules need `ROLE_MAP`
entries (coverage-gap findings point at the missing ones)" -- describes
the retired hand-edit workflow. Replace with the docstring-tag
convention + regenerated-marker-zone mechanism.

**`provenance-discipline`** -- larger, two separate edits on two
different timelines:
- **Lands with L-163's build (role only).** The "File inclusion is
  role-driven (L-078)" bullet under Scanner Mechanics: "resolve those by
  adding `ROLE_MAP` entries, not by editing the scanner" -- rewrite for
  the docstring-tag mechanism.
- **Lands with the L-156 cluster's Phase 3** (domain retirement, per
  Fable's amendment 2b, gated on this sweep completing first). The
  entire "Report Domain Classification" section (~40 lines) documents
  `MODULE_DOMAIN_MAP`/`classify_domain()` mechanics in working detail --
  "Extend `MODULE_DOMAIN_MAP` directly (not a heuristic) when a new file
  needs a home" is exactly the workflow being retired. Needs a full
  rewrite once that phase ships, not a patch.

Both skills carry a version + source-SHA line in their own header; each
edit bumps it. Neither update happens now -- both are premature until
their respective code exists to document accurately, same reasoning as
not building the classifier before the sweep completes. Captured here,
split by which build unlocks which edit, so neither floats.

Also found: `add_docstrings.py` already exists (batch-inserts module
docstrings, has a preview mode, touches no code) and is the right
existing tool to extend for actually executing the sweep, rather than
building something new.

## 14. Master plan

`documentation/MASTER_PLAN_UPDATE_provenance_and_prep.md`'s existing
"Section 6 Prep Work" is the right home for an entry on this design,
matching its own established format (see its "L-162 -- CENTER_BODY_RADII
de-duplication" entry as the template). Drafting deferred until L-163
is confirmed in the ledger.

## 17. Build sequencing

Four phases. Unlike the L-156 cluster's four phases (each independently
pushable), these are strictly gated -- each depends on the last actually
completing and being verified, not just designed, per the same
reasoning as Section 16's Phase-4 placement for the skill edits: you
cannot accurately build against or document a state that doesn't exist
yet.

**Phase 1 -- Archival and repo hygiene (content, no code).** Confirm the
7 archive candidates (Section 4) with Tony, move each to local archive,
delete their `ROLE_MAP` entries. Delete the 7 ghost `ROLE_MAP` entries
(5 gallery-repo names, `star_visualization_gui_before_pyinstaller_
refactor`) -- except `orrery_integration`, still undetermined (Section
1), ask Tony rather than guessing before closing this phase.
`test_constants_provenance.py` is explicitly NOT part of this phase's
archival (Section 4's pending-external-decision category).

**Phase 2 -- Content sweep (docstrings only, still no code).** Every
remaining real module in both repos gets an explicit `Role:` line
(121 orrery + ~22 gallery) and, where applicable, a `Domain:` line
(orrery: migrated from current `MODULE_DOMAIN_MAP`; gallery: the
4-value vocabulary in Section 11) -- via `add_docstrings.py`'s preview
mode first, written mode after review. Exact tag placement/format
relative to the credit line (Section "Gap") is the first thing to lock
down in this phase, before running it at scale.

**Phase 3 -- Classifier code.** New raw-docstring parser (Section 3);
`classify_role()` rewrite (3-state: valid tag / `undetermined`);
`ROLE_MAP` regeneration marker-zone (Section 5); UNCATEGORIZED/
UNDETERMINED report section in both atlas outputs (Section 6);
`SCAN_PATHS` + multi-path merge with collision-flagging for the gallery
copy (Section 8); the three call-site updates (`module_atlas.py`'s own
scan, `provenance_scanner.py`, `dep_trace.py`); `dep_trace.py`'s
fallback-cascade fix (Section 4a). Gated on Phase 2 completing in full
-- the classifier has nothing to read otherwise. Closes with the full
`agentic-pre-test` protocol, not `py_compile` alone.

**Phase 4 -- Verify, then document.** Run the shipped classifier against
the swept docstrings; confirm `ROLE_MAP` regenerates as expected and
every `undetermined` entry is accounted for, not a surprise. Only then:
update `ledger-and-session-records`' Codebase Tooling note and
`provenance-discipline`'s role-driven-inclusion bullet (Section 13) --
describing what Phase 3 actually verified, not what it intended. Bump
both skills' version + source-SHA header lines.

**Out of scope for all four phases:** the domain-code retirement
(Section 10) is a different build entirely, inside the L-156 cluster's
own Phase 3, gated on this Phase 2 completing first (it needs the swept
`Domain:` tags to exist) -- do not attempt it here.

Suggested builder: a Sonnet-class build session for all four phases --
bounded, well-specified implementation against an already-reviewed
design, matching the project's own assignment for the adjacent
cluster's Phases 1-3.

## Gap -- next-session scope

- **Orrery sweep:** 3 files previously flagged as "missing docstrings"
  are now archive candidates instead (Section 4) -- pending Tony's
  confirmation, likely need no new docstring, just removal + `ROLE_MAP`
  deletion. Also archive: `provenance_scanner_color_patch.py`,
  `smoke_phase4.py`, `smoke_dipole_cone.py`, `smoke_rotation_axis.py`.
  `test_constants_provenance.py` is NOT archived -- tag it `devtool` and
  sweep normally; its L-160 absorption target isn't built yet (verified
  at HEAD), so the standalone file stays until the replacement ships.
  Every remaining real module needs an explicit `Role:` line (migrated
  from current `ROLE_MAP` where valid) and a `Domain:` line (migrated
  from current `MODULE_DOMAIN_MAP`; unmapped ones need resolving).
- **Gallery sweep:** ~22 real modules (25 minus 3 `__init__.py`) need
  both `Role:` and `Domain:` written from scratch.
- **Exact tag placement/format** relative to the existing
  `Module updated: [Month Year] with Anthropic's Claude [model].`
  credit line -- direction agreed (near it), exact template not yet
  locked.
- **Code changes, this build (role, now includes dep_trace.py fix):**
  new raw-docstring parser in `module_atlas.py`; `classify_role()`
  rewrite (3-state: valid tag / undetermined); `ROLE_MAP` regeneration
  marker-zone; UNCATEGORIZED/UNDETERMINED report section in both atlas
  outputs; `SCAN_PATHS` + multi-path merge with collision-flagging for
  the gallery copy; call-site updates in `provenance_scanner.py` and
  `dep_trace.py`; drop `dep_trace.py`'s local fallback cascade (4a).
- **Code changes, deferred to provenance refactor (domain):**
  `provenance_scanner.py` retires `MODULE_DOMAIN_MAP`/`DOMAIN_LABELS`,
  imports domain from `module_atlas.py` instead; the cross-repo gallery
  scanner (L-155) consumes gallery-repo `Domain:` tags.
- **Skill updates (Section 13, two skills, split by timing):**
  `ledger-and-session-records`' Codebase Tooling section and
  `provenance-discipline`'s "File inclusion is role-driven" bullet land
  with THIS build (role). `provenance-discipline`'s entire "Report
  Domain Classification" section (~40 lines) lands with the L-156
  cluster's Phase 3 (domain retirement) -- do not edit it now, the
  mechanism it would describe doesn't exist until then. Both skills bump
  their version + source-SHA header line on edit.
- **Reconciliation needed before build:** a fuller read of the three
  provenance-refactor documents (Section 12) against this design,
  particularly the ROLE_MAP/MODULE_DOMAIN_MAP precedent-citation and
  the shared cleanup sites for D10's retirement list.
- **Done this session:** L-163 ledger DETAIL block drafted (with Fable's
  two confirmed amendments folded into its Gap/Note); matching Section-6
  entry for `MASTER_PLAN_UPDATE_provenance_and_prep.md` drafted; Fable 5
  review completed and independently re-verified (Section 16). Both
  await Tony pasting them into the actual files and pushing.

## Ref

`module_atlas.py`, `provenance_scanner.py` (`MODULE_DOMAIN_MAP`,
`DOMAIN_LABELS`, `classify_role` import), `dep_trace.py`,
`ledger_index.py` (pattern precedent), `add_docstrings.py` (sweep
execution tool), `PROVENANCE_AUDIT.md` (July 17, 2026 -- coverage-gap
evidence), `provenance-discipline` skill (needs update, Section 13 --
two edits, two timings), `ledger-and-session-records` skill (needs
update, Section 13), `gallery-pipeline` /
`gallery-cache-builder` / `gallery-assembler` skills (gallery domain
vocabulary source), L-078 (role-driven coverage-widening track),
`MASTER_PLAN_UPDATE_provenance_and_prep.md` (Section 14),
`PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md`,
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`,
`DESIGN_REVIEW_provenance_scoring_and_pinning.md` (all Section 12 --
L-154 through ~L-162 cluster, overlaps this design touches).

## 15. Prompt for Fable 5 (review, not design)

*(Same optimization as the project's existing Fable prompts -- brief,
reason-first, explicit boundaries, claim-grounding, trusts its judgment
rather than enumerating a checklist. Self-contained: paste as the
opening message in a new thread, attach this document. Fable 5 is the
right reviewer here specifically because it authored
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md` -- it already has the
deepest working knowledge of the cluster this design has to coordinate
with.)*

> I'm working on the Paloma's Orrery project with Tony Quintanilla (PE,
> retired civil/environmental engineer, not a professional developer --
> builds this through AI collaboration, holds sole commit authority).
> Attached is a design (Sonnet 5) for retiring two hand-maintained module-
> classification dicts (`ROLE_MAP`, `MODULE_DOMAIN_MAP`) in favor of an
> explicit tag in each module's own docstring, mechanically regenerated --
> the same pattern `ledger_index.py` already uses for its INDEX zone.
>
> **This is a review, not a design or build session.** Don't write or
> edit any file, don't propose a diff, don't touch either repo beyond
> reading. If your review's natural next step is "now implement this,"
> stop there and hand it back.
>
> Read the attached handoff in full first, then re-familiarize yourself
> with your own `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` and
> `PREDESIGN_HANDOFF_provenance_scoring_and_gallery_scanner.md` -- you
> authored the design this one has to coordinate with, so you're
> reviewing against your own work, not someone else's. Pull both repos
> fresh and re-confirm the SHAs in "Built on" still match before treating
> anything here as current; don't trust the summary over the live repo.
>
> **Your specific angle, not a general re-review:** this design's own
> verification (repo-wide reference checks, live HEAD reads) is already
> thorough on its own terms -- don't re-audit that. What only you can
> judge well is the integration with your cluster. Three concrete points
> already surfaced, but use your own judgment on whether there's more:
>
> 1. Section 12 -- your scoring-model design cites "the same pattern the
>    scanner already uses for ROLE_MAP and domain coverage gaps" as
>    precedent for the new criticality-classification mechanism. This
>    design changes that pattern (explicit tag, `undetermined` sentinel,
>    no silent default). Does your citation still hold against the
>    changed version, and does sequencing -- this landing first -- still
>    make sense, or would you sequence it differently?
> 2. Section 4's file-disposition table keeps `test_constants_provenance.py`
>    in the repo, untagged for archival, specifically because your D6/L-160
>    absorption target doesn't exist in `provenance_scanner.py` yet
>    (checked at HEAD). Does that read of D10's intent match what you
>    actually meant, or is there a cleaner way to sequence the standalone
>    file's retirement against your own build?
> 3. Anything else in your cluster's internals -- the pinning engine
>    placement, the `MODULE_DOMAIN_MAP`/`DOMAIN_LABELS` retirement this
>    design defers to your refactor, the five-listing-site cleanup in
>    D10 -- that this design's author, working without your cluster's
>    full internal detail, may have gotten wrong or oversimplified.
>
> Pause for Tony only on an actual judgment call with no clearly better
> answer -- not to confirm each point along the way.
>
> When you report back: lead with what you'd actually recommend, not a
> survey of everything considered. Structure it the way your own design
> review of this cluster was structured -- confirmed as-written, amended,
> new scope -- so it drops in next to Section 12's findings cleanly.
>
> Deliverable: a review document (zero code), anchored with both repos'
> SHAs the same way this one is.

## 16. Fable 5 review -- confirmed, 3 amendments (verified this session)

Fable reviewed against its own cluster (it authored
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`). Recommendation:
build-ready, land before its cluster as proposed. Both prompt questions
confirmed (precedent citation holds; `test_constants_provenance.py`
sequencing read is exactly right). Independently re-verified the three
load-bearing claims below against live HEAD before accepting them --
all checked out:

- **Domain fallback is default-plus-tracked, not purely silent.**
  `classify_domain()` returns `(domain, was_mapped)` -- corrects
  Section 10's framing above. Doesn't change the design (still upgrading
  to explicit-tag-or-`undetermined`), just the accuracy of why.
- **D10's `ROLE_MAP` cleanup site stops being a hand-edit.** Once
  regenerated, the entry disappears on the next `module_atlas.py` run
  after a file is archived -- Phase 3's checklist wording needs updating
  when that manifest is drafted, or a builder will hunt for an edit
  that no longer exists.
- **Real gap: the domain-code retirement has no landing phase.**
  Verified against the actual Phase 1-4 text -- Phase 3 touches
  `MODULE_DOMAIN_MAP` only for D10's single-entry cleanup, never the
  full dict-to-docstring-tag conversion this design defers. Fix:
  domain retirement joins Phase 3, gated on "L-163 sweep complete."
- **Real dependency: sequence the sweep before L-157's worksheet.**
  Giving 19 modules a real role (5 with claim-shaped content,
  `shell_configs.py` alone 91 strings) pulls new findings into scan
  scope, landing in counts D7/L-161 calibrated against. D8's own item 3
  states the precedent directly: vocabulary extensions surface hidden
  findings, sequence before L-157 so they land in the worksheet, not as
  fresh Tier-1 noise. Verified this is a real, already-written
  precedent, not an invented one.
- **Naming collision, open:** `undetermined` (this design) and
  `UNCLASSIFIED` (its amended D2) are independently-converged, same
  design on two axes. Fable's lean: adopt `undetermined` in both, since
  this design ships first. Tony's call, not decided here.

## 18. Prompt for the builder

*(Unlike Sections 6/15, this is a BUILD prompt, not a design or review
prompt -- code gets written. Calibrated accordingly: more explicit
structure and named CRITICAL gates rather than trimmed-down judgment
calls, since a build's correctness depends on procedure firing
reliably, not on freeform reasoning. Suggested for a Sonnet-class
session (Section 17). Self-contained -- paste as the opening message,
attach this document.)*

> I'm working on the Paloma's Orrery project with Tony Quintanilla (PE,
> retired civil/environmental engineer, not a professional developer --
> builds this through AI collaboration, holds sole commit authority).
> Attached is a fully designed and reviewed handoff (L-163) retiring two
> hand-maintained module-classification dicts (`ROLE_MAP`,
> `MODULE_DOMAIN_MAP`) in favor of an explicit tag in each module's own
> docstring. Design by Sonnet 5, reviewed by Fable 5 against the
> adjacent provenance-scoring cluster it authored -- both confirmed
> build-ready.
>
> **This is a build session, four phases, strictly gated -- stop and
> report back after each phase rather than continuing through all four.**
> Read the attached handoff in full first; Section 17 is your phase
> breakdown and actual task list, Section 4 is the archive-candidate
> evidence, Section 16 is Fable's review (two amendments already folded
> into the Gap below -- don't re-litigate them). Then load
> `agentic-pre-test`, `safe-file-editing`, `ledger-and-session-records`,
> and `provenance-discipline` -- all four fire on this work.
>
> Pull both repos fresh and confirm the SHAs in "Built on" still match
> before building on anything load-bearing. If they don't, stop and flag
> the mismatch rather than assuming the handoff still describes current
> HEAD.
>
> **Phase 1 (archival, no code):** one item has no decided answer --
> `orrery_integration`'s disposition (Section 1). Ask Tony rather than
> guessing before closing this phase.
>
> **Phase 2 (content sweep, no code):** lock down the exact `Role:`/
> `Domain:` tag placement against the existing credit-line convention
> with Tony first -- the one open design question the handoff didn't
> resolve -- before running `add_docstrings.py` at scale. Preview mode
> first, written mode only after review.
>
> **Phase 3 (classifier code):** Mode 2 (agentic) for the new parser and
> report section; Mode 1 (targeted snippets) everywhere you're editing
> `module_atlas.py`'s existing functions. Map all three call sites
> (`module_atlas.py`, `provenance_scanner.py`, `dep_trace.py`) before
> touching any of them -- Check All Parallel Pipelines is a resident
> CRITICAL gate for exactly this shape of change. Full `agentic-pre-test`
> protocol before delivery, not `py_compile` alone. Credit line on every
> touched module: "Module updated: [Month Year] with Anthropic's Claude
> [model]."
>
> **Phase 4 (verify, then document):** only after Phase 3's code is
> actually running against the swept docstrings, confirmed against a
> real output, not assumed from the code reading -- update
> `ledger-and-session-records`' Codebase Tooling note and
> `provenance-discipline`'s role-driven-inclusion bullet (Section 13).
> Do NOT touch `provenance-discipline`'s "Report Domain Classification"
> section -- that edit belongs to a different build (the L-156 cluster's
> own Phase 3) and the mechanism it would describe doesn't exist yet.
> Bump both skills' version + source-SHA header lines.
>
> Leave the domain-code retirement, gallery `Domain:` tag consumption,
> and anything in the L-154 through L-162 cluster alone -- tracked
> separately, out of scope here.
>
> When you report back after each phase: lead with what actually
> happened -- files touched, what you verified and how -- not a
> narration of the plan you're about to execute.
>
> Deliverable per phase: a short as-built note (changed, verified, still
> open), pushed with the standard SHA round trip.

---

Session written July 2026 with Anthropic's Claude Sonnet 5.
