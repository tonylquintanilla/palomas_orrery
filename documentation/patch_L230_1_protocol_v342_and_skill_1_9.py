"""patch_L230_1_protocol_v342_and_skill_1_9.py

Built on 41c0b27911bc25c88e6f7ccf98b6072beaffdebb at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 8ec4f261013f09697d649efd25c8a746bffeff64.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT. Open in VS Code, click Run.
    It edits four files, two of them under documentation/ and skills/.

Transactional, all-or-nothing, binary I/O, FOUR targets. Nothing is
written to ANY of them unless every anchor in ALL FOUR matches once.

WHY THIS PATCH EXISTS -- Tony's observation, 2026-08-23

"When we do skill updates, we should also update the project
information file, because the skill update goes in the skill manifest
and it should go in the history too."

He is describing a chain with four links:

    SKILL.md version line
      -> skills_index.py
        -> the manifest zone in PROJECT_INSTRUCTIONS.md
          -> a protocol VERSION HISTORY entry

The first three fire. The fourth does not, and it never had a written
home. This is not a new rule: the archive carries
`v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).` --
a skill bump alone earning an entry. The rule existed in practice and
stopped firing, which is the harder kind of gap to see.

The evidence of the gap is this same session: `safe-file-editing` went
to 1.8 and `orrery-coding-conventions` to 1.5, the manifest picked both
up automatically, and the protocol's written history recorded neither.
The generated half stayed current; the written half went stale.

WHAT IT DOES

  1. ledger-and-session-records 1.8 -> 1.9.
     Its "Protocol and Skills Change Log" section owns this. Two edits
     there:

     (a) THE BINDING RULE GAINS ITS FOURTH STEP. It said "bump the
         version line -> run skills_index.py -> commit both protocol
         copies." It now ends with the version-history entry.

     (b) A STALE SENTENCE IS CORRECTED. The section opened by saying
         the protocol's version history "lives in the ledger (appendix
         section)". v3.41 replaced that appendix with a pointer on
         2026-08-18; the history has lived in
         documentation/PROJECT_INSTRUCTIONS_HISTORY.md ever since. The
         skill that owns the change-log convention was itself carrying
         a five-day-old wrong claim about where the log lives -- The
         Correction Does Not Travel (safe-file-editing 1.8), found in
         the section that governs the thing.

  2. PROJECT_INSTRUCTIONS.md gains v3.42, recording all THREE of the
     day's skill bumps, and the header restamps v3.41 -> v3.42.

  3. v3.39 migrates down to documentation/PROJECT_INSTRUCTIONS_HISTORY.md,
     per the protocol's own mechanical rule: three entries stay
     resident, a fourth pushes the oldest out. It lands immediately
     after v3.38, which is where the archive currently ends -- so the
     archive stays contiguous with no gap.

  4. L-230 opens for the maintenance-suite checker, DEFERRED, with the
     design recorded and, more usefully, with the measurement that
     killed the naive design.

WHY THE CHECKER IS NOT BUILT HERE

  Tony's own suggestion, and it is right: the maintenance runner is the
  tool already in the routine, and the resident gate says put the check
  where it runs rather than in a document someone has to remember.

  But the OBVIOUS checker does not work, and this was measured rather
  than guessed. "For each skill in the manifest, does its current
  version appear anywhere in the written history?" reports 10 OF 10
  skills as unrecorded -- because only three entries stay resident, the
  archive names older versions, and several skills have sat at 1.1
  since creation and were never the subject of any entry. A check that
  fires on everything is ignored by its second run.

  The working design watches the TRANSITION, not the state: if a skill
  version changed since the last run, the protocol version must have
  changed too. That needs a state file, which is the pattern the suite
  already uses (data/worksheet_check_state.json,
  data/provenance_history.json) rather than a new store. Recorded in
  L-230 so a future session does not re-derive the dead end.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. v3.42, skill 1.9, the migrated entry and
  L-230 are not.

AFTER RUNNING, IN THIS ORDER
  1. python ledger_index.py
  2. python skills_index.py     (manifest still says 1.8)
  3. Settings > Skills: reinstall ledger-and-session-records (now 1.9).
  4. RE-UPLOAD PROJECT_INSTRUCTIONS.md to the Claude UI. It is a store
     in its own right, and this patch changed its version number.
  5. Maintenance suite; expect 11 of 11.
  6. Commit and push.
  7. Move this script to documentation/.

CARRIED OBLIGATION FOR THE HANDOFF
  THREE skill bumps today, so THREE confirmations next session:
  safe-file-editing 1.8, orrery-coding-conventions 1.5, and
  ledger-and-session-records 1.9. A mid-session reinstall cannot be
  verified from inside the session that makes it.
"""

import hashlib
import os
import sys

BASE_SHA = '41c0b27911bc25c88e6f7ccf98b6072beaffdebb'
GALLERY_SHA = '8ec4f261013f09697d649efd25c8a746bffeff64'

HERE = os.path.dirname(os.path.abspath(__file__))

SKILL = os.path.join('skills', 'ledger-and-session-records', 'SKILL.md')
PROTOCOL = 'PROJECT_INSTRUCTIONS.md'
ARCHIVE = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    SKILL: '232d0316c39a40cc1a4b113bf93c5f4e',
    PROTOCOL: '8601e37879dfc369e5113202bc4e3b41',
    ARCHIVE: '9916f325cb31e1ed6ea48c586849333b',
    LEDGER: '07bdb397c05a6edb6f699740b4e58f93',
}

TARGETS = [SKILL, PROTOCOL, ARCHIVE, LEDGER]

# EM DASH (U+2014), twice in the archive, predating this patch by weeks.
# Swept under safe-file-editing 1.8's rescoped Encoding Gate: a patch
# already holding a file open fixes incidental non-ASCII, and markdown
# is not an exception. Written as an escape so this script stays ASCII.
EM_DASH = '\u2014'
EXPECTED_EM_DASHES = 2


# ==================================================================
# EDIT 1 -- skill version line
# ==================================================================

OLD_1 = (
    "Skill version: 1.8 | Cut from palomas_orrery @ 3586970d (v1.8), earlier\n"
    "@ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970 (v1.5) | August 20,\n"
    "2026, with Anthropic's Claude Opus 5\n"
)
NEW_1 = (
    "Skill version: 1.9 | Cut from palomas_orrery @ 41c0b279 (v1.9), earlier\n"
    "@ 3586970d (v1.8), @ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970\n"
    "(v1.5) | August 23, 2026, with Anthropic's Claude Opus 5\n"
)


# ==================================================================
# EDIT 2 -- skill adds-paragraph
# ==================================================================

OLD_2 = (
    "and extends the status rule from handoff-vs-manifest to any session\n"
    "document contradicting a settled ledger decision (both L-221,\n"
    "August 20, 2026).\n"
)
NEW_2 = (
    "and extends the status rule from handoff-vs-manifest to any session\n"
    "document contradicting a settled ledger decision (both L-221,\n"
    "August 20, 2026). v1.9 (L-230) does two things to the Protocol and\n"
    "Skills Change Log. It adds the FOURTH step to the binding rule -- a\n"
    "skill bump also earns a protocol version-history entry, which is\n"
    "Tony's observation of August 23, 2026 that three links of a\n"
    "four-link chain were firing. And it corrects that section's own\n"
    "opening claim, which still said the protocol's version history lives\n"
    "in the ledger appendix five days after v3.41 replaced that appendix\n"
    "with a pointer.\n"
)


# ==================================================================
# EDIT 3 -- the stale sentence about where the history lives
# ==================================================================

OLD_3 = (
    "The protocol's version history lives in the ledger (appendix section),\n"
    "not in the protocol (which keeps the last few entries as a pointer).\n"
)
NEW_3 = (
    "The protocol's version history lives in\n"
    "`documentation/PROJECT_INSTRUCTIONS_HISTORY.md`, PART 1. The protocol\n"
    "itself keeps the THREE most recent entries resident; a fourth pushes\n"
    "the oldest down into that file, so an entry lives in exactly one place\n"
    "and never both. (Until 2026-08-23 this paragraph said the history\n"
    "lived in the ledger's appendix. v3.41 replaced that appendix with a\n"
    "pointer on 2026-08-18 and this sentence did not follow -- the section\n"
    "that owns the change-log convention carrying a stale claim about where\n"
    "the log lives. The Correction Does Not Travel, safe-file-editing 1.8.)\n"
)


# ==================================================================
# EDIT 4 -- the binding rule gains its fourth step
# ==================================================================

OLD_4 = (
    "**Binding rule [QUALITY].** A skill version bump is not done until the\n"
    "manifest agrees. The three steps travel in ONE commit: bump the version\n"
    "line in SKILL.md -> run `skills_index.py` -> commit SKILL.md and both\n"
    "protocol copies together. Do not leave the regeneration to a later\n"
    "checkpoint someone has to remember.\n"
)
NEW_4 = (
    "**Binding rule [QUALITY].** A skill version bump is not done until the\n"
    "manifest agrees AND the protocol's history says what changed. FOUR\n"
    "steps travel in ONE commit:\n"
    "\n"
    "1. Bump the version line in `SKILL.md`.\n"
    "2. Run `skills_index.py`.\n"
    "3. Add a **protocol version-history entry** to\n"
    "   `PROJECT_INSTRUCTIONS.md` naming the skill, the new version, and\n"
    "   WHY -- and push the oldest resident entry down into\n"
    "   `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` if that makes a\n"
    "   fourth.\n"
    "4. Commit `SKILL.md`, `PROJECT_INSTRUCTIONS.md` and the archive\n"
    "   together.\n"
    "\n"
    "Do not leave any of it to a later checkpoint someone has to remember.\n"
    "\n"
    "**Step 3 is the one that stops firing** (Tony's observation,\n"
    "2026-08-23). Steps 1, 2 and 4 are visible -- you are editing the file,\n"
    "running the tool, making the commit. Step 3 is the only one with no\n"
    "artifact prompting it, so it is the one that gets skipped, and the\n"
    "manifest going current on its own DISGUISES the omission: the protocol\n"
    "looks updated because half of it was. It is not a new rule --\n"
    "`v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).`\n"
    "is a skill bump earning an entry on its own. It stopped firing, which\n"
    "is harder to notice than a rule that never existed.\n"
    "\n"
    "Detection for step 3 is designed and unbuilt (L-230): a\n"
    "maintenance-suite checker that reports when a skill version changed\n"
    "since the last run and the protocol version did not. It has to watch\n"
    "the TRANSITION -- the naive form, asking whether each manifested\n"
    "version appears somewhere in the written history, was measured on\n"
    "2026-08-23 and reports 10 of 10 skills, which is a check nobody reads\n"
    "twice.\n"
)


# ==================================================================
# EDIT 5 -- protocol header restamp
# ==================================================================

OLD_5 = (
    "Tony Quintanilla, PE | Claude | v3.41 | August 23, 2026\n"
    "\n"
    "Cut from b65ac115 at https://github.com/tonylquintanilla/palomas_orrery\n"
)
NEW_5 = (
    "Tony Quintanilla, PE | Claude | v3.42 | August 23, 2026\n"
    "\n"
    "Cut from 41c0b279 at https://github.com/tonylquintanilla/palomas_orrery\n"
)


# ==================================================================
# EDIT 6a -- v3.42 goes in at the TOP of the resident list
# ==================================================================
# The resident three were ordered v3.41, v3.39, v3.40 -- not sorted.
# Inserting at the top and removing v3.39 leaves v3.42, v3.41, v3.40:
# reverse-chronological, which is what a reader expects.

OLD_6A = (
    "that file. An entry lives in exactly one place, never both.\n"
    "\n"
    "v3.41 (August 18, 2026): Records restructure and a skill bump.\n"
)
NEW_6A = (
    "that file. An entry lives in exactly one place, never both.\n"
    "\n"
    "v3.42 (August 23, 2026): No rule changed in this document. THREE skill\n"
    "bumps, recorded here because the recording is the point.\n"
    "(1) safe-file-editing 1.7 -> 1.8 (L-226), two of Tony's rulings. The\n"
    "Encoding Gate now says PROSE explicitly -- it read \"ASCII only in\n"
    "delivered code\" and a session took that as excluding markdown, leaving\n"
    "23 non-ASCII characters in a master plan it was already patching, while\n"
    "Stamp What You Change had said all along that markdown is not an\n"
    "exception. The skill's two halves disagreed and the reader followed the\n"
    "narrower one. And a new section, The Correction Does Not Travel, one\n"
    "scope out from Stamp What You Change: that governs the file the patch is\n"
    "editing, this governs the OTHER files quoting the value it just changed.\n"
    "Founding case -- constants_new.py read 15 R_sun from August 22 and the\n"
    "critical path summary still said 17 the next day, inside the paragraph\n"
    "written to correct an earlier wrong claim about the same row.\n"
    "(2) orrery-coding-conventions 1.4 -> 1.5 (L-227): Hover Line Width Is a\n"
    "Convention, Not an Accident. Found by Mode 5 when a tooltip ran off the\n"
    "viewport -- a hover string wrapped at 72 characters in the SOURCE with\n"
    "no breaks on the lines, rendering as one 378-character run. Canonical\n"
    "Text Format already governed which break character and said nothing\n"
    "about how often.\n"
    "(3) ledger-and-session-records 1.8 -> 1.9 (L-230), and it is why this\n"
    "entry exists at all. Tony observed that a skill bump runs a four-link\n"
    "chain -- SKILL.md, skills_index.py, the manifest zone, a protocol\n"
    "version entry -- and that only the first three fire. The binding rule\n"
    "gains its fourth step. Detection is designed and unbuilt: a\n"
    "maintenance-suite checker that watches the TRANSITION, because the\n"
    "naive form reports 10 of 10 skills and would be ignored by its second\n"
    "run.\n"
    "\n"
    "v3.41 (August 18, 2026): Records restructure and a skill bump.\n"
)


# ==================================================================
# EDIT 6b -- v3.39 leaves the resident list (it MOVES, see edit 7)
# ==================================================================

OLD_6B = (
    "v3.39 (August 12, 2026): One change. \"A Check That Cannot Fail Is Not\n"
    "Passing\" added to Part 3 as a CRITICAL gate, immediately after Verify\n"
    "Execution, Not Appearance, which it extends: that gate asks whether the\n"
    "edited code is the code that runs, this one asks whether the check being\n"
    "trusted can produce a failure at all. Origin was three instances in a\n"
    "single session, each in a different layer and each indistinguishable\n"
    "from a pass -- the provenance-discipline skill teaching an annotation\n"
    "format its own parser could not read, test_constants_provenance.py\n"
    "pinning 55 values in a file no routine executed, and\n"
    "constants_change_report.py reporting clean both for an edit shape it\n"
    "could not parse and for a path git does not track. The gate's three\n"
    "moves are: make success carry evidence, make the blind spot announce,\n"
    "and put the check where it actually runs. Tony's confirming question --\n"
    "what tells us it is working -- is the one that found the third instance.\n"
    "\n"
)
NEW_6B = ""


# ==================================================================
# EDIT 7 -- v3.39 lands in the archive, after v3.38
# ==================================================================

OLD_7 = (
    "Skill-layer companion: provenance-discipline v1.9 narrows the push gate\n"
    "to the ACTIVE BUILD PATH (L-184, ratified 2026-08-05), keeping global\n"
    "Tier-1 = 0 as the destination rather than the firing rule (finding F1).\n"
    "\n"
    "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"
)
NEW_7 = (
    "Skill-layer companion: provenance-discipline v1.9 narrows the push gate\n"
    "to the ACTIVE BUILD PATH (L-184, ratified 2026-08-05), keeping global\n"
    "Tier-1 = 0 as the destination rather than the firing rule (finding F1).\n"
    "\n"
    "v3.39 (August 12, 2026): One change. \"A Check That Cannot Fail Is Not\n"
    "Passing\" added to Part 3 as a CRITICAL gate, immediately after Verify\n"
    "Execution, Not Appearance, which it extends: that gate asks whether the\n"
    "edited code is the code that runs, this one asks whether the check being\n"
    "trusted can produce a failure at all. Origin was three instances in a\n"
    "single session, each in a different layer and each indistinguishable\n"
    "from a pass -- the provenance-discipline skill teaching an annotation\n"
    "format its own parser could not read, test_constants_provenance.py\n"
    "pinning 55 values in a file no routine executed, and\n"
    "constants_change_report.py reporting clean both for an edit shape it\n"
    "could not parse and for a path git does not track. The gate's three\n"
    "moves are: make success carry evidence, make the blind spot announce,\n"
    "and put the check where it actually runs. Tony's confirming question --\n"
    "what tells us it is working -- is the one that found the third instance.\n"
    "(Moved down from the resident protocol on 2026-08-23 when v3.42 made a\n"
    "fourth entry.)\n"
    "\n"
    "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"
)


# ==================================================================
# EDIT 8 -- L-230
# ==================================================================

OLD_8 = (
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)
NEW_8 = (
    "\n"
    "#### [L-230] A skill bump does not reach the protocol's version history\n"
    "<!-- L:230 status:DEFERRED upd:2026-08-23 section:A flag: "
    "rice:3/3/85/2 -->\n"
    "- **Tony's observation, 2026-08-23.** A skill bump runs a four-link\n"
    "  chain: `SKILL.md` version line -> `skills_index.py` -> the manifest\n"
    "  zone in `PROJECT_INSTRUCTIONS.md` -> a protocol VERSION HISTORY\n"
    "  entry. The first three fire. The fourth does not.\n"
    "- **Not a new rule -- one that stopped firing.** The archive carries\n"
    "  `v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).`\n"
    "  A skill bump earning an entry on its own. That is harder to notice\n"
    "  than a rule that never existed, and the manifest going current by\n"
    "  itself DISGUISES the omission: the protocol looks updated because\n"
    "  half of it was.\n"
    "- **Prevention landed 2026-08-23** in `ledger-and-session-records`\n"
    "  1.9: the binding rule gains its fourth step. Detection is this item.\n"
    "- **Tony's design instinct, and it is right:** report it in the\n"
    "  maintenance runner. That is the tool already in the routine, and\n"
    "  the resident gate says put the check where it runs rather than in a\n"
    "  document someone has to remember. An earlier Claude proposal to\n"
    "  write the convention into the protocol as prose was redirected for\n"
    "  exactly that reason.\n"
    "- **THE NAIVE CHECKER DOES NOT WORK, and this was measured rather\n"
    "  than guessed.** \"For each skill in the manifest, does its current\n"
    "  version appear anywhere in the written history?\" reports **10 of\n"
    "  10** skills as unrecorded at `41c0b279`. Three causes: only three\n"
    "  entries stay resident, the archive names older versions, and several\n"
    "  skills have sat at 1.1 since creation and were never the subject of\n"
    "  any entry. A check that fires on everything is ignored by its second\n"
    "  run -- the same failure as an audit whose denominator grows whenever\n"
    "  someone thinks of something.\n"
    "- **The design that does work watches the TRANSITION, not the state.**\n"
    "  If a skill version changed since the last run, the protocol version\n"
    "  must have changed too. That needs memory of the previous state,\n"
    "  which is the pattern the suite already uses\n"
    "  (`data/worksheet_check_state.json`, `data/provenance_history.json`)\n"
    "  rather than a new store. It can fail, and it fails exactly once per\n"
    "  unrecorded bump, which is what makes it worth running.\n"
    "- **Deferred deliberately.** A checker module, a state file, runner\n"
    "  wiring and its own test is a build, not a patch, and it deserves the\n"
    "  design round. The dead end above is recorded so a future session\n"
    "  does not re-derive it.\n"
    "- **Note:** RICE 3/3/85/2 -> 3.8 is Claude's proposed score.\n"
    "  **Tony-action (decide):** confirm or redirect, then re-run\n"
    "  `ledger_index.py`.\n"
    "- **Ref:** `PROJECT_INSTRUCTIONS.md` v3.42 and its Skill Manifest;\n"
    "  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`; `skills_index.py`;\n"
    "  `skills/ledger-and-session-records/SKILL.md` v1.9, Protocol and\n"
    "  Skills Change Log; L-188 (the maintenance runner); L-226, L-227 (the\n"
    "  two bumps whose absence from the history exposed this).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)


# ==================================================================
# EDIT 9 -- ledger currency stamp
# ==================================================================

OLD_9 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229\n"
    "part 2: the orientation is declared an ASSUMPTION; the unsourced\n"
    "magnetic-equator argument is withdrawn), built on ca97e81d.\n"
)
NEW_9 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229\n"
    "part 2: the orientation is declared an ASSUMPTION; the unsourced\n"
    "magnetic-equator argument is withdrawn), built on ca97e81d.\n"
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-230\n"
    "opened; protocol v3.42; ledger-and-session-records 1.8 -> 1.9),\n"
    "built on 41c0b279.\n"
)


EDITS = [
    (SKILL, '1 skill version 1.8 -> 1.9', OLD_1, NEW_1),
    (SKILL, '2 skill adds-paragraph', OLD_2, NEW_2),
    (SKILL, '3 stale "history lives in the ledger" corrected', OLD_3, NEW_3),
    (SKILL, '4 binding rule gains its fourth step', OLD_4, NEW_4),
    (PROTOCOL, '5 header restamp v3.41 -> v3.42', OLD_5, NEW_5),
    (PROTOCOL, '6a v3.42 inserted at the top', OLD_6A, NEW_6A),
    (PROTOCOL, '6b v3.39 removed (it moves to the archive)', OLD_6B, NEW_6B),
    (ARCHIVE, '7 v3.39 lands after v3.38', OLD_7, NEW_7),
    (LEDGER, '8 L-230 opened', OLD_8, NEW_8),
    (LEDGER, '9 ledger currency stamp', OLD_9, NEW_9),
]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. ALL FOUR files on disk are untouched.')
    sys.exit(1)


def main():
    print('patch_L230_1_protocol_v342_and_skill_1_9.py')
    print('built on %s' % BASE_SHA)
    print('')

    paths, originals, endings = {}, {}, {}
    for name in TARGETS:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            fail('%s not found relative to this script.\n'
                 '       This one goes in the REPO ROOT.\n'
                 '       It looked in: %s' % (name, HERE))
        paths[name] = path
        with open(path, 'rb') as handle:
            originals[name] = handle.read()

    for name in TARGETS:
        normalized = originals[name].replace(b'\r\n', b'\n')
        got = hashlib.md5(normalized).hexdigest()
        if got != FINGERPRINTS[name]:
            fail('BASE MOVED. %s fingerprints %s; built against %s.'
                 % (name, got, FINGERPRINTS[name]))
        endings[name] = b'\r\n' if b'\r\n' in originals[name] else b'\n'
        print('[base ok]       %-44s %s (%s)'
              % (name, got, 'CRLF' if endings[name] == b'\r\n' else 'LF'))

    for _n, label, old, new in EDITS:
        if sum(1 for ch in new if ord(ch) > 127) > \
                sum(1 for ch in old if ord(ch) > 127):
            fail('edit %s would INTRODUCE a non-ASCII character.' % label)
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    if any(byte > 127 for byte in own):
        fail('this script itself is not pure ASCII.')
    print('[ascii ok]      no edit introduces non-ASCII; script is ASCII '
          '(%d bytes)' % len(own))

    working = {n: originals[n].replace(b'\r\n', b'\n').decode('utf-8')
               for n in TARGETS}

    if '<!-- L:230 ' in working[LEDGER]:
        fail('L-230 already has an index comment; this would duplicate it.')
    print('[handle ok]     L-230 is absent, as expected')

    for name, label, old, new in EDITS:
        count = working[name].count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected 1 match, found %d. '
                 'First 70 chars: %r' % (label, count, old[:70]))
        working[name] = working[name].replace(old, new, 1)
        print('[ok]            %s' % label)

    for name in TARGETS:
        allowed = set()
        for n, _label, old, new in EDITS:
            if n != name:
                continue
            allowed.update(l for l in
                           (set(old.split('\n')) - set(new.split('\n'))) if l)
        after = set(working[name].split('\n'))
        before = originals[name].replace(b'\r\n', b'\n').decode('utf-8')
        lost = [l for l in before.split('\n') if l and l not in after]
        unexpected = [l for l in lost if l not in allowed]
        if unexpected:
            fail('%d line(s) of %s would be lost that no edit claims to '
                 'rewrite. First: %r'
                 % (len(unexpected), name, unexpected[0]))
        print('[addition ok]   %-44s %d line(s) rewritten'
              % (name, len(lost)))

    # --- The migration must be exactly a MOVE, not a copy or a loss --
    marker = 'v3.39 (August 12, 2026): One change.'
    if marker in working[PROTOCOL]:
        fail('v3.39 survives in the resident protocol -- it must MOVE, not '
             'be duplicated. Three entries stay resident, not four.')
    if working[ARCHIVE].count(marker) != 1:
        fail('v3.39 did not land in the archive exactly once (found %d).'
             % working[ARCHIVE].count(marker))
    resident = [l for l in working[PROTOCOL].split('\n')
                if l.startswith('v3.') and ' (August' in l]
    if len(resident) != 3:
        fail('the resident history holds %d entries; the protocol\'s own '
             'rule is exactly three. Found: %r'
             % (len(resident), [l[:12] for l in resident]))
    print('[migration ok]  v3.39 moved, not copied; %d entries resident, '
          'as the rule requires' % len(resident))

    found = working[ARCHIVE].count(EM_DASH)
    if found != EXPECTED_EM_DASHES:
        fail('expected %d em dash(es) in %s; found %d. Refusing to sweep '
             'blind.' % (EXPECTED_EM_DASHES, ARCHIVE, found))
    working[ARCHIVE] = working[ARCHIVE].replace(EM_DASH, '--')
    for name in TARGETS:
        left = sum(1 for ch in working[name] if ord(ch) > 127)
        if left:
            fail('%s still holds %d non-ASCII character(s).' % (name, left))
    print('[swept]         %d em dash(es) -> ASCII; all four targets are '
          'now pure ASCII' % found)

    if 'v3.42' not in working[PROTOCOL].split('\n')[1]:
        fail('the header did not restamp to v3.42.')
    if 'Skill version: 1.9' not in working[SKILL]:
        fail('the skill version did not land as 1.9.')
    if 'Skill version: 1.8' in working[SKILL]:
        fail('a 1.8 version line survives in the skill.')
    print('[version ok]    protocol header v3.42; SKILL.md declares 1.9')

    # ALL-OR-NOTHING, FOR REAL. Encode every target BEFORE writing any of
    # them. The earlier pattern encoded and wrote in one loop, so an encode
    # failure on file 3 left files 1 and 2 already on disk -- the harness
    # was transactional against ANCHOR failures (which happen before any
    # write) and not against ENCODE failures. Found 2026-08-23 when this
    # very patch hit a pre-existing em dash in the archive and wrote two
    # files before stopping. A promise that only holds for the failure mode
    # you happened to exercise is not a promise.
    encoded = {}
    for name in TARGETS:
        try:
            out = working[name].encode('ascii')
        except UnicodeEncodeError as exc:
            fail('%s would not encode as ASCII after patching: %s. Nothing '
                 'has been written -- the encode phase runs before the write '
                 'phase precisely so this is recoverable.' % (name, exc))
        if endings[name] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        encoded[name] = out
    print('[encode ok]     all %d targets encode as ASCII; writing now'
          % len(TARGETS))

    for name in TARGETS:
        with open(paths[name], 'wb') as handle:
            handle.write(encoded[name])
        print('[written]       %-44s %d -> %d bytes'
              % (name, len(originals[name]), len(encoded[name])))

    print('')
    print('patch applied -- %d edits across %d files'
          % (len(EDITS), len(TARGETS)))
    print('')
    print('NEXT, IN THIS ORDER:')
    print('  1. python ledger_index.py')
    print('  2. python skills_index.py     (manifest still says 1.8)')
    print('  3. Settings > Skills: reinstall ledger-and-session-records (1.9)')
    print('  4. RE-UPLOAD PROJECT_INSTRUCTIONS.md to the Claude UI --')
    print('     it is a store in its own right and its version changed.')
    print('  5. Maintenance suite; expect 11 of 11.')
    print('  6. Commit and push.')
    print('  7. Move this script to documentation/.')
    print('')
    print('CARRIED OBLIGATION for the handoff -- THREE now, not two:')
    print('  safe-file-editing 1.8, orrery-coding-conventions 1.5, and')
    print('  ledger-and-session-records 1.9. The next session confirms all')
    print('  three loaded copies before doing work in their scope.')
    print('')
    print('OPEN FOR TONY:')
    print('  - L-230 proposed RICE 3/3/85/2 (3.8), DEFERRED. The checker is')
    print('    designed, not built; the dead end is recorded so it is not')
    print('    re-derived.')


if __name__ == '__main__':
    main()
