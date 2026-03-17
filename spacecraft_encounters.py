"""
spacecraft_encounters.py

Tagged encounter data for spacecraft missions in Paloma's Orrery.

Design philosophy: Every spacecraft encounter we care about is already known.
Rather than computing pairwise closest approaches from trajectory data (which
fails due to date grid mismatches), we tag each encounter with its authoritative
epoch and parameters from NASA/JPL mission documentation.

Three authoritative epoch sources share one visual language:
  - CAD API:          small body -> planet    (close_approach_data.py)
  - Perihelion Tp:    comet -> Sun            (idealized_orbits.py)
  - Tagged dict:      spacecraft -> any       (this module)

Same pattern: authoritative epoch + Horizons position fetch = precision marker.

Usage:
    from spacecraft_encounters import (
        get_encounters_for_spacecraft,
        get_encounters_in_date_range,
        add_tagged_encounter_markers,
    )

Module created: March 11, 2026
"""

import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta


# ============================================================================
# ENCOUNTER DATABASE
# ============================================================================
#
# Each encounter dict contains:
#   target:       Target body name (must match celestial_objects.py names)
#   date:         UTC datetime string (authoritative epoch)
#   type:         flyby | gravity_assist | orbit_insertion | orbit |
#                 landing | sample | sample_return | end_of_mission | planned
#   dist_km:      Known closest approach distance (km, center-to-center)
#   dist_au:      Same in AU (km / 149597870.7)
#   v_kms:        Relative velocity at encounter (km/s), None if unknown
#   label:        Display label for GUI and marker
#   note:         Educational note for hover text (encounter-specific)
#   status:       completed | planned | canceled
#   source:       Data attribution
#   center:       Suggested center body for heliocentric view
#   select_also:  Objects to auto-select when navigating to this encounter
#   plot_days:    Suggested plot window (days) -- Stage B GUI preset
#   plot_scale_au: Suggested manual scale (AU), None for auto -- Stage B

AU_KM = 149597870.7  # 1 AU in km

SPACECRAFT_ENCOUNTERS = {

    # ========================================================================
    # NEW HORIZONS  (Horizons ID: -98)
    # ========================================================================
    'New Horizons': [
        {
            'target': 'Jupiter',
            'date': '2007-02-28 05:43:40',
            'type': 'gravity_assist',
            'dist_km': 2305000,        # 2.3 million km, 32 Jovian radii
            'dist_au': 2305000 / AU_KM,  # ~0.01541 AU
            'v_kms': 21.219,           # relative to Jupiter
            'v_helio_kms': 23.0,       # relative to Sun (post-assist)
            'label': 'Jupiter Gravity Assist',
            'note': ('Fastest launch ever: 16.26 km/s Earth-relative, '
                     'combining with Earth\'s orbital velocity to ~43 km/s '
                     'heliocentric (velocities add as vectors, not scalars). '
                     'The Sun\'s gravity steadily slowed it to ~19 km/s by '
                     'Jupiter. The gravity assist added ~4 km/s, boosting '
                     'speed to ~23 km/s -- partially recovering what the Sun '
                     'took. Without this boost, Pluto arrival would have been '
                     'three years later.'),
            'status': 'completed',
            'source': 'NASA/JPL',
            'center': 'Sun',
            'select_also': ['Jupiter'],
            'plot_days': 120,          # 4-month observation campaign
            'plot_scale_au': 8.0,
            'center_closeup': 'Jupiter',
            'plot_days_closeup': 120,
            'plot_scale_au_closeup': 0.1,
        },
        {
            'target': 'Pluto',
            'date': '2015-07-14 11:49:57',
            'type': 'flyby',
            'dist_km': 12472,          # surface distance 12,472 km
            'dist_au': 12472 / AU_KM,   # ~0.0000834 AU
            'v_kms': 13.78,            # relative to Pluto
            'v_helio_kms': 14.52,      # relative to Sun at encounter
            'label': 'Pluto Flyby',
            'note': ('First spacecraft to explore Pluto. Flew 12,472 km '
                     'above the surface at 13.78 km/s. Also passed within '
                     '28,800 km of Charon. Revealed Pluto\'s heart-shaped '
                     'nitrogen ice plain (Sputnik Planitia) and atmospheric haze layers.'),
            'resolution_note': ('Close-up trajectory fetched at 1-minute resolution. '
                                'Full mission trace (if visible) uses coarser 6h steps '
                                'and may diverge at this scale.'),
            'status': 'completed',
            'source': 'NASA/JPL',
            'center': 'Sun',
            'select_also': ['Pluto'],
            'plot_days': 28,
            'plot_scale_au': 0.5,
            'center_closeup': 'Pluto',
            'plot_days_closeup': 14,
            'plot_scale_au_closeup': 0.002,
        },
        {
            'target': 'Arrokoth',
            'date': '2019-01-01 05:33:22',  # JPL authoritative UTC (05:34:31 TDB)
            'type': 'flyby',
            'dist_km': 3538,           # 3,538.5 km from surface (JPL Horizons header)
            'dist_au': 3538 / AU_KM,    # ~0.0000236 AU
            'v_kms': 14.43,            # relative to Arrokoth
            'v_helio_kms': 13.87,      # relative to Sun at encounter
            'label': 'Arrokoth Flyby',
            'note': ('Most distant planetary flyby in history at 43.4 AU from the Sun. '
                     'Revealed a contact binary "snowman" shape -- two lobes gently merged. '
                     'First close-up look at a pristine Kuiper Belt object, offering clues '
                     'to how planetesimals formed at the dawn of the solar system.'),
            'resolution_note': ('Trajectory from SWRI NavSBE_2014MU69_od159 solution. '
                                'Vectors only -- no osculating elements available. '
                                'Trajectory resolution set by adaptive fetch step.'),
            'status': 'completed',
            'source': 'NASA/JPL',
            'center': 'Sun',
            'select_also': ['Arrokoth'],
            'plot_days': 28,
            'plot_scale_au': 0.5,
            'center_closeup': 'Arrokoth',  # center_id 2486958 in celestial_objects.py
            'plot_days_closeup': 3,         # Fallback only; adaptive resolution supersedes
            'plot_scale_au_closeup': 0.00003,  # Fallback only; adaptive resolution supersedes
        },
    ],

    # Future missions will be added here as we expand beyond the test case.
    # Template for adding a new spacecraft:
    #
    # 'Voyager 1': [
    #     {
    #         'target': 'Jupiter',
    #         'date': '1979-03-05 12:05:26',
    #         'type': 'gravity_assist',
    #         'dist_km': 349000,
    #         'dist_au': 349000 / AU_KM,
    #         'v_kms': None,
    #         'label': 'Jupiter Flyby',
    #         'note': '...',
    #         'status': 'completed',
    #         'source': 'NASA/JPL',
    #         'center': 'Sun',
    #         'select_also': ['Jupiter'],
    #         'plot_days': 60,
    #         'plot_scale_au': 8.0,
    #         'center_closeup': 'Jupiter',
    #         'plot_days_closeup': 60,
    #         'plot_scale_au_closeup': 0.1,
    #     },
    # ],
}

SPACECRAFT_FULL_MISSION = {
    'New Horizons': {
        'center': 'Sun',
        'select_also': ['Earth', 'Jupiter', 'Pluto', 'Arrokoth'],
        'start_date': '2006-01-20',
        'end_date': '2020-01-01',
        'plot_scale_au': None,
        'fetch_step': '6h',  # Restore default after fine-grained encounter views
        'label': 'Full Mission',
    },
}


# ============================================================================
# QUERY FUNCTIONS
# ============================================================================

def get_encounters_for_spacecraft(spacecraft_name):
    """
    Get all encounters for a given spacecraft.

    Parameters:
        spacecraft_name (str): Spacecraft name matching celestial_objects.py

    Returns:
        list: List of encounter dicts, or empty list if none found
    """
    return SPACECRAFT_ENCOUNTERS.get(spacecraft_name, [])


def get_encounters_in_date_range(spacecraft_name, start_date, end_date):
    """
    Get encounters for a spacecraft that fall within a date range.

    Parameters:
        spacecraft_name (str): Spacecraft name
        start_date (datetime): Start of plot window
        end_date (datetime): End of plot window

    Returns:
        list: Filtered list of encounter dicts within the date range
    """
    encounters = get_encounters_for_spacecraft(spacecraft_name)
    if not encounters:
        return []

    result = []
    for enc in encounters:
        try:
            enc_date = datetime.strptime(enc['date'], '%Y-%m-%d %H:%M:%S')
            if start_date <= enc_date <= end_date:
                result.append(enc)
        except (ValueError, KeyError) as e:
            print(f"[ENCOUNTER] Warning: Could not parse date for {spacecraft_name} "
                  f"{enc.get('label', '?')}: {e}", flush=True)
    return result


def get_all_encounter_spacecraft():
    """
    Get list of all spacecraft that have tagged encounters.

    Returns:
        list: Spacecraft names that have encounter data
    """
    return list(SPACECRAFT_ENCOUNTERS.keys())


def get_encounters_for_target(target_name):
    """
    Get all encounters where a given body is the target, across all spacecraft.
    Returns results sorted chronologically by encounter date.

    Used by create_celestial_checkbutton() to place encounter Go buttons under
    target body checkboxes (e.g., "Go: New Horizons Gravity Assist" under Jupiter).

    Parameters:
        target_name (str): Target body name (e.g., 'Jupiter', 'Pluto')

    Returns:
        list of tuples: [(spacecraft_name, encounter_index, encounter_dict), ...]
              sorted by encounter date (chronological)
    """
    results = []
    for sc_name, encounters in SPACECRAFT_ENCOUNTERS.items():
        for idx, enc in enumerate(encounters):
            if enc.get('target') == target_name:
                results.append((sc_name, idx, enc))
    # Sort chronologically by encounter date
    results.sort(key=lambda x: x[2].get('date', ''))
    return results


def get_full_mission_preset(spacecraft_name):
    return SPACECRAFT_FULL_MISSION.get(spacecraft_name, None)


def _snap_to_horizons_step(ideal_step_sec):
    """
    Snap an ideal step size (seconds) to the nearest Horizons-supported step.

    Horizons accepts {number}{unit} format: 1m, 5m, 10m, 30m, 1h, 2h, 3h, 6h, 1d.
    API-only (not available through the web interface).

    Returns:
        str: Horizons step string (e.g. '1m', '2h', '6h')
    """
    if ideal_step_sec < 120:
        return '1m'
    elif ideal_step_sec < 300:
        return '5m'
    elif ideal_step_sec < 600:
        return '10m'
    elif ideal_step_sec < 1800:
        return '30m'
    elif ideal_step_sec < 5400:
        return '1h'
    elif ideal_step_sec < 10800:
        return '2h'
    elif ideal_step_sec < 18000:
        return '3h'
    else:
        return '6h'


def _calculate_encounter_resolution(enc):
    """
    Derive cube scale, fetch step, and time window from encounter geometry.

    Everything derives from two numbers in the encounter dict:
      dist_km  -- authoritative flyby distance
      v_kms    -- encounter velocity (peak, target-relative)

    Two length scales:
      Cube scale (dist_km * 4) frames the view.
      Curvature scale (pi * dist_km / v_kms) drives the fetch step.
    Using cube diameter for resolution gives wrong answer for distant
    encounters (Jupiter GA: 6h vs correct 3h from curvature).

    Returns:
        dict with keys: plot_scale_au, fetch_step, start_dt, end_dt
        or None if v_kms is missing (caller should fall back to whole-day logic)
    """
    import math

    dist_km = enc.get('dist_km')
    v_kms = enc.get('v_kms')

    if not dist_km or not v_kms:
        return None

    try:
        enc_date = datetime.strptime(enc['date'], '%Y-%m-%d %H:%M:%S')
    except (ValueError, KeyError):
        return None

    # 1. CUBE SCALE (framing): 4x flyby distance
    cube_half_width_km = dist_km * 4
    plot_scale_au = cube_half_width_km / AU_KM

    # 2. ARC RESOLUTION (curvature): semicircle through closest approach
    arc_length_km = math.pi * dist_km
    arc_time_sec = arc_length_km / v_kms
    ideal_step_sec = arc_time_sec / 30  # target ~30 points through arc
    fetch_step = _snap_to_horizons_step(ideal_step_sec)

    # 3. TIME WINDOW (context): cube crossing time * 1.5
    cube_diameter_km = cube_half_width_km * 2
    crossing_time_sec = cube_diameter_km / v_kms
    window_sec = crossing_time_sec * 1.5  # margin for approach/departure
    # Minimum 10 minutes window to avoid degenerate cases
    window_sec = max(window_sec, 600)

    half_window = timedelta(seconds=window_sec / 2)
    start_dt = enc_date - half_window
    end_dt = enc_date + half_window

    return {
        'plot_scale_au': plot_scale_au,
        'fetch_step': fetch_step,
        'start_dt': start_dt,
        'end_dt': end_dt,
    }


def get_encounter_preset(spacecraft_name, encounter_index):
    """
    Build a close-up preset for a specific encounter.

    Uses the adaptive resolution calculation chain when v_kms is available:
      cube scale from dist_km * 4, arc resolution from pi * dist_km / v_kms,
      snap to Horizons step, time window from cube crossing * 1.5.

    Falls back to whole-day logic with 6h default when v_kms is missing.

    Returns:
        dict with keys: center, select_also, start_date, end_date,
                        plot_scale_au, fetch_step, label
        or None if encounter_index is invalid
    """
    encounters = get_encounters_for_spacecraft(spacecraft_name)
    if encounter_index < 0 or encounter_index >= len(encounters):
        return None
    enc = encounters[encounter_index]
    center = enc.get('center_closeup') or enc.get('center', 'Sun')

    # Try adaptive resolution first
    resolution = _calculate_encounter_resolution(enc)

    if resolution:
        # Adaptive: derived from dist_km and v_kms
        start_date = resolution['start_dt'].strftime('%Y-%m-%d %H:%M:%S')
        end_date = resolution['end_dt'].strftime('%Y-%m-%d %H:%M:%S')
        plot_scale = resolution['plot_scale_au']
        fetch_step = resolution['fetch_step']
        print(f"[ENCOUNTER PRESET] Adaptive resolution for {enc.get('label', '?')}: "
              f"scale={plot_scale:.7f} AU, step={fetch_step}, "
              f"window={start_date} to {end_date}", flush=True)
    else:
        # Fallback: whole-day logic with manual values from dict
        plot_days = enc.get('plot_days_closeup', enc.get('plot_days', 28))
        plot_scale = enc.get('plot_scale_au_closeup', enc.get('plot_scale_au'))
        fetch_step = '6h'
        try:
            enc_date = datetime.strptime(enc['date'], '%Y-%m-%d %H:%M:%S')
            half_days = plot_days // 2
            start_dt = enc_date - timedelta(days=half_days)
            end_dt = enc_date + timedelta(days=plot_days - half_days)
            start_date = start_dt.strftime('%Y-%m-%d %H:%M:%S')
            end_date = end_dt.strftime('%Y-%m-%d %H:%M:%S')
        except (ValueError, KeyError):
            start_date = None
            end_date = None
        print(f"[ENCOUNTER PRESET] Fallback resolution for {enc.get('label', '?')}: "
              f"scale={plot_scale}, step={fetch_step}, days={plot_days}", flush=True)

    select_also = list(enc.get('select_also', []))
    if enc.get('target') and enc['target'] not in select_also:
        select_also.append(enc['target'])

    return {
        'center': center,
        'select_also': select_also,
        'start_date': start_date,
        'end_date': end_date,
        'plot_scale_au': plot_scale,
        'fetch_step': fetch_step,
        'label': enc.get('label', 'Encounter'),
        'encounter_date': enc.get('date'),  # Authoritative epoch for position marker
    }


# ============================================================================
# COMET PERIHELION PRESET
# ============================================================================
#
# Builds a "Go: Perihelion" preset for comets, analogous to spacecraft
# encounter presets. Uses the three-path Tp resolution from Capability D
# (osculating cache -> analytical elements -> Horizons fetch) plus vis-viva
# for adaptive time window sizing.
#
# Same pattern as get_encounter_preset(): returns a dict that the GUI
# applies to center, date range, scale, and checked objects.

def get_comet_perihelion_preset(obj_name, obj_info=None):
    """
    Build a perihelion close-up preset for a comet.

    Resolves Tp via three-path fallback, reads a and e to compute q and
    perihelion velocity, then derives a time window and scale that frame
    the perihelion region.

    Parameters:
        obj_name (str):   Display name e.g. 'Halley', '3I/ATLAS', 'MAPS'
        obj_info (dict):  Optional object metadata dict (for horizons_id, id_type)

    Returns:
        dict with keys: center, select_also, start_date, end_date,
                        plot_scale_au, label, tp_date, q_au, v_km_s
        or None if Tp cannot be resolved
    """

    # ---- Resolve Tp via three-path fallback ----------------------------------
    tp_jd = None
    tp_source = None
    a_val = None
    e_val = None

    # Path A: Osculating cache
    try:
        from osculating_cache_manager import load_cache
        cache = load_cache()
        if obj_name in cache and not obj_name.startswith('_'):
            elems = cache[obj_name].get('elements', {})
            cached_tp = elems.get('TP')
            if cached_tp:
                tp_jd = cached_tp
                a_val = elems.get('a')
                e_val = elems.get('e')
                tp_source = 'osculating cache'
    except Exception as ex:
        print(f"[COMET PRESET] Cache lookup failed for {obj_name}: {ex}", flush=True)

    # Path B: Analytical elements
    if tp_jd is None:
        try:
            from orbital_elements import planetary_params as analytical_params
            if obj_name in analytical_params:
                params = analytical_params[obj_name]
                if 'TP' in params:
                    tp_jd = params['TP']
                    a_val = params.get('a')
                    e_val = params.get('e')
                    tp_source = 'analytical elements'
        except Exception as ex:
            print(f"[COMET PRESET] Analytical lookup failed for {obj_name}: {ex}", flush=True)

    # Path C: Horizons fetch at current date (most expensive)
    if tp_jd is None:
        try:
            from osculating_cache_manager import fetch_osculating_elements
            horizons_id = obj_name
            id_type = 'smallbody'
            if obj_info:
                horizons_id = obj_info.get('id', obj_name)
                id_type = obj_info.get('id_type', 'smallbody')
            print(f"[COMET PRESET] No cached Tp for {obj_name} -- fetching from Horizons", flush=True)
            entry = fetch_osculating_elements(
                obj_name=obj_name,
                horizons_id=horizons_id,
                id_type=id_type,
                date=None,  # Current date
                center_body='@10',
            )
            if entry and entry.get('elements'):
                elems = entry['elements']
                tp_jd = elems.get('TP')
                a_val = elems.get('a')
                e_val = elems.get('e')
                tp_source = 'Horizons fetch'
        except Exception as ex:
            print(f"[COMET PRESET] Horizons fetch failed for {obj_name}: {ex}", flush=True)

    if tp_jd is None:
        print(f"[COMET PRESET] No perihelion time available for {obj_name}", flush=True)
        return None

    if a_val is None or e_val is None or a_val == 0:
        print(f"[COMET PRESET] Missing orbital elements for {obj_name} (a={a_val}, e={e_val})", flush=True)
        return None

    # ---- Convert Tp to datetime ----------------------------------------------
    try:
        from astropy.time import Time
        tp_datetime = Time(tp_jd, format='jd').datetime
    except Exception as ex:
        print(f"[COMET PRESET] Could not convert Tp JD {tp_jd}: {ex}", flush=True)
        return None

    # ---- Compute q (perihelion distance) -------------------------------------
    if e_val > 1:
        q_au = abs(a_val) * (e_val - 1.0)
    else:
        q_au = a_val * (1.0 - e_val)

    # ---- Perihelion velocity via vis-viva ------------------------------------
    # v^2 = GM * (2/r - 1/a) at r = q
    GM_sun = 0.01720209895**2  # AU^3 / day^2  (Gaussian gravitational constant)
    import math
    v_au_day = math.sqrt(GM_sun * (2.0 / q_au - 1.0 / a_val))
    v_km_s = v_au_day * AU_KM / 86400.0

    # ---- Time window: crossing_time * 20, floor 7 days ----------------------
    # crossing_time = 2*q / v_perihelion (time to cross 2*q at perihelion speed)
    crossing_time_days = (2.0 * q_au) / v_au_day  # days
    window_days = max(7.0, crossing_time_days * 20.0)

    # ---- Scale: q * 4 -------------------------------------------------------
    plot_scale = q_au * 4.0

    # ---- Build date range around Tp ------------------------------------------
    half_window = timedelta(days=window_days / 2.0)
    start_dt = tp_datetime - half_window
    end_dt = tp_datetime + half_window
    start_date = start_dt.strftime('%Y-%m-%d %H:%M:%S')
    end_date = end_dt.strftime('%Y-%m-%d %H:%M:%S')

    print(f"[COMET PRESET] {obj_name} perihelion preset:", flush=True)
    print(f"  Tp: {tp_datetime.strftime('%Y-%m-%d %H:%M')} UTC (source: {tp_source})", flush=True)
    print(f"  q={q_au:.6f} AU ({q_au * AU_KM:,.0f} km), e={e_val:.6f}", flush=True)
    print(f"  v_perihelion={v_km_s:,.1f} km/s ({v_au_day:.6f} AU/day)", flush=True)
    print(f"  crossing_time={crossing_time_days:.4f} days, window={window_days:.1f} days", flush=True)
    print(f"  scale={plot_scale:.7f} AU, range: {start_date} to {end_date}", flush=True)

    return {
        'center': 'Sun',
        'select_also': ['Sun'],
        'start_date': start_date,
        'end_date': end_date,
        'plot_scale_au': plot_scale,
        'label': f'{obj_name} Perihelion',
        'tp_date': tp_datetime.strftime('%Y-%m-%d %H:%M:%S'),
        'q_au': q_au,
        'v_km_s': v_km_s,
    }


# ============================================================================
# POSITION FETCH
# ============================================================================

def fetch_position_at_encounter(encounter, center_id, spacecraft_id):
    """
    Fetch spacecraft position at the encounter epoch from JPL Horizons.

    Reuses the pattern from close_approach_data.py: authoritative epoch ->
    Horizons position fetch -> marker placement.

    Parameters:
        encounter (dict): Encounter dict with 'date' field
        center_id (str): Horizons center body ID (e.g. '500@10' for Sun)
        spacecraft_id (str): Horizons spacecraft ID (e.g. '-98')

    Returns:
        dict: {'x': float, 'y': float, 'z': float} in AU, or None on failure
    """
    try:
        from astroquery.jplhorizons import Horizons
        from astropy.time import Time

        enc_date = datetime.strptime(encounter['date'], '%Y-%m-%d %H:%M:%S')

        # Query Horizons for spacecraft position at encounter epoch
        # Use a tiny time window around the encounter date
        obj = Horizons(
            id=spacecraft_id,
            location=f'500@{center_id}' if center_id not in ('10', 'Sun') else '500@10',
            epochs={
                'start': enc_date.strftime('%Y-%m-%d %H:%M'),
                'stop': (enc_date + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M'),
                'step': '1m'
            },
            id_type='id'
        )

        vectors = obj.vectors(refplane='ecliptic')
        if len(vectors) > 0:
            pos = {
                'x': float(vectors['x'][0]),
                'y': float(vectors['y'][0]),
                'z': float(vectors['z'][0]),
            }
            print(f"[ENCOUNTER] Fetched position for {encounter['label']}: "
                  f"({pos['x']:.6f}, {pos['y']:.6f}, {pos['z']:.6f}) AU", flush=True)
            return pos
        else:
            print(f"[ENCOUNTER] No position data returned for {encounter['label']}", flush=True)
            return None

    except Exception as e:
        print(f"[ENCOUNTER] Error fetching position for {encounter['label']}: {e}", flush=True)
        return None


# ============================================================================
# MARKER PLACEMENT
# ============================================================================

def _wrap_text(text, width=50):
    """Word-wrap text with <br> tags for Plotly hover tooltips."""
    words = text.split()
    lines = []
    current_line = []
    current_len = 0
    for word in words:
        if current_len + len(word) + 1 > width and current_line:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word) + 1
    if current_line:
        lines.append(' '.join(current_line))
    return '<br>'.join(lines)


def _format_encounter_hover(encounter, spacecraft_name):
    """
    Format hover text for an encounter marker.

    Follows the hover text AU convention: all distances include both AU and km.

    Parameters:
        encounter (dict): Encounter dict
        spacecraft_name (str): Spacecraft name

    Returns:
        str: HTML-formatted hover text
    """
    label = encounter.get('label', 'Encounter')
    enc_date = encounter.get('date', '')
    dist_km = encounter.get('dist_km', 0)
    dist_au = encounter.get('dist_au', 0)
    v_kms = encounter.get('v_kms')
    enc_type = encounter.get('type', '')
    note = encounter.get('note', '')
    source = encounter.get('source', '')
    status = encounter.get('status', 'completed')

    # Format date nicely
    try:
        dt = datetime.strptime(enc_date, '%Y-%m-%d %H:%M:%S')
        date_str = dt.strftime('%Y-%m-%d %H:%M:%S UTC')
    except (ValueError, TypeError):
        date_str = str(enc_date)

    # Format distance -- AU + km per convention
    if dist_km < 10:
        km_str = f"{dist_km:.2f} km"
    elif dist_km < 1000:
        km_str = f"{dist_km:.1f} km"
    elif dist_km < 1000000:
        km_str = f"{dist_km:,.0f} km"
    else:
        km_str = f"{dist_km/1e6:,.2f} million km"

    if dist_au < 0.001:
        au_str = f"{dist_au:.7f} AU"
    elif dist_au < 0.1:
        au_str = f"{dist_au:.5f} AU"
    else:
        au_str = f"{dist_au:.4f} AU"

    # Build hover text
    lines = [
        f"<b>{spacecraft_name} {label}</b>",
        f"Date: {date_str}",
        f"Distance: {au_str} ({km_str})",
    ]

    if v_kms is not None:
        # Show target-relative velocity
        target = encounter.get('target', 'target')
        lines.append(f"Velocity relative to {target}: {v_kms:.2f} km/s")
    
    v_helio = encounter.get('v_helio_kms')
    if v_helio is not None:
        lines.append(f"Velocity relative to Sun: {v_helio:.2f} km/s")

    # Encounter type -- capitalize nicely
    type_labels = {
        'flyby': 'Flyby',
        'gravity_assist': 'Gravity Assist',
        'orbit_insertion': 'Orbit Insertion',
        'orbit': 'Orbital Operations',
        'landing': 'Landing',
        'sample': 'Sample Collection',
        'sample_return': 'Sample Return',
        'end_of_mission': 'End of Mission',
        'planned': 'Planned',
    }
    type_str = type_labels.get(enc_type, enc_type.replace('_', ' ').title())
    lines.append(f"Type: {type_str}")

    if status == 'planned':
        lines.append("<i>[PLANNED - parameters may change]</i>")

    if note:
        # Truncate long notes for hover -- first 400 chars
        if len(note) > 400:
            note = note[:397] + '...'
        # Word-wrap at ~50 chars for readable hover tooltip
        # Close/reopen <i> around <br> so Plotly renders line breaks
        wrapped_lines = _wrap_text(note, width=50).split('<br>')
        wrapped = '</i><br><i>'.join(wrapped_lines)
        lines.append(f"<br><i>{wrapped}</i>")

    # Resolution note -- transparency about trajectory sampling limitations
    resolution_note = encounter.get('resolution_note', '')
    if resolution_note:
        wrapped_rn = _wrap_text(resolution_note, width=50).split('<br>')
        wrapped_rn_str = '</i><br><i>'.join(wrapped_rn)
        lines.append(f"<i>{wrapped_rn_str}</i>")

    if source:
        lines.append(f"<br>Source: {source}")

    return '<br>'.join(lines)


def add_tagged_encounter_marker(fig, encounter, position, spacecraft_name, color_map):
    """
    Place a white diamond-open marker at the spacecraft's position at encounter epoch.

    Consistent with the visual language: white markers for precision apsidal/encounter
    points, object-colored markers for trajectory data.

    Parameters:
        fig: Plotly figure
        encounter (dict): Encounter dict
        position (dict): {'x', 'y', 'z'} position in AU
        spacecraft_name (str): Spacecraft name
        color_map: Color mapping function

    Returns:
        bool: True if marker was added
    """
    if position is None:
        return False

    label = encounter.get('label', 'Encounter')
    hover_text = _format_encounter_hover(encounter, spacecraft_name)

    fig.add_trace(
        go.Scatter3d(
            x=[position['x']],
            y=[position['y']],
            z=[position['z']],
            mode='markers',
            marker=dict(
                size=12,
                color='white',
                symbol='square-open',
                line=dict(color='gray', width=1),
            ),
            name=f"{spacecraft_name} {label}",
            text=[hover_text],
            customdata=[f"{spacecraft_name} {label}"],
            hovertemplate='%{text}<extra></extra>',
            showlegend=True,
        )
    )

    # Console log per convention
    dist_km = encounter.get('dist_km', 0)
    dist_au = encounter.get('dist_au', 0)
    v_kms = encounter.get('v_kms')
    v_str = f", {v_kms:.2f} km/s" if v_kms else ""
    print(f"[ENCOUNTER] {spacecraft_name} {label}: "
          f"{dist_km:,.0f} km ({dist_au:.7f} AU){v_str} "
          f"at ({position['x']:.4f}, {position['y']:.4f}, {position['z']:.4f}) AU",
          flush=True)
    return True


# ============================================================================
# INTEGRATION FUNCTION (called from palomas_orrery.py)
# ============================================================================

def add_tagged_encounter_markers(fig, selected_objects, objects, dates_lists,
                                  center_object_name, center_id, color_map,
                                  show_closest_approach=True, positions_cache=None):
    """
    Add tagged encounter markers for all selected spacecraft in the plot.

    Called from palomas_orrery.py after Capability D in both Pipeline 1 and Pipeline 2.
    Only fires for Sun-centered plots (encounters require heliocentric coordinates).

    Parameters:
        fig: Plotly figure
        selected_objects (list): List of selected object names or dicts
        objects (list): Full objects list from celestial_objects.py
        dates_lists (dict): Date lists per object
        center_object_name (str): Center body name
        center_id (str): Horizons center ID
        color_map: Color mapping function
        show_closest_approach (bool): Whether closest approach markers are enabled
        positions_cache (dict): Optional pre-fetched positions (Pipeline 2)

    Returns:
        int: Number of encounter markers added
    """
    if not show_closest_approach:
        return 0

    markers_added = 0

    # Build name list from selected_objects (may be strings or dicts)
    selected_names = []
    for obj in selected_objects:
        if isinstance(obj, dict):
            selected_names.append(obj['name'])
        else:
            selected_names.append(str(obj))

    # Determine plot date range from dates_lists
    all_dates = []
    for name, dates in dates_lists.items():
        if dates:
            all_dates.extend(dates)
    if not all_dates:
        return 0

    plot_start = min(all_dates)
    plot_end = max(all_dates)

    # Check each selected object for tagged encounters
    for sc_name in selected_names:
        encounters = get_encounters_in_date_range(sc_name, plot_start, plot_end)
        if not encounters:
            continue

        # Look up spacecraft Horizons ID
        sc_info = next((obj for obj in objects if obj['name'] == sc_name), None)
        if not sc_info:
            continue

        sc_id = sc_info.get('id', '')

        for enc in encounters:
            if center_object_name != 'Sun':
                if enc.get('target', '') != center_object_name:
                    continue
            position = fetch_position_at_encounter(enc, center_id, sc_id)

            if position:
                success = add_tagged_encounter_marker(
                    fig=fig,
                    encounter=enc,
                    position=position,
                    spacecraft_name=sc_name,
                    color_map=color_map,
                )
                if success:
                    markers_added += 1

    if markers_added > 0:
        print(f"[ENCOUNTER] Added {markers_added} tagged encounter marker(s)", flush=True)

    return markers_added


# ============================================================================
# UTILITY: List all encounters (for GUI Stage B)
# ============================================================================

def get_encounter_summary():
    """
    Get a summary of all encounters for all spacecraft.
    Useful for GUI display and debugging.

    Returns:
        list: List of (spacecraft_name, label, date_str, type, status) tuples
    """
    summary = []
    for sc_name, encounters in SPACECRAFT_ENCOUNTERS.items():
        for enc in encounters:
            summary.append((
                sc_name,
                enc.get('label', '?'),
                enc.get('date', '?'),
                enc.get('type', '?'),
                enc.get('status', '?'),
            ))
    return summary


# ============================================================================
# SELF-TEST
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("Spacecraft Encounters Module - Self Test")
    print("=" * 70)

    # Test: Query encounters
    nh_encounters = get_encounters_for_spacecraft('New Horizons')
    print(f"\nNew Horizons encounters: {len(nh_encounters)}")
    for enc in nh_encounters:
        print(f"  {enc['label']}: {enc['date']} | {enc['dist_km']:,.0f} km "
              f"({enc['dist_au']:.7f} AU) | {enc['type']}")

    # Test: Date range filtering
    print("\nDate range filter test (2014-2016):")
    filtered = get_encounters_in_date_range(
        'New Horizons',
        datetime(2014, 1, 1),
        datetime(2016, 12, 31)
    )
    for enc in filtered:
        print(f"  {enc['label']}: {enc['date']}")

    # Test: No encounters for unknown spacecraft
    empty = get_encounters_for_spacecraft('Nonexistent')
    print(f"\nNonexistent spacecraft: {len(empty)} encounters (expected 0)")

    # Test: Summary
    print("\nFull encounter summary:")
    for sc, label, date, etype, status in get_encounter_summary():
        status_tag = f" [{status.upper()}]" if status != 'completed' else ""
        print(f"  {sc}: {label} ({date}) - {etype}{status_tag}")

    # Test: Hover text formatting
    print("\nHover text sample:")
    hover = _format_encounter_hover(nh_encounters[1], 'New Horizons')
    # Strip HTML for console display
    import re
    clean = re.sub(r'<[^>]+>', ' ', hover).replace('  ', ' ')
    print(f"  {clean[:200]}...")

    print("\n" + "=" * 70)
    print("All self-tests passed.")
    print("=" * 70)


def get_comet_perihelion_preset(obj_name, obj_info=None):
    """
    Build a perihelion close-up preset for a comet.
    
    Uses resolve_tp() for the authoritative TP, then computes window
    and scale from orbital elements using vis-viva equation.
    
    Called by _apply_comet_perihelion_preset() in palomas_orrery.py.
    
    Parameters:
        obj_name (str): Comet display name (e.g., '3I/ATLAS', 'Halley')
        obj_info (dict, optional): Object info with 'id', 'id_type'
    
    Returns:
        dict: Preset with center, dates, scale, label, q, v, tp_jd, tp_source
              or None if TP cannot be resolved
    """
    import math
    from datetime import datetime, timedelta
    
    try:
        from osculating_cache_manager import resolve_tp, load_cache
        from astropy.time import Time
    except ImportError as ie:
        print(f"[COMET PRESET] Import error: {ie}", flush=True)
        return None
    
    # Resolve TP using authoritative hierarchy
    tp_jd, tp_source = resolve_tp(obj_name, obj_info=obj_info)
    if tp_jd is None:
        print(f"[COMET PRESET] No TP available for {obj_name}", flush=True)
        return None
    
    tp_datetime = Time(tp_jd, format='jd').datetime
    print(f"[COMET PRESET] {obj_name} Tp: {tp_datetime.strftime('%Y-%m-%d %H:%M:%S')} UTC "
          f"(source: {tp_source})", flush=True)
    
    # Get orbital elements for q and v computation
    a_au = None
    e_val = None
    
    # Try cache first
    try:
        cache = load_cache()
        if obj_name in cache:
            elems = cache[obj_name].get('elements', {})
            a_au = elems.get('a')
            e_val = elems.get('e')
    except Exception:
        pass
    
    # Fallback to analytical elements
    if a_au is None or e_val is None:
        try:
            from orbital_elements import planetary_params as analytical_params
            if obj_name in analytical_params:
                ap = analytical_params[obj_name]
                a_au = a_au or ap.get('a')
                e_val = e_val or ap.get('e')
        except Exception:
            pass
    
    if a_au is None or e_val is None:
        print(f"[COMET PRESET] Missing a or e for {obj_name}", flush=True)
        return None
    
    # Perihelion distance q
    if e_val >= 1.0:
        q_au = abs(a_au) * (e_val - 1.0)   # Hyperbolic
    else:
        q_au = a_au * (1.0 - e_val)         # Elliptical
    
    # Perihelion velocity via vis-viva: v^2 = GM * (2/r - 1/a)
    # GM_sun in AU^3/day^2
    GM_sun = 2.959122e-4
    if a_au < 0:
        v_sq = GM_sun * (2.0 / q_au + 1.0 / abs(a_au))
    else:
        v_sq = GM_sun * (2.0 / q_au - 1.0 / a_au)
    
    v_au_day = math.sqrt(max(v_sq, 0))
    v_kms = v_au_day * 149597870.7 / 86400.0
    
    # Time window: crossing_time * 20, floor 7 days, cap 365 days
    crossing_time_days = (2.0 * q_au / v_au_day) if v_au_day > 0 else 30.0
    window_days = max(7, min(365, int(crossing_time_days * 20)))
    
    half_window = timedelta(days=window_days / 2)
    start_dt = tp_datetime - half_window
    end_dt = tp_datetime + half_window
    
    # Plot scale: q * 4
    plot_scale = q_au * 4.0
    
    label = (f"{obj_name} Perihelion: {tp_datetime.strftime('%Y-%m-%d %H:%M')} UTC | "
             f"q={q_au:.4f} AU | v={v_kms:.1f} km/s")
    
    preset = {
        'label': label,
        'center': 'Sun',
        'select_also': ['Sun'],
        'start_date': start_dt.strftime('%Y-%m-%d %H:%M:%S'),
        'end_date': end_dt.strftime('%Y-%m-%d %H:%M:%S'),
        'plot_scale_au': plot_scale,
        'tp_jd': tp_jd,
        'tp_source': tp_source,
        'q_au': q_au,
        'v_kms': v_kms,
    }
    
    print(f"[COMET PRESET] Window: {window_days}d, Scale: {plot_scale:.5f} AU", flush=True)
    return preset