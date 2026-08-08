"""
patch_capture_20260807b.py

Captures the design rulings and findings from the second half of the
August 7 session.

Built on 9b4f2788ea0a95ac5c51489219020c5864898f6e at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
with gallery findings verified at 33fc7d68d26f24e686a88f2169b79f0a4903a2ef
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.

HOW TO RUN
    Save this file into the palomas_orrery folder (the one holding
    LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

WHAT IT DOES
    LEDGER_CONSOLIDATED.md
        L-181  Tony's store ruling; corrected entry counts; the belt and
               torus surface enumerated; registry structure named as a
               design task
        L-154  resolver bug re-verified at gallery HEAD; the block is
               reclassified -- provenance is not the nearest blocker
        + L-190  Scanner reach rule: anything rendered from sourced data
               must be reachable by the scanner
    documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md
        the 37 / 32 / 33 entry counts corrected and reconciled

AFTER RUNNING
    1. Run ledger_index.py (dashboard > Developer Tools).
    2. Commit and push in GitHub Desktop.

SAFETY
    Content-fingerprinted (line endings normalized before hashing), every
    anchor asserted to match exactly once, line endings preserved per
    file, binary mode throughout. Any mismatch aborts with NOTHING WAS
    WRITTEN.

Module updated: August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import pathlib
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
PLAN = 'documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md'

FINGERPRINTS = {LEDGER: '01d3c19d3b600d6a2f6c0f304e1964c1', PLAN: 'f998a695e294ea763f118fc21258bd84'}

EDITS = {}

EDITS[LEDGER] = [
    (
        "L-181: correct the counts and enumerate the belt/torus surface",
        b"- **Scope widened to three layers.** (1) 37 feature entries move out of\n"
        b"  `jupiter_`/`saturn_`/`uranus_`/`neptune_visualization_shells.py` into\n"
        b"  `constants_new.py`.",

        b"- **COUNT CORRECTED 2026-08-07.** The \"37 entries\" figure was never\n"
        b"  sourced and does not match the code. Enumerated by AST walk over the\n"
        b"  four shell modules at `9b4f278`: **33 ring entries** -- Jupiter 4\n"
        b"  (Main, Halo, Amalthea Gossamer, Thebe Gossamer), Saturn 7, Uranus 11,\n"
        b"  Neptune 11. Jupiter is 4, not the 5 the August 7 handoff stated.\n"
        b"- **A SECOND SURFACE exists and was in neither count.** Radiation belts\n"
        b"  and plasma tori carry geometry as BARE LITERALS inside function\n"
        b"  bodies, not as dicts with `inner_radius_km`: Jupiter\n"
        b"  `io_torus_distance=5.9`, thickness 2, width 1, `belt_distances=\n"
        b"  [1.5, 3.0, 6.0]`, `belt_thickness=0.5`; Saturn\n"
        b"  `enceladus_torus_distance=3.95`, thickness 1, width 2,\n"
        b"  `belt_distances=[2.7, 3.5, 4.4, 5.6, 7.4, 9.0]`, thickness 0.5;\n"
        b"  Uranus `belt_distances=[2, 6]`, thickness 0.5; Neptune dict-keyed on\n"
        b"  `thickness`. About 22 physical values in FOUR different shapes, and\n"
        b"  ZERO carry a `# Source:` comment. These are inside Artifact 2, which\n"
        b"  the plan defines as \"Jupiter/Saturn, rings + radiation belts.\"\n"
        b"- **Tony's ruling 2026-08-07 on their status:** the belt dimensions are\n"
        b"  NOT arbitrary. They are RANGES, and the modeling can use the ranges\n"
        b"  or interpolate within them -- the same treatment L-179 gave the solar\n"
        b"  gravitational influence. Where a value is genuinely a style choice\n"
        b"  (belt thickness for visibility, how many shells to draw), Tony\n"
        b"  decides and it is declared as such. An earlier framing of these as\n"
        b"  \"drawing choices\" was wrong and is withdrawn.\n"
        b"- **REGISTRY STRUCTURE IS A DESIGN TASK (Tony, 2026-08-07).** One\n"
        b"  `FEATURE_REGISTRY` has to hold rings (dict, inner/outer/thickness),\n"
        b"  belt sets (list of distances plus a scalar), and tori (three\n"
        b"  scalars). Tony: \"we need a structure for this data. it will extend\n"
        b"  to other bodies.\" Design the shape BEFORE the migration, because the\n"
        b"  migration writes into whatever it defines.\n"
        b"- **Scope widened to three layers.** (1) The feature entries above move\n"
        b"  out of `jupiter_`/`saturn_`/`uranus_`/`neptune_visualization_shells.py`\n"
        b"  into `constants_new.py`.",
    ),
    (
        "L-181: Tony's store ruling and the served-state findings",
        b"**Gap:** Blocked on Fable architecture review (sent 2026-08-06). Then\n"
        b"design the store format, decide on dead tooltip fields, sequence\n"
        b"migration per body. L-184's build path cannot be defined until this\n"
        b"settles.\n",

        b"- **TONY'S RULING 2026-08-07: `constants_new.py` IS THE STORE, and\n"
        b"  `objects_config.json` stops carrying feature values.** The `features`\n"
        b"  key is emptied and the store owns them. His reasoning: two files\n"
        b"  claiming the same value violates single-source-of-truth, and the\n"
        b"  frozen-file rule on `objects_config.json` \"is a rule we can't observe\n"
        b"  either way, to keep it current\" -- so freezing it does not protect\n"
        b"  anything that matters. This settles the ownership question the\n"
        b"  cross-repo scope note above raised but did not rule on.\n"
        b"- **Why it had to be ruled.** The builder assembles\n"
        b"  `feature_configs.json` from `objects_config.json`'s `features` key\n"
        b"  (`features_out[slug] = feats`). Track 0 would have the builder import\n"
        b"  `FEATURE_REGISTRY` instead. With both in place the builder picks one\n"
        b"  silently: edit the store, and if it still reads the config your edit\n"
        b"  never reaches the cache while every freshness signal stays green.\n"
        b"  That is the L-182 shape -- one value, two homes, no rule.\n"
        b"- **SERVED STATE MEASURED 2026-08-07** (gallery `33fc7d6`), and it is\n"
        b"  not what the project assumed. The hand-copy was INCOMPLETE when made,\n"
        b"  not merely stale. Jupiter: 4 of 4 rings with all three fields, plus\n"
        b"  belts -- every value matching the orrery EXACTLY. Saturn: 7 of 7\n"
        b"  rings but `thickness_km` absent on all seven, and NO radiation belts\n"
        b"  or Enceladus torus at all. Uranus and Neptune: nothing served, and\n"
        b"  neither slug exists in `objects_config.json`'s twelve. So the\n"
        b"  transport's job is not \"keep a synced copy fresh\" -- it is \"serve\n"
        b"  data that has never been served.\" No drift found in what IS served.\n"
        b"- **Which makes Jupiter the right pilot for a better reason than size:**\n"
        b"  it is the only body whose served feature data is complete and\n"
        b"  correct, so the transport has a real acceptance test. Stage 1,\n"
        b"  reproduce Jupiter's existing `feature_configs.json` entry exactly\n"
        b"  plus `source` fields -- proves the transport is faithful. Stage 2,\n"
        b"  serve something never served (the Io torus, or Saturn's\n"
        b"  `thickness_km`) -- proves it can extend the cache, which is the\n"
        b"  actual job. Neither 5 entries nor 12: 4 rings plus 2 belt values to\n"
        b"  match, then one new thing to prove extension.\n"
        b"- **Artifact 2 cannot be built from today's served data** regardless of\n"
        b"  how good the rendering layer is. Saturn's radiation belts are not in\n"
        b"  the cache, and Artifact 2 is defined as rings PLUS radiation belts.\n"
        b"**Gap:** Fable review complete (rounds 1 and 2, August 2026). Remaining\n"
        b"before build, in order: (a) **(decide)** ratify fetch-and-import;\n"
        b"(b) **(design)** the `FEATURE_REGISTRY` shape covering rings, belt sets\n"
        b"and tori; (c) **(design)** the migration shape and per-body sequence;\n"
        b"(d) decide on the 124 dead tooltip fields. L-184's build path cannot be\n"
        b"defined until this settles.\n",
    ),
    (
        "L-154: resolver bug re-verified, block reclassified",
        b"<!-- L:154 status:BLOCKED upd:2026-07-28 section:W.Active flag: rice:3/3/70/3 -->\n",

        b"<!-- L:154 status:BLOCKED upd:2026-08-07 section:W.Active flag: rice:3/3/70/3 -->\n"
        b"- **RE-VERIFIED 2026-08-07 at gallery HEAD `33fc7d6`, and the block is\n"
        b"  reclassified.** `gallery/assembler/resolver.py` line 133 STILL reads\n"
        b"  `features = tuple(rec.get(\"features\") or ())`. Failure reproduced\n"
        b"  directly this session: `{'ring_system': {'main_ring':\n"
        b"  {'inner_radius_km': 122500}}}` collapses to `('ring_system',)`.\n"
        b"  Third independent verification (2026-07-27 Fable, 2026-07-28 Sonnet,\n"
        b"  2026-08-07 Opus 5), each at a different HEAD.\n"
        b"- **Why the reclassification.** This entry is carried as blocked on the\n"
        b"  L-155-162 provenance cluster. That is true but it is not the NEAREST\n"
        b"  blocker, and reading it as the only one is misleading. Even with a\n"
        b"  perfect transport and perfectly sourced values, the resolver discards\n"
        b"  every parameter one step before anything could draw them. The\n"
        b"  resolver fix is small, independent of ALL provenance work, and can\n"
        b"  proceed at any time. Confirmed the same day: nothing on the client\n"
        b"  reads `feature_configs.json` at all -- zero references in any JS or\n"
        b"  HTML. The file is written nightly into the cache and no code reads\n"
        b"  it.\n"
        b"- Note the surfaces are distinct: `index.html` is the STATIC curated\n"
        b"  gallery and never needed feature data; `interactive.html` is the\n"
        b"  assembler surface and is the one that does. Only the Artifact 1 test\n"
        b"  harness reads the cache today.\n",
    ),
    (
        "add L-190, the scanner reach rule",
        b"**Ref:** provenance_scanner.py console summary block (~line 2909);\n"
        b"L-188; L-184.\n"
        b"\n"
        b"## PENDING ACTION (Tony-side)\n",

        b"**Ref:** provenance_scanner.py console summary block (~line 2909);\n"
        b"L-188; L-184.\n"
        b"\n"
        b"#### [L-190] Scanner reach: anything rendered must be reachable\n"
        b"<!-- L:190 status:OPEN upd:2026-08-07 section:A flag: rice:4/4/80/3 -->\n"
        b"- **Tony's rule, 2026-08-07:** \"anything rendered from sourced data\n"
        b"  should be reached by the scanner.\" Stated as a general principle, not\n"
        b"  a one-off fix.\n"
        b"- **It is a stronger rule than the one the scanner was built on.** The\n"
        b"  scanner today reaches values in the shapes it knows -- annotated\n"
        b"  module constants, dict entries, `# Source:` comments. Tony's test is\n"
        b"  whether a value reaches a RENDER, whatever shape it is stored in.\n"
        b"- **The gap that surfaced it.** The gas giant radiation belt and plasma\n"
        b"  torus geometry (about 22 values across four bodies, see L-181) is\n"
        b"  bare literals inside function bodies. The scanner does not see them:\n"
        b"  zero occurrences of `belt_distances`, `torus_distance` or\n"
        b"  `belt_thickness` anywhere in the 879-finding audit at `1ba20c3`.\n"
        b"  Every one of these values renders.\n"
        b"- **Why it matters beyond tidiness.** Batch 2's worksheet is built from\n"
        b"  scanner findings. An assumption formed this session -- that Batch 2\n"
        b"  would source the belt ranges as part of the gas giant cross-check it\n"
        b"  was already doing -- would have handled NOTHING, silently, because\n"
        b"  those values never reach the worksheet. Invisible-to-the-tool is the\n"
        b"  same failure class as uncited: both pass every check.\n"
        b"- Adjacent finding from the same session, worth folding in: the 20-line\n"
        b"  divergence check written for L-179 finds a class the scanner also\n"
        b"  cannot see -- a citation naming a constant and stating a value that\n"
        b"  disagrees with the store. It flags CITED claims, where the scanner\n"
        b"  flags UNCITED ones. See L-189.\n"
        b"**Gap:** Extend the scanner to reach bare literals that feed a render.\n"
        b"Start with the belt and torus values, since they gate Batch 2's\n"
        b"worksheet completeness. Treat as a shared-CI change.\n"
        b"**Ref:** L-181 (the enumerated belt/torus surface); L-189 (run history\n"
        b"and the divergence check); L-156 (Batch 2 worksheet).\n"
        b"\n"
        b"## PENDING ACTION (Tony-side)\n",
    ),
]

EDITS[PLAN] = [
    (
        "correct the pilot entry counts",
        b"    it, then scaling to the remaining 32 -- which under fetch-and-import\n",
        b"    it, then scaling to the remaining 29 rings -- which under fetch-and-import\n",
    ),
    (
        "correct the 37 figure",
        b"    really means \"first end-to-end test after all 37 entries move\" --\n",

        b"    really means \"first end-to-end test after all 33 ring entries move\"\n"
        b"    --\n",
    ),
    (
        "note the corrected enumeration beside the ring-pair count",
        b"  33 ring pairs.\n",

        b"  33 ring pairs.\n"
        b"\n"
        b"**Count corrected 2026-08-07.** An earlier \"37 entries\" figure appeared\n"
        b"once in this document, unsourced, alongside \"33 ring pairs\" elsewhere.\n"
        b"Enumerated by AST walk at `9b4f278`: 33 ring entries -- Jupiter 4,\n"
        b"Saturn 7, Uranus 11, Neptune 11. Jupiter is 4, not 5. Separately, the\n"
        b"radiation belt and plasma torus geometry is roughly 22 more physical\n"
        b"values in four different shapes, held as bare literals in function\n"
        b"bodies and counted in neither figure. See L-181 and L-190.\n",
    ),
]


def main():
    here = pathlib.Path(__file__).parent
    staged, problems = {}, []

    for name, fp_expected in FINGERPRINTS.items():
        path = here / name
        if not path.exists():
            problems.append(f"MISSING: {name} (run from the palomas_orrery folder)")
            continue
        data = path.read_bytes()
        fp_actual = hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()
        if not fp_expected.startswith('__') and fp_actual != fp_expected:
            problems.append(
                f"BASE MOVED: {name}\n"
                f"    expected content MD5 {fp_expected}\n"
                f"    actual   content MD5 {fp_actual}\n"
                f"    (line endings normalized -- a real content difference.)"
            )
            continue
        is_crlf = data.count(b'\r\n') > 0
        if is_crlf:
            print(f"  ..  {name}: CRLF file -- anchors translated, endings preserved")
        for label, old, new in EDITS.get(name, []):
            o, n = (old, new)
            if is_crlf:
                o = o.replace(b'\n', b'\r\n')
                n = n.replace(b'\n', b'\r\n')
            count = data.count(o)
            if count != 1:
                problems.append(
                    f"ANCHOR {count} MATCHES (expected 1): {name} -- {label}\n"
                    f"    first 70 bytes: {o[:70]!r}"
                )
            else:
                data = data.replace(o, n, 1)
        staged[name] = data

    if problems:
        print("\n".join(problems))
        print("\nNOTHING WAS WRITTEN.")
        return 1

    for name, data in staged.items():
        (here / name).write_bytes(data)
        for label, _o, _n in EDITS.get(name, []):
            print(f"  ok  {name} -- {label}")

    print("\npatch applied")
    print("\nNext, in order:")
    print("  1. Run ledger_index.py (dashboard > Developer Tools).")
    print("  2. Commit and push in GitHub Desktop.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
