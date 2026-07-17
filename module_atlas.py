"""
module_atlas.py - Codebase encyclopedia generator for Paloma's Orrery

Scans every .py file in the project directory ONCE and produces TWO files
from that single scan, so they can never diverge from each other again
(L-127, July 2026 -- MODULE_INDEX.md was previously hand-maintained and
drifted 4 months out of date with its own wrong module/line counts,
independent of MODULE_ATLAS.md's own auto-regeneration):

  MODULE_ATLAS.md -- the full reference (deep, for AI upload):
    - Module purpose (docstring or leading comment), full text
    - Public functions with their docstrings
    - Line count, role tag, dependencies, consumers
    - Alphabetical quick-reference index

  MODULE_INDEX.md -- the human-browsable index (light, for GitHub):
    - Same role-based grouping, friendlier section titles
    - One row per module: name + docstring-derived description + lines
    - No function lists / dependency graphs -- that's the atlas's job

Both are MECHANICAL extractions only (no AI synthesis step) -- the index
reads only as good as each module's own docstring. That's a deliberate
tradeoff (L-127): thin docstrings get thin index entries, which is a
visible incentive to improve the docstring rather than hand-patch the
index around it.

Both outputs write to the repo ROOT by default, matching where
MODULE_ATLAS.md already lived and fixing README.md's existing
[MODULE_INDEX.md](MODULE_INDEX.md) link at its root cause (the file used
to live in documentation/, where that root-relative link couldn't reach
it).

Usage:
    python module_atlas.py                     # scan current directory,
                                                # write both files to it
    python module_atlas.py /path/to/project    # scan specific directory
    python module_atlas.py --output atlas.md   # custom atlas filename
    python module_atlas.py --index-output idx.md  # custom index filename
    python module_atlas.py --atlas-only        # skip MODULE_INDEX.md
    python module_atlas.py --index-only        # skip MODULE_ATLAS.md

The atlas is designed to be uploaded to a Claude session as a reference
artifact. Ask Claude natural-language questions and it searches the atlas.
The index is designed to be read directly on GitHub.

Note: Scans only the top-level directory (no subdirectories).
      Run from your clean project directory to avoid picking up
      old copies or virtual environment files.

Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-127: single
scan now feeds both MODULE_ATLAS.md and the newly-mechanical
MODULE_INDEX.md; both write to repo root).
"""

import ast
import os
import sys
import re
import textwrap
from datetime import datetime
from pathlib import Path


# ============================================================
# ROLE CLASSIFICATION
# ============================================================
# Maps module names to functional roles. Modules not listed
# are classified by heuristic (see classify_role()).

ROLE_MAP = {
    # GUI - applications the user launches
    'palomas_orrery':           'gui',
    'palomas_orrery_dashboard': 'gui',
    'star_visualization_gui':   'gui',
    'earth_system_visualization_gui': 'gui',
    'earth_system_controller':  'gui',
    'orbital_param_viz':        'gui',
    'gallery_studio':           'gui',
    'gallery_editor':           'gui',
    'json_gallery':             'gui',

    # Pipeline - transforms data between stages
    'json_converter':           'pipeline',
    'social_media_export':      'pipeline',
    'plot_data_exchange':       'pipeline',
    'save_utils':               'pipeline',
    'gallery_json_fixer':       'pipeline',
    'messier_object_data_handler': 'pipeline',
    'sgr_a_visualization_core_arcs': 'pipeline',

    # Data - catalogs and constants
    'celestial_objects':        'data',
    'spacecraft_encounters':    'data',
    'close_approach_data':      'data',
    'constants_new':            'data',
    'info_dictionary':          'data',
    'exoplanet_systems':        'data',
    'exoplanet_coordinates':    'data',
    'exoplanet_stellar_properties': 'data',
    'sgr_a_star_data':          'data',
    'star_notes':               'data',
    'star_properties':          'data',
    'stellar_data_patches':     'data',
    'stellar_parameters':       'data',
    'messier_catalog':          'data',

    # Cache - fetch, store, retrieve
    'osculating_cache_manager': 'cache',
    'climate_cache_manager':    'cache',
    'incremental_cache_manager':'cache',
    'vot_cache_manager':        'cache',
    'orbit_data_manager':       'cache',

    # Computation - math, orbital mechanics, data processing
    'orbital_elements':         'computation',
    'idealized_orbits':         'computation',
    'celestial_coordinates':    'computation',
    'apsidal_markers':          'computation',
    'data_acquisition':         'computation',
    'data_acquisition_distance':'computation',
    'data_processing':          'computation',
    'object_type_analyzer':     'computation',
    'fetch_climate_data':       'computation',
    'fetch_paleoclimate_data':  'computation',
    'energy_imbalance':         'computation',
    'simbad_manager':           'computation',
    'catalog_selection':        'computation',
    'coordinate_system_guide':  'computation',

    # Rendering - builds visual traces and figures
    'planet_visualization':     'rendering',
    'planet_visualization_utilities': 'rendering',
    'visualization_utils':      'rendering',
    'visualization_2d':         'rendering',
    'visualization_3d':         'rendering',
    'visualization_core':       'rendering',
    'star_sphere_builder':      'rendering',
    'exoplanet_orbits':         'rendering',
    'sgr_a_visualization_core': 'rendering',
    'sgr_a_visualization_animation': 'rendering',
    'sgr_a_visualization_precession': 'rendering',
    'sgr_a_grand_tour':         'rendering',
    'hr_diagram_apparent_magnitude': 'rendering',
    'hr_diagram_distance':      'rendering',
    'planetarium_apparent_magnitude': 'rendering',
    'planetarium_distance':     'rendering',
    'paleoclimate_visualization': 'rendering',
    'paleoclimate_visualization_full': 'rendering',
    'paleoclimate_dual_scale':  'rendering',
    'paleoclimate_human_origins_full': 'rendering',
    'paleoclimate_wet_bulb_full': 'rendering',
    'plot_data_report_widget':  'rendering',

    # Rendering/shells - planetary shell visualizations
    # (classified by heuristic below)

    # Scenarios - specific Earth system scenarios
    'scenarios_heatwaves':      'scenario',
    'scenarios_coral_bleaching':'scenario',
    'scenarios_western_heatwave_march_2026': 'scenario',

    # Earth system - generator
    'earth_system_generator':   'computation',

    # Utility - shared helpers
    'shared_utilities':         'utility',
    'formatting_utils':         'utility',
    'shutdown_handler':         'utility',
    'palomas_orrery_helpers':   'utility',
    'orrery_integration':       'utility',
    'report_manager':           'utility',

    # Developer tools - audit, diagnostics, one-shot scripts
    'module_atlas':             'devtool',
    'dep_trace':                'devtool',
    'provenance_scanner':       'devtool',
    'test_constants_provenance':'devtool',
    'test_orbit_cache':         'devtool',
    'verify_orbit_cache':       'devtool',
    'add_docstrings':           'devtool',
    'create_cache_backups':     'devtool',
    'create_ephemeris_database':'devtool',
    'convert_hot_ph_to_json':   'devtool',
    'diagnose_bcodmo':          'devtool',
    'examine_hot_csv':          'devtool',

    # Legacy
    'star_visualization_gui_before_pyinstaller_refactor': 'legacy',
}


def classify_role(module_name):
    """Classify a module's functional role."""
    if module_name in ROLE_MAP:
        return ROLE_MAP[module_name]
    if module_name.endswith('_visualization_shells'):
        return 'rendering/shells'
    if module_name.endswith('_shells'):
        return 'rendering/shells'
    return 'other'


# Role descriptions for the atlas header
ROLE_DESCRIPTIONS = {
    'gui':              'Applications the user launches (GUIs, editors)',
    'pipeline':         'Transforms data between stages (export, conversion, plotting pipelines)',
    'data':             'Catalogs, constants, and static datasets',
    'cache':            'Fetch, store, and retrieve computed data',
    'computation':      'Math, orbital mechanics, data processing',
    'rendering':        'Builds visual traces, figures, and charts',
    'rendering/shells': 'Planetary shell visualizations (sphere layers)',
    'scenario':         'Specific Earth system scenarios',
    'utility':          'Shared helper functions',
    'devtool':          'Developer tools (dependency tracing, atlas)',
    'legacy':           'Archived / superseded modules',
    'other':            'Uncategorized',
}

# MODULE_INDEX.md section titles -- the same role tags as above, reworded
# for a human skimming the index rather than an AI querying the atlas
# (L-127 Gap item 1: reconcile ROLE_MAP against MODULE_INDEX's existing
# thematic groupings). Deliberately reuses ROLE_MAP as the grouping key
# rather than inventing a second classification scheme -- one source of
# truth for "what kind of module is this," two ways of labeling it.
ROLE_SECTION_TITLES = {
    'gui':              'Core Applications',
    'rendering':        'Visualization Modules',
    'rendering/shells': 'Planetary & Solar Shell Visualizations',
    'computation':      'Orbital Mechanics & Calculations',
    'data':             'Data Catalogs & Constants',
    'cache':            'Cache Management',
    'pipeline':         'Save, Export & Pipeline Utilities',
    'scenario':         'Earth System Scenarios',
    'utility':          'Utility & Helper Modules',
    'devtool':          'Developer Tools',
    'legacy':           'Legacy / Archived Modules',
    'other':            'Other Modules',
}


# ============================================================
# AST EXTRACTION
# ============================================================

def get_module_docstring(filepath):
    """Extract module-level docstring, falling back to leading comments."""
    try:
        with open(filepath, 'rb') as f:
            source = f.read()
        tree = ast.parse(source)
    except Exception:
        return '(parse error)'

    # Try AST docstring first
    doc = ast.get_docstring(tree)
    if doc:
        # Split into paragraphs
        paras = doc.split('\n\n')
        # Skip paragraphs that are just the filename or a title underline
        meaningful = []
        for p in paras:
            stripped = p.strip()
            # Skip if it's just the filename
            if stripped.replace('.py', '') == os.path.basename(filepath).replace('.py', ''):
                continue
            # Skip if it's just underlines (==== or ----)
            if all(c in '=-' for c in stripped.replace('\n', '')):
                continue
            # Remove inline underline lines from within a paragraph
            clean_lines = []
            for ln in stripped.split('\n'):
                if ln.strip() and not all(c in '=-' for c in ln.strip()):
                    clean_lines.append(ln.strip())
            stripped = ' '.join(clean_lines)
            if not stripped:
                continue
            # Skip if very short and looks like a title
            if len(stripped) < 40 and '\n' not in stripped and not stripped.endswith('.'):
                # Likely a heading -- keep looking but save as fallback
                if not meaningful:
                    meaningful.append(stripped)
                continue
            meaningful.append(stripped)
            break  # Got a real paragraph
        if meaningful:
            # Take up to 300 chars of the best paragraph
            result = meaningful[-1].replace('\n', ' ').strip()
            if len(result) > 300:
                result = result[:297] + '...'
            return result
        # Fallback to first paragraph
        return paras[0].strip().replace('\n', ' ')

    # Fall back to leading comments (lines starting with #)
    try:
        text = source.decode('utf-8', errors='replace')
    except Exception:
        return '(no description)'

    lines = text.split('\n')
    comment_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            # Skip shebang
            if stripped.startswith('#!'):
                continue
            content = stripped.lstrip('# ').strip()
            # Skip lines that are just "Import necessary libraries" etc.
            if content.lower().startswith('import '):
                break
            # Skip underline-only lines
            if content and all(c in '=-' for c in content):
                continue
            if content:
                comment_lines.append(content)
        elif stripped == '' and not comment_lines:
            continue  # skip leading blank lines
        elif stripped.startswith('import') or stripped.startswith('from'):
            break  # hit imports, stop
        elif comment_lines:
            break  # hit non-comment after comments
        else:
            break

    if comment_lines:
        return ' '.join(comment_lines)

    return '(no description)'


def get_public_functions(filepath):
    """Extract public function/class names with their docstrings."""
    try:
        with open(filepath, 'rb') as f:
            tree = ast.parse(f.read())
    except Exception:
        return []

    functions = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
            doc = ast.get_docstring(node) or ''
            # First line only
            first_line = doc.split('\n')[0].strip() if doc else ''
            # Get argument names (skip 'self')
            args = []
            for arg in node.args.args:
                name = arg.arg
                if name != 'self':
                    args.append(name)
            sig = f"{node.name}({', '.join(args)})"
            functions.append((sig, first_line, node.lineno))

        elif isinstance(node, ast.ClassDef) and not node.name.startswith('_'):
            doc = ast.get_docstring(node) or ''
            first_line = doc.split('\n')[0].strip() if doc else ''
            functions.append((f"class {node.name}", first_line, node.lineno))

    return functions


def get_local_imports(filepath, local_modules):
    """Extract project-local imports from a Python file."""
    try:
        with open(filepath, 'rb') as f:
            tree = ast.parse(f.read())
    except Exception:
        return set()

    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                base = alias.name.split('.')[0]
                if base in local_modules:
                    imports.add(base)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                base = node.module.split('.')[0]
                if base in local_modules:
                    imports.add(base)
    return imports


def count_lines(filepath):
    """Count non-blank lines in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            return sum(1 for line in f if line.strip())
    except Exception:
        return 0


# ============================================================
# GRAPH BUILDING
# ============================================================

def build_dependency_graph(project_dir):
    """Build bidirectional dependency graph for all local modules."""
    local_modules = set()
    for f in os.listdir(project_dir):
        if f.endswith('.py'):
            local_modules.add(f[:-3])

    deps = {}       # module -> set of modules it imports
    consumers = {}  # module -> set of modules that import it

    for mod in local_modules:
        fpath = os.path.join(project_dir, mod + '.py')
        if os.path.exists(fpath):
            imported = get_local_imports(fpath, local_modules)
            deps[mod] = imported
            for imp in imported:
                consumers.setdefault(imp, set()).add(mod)

    return deps, consumers, local_modules


# ============================================================
# SCAN -- shared by both generators, run exactly once per invocation
# ============================================================

def scan_modules(project_dir):
    """Scan every .py file in project_dir once and return the list of
    per-module info dicts that both generate_atlas() and generate_index()
    read from. This is the single source of truth both outputs share --
    running this once and handing the same result to both writers is what
    actually prevents the two files from diverging, not just a naming
    convention."""
    print(f"Scanning {project_dir}...")
    deps, consumers, local_modules = build_dependency_graph(project_dir)

    modules = []
    for mod in sorted(local_modules):
        fpath = os.path.join(project_dir, mod + '.py')
        if not os.path.exists(fpath):
            continue

        info = {
            'name': mod,
            'path': mod + '.py',
            'role': classify_role(mod),
            'docstring': get_module_docstring(fpath),
            'functions': get_public_functions(fpath),
            'lines': count_lines(fpath),
            'deps': sorted(deps.get(mod, set())),
            'consumers': sorted(consumers.get(mod, set())),
        }
        modules.append(info)

    return modules


ROLE_ORDER = [
    'gui', 'rendering', 'rendering/shells', 'computation',
    'data', 'cache', 'pipeline', 'scenario', 'utility',
    'devtool', 'legacy', 'other'
]


# ============================================================
# ATLAS GENERATION
# ============================================================

def generate_atlas(modules, output_path):
    """Write MODULE_ATLAS.md from an already-scanned modules list
    (see scan_modules)."""

    # Group by role
    by_role = {}
    for mod in modules:
        role = mod['role']
        by_role.setdefault(role, []).append(mod)

    # Count totals
    total_lines = sum(m['lines'] for m in modules)
    total_functions = sum(len(m['functions']) for m in modules)

    # Generate markdown
    lines = []
    now = datetime.now().strftime('%B %d, %Y')

    lines.append("# Paloma's Orrery -- Module Atlas")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append(f"Modules: {len(modules)} | "
                 f"Functions: {total_functions} | "
                 f"Lines: {total_lines:,}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## How to Use This Document")
    lines.append("")
    lines.append("Upload this file to a Claude session. Then ask questions:")
    lines.append("")
    lines.append('- "What modules are involved in rendering comets?"')
    lines.append('- "I want to add a new spacecraft encounter -- what do I touch?"')
    lines.append('- "What imports spacecraft_encounters and what does it import?"')
    lines.append('- "Show me the pipeline from GUI click to rendered figure"')
    lines.append('- "What would break if I changed constants_new?"')
    lines.append("")
    lines.append("Claude searches this atlas, reads relevant source files,")
    lines.append("and explains in context.")
    lines.append("")
    lines.append("For a lighter, human-browsable version of this same scan, see")
    lines.append("MODULE_INDEX.md (also generated by this script).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Role summary table
    lines.append("## Roles at a Glance")
    lines.append("")
    lines.append("| Role | Count | Description |")
    lines.append("|------|-------|-------------|")
    for role in ROLE_ORDER:
        if role in by_role:
            desc = ROLE_DESCRIPTIONS.get(role, '')
            count = len(by_role[role])
            lines.append(f"| {role} | {count} | {desc} |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Module entries grouped by role
    for role in ROLE_ORDER:
        if role not in by_role:
            continue

        role_desc = ROLE_DESCRIPTIONS.get(role, role)
        role_modules = by_role[role]

        lines.append(f"## {role.upper()}: {role_desc}")
        lines.append("")

        for mod in role_modules:
            lines.append(f"### {mod['name']}.py")
            lines.append("")
            lines.append(f"**Role:** {mod['role']} | "
                         f"**Lines:** {mod['lines']:,}")
            lines.append("")

            # Description
            lines.append(f"> {mod['docstring']}")
            lines.append("")

            # Dependencies
            if mod['deps']:
                lines.append(f"**Depends on:** "
                             f"{', '.join(mod['deps'])}")
            else:
                lines.append("**Depends on:** (none)")

            # Consumers
            if mod['consumers']:
                lines.append(f"**Consumed by:** "
                             f"{', '.join(mod['consumers'])}")
            else:
                lines.append("**Consumed by:** (none -- standalone)")

            lines.append("")

            # Public functions
            if mod['functions']:
                lines.append("**Public functions:**")
                lines.append("")
                for sig, doc, lineno in mod['functions']:
                    if doc:
                        lines.append(f"- `{sig}` (line {lineno}) -- {doc}")
                    else:
                        lines.append(f"- `{sig}` (line {lineno})")
                lines.append("")

            lines.append("---")
            lines.append("")

    # Alphabetical quick-reference index at the end
    lines.append("## Alphabetical Index")
    lines.append("")
    lines.append("| Module | Role | Lines | Deps | Consumers |")
    lines.append("|--------|------|------:|-----:|----------:|")
    for mod in sorted(modules, key=lambda m: m['name']):
        lines.append(
            f"| {mod['name']} | {mod['role']} | "
            f"{mod['lines']:,} | {len(mod['deps'])} | "
            f"{len(mod['consumers'])} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by module_atlas.py -- "
                 "Paloma's Orrery Developer Tools*")
    lines.append("")

    # Write output
    content = '\n'.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Atlas written to {output_path}")
    print(f"  {len(modules)} modules, {total_functions} functions, "
          f"{total_lines:,} lines")

    # Print role summary
    print("\nRole summary:")
    for role in ROLE_ORDER:
        if role in by_role:
            count = len(by_role[role])
            print(f"  {role:20s} {count:3d} modules")


# ============================================================
# INDEX GENERATION (L-127: mechanical, same scan as the atlas)
# ============================================================

def _index_description(mod):
    """The docstring text for an index row, with a redundant leading
    'modulename.py - ' prefix stripped (many docstrings restate the
    filename as their first words -- harmless in the atlas's blockquote
    format, repetitive next to a Module column that already says it)."""
    doc = mod['docstring']
    prefix_patterns = [
        mod['name'] + '.py - ', mod['name'] + '.py -',
        mod['name'] + '.py: ', mod['name'] + '.py ',
        mod['name'] + ' - ', mod['name'] + ' -',
    ]
    for p in prefix_patterns:
        if doc.startswith(p):
            doc = doc[len(p):].lstrip()
            break
    return doc[:1].upper() + doc[1:] if doc else doc


def generate_index(modules, output_path):
    """Write MODULE_INDEX.md from the SAME already-scanned modules list
    generate_atlas() uses -- a lighter, human-browsable companion, not an
    independent document. Mechanical only: each module's description is
    its own docstring (via scan_modules -> get_module_docstring), not an
    AI-synthesized summary. A thin docstring makes a thin index entry --
    deliberate, per L-127: that's a visible incentive to improve the
    docstring, not a reason to hand-patch the index around it."""

    by_role = {}
    for mod in modules:
        by_role.setdefault(mod['role'], []).append(mod)

    total_lines = sum(m['lines'] for m in modules)
    total_functions = sum(len(m['functions']) for m in modules)

    lines = []
    now = datetime.now().strftime('%B %d, %Y')

    lines.append("# Paloma's Orrery - Module Index")
    lines.append("")
    lines.append(f"**Generated:** {now} by `module_atlas.py`  ")
    lines.append("**Repository:** Paloma's Orrery - Solar System Visualization Suite  ")
    lines.append("**Philosophy:** Data Preservation is Climate Action")
    lines.append("")
    lines.append("This file and `MODULE_ATLAS.md` are generated from the SAME scan")
    lines.append("(see `module_atlas.py`) -- they cannot diverge from each other the")
    lines.append("way the old hand-maintained MODULE_INDEX.md did. This is the light,")
    lines.append("human-browsable view; `MODULE_ATLAS.md` is the deep reference")
    lines.append("(functions, dependencies, consumers) meant for AI-assisted queries.")
    lines.append("")
    lines.append(f"**Total Python Files:** {len(modules)}  ")
    lines.append(f"**Total Lines of Code (non-blank):** {total_lines:,}  ")
    lines.append(f"**Total Public Functions/Classes:** {total_functions:,}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for role in ROLE_ORDER:
        if role not in by_role:
            continue
        title = ROLE_SECTION_TITLES.get(role, role.title())
        role_modules = sorted(by_role[role], key=lambda m: m['name'])

        lines.append(f"## {title}")
        lines.append("")
        lines.append("| Module | Description |")
        lines.append("|--------|-------------|")
        for mod in role_modules:
            desc = _index_description(mod).replace('|', '\\|')
            lines.append(
                f"| `{mod['name']}.py` | {desc} ({mod['lines']:,} lines) |"
            )
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("*Generated by `module_atlas.py` -- Paloma's Orrery Developer Tools. "
                 "For function-level detail, dependencies, and consumers, see "
                 "`MODULE_ATLAS.md`.*")
    lines.append("")

    content = '\n'.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Index written to {output_path}")


# ============================================================
# MAIN
# ============================================================

def main():
    project_dir = '.'
    atlas_path = 'MODULE_ATLAS.md'
    index_path = 'MODULE_INDEX.md'
    do_atlas = True
    do_index = True

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--output' and i + 1 < len(args):
            atlas_path = args[i + 1]
            i += 2
        elif args[i] == '--index-output' and i + 1 < len(args):
            index_path = args[i + 1]
            i += 2
        elif args[i] == '--atlas-only':
            do_index = False
            i += 1
        elif args[i] == '--index-only':
            do_atlas = False
            i += 1
        elif not args[i].startswith('-'):
            project_dir = args[i]
            i += 1
        else:
            i += 1

    if not os.path.isdir(project_dir):
        print(f"ERROR: '{project_dir}' is not a directory")
        sys.exit(1)

    modules = scan_modules(project_dir)

    if do_atlas:
        generate_atlas(modules, atlas_path)
    if do_index:
        generate_index(modules, index_path)


if __name__ == '__main__':
    main()
