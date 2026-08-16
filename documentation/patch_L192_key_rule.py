"""
patch_L192_key_rule.py

L-192, one build. Adds the exact-key row rule to worksheet_checker.py,
and the tests that show the rule can fail.

Companion to the NEW module worksheet_request_builder.py, delivered as
a complete file. Save that one into the repo root as well; this script
only patches the two files that already exist.

WHAT IT CHANGES IN worksheet_checker.py

  - imports worksheet_keys
  - adds ROLE_KEY, and the 'key' / 'row key' headers, to the registry
  - adds module_source() and key_sources(), each read once per run
  - adds Claim.key(), which mints through worksheet_keys and never
    composes a key locally -- two spellings of the enclosing name
    would let a key be born stale
  - adds rule 0 to match_row(): an exact key match wins outright, and
    a key the WORKSHEET carries that no longer resolves announces
    KEY_STALE instead of falling through to the fuzzy rules
  - routes KEY_STALE at the L1 call site

WHAT IT CHANGES IN test_worksheet_checker.py

  - adds test_key_rule(): six checks, all synthetic. No worksheet in
    the corpus carries a Key column yet, so the live run cannot reach
    rule 0. Without these the rule would be a check that cannot fail.
    One of the six is load-bearing: a stale-key row whose PROSE would
    match, proving the rule refuses to fall through rather than
    passing because nothing matched.

HOW THE HUNKS ARE CARRIED

EDITS is JSON, one [line, old, new] triple per hunk, bottom-up per
file. `old` and `new` are the literal file text with \\n escapes, so
the whole patch is readable in this file rather than hidden behind an
encoding.

Base fingerprints taken at repo HEAD 87176e9, 2026-08-15. Every hunk
was derived by diffing that exact tree against a sandbox copy on which
the checker report, both test suites and the builder all ran green.

Run:
    Save into the palomas_orrery repo root, open in VS Code, click Run.

Success: one "ok" line per hunk, then "patch applied" per file.
Failure: a single ERROR or ANCHOR FAIL line; nothing is written.

Written August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import json
import os
import sys

BASE = {'worksheet_checker.py': '5eacb5d1766cff8f44cadc744a9c0ce6', 'test_worksheet_checker.py': 'b5ce1934ba262d0d6866c4b1cd7f14f9'}

EDITS = json.loads(r"""
{
 "worksheet_checker.py": [
  [
   997,
   "\n    best = None\n    ambiguous = ''\n    for table in tables:\n        row, rule, note = match_row(table, claim.label, '', claim.code_value)\n        if row is not None:\n            best = (table, row, rule)\n            break\n        if rule == 'AMBIGUOUS':\n            ambiguous = note\n    if best is None:\n        if ambiguous:\n            claim.fail('L1', 'AMBIGUOUS_ROW', ambiguous, 'SEND BACK')\n        else:\n            claim.fail('L1', 'UNMATCHED',",
   "\n    best = None\n    ambiguous = ''\n    stale = ''\n    for table in tables:\n        row, rule, note = match_row(table, claim.label, '',\n                                    claim.code_value, claim.key())\n        if row is not None:\n            best = (table, row, rule)\n            break\n        if rule == 'AMBIGUOUS':\n            ambiguous = note\n        if rule == 'KEY_STALE':\n            stale = note\n    if best is None:\n        if stale:\n            claim.fail('L1', 'KEY_STALE', stale, 'SEND BACK')\n        elif ambiguous:\n            claim.fail('L1', 'AMBIGUOUS_ROW', ambiguous, 'SEND BACK')\n        else:\n            claim.fail('L1', 'UNMATCHED',"
  ],
  [
   859,
   "        if self.unit.kind == 'constant':\n            return self.unit.value\n        return None\n\n    @property\n    def claim_values(self):",
   "        if self.unit.kind == 'constant':\n            return self.unit.value\n        return None\n\n    def key(self, ordinal=None):\n        \"\"\"The row key for this claim, minted the builder's way.\n\n        Minted by worksheet_keys, never composed here. Two spellings\n        of the enclosing name would let a key be born stale -- correct\n        when written, unresolvable forever, with nothing to say so.\n        \"\"\"\n        return wk.key_for_site(self.path, module_source(self.path),\n                               self.unit.line_start, self.label, ordinal)\n\n    @property\n    def claim_values(self):"
  ],
  [
   829,
   "    return kept, dropped\n\n\nclass Claim(object):\n    \"\"\"One annotation, with the value it is attached to.\"\"\"\n",
   "    return kept, dropped\n\n\n_SOURCE_CACHE = {}\n_KEY_SOURCES = {}\n\n\ndef key_sources(project_dir='.'):\n    \"\"\"module file name -> source text, for key resolution.\n\n    Built once and reused. A module missing from this map makes its\n    keys resolve to KEY_STALE with the module named, which is what a\n    reader needs; an empty map would make EVERY key stale and say the\n    same thing about all of them, so the map is built eagerly rather\n    than filled on demand.\n    \"\"\"\n    if not _KEY_SOURCES:\n        for fname in sorted(os.listdir(project_dir)):\n            if not fname.endswith('.py'):\n                continue\n            _KEY_SOURCES[fname] = module_source(\n                os.path.join(project_dir, fname))\n    return _KEY_SOURCES\n\n\ndef module_source(path):\n    \"\"\"Source text of a module, read once per run.\n\n    A read failure returns '' and is NOT swallowed: worksheet_keys\n    reports an unresolvable key as KEY_STALE, which is the honest\n    outcome for a module this process could not open.\n    \"\"\"\n    if path not in _SOURCE_CACHE:\n        try:\n            with open(path, encoding='utf-8', errors='replace') as handle:\n                _SOURCE_CACHE[path] = handle.read()\n        except OSError:\n            _SOURCE_CACHE[path] = ''\n    return _SOURCE_CACHE[path]\n\n\nclass Claim(object):\n    \"\"\"One annotation, with the value it is attached to.\"\"\"\n"
  ],
  [
   523,
   "    return name.lower() in strip_cell(cell).lower()\n\n\ndef match_row(table, unit_name, unit_text, code_value):\n    \"\"\"(row, rule, note) for the row about this value, or (None, ...).\n\n    Returns rule 'AMBIGUOUS' when a rule matched more than one row.\n    \"\"\"\n    id_index = table.column(ROLE_ID)\n    if id_index is None:\n        return None, 'NO_ID_COLUMN', ''",
   "    return name.lower() in strip_cell(cell).lower()\n\n\ndef match_row(table, unit_name, unit_text, code_value, key=''):\n    \"\"\"(row, rule, note) for the row about this value, or (None, ...).\n\n    Returns rule 'AMBIGUOUS' when a rule matched more than one row.\n\n    Rule 0 is the KEY, and it does not fall through. A worksheet that\n    states a key has named the site exactly; if that key does not\n    resolve against today's source, the honest outcome is KEY_STALE --\n    a rename someone has to confirm. Letting it drop into the fuzzy\n    rules would hide the rename behind a lucky prose hit, which is\n    the shape of failure the key was introduced to end.\n    \"\"\"\n    key_index = table.column(ROLE_KEY)\n    if key and key_index is not None:\n        hits = [row for row in table.rows\n                if key_index < len(row[1])\n                and strip_cell(row[1][key_index]).strip('`') == key]\n        if len(hits) == 1:\n            return hits[0], 'KEY', ''\n        if len(hits) > 1:\n            return None, 'AMBIGUOUS', '%d rows under KEY' % len(hits)\n        # No row carries this claim's key. Resolving the CLAIM's key\n        # here would be circular -- it was minted from today's source\n        # a moment ago, so it always resolves. The question is whether\n        # a key the WORKSHEET carries has stopped resolving, because\n        # that is what a rename looks like from this side.\n        for row in table.rows:\n            if key_index >= len(row[1]):\n                continue\n            recorded = strip_cell(row[1][key_index]).strip('`')\n            if not recorded:\n                continue\n            try:\n                wk.parse(recorded)\n            except wk.KeyError_:\n                continue\n            line, reason = wk.resolve(recorded, key_sources())\n            if line is None:\n                return None, 'KEY_STALE', reason\n        return None, 'KEY_ABSENT', 'no row carries %s' % key\n\n    id_index = table.column(ROLE_ID)\n    if id_index is None:\n        return None, 'NO_ID_COLUMN', ''"
  ],
  [
   138,
   "\nHEADER_ROLES = {\n    '#': ROLE_NUM,\n\n    'claim': ROLE_ID,\n    'claim in code': ROLE_ID,",
   "\nHEADER_ROLES = {\n    '#': ROLE_NUM,\n\n    'key': ROLE_KEY,\n    'row key': ROLE_KEY,\n\n    'claim': ROLE_ID,\n    'claim in code': ROLE_ID,"
  ],
  [
   121,
   "# this whole layer exists to prevent.\n\nROLE_NUM = 'num'\nROLE_ID = 'id'\nROLE_CODE = 'code_value'\nROLE_EVIDENCE = 'evidence_value'",
   "# this whole layer exists to prevent.\n\nROLE_NUM = 'num'\n# The row key minted by worksheet_request_builder.py. Not an\n# evidence role: a key names the row, it records nothing about it.\nROLE_KEY = 'key'\nROLE_ID = 'id'\nROLE_CODE = 'code_value'\nROLE_EVIDENCE = 'evidence_value'"
  ],
  [
   101,
   "import sys\n\nimport provenance_scanner as ps\n\nWORKSHEET_DIR = os.path.join('documentation', 'worksheets')\nREPORT_PATH = 'WORKSHEET_CHECK.md'",
   "import sys\n\nimport provenance_scanner as ps\nimport worksheet_keys as wk\n\nWORKSHEET_DIR = os.path.join('documentation', 'worksheets')\nREPORT_PATH = 'WORKSHEET_CHECK.md'"
  ]
 ],
 "test_worksheet_checker.py": [
  [
   513,
   "    test_comparison()\n    test_verdicts()\n    test_registry()\n    test_layers()\n    test_display_instructions()\n    test_live_corpus(project_dir)",
   "    test_comparison()\n    test_verdicts()\n    test_registry()\n    test_key_rule()\n    test_layers()\n    test_display_instructions()\n    test_live_corpus(project_dir)"
  ],
  [
   225,
   "    _own, _tok, _scope, column = wc.read_verdict(table, table.rows[0][1])\n    check('a citation-only table reports which column it read',\n          column == 'citation-only', column)\n\n\n# ============================================================",
   "    _own, _tok, _scope, column = wc.read_verdict(table, table.rows[0][1])\n    check('a citation-only table reports which column it read',\n          column == 'citation-only', column)\n\n\n# ============================================================\n# RULE 0 -- THE KEY, AND ITS REFUSAL TO FALL THROUGH\n# ============================================================\n#\n# The key rule is INERT against today's corpus: no worksheet carries a\n# Key column yet, so match_row never reaches rule 0 and the live run\n# proves nothing about it. These are synthetic on purpose. Each is\n# shown to produce its outcome AND, where it matters, shown not to\n# produce the outcome it would have had without the rule.\n\nKEY_TABLE = \"\"\"\n| # | Key | Claim | Code value | Your value | Source | Value correct? | Citation correct? | Notes |\n|---|---|---|---|---|---|---|---|---|\n| R1 | `worksheet_keys.py::compose` | the compose helper | 1.0 | 1.0 | somewhere | YES | YES | fine |\n| R2 | `worksheet_keys.py::parse` | the parse helper | 2.0 | 2.0 | somewhere | YES | YES | fine |\n\"\"\"\n\nDUPLICATE_KEY_TABLE = \"\"\"\n| # | Key | Claim | Code value | Notes |\n|---|---|---|---|---|\n| R1 | `worksheet_keys.py::compose` | first | 1.0 | a |\n| R2 | `worksheet_keys.py::compose` | second | 1.0 | b |\n\"\"\"\n\n# A prose-matchable row whose key names a function that does not\n# exist. Without rule 0 the PROSE rule would match it happily; that is\n# precisely the lucky hit a rename must not hide behind.\nSTALE_KEY_TABLE = \"\"\"\n| # | Key | Claim | Code value | Notes |\n|---|---|---|---|---|\n| R1 | `worksheet_keys.py::function_renamed_away` | the compose helper writes a key from its parts | 1.0 | a |\n\"\"\"\n\n\ndef test_key_rule():\n    table = table_from(KEY_TABLE)\n    check('a Key header is recognised as a role',\n          table.column(wc.ROLE_KEY) is not None, table.unregistered)\n\n    row, rule, _note = wc.match_row(table, '', '', 1.0,\n                                    'worksheet_keys.py::compose')\n    check('an exact key match wins as rule KEY', rule == 'KEY', rule)\n    check('and it picks the row that carries the key',\n          row is not None and 'compose' in ' '.join(row[1]), row)\n\n    _row, rule, note = wc.match_row(table, '', '', 1.0,\n                                    'worksheet_keys.py::resolve')\n    check('a resolvable key no row carries is KEY_ABSENT',\n          rule == 'KEY_ABSENT', '%s %s' % (rule, note))\n\n    table = table_from(DUPLICATE_KEY_TABLE)\n    _row, rule, note = wc.match_row(table, '', '', 1.0,\n                                    'worksheet_keys.py::compose')\n    check('two rows under one key announce rather than pick',\n          rule == 'AMBIGUOUS', '%s %s' % (rule, note))\n\n    # The load-bearing one. The worksheet records a key minted before a\n    # rename, so it no longer resolves; the claim now mints a different\n    # key that no row carries. The prose in that row WOULD satisfy the\n    # PROSE rule, so a fall-through would report a clean match and the\n    # rename would never surface.\n    table = table_from(STALE_KEY_TABLE)\n    _row, rule, note = wc.match_row(\n        table, '', 'the compose helper writes a key from its parts', 1.0,\n        'worksheet_keys.py::compose')\n    check('a key the worksheet carries that no longer resolves is '\n          'KEY_STALE', rule == 'KEY_STALE', '%s %s' % (rule, note))\n    check('and it does NOT fall through to a prose match',\n          rule != 'PROSE', rule)\n\n    # Same table, no key supplied: the prose match must still succeed,\n    # or the previous check proves nothing -- it would be passing\n    # because nothing matches rather than because rule 0 stopped it.\n    _row, rule, _note = wc.match_row(\n        table, '', 'the compose helper writes a key from its parts', 1.0)\n    check('the same row DOES match on prose when no key is given',\n          rule == 'PROSE', rule)\n\n\n# ============================================================"
  ]
 ]
}
""")


def fingerprint(data):
    return hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()


def main():
    staged = []
    for path in sorted(EDITS):
        if not os.path.exists(path):
            print("ERROR: not found: %s" % path)
            print("       run this from the palomas_orrery repo root.")
            return 1
        with open(path, "rb") as handle:
            data = handle.read()
        got = fingerprint(data)
        if got != BASE[path]:
            print("ERROR: base moved: %s" % path)
            print("       expected %s" % BASE[path])
            print("       found    %s" % got)
            print("       nothing written. Re-pull or re-anchor.")
            return 1
        crlf = data.count(b"\r\n") > 0
        for line, old, new in EDITS[path]:
            old_b = old.encode("ascii")
            new_b = new.encode("ascii")
            if crlf:
                old_b = old_b.replace(b"\n", b"\r\n")
                new_b = new_b.replace(b"\n", b"\r\n")
            count = data.count(old_b)
            if count != 1:
                print("ANCHOR FAIL (%d matches): %s near line %d"
                      % (count, path, line))
                print("       nothing written.")
                return 1
            data = data.replace(old_b, new_b)
            print("  ok  %s near line %d" % (path, line))
        staged.append((path, data))

    for path, data in staged:
        with open(path, "wb") as handle:
            handle.write(data)
        print("patch applied: %s (%d bytes)" % (path, len(data)))

    print("")
    print("NEXT, both from the Run button:")
    print("  worksheet_checker.py        -- report unchanged, 61 of 104")
    print("  test_worksheet_checker.py   -- expect 69 checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
