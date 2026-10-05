#!/usr/bin/env python3
"""
patch_L417_1_skill_install_limits_20261005.py -- ORRERY repo. The Skill
headers check holds every skill to Anthropic's documented limits (L-417).

Built on orrery 72e3b55805c29f1f08a583864bd815a47e7434c6
at https://github.com/tonylquintanilla/palomas_orrery
(gallery 624aa94557e16956b2fe022a467936ae2ccf3406 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io was not
read or changed).

It touches only skills_index.py, so it runs in any order with
patch_L413_2 and patch_L416_1; none of them changes another's file.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run. The same as:
        python patch_L417_1_skill_install_limits_20261005.py
    Then follow the numbered NEXT steps it prints.

WHAT IT DOES
    skills_index.py --check, the maintenance run's "Skill headers" row,
    now also fails on any skill whose header breaks a rule on Anthropic's
    Skills pages, read on 2026-10-05 (the overview and the authoring best
    practices):
        - a name over 64 characters, or with anything but lowercase
          letters, numbers and hyphens, or containing "anthropic" or
          "claude";
        - a description over 1024 characters;
        - an XML tag in either.
    It warns, without failing, on a SKILL.md body over Anthropic's
    500-line guideline. Five skills are over it today and will print a
    warning in the full output: provenance-discipline (2,910 lines),
    interactive-exhibit (796), safe-file-editing (705),
    orrery-coding-conventions (636), ledger-and-session-records (578).
    The run's summary row shows only the OK line, so it stays green.
    The description is measured the way YAML reads it, without a quoted
    value's quote marks.

    From a Claude Sonnet 5.5 session's check of the same day, rebuilt to
    this project's patch rules: a content fingerprint, LF line endings,
    the page actually read as the source, and no near-the-limit warning,
    which rested on a chosen number (Tony, 2026-10-05).

TESTED on a throwaway copy of 72e3b55: all 11 skills pass, with the five
warnings above; a made-up skill breaking all four rules fails with four
named problems and exit 1; a quoted description of exactly 1024
characters passes, with and without PyYAML; orrery_maintenance_run.py
passed 20 of 20 gating checkers; the scanner read 296.

LINE ENDINGS (safe-file-editing 1.12): written LF; a CRLF working copy
is named in a "note:" line. The file is committed LF.

PERMANENT, though this script is thrown away: the limits and the check.
No skill changes, so no skill version moves and nothing is reinstalled.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ERROR: or ANCHOR FAIL: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 5, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os

REPO = "orrery"
ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
BUILT_ON = "72e3b55"
NEXT = ["1. Move this script into documentation/ before the maintenance",
        "   run: in the root folder the provenance scanner counts it.",
        "2. Run orrery_maintenance_run.py. Skill headers should pass; its",
        "   full output lists the five long skills as warnings.",
        "3. Commit and push, with the other orrery patches or on its own."]

BASE = {'skills_index.py': 'aed8a0cb1e5f81e69fdae04bdde9a5b5'}

EDITS = {
  'skills_index.py': [
    ('docstring: what the check covers',
      ('exists, no duplicate names, and every skill has a fires_when field\n'
      '(missing fires_when falls back to the first sentence of description,\n'
      'truncated, and is reported as a warning).\n'),
      ('exists, no duplicate names, and every skill has a fires_when field\n'
      '(missing fires_when falls back to the first sentence of description,\n'
      'truncated, and is reported as a warning). It also holds every header to\n'
      "Anthropic's documented limits -- a name of at most 64 characters, only\n"
      'lowercase letters, numbers and hyphens, never "anthropic" or "claude";\n'
      'a description of at most 1024 characters; no XML tag in either -- and\n'
      "warns on a body over Anthropic's 500-line guideline (L-417; the pages\n"
      'and the date they were read are beside the constants below).\n'),
      1),
    ('docstring: credit',
      ('a bad header fails the run.)\n'
      '\n'
      'Role: devtool\n'),
      ('a bad header fails the run.)\n'
      '\n'
      "Module updated: October 5, 2026 with Anthropic's Claude Opus 5.5\n"
      "(L-417: Anthropic's documented header limits, read that day from the\n"
      'Skills overview and the authoring best practices, are checked -- name\n'
      'length, characters and reserved words, description length, no XML tag\n'
      '-- and each one broken is a CONSISTENCY PROBLEM, so --check exits 1 and\n'
      "the maintenance run's Skill headers row fails. A body over the 500-line\n"
      'guideline is a warning. The description is measured as YAML reads it,\n'
      "without a quoted value's quote marks. From a Claude Sonnet 5.5 session's\n"
      "check of the same day, rebuilt to this project's patch rules and\n"
      'without its near-the-limit warning, which rested on a chosen number.)\n'
      '\n'
      'Role: devtool\n'),
      1),
    ('the documented limits, with their source',
      'FALLBACK_TRUNC = 60   # chars of description used when fires_when is absent\n',
      ('FALLBACK_TRUNC = 60   # chars of description used when fires_when is absent\n'
      '\n'
      "# Anthropic's documented limits for a skill's header (L-417), read on\n"
      '# 2026-10-05 from two pages: the Skills overview, section "Skill\n'
      '# structure", and the authoring best practices, sections "YAML\n'
      '# frontmatter requirements" and "Token budgets".\n'
      '#   https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview\n'
      '#   https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices\n'
      '# The first four are rules, so breaking one is a CONSISTENCY PROBLEM and\n'
      '# --check exits 1. The body length is guidance ("Keep SKILL.md body under\n'
      '# 500 lines for optimal performance"), so it is a warning.\n'
      'NAME_MAX_CHARS = 64\n'
      "NAME_CHARS_RE = re.compile(r'[a-z0-9-]+')     # lowercase letters, numbers, hyphens\n"
      "NAME_RESERVED_WORDS = ('anthropic', 'claude')\n"
      'DESCRIPTION_MAX_CHARS = 1024\n'
      "XML_TAG_RE = re.compile(r'<[A-Za-z/][^>]*>')  # neither field may hold an XML tag\n"
      'BODY_GUIDELINE_LINES = 500\n'),
      1),
    ('description_value and check_install_limits',
      'def parse_skill(skill_dir):\n',
      ('def description_value(lines, body_start, loose):\n'
      '    """The description as the Settings uploader reads it: the YAML value.\n'
      '\n'
      "    The loose reader keeps a quoted value's quote marks, which would count\n"
      '    two characters too many against the limit (provenance-discipline and\n'
      '    earth-system-pipeline are quoted since L-407). PyYAML gives the value\n'
      '    itself where it is installed; otherwise one pair of outer quotes is\n'
      "    removed, and a double-quoted value's escaped quotes and backslashes\n"
      '    are read as single characters, which covers how these headers quote.\n'
      '    """\n'
      '    try:\n'
      '        import yaml\n'
      "        data = yaml.safe_load('\\n'.join(lines[1:body_start - 1]))\n"
      "        value = data.get('description') if isinstance(data, dict) else None\n"
      '        if isinstance(value, str):\n'
      '            return value.strip()\n'
      '    except Exception:\n'
      '        pass\n'
      "    raw = loose.get('description', '').strip()\n"
      '    if len(raw) >= 2 and raw[0] == raw[-1] == \'"\':\n'
      '        return raw[1:-1].replace(\'\\\\"\', \'"\').replace(\'\\\\\\\\\', \'\\\\\')\n'
      '    if len(raw) >= 2 and raw[0] == raw[-1] == "\'":\n'
      '        return raw[1:-1].replace("\'\'", "\'")\n'
      '    return raw\n'
      '\n'
      '\n'
      'def check_install_limits(name, desc, label, body_lines, problems, warnings):\n'
      '    """Anthropic\'s documented header limits (L-417), checked here so that a\n'
      '    skill which breaks one fails the maintenance run before it is pushed or\n'
      '    reinstalled, instead of being refused by Settings afterwards. The\n'
      '    limits and where they were read are the constants above.\n'
      '    """\n'
      '    if len(name) > NAME_MAX_CHARS:\n'
      '        problems.append(f"{label}: name is {len(name)} characters; Anthropic\'s "\n'
      '                        f"limit is {NAME_MAX_CHARS}")\n'
      '    if not NAME_CHARS_RE.fullmatch(name):\n'
      '        problems.append(f"{label}: name \'{name}\' may hold only lowercase "\n'
      '                        f"letters, numbers and hyphens")\n'
      '    for word in NAME_RESERVED_WORDS:\n'
      '        if word in name:\n'
      '            problems.append(f"{label}: name contains \'{word}\', a word "\n'
      '                            f"Anthropic reserves")\n'
      '    if len(desc) > DESCRIPTION_MAX_CHARS:\n'
      '        problems.append(f"{label}: description is {len(desc)} characters; "\n'
      '                        f"Anthropic\'s limit is {DESCRIPTION_MAX_CHARS}")\n'
      "    for field, value in (('name', name), ('description', desc)):\n"
      '        tag = XML_TAG_RE.search(value)\n'
      '        if tag:\n'
      '            problems.append(f"{label}: {field} holds an XML tag, "\n'
      '                            f"{tag.group(0)!r}, which Anthropic disallows")\n'
      '    if body_lines > BODY_GUIDELINE_LINES:\n'
      '        warnings.append(f"{label}: SKILL.md body is {body_lines} lines; "\n'
      '                        f"Anthropic\'s guideline is under "\n'
      '                        f"{BODY_GUIDELINE_LINES}")\n'
      '\n'
      '\n'
      'def parse_skill(skill_dir):\n'),
      1),
    ('called from parse_skill',
      ('    version = None\n'
      '    for line in lines[body_start:]:\n'
      '        m = VERSION_RE.match(line)\n'),
      ("    # L-417: Anthropic's documented limits on the header, and the body's\n"
      '    # length against its guideline. A file ending in a newline splits to\n'
      '    # one empty last item, which is not a line.\n'
      "    body_lines = len(lines) - body_start - (1 if text.endswith('\\n') else 0)\n"
      '    check_install_limits(name, description_value(lines, body_start, fm),\n'
      '                         skill_dir.name, body_lines, problems, warnings)\n'
      '\n'
      '    version = None\n'
      '    for line in lines[body_start:]:\n'
      '        m = VERSION_RE.match(line)\n'),
      1),
  ],
}


def fingerprint(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def non_ascii(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the %s "
                             "root. NOTHING was written." % (marker, REPO))
    results = []
    for path in sorted(EDITS):
        text, was_crlf = read_lf(path)
        got = fingerprint(text)
        if got != BASE[path]:
            raise SystemExit(
                "ERROR: %s is not the file this patch was built against.\n"
                "       expected %s, found %s. It has changed since\n"
                "       %s, or this patch has already run.\n"
                "       (Line endings are excluded, so they are not the cause.)\n"
                "       NOTHING was written." % (path, BASE[path], got, BUILT_ON))
        before = non_ascii(text)
        done = []
        for label, old, new, want in EDITS[path]:
            found = text.count(old)
            if found != want:
                raise SystemExit("ANCHOR FAIL (%s): expected %d match(es) in "
                                 "%s, found %d. NOTHING was written."
                                 % (label, want, path, found))
            text = text.replace(old, new)
            done.append(label)
        if non_ascii(text) > before:
            raise SystemExit("ERROR: %s would gain non-ASCII characters. "
                             "NOTHING was written." % path)
        results.append((path, text, done, was_crlf))
    for path, text, done, was_crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        for label in done:
            print("ok  %-30s %s" % (path, label))
        if was_crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
