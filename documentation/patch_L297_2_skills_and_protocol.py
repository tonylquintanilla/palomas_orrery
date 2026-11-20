"""
patch_L297_2_skills_and_protocol.py - the three skill updates L-297's
round learned, the protocol's v3.143, and L-537 (the skills page moved).

RUN COMMAND
    Save this file in the orrery folder (palomas_orrery_for_github),
    open it in VS Code and click Run:

        python patch_L297_2_skills_and_protocol.py

    Success: one "ok" line per step, then the two index tools, then
    "patch applied". Failure: an "ERROR:" or "ANCHOR FAIL" line, and
    NOTHING is written. Undo after a success: Discard Changes in GitHub
    Desktop.

    It touches no file the colour patch (patch_L432_1) touches, so the
    two run in either order.

WHY
    L-297's Session 2 (the website) ran out of time before Tony's push
    window of Nov 19 for the skill bumps its brief named; L-297's Gap
    carries them, with L-537. By the records skill's binding rule a bump
    travels as four steps in one commit: the SKILL.md, skills_index.py,
    a protocol version entry, and the commit. This is that.

WHAT IT DOES
    1. gallery-cache-builder 1.19 -> 1.20: A Lagrange Point Is Served as
       a Point, the fourth serving shape.
    2. interactive-exhibit 1.42 -> 1.43: a point drawn as its marker
       alone at the minute shown, its box, and a name's side set per
       body; Install and verify names the skills page where it is.
    3. provenance-discipline 2.36 -> 2.37: the working-out between
       served points, a third error, worked out for the curve the page
       draws (Tony, 2026-11-18), on for the points and the open-path
       comets only.
       Each skill is at its line cap, so each moves its oldest version
       entry, and the cache builder and provenance one passage of
       history each, word for word, to documentation/SKILL_HISTORIES.md.
    4. PROJECT_INSTRUCTIONS.md v3.143: its entry; the header; Stale
       Skill = Stop names "Plugins, in the claude.ai sidebar" in place of
       "Settings > Skills" (L-537; the older version entries keep their
       words); v3.140 moves down to
       documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1.
    5. The ledger: L-537 closed; L-297's Gap says the bumps are written.
    6. Runs skills_index.py (the manifest and the read plans) and
       ledger_index.py, then skills_index.py --check and
       doc_index.py --caps, and reports each.

AFTER IT RUNS
    1. (do) Move this file into documentation\\.
    2. (do) Commit and push the orrery, not while a night is running.
    3. (do) Reinstall three skills, gallery-cache-builder,
       interactive-exhibit and provenance-discipline (Plugins, in the
       claude.ai sidebar), and paste PROJECT_INSTRUCTIONS.md into the
       Project's instructions on claude.ai.

Built on palomas_orrery @ 4c44ea87c2399cef9a3b092428c06a6a9ec8bd52 and
gallery @ 0c832de1, Nov 19, 2026, with Anthropic's Claude Opus 5.5 (the
coordinating session), from L-297's notes and the code at orrery
a70d98c5 and gallery 56bc3fab.
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATE = '2026-11-19'

GCB = 'skills/gallery-cache-builder/SKILL.md'
IE = 'skills/interactive-exhibit/SKILL.md'
PD = 'skills/provenance-discipline/SKILL.md'
HIST = 'documentation/SKILL_HISTORIES.md'
PI = 'PROJECT_INSTRUCTIONS.md'
PIH = 'documentation/PROJECT_INSTRUCTIONS_HISTORY.md'
LEDGER = 'LEDGER_CONSOLIDATED.md'

# Each file must read its expected version before anything is written.
GUARDS = [
    (GCB, 'Skill version: 1.19 | 2026-11-11'),
    (IE, 'Skill version: 1.42 | 2026-11-12'),
    (PD, 'Skill version: 2.36 | 2026-10-29'),
    (PI, 'Tony Quintanilla, PE | Claude | v3.142 | November 18, 2026'),
]

# ---- gallery-cache-builder 1.20 -----------------------------------------

GCB_ENTRY = """Skill version: 1.20 | 2026-11-19, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ a70d98c5 and gallery @ 56bc3fab. v1.20 (L-297, the
Lagrange points) adds A Lagrange Point Is Served as a Point, the fourth
serving shape. To stay at the cap, the 1.17 entry, Fetch facts proven
live and a size note of 2026-10-25 moved out. Read from L-297's notes
and the gallery's builder at 56bc3fab before it was written.
Earlier: 1.19 | 2026-11-11, with Anthropic's Claude Opus 5.5, at
"""

GCB_SECTION = """## A Lagrange Point Is Served as a Point [QUALITY]

v1.20, L-297: the fourth shape, `serving_shape` 'point' (category
'lagrange_point'). A point has no mass and no orbit, so no elements
are fetched: only JPL's positions around the centre it is served
around (Earth for the Earth-Moon points, the Sun for the Earth-Sun
ones), a day apart across the served window and a day past each edge,
and an hour apart from yesterday to the day after tomorrow (`POINT_*`;
Tony, 2026-11-19). Fetched last, once the window is known
(`point_window`); a point never takes part in the window
(`served_window_from`), so it cannot narrow it. JPL's answer is held to
the point's own name: asked for 3013, JPL answers an asteroid. A failed
fetch serves the saved days (`serve_last_good_point`), today's point
nulled; the validator's #L (`point_problems`) refuses elements, a short
span, a missing day or hour, each planted.

"""

GCB_FIRES_OLD = ("an ended mission's last day (fetch_path_last_day), a "
                 "held body (HELD)\n---\n")
GCB_FIRES_NEW = ("an ended mission's last day (fetch_path_last_day), a "
                 "held body (HELD), a Lagrange point served as a point "
                 "(serving_shape 'point')\n---\n")

GCB_SIZE = """- SIZE: the first simulated build of 2026-10-25, on fake straight paths,
  served 68 KB of positions for the twelve; before the windows were
  thinned at their own scale it was about 1.7 MB. The real paths curve,
  so the first real build measures it.
"""

# ---- interactive-exhibit 1.43 -------------------------------------------

IE_ENTRY = """Skill version: 1.43 | 2026-11-19, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ a70d98c5 and gallery @ 56bc3fab. v1.43 (L-297, the
Lagrange points) adds A point is a marker, and a name has a side: a
point drawn as its marker alone at the minute shown, its box, and a
name's side set per body on Tony's look. Install and verify names the
skills page where it now is (L-537). To stay at the cap, the 1.40 entry
moved out. Read from L-297's notes and the gallery at 56bc3fab before
it was written.
Earlier: 1.42 | 2026-11-12, with Anthropic's Claude Opus 5.5, at
"""

IE_SECTION = """### A point is a marker, and a name has a side [QUALITY]

v1.43, L-297. A Lagrange point is drawn as its marker alone, the
orrery's open square, its name beside it, placed by `position_at` at
the minute shown (`render_spacecraft.build_point_traces`): no line, no
orbit. A point served around another body is drawn at that body's place
by ADDING, as a moon is (`compose_children.build_point_child_traces`).
The fetched centre rules the drawer (Tony, 2026-11-07, 11:26): the
Earth-Moon points are Earth's children, in its fold by distance; the
Earth-Sun points are a root group after Earth's row. The box
(`SolarSystemFigures.pointBox`): the name, the approved words, the
distance from its own centre, and "JPL states no accuracy for this
position." (JPL's 2xr answer is "n.a."); no orbit, no period.
A NAME'S SIDE is set per body (`presentation.label_side_for`, its
`_LABEL_SIDES` map), "top center" for every body not set; a side is
Mode 5, set on Tony's look (ESCAPADE-Gold below, Earth-Moon L1 left).
Bodies that share a few pixels at a room's scale keep their pile-up:
Centre on with the frame zoom is the answer (Tony, 2026-11-19).

"""

IE_FIRES_OLD = ("testing a room (the gallery run's checks, "
                "tools/headless); carding an exhibit in Studio\n---\n")
IE_FIRES_NEW = ("testing a room (the gallery run's checks, "
                "tools/headless); carding an exhibit in Studio; a "
                "Lagrange point's marker and box, a name's side "
                "(label_side_for)\n---\n")

IE_INSTALL_OLD = """Install to the account (Settings > Skills). Run `skills_index.py` so the
manifest in PROJECT_INSTRUCTIONS.md carries the version. Per Stale Skill
= Stop, the session that installs a version cannot verify the install.
Earlier installs and their confirmations, 1.0 to 1.41:
documentation/SKILL_HISTORIES.md, under interactive-exhibit.
1.42 was cut on 2026-11-12 in the Claude Code session for L-527, through
the python_work door, from the repo's copy of 1.41; a session that loads
the account's copy confirms it reads 1.42 before exhibit work.
"""
IE_INSTALL_NEW = """Install to the account (Plugins, in the claude.ai sidebar). Run
`skills_index.py` so the manifest in PROJECT_INSTRUCTIONS.md carries the
version. Per Stale Skill = Stop, the session that installs a version
cannot verify the install. Earlier installs and their confirmations,
1.0 to 1.42: documentation/SKILL_HISTORIES.md, under interactive-exhibit.
1.43 was written on 2026-11-19 by the coordinating session for L-297,
from the repo's copy of 1.42; a session that loads the account's copy
confirms it reads 1.43 before exhibit work.
"""
IE_INSTALL_142 = """1.42 was cut on 2026-11-12 in the Claude Code session for L-527, through
the python_work door, from the repo's copy of 1.41; a session that loads
the account's copy confirms it reads 1.42 before exhibit work.
"""

IE_OLDER_OLD = "and 2026-11-11 (L-522) and 2026-11-12 (L-527).\n"
IE_OLDER_NEW = ("and 2026-11-11 (L-522) and 2026-11-12 (L-527) and\n"
                "2026-11-19 (L-297).\n")

# ---- provenance-discipline 2.37 ------------------------------------------

PD_ENTRY = """Skill version: 2.37 | 2026-11-19, with Anthropic's Claude Opus 5.5, at
palomas_orrery @ a70d98c5 and gallery @ 56bc3fab. v2.37 (L-297) adds a
third error to A Computed Position Prints What Its Errors Earn: the
working-out between served points, for the curve the page draws (Tony,
2026-11-18). The 2.34 entry and a census of 2026-08-27 moved out.
Earlier: 2.36 | 2026-10-29, with Anthropic's Claude Opus 5.5, at
"""

PD_TWO_OLD = "count comes from its errors, and two of them bound it:\n"
PD_TWO_NEW = "count comes from its errors, and these bound it:\n"

PD_BULLET_ANCHOR = "  error itself and is used whole (v2.36, L-399).\n"
PD_BULLET_NEW = PD_BULLET_ANCHOR + """- **The working-out between served points** (v2.37, L-297). A body
  placed by its served positions (a spacecraft, a comet on an open
  path, a Lagrange point) sits on the parabola through the three
  points nearest the minute (`render_spacecraft.position_at`). Its error
  is the curve's, not the chord's (Tony, 2026-11-18): twice the larger
  gap between that parabola and the cubic through one more point, each
  side; never under the real miss in about 3,000 held-out points,
  undoubled under it half the time. On only where that holds
  (`CURVE_KINDS`, the "Curve error" row); orbiters wait for L-538.
"""

PD_LARGER_OLD = """**The display prints to the Report test's place (The ceiling, Report)
for the LARGER of the two**, each unit placed by its own error, never"""
PD_LARGER_NEW = """**The display prints to the Report test's place (The ceiling, Report)
for the LARGEST of them**, each unit placed by its own error, never"""

PD_CENSUS_START = "Census re-measured at `7f4a2f9f` (2026-08-27): 42 remaining --\n"
PD_CENSUS_END = "follow-up, from 16.) The rest clear in Batch 2.\n"
PD_CENSUS_POINTER = """Disposal is not a separate deletion patch: the status pass REPLACES
each stamp with a real `# Status:` line as it passes through. The
census of 2026-08-27 (42 then) is in documentation/SKILL_HISTORIES.md.
"""

PD_OLDER_OLD = "(L-443) and 2026-10-29 (L-399).\n"
PD_OLDER_NEW = "(L-443), 2026-10-29 (L-399) and 2026-11-19 (L-297).\n"

# ---- the protocol v3.143 -------------------------------------------------

PI_HEADER_OLD = """Tony Quintanilla, PE | Claude | v3.142 | November 18, 2026

Cut from 00c89ef0 at https://github.com/tonylquintanilla/palomas_orrery"""
PI_HEADER_NEW = """Tony Quintanilla, PE | Claude | v3.143 | November 19, 2026

Cut from 4c44ea87 at https://github.com/tonylquintanilla/palomas_orrery"""

PI_GATE1_OLD = "account install (Settings > Skills -- the copy Claude actually loads), and\n"
PI_GATE1_NEW = ("account install (Plugins, in the claude.ai sidebar -- the copy Claude\n"
                "actually loads), and\n")
PI_GATE2_OLD = "  - (do) reinstall it to the account profile (Settings > Skills),\n"
PI_GATE2_NEW = "  - (do) reinstall it to the account (Plugins, in the claude.ai sidebar),\n"

PI_ENTRY_ANCHOR = "v3.142 (November 18, 2026): No rule changed in this document. ONE\n"
PI_ENTRY = """v3.143 (November 19, 2026): One instruction's wording changed in this
document, and THREE skills bumped, from L-297 (the Lagrange points) and
L-537 (the skills page moved).

WHAT PROMPTED IT. The Claude Code sessions of Nov 18 and 19 (Claude
Opus 5.5), through the python_work door, keyed eight Lagrange points in
the orrery and served and drew them on the website, pushed at orrery
a70d98c5 and gallery 56bc3fab. JPL has no L3: the orrery's two L3
entries had drawn two asteroids, and are gone. Session 2 reached Tony's
push window before the skills; the coordinating session wrote them from
L-297's notes and the code at those SHAs.

WHAT CHANGED. gallery-cache-builder 1.19 -> 1.20: A Lagrange Point Is
Served as a Point, the fourth serving shape. interactive-exhibit 1.42
-> 1.43: a point drawn as its marker alone at the minute shown, its
box, and a name's side set per body on Tony's look.
provenance-discipline 2.36 -> 2.37: the working-out between served
points is a third error, worked out for the curve the page draws, not
the straight chord (Tony, Nov 18: "the straight path is not what is
happening"), on for the Lagrange points and open-path comets only; a
craft orbiting a planet keeps the chord until L-538. Each skill moved
its oldest version entry, and two of them a passage of history, to
documentation/SKILL_HISTORIES.md to stay at its cap. In this document,
Stale Skill = Stop names the skills page where it now is, Plugins in
the claude.ai sidebar, in place of Settings > Skills (L-537, closed);
the older version entries keep the words they were written with.

THE OBLIGATION TRAVELS. This session wrote the three from the repo's
copies, 1.19, 1.42 and 2.36, as the manifest expected. Tony reinstalls
all three (Plugins, in the claude.ai sidebar) and pastes this version
into the Project's instructions on claude.ai; the next session that
loads each from the account confirms its copy reads 1.20, 1.43 or 2.37
before that work.

The header stamp and the SHA anchor move with this entry.

Version history: v3.140 moves down to
documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three
resident.

"""

PI_V3140_START = "v3.140 (November 12, 2026, night): No rule changed in this document.\n"
PI_TAIL = "\n\nFunctional for Claude, readable for human, signal preserved."

PIH_ANCHOR = """(Moved down from the resident protocol on 2026-11-18, when
v3.142 made a fourth entry.)
"""

# ---- the ledger ----------------------------------------------------------

L537_META_OLD = "<!-- L:537 status:OPEN upd:2026-11-18 section:A flag: rice: -->\n"
L537_META_NEW = "<!-- L:537 status:DONE upd:2026-11-19 section:A flag: rice: -->\n"
L537_GAP_OLD = """**Gap:** the correction, at the next protocol version and at
interactive-exhibit's next version (L-297's round, if it bumps it).
"""
L537_GAP_NEW = """**Note:** (2026-11-19, the coordinating session, Claude Opus 5.5) corrected
by patch_L297_2_skills_and_protocol.py: the protocol's Stale Skill gate
(its two lines) and interactive-exhibit 1.43's Install and verify now
say "Plugins, in the claude.ai sidebar". The protocol's older version
entries (v3.141, v3.142, and v3.140, moved down) keep "Settings >
Skills": they record what was true when written. The help page, read
again Nov 19 (support.claude.com, article 17740565): in the sidebar,
what was Customize becomes Plugins, one Plugins page in place of the
Skills, Connectors and Plugins tabs. Some of claude.com's docs still
say Customize, so the change is still rolling out.
**Gap:** none.
"""

L297_GAP_OLD = """phone look; the skill bumps above, one protocol entry (v3.143), with
L-537.
"""
L297_GAP_NEW = """phone look; the skill bumps above are written, with L-537
(patch_L297_2_skills_and_protocol.py, Nov 19): Tony reinstalls the
three and pastes v3.143.
"""


# ---- the harness ---------------------------------------------------------

def fail(msg):
    print('ERROR: ' + msg)
    print('NOTHING was written.')
    sys.exit(1)


def read(rel):
    path = os.path.join(HERE, rel)
    if not os.path.exists(path):
        fail('%s not found. Save this patch in the orrery folder'
             ' (palomas_orrery_for_github).' % rel)
    raw = open(path, 'rb').read()
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), b'\r\n' in raw


def once(text, old, new, label):
    n = text.count(old)
    if n != 1:
        print('ANCHOR FAIL: %s (expected 1 match, found %d)' % (label, n))
        print('NOTHING was written.')
        sys.exit(1)
    print('ok ' + label)
    return text.replace(old, new)


def cut(text, start, end_before, label):
    """Remove [start, end_before) from text; return (text, removed)."""
    if text.count(start) != 1 or text.count(end_before) != 1:
        print('ANCHOR FAIL: %s (its start or end is not found once)' % label)
        print('NOTHING was written.')
        sys.exit(1)
    a = text.index(start)
    b = text.index(end_before)
    if b <= a:
        fail('%s: its end comes before its start.' % label)
    print('ok cut: ' + label)
    return text[:a] + text[b:], text[a:b]


def main():
    print('patch_L297_2: three skill bumps, the protocol v3.143, L-537')
    files, crlf = {}, {}
    for rel in (GCB, IE, PD, HIST, PI, PIH, LEDGER):
        files[rel], crlf[rel] = read(rel)
    for rel, line in GUARDS:
        if line not in files[rel]:
            fail('%s does not read "%s". It may already be updated, or the'
                 ' base moved: pull origin, then tell Claude.' % (rel, line))
        print('ok base: %s reads %s' % (rel, line.split('|')[0].strip()
                                        if 'Skill' in line else 'v3.142'))

    # gallery-cache-builder
    t = files[GCB]
    t, gcb_117 = cut(t, "Earlier: 1.17 | 2026-11-02",
                     "Older entries are in documentation/SKILL_HISTORIES.md, moved there on\n2026-10-05 (L-418), 2026-10-14 (L-431)",
                     'cache builder: the 1.17 entry')
    t = once(t, "Skill version: 1.19 | 2026-11-11, with Anthropic's Claude Opus 5.5, at\n",
             GCB_ENTRY, 'cache builder: the 1.20 entry')
    t = once(t, "2026-11-05 (L-507) and 2026-11-11 (L-525).\n",
             "2026-11-05 (L-507), 2026-11-11 (L-525) and 2026-11-19 (L-297).\n",
             'cache builder: the older-entries line')
    t = once(t, GCB_FIRES_OLD, GCB_FIRES_NEW, 'cache builder: fires_when')
    t = once(t, "- A Spacecraft Is Fetched by Its Plan [QUALITY]\n",
             "- A Spacecraft Is Fetched by Its Plan [QUALITY]\n"
             "- A Lagrange Point Is Served as a Point [QUALITY]\n",
             'cache builder: contents, the new section')
    t = once(t, "- Fetch facts proven live (2026-07-11 gate)\n", "",
             'cache builder: contents, Fetch facts out')
    t = once(t, GCB_SIZE, "", 'cache builder: the size note out')
    t, gcb_facts = cut(t, "## Fetch facts proven live (2026-07-11 gate)\n",
                       "## Field notes\n", 'cache builder: Fetch facts proven live')
    t = once(t, "## A Small Body's Own Uncertainty Is Served [QUALITY]\n",
             GCB_SECTION + "## A Small Body's Own Uncertainty Is Served [QUALITY]\n",
             'cache builder: A Lagrange Point Is Served as a Point')
    files[GCB] = t

    # interactive-exhibit
    t = files[IE]
    t, ie_140 = cut(t, "Earlier: 1.40 | 2026-11-10",
                    "Older entries are in documentation/SKILL_HISTORIES.md, moved there on\n2026-10-05 (L-418), 2026-10-10 (L-429)",
                    'exhibit: the 1.40 entry')
    t = once(t, "Skill version: 1.42 | 2026-11-12, with Anthropic's Claude Opus 5.5, at\n",
             IE_ENTRY, 'exhibit: the 1.43 entry')
    t = once(t, IE_OLDER_OLD, IE_OLDER_NEW, 'exhibit: the older-entries line')
    t = once(t, IE_FIRES_OLD, IE_FIRES_NEW, 'exhibit: fires_when')
    t = once(t, "  - The Solar System room's drawer: bodies, not shells [QUALITY]\n",
             "  - The Solar System room's drawer: bodies, not shells [QUALITY]\n"
             "  - A point is a marker, and a name has a side [QUALITY]\n",
             'exhibit: contents, the new section')
    t = once(t, "### A room's drawer lists its shells where each begins [QUALITY]\n",
             IE_SECTION + "### A room's drawer lists its shells where each begins [QUALITY]\n",
             'exhibit: A point is a marker, and a name has a side')
    t = once(t, IE_INSTALL_OLD, IE_INSTALL_NEW, 'exhibit: Install and verify (L-537)')
    files[IE] = t

    # provenance-discipline
    t = files[PD]
    t, pd_234 = cut(t, "Earlier: 2.34 | 2026-10-22",
                    "Older entries are in documentation/SKILL_HISTORIES.md, moved there\non 2026-10-05",
                    'provenance: the 2.34 entry')
    t = once(t, "Skill version: 2.36 | 2026-10-29, with Anthropic's Claude Opus 5.5, at\n",
             PD_ENTRY, 'provenance: the 2.37 entry')
    t = once(t, PD_OLDER_OLD, PD_OLDER_NEW, 'provenance: the older-entries line')
    t = once(t, PD_TWO_OLD, PD_TWO_NEW, 'provenance: "these bound it"')
    t = once(t, PD_BULLET_ANCHOR, PD_BULLET_NEW,
             'provenance: the working-out between served points')
    t = once(t, PD_LARGER_OLD, PD_LARGER_NEW, 'provenance: "the LARGEST of them"')
    a = t.index(PD_CENSUS_START) if t.count(PD_CENSUS_START) == 1 else -1
    if a < 0 or t.count(PD_CENSUS_END) != 1:
        fail('provenance: the census paragraph is not where it was.')
    b = t.index(PD_CENSUS_END) + len(PD_CENSUS_END)
    pd_census = t[a:b]
    t = t[:a] + PD_CENSUS_POINTER + t[b:]
    print('ok provenance: the census of 2026-08-27 out, a pointer left')
    files[PD] = t

    # the histories, each moved passage word for word
    h = files[HIST]
    h = once(h, "\n## horizons-orbital-mechanics\n",
             "\nThe 1.17 entry, moved here on %s (L-297), when 1.20 made a\n"
             "fourth resident entry:\n\n%s\n"
             "The size note from A Spacecraft Is Fetched by Its Plan and the\n"
             "section Fetch facts proven live, moved here word for word on\n"
             "%s (L-297, the skill at its cap):\n\n%s\n%s"
             "\n## horizons-orbital-mechanics\n"
             % (DATE, gcb_117.rstrip('\n'), DATE, GCB_SIZE, gcb_facts.rstrip('\n') + '\n'),
             'histories: the cache builder\'s three passages')
    h = once(h, "\n## safe-file-editing\n",
             "\nThe 1.40 entry, moved here on %s (L-297), when 1.43 made a\n"
             "fourth resident entry:\n\n%s\n"
             "The 1.42 install, from Install and verify, %s (L-297):\n%s"
             "\n## safe-file-editing\n"
             % (DATE, ie_140.rstrip('\n'), DATE, IE_INSTALL_142),
             'histories: the exhibit\'s 1.40 entry and 1.42 install')
    h = once(h, "\n## interactive-exhibit\n",
             "\nThe 2.34 entry, moved here on %s (L-297), when 2.37 made a\n"
             "fourth resident entry:\n\n%s\n"
             "The census of `# Verified:` stamps, from Retired: `# Verified:\n"
             "April 2026 via Gemini fact-check`, moved here word for word on\n"
             "%s (L-297, the skill at its cap):\n\n%s"
             "\n## interactive-exhibit\n"
             % (DATE, pd_234.rstrip('\n'), DATE, pd_census),
             'histories: provenance\'s 2.34 entry and census')
    files[HIST] = h

    # the protocol
    p = files[PI]
    p = once(p, PI_HEADER_OLD, PI_HEADER_NEW, 'protocol: header v3.143')
    p = once(p, PI_GATE1_OLD, PI_GATE1_NEW, 'protocol: Stale Skill gate, the stores')
    p = once(p, PI_GATE2_OLD, PI_GATE2_NEW, 'protocol: Stale Skill gate, reinstall')
    p = once(p, PI_ENTRY_ANCHOR, PI_ENTRY + PI_ENTRY_ANCHOR, 'protocol: the v3.143 entry')
    if p.count(PI_V3140_START) != 1 or p.count(PI_TAIL) != 1:
        fail('protocol: the v3.140 entry is not where it was.')
    a = p.index(PI_V3140_START)
    b = p.index(PI_TAIL)
    v3140 = p[a:b].rstrip('\n') + '\n'
    p = p[:a].rstrip('\n') + '\n' + p[b:]
    print('ok protocol: v3.140 out')
    files[PI] = p
    files[PIH] = once(files[PIH], PIH_ANCHOR,
                      PIH_ANCHOR + '\n' + v3140 + '\n(Moved down from the resident'
                      ' protocol on %s, when\nv3.143 made a fourth entry.)\n' % DATE,
                      'protocol history: v3.140 in')

    # the ledger
    l = files[LEDGER]
    l = once(l, L537_META_OLD, L537_META_NEW, 'ledger: L-537 DONE')
    l = once(l, L537_GAP_OLD, L537_GAP_NEW, 'ledger: L-537 note')
    l = once(l, L297_GAP_OLD, L297_GAP_NEW, 'ledger: L-297 Gap')
    files[LEDGER] = l

    for rel, text in files.items():
        bad = sum(1 for ch in text if ord(ch) > 127)
        if bad:
            print('note: %s holds %d non-ASCII character(s) this patch did'
                  ' not write' % (rel, bad))
    for new in (GCB_ENTRY, GCB_SECTION, IE_ENTRY, IE_SECTION, IE_INSTALL_NEW,
                PD_ENTRY, PD_BULLET_NEW, PI_ENTRY, L537_GAP_NEW, L297_GAP_NEW):
        if any(ord(ch) > 127 for ch in new):
            fail('this patch would write a non-ASCII character.')

    for rel, text in files.items():
        with open(os.path.join(HERE, rel), 'wb') as f:
            f.write(text.encode('utf-8'))
        print('ok written: %s%s' % (rel, ' (was CRLF; written LF)'
                                    if crlf[rel] else ''))

    def run(args, label):
        r = subprocess.run([sys.executable] + args, cwd=HERE,
                           capture_output=True, text=True)
        tail = (r.stdout.strip().splitlines() or [''])[-1]
        print('%s %s: %s' % ('ok' if r.returncode == 0 else 'RED', label, tail))
        if r.returncode != 0:
            print(r.stdout[-1500:])
            print(r.stderr[-800:])
        return r.returncode == 0

    good = run(['skills_index.py', 'PROJECT_INSTRUCTIONS.md'], 'skills_index.py')
    good &= run(['ledger_index.py'], 'ledger_index.py')
    good &= run(['skills_index.py', '--check'], 'skills_index.py --check')
    good &= run(['doc_index.py', '--caps'], 'doc_index.py --caps')
    if not good:
        print('The files are written but a check above is RED. Undo is'
              ' Discard Changes in GitHub Desktop; then tell Claude.')
        sys.exit(1)

    print('patch applied')
    print()
    print('Do next:')
    print('  1. (do) Move this file into documentation\\.')
    print('  2. (do) Commit and push the orrery, not while a night is running.')
    print('  3. (do) Reinstall gallery-cache-builder, interactive-exhibit and')
    print('     provenance-discipline (Plugins, in the claude.ai sidebar), and')
    print("     paste PROJECT_INSTRUCTIONS.md into the Project's instructions.")


if __name__ == '__main__':
    main()
