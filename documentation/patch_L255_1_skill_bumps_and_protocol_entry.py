r'''
patch_L255_1_skill_bumps_and_protocol_entry.py -- L-255.

Writes tonight's four rulings into the layer that fires on them, and
closes the four-link chain L-230 named: SKILL.md, then skills_index.py,
then the manifest zone, then a protocol version entry. Links one and
four are this patch. Links two and three are your `skills_index.py` run
afterwards, which regenerates the manifest zone -- NEVER hand-edited.

FOUR FILES, ALL OR NOTHING.

1. skills/provenance-discipline/SKILL.md   2.6 -> 2.7
2. skills/orrery-coding-conventions/SKILL.md   1.5 -> 1.6
3. PROJECT_INSTRUCTIONS.md   v3.43 -> v3.44, and v3.41 moves out
4. documentation/PROJECT_INSTRUCTIONS_HISTORY.md   receives v3.41

WHAT GOES INTO provenance-discipline 2.7. Three sections, all from
Tony's rulings of 2026-08-26, and all of them gaps this skill had.

  One Value, One Home [CRITICAL] -- the POSITIVE form. No Shadow
  Constants was a prohibition on copying a value that already exists in
  constants_new.py; it said nothing about where a NEW value's first home
  is, said nothing about prose, and carried no scope boundary. Earth's
  four hover strings typed their boundary figures for months beside a
  radius_fraction that disagreed with them, and nothing in this skill
  covered it.

  Report to the Figures You Have [QUALITY] -- had no home in any skill.
  Compute at full precision; report to the significant figures the least
  precise input supports. The two rules can be made to contradict each
  other by a careless reader, so they are stated together.

  A Breadcrumb Must Not Cite [CRITICAL], under Scanner Mechanics -- a
  `# Ref:`, a bare URL, `doi` or `arXiv` anywhere in the thirty-line
  lookback registers as a citation for the unit beside it. So an honest
  "unsourced, pending research" note cannot carry its own candidate
  papers. Non-obvious, and it would bite the next person who tries to
  leave one. (L-253.)

WHAT GOES INTO orrery-coding-conventions 1.6. Marker Separation for
Near-Equal Radii keeps its rule and loses its fixed number: the step is
an OUTCOME -- far enough to read as separate at the scale the family
renders at -- with 20 degrees for the solar skin stack and 10 for
Earth's crust as the two worked cases. Tony's ruling 2026-08-26, after
the arithmetic showed the required step depends on frame width and frame
width depends on which shells are enabled.

STALE SKILL = STOP, and why this patch cannot clear it. A reinstall
lands in your account and stays invisible to the session that made it.
So this patch does NOT clear the gate. It writes an obligation into the
handoff instead: the next session confirms its loaded copies read 2.7
and 1.6 before doing provenance or marker work.

RUN COMMAND (save this file into the repo root and run it from there --
it reaches into skills/ and documentation/ on its own):

    python patch_L255_1_skill_bumps_and_protocol_entry.py

Success prints one `ok` line per edit then `patch applied`. Any failure
prints a single ERROR:/ANCHOR FAIL line and writes nothing to any of the
four files. One-shot: a second run aborts on the fingerprints.

RUN ORDER: after patch_L254_1. Afterwards, in order:
  1. python skills_index.py PROJECT_INSTRUCTIONS.md   (regenerates the
     manifest zone -- links two and three of the chain)
  2. Settings > Skills: reinstall provenance-discipline and
     orrery-coding-conventions   (Tony-action (do))
  3. python maintenance_run.py
  4. Re-upload PROJECT_INSTRUCTIONS.md to the Claude UI (it is v3.44 now)

PERMANENT: the edits to all four files.
DISPOSABLE: this script. Archive it to documentation/ once it has run.
'''

import hashlib
import os
import sys

PROV = os.path.join('skills', 'provenance-discipline', 'SKILL.md')
CONV = os.path.join('skills', 'orrery-coding-conventions', 'SKILL.md')
PROTO = 'PROJECT_INSTRUCTIONS.md'
HIST = os.path.join('documentation', 'PROJECT_INSTRUCTIONS_HISTORY.md')

# md5 of the LF-normalised bases, orrery 3faa72a0533850dccd056742470c788aad9b04e0
BASE_FP = {
    PROV: 'ce228979a820f1176742394b558c6578',
    CONV: 'e1e122e7821759c6ed296d48b7db1aa6',
    PROTO: 'c8a2fdd6089d2d8cdce6b355cbe7222d',
    HIST: 'ed4020a4431291e07382f6d04402b860',
}


def bb(text):
    return text.encode('ascii')


# ------------------------------------------------------------------
# 1. provenance-discipline 2.6 -> 2.7
# ------------------------------------------------------------------

PROV_HEADER_OLD = bb(r'''Skill version: 2.6 | Cut from palomas_orrery @ f603be3 (v2.6), earlier
@ 731066f (v2.5), @ 6b99ace (v2.2), @ 00219d9 (v2.1), @ eb77c83 (v2.0),
@ cdcdb4b (v1.9) | August 19, 2026''')

PROV_HEADER_NEW = bb(r'''Skill version: 2.7 | Cut from palomas_orrery @ 3faa72a0 (v2.7),
earlier @ f603be3 (v2.6), @ 731066f (v2.5), @ 6b99ace (v2.2),
@ 00219d9 (v2.1), @ eb77c83 (v2.0), @ cdcdb4b (v1.9) | August 26, 2026
v2.7 adds three sections from Tony's rulings of 2026-08-26, each of
them a gap this skill had rather than a refinement of something it
said. One Value, One Home [CRITICAL] states positively what No Shadow
Constants only prohibited, and extends it to prose and to dead code.
Report to the Figures You Have [QUALITY] had no home in any skill.
A Breadcrumb Must Not Cite [CRITICAL] records why an honest
"pending sourcing" note cannot carry its own references (L-253).
Founding case for the first two: Earth's four interior hover strings
typed their boundary figures for months beside a radius_fraction that
disagreed with them by up to 297 km, and nothing here covered it.''')

PROV_ANCHOR = bb('## No Shadow Constants [CRITICAL]\n')

PROV_NEW = bb(r'''## One Value, One Home [CRITICAL]

**A numeric value has exactly one home -- `constants_new.py`, with its
source. Everything else references it: the drawing, the hover string,
the tooltip, the comment. A number typed anywhere else is a second
store, whether or not it currently agrees.**

This is the POSITIVE form of the section below, and the difference is
not stylistic. No Shadow Constants forbids copying a value that ALREADY
lives in `constants_new.py`. It says nothing about where a value's first
home is when a new feature introduces one, and a new feature is exactly
where the second store gets created.

**Prose counts.** A hover string that types `1,220 km` is a store. Build
the sentence so the number interpolates:

```python
f"The inner core is {EARTH_INNER_CORE_KM:,.1f} km in radius."
```

Two strings that both interpolate the same constant cannot disagree
numerically, which is why prose duplication and value duplication are
different problems -- the first is L-191, the second is this rule.

**Dead code counts.** A literal in a function nothing calls is still a
store, and it reads as authoritative to whoever finds it next. Wire it
or delete it; do not leave it because it cannot run. (L-254.)

**THE SCOPE BOUNDARY, and it must be stated in the same breath.**
MEASURED values migrate. DECLARED DRAWING PARAMETERS do not:
`n_points`, `marker_size`, `opacity`, `mesh_resolution`, an angular
marker step. Those stay where they are drawn. That is L-240's split, and
without it "only store" reads as hauling 25 and 3.4 into
`constants_new.py`, which buries the values that matter under the ones
that do not.

**IN TIME: forward-going on every file touched.** The standing backlog
carries the sweep -- L-181 is the parent, with L-243, L-244 and L-248 as
open slices. This rule does NOT open a repo-wide sweep on the day it is
adopted; that is the denominator that grows whenever someone thinks of
something. (The Braid, resident protocol Part 3.)

(Tony's ruling, 2026-08-26, stated as general and confirmed with the
boundary above in the same exchange.)

## Report to the Figures You Have [QUALITY]

**Compute at full precision. Report to the significant figures the least
precise input supports.** The two halves are separate and a careless
reader can make them contradict each other, so they are stated together.

Rounding a derived constant in code introduces error AND creates a
rounded second store of a value that lives elsewhere, so the derivation
stays symbolic:

```python
EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM
# Derived: 1221.5 / 6378.1366 = 0.19151 -- 5 significant figures, set
# Derived+: by the numerator. Report no more than that.
```

Significant figures govern REPORTING: every quotient stated in a
comment, a hover string or a tooltip, with the figure count named beside
it so the next reader does not re-derive it.

**A subtraction is governed by decimal PLACES, not significant figures.**
`6371.0 - 660` is good to units, so 5711 and not 5711.0.

The failure this catches is quiet. Stating `0.8953994` when the inputs
support `0.8954` is not a small error in the last digits -- it is six
digits the value was never entitled to, and it reads as a measurement.
(Tony's ruling, 2026-08-26, after exactly that appeared in a table.)

## No Shadow Constants [CRITICAL]
''')

PROV_SCANNER_ANCHOR = bb('## Report Domain Classification '
                         '(Findings by File / File Type)\n')

PROV_SCANNER_NEW = bb(r'''### A Breadcrumb Must Not Cite [CRITICAL]

Citations attach at BLOCK level over a thirty-line lookback, and
`SOURCE_PATTERNS` counts `# Source:`, `# Ref:`, a bare `https://` URL,
`doi`, `arXiv` and agency names (IAU, JPL, NASA, ESA, NIST, NOAA...) as
citations. All of that is in the section above. The consequence is not
obvious and it bites in one specific place.

**An honest "unsourced, pending research" note cannot carry its own
candidate references.** Put the papers next to the value and the scanner
reads them as that value's citation, and the unit ends up looking better
sourced than it is -- which is the wrong-but-cited failure, rebuilt
deliberately by someone trying to be careful.

So the code carries a HANDLE and nothing else:

```python
# Review-note: two figures for this boundary's variation, and the
# Review-note+: papers that may support them, are held in L-253 --
# Review-note+: unsourced, unused, deliberately not restated here.
```

The figures, the DOIs and where each actually came from live in the
ledger row, which is searchable by handle, holds "pending sourcing" as a
native state, is RICE-scorable against everything else, and sits outside
the audit entirely. The trail is preserved at zero cost to the
denominator.

(Tony's ruling, 2026-08-26. Founding case L-253: `EARTH_D660_DEPTH_KM`
carried a real, correctly transcribed reference to Ishii et al. 2019 --
true of the 660 km depth, and not the source of either figure in the
note beneath it. That paper is about the discontinuity's sharpness.)

## Report Domain Classification (Findings by File / File Type)
''')

# ------------------------------------------------------------------
# 2. orrery-coding-conventions 1.5 -> 1.6
# ------------------------------------------------------------------

CONV_HEADER_OLD = bb(r'''Skill version: 1.5 | Cut from palomas_orrery @ 15741822 (v1.5),
earlier @ 86f529a (v1.4), 3398970 (v1.3) | 2026-08-23''')

CONV_HEADER_NEW = bb(r'''Skill version: 1.6 | Cut from palomas_orrery @ 3faa72a0 (v1.6),
earlier @ 15741822 (v1.5), 86f529a (v1.4), 3398970 (v1.3) | 2026-08-26
v1.6 (L-249) makes the angular step in Marker Separation for
Near-Equal Radii an OUTCOME rather than a fixed 20 degrees, with 20 and
10 recorded as the two worked cases. Earned when Earth's upper mantle
moved to its sourced radius and its cross vanished under the crust's.''')

CONV_RULE_OLD = bb(r'''**Rule: the inner shell keeps the north pole. Each subsequent shell in
the stack steps 20 degrees in polar angle along the +x meridian, at its
own radius.** Separate angularly, never radially -- moving a marker off
its own shell's radius detaches it from the thing it labels.''')

CONV_RULE_NEW = bb(r'''**Rule: the inner shell keeps the north pole. Each subsequent shell in
the stack steps in polar angle along the +x meridian, at its own
radius.** Separate angularly, never radially -- moving a marker off its
own shell's radius detaches it from the thing it labels.

**HOW FAR is an outcome, not a number: far enough to read as two markers
at the scale the family actually renders at.** The step needed depends
on frame width, and frame width depends on which shells the user has
enabled -- Earth's interior alone frames at about 1 R, but switch the
magnetosphere on and the same step collapses to nothing. Two worked
cases:

- **20 degrees, the solar skin stack.** Renders across a 0-3 R_sun view,
  so the markers land 0.365 R_sun apart, about 12% of the frame.
- **10 degrees, Earth's crust against the upper mantle.** Interior-only
  view, so 10 degrees puts them 0.183 R apart -- roughly 1,165 km, 8-9%
  of the frame, up from 33 km.

Declare it per shell with `'info_polar_deg'` in `SHELL_CONFIGS`;
`build_sphere_shell()` reads it and places the marker at
`r*1.05` stepped by that polar angle. Absent or zero reproduces the pole
exactly, so adding the key to one shell moves nothing else. It is a
DECLARED drawing parameter under L-240 and stays in `shell_configs.py`,
never in `constants_new.py`.

(Tony's ruling 2026-08-26, and his Mode 5 call on which shell moves:
the CRUST, because it is the odd layer visually -- the only mesh3d
surface in the interior stack. The standing rule would have moved it
too, being the outer of the pair. Rule and eye agreed.)''')

# ------------------------------------------------------------------
# 3 and 4. Protocol version entry, and v3.41 moves down
# ------------------------------------------------------------------

PROTO_TITLE_OLD = bb('Tony Quintanilla, PE | Claude | v3.43 | August 25, 2026')
PROTO_TITLE_NEW = bb('Tony Quintanilla, PE | Claude | v3.44 | August 26, 2026')

PROTO_CUT_OLD = bb('Cut from 2bf0d06a at '
                   'https://github.com/tonylquintanilla/palomas_orrery')
PROTO_CUT_NEW = bb('Cut from 3faa72a0 at '
                   'https://github.com/tonylquintanilla/palomas_orrery')

V341 = r'''v3.41 (August 18, 2026): Records restructure and a skill bump.
No rule changed. (1) The version history left this document: v1.0-v3.38
now live in documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1, the
file that was LESSONS_ARCHIVE.md and still carries the v3.37 lessons
record verbatim as PART 2. The ledger's appendix is replaced by a
pointer. Three entries stay resident and a fourth pushes the oldest
down, which is the cap L-199 asked for; its part 1, a sizing section,
is still unbuilt. (2) The header gained an anchor and lost a
contradiction -- the repo copy read August 16 and the copy installed in
the Claude UI read August 17 under the SAME version, two stores with
nothing watching them the way Stale Skill = Stop watches the skills.
(3) provenance-discipline 2.3 -> 2.4 (L-203, L-204): the visibility
convention got a home, and the annotation grammar now accepts a .jsonl
or .json worksheet reference, because a returned verdict could be
checked and routed and then refused when written back into the code.
The reinstall cannot be verified from inside the session that makes it,
so the NEXT session confirms its loaded copy reads 2.4 before doing
provenance work.

'''

V344 = r'''v3.44 (August 26, 2026): No rule changed in this document. TWO skill
bumps and one long build, recorded here because the recording is the
fourth link of the chain L-230 named and the only one that does not
fire on its own.

(1) provenance-discipline 2.6 -> 2.7, three sections, all gaps rather
than refinements. One Value, One Home [CRITICAL] states positively what
No Shadow Constants only prohibited: a numeric value's home is
constants_new.py, and everything else -- drawing, hover string, tooltip,
comment, and code that cannot run -- references it. Its scope boundary
is stated in the same breath, because without it the rule reads as
hauling n_points and marker_size into the constants file: measured
values migrate, declared drawing parameters do not. Report to the
Figures You Have [QUALITY] had no home in any skill; compute at full
precision, report to the figures the least precise input supports, and
a subtraction is governed by decimal places. A Breadcrumb Must Not Cite
[CRITICAL] records that a Ref line or a bare URL inside the scanner's
thirty-line lookback becomes a citation for the unit beside it, so an
honest pending-sourcing note carries a ledger handle and nothing else.

(2) orrery-coding-conventions 1.5 -> 1.6 (L-249): the angular step in
Marker Separation for Near-Equal Radii becomes an outcome rather than a
fixed 20 degrees, with 20 for the solar skin stack and 10 for Earth's
crust as the two worked cases. The required step depends on frame width
and frame width depends on which shells are enabled, so one global
number was always going to be wrong somewhere.

The founding build was L-249, Earth's interior boundaries. Five patches
in one evening took four radius fractions that had been approximate
values taken by hand in 2024 and made them derivations of sourced radii
in constants_new.py, with the hover prose interpolating the same
constants. Three shells moved; the lower mantle moved 290 km. Two
defects of the class this protocol exists to catch were found in the
work itself rather than afterwards: a reference true of a constant and
false of the note beneath it, and a region check whose slice came out
empty so it passed having examined nothing. Handles L-249, L-253,
L-254, L-255. Version history: v3.41 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

'''

HIST_ANCHOR = bb(r'''v3.40 (August 16, 2026): No change to the protocol's own rules. Two''')

HIST_NEW = bb(V341 + '''(Moved down from the resident protocol on 2026-08-26 when v3.44 made a
fourth entry.)

v3.40 (August 16, 2026): No change to the protocol's own rules. Two''')


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def load(name):
    if not os.path.exists(name):
        print('ERROR: %s not found. Run this script from the repo ROOT -- it '
              'reaches into skills/ and documentation/ itself.' % name)
        return (None, None)
    with open(name, 'rb') as handle:
        data = handle.read()
    fp = fingerprint(data)
    if fp != BASE_FP[name]:
        print('ERROR: BASE MOVED. %s fingerprints %s, expected %s.'
              % (name, fp, BASE_FP[name]))
        print('       Nothing written to any of the four files. If this patch '
              'already ran, that is the expected result of a second run.')
        return (None, None)
    is_crlf = data.count(b'\r\n') > 0
    print('ok   base fingerprint %s (%s, %s)'
          % (fp, name, 'CRLF' if is_crlf else 'LF'))
    return (data, is_crlf)


def apply_edits(data, is_crlf, edits):
    for label, old, new in edits:
        if is_crlf:
            old = old.replace(b'\n', b'\r\n')
            new = new.replace(b'\n', b'\r\n')
        count = data.count(old)
        if count != 1:
            print('ANCHOR FAIL: %s -- expected 1 match, got %d: %r'
                  % (label, count, old[:70]))
            print('             Nothing written to any of the four files.')
            return None
        data = data.replace(old, new, 1)
        print('ok   %s' % label)
    return data


def main():
    staged = {}
    for name in (PROV, CONV, PROTO, HIST):
        data, crlf = load(name)
        if data is None:
            return 1
        staged[name] = [data, crlf]

    plans = {
        PROV: [
            ('provenance version header', PROV_HEADER_OLD, PROV_HEADER_NEW),
            ('One Value One Home + significant figures',
             PROV_ANCHOR, PROV_NEW),
            ('A Breadcrumb Must Not Cite',
             PROV_SCANNER_ANCHOR, PROV_SCANNER_NEW),
        ],
        CONV: [
            ('conventions version header', CONV_HEADER_OLD, CONV_HEADER_NEW),
            ('marker separation becomes an outcome',
             CONV_RULE_OLD, CONV_RULE_NEW),
        ],
        PROTO: [
            ('protocol title line', PROTO_TITLE_OLD, PROTO_TITLE_NEW),
            ('protocol cut anchor', PROTO_CUT_OLD, PROTO_CUT_NEW),
            ('v3.41 removed from the resident three', bb(V341), b''),
            ('v3.44 entry added',
             bb('v3.43 (August 25, 2026): One rule added'),
             bb(V344 + 'v3.43 (August 25, 2026): One rule added')),
        ],
        HIST: [
            ('v3.41 received into PART 1', HIST_ANCHOR, HIST_NEW),
        ],
    }

    for name, edits in plans.items():
        data, crlf = staged[name]
        data = apply_edits(data, crlf, edits)
        if data is None:
            return 1
        staged[name][0] = data

    for raw in (PROV_NEW, PROV_SCANNER_NEW, CONV_RULE_NEW, bb(V344)):
        try:
            raw.decode('ascii')
        except UnicodeDecodeError as exc:
            print('ERROR: non-ASCII byte in inserted text: %s' % exc)
            return 1
    print('ok   encoding gate -- inserted lines are ASCII')

    text = {n: staged[n][0].decode('ascii').replace('\r\n', '\n')
            for n in staged}

    # Versions must have MOVED, not merely be present.
    for name, want, dont in ((PROV, 'Skill version: 2.7', 'Skill version: 2.6'),
                             (CONV, 'Skill version: 1.6', 'Skill version: 1.5')):
        head = text[name][:2500]
        if want not in head:
            print('ERROR: post-condition -- %s does not declare %s.'
                  % (name, want))
            return 1
        if dont in head:
            print('ERROR: post-condition -- %s still declares %s.'
                  % (name, dont))
            return 1
    print('ok   post-condition -- both skills declare their new versions')

    # Exactly three version entries stay resident, and v3.41 is not one.
    resident = [v for v in ('v3.44', 'v3.43', 'v3.42', 'v3.41', 'v3.40')
                if ('\n%s (' % v) in text[PROTO]]
    if resident != ['v3.44', 'v3.43', 'v3.42']:
        print('ERROR: post-condition -- resident entries are %s, expected '
              "['v3.44', 'v3.43', 'v3.42']." % resident)
        return 1
    print('ok   post-condition -- three resident entries, v3.41 evicted')

    # And it must have LANDED. An eviction with no receipt loses an entry.
    if text[HIST].count('\nv3.41 (August 18, 2026)') != 1:
        print('ERROR: post-condition -- v3.41 appears %d times in the history '
              'file; the entry would be lost or doubled.'
              % text[HIST].count('\nv3.41 (August 18, 2026)'))
        return 1
    if text[HIST].index('v3.41 (August 18, 2026)') > text[HIST].index(
            'v3.40 (August 16, 2026)'):
        print('ERROR: post-condition -- v3.41 landed below v3.40; PART 1 runs '
              'newest first.')
        return 1
    print('ok   post-condition -- v3.41 landed once, above v3.40')

    if 'v3.44' not in text[PROTO][:200]:
        print('ERROR: post-condition -- the title line still reads an older '
              'version than the newest entry.')
        return 1
    print('ok   post-condition -- title line matches the newest entry')

    for name in staged:
        with open(name, 'wb') as handle:
            handle.write(staged[name][0])
    print('patch applied (%s)'
          % ', '.join('%s %d bytes' % (n, len(staged[n][0])) for n in staged))
    print('')
    print('Next, in order:')
    print('  1. python skills_index.py PROJECT_INSTRUCTIONS.md')
    print('  2. Settings > Skills: reinstall provenance-discipline and')
    print('     orrery-coding-conventions')
    print('  3. python maintenance_run.py')
    print('  4. Re-upload PROJECT_INSTRUCTIONS.md to the Claude UI (v3.44)')
    print('')
    print('The reinstall cannot be verified from inside this session. The')
    print('handoff carries it: the NEXT session confirms its loaded copies')
    print('read 2.7 and 1.6 before doing provenance or marker work.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
