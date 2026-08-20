# L-214 step 2 -- where the vocabulary lives

**Built on `3586970dd841d5b417f8e6f59de4d3e3d440d001` at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5.**

For the session building L-214. Its recommendation of (a) holds. What
follows is one correction to the premise, one confirmation, and one
scoping distinction that should be settled before code is written
rather than discovered during it.

---

## 1. Correction: nobody is compiling the vocabulary twice

L-214's build step 2 says "one home for the vocabulary with the scanner
and the checker importing rather than compiling their own." That wording
is mine and it overstates the problem. Verified at `3586970d`:

- `worksheet_checker.py:1190` calls `ps.CROSS_CHECK_LINE_RE.match(...)`
- `worksheet_checker.py:1623` calls `ps.RESOLVED_LINE_RE.match(...)`

The checker IMPORTS both from `provenance_scanner`. It does not compile
copies. So the state is not one duplicated set; it is TWO single homes,
each with its own importers and neither aware of the other:

| Vocabulary | Home | Importers |
|---|---|---|
| `Source`, `Ref`, `Also`, `See`, `Derived`, `Calculation` | `worksheet_keys.py` | request builder, checker, 3 test modules |
| `Cross-checked`, `Resolved` | `provenance_scanner.py` | checker |
| `Removed`, `Corrected` | nowhere | nothing |

**The live defect is that the two homes DISAGREE, not that they
duplicate.** The scanner's patterns are compiled `(?mi)` --
case-insensitive. `LEG_RE` in `worksheet_keys.py` carries no flags and
is case-sensitive. So `# CROSS-CHECKED:` is a record leg to the scanner
and an unclassified label to the builder. Under the new design that line
would be withheld and reported as unclassified while the scanner already
knows exactly what it is.

That mismatch survives ANY choice of home unless it is decided
deliberately. Whichever way it goes, it is a decision, not a detail:
case-insensitive matches the scanner and is more forgiving of hand-typed
comments; case-sensitive matches the builder and makes `# NOTE:` a
reportable defect rather than a silent synonym. The corpus contains both
spellings today.

---

## 2. Confirmation: (a) is the right home, and the check that would
have argued against it comes back the other way

The obvious objection to `worksheet_keys.py` is that it is named for
key minting, so the citation vocabulary would be a squatter. Checked:
it is not. The module docstring carries an explicit section headed
**"THE SECOND JOB: CITATION LEGS (L-207)"**, which states that the
citation prompt made `worksheet_checker.py` a second reader of the leg
grammar and that `legs_of` is the one shared implementation.

So the module already DECLARES ownership of the leg grammar. Adding the
record labels is a third label class inside a concern the module already
says it owns -- not a new job smuggled in beside an unrelated one.

Two supporting facts, both verified:

- `worksheet_keys.py` imports `ast`, `os`, `re` and `collections`.
  Nothing project-side. So `provenance_scanner` importing it introduces
  no cycle.
- That stdlib-only property is LOAD-BEARING, and it is the real argument
  against option (c) -- better than line count. The 52-site key
  round-trip runs in 0.7s in the maintenance run because the module it
  tests is cheap to import. Making `worksheet_keys` depend on the
  scanner puts that in the scanner's dependency shadow.

---

## 3. The scoping distinction: move the label SET, not the body grammar

"One home for the vocabulary" can be read two ways, and one of them
drags semantics into a keys module.

The scanner's constants are not label names. They are label names PLUS a
body contract. `CROSS_CHECK_LINE_RE` captures a named `body` group.
`RESOLVED_LINE_RE` has a companion `RESOLVED_BODY_RE` enforcing
`<worksheet> <key> -- <what> (L-nnn)`, with ISO-only dates and prose
dates rejected on purpose.

What belongs in the shared home is the **label set and its transport
policy**: which labels exist, and for each, does it travel to a
responder or is it withheld. What stays where the semantics live is the
**body grammar**: what a valid `Resolved:` body looks like, and who
validates it.

That split is the same two-axis model the Mode 7 review settled on --
transport and grammar as independent axes rather than one list. Applying
it here keeps `worksheet_keys.py` owning vocabulary and leaves
`provenance_scanner.py` owning what a record line MEANS.

Concretely: `worksheet_keys` gains the label set including the record
labels and `Review-note`. `provenance_scanner` keeps `RESOLVED_BODY_RE`
and its validation, and derives its line patterns from the shared label
names rather than from its own literals.

---

## 4. Two things the build owes under `safe-file-editing` 1.6

- The `worksheet_keys.py` docstring's "SECOND JOB" section must be
  updated in the same patch to say the module now owns the record labels
  and `Review-note` as well. `module_atlas.py` regenerates
  MODULE_ATLAS.md and MODULE_INDEX.md from that docstring, so a stale
  description propagates into two generated files.
- `provenance_scanner.py` changes what it does if its patterns become
  derived rather than literal. Its docstring moves with it.

---

## 5. What is NOT settled here

Whether the shared matcher is case-sensitive or case-insensitive. That
is a real decision with corpus evidence on both sides and it belongs to
Tony, not to the build. It is called out in section 1 so it is not
resolved by whichever module happens to be edited first.
