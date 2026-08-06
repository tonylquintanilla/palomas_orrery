
# -*- coding: utf-8 -*-
"""patch_ledger_L184_L185.py -- session closeout for the August 6, 2026
architecture session.

Built on 24452442aaa64393066cac9d9b5885a763c0a76a
at https://github.com/tonylquintanilla/palomas_orrery (branch main).

HOW TO RUN
    Save this file in the REPO ROOT (the folder holding
    LEDGER_CONSOLIDATED.md), open it in VS Code, and click Run.

    Success: four "ok" lines, then "patch applied".
    Failure: one "ANCHOR FAIL" or "ERROR" line followed by
    "NOTHING WAS WRITTEN". The ledger is unchanged either way.

AFTER RUNNING
    Run ledger_index.py to regenerate the index. This patch adds two
    L-handles, so the index WILL be stale until you do.

WHAT CHANGES

  L-1  New [L-184] -- interactive build-path push gate. Records Task 2a as
       DONE and 2b as reshaped by the August 6 architecture findings.

  L-2  New [L-185] -- source discipline for the assembler's own constants.
       Tony's ruling, August 6, 2026.

  L-3  [L-181] reframed. Tony's ruling: this is not a new constant layer,
       it is completion of the existing one. Scope widened to cover
       feature geometry and the cross-repo export. RICE effort raised.

  L-4  [L-183] note updated -- the smoke_* map cleanup it flagged has
       landed in the Task 2a patch.

NOTE ON UNPUSHED WORK
    At the time this patch was written, orrery HEAD was 24452442 and the
    Task 2a scanner patch had been applied locally but NOT pushed. That is
    fine and expected; it just means the ledger entry below describes work
    that is on your disk and not yet in the repo. Push when convenient.

Patch written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

TARGET = 'LEDGER_CONSOLIDATED.md'
BASE_MD5 = 'f48a604192c9bf0150388fb74972d6c9'

NEW_ITEMS = b"""#### [L-184] Interactive build-path push gate
<!-- L:184 status:OPEN upd:2026-08-06 section:A flag: rice:4/4/75/3 -->
- Tony ratified 2026-08-05: the global "Tier-1 = 0" push gate becomes
  "Tier-1 = 0 on the interactive build path" for this phase. The global
  gate was unreachable in practice -- of 206 Tier-1 findings measured at
  `4b82384`, 105 sit in the Earth System domain, a subsystem Artifact 2
  never touches. A gate nobody can reach stops functioning as a gate.
- Tony's correction to the original proposal, and the load-bearing part:
  the gate is BUILT BEFORE the batches it scopes. Deferring the definition
  of a gate to a later item is the same category error as deferring the
  gate. This item therefore records work being done, not work deferred.
- **Task 2a DONE (2026-08-06, local; push pending).** Console output now
  prints the per-domain split under each tier line. MODULE_DOMAIN_MAP
  gained explicit entries for `orrery_rendering` and `shell_configs` --
  both carried findings with no entry and defaulted to `orrery`, and
  `shell_configs.py` is the single most important file on the build path,
  so an accidental default was the one case worth ruling out by hand. Two
  stale entries removed (see L-183). Verified by live run: domain
  coverage-gap note gone, totals unchanged at 877 / 118 files /
  206-581-88-2.
- **Task 2b RESHAPED, not yet built.** The original plan was to compute
  build-path membership by walking the import graph from named orrery-side
  entry points. Tracing at `24452442` found the premise wrong in three
  ways: (1) the named entry points (`tools/gallery_cache_builder.py`,
  `gallery_studio.py`, `json_converter.py`) live in the GALLERY repo, not
  the orrery, and the scanner only scans the orrery; (2) the cache builder
  imports nothing from the orrery at all -- its docstring states "No orrery
  imports" as a design decision, so an import walk from it finds zero
  orrery modules; (3) `gallery_studio.py` does import three orrery modules
  (`info_dictionary`, `visualization_utils`, `celestial_objects`) but as
  FUNCTION-LOCAL imports inside function bodies, which a header-only walk
  misses entirely.
- Artifact-2 path measured by named file at `4b82384`: shell_configs 23,
  idealized_orbits 26, planet_visualization_utilities 4, saturn shells 1,
  uranus shells 1, orrery_rendering 1, jupiter shells 0, neptune shells 0
  -- 56 total. Two consequences: the gas giant shells are ALREADY nearly
  clean (2 Tier-1 across all four), so Batch 2's job on those files is
  value verification rather than Tier-1 clearance; and Artifact 2 is not
  blocked by scanner debt in the shells themselves.
- Tony-action (decide): entry points for the computed path, once the
  L-181 architecture settles. The two questions are now coupled.
**Gap:** 2b blocked on the L-181 architecture review (Fable, sent
2026-08-06). The build path cannot be defined until the cross-repo data
flow is decided.
**Ref:** HANDOFF_next_session_masterplan_v16.md Task 2;
MASTER_PLAN_INTERACTIVE_GALLERY.md v16, *New in v16* block.

#### [L-185] Source discipline for the assembler's own constants
<!-- L:185 status:OPEN upd:2026-08-06 section:A flag: rice:3/3/90/1 -->
- Tony's ruling, 2026-08-06: the same source discipline applies to the
  assembler's constants even though there are only a few.
- The assembler reads DATA (positions, elements, feature configs) from the
  served cache and authors none of it -- that model is correct. But it also
  performs arithmetic (client-side Kepler propagation, km-to-AU
  conversion), and arithmetic needs constants that arrive in no cache file.
- Uncited at gallery `e7e8c5e`: `AU_KM = 149597870.7` in
  `gallery/assembler/render_orbits.py:41`,
  `gallery/assembler/render_objects.py:20`, and
  `gallery/assembler/tests/test_artifact1_earth.py:43`;
  `K_GAUSS = 0.01720209895` in `render_orbits.py:42`;
  `_JD_UNIX_EPOCH = 2440587.5` in `tools/inspect_staging.py:63`.
  Total `# Source:` citations in the whole gallery repo: 4.
- The correct pattern already exists at `tools/gallery_cache_builder.py:89`
  -- a cross-repo citation naming file, line, and source SHA:
  `# Source: constants_new.py:47 (orrery 4e2629c) -- IAU km per AU.`
  Apply that shape to the five uncited lines.
- Reasoning error worth recording, because it generalizes: an earlier draft
  dismissed these as low-value because the values are exact by definition
  and will never drift. That substitutes "will this drift?" for "is this a
  claim?" Stability makes a value EASY to source, not exempt from sourcing.
  A reader meeting an uncited number cannot tell a deliberate skip from an
  unchecked one. Call it skip-because-stable; it is cite-to-clear pointed
  the other way.
- Not evidence on the push/pull fork. These values do not drift, and an
  earlier draft leaned on them there incorrectly.
- `No Shadow Constants` [CRITICAL] normally prescribes deleting the local
  copy and importing the real one. That remedy is UNAVAILABLE across the
  repo boundary while self-containment is preserved, which is the one place
  these constants touch L-181's architecture question.
**Gap:** Five lines. Can ship independently of L-181; should not wait on a
structural build.
**Ref:** PREDESIGN_HANDOFF_feature_constant_unification.md, Open Question 4.

"""

EDITS = [
    ('L-1/2', 'insert L-184 and L-185',
     b"\n## PENDING ACTION (Tony-side)\n",
     b"\n" + NEW_ITEMS + b"## PENDING ACTION (Tony-side)\n"),

    ('L-3a', 'L-181 header + RICE reframe',
     b"#### [L-181] Single-source-of-truth constant layer for shell visualization\n"
     b"<!-- L:181 status:OPEN upd:2026-08-04 section:A flag: rice:5/4/80/3 -->",
     b"#### [L-181] Complete the single-source-of-truth constant layer\n"
     b"<!-- L:181 status:OPEN upd:2026-08-06 section:A flag: rice:5/5/70/5 -->"),

    ('L-3b', 'L-181 scope: feature unification + cross-repo export',
     b"**Gap:** Design the constant layer. Decide on dead tooltip fields.\n"
     b"Sequence migration per body.",
     b"- **REFRAMED 2026-08-06 (Tony's ruling).** This is not a NEW constant\n"
     b"  layer; it is completion of the existing one. `constants_new.py`\n"
     b"  already holds feature geometry (CHROMOSPHERE_RADII, INNER_CORONA_RADII,\n"
     b"  OUTER_CORONA_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,\n"
     b"  TERMINATION_SHOCK_AU, HELIOPAUSE_RADII) and already handles nested\n"
     b"  dicts with per-entry citations (CENTER_BODY_RADII,\n"
     b"  KNOWN_ORBITAL_PERIODS). Solar shell geometry went into the store;\n"
     b"  planetary ring geometry stayed inline in the rendering modules. There\n"
     b"  is no principle behind which went where -- the split is historical.\n"
     b"- **Scope widened to three layers.** (1) 37 feature entries move out of\n"
     b"  `jupiter_`/`saturn_`/`uranus_`/`neptune_visualization_shells.py` into\n"
     b"  `constants_new.py`. (2) Provenance migrates from `# Source:` comments\n"
     b"  to `source` DATA fields, one pass, bounded to the store (36 citations\n"
     b"  in constants_new.py plus what migrates in) -- required because a\n"
     b"  comment cannot be read at runtime and Tony wants hover text to quote\n"
     b"  its source for Mode 5 audit. The scanner's own docstring already lists\n"
     b"  this as deferred fix item 6: extend SOURCE_PATTERNS to recognize\n"
     b"  `'source': '...'`. (3) The exporter reads the store rather than four\n"
     b"  shell modules -- which is also what makes it POSSIBLE, since reading\n"
     b"  shell configs pulls Plotly and the constants store does not.\n"
     b"- **Derivation, not annotation.** Every displayed number -- hover text,\n"
     b"  descriptions, L-176's illustrated dimensions -- is interpolated from\n"
     b"  the stored value at render time. Unification removes the duplicate\n"
     b"  STORE; derivation removes the duplicate STATEMENT. Both are needed:\n"
     b"  L-179 and L-180 are drift INSIDE constants_new.py today, which proves\n"
     b"  one store does not by itself prevent drift.\n"
     b"- **Cross-repo scope (new).** The gallery's `data/objects_config.json`\n"
     b"  carries feature values, has ONE commit in its history, has no writer\n"
     b"  anywhere in either repo, and has no per-value source fields. The\n"
     b"  nightly builder refreshes positions from Horizons and copies features\n"
     b"  verbatim (`features_out[slug] = feats`), so a green nightly build\n"
     b"  never refreshes feature geometry and gives no signal that it did not.\n"
     b"  Batch 2 is scheduled to move Saturn's values; nothing would carry the\n"
     b"  correction across. Confirmed live: the 2026-08-06 nightly touched\n"
     b"  vectors, elements and positions and did NOT touch objects_config.json\n"
     b"  or feature_configs.json.\n"
     b"- Tony-action (decide): push vs pull across the repo boundary -- handed\n"
     b"  to Fable for review 2026-08-06. Every push variant that genuinely\n"
     b"  detects staleness ends up making the same network call pull makes,\n"
     b"  while still carrying a second copy on disk. A content hash recorded\n"
     b"  beside its own artifact detects corruption, NOT staleness.\n"
     b"- Tony-action (decide, settled): description interpolation ships in this\n"
     b"  build, not as a follow-on. Tony's reasoning doubles as an acceptance\n"
     b"  test -- \"this should be minor if the architecture is right.\" A large\n"
     b"  Mode 5 surface is evidence the architecture is wrong, not evidence the\n"
     b"  scope was too big.\n"
     b"**Gap:** Blocked on Fable architecture review (sent 2026-08-06). Then\n"
     b"design the store format, decide on dead tooltip fields, sequence\n"
     b"migration per body. L-184's build path cannot be defined until this\n"
     b"settles.\n"
     b"**Note:** Architecture comes before Batch 2 -- Tony's deliberate\n"
     b"reversal of \"clear all batches first,\" 2026-08-06."),

    ('L-4', 'L-183 note: smoke_* cleanup landed',
     b"no longer in the root (`smoke_dipole_cone`, `smoke_rotation_axis`) \xe2\x80\x94 a\n"
     b"small scanner-side cleanup that pairs naturally with this work.",
     b"no longer in the root (`smoke_dipole_cone`, `smoke_rotation_axis`) \xe2\x80\x94 a\n"
     b"small scanner-side cleanup that pairs naturally with this work.\n"
     b"DONE 2026-08-06: both stale entries removed and `orrery_rendering` /\n"
     b"`shell_configs` mapped explicitly, in the Task 2a patch (L-184). The\n"
     b"remaining unmapped-root-modules question still rides with this item."),
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
        print("ok  %-6s %s" % (eid, label))

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
    print("NEXT: run ledger_index.py. Two new L-handles were added, so the")
    print("index is stale until you do.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
