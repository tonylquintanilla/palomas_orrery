"""patch_L196_6_master_plan_section_5a.py -- rewrite Section 5a as the
critical path.

RUN COMMAND
-----------
Save into the palomas_orrery repo root, open in VS Code, click Run.

    python patch_L196_6_master_plan_section_5a.py

WHAT IT DOES
------------
Replaces Section 5a of documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md.
Nothing outside that section is touched -- verified before delivery by a
guard asserting every changed line falls inside its bounds.

WHY
---
The old 5a was an execution map with model assignments and a dependency
chain, and it had drifted three ways:

  - it called Artifact 2 BLOCKED, which Section 6 of the same document
    had already amended on 2026-08-08;
  - it reported scanner Tier-1 at 210 and provenance-discipline at v1.4,
    against a live 206 and 2.3;
  - its NEXT named fifteen April Gemini worksheets, work the entire
    L-192 apparatus superseded.

And the framing was wrong in a way the numbers were not. It read as
though the provenance refactor WERE the path. It is one segment of it.

THE CORRECTION, IN ONE LINE
---------------------------
The assembler creates no data; it imports. Ephemerides are re-fetched
from Horizons nightly and are provenance-by-construction. Feature
constants -- ring radii, belt distances, shell bounds -- originate in
the orrery and reach the gallery by copy, and NOTHING downstream can
check them. So the provenance refactor precedes the assembler work
because its target is the orrery, so that importing from it blind is
safe. (Tony's framing, 2026-08-16.)

The new section states the end goal, the one-way pipeline, five
segments in order, and an honest "you are here" table pinned to
orrery 227f5b2 and gallery 3d10739.

WHAT IS PERMANENT
-----------------
This script is disposable. The section is not. Section 6 keeps every
ruling as history and is untouched.

VERIFIED BEFORE DELIVERY
------------------------
  - edit confined to lines 796-922, asserted before the patch was cut
  - Section 6 present exactly once afterwards
  - 14 '## Section' headings before and after
  - the new text is clean ASCII; the file's pre-existing 'B-prime'
    characters are left alone (the ASCII convention governs delivered
    code, not markdown, and B-prime is established notation used
    throughout the plan)
  - this script's own edit table is written with ascii(), so the
    deliverable stays ASCII while still matching lines that are not

SAFETY
------
All-or-nothing, fingerprinted, bottom-up, line endings preserved.
Success: one 'ok' line, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md': {
        'fp': 'e0b51daab2b29aaf3c86e53572789818',
        'edits': [
            (906, 921,
             [
              'All nine cluster items (L-154-162) have their own ledger entries. L-162',
              'closed (CENTER_BODY_RADII naming). L-163 role side closed; domain side',
              'deferred into the cluster.',
              '',
              'Still open under L-156: Phase 2 Tracks 1-2, Phases 3-4.',
              '',
              'NEXT: Phase 2 Track 1 -- complete the competitive pattern for the 15',
              'files with April 2026 Gemini worksheets (Claude independently verifies',
              'same claims, Tony compares, convergent claims get annotated by Opus 5).',
              'Then Track 2 (new worksheets for uncovered files, starting with',
              'celestial_objects.py). Then L-157/L-161 (source genuinely uncited',
              'findings). Then L-155/L-160 (Phase 3: pinning engine and test',
              "retirement). Once the scanner work closes, resume L-154's own open design",
              'questions (geometry-building approach, legend behavior, artifact',
              'sequencing -- captured in HANDOFF_gallery_feature_layer_L154_resume.md),',
              'then build Artifact 2.',
             ],
             [
              'Model assignments, per-item dependency chains and RICE scores. Those',
              'belong in the ledger, which is the in-flight record; a plan that',
              'duplicates them goes stale between sessions and then contradicts them.',
              'The August 5, 7 and 8 rulings that produced the track order stay in',
              'Section 6 as history.',
             ]),
            (903, 904,
             [
              'Current scanner state at HEAD (373c6d8): Tier 1 210, Tier 2 605, Tier 3',
              '62, Tier 4 2 (879 findings / 117 files).',
             ],
             [
              '### What this section deliberately does not carry',
             ]),
            (896, 901,
             [
              'Also landed across Phase 1 + follow-ons: build_pinned_values()',
              'citation-bleed flaw fixed; No Shadow Constants [CRITICAL] convention',
              'added to provenance-discipline (now v1.4); shadow constants in',
              'comet_visualization_shells.py deleted and properly imported; D8.5 Option A',
              'retired (23 findings to Tier 1) and staleness credit removed (16 findings',
              'to Tier 1).',
             ],
             [
              '| | State |',
              '|---|---|',
              "| Phase 0, stack | DONE. Pyodide + Plotly proven, B' resolved, 2.1-3.3 s cold start on iPhone. |",
              '| Phase 1a, vocabulary | COMPLETE. |',
              "| Phase 1b, serving | DONE. 12 objects served. Saturn's 7 rings, Jupiter's 4 rings and radiation belts, Earth's atmosphere and Van Allen belts all present in `feature_configs.json` with full parameters. |",
              '| Artifact 1, Earth | LOCKED (`artifact_1_earth_alone.json`). Proved propagation, the harness and the acceptance loop -- on an ORBIT. Exercised no features, which is how the feature path stayed broken unnoticed. |',
              '| Segment 1, orrery | IN PROGRESS. Track 0 has no open rulings. The reconciliation is measured: 102 annotations scored, **3 clean**, 40 SEND BACK, 19 CONVERSATION, 40 noted. Dispatch repaired but not finished -- 9 blockers found by the August 16 Fable/GPT review, 1 closed. |',
              '| Segment 2, transport | DESIGNED, not built. |',
              '| Segment 3, assembler draw | NOT STARTED. Two lines plus a type, then the renderers. |',
              '| Segment 4, Artifact 2 | Gated on 1-3. |',
             ]),
            (887, 894,
             [
              'Phase 2 Piece 1 (2026-08-01, Opus 5): scanner mechanism for the',
              'V_CROSS_CHECKED (V2) rung. parse_cross_checks() parser, scoring',
              'branches requiring source evidence AND two distinct checker annotations,',
              'diagnostics subsection, test_cross_checked.py (16 tests). Five-model',
              'competitive design review (GPT x2, Opus 5 x2, Fable 5) -- the competitive',
              'pattern produced genuine discovery (worksheet inventory error caught by',
              'one reviewer only, a live false-positive regex hazard caught by another',
              'only). Mechanism live, zero population until annotations written.',
             ],
             [
              '### You are here -- 2026-08-16, orrery `227f5b2`, gallery `3d10739`',
             ]),
            (881, 885,
             [
              'Phase 1 built by Opus 5 across four sessions, orchestrated by Opus 4.6',
              '(predesign) and reviewed by Opus 5. D8.5 (Option A retirement) closed as',
              'a Phase 1 follow-on. Phase 1 measured arc (the instrument got honest):',
              '145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171',
              '(1d/1e/1f) -> 210 (D8.5).',
             ],
             [
              '**Segment 5 -- Ship the Phase 2 page**, then Phase 3 stars, Phase 4',
              'exoplanets and Sgr A*, Phase 5 Earth system. Phase 6 dissolves into',
              'continuous refinement (Section 5).',
             ]),
            (877, 879,
             [
              'Detour status as of 2026-08-01: design and ledger phases CLOSED;',
              '**scanner Phase 1 (1a-1f) COMPLETE; Phase 2 Piece 1 (D4 scanner',
              'mechanism) COMPLETE.**',
             ],
             [
              '**Segment 4 -- Lock Artifact 2.** Needs all three. A golden artifact is',
              'fingerprinted, so locking one on values that are not yet sourced means',
              'redoing the lock rather than editing a number (Tony, August 2026). And',
              'an artifact defined as *Jupiter and Saturn with rings and radiation',
              'belts* cannot be Mode 5 accepted while nothing renders them.',
             ]),
            (869, 875,
             [
              'Phase 1b DONE. Nightly cache builder live; M2 (F1a trust/served_window)',
              'tested and closed (2026-07-21) -- see documentation/TESTING_PROTOCOL.md',
              'addendum. Phase 2 Artifact 1 (Earth) built and Mode-5 accepted; Artifact 2',
              '(Jupiter/Saturn, rings + radiation belts) is next in the artifact order but',
              'BLOCKED: the client-side feature-rendering JS layer it needs (L-154) is',
              'gated behind a provenance/scoring detour that opened while scoping it (see',
              'Section 6 for the full dependency chain).',
             ],
             [
              '**Segment 3 -- Make the assembler draw.** Independent of segments 1 and',
              '2 in the sense that it could be done today and would render immediately',
              '-- the data is already served. `resolver.py:133` reduces a feature dict',
              'to its keys (`tuple(rec.get("features") or ())`) with `models.py:91`',
              'typing the field to match, so parameters are discarded one step before',
              'anything could use them. Then L-154: the client feature renderers.',
              'Nothing in the gallery repo currently reads `feature_configs.json`.',
             ]),
            (867, 867,
             [
              '### Next Step',
             ],
             [
              "**Segment 2 -- Make the transport faithful.** Track 0's cross-repo",
              'transport (vendored pull, design endorsed August 8). A correct orrery is',
              'not sufficient while `objects_config.json` is maintained by hand;',
              'the copy can drift from a source that is right.',
             ]),
            (848, 865,
             [
              '**Sonnet 5** -- predesign discovery for L-154 (the resolver bug, the',
              'physical-radius source question) that surfaced the provenance scoring',
              "problem; independent design review of Fable 5's provenance fix (verified",
              'every factual claim by rerunning the tool and regrepping both repos rather',
              'than trusting the summary -- caught the Tier-2 flood size, the',
              'CENTER_BODY_RADII visibility gap, and two design refinements). Requested',
              "and synthesized Fable 5's broad review-and-scoping pass on the whole",
              'cluster (2026-07-26), which independently caught the unfixed resolver bug',
              'still asserted as "fixed" in L-154\'s own resume handoff, and a false',
              '"Phase 4 done" gap in L-163. Formalized all nine items (L-154 through',
              'L-162) into the ledger as their own DETAIL blocks -- previously they',
              'existed only in handoff documents -- and closed out L-114/L-120 in the',
              'same pass, all independently re-verified against live HEAD',
              '(`ledger_index.py --check`: clean, 160 blocks). Orchestrated and',
              'synthesized the D3 vulnerability-ladder calibration across three',
              'independent AI reviews (Gemini 3.1 Pro, GPT 5.5, Fable 5); Tony closed',
              'the one remaining fork (2026-07-27). Also handling L-162 (CENTER_BODY_RADII',
              'cleanup) as a dedicated prep session.',
             ],
             [
              '**Segment 1 -- Make the orrery right.** Track 0 (L-181): one store for',
              'feature constants, provenance carried as data, display text derived.',
              'Track 1 (L-156): the provenance batches, Batch 2 gas giants being the',
              'one Artifact 2 needs. The worksheet checker, the request builder, the',
              'key rule and the dispatch loop (L-192) are the MACHINERY of Track 1, not',
              'a phase of their own -- they are how 102 annotations get reconciled at',
              'scale instead of by hand.',
             ]),
            (843, 846,
             [
              '**Opus 4.8 and Opus 5** -- verification, convergence, restraint. Phase 1b design review',
              '(July 7, 2026: caught osculating center gap, validation invariants, parent',
              'dependency). Attribution page (fetch license terms). Vocabulary DD/OQ review',
              'at Phase 2 start. Phase 5 restraint discipline on human-cost content.',
             ],
             [
              '### The path, in order',
             ]),
            (838, 841,
             [
              '**Fable 5** -- Phase 1a vocabulary delivered. Data serving analysis delivered.',
              'Phase 1b design review (July 7, 2026: caught invariant #4 self-contradiction,',
              '`stored_center` overload, grid nesting). Fable access extended to July 12,',
              '2026. Available for: provenance Tier-1 triage, Phase 2 broad-first design.',
             ],
             [
              'That asymmetry is why the provenance refactor precedes the assembler',
              'work rather than running beside it. Its target is the ORRERY, so that',
              'importing from it blind is safe.',
             ]),
            (836, 836,
             [
              '### Model Assignments',
             ],
             [
              "*Feature constants* originate in the orrery's Python and reach the",
              'gallery by copy. The builder does not know what a correct ring radius',
              'is. Neither does the resolver, the renderer, or the browser. Horizons is',
              'never consulted for them. **An error in the orrery becomes an error in',
              'the gallery, permanently and silently.**',
             ]),
            (830, 834,
             [
              '**Secondary dependencies:**',
              '- Helpers split -> Phase 2 (computation functions freed from tkinter)',
              '- Attribution page -> any publicly reachable interactive page',
              '- Star cache wire format -> Phase 3 (Pyodide needs non-pickle format)',
              '- ~~A/B architecture decision~~ -> resolved: B\u2032 (July 6, 2026)',
             ],
             [
              '*Ephemerides* are re-fetched from Horizons every night. Provenance by',
              'construction; a bad value cannot survive a rebuild. Nothing to audit.',
             ]),
            (827, 828,
             [
              '**Critical path:** Phase 1b -> Phase 2 -> domain pages.',
              '(Phase 0, Phase 1a complete. A/B fork resolved: B\u2032.)',
             ],
             [
              '**The two data kinds behave differently and only one is',
              'self-correcting.**',
             ]),
            (800, 824,
             [
              'PREP (independent, can start now)',
              '  [x] LICENSE moved to root',
              '  [x] Section W ledger entries',
              '  [ ] Attribution page --------- 4.8 --> needed before public pages',
              '  [ ] Helpers split ------------ 4.6 --> needed before Phase 2',
              '',
              'PHASE 0 DONE ------ PHASE 1a COMPLETE ------ PHASE 1b',
              'Stack proven         Vocabulary delivered       Data serving pipeline',
              'Arch A proven        (Fable, Jul 4)             Export script + coverage',
              'B\u2032 measured: PASS                               index + serving home',
              '(Jul 6)                                         + slim plotly wheel',
              '                          |',
              '                     PHASE 2 <-- Phase 1b + helpers split',
              '                     Solar system assembler (B\u2032)',
              '                     Shared engines in Pyodide',
              '                     + interactive page',
              '                          |',
              '                     PHASE 3',
              '                     Star assembler + star cache format',
              '                          |',
              '                     PHASE 4',
              '                     Hybrid domains',
              '                          |',
              '                     PHASE 5 <-- 4.8 restraint discipline',
              '                     Earth system',
             ],
             [
              '    ORRERY                the source of truth for feature constants',
              '      |                   (ring radii, belt distances, shell bounds)',
              '      |  transport        currently a HAND COPY into',
              '      v                   gallery/data/objects_config.json',
              '    CACHE BUILDER         nightly; fetches ephemerides FRESH from',
              '      |                   Horizons; passes feature constants THROUGH',
              '      v',
              '    SERVED CACHE          coverage_index.json, feature_configs.json,',
              '      |                   positions/  (in the gallery repo, same origin)',
              '      v',
              '    ASSEMBLER             resolver -> render_* -> Plotly figure JSON',
              '      |',
              '      v',
              '    INTERACTIVE GALLERY   Pyodide + Plotly.js, static GitHub Pages',
             ]),
            (797, 797,
             [
              '### Dependency Chain',
             ],
             [
              '**Rewritten 2026-08-16 at `227f5b2`.** The previous 5a was an execution',
              'map with model assignments and a dependency chain. It had drifted: it',
              'called Artifact 2 BLOCKED, which Section 6 had already amended on',
              'August 8; it reported scanner and skill-version figures two weeks stale;',
              'and its NEXT named work that L-192 superseded. More importantly it',
              'described the provenance refactor as though that were the path, when the',
              'refactor is one segment of it.',
              '',
              'This section is the spine. Detail lives in Sections 5, 6 and 7; history',
              'of every ruling stays in Section 6. When 5a and another section',
              'disagree, 5a is the one that was rewritten last -- reconcile, do not',
              'guess.',
              '',
              '### The end goal',
              '',
              '**The Python orrery, running in the browser under Pyodide, serving the',
              'interactive gallery.** Not a translation of the orrery into JavaScript',
              '-- the same computation engines, the same conventions, one codebase.',
              "Architecture B' (Section 5, Phase 0). The static gallery it replaces",
              'stays as the pedagogical exhibit layer.',
              '',
              '### One pipeline, one direction',
              '',
              'The single most important structural fact, and the one the earlier 5a',
              'obscured: **the assembler creates no data.** It imports. There is no',
              'point downstream of the orrery at which a wrong constant can be caught.',
             ]),
            (795, 795,
             [
              '## Section 5a -- Execution Map: Dependencies & Model Assignments',
             ],
             [
              '## Section 5a -- The Critical Path',
             ]),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    if not os.path.isfile('constants_new.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding constants_new.py).')
        return 1

    staged = []
    fixed = []
    total = 0

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written.')
            return 1

        crlf = b'\r\n' in raw
        lines = normalized(raw).decode('utf-8').split('\n')

        # The gate is on what THIS patch introduces. A file that already
        # holds non-ASCII is reported rather than blocked -- blocking on
        # somebody else's bug stops a correct patch, and staying silent
        # about it is how the convention quietly stops being true.
        for _, _, _, new_lines in spec['edits']:
            for line in new_lines:
                try:
                    line.encode('ascii')
                except UnicodeEncodeError:
                    print('ERROR: this patch would insert non-ASCII into '
                          '%s. Nothing written.' % name)
                    print('       %r' % line)
                    return 1
        before = sum(1 for b in bytearray(raw) if b > 127)
        if before:
            fixed.append((name, before))

        for start, end, old, new in spec['edits']:
            if end >= len(lines):
                print('ANCHOR FAIL: %s lines %d-%d run past end of file.'
                      % (name, start + 1, end + 1))
                return 1
            if lines[start:end + 1] != old:
                print('ANCHOR FAIL: %s lines %d-%d do not read as recorded.'
                      % (name, start + 1, end + 1))
                for offset, want in enumerate(old):
                    got = lines[start + offset]
                    if got != want:
                        print('       first difference at line %d'
                              % (start + offset + 1))
                        print('       expected %r' % want)
                        print('       found    %r' % got)
                        break
                print('       Nothing written.')
                return 1
            lines[start:end + 1] = new

        out = '\n'.join(lines).encode('utf-8')
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-36s %d edit(s)' % (name, count))

    for name, before in fixed:
        with open(name, 'rb') as handle:
            after = sum(1 for b in bytearray(handle.read()) if b > 127)
        print('note: %s holds %d pre-existing non-ASCII byte(s) '
              '(B-prime notation), deliberately left alone -- the ASCII '
              'convention governs delivered code, not markdown'
              % (name, after))
    print('patch applied (%d bytes, %d edits across %d files)'
          % (total, sum(c for _, _, c in staged), len(staged)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
