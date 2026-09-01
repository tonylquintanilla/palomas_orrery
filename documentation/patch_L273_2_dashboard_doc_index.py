"""patch_L273_2_dashboard_doc_index.py -- add Document Index to the
dashboard, and remove two counts that had already gone stale.

RUN COMMAND
-----------
Save into the ORRERY repo root, open in VS Code, click Run.

    python patch_L273_2_dashboard_doc_index.py

WHAT IT DOES
------------
Three edits to palomas_orrery_dashboard.py, all-or-nothing:

  1. A "Document Index" entry indented under MAINTENANCE RUN, beneath
     Data Inventory, matching the shape of the other four generators.
     Tony's request, 2026-09-01.

  2. The MAINTENANCE RUN description said it "regenerates the four
     generated documents". It is five as of tonight. The count is
     removed rather than corrected to 5: the number was wrong within a
     day of being written, and the runner prints the real list every
     time it runs.

  3. The gallery runner description said "the 149-check cache builder
     suite". It is 158 as of tonight, and it will move again the next
     time anyone adds a pin. Same treatment, same reason.

WHY REMOVE THE COUNTS RATHER THAN UPDATE THEM
---------------------------------------------
Both numbers were correct when typed and both were stale within a day.
A count in a tool DESCRIPTION is a hand-maintained copy of something the
tool itself reports accurately at run time -- the same shape as the
README's sixteen hardcoded counts removed under L-270, and the same
answer: name the thing, let the tool carry the number.

Nothing else in this file holds a hardcoded count. That was checked, not
assumed.

WHAT IS PERMANENT
-----------------
The dashboard changes. This script is one-shot; archive it into
documentation/ once it has run.

NO BACKUP FILE
--------------
Per safe-file-editing 1.10.

Role: patch
Domain: dev_tools

Module created: September 1, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = "palomas_orrery_dashboard.py"
TARGET_MD5 = "fa3f601934b5e9624abbc6fff40d36f5"

EDITS = []

# ---- 1: the new entry, after Data Inventory ----
EDITS.append((
    "Document Index entry",
    '''        ("Data Inventory",
         "data_inventory.py",
         "Inventory the large, gitignored data stores (data/, star_data/). "
         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",
         SCRIPT_DIR,
         True,
         None,
         True),''',
    '''        ("Data Inventory",
         "data_inventory.py",
         "Inventory the large, gitignored data stores (data/, star_data/). "
         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Document Index",
         "doc_index.py",
         "Regenerate the key-documents table in README.md from the "
         "one-line Doc-Kind tag each root document carries. The purpose "
         "text lives in the document it describes, not in this tool and "
         "not in the README, so the wording stays yours while the table "
         "stays generated. Three kinds: generated (never hand-edit -- the "
         "next run destroys the edit), zoned (hand-written prose around a "
         "marker zone a tool rewrites), and hand. A document with no tag "
         "is listed as untagged and named in the summary rather than "
         "quietly dropped. Run after adding, renaming, or retiring a root "
         "document; --check reports staleness without writing.",
         SCRIPT_DIR,
         True,
         None,
         True),''',
))

# ---- 2: the stale generator count ----
EDITS.append((
    "maintenance run description count",
    '''         "One command for the whole routine: regenerates the four generated "
         "documents, then runs every checker, then prints one summary. It "''',
    '''         "One command for the whole routine: regenerates the generated "
         "documents, then runs every checker, then prints one summary. It "''',
))

# ---- 3: the stale gallery suite count ----
EDITS.append((
    "gallery suite count",
    '''        "Regenerates the module atlas, then runs the 149-check cache "
        "builder suite, the three Node smoke suites, and the artifact-1 "''',
    '''        "Regenerates the module atlas, then runs the cache "
        "builder suite, the three Node smoke suites, and the artifact-1 "''',
))


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
    if not os.path.isfile(TARGET):
        fail(TARGET + " not found in " + os.getcwd())
    if not os.path.isfile("doc_index.py"):
        fail("doc_index.py not found. Run patch_L273_1_doc_index.py first; "
             "this adds a dashboard entry for a tool that must exist.")

    content, was_crlf = read_norm(TARGET)
    actual = hashlib.md5(content).hexdigest()
    if actual != TARGET_MD5:
        fail("BASE MOVED. " + TARGET + " fingerprints " + actual +
             ", expected " + TARGET_MD5 + ".\n"
             "  Establish WHAT differs before assuming an edit was made: a\n"
             "  size delta of about one byte per line means line endings,\n"
             "  not content.")
    print("ok  base fingerprint matches" +
          (" [CRLF, normalised]" if was_crlf else ""))

    text = content.decode("utf-8", "strict")

    if '"Document Index"' in text:
        fail("the dashboard already has a Document Index entry.")

    for label, old, new in EDITS:
        n = text.count(old)
        if n != 1:
            fail("anchor for %s appears %d times, expected exactly 1."
                 % (label, n))
    print("ok  %d/%d anchors found, each exactly once" % (len(EDITS), len(EDITS)))

    for label, old, new in EDITS:
        text = text.replace(old, new, 1)

    bad = [c for c in text if ord(c) > 127]
    if bad:
        fail("result would hold %d non-ASCII character(s)." % len(bad))

    out = text.encode("utf-8")
    if was_crlf:
        out = out.replace(b"\n", b"\r\n")
    with open(TARGET, "wb") as fh:
        fh.write(out)
    print("ok  wrote %s (%d bytes)" % (TARGET, len(out)))

    # ---- verification: read back from disk ----
    back, _ = read_norm(TARGET)
    got = back.decode("utf-8", "replace")
    problems = []

    if got.count('"Document Index"') != 1:
        problems.append("Document Index entry not present exactly once")
    if got.count('"doc_index.py"') != 1:
        problems.append("doc_index.py not referenced exactly once")
    if "the four generated " in got:
        problems.append("the stale generator count survived")
    if "149-check" in got:
        problems.append("the stale gallery suite count survived")
    # The entry must sit INSIDE the indented block, i.e. after Data
    # Inventory and before the first checker. Position, not just presence.
    try:
        i_data = got.index('"Data Inventory"')
        i_doc = got.index('"Document Index"')
        i_next = got.index('"Constants Change Report"')
        if not (i_data < i_doc < i_next):
            problems.append("Document Index is not between Data Inventory "
                            "and Constants Change Report")
    except ValueError:
        problems.append("could not locate the surrounding entries")

    import py_compile
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        try:
            py_compile.compile(TARGET, doraise=True,
                               cfile=os.path.join(td, "d.pyc"))
        except py_compile.PyCompileError as e:
            problems.append("does not compile: %s" % e)

    if problems:
        print("")
        print("VERIFICATION FAILED after writing:")
        for p in problems:
            print("  - " + p)
        print("Undo is Discard Changes in GitHub Desktop.")
        sys.exit(1)

    print("ok  verified: entry present once, positioned under MAINTENANCE "
          "RUN, both stale counts gone, compiles")
    print("")
    print("patch applied.")
    print("")
    print("NEXT STEPS")
    print("  1. Run: python palomas_orrery_dashboard.py")
    print("     Document Index should appear indented under MAINTENANCE")
    print("     RUN, below Data Inventory.")
    print("  2. Run: python orrery_maintenance_run.py")
    print("  3. Commit and push.")


if __name__ == "__main__":
    main()
