"""build_L559_protocol_v4_1.py -- the edits that made the protocol's v4.1
(L-559) from v4.0, one named edit at a time.

WHAT THIS IS
    A session's tool and a record, not one of Tony's Run-button scripts:
    it needs two file names and writes only the second. It was run on
    PROJECT_INSTRUCTIONS.md at orrery de65fb87 (v4.0) and its output was
    placed as v4.1. Each edit must match its input exactly once, or it
    stops and names the edit; it prints each edit's lines before and
    after and the sum, so the build carries its own arithmetic. Run on
    v4.1 itself it stops at the first edit: the work is done.
    It supersedes documentation/build_L559_protocol_v4_1_draft.py, which
    built the draft Tony ruled on.

HOW IT WAS RUN, from the orrery's root folder
    python documentation/build_L559_protocol_v4_1.py \\
        documentation/project_instructions_v4_0.md <file to write>

Tony's rulings on the nine items, and the cold read's fixes, are on
L-559 in LEDGER_CONSOLIDATED.md; the review is
documentation/REVIEW_L559_protocol_review_20261125.md.

Written November 25, 2026 with Anthropic's Claude Fable 5.2 (L-559).
"""
import sys, hashlib
SRC, OUT = sys.argv[1], sys.argv[2]
text = open(SRC, encoding='utf-8', newline='').read()
assert '\r' not in text, 'source is not LF'
base_lines = text.count('\n')
edits = []

def E(name, old, new):
    edits.append((name, old, new))

# ---- 0. first line (draft marker) ----------------------------------
E('0 first line',
"<!-- Doc-Kind: zoned | The protocol. How a session is run, which checks are load-bearing, and why. Carries the generated list of skill names. -->\n",
"<!-- Doc-Kind: zoned | The protocol: the project's instructions. What the project is, how a session is run, which checks are load-bearing, and why. Carries the generated list of skill names. -->\n")

# ---- 1. header + THE PROJECT ---------------------------------------
E('1 header, and THE PROJECT (new)',
"""Tony Quintanilla, PE | Claude | v4.0 | November 23, 2026

Cut from 7087b3ad at https://github.com/tonylquintanilla/palomas_orrery
(branch main). Gallery repo: tonyquintanilla/tonyquintanilla.github.io.
Every earlier version and the stories behind the rules:
documentation/PROJECT_INSTRUCTIONS_HISTORY.md. The philosophy as it
stood until this version: PROJECT_ORIGIN.md.

The anchor names the state this document was CUT FROM, not a promise
that the repo still sits there. It is here because this file's own
CRITICAL gate requires it of any document leaving a live session, and
a relay partner reading this has no other way to know what it
describes.

PREAMBLE: WHY THIS PROTOCOL EXISTS
""",
"""Tony Quintanilla, PE | Claude | v4.1 | November 25, 2026

The project's instructions: what Paloma's Orrery is, how a session works
in it, and which checks are never skipped. Written for Claude, starting cold.
Cut from de65fb87 at https://github.com/tonylquintanilla/palomas_orrery
(branch main), the website repository tonyquintanilla.github.io at 972b4a93:
the state this was cut from, not a promise either still sits there. Earlier
versions and the rules' stories: documentation/PROJECT_INSTRUCTIONS_HISTORY.md.
The philosophy as it stood until v4.0: PROJECT_ORIGIN.md.

THE PROJECT
What it is for, its parts and how they connect: the archived master plan's job.

WHAT IT IS FOR. Paloma's Orrery explores three subjects, in Tony's words
"the Earth System, the orrery and the stars": Earth's climate, the solar
system, and the Sun's stellar neighbourhood. It is named for his daughter,
and "this website is a legacy gift for Paloma": it must stay running, and
stay right, without him. "Data Preservation is Climate Action." WHERE IT IS
GOING (the goal that ends the road on Where We Are): the website will do
what the desktop orrery does, with a date to choose, within its data's range.

THREE PARTS, connected in one direction, by files.
1. THE ORRERY defines. Python in the orrery repository, run on Tony's
   computer, asking its sources live and drawing on his screen. Three
   components, each a window palomas_orrery_dashboard.py opens: the Solar
   System orrery (palomas_orrery.py), the Stars (star_visualization_gui.py)
   and the Earth System (earth_system_visualization_gui.py, the generators).
   Every definition lives here: the bodies and how JPL is asked for each
   (celestial_objects.py), the constants (constants_new.py), each
   spacecraft's path plan, the stored drawings, the words. Its checks hold
   them to their sources; its night (orrery_maintenance_run.py --night, on
   GitHub's computers) writes the exports. This repository also holds the
   project's documents: this protocol, skills/, the ledger, documentation/.
2. THE WEBSITE'S NIGHT fetches and serves. Python in the website repository,
   which GitHub Pages serves as palomasorrery.com; it runs on GitHub's
   computers (daily_run.py --night). It pulls the orrery's exports and
   mirrors their facts into data/objects_config.json; then
   tools/gallery_cache_builder.py asks JPL itself: an orbit for each body
   that has one, the positions themselves for each on a path. It measures
   how far each orbit can be trusted, holds a body it cannot stand behind,
   and writes the files the page reads (data/solar-system/).
3. THE PAGE works out and draws, in a visitor's browser. It asks JPL
   nothing. In a room, a live view (interactive.html), Python in the browser
   (gallery/assembler/, under Pyodide) works out where a body on an orbit is
   at the minute shown and draws a path from its served points; JavaScript
   (gallery/*.js) draws the tree, the boxes and the shells. An encounter is
   a package a tool fetched from JPL once, played with no Python.

NOT EVERY SUBJECT IS LIVE. Only the Solar System has rooms. An Earth System
layer's generator, run by Tony, writes its page, pictures and Google Earth
file (earth/); for El Nino the orrery's night checks NOAA and flags, and
never changes a page. The Stars, and older views of all three, are pictures
saved from the orrery and curated by hand (index.html; gallery-pipeline).

ONE BODY OF KNOWLEDGE, TWO MACHINERIES. The orrery asks JPL live for each
place it draws. The page cannot ask, so it works each place out from what
the night served, alone. Orbital mechanics, JPL's conventions and the
visual language carry across as knowledge; code does not. Two failures come
of forgetting it: porting orrery code to the page and expecting orrery
behaviour, and "fixing" the page by subtracting one large JPL answer from
another (retired for catastrophic cancellation: gallery-assembler). A body
is defined in the orrery first and reaches the website by the export, never
typed there. Tony's pushes carry code and words; the two nights carry data.

THE WORDS. "Gallery" was the old word for the website, and "assembler" for
the Python on the page. Both stay in the names of files, folders and skills
(gallery/, gallery_cache_builder.py, gallery-assembler), which do not
change. Prose says the website, the night, the page, and a room.

PREAMBLE: WHY THIS PROTOCOL EXISTS
""")

# ---- 2. Preamble: origin parenthetical ------------------------------
E('2 Preamble, the 2024 origin note shortened',
"""not building on a stale base, not trusting a handoff over the render.
(Origin: not asserted philosophy -- Mode 1 and targeted-for-existing-code
trace to full-file replacement corrupting the single-file GPT-4 orrery in
2024; see PROJECT_ORIGIN.md at the repo root.) Each shortcut looks harmless
in isolation; together they are how the project drifts.
""",
"""not building on a stale base, not trusting a handoff over the render.
Each shortcut looks harmless in isolation; together they are how the
project drifts. (The first lesson, 2024: a whole file regenerated, and
the single-file orrery corrupted. PROJECT_ORIGIN.md.)
""")

# ---- 3. Preamble: the two layers ------------------------------------
E('3 Preamble, the two layers said without v3.30',
"""As of v3.30 the protocol is the CONSTITUTION of a two-layer system: this
document stays resident every session and carries the judgment, the modes,
and the checkpoint gates that must fire unprompted; task-specific procedures
and conventions live in on-demand SKILLS (see the Skill Manifest, Part 3),
authored in the repo under skills/ and installed to Tony's account. The
skills are versioned and SHA-pinned like everything else; the ledger is
their change log.

Everything that follows -- the modes, the criticality tiers, the technical
checks, the philosophy -- is downstream of this. Apply the rules in its light.
""",
"""The protocol is the resident layer of two, the CONSTITUTION: read every
session, it carries the project, the judgment and the gates that must fire
unprompted. Task procedures and conventions live in SKILLS (Part 3), loaded
when their work comes up. Everything that follows is downstream of this
preamble. Apply the rules in its light.
""")

# ---- 4. Session Start ------------------------------------------------
E('4 Session Start, where the order lives; the skills gate named',
"""Read Where We Are - documentation/WHERE_WE_ARE.md. Its "Do next" line
  names the job, and a brief or handoff it names carries the details.
""",
"""Read Where We Are - documentation/WHERE_WE_ARE.md. Its "Do next" line
  names the job, and a brief or handoff it names carries the details.
  Its road is the ONE place the order of the work lives (not the ledger).
""")
E('4b Session Start, the skills comparison named beside the base',
"""Record the base - both repositories; see the SHA Round Trip, Part 3.
""",
"""Record the base, compare the skills - the first two gates of Part 3.
""")


# ---- 5. Two modes: Visual Verification folded in --------------------
E('5 Mode 5 takes Visual Verification\'s sentences',
"""Mode 5 - Visual. Claude implements; Tony judges. His eyes on the
  render, on his own screen or phone, are the gate.
""",
"""Mode 5 - Visual. Claude implements; Tony judges. "Runs without errors"
  is not "correct": the render is the ground truth, and his eyes on it, on
  his own screen or phone, are the gate. Looks wrong? Check reference frames.
  When Claude explains away what his eyes see, that is the moment to be
  most skeptical. (Specifics: orrery-coding-conventions.)
""")
E('5c The default, said without the old mode numbers',
"""The default is agentic, the old Mode 2: the session does the job whole
and verifies it. That is who does the work. HOW existing code is
changed is still Targeted for Existing Code: an edit in place, never a
regenerated file. A snippet for Tony to place by hand, the old Mode 1,
is made only when he asks. (The seven-mode table moved to the history
file 2026-11-23.)
""",
"""The default is agentic: the session does the job whole and verifies it.
HOW existing code is changed is still Targeted for Existing Code: an edit
in place, never a regenerated file. A snippet for Tony to place by hand
is made only when he asks.
""")
E('5b Visual Verification, the section, leaves (its sentences are in Mode 5)',
"""Visual Verification [QUALITY]
"Runs without errors" != correct. The render is the ground truth and
Tony's eyes are the gate. Looks wrong? Check reference frames. When Claude
explains away what Tony's eyes see, that is the moment to be most
skeptical. (Verification specifics: orrery-coding-conventions.)

""", "")

# ---- 6. Kinds of Session: one writer ---------------------------------
E('6 Kinds of Session, one writer in a folder (NEW RULE, proposed)',
"""folders; that is routine too, and each is read back (Know Which Copy
You Are Reading, Part 3).
""",
"""folders; that is routine too, and each is read back (Know Which Copy
You Are Reading, Part 3). One writer in a folder at a time, a rule Tony
keeps too when he works across sessions: before a session places a file
another session edits, it asks him whether one is running.
""")

# ---- 7. Core Principles + Anti-Patterns ------------------------------
E('7 Core Principles gain the three lines with no other home',
"""The Conversation is the Point - Understanding emerges through dialogue. Can't be shortcut.
""",
"""The Conversation is the Point - Understanding emerges through dialogue. Can't be shortcut.
Fix Only What Was Asked - Changing unrelated code is scope creep.
One Renderer - Duplicate rendering is double maintenance. Extract to the source module.
Derive From Known Quantities - Don't estimate manually.
Multi-File Changes - Map touchpoints and order first (dep_trace.py): data -> processing -> UI -> docs.
""")
E('7c Multi-File Changes, the section, leaves (its line is a principle above)',
"""Workflow Patterns

Multi-File Changes
Map touchpoints and order (dep_trace.py): data -> processing -> UI -> docs.

Graceful Fallback
""",
"""Workflow Patterns

Graceful Fallback
""")
E('7b Anti-Patterns table leaves (each row is a principle above, or a skill\'s)',
"""Anti-Patterns
Don't                       Why                         Do Instead
Assume                      Guess wrong, redo            Ask
Rewrite working code        Breaks things                Targeted changes
Change unrelated code       Scope creep                  Fix only what asked
Build first architecture    Complexity locks in          Iterate design in conversation first
Guard strips with if list:  Stale data survives          Strip unconditionally before the guard
Duplicate rendering         Double maintenance           Extract to source module

""", "")

# ---- 8. Graceful Fallback --------------------------------------------
E('8 Graceful Fallback, the website\'s rule beside the orrery\'s',
"""Graceful Fallback
API fails -> Check fallback list -> Calculate locally -> Attribute source.
Explicit lists, not automatic. Document assumptions.
""",
"""Graceful Fallback
A source that cannot answer never gets a silent substitute. In the orrery:
API fails -> Check fallback list -> Calculate locally -> Attribute source.
Explicit lists, not automatic. Document assumptions. The website's night
holds the body at its last good build and says so (gallery-cache-builder).
""")

# ---- 9. SHA Round Trip label -----------------------------------------
E('9 SHA Round Trip, "Gallery:" becomes "Website:"',
"""Gallery: https://github.com/tonylquintanilla/tonyquintanilla.github.io.
""",
"""Website: https://github.com/tonylquintanilla/tonyquintanilla.github.io.
""")

# ---- 10. Know Which Copy: the read-back ------------------------------
E('10 Know Which Copy, the read-back (RULE CHANGED, proposed)',
"""- A linked session's write to Tony's folder is not counted until it is
  read back from the folder and compared, by its size at least. Each
  write is sent as a fresh copy, never a re-send of an earlier one. A
  write that cannot be read back is reported as unconfirmed.
  (2026-11-10, L-522: a re-sent file delivered the first write's
  bytes; the read-back caught it by the file's size.)
""",
"""- A linked session's write to Tony's folder is not counted until it is
  read back from the folder and compared: byte for byte where it can be,
  by its size at least. Each write goes from a path not used before. A
  read-back refused as "hardlinked" is tried again after a minute; one
  that cannot be read is reported unconfirmed. (L-522: a re-sent file
  delivered its first bytes, 2026-11-10; again 2026-11-25, same size.)
""")

# ---- 11. A Report Names Its Items: tense -----------------------------
E('11 A Report Names Its Items, the stale example put in the past',
"""  "two limits" name what they count; "5 parallel pipelines" does not.
""",
"""  "two limits" name what they count; "5 parallel pipelines" did not.
""")

# ---- 12. Check All Parallel Pipelines --------------------------------
E('12 Check All Parallel Pipelines, the website named and the parts pointed to',
"""Position data reaches a viewer through SIX parallel consumers, three of
them in the gallery repository, and a fix in one does not reach the
others. Before patching anything in the data flow -- a change as small
as hover text counts -- load orrery-coding-conventions and map ALL of
them from its list. (L-269; the sixth, the website's own chain, L-522.)
""",
"""Position data reaches a viewer through SIX parallel consumers, three of
them in the website repository, and a fix in one does not reach the
others (The Project, Two Machineries). Before patching anything in the
data flow -- a change as small as hover text counts -- load
orrery-coding-conventions and map ALL of them. (L-269; the sixth, L-522.)
""")

# ---- 13. Measure, Then Say -------------------------------------------
E('13 Measure, Then Say (NEW RULE, proposed)',
"""that would catch it. (Working procedures, scanner mechanics, and the
active-build-path Tier-1 push gate: provenance-discipline skill.)
""",
"""that would catch it. (Working procedures, scanner mechanics, and the
active-build-path Tier-1 push gate: provenance-discipline skill.)

Measure, Then Say [QUALITY]
The same convention, turned on the session's own words. A number or a
behaviour told to Tony is measured or read in this session first: the file
counted, the code path read, the page opened. An estimate is named as one,
and is never offered for a ruling. (Six handoffs of Nov 23 to 25 each
record one said first and found wrong. L-559.)
""")

# ---- 14. The Orrery and the Assembler leaves --------------------------
E('14 The Orrery and the Assembler leaves (The Project replaces it)',
"""The Orrery and the Assembler
Two instruments, one body of understanding underneath them. The orrery solves
"ask Horizons the right question, live" -- there is no local math to get wrong,
because there is no local math. The assembler solves a problem the orrery never
faces: no live connection, so it must cache a recipe once and reconstruct it
correctly, later, alone. Nearly everything distinguishing the two -- caching,
client-side propagation, trust measurement itself -- exists because of that one
difference. What transfers is knowledge (orbital mechanics, Horizons convention,
the visual language); what doesn't is the machinery. Forgetting this both ways
is a failure mode: porting orrery code into the assembler expecting orrery
behavior, or "fixing" the assembler by translating between frames it was
deliberately built never to translate between (subtraction was tried and
retired for cause -- catastrophic cancellation, real numbers, not a style
preference). The assembler exists because the orrery's Python requirement is
a wall between the work and everyone who isn't Tony.

""", "")

# ---- 15. Lessons Archive leaves ---------------------------------------
E('15 Lessons Archive leaves (each lesson is in a skill or a principle)',
"""Lessons Archive
Technical lessons live as field notes in their skills. These process
lessons exist nowhere else. (The philosophical lessons and the
quotations moved to PROJECT_ORIGIN.md on 2026-11-23.)

Process:
- Bugs become lessons when documented. Stories make science memorable
- Pure design sessions (zero code) are first-class outputs
- Derive from known quantities, don't estimate manually
- Module Atlas as prompt artifact: complete and current reference for codebase-aware sessions
- Fixing an invisible thing surfaces its neighbors. Budget for "now I can see it's too close to its neighbors" as the follow-on to any "nothing renders" fix
- Central factories need explicit migration intent: migrate-in-scope, defer-with-tracked-backlog, or declare new-code-only. The danger zone is the unstated fourth option (factory exists, no plan) -- it gets quoted as a standard while call sites bypass it
- Testing iterates in dependency order: regression gate, then features, then animation. Some bugs are only findable in later rounds (the Sun-checkbox-off bug needed Round 3). A three-round fix is fine when each round teaches something new
- When deferring a pipeline patch, smoke-test the deferred pipeline to confirm it is in a KNOWN state, not just that it does not error
- Handoff item numbers get rebased across versions (Paloma's shell track rebased twice: c4 1-22 -> D1 1-41 -> D2 42-54). A number means different things in different handoffs; items leak at the rebase. One authoritative running ledger beats per-handoff renumbering
- Skills are stores too: author them in the repo, version them, SHA-stamp them, and let the ledger log their changes -- an unversioned knowledge layer is the drift class this protocol exists to kill

""", "")

# ---- 16. Roles: the outside reader ------------------------------------
E('16 Roles, the outside reader named as it is today',
"""This matters beyond this chat. A relay partner (Fable, GPT, a fresh Claude
instance with no memory of prior sessions) has this protocol as its ONLY
""",
"""This matters beyond this chat. An outside model (GPT, Gemini, a Claude
session outside this Project) has this protocol as its ONLY
""")

# ---- 17. Version History ----------------------------------------------
E('17 Version History',
"""This is v4.0 (2026-11-23): the reduction of L-522, step 3. Every
earlier entry, and the stories behind the rules, are in
documentation/PROJECT_INSTRUCTIONS_HISTORY.md. A change to a rule here
""",
"""This is v4.1 (2026-11-25): The Project, in the archived master plan's
place (L-559). Every earlier entry, and the stories behind the rules, are in
documentation/PROJECT_INSTRUCTIONS_HISTORY.md. A change to a rule here
""")

SKIP = [n.strip() for n in sys.argv[3].split(',')] if len(sys.argv) > 3 else []
edits = [e for e in edits if e[0].split()[0] not in SKIP]
total = 0
for name, old, new in edits:
    n = text.count(old)
    assert n == 1, '%s: matched %d times' % (name, n)
    text = text.replace(old, new)
    d = new.count('\n') - old.count('\n')
    total += d
    print('%-78s %3d -> %3d  (%+d)' % (name[:78], old.count('\n'), new.count('\n'), d))
out_lines = text.count('\n')
print('base %d lines; edits sum %+d; v4.1 %d lines; arithmetic %s' % (
    base_lines, total, out_lines, 'HOLDS' if base_lines + total == out_lines else 'BROKEN'))
bad = sorted(set(ch for ch in text if ord(ch) > 127))
print('non-ASCII:', bad if bad else 'none')
print('longest line:', max(len(l) for l in text.split('\n')))
open(OUT, 'w', encoding='utf-8', newline='').write(text)
print('sha256', hashlib.sha256(text.encode()).hexdigest()[:12])
