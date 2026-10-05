#!/usr/bin/env python3
"""
patch_L416_1_dashboard_buttons_20261005.py -- ORRERY repo. Every step of
the two maintenance runs gets a dashboard button (L-416, Tony's approval
of 2026-10-05).

Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 624aa94557e16956b2fe022a467936ae2ccf3406 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io; its half
is patch_L416_2, which adds the wrapper seven of these buttons run).

It touches only palomas_orrery_dashboard.py, so it can run before or
after patch_L413_2_earth_orrery_20261005.py; neither changes the other's
file.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L416_1_dashboard_buttons_20261005.py
    Then follow the numbered NEXT steps it prints.

WHAT YOU SEE AFTER IT, ON THE DASHBOARD
    Under the Maintenance Run's checkers, in alphabetical place:
        Test Skill Headers      skills_index.py --check (L-407)
    Under Gallery -- checks and data, in alphabetical place:
        Arrival                 } Node checks, run through the gallery's
        Display Figures         } documentation/run_offline_check.py,
        Earth Scene Geometry    } which reads each command from the
        Feature Renderers       } gallery runner's own list, so the
        Page Framing            } button and the runner cannot drift
        Solar System Drawer     }
        Sun Shells              }
        Pole of Date            tools/test_pole_of_date.py
        Daily Run Steps         daily_run.py --check
        Gallery Module Atlas    the gallery's own module_atlas.py
    The offline runner's description now names the Solar System drawer,
    which it had left out, and says every checker it names has its own
    button.
    Seven of these were the ones Claude named; Daily Run Steps and the
    gallery's module atlas were missed in that count and found when the
    match was rerun against both runners' own lists.

TESTED in a sandbox with both repos side by side: the dashboard loads
and draws; all 92 buttons find their scripts; every step of both runners
now has a button (the three older wrappers cover hover budget, Solar
System figures and the guest book); each Node check run through the
wrapper passes, and one made to fail reports FAILED with its exit code.

LINE ENDINGS (safe-file-editing 1.12): written LF; a CRLF working copy
is named in a "note:" line. The file is committed LF.

PERMANENT, though this script is thrown away: the eleven buttons.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
BUILT_ON = "72e3b55"
NEXT = ["1. Move this script into documentation/ before any maintenance",
        "   run: in the root folder the provenance scanner counts it.",
        "2. Open the dashboard and look: the eleven new buttons, each in",
        "   alphabetical place. The seven Node ones work once the gallery",
        "   patch, patch_L416_2, has run; before that each reports the",
        "   missing wrapper.",
        "3. Commit and push, with the Earth patch or on its own."]

BASE = {'palomas_orrery_dashboard.py': '1d9116405a723850523932686c4d4f0f'}

EDITS = {
  'palomas_orrery_dashboard.py': [
    ('Arrival',
      '        ("Artifact 1 Assembler Pin",\n',
      ('        ("Arrival",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "Both rooms open on the right things (L-334). Builds the Sun "\n'
      '        "room\'s shells and the Earth room\'s scene with the real "\n'
      '        "renderers, applies gallery/arrival.js with the real "\n'
      '        "data/objects_config.json, and compares what is drawn on "\n'
      '        "opening against its list; it also fails on any trace with no "\n'
      '        "shell key. It first makes itself fail on purpose four ways. "\n'
      '        "GATES the gallery runner. The check is Node, so this button "\n'
      '        "runs it through documentation/run_offline_check.py, which "\n'
      '        "reads its command from the gallery runner\'s own list: the two "\n'
      '        "cannot drift. Runs from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Arrival"],\n'
      '        True),\n'
      '        ("Artifact 1 Assembler Pin",\n'),
      1),
    ('Daily Run Steps, Display Figures, Earth Scene Geometry, Feature Renderers',
      '        ("Gallery Builder Offline Tests",\n',
      ('        ("Daily Run Steps",\n'
      '        "daily_run.py",\n'
      '        "daily_run.py --check: fails if any of the three scripts the "\n'
      '        "Daily Run calls is missing, say after a rename, and names it. "\n'
      '        "Runs nothing else. GATES the gallery runner.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["--check"],\n'
      '        True),\n'
      '        ("Display Figures",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "Every number in an Earth hover shows the figures its source "\n'
      '        "supports (L-342). Reads the BUILT hovers from the served "\n'
      '        "cache, not the formatting helpers, and fails on any number it "\n'
      '        "cannot account for, or if the config and the cache would print "\n'
      '        "differently. GATES the gallery runner. The check is Node, so "\n'
      '        "this button runs it through "\n'
      '        "documentation/run_offline_check.py, which reads its command "\n'
      '        "from the gallery runner\'s own list: the two cannot drift. Runs "\n'
      '        "from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Display figures"],\n'
      '        True),\n'
      '        ("Earth Scene Geometry",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "The Earth room\'s composed scene, headless, on the recorded "\n'
      '        "payload documentation/payload_earth_scene.json: the axis tilt "\n'
      '        "against the served pole of date, the equator and geostationary "\n'
      '        "ring in one plane, the terminator, the subsolar point, the "\n'
      '        "Moon\'s arc and what the room opens on. Every number compared "\n'
      '        "is read from the served rows. GATES the gallery runner. The "\n'
      '        "check is Node, so this button runs it through "\n'
      '        "documentation/run_offline_check.py, which reads its command "\n'
      '        "from the gallery runner\'s own list: the two cannot drift. Runs "\n'
      '        "from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Earth scene geometry"],\n'
      '        True),\n'
      '        ("Feature Renderers",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "Smoke test for gallery/feature_renderers.js, the code that "\n'
      '        "draws every shell, ring, belt and magnetosphere on the "\n'
      '        "website. The geometry checks measure the drawn points, not the "\n'
      '        "inputs, so a wrong answer fails. GATES the gallery runner. The "\n'
      '        "check is Node, so this button runs it through "\n'
      '        "documentation/run_offline_check.py, which reads its command "\n'
      '        "from the gallery runner\'s own list: the two cannot drift. Runs "\n'
      '        "from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Feature renderers"],\n'
      '        True),\n'
      '        ("Gallery Builder Offline Tests",\n'),
      1),
    ('Gallery Module Atlas',
      '        ("Guest Book Checks",\n',
      ('        ("Gallery Module Atlas",\n'
      '        "module_atlas.py",\n'
      '        "The gallery repo\'s own module atlas: regenerates its "\n'
      '        "MODULE_ATLAS.md and MODULE_INDEX.md. The gallery runner does "\n'
      '        "this first on every run, as a generator. Not the orrery\'s "\n'
      '        "atlas, which has its own button under the maintenance run.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        None,\n'
      '        True),\n'
      '        ("Guest Book Checks",\n'),
      1),
    ('Page Framing',
      '        ("Pointer Join",\n',
      ('        ("Page Framing",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "The page\'s own framing helpers, taken out of the page and run "\n'
      '        "against real feature traces; the checks measure the axis "\n'
      '        "ranges that result, so a wrong range fails. GATES the gallery "\n'
      '        "runner. The check is Node, so this button runs it through "\n'
      '        "documentation/run_offline_check.py, which reads its command "\n'
      '        "from the gallery runner\'s own list: the two cannot drift. Runs "\n'
      '        "from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Page framing"],\n'
      '        True),\n'
      '        ("Pointer Join",\n'),
      1),
    ('Pole of Date, Solar System Drawer',
      '        ("Solar System Figures",\n',
      ('        ("Pole of Date",\n'
      '        os.path.join("tools", "test_pole_of_date.py"),\n'
      '        "Holds the cache builder\'s copy of the orrery\'s tilt geometry "\n'
      '        "(tools/pole_of_date.py) to the frame angle in the constants "\n'
      '        "export, to the orrery\'s own results on two real Horizons days, "\n'
      '        "and to ERFA, the IAU\'s routines; then reruns each check with "\n'
      '        "one input altered, where it must fail. Needs astropy. GATES "\n'
      '        "the gallery runner. Runs from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        None,\n'
      '        True),\n'
      '        ("Solar System Drawer",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "The Solar System room\'s drawer does what Tony\'s design says "\n'
      '        "(L-363): worked cases on the real "\n'
      '        "gallery/solar_system_drawer.js, the real "\n'
      '        "data/objects_config.json\'s rows, and interactive.html loading "\n'
      '        "the file and calling each function it must. GATES the gallery "\n'
      '        "runner. The check is Node, so this button runs it through "\n'
      '        "documentation/run_offline_check.py, which reads its command "\n'
      '        "from the gallery runner\'s own list: the two cannot drift. Runs "\n'
      '        "from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Solar System drawer"],\n'
      '        True),\n'
      '        ("Solar System Figures",\n'),
      1),
    ('Sun Shells',
      '        ("Gallery Maintenance Run -- live, AFTER a push",\n',
      ('        ("Sun Shells",\n'
      '        os.path.join("documentation", "run_offline_check.py"),\n'
      '        "The Sun room\'s shells, built by the real renderers from the "\n'
      '        "real data/objects_config.json: no input left unread, the "\n'
      '        "expected geometry traces, and the shapes that must be thinned "\n'
      '        "or tilted measured where they are drawn. GATES the gallery "\n'
      '        "runner. The check is Node, so this button runs it through "\n'
      '        "documentation/run_offline_check.py, which reads its command "\n'
      '        "from the gallery runner\'s own list: the two cannot drift. Runs "\n'
      '        "from the gallery repo ROOT.",\n'
      '        GALLERY_REPO_DIR,\n'
      '        True,\n'
      '        ["Sun shells"],\n'
      '        True),\n'
      '        ("Gallery Maintenance Run -- live, AFTER a push",\n'),
      1),
    ('Test Skill Headers',
      '        ("Test Status Lines",\n',
      ('        ("Test Skill Headers",\n'
      '         "skills_index.py",\n'
      '         "skills_index.py --check: reads every skill\'s header as YAML, "\n'
      '         "the way Settings > Skills does, and fails on a header YAML "\n'
      '         "refuses, a name or description that is not text, or a value "\n'
      '         "YAML would cut short at a space before a # (L-407). The Update "\n'
      '         "Skill Manifest button runs the same script without the check, "\n'
      '         "and writes the protocol\'s table.",\n'
      '         SCRIPT_DIR,\n'
      '         True,\n'
      '         ["--check"],\n'
      '         True),\n'
      '        ("Test Status Lines",\n'),
      1),
    ("offline runner's description: the drawer, and every check has a button",
      ('        "hover budget, arrival, display figures, Solar System figures, "\n'
      '        "and the guest book. "\n'),
      ('        "hover budget, arrival, display figures, Solar System figures, "\n'
      '        "the Solar System drawer, and the guest book. "\n'),
      1),
    ("offline runner's description: last sentence",
      ('        "as a pass. The indented buttons below launch some of these "\n'
      '        "one at a time.",\n'),
      ('        "as a pass. Every checker named here also has its own indented "\n'
      '        "button below, to run it alone.",\n'),
      1),
    ('docstring credit',
      ('Objects Mirror Suite, each in alphabetical place.\n'
      '"""\n'),
      ('Objects Mirror Suite, each in alphabetical place.\n'
      "October 5, 2026 with Anthropic's Claude Opus 5.5 (L-416), on Tony's\n"
      'question and approval: every step of the two maintenance runs now has\n'
      "a button. Added in alphabetical place, under the orrery's checkers,\n"
      'Test Skill Headers (skills_index.py --check, L-407); and under the\n'
      'gallery checks Arrival, Daily Run Steps, Display Figures, Earth Scene\n'
      'Geometry, Feature Renderers, Gallery Module Atlas, Page Framing, Pole\n'
      'of Date, Solar System Drawer and Sun Shells. The seven Node checks run\n'
      "through the gallery's documentation/run_offline_check.py, which reads\n"
      "each command from the gallery runner's own list. The offline runner's\n"
      'description names the Solar System drawer, which it had left out.\n'
      '"""\n'),
      1),
  ],
}


def fingerprint(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def non_ascii(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    results = []
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        got = fingerprint(text)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       %s, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got, BUILT_ON))
        before = non_ascii(text)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        if non_ascii(text) > before:
            raise SystemExit("ERROR: %s would gain non-ASCII characters. "
                             "NOTHING was written." % path)
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
