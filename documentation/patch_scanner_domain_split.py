# -*- coding: utf-8 -*-
"""patch_scanner_domain_split.py -- Task 2a: show the per-domain breakdown
under each tier line in the scanner's console output, and close the two
MODULE_DOMAIN_MAP gaps.

Built on 24452442aaa64393066cac9d9b5885a763c0a76a
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file in the REPO ROOT (the folder holding
    provenance_scanner.py), open it in VS Code, and click Run.

    Success: four "ok" lines, then "patch applied".
    Failure: one "ANCHOR FAIL" or "ERROR" line followed by
    "NOTHING WAS WRITTEN". The file is left exactly as it was either way.

AFTER RUNNING
    Run provenance_scanner.py once. Expect the console to print a domain
    breakdown under each tier line. See the note below about the total.

WHAT CHANGES

  2a-1  MODULE_DOMAIN_MAP gains explicit entries for orrery_rendering and
        shell_configs. Both currently have findings but no entry, so they
        silently default to 'orrery' and are reported as a coverage gap.
        shell_configs.py is the single most important file on the
        interactive build path; it should not be in the generic bucket by
        accident.

  2a-2  Two stale MODULE_DOMAIN_MAP entries removed -- smoke_dipole_cone
        and smoke_rotation_axis. Neither file exists in the repo root any
        more (verified at this SHA).

  2a-3  Console output prints the per-domain split under each tier line.
        The full "Findings by File Type" table already exists in
        PROVENANCE_AUDIT.md; this surfaces the same data at the point the
        push-gate decision is actually made.

  2a-4  Docstring credit line.

EXPECTED SELF-SCAN EFFECT
    The scanner scans itself. Editing MODULE_DOMAIN_MAP changes a
    module-level dict inside provenance_scanner.py, so its own findings
    count can move by a small amount. That is correct behaviour, not a
    regression. Baseline immediately before this patch, measured at
    24452442: 877 findings across 118 files -- Tier 1 206, Tier 2 581,
    Tier 3 88, Tier 4 2. Compare against that, and expect any delta to
    land in the low tiers against provenance_scanner.py itself.

Patch written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'provenance_scanner.py'
BASE_MD5 = '0af5d6456421aaf133952acedd9c5832'

EDITS = [
    ('2a-1', 'MODULE_DOMAIN_MAP: add orrery_rendering + shell_configs',
     b"    'solar_visualization_shells': 'orrery',\n",
     b"    'solar_visualization_shells': 'orrery',\n"
     b"    # Added August 2026 (Task 2a): both carried findings with no\n"
     b"    # entry and defaulted to 'orrery' via the coverage-gap path.\n"
     b"    # shell_configs is on the interactive build path, so an\n"
     b"    # accidental default is the one case worth ruling out by hand.\n"
     b"    'orrery_rendering': 'orrery',\n"
     b"    'shell_configs': 'orrery',\n"),

    ('2a-2', 'MODULE_DOMAIN_MAP: drop two entries for files no longer present',
     b"    'smoke_dipole_cone': 'dev_tools',\n"
     b"    'smoke_rotation_axis': 'dev_tools',\n",
     b""),

    ('2a-3', 'console: per-domain split under each tier line',
     b'    print("Priority summary:")\n'
     b'    for tier in [1, 2, 3, 4]:\n'
     b'        score_range, action = tier_labels[tier]\n'
     b'        count = tier_counts.get(tier, 0)\n'
     b'        print(f"  Tier {tier} ({score_range}): {count:5d} '
     b'findings -- {action}")\n',

     b'    # Task 2a: the audit already carries a full "Findings by File\n'
     b'    # Type" table. This surfaces the same rollup on the console,\n'
     b'    # where the push-gate call actually gets made. Domain stays a\n'
     b'    # report-only grouping -- nothing here affects scanning or\n'
     b'    # scoring.\n'
     b'    domain_by_tier = defaultdict(lambda: defaultdict(int))\n'
     b'    for u in scored:\n'
     b'        stem = u.file[:-3] if u.file.endswith(\'.py\') else u.file\n'
     b'        dom, _mapped = classify_domain(stem)\n'
     b'        domain_by_tier[action_tier(u.score)][dom] += 1\n'
     b'\n'
     b'    print("Priority summary:")\n'
     b'    for tier in [1, 2, 3, 4]:\n'
     b'        score_range, action = tier_labels[tier]\n'
     b'        count = tier_counts.get(tier, 0)\n'
     b'        print(f"  Tier {tier} ({score_range}): {count:5d} '
     b'findings -- {action}")\n'
     b'        split = domain_by_tier.get(tier, {})\n'
     b'        for dom, n in sorted(split.items(),\n'
     b'                             key=lambda kv: (-kv[1], kv[0])):\n'
     b'            print(f"      {dom:<16s}{n:5d}")\n'),

    ('2a-4', 'docstring credit line',
     b'Role: devtool\nDomain: dev_tools\n"""',
     b'Module updated: August 2026 with Anthropic\'s Claude Opus 5 (Task 2a:\n'
     b'per-domain split printed under each console tier line;\n'
     b'MODULE_DOMAIN_MAP entries added for orrery_rendering and shell_configs,\n'
     b'and two entries removed for smoke_* files no longer in the repo.\n'
     b'Report-only grouping -- no scanning or scoring behaviour changed).\n'
     b'\nRole: devtool\nDomain: dev_tools\n"""'),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found." % TARGET)
        print("       Save this script in the REPO ROOT.")
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    norm = 0
    if b'\r\n' in data:
        norm = data.count(b'\r\n')
        data = data.replace(b'\r\n', b'\n')
        print("fix CRLF     %s: normalized %d line endings to LF" % (TARGET, norm))

    if BASE_MD5 != 'PLACEHOLDER':
        got = hashlib.md5(data).hexdigest()
        if got != BASE_MD5:
            print("ERROR: %s base does not match." % TARGET)
            print("       expected md5 %s" % BASE_MD5)
            print("       found    md5 %s" % got)
            print("       NOTHING WAS WRITTEN. Re-pull and rebuild.")
            return 1

    # Verify EVERY anchor before writing ANYTHING.
    for eid, label, old, new in EDITS:
        c = data.count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) matched %d, expected 1." % (eid, label, c))
            print("             NOTHING WAS WRITTEN. The file is unchanged.")
            print("             Fix the cause, then RE-RUN this script.")
            return 1

    for eid, label, old, new in EDITS:
        data = data.replace(old, new, 1)
        print("ok  %-6s %s" % (eid, label))

    try:
        data.decode('utf-8')
    except UnicodeDecodeError as exc:
        print("ERROR: result is not valid UTF-8 (%s)." % exc)
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'wb') as f:
        f.write(data)

    print("")
    print("patch applied%s" % (" (+%d CRLF normalized)" % norm if norm else ""))
    print("  %s" % TARGET)
    print("")
    print("Next: run provenance_scanner.py. Baseline to compare against is")
    print("877 findings / 118 files, Tier 1 206 / Tier 2 581 / Tier 3 88 /")
    print("Tier 4 2. A small delta against provenance_scanner.py's own entry")
    print("is expected -- the scanner scans itself.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
