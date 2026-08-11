LESSONS REMOVED FROM PROJECT_INSTRUCTIONS.md AT v3.37

August 11, 2026. Working copy at the time was 824 lines; repo HEAD was
22b0db339e0ce99ca0a6a6dc11f1c9546845577f at
https://github.com/tonylquintanilla/palomas_orrery.

THIS FILE IS A RECORD, NOT A STORE. Nothing in it is load-bearing. Every
bullet below was removed from the protocol's Part 5 Lessons Archive
because the same instruction is already stated somewhere that FIRES -- a
Part 3 CRITICAL gate, a Part 2 or Part 4 section, an Anti-Patterns row, a
Mode 7 table, a Quotable, or a skill that loads on task match. Each entry
names where it still lives.

The lessons that exist in only one place are NOT here. They stayed
resident in the protocol, which is the point of the cut.

Why this file was briefly something else. An earlier version of this
trim moved all forty-one lessons here and left the protocol with only a
pointer. That was wrong and was reversed the same day. A skill fires on
task match and the ledger is read at session start, but an archive file
has no trigger -- so the fourteen lessons with no counterpart elsewhere
would have quietly left the system. The v3.30 precedent, where technical
lessons went into skills, does not transfer, because skills fire.

If any line below turns out to be doing work its counterpart does not do,
put it back in the protocol. That judgment is Tony's, and this file exists
so it can be made by reading rather than from memory.


1. Map multi-file changes before implementing. Parallel pipelines: fix in one doesn't propagate
   STILL STATED IN: Part 2 Multi-File Changes; Part 3 Check All Parallel Pipelines [CRITICAL]

2. Unicode in generated files breaks on Windows -- use ASCII
   STILL STATED IN: Part 2 Anti-Patterns, 'Use unicode in code'; safe-file-editing Encoding Gate

3. Agentic = confident but harder to review; targeted = visible changes
   STILL STATED IN: Part 2 Agentic vs Targeted Choice table

4. Multi-AI: Gemini for domain knowledge, Claude for implementation, Tony integrates
   STILL STATED IN: Part 1 Mode 7 AI Roles table

5. Iterative design beats first-draft architecture -- each round should simplify
   STILL STATED IN: Part 2 Iterative Design Planning; Anti-Patterns 'Build first architecture'

6. Gallery pipeline: HTML export -> JSON converter -> gallery viewer
   STILL STATED IN: gallery-pipeline skill (fires on gallery work)

7. Flag-based contracts: _studio means "trust this, don't override." Strip unconditionally before guards
   STILL STATED IN: Part 2 Anti-Patterns, 'Guard strips with if list:'; gallery-pipeline skill

8. Renderer refactor: extract duplicated inline code into source module
   STILL STATED IN: Part 2 Anti-Patterns, 'Duplicate rendering -> Extract to source module'

9. /mnt/project/ is a read-only snapshot from session start. Does not update mid-session
   STILL STATED IN: Part 1 Context Priority 'Project file staleness'; Part 3 Uploads Before Project Files [CRITICAL]

10. Collegial Mode 7: Claude-to-Claude relay via Tony. No orchestration -- "here's the job, flag problems"
   STILL STATED IN: Part 1 Mode 7 Patterns table, 'Collegial'

11. LOTO lesson: critical failures happen when procedures are not developed, not enforced, or not followed -- all three are distinct. The most critical procedure is often the one that feels unnecessary right up until it isn't
   STILL STATED IN: Part 2 Procedural Criticality, closing paragraph (LOTO, verbatim)

12. Map the dispatch before editing the leaves: grep for where a function is CALLED, not imported. Compile-clean and tests-pass do not detect that a function is never called
   STILL STATED IN: Part 3 Verify Execution, Not Appearance [CRITICAL] -- verbatim

13. Structural fixes scale; data-side fixes don't. A violation in N consumers of one producer -> fix the producer. (83 sphere-shell pairs brought into compliance by 2 edits to the factory)
   STILL STATED IN: Part 5 Quotables, 'fix the producer'; Part 2 Anti-Patterns

14. Handoffs are claims; runtime output is fact. When a smoke test contradicts a handoff, the smoke test wins and the handoff gets corrected
   STILL STATED IN: Part 2 Anti-Patterns, 'handoff is a claim, render is fact'

15. Data-content sweeps (hover text, legendgroup, marker styling) need a runtime smoke test that constructs and inspects traces on the LIVE dispatch -- a smoke test of the wrong path passes falsely
   STILL STATED IN: Part 3 Agentic Pre-Test [CRITICAL]; agentic-pre-test skill

16. Transactional binary-mode patching for clustered edits: one script, anchored byte-level replaces, each asserting exactly one match -- all-or-nothing, fails loud on drift
   STILL STATED IN: safe-file-editing skill, 'Transactional Patching for Clustered Edits'

17. Assign, don't hardcode, to stay in the house pattern: define color = 'white' once, reference it from both line and marker -- one-line restyle later
   STILL STATED IN: orrery-coding-conventions skill

18. Enumerate uploaded files before claiming a review: the in-context subset is invisible to Tony and not authoritative. Read the whole set on disk first (lesson: a review and a protocol edit were both built on 9 of 19 handoffs)
   STILL STATED IN: Part 3 Enumerate Uploads Before Claiming a Review [CRITICAL] -- verbatim

19. Floating items get lost; capture on first mention. A bug "floating outside the deferred list" only closed when Tony asked "is this deferred?" -- promote observations into the ledger immediately, even if no work happens yet
   STILL STATED IN: Part 5 Quotables, 'Floating items get lost; capture on first mention'

20. Verify universal-propagation claims with grep. "A central factory exists" does not imply "every call site uses it" -- grep the actual call sites when propagation is load-bearing; don't trust the handoff narrative
   STILL STATED IN: Part 5 Quotables, 'Grep, don't trust the narrative'

21. Tony's session loop makes the repo trustworthy: sandbox -> test -> local repo -> provenance/atlas update -> push, all before a new session. Because the push precedes the session, repo HEAD == session-start ground truth by construction
   STILL STATED IN: Part 3 Session-Start Repo Pull [CRITICAL] -- states the loop verbatim

22. Route around a fragile store you do not control to one you do: project knowledge proved it could be stale and haunted; the repo is Tony's, so make it the build base -- and ultimately remove the fragile store entirely (v3.30, July 2026)
   STILL STATED IN: Part 5 Quotables, 'Route around the store you don't control'

23. Irreducibility protects both sides equally
   STILL STATED IN: Part 4 The Irreducibility Argument

24. Hassabis corroboration: AI's limitations map to why partnership outperforms autonomy
   STILL STATED IN: Part 4 The Hassabis Corroboration

25. The Double-Helix IS the safety mechanism: error-correction and alignment are the same loop
   STILL STATED IN: Part 4 The Double-Helix IS the Safety Mechanism

26. The Weasley Principle: the vulnerability comes when the conversation becomes the only conversation
   STILL STATED IN: Part 4 The Weasley Principle

27. Broad-first requires judgment to recognize convergence. That judgment is Tony's
   STILL STATED IN: Part 4 Broad-First as Valid Methodology
