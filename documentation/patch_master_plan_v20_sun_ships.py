"""
patch_master_plan_v20_sun_ships.py

Updates both plan documents for 2026-08-29, when the Sun went live on
the public gallery.

Built on orrery `688561ef63706cefcac981e381d794c324033432` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `ac9a5c7baf108b4c90a32ed5c80235e4a1c8625a` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote 2026-08-29.

Two files, one transaction.  Nothing is written unless every anchor in
both matches.


WHAT CHANGES, AND WHY THESE FOUR THINGS

1. THE MODE 5 SENTENCE, corrected in both documents.  Section 5a says a
   wrong ring radius "becomes something Tony's EYES can catch"; the
   critical path says "something a person can look at."  That sentence
   is the stated justification for the braid's ordering, so it is
   load-bearing rather than decorative.

   Fable's review of 2026-08-27 contradicted it and this session
   produced the direct evidence.  RADIATIVE_ZONE_AU moved 0.7 -> 0.713,
   a 1.9 percent change in a drawn radius, and it was caught by READING
   THE HOVER TEXT, not by seeing the geometry.  At no zoom is 1.9
   percent visible.

   The passage is not withdrawn, because the render did catch it -- but
   through a different mechanism than the sentence claimed, and the
   difference matters for what the render can be trusted to do.  The
   correction narrows the claim to the geometry and adds the mechanism
   that actually worked.

2. SEGMENT 2 IS RAISED, on evidence rather than argument.  Both
   documents place the transport as protection against later drift.  On
   2026-08-29 it was the thing standing between a corrected orrery and a
   stale public page: the builder ran clean and served 0.7 for hours
   after constants_new.py held 0.713, because objects_config.json is a
   hand copy and fetch-and-import was ratified on 2026-08-08 and never
   built.

3. THE STALE ROWS ARE RE-MEASURED.  Section 5a's "You are here" table
   was read on 2026-08-23 and its segment-3 row has carried a NOT
   STARTED that the 2026-08-25 append already flagged.  It is now wrong
   in a second direction: the Sun is not merely complete in the
   assembler, it is live on the public site.

4. THE SHELL COUNT.  The 2026-08-25 append says 19 shells.  Measured at
   gallery ac9a5c7b through the real renderer: 18 drawable, 18 named
   traces plus 18 info-marker companions.  Corrected rather than
   restated, per this document's own rule about the 105/107/110 drift.


HOW TO RUN IT

Drop this file into the ORRERY repo root -- the folder holding
constants_new.py and documentation/ -- and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"

PROBE = "constants_new.py"
MP = os.path.join("documentation", "MASTER_PLAN_INTERACTIVE_GALLERY.md")
CP = os.path.join("documentation", "MASTER_PLAN_CRITICAL_PATH_SUMMARY.md")

MP_MD5 = "652ff5f8a6f42c52391b6be15b883bba"
CP_MD5 = "c9da694bf362153ca1652843b6ba4f3a"


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


# ---------------------------------------------------------------------
# MASTER_PLAN_INTERACTIVE_GALLERY.md
# ---------------------------------------------------------------------

MP_EDITS = [
    (
        "status header v19 -> v20",
        "**Status:** v19 -- Phase 2 (solar system assembler) BUILD UNDERWAY.",
        "**Status:** v20 -- Phase 2 (solar system assembler) BUILD UNDERWAY;\n"
        "**the first feature-bearing exhibit is LIVE.** The Sun ships at\n"
        "`palomasorrery.com/interactive.html?exhibit=sun`, unlinked from the\n"
        "landing page, Mode 5 accepted 2026-08-29 (gallery `ac9a5c7b`).",
    ),
    (
        "narrow the Mode 5 claim in 5a to what the geometry actually catches",
        "And the order pays for itself, because the render is this project's own\n"
        "ground truth. Ring provenance today is an audit of numbers nobody can\n"
        "see -- text checked against text, which is precisely the mode that\n"
        "produced three separate failures on 2026-08-22. Once the assembler\n"
        "draws, a wrong ring radius becomes something Tony's EYES can catch.\n"
        "Segment 3 is what gives the provenance work a render to be checked\n"
        "against.\n",

        "And the order pays for itself, because the render is this project's own\n"
        "ground truth. Ring provenance today is an audit of numbers nobody can\n"
        "see -- text checked against text, which is precisely the mode that\n"
        "produced three separate failures on 2026-08-22. Segment 3 is what\n"
        "gives the provenance work a render to be checked against.\n"
        "\n"
        "**One clause here was too strong and is corrected 2026-08-29.** It\n"
        "read that a wrong ring radius \"becomes something Tony's EYES can\n"
        "catch.\" The GEOMETRY catches gross errors -- a wrong frame, a factor\n"
        "of two, a body in the wrong place. It does not catch a few percent.\n"
        "Fable's review of 2026-08-27 said so, and this project then produced\n"
        "the case: `RADIATIVE_ZONE_AU` moved 0.7 -> 0.713, a 1.9 percent\n"
        "change in a drawn radius, invisible at any zoom.\n"
        "\n"
        "It WAS caught on the render, which is why the argument survives --\n"
        "but by READING THE HOVER TEXT, not by seeing the shell. That is the\n"
        "mechanism worth naming, because it is the one to design for: the\n"
        "hover carries the value, the units and the source, so drawing a\n"
        "feature puts its provenance in front of a reader for the first time.\n"
        "The Alfven case Fable cited -- one solar radius in fifteen -- would\n"
        "have been caught the same way and by nothing else.\n",
    ),
    (
        "re-measure the stale rows and record 2026-08-29",
        "**Two rows above are stale and are deliberately left standing.**\n"
        "\"Segment 3, assembler draw: NOT STARTED\" -- the Sun is now complete in\n"
        "the assembler, 19 shells, Mode 5 passed on 2026-08-24 and 2026-08-25.\n"
        "\"Artifact 1, Earth: LOCKED\" -- reopened by the ruling above, and its\n"
        "golden record is stale in four fields (L-237). Re-measuring those rows\n"
        "belongs to a pass that reads the repo, not to this append; a table\n"
        "re-stated from memory is how the 105 / 107 / 110 drift happened in this\n"
        "document.\n",

        "**Two rows above are stale and are deliberately left standing.**\n"
        "\"Segment 3, assembler draw: NOT STARTED\" -- the Sun is now complete in\n"
        "the assembler, 19 shells, Mode 5 passed on 2026-08-24 and 2026-08-25.\n"
        "\"Artifact 1, Earth: LOCKED\" -- reopened by the ruling above, and its\n"
        "golden record is stale in four fields (L-237). Re-measuring those rows\n"
        "belongs to a pass that reads the repo, not to this append; a table\n"
        "re-stated from memory is how the 105 / 107 / 110 drift happened in this\n"
        "document.\n"
        "\n"
        "### 2026-08-29 -- the Sun ships, and four things shipping it found\n"
        "\n"
        "Measured at orrery `688561ef` and gallery `ac9a5c7b`, both confirmed\n"
        "against the live remote. The row above is now stale in a second\n"
        "direction and this subsection re-measures it rather than editing the\n"
        "table from memory.\n"
        "\n"
        "**Segment 3 is DONE for the Sun, and segment 5 has begun.** The Sun\n"
        "exhibit is live at `interactive.html?exhibit=sun`, unlinked from the\n"
        "landing page, carrying inline credit. It runs the shared assembler\n"
        "package in Pyodide against the served cache and hands the feature\n"
        "report to `feature_renderers.js` -- architecture B', Section 3a's\n"
        "Python-assembles / JavaScript-draws split, working end to end in a\n"
        "visitor's browser for the first time. Mode 5 accepted.\n"
        "\n"
        "It is a SECOND exhibit on the page that has been public since July,\n"
        "reached by the `?exhibit=` parameter Section 2a designed for exactly\n"
        "this. The Solar System Explorer is untouched and still the default.\n"
        "\n"
        "**The shell count is 18, not 19.** Measured through the real renderer\n"
        "at `ac9a5c7b`: 18 drawable shells, 18 named traces plus 18\n"
        "info-marker companions. The 2026-08-25 append says 19. Corrected\n"
        "here rather than restated.\n"
        "\n"
        "**Four defects surfaced, three of which nothing could have caught\n"
        "earlier.** GitHub Pages served no `.py` file in the repo at all --\n"
        "Jekyll runs by default and there was no `.nojekyll`, so the whole\n"
        "assembler directory 404'd while working perfectly over a local\n"
        "server. Fixed at gallery `833daa9a`. The scene axes were pinned, so\n"
        "the legend could not move the frame and a visitor toggling the\n"
        "heliopause saw nothing happen. And `feature_renderers.js` sent a\n"
        "shell's GEOMETRY to the legend without its info marker, so nine\n"
        "markers were being drawn between 94 AU and 150,000 AU, hoverable,\n"
        "with nothing around them -- invisible only because the pinned axes\n"
        "fell inside them. That one predates the Sun exhibit and was surfaced\n"
        "by fixing the second: the protocol's own lesson about an invisible\n"
        "thing surfacing its neighbours.\n"
        "\n"
        "**The fourth is SEGMENT 2, and it stops being theoretical.** The\n"
        "session corrected `RADIATIVE_ZONE_AU` in the orrery, pushed, and\n"
        "re-ran the cache builder -- and the site went on serving 0.7 for\n"
        "hours. The builder passes feature constants THROUGH from\n"
        "`data/objects_config.json`, a hand copy in the gallery repo. It has\n"
        "never read `constants_new.py`. Fetch-and-import was RATIFIED\n"
        "2026-08-08 (Section 7, decision 12) and never built, so the two\n"
        "repos have no mechanism connecting them at all.\n"
        "\n"
        "The value reached the site by a hand patch to `objects_config.json`.\n"
        "That is not a workaround, it is the current architecture.\n"
        "\n"
        "**So segment 2 is repositioned.** It is described in this section as\n"
        "protection against a correct orrery drifting from its copy LATER.\n"
        "That is too weak. Under the export gate (provenance-discipline 2.9)\n"
        "the boundary the gate names is a human copy with no check on it, so\n"
        "the transport is the gate's MISSING ENFORCEMENT POINT. The\n"
        "2026-08-28 handoff predicted this in the abstract; it failed in its\n"
        "first real test the following day. It does not gate the next\n"
        "exhibit, and it should be built before the ladder gets long enough\n"
        "that hand-copying many bodies becomes routine.\n"
        "\n"
        "**Handles owed, not minted here.** L-258 (the significant-figures\n"
        "rule and its two constants) has no ledger entry; the Sun exhibit has\n"
        "no handle at all; and `provenance-discipline` went 2.9 -> 2.10 in a\n"
        "session that cannot verify its own reinstall. The ledger carries\n"
        "status authority (L-221), so those are ledger edits and this section\n"
        "records them rather than asserting around them.\n",
    ),
]


# ---------------------------------------------------------------------
# MASTER_PLAN_CRITICAL_PATH_SUMMARY.md
# ---------------------------------------------------------------------

CP_EDITS = [
    (
        "date header and anchors",
        "**Updated August 23, 2026.** Orrery at\n"
        "`09736422e8b26d348f539cd8b49628e8a0c670ab`, gallery at\n"
        "`02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6`. Both confirmed against\n"
        "the live remote. First written August 16 at `227f5b2d`; the five\n"
        "steps below still have not moved.\n",

        "**Updated August 29, 2026.** Orrery at\n"
        "`688561ef63706cefcac981e381d794c324033432`, gallery at\n"
        "`ac9a5c7baf108b4c90a32ed5c80235e4a1c8625a`. Both confirmed against\n"
        "the live remote. First written August 16 at `227f5b2d`.\n"
        "\n"
        "**On August 29 a step moved for the first time.** Step three is done\n"
        "for one body and step five has begun: the Sun is live on the public\n"
        "gallery. What that cost, and the three defects it exposed, is at the\n"
        "end of this file under \"August 29 -- the first one ships.\" The body\n"
        "of the document below is as it stood on August 23 except where a\n"
        "correction is marked.\n",
    ),
    (
        "narrow the ground-truth claim to what the geometry catches",
        "The order also pays for itself. A ring radius nobody can see can only\n"
        "be checked as text against text. Once the assembler draws it, a wrong\n"
        "radius becomes something a person can look at -- which is this\n"
        "project's own definition of ground truth.\n",

        "The order also pays for itself. A ring radius nobody can see can only\n"
        "be checked as text against text. Once the assembler draws it, a wrong\n"
        "radius becomes something a person can look at -- which is this\n"
        "project's own definition of ground truth.\n"
        "\n"
        "**That last sentence is too strong and is corrected August 29.** The\n"
        "geometry catches gross errors: a wrong frame, a factor of two, a body\n"
        "in the wrong place. It does not catch a few percent. The radiative\n"
        "zone moved 0.7 -> 0.713 that day -- 1.9 percent of a drawn radius,\n"
        "invisible at any zoom -- and it WAS caught on the live page, by\n"
        "reading the hover text rather than by looking at the shell. The hover\n"
        "carries the value, the units and the source, so drawing a feature is\n"
        "what puts its provenance in front of a reader. That is the real\n"
        "mechanism and it is worth designing for; \"a person can look at it\"\n"
        "names the wrong half.\n",
    ),
    (
        "raise step two on evidence",
        "**Two. Make the copy faithful.** A correct orrery is not enough while\n"
        "the gallery's copy of its constants is maintained by hand. The transport\n"
        "design is settled; it has not been built.\n",

        "**Two. Make the copy faithful.** A correct orrery is not enough while\n"
        "the gallery's copy of its constants is maintained by hand. The transport\n"
        "design is settled; it has not been built.\n"
        "\n"
        "**Raised August 29, on evidence rather than argument.** This step\n"
        "was written as protection against drift arriving later. It is not:\n"
        "on August 29 a value was corrected in the orrery, pushed, and the\n"
        "cache builder re-run, and the public site went on serving the old\n"
        "number for hours. The builder has never read `constants_new.py` --\n"
        "it copies from `objects_config.json`, which is maintained by hand in\n"
        "the other repo. The correction reached the site by a hand patch.\n"
        "Under the export gate the transport is not a defence against future\n"
        "drift; it is the only place the gate could ever fire.\n",
    ),
    (
        "step three: done for one body",
        "**Three. Teach the assembler to draw. This is the next work.** It is\n"
        "independent of the first two and could be done tomorrow -- the data is\n"
        "already sitting in the served cache.",

        "**Three. Teach the assembler to draw.** DONE for the Sun on August\n"
        "29 and live on the public site; see the section at the end of this\n"
        "file. The paragraph below is as written on August 23, when it had\n"
        "not been started. It is\n"
        "independent of the first two and could be done tomorrow -- the data is\n"
        "already sitting in the served cache.",
    ),
    (
        "append the August 29 record",
        "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures\n",

        "## August 29 -- the first one ships\n"
        "\n"
        "**The Sun is live** at `palomasorrery.com/interactive.html?exhibit=sun`,\n"
        "unlinked from the landing page, Mode 5 accepted. Eighteen shells from\n"
        "the core out to the Sun's gravitational influence at 150,000 AU, each\n"
        "carrying its source in its hover text.\n"
        "\n"
        "What is actually new is not the picture. It is that the shared Python\n"
        "assembler ran in a visitor's browser, against the served cache, and\n"
        "handed its feature report to JavaScript to draw -- the architecture\n"
        "settled in July, working end to end outside this machine for the\n"
        "first time. No server, no Horizons call, no ephemeris: a Sun-alone\n"
        "scene has no orbit, so every number in it comes from published\n"
        "literature.\n"
        "\n"
        "**Three defects surfaced that nothing had been able to see.**\n"
        "\n"
        "GitHub Pages was serving no `.py` file in the repository at all.\n"
        "Pages runs Jekyll by default, there was no `.nojekyll`, and the whole\n"
        "assembler directory returned 404 -- while working perfectly over a\n"
        "local server, which is where every previous test had run. One empty\n"
        "file fixed it.\n"
        "\n"
        "The scene axes were pinned, so nothing the legend did could move the\n"
        "frame: a visitor turning on the heliopause at 121 AU inside a\n"
        "quarter-AU box saw the page do nothing at all.\n"
        "\n"
        "And each shell is drawn as two traces -- geometry, and one marker\n"
        "carrying the hover. The renderer sent the geometry to the legend when\n"
        "a shell was too big for the frame and left its marker behind. Nine\n"
        "markers were being drawn between 94 AU and 150,000 AU with nothing\n"
        "around them, invisible only because the pinned axes fell inside them.\n"
        "That defect predates the exhibit and was surfaced by fixing the\n"
        "second one: fixing an invisible thing surfaces its neighbours.\n"
        "\n"
        "**And step two failed in its first real test**, which is recorded\n"
        "above where the step is described. The short form: a corrected value\n"
        "did not travel, the builder that was supposed to carry it never reads\n"
        "the store, and a hand patch to the other repo is what put the right\n"
        "number on the site.\n"
        "\n"
        "**Two values were closed on the way**, both drawn on the page.\n"
        "`RADIATIVE_ZONE_AU` went to 0.713, the figure its own source supports,\n"
        "with the citation restated to say what the paper says: a\n"
        "convection-zone depth of 0.287, base at 1 - 0.287. And\n"
        "`INNER_CORONA_RADII` kept its value and changed its citation, from a\n"
        "book locatable only as \"Chapter 1\" to open text stating the same\n"
        "boundary. Three cross-check legs retired with the values and\n"
        "citations they had certified.\n"
        "\n"
        "The rule behind the first one is now in the skill rather than in\n"
        "anyone's head: a store carries the verified figure, and rounding\n"
        "happens at the reporting step, never at rest.\n"
        "\n"
        "---\n"
        "\n"
        "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; figures\n",
    ),
    (
        "footer anchors",
        "`STREAMER_BELT_RADII`, and DeForest's 15 R_sun. Built on\n"
        "`09736422e8b26d348f539cd8b49628e8a0c670ab` at\n"
        "https://github.com/tonylquintanilla/palomas_orrery, gallery at\n"
        "`02aefc0cefbf334889b7c6b3b05bf8fdfab74fa6`. Both confirmed against\n"
        "the live remote.*\n",

        "`STREAMER_BELT_RADII`, and DeForest's 15 R_sun. Revised August 29\n"
        "for the first shipped exhibit: step three done for one body, step\n"
        "two raised on evidence, and the ground-truth claim narrowed to what\n"
        "the geometry actually catches. Built on\n"
        "`688561ef63706cefcac981e381d794c324033432` at\n"
        "https://github.com/tonylquintanilla/palomas_orrery, gallery at\n"
        "`ac9a5c7baf108b4c90a32ed5c80235e4a1c8625a`. Both confirmed against\n"
        "the live remote.*\n",
    ),
]


def check(path, expected_md5, edits, label):
    print("")
    print("--- %s" % label)
    print("path   :", path)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return None
    with open(path, "rb") as fh:
        raw = fh.read()
    actual = hashlib.md5(raw).hexdigest()
    print("md5    : %s (expected %s)" % (actual, expected_md5))
    if actual != expected_md5:
        print("REFUSED: not the file this patch was cut against.")
        return None
    if b"\r\n" in raw:
        print("REFUSED: CRLF line endings; this patch expects LF.")
        return None
    text = raw.decode("utf-8")
    for name, old, _new in edits:
        n = text.count(old)
        print("  anchor x%d  %s" % (n, name))
        if n != 1:
            print("REFUSED: anchor matched %d times, expected 1." % n)
            return None
    return raw, text


def main():
    print("patch_master_plan_v20_sun_ships.py")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    mp_path = os.path.join(root, MP)
    cp_path = os.path.join(root, CP)

    mp = check(mp_path, MP_MD5, MP_EDITS, "MASTER_PLAN_INTERACTIVE_GALLERY.md")
    if mp is None:
        print("")
        print("NOTHING WAS WRITTEN.")
        return 1

    cp = check(cp_path, CP_MD5, CP_EDITS,
               "MASTER_PLAN_CRITICAL_PATH_SUMMARY.md")
    if cp is None:
        print("")
        print("NOTHING WAS WRITTEN. The master plan is untouched.")
        return 1

    outputs = []
    for (raw, text), edits, path in ((mp, MP_EDITS, mp_path),
                                     (cp, CP_EDITS, cp_path)):
        for _name, old, new in edits:
            text = text.replace(old, new, 1)
        out = text.encode("utf-8")
        before = sum(1 for c in raw if c > 127)
        after = sum(1 for c in out if c > 127)
        if after != before:
            print("REFUSED: %s gained non-ASCII text (%d -> %d). Nothing "
                  "written." % (os.path.basename(path), before, after))
            return 1
        outputs.append((path, raw, out))

    for path, raw, out in outputs:
        with open(path + ".bak", "wb") as fh:
            fh.write(raw)
        with open(path, "wb") as fh:
            fh.write(out)

    print("")
    for path, raw, out in outputs:
        print("WROTE   %s  (%d -> %d bytes)" % (path, len(raw), len(out)))
    print("")
    print("Both documents are pure ASCII and stay that way.")
    print("Master plan is now v20. Critical path is dated August 29.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
