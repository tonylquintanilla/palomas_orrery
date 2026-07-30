Where we are 7/30/2026 12:14 PM

Interactive gallery build (the master plan's own Phase 0–6): Phase 0 (stack proof, architecture B′) and Phase 1a (vocabulary) are done. Phase 1b (data serving pipeline — nightly cache builder, coverage index, served_window trust system) is DONE — Layer 1/2 both closed and tested; Layer 3 (Task Scheduler) is live with a known intermittent promotion-step glitch still being watched.

Phase 2 (current phase) — the artifacts themselves:

Artifact 1 (Earth) — built, Mode-5 accepted. Closed.
Artifact 2 (Jupiter/Saturn: rings, shells, radiation belts) — next in line, and blocked. Not on data — the cache builder already serves the real ported values (Earth atmosphere/Van Allen, Jupiter rings/belts, Saturn's 7 rings). It's blocked because the client-side JS layer that would actually draw those features (L-154) doesn't exist anywhere in the repo yet.

Why that's still blocked — the detour: scoping L-154 surfaced a real problem in provenance_scanner.py's scoring model (foundational constants like SUN_RADIUS_KM were scoring as low-priority because criticality was import-count-based). That became its own cluster, L-154 through L-162. Design and ledger formalization for the whole cluster are closed. The scanner rebuild itself (Opus 5, Phase 1 sub-stepped 1a–1f) is in progress: 1a done, 1b just landed and pushed (bf36743), 1c–1f remain — 1c (citation-window inheritance) is next. Once Phase 1 closes, L-157/L-161 (the Gemini cross-check sweeps) run, then L-154's own design questions (geometry-building approach, legend behavior, artifact sequencing) resume, then Artifact 2 actually gets built.

Adjacent, already resolved: L-162 (CENTER_BODY_RADII naming) is done — confirmed directly in constants_new.py earlier this session. L-163 (module role/domain classification) — role side fully closed; domain side deliberately deferred into this same cluster.

So: provenance scanner 1c is the very next build step, and it's the last thing standing between here and getting back to Artifact 2.