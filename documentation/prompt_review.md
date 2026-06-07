Let me verify the inventory claims in the prompt against the actual codebase before advising Tony.Line counts match. Now let me verify the `_info` import chain claims.This is a critical finding. Let me verify whether `/mnt/project/` is stale or current relative to Step 2 (May 11 refactor):I've audited the prompt against the actual codebase. Here's my review.

## Bottom line

The prompt is well-structured and the architecture is sound, but there are **four issues that will produce a flawed manifest if not fixed** before sending to Opus 4.7. Two are critical, two are gaps in the architecture spec.

---

## Critical issue 1: `/mnt/project/` is stale and the prompt tells Opus 4.7 to trust it 

The prompt says (line 356): *"The project files are up to date and available for reading."* This is **wrong for our session snapshot**. 

I verified by grepping for the Step-2 marker `hoverinfo='skip'` across all 15 shell files in `/mnt/project/`:

```
ONLY post-Step-2:  solar_visualization_shells.py, comet_visualization_shells.py
STILL pre-Step-2:  mercury, venus, earth, mars, jupiter, saturn, uranus, neptune,
                   moon, pluto, eris, planet9, asteroid_belt
```

Mercury atmosphere shell in `/mnt/project/` still has `text=[layer_info['description']] * len(x)` and `n_points=50` — pure pre-Step-2 form. If Opus 4.7 extracts data from these files, the manifest will inherit:
- Wrong `n_points` (50 instead of 20/25)
- Hover text written for the old N-copy pattern (may include the "TO VISUALIZE..." preamble formatted for an older context)
- Possibly different `_info` strings if Step 2 also normalized them
- And it won't see the legendgroup / info-marker conventions that Step 2 established

This is exactly the staleness anti-pattern formalized in v3.21. The protocol says: *"A bad snippet is a localized error. A complete file from a stale base is destructive."*

**Fix:** Upload the current post-Step-2 versions of all 15 shell files to the Opus 4.7 session, and replace prompt line 356 with something like:

> Source of truth for data extraction: the uploaded files only. `/mnt/project/` may be a pre-Step-2 snapshot — solar and comet shells are the only files there that reflect Step 2. Do not extract `n_points`, `text` patterns, or hover strings from any `/mnt/project/` shell file. If a value can't be confirmed from an uploaded file, flag it for Tony rather than guessing.

This is the single most important fix. Everything else is secondary.

---

## Critical issue 2: GUI tooltip wiring is more complex than the prompt admits

The prompt collapses tooltip wiring into one sentence: *"GUI tooltip text reads directly from `shell_configs.py` instead."* But there are actually **three different wiring paths** in the live code, and the manifest must address all three:

**Path A — Earth, inline by name (11 calls, ~lines 8021-8092):**
```python
CreateToolTip(earth_inner_core_checkbutton, earth_inner_core_info)
```
Earth bypasses `build_shell_checkboxes` because of the "Earth System Visualization" special case (comment in `celestial_objects.py` line 1349). These 11 references are by *name* in `palomas_orrery.py`.

**Path B — most planets, dynamic via `globals()` (78 tooltips, all via one function):**
`palomas_orrery.py` lines 8004-8279 call `build_shell_checkboxes('Mercury', ...)` etc., passing `globals()` as the tooltip dict. In `celestial_objects.py` line 1485:
```python
tooltip_text = tooltips_dict.get(tooltip_name, "No information available")
```
That `tooltip_name` is built at runtime as `f"{body_prefix}_{shell['var_suffix']}_info"`. The imports in `palomas_orrery.py` exist only to put those `_info` strings into `globals()`. A raw grep won't find these references — that's why my first usage scan reported them as "unused."

**Path C — Sun and asteroid belts, direct import from shell files:**
`palomas_orrery.py` lines 209-246 import `core_info`, `radiative_zone_info`, `main_belt_info`, etc. **directly** from `solar_visualization_shells.py` and `asteroid_belt_visualization_shells.py` — bypassing the `planet_visualization.py` re-export chain entirely. These are used inline like Path A.

**What this means for the manifest:**
- Phase D must update `build_shell_checkboxes()` in `celestial_objects.py` to read from `SHELL_CONFIGS` — **`celestial_objects.py` is not in the prompt's "Files to audit" list at all.**
- Path A's 11 Earth tooltips need inline replacement (e.g. `SHELL_CONFIGS['Earth']['inner_core']['tooltip']`)
- Path C's direct imports from solar/asteroid shells also need redirecting if those shells are migrated

**Fix:** Add `celestial_objects.py` to the audit list. Have Opus 4.7 produce explicit before/after for `build_shell_checkboxes` and for the Earth inline calls. The "~210 lines disappear" claim is approximately right in total but the wiring fix is more than one edit.

---

## Gap 1: `CUSTOM_SHELLS` registry has no tooltip field

Custom shells (Mercury sodium tail, Jupiter ring system, Saturn magnetosphere, Earth LEO/GEO, etc.) all need GUI tooltips. The architecture as specified puts tooltips in `SHELL_CONFIGS`, but `CUSTOM_SHELLS` only contains `module.function` strings. So where does the sodium-tail tooltip live?

The handoff doesn't address this either. The prompt should pick one of:

1. **Add a `tooltip` field to `CUSTOM_SHELLS` entries** — restructure `CUSTOM_SHELLS` from `{shell_name: 'module.function'}` to `{shell_name: {'builder': 'module.function', 'tooltip': '...'}}`.
2. **Separate `CUSTOM_SHELL_TOOLTIPS` dict in `shell_configs.py`** — keeps the registry simple but splits the data.
3. **Leave `_info` strings in shell files for custom shells only** — partial migration; the `_info` import chain shrinks but doesn't disappear.

This needs a decision **before** Opus 4.7 writes the manifest — otherwise option-1 vs option-2 forces structural rework mid-implementation. Recommend deciding now and stating the answer in the prompt.

---

## Gap 2: "Fully archivable" claim conflicts with Mesh3d crust functions

Prompt Phase B claims Pluto, Planet 9, Eris, Moon are sphere-only and their shell files become "fully archivable." But:

- `pluto_visualization_shells.py` `create_pluto_crust_shell` uses `go.Mesh3d` (triangulated mesh sphere with flat shading) — *not* `Scatter3d` markers
- Same pattern almost certainly in: Mercury crust, Venus crust, Earth crust, Mars crust, Moon crust, Eris crust, plus Jupiter/Saturn/Uranus/Neptune cloud_layer

The prompt correctly flags this as a judgment call (page bottom of "What the manifest must contain" #7), but doesn't follow the implication: **if Mesh3d crusts stay as custom geometry, then Pluto/Moon/Eris/Planet9 shell files are NOT fully archivable** — they each keep the crust function. The "archivable" claim and the Mesh3d question need to be resolved together.

Three options:

(a) **Build a second config-driven builder** (`build_mesh3d_shell`) for Mesh3d-style sphere shells, including the lighting/flatshading parameters. Crusts become config-driven. Files truly archivable.

(b) **Refactor Mesh3d crusts to Scatter3d sphere shells.** Loses the smooth-surface visual effect (which Tony may or may not value). One-time visual judgment call per body.

(c) **Mesh3d crusts stay as custom shells.** Phase B isn't "fully archivable" — Pluto/Moon/Eris keep ~80-line shell files each holding just the crust function.

Recommend deciding now and saying so in the prompt. Otherwise Opus 4.7 has to pick, and may pick differently than you would.

---

## Smaller issues, worth fixing in passing

- **Inventory: Mercury "custom geometry" column.** Prompt says Mercury custom = "sodium tail, magnetosphere" (line ~275). Handoff `CUSTOM_SHELLS` for Mercury also lists `atmosphere` as custom (line 434). The actual code shows Mercury's atmosphere is a `Scatter3d` sphere shell with a tagged-on `create_sun_direction_indicator()` call after the trace list. So atmosphere belongs in `SHELL_CONFIGS`, not `CUSTOM_SHELLS`. The sun-direction indicator is the wrinkle — does `build_sphere_shell()` get an optional `add_sun_indicator=True` flag, or does the dispatch caller add it post-hoc? Flag for Opus 4.7 to resolve.

- **Solar shell count.** Prompt says 13 sphere + 3 custom for solar. Actual count: 15 `create_sun_*_shell` functions (gravitational, outer_oort, inner_oort, inner_oort_limit, heliopause, termination_shock, outer_corona, inner_corona, streamer_belt, roche_limit, alfven_surface, chromosphere, photosphere, radiative, core) + 3 custom (hills_cloud_torus, outer_oort_clumpy, galactic_tide). Minor inventory drift.

- **Line endings in /mnt/project/ snapshot:** Pure CRLF for `palomas_orrery_helpers.py` and `planet_visualization.py`. Mixed (CRLF + LF) for 11 of 15 shell files. The prompt says all shell files are LF post-Step-2 — that's likely true on Tony's disk, but again the snapshot is misleading. The manifest's "confirm LF" instruction is the right safeguard; just don't expect uniform pre-existing LF.

- **Dispatch chain end line.** Actually `535-867`, not `535-860`. Mark line numbers approximate.

- **`_info` import counts.** Actual: 87 in helpers (all dead, confirmed), 89 in `palomas_orrery.py` (11 named, 78 dynamic-via-globals). Prompt says "~105" in each — close enough for budgeting, but the dynamic-via-globals point matters for the wiring fix.

- **n_points convention precedence.** Handoff says default n_points=20 outer / 25 inner. But after Step 2 each shell has a specific tuned value. Manifest should specify: *use the n_points value from the current uploaded shell file, fall back to 20/25 only if missing.* Otherwise Step 2 tuning gets thrown away.

---

## One concern about manifest scope vs context window

The single-info-marker manifest was 2,342 lines and hit context limits during implementation. This refactor is bigger:

- ~80 sphere shell configs to extract (each ~15-line config block)
- ~20 `CUSTOM_SHELLS` entries
- `build_sphere_shell()` implementation + `build_mesh3d_shell()` if option (a) above
- Dispatch chain replacement
- `_info` import cleanup across 4 files (palomas_orrery.py, palomas_orrery_helpers.py, planet_visualization.py, celestial_objects.py)
- LF / Python-binary-mode notes throughout

Conservative estimate: 2,500-3,500 lines if Opus 4.7 produces full before/after for everything. Even with Phase A/B/C/D structure, **the full manifest in one document may not fit one session's context** for either Opus 4.7 (writing it) or Opus 4.6 (executing it).

Three options worth considering:

1. **One Opus 4.7 session per phase.** Phase A in session 1, Phase B in session 2, etc. Each session inherits decisions from prior phases via Tony.
2. **Phase A in full mechanical detail; B/C/D as patterned outlines.** Phase A proves the pattern (Mercury POC), and B/C/D are 50-line "follow the Mercury template for X" outlines that Opus 4.6 fills in mechanically using the uploaded shell files.
3. **Manifest specifies structure + extraction rules; implementation Claude extracts values.** Opus 4.7 writes the builder, the config schema, and the per-body section template. Tony+4.6 extract the actual values during implementation from the uploaded files. Less mechanical, more like Mode 1 guided implementation — but the manifest fits in 800-1200 lines.

I'd lean toward (2) personally — Phase A in full detail, B/C/D as patterned outlines. The info-marker manifest worked because the pattern was simple enough that "apply this conversion to 18 files" produced verifiable mechanical output. A shell config extraction has more variation (radius_fraction vs radius_au, sphere vs mesh, sun_indicator add-on, hill sphere as 89× scale), so Phase A needs to be exhaustive — but once that pattern is locked, B/C/D become "Mercury, but for Pluto" templates that Tony+4.6 can execute together.

---

## Suggested edits to the prompt before sending

A minimal patch list:

1. **Add staleness warning.** Replace the "project files are up to date" sentence with the explicit upload-as-source-of-truth instruction above.
2. **Add `celestial_objects.py` to "Files to audit"** and call out `build_shell_checkboxes` as the central wiring point for Path B tooltips.
3. **Pre-decide the CUSTOM_SHELLS tooltip question.** Pick option 1, 2, or 3 above and state it in the architecture section.
4. **Pre-decide the Mesh3d crust question.** Pick option a, b, or c above and state it in the architecture section. This determines whether Phase B's "fully archivable" claim is true.
5. **Clarify the Mercury atmosphere classification** (sphere with sun-direction indicator, not custom).
6. **Specify n_points precedence:** use the value from the current shell file; 20/25 only as fallback.
7. **State the phasing/manifest-size strategy** explicitly (one of the three options above) so Opus 4.7 calibrates its output.
8. **Mark line ranges as approximate** (palomas_orrery.py is at 9,938 lines and shifting; absolute lines drift between sessions).

If you make those edits and upload the 15 current shell files + `celestial_objects.py` + `palomas_orrery.py` + `palomas_orrery_helpers.py` + `planet_visualization.py` + `constants_new.py` to the Opus 4.7 session, the manifest should come back clean. Without them, it'll come back precise-looking but built on wrong data — and the manifest's authority is exactly what makes that dangerous.

Ready to help you patch the prompt, or wait for your call on the architecture decisions first?