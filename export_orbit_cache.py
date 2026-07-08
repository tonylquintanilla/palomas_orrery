"""
export_orbit_cache.py - Phase 1b desktop devtool: read the local orbit caches
and write web-servable orbit/position files for the interactive gallery.

Runs on Tony's desktop only (never in the browser); reads the caches read-only
and never modifies them.

=============================================================================
RUNNING THE MODULE
=============================================================================
Placement: put this file in the orrery repo ROOT (beside gallery_studio.py),
so `celestial_objects`, `constants_new`, and `shell_configs` import and the
caches resolve at ./data/orbit_paths.json and ./data/osculating_cache.json
(CACHE_DIR = the script's folder / 'data'). Run from that folder.

Prerequisites (already present in the orrery desktop env): Python 3, the repo
modules above, and plotly (pulled transitively by shell_configs for Step 6
only; the rest of the export does not need it).

Commands:
  # 1. Pre-flight FIRST -- read-only diagnostics, writes nothing. Capture the
  #    output; it is the ground truth the export proceeds on.
  python export_orbit_cache.py --preflight-only

  # 2. Export the test tranche to the SAFE default scratch dir (./_export_out).
  #    Writes locally so you can inspect BEFORE anything touches the gallery.
  python export_orbit_cache.py

  # 3. DEPLOY: export straight into the gallery repo -- EXPLICIT path only, so a
  #    bare run can never overwrite the live gallery data by accident.
  python export_orbit_cache.py --output-dir ../tonyquintanilla.github.io/data/solar-system/

  # 4. (follow-on) Export the whole catalog, not just the 9-object tranche.
  #    Tranche-scoped in this build -- prints a notice and exports the tranche.
  python export_orbit_cache.py --full-catalog

Flags:
  --output-dir <path>   where files are written (default: ./_export_out -- a
                        local scratch dir; add it to the orrery repo .gitignore.
                        Pass the gallery data path explicitly, as in (3), to
                        deploy. The default NEVER writes to the gallery.)
  --preflight-only      run Step 0 diagnostics + Step 0-STOP, then stop
  --full-catalog        follow-on; tranche-scoped for now

Operational order (the double-helix loop): (1) --preflight-only and read it;
(2) export to the scratch default and INSPECT (positions/*.json km+JD, the
coverage index, the invariant line); (3) Mode 5 -- open the render, Tony's eyes
are the gate on the ~6.4-pt Pluto/Charon hexagons and the Moon/Titan traces;
(4) provenance scan Tier-1 = 0 (add a ROLE_MAP entry for this module so the
coverage-gap check can classify it); (5) DEPLOY -- re-run with --output-dir set
to the gallery data path (or copy _export_out/ across), commit, push, and
record the pushed SHA in the handoff.

Exit codes: 0 success; 1 caches not found; a raised AssertionError on a failed
invariant (e.g. a center mismatch) is a LOUD failure, by design -- not a
silent envelope lie. A missing position pair does NOT abort: it warns and the
object ships osculating-only.

=============================================================================
PRODUCT MODEL (v4 -- the subtraction model was rejected)
=============================================================================
Osculating elements are the PRIMARY orbit product (matched to each object's
viewing center); direct relative-frame Horizons position vectors are a
SECONDARY trajectory layer, served where a direct pair exists at adequate
cadence. There is NO subtraction: differencing two heliocentric ephemerides
was empirically rejected on the desktop (catastrophic cancellation of two
large vectors down to a small residual, plus daily-cadence aliasing of fast
moon motion), so every served frame is one Horizons produced directly and the
matching osculating center is used for the orbit ellipse. The orbit ALWAYS
renders from osculating; the position trace is additive where cadence allows.

=============================================================================
OUTPUT STRUCTURE (schema aligned to PHASE1B_DATA_SERVING_DESIGN_HANDOFF v0.6)
=============================================================================
<output_dir>/
  coverage_index.json
  feature_configs.json
  positions/<slug>.json      one per object with a served trace
  presets/<slug>.json        (none in this tranche -- Apophis 2029 data absent)

coverage_index.json (top level):
  schema_version   "1.0"          schema format version (not the handoff version)
  generated        ISO datetime    provenance anchor for the data
  generator        str             this script + version
  serving_base     str             path prefix for file references
  feature_configs  str             path to feature_configs.json
  scene_features   [str]           scene-wide feature slugs (belts, heliosphere)
  model            {..}            v4 note: osculating-primary, no subtraction
  objects          {slug: {..}}    keyed by slug (below)

coverage_index objects.<slug>:
  name             str             display name
  horizons_id      str             JPL Horizons id of the OBJECT (not the center)
  category         enum            planet|dwarf_planet|moon|asteroid|comet|spacecraft
  availability     enum            analytic|spacecraft   (v4: 'cache-required'
                                   retired -- the orbit always renders from
                                   osculating; a served trace no longer means
                                   the cache is REQUIRED to draw the orbit)
  parent           str             gravitational parent slug (sun, jupiter, ...)
  stored_center    str             center of the served orbit AND trace (the
                                   frame both live in; matches osculating.center)
  canonical_frame  enum            heliocentric | parent-relative |
                                   barycenter-relative (v4 addition) |
                                   arc-natural | geocentric
  trajectory_of    str|null        non-null only if the served path is a
                                   substitute body's; null under v4 (each object
                                   serves its own frame, including Pluto's
                                   barycenter wobble)
  osculating       obj|null        {center, epoch_jd, a_au, e, i_deg, node_deg,
                                   peri_deg, M0_deg, source}; null for spacecraft
  positions        obj|null        {file, start, end, step_hours, n_points,
                                   size_kb}; null when no trace is served
  presets          [obj]|null      self-contained Tier-2 sets; null in tranche
  features         [str]|null      visual-feature slugs (params in feature_configs)

osculating.source (structured, for Horizons re-verification):
  {query_target, center, epoch, retrieved}

position file <slug>.json (column-oriented, self-documenting):
  object, center, frame, unit "km", epoch_type "JD",
  source {query_target, center, epoch, retrieved},
  data  {t:[JD...], x:[km...], y:[km...], z:[km...]}

preset object (documented; none emitted this tranche):
  {name, slug, description, tier, positions:{...positions..., center,
   canonical_frame}} -- built from close_approach_data.py when data exists.

=============================================================================
VALIDATION INVARIANTS asserted before the index is written (v4 set)
=============================================================================
  #2 spacecraft  -> osculating == null AND positions != null
  #3 analytic    -> osculating != null            (hard assert for the tranche)
  #5 osculating != null -> osculating.center populated and a valid slug
  #6 every presets[].positions.file exists on disk
  #8 every positions.file exists on disk
  #C center-match (v4, the Charon@9 lesson): osculating.center == stored_center
  #F frame-contamination guard (v4.1): a parent-/barycenter-relative served
     trace whose max |r| exceeds 0.5 AU is heliocentric-contaminated (a cache
     pair with mixed-frame points); the trace is DROPPED to osculating-only
     with a loud warning, and the cache source must be repaired.
RETIRED with the subtraction model: v0.6 #1 (cache-required -> positions),
#4 (parent-relative parent dependency), #7 (moon/parent grid nesting) -- all
were artifacts of deriving moon frames by subtraction, which v4 does not do.

Key functions:
    run_preflight()          - Step 0 (0a-0f) read-only diagnostics + Step 0-STOP
    run_export()             - Steps 1-6: osculating + position files + index
    build_osculating_entry() - Step 4: elements -> coverage-index osculating block
    write_position_file()    - Step 3: a direct relative pair -> a position file
    resolve_center_slug()    - Horizons center (@id or name) -> schema slug

Consumed by: Tony's desktop (manual run); output copied to
tonyquintanilla.github.io/data/solar-system/. Grounded against orrery HEAD
d4c37cf (idealized_orbits.py osculating-only satellite systems + barycenter
mode; celestial_objects.py Pluto 999 vs barycenter 9; osculating_cache_manager
keys/fields; constants_new KM_PER_AU / KNOWN_ORBITAL_PERIODS;
PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6 schema).

Module updated: July 2026 with Anthropic's Claude Opus 4.8
(Stage 2 build: v4 osculating-primary model; coverage index reconciled to
design handoff v0.6; subtraction path retired).
"""

import argparse
import json
import math
import os
import sys
from collections import namedtuple
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

# Authoritative constants from the codebase (NOT recalled).
from constants_new import KM_PER_AU, KNOWN_ORBITAL_PERIODS

SCHEMA_VERSION = "1.0"          # coverage-index format version (per v0.6 schema)
GENERATOR = "export_orbit_cache.py v4"
# Source: PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.6 (scene-wide features).
SCENE_FEATURES = ["asteroid_belt", "kuiper_belt", "heliosphere"]

# Caches live in ./data next to this script (verified against
# osculating_cache_manager.py at HEAD: CACHE_DIR = __file__ parent / 'data').
CACHE_DIR = Path(__file__).parent / 'data'
ORBIT_PATHS = CACHE_DIR / 'orbit_paths.json'
OSC_CACHE = CACHE_DIR / 'osculating_cache.json'

_UNIX_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


# ---------------------------------------------------------------------------
# Center resolution (Step 2 scaffolding)
# ---------------------------------------------------------------------------
# Horizons center comes in two conventions in the caches: osculating metadata
# uses @-ids ('@sun','@399','@9'); position metadata uses NAMES ('Sun','Earth',
# 'Pluto-Charon Barycenter'). The map covers both so a served position center
# and its osculating center resolve to the same slug (the center-match check).
CENTER_SLUG_MAP = {
    '@sun': 'sun', '@0': 'sun', '@10': 'sun', 'sun': 'sun', 'Sun': 'sun',
    '0': 'sun', '10': 'sun',
    '@399': 'earth', '399': 'earth', 'Earth': 'earth',
    '@599': 'jupiter', '599': 'jupiter', 'Jupiter': 'jupiter',
    '@699': 'saturn', '699': 'saturn', 'Saturn': 'saturn',
    '@9': 'pluto_barycenter', '9': 'pluto_barycenter',
    'Pluto-Charon Barycenter': 'pluto_barycenter',
    '@3': 'earth_moon_barycenter', '3': 'earth_moon_barycenter',
    'Earth-Moon Barycenter': 'earth_moon_barycenter',
}
VALID_SLUGS = set(CENTER_SLUG_MAP.values())


def resolve_center_slug(center_body):
    """Map a Horizons center (@-id or name) to a schema slug. Rejects unmapped."""
    if center_body is None:
        raise ValueError("center_body is None")
    slug = CENTER_SLUG_MAP.get(center_body)
    if slug is None:
        slug = CENTER_SLUG_MAP.get(str(center_body).lstrip('@'))
    if slug is None:
        raise ValueError("Unmapped center_body: %r" % (center_body,))
    return slug


# v4 tranche. Fields carry the v0.6 coverage-index shape plus the build-side
# keys (osc_key, position_pair_key, trace_policy). availability is 'analytic'
# for every non-spacecraft (the orbit renders from osculating); 'cache-required'
# is retired. stored_center is the frame the orbit AND trace live in.
TestObject = namedtuple('TestObject',
    'slug name horizons_id category availability parent stored_center '
    'canonical_frame trajectory_of osc_key position_pair_key trace_policy features')

TEST_OBJECTS = [
    TestObject("earth",     "Earth",     "399",   "planet",       "analytic",   "sun",     "sun",              "heliocentric",        None, "Earth",    "Earth_Sun",                     "serve", ["van_allen_belts", "atmosphere_shell"]),
    TestObject("jupiter",   "Jupiter",   "599",   "planet",       "analytic",   "sun",     "sun",              "heliocentric",        None, "Jupiter",  "Jupiter_Sun",                   "serve", ["magnetosphere", "ring_system"]),
    TestObject("saturn",    "Saturn",    "699",   "planet",       "analytic",   "sun",     "sun",              "heliocentric",        None, "Saturn",   "Saturn_Sun",                    "serve", ["ring_system"]),
    TestObject("moon",      "Moon",      "301",   "moon",         "analytic",   "earth",   "earth",            "parent-relative",     None, "Moon",     "Moon_Earth",                    "serve", None),
    TestObject("io",        "Io",        "501",   "moon",         "analytic",   "jupiter", "jupiter",          "parent-relative",     None, "Io",       "Io_Jupiter",                    "none",  None),
    TestObject("titan",     "Titan",     "606",   "moon",         "analytic",   "saturn",  "saturn",           "parent-relative",     None, "Titan",    "Titan_Saturn",                  "serve", None),
    TestObject("pluto",     "Pluto",     "999",   "dwarf_planet", "analytic",   "sun",     "pluto_barycenter", "barycenter-relative", None, "Pluto@9",  "Pluto_Pluto-Charon Barycenter", "serve", None),
    TestObject("charon",    "Charon",    "901",   "moon",         "analytic",   "pluto",   "pluto_barycenter", "barycenter-relative", None, "Charon@9", "Charon_Pluto-Charon Barycenter","serve", None),
    TestObject("apophis",   "Apophis",   "99942", "asteroid",     "analytic",   "sun",     "sun",              "heliocentric",        None, "Apophis",  "Apophis_Sun",                   "none",  None),
    TestObject("voyager_1", "Voyager 1", "-31",   "spacecraft",   "spacecraft", "sun",     "sun",              "arc-natural",         None, None,       "Voyager 1_Sun",                 "serve", None),
]

# Io trace_policy 'none' on CADENCE (daily ~1.8 pts/orbit -- cannot close the
# orbit), not because the pair is missing; its orbit still renders from
# osculating. Apophis is osculating + null 2029 preset (its heliocentric pair
# exists and could be served if scope changes). Pluto/Charon are served in the
# barycenter frame per Tony's ruling; trajectory_of is null because each serves
# its OWN barycenter-relative path (not a substituted body).


# ---------------------------------------------------------------------------
# JD + anomaly helpers (Step 3 / Step 4)
# ---------------------------------------------------------------------------
def _dt_to_jd(dt):
    """UTC datetime -> Julian Date. Pure Python via the unix epoch (JD
    2440587.5); leap seconds are sub-second and negligible for visualization.
    Used for BOTH position timestamps and osculating epochs so orbit and trace
    share one time scale."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return 2440587.5 + (dt - _UNIX_EPOCH).total_seconds() / 86400.0


def _parse_calendar(s):
    """Parse a cache date/epoch string (date-only or time-bearing) to datetime."""
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d'):
        try:
            return datetime.strptime(s.strip(), fmt)
        except ValueError:
            continue
    raise ValueError("unparseable date/epoch: %r" % (s,))


def parse_osc_epoch_to_jd(epoch_str):
    """Osculating epoch string -> JD. Strips the trailing ' osc.' and parses the
    remainder, which may be 'YYYY-MM-DD HH:MM' (8/9 of the tranche) or
    'YYYY-MM-DD' (Apophis). Do NOT split-and-take-date-only -- that drops the
    time-of-day and shifts M0's epoch by up to ~1 day."""
    s = epoch_str.strip()
    if s.lower().endswith('osc.'):
        s = s[:-4].strip()
    return _dt_to_jd(_parse_calendar(s))


def _true_to_mean_anomaly_deg(ta_deg, e):
    """True anomaly (deg) -> mean anomaly (deg), elliptical only. Defensive
    fallback for MA=None (0/9 in the tranche). Returns None if not elliptical."""
    if e is None or e >= 1.0:
        return None
    ta = math.radians(ta_deg)
    ecc = math.atan2(math.sqrt(1.0 - e * e) * math.sin(ta), e + math.cos(ta))
    m = ecc - e * math.sin(ecc)
    return math.degrees(m) % 360.0


# ---------------------------------------------------------------------------
# Step 0: pre-flight (SHIPPED, RUN -- kept for repeatability)
# ---------------------------------------------------------------------------
def _load_json(path):
    with open(path, 'r') as fh:
        return json.load(fh)


def _key_format(keys):
    if not keys:
        return 'none'
    return 'time-bearing' if (':' in keys[0] or 'T' in keys[0]) else 'date-only'


def _median_spacing_days(date_keys):
    if len(date_keys) < 2:
        return None
    try:
        parsed = sorted(_parse_calendar(k) for k in date_keys)
    except ValueError:
        return None
    gaps = [(parsed[i + 1] - parsed[i]).total_seconds() / 86400.0
            for i in range(len(parsed) - 1)]
    return median(gaps) if gaps else None


PREFLIGHT_PAIR_KEYS = [
    'Earth_Sun', 'Jupiter_Sun', 'Saturn_Sun', 'Pluto_Sun', 'Moon_Sun',
    'Io_Sun', 'Titan_Sun', 'Charon_Sun', 'Voyager 1_Sun', 'Apophis_Sun',
]


def run_preflight():
    """Step 0 (0a-0f) + Step 0-STOP. Read-only. Prints the ground truth."""
    print("=" * 72)
    print("PHASE 1B PRE-FLIGHT (Step 0) -- read-only diagnostics")
    print("Cache dir:", CACHE_DIR.resolve())
    print("=" * 72)
    if not ORBIT_PATHS.exists() or not OSC_CACHE.exists():
        print("\n[FATAL] cache(s) not found under", CACHE_DIR.resolve())
        return
    cache = _load_json(ORBIT_PATHS)
    print("\norbit_paths.json: %d pair keys" % len(cache))

    print("\n--- 0a/0c/0e: presence, key format, cadence, units ---")
    moon_cadence = {}
    for k in PREFLIGHT_PAIR_KEYS:
        entry = cache.get(k, {})
        if not entry:
            print("  %-16s ABSENT" % k)
            continue
        dp = entry.get('data_points', {})
        meta = entry.get('metadata', {})
        keys = sorted(dp.keys())
        fmt = _key_format(keys)
        spacing = _median_spacing_days(keys) if fmt == 'date-only' else None
        cad = ("%.3f d/step" % spacing) if spacing is not None else "(%s)" % fmt
        span = ("%s .. %s" % (keys[0], keys[-1])) if keys else "N/A"
        print("  %-16s %5d pts | %-12s | %-9s | %s | center=%s"
              % (k, len(keys), fmt, cad, span, meta.get('center_body', 'N/A')))
        if keys:
            p = dp[keys[0]]
            try:
                mag = (p['x'] ** 2 + p['y'] ** 2 + p['z'] ** 2) ** 0.5
                unit = "AU" if mag < 1e4 else "LOOKS LIKE km -- STOP"
                print("       first-pt |r|=%.4g -> %s" % (mag, unit))
            except (KeyError, TypeError):
                pass
        slug = {'Moon_Sun': 'Moon', 'Io_Sun': 'Io', 'Titan_Sun': 'Titan',
                'Charon_Sun': 'Charon'}.get(k)
        if slug and spacing is not None:
            moon_cadence[slug] = spacing

    print("\n--- 0b: Pluto pair -- which Horizons target? ---")
    pl_meta = cache.get('Pluto_Sun', {}).get('metadata', {})
    print("  Pluto_Sun center_body=%s horizons_id=%s"
          % (pl_meta.get('center_body'), pl_meta.get('horizons_id')))

    print("\n--- 0d: imports ---")
    print("  constants_new.KM_PER_AU: %s" % KM_PER_AU)
    try:
        from celestial_objects import OBJECT_DEFINITIONS
        print("  celestial_objects.OBJECT_DEFINITIONS: %d" % len(OBJECT_DEFINITIONS))
    except Exception as exc:
        print("  [WARN] celestial_objects import failed: %r" % exc)

    print("\n--- 0f: osculating cache structure ---")
    osc = _load_json(OSC_CACHE)
    print("  osculating entries: %d" % len(osc))
    osc_tranche = [o.osc_key for o in TEST_OBJECTS if o.osc_key]
    present = sum(1 for k in osc_tranche if k in osc)
    with_time = sum(1 for k in osc_tranche
                    if k in osc and ':' in str(osc[k].get('elements', {}).get('epoch', '')))
    ma_none = sum(1 for k in osc_tranche
                  if k in osc and osc[k].get('elements', {}).get('MA') is None)
    print("  tranche osc keys present: %d/%d" % (present, len(osc_tranche)))
    print("  epochs carrying HH:MM: %d/%d" % (with_time, present))
    print("  entries with MA=None:  %d/%d" % (ma_none, present))

    print("\n" + "=" * 72)
    print("STEP 0-STOP: moon-cadence -- orbit ALWAYS ships (osculating);")
    print("the question is whether the direct position TRACE is added.")
    print("=" * 72)
    for slug in ('Moon', 'Io', 'Titan', 'Charon'):
        step = moon_cadence.get(slug)
        per = KNOWN_ORBITAL_PERIODS.get(slug)
        if step is None or per is None:
            print("  %-7s : no date-only cadence / period" % slug)
            continue
        ppo = per / step if step > 0 else float('inf')
        verdict = ("trace UNUSABLE (osculating only)" if ppo < 3 else
                   "trace chunky (Mode 5)" if ppo < 40 else "trace fine")
        print("  %-7s : %.3f d/step, period %.3f d -> ~%.1f pts/orbit [%s]"
              % (slug, step, per, ppo, verdict))
    print("=" * 72)


# ---------------------------------------------------------------------------
# Step 4: build a coverage-index osculating block
# ---------------------------------------------------------------------------
def build_osculating_entry(osc_cache, obj, warn):
    osc = osc_cache.get(obj.osc_key)
    if osc is None:
        warn("osculating key %r missing for %s" % (obj.osc_key, obj.slug))
        return None
    els = osc.get('elements', {})
    md = osc.get('metadata', {})
    e = els.get('e')
    ma = els.get('MA')
    ta = els.get('TA')
    if ma is not None:
        m0 = float(ma) % 360.0
    elif ta is not None:
        m0 = _true_to_mean_anomaly_deg(float(ta), float(e) if e is not None else None)
        if m0 is None:
            warn("%s: MA=None and TA->M0 not possible (e=%r); M0 omitted"
                 % (obj.slug, e))
        else:
            warn("%s: MA=None; M0 derived from TA" % obj.slug)
    else:
        m0 = None
        warn("%s: MA and TA both None; M0 omitted" % obj.slug)

    center_slug = resolve_center_slug(md.get('center_body'))
    # #C center-match (the Charon@9 lesson): elements center == served center.
    if center_slug != obj.stored_center:
        raise AssertionError(
            "center mismatch for %s: osculating %s != stored_center %s"
            % (obj.slug, center_slug, obj.stored_center))

    epoch = els.get('epoch')
    return {
        'center': center_slug,
        'epoch_jd': parse_osc_epoch_to_jd(epoch) if epoch else None,
        'a_au': float(els['a']),
        'e': float(e) if e is not None else None,
        'i_deg': float(els['i']),
        'node_deg': float(els['Omega']),
        'peri_deg': float(els['omega']),
        'M0_deg': m0,
        'source': {
            'query_target': md.get('horizons_id'),
            'center': md.get('center_body'),
            'epoch': epoch,
            'retrieved': md.get('fetched'),
        },
    }


# ---------------------------------------------------------------------------
# Step 3: write a position file from a DIRECT relative pair (no subtraction)
# ---------------------------------------------------------------------------
def write_position_file(cache, obj, out_dir, warn):
    entry = cache.get(obj.position_pair_key)
    if not entry:
        warn("position pair %r missing for %s -> positions:null"
             % (obj.position_pair_key, obj.slug))
        return None
    dp = entry.get('data_points', {})
    dates = sorted(dp.keys())
    if not dates:
        warn("position pair %r empty for %s" % (obj.position_pair_key, obj.slug))
        return None

    md = entry.get('metadata', {})
    mcb = md.get('center_body')  # informational only -- unreliable label (many
                                 # writer paths default to 'Sun'); NOT trusted
                                 # for the frame check (see the guard below).

    t, xs, ys, zs = [], [], [], []
    max_r_km = 0.0
    for d in dates:
        p = dp[d]
        t.append(_dt_to_jd(_parse_calendar(d)))
        x, y, z = p['x'] * KM_PER_AU, p['y'] * KM_PER_AU, p['z'] * KM_PER_AU
        xs.append(x); ys.append(y); zs.append(z)
        r = (x * x + y * y + z * z) ** 0.5
        if r > max_r_km:
            max_r_km = r

    # Frame-contamination guard (replaces the center_body-string check, which
    # false-alarmed on stale labels AND missed real contamination). A parent-
    # or barycenter-relative trace must NOT contain heliocentric-scale points:
    # a cache pair can accumulate points from a heliocentric fetch merged under
    # a relative-frame key (observed on Pluto/Charon: the pre-2027-02 tail was
    # ~35 AU). 0.5 AU is far above any real moon/barycenter orbit (the Moon is
    # ~0.003 AU, distant irregulars stay well under) and far below any
    # heliocentric radius (>= the system's AU distance). If tripped, drop the
    # whole trace to osculating-only -- a half-contaminated trace renders as a
    # broken orbit; the osculating conic renders clean. Repair the cache source.
    if obj.canonical_frame not in ('heliocentric', 'arc-natural'):
        max_r_au = max_r_km / KM_PER_AU
        if max_r_au > 0.5:
            warn("%s: FRAME CONTAMINATION -- %s trace reaches %.2f AU "
                 "(heliocentric-scale) in pair %r; the cache pair mixes frames. "
                 "Trace DROPPED to osculating-only. Repair the cache source."
                 % (obj.slug, obj.canonical_frame, max_r_au, obj.position_pair_key))
            return None

    start, end = dates[0][:10], dates[-1][:10]
    spacing = _median_spacing_days(dates)
    step_hours = int(round(spacing * 24)) if spacing is not None else None

    payload = {
        'object': obj.slug,
        'center': obj.stored_center,
        'frame': obj.canonical_frame,
        'unit': 'km',
        'epoch_type': 'JD',
        'source': {
            'query_target': md.get('horizons_id'),
            'center': mcb,
            'epoch': "%s to %s" % (start, end),
            'retrieved': md.get('last_updated'),
        },
        'data': {'t': t, 'x': xs, 'y': ys, 'z': zs},
    }
    (out_dir / 'positions').mkdir(parents=True, exist_ok=True)
    path = out_dir / 'positions' / ("%s.json" % obj.slug)
    with open(path, 'w') as fh:
        json.dump(payload, fh)
    size_kb = int(round(os.path.getsize(path) / 1024.0))
    return {
        'file': "positions/%s.json" % obj.slug,
        'start': start, 'end': end,
        'step_hours': step_hours,
        'n_points': len(t),
        'size_kb': size_kb,
    }


# ---------------------------------------------------------------------------
# Step 5: assemble the coverage index + assert invariants (v4 set)
# ---------------------------------------------------------------------------
def assert_invariants(index, out_dir):
    for slug, o in index['objects'].items():
        av = o['availability']
        osc = o['osculating']
        pos = o['positions']
        if av == 'spacecraft':
            assert osc is None, "#2 %s spacecraft has osculating" % slug
            assert pos is not None, "#2 %s spacecraft has no positions" % slug
        if av == 'analytic':
            assert osc is not None, "#3 %s analytic missing osculating" % slug
        if osc is not None:
            assert osc['center'] in VALID_SLUGS, \
                "#5 %s osculating center invalid: %r" % (slug, osc['center'])
            # #C center-match
            assert osc['center'] == o['stored_center'], \
                "#C %s osc.center %s != stored_center %s" % (slug, osc['center'], o['stored_center'])
        if pos is not None:
            assert (out_dir / pos['file']).exists(), \
                "#8 %s positions file missing: %s" % (slug, pos['file'])
        for preset in (o['presets'] or []):
            assert (out_dir / preset['positions']['file']).exists(), \
                "#6 %s preset file missing" % slug
    print("  invariants #2,#3,#5,#6,#8,#C: PASS")


def write_feature_configs(out_dir, warn):
    """Step 6: best-effort feature params from SHELL_CONFIGS (pulls plotly)."""
    try:
        from shell_configs import SHELL_CONFIGS
    except Exception as exc:
        warn("shell_configs unavailable (%r); feature_configs.json skipped" % exc)
        return
    used = set()
    for o in TEST_OBJECTS:
        if o.features:
            used.update(o.features)
    configs = {}
    for name in sorted(used):
        cfg = SHELL_CONFIGS.get(name) if isinstance(SHELL_CONFIGS, dict) else None
        if cfg is None:
            warn("feature %r not in SHELL_CONFIGS" % name)
            continue
        configs[name] = {'renderer': cfg.get('renderer', cfg.get('type', 'unknown'))}
    with open(out_dir / 'feature_configs.json', 'w') as fh:
        json.dump({'schema_version': SCHEMA_VERSION, 'features': configs}, fh, indent=2)
    print("  feature_configs.json: %d feature(s)" % len(configs))


def run_export(output_dir, full_catalog):
    if full_catalog:
        print("[note] --full-catalog is a follow-on; this build is tranche-scoped.")
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    warnings_log = []
    warn = warnings_log.append

    print("Loading caches from", CACHE_DIR.resolve())
    if not ORBIT_PATHS.exists() or not OSC_CACHE.exists():
        print("[FATAL] cache(s) not found under", CACHE_DIR.resolve())
        return 1
    cache = _load_json(ORBIT_PATHS)
    osc_cache = _load_json(OSC_CACHE)

    objects = {}
    files_written = 0
    for obj in TEST_OBJECTS:
        osc_block = build_osculating_entry(osc_cache, obj, warn) if obj.osc_key else None
        pos_block = None
        if obj.trace_policy == 'serve' and obj.position_pair_key is not None:
            pos_block = write_position_file(cache, obj, out_dir, warn)
            if pos_block is not None:
                files_written += 1
        objects[obj.slug] = {
            'name': obj.name,
            'horizons_id': obj.horizons_id,
            'category': obj.category,
            'availability': obj.availability,
            'parent': obj.parent,
            'stored_center': obj.stored_center,
            'canonical_frame': obj.canonical_frame,
            'trajectory_of': obj.trajectory_of,
            'osculating': osc_block,
            'positions': pos_block,
            'presets': None,          # none in this tranche (Apophis 2029 absent)
            'features': obj.features,
        }

    index = {
        'schema_version': SCHEMA_VERSION,
        'generated': datetime.now(timezone.utc).isoformat(),
        'generator': GENERATOR,
        'serving_base': str(output_dir),
        'feature_configs': 'feature_configs.json',
        'scene_features': SCENE_FEATURES,
        'model': {
            'orbit_source': 'osculating-primary',
            'positions': 'direct-horizons-relative',
            'subtraction': 'not-used',
            'note': 'v4: orbit renders from osculating; trace is additive.',
        },
        'objects': objects,
    }

    print("Asserting invariants...")
    assert_invariants(index, out_dir)

    with open(out_dir / 'coverage_index.json', 'w') as fh:
        json.dump(index, fh, indent=2)
    write_feature_configs(out_dir, warn)

    served = [s for s, o in objects.items() if o['positions']]
    osc_only = [s for s, o in objects.items()
                if o['osculating'] and not o['positions']]
    print("\nSummary")
    print("  objects:          %d" % len(objects))
    print("  position files:   %d  (%s)" % (files_written, ", ".join(served)))
    print("  osculating-only:  %s" % ", ".join(osc_only))
    print("  coverage_index.json + feature_configs.json written")
    if warnings_log:
        print("  warnings (%d):" % len(warnings_log))
        for w in warnings_log:
            print("    - " + w)
    else:
        print("  warnings: none")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Phase 1b orbit-cache exporter (v4: osculating-primary).")
    parser.add_argument('--output-dir', default='./_export_out',
                        help='output dir (default: ./_export_out scratch; pass '
                             'the gallery data path explicitly to deploy)')
    parser.add_argument('--full-catalog', action='store_true')
    parser.add_argument('--preflight-only', action='store_true')
    args = parser.parse_args(argv)
    if args.preflight_only:
        run_preflight()
        return 0
    return run_export(args.output_dir, args.full_catalog)


if __name__ == '__main__':
    sys.exit(main())
