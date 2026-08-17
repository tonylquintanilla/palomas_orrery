"""patch_L201_1_selection_and_json.py -- L-201 and L-202. Ask the
builder for fewer rows, and emit the request as JSON.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
worksheet_request_builder.py), open it in VS Code, and click Run.

    python patch_L201_1_selection_and_json.py

WHAT IT DOES
------------
Two ledger items in one patch, because they edit the same two files and
two patches fingerprinting one file would abort the second.

L-201 -- SELECTION. build() returns the whole annotated corpus and
main() renders every row, so producing a pilot slice today means
hand-editing the generated file. This adds named selections: entries in
the module, each a name, a purpose, and a rule. main() lists them at the
prompt; a blank answer means the whole corpus, so the previous behaviour
is the default. Three ship: `all`, `constants_new` (the pilot's 23 rows),
and `sendbacks`, which reads a checker-written key list.

A selection is CODE, not typing. A pilot chosen by hand is a one-off no
matter how carefully it is chosen, because nothing records why those rows
and nothing can produce them again.

L-202 -- JSON. The request is emitted as JSON Lines, one complete object
per line, alongside the markdown. Line-delimited on purpose: a single
JSON document fails whole-file, and one object per line makes a truncated
return salvageable object by object. Markdown is written every run as the
fallback and its parser stays live permanently, because the seventeen
historical worksheets are markdown.

Each JSON row carries an eight-character hash over the fields a responder
must not edit. The case is ATTRIBUTION, not tamper-proofing: without it,
a responder who rounds a code value produces an L2b mismatch that reports
the CODE as drifted, sending somebody to investigate a constant that
never moved.

BLOCKER 8, CLOSED IN PASSING
----------------------------
Both formats now print the accepted verdict words, READ FROM
worksheet_checker.VERDICT_TOKENS rather than retyped. A list written out
in the builder would be a second store of the same fact, free to drift
from the registry the checker enforces -- and a request naming a word the
checker rejects sends a responder to write UNREADABLE. This was on the
open list as blocker 8 with no ruling outstanding; the header was being
rewritten anyway.

WHAT THE RATCHET RESTS ON, CORRECTED
------------------------------------
The L-196 refusal must not be bypassable by selecting around a bad file.
The first version of this work claimed the ORDER of statements in main()
enforced that. A mutation test disproved it: reordering so selection runs
first changes nothing. What enforces it is the collection the refusal
loop reads -- the whole corpus, never the selected subset. The one-word
mutation that DOES bypass it now has a test pinned against it.

PERMANENT vs DISPOSABLE
-----------------------
This script is disposable and one-shot -- it guards on a fingerprint of a
tree that stops existing the moment it succeeds. What it installs is
permanent: the selection mechanism, the JSON emitter, the row hash, the
verdict vocabulary in both formats, and 20 new tests.

SAFETY
------
All-or-nothing across BOTH files. Each is fingerprinted
(CRLF-normalized) and every anchor must match exactly once before
anything is written. Any mismatch aborts with nothing written. Each
file's own line endings are preserved.

Success: one `ok` line per file, then `patch applied (N bytes)`.
Failure: a single `ERROR:` or `ANCHOR FAIL` line; nothing is written.

AFTER IT RUNS
-------------
    python test_worksheet_request_builder.py     (expect 61 checks)
    python maintenance_run.py
"""

import hashlib
import os
import sys


EDITS = {
    'worksheet_request_builder.py': {
        'fp': '0e9fcd2001e6e0c3b6d07522e75ec38f',
        'edits': [
            ('\nimport os',
             '\nimport hashlib\nimport json\nimport os'),
            ("\ndef build(project_dir='.'):",
             '\n# ============================================================\n# SELECTION -- ASKING THE BUILDER FOR FEWER ROWS (L-201)\n# ============================================================\n#\n# A selection is CODE, not typing. Each entry below is a name, a\n# one-line statement of what it is for, and a rule. A pilot chosen by\n# hand is a one-off no matter how carefully it is chosen, because\n# nothing records why those rows and nothing can produce them again.\n# An entry here is reviewable in a diff, pinned to a SHA, and\n# reproducible by anyone who runs the tool.\n#\n# Blank at the prompt means the whole corpus, so the behaviour before\n# this existed is still the default.\n#\n# WHERE SELECTION HAPPENS: after the L-196 refusal, never before.\n# Excluding a site must never excuse an unmarked continuation, and a\n# ratchet with a bypass is not a ratchet.\n#\n# The ORDER in main() is not what enforces that, and saying so was\n# wrong when first written here. What enforces it is the collection the\n# refusal loop reads: it iterates the whole corpus, never the selected\n# subset. Reordering main() so selection runs first changes nothing --\n# measured, by doing it. The mutation that DOES bypass the ratchet is\n# one line, `for request in selected`, and it writes a request over a\n# corpus holding an unmarked continuation. test_worksheet_request_\n# builder.py pins the invariant against exactly that edit.\n\n# The checker writes this. A selection may read a key list ONLY when\n# the checker wrote it -- never one a person typed. The test is whether\n# the list can be regenerated: a checker-written list can, a remembered\n# one cannot.\nROUTED_PATH = os.path.join(\'data\', \'worksheet_routed.json\')\n\n\nclass Selection(object):\n    """One named way to choose rows.\n\n    `rule` is a predicate over a Request, or None for the whole corpus.\n    `keys_from` names a checker-written JSON file whose keys are the\n    selection; it is read at run time, and a missing file is an ERROR\n    rather than an empty result.\n    """\n\n    def __init__(self, name, why, rule=None, keys_from=None):\n        self.name = name\n        self.why = why\n        self.rule = rule\n        self.keys_from = keys_from\n\n\ndef _file_of(request):\n    return request.where.split(\':\')[0]\n\n\ndef _is_constants_new(request):\n    return _file_of(request) == \'constants_new.py\'\n\n\nSELECTIONS = (\n    Selection(\'all\', \'the whole annotated corpus\'),\n    Selection(\'constants_new\',\n              \'constants_new.py only -- the pilot slice (L-201). Its \'\n              \'branch coverage is a property of the file, not of \'\n              \'anyone\\\'s judgement about which rows are interesting.\',\n              rule=_is_constants_new),\n    Selection(\'sendbacks\',\n              \'rows the checker last routed SEND BACK, read from %s\'\n              % ROUTED_PATH,\n              keys_from=ROUTED_PATH),\n)\n\n\ndef routed_keys(project_dir, path):\n    """(keys, error) from a checker-written routing file.\n\n    Returns a set of keys, or an error string. A missing or unreadable\n    file is an error and stops the run: selecting from a list that is\n    not there would otherwise produce an empty request that looks like\n    a finished one.\n    """\n    full = os.path.join(project_dir, path)\n    if not os.path.isfile(full):\n        return None, (\'%s does not exist. Run worksheet_checker.py \'\n                      \'first -- it writes the routing file this \'\n                      \'selection reads.\' % path)\n    try:\n        with open(full, encoding=\'utf-8\') as handle:\n            data = json.load(handle)\n    except (IOError, OSError, ValueError) as exc:\n        return None, \'%s could not be read: %s\' % (path, exc)\n    keys = data.get(\'send_back\') if isinstance(data, dict) else None\n    if not isinstance(keys, list):\n        return None, (\'%s carries no "send_back" list. It was written \'\n                      \'by something other than the checker, or by an \'\n                      \'older version of it.\' % path)\n    return set(str(key) for key in keys), None\n\n\ndef apply_selection(selection, requests, project_dir=\'.\'):\n    """(selected, error) for one named selection."""\n    if selection.keys_from:\n        keys, error = routed_keys(project_dir, selection.keys_from)\n        if error:\n            return None, error\n        return [r for r in requests if r.key in keys], None\n    if selection.rule is None:\n        return list(requests), None\n    return [r for r in requests if selection.rule(r)], None\n\n\n# ============================================================\n# ROW INTEGRITY HASH (L-202)\n# ============================================================\n#\n# The case is ATTRIBUTION, not tamper-proofing.\n#\n# The request tells a responder not to edit the Key, Claim or Code\n# value columns, and nothing verifies it. A responder who rounds a code\n# value produces a row that looks fine, and the checker\'s L2b layer\n# then compares the code NOW against the value the worksheet recorded,\n# finds a mismatch, and reports that the CODE drifted -- sending\n# somebody to investigate a constant that never moved. The defect is in\n# the worksheet and the report names the code.\n#\n# Eight hex characters over the three fields, joined and\n# whitespace-normalized, let the checker say the true thing instead:\n# this row\'s immutable half was modified.\n#\n# A MISSING hash FAILS the row on the checker side. A hash that quietly\n# passes when absent is a check that cannot fail.\n\nHASH_CHARS = 8\n\n\ndef row_hash(key, claim, code_value):\n    """Short digest over the fields a responder must not edit."""\n    parts = []\n    for field in (key, claim, code_value):\n        parts.append(\' \'.join(str(field if field is not None else \'\').split()))\n    blob = \'\\n\'.join(parts).encode(\'utf-8\')\n    return hashlib.sha256(blob).hexdigest()[:HASH_CHARS]\n\n\ndef verdict_vocabulary():\n    """The accepted verdict words, grouped, read from the checker.\n\n    Read rather than retyped. A list written out here would be a second\n    store of the same fact, free to drift from the registry the checker\n    actually enforces -- and a request naming a word the checker\n    rejects sends a responder to write UNREADABLE.\n    """\n    groups = {}\n    for token in sorted(wc.VERDICT_TOKENS):\n        own, scope = wc.VERDICT_TOKENS[token]\n        groups.setdefault(own, {\'words\': [], \'scope\': scope})\n        groups[own][\'words\'].append(token)\n    return [(own, groups[own][\'words\'], groups[own][\'scope\'])\n            for own in sorted(groups)]\n\n\ndef build(project_dir=\'.\'):'),
            ('\ndef render(requests, batch, sha, repo_url, skipped):\n    """The request file, as markdown the checker can read back."""',
             '\ndef render(requests, batch, sha, repo_url, skipped, selection,\n           corpus_size):\n    """The request file, as markdown the checker can read back."""'),
            ("               '`module.py::enclosing::label::cN`.' % wk.EXTRACTOR_VERSION)\n    out.append('')",
             "               '`module.py::enclosing::label::cN`.' % wk.EXTRACTOR_VERSION)\n    out.append('')\n    out.append('Selection: `%s` -- %s' % (selection.name, selection.why))\n    out.append('')\n    out.append('%d of %d rows in the corpus. The KEY identifies a row; '\n               'the number in the first column is assigned by position '\n               'in this file and means nothing outside it.'\n               % (len(requests), corpus_size))\n    out.append('')"),
            ("               'interpretation this system is built to avoid.')\n    out.append('')",
             "               'interpretation this system is built to avoid.')\n    out.append('')\n\n    # Read from the checker's own registry rather than retyped here. A\n    # list written out in this file would be free to drift from the one\n    # the checker enforces, and a request naming a word the checker\n    # rejects sends a responder to write UNREADABLE.\n    out.append('## The accepted verdict words')\n    out.append('')\n    out.append('Anything outside this list is read as unclassified and '\n               'the row comes back.')\n    out.append('')\n    for own, words, scope in verdict_vocabulary():\n        answers = {'value': 'the value only',\n                   'citation': 'the citation only'}.get(\n                       scope, 'whichever question the column asks')\n        out.append('- **%s** -- %s (answers %s)'\n                   % (own, ', '.join('`%s`' % w for w in words), answers))\n    out.append('')"),
            ('\ndef main():',
             '\ndef render_json(requests, batch, sha, repo_url, skipped, selection,\n                corpus_size):\n    """The request as JSON Lines -- one complete object per line.\n\n    Line-delimited on purpose. A single JSON document fails whole-file:\n    one trailing comma, one smart quote, one generation truncated at\n    row 19 of 23, and nothing parses. With one object per line a\n    truncated return is salvageable object by object, which is the only\n    cheap hedge against the failure mode markdown does not have.\n    (Tony\'s ruling 2026-08-17: send the JSON; if a return fails to\n    parse, send the markdown. Markdown stays live permanently -- the\n    seventeen historical worksheets are markdown.)\n\n    Line 1 is the header. Every later line is one row. The `record`\n    field says which.\n\n    The answer fields are present and empty, so a responder fills them\n    in place rather than inventing a shape.\n    """\n    lines = []\n    header = {\n        \'record\': \'header\',\n        \'batch\': batch,\n        \'built_on_sha\': sha,\n        \'repo\': repo_url,\n        \'extractor_version\': wk.EXTRACTOR_VERSION,\n        \'key_format\': \'module.py::enclosing::label::cN\',\n        \'selection\': selection.name,\n        \'selection_why\': selection.why,\n        \'rows_selected\': len(requests),\n        \'corpus_size\': corpus_size,\n        \'row_hash\': (\'sha256 over key, claim and code value, first %d \'\n                     \'hex characters. Do not edit those three fields; \'\n                     \'the checker recomputes this and a row whose hash \'\n                     \'is missing or wrong is returned rather than \'\n                     \'read.\' % HASH_CHARS),\n        \'identifies_rows\': (\'The KEY identifies a row. The id (R1, R2, \'\n                            \'...) is assigned by position in this file \'\n                            \'and means nothing outside it.\'),\n        \'answer_fields\': [\'your_value\', \'source\', \'value_correct\',\n                          \'citation_correct\', \'notes\'],\n        \'instructions\': [\n            \'your_value -- the number the source states. If sources \'\n            \'disagree, give the range AND the rule you used to reduce \'\n            \'it (for example "2.5-2.7, took the midpoint to two \'\n            \'significant figures").\',\n            \'source -- the authority you consulted, specific enough to \'\n            \'find again.\',\n            \'value_correct -- about the NUMBER only.\',\n            \'citation_correct -- about the code\\\'s cited source only, \'\n            \'carried on each row as "cited". Answer it separately from \'\n            \'the value: a right number under a wrong authority is a \'\n            \'real finding and one token cannot say it.\',\n            \'notes -- anything a token cannot carry. The checker reads \'\n            \'notes as prose for a human, never as a verdict.\',\n            \'One token per verdict field. A field holding a token plus \'\n            \'a qualification is reported as unclassified rather than \'\n            \'read, because guessing which half you meant is the \'\n            \'interpretation this system is built to avoid.\',\n        ],\n        \'verdict_tokens\': [\n            {\'means\': own, \'words\': words, \'answers\': scope}\n            for own, words, scope in verdict_vocabulary()\n        ],\n    }\n    if skipped:\n        header[\'not_reached\'] = [\n            {\'file\': name, \'reason\': reason} for name, reason in skipped]\n    lines.append(json.dumps(header, sort_keys=True))\n\n    for request in requests:\n        row = {\n            \'record\': \'row\',\n            \'id\': request.row_id,\n            \'key\': request.key,\n            \'claim\': request.claim,\n            \'code_value\': request.code_value,\n            \'hash\': row_hash(request.key, request.claim,\n                             request.code_value),\n            \'site\': request.where,\n            \'cited\': list(request.cited),\n            \'context_only\': list(request.context),\n            \'your_value\': \'\',\n            \'source\': \'\',\n            \'value_correct\': \'\',\n            \'citation_correct\': \'\',\n            \'notes\': \'\',\n        }\n        if not request.cited:\n            row[\'cited_note\'] = (\'none recorded. Answer \'\n                                 \'citation_correct as "no" and say so \'\n                                 \'in notes.\')\n        if request.problems:\n            row[\'malformed_continuation\'] = list(request.problems)\n        lines.append(json.dumps(row, sort_keys=True))\n\n    return \'\\n\'.join(lines) + \'\\n\'\n\ndef choose_selection():\n    """(selection, error) from the prompt.\n\n    Numbered, because Tony runs this with VS Code\'s Run button and\n    answers in the panel -- there are no command-line flags to pass.\n    Blank means the whole corpus, so the behaviour before selection\n    existed is still the default.\n    """\n    print(\'\')\n    print(\'Which rows?\')\n    for index, selection in enumerate(SELECTIONS, start=1):\n        print(\'  %d. %s -- %s\' % (index, selection.name, selection.why))\n    answer = input(\'Selection [1]: \').strip()\n    if not answer:\n        return SELECTIONS[0], None\n    try:\n        number = int(answer)\n    except ValueError:\n        return None, (\'"%s" is not one of the numbers above. Nothing \'\n                      \'written.\' % answer)\n    if not 1 <= number <= len(SELECTIONS):\n        return None, (\'%d is outside 1-%d. Nothing written.\'\n                      % (number, len(SELECTIONS)))\n    return SELECTIONS[number - 1], None\n\n\ndef main():'),
            ("    requests, skipped = build(project_dir)\n    for index, request in enumerate(requests, start=1):\n        request.row_id = 'R%d' % index\n",
             '    requests, skipped = build(project_dir)\n'),
            ("\n    batch = input('Batch name (e.g. batch3_gas_giants): ').strip()",
             '\n    selection, error = choose_selection()\n    if error:\n        print(error)\n        return 1\n\n    selected, error = apply_selection(selection, requests, project_dir)\n    if error:\n        print(\'ERROR: %s\' % error)\n        print(\'Nothing written.\')\n        return 1\n\n    # A selection matching nothing must refuse, not write an empty\n    # request. An empty worksheet is indistinguishable from a finished\n    # one once it is out of the room.\n    if not selected:\n        print(\'Selection "%s" matched 0 of %d rows. Nothing written.\'\n              % (selection.name, len(requests)))\n        return 1\n\n    print(\'Selection "%s": %d of %d rows.\'\n          % (selection.name, len(selected), len(requests)))\n\n    # Numbered AFTER selection, because the id is positional within the\n    # file being written. The key is what identifies a row anywhere\n    # else, and the request says so.\n    for index, request in enumerate(selected, start=1):\n        request.row_id = \'R%d\' % index\n\n    batch = input(\'Batch name (e.g. batch3_gas_giants): \').strip()'),
            ('\n    text = render(requests, batch, sha, repo_url, skipped)\n    if not os.path.isdir(OUTPUT_DIR):',
             '\n    # Both views, one producer. The JSON is what goes out; the markdown\n    # is the fallback if a return will not parse, and it costs nothing\n    # to write now rather than re-running later. Neither is derived\n    # from the other -- both read the same Request list, so there is no\n    # second source of truth to drift.\n    text = render(selected, batch, sha, repo_url, skipped, selection,\n                  len(requests))\n    payload = render_json(selected, batch, sha, repo_url, skipped,\n                          selection, len(requests))\n\n    if not os.path.isdir(OUTPUT_DIR):'),
            ("        os.makedirs(OUTPUT_DIR)\n    path = os.path.join(OUTPUT_DIR, 'REQUEST_%s.md' % batch)\n    if os.path.exists(path):\n        print('%s already exists. Nothing written.' % path)\n        return 1\n    with open(path, 'wb') as handle:\n        handle.write(text.encode('ascii', 'replace'))",
             "        os.makedirs(OUTPUT_DIR)\n    md_path = os.path.join(OUTPUT_DIR, 'REQUEST_%s.md' % batch)\n    json_path = os.path.join(OUTPUT_DIR, 'REQUEST_%s.jsonl' % batch)\n    for path in (md_path, json_path):\n        if os.path.exists(path):\n            print('%s already exists. Nothing written.' % path)\n            return 1\n    with open(md_path, 'wb') as handle:\n        handle.write(text.encode('ascii', 'replace'))"),
            ("        handle.write(text.encode('ascii', 'replace'))\n    print('Wrote %s (%d rows).' % (path, len(requests)))\n    return 0",
             "        handle.write(text.encode('ascii', 'replace'))\n    with open(json_path, 'wb') as handle:\n        handle.write(payload.encode('ascii', 'replace'))\n\n    print('Wrote %s (%d rows).' % (json_path, len(selected)))\n    print('Wrote %s (%d rows) -- the fallback.' % (md_path, len(selected)))\n    print('Send the .jsonl. If a return will not parse, send the .md '\n          'and say so, so the pilot records which format was used.')\n    return 0"),
        ],
    },
    'test_worksheet_request_builder.py': {
        'fp': '5d721086ee25ac35e6a6686440557b04',
        'edits': [
            ('\nimport os',
             '\nimport json\nimport os'),
            ('\nimport worksheet_request_builder as b',
             '\nimport worksheet_checker as wc\nimport worksheet_request_builder as b'),
            ('\ndef main():',
             '\ndef test_selection(project_dir):\n    """A selection narrows the corpus and refuses to select nothing."""\n    requests, _skipped = b.build(project_dir)\n\n    every, error = b.apply_selection(b.SELECTIONS[0], requests, project_dir)\n    check(\'selection: "all" returns the whole corpus\',\n          len(every) == len(requests) and error is None,\n          \'%d of %d, error %r\' % (len(every), len(requests), error))\n\n    pilot = [s for s in b.SELECTIONS if s.name == \'constants_new\'][0]\n    chosen, error = b.apply_selection(pilot, requests, project_dir)\n    check(\'selection: the pilot slice is one file\',\n          chosen and error is None\n          and set(r.where.split(\':\')[0] for r in chosen)\n          == {\'constants_new.py\'},\n          \'%d rows from %s\'\n          % (len(chosen), sorted(set(r.where.split(\':\')[0]\n                                     for r in chosen))))\n    check(\'selection: the pilot slice is a strict subset\',\n          0 < len(chosen) < len(requests),\n          \'%d of %d\' % (len(chosen), len(requests)))\n\n    nothing = b.Selection(\'nothing\', \'test\', rule=lambda r: False)\n    empty, error = b.apply_selection(nothing, requests, project_dir)\n    check(\'selection: a rule matching nothing returns nothing\',\n          empty == [] and error is None, repr(error))\n\n    # The refusal in main() turns that empty result into a stop. Pinned\n    # here as a fact about the source, because an empty request is\n    # indistinguishable from a finished one once it has left the room,\n    # and the guard is four lines that a tidy-up could remove.\n    source = open(os.path.join(project_dir,\n                               \'worksheet_request_builder.py\'),\n                  encoding=\'utf-8\').read()\n    check(\'selection: main refuses to write an empty request\',\n          \'matched 0 of %d rows\' in source\n          or \'matched 0 of\' in source,\n          \'the empty-selection guard is missing from main()\')\n\n\ndef test_ratchet_is_not_bypassed_by_selection(project_dir):\n    """The L-196 refusal reads the CORPUS, never the selection.\n\n    This is the invariant, and it is not the order of statements in\n    main(). Reordering so selection runs first changes nothing, because\n    the refusal loop iterates every request the corpus produced. The\n    mutation that DOES bypass it is a single word -- iterating the\n    selected subset instead -- which lets a request go out over a\n    corpus holding an unmarked continuation, as long as the offending\n    file was not selected.\n\n    Pinned against the source rather than by running main(), which\n    prompts for input. A grep is a weak test in general; it is the\n    right one here because the defect being pinned IS a one-word edit\n    at a known line.\n    """\n    source = open(os.path.join(project_dir,\n                               \'worksheet_request_builder.py\'),\n                  encoding=\'utf-8\').read()\n    start = source.find(\'    blocked = {}\')\n    check(\'ratchet: the refusal block is still in main()\', start != -1,\n          \'blocked = {} not found\')\n    if start == -1:\n        return\n    window = source[start:start + 400]\n    check(\'ratchet: the refusal reads the whole corpus\',\n          \'for request in requests:\' in window,\n          \'the refusal iterates something other than `requests`: %r\'\n          % window[:120])\n    check(\'ratchet: the refusal does not read the selection\',\n          \'for request in selected:\' not in window,\n          \'the refusal iterates the selected subset -- a selection can \'\n          \'now exclude a site and excuse its unmarked continuation\')\n\n\ndef test_row_hash():\n    """The hash moves when a do-not-edit field moves, and not otherwise."""\n    base = b.row_hash(\'constants_new.py::ROCHE_LIMIT_RADII\',\n                      \'ROCHE_LIMIT_RADII\', \'3.45\')\n    check(\'hash: eight characters\', len(base) == 8, base)\n    check(\'hash: a rounded code value changes it\',\n          base != b.row_hash(\'constants_new.py::ROCHE_LIMIT_RADII\',\n                             \'ROCHE_LIMIT_RADII\', \'3.450\'), base)\n    check(\'hash: a reflowed key changes it\',\n          base != b.row_hash(\'constants_new.py::ROCHE_LIMIT\',\n                             \'ROCHE_LIMIT_RADII\', \'3.45\'), base)\n    check(\'hash: whitespace alone does not change it\',\n          base == b.row_hash(\' constants_new.py::ROCHE_LIMIT_RADII \',\n                             \'ROCHE_LIMIT_RADII\', \'  3.45\'), base)\n\n\ndef test_json_lines(project_dir):\n    """Every line of the emitted request parses on its own."""\n    requests, skipped = b.build(project_dir)\n    pilot = [s for s in b.SELECTIONS if s.name == \'constants_new\'][0]\n    chosen, _error = b.apply_selection(pilot, requests, project_dir)\n    for index, request in enumerate(chosen, start=1):\n        request.row_id = \'R%d\' % index\n    payload = b.render_json(chosen, \'test_batch\', \'deadbeef\',\n                            \'https://example.invalid\', skipped, pilot,\n                            len(requests))\n\n    lines = payload.strip().split(\'\\n\')\n    parsed = []\n    bad = \'\'\n    for line in lines:\n        try:\n            parsed.append(json.loads(line))\n        except ValueError as exc:\n            bad = \'%s: %s\' % (exc, line[:60])\n            break\n    check(\'json: every line parses independently\', not bad, bad)\n    if bad:\n        return\n\n    check(\'json: one header plus one line per row\',\n          len(parsed) == len(chosen) + 1,\n          \'%d lines for %d rows\' % (len(parsed), len(chosen)))\n    check(\'json: the first record is the header\',\n          parsed[0].get(\'record\') == \'header\', repr(parsed[0])[:80])\n    check(\'json: the header states the selection and the counts\',\n          parsed[0].get(\'selection\') == \'constants_new\'\n          and parsed[0].get(\'rows_selected\') == len(chosen)\n          and parsed[0].get(\'corpus_size\') == len(requests),\n          repr(parsed[0].get(\'selection\')))\n\n    rows = parsed[1:]\n    check(\'json: every row carries a hash\',\n          all(len(r.get(\'hash\', \'\')) == 8 for r in rows),\n          repr([r.get(\'id\') for r in rows if len(r.get(\'hash\', \'\')) != 8]))\n    check(\'json: the hash matches the row it sits on\',\n          all(r.get(\'hash\') == b.row_hash(r.get(\'key\', \'\'),\n                                          r.get(\'claim\', \'\'),\n                                          r.get(\'code_value\', \'\'))\n              for r in rows),\n          \'a row hash is missing or does not match its own fields\')\n    check(\'json: answer fields are present and empty\',\n          all(r.get(field) == \'\' for r in rows\n              for field in (\'your_value\', \'source\', \'value_correct\',\n                            \'citation_correct\', \'notes\')),\n          \'an answer field is missing or pre-filled\')\n\n    # The vocabulary is read from the checker, so a token the checker\n    # accepts and the request does not name would be a drift the pilot\n    # would discover the hard way.\n    named = set()\n    for group in parsed[0].get(\'verdict_tokens\', []):\n        named.update(group.get(\'words\', []))\n    check(\'json: the request names every token the checker accepts\',\n          named == set(wc.VERDICT_TOKENS),\n          \'request %r vs checker %r\'\n          % (sorted(named), sorted(wc.VERDICT_TOKENS)))\n\n\ndef main():'),
            ("    print('=' * 70)\n    print('BUILDER MARKER JOIN TESTS -- does it join, and can it fail? '\n          '(L-195)')\n    print('=' * 70)",
             "    print('=' * 70)\n    print('BUILDER TESTS -- joins, selection, hash, JSON '\n          '(L-195 / L-201 / L-202)')\n    print('=' * 70)"),
            ('    test_live_corpus(project_dir)\n',
             '    test_live_corpus(project_dir)\n    test_selection(project_dir)\n    test_ratchet_is_not_bypassed_by_selection(project_dir)\n    test_row_hash()\n    test_json_lines(project_dir)\n'),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def non_ascii_count(text):
    return sum(1 for ch in text if ord(ch) > 127)


def main():
    if not os.path.isfile('worksheet_request_builder.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding worksheet_request_builder.py).')
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
    print('Next: python test_worksheet_request_builder.py '
          '(expect 61 checks), then python maintenance_run.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
