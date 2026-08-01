# Build Prompt — Fix `build_pinned_values()` citation bleed

**Built on `8bd7778dd3ce8f92f8205da3bd64cf016f8e0358`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## The problem

`build_pinned_values()` (line 1409 of `provenance_scanner.py`) uses a
10-line window to decide whether a constant in `constants_new.py` is
cited. If constant A has a citation and constant B sits within 10 lines
below it with no citation of its own, B falsely inherits A's citation
and enters the pinned set. This inflates Option A's scoring — display
strings get V_SOURCED credit based on constants whose citations don't
actually exist.

## The fix

The correct approach already exists in the same file: today's build
added `build_cited_constant_names()`, which reads only the contiguous
comment run physically touching each assignment. No window, no bleed,
proven and tested (15/15 in `test_provenance_1d.py`).

Replace `build_pinned_values()`'s citation-detection logic with the
same contiguous-comment-run approach used by `build_cited_constant_names()`.
The return value and the interface to Option A are unchanged — only the
method of deciding "is this constant cited" gets tightened.

## What to expect

The pinned set will shrink — constants that were falsely included via
neighbor bleed will drop out. Some display strings Option A currently
credits may lose V_SOURCED and move toward Tier 1. This is correct
behavior: they were getting credit they didn't deserve.

Measure before and after. Report the delta the same way Phase 1 has
throughout — isolated, with the cause named.

## Scope

This is a single-mechanism fix in `provenance_scanner.py`. No other
files touched. Same patch conventions as 1d/1e/1f: MD5 guard, anchored
transactional, bottom-up, binary mode, py_compile, ASCII/LF gates.
Run all three test suites after patching (test_provenance_1d 15,
test_citation_inheritance 20, test_constants_provenance 73).

This does NOT retire Option A (D8.5 remains open). It makes Option A's
input data correct.

## Reference

- `provenance_scanner.py` at HEAD: `build_pinned_values()` (line 1409),
  `build_cited_constant_names()` (today's addition), Option A scoring
  (lines 1563-1577)
- `AS_BUILT_L156_phase1d_e_f.md` section 6: documents the bleed flaw
- `provenance-discipline/SKILL.md` v1.3: No Shadow Constants [CRITICAL]

---

*Build prompt drafted July 31, 2026 by Claude Opus 4.6.*
