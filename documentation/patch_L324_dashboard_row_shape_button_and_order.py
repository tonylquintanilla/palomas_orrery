"""
patch_L324_dashboard_row_shape_button_and_order.py

Adds the two missing dashboard buttons and reorders the Developer Tools
group the way Tony asked for.

WHY A BUTTON WAS MISSING
    test_status_lines.py has been in the maintenance runner since L-305
    but never had a dashboard button, so the new row-shape guard had
    nowhere to appear either. I diffed the two lists rather than adding
    only the one I knew about: the runner has 5 generators and 15
    checkers, the dashboard had 18 indented buttons, and exactly two
    were missing -- Status lines and Row shape. Nothing checks that
    those two lists agree; today they do.

WHAT CHANGES (2 files)
  palomas_orrery_dashboard.py
    1. The Developer Tools list is reordered and two entries are added:
       Test Status Lines, and Test Row Shape (the same script run with
       --shape-only). Every existing entry is preserved BYTE FOR BYTE --
       the new list was generated from the file's own source text, not
       retyped -- so no description, path or flag changed.
       New order: Gallery Cache Builder, MAINTENANCE RUN, then the
       indented group as GENERATORS (5, alphabetical) and CHECKERS (17,
       alphabetical), then the 11 standalone tools alphabetically.
       Sorting is case-insensitive, so Verify Orbit Cache comes before
       VOT Cache Manager the way a person reads it.
    2. A bare string in a LAUNCH_GROUPS list is now a heading rather
       than a card, which is how GENERATORS and CHECKERS get labelled.
  LEDGER_CONSOLIDATED.md
    3. L-324 records the missing button and the runner/dashboard parity
       gap, and its Gap moves to what is left.

WHAT IS PERMANENT AND WHAT IS NOT
    This script is disposable and one-shot. The two buttons, the
    ordering and the heading support are permanent.

HOW TO RUN IT (Tony)
    Save this file into the orrery repo root -- the same folder as
    palomas_orrery_dashboard.py -- open it in VS Code, and click Run.
    Equivalent command:
    python patch_L324_dashboard_row_shape_button_and_order.py

    Success: one "ok" line per edit, two "stamp updated" lines, a
             "result matches the tested build" line, then
             "patch applied".
    Failure: one ERROR or ANCHOR FAIL line. NOTHING is written to
             either file. Undo is Discard Changes in GitHub Desktop.

    The patch checks its own OUTPUT as well as its input. After editing
    the dashboard in memory it compares the result against the
    fingerprint of the file that was actually launched and rendered
    during testing, and writes nothing if they differ. A success means
    the dashboard on your disk is byte-for-byte the tested one.

AFTER IT RUNS
    1. Open the dashboard and look at Developer Tools. Two new buttons
       sit in the indented group under CHECKERS: Test Row Shape and
       Test Status Lines. This part is yours to judge -- I can show it
       builds without error, not that it looks right.
    2. Run ledger_index.py as a parse check -- expect
       "OK: 319 L-blocks parsed, no consistency problems."

BASE
    Built on orrery a391262e9f5fc3ba9b590ef94dc249ed04781bb8 at
    https://github.com/tonylquintanilla/palomas_orrery

Written September 12, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

INDEX_START = b"<!-- INDEX:START"
INDEX_END = b"<!-- INDEX:END -->"

DASH = "palomas_orrery_dashboard.py"
LEDGER = "LEDGER_CONSOLIDATED.md"

BASE_FP = {
    DASH: "9b7adbf173229fad497bbef27065659b",
    LEDGER: "de735cc76ed12438a241c20aaf8893b7",
}

# LF-normalized md5 of the dashboard AFTER this patch, taken from the
# copy that was launched under xvfb and rendered without error. The
# patch refuses to write anything that does not match it.
RESULT_FP = "eeea44debba63f769ae54fe51523616d"


def fingerprint(path, data):
    lf = data.replace(b"\r\n", b"\n")
    if path == LEDGER:
        a = lf.index(INDEX_START)
        b = lf.index(INDEX_END) + len(INDEX_END)
        lf = lf[:a] + lf[b:]
    return hashlib.md5(lf).hexdigest()


OLD_BODY = '("Gallery Cache Builder -- Manual Run",\n         os.path.join("tools", "gallery_cache_builder.py"),\n         "Manual serving-cache build. Runs from the gallery repo ROOT: the "\n         "builder resolves its data/ paths from the working directory, so "\n         "launching it from tools/ cannot find data/objects_config.json. "\n         "With no flags it fetches from Horizons, validates, atomic-swaps "\n         "the new cache into data/solar-system, and STOPS -- it does not "\n         "commit or push. Commit it yourself in GitHub Desktop after the "\n         "run finishes. Do not commit while it is still running: mid-build "\n         "the working tree shows deletions only, which is the swap in "\n         "progress, not data loss. The console stays open at the repo root "\n         "if you want a flagged re-run (--dry-run --object <slug>, "\n         "--first-build).",\n         GALLERY_REPO_DIR,\n         True),\n        ("MAINTENANCE RUN -- everything indented below",\n         "orrery_maintenance_run.py",\n         "One command for the whole routine: regenerates the generated "\n         "documents, then runs every checker, then prints one summary. It "\n         "reports and continues rather than stopping at the first failure, "\n         "and says which generated files actually moved. About ten seconds. "\n         "Run after an edit session and before a push. Everything indented "\n         "below is included in it and can still be launched on its own.",\n         SCRIPT_DIR,\n         True),\n        ("Update Ledger Index",\n         "ledger_index.py",\n         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "\n         "and migrate DONE items to section C. Run after editing any ledger block.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Update Skill Manifest",\n         "skills_index.py",\n         "Regenerate the Skill Manifest table in the protocol from skills/*/SKILL.md. "\n         "Run after adding, renaming, or versioning a skill.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Regenerate Module Atlas",\n         "module_atlas.py",\n         "Scan codebase, generate MODULE_ATLAS.md. "\n         "Run after significant codebase changes (new modules, reorganizations).",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Data Inventory",\n         "data_inventory.py",\n         "Inventory the large, gitignored data stores (data/, star_data/). "\n         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Document Index",\n         "doc_index.py",\n         "Regenerate the key-documents table in README.md from the "\n         "one-line Doc-Kind tag each root document carries. The purpose "\n         "text lives in the document it describes, not in this tool and "\n         "not in the README, so the wording stays yours while the table "\n         "stays generated. Three kinds: generated (never hand-edit -- the "\n         "next run destroys the edit), zoned (hand-written prose around a "\n         "marker zone a tool rewrites), and hand. A document with no tag "\n         "is listed as untagged and named in the summary rather than "\n         "quietly dropped. Run after adding, renaming, or retiring a root "\n         "document; --check reports staleness without writing.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Constants Change Report",\n         "constants_change_report.py",\n         "Ask git what changed in constants_new.py since the last commit "\n         "and report each moved value in words. The line that matters "\n         "says whether the provenance moved WITH the number: a deliberate "\n         "correction edits the value and its comment block together, "\n         "while corruption -- a bad merge, a stray keystroke, a copied "\n         "stale value -- moves the number alone and leaves the evidence "\n         "describing the old one. Run before committing a change to "\n         "constants_new.py.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Constants Provenance",\n         "test_constants_provenance.py",\n         "Pass/fail regression tests for constants_new.py. "\n         "Run before committing changes to constants, or first if a plot looks wrong.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Cross-Check Annotations",\n         "test_cross_checked.py",\n         "Pass/fail tests for the cross-check annotation grammar and V2 "\n         "scoring. Run after editing annotations or the scanner\'s parser.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Citation Inheritance",\n         "test_citation_inheritance.py",\n         "Pass/fail tests for block-scoped citation inheritance in the "\n         "provenance scanner.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Scanner Recognition",\n         "test_provenance_1d.py",\n         "Proves the provenance scanner still recognizes a real citation "\n         "and still refuses a fake one. Covers shadow constants (a local "\n         "copy of a value already defined and cited in constants_new.py), "\n         "author-year forms like (Nolan et al. 2013), F/C units, and tier "\n         "labels. Half the tests are written backwards on purpose: a regex "\n         "that is too loose clears findings by matching what it should "\n         "not, and the Tier-1 count then falls, which looks like progress. "\n         "Ledger L-156, sub-steps 1d and 1e.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Reset Completeness",\n         "test_reset_completeness.py",\n         "Guard the Reset button against partial-reset drift: dirties every "\n         "tracked control, calls the live reset handler, asserts everything "\n         "returns to its startup default.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Orbit Cache",\n         "test_orbit_cache.py",\n         "Comprehensive test suite for orbit data caching, format conversion, "\n         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Worksheet Checker",\n         "worksheet_checker.py",\n         "Open the worksheet each cross-check annotation names and report "\n         "whether that worksheet records the check the annotation claims. "\n         "Catches a value edited AFTER its check, which no diff-based tool "\n         "can see once the edit is committed. Report-only -- it writes "\n         "WORKSHEET_CHECK.md and never gates a push. Run after writing "\n         "annotations, after a value moves, or before a gallery build.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Worksheet Checker",\n         "test_worksheet_checker.py",\n         "Pass/fail tests for the worksheet checker. Every layer is "\n         "exercised twice, once with evidence that clears it and once "\n         "with an injected violation that must not, because zero "\n         "findings and a broken check look identical. Run after editing "\n         "the checker or the worksheet schema.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Worksheet Key Round Trip",\n         "test_worksheet_keys.py",\n         "Assert that every annotated site mints a key that resolves back "\n         "to it, on every run. A rename breaks it, a split implementation "\n         "between the builder and the checker breaks it, and a change to "\n         "the enclosing-name rule breaks it -- all three loudly, at the "\n         "commit that introduced them, rather than months later when a "\n         "returned worksheet will not bind.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Builder Marker Join",\n         "test_worksheet_request_builder.py",\n         "Test that a citation continued onto a marked second line "\n         "(`# Source+:` under `# Source:`) is joined back before the "\n         "request quotes it. Every behaviour is exercised twice, once "\n         "with input that should join and once with input that must NOT: "\n         "a join firing on everything is indistinguishable from a join "\n         "firing correctly, and both report zero problems, so the "\n         "negative cases are the test. The last check runs against the "\n         "real corpus. Run after editing the builder or relabeling a "\n         "continuation.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Extractor Pins",\n         "test_extractor_pins.py",\n         "Pin the instruction filter\'s kept-and-dropped set at "\n         "LOOKBACK 30 / LOOKAHEAD 25, frozen 2026-08-14. The claim "\n         "ordinal in every issued key -- the `::c2` -- counts claims "\n         "AFTER this filter runs, so extending the instruction pattern "\n         "by one phrase lets a formerly-dropped number join the sequence "\n         "and shifts every ordinal after it with no prose edit at all. A "\n         "worksheet returned against the old ordinals would then bind to "\n         "the wrong claim. It does not decide whether a change is wrong; "\n         "it reports that the extractor no longer means what the issued "\n         "keys assume, and prints the replacement pin file.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Provenance Scanner",\n         "provenance_scanner.py",\n         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "\n         "Run before/after edits to shared values, or when a value looks suspicious.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Worksheet Request Builder",\n         "worksheet_request_builder.py",\n         "Write the cross-check request that goes OUT to a reader. The "\n         "checker reads what comes back; this writes what is sent. Opens "\n         "in its own console because it asks three questions, in this "\n         "order. WHICH ROWS -- a numbered list of named selections; it "\n         "DEFAULTS TO 1, the whole corpus, so type the number you want "\n         "rather than pressing Enter (2 is constants_new.py, the 23-row "\n         "pilot slice). BATCH NAME -- becomes the filename. ANCHOR SHA -- "\n         "the commit the request describes; use current HEAD, and re-run "\n         "if you commit anything before sending it, because a returned "\n         "row is checked against this SHA. It writes "\n         "REQUEST_<batch>.jsonl and REQUEST_<batch>.md into "\n         "documentation/worksheets/ and refuses rather than overwriting "\n         "if either name is taken. Send the .jsonl; the .md is the "\n         "fallback if a return will not parse. It judges nothing -- "\n         "reading the returns is Worksheet Checker, above.",\n         SCRIPT_DIR,\n         True),\n        ("Dependency Trace",\n         "dep_trace.py",\n         "Map who depends on (and is consumed by) a module. "\n         "Run before editing: python dep_trace.py <module_name> [hops]",\n         SCRIPT_DIR,\n         True),\n        ("Animation HTML Tool",\n         "measure_animation_html.py",\n         "Measure a saved animation HTML: trace count, frame count, which traces "\n         "are carried inside frames, and frames payload size. Run to compare a "\n         "baseline against a patched export and quantify the frame-fence fix.",\n         SCRIPT_DIR,\n         True),\n        ("Add Module Docstrings",\n         "add_docstrings.py",\n         "Add or improve module-level docstrings across the codebase; touches no code. "\n         "Run after adding modules, before regenerating the Module Atlas.",\n         SCRIPT_DIR,\n         True),\n        ("Verify Orbit Cache",\n         "verify_orbit_cache.py",\n         "Back up, validate, and repair orbit_paths.json, reporting any issues. "\n         "Run if orbit plots look wrong or the cache may be corrupted.",\n         SCRIPT_DIR,\n         True),\n        ("Export Orbit Cache",\n         "export_orbit_cache.py",\n         "Phase 1b devtool: read the local orbit caches (read-only) and write "\n         "web-servable orbit/position files for the interactive gallery.",\n         SCRIPT_DIR,\n         True),\n        ("Create Ephemeris Database",\n         "create_ephemeris_database.py",\n         "(Re)build satellite_ephemerides.json from idealized_orbits.py plus "\n         "any downloaded Horizons ephemeris files.",\n         SCRIPT_DIR,\n         True),\n        ("Climate Cache Manager",\n         "climate_cache_manager.py",\n         "Safely update the climate data caches, with validation and rollback.",\n         SCRIPT_DIR,\n         True),\n        ("VOT Cache Manager",\n         "vot_cache_manager.py",\n         "Verify VizieR VOT cache file integrity.",\n         SCRIPT_DIR,\n         True),\n        ("Osculating Cache Manager",\n         "osculating_cache_manager.py",\n         "Load and report on the osculating orbital elements cache "\n         "(two-generation backup, always-prompt workflow).",\n         SCRIPT_DIR,\n         True),\n        ("SIMBAD Query Manager",\n         "simbad_manager.py",\n         "Verify SIMBAD querying against a small sample of objects "\n         "(rate limiting and retry logic).",\n         SCRIPT_DIR,\n         True)'

NEW_BODY = '("Gallery Cache Builder -- Manual Run",\n         os.path.join("tools", "gallery_cache_builder.py"),\n         "Manual serving-cache build. Runs from the gallery repo ROOT: the "\n         "builder resolves its data/ paths from the working directory, so "\n         "launching it from tools/ cannot find data/objects_config.json. "\n         "With no flags it fetches from Horizons, validates, atomic-swaps "\n         "the new cache into data/solar-system, and STOPS -- it does not "\n         "commit or push. Commit it yourself in GitHub Desktop after the "\n         "run finishes. Do not commit while it is still running: mid-build "\n         "the working tree shows deletions only, which is the swap in "\n         "progress, not data loss. The console stays open at the repo root "\n         "if you want a flagged re-run (--dry-run --object <slug>, "\n         "--first-build).",\n         GALLERY_REPO_DIR,\n         True),\n        ("MAINTENANCE RUN -- everything indented below",\n         "orrery_maintenance_run.py",\n         "One command for the whole routine: regenerates the generated "\n         "documents, then runs every checker, then prints one summary. It "\n         "reports and continues rather than stopping at the first failure, "\n         "and says which generated files actually moved. About ten seconds. "\n         "Run after an edit session and before a push. Everything indented "\n         "below is included in it and can still be launched on its own.",\n         SCRIPT_DIR,\n         True),\n        "GENERATORS -- regenerated every run; a no-op when nothing moved",\n        ("Data Inventory",\n         "data_inventory.py",\n         "Inventory the large, gitignored data stores (data/, star_data/). "\n         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Document Index",\n         "doc_index.py",\n         "Regenerate the key-documents table in README.md from the "\n         "one-line Doc-Kind tag each root document carries. The purpose "\n         "text lives in the document it describes, not in this tool and "\n         "not in the README, so the wording stays yours while the table "\n         "stays generated. Three kinds: generated (never hand-edit -- the "\n         "next run destroys the edit), zoned (hand-written prose around a "\n         "marker zone a tool rewrites), and hand. A document with no tag "\n         "is listed as untagged and named in the summary rather than "\n         "quietly dropped. Run after adding, renaming, or retiring a root "\n         "document; --check reports staleness without writing.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Regenerate Module Atlas",\n         "module_atlas.py",\n         "Scan codebase, generate MODULE_ATLAS.md. "\n         "Run after significant codebase changes (new modules, reorganizations).",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Update Ledger Index",\n         "ledger_index.py",\n         "Regenerate the INDEX in LEDGER_CONSOLIDATED.md from the DETAIL blocks "\n         "and migrate DONE items to section C. Run after editing any ledger block.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Update Skill Manifest",\n         "skills_index.py",\n         "Regenerate the Skill Manifest table in the protocol from skills/*/SKILL.md. "\n         "Run after adding, renaming, or versioning a skill.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        "CHECKERS -- these decide the push call",\n        ("Builder Marker Join",\n         "test_worksheet_request_builder.py",\n         "Test that a citation continued onto a marked second line "\n         "(`# Source+:` under `# Source:`) is joined back before the "\n         "request quotes it. Every behaviour is exercised twice, once "\n         "with input that should join and once with input that must NOT: "\n         "a join firing on everything is indistinguishable from a join "\n         "firing correctly, and both report zero problems, so the "\n         "negative cases are the test. The last check runs against the "\n         "real corpus. Run after editing the builder or relabeling a "\n         "continuation.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Constants Change Report",\n         "constants_change_report.py",\n         "Ask git what changed in constants_new.py since the last commit "\n         "and report each moved value in words. The line that matters "\n         "says whether the provenance moved WITH the number: a deliberate "\n         "correction edits the value and its comment block together, "\n         "while corruption -- a bad merge, a stray keystroke, a copied "\n         "stale value -- moves the number alone and leaves the evidence "\n         "describing the old one. Run before committing a change to "\n         "constants_new.py.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Extractor Pins",\n         "test_extractor_pins.py",\n         "Pin the instruction filter\'s kept-and-dropped set at "\n         "LOOKBACK 30 / LOOKAHEAD 25, frozen 2026-08-14. The claim "\n         "ordinal in every issued key -- the `::c2` -- counts claims "\n         "AFTER this filter runs, so extending the instruction pattern "\n         "by one phrase lets a formerly-dropped number join the sequence "\n         "and shifts every ordinal after it with no prose edit at all. A "\n         "worksheet returned against the old ordinals would then bind to "\n         "the wrong claim. It does not decide whether a change is wrong; "\n         "it reports that the extractor no longer means what the issued "\n         "keys assume, and prints the replacement pin file.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Provenance Scanner",\n         "provenance_scanner.py",\n         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "\n         "Run before/after edits to shared values, or when a value looks suspicious.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Citation Inheritance",\n         "test_citation_inheritance.py",\n         "Pass/fail tests for block-scoped citation inheritance in the "\n         "provenance scanner.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Constants Provenance",\n         "test_constants_provenance.py",\n         "Pass/fail regression tests for constants_new.py. "\n         "Run before committing changes to constants, or first if a plot looks wrong.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Cross-Check Annotations",\n         "test_cross_checked.py",\n         "Pass/fail tests for the cross-check annotation grammar and V2 "\n         "scoring. Run after editing annotations or the scanner\'s parser.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Orbit Cache",\n         "test_orbit_cache.py",\n         "Comprehensive test suite for orbit data caching, format conversion, "\n         "and repair. Run alongside Verify Orbit Cache when the cache looks off.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Reset Completeness",\n         "test_reset_completeness.py",\n         "Guard the Reset button against partial-reset drift: dirties every "\n         "tracked control, calls the live reset handler, asserts everything "\n         "returns to its startup default.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Row Shape",\n         "test_status_lines.py",\n         "The row-shape guard by itself. A value that is not a container "\n         "literal must fit on the assignment\'s own line, because "\n         "constants_change_report.py reads values line by line off a git "\n         "diff and once reported a constant REMOVED that was only unreadable. "\n         "Dicts and lists are exempt: a lookup table cannot fit on one line. "\n         "Same script as Test Status Lines, run with --shape-only so it ends "\n         "on its own verdict.",\n         SCRIPT_DIR,\n         True,\n         ["--shape-only"],\n         True),\n        ("Test Scanner Recognition",\n         "test_provenance_1d.py",\n         "Proves the provenance scanner still recognizes a real citation "\n         "and still refuses a fake one. Covers shadow constants (a local "\n         "copy of a value already defined and cited in constants_new.py), "\n         "author-year forms like (Nolan et al. 2013), F/C units, and tier "\n         "labels. Half the tests are written backwards on purpose: a regex "\n         "that is too loose clears findings by matching what it should "\n         "not, and the Tier-1 count then falls, which looks like progress. "\n         "Ledger L-156, sub-steps 1d and 1e.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Status Lines",\n         "test_status_lines.py",\n         "Pass/fail tests for the Status Line grammar on every "\n         "constants_new.py row that carries one, plus coverage on the rows "\n         "that carry none. Runs the row-shape guard as well; Test Row Shape "\n         "below runs that half on its own.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Test Worksheet Checker",\n         "test_worksheet_checker.py",\n         "Pass/fail tests for the worksheet checker. Every layer is "\n         "exercised twice, once with evidence that clears it and once "\n         "with an injected violation that must not, because zero "\n         "findings and a broken check look identical. Run after editing "\n         "the checker or the worksheet schema.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Worksheet Checker",\n         "worksheet_checker.py",\n         "Open the worksheet each cross-check annotation names and report "\n         "whether that worksheet records the check the annotation claims. "\n         "Catches a value edited AFTER its check, which no diff-based tool "\n         "can see once the edit is committed. Report-only -- it writes "\n         "WORKSHEET_CHECK.md and never gates a push. Run after writing "\n         "annotations, after a value moves, or before a gallery build.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Worksheet Key Round Trip",\n         "test_worksheet_keys.py",\n         "Assert that every annotated site mints a key that resolves back "\n         "to it, on every run. A rename breaks it, a split implementation "\n         "between the builder and the checker breaks it, and a change to "\n         "the enclosing-name rule breaks it -- all three loudly, at the "\n         "commit that introduced them, rather than months later when a "\n         "returned worksheet will not bind.",\n         SCRIPT_DIR,\n         True,\n         None,\n         True),\n        ("Add Module Docstrings",\n         "add_docstrings.py",\n         "Add or improve module-level docstrings across the codebase; touches no code. "\n         "Run after adding modules, before regenerating the Module Atlas.",\n         SCRIPT_DIR,\n         True),\n        ("Animation HTML Tool",\n         "measure_animation_html.py",\n         "Measure a saved animation HTML: trace count, frame count, which traces "\n         "are carried inside frames, and frames payload size. Run to compare a "\n         "baseline against a patched export and quantify the frame-fence fix.",\n         SCRIPT_DIR,\n         True),\n        ("Climate Cache Manager",\n         "climate_cache_manager.py",\n         "Safely update the climate data caches, with validation and rollback.",\n         SCRIPT_DIR,\n         True),\n        ("Create Ephemeris Database",\n         "create_ephemeris_database.py",\n         "(Re)build satellite_ephemerides.json from idealized_orbits.py plus "\n         "any downloaded Horizons ephemeris files.",\n         SCRIPT_DIR,\n         True),\n        ("Dependency Trace",\n         "dep_trace.py",\n         "Map who depends on (and is consumed by) a module. "\n         "Run before editing: python dep_trace.py <module_name> [hops]",\n         SCRIPT_DIR,\n         True),\n        ("Export Orbit Cache",\n         "export_orbit_cache.py",\n         "Phase 1b devtool: read the local orbit caches (read-only) and write "\n         "web-servable orbit/position files for the interactive gallery.",\n         SCRIPT_DIR,\n         True),\n        ("Osculating Cache Manager",\n         "osculating_cache_manager.py",\n         "Load and report on the osculating orbital elements cache "\n         "(two-generation backup, always-prompt workflow).",\n         SCRIPT_DIR,\n         True),\n        ("SIMBAD Query Manager",\n         "simbad_manager.py",\n         "Verify SIMBAD querying against a small sample of objects "\n         "(rate limiting and retry logic).",\n         SCRIPT_DIR,\n         True),\n        ("Verify Orbit Cache",\n         "verify_orbit_cache.py",\n         "Back up, validate, and repair orbit_paths.json, reporting any issues. "\n         "Run if orbit plots look wrong or the cache may be corrupted.",\n         SCRIPT_DIR,\n         True),\n        ("VOT Cache Manager",\n         "vot_cache_manager.py",\n         "Verify VizieR VOT cache file integrity.",\n         SCRIPT_DIR,\n         True),\n        ("Worksheet Request Builder",\n         "worksheet_request_builder.py",\n         "Write the cross-check request that goes OUT to a reader. The "\n         "checker reads what comes back; this writes what is sent. Opens "\n         "in its own console because it asks three questions, in this "\n         "order. WHICH ROWS -- a numbered list of named selections; it "\n         "DEFAULTS TO 1, the whole corpus, so type the number you want "\n         "rather than pressing Enter (2 is constants_new.py, the 23-row "\n         "pilot slice). BATCH NAME -- becomes the filename. ANCHOR SHA -- "\n         "the commit the request describes; use current HEAD, and re-run "\n         "if you commit anything before sending it, because a returned "\n         "row is checked against this SHA. It writes "\n         "REQUEST_<batch>.jsonl and REQUEST_<batch>.md into "\n         "documentation/worksheets/ and refuses rather than overwriting "\n         "if either name is taken. Send the .jsonl; the .md is the "\n         "fallback if a return will not parse. It judges nothing -- "\n         "reading the returns is Worksheet Checker, above.",\n         SCRIPT_DIR,\n         True)'

DASH_BRANCH_OLD = '            for i, entry in enumerate(entries):\n                name, script, desc = entry[0], entry[1], entry[2]'

DASH_BRANCH_NEW = "            for i, entry in enumerate(entries):\n                # A bare string is a HEADING inside the group, not a\n                # card. The maintenance runner prints GENERATORS then\n                # CHECKERS, and the indented list here is that same\n                # list, so it reads the same way. Alphabetical order\n                # within each half is Tony's, 2026-09-12: without the\n                # two labels a sorted run of twenty buttons gives no\n                # clue where one kind stops and the other starts.\n                if isinstance(entry, str):\n                    self._build_indent_heading(cards_frame, entry)\n                    continue\n                name, script, desc = entry[0], entry[1], entry[2]"

DASH_METHOD_OLD = '    def _build_launch_card(self, parent, name, script, desc, base_dir,'

DASH_METHOD_NEW = '    def _build_indent_heading(self, parent, text):\n        """A dim heading inside the indented maintenance-run group.\n\n        Drawn for a bare string in a LAUNCH_GROUPS list. Not a card and\n        not clickable: it names which half of the runner the buttons\n        below it belong to.\n        """\n        ctk.CTkLabel(\n            parent, text=text,\n            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w"\n        ).pack(anchor="w", padx=(28, 0), pady=(10, 2))\n\n    def _build_launch_card(self, parent, name, script, desc, base_dir,'

DASH_STAMP_OLD = "gallery repo's tools/ and 8 root-level devtools that were live but\nunlisted."

DASH_STAMP_NEW = "gallery repo's tools/ and 8 root-level devtools that were live but\nunlisted.\nSeptember 12, 2026 with Anthropic's Claude Opus 5 (L-324): added the two\nmissing indented buttons, Test Status Lines and Test Row Shape --\ntest_status_lines.py had been in the maintenance runner since L-305 with\nno button here. Reordered Developer Tools on Tony's instruction: the\nindented group is GENERATORS then CHECKERS, each alphabetical, and the\nstandalone tools below are alphabetical too. A bare string in a\nLAUNCH_GROUPS list is now drawn as a heading."

LEDGER_GAP_OLD = "**Gap:** confirm `Row shape` appears in the dashboard's checker list\nreporting 103 read and 0 wrong, then close. The first half is\nalready confirmed: the run at `6284215b` passed 12 of 12 gating\ncheckers, with the change report reporting no changes to\n`constants_new.py` and the status-line checker clean.\n"

LEDGER_GAP_NEW = "**Note (2026-09-12) -- the runner and the dashboard had drifted, and\nnothing checks that they agree.** Tony went looking for the new check on\nthe dashboard and could not find it. The cause was not the row-shape\nguard: `test_status_lines.py` has been in `orrery_maintenance_run.py`\nsince L-305 and never had a button in `palomas_orrery_dashboard.py` at\nall, so its `--shape-only` half had nowhere to appear either. Diffing\nthe two lists, rather than adding the one button known to be missing, is\nwhat showed it -- 5 generators and 15 checkers in the runner against 18\nindented buttons on the dashboard, exactly TWO absent: Status lines and\nRow shape. Both added. The lists agree at this SHA and nothing enforces\nthat they keep agreeing; that parity check is one row of backlog by\nclass, not built here. [verified @a391262e]\n**Note (2026-09-12) -- the dashboard group is reordered, Tony's\ninstruction.** The indented group is GENERATORS then CHECKERS, each\nalphabetical, mirroring the runner's own two sections; the standalone\ntools below are alphabetical too, sorted case-insensitively so Verify\nOrbit Cache precedes VOT Cache Manager. Every pre-existing entry was\ncarried over byte for byte -- the new list was generated from the file's\nown source text rather than retyped -- so no description, path or flag\nmoved with the sort.\n**Gap:** Mode 5 on the dashboard. The two buttons and the two headings\nbuild and render without error, which is not the same as looking right.\nTony's eyes close this one.\n"

LEDGER_STAMP_OLD = 'line), built on 6284215b.\nReview and RICE update Tony 6-21-2026'

LEDGER_STAMP_NEW = "line), built on 6284215b.\nModule updated: September 12, 2026 with Anthropic's Claude Opus 5\n(L-324: the two missing dashboard buttons added, and Developer Tools\nreordered into GENERATORS and CHECKERS, each alphabetical), built on\na391262e.\nReview and RICE update Tony 6-21-2026"

EDITS = {
    DASH: [
        ("dashboard: Developer Tools reordered, 2 buttons added",
         OLD_BODY, NEW_BODY),
        ("dashboard: a bare string is a heading",
         DASH_BRANCH_OLD, DASH_BRANCH_NEW),
        ("dashboard: _build_indent_heading()",
         DASH_METHOD_OLD, DASH_METHOD_NEW),
    ],
    LEDGER: [
        ("ledger: L-324 parity note, reorder note and Gap",
         LEDGER_GAP_OLD, LEDGER_GAP_NEW),
    ],
}

STAMPS = {DASH: (DASH_STAMP_OLD, DASH_STAMP_NEW),
          LEDGER: (LEDGER_STAMP_OLD, LEDGER_STAMP_NEW)}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    originals = {}

    for path in (DASH, LEDGER):
        full = os.path.join(here, path)
        if not os.path.exists(full):
            print("ERROR: %s not found. Save this script into the orrery "
                  "repo root and Run again." % path)
            return 1
        with open(full, "rb") as handle:
            originals[path] = handle.read()

    for path, data in originals.items():
        try:
            fp = fingerprint(path, data)
        except ValueError:
            print("ERROR: INDEX zone markers not found in %s. NOTHING "
                  "written." % path)
            return 1
        if fp != BASE_FP[path]:
            print("ERROR: base moved. %s does not match the tree this patch "
                  "was built against." % path)
            print("  expected %s" % BASE_FP[path])
            print("  found    %s" % fp)
            print("NOTHING was written, to either file.")
            return 1

    updated = {}
    applied = []
    stamped = []

    for path, data in originals.items():
        is_crlf = data.count(b"\r\n") > 0
        new = data
        todo = list(EDITS[path]) + [
            ("%s: currency stamp" % path,) + STAMPS[path]]
        for label, old, repl in todo:
            o = old.encode("utf-8") if isinstance(old, str) else old
            r = repl.encode("utf-8") if isinstance(repl, str) else repl
            if is_crlf:
                o = o.replace(b"\n", b"\r\n")
                r = r.replace(b"\n", b"\r\n")
            n = new.count(o)
            if n != 1:
                print("ANCHOR FAIL: %s -- expected 1 match in %s, found %d."
                      % (label, path, n))
                print("NOTHING was written, to either file.")
                print("Undo is Discard Changes in GitHub Desktop.")
                return 1
            new = new.replace(o, r)
            if label.endswith("currency stamp"):
                stamped.append(path)
            else:
                applied.append(label)
        non_ascii = sum(1 for ch in new if ch > 127)
        if non_ascii:
            print("ERROR: patch would introduce %d non-ASCII byte(s) into "
                  "%s. NOTHING written." % (non_ascii, path))
            return 1
        updated[path] = new

    # The OUTPUT check. A matching input does not prove a matching
    # output, and the dashboard is the file that was actually launched
    # and rendered in testing -- so compare against that build before
    # writing rather than trusting that the same edits produce it.
    got = hashlib.md5(updated[DASH].replace(b"\r\n", b"\n")).hexdigest()
    if got != RESULT_FP:
        print("ERROR: the patched dashboard does not match the build that "
              "was tested.")
        print("  expected %s" % RESULT_FP)
        print("  produced %s" % got)
        print("NOTHING was written, to either file.")
        return 1

    for path, new in updated.items():
        with open(os.path.join(here, path), "wb") as handle:
            handle.write(new)

    for label in applied:
        print("ok  %s" % label)
    for path in stamped:
        print("stamp updated  %s" % path)
    print("result matches the tested build (%s)" % RESULT_FP)
    print("patch applied (%d files)" % len(updated))
    print("")
    print("NEXT:")
    print("  1. Open the dashboard and look at Developer Tools. Test Row")
    print("     Shape and Test Status Lines are in the indented group,")
    print("     under a CHECKERS heading. Your eyes judge the layout.")
    print("  2. Run ledger_index.py as a parse check -- expect")
    print("     'OK: 319 L-blocks parsed, no consistency problems.'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
