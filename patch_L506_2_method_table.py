"""
patch_L506_2_method_table.py -- L-506 (token economy), second slice.

Built on orrery 7277aa4c891c62d1917dca03f57344c02a86765b at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with the
gallery at 674160a07de266320b3ee92ead50efde20f377c3 read only
(https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

HOW TO RUN: save this file in the orrery folder (above), open it in VS
Code, and click Run. Or, from that folder: python patch_L506_2_method_table.py

WHAT IT DOES (records only; no orrery behaviour changes):
  1. palomas_orrery_dashboard.py: "Method, Model, Effort" joins the
     documents list (LOCAL_DOCS) after "Running a Patch File"; it opens
     METHOD_MODEL_EFFORT.md, already at the orrery's root. Docstring
     entry added.
  2. PROJECT_INSTRUCTIONS.md -> v3.122: one sentence in Token Economy
     pointing at the table; the v3.122 entry; the header stamp and the
     SHA anchor; v3.119 moved down to the history file.
  3. documentation/PROJECT_INSTRUCTIONS_HISTORY.md: v3.119 appended to
     PART 1.
  4. documentation/project_instructions_v3_122.md: the versioned copy
     (new).
  5. LEDGER_CONSOLIDATED.md: L-506's second slice and its Tony-action;
     L-505's correction to x marks, Tony's phone verdict, and its Gap.
  6. documentation/WHERE_WE_ARE.md: the header, the box, stage 11c,
     Signals, Where the details are; nothing below the run-record marker.

Each file is checked before anything is written; if any check fails,
NOTHING is written. The ledger and Where We Are are checked only at the
lines this patch edits, so Tony's notes elsewhere never stop it. Undo is
Discard Changes in GitHub Desktop.

Written November 2, 2026 with Anthropic's Claude Opus 5.5.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def p(rel):
    return os.path.join(HERE, *rel.split('/'))


def read_lf(rel):
    raw = open(p(rel), 'rb').read()
    return raw.replace(b'\r\n', b'\n'), (b'\r\n' in raw)


def md5(b):
    return hashlib.md5(b).hexdigest()


def one(text, old, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit('ANCHOR FAIL: %s: expected 1 match, found %d.\n'
                         'NOTHING was written. If this patch already ran, '
                         'there is nothing to do; otherwise the file moved '
                         'since 7277aa4c: Pull origin and ask the session.'
                         % (label, n))
    return text.replace(old, new_of[label])


new_of = {}
results = {}
notes = []

# ---------------------------------------------------------------- 1. dashboard
F_DASH = 'palomas_orrery_dashboard.py'
EXPECT_DASH = '86012af5d29bc15b2d5362406a1d4773'
t, crlf = read_lf(F_DASH)
if md5(t) != EXPECT_DASH:
    raise SystemExit('ERROR: %s is not the file this patch was built on '
                     '(orrery 7277aa4c). NOTHING was written. If the patch '
                     'already ran, there is nothing to do.' % F_DASH)
if crlf:
    notes.append('note: %s was CRLF in the working copy; written LF' % F_DASH)
edits = [
    ('dash: docstring',
     b'after Constants Relations, with its short line.\n"""',
     b'after Constants Relations, with its short line.\n'
     b'November 2, 2026 with Anthropic\'s Claude Opus 5.5 (L-506): Method,\n'
     b'Model, Effort joins the documents list after Running a Patch File. It\n'
     b'opens METHOD_MODEL_EFFORT.md, the one-page table of which instrument,\n'
     b'model and effort each kind of task gets.\n'
     b'"""'),
    ('dash: LOCAL_DOCS',
     b'    ("Running a Patch File", "RUNNING_A_PATCH_FILE.md"),\n',
     b'    ("Running a Patch File", "RUNNING_A_PATCH_FILE.md"),\n'
     b'    ("Method, Model, Effort", "METHOD_MODEL_EFFORT.md"),\n'),
]
for label, old, new in edits:
    new_of[label] = new
    t = one(t, old, label)
results[F_DASH] = (t, len(edits))

# ---------------------------------------------------------------- 2. protocol
F_PI = 'PROJECT_INSTRUCTIONS.md'
EXPECT_PI = 'a239b947aaa463218a43c26ad4a968ce'
t, crlf = read_lf(F_PI)
if md5(t) != EXPECT_PI:
    raise SystemExit('ERROR: %s is not the file this patch was built on '
                     '(v3.121 at 7277aa4c). NOTHING was written. If the '
                     'patch already ran, there is nothing to do.' % F_PI)
if crlf:
    notes.append('note: %s was CRLF in the working copy; written LF' % F_PI)

# v3.119 block: from its first line up to the closing signature line.
a = t.index(b'v3.119 (October 31, 2026):')
b = t.index(b'Functional for Claude, readable for human, signal preserved.')
assert t.count(b'v3.119 (October 31, 2026):') == 1 and a < b
V3119 = t[a:b]
assert V3119.endswith(b'resident.\n\n'), 'v3.119 block does not end as expected'
t = t[:a] + t[b:]

ENTRY_3122 = (
    b'v3.122 (November 2, 2026): No rule changed in this document. ONE\n'
    b'sentence added to Token Economy [QUALITY], after its instances:\n'
    b'where the table of method, model and effort lives. No skill bump.\n'
    b'THE TABLE MADE FINDABLE FROM THE PROTOCOL AND THE DASHBOARD.\n'
    b'\n'
    b'WHAT PROMPTED IT. Tony, Nov 2, 10:01 Chicago, in the coordinating\n'
    b'session (Claude Fable 5.1): "What would help would be recommendations\n'
    b'regarding model and effort as well as method meaning snippet, patch or\n'
    b'Code for our various actions and tasks." That session wrote the table,\n'
    b'placed it as METHOD_MODEL_EFFORT.md at the orrery\'s root, and left its\n'
    b'wiring to a patch by an Opus session, by the table\'s own row for\n'
    b'records-only work (HANDOFF_coordination_20261102_morning.md, section\n'
    b'8).\n'
    b'\n'
    b'WHAT CHANGED. Token Economy gains one sentence naming the table and\n'
    b'where it opens. The dashboard\'s documents list gains the table\'s row\n'
    b'after Running a Patch File (palomas_orrery_dashboard.py, LOCAL_DOCS).\n'
    b'L-506 records the second slice. Built by the coordinating session of\n'
    b'Nov 2, afternoon (Claude Opus 5.5), on orrery 7277aa4c, as\n'
    b'patch_L506_2_method_table.py.\n'
    b'\n'
    b'THE OBLIGATION TRAVELS. The Project\'s instructions on claude.ai read\n'
    b'v3.121 until Tony pastes this version in. No skill changed; nothing to\n'
    b'reinstall.\n'
    b'\n'
    b'The header stamp and the SHA anchor move with this entry.\n'
    b'\n'
    b'Version history: v3.119 moves down to\n'
    b'documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n'
    b'resident.\n'
    b'\n')

edits = [
    ('pi: header stamp',
     b'Tony Quintanilla, PE | Claude | v3.121 | November 2, 2026\n',
     b'Tony Quintanilla, PE | Claude | v3.122 | November 2, 2026\n'),
    ('pi: SHA anchor',
     b'Cut from fd3551cc at https://github.com/tonylquintanilla/palomas_orrery\n',
     b'Cut from 7277aa4c at https://github.com/tonylquintanilla/palomas_orrery\n'),
    ('pi: Token Economy pointer',
     b'"yes".)\n\n[QUALITY] on this document\'s own promotion test:',
     b'"yes".)\n\n'
     b'The table of which instrument, model and effort each kind of task\n'
     b'gets is METHOD_MODEL_EFFORT.md at the repository root, opened from\n'
     b'the dashboard\'s documents list.\n\n'
     b'[QUALITY] on this document\'s own promotion test:'),
    ('pi: v3.122 entry',
     b'v3.121 (November 2, 2026): ONE rule added',
     ENTRY_3122 + b'v3.121 (November 2, 2026): ONE rule added'),
]
for label, old, new in edits:
    new_of[label] = new
    t = one(t, old, label)
results[F_PI] = (t, len(edits) + 1)
PI_FINAL = t

# ---------------------------------------------------------------- 3. history
F_H = 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md'
EXPECT_H = 'f6af1df655331d6036b101a5eb22e2fe'
t, crlf = read_lf(F_H)
if md5(t) != EXPECT_H:
    raise SystemExit('ERROR: %s is not the file this patch was built on '
                     '(7277aa4c). NOTHING was written. If the patch already '
                     'ran, there is nothing to do.' % F_H)
if crlf:
    notes.append('note: %s was CRLF in the working copy; written LF' % F_H)
label = 'history: v3.119 into PART 1'
old = (b'v3.121 made a fourth entry.)\n\n'
       b'================================================================\n'
       b'PART 2 -- LESSONS REMOVED')
new_of[label] = (b'v3.121 made a fourth entry.)\n\n' + V3119 +
                 b'(Moved down from the resident protocol on 2026-11-02 when\n'
                 b'v3.122 made a fourth entry.)\n\n'
                 b'================================================================\n'
                 b'PART 2 -- LESSONS REMOVED')
t = one(t, old, label)
results[F_H] = (t, 1)

# ---------------------------------------------------------------- 4. versioned copy
F_V = 'documentation/project_instructions_v3_122.md'
if os.path.exists(p(F_V)):
    have, _ = read_lf(F_V)
    if have == PI_FINAL:
        notes.append('note: %s already there, identical; left as is' % F_V)
    else:
        raise SystemExit('ERROR: %s already exists and differs from what this '
                         'patch writes. Likely a copy saved from elsewhere: '
                         'delete it and run again. NOTHING was written.' % F_V)
else:
    results[F_V] = (PI_FINAL, 'new')

# ---------------------------------------------------------------- 5. ledger
F_L = 'LEDGER_CONSOLIDATED.md'
t, crlf = read_lf(F_L)
if crlf:
    notes.append('note: %s was CRLF in the working copy; written LF' % F_L)
edits = [
    ('ledger: L-506 second slice',
     b"- **Tony-action (do):** after this patch is pushed, paste the repo's\n"
     b"  PROJECT_INSTRUCTIONS.md (v3.121) into the Orrery Project's\n"
     b"  instructions on claude.ai; no skill changed, nothing to reinstall.\n",
     b"- **Second slice, 2026-11-02 afternoon,** by the coordinating session\n"
     b"  (Claude Opus 5.5, orrery 7277aa4c and gallery 674160a0 read live),\n"
     b"  from the morning handoff's section 8: `METHOD_MODEL_EFFORT.md`, the\n"
     b"  table of method, model and effort placed at the orrery's root that\n"
     b"  morning, gets its row in the dashboard's documents list\n"
     b"  (`palomas_orrery_dashboard.py`, `LOCAL_DOCS`, after Running a Patch\n"
     b"  File), and Token Economy one sentence pointing at it (protocol\n"
     b"  v3.122; v3.119 moved to the history file; the versioned copy).\n"
     b"  Delivered as `patch_L506_2_method_table.py`. That session printed no\n"
     b"  token count (a chat session); it read the two skills its patch\n"
     b"  fired in full and the target files at their edit sites only.\n"
     b"- **Tony-action (do):** paste the repo's PROJECT_INSTRUCTIONS.md into\n"
     b"  the Orrery Project's instructions on claude.ai after each protocol\n"
     b"  push. v3.121 pasted Nov 2 (\"done\", in\n"
     b"  `WHERE_WE_ARE_11-1-26_2249_run_record.md`); v3.122 after\n"
     b"  `patch_L506_2_method_table.py` is pushed. No skill changed, nothing\n"
     b"  to reinstall.\n"),
    ('ledger: L-505 stamp',
     b'<!-- L:505 status:OPEN upd:2026-11-01 ',
     b'<!-- L:505 status:OPEN upd:2026-11-02 '),
    ('ledger: L-505 x marks and Gap',
     b"**Gap:** Tony's push, then his phone in all three rooms (the dots at\n"
     b"two sizes, the ruler with two labels and no pill, no numbers on the box\n"
     b"edges, the AU note from the ruler, the frame note's new sentence, the\n"
     b"low camera angle), then the Mode 5 pass with the knobs; his settled\n"
     b"values written in as the defaults. Closes on his Mode 5, not on the\n"
     b"push. Then interactive-exhibit's bump (above), in an orrery session.\n",
     b"- **Corrected to x marks, 2026-11-02.** Tony's ruling of 2026-10-31,\n"
     b"  20:43: \"let's go with X then. X is simply a graphical marker with no\n"
     b"  render significance like a + while a filled square might be used for\n"
     b"  a render at some point.\" It never reached the committed design\n"
     b"  record, so the build above drew dots. The coordinating session of\n"
     b"  Nov 2, morning (Claude Fable 5.1), restored it in\n"
     b"  `documentation/DESIGN_axis_ticks_and_ruler_rulings_20261031.md`\n"
     b"  (its section 6 says what happened) and delivered the gallery's\n"
     b"  `patch_L505_x_marks.py`: the three tick traces to Plotly's symbol\n"
     b"  \"x\", the ruler's key to two x marks (`sunRulerX`), the frame note's\n"
     b"  sentence, and the walk's section 25. Tony ran it, the maintenance run\n"
     b"  36 of 36, and pushed (gallery 968fefb4, 8c6b1b37, 674160a0). His\n"
     b"  phone, Nov 2: the x marks in all three rooms, and `?tick=4,8` and\n"
     b"  `?tick=5,10`, \"looks good\" (`WHERE_WE_ARE_11-1-26_2249_run_record.md`).\n"
     b"  Wherever this item says dots above, read x marks, the\n"
     b"  interactive-exhibit bullet included. orrery-coding-conventions'\n"
     b"  marker table gains an x row (coordinate ticks: the axes' scale marks\n"
     b"  and the ruler; the cross row then info markers alone) at its next\n"
     b"  version, an orrery session's.\n"
     b"**Gap:** Tony's word on the tick sizes (3 and 6 as built; 4 and 8, and\n"
     b"5 and 10, both tried), then `?ruler=` and `?halo=`; his settled values\n"
     b"written in as the defaults by a gallery patch. Closes on his Mode 5.\n"
     b"Then interactive-exhibit's bump and orrery-coding-conventions' x row\n"
     b"(above), in an orrery session.\n"),
]
for label, old, new in edits:
    new_of[label] = new
    t = one(t, old, label)
results[F_L] = (t, len(edits))

# ---------------------------------------------------------------- 6. Where We Are
F_W = 'documentation/WHERE_WE_ARE.md'
t, crlf = read_lf(F_W)
if crlf:
    notes.append('note: %s was CRLF in the working copy; written LF' % F_W)
MARK = b'--- Your run record below this line.'
assert t.count(MARK) == 1, 'run-record marker not found once'
head, tail = t.split(MARK)
edits = [
    ('wwa: header',
     b'Last updated: November 2, 2026, morning: the coordinating session (the ticks\' ruling restored; the x patch; token economy).\n'
     b'- Written at orrery fd3551cc and gallery b7ddf77a, plus uncommitted edits.\n',
     b'Last updated: November 2, 2026, afternoon: the coordinating session (the x marks live; the method table wired; v3.122).\n'
     b'- Written at orrery 7277aa4c and gallery 674160a0, plus uncommitted edits.\n'),
    ('wwa: box',
     b'> - The ticks are x marks, by your ruling of Oct 31, 20:43. The build\n'
     b'>   drew dots because that ruling never reached the committed design\n'
     b'>   record (the file placed in your folder was an earlier copy). The\n'
     b'>   record is restored; a patch corrects the build.\n'
     b'> - Nov 2: neither night fired by 14:34 UTC; you ran both by hand.\n'
     b'> - Token economy is in the protocol (v3.121): paste it into the Project.\n'
     b'>\n'
     b'> **Do next:** *run `patch_L505_x_marks.py` from the website folder,\n'
     b'> then the maintenance run, push, and your phone on the x marks and\n'
     b'> their sizes (`?tick=4,8`, `?tick=5,10`).*\n',
     b'> - The x marks are live in all three rooms (website 674160a0), and\n'
     b'>   your phone says they look good, at 4 and 8 and at 5 and 10.\n'
     b'> - The method table opens from the dashboard, and the protocol\n'
     b'>   points to it (v3.122): paste it into the Project.\n'
     b'> - The website\'s two times had not run by 18:00 UTC on Nov 2. The\n'
     b'>   orrery wrote a run record at 17:06 (0099170), after your hand\n'
     b'>   run: the Actions tab says whether GitHub started it.\n'
     b'>\n'
     b'> **Do next:** *run `patch_L506_2_method_table.py` from the orrery\n'
     b'> folder, then `ledger_index.py`, push, and paste the protocol into\n'
     b'> the Project; then your word on the tick size.*\n'),
    ('wwa: road 11c',
     b' 11c.  [NOW]   *The ruler build (L-505 (the ticks and the ruler)): built\n'
     b'               Nov 1 with dots; the x patch next (your ruling of Oct 31,\n'
     b'               20:43); then sizes on your phone.* << changed this session\n',
     b' 11c.  [NOW]   *The ruler build (L-505 (the ticks and the ruler)): x marks\n'
     b'               live Nov 2, good on your phone; your word on the sizes\n'
     b'               next, then a patch writes them in.* << changed this session\n'),
    ('wwa: Settled mark cleared',
     b'## Settled  **>> UPDATED THIS SESSION**\n',
     b'## Settled\n'),
    ('wwa: Signals',
     b'- Last cache build: 20261102T150545Z, ok, no retry (the website\'s swap\n'
     b'  log\'s last line: your hand run of Nov 2, on GitHub).\n'
     b'- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md\n'
     b'  of the orrery session\'s maintenance run, Nov 1; no orrery code since).\n'
     b'- This page\'s date Nov 2; the ledger\'s newest stamp Nov 1: this update\n'
     b'  edits no ledger item (L-505\'s line comes with the next records patch).\n',
     b'- Last cache build: 20261102T150545Z, ok, no retry (the website\'s swap\n'
     b'  log\'s last line at 674160a0: your hand run of Nov 2, on GitHub).\n'
     b'- Tier-1 on the gate path: 0, the push gate holds (PROVENANCE_AUDIT.md\n'
     b'  of Nov 1; since then one file name in the dashboard, no number).\n'
     b'- This page\'s date and the ledger\'s newest stamp: both Nov 2. Agree.\n'),
    ('wwa: details',
     b'- Today: `HANDOFF_coordination_20261102_morning.md` (the lost ruling,\n'
     b'  the lesson, the nights); the design record\'s section 6; L-505; L-506.\n',
     b'- Today: `HANDOFF_coordination_20261102_morning.md` (the lost ruling,\n'
     b'  the nights, the queue); L-505; L-506; `METHOD_MODEL_EFFORT.md`.\n'),
]
for label, old, new in edits:
    new_of[label] = new
    head = one(head, old, label)
n_above = head.count(b'\n')
if n_above > 130:
    raise SystemExit('ERROR: Where We Are would stand %d lines above the '
                     'marker (cap 130). NOTHING was written.' % n_above)
results[F_W] = (head + MARK + tail, len(edits))

# ---------------------------------------------------------------- encoding gate
for rel, (data, _) in results.items():
    bad = sum(1 for ch in data if ch > 127)
    if bad:
        raise SystemExit('ERROR: %s would hold %d non-ASCII byte(s). NOTHING '
                         'was written.' % (rel, bad))

# ---------------------------------------------------------------- write
for rel, (data, n) in results.items():
    with open(p(rel), 'wb') as f:
        f.write(data)
    if n == 'new':
        print('ok %s (new; the versioned copy, %d bytes)' % (rel.replace('/', os.sep), len(data)))
    else:
        print('ok %s (%d edits)' % (rel.replace('/', os.sep), n))
for line in notes:
    print(line)
print('Where We Are: %d lines above the marker (cap 130); nothing below it touched.' % n_above)
print('Stamps moved: the protocol header (v3.122) and its SHA anchor (7277aa4c);')
print('  the dashboard docstring; L-505 upd:2026-11-02; Where We Are\'s header.')
print('patch applied')
print('''
Next, in this order:
  1. Run ledger_index.py (VS Code, Run) from this folder: it rebuilds the
     ledger's index with L-505 and L-506 as edited.
  2. Open the dashboard once and click Method, Model, Effort under the
     documents: the table should open.
  3. GitHub Desktop: commit and push the orrery, everything in the change
     list together (this patch's six files and the index); move this
     script into documentation\\ for the next commit.
  4. Paste the repo's PROJECT_INSTRUCTIONS.md (v3.122) into the Orrery
     Project's instructions on claude.ai.
  5. Your word on the tick size: 3 and 6 as built, 4 and 8, or 5 and 10.
''')
