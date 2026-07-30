# AS-BUILT -- Phase 1c, citation-block inheritance (L-156 Gap item 6)

Built on `cf061d7336cfed20a991218deec8b666e08d31b7`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Gallery repo unchanged this session, pinned for the record:
`cffb1caae03fd853adeafb4763e38530f639a7ab`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

**Type:** BUILD (two files delivered; neither committed -- awaiting Tony)

**Companion:** `PREDESIGN_1c_citation_inheritance.md` (built on `657542f`);
`documentation/BUILD_phase_1c_prompt.md`; ledger L-156 Gap item 6, L-173.

**Supersedes:** the predesign's Section 3 dict-split table (22/1) and its
predicted Tier-1 figure (~132). Both corrected below against measurement.
Everything else in the predesign held.

---

## 1. Session-start reconciliation

Repo HEAD moved mid-session. Traced before building rather than picked:

| | SHA | note |
|---|---|---|
| prompt anchor | `23635820b155103d01e4fe65b6c4b63901c0213b` | matched live HEAD at session start |
| live HEAD (after Tony's push) | `cf061d7336cfed20a991218deec8b666e08d31b7` | build anchored here |

`git diff 2363582 cf061d73` = one file changed, 24 insertions:
`documentation/BUILD_phase_1c_prompt.md` (the prompt itself). The build
target is untouched across the move -- `provenance_scanner.py` is
`94891f347cfe1b46bf14020468571993` at BOTH SHAs, so the prompt's
`EXPECTED_MD5` guard remains valid at the new HEAD. No rebuild needed.

The uploaded predesign is byte-identical to the repo copy
(`5584eed38bd8e9cde303b4cd7148495d`), so upload and repo agree and the
tier-1/tier-2 context-priority question does not arise.

**Skill version drift, minor:** the resident protocol's Skill Manifest
table lists `safe-file-editing` at 1.0. The repo skill and the installed
skill both read 1.1, and the build prompt itself says v1.1. Repo and
installed agree, so 1.1 is correct and the manifest table is stale --
same class as the L-152 near-miss, one row further down. Regenerating via
`skills_index.py` should clear it. **Tony-action (do).**

---

## 2. What was built

Two files. Neither is committed.

**`patch_phase1c_citation_inheritance.py`** -- anchored transactional
patch, 12 edits, same shape as 1a/1b:

- `EXPECTED_MD5` base-file guard, checked before any anchor is examined
- every anchor verified to match exactly once BEFORE any write
- bottom-up edit ordering; byte-level anchored replaces, binary mode
- ASCII and LF gates run on the patched RESULT, not just the input
- all-or-nothing: any failure writes nothing at all
- one `ok` line per edit, then `patch applied (N bytes)`
- run command stated in the module docstring; VS Code Run button framing
- re-running refuses cleanly and says WHY -- distinguishing
  already-applied (looks for `CITATION_LOOKBACK_BLOCK`) from Windows
  CRLF from genuine drift, rather than printing a bare hash mismatch

**`test_citation_inheritance.py`** -- 16 regression tests in
`test_constants_provenance.py`'s conventions (plain asserts, no pytest,
`main()` with pass/fail summary, exit 0 / non-zero). Mechanism tests use
synthetic source fixtures so they do not break when `shell_configs.py` is
edited; four live-repo tests assert relationships rather than hardcoded
line numbers.

### The mechanism, as delivered

Named constant `CITATION_LOOKBACK_BLOCK = 15`, justified in a comment
(8 covers `shell_configs.py`; 15 reaches `ring_params` with margin),
applied above both the block key and the enclosing assignment.

`build_citation_block_table()` -- one `ast.walk` pass over every
`ast.Assign` at any nesting depth. Records two block shapes: the whole
dict assignment (cited above its first line) and each dict-valued entry
(cited above its key line). Function-local dicts are reached; a
module-level-only walk would miss `ring_params` entirely.

`citation_run_above()` -- captures the whole contiguous comment run, not
the matched line. Necessary: for the Moon block `has_citation` matches a
continuation line, and recording only that line would drop Weber (2011)
above it and Draper (1847) below. Stops at the first non-comment,
non-blank line so a previous block's citation is never stolen.

`resolve_block_citation()` -- takes the narrowest block containing the
string and STOPS THERE. See section 4; this is the one place the build
departs from a literal reading of the prompt.

Blocks are keyed by line range, never by name, so cross-dict inheritance
is structurally impossible rather than merely avoided.

Inheriting strings score `V_SOURCED` with reason
`"Cited via enclosing block citation"`. No new rung; 1b's ladder
unchanged.

---

## 3. Measured outcome

Verified end-to-end from a clean clone at `cf061d73`: apply, test, scan.

| | at HEAD | predicted | measured | |
|---|---:|---:|---:|---|
| Tier 1 | 156 | ~132 | **133** | see 3a |
| Tier 2 | 563 | ~587 | **586** | see 3a |
| Tier 3 | 60 | 60 | **60** | +1 artifact, see 3b |
| Tier 4 | 2 | 2 | **2** | |
| Total | 781 | 781 | **781** | +1 artifact, see 3b |

Invariants asserted directly, all holding:

- 23 findings moved out of Tier 1; Tier 2 gained exactly 23
- nothing entered Tier 1, from any file
- Tier 3 and Tier 4 unmoved on the real population
- all movement confined to `shell_configs.py`

**The 21/2 split is confirmed independently.** Re-derived from the audit
rather than from the predesign's table: 21 from `SHELL_CONFIGS` (Earth 8,
Jupiter 6, Moon 4, Mercury 2, Planet 9 1) and 2 from `CUSTOM_SHELLS`
(Jupiter 1, Saturn 1). The prompt's correction stands; the predesign's
own 22/1 table is wrong.

**The 18 that stay match the L-173 table exactly** -- Pluto 10, Venus 3,
Eris 2, Mars 2, `CUSTOM_SHELLS['Mercury']` 1. Untouched, still Tier 1,
still V4. 1c left them exactly where it found them, as scoped.

### 3a. Why 133 and not ~132

The predesign is internally inconsistent, and the build is correct.

Its headline counts 24 inheriting findings -- 23 in `shell_configs.py`
plus 1 in `jupiter_visualization_shells.py` -- and `156 - 24 = 132`. But
its own Section 7 edge case requires that the Jupiter one DECLINE,
because `ring_params`' citation carries an explicit scope declaration.
Both cannot hold. The scope rule wins, 23 inherit, and Tier 1 lands at
133.

Recorded as a correction to the prediction, not a deviation in the build.

### 3b. Why the raw totals read 782 and 61

The scanner scans itself. The extra finding is the new
`CITATION_LOOKBACK_BLOCK = 15` constant in `provenance_scanner.py`,
scoring 6 (Tier 3). This is the self-referential quirk already noted as a
field note in the provenance-discipline skill.

On the real population -- everything the scanner is actually auditing --
781 is conserved exactly and Tier 3 stays at 60.

Anyone re-running this and reading 782/61 should check whether the delta
is this file measuring its own diff before chasing it further.

---

## 4. The one design departure, and why

The prompt's no-fallback invariant and its Jupiter case are in genuine
tension. This surfaced only under measurement.

The line-959 finding sits inside `ring_params['thebe_gossamer']`, which
is UNCITED. Only the enclosing `ring_params` assignment carries the
citation. So making that finding inherit requires an uncited block
resolving outward to an enclosing citation -- precisely what the prompt
identifies as "the bug this whole predesign exists to prevent."

Both readings were implemented and measured. **They produce
byte-identical audits at HEAD.** The reason is that `SHELL_CONFIGS` and
`CUSTOM_SHELLS` are themselves uncited at assignment level, so there is
no outer citation available for anything to fall back TO. The invariant
currently holds partly by accident of the data.

**Built: strict containment.** Narrowest containing block, cited or not,
stop there. Same numbers today, but the invariant holds by rule rather
than by luck. If anyone adds a `# Source:` above `SHELL_CONFIGS = {`
tomorrow, the 18 L-173 findings stay visible instead of silently
clearing -- which is exactly the failure the predesign was written to
prevent, and it would have been invisible in the audit totals.

Cost: under strict containment the resolver never reaches `ring_params`'
scope declaration, because it stops at the uncited inner block first. So
flagging was DECOUPLED from resolution -- scope-declared blocks are
collected during table construction regardless of whether any string
reaches them, and get their own audit section. `ring_params` appears
there correctly. `test_scope_declared_block_is_flagged_even_when_unreached`
pins this.

**Tony-action (decide):** confirm strict containment, or say the word and
it reverts to narrowest-cited-containing (a one-line change in
`resolve_block_citation`).

---

## 5. A judgment call deliberately not made

The `ring_params` scope declaration disclaims COLORS: "Colors below are
selected by the developer for visual distinction, not verified against
the cited source." The claims it is now suppressing are GEOMETRY --
129,000 km inner, 226,000 km outer, 8,600 km vertical extension -- which
the citation explicitly DOES cover ("ring geometry only (inner/outer
radius, thickness)").

So the blunt "scope marker present, decline wholesale" rule specified in
the prompt is declining a claim the author did source. It was built as
specified. But it is one finding, and worth a look before L-173's Gemini
worksheet is drafted, since the alternative is a finer rule that reads
what the scope actually excludes.

**Tony-action (decide):** leave the blunt rule, or open a follow-on item
for scope-aware inheritance.

---

## 6. Verification performed

| check | result |
|---|---|
| Base MD5 at both SHAs | `94891f34...` -- guard valid |
| Uploaded predesign vs repo copy | byte-identical |
| `py_compile` -- both deliverables | pass |
| `py_compile` -- patched target | pass |
| ASCII gate (deliverables + result) | clean |
| LF gate (deliverables + result) | no CRLF |
| Patch apply, clean clone | 12/12 anchors, one match each |
| Idempotency (re-run) | refuses, nothing written, cause named |
| `test_citation_inheritance.py` | 16/16 pass |
| `test_constants_provenance.py` | 73/73 pass (unchanged) |
| `test_reset_completeness.py` | fails identically on baseline AND patched -- missing `astroquery` in sandbox, not a regression |
| External consumers of changed functions | none (`plot_data_report_widget.py`'s `generate_report` is an unrelated class method) |
| Scanner live run, clean clone | 133 / 586 / 61 / 2 |

The xvfb GUI leg of the agentic pre-test does not apply here:
`provenance_scanner.py` is a devtool with no Tk surface. The
runtime-equivalent leg -- a live scan on the real repo plus the
regression suites -- was run instead, on a throwaway clone. The
deliverables themselves were never edited by any test.

---

## 7. Rollup -- Tony-action items

- **(do)** Save `patch_phase1c_citation_inheritance.py` into the
  `palomas_orrery` folder, open in VS Code, click Run. Expect 12 `ok`
  lines then `patch applied`.
- **(do)** Save `test_citation_inheritance.py` into the same folder and
  Run it. Expect 16 passed, 0 failed.
- **(do)** Run `provenance_scanner.py` to regenerate
  `PROVENANCE_AUDIT.md`. Expect Tier 1 133, Tier 2 586. Note the scanner
  will read 782/61 total while the patch script is still sitting in the
  folder plus its own new constant -- see 3b.
- **(do)** Regenerate the Skill Manifest via `skills_index.py`;
  `safe-file-editing` shows 1.0 in the protocol table but is 1.1 in both
  repo and installed copies.
- **(decide)** Strict containment vs narrowest-cited-containing (section 4).
- **(decide)** Blunt scope rule vs a follow-on for scope-aware
  inheritance (section 5).
- **(do)** Paste the L-156 note (delivered separately) and run
  `ledger_index.py`.
- **(do)** Commit and push; record `pushed at <SHA>` against this document.

---

## 8. What 1c did not touch

The 18 genuinely-uncited findings (L-173) are untouched, as scoped. They
need real sourcing via a Gemini worksheet, not a scoring change. Nothing
in this build resolves or routes around them, and
`test_live_shell_configs_uncited_blocks_still_uncited` will fail
deliberately if a future change starts clearing them -- which is the
intended tripwire, and is expected to be updated by hand when L-173 is
genuinely resolved.

`idealized_orbits.py` remains excluded on the structural basis the
predesign established: zero of its 24 Tier-1 findings fall inside any
cited block. Confirmed still true at this SHA -- the block table finds no
containing cited block for any of them.

---

*As-built written July 2026 with Anthropic's Claude Opus 5.*
