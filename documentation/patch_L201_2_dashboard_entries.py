"""patch_L201_2_dashboard_entries.py -- L-201.

SUPERSEDES patch_L201_2_dashboard_builder_entry.py. Delete that file and
run this one instead; it does everything that one did, plus four more
entries. If you already RAN the earlier patch, this will abort on the
fingerprint check and say so -- tell me and I will re-cut it against the
patched tree.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
palomas_orrery_dashboard.py), open it in VS Code, and click Run.

    python patch_L201_2_dashboard_entries.py

Success prints one `ok` line per file and then `patch applied`.
Failure prints a single ERROR or ANCHOR FAIL line and writes NOTHING.

WHAT IT DOES
------------
1. palomas_orrery_dashboard.py gains a "Worksheet Request Builder"
   launch card in Developer Tools, placed immediately after the
   indented maintenance-runner group and NOT indented, because the
   builder is not a checker and the runner does not cover it. It is
   marked interactive, so it opens in its own console window.

2. worksheet_request_builder.py's RUNNING IT block is corrected. It
   said the tool asks for a batch name and writes one file. Measured
   at HEAD, it asks three questions and writes two files. The stale
   text predates both the selection mechanism (L-201) and the JSON
   emitter (L-202); the docstring did not move with them.

3. The two generator cards are swapped into runner order: the
   dashboard listed Data Inventory before Module Atlas, the runner runs
   Module Atlas first. After this patch, reading down the indented
   group tells you exactly what maintenance_run.py does, generators and
   checkers alike.

4. Four runner-covered checkers that were missing from the dashboard
   are added to the indented group:

       constants_change_report.py        (Constants change)
       test_worksheet_keys.py            (Worksheet key round trip)
       test_worksheet_request_builder.py (Builder marker join)
       test_extractor_pins.py            (Extractor pins)

   Tony's ruling of 2026-08-12 was that a tool the maintenance runner
   covers stays visible as its own indented card, because staying
   visible is how the automation's contents remain known instead of
   disappearing behind one button. Four of thirteen had gone missing,
   which is the drift that ruling exists to prevent. They are inserted
   in RUNNER ORDER, so after this patch the indented group reads in
   the same sequence maintenance_run.py executes -- thirteen cards
   against thirteen CHECKERS rows, countable side by side.

The selection prompt's default is called out in both the card and the
docstring on purpose. It defaults to 1, the whole corpus, so pressing
Enter at that prompt produces a 100-row request rather than the 23-row
pilot slice -- a mistake that is silent, since a 100-row request looks
exactly like a working tool.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable and one-shot. Permanent: the five dashboard
entries and the corrected docstring.

Module created: August 17, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys


FINGERPRINTS = {
    'palomas_orrery_dashboard.py': 'b479da043ced5cb6df3566cff4d9f56a',
    'worksheet_request_builder.py': 'dd731de4da81dceed41aa4cfd383df0d',
}


# ---- edit 1: the two generator cards, swapped into runner order -----
#
# The dashboard listed Data Inventory before Module Atlas; the runner
# executes Module Atlas first. Nothing depends on the order -- both are
# generators and both run every time -- but with the checker half now
# mirroring the runner exactly, this was the only place left where
# reading down the dashboard did not tell you what the runner does.

GENERATOR_ORDER_ANCHOR = '''        ("Data Inventory",
         "data_inventory.py",
         "Inventory the large, gitignored data stores (data/, star_data/). "
         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Regenerate Module Atlas",
         "module_atlas.py",
         "Scan codebase, generate MODULE_ATLAS.md. "
         "Run after significant codebase changes (new modules, reorganizations).",
         SCRIPT_DIR,
         True,
         None,
         True),'''

GENERATOR_ORDER_ENTRY = '''        ("Regenerate Module Atlas",
         "module_atlas.py",
         "Scan codebase, generate MODULE_ATLAS.md. "
         "Run after significant codebase changes (new modules, reorganizations).",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Data Inventory",
         "data_inventory.py",
         "Inventory the large, gitignored data stores (data/, star_data/). "
         "Writes DATA_INVENTORY.md. Run before handoffs or to check cache state.",
         SCRIPT_DIR,
         True,
         None,
         True),'''


# ---- edit 2: Constants change, ahead of the constants test ----------

CONSTANTS_CHANGE_ANCHOR = '''        ("Test Constants Provenance",'''

CONSTANTS_CHANGE_ENTRY = '''        ("Constants Change Report",
         "constants_change_report.py",
         "Ask git what changed in constants_new.py since the last commit "
         "and report each moved value in words. The line that matters "
         "says whether the provenance moved WITH the number: a deliberate "
         "correction edits the value and its comment block together, "
         "while corruption -- a bad merge, a stray keystroke, a copied "
         "stale value -- moves the number alone and leaves the evidence "
         "describing the old one. Run before committing a change to "
         "constants_new.py.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Test Constants Provenance",'''


# ---- edit 3: the three worksheet checkers, in runner order ----------

WORKSHEET_TRIO_ANCHOR = '''        ("Provenance Scanner",
         "provenance_scanner.py",
         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "
         "Run before/after edits to shared values, or when a value looks suspicious.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Dependency Trace",'''

WORKSHEET_TRIO_ENTRY = '''        ("Worksheet Key Round Trip",
         "test_worksheet_keys.py",
         "Assert that every annotated site mints a key that resolves back "
         "to it, on every run. A rename breaks it, a split implementation "
         "between the builder and the checker breaks it, and a change to "
         "the enclosing-name rule breaks it -- all three loudly, at the "
         "commit that introduced them, rather than months later when a "
         "returned worksheet will not bind.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Builder Marker Join",
         "test_worksheet_request_builder.py",
         "Test that a citation continued onto a marked second line "
         "(`# Source+:` under `# Source:`) is joined back before the "
         "request quotes it. Every behaviour is exercised twice, once "
         "with input that should join and once with input that must NOT: "
         "a join firing on everything is indistinguishable from a join "
         "firing correctly, and both report zero problems, so the "
         "negative cases are the test. The last check runs against the "
         "real corpus. Run after editing the builder or relabeling a "
         "continuation.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Extractor Pins",
         "test_extractor_pins.py",
         "Pin the instruction filter's kept-and-dropped set at "
         "LOOKBACK 30 / LOOKAHEAD 25, frozen 2026-08-14. The claim "
         "ordinal in every issued key -- the `::c2` -- counts claims "
         "AFTER this filter runs, so extending the instruction pattern "
         "by one phrase lets a formerly-dropped number join the sequence "
         "and shifts every ordinal after it with no prose edit at all. A "
         "worksheet returned against the old ordinals would then bind to "
         "the wrong claim. It does not decide whether a change is wrong; "
         "it reports that the extractor no longer means what the issued "
         "keys assume, and prints the replacement pin file.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Provenance Scanner",
         "provenance_scanner.py",
         "Scan for hardcoded constants and duplicates. Writes PROVENANCE_AUDIT.md. "
         "Run before/after edits to shared values, or when a value looks suspicious.",
         SCRIPT_DIR,
         True,
         None,
         True),
        ("Worksheet Request Builder",
         "worksheet_request_builder.py",
         "Write the cross-check request that goes OUT to a reader. The "
         "checker reads what comes back; this writes what is sent. Opens "
         "in its own console because it asks three questions, in this "
         "order. WHICH ROWS -- a numbered list of named selections; it "
         "DEFAULTS TO 1, the whole corpus, so type the number you want "
         "rather than pressing Enter (2 is constants_new.py, the 23-row "
         "pilot slice). BATCH NAME -- becomes the filename. ANCHOR SHA -- "
         "the commit the request describes; use current HEAD, and re-run "
         "if you commit anything before sending it, because a returned "
         "row is checked against this SHA. It writes "
         "REQUEST_<batch>.jsonl and REQUEST_<batch>.md into "
         "documentation/worksheets/ and refuses rather than overwriting "
         "if either name is taken. Send the .jsonl; the .md is the "
         "fallback if a return will not parse. It judges nothing -- "
         "reading the returns is Worksheet Checker, above.",
         SCRIPT_DIR,
         True),
        ("Dependency Trace",'''


# ---- edit 4: the builder's own run instructions ---------------------

BUILDER_DOCSTRING_ANCHOR = '''RUNNING IT

Open in VS Code and press Run. It asks for a batch name and writes one
file into documentation/worksheets/. No command-line flags.
"""'''

BUILDER_DOCSTRING = '''RUNNING IT

Open in VS Code and press Run. No command-line flags; it asks three
questions in the console, in this order.

  1. WHICH ROWS. A numbered list of the named selections defined in
     this module. The prompt DEFAULTS TO 1 -- the whole corpus -- so
     pressing Enter here produces a request over every annotated row
     rather than the slice you meant. Type the number.
  2. BATCH NAME. Becomes the filename, and is recorded in the request
     header.
  3. ANCHOR SHA. The commit this request describes. A returned row is
     checked against it later, so it must be current HEAD at the
     moment of the run -- commit something afterwards and re-run.

It writes TWO files into documentation/worksheets/, both rendered from
the same Request list so there is no second source of truth:

    REQUEST_<batch>.jsonl   what goes out
    REQUEST_<batch>.md      the fallback, if a return will not parse

It refuses rather than overwriting if either name already exists, and
it refuses to write at all if a selection matches no rows -- an empty
worksheet is indistinguishable from a finished one once it is out of
the room.

It is also a launch card in palomas_orrery_dashboard.py, under
Developer Tools, which opens it in its own console window.
"""'''


PLAN = [
    ('palomas_orrery_dashboard.py', [
        (GENERATOR_ORDER_ANCHOR, GENERATOR_ORDER_ENTRY),
        (CONSTANTS_CHANGE_ANCHOR, CONSTANTS_CHANGE_ENTRY),
        (WORKSHEET_TRIO_ANCHOR, WORKSHEET_TRIO_ENTRY),
    ]),
    ('worksheet_request_builder.py', [
        (BUILDER_DOCSTRING_ANCHOR, BUILDER_DOCSTRING),
    ]),
]


def fingerprint(data):
    """Content fingerprint: line endings normalized before hashing."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def non_ascii(data):
    return [b for b in data if b > 127]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    for name, _edits in PLAN:
        if not os.path.isfile(name):
            print('ERROR: %s not found. Run this from the repo root.' % name)
            return 1
        with open(name, 'rb') as handle:
            data = handle.read()
        seen = fingerprint(data)
        want = FINGERPRINTS[name]
        if seen != want:
            print('ERROR: %s has moved. Expected %s, found %s.'
                  % (name, want, seen))
            print('       Nothing written. Built against '
                  '6c06b3f8a6dadcb321e84c28d6285cca7d4e46b1. If you already')
            print('       ran patch_L201_2_dashboard_builder_entry.py, say '
                  'so -- this needs re-cutting against that tree.')
            return 1

    staged = {}
    notes = []
    for name, edits in PLAN:
        with open(name, 'rb') as handle:
            data = handle.read()
        is_crlf = data.count(b'\r\n') > 0
        content = data
        for old, new in edits:
            old_b = old.encode('utf-8')
            new_b = new.encode('utf-8')
            if non_ascii(new_b):
                print('ERROR: this patch would insert non-ASCII bytes into '
                      '%s. Nothing written.' % name)
                return 1
            if is_crlf:
                old_b = old_b.replace(b'\n', b'\r\n')
                new_b = new_b.replace(b'\n', b'\r\n')
            count = content.count(old_b)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d for:'
                      % (name, count))
                print('   %s' % old.splitlines()[0][:70])
                print('Nothing written.')
                return 1
            content = content.replace(old_b, new_b)
        left = non_ascii(content)
        if left:
            notes.append('note: %s still holds %d non-ASCII byte(s) this '
                         'patch did not reach' % (name, len(left)))
        staged[name] = content

    written = 0
    for name, edits in PLAN:
        with open(name, 'wb') as handle:
            handle.write(staged[name])
        written += len(staged[name])
        print('ok  %s (%d edit%s)'
              % (name, len(edits), '' if len(edits) == 1 else 's'))

    for note in notes:
        print(note)
    print('patch applied (%d bytes across %d files)' % (written, len(PLAN)))
    print('')
    print('Next: launch the dashboard. Developer Tools should show 4')
    print('      generator cards then 13 checker cards under MAINTENANCE')
    print('      RUN, in the same order maintenance_run.py executes them,')
    print('      with Worksheet Request Builder un-indented below.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
