Built on 23635820b155103d01e4fe65b6c4b63901c0213b at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Task: build Phase 1c — the citation-window inheritance fix for provenance_scanner.py (L-156 Gap item 6). The attached predesign document is yours from this cluster's last session; it's been independently re-verified against live HEAD (Sonnet 5) and holds except for one internal table. Everything else in it — the mechanism recommendation, the edge cases, the Jupiter/Moon findings, the idealized_orbits.py exclusion — is confirmed and build-ready.

The one correction: the predesign's §3 table says "22 from SHELL_CONFIGS, 1 from CUSTOM_SHELLS." That's wrong. Independently verified split is 21 from SHELL_CONFIGS, 2 from CUSTOM_SHELLS — same total of 23, just a different breakdown (CUSTOM_SHELLS['Jupiter'] and CUSTOM_SHELLS['Saturn'] both test cited, not just one). This doesn't change anything about the mechanism or the predicted Tier counts below — just don't build against the predesign's own table if you re-derive it, use this one. Full verification trail is in L-156's 2026-07-30 Note in the ledger, at this SHA.

Explicitly out of scope: the 18 genuinely-uncited-block findings the predesign surfaced (Pluto/Venus/Eris/Mars/CUSTOM_SHELLS['Mercury']) are real citation gaps, not a scanner bug — they're tracked separately as L-173 and need actual sourcing (Gemini worksheet), not a scoring change. 1c should leave them at Tier 1/V4 exactly as they are now. Do not attempt to resolve or route around them in this build.

Build the mechanism as your predesign specified (option b, precomputed range table):

Single ast.walk pass over all ast.Assign nodes at any nesting depth (catches both shell_configs.py's module-level dicts and jupiter_visualization_shells.py's function-local ring_params). For each dict-valued entry, record (dict_name, key, block_start, block_end, citation_line, citation_text).
Named lookback constant, value 15, applied above both the block key and the enclosing assignment — justify the value in a comment (8 covers shell_configs.py, 15 covers the Jupiter case with margin).
No fallback for uncited blocks — this is the load-bearing invariant. An uncited block's contents inherit nothing, stay V4 RECALLED, land nowhere near this fix. If your implementation has any path where an uncited block resolves to an outer/module-level citation, that's the bug this whole predesign exists to prevent.
Nested blocks → innermost citation wins (narrowest containing span).
No cross-dict inheritance — SHELL_CONFIGS['Jupiter'] and CUSTOM_SHELLS['Jupiter'] have different citations and must not merge. Write an explicit test for this; a name-keyed implementation would get it wrong silently.
Multi-line citations → capture the whole contiguous comment run (walk up from the matched line to the top of the run), not just the single matched line.
Explicit scope declarations (Scope of the above citation:) → detect and decline to inherit; flag the block for review instead. One live instance today (ring_params's ring-geometry-only scope).
Inheriting strings score V3 SOURCED — no new rung, no change to 1b's ladder.

Predicted outcome (verify against, don't just assert): Tier 1 156 → ~132, Tier 2 563 → ~587, Tier 3 60 unchanged, Tier 4 2 unchanged, total 781 conserved. Invariant to assert directly in the build: 1c changes vulnerability only, on a population that's entirely display strings at C_PUBLIC=4 — nothing can enter Tier 1, Tier 3/4 cannot move. Treat any deviation as a bug to investigate, not a surprise to rationalize.

Delivery format (safe-file-editing v1.1): anchored transactional patch script, same shape as 1a/1b — EXPECTED_MD5 base-file guard (current provenance_scanner.py is 94891f347cfe1b46bf14020468571993 at this SHA), bottom-up edits, one ok/ANCHOR FAIL line per edit, VS Code Run button framing. Run the agentic pre-test protocol (py_compile, throwaway-copy xvfb run, live-dispatch smoke test) before delivering. Module credit line on provenance_scanner.py.

Everything else this cluster has established (L-156, L-158's inheritance precedent, the ladder itself from 1b) is live in the ledger at this SHA if you want to check it directly rather than take this prompt's word for it.