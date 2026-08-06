# -*- coding: utf-8 -*-
"""patch_skills_fable_fixes.py -- Fable skills-layer review fixes (8 skills)

Built on 339897000b63fa768ccb9b556dd432bac4f9d4eb
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file in the REPO ROOT (the folder containing skills/),
    open it in VS Code, and click Run. Nothing to type.

    Every anchor across all 8 files is verified BEFORE anything is
    written -- if one fails, no file is touched at all.

AFTER RUNNING
    Reinstall the changed skills to your account profile, then run
    skills_index.py so the manifest matches (this is now the binding
    rule recorded in ledger-and-session-records v1.5).

22 edits across 8 files.
"""

import os
import sys

# (relative_path, edit_id, label, old_bytes, new_bytes)
TARGET = None
ENCODING_GATE = 'utf-8'

EDITS = [
    ('skills/orrery-coding-conventions/SKILL.md', 'OCC-3', 'Hill table: deviations, Mars corrected',
     b'**Distance convention -- intended, and NOT yet uniform in the code.** The\nintent is perihelion: closest approach to the parent, where the Hill sphere\nis smallest, giving the conservative bound. Measured against the coded\n`radius_fraction` values at `1e60c783`, the codebase actually splits:\n\n| What the coded rf matches | Bodies |\n|---|---|\n| perihelion | Venus, Pluto, Eris |\n| semi-major axis | Mars, Jupiter, Uranus, Neptune |\n| aphelion | Saturn (also the Fable audit\'s worst finding) |\n| no convention within 3% | Mercury (rf 94.4; nearest is semi-major, off 4%) |\n\nThe perihelion convention holds for the bodies Batch 1 touched. It is an\naspiration for the rest, not a description of them. **Do not "correct" a\nbody to perihelion on the strength of this section alone** -- four bodies\nwould move, and the reconciliation has not been cross-checked. That work',
     b'**Distance convention -- intended, and NOT yet uniform in the code.** The\nintent is perihelion: closest approach to the parent, where the Hill sphere\nis smallest, giving the conservative bound. Re-measured 2026-08-05 with the\nMars Hill correction applied (L-182; pushed SHA recorded there), reporting\nthe deviation rather than a bucket -- a loose tolerance is what let Mars\'s\nunsourceable 324.5 read as "semi-major" for a version:\n\n| Body | coded rf | nearest convention | deviation |\n|---|---|---|---|\n| Venus | 166 | perihelion | +0.03% |\n| Mars | 319.2 | semi-major | +0.00% |\n| Neptune | 4685 | semi-major | -0.03% |\n| Pluto | 5041 | perihelion | +0.15% |\n| Jupiter | 740 | semi-major | -0.45% |\n| Uranus | 2770 | semi-major | +1.01% |\n| Eris | 6965 | perihelion | +1.39% |\n| Saturn | 1120 | aphelion | -1.73% |\n| **Mercury** | **94.4** | **none** | **+4.37% vs semi-major** |\n\nRead the deviation column, not just the label. Anything past ~0.5% is a\nnear-miss, not a match: Saturn, Uranus and Eris sit far enough out that\ntheir labels are descriptive convenience, and Mercury\'s rf 94.4 matches no\nconvention at all (perihelion 71.9, semi-major 90.5, aphelion 109.1) while\nits `# Source:` comment asserts the perihelion convention -- an open\nSOURCE_VS_VALUE conflict awaiting Batch 2.\n\nThe perihelion convention holds for the bodies Batch 1 touched. It is an\naspiration for the rest, not a description of them. **Do not "correct" a\nbody to perihelion on the strength of this section alone** -- four bodies\nwould move, and the reconciliation has not been cross-checked. That work'),
    ('skills/orrery-coding-conventions/SKILL.md', 'OCC-2', 'Barycenter Rule: add [QUALITY] tier tag',
     b'## Barycenter Rule',
     b'## Barycenter Rule [QUALITY]'),
    ('skills/orrery-coding-conventions/SKILL.md', 'OCC-1', 'version 1.2 -> 1.3',
     b'Skill version: 1.2 | Cut from palomas_orrery @ 1e60c783 | 2026-08-04',
     b'Skill version: 1.3 | Cut from palomas_orrery @ 3398970 | 2026-08-05'),
    ('skills/provenance-discipline/SKILL.md', 'PRV-2', 'comet precedent: mark fixed, stop describing as current',
     b'Known precedent: comet_visualization_shells.py lines 492-493 (SUN_RADIUS_KM, KM_PER_AU hardcoded despite KM_PER_AU already being imported) and line 602 (SUN_RADIUS_AU computed from the two hardcoded values). Same failure class as the close_approach_data.py stale-copy bug that originally motivated test_constants_provenance.py.',
     b'Known precedent (FIXED in L-156 1f; kept as history): comet_visualization_shells.py lines 492-493 once hardcoded SUN_RADIUS_KM and KM_PER_AU despite KM_PER_AU already being imported, with line 602 deriving SUN_RADIUS_AU from the two local copies. Those lines now carry the fix comment recording the removal -- a reader sent to find shadow constants there will find the repair, not the defect. Same failure class as the close_approach_data.py stale-copy bug that originally motivated test_constants_provenance.py.'),
    ('skills/provenance-discipline/SKILL.md', 'PRV-1', 'version 1.6 -> 1.7',
     b'Skill version: 1.6 | Cut from palomas_orrery @ 1e60c783 | August 4, 2026',
     b'Skill version: 1.7 | Cut from palomas_orrery @ 3398970 | August 5, 2026'),
    ('skills/agentic-pre-test/SKILL.md', 'APT-2', 'SystemButtonFace: drop the drifting literal count',
     b'palomas_orrery.py contains 26 SystemButtonFace literals and 0 native',
     b'palomas_orrery.py contains many SystemButtonFace literals and 0 native'),
    ('skills/agentic-pre-test/SKILL.md', 'APT-1', 'version 1.1 -> 1.2',
     b'Skill version: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12',
     b'Skill version: 1.2 | Cut from palomas_orrery @ 3398970 | 2026-08-05'),
    ('skills/safe-file-editing/SKILL.md', 'SFE-3', 'Encoding Gate: restore the heading',
     b'\n\nLF line endings. ASCII only in delivered code -- no emoji, arrows, degree',
     b'\n## Encoding Gate [QUALITY]\n\nLF line endings. ASCII only in delivered code -- no emoji, arrows, degree'),
    ('skills/safe-file-editing/SKILL.md', 'SFE-2', 'git apply: preference, not prohibition (Tony 2026-08-05)',
     b"run from a terminal with the working directory set to the repo root the\npatch targets (or the correct subfolder, e.g. `tools\\`, if the diff's\npaths are relative to one). Tony already has terminal access for this --\nno VS Code or GitHub Desktop needed, any Command Prompt/PowerShell cd'd\ninto the right folder works.",
     b"run from a terminal with the working directory set to the repo root the\npatch targets (or the correct subfolder, e.g. `tools\\`, if the diff's\npaths are relative to one).\n\n**Standing: the VS Code Run button is the preferred path where practical;\na terminal step is a fallback, not forbidden** (Tony, 2026-08-05,\nresolving the conflict Fable flagged between this section and the resident\nprotocol's WHO TONY IS). So prefer a runnable .py patch script over a\n.patch file when both would work. When a terminal step genuinely is the\nbetter tool, give the exact command and say what success and failure look\nlike -- which is what the two bullets below do."),
    ('skills/safe-file-editing/SKILL.md', 'SFE-1', 'version 1.1 -> 1.2',
     b'Skill version: 1.1 | Cut from palomas_orrery @ b29ad3f8 (v1.0), updated @',
     b'Skill version: 1.2 | Cut from palomas_orrery @ 3398970 (v1.2), earlier @'),
    ('skills/ledger-and-session-records/SKILL.md', 'LSR-3', 'Codebase Tooling: add skills_index.py',
     b'- ledger_index.py: regenerates the index zone in place; also supports\n  migrating closed items to section C.',
     b'- ledger_index.py: regenerates the index zone in place; also supports\n  migrating closed items to section C.\n- skills_index.py: regenerates the Skill Manifest table from the\n  skills/*/SKILL.md files and consistency-checks them. Same marker-zone\n  pattern as the two above. It targets the LIVE protocol only\n  (PROJECT_INSTRUCTIONS.md in the repo root); the versioned copies under\n  documentation/ are archival snapshots the tool deliberately never\n  rewrites, so do not expect a run to update them and do not hand-sync\n  them either -- an archive that keeps changing is not an archive. Since\n  August 2026 the run also PRINTS what the manifest was advertising before\n  it overwrites it, so drift is reported rather than silently absorbed.\n  See the binding rule under Protocol and Skills Change Log.'),
    ('skills/ledger-and-session-records/SKILL.md', 'LSR-2', 'Change Log: binding rule (prevention) + pointer to the resident gate',
     b"SHA it was cut from. The resident protocol's Skill Manifest table states\nthe EXPECTED installed versions -- reconcile a mismatch before trusting a\nskill, the same way a SHA mismatch is reconciled before a build.",
     b"SHA it was cut from. The resident protocol's Skill Manifest table states\nthe EXPECTED installed versions -- a mismatch STOPS the session under the\nresident Stale Skill = Stop [CRITICAL] gate, which also tells Tony the two\nactions needed (push to skills/, reinstall to the account profile).\n\n**Binding rule [QUALITY].** A skill version bump is not done until the\nmanifest agrees. The three steps travel in ONE commit: bump the version\nline in SKILL.md -> run `skills_index.py` -> commit SKILL.md and both\nprotocol copies together. Do not leave the regeneration to a later\ncheckpoint someone has to remember.\n\nThis is the PREVENTION side. Detection is the resident protocol's\nStale Skill = Stop [CRITICAL] gate, which halts a session outright when a\nloaded skill's version disagrees with the manifest row. Two layers because\nprevention depends on remembering and detection does not: if the binding\nrule is followed there is no window, and if it is missed the gate catches\nit before any work is done on the wrong copy.\n\nThe reason is not tidiness. The protocol tells a session that finds a\nskill-version mismatch to stop and reconcile, the same rule as a SHA\nmismatch. A stale manifest therefore fires that alarm on every session\nthat loads the affected skill -- and an alarm that is always wrong is one\nthe reader learns to wave off, which is the state in which a REAL mismatch\nstops registering. Bound to the commit, drift cannot exist at any pushed\nSHA. (Earned: the manifest advertised 1.1/1.4 against an actual 1.2/1.6\nfor about three weeks, provenance-discipline having already gone stale a\nversion earlier -- Fable skills-layer review, Job 3 #8. `skills_index.py`\nnow prints what the manifest was advertising before it overwrites it, so\nrunning the tool reports the drift instead of silently absorbing it.)"),
    ('skills/ledger-and-session-records/SKILL.md', 'LSR-1', 'version 1.4 -> 1.5',
     b'Skill version: 1.4 | Cut from palomas_orrery @ ca9c706e7c68dec724bbcd242e0b0048c5392dfb | July 26, 2026',
     b'Skill version: 1.5 | Cut from palomas_orrery @ 3398970 | August 5, 2026'),
    ('skills/gallery-pipeline/SKILL.md', 'GPL-2', 'SHA-pin line: name the master',
     b'the viewer. SHA-pin each repo separately in handoffs.',
     b'the viewer. SHA-pin each repo separately in handoffs (master: ledger-and-session-records, Anchor Requirement).'),
    ('skills/gallery-pipeline/SKILL.md', 'GPL-1', 'version 1.1 -> 1.2',
     b'Skill version: 1.1 | Cut from tonyquintanilla.github.io @ 89c8bf30 (code)',
     b'Skill version: 1.2 | Cut from tonyquintanilla.github.io @ 89c8bf30 (code)'),
    ('skills/gallery-cache-builder/SKILL.md', 'GCB-2', 'mislabeled comment: search by string, not line number',
     b'Field note: an inline comment near line 755 mislabels this as "guard/B3 WARN".',
     b'Field note: an inline comment mislabels this as "guard/B3 WARN" (search for that string; it has drifted from line 755 to ~1099 and will move again).'),
    ('skills/gallery-cache-builder/SKILL.md', 'GCB-1', 'version 1.1 -> 1.2',
     b'Skill version: 1.1 | Cut from tonyquintanilla.github.io @ a08bdd10 (code) and palomas_orrery @ af58f7f8 (context) | 2026-07-12',
     b'Skill version: 1.2 | Cut from tonyquintanilla.github.io @ a08bdd10 (code) and palomas_orrery @ 3398970 (context) | 2026-08-05'),
    ('skills/gallery-assembler/SKILL.md', 'GAS-3', 'time-deictic "as of tonight" -> the date',
     b'Pluto/Charon and Moon/Io/Titan are both, as of tonight, in the state of',
     b'Pluto/Charon and Moon/Io/Titan are both, as of July 20 2026, in the state of'),
    ('skills/gallery-assembler/SKILL.md', 'GAS-2', 'stale-doc note: add resolver.py',
     b'to include it. (Known stale doc: its own docstring still says',
     b'to include it. (Known stale docs: cache_reader.py AND resolver.py both still say'),
    ('skills/gallery-assembler/SKILL.md', 'GAS-5', 'pre-existing non-ASCII: section sign -> "sec."',
     b'session); master plan \xc2\xa73; L-149/L-150/L-151.',
     b'session); master plan sec. 3; L-149/L-150/L-151.'),
    ('skills/gallery-assembler/SKILL.md', 'GAS-4', 'pre-existing non-ASCII: section sign -> "sec."',
     b'exists because of that one constraint. Full treatment: master plan \xc2\xa73,',
     b'exists because of that one constraint. Full treatment: master plan sec. 3,'),
    ('skills/gallery-assembler/SKILL.md', 'GAS-1', 'version 1.0 -> 1.1',
     b'Skill version: 1.0 | Cut from gallery @ a7abea59ed5368a38ce7364ce53b4679aa83b5a1 / orrery @ e775050d227fa63aa79e97a7af3f290a5c038899 | July 20, 2026',
     b'Skill version: 1.1 | Cut from gallery @ f83a3abc72c5516e6dc2ad264be53ce95b68cf38 / orrery @ 3398970 | August 5, 2026'),
]



def main():
    root = os.path.dirname(os.path.abspath(__file__))
    rels = []
    for e in EDITS:
        r = e[0] if len(e) == 5 else TARGET
        if r not in rels:
            rels.append(r)

    files, normalized = {}, []
    for rel in rels:
        path = os.path.join(root, rel.replace('/', os.sep))
        if not os.path.exists(path):
            print("ERROR: %s not found. Save this script in the repo root.")
            print("       NOTHING WAS WRITTEN.")
            return 1
        with open(path, 'rb') as f:
            data = f.read()
        if b'\r\n' in data:
            n = data.count(b'\r\n')
            data = data.replace(b'\r\n', b'\n')
            normalized.append((rel, n))
        files[rel] = data

    for rel, n in normalized:
        print("fix CRLF     %s: normalized %d line endings to LF" % (rel, n))

    # Pass 1 -- verify every anchor before writing anything.
    for e in EDITS:
        rel, eid, label, old, new = e if len(e) == 5 else (TARGET,) + e
        c = files[rel].count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) in %s matched %d, expected 1." % (eid, label, rel, c))
            print("             NOTHING WAS WRITTEN. Every file is unchanged.")
            print("             Fix the cause, then RE-RUN this script.")
            return 1

    # Pass 2 -- apply.
    for e in EDITS:
        rel, eid, label, old, new = e if len(e) == 5 else (TARGET,) + e
        files[rel] = files[rel].replace(old, new, 1)
        print("ok  %-10s %s" % (eid, label))

    for rel, data in files.items():
        try:
            data.decode(ENCODING_GATE)
        except UnicodeDecodeError as exc:
            print("ERROR: %s would not be valid %s (%s)." % (rel, ENCODING_GATE, exc))
            print("       NOTHING WAS WRITTEN. Every file is unchanged.")
            return 1

    for rel, data in files.items():
        with open(os.path.join(root, rel.replace('/', os.sep)), 'wb') as f:
            f.write(data)

    print("")
    print("patch applied to %d file(s)%s"
          % (len(files), " (+%d CRLF normalized)" % len(normalized) if normalized else ""))
    return 0


if __name__ == '__main__':
    sys.exit(main())
