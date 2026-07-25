I'm working on the Paloma's Orrery project with Tony Quintanilla (PE, retired civil/environmental engineer, not a professional developer -- builds this through AI collaboration, holds sole commit authority). Attached are ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md (the L-163 design, Sonnet 5, reviewed by Fable 5) and AS_BUILT_L163_phase1.md (your own Phase 1 close-out). Phase 1 is done and verified -- this picks up at Phase 2.

Built on:

orrery: dcfe207101bdbbb934f5fd02759e46d39df74a74 at https://github.com/tonylquintanilla/palomas_orrery
gallery: 22c947c993a0d3e5f1aa9390288c28bcd2710275 at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Pull both repos fresh and confirm these SHAs still match before building on anything load-bearing. If they don't, stop and flag the mismatch.

Load agentic-pre-test, safe-file-editing, ledger-and-session-records, and provenance-discipline -- all four fire on this work.

Two design questions from the handoff are now decided -- don't re-litigate them:

Tag placement. Footer block: Role: and Domain: each on their own line, blank-line separated, directly above the existing Module updated: [Month Year] with Anthropic's Claude [model]. credit line. Modules with no credit line get the block at the end of the docstring instead.
Sentinel name. undetermined (not UNCLASSIFIED).

Build session, Phases 2-4, strictly gated -- stop and report back after each phase.

Phase 2 (content sweep, still no classifier code). add_docstrings.py can't run this sweep as written -- it replaces a module's whole docstring from a hand-authored dict; this job needs to insert 1-2 lines into ~136 mostly-existing orrery docstrings and ~22 gallery ones, leaving the rest untouched. Two known defects to fix while extending it (found during Phase 1, not new): has_leading_comment() is defined but never called, so a shebang-first module like ledger_index.py would get the new lines inserted above the shebang; and it currently locates the docstring by scanning for the first literal triple-quote rather than parsing -- switch that to ast.get_docstring(). Keep its binary-mode I/O, per-file line-ending detection, and preview/--write split as-is. Preview mode first, across both repos, nothing written. Stop there -- Tony reviews the preview against all three docstring shapes (credit line present / absent / shebang-first) before written mode runs at scale.

Phase 3 (classifier code, gated on Phase 2 fully done). New raw-docstring parser reading ast.get_docstring(), regex-matching Role:/Domain:; classify_role()'s 3-state rewrite (valid tag / legacy fallback during rollout / undetermined); ROLE_MAP's regeneration marker-zone (same pattern as ledger_index.py's INDEX zone); the UNCATEGORIZED/UNDETERMINED report section in both MODULE_ATLAS.md and MODULE_INDEX.md; SCAN_PATHS multi-path merge with collision-flagging for the gallery copy; the three call-site updates (module_atlas.py, provenance_scanner.py, dep_trace.py); dropping dep_trace.py's duplicated fallback cascade. Map all three call sites before touching any of them. Mode 2 (agentic) for the new parser and report section; Mode 1 (targeted) everywhere you're editing module_atlas.py's existing functions. Full agentic-pre-test protocol before delivery, not py_compile alone. Credit line on every touched module.

Phase 4 (verify, then document -- gated on Phase 3 actually running, not just built). Run the shipped classifier against the swept docstrings; confirm ROLE_MAP regenerates as expected and every undetermined entry is accounted for. Only then update ledger-and-session-records's Codebase Tooling note and provenance-discipline's role-driven-inclusion bullet. Do NOT touch provenance-discipline's "Report Domain Classification" section -- that's a different build, gated on this sweep completing first. Bump ledger-and-session-records 1.3 -> 1.4 and provenance-discipline's version + source-SHA line.

Leave the domain-code retirement, gallery Domain: tag consumption, and anything in the L-154 through L-162 cluster alone -- out of scope here.

When you report back after each phase: lead with what actually happened, not a narration of the plan.

Deliverable per phase: a short as-built note, pushed with the standard SHA round trip.