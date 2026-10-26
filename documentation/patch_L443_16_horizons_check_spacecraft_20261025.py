r"""patch_L443_16_horizons_check_spacecraft_20261025.py -- the Horizons check
reads JPL's empty answer for a spacecraft (L-443), and the evening's record.

Built on orrery d80aed3e95ad9e8ea0d41bcb7c4ad9cda3ce6c78 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).

WHAT IT FIXES

    Your maintenance run of Oct 25 said JPL could not be reached, at
    Voyager 1's identity. JPL was reached. Asked about a spacecraft's id
    in its small-body index, JPL's Lookup answers with its two header
    lines and nothing else, and the check read that as a failed fetch.
    It now reads that answer as "no matches". Any other unread line
    still fails. The check's suite gains a recorded Voyager 1 case and a
    planted fault.

WHAT IT EDITS

    horizons_check.py, test_horizons_check.py; LEDGER_CONSOLIDATED.md
    (your runs and the two fixes on L-443, the new L-487),
    documentation/WHERE_WE_ARE.md, and the build B handoff's section 6.

HOW TO RUN

    Open it in VS Code and press Run. It prints an "ok" line per file,
    then "patch applied". All or nothing: if any edit cannot be placed,
    nothing is written. A second run refuses. Then run
    orrery_maintenance_run.py with the internet on.

Written October 25, 2026 with Anthropic's Claude Opus 5.5.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DONE = 'patch applied: the Horizons check and a spacecraft, Oct 25 (%d files edited, %d new)'
EDITS = [('horizons_check.py', [('Earth\'s period: the period is asked of the target its record names, and\nthe confirmation records that target.)\n"""\n\n', 'Earth\'s period: the period is asked of the target its record names, and\nthe confirmation records that target.)\nModule updated: October 25, 2026 with Anthropic\'s Claude Opus 5.5 (L-443,\nthe twelve spacecraft: JPL\'s answer of its header alone, which is how\nthe Lookup answers a spacecraft\'s id in the small-body index, is read as\nno matches instead of as JPL unreachable.)\n"""\n\n'), ('        elif current is not None and key == "Primary designation":\n            current["designation"] = value\n    if not found and "no matches found" not in text:\n        raise Unreachable("the Lookup answer names no object and does not "\n                          "say \'no matches found\'")\n    return found\n\n\n', '        elif current is not None and key == "Primary designation":\n            current["designation"] = value\n    if not found and "no matches found" not in text and not bare(text):\n        raise Unreachable("the Lookup answer names no object and does not "\n                          "say \'no matches found\'")\n    return found\n\n\ndef bare(text):\n    """True when JPL\'s answer is its two header lines and nothing else.\n\n    L-443, 2026-10-25: JPL\'s Lookup answers a spacecraft\'s id (negative,\n    -31 for Voyager 1) in the small-body index with its header alone --\n    "API VERSION: 1.1" and "API SOURCE: NASA/JPL Horizons Lookup API",\n    no object and no "no matches found" notice (fetched that day, -31 and\n    -61 in group=sb). That is an empty index, not a failed fetch; until\n    then the first spacecraft stopped the whole run as UNREACHABLE. Any\n    other line still means the answer was not read, and still fails."""\n    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]\n    return bool(lines) and all(ln.startswith(("API VERSION:", "API SOURCE:"))\n                               for ln in lines)\n\n\n')]), ('test_horizons_check.py', [("       gave to another comet; a wrong object_type on the barycentre; JPL\n       unreachable; an answer that is not JPL's; a comet whose record\n       list cannot be fetched.\n    3. The period (L-431): Mercury, Jupiter and Encke agree with JPL's PR\n       at their own date and centre. Planted: a PR farther from the\n", "       gave to another comet; a wrong object_type on the barycentre; JPL\n       unreachable; an answer that is not JPL's; a comet whose record\n       list cannot be fetched. (L-443) A spacecraft, Voyager 1, agrees:\n       the small-body index answers its id with JPL's header alone, which\n       is no matches; planted: the same header with any other line is\n       still JPL not read, never a pass.\n    3. The period (L-431): Mercury, Jupiter and Encke agree with JPL's PR\n       at their own date and centre. Planted: a PR farther from the\n"), ('planted copy of the check asking the body\'s own id, on JPL\'s answers for\ntarget 3 in documentation/worksheets/period_answers_L445.json.)\n"""\n\n', 'planted copy of the check asking the body\'s own id, on JPL\'s answers for\ntarget 3 in documentation/worksheets/period_answers_L445.json.)\nModule updated: October 25, 2026 with Anthropic\'s Claude Opus 5.5 (L-443,\na spacecraft\'s identity on JPL\'s two Lookup answers for -31, fetched that\nday through the chat\'s web-fetch tool and kept in VOYAGER_1_LOOKUP.)\n"""\n\n'), ('              ("Pioneer 10", "-23"))\nFETCHED = ("Mercury", "Jupiter", "Encke")\n\n\n', '              ("Pioneer 10", "-23"))\nFETCHED = ("Mercury", "Jupiter", "Encke")\n\n# L-443, 2026-10-25: JPL\'s Lookup answers for Voyager 1 (-31), fetched\n# that day through the chat\'s web-fetch tool, word for word. The\n# small-body index answers a spacecraft\'s id with its header alone.\nVOYAGER_1 = ("Voyager 1", "-31", None, "Voyager 1 (spacecraft)",\n             "trajectory")\nVOYAGER_1_LOOKUP = {\n    hc.lookup_url("-31", "mb"): (\n        "API VERSION: 1.1\\n"\n        "API SOURCE: NASA/JPL Horizons Lookup API\\n\\n"\n        "Object name        = Voyager 1 (spacecraft)\\n"\n        "Type               = spacecraft\\n"\n        "Primary SPKID      = -31\\n"\n        "Primary designation= 1977-084A\\n"\n        "Aliases            = \\n"),\n    hc.lookup_url("-31", "sb"): (\n        "API VERSION: 1.1\\n"\n        "API SOURCE: NASA/JPL Horizons Lookup API\\n"),\n}\n\n\n'), ('            "a pinned comet whose record list cannot be fetched: %s"\n            % r["status"])\n\n    tmp = tempfile.mkdtemp(prefix="horizons_check_test_")\n', '            "a pinned comet whose record list cannot be fetched: %s"\n            % r["status"])\n    r = hc.check_entry("voyager_1", entry(VOYAGER_1),\n                       recorded_fetch({}, extra=VOYAGER_1_LOOKUP))\n    t.check(r["status"] == "agrees"\n            and r["jpl"].get("name") == "Voyager 1 (spacecraft)",\n            "a spacecraft agrees, the small-body index answering its id "\n            "with JPL\'s header alone: %s (JPL: %s)"\n            % (r["status"], r["jpl"].get("name") or r["error"]))\n    odd = dict(VOYAGER_1_LOOKUP)\n    odd[hc.lookup_url("-31", "sb")] += "ERROR: something JPL said\\n"\n    r = hc.check_entry("voyager_1", entry(VOYAGER_1),\n                       recorded_fetch({}, extra=odd))\n    t.check(r["status"] == "could not reach JPL",\n            "planted: JPL\'s header with any other line is not read as no "\n            "matches: %s" % r["status"])\n\n    tmp = tempfile.mkdtemp(prefix="horizons_check_test_")\n')]), ('LEDGER_CONSOLIDATED.md', [("two rules and L-484's into their skills; L-471 done), built on 0c27f47\nand gallery b1a4ce6.\nReview and RICE update Tony 6-21-2026\n\n", "two rules and L-484's into their skills; L-471 done), built on 0c27f47\nand gallery b1a4ce6.\nModule updated: October 25, 2026, evening, with Anthropic's Claude Opus\n5.5 (Tony's runs of build B on L-443: two fixes, the Horizons check and\nthe builder's span end; Voyager 1 goldenrod; L-487 new), built on\nd80aed3 and gallery 191d68f.\nReview and RICE update Tony 6-21-2026\n\n"), ('\n## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-486] A view carried into a room (gallery, the rooms)\n', '\n## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)\n\n#### [L-487] Each body\'s description in the i panel, one bullet per sentence (gallery, the i panel)\n<!-- L:487 status:OPEN upd:2026-10-25 section:A flag: rice: -->\n- **Tony, 2026-10-25, evening,** at his phone look of the spacecraft\n  (run record `documentation/WHERE_WE_ARE_10-24-26_1927_run_record.md`):\n  "i would suggest bulleting each sentence in the info panel object\n  descriptions, for all objects."\n**Gap:** a design talk: whether every body\'s description becomes one\nbullet per sentence, and whether the words are split where they are\nstored (the orrery\'s mission_info) or where the room shows them.\n**Ref:** gallery `interactive.html` (the i panel); orrery\n`celestial_objects.py` (mission_info); L-443.\n\n#### [L-486] A view carried into a room (gallery, the rooms)\n'), ("  - Skills: horizons-orbital-mechanics 1.11, gallery-cache-builder 1.12,\n    interactive-exhibit 1.24, safe-file-editing 1.14 (protocol v3.112).\n**Gap (replaces the one below, 2026-10-25):** Tony's runs (the handoff,\nsec. 2), the preview's report, the Daily Run and his phone look; then\nbuild B's second part, the comets, from the handoff's section 6: the\n", '  - Skills: horizons-orbital-mechanics 1.11, gallery-cache-builder 1.12,\n    interactive-exhibit 1.24, safe-file-editing 1.14 (protocol v3.112).\n- **Tony\'s runs, 2026-10-25, evening** (his run record,\n  `documentation/WHERE_WE_ARE_10-24-26_1927_run_record.md`). Patches 12\n  to 15 ran; orrery pushed at d80aed3, gallery at 191d68f. The preview\n  made by the orbiter rule: Juno 113 events to 4, Europa Clipper 87 to\n  5; patch 13 carried all twelve plans. Ten spacecraft built and drew;\n  his phone look: "juno looks correct. solid to today and dashed\n  predicted with both a hover text and info card"; Parker "correct".\n  Two failures, both fixed the same evening:\n  - **The Horizons check stopped at the first spacecraft as UNREACHABLE.**\n    JPL was reached. Its Lookup answers a spacecraft\'s id in the\n    small-body index with its two header lines alone (fetched that\n    evening for -31 and -61, group=sb), and the check read that as a\n    failed fetch. It now reads JPL\'s header alone as no matches (orrery\n    patch_L443_16, `horizons_check.py`, with a recorded Voyager 1 case\n    and a planted fault in its suite). The twelve names were checked\n    against JPL\'s Lookup the same evening; all twelve match.\n  - **Both Voyagers\' paths were refused by JPL** ("No ephemeris for\n    target ... after A.D. 2100-JAN-01 00:00:00.0000 TD"). Their data ends\n    at that minute exactly; the builder adds 69 s to every time it asks\n    (UTC to TDB), so the stop asked was 00:01. The span\'s end is now\n    taken back by the same 69 s (gallery patch_L443_17,\n    `gallery_cache_builder.py` `_plan_span`, with a check and a planted\n    fault in its suite). The other ten end later in their last day.\n    Voyager 1 was drawn from an old path with no marker, hover or panel\n    words; Voyager 2 was dropped.\n  - **Voyager 1 goldenrod**, not the orrery\'s white: "the white line\n    does not contrast with the white grid"; asked whether to share\n    Parker\'s gold, Tony chose "Gold, like Parker" (gallery\n    `presentation.py`, in patch_L443_17).\n  - His other notes: the TNO group opened with a lag; the failed fetches\n    are listed at the foot of the i panel, as intended; the description\n    bullets are L-487.\n**Gap (replaces the one below, 2026-10-25, evening):** Tony\'s runs of\npatch_L443_16 and the orrery maintenance run (the Horizons check\nconfirming the twelve), push; patch_L443_17 and the Daily Run (both\nVoyagers fetched), push; his look at Voyager 1. Then build B\'s second\npart, the comets, from the handoff\'s section 6, as below.\n**Gap (superseded above, 2026-10-25):** Tony\'s runs (the handoff,\nsec. 2), the preview\'s report, the Daily Run and his phone look; then\nbuild B\'s second part, the comets, from the handoff\'s section 6: the\n')]), ('documentation/WHERE_WE_ARE.md', [("# Where We Are\n\nLast updated: October 25, 2026: the spacecraft join the Solar System\nroom; the Daily Run stops when the pull and the push differ.\n- Written at orrery 0c27f47 and gallery b1a4ce6, with the close patch.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - The twelve spacecraft are built for the Solar System room, each\n>   path solid where flown, dashed where predicted; an orbiter keeps only\n>   its arrival and departure (L-443 (the objects)). Not yet run.\n> - The Daily Run stops when its pull is not your pushed orrery\n>   (L-461 (pull matches push)). Four skills bumped; protocol v3.112.\n>\n> **Do next:** *the comets, build B's second part, in a fresh session,\n", "# Where We Are\n\nLast updated: October 25, 2026, evening: ten spacecraft drew in the\nSolar System room; two fixes bring the Voyagers.\n- Written at orrery d80aed3 and gallery 191d68f, with the fix patches.\n\n> **READ THIS FIRST**\n>\n> **Changed since you last read this:**\n> - The spacecraft are in the Solar System room, each path solid where\n>   flown and dashed where predicted (L-443 (the objects)). Ten drew on\n>   your first run; the two Voyagers come with this evening's fix.\n> - The Horizons check now reads JPL's empty answer for a spacecraft,\n>   and the builder stops at JPL's last minute. Voyager 1 is gold.\n>\n> **Do next:** *the comets, build B's second part, in a fresh session,\n"), ('>\n> **Needs you now:**\n> - *(do) The run order in that handoff, section 2: three orrery\n>   patches, the maintenance run, push; the website patch, the Daily\n>   Run, push; then the phone look.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n', '>\n> **Needs you now:**\n> - *(do) patch_L443_16, the orrery maintenance run, push; then\n>   patch_L443_17, the Daily Run, push; then look at Voyager 1 again.*\n> - Two papers left to try (`READING_L456_tony_20261021.md`).\n\n'), ('- The orrery\'s own Sun axis hover: words to you first, and a source\n  for its "differential 24.5-35 d" (L-465 (the Sun\'s axis)).\n\nNot urgent, in your order:\n', '- The orrery\'s own Sun axis hover: words to you first, and a source\n  for its "differential 24.5-35 d" (L-465 (the Sun\'s axis)).\n- Each body\'s description in the i panel as one bullet per sentence,\n  for every object (L-487 (i panel bullets)).\n\nNot urgent, in your order:\n')]), ('documentation/HANDOFF_L443_slice2_buildB_spacecraft_20261025.md', [("\nRead this, the brief's sections 2.5 and 4, and the drawer-groups note.\n- Confirm the loaded skills read horizons-orbital-mechanics 1.11,\n  gallery-cache-builder 1.12, interactive-exhibit 1.24 and\n", "\nRead this, the brief's sections 2.5 and 4, and the drawer-groups note.\n- Added the same evening, after Tony's runs: two fixes followed (orrery\n  patch_L443_16, the Horizons check reading JPL's empty answer for a\n  spacecraft; gallery patch_L443_17, the builder stopping at JPL's last\n  minute, so the Voyagers are fetched; Voyager 1 goldenrod). Their\n  record is on L-443. Confirm from Tony's run record that both ran, the\n  Horizons check confirmed the twelve, and both Voyagers drew.\n- Confirm the loaded skills read horizons-orbital-mechanics 1.11,\n  gallery-cache-builder 1.12, interactive-exhibit 1.24 and\n")])]
NEW_FILES = []
SENTINELS = {'horizons_check.py': '    return bool(lines) and all(ln.startswith(("API VERSION:", "API SOURCE:"))', 'test_horizons_check.py': '            "planted: JPL\'s header with any other line is not read as no "', 'LEDGER_CONSOLIDATED.md': "#### [L-487] Each body's description in the i panel, one bullet per sentence (gallery, the i panel)", 'documentation/WHERE_WE_ARE.md': '>   flown and dashed where predicted (L-443 (the objects)). Ten drew on', 'documentation/HANDOFF_L443_slice2_buildB_spacecraft_20261025.md': "- Added the same evening, after Tony's runs: two fixes followed (orrery"}
POST_CALLS = []


def fail(msg):
    print(msg)
    print("NOTHING was written. Undo is not needed.")
    sys.exit(1)


def main():
    same_new = set()
    for rel, content in NEW_FILES:
        full = os.path.join(HERE, *rel.split("/"))
        if os.path.exists(full):
            have = open(full, "rb").read().replace(b"\r\n", b"\n")
            if have == content.encode("utf-8"):
                same_new.add(rel)
                continue
            fail("ERROR: %s already exists and differs from what this patch "
                 "writes. Most likely a copy of the same document saved from "
                 "a download or an attachment: delete it and run this patch "
                 "again." % rel)
    staged = []
    for rel, edits in EDITS:
        path = os.path.join(HERE, *rel.split("/"))
        if not os.path.isfile(path):
            fail("ERROR: not found: %s -- is this file in the right folder?"
                 % path)
        raw = open(path, "rb").read()
        crlf = b"\r\n" in raw
        text = raw.replace(b"\r\n", b"\n").decode("utf-8")
        if SENTINELS.get(rel) and SENTINELS[rel] in text:
            fail("ERROR: %s already carries this patch's change; this "
                 "patch has run." % rel)
        for k, (old, new) in enumerate(edits):
            n = text.count(old)
            if n != 1:
                if new and text.count(new) == 1 and old not in text:
                    fail("ERROR: %s already carries edit %d of %d; this "
                         "patch has run." % (rel, k + 1, len(edits)))
                fail("ANCHOR FAIL in %s, edit %d of %d: expected 1 match, "
                     "found %d" % (rel, k + 1, len(edits), n))
            text = text.replace(old, new)
        staged.append((rel, path, text, crlf, len(edits)))
    for rel, path, text, crlf, n in staged:
        open(path, "wb").write(text.encode("utf-8"))
        print("ok  %s (%d edits)" % (rel, n))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % rel)
        bad = sum(1 for c in text if ord(c) > 127)
        if bad:
            print("note: %s holds %d non-ASCII character(s) this patch did "
                  "not add" % (rel, bad))
    for rel, content in NEW_FILES:
        full = os.path.join(HERE, *rel.split("/"))
        if rel in same_new:
            print("ok  %s: already there, identical" % rel)
            continue
        d = os.path.dirname(full)
        if d and not os.path.isdir(d):
            os.makedirs(d)
        open(full, "wb").write(content.encode("utf-8"))
        print("ok  %s: new" % rel)
    for name in POST_CALLS:
        for line in globals()[name](HERE):
            print(line)
    print(DONE % (len(staged), len(NEW_FILES)))


if __name__ == "__main__":
    main()
