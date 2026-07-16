Thanks -- this matches what we already settled from your first pass on
this (same five-question structure, same measured-rate recommendation,
same Moon evection figure, same tolerance question). Good to see it
reproduce cleanly, but it turns out I attached the wrong file: that was
`FABLE_PROMPT_served_window_trust_bound_v0.1.md`, the original design
question, which is already closed. Tolerance is confirmed at 0.5 deg
(global for now, no basis beyond your own suggestion; per-view is a real
future refinement, not a blocker), and the whole served_window design is
now folded into `PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md`
(status: CONVERGED).

The actual ask this round is attached now:
`FABLE_MANIFEST_PROMPT_F1_v0.2.md`, requesting the executable build
manifest (the contract Opus builds from) against that v0.4 handoff --
not another design review. Please read that prompt fresh; it has its own
instructions (re-pin both repo SHAs, real creative latitude at the
manifest-architecture level, two independent bite-sized chunks). Go
ahead and produce the manifest itself this time.
