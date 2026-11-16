"""
patch_L060_1_el_nino_page_20261116.py -- records for the El Nino talk of
Nov 16 (the coordinating session, Claude Opus 5.5). Records only; no code.

Built on orrery e84baabd79993ff6a030092f03a5a42d8b95443f at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 1c5fe516cebaa7b239d34c7573f66a0f6099cc90 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, read live
on Nov 16, 2026, 12:30 Chicago, and checked against your local copies
of the ledger and Where We Are, which hold the document track's
unpushed edits of 08:35 (Claude Fable 5.2). Written under ledger-and-session-records
1.23, earth-system-pipeline 1.3 (the session's loaded copy read 1.3, as
v3.141 asked a session to confirm) and safe-file-editing 1.14.

Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
and gallery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\

WHAT IT CHANGES (two files)

    LEDGER_CONSOLIDATED.md
      - L-060 (El Nino): a dated note with your four rulings of Nov 16
        (a page like Sudan's; interrupt now, ahead of ESCAPADE; NOAA's
        own forecast chances; NOAA's Climate Prediction Center the one
        source of record), what still holds of the June design and
        what must be rewritten, and a new Gap. The old Gap is marked
        superseded. Its date stamp moves to 2026-11-16.
      Then it runs ledger_index.py, which rebuilds the index rows.

    documentation/WHERE_WE_ARE.md, by section: the header, the box
    (changed, do next, and the commit line, which keeps the document
    track's handoff in it), the road's stage 15, one Settled
    line added and one removed (the hold, which gallery-cache-builder
    1.19 now carries), one line under Where the details are, and the
    old marks cleared. Nothing below the run-record marker.

    Each edit is checked only at the text it replaces, so your notes
    elsewhere never stop it. A file that already holds the result is
    accepted and reported.

RUN COMMAND

    Save this file in the orrery's root folder
    (palomas_orrery_for_github), open it in VS Code and click Run.
    (python patch_L060_1_el_nino_page_20261116.py)

    Success: one "ok" line per edit, the index tool's last lines, then
    "patch applied". Failure: one ERROR or ANCHOR FAIL line, and
    nothing is written. Undo is Discard Changes in GitHub Desktop.

Written November 16, 2026 with Anthropic's Claude Opus 5.5.
"""

import os
import subprocess
import sys

LEDGER = "LEDGER_CONSOLIDATED.md"
PAGE = os.path.join("documentation", "WHERE_WE_ARE.md")
MARKER = b"--- Your run record below this line"


def b(s):
    return s.encode("ascii")


L060_NOTE = """\
- **2026-11-16: EL NINO COMES BACK, AS A PAGE** (the coordinating
  session of Nov 16, Claude Opus 5.5, from Tony's phone). Prompted by a
  magazine article Tony shared, dated Nov 16, 2026, on this El Nino and
  the Amazon's fires. Four rulings, in Tony's words:
  - 09:06, "Yes": El Nino is its own page on the website, like Sudan's
    (earth/[id].html, earth-system-pipeline 1.3, A Layer's Page and Its
    Walk), with the June chart at its centre; a walk is added only if
    it earns one. Not the old-gallery card the June spec planned: the
    old lobby's Earth System cards are being retired (L-531 (the Earth
    Science room)).
  - 09:11, "Yes, interrupt.": ahead of ESCAPADE's path (L-533), as
    Tony's words of Nov 13 on L-531 allowed ("We may interrupt again
    for something else like el nino.").
  - 09:15, "Switch.": the forecast is NOAA's own, the Climate
    Prediction Center's chances season by season, on RONI, the same
    index as the chart's main line. It replaces the June plan of the
    IRI model plume, a band on the ONI basis (the spec's D6 and section
    2.3). Two reasons: NOAA forecasts on RONI since Feb 1, 2026; and a
    session of Oct 19 found the IRI plume's numbers published only as a
    picture, to be typed in by hand each month.
  - 12:24, "yes, please proceed.": NOAA's Climate Prediction Center
    (CPC) is the one source of record, as IPC is for food insecurity:
    the history (RONI.ascii.txt), the status (the ENSO Alert System)
    and the forecast's chances, from one body. No internationally
    agreed El Nino threshold exists (CPC +0.5, Australia's Bureau of
    Meteorology +0.8, on its own relative index), so WMO's quarterly
    update and the Bureau's figures are left out, not mixed in.
  - Tony's question at 09:58, NOAA's funding and its labs, and what
    was answered: CPC is part of the operational Weather Service
    (CLIMATE PREDICTION CENTER/NCEP/NWS on its discussions), not the
    research office (OAR) the FY2026 and FY2027 requests proposed to
    eliminate; Congress kept OAR for FY2026, and the House committee
    rejected the FY2027 request. Two safeguards, method for the build:
    the page shows the date of NOAA's latest update and says so when
    one is overdue; every build saves a copy of the NOAA files it read.
    If CPC stopped, a new source of record is Tony's decision then,
    never a fallback that switches in by itself.
  - Still holds from the June spec (documentation/ENSO_chart_spec.md
    v2): RONI as the lead series, a filled seesaw, red above and blue
    below; ONI as a thin line; phases and strength computed from RONI
    (D4), never a recalled label; the 2026 event provisional; the
    charge-and-discharge drawing for the mechanism. A record is shown
    as possible until the data shows one.
  - Must be rewritten for the build: the spec's build parts (sections
    3 and 6: the Plotly teaser, gallery_metadata.json, the old viewer's
    i card) to the page rules; and its card notes' figures from memory
    (the years of the deepest imbalance minima) sourced or removed.
  - Read this session [verified, fetched Nov 16]: RONI.ascii.txt live,
    its last season JAS 2026 at +1.69, the file's highest DJF 1983 at
    +2.40; CPC's discussion issued 12 November 2026, the next
    scheduled 10 December 2026.
  - Not in this item, recorded only: the Amazon's fires as a later
    step, if at all. The article names three pressures (El Nino,
    deforestation, repeated fire), so a page could show El Nino as the
    background, never the cause; its figures would come from INPE and
    MapBiomas, not the magazine. The Phase 2 pass on
    energy_imbalance.py stands as deferred; its chart is an old-gallery
    card, so its form waits on L-531.
**Gap (replaces the one above, 2026-11-16):** the brief for El Nino's
Code session (the page by the earth-system-pipeline rules; the June
chart with NOAA's chances as its forecast; CPC the one source; the two
safeguards; the spec's build parts rewritten); then the build, Tony's
phone look, and his reading of every word before it goes live. Then
ESCAPADE's path (L-533).
"""

LEDGER_EDITS = [
    ("L-060: the old Gap marked superseded",
     b("**Gap:** build next session. One genuine open call left (build, "
       "not design)"),
     b("**Gap (superseded below, 2026-11-16):** build next session. One "
       "genuine open call left (build, not design)")),
    ("L-060: the Nov 16 note and new Gap",
     b("**Ref:** ENSO_chart_spec.md v2 (design spec, this session); "
       "cross-ref L-001"),
     b(L060_NOTE) + b("**Ref:** ENSO_chart_spec.md v2 (design spec, this "
                      "session); cross-ref L-001")),
    ("L-060: date stamp",
     b("<!-- L:060 status:OPEN upd:2026-10-07 section:A flag: "
       "rice:3/3/75/2.5 -->"),
     b("<!-- L:060 status:OPEN upd:2026-11-16 section:A flag: "
       "rice:3/3/75/2.5 -->")),
]

PAGE_EDITS = [
    ("the page's header",
     b("Last updated: November 16, 2026, 01:10: the coordinating "
       "session's close (Opus), its handoff to the ESCAPADE coordinator; "
       "then, 08:35, the document track's close (Fable), its handoff.\n"
       "- Written at orrery 273f4ac9 and gallery 1c5fe516, your pushes of "
       "the drawer and the records, with the handoff not yet pushed.\n"),
     b("Last updated: November 16, 2026, 12:30: the El Nino talk (Opus), "
       "an interruption before ESCAPADE; earlier today the coordinating "
       "session's close (Opus, 01:10) and the document track's (Fable, "
       "08:35).\n"
       "- Written at orrery e84baabd and gallery 1c5fe516, read live, "
       "over your local copy holding the document track's edits, not yet "
       "pushed.\n")),
    ("the box: changed since you last read this",
     b("> - The drawer opens at the row its handle names, scrolled to the "
       "top and highlighted: Earth at the opening, a tapped body, the Sun "
       "after a tap on the Sun, a centred body with its list below it. The "
       "first guide's cards are unchanged (walked in Chrome, 177 of 177).\n"
       "> - L-535 (the period's reason) is closed on your look; Mars was "
       "closed before it. The opening keeps Earth's row, your \"Keep "
       "Earth\".\n"),
     b("> - El Nino interrupts, ahead of ESCAPADE: its own page on the "
       "website, like Sudan's, with the June chart at its centre (L-060 "
       "(El Nino)).\n"
       "> - Its one source is NOAA's Climate Prediction Center, the way IPC "
       "is Sudan's. The forecast is NOAA's own chances, season by season, "
       "and the page shows the date of NOAA's latest update.\n")),
    ("the box: do next",
     b("> **Do next:** *ESCAPADE's path (L-533 (ESCAPADE)), its brief when "
       "it is next.*\n"),
     b("> **Do next:** *El Nino's brief (L-060 (El Nino)), then its Code "
       "session. ESCAPADE's path (L-533 (ESCAPADE)) waits behind it.*\n")),
    ("the box: needs you now",
     b("> - *(do) Commit and push the orrery: the document track's "
       "handoff, `documentation/HANDOFF_document_upkeep_20261116.md`, the "
       "ledger and this page.*\n"),
     b("> - *(do) Commit and push the orrery: the document track's "
       "handoff, `documentation/HANDOFF_document_upkeep_20261116.md`, the "
       "ledger (now with El Nino's entry), this page, and "
       "`documentation/patch_L060_1_el_nino_page_20261116.py`.*\n")),
    ("the road: stage 15",
     b(" 15.   [NOW]   *Mars (L-514 (the Mars room)): closed Nov 15 on your\n"
       "               looks. Next ESCAPADE's path (L-533), the\n"
       "               Lagrange points (L-297), the destinations and "
       "encounters\n"
       "               talk (L-534, L-529), then Uranus and Neptune. Io, "
       "Titan,\n"
       "               Charon and Pluto come to standard in their folds.*\n"),
     b(" 15.   [NOW]   *Mars (L-514 (the Mars room)) closed Nov 15. Now El "
       "Nino's\n"
       "               page, an interruption (L-060 (El Nino)), then "
       "ESCAPADE's\n"
       "               path (L-533), the Lagrange points (L-297), the "
       "destinations\n"
       "               and encounters talk (L-534, L-529), then Uranus and "
       "Neptune.\n"
       "               Io, Titan, Charon and Pluto come to standard in their "
       "folds.* << moved this session\n")),
    ("Settled: El Nino's rulings",
     b("Standing rulings; a line leaves once it is habit, or a skill "
       "carries it.\n"),
     b("Standing rulings; a line leaves once it is habit, or a skill "
       "carries it.\n"
       "- El Nino is a page like Sudan's, its chart the June design; one "
       "source of record, NOAA's Climate Prediction Center, its forecast "
       "NOAA's own chances on RONI; WMO and Australia's index left out "
       "(Nov 16; L-060 (El Nino)).\n")),
    ("Settled: the hold's line, now carried by gallery-cache-builder 1.19",
     b("- One body's failed accuracy test: \"Hold the bad data and report, "
       "then continue.\""),
     None),
    ("Signals: last session's mark cleared",
     b("## Signals  **>> UPDATED THIS SESSION**\n"),
     b("## Signals\n")),
    ("Waiting on you: last session's mark cleared",
     b("## Waiting on you  **>> UPDATED THIS SESSION**\n"),
     b("## Waiting on you\n")),
    ("Where the details are: El Nino's line",
     b("- Every item: `LEDGER_CONSOLIDATED.md`.\n"),
     b("- Every item: `LEDGER_CONSOLIDATED.md`.\n"
       "- El Nino: L-060 (El Nino); the June design "
       "`documentation/ENSO_chart_spec.md`, its build parts to be "
       "rewritten for a page.\n")),
]


def whole_line(top, start_text):
    """The full line of top that starts with start_text, with its newline."""
    i = top.find(b"\n" + start_text)
    if i < 0 or top.find(b"\n" + start_text, i + 1) >= 0:
        return None
    j = top.find(b"\n", i + 1)
    return top[i + 1:j + 1]


def plan(path, edits, top_only=False):
    if not os.path.exists(path):
        print("ERROR: %s not found. Run this from the orrery's root folder "
              "(palomas_orrery_for_github). Nothing was written." % path)
        return False, None
    raw = open(path, "rb").read()
    text = raw.replace(b"\r\n", b"\n")
    if top_only:
        if text.count(MARKER) != 1:
            print("ERROR: the run-record marker is not on %s once. Nothing "
                  "was written." % path)
            return False, None
        top, marker, bottom = text.partition(MARKER)
    else:
        top, marker, bottom = text, b"", b""

    def done(old, new):
        if new is None:
            return whole_line(top, old) is None and top.count(old) == 0
        return top.count(new) == 1

    if all(done(old, new) for _, old, new in edits):
        print("already there, identical: %s" % path)
        return True, None
    for label, old, new in edits:
        if new is None:
            line = whole_line(top, old)
            if line is None:
                print("ANCHOR FAIL: %s in %s -- expected its line once. "
                      "Nothing was written." % (label, path))
                return False, None
            top = top.replace(line, b"")
            print("ok %s" % label)
            continue
        n = top.count(old)
        if n != 1:
            print("ANCHOR FAIL: %s in %s -- expected its text once, found "
                  "%d. Nothing was written." % (label, path, n))
            return False, None
        top = top.replace(old, new)
        print("ok %s" % label)
    out = top + marker + bottom
    added = b"".join(new for _, _, new in edits if new)
    if any(c > 127 for c in added):
        print("ERROR: this patch's own text would add non-ASCII bytes to "
              "%s. Nothing was written." % path)
        return False, None
    if top_only and top.count(b"\n") > 130:
        print("ERROR: %s would stand over 130 lines above its marker (%d). "
              "Nothing was written." % (path, top.count(b"\n")))
        return False, None
    if b"\r\n" in raw:
        print("note: %s was CRLF in the working copy; written LF" % path)
    return True, out


def main():
    if os.path.basename(os.getcwd()).lower() == "documentation":
        print("ERROR: run this from the orrery's root folder, not from "
              "documentation\\. Nothing was written.")
        return 1
    ok1, led = plan(LEDGER, LEDGER_EDITS)
    if not ok1:
        return 1
    ok2, page = plan(PAGE, PAGE_EDITS, top_only=True)
    if not ok2:
        return 1
    wrote = False
    for path, out, n in ((LEDGER, led, len(LEDGER_EDITS)),
                         (PAGE, page, len(PAGE_EDITS))):
        if out is None:
            continue
        with open(path, "wb") as f:
            f.write(out)
        wrote = True
        print("ok %s (%d edits)" % (path, n))
    if led is not None:
        print("Running ledger_index.py ...")
        r = subprocess.run([sys.executable, "ledger_index.py"],
                           capture_output=True, text=True)
        for line in (r.stdout + r.stderr).strip().splitlines()[-6:]:
            print("  " + line)
        if r.returncode != 0:
            print("ERROR: ledger_index.py exited %d. The edits above are "
                  "written; Discard Changes in GitHub Desktop undoes them. "
                  "Paste these lines to the session." % r.returncode)
            return 1
        print("ok ledger_index.py")
    print("patch applied" if wrote else "Nothing to do.")
    print("")
    print("Do next:")
    print("  1. (do) Move this file into documentation\\.")
    print("  2. (do) In GitHub Desktop (orrery): the change list shows the "
          "ledger, WHERE_WE_ARE.md, this file and, if not yet pushed, the "
          "document track's handoff of 08:35. Commit and push -- not "
          "while the website's night is running (08:17 UTC, 2:17 "
          "Chicago, often hours late).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
