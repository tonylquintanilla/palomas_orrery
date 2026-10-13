<!-- Doc-Kind: hand | Audit of the dashboard's 103 buttons: labels against script names, description length, and how a tool is found. Working document for a design talk; not yet a ledger item. -->
# Dashboard labels, descriptions and findability: an audit

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery; gallery read at
f9453ddbc8b29ed15550a4e980bf3688eed79c82 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Neither is touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Fable 5.1.

- Type: DESIGN SESSION record (zero code). Read from `palomas_orrery_dashboard.py`
  (its LAUNCH_GROUPS), `orrery_maintenance_run.py` and the gallery's
  `gallery_maintenance_run.py`, by a script, not from memory.
- Not yet in the ledger. If a direction is chosen, it gets a handle then.

## 1. The numbers

- 103 buttons in 8 groups: Maintenance Run (36), Gallery -- checks and data (34), Tools and Caches (12), Gallery -- authoring (8), Earth System (5), Daily Run (5), Solar System (2), Stars (1).
- Every card shows its name and its whole description, wrapped at 600 px. The
  script name shows only as a tooltip on the Launch button.
- Descriptions: shortest 6 words, median 59, longest 221. 47 of 103 run over
  60 words; 15 run over 100.
- Every maintenance-run row, orrery (32 scripts) and gallery (28 rows), has a
  button. That was checked separately today.

## 2. Labels that do not say what the script is

The test: could you pick the button from the script name, or the script
from the button, without the description? 11 fail it outright; 4 are partial;
2 are clear but carry a different name from the maintenance run's row.

| Label | Script | Verdict | A label that says it |
|---|---|---|---|
| Food Insecurity Controller | `earth_system_controller.py` | partial | same script as Google Earth Controller; say so |
| Artifact 1 Assembler Pin | `documentation/pin_artifact1_known_failure.py` | partial | Artifact 1 -- known-failure pin |
| Config Mirror -- report only | `tools/mirror_constants.py` | unclear | Mirror Constants -- report only |
| Config Mirror Check | `tools/check_constants_links.py` | unclear | Constants Links -- config mirror |
| Daily Run Steps | `daily_run.py` | partial | Daily Run -- list its steps |
| Gallery Builder Offline Tests | `test_gallery_cache_builder_offline.py` | mismatch | Cache Builder -- offline tests |
| Gallery Module Atlas | `module_atlas.py` | partial | Module Atlas -- gallery |
| Mirror Suite | `tools/test_mirror_constants.py` | unclear | Mirror Constants -- test |
| Pointer Join | `tools/check_constants_links.py` | unclear | Constants Links -- pointer join |
| Builder Marker Join | `test_worksheet_request_builder.py` | unclear | Worksheet Request Builder -- test |
| Extractor Pins | `test_extractor_pins.py` | unclear | Extractor Pins -- test |
| Test Constants Provenance | `test_constants_provenance.py` | mismatch | Constants Relations (the run calls it that) |
| Test Exact Rows By The Count | `exact_rows_report.py` | unclear | Exact Rows Report -- check |
| Test Row Shape | `test_status_lines.py` | unclear | Status Lines -- shape only |
| Test Scanner Recognition | `test_provenance_1d.py` | unclear | Scanner Recognition (provenance 1d/1e) -- test |
| Worksheet Key Round Trip | `test_worksheet_keys.py` | unclear | Worksheet Keys -- test |
| Animation HTML Tool | `measure_animation_html.py` | unclear | Measure Animation HTML |

Two patterns behind most of these:

- **One script, two labels.** `check_constants_links.py` is "Config Mirror
  Check" and "Pointer Join"; `exact_rows_report.py` is "Exact Rows Report" and
  "Test Exact Rows By The Count"; `test_status_lines.py` is "Test Status Lines"
  and "Test Row Shape". The label names the mode and drops the script.
- **"Test" on some checkers and not others.** Under the CHECKERS heading, 20
  labels start with "Test" and 6 do not (Builder Marker Join, Constants Change
  Report, Extractor Pins, Provenance Scanner, Worksheet Checker, Worksheet Key
  Round Trip). The heading already says they are checkers.

## 3. The dashboard label and the run's row name disagree

When a row goes red in the maintenance run, you go to the dashboard to rerun
it. These are the rows whose name there is not the name here (the "Test"
prefix and an L-handle are ignored in the comparison):

| Run row | Dashboard label |
|---|---|
| Ledger index | Update Ledger Index |
| Skill manifest | Update Skill Manifest |
| Module atlas | Regenerate Module Atlas |
| Constants change | Constants Change Report |
| Constants relations | Test Constants Provenance |
| Constants export check | Test Constants Export |
| Objects export check | Test Objects Export |
| Drawings export check | Test Drawings Export |
| Worksheet checker tests | Test Worksheet Checker |
| Cache builder suite (gallery) | Gallery Builder Offline Tests |
| Drawings (gallery) | Drawings Check |
| Artifact 1 assembler (gallery) | Artifact 1 Assembler Pin |
| Guest book + Guest book updater (gallery) | Guest Book Checks (one button for both, by design, L-281) |

The other 47 rows match their button by name. A rule that fixes this class
for good: THE BUTTON IS NAMED WHAT THE RUN PRINTS. One name per check, in
both places, and a check in the maintenance run that the two lists agree
(the same shape as the skill-manifest check).

## 4. Descriptions: the ten longest, and what a short line looks like

| Words | Label | Script |
|---|---|---|
| 221 | Gallery Cache Builder -- Manual Run | `tools/gallery_cache_builder.py` |
| 171 | Exhibit Store Editor | `exhibit_store_editor.py` |
| 166 | Gallery Maintenance Run -- offline | `gallery_maintenance_run.py` |
| 158 | Cache Siblings | `documentation/check_cache_siblings.py` |
| 156 | Daily Run -- everything indented below | `daily_run.py` |
| 155 | Guest Book Updater | `tools/guestbook_updater.py` |
| 146 | Hover Budget | `documentation/run_hover_budget.py` |
| 144 | Worksheet Request Builder | `worksheet_request_builder.py` |
| 132 | Solar System Figures | `documentation/run_solar_system_figures.py` |
| 123 | Gallery Maintenance Run -- live, AFTER a push | `gallery_maintenance_run.py` |

A card can carry two things: a line that says what the tool does, in a
dozen words, always visible; and the paragraph as it is, behind the card
(a tooltip on the name, or an expand). Nothing written is lost. Five of
the longest, as a one-line "does what":

- Gallery Cache Builder -- Manual Run (221 words): *Fetches from Horizons,*
  *validates, and swaps the new cache into data/solar-system; you commit.*
- Exhibit Store Editor (171 words): *A window to edit the words a visitor*
  *reads in a room; writes only the line asked, in objects_config.json.*
- Gallery Maintenance Run -- offline (166 words): *Every gallery check that*
  *needs no network, in one run; run after the build, before you commit.*
- Daily Run (156 words): *The gallery's daily sequence in one window: guest*
  *book, Horizons check, cache build, offline maintenance run.*
- Guest Book Updater (155 words): *Shows each new form message to approve,*
  *decline or defer; writes only data/guestbook.json.*

These five are drafts for the shape, not the words; each would be checked
against its script before it lands.

## 5. Finding a tool without the search box

What is there now: eight groups in one scrolling column, two of them with
34 and 36 cards; a Find box that filters name and description and redraws
the matches under their group headings (L-341). The groups answer "which
repository and which kind", not "what am I trying to do".

Three ways to make a tool findable by eye, each on its own, any two together:

- **A. Shorter cards.** The one-line description, the script name in small
  type under the label, the paragraph behind the card. The column gets about
  three times shorter and a label-plus-script line is scannable. Cheapest;
  changes no grouping; your checker order of 2026-09-12 stands.
- **B. Subheadings inside the two big groups.** Maintenance Run already has
  GENERATORS and CHECKERS. The gallery checks group has none; its 34 cards
  fall into five kinds: pulls from the orrery (3), mirror checks and suites
  (6), room smokes run by Node (10), the cache and its builder (5), the
  rest. A heading per kind, cards alphabetical under it. Changes the drawn
  order of that group only.
- **C. A "when" index above the groups.** A short list of occasions, each
  naming its buttons: before a push; after editing constants_new.py; after
  a cache build; a room looks wrong; a new object. It answers the question
  you actually arrive with. Costs the most to keep true, so it would need
  to be generated from a tag on each entry, not hand-written.

On Claude's own tools: the Design type fits a mock-up of a card and a
group for you to judge before any code moves; the Dashboard type is for
live metrics pages and does not fit a launcher.

## 6. The whole list

| Group | Label | Script | Run row | Words |
|---|---|---|---|---|
| Solar System | Paloma's Orrery | `palomas_orrery.py` |  | 9 |
| Solar System | Orbital Construction | `orbital_param_viz.py` |  | 7 |
| Earth System | Earth System Viewer | `earth_system_visualization_gui.py` |  | 6 |
| Earth System | Google Earth Controller | `earth_system_controller.py` |  | 7 |
| Earth System | Earth System Generator | `earth_system_generator.py` |  | 7 |
| Earth System | Food Insecurity Generator | `food_insecurity_generator.py` |  | 8 |
| Earth System | Food Insecurity Controller | `earth_system_controller.py` |  | 11 |
| Stars | Star Visualization | `star_visualization_gui.py` |  | 8 |
| Daily Run | Daily Run -- everything indented below | `daily_run.py` | Daily run steps | 156 |
| Daily Run | Guest Book Updater | `tools/guestbook_updater.py` |  | 155 |
| Daily Run | Horizons Check | `tools/horizons_check.py` |  | 116 |
| Daily Run | Gallery Cache Builder -- Manual Run | `tools/gallery_cache_builder.py` |  | 221 |
| Daily Run | Gallery Maintenance Run -- offline | `gallery_maintenance_run.py` |  | 33 |
| Gallery -- checks and data | Gallery Maintenance Run -- offline | `gallery_maintenance_run.py` |  | 166 |
| Gallery -- checks and data | Arrival | `documentation/run_offline_check.py` |  | 92 |
| Gallery -- checks and data | Artifact 1 Assembler Pin | `documentation/pin_artifact1_known_failure.py` | Artifact 1 assembler | 68 |
| Gallery -- checks and data | Cache In Step | `tools/check_cache_in_step.py` | Cache in step | 68 |
| Gallery -- checks and data | Cache Siblings | `documentation/check_cache_siblings.py` | Cache siblings | 158 |
| Gallery -- checks and data | Collapsed Features | `sweep_collapsed_features.py` | Collapsed features | 55 |
| Gallery -- checks and data | Config Mirror -- report only | `tools/mirror_constants.py` |  | 81 |
| Gallery -- checks and data | Config Mirror Check | `tools/check_constants_links.py` | Pointer join | 47 |
| Gallery -- checks and data | Constants Export Pull | `tools/pull_constants_export.py` |  | 68 |
| Gallery -- checks and data | Daily Run Steps | `daily_run.py` | Daily run steps | 29 |
| Gallery -- checks and data | Display Figures | `documentation/run_offline_check.py` |  | 79 |
| Gallery -- checks and data | Drawings Check | `tools/check_drawings.py` | Drawings | 78 |
| Gallery -- checks and data | Drawings Pull | `tools/pull_drawings.py` |  | 69 |
| Gallery -- checks and data | Earth Scene Geometry | `documentation/run_offline_check.py` |  | 86 |
| Gallery -- checks and data | Feature Renderers | `documentation/run_offline_check.py` |  | 67 |
| Gallery -- checks and data | Gallery Builder Offline Tests | `test_gallery_cache_builder_offline.py` | Cache builder suite | 119 |
| Gallery -- checks and data | Gallery Module Atlas | `module_atlas.py` | Module atlas | 36 |
| Gallery -- checks and data | Guest Book Checks | `documentation/run_guestbook_checks.py` |  | 114 |
| Gallery -- checks and data | Horizons Check Suite | `tools/test_horizons_check.py` | Horizons check suite | 60 |
| Gallery -- checks and data | Horizons Confirmations | `tools/check_horizons_confirmations.py` | Horizons confirmations | 39 |
| Gallery -- checks and data | Hover Budget | `documentation/run_hover_budget.py` |  | 146 |
| Gallery -- checks and data | Mirror Suite | `tools/test_mirror_constants.py` | Mirror suite | 60 |
| Gallery -- checks and data | Objects Export Pull | `tools/pull_objects_export.py` |  | 52 |
| Gallery -- checks and data | Objects Mirror Check | `tools/mirror_objects.py` | Objects mirror check | 65 |
| Gallery -- checks and data | Objects Mirror Suite | `tools/test_mirror_objects.py` | Objects mirror suite | 55 |
| Gallery -- checks and data | Page Framing | `documentation/run_offline_check.py` |  | 64 |
| Gallery -- checks and data | Pointer Join | `tools/check_constants_links.py` | Pointer join | 69 |
| Gallery -- checks and data | Pole of Date | `tools/test_pole_of_date.py` | Pole of date | 59 |
| Gallery -- checks and data | Solar System Drawer | `documentation/run_offline_check.py` |  | 67 |
| Gallery -- checks and data | Solar System Figures | `documentation/run_solar_system_figures.py` |  | 132 |
| Gallery -- checks and data | Store Editor Suite | `tools/test_exhibit_store_editor.py` | Store editor suite | 111 |
| Gallery -- checks and data | Store Writer Suite | `tools/test_store_writer.py` | Store writer suite | 94 |
| Gallery -- checks and data | Sun Shells | `documentation/run_offline_check.py` |  | 70 |
| Gallery -- checks and data | Gallery Maintenance Run -- live, AFTER a push | `gallery_maintenance_run.py` |  | 123 |
| Gallery -- authoring | Exhibit Store Editor | `exhibit_store_editor.py` |  | 171 |
| Gallery -- authoring | Gallery Cleanup | `gallery_cleanup.py` |  | 17 |
| Gallery -- authoring | Gallery Editor | `gallery_editor.py` |  | 7 |
| Gallery -- authoring | Gallery JSON Fixer | `gallery_json_fixer.py` |  | 8 |
| Gallery -- authoring | Gallery Studio | `gallery_studio.py` |  | 8 |
| Gallery -- authoring | Inspect Staging | `inspect_staging.py` |  | 60 |
| Gallery -- authoring | JSON Converter | `json_converter.py` |  | 6 |
| Gallery -- authoring | Serve Gallery Locally | `serve_gallery.py` |  | 78 |
| Maintenance Run | MAINTENANCE RUN -- everything indented below | `orrery_maintenance_run.py` |  | 63 |
| Maintenance Run | *GENERATORS -- regenerated every run; a no-op when nothing mo* | | | |
| Maintenance Run | Constants Export | `export_constants.py` | Constants export | 72 |
| Maintenance Run | Data Inventory | `data_inventory.py` | Data inventory | 18 |
| Maintenance Run | Exact Rows Report | `exact_rows_report.py` | Exact rows by the count | 120 |
| Maintenance Run | Document Index | `doc_index.py` | Document index | 99 |
| Maintenance Run | Drawings Export | `export_drawings.py` | Drawings export | 48 |
| Maintenance Run | Objects Export | `export_objects.py` | Objects export | 77 |
| Maintenance Run | Regenerate Module Atlas | `module_atlas.py` | Module atlas | 12 |
| Maintenance Run | Update Ledger Index | `ledger_index.py` | Ledger index | 22 |
| Maintenance Run | Update Skill Manifest | `skills_index.py` | Skill headers | 18 |
| Maintenance Run | *CHECKERS -- these decide the push call* | | | |
| Maintenance Run | Builder Marker Join | `test_worksheet_request_builder.py` | Builder marker join | 82 |
| Maintenance Run | Constants Change Report | `constants_change_report.py` | Constants change | 73 |
| Maintenance Run | Extractor Pins | `test_extractor_pins.py` | Extractor pins | 100 |
| Maintenance Run | Provenance Scanner | `provenance_scanner.py` | Provenance scanner | 20 |
| Maintenance Run | Test Citation Inheritance | `test_citation_inheritance.py` | Citation inheritance | 10 |
| Maintenance Run | Test Constants Export | `test_constants_export.py` | Constants export check | 50 |
| Maintenance Run | Test Constants Provenance | `test_constants_provenance.py` | Constants relations | 18 |
| Maintenance Run | Test Cross-Check Annotations | `test_cross_checked.py` | Cross-check annotations | 18 |
| Maintenance Run | Test Derived Figures | `test_derived_figures.py` | Derived figures | 66 |
| Maintenance Run | Test Dimensions | `test_dimensions.py` | Dimensions | 59 |
| Maintenance Run | Test Drawings Export | `test_drawings_export.py` | Drawings export check | 70 |
| Maintenance Run | Test Earth Pole of Date | `test_earth_pole_of_date.py` | Earth pole of date | 62 |
| Maintenance Run | Test Exact Rows By The Count | `exact_rows_report.py` | Exact rows by the count | 53 |
| Maintenance Run | Test Hills Cloud Sampler | `test_hills_cloud_sampler.py` | Hills cloud sampler (L-421) | 57 |
| Maintenance Run | Test Objects Export | `test_objects_export.py` | Objects export check | 54 |
| Maintenance Run | Test Orbit Cache | `test_orbit_cache.py` | Orbit cache | 21 |
| Maintenance Run | Test Position Digits | `test_position_digits.py` | Position digits (L-401) | 96 |
| Maintenance Run | Test Reset Completeness | `test_reset_completeness.py` | Reset completeness | 23 |
| Maintenance Run | Test Row Shape | `test_status_lines.py` | Row shape | 70 |
| Maintenance Run | Test Scanner Recognition | `test_provenance_1d.py` | Scanner recognition 1d/1e | 80 |
| Maintenance Run | Test Scanner Row Run | `test_row_run.py` | Scanner row run (L-414) | 38 |
| Maintenance Run | Test Skill Headers | `skills_index.py` | Skill headers | 60 |
| Maintenance Run | Test Status Lines | `test_status_lines.py` | Row shape | 38 |
| Maintenance Run | Test Worksheet Checker | `test_worksheet_checker.py` | Worksheet checker tests | 44 |
| Maintenance Run | Worksheet Checker | `worksheet_checker.py` | Worksheet checker | 59 |
| Maintenance Run | Worksheet Key Round Trip | `test_worksheet_keys.py` | Worksheet key round trip | 61 |
| Tools and Caches | Add Module Docstrings | `add_docstrings.py` |  | 20 |
| Tools and Caches | Animation HTML Tool | `measure_animation_html.py` |  | 33 |
| Tools and Caches | Climate Cache Manager | `climate_cache_manager.py` |  | 10 |
| Tools and Caches | Create Ephemeris Database | `create_ephemeris_database.py` |  | 10 |
| Tools and Caches | Dependency Trace | `dep_trace.py` |  | 17 |
| Tools and Caches | Earth Pole Live Check | `earth_pole_live_check.py` |  | 68 |
| Tools and Caches | Export Orbit Cache | `export_orbit_cache.py` |  | 18 |
| Tools and Caches | Osculating Cache Manager | `osculating_cache_manager.py` |  | 13 |
| Tools and Caches | SIMBAD Query Manager | `simbad_manager.py` |  | 14 |
| Tools and Caches | Verify Orbit Cache | `verify_orbit_cache.py` |  | 21 |
| Tools and Caches | VOT Cache Manager | `vot_cache_manager.py` |  | 6 |
| Tools and Caches | Worksheet Request Builder | `worksheet_request_builder.py` |  | 144 |

Session record written October 2026 with Anthropic's Claude Fable 5.1.
