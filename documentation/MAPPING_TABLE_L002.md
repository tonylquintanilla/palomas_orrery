# L-002 Extraction Mapping Table

v3.29 (807 lines) -> v3.30 (resident) + skills/ (on demand) + ledger.
Line numbers reference project_instructions_v3_29.md as uploaded July 1,
2026. Every v3.29 line lands in exactly one PRIMARY destination; deliberate
duplications are listed separately in the registry at the end.
Verification method: read this table against v3.29; every section should be
accounted for. Nothing was dropped.

## Part-by-part disposition

| v3.29 section (lines) | Disposition | Destination |
|---|---|---|
| Preamble (1-28) | RESIDENT, amended | v3.30 Preamble (adds the two-layer constitution paragraph) |
| Part 1: Session Start (30-41) | RESIDENT, amended | v3.30 Part 1 (adds ledger to Check context, per go-ahead point 7) |
| Part 1: Quick Decisions (43-60) | RESIDENT unchanged | v3.30 Part 1 |
| Part 1: Modes + Mode 7 (62-110) | RESIDENT unchanged | v3.30 Part 1 |
| Part 1: Triggers -> Responses (112-132) | RESIDENT, amended | v3.30 Part 1 (adds "Relevant skill unfired -> load it" row) |
| Part 1: Context Priority (134-161) | RESIDENT, amended | v3.30 Part 1 (tier 5 now names skills + manifest versions) |
| Part 2: Core Principles (167-175) | RESIDENT unchanged | v3.30 Part 2 |
| Part 2: Procedural Criticality (177-200) | RESIDENT, amended | v3.30 Part 2 (adds one sentence: tiers span both layers) |
| Part 2: Anti-Patterns (202-225) | RESIDENT, amended | v3.30 Part 2 ("Skip agentic pre-test" row now points at the skill) |
| Part 2: Workflow Patterns (227-263) | RESIDENT unchanged | v3.30 Part 2 (incl. Graceful Fallback; also echoed in horizons skill) |
| Bottom-Up Editing (267-269) | EXTRACT | safe-file-editing |
| Unicode-Safe Agentic Editing (271-281) | EXTRACT | safe-file-editing |
| Agentic Pre-Test Protocol (283-312) | EXTRACT + resident pointer | agentic-pre-test (full); v3.30 Part 3 one-paragraph pointer [CRITICAL] |
| grep -c in && chains (314-319) | EXTRACT | safe-file-editing |
| File Encoding (321-324) | EXTRACT | safe-file-editing |
| Platform Neutrality (326-335) | EXTRACT, split | safe-file-editing (generic patterns); agentic-pre-test (SystemButtonFace headliner) |
| Session-Start Repo Pull / SHA Round Trip (337-367) | RESIDENT, amended | v3.30 Part 3 (adds gallery-repo separate-pin line) |
| Uploads Before Project Files (369-372) | RESIDENT unchanged | v3.30 Part 3 |
| Enumerate Uploads (374-388) | RESIDENT unchanged | v3.30 Part 3 |
| Verify Base Against Handoff (390-392) | RESIDENT unchanged | v3.30 Part 3 |
| Verify Execution, Not Appearance (394-413) | RESIDENT, compressed | v3.30 Part 3 (principle + 3 failure modes kept; SHELL_CONFIGS dispatch specifics -> orrery-coding-conventions "Live Shell Dispatch") |
| Check All Parallel Pipelines (415-419) | RESIDENT unchanged | v3.30 Part 3 |
| Visual Verification (421-425) | RESIDENT, compressed | v3.30 Part 3 (judgment core kept; kissing-test specifics -> orrery-coding-conventions "Visual Verification Details") |
| Reference Frame Diagnostic (427-428) | EXTRACT | horizons-orbital-mechanics |
| Horizons Center Body Rules (430-434) | EXTRACT | horizons-orbital-mechanics |
| 3D Axis Control Convention (436-440) | EXTRACT | orrery-coding-conventions |
| Hover Text AU Convention (442-445) | EXTRACT | orrery-coding-conventions (master copy) |
| Single Info Marker Pattern (447-468) | EXTRACT | orrery-coding-conventions |
| Credit Line Convention (470-473) | EXTRACT | orrery-coding-conventions (master copy) |
| Marker Symbol Convention (475-485) | EXTRACT | orrery-coding-conventions |
| Module Docstring Standard (487-505) | EXTRACT | orrery-coding-conventions (atlas tooling line also echoed in ledger-and-session-records) |
| Fetched vs Recalled Convention (507-520) | RESIDENT unchanged | v3.30 Part 3 (procedures duplicated in provenance-discipline; principle stays the gate) |
| Show the Envelope (522-537) | RESIDENT unchanged | v3.30 Part 3 (summary duplicated in provenance-discipline) |
| Provenance Audit (539-556) | EXTRACT, updated | provenance-discipline (scanner mechanics updated to HEAD b29ad3f8: role-driven gate, humanitarian units, coverage gap -- v3.29's text predated L-078) |
| Barycenter Rule (558-560) | EXTRACT | orrery-coding-conventions |
| Part 4: Foundation (563-651) | RESIDENT unchanged | v3.30 Part 4 (byte-comparable) |
| Part 5: Quotables (656-687) | RESIDENT unchanged | v3.30 Part 5 |
| Part 5: Lessons Archive, Technical (691-718) | EXTRACT, distributed | See per-lesson table below; full list also preserved in ledger appendix |
| Part 5: Lessons Archive, Process (721-752) | RESIDENT unchanged | v3.30 Part 5 (+1 new skills-are-stores lesson appended) |
| Part 5: Lessons Archive, Philosophical (755-764) | RESIDENT unchanged | v3.30 Part 5 |
| Part 5: Roles (767-770) | RESIDENT unchanged | v3.30 Part 5 |
| Part 5: Version History (773-807) | MOVED | LEDGER_version_history_block.md (full); v3.30 keeps v3.29 summary + new v3.30 entry as pointer |

## Technical lessons -> skill field notes (per-lesson)

| v3.29 technical lesson (line) | Destination skill |
|---|---|
| Cache nested dict (692) | horizons-orbital-mechanics |
| Reference frames differ / inclination (693) | horizons-orbital-mechanics |
| Osculating elements match center (694) | horizons-orbital-mechanics |
| Horizons numeric centers, helio_id vs center_id (695) | horizons-orbital-mechanics |
| JPL binary IDs (696) | horizons-orbital-mechanics |
| Plotly camera zoom (697) | orrery-coding-conventions |
| xvfb + throwaway swap (698) | agentic-pre-test |
| Binary mode preserves endings (699) | safe-file-editing |
| 5 parallel pipelines (700) | orrery-coding-conventions (gate itself stays resident) |
| customdata / _studio survive extraction (701) | orrery-coding-conventions + gallery-pipeline |
| Plotly.js native touch (702) | gallery-pipeline |
| D-pad pan arrows 2D/3D (703) | gallery-pipeline |
| Stacked bugs (704) | orrery-coding-conventions |
| JSON.stringify guard (705) | gallery-pipeline |
| position: fixed vs absolute (706) | gallery-pipeline |
| 3D annotations scene vs layout (707) | orrery-coding-conventions |
| Studio source vs export (708) | gallery-pipeline |
| Horizons step format (709) | horizons-orbital-mechanics |
| Encounter resolution scales (710) | horizons-orbital-mechanics |
| Roche limit (711) | horizons-orbital-mechanics |
| Celestial sphere obliquity rotation (712) | horizons-orbital-mechanics (also noted in orrery-coding-conventions) |
| Shell dispatch live/dead paths (713) | orrery-coding-conventions |
| Scatter3d border width + 8-symbol palette (714) | orrery-coding-conventions |
| Swallowed exception hides render bugs (715) | orrery-coding-conventions (also resident in Verify Execution) |
| grep -c non-zero exit (716) | safe-file-editing |
| GitHub reachable, SHA round-trip mechanics (717) | RESIDENT (already in Part 3 SHA gate; lesson line preserved in ledger appendix) |
| Two surviving store failures (718) | RESIDENT (same; preserved in ledger appendix) |

## New content with no v3.29 source (first-time capture)

| Content | Skill | Sources |
|---|---|---|
| Teaser/blockbuster architecture, engine/scenario contract, 3+5 cards, CDATA, ERA5T lag, three-tier fetch, cache invalidation, developing-scenario pattern, briefing/encyclopedia split, Copernicus attribution | earth-system-pipeline | earth_system_generator.py, earth_system_common.py, scenario modules at b29ad3f8; western_heatwave_handoff_v9.md |
| Human-cost restraint discipline (transcribe-don't-sum, >=20% rule, IPC voice, two-tier text, route ethics) | earth-system-pipeline | HANDOFF_food_insecurity_design_v2.md, HANDOFF_food_insecurity_build_v2.md, food_insecurity_generator.py |
| Two-repo coupling, WYSIWYG authority, flag contracts (_studio_config, _encyclopedia, _kmz_handoff, _original_text), preview-through-viewer, deployment patterns, mobile facts | gallery-pipeline | tools/gallery_studio.py, tools/json_converter.py, index.html at 89c8bf30; web_gallery_handoff.md |
| Ledger block format, indexer mechanics, RICE, handoff structure, verification tags, protocol/skills change-log role | ledger-and-session-records | LEDGER_CONSOLIDATED.md header, ledger_index.py at b29ad3f8; handoffs v28/v29 |
| Scanner role-driven gate, coverage gap, humanitarian units, composed/transcribed tiers | provenance-discipline | provenance_scanner.py at b29ad3f8; food insecurity handoffs |

## Deliberate duplication registry (update all copies on amendment)

| Convention | Master copy | Duplicates |
|---|---|---|
| Hover AU alongside km | orrery-coding-conventions | earth-system-pipeline, gallery-pipeline (shared-conventions stanzas) |
| Credit line | orrery-coding-conventions | earth-system-pipeline, gallery-pipeline |
| ASCII/LF encoding gate | safe-file-editing | agentic-pre-test, earth-system-pipeline, gallery-pipeline |
| Human-cost restraint core (3 lines) | earth-system-pipeline | gallery-pipeline (with load pointer) |
| Fetched-vs-recalled + envelope | RESIDENT v3.30 Part 3 (governing) | provenance-discipline (procedures) -- skill defers to gates on conflict |
| Shell dispatch map | orrery-coding-conventions | agentic-pre-test (one-line live-path fact); resident Verify Execution (pointer only) |
| Tier-1 = 0 push gate | provenance-discipline | v3.30 Skill Manifest row; earth-system-pipeline shared stanza |
| Barycenter rule | orrery-coding-conventions | horizons-orbital-mechanics (pointer only) |

## Accounting

v3.29: 807 lines resident. v3.30: ~640 lines resident (Preamble +25 net for
the constitution paragraph and manifest table; Part 3 -170 net; Part 5 -75
net: technical lessons and version history out, pointers and one new lesson
in). Net resident reduction ~165-170 lines (~21%), PLUS ~1,100 lines of
skill content of which roughly two thirds is knowledge never before written
down in the protocol (skills 6-8). The payoff is the extensible layer, not
the line count.

[VERIFY] tags: none remain in the delivered skills -- every workflow claim
in skills 6-8 traces to code at the pinned SHAs or to a named handoff. Two
items were VERIFIED AGAINST HEAD during the build rather than trusted from
the pre-design: (1) the scanner's L-078 role-driven gate IS at b29ad3f8, so
provenance-discipline describes it (v3.29's Provenance Audit text was
already stale); (2) gallery_studio.py / json_converter.py live in the
GALLERY repo tools/, not the orrery repo -- gallery-pipeline is stamped with
both SHAs.
