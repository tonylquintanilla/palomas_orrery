# HANDOFF -- Ledger Cleanup + Next-Session Scoping
# Tony Quintanilla, PE | Claude Opus 4.6 | June 18, 2026
# Base SHA: feab717 -> Final SHA: 7a870ff

---

## What was done this session

### C) Dead import removal (L-015 partial, L-018 closed)
Three confirmed-dead imports removed from palomas_orrery_helpers.py via
binary-mode patch (CRLF-preserving):
- `create_planet_visualization` (from planet_visualization, line 55)
- `hover_text_sun` (from solar_visualization_shells, line 160)
- `create_sun_direction_indicator` (from shared_utilities, line 52)

All three: grep-confirmed zero callers. 916 -> 913 lines.

L-018 -> DONE, migrated to section C.
L-015 narrowed: ~78 dead _info imports remain (broader sweep deferred).

### A) D.Structural detail blocks fleshed out
All 15 [per chain] stubs replaced with code-investigated Gap statements,
type classifications, and scope assessments. Key finding: 9 of 16 items
were either already done, visual-verification-only, or miscategorized.

### B) Recategorization
- L-014 (asteroid-belt migration) -> D.Feature-C (design decision)
- L-017 (globals() rewiring) -> D.Feature-C (refactor, design-before-code)
- L-022 (asteroid belt single-info-marker) -> C (already done, May 27-29 sweep)
- L-024 (Planet 9 sphere n=50) -> C (current value 20-24, resolved)
- L-029 (v25 D3 dead-code annotations) -> C (zero matches in codebase)
- L-019, L-021, L-023 (Neptune/Saturn/Uranus ring markers) -> C (Tony verified)

D.Structural: 16 items -> 7 remaining. Total live items: 58 -> 46.

### Two items still open for quick closure
- L-025: confirming grep (inline markers custom-geometry-only). Likely done.
- L-020: CUSTOM_SHELLS tooltip scan. Scriptable.

### RICE scoring added to ledger_index.py
Adapted RICE framework (Reach/Impact/Confidence/Effort) added to the INDEX
generator. Metadata field: `rice:R/I/C/E` (separator `/` for decimal values).
Score = R x I x (C/100) / E. Scored items sort to top of their section
(descending); unscored show `--`. Full backward compatibility with existing
metadata. RICE documentation added to LEDGER_CONSOLIDATED.md in the "Using
and maintaining this ledger" section. Tony placed placeholder scores
(rice:2/2/50/2 -> 1.0) on all items as a starting point for deliberate
scoring.

### Dashboard launcher pinned to Windows taskbar
`_run_dashboard.bat` pinned via `explorer.exe` wrapper shortcut (Windows 11
blocks direct .bat pinning; `explorer.exe "path\to\file.bat"` shortcut
bypasses the restriction).

---

## Next-session scoping

### 1. Dipole cones: Mercury, Earth, Jupiter, Saturn
**Ledger:** L-009 (dipole cluster), L-006 (Mercury offset)

#### Sourced data (Gemini, de-novo, June 18 2026)

| Body    | Tilt (deg) | Offset (R_p) | Direction      | Source                                          |
|---------|-----------|---------------|----------------|-------------------------------------------------|
| Mercury |    0      | 0.19 +/- 0.01 | Northward (axial) | Anderson et al. 2011, MESSENGER (Science 333, 1859) |
| Earth   |   ~9.6    | ~0.085        | Complex (secular variation) | Alken et al. 2021, IGRF-13 (Earth Planets Space 73, 49) |
| Jupiter |   10.31   | 0.12          | N. hemisphere  | Connerney et al. 2022, JRM33 (JGR Planets 127)  |
| Saturn  |    0      | 0.04-0.05     | Northward (axial) | Dougherty et al. 2018, Cassini Grand Finale (Science 362) |

PROVENANCE GATE (L-009) SATISFIED: all tilts now sourced from peer-reviewed
mission data. The recalled values are retired; these are the cited replacements.

#### Current architecture
- `PLANET_DIPOLE` dict in planet_visualization_utilities.py (L665):
  `{'tilt_deg': float, 'azimuth_deg': float, 'source': str}`
- Builder: `build_dipole_cone_traces()` (L675) reads PLANET_DIPOLE + PLANET_ROTATION.
- Uranus (60 deg) and Neptune (47 deg) are done and working.
- All four target bodies already have PLANET_ROTATION entries (sense, half_len_frac).
- All four already have CUSTOM_SHELLS entries (magnetosphere, etc.) -- dipole_cone
  is a sibling entry, same pattern as Uranus/Neptune.
- Builder docstring (L692): "the dipole center offset is DEFERRED (magnitude
  sourced, direction not)."

#### Draft PLANET_DIPOLE entries (for review)
```python
PLANET_DIPOLE = {
    'Mercury': {'tilt_deg': 0.0, 'azimuth_deg': 0.0,
                'offset_fraction': 0.19,   # NEW FIELD
                'source': 'Anderson et al. 2011, MESSENGER (Science 333, 1859)'},
    'Earth':   {'tilt_deg': 9.6, 'azimuth_deg': 0.0,
                'offset_fraction': 0.085,  # NEW FIELD
                'source': 'Alken et al. 2021, IGRF-13 (Earth Planets Space 73, 49)'},
    'Jupiter': {'tilt_deg': 10.31, 'azimuth_deg': 0.0,
                'offset_fraction': 0.12,   # NEW FIELD
                'source': 'Connerney et al. 2022, JRM33 (JGR Planets 127(2))'},
    'Saturn':  {'tilt_deg': 0.0, 'azimuth_deg': 0.0,
                'offset_fraction': 0.045,  # NEW FIELD (midpoint of 0.04-0.05)
                'source': 'Dougherty et al. 2018, Cassini Grand Finale (Science 362)'},
    'Uranus':  {'tilt_deg': 60.0, 'azimuth_deg': 35.0,
                'source': 'Ness et al. 1986, Voyager 2 magnetometer (Science 233, 85)'},
    'Neptune': {'tilt_deg': 47.0, 'azimuth_deg': 35.0,
                'source': 'Ness et al. 1989, Voyager 2 (Science 246, 1473)'},
}
```

#### Design decisions needed (conversation before building)

D1. **offset_fraction field**: Add to PLANET_DIPOLE. Builder shifts the cone
    apex by offset_fraction * body_radius along the spin axis (northward for
    all four). Uranus/Neptune: no offset field -> default 0 -> no change.
    Does backward compatibility require a default, or are we fine with
    .get('offset_fraction', 0.0)?

D2. **Degenerate cones (Mercury, Saturn: tilt = 0)**:
    Half-angle 0 -> the cone collapses to a line on the spin axis.
    Options:
    a) Render just the offset axis line + info marker (no cone surface).
       Hover text explains the near-zero tilt.
    b) Render a very narrow cone (e.g., tilt = 1 deg) with hover disclosing
       "tilt < 1 deg; cone exaggerated for visibility."
    c) Skip cone entirely; let the existing magnetosphere carry the visual.
       The offset becomes a detail in the magnetosphere hover text.
    Show the Envelope of the Unknowable applies: tilt = 0 means the
    envelope IS a line; faking a wider cone would be the cite-over-recalled
    failure class. Recommendation: option (a).

D3. **Earth offset direction**: Not purely axial -- the dipole center is
    displaced ~540 km toward ~22 deg N, 140 deg E (secular variation). For a
    static visualization, an axial approximation (0.085 R_E northward) is
    defensible with a hover disclosure. The lateral component is small
    relative to the tilt cone's visual scale.

D4. **Jupiter offset direction**: "Shifted toward the northern hemisphere and
    toward the System III active longitude sector." For the same reason as
    azimuth_deg (rotation phase unmodeled), an axial-only offset is the
    honest envelope. Hover text discloses the real geometry is more complex.

D5. **Saturn narrative**: Gemini suggests "render as a purely vertical,
    northward-shifted cylinder." With option (a), Saturn gets an offset line
    + info marker explaining the remarkable near-zero tilt (Cowling's theorem
    paradox, helium-rain axisymmetric filter). Educational value is high.

D6. **CUSTOM_SHELLS wiring**: Each body needs a dipole_cone entry in
    shell_configs.py CUSTOM_SHELLS, identical pattern to Uranus/Neptune
    (per_frame: True, needs_planet_name: True, builder: same function).
    Tooltip per body with sourced tilt, offset, and mission context.

D7. **L-006 (Mercury +0.2 R_M offset)**: Closes naturally when
    offset_fraction is implemented. Anderson 2011 reports 0.19 +/- 0.01;
    L-006 rounds to 0.2. Same data, same source. Close L-006 when the
    entry is built and rendered.

#### Session order
1. Resolve D1-D5 in conversation (design stabilizes before building)
2. Add PLANET_DIPOLE entries (planet_visualization_utilities.py)
3. Extend build_dipole_cone_traces to handle offset_fraction and tilt=0
4. Add CUSTOM_SHELLS dipole_cone entries for Mercury, Earth, Jupiter, Saturn
5. Add/verify checkbox vars in palomas_orrery.py GUI section
6. Smoke test (xvfb)
7. Mode 5 visual verification (Tony renders Mercury, Earth, Jupiter, Saturn)
8. Close L-009 (or narrow), close L-006

---

### 2. Comet MAPS per-frame tail animation
**Ledger:** L-056 (Phase 4 residuals, MAPS per-frame wiring deferred)

#### Current state
- Per-frame engine animates comet tails for all non-MAPS comets when the
  `animate_comet_tails_var` checkbox is on.
- MAPS is explicitly skipped: palomas_orrery.py L2324 (`if name == 'MAPS': continue`).
- The exclusion was a caution gate per ADDENDUM_phase4 decision 1, with a
  "two-site exclusion warning and partition design" captured there.
- The callable (`build_comet_tail_traces`) is the same builder used by all
  comets -- no MAPS-specific builder is needed.
- Static comet tails (plot_objects path, main L6062) already handle MAPS.

#### Prerequisites
- Read ADDENDUM_phase4 to understand the specific concern behind the
  exclusion. The "two-site" warning and "partition design" may refer to the
  frame-1 tail doubling bug (C2a), which was a pre-existing issue for
  engine-owned comets. MAPS might need the same frame-1 guard.
- Understand whether MAPS has any synthetic-object characteristics that
  would interact badly with the per-frame engine (the exoplanet synthetic
  object traceback is a known pattern -- L-055).

#### Session scope
1. Review ADDENDUM_phase4 decision 1 (Tony provides or we find it)
2. Remove the MAPS exclusion gate (L2324)
3. Verify MAPS enters the per-frame allocation correctly
4. Smoke test: animate with MAPS + comet tails checkbox on
5. Verify no frame-1 doubling
6. Check both pipelines (static plot_objects path + animated per-frame path)
7. Update L-056 (close the MAPS wiring item; the other L-056 residuals
   -- O2/O3 wording, apsidal em-dashes -- remain)

#### Risk assessment
Low. The builder is shared. The exclusion was caution, not technical
incompatibility. Main risk: frame-1 doubling (known pattern, known guard).

---

## Ledger items touched or referenced this session

| L-#   | Status change       | Notes                                     |
|-------|--------------------|--------------------------------------------|
| L-015 | Narrowed (OPEN)    | 3 named imports removed; ~78 _info remain  |
| L-018 | -> DONE -> C       | Sole dead import removed; remainder verified |
| L-022 | -> DONE -> C       | Already done (May 27-29 sweep)             |
| L-024 | -> DONE -> C       | Resolved (mesh_resolution 24)              |
| L-029 | -> DONE -> C       | Absorbed; zero matches in codebase         |
| L-019 | -> DONE -> C       | Tony verified ring marker rotation         |
| L-021 | -> DONE -> C       | Tony verified no superimposition           |
| L-023 | -> DONE -> C       | Tony verified ring marker placement        |
| L-014 | -> D.Feature-C     | Recategorized: design decision             |
| L-017 | -> D.Feature-C     | Recategorized: refactor, design-before-code |
| L-006 | Scoped (next)      | Closes with dipole offset implementation   |
| L-009 | Scoped (next)      | Provenance gate now satisfied              |
| L-056 | Scoped (next)      | MAPS per-frame wiring                      |
| --    | Tooling            | ledger_index.py: RICE scoring (Score column, sort by score) |
| --    | Documentation      | LEDGER_CONSOLIDATED.md: RICE dimensions + usage documented |

Commits: feab717 -> 7964193 -> e0c5313 -> dc88a53 -> 7a870ff (5 commits)

Final HEAD: 7a870ff40e932603f847e22648c7b40f57b8a898
