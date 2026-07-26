Built on:
- orrery: a812f9fee0e56a1f7b25aa8cadb4a5e3b37517d7 at https://github.com/tonylquintanilla/palomas_orrery
- gallery: ba2d1c059e8f1e98492bb2616cfb719633c97e51 at https://github.com/tonylquintanilla/tonyquintanilla.github.io
- pushed at: [paste both SHAs after committing the fix to both add_docstrings.py copies]

Ledger handle: L-163
Phase: 3b blocker fix -- add_docstrings.py tag-relocation defect
Session: Opus 5 builder session, July 26, 2026

---

# L-163 -- add_docstrings.py off-by-one fix

## What broke

`strip_existing_tags()` removes the two tag lines and then collapses the
blank-line seam they leave behind -- three lines out of the list -- but
returns only `removed = 2`. The caller does `end -= removed` to keep its
docstring-end index valid, so `end` lands one line PAST the closing
quotes.

`find_insert_point()` anchors on the credit line when there is exactly
one, and returns `end` otherwise. So the two branches behave differently:

- **One credit line:** the anchor is found by content, so the stale
  `end` is never used. Safe.
- **Zero credit lines, or two or more (changelog):** returns `end`, and
  the tag block is written one line below the closing `"""` -- into
  module scope.

The original 136-module sweep was clean because nothing was stripped on
a first write: `removed == 0`, no seam collapse, no off-by-one. The
defect only fires on a **refresh** that also lands in the
end-of-docstring branch.

## Why it was hard to see

`Role: devtool` at module level is a legal Python variable annotation.
`py_compile` passes. `compileall` passes. The module raises `NameError`
only when something imports it. I ran `compileall` on the damaged tree,
saw it clean, and moved on -- the failure surfaced only when the tool
crashed importing itself.

This is the protocol's own lesson arriving in a new costume:
compile-only verification is the absence of a runtime test, not a
substitute for one. Worth a field note in agentic-pre-test -- for
docstring-level sweeps the gate is "does it import", not "does it
compile".

## The trigger, and how close it was

The six existing changelog modules got their tags placed at
end-of-docstring on the FIRST write, so re-runs find them already
positioned and report SAME. The defect fires on the **transition**: a
module that currently has one credit line gains a second one, then gets
swept.

Adding a credit line is what the project's own convention requires on
every touched module. So the next routine edit to any of the ~108
single-credit-line modules would have hit this -- including all five
modules Phase 3b touches. It reproduced on all five.

## The fix

One line, plus the comment explaining it, in `strip_existing_tags()`:
count the seam deletion in the returned total. The caller's arithmetic
is then correct and both placement branches work. `removed` is also used
as a truthiness test for the added/updated label, which a value of 3
does not disturb.

Same edit applies to BOTH copies -- orrery root and gallery root. They
are identical apart from `SCAN_PATHS`, and should stay that way.

## Verified

- **Reproduction before the fix:** clean orrery HEAD, one credit
  paragraph appended to five docstrings, one sweep write. All five had
  their tag blocks written into module scope. All five still passed
  `py_compile`. All five failed on import.
- **Same reproduction after the fix:** all 114 modules keep both tags
  inside the docstring; zero `Role:`/`Domain:` module-level annotations
  anywhere; all five edited modules execute their module body cleanly.
- **Idempotent:** a second write run reproduces the tree byte for byte.
- **Placement is right:** for a changelog docstring the block lands at
  the very end, after the whole history -- your Phase 2 close-out
  decision, now actually reached instead of overshooting past the
  quotes.
- **Change scope:** 35 lines added across the 114 modules, every one of
  them a tag line, a blank separator, or the intended credit line. Zero
  unexpected edits.
- **Live repos are clean.** All 140 modules across both HEADs checked
  for stray module-level `Role:`/`Domain:` annotations: none. Nothing
  shipped damaged; the blast radius was my sandbox.

## Unreported drift, no action needed

The gallery moved `d1be9e63` -> `ba2d1c05` since the last report: 26
files under `data/solar-system/`, a nightly cache builder run. No `.py`
touched, so nothing here is affected.

## Still open

**Tony-action (do):** apply the snippet to both `add_docstrings.py`
copies, re-run the sweep in both repos to confirm SAME across the board,
and push. Send both SHAs.

**Tony:**
gallery output: 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
  Scan paths: ., tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  SAME     add_docstrings.py                               
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
  total        23

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
  Scan paths: ., tools, gallery/assembler, gallery/assembler/harness, gallery/assembler/tests
==============================================================

  SAME     add_docstrings.py                               
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
  total        23

  CHANGELOG (2) -- more than one credit line. Per the
  Phase 2 placement decision, the tag goes at the very end
  of the docstring instead of above any single entry:
    - tools/gallery_cache_builder.py: 3 credit lines (changelog docstring)
    - tools/gallery_studio.py: 3 credit lines (changelog docstring)

  No problems. Every module in scope carries both tags.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

orrery output:
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/add_docstrings.py

==============================================================
  Role / Domain Tag Sweep -- PREVIEW (nothing written)
  Target: C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github
  Scan paths: .
==============================================================

  SAME     add_docstrings.py                               
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
  unchanged    114
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

  SAME     add_docstrings.py                               
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
  unchanged    114
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

**Gate:** Phase 3b resumes on that push. The classifier work itself was
built and behaved correctly before I stopped -- three-state
classification, self-safe marker-zone regeneration, working gallery
copy, all three call sites updated -- but every one of those files went
through the credit-line step, which is the contaminated path. It gets
rebuilt from the fixed base rather than salvaged.

## Ref

`add_docstrings.py` (`strip_existing_tags`, `find_insert_point`,
`insert_tags`), `AS_BUILT_L163_phase2.md` (close-out placement
decision), `AS_BUILT_L163_phase3a.md`, agentic-pre-test skill v1.1,
`LEDGER_CONSOLIDATED.md` (L-163).

---

Session written July 2026 with Anthropic's Claude Opus 5.
