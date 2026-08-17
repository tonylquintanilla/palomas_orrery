"""patch_L196_7_summary_current.py -- bring the readable snapshot current,
and make Claude's session-start checks visible to Tony.

RUN COMMAND
-----------
Save into the palomas_orrery repo root, open in VS Code, click Run.

    python patch_L196_7_summary_current.py

Run AFTER patch_L196_6 (the Section 5a rewrite). It touches a different
file, so order does not strictly matter, but the two are one change.

WHAT IT DOES
------------
Updates documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md from
its 2026-08-13 state at 00219d9 to 2026-08-16 at 227f5b2. Nineteen
hunks.

THE ADDITION THAT MOTIVATED THIS
--------------------------------
A new section, WHAT CLAUDE CHECKS BEFORE ANYTHING ELSE. Tony's
instruction, 2026-08-16: "so I can track the steps that Claude is
tracking -- conceptually we need to be aligned at the same register."

Those checks fire unprompted at session start and were invisible from
Tony's side, which meant he could neither prepare for them nor notice
one being skipped. The section lists all five -- SHA round trip, skill
version check, uploads enumerated, ledger read, handoff obligations --
and states plainly what Tony can do with the list: push before a
session so HEAD is current, and keep the three skill stores in sync so
the version gate has nothing to catch.

It also carries the currently outstanding obligation, in place rather
than only in a handoff: safe-file-editing and orrery-coding-conventions
both went 1.3 -> 1.4 on August 16, the session that bumped them loaded
1.3, and the next session must confirm 1.4 before patch-script or
marker work.

WHAT ELSE MOVED
---------------
  - header re-anchored to both current SHAs, and the division of labour
    between this document, Section 5a and CRITICAL_PATH_SUMMARY.md
    stated
  - THE SHORT VERSION rewritten: the checker is built and running, the
    reconciliation is 3 clean of 102, the dispatch has nine blockers
    from the Fable/GPT review, the chromosphere is retired
  - scanner Tier-1 re-measured at 227f5b2 and UNCHANGED at 206
  - ledger by track: L-192 built, L-193 through L-196 added, L-180
    marked dormant-not-superseded, L-154 given its precise diagnosis
  - Jupiter's registry entry count moved from unsettled to settled at 4
  - protocol v3.39 -> v3.40 with both skill bumps named
  - a new WHAT IS TRACKED RIGHT NOW block at the end

One passage is deliberately NOT corrected. The old tail says the
checker "is designed and reviewed and NOT built." A bracketed note
records that both halves are since done, and the original wording
stays, because it is the record of what was true then. Correcting it
would falsify the record -- the same reasoning the document already
applies to a historical tooltip count.

WHAT IS PERMANENT
-----------------
This script is disposable. The document is not.

SAFETY
------
All-or-nothing, fingerprinted, bottom-up, line endings preserved. Every
replaced block must read exactly as recorded. The edit table is written
with ascii() so this deliverable stays ASCII.
Success: one 'ok' line, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md': {
        'fp': '382d92fb07b0a6258dd45c862e00e8e2',
        'edits': [
            (514, 513,
             [
             ],
             [
              'WHAT IS TRACKED RIGHT NOW -- 2026-08-16',
              '',
              '  Ready to build, no ruling outstanding',
              '    Builder marker join + loud failure  <- do this first; 96 markers',
              '      are placed and currently do nothing',
              '    Stage 2 continuation markers -- 117 runs, 23 files, fingerprints',
              '      to be regenerated against 227f5b2',
              '    Six Shape A citation swaps (L-195)',
              '    Ordinal context window -- 26 rows share 8 excerpts today',
              '    Print the seven verdict tokens in the request',
              '    Resolver + models fix (L-154) -- independent of all provenance work',
              '',
              '  Waiting on a ruling',
              '    Lazy responder: canaries, or remove the self-certifying field',
              '    Claim typing: real row types, or wait for a measured population',
              '    Cross-worksheet disagreement, what UNKNOWN does, pluto 614/638,',
              '      transition sequencing, whether batching becomes real',
              '',
              '  Carried as an obligation',
              '    Confirm safe-file-editing and orrery-coding-conventions load at',
              '      1.4 before patch-script or marker work',
              '',
              '  Not yet written',
              '    Ledger entries for L-194, L-195, L-196 and the L-192 as-built',
              '',
              '',
              "Entry written August 2026 with Anthropic's Claude Opus 5. Updated",
              'August 16, 2026, built on 227f5b2d6763baa384c090a911c2c5ced64f4a4d.',
              '',
             ]),
            (512, 512,
             [
              "Entry written August 2026 with Anthropic's Claude Opus 5.",
             ],
             [
             ]),
            (511, 510,
             [
             ],
             [
              '  [Both since done. The checker was built and now runs continually;',
              '  the half-confirmed question was ruled. Left as written because it',
              '  is the record of what was true then.]',
             ]),
            (439, 439,
             [
              'Protocol at v3.39. The v3.36 Register Rule amendment is applied, and',
             ],
             [
              'Protocol at v3.40 (August 16) -- no change to its own rules; the entry',
              'records two skill bumps and the two bad deliveries that preceded the',
              'good ones. safe-file-editing 1.4 adds Fix In Passing, Report It and the',
              'patch-script naming convention. orrery-coding-conventions 1.4 adds',
              'Marker Separation for Near-Equal Radii and Harvest the Conventions You',
              'Find. The v3.36 Register Rule amendment is applied, and',
             ]),
            (420, 422,
             [
              "Jupiter's registry entry count is unsettled. The August 7 revision of",
              'this summary said five; the August 10 session counted four ring entries.',
              'Confirm before the pilot starts, since the pilot is scoped by it.',
             ],
             [
              "Jupiter's registry entry count is SETTLED at four, confirmed at 253bcdd",
              'on August 15. Jupiter 4, Saturn 7, Uranus 11, Neptune 11, total 33 --',
              "matching L-181's enumeration. The five came from counting",
              'inner_radius_km including the line that reads the key.',
             ]),
            (383, 383,
             [
              '  Track 2     L-154  JS feature-rendering layer -- does not exist yet',
             ],
             [
              '  Track 2     L-154  JS feature-rendering layer -- does not exist yet.',
              '                     Now precisely diagnosed: resolver.py:133 reduces a',
              '                     feature dict to its keys, models.py:91 types the',
              '                     field to match, and no code in the gallery repo',
              '                     reads feature_configs.json at all. Two lines and a',
              '                     type, then the renderers.',
             ]),
            (378, 379,
             [
              '              L-192  Worksheet checker -- scanner half built,',
              '                     checker designed and reviewed, NOT built',
             ],
             [
              '              L-192  Worksheet checker  BUILT and running as one of',
              '                     the twelve maintenance checkers. Request builder',
              '                     built. Key rule built. DISPATCH not finished --',
              '                     see the nine blockers.',
              '              L-193  Worksheet corpus reconciliation',
              '              L-194  Text-only assertions (no number in the claim)',
              '                     DEFERRED, blocking nothing',
              '              L-195  Citation legs -- authority not in the # Source:',
              '                     line. Six of 65 dispatch rows. Shape A ruled,',
              '                     swaps NOT built.',
              '              L-196  Chromosphere retirement, continuation markers,',
              '                     key retirement record  DONE',
             ]),
            (374, 374,
             [
              '              L-180  Solar chromosphere  DONE',
             ],
             [
              '              L-180  Solar chromosphere  ON RECORD, DORMANT -- the',
              '                     stylization it governed is retired, so it governs',
              '                     nothing. NOT categorically superseded; a future',
              '                     stylization anywhere would revive it.',
             ]),
            (324, 326,
             [
              'The tier breakdown below was measured at 1ba20c3 on August 7 and has not',
              'been re-measured since: 879 findings across 117 files, Tier 1 206,',
              'Tier 2 583, Tier 3 88, Tier 4 2.',
             ],
             [
              'The tier breakdown below was measured at 1ba20c3 on August 7: 879',
              'findings across 117 files, Tier 1 206, Tier 2 583, Tier 3 88, Tier 4 2.',
              'Tier 1 was re-measured at 227f5b2 on August 16 and is UNCHANGED at 206',
              '-- the chromosphere retirement and the continuation markers moved',
              'nothing, which is correct, since neither added or removed a claim about',
              'the world.',
             ]),
            (43, 44,
             [
              'The next session opens with the build of L-189, the',
              'scanner run history.',
             ],
             [
              'The chromosphere stylization is retired. The shell now draws at true',
              'physical scale, 1.002875 solar radii, and the fact that it reads as a',
              'hairline welded to the photosphere is the lesson rather than a defect.',
              'That decision closed one of the nine blockers by removing the question',
              'instead of answering it.',
              '',
              'The next session opens with the builder-side marker join. Ninety-six',
              'continuation markers were placed in seven files on August 16 and the',
              'builder does not yet know they exist, so the largest blocker -- 45 of',
              '65 dispatch rows showing a truncated citation -- is still live.',
              '',
              '',
              'WHAT CLAUDE CHECKS BEFORE ANYTHING ELSE',
              '',
              "Recorded here on Tony's instruction, 2026-08-16, so the two of us",
              'track the same list. These fire at session start, unprompted, and a',
              'session that skips them is building on an unverified base.',
              '',
              '  1. SHA round trip, both repos. A live remote read of HEAD for the',
              '     orrery and the gallery, compared against what the handoff says',
              '     was pushed. A matching HEAD confirms commit and push in one',
              '     unforgeable check. A mismatch is reconciled BEFORE any build.',
              '',
              '  2. Skill version check. Every skill Claude loads has its version',
              '     line compared against the manifest row in PROJECT_INSTRUCTIONS.md.',
              '     If they disagree, the session STOPS and asks Tony to push the',
              '     current SKILL.md to skills/ and reinstall it in Settings.',
              '',
              '     Two limits worth Tony knowing. The check is LOAD-triggered, so a',
              '     skill bumped later in the same session produces a mismatch with',
              '     nothing left to fire on. And a mid-session reinstall cannot be',
              '     verified from inside the session -- the loaded copy appears bound',
              '     at conversation start. So a mid-session bump is NOT cleared in',
              '     session. It is written into the handoff as an obligation the next',
              '     session discharges.',
              '',
              '     CURRENTLY OUTSTANDING: safe-file-editing and',
              '     orrery-coding-conventions both went 1.3 -> 1.4 on August 16. The',
              '     session that bumped them loaded 1.3. The next session must',
              '     confirm its loaded copies read 1.4 before any patch-script or',
              '     marker work.',
              '',
              '  3. Uploads enumerated. Some uploaded files arrive as readable text',
              "     and others sit only on disk. The split is invisible from Tony's",
              '     side. Claude lists the directory and reads the whole set before',
              '     claiming to have reviewed anything.',
              '',
              '  4. Ledger read. Open items, Tony comments and Gap notes, before',
              '     proposing work.',
              '',
              '  5. Handoff obligations discharged. Anything the previous session',
              '     wrote down as unverifiable at the time.',
              '',
              'What Tony can do with this list: push before a session starts so HEAD',
              'is current, and keep the three skill stores in sync (repo skills/,',
              'Settings, then skills_index.py) so the version gate has nothing to',
              'catch.',
             ]),
            (37, 41,
             [
              "Two smaller things landed on August 10. L-186's mechanical half is done",
              '-- eight annotations repointed at a real worksheet file, three appended',
              'values stripped -- and one shadow constant is gone. The scheduled',
              'nightly build is retired; Tony now runs the builder by hand and commits',
              'it himself.',
             ],
             [
              'The dispatch that clears them is repaired but not finished. Fable 5',
              'and GPT 5.6 Sol reviewed it blind on August 16; both said do not send',
              'it yet, and between them they found nine structural blockers where',
              'two were known. One is closed, three are ruled and unbuilt, three are',
              'open, two need no ruling.',
             ]),
            (30, 35,
             [
              'The order changed in a way worth stating plainly. Artifact 2 was blocked',
              'behind Track 0 and Batch 2. It is now step 2: prove the registry',
              'structure on Jupiter first, where the served data is already complete',
              'and correct so the transport gets a real acceptance test, then',
              "cross-check Artifact 2's remaining values into the proven structure.",
              'Structure first, values second.',
             ],
             [
              'What the checker reports is the number that now organizes Track 1:',
              '102 annotations scored, THREE clean. Forty route to SEND BACK,',
              'nineteen to CONVERSATION, forty are noted with no route. That is not',
              'a discouraging result. Before the checker existed the same 102 claims',
              'were unexamined and looked fine.',
             ]),
            (24, 28,
             [
              'Track 0 is no longer waiting on decisions. On August 8 Tony ruled the',
              'five questions that were blocking it -- the transport, the shape of a',
              'registry entry, what a measured field carries, where display text gets',
              'assembled, and what order the migration runs in. Nothing in Track 0 now',
              'needs a ruling before work can start.',
             ],
             [
              'The worksheet checker is built and running. It is one of the twelve',
              'checkers in maintenance_run.py, so the reconciliation Tony wanted',
              'continual rather than one-shot is continual. The request builder that',
              'sends questions out is built too, and the key rule that binds a',
              'returned row to the right claim.',
             ]),
            (16, 19,
             [
              'The plan is now current with this snapshot. Every August 8 ruling is',
              'written into Section 7 -- decision 12 ratified, 16 and 17 ruled, and 18',
              "added for the registry's three-zone shape. Where the two documents once",
              'disagreed they now agree, so either is safe to read.',
             ],
             [
              'Section 5a of the plan was rewritten on August 16 as the critical',
              'path -- end goal, one-way pipeline, five segments, and a "you are',
              'here" table. CRITICAL_PATH_SUMMARY.md is its readable companion and',
              'answers "how far to the end." THIS document answers "what is being',
              'tracked right now." Read 5a for the shape of the work; read this for',
              'its state.',
             ]),
            (8, 13,
             [
              'Two facts were refreshed 2026-08-15 at 253bcdd: the',
              'provenance-discipline version and the maintenance_run.py checker',
              'count. Everything else here still describes 00219d9 -- notably',
              "L-192's status, which has moved.",
              '',
              'Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md v18. The plan is the',
             ],
             [
              'Companion to MASTER_PLAN_INTERACTIVE_GALLERY.md. The plan is the',
             ]),
            (7, 6,
             [
             ],
             [
              'Both confirmed by live check on the date above.',
             ]),
            (5, 5,
             [
              'gallery at cd4874467254c89e88dc2a8fa0645e99bf5c986e at',
             ],
             [
              'gallery at 3d10739b097e2b63395cf58742873cf378210e68 at',
             ]),
            (2, 3,
             [
              'Updated 2026-08-13 after the August 12-13 sessions. Built on',
              '00219d9 at',
             ],
             [
              'Updated 2026-08-16 after the August 15-16 sessions. Built on',
              '227f5b2d6763baa384c090a911c2c5ced64f4a4d at',
             ]),
            (0, 0,
             [
              'Where we are 8/13/2026',
             ],
             [
              'Where we are 8/16/2026',
             ]),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    if not os.path.isfile('constants_new.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding constants_new.py).')
        return 1

    staged = []
    fixed = []
    total = 0

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written.')
            return 1

        crlf = b'\r\n' in raw
        lines = normalized(raw).decode('utf-8').split('\n')

        # The gate is on what THIS patch introduces. A file that already
        # holds non-ASCII is reported rather than blocked -- blocking on
        # somebody else's bug stops a correct patch, and staying silent
        # about it is how the convention quietly stops being true.
        for _, _, _, new_lines in spec['edits']:
            for line in new_lines:
                try:
                    line.encode('ascii')
                except UnicodeEncodeError:
                    print('ERROR: this patch would insert non-ASCII into '
                          '%s. Nothing written.' % name)
                    print('       %r' % line)
                    return 1
        before = sum(1 for b in bytearray(raw) if b > 127)
        if before:
            fixed.append((name, before))

        for start, end, old, new in spec['edits']:
            if end >= len(lines):
                print('ANCHOR FAIL: %s lines %d-%d run past end of file.'
                      % (name, start + 1, end + 1))
                return 1
            if lines[start:end + 1] != old:
                print('ANCHOR FAIL: %s lines %d-%d do not read as recorded.'
                      % (name, start + 1, end + 1))
                for offset, want in enumerate(old):
                    got = lines[start + offset]
                    if got != want:
                        print('       first difference at line %d'
                              % (start + offset + 1))
                        print('       expected %r' % want)
                        print('       found    %r' % got)
                        break
                print('       Nothing written.')
                return 1
            lines[start:end + 1] = new

        out = '\n'.join(lines).encode('utf-8')
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-36s %d edit(s)' % (name, count))

    for name, before in fixed:
        with open(name, 'rb') as handle:
            after = sum(1 for b in bytearray(handle.read()) if b > 127)
        print('note: %s holds %d non-ASCII byte(s)' % (name, after))
    print('patch applied (%d bytes, %d edits across %d files)'
          % (total, sum(c for _, _, c in staged), len(staged)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
