"""constants_change_report.py -- what moved in constants_new.py, and why.

RUN COMMAND
-----------
Open this file in VS Code and click Run. It takes no arguments.

    python constants_change_report.py

Run it before committing a change to constants_new.py. The maintenance
runner also calls it.

WHAT IT DOES
------------
Asks git what changed in constants_new.py since the last commit, and
reports each changed value in words:

    CHROMOSPHERE_RADII            1.5 -> 1.1
        provenance also changed -- deliberate correction

    BENNU_RADIUS_KM               0.246 -> 0.25
        VALUE MOVED ALONE -- no provenance change in this block

That second line is the whole point. A deliberate correction moves the
number AND its comment block together: someone writes a new `# Source:`,
a `# Corrected:` record, or fresh `# Cross-checked:` annotations in the
same edit. Corruption -- a bad merge, a stray keystroke, a copied stale
value -- moves the number alone and leaves the evidence describing the
old one.

WHY THERE IS NO SECOND COPY OF ANY NUMBER
-----------------------------------------
This tool stores nothing. git already holds every prior value of every
constant; the old number comes out of the diff's removed line and the new
one out of the added line. That is deliberate (Tony's ruling,
2026-08-12): a stored list of expected values is a second dictionary, and
a second dictionary has to be hand-maintained, and a hand-maintained copy
goes stale. test_constants_provenance.py was that copy -- 52 pinned
literals, six of which sat behind an August 2 correction batch for ten
days.

It also means this covers constants that do not exist yet. A value added
next month is reported the first time it moves, with nobody writing
anything.

WHAT IT CANNOT SEE
------------------
Anything already committed. This compares the working tree against the
last commit, so it is a pre-commit reader. A value corrupted and
committed three weeks ago is history, not a pending change, and this
tool will not mention it -- that is the provenance scanner's job.

Comparing against something other than the last commit:

    python constants_change_report.py <sha>

EXIT CODE
---------
0 only when everything was understood and every changed value also moved
its provenance. 1 when a value moved alone, when a change could not be
attributed, or when a changed line was not understood at all. The
maintenance runner surfaces that as a failed checker.

A gap announces. Nothing this tool could not read is reported as clean.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5.
"""

import os
import re
import subprocess
import sys

TARGET = 'constants_new.py'

# NAME = <number>, at any indent, with an optional trailing comment.
ASSIGN_RE = re.compile(
    r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*'
    r'(-?\d+\.?\d*(?:[eE][-+]?\d+)?)\s*(?:#.*)?$')

# 'Key': <number>, inside a dict literal.
DICT_RE = re.compile(
    r"^\s*['\"]([^'\"]+)['\"]\s*:\s*"
    r'(-?\d+\.?\d*(?:[eE][-+]?\d+)?)\s*,?\s*(?:#.*)?$')

COMMENT_RE = re.compile(r'^\s*#')


def git(args, cwd):
    """Run a git command. Returns (ok, output)."""
    try:
        done = subprocess.run(['git'] + args, cwd=cwd,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              stdin=subprocess.DEVNULL,
                              timeout=60)
    except FileNotFoundError:
        return False, ('git was not found on PATH. This tool reads the '
                       'diff from git rather than storing its own copy of '
                       'the values, so it cannot run without it.')
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, 'git failed to run: %s' % exc
    text = done.stdout.decode('utf-8', 'replace')
    if done.returncode != 0:
        return False, text.strip()
    return True, text


def parse_line(line):
    """(name, value) from a diff line body, or None if it is not one."""
    for pattern in (ASSIGN_RE, DICT_RE):
        match = pattern.match(line)
        if match:
            return match.group(1), match.group(2)
    return None


def split_hunks(diff_text):
    """The diff's hunks, each as a list of raw lines."""
    hunks = []
    current = None
    for line in diff_text.splitlines():
        if line.startswith('@@'):
            current = []
            hunks.append(current)
        elif current is not None:
            current.append(line)
    return hunks


def read_changes(diff_text):
    """Value changes, additions, removals, and everything not understood.

    Provenance is judged per HUNK: if the hunk carrying a value change
    also adds or removes comment lines, the evidence moved with the
    number. A hunk is git's own unit of nearby change, which is close
    enough to "the block around this constant" without parsing Python.

    Two ways that judgement can be wrong, and BOTH announce rather than
    resolve themselves quietly (Tony's ruling, 2026-08-12: a gap should
    announce and we track it down):

    AMBIGUOUS -- more than one value changed in a hunk that also moved
    comments. The comment edit documents SOME constant in that hunk and
    this tool cannot say which, so it credits none of them and says so.

    UNPARSED -- a changed line carrying a digit that matched neither the
    assignment nor the dict-entry shape. That is a value edit written in
    a form this tool does not read, and reporting clean would be the
    silent failure worth fearing most, since a skipped line looks exactly
    like no change at all.
    """
    changed, added, removed, unparsed = [], [], [], []

    for hunk in split_hunks(diff_text):
        old_vals, new_vals = {}, {}
        comment_moved = False
        hunk_unparsed = []
        for line in hunk:
            if not line or line[0] not in '+- ':
                continue
            body, sign = line[1:], line[0]
            if sign == ' ':
                continue
            if COMMENT_RE.match(body):
                comment_moved = True
                continue
            parsed = parse_line(body)
            if parsed is None:
                if any(ch.isdigit() for ch in body) and body.strip():
                    hunk_unparsed.append(sign + body.rstrip())
                continue
            name, value = parsed
            (old_vals if sign == '-' else new_vals)[name] = value

        unparsed.extend(hunk_unparsed)

        moved_here = [n for n in set(old_vals) & set(new_vals)
                      if old_vals[n] != new_vals[n]]
        ambiguous = comment_moved and len(moved_here) > 1

        for name in sorted(set(old_vals) | set(new_vals)):
            before, after = old_vals.get(name), new_vals.get(name)
            if before is not None and after is not None:
                if before != after:
                    state = ('ambiguous' if ambiguous
                             else 'documented' if comment_moved
                             else 'bare')
                    changed.append((name, before, after, state))
            elif after is not None:
                added.append((name, after, comment_moved))
            else:
                removed.append((name, before))

    return changed, added, removed, unparsed


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    base = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'

    if not os.path.exists(os.path.join(here, TARGET)):
        print('ERROR: %s not found. Run this from the repo root.' % TARGET)
        return 2

    print('=' * 70)
    print('CONSTANTS CHANGE REPORT -- %s vs %s' % (TARGET, base))
    print('=' * 70)

    ok, out = git(['diff', '--unified=6', base, '--', TARGET], here)
    if not ok:
        print('  %s' % out)
        print()
        print('  Nothing was checked. This is not a pass.')
        return 2

    if not out.strip():
        print('  No changes to %s since %s.' % (TARGET, base))
        return 0

    changed, added, removed, unparsed = read_changes(out)

    if not (changed or added or removed or unparsed):
        print('  %s changed, but no numeric value moved.' % TARGET)
        print('  (Comments, formatting, or non-numeric edits only.)')
        return 0

    bare, unclear = [], []
    for name, before, after, state in changed:
        print('  %-30s %s -> %s' % (name, before, after))
        if state == 'documented':
            print('      provenance also changed -- deliberate correction')
        elif state == 'ambiguous':
            print('      AMBIGUOUS -- several values changed in one block')
            print('      with one provenance edit; cannot say which it')
            print('      documents. Check this one by hand.')
            unclear.append(name)
        else:
            print('      VALUE MOVED ALONE -- no provenance change in this'
                  ' block')
            bare.append(name)
        print()

    for name, value, comment_moved in added:
        print('  %-30s NEW = %s' % (name, value))
        if not comment_moved:
            print('      added with no comment block -- needs a # Source:')
        print()

    for name, before in removed:
        print('  %-30s REMOVED (was %s)' % (name, before))
        print()

    if unparsed:
        print('  %d changed line(s) carry a number but match no shape this'
              % len(unparsed))
        print('  tool reads. It did NOT check them:')
        for line in unparsed[:10]:
            print('      %s' % line[:66])
        if len(unparsed) > 10:
            print('      ... and %d more' % (len(unparsed) - 10))
        print()

    print('-' * 70)
    print('  %d changed, %d added, %d removed'
          % (len(changed), len(added), len(removed)))
    if unclear:
        print('  %d value(s) could not be attributed: %s'
              % (len(unclear), ', '.join(unclear)))
    if unparsed:
        print('  %d changed line(s) were not understood -- see above.'
              % len(unparsed))
    if bare:
        print('  %d value(s) moved without their evidence: %s'
              % (len(bare), ', '.join(bare)))
        print('  Look at these before committing. A correction updates the')
        print('  number and its comment block in the same edit; a value')
        print('  that moved alone did not come from a documented check.')
    print('-' * 70)

    return 1 if (bare or unclear or unparsed) else 0


if __name__ == '__main__':
    sys.exit(main())
