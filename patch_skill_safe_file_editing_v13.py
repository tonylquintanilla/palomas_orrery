"""
patch_skill_safe_file_editing_v13.py

Adds the line-ending discipline earned on 2026-08-07 to the
safe-file-editing skill, and bumps it 1.2 -> 1.3.

Built on 1ba20c324302bb372590582dca707f4ce9e14df4 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file into the palomas_orrery folder (the folder that holds
    skills/), open it in VS Code, and click Run.
    Equivalent command line: python patch_skill_safe_file_editing_v13.py

WHAT IT DOES
    skills/safe-file-editing/SKILL.md
        version 1.2 -> 1.3
        + new section: Line Endings Are Not Content [QUALITY]
        + two field notes from the L-179/L-180 patch rounds

AFTER RUNNING (Tony, in order)
    1. Commit and push in GitHub Desktop.
    2. Reinstall the skill: Settings > Skills > safe-file-editing,
       upload the updated skills/safe-file-editing/SKILL.md.
    3. Run skills_index.py from the dashboard to regenerate the
       Skill Manifest table in the protocol.
    4. Commit and push again.
    Steps 2 and 3 are what keep the three stores in sync; skipping either
    is the drift the Stale Skill = Stop gate exists to catch.

SAFETY
    The file is fingerprinted on CONTENT (line endings normalized before
    hashing) and every anchor must match exactly once. Any mismatch aborts
    with NOTHING WAS WRITTEN. The file's existing line-ending convention
    is preserved.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import pathlib
import sys

TARGET = 'skills/safe-file-editing/SKILL.md'
CONTENT_FINGERPRINT = '9d27281ded1e8f4ace36719b2743d4f7'

EDITS = [
    (
        "version 1.2 -> 1.3",
        b"Skill version: 1.2 | Cut from palomas_orrery @ 3398970 (v1.2), earlier @\n"
        b"bdaaa0c (v1.1) | July 29, 2026\n"
        b"Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;\n"
        b"v1.1 adds the delivery-format convention from a same-day incident (a\n"
        b"transactional patch silently never run; see Field Notes).\n",

        b"Skill version: 1.3 | Cut from palomas_orrery @ 1ba20c3 (v1.3), earlier @\n"
        b"3398970 (v1.2), bdaaa0c (v1.1) | August 7, 2026\n"
        b"Source: project_instructions_v3_29.md Part 3 + Part 5 technical lessons;\n"
        b"v1.1 adds the delivery-format convention from a same-day incident (a\n"
        b"transactional patch silently never run; see Field Notes). v1.3 adds\n"
        b"Line Endings Are Not Content, earned when a patch aborted twice on a\n"
        b"CRLF working copy whose bytes were identical to the repo's.\n",
    ),
    (
        "add the Line Endings Are Not Content section",
        b"The assert is the point: a zero-match replace \"succeeds\" silently and the\n"
        b"edit never lands.",

        b"### Line Endings Are Not Content [QUALITY]\n"
        b"\n"
        b"A patch harness has to answer two questions, and they are different:\n"
        b"\"is this the file I built against\" and \"does this anchor still exist.\"\n"
        b"Line endings can change the first answer while leaving the second true.\n"
        b"\n"
        b"**Fingerprint the content, not the raw bytes.** Normalize before hashing:\n"
        b"\n"
        b"```python\n"
        b"fp = hashlib.md5(data.replace(b'\\r\\n', b'\\n')).hexdigest()\n"
        b"```\n"
        b"\n"
        b"A Windows working copy can hold CRLF where the repo holds LF. With\n"
        b"`.gitattributes` set to `* text=auto eol=lf`, git normalizes on commit\n"
        b"and reports NO change -- correctly, because there is none. A raw-byte\n"
        b"fingerprint calls that \"BASE MOVED\" and sends everyone hunting for an\n"
        b"edit that was never made. The delta is exactly one byte per line, which\n"
        b"is the tell: compare sizes before assuming content drift.\n"
        b"\n"
        b"**Translate anchors to the file's own convention.** Anchors are written\n"
        b"LF; a CRLF file matches none of them and the patch aborts on a file it\n"
        b"could have edited safely. Detect per file and convert both sides:\n"
        b"\n"
        b"```python\n"
        b"is_crlf = data.count(b'\\r\\n') > 0\n"
        b"if is_crlf:\n"
        b"    old = old.replace(b'\\n', b'\\r\\n')\n"
        b"    new = new.replace(b'\\n', b'\\r\\n')\n"
        b"```\n"
        b"\n"
        b"Preserve what the file already uses rather than converting it. The patch\n"
        b"is there to make one change, not to also silently restyle 11,000 lines.\n"
        b"\n"
        b"**Files in one repo can disagree.** Do not detect once and apply the\n"
        b"answer everywhere. In the case that produced this note, four files were\n"
        b"LF and one was CRLF in the same working directory -- something had\n"
        b"rewritten that one file in text mode, which is precisely what the\n"
        b"binary-mode rule above exists to prevent.\n"
        b"\n"
        b"The assert is the point: a zero-match replace \"succeeds\" silently and the\n"
        b"edit never lands.",
    ),
    (
        "add two field notes",
        b"- `grep -c 'a\\|b\\|c'` confirms something matched, not which pattern did.\n"
        b"  Verifying three distinct claims in one combined call read as confirming\n"
        b"  all three when only one had actually landed. Check each anchor\n"
        b"  separately when verifying multiple distinct claims. (2026-07-29)\n",

        b"- `grep -c 'a\\|b\\|c'` confirms something matched, not which pattern did.\n"
        b"  Verifying three distinct claims in one combined call read as confirming\n"
        b"  all three when only one had actually landed. Check each anchor\n"
        b"  separately when verifying multiple distinct claims. (2026-07-29)\n"
        b"- **A fingerprint mismatch is evidence of difference, not evidence of\n"
        b"  editing.** A patch aborted with BASE MOVED and the diagnosis offered\n"
        b"  was \"your working copy has unpushed edits\" -- stated as fact, inferred\n"
        b"  from comparing the working copy against repo bytes without checking\n"
        b"  what kind of difference it was. It was CRLF versus LF, content\n"
        b"  identical, nothing edited. The check was right to fire and the reading\n"
        b"  of it was wrong. When a fingerprint fails, establish WHAT differs\n"
        b"  before saying WHY. (2026-08-07)\n"
        b"- **Build patch anchors from the file, not from memory of the file.** An\n"
        b"  anchor included trailing context typed from recall; the actual next\n"
        b"  line was a different `# Source:` comment entirely, so the anchor\n"
        b"  matched zero times and the harness refused. This is the harness\n"
        b"  working, but it costs a round trip. Read the exact bytes at the edit\n"
        b"  site first, and prefer a short unique anchor over a long guessed one.\n"
        b"  Where a block genuinely appears twice and both copies get the same\n"
        b"  replacement, one edit with an explicit expected count of 2 is safer\n"
        b"  than two long anchors distinguished only by distant context.\n"
        b"  (2026-08-07)\n",
    ),
]


def main():
    here = pathlib.Path(__file__).parent
    path = here / TARGET

    if not path.exists():
        print(f"MISSING: {TARGET}")
        print("Run this from the palomas_orrery folder (the one holding skills/).")
        print("\nNOTHING WAS WRITTEN.")
        return 1

    data = path.read_bytes()
    fp_actual = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
    if not CONTENT_FINGERPRINT.startswith('__') and fp_actual != CONTENT_FINGERPRINT:
        print(f"BASE MOVED: {TARGET}")
        print(f"    expected content MD5 {CONTENT_FINGERPRINT}")
        print(f"    actual   content MD5 {fp_actual}")
        print("    (line endings normalized, so this is a real content difference.)")
        print("\nNOTHING WAS WRITTEN.")
        return 1

    is_crlf = data.count(b'\r\n') > 0
    if is_crlf:
        print(f"  ..  {TARGET}: CRLF file -- anchors translated, endings preserved")

    problems = []
    for label, old, new in EDITS:
        o, n = (old, new)
        if is_crlf:
            o = o.replace(b'\n', b'\r\n')
            n = n.replace(b'\n', b'\r\n')
        count = data.count(o)
        if count != 1:
            problems.append(f"ANCHOR {count} MATCHES (expected 1): {label}\n"
                            f"    first 70 bytes: {o[:70]!r}")
        else:
            data = data.replace(o, n, 1)

    if problems:
        print("\n".join(problems))
        print("\nNOTHING WAS WRITTEN.")
        return 1

    path.write_bytes(data)
    for label, _o, _n in EDITS:
        print(f"  ok  {TARGET} -- {label}")
    print(f"\npatch applied ({len(data)} bytes)")
    print("\nNext, in order:")
    print("  1. Commit and push in GitHub Desktop.")
    print("  2. Settings > Skills: reinstall safe-file-editing from the")
    print("     updated skills/safe-file-editing/SKILL.md.")
    print("  3. Run skills_index.py to regenerate the Skill Manifest table.")
    print("  4. Commit and push again.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
