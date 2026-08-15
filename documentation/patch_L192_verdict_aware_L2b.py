"""Teach L2b the difference between a fix and a defect.

Before this patch the checker compared the code value against the
worksheet's code-value cell and called any difference DRIFTED. It read
the worksheet's verdict three lines later and never used it here, so a
value that moved because the worksheet FOUND AN ERROR was reported the
same way as one that walked away from a confirmed number.

After it, L2b has three outcomes:

  DRIFTED         the worksheet confirmed that value and the code left
                  it anyway -- the only defect of the three
  CORRECTED       the worksheet refuted it and the code moved
  UNCHECKED_MOVE  no value verdict exists, so neither word is honest

On the live corpus all eight L2b findings become UNCHECKED_MOVE, not
CORRECTED. Their worksheets carry only a 'Citation correct?' column,
and a NO there routinely means 'wrong authority, value correct' -- see
rows G4, G6, G7 and G8. Nobody ever answered the value question in a
place a tool can read, and the tool now says that instead of guessing.

Two files, five hunks. Every hunk asserts EXACTLY ONE match before
anything is written, and all of them are planned before any of them is
written, so a drifted file cannot leave a half-patched tree behind.
Re-running is safe: an already-patched file reports 'already'.

Run it from the repo root with the Run button.

Written August 2026 with Anthropic's Claude Opus 5 (L-192).
"""

import hashlib
import os
import sys


def normalized(path):
    with open(path, 'rb') as handle:
        return handle.read().replace(b'\r\n', b'\n')


HUNKS = [
    ('worksheet_checker.py',
     ('    a wrong authority is value-YES and citation-NO, and calling that a\n'
      '    refuted value misclassifies in both directions.\n'
      '    """\n'
      '    tag = quoted(token)\n'
      '    if own in VERDICT_CLEARS:\n'
      '        return True\n'
      '    if own == V_INCOMPLETE:\n'
      '        # PARTIAL and APPROX return to the originator unconditionally,\n'
      '        # without first asking why the row is qualified.\n'),
     ('    a wrong authority is value-YES and citation-NO, and calling that a\n'
      '    refuted value misclassifies in both directions.\n'
      '    """\n'
      '    tag = quoted(token)\n'
      '\n'
      '    # A pass with a reservation is not a pass. This is the ONE branch\n'
      '    # that returns without recording anything, so it is the only place\n'
      '    # a qualification actually vanishes -- every other class below\n'
      '    # already quotes the whole cell into its finding. Fifteen of this\n'
      "    # corpus's sixty-one compound cells qualify a YES, and each of\n"
      '    # them reads as clean today.\n'
      '    if own in VERDICT_CLEARS:\n'
      '        if is_compound(token):\n'
      "            claim.fail('L3', 'QUALIFIED_PASS',\n"
      "                       '%s reads %s -- confirmed with a reservation%s'\n"
      "                       % (where, tag, extra), '')\n"
      '        return True\n'
      '    if own == V_INCOMPLETE:\n'
      '        # PARTIAL and APPROX return to the originator unconditionally,\n'
      '        # without first asking why the row is qualified.\n')),
    ('worksheet_checker.py',
     ("        claim.fail('L3', 'CITATION_DEFECT',\n"
      "                   '%s reads %s -- the cited source does not publish '\n"
      "                   'it%s' % (where, tag, extra), 'CONVERSATION')\n"
      '    elif own == V_REFUTED:\n'
      '        if scope == SCOPE_CITATION:\n'
      "            claim.fail('L3', 'CITATION_DEFECT',\n"
      "                       '%s reads %s -- wrong authority for a value that '\n"
      "                       'may still be right%s' % (where, tag, extra),\n"
      "                       'CONVERSATION')\n"),
     ("        claim.fail('L3', 'CITATION_DEFECT',\n"
      "                   '%s reads %s -- the cited source does not publish '\n"
      "                   'it%s' % (where, tag, extra), 'CONVERSATION')\n"
      '    elif own == V_REFUTED:\n'
      '        if scope == SCOPE_CITATION and is_compound(token):\n'
      '            # The column asks whether the citation is right. A bare NO\n'
      '            # answers that question and nothing else. A NO carrying its\n'
      '            # own reason may answer a different one: in this corpus\n'
      '            # "NO -- wrong authority" means the value is fine and the\n'
      '            # source is not, while "NO -- arithmetic error" means the\n'
      '            # source is fine and the value is not. Same token, same\n'
      '            # column, opposite meanings.\n'
      '            #\n'
      '            # So the qualification decides whether this tool may say\n'
      '            # which kind of refusal it is, and it never reads the\n'
      '            # qualification to decide what it says -- that would be a\n'
      '            # prose-parsed convention, which is the failure class this\n'
      '            # project keeps meeting. It states the quote and stops.\n'
      "            claim.fail('L3', 'REFUSAL_UNCLASSIFIED',\n"
      "                       '%s reads %s -- a refusal qualified beyond what '\n"
      "                       'the column asks; whether the citation or the '\n"
      "                       'value is at fault is not decidable here%s'\n"
      "                       % (where, tag, extra), 'CONVERSATION')\n"
      '        elif scope == SCOPE_CITATION:\n'
      "            claim.fail('L3', 'CITATION_DEFECT',\n"
      "                       '%s reads %s -- wrong authority for a value that '\n"
      "                       'may still be right%s' % (where, tag, extra),\n"
      "                       'CONVERSATION')\n")),
    ('worksheet_checker.py',
     ('DISPLAY_INSTRUCTION_RE = re.compile(\n'
      "    r'(?i)manual scale|manual scaled|mb per frame|to visualize|'\n"
      "    r'to view closely|frame for html')\n"
      '\n'
      '# Tight and directional on purpose. The instruction phrase sits right\n'
      '# against its own number -- "MANUAL SCALE OF 0.005 AU", "4.6 MB PER\n'
      '# FRAME" -- so a wide window reaches across the paragraph break and\n'
      '# swallows the science claim that follows it.\n'),
     ('DISPLAY_INSTRUCTION_RE = re.compile(\n'
      "    r'(?i)manual scale|manual scaled|mb per frame|to visualize|'\n"
      "    r'to view closely|frame for html')\n"
      '\n'
      '# FROZEN by Tony 2026-08-14 and pinned. Measured over the L-192\n'
      '# corpus, the drop set is identical for lookback 25 through 60 at\n'
      '# every lookahead tested; 30 sits mid-plateau. These values decide\n'
      '# which numbers count as claims, and the ::cN ordinal in every\n'
      '# issued key counts claims AFTER this filter runs -- so retuning\n'
      '# either one re-points ordinals corpus-wide with no prose edit at\n'
      '# all. test_extractor_pins.py asserts them against\n'
      '# documentation/worksheets/L192_extractor_pins.txt on every run.\n'
      '#\n'
      '# Tight and directional on purpose. The instruction phrase sits right\n'
      '# against its own number -- "MANUAL SCALE OF 0.005 AU", "4.6 MB PER\n'
      '# FRAME" -- so a wide window reaches across the paragraph break and\n'
      '# swallows the science claim that follows it.\n')),
    ('worksheet_checker.py',
     ("            claim.fail('L2a', 'RANGE', 'evidence is a range: %s' % detail, '')\n"
      "        elif verdict == 'CONVERSION':\n"
      "            claim.fail('L2a', 'MATCHED_VIA_CONVERSION', detail, '')\n"
      '\n'
      '    # ---- L2b: drift since the check ----------------------------------\n'
      '    #\n'
      "    # The code-value cell is what the checker read at the prompt's SHA.\n"
      '    # Comparing it to the code NOW is the committed-history failure\n'
      '    # caught directly rather than inferred. It exists only where the\n'
      '    # schema carries the column, and the coverage count says so.\n'
      '    recorded = table.cell(cells, ROLE_CODE)\n'
      '    if claim.code_value is not None and recorded:\n'
      '        verdict, detail = compare(claim.code_value, recorded)\n'
      "        if verdict == 'MISMATCH':\n"
      "            claim.fail('L2b', 'DRIFTED',\n"
      "                       'code now %s, checker read %s'\n"
      "                       % (claim.unit.value_str, detail), 'CONVERSATION')\n"
      '\n'
      '    # ---- L3: the verdict is read -------------------------------------\n'
      '    own, token, scope, column = read_verdict(table, cells)\n'
      '    claim.verdict_column = column\n'
      '    if own is None:\n'
      "        claim.fail('L3', 'NO_VERDICT_COLUMN',\n"
      "                   'the matched table records no verdict', 'SEND BACK')\n"),
     ("            claim.fail('L2a', 'RANGE', 'evidence is a range: %s' % detail, '')\n"
      "        elif verdict == 'CONVERSION':\n"
      "            claim.fail('L2a', 'MATCHED_VIA_CONVERSION', detail, '')\n"
      '\n'
      '    # ---- The verdict, read once --------------------------------------\n'
      '    #\n'
      '    # Read here rather than at L3 because L2b needs it, and reused\n'
      '    # below so there is still exactly one read.\n'
      '    own, token, scope, column = read_verdict(table, cells)\n'
      '\n'
      '    # ---- L2b: drift since the check ----------------------------------\n'
      '    #\n'
      "    # The code-value cell is what the checker read at the prompt's SHA.\n"
      '    # Comparing it to the code NOW is the committed-history failure\n'
      '    # caught directly rather than inferred. It exists only where the\n'
      '    # schema carries the column, and the coverage count says so.\n'
      '    #\n'
      '    # THREE outcomes, not two. A value that moved away from a number\n'
      '    # the worksheet REJECTED is the correction landing -- this whole\n'
      '    # apparatus working -- and reporting it as drift tells a reader to\n'
      '    # go re-check a resolution the code already records. All eight L2b\n'
      '    # findings in the L-192 report were that shape. The information\n'
      '    # needed to tell them apart was already in the matched row, three\n'
      '    # lines further down, and was simply read too late.\n'
      '    #\n'
      '    #   DRIFTED         the worksheet confirmed that value; the code\n'
      '    #                   left it anyway. The only defect of the three.\n'
      '    #   CORRECTED       the worksheet refuted it and the code moved.\n'
      '    #                   Recorded, not routed.\n'
      '    #   UNCHECKED_MOVE  the worksheet neither confirmed nor refuted it,\n'
      '    #                   so neither word is honest. Routed, because\n'
      '    #                   nobody has established anything.\n'
      '    recorded = table.cell(cells, ROLE_CODE)\n'
      '    if claim.code_value is not None and recorded:\n'
      '        verdict, detail = compare(claim.code_value, recorded)\n'
      "        if verdict == 'MISMATCH':\n"
      "            moved = ('code now %s, checker read %s'\n"
      '                     % (claim.unit.value_str, detail))\n'
      "            if column == 'citation-only':\n"
      "                claim.fail('L2b', 'UNCHECKED_MOVE',\n"
      "                           '%s; this worksheet carries no value verdict'\n"
      "                           % moved, 'CONVERSATION')\n"
      '            elif own == V_REFUTED:\n'
      "                claim.fail('L2b', 'CORRECTED',\n"
      "                           '%s, which it rejected: %s' % (moved, token), '')\n"
      '            elif own in (V_CONFIRMED, V_INCOMPLETE):\n'
      "                claim.fail('L2b', 'DRIFTED', moved, 'CONVERSATION')\n"
      '            else:\n'
      "                claim.fail('L2b', 'UNCHECKED_MOVE',\n"
      "                           '%s; the verdict on that value was %s'\n"
      "                           % (moved, own), 'CONVERSATION')\n"
      '\n'
      '    # ---- L3: the verdict is used -------------------------------------\n'
      '    claim.verdict_column = column\n'
      '    if own is None:\n'
      "        claim.fail('L3', 'NO_VERDICT_COLUMN',\n"
      "                   'the matched table records no verdict', 'SEND BACK')\n")),
    ('test_worksheet_checker.py',
     ('""")\n'
      "    check('L2b fails when the code moved since the check',\n"
      "          'DRIFTED' in codes(claim), codes(claim))\n"
      '\n'
      '    # L3 -- the Oort shape: an annotation asserting a completed check\n'
      '    # over a row that records the check as not performed.\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Code value | Your value | Value correct? |\n'),
     ('""")\n'
      "    check('L2b fails when the code moved since the check',\n"
      "          'DRIFTED' in codes(claim), codes(claim))\n"
      '\n'
      '    # L2b, the other two outcomes. DRIFTED above earns its name only\n'
      "    # because that row's verdict is YES: the worksheet confirmed 137.5\n"
      '    # and the code left it anyway. Change the verdict and the same\n'
      '    # movement means something else entirely.\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Code value | Your value | Value correct? |\n'
      '|---|---|---|---|---|\n'
      '| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **NO -- does not follow** |\n'
      '""")\n'
      "    check('a value the worksheet REFUTED reports CORRECTED, not DRIFTED',\n"
      "          'CORRECTED' in codes(claim) and 'DRIFTED' not in codes(claim),\n"
      '          codes(claim))\n'
      "    check('a correction is recorded but not routed back',\n"
      "          claim.route != 'SEND BACK', claim.route)\n"
      '\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Code value | Your value | Value correct? |\n'
      '|---|---|---|---|---|\n'
      '| 1 | `TEST_RADIUS_KM` | 137.5 | 100.0 | **UNVERIFIED** |\n'
      '""")\n'
      "    check('a value nobody checked reports UNCHECKED_MOVE',\n"
      "          'UNCHECKED_MOVE' in codes(claim), codes(claim))\n"
      '\n'
      '    # The live corpus case. A worksheet whose only verdict column asks\n'
      '    # about the CITATION has not answered the value question at all, so\n'
      '    # neither DRIFTED nor CORRECTED is honest -- and a NO here routinely\n'
      "    # means 'wrong authority, value correct' (rows G4, G6, G7, G8).\n"
      '    claim = run_layers("""\n'
      '| # | Constant | Value | Cited source | Citation correct? |\n'
      '|---|---|---|---|---|\n'
      '| 1 | `TEST_RADIUS_KM` | 137.5 | Somebody et al. | **NO -- wrong authority** |\n'
      '""")\n'
      "    check('a citation-only verdict cannot clear or condemn a moved value',\n"
      "          'UNCHECKED_MOVE' in codes(claim), codes(claim))\n"
      '\n'
      '    # L3 -- a qualification is evidence. The clearing branch is the one\n'
      '    # place a verdict produces no finding at all, so it is the only\n'
      '    # place a reservation can disappear. No live claim currently sits\n'
      '    # on a qualified YES, which is exactly why these two run: the guard\n'
      '    # would otherwise be unfalsifiable on this corpus.\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Code value | Your value | Value correct? | Notes |\n'
      '|---|---|---|---|---|---|\n'
      '| 1 | `TEST_RADIUS_KM` | 100.0 | 100.0 | **YES -- to 2 dp only** | fine |\n'
      '""")\n'
      "    check('a YES carrying a reservation does not read as clean',\n"
      "          'QUALIFIED_PASS' in codes(claim), codes(claim))\n"
      '\n'
      '    claim = run_layers(VALUE_TABLE)\n'
      "    check('a bare YES still clears with no findings at all',\n"
      '          not codes(claim), codes(claim))\n'
      '\n'
      '    # L3 -- the same NO means opposite things in the same column.\n'
      "    # 'wrong authority' says the value is fine; 'arithmetic error' says\n"
      '    # the source is fine. The tool may not pick one, and until this\n'
      '    # change it printed the first reading over both.\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Value | Cited source | Citation correct? | Notes |\n'
      '|---|---|---|---|---|---|\n'
      '| 1 | `TEST_RADIUS_KM` | 100.0 | Somebody et al. | **NO -- arithmetic error** | x |\n'
      '""")\n'
      "    check('a qualified refusal is not classified as a citation defect',\n"
      "          'REFUSAL_UNCLASSIFIED' in codes(claim)\n"
      "          and 'CITATION_DEFECT' not in codes(claim), codes(claim))\n"
      '\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Value | Cited source | Citation correct? | Notes |\n'
      '|---|---|---|---|---|---|\n'
      '| 1 | `TEST_RADIUS_KM` | 100.0 | Somebody et al. | **NO** | x |\n'
      '""")\n'
      "    check('a bare NO in a citation column is still a citation defect',\n"
      "          'CITATION_DEFECT' in codes(claim), codes(claim))\n"
      '\n'
      '    # L3 -- the Oort shape: an annotation asserting a completed check\n'
      '    # over a row that records the check as not performed.\n'
      '    claim = run_layers("""\n'
      '| # | Constant | Code value | Your value | Value correct? |\n')),
    ('test_worksheet_checker.py',
     ('# ============================================================\n'
      '# THE LIVE CORPUS -- pin what the checker actually finds\n'
      '# ============================================================\n'
      '\n'
      "DRIFTED_CONSTANTS = ('HELIOPAUSE_RADII', 'BENNU_RADIUS_KM',\n"
      "                     'HAUMEA_RADIUS_KM', 'ARROKOTH_RADIUS_KM')\n"
      '\n'
      '\n'
      'def test_live_corpus(project_dir):\n'
      '    sheets = wc.load_worksheets(project_dir)\n'),
     ('# ============================================================\n'
      '# THE LIVE CORPUS -- pin what the checker actually finds\n'
      '# ============================================================\n'
      '\n'
      '# All four moved after their worksheets ran, and all four sit in\n'
      '# worksheets whose only verdict column asks about the CITATION. So the\n'
      '# tool cannot say whether the movement was a correction or a defect,\n'
      '# and says so. Before 2026-08-15 it called all eight rows DRIFTED,\n'
      '# which asserted the strongest of the three readings on no evidence.\n'
      "UNCHECKED_MOVE_CONSTANTS = ('HELIOPAUSE_RADII', 'BENNU_RADIUS_KM',\n"
      "                            'HAUMEA_RADIUS_KM', 'ARROKOTH_RADIUS_KM')\n"
      '\n'
      '\n'
      'def test_live_corpus(project_dir):\n'
      '    sheets = wc.load_worksheets(project_dir)\n')),
    ('test_worksheet_checker.py',
     ("    check('the checker reads the whole python corpus', files > 50, files)\n"
      "    check('annotations are found at all', len(claims) > 50, len(claims))\n"
      '\n'
      '    drifted = set()\n'
      '    not_performed = set()\n'
      '    for claim in claims:\n'
      '        for _layer, code, _detail in claim.findings:\n'
      "            if code == 'DRIFTED':\n"
      '                drifted.add(claim.label)\n'
      "            if code == 'CHECK_NOT_PERFORMED':\n"
      '                not_performed.add(claim.label)\n'
      '\n'
      '    for name in DRIFTED_CONSTANTS:\n'
      "        check('L2b still finds the drift in %s' % name,\n"
      '              name in drifted, sorted(drifted))\n'
      '\n'
      "    check('L3 still finds BENNU_RADIUS_KM crediting an unperformed check',\n"
      "          'BENNU_RADIUS_KM' in not_performed, sorted(not_performed))\n"
      '\n'),
     ("    check('the checker reads the whole python corpus', files > 50, files)\n"
      "    check('annotations are found at all', len(claims) > 50, len(claims))\n"
      '\n'
      '    drifted = set()\n'
      '    moved = set()\n'
      '    not_performed = set()\n'
      '    for claim in claims:\n'
      '        for _layer, code, _detail in claim.findings:\n'
      "            if code == 'DRIFTED':\n"
      '                drifted.add(claim.label)\n'
      "            if code in ('UNCHECKED_MOVE', 'CORRECTED'):\n"
      '                moved.add(claim.label)\n'
      "            if code == 'CHECK_NOT_PERFORMED':\n"
      '                not_performed.add(claim.label)\n'
      '\n'
      '    for name in UNCHECKED_MOVE_CONSTANTS:\n'
      "        check('L2b still sees the movement in %s' % name,\n"
      '              name in moved, sorted(moved))\n'
      '\n'
      '    # The point of the change is that the strong word is now reserved.\n'
      '    # If DRIFTED reappears in this corpus, a worksheet grew a value\n'
      '    # verdict and a real defect is being reported -- read it, do not\n'
      '    # relax this.\n'
      "    check('no live claim is called DRIFTED without a value verdict',\n"
      '          not drifted, sorted(drifted))\n'
      '\n'
      '    # Seven live refusals carry their own reason and are no longer\n'
      '    # reported as wrong-authority. If this reaches zero, either the\n'
      '    # worksheets were re-cut or the qualification stopped being read.\n'
      '    unclassified = sum(1 for c in claims\n'
      '                       for _l, code, _d in c.findings\n'
      "                       if code == 'REFUSAL_UNCLASSIFIED')\n"
      "    check('qualified refusals are reported as unclassified',\n"
      '          unclassified > 0, unclassified)\n'
      '\n'
      "    check('L3 still finds BENNU_RADIUS_KM crediting an unperformed check',\n"
      "          'BENNU_RADIUS_KM' in not_performed, sorted(not_performed))\n"
      '\n')),
]


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    texts = {}
    for name, _old, _new in HUNKS:
        if not os.path.exists(name):
            print('ABORT: %s not found. Run this from the repo root.' % name)
            return 1
        texts.setdefault(name, normalized(name).decode('utf-8'))

    planned = []
    for index, (name, old, new) in enumerate(HUNKS, 1):
        text = texts[name]
        if new in text:
            planned.append((index, name, 'already'))
            continue
        count = text.count(old)
        if count != 1:
            print('ABORT: hunk %d in %s matched %d times, expected 1.'
                  % (index, name, count))
            print('Nothing was written, in any file. The code this patch')
            print('was written against is not the code on disk.')
            return 1
        texts[name] = text.replace(old, new)
        planned.append((index, name, 'apply'))

    for index, name, action in planned:
        print('  hunk %d  %-9s %s' % (index, action, name))

    if all(action == 'already' for _i, _n, action in planned):
        print('Nothing to do. Every hunk is already in place.')
        return 0

    for name, text in texts.items():
        with open(name, 'wb') as handle:
            handle.write(text.encode('utf-8'))
        print('  wrote     %s  -> %s'
              % (name, hashlib.md5(normalized(name)).hexdigest()))

    print()
    print('Done. Next: run test_worksheet_checker.py, then')
    print('worksheet_checker.py, then maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
