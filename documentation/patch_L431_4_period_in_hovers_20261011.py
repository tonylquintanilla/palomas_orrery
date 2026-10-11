"""patch_L431_4_period_in_hovers_20261011.py -- L-431 (orbital periods from
JPL), build 1 of 3: the period in the orrery's hovers.

Built on orrery 41e9a1d569098d35f327870ca30050cb83645924 at
https://github.com/tonylquintanilla/palomas_orrery ("Update
WHERE_WE_ARE_10-11-26_1311_run_record.md"). The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 11, 2026 with Anthropic's Claude Opus 5.5, from
documentation/DESIGN_L431_orbital_periods_rulings_20261011.md, sections
2 to 5.

HOW TO RUN
    The patch sits in the orrery repo's ROOT folder (the folder that
    holds LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run. Or,
    from a terminal in that folder:
        python patch_L431_4_period_in_hovers_20261011.py
    Success prints one "ok" line per edit, then "patch applied". It then
    asks JPL, live, for four bodies' periods and prints what came back
    (it writes nothing for that). Then run
    patch_L431_5_records_20261011.py.

WHAT IT CHANGES
    orbital_period.py -- NEW. Fetches a body's period (Horizons' PR) at
        the plot date and a year later, around the Sun and around the
        solar system's barycentre, keeps the centre whose period moved
        less, reads JPL's stated uncertainty from the Small-Body Database
        where the body has one, and prints the period by the larger of
        the two errors. Also the fallback order for showing a period.
    osculating_cache_manager.py -- a fetch you accept in the "Update
        Orbital Elements?" box also saves the period beside the elements,
        under 'period' in data/osculating_cache.json. The elements are
        not changed.
    orbit_data_manager.py -- the elements fetch keeps PR as 'P_days'.
    visualization_utils.py -- the hover's period line.
    orbital_param_viz.py -- the parameters window's Orbital Period row.
    palomas_orrery.py -- the precession note's orbit count and
        fetch_position's period record.
    constants_new.py -- D_PER_JULIAN_YEAR (365.25 days, exact, IAU
        Style Manual); a note above KNOWN_ORBITAL_PERIODS.
    constants_tokens.py -- the d_per_yr token for that row.
    Not changed: the drawn orbits, the perihelion and aphelion markers,
    the gallery (L-431's builds 2 and 3).

PERMANENT, after the script itself is archived: orbital_period.py, the
'period' record in the orbit cache, the new row and token.

SAFETY
    Each file is checked only at the lines this patch edits: every
    anchor must match exactly once. If any check fails, NOTHING is
    written. A file found with Windows line endings is matched after
    turning them into LF and written back LF, and the patch says so.
    Undo after a run is Discard Changes in GitHub Desktop, and delete
    orbital_period.py.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EDITS = [
    ('constants_new.py', 'stamp',
     'drawn from, its two cell sizes, and the drawn orbits\' eccentricity.)\n"""\n',
     'drawn from, its two cell sizes, and the drawn orbits\' eccentricity.)\nModule updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5\n(L-431, orbital periods from JPL, build 1: D_PER_JULIAN_YEAR, an exact\nconversion read from the IAU Style Manual, so the period\'s years and its\none-year test step go through a row; a note above KNOWN_ORBITAL_PERIODS\nsays it is now the last fallback for showing a period. No value changes.)\n"""\n'),
    ('constants_new.py', 'row D_PER_JULIAN_YEAR',
     "# Note+: unit is asserted here, as DEG_PER_RAD's is.\n\nEARTH_SIDEREAL_ROTATION_PERIOD_H",
     '# Note+: unit is asserted here, as DEG_PER_RAD\'s is.\n\nD_PER_JULIAN_YEAR = 365.25\n# Unit: d_per_yr\n# Status: declared 2026-10-11 -- an exact unit conversion, days in one\n# Status+: Julian year. Belongs to no body\'s slice.\n# Figures: exact -- a definition, not a measurement.\n# Read: Table 5 and sec. 5.15, IAU Style Manual, "SI Units" page,\n# Read+: 2026-10-11, Claude Opus 5.5, through the chat\'s web-fetch tool\n# Source: IAU Style Manual, SI Units, Table 5 (non-SI units recognised for\n# Source+: use in astronomy) -- year (Julian), a, 31.5576 Ms = 365.25 d;\n# Source+: sec. 5.15 regards a year as a Julian year of 365.25 days.\n# Ref: https://www.iau.org/publications/proceedings_rules/units/\n# Note: L-431. The orbital period\'s years convert through this row, and\n# Note+: the period\'s one-year test steps by it (orbital_period.py), so\n# Note+: neither divides by a bare 365.25. The older bare 365.25s in other\n# Note+: modules are one class on L-431, not chased.\n\nEARTH_SIDEREAL_ROTATION_PERIOD_H'),
    ('constants_new.py', 'note above KNOWN_ORBITAL_PERIODS',
     '\n\nKNOWN_ORBITAL_PERIODS = {\n    # Planets (converted from years to days)\n',
     "\n\n# L-431 (2026-10-11): the LAST fallback for showing a period. A period\n# fetched with a body's elements and saved in data/osculating_cache.json\n# comes first (orbital_period.py), and a hover that reaches this table\n# says the value is typed. Its rows carry no source line: one class on\n# L-431, not chased. The drawn orbits and the markers still read it until\n# L-431's second build.\nKNOWN_ORBITAL_PERIODS = {\n    # Planets (converted from years to days)\n"),
    ('constants_tokens.py', 'stamp',
     'cloud drawn as dots along orbits following Nesvorny et al. (2025).)\n"""\n',
     'cloud drawn as dots along orbits following Nesvorny et al. (2025).)\nModule updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5\n(L-431: d_per_yr, for D_PER_JULIAN_YEAR, the exact conversion an\norbital period\'s years go through.)\n"""\n'),
    ('constants_tokens.py', 'token d_per_yr',
     '        "meaning": "seconds per hour, an exact unit conversion",\n    },\n',
     '        "meaning": "seconds per hour, an exact unit conversion",\n    },\n    # L-431 (2026-10-11): days per Julian year, the conversion an orbital\n    # period\'s years go through.\n    "d_per_yr": {\n        "dimension": "d / yr",\n        "defining_constant": None,\n        "meaning": "days per Julian year, an exact unit conversion",\n    },\n'),
    ('orbit_data_manager.py', 'stamp',
     'using an incremental approach to minimize API calls and processing time.\n\nRole: cache\n',
     "using an incremental approach to minimize API calls and processing time.\n\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-431:\nquery_horizons_elements keeps Horizons' PR, the sidereal orbit period, in\ndays, as 'P_days' in its result; an open orbit's placeholder is kept as\nnothing. The elements it returns are unchanged.)\n\nRole: cache\n"),
    ('orbit_data_manager.py', 'keep PR (read)',
     "        try:\n            ta_val = get_col(['TA', 'nu', 'trueAnomaly'])\n        except KeyError:\n            ta_val = None\n",
     "        try:\n            ta_val = get_col(['TA', 'nu', 'trueAnomaly'])\n        except KeyError:\n            ta_val = None\n\n        # L-431: keep Horizons' PR, the sidereal orbit period. astroquery's\n        # elements() asks for AU-D units and names PR 'P', in days. Horizons\n        # prints 9.999E+99 for an open orbit; that is kept as None.\n        try:\n            from orbital_period import OPEN_ORBIT_PLACEHOLDER_FLOOR\n            p_val = float(row['P']) if 'P' in row.colnames else None\n            if p_val is not None and not (abs(p_val) < OPEN_ORBIT_PLACEHOLDER_FLOOR):\n                p_val = None\n        except Exception:\n            p_val = None\n"),
    ('orbit_data_manager.py', 'keep PR (return)',
     "        if q_val is not None:\n            result['q'] = q_val\n        \n        return result\n",
     "        if q_val is not None:\n            result['q'] = q_val\n        if p_val is not None:\n            result['P_days'] = p_val  # L-431: Horizons' PR, days\n        \n        return result\n"),
    ('osculating_cache_manager.py', 'stamp',
     'Created: November 18, 2025\n\nRole: cache\n',
     "Created: November 18, 2025\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-431,\nbuild 1: a fetch made through get_elements_with_prompt also saves the\nbody's orbital period beside its elements, under 'period', with the\ncentre it was taken around, its date and its error (orbital_period.py).\nThe elements are unchanged, so nothing drawn moves.)\n\nRole: cache\n"),
    ('osculating_cache_manager.py', 'fetch: with_period parameter',
     "def fetch_osculating_elements(obj_name, horizons_id=None, id_type='smallbody', date=None, center_body=None):\n",
     "def fetch_osculating_elements(obj_name, horizons_id=None, id_type='smallbody', date=None, center_body=None,\n                              with_period=False):\n"),
    ('osculating_cache_manager.py', 'fetch: docstring',
     "        center_body (str, optional): Override center body (e.g., '@9' for Pluto barycenter)\n                                     If None, auto-detects based on object ID.\n    \n    Returns:\n        dict: Cache entry with elements and metadata, or None if fetch fails\n",
     "        center_body (str, optional): Override center body (e.g., '@9' for Pluto barycenter)\n                                     If None, auto-detects based on object ID.\n        with_period (bool): also fetch the orbital period record (L-431):\n                            two to three more Horizons queries and one\n                            Small-Body Database query. Default False, so\n                            the direct fetches in idealized_orbits.py and\n                            spacecraft_encounters.py cost what they did.\n    \n    Returns:\n        dict: Cache entry with elements and metadata, or None if fetch fails\n"),
    ('osculating_cache_manager.py', 'fetch: period record',
     '        print(f"[OK] Fetched elements (solution date: {cache_entry[\'metadata\'][\'solution_date\']})", flush=True)\n        return cache_entry\n',
     '        # L-431 (orbital periods from JPL), build 1: the period record, kept\n        # beside the elements and read only to SHOW a period. The elements\n        # above are untouched, so nothing drawn moves. A failed period query\n        # keeps the last fetched period, the fallback order\'s second step.\n        if with_period:\n            previous = None\n            try:\n                previous = (load_cache().get(get_cache_key(obj_name, center_body)) or {}).get(\'period\')\n            except Exception:\n                previous = None\n            try:\n                from orbital_period import build_period_record\n                cache_entry[\'period\'] = build_period_record(\n                    query_id, id_type, date_str,\n                    cache_entry[\'metadata\'][\'center_body\'],\n                    previous=previous,\n                    elements_p_days=result.get(\'P_days\'))\n                _rec = cache_entry[\'period\']\n                print(f"[OK] Period for {obj_name}: {_rec[\'days\']} d around {_rec[\'center\']} "\n                      f"(change in a year {_rec[\'year_change_days\']} d; {_rec[\'sbdb_status\']})", flush=True)\n            except Exception as ex:\n                print(f"[WARN] Period not fetched for {obj_name} ({ex})"\n                      f"{\'; keeping the last fetched period\' if previous else \'\'}", flush=True)\n                if previous:\n                    cache_entry[\'period\'] = previous\n\n        print(f"[OK] Fetched elements (solution date: {cache_entry[\'metadata\'][\'solution_date\']})", flush=True)\n        return cache_entry\n'),
    ('osculating_cache_manager.py', 'prompt: ask for the period',
     '            date=plot_date,\n            center_body=center_body\n        )\n\n        if fresh_entry:\n',
     "            date=plot_date,\n            center_body=center_body,\n            with_period=True,   # L-431: the hover's period is saved with the elements\n        )\n\n        if fresh_entry:\n"),
    ('visualization_utils.py', 'stamp',
     '    Phase 2 adds auto_dtick + autorange suppression for close-approach grids.\n\nRole: rendering\n',
     "    Phase 2 adds auto_dtick + autorange suppression for close-approach grids.\nModule updated: October 11, 2026 with Anthropic's Claude Opus 5.5 (L-431,\n    build 1: the hover's orbital period is the one fetched from JPL and\n    saved with the elements, around the centre it is steadiest about, to\n    the digits its errors earn; the typed table only when nothing was\n    fetched, and the hover then says it is typed. orbital_period.py.)\n\nRole: rendering\n"),
    ('visualization_utils.py', 'hover: the period',
     '    # Get known orbital period if available\n    # Context-aware: Pluto uses barycentric period (6.387 days) when centered on Pluto-Charon Barycenter\n    if obj_name == \'Pluto\' and center_object_name == \'Pluto-Charon Barycenter\':\n        # Pluto orbits the barycenter with the same period as Charon (6.387 days)\n        known_value = 6.387  # Binary orbital period, same as Charon\n        known_period = {\n            \'days\': known_value,\n            \'years\': known_value / 365.25\n        }\n    elif obj_name in KNOWN_ORBITAL_PERIODS:\n        known_value = KNOWN_ORBITAL_PERIODS[obj_name]\n        \n        if known_value is None:\n            # Handle hyperbolic/parabolic objects\n            known_period = "N/A (hyperbolic/parabolic orbit)"\n        else:\n            known_period = {\n                \'days\': known_value,\n                \'years\': known_value / 365.25\n            }\n\n    # Format known period\n    if isinstance(known_period, dict):\n        known_years = known_period.get(\'years\')\n        known_days = known_period.get(\'days\')\n        known_period_str = f"{known_years:.4f} Earth years ({known_days:.2f} days)"\n    else:\n        known_period_str = str(known_period)\n',
     "    # The orbital period to show (L-431, build 1). A period fetched from JPL\n    # Horizons and saved with the elements in the orbit cache comes first,\n    # around the centre it is steadiest about, to the digits the larger of\n    # its errors earns; the typed table KNOWN_ORBITAL_PERIODS only when\n    # nothing was fetched, and the hover then says so (orbital_period.py).\n    # Context-aware: Pluto viewed from the Pluto-Charon Barycenter keeps its\n    # old typed value, 6.387 days, as its typed fallback in that view.\n    from orbital_period import resolve_display_period, period_hover_lines\n    _typed_override = None\n    if obj_name == 'Pluto' and center_object_name == 'Pluto-Charon Barycenter':\n        _typed_override = 6.387  # typed: Pluto around the barycenter, as Charon\n    _resolved_period = resolve_display_period(\n        obj_name, center_object_name=center_object_name,\n        parent_name=planet if is_satellite else None,\n        typed_table=KNOWN_ORBITAL_PERIODS, typed_override=_typed_override)\n    known_period_str = period_hover_lines(_resolved_period)\n"),
    ('visualization_utils.py', 'hover: the line',
     '    # Add orbital period information (known period only)\n    full_hover_text += f"Known Orbital Period: {known_period_str}"\n',
     '    # Add orbital period information (L-431: fetched first, typed last and marked)\n    full_hover_text += known_period_str\n'),
    ('orbital_param_viz.py', 'stamp',
     'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6\n"""\nimport numpy as np\n',
     'Module updated: April 2026 with Anthropic\'s Claude Opus 4.6\nModule updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nbuild 1: the window\'s Orbital Period row shows the period fetched from\nJPL, to the digits its errors earn, or the typed value marked as typed.\nThe estimated perihelion and aphelion dates still use the typed period\nuntil L-431\'s second build.)\n"""\nimport numpy as np\n'),
    ('orbital_param_viz.py', 'import',
     'from constants_new import KNOWN_ORBITAL_PERIODS, color_map\n',
     'from constants_new import KNOWN_ORBITAL_PERIODS, color_map\nfrom orbital_period import resolve_display_period, period_panel_text  # L-431\n'),
    ('orbital_param_viz.py', 'panel: unit column',
     "        ('period', 'Orbital Period:', 'days')\n",
     "        ('period', 'Orbital Period:', '')   # L-431: the text carries its units\n"),
    ('orbital_param_viz.py', 'panel: Earth at open',
     '        params = planetary_params["Earth"]\n        for key, label in param_labels.items():\n            if key in params:\n',
     '        params = planetary_params["Earth"]\n        for key, label in param_labels.items():\n            if key == \'period\':\n                # L-431: the period fetched from JPL, else typed and marked\n                label.config(text=period_panel_text(resolve_display_period(\n                    "Earth", typed_table=KNOWN_ORBITAL_PERIODS)))\n                continue\n            if key in params:\n'),
    ('orbital_param_viz.py', 'panel: the chosen body',
     '                params = planetary_params[selected_obj]\n                for key, label in param_labels.items():\n                    if key in params:\n',
     "                params = planetary_params[selected_obj]\n                for key, label in param_labels.items():\n                    if key == 'period':\n                        # L-431: the period fetched from JPL, else typed and marked\n                        label.config(text=period_panel_text(resolve_display_period(\n                            selected_obj, typed_table=KNOWN_ORBITAL_PERIODS)))\n                        continue\n                    if key in params:\n"),
    ('palomas_orrery.py', 'stamp',
     'of first apparition, Tony 2026-10-10.)\n\n"""\n#Paloma\'s Orrery',
     'of first apparition, Tony 2026-10-10.)\nModule updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nbuild 1: the precession note\'s orbit count and fetch_position\'s period\nrecord read the period fetched from JPL first and the typed table last,\nthrough orbital_period.py. Nothing drawn changes.)\n\n"""\n#Paloma\'s Orrery'),
    ('palomas_orrery.py', 'precession note: the period',
     '            orbital_period_days = KNOWN_ORBITAL_PERIODS.get(obj_name, 1.0)\n',
     "            # L-431: the period fetched from JPL first, the typed table last\n            from orbital_period import resolve_display_period\n            orbital_period_days = resolve_display_period(\n                obj_name, center_object_name=center_object_name,\n                typed_table=KNOWN_ORBITAL_PERIODS)['days'] or 1.0\n"),
    ('palomas_orrery.py', 'fetch_position: the period',
     '        # Get the known orbital period if available\n        if obj_name in KNOWN_ORBITAL_PERIODS:\n            known_value = KNOWN_ORBITAL_PERIODS[obj_name]\n',
     "        # The orbital period (L-431): the period fetched from JPL and saved\n        # with the elements first, the typed table only when none was.\n        from orbital_period import resolve_display_period\n        _period = (resolve_display_period(obj_name, typed_table=KNOWN_ORBITAL_PERIODS)\n                   if obj_name else {'kind': 'none'})\n        if _period['kind'] != 'none':\n            known_value = _period['days']\n"),
]

NEW_MODULE = '"""\norbital_period.py - A body\'s orbital period from JPL, printed to the digits its errors earn.\n\nFetches each body\'s sidereal orbital period (Horizons\' PR) with its\nosculating elements, picks the centre it is steadiest around (the Sun or\nthe solar system\'s barycentre, its centre of mass), measures how much it\nmoves in a year, reads JPL\'s stated uncertainty of the orbit fit (the\nSmall-Body Database\'s sigma) where the body has one, and prints the\nperiod by the larger of those two errors. Ledger L-431, build 1 of 3;\nrulings in documentation/DESIGN_L431_orbital_periods_rulings_20261011.md.\n\nThe fallback order for SHOWING a period (Tony\'s ruling 5):\n    1. a fresh fetch, saved in the orbit cache (data/osculating_cache.json)\n       under the entry\'s \'period\' key, with its centre, date and error;\n    2. the last fetched period saved there, which is the same record\n       carried forward when a later fetch could not get one;\n    3. the typed table KNOWN_ORBITAL_PERIODS (constants_new.py), printed\n       as typed with the note "typed value, not fetched from JPL".\nThe cache\'s \'elements\' are not changed by any of this, so the drawn\nellipse and the perihelion and aphelion markers do not move (build 2).\n\nKey functions:\n    build_period_record() - Horizons + SBDB queries -> the cache\'s period record\n    resolve_display_period() - the fallback order, for one body and one view\n    period_hover_lines() - the hover\'s period lines, <br>-joined\n    period_panel_text() - one short line for the orbital parameters window\n    report_exponent() - the Report test\'s place for an error\n\nConsumed by: osculating_cache_manager.fetch_osculating_elements (writes),\nvisualization_utils.format_detailed_hover_text, orbital_param_viz.py and\npalomas_orrery.py (read).\n\nRole: computation\nDomain: orrery\n\nModule updated: October 11, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nnew module).\n"""\n\nimport math\nimport os\nimport re\nfrom datetime import datetime\n\nfrom constants_new import D_PER_JULIAN_YEAR\n\n# Horizons prints PR as 9.999E+99 for an open orbit (read 2026-10-11 on\n# C/2025 N1 through the chat\'s web-fetch tool). Anything this large is\n# that placeholder, not a period.\nOPEN_ORBIT_PLACEHOLDER_FLOOR = 1e90\n\n# The two centres of the two-centre test (ruling 2), in Horizons\' location\n# form, as orbit_data_manager.query_horizons_elements passes them.\nCENTRE_SUN = \'@sun\'\nCENTRE_BARYCENTRE = \'@0\'\nHELIOCENTRIC_FORMS = (\'@sun\', \'@10\', \'sun\', \'10\')\n\nSBDB_API_URL = \'https://ssd-api.jpl.nasa.gov/sbdb.api\'\n\n# The view centres that make palomas_orrery.py fetch an object\'s elements\n# around another centre. A COPY of the block that sets\n# osculating_center_body in palomas_orrery.py (search for\n# "osculating_center_body = \'@9\'"). Build 2 edits that path and folds this\n# copy into one home there (L-431). The pre-test checks the two agree.\nVIEW_TO_OSCULATING_CENTRE = {\n    \'Pluto-Charon Barycenter\': \'@9\',\n    \'Pluto\': \'@999\',\n    \'Orcus-Vanth Barycenter\': \'@20090482\',\n    \'Orcus\': \'@920090482\',\n    \'Patroclus-Menoetius Barycenter\': \'@20000617\',\n    \'Earth-Moon Barycenter\': \'@3\',\n    \'Earth\': \'@399\',\n}\n\n# What the hover calls each centre. Words, not values.\nCENTRE_LABELS = {\n    \'sun\': \'the Sun\',\n    \'10\': \'the Sun\',\n    \'0\': "the solar system\'s center of mass",\n    \'ssb\': "the solar system\'s center of mass",\n    \'3\': \'the Earth-Moon center of mass\',\n    \'9\': \'the Pluto-Charon center of mass\',\n    \'20090482\': \'the Orcus-Vanth center of mass\',\n    \'20000617\': \'the Patroclus-Menoetius center of mass\',\n    \'20136199\': \'the Eris-Dysnomia center of mass\',\n    \'20136108\': "the Haumea system\'s center of mass",\n    \'20136472\': "the Makemake system\'s center of mass",\n    \'20225088\': "the Gonggong system\'s center of mass",\n    \'920050000\': \'Quaoar\',\n    \'920090482\': \'Orcus\',\n    \'199\': \'Mercury\', \'299\': \'Venus\', \'399\': \'Earth\', \'499\': \'Mars\',\n    \'599\': \'Jupiter\', \'699\': \'Saturn\', \'799\': \'Uranus\', \'899\': \'Neptune\',\n    \'999\': \'Pluto\',\n}\n\n\ndef centre_label(location, parent_name=None):\n    """The hover\'s words for a Horizons centre such as \'@sun\' or \'@599\'."""\n    key = str(location or \'\').lstrip(\'@\').lower()\n    if key in CENTRE_LABELS:\n        return CENTRE_LABELS[key]\n    if parent_name:\n        return parent_name\n    return \'Horizons center %s\' % key\n\n\ndef _is_heliocentric(location):\n    return str(location or \'\').lower() in HELIOCENTRIC_FORMS\n\n\n# ============================================================================\n# THE DIGITS RULE (ruling 3; provenance-discipline, The ceiling, Report)\n# ============================================================================\n\ndef report_exponent(err):\n    """\n    The Report test\'s place for an error: the power of ten p whose implied\n    half-width, half of 10**p, is closest to err on a log scale; a tie goes\n    to the coarser place. Returns p (0 = whole units, -2 = hundredths).\n    """\n    x = math.log10(2.0 * err)\n    return int(math.floor(x + 0.5))\n\n\ndef format_by_error(value, err):\n    """\n    value printed to the place its error earns, never fewer than one\n    figure. Thousands separators from 10,000 up, as the rulings record\'s\n    section 5 table prints them.\n    """\n    if value is None:\n        return None\n    if err is None or not (err > 0):\n        # No error to round by: keep ten figures and let the caller say so.\n        err = abs(value) * 1e-10 if value else 1e-10\n    p = report_exponent(err)\n    if value != 0:\n        top = int(math.floor(math.log10(abs(value))))\n        if p > top:\n            p = top                  # never fewer than one figure\n    if p >= 0:\n        unit = 10 ** p\n        r = int(round(value / unit)) * unit\n        return (\'{:,}\'.format(r) if abs(r) >= 10000 else str(r))\n    places = -p\n    s = \'%.*f\' % (places, value)\n    if abs(value) >= 10000:\n        whole, _, frac = s.partition(\'.\')\n        s = \'{:,}\'.format(int(whole)) + (\'.\' + frac if frac else \'\')\n    return s\n\n\n# ============================================================================\n# FETCHING (Horizons and the Small-Body Database)\n# ============================================================================\n\ndef query_period_pair(horizons_id, id_type, date_str, location):\n    """\n    One Horizons elements query, two epochs: the plot date and a Julian\n    year later (a year earlier if the later date is refused). Returns\n    {\'p1\', \'p2\', \'step_days\', \'e\', \'targetname\'}; a period is None for an\n    open orbit (PR printed as the 9.999E+99 placeholder).\n    astroquery\'s elements() asks for OUT_UNITS AU-D and names PR \'P\', in\n    days (astroquery 0.4.11, jplhorizons/__init__.py, elem_columns).\n    """\n    from astroquery.jplhorizons import Horizons\n    from astropy.time import Time\n\n    jd = Time(date_str).jd\n    last_error = None\n    for step in (D_PER_JULIAN_YEAR, -D_PER_JULIAN_YEAR):\n        try:\n            obj = Horizons(id=horizons_id, id_type=id_type, location=location,\n                           epochs=[jd, jd + step])\n            el = obj.elements()\n            if len(el) < 2:\n                raise ValueError(\'Horizons returned %d rows, not 2\' % len(el))\n            if \'P\' not in el.colnames:\n                raise KeyError(\'no period column P in %s\' % (el.colnames,))\n\n            def _p(row):\n                v = float(row[\'P\'])\n                return None if (not math.isfinite(v) or abs(v) >= OPEN_ORBIT_PLACEHOLDER_FLOOR) else v\n\n            e_val = float(el[0][\'e\']) if \'e\' in el.colnames else None\n            p1, p2 = _p(el[0]), _p(el[1])\n            if e_val is not None and e_val >= 1.0:\n                p1 = p2 = None\n            return {\n                \'p1\': p1, \'p2\': p2, \'step_days\': step, \'e\': e_val,\n                \'targetname\': str(el[0][\'targetname\']) if \'targetname\' in el.colnames else None,\n            }\n        except Exception as ex:          # try the other side of the year\n            last_error = ex\n    raise last_error\n\n\ndef sbdb_search_string(horizons_id, targetname=None):\n    """\n    What to ask the Small-Body Database for. A pinned Horizons record\n    number (9 followed by seven digits) is not something SBDB can find\n    (horizons-orbital-mechanics 1.2, Checking an Entry Against JPL), so\n    for one the name Horizons gave the record is used: \'2P/Encke\' -> \'2P\'.\n    """\n    hid = str(horizons_id).strip()\n    if re.match(r\'^9\\d{7}$\', hid) and targetname:\n        name = targetname.strip()\n        m = re.match(r\'^(\\d+[PI])/\', name)\n        if m:\n            return m.group(1)\n        m = re.search(r\'\\(([^()]+)\\)\\s*$\', name)\n        return m.group(1).strip() if m else name\n    return hid\n\n\ndef fetch_sbdb_period_sigma(search):\n    """\n    JPL\'s stated 1-sigma of the sidereal orbital period, in days, from the\n    Small-Body Database API (orbit.elements, name \'per\'). Returns\n    (sigma_days or None, status words, SBDB\'s full name or None).\n    """\n    import requests\n    try:\n        resp = requests.get(SBDB_API_URL, params={\'sstr\': search, \'full-prec\': \'1\'},\n                            timeout=30)\n        data = resp.json()\n    except Exception as ex:\n        return None, \'SBDB not reached (%s)\' % ex.__class__.__name__, None\n    if \'list\' in data:\n        return None, \'SBDB found several matches for %r\' % search, None\n    if \'orbit\' not in data:\n        return None, \'SBDB has no entry for %r\' % search, None\n    fullname = (data.get(\'object\') or {}).get(\'fullname\')\n    for el in data[\'orbit\'].get(\'elements\', []):\n        if el.get(\'name\') == \'per\':\n            try:\n                return float(el.get(\'sigma\')), \'SBDB sigma\', fullname\n            except (TypeError, ValueError):\n                return None, \'SBDB gives no sigma for the period\', fullname\n    return None, \'SBDB gives no period (open orbit?)\', fullname\n\n\ndef _is_small_body(horizons_id, id_type):\n    if id_type in (\'smallbody\', \'designation\', \'asteroid_name\', \'comet_name\'):\n        return not str(horizons_id).startswith(\'-\')\n    return False\n\n\ndef build_period_record(horizons_id, id_type, date_str, location, previous=None,\n                        elements_p_days=None):\n    """\n    The period record the orbit cache keeps beside an entry\'s elements.\n\n    location is the centre the elements were fetched around. When it is the\n    Sun -- the default for planets, asteroids and comets -- the two-centre\n    test runs (ruling 2): the period around the Sun and around the solar\n    system\'s barycentre, each at the plot date and a year later, and the\n    centre whose period moved less is kept. Its choice is saved, so a later\n    fetch asks only for the chosen centre. A later fetch whose chosen centre\n    moved more than the other centre did when the choice was made runs the\n    test again. Moons and the Pluto system keep the centre the orrery gives\n    them (method 3) and are measured there alone.\n\n    elements_p_days is the PR the elements fetch itself returned, around\n    location at the same date. Where the chosen centre is that location,\n    the two must agree, and the record says whether they did.\n\n    Raises on a failed query; the caller keeps the previous record.\n    """\n    test = None\n    chosen = location\n    if _is_heliocentric(location):\n        prev_test = (previous or {}).get(\'test\') or {}\n        prev_choice = (previous or {}).get(\'center\')\n        if prev_choice in (CENTRE_SUN, CENTRE_BARYCENTRE) and prev_test:\n            chosen = prev_choice\n        else:\n            chosen = None\n    if chosen is not None:\n        pair = query_period_pair(horizons_id, id_type, date_str, chosen)\n        if _is_heliocentric(location):\n            other = CENTRE_BARYCENTRE if chosen == CENTRE_SUN else CENTRE_SUN\n            other_change = prev_test.get(other)\n            change = _change(pair)\n            if change is not None and other_change is not None and change > other_change:\n                print(\'  [L-431 period] %s: around %s it moved %.6g d this year, more than \'\n                      \'%s did when chosen (%.6g d); running the two-centre test again\'\n                      % (horizons_id, chosen, change, other, other_change), flush=True)\n                chosen = None\n            else:\n                test = prev_test\n    if chosen is None:\n        sun = query_period_pair(horizons_id, id_type, date_str, CENTRE_SUN)\n        bary = query_period_pair(horizons_id, id_type, date_str, CENTRE_BARYCENTRE)\n        c_sun, c_bary = _change(sun), _change(bary)\n        test = {CENTRE_SUN: c_sun, CENTRE_BARYCENTRE: c_bary,\n                \'run\': datetime.now().strftime(\'%Y-%m-%d\')}\n        if c_bary is not None and (c_sun is None or c_bary < c_sun):\n            chosen, pair = CENTRE_BARYCENTRE, bary\n        else:\n            chosen, pair = CENTRE_SUN, sun\n        print(\'  [L-431 period] %s: year change around the Sun %s d, around the \'\n              \'barycentre %s d -> %s\'\n              % (horizons_id, _fmt(c_sun), _fmt(c_bary), chosen), flush=True)\n\n    days = pair[\'p1\']\n    change = _change(pair)\n    agrees = None\n    if elements_p_days is not None and days is not None and (\n            chosen == location or (_is_heliocentric(chosen) and _is_heliocentric(location))):\n        agrees = abs(elements_p_days - days) <= 1e-9 * abs(days)\n        print(\'  [L-431 period] %s: the elements fetch gave PR %.10g d, the period \'\n              \'query %.10g d -- %s\' % (horizons_id, elements_p_days, days,\n                                       \'agree\' if agrees else \'DISAGREE\'), flush=True)\n    sigma, sigma_status, sbdb_name = None, \'not a small body; SBDB not asked\', None\n    if days is None:\n        sigma_status = \'open orbit; SBDB not asked\'\n    elif _is_small_body(horizons_id, id_type):\n        search = sbdb_search_string(horizons_id, pair.get(\'targetname\'))\n        sigma, sigma_status, sbdb_name = fetch_sbdb_period_sigma(search)\n    errors = [x for x in (change, sigma) if x is not None]\n    err = max(errors) if errors else None\n    if err is None:\n        governs = None\n    elif sigma is not None and sigma >= (change or 0.0):\n        governs = \'sigma\'\n    else:\n        governs = \'year_change\'\n\n    return {\n        \'days\': days,\n        \'open_orbit\': days is None,\n        \'center\': chosen,\n        \'epoch\': date_str,\n        \'fetched\': datetime.now().strftime(\'%Y-%m-%d\'),\n        \'source\': \'JPL Horizons PR (sidereal orbit period)\',\n        \'year_change_days\': change,\n        \'year_step_days\': pair[\'step_days\'],\n        \'sbdb_sigma_days\': sigma,\n        \'sbdb_status\': sigma_status,\n        \'sbdb_fullname\': sbdb_name,\n        \'error_days\': err,\n        \'error_from\': governs,\n        \'test\': test,\n        \'horizons_targetname\': pair.get(\'targetname\'),\n        \'agrees_with_elements_fetch\': agrees,\n    }\n\n\ndef _change(pair):\n    if pair is None or pair[\'p1\'] is None or pair[\'p2\'] is None:\n        return None\n    return abs(pair[\'p2\'] - pair[\'p1\'])\n\n\ndef _fmt(x):\n    return \'n/a\' if x is None else \'%.6g\' % x\n\n\n# ============================================================================\n# READING (the fallback order, for showing)\n# ============================================================================\n\nclass _CacheMemo:\n    """The orbit cache as last read, and the file time it was read at."""\n    mtime = None\n    data = None\n\n\ndef _load_cache_quietly():\n    """The orbit cache, re-read only when the file changes."""\n    try:\n        from osculating_cache_manager import CACHE_FILE\n        mtime = os.path.getmtime(CACHE_FILE)\n        if _CacheMemo.mtime != mtime:\n            import json\n            with open(CACHE_FILE, \'r\', encoding=\'utf-8\') as f:\n                _CacheMemo.data = json.load(f)\n            _CacheMemo.mtime = mtime\n        return _CacheMemo.data or {}\n    except Exception:\n        return {}\n\n\ndef _cache_entry_for(obj_name, center_object_name, cache, view_only=False):\n    """\n    The cache entry the hover\'s view would have fetched: the one keyed to\n    the view\'s centre (e.g. \'Pluto@9\') where it exists, else the plain one.\n    view_only skips the plain one, for a caller whose typed value belongs\n    to the view and must not be replaced by a period around another centre.\n    """\n    osc = VIEW_TO_OSCULATING_CENTRE.get(center_object_name)\n    if osc:\n        key = \'%s@%s\' % (obj_name, osc.lstrip(\'@\'))\n        if key in cache:\n            return cache[key]\n    if view_only:\n        return None\n    return cache.get(obj_name)\n\n\ndef resolve_display_period(obj_name, center_object_name=None, parent_name=None,\n                           typed_table=None, typed_override=None, cache=None):\n    """\n    The period to SHOW for one body in one view, by the fallback order.\n\n    Returns a dict:\n        kind     \'fetched\' | \'typed\' | \'none\'\n        days     float, or None for an open orbit or nothing known\n        record   the cache\'s period record (fetched only)\n        label    the centre\'s words (fetched only)\n    typed_override is a value the caller types for its own view (Pluto\n    around the Pluto-Charon barycentre); it is printed as typed, with the\n    note, when nothing was fetched.\n    """\n    if cache is None:\n        cache = _load_cache_quietly()\n    entry = (_cache_entry_for(obj_name, center_object_name, cache,\n                              view_only=typed_override is not None)\n             if obj_name else None)\n    rec = (entry or {}).get(\'period\') if isinstance(entry, dict) else None\n    if isinstance(rec, dict) and (\'days\' in rec):\n        return {\'kind\': \'fetched\', \'days\': rec.get(\'days\'), \'record\': rec,\n                \'label\': centre_label(rec.get(\'center\'), parent_name)}\n    if typed_override is not None:\n        return {\'kind\': \'typed\', \'days\': typed_override, \'record\': None, \'label\': None}\n    if typed_table is not None and obj_name in typed_table:\n        return {\'kind\': \'typed\', \'days\': typed_table[obj_name], \'record\': None, \'label\': None}\n    return {\'kind\': \'none\', \'days\': None, \'record\': None, \'label\': None}\n\n\ndef _typed_strings(days):\n    """A typed value as typed, and its years to the same figure count."""\n    days_s = repr(float(days)) if not float(days).is_integer() else \'%d\' % days\n    digits = len(re.sub(r\'[^0-9]\', \'\', days_s).lstrip(\'0\')) or 1\n    years = days / D_PER_JULIAN_YEAR\n    years_s = \'%.*g\' % (digits, years)\n    if \'e\' in years_s:\n        years_s = \'%.*f\' % (max(digits - 1 - int(math.floor(math.log10(abs(years)))), 0), years)\n    return years_s, days_s\n\n\ndef period_hover_lines(resolved):\n    """\n    The hover\'s period lines, each ending in <br> except the last, every\n    line under 98 characters (orrery-coding-conventions, Hover Line Width).\n    The words are proposed by build 1 and Tony approves them at its look.\n    """\n    kind = resolved[\'kind\']\n    if kind == \'none\':\n        return \'Orbital period: N/A\'\n    if kind == \'typed\':\n        if resolved[\'days\'] is None:\n            return (\'Orbital period: none (open orbit)<br>\'\n                    \'Typed value, not fetched from JPL.\')\n        years_s, days_s = _typed_strings(resolved[\'days\'])\n        return (\'Orbital period: %s years (%s days)<br>\'\n                \'Typed value, not fetched from JPL.\' % (years_s, days_s))\n    rec = resolved[\'record\']\n    where = \'Around %s, from JPL Horizons, fetched %s.\' % (resolved[\'label\'], rec.get(\'fetched\'))\n    if rec.get(\'days\') is None:\n        return \'Orbital period: none (open orbit)<br>\' + where\n    err = rec.get(\'error_days\')\n    days_s = format_by_error(rec[\'days\'], err)\n    years_s = format_by_error(rec[\'days\'] / D_PER_JULIAN_YEAR,\n                              err / D_PER_JULIAN_YEAR if err else None)\n    governs = rec.get(\'error_from\')\n    if governs == \'sigma\':\n        why = "Rounded to JPL\'s stated uncertainty in the orbit."\n    elif governs == \'year_change\' and rec.get(\'sbdb_sigma_days\') is not None:\n        why = \'Rounded to how much the period changes in a year.\'\n    elif governs == \'year_change\':\n        why = (\'Rounded to how much the period changes in a year;<br>\'\n               \'JPL lists no orbit uncertainty for this body.\')\n    else:\n        why = \'No error was measured, so the digits are not rounded to one.\'\n    return (\'Orbital period: %s years (%s days)<br>%s<br>%s\'\n            % (years_s, days_s, where, why))\n\n\ndef period_panel_text(resolved):\n    """One short line for the orbital parameters window."""\n    kind = resolved[\'kind\']\n    if kind == \'none\':\n        return \'---\'\n    if resolved[\'days\'] is None:\n        return \'none (open orbit)\' + (\' - typed, not from JPL\' if kind == \'typed\' else \'\')\n    if kind == \'typed\':\n        years_s, days_s = _typed_strings(resolved[\'days\'])\n        return \'%s days (%s yr) - typed, not from JPL\' % (days_s, years_s)\n    rec = resolved[\'record\']\n    err = rec.get(\'error_days\')\n    days_s = format_by_error(rec[\'days\'], err)\n    years_s = format_by_error(rec[\'days\'] / D_PER_JULIAN_YEAR,\n                              err / D_PER_JULIAN_YEAR if err else None)\n    return \'%s days (%s yr), JPL, around %s\' % (days_s, years_s, resolved[\'label\'])\n'


LIVE_CHECK = r'''
import datetime, sys
sys.path.insert(0, '.')
from orbital_period import (build_period_record, period_hover_lines,
                            centre_label, CENTRE_SUN)
from orbit_data_manager import query_horizons_elements
date_str = datetime.datetime.now().strftime('%Y-%m-%d')
bodies = [('Encke', '90000091', 'smallbody'), ('Sedna', '2003 VB12', 'smallbody'),
          ('Mercury', '199', None), ('3I/ATLAS', 'C/2025 N1', 'smallbody')]
for name, hid, idt in bodies:
    print('-' * 70)
    print('%s (Horizons %s), %s' % (name, hid, date_str))
    try:
        el = query_horizons_elements(hid, idt, date_str)
        print('  elements fetch: P_days = %r around %s' % (el.get('P_days'), el.get('center_body')))
        rec = build_period_record(hid, idt, date_str, el.get('center_body', CENTRE_SUN),
                                  elements_p_days=el.get('P_days'))
        for k in ('days', 'center', 'year_change_days', 'sbdb_sigma_days',
                  'sbdb_status', 'sbdb_fullname', 'error_days', 'error_from', 'test',
                  'horizons_targetname'):
            print('  %-18s %r' % (k, rec.get(k)))
        print('  HOVER:')
        hover = period_hover_lines({'kind': 'fetched', 'days': rec['days'], 'record': rec,
                                    'label': centre_label(rec['center'])})
        for line in hover.split('<br>'):
            print('    ' + line)
    except Exception as ex:
        print('  NOT CHECKED: %s: %s' % (ex.__class__.__name__, ex))
print('-' * 70)
'''


def main():
    if os.path.exists(os.path.join(ROOT, 'orbital_period.py')):
        print('ERROR: orbital_period.py already exists here; this patch has run '
              'or the folder is not the one it was built for. NOTHING was written.')
        sys.exit(1)
    texts, crlf = {}, set()
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                sys.exit(1)
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        n = texts[f].count(old)
        if n != 1:
            print('ANCHOR FAIL  %-28s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            sys.exit(1)
        texts[f] = texts[f].replace(old, new)
        print('ok  %-28s %s' % (f, label))
    for f, text in texts.items():
        bad = sum(1 for c in text if ord(c) > 127)
        if bad:
            print('note: %s holds %d non-ASCII character(s) this patch did not add' % (f, bad))
    for f, text in texts.items():
        with open(os.path.join(ROOT, f), 'wb') as fh:
            fh.write(text.encode('utf-8'))
        if f in crlf:
            print('note: %s was CRLF in the working copy; written LF' % f)
    with open(os.path.join(ROOT, 'orbital_period.py'), 'wb') as fh:
        fh.write(NEW_MODULE.encode('utf-8'))
    print('ok  %-28s created' % 'orbital_period.py')
    print()
    print('patch applied (%d edits in %d files, one file created)' % (len(EDITS), len(texts)))
    print('Stamps updated: the module docstrings of all seven edited files.')
    print()
    print('LIVE CHECK -- asking JPL for four periods (nothing is written):')
    try:
        subprocess.run([sys.executable, '-c', LIVE_CHECK], cwd=ROOT, timeout=600)
    except Exception as ex:
        print('  The live check did not run (%s). The patch stands; the orrery' % ex)
        print('  will ask JPL itself when you accept an elements update.')
    print()
    print('NEXT:')
    print('  1. Paste this output into your run record.')
    print('  2. Run patch_L431_5_records_20261011.py, then orrery_maintenance_run.py.')
    print('  3. Open the orrery, tick Encke, Sedna and Mercury, press Plot, answer')
    print('     Yes to each "Update Orbital Elements?" box, and hover each body.')
    print('  4. Move both patch scripts into documentation/; commit and push.')


if __name__ == '__main__':
    main()
