"""L-188 -- wire the maintenance runner into the dashboard.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo ROOT, open it in VS Code,
and click Run.

    python patch_L188_dashboard_runner.py

Requires maintenance_run.py to be in the repo root already; the patch
checks and refuses otherwise, since a Not Found button is worse than no
button.

WHAT IT DOES
------------
Two edits to palomas_orrery_dashboard.py.

1. The renderer learns an `indent` flag -- positional slot 6 on a launch
   entry, after `args`. An indented card gets 28px of left padding and
   nothing else changes.

2. Developer Tools is reordered. MAINTENANCE RUN goes first, and the
   eight tools it runs sit indented beneath it, in the order the runner
   executes them: the four generators, then the checkers, with the
   provenance scanner last so its verdict reads last. Three test files
   the runner covers but the dashboard never listed are added --
   test_cross_checked.py, test_citation_inheritance.py and
   test_provenance_1d.py. The five tools the runner deliberately does
   NOT cover (Dependency Trace, Animation HTML Tool, Add Module
   Docstrings, Verify Orbit Cache, Export Orbit Cache) stay unindented
   below, as peers of the runner rather than members of it.

WHY INDENT RATHER THAN REPLACE
------------------------------
L-188 as written says the runner "must REPLACE the individual entries,
not join them," because a ninth peer entry reproduces the eight-judgment-
calls problem it exists to solve. Tony ruled on 2026-08-12 to indent
instead. That satisfies what the constraint was protecting: an indented
child is not a peer, so the one-action default survives, and the
individual tools stay launchable and -- his reason -- stay visible, so
what the automation covers remains known rather than disappearing behind
one button. The L-188 bullet should be rewritten to match; that belongs
in the ledger capture pass, not in this patch.

SAFETY
------
Transactional: both anchors must match exactly once and
maintenance_run.py must exist, or nothing is written. Base fingerprint is
MD5 over LF-normalized content. Binary-mode I/O; line endings preserved.

WHAT SUCCESS LOOKS LIKE
-----------------------
One `ok` line per edit, then `patch applied`. Any `ERROR:` or
`ANCHOR FAIL` means nothing was written.

AFTER RUNNING
-------------
Launch the dashboard and look at Developer Tools. MAINTENANCE RUN should
head the section with eight indented tools beneath it, every button
reading Launch rather than Not Found.
"""

import hashlib
import os
import sys

TARGET = 'palomas_orrery_dashboard.py'
BASE_MD5 = '854b7e480ec7b5799740c3ebdc0796d6'
REQUIRED = 'maintenance_run.py'

RENDER_OLD = b'                base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR\n                interactive = entry[4] if len(entry) > 4 else False\n                args = entry[5] if len(entry) > 5 else None\n                self._build_launch_card(cards_frame, name, script, desc,\n                                        base_dir, interactive, args, i)\n\n    def _build_launch_card(self, parent, name, script, desc, base_dir,\n                           interactive, args, index):\n        """Individual launch card with button and description."""\n        card = ctk.CTkFrame(parent, fg_color=COLOR_SURFACE,\n                            corner_radius=10)\n        card.pack(fill="x", pady=4, ipady=6)\n'

RENDER_NEW = b'                base_dir = entry[3] if len(entry) > 3 else SCRIPT_DIR\n                interactive = entry[4] if len(entry) > 4 else False\n                args = entry[5] if len(entry) > 5 else None\n                indent = entry[6] if len(entry) > 6 else False\n                self._build_launch_card(cards_frame, name, script, desc,\n                                        base_dir, interactive, args, i,\n                                        indent)\n\n    def _build_launch_card(self, parent, name, script, desc, base_dir,\n                           interactive, args, index, indent=False):\n        """Individual launch card with button and description.\n\n        `indent` marks a tool that the maintenance runner already covers.\n        Indenting rather than removing was Tony\'s ruling of 2026-08-12:\n        the individual entries stay launchable, and staying visible is how\n        the automation\'s contents remain known instead of disappearing\n        behind one button. The runner sits directly above its indented\n        group.\n        """\n        card = ctk.CTkFrame(parent, fg_color=COLOR_SURFACE,\n                            corner_radius=10)\n        card.pack(fill="x", pady=4, ipady=6,\n                  padx=(28, 0) if indent else 0)\n'

REGION_OLD = b'        ("Update Ledger Index",\n         "ledger_index.py",\n         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "\n         "and migrate DONE items to section C. Run after editing any ledger block.",\n         SCRIPT_DIR,\n         True),\n        ("Update Skill Manifest",\n         "skills_index.py",\n         "Regenerate the Skill Manifest table in the protocol from skills/*/SKILL.md. "\n         "Run after adding, renaming, or versioning a skill.",\n         SCRIPT_DIR,\n         True),\n        ("Data Inventory",\n         "data_inventory.py",\n         "Inventory the large, gitignored data stores (data/, star_data/). "\n         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",\n         SCRIPT_DIR,\n         True),\n        ("Provenance Scanner",\n         "provenance_scanner.py",\n         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "\n         "Run before/after edits to shared values, or when a value looks suspicious.",\n         SCRIPT_DIR,\n         True),\n        ("Regenerate Module Atlas",\n         "module_atlas.py",\n         "Scan codebase, generate MODULE_ATLAS.md. "\n         "Run after significant codebase changes (new modules, reorganizations).",\n         SCRIPT_DIR,\n         True),\n        ("Dependency Trace",\n         "dep_trace.py",\n         "Map who depends on (and is consumed by) a module. "\n         "Run before editing: python dep_trace.py <module_name> [hops]",\n         SCRIPT_DIR,\n         True),\n        ("Animation HTML Tool",\n         "measure_animation_html.py",\n         "Measure a saved animation HTML: trace count, frame count, which traces "\n         "are carried inside frames, and frames payload size. Run to compare a "\n         "baseline against a patched export and quantify the frame-fence fix.",\n         SCRIPT_DIR,\n         True),\n        ("Test Constants Provenance",\n         "test_constants_provenance.py",\n         "Pass/fail regression tests for constants_new.py. "\n         "Run before committing changes to constants, or first if a plot looks wrong.",\n         SCRIPT_DIR,\n         True),\n        ("Add Module Docstrings",\n         "add_docstrings.py",\n         "Add or improve module-level docstrings across the codebase; touches no code. "\n         "Run after adding modules, before regenerating the Module Atlas.",\n         SCRIPT_DIR,\n         True),\n        ("Verify Orbit Cache",\n         "verify_orbit_cache.py",\n         "Back up, validate, and repair orbit_paths.json, reporting any issues. "\n         "Run if orbit plots look wrong or the cache may be corrupted.",\n         SCRIPT_DIR,\n         True),\n        ("Test Orbit Cache",\n         "test_orbit_cache.py",\n         "Comprehensive test suite for orbit data caching, format conversion, "\n         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",\n         SCRIPT_DIR,\n         True),\n        ("Export Orbit Cache",\n         "export_orbit_cache.py",\n         "Phase 1b devtool: read the local orbit caches (read-only) and write "\n         "web-servable orbit/position files for the interactive gallery.",\n         SCRIPT_DIR,\n         True),\n        ("Test Reset Completeness",\n         "test_reset_completeness.py",\n         "Guard the Reset button against partial-reset drift: dirties every "\n         "tracked control, calls the live reset handler, asserts everything "\n         "returns to its startup default.",\n         SCRIPT_DIR,\n         True),\n'

REGION_NEW = b'        ("MAINTENANCE RUN -- everything indented below",\n         "maintenance_run.py",\n         "One command for the whole routine: regenerates the four generated "\n         "documents, then runs every checker, then prints one summary. It "\n         "reports and continues rather than stopping at the first failure, "\n         "and says which generated files actually moved. About ten seconds. "\n         "Run after an edit session and before a push. Everything indented "\n         "below is included in it and can still be launched on its own.",\n         SCRIPT_DIR,\n         True),\n        ("Update Ledger Index",\n         "ledger_index.py",\n         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "\n         "and migrate DONE items to section C. Run after editing any ledger block.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Update Skill Manifest",\n         "skills_index.py",\n         "Regenerate the Skill Manifest table in the protocol from skills/*/SKILL.md. "\n         "Run after adding, renaming, or versioning a skill.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Data Inventory",\n         "data_inventory.py",\n         "Inventory the large, gitignored data stores (data/, star_data/). "\n         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Regenerate Module Atlas",\n         "module_atlas.py",\n         "Scan codebase, generate MODULE_ATLAS.md. "\n         "Run after significant codebase changes (new modules, reorganizations).",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Constants Provenance",\n         "test_constants_provenance.py",\n         "Pass/fail regression tests for constants_new.py. "\n         "Run before committing changes to constants, or first if a plot looks wrong.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Cross-Check Annotations",\n         "test_cross_checked.py",\n         "Pass/fail tests for the cross-check annotation grammar and V2 "\n         "scoring. Run after editing annotations or the scanner\'s parser.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Citation Inheritance",\n         "test_citation_inheritance.py",\n         "Pass/fail tests for block-scoped citation inheritance in the "\n         "provenance scanner.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Provenance 1d/1e",\n         "test_provenance_1d.py",\n         "Pass/fail regression tests for the Phase 1d/1e scanner mechanisms.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Reset Completeness",\n         "test_reset_completeness.py",\n         "Guard the Reset button against partial-reset drift: dirties every "\n         "tracked control, calls the live reset handler, asserts everything "\n         "returns to its startup default.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Orbit Cache",\n         "test_orbit_cache.py",\n         "Comprehensive test suite for orbit data caching, format conversion, "\n         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Provenance Scanner",\n         "provenance_scanner.py",\n         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "\n         "Run before/after edits to shared values, or when a value looks suspicious.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Dependency Trace",\n         "dep_trace.py",\n         "Map who depends on (and is consumed by) a module. "\n         "Run before editing: python dep_trace.py <module_name> [hops]",\n         SCRIPT_DIR,\n         True),\n        ("Animation HTML Tool",\n         "measure_animation_html.py",\n         "Measure a saved animation HTML: trace count, frame count, which traces "\n         "are carried inside frames, and frames payload size. Run to compare a "\n         "baseline against a patched export and quantify the frame-fence fix.",\n         SCRIPT_DIR,\n         True),\n        ("Add Module Docstrings",\n         "add_docstrings.py",\n         "Add or improve module-level docstrings across the codebase; touches no code. "\n         "Run after adding modules, before regenerating the Module Atlas.",\n         SCRIPT_DIR,\n         True),\n        ("Verify Orbit Cache",\n         "verify_orbit_cache.py",\n         "Back up, validate, and repair orbit_paths.json, reporting any issues. "\n         "Run if orbit plots look wrong or the cache may be corrupted.",\n         SCRIPT_DIR,\n         True),\n        ("Export Orbit Cache",\n         "export_orbit_cache.py",\n         "Phase 1b devtool: read the local orbit caches (read-only) and write "\n         "web-servable orbit/position files for the interactive gallery.",\n         SCRIPT_DIR,\n         True),\n'

EDITS = [
    ('renderer: indent flag', RENDER_OLD, RENDER_NEW),
    ('Developer Tools: runner first, members indented', REGION_OLD, REGION_NEW),
]


def fingerprint(data):
    """MD5 over LF-normalized content -- line endings are not content."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    if not os.path.exists(os.path.join(here, REQUIRED)):
        print("ERROR: %s is not in this folder." % REQUIRED)
        print("       Save it here first -- the dashboard entry this patch")
        print("       adds would otherwise render as Not Found.")
        sys.exit(1)

    path = os.path.join(here, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this from the repo root." % TARGET)
        sys.exit(1)

    with open(path, 'rb') as handle:
        data = handle.read()

    got = fingerprint(data)
    if got != BASE_MD5:
        print("ERROR: base moved for %s" % TARGET)
        print("       expected %s" % BASE_MD5)
        print("       got      %s" % got)
        print("Nothing written.")
        sys.exit(1)

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print("note: %s uses CRLF; anchors translated to match." % TARGET)

    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print("ANCHOR FAIL (%s): expected 1 match, found %d."
                  % (label, count))
            print("Nothing written.")
            sys.exit(1)
        data = data.replace(old, new)
        print("  ok  %s" % label)

    with open(path, 'wb') as handle:
        handle.write(data)

    print()
    print("patch applied -- %s, %d bytes" % (TARGET, len(data)))
    print()
    print("NEXT: launch the dashboard and check Developer Tools.")
    print("  MAINTENANCE RUN heads the section, eight tools indented under it,")
    print("  every button reading Launch rather than Not Found.")


if __name__ == '__main__':
    main()
