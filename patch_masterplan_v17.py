# -*- coding: utf-8 -*-
"""patch_masterplan_v17.py -- Master Plan v16 -> v17: record the Phase 2
track structure and Tony's C-then-B-then-A ordering ruling.

Built on ee0da47c483cda02ac035d48ce99bc855a56e03c
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned at 61a78c00668573dbff111ec9f10a96b1cd2fdc35.

HOW TO RUN
    Save this file in the REPO ROOT (the folder holding documentation/),
    open it in VS Code, and click Run.

    Success: seven "ok" lines, then "patch applied".
    Failure: one "ANCHOR FAIL" or "ERROR" line, then "NOTHING WAS
    WRITTEN". The plan is unchanged either way.

WHAT CHANGES

  v17-1  Header status v16 -> v17, SHAs, date.
  v17-2  Phase 2 gains an explicit three-track structure with Track 0
         (constant layer scaffolding) ahead of the provenance batches.
  v17-3  Section 6's Batch 2 line updated: Track 0 now precedes it.
  v17-4  Section 7 gains three open decisions (12, 13, 14) covering the
         transport form, the generator shape, and L-179/L-180.
  v17-5  New in v17 block.
  v17-6/7  Tail base SHAs and next-step line.

THE RULING THIS RECORDS
    Tony, August 6, 2026: the order is C, then B, then A -- scaffolding,
    then provenance batches, then Artifact 2. Reasoning: a golden
    artifact is fingerprinted, so locking one on values that are not yet
    sourced and derived means redoing the lock rather than editing a
    number. This SUPERSEDES the August 5 "clear all batches before
    Artifact 2" instruction, which is preserved below it as history.

Patch written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = os.path.join('documentation', 'MASTER_PLAN_INTERACTIVE_GALLERY.md')
BASE_MD5 = 'd2ce153372ef30c5a92a6316800e1413'

PHASE2_TRACKS = b"""
**Track structure (added v17, Tony's ruling August 6, 2026).** Phase 2
runs in three tracks, in this order. The ordering is C-then-B-then-A in
the shorthand of the August 6 design session: scaffolding, then
provenance batches, then the artifact.

| Track | What | Exit condition |
|---|---|---|
| **0** | Constant layer scaffolding (L-181) | One store, provenance carried as data, display text derived, cross-repo transport working end to end |
| **1** | Provenance batches (L-156) | Batch 2 gas giants verified, on the Track 0 scaffolding |
| **2** | Artifact 2 (Jupiter/Saturn) | Golden artifact locked on verified, sourced, derived values |

**Why this order.** A golden artifact is fingerprinted. Locking one on
values that are not yet sourced and derived means redoing the lock later,
not editing a number. Scaffolding first is the cheaper order, not the
slower one. (Tony, August 6, 2026.)

**This supersedes the August 5 instruction** that all provenance batches
clear before Artifact 2 proceeds. That instruction is not withdrawn --
batches still precede the artifact -- but Track 0 now precedes the
batches. Recorded as a deliberate reversal, not a drift.

**Numbering note.** "Track 0" rather than renumbering, because Section 6
already refers to "Phase 2 Track 1, Batch 1 / Batch 2" and existing
handoffs cite those numbers. Renumbering would rebase item numbers across
documents -- the leak class the ledger already carries a lesson about.
Zero means "before Track 1" and touches nothing.

**What Track 0 collapses.** Three questions stop needing separate
answers under this order: the 17 citation-level mismatches ride with the
scaffolding rather than getting 17 comment repeats; Batch 2's annotations
write into whatever citation form Track 0 establishes rather than a form
Track 0 would then migrate; and L-179/L-180 become the first thing Track
0 fixes rather than a gate standing in front of it.

Gate: scene equivalence (Mode 5) + the gallery page ships.

### Phase 3"""

NEW_DECISIONS = b"""12. **How feature data crosses the repo boundary.** Framed in the August 6
    predesign handoff, reviewed by Fable 5 the same day, then reopened by
    Tony's questioning of the premise. Three candidates:
    (1) **Export then fetch** -- something in the orrery reads
    `constants_new.py` and writes a JSON artifact; the nightly builder
    fetches it, validates it, and commits it. This is what Fable reviewed
    and recommended (as "vendored pull": fetch it, and also commit the
    copy you fetched, so an unreachable orrery falls back to last night).
    (2) **JSON as the source of truth** -- values live in a data file both
    sides read. No generation at all, but the provenance scanner reads
    `.py` only, so the source of truth would be invisible to it. Fable
    advised against teaching the scanner JSON.
    (3) **Builder extracts directly** -- the builder fetches
    `constants_new.py` as TEXT at the orrery HEAD SHA and reads the values
    out with Python's `ast` module (parse the structure, never execute the
    file). No exporter, no new step in Tony's workflow, no scheduled job
    committing into the orrery repo. The technique is not novel:
    `provenance_scanner.py` line 899 already does exactly this to the same
    file, so the extraction machinery is proven in-project.
    **Option 3 is the leading candidate.** It is a material change from
    what Fable reviewed -- the review evaluated a design in which "the
    exporter" was presented as a given -- so it should go back for review
    before anything is built.
13. **Generator shape and run cadence.** LIVE ONLY IF decision 12 lands on
    option 1; option 3 dissolves it rather than answering it. Kept because
    the context is worth preserving either way:
    `export_orbit_cache.py` is a DORMANT Phase 1b seeding tool, not a live
    exporter. Nothing calls or imports it; all four tooling maps classify
    it `dev_tools`; the gallery references it only as a historical porting
    source at orrery `4e2629c`. The August 6 session twice built on the
    assumption it was live and Tony corrected it both times. Under option 1
    the export step is a NEW responsibility and "run something before
    pushing" is a habit that does not exist today -- a real cost to weigh,
    not a detail. Nightly export is the wrong shape for it: feature values
    change rarely, and scheduling it would mean an automated commit into
    the repo where Tony holds sole commit authority and works by hand
    through GitHub Desktop.
14. **L-179 and L-180 values.** Solar gravitational influence (150,000 vs
    126,000 AU) and the solar chromosphere's three inconsistent extents.
    Both are drift inside `constants_new.py` today. Under the v17 order
    they are the FIRST thing Track 0 settles -- migrating and deriving
    before they are resolved would transport a known-inconsistent value
    into the gallery artifact, the served cache, and the hover text,
    authoritative-looking in three more places.
15. **Unit-sanity validation.** Independent of decision 12 and needed
    under every option. Shape validation and source-presence validation
    both PASS on a value whose units changed -- switch a ring radius from
    km to AU and the parse succeeds, the shape matches, and a number three
    orders of magnitude wrong gets served. Range checking is the only
    guard that catches this class (a gas giant ring radius belongs roughly
    between 10,000 and 10,000,000 km; 0.0008 fails immediately whatever
    units were intended). Fable called for this as part of the load-time
    validation pass; recorded here so it is not lost if decision 12
    changes shape again.

---

## \xc2\xa78 \xe2\x80\x94 Vision Opportunities"""

NEW_V17 = b"""*New in v17 (August 6, 2026):*
- **Phase 2 track structure added, and Tony's ordering ruling recorded.**
  Track 0 (constant layer scaffolding) precedes Track 1 (provenance
  batches) precedes Track 2 (Artifact 2). Reasoning: a golden artifact is
  fingerprinted, so locking one on unsourced values means redoing the
  lock. Supersedes the August 5 "clear all batches first" instruction,
  which is preserved as history rather than deleted.
- **L-181 promoted out of Prep Work into a phase track.** As reframed on
  August 6 it carries one store, a citation-form migration, derivation
  across five restatement surfaces, a generator, a cross-repo transport,
  and a load-time validation pass. That is phase-scale work, and leaving
  it in Section 6 was why the August 6 design session kept expanding --
  implementation questions were being answered against no scope boundary.
- **Fable 5 design review, August 6** (built on orrery `ee0da47c` /
  gallery `61a78c0`; zero code). Architecture endorsed. Four findings the
  predesign handoff's evidence chain missed, all independently verified
  by Claude Opus 5 at the same anchors: `spectral_subclass_temps` is an
  uncited physical claim inside the store itself, so the convention must
  apply at home before it is enforced outward; `KNOWN_ORBITAL_PERIODS`
  carries the key `'Phobos'` twice (133 keys, one duplicate, same value
  today) -- Python silently keeps the last, which is the argument for a
  load-time validation pass; the module-level `*_info` tooltip strings
  are a FIFTH restatement surface the handoff's count missed (Uranus
  restates 25,559 km nine times and does arithmetic in prose), and had
  derivation covered dict descriptions but not these, the `*_info`
  strings would have become the surviving duplicate -- L-182's exact
  shape, which the build was on course to recreate; and the gallery
  constant enumeration missed four sites including three BARE literals
  `149597870.7` inline in `gallery_studio.py`.
- **Four open decisions added to Section 7** (12-15): transport form,
  generator shape, the L-179/L-180 values, and unit-sanity validation.
- **The transport question reopened after Fable's review, by Tony
  questioning the premise.** The handoff and the review both wrote "the
  exporter" as though pointing at something live. It is not:
  `export_orbit_cache.py` is a dormant Phase 1b seeding tool that nothing
  calls. Removing that assumption surfaced a third option neither
  document considered -- the nightly builder fetching `constants_new.py`
  as text and reading the values out with Python's `ast` module, the same
  technique `provenance_scanner.py` already applies to that file at line
  899. It needs no exporter, no new step in Tony's workflow, and no
  scheduled job committing into the orrery repo. Leading candidate,
  pending a Fable re-review, since it is a material change from what was
  reviewed.
- **Coupling note for whichever option lands.** Under option 3 the
  builder depends on the store's dict NAMES and SHAPE -- not on its
  values. Value edits, new entries, new bodies, and comment changes all
  flow through untouched; renames, field renames, nesting changes, and
  file moves break the extractor, loudly, at build time. Because Track 0
  itself restructures the store, the extractor is built AFTER Track 0
  settles the shape. The coupling must be documented on BOTH sides -- a
  note reaching only one of two editors is the L-182 shape again -- and
  that is recorded as a Track 0 exit criterion in L-181 rather than as
  its own ledger item.
- Scanner console now prints the per-domain split under each tier line,
  and `MODULE_DOMAIN_MAP` covers `orrery_rendering` and `shell_configs`
  explicitly (L-184, Task 2a, landed `5a56473`). Domain coverage-gap note
  cleared; totals unchanged at 877 / 117 files / 206-581-88-2.
- Ledger items opened this cycle: L-184 (build-path gate), L-185
  (assembler source discipline), L-186 (cross-check annotation issues),
  L-187 (info_dictionary numeric-overlap enumeration).

"""

EDITS = [
    ('v17-1a', 'header status v16 -> v17',
     b"**Status:** v16 -- Phase 2 (solar system assembler) BUILD UNDERWAY.",
     b"**Status:** v17 -- Phase 2 (solar system assembler) BUILD UNDERWAY."),

    ('v17-1b', 'header current-HEAD anchor',
     b"HEAD orrery `4b82384e` / gallery `e7e8c5ef`",
     b"HEAD orrery `ee0da47c` / gallery `61a78c00`"),

    ('v17-1c', 'last-updated date',
     b"**Last updated:** August 5, 2026",
     b"**Last updated:** August 6, 2026"),

    ('v17-2', 'Phase 2 track structure',
     b"Gate: scene equivalence (Mode 5) + the gallery page ships.\n\n### Phase 3",
     PHASE2_TRACKS),

    ('v17-3', 'Section 6: Track 0 precedes Batch 2',
     b"Batch 2 is now the stated gate before Artifact 2 (Tony, 2026-08-05):",
     b"AMENDED v17 (Tony, 2026-08-06): Track 0 (constant layer scaffolding)\n"
     b"now precedes the batches. The August 5 wording is preserved below as\n"
     b"history -- batches still precede the artifact, but they no longer come\n"
     b"first. See Phase 2 track structure in Section 5.\n"
     b"Batch 2 is the stated gate before Artifact 2 (Tony, 2026-08-05):"),

    ('v17-4', 'Section 7: decisions 12, 13, 14',
     b"---\n\n## \xc2\xa78 \xe2\x80\x94 Vision Opportunities",
     NEW_DECISIONS),

    ('v17-5', 'New in v17 block',
     b"*New in v16 (August 5, 2026):*",
     NEW_V17 + b"*New in v16 (August 5, 2026):*"),

    ('v17-6', 'tail base SHAs',
     b"Base: orrery @ `4b82384` / gallery @ `e7e8c5e` (v16; v15 was orrery",
     b"Base: orrery @ `ee0da47` / gallery @ `61a78c0` (v17; v16 was orrery\n"
     b"`4b82384` / gallery `e7e8c5e`; v15 was orrery"),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found." % TARGET)
        print("       Save this script in the REPO ROOT, not documentation/.")
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    norm = 0
    if b'\r\n' in data:
        norm = data.count(b'\r\n')
        data = data.replace(b'\r\n', b'\n')
        print("fix CRLF     normalized %d line endings to LF" % norm)

    got = hashlib.md5(data).hexdigest()
    if got != BASE_MD5:
        print("ERROR: master plan base does not match.")
        print("       expected md5 %s" % BASE_MD5)
        print("       found    md5 %s" % got)
        print("       NOTHING WAS WRITTEN. Re-pull and rebuild.")
        return 1

    for eid, label, old, new in EDITS:
        c = data.count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) matched %d, expected 1." % (eid, label, c))
            print("             NOTHING WAS WRITTEN. The plan is unchanged.")
            return 1

    for eid, label, old, new in EDITS:
        data = data.replace(old, new, 1)
        print("ok  %-8s %s" % (eid, label))

    try:
        data.decode('utf-8')
    except UnicodeDecodeError as exc:
        print("ERROR: result is not valid UTF-8 (%s)." % exc)
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'wb') as f:
        f.write(data)

    print("")
    print("patch applied%s" % (" (+%d CRLF normalized)" % norm if norm else ""))
    print("  %s  -> v17" % TARGET)
    print("")
    print("No ledger edits here. Run patch_ledger_fable_review_v2.py next,")
    print("then ledger_index.py.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
