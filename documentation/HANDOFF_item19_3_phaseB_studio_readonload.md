# Handoff: Item 19.3 Phase B -- Studio read-on-load round trip (gallery)

Paloma's Orrery | Tony Quintanilla, PE + Claude | June 16, 2026

Built on:  gallery HEAD 2f40d9d58f8ff784ceb4eff0c870775ff5027fdc (branch main)
Orrery:    HEAD c28eec0422a0b32bf794b92162c183e67f12b723 (read-only ref; unchanged this phase)
Pushed at: gallery HEAD __________ (fill after commit + push, then re-pin)
Design authority: documentation/3d_axis_control_handoff.md (D1) +
                  HANDOFF_item19_3_phaseA_dtick_gui.md (D1-D5)
Apply:     item19_3_phaseB_studio_readonload.patch (git apply, verified clean @2f40d9d)

--------------------------------------------------------------------------
## 1. What shipped (Phase B)

Closes the item-19.3 round trip on the STUDIO side. Before: loading a raw
orrery plot reset the two 3D grid boxes (scene_axis_range / scene_dtick) to 0
("auto"), so the orrery's baked grid was invisible and uneditable -- the data
round-tripped, the display did not. After: those boxes POPULATE from the
figure on load, and the km-equivalent axis-title suffix is gated to
close-approach scale only.

One file, tools/gallery_studio.py, six edit groups, +84/-15 lines.

--------------------------------------------------------------------------
## 2. The one reconciliation (handoff D1 vs the live bytes)

The Phase-A handoff's D1 described the km-suffix gate as "range half-extent <
KM_SUFFIX_MAX_AU = 0.01, binary km/plain." The LIVE apply_config gated the
suffix on EFFECTIVE_DTICK in three tiers (<0.01 exact km, <0.1 "M km", else
none) -- a different quantity. They diverge on exactly the cases D1 calls
"neutral": Proxima half-extent ~0.058 -> auto dtick ~0.02 -> the live code
printed "(grid: 2.99M km)", but D1 wants Proxima plain. So D1 was a re-key,
not a guard, and the handoff's build-shape note ("guard around the suffix
line") was in mild tension with its own prose.

Resolved with Tony as OPTION B (June 16): gate suffix EMISSION on the
half-extent (< KM_SUFFIX_MAX_AU when a range is present; fall back to the
dtick key when the range is auto/0, so a pure fine-dtick override still
annotates), and KEEP the existing exact-km vs "M km" tiers inside. This
reconciles D1's prose (half-extent gate) with its build-shape note (guard the
existing line) AND preserves the "M km" formatting for the one real corner it
still serves (a coarse user dtick on a small range). The "M km" tier is
otherwise unreachable under a 0.01 half-extent gate -- kept, not relied on.

--------------------------------------------------------------------------
## 3. Verified map (live @2f40d9d; new line numbers shift after apply)

  KM_SUFFIX_MAX_AU = 0.01           module constant, before DEFAULT_CONFIG (~54)
  _read_scene_grid_from_figure()    new module-level shared reader, before
                                    apply_config (~827)
  apply_config suffix gate          Option-B emit gate (~967-980)
  _do_load studio branch            D3 fallback to figure when studio cfg = 0
  _do_load raw-orrery else branch   read figure grid into source_cfg
  _extract_encounter_data           routed through the shared reader; now also
                                    surfaces the figure dtick (panel stops
                                    showing "auto" for a dtick-bearing figure)

Handoff corrections found at pull (do not trust cold next time):
  - real path is tools/gallery_studio.py, not gallery/tools/.
  - THREE config dicts carry the keys (54-ish, 169-170, 299-300), not two.
  - the raw-orrery load path is the ELSE branch of _do_load, ~5808.

--------------------------------------------------------------------------
## 4. Decisions as implemented (D1-D5, Phase-A handoff sec 5)

  D1  km-suffix gate: OPTION B (see sec 2). KM_SUFFIX_MAX_AU = 0.01, named.
  D2  populate fields with the figure's REAL value (idempotent re-apply). DONE.
  D3  precedence: explicit non-zero _studio_config wins; else read the figure.
      Studio branch fills only fields the studio cfg left at 0; raw-orrery
      branch always reads the figure. DONE.
  D4  edges: no explicit dtick -> field stays 0 (auto/inherit); 2D (no scene)
      -> reader returns (0,0), fields stay 0. DONE (smoke R3/R4).
  D5  read BOTH range and dtick. DONE (reader returns the pair).

--------------------------------------------------------------------------
## 5. Verification

Claude-side gate (sandbox clone @2f40d9d + tkinter installed):
  - py_compile PASS on the edited file.
  - ASCII-only (0 non-ASCII) + LF; patch itself ASCII/LF, applies clean
    (git apply --check) against a fresh 2f40d9d tree.
  - LIVE smoke against the REAL module functions (not copies) -- 13/13 PASS:
      Reader R1-R6: range+dtick, range-only, dtick-only, 2D, asymmetric
        (max |bound|), garbage-bounds-ignored.
      Suffix S1-S7: Apophis -> exact km; Proxima 0.058 -> NEUTRAL "X (AU)";
        TRAPPIST 0.075 -> NEUTRAL; Earth 1.3 -> NEUTRAL; range-auto + fine
        dtick -> emit (fallback); small-range + coarse dtick -> "M km" kept;
        no override -> no suffix.
    apply_config used its in-file _calculate_grid_dtick fallback (no
    visualization_utils in the gallery tree) -- the live path in Studio.

  NOT live-smoked (honest scope): the _do_load WIRING (D3 glue) is a GUI
  method needing a full Tk App + a real HTML file; verified by py_compile +
  read-back only. The logic it calls (the shared reader) IS live-verified.
  Its true ground truth is Tony's render gate below.

Mode-5 render gate (Tony) -- the round trip, in plain terms:
  1. Load a raw orrery CLOSE-APPROACH export (Apophis / an Artemis flyby):
     the Axis range + Grid spacing boxes fill with real numbers (not 0), and
     axis titles read like "X (AU) (grid: 38,000 km)".
  2. Load a raw SYSTEM or EXOPLANET export (normal solar-system, or
     Proxima / TRAPPIST): boxes fill (range is a larger AU number), titles
     stay plain "X (AU)" -- no km clutter.  <-- the D1 fix.
  3. Change Grid spacing, re-render: grid refines; km label updates on a
     close-up, stays plain on a wide plot.
  4. Export the refined plot, reload it: boxes still show the values, no
     drift; close-up still annotated, wide still plain.
  5. Load a STUDIO export that had an explicit grid override: the override
     shows (it wins over the figure's baked value -- D3).
  6. Sanity: a 2D plot loads fine, grid boxes stay 0.
  7. Bonus: the encounter "View Parameters (auto-extracted)" panel now shows
     the real scene_dtick from the figure instead of "auto".

--------------------------------------------------------------------------
## 6. Ledger entry (append under item 19, Bucket A; do not regenerate)

  - (June 16, item 19.3 Phase B SHIPPED) Studio read-on-load round trip,
    gallery tools/gallery_studio.py, built on 2f40d9d / orrery c28eec0.
    New shared reader _read_scene_grid_from_figure; both _do_load branches
    populate scene_axis_range/scene_dtick from the figure (D3 precedence:
    explicit studio override wins, else figure); _extract_encounter_data
    routed through the same reader (+ figure dtick now surfaced in the
    read-only panel). D1 RECONCILED to the live bytes: the handoff's
    half-extent gate did not match the live dtick-keyed suffix; OPTION B
    chosen (KM_SUFFIX_MAX_AU = 0.01 emit gate on half-extent, dtick tiers
    kept inside, range-auto fallback). Closes the item-19.3 round trip
    (orrery bakes -> Studio reads + refines). Render-gate items in handoff
    sec 5. Optional later: orrery also emitting the suffix under the same
    cutoff (full title parity) -- NOT this item.

--------------------------------------------------------------------------
## 7. SHA carry

Built on gallery 2f40d9d (orrery c28eec0, unchanged this phase). After commit
+ push, record the new gallery HEAD here and re-pin before any follow-on. The
orrery side was NOT touched; only tools/gallery_studio.py changed.

Module updated: June 2026 with Anthropic's Claude Opus 4.8 (item 19.3
Phase B: Studio read-on-load round trip).
