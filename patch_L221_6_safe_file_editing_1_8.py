"""patch_L221_6_safe_file_editing_1_8.py

Built on 6d12ecace4c5867d4d718466c7ef5923fc47622e at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6.
Both confirmed by live git ls-remote.
Written August 23, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into the REPO ROOT (the folder holding LEDGER_CONSOLIDATED.md,
    skills_index.py and the skills/ folder). Open in VS Code, click Run.
    Equivalent command: python patch_L221_6_safe_file_editing_1_8.py

Transactional, all-or-nothing, binary I/O, two targets. Nothing is
written to EITHER file unless every anchor in BOTH matches exactly once.

  skills/safe-file-editing/SKILL.md   1.7 -> 1.8
  LEDGER_CONSOLIDATED.md              L-226 opened (the skill bump)

WHAT IT ADDS -- two of Tony's rulings, both made 2026-08-23

  1. THE ENCODING GATE IS RESCOPED TO PROSE.
     It read "ASCII only in delivered CODE." A session read that as
     excluding markdown, found 23 non-ASCII characters in a master plan
     it was already patching, and reported them instead of fixing them.
     Tony overruled it: a patch already holding a file open fixes
     incidental non-ASCII, and Stamp What You Change is explicit that
     markdown is not an exception -- it is where that rule was earned.
     The gate now says so in its own words rather than leaving the
     reader to infer it from a neighbouring section.

  2. A CORRECTION DOES NOT TRAVEL TO THE PROSE DESCRIBING IT.
     New section, "The Correction Does Not Travel [QUALITY]",
     immediately after Stamp What You Change and scoped one level out
     from it. Stamp What You Change governs the file the patch is
     already editing. This governs the OTHER files that quote the value
     the patch just changed.

     Founding case, 2026-08-23: constants_new.py had said 15 R_sun
     since 2026-08-22 (L-209 corrected DeForest's figure from 17 at
     source). MASTER_PLAN_CRITICAL_PATH_SUMMARY.md still said 17 --
     inside the paragraph that file had written to correct an EARLIER
     wrong claim about the same row, in a document whose own text
     argues that a wrong claim in a summary outlives the conversation
     it came from. The same file also named a constant L-224 had
     renamed, and called a ledger item unbuilt that had gone DONE two
     days earlier.

     The provenance machinery watches the code. Nothing watched
     whether the documents describing the code kept up.

  3. Version line, cut-from SHA, date, and the v1.8 adds-paragraph.
  4. L-226 opened, because a skill revision is a ledger entry.

WHAT IS PERMANENT AND WHAT IS NOT
  The script is disposable. Skill v1.8 and L-226 are not.

AFTER RUNNING, IN THIS ORDER
  1. python skills_index.py
     Regenerates the Skill Manifest inside PROJECT_INSTRUCTIONS.md. The
     manifest still advertises 1.7 until this runs, and Stale Skill =
     Stop compares a loaded skill against the manifest -- so leaving
     this step is how a bump quietly half-lands.
  2. Settings > Skills: reinstall safe-file-editing (now 1.8).
  3. Commit and push SKILL.md, the ledger and PROJECT_INSTRUCTIONS.md
     together in ONE commit. The binding rule: a version bump is not
     done until the manifest agrees, and the three travel together.
  4. Move this script to documentation/.

CARRIED OBLIGATION FOR THE HANDOFF
  This bumps safe-file-editing to 1.8, and a mid-session reinstall
  cannot be verified from inside the session that makes it. The NEXT
  session confirms its loaded copy reads 1.8 before doing any
  file-editing work. This session loaded 1.7 and that was correct at
  the time.
"""

import hashlib
import os
import sys

BASE_SHA = '6d12ecace4c5867d4d718466c7ef5923fc47622e'
GALLERY_SHA = '02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))

SKILL = os.path.join('skills', 'safe-file-editing', 'SKILL.md')
LEDGER = 'LEDGER_CONSOLIDATED.md'

FINGERPRINTS = {
    SKILL: '63676a3a04ba9cc30e34a0e063fb53a5',
    LEDGER: '806f1c25257093a97567a38444315a59',
}


# ==================================================================
# EDIT 1 -- the version block
# ==================================================================

OLD_1 = (
    "Skill version: 1.7 | Cut from palomas_orrery @ d424c459 (v1.7),\n"
    "earlier @ ef3bd13 (v1.6), 50438c6 (v1.5), a872205 (v1.4), 1ba20c3\n"
    "(v1.3), 3398970 (v1.2), bdaaa0c (v1.1) | August 21, 2026, with\n"
    "Anthropic's Claude Opus 5\n"
)
NEW_1 = (
    "Skill version: 1.8 | Cut from palomas_orrery @ 6d12ecac (v1.8),\n"
    "earlier @ d424c459 (v1.7), ef3bd13 (v1.6), 50438c6 (v1.5), a872205\n"
    "(v1.4), 1ba20c3 (v1.3), 3398970 (v1.2), bdaaa0c (v1.1) | August 23,\n"
    "2026, with Anthropic's Claude Opus 5\n"
)


# ==================================================================
# EDIT 2 -- the adds-paragraph
# ==================================================================

OLD_2 = (
    "Is An Unverified Transfer (L-223), which extends the delivery rule to\n"
    "prose, markdown and ledger files -- every example in 1.6 was code, and\n"
    "this project had been hand-editing a 579 KB ledger on that silence.\n"
    "Portable: applies to any project, not only Paloma's Orrery.\n"
)
NEW_2 = (
    "Is An Unverified Transfer (L-223), which extends the delivery rule to\n"
    "prose, markdown and ledger files -- every example in 1.6 was code, and\n"
    "this project had been hand-editing a 579 KB ledger on that silence.\n"
    "v1.8 (L-226) does two things, both from Tony's rulings of 2026-08-23.\n"
    "It rescopes the Encoding Gate to say PROSE explicitly, because a\n"
    "session read \"delivered code\" as excluding markdown and left 23\n"
    "non-ASCII characters in a file it was already patching. And it adds\n"
    "The Correction Does Not Travel, one scope out from Stamp What You\n"
    "Change: that section governs the file the patch is editing, this one\n"
    "governs the other files quoting the value it just changed.\n"
    "Portable: applies to any project, not only Paloma's Orrery.\n"
)


# ==================================================================
# EDIT 3 -- the Encoding Gate says prose out loud
# ==================================================================

OLD_3 = (
    "## Encoding Gate [QUALITY]\n"
    "\n"
    "LF line endings. ASCII only in delivered code -- no emoji, arrows, degree\n"
    "signs, or checkmarks (Windows cp1252 consoles mangle them).\n"
    "\n"
    "```bash\n"
    "grep -P '[^\\x00-\\x7F]' filename.py   # Find non-ASCII (should be empty)\n"
    "file filename.py                      # Check line endings\n"
    "```\n"
)
NEW_3 = (
    "## Encoding Gate [QUALITY]\n"
    "\n"
    "LF line endings. ASCII only -- no emoji, arrows, degree signs, or\n"
    "checkmarks (Windows cp1252 consoles mangle them).\n"
    "\n"
    "**This covers PROSE, not only code.** Markdown, documentation, plans,\n"
    "handoffs and the ledger are all in scope, on the same terms as a .py\n"
    "file. Earlier wordings said \"delivered code\", and that phrasing was\n"
    "read as putting markdown outside the gate.\n"
    "\n"
    "```bash\n"
    "grep -P '[^\\x00-\\x7F]' filename.py   # Find non-ASCII (should be empty)\n"
    "file filename.py                      # Check line endings\n"
    "```\n"
    "\n"
    "(Tony's ruling, 2026-08-23. A patch revising a master plan found 22\n"
    "PRIME characters and one DOUBLE PRIME in an architecture name,\n"
    "reported them, and declined to sweep them -- reasoning that the gate\n"
    "was scoped to code and that prose typography needed a ruling rather\n"
    "than a sweep. All three Fix In Passing conditions held, and the patch\n"
    "was holding the fingerprint and the all-or-nothing harness at that\n"
    "exact moment. Tony: when touching a file, incidental non-ASCII gets\n"
    "fixed. Note that Stamp What You Change already said markdown is not an\n"
    "exception -- so the skill's two halves disagreed, and the reader\n"
    "followed the narrower one.)\n"
)


# ==================================================================
# EDIT 4 -- the new section, after Stamp What You Change
# ==================================================================

OLD_4 = (
    "(Origin: Tony's rule, 2026-08-20, from the observation that this project\n"
    "\"tends to update the body more than the anchors\" -- master plan headers,\n"
    "module histories and dates drift while their bodies stay current. The\n"
    "alternative considered and rejected was a generated currency stamp\n"
    "rebuilt by the maintenance run. It was rejected because it needs its own\n"
    "generator to maintain, while a stamp written by the patch that caused\n"
    "the staleness cannot drift: there is no second step to forget.)\n"
    "\n"
    "## grep -c in && Chains [QUALITY]\n"
)
NEW_4 = (
    "(Origin: Tony's rule, 2026-08-20, from the observation that this project\n"
    "\"tends to update the body more than the anchors\" -- master plan headers,\n"
    "module histories and dates drift while their bodies stay current. The\n"
    "alternative considered and rejected was a generated currency stamp\n"
    "rebuilt by the maintenance run. It was rejected because it needs its own\n"
    "generator to maintain, while a stamp written by the patch that caused\n"
    "the staleness cannot drift: there is no second step to forget.)\n"
    "\n"
    "### The Correction Does Not Travel [QUALITY]\n"
    "\n"
    "One scope out from Stamp What You Change. That section governs the\n"
    "file the patch is editing. This one governs the OTHER files that\n"
    "quote the value the patch just changed.\n"
    "\n"
    "**When you correct a value, a name, or a status in code, the prose\n"
    "describing it does not follow. Nobody is assigned to carry it.**\n"
    "\n"
    "The asymmetry is what makes this dangerous rather than merely untidy.\n"
    "A wrong value in code tends to surface -- something renders oddly, a\n"
    "test pins it, a checker reads it. A wrong value in a document that\n"
    "DESCRIBES the code surfaces only when a human reads that sentence and\n"
    "happens to know better. So the document version outlives the code\n"
    "version, and it is the one a future session reads first.\n"
    "\n"
    "So when a patch changes any of the following, ask what QUOTES it:\n"
    "- a numeric value with a source (the documents citing that source)\n"
    "- a constant's NAME (anything that told a reader to grep for it)\n"
    "- an item's STATUS (plans and summaries describing it as open)\n"
    "- a file's location or name (every pointer to it)\n"
    "\n"
    "Three moves, in the order they are usually available:\n"
    "- **Fix it in the same patch** where the quoting file is already a\n"
    "  target. Cheapest, and the only version with no second step.\n"
    "- **Name the quoting file in the patch's own output** where it is\n"
    "  not. \"constants_new.py now reads 15; MASTER_PLAN_CRITICAL_PATH_\n"
    "  SUMMARY.md still says 17\" is a line somebody can act on. Silence\n"
    "  is not.\n"
    "- **Record the correction VISIBLY when you do fix it**, rather than\n"
    "  swapping the digit. A document that silently rewrites its own past\n"
    "  stops being evidence of anything, and the next reader has nothing\n"
    "  to check it against.\n"
    "\n"
    "The confirming question is the project's own, pointed sideways:\n"
    "WHAT ELSE SAYS THIS? If the answer is \"nothing\" without having\n"
    "looked, that is not an answer.\n"
    "\n"
    "(Origin, 2026-08-23. `constants_new.py` had read 15 R_sun since\n"
    "2026-08-22, when L-209 corrected DeForest, Howard and McComas (2014)\n"
    "at source -- the paper's arXiv abstract page disagrees with the\n"
    "accepted manuscript arXiv itself serves, and two earlier reads had\n"
    "both quoted the listing page. `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`\n"
    "still said 17 the next day, INSIDE the paragraph that file had\n"
    "written to correct an earlier wrong claim about the same row, in a\n"
    "document whose own text argues that a wrong claim in a summary\n"
    "outlives the conversation it came from. The same file named\n"
    "`STREAMER_BELT_RADII`, which L-224 had renamed the day before, and\n"
    "called L-214 \"designed and unbuilt, and the next scheduled work\"\n"
    "two days after L-214 went DONE. Three instances, one file, one\n"
    "cause. The provenance machinery watches the code; nothing watched\n"
    "whether the documents describing the code kept up.)\n"
    "\n"
    "## grep -c in && Chains [QUALITY]\n"
)


# ==================================================================
# EDIT 5 -- L-226 in the ledger
# ==================================================================

OLD_5 = (
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)
NEW_5 = (
    "\n"
    "#### [L-226] safe-file-editing 1.8 -- encoding gate covers prose; "
    "corrections do not travel\n"
    "<!-- L:226 status:OPEN upd:2026-08-23 section:A flag: rice:3/3/90/1 -->\n"
    "- **Two rulings by Tony on 2026-08-23, both from the v19 master plan\n"
    "  session.** Recorded here because a skill revision is a ledger entry.\n"
    "- **1. The Encoding Gate now says PROSE.** It read \"ASCII only in\n"
    "  delivered code.\" `patch_L221_2` found 22 PRIME and one DOUBLE PRIME\n"
    "  in the master plan, reported them, and declined to sweep them on the\n"
    "  grounds that the gate was scoped to code. All three Fix In Passing\n"
    "  conditions held. Tony: a patch already holding a file open fixes\n"
    "  incidental non-ASCII. The sharper point is that Stamp What You\n"
    "  Change ALREADY said markdown is not an exception -- so the skill's\n"
    "  two halves disagreed and the reader followed the narrower one.\n"
    "  Swept in `patch_L221_3`; both master plan documents are now pure\n"
    "  ASCII.\n"
    "- **2. New section: The Correction Does Not Travel.** Scoped one level\n"
    "  out from Stamp What You Change -- that governs the file the patch is\n"
    "  editing, this governs the other files quoting what it changed.\n"
    "  Founding case: `constants_new.py` read 15 R_sun from 2026-08-22\n"
    "  (L-209, DeForest corrected at source);\n"
    "  `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` still said 17 the next day,\n"
    "  inside the paragraph written to correct an EARLIER wrong claim about\n"
    "  the same row. The same file named `STREAMER_BELT_RADII` after L-224\n"
    "  renamed it, and called L-214 unbuilt two days after it closed.\n"
    "  Three instances, one file, one cause: the provenance machinery\n"
    "  watches the code and nothing watched the documents describing it.\n"
    "- **Note:** RICE 3/3/90/1 -> 8.1 is Claude's proposed score. Reach 3\n"
    "  (every future patch), Impact 3 (a wrong document outlives a wrong\n"
    "  constant because nothing surfaces it), Confidence 90 (the rulings\n"
    "  are Tony's and the founding cases are measured), Effort 1 (the\n"
    "  skill edit is written). **Tony-action (decide):** confirm or\n"
    "  redirect, then re-run `ledger_index.py`.\n"
    "- **Tony-action (do):** run `skills_index.py`, then reinstall\n"
    "  safe-file-editing at Settings > Skills, then commit SKILL.md, this\n"
    "  ledger and PROJECT_INSTRUCTIONS.md in ONE commit. A version bump is\n"
    "  not done until the manifest agrees.\n"
    "- **Gap:** the reinstall cannot be verified from inside the session\n"
    "  that makes it. The NEXT session confirms its loaded copy reads 1.8\n"
    "  before doing file-editing work. This session loaded 1.7, correctly\n"
    "  at the time.\n"
    "- **Ref:** `skills/safe-file-editing/SKILL.md` v1.8;\n"
    "  `documentation/HANDOFF_20260823_braid_and_v19.md`; L-209 (the\n"
    "  DeForest figure); L-214, L-224 (the other two stale claims);\n"
    "  L-220 (Stamp What You Change); L-223 (A Paste Is An Unverified\n"
    "  Transfer).\n"
    "\n"
    "## PENDING ACTION (Tony-side)\n"
)


# ==================================================================
# EDIT 6 -- ledger currency stamp
# ==================================================================

OLD_6 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-154\n"
    "BLOCKED -> OPEN under the braid; L-225 opened, having been in\n"
    "circulation with no entry), built on ce2ff5d1.\n"
)
NEW_6 = (
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-154\n"
    "BLOCKED -> OPEN under the braid; L-225 opened, having been in\n"
    "circulation with no entry), built on ce2ff5d1.\n"
    "Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-226:\n"
    "safe-file-editing 1.7 -> 1.8), built on 6d12ecac.\n"
)


EDITS = [
    (SKILL, '1 version line 1.7 -> 1.8', OLD_1, NEW_1),
    (SKILL, '2 adds-paragraph for v1.8', OLD_2, NEW_2),
    (SKILL, '3 Encoding Gate covers prose', OLD_3, NEW_3),
    (SKILL, '4 new: The Correction Does Not Travel', OLD_4, NEW_4),
    (LEDGER, '5 L-226 opened', OLD_5, NEW_5),
    (LEDGER, '6 ledger currency stamp', OLD_6, NEW_6),
]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. BOTH files on disk are untouched.')
    sys.exit(1)


def main():
    print('patch_L221_6_safe_file_editing_1_8.py')
    print('built on %s' % BASE_SHA)
    print('gallery  %s' % GALLERY_SHA)
    print('')

    paths, originals, endings = {}, {}, {}
    for name in (SKILL, LEDGER):
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            fail('%s not found relative to this script.\n'
                 '       This one goes in the REPO ROOT -- the folder with\n'
                 '       LEDGER_CONSOLIDATED.md, skills_index.py and the\n'
                 '       skills/ folder.\n'
                 '       It looked in: %s' % (name, HERE))
        paths[name] = path
        with open(path, 'rb') as handle:
            originals[name] = handle.read()

    for name in (SKILL, LEDGER):
        normalized = originals[name].replace(b'\r\n', b'\n')
        got = hashlib.md5(normalized).hexdigest()
        if got != FINGERPRINTS[name]:
            fail('BASE MOVED. %s fingerprints %s; this patch was built '
                 'against %s. Re-pull at HEAD, or ask for a rebuilt patch.'
                 % (name, got, FINGERPRINTS[name]))
        endings[name] = b'\r\n' if b'\r\n' in originals[name] else b'\n'
        print('[base ok]      %-36s %s (%s)'
              % (name, got, 'CRLF' if endings[name] == b'\r\n' else 'LF'))

    # --- ASCII, both directions -- the very rule being added ---------
    for _name, label, old, new in EDITS:
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
               for n in (SKILL, LEDGER)}

    # --- A check that can fail: L-226 must not already exist ---------
    if '<!-- L:226 ' in working[LEDGER]:
        fail('L-226 already has an index comment. This patch would create '
             'a duplicate handle.')
    print('[handle ok]     L-226 is absent, as expected')

    for name, label, old, new in EDITS:
        count = working[name].count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected exactly 1 match, found '
                 '%d. First 70 chars: %r' % (label, count, old[:70]))
        working[name] = working[name].replace(old, new, 1)
        print('[ok]            %s' % label)

    # --- Pure addition, except the two lines each edit rewrites ------
    for name in (SKILL, LEDGER):
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
                 'rewrite. First: %r' % (len(unexpected), name,
                                         unexpected[0]))
        print('[addition ok]   %-36s %d line(s) rewritten, all accounted for'
              % (name, len(lost)))

    # --- Evidence the version actually moved ------------------------
    if 'Skill version: 1.8' not in working[SKILL]:
        fail('the version line did not land as 1.8.')
    if 'Skill version: 1.7' in working[SKILL]:
        fail('a 1.7 version line survives in the skill.')
    print('[version ok]    SKILL.md now declares 1.8, and no 1.7 line '
          'survives')

    for name in (SKILL, LEDGER):
        out = working[name].encode('ascii')
        if endings[name] == b'\r\n':
            out = out.replace(b'\n', b'\r\n')
        with open(paths[name], 'wb') as handle:
            handle.write(out)
        print('[written]       %-36s %d -> %d bytes'
              % (name, len(originals[name]), len(out)))

    print('')
    print('patch applied -- %d edits across 2 files' % len(EDITS))
    print('')
    print('CURRENCY STAMPS UPDATED (Stamp What You Change):')
    print('  SKILL.md    version 1.7 -> 1.8, cut-from SHA %s, date,'
          % BASE_SHA[:8])
    print('              and the v1.8 adds-paragraph')
    print('  LEDGER      new "Module updated" line, %s' % MODEL)
    print('')
    print('NEXT, IN THIS ORDER -- the bump is not done until step 1 runs:')
    print('  1. python skills_index.py')
    print('     The manifest in PROJECT_INSTRUCTIONS.md still advertises')
    print('     1.7. Stale Skill = Stop compares a loaded skill against')
    print('     THAT manifest, so skipping this half-lands the bump.')
    print('  2. Settings > Skills: reinstall safe-file-editing (now 1.8).')
    print('  3. Commit SKILL.md + LEDGER_CONSOLIDATED.md +')
    print('     PROJECT_INSTRUCTIONS.md in ONE commit, then push.')
    print('  4. Move this script to documentation/.')
    print('')
    print('CARRIED OBLIGATION for the handoff:')
    print('  safe-file-editing goes to 1.8 at this SHA. The session that')
    print('  bumped it loaded 1.7. A mid-session reinstall cannot be')
    print('  verified from inside the session that makes it, so the NEXT')
    print('  session confirms its loaded copy reads 1.8 before doing any')
    print('  file-editing work.')
    print('')
    print('OPEN FOR TONY:')
    print('  - L-226 carries a PROPOSED RICE of 3/3/90/1 (score 8.1).')
    print('    Confirm or redirect, then re-run ledger_index.py.')


if __name__ == '__main__':
    main()
