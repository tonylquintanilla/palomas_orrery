"""patch_L202_1_checker_json_returns.py -- L-202 and L-201, checker
side. Read a JSON return, verify its row hashes, and write the routing
file the `sendbacks` selection consumes.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
worksheet_checker.py), open it in VS Code, and click Run.

    python patch_L202_1_checker_json_returns.py

Companion to patch_L201_1_selection_and_json.py, which built the
producer side. This one edits worksheet_checker.py and
test_worksheet_checker.py, so the two cannot collide.

WHAT IT DOES
------------
READING A JSON RETURN. A returned .jsonl worksheet is parsed into the
SAME Table the markdown parser produces, by naming the synthesized
columns exactly as HEADER_ROLES already spells them. Every layer below
-- match, L2a, L2b, L3 -- then runs unchanged against either format.
One adapter, not a second checking path.

Markdown is NOT deprecated and both readers stay live permanently: the
seventeen historical worksheets are markdown. A responder who returns a
JSON array instead of one object per line is also accepted, because
refusing work over a formatting choice would be a poor trade.

LH, A NEW LAYER. Each returned row carries an eight-character hash over
the fields a responder must not edit. A row whose hash is wrong reads
ROW_MODIFIED; a row with NO hash reads ROW_HASH_MISSING. Both go back.
The case is attribution: without this, a responder who rounds a code
value produces an L2b mismatch that reports the CODE as drifted,
sending somebody to investigate a constant that never moved.

A markdown table has no integrity map, and that is NOT APPLICABLE
rather than a pass -- the layer records nothing there.

TRUNCATION IS SALVAGED AND ANNOUNCED. A return cut off mid-generation
keeps every complete line, and the lines that did not parse are counted
and printed. A blind spot that stays silent is the failure mode.

THE ROUTING FILE. Every run writes data/worksheet_routed.json with the
keys of rows routed SEND BACK. That is what the builder's `sendbacks`
selection reads. A key list is legitimate only when the checker wrote
it, never one a person typed, and the test is whether the list can be
regenerated -- this one is an output of the run that produced the
routing.

EVIDENCE ON EVERY RUN. The summary gains a line that cannot print
unless the rows were read: "N row hash(es) verified: N ok, N missing, N
modified", plus the count of keys written.

WHAT THE MUTATION TESTS FOUND, AND IT IS THE POINT
---------------------------------------------------
Two of the first tests written for this could not fail.

The integrity layer had a test for the markdown NOT-APPLICABLE case and
none for the failing case, so a mutation that made the layer return
early for EVERY status passed all 96 checks. It now has five checks
that ask it to fail.

The routing test asserted the file exists -- and it did, because an
earlier real run had written it into the repo. A mutation replacing the
write with `pass` passed. It now writes into a fresh temporary
directory, where existence proves THIS call wrote it, and checks a
non-zero count against the file's own contents.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot. What it installs is permanent:
the JSON reader, the LH layer, the routing file, and 44 new tests.

SAFETY
------
All-or-nothing across BOTH files. Each is fingerprinted
(CRLF-normalized) and every anchor must match exactly once before
anything is written. Any mismatch aborts with nothing written.

Success: one `ok` line per file, then `patch applied (N bytes)`.
Failure: a single `ERROR:` or `ANCHOR FAIL` line; nothing is written.

AFTER IT RUNS
-------------
    python test_worksheet_checker.py        (expect 105 checks)
    python maintenance_run.py
"""

import hashlib
import os
import sys


EDITS = {
    'test_worksheet_checker.py': {
        'fp': 'e02ed891238cb1bd2e94392472fdcb98',
        'edits': [
            ('\nimport os',
             '\nimport json\nimport os'),
            ('import sys\n',
             'import sys\nimport tempfile\n'),
            ('\ndef main():',
             '\ndef _pilot_row(**overrides):\n    """One returned row object, valid unless an override breaks it."""\n    row = {\n        \'record\': \'row\',\n        \'id\': \'R1\',\n        \'key\': \'constants_new.py::KM_PER_AU\',\n        \'claim\': \'KM_PER_AU\',\n        \'code_value\': \'149597870.7\',\n        \'your_value\': \'149597870.7\',\n        \'source\': \'IAU 2012 Resolution B2\',\n        \'value_correct\': \'yes\',\n        \'citation_correct\': \'yes\',\n        \'notes\': \'\',\n    }\n    row[\'hash\'] = wc.row_hash(row[\'key\'], row[\'claim\'], row[\'code_value\'])\n    row.update(overrides)\n    return row\n\n\ndef _as_jsonl(rows):\n    return \'\\n\'.join(json.dumps(r, sort_keys=True) for r in rows) + \'\\n\'\n\n\ndef test_json_reader():\n    """A JSON return becomes the same Table a markdown one does."""\n    header = {\'record\': \'header\', \'batch\': \'test\', \'selection\': \'all\'}\n    text = _as_jsonl([header, _pilot_row(), _pilot_row(id=\'R2\')])\n    tables, integrity, unreadable = wc.parse_json_worksheet(\'r.jsonl\', text)\n\n    check(\'json: one table comes back\', len(tables) == 1, len(tables))\n    if not tables:\n        return\n    table = tables[0]\n    check(\'json: the header line is not a row\', len(table.rows) == 2,\n          len(table.rows))\n    check(\'json: it is a row table the layers will use\',\n          table.is_row_table, repr(table.roles))\n    check(\'json: no column is unregistered\', table.unregistered == [],\n          repr(table.unregistered))\n    check(\'json: the code value lands in the code column\',\n          table.cell(table.rows[0][1], wc.ROLE_CODE) == \'149597870.7\',\n          table.cell(table.rows[0][1], wc.ROLE_CODE))\n    check(\'json: the citation verdict lands in its own column\',\n          table.cell(table.rows[0][1], wc.ROLE_CITATION_VERDICT) == \'yes\',\n          table.cell(table.rows[0][1], wc.ROLE_CITATION_VERDICT))\n    check(\'json: nothing unreadable in a clean return\', unreadable == [],\n          repr(unreadable))\n    check(\'json: every row is hash-checked\', len(integrity) == 2,\n          repr(integrity))\n\n\ndef test_json_row_hash():\n    """The hash catches an edited do-not-edit field, and its absence."""\n    good = _pilot_row()\n    status, _detail = wc.check_row_hash(good)\n    check(\'hash: a clean row passes\', status == \'ok\', status)\n\n    rounded = _pilot_row(code_value=\'149597871\')\n    status, detail = wc.check_row_hash(rounded)\n    check(\'hash: a rounded code value is caught\', status == \'mismatch\',\n          status)\n    check(\'hash: the detail names the cause\',\n          \'do-not-edit\' in detail, detail)\n\n    reflowed = _pilot_row(key=\'constants_new.py :: KM_PER_AU\')\n    check(\'hash: a reflowed key is caught\',\n          wc.check_row_hash(reflowed)[0] == \'mismatch\', \'\')\n\n    stripped = _pilot_row()\n    del stripped[\'hash\']\n    check(\'hash: a MISSING hash fails rather than passing\',\n          wc.check_row_hash(stripped)[0] == \'missing\',\n          wc.check_row_hash(stripped)[0])\n\n    blank = _pilot_row(hash=\'\')\n    check(\'hash: a blank hash fails too\',\n          wc.check_row_hash(blank)[0] == \'missing\', \'\')\n\n    # The builder and the checker each carry this function; they must\n    # agree byte for byte or every returned row reads as modified.\n    check(\'hash: eight characters, as the request states\',\n          len(wc.row_hash(\'a\', \'b\', \'c\')) == 8, wc.row_hash(\'a\', \'b\', \'c\'))\n\n\ndef test_json_truncation_is_salvaged_and_announced():\n    """A return cut off mid-generation keeps its complete rows."""\n    header = {\'record\': \'header\', \'batch\': \'test\'}\n    text = _as_jsonl([header, _pilot_row(), _pilot_row(id=\'R2\')])\n    cut = text.strip().split(\'\\n\')\n    cut[-1] = cut[-1][:40]\n    tables, integrity, unreadable = wc.parse_json_worksheet(\n        \'cut.jsonl\', \'\\n\'.join(cut) + \'\\n\')\n\n    check(\'truncation: the complete rows survive\',\n          tables and len(tables[0].rows) == 1,\n          len(tables[0].rows) if tables else 0)\n    check(\'truncation: the broken line is REPORTED, not dropped\',\n          len(unreadable) == 1, repr(unreadable))\n\n\ndef test_json_array_return_is_accepted():\n    """A responder who returns an array instead of lines is still read."""\n    rows = [{\'record\': \'header\'}, _pilot_row(), _pilot_row(id=\'R2\')]\n    tables, _integrity, unreadable = wc.parse_json_worksheet(\n        \'array.json\', json.dumps(rows))\n    check(\'array: rows are read\', tables and len(tables[0].rows) == 2,\n          len(tables[0].rows) if tables else 0)\n    check(\'array: nothing reported unreadable\', unreadable == [],\n          repr(unreadable))\n\n\ndef test_markdown_has_no_integrity_map():\n    """A markdown worksheet is NOT APPLICABLE, not passed."""\n    text = (\'| Key | Claim | Code value | Value correct? |\\n\'\n            \'|---|---|---|---|\\n\'\n            \'| `k` | KM_PER_AU | 149597870.7 | yes |\\n\')\n    tables = wc.parse_tables(\'sheet.md\', text)\n    check(\'markdown: still parses\', len(tables) == 1, len(tables))\n    check(\'markdown: carries no integrity map\',\n          tables[0].integrity is None, repr(tables[0].integrity))\n\n    # The layer must not invent a failure for a format that never had\n    # hashes. Seventeen historical worksheets are markdown.\n    class Fake(object):\n        def __init__(self):\n            self.findings = []\n            self.route = \'\'\n            self.current_ordinal = None\n            self.routed_ordinals = []\n\n        def fail(self, layer, code, detail, route):\n            self.findings.append((layer, code, detail))\n            if route:\n                self.route = route\n\n    claim = Fake()\n    wc.check_row_integrity(claim, tables[0], 3)\n    check(\'markdown: the integrity layer records nothing\',\n          claim.findings == [], repr(claim.findings))\n\n\ndef test_integrity_layer_fails_a_bad_row():\n    """LH routes a modified or unhashed row back.\n\n    The NOT APPLICABLE case above is only half the layer. A mutation\n    that made check_row_integrity return early for EVERY status passed\n    all 96 checks, because nothing here had ever asked it to fail.\n    """\n    class Fake(object):\n        def __init__(self):\n            self.findings = []\n            self.route = \'\'\n            self.current_ordinal = None\n            self.routed_ordinals = []\n\n        def fail(self, layer, code, detail, route):\n            self.findings.append((layer, code, detail))\n            if route:\n                self.route = route\n\n    header = {\'record\': \'header\'}\n    rows = [_pilot_row(id=\'R1\'),\n            _pilot_row(id=\'R2\', code_value=\'999\'),\n            _pilot_row(id=\'R3\')]\n    del rows[2][\'hash\']\n    tables, _integrity, _bad = wc.parse_json_worksheet(\n        \'r.jsonl\', _as_jsonl([header] + rows))\n    table = tables[0]\n    lines = [line_no for line_no, _cells in table.rows]\n\n    clean = Fake()\n    wc.check_row_integrity(clean, table, lines[0])\n    check(\'LH: a clean row records nothing\', clean.findings == [],\n          repr(clean.findings))\n\n    modified = Fake()\n    wc.check_row_integrity(modified, table, lines[1])\n    check(\'LH: a modified row is caught\',\n          [f[1] for f in modified.findings] == [\'ROW_MODIFIED\'],\n          repr(modified.findings))\n    check(\'LH: a modified row goes back\',\n          modified.route == \'SEND BACK\', modified.route)\n\n    unhashed = Fake()\n    wc.check_row_integrity(unhashed, table, lines[2])\n    check(\'LH: an unhashed row is caught\',\n          [f[1] for f in unhashed.findings] == [\'ROW_HASH_MISSING\'],\n          repr(unhashed.findings))\n    check(\'LH: an unhashed row goes back\',\n          unhashed.route == \'SEND BACK\', unhashed.route)\n\n    absent = Fake()\n    wc.check_row_integrity(absent, table, 9999)\n    check(\'LH: a row missing from the map is caught, not assumed fine\',\n          absent.route == \'SEND BACK\', repr(absent.findings))\n\n\ndef test_routing_file(project_dir):\n    """The routing file is written, and says what it contains."""\n    scratch = tempfile.mkdtemp(prefix=\'routing_test_\')\n    written, error = wc.write_routing_file(scratch, [])\n    check(\'routing: an empty run still writes the file\',\n          error == \'\' and written == 0, \'%r %r\' % (written, error))\n\n    # Deliberately NOT the repo\'s own copy. Checking the repo file\n    # proved only that some earlier run had written one -- a mutation\n    # replacing the write with `pass` passed this test.\n    path = os.path.join(scratch, wc.ROUTED_PATH)\n    check(\'routing: the file exists\', os.path.isfile(path), path)\n    if not os.path.isfile(path):\n        return\n    with open(path, encoding=\'utf-8\') as handle:\n        payload = json.load(handle)\n    check(\'routing: it names its writer\',\n          payload.get(\'written_by\') == \'worksheet_checker.py\',\n          repr(payload.get(\'written_by\')))\n    check(\'routing: the key list is a list\',\n          isinstance(payload.get(\'send_back\'), list),\n          repr(type(payload.get(\'send_back\'))))\n    check(\'routing: the count matches the list\',\n          payload.get(\'send_back_count\') == len(payload.get(\'send_back\', [])),\n          repr(payload.get(\'send_back_count\')))\n\n    # With real keys, so the returned count and the file agree on a\n    # number that is not zero. A mutation returning a hard 0 passed\n    # while every count in sight was already 0.\n    class FakeClaim(object):\n        def __init__(self, key, route):\n            self._key = key\n            self.route = route\n            self.routed_ordinals = []\n\n        def key(self, ordinal=None):\n            return self._key\n\n    claims = [FakeClaim(\'a.py::ONE\', \'SEND BACK\'),\n              FakeClaim(\'a.py::TWO\', \'SEND BACK\'),\n              FakeClaim(\'a.py::THREE\', \'CONVERSATION\')]\n    written, error = wc.write_routing_file(scratch, claims)\n    check(\'routing: only SEND BACK rows are written\',\n          written == 2 and error == \'\', \'%r %r\' % (written, error))\n    with open(path, encoding=\'utf-8\') as handle:\n        payload = json.load(handle)\n    check(\'routing: the file holds the two routed keys\',\n          payload.get(\'send_back\') == [\'a.py::ONE\', \'a.py::TWO\'],\n          repr(payload.get(\'send_back\')))\n    check(\'routing: the returned count matches what was written\',\n          written == len(payload.get(\'send_back\', [])),\n          \'%r vs %r\' % (written, payload.get(\'send_back\')))\n\n\ndef main():'),
            ('    test_live_corpus(project_dir)\n',
             '    test_live_corpus(project_dir)\n    test_json_reader()\n    test_json_row_hash()\n    test_json_truncation_is_salvaged_and_announced()\n    test_json_array_return_is_accepted()\n    test_markdown_has_no_integrity_map()\n    test_integrity_layer_fails_a_bad_row()\n    test_routing_file(project_dir)\n'),
        ],
    },
    'worksheet_checker.py': {
        'fp': 'e80e1d8221e31d0a16a91c9a019c22b3',
        'edits': [
            ('\nimport json',
             '\nimport hashlib\nimport json'),
            ("STATE_PATH = os.path.join('data', 'worksheet_check_state.json')\n",
             "STATE_PATH = os.path.join('data', 'worksheet_check_state.json')\n# Written by this tool, read by worksheet_request_builder's `sendbacks`\n# selection. See write_routing_file.\nROUTED_PATH = os.path.join('data', 'worksheet_routed.json')\n"),
            ('\n    def __init__(self, path, header_line, headers, rows):\n        self.path = path',
             '\n    def __init__(self, path, header_line, headers, rows,\n                 integrity=None):\n        self.path = path'),
            ('        self.rows = rows\n        self.roles = [HEADER_ROLES.get(strip_cell(h).lower())',
             '        self.rows = rows\n        # {line_no: (status, detail)} for a JSON return; None for a\n        # markdown worksheet, which carries no hashes and never did.\n        # None means NOT APPLICABLE, not "passed" -- the layer that\n        # reads this skips a markdown table rather than clearing it.\n        self.integrity = integrity\n        self.roles = [HEADER_ROLES.get(strip_cell(h).lower())'),
            ('    return tables\n',
             '    return tables\n\n\n# ============================================================\n# JSON RETURNS (L-202)\n# ============================================================\n#\n# The request now goes out as JSON Lines and comes back the same way.\n# This reads it into the SAME Table the markdown parser produces, so\n# every layer below -- match, L2a, L2b, L3 -- runs unchanged against\n# either format. One adapter rather than a second checking path: a\n# parallel pipeline is the thing this project has a rule about.\n#\n# The adapter works by naming the synthesized columns exactly as\n# HEADER_ROLES already spells them. Nothing here decides what a column\n# MEANS; the registry above still does.\n#\n# MARKDOWN IS NOT DEPRECATED. Seventeen historical worksheets are\n# markdown and always will be, so both readers stay live permanently.\n# (Tony\'s ruling 2026-08-17: send the JSON, fall back to markdown if a\n# return will not parse.)\n\nJSON_SUFFIXES = (\'.jsonl\', \'.json\')\n\n# Field in the returned object -> the header spelling HEADER_ROLES\n# knows. Order fixes the cell order of the synthesized row.\nJSON_FIELD_HEADERS = (\n    (\'key\', \'Key\'),\n    (\'claim\', \'Claim\'),\n    (\'code_value\', \'Code value\'),\n    (\'your_value\', \'Your value\'),\n    (\'source\', \'Source\'),\n    (\'value_correct\', \'Value correct?\'),\n    (\'citation_correct\', \'Citation correct?\'),\n    (\'notes\', \'Notes\'),\n)\n\nHASH_CHARS = 8\n\n\ndef row_hash(key, claim, code_value):\n    """Short digest over the fields a responder must not edit.\n\n    Must agree with worksheet_request_builder.row_hash byte for byte.\n    Duplicated deliberately rather than imported: the checker is\n    read-only over the corpus and does not import the builder, which\n    would put a writer behind that boundary. The two are pinned\n    together by test_worksheet_request_builder.py.\n    """\n    parts = []\n    for field in (key, claim, code_value):\n        parts.append(\' \'.join(str(field if field is not None else \'\').split()))\n    blob = \'\\n\'.join(parts).encode(\'utf-8\')\n    return hashlib.sha256(blob).hexdigest()[:HASH_CHARS]\n\n\ndef check_row_hash(record):\n    """(\'ok\'|\'missing\'|\'mismatch\', detail) for one returned row.\n\n    A MISSING hash fails. A hash that quietly passes when absent is a\n    check that cannot fail -- and stripping the field is exactly what\n    an editor reformatting the file would do.\n    """\n    stated = str(record.get(\'hash\', \'\') or \'\').strip().lower()\n    if not stated:\n        return \'missing\', \'the row carries no hash\'\n    expected = row_hash(record.get(\'key\', \'\'), record.get(\'claim\', \'\'),\n                        record.get(\'code_value\', \'\'))\n    if stated != expected:\n        return \'mismatch\', (\'hash %s, but key/claim/code value hash to %s \'\n                            \'-- a do-not-edit field was changed\'\n                            % (stated, expected))\n    return \'ok\', \'\'\n\n\ndef parse_json_worksheet(path, text):\n    """(tables, integrity, unreadable) for one JSON Lines worksheet.\n\n    `integrity` maps a synthesized row\'s line number to (status,\n    detail). `unreadable` lists lines that did not parse, because a\n    blind spot that stays silent is the failure mode, not a tidy\n    output.\n\n    Tolerant on the way IN, deliberately: a return may come back as a\n    JSON array rather than one object per line, and refusing it would\n    throw away work over a formatting choice. Line-delimited is what\n    goes out, because it is what survives truncation.\n    """\n    records = []\n    unreadable = []\n    lines = text.splitlines()\n    stripped = text.strip()\n\n    array = None\n    if stripped.startswith(\'[\') or stripped.startswith(\'{"records"\'):\n        try:\n            loaded = json.loads(stripped)\n        except ValueError:\n            loaded = None\n        if isinstance(loaded, list):\n            array = loaded\n        elif isinstance(loaded, dict) and isinstance(\n                loaded.get(\'records\'), list):\n            array = loaded[\'records\']\n\n    if array is not None:\n        for index, item in enumerate(array, start=1):\n            if isinstance(item, dict):\n                records.append((index, item))\n            else:\n                unreadable.append((index, \'not an object\'))\n    else:\n        for number, line in enumerate(lines, start=1):\n            body = line.strip()\n            if not body:\n                continue\n            try:\n                item = json.loads(body)\n            except ValueError as exc:\n                unreadable.append((number, str(exc)))\n                continue\n            if isinstance(item, dict):\n                records.append((number, item))\n            else:\n                unreadable.append((number, \'not an object\'))\n\n    headers = [header for _field, header in JSON_FIELD_HEADERS]\n    rows = []\n    integrity = {}\n    for number, record in records:\n        if record.get(\'record\') == \'header\':\n            continue\n        if \'key\' not in record and \'claim\' not in record:\n            continue\n        cells = []\n        for field, _header in JSON_FIELD_HEADERS:\n            value = record.get(field, \'\')\n            if isinstance(value, (list, tuple)):\n                value = \' \'.join(str(part) for part in value)\n            cells.append(\'\' if value is None else str(value))\n        rows.append((number, cells))\n        integrity[number] = check_row_hash(record)\n\n    if not rows:\n        return [], integrity, unreadable\n    table = Table(path, 0, headers, rows, integrity=integrity)\n    return [table], integrity, unreadable\n'),
            ('        self.matched_line = None\n',
             '        self.matched_line = None\n        # Which ordinals of this claim were routed back, so the\n        # routing file can name the ROW rather than the annotation. A\n        # constant has one row and records None; a display string has\n        # one per numeric claim and records the ordinal being checked\n        # when the finding fired.\n        self.routed_ordinals = []\n        self.current_ordinal = None\n'),
            ('            self.route = route\n',
             "            self.route = route\n        if route == 'SEND BACK':\n            if self.current_ordinal not in self.routed_ordinals:\n                self.routed_ordinals.append(self.current_ordinal)\n"),
            ('    return ()\n',
             '    return ()\n\n\ndef check_row_integrity(claim, table, line_no):\n    """LH -- the returned row\'s do-not-edit fields are unchanged.\n\n    The case is ATTRIBUTION. Without this, a responder who rounds a\n    code value produces an L2b mismatch that reports the CODE as\n    drifted, sending somebody to investigate a constant that never\n    moved. The defect is in the worksheet and the report names the\n    code.\n\n    A markdown table has no integrity map. That is NOT APPLICABLE\n    rather than a pass, and this returns without recording anything --\n    a markdown worksheet cannot fail a check that did not exist when it\n    was written.\n    """\n    if not getattr(table, \'integrity\', None):\n        return\n    status, detail = table.integrity.get(line_no, (\'missing\',\n                                                   \'row not in the \'\n                                                   \'integrity map\'))\n    if status == \'ok\':\n        return\n    code = (\'ROW_HASH_MISSING\' if status == \'missing\'\n            else \'ROW_MODIFIED\')\n    claim.fail(\'LH\', code, \'row %d: %s\' % (line_no, detail), \'SEND BACK\')\n'),
            ('    claim.match_rule = rule\n    # Keyed to the MATCHED row and nothing else. No row, no quote -- a',
             "    claim.match_rule = rule\n\n    # ---- LH: the row's immutable half is intact ----------------------\n    #\n    # Only a JSON return carries a hash, so this reads as NOT\n    # APPLICABLE for markdown and clears nothing there.\n    check_row_integrity(claim, table, line_no)\n    # Keyed to the MATCHED row and nothing else. No row, no quote -- a"),
            ('    addressed = 0\n    for value in values:\n        hits = claim_rows(tables, value, text, token)',
             '    addressed = 0\n    for ordinal, value in enumerate(values, start=1):\n        claim.current_ordinal = ordinal\n        hits = claim_rows(tables, value, text, token)'),
            ('        claim.notes = table.cell(cells, ROLE_NOTES)\n',
             '        claim.notes = table.cell(cells, ROLE_NOTES)\n        check_row_integrity(claim, table, line_no)\n'),
            ('\n    claim.claims_addressed = addressed',
             '\n    # Findings after the loop belong to the annotation, not to one\n    # ordinal, so the routing file names the whole site for them.\n    claim.current_ordinal = None\n    claim.claims_addressed = addressed'),
            ('def load_worksheets(project_dir):\n    """Every worksheet on disk, parsed into tables."""\n    directory = os.path.join(project_dir, WORKSHEET_DIR)',
             'def load_worksheets(project_dir):\n    """Every worksheet on disk, parsed into tables.\n\n    Markdown and JSON both land here as Tables, so nothing downstream\n    knows which format it is reading. `hashes` and `unreadable` are\n    carried per sheet so the run can REPORT what it examined -- a run\n    that says only "no problems" cannot be told from one that read\n    nothing.\n    """\n    directory = os.path.join(project_dir, WORKSHEET_DIR)'),
            ("    for name in sorted(os.listdir(directory)):\n        if not name.endswith('.md'):\n            continue",
             "    for name in sorted(os.listdir(directory)):\n        path = os.path.join(directory, name)\n        if name.endswith('.md'):\n            with open(path, encoding='utf-8', errors='replace') as handle:\n                text = handle.read()\n            sheets[name] = {'path': path,\n                            'tables': parse_tables(name, text),\n                            'format': 'markdown',\n                            'hashes': {},\n                            'unreadable': []}\n            continue"),
            ("            continue\n        path = os.path.join(directory, name)\n        with open(path, encoding='utf-8', errors='replace') as handle:",
             "            continue\n        if not name.endswith(JSON_SUFFIXES):\n            continue\n        with open(path, encoding='utf-8', errors='replace') as handle:"),
            ("            text = handle.read()\n        sheets[name] = {'path': path, 'tables': parse_tables(name, text)}\n    return sheets",
             "            text = handle.read()\n        tables, integrity, unreadable = parse_json_worksheet(name, text)\n        sheets[name] = {'path': path,\n                        'tables': tables,\n                        'format': 'json',\n                        'hashes': integrity,\n                        'unreadable': unreadable}\n    return sheets"),
            ('    return sheets\n',
             '    return sheets\n\n\ndef integrity_summary(worksheets):\n    """(examined, ok, missing, mismatch, unreadable_lines) over JSON."""\n    examined = ok = missing = mismatch = 0\n    unreadable = 0\n    for sheet in worksheets.values():\n        if sheet.get(\'format\') != \'json\':\n            continue\n        unreadable += len(sheet.get(\'unreadable\') or ())\n        for status, _detail in (sheet.get(\'hashes\') or {}).values():\n            examined += 1\n            if status == \'ok\':\n                ok += 1\n            elif status == \'missing\':\n                missing += 1\n            else:\n                mismatch += 1\n    return examined, ok, missing, mismatch, unreadable\n\n\ndef write_routing_file(project_dir, claims):\n    """The keys a later dispatch can re-ask, written for a machine.\n\n    The `sendbacks` selection in worksheet_request_builder.py reads\n    this. A key list is legitimate ONLY when the checker wrote it --\n    never one a person typed -- and the test is whether the list can be\n    regenerated. This one can: it is an output of the run that produced\n    the routing.\n    """\n    keys = []\n    for claim in claims:\n        if claim.route != \'SEND BACK\':\n            continue\n        ordinals = claim.routed_ordinals or [None]\n        for ordinal in ordinals:\n            key = claim.key(ordinal)\n            if key and key not in keys:\n                keys.append(key)\n    payload = {\n        \'written_by\': \'worksheet_checker.py\',\n        \'send_back\': sorted(keys),\n        \'send_back_count\': len(keys),\n    }\n    path = os.path.join(project_dir, ROUTED_PATH)\n    try:\n        os.makedirs(os.path.dirname(path), exist_ok=True)\n        with open(path, \'w\', encoding=\'utf-8\', newline=\'\\n\') as handle:\n            json.dump(payload, handle, indent=2, sort_keys=True)\n            handle.write(\'\\n\')\n    except (IOError, OSError) as exc:\n        return 0, \'could not write %s: %s\' % (ROUTED_PATH, exc)\n    return len(keys), \'\'\n'),
            ("\n    send_back = sum(1 for c in claims if c.route == 'SEND BACK')",
             "\n    routed_written, routing_error = write_routing_file(project_dir, claims)\n    examined, ok, missing, mismatch, unreadable = integrity_summary(\n        worksheets)\n\n    send_back = sum(1 for c in claims if c.route == 'SEND BACK')"),
            ("        'unregistered': len(unregistered),\n    }",
             "        'unregistered': len(unregistered),\n        'hashes_examined': examined,\n        'hashes_ok': ok,\n        'hashes_missing': missing,\n        'hashes_mismatch': mismatch,\n        'json_unreadable_lines': unreadable,\n        'routed_keys_written': routed_written,\n    }"),
            ("                 len(claims) - routed - clean, len(unreached)))\n    summary = ('WORKSHEET CHECK: %d of %d routed, %d clean'",
             '                 len(claims) - routed - clean, len(unreached)))\n\n    # Printed every run, including zero. "N row hashes verified" cannot\n    # print unless the rows were read; silence about it could mean\n    # anything, which is the shape of a check that cannot fail. The\n    # blind spot -- a line that would not parse -- announces on its own\n    # line rather than being dropped.\n    detail += (\'\\n  %d row hash(es) verified: %d ok, %d missing, \'\n               \'%d modified\' % (examined, ok, missing, mismatch))\n    if unreadable:\n        detail += (\'\\n  %d JSON line(s) could not be parsed and were \'\n                   \'NOT checked\' % unreadable)\n    if routing_error:\n        detail += \'\\n  %s\' % routing_error\n    else:\n        detail += (\'\\n  %d key(s) written to %s for re-dispatch\'\n                   % (routed_written, ROUTED_PATH))\n    summary = (\'WORKSHEET CHECK: %d of %d routed, %d clean\''),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile('worksheet_checker.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding worksheet_checker.py).')
        return 1

    staged = []
    total = 0
    notes = []

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was '
                  'built against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. If this patch has already '
                  'run, that is the expected abort -- it is one-shot.')
            return 1

        crlf = b'\r\n' in raw
        text = normalized(raw).decode('utf-8')

        for old, new in spec['edits']:
            count = text.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d.'
                      % (name, count))
                print('       anchor starts: %r' % old[:70])
                print('       Nothing written.')
                return 1
            if non_ascii_count(new):
                print('ERROR: %s -- an inserted block carries '
                      'non-ASCII. Nothing written.' % name)
                return 1
            text = text.replace(old, new)

        out = text.encode('utf-8')
        pre_existing = non_ascii_count(text)
        if pre_existing:
            notes.append('note: %s still holds %d non-ASCII '
                         'character(s) this patch did not reach'
                         % (name, pre_existing))
        else:
            notes.append('note: %s is ASCII-clean' % name)
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-38s %d edit(s)' % (name, count))

    for note in notes:
        print(note)
    print('patch applied (%d bytes)' % total)
    print('')
    print('Next: python test_worksheet_checker.py (expect 105 checks), '
          'then python maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
