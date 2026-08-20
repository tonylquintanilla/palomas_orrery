"""patch_L221_1_master_plan_sequencing.py

Built on 3586970dd841d5b417f8e6f59de4d3e3d440d001 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 20, 2026 with Anthropic's Claude Opus 5.

Transactional, all-or-nothing, binary I/O (both targets are pure LF at
the base SHA and stay that way). Nothing is written unless every anchor
in every file matches exactly once.

WHAT IT DOES

  LEDGER_CONSOLIDATED.md
    1. L-214 build-step wording corrected: the scanner and checker are
       not compiling their own patterns. Two homes that DISAGREE.
    2. L-214 gains four bullets -- the correction, the note that the
       case question is already answered by step 6, the label-set /
       body-grammar scoping split, and the missing Role: tag on
       worksheet_keys.py that the build picks up in passing.
    3. New item L-221 opened in section A.
    4. Header currency stamp.

  skills/ledger-and-session-records/SKILL.md
    5. Document Stack gains the master plan, as a SEQUENCING authority
       rather than a rung in the status ordering; and the status rule
       is extended from handoff-vs-manifest to any session document
       contradicting a settled ledger decision.
    6. Version 1.7 -> 1.8 with its cut-from SHA, date and adds-paragraph.

  Cross-handle note: this script is named for L-221 but also amends
  L-214's block. That is exactly the gap L-219 is open on -- the naming
  convention cannot express a cross-handle run order. Recorded, not
  worked around.

AFTER RUNNING
  python ledger_index.py       (regenerates the ledger index tables)
  python skills_index.py       (regenerates the manifest in PROJECT_INSTRUCTIONS)
  Reinstall ledger-and-session-records at Settings > Skills.
  Move this script to documentation/.
"""

import hashlib
import os
import sys

BASE_SHA = '3586970dd841d5b417f8e6f59de4d3e3d440d001'
MODEL = "Anthropic's Claude Opus 5"

LEDGER = 'LEDGER_CONSOLIDATED.md'
SKILL = os.path.join('skills', 'ledger-and-session-records', 'SKILL.md')

# Fingerprints of the two targets at BASE_SHA. A mismatch aborts before
# anything is written, and says which file moved.
FINGERPRINTS = {
    LEDGER: '64adfa3b3e500ca8817d1071cdffa89a',
    SKILL: 'd51ed6695816a80551f909b8ad79a8f0',
}

# ------------------------------------------------------------------
# EDIT 1 -- L-214 build-step wording
# ------------------------------------------------------------------

LEDGER_OLD_1 = (
    "generic label detection separated from policy; one home for the\n"
    "vocabulary with the scanner and the checker importing rather than\n"
    "compiling their own; `Note` admitted to context; `# Review-note:`\n"
    "added as withheld free-form; the moon line rehomed; the four odd\n"
    "labels fixed at source; the 12-line marker sweep. Deciding the form of\n"
)

LEDGER_NEW_1 = (
    "generic label detection separated from policy; one home for the\n"
    "vocabulary that both the scanner and the checker read from; `Note`\n"
    "admitted to context; `# Review-note:` added as withheld free-form; the\n"
    "moon line rehomed; the four odd labels fixed at source; the 12-line\n"
    "marker sweep. Deciding the form of\n"
)

# ------------------------------------------------------------------
# EDIT 2 -- four bullets appended to L-214, before its Gap line
# ------------------------------------------------------------------

LEDGER_ANCHOR_2 = (
    "  labels that have no compiled pattern -- the two nothing was\n"
    "  watching.\n"
    "**Gap:** the BUILD."
)

LEDGER_INSERT_2 = (
    "  labels that have no compiled pattern -- the two nothing was\n"
    "  watching.\n"
    "- **CORRECTION, 2026-08-20: nobody is compiling the vocabulary\n"
    "  twice** [verified @3586970d]. The build-step wording above said\n"
    "  the scanner and the checker should import \"rather than compiling\n"
    "  their own.\" That overstated the problem. `worksheet_checker.py`\n"
    "  already imports both record patterns from `provenance_scanner`\n"
    "  (`ps.CROSS_CHECK_LINE_RE` at line 1190, `ps.RESOLVED_LINE_RE` at\n"
    "  line 1623) and compiles no copies of its own. The state is not\n"
    "  one duplicated set. It is TWO single homes that DISAGREE: the\n"
    "  scanner's patterns are compiled `(?mi)`, case-INsensitive, while\n"
    "  `LEG_RE` in `worksheet_keys.py` carries no flags and is\n"
    "  case-SENSITIVE. The wording is corrected above.\n"
    "- **That disagreement is NOT a new decision, and reopening it as\n"
    "  one would have undone a measured build step.** Step 6 already\n"
    "  fixes the four odd labels at source, and the 12-lines-at-8-sites\n"
    "  count depends on that relabelling. Relaxing the shared matcher to\n"
    "  ignore case would make `# NOTE:` work without being edited,\n"
    "  remove part of step 6's reason to exist, and invalidate the\n"
    "  count Fable had already caught this project undercounting once.\n"
    "  The ruling stands as made: edit at source, do not alias, do not\n"
    "  relax the matcher. The scanner keeps its existing\n"
    "  case-insensitive behaviour by default, and after step 6 nothing\n"
    "  case-odd remains on the builder's side to disagree about.\n"
    "- **SCOPING: move the label SET, not the body grammar** [verified\n"
    "  @3586970d]. \"One home for the vocabulary\" can be read as \"move\n"
    "  the regexes,\" which would drag semantics into a keys module. The\n"
    "  scanner's constants are label names PLUS a body contract:\n"
    "  `RESOLVED_LINE_RE` has a companion `RESOLVED_BODY_RE` enforcing\n"
    "  `<worksheet> <key> -- <what> (L-nnn)` with ISO-only dates. What\n"
    "  moves to `worksheet_keys.py` is the label set and its TRANSPORT\n"
    "  policy -- which labels exist, and for each, whether it travels to\n"
    "  a responder or is withheld. What stays in `provenance_scanner.py`\n"
    "  is the body GRAMMAR and its validation, with the scanner's line\n"
    "  patterns derived from the shared label names rather than from its\n"
    "  own literals. That is the same transport/grammar split the Mode 7\n"
    "  review settled on, applied one layer down.\n"
    "- **`worksheet_keys.py` carries no `Role:` tag** [verified\n"
    "  @3586970d]. `Domain: dev_tools` is present and `Role:` is absent,\n"
    "  so `module_atlas.py` files it under \"Undetermined role (6)\" on\n"
    "  the atlas's own front page -- together with\n"
    "  `worksheet_key_aliases.py`, `test_worksheet_keys.py` and\n"
    "  `test_extractor_pins.py`, the whole worksheet-keys cluster\n"
    "  untagged as a group. The build opens that docstring anyway for\n"
    "  the SECOND JOB section, so the tag goes in the same patch under\n"
    "  Fix In Passing, Report It. `TAG_RE` requires `Role:` alone on a\n"
    "  line with a SINGLE-token value drawn from `VALID_ROLES`, read via\n"
    "  `ast.get_docstring` -- a two-word value or a comment-block header\n"
    "  reads as absent rather than as an error.\n"
    "**Gap:** the BUILD."
)

# ------------------------------------------------------------------
# EDIT 3 -- new item L-221, at the end of section A
# ------------------------------------------------------------------

LEDGER_ANCHOR_3 = (
    "exposed it); HANDOFF_20260819_alfven_and_the_swap.md, error 4.\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)

LEDGER_INSERT_3 = (
    "exposed it); HANDOFF_20260819_alfven_and_the_swap.md, error 4.\n"
    "\n"
    "#### [L-221] The master plan is the roadmap, and it outranks RICE\n"
    "<!-- L:221 status:OPEN upd:2026-08-20 section:A flag: rice:3/2/90/0.5 -->\n"
    "- **Tony's ruling, 2026-08-20.** The document stack in\n"
    "  `ledger-and-session-records` is an AUTHORITY ordering -- who wins\n"
    "  when two documents disagree about status. The master plan is not\n"
    "  in it and does not belong in it, because it is not competing on\n"
    "  that axis. It has a different authority: SEQUENCING.\n"
    "- **What the master plan is for.** It is the roadmap -- where we\n"
    "  are and where we are going, not what is directly in front. It is\n"
    "  traced at three levels of zoom: the full plan\n"
    "  (`MASTER_PLAN_INTERACTIVE_GALLERY.md`), its summary, and the\n"
    "  critical path (`MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`).\n"
    "- **It updates at key junctures, not at every change.** Stepwise\n"
    "  updating is the ledger's job. That cadence is a property of what\n"
    "  the plan is for, not a defect to be corrected by restamping it\n"
    "  more often -- a juncture is its unit.\n"
    "- **It outranks RICE on sequencing.** RICE ranks items in\n"
    "  isolation. Bundling several items to complete a planned step\n"
    "  SUPERSEDES RICE order. The ledger header already calls RICE\n"
    "  \"prioritization for planning\"; this names what the planning is\n"
    "  and says it wins. Where the plan and the ledger disagree about\n"
    "  STATUS, the ledger still wins -- the two authorities do not\n"
    "  overlap.\n"
    "- **Why it came up.** A session read the missing anchor on the\n"
    "  2,010-line gallery master plan as evidence the plan was stale and\n"
    "  proposed ranking it below the ledger on currency. That framing\n"
    "  implies the plan is deficient and should update more often, which\n"
    "  would manufacture work. Tony's correction supplied the right\n"
    "  axis. (The missing anchor itself is not a finding: it is the\n"
    "  founding case of L-220, already ruled.)\n"
    "- **Confirmed the same day: the status rule covers session\n"
    "  DOCUMENTS, not just handoffs and manifests.** The skill stated it\n"
    "  for handoff-vs-manifest only. Any document written in a live\n"
    "  session -- a review return, a design note, an analysis -- can\n"
    "  assert that a question is open when the ledger has settled it.\n"
    "  Newest bytes are not a claim about what was decided. Recorded in\n"
    "  `ledger-and-session-records` 1.8 beside the ruling above.\n"
    "**Note:** RICE is Claude's proposal, unratified.\n"
    "**Gap:** none -- both rulings are recorded in\n"
    "`ledger-and-session-records` 1.8 by this patch. Close once a session\n"
    "confirms its loaded copy reads 1.8.\n"
    "**Ref:** `skills/ledger-and-session-records/SKILL.md` \"The Document\n"
    "Stack\"; LEDGER_CONSOLIDATED.md \"RICE scoring -- prioritization for\n"
    "planning\"; L-220 (Stamp What You Change); L-215 (the RICE tail\n"
    "measurement); L-214 (the session this surfaced in).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)

# ------------------------------------------------------------------
# EDIT 4 -- ledger header currency stamp
# ------------------------------------------------------------------

LEDGER_OLD_4 = (
    "Module updated: June 2026 with Anthropic's Claude Sonnet 4.6, Opus 4.8"
    " + Claude Fable 5\n"
    "Review and RICE update Tony 6-21-2026\n"
)

LEDGER_NEW_4 = (
    "Module updated: June 2026 with Anthropic's Claude Sonnet 4.6, Opus 4.8"
    " + Claude Fable 5\n"
    "Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-221:\n"
    "master plan as sequencing authority; L-214 correction and scoping),\n"
    "built on 3586970d.\n"
    "Review and RICE update Tony 6-21-2026\n"
)

# ------------------------------------------------------------------
# EDIT 5 -- skill: the master plan enters the Document Stack
# ------------------------------------------------------------------

SKILL_ANCHOR_5 = (
    "- Manifest: the executable build contract, written against HEAD at build\n"
    "  time (never on an un-pushed base); opens with the anchor (built on\n"
    "  <SHA> at <URL>) per the requirement below. If handoff and manifest\n"
    "  disagree, that is a flag to raise, not a thing to silently resolve.\n"
)

SKILL_INSERT_5 = (
    "- Manifest: the executable build contract, written against HEAD at build\n"
    "  time (never on an un-pushed base); opens with the anchor (built on\n"
    "  <SHA> at <URL>) per the requirement below. If handoff and manifest\n"
    "  disagree, that is a flag to raise, not a thing to silently resolve.\n"
    "\n"
    "**The master plan is not a rung in that ordering** (Tony's ruling,\n"
    "2026-08-20, L-221). It is the ROADMAP -- where we are and where we\n"
    "are going, not what is directly in front -- traced at three levels\n"
    "of zoom: the full plan, its summary, and the critical path. It\n"
    "restamps at key junctures rather than at every change, because a\n"
    "juncture is its unit; stepwise updating is the ledger's job. That\n"
    "cadence is not staleness to be corrected by restamping more often.\n"
    "\n"
    "It does not compete on the axis above, which is about STATUS: where\n"
    "any two documents disagree about what is done, the ledger wins. The\n"
    "plan carries a different authority, SEQUENCING. RICE ranks items in\n"
    "isolation; bundling several items to complete a planned step\n"
    "SUPERSEDES RICE order. The ledger already calls RICE\n"
    "\"prioritization for planning\" -- this names what the planning is\n"
    "and says it outranks the score.\n"
    "\n"
    "**The same rule reaches past handoffs and manifests** (Tony's\n"
    "ruling, 2026-08-20, L-221). Any session document -- a review\n"
    "return, a design note, an analysis written this session -- can\n"
    "assert that a question is open when the ledger has already settled\n"
    "it. Being the newest file in the room makes a document's BYTES\n"
    "current; it does not make it right about what was decided. Context\n"
    "Priority ranks uploads above the repo for exactly the first reason\n"
    "and not the second. So check a document's status claims against the\n"
    "ledger before acting on them, and raise the disagreement rather\n"
    "than resolving it silently. (Origin, 2026-08-20: a document's\n"
    "closing section said a decision \"belongs to Tony\"; the ledger had\n"
    "ruled it two sessions earlier and a build step depended on the\n"
    "ruling.)\n"
)

# ------------------------------------------------------------------
# EDIT 6 -- skill version block
# ------------------------------------------------------------------

SKILL_OLD_6 = (
    "Skill version: 1.7 | Cut from palomas_orrery @ 434a712b (v1.7), earlier\n"
    "@ 305b269 (v1.6), @ 3398970 (v1.5) | August 19, 2026\n"
)

SKILL_NEW_6 = (
    "Skill version: 1.8 | Cut from palomas_orrery @ 3586970d (v1.8), earlier\n"
    "@ 434a712b (v1.7), @ 305b269 (v1.6), @ 3398970 (v1.5) | August 20,\n"
    "2026, with Anthropic's Claude Opus 5\n"
)

SKILL_OLD_7 = (
    "below RICE 3.0 and untouched for a month (L-215).\n"
)

SKILL_NEW_7 = (
    "below RICE 3.0 and untouched for a month (L-215). v1.8 adds the\n"
    "master plan to The Document Stack as a SEQUENCING authority rather\n"
    "than a rung in the status ordering, with Tony's ruling that\n"
    "bundling items to complete a planned step supersedes RICE order,\n"
    "and extends the status rule from handoff-vs-manifest to any session\n"
    "document contradicting a settled ledger decision (both L-221,\n"
    "August 20, 2026).\n"
)

EDITS = [
    (LEDGER, 'L-214 build-step wording', LEDGER_OLD_1, LEDGER_NEW_1),
    (LEDGER, 'L-214 correction/scoping bullets', LEDGER_ANCHOR_2,
     LEDGER_INSERT_2),
    (LEDGER, 'new item L-221', LEDGER_ANCHOR_3, LEDGER_INSERT_3),
    (LEDGER, 'CURRENCY: ledger header stamp', LEDGER_OLD_4, LEDGER_NEW_4),
    (SKILL, 'Document Stack: master plan', SKILL_ANCHOR_5, SKILL_INSERT_5),
    (SKILL, 'CURRENCY: skill version 1.7 -> 1.8', SKILL_OLD_6, SKILL_NEW_6),
    (SKILL, 'CURRENCY: skill adds-paragraph', SKILL_OLD_7, SKILL_NEW_7),
]


def fail(message):
    print('ABORT: %s' % message)
    print('Nothing was written.')
    sys.exit(1)


def main():
    for path in (LEDGER, SKILL):
        if not os.path.isfile(path):
            fail('%s not found. Run this from the repo root.' % path)

    # --- Gate 1: base fingerprints ---------------------------------
    originals = {}
    for path, expected in FINGERPRINTS.items():
        with open(path, 'rb') as handle:
            data = handle.read()
        actual = hashlib.md5(data).hexdigest()
        if actual != expected:
            fail('%s does not match the base at %s.\n'
                 '  expected md5 %s\n  actual   md5 %s\n'
                 '  Reconcile against HEAD before running this.'
                 % (path, BASE_SHA[:8], expected, actual))
        originals[path] = data
        print('[base ok] %s  md5 %s' % (path, actual))

    # --- Gate 2: encoding -------------------------------------------
    for path, data in originals.items():
        try:
            data.decode('ascii')
        except UnicodeDecodeError as exc:
            fail('%s carries non-ASCII bytes at offset %d. This patch does '
                 'not sweep pre-existing non-ASCII; report it instead.'
                 % (path, exc.start))
        print('[ascii ok] %s' % path)

    # --- Gate 3: every anchor matches exactly once -------------------
    working = dict((p, d.decode('ascii')) for p, d in originals.items())
    for path, label, old, new in EDITS:
        count = working[path].count(old)
        if count != 1:
            fail('anchor for "%s" in %s matched %d times, expected exactly 1.'
                 % (label, path, count))
        working[path] = working[path].replace(old, new, 1)
        print('[anchor ok] %-34s %s' % (label, path))

    # --- Gate 4: no line disappears that no edit claims to rewrite ---
    # The permitted-loss set is DERIVED from the edits, not hand-listed:
    # a line may vanish only if it appears in some edit's `old` fragment
    # and not in that edit's `new` fragment. A hand-maintained list would
    # drift out of step with the edits it is supposed to describe; this
    # cannot, because it is built from them. (Every fragment above is cut
    # on line boundaries, which is what makes this comparison honest.)
    allowed = {}
    for path, label, old, new in EDITS:
        gone = set(old.split('\n')) - set(new.split('\n'))
        allowed.setdefault(path, set()).update(l for l in gone if l)

    for path in (LEDGER, SKILL):
        before = originals[path].decode('ascii').split('\n')
        after = set(working[path].split('\n'))
        lost = [line for line in before if line and line not in after]
        unexpected = [l for l in lost if l not in allowed.get(path, set())]
        if unexpected:
            fail('%d line(s) of %s would be lost that no edit claims to '
                 'rewrite. First: %r' % (len(unexpected), path,
                                         unexpected[0]))
        print('[addition ok] %-38s %d line(s) rewritten, all accounted for'
              % (path, len(lost)))

    # --- Write, all or nothing --------------------------------------
    for path in (LEDGER, SKILL):
        with open(path, 'wb') as handle:
            handle.write(working[path].encode('ascii'))
        print('[written] %s' % path)

    print('')
    print('CURRENCY STAMPS UPDATED (Stamp What You Change, '
          'safe-file-editing 1.6):')
    print('  %s  -- header "Module updated" line, %s, built on %s'
          % (LEDGER, MODEL, BASE_SHA[:8]))
    print('  %s  -- Skill version 1.7 -> 1.8, cut-from SHA, date, model, '
          'and the vN.M adds paragraph' % SKILL)
    print('')
    print('NEXT, in this order:')
    print('  1. python ledger_index.py')
    print('  2. python skills_index.py')
    print('  3. Settings > Skills: reinstall ledger-and-session-records '
          '(now 1.8)')
    print('  4. Move this script to documentation/')
    print('  5. Commit and push all of it in ONE commit '
          '(skill bump + manifest travel together)')
    print('')
    print('CARRIED OBLIGATION for the handoff: this bumps '
          'ledger-and-session-records to 1.8, and a reinstall cannot be '
          'verified from inside the session that makes it. The NEXT '
          'session confirms its loaded copy reads 1.8 before doing '
          'ledger work.')


if __name__ == '__main__':
    main()
