"""
export_orbit_cache.py - Phase 1b desktop devtool: read local orbit caches and
write web-servable position/coverage files for the interactive gallery.

Runs on Tony's desktop only (never in the browser); reads the local caches
read-only and never modifies them. This file is delivered in STAGES per the
Phase 1b build manifest v3: Stage 1 (Step 0 pre-flight, below) is complete and
runnable now; Stage 2 (Steps 1-6, the export) is written after the pre-flight
output is captured and the Step 0-STOP moon-cadence branch is ruled on, because
both depend on facts only the primary cache can supply.

Key functions:
    run_preflight()      - Step 0 (0a-0f) diagnostics + the Step 0-STOP summary
    resolve_center_slug() - map a Horizons center_body to a schema slug
    main()               - CLI entry (--preflight-only works today)

Consumed by: Tony's desktop (manual run); output copied to
tonyquintanilla.github.io/data/solar-system/

Module updated: July 2026 with Anthropic's Claude Opus 4.8
"""

import argparse
import json
import sys
from collections import namedtuple
from pathlib import Path
from statistics import median

# The caches live in ./data relative to this script (verified against
# osculating_cache_manager.py at orrery HEAD: CACHE_DIR = __file__ parent /'data').
CACHE_DIR = Path(__file__).parent / 'data'
ORBIT_PATHS = CACHE_DIR / 'orbit_paths.json'
OSC_CACHE = CACHE_DIR / 'osculating_cache.json'


# ---------------------------------------------------------------------------
# Step 2 scaffolding (decision-independent; used by both pre-flight and export)
# ---------------------------------------------------------------------------

# Horizons center_body -> schema slug. Explicit map, not string-strip.
CENTER_SLUG_MAP = {
    '@sun': 'sun', '@0': 'sun', '@10': 'sun', 'Sun': 'sun', '0': 'sun',
    '@399': 'earth', '399': 'earth',
    '@599': 'jupiter', '599': 'jupiter',
    '@699': 'saturn', '699': 'saturn',
    '@9': 'pluto_barycenter', '9': 'pluto_barycenter',
}


def resolve_center_slug(center_body_str):
    """Map a Horizons center_body string to a schema slug. Rejects unmapped."""
    if center_body_str is None:
        raise ValueError("center_body is None")
    slug = CENTER_SLUG_MAP.get(center_body_str)
    if slug is None:
        slug = CENTER_SLUG_MAP.get(str(center_body_str).lstrip('@'))
    if slug is None:
        raise ValueError("Unmapped center_body: %r" % (center_body_str,))
    return slug


TestObject = namedtuple('TestObject',
    'slug cache_pair_key osc_key horizons_id category availability '
    'parent stored_center canonical_frame trajectory_of features')

TEST_OBJECTS = [
    TestObject("earth",     "Earth_Sun",     "Earth",     "399",   "planet",       "analytic",       "sun",     "sun",              "heliocentric",    None,               ["van_allen_belts", "atmosphere_shell"]),
    TestObject("jupiter",   "Jupiter_Sun",   "Jupiter",   "599",   "planet",       "analytic",       "sun",     "sun",              "heliocentric",    None,               ["magnetosphere", "ring_system"]),
    TestObject("saturn",    "Saturn_Sun",    "Saturn",    "699",   "planet",       "analytic",       "sun",     "sun",              "heliocentric",    None,               ["ring_system"]),
    TestObject("moon",      "Moon_Sun",      "Moon",      "301",   "moon",         "cache-required", "earth",   "earth",            "parent-relative", None,               None),
    TestObject("io",        "Io_Sun",        "Io",        "501",   "moon",         "cache-required", "jupiter", "jupiter",          "parent-relative", None,               None),
    TestObject("titan",     "Titan_Sun",     "Titan",     "606",   "moon",         "cache-required", "saturn",  "saturn",           "parent-relative", None,               None),
    TestObject("pluto",     "Pluto_Sun",     "Pluto",     "999",   "dwarf_planet", "analytic",       "sun",     "sun",              "heliocentric",    "pluto_barycenter", None),
    TestObject("charon",    "Charon_Sun",    "Charon@9",  "901",   "moon",         "cache-required", "pluto",   "pluto_barycenter", "parent-relative", None,               None),
    TestObject("apophis",   "Apophis_Sun",   "Apophis",   "99942", "asteroid",     "analytic",       "sun",     "sun",              "heliocentric",    None,               None),
    TestObject("voyager_1", "Voyager 1_Sun", None,        "-31",   "spacecraft",   "spacecraft",     "sun",     "sun",              "arc-natural",     None,               None),
]

# Parents whose position files are required for moon composition.
PARENT_OBJECTS = {"earth", "jupiter", "saturn", "pluto"}

# Objects that need position files written. Keyed on availability (NOT category:
# the v2 comprehension read the category field and silently dropped all moons).
NEEDS_POSITIONS = {o.slug for o in TEST_OBJECTS
                   if o.availability in ("cache-required", "spacecraft")} \
                  | PARENT_OBJECTS

# Sidereal periods of the served moons, in DAYS. RECALLED approximations, used
# ONLY to translate on-disk cadence into a points-per-orbit sanity figure in the
# Step 0-STOP print. Not a served value; not embedded in any output file. If the
# figure is load-bearing for the ruling, confirm the period against JPL.
_MOON_PERIOD_DAYS_APPROX = {
    'moon': 27.32, 'io': 1.77, 'titan': 15.95, 'charon': 6.39,
}


# ---------------------------------------------------------------------------
# Step 0: pre-flight verification
# ---------------------------------------------------------------------------

def _load_json(path):
    with open(path, 'r') as fh:
        return json.load(fh)


def _key_format(keys):
    """Classify sorted date keys as date-only or time-bearing."""
    if not keys:
        return 'none'
    k0 = keys[0]
    return 'time-bearing' if (':' in k0 or 'T' in k0) else 'date-only'


def _median_spacing_days(date_keys):
    """Median gap (days) between consecutive date-only keys. None if not
    date-only or < 2 points."""
    if len(date_keys) < 2:
        return None
    from datetime import datetime
    parsed = []
    for k in date_keys:
        try:
            parsed.append(datetime.strptime(k[:10], '%Y-%m-%d'))
        except ValueError:
            return None  # time-bearing or unexpected -- caller reports format
    parsed.sort()
    gaps = [(parsed[i + 1] - parsed[i]).total_seconds() / 86400.0
            for i in range(len(parsed) - 1)]
    return median(gaps) if gaps else None


TRANCHE_PAIR_KEYS = [
    'Earth_Sun', 'Jupiter_Sun', 'Saturn_Sun', 'Pluto_Sun', 'Moon_Sun',
    'Io_Sun', 'Titan_Sun', 'Charon_Sun', 'Voyager 1_Sun', 'Apophis_Sun',
]


def run_preflight():
    """Run Step 0 (0a-0f) + Step 0-STOP summary. Read-only. Returns nothing;
    prints the ground truth the build proceeds on. Capture and paste into the
    build session."""
    print("=" * 72)
    print("PHASE 1B PRE-FLIGHT (Step 0) -- read-only diagnostics")
    print("Cache dir:", CACHE_DIR.resolve())
    print("=" * 72)

    if not ORBIT_PATHS.exists():
        print("\n[FATAL] %s not found. Run this on the desktop where the "
              "primary orbit cache lives." % ORBIT_PATHS)
        return
    if not OSC_CACHE.exists():
        print("\n[FATAL] %s not found." % OSC_CACHE)
        return

    cache = _load_json(ORBIT_PATHS)
    print("\norbit_paths.json: %d top-level pair keys" % len(cache))

    # 0a + 0c + 0e: presence, key format, cadence, coverage, unit sanity ------
    print("\n--- 0a/0c/0e: tranche presence, key format, cadence, units ---")
    moon_cadence = {}
    for k in TRANCHE_PAIR_KEYS:
        entry = cache.get(k, {})
        if not entry:
            print("  %-16s ABSENT" % k)
            continue
        dp = entry.get('data_points', {})
        meta = entry.get('metadata', {})
        keys = sorted(dp.keys())
        fmt = _key_format(keys)
        span = ("%s .. %s" % (keys[0], keys[-1])) if keys else "N/A"
        spacing = _median_spacing_days(keys) if fmt == 'date-only' else None
        cad = ("%.3f d/step" % spacing) if spacing is not None else "(%s)" % fmt
        print("  %-16s %5d pts | %-12s | %-9s | %s | center=%s"
              % (k, len(keys), fmt, cad, span, meta.get('center_body', 'N/A')))
        # unit sanity on first point
        if keys:
            p = dp[keys[0]]
            try:
                mag = (p['x'] ** 2 + p['y'] ** 2 + p['z'] ** 2) ** 0.5
                unit = "AU (expected)" if mag < 1e4 else "LOOKS LIKE km -- STOP, reconcile"
                print("       first-pt |r|=%.4g  -> %s" % (mag, unit))
            except (KeyError, TypeError):
                print("       (could not read x/y/z on first point)")
        # capture moon cadence for the STOP summary
        slug = {'Moon_Sun': 'moon', 'Io_Sun': 'io', 'Titan_Sun': 'titan',
                'Charon_Sun': 'charon'}.get(k)
        if slug and spacing is not None:
            moon_cadence[slug] = spacing

    # 0b: Pluto target (9 barycenter vs 999 body) -----------------------------
    print("\n--- 0b: Pluto pair -- which Horizons target? ---")
    pl = cache.get('Pluto_Sun', {})
    pl_meta = pl.get('metadata', {})
    print("  Pluto_Sun center_body=%s  horizons_id=%s  pts=%d"
          % (pl_meta.get('center_body'), pl_meta.get('horizons_id'),
             len(pl.get('data_points', {}))))
    print("  (target 9 -> Charon subtraction consistent; pluto.json is the")
    print("   barycenter trajectory. target 999 -> mismatch; see Step 0-STOP.)")

    # 0d: imports (informational; shell_configs pulling plotly is EXPECTED) ----
    print("\n--- 0d: imports ---")
    try:
        from celestial_objects import OBJECT_DEFINITIONS
        print("  celestial_objects.OBJECT_DEFINITIONS: %d objects"
              % len(OBJECT_DEFINITIONS))
    except Exception as exc:
        print("  [WARN] celestial_objects import failed: %r" % exc)
    try:
        from constants_new import KM_PER_AU
        print("  constants_new.KM_PER_AU: %s" % KM_PER_AU)
    except Exception as exc:
        print("  [WARN] constants_new import failed: %r" % exc)
    try:
        from shell_configs import SHELL_CONFIGS  # noqa: F401 (pulls plotly; fine)
        print("  shell_configs.SHELL_CONFIGS: imported (plotly loaded "
              "transitively -- expected, not a defect)")
    except Exception as exc:
        print("  [WARN] shell_configs import failed: %r" % exc)

    # 0f: osculating cache structure ------------------------------------------
    print("\n--- 0f: osculating cache structure ---")
    osc = _load_json(OSC_CACHE)
    print("  osculating entries: %d" % len(osc))
    if 'Charon@9' not in osc:
        print("  [FATAL] Charon@9 barycentric elements missing")
    else:
        print("  Charon@9 present; center_body=%s (must map -> pluto_barycenter)"
              % osc['Charon@9'].get('metadata', {}).get('center_body'))
    # epoch format + MA/TA across tranche osculating keys
    osc_tranche = ['Earth', 'Jupiter', 'Saturn', 'Pluto', 'Moon', 'Io',
                   'Titan', 'Charon@9', 'Apophis']
    epochs_with_time = 0
    ma_none = 0
    present = 0
    for name in osc_tranche:
        e = osc.get(name)
        if not e:
            print("  %-10s ABSENT" % name)
            continue
        present += 1
        els = e.get('elements', {})
        epoch = els.get('epoch')
        if epoch and ':' in str(epoch):
            epochs_with_time += 1
        if els.get('MA') is None:
            ma_none += 1
    print("  tranche osc entries present: %d/%d" % (present, len(osc_tranche)))
    print("  epochs carrying HH:MM: %d/%d" % (epochs_with_time, present))
    print("  entries with MA=None:  %d/%d" % (ma_none, present))
    print("  NOTE (export Step 4): epoch parser must accept BOTH")
    print("       'YYYY-MM-DD HH:MM osc.' and 'YYYY-MM-DD osc.' -- strip the")
    print("       trailing ' osc.' and parse the remainder; do NOT split-and-")
    print("       take-date-only, which drops the time-of-day (up to ~1d epoch")
    print("       error on M0).")

    # Step 0-STOP: moon-cadence decision gate ---------------------------------
    print("\n" + "=" * 72)
    print("STEP 0-STOP: moon-cadence decision gate")
    print("=" * 72)
    if not moon_cadence:
        print("  No date-only moon cadence captured (moons ABSENT, time-bearing,")
        print("  or Pluto/Saturn missing). If moons are ABSENT in the primary,")
        print("  the tranche cannot ship parent-relative moons at all -- report.")
    for slug in ('moon', 'io', 'titan', 'charon'):
        step = moon_cadence.get(slug)
        if step is None:
            print("  %-7s : no date-only cadence (absent or time-bearing)" % slug)
            continue
        per = _MOON_PERIOD_DAYS_APPROX[slug]
        ppo = per / step if step > 0 else float('inf')
        verdict = ("UNUSABLE" if ppo < 3 else
                   "chunky (Mode 5 call)" if ppo < 40 else "fine")
        print("  %-7s : %.3f d/step, period~%.2f d -> ~%.1f pts/orbit  [%s]"
              % (slug, step, per, ppo, verdict))
    print("\n  Branch (i)  ship the daily tranche; inner moons below the usable")
    print("              threshold drop to analytic-only (conic still renders).")
    print("  Branch (ii) pull the desktop time-keyed-cache change into Phase 1b")
    print("              (orbit_data_manager.py) and re-fetch moons sub-daily.")
    print("  Ruling is Tony's, informed by the pts/orbit figures above.")
    print("=" * 72)


# ---------------------------------------------------------------------------
# Stage 2 (Steps 1-6): the export. Written after pre-flight + Step 0-STOP.
# ---------------------------------------------------------------------------

def run_export(output_dir, full_catalog):
    print("Export path is not yet implemented.")
    print("Per manifest v3, Steps 1-6 are written AFTER:")
    print("  (1) the Step 0 pre-flight output is captured from the primary cache")
    print("      (run: python export_orbit_cache.py --preflight-only), and")
    print("  (2) Tony rules on the Step 0-STOP moon-cadence branch (i)/(ii).")
    print("Nothing was written.")
    return 2


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Phase 1b orbit-cache exporter (Stage 1: pre-flight).")
    parser.add_argument('--output-dir',
                        default='../tonyquintanilla.github.io/data/solar-system/',
                        help='where the export writes (Stage 2)')
    parser.add_argument('--full-catalog', action='store_true',
                        help='export all cached objects, not just the tranche '
                             '(Stage 2)')
    parser.add_argument('--preflight-only', action='store_true',
                        help='run Step 0 diagnostics and stop (works today)')
    args = parser.parse_args(argv)

    if args.preflight_only:
        run_preflight()
        return 0
    return run_export(args.output_dir, args.full_catalog)


if __name__ == '__main__':
    sys.exit(main())
