"""
patch_L060_3_title_flag_20261117.py -- the night's EL NINO DUE flag is
read from the El Nino check's own row only (L-060).

Built on orrery 74720b62514ff0c209de9d87aac3011adedc3461 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), read
Nov 17, 2026, 11:30 Chicago. Written by the coordinating session (Claude
Opus 5.5) under safe-file-editing 1.14 and agentic-pre-test 1.3.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
and gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHAT WENT WRONG

The orrery's night of Nov 17 (commit c69b53b) titled itself "EL NINO
DUE" although its El Nino check row said CURRENT. night_title_flags()
looked for the words in EVERY row's verdict, and the El Nino check
SUITE's pass line describes its own test cases ("... each flag EL NINO
DUE ..."). So every clean night would say EL NINO DUE, and the flag would
mean nothing.

WHAT IT CHANGES (two files)

    orrery_maintenance_run.py: NIGHT_TITLE_FLAGS pairs each flag with
      the one row that may raise it, ('El Nino check', 'EL NINO DUE');
      night_title_flags() reads only that row's verdict.
    test_enso_night_check.py: one more title case, the night of Nov 17
      itself: the check says CURRENT and the suite's pass line mentions
      EL NINO DUE; the title must carry no flag.

    Each edit is checked at the text it replaces; a file that already
    holds the result is reported and left alone.

RUN COMMAND

    Save in the orrery's root folder, open in VS Code, click Run.
    (python patch_L060_3_title_flag_20261117.py)

    It then runs the El Nino check suite itself. Success: "ok" lines,
    the suite's PASS line, then "patch applied". Failure: one ERROR or
    ANCHOR FAIL line, and nothing is written.

Written November 17, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

RUNNER = "orrery_maintenance_run.py"
SUITE = "test_enso_night_check.py"

RUNNER_EDITS = [
    ("the flag list pairs each flag with its row",
     b"# Nino check says EL NINO DUE when NOAA has newer than the page shows.\n"
     b"NIGHT_TITLE_FLAGS = ('EL NINO DUE',)\n",
     b"# Nino check says EL NINO DUE when NOAA has newer than the page shows.\n"
     b"# Each flag is read from its OWN row only (L-060, Nov 17): the El Nino\n"
     b"# check suite's pass line names EL NINO DUE when it describes its test\n"
     b"# cases, and the night of Nov 17 (c69b53b) took that for the flag.\n"
     b"NIGHT_TITLE_FLAGS = (('El Nino check', 'EL NINO DUE'),)\n"),
    ("night_title_flags reads only the flag's own row",
     b"    NIGHT_TITLE_FLAGS that a row's verdict carries, followed by a space;\n"
     b"    '' when none does or the record cannot be read.\"\"\"\n",
     b"    NIGHT_TITLE_FLAGS whose own row's verdict carries it, followed by a\n"
     b"    space; '' when none does or the record cannot be read. Another\n"
     b"    row's words never raise a flag.\"\"\"\n"),
    ("night_title_flags matches by row",
     b"    found = [flag for flag in NIGHT_TITLE_FLAGS\n"
     b"             if any(flag in (row.get('verdict') or '') for row in rows)]\n",
     b"    found = [flag for label, flag in NIGHT_TITLE_FLAGS\n"
     b"             if any(row.get('row') == label\n"
     b"                    and flag in (row.get('verdict') or '')\n"
     b"                    for row in rows)]\n"),
]

SUITE_EDITS = [
    ("the night of Nov 17 as a title case",
     b"        for verdict, want_title in (\n"
     b"                (\"EL NINO DUE -- NOAA has newer\", \"EL NINO DUE \"),\n"
     b"                (\"CURRENT -- the page shows NOAA's latest\", \"\")):\n"
     b"            with open(os.path.join(tmpr, runner.NIGHT_RECORD), \"w\") as fh:\n"
     b"                json.dump({\"rows\": [{\"row\": \"El Nino check\",\n"
     b"                                     \"verdict\": verdict}]}, fh)\n",
     b"        # The third case is the night of Nov 17 (c69b53b): the check\n"
     b"        # says CURRENT and this suite's own pass line names EL NINO DUE.\n"
     b"        suite_line = (\"PASS -- 21 checks: ... each flag EL NINO DUE and \"\n"
     b"                      \"save the copies once\")\n"
     b"        for verdict, want_title, extra in (\n"
     b"                (\"EL NINO DUE -- NOAA has newer\", \"EL NINO DUE \", []),\n"
     b"                (\"CURRENT -- the page shows NOAA's latest\", \"\", []),\n"
     b"                (\"CURRENT -- the page shows NOAA's latest\", \"\",\n"
     b"                 [{\"row\": \"El Nino check suite\",\n"
     b"                   \"verdict\": suite_line}])):\n"
     b"            with open(os.path.join(tmpr, runner.NIGHT_RECORD), \"w\") as fh:\n"
     b"                json.dump({\"rows\": [{\"row\": \"El Nino check\",\n"
     b"                                     \"verdict\": verdict}] + extra}, fh)\n"),
]


def plan(path, edits):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % path)
        return False, None
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw
    text = raw.replace(b"\r\n", b"\n")
    if all(text.count(new) == 1 for _, _, new in edits):
        print("already there, identical: %s" % path)
        return True, None
    for label, old, new in edits:
        n = text.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found %d. "
                  "Nothing was written." % (label, path, n))
            return False, None
        text = text.replace(old, new)
        print("ok %s" % label)
    if any(c > 127 for c in b"".join(new for _, _, new in edits)):
        print("ERROR: non-ASCII in this patch's text. Nothing was written.")
        return False, None
    if crlf:
        text = text.replace(b"\n", b"\r\n")
    return True, text


def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    ok1, runner = plan(RUNNER, RUNNER_EDITS)
    ok2, suite = plan(SUITE, SUITE_EDITS)
    if not (ok1 and ok2):
        return 1
    for path, out in ((RUNNER, runner), (SUITE, suite)):
        if out is not None:
            with open(path, "wb") as f:
                f.write(out)
            print("ok %s written" % path)
    for path in (RUNNER, SUITE):
        r = subprocess.run([sys.executable, "-m", "py_compile", path],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("ERROR: %s does not compile: %s" % (path, r.stderr.strip()))
            return 1
    print("Running the El Nino check suite ...")
    r = subprocess.run([sys.executable, SUITE], capture_output=True, text=True)
    lines = (r.stdout + r.stderr).strip().splitlines()
    for line in lines[-2:]:
        print("  " + line)
    if r.returncode != 0:
        print("ERROR: the suite failed. Discard Changes in GitHub Desktop "
              "undoes this patch; paste these lines to the session.")
        return 1
    print("patch applied")
    print("")
    print("Do next:")
    print("  1. (do) Move this file into documentation\\.")
    print("  2. (do) In GitHub Desktop (orrery): commit and push the two files "
          "and this patch. Not between 07:17 and 11:17 UTC (1:17 to 5:17 "
          "Chicago), when the night runs.")
    print("  3. (do) Tomorrow morning: the orrery's night title should NOT "
          "start with EL NINO DUE (NOAA's next update is due 10 December).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
