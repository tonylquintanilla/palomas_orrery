# Handoff: Item 19.3 Phase B -- Studio read-on-load round trip (gallery)

Paloma's Orrery | Tony Quintanilla, PE + Claude | June 16, 2026

Built on:  gallery HEAD 2f40d9d58f8ff784ceb4eff0c870775ff5027fdc (branch main)
Orrery:    HEAD c28eec0422a0b32bf794b92162c183e67f12b723 (read-only ref; unchanged this phase)
SHA chain: gallery 2f40d9d (base) -> 6804b39 (Phase B read-on-load)
                                   -> 812c05f (toggle-default follow-on, current HEAD)
           All three verified by remote round trip + byte diff. Orrery untouched.
Design authority: documentation/3d_axis_control_handoff.md (D1) +
                  HANDOFF_item19_3_phaseA_dtick_gui.md (D1-D5)
Apply:     item19_3_phaseB_studio_readonload.patch (git apply, verified clean @2f40d9d)
           -- Phase B only. The toggle follow-on (sec 8) is 3 value flips, applied
           directly by Tony, NOT in this patch.

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

Mode-5 render gate (Tony) -- RESULT @6804b39: 1-5 + 7 PASS, 6 deferred.
  1. [PASS] Raw CLOSE-APPROACH (Apophis / Artemis flyby): Axis range + Grid
     spacing boxes fill with real numbers (not 0); titles carry km.
  2. [PASS] Raw SYSTEM / EXOPLANET (Proxima / TRAPPIST): boxes fill, titles
     stay plain "X (AU)" -- the D1 fix, the behavior that actually changed,
     confirmed by eye.
  3. [PASS] Change Grid spacing, re-render: grid refines; km updates on a
     close-up, stays plain on a wide plot.
  4. [PASS] Export refined plot, reload: values hold, no drift.
  5. [PASS] Studio export with explicit grid override: override wins (D3).
  6. [DEFERRED] 2D plot loads fine, grid boxes stay 0. (low-risk sanity)
  7. [PASS] Bonus: encounter "View Parameters (auto-extracted)" panel shows
     the real scene_dtick from the figure instead of "auto".

  OBSERVATION from the gate (-> resolved in sec 8): on raw-orrery load the
  show_axes / show_grid / show_modebar checkboxes came up unchecked
  (DEFAULT_CONFIG defaulted False) instead of reflecting the orrery output.

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

  - (June 16, item 19.3 Phase B follow-on, from the render-gate observation)
    DEFAULT_CONFIG show_axes / show_grid / show_modebar flipped False -> True
    (gallery tools/gallery_studio.py, landscape editorial baseline), pushed at
    812c05f. Tony's call: the boxes should reflect what the orrery HTML
    produces on load AND these defaults should display across the other modes
    ("I always turn them on"), so the global default was flipped rather than a
    surgical raw-branch-only set. Blast radius = every path that seeds from
    DEFAULT_CONFIG (app startup, Reset Defaults, landscape preset, orrery-mode
    entry, raw-orrery load) now starts with axes/grid/modebar on. Studio
    exports UNAFFECTED -- they carry their own saved toggle states in
    _studio_config, which override the default on load. show_modebar=True is
    safe vs non-Plotly input: Studio only ingests Plotly figures (others bounce
    at load), and show_modebar is only the exported HTML's Plotly
    displayModeBar flag -- never touches a tkinter window.

--------------------------------------------------------------------------
## 7. SHA carry

Phase B built on gallery 2f40d9d (orrery c28eec0, untouched). Pushed at
6804b39 (Phase B, byte-verified identical to the patch), then 812c05f
(toggle-default follow-on, sec 8). Current gallery HEAD = 812c05f. Orrery
side NOT touched -- only tools/gallery_studio.py changed in both pushes.
Next session: re-pin HEAD at 812c05f and round-trip-check before any build.

Module updated: June 2026 with Anthropic's Claude Opus 4.8 (item 19.3
Phase B: Studio read-on-load round trip).

--------------------------------------------------------------------------
## 8. Follow-on: toggle defaults flipped on (812c05f)

Surfaced by the Phase-B render gate (sec 5): on raw-orrery load the
show_axes / show_grid / show_modebar checkboxes came up unchecked because
DEFAULT_CONFIG defaulted them False, so the GUI did not reflect what the
orrery HTML actually produces. Pre-existing (that branch always applied the
False defaults); the gate put eyes on it.

Change (Tony, applied directly -- 3 value flips, NOT in the Phase-B patch):
  DEFAULT_CONFIG  "show_axes": False -> True
                  "show_grid": False -> True
                  "show_modebar": False -> True

Decision rationale: chose the GLOBAL default flip over the surgical
raw-branch-only set, because these defaults should display across the other
modes too, not just on raw load ("I always turn them on"). Consequence,
recorded so it is not a surprise later: every path seeded from
DEFAULT_CONFIG now starts with axes/grid/modebar on -- app startup, Reset
Defaults, landscape preset, orrery-mode entry, raw-orrery load. Studio
exports are UNAFFECTED (their saved _studio_config toggle states override the
default on load), so finished gallery files do not get forced on.

modebar safety (the "what if the plot isn't Plotly" question): no failure
mode. Studio only ingests Plotly figures -- a non-Plotly file fails at load
with a dialog and never reaches config. show_modebar is consumed in exactly
one place, the exported HTML's Plotly config (displayModeBar), a browser
toolbar flag; it never touches a tkinter window. A 2D Plotly plot with
modebar on just shows the 2D toolbar.

Verification @812c05f: remote round trip OK; byte diff vs Phase-B state =
exactly the 3 value flips, nothing else; py_compile PASS; ASCII/LF clean;
6,056 lines.

Render gate for the follow-on (Tony, quick confirm):
  - Load a raw orrery plot -> the three boxes now come up CHECKED, matching
    the orrery output.
  - Load a finished Studio gallery export -> its saved toggle states still
    win (NOT forced on by the new default).
  - Reset Defaults / fresh start now begin with the three on (expected).
