"""
patch_skills_prov18_cache13.py

Two skill updates, both content changes that earn a version bump.

  provenance-discipline  1.7 -> 1.8
  gallery-cache-builder  1.2 -> 1.3

WHAT CHANGES

provenance-discipline gets two additions, both from the August 10 session.

  1. WORKSHEET FIRST, ANNOTATION SECOND. A new rule under the Cross-Checked
     Annotation Format: if no worksheet file exists on disk, the annotation
     does not get written. Save the exchange as a .md first, then annotate
     against the real filename. The parenthetical in a Cross-checked line
     is a file path, and a path that resolves to nothing is cite-to-clear
     wearing the annotation format.

  2. A field note: an evidence artifact is filed AS RECEIVED. House ASCII
     rules and naming conventions apply to code and to documents we author,
     not to a document whose whole value is that someone else wrote it.
     This one cost a real citation's credibility -- the detail is in the
     note.

gallery-cache-builder gets the scheduler retirement, which makes one of its
existing statements false.

  3. The ABORT disposition says Task Scheduler history is the monitoring
     channel. As of August 10 there is no scheduler, so there is no
     monitoring channel at all -- the nonzero exit now surfaces in the
     console Tony is watching, because he started the run.

  4. Layer 3 of the testing protocol is marked RETIRED rather than deleted,
     with the conditions that would bring it back.

  5. The version line and the header sentence get the same treatment: the
     builder is described as manually run, not nightly.

Target files: skills/provenance-discipline/SKILL.md
              skills/gallery-cache-builder/SKILL.md
Built on 8e4b5ca447ea93af7ee54b0810564e146e5bb57b

HOW TO RUN
  Save this file in the ORRERY REPO ROOT (the folder that contains the
  skills/ directory), open it in VS Code, and click Run.

  Or from a terminal in that folder:
      python patch_skills_prov18_cache13.py

WHAT SUCCESS LOOKS LIKE
  One "ok" line per edit, then "patch applied" naming both files.

WHAT FAILURE LOOKS LIKE
  A single line beginning "ERROR:" or "ANCHOR FAIL:". NEITHER file is
  written if either one fails its checks -- both files are validated
  before anything is written, so a half-applied state is not possible.

AFTERWARD -- THREE STORES, AND THIS ONLY MOVES ONE
  A skill lives in the repo, in your account install, and in the protocol's
  manifest table. This patch edits the repo copy only. To finish:

    1. Run skills_index.py. It rewrites the manifest table in
       PROJECT_INSTRUCTIONS.md and prints what the table said before, so
       you can see the 1.7 -> 1.8 and 1.2 -> 1.3 move.
    2. Reinstall both skills to your account (Settings > Skills).

  Until step 2, a session that loads provenance-discipline gets 1.7 while
  the manifest advertises 1.8, and Stale Skill = Stop will halt it. That
  halt is the gate working, not a bug.
"""

import hashlib
import os
import sys

PROV = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
CACHE = os.path.join('skills', 'gallery-cache-builder', 'SKILL.md')

PROV_MD5 = '1241d4daa47ee7030f039eb186c94ee2'
CACHE_MD5 = '6bcbc84a2c2ef8223955afbbd7ecb2fd'

# ==================================================================
# provenance-discipline 1.7 -> 1.8
# ==================================================================

PROV_EDITS = []

# --- version line ---
PROV_EDITS.append((
    'version line',
    """shell-consistency audit, August 3-4, 2026.
""",
    """shell-consistency audit, August 3-4, 2026. v1.8 adds Worksheet First,
Annotation Second (an annotation naming a worksheet that does not exist
is cite-to-clear in the annotation's own format) and the field note that
an evidence artifact is filed as received -- both earned August 10, 2026,
when a recovered worksheet proved an annotation true that the session had
already talked itself into calling fabricated.
"""))

PROV_EDITS.append((
    'skill version number',
    "Skill version: 1.7 | Cut from palomas_orrery @ 3398970 | August 5, 2026",
    "Skill version: 1.8 | Cut from palomas_orrery @ 8e4b5ca (v1.8), earlier\n@ 3398970 (v1.7) | August 11, 2026"))

# --- new rule, placed right after the annotation format explanation ---
PROV_EDITS.append((
    'Worksheet First rule',
    """**Source leads, model is subordinate, worksheet is the audit trail.**
The source names the authority. The model names who found it. The
parenthetical worksheet reference points to the evidence on disk. The
ISO date is the check date, not the publication date.
""",
    """**Source leads, model is subordinate, worksheet is the audit trail.**
The source names the authority. The model names who found it. The
parenthetical worksheet reference points to the evidence on disk. The
ISO date is the check date, not the publication date.

#### Worksheet First, Annotation Second [CRITICAL]

If no worksheet file exists on disk, the annotation does not get written.
Save the exchange as a `.md` in `documentation/` first, then write the
annotation against the real filename.

The parenthetical is a PATH, and a path that resolves to nothing asserts
an audit trail that cannot be walked. That is cite-to-clear wearing the
annotation format -- and it is worse than a bare `# Source:` line,
because the annotation's whole promise is that the evidence is on disk.

Two failure shapes, and they need different fixes:
- The check happened but was never filed. Recoverable: find the exchange,
  file it as received, repoint the annotation. Eight annotations in
  `constants_new.py` were in this state and were repaired on August 10
  once Tony recovered the worksheet.
- The check never happened. Not recoverable by filing anything. Strip the
  annotation, and re-run the claim through the workflow.

Do not write the annotation planning to file the worksheet afterwards.
The gap between the two is where the first shape comes from."""))

# --- field note ---
PROV_EDITS.append((
    'evidence-as-received field note',
    """## Field Notes

- **Three wrong-paper citations survived into Batch 1 files**,""",
    """## Field Notes

- **An evidence artifact is filed AS RECEIVED.** House style -- ASCII
  rules, naming conventions, header blocks -- applies to code and to
  documents we author. It does NOT apply to a document whose entire value
  is that someone else wrote it. A session took Tony's uploaded Gemini
  worksheet, converted its LaTeX to ASCII, stripped the markdown escaping,
  added a header block and a provenance note it wrote itself, and filed
  the result labelled as the Gemini worksheet. Tony caught it: "you have
  created a parallel unsourced worksheet not made by gemini." The corpus
  settled the question -- the existing GPT worksheet carries 115
  non-ASCII bytes and the earlier Gemini one 37, so there was no
  consistency to fix, only an assumed one. Reformatting an evidence file
  destroys the property that makes it evidence.
- **Unverified and true is still unverified -- do not over-confess.** Asked
  whether it had fabricated a `(Gemini worksheet)` annotation, a session
  gave an accurate account of its method (it had pattern-matched an
  adjacent annotation's shape without checking), then concluded from that
  the CONTENT was fabricated, called it cite-to-clear, and offered to
  strip the annotation. The recovered worksheet proved all three
  specifics it believed it had invented were true. Acting on the
  self-report would have deleted a real citation. Separate the two
  findings: the METHOD was wrong and is worth fixing; whether the CONTENT
  is wrong is a different question with its own evidence. An
  over-confession is as much a calibration failure as a denial, and it is
  more persuasive because it sounds like rigor.
- **Three wrong-paper citations survived into Batch 1 files**,"""))

# ==================================================================
# gallery-cache-builder 1.2 -> 1.3
# ==================================================================

CACHE_EDITS = []

CACHE_EDITS.append((
    'skill version number',
    "Skill version: 1.2 | Cut from tonyquintanilla.github.io @ a08bdd10 (code) and palomas_orrery @ 3398970 (context) | 2026-08-05",
    "Skill version: 1.3 | Cut from tonyquintanilla.github.io @ 02d7163 (code) and palomas_orrery @ 8e4b5ca (context) | 2026-08-11"))

CACHE_EDITS.append((
    'header sentence',
    """The standalone nightly builder that fetches fresh JPL Horizons data and deploys
the web gallery's served cache.""",
    """The standalone builder that fetches fresh JPL Horizons data and deploys the
web gallery's served cache. Tony runs it MANUALLY and commits the result
himself; the scheduled nightly was retired August 10, 2026 (see Operating
mode below).

## Operating mode -- manual, as of August 10 2026

The Windows scheduled task is DISABLED, not deleted. Tony's ruling: "It
can't run without my machine being on anyway and it's consistent with me
being the only commit authority. And obviates complicated fail safe
procedures that could also fail."

What this means in practice:
- The builder is launched from the dashboard's Developer Tools group, or
  by running `tools/gallery_cache_builder.py` from the GALLERY REPO ROOT.
  The root matters: `--config` and `--output-dir` default to paths
  relative to the working directory, so launching from `tools/` fails at
  load_config.
- No flags runs nightly mode. `--commit` is NOT passed, so the builder
  swaps the new cache in and stops. Tony commits in GitHub Desktop.
- Because Tony starts the run, he knows a build is in flight. This is the
  substantive safety change: the atomic swap's window shows deletions only
  in a git client, and on August 10 that was committed by mistake by
  someone who did not know a build was running.
- A `pre-commit` hook refusing a deletion-only commit under
  `data/solar-system/` was designed and is deliberately NOT built. It
  becomes relevant again if the schedule returns, if a second person gains
  commit access to the gallery repo, or if the builder ever runs
  unattended in any other form.

The cadence question did not go away, it changed shape. "Did the nightly
run?" became "when did I last run it?" -- and a manual build has no
expected time at all, so an explicit staleness check is now the ONLY thing
that can report that the served data is eleven days old. That is L-189."""))

CACHE_EDITS.append((
    'ABORT monitoring channel',
    """- ABORT (raise ValidationAbort -> nonzero exit; Task Scheduler history is the
  monitoring channel): structural invariants (#2/#3/#C/#8), #B3""",
    """- ABORT (raise ValidationAbort -> nonzero exit; the nonzero exit surfaces in
  the console Tony is watching, since he starts the run -- through 2026-08-10
  this read "Task Scheduler history is the monitoring channel," which was
  true until the schedule was retired and is now the note to fix if the
  schedule ever returns): structural invariants (#2/#3/#C/#8), #B3"""))

CACHE_EDITS.append((
    'Layer 3 retirement',
    """- Layer 3 -- scheduling (unattended nightly). Correctness/operability items
  gate this (gap-aware catch-up, a health summary) -- see L-098 / L-111.""",
    """- Layer 3 -- scheduling (unattended nightly). RETIRED 2026-08-10; the task
  is disabled, not deleted. The layer is kept here because it becomes live
  again the moment the build runs unattended by any mechanism, including a
  GitHub Action. Its gating items are unchanged (gap-aware catch-up, a
  health summary) -- see L-098 / L-111."""))

FILES = [
    (PROV, PROV_MD5, PROV_EDITS, 'provenance-discipline 1.7 -> 1.8'),
    (CACHE, CACHE_MD5, CACHE_EDITS, 'gallery-cache-builder 1.2 -> 1.3'),
]


def main():
    here = os.path.dirname(os.path.abspath(__file__))

    if not os.path.isdir(os.path.join(here, 'skills')):
        print("ERROR: no skills/ folder here. Put this script in the orrery")
        print("       repo root (the folder holding skills/) and run again.")
        return 1

    staged = []

    # ---- validate EVERYTHING before writing ANYTHING ----
    for rel, want_md5, edits, label in FILES:
        path = os.path.join(here, rel)
        if not os.path.exists(path):
            print("ERROR: " + rel + " not found. Nothing was written.")
            return 1

        with open(path, 'rb') as f:
            data = f.read()

        fp = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if fp != want_md5:
            print("ERROR: base moved for " + rel + ".")
            print("       Expected " + want_md5 + ",")
            print("       found " + fp + ". Nothing was written.")
            return 1

        text = data.decode('utf-8')
        crlf = '\r\n' in text
        if crlf:
            text = text.replace('\r\n', '\n')

        for name, old, new in edits:
            n = text.count(old)
            if n != 1:
                print("ANCHOR FAIL: " + label + " / " + name)
                print("             expected 1 match, found " + str(n) + ".")
                print("             Nothing was written to either file.")
                return 1
            text = text.replace(old, new)

        if sum(1 for ch in text if ord(ch) > 127):
            print("ANCHOR FAIL: " + rel + " would contain non-ASCII.")
            print("             Nothing was written.")
            return 1

        if crlf:
            text = text.replace('\n', '\r\n')
        staged.append((path, text.encode('ascii'), edits, label))

    # ---- all checks passed; write ----
    for path, blob, edits, label in staged:
        with open(path, 'wb') as f:
            f.write(blob)
        for name, _o, _n in edits:
            print("ok   " + label.split(' ')[0] + ": " + name)

    print("")
    print("patch applied -- both SKILL.md files updated.")
    print("")
    print("Now do BOTH of these, or the next session will halt on")
    print("Stale Skill = Stop:")
    print("  1. Run skills_index.py (rewrites the manifest in the protocol)")
    print("  2. Reinstall both skills in Settings > Skills")
    return 0


if __name__ == '__main__':
    sys.exit(main())
