#!/usr/bin/env python3
"""
patch_L395_1_objects_export_20261001.py -- ORRERY repo.
The orrery's object list starts feeding the website: the first build of
L-395, for the Solar System room's eleven bodies.

Run: save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
open it in VS Code and click Run. The same as: python
patch_L395_1_objects_export_20261001.py

A patch is run from its repository's ROOT and filed in documentation/
AFTER it has run. This script refuses to run from documentation/.

Built on orrery 6b2ef097da67e67ab8f748b5481c222e5dd34acc
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 5a38de15d69df48749ba230cdfacf0e9d9e2fb5e
at https://github.com/tonylquintanilla/tonyquintanilla.github.io;
its half is patch_L395_2_objects_mirror_20261001.py, run AFTER this one
is pushed)

It runs whether or not you ran patch_L395_mars_jupiter_links_20261001.py
first. If you did not, this patch makes the same two link fixes, and the
small patch then has nothing left to do: move it to documentation/
unrun.

WHAT IT DOES.

  celestial_objects.py
      - A 'key' on the eleven entries the room serves: sun, mercury,
        venus, earth, mars, jupiter, saturn, uranus, neptune,
        pluto_barycenter, apophis. Spelled as the website spells them.
        Never shown; it is how the website finds the entry.
      - Mars and Jupiter link to NASA's planet pages (if not done yet).
      - Pluto-Charon Barycenter: "System period: 6.39 days." removed,
        because a description has nowhere to cite a source (Fetched vs
        Recalled: remove and note the gap). It links to NASA's Pluto
        page, the page the room's Pluto row was ruled to link to on
        2026-09-30; NASA has no barycentre page.
  export_objects.py         NEW generator: data/objects_export.json, the
                            keyed entries' name, Horizons id, id type,
                            description (without its "Horizons:" opening)
                            and link.
  test_objects_export.py    NEW checker: the export matches the list, and
                            no entry in the whole list writes a field
                            twice. It shows both can fail before trusting
                            a pass.
  orrery_maintenance_run.py the generator and the checker join the run.
  documentation/ORBITAL_MECHANICS_README_v1_4.md   a dated note: the
                            code gives Haumea 920136108 (Haumea itself),
                            not the barycentre id the examples show.

Everything is written or nothing is.

SUCCESS looks like: one "ok" line per edit and per new file, then
"patch applied". FAILURE looks like one ERROR: or ANCHOR FAIL: line, and
NOTHING is written. Undo is Discard Changes in GitHub Desktop.

Written October 1, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

SPEC = {'NEW': {'export_objects.py': '"""\nexport_objects.py -- write data/objects_export.json from the object list\nin celestial_objects.py. The orrery is the one definition of each object;\nthe gallery reads this file and never reads orrery source.\n\nRUN COMMAND\n-----------\nOpen this file in VS Code and click Run. It takes no arguments.\n\n    python export_objects.py\n\norrery_maintenance_run.py runs it on every maintenance run, as a\nGENERATOR, beside export_constants.py. Running it by hand is the same\nthing.\n\nWHICH ENTRIES ARE EXPORTED\n--------------------------\nOnly an entry in OBJECT_DEFINITIONS that carries a \'key\' field. The key\nis the website\'s name for the object, spelled exactly as the website\'s\ndata/objects_config.json spells its "slug" (\'mars\', \'pluto_barycenter\').\nIt is never shown to anyone, so renaming a display name cannot break the\nlink (Tony\'s ruling, 2026-10-01, L-395). An entry gains a key when the\nwebsite starts serving it, and not before.\n\nWHAT IT WRITES\n--------------\nOne JSON file, data/objects_export.json:\n\n    schema          1\n    source_sha256   the sha256 of celestial_objects.py, CRLF normalised\n                    to LF, so test_objects_export.py can tell whether the\n                    list moved after the export was made\n    objects         one entry per key, in list order:\n                      name         the entry\'s \'name\'\n                      horizons_id  the entry\'s \'id\'\n                      id_type      the entry\'s \'id_type\', or null where\n                                   the entry leaves it blank. A blank is\n                                   not a value: the gallery keeps its own\n                                   where the list states none\n                      description  the entry\'s \'mission_info\', with the\n                                   opening "Horizons: ..." sentence\n                                   removed when it has one. The website\n                                   prints the Horizons id on its own\n                                   source line, so the opening is the\n                                   orrery\'s and stays in the orrery\n                                   (Tony\'s ruling, 2026-10-01)\n                      info_url     the entry\'s \'mission_url\', or null\n    numbers         for each key whose description holds a digit, the\n                    numbers it holds, as written. Reported, so that no\n                    number reaches the website unseen: a number in a\n                    served description is sourced or comes out\n                    (provenance-discipline, Fetched vs Recalled)\n\nWHAT MAKES IT FAIL (exit 1, and NOTHING is written)\n---------------------------------------------------\n    - celestial_objects.py does not parse, or OBJECT_DEFINITIONS is not a\n      list of dict literals\n    - an entry writes the same field twice (the second silently wins in\n      Python, so one of the two is invisible)\n    - a key that is not lower-case letters, digits and underscores, or\n      two entries with the same key\n    - a keyed entry whose name, id, mission_info or mission_url is not a\n      plain literal\n    - an exported description that still says "Horizons:"\n\nThe list is read with Python\'s own parser (ast), not imported, so the\nexport never runs the orrery\'s code and cannot be changed by it.\n\nDETERMINISTIC ON PURPOSE\n------------------------\nThe same list bytes give the same export bytes: no timestamp, no git\nSHA (the gallery records the SHA it pulls at, as it does for the\nconstants export). The file is only written when its content would\nchange, and always with LF line endings.\n\nRole: devtool\nDomain: dev_tools\n\nModule created: October 1, 2026 with Anthropic\'s Claude Opus 5.5\n(L-395, the first build: the Solar System room\'s eleven bodies take\ntheir names, Horizons ids, descriptions and NASA links from the orrery).\n"""\n\nimport ast\nimport hashlib\nimport json\nimport os\nimport re\nimport sys\n\nSOURCE = "celestial_objects.py"\nTARGET = os.path.join("data", "objects_export.json")\nSCHEMA = 1\nKEY_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")\nOPENING = re.compile(r"^Horizons:[^.]*\\.\\s*")\nNUMBER = re.compile(r"\\d[\\d,.]*\\d|\\d")\nFIELDS = ("name", "id", "id_type", "mission_info", "mission_url")\n\n\nclass ExportError(Exception):\n    pass\n\n\ndef source_sha256(raw):\n    return hashlib.sha256(raw.replace(b"\\r\\n", b"\\n")).hexdigest()\n\n\ndef definitions(text):\n    """The OBJECT_DEFINITIONS list node. Raises ExportError."""\n    try:\n        tree = ast.parse(text)\n    except SyntaxError as exc:\n        raise ExportError("%s does not parse: %s" % (SOURCE, exc))\n    for node in tree.body:\n        if (isinstance(node, ast.Assign)\n                and any(getattr(t, "id", None) == "OBJECT_DEFINITIONS"\n                        for t in node.targets)):\n            if not isinstance(node.value, ast.List):\n                raise ExportError("OBJECT_DEFINITIONS is not a list literal")\n            return node.value\n    raise ExportError("OBJECT_DEFINITIONS was not found in %s" % SOURCE)\n\n\ndef entry_label(entry):\n    for k, v in zip(entry.keys, entry.values):\n        if isinstance(k, ast.Constant) and k.value == "name":\n            if isinstance(v, ast.Constant):\n                return str(v.value)\n    return "the entry at line %d" % entry.lineno\n\n\ndef repeated_fields(list_node):\n    """[(entry label, field, [line numbers])] for every field written twice."""\n    found = []\n    for entry in list_node.elts:\n        if not isinstance(entry, ast.Dict):\n            raise ExportError("an item at line %d of OBJECT_DEFINITIONS is "\n                              "not a dict literal" % entry.lineno)\n        seen = {}\n        for k in entry.keys:\n            if isinstance(k, ast.Constant) and isinstance(k.value, str):\n                seen.setdefault(k.value, []).append(k.lineno)\n        for field, lines in seen.items():\n            if len(lines) > 1:\n                found.append((entry_label(entry), field, lines))\n    return found\n\n\ndef literal_fields(entry):\n    """{field: value} for the fields the export reads, as literals."""\n    out = {}\n    for k, v in zip(entry.keys, entry.values):\n        if isinstance(k, ast.Constant) and k.value in FIELDS + ("key",):\n            try:\n                out[k.value] = ast.literal_eval(v)\n            except ValueError:\n                raise ExportError("%s: \'%s\' is not a plain literal"\n                                  % (entry_label(entry), k.value))\n    return out\n\n\ndef description_of(mission_info):\n    text = (mission_info or "").strip()\n    return OPENING.sub("", text, count=1).strip()\n\n\ndef build_export(text):\n    """The export dict for the list\'s source text. Raises ExportError."""\n    list_node = definitions(text)\n    repeats = repeated_fields(list_node)\n    if repeats:\n        raise ExportError("; ".join(\n            "%s writes \'%s\' %d times (lines %s)"\n            % (label, field, len(lines), ", ".join(map(str, lines)))\n            for label, field, lines in repeats))\n    objects = {}\n    numbers = {}\n    for entry in list_node.elts:\n        f = literal_fields(entry)\n        if "key" not in f:\n            continue\n        key = f["key"]\n        if not isinstance(key, str) or not KEY_PATTERN.match(key):\n            raise ExportError("%s: key %r is not lower-case letters, digits "\n                              "and underscores" % (f.get("name"), key))\n        if key in objects:\n            raise ExportError("key \'%s\' is on two entries (%s and %s)"\n                              % (key, objects[key]["name"], f.get("name")))\n        description = description_of(f.get("mission_info"))\n        if "Horizons:" in description:\n            raise ExportError("%s: its description still says \'Horizons:\' "\n                              "after the opening is removed" % key)\n        objects[key] = {\n            "name": f.get("name"),\n            "horizons_id": None if f.get("id") is None else str(f["id"]),\n            "id_type": f.get("id_type"),\n            "description": description or None,\n            "info_url": f.get("mission_url"),\n        }\n        found = NUMBER.findall(description)\n        if found:\n            numbers[key] = found\n    return {\n        "schema": SCHEMA,\n        "source_sha256": source_sha256(text.encode("utf-8")),\n        "objects": objects,\n        "numbers": numbers,\n    }\n\n\ndef render(export):\n    return json.dumps(export, indent=2, ensure_ascii=True,\n                      sort_keys=False) + "\\n"\n\n\ndef main():\n    root = os.path.dirname(os.path.abspath(__file__))\n    with open(os.path.join(root, SOURCE), "rb") as handle:\n        raw = handle.read()\n    try:\n        export = build_export(raw.decode("utf-8").replace("\\r\\n", "\\n"))\n    except ExportError as exc:\n        print("FAIL: %s. NOTHING was written." % exc)\n        return 1\n    target = os.path.join(root, TARGET)\n    content = render(export)\n    old = None\n    if os.path.exists(target):\n        with open(target, "r", encoding="utf-8", newline="") as handle:\n            old = handle.read()\n    keys = list(export["objects"])\n    if old == content:\n        print("Objects export unchanged: %d keyed entries (%s)."\n              % (len(keys), ", ".join(keys)))\n    else:\n        with open(target, "w", encoding="utf-8", newline="") as handle:\n            handle.write(content)\n        print("Objects export written to %s: %d keyed entries (%s)."\n              % (TARGET.replace(os.sep, "/"), len(keys), ", ".join(keys)))\n    if export["numbers"]:\n        print("Numbers in exported descriptions, each to be sourced or "\n              "removed: %s." % "; ".join(\n                  "%s: %s" % (k, ", ".join(v))\n                  for k, v in export["numbers"].items()))\n    else:\n        print("Numbers in exported descriptions: none.")\n    return 0\n\n\nif __name__ == "__main__":\n    sys.exit(main())\n', 'test_objects_export.py': '"""\ntest_objects_export.py -- data/objects_export.json says what the object\nlist in celestial_objects.py holds, and no entry in the list writes a\nfield twice.\n\nWHY THIS EXISTS\n    The gallery takes each served object\'s name, Horizons id,\n    description and NASA link from data/objects_export.json (L-395). If\n    the list moves and the export does not, the website serves the old\n    words under a green run. And a Python dict literal that writes a\n    field twice keeps only the second, silently: Tony found and removed\n    such repeats by hand in September 2026, and nothing stopped the next\n    one.\n\nRUN COMMAND\n    python test_objects_export.py\n\n    Open it in VS Code and click Run. orrery_maintenance_run.py runs it\n    among the checkers.\n\nWHAT IT CHECKS\n    1. Every entry in OBJECT_DEFINITIONS, all of them and not only the\n       keyed ones, writes each field once.\n    2. The export exists, was made from the list as it is now (its\n       source_sha256), and equals what export_objects.py would write\n       today, entry by entry.\n    3. Each exported description is free of the "Horizons:" opening.\n    It prints how many entries it scanned, the keys it compared, and\n    every number in an exported description by key, so a pass names\n    what it looked at.\n\n    Before any of that it shows that checks 1 and 2 can fail: it feeds a\n    list with a repeated field and an export with one changed word, and\n    each must be refused. If either is not, the run fails.\n\nWHAT MAKES IT FAIL\n    - a field written twice in any entry\n    - the export is missing, is not JSON, or is stale\n    - any exported entry differs from what the list gives now\n    - the self-test did not produce the refusals it must\n\nRole: devtool\nDomain: dev_tools\n\nModule created: October 1, 2026 with Anthropic\'s Claude Opus 5.5\n(L-395, the first build).\n"""\n\nimport json\nimport os\nimport sys\n\nimport export_objects as ex\n\n\nSELF_TEST_LIST = (\n    "OBJECT_DEFINITIONS = [\\n"\n    "    {\'name\': \'Mars\', \'key\': \'mars\', \'id\': \'499\',\\n"\n    "     \'mission_info\': \'Horizons: 499. Red.\', \'id\': \'4\'},\\n"\n    "]\\n")\n\n\ndef self_test():\n    """[problems] -- each refusal this check depends on, shown to happen."""\n    problems = []\n    try:\n        ex.build_export(SELF_TEST_LIST)\n        problems.append("a list writing \'id\' twice was not refused")\n    except ex.ExportError as exc:\n        if "\'id\' 2 times" not in str(exc):\n            problems.append("the repeated field was refused for the wrong "\n                            "reason: %s" % exc)\n    good = SELF_TEST_LIST.replace(", \'id\': \'4\'}", "}")\n    export = ex.build_export(good)\n    if export["objects"]["mars"]["description"] != "Red.":\n        problems.append("the \'Horizons:\' opening was not removed")\n    altered = json.loads(json.dumps(export))\n    altered["objects"]["mars"]["description"] = "Blue."\n    if not differences(altered, export):\n        problems.append("a changed description was not noticed")\n    return problems\n\n\ndef differences(held, fresh):\n    """[text] naming every way the held export differs from a fresh one."""\n    out = []\n    if held.get("schema") != fresh["schema"]:\n        out.append("schema %r, expected %r" % (held.get("schema"),\n                                                fresh["schema"]))\n    if held.get("source_sha256") != fresh["source_sha256"]:\n        out.append("made from an older %s (run export_objects.py)"\n                   % ex.SOURCE)\n    held_objects = held.get("objects") or {}\n    for key in fresh["objects"]:\n        if key not in held_objects:\n            out.append("%s: missing from the export" % key)\n            continue\n        for field, value in fresh["objects"][key].items():\n            if held_objects[key].get(field) != value:\n                out.append("%s.%s: export has %r, the list gives %r"\n                           % (key, field, held_objects[key].get(field),\n                              value))\n    for key in held_objects:\n        if key not in fresh["objects"]:\n            out.append("%s: in the export but no entry has that key" % key)\n    if held.get("numbers") != fresh["numbers"]:\n        out.append("the numbers list differs from the descriptions")\n    return out\n\n\ndef main():\n    root = os.path.dirname(os.path.abspath(__file__))\n    failures = self_test()\n    if failures:\n        print("SELF-TEST FAILED -- the checks below could not fail, so a "\n              "pass would mean nothing:")\n        for f in failures:\n            print("  - " + f)\n        return 1\n\n    with open(os.path.join(root, ex.SOURCE), "rb") as handle:\n        text = handle.read().decode("utf-8").replace("\\r\\n", "\\n")\n    list_node = ex.definitions(text)\n    scanned = len(list_node.elts)\n    repeats = ex.repeated_fields(list_node)\n    for label, field, lines in repeats:\n        failures.append("%s writes \'%s\' %d times (lines %s)"\n                        % (label, field, len(lines),\n                           ", ".join(map(str, lines))))\n    fresh = None\n    if not repeats:\n        try:\n            fresh = ex.build_export(text)\n        except ex.ExportError as exc:\n            failures.append(str(exc))\n\n    target = os.path.join(root, ex.TARGET)\n    held = None\n    if not os.path.exists(target):\n        failures.append("%s is missing (run export_objects.py)"\n                        % ex.TARGET.replace(os.sep, "/"))\n    else:\n        try:\n            with open(target, "r", encoding="utf-8") as handle:\n                held = json.load(handle)\n        except ValueError as exc:\n            failures.append("%s is not JSON: %s" % (ex.TARGET, exc))\n    if held is not None and fresh is not None:\n        failures.extend(differences(held, fresh))\n\n    print("Self-test: a repeated field and a changed word were each refused.")\n    print("Scanned %d entries in OBJECT_DEFINITIONS for repeated fields: "\n          "%d found." % (scanned, len(repeats)))\n    if fresh is not None:\n        keys = list(fresh["objects"])\n        print("Compared %d keyed entries with the export: %s."\n              % (len(keys), ", ".join(keys)))\n        if fresh["numbers"]:\n            print("Numbers in exported descriptions: %s." % "; ".join(\n                "%s: %s" % (k, ", ".join(v))\n                for k, v in fresh["numbers"].items()))\n        else:\n            print("Numbers in exported descriptions: none.")\n    if failures:\n        print("FAILURES (%d):" % len(failures))\n        for f in failures:\n            print("  - " + f)\n        print("OBJECTS EXPORT: FAIL")\n        return 1\n    print("OBJECTS EXPORT: pass")\n    return 0\n\n\nif __name__ == "__main__":\n    sys.exit(main())\n'}, 'CEL': [("    {'name': 'Sun', 'id': '10',", "    {'name': 'Sun', 'key': 'sun', 'id': '10',", "key 'sun' on Sun"), ("    {'name': 'Mercury', 'id': '199',", "    {'name': 'Mercury', 'key': 'mercury', 'id': '199',", "key 'mercury' on Mercury"), ("    {'name': 'Venus', 'id': '299',", "    {'name': 'Venus', 'key': 'venus', 'id': '299',", "key 'venus' on Venus"), ("    {'name': 'Earth', 'id': '399',", "    {'name': 'Earth', 'key': 'earth', 'id': '399',", "key 'earth' on Earth"), ("    {'name': 'Mars', 'id': '499',", "    {'name': 'Mars', 'key': 'mars', 'id': '499',", "key 'mars' on Mars"), ("    {'name': 'Jupiter', 'id': '599',", "    {'name': 'Jupiter', 'key': 'jupiter', 'id': '599',", "key 'jupiter' on Jupiter"), ("    {'name': 'Saturn', 'id': '699',", "    {'name': 'Saturn', 'key': 'saturn', 'id': '699',", "key 'saturn' on Saturn"), ("    {'name': 'Uranus', 'id': '799',", "    {'name': 'Uranus', 'key': 'uranus', 'id': '799',", "key 'uranus' on Uranus"), ("    {'name': 'Neptune', 'id': '899',", "    {'name': 'Neptune', 'key': 'neptune', 'id': '899',", "key 'neptune' on Neptune"), ("    {'name': 'Pluto-Charon Barycenter', 'id': '9',", "    {'name': 'Pluto-Charon Barycenter', 'key': 'pluto_barycenter', 'id': '9',", "key 'pluto_barycenter' on Pluto-Charon Barycenter"), ("    {'name': 'Apophis', 'id': '2004 MN4',", "    {'name': 'Apophis', 'key': 'apophis', 'id': '2004 MN4',", "key 'apophis' on Apophis"), ("     'mission_info': 'Center of mass for Pluto-Charon binary planet system. System period: 6.39 days.'},\n", "     'mission_info': 'Center of mass for Pluto-Charon binary planet system.',\n     'mission_url': 'https://science.nasa.gov/dwarf-planets/pluto/'},\n", "Pluto-Charon Barycenter: unsourced period removed; links to NASA's Pluto page"), ('keeping everything in its orbit. "\', \n', 'keeping everything in its orbit."\', \n', 'Sun: stray space inside the closing quote removed'), ("in 2029. Future OSIRIS-APEX target', \n", "in 2029. Future OSIRIS-APEX target.', \n", 'Apophis: closing full stop added')], 'OPTIONAL': [("    'mission_url': 'https://science.nasa.gov/?search=mars'},\n", "    'mission_url': 'https://science.nasa.gov/mars/'},\n", 'Mars links to science.nasa.gov/mars/'), ("    'mission_url': 'https://science.nasa.gov/?search=Jupiter'},\n", "    'mission_url': 'https://science.nasa.gov/jupiter/'},\n", 'Jupiter links to science.nasa.gov/jupiter/')], 'RUN': [("    ('Constants export', ['export_constants.py'],\n     ['data/constants_export.json']),\n", "    ('Constants export', ['export_constants.py'],\n     ['data/constants_export.json']),\n    # L-395 (2026-10-01): the orrery's object list is the one definition\n    # of each object the website serves. The entries carrying a 'key'\n    # are exported, and the gallery pulls the file as it pulls the\n    # constants export.\n    ('Objects export', ['export_objects.py'],\n     ['data/objects_export.json']),\n", 'GENERATORS: Objects export'), ("    ('Constants export check', ['test_constants_export.py'], None),\n", "    ('Constants export check', ['test_constants_export.py'], None),\n    # L-395: the objects export matches the list it was made from, and\n    # no entry in the list writes a field twice. It names every number\n    # in an exported description.\n    ('Objects export check', ['test_objects_export.py'],\n     'OBJECTS EXPORT:'),\n", 'CHECKERS: Objects export check')], 'README': [("    'id_type': 'majorbody',\n    ...\n}\n```\n\n### JPL Horizons ID Types and Coverage\n", "    'id_type': 'majorbody',\n    ...\n}\n```\n\n**Note, October 1, 2026 (L-395).** `celestial_objects.py` now gives Haumea\n`'id': '920136108'` and `'center_id': '920136108'`: Haumea itself, the main\nbody of its moon system (JPL's binary convention: 20XXXXXX is the system\nbarycenter, 920XXXXXX the primary, 120XXXXXX the secondary). The examples in\nthis README give the barycenter id, `20136108`, as the design was first\nwritten, and the coverage figures below were recorded for the barycenter\nids. `helio_id` is unchanged and is still what Sun-centered views fetch.\n\n### JPL Horizons ID Types and Coverage\n", 'dated note: the code now uses 920136108, Haumea itself')]}

BASE = {
    'celestial_objects.py': ('0cfcd7da45062cbb9c7ce0ce217303f3',
                             'f3e93c8fa540c8b4d4b369def5a59e49'),
    'orrery_maintenance_run.py': ('1cedd94d10b0cf9b7471fc81aac3d71c',),
    'documentation/ORBITAL_MECHANICS_README_v1_4.md':
        ('3824dc1c1fd31691ffc4bf6d63f68b8c',),
}


def fingerprint(raw):
    return hashlib.md5(raw.replace(b"\r\n", b"\n")).hexdigest()


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the ORRERY repo ROOT, next to "
                         "palomas_orrery.py -- not from documentation/. "
                         "NOTHING was written.")
    if not os.path.isfile("palomas_orrery.py"):
        raise SystemExit("ERROR: palomas_orrery.py is not here, so this is "
                         "not the orrery root. NOTHING was written.")
    for path in SPEC['NEW']:
        if os.path.exists(path):
            raise SystemExit("ERROR: %s already exists. If you already ran "
                             "this patch, it has nothing left to do. NOTHING "
                             "was written." % path)

    plan = {'celestial_objects.py': SPEC['CEL'],
            'orrery_maintenance_run.py': SPEC['RUN'],
            'documentation/ORBITAL_MECHANICS_README_v1_4.md': SPEC['README']}
    results = []
    for path, edits in sorted(plan.items()):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is missing. NOTHING was written." % path)
        with open(path, "rb") as handle:
            raw = handle.read()
        got = fingerprint(raw)
        if got not in BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written. Undo is Discard Changes in\n"
                "       GitHub Desktop." % (path, " or ".join(BASE[path]), got))
        nl = "\r\n" if raw.count(b"\r\n") > 0 else "\n"
        text = raw.decode("utf-8")
        done = []
        todo = list(edits)
        if path == 'celestial_objects.py':
            for old, new, label in SPEC['OPTIONAL']:
                if text.count(old.replace("\n", nl)) == 1:
                    todo.append((old, new, label))
                else:
                    done.append(label + " (already done)")
        for old, new, label in todo:
            o = old.replace("\n", nl)
            n = new.replace("\n", nl)
            count = text.count(o)
            if count != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. NOTHING was written."
                                 % (label, path, count))
            text = text.replace(o, n)
            done.append(label)
        # Code stays ASCII. A document keeps the symbols it already
        # holds (the README's omega and degree signs); this patch only
        # refuses to ADD any.
        added = (sum(1 for ch in text if ord(ch) > 127)
                 - sum(1 for ch in raw.decode("utf-8") if ord(ch) > 127))
        if (path.endswith(".py") and any(ord(ch) > 127 for ch in text)) \
                or added > 0:
            raise SystemExit("ERROR: %s would hold new non-ASCII text. "
                             "NOTHING was written." % path)
        results.append((path, text, done))

    for path, text, done in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s" % (path.split('/')[-1], label))
    for path, content in sorted(SPEC['NEW'].items()):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        print("ok  %-30s created" % path)

    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. python orrery_maintenance_run.py -- its new Objects export")
    print("     writes data/objects_export.json, and Objects export check")
    print("     should read: OBJECTS EXPORT: pass")
    print("  2. Move this script into documentation/ (and the small Mars and")
    print("     Jupiter patch, run or not).")
    print("  3. Commit and push. The gallery patch pulls the export from the")
    print("     orrery's pushed state, so this push comes first.")


if __name__ == "__main__":
    main()
