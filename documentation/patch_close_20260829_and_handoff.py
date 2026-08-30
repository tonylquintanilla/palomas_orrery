"""
patch_close_20260829_and_handoff.py

Closes the three ledger items whose fixes are now committed, and writes
the session handoff.

Built on orrery `bfa9de2fc0b9c2d30c9eb4de27828a8c2b4c8535` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `6c6123974e883a461a92b586b8352c9c535ee8d1` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote 2026-08-29.

FIVE files: four are edited under guards and one handoff is created.
Every guard and every anchor is checked before anything is written.


WHAT IT WRITES

  1. L-236 -> DONE. The gallery runner is committed and running; the
     serving-reachability and store-drift checks both pass live. Gains
     the CRLF-comparison defect its own first live runs surfaced.

  2. L-263 -> DONE. The chromosphere value is committed, and the drift
     check re-run against the live site reads 26 match, 0 DRIFT.

  3. L-260 stays OPEN, because the phone is untouched. Its axis half is
     closed and Mode 5 confirmed, and the stranded marker Tony was asked
     to check is recorded as NOT a defect so nobody re-raises it.

  4. safe-file-editing 1.8 -> 1.9: Compare Content, Not Bytes [QUALITY].
     Across a Windows working copy, compare the LF-normalised content and
     never the raw bytes, write each file back in the style it was found
     in, and say when normalising was what saved it.

  5. Protocol v3.48 recording that bump, IN THE SAME COMMIT. v3.45 moves
     down into the history file -- lifted by its own boundaries rather
     than retyped, so the moved entry cannot differ from the resident
     one.

  6. documentation/HANDOFF_20260829_night_sun_finished.md -- the session
     record.

Both items move to section C by their own status tags; ledger_index.py
migrates the blocks.


THE ONE STEP THIS PATCH CANNOT TAKE

A skill lives in three stores and the account install is the copy Claude
actually loads. Reinstalling it is Tony's, in Settings > Skills, and a
mid-session reinstall is invisible to the running conversation anyway.
So the handoff carries the obligation in writing: the next session
confirms its loaded copy reads 1.9 before doing patch work.

This patch itself obeys the rule it installs -- every guard below is
computed on LF-normalised content, and every file is written back in the
line-ending style it was found in.


AFTER RUNNING IT

  1. ledger_index.py            -- regenerates the index, migrates
                                   L-236 and L-263 to section C
  2. orrery_maintenance_run.py  -- should stay 11 of 11

Then commit.


HOW TO RUN IT

Drop this file into the ORRERY repo root and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"
PROBE = "constants_new.py"

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "5800cb87acc1059355e628b247cf44f4"

HANDOFF = os.path.join("documentation",
                       "HANDOFF_20260829_night_sun_finished.md")

SKILL = os.path.join("skills", "safe-file-editing", "SKILL.md")
SKILL_MD5 = "3715be64787b2c4f7a883b02bc189a64"

PROTO = "PROJECT_INSTRUCTIONS.md"
# PROJECT_INSTRUCTIONS.md is guarded on its POST-v3.47 content, which
# is what the earlier patch left and what HEAD now carries.
PROTO_MD5 = "30a1ed7367321324137961e3e4415313"

HISTORY = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
HISTORY_MD5 = "13acf75514683327760e5cf798cb3939"


EDITS = [
    (
        "L-236 closes, and gains the defect its own live runs found",

        "#### [L-236] Gallery maintenance runner [designed, unbuilt]\n"
        "<!-- L:236 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/80/4 -->\n",

        "#### [L-236] Gallery maintenance runner\n"
        "<!-- L:236 status:DONE upd:2026-08-29 section:C flag: rice:4/4/80/4 -->\n",
    ),
    (
        "L-236's Gap becomes its closing record",

        "**Gap:** built and delivered, not yet committed. **Tony-action\n"
        "(do):** commit `maintenance_run.py` to the gallery repo root; this\n"
        "item closes on that commit. Left OPEN rather than marked DONE in\n"
        "advance, because a ledger row claiming a file is committed before\n"
        "it is committed is a claim nothing can check.\n",

        "- **A defect in it, found by its own first two live runs.** The\n"
        "  served-reachability check compared the site's bytes against the\n"
        "  working copy's bytes, and reported `coverage_index.json` and\n"
        "  `feature_configs.json` stale on every run while everything else\n"
        "  matched -- including `interactive.html`, freshly pushed, which\n"
        "  proved the deploy was current. `gallery_cache_builder.py` writes\n"
        "  both with `open(path, 'w')`, so on Windows they land CRLF in the\n"
        "  working copy; `.gitattributes` carries `* text=auto eol=lf`, so\n"
        "  git stores LF and Pages serves LF. Identical content, and the\n"
        "  check was calling a correct deploy stale -- crying wolf on the\n"
        "  one check whose whole value is being believed.\n"
        "- **Why it shipped that way, which is the part worth keeping.**\n"
        "  The same line-ending fault made the first ledger patch refuse to\n"
        "  run a few hours earlier the same day. It was diagnosed and fixed\n"
        "  in the patch scripts and never carried to the runner, which had\n"
        "  already been written. One producer, two consumers, one of them\n"
        "  moved: Check All Parallel Pipelines, and L-182's shape.\n"
        "- **Fixed 2026-08-29** at gallery `6c612397`. The comparison reads\n"
        "  content, and a CRLF-only difference still says so on its row --\n"
        "  \"matches (the working copy is CRLF)\" -- rather than being\n"
        "  swallowed. Mutation-tested both ways before delivery: a\n"
        "  one-word content difference still reports NOT YET DEPLOYED, and\n"
        "  a 404 on the `.py` files while the page returns 200 still\n"
        "  reports FAIL.\n"
        "- **The portable rule is owed to a skill, not to this row.**\n"
        "  Across a Windows working copy, compare CONTENT, never raw bytes.\n"
        "  It belongs in safe-file-editing, which is a bump and therefore a\n"
        "  four-step binding-rule obligation. **Tony-action (do):** not\n"
        "  done in this pass; carried in the 2026-08-29 night handoff.\n"
        "**Closed 2026-08-29.** Built, committed at gallery `ae410c29`,\n"
        "renamed `gallery_maintenance_run.py` under L-264, and both live\n"
        "checks pass against the deployed site: served reachability 7 of 7,\n"
        "store drift 30 pointers with 26 match and 0 DRIFT.\n",
    ),
    (
        "L-263 closes on a verified re-run",

        "#### [L-263] The served chromosphere value is a rounded copy\n"
        "<!-- L:263 status:OPEN upd:2026-08-29 section:A flag: rice:2/3/95/1 -->\n",

        "#### [L-263] The served chromosphere value is a rounded copy\n"
        "<!-- L:263 status:DONE upd:2026-08-29 section:C flag: rice:2/3/95/1 -->\n",
    ),
    (
        "L-263's Gap becomes its closing record",

        "**Gap:** delivered, not yet committed. Closes on the gallery\n"
        "commit.\n",

        "**Closed 2026-08-29** at gallery `6c612397`. The value is\n"
        "1.002874802357338, and the drift check re-run against the LIVE\n"
        "site -- not against a local copy -- reports 26 match, 0 DRIFT,\n"
        "where it read 25 and 1 before. The corrected figure is visible in\n"
        "the exhibit's own hover with its citation, which is the first time\n"
        "a provenance correction in this project has been readable by a\n"
        "visitor.\n",
    ),
    (
        "L-260's axis half closes; the phone stays open; the marker is cleared",

        "**Gap:** the phone. The axis half is delivered and closes on the\n"
        "gallery commit; the phone read is Mode 5 and is Tony's.\n",

        "- **Axis half CLOSED 2026-08-29** at gallery `6c612397`, Mode 5\n"
        "  confirmed by Tony against the deployed page: the axes read\n"
        "  X (AU), Y (AU), Z (AU).\n"
        "- **A suspected tenth orphan marker, checked and cleared.** A red\n"
        "  cross appeared in Tony's 2026-08-29 screenshot below and right\n"
        "  of the corona, with no shell around it, and was raised as a\n"
        "  possible survivor of the nine-marker orphan fix. Tony checked\n"
        "  it on the live page: not a defect. Recorded so it is not\n"
        "  re-raised from the same screenshot later.\n"
        "- **The phone check happened, 2026-08-29**, on iPhone Safari, both\n"
        "  orientations. **The exhibit WORKS**: Pyodide loaded, the\n"
        "  assembler ran, the shells drew, the axis titles are there. The\n"
        "  premise of the whole interactive gallery -- that it works on a\n"
        "  phone -- held on its first real test.\n"
        "- **LANDSCAPE is usable as it stands.** The legend takes roughly a\n"
        "  quarter of the width, scrolls (11 of 18 entries visible with a\n"
        "  scrollbar), and the Sun renders clear of it.\n"
        "- **PORTRAIT is not.** The legend covers about 58 percent of the\n"
        "  width and 58 percent of the height as an overlay, and the Sun\n"
        "  sits BEHIND it -- the object of the exhibit is the part you\n"
        "  cannot see. All 18 entries render at once rather than scrolling\n"
        "  as they do in landscape.\n"
        "- **The axis titles clip in portrait.** Only fragments of the\n"
        "  X (AU) and Y (AU) labels reach the viewport at the bottom\n"
        "  corners. They are correct and they are cut off, which is a\n"
        "  narrower problem than the legend and probably the same fix.\n"
        "- **Not diagnosed, deliberately.** These are read from two\n"
        "  screenshots, not from the page. gallery-pipeline 1.2 carries the\n"
        "  768 px breakpoint and a bottom-drawer pattern for exactly this\n"
        "  case, and the Sun exhibit does not use it. Whether that is the\n"
        "  fix is a design conversation, not a guess to be made here.\n"
        "**Gap:** portrait. The legend overlays the object it describes,\n"
        "and the axis titles clip. Landscape needs nothing. Deferred by\n"
        "Tony to the next session, 2026-08-29.\n",
    ),
]


SKILL_EDITS = [
    (
        "safe-file-editing 1.8 -> 1.9",

        "Skill version: 1.8 | Cut from palomas_orrery @ 6d12ecac (v1.8),\n"
        "earlier @ d424c459 (v1.7), ef3bd13 (v1.6), 50438c6 (v1.5), a872205\n"
        "(v1.4), 1ba20c3 (v1.3), 3398970 (v1.2), bdaaa0c (v1.1) | August 23,\n"
        "2026, with Anthropic's Claude Opus 5\n",

        "Skill version: 1.9 | Cut from palomas_orrery @ bfa9de2f (v1.9),\n"
        "earlier @ 6d12ecac (v1.8), d424c459 (v1.7), ef3bd13 (v1.6),\n"
        "50438c6 (v1.5), a872205 (v1.4), 1ba20c3 (v1.3), 3398970 (v1.2),\n"
        "bdaaa0c (v1.1) | August 29, 2026, with Anthropic's Claude Opus 5\n",
    ),
    (
        "the new section: compare content, not bytes",

        "## grep -c in && Chains [QUALITY]\n",

        "## Compare Content, Not Bytes [QUALITY]\n"
        "\n"
        "A guard, a diff or a reachability check that compares RAW BYTES\n"
        "across a Windows working copy will refuse or cry wolf on files\n"
        "nobody has changed. Compare the LF-normalised content instead, and\n"
        "write each file back in the line-ending style you found it in.\n"
        "\n"
        "```python\n"
        "raw = open(path, \"rb\").read()\n"
        "was_crlf = b\"\\r\\n\" in raw\n"
        "content = raw.replace(b\"\\r\\n\", b\"\\n\") if was_crlf else raw\n"
        "actual = hashlib.md5(content).hexdigest()      # guard on THIS\n"
        "...\n"
        "final = out.replace(b\"\\n\", b\"\\r\\n\") if was_crlf else out\n"
        "```\n"
        "\n"
        "**Why the two copies legitimately differ.** Any tool that writes in\n"
        "TEXT mode on Windows -- `open(path, 'w')` -- turns every \\n into\n"
        "\\r\\n. Git normalises it back on commit, especially under a\n"
        "`* text=auto eol=lf` .gitattributes. So the repository holds LF, a\n"
        "static host serves LF, and the working copy holds CRLF, with not\n"
        "one character different between them. Nobody did anything wrong and\n"
        "the byte comparison is simply asking the wrong question.\n"
        "\n"
        "**Say when normalisation was what saved it.** Print `[CRLF]` beside\n"
        "a guard that matched only after normalising, and say \"matches (the\n"
        "working copy is CRLF)\" on a row rather than a bare match. Silently\n"
        "swallowing the difference trades a false alarm for a blind spot,\n"
        "which is the worse of the two.\n"
        "\n"
        "**Preserve the style on write.** Flipping a 700 KB file's line\n"
        "endings shows in a git GUI as every line changed, which buries the\n"
        "eight edits that actually matter. This half is not cosmetic: a diff\n"
        "nobody can read is a diff nobody reviews.\n"
        "\n"
        "**[QUALITY] rather than [CRITICAL], deliberately.** Both failure\n"
        "directions are LOUD -- a guard refuses, or a check reports stale --\n"
        "so nothing is silently corrupted and nothing passes that should\n"
        "not. What it costs is trust in the check, which is why it is worth\n"
        "a section at all. The critical tier stays short.\n"
        "\n"
        "(Two instances, one day, August 29 2026. A four-file patch refused\n"
        "to run because `ledger_index.py` had left LEDGER_CONSOLIDATED.md\n"
        "CRLF in the working copy; the md5 was reproduced exactly by\n"
        "converting the repo copy, proving not one character differed. Then\n"
        "the gallery maintenance runner reported two served files stale on\n"
        "every live run, because `gallery_cache_builder.py` writes\n"
        "coverage_index.json and feature_configs.json in text mode. The\n"
        "second is the lesson: the first had already been diagnosed and\n"
        "fixed in the patch scripts hours earlier, and was not carried to\n"
        "the runner that had already been written. One producer, two\n"
        "consumers, one of them moved -- Check All Parallel Pipelines, and\n"
        "L-182's shape. L-236.)\n"
        "\n"
        "## grep -c in && Chains [QUALITY]\n",
    ),
]

V348 = (
    "v3.48 (August 29, 2026): No rule changed in this document. One skill\n"
    "bump, recorded in the same commit that made it -- which is the whole\n"
    "of the improvement over this morning.\n"
    "\n"
    "safe-file-editing 1.8 -> 1.9 (L-236). Compare Content, Not Bytes\n"
    "[QUALITY]. A guard or a check that compares RAW BYTES across a\n"
    "Windows working copy refuses, or cries wolf, on files nobody has\n"
    "changed: any tool writing in text mode leaves CRLF behind, git\n"
    "normalises it back to LF on commit, and the two copies then differ\n"
    "byte-for-byte while agreeing on every character. Compare the\n"
    "LF-normalised content, write each file back in the style it was\n"
    "found in, and SAY when normalisation was what saved it.\n"
    "\n"
    "Two instances in one day earned it. A four-file patch refused\n"
    "because ledger_index.py had left the ledger CRLF; the md5 was\n"
    "reproduced exactly by converting the repo copy, which proved the\n"
    "content was identical. Then the new gallery runner called a correct\n"
    "deploy stale for the same reason. The second is the lesson: the\n"
    "first had been diagnosed and fixed in the patch scripts hours\n"
    "earlier and was not carried to the runner already written. One\n"
    "producer, two consumers, one of them moved.\n"
    "\n"
    "Kept at [QUALITY] on purpose. Both failure directions are loud, so\n"
    "nothing is silently corrupted and nothing passes that should not;\n"
    "what it costs is trust in the check. The critical tier stays short.\n"
    "\n"
    "One obligation this bump cannot discharge from inside the session\n"
    "that made it. A skill lives in three stores, and the account install\n"
    "is the copy Claude actually loads; a reinstall is invisible to the\n"
    "running conversation. So: safe-file-editing went to 1.9 at\n"
    "`bfa9de2f`, the session that bumped it had loaded 1.8, and the next\n"
    "session confirms its loaded copy reads 1.9 before doing patch work.\n"
    "\n"
    "Version history: v3.45 moves down to\n"
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n"
    "resident.\n"
    "\n"
)

PROTO_EDITS = [
    (
        "header to v3.48, anchored at bfa9de2f",

        "Tony Quintanilla, PE | Claude | v3.47 | August 29, 2026\n"
        "\n"
        "Cut from 8b762e04 at https://github.com/tonylquintanilla/palomas_orrery\n",

        "Tony Quintanilla, PE | Claude | v3.48 | August 29, 2026\n"
        "\n"
        "Cut from bfa9de2f at https://github.com/tonylquintanilla/palomas_orrery\n",
    ),
    (
        "the v3.48 entry, newest first",

        "v3.47 (August 29, 2026): One rule amended, and one skill bump\n",

        V348 + "v3.47 (August 29, 2026): One rule amended, and one skill bump\n",
    ),
]

# v3.45 is LIFTED by its own boundaries, not retyped, so the moved entry
# cannot differ from the resident one.
V345_START = "v3.45 (August 27, 2026): One rule added, one skill bumped, and the\n"
V345_END = "Functional for Claude, readable for human, signal preserved.\n"
V345_MUST_END_WITH = "resident.\n\n"

HISTORY_ANCHOR = (
    "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"
)
MOVED_NOTE = (
    "\n"
    "(Moved down from the resident protocol on 2026-08-29 when v3.48\n"
    "made a fourth entry.)\n"
    "\n"
)


HANDOFF_TEXT = """# HANDOFF -- 2026-08-29 night: the Sun exhibit finished, and the
# gallery gets a runner

**Built on** orrery `bfa9de2fc0b9c2d30c9eb4de27828a8c2b4c8535` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `6c6123974e883a461a92b586b8352c9c535ee8d1` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote at the close of the session.

**Type:** BUILD.

**Companion to** `documentation/HANDOFF_20260829_sun_ships.md`, which
records the ship itself earlier the same day. That document is not
superseded; this one continues from it.

---

## What was done

Everything below was measured, not carried. Where a figure came from a
document rather than a run, it says so.

**The Sun exhibit is finished on its visible surface.** The axes carry
X (AU), Y (AU), Z (AU), using the desktop orrery's own wording from
`build_scene_axes` in `visualization_utils.py`. Tony's Mode 5 read of
the deployed page confirmed both the defect and the fix. The Solar
System Explorer's `buildLayout` has the same blank titles and was left
alone: it is a frozen exhibit on the A path and changing it is a
separate call with its own Mode 5.

**The chromosphere value now matches the store.**
`objects_config.json` held 1.0028748 where `constants_new.py` derives
1.002874802357338. The drift check re-run against the LIVE site reports
26 match, 0 DRIFT, where it read 25 and 1. The corrected radiative-zone
figure is visible in the exhibit's hover with its full citation --
0.713 solar radii, 496,034 km, 0.00332 AU, Christensen-Dalsgaard, Gough
& Thompson (1991). A provenance correction readable by a visitor is new
in this project.

**The gallery has a maintenance runner** (L-236, closed). It departs
from the orrery's in two ways, and both were the design decision rather
than detail. TWO MOMENTS: the plain run is offline and goes before a
commit, and `--live` goes after a push, because the Jekyll failure that
broke the ship existed only on the deployed site and only after a push.
THREE STATES: pass, fail, and unreachable, with unreachable counted
separately and never folded into a passing total.

**Both runners have repo-specific names** (L-264, closed).
`orrery_maintenance_run.py` and `gallery_maintenance_run.py`. Seven live
references swept; the ledger, the handoffs and the spent patch scripts
deliberately left alone as records of what happened under the old name.
Two dashboard rows added for the gallery runner, offline and `--live`.
Nine tracked `.bak` files retired and `*.bak` added to `.gitignore`.

**provenance-discipline 2.10 is recorded in protocol v3.47** (L-258,
closed), together with the significant-figures rule it added, the
RADIATIVE_ZONE_AU correction, the INNER_CORONA_RADII re-homing, and the
two pinned literals restated as ratio bounds.

**The Register Rule makes plain speech the default** (L-261, closed),
on Tony's instruction. The compressed voice keeps its home in the
protocol and the skills; it leaves the chat.

---

## Four defects, and what each one teaches

**One. `smoke_framing.js` has never run** (L-262, OPEN). It slices
`interactive.html` between `function gridDtick(span) {` and
`async function fetchText(url) {`, and neither marker has ever existed
in that file in any commit -- measured across the whole history of both
files. It was added on 2026-08-26 with L-238 and has failed on every
execution since, unnoticed, because it sits in `documentation/` and was
in no routine. Put the check where it runs.

**Two. The reachability check called a correct deploy stale.** It
compared raw bytes; `gallery_cache_builder.py` writes two JSON files in
text mode, so they are CRLF in the working copy and LF in the repo and
on the site. The same line-ending fault had been diagnosed and fixed in
the patch scripts a few hours earlier and was not carried to the runner.
One producer, two consumers, one of them moved.

**Three. The orrery lost its own runner for three commits.** Two
programs were called `maintenance_run.py`, one per repo; the gallery's
was downloaded, the orrery's was displaced, and the deletion travelled
inside a commit that also added a patch script, so it was invisible at
a glance. Recovered byte-identical from `8b762e0`.

**Four. Two handles were cited before their blocks existed.** L-258's
protocol entry and L-264's ledger block were both named in committed
code before anything backed them. Both were found by a person reading,
not by a check. The detection L-230 designs is still unbuilt, and this
is now its third instance.

---

## The skill bump, and the one thing it cannot verify

**safe-file-editing went to 1.9** with Compare Content, Not Bytes
[QUALITY], and protocol v3.48 records it in the same commit that made
it -- which is the whole of the improvement over this morning, when
provenance-discipline 2.10 got its version line, its manifest row and
its commit and not its protocol entry.

**The one step that cannot be discharged from inside the session that
made it:** a skill lives in three stores, and the account install is the
copy Claude actually loads. A reinstall is invisible to the running
conversation, so it is carried in writing instead:

    safe-file-editing went to 1.9 at `bfa9de2f`; the session that
    bumped it had loaded 1.8; the next session confirms its loaded
    copy reads 1.9 before doing patch work.

**Tony-action (do):** reinstall safe-file-editing to the account profile
(Settings > Skills) alongside the commit.

---

## Open decisions for Tony

**L-262, how to fix it.** Re-point the smoke test's markers at the
page's real helpers, or extract those helpers so the page and the test
read one copy. The second is more work and removes the failure class,
since the test broke precisely because it read a copy of logic that
lives inline in the page. It touches `interactive.html`, which is live.

**L-256, which dict joins the status-pass beta.**
`spectral_subclass_temps` (9 entries, and Fable already flagged it as an
uncited physical claim inside the store) or `CENTER_BODY_RADII` (18
well-sourced radii). Open since 2026-08-27 and the single thing blocking
the item.

**L-237, when.** Earth's shells will change artifact 1's feature set
again, so re-cutting the golden record now means re-cutting it twice.
The recommendation is Earth first, re-cut once.

---

## Next-session scoping

The ladder's next rung is **Earth's existing shells**. The data is
already served -- `atmosphere_shell` with two shells plus
`planet_radius`, and `van_allen_belts` with both belts plus thickness --
and `feature_renderers.js` already has live cases for both slugs. No new
hand copy into `objects_config.json` is created by this step, which is
why it was chosen ahead of the transport.

Also open, unchanged by this session: L-257's three enforcement builds,
the rendering ladder still not written into the master plan, and
segment 2, the cross-repo transport, which failed its first real test
this morning and is now evidenced rather than argued.

**The mobile check happened at the close of the session**, on iPhone
Safari, both orientations, and it is the reason L-260 stays open.

The exhibit WORKS on a phone. Pyodide loaded, the assembler ran, the
shells drew, the axis titles are there. That is the premise of the whole
interactive gallery passing its first real test, and it is the headline
rather than what follows.

LANDSCAPE is usable as it stands: the legend takes about a quarter of
the width, scrolls, and the Sun renders clear of it.

PORTRAIT is not. The legend covers roughly 58 percent of the width and
58 percent of the height as an overlay, and the Sun sits BEHIND it, so
the object of the exhibit is the part you cannot see. All 18 entries
render at once instead of scrolling as they do in landscape. The axis
titles also clip -- only fragments of X (AU) and Y (AU) reach the
viewport at the bottom corners.

Both are read from screenshots rather than from the page, and neither is
diagnosed. gallery-pipeline 1.2 carries the 768 px breakpoint and a
bottom-drawer pattern for exactly this case, and the Sun exhibit does
not use it. Whether that is the fix is a design conversation. **This is
the first thing the next session should take up**, ahead of Earth's
shells: the exhibit is public, and portrait is how a phone is held.

---

*Session written August 2026 with Anthropic's Claude Opus 5. Built on
orrery `bfa9de2fc0b9c2d30c9eb4de27828a8c2b4c8535`, gallery
`6c6123974e883a461a92b586b8352c9c535ee8d1`; both confirmed against the
live remote.*
"""


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


def stage(root, name, want_md5, edits):
    """Guard a file and apply its edits. None on any refusal.

    The guard is computed on the LF-normalised CONTENT, not on the raw
    bytes, and the line-ending style is carried so each file is written
    back the way it was found. That is safe-file-editing 1.9's own rule,
    which this patch is the one that adds -- the tool obeying the rule it
    is installing.
    """
    path = os.path.join(root, name)
    print("")
    print("target :", name)
    if not os.path.isfile(path):
        print("REFUSED: no such file. Nothing written anywhere.")
        return None
    with open(path, "rb") as handle:
        raw = handle.read()
    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw
    actual = hashlib.md5(content).hexdigest()
    print("md5    : %s (expected %s)%s"
          % (actual, want_md5, "   [CRLF]" if was_crlf else ""))
    if actual != want_md5:
        print("REFUSED: %s is not in the state this patch expects." % name)
        print("         Nothing written anywhere, no handoff created.")
        return None

    text = content.decode("utf-8")
    for label, old, _new in edits:
        count = text.count(old)
        print("  anchor x%d  %s" % (count, label))
        if count != 1:
            print("REFUSED: anchor matched %d times, expected 1." % count)
            print("         Nothing written anywhere.")
            return None
    for _label, old, new in edits:
        text = text.replace(old, new, 1)

    out = text.encode("utf-8")
    before = sum(1 for byte in raw if byte > 127)
    after = sum(1 for byte in out if byte > 127)
    print("  non-ascii bytes: %d -> %d" % (before, after))
    if after != before:
        print("REFUSED: the patch introduced non-ASCII text.")
        return None
    return (path, name, raw, out, was_crlf)


def main():
    print("patch_close_20260829_and_handoff.py")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    handoff_path = os.path.join(root, HANDOFF)
    if os.path.exists(handoff_path):
        print("")
        print("REFUSED: %s already exists." % HANDOFF)
        print("         Either this patch has already run, or that name is")
        print("         taken. Nothing written.")
        return 1
    if not os.path.isdir(os.path.dirname(handoff_path)):
        print("REFUSED: no documentation/ directory.")
        return 1

    staged = []

    # ---- 1. the ledger ---------------------------------------------
    got = stage(root, LEDGER, LEDGER_MD5, EDITS)
    if got is None:
        return 1
    staged.append(got)

    # ---- 2. the skill ----------------------------------------------
    got = stage(root, SKILL, SKILL_MD5, SKILL_EDITS)
    if got is None:
        return 1
    staged.append(got)

    # ---- 3. the protocol: two edits, then lift v3.45 out ------------
    got = stage(root, PROTO, PROTO_MD5, PROTO_EDITS)
    if got is None:
        return 1
    path, name, raw, out, crlf = got
    text = out.decode("utf-8")
    for label, marker in (("v3.45 start", V345_START), ("v3.45 end", V345_END)):
        count = text.count(marker)
        print("  marker x%d  %s" % (count, label))
        if count != 1:
            print("REFUSED: marker matched %d times, expected 1." % count)
            return 1
    i, j = text.index(V345_START), text.index(V345_END)
    if not i < j:
        print("REFUSED: the v3.45 end marker precedes its start.")
        return 1
    v345 = text[i:j]
    if not v345.endswith(V345_MUST_END_WITH):
        print("REFUSED: the lifted v3.45 block does not end where expected.")
        return 1
    print("  lifted v3.45: %d bytes" % len(v345))
    staged.append((path, name, raw, (text[:i] + text[j:]).encode("utf-8"),
                   crlf))

    # ---- 4. the history receives v3.45 verbatim --------------------
    got = stage(root, HISTORY, HISTORY_MD5, [
        ("v3.45 lands above the preserved-lessons block",
         HISTORY_ANCHOR,
         v345.rstrip("\n") + "\n" + MOVED_NOTE + HISTORY_ANCHOR),
    ])
    if got is None:
        return 1
    staged.append(got)

    handoff_bytes = HANDOFF_TEXT.encode("utf-8")
    stray = sum(1 for byte in handoff_bytes if byte > 127)
    print("  handoff: %d bytes, %d non-ascii" % (len(handoff_bytes), stray))
    if stray:
        print("REFUSED: the handoff carries non-ASCII text.")
        return 1

    # ---- all four passed; write ------------------------------------
    print("")
    for path, name, raw, out, crlf in staged:
        # raw is the file EXACTLY as read, so the backup is written
        # unchanged. Converting it would double-convert a CRLF file into
        # \r\r\n and leave a corrupt undo -- which is the one file you
        # reach for when something has gone wrong.
        final = out.replace(b"\n", b"\r\n") if crlf else out
        with open(path + ".bak", "wb") as handle:
            handle.write(raw)
        with open(path, "wb") as handle:
            handle.write(final)
        print("WROTE   %-46s (%d -> %d bytes%s)"
              % (name, len(raw), len(final), ", CRLF" if crlf else ""))

    with open(handoff_path, "wb") as handle:
        handle.write(handoff_bytes)
    print("CREATED %s  (%d bytes)" % (HANDOFF, len(handoff_bytes)))

    print("")
    print("Next, in this order:")
    print("  1. ledger_index.py            -- migrates L-236 and L-263")
    print("                                   into section C")
    print("  2. orrery_maintenance_run.py  -- should stay 11 of 11")
    print("")
    print("Then commit ALL of it together -- ledger, skill, protocol,")
    print("history and handoff. That single commit is step 4 of the")
    print("skill-bump binding rule, and doing it in one go is the whole")
    print("point: this morning's bump got three of its four steps.")
    print("")
    print("One step this patch cannot do: reinstall safe-file-editing to")
    print("the account profile (Settings > Skills). The handoff carries")
    print("the obligation for the next session to confirm it reads 1.9.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
