# Ledger note -- L-156 Phase 1c (paste-ready)

Built on `cf061d7336cfed20a991218deec8b666e08d31b7`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Two blocks below. The first goes into **L-156**, appended after the
existing `Note (2026-07-30, 1c predesign verified)` paragraph. The second
is a one-line touch to **L-173**. Run `ledger_index.py` afterward to
regenerate the index zone -- do not hand-edit it.

Neither block changes any `status:` field. L-156 stays OPEN (Gap items 7+
remain); L-173 stays OPEN.

---

## Block 1 -- append inside L-156

```
Note (2026-07-30, 1c BUILT): Built on 23635820 at session start; HEAD moved to
cf061d7336cfed20a991218deec8b666e08d31b7 mid-session (Tony's push of the build
prompt itself, one file, 24 insertions). provenance_scanner.py byte-identical
across the move -- MD5 94891f347cfe1b46bf14020468571993 at both SHAs -- so the
patch guard stayed valid and no rebuild was needed. Delivered two uncommitted
files: patch_phase1c_citation_inheritance.py (12-edit anchored transactional
patch, MD5 guard, ASCII/LF gates on the result, refuses re-run with the cause
named) and test_citation_inheritance.py (16 tests, test_constants_provenance.py
conventions, synthetic fixtures plus four live-repo relationship tests).
Mechanism as specified: CITATION_LOOKBACK_BLOCK = 15 named and justified;
single ast.walk over all ast.Assign at any depth (reaches function-local
ring_params); assignment-level and entry-level blocks both recorded; whole
contiguous comment run captured (the Moon block's match is a continuation
line, so single-line capture would have dropped Weber 2011 and Draper 1847);
line-range keying makes cross-dict inheritance structurally impossible;
inheriting strings land V_SOURCED, no new rung. MEASURED, clean clone,
apply/test/scan: Tier 1 156 -> 133, Tier 2 563 -> 586, Tier 3 60 and Tier 4 2
unmoved, 781 conserved, nothing entered Tier 1, all movement confined to
shell_configs.py. The 21/2 split re-derived independently from the audit and
CONFIRMED (SHELL_CONFIGS: Earth 8, Jupiter 6, Moon 4, Mercury 2, Planet 9 1 =
21; CUSTOM_SHELLS: Jupiter 1, Saturn 1 = 2) -- the predesign's own 22/1 table
is wrong, the prompt's correction stands. The 18 L-173 findings match that
table exactly and were left untouched. TWO ACCOUNTING CORRECTIONS to the
prediction, neither a build defect. (a) Tier 1 is 133, not ~132: the predesign
is internally inconsistent, counting 24 inheriting in its headline while its
own Section 7 requires the jupiter_visualization_shells.py finding to DECLINE
on ring_params' scope declaration. Both cannot hold; the scope rule wins and
23 inherit. (b) Raw scanner output reads 782 findings / Tier 3 61: the +1 is
the scanner scanning itself and finding its own new CITATION_LOOKBACK_BLOCK
constant (score 6). Real population conserved exactly -- the self-referential
quirk already carried as a provenance-discipline field note. DESIGN DEPARTURE
surfaced by measurement and needing Tony's confirmation: the prompt's
no-fallback invariant and its Jupiter case are in genuine tension, because the
line-959 finding sits in an UNCITED nested entry (ring_params['thebe_gossamer'])
and only the enclosing assignment carries the citation -- so inheriting it
requires exactly the outward fallback the invariant forbids. Both readings
implemented and measured; they produce BYTE-IDENTICAL audits at HEAD, because
SHELL_CONFIGS and CUSTOM_SHELLS are themselves uncited at assignment level and
there is no outer citation to fall back to. Built the strict version
(narrowest containing block, cited or not, stop there) so the invariant holds
by rule rather than by accident of the data: if anyone adds a # Source: above
SHELL_CONFIGS = { the 18 L-173 findings stay visible instead of silently
clearing. Cost: strict containment never reaches ring_params' scope
declaration, so flagging was decoupled from resolution -- scope-declared
blocks are collected during table construction regardless of whether any
string reaches them and get their own audit section (SCOPE-LIMITED CITATIONS),
pinned by test_scope_declared_block_is_flagged_even_when_unreached. Tony-action
(decide): confirm strict containment, or revert to narrowest-cited-containing
(one line in resolve_block_citation). SECOND judgment call deliberately not
made: ring_params' scope note disclaims COLORS, but the claims now being
suppressed are GEOMETRY (129,000 / 226,000 / 8,600 km), which the citation
explicitly covers. Built the blunt rule as specified; Tony-action (decide)
whether to open a follow-on for scope-aware inheritance before L-173's Gemini
worksheet is drafted. Regression: test_constants_provenance.py 73/73 unchanged;
test_reset_completeness.py fails identically on baseline and patched (missing
astroquery in sandbox, not a regression); no external consumers of the changed
functions. Gap item (6): BUILT, awaiting Tony's run + push. Also found:
safe-file-editing reads 1.1 in both repo and installed copies while the
protocol's Skill Manifest table still says 1.0 -- same class as L-152, one row
down; Tony-action (do) regenerate via skills_index.py.

Add to Ref: patch_phase1c_citation_inheritance.py; test_citation_inheritance.py;
documentation/AS_BUILT_L156_phase1c.md; documentation/BUILD_phase_1c_prompt.md.
```

---

## Block 2 -- append inside L-173

```
Note (2026-07-30): 1c built and measured; these 18 findings verified UNTOUCHED
by it. Independently re-derived from the post-patch audit and matching the
predesign table exactly: SHELL_CONFIGS['Pluto'] 10, ['Venus'] 3, ['Eris'] 2,
['Mars'] 2, CUSTOM_SHELLS['Mercury'] 1. All still Tier 1 / V4 RECALLED. 1c's
strict-containment resolver stops at the narrowest containing block and never
searches outward, so these cannot be cleared by a scoring change -- they need
real sourcing. test_citation_inheritance.py carries
test_live_shell_configs_uncited_blocks_still_uncited as a deliberate tripwire:
it fails if any of these five blocks starts inheriting a citation. When L-173
is genuinely resolved that test is EXPECTED to be updated by hand, not
silenced -- the failure is the signal that these blocks changed state.
```

---

## Rollup -- Tony-action

- **(do)** Paste Block 1 into L-156, Block 2 into L-173.
- **(do)** Run `ledger_index.py` to regenerate the index zone.
- **(do)** Regenerate the Skill Manifest via `skills_index.py`
  (`safe-file-editing` 1.0 -> 1.1).
- **(decide)** Strict containment vs narrowest-cited-containing.
- **(decide)** Blunt scope rule vs a scope-aware follow-on item.
- **(do)** After push, add `pushed at <SHA>` to the as-built.

Neither block sets `status:DONE`, so nothing auto-archives to section C.

---

*Ledger note written July 2026 with Anthropic's Claude Opus 5.*
