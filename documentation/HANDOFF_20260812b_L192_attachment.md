# Session Handoff -- August 12, 2026 (second session)

**Built on `c5218f6202965bc051044e59988e1a040a234fc9`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery unchanged at `d5437f08f94feccd70b697729b52cdc44df8b51d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs verified live at session close.**

**Type: BUILD + RECORD.** One scanner change, two files patched, one
Mode 7 relay. No orrery rendering code touched.

**Continues from** `documentation/HANDOFF_20260812_L186_L188.md`
(anchored `417f70f`).

**Advances:** L-192 -- its scanner half is built and pushed. The
worksheet checker it was opened for is NOT built.
**Opens:** nothing new.

**Prepared:** August 12, 2026 by Claude Opus 5, Tony Quintanilla
integrator, with Claude Fable 5 as review partner.

---

## The skill obligation from the previous handoff is DISCHARGED

`provenance-discipline` loaded at **2.0**, and the manifest row in
`PROJECT_INSTRUCTIONS.md` at HEAD also reads 2.0. Checked against the
repo rather than against the resident protocol copy, which was one
version behind (v3.38, row 1.9) and would have produced a false STOP.

Nothing carries forward. The next session performs its own load check
as usual; there is no deferred verification outstanding.

---

## What happened

| SHA | What |
|---|---|
| `878e2c9` | attachment rule in `provenance_scanner.py`; two tests updated; patch script |
| `c5218f6` | maintenance run outputs, including the regenerated audit |

Session-start reconciliation: HEAD was `417f70f`, which is the previous
handoff's `c5c7d26` plus the handoff file itself. Nothing to reconcile.

---

## The finding, and what it cost

**A cross-check annotation was granting credit to values it was not
written for.**

The scanner reads a window around each declaration -- 30 lines back and
15 forward for a constant -- and counted any annotation inside it. That
window is correct for a CITATION: a section header naming IAU Resolution
B3 legitimately covers the constants beneath it, and the block-citation
table exists for exactly that. It is wrong for an ANNOTATION, which
names one checker who verified one value on one date.

Two examples, both verified at `417f70f` before anything was built:

- `MERCURY_RADIUS_KM` and `VENUS_RADIUS_KM` carry a source line and no
  annotation of their own. Both scored the top rung, "cross-checked by
  3 models," on annotations belonging to `MOON_RADIUS_KM` three and six
  lines below.
- `INNER_LIMIT_OORT_CLOUD_AU` scored the top rung on annotations
  belonging to the heliopause constant above it. In the two worksheets
  those annotations name, the row for the Oort value reads
  **UNVERIFIED** in Claude's and **PARTIAL** in GPT's. The window was
  converting a recorded non-verification into a top-rung badge.

The second one is the argument. The first is only a provenance error;
the second is wrong-but-cited, which this project treats as worse than
uncited.

---

## The Mode 7 relay

Tony carried `FABLE_REVIEW_REQUEST_annotation_attachment.md` (anchored
`417f70f`) to Fable 5 and brought back a review response at the same
anchor. Fable fetched the repo directly and reproduced the mechanism
independently before ruling.

**Fable's ruling: the scanner narrows.** Credit comes from annotations
attached to the value's own comment block, and the worksheet checker
consumes the scanner's attachment rather than computing a second one --
two definitions of "which annotations belong to this value" would drift
apart by construction, which is the parallel-pipeline anti-pattern.

Fable also answered the group-annotation question explicitly: the
legitimate pattern exists in this codebase, a parser cannot distinguish
it from proximity because in bytes the two are identical, and the fix is
per-value annotations rather than new block grammar. Its reason is
strong and worth keeping: a block-scope annotation reading "everything
below checked" would have papered over the two UNVERIFIED Oort rows
sitting inside its scope. Writing per-value forces the author to look at
each row.

---

## THE CORRECTION -- a number was wrong twice before it was caught

**The measured split is 50 keep / 27 drop, not 43 / 34.**

Fable's written rule and Fable's measured number disagreed. The rule
says a display string anchors on the KEY LINE that introduces it. Its
measurement script anchored on the string literal one line below, which
in the shells modules is one line past the `'description': (` that the
comments were written for.

**The independent leg reproduced the error.** Claude implemented the
rule from Fable's written spec rather than running its script, got
43/34 matching row for row across all eight files, and reported that
agreement to Tony as strong confirmation. It was strong confirmation of
a shared mistake. Two implementations agreeing is only as good as the
spec they share, and the spec was not what either one implemented.

It was caught by re-reading the written rule while implementing the
production version -- not by any check, and not by the agreement.

Seven display strings in `pluto_visualization_shells.py` and
`venus_visualization_shells.py` have their annotations directly above
the key that introduces them. They attach. The production rule anchors
on the entry line, which is what Fable's prose said all along.

Audit movement on the day it landed: the cross-checked rung fell from
**77 to 50**. Nothing got worse; 50 was always the true number.

---

## What was built

**`provenance_scanner.py`** -- one new concept, four helpers:

- `statement_spans()` and `entry_anchor_map()`, built once per file
  while the AST is in hand, because attachment is a property of where a
  declaration SITS.
- `attached_comment_indices()` / `attached_block()`. A module-level unit
  takes the unbroken comment run directly above its statement plus the
  one directly below -- `constants_new.py` writes citations below,
  the shells modules write them above, and both are correct. A string
  nested in a dict or a function body takes only the run above the entry
  that introduces it.
- `collect_orphan_annotations()`. An annotation whose comment run
  touches no code at all is reported. The test is "touches code," not
  "attached to a scored unit": `CORE_AU` is a product of two names so it
  never becomes a unit, and its annotations are correctly placed
  regardless. A run fenced off by blank lines on both sides is the
  genuinely unattached case.
- `score_unit()` reads attached annotations for CREDIT. The wide window
  still feeds the malformation diagnostics, because a broken annotation
  anywhere nearby is worth reporting.

New audit section: **ORPHAN ANNOTATIONS**, diagnostic, no scoring
effect.

**`test_cross_checked.py`** -- two tests went red the moment the rule
changed, which is what they were for. `test_lookback_window_bleed_is_
measured` had pinned the bleed ON PURPOSE, with a note saying that if it
ever failed the window had changed. It is now
`test_lookback_window_bleed_is_closed` and asserts the opposite, keeping
both halves pinned near and far. The synthetic fixtures needed
`attached_text` set, since they build units by hand.

Verified before delivery on a throwaway copy: both files compile;
`test_cross_checked.py` 17/17, `test_constants_provenance.py` 18/18,
`test_citation_inheritance.py` and `test_provenance_1d.py` green.
Confirmed after the push by reading the audit at `c5218f6`.

---

## The orphan queue -- four lines, two headers

Both in `constants_new.py`, both section headers whose annotations were
written to cover a group:

| Lines | Header | Worksheets named |
|---|---|---|
| 145-146 | SOLAR STRUCTURE | `worksheet_gemini_constants_remaining.md`, `constants_new_citation_verification_gpt.md` |
| 316-317 | CENTER BODY RADII | `worksheet_claude_constants_new.md`, `constants_new_citation_verification_gpt.md` |

Nothing else floated loose across the whole corpus.

These are the head of the backfill, not a cleanup. Each names a
worksheet holding per-value verdict rows. **Backfill is verdict-gated:**
appearing in a worksheet is not a passing check. Venus reads YES/YES,
Mercury reads PARTIAL/YES, the Oort values read UNVERIFIED/PARTIAL. Only
rows whose verdict is a completed check earn an annotation; the rest
stay honestly at V3 with their state visible.

---

## (do) -- outstanding

Items 1-4 carry forward from the previous handoff unchanged; 5 and 6 are
new.

1. **Open the ledger handle for the claim class** -- claims about the
   project that no tooling checks. Fable's earlier audit found fourteen
   in fifteen documents, eleven mechanically checkable. Still not open.
   This session added a third piece of evidence: a written rule and its
   own reference implementation disagreeing, with nothing to catch it.

2. **Record the scheduled-build retirement in the ledger.** The
   deployment-model decision block still describes the scheduled nightly
   as the operating model. Note the pre-commit fail-safe as designed but
   not built.

3. **Note on the L-191 block:** manual-scale instructions are
   orrery-surface-only and must not be collapsed into shared text that
   reaches the transport. 32 live in `shell_configs.py`.

4. **Record the eighteen inline literals** duplicating cited constants:
   `KM_PER_AU` 14 sites in 8 files, `MOON_RADIUS_KM` 3 in 2,
   `SUN_RADIUS_KM` 2 in 1. Inline in f-strings, so the scanner sees one
   of nineteen.

5. **Archive `patch_L192_attachment.py` to `documentation/`.** It is
   spent and currently sits at the repo root, where the scanner reads
   it.

6. **The runner's delta gap now has a cost** (was do-item 6 last
   session, filed in L-188). `maintenance_run.py` prints a checker's
   full output only on failure, so the one run where the number moved
   from 77 to 50 is the run that hid it -- neither the new count nor the
   four orphans reached the screen. Small fix.

---

## (decide) -- still open

Unchanged from the previous handoff, plus two from Fable.

1. **Jupiter's ring entry count: 4 or 5.** The pilot is scoped by it.
   Settle it by reading the file's structure.

2. **Migration shape and per-body sequence beyond Jupiter** (L-181).

3. **Saturn `thickness_km`:** absent from the served cache, but is it
   absent from the ORRERY? One look settles it.

4. **Do the three `provenance_history.py` constants earn
   `provenance_exceptions.json` entries?** Configuration, not factual
   claims. Tier 3, low stakes.

5. **`LESSONS_ARCHIVE.md` line-count discrepancy** (824 vs 882).
   Unreconciled, low weight.

6. **Does a PARTIAL worksheet verdict count as a completed leg for
   backfill?** Fable's question. It belongs inside L-192's definition,
   not a new handle.

7. **Are `DEFAULT_MARKER_SIZE` and `CENTER_MARKER_SIZE` in cross-check
   scope at all?** They are visual choices, not measurements, and may
   belong in the Track 0 registry's declared zone.

(The previous handoff's item 2 -- where the L-188 push-gate binding
lands -- is closed by default; L-188 is closed.)

---

## Next session

**L-192's second half: the worksheet checker.** It now has an attachment
rule to consume, so it knows which value each annotation belongs to
without inventing a second definition. The four escalation conditions
are already in the ledger block.

Measured this session and worth carrying: 134 live annotations, all 134
parse under the L-186 grammar, 18 distinct worksheets named, **zero
dangling**. Of the 34 files in `documentation/worksheets/`, 18 are
cited, 9 are uncited worksheets, and 7 are prompt files. The previous
handoff's "nine uncited" reconciles once the prompts are set aside. The
existence half is clean today; the value half is the build.

**Then the backfill** of the 27 that dropped, verdict-gated, starting
with the four orphans.

---

## Process -- read this before your first substantive reply

The Register Rule is binding. **Check 0: does this message ask Tony for
ONE thing?**

It held this session. Tony asked for an executive summary once, and the
message that prompted it was not overloaded -- it was jargon-dense.
Plain language is the second half of the rule and is easy to miss while
satisfying the first half.

**The lesson worth carrying is the correction above.** Cross-AI
verification requires independent legs, and this session had one --
Claude implemented Fable's rule from its written spec rather than
running its script. It still reproduced the error, because both
implementations read the same prose and neither implemented what it
said. The agreement was reported to Tony as confirmation. It was not.

What caught it was re-reading the written rule against the code being
produced, at the moment of production. Nothing else would have.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`c5218f6202965bc051044e59988e1a040a234fc9` at
https://github.com/tonylquintanilla/palomas_orrery and
`d5437f08f94feccd70b697729b52cdc44df8b51d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
