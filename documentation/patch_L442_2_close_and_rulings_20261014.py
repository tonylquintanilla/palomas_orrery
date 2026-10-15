#!/usr/bin/env python3
"""
patch_L442_2_close_and_rulings_20261014.py -- the restamp's close, and
Tony's rulings of 2026-10-14 from his run record and chat (L-442).

Domain: dev_tools
Role: dev_tools

Built on orrery 2b0e54cc525f616e477f639e4234a284be94d14d at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched (still 86ef2df6).
Written October 14, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN: save this file in the orrery folder
(C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
open it in VS Code and click Run. Or: python patch_L442_2_close_and_rulings_20261014.py

WHAT IT DOES, in three files, all or nothing:
  LEDGER_CONSOLIDATED.md
    L-442   records Tony's run (30 of 30, pushed at 2b0e54c) and his
            "it works" on the plan's front page
    L-444   OPENED: the maintenance run fetches a served body's missing
            period from JPL, as its own step before the Horizons check
            (Tony, 2026-10-14: "yes")
    L-436   closed, dropped (Tony: "drop")
    L-441   closed, dropped (Tony: "drop")
    L-410   Note: fuzzy boundaries wherever they are meaningful
    L-401   Note: build 3 stays its own small session
  documentation/WHERE_WE_ARE.md            by section, above the marker only
  documentation/HANDOFF_L442_master_plan_restamp_20261014.md   its "Pushed at" line

It checks each file only at the lines it edits, so Tony's notes elsewhere
in them are never refused. Every anchor must match exactly once, or
nothing is written.

Undo is Discard Changes in GitHub Desktop.
"""

import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = 'LEDGER_CONSOLIDATED.md'
WWA = 'documentation/WHERE_WE_ARE.md'
HANDOFF = 'documentation/HANDOFF_L442_master_plan_restamp_20261014.md'
MARKER = '--- Your run record below this line'
RUNREC = 'documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md'


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError('missing file: %s' % rel)
    raw = open(path, 'rb').read()
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), (b'\r\n' in raw)


def rep(text, old, new, label, log, fname):
    n = text.count(old)
    if n != 1:
        raise PatchError('ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r'
                         % (fname, label, n, old[:70]))
    log.append('ok  %-16s %s' % (fname, label))
    return text.replace(old, new)


# ---------------------------------------------------------------------------
# Ledger
# ---------------------------------------------------------------------------

STAMP_ANCHOR = 'Review and RICE update Tony 6-21-2026\n'
STAMP_NEW = '''Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5
(L-442 closed on Tony's run, pushed at 2b0e54c; L-444 opened, the run
fetches a served body's missing period; L-436 and L-441 dropped; notes
on L-410 and L-401), built on 2b0e54cc.
'''

A_ANCHOR = '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n'
L444 = '''#### [L-444] The maintenance run fetches a served body's missing period from JPL, as its own step before the Horizons check (orrery, periods)
<!-- L:444 status:OPEN upd:2026-10-14 section:A flag: rice: -->
- **Tony's question, 2026-10-14**, in his run record
  (`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`, at
  2b0e54c): "should the 30-day Horizons checker initiate a fetch of the
  missing data as well as report, including a new object as never having
  been fetched?"
- **What the check does at 2b0e54c:** it reports and never fetches. A
  served body whose period is from the typed table, or has none, is
  named "typed, not fetched from JPL" or "no period fetched from JPL"
  (`horizons_check.py`, the "not compared" branch). A period record is
  written only when Tony plots the body in the orrery
  (`osculating_cache_manager.py`, which calls
  `orbital_period.build_period_record`). So eight served bodies print a
  typed period, marked, until plotted: Venus, Earth, Mars, Saturn,
  Uranus, Neptune, Apophis and Halley (L-431). A new keyed object has
  its identity asked on the next run and its period never.
- **Ruled, 2026-10-14, on Claude's recommendation; Tony: "yes".** A
  separate GENERATOR row of the maintenance run, before the Horizons
  check:
  - it fetches with the orrery's own code, the path plotting takes, so a
    period fetched this way is the same record plotting would write;
  - it asks JPL only for what is missing: a keyed, served object with no
    fetched period record, including a new one the first time the run
    sees it. On most days it asks nothing;
  - the Horizons check runs after it and compares the new periods with
    JPL the same day;
  - a fetch that fails is named (UNREACHABLE, the convention for every
    row that needs the network), never passed;
  - the check stays a check: it does not fill gaps itself, so a missing
    period cannot stop being reported.
- **Effect:** the eight bodies print JPL's period on the website after
  the next maintenance run and push, without being plotted.
**Gap:** a small orrery build, its own session: the row, its dashboard
button (every new check gets a button), its planted faults (a fetch that
fails, a body already fetched asked again, a period written by another
path than plotting's), and the first live run.
**Ref:** `horizons_check.py`; `orbital_period.py`
(`build_period_record`); `osculating_cache_manager.py`;
`export_objects.py`; `orrery_maintenance_run.py`;
`palomas_orrery_dashboard.py`; L-431; L-395; L-443 (its new objects get
their periods this way); skills/horizons-orbital-mechanics/SKILL.md,
Where the Check Lives.

'''

L442_GAP_OLD = '''**Gap:** none. The next session confirms its loaded copy of
ledger-and-session-records reads 1.21 before ledger work.'''
L442_GAP_NEW = '''- **2026-10-14, run and pushed.** Tony's run record
  (`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`, at 2b0e54c):
  the plan's new front page, "it works"; patch_L442_1 ran ("patch
  applied (47 edits in 8 files)"); the maintenance run, "30 of 30
  gating checkers passed", the manifest and the ledger index rewritten
  and Tier-1 on the gate path 0; ledger-and-session-records 1.21
  reinstalled ("done"); `documentation/project_instructions_v3_97.md`
  saved and copied to the Project ("done"); pushed at
  2b0e54cc525f616e477f639e4234a284be94d14d.
- **His notes in the same record, filed by patch_L442_2:** the Horizons
  check's question, ruled the same night (L-444); "-- drop" on L-436 and
  L-441 (closed); fuzzy boundaries wherever they are meaningful (a Note
  on L-410); L-401's build 3 as its own small session (a Note on L-401).
**Gap:** none. The next session confirms its loaded copy of
ledger-and-session-records reads 1.21 before ledger work.'''

L436_HEAD_OLD = '''#### [L-436] The orrery away from the machine: the linked session from the phone; not Pyodide (idea)
<!-- L:436 status:OPEN upd:2026-10-13 section:D.Feature-C flag: rice: -->'''
L436_HEAD_NEW = '''#### [L-436] The orrery away from the machine: the linked session from the phone; not Pyodide (idea, dropped 2026-10-14)
<!-- L:436 status:DONE upd:2026-10-14 section:C flag: rice: -->'''
L436_GAP_OLD = '''**Gap:** not scoped; an idea on record. Unscored until opened (an item
outside any list gets a coarse score then).'''
L436_GAP_NEW = '''**CLOSED 2026-10-14, dropped by Tony.** His run record
(`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`, at 2b0e54c),
on this item in Where We Are's not-urgent list: "-- drop". Confirmed in
chat the same night: "yes". Its two Tony-actions (whether a hover
script joins L-401 build 3; the first command from the phone) are
struck with it: an idea dropped leaves no work behind.
**Gap:** none.'''

L441_HEAD_OLD = '''#### [L-441] The dashboard's "when" index, generated from tags (dashboard)
<!-- L:441 status:OPEN upd:2026-10-14 section:A flag: rice: -->'''
L441_HEAD_NEW = '''#### [L-441] The dashboard's "when" index, generated from tags (dashboard, dropped 2026-10-14)
<!-- L:441 status:DONE upd:2026-10-14 section:C flag: rice: -->'''
L441_GAP_OLD = '''**Gap:** a design talk, when Tony wants it.'''
L441_GAP_NEW = '''**CLOSED 2026-10-14, dropped by Tony.** His run record
(`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`, at 2b0e54c),
on this item in Where We Are's not-urgent list: "-- drop". Confirmed in
chat the same night: "yes".
**Gap:** none.'''

L410_GAP_OLD = '''**Gap:** a design talk before any build. The Sun slice's ninth item
(L-412).'''
L410_GAP_NEW = '''- **Tony, 2026-10-14**, in his run record
  (`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`, at 2b0e54c),
  beside "The fuzzy outer corona, with the dust cloud; the exosphere the
  same way": "in general we should implement fuzzy boundaries where they
  are meaningful." Confirmed in chat the same night: "yes". So the design
  talk takes up the rule, not only the corona and the exosphere: which
  drawn edges are known only as ranges, and which of them a fade would
  teach better than a shell.
**Gap:** a design talk before any build. The Sun slice's ninth item
(L-412).'''

L401_GAP_OLD = '''**Gap:** Builds 1 and 2 are built and accepted. Left, build 3: the fly-to buttons, the parameters window, the'''
L401_GAP_NEW = '''- **Tony, 2026-10-14**, in his run record
  (`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`, at 2b0e54c),
  on the road's stage 5: "**L-401 build 3** afterwards: the fly-to
  buttons, the parameters window, the animation's uncertainty. Small,
  and its own session." Confirmed in chat the same night: "yes".
**Gap:** Builds 1 and 2 are built and accepted. Left, build 3: the fly-to buttons, the parameters window, the'''


def patch_ledger(t, log):
    f = 'LEDGER'
    if '#### [L-444]' in t:
        raise PatchError('REFUSED: L-444 already exists in the ledger')
    if '<!-- L:442 status:DONE ' not in t:
        raise PatchError('REFUSED: L-442 is not in the ledger as closed; run patch_L442_1 first')
    t = rep(t, L442_GAP_OLD, L442_GAP_NEW, 'L-442 run recorded', log, f)
    t = rep(t, L436_GAP_OLD, L436_GAP_NEW, 'L-436 closed (dropped)', log, f)
    t = rep(t, L436_HEAD_OLD, L436_HEAD_NEW, 'L-436 status', log, f)
    t = rep(t, L401_GAP_OLD, L401_GAP_NEW, 'L-401 Note', log, f)
    t = rep(t, L410_GAP_OLD, L410_GAP_NEW, 'L-410 Note', log, f)
    t = rep(t, L441_GAP_OLD, L441_GAP_NEW, 'L-441 closed (dropped)', log, f)
    t = rep(t, L441_HEAD_OLD, L441_HEAD_NEW, 'L-441 status', log, f)
    t = rep(t, A_ANCHOR, A_ANCHOR + L444, 'L-444 opened', log, f)
    t = rep(t, STAMP_ANCHOR, STAMP_NEW + STAMP_ANCHOR, 'header stamp', log, f)
    return t


# ---------------------------------------------------------------------------
# Where We Are, above the marker only
# ---------------------------------------------------------------------------

W = []
W.append(('header', '''Last updated: October 14, 2026, night: the master plan restamped; its history moved out.
- Written at orrery 9248845 and gallery 86ef2df.''', '''Last updated: October 14, 2026, late: the restamp ran and is pushed; your notes filed.
- Written at orrery 2b0e54c and gallery 86ef2df.'''))

W.append(('the box', '''> - The master plan is strategy only. The order lives on the road
>   below; what is done lives in the ledger. (Your ruling, Oct 13.)
> - The plan's dated history and its lineage moved to one record,
>   `MASTER_PLAN_HISTORY.md`. (Your ruling, Oct 14.)
> - L-433 (the road after the Sun and Earth rooms) closed; the objects
>   work is L-443 (the objects to the website).
>
> **Do next:** *The design session for the orrery's objects on the
> website, L-443 (the objects to the website), from its brief.*
>
> **Needs you now:**
> - *Run patch_L442_1, then the maintenance run; reinstall
>   ledger-and-session-records 1.21; copy protocol v3.97 to the
>   Project; commit; push.*''', '''> - The restamp ran clean (30 of 30) and is pushed at 2b0e54c. The
>   plan is strategy; the road below is the order.
> - Ruled: the run fetches a served body's missing period from JPL,
>   as its own step: L-444 (the missing periods).
> - Dropped: L-436 (the orrery from your phone) and L-441 (the
>   dashboard's "when" index).
>
> **Do next:** *Build L-444 (the missing periods): small, orrery only.
> Then the design session for L-443 (the objects to the website).*
>
> **Needs you now:**
> - *Run patch_L442_2, then the maintenance run; commit; push.*'''))

W.append(('road: stage 8a', '''  8.   [done]  The served objects are checked against JPL Horizons, from
               the orrery's run; the periods passed live, Oct 14.
''', '''  8.   [done]  The served objects are checked against JPL Horizons, from
               the orrery's run; the periods passed live, Oct 14.
  8a.  [next]  *The run fetches each served body's missing period from
               JPL: L-444 (the missing periods).*
               << new this session
'''))

W.append(('road: stage 11 marks reset', ''' 11.   [next]  *The rest of the orrery's objects come to the website:
               L-443 (the objects to the website), design first.*
               << moved this session
''', ''' 11.   [next]  The rest of the orrery's objects come to the website:
               L-443 (the objects to the website), design first.
'''))

W.append(('settled: two lines in', '''  status. The plan's history and lineage: MASTER_PLAN_HISTORY.md. (Oct 13, 14)
''', '''  status. The plan's history and lineage: MASTER_PLAN_HISTORY.md. (Oct 13, 14)
- Fuzzy boundaries wherever they are meaningful, not only the corona
  and the exosphere. (Oct 14)
- A served body's missing period is fetched by the run, before the
  check, with the orrery's own code. (Oct 14)
'''))

W.append(('settled: Hills cloud line out', '''- The Hills cloud follows its paper (Fig. 3, its text), cited; to 10,000 AU. (Oct 10)
''', ''))

W.append(('signals', '''## Signals

Read from files when this page was written, not typed from memory.
- Last cache build: 20261014T225537Z, ok, no retry (gallery 86ef2df).
- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 5ca56df).''', '''## Signals  **>> UPDATED THIS SESSION**

Read from files when this page was written, not typed from memory.
- Last cache build: 20261014T225537Z, ok, no retry (gallery 86ef2df).
- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 2b0e54c).'''))

W.append(('waiting: two dropped', '''2. Choosing a date, and animation.
3. The orrery from your phone: L-436 (away from the machine), an idea.
4. The dashboard's "when" index: L-441, recorded for later.
''', '''2. Choosing a date, and animation.
'''))

W.append(('details: your notes', '''- Your notes of Oct 12: `WHERE_WE_ARE_10-12-26_2212_run_record.md`
''', '''- Your notes of Oct 14: `WHERE_WE_ARE_10-14-26_2250_run_record.md`
'''))

W.append(('details: L-436 line out', '''- L-436 (away from the machine): `DESIGN_L436_orrery_away_from_the_machine_20261013.md`
''', ''))

W.append(('details: next', '''- *Next: `HANDOFF_L438_objects_to_website_brief_20261013.md`; its item
  is now L-443 (the objects to the website)*''', '''- *Next: L-444 (the missing periods) in the ledger, then
  `HANDOFF_L438_objects_to_website_brief_20261013.md`, now L-443*'''))

W.append(('waiting: heading', '## Waiting on you\n', '## Waiting on you  **>> UPDATED THIS SESSION**\n'))


def patch_wwa(t, log):
    f = 'WHERE_WE_ARE'
    if t.count(MARKER) != 1:
        raise PatchError('ANCHOR FAIL [WHERE_WE_ARE run-record marker]')
    m = t.index(MARKER)
    top, bottom = t[:m], t[m:]
    for label, old, new in W:
        top = rep(top, old, new, label, log, f)
    above = top.count('\n')
    if above > 130:
        raise PatchError('WHERE_WE_ARE would stand %d lines above the marker (cap 130)' % above)
    log.append('ok  %-16s %d lines above the marker (cap 130)' % (f, above))
    return top + bottom


def patch_handoff(t, log):
    return rep(t, 'touched. Pushed at: (Tony fills in after his push).',
               'touched. Pushed at 2b0e54cc525f616e477f639e4234a284be94d14d\n'
               '(Tony\'s push of 2026-10-14; his run record is\n'
               '`documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md`).',
               'Pushed at line', log, 'HANDOFF_L442')


def main():
    log = []
    try:
        if not os.path.exists(os.path.join(ROOT, RUNREC)):
            raise PatchError('REFUSED: %s is not in this folder; this patch quotes it' % RUNREC)
        texts, crlf = {}, {}
        for rel in (LEDGER, WWA, HANDOFF):
            texts[rel], crlf[rel] = read(rel)
        out = {
            LEDGER: patch_ledger(texts[LEDGER], log),
            WWA: patch_wwa(texts[WWA], log),
            HANDOFF: patch_handoff(texts[HANDOFF], log),
        }
        for rel, t in out.items():
            bad = sum(1 for ch in t if ord(ch) > 127)
            if bad:
                raise PatchError('%s: %d non-ASCII character(s) after the edits' % (rel, bad))
    except PatchError as e:
        print('ERROR: %s' % e)
        print('NOTHING was written.')
        sys.exit(1)
    for line in log:
        print(line)
    total = 0
    for rel, t in out.items():
        data = t.encode('utf-8')
        open(os.path.join(ROOT, rel), 'wb').write(data)
        total += len(data)
        if crlf[rel]:
            print('note: %s was CRLF in the working copy; written LF' % rel)
    print()
    print('patch applied (%d edits in %d files, %d bytes)' % (len(log), len(out), total))
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect the ledger index to move')
    print('     L-436 and L-441 to the closed section, and 30 of 30.')
    print('  2. Move this script into documentation/; commit and push.')
    print('Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
