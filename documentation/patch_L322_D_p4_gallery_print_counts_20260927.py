#!/usr/bin/env python3
"""
patch_L322_D_p4_gallery_print_counts_20260927.py -- L-322 Stage D, gallery
patch 4: the gallery half of build manifest section 6. Exact rows print by
the print count their rows state.

Built on gallery 70a77347cf65a14789707bf741cf203d29739c79 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with
orrery e0a0c7ccbb48c738fe8b040c66f2a5bd27871611 at
https://github.com/tonylquintanilla/palomas_orrery.
Rules: provenance-discipline 2.20, Rule 7's exact row.

WHAT IT DOES

    The seven exact rows the Earth room prints -- the two LEO altitudes,
    the outer belt's drawn peak, the solar wind pressure and Bz, and the
    two cut angles -- print by the print count each row states in
    constants_new.py, which the orrery's export serves as "prints" since
    patch D15. Until now the page printed them by a width chosen on each
    line (toFixed and toLocaleString).

    What a visitor sees change: the magnetopause hover's "Bz 0.0 nT,
    dynamic pressure 2.0 nPa" becomes "Bz 0 nT, dynamic pressure 2 nPa";
    the bow shock's "at dynamic pressure 2.0 nPa" becomes "2 nPa"; and
    the crust's "Radius: 1.0000 Earth radii" becomes "Radius: 1 Earth
    radius" (Tony, 2026-09-27). One Earth radius is defined, as the
    equatorial radius of IERS Conventions (2010), so the crust's 1 is
    exact, and the mirror now serves it with "prints": 1. Every other
    hover prints exactly as before.

    An exact row served WITHOUT a count is printed in full, its own
    digits, and reported as a warning, which the smoke checks fail on.
    The page reports it rather than choosing a width, as the skill says.

FILES

    changed  data/objects_config.json -- nine "prints" fields, exactly
             what tools/mirror_constants.py writes from the orrery's
             export, so the maintenance run's mirror step changes nothing
    changed  gallery/feature_renderers.js
    changed  tools/mirror_constants.py -- copies "prints"
    changed  tools/test_mirror_constants.py -- case 19
    changed  documentation/smoke_display_figures.js -- the new lines, the
             LEO rule, two self-test ways, the new fixture
    new      documentation/fixture_hovers_L322d_p4_on_70a77347.json

    Permanent: all of the above. This script is one-shot; archive it to
    documentation/ once it has run.

RUN COMMAND

    Save this file in the GALLERY repo root (the folder holding
    interactive.html), open it in VS Code, and click Run.

        python patch_L322_D_p4_gallery_print_counts_20260927.py

    Success: one "ok" line per edit, "PATCH APPLIED", then the next steps.
    Failure: "FAILURE: ..." and NOTHING is written; every file is checked
    before any is written. Undo after a success is Discard Changes in
    GitHub Desktop.

Written September 27, 2026 with Anthropic's Claude Opus 5.5.
"""

import base64
import hashlib
import os
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))

TARGETS = [
    ('data/objects_config.json', '562df3eebc7d35a2324e52f5e6425d65', [
        ('prints: crust radius, 1 by definition',
         b'              "value": 1.0,\n              "unit": "r_earth",\n            "figures": "exact"\n            },\n',
         b'              "value": 1.0,\n              "unit": "r_earth",\n            "prints": 1,\n            "figures": "exact"\n            },\n', 1),
        ('prints: EARTH_LEO_LOWER_ALTITUDE_KM',
         b'              "value": 200.0,\n              "unit": "km",\n              "figures": "exact",\n              "orrery_constant": "constants_new.py::EARTH_LEO_LOWER_ALTITUDE_KM"\n',
         b'              "value": 200.0,\n              "unit": "km",\n              "prints": 3,\n              "figures": "exact",\n              "orrery_constant": "constants_new.py::EARTH_LEO_LOWER_ALTITUDE_KM"\n', 1),
        ('prints: EARTH_LEO_UPPER_ALTITUDE_KM',
         b'              "value": 2000.0,\n              "unit": "km",\n              "figures": "exact",\n              "orrery_constant": "constants_new.py::EARTH_LEO_UPPER_ALTITUDE_KM"\n',
         b'              "value": 2000.0,\n              "unit": "km",\n              "prints": 4,\n              "figures": "exact",\n              "orrery_constant": "constants_new.py::EARTH_LEO_UPPER_ALTITUDE_KM"\n', 1),
        ('prints: EARTH_SOLAR_WIND_BZ_NT',
         b'                "value": 0.0,\n                "unit": "nt",\n                "figures": "exact",\n                "_declared": "A neutral midpoint chosen for this scene, NOT a figure from the paper. Both boundaries are evaluated at the same conditions so the two surfaces can be compared.",\n',
         b'                "value": 0.0,\n                "unit": "nt",\n                "prints": 1,\n                "figures": "exact",\n                "_declared": "A neutral midpoint chosen for this scene, NOT a figure from the paper. Both boundaries are evaluated at the same conditions so the two surfaces can be compared.",\n', 1),
        ('prints: EARTH_SOLAR_WIND_PRESSURE_NPA',
         b'                "value": 2.0,\n                "unit": "npa",\n                "figures": "exact",\n                "_declared": "The solar wind dynamic pressure both fits are evaluated at. Declared for this scene, not measured.",\n',
         b'                "value": 2.0,\n                "unit": "npa",\n                "prints": 1,\n                "figures": "exact",\n                "_declared": "The solar wind dynamic pressure both fits are evaluated at. Declared for this scene, not measured.",\n', 1),
        ('prints: EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG',
         b'                "value": 120.0,\n                "unit": "deg",\n                "figures": "exact",\n                "_declared": "Where the drawn surface stops, measured from the nose. Shue\'s surface has no end: at this flaring the radius grows without bound as theta approaches 180 degrees, so a drawing must choose a stop. Shue et al. (1998) fig. 6, p. 17,695 plots the model out to 120 degrees, the furthest the authors evaluate it. A drawing limit, not an edge.",\n',
         b'                "value": 120.0,\n                "unit": "deg",\n                "prints": 3,\n                "figures": "exact",\n                "_declared": "Where the drawn surface stops, measured from the nose. Shue\'s surface has no end: at this flaring the radius grows without bound as theta approaches 180 degrees, so a drawing must choose a stop. Shue et al. (1998) fig. 6, p. 17,695 plots the model out to 120 degrees, the furthest the authors evaluate it. A drawing limit, not an edge.",\n', 1),
        ('prints: EARTH_SOLAR_WIND_PRESSURE_NPA',
         b'                "value": 2.0,\n                "unit": "npa",\n                "figures": "exact",\n                "_declared": "The same declared pressure as the magnetopause. Both surfaces must be evaluated at the same conditions or their relative positions mean nothing.",\n',
         b'                "value": 2.0,\n                "unit": "npa",\n                "prints": 1,\n                "figures": "exact",\n                "_declared": "The same declared pressure as the magnetopause. Both surfaces must be evaluated at the same conditions or their relative positions mean nothing.",\n', 1),
        ('prints: EARTH_BOW_SHOCK_CUT_ANGLE_DEG',
         b'                "value": 105.0,\n                "unit": "deg",\n                "figures": "exact",\n                "_declared": "Where the drawn surface stops, measured from the nose. Jelinek et al. fitted crossings within 7 hours of local noon either side, and 7 hours of Earth\'s turn is 105 degrees. A drawing limit set by where the data was, not by where the formula fails -- the opposite reason from the magnetopause\'s 120.",\n',
         b'                "value": 105.0,\n                "unit": "deg",\n                "prints": 3,\n                "figures": "exact",\n                "_declared": "Where the drawn surface stops, measured from the nose. Jelinek et al. fitted crossings within 7 hours of local noon either side, and 7 hours of Earth\'s turn is 105 degrees. A drawing limit set by where the data was, not by where the formula fails -- the opposite reason from the magnetopause\'s 120.",\n', 1),
        ('prints: EARTH_VAN_ALLEN_OUTER_RADII',
         b'            "value": 4.5,\n            "unit": "l_shell",\n            "figures": "exact",\n            "source": "Li et al. (2025), J. Geophys. Res. Space Physics, doi:10.1029/2024JA033504 -- sec. 1, the outer belt is most intense around L = 4 and 5; the value served is our midpoint of that band. Kellerman et al. (2014), as reported in arXiv:1809.00902 -- maximum electron flux at L = 4-5; the arXiv paper is the document opened and Kellerman is the layer below it.",\n',
         b'            "value": 4.5,\n            "unit": "l_shell",\n            "prints": 2,\n            "figures": "exact",\n            "source": "Li et al. (2025), J. Geophys. Res. Space Physics, doi:10.1029/2024JA033504 -- sec. 1, the outer belt is most intense around L = 4 and 5; the value served is our midpoint of that band. Kellerman et al. (2014), as reported in arXiv:1809.00902 -- maximum electron flux at L = 4-5; the arXiv paper is the document opened and Kellerman is the layer below it.",\n', 1),
    ]),
    ('gallery/feature_renderers.js', '815ad8acf5aedbdddf2d412bbb3f7b6c', [
        ('stamp',
         b' *   and larger, and the typed 0.5 belt thickness fallback is gone).\n */\n',
         b' *   and larger, and the typed 0.5 belt thickness fallback is gone).\n * Module updated: September 27, 2026 with Anthropic\'s Claude Opus 5.5\n *   (L-322 Stage D, gallery patch 4, build manifest section 6: an exact\n *   row prints by the print count its row states in constants_new.py,\n *   which the export serves and the mirror copies as "prints", never by a\n *   width chosen on the line -- provenance-discipline 2.20, Rule 7. An\n *   exact row served with no count is printed in full and reported as a\n *   warning. The magnetopause and bow shock hovers now read "Bz 0 nT" and\n *   "2 nPa", and the crust\'s "Radius: 1 Earth radius" (Tony,\n *   2026-09-27); every other hover prints as before).\n */\n', 1),
        ('the list of uncounted exact rows',
         b'  var KM_PER_AU = null;\n',
         b'  var KM_PER_AU = null;\n  // L-322 Stage D, gallery patch 4: exact rows this build printed with no\n  // print count, by name. buildFeatureTraces empties it on the way in and\n  // turns each into a warning on the way out, so the page REPORTS such a\n  // row rather than choosing a width for it (provenance-discipline 2.20,\n  // Rule 7). The smoke checks fail on any warning.\n  var exactUncounted = [];\n', 1),
        ('servedFigures reads the print count',
         b'  function servedFigures(node) {\n    return (isDict(node) && typeof node.figures === "number")\n      ? node.figures : null;\n  }\n',
         b'  function servedFigures(node) {\n    if (!isDict(node)) { return null; }\n    if (typeof node.figures === "number") { return node.figures; }\n    /* L-322 Stage D, gallery patch 4 (provenance-discipline 2.20, Rule 7):\n       an exact value prints by the print count served beside it as\n       "prints" -- an exact row\'s count, copied by the mirror from its row\n       in constants_new.py, or 1 for the crust\'s one Earth radius by\n       definition, which the mirror writes too. An EXACT ROW -- a node\n       pointing at a row of constants_new.py -- served with no count is\n       named for the warnings and answered "exact", which the formatters\n       print in full instead of to a width. */\n    if (node.figures === "exact") {\n      if (typeof node.prints === "number") { return node.prints; }\n      if (typeof node.orrery_constant === "string") {\n        if (exactUncounted.indexOf(node.orrery_constant) < 0) {\n          exactUncounted.push(node.orrery_constant);\n        }\n        return "exact";\n      }\n    }\n    return null;\n  }\n', 1),
        ('fmtServed prints an uncounted exact row in full',
         b'  function fmtServed(value, figures, digits) {\n    return (typeof figures === "number")\n      ? sigFigures(value, figures) : value.toFixed(digits);\n  }\n',
         b'  function fmtServed(value, figures, digits) {\n    // L-322 Stage D, gallery patch 4: an exact row with no print count is\n    // printed in full, its own digits, and servedFigures() has reported it.\n    if (figures === "exact") { return String(value); }\n    return (typeof figures === "number")\n      ? sigFigures(value, figures) : value.toFixed(digits);\n  }\n', 1),
        ('fmtKm prints an uncounted exact row in full',
         b'  function fmtKm(km, figures) {\n    if (typeof figures !== "number") {\n',
         b'  function fmtKm(km, figures) {\n    // L-322 Stage D, gallery patch 4: in full, as fmtServed() does.\n    if (figures === "exact") {\n      return km.toLocaleString("en-US", { maximumFractionDigits: 20 }) + " km";\n    }\n    if (typeof figures !== "number") {\n', 1),
        ('LEO altitude prints by its count',
         b'        out.altitudeKm = alt.value;             // Rule S\n        out.altitudeFigures = servedFigureField(alt);\n',
         b'        out.altitudeKm = alt.value;             // Rule S\n        // L-322 Stage D, gallery patch 4: an exact altitude (the two LEO\n        // edges) prints by its row\'s print count; the figure field is for\n        // arithmetic, where an exact input is skipped.\n        out.altitudeFigures = (servedFigureField(alt) === "exact")\n          ? servedFigures(alt) : servedFigureField(alt);\n', 1),
        ('belts: a print count per belt',
         b'    var figures = [];\n    // L-291: a belt distance may be a measured entry {value, unit\n',
         b"    var figures = [];\n    // L-322 Stage D, gallery patch 4: what each belt's distance PRINTS by.\n    // figures[] stays the figure field, for arithmetic; counts[] is what a\n    // hover formats to, which for an exact row is its print count.\n    var counts = [];\n    // L-291: a belt distance may be a measured entry {value, unit\n", 1),
        ('belts: collect the print count',
         b'        figures.push(servedFigureField(node));\n        return node.value;\n',
         b'        figures.push(servedFigureField(node));\n        counts.push(servedFigures(node));\n        return node.value;\n', 1),
        ('belts: the three print sites',
         b'fmtServed(distances[i], figures[i], 1)',
         b'fmtServed(distances[i], counts[i], 1)', 3),
        ('buildFeatureTraces: start empty',
         b'    function warn(msg) { warnings.push(msg); }\n\n    // L-322 Stage D: every served distance is converted with the served\n',
         b'    function warn(msg) { warnings.push(msg); }\n    exactUncounted.length = 0;\n\n    // L-322 Stage D: every served distance is converted with the served\n', 1),
        ('buildFeatureTraces: report uncounted exact rows',
         b'    return { traces: traces, warnings: warnings };\n  }\n',
         b'    // L-322 Stage D, gallery patch 4: report, never a width.\n    for (i = 0; i < exactUncounted.length; i++) {\n      warn(exactUncounted[i] + ": an exact row printed with no print " +\n           "count, so it was printed in full; its row in constants_new.py " +\n           "states none (provenance-discipline Rule 7)");\n    }\n    exactUncounted.length = 0;\n    return { traces: traces, warnings: warnings };\n  }\n', 1),
        ('the crust: 1 Earth radius, shell set path',
         b'      hover += "Radius: " +\n        fmtServed(cfg.radius.value, servedFigures(cfg.radius), 4) +\n        " Earth radii<br>";\n      if (km && km.altitudeKm !== null) {\n',
         b'      // L-322 Stage D, gallery patch 4: the crust\'s exact 1 prints as "1",\n      // and one of anything is singular (Tony, 2026-09-27).\n      var radiusText = fmtServed(cfg.radius.value, servedFigures(cfg.radius),\n                                 4);\n      hover += "Radius: " + radiusText +\n        (radiusText === "1" ? " Earth radius<br>" : " Earth radii<br>");\n      if (km && km.altitudeKm !== null) {\n', 1),
        ('the crust: 1 Earth radius, earth shell path',
         b'        hover += "Radius: " +\n        fmtServed(cfg.radius.value, servedFigures(cfg.radius), 4) +\n        " Earth radii<br>";\n',
         b'        // L-322 Stage D, gallery patch 4: as the shell set path above.\n        var rText = fmtServed(cfg.radius.value, servedFigures(cfg.radius), 4);\n        hover += "Radius: " + rText +\n          (rText === "1" ? " Earth radius<br>" : " Earth radii<br>");\n', 1),
        ('export servedFigures for the smoke check',
         b'    _fmtServed: fmtServed,\n',
         b'    _fmtServed: fmtServed,\n    // L-322 Stage D, gallery patch 4: so the hover suite can check that an\n    // exact row prints by its served count.\n    _servedFigures: servedFigures,\n', 1),
    ]),
    ('tools/mirror_constants.py', '38fc444fbf579d28f5955efd8e20a8df', [
        ('docstring: what it writes',
         b"               row's uncertainty where the export serves one (schema 4\n               and later; a row with none gets no field). Nothing else\n",
         b'               row\'s uncertainty where the export serves one (schema 4\n               and later; a row with none gets no field), and the print\n               count an exact row states, as "prints" (schema 5 and\n               later; a row with none gets no field). Nothing else\n', 1),
        ('docstring: stamp',
         b'is no longer one of the planet_poles links).\n"""\n',
         b'is no longer one of the planet_poles links).\nModule updated: September 27, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, gallery patch 4: the export\'s "prints", the print count\nan exact row states, is written beside the value, so the page prints an\nexact row by that count; the crust\'s 1 Earth radius by definition gets\n"prints": 1, its one digit, so the crust reads "1 Earth radius" and not\n"1.0000" (Tony, 2026-09-27). provenance-discipline 2.20, Rule 7).\n"""\n', 1),
        ('FIELDS gains prints',
         b'FIELDS = ("value", "unit", "figures", "uncertainty")\n',
         b'# L-322 Stage D, gallery patch 4: "prints" joins them, the print count\n# of an exact row a display prints (schema 5), or null, which is never\n# inserted.\nFIELDS = ("value", "unit", "figures", "uncertainty", "prints")\n', 1),
        ('a definition carries no print count',
         b'            wanted = {"value": 1.0, "unit": defines, "figures": "exact",\n                      "uncertainty": None}\n',
         b'            wanted = {"value": 1.0, "unit": defines, "figures": "exact",\n                      "uncertainty": None, "prints": 1}\n', 1),
        ('docstring: the definition prints 1',
         b'    measured in that token, the mirror writes 1 with figures "exact".\n',
         b'    measured in that token, the mirror writes 1 with figures "exact",\n    and "prints": 1, because the definition\'s one is its one digit: the\n    crust\'s hover reads "1 Earth radius", not "1.0000" (L-322 Stage D,\n    gallery patch 4, Tony\'s ruling of 2026-09-27).\n', 1),
        ('.get comment',
         b'        # .get: an export before schema 4 carries no "uncertainty".\n',
         b'        # .get: an export before schema 4 carries no "uncertainty", and\n        # one before schema 5 no "prints".\n', 1),
    ]),
    ('tools/test_mirror_constants.py', '111cb5db4fbf1bb7d54ff7b443a6184b', [
        ('docstring: case 19',
         b"    18. Earth's pole links to the store's fallback rows and is SERVED;\n        the real config no longer holds a planet_poles['Earth'] link\n",
         b'    18. Earth\'s pole links to the store\'s fallback rows and is SERVED;\n        the real config no longer holds a planet_poles[\'Earth\'] link\n    19. a print count the export serves is written beside the value as\n        "prints"; a row with none gets no field; the crust\'s 1 by\n        definition gets 1; a second run changes nothing; an export\n        from before schema 5 leaves the entries as they were\n', 1),
        ('docstring: stamp',
         b'the store is Jupiter\'s pole now, because Earth\'s is served).\n"""\n',
         b'the store is Jupiter\'s pole now, because Earth\'s is served).\nModule updated: September 27, 2026 with Anthropic\'s Claude Opus 5.5\n(L-322 Stage D, gallery patch 4: case 19, the print count).\n"""\n', 1),
        ('case 19',
         b'def real_config_earth_pole(root):\n',
         b'# ------------------------------------------------------------------\n# 19: the print count (L-322 Stage D, gallery patch 4).\n# ------------------------------------------------------------------\n\nPRINTS_CONFIG = \'\'\'{\n  "features": {\n    "counted": {\n      "value": 2.0, "unit": "npa", "figures": "exact",\n      "orrery_constant": "constants_new.py::EARTH_PRESSURE_NPA"\n    },\n    "uncounted": {\n      "value": 30.0, "unit": "r_earth", "figures": "exact",\n      "orrery_constant": "constants_new.py::EARTH_DRAWN_RADII"\n    }\n  }\n}\n\'\'\'\n\n\ndef with_prints(entry, prints):\n    entry = dict(entry)\n    entry["prints"] = prints\n    return entry\n\n\ndef prints_cases():\n    export = export_with({\n        "EARTH_PRESSURE_NPA": with_prints(row(2.0, "npa", "exact"), 1),\n        "EARTH_DRAWN_RADII": with_prints(row(30.0, "r_earth", "exact"), None),\n    })\n    links, failures, by_name = plan_of(PRINTS_CONFIG, export)\n    check(not failures, "19: nothing here is refused, got %r"\n          % [f.name for f in failures])\n    written = json.loads(mirror.apply_changes(PRINTS_CONFIG, links))\n    written = written["features"]\n    check(written["counted"].get("prints") == 1,\n          "19: a served print count is written, got %r"\n          % written["counted"].get("prints"))\n    check("prints" not in written["uncounted"],\n          "19: a row with no print count gets no field")\n    once = mirror.apply_changes(PRINTS_CONFIG, links)\n    second, _f, _b = plan_of(once, export)\n    check(not any(l.changes for l in second),\n          "19: a second run changes nothing")\n    # The crust\'s 1 by definition: exact, and it prints its one digit.\n    dlinks, _df, _db = plan_of(DEFINITION_CONFIG, DEFINITION_EXPORT)\n    slot = json.loads(mirror.apply_changes(DEFINITION_CONFIG, dlinks))\n    slot = slot["features"]["crust"]["radius"]\n    check(slot.get("prints") == 1,\n          "19: a definition\'s 1 prints as 1, got %r" % slot.get("prints"))\n    # An export from before schema 5 has no "prints" key at all.\n    old = export_with({\n        "EARTH_PRESSURE_NPA": row(2.0, "npa", "exact"),\n        "EARTH_DRAWN_RADII": row(30.0, "r_earth", "exact"),\n    })\n    for r in old["rows"].values():\n        r.pop("prints", None)\n    links3, failures3, _ = plan_of(PRINTS_CONFIG, old)\n    check(not failures3 and not any(l.changes for l in links3),\n          "19: an export before schema 5 leaves the entries as they were")\n\n\ndef real_config_earth_pole(root):\n', 1),
        ('main runs case 19',
         b'    uncertainty_cases()\n    real_config_earth_pole(root)\n',
         b'    uncertainty_cases()\n    prints_cases()\n    real_config_earth_pole(root)\n', 1),
        ('final message',
         b'          "uncertainty written as served, Earth\'s pole served."\n',
         b'          "uncertainty written as served, Earth\'s pole served, print "\n          "count written as served."\n', 1),
    ]),
    ('documentation/smoke_display_figures.js', 'aabe28f8cd682219a3a9e22fcb3d8a58', [
        ('header: rule F',
         b'//   F, format it.    A declared count prints to exactly that many\n//                    figures with a thousands separator and keeps a\n//                    significant trailing zero; no count prints exactly\n//                    as it does today; the AU in brackets shows three\n//                    figures or the count, whichever is fewer.\n',
         b'//   F, format it.    A declared count prints to exactly that many\n//                    figures with a thousands separator and keeps a\n//                    significant trailing zero; no count prints exactly\n//                    as it does today; the AU in brackets shows three\n//                    figures or the count, whichever is fewer. An exact\n//                    row prints by the print count its row states,\n//                    served as "prints" (provenance-discipline 2.20,\n//                    Rule 7; gallery patch 4).\n', 1),
        ('header: history',
         b'// fixture_hovers_L322d_p3_on_c6000f03.json; the D7 one is left in place,\n// unreferenced, as that one left its own predecessor.\n',
         b'// fixture_hovers_L322d_p3_on_c6000f03.json; the D7 one is left in place,\n// unreferenced, as that one left its own predecessor.\n// Updated September 27, 2026 with Anthropic\'s Claude Opus 5.5 (L-322\n// Stage D, gallery patch 4): an exact row prints by its served print\n// count. The LEO altitude rule reads it; the magnetopause and bow shock\n// are graded on their new lines, "Bz 0 nT, dynamic pressure 2 nPa" and\n// "at dynamic pressure 2 nPa", and fail on the old "0.0" and "2.0"; the\n// crust\'s radius line reads "Radius: 1 Earth radius" (Tony, 2026-09-27). The\n// self-test gains two ways to go red: the page not reading a served\n// count, and the page not reporting an exact row served without one.\n// The fixture is re-recorded as fixture_hovers_L322d_p4_on_70a77347.json;\n// the patch 3 one is left in place, unreferenced.\n', 1),
        ('fixture',
         b'const FIXTURE_AT = "c6000f03";\nconst FIXTURE = path.join(root, "documentation",\n                          "fixture_hovers_L322d_p3_on_c6000f03.json");\n',
         b'const FIXTURE_AT = "70a77347";\nconst FIXTURE = path.join(root, "documentation",\n                          "fixture_hovers_L322d_p4_on_70a77347.json");\n', 1),
        ('printCount',
         b'/* Rule 3, products and quotients: the fewest figures among the\n',
         b'/* What a served entry PRINTS by, as distinct from the count it\n   declares for arithmetic: an exact row\'s print count where one is\n   served, otherwise figures(). L-322 Stage D, gallery patch 4. */\nfunction printCount(node) {\n  if (node && typeof node === "object" && node.figures === "exact" &&\n      typeof node.prints === "number") return node.prints;\n  return figures(node);\n}\n\n/* Rule 3, products and quotients: the fewest figures among the\n', 1),
        ('LEO altitude prints by its count',
         b'    if (servedAlt) {                     // Rule S\n      out.altKm = servedAlt.value;\n      out.altFig = figures(servedAlt);\n',
         b'    if (servedAlt) {                     // Rule S\n      out.altKm = servedAlt.value;\n      out.altFig = printCount(servedAlt);  // gallery patch 4\n', 1),
        ('magnetopause lines',
         b'            "Beyond that angle the boundary is drawn as the magnetotail."],\n    absent: ["10.25", "65,376", "0.000437", "without limit"] },\n',
         b'            "Beyond that angle the boundary is drawn as the magnetotail.",\n            // gallery patch 4: the two declared conditions print by\n            // their rows\' print counts (Tony, 2026-09-27).\n            "Bz 0 nT, dynamic pressure 2 nPa"],\n    absent: ["10.25", "65,376", "0.000437", "without limit",\n             "0.0 nT", "2.0 nPa"] },\n', 1),
        ('bow shock lines',
         b'            "within 0.69 Earth radii of this model."],\n    absent: ["13.51", "86,180"] },\n',
         b'            "within 0.69 Earth radii of this model.",\n            // gallery patch 4, as the magnetopause.\n            "Jelinek et al. (2012), at dynamic pressure 2 nPa"],\n    absent: ["13.51", "86,180", "2.0 nPa"] },\n', 1),
        ('radiiLine prints by the count, singular at 1',
         b'function radiiLine(shell) {\n  const r = shell.radius;\n  const f = figures(r);\n',
         b'function radiiLine(shell) {\n  const r = shell.radius;\n  const f = printCount(r);            // gallery patch 4\n', 1),
        ('radiiLine singular',
         b'    : r.value.toFixed(4);\n  return "Radius: " + shown + " Earth radii";\n}\n',
         b'    : r.value.toFixed(4);\n  // gallery patch 4: the crust\'s exact 1 prints as "1", and singular.\n  return "Radius: " + shown + (shown === "1" ? " Earth radius" : " Earth radii");\n}\n', 1),
        ('self-test: two ways',
         b'  failures.length = p0;\n  examinedNames.length = n0;\n  numbersExamined = counted;\n  return notes;\n}\n',
         b'  // 7. gallery patch 4: the page prints an exact row by its served\n  // print count, and reports one served without a count.\n  const sf = GalleryFeatures._servedFigures;\n  if (sf({ value: 2.0, figures: "exact", prints: 1,\n           orrery_constant: "constants_new.py::X" }) !== 1) {\n    notes.push("the page did not read a served print count");\n  }\n  const bare = JSON.parse(JSON.stringify(cacheFeatures("earth") || {}));\n  const mpNode = bare.earth_magnetosphere &&\n    bare.earth_magnetosphere.magnetopause &&\n    bare.earth_magnetosphere.magnetopause.surface &&\n    bare.earth_magnetosphere.magnetopause.surface.bz;\n  if (!mpNode) {\n    notes.push("no served magnetopause Bz to test the report with");\n  } else {\n    delete mpNode.prints;\n    const reported = hoversOf("earth", bare, EARTH_OPTS).warnings\n      .filter(function (w) { return w.indexOf("EARTH_SOLAR_WIND_BZ_NT") >= 0; });\n    if (reported.length !== 1) {\n      notes.push("the page did not report an exact row served with no " +\n                 "print count");\n    }\n  }\n  failures.length = p0;\n  examinedNames.length = n0;\n  numbersExamined = counted;\n  return notes;\n}\n', 1),
        ('self-test count',
         b'              "(17 ways).\\n");\n',
         b'              "(19 ways).\\n");\n', 1),
    ]),
]

FIXTURE = 'documentation/fixture_hovers_L322d_p4_on_70a77347.json'
FIXTURE_MD5 = 'e55da84c88b4e671180348e78ca0625b'
FIXTURE_ZLIB_B64 = (
    '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'
    '///FvwHWROz2'
)

NEXT_STEPS = """
NEXT STEPS, in this order (a config change is not deployed until the
cache is rebuilt):

  1. (do) Run the cache builder by hand, as you do each night. It copies
     the nine new "prints" fields into the served cache.
  2. (do) Run python gallery_maintenance_run.py. Expect every offline
     check to pass. The pull brings the orrery's schema-5 export, and
     the Config mirror step should say "Unchanged": the nine fields are
     already there. "Display figures" should show the magnetopause and
     bow shock graded on their new lines.
  3. (do) Commit the config and the cache together, and push.
  4. (do) On your phone, close the tab and reopen the Earth room. Look at
     the magnetopause hover: "Bz 0 nT, dynamic pressure 2 nPa". And the
     bow shock hover: "at dynamic pressure 2 nPa". And the crust:
     "Radius: 1 Earth radius". Then the outer belt
     ("Drawn at 4.5 Earth radii"), and the two LEO shells ("Altitude:
     200 km", "Altitude: 2,000 km"), which should read as before. Then
     open the Sun room; it should look as it did.
  5. (do) In the ORRERY folder, run the orrery maintenance run. "Exact
     rows by the count" now passes: it reads this gallery's config and
     finds all eleven prints served their count. Commit and push the
     orrery's regenerated files.
  6. (do) Move this script into documentation/.
"""


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(msg):
    print('FAILURE: ' + msg)
    print('NOTHING was written. Undo is not needed.')
    sys.exit(1)


def main():
    if os.path.basename(os.getcwd()) == 'documentation' or \
            os.path.basename(HERE) == 'documentation':
        fail('this is running from documentation/. Run it from the gallery '
             'repo root, then file it in documentation/.')
    if not os.path.exists(os.path.join(HERE, 'interactive.html')):
        fail('interactive.html is not beside this script. Save it in the '
             'GALLERY repo root, not the orrery.')
    results = []
    for rel, fp, edits in TARGETS:
        path = os.path.join(HERE, rel)
        if not os.path.exists(path):
            fail('%s not found' % rel)
        with open(path, 'rb') as handle:
            data = handle.read()
        got = fingerprint(data)
        if got != fp:
            fail('%s is not the file this patch was built on (fingerprint '
                 '%s, expected %s). Pull or discard local changes first.'
                 % (rel, got, fp))
        crlf = data.count(b'\r\n') > 0
        for label, old, new, count in edits:
            if crlf:
                old = old.replace(b'\n', b'\r\n')
                new = new.replace(b'\n', b'\r\n')
            n = data.count(old)
            if n != count:
                fail('%s: "%s" -- expected %d match(es), got %d'
                     % (rel, label, count, n))
            data = data.replace(old, new)
            print('ok    %s: %s' % (rel, label))
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('%s would not be ASCII after the patch (%s)' % (rel, exc))
        results.append((path, data))
    fixture_path = os.path.join(HERE, FIXTURE)
    if os.path.exists(fixture_path):
        fail('%s already exists' % FIXTURE)
    fixture = zlib.decompress(base64.b64decode(''.join(FIXTURE_ZLIB_B64)))
    if hashlib.md5(fixture).hexdigest() != FIXTURE_MD5:
        fail('the embedded fixture does not match its checksum')
    print('ok    %s: new, %d bytes' % (FIXTURE, len(fixture)))
    for path, data in results:
        with open(path, 'wb') as handle:
            handle.write(data)
    with open(fixture_path, 'wb') as handle:
        handle.write(fixture)
    print('stamp gallery/feature_renderers.js, tools/mirror_constants.py, '
          'tools/test_mirror_constants.py, documentation/'
          'smoke_display_figures.js: updated September 27, 2026 '
          '(gallery patch 4)')
    print('PATCH APPLIED: %d files changed, 1 new.' % len(results))
    print(NEXT_STEPS)


if __name__ == '__main__':
    main()
