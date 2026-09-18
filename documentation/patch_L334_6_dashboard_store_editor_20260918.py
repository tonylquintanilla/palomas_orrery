#!/usr/bin/env python3
"""
patch_L334_6_dashboard_store_editor_20260918.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
palomas_orrery_dashboard.py), open it in VS Code and click Run.
Or:  python patch_L334_6_dashboard_store_editor_20260918.py

A patch is run from its repository's ROOT and filed in documentation/ AFTER
it has run. Filed first and run second, it stops with one line, writes
nothing, and the push goes out without it.

Built on orrery 8860b91b7cbcb6733844ef67478e7a6ef3cb52fd
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 2f971040d14f9a9ee8c3d7c49c9d2aa182a1e0f4)

WHAT IT DOES (one file, palomas_orrery_dashboard.py):

  Adds an Exhibit Store Editor button to Developer Tools, directly under
  Gallery Cache Builder -- Manual Run, so the two tools Tony runs BY HAND
  against the gallery sit together. It launches the gallery's
  tools/exhibit_store_editor.py as a window, with no console, the way
  Gallery Studio and Gallery Editor are launched.

  One line is added to the module's change log at the top, as every
  earlier change to this file has done.

SAFE TO RUN BEFORE THE EDITOR EXISTS. exhibit_store_editor.py lands in
the GALLERY repo in a later push. Until it does, pressing the button logs
"Not found: ...\\tools\\exhibit_store_editor.py" in the status panel and
does nothing else -- the dashboard checks the path before launching.

WHY DEVELOPER TOOLS RATHER THAN GALLERY & WEB. Because Tony asked for it
there. Worth knowing: Gallery Studio, Gallery Editor and the JSON
Converter are all in Gallery & Web, so if this button reads better beside
them, say so and it moves -- it is four lines either way.

THEN (Tony): python orrery_maintenance_run.py, then move this script into
documentation/, commit and push.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = 'palomas_orrery_dashboard.py'
FP_EXPECTED = 'e1cee633eda06a26b9e959a2310de3da'

LOG_OLD = b'''September 17, 2026 with Anthropic's Claude Fable 5.1 (L-334 session):
added Cache In Step, the gallery check that the served cache holds what
data/objects_config.json says, written after a config change reached
the live site ahead of the cache. The Gallery Maintenance Run
description said three Node smoke suites; it now names all six.
"""
'''

LOG_NEW = b'''September 17, 2026 with Anthropic's Claude Fable 5.1 (L-334 session):
added Cache In Step, the gallery check that the served cache holds what
data/objects_config.json says, written after a config change reached
the live site ahead of the cache. The Gallery Maintenance Run
description said three Node smoke suites; it now names all six.
September 18, 2026 with Anthropic's Claude Opus 5 (L-334): added
Exhibit Store Editor to Developer Tools, under Gallery Cache Builder --
Manual Run, so the two by-hand gallery tools sit together. It is a
window rather than a console tool, so it is declared the way Gallery
Studio is, with no interactive flag.
"""
'''

BUTTON_OLD = b'''         GALLERY_REPO_DIR,
         True),
        ("MAINTENANCE RUN -- everything indented below",
'''

BUTTON_NEW = b'''         GALLERY_REPO_DIR,
         True),
        ("Exhibit Store Editor",
         "exhibit_store_editor.py",
         "Edit the words a visitor reads in the exhibit rooms, and tick "
         "what each room opens on. A window: pick a room, pick a shell, "
         "type. It writes data/objects_config.json IN PLACE, changing "
         "only the line it was asked to, so the diff stays readable. It "
         "will write a shell's name, description, about, note, source "
         "and link, a radiation belt's words, and the arrival block's "
         "shells and Moon -- and nothing else. Numbers, their units, "
         "their figure counts and their orrery_constant links are shown "
         "in grey and cannot be typed into; a number changes in "
         "constants_new.py and arrives here through the export and the "
         "mirror. SAVING IS NOT DEPLOYING: words reach a visitor only "
         "after the cache builder has run, because the rooms draw their "
         "shells from the served cache, while the opening-view ticks are "
         "read from the config by the page itself and need only the "
         "push. The window says which after every save. It does NOT "
         "start the cache builder -- that stays a hand run with OneDrive "
         "paused (L-216).",
         GALLERY_TOOLS_DIR),
        ("MAINTENANCE RUN -- everything indented below",
'''

EDITS = [(LOG_OLD, LOG_NEW), (BUTTON_OLD, BUTTON_NEW)]


def lf(data):
    return data.replace(b'\r\n', b'\n')


def main():
    path = os.path.join(ROOT, TARGET)
    if not os.path.exists(path):
        print(f'ERROR: {TARGET} not found next to this script.')
        print('       Run this patch from the ORRERY repo ROOT, not from')
        print('       documentation/. NOTHING was written.')
        return 1
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    content = lf(raw)
    actual = hashlib.md5(content).hexdigest()
    if actual != FP_EXPECTED:
        print(f'ERROR: {TARGET} is not the file this patch was built against')
        print(f'       expected {FP_EXPECTED}, found {actual}'
              f'{" [CRLF]" if was_crlf else ""}')
        print('       NOTHING was written. Undo is Discard Changes in '
              'GitHub Desktop.')
        return 1
    for old, new in EDITS:
        n = content.count(old)
        if n != 1:
            print(f'ANCHOR FAIL: expected 1 match, found {n}: {old[:60]!r}')
            print('NOTHING was written. Undo is Discard Changes in '
                  'GitHub Desktop.')
            return 1
        content = content.replace(old, new, 1)
    if any(c > 127 for c in content):
        print('ERROR: the result would hold non-ASCII bytes. NOTHING was '
              'written.')
        return 1
    out = content.replace(b'\n', b'\r\n') if was_crlf else content
    with open(path, 'wb') as handle:
        handle.write(out)
    print(f'ok  {TARGET}  ({len(out)} bytes'
          f'{", CRLF preserved" if was_crlf else ""})')
    print('added: Exhibit Store Editor, in Developer Tools, under')
    print('       Gallery Cache Builder -- Manual Run')
    print('')
    print('Until the editor is pushed to the gallery, the button logs')
    print('"Not found: ...tools\\\\exhibit_store_editor.py" and does nothing')
    print('else. That is the dashboard checking the path, not an error.')
    print('')
    print('NEXT: python orrery_maintenance_run.py, then move this script')
    print('      into documentation/, commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
