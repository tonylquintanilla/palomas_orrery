"""patch_L395_5_horizons_name_and_encke_20261010.py -- the orrery half of
the Horizons check (L-395): JPL's exact name on each keyed entry, Halley
keyed, Encke's own entry, and the export that carries them.

Built on orrery ca5bbe12cb8f1c48b134f6aadaa700d45ae9e39d at
https://github.com/tonylquintanilla/palomas_orrery ("L427 records"), with
gallery 050637c3688e1bfcff81848ad4780b8a9e975a9e at
https://github.com/tonylquintanilla/tonyquintanilla.github.io pinned
beside it. Written October 10, 2026 with Anthropic's Claude Opus 5.5,
from documentation/HANDOFF_L395_horizons_check_build_brief_20261010.md.

HOW TO RUN
    Save this file in the orrery repo's ROOT folder (the folder that
    holds celestial_objects.py). Open it in VS Code and press Run. Or,
    from a terminal in that folder:
        python patch_L395_5_horizons_name_and_encke_20261010.py
    Success prints one "ok" line per edit, then "patch applied".
    Then run orrery_maintenance_run.py: it rewrites
    data/objects_export.json with thirteen keyed entries. Move this
    script into documentation/, commit and push.

WHAT IT CHANGES
    celestial_objects.py
        - 'horizons_name', JPL's exact name, on the eleven keyed entries
          and on Halley and Encke: Sun, Mercury, Venus, Earth, Mars,
          Jupiter, Saturn, Uranus, Neptune, "Pluto Barycenter",
          "99942 Apophis", "1P/Halley", "2P/Encke". 'name' is untouched.
        - Halley: 'key' "halley"; the words Tony approved on 2026-10-08;
          the link moves to NASA's 1P/Halley page.
        - Encke: a new entry, record 90000091, after Halley's.
        - the docstring: what the two new fields are, the count, a stamp.
    palomas_orrery.py
        - comet_encke_var and an "Encke" checkbox under Halley's, so the
          new entry can be selected in the window. Stamp.
    info_dictionary.py
        - INFO['Encke'], the checkbox's tooltip, in Tony's words. Stamp.
        - fixed in passing: the two non-ASCII letters in the file, both
          the s-acute of "Wierzchos" in Comet Wierzchos's tooltip, are
          written as a plain s (the ASCII rule).
    export_objects.py
        - each exported object carries horizons_name and object_type
          (the gallery's check compares object_type for the barycentre
          and the Sun); a keyed entry without a horizons_name is refused
          and nothing is written. Docstring and stamp.
    test_objects_export.py
        - its self-test plants an entry with a key and no horizons_name,
          and must see it refused, before it trusts a pass. It prints
          each keyed entry's horizons_name. Docstring and stamp.

    Encke draws in the default colour (goldenrod): constants_new.py has
    no 'Encke' colour, and this patch does not touch the store.

SAFETY
    Each file is checked only at the lines this patch edits: every
    anchor must match exactly once. If any check fails, NOTHING is
    written. A file found with Windows line endings is matched after
    turning them into LF and written back LF, and the patch says so.
    Undo after a run is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

EDITS = {}


def add(fname, label, old, new, count=1):
    # <SP> and <SP6> stand for trailing spaces in the target file, which an
    # editor may strip from this script; they are put back here.
    old, new = [t.replace(b"<SP6>", b" " * 6).replace(b"<SP>", b" ")
                for t in (old, new)]
    EDITS.setdefault(fname, []).append((label, old, new, count))


# ============================================================ celestial_objects.py
CO = "celestial_objects.py"

add(CO, "docstring: the two fields, the count",
b"""Master catalog of ~179 objects queried from JPL Horizons. Each entry is a
dict carrying the Horizons ID, object type, display symbol, hover text, and
URL. Separated from the GUI so palomas_orrery.py stays clean.""",
b"""Master catalog of 183 objects queried from JPL Horizons. Each entry is a
dict carrying the Horizons ID, object type, display symbol, hover text, and
URL. An entry the website serves also carries 'key', the website's name
for it (export_objects.py writes only keyed entries), and 'horizons_name',
JPL's exact name for the object, which nothing in the orrery reads: the
gallery's Horizons check compares it with JPL's answer (L-395). 'name'
stays the orrery's own choice. Separated from the GUI so palomas_orrery.py
stays clean.""")

add(CO, "docstring: stamp",
b"""Module updated: April 2026 with Anthropic's Claude Sonnet 4.6 with Gemini 3.5 Pro review
""",
b"""Module updated: April 2026 with Anthropic's Claude Sonnet 4.6 with Gemini 3.5 Pro review
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395,
the Horizons check: 'horizons_name' on the thirteen keyed entries; Halley
keyed, with Tony's words of 2026-10-08 and NASA's 1P/Halley page; Encke's
own entry, record 90000091, which until now only the website defined).
""")

for name, key, hid, hname in (
        ("Sun", "sun", "10", "Sun"),
        ("Mercury", "mercury", "199", "Mercury"),
        ("Venus", "venus", "299", "Venus"),
        ("Earth", "earth", "399", "Earth"),
        ("Mars", "mars", "499", "Mars"),
        ("Jupiter", "jupiter", "599", "Jupiter"),
        ("Saturn", "saturn", "699", "Saturn"),
        ("Uranus", "uranus", "799", "Uranus"),
        ("Neptune", "neptune", "899", "Neptune"),
        ("Pluto-Charon Barycenter", "pluto_barycenter", "9",
         "Pluto Barycenter"),
        ("Apophis", "apophis", "2004 MN4", "99942 Apophis")):
    head = "{'name': '%s', 'key': '%s', 'id': '%s', " % (name, key, hid)
    add(CO, "horizons_name %s" % name,
        (head + "'var_name'").encode("ascii"),
        (head + "'horizons_name': '%s', 'var_name'" % hname).encode("ascii"))

add(CO, "Halley keyed, words and link",
b"""    {'name': 'Halley', 'id': '90000030', 'var_name': 'comet_halley_var', 'color_key': 'Halley', 'symbol': 'diamond',
    'object_type': 'orbital', 'id_type': 'smallbody',<SP>
    #'start_date': datetime(1900, 1, 1), 'end_date': datetime(1994, 1, 11),<SP>
    # data arc: 1835-08-21 to 1994-01-11; 1P/Halley requires the record number to fetch position data for the 1986 apparition.
    'mission_info': 'Horizons: 1P/Halley. Retrograde. Most famous comet, returned in 1986 and will return in 2061. Retrograde (left-handed) orbit.',<SP>
    'mission_url': 'https://sites.google.com/view/tony-quintanilla/comets/halley-1986'},
""",
b"""    {'name': 'Halley', 'key': 'halley', 'id': '90000030', 'horizons_name': '1P/Halley', 'var_name': 'comet_halley_var', 'color_key': 'Halley', 'symbol': 'diamond',
    'object_type': 'orbital', 'id_type': 'smallbody',<SP>
    #'start_date': datetime(1900, 1, 1), 'end_date': datetime(1994, 1, 11),<SP>
    # data arc: 1835-08-21 to 1994-01-11; 1P/Halley requires the record number to fetch position data for the 1986 apparition.
    # Pinned record: the newest of 30 Horizons records for 1P (L-395; documentation/HORIZONS_ANSWERS_L395_20261007.md, G1 and G2).
    # The gallery's Horizons check reports a newer record for a person to decide; it never re-pins.
    # Words and link, Tony 2026-10-08: no numbers unless they come from the store; NASA's page (L-395).
    'mission_info': 'Horizons: 1P/Halley. The most famous periodic comet. Its orbit runs backward compared with the planets, and its dust gives two meteor showers each year, the Eta Aquarids and the Orionids.',<SP>
    'mission_url': 'https://science.nasa.gov/solar-system/comets/1p-halley/'},

    {'name': 'Encke', 'key': 'encke', 'id': '90000091', 'horizons_name': '2P/Encke', 'var_name': 'comet_encke_var', 'color_key': 'Encke', 'symbol': 'diamond',
    'object_type': 'orbital', 'id_type': 'smallbody',
    # Pinned record: 90000091, the 2023 apparition, the newest of 61 Horizons records for 2P; '2P' alone is
    # ambiguous (L-395; documentation/HORIZONS_ANSWERS_L395_20261007.md, G3 and G4). JPL re-solves the record
    # in place; the gallery's Horizons check reports a newer record for a person to decide; it never re-pins.
    # Added 2026-10-10 (L-395): the website served Encke before this list held it. Words and link, Tony 2026-10-08.
    'mission_info': 'Horizons: 2P/Encke. A short-period comet whose dust trail is the source of the Taurid meteor showers.',
    'mission_url': 'https://science.nasa.gov/solar-system/comets/2p-encke/'},
""")

# ============================================================ palomas_orrery.py
PO = "palomas_orrery.py"

add(PO, "stamp",
b"""each circle in star_sphere_builder.py. Words approved by Tony,
2026-10-06.)

\"\"\"""",
b"""each circle in star_sphere_builder.py. Words approved by Tony,
2026-10-06.)
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395:
an "Encke" checkbox under Halley's, for the list's new Encke entry,
record 90000091; its tooltip dates come from JPL's answers of
2026-10-07.)

\"\"\"""")

add(PO, "comet_encke_var",
b"""comet_halley_var = tk.IntVar(value=0)
""",
b"""comet_halley_var = tk.IntVar(value=0)

comet_encke_var = tk.IntVar(value=0)
""")

add(PO, "Encke checkbox",
b"""create_comet_checkbutton("Halley", comet_halley_var, "(1900-1-1 to 1994-1-11)",<SP6>
                         # data arc: 1835-08-21 to 1994-01-11
                         "February 8, 1986")    # 1986-Feb-08.1983372075
""",
b"""create_comet_checkbutton("Halley", comet_halley_var, "(1900-1-1 to 1994-1-11)",<SP6>
                         # data arc: 1835-08-21 to 1994-01-11
                         "February 8, 1986")    # 1986-Feb-08.1983372075

create_comet_checkbutton("Encke", comet_encke_var, "(1786-present, periodic)",
                         # 1786: the epoch-year of the first of JPL's 61 records for 2P (L-395, answer G4)
                         "October 22, 2023")    # TP of record 90000091, 2023-Oct-22.53 (L-395, answer G3)
""")

# ============================================================ info_dictionary.py
INF = "info_dictionary.py"

add(INF, "stamp",
b"""Provenance audit identified by Anthropic's Claude Opus 4.7.
\"\"\"""",
b"""Provenance audit identified by Anthropic's Claude Opus 4.7.
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395:
INFO['Encke'] for the list's new Encke entry, in the words Tony approved
on 2026-10-08.)
\"\"\"""")

add(INF, "INFO['Encke']",
b"""        'Schaumasse': '8.25-year period, mag ~9, passed near Jupiter Oct 2025, near Ceres in 2010',
""",
b"""        'Encke': 'Horizons: 2P/Encke. A short-period comet whose dust trail is the source of the Taurid meteor showers.',

        'Schaumasse': '8.25-year period, mag ~9, passed near Jupiter Oct 2025, near Ceres in 2010',
""")

add(INF, "fixed in passing: 'Wierzcho' + s-acute -> 'Wierzchos' (ASCII)",
b"Wierzcho\xc5\x9b", b"Wierzchos", count=2)

# ============================================================ export_objects.py
EX = "export_objects.py"

add(EX, "docstring: what it writes",
b"""                      name         the entry's 'name'
                      horizons_id  the entry's 'id'
""",
b"""                      name         the entry's 'name'
                      horizons_id  the entry's 'id'
                      horizons_name the entry's 'horizons_name', JPL's
                                   exact name for the object. Only the
                                   gallery's Horizons check reads it
                                   (L-395)
                      object_type  the entry's 'object_type'. The check
                                   compares it for "barycenter" and the
                                   Sun's "fixed" only
""")

add(EX, "docstring: what makes it fail",
b"""    - a keyed entry whose name, id, mission_info or mission_url is not a
      plain literal
""",
b"""    - a keyed entry whose name, id, mission_info or mission_url is not a
      plain literal
    - a keyed entry with no 'horizons_name', or one that is not a
      non-empty string: the gallery's Horizons check has nothing to
      compare JPL's name with (L-395)
""")

add(EX, "docstring: stamp",
b"""(L-395, the first build: the Solar System room's eleven bodies take
their names, Horizons ids, descriptions and NASA links from the orrery).
\"\"\"""",
b"""(L-395, the first build: the Solar System room's eleven bodies take
their names, Horizons ids, descriptions and NASA links from the orrery).
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395,
the Horizons check: each object carries horizons_name and object_type,
and a keyed entry without a horizons_name is refused).
\"\"\"""")

add(EX, "FIELDS",
b"""FIELDS = ("name", "id", "id_type", "mission_info", "mission_url")""",
b"""FIELDS = ("name", "id", "id_type", "mission_info", "mission_url",
          "horizons_name", "object_type")""")

add(EX, "refuse a keyed entry without horizons_name",
b"""        description = description_of(f.get("mission_info"))
        if "Horizons:" in description:""",
b"""        horizons_name = f.get("horizons_name")
        if not isinstance(horizons_name, str) or not horizons_name.strip():
            raise ExportError("%s: key '%s' has no horizons_name (JPL's "
                              "exact name, which the gallery's Horizons "
                              "check compares)" % (f.get("name"), key))
        description = description_of(f.get("mission_info"))
        if "Horizons:" in description:""")

add(EX, "export the two fields",
b"""            "horizons_id": None if f.get("id") is None else str(f["id"]),
            "id_type": f.get("id_type"),
""",
b"""            "horizons_id": None if f.get("id") is None else str(f["id"]),
            "horizons_name": horizons_name,
            "id_type": f.get("id_type"),
            "object_type": f.get("object_type"),
""")

# ============================================================ test_objects_export.py
TE = "test_objects_export.py"

add(TE, "docstring: what it checks",
b"""    Before any of that it shows that checks 1 and 2 can fail: it feeds a
    list with a repeated field and an export with one changed word, and
    each must be refused. If either is not, the run fails.
""",
b"""    4. Every keyed entry carries a horizons_name, JPL's exact name, which
       the gallery's Horizons check compares (L-395); the run prints
       each one beside its key.
    Before any of that it shows that checks 1, 2 and 4 can fail: it
    feeds a list with a repeated field, an export with one changed word,
    and a keyed entry with no horizons_name, and each must be refused.
    If any is not, the run fails.
""")

add(TE, "docstring: what makes it fail",
b"""    - any exported entry differs from what the list gives now
""",
b"""    - any exported entry differs from what the list gives now
    - a keyed entry has no horizons_name
""")

add(TE, "docstring: stamp",
b"""Module created: October 1, 2026 with Anthropic's Claude Opus 5.5
(L-395, the first build).
\"\"\"""",
b"""Module created: October 1, 2026 with Anthropic's Claude Opus 5.5
(L-395, the first build).
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5 (L-395,
the Horizons check: a keyed entry without a horizons_name fails, shown
failing on a planted entry first).
\"\"\"""")

add(TE, "self-test list carries horizons_name",
b"""    "    {'name': 'Mars', 'key': 'mars', 'id': '499',\\n"
""",
b"""    "    {'name': 'Mars', 'key': 'mars', 'id': '499', 'horizons_name': 'Mars',\\n"
""")

add(TE, "self-test: a keyed entry without horizons_name",
b"""    altered = json.loads(json.dumps(export))
    altered["objects"]["mars"]["description"] = "Blue."
    if not differences(altered, export):
        problems.append("a changed description was not noticed")
    return problems
""",
b"""    altered = json.loads(json.dumps(export))
    altered["objects"]["mars"]["description"] = "Blue."
    if not differences(altered, export):
        problems.append("a changed description was not noticed")
    nameless = good.replace(" 'horizons_name': 'Mars',", "")
    try:
        ex.build_export(nameless)
        problems.append("a keyed entry with no horizons_name was not "
                        "refused")
    except ex.ExportError as exc:
        if "no horizons_name" not in str(exc):
            problems.append("the entry with no horizons_name was refused "
                            "for the wrong reason: %s" % exc)
    return problems
""")

add(TE, "print line: the self-test",
b"""    print("Self-test: a repeated field and a changed word were each refused.")
""",
b"""    print("Self-test: a repeated field, a changed word and a keyed entry "
          "with no horizons_name were each refused.")
""")

add(TE, "print each horizons_name",
b"""        print("Compared %d keyed entries with the export: %s."
              % (len(keys), ", ".join(keys)))
""",
b"""        print("Compared %d keyed entries with the export: %s."
              % (len(keys), ", ".join(keys)))
        print("JPL names (horizons_name): %s." % "; ".join(
            "%s = %s" % (k, fresh["objects"][k]["horizons_name"])
            for k in keys))
""")


def main():
    if not os.path.exists(os.path.join(ROOT, CO)):
        print("ERROR: %s is not in this folder. Save the patch in the "
              "orrery repo's root folder. NOTHING was written." % CO)
        return 1
    staged = {}
    notes = []
    failures = []
    for fname, edits in EDITS.items():
        path = os.path.join(ROOT, fname)
        raw = open(path, "rb").read()
        was_crlf = b"\r\n" in raw
        text = raw.replace(b"\r\n", b"\n")
        if fname == CO and b"'horizons_name'" in text:
            print("ERROR: %s already carries 'horizons_name'; this patch "
                  "has run. NOTHING was written." % CO)
            return 1
        for label, old, new, count in edits:
            n = text.count(old)
            if n != count:
                failures.append("ANCHOR FAIL %s -- %s: expected %d match, "
                                "found %d" % (fname, label, count, n))
                continue
            try:
                new.decode("ascii")
            except UnicodeDecodeError:
                failures.append("NON-ASCII in the text this patch inserts: "
                                "%s -- %s" % (fname, label))
                continue
            text = text.replace(old, new)
            print("ok  %-24s %s" % (fname, label))
        staged[fname] = text
        if was_crlf:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % fname)
        left = sum(1 for b in text if b > 127)
        if left:
            notes.append("note: %s still holds %d non-ASCII byte(s) this "
                         "patch did not reach" % (fname, left))
    if failures:
        for f in failures:
            print(f)
        print("FAILURE: NOTHING was written. Undo is not needed.")
        return 1
    for fname, text in staged.items():
        with open(os.path.join(ROOT, fname), "wb") as handle:
            handle.write(text)
    for n in notes:
        print(n)
    total = sum(len(e) for e in EDITS.values())
    print("patch applied: %d edits in %d files (%s)."
          % (total, len(staged), ", ".join(staged)))
    print("Next: run orrery_maintenance_run.py. It rewrites "
          "data/objects_export.json; expect 'Objects export written ... "
          "13 keyed entries' and 'OBJECTS EXPORT: pass'.")
    print("Undo is Discard Changes in GitHub Desktop.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
