# Opus 5 Build Prompt — Batch 1 Cross-Check Patch Scripts

**Built on `2ccf6839c4278f01db00fbe2101440ab267a90c2`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Verify HEAD matches before building.**

---

## Context

You are Claude Opus 5, building transactional patch scripts for
Paloma's Orrery. Tony Quintanilla is the integrator. The attached
`PATCH_SPEC_batch1_cross_check.md` contains 47 edits across 5 shell
module files, implementing the results of the L-156 Phase 2 Batch 1
provenance cross-check.

This is a mechanical build job. Every value, citation, and replacement
string is fully specified in the patch spec. Your job is to translate
the spec into executable Python patch scripts, one per file, following
the project's established patching conventions.

## Skills to load

1. **safe-file-editing** — transactional binary-mode patching, bottom-up
   edit ordering, LF/ASCII gates, single-match assertions.
2. **agentic-pre-test** — py_compile + xvfb smoke test after each patch.
   Throwaway-copy rule: the deliverable is never edited by the pre-test.
3. **orrery-coding-conventions** — for any display-text edits that touch
   hover text, markers, or shell descriptions.

## What to produce

**Five patch scripts**, one per file:

```
patch_moon_cross_check.py
patch_eris_cross_check.py
patch_mercury_cross_check.py
patch_venus_cross_check.py
patch_pluto_cross_check.py
```

Each script:
1. Opens the target file in binary mode (`'rb'`).
2. For each edit (bottom-up by line number):
   - Finds the exact old bytes (assert exactly one match).
   - Replaces with new bytes.
3. Writes the result to the same path.
4. Reports success/failure per edit.
5. All-or-nothing: if any assertion fails, no write occurs.

**Conventions from the Mars and constants_new.py precedents:**
- Use `content.count(old_bytes)` to assert exactly 1 match before replacing.
- Print each edit ID (e.g., "MOON-1: Hill sphere Source") as it applies.
- Exit with error message (not silent failure) on mismatch.
- LF line endings throughout (no `\r\n`).
- ASCII only in all replacement text.

## Pull the files fresh

Before building each script, pull the target file from HEAD to verify
the exact byte content you're matching against:

```
https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/<filename>
```

## Key implementation decisions

**Venus de-duplication (VEN-4):** The spec offers two approaches:
(a) `.replace("\\n", "<br>")` reference, or (b) fix both copies in place.
Try approach (a) first. If the string escaping is fragile (the `\\n` in
the source is actual `\n` inside Python string literals), fall back to
(b) and add a `# NOTE: duplicated text — edit both copies together`
comment.

**Mercury sodium tail (MERC-2):** This edit changes both display text
AND a code parameter (`max_tail_length`). The display text appears in
two copies (info text and description dict). All three must change.

**Pluto exobase (PLUT-2):** The `radius_fraction` changes from 1.43 to
2.43, which will significantly change the rendered atmosphere shell
size. This is correct — the old value was a unit confusion (center-
distance interpreted as altitude). The shell will now be ~70% larger,
matching the actual exobase altitude.

**"Verified" line removal:** Every `# Verified: April 2026 via Gemini
fact-check` line in these 5 files gets removed. There are 3 in Eris
(lines 37, 210, 460) and scattered across the others. The patch
scripts should handle these as separate find-and-delete operations
(replace with empty string, which removes the line).

## Validation

After each patch script runs:
1. `py_compile` the patched file.
2. Run the xvfb smoke test per the agentic-pre-test skill.
3. Verify no non-ASCII bytes crept in.
4. Verify LF-only line endings.

## What NOT to do

- Do NOT regenerate complete files. These are targeted patches.
- Do NOT change anything not listed in the patch spec.
- Do NOT "improve" display text beyond what the spec says.
- Do NOT touch files outside the 5 listed.

## After the patches

Tony runs the scripts in VS Code (one at a time, checking output).
Tony commits and pushes. The next session documents in the ledger
and master plan, then continues with Batch 2.

---

*Prompt prepared August 3, 2026 by Claude Opus 4.6 (orchestration).*
