# Move 1 -- Skills v1.1 batch (Fable Mode 7 review, targeted snippets)
**Prepared by Opus 4.8, 2026-07-12 | all edits verified against orrery HEAD 7e108b8**

Apply alongside your local L-114 work; everything pushes together. All edits are
ASCII/LF. No pre-test gate fires here -- these are Mode 1 doc/comment snippets;
the apply + render is the gate. After push: re-round-trip both repos, then do the
SHA re-pins (see step at the end).

Five edits: items 2, 3, 4, 6 (skill v1.1 bumps) + item 7 (code comment).
Item 8 (provenance carve-out) was DROPPED -- provenance_scanner.py:382 walks
`.py` only, so SKILL.md is already outside the scan; the line would document a
risk that cannot occur.

---

## ITEM 7 -- palomas_orrery.py (orrery repo) -- Encke comment [Fable F4]

Line 1522. Stale recalled record number.

OLD:
    # Halley = 90000030, Encke = 90000002, etc.

NEW:
    # Halley = 90000030, Encke = 90000091, etc.

---

## ITEM 2 -- skills/agentic-pre-test/SKILL.md (orrery repo) -> v1.1 [Fable F2]

### 2a. Correct the inverted gray90 rationale (the fact was backwards)

OLD:
    palomas_orrery.py natively contains 26 legitimate gray90 literals, so a
    gray90->SystemButtonFace restore converts those real values too, silently
    corrupting the delivered file. Test on a copy, discard the copy; the
    deliverable is never edited by the pre-test. (Caught June 9, 2026;
    practice every session since.)

NEW:
    palomas_orrery.py contains 26 SystemButtonFace literals and 0 native
    gray90, so the test swap yields gray90 literals indistinguishable from
    NATIVE gray90 -- which DOES exist in sibling GUI files
    (star_visualization_gui.py has 5, earth_system_visualization_gui.py has 3
    at the time of writing). A gray90->SystemButtonFace restore therefore
    cannot tell converted from legitimate values; run it on the wrong file, or
    after the counts drift, and it silently corrupts the deliverable. Test on a
    copy, discard the copy; the deliverable is never edited by the pre-test.
    (Caught June 9, 2026; practice every session since.)

### 2b. Cross-pointer to the builder gate (append to "When This Protocol Is Required")

OLD:
    himself (the render is the gate there), pure documentation, design
    sessions.

NEW:
    himself (the render is the gate there), pure documentation, design
    sessions.

    Gallery-repo builder deliverables have their own layered gate (offline
    suite + live dry-run + schedule) -- see the gallery-cache-builder skill and
    documentation/TESTING_PROTOCOL.md, not this protocol.

### 2c. Version line

OLD:
    Skill version: 1.0 | Cut from palomas_orrery @ b29ad3f8 | July 1, 2026

NEW:
    Skill version: 1.1 | Cut from palomas_orrery @ <ORRERY HEAD after push> | 2026-07-12

---

## ITEM 3 -- skills/horizons-orbital-mechanics/SKILL.md (orrery repo) -> v1.1 [seed 1]

### 3a. fires_when (line 4) gains the new trigger

OLD:
    fires_when: Horizons queries, centers, frames, osculating elements, encounters

NEW:
    fires_when: Horizons queries, centers, frames, osculating elements, encounters, comet record pinning

### 3b. New section, inserted AFTER "JPL Binary System IDs", BEFORE "Reference Frame Diagnostic"

OLD:
      Horizons serves only one member.

    ## Reference Frame Diagnostic

NEW:
      Horizons serves only one member.

    ## Small-Body Record Pinning (periodic comets)

    90000000+ numeric IDs are Horizons small-body RECORD numbers -- one
    specific orbit solution, usually the current apparition. Use them to pin
    periodic comets:
    - A bare short designation ("2P") with id_type='smallbody' resolves
      AMBIGUOUSLY (Encke: 61 historical apparition records), and adding
      closest_apparition throws a syntax error -- astroquery prepends the
      required DES= key only for id_type='designation'/'name', never for
      'smallbody'.
    - House pattern: pin the specific current record, no apparition flag
      needed. Halley id='90000030' (celestial_objects.py); Encke '90000091'
      (gallery objects_config.json). Proven live 2026-07-11.
    - Cost of pinning: a pinned record does NOT auto-track a future JPL
      solution update. Recheck pinned records periodically, like any frozen
      upstream identifier.

    ## Reference Frame Diagnostic

### 3c. Version line -- same bump as 2c (1.0 -> 1.1, re-pin SHA post-push, date 2026-07-12)

---

## ITEM 4 -- skills/earth-system-pipeline/SKILL.md (orrery repo) -> v1.1 [Fable F3]

### 4a. Fix the phantom GUI name (MissionSelector / all_scenarios do not exist)

OLD:
    the GUI (MissionSelector) extends
    all_scenarios from each module's SCENARIOS.

NEW:
    _heat_scenarios() in earth_system_generator.py aggregates the scalar-engine
    modules' SCENARIOS lists (food insecurity is deliberately NOT aggregated
    there -- it has its own generator and its own controller entry point,
    MissionControlApp in earth_system_controller.py, with the shared
    ScenarioPicker from earth_system_common).

### 4b. Version line -- same bump (1.0 -> 1.1, re-pin SHA post-push, date 2026-07-12)

---

## ITEM 6 -- skills/orrery-coding-conventions/SKILL.md (orrery repo) -> v1.1 [seed 2]

### 6a. Add the optional "Operational gotchas" block to the Module Docstring Standard

INSERT the block below between the docstring template's closing fence and the
"Tooling:" paragraph (i.e., right after the template code block, before
"Tooling: module_atlas.py ..."):

    Optional, for modules with real operational risk (unattended
    infrastructure, destructive file operations, cache managers) -- an
    "Operational gotchas" block at the end of the docstring:

        Operational gotchas:
            KNOWN TRAP: <the one mistake an operator will plausibly make, and
            its consequence>
            NORMAL BUT SCARY: <the one alarming-looking state that is actually
            fine, so nobody "fixes" it>

    One line each, only where earned; most modules never need it. (Motivated by
    L-114: the config-swap trap and the .prev directory both needed exactly
    this warning.)

### 6b. Version line -- same bump (1.0 -> 1.1, re-pin SHA post-push, date 2026-07-12)

---

## LEDGER ENTRY -- L-115 (orrery repo, LEDGER_CONSOLIDATED.md)

Paste the detail block; then run ledger_index.py to regenerate the index zone.

    #### [L-115] Skills v1.1 batch: accuracy fixes + two seed blocks (Fable Mode 7)
    <!-- L:115 status:OPEN upd:2026-07-12 section:H flag: rice:2/2/90/1 -->
    - **What.** Move 1 of the skills-layer update from Fable 5's 2026-07-12
      Mode 7 review. Five targeted edits, all verified against orrery HEAD
      7e108b8 by Opus before delivery:
        - agentic-pre-test 1.1: correct the inverted gray90/SystemButtonFace
          rationale (palomas_orrery.py has 0 gray90 / 26 SystemButtonFace at
          HEAD and at the b29ad3f8 cut; real risk is cross-file
          indistinguishability -- siblings star_visualization_gui.py=5,
          earth_system_visualization_gui.py=3) + cross-pointer to the
          gallery-cache-builder gate. [Fable F2]
        - horizons-orbital-mechanics 1.1: new Small-Body Record Pinning block
          (short-designation ambiguity; pin comets to 900000XX records: Encke
          90000091, Halley 90000030); fires_when gains "comet record pinning".
          [seed 1]
        - earth-system-pipeline 1.1: fix a phantom GUI name -- MissionSelector /
          all_scenarios do not exist; real names MissionControlApp,
          ScenarioPicker, _heat_scenarios(). [Fable F3]
        - orrery-coding-conventions 1.1: optional "Operational gotchas"
          docstring block (known-trap + normal-but-scary), PRACTICE. [seed 2]
        - palomas_orrery.py:1522 comment: Encke 90000002 -> 90000091 (stale
          recalled record number in an illustrative comment). [Fable F4]
    - **Dropped from the batch:** Fable's provenance-discipline carve-out line
      -- provenance_scanner.py:382 walks .py only, so SKILL.md is already
      structurally outside the scan; the line would document a non-existent
      risk. [verified @7e108b8]
    - **Gap.** Apply the five snippets; bump the four skill version lines to 1.1
      and re-pin "Cut from ... @ <SHA>" to the POST-PUSH orrery HEAD; run
      skills_index.py to regenerate the Skill Manifest (horizons fires_when
      changed); reinstall the four skills to Tony's account. Move 2 (new
      gallery-cache-builder skill) tracked as a sibling entry when opened.
    - **Ref.** Fable review doc 2026-07-12 (F2/F3/F4, seeds 1-2). Parent: L-002
      (skills layer).
    **Tony:** RICE proposed 2/2/90/1 -- yours to finalize. One umbrella entry as
    delivered, or split per skill (your call).

---

## POST-APPLY STEPS (after all five edits + the ledger entry are in)

1. Re-run the ASCII/LF gate on the four touched SKILL.md files + palomas_orrery.py.
2. Commit + push the orrery repo (this batch rides with your local L-114 ledger
   entry + the gallery L-114 code push).
3. Re-round-trip both repos (git ls-remote); record the new orrery HEAD.
4. Re-pin the four version lines' "Cut from ... @ <SHA>" to that new orrery HEAD
   (so each pin matches the tree its prose describes, per Fable's sequencing).
   This is a second tiny commit -- the pin references the tree, not itself.
5. Run skills_index.py; confirm the Skill Manifest table shows the four v1.1
   bumps and horizons' widened fires_when. Never hand-edit the manifest zone.
6. Reinstall the four skills to your account.

Move 2 (the ninth skill, gallery-cache-builder) comes next, as its own agentic
build from Fable's skeleton -- fleshed from fetched sources, ASCII/LF-gated,
with the gallery-pipeline cross-pointer and a fresh manifest regen.
