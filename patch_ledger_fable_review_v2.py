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
<!-- L:186 status:OPEN upd:2026-08-06 section:A flag: rice:3/3/80/2 -->
- Scanner reports 12 annotation lines it saw but could not use. None
  changed a score. They matter because an annotation that quietly does
  nothing reads as a completed cross-check to anyone skimming the source.
- Tony ruled 2026-08-06: clear these BEFORE Batch 2 rather than during,
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
<!-- L:187 status:OPEN upd:2026-08-06 section:A flag: rice:3/3/60/3 -->
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

L181_ADD = b"""- **FABLE DESIGN REVIEW, 2026-08-06** (built on orrery `ee0da47c` /
  gallery `61a78c0`; zero code). Architecture ENDORSED: one store, three
  zones per entry, provenance as data, derivation instead of annotation,
  exporter aborting on a missing source. Every piece extends an existing
  pattern rather than inventing one. All findings below independently
  verified by Claude Opus 5 at the same anchors before recording.
- **Transport form: three candidates, none ruled. Option 3 leading.**
  (1) Export then fetch -- something in the orrery writes a JSON artifact;
  the builder fetches it at the orrery HEAD SHA, validates shape +
  source-presence + content hash, and commits it with the nightly output
  (Fable's "vendored pull": fetch it AND commit the copy, so an
  unreachable orrery falls back to last night). (2) JSON as the source of
  truth -- no generation, but the scanner reads `.py` only, so the source
  would be invisible to it. (3) Builder extracts directly -- fetch
  `constants_new.py` as TEXT at the orrery HEAD SHA and read the values
  out with Python's `ast` module, parsing structure without executing the
  file. No exporter, no new step in Tony's workflow, no scheduled job
  committing into the orrery repo. Not a novel technique:
  `provenance_scanner.py` line 899 already does this to the same file.
  Under every option the failure path is the same -- quarantine, keep
  serving the last good copy, warn loudly.
- **Option 3 surfaced only after Tony questioned the premise.** Both the
  predesign handoff and Fable's review wrote "the exporter" as though
  pointing at something live. Once that assumption was removed, the
  export step turned out to be optional rather than structural. This is a
  material change from what Fable reviewed, so it goes back for a second
  look before anything is built. See master plan Section 7 decision 12.
- The reframe that dissolved the fork: self-containment is TWO
  properties, not one. Render-time self-containment (the assembler
  reconstructing alone from the cache) is what the protocol protects, and
  pull never touches it. The network dependency lands in the BUILDER at
  build time -- already network-dependent via Horizons, already
  committing fetched external data nightly. Push-vs-pull was a false
  binary; the vendored form is the third option. It also resolves the
  pin-vs-HEAD tension: track HEAD at fetch time, pin by record in git
  history, so every nightly commit is a reproducible snapshot.
- Claude Opus 5 addition: the builder should SURFACE the orrery SHA lag
  ("features stale as of orrery <SHA>"), not merely log it. That also
  covers the third staleness vector -- a build that did not run at all
  (Tony's machine off, 2026-08-06) presents identically to one that ran
  and failed, from the served side.
- **Store-internal findings -- the convention must apply at home before
  it is enforced outward.** (1) `spectral_subclass_temps` is a numeric
  physical claim with no citation of any kind; it belongs in the
  citation-form migration or gets an explicit carve-out ruling.
  (2) `color_map()` and `stellar_class_labels` are presentation living
  untagged in the store; tag them under the same three-zone convention.
  (3) `KNOWN_ORBITAL_PERIODS` contains the key `'Phobos'` TWICE (both
  0.319, verified: 133 keys, one duplicate). Same value today, so
  harmless -- but Python silently keeps the last, which is the exact
  silent-drift class this design exists to kill. It is the argument for a
  load-time validation pass over the store (duplicate keys, source
  presence on physics fields, unit sanity). The exporter's abort is
  generation-time; this is the matching import-time check.
- **Fifth restatement surface, missed by the handoff's count.** The
  handoff counted `description` fields inside the params dicts. The four
  shell modules ALSO carry module-level `*_info` strings imported by
  `palomas_orrery.py` for Tk GUI tooltips -- a different consumer.
  Verified: Uranus restates 25,559 km nine times and does arithmetic in
  prose ("25,559 km + 50 km = 25,609 ... fraction ~1.002"); Neptune's
  Galle info restates "41,900-42,900 km". Counts of module-level `*_info`
  strings: jupiter 10, saturn 10, uranus 8, neptune 8. If interpolation
  covers dict descriptions but not these, the `*_info` strings become the
  surviving duplicate and the next consistency pass harmonizes toward
  them -- L-182's exact shape, which the build was on course to recreate.
  Include in derivation scope or defer explicitly.
- **Three prose cases resist naive interpolation; use them as the
  acceptance test set.** (1) Jupiter main ring: prose says "about
  30-300 km" against a stored scalar `thickness_km` of 30. (2) Neptune
  Galle: "41,900-42,900 km" where the stored pair is inner/outer radius,
  derivable but not by naive field substitution. (3) Uranus atmosphere
  info: arithmetic performed in prose. These need a small schema answer
  (optional range field, derived value computed in code, or a documented
  per-case carve-out). This is Tony's acceptance test in miniature: if
  the schema absorbs these three cleanly the architecture is right; if
  many more surface, that is the signal.
- **Sequencing rule for the scanner change.** Land the SOURCE_PATTERNS
  extension ALONE, run the full scan, diff the finding set against the
  prior audit, and attribute any newly-exposed pre-existing findings to
  the scanner change BEFORE the citation migration lands. Otherwise the
  migration diff and the scanner diff interleave and neither is
  auditable. (Precedent: a unit-vocabulary extension once exposed a
  pre-existing Tier-1 in `star_notes.py`.)
- **The 17 citation-level mismatches ride here, not as a separate fix.**
  Scanner diagnostic at `ee0da47c`: 11 in `planet_visualization_utilities.py`
  (one per body in `PLANET_ROTATION`, shadowed from the block citation at
  491) and 6 in `comet_visualization_shells.py` (shadowed from
  `HISTORICAL_TAIL_DATA` at 86). Nothing is mis-scored today; the flat
  60-line context window catches them independently, which is why the
  mismatch is easy to miss. The mechanical fix -- repeat a short citation
  above each inner key -- would write 17 NEW citation copies into files
  this item is about to restructure. Under the data-field design each
  entry carries its own `source` and nothing can be shadowed by
  construction. Track, do not patch.
- **Filename collision to resolve in this build.** Two files are already
  named `feature_configs.json` (orrery exporter writes one, gallery
  builder writes another). Under vendored pull that becomes three. The
  orrery artifact should either replace `objects_config.json`'s features
  block outright or take a distinct name. Same-name-different-content
  across repos is a standing trap for every future session and for the
  scanner.
- **Schema uniformity.** The gallery copy drops `thickness_km` for Saturn
  while keeping it for Jupiter (verified at `61a78c0`) -- an artifact of
  hand-seeding. The generated artifact must emit a uniform schema.
- **Do NOT teach the scanner JSON.** Fable's answer to the handoff's
  closing question: extend provenance into config JSON via the
  generator's abort-on-missing-source and the builder's validation gate,
  not by widening the scanner's `.py`-only filter. The artifact's own
  validation is the compensating control.
- **GATE: settle L-179 and L-180 BEFORE the migration transports their
  values.** Both are drift inside the store today. Migrating and deriving
  first would carry a known-inconsistent value into the gallery, the
  served cache, and the hover text, now looking authoritative in three
  more places. The handoff's own "presence is not truth" warning applies
  to its own build order.
- **PROMOTED TO PHASE 2 TRACK 0 (Tony's ruling, 2026-08-06).** The order
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
  (c) unit-sanity range checking is in place -- shape validation and
      source-presence validation BOTH pass on a value whose units
      changed, so neither catches a km-to-AU slip (master plan decision
      15);
  (d) the store-to-builder coupling is documented on BOTH sides. Under
      option 3 the builder depends on the store's dict NAMES and SHAPE,
      not its values: value edits, new entries, new bodies and comment
      changes flow through untouched, while renames, field renames,
      nesting changes and file moves break the extractor. A note placed
      on only one side reaches only one of the two editors -- the L-182
      shape again. The three places: a comment at the feature block in
      `constants_new.py` (catches the editor mid-edit, rank this first),
      a field note in `provenance-discipline` (fires on any
      `constants_new.py` work), and a field note in
      `gallery-cache-builder` (fires from the consumer side).
- **Build the extractor AFTER Track 0 settles the shape**, not before.
  Track 0 is itself a restructure -- it moves 37 entries into the store
  and adds `source` fields -- so an extractor written first would be
  chasing a shape about to change. Related benefit worth noting: today
  the `*_params` dicts are function-local, which is awkward to extract
  reliably; after Track 0 they are module-level, which is the easy case.
  Track 0 also narrows the coupling from four rendering modules to one
  file.
- **L-179/L-180 change role under this order.** They were a gate standing
  in front of the migration. They are now the FIRST thing Track 0 fixes.
  Same requirement, better placement.
- Correction worth carrying: `export_orbit_cache.py` is a DORMANT Phase
  1b seeding tool, not a live exporter. Nothing calls or imports it; all
  four tooling maps classify it `dev_tools`; the gallery references it
  only as a historical porting source at orrery `4e2629c`. The August 6
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
     b"  2026-08-06; Fable sequencing note). Migrating and deriving before\n"
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
     b"- **FIRST STEP OF PHASE 2 TRACK 0** (2026-08-06). Same reasoning as\n"
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
    print("  - transport form (opt 3 leading)   plan sec 7 #12")
    print("  - generator shape (opt 1 only)     plan sec 7 #13")
    print("  - unit-sanity validation           plan sec 7 #15")
    print("  - L-179 / L-180 values             plan sec 7 #14, Track 0 step 1")
    print("  - annotation parser ruling         [L-186], Track 1")
    return 0


if __name__ == '__main__':
    sys.exit(main())
