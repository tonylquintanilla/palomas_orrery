"""
patch_L334_1d_dashboard_cache_in_step_20260917.py -- ORRERY repo. The
shared dashboard gains the gallery's new checker.

Built on orrery bb481bf43fe117e34342bd9d992fe9cc116edc70 at
https://github.com/tonylquintanilla/palomas_orrery
(the dashboard is unchanged since 2ef16f3b, where this was first cut)
Pairs with the gallery's patch_L334_1c_cache_in_step_20260917.py; run
that one first, or this button points at a file that is not there yet.

RUN
---
Save this file in the ORRERY repo root and click Run in VS Code.

WHAT IT DOES -- all or nothing, one file
----------------------------------------
    palomas_orrery_dashboard.py
      - a new button, "Cache In Step", after Pointer Join
      - the Gallery Maintenance Run description said "the three Node
        smoke suites". The run has six (Feature renderers, Page framing,
        Sun shells, Earth scene geometry, Hover budget, Arrival). It now
        names them, and names the cache-in-step check
      - the docstring records this change

AFTER IT RUNS: move this script into documentation/, run
python orrery_maintenance_run.py, commit, push.

UNDO: Discard Changes in GitHub Desktop.

Role: patch
Domain: dev_tools

Written September 17, 2026 with Anthropic's Claude Fable 5.1.
"""

import hashlib
import os
import sys

BUILT_ON = "bb481bf4"
DASHBOARD = "palomas_orrery_dashboard.py"
FINGERPRINT = "058a1d4c5f32308cb2143b82ebc5daa9"

EDITS = [('them and a Store drift that examined every link.\n"""\n',
  'them and a Store drift that examined every link.\n'
  "September 17, 2026 with Anthropic's Claude Fable 5.1 (L-334 session):\n"
  'added Cache In Step, the gallery check that the served cache holds what\n'
  'data/objects_config.json says, written after a config change reached\n'
  'the live site ahead of the cache. The Gallery Maintenance Run\n'
  'description said three Node smoke suites; it now names all six.\n'
  '"""\n'),
 ('        "the mirror suite, the config mirror check, the pointer join, "\n'
  '        "the three Node smoke suites, and the artifact-1 assembler "\n',
  '        "the mirror suite, the config mirror check, the pointer join, "\n'
  '        "the cache-in-step check, the six Node suites (feature "\n'
  '        "renderers, page framing, Sun shells, Earth scene geometry, "\n'
  '        "hover budget, arrival), and the artifact-1 assembler "\n'),
 ('        GALLERY_REPO_DIR,\n'
  '        True,\n'
  '        ["--join"],\n'
  '        True),\n',
  '        GALLERY_REPO_DIR,\n'
  '        True,\n'
  '        ["--join"],\n'
  '        True),\n'
  '        ("Cache In Step",\n'
  '        os.path.join("tools", "check_cache_in_step.py"),\n'
  '        "Checks that the served cache holds the same shells as "\n'
  '        "data/objects_config.json, value for value. The rooms draw from '
  '"\n'
  '        "the cache, not from the config, so a config change reaches a "\n'
  '        "visitor only after the cache builder has run. When this fails, '
  '"\n'
  '        "run the cache builder and commit its output with the config; do '
  '"\n'
  '        "not push the config alone. Names each difference by its path. "\n'
  '        "GATES the gallery runner.",\n'
  '        GALLERY_REPO_DIR,\n'
  '        True,\n'
  '        None,\n'
  '        True),\n')]

def lf(data):
    return data.replace(b"\r\n", b"\n")


def apply_edits(name, fingerprint, pairs, built_on):
    with open(name, "rb") as handle:
        old = handle.read()
    if hashlib.md5(lf(old)).hexdigest() != fingerprint:
        raise SystemExit("ERROR: %s is not the version this patch was built "
                         "on (%s), or this patch has already run. NOTHING "
                         "was written." % (name, built_on))
    was_crlf = b"\r\n" in old
    text = lf(old).decode("utf-8")
    for index, (before, after) in enumerate(pairs):
        if text.count(before) != 1:
            raise SystemExit("ANCHOR FAIL in %s, change %d of %d: found %d "
                             "matches, expected 1. NOTHING was written."
                             % (name, index + 1, len(pairs),
                                text.count(before)))
        text = text.replace(before, after)
    data = text.encode("utf-8")
    try:
        data.decode("ascii")
    except UnicodeDecodeError:
        raise SystemExit("ERROR: %s would contain non-ASCII text. NOTHING "
                         "was written." % name)
    if was_crlf:
        data = data.replace(b"\n", b"\r\n")
    return data, was_crlf


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    if not os.path.exists("constants_new.py"):
        raise SystemExit("ERROR: this script is not in the orrery repo root "
                         "(no constants_new.py beside it). NOTHING was "
                         "written.")
    data, was_crlf = apply_edits(DASHBOARD, FINGERPRINT, EDITS, BUILT_ON)
    with open(DASHBOARD, "wb") as handle:
        handle.write(data)
    print("ok  %-30s %d change(s)%s" % (DASHBOARD, len(EDITS),
                                         " [CRLF kept]" if was_crlf else ""))
    print("")
    print("patch applied (1 file)")
    print("Next: move this script into documentation/, then run")
    print("python orrery_maintenance_run.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
