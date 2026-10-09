"""
patch_L412_2_decisions_20261008.py

Records the rulings of the decisions session of October 8, 2026 in
LEDGER_CONSOLIDATED.md and on documentation/WHERE_WE_ARE.md. Records
only: no code file, no skill and no served file is touched.

HOW TO RUN (Tony): save this file in the orrery repo root folder (the
folder that holds LEDGER_CONSOLIDATED.md), open it in VS Code and click
Run. The command it runs is:  python patch_L412_2_decisions_20261008.py
It asks no questions.

What it does, by ledger handle:
  - L-216 (the swap retry): CLOSED, with Tony's no-pause trial noted.
    Its loose ends go to L-351 (what each skill is owed) and L-395.
  - L-252 (an incomplete verdict is not a confirmation): CLOSED. The
    paragraph Tony approved goes on L-418 word for word.
  - A NEW item, the website's checks, in the order Tony confirmed. Its
    handle is the next free one, worked out when this runs and printed.
  - L-412 (the Sun's slice): question (b) answered. RICE scores struck
    on list members: L-131, L-128, L-228, L-241, L-292, L-235, L-237,
    L-262.
  - L-262, L-357, L-367, L-378, L-360, L-380, L-388: their place in the
    new list; Tony's delete ruling on L-357.
  - L-395 (the Horizons check): Halley keyed; both comets' words and
    NASA links; the daily_run.py OneDrive line.
  - L-418 (splitting provenance-discipline): the 2.27 ruling and the
    approved paragraph. L-414: gets its own session, 2.28.
  - Where We Are: edited by section. Nothing below the run-record
    marker is touched.

SAFE TO RUN IN EITHER ORDER with the split session's patch (L-418).
Each edit anchors only on the lines it changes; no whole-file
fingerprint and nothing inside the ledger's INDEX zone. If an anchor is
missing, the patch prints ANCHOR FAIL and writes NOTHING.

If it was already applied, it says so and writes nothing.
Undo is Discard Changes in GitHub Desktop.

Built on orrery b0b3df8264958ec9f4a7270f4e4008825452f08d at
https://github.com/tonylquintanilla/palomas_orrery (gallery
ab66aba70a5874b033742a8428070b5889484490, not touched).
Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(ROOT, 'LEDGER_CONSOLIDATED.md')
PAGE = os.path.join(ROOT, 'documentation', 'WHERE_WE_ARE.md')
DONE_MARK = 'the decisions session of 2026-10-08'
MARKER = '--- Your run record below this line.'
CAP = 130

results = []


class AnchorFail(Exception):
    pass


def ok(fname, label, note=''):
    results.append('ok  %-24s %s%s' % (fname, label, ('  (' + note + ')') if note else ''))


def ascii_or_die(s, label):
    bad = [c for c in s if ord(c) > 127]
    if bad:
        raise AnchorFail('non-ASCII in inserted text: %s' % label)


def replace_once(text, old, new, fname, label):
    n = text.count(old)
    if n != 1:
        raise AnchorFail('%s: %s -- expected 1 match, got %d: %r'
                         % (fname, label, n, old[:70]))
    ascii_or_die(new, label)
    ok(fname, label)
    return text.replace(old, new)


def drop_if_present(text, old, fname, label):
    n = text.count(old)
    if n > 1:
        raise AnchorFail('%s: %s -- matched %d times' % (fname, label, n))
    if n == 1:
        ok(fname, label, 'removed')
        return text.replace(old, '')
    ok(fname, label, 'already gone, nothing to remove')
    return text


def block_span(text, num):
    pat = re.compile(r'^#### \[L-%03d\b[^\n]*$' % num, re.M)
    hits = list(pat.finditer(text))
    if len(hits) != 1:
        raise AnchorFail('ledger: L-%d header -- expected 1, got %d'
                         % (num, len(hits)))
    start = hits[0].start()
    nxt = re.compile(r'^#### \[L-', re.M).search(text, hits[0].end())
    end = nxt.start() if nxt else len(text)
    return start, end


META = re.compile(r'^<!-- L:(\d+) [^\n]*-->$', re.M)


def set_meta(text, num, label, **fields):
    s, e = block_span(text, num)
    block = text[s:e]
    m = META.search(block)
    if not m or int(m.group(1)) != num:
        raise AnchorFail('ledger: L-%d metadata line not found' % num)
    line = m.group(0)
    new = line
    for k, v in fields.items():
        new2, n = re.subn(r'\b%s:\S*' % k, '%s:%s' % (k, v), new)
        if n != 1:
            raise AnchorFail('ledger: L-%d metadata has no %s field' % (num, k))
        new = new2
    block = block[:m.start()] + new + block[m.end():]
    ok('LEDGER', 'L-%d %s' % (num, label))
    return text[:s] + block + text[e:]


def insert_after_meta(text, num, lines, label):
    ascii_or_die(lines, label)
    s, e = block_span(text, num)
    block = text[s:e]
    m = META.search(block)
    if not m:
        raise AnchorFail('ledger: L-%d metadata line not found' % num)
    pos = m.end() + 1  # after the newline
    block = block[:pos] + lines + block[pos:]
    ok('LEDGER', 'L-%d %s' % (num, label))
    return text[:s] + block + text[e:]


def replace_in_block(text, num, old, new, label):
    s, e = block_span(text, num)
    block = text[s:e]
    n = block.count(old)
    if n != 1:
        raise AnchorFail('ledger: L-%d %s -- expected 1 match in the block, got %d: %r'
                         % (num, label, n, old[:70]))
    ascii_or_die(new, label)
    block = block.replace(old, new)
    ok('LEDGER', 'L-%d %s' % (num, label))
    return text[:s] + block + text[e:]


def insert_before_in_block(text, num, anchor, new, label):
    return replace_in_block(text, num, anchor, new + anchor, label)


def next_handle(text):
    nums = [int(x) for x in re.findall(r'^#### \[L-(\d+)', text, re.M)]
    nums += [int(x) for x in re.findall(r'^<!-- L:(\d+) ', text, re.M)]
    return max(nums) + 1


def read(path):
    raw = open(path, 'rb').read()
    was_crlf = b'\r\n' in raw
    return raw.replace(b'\r\n', b'\n').decode('utf-8'), was_crlf


def count_non_ascii(s):
    return sum(1 for c in s if ord(c) > 127)


# ---------------------------------------------------------------------
# The texts
# ---------------------------------------------------------------------

APPROVED_PARAGRAPH = """\
**What the checker reports is a different list** (L-252, Tony,
2026-10-08). `worksheet_checker.py` compares the code against a
worksheet and reports one of four outcomes. They are the checker's
words, not worksheet tokens, and never belong in a verdict cell.

- DRIFTED -- the worksheet confirmed a value and the code left it, or
  called it APPROX or PARTIAL and the code moved somewhere the
  worksheet never named. The only defect of the four; routed to
  conversation.
- CORRECTED -- the worksheet rejected the value and the code moved.
  Recorded, not routed.
- COMPLETED -- the worksheet called it APPROX or PARTIAL and supplied a
  value, and the code now reads exactly that value. Recorded, not
  routed.
- UNCHECKED_MOVE -- the code moved and the worksheet carries no value
  verdict. Routed, because nobody has established anything.

COMPLETED says only that the code took the value the worksheet
supplied. It is not a confirmation. The row is still APPROX or
PARTIAL, it earns no leg toward the cross-checked rung, and the
send-back rule above is unchanged.
"""


def indent(s, pad='    '):
    return ''.join((pad + ln) if ln.strip() else ln
                   for ln in s.splitlines(True))


def ledger_edits(L, NEW):
    F = 'LEDGER'

    # --- header stamp, inserted before a fixed line below the stanzas
    L = replace_once(
        L, 'Review and RICE update Tony 6-21-2026\n',
        "Module updated: October 8, 2026 with Anthropic's Claude Opus 5.5\n"
        "(the decisions session of 2026-10-08: L-216 and L-252 closed;\n"
        "L-%d opened, the website's checks; rulings on L-395, L-418 and\n"
        "L-412's question (b); scores struck on list members), built on\n"
        "b0b3df82.\n"
        "Review and RICE update Tony 6-21-2026\n" % NEW,
        F, 'header stamp')

    # --- L-216 (the swap retry): close
    L = set_meta(L, 216, 'closed', status='DONE', upd='2026-10-08', section='C')
    L = replace_in_block(
        L, 216,
        '**Tony-action (decide):** whether this item CLOSES on that evidence.',
        '**Tony-action (decide) -- DECIDED 2026-10-08: it closes.** Whether\n'
        'this item CLOSES on that evidence.',
        'decide line marked decided')
    L = replace_in_block(
        L, 216,
        '**Gap (corrected 2026-09-21):** the CAUSE, unchanged. WATCH FOR A SWAP\n'
        'THAT TOOK MORE THAN ONE ATTEMPT -- the builder\'s `[SWAP]` line now says it\n'
        'on screen, and the maintenance run\'s last line reads it back from the\n'
        'log. That is the fix doing its job, and until one appears the retry is\n'
        'unproven. The empty " (N)" folders are a second, smaller symptom with the\n'
        'same suspected cause and no known harm.\n',
        '**Gap:** none. CLOSED 2026-10-08 in the decisions session of\n'
        '2026-10-08, on the evidence below (the retry proven twice, read from\n'
        'the swap log). Tony: "Yes, close it with those comments." The\n'
        'cause, a OneDrive or Windows lock on the live folder, is outside the\n'
        'project and is not chased. Loose ends re-homed (A Closing Item\n'
        'Re-homes Its Loose Ends): the gallery-cache-builder owed items, now\n'
        'with the two proven retries, and the "conflict copies" wording in\n'
        'four places, to L-351; the `daily_run.py` OneDrive-pause line to\n'
        'L-395. (Was, 2026-09-21: the CAUSE, unchanged; watch for a swap that\n'
        'took more than one attempt. Two have since appeared.)\n',
        'Gap closed')
    L = insert_before_in_block(
        L, 216, '**Ref:** `tools/gallery_cache_builder.py`',
        '**Note (2026-10-08) -- Tony is trying builds without the OneDrive\n'
        'pause.** Tony: "Today I ran the daily run without pausing the sync.\n'
        'With the retry as the fail safe do I need the pause?" Claude\'s\n'
        'answer: probably not. The pause has never prevented the lock -- both\n'
        'proven retries, and two outright September failures, happened while\n'
        'paused -- and the retry, then the roll-back, are what protect the\n'
        'served cache. What is not known is whether sync running makes a lock\n'
        'outlast the retry\'s six tries over about fifty seconds; a few weeks\n'
        'of runs will say. The swap log shows it either way: a line with more\n'
        'than one attempt is the retry absorbing a lock. That run had not been\n'
        'pushed when this was written; the log\'s newest line was\n'
        '20261008T013323Z. This also changes the `daily_run.py` fix carried on\n'
        'L-395.\n',
        'no-pause trial note')

    # --- L-252: close
    L = set_meta(L, 252, 'closed', status='DONE', upd='2026-10-08', section='C')
    L = replace_in_block(
        L, 252,
        '**Gap:** none in the tool. Whether the four outcomes want a matching\n'
        'line in provenance-discipline\'s verdict vocabulary is unruled --\n'
        'COMPLETED is a checker outcome, not a worksheet token, and the two\n'
        'vocabularies have stayed separate so far.\n'
        '- **Note:** RICE 3/4/95/1 is Claude\'s proposed score.\n'
        '  **Tony-action (decide):** confirm or redirect.\n',
        '**Gap:** none. CLOSED 2026-10-08 in the decisions session of\n'
        '2026-10-08. The fix is in the code at b0b3df82: the four L2b\n'
        'outcomes in `worksheet_checker.py`, both directions pinned in\n'
        '`test_worksheet_checker.py`, `patch_L252_1` archived. The open\n'
        'wording question (was: "whether the four outcomes want a matching\n'
        'line in provenance-discipline\'s verdict vocabulary is unruled") was\n'
        'explained to Tony and settled: the skill names the checker\'s four\n'
        'outcomes in one paragraph, and says COMPLETED is not a confirmation\n'
        'and the send-back rule still applies. Tony: "Agree. But we should\n'
        'add the skill update in this session." Offered a bump now (2.27,\n'
        'the split renumbered to 2.28) or the exact words now, carried by the\n'
        'split; Tony: "Concur with B." The wording: "Approved". Re-homed, word\n'
        'for word, to L-418. The RICE question this block carried is moot.\n',
        'Gap closed, paragraph re-homed')

    # --- the new item, before L-412's header
    new_block = (
        "#### [L-%d] The website's checks: the order Tony confirmed (checks, gallery)\n"
        "<!-- L:%d status:OPEN upd:2026-10-08 section:A flag: rice: -->\n"
        "- **Confirmed by Tony, 2026-10-08**, in the decisions session of\n"
        "  2026-10-08: \"Yes open it now\"; on the order, \"The order is okay\".\n"
        "  This is road stage 9 on Where We Are. It comes before the front-door\n"
        "  swap, L-363 (the Solar System room as front door), as Tony asked on\n"
        "  2026-10-04 (L-412): one member, L-367, is that no checker opens a\n"
        "  new room, and the swap changes the front door. Smallest and most\n"
        "  settled first:\n"
        "  1. L-262, the framing test. Both of its one-line fixes are already\n"
        "     in, at gallery ab66aba7. Confirm the Page framing row passes on\n"
        "     the next gallery maintenance run, then close it; its residual\n"
        "     (the live room's framing has no test) moves into L-367.\n"
        "  2. L-380 and L-388, the export pull, as one patch: pull before the\n"
        "     cache build, and fail by name when the pull cannot fetch.\n"
        "  3. L-357, stale leftovers: delete the unreferenced hover fixture\n"
        "     (Tony, 2026-10-08: yes) and correct two code comments.\n"
        "  4. L-235 with L-237, the Earth golden record, as a pair: the check\n"
        "     reads the stored record, then the record is re-cut.\n"
        "  5. L-360, the hover-length check, measured from the live config.\n"
        "  6. L-367, a checker that opens every room and reads the lobby code.\n"
        "     Finishes before L-363.\n"
        "  7. L-378, the phone check: automate it, or decide it stays Tony's\n"
        "     manual check. Decided after item 6 shows what a headless browser\n"
        "     can see. May follow L-363.\n"
        "- Members carry no RICE score: the list's order is its priority\n"
        "  (Tony's rule of 2026-10-07, L-412). The scores L-235, L-237 and\n"
        "  L-262 carried are struck.\n"
        "- **Not a member:** L-379 (the aging Earth recording). Its only\n"
        "  remaining piece, `documentation/payload_earth.json`, waits for a\n"
        "  build that opens that file.\n"
        "**Gap:** work down the list from item 1.\n"
        "**Ref:** L-412; L-363; the members above;\n"
        "`documentation/HANDOFF_decisions_20261008.md`.\n\n" % (NEW, NEW))
    L = replace_once(
        L, '#### [L-412] The Sun\'s slice: the order Tony confirmed',
        new_block + '#### [L-412] The Sun\'s slice: the order Tony confirmed',
        F, 'L-%d opened before L-412' % NEW)

    # --- L-412: question (b)
    L = set_meta(L, 412, 'date', upd='2026-10-08')
    L = replace_in_block(
        L, 412,
        '  ledger-and-session-records 1.17 (L-422), not at L-418\'s build.\n'
        '  Question (b) is still open.\n',
        '  ledger-and-session-records 1.17 (L-422), not at L-418\'s build.\n'
        '  Question (b) is still open.\n'
        '- **2026-10-08, question (b) answered** in the decisions session of\n'
        '  2026-10-08. Under the ruling on (a), the scores proposed for L-131\n'
        '  and L-128 (this list\'s items 9 and 10), L-228 and L-241 (items 4\n'
        '  and 6) and L-292 (a member of L-413) do not apply, and the scores\n'
        '  they carried are struck. L-216 (the swap retry) closed. L-252 (an\n'
        '  incomplete verdict is not a confirmation), the one live score,\n'
        '  closed too: its fix was built in August, and its wording question\n'
        '  became a paragraph for provenance-discipline (L-418). The gallery\'s\n'
        '  checks, the list after this one, are now L-%d.\n' % NEW,
        'question (b) answered')

    # --- RICE struck on list members
    members = [
        (131, '2/2/50/2', 'item 9 of L-412 (the Sun\'s slice)'),
        (128, '2/2/50/2', 'item 10 of L-412 (the Sun\'s slice)'),
        (228, '2/3/60/2', 'item 4 of L-412 (the Sun\'s slice)'),
        (241, '2/2/95/1', 'item 6 of L-412 (the Sun\'s slice)'),
        (292, '3/3/75/2', 'a member of L-413 (Earth\'s list)'),
        (235, '3/4/95/1', 'item 4 of L-%d (the website\'s checks)' % NEW),
        (237, '3/4/90/1', 'item 4 of L-%d (the website\'s checks)' % NEW),
        (262, '3/4/95/1', 'item 1 of L-%d (the website\'s checks)' % NEW),
    ]
    for num, was, where in members:
        s, e = block_span(L, num)
        m = META.search(L[s:e])
        if 'rice:%s' % was not in m.group(0):
            raise AnchorFail('ledger: L-%d expected rice:%s, found %r'
                             % (num, was, m.group(0)))
        L = set_meta(L, num, 'RICE struck', upd='2026-10-08', rice='')
        L = insert_after_meta(
            L, num,
            '- **Note (2026-10-08):** RICE struck (was %s). This item is %s,\n'
            '  and an item in an ordered list carries no score; the list\'s\n'
            '  order is its priority (Tony\'s rule of 2026-10-07, L-412).\n'
            % (was, where), 'struck-score note')

    # --- L-262: the fixes are in
    L = insert_after_meta(
        L, 262,
        '- **2026-10-08, checked at gallery ab66aba7:** both one-line fixes\n'
        '  below are in. The gallery maintenance run\'s Page framing row passes\n'
        '  `gallery/solar_system_earth_test2.html` and\n'
        '  `gallery/feature_renderers.js`, and `smoke_framing.js` reads\n'
        '  `documentation/payload_jupiter_saturn.json`. Left: confirm the row\n'
        '  passes on the next run, and the residual -- the live room\'s\n'
        '  framing, `sunRefitFrame` in `interactive.html`, has no test -- which\n'
        '  moves into L-367 when this item closes.\n',
        'fixes found already in')

    # --- other members
    member_notes = [
        (367, '- **2026-10-08:** item 6 of L-%d (the website\'s checks). Takes\n'
              '  L-262\'s residual (the live room\'s framing has no test) when\n'
              '  L-262 closes. Finishes before L-363.\n' % NEW),
        (378, '- **2026-10-08:** item 7 of L-%d (the website\'s checks). The\n'
              '  choice in the Gap -- automate it, or a stated decision that it\n'
              '  stays manual -- waits until item 6 (L-367) shows what a\n'
              '  headless browser can see. May follow L-363.\n' % NEW),
        (360, '- **2026-10-08:** item 5 of L-%d (the website\'s checks).\n' % NEW),
        (380, '- **2026-10-08:** item 2 of L-%d (the website\'s checks), one\n'
              '  patch with L-388.\n' % NEW),
        (388, '- **2026-10-08:** item 2 of L-%d (the website\'s checks), one\n'
              '  patch with L-380.\n' % NEW),
        (235, '- **2026-10-08:** item 4 of L-%d (the website\'s checks), with\n'
              '  L-237. Instance 1 is still there at gallery ab66aba7\n'
              '  (`fp.compare(golden, golden)`).\n' % NEW),
        (237, '- **2026-10-08:** item 4 of L-%d (the website\'s checks), with\n'
              '  L-235.\n' % NEW),
    ]
    for num, note in member_notes:
        L = set_meta(L, num, 'date', upd='2026-10-08')
        L = insert_after_meta(L, num, note, 'list membership')

    # --- L-357: Tony's delete ruling
    L = set_meta(L, 357, 'date', upd='2026-10-08')
    L = replace_in_block(
        L, 357,
        '**Gap:** **Tony-action (decide):** whether the unreferenced fixture is deleted.',
        '**Gap:** **Tony-action (decide) -- DECIDED 2026-10-08: delete it.**\n'
        'Tony: "yes" (the unreferenced `documentation/fixture_hovers_cdfa74c3.json`,\n'
        'still present at gallery ab66aba7). It goes in item 3 of L-%d (the\n'
        'website\'s checks).' % NEW,
        'delete ruling')

    # --- L-351: the gallery-cache-builder line, from L-216
    L = set_meta(L, 351, 'date', upd='2026-10-08')
    L = replace_in_block(
        L, 351,
        '  - gallery-cache-builder: the `[SWAP]` line, the run order and the\n'
        '    empty "(N)" folders (L-216).\n',
        '  - gallery-cache-builder: the `[SWAP]` line, the run order and the\n'
        '    empty "(N)" folders (L-216); and, re-homed 2026-10-08 when L-216\n'
        '    closed, the two proven retries (runs 20261004T205153Z and\n'
        '    20261006T182032Z, each `staging_to_live` on its second attempt,\n'
        '    both with OneDrive paused), and that Tony is trying builds\n'
        '    without the pause. Also from L-216: the "conflict copies" wording\n'
        '    for the empty " (N)" folders, which the 2026-09-21 report does\n'
        '    not support, in four places -- the comment above the two rules in\n'
        '    the gallery\'s `.gitignore`, the docstring of the gallery\'s\n'
        '    `documentation/check_cache_siblings.py`, the orrery dashboard\'s\n'
        '    Cache Siblings description, and the orrery\'s\n'
        '    `documentation/L342_install_test_run_sequence.md`; for a pass\n'
        '    that touches them anyway.\n',
        'gallery-cache-builder owed items')

    # --- L-395: the build questions
    L = set_meta(L, 395, 'date', upd='2026-10-08')
    L = replace_in_block(
        L, 395,
        '- (decide) At the build: whether Halley is keyed and checked too; and\n'
        '  Encke\'s description and link.\n',
        '- (decide) At the build: whether Halley is keyed and checked too; and\n'
        '  Encke\'s description and link. DECIDED 2026-10-08; see below.\n',
        'decide line marked decided')
    L = insert_before_in_block(
        L, 395, '**Gap:** The first build is done (the room\'s eleven bodies).',
        '- **2026-10-08, the two build questions ruled** in the decisions\n'
        '  session of 2026-10-08, Tony on his phone:\n'
        '  - Halley is keyed and checked too. Tony: "yes, and follow the new\n'
        '    url rule." Its link moves from Tony\'s own Halley page\n'
        '    (sites.google.com/view/tony-quintanilla/comets/halley-1986) to\n'
        '    NASA\'s 1P/Halley page,\n'
        '    https://science.nasa.gov/solar-system/comets/1p-halley/ -- the\n'
        '    rule is a NASA page where one is specific, else Wikipedia\n'
        '    (interactive-exhibit, A feature\'s info link), and the list\'s one\n'
        '    link field carries it in both the orrery and the website.\n'
        '  - Encke\'s new entry links NASA\'s 2P/Encke page,\n'
        '    https://science.nasa.gov/solar-system/comets/2p-encke/ . Both URLs\n'
        '    fetched live 2026-10-08.\n'
        '  - The words. Tony: "No numbers unless they come from the store."\n'
        '    Halley\'s period is in the store only as a drawing value\n'
        '    (`KNOWN_ORBITAL_PERIODS` in `constants_new.py`), which a\n'
        '    description cannot read; Encke has none. So no numbers. After\n'
        '    each entry\'s own "Horizons: ..." opening sentence (kept in the\n'
        '    orrery, dropped by the export):\n'
        '    - Halley: "The most famous periodic comet. Its orbit runs\n'
        '      backward compared with the planets, and its dust gives two\n'
        '      meteor showers each year, the Eta Aquarids and the Orionids."\n'
        '    - Encke: "A short-period comet whose dust trail is the source of\n'
        '      the Taurid meteor showers."\n'
        '    Checked against the two NASA pages, read 2026-10-08. Halley\'s\n'
        '    old words ("returned in 1986 and will return in 2061", and\n'
        '    "Retrograde" twice) are replaced. Left out on purpose: the Encke\n'
        '    page\'s "shortest orbital period of any known comet". Claude\'s\n'
        '    recollection, not checked, is that comets found since are\n'
        '    shorter, and the same page gives a stale last perihelion, 2015.\n'
        '- **2026-10-08, the `daily_run.py` OneDrive line, re-homed from L-216\n'
        '  (closed):** gallery `daily_run.py` step 2 says the pause lasts 2\n'
        '  hours and prints an expiry two hours on. Tony pauses 24, and on\n'
        '  2026-10-08 ran a build without pausing, as a trial ("With the\n'
        '  retry as the fail safe do I need the pause?"). So this build\'s fix\n'
        '  is no longer only "say 24 hours": ask Tony then whether the pause\n'
        '  step becomes optional or goes.\n',
        'rulings recorded before the Gap')

    # --- L-418: the 2.27 ruling and the approved paragraph
    L = set_meta(L, 418, 'date', upd='2026-10-08')
    L = insert_after_meta(
        L, 418,
        '- **2026-10-08, the split brief\'s section 4 decision, ruled** in the\n'
        '  decisions session of 2026-10-08 (Tony: "As recommended? -- yes"):\n'
        '  L-371 (the Sun room\'s served numbers) and L-390 (the conversion\n'
        '  marker) ride provenance-discipline 2.27 with the split; L-414 (the\n'
        '  scanner\'s window) gets its own session, which cuts 2.28, before the\n'
        '  Sun\'s list reaches L-228 (the Alfven surface\'s ranges). Carried to\n'
        '  the split session, already running, by\n'
        '  `documentation/NOTE_for_split_session_L252_paragraph_20261008.md`.\n'
        '- **2026-10-08, one approved paragraph rides the split too,** from\n'
        '  L-252 (closed). Tony: "Concur with B" (the exact words now, carried\n'
        '  by the split, not a bump of its own); on the wording, "Approved".\n'
        '  It goes right after the send-back rule ("PARTIAL and APPROX return\n'
        '  to the originator for completion", and its "Ask for a NEW file"\n'
        '  paragraph), before "A Complete Row That Disagrees Is a Finding". If\n'
        '  the split moves that section to provenance-cross-check 1.0, the\n'
        '  paragraph goes with it; placement is the split session\'s call. If\n'
        '  the split shipped without it, it rides L-414\'s 2.28. The text,\n'
        '  word for word (indented four spaces here; the text starts at the\n'
        '  bold line):\n\n'
        + indent(APPROVED_PARAGRAPH) + '\n',
        '2.27 ruling and the approved paragraph')

    # --- L-414: its own session
    L = set_meta(L, 414, 'date', upd='2026-10-08')
    L = insert_after_meta(
        L, 414,
        '- **2026-10-08:** Tony ruled that this item gets its own session,\n'
        '  which cuts provenance-discipline 2.28, before the Sun\'s list\n'
        '  reaches L-228 (the Alfven surface\'s ranges); it does not ride the\n'
        '  split (L-418). If the split shipped 2.27 without L-252\'s approved\n'
        '  paragraph (on L-418), that paragraph rides this item\'s 2.28.\n',
        'own session, 2.28')
    return L


def page_edits(P, NEW):
    F = 'WHERE_WE_ARE'

    m = re.search(r'^Last updated: [^\n]*\n- Written at [^\n]*\n(?:  [^\n]*\n)*',
                  P, re.M)
    if not m:
        raise AnchorFail('%s: header "Last updated" lines not found' % F)
    P = P[:m.start()] + (
        'Last updated: October 8, 2026, after the decisions session.\n'
        '- Written at orrery b0b3df82 and gallery ab66aba7, before your run of\n'
        '  patch_L412_2_decisions_20261008.py.\n') + P[m.end():]
    ok(F, 'header date')

    # The box: the previous session's "changed" lines go if still there.
    old_changed = [
        '> - 15 of the 17 typed facts are served with their sources and live,\n'
        '>   in three website patches. You found every hover\'s words correct.\n',
        '> - Earth\'s four drawn guides have Read more links: the Sun\n'
        '>   Direction, the rotation axis, the day-night line and the Moon.\n',
        '> - Their sources reach the panel now; they had been served but not\n'
        '>   shown. The panel\'s words and footer are brighter.\n',
        '> - The inner Oort cloud is drawn flat, but a 2025 paper finds it\n'
        '>   tilted about 30 degrees. You ruled it is redrawn now, as part of\n'
        '>   the Sun\'s slice.\n',
    ]
    for i, old in enumerate(old_changed, 1):
        P = drop_if_present(P, old, F, 'box: old changed line %d' % i)
    P = replace_once(
        P, '> **Changed since you last read this:**\n',
        '> **Changed since you last read this:**\n'
        '> - L-216 (the swap retry) is closed. You are trying builds without\n'
        '>   the OneDrive pause; the swap log shows any retry.\n'
        '> - L-252 (an incomplete verdict is not a confirmation) is closed. Its\n'
        '>   approved paragraph rides the split.\n'
        '> - The website\'s checks are an ordered list: L-%d (the website\'s checks).\n'
        '> - Halley is checked too; both comets get NASA pages and no numbers.\n'
        '> - The split carries L-371 (the Sun room\'s served numbers) and L-390\n'
        '>   (the conversion marker); L-414 (the scanner\'s window) waits.\n' % NEW,
        F, 'box: changed since')

    m = re.search(r'^> \*\*Do next:\*\*[^\n]*\n(?:> [^\n]+\n)*', P, re.M)
    if not m:
        raise AnchorFail('%s: "Do next" line not found' % F)
    P = P[:m.start()] + (
        '> **Do next:** *the split session (running now) finishes first. Then,\n'
        '> as you confirmed: the typed facts (the inner Oort cloud, then the\n'
        '> check); the Horizons check build; the Sun\'s list from item 3, with\n'
        '> the scanner\'s window session before the Alfven surface\'s ranges.*\n') + P[m.end():]
    ok(F, 'box: do next (the confirmed order)')

    P = drop_if_present(
        P, '> - *Run this closing patch, then orrery_maintenance_run.py, and push.*\n',
        F, 'box: old needs-you line')
    P = replace_once(
        P, '> **Needs you now:**\n',
        '> **Needs you now:**\n'
        '> - *Run patch_L412_2_decisions_20261008.py, then\n'
        '>   orrery_maintenance_run.py, and push.*\n',
        F, 'box: needs you now')

    # The road
    # Marks reset at every update; another session's close may already
    # have cleared these, so each accepts either form.
    if 'cloud, redrawn tilted, and the check. << moved this session\n' in P:
        P = replace_once(
            P, 'cloud, redrawn tilted, and the check. << moved this session\n',
            'cloud, redrawn tilted, and the check.\n',
            F, 'road: stage 6 mark cleared')
    else:
        ok(F, 'road: stage 6 mark', 'already cleared')
    m = re.search(r"^               Designed and recorded; build next, with Encke added\n"
                  r"               to the orrery's list\.(?: << new this session)?\n",
                  P, re.M)
    if not m:
        raise AnchorFail('%s: road stage 8 lines not found' % F)
    P = P[:m.start()] + (
        '               Designed and recorded; build next, with Encke added\n'
        '               and Halley checked too. << new this session\n') + P[m.end():]
    ok(F, 'road: stage 8')
    P = replace_once(
        P, '  9.   [next]  The website\'s checks get a short list of their own.\n',
        '  9.   [next]  The website\'s checks, in the order you confirmed:\n'
        '               L-%d (the website\'s checks). << new this session\n' % NEW,
        F, 'road: stage 9')

    # Settled
    P = replace_once(
        P, '- OneDrive: pause 24 hours before a build; the retry absorbs the lock\n'
           '  either way. Empty "solar-system (N)" folders are harmless; delete by\n'
           '  hand. (Oct 7)\n',
        '- OneDrive: you are trying builds without the pause; the retry absorbs\n'
        '  the lock, and the swap log shows any retry. Empty "solar-system (N)"\n'
        '  folders are harmless; delete by hand. (Oct 8)\n'
        '- An object\'s words in the list carry no numbers unless they come\n'
        '  from the store. (Oct 8)\n',
        F, 'settled: OneDrive, and no numbers in object words')

    # Waiting on you: the decisions are all ruled
    P = replace_once(
        P, 'Decisions, one at a time:\n'
           '- At the Horizons check\'s build, L-395 (the Horizons check): whether\n'
           '  Halley is checked too, and Encke\'s description and link.\n'
           '- Whether L-216 (the swap retry) closes. Recommended: yes.\n'
           '- The handful of RICE scores the sweep proposes.\n'
           '- Whether the gallery-checks list becomes a ledger item before building.\n',
        'Decisions, one at a time:\n'
        '- None waiting. All were ruled on Oct 8.\n',
        F, 'waiting: decisions cleared')

    # Where the details are
    m = re.search(r'^## Where the details are[^\n]*\n\n', P, re.M)
    if not m:
        raise AnchorFail('%s: "Where the details are" heading not found' % F)
    P = P[:m.start()] + (
        '## Where the details are  **>> UPDATED THIS SESSION**\n\n'
        '- Today\'s decisions: `documentation/HANDOFF_decisions_20261008.md`.\n'
        '  The new list: L-%d (the website\'s checks).\n' % NEW) + P[m.end():]
    ok(F, 'details: this session')
    return P


def main():
    for p in (LEDGER, PAGE):
        if not os.path.exists(p):
            print('ERROR: %s not found. Save this script in the orrery repo root '
                  '(the folder that holds LEDGER_CONSOLIDATED.md). NOTHING was '
                  'written.' % p)
            return 1
    L, l_crlf = read(LEDGER)
    P, p_crlf = read(PAGE)
    if DONE_MARK in L:
        print('ALREADY APPLIED: the ledger already records the decisions '
              'session of 2026-10-08. NOTHING was written.')
        return 1
    if MARKER not in P:
        print('ERROR: the run-record marker line is missing from '
              'WHERE_WE_ARE.md. NOTHING was written.')
        return 1
    l_before = count_non_ascii(L)
    p_before = count_non_ascii(P)
    below_before = P[P.index(MARKER):]
    NEW = next_handle(L)
    try:
        L2 = ledger_edits(L, NEW)
        P2 = page_edits(P, NEW)
    except AnchorFail as e:
        print('ANCHOR FAIL: %s' % e)
        print('NOTHING was written. Undo is not needed.')
        return 1
    if P2[P2.index(MARKER):] != below_before:
        print('ERROR: an edit reached below the run-record marker. NOTHING '
              'was written.')
        return 1
    above = P2[:P2.index(MARKER)].count('\n')
    if above > CAP:
        print('ERROR: the page would have %d lines above the marker (cap %d). '
              'NOTHING was written.' % (above, CAP))
        return 1
    with open(LEDGER, 'wb') as f:
        f.write(L2.encode('utf-8'))
    with open(PAGE, 'wb') as f:
        f.write(P2.encode('utf-8'))
    for r in results:
        print(r)
    print()
    print('New item: L-%d (the website\'s checks).' % NEW)
    print('Stamps updated: LEDGER_CONSOLIDATED.md header stamp; '
          'WHERE_WE_ARE.md "Last updated" lines.')
    print('Where We Are: %d lines above the run-record marker (cap %d); '
          'nothing below it touched.' % (above, CAP))
    for name, crlf in (('LEDGER_CONSOLIDATED.md', l_crlf),
                       ('WHERE_WE_ARE.md', p_crlf)):
        if crlf:
            print('note: %s was CRLF in the working copy; written LF' % name)
    if l_before or p_before:
        print('note: non-ASCII bytes this patch did not reach: ledger %d, '
              'page %d' % (l_before, p_before))
    print()
    print('patch applied')
    print()
    print('NEXT:')
    print('  1. Run orrery_maintenance_run.py -- it rebuilds the ledger\'s index')
    print('     and moves L-216 and L-252 into the closed section.')
    print('  2. Move this script into documentation/, with these two files from')
    print('     the decisions session: HANDOFF_decisions_20261008.md and')
    print('     NOTE_for_split_session_L252_paragraph_20261008.md, and the')
    print('     brief HANDOFF_decisions_brief_20261008.md if it is not there.')
    print('  3. Commit and push.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
