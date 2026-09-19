# HANDOFF -- the exhibit store editor, built (L-334) and closed

Built on orrery `bb614c7fd4b8b7760c3512baa0c39964972a82e2`
at https://github.com/tonylquintanilla/palomas_orrery
and gallery `2ebd001f2ec5d358aa6bb5fa1c6a573be99a502d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io

Session of 2026-09-18/19, Tony with Anthropic's Claude Opus 5, with a
review by Claude Fable 5.1 partway through. Written 2026-09-19.

Both anchors are the state AFTER everything below was pushed. Ten
patches ran, each verified in the pushed tree before the next was cut.


## READ THIS FIRST, before any exhibit or cache work

TWO SKILLS WERE BUMPED IN THIS SESSION AND REINSTALLED BY TONY AFTER
IT. A reinstall lands in the account and stays invisible to the session
that makes it, so this session could not verify it and did not try.

    interactive-exhibit      1.3 -> 1.4
    gallery-cache-builder    1.4 -> 1.5

CONFIRM YOUR LOADED COPIES READ 1.4 AND 1.5 before doing exhibit or
cache work. If either reads the old version, that is the stale-skill
gate and it stops the task -- say so and ask Tony to reinstall, rather
than working from what loaded.

The protocol is v3.62 and carries both bumps in one entry.


## What exists now that did not on 2026-09-17

An editor for the words a visitor reads in the exhibit rooms, reachable
from the dashboard at Gallery & Web > Exhibit Store Editor.

    gallery  tools/store_writer.py            the in-place writer
             tools/exhibit_store_editor.py    the window
             tools/test_store_writer.py       245 checks
             tools/test_exhibit_store_editor.py
                                              246 without a window,
                                              286 with --window
             gallery/arrival.js               what a room opens on,
                                              moved out of the page

The gallery maintenance run is 14 of 14 offline and 2 of 2 live, and the
live run now fetches ELEVEN served files rather than eight.

HOW THE PIECES FIT. `data/objects_config.json` is hand-formatted and a
person reads its diffs, so nothing rewrites it wholesale. Two tools edit
it in place, sharing one scanner (`mirror_constants.parse_with_spans`):
the mirror writes the NUMBERS from the orrery's export, and the store
writer writes the WORDS and the arrival settings. The editor is a window
over the writer. What the writer may touch is an ALLOW LIST built by
reading the config -- 203 paths at `2ebd001f` -- so anything not on it
is refused whatever it is.


## What closed, and what is open

CLOSED THIS SESSION:

    L-334  the editor. Three stages: the ledger, the arrival tidy-up,
           the editor itself.
    L-336  the served cache went out of step with the config, and no
           check read the file the browser reads.
    L-338  logic that needs no browser lives in its own file. Tony's
           rule, 2026-09-18.
    L-339  the live check did not read every file the browser fetches.

OPEN, AND THEY ARE THE NEXT SESSION'S MATERIAL:

    L-340  the Mode 5 pass over the editor. Its three recorded findings
           are FIXED and pushed; what remains is Tony at the window with
           time to look properly. Whatever he finds belongs here.
           It also carries two things this session learned the hard way:
           a skill description is capped at 1024 characters, and a
           proposal that `skills_index.py` fail a run that exceeds it.
    L-337  a centre marker for bodies without shells. TONY ADDED TO THIS
           ON 2026-09-19, and the addition is not yet in the ledger --
           put it there in the next ledger patch, as the first thing:
           "while it is not a shell or a tick, the 'sun' object is
           useful for centering the scene nominally. the earth should
           have one too in case we wish to display no shells. this is an
           option in the orrery." So the marker is a CENTRING object,
           the Sun's room already has one, Earth's needs one, and the
           orrery already offers it as an option -- which is where to
           look for the shape of the answer.
    L-216  the folder swap under OneDrive. Still open for the CAUSE.
           The record of it is now in gallery-cache-builder 1.5.


## The L-322 picture, measured 2026-09-19

Tony asked what remains of L-322 and of the Earth slice. Measured rather
than recalled, at orrery `bb614c7f`:

  - L-322's gallery half is DONE and deployed.
  - `constants_new.py` holds 110 assignments, 57 of them `EARTH_`.
  - Of those 57: 28 carry `# Unit:`, 28 carry `# Status:`, 22 carry
    `# Derived:`, and ZERO carry `# Figures:` or `# Read:`.
  - Zero of all 110 carry `# Figures:`. The field that
    provenance-discipline 2.13 was bumped to define has not been written
    anywhere yet. The orrery run says the same: 31 derived rows read, 0
    judged, 31 not yet migrated.
  - `constants_rows.CLOSED_SLICES` is still `()`, and both standoffs are
    still in `TRANSITIONAL` as rounded literals awaiting the revert that
    L-325's withdrawal set up.

L-249 IS A DIFFERENT PASS OVER THE SAME ROWS and comes first for any row
not yet in the store: it is Earth's interior boundaries becoming sourced
constants at all. L-322's Earth slice is what each row DECLARES once it
is there.


## Five things this session learned, and where each now lives

1. A REFUSAL LIST CANNOT BE COMPLETE. The writer's first design refused
   six named fields and accepted everything else, so it would change a
   room's `slug` or a shell's `color` -- either breaks a room. Claude
   Fable 5.1 found it by trying. An allow list only has to know what is
   right. Now in interactive-exhibit 1.4.

2. A CONFIG CHANGE IS NOT DEPLOYED UNTIL THE CACHE IS REBUILT, and the
   two are committed together. True long before anyone wrote it down;
   cost both rooms on the live site on 2026-09-17 while eleven checks
   passed. Now in gallery-cache-builder 1.5.

3. TWO CHECKS THAT COULD NOT FAIL, both Claude's, both found by breaking
   them on purpose. One asserted a refusal message MENTIONED "value" --
   and "value" is in the path, so emptying the refusal list left it
   green. The other built Earth's features without the Sun direction, so
   two of Earth's sixteen shells were never examined by the check
   written to examine all of them. The habit that found both: break it
   and watch it go red.

4. A SKILL DESCRIPTION IS CAPPED AT 1024 CHARACTERS. interactive-exhibit
   1.4 came out at 1042 and would not install; the 35 kB body was never
   the problem. On L-340.

5. A PATCH THAT DELETES AN ENTRY FROM ONE FILE WRITES IT INTO THE OTHER
   IN THE SAME RUN. `patch_L334_9` removed v3.59 from the protocol and
   printed it for Tony to paste, which broke the one-place rule toward
   ZERO. Repaired by `patch_L334_10`. Tony's correction: "normally this
   is done by the patch."


## Housekeeping worth knowing

TWO SHA TRANSPOSITIONS happened this session -- the orrery's SHA reported
as the gallery's, twice. Both were caught by reading the live HEADs
rather than trusting the message. Read both remotes at session start and
name which is which.

THREE FILES WERE COMMITTED TO THE GALLERY ROOT and cleaned up on
2026-09-19: two stray copies of the editor saved from files handed over
for reading, and a patch script that had not been moved into
`documentation/`. The stray copies were byte-identical to the real ones
in `tools/`, which is exactly the trap.

ONE EXCEPTION IS RECORDED AND NOT YET IN A SKILL.
`patch_L340_1_editor_polish_20260919.py` wrote `data/objects_config.json`
directly, to remove a `moon` key the writer cannot remove. That is a
third writer against interactive-exhibit 1.4's rule that only two tools
write the file. It is on L-340 so the next bump of that skill can carry
the exception for one-off correction patches.


## The patches, in order, all run and pushed

    orrery   patch_L334_2_ledger_stage_a_20260917.py
    gallery  patch_L334_3_arrival_module_20260918.py
    orrery   patch_L334_4_ledger_stage_b_20260918.py
    gallery  patch_L334_5_store_writer_20260918.py
    orrery   patch_L334_6_dashboard_store_editor_20260918.py
    orrery   patch_L334_7_dashboard_gallery_web_20260918.py
    gallery  patch_L334_8_store_editor_20260919.py
    orrery   patch_L334_9_records_20260919.py
    orrery   patch_L334_10_skill_description_and_history_20260919.py
    gallery  patch_L340_1_editor_polish_20260919.py

All ten are filed in their repository's `documentation/`.

Written September 2026 with Anthropic's Claude Opus 5.
