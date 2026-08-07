# -*- coding: utf-8 -*-
"""patch_ledger_fable_review_v2.py -- record the Fable design review AND
Tony's C-then-B-then-A ordering ruling, and close out the three items
left floating on August 6.

RUN patch_masterplan_v17.py FIRST. This patch records ledger state that
assumes the master plan already carries the Phase 2 track structure.

Built on ee0da47c483cda02ac035d48ce99bc855a56e03c
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned at 61a78c00668573dbff111ec9f10a96b1cd2fdc35.

HOW TO RUN
    Save this file in the REPO ROOT (the folder holding
    LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    Success: five "ok" lines, then "patch applied".
    Failure: one "ANCHOR FAIL" or "ERROR" line, then "NOTHING WAS
    WRITTEN". The ledger is unchanged either way.

AFTER RUNNING
    Run ledger_index.py. Two new L-handles are added, so the index is
    stale until you do.

WHAT CHANGES

  F-1  [L-181] gains the Fable review outcome: the vendored-pull
       recommendation (still awaiting Tony's decision -- recorded as
       RECOMMENDED, not ratified), four store-internal findings, the
       *_info fifth restatement surface, the three prose test cases, the
       SOURCE_PATTERNS sequencing rule, the filename collision, and the
       L-179/L-180 gate.

  F-2  [L-185] gains four sites the handoff enumeration missed, the
       orrery-side shadow constant, and Fable's ruling that arithmetic
       constants stay in code rather than riding the pulled artifact.

  F-3  [L-179] and [L-180] marked as GATING the L-181 migration.

  F-4  New [L-186] -- the 12 cross-check annotation issues, to clear
       before Batch 2, carrying the parser question.

  F-5  New [L-187] -- info_dictionary numeric-overlap enumeration,
       explicitly deferred out of the L-181 build.

NOTE ON WHAT IS AND IS NOT DECIDED
    Vendored pull is Fable's RECOMMENDATION and Claude Opus 5's
    endorsement. Tony has not ruled. It is recorded as an open
    Tony-action (decide) so a future session does not read the
    recommendation as a ruling. Same for L-179 and L-180 values.

Patch written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
BASE_MD5 = 'cc983fd356090aaa7d5f45d04a29f84b'

NEW_ITEMS = b"""#### [L-186] Cross-check annotation issues -- clear before Batch 2
<!-- L:186 status:OPEN upd:2026-08-07 section:A flag: rice:3/3/80/2 -->
- Scanner reports 12 annotation lines it saw but could not use. None
  changed a score. They matter because an annotation that quietly does
  nothing reads as a completed cross-check to anyone skimming the source.
- Tony ruled 2026-08-07: clear these BEFORE Batch 2 rather than during,
  since Batch 2 will add more annotations of the same kind.
- **Six `duplicate_identity`** -- two or more annotations naming the same
  checker on one claim, which cannot earn V2 (V2 needs two DIFFERENT
  checkers). Sites: `constants_new.py` 388, `eris_visualization_shells.py`
  218, `mercury_visualization_shells.py` 49,
  `pluto_visualization_shells.py` 41, `shell_configs.py` 128,
  `venus_visualization_shells.py` 528. Each needs a look at the source:
  either one annotation is redundant, or a checker name is wrong. Data
  question, not a mechanical fix.
- **Six `non_markdown_reference`**, splitting two ways. Three in
  `constants_new.py` (124, 152, 293) say "(Gemini worksheet)" with no
  filename at all -- genuinely incomplete, supply the real worksheet
  name. Three in `eris_visualization_shells.py` 478 (x2) and
  `venus_visualization_shells.py` 681 DO name the `.md` file but append
  the checked value, e.g. `(batch1_tier2_followup_gpt.md: 14.27 Mkm)`.
  The parser tests that the parenthetical ENDS in `.md`, so a richer
  annotation is rejected for carrying more provenance, not less.
- Tony-action (decide): strip the appended values to satisfy the parser,
  or extend the pattern to accept `(worksheet.md: value)`. Claude's lean
  is to extend, since the format currently punishes better annotations --
  but this is adjacent to "do not loosen a checker to clear findings," so
  the ruling is Tony's. If extended, it is a scanner change and should
  follow the same land-scan-diff sequencing as the SOURCE_PATTERNS work
  in L-181.
- **Sequencing under the v17 order:** Track 1 work, so it now follows
  Track 0. That is a real gain -- Batch 2 and this cleanup both write
  into whatever citation form Track 0 establishes, rather than writing
  comment-form annotations Track 0 would then migrate.
**Gap:** Six data questions, three fill-in-the-filename fixes, one parser
ruling.
**Ref:** PROVENANCE_AUDIT.md, CROSS-CHECK ANNOTATION ISSUES section, at
`ee0da47c`.

#### [L-187] info_dictionary numeric-overlap enumeration
<!-- L:187 status:OPEN upd:2026-08-07 section:A flag: rice:3/3/60/3 -->
- Fable review, Open Question 2(d): do NOT extend the L-181 interpolation
  migration into `info_dictionary.py` now. Applied literally, the
  derivation rule would pull every numeric claim in 2,248 lines of prose
  into scope -- a scope explosion contradicting the settled "one pass,
  bounded to the store" ruling.
- The principled boundary Fable proposes: where a number in INFO prose
  DUPLICATES a stored constant, interpolate it (it is a two-copy pair at
  L-182 risk); where a number exists ONLY in prose, it stays prose with
  its `# Source:` comment -- provenance on narrative, a different job.
- The preparatory task is therefore an ENUMERATION, not a migration:
  which `info_dictionary.py` numbers duplicate store constants. A one-off
  script or a scanner extension.
- Context: `info_dictionary.py` carries 62 `# Source:` comments and was
  deliberately split from `constants_new.py` to separate narrative
  content (fact-checked) from numeric constants (source-cited). It is
  also one of three orrery modules `gallery_studio.py` imports directly,
  via function-local imports a header-only import walk misses.
**Gap:** Write the enumeration. Then decide scope from real numbers.
**Ref:** FABLE_REVIEW_feature_constant_unification.md, Open Question 2(d)
and findings summary #5.

"""

L181_ADD = b"""- **FABLE DESIGN REVIEWS, ROUNDS 1 AND 2, AUGUST 2026** (built on orrery `ee0da47c` /
  gallery `61a78c0`; zero code). Architecture ENDORSED: one store, three
  zones per entry, provenance as data, derivation instead of annotation,
  exporter aborting on a missing source. Every piece extends an existing
  pattern rather than inventing one. All findings below independently
  verified by Claude Opus 5 at the same anchors before recording.
- **Transport form: FETCH-AND-IMPORT.** Recommended by Claude Opus 5,
  endorsed by Fable 5 round 2, NOT YET RATIFIED by Tony. The nightly
  builder resolves the orrery HEAD SHA, fetches `constants_new.py` as
  text at that SHA, imports it, reads the feature values and their
  sources, validates, and writes into staging under existing atomic-swap
  semantics. Python evaluates all derivation natively. Tony's workflow
  does not change. Fable's summary: "round 1's vendored pull with the
  exporter removed -- same fallback property, same SHA recording, same
  quarantine semantics, strictly fewer moving parts, and zero hand
  steps."
- Two earlier candidates retired. Exporting a JSON artifact rests on a
  generation step and a run trigger that do not exist. Reading the file
  with `ast` without executing it fights the store's design: 7 of 45
  top-level assignments are derived rather than literal, and two contain
  constructor calls `ast.literal_eval` cannot evaluate at all.
- **Three premises were removed by Tony's questions to get here**, and
  the pattern is worth carrying: each was Claude reading code and
  treating that as knowing the system. (1) "The exporter" was written as
  live; it is dormant. (2) The 7 derived constants were written up as a
  complication; they are the store's own principle working, and
  `SOLAR_RADIUS_AU` alone has 11 consumers. (3) The claim that the
  gallery could not execute the file was never tested; the store imports
  only numpy and `datetime`, and the builder already hard-depends on
  numpy through astroquery.
- **Round 2 build requirements.** (a) Drop the dead `numpy` and
  `timedelta` imports from `constants_new.py` -- both are imported and
  never used, verified; the store becomes stdlib-only, removing the
  version-skew surface between environments. (b) Add a PRE-IMPORT GATE:
  parse the fetched file with `ast` and check exactly two structural
  properties -- imports on an allowlist, no duplicate dict keys -- then
  hand off to import. This is not a revival of ast-extraction; it reads
  no values. It recovers the one capability fetch-and-import loses: after
  import, Python has already silently kept the last duplicate, so the
  Phobos class becomes invisible. (c) Load via
  `importlib.util.spec_from_file_location` from the staging path with a
  per-run module name; never insert staging into `sys.path`. (d) Add a
  one-line rule to the store docstring: data-only module, no top-level
  I/O -- importing executes top-level code, so a future file write or
  network call would be inherited silently every night.
- **FEATURE_REGISTRY: shrink the contract to one name.** Track 0 defines
  a single dict in the store mapping body slug to that body's feature
  entries, and the builder reads exactly that name. Every rename,
  regrouping, or nesting change inside the store then stays internal; the
  only breaking change left is renaming the registry itself, which is one
  grep from impossible to miss. This is the mechanical answer to the
  coupling question, and it demotes the three documentation notes from
  load-bearing to descriptive.
- **PROMOTED TO PHASE 2 TRACK 0 (Tony's ruling, 2026-08-07).** The order
  is scaffolding, then provenance batches, then Artifact 2. Reasoning: a
  golden artifact is fingerprinted, so locking one on values that are not
  yet sourced and derived means redoing the lock rather than editing a
  number. Scaffolding first is the cheaper order, not the slower one.
  This supersedes the August 5 "clear all batches before Artifact 2"
  instruction -- batches still precede the artifact, but Track 0 now
  precedes the batches. See MASTER_PLAN_INTERACTIVE_GALLERY.md v17,
  Phase 2 track structure.
- This item left Prep Work because it outgrew it. As reframed it carries
  one store, a citation-form migration, derivation across five
  restatement surfaces, a generator, a cross-repo transport, and a
  load-time validation pass. That is phase-scale work, and leaving it in
  a section meant for small gating tasks is why the August 6 design
  session kept expanding -- implementation questions were being answered
  against no scope boundary.
- **Open decisions are SCOPED, not blocking.** Transport form, generator
  shape, and unit-sanity validation live in master plan Section 7 as
  decisions 12, 13 and 15. They are answerable once Track 0 has a scope
  boundary to answer them against; none of them gate starting Track 0.
- **TRACK 0 EXIT CHECKLIST for the transport piece.** Recorded here
  rather than as a separate ledger handle -- it is the same work, and
  multiplying handles buries rather than clarifies. The transport piece
  is NOT done until all of the following hold:
  (a) values flow from `constants_new.py` to the served cache with no
      hand step;
  (b) every physics value carries a source, enforced by an abort rather
      than a warning;
  (c) all four validation layers are in place (master plan decision 15):
      source presence as an ABORT not a warning; unit-sanity RANGE
      checking, since shape and source-presence validation both pass on a
      value whose units changed and only magnitude bounds catch a
      km-to-AU slip; a cross-field ring invariant using `inner <= outer`
      -- NOT Fable's strict `<`, which was verified against the store and
      would fire on 8 Neptune entries where inner and outer are
      deliberately equal (Le Verrier at 53,200 km, six Adams arcs at
      62,932 km; `inner > outer` is genuinely zero across all 33 pairs);
      and a nightly value-diff against last night's committed copy
      logging old, new, and both orrery SHAs, which is the only guard
      that sees CHANGE itself -- the L-182 family;
  (f) the JSON-serializability boundary is enforced: import yields live
      Python objects while the cache is JSON, and the store already holds
      a function (`color_map`) and a datetime (`HORIZONS_MAX_DATE`) at
      top level. Every value bound for the cache is coerced to plain
      int/float/str/list/dict; anything else is a validation failure, not
      a crash mid-write;
  (g) the interpolation locus is decided before the cache schema is
      written (master plan decision 17). Fable recommends builder-side
      pre-interpolation: it keeps the assembler dumb and moves template
      errors to build time where quarantine exists, rather than into a
      user's browser;
  (d) the store-to-builder coupling is reduced to the single
      `FEATURE_REGISTRY` name and documented on BOTH sides. Under
      fetch-and-import the builder reads NAMES, not structures, so
      nesting and shape changes no longer break it and only a rename
      does -- weaker coupling than the retired `ast` route implied. A
      note placed on one side reaches only one of two editors, the L-182
      shape again. Three places: a comment at the registry in
      `constants_new.py` (catches the editor mid-edit, rank first), a
      field note in `provenance-discipline` (fires on any store work),
      and a field note in `gallery-cache-builder` (fires from the
      consumer side).
  (e) the run manifest records BOTH the orrery SHA and the content hash
      of the fetched `constants_new.py` (`_write_run_manifest`, builder
      line 1476), so any served state traces to exact store bytes.
- **Sequencing within Track 0 is now open, not settled.** The earlier
  "build transport after Track 0" reasoning assumed a shape-sensitive
  extractor. Fetch-and-import is not shape-sensitive, which reopens it.
  Fable round 2 recommends a PILOT SLICE: migrate Jupiter (5 entries)
  through the full Track 0 treatment, build the transport end-to-end
  against it, then scale to the remaining 32 -- which needs zero
  transport rework. The argument: the transport cannot be tested against
  today's store at all, since no `source` fields exist for
  abort-on-missing-source to act on, so "transport after Track 0" really
  means "first end-to-end test after all 37 entries move," the largest
  possible batch before the first proof. Jupiter also holds the
  resistant-prose cases. Cost: two passes over the migration tooling.
  Tony-action (decide); master plan Section 7 decision 16.
- **L-179/L-180 change role under this order.** They were a gate standing
  in front of the migration. They are now the FIRST thing Track 0 fixes.
  Same requirement, better placement.
- Correction worth carrying: `export_orbit_cache.py` is a DORMANT Phase
  1b seeding tool, not a live exporter. Nothing calls or imports it; all
  four tooling maps classify it `dev_tools`; the gallery references it
  only as a historical porting source at orrery `4e2629c`. The August 6-7
  session twice built on the assumption it was live and Tony corrected it
  both times. Whatever generates the feature artifact is a NEW
  responsibility, and "run something before pushing" is a habit that does
  not exist today -- a real cost to weigh in decision 13, not a detail.
"""

L185_ADD = b"""- **Scope additions, 2026-08-06.** Tony approved folding in the
  orrery-side shadow constant found by the same scanner run:
  `orbit_data_manager.py:1850`, `KM_TO_AU`, classed `derived` (computed
  from pinned literals rather than from the imported name). Here the
  standard remedy IS available -- delete the local definition and import
  -- and the audit is explicit that adding a `# Source:` would
  cite-to-clear a structural problem.
- **Fable review found four more gallery sites the handoff enumeration
  missed** (verified at `61a78c0`): `tools/gallery_studio.py` lines 1035,
  1051, 5520 carry BARE LITERALS `149597870.7` inline in expressions, not
  even assigned to a named constant -- worse than every enumerated case,
  violating assign-don't-hardcode on top of being uncited.
  `tools/gallery_cache_builder.py` lines 127 and 135 use `2440587.5`
  inline (the docstring at 123 explains it; the citation shape is
  absent). `tools/test_gallery_cache_builder_offline.py:34`
  `_MOCK_K_GAUSS` carries an in-repo mirror comment but no physical
  source -- a mirror note is not a citation; once `render_orbits.py`'s
  citation lands, the mock should point at it.
- Running total: roughly eight sites, one bounded hand pass.
- **Fable ruling, endorsed: keep the arithmetic constants in CODE.** The
  temptation under vendored pull is to let `AU_KM` and `K_GAUSS` ride
  along in the artifact. Do not. They are exact-by-definition or
  conventional, so making the assembler's arithmetic depend on a cache
  read adds a failure mode (cache unreadable means no math at all) for
  zero drift benefit. The line-89 cross-repo citation is the right
  remedy.
- Refinement worth taking: once the vendored artifact exists and records
  the orrery SHA per build, new citations can reference "orrery SHA per
  feature artifact" rather than a hand-typed SHA that goes stale.
"""

EDITS = [
    ('F-1', 'L-181: Fable review outcome',
     b"**Note:** Architecture comes before Batch 2 -- Tony's deliberate\n"
     b"reversal of \"clear all batches first,\" 2026-08-06.",
     L181_ADD +
     b"**Note:** Architecture comes before Batch 2 -- Tony's deliberate\n"
     b"reversal of \"clear all batches first,\" 2026-08-06.\n"
     b"**Ref:** FABLE_REVIEW_feature_constant_unification.md (orrery\n"
     b"`ee0da47c` / gallery `61a78c0`);\n"
     b"PREDESIGN_HANDOFF_feature_constant_unification.md."),

    ('F-2', 'L-185: missed sites + keep-constants-in-code ruling',
     b"**Gap:** Five lines. Can ship independently of L-181; should not wait on a\n"
     b"structural build.",
     L185_ADD +
     b"**Gap:** About eight sites now. Can still ship independently of L-181;\n"
     b"should not wait on a structural build."),

    ('F-3a', 'L-179: gates the L-181 migration',
     b"**Gap:** Resolve which value is authoritative. Update the loser.\n"
     b"**Ref:** FABLE_shell_consistency_audit_report.md findings #29-30.",
     b"- **FIRST STEP OF PHASE 2 TRACK 0** (Tony's ordering ruling,\n"
     b"  2026-08-07; Fable sequencing note). Migrating and deriving before\n"
     b"  this value is settled would transport a known-inconsistent number\n"
     b"  into the gallery artifact, the served cache, and the hover text --\n"
     b"  authoritative-looking in three more places. Settle it first, as\n"
     b"  Track 0 work rather than as a gate in front of Track 0.\n"
     b"**Gap:** Resolve which value is authoritative. Update the loser.\n"
     b"**Ref:** FABLE_shell_consistency_audit_report.md findings #29-30;\n"
     b"FABLE_REVIEW_feature_constant_unification.md sequencing note."),

    ('F-3b', 'L-180: gates the L-181 migration',
     b"**Gap:** Reconcile text, add Show-the-Envelope comment.\n"
     b"**Ref:** FABLE_shell_consistency_audit_report.md finding #31.",
     b"- **FIRST STEP OF PHASE 2 TRACK 0** (2026-08-07). Same reasoning as\n"
     b"  L-179: do not transport an unsettled value into three more places.\n"
     b"**Gap:** Reconcile text, add Show-the-Envelope comment.\n"
     b"**Ref:** FABLE_shell_consistency_audit_report.md finding #31;\n"
     b"FABLE_REVIEW_feature_constant_unification.md sequencing note."),

    ('F-4/5', 'insert L-186 and L-187',
     b"\n## PENDING ACTION (Tony-side)\n",
     b"\n" + NEW_ITEMS + b"## PENDING ACTION (Tony-side)\n"),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(root, TARGET)
    if not os.path.exists(path):
        print("ERROR: %s not found." % TARGET)
        print("       Save this script in the REPO ROOT.")
        print("       NOTHING WAS WRITTEN.")
        return 1

    with open(path, 'rb') as f:
        data = f.read()

    norm = 0
    if b'\r\n' in data:
        norm = data.count(b'\r\n')
        data = data.replace(b'\r\n', b'\n')
        print("fix CRLF     %s: normalized %d line endings to LF" % (TARGET, norm))

    got = hashlib.md5(data).hexdigest()
    if got != BASE_MD5:
        print("ERROR: %s base does not match." % TARGET)
        print("       expected md5 %s" % BASE_MD5)
        print("       found    md5 %s" % got)
        print("       The ledger changed since this patch was written.")
        print("       NOTHING WAS WRITTEN. Re-pull and rebuild.")
        return 1

    for eid, label, old, new in EDITS:
        c = data.count(old)
        if c != 1:
            print("ANCHOR FAIL: %s (%s) matched %d, expected 1." % (eid, label, c))
            print("             NOTHING WAS WRITTEN. The ledger is unchanged.")
            return 1

    for eid, label, old, new in EDITS:
        data = data.replace(old, new, 1)
        print("ok  %-7s %s" % (eid, label))

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
    print("  %s" % TARGET)
    print("")
    print("NEXT: run ledger_index.py -- two new handles were added.")
    print("")
    print("PHASE 2 ORDER (master plan v17): Track 0 scaffolding ->")
    print("Track 1 provenance batches -> Track 2 Artifact 2.")
    print("")
    print("OPEN, and none of them block starting Track 0:")
    print("  - ratify fetch-and-import          plan sec 7 #12")
    print("  - pilot slice inside Track 0       plan sec 7 #16")
    print("  - interpolation locus              plan sec 7 #17")
    print("  - L-179 / L-180 values             plan sec 7 #14, Track 0 step 1")
    print("  - annotation parser ruling         [L-186], Track 1")
    return 0


if __name__ == '__main__':
    sys.exit(main())
