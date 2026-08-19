"""patch_L209_2_plan_docs_post_pilot.py -- the three planning docs.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root, open it in VS Code,
and click Run. It takes no arguments.

    python patch_L209_2_plan_docs_post_pilot.py

Success: one `ok` line per file, then `patch applied`.
Failure: a single `ERROR:` or `ANCHOR FAIL:` line, and nothing is
written.

Run patch_L209_1_pilot_findings.py and ledger_index.py FIRST if you
have not. This patch does not depend on them, but the ledger is where
the three new items live and the docs below point at them.

WHAT IT DOES
------------
Brings the three planning documents to the post-pilot state. All three
said the same thing on August 18 -- the dispatch machinery is finished
and no dispatch has gone out. That stopped being true on August 18.

  CRITICAL_PATH_SUMMARY.md   anchors, and the segment-1 status: the
                             first dispatch happened and returned.
  MASTER_PLAN_..._GALLERY.md Section 5a "you are here" table.
  ..._GALLERY_SUMMARY.md     header anchors, the FINISHED-and-unused
                             paragraph, the next-session paragraph,
                             and the tracked-right-now list.

The summary document states its own rule: a claim that was true when
written and has since been overtaken is left in place with a bracketed
note rather than deleted, because a document that silently rewrites
its past stops being evidence. This patch follows that rule in the
summary and updates the other two in place, which is their convention.

WHAT IS PERMANENT AND WHAT IS NOT
---------------------------------
This script is disposable; the document state it writes is not.

Written August 2026 with Anthropic's Claude Opus 5. Built on
9ffb9b403a7d62090b30a9acf9adbc6180a6baec at
https://github.com/tonylquintanilla/palomas_orrery
"""

import hashlib
import os
import sys


BASE = {
    'documentation/CRITICAL_PATH_SUMMARY.md':
        '2a87d78196bad2640eaeb4225bf9d8d4',
    'documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md':
        'e026d1f03c4dee6817b35e33f1f8748b',
    'documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md':
        '9ec2ed72495bc7cd3806c8c148723700',
}

# The anchor these documents are CUT FROM. The commit that lands them
# moves HEAD past it, which is correct and self-correcting: the next
# update restamps.
SHA = '9ffb9b403a7d62090b30a9acf9adbc6180a6baec'
SHORT = '9ffb9b4'
GALLERY = 'ff18d3e6fa31f70a8f525df471e751d046cf14fa'


EDITS = [

    # ============================================================
    # 1. CRITICAL_PATH_SUMMARY.md
    # ============================================================
    ('documentation/CRITICAL_PATH_SUMMARY.md', [

        ("**Updated August 18, 2026.** Orrery at\n"
         "`b65ac115fc0f820e8270c0807249813c67bde7bc`, gallery at\n"
         "`ff18d3e6fa31f70a8f525df471e751d046cf14fa`. Both confirmed "
         "by live\ncheck. First written August 16 at `227f5b2d`; the "
         "structure below is\nunchanged from that version and only the "
         "measured figures moved.\n",

         "**Updated August 19, 2026.** Orrery at\n`%s`, gallery at\n"
         "`%s`. Both confirmed by live\ncheck. First written August 16 "
         "at `227f5b2d`; the structure below is\nunchanged from that "
         "version. The figures moved, and one claim\nreversed: the "
         "first dispatch has now gone out and come back.\n"
         % (SHA, GALLERY)),

        ("As of August 18 that machinery is FINISHED and unused. A "
         "request can be\nbuilt for a chosen slice of rows, carried out "
         "as JSON, returned,\nchecked, routed, and written back into "
         "the code as an annotation the\nscanner accepts. The last inch "
         "closed on August 18: until then a\nreturned verdict could be "
         "checked and routed and then refused when\nsomebody tried to "
         "cite it, because the annotation grammar accepted only\na "
         "markdown reference. What has not happened is the first "
         "dispatch.\n",

         "That machinery was finished and unused for one day. A request "
         "can be\nbuilt for a chosen slice of rows, carried out as "
         "JSON, returned,\nchecked, routed, and written back into the "
         "code as an annotation the\nscanner accepts. The last inch "
         "closed on August 18: until then a\nreturned verdict could be "
         "checked and routed and then refused when\nsomebody tried to "
         "cite it, because the annotation grammar accepted only\na "
         "markdown reference.\n"
         "\n"
         "**The first dispatch went out the same day and came back.** "
         "Twenty-three\nrows from `constants_new.py` to three models in "
         "fresh chats. Sixty-nine\nanswered rows, and across all of "
         "them: no unparseable line, no missing\nor modified row hash, "
         "no duplicate key, no empty answer field, no token\noutside "
         "the vocabulary. The JSON format needed no fallback. The "
         "loop\nworks.\n"
         "\n"
         "What it found is in\n`documentation/PILOT_CONVERGENCE_"
         "20260819.md`. The headline: a\nprediction of 13 clear rows, "
         "written six days before dispatch, drew 17,\n10 and 11 from "
         "the three legs. All three planted trap rows failed to\n"
         "spring, which means the artifact conveys what it was built to "
         "convey.\nTen rows came back clean from all three models "
         "independently, and six\nwere flagged by all three.\n"),

        ("**Step one is in progress and the backlog is now visible.**",

         "**Step one is in progress, the backlog is visible, and the "
         "loop has now\nrun end to end.**"),

        ("**Step two is designed, not built.**\n",

         "The pilot also found two things worth acting on that no "
         "reading had\ncaught. `ALFVEN_SURFACE_RADII` measures from the "
         "photosphere while its\nsibling `PARKER_CLOSEST_RADII` "
         "measures from Sun centre -- two constants\nin one file, same "
         "spacecraft, one solar radius apart, which is a\nrendering "
         "defect rather than a documentation one if that shell "
         "draws\nfrom centre (L-209). And `STREAMER_BELT_RADII` cites a "
         "paper\ninverted: the cited 6 R_sun is that paper's FLOOR, and "
         "its actual\nresult is a lower bound three times larger "
         "(L-210).\n"
         "\n"
         "**Step two is designed, not built.**\n"),

        ("*Prepared August 16, 2026 with Anthropic's Claude Opus 5; "
         "figures\nupdated August 18. Built on\n"
         "`b65ac115fc0f820e8270c0807249813c67bde7bc` at\n"
         "https://github.com/tonylquintanilla/palomas_orrery, gallery "
         "at\n`ff18d3e6fa31f70a8f525df471e751d046cf14fa`.*\n",

         "*Prepared August 16, 2026 with Anthropic's Claude Opus 5; "
         "figures\nupdated August 18, dispatch result added August 19. "
         "Built on\n`%s` at\nhttps://github.com/tonylquintanilla/"
         "palomas_orrery, gallery at\n`%s`.*\n" % (SHA, GALLERY)),
    ]),

    # ============================================================
    # 2. MASTER_PLAN_INTERACTIVE_GALLERY.md -- Section 5a
    # ============================================================
    ('documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md', [

        ("### You are here -- 2026-08-18, orrery `b65ac11`, gallery "
         "`ff18d3e`\n",
         "### You are here -- 2026-08-19, orrery `%s`, gallery "
         "`ff18d3e`\n" % SHORT),

        ("| Segment 1, orrery | IN PROGRESS. Track 0 has no open "
         "rulings. The reconciliation is measured: 110 annotations "
         "scored, **8 clean**, 48 SEND BACK, 20 CONVERSATION, 34 noted, "
         "24 not scanner-reachable. The corpus grew and the clean count "
         "tripled because L-198 taught the scanner units it could not "
         "read -- coverage, not regression. Dispatch machinery COMPLETE "
         "as of August 18; 8 of the 9 August-16 blockers closed, the "
         "9th (ordinal context window) deliberately unexercised by the "
         "pilot. The first dispatch has not gone out. |\n",

         "| Segment 1, orrery | IN PROGRESS. Track 0 has no open "
         "rulings. The reconciliation is measured: 110 annotations "
         "scored, **8 clean**, 48 SEND BACK, 20 CONVERSATION, 34 noted, "
         "24 not scanner-reachable. The corpus grew and the clean count "
         "tripled because L-198 taught the scanner units it could not "
         "read -- coverage, not regression. Dispatch machinery COMPLETE "
         "as of August 18; 8 of the 9 August-16 blockers closed, the "
         "9th (ordinal context window) deliberately unexercised by the "
         "pilot. **The first dispatch went out and returned on August "
         "18**: 23 rows to three models, 69 answered rows, zero format "
         "defects, all three trap rows unsprung. Findings at L-209, "
         "L-210, L-211; evidence in "
         "`documentation/PILOT_CONVERGENCE_20260819.md`. |\n"),

        ("| Artifact 1, Earth | LOCKED (`artifact_1_earth_alone.json`). "
         "Proved propagation, the harness and the acceptance loop -- on "
         "an ORBIT. Exercised no features, which is how the feature "
         "path stayed broken unnoticed. |\n",

         "| Artifact 1, Earth | LOCKED (`artifact_1_earth_alone.json`). "
         "Proved propagation, the harness and the acceptance loop -- on "
         "an ORBIT. Exercised no features, which is how the feature "
         "path stayed broken unnoticed. |\n"
         "| L-207, citation prompt | BUILT August 18. The checker emits "
         "`documentation/prompts/citation_review.jsonl` every run -- 53 "
         "rows, one per key, carrying what the code cites and what each "
         "responder concluded. Closes the last leg of the loop: the "
         "citation half of a return now reaches a reader. |\n"),
    ]),

    # ============================================================
    # 3. MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md
    # ============================================================
    ('documentation/MASTER_PLAN_INTERACTIVE_GALLERY_SUMMARY.md', [

        ("Where we are 8/18/2026\n\nUpdated 2026-08-18 after the August "
         "17-18 sessions. Built on\nb65ac115fc0f820e8270c0807249813c67b"
         "de7bc at\n",
         "Where we are 8/19/2026\n\nUpdated 2026-08-19 after the August "
         "18 pilot session. Built on\n%s at\n" % SHA),

        ("The dispatch loop is FINISHED and unused. Fable 5 and GPT 5.6 "
         "Sol\nreviewed it blind on August 16; both said do not send it "
         "yet, and\nbetween them found nine structural blockers where "
         "two were known.\nEight are closed. The ninth -- the truncated "
         "ordinal context window --\nis deliberately not exercised by "
         "the pilot, since constants carry no\nordinals.\n",

         "The dispatch loop is FINISHED and unused. Fable 5 and GPT 5.6 "
         "Sol\nreviewed it blind on August 16; both said do not send it "
         "yet, and\nbetween them found nine structural blockers where "
         "two were known.\nEight are closed. The ninth -- the truncated "
         "ordinal context window --\nis deliberately not exercised by "
         "the pilot, since constants carry no\nordinals.\n"
         "\n"
         "  [2026-08-18: overtaken within a day. The loop RAN. "
         "Twenty-three rows\n  to Gemini, GPT and Claude in fresh "
         "chats; 69 answered rows; zero\n  format defects of any kind "
         "across all three returns, so the JSON\n  format needed no "
         "fallback. Full result:\n  "
         "documentation/PILOT_CONVERGENCE_20260819.md.]\n"),

        ("What opens the next session is the DISPATCH. The request is "
         "one file,\nreader-agnostic, 23 rows over constants_new.py, "
         "with every row's\nexpected disposition written down before it "
         "goes out\n(PILOT_EXPECTED_DISPOSITIONS_20260817.md: 13 clear, "
         "10 return, three\ntrap rows). If all 23 come back clear, that "
         "is agreement rather than\nsuccess, and the prediction file is "
         "what makes the difference\nvisible.\n",

         "What opens the next session is the DISPATCH. The request is "
         "one file,\nreader-agnostic, 23 rows over constants_new.py, "
         "with every row's\nexpected disposition written down before it "
         "goes out\n(PILOT_EXPECTED_DISPOSITIONS_20260817.md: 13 clear, "
         "10 return, three\ntrap rows). If all 23 come back clear, that "
         "is agreement rather than\nsuccess, and the prediction file is "
         "what makes the difference\nvisible.\n"
         "\n"
         "  [2026-08-18: it went out and came back the same day. The "
         "prediction\n  of 13 clears drew 17, 10 and 11 from the three "
         "legs. All three trap\n  rows failed to spring. Ten rows came "
         "back clean from every leg and\n  six were flagged by every "
         "leg. The warning above held: Gemini's 17\n  is the sweep it "
         "describes, and it carries the shortest notes of the\n  "
         "three. Result: documentation/PILOT_CONVERGENCE_20260819.md.]"
         "\n"),

        ("WHAT IS TRACKED RIGHT NOW -- 2026-08-18\n\n"
         "  Unstarted and unblocked\n"
         "    The pilot dispatch. 23 rows over constants_new.py, "
         "request built\n      by selection 2, sent as JSON with "
         "markdown as the fallback,\n      expected dispositions "
         "written before it goes out.\n",

         "WHAT IS TRACKED RIGHT NOW -- 2026-08-19\n\n"
         "  Unstarted and unblocked\n"
         "    L-209. ALFVEN_SURFACE_RADII origin mismatch -- 18.8 is an "
         "altitude\n      above the photosphere; the sibling row "
         "PARKER_CLOSEST_RADII at\n      9.86 is heliocentric. Confirm "
         "whether the shell draws from Sun\n      centre before "
         "editing: that decides render bug or comment bug.\n"
         "    L-210. Four pilot citation findings in constants_new.py. "
         "Streamer\n      first -- the DeForest citation is inverted, "
         "not merely loose.\n"
         "    L-211. Build UNKNOWN. The pre-registered trigger asked "
         "for two\n      rows and got seven.\n"
         "\n"
         "  Done this session\n"
         "    L-207, the citation prompt. 53 rows written every checker "
         "run.\n"
         "    The pilot dispatch itself, three legs, zero format "
         "defects.\n"),

        ("  Waiting on a ruling\n"
         "    Lazy responder: canaries, or remove the self-certifying "
         "field\n"
         "    Claim typing: real row types, or wait for a measured "
         "population\n"
         "    Cross-worksheet disagreement, what UNKNOWN does, pluto "
         "614/638,\n      transition sequencing, whether batching "
         "becomes real\n",

         "  Waiting on a ruling\n"
         "    Whether a VISUALIZATION BOUNDARY is verdictable at all. "
         "All three\n      legs declined to confirm INNER_CORONA_RADII "
         "and split on what\n      kind of thing it is. The "
         "artifact-bounds question arriving as a\n      worksheet row "
         "rather than as an argument.\n"
         "    Whether Gemini stays a leg of record. It cleared 17 of "
         "23 with the\n      shortest notes in the batch and confirmed "
         "both rows the other two\n      refused.\n"
         "    Whether the pilot is finished. Nothing has been written "
         "back into\n      the code as an annotation yet, and the pilot "
         "was scoped to end at\n      re-verification in code.\n"
         "    Lazy responder: canaries, or remove the self-certifying "
         "field.\n      Note L-207 may have answered this -- a "
         "reviewer disagreeing with a\n      responder's citation "
         "verdict is now measured per row.\n"
         "    Claim typing: real row types, or wait for a measured "
         "population\n"
         "    Cross-worksheet disagreement, pluto 614/638, transition "
         "sequencing,\n      whether batching becomes real\n"),

        ("  Carried as an obligation\n"
         "    Confirm provenance-discipline loads at 2.4 before "
         "provenance work\n",

         "  Carried as an obligation\n"
         "    Confirm provenance-discipline loads at 2.5 before "
         "provenance work.\n      [2.4 was confirmed and discharged on "
         "August 18; the skill went to\n      2.5 the same session and "
         "a mid-session reinstall cannot be verified\n      from inside "
         "the session that makes it. One session later a fresh\n      "
         "chat reported loading 2.5, which is the first independent\n"
         "      confirmation.]\n"
         "    Add the dispatch-hygiene rule to provenance-discipline: a "
         "fresh\n      chat is not enough, it must be OUTSIDE any "
         "project. A new chat\n      inside the Paloma's Orrery project "
         "inherits memory naming the\n      pilot's trap rows, which "
         "turns row-checking into trap-hunting. Found\n      when a "
         "responder refused the job for that reason.\n"),

        ("Entry written August 2026 with Anthropic's Claude Opus 5. "
         "Updated\nAugust 18, 2026, built on "
         "b65ac115fc0f820e8270c0807249813c67bde7bc;\ngallery at "
         "ff18d3e6fa31f70a8f525df471e751d046cf14fa.\n",

         "Entry written August 2026 with Anthropic's Claude Opus 5. "
         "Updated\nAugust 19, 2026, built on %s;\ngallery at %s.\n"
         % (SHA, GALLERY)),
    ]),
]


def fingerprint(data):
    return hashlib.md5(data.replace(b'\r\n', b'\n')).hexdigest()


def fail(message):
    print('ERROR: %s' % message)
    print('Nothing was written.')
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)

    for name, expected in sorted(BASE.items()):
        if not os.path.isfile(name):
            return fail('%s not found. Save this script in the repo '
                        'root and run it there.' % name)
        with open(name, 'rb') as handle:
            found = fingerprint(handle.read())
        if found != expected:
            return fail('%s has moved since this patch was built '
                        '(expected %s, found %s).'
                        % (name, expected, found))

    # Inserted text is ASCII. These files are prose and may already
    # carry non-ASCII; that is reported, not swept, because two of the
    # three quote responder text and normalising a quotation is
    # interpretation.
    for _name, edits in EDITS:
        for _anchor, replacement in edits:
            try:
                replacement.encode('ascii')
            except UnicodeEncodeError as exc:
                return fail('this patch would insert non-ASCII: %s' % exc)

    staged = {}
    for name, edits in EDITS:
        with open(name, 'rb') as handle:
            data = handle.read()
        crlf = data.count(b'\r\n') > 0
        for anchor, replacement in edits:
            old = anchor.encode('ascii')
            new = replacement.encode('ascii')
            if crlf:
                old = old.replace(b'\n', b'\r\n')
                new = new.replace(b'\n', b'\r\n')
            count = data.count(old)
            if count != 1:
                print('ANCHOR FAIL: %s -- expected 1 match, found %d '
                      'for %r' % (name, count, anchor[:70]))
                print('Nothing was written.')
                return 1
            data = data.replace(old, new)
        left = sum(1 for byte in data if byte > 127)
        staged[name] = (data, left)

    for name, (data, left) in sorted(staged.items()):
        with open(name, 'wb') as handle:
            handle.write(data)
        note = ''
        if left:
            note = ('  [note: %d pre-existing non-ASCII byte(s), left '
                    'alone -- prose quoting responders]' % left)
        print('  ok  %s (%d bytes)%s' % (name, len(data), note))

    print('patch applied')
    return 0


if __name__ == '__main__':
    sys.exit(main())
