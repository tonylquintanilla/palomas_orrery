# Ledger insert -- Protocol Version History appendix

INSTRUCTIONS (delete this header block after pasting):
Paste everything below the cut line at the END of LEDGER_CONSOLIDATED.md,
after the last detail section. Safe for ledger_index.py by construction:
the indexer only regenerates the zone between <!-- INDEX:START --> and
<!-- INDEX:END --> and only parses `#### [L-` headers -- this appendix uses
neither, so it is inert to the tooling. Then run ledger_index.py once to
confirm zero new problems reported. The v3.30 protocol's Part 5 points here.

------------------------------------------------------------------- cut ---

## Appendix: Protocol Version History

The protocol's change log lives here as of v3.30; the protocol document
keeps only the most recent entries. Skill-layer changes are logged here
too (or as L-items when they warrant one): skill name, new version, and
the SHA it was cut from.

v1.0-v3.12 (Oct 2025 - Feb 2026): Foundation through Gallery Studio workflow redesign.
  Covers: modes, alignment, discovery pathway, Einstein proof, platform integration,
  Windows encoding, Horizons center patterns, agentic/targeted guidance, xvfb pre-test,
  bottom-up editing, Unicode-safe editing, Mode 7, LF line endings, JPL binary IDs,
  parallel pipeline lesson, iterative design planning, irreducibility argument,
  Gallery Studio session, _studio flag, pan arrows, Hassabis corroboration,
  featured trace labels, gallery badges, studio workflow redesign.

v3.13 (Mar 5, 2026): Studio source vs export distinction. 3D axis dtick+range convention. Hover text AU convention.

v3.14 (Mar 9, 2026): The Epistemic Dialogue. Polycrisis framework. Gemini elevated to dialogue partner.

v3.15 (Mar 14, 2026): Adaptive encounter resolution design. Two-length-scale insight. Double-Helix as safety mechanism.

v3.16 (Mar 25, 2026): Verify base against handoff before building on multi-session files.

v3.17 (Apr 3, 2026): Competitive Mode 7. Activation vs provision. Interpretation gap as signal. Fog of war is the experiment.

v3.18 (Apr 10, 2026): Single info marker pattern. Credit line convention. Ghost tail legendgroup. MAPS elegy.

v3.19 (Apr 13, 2026): Marker symbol convention. Two-tier label system. Renderer refactor. Celestial sphere complete.

v3.20 (Apr 14, 2026): Module Docstring Standard. Module Atlas tooling (99 modules, 785 functions, 86K lines).

v3.21 (May 4, 2026): Project file staleness rule formalized. Object Encyclopedia. Encounter Export design.

v3.22 (May 12, 2026): Collegial Mode 7 pattern. The Weasley Principle. Single info marker codebase-wide refactor: 141 conversions, 18 files, 3 Claude models, 9-13 MB savings per render.

v3.23 (May 16, 2026): Procedural criticality framework -- three-tier taxonomy (CRITICAL / QUALITY / PRACTICE), a Part-2 principle with markers across Part 3. Broad-first methodology validated; procedure-to-judgment ratio scales with experience and shared context. Grounded in Tony's ops-management experience (LOTO, normalization of deviance).

v3.24 (May 29, 2026): Verify Execution, Not Appearance [CRITICAL] -- map the dispatch before editing leaves; compile != used != edited; swallowed exceptions hide render bugs. Agentic Pre-Test refined: data-content sweeps need a runtime smoke against the LIVE dispatch. Platform Neutrality [QUALITY]. Plotly facts (Scatter3d ignores border width, 8-symbol palette); transactional binary-mode patching. From the shell-consolidation dispatch discovery -- an inline-marker sweep editing dead code, an osculating marker silently absent 11 weeks; Tony's eyes caught both.

v3.24 re-issue (May 29, 2026): Enumerate Uploads Before Claiming a Review [CRITICAL] -- ls the uploads dir, read the whole set; the in-context subset is invisible to Tony and not authoritative. Recovered lessons the first pass missed (itself built on 9 of 19 handoffs -- the exact failure it names): floating-items-capture, verify-propagation-with-grep, central-factory-migration-intent, testing-in-dependency-order, smoke-test-deferred-pipelines, handoff-numbering-rebase drift.

v3.25 (May 31, 2026): Provenance Audit named as a Part-3 skill (scanner, Tier-1=0 goal, lookback-window mechanics, exceptions-file over-report gotcha). Fetched-vs-Recalled extended: three outcomes (cite / remove-and-note-the-gap / never cite-to-clear); a citation is a provenance claim that must be TRUE [CRITICAL]. From provenance Phase 1, after nearly papering a # Source over recalled data.

v3.26 (June 2, 2026): Session-Start Repo Pull [CRITICAL] -- the GitHub repo at HEAD is ground truth; pull and SHA-pin, build on repo or fresh upload, /mnt/project + project knowledge demoted to orientation. From the stale-Earth thread: a duplicate upload shadowed the current file and a true ghost was served through a project-knowledge replacement; repo-pull validated byte-for-byte.

v3.27 (June 4, 2026): Project knowledge now auto-syncs from the repo (no manual add/delete), retiring v3.26's stale-snapshot + served-ghost class at source. Session-Start reframed around "The SHA is the round trip" -- a matching remote HEAD confirms commit + push + sync in one unforgeable check. Foundation gains "access is not understanding." Quotable: "Our work is not just right -- it's beautiful."

v3.28 (June 6, 2026): Two additions (Movement-2 dipole-cone session, handoff v27). (1) Live repo vs snapshots -- the repo is live-readable any time (re-pull after a push; reading HEAD is the round-trip check, run live: de12f56 -> c25bdd7); project knowledge does NOT re-sync mid-session; un-pushed edits live only in uploads, which stay tier 1. (2) Show the Envelope of the Unknowable -- companion to Fetched-vs-Recalled: where a value is genuinely unknowable (rotation phase / instantaneous azimuth), show the envelope, not a faked point, and say so in the hover where the shape is approximate; faking an unknowable value is the cite-over-recalled failure class [CRITICAL].

v3.29 (June 22, 2026): Three amendments from the animation-refactor sessions (L-003). (1) Agentic Pre-Test [CRITICAL] corrected -- the SystemButtonFace<->gray90 sed round trip is NOT idempotent (palomas_orrery.py has 26 native gray90 literals), so swap on a THROWAWAY copy and discard it; never restore-in-place on the deliverable. (2) Live-dispatch smoke test folded into the data-sweep gate -- exec the whole module under xvfb with the tk mainloop suppressed, to exercise the real path rather than a lookalike. (3) grep -c in && chains [QUALITY] -- grep -c exits non-zero on a zero count, silently breaking the chain; run verification greps standalone or join with ;. Cleanup: merged the duplicate data-sweep paragraphs, trimmed the redundant Uploads-Before-Project-Files block to a pointer, corrected the stale xvfb archive line, dropped the [NEW v3.23] tag.

v3.30 (July 1, 2026): The skills refactor (L-002). The protocol becomes the
constitution of a two-layer system: Part 3's task-triggered conventions and
procedures extracted into eight repo-authored skills (skills/<name>/SKILL.md,
each versioned and SHA-stamped; installed to the account as a deployment
step), with the resident document keeping the checkpoint CRITICAL gates, the
modes, the principles, the Foundation, and the quotables. Skill set at 1.0:
orrery-coding-conventions, safe-file-editing (portable), agentic-pre-test,
horizons-orbital-mechanics, provenance-discipline, earth-system-pipeline,
gallery-pipeline, ledger-and-session-records -- all cut from palomas_orrery
@ b29ad3f8 (gallery-pipeline also from tonyquintanilla.github.io @ 89c8bf30).
Part-3 technical lessons distributed into skills as field notes; the full
v3.29 Technical lessons list is preserved verbatim below for institutional
memory. Skill Manifest table added to Part 3 as the under-trigger backstop
and version drift check; a Triggers row added ("Relevant skill unfired ->
load it"). Skills 6-8 are first-time capture: Earth System pipeline +
human-cost restraint discipline, gallery pipeline + WYSIWYG authority,
ledger/handoff/manifest conventions -- knowledge that previously lived only
in handoffs and code. Version history moved here; the ledger is now the
change log for protocol and skills. Extraction audit trail:
documentation/MAPPING_TABLE_L002.md. Designed with Claude Opus 4.6; built
with Claude Fable 5 via collegial relay; Tony integrated.

### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)

- Cache: cache[name]['elements'] (nested dict)
- Reference frames can differ for same object; inclination reveals coordinate system
- Osculating elements must match viewing center (Charon@9)
- Horizons centers: Only numeric IDs work. helio_id vs center_id: opposite directions
- JPL binary IDs: 20XXXXXX (barycenter), 920XXXXXX (primary), 120XXXXXX (secondary). Derive primary from secondary via mass ratio
- Plotly camera: Axis ranges control zoom, not camera distance
- xvfb-run enables headless GUI testing; SystemButtonFace -> gray90 for Linux on a THROWAWAY copy -- the swap is NOT idempotent (26 native gray90 literals in palomas_orrery.py), so never restore-in-place on the deliverable
- Python binary mode (rb/wb) preserves line endings and Unicode; sed can corrupt multi-byte UTF-8
- Position data flows through 5 parallel pipelines in palomas_orrery.py -- ALL must be patched
- Plotly customdata survives JSON extraction; _studio flag survives -- downstream consumers can detect curated plots
- Plotly.js native touch works on mobile/tablet without custom code
- D-pad pan arrows: 2D uses Plotly.relayout on axis ranges, 3D uses camera eye/center shifting
- Stacked bugs: fixing one can reveal a second that was invisible before
- JS: JSON.stringify(undefined).substring() crashes; always guard with || ''
- position: fixed escapes CSS containment; position: absolute stays inside parent
- Plotly 3D annotations go on scene.annotations; 2D on layout.annotations
- Gallery Studio source vs export: source has figure-native values; export has _studio_config overlay
- Horizons step format: {number}{unit} (1m, 5m, 1h, 6h, 1d)
- Encounter resolution: cube scale (dist_km * 4) frames view; curvature scale drives fetch step
- Roche limit is not absolute: tensile strength allows survival inside it
- Celestial sphere in ecliptic frame: unit vectors rotated from equatorial via obliquity about X axis
- Sphere shells render via SHELL_CONFIGS -> build_sphere_shell -> create_info_marker (factory). Inline markers in *_visualization_shells.py are dead code for sphere shells; custom geometry (magnetospheres, rings, belts) routes via CUSTOM_SHELLS and uses the live inline path
- Plotly Scatter3d ignores marker border WIDTH (plotly.js #4118) -- the contrast lever is FILL color, not border. 3D symbol palette is only 8: circle, circle-open, cross, diamond, diamond-open, square, square-open, x
- A swallowed exception in try/except hides render bugs; an undefined variable can drop a marker silently for weeks. Check the console for the caught-error print
- grep -c exits non-zero on a zero count, silently breaking an && chain (the next command never runs while output looks complete) -- run verification greps standalone or join with ;
- GitHub is reachable in-environment: git ls-remote gives branch+HEAD SHA with no auth; raw.githubusercontent.com fetches files byte-exact. The HEAD SHA is the unforgeable current-state token AND the round-trip check -- a matching remote HEAD confirms commit + push + sync at once (project knowledge auto-syncs from the repo as of v3.27)
- The two surviving store failures are honest and visible -- no push, or no sync -- both show as a HEAD mismatch. (v3.26's stale-snapshot + served-ghost failures came from the manual step, retired in v3.27)
