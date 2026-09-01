"""patch_L275_1_gallery_dashboard_entries.py -- two gallery entries in the
dashboard, and a ledger block for the three that need a launcher change.

RUN COMMAND
-----------
Save into the ORRERY repo root, open in VS Code, click Run.

    python patch_L275_1_gallery_dashboard_entries.py

WHAT IT DOES
------------
Two files, all-or-nothing:

  1. palomas_orrery_dashboard.py -- two entries indented under the
     gallery maintenance runner, beneath Gallery Builder Offline Tests:
     Artifact 1 Assembler Pin and Cache Siblings. Both are Python with
     no arguments and run from the gallery repo root.

  2. LEDGER_CONSOLIDATED.md -- L-275 opened for the three Node smoke
     suites, which cannot be dashboard entries until the launcher can
     run something other than Python.

THE MEASUREMENT BEHIND IT
-------------------------
Tony asked, 2026-09-01, whether any indented tests were missing from
either runner's dashboard block. Answered by comparing each runner's
actual tool list against the dashboard's indented entries rather than by
reading:

  ORRERY   18 of 18 present. Five generators, thirteen checkers,
           nothing missing.
  GALLERY  2 of 9 present -- Module atlas and Gallery Builder Offline
           Tests. Seven absent.

Of the seven: two are Python and are added here. Three are Node and need
a launcher change (L-275). Two are correctly absent and are NOT a gap --
Served reachability and Store drift are in-process functions inside
gallery_maintenance_run.py, with no file to launch. The dashboard's
indent means "the runner covers this, and you can still run it alone",
and the second half is false for them.

Role: patch
Domain: dev_tools

Module created: September 1, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

DASH = "palomas_orrery_dashboard.py"
LEDGER = "LEDGER_CONSOLIDATED.md"

FINGERPRINTS = {
    DASH: "51ad7d9dfe9be48bf503686ed69bb22c",
    LEDGER: "6c8aedb76d92e86ef060a4a1624194ea",
}

# ---- dashboard: two entries after Gallery Builder Offline Tests ----

OLD_DASH = '''        ("Gallery Builder Offline Tests",
        "test_gallery_cache_builder_offline.py",
        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network.",
        GALLERY_TOOLS_DIR,
        True,
        None,
        True),
    ],'''

NEW_DASH = '''        ("Gallery Builder Offline Tests",
        "test_gallery_cache_builder_offline.py",
        "Offline smoke test for gallery_cache_builder.py: mocks Horizons, "
        "exercises first-build, nightly re-run, and the Guard v2 monitor path. "
        "No network.",
        GALLERY_TOOLS_DIR,
        True,
        None,
        True),
        ("Artifact 1 Assembler Pin",
        os.path.join("documentation", "pin_artifact1_known_failure.py"),
        "Runs the Artifact 1 assembler test and compares its five verdicts, "
        "and T3's feature set, against the 2026-08-31 pin. It GATES the "
        "gallery runner. Before the pin (L-237) the row printed FAIL every "
        "single run for a known reason, which made a real regression "
        "indistinguishable from the old one -- a row that always fails hides "
        "the next change behind the last. Runs from the gallery repo ROOT.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
        ("Cache Siblings",
        os.path.join("documentation", "check_cache_siblings.py"),
        "Reports the served cache's sibling directories -- the .staging_* "
        "and .quarantine_* remnants -- with each one's age taken from the "
        "run id in its NAME, and names those the builder's next run should "
        "reap. Report-only: it exits 0 whatever it finds. It exists because "
        "the builder's sweep failed silently for six weeks and nothing said "
        "so (L-274); if it goes quiet again this says so within a day. "
        "Runs from the gallery repo ROOT and deletes nothing.",
        GALLERY_REPO_DIR,
        True,
        None,
        True),
    ],'''

# ---- ledger: L-275 ----

LEDGER_ANCHOR = "#### [L-273] A document indexer, so the README's document table stops being hand-maintained"

LEDGER_BLOCK = '''#### [L-275] The dashboard cannot launch a Node tool, so three gallery smoke suites have no button
<!-- L:275 status:OPEN upd:2026-09-01 section:A flag: rice:2/2/95/2 -->
- **Found 2026-09-01, answering Tony's question about missing indented
  entries.** Measured rather than read: each runner's actual tool list
  compared against the dashboard's indented entries.
- **The orrery side is complete.** Eighteen of eighteen -- five
  generators and thirteen checkers -- all present. Nothing to do.
- **The gallery side was two of nine.** Only `Module atlas` and
  `Gallery Builder Offline Tests`. Of the seven absent, two were Python
  and were added the same evening: `pin_artifact1_known_failure.py` and
  `check_cache_siblings.py`.
- **THE ITEM IS THE REMAINING THREE, and they are blocked on the
  launcher, not on anyone's attention.** `documentation/smoke_features.js`,
  `documentation/smoke_framing.js` and `documentation/smoke_sun_shells.js`
  are Node. `palomas_orrery_dashboard.py` builds every launch command as
  `[sys.executable, script_path] + args`, so it can only run Python. A
  Node entry needs the launch path to dispatch on file extension, plus a
  clear message when Node is absent -- the same UNREACHABLE state
  `gallery_maintenance_run.py` already models, and it should say the same
  thing rather than inventing a second vocabulary for it.
- **Deferred deliberately, Tony's call 2026-09-01.** The launcher change
  touches the code path every button in the dashboard uses, and the file
  had just been committed at the end of a long session. The three suites
  already run inside the gallery runner, which is where they gate; the
  dashboard entry is convenience, not coverage.
- **TWO MORE ARE ABSENT AND MUST STAY ABSENT. This is a ruling, not a
  backlog.** `Served reachability` and `Store drift` are in-process
  Python FUNCTIONS inside `gallery_maintenance_run.py`, reached through
  its `LIVE_CHECKERS` list. They have no file to launch. The dashboard's
  indent means two things at once -- the runner covers this, AND you can
  still run it alone -- and the second is false for them. An entry would
  be a button that cannot exist. Recorded here so a later session
  counting nine against seven does not read it as a gap and try to close
  it.
- **Claude:** RICE 2/2/95/2 -> 1.9 proposed, not confirmed. Reach 2 and
  Impact 2 because it is convenience over an existing gate; Effort 2
  because the launcher change is small but sits under every button.
- **Ref:** L-237 (the Artifact 1 pin); L-274 (the sibling checker);
  L-236 (the gallery runner); A Report Names Its Items, resident
  protocol Part 3 -- the two correctly-absent entries are named here
  precisely so the count does not mislead.

'''


def fail(msg):
    print("")
    print("FAILURE: " + msg)
    print("NOTHING was written.")
    print("Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def read_norm(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    return raw.replace(b"\r\n", b"\n"), b"\r\n" in raw


def main():
    if not os.path.isfile("PROJECT_INSTRUCTIONS.md"):
        fail("run this from the ORRERY repo root (the folder holding "
             "PROJECT_INSTRUCTIONS.md). Current folder: " + os.getcwd())

    loaded = {}
    for path, want in sorted(FINGERPRINTS.items()):
        if not os.path.isfile(path):
            fail(path + " not found in " + os.getcwd())
        content, was_crlf = read_norm(path)
        got = hashlib.md5(content).hexdigest()
        if got != want:
            fail("BASE MOVED. " + path + " fingerprints " + got +
                 ", expected " + want + ".\n"
                 "  Establish WHAT differs before assuming an edit was made:\n"
                 "  a size delta of about one byte per line means line\n"
                 "  endings, not content.")
        loaded[path] = (content.decode("utf-8", "strict"), was_crlf)
    print("ok  2/2 base fingerprints match")

    dash_text = loaded[DASH][0]
    ledger_text = loaded[LEDGER][0]

    if '"Artifact 1 Assembler Pin"' in dash_text:
        fail("the dashboard already has an Artifact 1 Assembler Pin entry.")
    if "L-275" in ledger_text:
        fail("the ledger already mentions L-275.")

    for label, text, anchor in (("dashboard", dash_text, OLD_DASH),
                                ("ledger", ledger_text, LEDGER_ANCHOR)):
        n = text.count(anchor)
        if n != 1:
            fail("the %s anchor appears %d times, expected exactly 1."
                 % (label, n))
    print("ok  2/2 anchors found, each exactly once")

    new_dash = dash_text.replace(OLD_DASH, NEW_DASH, 1)
    new_ledger = ledger_text.replace(LEDGER_ANCHOR,
                                     LEDGER_BLOCK + LEDGER_ANCHOR, 1)

    for chunk in (NEW_DASH, LEDGER_BLOCK):
        bad = [c for c in chunk if ord(c) > 127]
        if bad:
            fail("inserted text holds %d non-ASCII character(s)." % len(bad))
    print("ok  inserted text is ASCII")

    for path, text in ((DASH, new_dash), (LEDGER, new_ledger)):
        out = text.encode("utf-8")
        if loaded[path][1]:
            out = out.replace(b"\n", b"\r\n")
        with open(path, "wb") as fh:
            fh.write(out)
        print("ok  wrote %s (%d bytes)" % (path, len(out)))

    # ---- verification: read back from disk ----
    problems = []

    back, _ = read_norm(DASH)
    dt = back.decode("utf-8", "replace")
    for probe, why in (('"Artifact 1 Assembler Pin"', "Artifact 1 entry missing"),
                       ('"Cache Siblings"', "Cache Siblings entry missing"),
                       ('"pin_artifact1_known_failure.py"', "pin script not referenced"),
                       ('"check_cache_siblings.py"', "siblings script not referenced")):
        if dt.count(probe) != 1:
            problems.append(why)
    # Position: both must sit between the existing gallery indented entry
    # and the Developer Tools section, not merely exist somewhere.
    try:
        i_prev = dt.index('"Gallery Builder Offline Tests"')
        i_pin = dt.index('"Artifact 1 Assembler Pin"')
        i_sib = dt.index('"Cache Siblings"')
        i_next = dt.index('"Developer Tools"')
        if not (i_prev < i_pin < i_sib < i_next):
            problems.append("the two entries are not inside the gallery "
                            "indented block")
    except ValueError:
        problems.append("could not locate the surrounding entries")

    back, _ = read_norm(LEDGER)
    lt = back.decode("utf-8", "replace")
    if lt.count("<!-- L:275 status:OPEN") != 1:
        problems.append("L-275 metadata line not present exactly once")
    if lt.count("#### [L-275] The dashboard cannot launch a Node tool") != 1:
        problems.append("L-275 header not present exactly once")
    if lt.count("#### [L-273] A document indexer") != 1:
        problems.append("L-273's block was disturbed")

    import py_compile
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        try:
            py_compile.compile(DASH, doraise=True,
                               cfile=os.path.join(td, "d.pyc"))
        except py_compile.PyCompileError as e:
            problems.append("dashboard does not compile: %s" % e)

    if problems:
        print("")
        print("VERIFICATION FAILED after writing:")
        for p in problems:
            print("  - " + p)
        print("Undo is Discard Changes in GitHub Desktop.")
        sys.exit(1)

    print("ok  verified: 2 entries positioned in the gallery block, L-275 "
          "opened, dashboard compiles")
    print("")
    print("patch applied.")
    print("")
    print("NEXT STEPS")
    print("  1. Run: python palomas_orrery_dashboard.py")
    print("     Artifact 1 Assembler Pin and Cache Siblings should appear")
    print("     indented under the gallery maintenance runner.")
    print("  2. Run: python orrery_maintenance_run.py")
    print("  3. Commit and push.")
    print("")
    print("The gallery dashboard block is now 4 of 9. L-275 carries the")
    print("three Node suites; the remaining two are ruled permanently")
    print("absent in that block, with the reason, so the count does not")
    print("read as a gap later.")


if __name__ == "__main__":
    main()
