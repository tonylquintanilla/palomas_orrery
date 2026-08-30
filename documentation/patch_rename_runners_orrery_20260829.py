"""
patch_rename_runners_orrery_20260829.py -- the ORRERY half.

Two programs were called maintenance_run.py, one per repository, and on
2026-08-29 that cost the orrery its runner for three commits: the gallery
one was downloaded, the orrery one was displaced, and the dashboard button
reported "not found". This patch gives each runner a name that says which
repository it belongs to.

    orrery_maintenance_run.py     here (L-188, 4 generators, 11 checkers)
    gallery_maintenance_run.py    the gallery repo (L-236)

Run the gallery half separately:
    patch_rename_gallery_runner_20260829.py

Neither depends on the other and the order does not matter -- they are in
different repositories and touch no shared file.

Built on orrery `c76bfa021d2a174f7d7b329ad526d8979cb52b25` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `5753aa7994d8fc6e507b6e33d2c90f9a2eecbaa1` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote 2026-08-29.

EIGHT files, ONE transaction. Every guard, every anchor and every rename
is checked before anything is written. If one refuses, nothing moves.


WHAT IT DOES

 1. RENAMES maintenance_run_ORRERY.py -> orrery_maintenance_run.py. That
    _ORRERY suffix was never meant to survive; it was a label on a
    download so two files with one name could not collide in a downloads
    folder again. The rename is done here rather than by hand, because
    hand-moving these two files is what caused the incident.

 2. SWEEPS the seven live references to the old filename -- the dashboard
    button, module_atlas.py's role map, worksheet_checker.py twice, and
    three test-module docstrings. MODULE_ATLAS.md carries four more and
    is left alone: it is generated, and module_atlas.py rewrites it.

    NOT swept, deliberately: LEDGER_CONSOLIDATED.md, the handoffs, and
    the spent patch scripts under documentation/. Those record what
    happened under the name it had at the time. Rewriting them would be
    the rebasing failure the ledger already carries a lesson about.

 3. ADDS two dashboard entries for the gallery runner, offline and
    --live, both launching in GALLERY_REPO_DIR. The dashboard already
    runs gallery-repo tools that way -- Gallery Cache Builder does -- so
    this follows the existing pattern rather than introducing one. The
    two rows share a script and differ by args, which the launcher's
    debounce key already accounts for.

    Gallery Builder Offline Tests becomes indented beneath them, because
    indent means "the runner above already covers this" and the gallery
    runner does cover that suite.

 4. RETIRES the tracked .bak files. Nine of them are committed, including
    2,268 lines of superseded master plan and a superseded copy of
    provenance-discipline. A future session grepping for a constant or a
    rule can hit one and read a retired value as current, which is The
    Correction Does Not Travel with the correction sitting right beside
    the stale copy. *.bak goes into .gitignore and the nine come out.

    The patch deletes them from disk. Git will show nine deletions;
    commit them.


AFTER RUNNING IT

  1. module_atlas.py        -- regenerates MODULE_ATLAS.md under the new
                               name, which is what closes reference 8-11
  2. orrery_maintenance_run.py
  3. the dashboard, to see the two new gallery buttons

Then commit. Rename plus deletions in one commit is fine; git records
the rename as a rename.

HOW TO RUN IT

Drop this file into the ORRERY repo root and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5 (L-264).
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"
PROBE = "constants_new.py"

OLD_RUNNER = "maintenance_run_ORRERY.py"
NEW_RUNNER = "orrery_maintenance_run.py"

# Guards are md5 of the LF-NORMALISED content, not of the raw bytes. A
# Windows tool writing in text mode flips a whole file to CRLF without
# changing a character, and git normalises it back on commit, so the repo
# and the working copy legitimately disagree byte-for-byte. .gitignore is
# stored CRLF in this repo already.
GUARDS = {
    "palomas_orrery_dashboard.py": "0e0b03e0a7e249a5d170e9fe71b1a1e0",
    "module_atlas.py": "01cee1ee346fca4670e898ac919276a0",
    "worksheet_checker.py": "b3818b16b5f680ba48288f36852ddc00",
    "test_worksheet_checker.py": "10deca047f1bf1fb4391fd697d11663e",
    "test_worksheet_request_builder.py": "9bb2657b371929decd1a6e6a72296042",
    "test_reset_completeness.py": "c1815206bfd9d0c5a4db29ed88e308ae",
    OLD_RUNNER: "9a4a719b5b86660324262b2ed8c8ce68",
    ".gitignore": "e96d88b077dd0ac70736f4fee2264688",
}

BAK_FILES = [
    "LEDGER_CONSOLIDATED.md.bak",
    "PROJECT_INSTRUCTIONS.md.bak",
    "constants_new.py.bak",
    "test_constants_provenance.py.bak",
    os.path.join("documentation", "HANDOFF_20260829_sun_ships.md.bak"),
    os.path.join("documentation", "MASTER_PLAN_CRITICAL_PATH_SUMMARY.md.bak"),
    os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md.bak"),
    os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md.bak"),
    os.path.join("skills", "provenance-discipline", "SKILL.md.bak"),
]


# ------------------------------------------------------------------
# The two new dashboard rows
# ------------------------------------------------------------------

GALLERY_ROWS = (
    '        ("Gallery Maintenance Run -- offline",\n'
    '        "gallery_maintenance_run.py",\n'
    '        "The gallery repo\'s own runner (L-236), before you commit. "\n'
    '        "Regenerates the module atlas, then runs the 149-check cache "\n'
    '        "builder suite, the three Node smoke suites, and the artifact-1 "\n'
    '        "assembler test. Three states rather than two: a suite that '
    'could "\n'
    '        "not run -- Node missing, say -- reports UNREACHABLE and is "\n'
    '        "never counted as a pass. Everything indented below is included "\n'
    '        "in it.",\n'
    '        GALLERY_REPO_DIR,\n'
    '        True),\n'
    '        ("Gallery Maintenance Run -- live, AFTER a push",\n'
    '        "gallery_maintenance_run.py",\n'
    '        "The two checks that can only mean something once GitHub Pages "\n'
    '        "has deployed. Fetches seven files from palomasorrery.com and "\n'
    '        "requires each to be served -- this is what catches Jekyll "\n'
    '        "dropping every .py in the repo, which no local test can see. "\n'
    '        "Then follows objects_config.json\'s orrery_constant pointers "\n'
    '        "into constants_new.py at the orrery HEAD and reports any value "\n'
    '        "that has drifted. If the site is still serving the previous "\n'
    '        "deploy it says NOT YET DEPLOYED rather than passing. Report "\n'
    '        "only; it gates nothing.",\n'
    '        GALLERY_REPO_DIR,\n'
    '        True,\n'
    '        ["--live"]),\n'
)


# ------------------------------------------------------------------
# Edits, per file
# ------------------------------------------------------------------

EDITS = {
    "palomas_orrery_dashboard.py": [
        (
            "dashboard button points at the renamed runner",
            '        ("MAINTENANCE RUN -- everything indented below",\n'
            '         "maintenance_run.py",\n',
            '        ("MAINTENANCE RUN -- everything indented below",\n'
            '         "orrery_maintenance_run.py",\n',
        ),
        (
            "two gallery runner rows; the offline suite indents beneath them",
            '        ("Gallery Builder Offline Tests",\n'
            '        "test_gallery_cache_builder_offline.py",\n'
            '        "Offline smoke test for gallery_cache_builder.py: mocks '
            'Horizons, "\n'
            '        "exercises first-build, nightly re-run, and the Guard v2 '
            'monitor path. "\n'
            '        "No network.",\n'
            '        GALLERY_TOOLS_DIR,\n'
            '        True),\n',

            GALLERY_ROWS +
            '        ("Gallery Builder Offline Tests",\n'
            '        "test_gallery_cache_builder_offline.py",\n'
            '        "Offline smoke test for gallery_cache_builder.py: mocks '
            'Horizons, "\n'
            '        "exercises first-build, nightly re-run, and the Guard v2 '
            'monitor path. "\n'
            '        "No network.",\n'
            '        GALLERY_TOOLS_DIR,\n'
            '        True,\n'
            '        None,\n'
            '        True),\n',
        ),
    ],
    "module_atlas.py": [
        (
            "role map key follows the filename",
            "    'maintenance_run':                        'devtool',\n",
            "    'orrery_maintenance_run':                 'devtool',\n",
        ),
    ],
    "worksheet_checker.py": [
        (
            "module docstring names the renamed runner",
            "It is also the last CHECKERS row in maintenance_run.py, so a normal\n",
            "It is also the last CHECKERS row in orrery_maintenance_run.py, so a\n"
            "normal\n",
        ),
        (
            "inline comment names the renamed runner",
            "    # It is also SHORT on purpose. maintenance_run.py trims a checker's\n",
            "    # It is also SHORT on purpose. orrery_maintenance_run.py trims a\n"
            "    # checker's\n",
        ),
    ],
    "test_worksheet_checker.py": [
        (
            "module docstring names the renamed runner",
            "It is also a CHECKERS row in maintenance_run.py, so a normal\n",
            "It is also a CHECKERS row in orrery_maintenance_run.py, so a normal\n",
        ),
    ],
    "test_worksheet_request_builder.py": [
        (
            "module docstring names the renamed runner",
            "It is also a CHECKERS row in maintenance_run.py, so a normal\n",
            "It is also a CHECKERS row in orrery_maintenance_run.py, so a normal\n",
        ),
    ],
    "test_reset_completeness.py": [
        (
            "comment names the renamed runner",
            "# The prefix is what maintenance_run.py matches on. Without it the runner\n",
            "# The prefix is what orrery_maintenance_run.py matches on. Without it\n"
            "# the runner\n",
        ),
    ],
    OLD_RUNNER: [
        (
            "the runner names itself, and names its counterpart",
            '"""maintenance_run.py -- L-188. One command, the whole maintenance suite.\n',
            '"""orrery_maintenance_run.py -- L-188. One command, the whole\n'
            'maintenance suite.\n'
            '\n'
            'THE OTHER RUNNER\n'
            'The gallery repo has its own, gallery_maintenance_run.py (L-236),\n'
            'and it is a different program: six rows offline and two more under\n'
            '--live, against the gallery\'s own files and the deployed site. The\n'
            'two were both called maintenance_run.py until 2026-08-29, when that\n'
            'cost this file three commits of not existing. Renamed under L-264.\n',
        ),
        (
            "run command names the renamed runner",
            "    python maintenance_run.py\n",
            "    python orrery_maintenance_run.py\n",
        ),
    ],
    ".gitignore": [
        (
            "*.bak stops being committed",
            "_export_out/\n"
            "data/solar-system/\n",
            "_export_out/\n"
            "data/solar-system/\n"
            "\n"
            "# Patch-script backups. Nine were tracked until 2026-08-29,\n"
            "# including a superseded master plan and a superseded skill. A\n"
            "# session grepping for a value can hit one and read it as current.\n"
            "*.bak\n",
        ),
    ],
}


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


def read_guarded(path, name, want_md5):
    """Read a file and refuse unless its CONTENT is what we expect.

    Returns (content, was_crlf). The style is carried so each file is
    written back the way it was found -- flipping a file's line endings
    would show in GitHub Desktop as every line changed, burying the edits
    that matter.
    """
    print("")
    print("target :", name)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return None, False
    with open(path, "rb") as handle:
        raw = handle.read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    actual = hashlib.md5(content).hexdigest()
    print("md5    : %s (expected %s)%s"
          % (actual, want_md5, "   [CRLF]" if was_crlf else ""))
    if actual != want_md5:
        print("REFUSED: %s is not in the state this patch expects." % name)
        print("         Nothing written, nothing renamed, nothing deleted.")
        return None, False
    return content, was_crlf


def main():
    print("patch_rename_runners_orrery_20260829.py -- the ORRERY half")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    new_runner_path = os.path.join(root, NEW_RUNNER)
    if os.path.exists(new_runner_path):
        print("")
        print("REFUSED: %s already exists. Either this patch has already"
              % NEW_RUNNER)
        print("         run, or there is a second copy to sort out by hand.")
        return 1

    staged = []

    # ---- verify every file first; write nothing yet -----------------
    for name in sorted(GUARDS):
        path = os.path.join(root, name)
        raw, crlf = read_guarded(path, name, GUARDS[name])
        if raw is None:
            return 1
        text = raw.decode("utf-8")
        for label, old, _new in EDITS[name]:
            count = text.count(old)
            print("  anchor x%d  %s" % (count, label))
            if count != 1:
                print("REFUSED: anchor matched %d times, expected 1." % count)
                print("         Nothing written, nothing renamed.")
                return 1
        for _label, old, new in EDITS[name]:
            text = text.replace(old, new, 1)
        out = text.encode("utf-8")
        before = sum(1 for byte in raw if byte > 127)
        after = sum(1 for byte in out if byte > 127)
        print("  non-ascii bytes: %d -> %d" % (before, after))
        if after != before:
            print("REFUSED: the patch introduced non-ASCII text.")
            return 1
        staged.append((path, name, raw, out, crlf))

    # ---- the backups: confirm they are where we think ---------------
    print("")
    missing = [name for name in BAK_FILES
               if not os.path.isfile(os.path.join(root, name))]
    for name in BAK_FILES:
        print("  %-52s %s" % (name, "gone already" if name in missing
                              else "will be deleted"))
    if missing:
        print("  %d of %d were already gone; the rest still go."
              % (len(missing), len(BAK_FILES)))

    # ---- every guard passed; now write, rename, delete ---------------
    print("")
    for path, name, raw, out, crlf in staged:
        backup = raw.replace(b"\n", b"\r\n") if crlf else raw
        final = out.replace(b"\n", b"\r\n") if crlf else out
        with open(path + ".bak", "wb") as handle:
            handle.write(backup)
        with open(path, "wb") as handle:
            handle.write(final)
        print("WROTE   %-40s (%d -> %d bytes%s)"
              % (name, len(backup), len(final), ", CRLF" if crlf else ""))

    os.rename(os.path.join(root, OLD_RUNNER), new_runner_path)
    print("RENAMED %s -> %s" % (OLD_RUNNER, NEW_RUNNER))
    # Its own .bak was just written under the old name; move it too so it
    # is not left behind as an orphan under a name nothing uses.
    old_bak = os.path.join(root, OLD_RUNNER + ".bak")
    if os.path.isfile(old_bak):
        os.rename(old_bak, new_runner_path + ".bak")

    removed = 0
    for name in BAK_FILES:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            os.remove(path)
            removed += 1
    print("DELETED %d of %d tracked .bak files" % (removed, len(BAK_FILES)))

    print("")
    print("This patch wrote fresh .bak files for the eight it edited, and")
    print("*.bak is now ignored, so git will not offer them. They are")
    print("yours to keep or delete locally.")
    print("")
    print("Next, in this order:")
    print("  1. module_atlas.py            -- rewrites MODULE_ATLAS.md")
    print("  2. orrery_maintenance_run.py  -- confirm the rename runs")
    print("  3. the dashboard              -- two new gallery buttons")
    print("")
    print("Then commit. The gallery half is a separate script:")
    print("  patch_rename_gallery_runner_20260829.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
