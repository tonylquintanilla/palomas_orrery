# Opus 5 Build Prompt: Skill Updates (orrery-coding-conventions + provenance-discipline)

**Built on `1e60c783779747835319a6b9b4bd2b76f6c61d3f`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Prepared:** August 4, 2026 by Claude Opus 4.6 (orchestration) · Tony Quintanilla, integrator
**Implements:** L-156 Batch 1 process conventions, Fable audit findings

---

## Who you are working for

Tony Quintanilla, PE — a retired civil and environmental engineer, artist,
and anthropologist. He builds Paloma's Orrery through conversational AI
collaboration ("vibe coding") and holds sole commit authority. The
codebase's structure and discipline are the product of iterative
collaboration with Claude, not something Tony wrote unassisted.

## Your job

Update two skills in the repo at `skills/<name>/SKILL.md` to encode
the conventions established during the L-156 Phase 2 Batch 1 cross-check
and the Fable consistency audit (August 3-4, 2026). The skills are
versioned, SHA-stamped artifacts — bump the version, update the SHA,
and add a version-history line at the top explaining what changed.

Both skills are at HEAD. Pull them from:
- `skills/orrery-coding-conventions/SKILL.md` (currently v1.1)
- `skills/provenance-discipline/SKILL.md` (currently v1.5)

## Skill 1: orrery-coding-conventions → v1.2

Add the following conventions. Each was established through the Batch 1
cross-check process and confirmed by Tony. Place them as new sections
in the appropriate location (after the existing shell dispatch section
is natural for most of these).

### 1a. Visualization constant vs range convention [QUALITY]

When a physical quantity has a range in the literature (e.g. Venus
troposphere 60-65 km, Moon inner core 240 ± some uncertainty), the
convention is:

- **Code constant:** best-sourced single value (the value that went
  through the three-model competitive cross-check).
- **Display text:** state the range in the description, identify the
  chosen visualization value.
- **`# Source:` comment:** cite the source for the chosen value AND
  note the range and the rationale for the choice.

Example:
```python
# Source: New et al. (2023), Icarus -- troposphere top 60-65 km.
#         Visualization at 60 km (lower bound, well-sourced).
```

This prevents "which value is right?" confusion when a future cross-check
finds a different number in a different paper — the choice and its
rationale are documented at the definition site.

### 1b. Hill sphere documentation standard [QUALITY]

Hill sphere radius_fraction values follow these conventions:

- **Distance:** perihelion distance (closest approach to the parent,
  where the Hill sphere is smallest — the conservative, worst-case
  bound). This is the project convention for all bodies.
- **Mass for barycenter binaries** (Pluto-Charon, Eris-Dysnomia): use
  the system mass (combined mass), since the Hill sphere belongs to the
  binary system, not the primary alone. For these bodies, the
  JPL-published mass IS the system mass (derived from the companion's
  orbit).
- **Mass for non-binaries:** use JPL-published mass for the body.
- **Display text:** state the Hill sphere extent in Mkm and in body
  radii, note perihelion convention in the `# Source:` comment.

Example:
```python
# Source: Standard Hill approximation, perihelion convention.
#         a = 30.171 AU (perihelion), GM_system = 869.326 km³/s²,
#         GM_Sun = 1.327e11 km³/s². r_Hill = a * (M/3M_sun)^(1/3).
```

### 1c. `<br>` canonical direction [QUALITY]

Module `_info` strings (consumed by the Tk GUI tooltip via `globals()`
and `build_shell_checkboxes()`) must use `\n` for line breaks, not
`<br>`. The Tk tooltip renders `<br>` as literal text.

The canonical text format is `\n`. Derive `<br>` at the Plotly hover
boundary — which is what the reference pattern in `shell_configs.py`
already does:
```python
'hover_text': neptune_hill_sphere_info.replace('\n', '<br>'),
```

For bodies not yet migrated to the reference pattern, `shell_configs.py`
carries its own inline copy with `<br>` for Plotly. Both copies must
agree on content even though they differ in format. The structural fix
(L-181) will eliminate the duplication.

**Migration status as of August 2026:**
- Reference pattern (text linked): Saturn, Uranus, Neptune, Sun
- Duplicated copies (text independent): Mercury, Venus, Moon, Mars,
  Earth, Eris, Pluto, Jupiter, Planet 9, Asteroid Belt, Comet

### 1d. Shell dispatch path — expanded for dual-pipeline awareness [QUALITY]

Update the existing "Live Shell Dispatch" section to note:

- `shell_configs.py` has two sections: `SHELL_CONFIGS` (sphere shells
  via `build_sphere_shell`) and `CUSTOM_SHELLS` (custom geometry via
  lazy-imported builder functions).
- The `tooltip` field in both `SHELL_CONFIGS` and `CUSTOM_SHELLS` is
  **dead data** — no consumer reads it (124 entries total). It exists
  but does not render. Tracked for a delete-or-wire decision in L-181.
- For sphere shells, `radius_fraction` in `SHELL_CONFIGS` controls the
  drawn geometry. The hover text describes the physical value. When
  these drift, the shell renders at the wrong size while the hover
  claims the correct size — Batch 1's geometry follow-up caught exactly
  this class.

### 1e. Layer chain gap handling [PRACTICE]

When a body's internal layers don't sum to the body radius (e.g.
Mercury: 2020 + 331 + 26 = 2377 km vs R = 2440 km), the gap represents
unmodeled structure. The convention:

- **Do not silently adjust** values to close the gap.
- **Flag in a code comment** at the outermost affected shell.
- **Keep the surface layer at rf 1.0** — it's the surface, regardless
  of whether the layers beneath it tile perfectly.
- **Adjusting visual thickness for readability is a Mode 5 decision**
  for Tony, not a patch target.

### 1f. Field note additions

Add to the Field Notes section:

- The reference pattern (text linked via `_info.replace()`) solves text
  duplication but NOT geometry-to-text drift. Saturn (fully migrated)
  carried the Fable audit's worst finding — proving the pattern alone
  doesn't prevent value drift. The single-source-of-truth constant
  layer (L-181) is the structural fix.
- "Defensible number, wrong citation" is the most common failure mode
  in cross-checks (GPT's framing, August 2026). The value passes a
  reasonableness test but the cited paper doesn't contain it, or cites
  a different paper entirely.

## Skill 2: provenance-discipline → v1.6

Add the following conventions, established during Batch 1.

### 2a. Batch 1 process findings — update the Batch Worksheet Workflow

Add after the existing step 6 (Gemini gets targeted prompts):

**7. Blind source lookup.** When multiple models diverge on a value and
the divergence might stem from confirmation bias (all models saw the
expected value in the prompt), run a follow-up round with **no expected
value** in the prompt. Present only the claim text and ask each model
to independently source it. This was the fourth round of the Batch 1
cross-check and resolved 8 previously unresolved items.

**8. Fable consistency audit.** After patches land, run a Fable
full-codebase audit checking internal consistency between visualization
constants and display text, and mapping dual-pipeline values for the
single-source-of-truth migration. This catches the class of error where
text is corrected but geometry constants are not — a gap invisible to
the per-claim worksheet approach. The audit prompt is
`documentation/PROMPT_fable_shell_consistency_audit.md`.

### 2b. Model credit convention [PRACTICE]

When a correction is found during cross-checking, note which model
found it in the `# Cross-checked:` annotation:

```python
# Cross-checked: Hauck et al. (2013) via Claude Opus 5 2026-08-03
#   (worksheet_claude_batch1_tier2.md) -- corrected from Margot (2012)
```

The model name is not vanity — it's the audit trail for which
verification leg produced the finding. Two Claude passes are one leg,
not two (same training data). Track which model produced each worksheet
to ensure genuine independence.

### 2c. Retired annotation format

Add a note that `# Verified: April 2026 via Gemini fact-check` is a
retired format. These stamps are being replaced during cross-check
batches with proper `# Cross-checked:` annotations that include:
- The authoritative source (not just "Gemini")
- The model that performed the check
- The worksheet reference on disk
- The ISO date of the check

The old format gave the appearance of verification without the audit
trail that makes it checkable. Remaining instances (44 in
shell_configs.py, 0 in the 5 Batch 1 files, 0 in Mars) are being
cleared in Batch 2.

### 2d. Geometry constants as first-class provenance claims

Add to the "Clearing a Flagged Claim" section or as a new subsection:

`radius_fraction` values in `shell_configs.py` are provenance claims
just as much as display-text numbers. When a cross-check corrects a
display value (e.g. outer core from 2074 km to 2020 km), the
`radius_fraction` must be updated in the same patch — not deferred.
The geometry follow-up that caught this gap in Batch 1 is the evidence
that text-only patches leave the render wrong while the hover text
claims it's right.

The scanner doesn't flag `radius_fraction` directly (it's a dict
constant, not a display string), so this class of drift is caught by
the Fable consistency audit (step 8 above), not by the scanner.

### 2e. Field note additions

- "Verified: April 2026" stamps can sit over values with 34% errors
  (Eris Hill sphere) — the stamp means "a model looked at it," not
  "a model verified it correctly." The competitive pattern with
  row-per-claim worksheets replaces this.
- Three fabricated or wrong-paper citations survived in Batch 1 files:
  Mercury "Pei et al." (mis-parsed given name → wrong author), Eris
  "Glein" (different paper by the same author), Mercury crust citing
  the paper that refutes the claimed value. Wrong-but-cited is worse
  than uncited because the citation suppresses the suspicion that would
  catch it.

## Build conventions

- Deliver two updated SKILL.md files (complete files, not patches —
  skills are small enough for agentic delivery).
- Bump version numbers: orrery-coding-conventions 1.1 → 1.2,
  provenance-discipline 1.5 → 1.6.
- Update the SHA stamp in the version line to the HEAD SHA this prompt
  is anchored to.
- Add a version-history sentence at the top (same pattern as the
  existing version notes).
- ASCII only, LF line endings.
- Do not change any existing content unless it contradicts a new
  convention — additions only.
- The `fires_when` frontmatter field and `description` field may need
  minor updates if the new conventions add trigger words.

## Verification

- `py_compile` is not applicable (these are .md files).
- Verify that every new convention references the session or document
  it emerged from (Batch 1, Fable audit, specific L-item).
- Verify that no existing convention is contradicted by the additions.
- Verify ASCII-only content (no unicode in the delivered files).

---

*Prompt prepared August 4, 2026 by Claude Opus 4.6 (orchestration).*
