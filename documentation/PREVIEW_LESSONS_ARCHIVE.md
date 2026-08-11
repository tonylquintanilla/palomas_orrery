LESSONS ARCHIVE -- Paloma's Orrery

Cut from PROJECT_INSTRUCTIONS.md v3.36 on August 11, 2026, at
22b0db339e0ce99ca0a6a6dc11f1c9546845577f
at https://github.com/tonylquintanilla/palomas_orrery.

These are the PROCESS and PHILOSOPHICAL lessons. They were resident in the
protocol from its earliest versions through v3.36, and were moved here to
bring the protocol back under 850 lines. Nothing was reworded or dropped:
the two lists below are the protocol's own text, verbatim.

The TECHNICAL lessons are not in this file. They were distributed into the
skills as field notes at v3.30 and live in skills/<name>/SKILL.md under
"Field Notes".

Why this file exists rather than a ledger appendix. Through v3.36 the
protocol stated that the complete archive was preserved verbatim in
LEDGER_CONSOLIDATED.md's Protocol Version History appendix. It was not, and
had never been -- that appendix is a per-version change log, one entry per
protocol version, and carries none of these lines. So from v3.30 to v3.36
the protocol described a backup that did not exist, and the lists were
resident in exactly one place while the document said otherwise. Writing
them here makes the pointer true for the first time.

That gap is itself an instance of the L-190 second class: a claim about the
project that no tooling checks. Nobody was careless. There was simply
nothing that could have caught it.

Process:
- Bugs become lessons when documented. Stories make science memorable
- Map multi-file changes before implementing. Parallel pipelines: fix in one doesn't propagate
- Unicode in generated files breaks on Windows -- use ASCII
- Agentic = confident but harder to review; targeted = visible changes
- Multi-AI: Gemini for domain knowledge, Claude for implementation, Tony integrates
- Iterative design beats first-draft architecture -- each round should simplify
- Gallery pipeline: HTML export -> JSON converter -> gallery viewer
- Flag-based contracts: _studio means "trust this, don't override." Strip unconditionally before guards
- Pure design sessions (zero code) are first-class outputs
- Derive from known quantities, don't estimate manually
- Renderer refactor: extract duplicated inline code into source module
- Module Atlas as prompt artifact: complete and current reference for codebase-aware sessions
- /mnt/project/ is a read-only snapshot from session start. Does not update mid-session
- Collegial Mode 7: Claude-to-Claude relay via Tony. No orchestration -- "here's the job, flag problems"
- LOTO lesson: critical failures happen when procedures are not developed, not enforced, or not followed -- all three are distinct. The most critical procedure is often the one that feels unnecessary right up until it isn't
- Map the dispatch before editing the leaves: grep for where a function is CALLED, not imported. Compile-clean and tests-pass do not detect that a function is never called
- Structural fixes scale; data-side fixes don't. A violation in N consumers of one producer -> fix the producer. (83 sphere-shell pairs brought into compliance by 2 edits to the factory)
- Handoffs are claims; runtime output is fact. When a smoke test contradicts a handoff, the smoke test wins and the handoff gets corrected
- Data-content sweeps (hover text, legendgroup, marker styling) need a runtime smoke test that constructs and inspects traces on the LIVE dispatch -- a smoke test of the wrong path passes falsely
- Transactional binary-mode patching for clustered edits: one script, anchored byte-level replaces, each asserting exactly one match -- all-or-nothing, fails loud on drift
- Assign, don't hardcode, to stay in the house pattern: define color = 'white' once, reference it from both line and marker -- one-line restyle later
- Fixing an invisible thing surfaces its neighbors. Budget for "now I can see it's too close to its neighbors" as the follow-on to any "nothing renders" fix
- Enumerate uploaded files before claiming a review: the in-context subset is invisible to Tony and not authoritative. Read the whole set on disk first (lesson: a review and a protocol edit were both built on 9 of 19 handoffs)
- Floating items get lost; capture on first mention. A bug "floating outside the deferred list" only closed when Tony asked "is this deferred?" -- promote observations into the ledger immediately, even if no work happens yet
- Verify universal-propagation claims with grep. "A central factory exists" does not imply "every call site uses it" -- grep the actual call sites when propagation is load-bearing; don't trust the handoff narrative
- Central factories need explicit migration intent: migrate-in-scope, defer-with-tracked-backlog, or declare new-code-only. The danger zone is the unstated fourth option (factory exists, no plan) -- it gets quoted as a standard while call sites bypass it
- Testing iterates in dependency order: regression gate, then features, then animation. Some bugs are only findable in later rounds (the Sun-checkbox-off bug needed Round 3). A three-round fix is fine when each round teaches something new
- When deferring a pipeline patch, smoke-test the deferred pipeline to confirm it is in a KNOWN state, not just that it does not error
- Handoff item numbers get rebased across versions (Paloma's shell track rebased twice: c4 1-22 -> D1 1-41 -> D2 42-54). A number means different things in different handoffs; items leak at the rebase. One authoritative running ledger beats per-handoff renumbering
- Tony's session loop makes the repo trustworthy: sandbox -> test -> local repo -> provenance/atlas update -> push, all before a new session. Because the push precedes the session, repo HEAD == session-start ground truth by construction
- Route around a fragile store you do not control to one you do: project knowledge proved it could be stale and haunted; the repo is Tony's, so make it the build base -- and ultimately remove the fragile store entirely (v3.30, July 2026)
- Skills are stores too: author them in the repo, version them, SHA-stamp them, and let the ledger log their changes -- an unversioned knowledge layer is the drift class this protocol exists to kill

Philosophical:
- The project makes Tony more informed -- that's the real output
- Design gets simpler through conversation; it gets more complex through autonomous iteration
- Irreducibility protects both sides equally
- Hassabis corroboration: AI's limitations map to why partnership outperforms autonomy
- The Double-Helix IS the safety mechanism: error-correction and alignment are the same loop
- The Weasley Principle: the vulnerability comes when the conversation becomes the only conversation
- Broad-first requires judgment to recognize convergence. That judgment is Tony's
- Procedure-to-judgment ratio scales inversely with experience and accumulated shared context. New project: more procedure. Mature partnership: more freedom. The skill is knowing which rules are load-bearing
- "Tony's eyes win" extends to beauty, not just correctness: the render that confirmed the frames were right was the one that was beautiful -- and those turned out to be the same thing
