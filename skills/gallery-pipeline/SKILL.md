---
name: gallery-pipeline
description: Web gallery pipeline for the Paloma's Orrery project (palomasorrery.com). Use for any task touching gallery_studio.py, json_converter.py, gallery_editor.py, gallery_json_fixer.py, the index.html gallery viewer, gallery_metadata.json, gallery_config.json, the tonyquintanilla.github.io repo, or GitHub Pages deployment. Use when curating or exporting plots through Gallery Studio, converting HTML to gallery JSON, editing gallery cards or categories, working with _studio_config / _studio / _encyclopedia / _kmz_handoff / _original_text keys, studio presets, mobile or portrait rendering, or the WYSIWYG preview. Do not use for projects other than Paloma's Orrery.
---

# Gallery Pipeline

Skill version: 1.0 | Cut from tonyquintanilla.github.io @ 89c8bf30 (code)
and palomas_orrery @ b29ad3f8 (context) | July 1, 2026
Sources: gallery_studio.py, json_converter.py, index.html at HEAD;
web_gallery_handoff.md (30+ sessions).

## Two-Repo Coupling (load-bearing)

The pipeline code lives in the GALLERY repo, not the orrery repo:
tonyquintanilla.github.io/tools/ holds gallery_studio.py,
json_converter.py, gallery_editor.py, gallery_json_fixer.py;
index.html at the repo root IS the homepage and the viewer;
gallery/ holds the JSON files, gallery_metadata.json, gallery_config.json,
and assets/ (KMZs). The orrery repo produces the raw Plotly HTML exports
the pipeline consumes. Fixes routinely need BOTH repos checked (the
parallel-pipelines gate): the same bug appears independently in Studio and
the viewer. SHA-pin each repo separately in handoffs.

## The Chain

Desktop app (Python/Plotly) -> save_plot() HTML export (Standard, not
Offline) -> Gallery Studio (ALL curation decisions) -> json_converter.py
(HTML -> JSON extraction, no transforms) -> gallery/*.json +
gallery_metadata.json -> GitHub Pages -> index.html viewer (dumb renderer).

PNG cannot feed the pipeline: the converter needs HTML with an embedded
Plotly.newPlot() call. Extraction is by BRACKET-MATCHING (count brackets,
respect strings/escapes) -- regex fails on write_html whitespace padding.

## WYSIWYG Authority (the core principle)

Studio makes all content decisions; the viewer applies NO content
overrides ("the viewer should not pre-empt or supersede Studio -- where
decisions can be made by Studio, the viewer should be silent or
neutral"). Hidden viewer transforms create a developer-user gap: the last
visual checkpoint before pushing must match what the public sees.
Consequences:
- The viewer checks Studio flags (e.g. _hover_mode) and stays silent when
  Studio did not set them.
- Studio Preview renders THROUGH the real viewer: build_gallery_html ->
  the REAL json_converter extractor -> gallery/_studio_preview.json ->
  index.html served over localhost with ?preview=<file>. No second
  renderer, so WYSIWYG holds by construction. The GE button 404s for an
  un-pushed KMZ -- by design, as a push-status check.

## Flag Contracts and Key Preservation

- _studio means "trust this, don't override." Strip stale flags
  UNCONDITIONALLY before guards -- a guard of the form
  `if list: strip` lets stale data survive an empty list.
- _studio_config is the Studio settings overlay; SOURCE files carry
  figure-native values, EXPORTS carry the _studio_config overlay. The
  round trip (Phase B): Studio reads config on load via a shared reader
  in both _do_load branches; a Studio override wins on reload.
- _encyclopedia must be in the converter's preserve list -- it drives the
  viewer's "i" card. Encyclopedia matching is EXACT by trace name (no
  fuzzy match); fix mismatches by adding an alias key in constants_new.py
  (orrery repo), not in Studio.
- _original_text is the non-destructive hover-routing stash; the
  converter STRIPS it from traces before writing JSON.
- _kmz_handoff drives the viewer's green Google Earth button; _link_data
  drives the link-icon dropdown. Both are VIEWER CHROME, not figure
  annotations.
- Two variants exist per teaser: raw *_teaser.json (generator output, no
  _kmz_handoff) and *_teaser_gallery.json (Studio export, has it). Only
  _gallery/_desktop variants are served; raw files are cull candidates
  (L-074).

## Configuration and Metadata

- gallery_config.json is the SINGLE SOURCE OF TRUTH for categories; all
  consumers (converter, editor, viewer) read it, with hardcoded fallbacks
  for robustness. Renaming a category updates both key and label on all
  affected vizs plus the config entry.
- gallery_metadata.json is the visualization index; non-contiguous
  category blocks are normalized by the editor (extract, regroup,
  reinsert).
- Theme signal: the converter promotes paper_bgcolor / plot_bgcolor from
  the template to top-level layout BEFORE stripping templates (both the
  viewer and local preview strip templates on load). Light-themed plots
  skip all dark overrides.
- Minimal-override principle for the viewer: transparent backgrounds +
  light font for dark theme only; everything else is Studio's job.

## Deployment

GitHub Pages via GitHub Desktop pushes. If a deploy fails with a
"multiple artifacts" error, do NOT re-run the failed workflow -- push a
new commit (the handoff update is a natural second push). KMZ-only
updates: replace the file in gallery/assets/ and push; the card links by
stable filename.

## Mobile and Rendering Facts

- 768px separates phones from tablets; below it, force portrait and hide
  the Desktop/Mobile toggle.
- 100dvh over 100vh for iOS Safari bottom-toolbar clipping (declare vh
  first as fallback); viewport-fit=cover activates
  env(safe-area-inset-bottom).
- Hide the Plotly modebar on mobile; zoom buttons + pinch + tap cover it.
- 2D zoom = axis range relayout; 3D zoom = synthetic WheelEvent to the
  WebGL canvas (gl-plot3d's camera object is read-only; relayout of
  scene.camera.eye clips in orthographic projection). 3D zoom RESET is
  not possible (projection matrix below API level) -- orientation and pan
  reset work.
- Make annotation boxes transparent on mobile (strip bgcolor/border),
  keep the text -- generic, content-safe.
- Polar/radial charts are landscape-only; curate with mode tagging, not
  code.
- Nav arrows are landscape-only by design (portrait is touch-first).
- iOS home-screen bookmarks cache separately from Safari; delete and
  re-add for persistent staleness.

## SENSITIVE CONTENT (core rule; full treatment in earth-system-pipeline)

Gallery cards, briefings, and encyclopedia text for human-cost scenarios
(food insecurity, heat deaths, displacement) follow the restraint
discipline even when the session never touches the KMZ side: transcribe,
don't sum; the source's voice only, causation deferred to the reader;
state the basis -- do not hand the lay reader a connection we will not
draw ourselves. Load earth-system-pipeline before writing or editing any
such text.

## Shared Conventions (duplicated deliberately; masters elsewhere)

- Credit line on substantive edits (master: orrery-coding-conventions).
- ASCII/LF for Python deliverables (master: safe-file-editing).
- Distance hover text includes AU alongside km (master:
  orrery-coding-conventions); Studio's km-suffix title gate keeps
  exact-km / M-km tiers inside the gate with a range-auto fallback.

## Field Notes

- JS: JSON.stringify(undefined).substring() crashes; guard with || ''.
- position: fixed escapes CSS containment; position: absolute stays
  inside the parent.
- Plotly.js native touch works on mobile without custom code.
- D-pad pan arrows: 2D uses Plotly.relayout on axis ranges; 3D shifts
  camera eye/center.
- DEFAULT_CONFIG changes have wide blast radius: every path seeded from
  it (startup, Reset Defaults, presets, raw load) -- Studio exports are
  unaffected because saved _studio_config states override defaults.
- Presets must preserve scenario-specific settings (KMZ link, custom
  title) -- presets set general layout only.
- Animated plots: strip_hidden_traces requires frame trace-index
  remapping, or stripped portrait exports animate the wrong traces.
- social_media_export.py is mostly superseded by Studio; its
  _parse_hover_html() survives as a shared utility.
