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
| `test_reset_completeness` | devtool | Matches `test_orbit_cache`, `verify_orbit_cache`. | 

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

**Tony:** orrery docstring output:

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
  Scan paths: .
==============================================================

  ADDED    add_docstrings.py                                devtool / dev_tools
  ADDED    apsidal_markers.py                               computation / orrery
  ADDED    asteroid_belt_visualization_shells.py            rendering/shells / orrery
  ADDED    catalog_selection.py                             computation / stars
  ADDED    celestial_coordinates.py                         computation / orrery
  ADDED    celestial_objects.py                             data / orrery
  ADDED    climate_cache_manager.py                         cache / earth_science
  ADDED    close_approach_data.py                           data / orrery
  ADDED    comet_visualization_shells.py                    rendering/shells / orrery
  ADDED    constants_new.py                                 data / orrery
  ADDED    convert_hot_ph_to_json.py                        devtool / dev_tools
  ADDED    coordinate_system_guide.py                       computation / orrery
  ADDED    create_cache_backups.py                          devtool / dev_tools
  ADDED    create_ephemeris_database.py                     devtool / dev_tools
  ADDED    data_acquisition.py                              computation / orrery
  ADDED    data_acquisition_distance.py                     computation / orrery
  ADDED    data_inventory.py                                devtool / dev_tools
  ADDED    data_processing.py                               computation / stars
  ADDED    dep_trace.py                                     devtool / dev_tools
  ADDED    diagnose_bcodmo.py                               devtool / dev_tools
  ADDED    earth_system_common.py                           utility / earth_science
  ADDED    earth_system_controller.py                       gui / earth_science
  ADDED    earth_system_generator.py                        computation / earth_science -- should be dev tool
  ADDED    earth_system_visualization_gui.py                gui / earth_science
  ADDED    earth_visualization_shells.py                    rendering/shells / earth_science
  ADDED    energy_imbalance.py                              computation / earth_science
  ADDED    eris_visualization_shells.py                     rendering/shells / orrery
  ADDED    examine_hot_csv.py                               devtool / dev_tools
  ADDED    exoplanet_coordinates.py                         data / stars
  ADDED    exoplanet_orbits.py                              rendering / stars
  ADDED    exoplanet_stellar_properties.py                  data / stars
  ADDED    exoplanet_systems.py                             data / stars
  ADDED    export_orbit_cache.py                            devtool / dev_tools
  ADDED    fetch_climate_data.py                            computation / earth_science
  ADDED    fetch_paleoclimate_data.py                       computation / earth_science
  ADDED    food_insecurity_generator.py                     computation / earth_science -- should be dev tool
  ADDED    formatting_utils.py                              utility / utilities
  ADDED    hr_diagram_apparent_magnitude.py                 rendering / stars
  ADDED    hr_diagram_distance.py                           rendering / stars
  ADDED    idealized_orbits.py                              computation / orrery
  ADDED    incremental_cache_manager.py                     cache / stars
  ADDED    info_dictionary.py                               data / orrery
  ADDED    jupiter_visualization_shells.py                  rendering/shells / orrery
  ADDED    ledger_index.py                                  devtool / dev_tools
  ADDED    mars_visualization_shells.py                     rendering/shells / orrery
  ADDED    measure_animation_html.py                        devtool / dev_tools
  ADDED    measure_perframe_elements.py                     devtool / dev_tools
  ADDED    mercury_visualization_shells.py                  rendering/shells / orrery
  ADDED    messier_catalog.py                               data / stars
  ADDED    messier_object_data_handler.py                   pipeline / stars
  ADDED    module_atlas.py                                  devtool / dev_tools
  ADDED    moon_visualization_shells.py                     rendering/shells / orrery
  ADDED    neptune_visualization_shells.py                  rendering/shells / orrery
  ADDED    object_type_analyzer.py                          computation / orrery
  ADDED    orbit_data_manager.py                            cache / orrery
  ADDED    orbital_elements.py                              computation / orrery
  ADDED    orbital_param_viz.py                             gui / orrery
  ADDED    orrery_rendering.py                              rendering / orrery
  ADDED    osculating_cache_manager.py                      cache / orrery
  ADDED    paleoclimate_dual_scale.py                       rendering / earth_science
  ADDED    paleoclimate_human_origins_full.py               rendering / earth_science
  ADDED    paleoclimate_visualization.py                    rendering / earth_science
  ADDED    paleoclimate_visualization_full.py               rendering / earth_science
  ADDED    paleoclimate_wet_bulb_full.py                    rendering / earth_science
  ADDED    palomas_orrery.py                                gui / orrery
  ADDED    palomas_orrery_dashboard.py                      gui / orrery
  ADDED    palomas_orrery_helpers.py                        utility / orrery
  ADDED    planet9_visualization_shells.py                  rendering/shells / orrery
  ADDED    planet_visualization.py                          rendering / orrery
  ADDED    planet_visualization_utilities.py                rendering / orrery
  ADDED    planetarium_apparent_magnitude.py                rendering / stars
  ADDED    planetarium_distance.py                          rendering / stars
  ADDED    plot_data_exchange.py                            pipeline / utilities
  ADDED    plot_data_report_widget.py                       rendering / utilities
  ADDED    pluto_visualization_shells.py                    rendering/shells / orrery
  ADDED    provenance_scanner.py                            devtool / dev_tools
  ADDED    report_manager.py                                utility / utilities
  ADDED    saturn_visualization_shells.py                   rendering/shells / orrery
  ADDED    save_utils.py                                    pipeline / utilities
  ADDED    scenarios_coral_bleaching.py                     scenario / earth_science
  ADDED    scenarios_food_insecurity.py                     scenario / earth_science
  ADDED    scenarios_heatwaves.py                           scenario / earth_science
  ADDED    scenarios_western_heatwave_march_2026.py         scenario / earth_science
  ADDED    sgr_a_grand_tour.py                              rendering / orrery
  ADDED    sgr_a_star_data.py                               data / orrery
  ADDED    sgr_a_visualization_animation.py                 rendering / orrery
  ADDED    sgr_a_visualization_core.py                      rendering / orrery
  ADDED    sgr_a_visualization_core_arcs.py                 pipeline / orrery
  ADDED    sgr_a_visualization_precession.py                rendering / orrery
  ADDED    shared_utilities.py                              utility / utilities
  ADDED    shell_configs.py                                 data / orrery
  ADDED    shutdown_handler.py                              utility / utilities
  ADDED    simbad_manager.py                                computation / stars
  ADDED    skills_index.py                                  devtool / dev_tools
  ADDED    social_media_export.py                           pipeline / gallery
  ADDED    solar_visualization_shells.py                    rendering/shells / orrery
  ADDED    spacecraft_encounters.py                         data / orrery
  ADDED    star_notes.py                                    data / stars
  ADDED    star_properties.py                               data / stars
  ADDED    star_sphere_builder.py                           rendering / stars
  ADDED    star_visualization_gui.py                        gui / stars
  ADDED    stellar_data_patches.py                          data / stars
  ADDED    stellar_parameters.py                            data / stars
  ADDED    test_constants_provenance.py                     devtool / dev_tools
  ADDED    test_orbit_cache.py                              devtool / dev_tools
  ADDED    test_reset_completeness.py                       devtool / dev_tools
  ADDED    uranus_visualization_shells.py                   rendering/shells / orrery
  ADDED    venus_visualization_shells.py                    rendering/shells / orrery
  ADDED    verify_orbit_cache.py                            devtool / dev_tools
  ADDED    visualization_2d.py                              rendering / stars
  ADDED    visualization_3d.py                              rendering / stars
  ADDED    visualization_core.py                            rendering / stars
  ADDED    visualization_utils.py                           rendering / stars
  ADDED    vot_cache_manager.py                             cache / stars

--------------------------------------------------------------
  added        114
  total        114

  REVIEW (6) -- more than one credit line, so "above the
  credit line" is ambiguous. Anchored on the LAST one;
  confirm that reads right before any write run:
    - apsidal_markers.py: 4 credit lines (changelog docstring)
    - earth_system_controller.py: 2 credit lines (changelog docstring)
    - idealized_orbits.py: 2 credit lines (changelog docstring)
    - planet_visualization.py: 2 credit lines (changelog docstring)
    - planet_visualization_utilities.py: 4 credit lines (changelog docstring)
    - visualization_utils.py: 2 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

**Tony:** gallery docstring output:

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
  Scan paths: tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  ADDED    tools/debug_encke_tp.py                          devtool / dev_tools
  ADDED    tools/gallery_cache_builder.py                   cache / cache_builder
  ADDED    tools/gallery_cleanup.py                         devtool / cache_builder
  ADDED    tools/gallery_editor.py                          gui / gallery_pipeline
  ADDED    tools/gallery_json_fixer.py                      pipeline / gallery_pipeline
  ADDED    tools/gallery_studio.py                          gui / gallery_pipeline
  ADDED    tools/inspect_staging.py                         devtool / dev_tools
  ADDED    tools/json_converter.py                          pipeline / gallery_pipeline
  ADDED    tools/test_gallery_cache_builder_offline.py      devtool / dev_tools
  ADDED    gallery/assembler/assemble.py                    pipeline / assembler
  ADDED    gallery/assembler/cache_reader.py                cache / assembler
  ADDED    gallery/assembler/catalog.py                     data / assembler
  ADDED    gallery/assembler/errors.py                      utility / assembler
  ADDED    gallery/assembler/models.py                      data / assembler
  ADDED    gallery/assembler/presentation.py                rendering / assembler
  ADDED    gallery/assembler/render_events.py               rendering / assembler
  ADDED    gallery/assembler/render_objects.py              rendering / assembler
  ADDED    gallery/assembler/render_orbits.py               rendering / assembler
  ADDED    gallery/assembler/render_spacecraft.py           rendering / assembler
  ADDED    gallery/assembler/resolver.py                    computation / assembler
  ADDED    gallery/assembler/harness/fingerprint.py         devtool / dev_tools
  ADDED    gallery/assembler/tests/test_artifact1_earth.py  devtool / dev_tools

--------------------------------------------------------------
  added        22
  total        22

  REVIEW (2) -- more than one credit line, so "above the
  credit line" is ambiguous. Anchored on the LAST one;
  confirm that reads right before any write run:
    - tools/gallery_cache_builder.py: 3 credit lines (changelog docstring)
    - tools/gallery_studio.py: 3 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

**Claude:**
Now the rest of your notes — mostly good, two things need a call:

done appears twice in your notes (once right after the diff description, once at the bottom for "commit and push"). Not a problem, just flagging in case one was a stray paste. Either way — confirmed, both repos did get pushed.

test_reset_completeness.py — checked it directly: it's a standing regression guard ("if a future shell/toggle family is added and Reset misses it, this fails loudly"), meant to be re-run any time the GUI changes, not a one-off. Same pattern as its peers test_orbit_cache.py and verify_orbit_cache.py. So: persistent, and devtool is right regardless — there's no separate "one-time" role in the vocabulary anyway.

Generators as devtools — this one needs a decision. Your note says generators should be devtool "because the developer uses them to produce the visualization files." That reasoning would also apply to earth_system_generator.py — the existing, already-migrated peer that food_insecurity_generator was matched against — which is currently computation, not devtool. If the principle is right, both should probably move together; if only food_insecurity_generator changes, the two peers end up classified differently for the same job. Which do you want: both to devtool, or leave both as computation and drop this one? -- **Tony:** both should be dev tools as noted

Gallery gui → devtool for gallery_studio/gallery_editor, and pipeline → devtool for json_converter/gallery_json_fixer — no conflict with the design (that only fixed domains, not roles, for these four). Worth noticing: with this change, no .py file in the gallery repo carries the gui role at all — everything there is developer-facing tooling, none of it is what an actual gallery visitor sees. If that's the intent, this is consistent; just flagging so it's a deliberate choice, not a side effect. -- **Tony:** that is correct. the gallery repo is all dev tooling. no user gui.

The "put the credit after the doc string" note — I read this as: for the 8 changelog files, put the Role:/Domain: block at the very end of the docstring, after all the history, rather than wedging it between entries (the option I'd also leaned toward). If that's right, no action needed — just confirm, since this is the one note I couldn't parse with full confidence.

Everything else — data_acquisition* → stars, the 16 domain assignments, the rest of the gallery roles, the ghost MODULE_DOMAIN_MAP entries left alone — all consistent, no issues.

Two small extras, not urgent: the commit also added documentation/prompt_to_opus_5_for_module_atlas_refactor.md — that's just your saved copy of the Phase 2-4 prompt I wrote earlier, nothing new. And there are two stray 0-byte files at the gallery repo root, cd and git — harmless clutter, worth deleting whenever you're in there next. -- **Tony:** removed; what does CNAME do? 

Once the gallery file is moved and both previews check out, and you've settled the generators question, you're clear to run the real write.

**Tony:**

gallery write:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
  Scan paths: tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  SAME     tools/debug_encke_tp.py                         
  SAME     tools/gallery_cache_builder.py                  
  SAME     tools/gallery_cleanup.py                        
  UPDATED  tools/gallery_editor.py                          devtool / gallery_pipeline
  UPDATED  tools/gallery_json_fixer.py                      devtool / gallery_pipeline
  UPDATED  tools/gallery_studio.py                          devtool / gallery_pipeline
  SAME     tools/inspect_staging.py                        
  UPDATED  tools/json_converter.py                          devtool / gallery_pipeline
  SAME     tools/test_gallery_cache_builder_offline.py     
  SAME     gallery/assembler/assemble.py                   
  SAME     gallery/assembler/cache_reader.py               
  SAME     gallery/assembler/catalog.py                    
  SAME     gallery/assembler/errors.py                     
  SAME     gallery/assembler/models.py                     
  SAME     gallery/assembler/presentation.py               
  SAME     gallery/assembler/render_events.py              
  SAME     gallery/assembler/render_objects.py             
  SAME     gallery/assembler/render_orbits.py              
  SAME     gallery/assembler/render_spacecraft.py          
  SAME     gallery/assembler/resolver.py                   
  SAME     gallery/assembler/harness/fingerprint.py        
  SAME     gallery/assembler/tests/test_artifact1_earth.py 

--------------------------------------------------------------
  unchanged    18
  updated      4
  total        22

  CHANGELOG (2) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - tools/gallery_cache_builder.py: 3 credit lines (changelog docstring)
    - tools/gallery_studio.py: 3 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.


  Write these changes? [y/n]: y


==============================================================
  Role / Domain Tag Sweep -- WRITING
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
  Scan paths: tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  SAME     tools/debug_encke_tp.py                         
  SAME     tools/gallery_cache_builder.py                  
  SAME     tools/gallery_cleanup.py                        
  UPDATED  tools/gallery_editor.py                          devtool / gallery_pipeline
  UPDATED  tools/gallery_json_fixer.py                      devtool / gallery_pipeline
  UPDATED  tools/gallery_studio.py                          devtool / gallery_pipeline
  SAME     tools/inspect_staging.py                        
  UPDATED  tools/json_converter.py                          devtool / gallery_pipeline
  SAME     tools/test_gallery_cache_builder_offline.py     
  SAME     gallery/assembler/assemble.py                   
  SAME     gallery/assembler/cache_reader.py               
  SAME     gallery/assembler/catalog.py                    
  SAME     gallery/assembler/errors.py                     
  SAME     gallery/assembler/models.py                     
  SAME     gallery/assembler/presentation.py               
  SAME     gallery/assembler/render_events.py              
  SAME     gallery/assembler/render_objects.py             
  SAME     gallery/assembler/render_orbits.py              
  SAME     gallery/assembler/render_spacecraft.py          
  SAME     gallery/assembler/resolver.py                   
  SAME     gallery/assembler/harness/fingerprint.py        
  SAME     gallery/assembler/tests/test_artifact1_earth.py 

--------------------------------------------------------------
  unchanged    18
  updated      4
  total        22

  CHANGELOG (2) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - tools/gallery_cache_builder.py: 3 credit lines (changelog docstring)
    - tools/gallery_studio.py: 3 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

**Tony:**
orrery write: 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
  Scan paths: .
==============================================================

  ADDED    add_docstrings.py                                devtool / dev_tools
  SAME     apsidal_markers.py                              
  SAME     asteroid_belt_visualization_shells.py           
  SAME     catalog_selection.py                            
  SAME     celestial_coordinates.py                        
  SAME     celestial_objects.py                            
  SAME     climate_cache_manager.py                        
  SAME     close_approach_data.py                          
  SAME     comet_visualization_shells.py                   
  SAME     constants_new.py                                
  SAME     convert_hot_ph_to_json.py                       
  SAME     coordinate_system_guide.py                      
  SAME     create_cache_backups.py                         
  SAME     create_ephemeris_database.py                    
  UPDATED  data_acquisition.py                              computation / stars
  UPDATED  data_acquisition_distance.py                     computation / stars
  SAME     data_inventory.py                               
  SAME     data_processing.py                              
  SAME     dep_trace.py                                    
  SAME     diagnose_bcodmo.py                              
  SAME     earth_system_common.py                          
  SAME     earth_system_controller.py                      
  SAME     earth_system_generator.py                       
  SAME     earth_system_visualization_gui.py               
  SAME     earth_visualization_shells.py                   
  SAME     energy_imbalance.py                             
  SAME     eris_visualization_shells.py                    
  SAME     examine_hot_csv.py                              
  SAME     exoplanet_coordinates.py                        
  SAME     exoplanet_orbits.py                             
  SAME     exoplanet_stellar_properties.py                 
  SAME     exoplanet_systems.py                            
  SAME     export_orbit_cache.py                           
  SAME     fetch_climate_data.py                           
  SAME     fetch_paleoclimate_data.py                      
  SAME     food_insecurity_generator.py                    
  SAME     formatting_utils.py                             
  SAME     hr_diagram_apparent_magnitude.py                
  SAME     hr_diagram_distance.py                          
  SAME     idealized_orbits.py                             
  SAME     incremental_cache_manager.py                    
  SAME     info_dictionary.py                              
  SAME     jupiter_visualization_shells.py                 
  SAME     ledger_index.py                                 
  SAME     mars_visualization_shells.py                    
  SAME     measure_animation_html.py                       
  SAME     measure_perframe_elements.py                    
  SAME     mercury_visualization_shells.py                 
  SAME     messier_catalog.py                              
  SAME     messier_object_data_handler.py                  
  SAME     module_atlas.py                                 
  SAME     moon_visualization_shells.py                    
  SAME     neptune_visualization_shells.py                 
  SAME     object_type_analyzer.py                         
  SAME     orbit_data_manager.py                           
  SAME     orbital_elements.py                             
  SAME     orbital_param_viz.py                            
  SAME     orrery_rendering.py                             
  SAME     osculating_cache_manager.py                     
  SAME     paleoclimate_dual_scale.py                      
  SAME     paleoclimate_human_origins_full.py              
  SAME     paleoclimate_visualization.py                   
  SAME     paleoclimate_visualization_full.py              
  SAME     paleoclimate_wet_bulb_full.py                   
  SAME     palomas_orrery.py                               
  SAME     palomas_orrery_dashboard.py                     
  SAME     palomas_orrery_helpers.py                       
  SAME     planet9_visualization_shells.py                 
  SAME     planet_visualization.py                         
  SAME     planet_visualization_utilities.py               
  SAME     planetarium_apparent_magnitude.py               
  SAME     planetarium_distance.py                         
  SAME     plot_data_exchange.py                           
  SAME     plot_data_report_widget.py                      
  SAME     pluto_visualization_shells.py                   
  SAME     provenance_scanner.py                           
  SAME     report_manager.py                               
  SAME     saturn_visualization_shells.py                  
  SAME     save_utils.py                                   
  SAME     scenarios_coral_bleaching.py                    
  SAME     scenarios_food_insecurity.py                    
  SAME     scenarios_heatwaves.py                          
  SAME     scenarios_western_heatwave_march_2026.py        
  SAME     sgr_a_grand_tour.py                             
  SAME     sgr_a_star_data.py                              
  SAME     sgr_a_visualization_animation.py                
  SAME     sgr_a_visualization_core.py                     
  SAME     sgr_a_visualization_core_arcs.py                
  SAME     sgr_a_visualization_precession.py               
  SAME     shared_utilities.py                             
  SAME     shell_configs.py                                
  SAME     shutdown_handler.py                             
  SAME     simbad_manager.py                               
  SAME     skills_index.py                                 
  SAME     social_media_export.py                          
  SAME     solar_visualization_shells.py                   
  SAME     spacecraft_encounters.py                        
  SAME     star_notes.py                                   
  SAME     star_properties.py                              
  SAME     star_sphere_builder.py                          
  SAME     star_visualization_gui.py                       
  SAME     stellar_data_patches.py                         
  SAME     stellar_parameters.py                           
  SAME     test_constants_provenance.py                    
  SAME     test_orbit_cache.py                             
  SAME     test_reset_completeness.py                      
  SAME     uranus_visualization_shells.py                  
  SAME     venus_visualization_shells.py                   
  SAME     verify_orbit_cache.py                           
  SAME     visualization_2d.py                             
  SAME     visualization_3d.py                             
  SAME     visualization_core.py                           
  SAME     visualization_utils.py                          
  SAME     vot_cache_manager.py                            

--------------------------------------------------------------
  added        1
  unchanged    111
  updated      2
  total        114

  CHANGELOG (6) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - apsidal_markers.py: 4 credit lines (changelog docstring)
    - earth_system_controller.py: 2 credit lines (changelog docstring)
    - idealized_orbits.py: 2 credit lines (changelog docstring)
    - planet_visualization.py: 2 credit lines (changelog docstring)
    - planet_visualization_utilities.py: 4 credit lines (changelog docstring)
    - visualization_utils.py: 2 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.


  Write these changes? [y/n]: y


==============================================================
  Role / Domain Tag Sweep -- WRITING
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
  Scan paths: .
==============================================================

  ADDED    add_docstrings.py                                devtool / dev_tools
  SAME     apsidal_markers.py                              
  SAME     asteroid_belt_visualization_shells.py           
  SAME     catalog_selection.py                            
  SAME     celestial_coordinates.py                        
  SAME     celestial_objects.py                            
  SAME     climate_cache_manager.py                        
  SAME     close_approach_data.py                          
  SAME     comet_visualization_shells.py                   
  SAME     constants_new.py                                
  SAME     convert_hot_ph_to_json.py                       
  SAME     coordinate_system_guide.py                      
  SAME     create_cache_backups.py                         
  SAME     create_ephemeris_database.py                    
  UPDATED  data_acquisition.py                              computation / stars
  UPDATED  data_acquisition_distance.py                     computation / stars
  SAME     data_inventory.py                               
  SAME     data_processing.py                              
  SAME     dep_trace.py                                    
  SAME     diagnose_bcodmo.py                              
  SAME     earth_system_common.py                          
  SAME     earth_system_controller.py                      
  SAME     earth_system_generator.py                       
  SAME     earth_system_visualization_gui.py               
  SAME     earth_visualization_shells.py                   
  SAME     energy_imbalance.py                             
  SAME     eris_visualization_shells.py                    
  SAME     examine_hot_csv.py                              
  SAME     exoplanet_coordinates.py                        
  SAME     exoplanet_orbits.py                             
  SAME     exoplanet_stellar_properties.py                 
  SAME     exoplanet_systems.py                            
  SAME     export_orbit_cache.py                           
  SAME     fetch_climate_data.py                           
  SAME     fetch_paleoclimate_data.py                      
  SAME     food_insecurity_generator.py                    
  SAME     formatting_utils.py                             
  SAME     hr_diagram_apparent_magnitude.py                
  SAME     hr_diagram_distance.py                          
  SAME     idealized_orbits.py                             
  SAME     incremental_cache_manager.py                    
  SAME     info_dictionary.py                              
  SAME     jupiter_visualization_shells.py                 
  SAME     ledger_index.py                                 
  SAME     mars_visualization_shells.py                    
  SAME     measure_animation_html.py                       
  SAME     measure_perframe_elements.py                    
  SAME     mercury_visualization_shells.py                 
  SAME     messier_catalog.py                              
  SAME     messier_object_data_handler.py                  
  SAME     module_atlas.py                                 
  SAME     moon_visualization_shells.py                    
  SAME     neptune_visualization_shells.py                 
  SAME     object_type_analyzer.py                         
  SAME     orbit_data_manager.py                           
  SAME     orbital_elements.py                             
  SAME     orbital_param_viz.py                            
  SAME     orrery_rendering.py                             
  SAME     osculating_cache_manager.py                     
  SAME     paleoclimate_dual_scale.py                      
  SAME     paleoclimate_human_origins_full.py              
  SAME     paleoclimate_visualization.py                   
  SAME     paleoclimate_visualization_full.py              
  SAME     paleoclimate_wet_bulb_full.py                   
  SAME     palomas_orrery.py                               
  SAME     palomas_orrery_dashboard.py                     
  SAME     palomas_orrery_helpers.py                       
  SAME     planet9_visualization_shells.py                 
  SAME     planet_visualization.py                         
  SAME     planet_visualization_utilities.py               
  SAME     planetarium_apparent_magnitude.py               
  SAME     planetarium_distance.py                         
  SAME     plot_data_exchange.py                           
  SAME     plot_data_report_widget.py                      
  SAME     pluto_visualization_shells.py                   
  SAME     provenance_scanner.py                           
  SAME     report_manager.py                               
  SAME     saturn_visualization_shells.py                  
  SAME     save_utils.py                                   
  SAME     scenarios_coral_bleaching.py                    
  SAME     scenarios_food_insecurity.py                    
  SAME     scenarios_heatwaves.py                          
  SAME     scenarios_western_heatwave_march_2026.py        
  SAME     sgr_a_grand_tour.py                             
  SAME     sgr_a_star_data.py                              
  SAME     sgr_a_visualization_animation.py                
  SAME     sgr_a_visualization_core.py                     
  SAME     sgr_a_visualization_core_arcs.py                
  SAME     sgr_a_visualization_precession.py               
  SAME     shared_utilities.py                             
  SAME     shell_configs.py                                
  SAME     shutdown_handler.py                             
  SAME     simbad_manager.py                               
  SAME     skills_index.py                                 
  SAME     social_media_export.py                          
  SAME     solar_visualization_shells.py                   
  SAME     spacecraft_encounters.py                        
  SAME     star_notes.py                                   
  SAME     star_properties.py                              
  SAME     star_sphere_builder.py                          
  SAME     star_visualization_gui.py                       
  SAME     stellar_data_patches.py                         
  SAME     stellar_parameters.py                           
  SAME     test_constants_provenance.py                    
  SAME     test_orbit_cache.py                             
  SAME     test_reset_completeness.py                      
  SAME     uranus_visualization_shells.py                  
  SAME     venus_visualization_shells.py                   
  SAME     verify_orbit_cache.py                           
  SAME     visualization_2d.py                             
  SAME     visualization_3d.py                             
  SAME     visualization_core.py                           
  SAME     visualization_utils.py                          
  SAME     vot_cache_manager.py                            

--------------------------------------------------------------
  added        1
  unchanged    111
  updated      2
  total        114

  CHANGELOG (6) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - apsidal_markers.py: 4 credit lines (changelog docstring)
    - earth_system_controller.py: 2 credit lines (changelog docstring)
    - idealized_orbits.py: 2 credit lines (changelog docstring)
    - planet_visualization.py: 2 credit lines (changelog docstring)
    - planet_visualization_utilities.py: 4 credit lines (changelog docstring)
    - visualization_utils.py: 2 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

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
