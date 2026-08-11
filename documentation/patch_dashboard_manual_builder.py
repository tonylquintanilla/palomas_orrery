"""
patch_dashboard_manual_builder.py

Adds the gallery cache builder to the dashboard's Developer Tools group as
the first entry, launched from the GALLERY REPO ROOT so its relative data/
paths resolve. Removes the old Gallery & Web entry for the same script,
which launched from tools/ and therefore could not find
data/objects_config.json. Also gives card descriptions a wrap width, so a
long description renders instead of running off the edge of the window.

Target file: palomas_orrery_dashboard.py (orrery repo root)
Built on 826a932f8bb7329e211337085f4d68d26aaa4a51

HOW TO RUN
  Save this file into the SAME folder as palomas_orrery_dashboard.py,
  open it in VS Code, and click Run.

  Or from a terminal in that folder:  python patch_dashboard_manual_builder.py

WHAT SUCCESS LOOKS LIKE
  Four lines reading "ok", then "patch applied (N bytes)".

WHAT FAILURE LOOKS LIKE
  A single line beginning "ERROR:" or "ANCHOR FAIL:". Nothing is written
  in either case, so it is always safe to re-check and run again.
"""

import hashlib
import os
import sys

TARGET = 'palomas_orrery_dashboard.py'
BASE_MD5 = 'f1ac10411e4ff618ee99eca10910bb46'   # line-ending normalized

# ------------------------------------------------------------------
# Edits, bottom-up by position in the file.
# ------------------------------------------------------------------

EDIT_4_OLD = '''        ctk.CTkLabel(
            text_frame, text=desc,
            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w"
        ).pack(anchor="w")'''

EDIT_4_NEW = '''        ctk.CTkLabel(
            text_frame, text=desc,
            font=FONT_DESC, text_color=COLOR_TEXT_DIM, anchor="w",
            wraplength=600, justify="left"
        ).pack(anchor="w")'''

EDIT_3_OLD = '''    "Developer Tools": [
        ("Update Ledger Index",'''

EDIT_3_NEW = '''    "Developer Tools": [
        ("Gallery Cache Builder -- Manual Run",
         os.path.join("tools", "gallery_cache_builder.py"),
         "Manual serving-cache build. Runs from the gallery repo ROOT: the "
         "builder resolves its data/ paths from the working directory, so "
         "launching it from tools/ cannot find data/objects_config.json. "
         "With no flags it fetches from Horizons, validates, atomic-swaps "
         "the new cache into data/solar-system, and STOPS -- it does not "
         "commit or push. Commit it yourself in GitHub Desktop after the "
         "run finishes. Do not commit while it is still running: mid-build "
         "the working tree shows deletions only, which is the swap in "
         "progress, not data loss. The console stays open at the repo root "
         "if you want a flagged re-run (--dry-run --object <slug>, "
         "--first-build).",
         GALLERY_REPO_DIR,
         True),
        ("Update Ledger Index",'''

EDIT_2_OLD = '''        ("Gallery Cache Builder",
        "gallery_cache_builder.py",
        "Nightly serving-cache builder (Phase 2 F1): fetch from Horizons, "
        "validate, atomic swap, commit. Needs flags -- opens a console so "
        "you can type --dry-run / --first-build / --nightly / --object etc.",
        GALLERY_TOOLS_DIR,
        True),
'''

EDIT_2_NEW = ''

EDIT_1_OLD = '''# Gallery tools live in a sibling directory
GALLERY_TOOLS_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io", "tools")'''

EDIT_1_NEW = '''# Gallery tools live in a sibling directory
GALLERY_TOOLS_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io", "tools")

# The cache builder must run from the gallery REPO ROOT, not from tools/:
# its --config and --output-dir defaults are relative to the working
# directory. Launching it from GALLERY_TOOLS_DIR fails on load_config().
GALLERY_REPO_DIR = os.path.join(SCRIPT_DIR, "..", "tonyquintanilla.github.io")'''

EDITS = [
    ('description wrap width', EDIT_4_OLD, EDIT_4_NEW),
    ('Developer Tools entry', EDIT_3_OLD, EDIT_3_NEW),
    ('remove old Gallery & Web entry', EDIT_2_OLD, EDIT_2_NEW),
    ('GALLERY_REPO_DIR constant', EDIT_1_OLD, EDIT_1_NEW),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, TARGET)

    if not os.path.exists(path):
        print("ERROR: %s not found next to this script." % TARGET)
        print("       Put this file in the same folder and run it again.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fp != BASE_MD5:
        print("ERROR: base moved. %s is not the file this patch was built" % TARGET)
        print("       against. Expected %s, found %s." % (BASE_MD5, fp))
        print("       Nothing was written. Send me the current file.")
        return 1

    is_crlf = data.count(b'\r\n') > 0

    for label, old, new in EDITS:
        o = old.encode('ascii')
        n = new.encode('ascii')
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = data.count(o)
        if count != 1:
            print("ANCHOR FAIL: %s -- expected 1 match, found %d." % (label, count))
            print("             Nothing was written.")
            return 1
        data = data.replace(o, n)
        print("ok   %s" % label)

    with open(path, 'wb') as f:
        f.write(data)

    print("patch applied (%d bytes)" % len(data))
    print("")
    print("Next: run palomas_orrery_dashboard.py and check the Developer")
    print("Tools group. The builder should be the first card, and the long")
    print("descriptions should now wrap onto several lines instead of")
    print("running off the right edge.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
