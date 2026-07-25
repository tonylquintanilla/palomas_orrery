Built on:
- orrery: dcfe207101bdbbb934f5fd02759e46d39df74a74 at https://github.com/tonylquintanilla/palomas_orrery
- gallery: 22c947c993a0d3e5f1aa9390288c28bcd2710275 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
- pushed at: [PHASE 2 CLOSE -- paste the new SHAs after committing the two add_docstrings.py copies]

Ledger handle: L-163
Phase: 2 of 4 -- Content sweep (docstrings only, no classifier code)
Session: Opus 5 builder session, July 25, 2026
Design: ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md (Sonnet 5), Fable 5 review
Section 16, Phase 0 reconciliation Section 19, Phase 1 as-built.

---

# L-163 Phase 2 -- As-Built

## Status: preview only. Nothing has been written to any module.

Both repos previewed clean. The write run is gated on Tony's review of
the classifications and the two flagged cases below.

## Changed

`add_docstrings.py` extended with a tag-insertion mode. Two copies, one
per repo, differing only in `SCAN_PATHS`:

- orrery copy: `SCAN_PATHS = ['.']`
- gallery copy: `SCAN_PATHS = ['tools', 'gallery/assembler',
  'gallery/assembler/harness', 'gallery/assembler/tests']`

The diff against HEAD is four hunks, all pure insertions -- every
pre-existing line survives byte-identical, including the entire 556-line
`DOCSTRINGS` table and all five original helper functions. The one
exception is `insert_docstring()`, deliberately rewritten to fix the two
known defects.

**Tony:** done

New in the file:

- `MODULE_TAGS` -- 136 entries (114 orrery + 22 gallery) keyed by
  repo-relative path, so both repos share one table with no collision
  risk and the two copies stay textually identical apart from
  `SCAN_PATHS`.
- `ROLE_VOCAB` / `DOMAIN_VOCAB` -- validation against the 12 role values
  and the 9 domain values (6 orrery + 3 gallery-specific). An
  out-of-vocabulary tag is reported, never written.
- `find_docstring_lines()` -- locates the docstring by `ast.parse`,
  replacing the old scan-for-the-first-triple-quote.
- `insert_tags()` -- inserts or refreshes the two-line block inside the
  existing docstring. Nothing outside the docstring is touched.
- `run_tag_sweep()` -- the `ledger_index.py` reporting pattern: a
  `problems` list plus a non-zero exit code, so a bad run cannot pass
  quietly in the VS Code panel.

**Defect fixes (both called for in the build prompt):**

- `has_leading_comment()` was defined and never called. It is now used:
  a module with no docstring gets one inserted BELOW its shebang and
  comment header, not above. Previously a docstring would have landed
  above `#!/usr/bin/env python3` and silently disabled it.
- `insert_docstring()` located the docstring by scanning for the first
  literal triple-quote; it now parses. The old scan could not tell a
  module docstring from a quoted string in a comment above it.

**Invocation:** preview is the default, so the sweep runs from VS Code's
Run button with no arguments. `--write` applies. The original
whole-docstring mode still works, moved behind `--docstrings`, so the
`DOCSTRINGS` table remains usable for new modules.

## Verified

- **Preview, orrery:** 114 modules, 114 tag blocks, zero problems.
- **Preview, gallery:** 22 modules, 22 tag blocks, zero problems.
  `__init__.py` files exempt per design Section 3; the three of them are
  correctly absent from both the table and the scan.
- **Write run in a sandbox** (throwaway clones at the pinned SHAs, never
  the deliverable): all 136 modules re-parse, every one carries exactly
  one `Role:` and one `Domain:` line, `compileall` clean across both
  repos.
- **Idempotent.** A second write run produces byte-identical files in
  both repos. This did not hold on the first implementation -- removing
  an existing block left its two blank separators adjacent, so each run
  grew the docstring by one blank line. Caught by running the sweep
  twice rather than once; fixed by collapsing that one seam.
- **Encoding preserved.** No file changed line endings and no file
  changed its non-ASCII byte count.
- **agentic-pre-test:** `py_compile` on both deliverable copies, then
  `palomas_orrery.py` launched under `xvfb` from the fully-swept sandbox
  on a throwaway copy with the `SystemButtonFace` swap. It reached GUI
  init and center-body registration cleanly. Throwaway deleted; the
  deliverable was never edited by the test.

## Finding: the codebase is not uniformly LF

21 of the 114 orrery root modules are CRLF; the gallery is entirely LF.
Per-file line-ending detection is therefore load-bearing, not
belt-and-braces. `add_docstrings.py` already did this correctly and that
behavior is preserved unchanged. Worth knowing before any future sweep
normalizes endings by accident:

`catalog_selection`, `create_cache_backups`, `data_acquisition`,
`data_acquisition_distance`, `data_processing`, `formatting_utils`,
`hr_diagram_apparent_magnitude`, `hr_diagram_distance`,
`messier_object_data_handler`, `object_type_analyzer`,
`planetarium_apparent_magnitude`, `planetarium_distance`,
`report_manager`, `shutdown_handler`, `star_notes`, `star_properties`,
`stellar_data_patches`, `stellar_parameters`, `visualization_2d`,
`visualization_3d`, `visualization_core`.

## Tony-action (decide): 8 changelog docstrings

Eight modules carry more than one `Module updated:` line -- a changelog
of several entries inside one docstring. For these, "directly above the
credit line" does not name a single place. The sweep anchors on the LAST
credit line and flags each one in a REVIEW block rather than resolving it
silently.

Orrery: `apsidal_markers` (4 entries), `planet_visualization_utilities`
(4), `earth_system_controller` (2), `idealized_orbits` (2),
`planet_visualization` (2), `visualization_utils` (2).
Gallery: `tools/gallery_studio` (3), `tools/gallery_cache_builder` (3).

Anchoring on the last entry puts the tag block between the
second-to-last and last changelog entries. It is a faithful reading of
the decided rule, but it reads oddly -- in `apsidal_markers.py` the tags
land between the May 2 and May 8 entries. The alternative is to treat a
changelog docstring as a no-credit-line case and put the block at the
very end, after the whole history. That is cleaner to read but puts the
tags below the last credit line rather than above it. This is a real
choice the placement decision did not anticipate; it is yours.

**Tony:** put the credit after the doc string

## Tony-action (decide): 50 classifications made this session

Everything else was migrated from the existing dicts. These are new
judgment calls and are the substance of what needs reviewing.

**Orrery roles (12) -- no `ROLE_MAP` entry existed:**

| Module | Role | Reasoning |
|---|---|---|
| `data_inventory` | devtool | Walks data stores, emits a report. |
| `earth_system_common` | utility | Its own docstring: shared engine-agnostic helpers. |
| `export_orbit_cache` | devtool | Its own docstring calls it a desktop devtool. |
| `food_insecurity_generator` | computation | Matches `earth_system_generator`, the existing peer generator. | -- the generators are dev tools because the developer uses them to produce the visualization files
| `ledger_index` | devtool | |
| `measure_animation_html` | devtool | |
| `measure_perframe_elements` | devtool | |
| `orrery_rendering` | rendering | Sphere shell builder + info marker factory. |
| `scenarios_food_insecurity` | scenario | Matches the three existing `scenarios_*` peers. |
| `shell_configs` | data | Two configuration registries, no behavior. |
| `skills_index` | devtool | |
| `test_reset_completeness` | devtool | Matches `test_orbit_cache`, `verify_orbit_cache`. | -- is this a one time tool or persistent?

**Orrery domains (16) -- no `MODULE_DOMAIN_MAP` entry existed:** -- okay
`catalog_selection`, `data_processing`, `incremental_cache_manager`,
`star_visualization_gui`, `vot_cache_manager` -> `stars`;

`earth_system_common`, `earth_system_controller`,
`earth_system_visualization_gui`, `scenarios_food_insecurity` ->
`earth_science`; 

`orbital_param_viz`, `orrery_rendering`,
`palomas_orrery_helpers`, `planet_visualization`, `shell_configs` ->
`orrery`;

 `shutdown_handler` -> `utilities`;
 
  `measure_animation_html` ->
`dev_tools`.

**Gallery roles (22) -- no prior classification existed at all.** Domains
come straight from design Section 11. -- okay except as noted

GUI tools `gallery_studio` and
`gallery_editor` -> `gui`; -- i think these are better under dev tools

`json_converter`, `gallery_json_fixer`, -- dev tools
and
the assembler's `assemble` -> `pipeline`;  -- okay

`gallery_cache_builder` and
`cache_reader` -> `cache`; 

`catalog` and `models` -> `data`; 

`errors` ->
`utility` (design Section 3 explicitly puts `errors.py`-style modules
there); 

`resolver` -> `computation`; 

the four `render_*` modules and
`presentation` -> `rendering`; 

`gallery_cleanup`, `debug_encke_tp`,
`inspect_staging`, `test_gallery_cache_builder_offline`,
`harness/fingerprint`, `tests/test_artifact1_earth` -> `devtool`.

**15 more made explicit rather than inferred:** the `*_visualization_
shells` modules previously got `rendering/shells` from the filename
heuristic. They now carry it as a written tag, which is the point of the
redesign -- design Section 3 keeps heuristics as suggestion-only.

## Also found, not acted on

- **`MODULE_DOMAIN_MAP` carries 2 ghosts.** `smoke_dipole_cone` and
  `smoke_rotation_axis` were archived in Phase 1, and their `ROLE_MAP`
  entries went with them, but their `MODULE_DOMAIN_MAP` entries in
  `provenance_scanner.py` survive. Not touched: the build prompt puts
  domain-code changes out of scope, and `provenance_scanner.py` is a
  Phase 3 call site. Flagged so the later build does not inherit them
  silently.

- **Two domain assignments worth a second look.** `data_acquisition` and
  `data_acquisition_distance` are mapped `orrery` in the existing
  `MODULE_DOMAIN_MAP`, but both fetch star catalog data and sit in the
  same pipeline as `catalog_selection` and `data_processing`, which this
  session put in `stars`. Existing values were migrated unchanged rather
  than silently re-classified. If they are wrong, Phase 2's write run is
  the cheap moment to fix them. -- move to stars

- **Three single-line docstrings** (`data_acquisition_distance`,
  `formatting_utils`, `planetarium_apparent_magnitude`) are expanded to
  the multi-line form so the block lands consistently. The original text
  is preserved verbatim on the opening line.

## Still open

**Tony-action (do):** commit both `add_docstrings.py` copies and push;
record the SHAs in this note's anchor. -- done

**Tony-action (decide):** the changelog-docstring placement, the 50 new
classifications, and the two `data_acquisition*` domains above. -- done as noted

**Tony-action (do):** run the preview yourself in both repos from the VS
Code Run button and read the output against the three docstring shapes
the build prompt names -- credit line present, credit line absent,
shebang-first. Representative results after a sandbox write run:

```
credit present   Key functions:
                     select_stars() - ...

                 Role: computation
                 Domain: stars

                 Module updated: April 2026 with Anthropic's Claude Opus 4.6
                 """

credit absent    ... prose ...

                 Role: utility
                 Domain: assembler
                 """

shebang-first    #!/usr/bin/env python3
                 """
                 ledger_index.py - Generate the at-a-glance INDEX ...
```

**Gate:** Phase 3 is gated on the write run actually completing, not on
this preview. The classifier has nothing to read until the tags exist in
the files.

## Ref

`add_docstrings.py`, `module_atlas.py`, `provenance_scanner.py`
(`MODULE_DOMAIN_MAP`), `ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md`
(Sections 3, 8, 10, 11, 17), `AS_BUILT_L163_phase1.md`,
`LEDGER_CONSOLIDATED.md` (L-163), `ledger_index.py` (the reporting
pattern this follows).

---

Session written July 2026 with Anthropic's Claude Opus 5.
