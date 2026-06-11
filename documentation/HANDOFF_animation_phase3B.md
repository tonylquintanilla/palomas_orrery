# HANDOFF -- Animation Refactor 21/51, Phase 3 Session B (June 11, 2026)

Built on: orrery repo HEAD a9f0ec4e5fdb8869c39b77fabec38ae9c6efc925 (verified;
matches the SHA Tony supplied; Session-A files at this base byte-confirmed).
Deliverables: palomas_orrery.py + shell_configs.py (the engine),
ANIMATION_TEST_PROTOCOL_v3.md, two diff files vs HEAD.

Session B scope per ANIMATION_ENGINE_DESIGN_v1.md sec 10: engine + first
customers (rotation axis, dipole cone, sun-direction indicator) + protocol
v3. DELIVERED, render-gated on protocol v3. The Finding-2 legend upgrade
shipped WITH the engine (it was small once the mechanism was verified).

## Answer to the Finding-2 question (verified live, not recalled)

**Yes -- `visible='legendonly'` is exactly the mechanism, and it works.**
Verified in-container: a dataless trace (`x=[None]`) with
`visible='legendonly'`, an italic parenthetical in the name
(`<i>(static plots only)</i>` -- Plotly legend text accepts the basic HTML
subset), `legendrank=9999` to sink the block to the legend bottom, and
`hoverinfo='skip'` serializes cleanly at ~230 bytes per entry. Plotly draws
legendonly entries in the muted toggled-off style -- the greyed look for
free. Constraints found:
1. **Click wart:** clicking a greyed entry flips it to visible=True --
   nothing renders (no data), but the entry text UN-MUTES until clicked
   again. Cosmetic; judge in B4.
2. **Grouping:** placeholders deliberately get NO legendgroup -- sharing a
   group with real traces would couple their mute-state to group clicks.
   legendrank does the visual separation instead.
3. Legendgroup toggles for real traces are untouched (placeholders are
   group-free); names are arbitrary strings, so the parenthetical is safe.

Implemented as `add_static_only_legend_placeholders()`: one muted entry per
CHECKED shell of every body the animate path will not render (non-center
bodies' shells + offset-Sun shells). Console notices kept as developer
diagnostics, per the Finding-2 decision. The design-doc paper footnote is
SUPERSEDED and will not be built.

## What changed

shell_configs.py (13 one-line insertions, transactional with count asserts):
`'per_frame': True` tags on all 11 rotation_axis entries + 2 dipole_cone
entries. Inert metadata for the static path; the engine's registry.

palomas_orrery.py (6 hunks; file 10,062 -> 10,239 lines):
- ENGINE CORE (after the Phase-2 helpers): `collect_perframe_elements`
  (eligibility: non-center + shells-checked trigger + per_frame tag, plus
  the indicator builtin -- suppression handled at allocation per design rule
  2(b)); `build_perframe_traces` (the ONE rebuild mechanism --
  builder(**frame_context), no translate path); `allocate_perframe_elements`
  (frame-1 allocation, index registry, live byte budget print + 150 KB/frame
  soft-warn guardrail); `add_static_only_legend_placeholders`.
- ANIMATE WIRING: allocation runs after orbit paths, just before the Phase-1
  fence; the fence's dynamic set is the union of trace_indices and engine
  group indices (the Phase-1 sparse mapping needed NO change -- it was
  designed for arbitrary sets). Frame loop: each group rebuilds at this
  frame's body/Sun position; missing position -> group invisible that frame;
  **trace-count stability asserted LOUD** with a message naming the
  body/element/frame. Frozen-Sun fallback: if the Sun was not fetched,
  sun-direction elements hold the frame-1 Sun position (one console NOTE).
- Greyed-legend call after the O2/O3 notices.

## Verification done (Claude-side)

- py_compile clean (both files); ASCII-only; LF; diffs confined (6 + 13
  hunks); verification greps run STANDALONE (the Session-A grep -c lesson,
  applied).
- LIVE end-to-end engine tests in the real module namespace under xvfb
  (real builders + real tk vars; synthetic 5-frame trajectories standing in
  for Horizons):
  T1 eligibility: Uranus with one shell checked -> exactly axis + cone +
     indicator; Earth (no shells checked) excluded; center excluded.
  T2 allocation: 16 traces, 3 groups, indices contiguous and recorded;
     budget line printed: "~29.4 KB/frame" (matches the Session-A harness
     within rounding).
  T3 rebuild at frame 3: counts stable; geometry MOVES with the body.
  T4 a deliberately count-unstable builder is detected (the frame-loop
     assert would trip loud).
  T5 placeholders: one per checked shell, legendonly + rank + italic note,
     real names ("Sun: Gravitational", "Earth: Magnetosphere",
     "Uranus: Core").
- NOT verifiable in-container: full animation with Horizons, the greyed
  RENDER appearance, and the riding primitives' visual quality -- protocol
  v3, B1-B6 + O10-O13.

## Ledger-ready updates

- 21/51 Phase 3: Session B DELIVERED `[render-gated on protocol v3]`.
  Engine live with first customers; budget guardrail in console;
  Finding-2 greyed-legend disclosure SHIPPED (supersedes the design-doc
  footnote -- amend ANIMATION_ENGINE_DESIGN_v1.md sec 8 on next touch).
  Phase-1 fence/mapping unchanged (extension only); Phase-2 helpers
  unchanged.
- Finding 1 (scaling): UNCHANGED this session, by design (Decision 3) --
  the concrete cases (photosphere collapse, indicator truncation) are
  Session-C consolidated-auto-scale inputs; O12 collects any new ones the
  riding primitives expose.
- Finding 3 (Sun axis needs a checkbox): the engine deliberately uses the
  SAME shells-checked trigger for all bodies including the Sun -- uniform
  with the center dispatch; the center-side Sun asymmetry remains
  pre-existing behavior, noted, untouched.
- D.Cosmetic candidate from T5: placeholder display names derive
  mechanically from checkbox keys; O11 flags any that read wrong.
- Session C scope (unchanged): comet-tail trace-returning core + opt-in
  mode, sodium tail, per-element hover disclosure sweep, consolidated
  auto-scale (with Finding-1 cases as test fixtures).

## Session B Test Results (June 11, 2026 -- Tony, Mode 5)

Tested at HEAD e5fd86df57e279dc5f59576ea668848d95e1efc1. Engine and
greyed legend verified on Windows, Python 3.13.

### B1 -- Uranus headline
- PARTIAL PASS. Console reports 3 element groups, ~27.1 KB/frame (correct).
  Greyed "Uranus: Magnetosphere (static plots only)" in legend (correct).
  No assert errors. HOWEVER: at solar system scale the riding primitives
  are subpixel on Uranus -- visual verification of per-frame movement is
  impossible. Fly To only shows frame 1 position, cannot track across
  frames. The engine appears to work (console confirms allocation and
  rebuild) but Mode-5 visual confirmation of the riding behavior requires
  tooling that doesn't exist yet. LEDGER ITEM.

### B2 -- Earth non-center
- SAME as B1. Engine allocates and rebuilds, greyed legend correct, but
  riding primitives not visually verifiable at solar system scale.

### B3 -- Sun as non-center
- PASS. Sun's rotation axis rides the moving Sun marker in Earth-centered
  view. Sun direction indicator correctly suppressed. Sun shells greyed
  in legend. Center body's Sun Direction indicator stays frozen at frame 1
  (known Phase 1 behavior, not a regression).

### B3 bonus -- Earth-Moon Barycenter centered
- FINDING: Earth's Sun Direction indicator points at the Moon (not the
  Sun) and tracks the Moon's orbit as it moves. This is a physics bug:
  when the Sun checkbox is off, the engine falls back to the frame-1 Sun
  position which defaults to (0,0,0) -- the barycenter. The indicator
  points from Earth toward (0,0,0), which visually aligns with the Moon's
  direction since Earth and Moon are on opposite sides of the barycenter.
  FIX NEEDED: when Sun is not in positions_over_time, the engine should
  fetch the Sun's actual position rather than using (0,0,0). Session C
  scope.
- Earth's rotation axis stays in correct relative position as Earth orbits
  the barycenter. Earth's and Moon's sphere shells greyed at legend bottom.

### B4 -- Legend disclosure
- PASS. Greyed entries at legend bottom, muted style, italic note. Click
  wart (un-mutes text, nothing renders) ACCEPTABLE -- meaning is clear.

### B5 -- Payload measurement
- DEFERRED. Measurement tool needs a file browser dialog (like Gallery
  Studio) for convenience -- the HTML files are saved in a separate folder.
  LEDGER ITEM: upgrade measure_animation_html.py with tkinter file browser.

### B6 -- Regression
- PASS. Animated inner planets, no shells: no engine console line, no
  greyed entries. Static plot with shells: shell_configs per_frame tags
  are inert. No overhead when unused.

### Observation Log v3 (O10-O13)

O10 -- Riding primitives read okay where visible. At planetary scale
(Earth-centered) the axis and indicators are discernible and educational.
At solar system scale (Sun-centered outer planets) they are subpixel.

O11 -- Greyed legend naming quality: good. Names derive correctly from
checkbox keys.

O12 -- Scaling: Sun Direction indicator clipping by cube range (previously
noted). Sun orbit around Earth center lacks buffer (previously noted).

O13 -- Additional findings:
(a) Console spam: "Sun direction indicator: Using shell radius..." prints
    29 times (once per frame rebuild). Should be suppressed after first
    print or gated behind a verbose flag. Session C scope.
(b) Fly To zoom limit does not reach shell-discernible distance for
    planets. Computed from orbital distance or marker size, not shell
    extent. Comets are okay (tail geometry is large enough). Planets
    stop too far away to see magnetosphere, radiation belts, etc. Fly To
    distance should consider shell extent when shells are checked.
    LEDGER ITEM: part of scaling/cube/grid comprehensive review.
(c) No camera-tracking-across-frames capability exists. Fly To shows
    frame 1 only. To visually verify per-frame engine at outer-planet
    scales, either camera tracking or directional-arrow camera control
    (available in Gallery Studio 2D but not Plotly 3D) would be needed.
    LEDGER ITEM.

### Session B Disposition

Session B CONDITIONALLY RENDER-CONFIRMED. Engine allocates, rebuilds,
and budget-reports correctly. Greyed legend disclosure works and is
accepted. No regressions. Riding behavior visually confirmed at
planet-centered scale (B3) but not at solar-system scale (B1/B2) due
to tooling gap. The engine is architecturally sound; the visual
verification gap is a tooling issue, not an engine issue.

Barycenter Sun-Direction bug (B3 bonus) is a real physics error requiring
a fix in Session C (fetch Sun position when Sun checkbox is off).

### New Ledger Items

- Fly To zoom limit: should consider shell extent, not just orbital
  distance. Part of scaling/cube/grid review (O6c).
- Camera tracking across animation frames: no mechanism exists. Needed
  for visual verification at outer-planet scales.
- measure_animation_html.py: add tkinter file browser dialog.
- Console spam: Sun direction indicator message per frame. Suppress
  after first or gate behind verbose flag.
- Barycenter Sun-Direction indicator bug: points at barycenter (0,0,0)
  instead of Sun when Sun checkbox off. Session C fix.

Module updated: June 2026 with Anthropic's Claude Fable 5 + Claude Sonnet 4.6
