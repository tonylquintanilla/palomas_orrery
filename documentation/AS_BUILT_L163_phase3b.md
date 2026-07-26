Built on:
- orrery: c53ec70807f0dde83c584100facc416ae5c5d39e at https://github.com/tonylquintanilla/palomas_orrery
- gallery: 4a129af370e4d2d5c7b3995185caa6226b6df5bc at https://github.com/tonylquintanilla/tonyquintanilla.github.io
- pushed at: [PHASE 3B CLOSE -- paste both SHAs after committing]

Ledger handle: L-163
Phase: 3b of 4 -- The classifier code
Session: Opus 5 builder session, July 26, 2026

---

# L-163 Phase 3b -- As-Built

Rebuilt from the fixed base, not salvaged from the contaminated tree.

## Changed -- 7 files

**orrery/module_atlas.py** (743 -> 1073 lines)
- New tag-parser section: `parse_module_tags()` via `ast.get_docstring()`,
  `classify_module()` returning `(role, domain, source)`, plus
  `resolve_module_path()` and `set_tag_source_dir()` so a name-only
  caller still works.
- `classify_role(module_name, filepath=None)` -- reads the tag. Old
  filename heuristic removed; an unrecognized or missing tag is
  `undetermined`, never guessed. New `classify_domain()` alongside it.
- `ROLE_MAP` wrapped in a `# ROLE-MAP:START/END` marker zone and
  regenerated from the tags each run, mirroring `ledger_index.py`.
- `UNDETERMINED` added to all three role-keyed structures, with a module-
  level assert that they never drift apart again.
- `SCAN_PATHS` multi-path discovery via `iter_module_files()`, with
  collision reporting.
- `classification_report_lines()` writes a Classification Coverage
  section into both MODULE_ATLAS.md and MODULE_INDEX.md.

**orrery/dep_trace.py** -- fallback cascade removed entirely: the
duplicated `_shells` heuristic, the silent `'other'` default, and the
unreachable `elif mod in ROLE_MAP` branch. An unimportable atlas now
prints one warning and renders everything as `other`.

**orrery/provenance_scanner.py** -- passes the `filepath` its scan loop
already has.

**orrery/export_orbit_cache.py** -- the stale "add a ROLE_MAP entry"
step corrected.

**orrery/add_docstrings.py**, **gallery/add_docstrings.py** --
`module_atlas.py` added to `GALLERY_ROOT_FILES`.

**gallery/module_atlas.py** -- NEW FILE. The gallery had no atlas at all.
Same file as the orrery's apart from `SCAN_PATHS` and an empty starting
mirror. It will also create MODULE_ATLAS.md and MODULE_INDEX.md in that
repo on first run.

Credit lines on all seven.

## Verified

- **Import, not just compile.** Every touched module executed in a clean
  namespace. This is the gate the last round taught: `Role: devtool` at
  module level is a legal annotation, so `py_compile` cannot see the
  failure mode.
- **No tag leakage.** All 141 modules across both trees: every tag inside
  its docstring, zero module-level `Role:`/`Domain:` annotations.
- **Classifier agrees with every docstring**, 114 of 114, all `source ==
  'tag'`.
- **Three states demonstrated** on throwaways: normal tag; legacy
  fallback when the tag is removed but the mirror remembers; true
  `undetermined` when both are gone, appearing under its own
  MODULE_INDEX heading and in the coverage report.
- **Self-rewrite is safe.** The marker regex is line-anchored because
  this file defines the marker strings -- unanchored, it would match the
  constant definitions and eat them. Second run reports "already
  current".
- **Gallery copy** scans 24 modules across five paths, zero collisions.
- **dep_trace** returns correct visual categories through the existing
  `_ROLE_TO_VISUAL` map; an unknown module gives `other`.
- **agentic-pre-test:** `palomas_orrery.py` under `xvfb`, throwaway copy,
  `SystemButtonFace` swap -- reached `Dashboard ready`, 182 object
  variables, sash positions. Throwaway deleted.

## Tony-action (decide): provenance Tier-1 moved

Tier-1 findings went from **105 at clean HEAD to 145** on the built tree,
in this sandbox. Both numbers are non-zero, so this environment is
missing something the real run has -- suppression state, most likely --
and neither figure should be read as the true count.

The most likely cause of the increase is the intended one: `classify_role`
now returns a real role for modules that used to fall through, which is
exactly the L-078 coverage widening this work was meant to produce. More
modules in scope means more findings surfaced, not more problems created.
But I could not confirm that in this session, and Tier-1 = 0 is a push
gate. Run the scanner locally and compare against your own baseline
before pushing.

## Noted, not fixed

`dep_trace.py` carries 1279 non-ASCII bytes -- box-drawing characters in
its section divider comments. Byte-identical before and after my edits,
so it predates this work. It is a standing violation of the ASCII-only
convention; out of scope here, worth a ledger item.

## Still open

**Tony-action (do):** commit all seven, run `module_atlas.py` in both
repos, and push. Send both SHAs.

**Tony:**
gallery docstring output:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
  Scan paths: ., tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  UPDATED  add_docstrings.py                                devtool / dev_tools
  SAME     module_atlas.py                                 
  SAME     tools/debug_encke_tp.py                         
  SAME     tools/gallery_cache_builder.py                  
  SAME     tools/gallery_cleanup.py                        
  SAME     tools/gallery_editor.py                         
  SAME     tools/gallery_json_fixer.py                     
  SAME     tools/gallery_studio.py                         
  SAME     tools/inspect_staging.py                        
  SAME     tools/json_converter.py                         
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
  unchanged    23
  updated      1
  total        24

  CHANGELOG (4) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - add_docstrings.py: 2 credit lines (changelog docstring)
    - module_atlas.py: 2 credit lines (changelog docstring)
    - tools/gallery_cache_builder.py: 3 credit lines (changelog docstring)
    - tools/gallery_studio.py: 3 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.


  Write these changes? [y/n]: y


==============================================================
  Role / Domain Tag Sweep -- WRITING
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
  Scan paths: ., tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  UPDATED  add_docstrings.py                                devtool / dev_tools
  SAME     module_atlas.py                                 
  SAME     tools/debug_encke_tp.py                         
  SAME     tools/gallery_cache_builder.py                  
  SAME     tools/gallery_cleanup.py                        
  SAME     tools/gallery_editor.py                         
  SAME     tools/gallery_json_fixer.py                     
  SAME     tools/gallery_studio.py                         
  SAME     tools/inspect_staging.py                        
  SAME     tools/json_converter.py                         
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
  unchanged    23
  updated      1
  total        24

  CHANGELOG (4) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - add_docstrings.py: 2 credit lines (changelog docstring)
    - module_atlas.py: 2 credit lines (changelog docstring)
    - tools/gallery_cache_builder.py: 3 credit lines (changelog docstring)
    - tools/gallery_studio.py: 3 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

orrery docstring output:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
  Scan paths: .
==============================================================

  UPDATED  add_docstrings.py                                devtool / dev_tools
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
  SAME     data_acquisition.py                             
  SAME     data_acquisition_distance.py                    
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
  unchanged    113
  updated      1
  total        114

  CHANGELOG (11) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - add_docstrings.py: 2 credit lines (changelog docstring)
    - apsidal_markers.py: 4 credit lines (changelog docstring)
    - dep_trace.py: 2 credit lines (changelog docstring)
    - earth_system_controller.py: 2 credit lines (changelog docstring)
    - export_orbit_cache.py: 2 credit lines (changelog docstring)
    - idealized_orbits.py: 2 credit lines (changelog docstring)
    - module_atlas.py: 2 credit lines (changelog docstring)
    - planet_visualization.py: 2 credit lines (changelog docstring)
    - planet_visualization_utilities.py: 4 credit lines (changelog docstring)
    - provenance_scanner.py: 2 credit lines (changelog docstring)
    - visualization_utils.py: 2 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.


  Write these changes? [y/n]: y


==============================================================
  Role / Domain Tag Sweep -- WRITING
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
  Scan paths: .
==============================================================

  UPDATED  add_docstrings.py                                devtool / dev_tools
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
  SAME     data_acquisition.py                             
  SAME     data_acquisition_distance.py                    
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
  unchanged    113
  updated      1
  total        114

  CHANGELOG (11) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - add_docstrings.py: 2 credit lines (changelog docstring)
    - apsidal_markers.py: 4 credit lines (changelog docstring)
    - dep_trace.py: 2 credit lines (changelog docstring)
    - earth_system_controller.py: 2 credit lines (changelog docstring)
    - export_orbit_cache.py: 2 credit lines (changelog docstring)
    - idealized_orbits.py: 2 credit lines (changelog docstring)
    - module_atlas.py: 2 credit lines (changelog docstring)
    - planet_visualization.py: 2 credit lines (changelog docstring)
    - planet_visualization_utilities.py: 4 credit lines (changelog docstring)
    - provenance_scanner.py: 2 credit lines (changelog docstring)
    - visualization_utils.py: 2 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

orrery module atlas output: 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/module_atlas.py
Scanning ....
  ROLE_MAP: already current (114 modules)
Atlas written to MODULE_ATLAS.md
  114 modules, 962 functions, 92,707 lines

Role summary:
  gui                    6 modules
  rendering             23 modules
  rendering/shells      15 modules
  computation           14 modules
  data                  15 modules
  cache                  5 modules
  pipeline               5 modules
  scenario               4 modules
  utility                6 modules
  devtool               21 modules
Index written to MODULE_INDEX.md
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

gallery module atlas output:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/module_atlas.py
Scanning ....
  ROLE_MAP: already current (24 modules)
Atlas written to MODULE_ATLAS.md
  24 modules, 137 functions, 13,215 lines

Role summary:
  rendering              5 modules
  computation            1 modules
  data                   2 modules
  cache                  2 modules
  pipeline               1 modules
  utility                1 modules
  devtool               12 modules
Index written to MODULE_INDEX.md
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

**Gate:** Phase 4 (verify the shipped classifier, then update the two
skill docs) opens on that push. Nothing in Phase 4 was started.

## Ref

`module_atlas.py`, `dep_trace.py`, `provenance_scanner.py`,
`export_orbit_cache.py`, `add_docstrings.py` (both), `ledger_index.py`
(marker-zone pattern), `AS_BUILT_L163_phase3a.md`,
`AS_BUILT_L163_add_docstrings_fix.md`, L-078, agentic-pre-test v1.1.

---

Session written July 2026 with Anthropic's Claude Opus 5.
