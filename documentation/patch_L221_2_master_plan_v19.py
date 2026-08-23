"""patch_L221_2_master_plan_v19.py

Built on 38923c1cc64d492006135ec77779e1fb592582d5 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery at 493a0bd7fcba4067c56db318357889e965fba514.
Written August 22, 2026 with Anthropic's Claude Opus 5.

RUN IT LIKE THIS
    Save into documentation/ (beside the file it edits), open in VS Code,
    click Run.  Equivalent command: python patch_L221_2_master_plan_v19.py
    The target is resolved beside this script, so the working directory
    does not matter.

Transactional, all-or-nothing, binary I/O.  Nothing is written unless
every anchor matches exactly once.  One target:
documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md

WHAT IT DOES -- v18 -> v19, twenty-one edits carrying twenty-nine findings
from the full-document sweep.  Grouped as the sweep grouped them.

  THE BRAID (Tony's ruling, 2026-08-22; argument in
  documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md Section 1)
     1. Header Status line: v18 -> v19, carrying the braid in one sentence.
    11. Section 5 Phase 2 track table gains a superseded-by pointer.  The
        August ruling stays as history; only its scope narrows.
    12. Section 5a gains an "Amended 2026-08-22" paragraph.
    13. Section 5a: the "that asymmetry is why the provenance refactor
        precedes the assembler work" paragraph is the exact claim the
        braid overturns.  Replaced.
    14. Section 5a segment 1 gains the per-artifact slice, counted.
    15. Section 5a segment 4 stops implying Saturn has radiation belts.
    16. Section 5a gains "The order of execution" -- the five segments do
        NOT move; the order they are worked in does.
    17. Section 5a "You are here" restamped to 2026-08-22 / 38923c1 /
        493a0bd, with the reconciliation figures re-measured.
    20. Section 10 gains a *New in v19* lineage entry.

  MECHANICAL -- the repo contradicted the document
     2. L-120 (F3) is DONE 2026-07-27, not OPEN.
     3. Base block restamped; L-151 is DONE 2026-07-27; and the internal
        contradiction is removed (the header said Layer 3 was "enabled
        with a known open issue" forty lines after saying it was RETIRED).
     4. Section 1 gallery size re-measured: 439 MB / ~585 MB headroom.
     6. Section 3a stops carrying a SECOND, disagreeing size figure.
     7. Section 3a's L-108 pointer: that item CLOSED 2026-07-12.
     8. OQ-E likewise defers to Section 1 for size.
     9. palomas_orrery.py is 11,092 lines, not 11,110.
    18. Section 6: L-162 is DONE 2026-07-29, not "[ ] Not started".
    21. Section 11: gallery-pipeline v1.1 landed; it is at 1.2.

  A REASON THAT WAS FALSE WHILE ITS CONCLUSION HELD
     5. Section 2 seam 2, 10. Phase 2 "Requires", and 17. Section 6's
        entry all said palomas_orrery_helpers.py imports tkinter and that
        the split is not started.  At HEAD the file has ZERO tkinter
        references and L-087 is DONE (2026-07-15).  The seam survives in
        a different shape -- three modules in its transitive import
        closure still import tkinter -- so the requirement is real and
        the stated reason was not.  Corrected, not re-opened.

  OPEN QUESTIONS THE PLAN ASKED, ANSWERED BY MEASUREMENT
    18. Section 7 decision 12 said "the plan says two [constructor calls],
        measurement finds one ... Resolve by looking, not by patching."
        Looked: TWO.  HORIZONS_MAX_DATE and stellar_class_labels.
    19. Section 7 decision 16 said "Confirm before the pilot starts":
        Jupiter has FOUR ring entries.

  STRUCTURAL
    20. Section 10: AB_FORK_ANALYSIS.md is cited and is in neither repo.
    22. Closing block: base SHAs, protocol version, and the ten
        hand-written skill versions.  The version list is DELETED and
        replaced by a pointer to the protocol's generated Skill Manifest
        -- five of ten had drifted and nothing watched them.  Tony's
        ruling, 2026-08-22.  Fix the producer, not N consumers.
    23. The unmatched code fence at end of file is removed.  The file
        held five ``` markers, an odd count; the last one opened a block
        that never closed.

WHAT IS PERMANENT AND WHAT IS NOT
  This script is disposable -- it guards on a fingerprint that stops
  existing the moment it succeeds.  What it installs is permanent: the
  v19 document, and in particular the removal of the skill-version
  shadow store, which is a standing change to what this document
  carries rather than a correction to a value in it.

NOT DONE HERE, and reported instead (they are not this file's to fix):
  - L-225 has no ledger entry.  The highest handle is L-224.
  - L-154 is ledger-BLOCKED and the braid unblocks it.  The plan is the
    sequencing authority, the ledger is the status authority, so this
    needs a ledger edit rather than a silent contradiction.
  - MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md line 20 still points at
    the bare CRITICAL_PATH_SUMMARY.md.

AFTER RUNNING
  1. Read the run output; every line should say ok.
  2. Move this script to documentation/ if it is not already there.
  3. Commit and push.
"""

import hashlib
import os
import sys

BASE_SHA = '38923c1cc64d492006135ec77779e1fb592582d5'
GALLERY_SHA = '493a0bd7fcba4067c56db318357889e965fba514'
MODEL = "Anthropic's Claude Opus 5"

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET_NAME = 'MASTER_PLAN_INTERACTIVE_GALLERY.md'

# Content fingerprint at BASE_SHA, CRLF-normalized before hashing so a
# Windows working copy with CRLF is not mistaken for a moved base.
FINGERPRINT = '4a6f46738f0bd86d641d64bf10d2cdb5'

# This file legitimately contains U+2032 PRIME (the "B-prime" architecture
# name, 22 times) and one U+2033 DOUBLE PRIME.  They are NOT normalized:
# the encoding gate is scoped to delivered code, these are prose
# typography, and Section 5a already spells the same name with an ASCII
# apostrophe.  Everything this patch INSERTS is ASCII, and the script
# asserts that.


# ==================================================================
# EDIT 1 -- header Status line: the braid
# ==================================================================

OLD_01 = (
    "**Status:** v18 -- Phase 2 (solar system assembler) BUILD UNDERWAY. Design\n"
)
NEW_01 = (
    "**Status:** v19 -- Phase 2 (solar system assembler) BUILD UNDERWAY.\n"
    "**The braid, ruled 2026-08-22:** provenance stops being a GATE and\n"
    "becomes a per-artifact slice, and the rendering layer is worked first.\n"
    "The five segments of Section 5a do NOT move; the order they are worked\n"
    "in does. Argument in\n"
    "`documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`\n"
    "Section 1. Design\n"
)


# ==================================================================
# EDIT 2 -- L-120 is DONE
# ==================================================================

OLD_02 = (
    "July 21-22); L-119/L-120/L-121/L-122 still OPEN, none built yet.\n"
)
NEW_02 = (
    "July 21-22); L-120 (F3, Halley in the served index) DONE 2026-07-27;\n"
    "L-119, L-121 and L-122 still OPEN.\n"
)


# ==================================================================
# EDIT 3 -- base block, L-151, and an internal contradiction
# ==================================================================

OLD_03 = (
    "**Base:** orrery @ `c10a424`, gallery @ `e864fd42` (design ratified here;\n"
    "Artifact 1 built+pushed at orrery `6fc52b9a` / gallery `f89d83c4`; current\n"
    "state as of that work, orrery `ee0da47c` / gallery `61a78c00` -- F1a (M2)\n"
    "fully closed: L-149\n"
    "and L-118 both DONE, Layer 2 Steps 1-5 passed live; Layer 3 enabled with a\n"
    "known open issue; L-150 (multi-orbit binaries) and L-151 (gallery-assembler\n"
    "skill) still decided, not yet built)\n"
    "**Date begun:** July 3, 2026\n"
    "**Last updated:** August 7, 2026\n"
)
NEW_03 = (
    "**Base:** orrery @ `38923c1`, gallery @ `493a0bd` (v19; both confirmed\n"
    "against the live remote, not carried forward. Design ratified at orrery\n"
    "`c10a424` / gallery `e864fd42`; Artifact 1 built+pushed at orrery\n"
    "`6fc52b9a` / gallery `f89d83c4`; v18 stood at orrery `ee0da47c` /\n"
    "gallery `61a78c00`. F1a (M2) fully closed: L-149 and L-118 both DONE,\n"
    "Layer 2 Steps 1-5 passed live. Layer 3 RETIRED 2026-08-10 -- the v18\n"
    "text here read \"enabled with a known open issue\", contradicting its own\n"
    "header forty lines below. L-151 (gallery-assembler skill) DONE\n"
    "2026-07-27; L-150 (multi-orbit binaries) still decided, not yet built.)\n"
    "**Date begun:** July 3, 2026\n"
    "**Last updated:** August 22, 2026\n"
)


# ==================================================================
# EDIT 4 -- Section 1, gallery size measured once
# ==================================================================

OLD_04 = (
    "**GitHub Pages hosting.** The gallery is ~436 MB against Pages' 1 GB ceiling,\n"
    "with ~588 MB of headroom (post-cleanup, July 2026). The largest remaining\n"
)
NEW_04 = (
    "**GitHub Pages hosting.** The gallery is 439 MB against Pages' 1 GB ceiling,\n"
    "with ~585 MB of headroom (measured at gallery `493a0bd`, 2026-08-22;\n"
    "~436 MB post-cleanup in July 2026). This is the document's ONE size\n"
    "figure -- Section 3a used to carry a second, disagreeing one. The largest remaining\n"
)


# ==================================================================
# EDIT 5 -- Section 2 seam 2: the reason was false, the seam is real
# ==================================================================

OLD_05 = (
    "2. `palomas_orrery_helpers.py` -- imports tkinter directly and carries\n"
    "   computation the assembler will want. Fix: split computation from GUI helpers\n"
    "   (L-087).\n"
)
NEW_05 = (
    "2. `palomas_orrery_helpers.py` -- carries computation the assembler will\n"
    "   want. **L-087 CLOSED 2026-07-15 and the file no longer imports tkinter\n"
    "   at all** (measured at `38923c1`: zero references; all three functions\n"
    "   the assembler needs are present). The seam survives in a different\n"
    "   shape: three modules in its TRANSITIVE import closure still import\n"
    "   tkinter -- `osculating_cache_manager`, `save_utils`, `shutdown_handler`.\n"
    "   So the constraint is real and the reason v18 gave for it was not.\n"
)


# ==================================================================
# EDIT 6 -- Section 3a: stop carrying a second size figure
# ==================================================================

OLD_06 = (
    "origin by construction -- no CORS question. Gallery measured at 474 MB with\n"
    "526 MB headroom against the 1 GB GitHub Pages soft limit; all-phase data\n"
    "needs are ~72 MB (14% of remaining). Pre-heavy gallery JSONs are cullable\n"
)
NEW_06 = (
    "origin by construction -- no CORS question. Gallery size and headroom are\n"
    "stated ONCE, in Section 1, and measured there; all-phase data needs are\n"
    "~72 MB. Pre-heavy gallery JSONs are cullable\n"
)


# ==================================================================
# EDIT 7 -- Section 3a: L-108 closed
# ==================================================================

OLD_07 = (
    "> authoritative. Full section-3a rewrite tracked as L-108.\n"
)
NEW_07 = (
    "> authoritative. The full section-3a rewrite was tracked as L-108, which\n"
    "> CLOSED 2026-07-12.\n"
)


# ==================================================================
# EDIT 8 -- OQ-E defers to Section 1 for size
# ==================================================================

OLD_08 = (
    "  measured at 474 MB, 526 MB headroom, all-phase data needs ~72 MB. No\n"
)
NEW_08 = (
    "  size and headroom per Section 1; all-phase data needs ~72 MB. No\n"
)


# ==================================================================
# EDIT 9 -- Section 4a line count
# ==================================================================

OLD_09 = (
    "**Desktop GUI:** `palomas_orrery.py` (11,110 lines at HEAD). `plot_objects` and\n"
)
NEW_09 = (
    "**Desktop GUI:** `palomas_orrery.py` (11,092 lines at `38923c1`). `plot_objects` and\n"
)


# ==================================================================
# EDIT 10 -- Phase 2 "Requires": L-087 is discharged
# ==================================================================

# The PRIME (U+2032) below is written as an escape so this script's own
# bytes stay pure ASCII while still matching -- and re-emitting -- the
# character the document already carries (safe-file-editing 1.7, "The
# patch script's own bytes are also in scope").
OLD_10 = (
    "Requires: helpers split (L-087), Phase 1b data pipeline. Architecture B"
    "\u2032\n"
)
NEW_10 = (
    "Requires: Phase 1b data pipeline (done). The helpers split (L-087) is\n"
    "DISCHARGED -- closed 2026-07-15; see Section 2, seam 2, for what\n"
    "remains transitively. Architecture B\u2032\n"
)


# ==================================================================
# EDIT 11 -- Section 5 Phase 2 track table: superseded-by pointer
# ==================================================================

OLD_11 = (
    "**This supersedes the August 5 instruction** that all provenance batches\n"
    "clear before Artifact 2 proceeds. That instruction is not withdrawn --\n"
    "batches still precede the artifact -- but Track 0 now precedes the\n"
    "batches. Recorded as a deliberate reversal, not a drift.\n"
)
NEW_11 = (
    "**This supersedes the August 5 instruction** that all provenance batches\n"
    "clear before Artifact 2 proceeds. That instruction is not withdrawn --\n"
    "batches still precede the artifact -- but Track 0 now precedes the\n"
    "batches. Recorded as a deliberate reversal, not a drift.\n"
    "\n"
    "**Narrowed 2026-08-22 by the braid (Section 5a).** Track 1's exit\n"
    "condition above reads \"Batch 2 gas giants verified\", which is Jupiter,\n"
    "Saturn, Uranus and Neptune. What Artifact 2 needs is a SUBSET of that:\n"
    "Saturn's rings, Jupiter's rings, and Jupiter's belts. Uranus and Neptune\n"
    "are not in Artifact 2 and do not gate it. The table is left as written\n"
    "because it is the record of the August ruling; the scope that applies to\n"
    "Artifact 2 is the one in Section 5a.\n"
)


# ==================================================================
# EDIT 12 -- Section 5a: the amendment paragraph
# ==================================================================

OLD_12 = (
    "This section is the spine. Detail lives in Sections 5, 6 and 7; history\n"
    "of every ruling stays in Section 6. When 5a and another section\n"
    "disagree, 5a is the one that was rewritten last -- reconcile, do not\n"
    "guess.\n"
)
NEW_12 = (
    "**Amended 2026-08-22 at `38923c1` -- the braid.** Provenance stops being\n"
    "a GATE and becomes a per-artifact slice, and segment 3 is worked first.\n"
    "The five segments below do NOT move: they are the SHAPE of the work and\n"
    "they were confirmed unchanged on 2026-08-16. What moved is the order\n"
    "they are worked in and the scope segment 1 must reach before an artifact\n"
    "can lock. The argument, with its reasoning, is in\n"
    "`documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`\n"
    "Section 1; the short form is that a precondition which does not\n"
    "terminate is not a plan.\n"
    "\n"
    "This section is the spine. Detail lives in Sections 5, 6 and 7; history\n"
    "of every ruling stays in Section 6. When 5a and another section\n"
    "disagree, 5a is the one that was rewritten last -- reconcile, do not\n"
    "guess.\n"
)


# ==================================================================
# EDIT 13 -- Section 5a: the claim the braid overturns
# ==================================================================

OLD_13 = (
    "That asymmetry is why the provenance refactor precedes the assembler\n"
    "work rather than running beside it. Its target is the ORRERY, so that\n"
    "importing from it blind is safe.\n"
)
NEW_13 = (
    "That asymmetry is why the provenance work exists and why its target is\n"
    "the ORRERY. Until 2026-08-22 this paragraph drew a second conclusion\n"
    "from it -- that the refactor must PRECEDE the assembler work rather than\n"
    "run beside it -- and that conclusion is withdrawn.\n"
    "\n"
    "The asymmetry governs what an artifact may LOCK, not what may be BUILT.\n"
    "A fingerprinted artifact freezes its values, so it must not be locked on\n"
    "unsourced ones. Drawing a ring freezes nothing.\n"
    "\n"
    "And the order pays for itself, because the render is this project's own\n"
    "ground truth. Ring provenance today is an audit of numbers nobody can\n"
    "see -- text checked against text, which is precisely the mode that\n"
    "produced three separate failures on 2026-08-22. Once the assembler\n"
    "draws, a wrong ring radius becomes something Tony's EYES can catch.\n"
    "Segment 3 is what gives the provenance work a render to be checked\n"
    "against.\n"
)


# ==================================================================
# EDIT 14 -- Section 5a segment 1: the slice, counted
# ==================================================================

OLD_14 = (
    "**Segment 1 -- Make the orrery right.** Track 0 (L-181): one store for\n"
    "feature constants, provenance carried as data, display text derived.\n"
    "Track 1 (L-156): the provenance batches, Batch 2 gas giants being the\n"
    "one Artifact 2 needs. The worksheet checker, the request builder, the\n"
    "key rule and the dispatch loop (L-192) are the MACHINERY of Track 1, not\n"
    "a phase of their own -- they are how 102 annotations get reconciled at\n"
    "scale instead of by hand.\n"
)
NEW_14 = (
    "**Segment 1 -- Make the orrery right.** Track 0 (L-181): one store for\n"
    "feature constants, provenance carried as data, display text derived.\n"
    "Track 1 (L-156): the provenance batches. The worksheet checker, the\n"
    "request builder, the key rule and the dispatch loop (L-192) are the\n"
    "MACHINERY of Track 1, not a phase of their own -- they are how the\n"
    "annotations get reconciled at scale instead of by hand.\n"
    "\n"
    "**Scoped per artifact, since 2026-08-22.** This segment as a whole does\n"
    "not gate anything. What gates Artifact 2 is the slice Artifact 2\n"
    "RENDERS, and that slice is countable, which is the whole point of\n"
    "scoping it this way. Measured in the served cache at gallery\n"
    "`493a0bd`: Saturn's seven rings carry `inner_radius_km` and\n"
    "`outer_radius_km`; Jupiter's four rings add `thickness_km`; the belts\n"
    "carry `belt_distances` (three values) and `belt_thickness`. **Thirty\n"
    "measured numbers.** `n_rings` and `n_points` are drawing parameters --\n"
    "DECLARED under Section 7 decision 18, and not findings.\n"
    "\n"
    "The general audit does not stop. It stops being a gate. This is \"The\n"
    "Artifact Bounds the Audit\" (PROJECT_INSTRUCTIONS.md, Part 3) extended by\n"
    "one word: that rule bounds WHICH values are in scope, and this bounds\n"
    "which are in scope NEXT.\n"
)


# ==================================================================
# EDIT 15 -- Section 5a segment 4: Saturn has no belts
# ==================================================================

OLD_15 = (
    "**Segment 4 -- Lock Artifact 2.** Needs all three. A golden artifact is\n"
    "fingerprinted, so locking one on values that are not yet sourced means\n"
    "redoing the lock rather than editing a number (Tony, August 2026). And\n"
    "an artifact defined as *Jupiter and Saturn with rings and radiation\n"
    "belts* cannot be Mode 5 accepted while nothing renders them.\n"
)
NEW_15 = (
    "**Segment 4 -- Lock Artifact 2.** A golden artifact is fingerprinted, so\n"
    "locking one on values that are not yet sourced means redoing the lock\n"
    "rather than editing a number (Tony, August 2026). And an artifact\n"
    "defined as *Jupiter and Saturn with rings and radiation belts* cannot be\n"
    "Mode 5 accepted while nothing renders them.\n"
    "\n"
    "One precision, measured 2026-08-22: **Saturn has no radiation belts** in\n"
    "the served cache or in `objects_config.json`. Only Jupiter's are served.\n"
    "The phrase above reads as though both bodies have them.\n"
)


# ==================================================================
# EDIT 16 -- Section 5a: the order of execution
# ==================================================================

OLD_16 = (
    "**Segment 5 -- Ship the Phase 2 page**, then Phase 3 stars, Phase 4\n"
    "exoplanets and Sgr A*, Phase 5 Earth system. Phase 6 dissolves into\n"
    "continuous refinement (Section 5).\n"
)
NEW_16 = (
    "**Segment 5 -- Ship the Phase 2 page**, then Phase 3 stars, Phase 4\n"
    "exoplanets and Sgr A*, Phase 5 Earth system. Phase 6 dissolves into\n"
    "continuous refinement (Section 5).\n"
    "\n"
    "### The order of execution -- amended 2026-08-22\n"
    "\n"
    "The five segments above are the SHAPE: what depends on what. They are\n"
    "unchanged. This is the ORDER they are worked in, which is not the same\n"
    "thing and which the braid changed.\n"
    "\n"
    "1. **Segment 3** -- the rendering layer. Two lines in `resolver.py` plus\n"
    "   a type, then the client feature renderers (L-154). Saturn on screen,\n"
    "   unfingerprinted. This depends on NOTHING: the data is already served.\n"
    "2. **Segment 1, sliced to Artifact 2** -- the thirty measured numbers\n"
    "   above, and only those.\n"
    "3. **Segment 4** -- lock Artifact 2.\n"
    "4. **Segment 5** -- ship.\n"
    "\n"
    "Segment 2 (the transport) is not in that list because it is not on the\n"
    "path to Artifact 2 rendering; it is what stops a correct orrery drifting\n"
    "from its copy afterwards.\n"
    "\n"
    "**A consequence to record rather than resolve here:** L-154 is BLOCKED\n"
    "in the ledger, and this order unblocks it. The plan carries SEQUENCING\n"
    "authority and the ledger carries STATUS authority (L-221), so that is a\n"
    "ledger edit, not something this section may assert around.\n"
)


# ==================================================================
# EDIT 17 -- Section 5a "You are here": restamp and re-measure
# ==================================================================

OLD_17 = (
    "### You are here -- 2026-08-19, orrery `9ffb9b4`, gallery `ff18d3e`\n"
)
NEW_17 = (
    "### You are here -- 2026-08-22, orrery `38923c1`, gallery `493a0bd`\n"
)

OLD_18 = (
    "| Segment 1, orrery | IN PROGRESS. Track 0 has no open rulings. "
    "The reconciliation is measured: 110 annotations scored, **8 clean**, "
    "48 SEND BACK, 20 CONVERSATION, 34 noted, 24 not scanner-reachable. "
    "The corpus grew and the clean count tripled because L-198 taught the "
    "scanner units it could not read -- coverage, not regression. Dispatch "
    "machinery COMPLETE as of August 18; 8 of the 9 August-16 blockers "
    "closed, the 9th (ordinal context window) deliberately unexercised by "
    "the pilot. **The first dispatch went out and returned on August 18**: "
    "23 rows to three models, 69 answered rows, zero format defects, all "
    "three trap rows unsprung. Findings at L-209, L-210, L-211; evidence in "
    "`documentation/PILOT_CONVERGENCE_20260819.md`. |\n"
)
NEW_18 = (
    "| Segment 1, orrery | IN PROGRESS, and **no longer a gate** (the braid, "
    "2026-08-22). Track 0 has no open rulings. Re-measured at `38923c1` from "
    "`WORKSHEET_CHECK.md`: 105 annotations scored, **8 clean**, 47 SEND "
    "BACK, 19 CONVERSATION, 31 noted, 22 not scanner-reachable; 292 Tier-1 "
    "findings tree-wide. (v18 reported 110/8/48/20/34/24, read on "
    "2026-08-19.) The corpus grew and the clean count tripled because L-198 "
    "taught the scanner units it could not read -- coverage, not "
    "regression. Dispatch machinery COMPLETE as of August 18; 8 of the 9 "
    "August-16 blockers closed, the 9th (ordinal context window) "
    "deliberately unexercised by the pilot. **The first dispatch went out "
    "and returned on August 18**: 23 rows to three models, 69 answered "
    "rows, zero format defects, all three trap rows unsprung. Findings at "
    "L-209, L-210, L-211; evidence in "
    "`documentation/PILOT_CONVERGENCE_20260819.md`. |\n"
)

OLD_19 = (
    "| Segment 3, assembler draw | NOT STARTED. Two lines plus a type, then the renderers. Now the only item anywhere with no ruling outstanding and no dependency on the provenance work. |\n"
    "| Segment 4, Artifact 2 | Gated on 1-3. |\n"
)
NEW_19 = (
    "| Segment 3, assembler draw | NOT STARTED, and **now the next work**. Verified at gallery `493a0bd`: `resolver.py:133` still reduces the feature dict to its keys (`tuple(rec.get(\"features\") or ())`), `models.py:91` still types the field `Tuple[str, ...]` to match, and NOTHING in the gallery repo reads `feature_configs.json` -- only the builder writes it. |\n"
    "| Segment 4, Artifact 2 | Gated on segment 3 and on segment 1's thirty-number slice. Not on the general audit. |\n"
)


# ==================================================================
# EDIT 20 -- Section 6: L-162 is DONE
# ==================================================================

OLD_20 = (
    "**L-162 -- CENTER_BODY_RADII de-duplication.** [ ] Not started, scoped, now\n"
    "with its own ledger entry (previously design-doc only). Promote 15\n"
)
NEW_20 = (
    "**L-162 -- CENTER_BODY_RADII de-duplication.** [x] **DONE 2026-07-29.**\n"
    "The description below is preserved as the scope that was executed; it\n"
    "read \"[ ] Not started\" through v18. Promote 15\n"
)


# ==================================================================
# EDIT 21 -- Section 6: the helpers split is done
# ==================================================================

OLD_21 = (
    "**`palomas_orrery_helpers.py` split** -- [ ] Not started. Separate computation\n"
    "from tkinter GUI helpers. Computation the assembler needs:\n"
    "`calculate_planet9_position_on_orbit`, `rotate_points2`,\n"
    "`calculate_axis_range`. Required before Phase 2.\n"
)
NEW_21 = (
    "**`palomas_orrery_helpers.py` split** -- [x] **DONE 2026-07-15 (L-087).**\n"
    "Verified at `38923c1`: the file holds zero tkinter references, and all\n"
    "three functions the assembler needs are present --\n"
    "`calculate_planet9_position_on_orbit`, `rotate_points2`,\n"
    "`calculate_axis_range`. Residual, not a re-open: three modules in its\n"
    "transitive import closure still import tkinter\n"
    "(`osculating_cache_manager`, `save_utils`, `shutdown_handler`).\n"
)


# ==================================================================
# EDIT 22 -- Section 6: L-154's unblocking is the braid's, and the ledger's
# ==================================================================

OLD_22 = (
    "L-154 unblocks once the scanner work closes.\n"
)
NEW_22 = (
    "L-154 unblocks once the scanner work closes. **Superseded 2026-08-22 by\n"
    "the braid (Section 5a):** L-154 is the rendering layer and is now the\n"
    "FIRST work, not work waiting on the scanner. Its ledger status still\n"
    "reads BLOCKED; the ledger is the status authority, so that edit belongs\n"
    "there and not here.\n"
)


# ==================================================================
# EDIT 23 -- Section 7 decision 12: the open count, resolved by looking
# ==================================================================

OLD_23 = (
    "    **Count correction, 2026-08-11.** Measured at HEAD: 49 assignments, 6\n"
    "    derived. The plan read 7 of 45. The 45-to-49 gap is exactly the four\n"
    "    L-179/L-180 additions, so that half was stale rather than wrong. The\n"
    "    constructor-call count is a genuine open question rather than a\n"
    "    correction: the plan says two, measurement finds one\n"
    "    (`HORIZONS_MAX_DATE = datetime(...)`), with no calls nested inside any\n"
    "    of the six derived expressions -- and staleness explains a count going\n"
    "    UP, not down. Resolve by looking, not by patching. The argument\n"
    "    against `ast` is unaffected either way; one non-evaluable constructor\n"
    "    is as fatal to it as two.\n"
)
NEW_23 = (
    "    **Count correction, 2026-08-11.** Measured at HEAD: 49 assignments, 6\n"
    "    derived. The plan read 7 of 45. The 45-to-49 gap is exactly the four\n"
    "    L-179/L-180 additions, so that half was stale rather than wrong. The\n"
    "    constructor-call count was left as an open question -- the plan said\n"
    "    two, that measurement found one -- with the instruction to resolve it\n"
    "    by looking, not by patching.\n"
    "    **Resolved by looking, 2026-08-22 at `38923c1`: TWO is right.**\n"
    "    `constants_new.py` holds 48 top-level assignments; the six arithmetic\n"
    "    derivations are unchanged; and TWO assignments contain constructor\n"
    "    calls -- `HORIZONS_MAX_DATE = datetime(...)` at line 141, and\n"
    "    `stellar_class_labels` at line 902, which holds twelve `dict()` calls\n"
    "    inside a list of label specifications. The August 11 count missed the\n"
    "    second because it looked only inside the derived expressions. The\n"
    "    argument against `ast` is unaffected either way; one non-evaluable\n"
    "    constructor is as fatal to it as two.\n"
)


# ==================================================================
# EDIT 24 -- Section 7 decision 16: the ring count, confirmed
# ==================================================================

OLD_24 = (
    "    below is what Tony ruled on, and it stands as written except for one\n"
    "    number: it says Jupiter has 5 entries, and the August 10 session\n"
    "    counted 4 ring entries. Confirm before the pilot starts, since the\n"
    "    pilot is scoped by it.\n"
)
NEW_24 = (
    "    below is what Tony ruled on, and it stands as written except for one\n"
    "    number: it says Jupiter has 5 entries, and the August 10 session\n"
    "    counted 4 ring entries.\n"
    "    **Confirmed 2026-08-22: FOUR.** `main_ring`, `halo_ring`,\n"
    "    `amalthea_gossamer`, `thebe_gossamer` -- identical in\n"
    "    `objects_config.json` and in the served `feature_configs.json` at\n"
    "    gallery `493a0bd`. The \"5 entries\" in the recommendation below is\n"
    "    wrong and is left in place because it is a quotation of what was\n"
    "    ruled on.\n"
)


# ==================================================================
# EDIT 25 -- Section 10: a citation to a file that does not exist
# ==================================================================

OLD_25 = (
    "  OQ-i through OQ-v for Phase 2 start. (`AB_FORK_ANALYSIS.md`, built on\n"
    "  `873c6cd` / `827d0b3`.)\n"
)
NEW_25 = (
    "  OQ-i through OQ-v for Phase 2 start. (`AB_FORK_ANALYSIS.md`, built on\n"
    "  `873c6cd` / `827d0b3` -- **that file is in NEITHER repo as of\n"
    "  2026-08-22**, and no near-match name exists. The lineage entry stays\n"
    "  because the analysis happened and its results are recorded above; the\n"
    "  gap is noted rather than the citation quietly dropped.)\n"
)


# ==================================================================
# EDIT 26 -- Section 10: New in v19
# ==================================================================

OLD_26 = (
    "  it explicitly did not perform. Now carried in\n"
    "  provenance-discipline v2.3.\n"
    "\n"
    "---\n"
    "\n"
    "## Section 11 -- Protocol & Skills Review (from Phase 0)\n"
)
NEW_26 = (
    "  it explicitly did not perform. Now carried in\n"
    "  provenance-discipline v2.3.\n"
    "\n"
    "*New in v19 (August 22, 2026):*\n"
    "- **The braid: provenance stops being a gate and becomes a per-artifact\n"
    "  slice** (Tony's ruling, 2026-08-22). Step one of the critical path had\n"
    "  8 clean rows of 105 and 292 Tier-1 findings tree-wide, and a full\n"
    "  session on 2026-08-22 went to ONE solar shell that is not in Artifact 2\n"
    "  and does not block it. A precondition that does not terminate is not a\n"
    "  plan. Priority becomes what the NEXT ARTIFACT renders -- for Artifact 2,\n"
    "  thirty measured numbers. The five segments of Section 5a do not move;\n"
    "  the order they are worked in does, and segment 3 goes first.\n"
    "- **The load-bearing half is the render.** Ring provenance today is text\n"
    "  checked against text. Once the assembler draws, a wrong ring radius is\n"
    "  something Tony's eyes can catch -- and the resident gate already says\n"
    "  the render wins when it disagrees with a code reading. Building the\n"
    "  rendering layer is what gives the provenance work something to be\n"
    "  checked against. Rings can be drawn without being fingerprinted;\n"
    "  BUILDING and LOCKING are separable and v18 conflated them.\n"
    "- **A full-document sweep, not a section edit.** Every numeric and status\n"
    "  claim in this file was measured against HEAD rather than read forward,\n"
    "  and 63 file references were resolved against both repos. Twenty-nine\n"
    "  items had moved. The pattern in them is worth more than the list: five\n"
    "  ledger items the plan called open had closed (L-087, L-108, L-120,\n"
    "  L-151, L-162), one stated REASON was false while its conclusion held\n"
    "  (the helpers seam), two size figures disagreed inside one document, and\n"
    "  two questions the plan told a future session to resolve by looking were\n"
    "  answered by looking.\n"
    "- **The skill-version list is deleted, not updated** (Tony's ruling,\n"
    "  2026-08-22). The closing block restated ten skill versions by hand and\n"
    "  five had drifted, provenance-discipline worst at 1.8 against an actual\n"
    "  2.6. It is a second store for a value the protocol's generated Skill\n"
    "  Manifest already owns, and Stale Skill = Stop compares against that\n"
    "  manifest, not against this document. Fix the producer, not N consumers.\n"
    "- **An unmatched code fence removed.** The file carried five ``` markers,\n"
    "  an odd count; the last opened a block that never closed.\n"
    "- **Two consequences recorded rather than resolved here.** L-225 has no\n"
    "  ledger entry although the design note and the session queue both cite\n"
    "  it; and L-154 is ledger-BLOCKED while this plan now makes it the first\n"
    "  work. The plan carries sequencing authority and the ledger carries\n"
    "  status authority (L-221), so both are ledger edits.\n"
    "\n"
    "---\n"
    "\n"
    "## Section 11 -- Protocol & Skills Review (from Phase 0)\n"
)


# ==================================================================
# EDIT 27 -- Section 11: that skill update landed
# ==================================================================

OLD_27 = (
    "- `gallery-pipeline` v1.1: Option C viewer, consent gate, two-tier model,\n"
    "  `interactive.html` conventions, `?exhibit=` parameter.\n"
    "- Decide: separate `pyodide-interactive` skill or extend `gallery-pipeline`.\n"
)
NEW_27 = (
    "- `gallery-pipeline` v1.1: Option C viewer, consent gate, two-tier model,\n"
    "  `interactive.html` conventions, `?exhibit=` parameter. **LANDED** -- the\n"
    "  skill is at 1.2.\n"
    "- Decide: separate `pyodide-interactive` skill or extend `gallery-pipeline`.\n"
    "  Still open.\n"
)


# ==================================================================
# EDIT 28 -- the closing block: restamp, kill the shadow store, close
#            the stray fence
# ==================================================================

OLD_28 = (
    "Base: orrery @ `ee0da47` / gallery @ `61a78c0` (v17; v16 was orrery\n"
    "`4b82384` / gallery `e7e8c5e`; v15 was orrery\n"
    "`b59cb72` / gallery `22c947c9`).\n"
)
NEW_28 = (
    "Base: orrery @ `38923c1` / gallery @ `493a0bd` (v19, confirmed against\n"
    "the live remote; v17-v18 stood at orrery `ee0da47` / gallery `61a78c0`;\n"
    "v16 was orrery `4b82384` / gallery `e7e8c5e`; v15 was orrery\n"
    "`b59cb72` / gallery `22c947c9`).\n"
)

OLD_29 = (
    "Track 1 Batch 1 COMPLETE -- three-model competitive cross-check of 5 shell\n"
    "modules + Mars, geometry follow-up, Fable consistency audit. Phase 2\n"
    "Track 1 Batch 2 NEXT: gas giants (jupiter, saturn, uranus, neptune)\n"
    "-- and the stated gate before Artifact 2. Push gate for this phase:\n"
)
NEW_29 = (
    "Track 1 Batch 1 COMPLETE -- three-model competitive cross-check of 5 shell\n"
    "modules + Mars, geometry follow-up, Fable consistency audit. Phase 2\n"
    "Track 1 Batch 2 (gas giants: jupiter, saturn, uranus, neptune) is NO\n"
    "LONGER the gate before Artifact 2 -- the braid narrowed that gate on\n"
    "2026-08-22 to the slice Artifact 2 renders (Section 5a). Push gate for\n"
    "this phase:\n"
)

OLD_30 = (
    "New structural items from Fable audit: L-176 (illustrated dimensions in\n"
    "hover text), L-177 (Mercury Hill sphere convention), L-178-180\n"
    "(Earth/solar inconsistencies), L-181 (single-source-of-truth constant\n"
    "layer). Skill updates LANDED 2026-08-05: all ten skills bumped and reconciled\n"
    "across repo, manifest, and account install --\n"
    "orrery-coding-conventions 1.3, provenance-discipline 1.8,\n"
    "ledger-and-session-records 1.5, safe-file-editing 1.3,\n"
    "agentic-pre-test 1.2, gallery-pipeline 1.2, gallery-assembler 1.1,\n"
    "gallery-cache-builder 1.3, horizons-orbital-mechanics 1.1,\n"
    "earth-system-pipeline 1.1. Protocol at v3.37.\n"
    "(Versions above current as of 2026-08-11: safe-file-editing 1.2 -> 1.3\n"
    "Aug 7; provenance-discipline 1.7 -> 1.8 and gallery-cache-builder\n"
    "1.2 -> 1.3 Aug 11; protocol v3.34 -> v3.37 Aug 8-11. All three stores\n"
    "reconciled -- repo, manifest, account install.)\n"
)
NEW_30 = (
    "New structural items from Fable audit: L-176 (illustrated dimensions in\n"
    "hover text), L-177 (Mercury Hill sphere convention), L-178-180\n"
    "(Earth/solar inconsistencies), L-181 (single-source-of-truth constant\n"
    "layer).\n"
    "\n"
    "SKILL AND PROTOCOL VERSIONS ARE NOT RESTATED HERE. This block used to\n"
    "carry ten of them by hand; five had drifted by 2026-08-22 and nothing\n"
    "watched them. The authority is the generated Skill Manifest in\n"
    "`PROJECT_INSTRUCTIONS.md`, Part 3 -- rebuilt by `skills_index.py`, and\n"
    "the copy Stale Skill = Stop actually compares a loaded skill against.\n"
    "Read it there. (Tony's ruling, 2026-08-22: fix the producer, not N\n"
    "consumers.)\n"
)

OLD_31 = (
    "Solar System Explorer live at palomasorrery.com/interactive.html.\n"
    "```\n"
)
NEW_31 = (
    "Solar System Explorer live at palomasorrery.com/interactive.html.\n"
)


# ==================================================================
# EDIT 32 -- two headings about "order" would now say different things
# ==================================================================
# Introduced by edit 16: "The path, in order" (dependency shape) and
# "The order of execution" (what is worked first) are not the same
# claim, and a reader meeting both is entitled to be confused. The
# segments themselves do not move; only the heading changes.

# ==================================================================
# EDIT 33 -- the closing block still called L-151 unbuilt
# ==================================================================
# Edit 03 corrected the header; this is the same claim forty lines
# further down, and a document that disagrees with itself is worse
# than one that is uniformly stale.

OLD_33 = (
    "fully tested and closed -- L-149 and L-118 both DONE; L-150/L-151 still\n"
    "decided, not built.\n"
)
NEW_33 = (
    "fully tested and closed -- L-149 and L-118 both DONE; L-151 DONE\n"
    "2026-07-27; L-150 still decided, not built.\n"
)


# ==================================================================
# EDIT 34 -- "next AFTER scanner work" is what the braid overturns
# ==================================================================

OLD_34 = (
    "Next after scanner work: write the feature-rendering JS layer\n"
    "(ring/shell/belt consumers) -- that's what stands between here and\n"
    "attempting Artifact 2 (Jupiter/Saturn) Mode 5. Layer 3 (nightly Task\n"
)
NEW_34 = (
    "NEXT, and no longer waiting on the scanner work (the braid,\n"
    "2026-08-22): write the feature-rendering JS layer (ring/shell/belt\n"
    "consumers). It is what stands between here and attempting Artifact 2\n"
    "(Jupiter/Saturn) Mode 5, it depends on nothing, and the data it needs\n"
    "is already served. Layer 3 (nightly Task\n"
)


OLD_32 = (
    "### The path, in order\n"
)
NEW_32 = (
    "### The path -- the five segments\n"
    "\n"
    "What depends on what. The segments are numbered by DEPENDENCY, not by\n"
    "the order they are worked in -- that is the subsection after this one,\n"
    "and since 2026-08-22 the two are different.\n"
)


# ==================================================================
# The edit table
# ==================================================================

EDITS = [
    ('01 header Status line -- the braid', OLD_01, NEW_01),
    ('02 L-120 is DONE', OLD_02, NEW_02),
    ('03 base block, L-151, Layer 3 contradiction', OLD_03, NEW_03),
    ('04 S1 gallery size, measured once', OLD_04, NEW_04),
    ('05 S2 seam 2 -- the reason was false', OLD_05, NEW_05),
    ('06 S3a second size figure removed', OLD_06, NEW_06),
    ('07 S3a L-108 closed', OLD_07, NEW_07),
    ('08 OQ-E defers to S1 for size', OLD_08, NEW_08),
    ('09 S4a line count 11,110 -> 11,092', OLD_09, NEW_09),
    ('10 Phase 2 Requires -- L-087 discharged', OLD_10, NEW_10),
    ('11 Phase 2 track table -- narrowed by the braid', OLD_11, NEW_11),
    ('12 S5a amendment paragraph', OLD_12, NEW_12),
    ('13 S5a -- the claim the braid overturns', OLD_13, NEW_13),
    ('14 S5a segment 1 -- the slice, counted', OLD_14, NEW_14),
    ('15 S5a segment 4 -- Saturn has no belts', OLD_15, NEW_15),
    ('16 S5a -- the order of execution', OLD_16, NEW_16),
    ('17 S5a You-are-here heading restamped', OLD_17, NEW_17),
    ('18 S5a segment 1 row re-measured', OLD_18, NEW_18),
    ('19 S5a segment 3 and 4 rows', OLD_19, NEW_19),
    ('20 S6 L-162 is DONE', OLD_20, NEW_20),
    ('21 S6 helpers split is DONE', OLD_21, NEW_21),
    ('22 S6 L-154 superseded by the braid', OLD_22, NEW_22),
    ('23 S7 d12 -- constructor count resolved: two', OLD_23, NEW_23),
    ('24 S7 d16 -- Jupiter ring count confirmed: four', OLD_24, NEW_24),
    ('25 S10 AB_FORK_ANALYSIS.md is missing', OLD_25, NEW_25),
    ('26 S10 New in v19', OLD_26, NEW_26),
    ('27 S11 gallery-pipeline 1.1 landed', OLD_27, NEW_27),
    ('28 closing base SHAs', OLD_28, NEW_28),
    ('29 closing -- Batch 2 is no longer the gate', OLD_29, NEW_29),
    ('30 closing -- skill-version shadow store deleted', OLD_30, NEW_30),
    ('31 closing -- unmatched code fence removed', OLD_31, NEW_31),
    ('32 S5a heading -- shape vs execution order', OLD_32, NEW_32),
    ('33 closing -- L-151 is DONE (header already said so)', OLD_33, NEW_33),
    ('34 closing -- the JS layer is first, not "after"', OLD_34, NEW_34),
]


def fail(message):
    print('')
    print('ERROR: ' + message)
    print('Nothing was written. The file on disk is untouched.')
    sys.exit(1)


def main():
    target = os.path.join(HERE, TARGET_NAME)
    print('patch_L221_2_master_plan_v19.py')
    print('built on %s' % BASE_SHA)
    print('gallery  %s' % GALLERY_SHA)
    print('target   %s' % target)
    print('')

    if not os.path.exists(target):
        fail('%s not found beside this script. Save the script into '
             'documentation/ and run it again.' % TARGET_NAME)

    with open(target, 'rb') as handle:
        raw = handle.read()

    # --- Gate 1: is this the file we built against? ------------------
    normalized = raw.replace(b'\r\n', b'\n')
    got = hashlib.md5(normalized).hexdigest()
    if got != FINGERPRINT:
        fail('BASE MOVED. %s fingerprints %s; this patch was built against '
             '%s. Re-pull at HEAD, or ask for a rebuilt patch.'
             % (TARGET_NAME, got, FINGERPRINT))
    print('[base ok]      fingerprint %s (%d bytes)' % (got, len(raw)))

    is_crlf = b'\r\n' in raw
    print('[endings]      %s -- preserved on write'
          % ('CRLF' if is_crlf else 'LF'))

    # --- Gate 2: this patch may PRESERVE non-ASCII, never INTRODUCE it
    # A blunt "new must be pure ASCII" test would refuse an anchor that
    # simply carries a character the document already holds. The honest
    # test is that no edit raises the count.
    carried = 0
    for label, old, new in EDITS:
        old_n = sum(1 for ch in old if ord(ch) > 127)
        new_n = sum(1 for ch in new if ord(ch) > 127)
        if new_n > old_n:
            fail('edit %s would INTRODUCE %d non-ASCII character(s).'
                 % (label, new_n - old_n))
        carried += new_n
    print('[ascii ok]     no edit introduces a non-ASCII character '
          '(%d carried through unchanged)' % carried)

    # And the script's own bytes must be ASCII, which is why the one
    # character it carries is written as a \\u escape.
    with open(os.path.abspath(__file__), 'rb') as handle:
        own = handle.read()
    own_bad = sum(1 for byte in own if byte > 127)
    if own_bad:
        fail('this script itself holds %d non-ASCII byte(s); it must be '
             'pure ASCII.' % own_bad)
    print('[self ok]      this script is pure ASCII (%d bytes)' % len(own))

    # Pre-existing non-ASCII is REPORTED, not silently normalized. These
    # are U+2032 PRIME in the "B-prime" architecture name and one U+2033.
    # Fix In Passing does not apply: the encoding gate is scoped to
    # delivered code, and this is prose typography, so it needs a ruling
    # rather than a mechanical sweep.
    text = normalized.decode('utf-8')
    pre_existing = sum(1 for ch in text if ord(ch) > 127)

    # --- Gate 3: every anchor matches exactly once -------------------
    working = text
    for label, old, new in EDITS:
        count = working.count(old)
        if count != 1:
            fail('ANCHOR FAIL on edit %s -- expected exactly 1 match, '
                 'found %d. First 70 chars of the anchor: %r'
                 % (label, count, old[:70]))
        working = working.replace(old, new, 1)
        print('[ok]           %s' % label)

    # --- Gate 4: no line vanishes that no edit claims to rewrite -----
    # The permitted-loss set is DERIVED from the edits rather than
    # hand-listed, so it cannot drift out of step with them.
    allowed = set()
    for _label, old, new in EDITS:
        allowed.update(l for l in (set(old.split('\n')) - set(new.split('\n')))
                       if l)

    after = set(working.split('\n'))
    lost = [l for l in text.split('\n') if l and l not in after]
    unexpected = [l for l in lost if l not in allowed]
    if unexpected:
        fail('%d line(s) would be lost that no edit claims to rewrite. '
             'First: %r' % (len(unexpected), unexpected[0]))
    print('[addition ok]  %d line(s) rewritten, all accounted for'
          % len(lost))

    # --- Gate 5: the code fence count must come out even -------------
    fences_before = text.count('\n```')
    fences_after = working.count('\n```')
    if fences_after % 2 != 0:
        fail('code fences still unbalanced after the patch: %d markers. '
             'This patch exists partly to fix that.' % fences_after)
    print('[fences ok]    %d markers before (odd), %d after (even)'
          % (fences_before, fences_after))

    # --- Write, all or nothing --------------------------------------
    out = working.encode('utf-8')
    if is_crlf:
        out = out.replace(b'\n', b'\r\n')
    with open(target, 'wb') as handle:
        handle.write(out)

    print('')
    print('patch applied (%d bytes -> %d bytes, %d edits)'
          % (len(raw), len(out), len(EDITS)))
    print('')
    print('CURRENCY STAMPS UPDATED (Stamp What You Change, '
          'safe-file-editing 1.7):')
    print('  Status line          v18 -> v19')
    print('  Last updated         August 7 -> August 22, 2026')
    print('  Base (header)        orrery %s / gallery %s'
          % (BASE_SHA[:7], GALLERY_SHA[:7]))
    print('  Base (closing)       same')
    print('')
    print('note: %s still holds %d non-ASCII byte(s) this patch did not '
          'reach.' % (TARGET_NAME, pre_existing))
    print('      They are U+2032 PRIME (the "B-prime" architecture name, 22')
    print('      times) and one U+2033 DOUBLE PRIME. Deliberately NOT swept:')
    print('      the encoding gate is scoped to delivered code, this is prose')
    print('      typography, and Section 5a already spells the same name with')
    print('      an ASCII apostrophe. Normalizing needs a ruling, not a patch.')
    print('')
    print('NEXT:')
    print('  1. Move this script to documentation/ if it is not there already.')
    print('  2. Commit and push.')
    print('')
    print('STILL OPEN, reported not fixed -- these are ledger edits:')
    print('  - L-225 has no ledger entry; the highest handle is L-224.')
    print('  - L-154 reads BLOCKED; the braid makes it the first work.')
    print('  - MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md line 20 still')
    print('    points at the bare CRITICAL_PATH_SUMMARY.md.')


if __name__ == '__main__':
    main()
