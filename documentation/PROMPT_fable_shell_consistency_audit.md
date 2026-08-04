# Fable Audit Prompt: Shell Visualization Internal Consistency

**Built on `55b07a6cf5ebfe2dce604d4e9fbff3c010e1b0eb`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared:** August 4, 2026 by Claude Opus 4.6 (orchestration) · Tony Quintanilla, integrator

---

## Who you are working for

Tony Quintanilla, PE — a retired civil and environmental engineer, artist,
and anthropologist. He is not a professional programmer and not a formally
trained astronomer. He builds Paloma's Orrery through conversational AI
collaboration ("vibe coding") and holds sole commit authority and final
judgment. The codebase's structure and discipline are the product of
iterative collaboration with Claude, not something Tony wrote unassisted.
Read code quality as evidence of the partnership, not of Tony's independent
programming skill.

## Your role

Fable: large-context comprehensive audit. You have two jobs:

### Job 1: Find internal consistency failures

Places where a visualization constant defined in code drifts from what
the display text (hover text, tooltip, info string) claims, or where a
`# Source:` citation no longer matches the value sitting below it. This
is the same class of error that Batch 1 of the L-156 provenance
cross-check found and fixed in 5 files (examples: Eris Hill sphere said
"~9.4 Mkm" but the correct derivation gives ~14.3; Mercury sodium tail
said "10,000 R_M" but the sourced papers say ~1,400; Pluto exobase said
"1.43 R_Pluto" but the math gives 2.43). Find any remaining instances
across the **entire** set of shell files, not just the ones already
patched.

This is a pattern-recognition audit, not a value-verification audit. You
are NOT being asked to independently research whether each number is
scientifically correct — that is Batch 2's three-model competitive
cross-check job. You ARE being asked to find places where the code
**contradicts itself**: a `radius_fraction` that doesn't match the km
value in the hover text, a temperature in the display string that
doesn't match the temperature in the `# Source:` comment, a thickness
claimed in one place and a different thickness claimed 20 lines later,
a `shell_configs.py` entry that says one thing while the matching shell
module `_info` string says another.

### Job 2: Map every dual-pipeline value for single-source-of-truth migration

The deeper structural problem is that the same physical value often
lives in two (or more) independent places as separately typed literals,
with no shared constant linking them. When a value gets corrected in
one place but not the other, the codebase drifts — Batch 1 found
exactly this. The fix is not just patching the drifted copy; it's
defining each value **once** as a named constant and referencing it
from every place that needs it.

**Example of the problem:** Mercury's core radius is `2020 km`. This
value appears as a `radius_fraction` in `shell_configs.py` (computed
as `2020 / 2440`), as the literal string `"2020 km"` in the hover text,
and potentially in the `_info` string in the shell module. Three
independent copies of the same fact. If the value is corrected, all
three must be found and updated manually.

**Example of the fix (already in place for some bodies):** Saturn,
Uranus, and Neptune use a reference pattern where `shell_configs.py`
imports the `_info` string from the shell module:
```python
'hover_text': neptune_hill_sphere_info.replace('\n', '<br>'),
'tooltip': neptune_hill_sphere_info,
```
This eliminates the text duplication. But even this pattern doesn't
solve the constant-vs-text problem — if `radius_fraction: 4685` encodes
a Hill sphere radius of 116,000,000 km and the hover text also states
"116 million km", there's still no shared constant linking them.

**What to produce:** For each body, map every value that appears in
more than one place (code constant AND display text, or shell module
AND shell_configs.py, or both). For each, note:
- Where copy 1 lives (file, line, form — e.g. `radius_fraction: 0.83`)
- Where copy 2 lives (file, line, form — e.g. `"2020 km"` in hover text)
- Whether they currently agree or have drifted
- Whether the reference pattern is already in use for this body's text

This map is the input to the migration design. It tells us where to
define constants and how many call sites each one has.

## The architecture you need to understand

Each celestial body's shell visualization has **two storage locations**
that must agree:

1. **Shell module** (`<body>_visualization_shells.py`): contains `_info`
   strings (consumed by the GUI for tooltip text) and custom geometry
   functions (sodium tail, magnetosphere, radiation belts, etc.).

2. **`shell_configs.py`**: contains `SHELL_CONFIGS` (a dict driving
   `build_sphere_shell()` for standard sphere shells — has `hover_text`,
   `tooltip`, `radius_fraction`, `opacity`, `color`, etc.) and
   `CUSTOM_SHELLS` (a dict mapping custom geometry to its builder
   function and tooltip text).

**The migration status is mixed.** Some bodies (Saturn, Uranus, Neptune)
already use a reference pattern in `shell_configs.py`:
```python
'hover_text': neptune_hill_sphere_info.replace('\n', '<br>'),
'tooltip': neptune_hill_sphere_info,
```
For those, editing the shell module _does_ reach the render. Other bodies
(Moon, Eris, Mercury, Venus, Pluto) still carry duplicated inline copies
in `shell_configs.py`. For those, the shell module text is **dead code**
— `shell_configs.py` is what actually renders. Both copies must agree
even when only one renders, because a future migration would promote the
currently-dead copy.

**What actually drives the render:** `build_sphere_shell(config, ...)`
reads `hover_text` and `tooltip` from the `SHELL_CONFIGS` dict entry.
Custom geometry functions in the shell modules produce their own traces
with inline hover text. The `_info` strings in the shell modules are
consumed by `palomas_orrery.py` via `globals()` for
`build_shell_checkboxes()` tooltip wiring.

## Files to audit (16 total, ~17,600 lines)

**Already cross-checked (Batch 1 + Mars precedent) — audit for
post-patch internal consistency and any residuals the patches missed:**

| File | Lines | Notes |
|------|------:|-------|
| mercury_visualization_shells.py | 427 | Patched Aug 2026 |
| moon_visualization_shells.py | 649 | Patched Aug 2026 |
| eris_visualization_shells.py | 547 | Patched Aug 2026 |
| venus_visualization_shells.py | 743 | Patched Aug 2026 |
| pluto_visualization_shells.py | 689 | Patched Aug 2026 |
| mars_visualization_shells.py | 924 | Cross-checked Aug 2026 (precedent) |

**Not yet cross-checked — full audit:**

| File | Lines | Notes |
|------|------:|-------|
| jupiter_visualization_shells.py | 1044 | Batch 2 target |
| saturn_visualization_shells.py | 1238 | Batch 2 target |
| uranus_visualization_shells.py | 1221 | Batch 2 target |
| neptune_visualization_shells.py | 1753 | Batch 2 target |
| earth_visualization_shells.py | 1149 | |
| solar_visualization_shells.py | 1535 | |
| comet_visualization_shells.py | 2120 | |
| asteroid_belt_visualization_shells.py | 502 | |
| planet9_visualization_shells.py | 307 | |

**Central config (audit all body blocks):**

| File | Lines | Notes |
|------|------:|-------|
| shell_configs.py | 2759 | SHELL_CONFIGS + CUSTOM_SHELLS |

## What to check (per body, per shell)

For each shell entry across both the module and `shell_configs.py`:

### Consistency checks (Job 1)

1. **Constant vs display text.** Does the `radius_fraction` value match
   the radius or thickness in km stated in the hover text, given the
   body's radius? Does the `opacity` make sense relative to what the
   text describes? Does a colour comment (e.g. "dark red-orange at
   1700K") reference a value that's been removed from the display text?

2. **Internal text consistency.** Does the same shell say "26 km" in one
   sentence and "35 km" in another? Does an `_info` string say one value
   while its `shell_configs.py` `hover_text` counterpart says a
   different value?

3. **Source-vs-value consistency.** Does a `# Source:` comment cite a
   paper with a specific value that doesn't match the value immediately
   below it? Does a body-level header `# Source:` cite authors whose
   values were replaced by Batch 1 patches?

4. **Stale legacy annotations.** Any `# Verified: April 2026 via Gemini
   fact-check` stamps — these are a retired format. Note their location
   but don't treat them as findings requiring a fix; they'll be cleaned
   up in Batch 2.

5. **Shadow constants.** Any hardcoded numeric literals that duplicate
   values from `constants_new.py` (e.g. `SUN_RADIUS_KM = 695700`,
   `KM_PER_AU = 149597870.7` defined locally when they're already
   importable). Known precedent: `comet_visualization_shells.py` lines
   492-493.

6. **Cross-copy drift.** Where both the shell module and
   `shell_configs.py` carry the same text, do they actually match? Flag
   any divergence, noting which copy is the one that renders (usually
   `shell_configs.py` for sphere shells).

### Single-source-of-truth map (Job 2)

7. **Dual-pipeline values.** For each shell, identify every physical
   value (radius, thickness, temperature, distance, pressure, etc.)
   that appears in more than one form. Common patterns:

   - A km value typed as a literal in hover text AND encoded as a
     `radius_fraction` in `shell_configs.py` (e.g. "2020 km" in text,
     `radius_fraction: 0.83` computed from `2020 / 2440`)
   - The same text in an `_info` string in the shell module AND as
     inline `hover_text`/`tooltip` in `shell_configs.py` (the
     duplication that the reference pattern solves)
   - A value in a `# Source:` comment AND in the display string AND
     as a code constant — three independent copies

   For each, record:
   - **Value**: what physical quantity (e.g. "Mercury core radius 2020 km")
   - **Copy 1**: file, line, form (e.g. `shell_configs.py:98`,
     `radius_fraction: 0.83`)
   - **Copy 2**: file, line, form (e.g. `shell_configs.py:105`,
     `"Core radius approximately 2020 km"` in hover_text)
   - **Copy 3** (if any): file, line, form
   - **Currently agree?**: yes / no / can't tell
   - **Reference pattern?**: does this body already use the
     `_info.replace('\n', '<br>')` pattern for its text? (yes = text
     copies are linked; no = text copies are independent)

8. **Bodies already migrated.** Note which bodies already use the
   reference pattern for text, so the migration plan knows which
   bodies still need it. From the Batch 1 as-built: Saturn, Uranus,
   and Neptune are migrated; Moon, Eris, Mercury, Venus, and Pluto
   are not. Confirm this and extend to all bodies.

## What NOT to do

- **Do not independently verify scientific accuracy.** That is the
  three-model competitive cross-check's job. You are checking internal
  consistency and mapping the dual-pipeline structure.
- **Do not propose fixes or design the constant layer.** Flag findings
  and map the structure; Tony and the orchestrating Claude will design
  the migration.
- **Do not cite from training memory.** If you notice a value looks
  wrong based on your knowledge, you may note that in a "suspicion"
  column, but do not assert the correct value.

## Output format

### Job 1 output: Findings table

One table per file, findings only (skip files with no findings). Each
row is one finding:

| # | File | Line(s) | Shell | Finding type | Description |
|---|------|---------|-------|-------------|-------------|

Finding types:
- **CONSTANT_VS_TEXT** — a code constant contradicts its display text
- **TEXT_VS_TEXT** — two display texts for the same shell disagree
- **SOURCE_VS_VALUE** — a `# Source:` comment cites a value that
  doesn't match the code
- **CROSS_COPY_DRIFT** — shell module and shell_configs.py diverge
- **SHADOW_CONSTANT** — hardcoded value that should be an import
- **STALE_ANNOTATION** — `Verified: April 2026` stamp (informational)
- **SUSPICION** — the value looks internally consistent but implausible
  (flag for the cross-check, don't assert)

After all tables, provide a **summary count** by file and by finding
type.

### Job 2 output: Single-source-of-truth map

One table per body, covering all shells. Every row is a physical value
that exists in more than one place:

| Value | Copy 1 (file:line, form) | Copy 2 (file:line, form) | Copy 3? | Agree? | Ref pattern? |
|-------|--------------------------|--------------------------|---------|--------|-------------|

After all body tables, provide a **migration status summary**:

| Body | Text ref pattern? | # dual-pipeline values | # drifted |
|------|------------------|----------------------|-----------|

This summary is the input for designing the single-source-of-truth
constant layer.

## Completed pre-work (do not repeat)

The following greps were run against HEAD `55b07a6` and confirmed clean:

- "10,000" as Mercury's sodium tail: gone from source (survives only in
  a `# Removed:` note and one stale comment in `palomas_orrery.py`
  line 7565)
- "9.4" as Eris Hill sphere: gone (survives only in a `# Corrected:`
  note)
- "1074" as Mercury outer core: gone from shell files (only in
  `orbital_elements.py` eccentricity values — different context)
- "Pei et al" (fabricated citation): gone from source files (only in
  patch script anchor text)
- "Verified: April 2026" in the 5 Batch 1 shell modules: all clean
- "Verified: April 2026" in `shell_configs.py`: 16 remaining (listed
  in the as-built section 6c — out of Batch 1 scope)

## Known residuals from the Batch 1 as-built (confirm or extend)

These were flagged but deliberately left in place pending Tony's decision.
Confirm they are still present and note any related findings nearby:

a. Mercury mantle diamond claim — `mercury_visualization_shells.py`
   line 55 and `shell_configs.py` lines 144, 149
b. Stale `shell_configs.py` body-level headers — Mercury (lines 93-94)
   cites Margot/Sori after Batch 1 replaced their values; Moon (lines
   236-239) cites Apollo after Batch 1 replaced with Nakamura
c. Moon `# dark red-orange at 1700K` colour comment — line 56 of
   `moon_visualization_shells.py`; temperature removed from display text
d. Stale comment in `palomas_orrery.py` line 7565 referencing
   "sodium tail (10,000 body radii)"

---

*Prompt prepared August 4, 2026 by Claude Opus 4.6 (orchestration).*
