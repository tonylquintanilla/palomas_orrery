# Move 2 -- gallery-cache-builder skill + surrounding edits
**Prepared by Opus 4.8, 2026-07-12 | verified against gallery HEAD 8e060677, orrery HEAD e83fe9ce**

Round-trip confirmed: both HEADs match your push. Move 1 / L-114 landed clean
(config default = data/objects_config.json, offline-test line 79 moved, Encke
comment = 90000091, four skills at v1.1).

Everything below goes in the ORRERY repo. All ASCII/LF. Note the key contrast
with Move 1: these skills describe ALREADY-PUSHED, stable trees, so their
Cut-from SHAs are real and final now -- NO post-push re-pin needed this time.

---

## 1. NEW FILE -- skills/gallery-cache-builder/SKILL.md

Create the directory and drop in the delivered SKILL.md
(gallery-cache-builder_SKILL.md). It is already pinned:
`Cut from tonyquintanilla.github.io @ 8e060677 (code) and palomas_orrery @ e83fe9ce (context)`.
Every code fact in it was verified against those HEADs (function names,
validation dispositions, swap/sibling semantics, the four served files,
interactive.html's not-yet-a-consumer status).

Notable corrections baked in vs Fable's skeleton:
- _sweep_siblings (verified at builder line 869) -- NOT cleanup_stale_siblings.
- #B3 is an ABORT, not a WARN -- the code raises ValidationAbort (line ~790);
  only Guard v2 warns-and-keeps. (The builder's own line-755 inline comment
  mislabels this; flagged as a separate cleanup, see item 4.)

---

## 2. EDIT -- skills/gallery-pipeline/SKILL.md -> v1.1 (cross-pointer)

### 2a. Add the cross-pointer at the END of "Two-Repo Coupling (load-bearing)"

OLD:
    the same bug appears independently in Studio and
    the viewer. SHA-pin each repo separately in handoffs.

    ## The Chain

NEW:
    the same bug appears independently in Studio and
    the viewer. SHA-pin each repo separately in handoffs.

    The nightly data-serving stack (tools/gallery_cache_builder.py,
    data/objects_config.json, data/solar-system/, and the future
    interactive.html consumer) is a SEPARATE subsystem with its own skill --
    load gallery-cache-builder for any task touching it.

    ## The Chain

### 2b. Version line

Bump `Skill version: 1.0` -> `1.1` and update the date to `2026-07-12` on the
version line. LEAVE the Cut-from SHAs as-is (89c8bf30 / b29ad3f8): the skill's
substantive content (Studio/converter/viewer) is unchanged and was not
re-verified against the new HEAD this session -- only the cross-pointer was
added. fires_when unchanged.

---

## 3. FIX -- the four Move-1 placeholder version lines (re-pin)

Move 1 pushed with the literal placeholder committed verbatim. In each of these
four files, replace on the "Skill version:" line:

    <ORRERY HEAD after push>   ->   e83fe9ce

Files: skills/agentic-pre-test/SKILL.md, skills/horizons-orbital-mechanics/SKILL.md,
skills/earth-system-pipeline/SKILL.md, skills/orrery-coding-conventions/SKILL.md.
(e83fe9ce is the post-Move-1 orrery HEAD those skills were verified against.)

---

## 4. LEDGER ENTRY -- L-116 (orrery repo, LEDGER_CONSOLIDATED.md)

Paste the detail block; then run ledger_index.py to regenerate the index zone.

    #### [L-116] New skill: gallery-cache-builder (Move 2 of the skills update)
    <!-- L:116 status:OPEN upd:2026-07-12 section:H flag: rice:3/2/85/2 -->
    - **What.** Ninth skill, gallery-cache-builder, added for the Phase 1b
      nightly serving subsystem (L-098) -- Move 2 of Fable 5's 2026-07-12 Mode 7
      review. Decomposition decision (Tony, this session): NEW skill, not an
      extension of gallery-pipeline (non-overlapping moments of need; the
      builder passes every subsystem marker). Authored
      skills/gallery-cache-builder/SKILL.md in the orrery repo (L-002
      convention; describes gallery code @ 8e060677 + orrery context @
      e83fe9ce). Every code fact verified against HEAD before delivery; Fable's
      cleanup_stale_siblings seed corrected to _sweep_siblings; validation
      stance corrected (#B3 ABORTs, not WARN -- the code raises).
      gallery-pipeline bumped to 1.1 with a one-line cross-pointer.
    - **Also in this push (Move 1 follow-through).** Re-pin the four Move-1 skill
      version lines: the literal placeholder "<ORRERY HEAD after push>" was
      committed verbatim and is corrected to e83fe9ce (the post-Move-1 orrery
      HEAD they were verified against).
    - **Spotted, not fixed here.** gallery_cache_builder.py ~line 755 inline
      comment "guard/B3 WARN" contradicts the code (#B3 raises ValidationAbort)
      and the module docstring. Low-priority builder-comment cleanup; deferred.
    - **Gap.** Create the new skill dir + file; apply the gallery-pipeline
      cross-pointer + 1.1 bump; apply the four re-pins; run skills_index.py
      (manifest gains a 9th row, gallery-pipeline -> 1.1); reinstall the new +
      edited skills. On push, no post-push re-pin needed -- Move 2's skills
      describe already-pushed stable trees (unlike Move 1).
    - **Ref.** Fable review doc 2026-07-12, section 2.1 (new-skill argument),
      seed 3. Parent: L-002. Sibling: L-115 (Move 1). Subsystem: L-098.
    **Tony:** RICE proposed 3/2/85/2 -- yours to finalize.

---

## 5. POST-APPLY STEPS

1. ASCII/LF gate the new skill + gallery-pipeline + the four re-pinned skills.
2. Run skills_index.py; confirm the Skill Manifest now shows NINE rows with
   gallery-cache-builder present and gallery-pipeline at 1.1. Never hand-edit
   the manifest zone.
3. Reinstall the new skill (and gallery-pipeline) to your account; the four
   re-pinned skills need reinstalling too if the install copies carry the
   version line.
4. Commit + push the orrery repo. No re-pin follow-up this time.
5. Optional: round-trip once more so I can confirm the manifest and pins landed.

That closes the skills update (Moves 1 + 2). Open threads it leaves, all
tracked, none blocking: the builder line-755 comment cleanup; and the broader
Phase 1b close-out (L-098 gap items -- Guard-banner injection check, backup
action, and the L-111 unattended-nightly correctness/operability items).
