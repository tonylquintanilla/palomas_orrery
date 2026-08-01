# Build Prompt — L-156 Phase 2 Piece 1: Cross-Checked Annotation Scanner

**Built on `d03f586196bc07e8c4cb6f8435e16ac85de194b9`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify fresh — this is stated, not assumed.**

---

## Your role

You are Claude Opus 5, building Phase 2 Piece 1 of the L-156 provenance
scanner rebuild. You implement, you don't redesign. The predesign has
been through two rounds of competitive review (GPT, Opus 5 ×2, Fable 5)
and Tony's decisions are final. If something looks wrong, flag it —
don't silently change the design.

Tony Quintanilla is the integrator. He has sole commit authority. He
runs Python via VS Code's Run button, not the terminal. He works
exclusively through GitHub Desktop — never CLI git.

---

## What you're building

Teach `provenance_scanner.py` to recognize `# Cross-checked:`
annotations and score them V_CROSS_CHECKED (V2). This activates a
rung that exists in the code but currently has zero population.

The annotation form:

```python
# Source: NASA Planetary Fact Sheet
# Cross-checked: Gemini 2026-04-15 (worksheet_earth_visualization.md)
# Cross-checked: Claude 2026-08-10 (worksheet_earth_visualization.md)
```

**V2 requires ALL of:**
- Source evidence (direct `# Source:` citation OR inherited citation
  from an enclosing block)
- Two valid `# Cross-checked:` annotations with distinct checker
  identities
- Each annotation must have an ISO date (YYYY, YYYY-MM, or
  YYYY-MM-DD) and a parenthetical reference ending in `.md`

---

## Deliverables

### 1. `parse_cross_checks(text)` function

**Returns:** `(records, issues)` tuple.

- `records`: list of `(checker_identity, date, reference)` for each
  valid annotation line.
- `issues`: list of `(raw_line, error_code)` for malformed annotations
  the parser rejected.

Error codes: `missing_reference`, `missing_year`,
`non_markdown_reference`, or others as appropriate.

**Regex:** must use `re.MULTILINE` and anchor to line start with
required colon:

```python
r'(?mi)^\s*#\s*cross-checked\s*:'
```

**Why the colon matters:** `planet_visualization_utilities.py` already
contains "Giants cross-checked to Voyager 2 (Uranus: Desch..." around
line 456. Without the colon anchor, that's a false positive today.

**Date:** ISO only. Must start with a four-digit year. Prose dates
like "April 2026" are NOT valid — they create identity/date parsing
ambiguity.

**Reference:** non-empty parenthetical ending in `.md`. Rejects `(x)`,
`(done)`, `()`.

**Checker identity:** everything between the colon and the ISO date,
trimmed and normalized. Two annotations are "distinct" if their
identities differ after case-folding and whitespace normalization.

**Known limitation to document, not solve:** "Gemini" vs "Gemini Pro"
count as distinct. The competitive pattern is human-mediated; the
scanner checks string identity, not model family.

**Placement:** immediately after `has_citation()` in the source.

### 2. Scoring change in `score_unit()`

Insert BEFORE the existing `if cited` branch:

```python
records, issues = parse_cross_checks(text)
distinct_checkers = len({r[0].lower().strip() for r in records}) >= 2
sourced = cited or bool(unit.inherited_citation)

if sourced and distinct_checkers:
    unit.vuln = V_CROSS_CHECKED
    unit.vuln_reason = "Cross-checked by N models (identities)"
elif sourced and records:
    unit.vuln = V_SOURCED
    unit.vuln_reason = "Cited; cross-check incomplete (N/2 models)"
```

The `elif sourced and records` case falls through to V_SOURCED with
a distinct reason — one leg done, visible in the audit. The remaining
branches (`elif cited`, `elif inherited`, `elif stale`, `else`) are
unchanged.

**Stale interaction:** fully qualified cross-check + stale marker →
V_CROSS_CHECKED, reason notes "date-sensitive."

### 3. V_CROSS_CHECKED comment update

Current text (lines 318-326):

```python
V_CROSS_CHECKED = 2   # Independently cross-checked against dated evidence,
                      # blind (the checker was not shown our value). NEVER
                      # auto-promotable to V_FETCHED at any rigor level --
                      # the scanner can observe that a check is claimed, not
                      # that it was rigorous.
                      # NOTHING SETS THIS YET. Population arrives with the
                      # `# Cross-checked:` annotation recognition in D4;
                      # until then this rung is intentionally empty rather
                      # than dead code.
```

Replace with:

```python
V_CROSS_CHECKED = 2   # Independently verified via competitive pattern:
                      # same worksheet to multiple models, independent
                      # research, integrator compares. Requires source
                      # evidence AND two distinct checker annotations.
                      # NEVER auto-promotable to V_FETCHED at any rigor
                      # level -- the scanner can observe that a check is
                      # claimed, not that it was rigorous.
                      # See provenance-discipline skill v1.4 for the
                      # annotation form and competitive-pattern definition.
```

**CRITICAL: do NOT put a worked annotation example here.** The scanner
scans itself. A complete `# Cross-checked: Model YYYY-MM-DD (file.md)`
example in this comment block would grant the ladder constants V2 on
themselves.

### 4. Diagnostics

Add a diagnostic subsection to the report for:
- Cross-check annotation on an unsourced unit
- Two annotations with the same checker identity
- Annotation reference doesn't end in `.md`
- Any parse issues from the `issues` list

Same pattern as existing shadow-constant diagnostics. This requires
collecting issue records during scanning, passing them to
`generate_report()`, and rendering a new subsection.

### 5. `test_cross_checked.py`

**Keep ALL example strings inside function bodies.** No module-level
constants, dicts, or string tables. The scanner scans test files.

16 tests (see predesign §2g for full descriptions):

1. Full V2: sourced + two distinct checks → V_CROSS_CHECKED
2. V2 with inherited citation → V_CROSS_CHECKED
3. V2 requires source: two checks, no source → V_RECALLED
4. Single checker (incomplete) → V_SOURCED with reason
5. Same identity twice → V_SOURCED
6. Missing reference → no valid record
7. Empty/trivial reference → not valid
8. Normal citation → no cross-check records
9. Voyager false positive (exact text from ~line 456) → no record
10. Case insensitivity
11. ISO date required (prose date rejected)
12. Staleness interaction
13. Population conservation by identity diff
14. Lookback bleed (adjacent findings, only one annotated)
15. Self-scan regression (identity diff, explain any delta)
16. Parse issues (error codes for malformed annotations)

---

## What NOT to do

- Do NOT add `Cross-checked` to `SOURCE_PATTERNS`. A malformed
  annotation earns nothing — this is correct.
- Do NOT redesign the scoring logic. The `sourced AND distinct_checkers`
  rule is decided after five reviews.
- Do NOT touch any source files with actual `# Cross-checked:`
  annotations. That's Piece 2, after Tony's worksheet review.
- Do NOT return a complete file from a stale base. Verify HEAD, pull
  fresh, apply targeted changes.

---

## Skills to load

Before writing any code:
- `provenance-discipline` (v1.4 in the repo)
- `safe-file-editing`
- `agentic-pre-test` (before delivering any complete file)

---

## Acceptance criteria

1. All 16 tests pass.
2. Full scanner run reproduces the baseline identity set (any delta
   explained — the new test file adding one scanned file is expected).
3. `py_compile` clean on both modified/new files.
4. No `# Cross-checked:` annotations exist in any source file yet.
5. The V_CROSS_CHECKED constant comment matches the decided wording.
6. The Voyager false positive does not match.
7. ASCII only, LF line endings.

---

## Reference documents in the repo

Read from live HEAD before writing code:

- `provenance_scanner.py` — the file you're modifying
- `test_provenance_1d.py` — precedent for test structure
- `test_citation_inheritance.py` — precedent for test structure
- `skills/provenance-discipline/SKILL.md` — v1.4, the annotation
  definition and competitive-pattern description
- `planet_visualization_utilities.py` ~line 456 — the live false
  positive text for test 9

The full predesign (R2) is attached. It contains the complete design
rationale, the review history, and the backfill plan that follows
this build.

---

*Build prompt prepared August 1, 2026 by Claude Opus 4.6
(orchestration).*
