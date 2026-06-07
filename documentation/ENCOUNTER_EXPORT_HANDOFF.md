# Encounter Export — Design Handoff

**May 4, 2026 | Tony + Claude (Opus 4.6) | Design session + encyclopedia build**
**Updated May 8, 2026 | Tony + Claude (Opus 4.6 + Opus 4.7) | Diagnostic + fix session**

---

## What this is

A new export path in Gallery Studio that captures spacecraft encounter
visualizations as Python dict entries for `spacecraft_encounters.py`.
The goal: the hard work of finding an encounter, refining the camera,
selecting traces, and getting the view right should not evaporate.
Studio already captures this work for the gallery (Fork 1). This adds
Fork 2: the same curation work, exported as an orrery encounter preset.

## The problem it solves

Several fields in `SPACECRAFT_ENCOUNTERS` require plotting the encounter
first, visually exploring it, then manually transcribing numbers from
hover text into code. The loop is: Orrery -> eyes -> code -> Orrery again.
Studio already has the view parameters. This closes the loop.

## Current status (May 8, 2026)

The encounter exporter exists and is functional. The May 8 diagnostic
session identified six bugs in the extraction pipeline, fixed five
(animation loss deferred), and validated the round-trip through Tests A-C.

**Tests A-C passed.** The pipeline correctly extracts center body,
encounter date, distance, and scale for the Psyche Phobos flyby.
The generated dict round-trips through the Go button and produces
the correct plot.

**Tests D-H remain** (regression, edge cases). See TEST_encounter_export_fix.md.

### Bugs fixed (May 8, 2026)

| Bug | Description | Fix | Files |
|-----|-------------|-----|-------|
| 1 | Center defaults to Sun | Detect from hover text + manual entry field | gallery_studio.py |
| 2 | Wrong closest point (Full Mission vs Plotted Period) | Deconflict trace names at source | apsidal_markers.py, palomas_orrery.py, gallery_studio.py |
| 3 | No surface distance extraction | Extract both center-to-center and surface | gallery_studio.py |
| 4 | Date format breaks parsers | Pre-fill from hover, normalize output, defensive parser | gallery_studio.py, spacecraft_encounters.py |
| 5 | Animation loss (Go button always static) | **Deferred to Phase C** | — |
| 6 | Psyche full mission empty dates | Fill from celestial_objects.py | spacecraft_encounters.py, gallery_studio.py |

### Additional fixes found during testing

| Issue | Fix | File |
|-------|-----|------|
| Scale override — adaptive resolution ignores dict scale | Dict scale takes priority when present | spacecraft_encounters.py line 762 |
| plot_actual_orbits missing qualifier | Added trajectory qualifier at third call site (line 3384) | palomas_orrery.py |
| Doubled spacecraft name in encounter marker | Changed label to exclude spacecraft name | spacecraft_encounters.py (dict entry) |
| Encounter marker not labeled as Horizons-refined | Added `_horizons_refined` flag + "(Horizons)" suffix | spacecraft_encounters.py |
| Mars GA dates still malformed | Manually corrected to YYYY-MM-DD HH:MM:SS | spacecraft_encounters.py |

### Key design decisions from diagnostic session

**Trace deconfliction at the source (Bug 2).** Rather than having the
extractor guess which "Closest Plotted Point" is the encounter distance,
we renamed the traces:
- `"Psyche Closest Plotted Period Point"` — encounter distance (yellow)
- `"Psyche Closest Full Mission Point"` — full-trajectory distance (base color)
- `"Mars Closest Plotted Point"` — unchanged (not a spacecraft)

Backward compatible: extractor falls through to generic name for older HTML.

**Scale floor (testing discovery).** The adaptive resolution calculator
computes `plot_scale_au` from `dist_km * 4`. For the Phobos flyby this
gives 0.0000308 AU — a 4,600 km cube that excludes Mars (9,400 km away).
The dict's `plot_scale_au: 0.0003` is intentional: sized to include all
`select_also` objects. Fix: dict scale takes priority when present.
```python
plot_scale = enc.get('plot_scale_au') or resolution['plot_scale_au']
```

**Two encounter markers are valid.** The Go button produces both a
"Closest Plotted Period Point" (argmin of plotted trajectory) and a
Horizons-refined encounter marker (two-pass search). They agree within
13 seconds at 1-minute Horizons resolution. Both are kept — the Plotted
Period point reflects the figure data, the encounter marker reflects
Horizons' best answer. The encounter marker is labeled "(Horizons)"
when refinement succeeded.

**Center detection from hover text.** Every closest plotted point trace
contains `"{Body} radius: X km"` in its hover text. This reliably
identifies the center body without parsing the figure title (which never
worked for Orrery-generated titles). Manual override available in dialog.

**Distance convention formalized.** `dist_km` = center-to-center.
`dist_surface_km` = surface distance when body radius is known. Both
values extracted and included in generated dict. See DESIGN_encounter_export_v2.md
for the existing entries audit.

---

## Pipeline (validated May 8)

```
1. Generate plot in Orrery, save as HTML
2. Import HTML into Gallery Studio
3. Enter Orrery Preset mode (strips post-production, enables encounter export)
4. Open Export Encounter dialog
5. Verify auto-populated fields (center, date, distance pre-filled)
6. Fill manual metadata (target, label, v_kms, note, etc.)
7. Generate Python dict
8. Paste into spacecraft_encounters.py
9. Go button produces the correct encounter plot
```

Key contract: the Go button reproduces the encounter geometry from the
dict. Not identical to the original HTML (camera, annotations, animation
may differ) but the same center, scale, date window, and visible objects.

## Parameter set (validated May 8)

### Render parameters (drive Go button)

| Parameter      | Source                        | Notes                                |
|----------------|-------------------------------|--------------------------------------|
| center body    | Hover text detection + manual | `{Body} radius:` pattern in CPP text |
| select_also    | Extracted from visible traces | Deduplicated, spacecraft excluded    |
| date window    | From Orrery title dates       | Parsed from title text               |
| plot_scale_au  | From Orrery, editable in Studio | Dict value takes priority over adaptive |

### Extracted science data (from closest plotted point marker)

| Parameter       | Source                         | Notes                              |
|-----------------|--------------------------------|------------------------------------|
| encounter date  | Closest Plotted Period Point    | Format: YYYY-MM-DD HH:MM:SS       |
| dist_km         | Center-to-center distance      | From CPP hover text                |
| dist_surface_km | Surface distance if radius known | From CPP hover text              |

### Manual metadata (user enters in dialog)

| Parameter   | Widget   | Default       | Notes                          |
|-------------|----------|---------------|--------------------------------|
| target      | Entry    | (suggestion)  | Mission target, informational  |
| center      | Entry    | (pre-filled)  | From hover detection, editable |
| label       | Entry    | (empty)       | Display label (exclude spacecraft name) |
| date_source | Dropdown | 'horizons'    | horizons / authoritative / planning |
| v_kms       | Entry    | (empty)       | Manual entry for now           |
| status      | Dropdown | 'completed'   | completed / ongoing / planned / canceled |
| source      | Entry    | 'NASA/JPL'    | Data attribution               |
| note        | Text     | (empty)       | Supports paste entry           |

---

## The post-production fork problem

Studio applies two kinds of edits to a figure:

**Orrery-native** — parameters the orrery controls at generation time
(axis scale, dtick, camera, trace selection). These translate to Go
button presets. The orrery can reproduce them.

**Post-production** — transforms that exist only in Studio's export
pipeline (margins, font scaling, legend position, annotation stripping,
featured labels, hover routing, fly-to buttons, mobile briefing).
The orrery has no concept of these.

If the encounter export captures post-production values, the Go button
will generate a plot that doesn't match what Studio showed. The pipeline
breaks.

### Solution: Orrery preset mode with visible constraints

Studio's "Presets & Output Format" section gets a new option: **"Orrery"**
alongside the existing landscape and portrait presets. Switching to Orrery
mode does not change defaults — it changes *availability*. Controls that
have no orrery equivalent are grayed out. What remains active is exactly
what translates to a Go button preset.

**Active in Orrery mode (orrery-native parameters):**

| Control | Maps to |
|---------|---------|
| scene_dtick | Axis tick spacing in encounter preset |
| scene_axis_range | plot_scale_au in encounter preset |
| scene_camera | Initial camera angle |
| Trace visibility | select_also list (visible = selected) |
| show_axes / show_grid | Gray area — orrery has global setting, not per-plot |

**Grayed out in Orrery mode (post-production only):**

- Margins (top/bottom/left/right)
- Title font scale, title color
- Legend orientation, position, font scale, group title scale
- Annotation stripping, font scale, toggle button
- Featured traces, featured labels
- Mobile briefing
- Hover routing, hover mode
- Strip hidden traces, strip template
- Modebar, colorbar
- Navigation arrows, fly-to buttons
- Marker size boost, line width min
- Output format (landscape/portrait)
- 2D axis scales
- 3D handoff (KMZ link)

---

## Remaining work

### Phase B: WYSIWYG preview (next design conversation)

The design doc's centerpiece, not yet implemented. The preview would
render a temp HTML using the same path as the Go button, so the user
validates the extraction visually before generating the dict. Every
extraction error would be visible as a wrong plot, not as a wrong text
label.

Pipeline with preview:
```
Extract -> Parameter Set -> Preview (temp HTML) -> User validates ->
Generate dict + optional HTML export -> Go button produces same plot
```

Key question: how to render the preview. Options discussed but not decided:
- Launch Orrery in subprocess with proposed preset
- Import enough of plot_objects into Studio
- Generate a simplified Plotly figure directly in Studio

### Phase C: Animation support (deferred)

The Go button always calls `plot_objects` (static). Animation requires:
- Animation parameters in encounter dict schema
- Go button routing to `animate_objects` when animated
- Preview showing static limitation until animation is supported

### Minor items

- Complete Tests D-H (regression, edge cases)
- Full mission date extraction from celestial_objects.py (Edit 6b — implemented but untested)
- Backward compatibility with older HTML files (Test H)

---

## Completed: Object Encyclopedia (May 4, 2026)

The encyclopedia overlay is now orrery-native. `save_utils.py` injects
the interactive "i" button and card overlay into every HTML file the
orrery produces. Always-on, no toggle.

---

## Reference documents

| Document | Contents |
|----------|----------|
| DESIGN_encounter_export_v2.md | Problem statement, pipeline, parameter set, all six bugs diagnosed |
| MANIFEST_encounter_export_fix.md | 16 targeted edits across 4 files, ordered bottom-up |
| ENCOUNTER_EXPORT_FIX_SNIPPETS.md | Verified snippets from Opus 4.7 with 5 corrections |
| TEST_encounter_export_fix.md | 8 tests (A-H), A-C passed, D-H pending |

## Files modified (May 8, 2026)

| File | Changes |
|------|---------|
| apsidal_markers.py | trace_qualifier parameter, deconflicted labels |
| spacecraft_encounters.py | Defensive date parser, Psyche dates, scale floor, Horizons refined flag |
| palomas_orrery.py | Three callers pass trace_qualifier, plot_actual_orbits qualifier for trajectories |
| gallery_studio.py | Extraction rewrite (center, date, distance, surface), dialog pre-fill, date normalization, center field, mission date lookup |

---

## Workflow: how Tony uses this

1. Plot a mission in the orrery (select spacecraft + targets, set dates)
2. Load the HTML into Gallery Studio
3. Curate for gallery in landscape/portrait mode -> Export HTML (Fork 1)
4. Switch preset to **Orrery** — post-production controls gray out
5. Adjust active controls: dtick, axis range, camera, trace visibility
6. Click **Export Encounter...** -> modal dialog opens
   - Verify auto-extracted view parameters (left side, read-only)
   - Fill in science metadata (right side)
   - Generate Python artifact
7. Copy generated dict into `spacecraft_encounters.py`
8. Test: run orrery, click the new Go button, verify it recreates the view
9. Optionally: the Go button output can come back through Studio for
   gallery curation (the loop closes)

Steps 3 and 4-6 are independent. Same loaded figure, different output
modes, any order.

---

## Origin

Design session: May 4, 2026. Tony's question: "How can we facilitate
adding visualizations to spacecraft_encounters?" Iterated through six
rounds of conversation.

Diagnostic session: May 7-8, 2026. Three Psyche encounter exports
(Mars GA static, Mars GA animated, Phobos flyby) all produced incorrect
dicts. Six bugs diagnosed through code tracing and HTML parsing.
Five fixed with targeted snippets, validated through Go button round-trip.
Cross-AI workflow: Opus 4.6 (diagnosis + design), Opus 4.7 (snippet
verification + execution), Opus 4.6 (test review + additional fixes).

Key insights from diagnostic:
- "The preview IS the test of the extraction." (WYSIWYG principle)
- The exporter should deconflict at the source, not guess at extraction time
- Dict scale is intentional (sized for select_also objects), not a default to override
- Two encounter markers (Plotted Period + Horizons refined) are complementary, not redundant

---

*Handoff v4.0 — May 8, 2026*
*Design + build: Tony Quintanilla + Anthropic's Claude Opus 4.6 / 4.7*
