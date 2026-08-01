# Build Prompt — Retire Option A (D8.5)

**Built on `adc9b20d2e6533c25544d565430336f835e87a48`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are the builder. You built all of Phase 1 (1a-1f) and the
`build_pinned_values()` bleed fix. You know the scanner's internals.

## The decision

Tony has decided to retire Option A. The reasoning: Option A grants
V_SOURCED to display strings based on numeric coincidence (values
matching `constants_new.py`), not actual sourcing. That's credit without
provenance — the same failure class the scanner exists to prevent. A
match on 0.5 or 10.0 means nothing; even a 6-digit match proves the
numbers are the same, not that the programmer derived the value from the
constant. Suspicious matches already have the right home: the
shadow-constant detector (diagnostic, advisory). Scoring credit for
unverified matches is exculpatory, not advisory, and suppresses findings
that should be visible.

## What to remove

Option A lives in `score_unit()` at lines 1563-1577 of
`provenance_scanner.py`. It checks whether an uncited display string's
numeric claims all match pinned constant values, and if so grants
V_SOURCED. Remove this scoring block.

`build_pinned_values()` itself (line 1409) may or may not still have
callers after Option A is removed. Check: if nothing else uses the
pinned-values dict, remove `build_pinned_values()` too and the call at
line 1872. The shared `constant_has_own_citation()` predicate (today's
bleed fix) is used by `build_cited_constant_names()` for the shadow-
constant detector — that stays regardless.

If `build_pinned_values()` is used elsewhere (e.g., in the report or
diagnostics beyond Option A scoring), leave it and just remove the
scoring block.

## What to expect

The 18 display strings Option A currently credits will lose V_SOURCED
and become visible as uncited findings. Measure the tier impact: how many
move to Tier 1 vs Tier 2, and which modules they're in.

This may increase the Tier-1 count again. That is correct — these are
findings that should have been visible all along.

## Scope

Single-mechanism removal in `provenance_scanner.py`. No other files.
Same patch conventions as the Phase 1 builds: MD5 guard, anchored
transactional, bottom-up, binary mode, py_compile, ASCII/LF gates.
Run all three test suites after patching (test_provenance_1d 20,
test_citation_inheritance 20, test_constants_provenance 73). If any
existing test asserts Option A behavior, update the test to reflect
the removal.

Update the scanner's module docstring to remove references to Option A
as a live mechanism. Add a credit line.

## Check for related failure points

Option A is the known instance of credit-without-sourcing. Before
closing D8.5, audit the scanner for any other places where the same
pattern exists — scoring credit based on coincidence, pattern matching,
or indirect inference rather than an actual citation. This includes any
path where a finding's vulnerability score improves without a real
`# Source:` / `# Verified:` / author-year citation being present.

If you find any, flag them with the specific mechanism and where it
fires. Tony wants to know whether Option A was the only instance of
this failure class or whether there are others.

## What this closes

D8.5 in the design handoff. Note the closure in L-156.

## Reference

- `provenance_scanner.py` at HEAD: `score_unit()` Option A block (lines
  1563-1577), `build_pinned_values()` (line 1409), call site (line 1872),
  `build_cited_constant_names()` and `constant_has_own_citation()` (the
  shadow-constant detector, unchanged)
- `AS_BUILT_L156_phase1d_e_f.md` section 3: documents why 1d diverged
  from amending Option A
- L-156 in LEDGER_CONSOLIDATED.md: D8.5 reference

---

*Build prompt drafted August 1, 2026 by Claude Opus 4.6.*
