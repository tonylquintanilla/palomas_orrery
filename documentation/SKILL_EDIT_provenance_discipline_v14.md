# Provenance-discipline v1.4 edit — two changes + version bump

Three edits in `skills/provenance-discipline/SKILL.md`.

---

## Edit 1: Version block (line 9)

Find:
```
Skill version: 1.3 | Cut from palomas_orrery @ 4b6b5c12 | July 31, 2026
Source: project_instructions_v3_29.md Part 3 (Provenance Audit, Fetched vs
Recalled) + food insecurity build handoff + scanner source at HEAD. v1.1
adds the report domain-classification mechanics, the Review-Repair
Protocol (promoted from documentation/provenance_audit_handoff_v4.md),
and field notes from the F1 provenance-cleanup groundwork session (July
2026): the by-file/by-file-type report breakdown, a self-referential
scanning quirk, and a stale-audit-doc near-miss. v1.2 updates the
role-driven-inclusion bullet for L-163 Phase 3: a coverage gap is
resolved by tagging the module's own docstring, since ROLE_MAP is now a
regenerated mirror rather than a hand-maintained dict. MODULE_DOMAIN_MAP
and classify_domain() are unaffected and remain hand-maintained. v1.3
adds No Shadow Constants [CRITICAL]: local copies of constants_new.py
values must be deleted and replaced with proper imports — a frozen copy
bypasses the citation chain and drifts silently, same failure class as
citing over recalled data.
```

Replace with:
```
Skill version: 1.4 | Cut from palomas_orrery @ <SHA after push> | August 1, 2026
Source: project_instructions_v3_29.md Part 3 (Provenance Audit, Fetched vs
Recalled) + food insecurity build handoff + scanner source at HEAD. v1.1
adds the report domain-classification mechanics, the Review-Repair
Protocol (promoted from documentation/provenance_audit_handoff_v4.md),
and field notes from the F1 provenance-cleanup groundwork session (July
2026): the by-file/by-file-type report breakdown, a self-referential
scanning quirk, and a stale-audit-doc near-miss. v1.2 updates the
role-driven-inclusion bullet for L-163 Phase 3: a coverage gap is
resolved by tagging the module's own docstring, since ROLE_MAP is now a
regenerated mirror rather than a hand-maintained dict. MODULE_DOMAIN_MAP
and classify_domain() are unaffected and remain hand-maintained. v1.3
adds No Shadow Constants [CRITICAL]: local copies of constants_new.py
values must be deleted and replaced with proper imports — a frozen copy
bypasses the citation chain and drifts silently, same failure class as
citing over recalled data. v1.4 rewrites Review-Repair Protocol step 2:
cross-checking is the competitive pattern (same worksheet, independent
models, Tony compares), not one model reviewing another's output. The
worksheet format is the discipline — it forces primary source citations
per cell, preventing any cross-checker from fabricating authority from
training memory.
```

---

## Edit 2: Replace step 2 and add the discipline note (lines ~63-75)

Find:
```
2. **Tony and/or Gemini research and verify.** This is where the actual
   sourcing happens -- an outside authority is consulted, not Claude's
   training memory.
3. **Claude mechanically inserts the confirmed citations/corrections.**
   Transcribe what came back from step 2; do not add, embellish, or
   "helpfully" fill gaps with recalled values while doing this.

Why this order, not "Claude checks its own training data first": a
citation Claude invented to clear a flag is the exact failure this skill
exists to prevent (see Clearing a Flagged Claim). The worksheet step is
Claude's real contribution -- triage, grouping, flagging what's odd -- not
verification.
```

Replace with:
```
2. **Cross-check via competitive pattern.** The same worksheet goes to
   both Claude and Gemini (or another cross-checker) independently --
   same prompt, independent answers. Tony compares. Convergence builds
   confidence; divergence flags where to dig. This is NOT one model
   reviewing the other's output -- both work from the original claims,
   not from each other. The worksheet format is the discipline: every
   cell requires a primary source citation, so a model working from
   memory instead of sourcing produces visibly empty citation fields.
3. **Claude mechanically inserts the confirmed citations/corrections.**
   Transcribe what came back from step 2; do not add, embellish, or
   "helpfully" fill gaps with recalled values while doing this.

Why this order, not "Claude checks its own training data first": a
citation Claude invented to clear a flag is the exact failure this skill
exists to prevent (see Clearing a Flagged Claim). The worksheet step is
Claude's real contribution -- triage, grouping, flagging what's odd -- not
verification.

**Why the worksheet format matters for the cross-checker too.** The same
"fetched not recalled" rule that governs Claude's citations governs the
cross-check. A known failure mode for any AI cross-checker is fabricating
authority from training memory when the output format allows ungrounded
narrative. The structured worksheet does not -- it forces primary source
citations per cell. Constrain the format, and the discipline follows.
```

---

## Edit 3: Update the Skill Manifest in the protocol

Tony, when you next update project_instructions, bump the Skill Manifest
row for provenance-discipline from 1.3 to 1.4. The `fires_when` field
is unchanged.

---

After both edits, push, then stamp `<SHA after push>` on line 9.
