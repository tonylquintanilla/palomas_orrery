#!/usr/bin/env python3
"""
patch_L442_1_master_plan_restamp_20261014.py -- the master plan's
restamp (v36) and Tony's seven kinds of document (L-442).

Domain: dev_tools
Role: dev_tools

Built on orrery 9248845ca8516dcee3498f07c554e6a24426c23c at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched (read at 86ef2df6 for the summary's signals).
Written October 14, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN: save this file in the orrery folder
(C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\),
open it in VS Code and click Run. Or: python patch_L442_1_master_plan_restamp_20261014.py

WHAT IT DOES, in eight files, all or nothing:
  documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md   v35 -> v36
  documentation/MASTER_PLAN_HISTORY.md               NEW (refuses if it exists)
  skills/ledger-and-session-records/SKILL.md         1.20 -> 1.21
  documentation/SKILL_HISTORIES.md                   receives the skill's 1.18 entry
  PROJECT_INSTRUCTIONS.md                            v3.96 -> v3.97
  documentation/PROJECT_INSTRUCTIONS_HISTORY.md      receives v3.94
  LEDGER_CONSOLIDATED.md                             L-442 (closed), L-443 (opened),
                                                     L-433 closed, notes on L-221, L-431
  documentation/WHERE_WE_ARE.md                      by section, above the run-record marker

It refuses to run unless L-431 (orbital periods) is closed in the ledger,
so it cannot run before build 3's close. Every anchor must match exactly
once, or nothing is written. After writing it checks its own result
(the post-checks below) and, if one fails, restores every file and says
which.

Permanent parts: the new history file, the skill's Document Stack, the
protocol entry, the ledger items. The script itself is one-shot; move it
into documentation/ after it has run.

Undo is Discard Changes in GitHub Desktop.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

PLAN = 'documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md'
HIST = 'documentation/MASTER_PLAN_HISTORY.md'
SKILL = 'skills/ledger-and-session-records/SKILL.md'
SKHIST = 'documentation/SKILL_HISTORIES.md'
PROTO = 'PROJECT_INSTRUCTIONS.md'
PHIST = 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md'
LEDGER = 'LEDGER_CONSOLIDATED.md'
WWA = 'documentation/WHERE_WE_ARE.md'

MARKER = '--- Your run record below this line'


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError('missing file: %s' % rel)
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    text = raw.replace(b'\r\n', b'\n').decode('utf-8')
    return text, was_crlf


def once(text, old, label):
    n = text.count(old)
    if n != 1:
        raise PatchError('ANCHOR FAIL [%s]: expected 1 match, got %d: %r'
                         % (label, n, old[:70]))


def rep(text, old, new, label, log, fname):
    once(text, old, label)
    log.append('ok  %-34s %s' % (fname, label))
    return text.replace(old, new)


def span(text, start, end, label):
    """Index range from the start of `start` up to (not including) `end`."""
    once(text, start, label + ' (start)')
    once(text, end, label + ' (end)')
    a = text.index(start)
    b = text.index(end)
    if b <= a:
        raise PatchError('ANCHOR FAIL [%s]: end before start' % label)
    return a, b


# ---------------------------------------------------------------------------
# 1. The master plan
# ---------------------------------------------------------------------------

PLAN_DOCKIND = ('<!-- Doc-Kind: hand | The strategy for the interactive gallery: '
                'what the website is for, how it is built, and where the work '
                'goes over months. The order of the work is the road on '
                'WHERE_WE_ARE.md; status is the ledger\'s. -->\n')

SUMMARY = r'''## Executive summary -- v36, October 14, 2026

Built on orrery `9248845ca8516dcee3498f07c554e6a24426c23c` at
https://github.com/tonylquintanilla/palomas_orrery and gallery
`86ef2df6313f956f5c9e49611e6a2bdd0e95da29` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on 2026-10-14. This summary is rewritten at every restamp, never
carried forward.

**What this plan is, and what it is not.** It is the strategy for the
interactive gallery at palomasorrery.com: what the website is for, how
it is built, and where the work goes over months. It does not say what
is next. The order of the work lives in one place only, the road on
`documentation/WHERE_WE_ARE.md`. What is done, and what was ruled, is
the ledger's. Read this plan when a decision changes direction, when a
new kind of work opens, or at a restamp. (Tony's ruling, 2026-10-13.)

**Seven kinds of document** (Tony, 2026-10-13; the full statement, with
when each is read, is in the skill ledger-and-session-records):
1. Strategy: this plan. Where the work goes over months.
2. Tactics: Where We Are, and the road on it. What is next, in order.
3. Communication: briefs, design records, manifests, handoffs, review
   prompts and Tony's run records. Each carries work from one session,
   person or model to another.
4. Logistics: the ledger. Every job's history and the open work
   orders. Never a schedule.
5. The field manual: the protocol and the skills. How we work together.
6. Reference: generated documents read for the current state, such as
   the module atlas and the provenance audit.
7. The work: the code builds. The render is its ground truth; the SHA
   is its state.

**The end goal** (Section 5a). The website does what the desktop
orrery does, for anyone, with nothing to install, and with a date to
choose within the range the data covers.

**Where the work stands, by the five segments of Section 5a.**
- Segment 3, the website draws: done. Three rooms are live: the Sun
  (2026-08-29), Earth (2026-09-10), and the Solar System room, the
  gallery's front door. Each was accepted on Tony's phone and desktop.
- Segment 2, the numbers reach the website without a hand copy: done.
  The orrery exports its constants and its objects, and the website
  pulls both. The newest are the orbital periods: JPL's own, in the
  orrery and on the website since 2026-10-14.
- Segment 1, the orrery's numbers are right: worked room by room, never
  as one sweep. Earth is the first closed slice (2026-09-22). The Sun's
  is open.
- Segment 5, shipping: the three rooms are shipped. The Solar System
  room becomes the page a bare link opens once every room it leads
  into prints only served numbers.
- Segment 4, Jupiter and Saturn's golden artifact: no longer next. It
  falls in the shells phase, after the orrery's objects reach the
  website.

**The direction** (Tony, 2026-10-10 and 2026-10-12; L-433). Section
5a, The direction, has the paragraph. In short: finish the Sun and
Earth rooms, with the Solar System room's features, as the template
for every body's room; bring the rest of the orrery's objects to the
website; then the inner planets' rooms, with the Earth System layers
beside them.

**Signals, read from files.** Last cache build: 20261014T225537Z,
swapped in first time (gallery `data/cache_swap_log.jsonl`). Tier-1 on
what leaves the orrery: 0 (`PROVENANCE_AUDIT.md`). Whole tree: 280:
orrery 116, Earth System 149, stars 13, utilities 2.

**How to read the rest.** Sections 1 to 4 are the architecture.
Section 5 is the phases. Section 5a is the shape of the work: the end
goal, one pipeline in one direction, the five segments, the braid and
the direction. Section 6 is the prep work and Section 7 the
architectural decisions, both with their history. The plan's dated
history moved out on 2026-10-14 to
`documentation/MASTER_PLAN_HISTORY.md`: the critical path's session
record from August 23 to September 29, 2026, and the lineage (formerly
Section 10). The status block below is the running record the
restamps kept from July to v35; it is not updated.
'''

STATUS_NEXT_OLD = ('**Next: the order is in the executive summary above and in Section\n'
                   "5a's newest subsection, 2026-09-29.**")
STATUS_NEXT_NEW = ('**Next: the order lives on the road on `documentation/WHERE_WE_ARE.md`\n'
                   "(v36, Tony's ruling of 2026-10-13; until v36 this line named Section\n"
                   "5a's newest subsection).**")

LASTUPD_OLD = '**Last updated:** September 29, 2026 (v35: a DESIGN BUILD, L-363. The'
LASTUPD_NEW = ('**Last updated:** October 14, 2026 (v36: a DOCUMENTATION build, L-442,\n'
               "at Tony's direction. The plan becomes strategy only, on his ruling of\n"
               '2026-10-13: the road on Where We Are carries the order and the ledger\n'
               'the status. The executive summary is rewritten; Section 5a keeps the\n'
               'shape and gains The direction (L-433); the dated history of the\n'
               'critical path and the lineage (Section 10) move to\n'
               "`documentation/MASTER_PLAN_HISTORY.md`, on Tony's ruling of 2026-10-14;\n"
               'Sections 6 and 7 get one pass against the ledger; with Anthropic\'s\n'
               'Claude Opus 5.5. v35, September 29, 2026: a DESIGN BUILD, L-363. The')

V33_START = 'Claude Opus 5.5. v33, September 22, 2026: a DESIGN BUILD, L-322 Stage\n'
V33_END = 'Opus 5.5 (the gallery half and this update).)\n'

FIVEA_HOME_OLD = '''**Since v34 (2026-09-28) this section is the critical path's only
home.** `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`, its readable companion
since August 16, is retired as a dated record (L-333, L-362); the
executive summary at the top of this document gives its short form.'''
FIVEA_HOME_NEW = '''**Since v36 (2026-10-14) this section is the SHAPE of the work, not
its order.** The order lives on the road on
`documentation/WHERE_WE_ARE.md`, and the status in the ledger (Tony's
ruling of 2026-10-13, L-442). Its dated subsections, 2026-08-23 to
2026-09-29, moved word for word to `documentation/MASTER_PLAN_HISTORY.md`
PART 1. `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`, its readable companion
since August 16, was retired as a dated record at v34 (L-333, L-362).'''

SPINE_OLD = '''This section is the spine. Detail lives in Sections 5, 6 and 7; history
of every ruling stays in Section 6. When 5a and another section
disagree, 5a is the one that was rewritten last -- reconcile, do not
guess.'''
SPINE_NEW = '''This section is the spine of the strategy. Detail lives in Sections 5,
6 and 7; history of every ruling stays in Section 6. When 5a and
another section disagree, 5a is the one that was rewritten last --
reconcile, do not guess. The order of the next jobs is not this
section's: it is the road's.'''

L154_5A_OLD = '''**A consequence to record rather than resolve here:** L-154 is BLOCKED
in the ledger, and this order unblocks it. The plan carries SEQUENCING
authority and the ledger carries STATUS authority (L-221), so that is a
ledger edit, not something this section may assert around.'''
L154_5A_NEW = '''**A consequence recorded at the time:** L-154 was BLOCKED in the ledger,
and this order unblocked it. The ledger made that edit; L-154 closed
DONE on 2026-08-24. (Until v36 this paragraph also said the plan
carries sequencing authority. Since 2026-10-13 the road on Where We
Are does, and the ledger keeps status: L-442.)'''

FIVEA_MOVED_START = '### You are here -- read 2026-08-23 at orrery `38923c1`, gallery `493a0bd`\n'
FIVEA_MOVED_END = '### What this section deliberately does not carry\n'

FIVEA_REPLACEMENT = '''### The direction, after the Sun and Earth rooms

Tony's direction of 2026-10-10, confirmed on 2026-10-12 (L-433). The
Sun and Earth rooms are finished first, and "the Sun and Earth rooms"
includes the Solar System room's features: the fuzzy boundaries and
the scattered disk sit inside that work, not after it. Finished, they
are the template for every body's room. The rest of the orrery's
objects then come to the website as plotted positions. Then the inner
planets get their rooms, Mercury, Venus and Mars, from the template,
with Jupiter and Saturn after them; the Earth System layers are built
beside the planets' rooms, not after them. Encounters and the golden
artifacts stay paths to choose from then, not fixed steps. The checks
that keep the work honest are cleared beside the rooms, so nothing is
in front of them when they close. The end of the road is the website
doing what the desktop orrery does, with a date to choose, within the
range the data covers.

### Where the order and the history are

- The order of the work: the road on `documentation/WHERE_WE_ARE.md`.
- What is done, and what was ruled: `LEDGER_CONSOLIDATED.md`.
- This section is the shape of the work; its dated account, August 23
  to September 29, 2026, is `documentation/MASTER_PLAN_HISTORY.md`
  PART 1.

'''

NOTCARRY_OLD = '''Model assignments, per-item dependency chains and RICE scores. Those
belong in the ledger, which is the in-flight record; a plan that
duplicates them goes stale between sessions and then contradicts them.'''
NOTCARRY_NEW = '''Model assignments, per-item dependency chains and RICE scores. Those
belong in the ledger, which is the in-flight record; a plan that
duplicates them goes stale between sessions and then contradicts them.
Nor the order of the next jobs, which is the road's on Where We Are,
nor a dated account of sessions, which since 2026-10-14 is
`documentation/MASTER_PLAN_HISTORY.md` (L-442).'''

S6_L154_OLD = '''FIRST work, not work waiting on the scanner. Its ledger status still
reads BLOCKED; the ledger is the status authority, so that edit belongs
there and not here.'''
S6_L154_NEW = '''FIRST work, not work waiting on the scanner. Its ledger status then
read BLOCKED; the ledger is the status authority, so that edit belonged
there and not here. (The ledger made it: L-154 closed DONE on
2026-08-24. Corrected at v36.)'''

S6_L163_OLD = '''NOT part of the above -- deliberately deferred to the L-156 cluster,
which cites this item's coverage-gap pattern as its own precedent.'''
S6_L163_NEW = '''NOT part of the above -- deliberately deferred to the L-156 cluster,
which cites this item's coverage-gap pattern as its own precedent.
(Done since: L-437 retired MODULE_DOMAIN_MAP on 2026-10-13; the scanner
reads each module's own Domain: tag. Corrected at v36.)'''

D12_OLD = '''    Two earlier candidates are retired: exporting to a JSON artifact
    (rests on a generation step and a run trigger that do not exist), and'''
D12_NEW = '''    **Superseded in part, recorded at v36:** L-322 (its ruling 6) built
    the JSON export after all -- `export_constants.py` writes
    `data/constants_export.json` (2026-09-16), and the gallery pulls it;
    that is the route numbers take today. The paragraph below is the
    reasoning as ruled on 2026-08-08.
    Two earlier candidates are retired: exporting to a JSON artifact
    (rests on a generation step and a run trigger that do not exist), and'''

D13_OLD = '''13. **Generator shape and run cadence.** DISSOLVED by decision 12. There
    is no generation step -- "generation" is Tony editing the store.'''
D13_NEW = '''13. **Generator shape and run cadence.** DISSOLVED by decision 12. There
    is no generation step -- "generation" is Tony editing the store.
    (Since 2026-09-16 there is one: `export_constants.py`, run by the
    orrery maintenance run, L-322. Recorded at v36.)'''

D18_OLD = '''    `thickness_km` says 30, so the prose is more accurate than the data
    beside it.'''
D18_NEW = '''    `thickness_km` says 30, so the prose is more accurate than the data
    beside it.
    (Answered as method since: provenance-discipline, When the source
    gives a range -- the range is stored as rows and the drawn value is
    a declared construction over them. Recorded at v36.)'''

S10_MOVED_START = '## Section 10 -- Lineage\n'
S10_MOVED_END = '## Section 11 -- Protocol & Skills Review (from Phase 0)\n'
S10_REPLACEMENT = '''## Section 10 -- Lineage

Moved on 2026-10-14, word for word, to
`documentation/MASTER_PLAN_HISTORY.md` PART 2 (Tony's ruling of
2026-10-14, L-442). It was last added to at v19, 2026-08-23.

---

'''

S11_OLD = '''to be written, five days after it shipped with the Sun exhibit. The
order lives in Section 5a, dated 2026-09-03, and only there (the
same fix-the-producer ruling as the paragraph above).'''
S11_NEW = '''to be written, five days after it shipped with the Sun exhibit. The
order lives on the road on `documentation/WHERE_WE_ARE.md`, and only
there (Tony's ruling of 2026-10-13; until v36 this line named Section
5a, dated 2026-09-03; the same fix-the-producer ruling as the
paragraph above).'''

HIST_HEAD = '''<!-- Doc-Kind: hand | The master plan's dated history, moved out of the plan on 2026-10-14: the critical path's session record, August 23 to September 29, 2026, and the plan's lineage. A record; not updated. -->
# MASTER PLAN HISTORY -- Paloma's Orrery Interactive Gallery

Cut from orrery 9248845ca8516dcee3498f07c554e6a24426c23c at
https://github.com/tonylquintanilla/palomas_orrery (branch main), by
patch_L442_1_master_plan_restamp_20261014.py. Written October 14, 2026
with Anthropic's Claude Opus 5.5.

THIS FILE IS A RECORD, NOT A PLAN. Nothing in it says what is next.
It holds the dated history that used to sit inside
`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`, moved out word for
word when the plan became strategy only (Tony's rulings of 2026-10-13
and 2026-10-14, L-442). It is no longer updated. What came after is in
the ledger and on the road in `documentation/WHERE_WE_ARE.md`. Like the
plan's two retired companions, it is a dated record, not a versioned
copy of the plan; git holds the plan's earlier versions.

  PART 1  The critical path's session record, from Section 5a: the
          "You are here" table of 2026-08-23 and the dated subsections
          2026-08-25 to 2026-09-29.
  PART 2  The plan's lineage, formerly its Section 10: the sessions it
          drew from and what each version added, through v19
          (2026-08-23).

================================================================
PART 1 -- THE CRITICAL PATH'S SESSION RECORD (from Section 5a)
================================================================

'''

HIST_PART2 = '''
================================================================
PART 2 -- THE LINEAGE (formerly Section 10)
================================================================

'''


def patch_plan(text, log):
    f = 'MASTER_PLAN'
    if text.startswith('<!-- Doc-Kind'):
        raise PatchError('the plan already opens with a Doc-Kind line')
    # Bottom-up: Section 11, Section 10 move, Section 7, Section 6, 5a, status, summary.
    text = rep(text, S11_OLD, S11_NEW, 'Section 11: the order is the road', log, f)
    a, b = span(text, S10_MOVED_START, S10_MOVED_END, 'Section 10 span')
    moved10 = text[a:b]
    text = text[:a] + S10_REPLACEMENT + text[b:]
    log.append('ok  %-34s %s' % (f, 'Section 10 moved out (%d bytes)' % len(moved10.encode())))
    text = rep(text, D18_OLD, D18_NEW, 'Section 7 decision 18 note', log, f)
    text = rep(text, D13_OLD, D13_NEW, 'Section 7 decision 13 note', log, f)
    text = rep(text, D12_OLD, D12_NEW, 'Section 7 decision 12 note', log, f)
    text = rep(text, S6_L163_OLD, S6_L163_NEW, 'Section 6 L-163 line', log, f)
    text = rep(text, S6_L154_OLD, S6_L154_NEW, 'Section 6 L-154 line', log, f)
    text = rep(text, NOTCARRY_OLD, NOTCARRY_NEW, '5a: does not carry', log, f)
    a, b = span(text, FIVEA_MOVED_START, FIVEA_MOVED_END, '5a dated span')
    moved5a = text[a:b]
    text = text[:a] + FIVEA_REPLACEMENT + text[b:]
    log.append('ok  %-34s %s' % (f, '5a dated subsections moved out (%d bytes)' % len(moved5a.encode())))
    text = rep(text, L154_5A_OLD, L154_5A_NEW, '5a: L-154 paragraph', log, f)
    text = rep(text, SPINE_OLD, SPINE_NEW, '5a: the spine', log, f)
    text = rep(text, FIVEA_HOME_OLD, FIVEA_HOME_NEW, '5a: opening', log, f)
    a, b = span(text, V33_START, V33_END, 'v33 stamp')
    text = text[:a] + 'Claude Opus 5.5.)\n' + text[b + len(V33_END):]
    log.append('ok  %-34s %s' % (f, 'rolling stamp: v33 dropped'))
    text = rep(text, LASTUPD_OLD, LASTUPD_NEW, 'rolling stamp: v36 added', log, f)
    text = rep(text, STATUS_NEXT_OLD, STATUS_NEXT_NEW, 'status block: Next line', log, f)
    a, b = span(text, '## Executive summary -- v35, September 29, 2026\n',
                'restamps have kept since July; this summary is the short form of it.\n',
                'summary')
    b = b + len('restamps have kept since July; this summary is the short form of it.\n')
    text = text[:a] + SUMMARY + text[b:]
    log.append('ok  %-34s %s' % (f, 'executive summary rewritten (v36)'))
    text = PLAN_DOCKIND + text
    log.append('ok  %-34s %s' % (f, 'Doc-Kind line added'))
    return text, moved5a, moved10


# ---------------------------------------------------------------------------
# 2. The skill
# ---------------------------------------------------------------------------

SK_VER_OLD = '''Skill version: 1.20 | 2026-10-11, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 1bbd9fe1.'''
SK_VER_NEW = '''Skill version: 1.21 | 2026-10-14, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 9248845c. v1.21 (L-442) carries Tony's seven kinds of
document. The Document Stack is rewritten as the seven, each with when
it is read: strategy (the master plan), tactics (Where We Are and its
road), communication, logistics (the ledger), the field manual,
reference, and the work. Sequencing moves from the plan to the road on
Where We Are; the ledger keeps status. A table maps the Doc-Kind values
in use onto the seven. Riding this version: Where We Are's section and
the RICE bullet name the road as the order's home. Tony, 2026-10-13:
"master plan: strategic - where we are: tactical - handoffs: orders
and reports - ledger: logistics."
Earlier: 1.20 | 2026-10-11, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ 1bbd9fe1.'''

SK_118_START = '''Earlier: 1.18 | 2026-10-08, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ b0b3df82.'''
SK_118_END = '''names provenance-cross-check for a review prompt carried to another
model.
'''

SK_OLDER_OLD = '''on 2026-10-05 (L-418), 2026-10-07 (L-422), 2026-10-08 (L-418),
2026-10-10 (L-395) and 2026-10-11 (L-421).'''
SK_OLDER_NEW = '''on 2026-10-05 (L-418), 2026-10-07 (L-422), 2026-10-08 (L-418),
2026-10-10 (L-395), 2026-10-11 (L-421) and 2026-10-14 (L-442).'''

SK_CONTENTS_OLD = '- The Document Stack (the round trip)\n'
SK_CONTENTS_NEW = '- The Document Stack (seven kinds of document)\n'

SK_STACK_START = '## The Document Stack (the round trip)\n'
SK_STACK_END = '**The same rule reaches past handoffs and manifests** (Tony\'s\n'

SK_STACK_NEW = r'''## The Document Stack (seven kinds of document)

Tony's ruling of 2026-10-13 (L-442), in his words, in the order he gave
them: "master plan: strategic - where we are: tactical - handoffs:
orders and reports - ledger: logistics." Then: "by handoff I am
conflating different documents, briefs, design manifests, closing
reports and maybe others. But they are still all communication
documents." "And of course there are code builds. Which is the work
itself." And: "the ledger is like a maintenance management system, both
history and work orders with priority, but by itself is not a schedule
or a plan. Skills and the project instructions as you said is how we
work together. You could say it's our field manual. There are other
documents that are references like the module atlas and the provenance
scanner report." He said "Yes" to the statement below.

Seven kinds, each with what it is for and WHEN IT IS READ:

1. STRATEGY: the master plan. What the gallery is for, how it is
   built, where the work goes over months. Read when a decision changes
   direction, when a new class of work opens, and at a restamp. Never
   read to learn what is next.
2. TACTICS: Where We Are, and on it the road. What is next and in what
   order. Read at the start of every session and written at the end.
   The ONLY place sequencing lives; the plan defers to it.
3. COMMUNICATION: briefs, design records, manifests, closing reports
   and handoffs, coordination notes, review prompts and returns, and
   the run record in Tony's hand. A document that carries work from
   one session, person or model to another. Written once, read by its
   receiver, then history. A ruling in one of them is not recorded
   until it reaches the ledger.
4. LOGISTICS: the ledger. A maintenance management system: the history
   of every job, and the open work orders with their priority. Never a
   schedule. Read two ways: as the work-order list when sizing or
   choosing a slice; as the archive when asking what was already
   decided. It wins on STATUS (what is done, what was ruled).
5. THE FIELD MANUAL: the protocol and the skills. How we work
   together. The protocol is read every session because it is
   resident; a skill when its trigger fires. Neither says what to
   build.
6. REFERENCE: generated documents that make no claim of their own and
   are read to learn the current state of the code or the data: the
   module atlas, PROVENANCE_AUDIT.md, DATA_INVENTORY, the worksheet
   check, the scanner's run history, the exports. Not communication
   (written to nobody); not logistics (no priority).
7. THE WORK: the code builds. Everything above exists to get them done
   well and keep them from drifting. The render is the ground truth
   for the work; the SHA for its state.

Under COMMUNICATION, the documents a build passes through go in one
order, the round trip: protocol -> ledger -> handoff -> manifest ->
code -> repo -> ledger.
- Handoff: a session record -- decisions, deliveries, open scope. A
  handoff is a CLAIM, not a verification; the render and the repo are the
  facts. Design-session handoffs (zero code) are first-class outputs: the
  reasoning trail for WHY the design is what it is.
- Manifest: the executable build contract, written against HEAD at build
  time (never on an un-pushed base); opens with the anchor (built on
  <SHA> at <URL>) per the requirement below. If handoff and manifest
  disagree, that is a flag to raise, not a thing to silently resolve.
- A design record carries rulings until they are moved out of it: to
  the ledger if they are decisions, to a skill if they are method (the
  protocol's Method Belongs to the Skill). The record is then history.

Under LOGISTICS, the ledger is also the change log for the protocol's
version history and the skills layer (v3.30). Under THE FIELD MANUAL,
the protocol is the constitution: it evolves slowly, and Tony ratifies
its amendments.

**Where a file's kind is written.** A documentation file's first line
carries a Doc-Kind comment, which `doc_index.py` reads. Its three values
in use at 9248845c (hand 95, zoned 48, generated 6) say HOW a file is
written, not which of the seven kinds it is, so the table maps one onto
the other:

| Doc-Kind | How it is written | Kinds of document carrying it |
|---|---|---|
| hand | by hand throughout | strategy (the plan), tactics (Where We Are), communication (briefs, handoffs, records) |
| zoned | by hand around a zone a tool writes | the field manual (the protocol and its archived copies), logistics (the ledger), the README |
| generated | wholly by a tool | reference (MODULE_ATLAS.md, MODULE_INDEX.md, PROVENANCE_AUDIT.md, DATA_INVENTORY.md, WORKSHEET_CHECK.md, EXACT_ROWS_PRINTED.md) |

No value is added: every kind in use has one, and a second tag per file
for its kind would be a second store. A file's kind of document is read
from its name (HANDOFF_, DESIGN_, MANIFEST_, SURVEY_, REVIEW_) and its
place. A skill opens with frontmatter and carries no Doc-Kind; the
work carries its Role: and Domain: tags.

**The master plan is not a rung in the round trip** (Tony's ruling,
2026-08-20, L-221). It is the STRATEGY (Tony's ruling of 2026-10-13,
L-442; until then this skill called it the ROADMAP): where the work goes
over months, not what is directly in front. It is ONE document at two
zooms (v1.12, Tony's ruling of 2026-09-28, L-333 and L-362): an
EXECUTIVE SUMMARY at the top, and the body, which keeps the shape of
the critical path as Section 5a. Its dated session history and its
lineage moved to `documentation/MASTER_PLAN_HISTORY.md` on 2026-10-14
(L-442), a dated record like the two retired companions. The summary is
REWRITTEN from the current state at every restamp, never carried
forward, so it cannot fall behind the body the way the two separate
companion files did: they restamped with v19 and v20 and then stood
still for a month while the plan reached v33. Those files,
`MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md` and
`MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`, carry a retirement line and are
dated records. The plan restamps once per DESIGN BUILD; stepwise
updating is the ledger's job. That is Tony's ruling of 2026-09-06
(L-296), replacing "at key junctures": a juncture is not countable, so
the rule could not be applied without a judgment call every time, and
the call kept landing on Tony. A design build is countable. Versions
are REPLACED, not archived -- only the PROTOCOL keeps a versioned copy
per version -- and git holds the superseded bytes either way, which is
why the plan's own rolling stamp keeps three entries and simply drops
the fourth instead of pushing it down into a history file. That cadence
is not staleness to be corrected by restamping more often.

Where any two documents disagree about what is done, the ledger wins:
that is STATUS. The order of the work is the road's on Where We Are:
that is SEQUENCING. L-221 gave sequencing to the plan on 2026-08-20;
Tony's ruling of 2026-10-13 moved it to the road (L-442), which had
been doing that job since 2026-10-10 (L-433). RICE ranks items in
isolation; bundling several items to complete a step on the road
SUPERSEDES RICE order. The ledger already calls RICE "prioritization
for planning" -- this names what the planning is and says it outranks
the score.

'''

SK_WWA_OLD = '''ordering and it is not another zoom of the master plan: the ledger still
wins on status and the plan on sequencing. It restates both in plain
words, for a reader who cannot hold the detail.'''
SK_WWA_NEW = '''ordering and it is not another zoom of the master plan: the ledger wins
on status and the road on this page on sequencing (moved from the plan
on 2026-10-13, L-442). It restates the status in plain words and carries
the order itself, for a reader who cannot hold the detail.'''

SK_RICE_OLD = '''  or Earth's list (L-413) IS the priority, under the master plan's
  sequencing authority (L-221), and a score beside it would only'''
SK_RICE_NEW = '''  or Earth's list (L-413) IS the priority, under the road's
  sequencing authority (L-221, moved to the road 2026-10-13, L-442),
  and a score beside it would only'''


def patch_skill(text, log):
    f = 'ledger skill'
    text = rep(text, SK_RICE_OLD, SK_RICE_NEW, 'RICE bullet: the road', log, f)
    text = rep(text, SK_WWA_OLD, SK_WWA_NEW, 'Where We Are: the road', log, f)
    a, b = span(text, SK_STACK_START, SK_STACK_END, 'Document Stack')
    text = text[:a] + SK_STACK_NEW + text[b:]
    log.append('ok  %-34s %s' % (f, 'Document Stack: seven kinds'))
    text = rep(text, SK_CONTENTS_OLD, SK_CONTENTS_NEW, 'Contents line', log, f)
    text = rep(text, SK_OLDER_OLD, SK_OLDER_NEW, 'older-entries line', log, f)
    a, b = span(text, SK_118_START, SK_118_END, '1.18 entry')
    b = b + len(SK_118_END)
    entry118 = text[a:b]
    text = text[:a] + text[b:]
    log.append('ok  %-34s %s' % (f, '1.18 entry moved out'))
    text = rep(text, SK_VER_OLD, SK_VER_NEW, 'version line 1.21', log, f)
    return text, entry118


SKH_ANCHOR = '\n## gallery-cache-builder\n'


def patch_skhist(text, entry118, log):
    f = 'SKILL_HISTORIES'
    new = ('\nThe skill\'s v1.18 entry, moved here word for word on 2026-10-14 when\n'
           'v1.21 made a fourth entry (L-442):\n' + entry118)
    once(text, SKH_ANCHOR, 'ledger skill section end')
    text = text.replace(SKH_ANCHOR, new + SKH_ANCHOR)
    log.append('ok  %-34s %s' % (f, 'ledger skill 1.18 entry received'))
    return text


# ---------------------------------------------------------------------------
# 3. The protocol
# ---------------------------------------------------------------------------

PR_HEAD_OLD = 'Tony Quintanilla, PE | Claude | v3.96 | October 14, 2026\n\nCut from 5cd63cce at'
PR_HEAD_NEW = 'Tony Quintanilla, PE | Claude | v3.97 | October 14, 2026\n\nCut from 9248845c at'

PR_ENTRY_ANCHOR = 'v3.96 (October 14, 2026): No rule changed in this document. THREE\n'
PR_ENTRY_NEW = '''v3.97 (October 14, 2026): No rule changed in this document. ONE
skill bump, one version (L-442): ledger-and-session-records 1.20 ->
1.21. THE PLAN IS STRATEGY; THE ROAD IS THE ORDER.

WHAT PROMPTED IT. Tony, 2026-10-13: "We should update the master plan
soon," then "the master plan for the interactive gallery is our
planning roadmap. Is it doing its job?" It worked as the record of the
architecture and had stopped working as the order of the work; the road
on Where We Are had taken that job on 2026-10-10 (L-433). His ruling the
same day named seven kinds of document: "master plan: strategic - where
we are: tactical - handoffs: orders and reports - ledger: logistics."

WHAT CHANGED. ledger-and-session-records rewrites The Document Stack as
the seven kinds -- strategy, tactics, communication, logistics, the
field manual, reference, the work -- each with when it is read, and
maps the Doc-Kind values in use onto them. Sequencing moves from the
master plan to the road on Where We Are; the ledger keeps status.
The plan restamps to v36 beside it: strategy only, its dated history
and its lineage moved to documentation/MASTER_PLAN_HISTORY.md (Tony's
ruling of 2026-10-14). The skill's v1.18 entry moved to
documentation/SKILL_HISTORIES.md, by the three-entry rule. This
document's one mention of the plan (The Braid: Section 5a carries the
braid's sequencing form) stays true: 5a keeps the braid.

THE OBLIGATION TRAVELS. A reinstall during a session is not visible to
that session. The next session confirms its loaded copy reads
ledger-and-session-records 1.21 before ledger work. This session
confirmed its loaded copies read horizons-orbital-mechanics 1.6,
gallery-cache-builder 1.9 and interactive-exhibit 1.15, discharging
v3.96's obligation.

The header stamp and the SHA anchor move with this entry.

Version history: v3.94 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

'''

PR_V394_START = 'v3.94 (October 13, 2026): No rule changed in this document. ONE\n'
PR_V394_END = '''Version history: v3.91 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

'''

PH_ANCHOR = '''(Moved down from the resident protocol on 2026-10-14 when
v3.96 made a fourth entry.)

================================================================
PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37'''


def patch_proto(text, log):
    f = 'PROJECT_INSTRUCTIONS'
    a, b = span(text, PR_V394_START, 'Functional for Claude, readable for human, signal preserved.',
                'v3.94 entry')
    entry = text[a:b]
    if not entry.endswith(PR_V394_END):
        raise PatchError('ANCHOR FAIL [v3.94 entry]: does not end as expected')
    text = text[:a] + text[b:]
    log.append('ok  %-34s %s' % (f, 'v3.94 moved out'))
    text = rep(text, PR_ENTRY_ANCHOR, PR_ENTRY_NEW + PR_ENTRY_ANCHOR, 'v3.97 entry', log, f)
    text = rep(text, PR_HEAD_OLD, PR_HEAD_NEW, 'header v3.97 and anchor', log, f)
    return text, entry


def patch_phist(text, entry394, log):
    f = 'PROJECT_INSTRUCTIONS_HISTORY'
    new_tail = ('(Moved down from the resident protocol on 2026-10-14 when\n'
                'v3.96 made a fourth entry.)\n\n' + entry394.rstrip('\n') + '\n\n'
                '(Moved down from the resident protocol on 2026-10-14 when\n'
                'v3.97 made a fourth entry.)\n\n'
                '================================================================\n'
                'PART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37')
    text = rep(text, PH_ANCHOR, new_tail, 'v3.94 received', log, f)
    return text


# ---------------------------------------------------------------------------
# 4. The ledger
# ---------------------------------------------------------------------------

LG_STAMP_ANCHOR = 'Review and RICE update Tony 6-21-2026\n'
LG_STAMP_NEW = '''Module updated: October 14, 2026 with Anthropic's Claude Opus 5.5
(L-442: the master plan is strategy and the road is the order, Tony's
seven kinds of document; plan v36, its history moved out;
ledger-and-session-records 1.21, protocol v3.97; L-433 closed, its loose
ends to L-443, opened; L-431's live-check line corrected), built on
9248845c.
'''

L443 = '''#### [L-443] The rest of the orrery's objects come to the website as plotted positions (gallery + orrery, objects)
<!-- L:443 status:OPEN upd:2026-10-14 section:A flag: rice: -->
- **Tony, 2026-10-13:** "I am anxious to add the symbols to the gallery
  too so visitors can at least plot positions." And his note of
  2026-10-10 on L-433: "then add the symbols for most if not all the
  orrery's objects list." Stage 11 on the road.
- **Opened 2026-10-14, at L-433's close** (L-442), so L-433's loose ends
  have an open home. The brief,
  `documentation/HANDOFF_L438_objects_to_website_brief_20261013.md`,
  names this work L-438; the ledger's index had retired L-438 and L-439
  before the item opened, and a retired handle is never reused. The
  brief is otherwise current.
- **Loose ends received from L-433** (its note of 2026-10-14, from L-431
  and L-395), word for word:
  - The served objects with no `'key'` in the orrery's list (moon, io,
    titan, pluto, charon, voyager_1) get no period on the website and
    no Horizons check; each gains both when it gets a key.
  - The Pluto-Charon barycentre's own period, around the Sun: the
    orrery never fetches elements for the barycentre itself, so the
    website prints "not yet fetched from JPL" for it.
  - From L-395: the fields the list lacks (a moon's parent, a clean
    kind); the display-name rename, which waits for names to stop
    being keys; MAPS and 3I/ATLAS checked live once served; and
    whether the identity check widens past the keyed entries (default
    no).
**Gap:** the design session, from the brief: measure, propose the
slices and the mechanism, and build the first slice only after Tony's
word.
**Ref:** `documentation/HANDOFF_L438_objects_to_website_brief_20261013.md`;
L-433; L-431; L-395; L-442; `export_objects.py`; `celestial_objects.py`;
gallery `data/objects_config.json`.

'''

LG_A_ANCHOR = '## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n'

L442 = '''#### [L-442] The master plan is strategy and the road is the order: Tony's seven kinds of document (documentation, DONE 2026-10-14)
<!-- L:442 status:DONE upd:2026-10-14 section:C flag: rice: -->
- **Tony's ruling, 2026-10-13**, in the coordination session of
  October 12 and 13, recorded in
  `documentation/HANDOFF_master_plan_restamp_brief_20261013.md`,
  section 1. His words: "master plan: strategic - where we are:
  tactical - handoffs: orders and reports - ledger: logistics." "by
  handoff I am conflating different documents, briefs, design
  manifests, closing reports and maybe others. But they are still all
  communication documents." "And of course there are code builds. Which
  is the work itself." "the ledger is like a maintenance management
  system, both history and work orders with priority, but by itself is
  not a schedule or a plan. Skills and the project instructions as you
  said is how we work together. You could say it's our field manual.
  There are other documents that are references like the module atlas
  and the provenance scanner report." And "Yes" to the seven-part
  statement.
- **The seven kinds:** strategy (the master plan); tactics (Where We
  Are and its road); communication (briefs, design records, manifests,
  handoffs and closing reports, review prompts and returns, Tony's run
  records); logistics (the ledger); the field manual (the protocol and
  the skills); reference (generated documents); the work (the code
  builds).
- **What moved, and where each now lives:**
  - Sequencing: from the plan's Section 5a to the road on
    `documentation/WHERE_WE_ARE.md`. Status stays with the ledger (a
    Note on L-221).
  - The critical path's dated record (the "You are here" table of
    2026-08-23 and the subsections 2026-08-25 to 2026-09-29): to
    `documentation/MASTER_PLAN_HISTORY.md` PART 1, word for word.
  - Section 10, Lineage: to the same file's PART 2, word for word.
    Tony, 2026-10-14, first "Keep history in the plan, so no.", then,
    asking for a recommendation and given one: "Changing ruling to: Yes
    move it." The brief's file name, MASTER_PLAN_CRITICAL_PATH_CHRONICLE.md,
    became MASTER_PLAN_HISTORY.md because the file holds both.
  - The rule: `skills/ledger-and-session-records/SKILL.md` 1.21, The
    Document Stack; protocol v3.97.
- **The plan's v36:** the executive summary rewritten (both SHAs read
  live; what the plan is and is not; the seven kinds; the five
  segments' state; the direction; signals read from files); Section 5a
  gains The direction, L-433's paragraph. Every line naming 5a as the
  order's home is changed: the summary's How to read the rest, the
  status block's Next line, 5a's opening and its L-154 paragraph, What
  this section deliberately does not carry, and Section 11's NEXT
  paragraph. The plan gains a Doc-Kind line (it had none).
- **Sections 6 and 7 against the ledger at 9248845c**, one pass (The
  Braid). Five disagreements, each corrected in one line and marked
  "at v36": Section 6 said L-154's status still read BLOCKED (DONE
  2026-08-24); Section 6 said MODULE_DOMAIN_MAP's retirement was
  deferred (L-437 retired it, 2026-10-13); Section 7 decision 12
  retired a JSON export that L-322 then built
  (`data/constants_export.json`, 2026-09-16); decision 13 said there is
  no generation step (the same); decision 18's open question, whether
  every measured field is range-capable, is answered as method by
  provenance-discipline, When the source gives a range. Checked and in
  agreement, or still open in the ledger: L-080, L-068 with L-066,
  L-016 and L-014, L-087, L-162, L-170 to L-173, L-176 to L-182, L-190.
- **Found and recorded, not chased:** Section 6's Attribution page
  ("[ ] Not started", required before any publicly reachable interactive
  page) has no ledger item. The plan's status block under the summary
  was last written at v35; it now says so and is not updated.
- **Doc-Kind:** the brief assumed the Doc-Kind comment is where a file's
  class is written. It is not: its three values in use (hand, zoned,
  generated) say how a file is written, read by `doc_index.py`. The
  skill maps them onto the seven kinds in a table and adds no value.
- **The obligation from v3.96 discharged:** this session's loaded copies
  read horizons-orbital-mechanics 1.6, gallery-cache-builder 1.9 and
  interactive-exhibit 1.15.
**Gap:** none. The next session confirms its loaded copy of
ledger-and-session-records reads 1.21 before ledger work.
**Ref:** `documentation/HANDOFF_master_plan_restamp_brief_20261013.md`;
`documentation/HANDOFF_L442_master_plan_restamp_20261014.md`;
`documentation/MASTER_PLAN_HISTORY.md`;
`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` v36;
`skills/ledger-and-session-records/SKILL.md` 1.21;
`PROJECT_INSTRUCTIONS.md` v3.97; L-221; L-433; L-443; L-296; L-437.

'''

LG_D_ANCHOR = '## D. RECONCILED LEDGER -- OPEN\n'

L433_HEAD_OLD = '''#### [L-433] The road after the Sun and Earth rooms, in Tony's words (planning)
<!-- L:433 status:OPEN upd:2026-10-14 section:A flag: rice: -->'''
L433_HEAD_NEW = '''#### [L-433] The road after the Sun and Earth rooms, in Tony's words (planning, DONE 2026-10-14)
<!-- L:433 status:DONE upd:2026-10-14 section:C flag: rice: -->'''

L433_NOTE_OLD = '''    as retired with L-439 (the dashboard labels took L-440). The objects
    work opens its block under the next free handle.
**Gap:** at the next design talk after the orbital periods: Tony
confirms the order, and the road and the master plan's critical path
(`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`, Section 5a) are
rewritten to it. Until then the road stands, with his lean noted.'''
L433_NOTE_NEW = '''    as retired with L-439 (the dashboard labels took L-440). The objects
    work opens its block under the next free handle.
  - Re-homed 2026-10-14, word for word, to L-443 (the objects to the
    website), opened at this item's close.
**CLOSED 2026-10-14** (L-442). Tony confirmed the order on 2026-10-12
(`documentation/DESIGN_rulings_20261012.md`, ruling 3): "Confirmed."
and "when I said sun and earth rooms I included the solar system
features." His lean went in: the inner planets' rooms (Mercury, Venus,
Mars) after the objects, Jupiter and Saturn after them, the Earth
System beside. The road on Where We Are has carried it since that
session; the master plan's v36 carries the direction in Section 5a.
**Gap:** none. The loose ends above went to L-443.'''


L221_ANCHOR = '''later session can actually read. Same structure as the SHA round trip.
'''
L221_NEW = L221_ANCHOR + '''**Note (2026-10-14):** sequencing authority moved from the plan to the
road on Where We Are (L-442, Tony's ruling of 2026-10-13); the status
half of this ruling stands.
'''

L431_OLD = '''  from JPL", and the barycentre's own period waits for the objects work
  (L-433's note). The live check's output is not in the record.'''
L431_NEW = '''  from JPL", and the barycentre's own period waits for the objects work
  (L-433's note). The website's live check is in the record too: "2 of
  2 gating checkers passed", the served files byte-identical and the
  export the orrery's at b9aee91a. (Corrected 2026-10-14, L-442; this
  line first read that its output was not in the record.)'''


def patch_ledger(text, log):
    f = 'LEDGER'
    # Bottom-up: section D anchor, L-431, L-221, L-433, section A, header.
    text = rep(text, LG_D_ANCHOR, L442 + LG_D_ANCHOR, 'L-442 added (closed)', log, f)
    text = rep(text, L431_OLD, L431_NEW, 'L-431 live-check line', log, f)
    text = rep(text, L221_ANCHOR, L221_NEW, 'L-221 Note', log, f)
    text = rep(text, L433_NOTE_OLD, L433_NOTE_NEW, 'L-433 closed, loose ends', log, f)
    text = rep(text, L433_HEAD_OLD, L433_HEAD_NEW, 'L-433 status DONE', log, f)
    text = rep(text, LG_A_ANCHOR, LG_A_ANCHOR + L443, 'L-443 opened', log, f)
    text = rep(text, LG_STAMP_ANCHOR, LG_STAMP_NEW + LG_STAMP_ANCHOR, 'header stamp', log, f)
    return text


# ---------------------------------------------------------------------------
# 5. Where We Are, by section, above the marker only
# ---------------------------------------------------------------------------

WW_HEAD_START = 'Last updated: '
WW_HEAD_END = '> **READ THIS FIRST**\n'
WW_HEAD_NEW = '''Last updated: October 14, 2026, night: the master plan restamped; its history moved out.
- Written at orrery 9248845 and gallery 86ef2df.

'''

WW_BOX_START = '> **Changed since you last read this:**\n'
WW_BOX_END = '*Italic* lines are the must-reads.'
WW_BOX_NEW = '''> **Changed since you last read this:**
> - The master plan is strategy only. The order lives on the road
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
>   Project; commit; push.*

'''

WW_6A_OLD = '''  6a.  [done]  *Orbital periods from JPL, in the orrery and on the
               website; accepted at your look, Oct 14.*
               << moved this session
'''
WW_6A_NEW = '''  6a.  [done]  Orbital periods from JPL, orrery and website (Oct 14).
'''

WW_11_OLD = ''' 11.   [later] The rest of the orrery's objects come to the website.
'''
WW_11_NEW = ''' 11.   [next]  *The rest of the orrery's objects come to the website:
               L-443 (the objects to the website), design first.*
               << moved this session
'''

WW_SETTLED_OLD = '''Standing rulings. A line leaves after a few weeks, once it is habit.
'''
WW_SETTLED_NEW = '''Standing rulings. A line leaves after a few weeks, once it is habit.
- The plan is strategy; the road here is the order; the ledger has
  status. The plan's history and lineage: MASTER_PLAN_HISTORY.md. (Oct 13, 14)
'''
WW_SETTLED_DROP = '''- OneDrive: no pause before a build; the retry is sufficient. Empty
  "solar-system (N)" folders are harmless; delete by hand. (Oct 8, 10)
'''

WW_SIGNALS_OLD = '## Signals  **>> UPDATED THIS SESSION**\n'
WW_SIGNALS_NEW = '## Signals\n'
WW_WAIT_OLD = '## Waiting on you  **>> UPDATED THIS SESSION**\n'
WW_WAIT_NEW = '## Waiting on you\n'

WW_DETAILS_START = '## Where the details are  **>> UPDATED THIS SESSION**\n'
WW_DETAILS_END = MARKER
WW_DETAILS_NEW = '''## Where the details are  **>> UPDATED THIS SESSION**

- Every item: `LEDGER_CONSOLIDATED.md`. Open for build: L-421 (the
  typed facts), its check.
- *Next: `HANDOFF_L438_objects_to_website_brief_20261013.md`; its item
  is now L-443 (the objects to the website)*
- This session: `HANDOFF_L442_master_plan_restamp_20261014.md`
- The distance digits: `DESIGN_L401_distance_digits_rulings_20261011.md`;
  reviews `REVIEW_L401_..._comparison_20261011.md`; build 1
  `HANDOFF_L401_distance_build1_20261012.md`
- Your notes of Oct 12: `WHERE_WE_ARE_10-12-26_2212_run_record.md`
- L-421 (typed facts, inner Oort): `MANIFEST_L421_typed_facts_20261006.md`, `HANDOFF_L421_*`
- L-436 (away from the machine): `DESIGN_L436_orrery_away_from_the_machine_20261013.md`
- Your six rulings of Oct 12: `DESIGN_rulings_20261012.md`; briefs for L-425,
  L-424 with L-426; the dashboard: `HANDOFF_L440_dashboard_labels_20261013.md`
- The strategy behind the road: `MASTER_PLAN_INTERACTIVE_GALLERY.md`

'''


def patch_wwa(text, log):
    f = 'WHERE_WE_ARE'
    once(text, MARKER, 'run-record marker')
    m = text.index(MARKER)
    top, bottom = text[:m], text[m:]
    # Where the details are: from its heading to the marker line.
    once(top, WW_DETAILS_START, 'details heading')
    a = top.index(WW_DETAILS_START)
    top = top[:a] + WW_DETAILS_NEW
    log.append('ok  %-34s %s' % (f, 'where the details are'))
    top = rep(top, WW_WAIT_OLD, WW_WAIT_NEW, 'waiting on you: mark cleared', log, f)
    top = rep(top, WW_SIGNALS_OLD, WW_SIGNALS_NEW, 'signals: mark cleared', log, f)
    top = rep(top, WW_SETTLED_DROP, '', 'settled: OneDrive line out', log, f)
    top = rep(top, WW_SETTLED_OLD, WW_SETTLED_NEW, 'settled: the plan line', log, f)
    top = rep(top, WW_11_OLD, WW_11_NEW, 'road: stage 11', log, f)
    top = rep(top, WW_6A_OLD, WW_6A_NEW, 'road: 6a marks reset', log, f)
    a, b = span(top, WW_BOX_START, WW_BOX_END, 'the box')
    top = top[:a] + WW_BOX_NEW + top[b:]
    log.append('ok  %-34s %s' % (f, 'the box'))
    a, b = span(top, WW_HEAD_START, WW_HEAD_END, 'header')
    top = top[:a] + WW_HEAD_NEW + top[b:]
    log.append('ok  %-34s %s' % (f, 'header date and SHAs'))
    above = top.count('\n')
    if above > 130:
        raise PatchError('WHERE_WE_ARE would stand %d lines above the marker (cap 130)' % above)
    log.append('ok  %-34s %s' % (f, '%d lines above the marker (cap 130)' % above))
    return top + bottom


# ---------------------------------------------------------------------------
# Post-checks: each one is a planted fault in the pre-test.
# ---------------------------------------------------------------------------

def postchecks(out, moved5a, moved10):
    errs = []
    plan = out[PLAN]
    # 1. no dated "### 2026-" subsection inside 5a
    a = plan.find('## Section 5a -- The Critical Path')
    b = plan.find('## Section 6 -- Prep Work')
    if a < 0 or b < 0:
        errs.append('plan: Section 5a or 6 heading not found')
    elif re.search(r'^### 2026-', plan[a:b], re.M):
        errs.append('plan: a dated "### 2026-" subsection is still inside Section 5a')
    # 2. no line saying the order lives in 5a
    for pat in (r'order lives in Section 5a', r'Section 5a is the critical path',
                r'Section 5a\'s newest subsection, 2026-09-29\.\*\*',
                r'plan carries a different authority, SEQUENCING',
                r'only home\.\*\*'):
        if re.search(pat, plan):
            errs.append('plan: a line still names 5a as the order\'s home (%s)' % pat)
    # 3. the skill's Document Stack has no sequencing sentence for the plan
    sk = out[SKILL]
    if 'The\nplan carries a different authority, SEQUENCING' in sk or \
       'plan carries a different authority, SEQUENCING' in sk.replace('\n', ' '):
        errs.append('skill: the Document Stack still gives the plan SEQUENCING')
    if 'wins on status and the plan on sequencing' in sk.replace('\n', ' '):
        errs.append('skill: Where We Are still gives the plan sequencing')
    if 'Skill version: 1.21' not in sk:
        errs.append('skill: version line is not 1.21')
    # 4. the history file holds the moved spans byte for byte, and the plan does not
    hist = out[HIST]
    for name, piece in (('5a record', moved5a), ('lineage', moved10)):
        if hist.count(piece) != 1:
            errs.append('history: the %s is not in the history file exactly once' % name)
        if piece in plan:
            errs.append('plan: the %s is still in the plan' % name)
    expect = len(HIST_HEAD.encode()) + len(moved5a.encode()) + len(HIST_PART2.encode()) + len(moved10.encode())
    if len(hist.encode()) != expect:
        errs.append('history: %d bytes, expected %d (header + moved spans)'
                    % (len(hist.encode()), expect))
    # ASCII and LF on everything written
    for rel, t in out.items():
        bad = sum(1 for ch in t if ord(ch) > 127)
        if bad:
            errs.append('%s: %d non-ASCII character(s)' % (rel, bad))
        if '\r' in t:
            errs.append('%s: carries a carriage return' % rel)
    return errs


def build(texts):
    """Pure function: input texts -> output texts, the moved spans, and the log."""
    log = []
    out = {}
    ledger = texts[LEDGER]
    if not re.search(r'<!-- L:431 status:DONE ', ledger):
        raise PatchError('REFUSED: L-431 (orbital periods) is not closed in the ledger. '
                         'This patch runs after build 3\'s close.')
    for h in ('L-442', 'L-443'):
        if re.search(r'^#### \[%s\]' % h, ledger, re.M):
            raise PatchError('REFUSED: %s already exists in the ledger' % h)
    plan, moved5a, moved10 = patch_plan(texts[PLAN], log)
    out[PLAN] = plan
    out[HIST] = HIST_HEAD + moved5a + HIST_PART2 + moved10
    log.append('ok  %-34s %s' % ('MASTER_PLAN_HISTORY', 'written (%d bytes)' % len(out[HIST].encode())))
    sk, entry118 = patch_skill(texts[SKILL], log)
    out[SKILL] = sk
    out[SKHIST] = patch_skhist(texts[SKHIST], entry118, log)
    pr, entry394 = patch_proto(texts[PROTO], log)
    out[PROTO] = pr
    out[PHIST] = patch_phist(texts[PHIST], entry394, log)
    out[LEDGER] = patch_ledger(ledger, log)
    out[WWA] = patch_wwa(texts[WWA], log)
    return out, moved5a, moved10, log


def main():
    try:
        if os.path.exists(os.path.join(ROOT, HIST)):
            raise PatchError('REFUSED: %s already exists. Nothing was written.' % HIST)
        texts, crlf = {}, {}
        for rel in (PLAN, SKILL, SKHIST, PROTO, PHIST, LEDGER, WWA):
            texts[rel], crlf[rel] = read(rel)
        out, moved5a, moved10, log = build(texts)
        errs = postchecks(out, moved5a, moved10)
        if errs:
            raise PatchError('POST-CHECK FAILED:\n  ' + '\n  '.join(errs))
    except PatchError as e:
        print('ERROR: %s' % e)
        print('NOTHING was written. Undo is not needed.')
        sys.exit(1)

    for line in log:
        print(line)
    written = []
    total = 0
    for rel, t in out.items():
        data = t.encode('utf-8')
        with open(os.path.join(ROOT, rel), 'wb') as fh:
            fh.write(data)
        total += len(data)
        written.append(rel)
        if crlf.get(rel):
            print('note: %s was CRLF in the working copy; written LF' % rel)
    print()
    print('post-checks: the plan has no dated subsection in 5a; no line names 5a')
    print('  as the order\'s home; the skill gives sequencing to the road; the')
    print('  history file holds both moved spans byte for byte; all ASCII, LF.')
    print('patch applied (%d edits in %d files, %d bytes)' % (len(log), len(written), total))
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py. Expect skills_index to print the')
    print('     manifest moving ledger-and-session-records 1.20 -> 1.21, and the')
    print('     ledger index to move L-433 and L-442 to the closed section.')
    print('  2. Reinstall ledger-and-session-records from skills/ in Settings > Skills.')
    print('  3. Save PROJECT_INSTRUCTIONS.md as documentation/project_instructions_v3_97.md,')
    print('     and copy it to the Project instructions.')
    print('  4. Move this script into documentation/; commit and push.')
    print('Undo is Discard Changes in GitHub Desktop.')


if __name__ == '__main__':
    main()
