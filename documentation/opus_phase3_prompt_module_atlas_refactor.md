I'm working on the Paloma's Orrery project with Tony Quintanilla (PE, retired civil/environmental engineer, not a professional developer -- builds this through AI collaboration, holds sole commit authority). Attached are ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md (the L-163 design), AS_BUILT_L163_phase1.md, and AS_BUILT_L163_phase2.md. Phases 1-2 are done and verified -- this is Phase 3, the classifier code.

Built on:

orrery: [paste orrery SHA here after pushing] at https://github.com/tonylquintanilla/palomas_orrery
gallery: [paste gallery SHA here after pushing] at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Pull both repos fresh and confirm these SHAs still match before building on anything load-bearing. If they don't, stop and flag the mismatch.

Load agentic-pre-test, safe-file-editing, ledger-and-session-records, and provenance-discipline.

Phase 3a -- re-verify before writing anything new. Phase 2's as-built went through two rounds of close-out fixes (a tag-refresh bug that silently deleted a prose sentence, and three confirmed classification decisions that hadn't reached the code) plus a later scope widening (gallery now scans its own repo root too). All of that was verified by re-running the actual tool and checking file content directly -- but not by launching the GUI. Before touching any classifier code: py_compile/compileall both repos, then run the full agentic-pre-test GUI-launch check on palomas_orrery.py under xvfb (throwaway copy, SystemButtonFace swap) against the current, fully-tagged state of all 114 modules. Confirm it reaches GUI init and center-body registration cleanly, same bar as Phase 2's original check. Report this back on its own before proceeding -- if anything's off, stop there.

Phase 3b -- the classifier code, gated on 3a coming back clean. [... rest of Phase 3 exactly as before: sentinel name decided as undetermined; new parser reusing ast.get_docstring(); classify_role() rewrite; UNCATEGORIZED/UNDETERMINED report section, updating all three of ROLE_ORDER/ROLE_DESCRIPTIONS/ROLE_SECTION_TITLES; gallery's widened root-inclusive SCAN_PATHS mirrored here; the three call-site updates, including removing dep_trace.py's now-confirmed-dead elif mod in ROLE_MAP: branch; the one-line export_orbit_cache.py docstring fix.]

Map all three call sites before touching any of them. Mode 2 (agentic) for the new parser and report section; Mode 1 (targeted) everywhere you're editing module_atlas.py's existing functions. Full agentic-pre-test protocol before delivery, not py_compile alone. Credit line on every touched module.

Out of scope: domain-code retirement (MODULE_DOMAIN_MAP) and anything in the L-154 through L-162 cluster.

When you report back: lead with what actually happened, not a narration of the plan. Deliverable: a short as-built note per sub-phase, pushed with the standard SHA round trip.

Load agentic-pre-test, safe-file-editing, ledger-and-session-records, and provenance-discipline.

The sentinel name is decided: undetermined (not UNCLASSIFIED). Write it into the code as such.

The job: every module in both repos now carries a Role:/Domain: line in its docstring (Phase 2, closed). Nothing reads them yet -- module_atlas.py's classify_role() still uses the old hand-maintained ROLE_MAP dict. Build the reader:

New parser. Given a module's source, extract its Role: and Domain: values from the docstring (reuse ast.get_docstring(), which module_atlas.py already calls elsewhere -- don't reinvent docstring location). Missing or unrecognized tag -> undetermined, never guessed.
classify_role() rewrite. Reads the parsed tag instead of ROLE_MAP. ROLE_MAP itself becomes a regenerated marker-zone (same pattern ledger_index.py already uses for its INDEX zone), not hand-edited again.
UNCATEGORIZED/UNDETERMINED report section in both MODULE_ATLAS.md and MODULE_INDEX.md, so anything unclear is visible, not silently dropped. Note: ROLE_ORDER, ROLE_DESCRIPTIONS, and ROLE_SECTION_TITLES in module_atlas.py are three separate structures that currently agree on the same 12 role values -- adding the undetermined sentinel means updating all three, or undetermined modules silently vanish from the index instead of showing up in the report section meant to surface them.
Gallery copy. Its SCAN_PATHS now includes the repo root as well as the four module directories (widened in Phase 2's close-out, so add_docstrings.py itself gets classified) -- mirror that same root-inclusive scope here, with multi-path merge and collision-flagging.
Three call-site updates: module_atlas.py, provenance_scanner.py (classify_role() call at its own scan loop), dep_trace.py. For dep_trace.py: its import-failure fallback has a hardcoded duplicate _shells heuristic and a silent 'other' default -- both real, both get dropped. Its elif mod in ROLE_MAP: branch is currently unreachable dead code (the except branch sets ROLE_MAP = {}, so that branch never fires) -- remove it along with the rest of the fallback cascade, don't preserve it.
One-line housekeeping while you're in export_orbit_cache.py: its docstring still tells the reader to "add a ROLE_MAP entry" -- stale advice now that tags live in docstrings. Fix the line.

Map all three call sites before touching any of them. Mode 2 (agentic) for the new parser and report section; Mode 1 (targeted) everywhere you're editing module_atlas.py's existing functions. Full agentic-pre-test protocol before delivery, not py_compile alone. Credit line on every touched module.

Out of scope: domain-code retirement (MODULE_DOMAIN_MAP) and anything in the L-154 through L-162 cluster -- tracked separately.

When you report back: lead with what actually happened, not a narration of the plan. Deliverable: a short as-built note, pushed with the standard SHA round trip. This is Phase 3 only -- stop and report before Phase 4 (verify, then update the two skill docs).