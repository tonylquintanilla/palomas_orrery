#!/usr/bin/env python3
"""
patch_L281_4_dashboard_and_ledger.py -- the Daily Run on the dashboard,
and L-281 brought up to date (L-281, step 4). ORRERY repo.

RUN: save this file in the ORRERY repo root (the folder that holds
palomas_orrery_dashboard.py), open it in VS Code and click Run.

WHAT IT DOES, all or nothing:
  palomas_orrery_dashboard.py
    - a new group, Daily Run, above the gallery groups: the Daily Run
      button, and indented under it the Guest Book Updater, the Gallery
      Cache Builder -- Manual Run (MOVED here from Gallery -- checks and
      data, with its description unchanged) and the offline maintenance
      run
    - Guest Book Checks among the gallery's checkers, in alphabetical
      place (Tony's request, 2026-09-27)
    - the offline maintenance run's description now names every check
      it runs; it said "six Node suites" and named six of eight
    - the docstring's change note
  LEDGER_CONSOLIDATED.md
    - L-281 rewritten as built: Cusdis gone, Tony's design, the four
      patches, what is left. Its history is kept.
    - the header stamp

After it: run the orrery maintenance run, which regenerates the ledger
index from the new L-281 block. The Daily Run group works only once the
gallery's patch_L281_3_daily_run.py has been run and pushed.

It writes NOTHING unless both files are the ones it was built against
(orrery e0a0c7cc). Undo is Discard Changes in GitHub Desktop.
One-shot: once it has run, move it to documentation/.

Written September 27, 2026 with Anthropic's Claude Opus 5.5.
"""

import hashlib
import os
import sys

BASE = "e0a0c7cc"

EXPECTED = {
    "palomas_orrery_dashboard.py": "922a1e58e75f89430854e5206961db4b",
    "LEDGER_CONSOLIDATED.md": "019ed74bbba00834783a2fffe8b6000a",
}

EDITS = {
    "palomas_orrery_dashboard.py": [
        ("change note", b'Report\'s description no longer says it is report-only.\n"""\n', b'Report\'s description no longer says it is report-only.\nSeptember 27, 2026 with Anthropic\'s Claude Opus 5.5 (L-281, patch 4),\non Tony\'s design: a Daily Run group above the gallery groups. Its top\nbutton runs daily_run.py in the gallery repo -- the guest book updater,\nthen the cache build after the OneDrive pause, then the offline\nmaintenance run -- and the three are indented under it. Gallery Cache\nBuilder -- Manual Run MOVED here from Gallery -- checks and data, its\ndescription unchanged; the offline runner appears in both groups, the\nfull description staying in the gallery group. Guest Book Checks added\nto the checkers in alphabetical place, on Tony\'s request. The offline\nrunner\'s description now names all it runs: it said "six Node suites"\nwhile the runner had eight.\n"""\n'),
        ("Daily Run group; builder moved into it", b'    "Stars": [\n        ("Star Visualization",\n         "star_visualization_gui.py",\n         "HR diagrams, stellar neighborhoods, and the Milky Way"),\n    ],\n\n    "Gallery -- checks and data": [\n        ("Gallery Cache Builder -- Manual Run",\n         os.path.join("tools", "gallery_cache_builder.py"),\n         "Manual serving-cache build. Runs from the gallery repo ROOT: the "\n         "builder resolves its data/ paths from the working directory, so "\n         "launching it from tools/ cannot find data/objects_config.json. "\n         "With no flags it fetches from Horizons, validates, atomic-swaps "\n         "the new cache into data/solar-system, and STOPS -- it does not "\n         "commit or push. Commit it yourself in GitHub Desktop after the "\n         "run finishes. Do not commit while it is still running: mid-build "\n         "the working tree shows deletions only, which is the swap in "\n         "progress, not data loss. The console stays open at the repo root "\n         "if you want a flagged re-run (--dry-run --object <slug>, "\n         "--first-build).\\n"\n         "\\n"\n         "THE ROUTINE (L-216). Pause OneDrive syncing and NOTE THE TIME -- "\n         "a pause lasts 2 hours -- then run the build. It ends with a "\n         "[SWAP] line saying how the swap went, and then prints its own "\n         "numbered next steps. Follow them: run Gallery Maintenance Run -- "\n         "offline BEFORE you commit, and check that its last line agrees "\n         "with the [SWAP] line; then look at GitHub Desktop\'s change list, "\n         "commit and push. The swap retries a refused rename for about "\n         "fifty seconds and puts the PREVIOUS cache back if it still "\n         "cannot finish, so you are never left without one. A swap that "\n         "took more than one attempt is a refusal the builder absorbed, "\n         "and those two lines are the only way you will know.",\n         GALLERY_REPO_DIR,\n         True),\n', b'    "Stars": [\n        ("Star Visualization",\n         "star_visualization_gui.py",\n         "HR diagrams, stellar neighborhoods, and the Milky Way"),\n    ],\n\n    "Daily Run": [\n        ("Daily Run -- everything indented below",\n         "daily_run.py",\n         "What the gallery needs once a day, in one window, in this order "\n         "(L-281, Tony\'s design of 2026-09-27). First the Guest Book "\n         "Updater: approve or decline each new message, and write entries "\n         "or replies if you like. Then it asks you to pause OneDrive and "\n         "note the time, and runs the Gallery Cache Builder; type s at "\n         "that question to skip the build today. Then the Gallery "\n         "Maintenance Run, offline, which the builder\'s own next steps "\n         "ask for before a commit. A step that reports a problem does not "\n         "stop the next one. It ends with one summary naming each step\'s "\n         "result and what is left for you: commit and push in GitHub "\n         "Desktop, the live maintenance run, and resuming OneDrive. It "\n         "opens by saying when the last cache build was, so a missed day "\n         "shows. It never commits or pushes. Everything indented below is "\n         "included in it and can still be run on its own.",\n         GALLERY_REPO_DIR,\n         True),\n        ("Guest Book Updater",\n         os.path.join("tools", "guestbook_updater.py"),\n         "The lobby\'s guest book (L-281). Fetches the messages visitors "\n         "sent through the Google Form and shows each one you have not "\n         "decided on: a to approve, d to decline, l to decide later. A "\n         "rating or other answer the form collects is shown to you beside "\n         "the message and never published. Then a menu: write an entry of "\n         "your own, reply under an entry, remove an entry, or set the "\n         "form\'s address, which turns on the lobby\'s Sign the guest book "\n         "link. Your entries and replies can link to gallery pages -- type "\n         "a room such as solar_system/earth, a card\'s id, or an exhibit "\n         "such as earth -- and a misspelt one is refused. It changes only "\n         "data/guestbook.json and says when that needs a commit. Run it "\n         "alone as often as you like; it is also the Daily Run\'s first "\n         "step. The private address of the form\'s responses is kept in "\n         "tools/guestbook_local.json, which git ignores.",\n         GALLERY_REPO_DIR,\n         True,\n         None,\n         True),\n        ("Gallery Cache Builder -- Manual Run",\n         os.path.join("tools", "gallery_cache_builder.py"),\n         "Manual serving-cache build. Runs from the gallery repo ROOT: the "\n         "builder resolves its data/ paths from the working directory, so "\n         "launching it from tools/ cannot find data/objects_config.json. "\n         "With no flags it fetches from Horizons, validates, atomic-swaps "\n         "the new cache into data/solar-system, and STOPS -- it does not "\n         "commit or push. Commit it yourself in GitHub Desktop after the "\n         "run finishes. Do not commit while it is still running: mid-build "\n         "the working tree shows deletions only, which is the swap in "\n         "progress, not data loss. The console stays open at the repo root "\n         "if you want a flagged re-run (--dry-run --object <slug>, "\n         "--first-build).\\n"\n         "\\n"\n         "THE ROUTINE (L-216). Pause OneDrive syncing and NOTE THE TIME -- "\n         "a pause lasts 2 hours -- then run the build. It ends with a "\n         "[SWAP] line saying how the swap went, and then prints its own "\n         "numbered next steps. Follow them: run Gallery Maintenance Run -- "\n         "offline BEFORE you commit, and check that its last line agrees "\n         "with the [SWAP] line; then look at GitHub Desktop\'s change list, "\n         "commit and push. The swap retries a refused rename for about "\n         "fifty seconds and puts the PREVIOUS cache back if it still "\n         "cannot finish, so you are never left without one. A swap that "\n         "took more than one attempt is a refusal the builder absorbed, "\n         "and those two lines are the only way you will know.",\n         GALLERY_REPO_DIR,\n         True,\n         None,\n         True),\n        ("Gallery Maintenance Run -- offline",\n         "gallery_maintenance_run.py",\n         "The Daily Run\'s third step: the same button as Gallery "\n         "Maintenance Run -- offline under Gallery -- checks and data, "\n         "which describes it in full. Run after the build and before you "\n         "commit.",\n         GALLERY_REPO_DIR,\n         True,\n         None,\n         True),\n    ],\n\n    "Gallery -- checks and data": [\n'),
        ("offline runner description", b'        "The gallery repo\'s own runner (L-236), before you commit. "\n        "Regenerates the module atlas, pulls the orrery\'s constants "\n        "export at its HEAD SHA and mirrors the served numbers into "\n        "data/objects_config.json, then runs the cache builder suite, "\n        "the mirror suite, the config mirror check, the pointer join, "\n        "the cache-in-step check, the six Node suites (feature "\n        "renderers, page framing, Sun shells, Earth scene geometry, "\n        "hover budget, arrival), and the artifact-1 assembler "\n        "test. Three states rather than two: a suite that could "\n        "not run -- Node missing, say -- reports UNREACHABLE and is "\n        "never counted as a pass. Everything indented below is included "\n        "in it.",\n', b'        "The gallery repo\'s own runner (L-236), before you commit. "\n        "Regenerates the module atlas, pulls the orrery\'s constants "\n        "export at its HEAD SHA and mirrors the served numbers into "\n        "data/objects_config.json, then runs every checker and prints "\n        "one line each. Python: the cache builder suite, pole of date, "\n        "the mirror suite, the store writer and store editor suites, "\n        "the config mirror check, the pointer join, cache in step, the "\n        "guest book updater, the Daily Run\'s steps, the artifact-1 "\n        "assembler pin, and cache siblings (report only). Node: feature "\n        "renderers, page framing, Sun shells, Earth scene geometry, "\n        "hover budget, arrival, display figures, and the guest book. "\n        "Three states rather than two: a suite that could not run -- "\n        "Node missing, say -- reports UNREACHABLE and is never counted "\n        "as a pass. The indented buttons below launch some of these "\n        "one at a time.",\n'),
        ("Guest Book Checks", b'        ("Hover Budget",\n', b'        ("Guest Book Checks",\n        os.path.join("documentation", "run_guestbook_checks.py"),\n        "Both checks for the lobby\'s guest book (L-281), which the "\n        "gallery runner also runs. Guest book: the page\'s own drawing "\n        "code on the real data/guestbook.json -- newest first, every "\n        "piece of text escaped so nothing a visitor types can become part "\n        "of the page, no link ever drawn on a visitor\'s entry, and only "\n        "links to this gallery\'s own pages. Guest book updater: the tool "\n        "in three scripted runs on made-up messages, including the case "\n        "where the form has no message or note column, which it must "\n        "refuse rather than guess. Each suite first proves it can fail. "\n        "The first is Node; this is the Python wrapper the dashboard "\n        "needs. GATES the gallery runner.",\n        GALLERY_REPO_DIR,\n        True,\n        None,\n        True),\n        ("Hover Budget",\n'),
        ("section symbol", b'    "Gallery -- checks and data": "",\n', b'    "Daily Run": "",\n    "Gallery -- checks and data": "",\n'),
    ],
    "LEDGER_CONSOLIDATED.md": [
        ("header stamp", b'b9cd4844.\nReview and RICE update Tony 6-21-2026\n', b"b9cd4844.\nModule updated: September 27, 2026 with Anthropic's Claude Opus 5.5\n(L-281 as built: Cusdis dropped because it has shut down; the guest book\nkept in the gallery repo, fed by a Google Form and Tony's approval; the\nDaily Run), built on e0a0c7cc.\nReview and RICE update Tony 6-21-2026\n"),
        ("L-281 metadata", b'<!-- L:281 status:OPEN upd:2026-09-03 section:A flag: rice:3/2/70/1 -->', b'<!-- L:281 status:OPEN upd:2026-09-27 section:A flag: rice:3/2/70/1 -->'),
        ("L-281 Cusdis decision superseded", b'- **Tony-action (decide):** Cusdis hosted free tier to start, or wait\n  until the hall exists. Adds a third-party script to a public page.\n', b'- **Tony-action (decide), SUPERSEDED 2026-09-26:** Cusdis hosted free\n  tier to start, or wait until the hall exists. Adds a third-party\n  script to a public page. (Cusdis has shut down; see the 2026-09-26\n  note below for what replaced it.)\n'),
        ("L-281 as built", b'**Gap:** decision; then a Cusdis account, the two-line embed at the\nbottom of the lobby (L-282), and a line in the placard saying comments\nare read before they appear.\n**Ref:** L-282 (was L-280); https://cusdis.com/;\nhttps://github.com/djyde/cusdis.\n', b'- **Note 2026-09-26: Cusdis has shut down.** Its own GitHub README now\n  opens by saying the project is deprecated and asks users to email for\n  an export of their data [verified 2026-09-26, github.com/djyde/cusdis].\n  A competitor\'s blog dates the archive to 2026-07-17 [not independently\n  confirmed]. If that date is right, the recommendation above was\n  written after the shutdown and was never checked against it.\n- **Tony\'s decision, 2026-09-26: the entries are kept in the gallery\n  repo.** No outside service on the page and no email in the loop. A\n  visitor fills in a Google Form. The form\'s responses sheet is\n  published as CSV at a private address. A tool Tony runs fetches the\n  submissions, and he approves, declines or defers each one. Approved\n  entries go into data/guestbook.json, which the lobby reads. Tony can\n  also write his own entries and public replies, with links to gallery\n  pages. Entries show newest first (Tony, 2026-09-26). A Daily Run\n  umbrella groups the updater with the cache builder, to be run first\n  thing each day; the updater can also be run alone (Tony, 2026-09-27).\n- **Built, four patches:**\n  - Patch 1, gallery, pushed at 70a77347: gallery/guestbook.js draws\n    the book; data/guestbook.json holds it; the check\n    documentation/smoke_guestbook.js (7 checks, which first prove they\n    can fail on a broken renderer); the lobby\'s "Under construction" row\n    replaced; the --live pass fetches both files. [verified: Tony\'s run\n    record, the live pass matched both files byte for byte]\n  - Patch 2, gallery, pushed at 9b787f99: tools/guestbook_updater.py\n    and tools/test_guestbook_updater.py; .gitignore keeps\n    tools/guestbook_local.json -- the private address and fingerprints\n    of decided messages, never their words -- out of the public repo.\n  - Patch 3, gallery, built on 9b787f99: daily_run.py and its\n    --check row in the gallery runner; documentation/\n    run_guestbook_checks.py for the dashboard; the updater finds the\n    message by a heading containing "message" or "note", with no\n    fallback to a column by position, and shows the form\'s other\n    answers to Tony privately.\n  - Patch 4, orrery, built on e0a0c7cc: the dashboard\'s Daily Run\n    group (the Gallery Cache Builder button moved into it), Guest Book\n    Checks, and this block.\n- **The safety rules live in the page, not only in the tool.** All text\n  is escaped. Links are drawn only on Tony\'s entries and replies, and\n  only to #card, #room=path or interactive.html?exhibit=name. The sign\n  link appears only for a Google Forms address.\n- **The form as Tony built it, 2026-09-27:** a name, an overall rating,\n  and "Leave a note about the gallery". An email question and a\n  favourite-exhibit question were deleted from the form. Their columns\n  stay hidden in the sheet, because Google will not delete a column\n  linked to a form. The first updater would have read the email column\n  as the message: no heading contained "message", and it fell back to\n  the third column. Caught from Tony\'s screenshot before any run; patch\n  3 removes the fallback, and the test now covers that sheet.\n- **Note:** the .lobby-row styles in index.html are no longer used by\n  anything. Left in place; remove on the next index.html patch.\n**Gap:**\n- Tony-action (do): run patch 3 in the gallery and patch 4 in the\n  orrery; each repo\'s maintenance run; commit and push both.\n- Tony-action (do): finish the form setup at step 5 -- publish the\n  responses sheet as CSV -- then send a test message, and run the\n  updater once: paste the address, decline the test, set the form\n  address with f, commit and push.\n- Mode 5: Tony looks at the lobby once the Sign the guest book link is\n  live, on the desktop and the phone.\n- Close when a real visitor\'s message has been approved and appears.\n**Ref:** L-282 (the lobby); L-216 (the OneDrive pause before a build);\ngallery 70a77347 and 9b787f99. The form lives in Tony\'s Google account\nas "Paloma\'s Orrery Guest Book". Kept for the record:\nhttps://cusdis.com/; https://github.com/djyde/cusdis.\n'),
    ],
}


def fingerprint(data):
    return hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest()


def fail(message):
    print("FAILURE: " + message)
    print("NOTHING was written. Undo is Discard Changes in GitHub Desktop.")
    sys.exit(1)


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(root, "palomas_orrery_dashboard.py")):
        fail("palomas_orrery_dashboard.py is not beside this script. Save it "
             "in the ORRERY repo root (palomas_orrery) and run it again.")
    results = {}
    for name, want in EXPECTED.items():
        with open(os.path.join(root, name), "rb") as f:
            data = f.read()
        got = fingerprint(data)
        if got != want:
            fail("%s is not the file this patch was built against (orrery "
                 "%s). Expected %s, found %s." % (name, BASE, want, got))
        crlf = b"\r\n" in data
        text = data.replace(b"\r\n", b"\n")
        for label, old, new in EDITS[name]:
            n = text.count(old)
            if n != 1:
                fail("ANCHOR FAIL in %s, edit '%s': expected 1 match, found %d."
                     % (name, label, n))
            if any(b > 127 for b in new):
                fail("edit '%s' carries non-ASCII bytes." % label)
            text = text.replace(old, new)
        if crlf:
            text = text.replace(b"\n", b"\r\n")
        results[name] = (text, [e[0] for e in EDITS[name]], crlf)
    for name, (text, labels, crlf) in results.items():
        with open(os.path.join(root, name), "wb") as f:
            f.write(text)
        for label in labels:
            print("ok   %s: %s" % (name, label))
        print("     %s written (%d bytes%s)" % (name, len(text), ", CRLF kept" if crlf else ""))
    print("stamps updated: dashboard docstring change note, ledger header")
    print("patch applied")
    print("")
    print("NEXT: run the orrery maintenance run -- it regenerates the ledger")
    print("index from the new L-281 block -- then commit and push.")


if __name__ == "__main__":
    main()
