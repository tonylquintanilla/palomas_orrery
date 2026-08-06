# -*- coding: utf-8 -*-
"""patch_skills_index_drift_report.py -- report what the manifest was advertising before overwriting it

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file in the REPO ROOT, open it in VS Code, click Run.
    All anchors are verified before anything is written; on failure
    nothing is touched.

AFTER RUNNING: the next skills_index.py run prints either
    "Manifest already matched all N skills." or a MANIFEST WAS STALE
    block naming each drifted skill.
"""

import os
import sys

EDITS = [
    ('skills_index.py', 'SIX-1', 'drift report before regeneration',
     b"    manifest = build_manifest(records)\n    new = re.sub(re.escape(START) + r'.*?' + re.escape(END),\n                 lambda _m: manifest, text, flags=re.DOTALL)",
     b'    manifest = build_manifest(records)\n\n    # Drift report (August 2026): name what the manifest was advertising\n    # BEFORE overwriting it. Regenerating silently is how three weeks of\n    # stale versions went unnoticed -- running the tool made the evidence\n    # disappear at the same moment it fixed the problem.\n    old_zone = re.search(re.escape(START) + r\'(.*?)\' + re.escape(END),\n                         text, flags=re.DOTALL)\n    if old_zone:\n        was = dict(re.findall(r\'^([a-z0-9][a-z0-9-]*)\\s+(\\S+)\\s\',\n                              old_zone.group(1), flags=re.M))\n        drift = [(r[\'name\'], was[r[\'name\']], r[\'version\'])\n                 for r in records\n                 if r[\'name\'] in was and was[r[\'name\']] != r[\'version\']]\n        missing = [r[\'name\'] for r in records if r[\'name\'] not in was]\n        dropped = [n for n in was if n not in {r[\'name\'] for r in records}]\n        if drift or missing or dropped:\n            print("MANIFEST WAS STALE -- corrected below:")\n            for name, old_v, new_v in drift:\n                print(f"  - {name}: manifest said {old_v}, SKILL.md says {new_v}")\n            for name in missing:\n                print(f"  - {name}: missing from the manifest entirely")\n            for name in dropped:\n                print(f"  - {name}: in the manifest but no longer a skill folder")\n            print("  Commit the protocol copies together with the SKILL.md")\n            print("  change -- see the binding rule in ledger-and-session-records.")\n        else:\n            print(f"Manifest already matched all {len(records)} skills.")\n\n    new = re.sub(re.escape(START) + r\'.*?\' + re.escape(END),\n                 lambda _m: manifest, text, flags=re.DOTALL)'),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    files = {}
    for rel, eid, label, old, new in EDITS:
        path = os.path.join(root, rel.replace('/', os.sep))
        if rel not in files:
            if not os.path.exists(path):
                print("ERROR: %s not found. Save this in the repo root." % rel)
                return 1
            with open(path, 'rb') as f:
                files[rel] = f.read()
            if b'\r\n' in files[rel]:
                print("ERROR: %s has CRLF line endings." % rel)
                return 1

    for rel, eid, label, old, new in EDITS:
        n = files[rel].count(old)
        if n != 1:
            print("ANCHOR FAIL: %s (%s) in %s matched %d, expected 1." % (eid, label, rel, n))
            print("             Nothing written.")
            return 1

    for rel, eid, label, old, new in EDITS:
        files[rel] = files[rel].replace(old, new, 1)
        print("ok  %-10s %s" % (eid, label))

    for rel, data in files.items():
        try:
            data.decode('utf-8')
        except UnicodeDecodeError as exc:
            print("ERROR: %s would not be valid UTF-8 (%s). Nothing written." % (rel, exc))
            return 1

    for rel, data in files.items():
        with open(os.path.join(root, rel.replace('/', os.sep)), 'wb') as f:
            f.write(data)
    print("")
    print("patch applied to %d file(s)" % len(files))
    return 0


if __name__ == '__main__':
    sys.exit(main())
