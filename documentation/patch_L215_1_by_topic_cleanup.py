"""
patch_L215_1_by_topic_cleanup.py -- record the by-topic cleanup convention,
close one tail item that was already done, and sweep an ASCII violation in a
file this session had open.

WHAT THIS CHANGES
-----------------
LEDGER_CONSOLIDATED.md
  - L-215 opened: ledger cleanup by topic, not by age, with the 2026-08-19
    baseline measurement (107 open, 54 in the tail).
  - L-028 closed as ALREADY DONE -- comet_visualization_shells.py holds zero
    non-ASCII bytes; the entry had sat 69 days counted as debt.
  - L-191 gains a Gap+ note: migrating a typed constant to a read SPLITS a
    display-string unit, so the Tier-1 count rises while the uncited surface
    shrinks. Measured 3 -> 6 findings, 52 -> 42 claims.

info_dictionary.py
  - ASCII sweep, 24 of 26 bytes: superscript 3 and 2 become ^3 and ^2, six em
    dashes become " -- ". The two remaining bytes are the s-acute in Kacper
    Wierzchos's name and are LEFT ALONE: transliterating a person's name is
    not mechanical. Recorded as a Tony-action (decide) on L-215.

skills/ledger-and-session-records/SKILL.md
  - 1.6 -> 1.7, adding "Cluster the Tail by Topic, Not by Age".

RUN IT
------
Save this file into the repo root (the folder holding palomas_orrery.py),
open it in VS Code, and click Run. Or from a terminal in that folder:

    python patch_L215_1_by_topic_cleanup.py

Success: one 'ok' line per edit, then 'patch applied' per file.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line. Nothing is written.

AFTER IT RUNS, three steps, and the third is CRITICAL:
  1. Re-run ledger_index.py and skills_index.py (or maintenance_run.py,
     which runs both) so the index and the protocol's Skill Manifest agree.
  2. Archive this script to documentation/.
  3. Reinstall ledger-and-session-records to the account profile
     (Settings > Skills). A mid-session reinstall CANNOT be verified from
     inside this session -- the NEXT session must confirm its loaded copy
     reads 1.7 before doing ledger work.

PERMANENT vs DISPOSABLE: this script is disposable. The ledger entries, the
ASCII sweep and the skill section are permanent.

Created August 2026 with Anthropic's Claude Opus 5.

Role: devtool
Domain: dev_tools
"""

import hashlib
import os
import sys


def fingerprint(data):
    """Hash CONTENT, not raw bytes: CRLF and LF copies are the same file."""
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def to_file_eol(chunk, is_crlf):
    """Translate an LF-written anchor into the file's own line endings."""
    return chunk.replace(b'\n', b'\r\n') if is_crlf else chunk


def load(path, expected):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this script from the repo root "
              "(the folder holding palomas_orrery.py)." % path)
        sys.exit(1)
    with open(path, 'rb') as f:
        data = f.read()
    got = fingerprint(data)
    if got != expected:
        print("ERROR: BASE MOVED for %s" % path)
        print("  expected content fingerprint %s" % expected)
        print("  found                        %s" % got)
        print("  Nothing was written.")
        sys.exit(1)
    print("ok    base confirmed: %s" % path)
    return data


def apply_edits(path, data, edits):
    """edits: (label, old, new, expected_count). Bottom-up order."""
    is_crlf = data.count(b'\r\n') > 0
    for label, old, new, want in edits:
        old_f = to_file_eol(old, is_crlf)
        new_f = to_file_eol(new, is_crlf)
        n = data.count(old_f)
        if n != want:
            print("ANCHOR FAIL in %s: %s -- expected %d match(es), found %d. "
                  "Nothing written." % (path, label, want, n))
            sys.exit(1)
        data = data.replace(old_f, new_f)
        print("ok    %s: %s%s" % (path, label,
                                  " (x%d)" % want if want > 1 else ""))
    return data


def encoding_report(path, data, inserted):
    """Hard-fail on non-ASCII INSERTED; report pre-existing separately."""
    for chunk in inserted:
        bad = [b for b in chunk if b > 127]
        if bad:
            print("ERROR: this patch would insert %d non-ASCII byte(s) into "
                  "%s. Nothing written." % (len(bad), path))
            sys.exit(1)
    left = sum(1 for b in data if b > 127)
    if left:
        print("note: %s still holds %d non-ASCII byte(s) this patch did not "
              "reach" % (path, left))
    else:
        print("note: %s is ASCII-clean" % path)


def write_all(results):
    for path, blob, inserted in results:
        with open(path, 'wb') as f:
            f.write(blob)
        print("patch applied: %s (%d bytes)" % (path, len(blob)))
        encoding_report(path, blob, inserted)


LG = 'LEDGER_CONSOLIDATED.md'
ID = 'info_dictionary.py'
SK = 'skills/ledger-and-session-records/SKILL.md'

EXPECTED = {'LEDGER_CONSOLIDATED.md': '7fb7440fb0093831b3106205d48d1e03', 'info_dictionary.py': '8e02c8567f50da82b8ee764f38780cb4', 'skills/ledger-and-session-records/SKILL.md': 'd32e6c0fe45f6b1c1acf6c95ee22ef68'}

LG_EDITS = [('L-191: Gap+ note on the Tier-1 counting artifact', b"**Gap:** TWO JOBS, not one. (1) SOLAR -- visible bug, template exists,\nmechanical: delete the 15 `_info_hover` duplicates, author the 18\n`_info` strings in `\\n`, add `.replace('\\n', '<br>')` at the solar\nentries in `shell_configs.py`. (2) EARTH -- no visible bug, same\nduplication, and it is the case that decides the shape of the fix\nbecause of the surface-specific-text requirement. Do the Mode 5\nsurvey first in both cases.", b"**Gap:** TWO JOBS, not one. (1) SOLAR -- visible bug, template exists,\nmechanical: delete the 15 `_info_hover` duplicates, author the 18\n`_info` strings in `\\n`, add `.replace('\\n', '<br>')` at the solar\nentries in `shell_configs.py`. (2) EARTH -- no visible bug, same\nduplication, and it is the case that decides the shape of the fix\nbecause of the surface-specific-text requirement. Do the Mode 5\nsurvey first in both cases.\n**Gap+ (2026-08-19):** replacing a typed constant with a read SPLITS a\ndisplay-string unit and raises the Tier-1 COUNT while the uncited surface\nshrinks. Measured on L-209: `solar_visualization_shells.py` went 3 -> 6\nTier-1 findings, and total counted claims went 52 -> 42, because an\nf-string prefix inserted mid-run ends one string unit and starts another.\nSame text, same absent citation, more rows to report it in. Expect the\ncount to climb through this item and L-181 while the files get better;\nthe real repair for those six rows is citing the corona hover text, which\nwas owed before today.", 1), ('L-028: closed as already-done', b'<!-- L:028 status:OPEN upd:2026-06-11 section:D.Structural flag: rice:1/1/100/1 -->', b'<!-- L:028 status:DONE upd:2026-08-19 section:C flag: rice:1/1/100/1 -->\n- **Closed 2026-08-19: ALREADY DONE, and nobody had closed it.**\n  `comet_visualization_shells.py` holds zero non-ASCII bytes at\n  `434a712b`, verified by byte scan, and the named lines L257/L505 are\n  unrelated code. The work was finished at some point and the entry sat\n  69 days in the tail counted as debt. Found by the first by-topic sweep\n  (L-215), not by anyone reading the list.', 1), ('L-215: opened, by-topic cleanup with the baseline', b'#### [L-210] Pilot citation findings -- four rows in constants_new.py\n', b'#### [L-215] Ledger cleanup by topic, not by age\n<!-- L:215 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/80/2 -->\n- **Tony, 2026-08-19:** "Can we do a cleanup run to move the items that\n  touch on our current work? This would reduce the effort factor and\n  increase the confidence factor, the reach and impact by coordination."\n  Replaces a by-age triage Claude had recommended.\n- **The rule underneath it.** RICE Effort is not a property of an item;\n  it is a property of an item GIVEN what else is open. Scoring each one\n  alone is what produces a tail, and a score-ordered board cannot\n  distinguish "correctly deprioritized" from "dropped."\n- **Baseline, measured 2026-08-19 at `434a712b`.** 107 open items. 52\n  score below RICE 2.0; 54 are both below 3.0 and untouched for more\n  than 30 days. Oldest is L-053 at 73 days. Nothing exceeds 90 days, so\n  the tail is a stratum rather than a swamp.\n- **The mechanism is a STEP, not an event.** When a job is scheduled,\n  sweep the open ledger for items whose FILES the job already opens and\n  clear them in the same patch.\n- **Cluster by files touched, NOT by keyword.** A keyword sweep for the\n  worksheet-builder topic returned 36 items including a comet-tail\n  animation, the food-insecurity track and a ring-colour audit -- shared\n  vocabulary, unrelated work. The file list a job already holds is the\n  version that survives being run twice.\n- **First run, two findings, both of which are the argument.** L-028 was\n  ALREADY DONE and still counted as debt at 69 days (now closed). And a\n  ruled ASCII violation sat in `info_dictionary.py`, a file this session\n  had already fingerprinted, opened and edited -- the number was printed\n  by the patch\'s own encoding report and read past, because no ledger\n  item gave it meaning.\n- **A correction, recorded.** Claude attributed those ASCII bytes to\n  L-187 in conversation. L-187 is `info_dictionary` NUMERIC-OVERLAP\n  enumeration and has nothing to do with encoding. The violation had no\n  ledger item at all, which is a worse finding than a stale one.\n- **Tony-action (decide):** two non-ASCII bytes remain in\n  `info_dictionary.py` after this sweep, both the `s`-acute in the name\n  of Kacper Wierzchos, the Polish astronomer who discovered C/2024 E1.\n  Transliterating a person\'s name is not a mechanical fix and reads\n  intent, so it stayed out of scope. Options: keep the diacritic and\n  carry a named exception, or write the ASCII spelling and note the\n  original in the same string.\n**Note:** RICE is Claude\'s proposal, unratified.\n**Gap:** the 54-item tail is measured but unswept. No sweep has run\nexcept the L-214-adjacent one that produced the findings above.\n**Ref:** L-191 and L-181 (the migration that will inflate Tier-1 counts);\nL-028 (closed by the first sweep); L-187; `ledger-and-session-records`\nv1.7, which carries the convention.\n\n#### [L-210] Pilot citation findings -- four rows in constants_new.py\n', 1)]
SK_EDITS = [('skill 1.6 -> 1.7', b'Skill version: 1.6 | Cut from palomas_orrery @ 305b269 (v1.6), earlier\n@ 3398970 (v1.5) | August 14, 2026\n', b'Skill version: 1.7 | Cut from palomas_orrery @ 434a712b (v1.7), earlier\n@ 305b269 (v1.6), @ 3398970 (v1.5) | August 19, 2026\n', 1), ('sources paragraph: what 1.7 adds', b'next module_atlas.py run overwrites.\n', b"next module_atlas.py run overwrites. v1.7 adds Cluster the Tail by\nTopic, Not by Age -- Tony's ruling of August 19, 2026, replacing a\nby-age triage, after a measurement found 54 of 107 open items both\nbelow RICE 3.0 and untouched for a month (L-215).\n", 1), ('new section: Cluster the Tail by Topic, Not by Age', b'\n## Anchor Requirement (all outbound documents)\n', b'\n### Cluster the Tail by Topic, Not by Age [QUALITY]\n\nRICE Effort is not a property of an item. It is a property of an item\nGIVEN what else is open. Scoring each one alone is what produces a\ntail: by August 2026 this ledger held 107 open items, 54 of them both\nbelow RICE 3.0 and untouched for over 30 days, and a score-ordered\nboard cannot distinguish "correctly deprioritized" from "dropped."\n\nThe move is not a scheduled cleanup event. It is a STEP inside every\njob: when work is scheduled, sweep the open ledger for items whose\nFILES the job already opens, and clear them in the same patch. Sitting\ninside a file the job has already fingerprinted lowers Effort, raises\nConfidence, and lets one patch carry reach neither item had alone.\n\n**Cluster by FILES TOUCHED, not by keyword.** A keyword sweep for the\nworksheet-builder topic returned 36 items including a comet-tail\nanimation, a food-insecurity track and a ring-colour audit -- shared\nvocabulary, unrelated work. The file list a job already holds is the\nversion that survives being run twice.\n\nTwo findings from the first run, and both are the reason it is worth\ndoing:\n- An item 69 days old at RICE 1.0 was ALREADY DONE. The work had been\n  finished and nobody closed the entry, so it sat in the tail counted\n  as debt. A tail nobody looks at cannot say which of its items are\n  dead.\n- A ruled ASCII violation sat in a file the session had already\n  fingerprinted, opened and edited. The safe-file-editing sweep\n  conditions all held. The count was printed by the patch\'s own\n  encoding report and read past, because the item that gave it meaning\n  was seventy rows down a list sorted by score.\n\n(Tony\'s proposal, 2026-08-19, replacing a by-age triage Claude had\nrecommended. His reasoning is the rule: coordination raises Reach,\nImpact and Confidence at the same time as it lowers Effort.)\n\n## Anchor Requirement (all outbound documents)\n', 1)]
ID_SUBS = [('superscript three -> ^3', b'\xc2\xb3', b'^3'), ('superscript two -> ^2', b'\xc2\xb2', b'^2'), ('em dash -> --', b'\xe2\x80\x94', b' -- ')]


def sweep_ascii(path, data):
    """Mechanical substitutions only. Report what is left, never silently."""
    before = sum(1 for b in data if b > 127)
    for label, old, new in ID_SUBS:
        n = data.count(old)
        if n:
            data = data.replace(old, new)
            print("ok    %s: %s (x%d)" % (path, label, n))
    after = sum(1 for b in data if b > 127)
    print("note: %s had %d non-ASCII byte(s); %d normalized to ASCII in "
          "passing" % (path, before, before - after))
    if after:
        print("note: %s still holds %d non-ASCII byte(s) this patch did not "
              "reach -- the s-acute in a person's name, left for Tony "
              "(L-215)" % (path, after))
    return data


def main():
    lg = load(LG, EXPECTED[LG])
    lg = apply_edits(LG, lg, LG_EDITS)

    sk = load(SK, EXPECTED[SK])
    sk = apply_edits(SK, sk, SK_EDITS)

    idict = load(ID, EXPECTED[ID])
    idict = sweep_ascii(ID, idict)

    if b'Skill version: 1.7' not in sk:
        print("ANCHOR FAIL: skill version did not reach 1.7. Nothing written.")
        sys.exit(1)

    write_all([
        (LG, lg, [e[2] for e in LG_EDITS]),
        (SK, sk, [e[2] for e in SK_EDITS]),
        (ID, idict, []),
    ])
    print("")
    print("Next: maintenance_run.py (regenerates the ledger index and the "
          "Skill Manifest), archive this script, then REINSTALL "
          "ledger-and-session-records 1.7 to the account profile.")


if __name__ == '__main__':
    main()
