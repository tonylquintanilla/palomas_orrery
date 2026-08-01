"""
provenance_scanner.py - Fact provenance auditor for Paloma's Orrery.

Scans every .py file in the project for facts that need verification:
named constants, dictionary contents, and numeric claims in display
strings. Scores each finding by Vulnerability x Criticality and flags
cross-file duplicates and inconsistencies. Produces PROVENANCE_AUDIT.md.

Architecture: "unit of provenance"
    The unit is the smallest thing that has a coherent source citation.
    A dict with one `# Source:` comment is ONE unit, not N entries.
    A hover string with three numbers that co-refer is ONE unit, not
    three separate claims. Each unit is scored once; reports can break
    down to per-entry for dicts when displayed.

    This matters because citations in this codebase attach at the
    declaration level (above a dict, in its docstring, at the top of
    a section) rather than line-by-line. An earlier line-granular
    scanner flagged every dict entry as uncited even when the dict
    itself had a clear source block above it.

    Criticality is resolved per imported-name, not per module. If
    `KM_PER_AU` is imported by four files, it is C=5 (propagating).
    If `color_map` is defined in the same file but not imported
    anywhere, it is not C=5 just because its module is.

Companion tools:
    module_atlas.py               -- shared dependency graph
    test_constants_provenance.py  -- pins specific verified values
                                     in constants_new.py

Usage:
    python provenance_scanner.py                   # scan current directory
    python provenance_scanner.py /path/to/project  # scan specific directory
    python provenance_scanner.py --output audit.md # custom output filename

Known limitations and accepted residuals:

    AUDIT HISTORY:
    Stage 1 (April 2026): Shell files audited. 231 Tier-1 findings across
    18 files processed. 26 factual corrections made. Primary tool: Claude
    Sonnet 4.6 + Gemini fact-check via Tony as integrator.

    Stage 2 (April 2026): info_dictionary.py audited. 54 Tier-1 findings
    processed, 9 factual corrections made, ~50 source citations added.
    Tool: Claude Sonnet 4.6 + Gemini (4 worksheets, ~130 claims verified).

    Stage 3 (April 2026): Scanner improvements. Claude Opus 4.7 reviewed
    the audit state and identified: (a) duplicate string detection gap
    (var=(text) / 'description':(text) pattern inflating counts ~30%),
    (b) cross-reference opportunity against constants_new.py pinned values,
    (c) solar/uranus shell files as primary remaining Tier-1 source.
    Option B (dedup) implemented; Option A (constant cross-reference)
    implemented, then retired in August 2026 (D8.5) -- value matching is
    not provenance. See mechanism 8 below.

    Stage 3 also added: lookback 30->60, exceptions file loading,
    accepted residuals block in report. 34 source citations added to
    solar_visualization_shells.py, 10 to uranus_visualization_shells.py.
    Gemini verified all remaining claims in asteroid_belt and star_notes.

    Stage 4 (April 2026): Final suppression fixes. Three persistent false
    positives (comet:1282, earth:649, neptune:903) remained after Stage 3
    due to two bugs: (a) fingerprints truncated to 40 chars in
    load_exceptions preventing matches on longer strings; (b) is_suppressed
    only searched context_text, missing fingerprints inside string values.
    Both fixed: truncation removed, raw_value added to ProvenanceUnit and
    searched alongside context_text. Correct fingerprints obtained from
    uploaded source files. Diagnostic: Claude Opus 4.7. Fix: Claude Sonnet 4.6.

    Stage 5 (April 2026): Remaining genuine Tier-2 gaps addressed.
    Citations added to: apsidal_markers.py ENCOUNTER_THRESHOLD_AU (Hill
    sphere derivation + engineering rationale); sgr_a_visualization_
    precession.py S4714_ACCURACY_PATCH (Peissker et al. 2020 + refinement
    note); solar_visualization_shells.py hover_text_sun and create_sun_
    hover_text() (NASA Solar Fact Sheet + corona refs). star_notes.py:
    10 star entries verified by Gemini (2 worksheets, Apr 2026) and cited.
    Corrections found: Betelgeuse size (Mars-Jupiter range, pulsates;
    Montarges et al. 2021), Mintaka distance (900->1200 ly; Shenar et al.
    2015 / Gaia), Fomalhaut b (reinterpreted as dust cloud, not planet).
    Sources: McAlister (2005), Hummel (2013), Ramiaramanantsoa (2018).

    Final state: Tier-1 = 0. All Tier-2 items cited or documented as
    accepted residuals. Audit complete April 2026.

    1. Multi-line string false positives (info_dictionary.py):
       INFO strings can be 50-100 lines long. The scanner detects
       citations at the entry-key level (# Source: above the dict key)
       but individual continuation lines within the same string may
       fall outside the lookback=60 window and be reported as uncited.
       Entries longer than ~60 lines (Apollo 11 S-IVB, Halley,
       Artemis II) still produce mid-string false positives.
       These are not real gaps -- the citation exists at the key level.
       Treat Tier-2 findings in info_dictionary.py as accepted residuals
       unless they correspond to a top-level entry key that genuinely
       lacks a # Source: comment.
       All info_dictionary.py Tier-1 findings resolved April 2026.
       9 factual corrections confirmed via Gemini fact-check.

    2. "Sourced but potentially stale" (V_STALE) findings:
       Entries verified correct by Gemini fact-check (April 2026) but
       containing date-sensitive language (e.g. "currently", "planned",
       "expected") are flagged V_STALE regardless. These reflect real
       staleness risk for mission status and close-approach data, not
       citation gaps. Review when adding new objects or updating missions,
       not as standalone audit tasks.

    3. Lagrange point entries (L1-L5, EM-L1 through EM-L5):
       Text is reproduced verbatim from JPL Horizons output and carries
       "From JPL Horizons" inline. Source comments added April 2026.
       Any residual flags on continuation lines are false positives.

    4. Numeric values in code lines flagged as display strings:
       The scanner flags numeric literals in Python code (variable
       assignments, np.radians() calls, coordinate arithmetic, Plotly
       arguments) as uncited display string claims. All confirmed false
       positives are suppressed via data/provenance_exceptions.json.
       Known pattern: neptune magnetic axis coordinates, earth bow shock
       trace construction, solar galactic tide showlegend argument,
       uranus empirical tilt code comment. Root cause: AST string-node
       detection picks up numeric literals in adjacent code lines.
       These recur when shell files are regenerated -- add new instances
       to provenance_exceptions.json rather than chasing them.
       Identified and classified by Claude Opus 4.7 (April 2026).

    5. Module docstrings and dict key strings flagged as display strings:
       Known false positives suppressed in provenance_exceptions.json:
         - jupiter_visualization_shells.py line 1 (module docstring)
         - comet_visualization_shells.py line 1282 (function docstring)
         - sgr_a_star_data.py lines 657, 664 (dict key name strings)
         - star_notes.py line 1 (module docstring)
       The scanner's docstring detector catches most of these but misses
       dict key strings. No action needed.

    6. Dict values with inline 'source' keys not recognized as citations:
       spacecraft_encounters.py Tier-2 findings at lines 235 and 266
       carry 'source': 'NASA/JSC' as a dict value. The scanner requires
       a # Source: comment; inline dict keys are not recognized. These
       entries are cited -- the scanner finding is a false positive.
       Future fix: extend SOURCE_PATTERNS to recognize 'source': '...'
       dict value pattern.

    7. Duplicate string detection (Option B):
       The var=(text) / 'description':(text) pattern in shell files
       creates two AST string nodes with identical content at different
       line numbers. Content-hash deduplication (first 200 chars) added
       April 2026 per Claude Opus 4.7 recommendation. First occurrence
       (standalone variable) wins; dict entry version suppressed.

    8. Constant cross-reference (Option A) -- RETIRED, D8.5, Aug 2026:
       Marked display string claims as V_SOURCED when their numeric
       values matched pinned constants in constants_new.py. Retired
       because a value match is not provenance: it shows two numbers
       are equal, not that anyone consulted a source. It credited 26
       display strings, 23 of which belonged in Tier 1.
       Value matches are still reported by the shadow-constant detector
       as a diagnostic. build_pinned_values() remains, feeding that
       detector only -- it no longer reaches scoring.
       The same audit retired STALE-ONLY credit, which granted
       V_SOURCED to uncited units carrying a staleness marker.

    9. Accepted Tier-2 residuals (documented, no action needed):
       The following are documented in provenance_exceptions.json:
         - info_dictionary.py: Tier-2 V_STALE findings are multi-line
           string continuation false positives (see item 1 above).
         - spacecraft_encounters.py: lines 235, 266 carry inline
           'source' dict value (see item 6 above).
         - star_notes.py unique_notes dict (553 entries, score 15):
           stellar parameters verified against SIMBAD/Gaia DR3 April
           2026. V_STALE flag reflects real staleness risk as catalogs
           improve. Review when adding new stars, not standalone task.
         - comet_visualization_shells.py COMET_NUCLEUS_SIZES and
           COMET_FEATURE_THRESHOLDS: rendering geometry dicts, low
           user-visible impact. Deferred until comet shell refactor.
         - constants_new.py Tier-2 items: all V_SOURCED (score 10 =
           V_SOURCED x C_PROPAGATING). Cited, not errors.

   10. Gemini fact-check verdicts (April 2026) -- key corrections found:
         - Polymele: D~40 km D-type 446h -> D~21 km P-type 5.9h
           (size/type swapped with Leucus)
         - Leucus: D~34 km, 4th Trojan -> D~40 km, 3rd Trojan, 446h
         - Vanth/Orcus-Vanth mass ratio: 16% -> 14.2% (ALMA 2018)
         - Dysnomia diameter: ~700 km -> ~150-400 km (uncertain)
         - Gonggong aphelion: "near aphelion ~52.7 AU" -> "~89 AU,
           aphelion ~101 AU late 21st century"
         - Pioneer 10 last signal: March 3 2002 -> April 27 2002
         - Gaia mission end: 2025-3-28 -> observations ceased 2025-1-15
         - Jupiter-family comets as Hills Cloud source: WRONG. JFCs
           originate from Kuiper Belt/Scattered Disk, not Hills Cloud.
           Fixed in 6 locations in solar_visualization_shells.py.
           Source: Dones et al. (2004) Comets II.
         - Hilda triangle "at L3/L4/L5 Lagrange points": WRONG. Pattern
           arises from 3:2 resonance dynamics; asteroids not resident at
           Lagrange points. Fixed in asteroid_belt_visualization_shells.py.
         - Agamemnon in L5 list: WRONG. 911 Agamemnon is at L4 (Greek
           camp). Moved to L4 entry.

    11. Color/RGB values are exempt from citable claims -- by design,
        not a gap (Tony's call, July 16, 2026; see LEDGER_CONSOLIDATED.md
        L-124/L-125):
        _make_dict_unit already skips non-constant dict values (colors as
        RGB tuples, nested dicts) when building a dict unit's scored
        `entries` -- a color never becomes its own claim needing its own
        citation. What was previously ambiguous is the OTHER direction:
        the "unit of provenance" convention above says a block `# Source:`
        comment covers the whole dict as one unit, which reads as if it
        also certifies that dict's `color` field(s). It does not. Color
        selection across this codebase is a developer/AI aesthetic
        judgment call -- sometimes loosely informed by real imagery or
        composition data, sometimes chosen purely for visual contrast or
        distinction, sometimes arbitrary -- and is never itself a claim
        this scanner verifies, regardless of what citation sits nearby.
        generate_report() prints this as a standing disclosure so it is
        visible in every generated audit, not just in this docstring.

Module rewritten: April 17, 2026 with Anthropic's Claude Opus 4.7
    (replaces earlier line-granular scanner that produced ~2000
    false-positive Tier-1 findings.)

Module updated: April 2026 with Anthropic's Claude Sonnet 4.6
    (Options A/B, lookback=60, exceptions loading, audit completion.)
Updated with Opus 4.8 for food insecurity provenance, June 26, 2026.
Updated with Claude Sonnet 5 for L-078 check 1: role-driven inclusion off
    module_atlas.classify_role, additive over narrative_files; coverage-gap
    safety net for 'other'-role files; citation-recognition fix for
    single-line narrative strings (June 30, 2026).
Updated with Claude Sonnet 5, July 2026: added a "Findings by File"
    summary table to generate_report(), showing tier 1-4 counts per file
    at a glance (sorted by total findings) ahead of the existing per-tier
    detail sections. First step of a two-part groundwork request (F1
    design-review session).
Updated with Claude Sonnet 5, July 2026 (same session, second increment):
    added MODULE_DOMAIN_MAP / classify_domain() and a "Findings by File
    Type" summary section, grouping findings into six subject-matter
    domains (orrery, earth science, gallery, stars, utilities, dev tools)
    -- the last two new, split out of an original four after Tony resolved
    four ambiguous clusters (Sgr A* family, cross-cutting utility files,
    devtools/infra, social_media_export.py). Domain is a report-only
    grouping, independent of module_atlas's functional-role ROLE_MAP. Also
    added a Domain column to the existing "Findings by File" table, and a
    Domain Coverage Gap note (mirroring the existing ROLE_MAP coverage-gap
    pattern) that flags any future file with findings but no
    MODULE_DOMAIN_MAP entry, rather than letting it silently default.
    Gallery domain currently shows 0 findings -- the gallery ASSEMBLER
    pipeline lives in the separate tonyquintanilla.github.io repo, out of
    this scanner's reach; only gallery-adjacent files inside this repo
    (currently just social_media_export.py) can ever populate it here.
    Self-referential note: this scanner scans itself, so this very change
    added 2 new low-tier findings against provenance_scanner.py's own
    entry in the audit (MODULE_DOMAIN_MAP as an uncited dict, Tier 3;
    DOMAIN_LABELS similarly, Tier 4) -- verified deliberate, not a scoring
    regression: both are organizational/report labels, not factual claims,
    correctly landing in the no-action tiers. Any future edit to this file
    that adds a new module-level dict or descriptive string will likewise
    nudge its own self-scan numbers. Worth remembering before assuming a
    total-findings delta always means a real citation gap appeared
    elsewhere -- check whether the delta is this file scanning its own
    diff first.

Updated with Claude Sonnet 5, July 16, 2026: documented the color/RGB
    exemption from citable claims (item 11 above) and added the matching
    disclosure paragraph to generate_report()'s header, per Tony's
    direct call that color citations across the codebase have been
    uneven and some effectively overclaimed -- this documents the
    scanner's existing skip behavior rather than changing any scoring.

Module updated: July 2026 with Anthropic's Claude Opus 5 (L-163 Phase 3:
classify_role() now takes the filepath this loop already has, so the role
comes from the module's own docstring tag).

Module updated: July 2026 with Anthropic's Claude Sonnet 5 (L-162:
CONCEPT_ALIASES entries added for the 14 newly-named CENTER_BODY_RADII
constants).

Module updated: July 2026 with Anthropic's Claude Opus 5 (constant_has_own_
Module updated: August 2026 with Anthropic's Claude Opus 5 (D8.5: Option A
retired -- V_SOURCED is no longer granted for numeric coincidence -- and
stale-only credit retired with it, since a staleness marker is not a source.
build_pinned_values retained; it now feeds the shadow-constant diagnostic only).

Module updated: July 2026 with Anthropic's Claude Opus 5 (constant_has_own_
citation extracted as the single citation predicate; build_pinned_values no
longer uses a distance window that could inherit a neighbour's citation).

Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Phase 1d/1e:
frozen-copy detection for shadow constants, author-year citation forms,
Fahrenheit/Celsius units, the Tier-1 banner, and neutral tier labels).

Module updated: July 2026 with Anthropic's Claude Opus 5 (L-156 Gap item 6,
Phase 1c: citation-block inheritance -- a display string inside a dict block
that carries its own citation now inherits it at V_SOURCED instead of
scoring V_RECALLED. Strictly narrowest-block containment; an uncited block
inherits nothing, which is what keeps the genuinely uncited blocks tracked
as L-173 visible).

Role: devtool
Domain: dev_tools
"""

import ast
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

# Reuse the atlas dependency graph builder
from module_atlas import build_dependency_graph, classify_role


# ============================================================
# SCORING CONSTANTS
# ============================================================

# Vulnerability: how likely is this fact to be wrong?
# The four-rung ladder settled in L-156 after three-AI calibration.
V_FETCHED       = 1   # From an authoritative pipeline at runtime
V_CROSS_CHECKED = 2   # Independently cross-checked against dated evidence,
                      # blind (the checker was not shown our value). NEVER
                      # auto-promotable to V_FETCHED at any rigor level --
                      # the scanner can observe that a check is claimed, not
                      # that it was rigorous.
                      # NOTHING SETS THIS YET. Population arrives with the
                      # `# Cross-checked:` annotation recognition in D4;
                      # until then this rung is intentionally empty rather
                      # than dead code.
V_SOURCED       = 3   # Cited, but never independently cross-checked.
                      # Absorbs the former V_STALE rung -- see the reason
                      # strings in score_unit for the retained distinction.
V_RECALLED      = 4   # From model training data, no citation

# Retained alias. V_STALE and V_SOURCED are the same rung as of L-156; the
# name is kept because the accepted-residuals prose and the exceptions file
# both still speak of "V_STALE staleness flags", and silently deleting the
# name would make that vocabulary unresolvable rather than merged.
V_STALE = V_SOURCED

# Criticality: what's the impact if it IS wrong?
C_COSMETIC    = 1   # Colors, label positions, descriptive text
C_INTERNAL    = 2   # Used in code but not displayed
C_LOADBEARING = 3   # Drives geometry, shell radii, orbit params
C_PUBLIC      = 4   # Visible in hover text, gallery, Instagram
C_PROPAGATING = 5   # Imported by other modules, affects calculations

# D1 (ledger L-156) replaced volume-based criticality with type-based
# criticality. The two categories that now decide a constant's or dict's
# score:
C_RELATIONAL  = 4   # Defined as a fraction/multiple of a tracked base
C_MEASURED    = 5   # Independently catalogued fact (radii, periods, masses)
# Ambiguity is not resolved by guessing in either direction. It scores at
# the MEASURED weight (fail-safe up, per D2) AND raises its own report
# banner (per the design review's amendment), so it can neither be buried
# by a low score nor lost in a normal finding row.
C_UNDETERMINED = 5

# ============================================================
# CRITICALITY CLASSIFICATION VOCABULARY (D2, ledger L-156)
# ============================================================
# D2 settled that classification rides the codebase's own naming
# conventions rather than a hand-curated list of named constants. This is
# that rule. It is widened from D2's four unit suffixes to the noun stems
# the codebase actually uses -- KNOWN_ORBITAL_PERIODS and
# COMET_NUCLEUS_SIZES carry their physical meaning in the noun, not in a
# _km/_au suffix, and under D2 as written both defaulted to unclassified
# (62 of 112 constant/dict units did).
#
# L-163's docstring role tags did not exist when D2 was written. They are
# used here as a second, structural input: as a veto on the physical
# categories for devtool/gui/cache modules, and as a fallback for what the
# vocabulary leaves unresolved in data/computation modules.
#
# Additions to these tuples are ledger-tracked under L-156.

CRIT_COSMETIC_STEMS = (
    'color', 'colour', 'label', 'opacity', 'font', 'rgb', 'symbol',
    'tooltip', 'marker',
)
CRIT_RELATIONAL_STEMS = (
    'fraction', 'multiplier', 'scale', 'ratio', 'factor', 'radii',
)
CRIT_MEASURED_STEMS = (
    '_km', '_au', '_kg', '_days', '_deg', '_sec', '_yr',
    'period', 'radius', 'size', 'mass', 'distance', 'belt', 'magnitude',
    'luminosity', 'velocity', 'density', 'albedo', 'diameter',
    'uncertainty', 'inclination', 'eccentricity', 'tilt', 'obliquity',
    'gravity', 'pressure', 'flux', 'wavelength', 'temp', 'temperature',
    'threshold',
)
CRIT_INTERNAL_STEMS = (
    'map', 'mapping', 'name', 'names', 'slug', 'config', 'dir', 'path',
    'url', 'version', 'schema', 'key', 'order', 'alias', 'width',
    'height', 'frames', 'points', 'resolution', 'decimals', 'interval',
    'title', 'tag', 'desc', 'col', 'wrap', 'trunc', 'kb', 'mb', 'count',
    'index', 'limit', 'skip', 'default', 'docstring', 'docstrings',
    'patch', 'ceiling', 'age',
)
CRIT_INTERNAL_ROLES = ('devtool', 'gui', 'cache')
CRIT_PHYSICAL_ROLES = ('data', 'computation')

# Names whose suffix reads relational but whose values are absolute.
# Empty as of Phase A (L-162). CENTER_BODY_RADII needed the override while
# it held 17 raw kilometre literals -- the '_radii' stem would have
# misfiled the project's central radius dict as RELATIONAL. Phase A moved
# those 17 to named *_RADIUS_KM constants, which the '_km' suffix scores
# MEASURED directly. The dict now yields exactly ONE numeric entry --
# Planet 9, deliberately left a raw literal as a model estimate excluded
# from pinning per L-159 -- so forcing MEASURED on it would assert
# catalogued-fact criticality over an explicitly illustrative value.
# Re-checked after Phase A landed, per the note this comment replaces.
CRIT_ABSOLUTE_OVERRIDE = ()


def action_tier(score):
    """Return tier number (1=highest priority, 4=lowest)."""
    if score >= 16: return 1
    if score >= 10: return 2
    if score >= 5:  return 3
    return 4


# ============================================================
# DOMAIN CLASSIFICATION (report grouping, not scanning behavior)
# ============================================================
# Maps module names (no .py) to a subject-matter domain, purely for the
# "Findings by File Type" report breakdown -- distinct from module_atlas's
# ROLE_MAP, which classifies functional role (data/rendering/devtool/...)
# and drives which files get SCANNED at all. Domain answers "what part of
# the project is this," not "what does this module do."
#
# Six domains, confirmed with Tony (F1 provenance-cleanup groundwork
# session, July 2026), expanding the original four (orrery, earth science,
# gallery, stars) after four ambiguous clusters were resolved:
#   - Sgr A*/Galactic Center family -> orrery
#   - devtools/one-shot infra       -> new "dev tools" bucket
#   - social_media_export.py       -> gallery
#   - cross-cutting reference-frame/utility cluster, split three ways:
#       celestial_coordinates, coordinate_system_guide      -> orrery
#       visualization_utils / _2d / _3d / _core             -> stars
#       shared_utilities, formatting_utils, save_utils,
#       report_manager, plot_data_exchange,
#       plot_data_report_widget                             -> new
#                                                                "utilities"
#                                                                bucket
#
# Note: the gallery ASSEMBLER pipeline (resolver.py, cache_reader.py,
# gallery_studio.py, json_converter.py, render_orbits.py, etc.) lives in
# the separate tonyquintanilla.github.io repo and is not scanned by this
# tool at all -- "gallery" here only ever covers gallery-adjacent files
# that live IN this repo (currently just social_media_export.py).
#
# Anything not listed here defaults to 'orrery' (the original catch-all)
# and is tracked as an unmapped module so new files don't silently drift
# into the wrong bucket forever -- see the Domain Coverage Gaps note in
# generate_report().
DOMAIN_LABELS = {
    'orrery':        'Orrery (solar system + orbital mechanics)',
    'earth_science': 'Earth System',
    'gallery':       'Gallery',
    'stars':         'Stars (stellar neighborhood)',
    'utilities':     'Utilities (cross-domain shared helpers)',
    'dev_tools':     'Dev Tools (audit, diagnostics, one-shot scripts)',
}

MODULE_DOMAIN_MAP = {
    # --- orrery: solar system bodies, orbital mechanics, core app ---
    'info_dictionary': 'orrery',
    'celestial_objects': 'orrery',
    'idealized_orbits': 'orrery',
    'solar_visualization_shells': 'orrery',
    'constants_new': 'orrery',
    'neptune_visualization_shells': 'orrery',
    'uranus_visualization_shells': 'orrery',
    'comet_visualization_shells': 'orrery',
    'planet_visualization_utilities': 'orrery',
    'jupiter_visualization_shells': 'orrery',
    'sgr_a_grand_tour': 'orrery',
    'sgr_a_star_data': 'orrery',
    'sgr_a_visualization_core': 'orrery',
    'sgr_a_visualization_core_arcs': 'orrery',
    'sgr_a_visualization_animation': 'orrery',
    'sgr_a_visualization_precession': 'orrery',
    'pluto_visualization_shells': 'orrery',
    'saturn_visualization_shells': 'orrery',
    'spacecraft_encounters': 'orrery',
    'mercury_visualization_shells': 'orrery',
    'asteroid_belt_visualization_shells': 'orrery',
    'celestial_coordinates': 'orrery',
    'venus_visualization_shells': 'orrery',
    'planet9_visualization_shells': 'orrery',
    'apsidal_markers': 'orrery',
    'eris_visualization_shells': 'orrery',
    'mars_visualization_shells': 'orrery',
    'moon_visualization_shells': 'orrery',
    'coordinate_system_guide': 'orrery',
    'palomas_orrery': 'orrery',
    'palomas_orrery_dashboard': 'orrery',
    'close_approach_data': 'orrery',
    'orbit_data_manager': 'orrery',
    'data_acquisition': 'orrery',
    'data_acquisition_distance': 'orrery',
    'orbital_elements': 'orrery',
    'osculating_cache_manager': 'orrery',
    'object_type_analyzer': 'orrery',

    # --- earth_science ---
    'earth_visualization_shells': 'earth_science',
    'paleoclimate_wet_bulb_full': 'earth_science',
    'paleoclimate_human_origins_full': 'earth_science',
    'scenarios_western_heatwave_march_2026': 'earth_science',
    'scenarios_heatwaves': 'earth_science',
    'paleoclimate_visualization_full': 'earth_science',
    'paleoclimate_visualization': 'earth_science',
    'scenarios_coral_bleaching': 'earth_science',
    'food_insecurity_generator': 'earth_science',
    'earth_system_generator': 'earth_science',
    'paleoclimate_dual_scale': 'earth_science',
    'energy_imbalance': 'earth_science',
    'fetch_paleoclimate_data': 'earth_science',
    'fetch_climate_data': 'earth_science',
    'climate_cache_manager': 'earth_science',

    # --- gallery (gallery-adjacent files that live in THIS repo only) ---
    'social_media_export': 'gallery',

    # --- stars: stellar neighborhood, exoplanets, HR/planetarium ---
    'star_notes': 'stars',
    'star_properties': 'stars',
    'stellar_data_patches': 'stars',
    'stellar_parameters': 'stars',
    'exoplanet_coordinates': 'stars',
    'exoplanet_stellar_properties': 'stars',
    'star_sphere_builder': 'stars',
    'exoplanet_systems': 'stars',
    'exoplanet_orbits': 'stars',
    'hr_diagram_distance': 'stars',
    'hr_diagram_apparent_magnitude': 'stars',
    'planetarium_distance': 'stars',
    'planetarium_apparent_magnitude': 'stars',
    'simbad_manager': 'stars',
    'messier_catalog': 'stars',
    'messier_object_data_handler': 'stars',
    'visualization_utils': 'stars',
    'visualization_2d': 'stars',
    'visualization_3d': 'stars',
    'visualization_core': 'stars',

    # --- utilities: genuinely cross-domain shared helpers (new bucket) ---
    'plot_data_report_widget': 'utilities',
    'shared_utilities': 'utilities',
    'formatting_utils': 'utilities',
    'save_utils': 'utilities',
    'report_manager': 'utilities',
    'plot_data_exchange': 'utilities',

    # --- dev_tools: audit/diagnostic/one-shot infra (new bucket) ---
    'provenance_scanner': 'dev_tools',
    'skills_index': 'dev_tools',
    'dep_trace': 'dev_tools',
    'ledger_index': 'dev_tools',
    'measure_perframe_elements': 'dev_tools',
    'module_atlas': 'dev_tools',
    'add_docstrings': 'dev_tools',
    'data_inventory': 'dev_tools',
    'smoke_dipole_cone': 'dev_tools',
    'smoke_rotation_axis': 'dev_tools',
    'test_reset_completeness': 'dev_tools',
    'test_constants_provenance': 'dev_tools',
    'test_orbit_cache': 'dev_tools',
    'verify_orbit_cache': 'dev_tools',
    'create_cache_backups': 'dev_tools',
    'create_ephemeris_database': 'dev_tools',
    'convert_hot_ph_to_json': 'dev_tools',
    'diagnose_bcodmo': 'dev_tools',
    'examine_hot_csv': 'dev_tools',
    'export_orbit_cache': 'dev_tools',
}


def classify_domain(module_name):
    """Classify a module's report domain. Returns (domain, was_mapped)."""
    if module_name in MODULE_DOMAIN_MAP:
        return MODULE_DOMAIN_MAP[module_name], True
    return 'orrery', False  # catch-all default; flagged as unmapped


# ============================================================
# CITATION PATTERNS
# ============================================================
# Applied to the text of a "context block" -- up to 30 lines
# preceding a unit, plus the unit's own lines. This is where
# `# Source: ...` block comments live.

SOURCE_PATTERNS = [
    re.compile(r'#\s*[Ss]ource\s*:', re.IGNORECASE),
    re.compile(r'#\s*(?:Ref|Reference)\s*:', re.IGNORECASE),
    re.compile(r'#\s*(?:IAU|JPL|NASA|ESA|NIST|Horizons|arXiv|doi|'
               r'SIMBAD|Gaia|Hipparcos|VizieR|NSSDCA|NOAA|BCO[- ]DMO|'
               r'ERA5|Copernicus)', re.IGNORECASE),
    re.compile(r'#\s*https?://', re.IGNORECASE),
    re.compile(r'#\s*(?:Verified|Confirmed)\s+', re.IGNORECASE),
    re.compile(r'#\s*(?:Based on|Per|Derived from|According to)\s+',
               re.IGNORECASE),
    # Markers that appear inside docstrings (no leading '#')
    # L-078: case-insensitive -- narrative display strings (scenario
    # briefings, KMZ balloon text) write these ALL CAPS ("SOURCE:") as
    # the reader-facing convention; the code-comment form above is
    # already case-insensitive, this brings the prose form in line.
    re.compile(r'^\s*[Ss]ource\s*:\s', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*[Vv]erified\s*:\s', re.MULTILINE | re.IGNORECASE),
    re.compile(r'^\s*[Rr]ef(?:erence)?\s*:\s', re.MULTILINE | re.IGNORECASE),
    # URL-as-citation patterns (data dict entries like celestial_objects.py
    # where `mission_url` sits alongside `mission_info` narrative).
    # An https URL appearing anywhere in the context block, or a *_url
    # key in a dict, counts as a citation for adjacent claims.
    re.compile(r"['\"]?\w*url\w*['\"]?\s*[:=]\s*['\"]https?://",
               re.IGNORECASE),
    re.compile(r'https?://\S+\.\S+', re.IGNORECASE),
    # L-156 Gap item 7: bare author-year parentheticals.
    #
    # Two live forms, both real citations that previously scored V4
    # RECALLED -- the scanner calling a cited value uncited:
    #     (Vecellio et al.)          (Sherwood & Huber)
    #     (Vecellio et al., 2022)    (Sherwood & Huber, 2010)
    #
    # Tightness is the whole difficulty here. A pattern that merely
    # looks for a capitalised word and a year inside parentheses
    # matches "(May 2026)" -- a date in a comment -- on the first file
    # in the repo. So a match requires EITHER a multi-author marker
    # (et al. / & Author / and Author), OR a four-digit year following
    # a capitalised surname, and month names are excluded outright.
    re.compile(
        r'\((?!(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))'
        r'[A-Z][A-Za-z\'\-]+'
        r'(?:\s+et\s+al\.?|\s*&\s*[A-Z][A-Za-z\'\-]+'
        r'|\s+and\s+[A-Z][A-Za-z\'\-]+)'
        r'(?:,?\s*(?:19|20)\d{2}[a-z]?)?\)'
        r'|'
        r'\((?!(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))'
        r'[A-Z][A-Za-z\'\-]+,?\s+(?:19|20)\d{2}[a-z]?\)'
    ),
]

# Patterns that suggest a cited value may be stale (date-sensitive).
STALE_PATTERNS = [
    re.compile(r'(?:as of|current|currently|latest|updated)\s+\d{4}',
               re.IGNORECASE),
    re.compile(r'(?:Planned|Expected|Upcoming|scheduled)\b',
               re.IGNORECASE),
    re.compile(r'(?:Still active|Currently operating)', re.IGNORECASE),
]

# Looser patterns applied ONLY to docstring text. Docstrings are prose
# and mention provenance without the structured `# Source:` marker.
# If a module or function docstring uses any of these words in a
# citation-like context, we treat the associated claims as cited.
DOCSTRING_CITATION_PATTERNS = [
    re.compile(r'\b[Vv]erified\b', re.IGNORECASE),
    re.compile(r'\b[Cc]itation\b', re.IGNORECASE),
    re.compile(r'\b[Cc]ited\b', re.IGNORECASE),
    re.compile(r'\b(?:authoritative|nominal|canonical)\b', re.IGNORECASE),
    re.compile(r'\b(?:IAU|JPL|NASA|NIST|ESA|Horizons)\b'),
    re.compile(r'\b(?:arXiv|doi)\b', re.IGNORECASE),
    re.compile(r'\bper\s+(?:IAU|JPL|NASA|NIST|ESA|Gemini|review)\b',
               re.IGNORECASE),
    re.compile(r'\bSource of truth\b', re.IGNORECASE),
    re.compile(r'\b[Rr]eviewed\s+by\b'),
]


def has_citation(text, is_docstring=False):
    """Does the given text block contain a citation marker?

    If `is_docstring` is True, prose-style markers are also accepted
    (docstrings describe provenance in prose, not in `# Source:` form)."""
    for pat in SOURCE_PATTERNS:
        if pat.search(text):
            return True
    if is_docstring:
        for pat in DOCSTRING_CITATION_PATTERNS:
            if pat.search(text):
                return True
    return False


def has_stale_marker(text):
    """Does the given text contain a staleness indicator?"""
    for pat in STALE_PATTERNS:
        if pat.search(text):
            return True
    return False


# ============================================================
# NUMERIC CLAIM EXTRACTION (for display strings)
# ============================================================
# Captures numbers with optional comma separators and decimal parts.
# Comma handling: "31,000 km" is one token, not "31" + "000 km".

NUMERIC_CLAIM_RE = re.compile(
    r'(\d{1,3}(?:,\d{3})+(?:\.\d+)?|'     # 31,000 or 31,000.5
    r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'    # 8.33 or 1.5e-3
    r'\s*'
    r'(degrees?\s*[CF]\b|deg\s*[CF]\b|\xb0\s*[CF]\b|'
    r'degrees?\s+(?:Celsius|Fahrenheit)\b|'
    r'R_sun|AU|km/s|km|m/s|degrees?|deg\b|arcsec|mas|pc|kpc|Mpc|'
    r'solar radii|Earth (?:masses|radii)|M_sun|M_earth|R_earth|'
    r'ly|light[- ]years?|parsec|'
    r'days?|years?|hours?|minutes?\b|min\b|sec\b|'
    r'K\b|kelvin|kg\b|g/cm3|g/cc|'
    r'km/h|mph|people|persons?|percent|%)\b',
    re.IGNORECASE
)


def extract_numeric_claims(text):
    """Yield (num_str, unit, value_float) for each numeric claim in text.
    Trivial paired values (0/1/2/3 days/years/hours) are skipped."""
    for m in NUMERIC_CLAIM_RE.finditer(text):
        num_str = m.group(1)
        unit = m.group(2)
        try:
            value = float(num_str.replace(',', ''))
        except ValueError:
            continue
        if value in (0, 1, 2, 3) and unit.lower() in (
                'days', 'years', 'hours', 'minutes', 'min'):
            continue
        yield num_str, unit, value


# ============================================================
# IMPORT RESOLUTION (per-name, not per-module)
# ============================================================

def build_name_import_map(project_dir, local_modules):
    """For each local module, find which NAMES other modules import from it.

    Returns: dict mapping module_name -> {imported_name: set(consumer_modules)}

    Example: imported_names['constants_new']['KM_PER_AU'] =
        {'apsidal_markers', 'idealized_orbits', ...}

    This lets us score a specific symbol rather than the whole module.
    """
    imported_names = defaultdict(lambda: defaultdict(set))

    for fname in os.listdir(project_dir):
        if not fname.endswith('.py'):
            continue
        consumer = fname[:-3]
        filepath = os.path.join(project_dir, fname)
        try:
            with open(filepath, 'rb') as f:
                tree = ast.parse(f.read())
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                mod_root = node.module.split('.')[0]
                if mod_root not in local_modules:
                    continue
                for alias in node.names:
                    name = alias.name
                    if name == '*':
                        imported_names[mod_root]['*'].add(consumer)
                    else:
                        imported_names[mod_root][name].add(consumer)

    return imported_names


def name_is_imported(name, module_name, imported_names):
    """Return (count, consumers) for a name defined in module_name.
    Star imports conservatively contribute as if the name were imported."""
    mod_imports = imported_names.get(module_name, {})
    consumers = set(mod_imports.get(name, set()))
    consumers |= mod_imports.get('*', set())
    return len(consumers), consumers


# ============================================================
# PROVENANCE UNIT MODEL
# ============================================================

# ============================================================
# CITATION BLOCK INHERITANCE (L-156 Gap item 6, Phase 1c)
# ============================================================
# Citations in this codebase attach at the block level: a comment run
# above a dict entry covers the whole body block below it. The string
# extractor walks each string with its own flat lookback window and
# cannot see that. These helpers close the gap structurally -- by
# containment, not by widening the window.
#
# Distance is deliberately NOT the discriminator here. shell_configs.py
# and idealized_orbits.py have overlapping citation-gap distributions,
# so no threshold separates "inside a cited block" from "happens to have
# a citation somewhere above." Widening the window is not a smaller
# version of this fix; it is a different and wrong one.

# Lookback from a block's opening line up to its citation comment run.
# 8 lines covers every cited block in shell_configs.py. 15 covers
# jupiter_visualization_shells.py's function-local ring_params (citation
# at line 897, assignment opens at 906) with margin, and is applied above
# both the block key and the enclosing assignment.
CITATION_LOOKBACK_BLOCK = 15

# An author may explicitly narrow what a citation covers. Where this
# marker appears in a captured run, the scanner declines to inherit and
# flags the block for review instead. Inheriting past a comment that says
# "colors below are developer-selected" would be the scanner asserting
# provenance the author disclaimed -- the same failure class as a
# "# Source:" over recalled data, pointed the other way.
SCOPE_DECLARATION_RE = re.compile(r'Scope of the above citation:',
                                  re.IGNORECASE)

# Blocks whose citation carries a scope declaration. Collected during
# extraction and reported after the scan so they stay visible rather
# than silently doing nothing.
SCOPE_DECLARED_BLOCKS = []

# L-174 diagnostics. Neither affects scoring; both exist so that a
# citation pitched at the wrong LEVEL is visible instead of silent.
#
# Strict containment means the resolver reads exactly one block: the
# narrowest one containing the string. A citation written one level too
# far out is therefore invisible to it, and -- because the flat 60-line
# context window usually catches the string anyway -- the mismatch does
# not show up as a finding. It shows up as nothing at all, until someone
# moves a few lines and it quietly becomes a real gap.
#
# SHADOWED_STRINGS: narrowest containing block uncited, an outer
#   containing block cited. This is the ring_params shape.
# DEEP_CITATIONS: a dict nested 3+ levels deep carrying its own
#   citation. The block table records only depth 1 (the assignment) and
#   depth 2 (its direct dict-valued entries), so such a citation cannot
#   be reached and its strings would inherit the depth-2 citation
#   instead -- "innermost wins" failing one level down. None exist
#   today; this is a tripwire, not a backlog.
SHADOWED_STRINGS = []
DEEP_CITATIONS = []


def citation_run_above(lines, decl_line, lookback=CITATION_LOOKBACK_BLOCK):
    """Find the citation comment run immediately above a declaration.

    Searches up to `lookback` lines above `decl_line` for a line matching
    a citation pattern, then expands to the whole contiguous comment run
    around it. Capturing the run rather than the matched line matters:
    for shell_configs.py's Moon block the pattern matches a CONTINUATION
    line, not the "# Source:" head, and recording only the matched line
    would put a fragment in the report and lose the sources named on the
    other lines.

    Stops at the first line that is neither blank nor a comment, so a
    citation belonging to a previous block is never picked up.

    Returns (citation_line, citation_text), or (None, None).
    """
    i = decl_line - 2
    limit = max(-1, decl_line - 2 - lookback)
    while i > limit:
        text = lines[i]
        if has_citation(text):
            top = i
            while top - 1 >= 0 and lines[top - 1].lstrip().startswith('#'):
                top -= 1
            bottom = i
            while (bottom + 1 < len(lines)
                   and lines[bottom + 1].lstrip().startswith('#')):
                bottom += 1
            return i + 1, ''.join(lines[top:bottom + 1])
        if text.strip() and not text.lstrip().startswith('#'):
            break
        i -= 1
    return None, None


def build_citation_block_table(tree, lines, fname=None):
    """Record every dict block in a file and the citation above it.

    One ast.walk pass over every ast.Assign at ANY nesting depth. Depth
    matters: shell_configs.py's dicts are module-level, but
    jupiter_visualization_shells.py's ring_params is function-local, and
    a module-level-only walk misses it entirely.

    Two block shapes are recorded, because citations attach to both:
      - 'assign': the whole dict assignment, cited above its first line
      - 'entry':  one dict-valued entry, cited above its key line

    Blocks are keyed by LINE RANGE, not by name. That is what makes
    cross-dict inheritance impossible: SHELL_CONFIGS['Jupiter'] and
    CUSTOM_SHELLS['Jupiter'] carry different citations and occupy
    disjoint spans, so neither can reach the other's.
    """
    blocks = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if not isinstance(node.value, ast.Dict):
            continue

        dict_name = target.id
        assign_start = node.lineno
        assign_end = (getattr(node.value, 'end_lineno', assign_start)
                      or assign_start)
        cite_line, cite_text = citation_run_above(lines, assign_start)
        blocks.append({
            'dict_name': dict_name, 'key': None, 'kind': 'assign',
            'start': assign_start, 'end': assign_end,
            'citation_line': cite_line, 'citation_text': cite_text,
        })

        for key, value in zip(node.value.keys, node.value.values):
            if key is None:
                continue
            if not (isinstance(key, ast.Constant)
                    and isinstance(key.value, str)):
                continue
            if not isinstance(value, ast.Dict):
                continue
            entry_start = key.lineno
            entry_end = (getattr(value, 'end_lineno', entry_start)
                         or entry_start)
            k_line, k_text = citation_run_above(lines, entry_start)
            blocks.append({
                'dict_name': dict_name, 'key': key.value, 'kind': 'entry',
                'start': entry_start, 'end': entry_end,
                'citation_line': k_line, 'citation_text': k_text,
            })

    for block in blocks:
        if block['citation_text'] and SCOPE_DECLARATION_RE.search(
                block['citation_text']):
            SCOPE_DECLARED_BLOCKS.append((
                fname or '<unknown>', block['dict_name'], block['key'],
                block['start'], block['end'], block['citation_line']))

    _record_deep_citations(tree, lines, fname)

    return blocks


def _record_deep_citations(tree, lines, fname=None):
    """Flag dicts nested 3+ deep that carry their own citation.

    build_citation_block_table records depth 1 and depth 2 only. A
    citation written above a depth-3 key is therefore unreachable: the
    resolver will hand that string the depth-2 citation instead, which
    is a real misattribution and invisible in the tier counts.

    Nothing in the repo triggers this today. It is recorded rather than
    handled because the honest fix is to extend the table, and doing
    that speculatively for a population of zero would add depth to the
    project's measurement instrument for no measured need.
    """
    def descend(dict_node, depth, name, keypath):
        for key, value in zip(dict_node.keys, dict_node.values):
            if key is None:
                continue
            if not (isinstance(key, ast.Constant)
                    and isinstance(key.value, str)):
                continue
            if not isinstance(value, ast.Dict):
                continue
            path = keypath + [key.value]
            if depth + 1 >= 3:
                cite_line, cite_text = citation_run_above(lines, key.lineno)
                if cite_text:
                    DEEP_CITATIONS.append((
                        fname or '<unknown>', name, list(path),
                        depth + 1, key.lineno, cite_line))
            descend(value, depth + 1, name, path)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        if not isinstance(node.targets[0], ast.Name):
            continue
        if not isinstance(node.value, ast.Dict):
            continue
        descend(node.value, 1, node.targets[0].id, [])


def find_shadowing_block(blocks, line_start, line_end):
    """Return the outer cited block a string is shadowed FROM, or None.

    Shadowed means: the narrowest block containing this string has no
    citation, but some wider containing block does. The resolver
    correctly declines to inherit -- that strictness is what protects
    L-173 -- but the author almost certainly meant the outer citation to
    cover this content, so it is worth reporting.

    Reporting is all this does. Scoring is unchanged.
    """
    containing = [b for b in blocks
                  if b['start'] <= line_start and line_end <= b['end']]
    if len(containing) < 2:
        return None
    containing.sort(key=lambda b: (b['end'] - b['start'], b['start']))
    if containing[0]['citation_text']:
        return None
    for block in containing[1:]:
        if block['citation_text']:
            return block
    return None


def resolve_block_citation(blocks, line_start, line_end):
    """Return the citation a string at these lines inherits, or None.

    Takes the NARROWEST block containing the string and stops there.
    If that block has no citation of its own, the string inherits
    nothing -- the resolver does NOT continue outward to an enclosing
    dict or to the module.

    That stopping rule is the whole point. Searching outward would let
    SHELL_CONFIGS['Pluto'] (genuinely uncited, 10 findings) pick up a
    citation from SHELL_CONFIGS itself the moment anyone adds one,
    silently clearing findings whose real problem is a missing source.
    Those blocks are tracked as L-173 and need actual sourcing, not a
    scoring change.

    Returns (citation_text, declined), where `declined` is True when the
    resolved citation carries an explicit scope declaration.
    """
    containing = [b for b in blocks
                  if b['start'] <= line_start and line_end <= b['end']]
    if not containing:
        return None, False

    containing.sort(key=lambda b: (b['end'] - b['start'], b['start']))
    block = containing[0]

    if not block['citation_text']:
        return None, False
    if SCOPE_DECLARATION_RE.search(block['citation_text']):
        return None, True
    return block['citation_text'], False


class ProvenanceUnit:
    """The smallest thing that has a coherent source citation.

    Three kinds:
      - 'constant':  a module-level UPPER_CASE or Title_Case assignment
      - 'dict':      a module-level dict literal assignment
      - 'string':    a single string literal containing numeric claims
    """

    __slots__ = [
        'kind', 'module', 'file', 'name', 'line_start', 'line_end',
        'context_text',        # text the unit sees for citation lookup
        'raw_value',           # for strings: the actual string content (for suppression matching)
        'entries',             # for dicts: [(key_name, value, value_str, line)]
        'numeric_claims',      # for strings: [(num_str, unit, value)]
        'value',               # for constants: the numeric value
        'value_str',
        'vuln', 'vuln_reason',
        'crit', 'crit_reason',
        'score',
        'role', 'consumer_count', 'consumers',
        'is_docstring',        # for strings: True if this is a module/class/func docstring
        'inherited_citation',  # for strings: citation text of the containing block
        'scope_declined',      # for strings: containing block's citation is scope-limited
    ]

    def __init__(self, **kwargs):
        for k in self.__slots__:
            setattr(self, k, kwargs.get(k, None))
        if self.entries is None:
            self.entries = []
        if self.numeric_claims is None:
            self.numeric_claims = []
        if self.consumers is None:
            self.consumers = set()

    def compute_score(self):
        if self.vuln and self.crit:
            self.score = self.vuln * self.crit
        else:
            self.score = 0

    @property
    def display_name(self):
        if self.kind == 'dict':
            return f"{self.name}[...]" if self.name else "<anonymous dict>"
        if self.kind == 'string':
            return f"display string @ line {self.line_start}"
        return self.name or "<anonymous>"

    @property
    def short_value(self):
        if self.kind == 'constant':
            return str(self.value_str) if self.value_str else str(self.value)
        if self.kind == 'dict':
            n = len(self.entries)
            return f"({n} entr{'y' if n == 1 else 'ies'})"
        if self.kind == 'string':
            n = len(self.numeric_claims)
            return f"({n} claim{'s' if n != 1 else ''})"
        return ''


# ============================================================
# CONTEXT BLOCK EXTRACTION
# ============================================================

def get_context_block(lines, unit_start_line, unit_end_line=None,
                      lookback=30, lookahead=15):
    """Return the block of text a unit can see for citation purposes.

    Looks both directions from the unit:
      - `lookback` lines BEFORE the unit (for section-header citations)
      - the unit's declaration itself
      - `lookahead` lines AFTER the unit (for trailing `# Source:` comments,
        which is this codebase's dominant convention)

    Both directions matter. constants_new.py places citations AFTER the
    declaration ("KM_PER_AU = 149597870.7\\n# Source: IAU 2012 ..."),
    but section headers and dict-level citations tend to be ABOVE.
    """
    if unit_end_line is None:
        unit_end_line = unit_start_line
    start = max(0, unit_start_line - 1 - lookback)
    end = min(len(lines), unit_end_line + lookahead)
    return ''.join(lines[start:end])


def get_unit_interior(lines, line_start, line_end):
    """Return the text inside the unit itself (per-entry comments)."""
    start = max(0, line_start - 1)
    end = min(len(lines), line_end)
    return ''.join(lines[start:end])


# ============================================================
# AST-BASED UNIT EXTRACTION
# ============================================================

CONSTANT_NAME_SKIP = {
    'Path', 'Optional', 'Dict', 'List', 'Tuple', 'Set', 'Union',
    'Any', 'Callable', 'Iterator', 'Sequence', 'Mapping',
    'TYPE_CHECKING',
}


def extract_numeric_value(node):
    """Evaluate an AST node to a numeric constant.
    Returns (value, display_str) or (None, None) if not numeric."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(
                node.value, bool):
            return node.value, str(node.value)
        return None, None
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        v, s = extract_numeric_value(node.operand)
        if v is not None:
            return -v, f"-{s}"
    if isinstance(node, ast.BinOp):
        try:
            v = eval(compile(ast.Expression(node), '<eval>', 'eval'))
            if isinstance(v, (int, float)):
                src = ast.unparse(node) if hasattr(ast, 'unparse') else str(v)
                return v, src
        except Exception:
            return None, None
    return None, None


def extract_units_from_file(filepath, module_name, role):
    """Walk the AST of one file and emit ProvenanceUnits.

    Emits:
      - 'constant' units for top-level numeric assignments
      - 'dict' units for top-level dict literal assignments
      - 'string' units for string literals containing numeric claims
        (only in files expected to carry public-facing narrative)
    """
    units = []

    try:
        with open(filepath, 'rb') as f:
            source_bytes = f.read()
        tree = ast.parse(source_bytes)
    except Exception:
        return units

    try:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
    except Exception:
        return units

    fname = os.path.basename(filepath)

    # ---- Top-level assignments: constants and dicts ----
    for node in ast.iter_child_nodes(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        name = target.id

        if isinstance(node.value, ast.Dict):
            unit = _make_dict_unit(node, name, lines, module_name,
                                    fname, role)
            if unit is not None:
                units.append(unit)
            continue

        # Numeric constant? Only UPPER_CASE / Title_Case names.
        looks_like_constant = (name.isupper() or
                               (name[0].isupper() and '_' in name))
        if not looks_like_constant:
            continue
        if name in CONSTANT_NAME_SKIP:
            continue

        value, value_str = extract_numeric_value(node.value)
        if value is None:
            continue

        line_start = node.lineno
        line_end = getattr(node, 'end_lineno', line_start) or line_start
        context_text = get_context_block(lines, line_start, line_end,
                                         lookback=30, lookahead=15)

        units.append(ProvenanceUnit(
            kind='constant',
            module=module_name,
            file=fname,
            name=name,
            line_start=line_start,
            line_end=line_end,
            context_text=context_text,
            value=value,
            value_str=value_str,
            role=role,
        ))

    # ---- String literals with numeric claims ----

    narrative_files = {
        'constants_new', 'info_dictionary', 'celestial_objects',
        'spacecraft_encounters', 'close_approach_data',
        'exoplanet_systems', 'exoplanet_stellar_properties',
        'sgr_a_star_data', 'star_notes', 'solar_visualization_shells',
        'food_insecurity_generator',
    }
    # L-078 check 1: role-driven inclusion, additive over the legacy
    # allow-list -- nothing currently covered loses coverage; the
    # allow-list becomes a pure safety net once module_atlas.ROLE_MAP
    # is complete (food_insecurity_generator still shows 'other' there
    # today, which is why this stays additive rather than a replace).
    NARRATIVE_ROLES = {'data', 'scenario', 'rendering', 'rendering/shells',
                        'computation'}
    is_shell_file = module_name.endswith('_visualization_shells')
    is_narrative_role = role in NARRATIVE_ROLES
    if module_name in narrative_files or is_shell_file or is_narrative_role:
        # Phase 1c: containment table for block-citation inheritance.
        block_table = build_citation_block_table(tree, lines, fname)
        units.extend(_extract_string_units(
            tree, lines, module_name, fname, role, block_table))

    return units


def _make_dict_unit(assign_node, name, lines, module_name, fname, role):
    """Build a ProvenanceUnit for a top-level dict assignment."""
    dict_node = assign_node.value
    if not isinstance(dict_node, ast.Dict):
        return None

    line_start = assign_node.lineno
    line_end = getattr(dict_node, 'end_lineno', line_start) or line_start
    # For dicts the interior is captured separately; use the declaration
    # line as both start/end for lookahead so we catch trailing
    # `# Source:` comments that follow the closing brace.
    context_text = get_context_block(lines, line_start, line_end,
                                     lookback=30, lookahead=10)
    interior_text = get_unit_interior(lines, line_start, line_end)

    entries = []
    for key, val in zip(dict_node.keys, dict_node.values):
        if key is None:  # ** unpacking
            continue
        if not (isinstance(key, ast.Constant) and isinstance(key.value, str)):
            continue
        key_name = key.value
        num_value, num_str = extract_numeric_value(val)
        if num_value is None:
            # Accept None / other AST-constant values (e.g. period=None for
            # hyperbolic comets). Skip non-constants (colors as RGB tuples,
            # nested dicts, etc).
            if isinstance(val, ast.Constant):
                num_value = val.value
                num_str = repr(val.value) if val.value is not None else 'None'
            else:
                continue
        entry_line = getattr(val, 'lineno', line_start)
        entries.append((key_name, num_value, num_str, entry_line))

    if not entries:
        return None

    return ProvenanceUnit(
        kind='dict',
        module=module_name,
        file=fname,
        name=name,
        line_start=line_start,
        line_end=line_end,
        context_text=context_text + '\n' + interior_text,
        entries=entries,
        role=role,
    )


def _extract_string_units(tree, lines, module_name, fname, role,
                          block_table=None):
    """Find string literals containing numeric claims. One string = one unit.

    Module/class/function docstrings are treated specially: their own text
    is included in the citation-search scope, so a docstring that mentions
    "Verified", "Source:", "per NASA", etc. is treated as self-cited.
    """
    # Identify docstring string nodes by position (first stmt of module /
    # class / function whose value is a Constant str).
    docstring_lines = set()

    def _collect_docstrings(n):
        body = getattr(n, 'body', None)
        if body and body:
            first = body[0]
            if (isinstance(first, ast.Expr) and
                isinstance(first.value, ast.Constant) and
                isinstance(first.value.value, str)):
                docstring_lines.add(first.value.lineno)
        for child in ast.iter_child_nodes(n):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef,
                                   ast.ClassDef, ast.Module)):
                _collect_docstrings(child)

    _collect_docstrings(tree)

    units = []
    seen_lines = set()
    seen_content_hashes = set()  # Option B: deduplicate var=(text)/'description':(text) pattern

    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant):
            continue
        if not isinstance(node.value, str):
            continue
        s = node.value
        if len(s) < 3:
            continue
        claims = list(extract_numeric_claims(s))
        if not claims:
            continue

        line_start = node.lineno
        if line_start in seen_lines:
            continue
        seen_lines.add(line_start)
        line_end = getattr(node, 'end_lineno', line_start) or line_start

        # Option B: Deduplicate -- same string content appearing at two
        # locations in the same file (standalone variable + dict 'description'
        # key) is the standard shell file pattern. First occurrence wins;
        # subsequent identical content is suppressed. Uses first 200 chars
        # as key -- specific enough, fast enough.
        content_key = s[:200]
        if content_key in seen_content_hashes:
            continue
        seen_content_hashes.add(content_key)

        # If this string is a docstring, include its own text in the
        # citation-search scope (docstrings self-contextualize).
        #
        # Lookback=60: info_dictionary.py INFO strings can be 50-100 lines
        # long. With lookback=30, continuation lines deep in a long entry
        # fall outside the citation window even when `# Source:` sits just
        # above the entry key. 60 lines covers the longest INFO entries
        # without false-positives in shorter files.
        # Known residual: very long entries (Apollo 11 S-IVB, Halley,
        # Artemis II) may still generate mid-string false positives if the
        # entry itself exceeds 60 lines. These are accepted scanner
        # limitations -- the citation exists at the entry key level.
        base_context = get_context_block(lines, line_start, line_end,
                                         lookback=60, lookahead=10)
        # L-078: self-contextualize ALL string units, not just docstrings.
        # The unit-of-provenance is the whole string either way; a
        # narrative display string (scenario briefing, KMZ balloon) is
        # exactly as much "what the reader sees" as a docstring is, and
        # an inline SOURCE: marker at its end is a real citation -- it
        # was only invisible before because this text was never part of
        # the searched context for non-docstring strings.
        context_text = base_context + '\n' + s

        # Phase 1c: does an enclosing cited dict block cover this string?
        inherited_citation = None
        scope_declined = False
        if block_table:
            inherited_citation, scope_declined = resolve_block_citation(
                block_table, line_start, line_end)
            # L-174: diagnostic only, no effect on scoring.
            if inherited_citation is None and not scope_declined:
                shadowing = find_shadowing_block(
                    block_table, line_start, line_end)
                if shadowing is not None:
                    SHADOWED_STRINGS.append((
                        fname, line_start, shadowing['dict_name'],
                        shadowing['key'], shadowing['citation_line']))

        units.append(ProvenanceUnit(
            kind='string',
            module=module_name,
            file=fname,
            name=None,
            line_start=line_start,
            line_end=line_end,
            context_text=context_text,
            raw_value=s,           # stored for suppression fingerprint matching
            numeric_claims=claims,
            role=role,
            is_docstring=(line_start in docstring_lines),
            inherited_citation=inherited_citation,
            scope_declined=scope_declined,
        ))

    return units


# ============================================================
# OPTION A: PINNED CONSTANT CROSS-REFERENCE
# ============================================================

# ============================================================
# SHADOW CONSTANTS (L-156 Gap item 5 / L-158; 1d piece 1)
# ============================================================
# A module that hand-types a value already defined and cited in
# constants_new.py has made a frozen copy. The number may be correct
# today; the problem is that it will not follow if the source is ever
# corrected, and it sits outside the citation chain in the meantime.
# provenance-discipline v1.3 makes this a [CRITICAL] convention: delete
# the local definition and import the real one. Never add a "# Source:"
# comment to a local copy -- that cites-to-clear a structural problem.
#
# Detection matches on NAME AND VALUE TOGETHER. Measured repo-wide at
# the time this was written: name+value returns exactly the two known
# direct instances and nothing else; value alone returns 77 candidates,
# almost all coincidental round numbers (0.5, 2.2, 10.0) that happen to
# equal some pinned constant. Value alone is not a usable signal.
#
# This is a DIAGNOSTIC. It does not change any unit's score. The
# constants involved are function-local assignments, which the scanner
# does not extract as units at all, so there is no score to change --
# see the as-built for why Option A was left alone.

# A derived shadow is an expression built from pinned literals, e.g.
# SUN_RADIUS_AU = 695700.0 / 149597870.7. Requiring at least one
# literal of this magnitude excludes trivial coincidences: without it,
# an expression containing 2 twice matches, because 2.0 is itself a
# pinned value.
SHADOW_DERIVED_MIN_MAGNITUDE = 100.0

SHADOW_CONSTANTS = []


def _numeric_from_node(node):
    """Return the float value of a numeric literal node, or None."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) \
            and not isinstance(node.value, bool):
        return float(node.value)
    if (isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub)
            and isinstance(node.operand, ast.Constant)
            and isinstance(node.operand.value, (int, float))):
        return -float(node.operand.value)
    return None


def constant_has_own_citation(lines_c, lineno, source_re):
    """Does the constant assigned at `lineno` carry its OWN citation?

    Single source of truth for this question. Both build_pinned_values()
    and build_cited_constant_names() route through here, because two
    functions in one file answering "is this cited" by different rules
    is how the scanner ends up disagreeing with itself.

    The rule is CONTIGUITY, not distance. A citation counts only if it
    sits in a comment run physically touching the assignment -- a blank
    line ends the run. Distance windows do not work here: a window wide
    enough to catch a real citation is also wide enough to reach the
    NEXT constant's citation, and then an uncited value silently
    inherits provenance it never had.

    Both conventions in this codebase are accepted, because both are in
    use. constants_new.py writes the citation BELOW the assignment:

        KM_PER_AU = 149597870.7
        # Source: IAU 2012 Resolution B2

    while the rest of the repo writes it above. Below is checked first,
    since that is the convention of the file this predicate is applied
    to most often.

    `lines_c` is the file's lines with line endings kept; `lineno` is the
    1-based AST line number; `source_re` is the caller's citation
    pattern.
    """
    # Below: a comment run starting on the very next line. No blank may
    # intervene -- that is what keeps the next constant's citation out.
    idx = lineno
    while idx < len(lines_c) and lines_c[idx].lstrip().startswith('#'):
        if source_re.search(lines_c[idx]):
            return True
        idx += 1

    # Above: walk up through comments and blanks, stopping at the first
    # line of code, which is the previous assignment.
    idx = lineno - 2
    while idx >= 0:
        line = lines_c[idx]
        if source_re.search(line):
            return True
        if line.strip() and not line.lstrip().startswith('#'):
            break
        idx -= 1

    return False


def build_cited_constant_names(project_dir):
    """Map NAME -> value for cited numeric constants in constants_new.py.

    build_pinned_values() returns values only, which is enough to ask
    "does this number appear upstream" but not "is this the same
    constant." The name is what separates a frozen copy from a
    coincidence, so it has to be carried.
    """
    path = os.path.join(project_dir, 'constants_new.py')
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'rb') as f:
            content = f.read()
        lines_c = content.decode('utf-8', errors='replace').splitlines(
            keepends=True)
        tree = ast.parse(content)
    except Exception:
        return {}

    source_re = re.compile(r'#\s*[Ss]ource\s*:', re.IGNORECASE)
    named = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or not target.id.isupper():
            continue
        num = _numeric_from_node(node.value)
        if num is None:
            continue
        if constant_has_own_citation(lines_c, node.lineno, source_re):
            named[target.id] = num
    return named


def scan_shadow_constants(project_dir, cited_names, pinned_values):
    """Populate SHADOW_CONSTANTS with local copies of cited constants.

    Walks every assignment at ANY nesting depth, because the known
    instances are function-local -- extract_units_from_file only reads
    top-level assignments, so these are invisible to the normal unit
    pipeline.

    Two shapes:
      'direct'  -- NAME = <literal>, where NAME is a cited constant in
                   constants_new.py and the value agrees.
      'derived' -- NAME = <expression of literals>, where every literal
                   matches a pinned value and at least one is large
                   enough not to be a coincidence.
    """
    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py') or fname == 'constants_new.py':
            continue
        path = os.path.join(project_dir, fname)
        try:
            with open(path, 'rb') as f:
                tree = ast.parse(f.read())
        except Exception:
            continue

        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign) or len(node.targets) != 1:
                continue
            target = node.targets[0]
            if not isinstance(target, ast.Name):
                continue
            name = target.id

            num = _numeric_from_node(node.value)
            if num is not None:
                upstream = cited_names.get(name)
                if upstream is not None and abs(num - upstream) < 1e-9:
                    SHADOW_CONSTANTS.append(
                        (fname, node.lineno, name, 'direct', num))
                continue

            if isinstance(node.value, ast.BinOp) and name.isupper():
                literals = []
                ok = True
                for sub in ast.walk(node.value):
                    val = None
                    if isinstance(sub, ast.Constant) and isinstance(
                            sub.value, (int, float)) and not isinstance(
                            sub.value, bool):
                        val = float(sub.value)
                    if val is None:
                        continue
                    literals.append(val)
                    if round(val, 3) not in pinned_values:
                        ok = False
                        break
                if (ok and len(literals) >= 2
                        and any(abs(v) >= SHADOW_DERIVED_MIN_MAGNITUDE
                                for v in literals)):
                    SHADOW_CONSTANTS.append(
                        (fname, node.lineno, name, 'derived', None))


def build_pinned_values(project_dir):
    """Extract numeric values from constants_new.py that have source citations.

    Returns a set of rounded float values. A display string whose numeric
    claims all match pinned values is treated as V_SOURCED (cited by
    reference to the pinned constant) rather than V_RECALLED.

    Only constants with a nearby # Source: comment are included --
    prevents laundering of uncited constants.
    """
    constants_path = os.path.join(project_dir, 'constants_new.py')
    if not os.path.exists(constants_path):
        return set()
    try:
        with open(constants_path, 'rb') as f:
            content = f.read()
        lines_c = content.decode('utf-8', errors='replace').splitlines(keepends=True)
        tree = ast.parse(content)
    except Exception:
        return set()

    pinned = set()
    SOURCE_RE = re.compile(r'#\s*[Ss]ource\s*:', re.IGNORECASE)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if not target.id.isupper():
            continue
        val = node.value
        if isinstance(val, ast.Constant) and isinstance(val.value, (int, float)):
            num = float(val.value)
        elif (isinstance(val, ast.UnaryOp) and isinstance(val.op, ast.USub)
              and isinstance(val.operand, ast.Constant)):
            num = -float(val.operand.value)
        else:
            continue
        # Was a flat window of 10 lines above and 5 below, which could
        # reach past this constant onto a neighbour's citation. Now the
        # same predicate build_cited_constant_names() uses, so the two
        # cannot disagree about what "cited" means.
        if constant_has_own_citation(lines_c, node.lineno, SOURCE_RE):
            # Store at multiple precisions to match how hover text rounds
            for prec in (0, 1, 2, 3):
                pinned.add(round(num, prec))

    return pinned


# ============================================================
# SCORING
# ============================================================

def classify_criticality(unit):
    """Classify a constant/dict unit into a D1 criticality category.

    Returns (crit, crit_reason). Match order is significant:

        role veto -> cosmetic -> absolute-override -> relational
                  -> measured -> internal(name) -> same four on entry KEYS
                  -> measured(role) -> undetermined

    Name before keys is deliberate: a dict's entry keys are usually its
    DOMAIN (body names, module names), not the quantity it stores.
    Classifying CENTER_BODY_RADII from its keys would read "Mercury",
    not "radii".
    """
    numeric_entries = any(
        isinstance(v, (int, float)) and not isinstance(v, bool)
        for _, v, _, _ in (unit.entries or []))

    role = unit.role or ''
    # Role VETO. A devtool/gui/cache module does not hold claims about the
    # world, so a generic physical stem must not promote its parameters.
    # Measured during the 1a build: without this, HUB_THRESHOLD ('threshold'),
    # MAX_DATA_AGE_DAYS ('_days') and PERFRAME_INDICATOR_RADIUS_FACTOR
    # ('radius') all scored MEASURED and put uncited tool config into Tier 1.
    if role in CRIT_INTERNAL_ROLES:
        return C_INTERNAL, f"Internal (role '{role}')"

    cat = _crit_by_vocabulary(unit.name or '', unit.kind, numeric_entries)
    src = 'name'
    if cat is None:
        for key, _, _, _ in (unit.entries or []):
            cat = _crit_by_vocabulary(key, unit.kind, numeric_entries)
            if cat is not None:
                src = 'key'
                break
    if cat is None:
        if role in CRIT_PHYSICAL_ROLES:
            return C_MEASURED, f"MEASURED (inferred from role '{role}')"
        return C_UNDETERMINED, "UNDETERMINED -- could not be classified"

    if cat == 'cosmetic':
        return C_COSMETIC, f"Cosmetic ({src} vocabulary)"
    if cat == 'relational':
        return C_RELATIONAL, f"RELATIONAL -- defined against a tracked base ({src})"
    if cat == 'measured':
        return C_MEASURED, f"MEASURED -- independently catalogued fact ({src})"
    return C_INTERNAL, f"Internal use ({src} vocabulary)"


def _crit_by_vocabulary(name, kind, numeric_entries):
    """Match one name against the criticality vocabulary. None = no match."""
    if _vocab_hit(name, CRIT_COSMETIC_STEMS):
        # D2 cosmetic gate: the name heuristic alone is not enough. A dict
        # named "colors" that holds numbers stops being waved through.
        if not (kind == 'dict' and numeric_entries):
            return 'cosmetic'
    if name in CRIT_ABSOLUTE_OVERRIDE:
        return 'measured'
    if _vocab_hit(name, CRIT_RELATIONAL_STEMS):
        return 'relational'
    if _vocab_hit(name, CRIT_MEASURED_STEMS):
        return 'measured'
    if _vocab_hit(name, CRIT_INTERNAL_STEMS):
        return 'internal'
    return None


def _vocab_hit(name, stems):
    """Token-aware stem match.

    Tokens, not substrings: PAGES_CEILING_MB must not match the stem 'age',
    and TEMPLATE must not match 'temp'. A stem written with a leading
    underscore matches the FINAL token only, so '_km' reads as a unit suffix
    rather than an anywhere-match.
    """
    tokens = [t for t in (name or '').lower().replace('-', '_').split('_') if t]
    if not tokens:
        return False
    for stem in stems:
        if stem.startswith('_'):
            if tokens[-1] == stem[1:]:
                return True
        else:
            for tok in tokens:
                if tok == stem or (tok.startswith(stem)
                                   and len(tok) - len(stem) <= 2):
                    return True
    return False


def score_unit(unit, imported_names):
    """Assign vulnerability and criticality to a unit.

    Vulnerability answers one question: does a citation exist for this
    claim? Nothing else may substitute for it. Two mechanisms that once
    did were retired in D8.5 -- see the note above the ladder below.
    """
    # ---- Vulnerability ----
    text = unit.context_text or ''
    is_doc = bool(unit.is_docstring)
    cited = has_citation(text, is_docstring=is_doc)
    stale = has_stale_marker(text)

    # D8.5 -- two mechanisms removed here, both of the same class.
    #
    # OPTION A granted V_SOURCED to an uncited display string when all
    # its numeric claims matched values pinned from constants_new.py. A
    # value match proves two numbers are equal; it does not prove anyone
    # consulted a source. Suspicious matches are still reported, by the
    # shadow-constant detector, as a DIAGNOSTIC -- which tells you to go
    # look, where a score told you not to bother.
    #
    # STALE-ONLY CREDIT granted V_SOURCED to a unit with no citation at
    # all whenever its text carried a staleness marker ("as of 2024",
    # "Planned"). Its own reason string read "No source, contains
    # date-sensitive claims" -- the scanner stating there was no source
    # and scoring it as though there were. A staleness marker is
    # evidence a claim will EXPIRE, not evidence it was ever sourced;
    # if anything it belongs on the other side of the ladder.
    #
    # Both predate the D3 ladder, when V_SOURCED meant something looser
    # than "a citation exists." Under the ladder 1b landed it means
    # "cited, never independently cross-checked," and neither of these
    # can claim the first half of that.
    #
    # Staleness is still DETECTED and still reported in the reason,
    # which is where it was always the useful information -- it just no
    # longer moves the score on its own.
    if cited and stale:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not cross-checked; date-sensitive"
    elif cited:
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited, not independently cross-checked"
    elif unit.inherited_citation:
        # Phase 1c: the string sits inside a dict block that carries its
        # own citation. Inheriting is not clearing -- V_SOURCED means
        # "cited, never independently cross-checked," same rung L-158
        # gave derived values.
        unit.vuln = V_SOURCED
        unit.vuln_reason = "Cited via enclosing block citation"
    elif stale:
        # No citation, and the text says it will go out of date. V4,
        # with the staleness carried in the reason.
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation; date-sensitive (recalled)"
    else:
        unit.vuln = V_RECALLED
        unit.vuln_reason = "No source citation (recalled)"

    # ---- Criticality ----
    # D1: criticality is now by claim TYPE, not by import volume. Consumer
    # count is still resolved and still reported (blast radius is useful
    # information) but it no longer sets the score.
    if unit.kind == 'string':
        unit.crit = C_PUBLIC
        unit.crit_reason = "Public-facing display string (hover/INFO)"
    elif unit.kind in ('constant', 'dict') and unit.name:
        count, consumers = name_is_imported(
            unit.name, unit.module, imported_names)
        unit.consumer_count = count
        unit.consumers = consumers
        unit.crit, unit.crit_reason = classify_criticality(unit)
    else:
        unit.crit, unit.crit_reason = _role_based_criticality(unit)

    unit.compute_score()


def _role_based_criticality(unit):
    """Fallback criticality when per-name resolution doesn't apply."""
    if unit.kind == 'dict' and unit.name:
        lname = unit.name.lower()
        if lname in ('colors',) or 'label' in lname or 'color' in lname:
            return C_COSMETIC, f"Cosmetic dictionary ({unit.name})"

    role = unit.role or ''
    if unit.kind == 'dict' and role.startswith('rendering'):
        return C_LOADBEARING, f"Geometry dict in {role} module"

    if unit.kind == 'constant' and role in ('computation', 'data'):
        return C_LOADBEARING, f"Numeric constant in {role} module"

    return C_INTERNAL, "Internal use (not imported externally)"


# ============================================================
# DUPLICATE / INCONSISTENCY DETECTION
# ============================================================
# Hand-curated aliases avoid both false positives and false negatives.
# Same-spelled names across files are caught; deliberately different
# names (CENTER_BODY_RADII_KM shadow) are NOT caught here -- that
# requires shadow detection (planned separately).

CONCEPT_ALIASES = {
    # Map canonical concept name -> tuple of exact name matches.
    # Matching is done by checking if the constant NAME equals any alias
    # (substring matching is too loose -- SPEED_OF_LIGHT_KM_S would
    # collide with SPEED_OF_LIGHT even though they're in different units).
    'SOLAR_RADIUS_KM':   ('SOLAR_RADIUS_KM', 'SUN_RADIUS_KM'),
    'SOLAR_RADIUS_AU':   ('SOLAR_RADIUS_AU', 'SUN_RADIUS_AU'),
    'KM_PER_AU':         ('KM_PER_AU', 'AU_TO_KM', 'AU_IN_KM'),
    'EARTH_RADIUS_KM':   ('EARTH_RADIUS_KM', 'EARTH_EQUATORIAL_RADIUS_KM'),
    'SPEED_OF_LIGHT_M_S': ('SPEED_OF_LIGHT',),  # m/s variant
    'SPEED_OF_LIGHT_KM_S': ('SPEED_OF_LIGHT_KM_S', 'C_KM_S'),
    'OBLIQUITY':         ('OBLIQUITY', 'EARTH_OBLIQUITY'),
    'LIGHT_MINUTES_PER_AU': ('LIGHT_MINUTES_PER_AU',),
    'JUPITER_RADIUS_KM': ('JUPITER_RADIUS_KM', 'JUPITER_EQUATORIAL_RADIUS_KM'),

    # L-162 (2026-07-29): the 14 bodies newly promoted from
    # CENTER_BODY_RADII dict entries to named constants. No known
    # alternate name exists elsewhere in the repo for any of these today
    # (checked); each is registered under its own canonical name so a
    # future differently-named duplicate has an anchor to be caught
    # against, per the design's hard requirement.
    'MERCURY_RADIUS_KM':  ('MERCURY_RADIUS_KM',),
    'VENUS_RADIUS_KM':    ('VENUS_RADIUS_KM',),
    'MOON_RADIUS_KM':     ('MOON_RADIUS_KM',),
    'MARS_RADIUS_KM':     ('MARS_RADIUS_KM',),
    'PHOBOS_RADIUS_KM':   ('PHOBOS_RADIUS_KM',),
    'SATURN_RADIUS_KM':   ('SATURN_RADIUS_KM',),
    'URANUS_RADIUS_KM':   ('URANUS_RADIUS_KM',),
    'NEPTUNE_RADIUS_KM':  ('NEPTUNE_RADIUS_KM',),
    'PLUTO_RADIUS_KM':    ('PLUTO_RADIUS_KM',),
    'BENNU_RADIUS_KM':    ('BENNU_RADIUS_KM',),
    'ERIS_RADIUS_KM':     ('ERIS_RADIUS_KM',),
    'HAUMEA_RADIUS_KM':   ('HAUMEA_RADIUS_KM',),
    'MAKEMAKE_RADIUS_KM': ('MAKEMAKE_RADIUS_KM',),
    'ARROKOTH_RADIUS_KM': ('ARROKOTH_RADIUS_KM',),
}


def canonical_concept(name):
    """Map a constant name to its canonical concept, or None.
    Uses EXACT name match (not substring) to avoid unit-mismatch
    false positives like SPEED_OF_LIGHT vs SPEED_OF_LIGHT_KM_S."""
    up = name.upper()
    for concept, aliases in CONCEPT_ALIASES.items():
        if up in aliases:
            return concept
    return None


def find_cross_file_issues(units):
    """Find same-concept constants across multiple files.
    Returns (consistent_dups, inconsistencies)."""
    by_concept = defaultdict(list)
    for u in units:
        if u.kind != 'constant' or u.name is None:
            continue
        concept = canonical_concept(u.name)
        if concept:
            by_concept[concept].append(u)

    consistent_dups = []
    inconsistencies = []

    for concept, group in by_concept.items():
        if len(group) < 2:
            continue
        files = set(u.file for u in group)
        if len(files) < 2:
            continue
        values = set()
        for u in group:
            try:
                values.add(round(float(u.value), 6))
            except (TypeError, ValueError):
                values.add(u.value)
        entry = {
            'concept': concept,
            'units': group,
            'files': files,
            'values': values,
        }
        if len(values) == 1:
            consistent_dups.append(entry)
        else:
            inconsistencies.append(entry)

    return consistent_dups, inconsistencies


# ============================================================
# MAIN SCAN
# ============================================================

def load_exceptions(project_dir):
    """Load provenance_exceptions.json from data/ subdirectory if present.

    Returns (suppressed_fingerprints, accepted_residuals) where:
      suppressed_fingerprints: set of (file, fingerprint) tuples to drop
      accepted_residuals: list of dicts describing file-level accepted gaps
    """
    exceptions_path = os.path.join(project_dir, 'data', 'provenance_exceptions.json')
    if not os.path.exists(exceptions_path):
        return set(), []

    try:
        import json
        with open(exceptions_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"WARNING: Could not load exceptions file: {e}")
        return set(), []

    suppressed = set()
    for entry in data.get('suppressed', []):
        fname = entry.get('file', '')
        fp = entry.get('fingerprint', '')
        if fname and fp:
            suppressed.add((fname, fp[:40]))

    accepted = data.get('accepted_residuals', [])
    print(f"Loaded exceptions: {len(suppressed)} suppressed fingerprints, "
          f"{len(accepted)} accepted residuals")
    return suppressed, accepted


def is_suppressed(unit, suppressed_fingerprints):
    """Check if a unit matches any suppressed fingerprint.

    Checks both context_text (surrounding code, 60-line window) and
    raw_value (the actual string content). This is necessary because:
    - Code-line false positives: fingerprint appears in surrounding code
      (context_text) but not in the string value itself
    - Docstring/display-string false positives: fingerprint is inside the
      string content (raw_value), which for non-docstrings is NOT included
      in context_text by the scanner's citation logic
    Fix identified by Claude Opus 4.7 (April 2026).
    """
    if not suppressed_fingerprints:
        return False, None

    # Combined search: context window + raw string value
    context_sample = unit.context_text or ''
    raw_sample = getattr(unit, 'raw_value', None) or ''
    combined = context_sample + raw_sample

    for fname, fp in suppressed_fingerprints:
        if unit.file != fname:
            continue
        if fp in combined:
            return True, fp

    return False, None


def format_accepted_residuals(accepted_residuals):
    """Format accepted residuals as a markdown block for the audit report."""
    if not accepted_residuals:
        return []
    lines = [
        "## Accepted Residuals (data/provenance_exceptions.json)",
        "",
        "The following findings are documented exceptions -- known false positives",
        "or deliberately deferred items. They appear in lower tiers but require",
        "no action unless the underlying file is being actively modified.",
        "",
    ]
    for entry in accepted_residuals:
        fname = entry.get('file', 'unknown')
        tier = entry.get('tier', '?')
        category = entry.get('category', '')
        reason = entry.get('reason', '')
        lines.append(f"**{fname}** (Tier {tier}) -- {category}")
        lines.append(f"  {reason}")
        lines.append("")
    lines.append("---")
    lines.append("")
    return lines


def _scan_coverage_gap(filepath):
    """Lightweight claim-shape check for role='other' files (L-078 check 1b).

    These files bypass narrative-string extraction entirely -- role is
    genuinely unclassified, not a deliberate exclusion like 'gui' or
    'devtool'. Without this check they sit invisible with no trace, the
    same failure food_insecurity_generator had before L-064. Returns a
    count of strings that would register >=1 numeric claim; does not
    build ProvenanceUnits -- this is a coverage signal, not an audit.
    """
    try:
        with open(filepath, 'rb') as f:
            tree = ast.parse(f.read())
    except Exception:
        return 0

    count = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Constant):
            continue
        if not isinstance(node.value, str):
            continue
        if len(node.value) < 3:
            continue
        if list(extract_numeric_claims(node.value)):
            count += 1
    return count


def scan_project(project_dir, output_path='PROVENANCE_AUDIT.md'):
    """Scan all .py files and produce the provenance audit report."""
    print(f"Provenance Scanner -- scanning {project_dir}")
    print()

    # Phase 1c / L-174: module-level collectors, cleared per scan so a
    # second scan_project() call in the same process does not
    # double-report.
    del SCOPE_DECLARED_BLOCKS[:]
    del SHADOWED_STRINGS[:]
    del DEEP_CITATIONS[:]
    del SHADOW_CONSTANTS[:]

    suppressed_fingerprints, accepted_residuals = load_exceptions(project_dir)

    deps, consumers, local_modules = build_dependency_graph(project_dir)
    imported_names = build_name_import_map(project_dir, local_modules)

    # Pinned constant lookup from constants_new.py. Since D8.5 this
    # feeds the shadow-constant detector ONLY -- it no longer reaches
    # scoring. A value match is a reason to go look, not a reason to
    # grant credit.
    pinned_values = build_pinned_values(project_dir)
    if pinned_values:
        print(f"Loaded {len(pinned_values)} pinned constant values "
              f"for cross-reference scoring")

    # 1d piece 1: frozen-copy detection. Diagnostic only -- this does
    # not feed scoring.
    cited_names = build_cited_constant_names(project_dir)
    scan_shadow_constants(project_dir, cited_names, pinned_values)

    all_units = []
    files_scanned = 0
    suppressed_count = 0
    coverage_gaps = []  # L-078 check 1b: [(module_name, claim_string_count), ...]

    for fname in sorted(os.listdir(project_dir)):
        if not fname.endswith('.py'):
            continue
        filepath = os.path.join(project_dir, fname)
        module_name = fname[:-3]
        # Pass the path we already have: classify_role() reads the module's
        # docstring Role: tag now (L-163 Phase 3), so handing it the file
        # skips a name-to-path resolution that could pick the wrong tree.
        role = classify_role(module_name, filepath)

        units = extract_units_from_file(filepath, module_name, role)
        for u in units:
            score_unit(u, imported_names)
            hit, fp = is_suppressed(u, suppressed_fingerprints)
            if hit:
                suppressed_count += 1
            else:
                all_units.append(u)
        files_scanned += 1

        # L-078 check 1b: coverage-gap safety net for unclassified files.
        if role == 'other':
            gap_count = _scan_coverage_gap(filepath)
            if gap_count:
                coverage_gaps.append((module_name, gap_count))

    if suppressed_count:
        print(f"Suppressed {suppressed_count} known false positives "
              f"(see data/provenance_exceptions.json)")

    consistent_dups, inconsistencies = find_cross_file_issues(all_units)

    if SCOPE_DECLARED_BLOCKS:
        print(f"{len(SCOPE_DECLARED_BLOCKS)} block(s) carry a scope-limited "
              f"citation -- inheritance declined, see audit")
    if SHADOWED_STRINGS:
        print(f"{len(SHADOWED_STRINGS)} string(s) sit in an uncited block "
              f"inside a cited one -- citation level mismatch, see audit")
    if DEEP_CITATIONS:
        print(f"WARNING: {len(DEEP_CITATIONS)} citation(s) sit on a dict "
              f"nested deeper than the block table reads -- see audit")
    if SHADOW_CONSTANTS:
        print(f"{len(SHADOW_CONSTANTS)} shadow constant(s) -- local copies "
              f"of cited constants_new.py values, see audit")

    generate_report(all_units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=accepted_residuals,
                    coverage_gaps=coverage_gaps,
                    scope_declared=list(SCOPE_DECLARED_BLOCKS),
                    shadowed=list(SHADOWED_STRINGS),
                    deep_citations=list(DEEP_CITATIONS),
                    shadow_constants=list(SHADOW_CONSTANTS))

    return all_units, consistent_dups, inconsistencies


# ============================================================
# REPORT GENERATION
# ============================================================

def generate_report(units, consistent_dups, inconsistencies,
                    files_scanned, project_dir, output_path,
                    accepted_residuals=None, coverage_gaps=None,
                    scope_declared=None, shadowed=None,
                    deep_citations=None, shadow_constants=None):
    """Write PROVENANCE_AUDIT.md."""
    now = datetime.now().strftime('%B %d, %Y')

    scored = [u for u in units if u.score and u.score > 0]
    scored.sort(key=lambda u: (-u.score, u.file, u.line_start))

    tier_counts = defaultdict(int)
    for u in scored:
        tier_counts[action_tier(u.score)] += 1

    kind_counts = defaultdict(int)
    for u in scored:
        kind_counts[u.kind] += 1

    out = []

    # ---- Header ----
    out.append("# Paloma's Orrery -- Provenance Audit")
    out.append("")
    out.append(f"Generated: {now}")
    out.append(f"Files scanned: {files_scanned}")
    out.append(f"Total findings: {len(scored)}")
    out.append(f"Constants: {kind_counts.get('constant', 0)} | "
               f"Dicts: {kind_counts.get('dict', 0)} | "
               f"Display strings: {kind_counts.get('string', 0)}")
    out.append("")
    out.append("Unit of provenance: the smallest thing with a coherent "
               "source citation. A dict with one block-level `# Source:` "
               "comment is ONE unit; all its entries inherit that citation. "
               "A hover string with co-referring numbers is ONE unit.")
    out.append("")
    out.append("**Color values are excluded from this audit.** RGB/color "
               "fields are never scored as claims (see _make_dict_unit), "
               "and a dict's block `# Source:` citation should never be "
               "read as covering that dict's `color` field(s), even when "
               "it covers everything else in the same unit. This does not "
               "mean color choices have no basis at all -- some are loosely "
               "informed by real imagery or composition data -- but color "
               "selection across this codebase is inconsistent in method: "
               "sometimes evidence-informed, sometimes chosen purely for "
               "visual contrast or distinction, sometimes arbitrary. Treat "
               "every color value as a developer/AI judgment call, not a "
               "measured or verified quantity, regardless of what citation "
               "sits nearby. (Tony's call, July 16, 2026; a low-priority "
               "wishlist item for a real, systematic color-accuracy pass is "
               "tracked at LEDGER_CONSOLIDATED.md L-124.)")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Risk matrix ----
    out.append("## Risk Matrix: Vulnerability x Criticality")
    out.append("")
    out.append("**Vulnerability** (how likely to be wrong):")
    out.append("- 1 = Fetched (authoritative pipeline)")
    out.append("- 2 = Sourced (has citation)")
    out.append("- 3 = Stale (may have changed)")
    out.append("- 4 = Recalled (LLM training data, no citation)")
    out.append("")
    out.append("**Criticality** (impact if wrong):")
    out.append("- 1 = Cosmetic (colors, labels)")
    out.append("- 2 = Internal (used but not imported elsewhere)")
    out.append("- 3 = Load-bearing (drives geometry) or imported 1-2x")
    out.append("- 4 = Public-facing (hover text, gallery)")
    out.append("- 5 = Propagating (imported by 3+ modules)")
    out.append("")
    out.append("**Score = V x C** | Action thresholds:")
    out.append("- 16-20: FIX NOW")
    out.append("- 10-15: REVIEW")
    out.append("- 5-9: LOW PRIORITY")
    out.append("- 1-4: LOWEST PRIORITY")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Priority summary ----
    out.append("## Priority Summary")
    out.append("")
    out.append("| Tier | Score | Action | Count |")
    out.append("|------|-------|--------|------:|")
    # 1e piece 2 (design handoff D7): tier names are score bands, not
    # claims about the findings inside them. The old Tier-2 name asserted
    # "ALL ACCEPTED RESIDUALS", so every new finding landing in that band
    # was narrated as already-reviewed by this template -- including the
    # ones 1b had just moved there. Accepted-residual status is
    # per-finding and has its own report block.
    tier_labels = {
        1: ("16-20", "FIX NOW"),
        2: ("10-15", "REVIEW"),
        3: ("5-9", "LOW PRIORITY"),
        4: ("1-4", "LOWEST PRIORITY"),
    }
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        out.append(f"| {tier} | {score_range} | {action} | {count} |")
    out.append("")
    out.append("**Tier 2 note (April 2026 audit):** All Tier-2 findings are documented")
    out.append("accepted residuals -- cited constants, V_STALE staleness flags on verified")
    out.append("strings, or known scanner limitations. No action required unless a new")
    out.append("uncited entry appears. See Accepted Residuals block below for details.")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Findings by file (all tiers, at-a-glance) ----
    out.append("## Findings by File")
    out.append("")
    out.append("Quick-reference counts before the per-tier detail below. Same "
               "data, grouped the other way: every file that has at least one "
               "finding, with its count in each tier.")
    out.append("")
    file_tier_counts = defaultdict(lambda: defaultdict(int))
    for u in scored:
        file_tier_counts[u.file][action_tier(u.score)] += 1
    unmapped_files = set()

    def _domain_for(fname):
        stem = fname[:-3] if fname.endswith('.py') else fname
        domain, was_mapped = classify_domain(stem)
        if not was_mapped:
            unmapped_files.add(fname)
        return domain

    out.append("| File | Domain | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |")
    out.append("|------|--------|-------:|-------:|-------:|-------:|------:|")
    for fname in sorted(file_tier_counts.keys(),
                        key=lambda f: -sum(file_tier_counts[f].values())):
        counts = file_tier_counts[fname]
        total = sum(counts.values())
        domain = _domain_for(fname)
        out.append(f"| `{fname}` | {domain} | {counts.get(1, 0)} | "
                   f"{counts.get(2, 0)} | {counts.get(3, 0)} | "
                   f"{counts.get(4, 0)} | {total} |")
    out.append("")
    out.append("---")
    out.append("")

    # ---- Findings by file type (domain breakdown) ----
    out.append("## Findings by File Type")
    out.append("")
    out.append("Same data again, grouped by subject-matter domain rather than "
               "by individual file -- orrery, earth science, gallery, stars, "
               "utilities, dev tools. Domain is a report-only grouping "
               "(see MODULE_DOMAIN_MAP / classify_domain()); it does not "
               "affect which files get scanned or scored.")
    out.append("")
    domain_tier_counts = defaultdict(lambda: defaultdict(int))
    domain_file_counts = defaultdict(set)
    for fname, counts in file_tier_counts.items():
        domain = _domain_for(fname)
        domain_file_counts[domain].add(fname)
        for tier, n in counts.items():
            domain_tier_counts[domain][tier] += n
    out.append("| Domain | Files | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Total |")
    out.append("|--------|------:|-------:|-------:|-------:|-------:|------:|")
    # Show all six domains, including any with zero current findings --
    # a domain going quiet (e.g. gallery) is itself worth seeing, not
    # worth silently dropping from the table.
    all_domains = sorted(DOMAIN_LABELS.keys(),
                         key=lambda d: -sum(domain_tier_counts[d].values()))
    for domain in all_domains:
        counts = domain_tier_counts[domain]
        total = sum(counts.values())
        label = DOMAIN_LABELS.get(domain, domain)
        out.append(f"| {label} | {len(domain_file_counts[domain])} | "
                   f"{counts.get(1, 0)} | {counts.get(2, 0)} | "
                   f"{counts.get(3, 0)} | {counts.get(4, 0)} | {total} |")
    out.append("")
    if unmapped_files:
        out.append("**Domain coverage gap:** the following files have findings "
                   "but no entry in `MODULE_DOMAIN_MAP` -- defaulted to "
                   "`orrery` rather than guessed into a more specific bucket. "
                   "Add each to `MODULE_DOMAIN_MAP` in provenance_scanner.py "
                   "with its real domain so this stops silently defaulting:")
        out.append("")
        for fname in sorted(unmapped_files):
            out.append(f"- `{fname}`")
        out.append("")
    out.append("---")
    out.append("")

    # ---- Shadow constants (L-156 Gap item 5, 1d piece 1) ----
    if shadow_constants:
        out.append("## SHADOW CONSTANTS -- [CRITICAL] convention violation")
        out.append("")
        out.append("Local copies of values that are already defined and "
                   "cited in `constants_new.py`. The number may be correct "
                   "today; the problem is that it will not follow if the "
                   "source value is ever corrected, and it sits outside "
                   "the citation chain in the meantime.")
        out.append("")
        out.append("Per provenance-discipline v1.3, No Shadow Constants "
                   "[CRITICAL]: delete the local definition and import the "
                   "real one, through the `planet_visualization_utilities` "
                   "shim or directly. Do NOT add a `# Source:` comment to "
                   "the local copy -- that cites-to-clear a structural "
                   "problem instead of fixing it.")
        out.append("")
        out.append("`direct` means the local name and value both match a "
                   "cited constant. `derived` means the value is computed "
                   "from pinned literals rather than from the imported "
                   "names.")
        out.append("")
        out.append("| File | Line | Name | Kind |")
        out.append("|------|-----:|------|------|")
        for entry in sorted(shadow_constants):
            sfile, line, name, kind, _val = entry
            out.append(f"| `{sfile}` | {line} | `{name}` | {kind} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Citation level mismatch (L-174) ----
    if shadowed or deep_citations:
        out.append("## CITATION LEVEL MISMATCH -- diagnostic, no scoring effect")
        out.append("")
        out.append("Citations in this codebase attach to a block. The "
                   "resolver reads exactly one block per string: the "
                   "narrowest one containing it. A citation written one "
                   "level further out is invisible to it. Nothing below "
                   "is mis-scored today -- the flat 60-line context "
                   "window catches these independently, which is exactly "
                   "why the mismatch is easy to miss. Move a few lines "
                   "and it becomes a real gap with no warning.")
        out.append("")

    if shadowed:
        from collections import defaultdict as _dd
        grouped = _dd(list)
        for sfile, line, dname, dkey, cline in shadowed:
            grouped[sfile].append((line, dname, dkey, cline))
        out.append("### Shadowed strings")
        out.append("")
        out.append("The string sits in a block with no citation, inside a "
                   "block that has one. Fix by repeating a short citation "
                   "above the inner block's key, as done for "
                   "`ring_params` -- not by loosening the resolver, which "
                   "would clear the L-173 gaps by accident.")
        out.append("")
        out.append("| File | Line | Shadowed from | Its citation at |")
        out.append("|------|-----:|---------------|----------------:|")
        for sfile in sorted(grouped):
            for line, dname, dkey, cline in sorted(grouped[sfile]):
                label = f"`{dname}['{dkey}']`" if dkey else f"`{dname}`"
                out.append(f"| `{sfile}` | {line} | {label} | {cline} |")
        out.append("")

    if deep_citations:
        out.append("### Citations below the table's reach -- ACTION NEEDED")
        out.append("")
        out.append("A dict nested three or more levels deep carries its "
                   "own citation. The block table records only the "
                   "assignment and its direct entries, so this citation "
                   "cannot be reached and strings inside it will inherit "
                   "the shallower one instead -- a real misattribution "
                   "that will not show up in the tier counts. This list "
                   "was empty when the diagnostic was written; if it is "
                   "not empty now, the table needs extending.")
        out.append("")
        out.append("| File | Path | Depth | Key line | Citation at |")
        out.append("|------|------|------:|---------:|------------:|")
        for dfile, dname, path, depth, kline, cline in sorted(deep_citations):
            label = dname + ''.join(f"['{p}']" for p in path)
            out.append(f"| `{dfile}` | `{label}` | {depth} | {kline} "
                       f"| {cline} |")
        out.append("")

    if shadowed or deep_citations:
        out.append("---")
        out.append("")

    # ---- Scope-limited citations (L-156 Phase 1c) ----
    if scope_declared:
        out.append("## SCOPE-LIMITED CITATIONS -- inheritance declined")
        out.append("")
        out.append("These dict blocks carry a citation whose author "
                   "explicitly narrowed what it covers (a `Scope of the "
                   "above citation:` note). Strings inside them do NOT "
                   "inherit the citation -- asserting provenance the "
                   "author disclaimed is the same failure as citing over "
                   "recalled data, pointed the other way. Findings inside "
                   "these blocks stay where they were. Listed here so the "
                   "decision stays visible rather than silently doing "
                   "nothing.")
        out.append("")
        out.append("| File | Block | Lines | Citation at |")
        out.append("|------|-------|-------|------------:|")
        for entry in sorted(scope_declared):
            sfile, dname, dkey, bstart, bend, cline = entry
            label = f"`{dname}['{dkey}']`" if dkey else f"`{dname}`"
            out.append(f"| `{sfile}` | {label} | {bstart}-{bend} | {cline} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Coverage gaps (L-078 check 1b) ----
    if coverage_gaps:
        out.append("## COVERAGE GAPS -- needs role classification")
        out.append("")
        out.append("These modules are classified `'other'` in module_atlas.py's "
                   "ROLE_MAP (unrecognized, not deliberately excluded) and contain "
                   "string content that looks claim-shaped. They are NOT scanned "
                   "for narrative citations -- role-driven inclusion only covers "
                   "data / scenario / rendering / rendering-shells / computation. "
                   "Add each to ROLE_MAP with its real role (or to narrative_files "
                   "as a manual override) so it stops being invisible.")
        out.append("")
        out.append("| Module | Claim-shaped strings |")
        out.append("|--------|----------------------:|")
        for module_name, count in sorted(coverage_gaps, key=lambda x: -x[1]):
            out.append(f"| `{module_name}.py` | {count} |")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Accepted residuals (from exceptions file) ----
    if accepted_residuals:
        out.extend(format_accepted_residuals(accepted_residuals))

    # ---- Inconsistencies (highest priority) ----
    if inconsistencies:
        out.append("## INCONSISTENCIES (Same concept, different values)")
        out.append("")
        out.append("Highest-risk findings: the same physical concept has ")
        out.append("different numeric values in different files.")
        out.append("")
        for entry in inconsistencies:
            out.append(f"### {entry['concept']}")
            out.append("")
            out.append(f"**Values found:** " +
                       ", ".join(str(v) for v in sorted(entry['values'])))
            out.append(f"**Files:** " + ", ".join(sorted(entry['files'])))
            out.append("")
            for u in sorted(entry['units'],
                            key=lambda x: (x.file, x.line_start)):
                out.append(f"- `{u.file}:{u.line_start}` -- "
                           f"`{u.name} = {u.value_str}`")
            out.append("")
            out.append("**Action:** Determine correct value with citation. "
                       "Consolidate to single source of truth in "
                       "constants_new.py. Replace duplicates with imports.")
            out.append("")
        out.append("---")
        out.append("")
    else:
        out.append("## INCONSISTENCIES")
        out.append("")
        out.append("None detected. No same-concept constants with differing ")
        out.append("values found across files.")
        out.append("")
        out.append("Note: this does NOT rule out silent shadowing (a local ")
        out.append("dict with different name but overlapping keys). That ")
        out.append("pattern is the April 16 bug family; shadow detection ")
        out.append("is planned for a future session.")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Consistent duplicates ----
    if consistent_dups:
        out.append("## DUPLICATES (Same value, multiple files)")
        out.append("")
        out.append("Consistent values defined in multiple places rather ")
        out.append("than imported from one source. Consolidation candidates.")
        out.append("")
        for entry in consistent_dups:
            val = list(entry['values'])[0]
            files_str = ", ".join(sorted(entry['files']))
            out.append(f"- **{entry['concept']}** = {val} -- in {files_str}")
        out.append("")
        out.append("**Action:** Consolidate to constants_new.py and import.")
        out.append("")
        out.append("---")
        out.append("")

    # ---- Per-tier findings ----
    for tier in [1, 2, 3, 4]:
        tier_units = [u for u in scored if action_tier(u.score) == tier]
        if not tier_units:
            continue
        score_range, action = tier_labels[tier]
        out.append(f"## Tier {tier}: {action} (Score {score_range})")
        out.append("")

        by_file = defaultdict(list)
        for u in tier_units:
            by_file[u.file].append(u)

        for fname in sorted(by_file.keys()):
            out.append(f"### {fname}")
            out.append("")
            out.append("| Line | Kind | Name | Size/Value | V | C | "
                       "Score | Vulnerability | Criticality |")
            out.append("|-----:|------|------|------------|--:|--:|"
                       "------:|---------------|-------------|")
            for u in sorted(by_file[fname], key=lambda x: -x.score):
                name = u.display_name[:40]
                val = u.short_value[:20]
                out.append(
                    f"| {u.line_start} | {u.kind} | {name} | {val} | "
                    f"{u.vuln} | {u.crit} | **{u.score}** | "
                    f"{u.vuln_reason} | {u.crit_reason} |"
                )
            out.append("")
        out.append("---")
        out.append("")

    # ---- Footer ----
    out.append("## How to Use This Audit")
    out.append("")
    out.append("1. Start with INCONSISTENCIES -- these are confirmed problems.")
    out.append("2. Work through Tier 1 (FIX NOW) findings.")
    out.append("3. For each finding:")
    out.append("   a. Locate the correct value from an authoritative source.")
    out.append("   b. Update constants_new.py (or info_dictionary.py).")
    out.append("   c. Add a `# Source:` comment above the declaration.")
    out.append("   d. Replace local copies with imports.")
    out.append("   e. Verify downstream plots unchanged.")
    out.append("4. Re-run this scanner to confirm fixes.")
    out.append("")
    out.append("Companion tools:")
    out.append("- module_atlas.py              -- dependency graph")
    out.append("- test_constants_provenance.py -- pin constants_new.py values")
    out.append("- dep_trace.py                 -- per-module import tracing")
    out.append("")
    out.append("---")
    out.append("")
    out.append("*Generated by provenance_scanner.py -- "
               "Paloma's Orrery Developer Tools*")
    out.append("")

    content = "\n".join(out)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Audit written to {output_path}")
    print(f"  {len(scored)} findings across {files_scanned} files")
    print()
    print("Priority summary:")
    for tier in [1, 2, 3, 4]:
        score_range, action = tier_labels[tier]
        count = tier_counts.get(tier, 0)
        print(f"  Tier {tier} ({score_range}): {count:5d} findings -- {action}")

    # 1e piece 1: Tier-1 banner. INFORMATIONAL ONLY.
    #
    # The exit code is deliberately untouched here, and should stay that
    # way. Design review section 3c: Tier-1 never gets an auto-exit gate,
    # at any threshold, ever -- a count is the wrong thing to judge by,
    # since a trivial new finding would fail a good run and a serious
    # finding replacing a trivial one at equal count would pass a bad
    # one. Whether N findings are acceptable to push past is a judgment
    # call every time. The only hard exit-code gate belongs to the
    # pinning checks, which are genuinely binary.
    #
    # (HANDOFF_phase1_1d_to_1f.md at HEAD describes a deferred exit-gate
    # flip. That is the superseded Fable design; do not revive it from
    # that document.)
    tier1 = tier_counts.get(1, 0)
    if tier1:
        bar = "=" * 70
        print()
        print(bar)
        print(f"  {tier1} TIER-1 FINDINGS -- PUSH GATE NOT MET")
        print()
        print("  Informational only. This does not affect the exit code.")
        print("  Review them before pushing; the call is yours.")
        print(bar)

    if inconsistencies:
        print()
        print(f"  *** {len(inconsistencies)} INCONSISTENCIES detected ***")
    if consistent_dups:
        print(f"  {len(consistent_dups)} consistent duplicates "
              f"(consolidation candidates)")


# ============================================================
# CLI
# ============================================================

def main():
    project_dir = '.'
    output_path = 'PROVENANCE_AUDIT.md'

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == '--output' and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        elif not args[i].startswith('-'):
            project_dir = args[i]
            i += 1
        else:
            i += 1

    if not os.path.isdir(project_dir):
        print(f"ERROR: '{project_dir}' is not a directory")
        sys.exit(1)

    scan_project(project_dir, output_path)


if __name__ == '__main__':
    main()