"""patch_L431_13_dashboard_buttons_20261014.py -- L-431 (orbital periods
from JPL), build 3, its third and last patch: the dashboard's buttons for
the website follow the website's patch.

Built on orrery 5cd63ccea16e5242014f8aeb12cfb4beeb36ea31 at
https://github.com/tonylquintanilla/palomas_orrery ("L431"),
AFTER patch_L431_11_website_orrery_20261014.py, and after
patch_L431_12_website_gallery_20261014.py has run in the gallery
(gallery 77988635526d1dd68f8c082cae39f4b7ad3f56b8 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 14, 2026 with Anthropic's Claude Opus 5.5.
Record: documentation/HANDOFF_L431_build3_website_20261014.md.

WHY A THIRD PATCH
    The dashboard lives in the orrery, and Dashboard Parity (L-440), a
    checker of the orrery's maintenance run, holds its buttons to the
    website's run steps, reading the gallery folder beside this one. The
    website's Horizons buttons can leave only once their scripts have
    left the website, which is the gallery patch's job; before it, the
    check would fail. So this runs after that patch.

HOW TO RUN
    Save it in the orrery repo's ROOT folder, open it in VS Code and press
    Run, or from a terminal in that folder:
        python patch_L431_13_dashboard_buttons_20261014.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing. It refuses, writing nothing, unless the
    gallery folder beside this one shows the gallery patch has run
    (tools/test_drawn_orbit.py there, tools/horizons_check.py gone).

WHAT IT CHANGES
    palomas_orrery_dashboard.py only: the Daily Run group loses Horizons
      Check and says three steps; the website checks lose Horizons Check
      Suite; the website's Horizons Confirmations says where its dates
      come from now; Drawn Orbit, the website's new checker, gets its
      button under the served cache; their short lines follow; the
      docstring says so.

SAFETY
    The file is checked only at the lines this patch edits: every anchor
    must match exactly once. If any check fails, NOTHING is written. A
    file found with Windows line endings is matched after turning them
    into LF and written back LF, and the patch says so. Undo after a run
    is Discard Changes in GitHub Desktop.

Role: patch
Domain: dev_tools
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
GALLERY = os.path.normpath(os.path.join(ROOT, '..', 'tonyquintanilla.github.io'))
MARKER = '--- Your run record below this line'
ZONES = ()
MUST_EXIST = ('celestial_objects.py', 'palomas_orrery_dashboard.py')

EDITS = [
    ('palomas_orrery_dashboard.py', "line 248: October 14, 2026 with Anthropic's Claude Opus",
     (
         'patch has removed their scripts, so Dashboard Parity holds at every step.\n'
         '"""\n'
     ),
     (
         'patch has removed their scripts, so Dashboard Parity holds at every step.\n'
         "October 14, 2026 with Anthropic's Claude Opus 5.5 (L-431 build 3, its\n"
         "third patch, patch_L431_13, run after the website's): the Daily Run\n"
         'group loses Horizons Check and says three steps; the website checks lose\n'
         "Horizons Check Suite, whose script went to the orrery; the website's\n"
         'Horizons Confirmations says it reads the dates from the pulled export;\n'
         "and Drawn Orbit, the website's new checker, gets its button under the\n"
         'served cache, in alphabetical place, with its short line.\n'
         '"""\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 366: "or replies if you like. Then the Horizons Ch',
     (
         '         "Updater: approve or decline each new message, and write entries "\n'
         '         "or replies if you like. Then the Horizons Check: JPL confirms "\n'
         '         "the website\'s objects that are due (L-395). Then the Cache "\n'
         '         "Builder, with no OneDrive pause since 2026-10-10 (L-216: "\n'
     ),
     (
         '         "Updater: approve or decline each new message, and write entries "\n'
         '         "or replies if you like. Then the Cache "\n'
         '         "Builder, with no OneDrive pause since 2026-10-10 (L-216: "\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 396: GALLERY_REPO_DIR,',
     (
         '         "tools/guestbook_local.json, which git ignores.",\n'
         '         GALLERY_REPO_DIR,\n'
         '         True,\n'
         '         None,\n'
         '         True),\n'
         '        ("Horizons Check",\n'
         '         os.path.join("tools", "horizons_check.py"),\n'
         '         "The Daily Run\'s second step (L-395). Asks JPL Horizons whether "\n'
         '         "each object the website takes from the orrery\'s list is still "\n'
         '         "the object the list says -- the same id, the same index, JPL\'s "\n'
         '         "exact name -- for the entries that are due: each every 30 days, "\n'
         '         "and at once after its entry changes. A pinned comet record "\n'
         '         "(Halley, Encke) must still be JPL\'s newest. One line per entry; "\n'
         '         "for each disagreement the list\'s value, JPL\'s value and the "\n'
         '         "query to paste into a browser. Records each confirmation in "\n'
         '         "data/horizons_confirmations.json and never edits the list. "\n'
         '         "Needs the internet; if JPL cannot be reached it says so and "\n'
         '         "asks nothing more. Runs from the gallery repo ROOT.",\n'
         '         GALLERY_REPO_DIR,\n'
     ),
     (
         '         "tools/guestbook_local.json, which git ignores.",\n'
         '         GALLERY_REPO_DIR,\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 448: "The Daily Run\'s fourth step: the same button',
     (
         '         "gallery_maintenance_run.py",\n'
         '         "The Daily Run\'s fourth step: the same button as Gallery "\n'
         '         "Maintenance Run -- offline under Gallery -- checks and data, "\n'
     ),
     (
         '         "gallery_maintenance_run.py",\n'
         '         "The Daily Run\'s third step: the same button as Gallery "\n'
         '         "Maintenance Run -- offline under Gallery -- checks and data, "\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 468: "the config mirror check, the Horizons check ',
     (
         '        "the mirror suite, the store writer and store editor suites, "\n'
         '        "the config mirror check, the Horizons check suite, Horizons "\n'
         '        "confirmations, the pointer join, cache in step, the drawings "\n'
         '        "check, the collapsed-features sweep, the "\n'
     ),
     (
         '        "the mirror suite, the store writer and store editor suites, "\n'
         '        "the config mirror check, Horizons "\n'
         '        "confirmations, the pointer join, cache in step, drawn orbit, the drawings "\n'
         '        "check, the collapsed-features sweep, the "\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 485: "daily_run.py --check: fails if any of the fo',
     (
         '        "daily_run.py",\n'
         '        "daily_run.py --check: fails if any of the four scripts the "\n'
         '        "Daily Run calls is missing, say after a rename, and names it. "\n'
     ),
     (
         '        "daily_run.py",\n'
         '        "daily_run.py --check: fails if any of the three scripts the "\n'
         '        "Daily Run calls is missing, say after a rename, and names it. "\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 552: ("Horizons Check Suite",',
     (
         '        "JPL\'S CHECK OF THE OBJECTS",\n'
         '        ("Horizons Check Suite",\n'
         '        os.path.join("tools", "test_horizons_check.py"),\n'
         '        "The Horizons check on JPL\'s recorded answers, with no network "\n'
         '        "(documentation/horizons_answers_L395.json, each answer with its "\n'
         '        "source): every served entry agrees, and each planted mistake -- a "\n'
         '        "wrong id, the wrong index, a name off by one letter, a stale pin, "\n'
         '        "a record number JPL gave to another comet, JPL unreachable -- is "\n'
         '        "caught by name (L-395). GATES the gallery runner.",\n'
         '        GALLERY_REPO_DIR,\n'
         '        True,\n'
         '        None,\n'
         '        True),\n'
         '        ("Horizons Confirmations",\n'
         '        os.path.join("tools", "check_horizons_confirmations.py"),\n'
         '        "Reads data/horizons_confirmations.json offline and fails on any "\n'
         '        "served object never confirmed against JPL, confirmed 30 or more "\n'
         '        "days ago, or changed since it was confirmed -- so a Horizons "\n'
         '        "Check that stopped running shows (L-395). GATES the gallery "\n'
         '        "runner.",\n'
         '        GALLERY_REPO_DIR,\n'
     ),
     (
         '        "JPL\'S CHECK OF THE OBJECTS",\n'
         '        ("Horizons Confirmations",\n'
         '        os.path.join("tools", "check_horizons_confirmations.py"),\n'
         '        "The website\'s own check of JPL\'s confirmations, offline: it reads "\n'
         '        "the dates in the pulled data/objects_export.json and fails on any "\n'
         '        "served object never confirmed against JPL, confirmed 30 or more "\n'
         '        "days ago, or changed since -- and on a fetched period the same "\n'
         '        "way -- so the website shows it when the orrery\'s Horizons Check "\n'
         '        "has not run (L-395; the check itself moved into the orrery\'s "\n'
         '        "Maintenance Run on 2026-10-14, L-431). GATES the gallery runner.",\n'
         '        GALLERY_REPO_DIR,\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 636: GALLERY_REPO_DIR,',
     (
         '        "it, not by its name.",\n'
         '        GALLERY_REPO_DIR,\n'
     ),
     (
         '        "it, not by its name.",\n'
         '        GALLERY_REPO_DIR,\n'
         '        True,\n'
         '        None,\n'
         '        True),\n'
         '        ("Drawn Orbit",\n'
         '        os.path.join("tools", "test_drawn_orbit.py"),\n'
         '        "An orbit whose period JPL gives around the solar system\'s "\n'
         '        "barycentre is drawn around the barycentre, moved to where it sits "\n'
         '        "seen from the Sun (L-431 build 3). Checks the cache builder serves "\n'
         '        "those elements only for such a body and only at the date of its "\n'
         '        "Sun-centred ones, refuses a set from another date, and that the "\n'
         '        "room draws the ellipse in the right place, on Sedna\'s real numbers. "\n'
         '        "Planted faults, among them an orbit drawn around the Sun, are each "\n'
         '        "caught. GATES the gallery runner.",\n'
         '        GALLERY_REPO_DIR,\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 1675: "Horizons Check"):',
     (
         '    ("Daily Run",\n'
         '     "Horizons Check"):\n'
         '        "Asks JPL whether each object the website serves is still that object.",\n'
         '    ("Daily Run",\n'
         '     "Cache Builder"):\n'
     ),
     (
         '    ("Daily Run",\n'
         '     "Cache Builder"):\n'
     )),
    ('palomas_orrery_dashboard.py', 'line 1702: "Horizons Check Suite"):',
     (
         '    ("Gallery -- checks and data",\n'
         '     "Horizons Check Suite"):\n'
         '        "The Horizons check on JPL\'s recorded answers, planted mistakes caught.",\n'
         '    ("Gallery -- checks and data",\n'
         '     "Horizons Confirmations"):\n'
         '        "Fails on any served object JPL has not confirmed within 30 days.",\n'
         '    ("Gallery -- checks and data",\n'
     ),
     (
         '    ("Gallery -- checks and data",\n'
         '     "Horizons Confirmations"):\n'
         '        "Fails on any served object JPL has not confirmed within 30 days.",\n'
         '    ("Gallery -- checks and data",\n'
         '     "Drawn Orbit"):\n'
         '        "Checks a barycentre orbit is served and drawn around the barycentre.",\n'
         '    ("Gallery -- checks and data",\n'
     )),
]

CREATED = {
}



def _zone_hit(text, pos, length):
    spans = []
    for a, b in ZONES:
        if a in text and b in text:
            spans.append((text.index(a), text.index(b) + len(b)))
    if MARKER in text:
        spans.append((text.index(MARKER), len(text)))
    for s, e in spans:
        if pos < e and pos + length > s:
            return True
    return False


def apply():
    print('%s' % os.path.basename(__file__))
    print('Running in: %s' % ROOT)
    print()
    for f in MUST_EXIST:
        if not os.path.exists(os.path.join(ROOT, f)):
            print('ERROR: %s is not here. Save this script in the orrery repo\'s ROOT '
                  'folder and run it there. NOTHING was written.' % f)
            return None
    if not os.path.isdir(GALLERY):
        print('ERROR: the gallery folder is not beside this one (%s). NOTHING was'
              % GALLERY)
        print('written.')
        return None
    if (not os.path.exists(os.path.join(GALLERY, 'tools', 'test_drawn_orbit.py'))
            or os.path.exists(os.path.join(GALLERY, 'tools', 'horizons_check.py'))):
        print('ERROR: the gallery patch has not run yet: run')
        print('patch_L431_12_website_gallery_20261014.py in the gallery folder first.')
        print('NOTHING was written.')
        return None
    if not os.path.exists(os.path.join(ROOT, 'horizons_check.py')):
        print('ERROR: horizons_check.py is not here: run')
        print('patch_L431_11_website_orrery_20261014.py first. NOTHING was written.')
        return None
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return None
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-45s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            return None
        if _zone_hit(t, t.index(old), len(old)):
            print('ANCHOR FAIL  %-45s %s lies in a generated zone or below the run-record '
                  'marker. NOTHING was written.' % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, t in list(texts.items()) + list(CREATED.items()):
        if any(ord(c) > 127 for c in t):
            print('ERROR: %s would hold non-ASCII after this patch. NOTHING was written.' % f)
            return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, t in CREATED.items():
        d = os.path.dirname(os.path.join(ROOT, f))
        if d and not os.path.isdir(d):
            os.makedirs(d)
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in CREATED:
        print('ok  %-45s created' % f)
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d file)' % (len(done), len(texts)))
    print('Stamp updated: the dashboard\'s docstring.')
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect "Dashboard parity" to pass and')
    print('     every gating checker with it.')
    print('  2. Move this script into documentation/. Commit and push the orrery.')
    print('  3. Back in the gallery: the Daily Run, then commit and push (the')
    print('     handoff, step 9 on).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
