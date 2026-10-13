"""patch_L431_8_no_bary_perturbation_20261013.py -- L-431 (orbital
periods from JPL): Tony's ruling of 2026-10-13, no perturbation lines
for an orbit drawn around the solar system's barycentre;
horizons-orbital-mechanics 1.5 and protocol v3.94 record it.

Built on orrery 400a9615ce7238ec4e836c5eeba9b359c5f619bf at
https://github.com/tonylquintanilla/palomas_orrery ("L431 build 2 L436",
with patch_L431_7 run). The gallery is not touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\;
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\.
Written October 13, 2026 with Anthropic's Claude Opus 5.5.
Record: section 6 of documentation/HANDOFF_L431_build2_look_fixes_20261013.md
(added by this patch).

HOW TO RUN
    From the orrery repo's ROOT folder: open this file in VS Code and
    press Run, or from a terminal in that folder:
        python patch_L431_8_no_bary_perturbation_20261013.py
    Success prints one "ok" line per edit, then "patch applied". It asks
    nothing and fetches nothing. A second run finds its anchors gone and
    writes nothing.

WHAT IT CHANGES
    idealized_orbits.py: an orbit drawn around another centre than the
      Sun (Sedna) gets no osculating-vs-mean comparison; its hover says
      "not shown" and why. The "both around the Sun" label from
      patch_L431_7 is gone. Orbits drawn around the Sun keep theirs.
    test_orbit_markers.py: the judge and its planted fault for that;
      still twelve planted faults.
    skills/horizons-orbital-mechanics/SKILL.md: 1.4 -> 1.5, the corrected
      bullet; its v1.2 entry to documentation/SKILL_HISTORIES.md.
    PROJECT_INSTRUCTIONS.md: v3.94; v3.91 to
      documentation/PROJECT_INSTRUCTIONS_HISTORY.md. The maintenance run
      then rewrites the Skill Manifest to 1.5.
    LEDGER_CONSOLIDATED.md (L-431, the stamp);
      documentation/WHERE_WE_ARE.md, by section, never below the
      run-record marker; the look-and-fixes handoff, a new section 6.

SAFETY
    Each file is checked only at the lines this patch edits: every anchor
    must match exactly once, and no edit lands below the run-record
    marker, so your notes cannot make it refuse. If any check fails,
    NOTHING is written. A file found with Windows line endings is matched
    after turning them into LF and written back LF, and the patch says
    so. Undo after a run is Discard Changes in GitHub Desktop.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MARKER = '--- Your run record below this line'

EDITS = [
    ('idealized_orbits.py', 'line 53: block says it compares the Sun-centred eleme',
     'block says it compares the Sun-centred elements with the mean ones and\nprints them, so its Delta-a is not read against the drawn a.)\n\nRole: computation\n',
     'block says it compares the Sun-centred elements with the mean ones and\nprints them, so its Delta-a is not read against the drawn a.)\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nTony\'s ruling of the same day: an orbit drawn around another centre than\nthe Sun gets no osculating-vs-mean comparison, only a sentence saying\nwhy; the "both around the Sun" label is gone.)\n\nRole: computation\n'),
    ('idealized_orbits.py', 'line 224: return perturbation_notes.get(obj_name, defa',
     '    return perturbation_notes.get(obj_name, default_note)\ndef get_mean_vs_osculating_assessment(obj_name, osc_params, mean_params, acc=None,\n                                      compared_around=None):\n    """\n    Compare osculating vs mean orbital elements and return perturbation assessment HTML.\n',
     '    return perturbation_notes.get(obj_name, default_note)\ndef get_mean_vs_osculating_assessment(obj_name, osc_params, mean_params, acc=None,\n                                      drawn_around=None):\n    """\n    Compare osculating vs mean orbital elements and return perturbation assessment HTML.\n'),
    ('idealized_orbits.py', 'line 237: osc_params (dict): Current osculating parame',
     "        osc_params (dict): Current osculating parameters (a, e, i, omega, Omega)\n        mean_params (dict): Mean parameters from orbital_elements.py\n        compared_around (str): the centre's words, given when the drawn\n            orbit is around another centre than osc_params (L-431 build 2:\n            Sedna is drawn around the solar system's center of mass, and\n            compared around the Sun, where the mean elements are). The\n            block then names the centre and prints the elements it\n            compared, so its deltas are not read against the drawn ones.\n    \n    Returns:\n",
     '        osc_params (dict): Current osculating parameters (a, e, i, omega, Omega)\n        mean_params (dict): Mean parameters from orbital_elements.py\n        drawn_around (str): the centre\'s words, given when the drawn orbit\n            is around another centre than the Sun (Sedna, around the solar\n            system\'s center of mass). No comparison is printed then, only\n            a sentence saying why (Tony\'s ruling, 2026-10-13). The stored\n            "mean" elements are JPL\'s elements around the Sun at its orbit\n            solution\'s epoch (Sedna\'s, 2018); around the Sun such a body\'s\n            elements move with the Sun\'s own wobble about the center of\n            mass, which the planets cause by pulling on the Sun, so the\n            difference would mostly show that, not a change in the body\'s\n            path.\n    \n    Returns:\n'),
    ('idealized_orbits.py', 'line 253: if not mean_params:',
     '    if not mean_params:\n        return ""\n    \n    osc_e = osc_params.get(\'e\', 0)\n',
     '    if not mean_params:\n        return ""\n    # FIXED (L-431, Tony\'s ruling of 2026-10-13): an orbit drawn around the\n    # solar system\'s center of mass gets no osculating-vs-mean comparison.\n    # The first fix (patch_L431_7) labelled the comparison "both around\n    # the Sun"; that made it clearer but not true, so it is removed.\n    if drawn_around:\n        return ("<br><br><b>Perturbation (osculating vs mean):</b> not shown."\n                f"<br>This orbit is drawn around {drawn_around}."\n                "<br>Compared around the Sun, the difference would mostly show"\n                "<br>the Sun\'s own wobble, not a change in this body\'s path.")\n    \n    osc_e = osc_params.get(\'e\', 0)\n'),
    ('idealized_orbits.py', "line 306: epoch_str = mean_params.get('epoch', 'N/A')",
     '    epoch_str = mean_params.get(\'epoch\', \'N/A\')\n    \n    # FIXED (L-431, after build 2\'s look): when the drawn orbit is around\n    # another centre, say which elements were compared, so "+58.56 AU"\n    # is not read against the drawn a.\n    if compared_around:\n        heading = (f"<br><br><b>Perturbation (osculating vs mean, both around "\n                   f"{compared_around}):</b>"\n                   f"<br>Osculating around {compared_around}: a={_pa.as_given(osc_a)} AU, "\n                   f"e={_pa.as_given(osc_e)}")\n    else:\n        heading = f"<br><br><b>Perturbation (osculating vs mean):</b>"\n    assessment = (\n        f"{heading}"\n        f"<br>Delta-e: {delta_e:+.8f} ({qual_e})"\n        f"{delta_a_text}"\n',
     '    epoch_str = mean_params.get(\'epoch\', \'N/A\')\n    \n    assessment = (\n        f"<br><br><b>Perturbation (osculating vs mean):</b>"\n        f"<br>Delta-e: {delta_e:+.8f} ({qual_e})"\n        f"{delta_a_text}"\n'),
    ('idealized_orbits.py', "line 5485: 'period': {'days': None, 'err_days': None, '",
     "                          'period': {'days': None, 'err_days': None, 'kind': 'none',\n                                     'center': None, 'label': None, 'record': None}}\n            # The mean elements are around the Sun, so the comparison stays\n            # there; when the drawn orbit is not, the comparison says so.\n            _compared_around = 'the Sun' if _orbit['elements'] is not params else None\n            if _orbit['elements'] is not params:\n                params = dict(_orbit['elements'])\n",
     "                          'period': {'days': None, 'err_days': None, 'kind': 'none',\n                                     'center': None, 'label': None, 'record': None}}\n            # An orbit drawn around another centre gets no comparison with the\n            # stored mean elements (Tony's ruling, 2026-10-13).\n            _drawn_around = (_orbit.get('label') or 'another centre') \\\n                if _orbit['elements'] is not params else None\n            if _orbit['elements'] is not params:\n                params = dict(_orbit['elements'])\n"),
    ('idealized_orbits.py', 'line 5870: f"i={_pa.as_given(i)} deg"',
     '                f"i={_pa.as_given(i)} deg"\n                f"{get_planet_perturbation_note(obj_name)}"\n                f"{get_mean_vs_osculating_assessment(obj_name, planetary_params[obj_name], ORIGINAL_planetary_params.get(obj_name, {}), _acc, _compared_around)}"\n            )\n            fig.add_trace(\n',
     '                f"i={_pa.as_given(i)} deg"\n                f"{get_planet_perturbation_note(obj_name)}"\n                f"{get_mean_vs_osculating_assessment(obj_name, planetary_params[obj_name], ORIGINAL_planetary_params.get(obj_name, {}), _acc, _drawn_around)}"\n            )\n            fig.add_trace(\n'),
    ('test_orbit_markers.py', "line 40: the perihelion osculating orbit's hover with",
     "    the perihelion osculating orbit's hover without  DISTANCES WITHOUT THEIR ACCURACY SENTENCE\n      its accuracy sentence\n    Sedna's perturbation block not naming the        PERTURBATION COMPARED WITHOUT ITS CENTRE\n      centre it compared around\n    the plot's frame sized from the Sun-centred      FRAME SIZED FROM ANOTHER ORBIT\n      orbit while Sedna is drawn around the\n",
     "    the perihelion osculating orbit's hover without  DISTANCES WITHOUT THEIR ACCURACY SENTENCE\n      its accuracy sentence\n    Sedna's perturbation block printed while its     PERTURBATION SHOWN FOR A BARYCENTRE ORBIT\n      orbit is drawn around the barycentre\n    the plot's frame sized from the Sun-centred      FRAME SIZED FROM ANOTHER ORBIT\n      orbit while Sedna is drawn around the\n"),
    ('test_orbit_markers.py', "line 86: the drawn orbit. A whole number's trailing z",
     'the drawn orbit. A whole number\'s trailing zeros are no longer called\ncoarse, since its place cannot be read from the print.)\n"""\nimport contextlib\n',
     'the drawn orbit. A whole number\'s trailing zeros are no longer called\ncoarse, since its place cannot be read from the print.)\nModule updated: October 13, 2026 with Anthropic\'s Claude Opus 5.5 (L-431,\nTony\'s ruling of the same day: Sedna\'s perturbation block is not printed\nat all while its orbit is drawn around the barycentre; the judge and its\nplanted fault say so, and Mercury must keep its comparison.)\n"""\nimport contextlib\n'),
    ('test_orbit_markers.py', 'line 115: from celestial_objects import OBJECT_DEFINIT',
     'from celestial_objects import OBJECT_DEFINITIONS\nfrom orbital_elements import parent_planets\nfrom orbital_elements import planetary_params as MEAN_ELEMENTS\n\n# ============================================================================\n',
     'from celestial_objects import OBJECT_DEFINITIONS\nfrom orbital_elements import parent_planets\n\n# ============================================================================\n'),
    ('test_orbit_markers.py', 'line 735: def judge_comparison(fig, findings, counts):',
     '\ndef judge_comparison(fig, findings, counts):\n    """The perturbation block compares the Sun-centred osculating elements\n    with the mean ones, which are around the Sun. Where the drawn orbit is\n    around another centre (Sedna), the block must say so and print the\n    elements it compared, and its Delta-a must be their difference\n    (worked out here); where it is not, it must not claim a centre."""\n    mean_a = MEAN_ELEMENTS[\'Sedna\'][\'a\']\n    for body in (\'Sedna\', \'Mercury\', \'Encke\'):\n        tr = traces(fig, body)\n        info = tr[\'info\'].text[0] if \'info\' in tr else \'\'\n        if \'Perturbation (osculating vs mean\' not in info:\n            continue\n        counts[\'comparisons\'] += 1\n        named = \'both around the Sun\' in info\n        if body != \'Sedna\':\n            if named:\n                findings.append((\'PERTURBATION COMPARED WITHOUT ITS CENTRE\',\n                                 \'%s is drawn around the Sun and its block names a centre\' % body))\n            continue\n        if not named or (\'Osculating around the Sun: a=%r AU\' % SEDNA[\'a\']) not in info:\n            findings.append((\'PERTURBATION COMPARED WITHOUT ITS CENTRE\',\n                             \'Sedna is drawn around the barycentre (a=%r) and its block does not \'\n                             \'say it compares the Sun-centred a=%r\' % (SEDNA_BARY[\'a\'], SEDNA[\'a\'])))\n        m = re.search(r\'Delta-a: \\+?(%s) AU\' % NUM, info)\n        if not m or abs(float(m.group(1)) - (SEDNA[\'a\'] - mean_a)) > 0.01:\n            findings.append((\'PERTURBATION COMPARED WITHOUT ITS CENTRE\',\n                             \'Sedna Delta-a %s is not the Sun-centred a minus the mean a (%.2f)\'\n                             % (m.group(1) if m else \'missing\', SEDNA[\'a\'] - mean_a)))\n\n\n',
     '\ndef judge_comparison(fig, findings, counts):\n    """An orbit drawn around another centre than the Sun (Sedna, around\n    the solar system\'s center of mass) gets no osculating-vs-mean\n    comparison, only a sentence saying why (Tony\'s ruling, 2026-10-13):\n    no Delta line, and the drawn centre named. An orbit drawn around the\n    Sun (Mercury) keeps its comparison."""\n    for body, drawn_around in ((\'Sedna\', "the solar system\'s center of mass"),\n                               (\'Mercury\', None)):\n        tr = traces(fig, body)\n        info = tr[\'info\'].text[0] if \'info\' in tr else \'\'\n        counts[\'comparisons\'] += 1\n        deltas = re.findall(r\'Delta-[aeiq]:\', info)\n        if drawn_around:\n            if deltas or \'not shown\' not in info or drawn_around not in info:\n                findings.append((\'PERTURBATION SHOWN FOR A BARYCENTRE ORBIT\',\n                                 \'%s is drawn around %s and its hover prints %s\'\n                                 % (body, drawn_around, \', \'.join(deltas) or\n                                    \'no sentence saying why the comparison is not shown\')))\n        elif not deltas:\n            findings.append((\'PERTURBATION SHOWN FOR A BARYCENTRE ORBIT\',\n                             \'%s is drawn around the Sun and lost its comparison\' % body))\n\n\n'),
    ('test_orbit_markers.py', 'line 901: (\'idealized_orbits\', "        f\\"{_accuracy_',
     '     (\'idealized_orbits\', "        f\\"{_accuracy_tail(_pa.accuracy_for(obj_name, \'Sun\'))}\\"\\n", ""),\n     \'DISTANCES WITHOUT THEIR ACCURACY SENTENCE\'),\n    ("Sedna\'s perturbation block not naming the centre it compared around",\n     (\'idealized_orbits\', "_acc, _compared_around)}\\"", "_acc)}\\""),\n     \'PERTURBATION COMPARED WITHOUT ITS CENTRE\'),\n    ("the frame sized from the Sun-centred orbit",\n     (\'palomas_orrery\', "                        aphelion = _drawn_far\\n",\n',
     '     (\'idealized_orbits\', "        f\\"{_accuracy_tail(_pa.accuracy_for(obj_name, \'Sun\'))}\\"\\n", ""),\n     \'DISTANCES WITHOUT THEIR ACCURACY SENTENCE\'),\n    ("Sedna\'s perturbation block printed while drawn around the barycentre",\n     (\'idealized_orbits\', "_acc, _drawn_around)}\\"", "_acc)}\\""),\n     \'PERTURBATION SHOWN FOR A BARYCENTRE ORBIT\'),\n    ("the frame sized from the Sun-centred orbit",\n     (\'palomas_orrery\', "                        aphelion = _drawn_far\\n",\n'),
    ('test_orbit_markers.py', "line 968: 'year on against the drawn elements\\' period",
     "          'year on against the drawn elements\\' period; a pre-build-2 record\\'s drawing '\n          'and dates; the parameters window\\'s apsis dates against Earth\\'s own period; '\n          'the Moon\\'s arc against its fetched period; Sedna\\'s perturbation block against '\n          'the Sun-centred a minus the mean a; Encke\\'s perihelion osculating orbit against the '\n          'whole-kilometer floor and its sentence; the frame against Sedna\\'s drawn far end; '\n          'and the dispatch in palomas_orrery.py')\n",
     "          'year on against the drawn elements\\' period; a pre-build-2 record\\'s drawing '\n          'and dates; the parameters window\\'s apsis dates against Earth\\'s own period; '\n          'the Moon\\'s arc against its fetched period; Sedna\\'s orbit hover for no perturbation '\n          'block (drawn around the barycentre) and Mercury\\'s for one; Encke\\'s perihelion osculating orbit against the '\n          'whole-kilometer floor and its sentence; the frame against Sedna\\'s drawn far end; '\n          'and the dispatch in palomas_orrery.py')\n"),
    ('test_orbit_markers.py', "line 983: 'drawn points on their period\\'s centre; %d ",
     "          'drawn points on their period\\'s centre; %d markers, %d dates, %d printed distances '\n          'against their errors; %d elements as given; %d Keplerian positions half a year '\n          'on; %d parameters-window date pairs; %d Moon arcs; %d perturbation blocks; '\n          '%d perihelion osculating orbits; %d frames; %d sources read'\n          % (len(PLANTS), len(PLANTS), counts['bodies'], counts['points'], counts['markers'],\n",
     "          'drawn points on their period\\'s centre; %d markers, %d dates, %d printed distances '\n          'against their errors; %d elements as given; %d Keplerian positions half a year '\n          'on; %d parameters-window date pairs; %d Moon arcs; %d perturbation checks; '\n          '%d perihelion osculating orbits; %d frames; %d sources read'\n          % (len(PLANTS), len(PLANTS), counts['bodies'], counts['points'], counts['markers'],\n"),
    ('skills/horizons-orbital-mechanics/SKILL.md', 'line 9: Skill version: 1.5 | 2026-10-13, with Anthro',
     "Skill version: 1.4 | 2026-10-12, with Anthropic's Claude Opus 5.5, at\n",
     "Skill version: 1.5 | 2026-10-13, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 400a9615. v1.5 (L-431) corrects one bullet of 1.4, by\nTony's ruling of 2026-10-13: an orbit drawn around the solar system's\nbarycentre gets no comparison with the stored mean elements. 1.4 said\nthe comparison stays Sun-centred; for a body as far out as Sedna that\nmostly measures the Sun's own wobble. A second version in one session, as interactive-exhibit 1.14\nwas, because the ruling came after 1.4 was installed.\nEarlier: 1.4 | 2026-10-12, with Anthropic's Claude Opus 5.5, at\n"),
    ('skills/horizons-orbital-mechanics/SKILL.md', 'line 32: ',
     "Earlier: 1.2 | 2026-10-10, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 32619f8d and gallery @ a7d1a542. v1.2 (L-395) adds\nChecking an Entry Against JPL, what the Horizons check's build learned:\nJPL's Lookup cannot see record numbers; a bare number also finds\nasteroids and spacecraft, so an entry is found in three steps; JPL\nre-solves a record in place; and a recent comet's record number can be\ngiven to another comet. It corrects two lines under Small-Body Record\nPinning: Encke's pin now lives in the orrery's list, and what a pin\ndoes not follow is a NEWER record, not a new solution.\n",
     ''),
    ('skills/horizons-orbital-mechanics/SKILL.md', 'line 33: on 2026-10-12 and 2026-10-13 (L-431).',
     'on 2026-10-12 (L-431).\n',
     'on 2026-10-12 and 2026-10-13 (L-431).\n'),
    ('skills/horizons-orbital-mechanics/SKILL.md', 'line 167: - An orbit drawn around the barycentre gets ',
     "- Comparing the osculating orbit with JPL's mean elements keeps the\n  Sun-centred elements, because the mean elements are Sun-centred: a\n  barycentre ellipse against them reports a perturbation that is only\n  the change of centre.\n",
     '- An orbit drawn around the barycentre gets no comparison with the\n  stored "mean" elements; the hover says why in one sentence (Tony\'s\n  ruling, 2026-10-13). Around the Sun, a body this far out has elements\n  that move with the Sun\'s own wobble about the barycentre, which the\n  planets cause by pulling on the Sun (Sedna\'s period around the Sun\n  moved 370 years in one year). The stored "mean" elements are JPL\'s\n  elements around the Sun at the orbit solution\'s epoch, not means:\n  Sedna\'s are at 2018 (a = 481 au; its `epoch` field holds the date\n  Tony downloaded them, 2025). Against today\'s Sun-centred a of 540 au\n  the difference mostly shows the wobble, not a change in Sedna\'s path.\n  An orbit drawn around the Sun keeps its comparison. (1.4 said the\n  comparison stays Sun-centred; a label saying so was built and then\n  removed the same day.)\n'),
    ('PROJECT_INSTRUCTIONS.md', 'line 3: Tony Quintanilla, PE | Claude | v3.94 | Octo',
     'Tony Quintanilla, PE | Claude | v3.93 | October 12, 2026\n',
     'Tony Quintanilla, PE | Claude | v3.94 | October 13, 2026\n'),
    ('PROJECT_INSTRUCTIONS.md', 'line 5: Cut from 400a9615 at https://github.com/tony',
     'Cut from c9722520 at https://github.com/tonylquintanilla/palomas_orrery\n',
     'Cut from 400a9615 at https://github.com/tonylquintanilla/palomas_orrery\n'),
    ('PROJECT_INSTRUCTIONS.md', 'line 1170: v3.94 (October 13, 2026): No rule changed in',
     '\nv3.93 (October 12, 2026): No rule changed in this document. ONE\n',
     '\nv3.94 (October 13, 2026): No rule changed in this document. ONE\nskill bump, one version (L-431): horizons-orbital-mechanics 1.4 -> 1.5.\nNO PERTURBATION LINES FOR AN ORBIT DRAWN AROUND THE BARYCENTRE.\n\nWHAT PROMPTED IT. Tony\'s look at L-431\'s second build was accepted; his\nsaved plot showed Sedna\'s orbit hover comparing its orbit around the\nSun with a stored "mean" orbit, beneath elements drawn around the\nbarycentre. The first fix labelled the comparison "both around the\nSun". Tony asked why, when Sedna is worked out around the barycentre.\nFor a body that far out the orbit around the Sun moves with the Sun\'s\nown wobble about the barycentre. Sedna\'s stored elements are JPL\'s\naround the Sun at its 2018 solution epoch (Tony\'s Horizons file showed\nthe centre and the epoch), so the difference from today\'s mostly shows\nthat wobble, not a change in Sedna\'s path.\nHis ruling, 2026-10-13: remove the lines for orbits drawn around the\nbarycentre.\n\nWHAT CHANGED. horizons-orbital-mechanics 1.5 replaces 1.4\'s bullet\n"the comparison with mean elements stays Sun-centred" with the ruling.\nA second version in one session, as interactive-exhibit 1.14 was,\nbecause the ruling came after 1.4 was installed. Its v1.2 entry moved\nto documentation/SKILL_HISTORIES.md, by the three-entry rule.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nhorizons-orbital-mechanics 1.5 before Horizons work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.91 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\nv3.93 (October 12, 2026): No rule changed in this document. ONE\n'),
    ('PROJECT_INSTRUCTIONS.md', 'line 1262: ',
     'v3.91 (October 11, 2026): No rule changed in this document. ONE\nskill bump, one version (L-351, L-421): ledger-and-session-records\n1.19 -> 1.20. YOUR TWO FOLDERS IN EVERY HEADER.\n\nWHAT PROMPTED IT. Tony, in his run record of 2026-10-10: "since we\nare using cowork, the location of the local files should be included\nin the handoff header along with the github info." 1.19 named the\nfolders under Where a File Goes; a session reading a brief cold did\nnot see them there. The brief for the inner Oort cloud\'s website half\ncarried them in its header, and its session saved both patches where\nTony runs them. Tony asked for this version at that session\'s close,\none version only.\n\nWHAT CHANGED. ledger-and-session-records, under Anchor Requirement,\nHandoff Structure and Tony\'s Local Folders: every handoff, brief and\ndesign record names both folders beside the GitHub line. Its v1.17\nentry moved to documentation/SKILL_HISTORIES.md, by the three-entry\nrule.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nledger-and-session-records 1.20 before ledger or handoff work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.88 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n',
     ''),
    ('documentation/PROJECT_INSTRUCTIONS_HISTORY.md', 'line 2642: v3.91 (October 11, 2026): No rule changed in',
     'v3.93 made a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n',
     'v3.93 made a fourth entry.)\n\nv3.91 (October 11, 2026): No rule changed in this document. ONE\nskill bump, one version (L-351, L-421): ledger-and-session-records\n1.19 -> 1.20. YOUR TWO FOLDERS IN EVERY HEADER.\n\nWHAT PROMPTED IT. Tony, in his run record of 2026-10-10: "since we\nare using cowork, the location of the local files should be included\nin the handoff header along with the github info." 1.19 named the\nfolders under Where a File Goes; a session reading a brief cold did\nnot see them there. The brief for the inner Oort cloud\'s website half\ncarried them in its header, and its session saved both patches where\nTony runs them. Tony asked for this version at that session\'s close,\none version only.\n\nWHAT CHANGED. ledger-and-session-records, under Anchor Requirement,\nHandoff Structure and Tony\'s Local Folders: every handoff, brief and\ndesign record names both folders beside the GitHub line. Its v1.17\nentry moved to documentation/SKILL_HISTORIES.md, by the three-entry\nrule.\n\nTHE OBLIGATION TRAVELS. A reinstall during a session is not visible to\nthat session. The next session confirms its loaded copy reads\nledger-and-session-records 1.20 before ledger or handoff work.\n\nThe header stamp and the SHA anchor move with this entry.\n\nVersion history: v3.88 moves down to\ndocumentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\nresident.\n\n(Moved down from the resident protocol on 2026-10-13 when\nv3.94 made a fourth entry.)\n\n================================================================\nPART 2 -- LESSONS REMOVED FROM THE PROTOCOL AT v3.37\n'),
    ('documentation/SKILL_HISTORIES.md', "line 738: Earlier: 1.2 | 2026-10-10, with Anthropic's ",
     '\nEarlier: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12\n',
     "\nEarlier: 1.2 | 2026-10-10, with Anthropic's Claude Opus 5.5, at\npalomas_orrery @ 32619f8d and gallery @ a7d1a542. v1.2 (L-395) adds\nChecking an Entry Against JPL, what the Horizons check's build learned:\nJPL's Lookup cannot see record numbers; a bare number also finds\nasteroids and spacecraft, so an entry is found in three steps; JPL\nre-solves a record in place; and a recent comet's record number can be\ngiven to another comet. It corrects two lines under Small-Body Record\nPinning: Encke's pin now lives in the orrery's list, and what a pin\ndoes not follow is a NEWER record, not a new solution.\n(Moved down 2026-10-13, when 1.5 made a fourth entry.)\n\nEarlier: 1.1 | Cut from palomas_orrery @ e83fe9ce | 2026-07-12\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 378: Module updated: October 13, 2026 with Anthro',
     'three findings read from his saved plot fixed), built on 87a54704.\nReview and RICE update Tony 6-21-2026\n',
     "three findings read from his saved plot fixed), built on 87a54704.\nModule updated: October 13, 2026 with Anthropic's Claude Opus 5.5\n(L-431: Tony's ruling, no perturbation lines for an orbit drawn around\nthe barycentre; horizons-orbital-mechanics 1.5, protocol v3.94), built\non 400a9615.\nReview and RICE update Tony 6-21-2026\n"),
    ('LEDGER_CONSOLIDATED.md', 'line 1726: and prints the elements it compared. SUPERSE',
     '    and prints the elements it compared.\n',
     '    and prints the elements it compared. SUPERSEDED the same day, below.\n'),
    ('LEDGER_CONSOLIDATED.md', "line 1731: - **2026-10-13, Tony's ruling on the perturb",
     "    (`orbital_period.drawn_aphelion_distance`): 1,030 au.\n**Gap:** three builds, in order (the record's section 3):\n",
     '    (`orbital_period.drawn_aphelion_distance`): 1,030 au.\n- **2026-10-13, Tony\'s ruling on the perturbation lines** (in chat,\n  after patch_L431_7 ran and was pushed at 400a9615). He asked why\n  Sedna\'s comparison was around the Sun when Sedna is worked out\n  around the barycentre. Claude first told him the stored "mean"\n  elements had no recorded centre and a mismatched date; Tony corrected\n  that with the Horizons file they came from\n  (`horizons_results_sedna.txt`, uploaded in chat): "2018 is the epoch of\n  the mean elements. 2025 is when i downloaded the ephemeris." Its\n  header reads "IAU76/J2000 helio. ecliptic osc. elements", EPOCH\n  2018-Oct-20 in JPL\'s current solution (the stored set, 2018-May-16,\n  is from an earlier one). So both sides were around the Sun, eight\n  years apart: a = 481 au then, 540 au now. Around the Sun, Sedna\'s\n  elements move with the Sun\'s own wobble about the barycentre, which\n  the planets cause by pulling on the Sun (its period around the Sun\n  moved 370 years in one year), so the "+58.56 AU (12.2%)" mostly\n  showed that wobble, not a change in Sedna\'s path. Tony: remove the\n  lines for orbits drawn around the barycentre. `patch_L431_8_no_bary_perturbation_20261013.py`\n  does: the hover says "not shown" and why; Mercury and every orbit\n  drawn around the Sun keep theirs. The checker\'s planted fault now\n  prints the block for Sedna. horizons-orbital-mechanics 1.5 replaces\n  1.4\'s "the comparison stays Sun-centred"; protocol v3.94.\n- **Found, recorded and not chased (The Braid):** the stored "mean"\n  elements in `orbital_elements.py` are JPL\'s elements around the Sun at\n  each orbit solution\'s epoch, not means; their `epoch` field holds the\n  date they were downloaded, and their centre is not written beside\n  them. The comparison still runs for every orbit drawn around the Sun.\n  One class: what the word "mean" and the epoch field should say.\n**Gap:** three builds, in order (the record\'s section 3):\n'),
    ('LEDGER_CONSOLIDATED.md', 'line 1765: patch_L431_7 (run, pushed at 400a9615); the ',
     '   patch_L431_7, which waits for his run.\n',
     '   patch_L431_7 (run, pushed at 400a9615); the perturbation lines are\n   removed for barycentre orbits in patch_L431_8, which waits for his run.\n'),
    ('documentation/WHERE_WE_ARE.md', 'line 4: Last updated: October 13, 2026, afternoon: n',
     'Last updated: October 13, 2026: L-431 build 2 accepted at your look; three fixes.\n- Written at orrery 87a54704 and gallery 924977a3.\n',
     'Last updated: October 13, 2026, afternoon: no perturbation lines for Sedna.\n- Written at orrery 400a9615 and gallery 924977a3.\n'),
    ('documentation/WHERE_WE_ARE.md', "line 12: > - Fixes from your saved plot: Encke's whit",
     '> - Three fixes from your saved plot: Encke\'s white arc\'s accuracy line;\n>   Sedna\'s perturbation lines say "around the Sun"; the frame fits\n>   Sedna\'s drawn orbit (1,030 au, not 1,104).\n',
     "> - Fixes from your saved plot: Encke's white arc's accuracy line; the\n>   frame fits Sedna (1,030 au, not 1,104); by your ruling, no\n>   perturbation lines for orbits drawn around the barycentre.\n"),
    ('documentation/WHERE_WE_ARE.md', 'line 20: > - *Run patch_L431_8 and the maintenance ru',
     '> - *Run patch_L431_7 and the maintenance run (25 of 25, Orbit markers\n>   12 of 12); move the patch into documentation/; push. No look\n>   needed.*\n',
     "> - *Run patch_L431_8 and the maintenance run (25 of 25); reinstall\n>   horizons-orbital-mechanics 1.5; the Project's instructions to\n>   v3.94; move both patches into documentation/; push.*\n"),
    ('documentation/HANDOFF_L431_build2_look_fixes_20261013.md', 'line 115: [Superseded by section 6: patch_L431_8 bumps',
     '(this session loaded 1.3, and was the one that bumped it).\n',
     '(this session loaded 1.3, and was the one that bumped it).\n[Superseded by section 6: patch_L431_8 bumps it to 1.5.]\n\n## 6. Afterwards: no perturbation lines for a barycentre orbit\n\nAdded by `patch_L431_8_no_bary_perturbation_20261013.py`, built on\n400a9615 (patch_L431_7 run and pushed).\n\nTony read fix 2 above and asked why Sedna\'s comparison was around the\nSun, when Sedna is worked out around the barycentre. The answer\nchanged the fix:\n- The stored "mean" elements (`orbital_elements.py`) are JPL\'s\n  elements around the Sun at the orbit solution\'s epoch. Claude first\n  said their centre was never recorded and their dates disagreed; Tony\n  corrected it with the Horizons file they came from: "2018 is the\n  epoch of the mean elements. 2025 is when i downloaded the\n  ephemeris." The file\'s header reads "helio. ecliptic osc. elements",\n  epoch 2018. So both sides of the comparison are around the Sun,\n  eight years apart: a = 481 au then, 540 au now.\n- Around the Sun, a body as far out as Sedna has elements that move\n  with the Sun\'s own wobble about the barycentre, which the planets\n  cause by pulling on the Sun: its period around the Sun moved 370\n  years in one year (horizons-orbital-mechanics, A Period Depends on\n  Its Centre). So "+58.56 AU (12.2%)" was mostly that wobble, not a\n  change in Sedna\'s path.\n\nTony\'s ruling, 2026-10-13: remove the lines for orbits drawn around the\nbarycentre. Now Sedna\'s orbit hover reads "Perturbation (osculating vs\nmean): not shown.", names the centre it is drawn around, and says the\ncomparison around the Sun would mostly show the Sun\'s own wobble, not a\nchange in this body\'s path.\nMercury and every other orbit drawn around the Sun keep their\ncomparison (Encke has no stored elements to compare with). The "both\naround the Sun" label is gone.\n\nThe checker\'s planted fault for this now prints the block for Sedna and\nmust be caught as PERTURBATION SHOWN FOR A BARYCENTRE ORBIT; it also\nfails if Mercury loses its comparison. Still twelve planted faults.\n\nhorizons-orbital-mechanics 1.4 said the comparison stays Sun-centred.\nThat would lead a session to rebuild the misleading lines, so 1.5\ncorrects it, a second version in one session (the ruling came after\n1.4 was installed), with protocol v3.94. The next session confirms its\nloaded copy reads 1.5 before Horizons work.\n\nRecorded, not chased: the stored "mean" elements are JPL\'s\nsolution-epoch elements around the Sun, and their `epoch` field holds\nthe download date; what "mean" and that field should say is one class\non L-431.\n\nFor Tony:\n- (do) Run `patch_L431_8_no_bary_perturbation_20261013.py` (VS Code,\n  Run), then `orrery_maintenance_run.py`: 25 of 25, Orbit markers 12 of\n  12; it also rewrites the Skill Manifest to 1.5.\n- (do) Reinstall horizons-orbital-mechanics 1.5 (Settings > Skills);\n  copy PROJECT_INSTRUCTIONS.md (v3.94) to the Project\'s instructions and\n  to `documentation/project_instructions_v3_94.md`.\n- (do) Move patch_L431_7 and patch_L431_8 into `documentation/`; commit\n  and push.\n'),
]



def apply():
    texts, crlf, done = {}, set(), []
    for f, label, old, new in EDITS:
        path = os.path.join(ROOT, f)
        if f not in texts:
            if not os.path.exists(path):
                print('ERROR: %s not found in %s. NOTHING was written.' % (f, ROOT))
                return None
            raw = open(path, 'rb').read()
            if b'\r\n' in raw:
                crlf.add(f)
            texts[f] = raw.replace(b'\r\n', b'\n').decode('utf-8')
        t = texts[f]
        n = t.count(old)
        if n != 1:
            print('ANCHOR FAIL  %-45s %s (found %d times, expected 1). NOTHING was written.'
                  % (f, label, n))
            if n == 0 and 'drawn_around' in texts.get('idealized_orbits.py', ''):
                print('It looks as though this patch has already run.')
            return None
        if MARKER in t and t.index(old) > t.index(MARKER):
            print('ANCHOR FAIL  %-45s %s lies below the run-record marker. NOTHING was written.'
                  % (f, label))
            return None
        texts[f] = t.replace(old, new)
        done.append((f, label))
    for f, label, old, new in EDITS:
        if any(ord(c) > 127 for c in new):
            print('ERROR: an edit to %s would add non-ASCII. NOTHING was written.' % f)
            return None
    for f, t in texts.items():
        with open(os.path.join(ROOT, f), 'w', encoding='utf-8', newline='') as h:
            h.write(t)
    for f, label in done:
        print('ok  %-45s %s' % (f, label))
    for f in sorted(crlf):
        print('note: %s was CRLF in the working copy; written LF' % f)
    print()
    print('patch applied (%d edits in %d files)' % (len(done), len(texts)))
    print('Stamps updated: idealized_orbits.py, test_orbit_markers.py, the skill\'s version')
    print('line, the protocol\'s header, the ledger.')
    print()
    print('What changed in the plot: Sedna\'s orbit hover now reads')
    print('  "Perturbation (osculating vs mean): not shown."')
    print('  "This orbit is drawn around the solar system\'s center of mass."')
    print('  "Compared around the Sun, the difference would mostly show"')
    print('  "the Sun\'s own wobble, not the pull of the planets."')
    print('Mercury and every orbit drawn around the Sun keep their comparison.')
    return True


def main():
    if not apply():
        return 1
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py: expect 25 of 25 gating checkers, "Orbit markers"')
    print('     with 12 of 12 planted faults, and "0 TIER-1 -- the push gate holds". It also')
    print('     rewrites the Skill Manifest to horizons-orbital-mechanics 1.5.')
    print('  2. Reinstall horizons-orbital-mechanics 1.5 (Settings > Skills); copy')
    print('     PROJECT_INSTRUCTIONS.md (v3.94) to the Project\'s instructions and to')
    print('     documentation/project_instructions_v3_94.md.')
    print('  3. Move this script, patch_L431_7_look_fixes_20261013.py and')
    print('     patch_L436_1_idea_20261013.py into documentation/; commit and push.')
    print('     The maintenance run will say "Tier-1 rose" in patch_L436_1 while it sits in')
    print('     the root folder (281 in the whole tree); filed in documentation/, it is 280.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
