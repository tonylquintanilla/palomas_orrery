"""
patch_L276_sites_and_relay_access.py -- two repairs from the 2026-09-02 run.

Built on palomas_orrery 5639a9527edad813c2bd99a23e83a3326c79dcc1 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT DOES

  1. documentation/worksheets/L192_annotated_sites.txt -- corrects ten
     stale line numbers. patch_L254_2 inserted 31 lines into
     venus_visualization_shells.py and 31 into mars_visualization_shells.py,
     and this store anchors its sites by LINE. That is the whole of both
     maintenance-run failures: Worksheet key round trip and Extractor pins.
     Verified: all ten corrected rows mint exactly the keys the pin file
     already holds, so nothing is repinned and no pin is retired.

  2. LEDGER_CONSOLIDATED.md -- opens L-276 (Mode 7 asserts relay models
     have no repo access; they do) and L-277 (the line-anchored site
     store breaks on any insertion, eight more times if L-254 finishes).

  Nothing executable changes. No render, no check logic, no citation.

HOW TO RUN
  Open in VS Code from the palomas_orrery repo root and press Run. It
  takes no arguments and asks no questions. Afterwards, re-run the
  maintenance runner: both failing checkers should pass.

GUARDS
  Both files fingerprinted (MD5 over LF-normalised content); every
  anchor verified to match exactly once BEFORE any write; all-or-nothing.
  Post-conditions read back from disk, and the site rows are re-resolved
  through worksheet_keys.resolve() rather than merely counted.

  No .bak written (safe-file-editing 1.10). Undo is Discard Changes in
  GitHub Desktop.

Module created: September 2, 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

SITES = os.path.join('documentation', 'worksheets', 'L192_annotated_sites.txt')
LEDGER = 'LEDGER_CONSOLIDATED.md'

EXPECTED = {
    SITES:  '9ff25e5df27f032e95f61c61140c7204',
    LEDGER: '2773b3130b11e88f74634bf58079f8e5',
}

# (module, old line, new line, label) -- new lines found by matching the
# source text of each old row in the patched file, then confirmed by
# minting the key and resolving it.
SITE_MOVES = [
    ('venus_visualization_shells.py',  43,  74, 'venus_core_info'),
    ('venus_visualization_shells.py',  62, 100, 'description'),
    ('venus_visualization_shells.py', 339, 391, 'venus_atmosphere_info'),
    ('venus_visualization_shells.py', 437, 503, 'description'),
    ('venus_visualization_shells.py', 528, 594, 'venus_magnetosphere_info'),
    ('venus_visualization_shells.py', 681, 747, 'venus_hill_sphere_info'),
    ('mars_visualization_shells.py',  518, 586, 'mars_upper_atmosphere_info'),
    ('mars_visualization_shells.py',  599, 674, 'mars_magnetosphere_info'),
    ('mars_visualization_shells.py',  713, 788, 'bow_shock_text'),
    ('mars_visualization_shells.py',  850, 925, 'mars_hill_sphere_info'),
]

L276 = """#### [L-276] Mode 7 tells relay partners they cannot read the repo, and they can
<!-- L:276 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/95/1 -->
- **The sentence.** PROJECT_INSTRUCTIONS.md Part 1, Mode 7, Documents as
  handoffs: "the receiving AI has zero independent repo access, so an
  un-anchored document is unverifiable input."
- **It is false for a Claude relay, and this project's own records prove
  it.** RELAY_RESPONSE_L191_survey_fable_20260821.md reports running
  `git ls-remote` against the pinned SHA and doing AST analysis of the
  parsed source. Fable cloned the repo. Tony's ruling 2026-09-02: all the
  models queried here have repo access, and Claude and GPT reach GitHub
  natively.
- **The requirement survives; only its stated reason is wrong.** An
  anchor records which state a document DESCRIBES, and the repo moves.
  Proposed replacement for the clause: *the repo moves, so an un-anchored
  document does not say which state it describes. A partner that can
  fetch needs the anchor to fetch the right bytes; a partner that cannot
  needs it to know what it is reading.* That covers both cases instead of
  assuming the weaker one.
- **One live store.** PROJECT_INSTRUCTIONS.md at the repo root is the
  only file carrying the sentence. Nineteen other hits are archived
  version snapshots (v3_32 through v3_49) and stay as they are. Nothing
  in the gallery repo. Verified at 5639a952.
**Note:** the failure that surfaced it is worth keeping. A session read
the L-191 relay response, which says plainly that Fable cloned the repo,
and then repeated the blanket sentence anyway -- a general claim in a
document trusted over specific evidence already in hand. Same shape as
trusting a handoff over the render, one layer up.
- Tony-action (do): run the PROJECT_INSTRUCTIONS.md patch when it is
  built; it is a one-clause edit plus a version bump.
**Gap:** patch not yet built. Wording above is proposed, not approved.
**Ref:** PROJECT_INSTRUCTIONS.md Part 1 Mode 7;
documentation/RELAY_RESPONSE_L191_survey_fable_20260821.md; L-191.

"""

L277 = """#### [L-277] The L-192 site store anchors by line number, so any insertion breaks two checkers
<!-- L:277 status:OPEN upd:2026-09-02 section:A flag: rice:3/3/90/2 -->
- **What happened 2026-09-02.** `patch_L254_2` inserted 31 lines into
  venus_visualization_shells.py and 31 into mars_visualization_shells.py
  -- comments and docstrings only, nothing executable. The maintenance
  run then failed two checkers: Worksheet key round trip (1 unresolved)
  and Extractor pins (10 PIN UNMATCHED). Same cause, one store.
- **The mechanism.** documentation/worksheets/L192_annotated_sites.txt
  holds `module TAB line TAB label` rows, generated once from
  WORKSHEET_CHECK.md at 305b269 and hand-maintained since. Nothing
  regenerates it. `key_for_site()` reads the line, asks
  `enclosing_name()` which def contains it, and mints
  `module::enclosing::label`. Move the lines and the enclosing scope
  changes: venus line 62 was a `description` inside
  `create_venus_core_shell` and now lands in a comment block, where no
  function encloses it, so the key degrades to
  `venus_visualization_shells.py::description` and resolves to nothing.
- **The checkers were right and the repin would have been wrong.** The
  Extractor pins failure printed a REPIN block that silently omits all
  ten venus and mars rows -- accepting it would have retired ten live
  pins to clear a red light. Fixed by correcting the ten line numbers
  instead; all ten then mint exactly the keys the pin file already holds.
- **THE FORWARD COST IS THE ITEM.** L-254 has 55 dead builders left
  across eris, jupiter, moon, neptune, planet9, pluto, saturn, solar and
  uranus. Every one of those nine modules that also holds an L-192 site
  will break these two checkers the same way. Four of the nine do:
  eris, mercury-adjacent moon, pluto and solar all appear in the pin
  file. So the annotation sweep and this store are coupled, and the
  coupling is currently discovered at run time by a red light.
**Note:** two shapes to weigh, and this is a design call rather than a
method one. (a) Every L-254 slice updates the site store in the same
patch -- cheap, but it is a rule a session has to remember. (b) The
store stops anchoring by line and anchors by enclosing name plus label,
which is what the key already is -- more work once, nothing to remember
after. Claude's read is (b), because (a) is a convention that fails
silently the first time somebody forgets, and the whole point of this
store is to not fail silently.
- Tony-action (decide): (a) update the store per slice, or (b) reanchor
  the store to names.
**Gap:** decision, then a patch. The 2026-09-02 breakage is already
repaired; this item is about the next eight.
**Ref:** worksheet_keys.py `key_for_site` / `enclosing_name` /
`parse_sites_doc`; documentation/worksheets/L192_annotated_sites.txt;
documentation/worksheets/L192_extractor_pins.txt; L-192; L-254.

"""

LEDGER_ANCHOR = ('#### [L-275] The dashboard cannot launch a Node tool, '
                 'so three gallery smoke suites have no button\n')


def fail(msg):
    print('')
    print('FAILURE: %s' % msg)
    print('NOTHING was written. No file on disk has changed.')
    print('If a previous run did write, undo is Discard Changes in GitHub Desktop.')
    sys.exit(1)


def read_lf(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return (raw.replace(b'\r\n', b'\n') if was_crlf else raw), was_crlf


def build_edits():
    site_edits = []
    for module, old, new, label in SITE_MOVES:
        a = '%s\t%d\t%s\n' % (module, old, label)
        b = '%s\t%d\t%s\n' % (module, new, label)
        site_edits.append((a, b))
    ledger_edits = [(LEDGER_ANCHOR, L276 + L277 + LEDGER_ANCHOR)]
    return {SITES: site_edits, LEDGER: ledger_edits}


def main():
    print('patch_L276 -- L-192 site store repair + two ledger items')
    print('=' * 66)

    edits = build_edits()

    for fn, pairs in edits.items():
        for _, new in pairs:
            try:
                new.encode('ascii')
            except UnicodeEncodeError as exc:
                fail('non-ASCII in replacement text for %s: %s' % (fn, exc))

    if 'L:276' in read_lf(LEDGER)[0].decode('utf-8', 'replace'):
        fail('LEDGER_CONSOLIDATED.md already carries L-276. This patch has run.')

    staged = {}
    for fn, pairs in edits.items():
        if not os.path.exists(fn):
            fail('%s not found. Run this from the palomas_orrery repo root.' % fn)

        content, was_crlf = read_lf(fn)
        actual = hashlib.md5(content).hexdigest()
        if actual != EXPECTED[fn]:
            fail('BASE MOVED for %s.\n  expected %s\n  found    %s\n'
                 '  Built against 5639a952. A size delta of about one byte per\n'
                 '  line is CRLF, not content.' % (fn, EXPECTED[fn], actual))
        print('  %-46s fingerprint matches%s'
              % (fn, ' [CRLF]' if was_crlf else ''))

        out = content
        for anchor, new in pairs:
            a = anchor.encode('ascii')
            n = out.count(a)
            if n != 1:
                fail('anchor matched %d times (expected 1) in %s:\n    %r'
                     % (n, fn, anchor[:80]))
            out = out.replace(a, new.encode('ascii'))
        staged[fn] = (out.replace(b'\n', b'\r\n') if was_crlf else out, len(pairs))

    print('  all anchors verified, %d edits staged' % sum(v[1] for v in staged.values()))

    for fn, (data, n_edits) in staged.items():
        with open(fn, 'wb') as f:
            f.write(data)
        print('  wrote %-46s %d edits' % (fn, n_edits))

    # --- Post-conditions, read from disk ---------------------------------
    print('')
    print('Post-conditions (read back from disk):')

    ledger = read_lf(LEDGER)[0].decode('utf-8', 'replace')
    for handle in ('L:276', 'L:277'):
        print('  ledger carries %-6s %s' % (handle, handle in ledger))
    if 'L:276' not in ledger or 'L:277' not in ledger:
        fail('ledger items did not land')

    # The real check: re-resolve every corrected row through the module
    # the checkers use. Counting rows would pass whether or not the
    # numbers are right.
    print('')
    print('  Re-resolving the ten corrected sites through worksheet_keys:')
    sys.path.insert(0, os.getcwd())
    try:
        import worksheet_keys as wk
    except Exception as exc:
        print('  could not import worksheet_keys (%s) -- run the maintenance'
              ' runner to confirm instead.' % exc)
        return

    sources = {}
    bad = []
    for module, _old, new, label in SITE_MOVES:
        if module not in sources:
            sources[module] = open(module, encoding='utf-8').read()
        key = wk.key_for_site(module, sources[module], new, label=label)
        line, reason = wk.resolve(key, sources)
        status = 'OK  ' if line else 'FAIL'
        if not line:
            bad.append((key, reason))
        print('    %s %s' % (status, key))
    if bad:
        print('')
        print('POST-CONDITION FAILED. %d site(s) still unresolved.' % len(bad))
        print('Undo is Discard Changes in GitHub Desktop, then report this.')
        sys.exit(1)

    print('')
    print('DONE. Ten site rows corrected, L-276 and L-277 opened.')
    print('')
    print('Next: re-run the maintenance runner. Worksheet key round trip and')
    print('Extractor pins should both pass. Do NOT bump EXTRACTOR_VERSION and')
    print('do NOT accept the REPIN block the failure printed -- it drops all')
    print('ten venus and mars pins, which is retiring live pins to clear a')
    print('red light. Nothing about the extractor changed; only line numbers.')
    print('')
    print('Then commit, push, and record the SHA on L-254, L-276 and L-277.')


if __name__ == '__main__':
    main()
