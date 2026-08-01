# AS-BUILT -- Phase 1d / 1e / 1f (L-156)

Built on `e29841f88fcc4b0f4d02681df1e0ec06b13a08c6`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Gallery repo untouched, pinned for the record:
`bf40b1a69051b2b6f87e72c0850a353654362d66`

**Type:** BUILD. Two deliverables, neither committed -- awaiting Tony.

**Companion:** `PREDESIGN_HANDOFF_phase1_d_e_f_R1.md` (built on `4b6b5c12`);
`REVIEW_predesign_1d_1e_1f.md`; `AS_BUILT_L156_phase1c.md`.

**Reading order:** section 2 is the headline number and needs a decision.
Section 3 is a deliberate divergence from the predesign. Everything else
is routine.

---

## 1. Anchor

Prompt anchor and live HEAD both `e29841f8` -- matched at session start,
no drift. The two commits since the review (`4b6b5c12` -> `e29841f8`)
added five documentation files and no code, so everything verified during
the review still held.

Base-file guards, verified before any edit:

| file | MD5 |
|---|---|
| `provenance_scanner.py` | `004d179fe93c200db4534cf1b0a7f038` |
| `comet_visualization_shells.py` | `58929e7fc7137f6264d950031a6bf6a7` |

---

## 2. Measured outcome -- and the decision it needs

Clean clone, patch applied, full scan:

| | before | after | delta |
|---|---:|---:|---:|
| Tier 1 | 132 | **171** | **+39** |
| Tier 2 | 588 | 645 | +57 |
| Tier 3 | 61 | 62 | +1 |
| Tier 4 | 2 | 2 | 0 |
| Total | 783 | 880 | +97 |

**Tier 1 went up by 39.** Every other step in Phase 1 brought it down.
The predesign predicted no number for this build, so there is nothing to
compare against -- which is exactly why it needs saying plainly rather
than being reported as a delta and left.

I isolated each piece rather than attribute one diff to three causes:

| change measured alone | Tier 1 | total |
|---|---:|---:|
| baseline | 132 | 783 |
| **piece 2 only** (citation forms) | **119** (-13) | 783 (conserved) |
| **piece 3 only** (F/C units) | **193** (+61) | 879 (+96) |
| both, as shipped | 171 | 880 |

So piece 2 behaves exactly as designed: 13 findings move Tier 1 -> Tier 2,
population conserved, close to the ~15 ceiling I measured during the
review. Piece 3 is the whole story.

**Piece 3 is the largest tier-moving change in Phase 1, larger than 1b.**
The predesign calls it "small, bounded, no design question." Measured, it
is none of those. It adds 96 findings, 61 of them Tier 1, and they land
almost entirely in four modules:

| module | total findings before -> after |
|---|---|
| `paleoclimate_wet_bulb_full.py` | 16 -> 51 |
| `paleoclimate_human_origins_full.py` | 11 -> 32 |
| `paleoclimate_visualization_full.py` | 7 -> 28 |
| `paleoclimate_dual_scale.py` | 2 -> 9 |

The regex is not over-matching -- I checked that specifically. Plain
`degrees` and `deg` still resolve as angles, bare `98.6 F` and `21 C` are
deliberately not matched (a bare trailing C or F would false-positive on
everything from spectral types to variable names), and the temperature
forms only fire on an explicit `degC` / `degF` / `degrees C` / `deg C` /
`degrees Celsius` shape. These are real temperature claims in
public-facing climate narrative that the scanner has been blind to since
it was written. L-078(d) asked for exactly this.

**Tony-action (decide).** Three ways to take it:

1. **Ship as built.** The claims are real and uncited. A climate
   visualization project whose provenance scanner cannot see temperature
   values is the wrong instrument, and "Data Preservation is Climate
   Action" is the reason this matters more here than it would elsewhere.
2. **Ship, and track the new population separately** the way L-173 tracks
   the `shell_configs.py` gaps -- so Tier 1 reads as "132 known + 61
   newly visible" rather than as a regression.
3. **Defer piece 3** to its own sub-step with a sourcing plan attached.

My recommendation is 1 plus 2: ship it, and open a ledger item for the
newly-visible temperature claims. Deferring buys a smaller number by
keeping the scanner deliberately blind, which is the one option that
makes the audit less true than it is now.

Note also that these modules carry human-cost content -- heat deaths,
food insecurity -- where the earth-system-pipeline skill's restraint
discipline applies. That is an argument for sourcing them properly, not
for leaving them unseen.

---

## 3. Divergence: 1d piece 1 is a detector, not an Option A amendment

The predesign, corrected in R1, asks for piece 1 as an amendment to
`score_unit()`'s Option A block. I did not build it that way. Flagging
rather than resolving, per the build prompt.

**Three measured reasons.**

**Option A cannot see the problem.** It inspects `unit.kind == 'string'`
only. All three confirmed shadow constants are numeric assignments, and
they are function-local -- `extract_units_from_file` walks
`ast.iter_child_nodes` for constants, so it reads TOP-LEVEL assignments
only. The scanner produces no unit at all for lines 492, 493 or 602.
There is no score to amend. Verified directly: extracting units from
`comet_visualization_shells.py` returns nothing at those lines.

**Amending Option A would push findings the wrong way.** Option A
currently fires on 18 display strings, granting them V_SOURCED. Of those,
9 sit in modules that import nothing from `constants_new.py` or the shim.
Requiring an import would demote those 9 to V_RECALLED -- raising their
vulnerability and moving them toward Tier 1, on a build already carrying
piece 3's increase, and for strings that have nothing to do with the
shadow-constant problem.

**Value-only matching is not a usable signal.** Measured repo-wide:

| discriminator | hits |
|---|---:|
| value matches a pinned constant | **77** |
| **name AND value both match** | **2** (exactly the confirmed instances) |

The 77 are dominated by coincidental round numbers -- `0.5`, `2.2`,
`10.0`, `3.0` -- that happen to equal some pinned value. The scanner's
own docstring already warns about this failure mode for Option A
("rarely fires in practice... breaks on coincidental numbers"). A
detector at that noise level gets ignored, which is worse than no
detector.

**So:** a dedicated `scan_shadow_constants()` walking every assignment at
any depth, matching name AND value, reported as a diagnostic. Option A's
scoring is untouched. Whether to retire Option A properly per D8.5
remains open and is not made worse by this.

---

## 4. Fire-then-silence -- the test the sequencing existed for

Built in two stages, precisely so the detector could be proven against
real code before 1f removed the evidence:

| stage | console |
|---|---|
| 1d only | `3 shadow constant(s) -- local copies of cited constants_new.py values` |
| | reported: `SUN_RADIUS_KM` 492 direct, `KM_PER_AU` 493 direct, `SUN_RADIUS_AU` 602 derived |
| + 1f | line absent; audit section empty |

Detector fires on all three, fix lands, detector goes quiet. That is a
stronger result than any synthetic fixture, and it is the whole reason
the review recommended reversing the predesign's original order.

---

## 5. What each piece does

**1d piece 1 -- shadow constants.** `build_cited_constant_names()` maps
NAME -> value for cited constants. `scan_shadow_constants()` walks all
assignments at any depth and flags two shapes: `direct` (name and value
both match) and `derived` (an expression whose literals are all pinned,
with a magnitude floor). Diagnostic only; no scoring effect. New audit
section, new console line.

**1d piece 2 -- author-year citations.** One pattern added to
`SOURCE_PATTERNS`, recognising both live forms. A match requires either a
multi-author marker (`et al.` / `& Author` / `and Author`) or a
four-digit year after a capitalised surname, with month names excluded.
The month exclusion is not hypothetical: my first draft matched
`(May 2026)` on the first file in the repo.

**1d piece 3 -- temperature units.** Temperature alternatives added to
`NUMERIC_CLAIM_RE`, placed BEFORE the generic degree alternatives.
Ordering is load-bearing: Python alternation is first-match-wins, and
without it `35 degrees C` keeps matching as 35 angular degrees. The
degree sign is written `\xb0` to keep the source ASCII.

**1e piece 1 -- Tier-1 banner.** Bordered, printed when Tier-1 findings
exist, informational only. The exit code is untouched, per design review
3c, and the code carries a comment saying so and naming the superseded
document, so a future session does not revive the deferred flip from
`HANDOFF_phase1_1d_to_1f.md`.

**1e piece 2 -- tier labels.** Tiers 2, 3 and 4 now carry neutral
score-band names (`REVIEW`, `LOW PRIORITY`, `LOWEST PRIORITY`).

**1f -- shadow constants deleted.** Imports `SUN_RADIUS_KM` and
`SOLAR_RADIUS_AU` through the shim. Verified at runtime that the imported
values equal both `constants_new.py`'s and the deleted literals, so the
change is value-preserving. `SUN_RADIUS_AU` is kept as a local alias of
`SOLAR_RADIUS_AU` so the downstream uses at 608-609 need no edit; it
tracks the import rather than freezing a value.

---

## 6. Decisions and observations for Tony

**(decide) Tier 1 keeps "FIX NOW".** The decided text says tiers get
"neutral score-band names only," but the failure it names is the Tier-2
blanket residual claim. "FIX NOW" is an action directive, not an
assertion about the findings' status, and it is referenced elsewhere in
the report. I neutralised 2, 3 and 4 and left 1. One line to change if
you want all four.

**(note) `comet_visualization_shells.py` already violates ASCII-only.**
Three em-dashes, 9 bytes, at offsets ~13951 (inside a user-facing display
string) and ~24506 (in a comment). Pre-existing, not introduced here. My
patch's ASCII gate originally failed on this and I corrected the gate,
not the file: it now asserts the patch introduces no NEW non-ASCII and
reports the pre-existing count. Fixing the em-dashes changes a display
string, which is your call, not a build-time cleanup.

**(note) `build_pinned_values()` has a citation-bleed flaw.** It uses a
flat window of 10 lines above and 5 below, so in a densely packed file a
constant with no citation of its own picks up a neighbour's. My new
`build_cited_constant_names()` avoids it by reading only the contiguous
comment run touching the assignment. I did not change
`build_pinned_values()` itself -- that would shift the pinned set and
therefore Option A's behaviour, which is out of scope here. Worth an item
if Option A is kept.

**(note) my own negative test caught a real bug mid-build.** The first
implementation of `build_cited_constant_names()` walked upward only, and
`test_uncited_constant_is_not_a_shadow_source` failed -- which exposed
that `constants_new.py` writes citations BELOW the assignment, not above.
The final version accepts both, as a contiguous comment run touching the
assignment in either direction. Recording it because the failure was the
useful part: the test was written to catch a false positive and instead
found a false negative in the opposite direction.

---

## 7. Verification performed

| check | result |
|---|---|
| SHA round trip | prompt anchor == live HEAD, `e29841f8` |
| Base-file MD5s, both targets | match |
| `py_compile`, deliverables | pass |
| `py_compile`, patched targets | pass |
| ASCII gate, deliverables | clean |
| ASCII gate, patched results | no new non-ASCII; 9 pre-existing reported |
| LF gate | no CRLF anywhere |
| Patch apply, clean clone | 16/16 anchors, one match each, 2 files |
| Idempotency | refuses, nothing written, cause named per file |
| Fire-then-silence | 3 detected at stage 1, 0 after 1f |
| 1f runtime import | values equal `constants_new.py` AND the deleted literals |
| `test_provenance_1d.py` | **15/15** |
| `test_citation_inheritance.py` | 20/20 unchanged |
| `test_constants_provenance.py` | 73/73 unchanged |
| Per-piece isolation | measured separately, section 2 |
| Regex negative cases | 13 non-citations asserted rejected |

Agentic pre-test: `provenance_scanner.py` is a devtool with no Tk
surface, so the xvfb leg does not apply. The runtime-equivalent leg was a
live scan on the real repo plus all three suites, on throwaway clones.
The deliverables were never edited by any test.

---

## 8. Rollup -- Tony-action

- **(do)** Run `patch_phase1_d_e_f.py` via VS Code's Run button. Expect
  16 `ok` lines across 2 files, plus a note about the pre-existing
  non-ASCII bytes.
- **(do)** Run `test_provenance_1d.py` (15), `test_citation_inheritance.py`
  (20), `test_constants_provenance.py` (73).
- **(do)** Run `provenance_scanner.py .`. Expect Tier 1 171, Tier 2 645,
  the new banner, neutral tier names, and an EMPTY shadow-constant
  section.
- **(decide)** Section 2 -- how to treat piece 3's +61 Tier-1 findings.
- **(decide)** Section 6 -- whether Tier 1 keeps "FIX NOW".
- **(decide)** Whether to fix the three em-dashes in
  `comet_visualization_shells.py`.
- **(do)** Correct or supersede `HANDOFF_phase1_1d_to_1f.md` -- still
  wrong on 1e at HEAD.
- **(do)** Stamp the provenance-discipline v1.3 SHA placeholder.
- **(do)** Paste the L-156 note, run `ledger_index.py`, push, record
  `pushed at <SHA>`.

---

## 9. What this build did not touch

L-173's 18 findings, L-155, L-160, L-157, L-161, L-159, the D4 backfill,
and the repo-wide shadow-constant sweep are all out of scope and
untouched. Option A's scoring is unchanged, so D8.5's retirement question
is still open. `build_pinned_values()` is unchanged.

One in-scope item confirmed complete: the 1f grep for other shadow
constants in `comet_visualization_shells.py` found none beyond the three
fixed. The repo-wide detector now covers the rest permanently.

---

*As-built written July 2026 with Anthropic's Claude Opus 5.*
