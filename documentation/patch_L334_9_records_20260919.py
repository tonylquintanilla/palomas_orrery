#!/usr/bin/env python3
"""
patch_L334_9_records_20260919.py -- ORRERY repo.

Run: save this file in the ORRERY repo ROOT (next to
LEDGER_CONSOLIDATED.md), open it in VS Code and click Run.
Or:  python patch_L334_9_records_20260919.py

A patch is run from its repository's ROOT and filed in documentation/ AFTER
it has run. Filed first and run second, it stops with one line, writes
nothing, and the push goes out without it.

Built on orrery e1a79f675689618850c9a8aaeffc5735fed90090
at https://github.com/tonylquintanilla/palomas_orrery
(gallery d9d7a48f90725f605b95dd39df5fccafe12c3dd3)

L-334 STAGE C, THIRD OF THREE PUSHES -- piece 6, the records. No code
changes. This is what makes the session's lessons travel; without it
they live only in a conversation that ends.

WHAT IT DOES (four files, all-or-nothing):

  skills/interactive-exhibit/SKILL.md       1.3 -> 1.4. Five new rules:
        what a room opens on is SERVED, not coded; a shell trace carries
        its key and an unstamped one is DRAWN; only two tools write the
        served config, and what each may touch; one check must read the
        file the browser fetches; and Tony's ruling of 2026-09-18 that
        logic needing no browser lives in its own file.
  skills/gallery-cache-builder/SKILL.md     1.4 -> 1.5. A CRITICAL rule:
        a config change is not deployed until the cache is rebuilt, and
        the two are committed together. The "one data point" sentence in
        the recovery section is now FALSE -- three occurrences -- and is
        corrected, with Tony's hand routine written down.
  PROJECT_INSTRUCTIONS.md                   v3.61 -> v3.62, carrying both
        bumps in ONE entry, as this document's own rule asks. The header
        stamp and the SHA anchor move with it. v3.59 moves down to
        documentation/PROJECT_INSTRUCTIONS_HISTORY.md to keep three
        resident -- THAT MOVE IS TONY'S, see below.
  LEDGER_CONSOLIDATED.md                    L-334 records stage C and
        closes; L-338 closes; L-216 gains the skill it was waiting for;
        and L-340 OPENS to hold what L-334 hands over -- three cosmetic
        things in the editor window and the Mode 5 pass that will find
        the rest. A closing item re-homes its loose ends, and a pointer
        to a handle that does not exist is not a home.

ONE THING THIS PATCH DOES NOT DO. The protocol's own rule is that when a
fourth version-history entry is added, the oldest of the four moves down
into documentation/PROJECT_INSTRUCTIONS_HISTORY.md, so an entry lives in
exactly one place. This patch REMOVES v3.59 from PROJECT_INSTRUCTIONS.md
and prints its text for you to paste into PART 1 of that file. It does
not write the history file itself, because appending to a 3,000-line
record in the right place is a judgement about that file's shape, not a
mechanical insert.

THE SKILL OBLIGATION THIS SESSION CANNOT DISCHARGE. A reinstall lands in
the account and stays invisible to the session that makes it. This
session LOADED interactive-exhibit 1.3 and gallery-cache-builder 1.4,
and both matched the repo. After you push, reinstall both from
Settings > Skills. The NEXT session confirms its loaded copies read 1.4
and 1.5 before exhibit or cache work; that obligation is written into
the ledger and the protocol entry, which is where it belongs, because it
is the only check that can actually fire.

THEN (Tony), in this order:
  1. python ledger_index.py LEDGER_CONSOLIDATED.md -- TWICE. Expect
     "OK: 335 L-blocks parsed" on the SECOND run -- 335, not 334,
     because L-340 is added -- and 193 live items: 194, minus L-334
     and L-338 closing, plus L-340 opening. The FIRST run prints
     CONSISTENCY PROBLEMS and moves the two closed blocks into
     section C, which is its job. It exits 0.
  2. python orrery_maintenance_run.py. The Skill manifest generator will
     REWRITE the table in PROJECT_INSTRUCTIONS.md rather than report it
     unchanged -- that is it picking up 1.4 and 1.5.
  3. Paste the printed v3.59 entry into
     documentation/PROJECT_INSTRUCTIONS_HISTORY.md, PART 1.
  4. Move this script into documentation/, commit and push.
  5. Reinstall interactive-exhibit and gallery-cache-builder from
     Settings > Skills.

FAILURE: a single ERROR: or ANCHOR FAIL line, and NOTHING is written.
Undo is Discard Changes in GitHub Desktop.

Written September 2026 with Anthropic's Claude Opus 5.
"""
import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ZONE = ('<!-- INDEX:START', '<!-- INDEX:END -->')

FINGERPRINTS = {
    'skills/interactive-exhibit/SKILL.md': '5bbba7438edcd408f31d54d440af331f',
    'skills/gallery-cache-builder/SKILL.md': '787db66bf18d1de1e974b229e5392bcd',
    'PROJECT_INSTRUCTIONS.md': 'a409f9f6a277d58bfef7e2951c729480',
    'LEDGER_CONSOLIDATED.md': 'b893a7f7fd37f3a53e88b026f77b18b4',
}

# ======================================================================
# interactive-exhibit 1.3 -> 1.4
# ======================================================================

IE_VERSION_OLD = """Skill version: 1.3 | Cut from gallery @ b375cfe1 (interactive.html,
gallery/nav_cluster.js, gallery/feature_renderers.js,
documentation/smoke_hover_budget.js) and orrery @ d99d8db1
(LEDGER_CONSOLIDATED.md L-316, L-318, L-331, L-332) | 2026-09-16, with
Anthropic's Claude Opus 5
"""

IE_VERSION_NEW = """Skill version: 1.4 | Cut from gallery @ d9d7a48f (interactive.html,
gallery/arrival.js, gallery/feature_renderers.js, gallery/nav_cluster.js,
tools/store_writer.py, tools/exhibit_store_editor.py,
gallery_maintenance_run.py, documentation/smoke_arrival.js) and orrery @
e1a79f67 (LEDGER_CONSOLIDATED.md L-334, L-336, L-338, L-339) |
2026-09-19, with Anthropic's Claude Opus 5
v1.4 (L-334) carries what a room OPENS on and who may write the file it
is read from. Five rules: the arrival block is served, not coded; every
trace belonging to a served shell carries that shell's key, and one that
loses it is DRAWN rather than hidden; only two tools write
data/objects_config.json, and each has an allow list rather than a
refusal list; one check must read the file the browser actually fetches;
and logic that needs no browser lives in its own file, which is Tony's
ruling of 2026-09-18. Built through three pushes on 2026-09-18/19,
Mode 5 on Tony's phone between each.
"""

IE_RULES = """### What a room opens on is SERVED, not coded [QUALITY]
Each room's object in `data/objects_config.json` carries an `arrival`
block: `drawn`, a list of shell KEYS, and `moon`, true or false.
`GalleryArrival.applyArrival` in `gallery/arrival.js` applies it before
the opening view is measured, so the view fits what is drawn. With no
block the page behaves as it did before arrival blocks existed --
nothing is hidden.

Tony's ruling, 2026-09-17, and it supersedes two earlier rulings of his
own (the Sun's 0.25 AU arrival of 2026-08-29 and L-291's eight-shell
Earth arrival): a room opens on "the surface shell plus frame elements
like sun direction, axes, terminator", and the Moon starts "with its box
not selected". There is NO floor under the opening view.

THE ARRIVAL BLOCK IS THE ONE PART OF A ROOM'S DATA THE PAGE READS
DIRECTLY. Everything else a room draws comes from the served cache under
`data/solar-system/`, which the cache builder writes. So a change to
`drawn` or `moon` reaches a visitor on the PUSH ALONE, while a change to
a shell's words does not reach them until the cache has been rebuilt.
Say which when telling anyone what a change will do.

### A shell trace carries its key [CRITICAL]
`gallery/feature_renderers.js` stamps `meta.shell_key` on every trace
belonging to a served shell -- the key it sits under in the object's
features, not its display name. `stampShell()` does it at nine sites,
and `stampLink()` carries an existing key across so the two stamps
cannot overwrite each other in either order.

The arrival rule tells three kinds of trace apart by that stamp: a
SERVED SHELL carries a key and is drawn only if `drawn` names it; the
MOON is legend group `moon`; a FRAME ELEMENT carries no key and is
always drawn.

THAT IS WHY THIS IS CRITICAL. A shell trace that loses its stamp reads
as a frame element and is DRAWN -- the failure is a room opening on more
than it should, which no compiler and no page error will mention.
`documentation/smoke_arrival.js` therefore checks that EVERY trace the
feature renderers build carries a key, and names by legend group any
that does not. Add a renderer, or a branch inside one, and stamp it.

Before 2026-09-18 a shell was found by the END of its legend group name,
which was a second reading of the label formula the renderers build. Two
readings of one formula is how they come to disagree. There is one way
of matching now; do not add a second.

### Only two tools write the served config [QUALITY]
`data/objects_config.json` is hand-formatted and a person reads its
diffs, so nothing rewrites it wholesale. Two tools edit it IN PLACE,
sharing one scanner (`tools/mirror_constants.py`'s `parse_with_spans`)
so they cannot come to disagree about the file's layout:

- `tools/mirror_constants.py` writes the NUMBERS, pulled from the
  orrery's export. A number changes in `constants_new.py`, never here.
- `tools/store_writer.py` writes the WORDS and the arrival settings, and
  `tools/exhibit_store_editor.py` is the window over it.

WHAT THE WRITER MAY TOUCH IS AN ALLOW LIST BUILT BY READING THE CONFIG,
not a list of exceptions -- 204 paths at gallery `d9d7a48f`: a served
shell's six words, a belt's parallel words, and `drawn` and `moon`. The
first design was a refusal list of six field names, and Claude Fable 5.1
found on 2026-09-18 that it would happily change a room's `slug` to
"earthx" or a shell's `color` to "zzz". A refusal list has to anticipate
every way of being wrong; an allow list only has to know what is right.
Keep it that way.

A SERVED SHELL IS A MEMBER CARRYING A DISPLAY `name`. That is the rule
`tools/check_cache_in_step.py` counts by and the set the renderers
stamp, so the editor's list, that check's count and what a visitor can
tick all mean one thing. A plain walk of the config gives 22 for Earth
where the renderers draw 16; the name rule gives 18 for the Sun and 14
for Earth.

EARTH'S TWO RADIATION BELTS ARE THE EXCEPTION AND ALWAYS WILL BE while
they are served as they are. Their names, descriptions, abouts and links
are PARALLEL LISTS under one group key rather than a member each, so
they have no per-belt key: both carry the feature key
`van_allen_belts`, they tick together as one arrival choice, and they
serve no note and no source. Earth's word list therefore holds 16 rows
against 15 tick boxes. The counts differ ON PURPOSE; a change that makes
them match has probably dropped the belts from one list.

### One check reads the file the browser fetches [CRITICAL]
On 2026-09-17 both rooms broke on the live site -- the Sun showing 9
drawer rows instead of 18 -- while eleven checks passed. Every one of
them built its scene from the config or from a recorded fixture, and
none read the served cache, which is the file the browser fetches
(L-336).

So: for anything a visitor sees, ask WHICH FILE THE BROWSER ACTUALLY
FETCHES, and make one check read that file. Two exist now and both gate
the gallery runner. `tools/check_cache_in_step.py` compares the served
cache against the config it was built from. `gallery_maintenance_run.py
--live` fetches the served page's files and compares them with the
working copy; its list is eleven files as of `d9d7a48f`, and a new file
the page fetches by name is added to `SERVED_FILES` in the same push
that adds it (L-339).

### Logic that needs no browser lives in its own file [QUALITY]
Tony's ruling, 2026-09-18 (L-338). His reason first, because it is his:
to limit the growing size of `interactive.html`. The second reason is
that a check can then reach the logic as a FILE --
`documentation/smoke_arrival.js` used to test the arrival function by
cutting the text between two comment lines out of the page, which is a
check whose subject is a substring and which stops being true the moment
a comment line moves.

It is not a call for a general reorganisation. Logic moves out WHEN A
BUILD ALREADY TOUCHES IT. `gallery/arrival.js` is the first instance:
118 lines left the page, the smoke check now requires the file, and a
visitor saw no difference.

ONE SCOPE QUESTION IS OPEN and Tony should settle it the first time it
matters: his reason covers bulk that is not logic at all -- a long block
of styling, say -- and the testability reason says nothing about that.
Ask rather than assume.

ONE FLOOR OVER, the same rule applies to a Tkinter tool: everything in
`tools/exhibit_store_editor.py` above the window class runs without Tk,
and its suite exercises it there. Logic that needs no WINDOW must be
reachable without one, or the only way to test it is to open it and
look.

"""

IE_NOTES = """- 2026-09-17, L-334: Tony ruled the config is EDITED IN PLACE with the
  mirror's scanner, not dumped through `json.dump`. The manifest had
  proposed accepting a one-time reformat of all 929 lines; the mirror
  already edits in place, and two writers with two layouts would fight.
- 2026-09-18, L-334: not every shell is served with all six words --
  the Sun's core has no `note`. A form that shows a field it can never
  save is a trap, so the writer ADDS a missing word using the mirror's
  own insertion. 23 of the 192 shell-and-field combinations in the real
  config are additions.
- 2026-09-18, L-334: a check that could not fail. The writer's suite
  asserted that refusing `value` produced a message MENTIONING "value"
  -- and "value" is in the path, so emptying the refusal list left the
  suite green. It now asserts the reason. Found by emptying the list on
  purpose, which is the only way that class of hole is ever found.
- 2026-09-18, L-334: the stamp check had a blind spot of its own. It
  built Earth's features without the Sun direction, so the magnetopause
  and the bow shock drew nothing and two of Earth's sixteen shells were
  never examined. A check that examines less than it appears to is the
  same failure as a check that cannot fail.
- 2026-09-19, L-334: two copies of the editor lived in the gallery for
  a day -- `tools/exhibit_store_editor.py` from the patch and a stray
  at the repo root, saved from a file handed over for reading. They
  were byte-identical, which is exactly the trap. Deleted.
"""

# ======================================================================
# gallery-cache-builder 1.4 -> 1.5
# ======================================================================

GC_VERSION_OLD = """Skill version: 1.4 | Cut from tonyquintanilla.github.io @ 02d7163 (code) and palomas_orrery @ 2f0aabe (context), earlier @ 8e4b5ca (v1.3) | 2026-08-19
v1.4 adds Recovery from a failed swap: discard and re-run -- Tony's
operational rule of 2026-08-19, after a nightly run wiped the served tree
and the ~30 quarantine directories turned out to be the same mechanism
printing harmlessly every night since July 21 (L-216).
"""

GC_VERSION_NEW = """Skill version: 1.5 | Cut from tonyquintanilla.github.io @ d9d7a48f (tools/check_cache_in_step.py, gallery_maintenance_run.py, data/objects_config.json) and palomas_orrery @ e1a79f67 (LEDGER_CONSOLIDATED.md L-216, L-322, L-334, L-336) | 2026-09-19, with Anthropic's Claude Opus 5
v1.5 adds the rule the project did not have written down anywhere until
a config change reached the live site ahead of the cache and broke both
exhibit rooms: A CONFIG CHANGE IS NOT DEPLOYED UNTIL THE CACHE IS
REBUILT (L-336). It also corrects this skill's own claim that the failed
`staging -> live` rename was "one data point" -- there have been three,
the third on 2026-09-17 -- and writes down the hand routine Tony
actually uses now.
v1.4 adds Recovery from a failed swap: discard and re-run -- Tony's
operational rule of 2026-08-19, after a nightly run wiped the served tree
and the ~30 quarantine directories turned out to be the same mechanism
printing harmlessly every night since July 21 (L-216).
"""

GC_DEPLOY_RULE = """## A config change is not deployed until the cache is rebuilt [CRITICAL]

The rooms in `interactive.html` draw their shells from the SERVED CACHE,
`data/solar-system/coverage_index.json`, which this builder copies from
`data/objects_config.json`. Pushing the config alone changes nothing a
visitor sees -- except where the two disagree, and there it breaks the
page.

WHAT HAPPENED, 2026-09-17 (L-336). L-322's gallery half was pushed at
gallery `d2ca28b6` before the builder had run. The unit spellings had
changed in the config and in the renderers (`R_sun` to `r_sun`); the
cache still held the old spelling; the renderers refused every shell
that used it. Tony's phone showed the Sun's room with 9 drawer rows
instead of 18 and Earth's with 8, on the live site, while the
maintenance run printed 11 of 11.

THE ROUTINE, and it is one routine rather than a judgement call:

  1. Change `data/objects_config.json`.
  2. Run this builder. By hand -- see Operating mode.
  3. Run `python gallery_maintenance_run.py`.
  4. Commit the CONFIG AND THE CACHE TOGETHER, and push.

`tools/check_cache_in_step.py` gates step 3 and compares the served
cache against the config it was built from. A red "Cache in step" right
after a config change is CORRECT and means step 2 has not happened yet.

THE ONE EXCEPTION, and it is worth knowing because it is the only part
of a room's data the page reads directly: the `arrival` block --
`drawn` and `moon` -- is fetched from `data/objects_config.json` by
`gallery/arrival.js`, not from the cache. A change to what a room OPENS
on needs only the push. Everything else needs the builder.

"""

GC_ONE_DATA_POINT_OLD = """Two things are NOT established and should not be asserted. Whether the
`staging -> live` rename is exposed to the same lock as the cleanup, or
was unlucky once, is one data point. And the run record is written INSIDE
the generation, so a run whose swap fails strands its own record in a
directory `.gitignore` hides -- meaning the committed history shows no
sign that a run lost its data. Recording the swap OUTCOME outside the
generation comes BEFORE fixing the cause; otherwise every recurrence costs
another evening of inference.
"""

GC_ONE_DATA_POINT_NEW = """THREE OCCURRENCES, so the exposure IS established (corrected 2026-09-19;
this skill said "one data point" until then and that was already false).
The `staging -> live` rename is exposed to the same lock as the cleanup.
It is not bad luck. The third was 2026-09-17, during the rebuild L-336's
deployment fault made necessary; Tony: "This is like the third time."

WHAT IS STILL NOT ESTABLISHED is the fix, and one thing that is NOT a fix
is a louder failure. The run record is written INSIDE the generation, so
a run whose swap fails strands its own record in a directory `.gitignore`
hides -- meaning the committed history shows no sign that a run lost its
data. Recording the swap OUTCOME outside the generation comes BEFORE
fixing the cause; otherwise every recurrence costs another evening of
inference.

TONY'S HAND ROUTINE, 2026-09-17, and it is deliberate rather than a
workaround he would rather not need. The scheduled nightly is SUSPENDED.
He pauses OneDrive syncing FIRST, runs the builder by hand, and watches
GitHub Desktop's change list, stopping if the commit does not form
correctly. Pausing sync before a re-run worked.

ONE STEP IS ADDED TO THE DISCARD RULE ABOVE when the change list also
holds work that is not the cache -- which it did on 2026-09-17, because
the arrival work was sitting beside the wreckage. COMMIT THE NON-CACHE
FILES FIRST, then discard the rest, then re-run. A blanket discard would
have thrown away committed-worthy work.

MOVING THE REPOSITORIES OFF ONEDRIVE is the lasting fix and Tony's answer
on 2026-09-17 was "not at this time". It changes his machine outside his
usual working set and needs its steps and risks written out before he
decides. Do not propose it casually.
"""

GC_DESC_OLD = ("or wiring interactive.html to the served data. Do NOT use for the "
               "Studio/converter/viewer curation chain")
GC_DESC_NEW = ("or wiring interactive.html to the served data; and for the rule "
               "that a config change is not deployed until the cache is "
               "rebuilt. Do NOT use for the Studio/converter/viewer curation "
               "chain")

IE_DESC_OLD = ("when deciding what an exhibit may render. Not for propagation "
               "math (gallery-assembler)")
IE_DESC_NEW = ("when deciding what an exhibit may render; when touching the "
               "arrival block, the shell-key stamp, or the store editor and "
               "its writer. Not for propagation math (gallery-assembler)")

IE_FIRES_OLD = ('deciding what numbers an exhibit may render and where they '
                'come from; carding an exhibit in Studio')
IE_FIRES_NEW = ('deciding what numbers an exhibit may render and where they '
                'come from; what a room opens on (arrival block, drawn, moon); '
                'meta.shell_key and the trace stamp; editing the served words '
                'with store_writer or exhibit_store_editor; carding an exhibit '
                'in Studio')


def lf(text):
    return text.replace('\r\n', '\n')


def ledger_fingerprint(content):
    a = content.index(ZONE[0])
    b = content.index(ZONE[1]) + len(ZONE[1])
    return hashlib.md5((content[:a] + content[b:]).encode('utf-8')).hexdigest()


def main():
    if not os.path.exists(os.path.join(ROOT, 'LEDGER_CONSOLIDATED.md')):
        print('ERROR: LEDGER_CONSOLIDATED.md not found next to this script.')
        print('       Run this patch from the ORRERY repo ROOT, not from')
        print('       documentation/. NOTHING was written.')
        return 1

    loaded = {}
    for rel, want in FINGERPRINTS.items():
        path = os.path.join(ROOT, rel.replace('/', os.sep))
        if not os.path.exists(path):
            print('ERROR: %s not found. NOTHING was written.' % rel)
            return 1
        raw = open(path, 'rb').read()
        text = lf(raw.decode('utf-8'))
        got = (ledger_fingerprint(text) if rel.endswith('LEDGER_CONSOLIDATED.md')
               else hashlib.md5(text.encode('utf-8')).hexdigest())
        if got != want:
            print('ERROR: %s is not the file this patch was built against' % rel)
            print('       expected %s, found %s%s'
                  % (want, got, ' [CRLF]' if b'\r\n' in raw else ''))
            print('       NOTHING was written. Undo is Discard Changes in '
                  'GitHub Desktop.')
            return 1
        loaded[rel] = (text, b'\r\n' in raw)

    edits = build_edits(loaded)
    out = {}
    for rel, pairs in edits.items():
        text = loaded[rel][0]
        for old, new in pairs:
            n = text.count(old)
            if n != 1:
                print('ANCHOR FAIL in %s: expected 1 match, found %d: %r'
                      % (rel, n, old[:70]))
                print('NOTHING was written. Undo is Discard Changes in '
                      'GitHub Desktop.')
                return 1
            text = text.replace(old, new, 1)
        out[rel] = text

    for rel, text in out.items():
        bad = sum(1 for c in text if ord(c) > 127)
        if bad:
            print('ERROR: %s would hold %d non-ASCII character(s). NOTHING '
                  'was written.' % (rel, bad))
            return 1

    for rel, text in out.items():
        path = os.path.join(ROOT, rel.replace('/', os.sep))
        data = text.encode('ascii')
        if loaded[rel][1]:
            data = data.replace(b'\n', b'\r\n')
        open(path, 'wb').write(data)
        print('ok  %-38s (%d bytes%s)'
              % (rel, len(data), ', CRLF preserved' if loaded[rel][1] else ''))

    print('')
    print('=' * 70)
    print('PASTE THE FOLLOWING INTO documentation/PROJECT_INSTRUCTIONS_HISTORY.md,')
    print('PART 1, as the newest entry there. It has been REMOVED from')
    print('PROJECT_INSTRUCTIONS.md, so right now it lives nowhere else.')
    print('=' * 70)
    print(V359_ENTRY)
    print('=' * 70)
    print('')
    print('NEXT, in this order:')
    print('  1. python ledger_index.py LEDGER_CONSOLIDATED.md -- TWICE.')
    print('     The FIRST run prints CONSISTENCY PROBLEMS and names')
    print('     L-334 and L-338 as [auto-fix]. That is the indexer')
    print('     moving two closed blocks into section C -- its job,')
    print('     not a failure. It exits 0.')
    print('     The SECOND run is the verdict: "OK: 335 L-blocks')
    print('     parsed" -- 335, not 334, because L-340 is added -- and')
    print('     193 live items.')
    print('  2. python orrery_maintenance_run.py. The Skill manifest')
    print('     generator will REWRITE the table rather than report it')
    print('     unchanged -- that is it reading 1.4 and 1.5.')
    print('  3. Paste the entry above into PROJECT_INSTRUCTIONS_HISTORY.md.')
    print('  4. Move this script into documentation/, commit and push.')
    print('  5. Reinstall interactive-exhibit and gallery-cache-builder')
    print('     from Settings > Skills. This session cannot verify that,')
    print('     so the next one does it -- the ledger says so.')
    return 0


def build_edits(loaded):
    protocol = loaded['PROJECT_INSTRUCTIONS.md'][0]
    start = protocol.index('v3.59 (September 14, 2026):')
    end = protocol.index('Functional for Claude, readable for human')
    global V359_ENTRY
    V359_ENTRY = protocol[start:end].rstrip() + '\n'

    return {
        'skills/interactive-exhibit/SKILL.md': [
            (IE_DESC_OLD, IE_DESC_NEW),
            (IE_FIRES_OLD, IE_FIRES_NEW),
            (IE_VERSION_OLD, IE_VERSION_NEW),
            ('### Never mutate a plot from inside a Plotly event handler',
             IE_RULES + '### Never mutate a plot from inside a Plotly event handler'),
            ('## Field notes\n\n', '## Field notes\n\n' + IE_NOTES),
        ],
        'skills/gallery-cache-builder/SKILL.md': [
            (GC_DESC_OLD, GC_DESC_NEW),
            (GC_VERSION_OLD, GC_VERSION_NEW),
            (GC_ONE_DATA_POINT_OLD, GC_ONE_DATA_POINT_NEW),
            ('## Validation stance', GC_DEPLOY_RULE + '## Validation stance'),
        ],
        'PROJECT_INSTRUCTIONS.md': [
            ('Tony Quintanilla, PE | Claude | v3.61 | September 16, 2026',
             'Tony Quintanilla, PE | Claude | v3.62 | September 19, 2026'),
            ('Cut from ebdc55cc at https://github.com/tonylquintanilla/palomas_orrery',
             'Cut from e1a79f67 at https://github.com/tonylquintanilla/palomas_orrery'),
            ('v3.61 (September 16, 2026):', V362_ENTRY + 'v3.61 (September 16, 2026):'),
            (V359_ENTRY, ''),
        ],
        'LEDGER_CONSOLIDATED.md': ledger_edits(loaded),
    }


V362_ENTRY = """v3.62 (September 19, 2026): No rule changed in this document. TWO skill
bumps, taken after the build they record rather than before it, which is
the exception to v3.55's ordering and is stated here so it is not read as
a precedent: these rules were LEARNED in the build, and there was nothing
to write before it ran.

interactive-exhibit 1.3 -> 1.4 (L-334) and gallery-cache-builder
1.4 -> 1.5 (L-336, L-216).

WHAT THE EXHIBIT SKILL GAINS is what a room opens on and who may write
the file it is read from. The arrival block is served rather than coded,
and it is the one part of a room's data the page reads directly, so a
change to it reaches a visitor on the push while a change to a shell's
words waits for the cache builder. Every trace belonging to a served
shell now carries that shell's key, and a trace that loses its stamp is
DRAWN rather than hidden, which is why that rule is CRITICAL and why a
check reads every trace the renderers build. Two tools write the served
config and each has an ALLOW list rather than a refusal list. And Tony's
ruling of 2026-09-18 is in it: logic that needs no browser lives in its
own file, his reason -- the size of interactive.html -- first, and the
testability reason second.

WHAT THE BUILDER SKILL GAINS was true long before anyone wrote it down.
A CONFIG CHANGE IS NOT DEPLOYED UNTIL THE CACHE IS REBUILT, and the two
are committed together. On 2026-09-17 the config went out ahead of the
cache and both rooms broke on the live site -- the Sun showing 9 drawer
rows instead of 18 -- while eleven checks passed, because every one of
them read the config or a fixture and none read the file the browser
fetches. The same bump corrects this skill's own claim that the failed
folder swap was "one data point": there have been three, and the
exposure is established rather than unlucky.

THE OBLIGATION TRAVELS, as it always does. This session loaded 1.3 and
1.4, and a reinstall cannot be verified from inside the session that
makes it. The next session confirms its loaded copies read 1.4 and 1.5
before exhibit or cache work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.59 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""


def ledger_edits(loaded):
    return [
        ('<!-- L:334 status:OPEN upd:2026-09-18 section:A flag: rice:4/4/85/3 -->',
         '<!-- L:334 status:DONE upd:2026-09-19 section:C flag: rice:4/4/85/3 -->'),
        (L334_GAP_OLD, L334_STAGE_C + L334_GAP_NEW),
        ('<!-- L:338 status:OPEN upd:2026-09-18 section:A flag: rice:3/3/80/1 -->',
         '<!-- L:338 status:DONE upd:2026-09-19 section:C flag: rice:3/3/80/1 -->'),
        (L338_GAP_OLD, L338_GAP_NEW),
        ('<!-- L:216 status:OPEN upd:2026-09-17 section:A flag: rice:3/3/85/2 -->',
         '<!-- L:216 status:OPEN upd:2026-09-19 section:A flag: rice:3/3/85/2 -->'),
        (L216_ACTION_OLD, L216_ACTION_NEW),
        (SECTION_A_ANCHOR, SECTION_A_ANCHOR + L340_BLOCK),
    ]


SECTION_A_ANCHOR = ("## A. ACTIVE SEPARATE TRACKS (not orrery-refactor "
                    "backlog; cross-referenced)\n\n")

L340_BLOCK = '''#### [L-340] The exhibit store editor: what the first screenshot showed, and the Mode 5 pass
<!-- L:340 status:OPEN upd:2026-09-19 section:A flag: rice:3/3/90/1 -->
- **Opened 2026-09-19 because L-334 closed.** The editor is built,
  pushed and working; these are the things left, and a pointer in a
  closed item is not a home for them.
- **THREE THINGS VISIBLE IN TONY'S FIRST SCREENSHOT**, measured at
  gallery `d9d7a48f`, none of which he had hit yet:
  (1) Three shell names are cut off in the left list -- Streamer Belt
  (helmet and stalk), Chromosphere (2,000 km skin) and Galactic Tide
  (thinned at the plane), the longest 36 characters against a
  26-character listbox.
  (2) The `source` field is a single-line box 54 characters wide, and
  the Sun core's citation is 134 characters, so about a third of it is
  readable. A citation is a sentence; it wants a wrapped box like
  `description` and `about`.
  (3) The Sun's room shows a Moon tick. Its arrival block carries a
  `moon` key, so the panel offers it, but the Sun's scene has no Moon
  trace -- ticking it writes `true` and changes nothing.
- **AND THE MODE 5 PASS ITSELF**, which is the point of this item. Tony
  has seen the window in a screenshot and not yet used it. A checklist
  pass over both rooms will find things this list does not have, and
  those belong here.
- **Claude:** RICE 3/3/90/1 -> 8.1 proposed, unratified. Effort 1
  because all three are layout, in one file, with a suite that already
  walks every row; the Mode 5 pass is Tony's time rather than build
  time.
- **Ref:** L-334 (the build this hands over from), L-291 (the Earth
  room), L-320 (info markers); gallery `tools/exhibit_store_editor.py`,
  `tools/test_exhibit_store_editor.py`, `data/objects_config.json`;
  interactive-exhibit skill 1.4.

'''

L334_GAP_OLD = """**Gap (current, 2026-09-18):** STAGE C, the editor itself. Stage B is
done and its description is kept below as the record of what it was
contracted to do."""

L334_GAP_NEW = """**Gap:** none -- move to section C. What is left is cosmetic and is
carried by L-340, opened in the same patch: three things Tony's first
screenshot showed, plus the Mode 5 pass, listed there rather than
holding this item open.
**Gap (as it stood on 2026-09-18, DISCHARGED):** STAGE C, the editor
itself. Stage B is done and its description is kept below as the record
of what it was contracted to do."""

L334_STAGE_C = """- **STAGE C BUILT, PUSHED and SEEN, 2026-09-18/19, in three pushes.**
  The writer at gallery `d3e90bae`
  (`patch_L334_5_store_writer_20260918.py`), the window at
  `dcdeea35` (`patch_L334_8_store_editor_20260919.py`), and the
  dashboard button in the orrery at `8989b13d` and `e1a79f67`
  (`patch_L334_6`, then `patch_L334_7` moving it to Gallery & Web on
  Tony's second thought and sorting that group). Tony, on the first
  screenshot of the window with both rooms loading: "looks great... both
  sun and earth! good job." [render-confirmed Mode 5]
- **WHAT EXISTS NOW.** `tools/store_writer.py`, which edits
  `data/objects_config.json` in place through the mirror's scanner;
  `tools/exhibit_store_editor.py`, the window, one panel on Tony's
  ruling of 2026-09-18 with the shells at the left, the form in the
  middle and the arrival ticks at the right on their own ground;
  `tools/test_store_writer.py` (245 checks) and
  `tools/test_exhibit_store_editor.py` (240 without a window, 280 with
  one), both gating the gallery runner, which is 14 of 14.
- **THE DESIGN CHANGED ONCE, ON REVIEW, AND THE CHANGE WAS RIGHT.**
  Claude Fable 5.1 reviewed the writer on 2026-09-18 and found that a
  REFUSAL list of six field names accepted everything else -- it would
  change a room's `slug` to "earthx" or a shell's `color` to "zzz",
  either of which breaks a room. Reproduced, then rebuilt around an
  ALLOW list read from the config: 204 paths. The weakness came from the
  manifest asking for a refusal list, and the general form is worth
  keeping: a refusal list has to anticipate every way of being wrong; an
  allow list only has to know what is right. Fable's other two notes are
  in as well -- an empty word is not added, and a belt's words turn out
  to be reachable, which made leaving the belts out of the editor a
  choice rather than a limit. Tony ruled them IN on 2026-09-18.
- **THREE THINGS THE BUILD FOUND THAT THE CONTRACT HAD WRONG.** (1) Not
  every shell carries all six words -- the Sun's core has no `note` --
  so the writer ADDS a missing word rather than refusing it; 23 of 192
  shell-and-field combinations are additions. (2) The shell list cannot
  be a plain config walk, which gives 22 for Earth where the renderers
  draw 16; the rule that matches is `check_cache_in_step.py`'s, a member
  carrying a display `name`. (3) Earth's belts have no per-belt key, so
  the word list holds 16 rows against 15 tick boxes, on purpose.
- **AND ONE OF CLAUDE'S OWN CHECKS COULD NOT FAIL.** The writer's suite
  asserted that refusing `value` produced a message MENTIONING "value".
  "value" is in the path, so emptying the refusal list left the suite
  green. Found by emptying it on purpose. The suite now asserts the
  reason. Same session, a second instance: the stamp check built Earth's
  features without the Sun direction, so two of Earth's sixteen shells
  were never examined by the check written to examine all of them.
- **RECORDS, and this note is them.** interactive-exhibit 1.3 -> 1.4 and
  gallery-cache-builder 1.4 -> 1.5, under one protocol entry, v3.62.
  **Tony-action (do):** reinstall both from Settings > Skills after the
  push. A mid-session reinstall cannot be verified from inside the
  session that makes it, so THE NEXT SESSION confirms its loaded copies
  read 1.4 and 1.5 before exhibit or cache work.
"""

L338_GAP_OLD = """**Gap:** the rule does not travel until it is in a skill a page edit
loads. It goes into interactive-exhibit 1.4 as piece 6 of L-334's stage
C, with the wording above for Tony to read. A convention that is not in
the skill does not travel (L-317, L-326, L-335, now here)."""

L338_GAP_NEW = """- **CLOSED 2026-09-19.** The rule is in interactive-exhibit 1.4, under
  its own heading, with Tony's reason first and the testability reason
  second, and with the scope question named as open rather than settled
  quietly: his reason covers bulk that is not logic, and the
  testability reason does not. A page edit loads that skill, so the rule
  now travels.
**Gap:** none -- move to section C."""

L216_ACTION_OLD = """**Tony-action (do) -- SCHEDULED:** the skill sentence that calls this
"one data point" is corrected in gallery-cache-builder 1.5, together with
the hand routine above, as piece 6 of L-334's stage C."""

L216_ACTION_NEW = """**Tony-action (do) -- DONE 2026-09-19:** gallery-cache-builder 1.5 now
says three occurrences and that the exposure is established rather than
unlucky, and carries the hand routine above, including the step that
commits non-cache files before discarding. This item stays OPEN for the
CAUSE, not for the record of it."""


if __name__ == '__main__':
    sys.exit(main())
