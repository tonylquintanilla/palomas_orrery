"""
provenance_history.py - Run history and run-to-run delta for the
provenance scanner (ledger L-189).

The scanner reports a TOTAL. A total answers nothing on its own: "206
Tier-1" is the same sentence whether the last run said 206 or 180. The
number that informs the push call is the DELTA, and the delta needs a
record of the previous run to exist.

This module owns that record. It keeps the last MAX_RUNS runs in a single
JSON file, tracked in git, because when an audit was taken and against
which commit is itself provenance (Tony's call, 2026-08-07).

What lives here:
    - the on-disk shape and the ring buffer
    - the repo HEAD read, done without shelling out to git
    - the run-to-run comparison and its console rendering
    - the Run History table for PROVENANCE_AUDIT.md
    - is_overdue(), which nothing in this repo calls yet -- see below

INFORMATIONAL ONLY. Nothing here touches an exit code. The scanner's own
comments are emphatic that Tier-1 never gets an auto-exit gate at any
threshold; history makes the judgment better informed, it does not
automate it.

On is_overdue() being unused: a staleness check cannot live inside the
thing it watches. If the scanner never runs, the scanner cannot report
that it never ran. is_overdue() is here for the L-188 maintenance runner
to call from the outside. It is not dead code awaiting deletion -- it is
the half of L-189 whose caller has not been built yet.

Usage:
    Imported by provenance_scanner.py. Not run directly.

Role: devtool
Domain: dev_tools

Module created: August 2026 with Anthropic's Claude Opus 5 (L-189).
"""

import json
import os
from datetime import datetime, timedelta, timezone

SCHEMA_VERSION = 1

# Ring buffer depth. Six runs is Tony's call (2026-08-07): enough to see
# a trend across a working week, small enough that the file stays
# readable and its git diff stays reviewable.
MAX_RUNS = 6

# How often a run is expected. Tony's call (2026-08-11): once per day,
# not at a fixed time, because the run is manual. Date-based, therefore
# -- a run is overdue when the newest record's calendar date is older
# than the threshold, regardless of clock time.
EXPECTED_CADENCE_DAYS = 1

HISTORY_RELPATH = os.path.join('data', 'provenance_history.json')

TIER_KEYS = ('1', '2', '3', '4')


# ============================================================
# LOCATION AND REPO STATE
# ============================================================

def history_path(project_dir):
    """Absolute path to the history file for a given project tree."""
    return os.path.join(project_dir, HISTORY_RELPATH)


def head_sha(project_dir):
    """Read the repo's HEAD commit SHA without invoking git.

    Returns the 40-character SHA, or None if this tree is not a git
    checkout or HEAD cannot be resolved. Handles the two normal cases
    (a loose ref file and a packed-refs entry). A .git that is a FILE
    rather than a directory -- a worktree or submodule -- returns None
    rather than guessing.
    """
    git_dir = os.path.join(project_dir, '.git')
    if not os.path.isdir(git_dir):
        return None

    head_file = os.path.join(git_dir, 'HEAD')
    try:
        with open(head_file, 'r', encoding='utf-8') as f:
            line = f.read().strip()
    except OSError:
        return None

    if not line.startswith('ref:'):
        return line if len(line) == 40 else None

    ref = line.split(':', 1)[1].strip()

    loose = os.path.join(git_dir, *ref.split('/'))
    if os.path.isfile(loose):
        try:
            with open(loose, 'r', encoding='utf-8') as f:
                sha = f.read().strip()
            return sha or None
        except OSError:
            return None

    packed = os.path.join(git_dir, 'packed-refs')
    if os.path.isfile(packed):
        try:
            with open(packed, 'r', encoding='utf-8') as f:
                for raw in f:
                    entry = raw.strip()
                    if not entry or entry[0] in '#^':
                        continue
                    parts = entry.split(' ', 1)
                    if len(parts) == 2 and parts[1].strip() == ref:
                        return parts[0]
        except OSError:
            return None

    return None


def short_sha(sha):
    """Seven characters, or a placeholder when the SHA is unknown."""
    return sha[:7] if sha else '(no repo)'


# ============================================================
# LOAD AND SAVE
# ============================================================

def _empty_history():
    return {
        'schema_version': SCHEMA_VERSION,
        'expected_cadence_days': EXPECTED_CADENCE_DAYS,
        'max_runs': MAX_RUNS,
        'runs': [],
    }


def load_history(project_dir):
    """Read the history file. A missing or unreadable file is not an
    error -- the first run has no history, and a corrupt file should not
    stop an audit. Either returns an empty history.

    Runs are ordered oldest first.
    """
    path = history_path(project_dir)
    if not os.path.isfile(path):
        return _empty_history()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, ValueError):
        return _empty_history()

    if not isinstance(data, dict) or not isinstance(data.get('runs'), list):
        return _empty_history()

    data.setdefault('schema_version', SCHEMA_VERSION)
    data.setdefault('expected_cadence_days', EXPECTED_CADENCE_DAYS)
    data.setdefault('max_runs', MAX_RUNS)
    return data


def save_history(project_dir, history):
    """Write the history file, creating data/ if needed.

    Returns True on success, False if the write failed. A failed write is
    reported but never raises -- the audit itself has already been
    produced by the time this is called, and losing a history record is
    not a reason to lose the audit.
    """
    path = history_path(project_dir)
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
            f.write('\n')
        return True
    except OSError:
        return False


def append_run(history, record):
    """Add a run and trim to the ring-buffer depth. Oldest falls off."""
    runs = history.setdefault('runs', [])
    runs.append(record)
    depth = history.get('max_runs') or MAX_RUNS
    if len(runs) > depth:
        del runs[:len(runs) - depth]
    return history


def previous_run(history):
    """The most recent recorded run, or None if there is no history."""
    runs = history.get('runs') or []
    return runs[-1] if runs else None


# ============================================================
# BUILDING A RECORD
# ============================================================

def utc_now():
    return datetime.now(timezone.utc)


def run_id_for(moment):
    """Compact UTC stamp, matching the gallery cache builder's run_id."""
    return moment.strftime('%Y%m%dT%H%M%SZ')


def make_run_record(started, finished, project_dir, files_scanned,
                    total_findings, tier_counts, domain_counts,
                    tier1_by_file, mode='scan'):
    """Assemble one run record.

    tier_counts is keyed by int tier; it is stored keyed by string
    because JSON has no integer keys and a silent int-to-string
    conversion on save would make loaded records disagree with fresh
    ones.
    """
    return {
        'run_id': run_id_for(started),
        'started': started.isoformat(),
        'finished': finished.isoformat(),
        'mode': mode,
        'head_sha': head_sha(project_dir),
        'files_scanned': files_scanned,
        'total_findings': total_findings,
        'tier_counts': {str(t): int(tier_counts.get(int(t), 0))
                        for t in TIER_KEYS},
        'domain_counts': {str(k): int(v)
                          for k, v in sorted(domain_counts.items())},
        'tier1_by_file': {str(k): int(v)
                          for k, v in sorted(tier1_by_file.items())},
    }


# ============================================================
# COMPARISON
# ============================================================

def compare(prev, cur):
    """Run-to-run delta.

    Returns a dict with total and per-tier deltas, plus the files whose
    Tier-1 count ROSE. Files whose Tier-1 fell are not named: a drop is
    the outcome the work is aiming at, and naming it competes for
    attention with the thing that needs a decision.
    """
    prev_tiers = (prev or {}).get('tier_counts', {})
    cur_tiers = cur.get('tier_counts', {})

    tier_delta = {}
    for key in TIER_KEYS:
        tier_delta[key] = int(cur_tiers.get(key, 0)) - int(prev_tiers.get(key, 0))

    prev_files = (prev or {}).get('tier1_by_file', {})
    cur_files = cur.get('tier1_by_file', {})

    risen = []
    for fname in sorted(cur_files):
        before = int(prev_files.get(fname, 0))
        after = int(cur_files[fname])
        if after > before:
            risen.append((fname, before, after))

    return {
        'total_delta': int(cur.get('total_findings', 0))
        - int((prev or {}).get('total_findings', 0)),
        'tier_delta': tier_delta,
        'risen': risen,
    }


def _age_phrase(prev, cur):
    """Human-readable gap between two runs, e.g. '1 day ago'."""
    try:
        a = datetime.fromisoformat(prev['started'])
        b = datetime.fromisoformat(cur['started'])
    except (KeyError, TypeError, ValueError):
        return 'unknown interval'
    gap = b - a
    hours = gap.total_seconds() / 3600.0
    if hours < 1:
        return 'under an hour earlier'
    if hours < 48:
        return '%.0f hours earlier' % hours
    return '%.0f days earlier' % (hours / 24.0)


def console_lines(history, cur, first_run_note=True):
    """The lines the scanner prints after its priority summary.

    Delta, not total -- the total is already on screen directly above.
    """
    lines = []
    lines.append('Run history (%s):' % HISTORY_RELPATH.replace(os.sep, '/'))

    prev = previous_run(history)
    if prev is None:
        lines.append('  first recorded run -- nothing to compare against yet.')
        if first_run_note:
            lines.append('  This is the first run since the run-history')
            lines.append('  feature landed, so the totals above include')
            lines.append('  provenance_history.py\'s own findings. Comparing')
            lines.append('  them against a previously committed')
            lines.append('  PROVENANCE_AUDIT.md is not like for like.')
        return lines

    delta = compare(prev, cur)
    lines.append('  previous run %s (%s, HEAD %s)'
                 % (prev.get('run_id', '?'), _age_phrase(prev, cur),
                    short_sha(prev.get('head_sha'))))

    td = delta['tier_delta']
    lines.append('  delta   total %+d   T1 %+d   T2 %+d   T3 %+d   T4 %+d'
                 % (delta['total_delta'], td['1'], td['2'], td['3'], td['4']))

    if not delta['risen']:
        lines.append('  no file\'s Tier-1 count rose.')
    else:
        lines.append('  Tier-1 ROSE in %d file(s):' % len(delta['risen']))
        for fname, before, after in delta['risen']:
            lines.append('      %-44s %d -> %d  (+%d)'
                         % (fname[:44], before, after, after - before))
    return lines


# ============================================================
# STALENESS -- FOR THE L-188 RUNNER, NOT FOR THE SCANNER
# ============================================================

def is_overdue(history, now=None):
    """Has a scanner run been missed?

    Returns (overdue, days_since, last_run_id). days_since is None when
    no run has ever been recorded, which counts as overdue.

    Deliberately not called by provenance_scanner.py. A scanner that is
    running is by definition not stale, so a self-check would only ever
    report the answer nobody needs. The caller is the L-188 maintenance
    runner: L-188 is the trigger, L-189 is the data.
    """
    now = now or utc_now()
    prev = previous_run(history)
    if prev is None:
        return True, None, None

    try:
        last = datetime.fromisoformat(prev['started'])
    except (KeyError, TypeError, ValueError):
        return True, None, prev.get('run_id')

    if last.tzinfo is None:
        last = last.replace(tzinfo=timezone.utc)

    days = (now.date() - last.date()).days
    cadence = history.get('expected_cadence_days') or EXPECTED_CADENCE_DAYS
    return days > cadence, days, prev.get('run_id')


def overdue_lines(history, now=None):
    """One-or-two-line report for whatever runs the staleness check."""
    overdue, days, run_id = is_overdue(history, now)
    if not overdue:
        return ['Provenance scan is current (last run %s, %d day(s) ago).'
                % (run_id, days)]
    if days is None:
        return ['Provenance scan: NO RUN ON RECORD.']
    return ['Provenance scan is STALE: last run %s was %d day(s) ago '
            '(expected every %d).'
            % (run_id, days,
               history.get('expected_cadence_days') or EXPECTED_CADENCE_DAYS)]


# ============================================================
# REPORT TABLE
# ============================================================

def history_table(history):
    """Markdown block for PROVENANCE_AUDIT.md. Newest run first."""
    lines = []
    lines.append('## Run History')
    lines.append('')
    lines.append('The last %d recorded scanner runs, newest first. Written '
                 'by provenance_history.py and tracked in git: when an audit '
                 'was taken, and against which commit, is itself provenance.'
                 % (history.get('max_runs') or MAX_RUNS))
    lines.append('')
    lines.append('A run is expected every %d day(s). Nothing here affects '
                 'the exit code -- the delta informs the push call, it does '
                 'not make it.'
                 % (history.get('expected_cadence_days')
                    or EXPECTED_CADENCE_DAYS))
    lines.append('')

    runs = list(history.get('runs') or [])
    if not runs:
        lines.append('No runs recorded yet.')
        lines.append('')
        lines.append('---')
        lines.append('')
        return lines

    lines.append('| Run (UTC) | HEAD | Files | Total | T1 | T2 | T3 | T4 |')
    lines.append('|-----------|------|------:|------:|---:|---:|---:|---:|')

    for rec in reversed(runs):
        tiers = rec.get('tier_counts', {})
        lines.append(
            '| %s | `%s` | %d | %d | %s | %s | %s | %s |'
            % (rec.get('run_id', '?'),
               short_sha(rec.get('head_sha')),
               int(rec.get('files_scanned', 0)),
               int(rec.get('total_findings', 0)),
               tiers.get('1', 0), tiers.get('2', 0),
               tiers.get('3', 0), tiers.get('4', 0)))

    lines.append('')

    if len(runs) >= 2:
        delta = compare(runs[-2], runs[-1])
        td = delta['tier_delta']
        lines.append('Change since the previous run: total %+d, Tier-1 %+d.'
                     % (delta['total_delta'], td['1']))
        if delta['risen']:
            lines.append('')
            lines.append('Tier-1 rose in these files:')
            lines.append('')
            lines.append('| File | Before | After |')
            lines.append('|------|-------:|------:|')
            for fname, before, after in delta['risen']:
                lines.append('| %s | %d | %d |' % (fname, before, after))
        else:
            lines.append('')
            lines.append('No file\'s Tier-1 count rose.')

    lines.append('')
    lines.append('---')
    lines.append('')
    return lines
