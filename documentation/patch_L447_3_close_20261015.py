#!/usr/bin/env python3
"""
patch_L447_3_close_20261015.py -- closes L-447 (the front page's words)
on Tony's look ("perfect"), records on L-446 tonight's Cache in step
failure, and opens a small item for the test file the maintenance run
writes into the repository.

Built on orrery 464d872b1b3f09a1003fe7e81aea399593145a6a at
https://github.com/tonylquintanilla/palomas_orrery; the gallery read at
db63b7d763b6be8c6933ac3c5f40511ad334a800 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io and not
touched.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L447_3_close_20261015.py

    Save this file in the ORRERY folder above, open it in VS Code and
    click Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in three files

    LEDGER_CONSOLIDATED.md    L-447 to DONE, with Tony's runs and look;
                              a note on L-446; a new item, given the next
                              free handle when it runs, for
                              test_output/test_orbit_paths.json; header
                              stamp
    documentation/WHERE_WE_ARE.md   above the run-record marker only:
                              the date, the box
    documentation/HANDOFF_L447_front_page_words_20261015.md
                              the push SHAs, and a section for the close

    Each file is checked only at the lines edited.

WHAT IT PRINTS

    Success: one "ok" line per edit, the new item's handle, then "patch
    applied". Failure: one ERROR or ANCHOR FAIL line and "NOTHING was
    written."

Undo is Discard Changes in GitHub Desktop.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
HANDOFF = "documentation/HANDOFF_L447_front_page_words_20261015.md"
MARKER = "--- Your run record below this line"
WWA_CAP = 130


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the orrery folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def rep(text, old, new, label, log, rel):
    n = text.count(old)
    if n != 1:
        raise PatchError("ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r"
                         % (rel, label, n, old[:70]))
    log.append("ok  %-58s %s" % (rel, label))
    return text.replace(old, new)


L447_META_OLD = "<!-- L:447 status:OPEN upd:2026-10-15 section:A flag: rice: -->"
L447_META_NEW = "<!-- L:447 status:DONE upd:2026-10-15 section:C flag: rice: -->"

L447_GAP_OLD = """**Gap:** Tony's look at the front page on his phone (the acceptance);
then close.
"""
L447_GAP_NEW = """- **Run and pushed, 2026-10-15** (Tony's run record, the copy of
  `documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md` he uploaded
  at 20:36): the gallery patch "patch applied (13 edits in 2 files)",
  pushed at db63b7d; the orrery records patch, pushed at 8e50aea. His
  gallery maintenance run: 26 of 27, the one failure Cache in step for
  Saturn, Uranus and Neptune, which is not this item's: the periods
  reached the website's config in that run and the cache builder had
  not run since (recorded on L-446). The live run: 2 of 2.
- **Tony's look, 2026-10-15:** "perfect."
- **Loose ends:** none. The Cache in step failure is L-446's, noted
  there; the test file Tony saw committed is L-{H}.
**Gap:** none. Closed 2026-10-15.
"""

L446_GAP_OLD = """**Gap:** a small gallery build, its own session: the pulls and copies
ahead of the builder;"""
L446_GAP_NEW = """- **Seen 2026-10-15, in Tony's gallery maintenance run after L-447**
  (gallery db63b7d): Cache in step failed for Saturn, Uranus and
  Neptune -- "the config's period is around @0, the cache draws its
  orbit around the Sun". The maintenance run had just pulled L-444's
  periods into the config, and the builder last ran at 10:36, before
  them. This item's order removes that gap; until it is built, the next
  Daily Run's builder clears it.
**Gap:** a small gallery build, its own session: the pulls and copies
ahead of the builder;"""

NEW_ITEM = """#### [L-{H}] The maintenance run writes a test file into the tracked tree (orrery, maintenance)
<!-- L:{H} status:OPEN upd:2026-10-15 section:A flag: rice: -->
- **Seen by Tony, 2026-10-15,** pushing L-447's records: "test_orbit_paths.json
  was pushed." `test_output/test_orbit_paths.json` is a fixed fixture
  that `test_orbit_cache.py` writes on every maintenance run (a valid and
  a deliberately corrupted entry, dated 2025). It is tracked, and has
  been since at least 87a5470 (2026-10-13). At 8e50aea it was caught
  deleted mid-run and committed as a deletion, and 464d872 put it back
  with the same bytes, so the repository gained two commits and no
  change.
**Gap:** stop tracking it: the test writes it into a folder git ignores
(or a temporary folder), and the file leaves the repository in the same
patch. Small; ride a session already touching the maintenance run.
**Ref:** `test_orbit_cache.py`; `.gitignore`; L-447.

"""

STAMP_ANCHOR = "Review and RICE update Tony 6-21-2026\n"
STAMP = ("Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5\n"
         "(L-447 closed on Tony's look; a note on L-446; L-{H} opened, the\n"
         "test file in the tracked tree), built on 464d872b.\n" + STAMP_ANCHOR)

WWA_EDITS = [
    ("header",
     """Last updated: October 15, 2026, evening: the front page's words.
- Written at orrery 47d241b and gallery 9f8569e.
""",
     """Last updated: October 15, 2026, night: the front page's words done.
- Written at orrery 464d872 and gallery db63b7d.
"""),
    ("changed since you last read this",
     """> - Built: the front page says what the site is: L-447 (its words).
""",
     """> - Done: the front page says what the site is: L-447 (its words).
"""),
    ("needs you now",
     """> - *Run the two L-447 patches; look at the front page on your phone.*
""",
     """> - *Run patch_L447_3_close; one Daily Run clears Cache in step.*
"""),
]

HANDOFF_EDITS = [
    ("pushed at",
     "Pushed at: (Tony's commits after his run).\n",
     "Pushed at: gallery db63b7d7 and orrery 8e50aea (2026-10-15).\n"),
    ("the close",
     "Session record written October 2026 with Anthropic's Claude Opus 5.5.\n",
     """## 6. Tony's run, his look, and the close (added 2026-10-15)

- Both patches applied and were pushed: gallery db63b7d, orrery
  8e50aea. Tony's look on the phone: "perfect." L-447 closed by
  `patch_L447_3_close_20261015.py`.
- His gallery maintenance run failed one checker, Cache in step, for
  Saturn, Uranus and Neptune: L-444's periods had just reached the
  website's config, and the cache builder had not run since. Not this
  item's; recorded on L-446, and the next Daily Run clears it.
- He saw `test_output/test_orbit_paths.json` committed. It is a test
  fixture the maintenance run writes, tracked since at least
  2026-10-13; opened as L-{H}.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
"""),
]


def next_handle(text):
    return max(int(n) for n in re.findall(r"\bL-(\d{3,4})\b", text)) + 1


def main():
    log = []
    try:
        led, led_crlf = read(LEDGER)
        if L447_META_NEW in led:
            raise PatchError("L-447 is already closed; this patch has run")
        H = "%d" % next_handle(led)
        led = rep(led, L447_META_OLD, L447_META_NEW, "L-447 to DONE", log, LEDGER)
        led = rep(led, L447_GAP_OLD, L447_GAP_NEW.replace("{H}", H),
                  "L-447 run and look recorded", log, LEDGER)
        led = rep(led, L446_GAP_OLD, L446_GAP_NEW, "L-446 note: Cache in step",
                  log, LEDGER)
        anchor = "#### [L-447] The website's front page"
        if led.count(anchor) != 1:
            raise PatchError("ANCHOR FAIL [%s L-447 header]" % LEDGER)
        i = led.index(anchor)
        led = led[:i] + NEW_ITEM.replace("{H}", H) + led[i:]
        log.append("ok  %-58s L-%s opened, the test file" % (LEDGER, H))
        led = rep(led, STAMP_ANCHOR, STAMP.replace("{H}", H), "header stamp",
                  log, LEDGER)

        wwa, wwa_crlf = read(WWA)
        if wwa.count(MARKER) != 1:
            raise PatchError("ANCHOR FAIL [%s run-record marker]" % WWA)
        cut = wwa.index(MARKER)
        top, bottom = wwa[:cut], wwa[cut:]
        for label, old, new in WWA_EDITS:
            top = rep(top, old, new, label, log, WWA)
        above = top.count("\n")
        if above > WWA_CAP:
            raise PatchError("%s would stand %d lines above the marker (cap %d)"
                             % (WWA, above, WWA_CAP))
        log.append("ok  %s: %d lines above the marker (cap %d)"
                   % (WWA, above, WWA_CAP))
        wwa = top + bottom

        ho, ho_crlf = read(HANDOFF)
        for label, old, new in HANDOFF_EDITS:
            ho = rep(ho, old, new.replace("{H}", H), label, log, HANDOFF)

        out = {LEDGER: (led, led_crlf), WWA: (wwa, wwa_crlf),
               HANDOFF: (ho, ho_crlf)}
        for rel, (text, _c) in out.items():
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s)" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        sys.exit(1)

    notes = []
    for rel, (text, crlf) in out.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log + notes:
        print(line)
    print("stamps updated: the ledger's header; Where We Are's date; the "
          "build record's push line")
    print("")
    print("The new item is L-%s (the test file in the tracked tree)." % H)
    print("patch applied (3 files)")
    print("")
    print("NEXT:")
    print("  1. Move this script into documentation/ first; then run")
    print("     orrery_maintenance_run.py; commit and push the orrery.")
    print("  2. In the gallery, run the Daily Run once; commit and push.")
    print("     Its maintenance run's Cache in step should then pass.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
