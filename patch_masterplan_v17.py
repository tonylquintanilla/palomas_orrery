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
    Tony, August 6-7, 2026: the order is C, then B, then A -- scaffolding,
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
**Track structure (added v17, Tony's ruling, August 2026 session).** Phase 2
runs in three tracks, in this order. The ordering is C-then-B-then-A in
the shorthand of the August 6-7 design session: scaffolding, then
provenance batches, then the artifact.

| Track | What | Exit condition |
|---|---|---|
| **0** | Constant layer scaffolding (L-181) | One store, provenance carried as data, display text derived, cross-repo transport working end to end |
| **1** | Provenance batches (L-156) | Batch 2 gas giants verified, on the Track 0 scaffolding |
| **2** | Artifact 2 (Jupiter/Saturn) | Golden artifact locked on verified, sourced, derived values |

**Why this order.** A golden artifact is fingerprinted. Locking one on
values that are not yet sourced and derived means redoing the lock later,
not editing a number. Scaffolding first is the cheaper order, not the
slower one. (Tony, August 2026 session.)

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

NEW_DECISIONS = b"""12. **How feature data crosses the repo boundary.** RECOMMENDED, not yet
    ratified: **fetch-and-import.** The nightly builder resolves the
    orrery HEAD SHA, fetches `constants_new.py` as text at that SHA,
    imports it, reads the feature values and their sources, validates,
    and writes into the staging cache under existing atomic-swap
    semantics. Python evaluates all derivation natively. Tony's workflow
    does not change: edit a constant, commit, push. Endorsed by Fable 5
    round 2 as "round 1's vendored pull with the exporter removed -- same
    fallback property, same SHA recording, same quarantine semantics,
    strictly fewer moving parts, and zero hand steps."
    Two earlier candidates are retired: exporting to a JSON artifact
    (rests on a generation step and a run trigger that do not exist), and
    reading the file with Python's `ast` module without executing it
    (fights the store's design -- 7 of 45 top-level assignments are
    derived rather than literal, and two contain constructor calls
    `ast.literal_eval` cannot evaluate at all).
    Trust argument, recorded because future sessions will re-ask it: the
    builder, the orrery GUI, and every patch script Tony runs already
    come from the same two repos under the same account, so importing one
    more file from it adds NO NEW TRUST ROOT. A raw fetch at a full
    40-character SHA is content-addressed, so there is no window in which
    what was checked and what was imported can differ.
13. **Generator shape and run cadence.** DISSOLVED by decision 12. There
    is no generation step -- "generation" is Tony editing the store.
    Kept as a record because two sessions built on the opposite
    assumption: `export_orbit_cache.py` is a DORMANT Phase 1b seeding
    tool. Nothing imports or calls it on any automated path; all four
    tooling maps classify it `dev_tools`; the gallery references it only
    as a historical porting source at orrery `4e2629c`. One live pointer
    remains -- `palomas_orrery_dashboard.py` line 253 advertises it in
    the launcher menu (Fable round 2). That entry, and the exporter's own
    `feature_configs.json` output, belong in a retirement note so no
    future session reads them as live.
14. **L-179 and L-180 values.** Solar gravitational influence (150,000 vs
    126,000 AU) and the solar chromosphere's three inconsistent extents.
    Both are drift inside `constants_new.py` today. Under the v17 order
    they are the FIRST thing Track 0 settles -- migrating and deriving
    before they are resolved would transport a known-inconsistent value
    into the served cache and the hover text, authoritative-looking in
    three more places.
15. **Validation layers.** Four checks, each catching a class the others
    miss. (a) Source presence -- abort, not warn. (b) Unit-sanity RANGE
    checking: shape and source-presence validation both PASS on a value
    whose units changed, and only magnitude bounds catch a km-to-AU slip.
    (c) Cross-field invariant on ring geometry. **Use `inner <= outer`,
    NOT `inner < outer`.** Fable recommended strict less-than and stated
    it catches nothing spurious today; verified against the store, strict
    `<` would fire on 8 Neptune entries where inner and outer are
    deliberately equal -- narrow ringlets modelled at a single radius
    (Le Verrier at 53,200 km; six Adams arcs at 62,932 km). `inner >
    outer` is genuinely zero. A check that fires spuriously on day one is
    one people learn to ignore. (d) Nightly value-diff against last
    night's committed copy, logging every changed value with old, new,
    and both orrery SHAs -- the only guard that sees CHANGE itself, which
    is the L-182 failure family.
16. **Pilot slice inside Track 0.** OPEN, Tony decides. Fable round 2
    recommends migrating ONE body first (Jupiter, 5 entries) through the
    full Track 0 treatment and building the transport end-to-end against
    it, then scaling to the remaining 32 -- which under fetch-and-import
    needs zero transport rework, since new entries flow through
    untouched. The argument: the transport cannot be tested against
    today's store at all, because no `source` fields exist for
    abort-on-missing-source to act on, so "transport after Track 0"
    really means "first end-to-end test after all 37 entries move" --
    the largest possible batch before the first proof. A pilot gives
    Tony's acceptance test ("this should be minor if the architecture is
    right") its first data point at one-seventh the exposure, and
    Jupiter's descriptions contain the resistant-prose cases. Cost: two
    passes over the migration tooling instead of one.
17. **Where description interpolation happens.** OPEN. The served cache
    can hold templates plus values, with the assembler interpolating at
    render time; or pre-interpolated final strings, with the builder
    interpolating at build time. Fable recommends builder-side: it keeps
    the assembler dumb, keeps the failure surface at build time where
    quarantine already exists, and means a template error is caught
    nightly rather than in a user's browser. Either answer works, but it
    decides the cache schema, so it is decided before the schema is
    written.

---

## \xc2\xa78 \xe2\x80\x94 Vision Opportunities"""

NEW_V17 = b"""*New in v17 (August 7, 2026):*
- **Phase 2 track structure added, and Tony's ordering ruling recorded.**
  Track 0 (constant layer scaffolding) precedes Track 1 (provenance
  batches) precedes Track 2 (Artifact 2). Reasoning: a golden artifact is
  fingerprinted, so locking one on unsourced values means redoing the
  lock. Supersedes the August 5 "clear all batches first" instruction,
  which is preserved as history rather than deleted.
- **L-181 promoted out of Prep Work into a phase track.** As reframed on
  August 6-7 it carries one store, a citation-form migration, derivation
  across five restatement surfaces, a generator, a cross-repo transport,
  and a load-time validation pass. That is phase-scale work, and leaving
  it in Section 6 was why the August 6-7 design session kept expanding --
  implementation questions were being answered against no scope boundary.
- **Six open decisions added to Section 7** (12-17): transport form,
  generator shape (dissolved), the L-179/L-180 values, validation layers,
  pilot-slice sequencing, and the interpolation locus.
- **Two Fable 5 design reviews, August 2026** (round 1 at orrery
  `ee0da47c`, round 2 at `754f46b`; zero code in either). Architecture
  endorsed in round 1; transport endorsed in round 2. All findings from
  both rounds independently verified by Claude Opus 5 at the review
  anchors before being recorded.
- **Round 1 findings the predesign handoff missed:**
  `spectral_subclass_temps` is an uncited physical claim inside the store
  itself, so the convention must apply at home before it is enforced
  outward; `KNOWN_ORBITAL_PERIODS` carries the key `'Phobos'` twice (133
  keys, one duplicate, same value today) -- Python silently keeps the
  last, which is the argument for a validation pass; the module-level
  `*_info` tooltip strings are a FIFTH restatement surface (Uranus
  restates 25,559 km nine times and does arithmetic in prose), and had
  derivation covered dict descriptions but not these, the `*_info`
  strings would have become the surviving duplicate -- L-182's exact
  shape, which the build was on course to recreate; and the gallery
  constant enumeration missed four sites including three BARE literals
  `149597870.7` inline in `gallery_studio.py`.
- **The transport question was reopened after round 1 by Tony
  questioning three premises this session supplied and never checked.**
  (1) "The exporter" was written as though pointing at something live; it
  is dormant. (2) The store's 7 derived constants were written up as a
  complication; they are the store's own stated principle working, and
  `SOLAR_RADIUS_AU` alone has 11 consumers. (3) The claim that the
  gallery could not execute the file was never tested; `constants_new.py`
  imports only numpy and `datetime`, and the builder already hard-depends
  on numpy through astroquery. Each error was Claude reading code and
  treating that as knowing the system. Removing the premises produced
  fetch-and-import, which is simpler than everything that preceded it.
- **Round 2 findings.** `numpy` and `timedelta` are imported by
  `constants_new.py` and never used -- Track 0 should drop both, making
  the store stdlib-only and removing the version-skew surface between the
  two environments. A pre-import gate is recommended: parse the fetched
  file with `ast` and check exactly two structural properties -- imports
  on an allowlist, and no duplicate dict keys -- then hand off to import
  for everything else. That recovers the one capability fetch-and-import
  loses, since after import Python has already silently kept the last
  duplicate and the Phobos class becomes invisible. Track 0 should also
  define a single-name contract, `FEATURE_REGISTRY`, that the builder
  reads and nothing else; every rename or regrouping inside the store
  then stays internal, and the only breaking change left is renaming the
  registry itself.
- **Correction to a round 2 recommendation, verified against the store.**
  Fable recommended a strict `inner_radius_km < outer_radius_km`
  invariant and stated it catches nothing spurious today. It would fire
  on 8 Neptune entries where inner and outer are deliberately equal --
  narrow ringlets modelled at a single radius. Use `inner <= outer`. The
  directional claim holds: `inner > outer` is genuinely zero across all
  33 ring pairs.
- **Coupling requirement recorded as a Track 0 exit criterion in L-181**
  rather than as its own ledger item, per Tony: do not multiply handles.
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
     b"**Last updated:** August 7, 2026"),

    ('v17-2', 'Phase 2 track structure',
     b"Gate: scene equivalence (Mode 5) + the gallery page ships.\n\n### Phase 3",
     PHASE2_TRACKS),

    ('v17-3', 'Section 6: Track 0 precedes Batch 2',
     b"Batch 2 is now the stated gate before Artifact 2 (Tony, 2026-08-05):",
     b"AMENDED v17 (Tony, 2026-08-07): Track 0 (constant layer scaffolding)\n"
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
