"""
close_approach_data.py - JPL CAD API client for small-body close approach data.

Fetches and caches close approach data from JPL's Small Body Close Approach
Data (CAD) API. Returns center-to-center distances plus derived surface
distances using canonical center-body radii from constants_new.py. Supports
any small body against any major planet (plus Moon, Pluto).

Motivated by Apophis (99942) Earth flyby on April 13, 2029 (Friday the 13th).

API endpoint: https://ssd-api.jpl.nasa.gov/cad.api
Cache: data/close_approach_cache.json under 'close_approach:DESIGNATION:BODY' keys.

Key functions:
    get_close_approaches(designation, body, date_min, date_max) - all approaches
    get_closest_approach(designation, body, date_min, date_max) - single closest

Usage:
    from close_approach_data import get_closest_approach
    approach = get_closest_approach('99942', body='Earth',
                                     date_min='2029-01-01', date_max='2030-01-01')
    if approach:
        print(f"Perigee: {approach['date']}")
        print(f"Distance: {approach['dist_km']:.1f} km center-to-center")
        print(f"Velocity: {approach['v_rel_kms']:.3f} km/s")

Consumed by: palomas_orrery.py (Apophis and other close-approach plots)

Part of Paloma's Orrery - Data Preservation is Climate Action
Created: March 2026

Module updated: April 17, 2026 with Anthropic's Claude Opus 4.7
(provenance audit; local AU conversion and radii dict replaced with imports
from constants_new.py. The previous local radii dict had pre-April-16
volumetric-mean values, so Jupiter surface distances were off by ~1,580 km
and Saturn by ~2,000 km under the current Hybrid Radius Convention.
Consolidation fixes that staleness.)
"""

import json
import os
import urllib.request
import urllib.parse
from datetime import datetime, date
from pathlib import Path

from constants_new import KM_PER_AU, CENTER_BODY_RADII

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CAD_API_URL = "https://ssd-api.jpl.nasa.gov/cad.api"

# Local alias preserved for minimal churn in existing callsites.
# Canonical source: constants_new.KM_PER_AU.
AU_TO_KM = KM_PER_AU

# Surface radii for center bodies now come from constants_new.CENTER_BODY_RADII
# (canonical, hybrid convention: equatorial for major planets, volumetric for
# small bodies). Previously a local dict carried pre-April-16 volumetric values.

# Abbreviated body names accepted by the CAD API
# See: https://ssd-api.jpl.nasa.gov/doc/cad.html
CAD_BODY_NAMES = {
    'Mercury': 'Merc',
    'Venus':   'Venus',
    'Earth':   'Earth',
    'Moon':    'Moon',
    'Mars':    'Mars',
    'Jupiter': 'Juptr',
    'Saturn':  'Satrn',
    'Uranus':  'Urnus',
    'Neptune': 'Neptn',
    'Pluto':   'Pluto',
    'ALL':     'ALL',
}

# Canonical body name lookup (reverse of above + aliases)
_BODY_CANONICAL = {v: k for k, v in CAD_BODY_NAMES.items()}
_BODY_CANONICAL['Earth'] = 'Earth'   # already canonical


# ---------------------------------------------------------------------------
# Cache helpers
# CAD data lives in its OWN file (data/close_approach_cache.json), NOT in
# orbit_paths.json. The orbit_paths validator expects data_points or x/y/z
# arrays -- our close approach dicts have neither, which triggers the cache
# repair logic and removes the entry, reducing the count by 1, which then
# trips the size-reduction safety check and blocks the save on every startup.
# Separate file = no collision with orbit_paths validation.
# ---------------------------------------------------------------------------

CAD_CACHE_FILENAME = 'close_approach_cache.json'


def _get_cache_path():
    """Return path to close_approach_cache.json, searching common locations."""
    candidates = [
        Path('data') / CAD_CACHE_FILENAME,
        Path(__file__).parent / 'data' / CAD_CACHE_FILENAME,
        Path(CAD_CACHE_FILENAME),
    ]
    for p in candidates:
        if p.exists():
            return p
    # Default: data/ relative to this file (created on first save)
    default = Path(__file__).parent / 'data' / CAD_CACHE_FILENAME
    return default


def _load_cache():
    cache_path = _get_cache_path()
    if cache_path.exists():
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"[CAD] Warning: Could not load cache from {cache_path}: {e}", flush=True)
    return {}


def _save_cache(cache):
    """Save cache with two-generation backup protection."""
    import shutil
    cache_path = _get_cache_path()
    cache_path.parent.mkdir(parents=True, exist_ok=True)

    # Two-generation backup (bak1 = previous run, bak2 = one before that)
    backup1 = cache_path.with_suffix('.json.bak1')
    backup2 = cache_path.with_suffix('.json.bak2')

    if backup1.exists():
        try:
            shutil.copy2(backup1, backup2)
        except Exception as e:
            print(f"[CAD] Warning: Could not rotate backup: {e}", flush=True)

    if cache_path.exists():
        try:
            shutil.copy2(cache_path, backup1)
        except Exception as e:
            print(f"[CAD] Warning: Could not create backup: {e}", flush=True)

    try:
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2)
        print(f"[CAD] Cache saved: {cache_path}", flush=True)
    except IOError as e:
        print(f"[CAD] Error: Could not save cache: {e}", flush=True)


def _cache_key(designation, body):
    """Build cache key for a given designation + body pair."""
    # Normalize body to canonical name
    canonical_body = _BODY_CANONICAL.get(body, body)
    return f"close_approach:{designation}:{canonical_body}"


# ---------------------------------------------------------------------------
# Raw API fetch
# ---------------------------------------------------------------------------

def _fetch_from_api(designation, body='Earth', date_min=None, date_max=None,
                    dist_max='0.5'):
    """
    Query JPL CAD API and return parsed list of approach dicts.

    Parameters:
        designation (str): Small body designation e.g. '99942', 'C/2023 A3'
        body (str): Major body name (canonical or CAD abbreviated)
        date_min (str): Start date 'YYYY-MM-DD' (optional)
        date_max (str): End date 'YYYY-MM-DD' (optional)
        dist_max (str): Maximum distance in AU (default '0.5')

    Returns:
        list[dict] | None: Parsed approach list or None on failure
    """
    cad_body = CAD_BODY_NAMES.get(body, body)   # translate to CAD abbreviation

    params = {
        'des':       designation,
        'body':      cad_body,
        'dist-max':  dist_max,
        'fullname':  '1',   # include full designation in response
    }
    if date_min:
        params['date-min'] = date_min
    if date_max:
        params['date-max'] = date_max

    url = CAD_API_URL + '?' + urllib.parse.urlencode(params)
    print(f"[CAD] Querying: {url}", flush=True)

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            raw = response.read().decode('utf-8')
    except Exception as e:
        print(f"[CAD] Network error: {e}", flush=True)
        return None

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[CAD] JSON parse error: {e}", flush=True)
        return None

    # Check for API-level error
    if 'message' in data and data.get('count', 1) == 0:
        print(f"[CAD] API message: {data['message']}", flush=True)
        return []

    if 'data' not in data or not data['data']:
        print(f"[CAD] No close approach data returned for {designation} near {body}", flush=True)
        return []

    # Parse fields header
    fields = data.get('fields', [])
    # Expected fields from CAD API: des, orbit_id, jd, cd, dist, dist_min,
    # dist_max, v_rel, v_inf, t_sigma_f, h
    # (field names vary by API version; use index-based access with fallback)

    def field_idx(name, *aliases):
        """Return index of first matching field name."""
        for n in (name,) + aliases:
            if n in fields:
                return fields.index(n)
        return None

    i_jd       = field_idx('jd')
    i_cd       = field_idx('cd')
    i_dist     = field_idx('dist')
    i_dist_min = field_idx('dist_min')
    i_dist_max = field_idx('dist_max')
    i_v_rel    = field_idx('v_rel')
    i_v_inf    = field_idx('v_inf')
    i_h        = field_idx('h')
    i_orbit_id = field_idx('orbit_id')

    def safe_float(row, idx):
        if idx is None or idx >= len(row):
            return None
        val = row[idx]
        if val is None or val == '':
            return None
        try:
            return float(val)
        except (ValueError, TypeError):
            return None

    approaches = []
    for row in data['data']:
        jd   = safe_float(row, i_jd)
        dist = safe_float(row, i_dist)
        if jd is None or dist is None:
            continue   # Skip malformed rows

        dist_min = safe_float(row, i_dist_min)
        dist_max_val = safe_float(row, i_dist_max)
        v_rel    = safe_float(row, i_v_rel)
        v_inf    = safe_float(row, i_v_inf)
        h_mag    = safe_float(row, i_h)
        orbit_id = row[i_orbit_id] if i_orbit_id is not None else None

        date_str = row[i_cd] if i_cd is not None else None
        # Tidy up date string (CAD returns e.g. '2029-Apr-13 21:46')
        if date_str:
            date_str = str(date_str).strip()

        dist_km = dist * AU_TO_KM
        surface_km = None
        canonical_body = _BODY_CANONICAL.get(cad_body, body)
        if canonical_body in CENTER_BODY_RADII:
            surface_km = dist_km - CENTER_BODY_RADII[canonical_body]

        approaches.append({
            'jd':          jd,
            'date':        date_str,
            'dist_au':     dist,
            'dist_km':     dist_km,
            'dist_min_au': dist_min,
            'dist_max_au': dist_max_val,
            'surface_km':  surface_km,
            'v_rel_kms':   v_rel,
            'v_inf_kms':   v_inf,
            'h_mag':       h_mag,
            'orbit_id':    orbit_id,
        })

    print(f"[CAD] Parsed {len(approaches)} approach(es) for {designation} near {body}", flush=True)
    return approaches


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_close_approaches(designation, body='Earth', date_min=None, date_max=None,
                          dist_max='0.5', force_refresh=False):
    """
    Return list of close approach events for a small body near a major body.

    Results are cached in data/close_approach_cache.json under 'close_approach:DES:BODY'.
    Cache is used unless force_refresh=True.

    Parameters:
        designation (str): Small body designation (e.g. '99942' for Apophis,
                           '2004 MN4', 'C/2023 A3')
        body (str):        Major body name: 'Earth', 'Moon', 'Mars', 'Jupiter',
                           'Saturn', 'Uranus', 'Neptune', 'Venus', 'Mercury',
                           'Pluto', or 'ALL'
        date_min (str):    Start date 'YYYY-MM-DD' (optional)
        date_max (str):    End date 'YYYY-MM-DD' (optional)
        dist_max (str):    Max distance in AU as string (default '0.5')
        force_refresh (bool): If True, bypass cache and re-fetch from JPL

    Returns:
        list[dict]: List of approach dicts, each containing:
            jd          - Julian Date of closest approach (TDB)
            date        - Calendar date string e.g. '2029-Apr-13 21:46'
            dist_au     - Nominal center-to-center distance (AU)
            dist_km     - Nominal center-to-center distance (km)
            dist_min_au - 3-sigma minimum distance (AU), may be None
            dist_max_au - 3-sigma maximum distance (AU), may be None
            surface_km  - Distance from surface (km), None if radius unknown
            v_rel_kms   - Relative velocity at closest approach (km/s)
            v_inf_kms   - Asymptotic velocity (km/s), None if not returned
            h_mag       - Absolute magnitude H, may be None
            orbit_id    - JPL orbit solution ID
        Returns [] if no approaches found, None if fetch failed.
    """
    key = _cache_key(designation, body)

    if not force_refresh:
        cache = _load_cache()
        if key in cache:
            entry = cache[key]
            print(f"[CAD] Cache hit: {key} ({len(entry.get('approaches', []))} approach(es))",
                  flush=True)
            return entry.get('approaches', [])

    # Not in cache (or forced refresh) -- fetch from API
    approaches = _fetch_from_api(designation, body, date_min, date_max, dist_max)
    if approaches is None:
        print(f"[CAD] Fetch failed for {designation} near {body}", flush=True)
        return None

    # Cache the result
    cache = _load_cache()
    cache[key] = {
        'designation':  designation,
        'body':         _BODY_CANONICAL.get(CAD_BODY_NAMES.get(body, body), body),
        'approaches':   approaches,
        'date_min':     date_min,
        'date_max':     date_max,
        'dist_max':     dist_max,
        'fetched':      datetime.now().strftime('%Y-%m-%d'),
    }
    _save_cache(cache)

    return approaches


def get_closest_approach(designation, body='Earth', date_min=None, date_max=None,
                          dist_max='0.5', force_refresh=False):
    """
    Return the single closest approach event (minimum dist_au) within the
    specified date range, or None if none found.

    Parameters: same as get_close_approaches().

    Returns:
        dict | None: Single approach dict (see get_close_approaches) for the
                     closest approach, or None.
    """
    approaches = get_close_approaches(designation, body, date_min, date_max,
                                       dist_max, force_refresh)
    if not approaches:
        return None
    # Sort by nominal distance, return minimum
    return min(approaches, key=lambda a: a['dist_au'])


def get_approach_within_date_range(designation, body, start_date, end_date,
                                    force_refresh=False):
    """
    Check if a cached close approach falls within a plotted date range.

    Intended for use by perigee marker logic: given the plotted start/end dates,
    return any cached close approach that falls within that window.

    Parameters:
        designation (str): Small body designation
        body (str):        Major body name
        start_date:        datetime or date object (start of plotted range)
        end_date:          datetime or date object (end of plotted range)
        force_refresh (bool): Bypass cache

    Returns:
        list[dict]: Approaches whose JD falls within [start_date, end_date].
                    Empty list if none found.
    """
    from astropy.time import Time

    # Convert start/end to JD for comparison
    try:
        if isinstance(start_date, datetime):
            jd_start = Time(start_date).jd
        else:
            jd_start = Time(str(start_date)).jd

        if isinstance(end_date, datetime):
            jd_end = Time(end_date).jd
        else:
            jd_end = Time(str(end_date)).jd
    except Exception as e:
        print(f"[CAD] Date conversion error: {e}", flush=True)
        return []

    # Use wide date range for fetch (cache will cover it)
    date_min_str = start_date.strftime('%Y-%m-%d') if hasattr(start_date, 'strftime') else str(start_date)[:10]
    date_max_str = end_date.strftime('%Y-%m-%d') if hasattr(end_date, 'strftime') else str(end_date)[:10]

    approaches = get_close_approaches(designation, body,
                                       date_min=date_min_str, date_max=date_max_str,
                                       force_refresh=force_refresh)
    if not approaches:
        return []

    return [a for a in approaches if jd_start <= a['jd'] <= jd_end]


def format_approach_hover(approach, body='Earth', obj_name='Object'):
    """
    Build Plotly-compatible HTML hover text for a close approach marker.

    Parameters:
        approach (dict): Single approach dict from get_close_approaches()
        body (str):      Major body name (for terminology)
        obj_name (str):  Display name of the small body

    Returns:
        str: HTML hover text string
    """
    from apsidal_markers import get_apsidal_terms

    near_term, _ = get_apsidal_terms(body)

    date_str  = approach.get('date', 'Unknown')
    dist_au   = approach.get('dist_au', 0)
    dist_km   = approach.get('dist_km', 0)
    surf_km   = approach.get('surface_km')
    v_rel     = approach.get('v_rel_kms')
    dist_min  = approach.get('dist_min_au')
    dist_max  = approach.get('dist_max_au')
    orbit_id  = approach.get('orbit_id', 'N/A')

    lines = [
        f"<b>{obj_name} {near_term} (JPL CAD)</b>",
        f"Date: {date_str}",
        f"Distance (center-to-center): {dist_au:.9f} AU",
        f"Distance (center-to-center): {dist_km:,.1f} km",
    ]

    if surf_km is not None:
        lines.append(f"Distance (from surface): {surf_km:,.1f} km")

    if v_rel is not None:
        lines.append(f"Relative velocity: {v_rel:.3f} km/s")

    if dist_min is not None and dist_max is not None:
        unc_km = (dist_max - dist_min) * AU_TO_KM / 2.0
        lines.append(f"3-sigma uncertainty: +/- {unc_km:.1f} km")

    lines += [
        f"JPL orbit solution: {orbit_id}",
        "",
        "<i>Note: Marker position from JPL Horizons at perigee time.</i>",
        "<i>May not sit exactly on plotted trajectory</i>",
        "<i>(trajectory time resolution is coarser than perigee precision).</i>",
        "<i>Source: JPL Small Body Close Approach Data (CAD) API</i>",
    ]

    return "<br>".join(lines)


def add_cad_perigee_marker(fig, approach, position, body, obj_name, color_map,
                            label_suffix=''):
    """
    Add a CAD-sourced perigee marker to a Plotly 3D figure.

    White square-open, same visual language as other apsidal markers.
    The white color distinguishes it from Keplerian markers (which use
    the object's color) while keeping it consistent with "reference data."

    Parameters:
        fig:          Plotly Figure object
        approach:     Single approach dict from get_close_approaches()
        position:     dict with 'x', 'y', 'z' keys (AU) -- from Horizons at perigee time
        body (str):   Central body name (for terminology and hover text)
        obj_name:     Display name of the small body
        color_map:    Color lookup function (kept for API compatibility)
        label_suffix: Optional suffix for the trace name

    Returns:
        None (modifies fig in place)
    """
    import plotly.graph_objects as go
    from apsidal_markers import get_apsidal_terms

    near_term, _ = get_apsidal_terms(body)

    hover = format_approach_hover(approach, body, obj_name)
    trace_name = f"{obj_name} {near_term} (JPL CAD){label_suffix}"

    fig.add_trace(
        go.Scatter3d(
            x=[position['x']],
            y=[position['y']],
            z=[position['z']],
            mode='markers',
            marker=dict(
                size=8,
                color='white',
                symbol='square-open',     # Consistent with other apsidal markers
                line=dict(color='white', width=2),
            ),
            name=trace_name,
            text=[hover],
            customdata=[trace_name],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True,
        )
    )
    print(f"[CAD] Added perigee marker for {obj_name} ({near_term})", flush=True)


# ---------------------------------------------------------------------------
# Convenience: fetch Horizons position at approach epoch
# ---------------------------------------------------------------------------

def fetch_position_at_approach(approach, designation, center_body_id='399',
                                id_type='smallbody'):
    """
    Fetch the geocentric (or other center) position of a small body at the
    close approach epoch from JPL Horizons.

    Parameters:
        approach (dict):       Approach dict from get_close_approaches()
        designation (str):     Small body designation
        center_body_id (str):  Horizons center ID e.g. '399' for Earth
        id_type (str):         'smallbody' or 'majorbody'

    Returns:
        dict | None: {'x', 'y', 'z'} in AU at approach epoch, or None.
    """
    from astroquery.jplhorizons import Horizons
    from astropy.time import Time

    jd = approach.get('jd')
    if jd is None:
        print("[CAD] No JD in approach dict -- cannot fetch position", flush=True)
        return None

    # Add '@' prefix if not present
    location = center_body_id if center_body_id.startswith('@') else f'@{center_body_id}'

    print(f"[CAD] Fetching Horizons position for {designation} at JD {jd:.6f} "
          f"(center: {location})", flush=True)

    try:
        obj = Horizons(id=designation, id_type=id_type,
                       location=location, epochs=jd)
        vec = obj.vectors()
        if len(vec) == 0:
            print("[CAD] No vectors returned from Horizons", flush=True)
            return None

        row = vec[0]
        x = float(row['x'])
        y = float(row['y'])
        z = float(row['z'])
        print(f"[CAD] Position: x={x:.8f}, y={y:.8f}, z={z:.8f} AU", flush=True)
        return {'x': x, 'y': y, 'z': z}

    except Exception as e:
        print(f"[CAD] Horizons position fetch failed: {e}", flush=True)
        return None


# ---------------------------------------------------------------------------
# Diagnostic / standalone test
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print("=" * 60)
    print("close_approach_data.py -- standalone test")
    print("Querying Apophis (99942) close approaches near Earth (2029)")
    print("=" * 60)

    approaches = get_close_approaches(
        designation='99942',
        body='Earth',
        date_min='2029-01-01',
        date_max='2030-01-01',
        dist_max='0.5',
        force_refresh=True
    )

    if approaches:
        for a in approaches:
            print(f"\n  Date:      {a['date']}")
            print(f"  JD:        {a['jd']:.6f}")
            print(f"  Dist:      {a['dist_au']:.9f} AU  |  {a['dist_km']:,.1f} km")
            if a['surface_km'] is not None:
                print(f"  Surface:   {a['surface_km']:,.1f} km")
            if a['v_rel_kms'] is not None:
                print(f"  V_rel:     {a['v_rel_kms']:.3f} km/s")
            if a['dist_min_au'] and a['dist_max_au']:
                unc = (a['dist_max_au'] - a['dist_min_au']) * AU_TO_KM / 2
                print(f"  3-sigma:   +/- {unc:.1f} km")
            print(f"  Orbit ID:  {a['orbit_id']}")
    else:
        print("No approaches returned.")

    print("\n[OK] Test complete.")
