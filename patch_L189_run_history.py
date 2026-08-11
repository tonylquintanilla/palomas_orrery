"""
patch_L189_run_history.py -- wire the run-history module into
provenance_scanner.py (ledger L-189).

WHAT THIS DOES
    Eight anchored edits to provenance_scanner.py:
      1. import provenance_history
      2. MODULE_DOMAIN_MAP entry for the new module (dev_tools)
      3. scan_project() stamps the run start time
      4. that stamp is passed through to generate_report()
      5. generate_report() accepts it
      6. generate_report() builds this run's record and loads history
      7. a Run History table goes into PROVENANCE_AUDIT.md
      8. the run-to-run delta prints to the console; history is saved

    Nothing here touches an exit code. The delta is informational, the
    same as the Tier-1 banner it prints above.

BEFORE YOU RUN IT
    provenance_history.py must already be saved into the SAME FOLDER as
    provenance_scanner.py. This script checks and refuses if it is not
    there -- patching the import in before the module exists would leave
    the scanner unable to start.

HOW TO RUN IT
    Save this file into the palomas_orrery repo root (the folder holding
    provenance_scanner.py), open it in VS Code, and click Run.

    Or from a terminal in that folder:
        python patch_L189_run_history.py

WHAT SUCCESS LOOKS LIKE
    One "ok" line per edit, then "patch applied (N bytes)".

WHAT FAILURE LOOKS LIKE
    A single "ERROR:" line (wrong base file, or the new module missing)
    or an "ANCHOR FAIL" line naming the edit whose text was not found.
    Either way NOTHING is written and the file on disk is untouched, so
    it is always safe to re-check and run again.

Built on df7ca50f1730a40717c9f0fc22138465a5c4cef1
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

Written August 2026 with Anthropic's Claude Opus 5 (L-189).
"""

import hashlib
import os
import sys

TARGET = 'provenance_scanner.py'
COMPANION = 'provenance_history.py'

# md5 of the base file with line endings normalized to LF. Content
# fingerprint, not a raw-byte one: a Windows working copy may hold CRLF
# where the repo holds LF, and that is not an edit.
BASE_MD5 = '6c7351236c46a504556fffaefe9f535a'


EDITS = [
    (
        'import the new module',
        b"# Reuse the atlas dependency graph builder\n"
        b"from module_atlas import build_dependency_graph, classify_role\n",

        b"# Reuse the atlas dependency graph builder\n"
        b"from module_atlas import build_dependency_graph, classify_role\n"
        b"\n"
        b"# L-189: run history and run-to-run delta. Informational only --\n"
        b"# nothing imported here touches the exit code.\n"
        b"import provenance_history\n",
    ),
    (
        'MODULE_DOMAIN_MAP entry',
        b"    'provenance_scanner': 'dev_tools',\n",

        b"    'provenance_scanner': 'dev_tools',\n"
        b"    'provenance_history': 'dev_tools',\n",
    ),
    (
        'scan_project stamps the run start',
        b'    """Scan all .py files and produce the provenance audit report."""\n'
        b'    print(f"Provenance Scanner -- scanning {project_dir}")\n',

        b'    """Scan all .py files and produce the provenance audit report."""\n'
        b'    # L-189: stamped before any work, so the recorded run spans the\n'
        b'    # scan and not just the report write.\n'
        b'    run_started = provenance_history.utc_now()\n'
        b'\n'
        b'    print(f"Provenance Scanner -- scanning {project_dir}")\n',
    ),
    (
        'pass the stamp to generate_report',
        b"                    cross_check_issues=list(CROSS_CHECK_ISSUES))\n",

        b"                    cross_check_issues=list(CROSS_CHECK_ISSUES),\n"
        b"                    started=run_started)\n",
    ),
    (
        'generate_report accepts the stamp',
        b"                    deep_citations=None, shadow_constants=None,\n"
        b"                    cross_check_issues=None):\n",

        b"                    deep_citations=None, shadow_constants=None,\n"
        b"                    cross_check_issues=None, started=None):\n",
    ),
    (
        'build this run record',
        b"    kind_counts = defaultdict(int)\n"
        b"    for u in scored:\n"
        b"        kind_counts[u.kind] += 1\n"
        b"\n"
        b"    out = []\n",

        b"    kind_counts = defaultdict(int)\n"
        b"    for u in scored:\n"
        b"        kind_counts[u.kind] += 1\n"
        b"\n"
        b"    # ---- L-189: run history ----\n"
        b"    # Built here, before the report body, so the Run History table\n"
        b"    # below can include the run being written. It reaches DISK only\n"
        b"    # at the end of this function, after the audit itself is safely\n"
        b"    # written: a history write is never worth an audit.\n"
        b"    #\n"
        b"    # This walks `scored` a second time. The existing console\n"
        b"    # rollup near the end of this function walks it for a different\n"
        b"    # cut (by tier, not by file), and merging them would mean\n"
        b"    # editing working code to save one pass over an in-memory list.\n"
        b"    domain_counts = defaultdict(int)\n"
        b"    tier1_by_file = defaultdict(int)\n"
        b"    for u in scored:\n"
        b"        stem = u.file[:-3] if u.file.endswith('.py') else u.file\n"
        b"        dom, _mapped = classify_domain(stem)\n"
        b"        domain_counts[dom] += 1\n"
        b"        if action_tier(u.score) == 1:\n"
        b"            tier1_by_file[u.file] += 1\n"
        b"\n"
        b"    history = provenance_history.load_history(project_dir)\n"
        b"    run_record = provenance_history.make_run_record(\n"
        b"        started or provenance_history.utc_now(),\n"
        b"        provenance_history.utc_now(), project_dir,\n"
        b"        files_scanned, len(scored), tier_counts, domain_counts,\n"
        b"        tier1_by_file)\n"
        b"\n"
        b"    # A copy for the table, so `history` still holds the PREVIOUS\n"
        b"    # state when the console delta is computed further down.\n"
        b"    history_preview = {\n"
        b"        'schema_version': history.get('schema_version'),\n"
        b"        'expected_cadence_days': history.get('expected_cadence_days'),\n"
        b"        'max_runs': history.get('max_runs'),\n"
        b"        'runs': list(history.get('runs') or []),\n"
        b"    }\n"
        b"    provenance_history.append_run(history_preview, run_record)\n"
        b"\n"
        b"    out = []\n",
    ),
    (
        'Run History table in the audit',
        b'    # ---- Risk matrix ----\n'
        b'    out.append("## Risk Matrix: Vulnerability x Criticality")\n',

        b'    # ---- Run history (L-189) ----\n'
        b'    # Ahead of the risk matrix on purpose: the delta is the part\n'
        b'    # that changed since last time, and the matrix below it is\n'
        b'    # reference material that does not.\n'
        b'    out.extend(provenance_history.history_table(history_preview))\n'
        b'\n'
        b'    # ---- Risk matrix ----\n'
        b'    out.append("## Risk Matrix: Vulnerability x Criticality")\n',
    ),
    (
        'console delta and history save',
        b'            print(f"      {dom:<16s}{n:5d}")\n'
        b'\n'
        b'    # 1e piece 1: Tier-1 banner. INFORMATIONAL ONLY.\n',

        b'            print(f"      {dom:<16s}{n:5d}")\n'
        b'\n'
        b'    # L-189: run-to-run delta. After the priority summary and\n'
        b'    # before the Tier-1 banner, because the delta is what informs\n'
        b'    # the push call while the total above it does not. Saved last\n'
        b'    # so a failed write costs a history record, never the audit.\n'
        b'    print()\n'
        b'    for _line in provenance_history.console_lines(history, run_record):\n'
        b'        print(_line)\n'
        b'    provenance_history.append_run(history, run_record)\n'
        b'    if not provenance_history.save_history(project_dir, history):\n'
        b'        print("  WARNING: could not write "\n'
        b'              "data/provenance_history.json -- run not recorded.")\n'
        b'\n'
        b'    # 1e piece 1: Tier-1 banner. INFORMATIONAL ONLY.\n',
    ),
]


def fail(msg):
    print("ERROR: %s" % msg)
    sys.exit(1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(here, TARGET)
    companion = os.path.join(here, COMPANION)

    if not os.path.isfile(target):
        fail("%s not found next to this script. Save this script into the "
             "folder that holds %s." % (TARGET, TARGET))

    if not os.path.isfile(companion):
        fail("%s not found next to this script. Save that module into this "
             "folder first -- patching the import in before the module "
             "exists would leave the scanner unable to start." % COMPANION)

    with open(target, 'rb') as f:
        data = f.read()

    fingerprint = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if fingerprint != BASE_MD5:
        fail("base file has moved.\n"
             "       expected md5 (LF-normalized) %s\n"
             "       found                        %s\n"
             "       Nothing was written. The working copy differs from the "
             "commit this patch was built on; reconcile before applying."
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
    print("Next: run provenance_scanner.py. The first run records itself")
    print("and prints a note explaining why its totals are not comparable")
    print("to the previously committed audit.")


if __name__ == '__main__':
    main()
