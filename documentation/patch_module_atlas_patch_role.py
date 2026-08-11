"""
patch_module_atlas_patch_role.py -- add a transient `patch` role to
module_atlas.py so spent one-shot patch scripts classify as what they
are instead of landing in `undetermined`.

WHY
    `undetermined` was doing two jobs: "someone forgot a Role: tag" (a
    defect) and "a patch script is sitting in the scanned tree" (a
    filing step not yet done). Merging them means neither reads
    cleanly, and the second one only got noticed by hand.

    A `patch` role separates them. It is TRANSIENT by declaration: a
    module carrying it is reported under "Patch scripts awaiting
    archive" with the action named, rather than folded into the clean
    roster where its presence would stop being visible. `undetermined`
    goes back to meaning only what it says.

WHAT THIS DOES
    Six anchored edits to module_atlas.py:
      1. `patch` added to ROLE_ORDER (between devtool and legacy)
      2. its ROLE_DESCRIPTIONS entry
      3. its ROLE_SECTION_TITLES entry
      4. classification_report_lines() collects patch-role modules
      5. an "awaiting archive" block in the Markdown coverage report
      6. the matching console lines, plus a credit line in the docstring

    ROLE_ORDER, ROLE_DESCRIPTIONS and ROLE_SECTION_TITLES are held in
    agreement by an assert at import time. All three move together here;
    if one were missed the module would refuse to import, which is the
    check doing its job.

    The provenance scanner needs no change. Its NARRATIVE_ROLES gate
    does not include `patch`, so patch scripts stay out of claim
    extraction -- which is the correct behavior.

THE CONVENTION THIS ESTABLISHES
    Every patch script from now on carries these two lines in its module
    docstring:

        Role: patch
        Domain: dev_tools

    THIS script carries them, so the first run of module_atlas.py after
    the patch lands will list this file under "awaiting archive" -- the
    feature demonstrating itself on its own author.

HOW TO RUN IT
    Save this file into the palomas_orrery repo root (the folder holding
    module_atlas.py), open it in VS Code, and click Run.

    Or from a terminal in that folder:
        python patch_module_atlas_patch_role.py

    THEN run module_atlas.py the same way, to regenerate MODULE_ATLAS.md
    and MODULE_INDEX.md. They are currently stale: both still list
    patch_L189_run_history as a module after it moved to documentation/.

WHAT SUCCESS LOOKS LIKE
    One "ok" line per edit, then "patch applied (N bytes)".

WHAT FAILURE LOOKS LIKE
    A single "ERROR:" line (wrong base file) or an "ANCHOR FAIL" line
    naming the edit whose text was not found. Either way NOTHING is
    written and the file on disk is untouched.

Built on 84b4ee7de14197b0e8a4b2f9daba9dbb4fe5251d
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Role: patch
Domain: dev_tools

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'module_atlas.py'

# Content fingerprint with line endings normalized to LF.
BASE_MD5 = 'df9e696fa7ce8d5a64c9d8d004f65918'


EDITS = [
    (
        'ROLE_ORDER gains patch',
        b"    'devtool', 'legacy', 'other', UNDETERMINED\n",

        b"    'devtool', 'patch', 'legacy', 'other', UNDETERMINED\n",
    ),
    (
        'ROLE_DESCRIPTIONS entry',
        b"    'devtool':          'Developer tools (dependency tracing, "
        b"atlas)',\n"
        b"    'legacy':           'Archived / superseded modules',\n",

        b"    'devtool':          'Developer tools (dependency tracing, "
        b"atlas)',\n"
        b"    'patch':            'Spent one-shot patch script -- transient, "
        b"belongs in documentation/',\n"
        b"    'legacy':           'Archived / superseded modules',\n",
    ),
    (
        'ROLE_SECTION_TITLES entry',
        b"    'devtool':          'Developer Tools',\n"
        b"    'legacy':           'Legacy / Archived Modules',\n",

        b"    'devtool':          'Developer Tools',\n"
        b"    'patch':            'Patch Scripts (transient -- awaiting "
        b"archive)',\n"
        b"    'legacy':           'Legacy / Archived Modules',\n",
    ),
    (
        'coverage report collects patch-role modules',
        b"    undetermined = [m for m in modules if m['role'] == UNDETERMINED]\n"
        b"    legacy = [m for m in modules if m.get('role_source') == 'legacy']\n"
        b"    no_domain = [m for m in modules\n"
        b"                 if m.get('domain', UNDETERMINED) == UNDETERMINED]\n"
        b"\n"
        b"    out = [f'{heading_level} Classification Coverage', '']\n"
        b"    if not undetermined and not legacy and not no_domain:\n",

        b"    undetermined = [m for m in modules if m['role'] == UNDETERMINED]\n"
        b"    legacy = [m for m in modules if m.get('role_source') == 'legacy']\n"
        b"    no_domain = [m for m in modules\n"
        b"                 if m.get('domain', UNDETERMINED) == UNDETERMINED]\n"
        b"    # A `patch` module is transient by declaration -- it is not a\n"
        b"    # classification failure, it is a filing step not yet done. It\n"
        b"    # is reported here rather than in the clean roster so that its\n"
        b"    # presence stays visible until it is archived.\n"
        b"    awaiting = [m for m in modules if m['role'] == 'patch']\n"
        b"\n"
        b"    out = [f'{heading_level} Classification Coverage', '']\n"
        b"    if not undetermined and not legacy and not no_domain \\\n"
        b"            and not awaiting:\n",
    ),
    (
        'awaiting-archive block in the report',
        b"    if undetermined:\n"
        b"        out.append(f'**Undetermined role ({len(undetermined)}).** "
        b"No valid '\n",

        b"    if awaiting:\n"
        b"        out.append(f'**Patch scripts awaiting archive "
        b"({len(awaiting)}).** '\n"
        b"                   'A `Role: patch` module is a one-shot script "
        b"that has '\n"
        b"                   'already run. Its base fingerprint no longer "
        b"matches, '\n"
        b"                   'so it cannot run again. Move each into '\n"
        b"                   '`documentation/`. While one sits in the scanned "
        b"tree '\n"
        b"                   'it inflates the module count here and the file "
        b"count '\n"
        b"                   'in the provenance audit.')\n"
        b"        out.append('')\n"
        b"        for m in awaiting:\n"
        b"            out.append(f'- `{m[\"path\"]}`')\n"
        b"        out.append('')\n"
        b"\n"
        b"    if undetermined:\n"
        b"        out.append(f'**Undetermined role ({len(undetermined)}).** "
        b"No valid '\n",
    ),
    (
        'console lines and credit',
        b"    # Print role summary\n"
        b"    print(\"\\nRole summary:\")\n"
        b"    for role in ROLE_ORDER:\n"
        b"        if role in by_role:\n"
        b"            count = len(by_role[role])\n"
        b"            print(f\"  {role:20s} {count:3d} modules\")\n",

        b"    # Print role summary\n"
        b"    print(\"\\nRole summary:\")\n"
        b"    for role in ROLE_ORDER:\n"
        b"        if role in by_role:\n"
        b"            count = len(by_role[role])\n"
        b"            print(f\"  {role:20s} {count:3d} modules\")\n"
        b"\n"
        b"    # Transient class: name the action rather than the count. A\n"
        b"    # zero here is the steady state, so nothing prints when clean.\n"
        b"    awaiting = by_role.get('patch') or []\n"
        b"    if awaiting:\n"
        b"        print(f\"\\n  {len(awaiting)} patch script(s) awaiting \"\n"
        b"              f\"archive -- move into documentation/:\")\n"
        b"        for mod in awaiting:\n"
        b"            print(f\"      {mod['path']}\")\n",
    ),
    (
        'docstring credit line',
        b"Role: devtool\nDomain: dev_tools\n\"\"\"\n",

        b"Module updated: August 2026 with Anthropic's Claude Opus 5: adds the\n"
        b"transient `patch` role. A spent one-shot patch script now classifies\n"
        b"as `patch` and is reported under \"Patch scripts awaiting archive\"\n"
        b"with the action named, instead of landing in `undetermined` -- which\n"
        b"had been carrying two unrelated meanings at once.\n"
        b"\n"
        b"Role: devtool\nDomain: dev_tools\n\"\"\"\n",
    ),
]


def fail(msg):
    print("ERROR: %s" % msg)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(here, TARGET)

    if not os.path.isfile(target):
        fail("%s not found next to this script. Save this script into the "
             "folder that holds %s." % (TARGET, TARGET))

    with open(target, 'rb') as f:
        data = f.read()

    fingerprint = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fingerprint != BASE_MD5:
        fail("base file has moved.\n"
             "       expected md5 (LF-normalized) %s\n"
             "       found                        %s\n"
             "       Nothing was written. Reconcile before applying."
             % (BASE_MD5, fingerprint))

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print("note: target uses CRLF; anchors translated to match.")

    patched = data
    for label, old, new in EDITS:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = patched.count(old)
        if count != 1:
            print("ANCHOR FAIL (%s): expected 1 match, found %d. "
                  "Nothing written." % (label, count))
            sys.exit(1)
        patched = patched.replace(old, new)
        print("  ok  %s" % label)

    with open(target, 'wb') as f:
        f.write(patched)

    print()
    print("patch applied (%d bytes)" % len(patched))
    print()
    print("NEXT: run module_atlas.py. It regenerates MODULE_ATLAS.md and")
    print("MODULE_INDEX.md, which are stale -- both still list")
    print("patch_L189_run_history as a module after it moved.")
    print("That run will also list THIS script as awaiting archive,")
    print("which is the new class working on its own author.")


if __name__ == '__main__':
    main()
