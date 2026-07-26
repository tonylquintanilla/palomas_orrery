"""
add_docstrings.py - Two related tools for module-level docstrings.

(1) The Role:/Domain: tag sweep (L-163, the DEFAULT mode when you just
    run this file). Inserts or refreshes a two-line classification block
    inside a module's EXISTING docstring. Touches nothing else.
(2) The original whole-docstring inserter (--docstrings flag, LEGACY
    mode). Replaces a module's entire docstring from the hand-authored
    DOCSTRINGS dict below. Still useful for a brand-new module that has
    no docstring at all yet.

=====================================================================
HOW TO RUN IT (both modes)
=====================================================================
From VS Code: open this file and click Run. It always starts in PREVIEW
-- nothing is written to any file yet, it only prints what it WOULD do.

If the preview finds no problems, it then asks:

    Write these changes? [y/n]:

Click into the terminal panel, type y and press Enter to actually save
the changes, or press Enter (or type n) to stop without writing
anything -- anything other than y/yes is treated as "don't write," so
a blank answer or a typo can never accidentally write. If the preview
finds PROBLEMS, it will not ask -- fix those first (usually a module
missing from MODULE_TAGS, or a role/domain not in the approved list
below) and run it again.

Advanced, not needed for normal use: `python add_docstrings.py --write`
from a terminal writes immediately, skipping the preview and the
question. The y/n prompt above does the same thing more safely, so
there's normally no reason to use this.

=====================================================================
WHEN TO RUN THE TAG SWEEP (mode 1, the default)
=====================================================================
Run it any time a module's Role:/Domain: tag needs adding or fixing:
  - A new module was added and has no tag yet.
  - An existing tag looks wrong and needs correcting.
For a single module, it's just as easy to type the two lines by hand
directly into that module's own docstring (see placement rule below).
This script earns its keep for BULK changes -- many modules at once --
or when you want the placement rule applied consistently without doing
it by hand every time.

HOW TO ADD OR CHANGE A CLASSIFICATION:
  1. Find (or add) the module's entry in MODULE_TAGS below, keyed by
     its path relative to the repo root (e.g. 'my_module.py' for the
     orrery repo root, or 'gallery/assembler/errors.py' for the
     gallery repo).
  2. Set the value to (role, domain). role must be one of ROLE_VOCAB,
     domain one of DOMAIN_VOCAB (both defined below) -- anything else
     is reported as a PROBLEM and never written, so a typo gets caught
     instead of silently landing in a file.
  3. Run this script as described above.

PLACEMENT RULE the sweep applies: the two-line block goes directly
above the module's 'Module updated:' credit line, blank-line separated.
No credit line, OR more than one (a changelog docstring with several
'Module updated:' entries) -> the block goes at the very end of the
docstring instead, after all of it (decided in chat, July 2026 --
wedging it between two changelog entries read worse than putting it
after the whole history).

IS ROLE_MAP UPDATED AUTOMATICALLY? Not yet, as of this writing (Phase 2,
July 2026). This script only writes tags INTO each module's docstring --
module_atlas.py's ROLE_MAP dictionary is still a separate, hand-maintained
table and does not read these tags yet. Phase 3 of this redesign will
change that: module_atlas.py will read the Role:/Domain: lines straight
out of each module's docstring and build ROLE_MAP from them automatically,
every time it runs. Once that lands, editing a module's docstring (by
hand or with this script) is enough -- ROLE_MAP updates itself the next
time module_atlas.py runs, with no separate dictionary to keep in sync.
This paragraph should be updated once Phase 3 ships.

=====================================================================
LEGACY MODE (--docstrings): adding a docstring to a module with none
=====================================================================
Reads each module name in the DOCSTRINGS dict below, inserts a full
triple-quoted docstring before the first import or code line (or below
any shebang/comment header). Uses Python binary mode to preserve line
endings (CRLF/LF). For a module that already has a docstring, prefer
hand-editing it directly, or use the tag sweep above to add just the
two classification lines -- this legacy mode replaces the WHOLE
docstring.

Role: devtool
Domain: dev_tools

Module updated: July 2026 with Anthropic's Claude Sonnet 5
"""

import os
import sys
import re
import ast

# Docstring credit line the tag block anchors to, and the tag pattern the
# sweep uses to find (and refresh) a block it wrote on an earlier run.
CREDIT_PREFIX = 'Module updated:'
TAG_RE = re.compile(r'^\s*(Role|Domain):\s')

# ============================================================
# DOCSTRINGS TO ADD
# ============================================================
# Key = module name (without .py)
# Value = docstring content (will be wrapped in triple quotes)
#
# Standard format:
#   Line 1: module_name.py - One-line purpose.
#   Lines 2+: 2-3 sentence explanation.
#   Key functions: top 3-5 (only for complex modules)
#   Credit line.

DOCSTRINGS = {

    # ============================================================
    # NO DOCSTRING GROUP (21 modules)
    # ============================================================

    'catalog_selection': (
        'catalog_selection.py - Unified star selection from Hipparcos and Gaia catalogs.\n'
        '\n'
        'Merges stars from both catalogs with consistent deduplication logic.\n'
        'Used by both magnitude-mode and distance-mode HR diagram pipelines.\n'
        'Returns combined astropy Table with star counts by source category.\n'
        '\n'
        'Key functions:\n'
        '    select_stars() - Select and merge stars by magnitude or distance limit\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'comet_visualization_shells': (
        'comet_visualization_shells.py - Comet visual components for 3D orrery plots.\n'
        '\n'
        'Builds nucleus, coma, ion tail, dust tail, and anti-tail traces for comets.\n'
        'Tail geometry is computed from Sun direction and heliocentric distance using\n'
        'activity factors that scale with solar proximity. Includes specialized traces\n'
        'for C/2026 A1 (MAPS): disintegration marker and ghost tail arc.\n'
        '\n'
        'Key functions:\n'
        '    create_comet_nucleus() - Scaled sphere marker at comet position\n'
        '    create_comet_ion_tail() - Straight anti-sunward ion tail\n'
        '    create_comet_dust_tail() - Curved dust tail with radiation pressure\n'
        '    create_maps_disintegration_marker() - Green diamond at 8.33 R_sun\n'
        '    create_maps_ghost_tail_trace() - Post-disintegration debris arc\n'
        '    add_comet_tails_to_figure() - Master dispatch: adds all tail traces to fig\n'
        '\n'
        'Consumed by: palomas_orrery.py (plot_objects, animate_objects)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'create_cache_backups': (
        'create_cache_backups.py - One-shot script to create timestamped backups of star data caches.\n'
        '\n'
        'Calls simbad_manager.protect_all_star_data() to back up SIMBAD query results\n'
        'and stellar property caches. Run manually before risky cache operations.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'earth_system_controller': (
        'earth_system_controller.py - KMZ layer selector for Google Earth Pro.\n'
        '\n'
        'Simple Tkinter GUI that lets users browse, select, and open KMZ climate\n'
        'data layers in Google Earth Pro. Layers are generated by\n'
        'earth_system_generator.py and stored in the data/ directory.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'earth_visualization_shells': (
        'earth_visualization_shells.py - Earth interior and orbital shell traces.\n'
        '\n'
        'Sphere shells for Earth\'s interior layers (inner core through crust),\n'
        'atmosphere, and upper atmosphere. Custom geometry for the magnetosphere,\n'
        'LEO altitude shell, and geostationary belt. Each function returns Plotly\n'
        'Scatter3d traces positioned relative to a center_position in AU.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'eris_visualization_shells': (
        'eris_visualization_shells.py - Eris interior and boundary shell traces.\n'
        '\n'
        'Sphere shells for Eris: core, mantle, crust, tenuous atmosphere, and\n'
        'Hill sphere. Based on New Horizons flyby constraints and thermal models.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'jupiter_visualization_shells': (
        'jupiter_visualization_shells.py - Jupiter interior, ring, and magnetosphere shell traces.\n'
        '\n'
        'Sphere shells for Jupiter\'s interior (core through cloud layer). Custom\n'
        'geometry for the ring system, Io plasma torus, radiation belts, and\n'
        'magnetosphere. Jupiter\'s magnetosphere is the largest structure in the\n'
        'solar system after the heliosphere.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'mars_visualization_shells': (
        'mars_visualization_shells.py - Mars interior and remnant field shell traces.\n'
        '\n'
        'Sphere shells for Mars interior layers (inner core through crust),\n'
        'atmosphere, upper atmosphere, remnant magnetosphere, and Hill sphere.\n'
        'Mars lacks a global dipole field; its magnetosphere represents crustal\n'
        'magnetic anomalies.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'mercury_visualization_shells': (
        'mercury_visualization_shells.py - Mercury interior, exosphere, and unique feature traces.\n'
        '\n'
        'Sphere shells for Mercury\'s large iron core (inner/outer), thin mantle and\n'
        'crust. Custom geometry for the sodium exosphere tail (anti-sunward),\n'
        'magnetosphere (compressed by solar wind), and Hill sphere. Mercury\'s core\n'
        'is proportionally the largest of any planet (~85%% of its radius).\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'moon_visualization_shells': (
        'moon_visualization_shells.py - Lunar interior and exosphere shell traces.\n'
        '\n'
        'Sphere shells for the Moon: inner core, outer core, mantle, crust,\n'
        'tenuous exosphere, and Hill sphere. All sphere-only -- no custom geometry.\n'
        'Candidate for full migration to shell_configs.py (no custom functions needed).\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'neptune_visualization_shells': (
        'neptune_visualization_shells.py - Neptune interior, ring, and magnetosphere shell traces.\n'
        '\n'
        'Sphere shells for Neptune\'s interior (core, mantle, clouds). Custom geometry\n'
        'for the ring system, tilted magnetosphere (47 degrees from rotation axis),\n'
        'magnetic field lines, and radiation belts. Neptune\'s offset dipole creates\n'
        'one of the most complex magnetospheres in the solar system.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'orbital_param_viz': (
        'orbital_param_viz.py - Interactive orbital element visualization tool.\n'
        '\n'
        'Standalone Tkinter GUI that shows how the six Keplerian orbital elements\n'
        '(a, e, i, omega, Omega, M) transform a circle into a 3D orbit. Step-by-step\n'
        'construction with animated arcs, coordinate frames, and angle annotations.\n'
        'Educational companion to the main orrery -- helps users understand what\n'
        'osculating elements mean geometrically.\n'
        '\n'
        'Key functions:\n'
        '    create_orbital_transformation_viz() - Build the step-by-step 3D figure\n'
        '    create_eccentricity_demo_window() - Interactive e slider demonstration\n'
        '    create_orbital_viz_window() - Main GUI window with object selector\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'planet9_visualization_shells': (
        'planet9_visualization_shells.py - Hypothetical Planet 9 shell traces.\n'
        '\n'
        'Sphere shells for Planet 9: estimated surface and Hill sphere only.\n'
        'Based on Batygin & Brown (2016) orbital predictions. All sphere-only --\n'
        'fully archivable once shell_configs.py migration is complete.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'plot_data_exchange': (
        'plot_data_exchange.py - JSON data exchange between subprocess scripts and GUI.\n'
        '\n'
        'Saves plot data (star counts, processing times, mode settings) to a JSON\n'
        'file that the main GUI reads to populate the report widget. Bridge between\n'
        'standalone HR diagram scripts (which run as subprocesses) and the star\n'
        'visualization GUI.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'plot_data_report_widget': (
        'plot_data_report_widget.py - Embedded report panel for star visualization results.\n'
        '\n'
        'Tkinter widget that displays star counts, magnitude distributions, spectral\n'
        'class breakdowns, and processing times after an HR diagram is generated.\n'
        'Reads data from plot_data_exchange.py. Includes object type analysis via\n'
        'ObjectTypeAnalyzer when available.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'pluto_visualization_shells': (
        'pluto_visualization_shells.py - Pluto interior and atmosphere shell traces.\n'
        '\n'
        'Sphere shells for Pluto: core, mantle, crust, haze layer, atmosphere,\n'
        'and Hill sphere. Based on New Horizons (2015) data. All sphere-only --\n'
        'fully archivable once shell_configs.py migration is complete.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'saturn_visualization_shells': (
        'saturn_visualization_shells.py - Saturn interior, ring, and magnetosphere shell traces.\n'
        '\n'
        'Sphere shells for Saturn\'s interior (core through cloud layer). Custom\n'
        'geometry for the ring system (A, B, C, D, F, G, E rings with Cassini\n'
        'Division), Enceladus plasma torus, radiation belts, and magnetosphere.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'solar_visualization_shells': (
        'solar_visualization_shells.py - Sun interior, corona, and heliosphere shell traces.\n'
        '\n'
        'The largest shell module: 14 sphere shells from core to gravitational\n'
        'influence boundary, plus custom geometry for Hills Cloud torus, Oort Cloud\n'
        'clumpy distribution, and galactic tide shell. Includes the v3.18 solar\n'
        'shell refactor: single-info-marker pattern, n_points=20/25, and the\n'
        'three inner corona shells (Streamer Belt, Roche Limit, Alfven Surface)\n'
        'added for the MAPS comet coronal journey.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher),\n'
        '             palomas_orrery.py (hover_text_sun import)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'star_properties': (
        'star_properties.py - SIMBAD stellar property queries with local caching.\n'
        '\n'
        'Fetches detailed stellar properties (spectral type, magnitudes, identifiers)\n'
        'from SIMBAD for individual stars, caching results locally to avoid repeated\n'
        'queries. Handles both old and new SIMBAD API column name formats.\n'
        '\n'
        'Key functions:\n'
        '    query_simbad_for_star_properties() - Batch query with cache\n'
        '    load_existing_properties() - Load from local pickle cache\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'uranus_visualization_shells': (
        'uranus_visualization_shells.py - Uranus interior, ring, and magnetosphere shell traces.\n'
        '\n'
        'Sphere shells for Uranus interior (core, mantle, clouds). Custom geometry\n'
        'for the ring system, radiation belts, tilted magnetosphere (59 degrees\n'
        'from rotation axis), and Hill sphere. Uranus rotates nearly on its side,\n'
        'making its magnetosphere geometry unique.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'venus_visualization_shells': (
        'venus_visualization_shells.py - Venus interior and atmosphere shell traces.\n'
        '\n'
        'Sphere shells for Venus: core, mantle, crust, dense atmosphere, upper\n'
        'atmosphere, induced magnetosphere, and Hill sphere. Venus has no intrinsic\n'
        'magnetic field; its induced magnetosphere results from solar wind\n'
        'interaction with the ionosphere.\n'
        '\n'
        'Consumed by: planet_visualization.py (routing dispatcher)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    # ============================================================
    # WEAK DOCSTRING GROUP (21 modules)
    # ============================================================

    'constants_new': (
        'constants_new.py - Central constants, parameters, and object catalogs for the orrery.\n'
        '\n'
        'The project\'s single source of truth for physical constants (KM_PER_AU,\n'
        'solar radii, planetary radii), object type mappings, color palettes, orbital\n'
        'period tables, spectral class data, and the master lists of planets, moons,\n'
        'comets, asteroids, and spacecraft with their Horizons IDs and orbital elements.\n'
        'Nearly every module in the project imports from this file.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'data_processing': (
        'data_processing.py - Star catalog data cleaning, merging, and analysis.\n'
        '\n'
        'Processes raw Hipparcos and Gaia catalog data: coordinate system alignment,\n'
        'magnitude estimation, distance calculation, deduplication, and outlier\n'
        'detection. Produces the cleaned combined tables used by HR diagram and\n'
        'planetarium visualization pipelines.\n'
        '\n'
        'Key functions:\n'
        '    calculate_distances() - Parallax to light-year conversion\n'
        '    align_coordinate_systems() - ICRS/Hipparcos frame alignment\n'
        '    select_stars_by_magnitude() - Apply magnitude/distance cuts\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'hr_diagram_apparent_magnitude': (
        'hr_diagram_apparent_magnitude.py - HR diagram pipeline for apparent magnitude queries.\n'
        '\n'
        'Standalone script (runs as subprocess from star_visualization_gui.py).\n'
        'Fetches stars from Hipparcos and Gaia by apparent magnitude limit,\n'
        'processes through data_processing.py, builds 2D HR diagram via\n'
        'visualization_2d.py. Results passed back via plot_data_exchange.py.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'hr_diagram_distance': (
        'hr_diagram_distance.py - HR diagram pipeline for distance-based queries.\n'
        '\n'
        'Standalone script (runs as subprocess from star_visualization_gui.py).\n'
        'Fetches stars from Hipparcos and Gaia within a distance limit in\n'
        'light-years, processes through data_processing.py, builds 2D HR diagram\n'
        'via visualization_2d.py. Results passed back via plot_data_exchange.py.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'idealized_orbits': (
        'idealized_orbits.py - Keplerian orbit ellipse construction and satellite orbit models.\n'
        '\n'
        'Computes and plots idealized (Keplerian) orbit paths from orbital elements,\n'
        'with osculating element support for high-accuracy visualization. Handles\n'
        'elliptical, parabolic, and hyperbolic orbits. Includes specialized models\n'
        'for planetary satellite systems (Mars, Jupiter, Saturn, Uranus, Neptune)\n'
        'with proper parent-body-relative coordinate transforms.\n'
        '\n'
        'The largest computation module (~6,100 lines). Consumed by palomas_orrery.py\n'
        'for both plot_objects and animate_objects orbit rendering.\n'
        '\n'
        'Key functions:\n'
        '    plot_idealized_orbits() - Master orbit renderer for all object types\n'
        '    add_mean_orbit_trace() - Simple Keplerian ellipse from mean elements\n'
        '    calculate_*_satellite_elements() - Per-system satellite orbit models\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'messier_catalog': (
        'messier_catalog.py - Static catalog of Messier objects and bright deep-sky objects.\n'
        '\n'
        'Dictionary-based catalogs of Messier objects (M1-M110), bright open clusters,\n'
        'bright planetary nebulae, and bright emission nebulae. Each entry includes\n'
        'name, type, visual magnitude, distance, coordinates, and observing notes.\n'
        'Data source for the star visualization 3D planetarium views.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'messier_object_data_handler': (
        'messier_object_data_handler.py - Messier object coordinate transforms and data preparation.\n'
        '\n'
        'Converts Messier catalog entries from RA/Dec to Cartesian coordinates for\n'
        '3D visualization. Handles both distance-based and magnitude-based queries.\n'
        'Adds hover text with observing notes from star_notes.py. Produces pandas\n'
        'DataFrames consumed by visualization_3d.py for planetarium rendering.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'palomas_orrery': (
        'palomas_orrery.py - Main GUI and plotting engine for Paloma\'s Orrery.\n'
        '\n'
        'The central application: Tkinter GUI with object selection, date controls,\n'
        'and two primary rendering pipelines -- plot_objects() for static 3D scenes\n'
        'and animate_objects() for animated sequences. Integrates JPL Horizons\n'
        'ephemeris data, osculating orbital elements, spacecraft encounters, comet\n'
        'tails, shell visualizations, and the celestial sphere into interactive\n'
        'Plotly figures.\n'
        '\n'
        'At ~8,600 lines this is the project monolith. Key internal functions:\n'
        '    plot_objects() - Static 3D solar system rendering (~line 3900)\n'
        '    animate_objects() - Animated rendering with frames (~line 5744)\n'
        '    fetch_position() - JPL Horizons position query (~line 1531)\n'
        '    calculate_axis_range_from_orbits() - Scale-aware axis fitting (~line 602)\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'palomas_orrery_helpers': (
        'palomas_orrery_helpers.py - Support functions extracted from the main orrery monolith.\n'
        '\n'
        'Trajectory fetching, orbit path backup/restore, URL button construction,\n'
        'camera presets, Planet 9 analytical position calculation, and the _info\n'
        'string imports for shell tooltip text. Originally created to reduce\n'
        'palomas_orrery.py file size.\n'
        '\n'
        'Key functions:\n'
        '    fetch_trajectory() - Multi-segment Horizons trajectory fetch\n'
        '    add_url_buttons() - Plotly updatemenus for JPL/NASA links\n'
        '    get_default_camera() - Standard camera position dict\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'planetarium_distance': (
        'planetarium_distance.py - 3D star field pipeline for distance-based queries.\n'
        '\n'
        'Standalone script (runs as subprocess from star_visualization_gui.py).\n'
        'Fetches stars within a distance limit, processes through data_processing.py,\n'
        'builds 3D stellar neighborhood visualization via visualization_3d.py.\n'
        'Results passed back via plot_data_exchange.py.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'shared_utilities': (
        'shared_utilities.py - Small shared helpers used across shell visualization modules.\n'
        '\n'
        'Currently contains create_sun_direction_indicator(), which adds a visual\n'
        'arrow showing the Sun\'s direction in body-centered plots. Used by most\n'
        'planetary shell modules when the center body is not the Sun.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'shutdown_handler': (
        'shutdown_handler.py - Graceful shutdown and safe figure display for Plotly.\n'
        '\n'
        'Manages thread cleanup on application exit and provides show_figure_safely(),\n'
        'which opens Plotly figures in the browser with proper temp file handling\n'
        'and optional save-to-file dialog. Wraps save_utils.show_and_save().\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'star_notes': (
        'star_notes.py - Curated hover text annotations for notable stars.\n'
        '\n'
        'Dictionary mapping SIMBAD identifiers to HTML-formatted descriptive text\n'
        'for ~200 notable stars. Includes historical names, physical properties,\n'
        'binary/multiple system notes, and cultural significance. Displayed as\n'
        'hover text in HR diagrams and 3D star visualizations.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'star_visualization_gui': (
        'star_visualization_gui.py - Stellar visualization GUI for Paloma\'s Orrery.\n'
        '\n'
        'Tkinter interface for HR diagrams (2D), 3D stellar neighborhoods, and\n'
        'planetarium views. Launches hr_diagram_*.py and planetarium_*.py as\n'
        'subprocesses, displays results via plot_data_report_widget.py. Supports\n'
        'magnitude-based and distance-based queries with lazy-loaded star property\n'
        'details.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'star_visualization_gui_before_pyinstaller_refactor': (
        'star_visualization_gui_before_pyinstaller_refactor.py - Pre-PyInstaller version of the star GUI.\n'
        '\n'
        'Archived copy of star_visualization_gui.py before the PyInstaller\n'
        'packaging refactor. Kept as reference. Use star_visualization_gui.py\n'
        'for active development.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'stellar_data_patches': (
        'stellar_data_patches.py - Manual corrections for stars with known bad catalog data.\n'
        '\n'
        'Small patch table mapping HIP numbers to corrected temperature, luminosity,\n'
        'and spectral type values. Applied after catalog processing to fix stars\n'
        'where automated pipelines produce incorrect results (e.g., Mizar).\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'stellar_parameters': (
        'stellar_parameters.py - Stellar temperature and parameter estimation from spectral types.\n'
        '\n'
        'Converts spectral type strings (e.g., "G2V", "M3III") to effective\n'
        'temperatures using lookup tables from constants_new.py. Handles B-V\n'
        'color index temperature estimation as fallback. Used by the HR diagram\n'
        'pipeline when catalog temperatures are missing.\n'
        '\n'
        'Key functions:\n'
        '    estimate_temperature_from_spectral_type() - Spectral type to Teff\n'
        '    calculate_bv_temperature() - B-V color to Teff fallback\n'
        '    select_best_temperature() - Pick best available Teff source\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'visualization_2d': (
        'visualization_2d.py - 2D HR diagram (color-magnitude) plot builder.\n'
        '\n'
        'Creates Hertzsprung-Russell diagrams from processed star data: temperature\n'
        'vs. luminosity scatter plots with spectral class coloring, hover text with\n'
        'stellar properties, and statistical annotation. The 2D counterpart to\n'
        'visualization_3d.py. Output displayed in browser via Plotly.\n'
        '\n'
        'Key functions:\n'
        '    create_hr_diagram() - Main HR diagram figure builder\n'
        '    prepare_2d_data() - Data preparation and filtering\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'visualization_3d': (
        'visualization_3d.py - 3D stellar neighborhood and planetarium plot builder.\n'
        '\n'
        'Creates 3D scatter plots of stars in Cartesian coordinates (light-years or\n'
        'parsecs) with spectral class coloring, Messier object overlays, and notable\n'
        'star annotations. Includes the Sun at origin. The 3D counterpart to\n'
        'visualization_2d.py.\n'
        '\n'
        'Key functions:\n'
        '    create_3d_visualization() - Main 3D star field figure builder\n'
        '    prepare_3d_data() - Coordinate transforms and data preparation\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'visualization_core': (
        'visualization_core.py - Shared data preparation and formatting for star visualizations.\n'
        '\n'
        'Common functions used by both visualization_2d.py and visualization_3d.py:\n'
        'temperature-to-color mapping, star count analysis, magnitude distribution\n'
        'statistics, and hover text formatting. Extracted to avoid duplication\n'
        'between the 2D and 3D pipelines.\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),

    'visualization_utils': (
        'visualization_utils.py - Shared Plotly utilities for orrery and star visualizations.\n'
        '\n'
        'Interactive figure controls used by both plot_objects and animate_objects:\n'
        'hover toggle buttons, camera center/look-at/fly-to buttons, and the\n'
        'format_detailed_hover_text() builder for orrery object hover strings.\n'
        'Also contains _calculate_grid_dtick() for scale-aware axis tick spacing.\n'
        '\n'
        'Key functions:\n'
        '    format_detailed_hover_text() - Full hover string for orrery objects\n'
        '    add_hover_toggle_buttons() - Show/hide hover text toggle\n'
        '    add_fly_to_object_buttons() - Camera fly-to dropdown\n'
        '    _calculate_grid_dtick() - Auto-dtick from axis span\n'
        '\n'
        'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6'
    ),
}


# ============================================================
# INSERTION LOGIC
# ============================================================

def detect_line_ending(content_bytes):
    """Detect whether file uses CRLF or LF."""
    if b'\r\n' in content_bytes:
        return b'\r\n'
    return b'\n'


def has_existing_docstring(content_bytes):
    """Check if file starts with a docstring (triple quotes)."""
    text = content_bytes.lstrip()
    return text.startswith(b'"""') or text.startswith(b"'''")


def has_leading_comment(content_bytes):
    """Check if file starts with # comments (before imports)."""
    text = content_bytes.lstrip()
    return text.startswith(b'#')


def insert_docstring(content_bytes, docstring_text, line_ending):
    """Insert or replace the module docstring.

    Two fixes over the original, both found during L-163 Phase 1:

    1. An existing docstring is located by PARSING (find_docstring_lines)
       rather than by scanning for the first literal triple-quote. The
       old scan could not tell a real module docstring from a quoted
       string sitting in a comment above it.
    2. When there is no docstring, the new one now goes BELOW any shebang
       or leading comment block -- has_leading_comment() existed for
       exactly this and was never called, so a shebang-first module like
       ledger_index.py would have had the docstring inserted ABOVE
       `#!/usr/bin/env python3`, silently disabling it.
    """
    nl = line_ending
    text = _decode_source(content_bytes)
    lines = text.split('\n')
    doc_lines = ('"""\n' + docstring_text + '\n"""').split('\n')

    span = find_docstring_lines(text)
    if span is not None:
        start, end, _ = span
        lines = lines[:start] + doc_lines + lines[end + 1:]
    elif has_leading_comment(content_bytes):
        # Walk past the shebang / comment header, then back off any blank
        # lines so the docstring sits directly under it.
        at = 0
        while at < len(lines) and (lines[at].lstrip().startswith('#')
                                   or lines[at].strip() == ''):
            at += 1
        while at > 0 and lines[at - 1].strip() == '':
            at -= 1
        lines = lines[:at] + [''] + doc_lines + lines[at:]
    else:
        lines = doc_lines + lines

    out = '\n'.join(lines)
    if nl != b'\n':
        out = out.replace('\n', nl.decode('ascii'))
    return out.encode('utf-8')


def process_module(project_dir, module_name, docstring_text, write=False):
    """Process a single module: read, insert docstring, optionally write."""
    filepath = os.path.join(project_dir, module_name + '.py')
    if not os.path.exists(filepath):
        print(f"  SKIP {module_name}.py -- file not found")
        return False

    with open(filepath, 'rb') as f:
        content = f.read()

    line_ending = detect_line_ending(content)
    new_content = insert_docstring(content, docstring_text, line_ending)

    if new_content == content:
        print(f"  SKIP {module_name}.py -- no change needed")
        return False

    if write:
        with open(filepath, 'wb') as f:
            f.write(new_content)
        print(f"  WROTE {module_name}.py")
    else:
        # Preview: show first 5 lines of docstring
        preview = docstring_text.split('\n')[0]
        print(f"  PREVIEW {module_name}.py -- {preview}")

    return True


# ============================================================
# ROLE / DOMAIN TAG SWEEP  (L-163 Phase 2)
# ============================================================
# Inserts an explicit two-line metadata block into each module's
# EXISTING docstring -- it does not rewrite the docstring:
#
#     Role: <one of ROLE_VOCAB>
#     Domain: <one of the repo's domain vocabulary>
#
# Placement: directly above the 'Module updated:' credit line, blank-
# line separated. Modules with no credit line get the block at the end
# of the docstring instead. Re-running updates an existing block in
# place rather than adding a second one.
#
# Keys are repo-relative paths, so the orrery's flat modules and the
# gallery's nested ones share one table with no collision risk.
# __init__.py package markers are exempt (design Section 3).

ROLE_VOCAB = (
    'gui', 'rendering', 'rendering/shells', 'computation', 'data',
    'cache', 'pipeline', 'scenario', 'utility', 'devtool', 'legacy',
    'other',
)

DOMAIN_VOCAB = (
    # orrery repo
    'orrery', 'earth_science', 'gallery', 'stars', 'utilities',
    'dev_tools',
    # gallery repo
    'gallery_pipeline', 'cache_builder', 'assembler',
)

# Which directories to sweep, relative to the repo root.
# Orrery copy: ['.']  Gallery copy: the four module directories.
SCAN_PATHS = ['.']
# SCAN_PATHS = ['.', 'tools', 'gallery/assembler',
#               'gallery/assembler/harness', 'gallery/assembler/tests']

# Bare (no-slash) MODULE_TAGS keys that belong to the GALLERY repo's root
# scan specifically. Needed because both copies now scan '.', and the
# orrery repo is entirely flat (every bare key belongs to it, no list
# needed) -- without this, every one of the orrery's ~114 bare-name
# entries would falsely appear to "belong" to the gallery root too,
# since both copies share one MODULE_TAGS table. Add to this set (and
# to MODULE_TAGS) if another root-level gallery tool is added later.
GALLERY_ROOT_FILES = {'add_docstrings.py'}

MODULE_TAGS = {

    # ---------- orrery repo (114 modules) ----------
    # Source: MAP = migrated from the existing ROLE_MAP /
    # MODULE_DOMAIN_MAP; HEUR = the _shells suffix heuristic, now made
    # explicit; NEW = classified this session, listed in the Phase 2
    # as-built for Tony's review.
    'add_docstrings.py':                        ('devtool', 'dev_tools'),
    'apsidal_markers.py':                       ('computation', 'orrery'),
    'asteroid_belt_visualization_shells.py':    ('rendering/shells', 'orrery'),   # HEUR/MAP
    'catalog_selection.py':                     ('computation', 'stars'),   # MAP/NEW
    'celestial_coordinates.py':                 ('computation', 'orrery'),
    'celestial_objects.py':                     ('data', 'orrery'),
    'climate_cache_manager.py':                 ('cache', 'earth_science'),
    'close_approach_data.py':                   ('data', 'orrery'),
    'comet_visualization_shells.py':            ('rendering/shells', 'orrery'),   # HEUR/MAP
    'constants_new.py':                         ('data', 'orrery'),
    'convert_hot_ph_to_json.py':                ('devtool', 'dev_tools'),
    'coordinate_system_guide.py':               ('computation', 'orrery'),
    'create_cache_backups.py':                  ('devtool', 'dev_tools'),
    'create_ephemeris_database.py':             ('devtool', 'dev_tools'),
    'data_acquisition.py':                      ('computation', 'stars'),   # CHANGED (was orrery)
    'data_acquisition_distance.py':             ('computation', 'stars'),   # CHANGED (was orrery)
    'data_inventory.py':                        ('devtool', 'dev_tools'),   # NEW/MAP
    'data_processing.py':                       ('computation', 'stars'),   # MAP/NEW
    'dep_trace.py':                             ('devtool', 'dev_tools'),
    'diagnose_bcodmo.py':                       ('devtool', 'dev_tools'),
    'earth_system_common.py':                   ('utility', 'earth_science'),   # NEW/NEW
    'earth_system_controller.py':               ('gui', 'earth_science'),   # MAP/NEW
    'earth_system_generator.py':                ('devtool', 'earth_science'),   # CHANGED (was computation)
    'earth_system_visualization_gui.py':        ('gui', 'earth_science'),   # MAP/NEW
    'earth_visualization_shells.py':            ('rendering/shells', 'earth_science'),   # HEUR/MAP
    'energy_imbalance.py':                      ('computation', 'earth_science'),
    'eris_visualization_shells.py':             ('rendering/shells', 'orrery'),   # HEUR/MAP
    'examine_hot_csv.py':                       ('devtool', 'dev_tools'),
    'exoplanet_coordinates.py':                 ('data', 'stars'),
    'exoplanet_orbits.py':                      ('rendering', 'stars'),
    'exoplanet_stellar_properties.py':          ('data', 'stars'),
    'exoplanet_systems.py':                     ('data', 'stars'),
    'export_orbit_cache.py':                    ('devtool', 'dev_tools'),   # NEW/MAP
    'fetch_climate_data.py':                    ('computation', 'earth_science'),
    'fetch_paleoclimate_data.py':               ('computation', 'earth_science'),
    'food_insecurity_generator.py':             ('devtool', 'earth_science'),   # NEW/MAP, CHANGED (was computation)
    'formatting_utils.py':                      ('utility', 'utilities'),
    'hr_diagram_apparent_magnitude.py':         ('rendering', 'stars'),
    'hr_diagram_distance.py':                   ('rendering', 'stars'),
    'idealized_orbits.py':                      ('computation', 'orrery'),
    'incremental_cache_manager.py':             ('cache', 'stars'),   # MAP/NEW
    'info_dictionary.py':                       ('data', 'orrery'),
    'jupiter_visualization_shells.py':          ('rendering/shells', 'orrery'),   # HEUR/MAP
    'ledger_index.py':                          ('devtool', 'dev_tools'),   # NEW/MAP
    'mars_visualization_shells.py':             ('rendering/shells', 'orrery'),   # HEUR/MAP
    'measure_animation_html.py':                ('devtool', 'dev_tools'),   # NEW/NEW
    'measure_perframe_elements.py':             ('devtool', 'dev_tools'),   # NEW/MAP
    'mercury_visualization_shells.py':          ('rendering/shells', 'orrery'),   # HEUR/MAP
    'messier_catalog.py':                       ('data', 'stars'),
    'messier_object_data_handler.py':           ('pipeline', 'stars'),
    'module_atlas.py':                          ('devtool', 'dev_tools'),
    'moon_visualization_shells.py':             ('rendering/shells', 'orrery'),   # HEUR/MAP
    'neptune_visualization_shells.py':          ('rendering/shells', 'orrery'),   # HEUR/MAP
    'object_type_analyzer.py':                  ('computation', 'orrery'),
    'orbit_data_manager.py':                    ('cache', 'orrery'),
    'orbital_elements.py':                      ('computation', 'orrery'),
    'orbital_param_viz.py':                     ('gui', 'orrery'),   # MAP/NEW
    'orrery_rendering.py':                      ('rendering', 'orrery'),   # NEW/NEW
    'osculating_cache_manager.py':              ('cache', 'orrery'),
    'paleoclimate_dual_scale.py':               ('rendering', 'earth_science'),
    'paleoclimate_human_origins_full.py':       ('rendering', 'earth_science'),
    'paleoclimate_visualization.py':            ('rendering', 'earth_science'),
    'paleoclimate_visualization_full.py':       ('rendering', 'earth_science'),
    'paleoclimate_wet_bulb_full.py':            ('rendering', 'earth_science'),
    'palomas_orrery.py':                        ('gui', 'orrery'),
    'palomas_orrery_dashboard.py':              ('gui', 'orrery'),
    'palomas_orrery_helpers.py':                ('utility', 'orrery'),   # MAP/NEW
    'planet9_visualization_shells.py':          ('rendering/shells', 'orrery'),   # HEUR/MAP
    'planet_visualization.py':                  ('rendering', 'orrery'),   # MAP/NEW
    'planet_visualization_utilities.py':        ('rendering', 'orrery'),
    'planetarium_apparent_magnitude.py':        ('rendering', 'stars'),
    'planetarium_distance.py':                  ('rendering', 'stars'),
    'plot_data_exchange.py':                    ('pipeline', 'utilities'),
    'plot_data_report_widget.py':               ('rendering', 'utilities'),
    'pluto_visualization_shells.py':            ('rendering/shells', 'orrery'),   # HEUR/MAP
    'provenance_scanner.py':                    ('devtool', 'dev_tools'),
    'report_manager.py':                        ('utility', 'utilities'),
    'saturn_visualization_shells.py':           ('rendering/shells', 'orrery'),   # HEUR/MAP
    'save_utils.py':                            ('pipeline', 'utilities'),
    'scenarios_coral_bleaching.py':             ('scenario', 'earth_science'),
    'scenarios_food_insecurity.py':             ('scenario', 'earth_science'),   # NEW/NEW
    'scenarios_heatwaves.py':                   ('scenario', 'earth_science'),
    'scenarios_western_heatwave_march_2026.py': ('scenario', 'earth_science'),
    'sgr_a_grand_tour.py':                      ('rendering', 'orrery'),
    'sgr_a_star_data.py':                       ('data', 'orrery'),
    'sgr_a_visualization_animation.py':         ('rendering', 'orrery'),
    'sgr_a_visualization_core.py':              ('rendering', 'orrery'),
    'sgr_a_visualization_core_arcs.py':         ('pipeline', 'orrery'),
    'sgr_a_visualization_precession.py':        ('rendering', 'orrery'),
    'shared_utilities.py':                      ('utility', 'utilities'),
    'shell_configs.py':                         ('data', 'orrery'),   # NEW/NEW
    'shutdown_handler.py':                      ('utility', 'utilities'),   # MAP/NEW
    'simbad_manager.py':                        ('computation', 'stars'),
    'skills_index.py':                          ('devtool', 'dev_tools'),   # NEW/MAP
    'social_media_export.py':                   ('pipeline', 'gallery'),
    'solar_visualization_shells.py':            ('rendering/shells', 'orrery'),   # HEUR/MAP
    'spacecraft_encounters.py':                 ('data', 'orrery'),
    'star_notes.py':                            ('data', 'stars'),
    'star_properties.py':                       ('data', 'stars'),
    'star_sphere_builder.py':                   ('rendering', 'stars'),
    'star_visualization_gui.py':                ('gui', 'stars'),   # MAP/NEW
    'stellar_data_patches.py':                  ('data', 'stars'),
    'stellar_parameters.py':                    ('data', 'stars'),
    'test_constants_provenance.py':             ('devtool', 'dev_tools'),
    'test_orbit_cache.py':                      ('devtool', 'dev_tools'),
    'test_reset_completeness.py':               ('devtool', 'dev_tools'),   # NEW/MAP
    'uranus_visualization_shells.py':           ('rendering/shells', 'orrery'),   # HEUR/MAP
    'venus_visualization_shells.py':            ('rendering/shells', 'orrery'),   # HEUR/MAP
    'verify_orbit_cache.py':                    ('devtool', 'dev_tools'),
    'visualization_2d.py':                      ('rendering', 'stars'),
    'visualization_3d.py':                      ('rendering', 'stars'),
    'visualization_core.py':                    ('rendering', 'stars'),
    'visualization_utils.py':                   ('rendering', 'stars'),
    'vot_cache_manager.py':                     ('cache', 'stars'),   # MAP/NEW

    # ---------- gallery repo (22 modules) ----------
    # Roles classified this session; domains from design Section 11.
    'gallery/assembler/assemble.py':                   ('pipeline', 'assembler'),   # NEW/S11
    'gallery/assembler/cache_reader.py':               ('cache', 'assembler'),   # NEW/S11
    'gallery/assembler/catalog.py':                    ('data', 'assembler'),   # NEW/S11
    'gallery/assembler/errors.py':                     ('utility', 'assembler'),   # NEW/S11
    'gallery/assembler/harness/fingerprint.py':        ('devtool', 'dev_tools'),   # NEW/S11
    'gallery/assembler/models.py':                     ('data', 'assembler'),   # NEW/S11
    'gallery/assembler/presentation.py':               ('rendering', 'assembler'),   # NEW/S11
    'gallery/assembler/render_events.py':              ('rendering', 'assembler'),   # NEW/S11
    'gallery/assembler/render_objects.py':             ('rendering', 'assembler'),   # NEW/S11
    'gallery/assembler/render_orbits.py':              ('rendering', 'assembler'),   # NEW/S11
    'gallery/assembler/render_spacecraft.py':          ('rendering', 'assembler'),   # NEW/S11
    'gallery/assembler/resolver.py':                   ('computation', 'assembler'),   # NEW/S11
    'gallery/assembler/tests/test_artifact1_earth.py': ('devtool', 'dev_tools'),   # NEW/S11
    'tools/debug_encke_tp.py':                         ('devtool', 'dev_tools'),   # NEW/S11
    'tools/gallery_cache_builder.py':                  ('cache', 'cache_builder'),   # NEW/S11
    'tools/gallery_cleanup.py':                        ('devtool', 'cache_builder'),   # NEW/S11
    'tools/gallery_editor.py':                         ('devtool', 'gallery_pipeline'),   # CHANGED (was gui)
    'tools/gallery_json_fixer.py':                     ('devtool', 'gallery_pipeline'),   # CHANGED (was pipeline)
    'tools/gallery_studio.py':                         ('devtool', 'gallery_pipeline'),   # CHANGED (was gui)
    'tools/inspect_staging.py':                        ('devtool', 'dev_tools'),   # NEW/S11
    'tools/json_converter.py':                         ('devtool', 'gallery_pipeline'),   # CHANGED (was pipeline)
    'tools/test_gallery_cache_builder_offline.py':     ('devtool', 'dev_tools'),   # NEW/S11
}


def _decode_source(content_bytes):
    """Decode a module to text with LF endings for line-wise editing."""
    text = content_bytes.decode('utf-8')
    return text.replace('\r\n', '\n')


def find_docstring_lines(text):
    """Locate the module docstring by PARSING, not by scanning for quotes.

    Returns (start_index, end_index, quote) as 0-based line indexes into
    text.split('\n'), or None if the module has no docstring. Parsing is
    what makes this correct for shebang-first and comment-first modules --
    the old scan-for-the-first-triple-quote approach could not tell a
    module docstring from a string appearing earlier in a comment.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return None
    if not tree.body:
        return None
    node = tree.body[0]
    if not isinstance(node, ast.Expr):
        return None
    value = node.value
    if not isinstance(value, ast.Constant) or not isinstance(value.value, str):
        return None
    lines = text.split('\n')
    opener = lines[value.lineno - 1]
    quote = '"""' if '"""' in opener else "'''"
    return (value.lineno - 1, value.end_lineno - 1, quote)


def find_insert_point(lines, start, end):
    """Decide where the tag block goes inside an existing docstring.

    Returns (index, needs_blank_before). The rule, per the Phase 2
    decision: directly above the credit line when there is EXACTLY ONE
    'Module updated:' line. Zero credit lines, or more than one (a
    changelog docstring), both go at the very end of the docstring,
    just above its closing quotes -- Tony's call (chat, July 2026):
    wedging the block between two changelog entries read worse than
    putting it after the whole history, so a changelog is treated the
    same as having no credit line at all.
    """
    hits = [i for i in range(start, end + 1)
            if lines[i].lstrip().startswith(CREDIT_PREFIX)]
    if len(hits) == 1:
        i = hits[0]
        return i, lines[i - 1].strip() != ''
    return end, lines[end - 1].strip() != ''


def strip_existing_tags(lines, start, end):
    """Remove an existing Role:/Domain: PAIR already inside the docstring.

    Makes the sweep idempotent: a second run updates the block in place
    instead of stacking a second copy underneath the first.

    Deliberately strict: strips only two ADJACENT lines shaped exactly
    like 'Role: <x>' immediately followed by 'Domain: <y>' -- the pair
    this script always writes together -- never a single line that
    merely starts with the word "Role:" or "Domain:" on its own. A lone
    such line can be ordinary prose (documentation ABOUT the tag format,
    for instance) and must be left alone.

    Bug found in the wild (July 2026): this file's own docstring had a
    wrapped sentence starting "Domain: lines -- this legacy mode..." --
    plain prose, not a tag. The earlier single-line version of this
    function matched that line in isolation and deleted it. Requiring
    the adjacent pair fixes this: a lone Role:-or-Domain:-looking line
    with no matching partner right next to it is never touched.
    """
    keep = []
    removed = 0
    seam = None
    i = start
    for j in range(0, start):
        keep.append(lines[j])
    while i <= end:
        line = lines[i]
        is_pair = (i < end
                   and re.match(r'^\s*Role:\s', line)
                   and re.match(r'^\s*Domain:\s', lines[i + 1]))
        if is_pair:
            if seam is None:
                seam = len(keep)
            removed += 2
            i += 2
            continue
        keep.append(line)
        i += 1
    for j in range(end + 1, len(lines)):
        keep.append(lines[j])
    if removed and seam is not None and 0 < seam < len(keep):
        # Taking the block out can leave the blank line above it sitting
        # directly on the blank line below it. Collapse that one seam --
        # and only that seam -- so a re-run reproduces the file byte for
        # byte instead of growing a blank line each time.
        if keep[seam - 1].strip() == '' and keep[seam].strip() == '':
            del keep[seam]
    return keep, removed


def expand_single_line_docstring(lines, start, quote):
    """Convert \"\"\"one-liner.\"\"\" into an openable multi-line docstring.

    Three modules use the one-line form. Rather than skip them, give them
    the same shape as everything else so the tag block lands consistently.
    """
    body = lines[start].strip()
    inner = body[len(quote):-len(quote)]
    indent = lines[start][:len(lines[start]) - len(lines[start].lstrip())]
    return [indent + quote + inner, indent + quote]


def insert_tags(content_bytes, role, domain, line_ending):
    """Insert or refresh the Role:/Domain: block inside the docstring.

    Everything outside the docstring is left byte-identical; inside it,
    only the tag block and its blank-line separator are touched.
    """
    text = _decode_source(content_bytes)
    span = find_docstring_lines(text)
    if span is None:
        return None, 'no docstring'
    start, end, quote = span
    lines = text.split('\n')

    if start == end:
        expanded = expand_single_line_docstring(lines, start, quote)
        lines = lines[:start] + expanded + lines[start + 1:]
        end = start + 1

    lines, removed = strip_existing_tags(lines, start, end)
    end -= removed

    point, needs_blank = find_insert_point(lines, start, end)
    block = ['Role: ' + role, 'Domain: ' + domain]
    if needs_blank:
        block = [''] + block
    if lines[point].lstrip().startswith(CREDIT_PREFIX):
        block = block + ['']

    lines = lines[:point] + block + lines[point:]
    out = '\n'.join(lines)
    if line_ending != b'\n':
        out = out.replace('\n', line_ending.decode('ascii'))
    action = 'updated' if removed else 'added'
    return out.encode('utf-8'), action


def iter_tag_targets(project_dir):
    """Yield (relative_path, absolute_path) for every module to sweep.

    Walks only SCAN_PATHS -- no recursion -- so the gallery copy reaches
    its four module directories without dragging in anything else.
    __init__.py package markers are skipped by design.
    """
    for scan in SCAN_PATHS:
        directory = os.path.join(project_dir, scan)
        if not os.path.isdir(directory):
            print("  WARNING: SCAN_PATHS entry not found: %s" % scan)
            continue
        for name in sorted(os.listdir(directory)):
            if not name.endswith('.py') or name == '__init__.py':
                continue
            full = os.path.join(directory, name)
            if not os.path.isfile(full):
                continue
            rel = name if scan == '.' else scan + '/' + name
            yield rel, full


def count_credit_lines(content_bytes):
    """How many 'Module updated:' lines the docstring carries.

    More than one means a changelog-style docstring, where 'above the
    credit line' is ambiguous. Reported, never silently resolved.
    """
    text = _decode_source(content_bytes)
    span = find_docstring_lines(text)
    if span is None:
        return 0
    start, end, _ = span
    lines = text.split('\n')
    return sum(1 for i in range(start, end + 1)
               if lines[i].lstrip().startswith(CREDIT_PREFIX))


def process_module_tags(rel_path, full_path, write=False):
    """Sweep one module. Returns (status, detail)."""
    tags = MODULE_TAGS.get(rel_path)
    if tags is None:
        return 'unmapped', 'no MODULE_TAGS entry'
    role, domain = tags
    if role not in ROLE_VOCAB:
        return 'bad-role', role
    if domain not in DOMAIN_VOCAB:
        return 'bad-domain', domain

    with open(full_path, 'rb') as handle:
        content = handle.read()
    line_ending = detect_line_ending(content)
    new_content, action = insert_tags(content, role, domain, line_ending)
    if new_content is None:
        return 'no-docstring', action
    if new_content == content:
        return 'unchanged', ''
    if write:
        with open(full_path, 'wb') as handle:
            handle.write(new_content)
    return action, '%s / %s' % (role, domain)


def run_tag_sweep(project_dir, write=False):
    """Phase 2 sweep across SCAN_PATHS. Preview unless write=True.

    Reports the way ledger_index.py does: fix what is mechanically
    knowable, collect everything else into a problems list, and exit
    non-zero so a bad run cannot pass quietly in the VS Code panel.
    """
    label = 'WRITING' if write else 'PREVIEW (nothing written)'
    print('\n' + '=' * 62)
    print('  Role / Domain Tag Sweep -- %s' % label)
    print('  Target: %s' % os.path.abspath(project_dir))
    print('  Scan paths: %s' % ', '.join(SCAN_PATHS))
    print('=' * 62 + '\n')

    counts = {}
    problems = []
    review = []
    seen = set()
    for rel, full in iter_tag_targets(project_dir):
        seen.add(rel)
        with open(full, 'rb') as handle:
            credits = count_credit_lines(handle.read())
        if credits > 1:
            review.append('%s: %d credit lines (changelog docstring)'
                          % (rel, credits))
        status, detail = process_module_tags(rel, full, write=write)
        counts[status] = counts.get(status, 0) + 1
        if status in ('added', 'updated'):
            print('  %-8s %-48s %s' % (status.upper(), rel, detail))
        elif status == 'unchanged':
            print('  %-8s %-48s' % ('SAME', rel))
        else:
            print('  %-8s %-48s %s' % ('PROBLEM', rel, detail))
            problems.append('%s: %s (%s)' % (rel, status, detail))

    expected = set(k for k in MODULE_TAGS if _belongs_to_this_repo(k))
    missing_file = sorted(expected - seen)
    for rel in missing_file:
        problems.append('%s: MODULE_TAGS entry has no file' % rel)

    print('\n' + '-' * 62)
    for key in sorted(counts):
        print('  %-12s %d' % (key, counts[key]))
    print('  %-12s %d' % ('total', sum(counts.values())))

    if review:
        print('\n  CHANGELOG (%d) -- more than one credit line. Per the'
              % len(review))
        print('  Phase 2 placement decision, the tag goes at the very end')
        print('  of the docstring instead of above any single entry:')
        for item in review:
            print('    - %s' % item)

    if problems:
        print('\n  PROBLEMS (%d) -- nothing guessed, each needs a decision:' % len(problems))
        for item in problems:
            print('    - %s' % item)
        print()
        return 1
    print('\n  No problems. Every module in scope carries both tags.\n')
    return 0


def _belongs_to_this_repo(rel_path):
    """True if a MODULE_TAGS key is in scope for the current SCAN_PATHS.

    The table holds both repos so the two copies stay identical; this is
    what keeps the orrery run from reporting every gallery entry as a
    missing file, and vice versa. Now that both copies scan '.', a bare
    (no-slash) key needs a further check: the orrery repo is flat, so
    every bare key genuinely belongs to it (SCAN_PATHS == ['.'] exactly
    identifies that copy). The gallery copy also scans '.', but only for
    its own small GALLERY_ROOT_FILES set -- otherwise every orrery
    bare-name entry would falsely appear to belong here too.
    """
    for scan in SCAN_PATHS:
        if scan == '.':
            if '/' not in rel_path:
                if SCAN_PATHS == ['.']:
                    return True
                return rel_path in GALLERY_ROOT_FILES
        elif rel_path.startswith(scan + '/'):
            if rel_path[len(scan) + 1:].count('/') == 0:
                return True
    return False


# ============================================================
# MAIN
# ============================================================

def confirm_write():
    """Ask whether to actually write the just-previewed changes.

    Only an explicit y/yes answer returns True. A blank Enter, 'n',
    a typo, or even a read error (EOFError) all return False -- silence
    defaults to the safe choice, never to writing.
    """
    try:
        answer = input('\n  Write these changes? [y/n]: ').strip().lower()
    except EOFError:
        answer = ''
    return answer in ('y', 'yes')


def main():
    write_mode = '--write' in sys.argv
    legacy_mode = '--docstrings' in sys.argv
    project_dir = '.'

    # Check for directory argument
    for arg in sys.argv[1:]:
        if arg != '--write' and os.path.isdir(arg):
            project_dir = arg

    if not legacy_mode:
        # Default job is the L-163 Phase 2 tag sweep. --write skips the
        # question and writes immediately (advanced/scripted use); the
        # normal path previews, then asks before writing anything.
        if write_mode:
            sys.exit(run_tag_sweep(project_dir, write=True))
        result = run_tag_sweep(project_dir, write=False)
        if result != 0:
            print('  Fix the problems above, then run again before writing.\n')
            sys.exit(result)
        if confirm_write():
            print()
            sys.exit(run_tag_sweep(project_dir, write=True))
        print('\n  No changes written.\n')
        sys.exit(0)

    # Legacy whole-docstring mode (--docstrings), same preview-then-ask
    # shape as above; --write still skips straight to writing.
    def run_legacy(write):
        mode_label = "WRITING" if write else "PREVIEW (use --write to apply)"
        print(f"\n{'='*60}")
        print(f"  Module Docstring Update -- {mode_label}")
        print(f"  Target: {os.path.abspath(project_dir)}")
        print(f"  Modules to update: {len(DOCSTRINGS)}")
        print(f"{'='*60}\n")

        updated = 0
        skipped = 0
        for module_name, docstring_text in sorted(DOCSTRINGS.items()):
            if process_module(project_dir, module_name, docstring_text, write=write):
                updated += 1
            else:
                skipped += 1

        print(f"\n  {'Updated' if write else 'Would update'}: {updated}")
        print(f"  Skipped: {skipped}")
        print()
        return updated

    if write_mode:
        run_legacy(True)
        return

    updated = run_legacy(False)
    if updated > 0 and confirm_write():
        print()
        run_legacy(True)
    else:
        print('  No changes written.\n')


if __name__ == '__main__':
    main()
