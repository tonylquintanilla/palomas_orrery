"""patch_L428_2_records_20261009.py -- records for L-428 (the lobby's way in).

Built on orrery b6652f9ad7bb96aea06be416d398f3234a91ca93 at
https://github.com/tonylquintanilla/palomas_orrery ("L414 L421"), with
gallery 5ec4739b6f160b7f4a455004b2bc5727e61a7815 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Written October 9, 2026 with Anthropic's Claude Opus 5.5.

HOW TO RUN
    Save this file in the orrery repo's ROOT folder (the folder that
    holds LEDGER_CONSOLIDATED.md). Open it in VS Code and press Run. Or,
    from a terminal in that folder:
        python patch_L428_2_records_20261009.py
    Then run orrery_maintenance_run.py (it rebuilds the ledger's index),
    move this script into documentation/, commit and push.

WHAT IT CHANGES
    LEDGER_CONSOLIDATED.md
      - a header stamp;
      - L-428 (the lobby's way in) opened, before L-427's block;
      - one dated line each on L-282 (the lobby), L-363 (the Solar
        System room and the front door), L-367 (no checker opens a
        room) and L-414 (the scanner's window: Tony's run, quoted from
        his copy). The upd: dates of L-282, L-363 and L-367 move to
        2026-10-09. Nothing is closed.
    documentation/WHERE_WE_ARE.md, by section, never below the
        run-record marker: the date line, the box, one Settled line,
        the Signals, one Where-the-details line.
    documentation/HANDOFF_lobby_option_E_20261009.md -- created.

SAFETY
    Each file is checked only at the lines this patch edits; Tony's
    notes elsewhere never stop it. Every anchor must match exactly once.
    If any check fails, NOTHING is written. Undo after a run is Discard
    Changes in GitHub Desktop (and delete the new handoff file).
    Success prints one "ok" line per edit and "patch applied".
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(ROOT, "LEDGER_CONSOLIDATED.md")
PAGE = os.path.join(ROOT, "documentation", "WHERE_WE_ARE.md")
HANDOFF = os.path.join(ROOT, "documentation", "HANDOFF_lobby_option_E_20261009.md")

HANDOFF_TEXT = '<!-- Doc-Kind: hand | Session record for L-428 (the lobby\'s way in): option E built as one gallery patch and one records patch, verified headless at phone and desktop width. Written October 9, 2026. -->\n# Handoff: the lobby\'s way in (option E), built\n\nBuilt on orrery b6652f9ad7bb96aea06be416d398f3234a91ca93 at\nhttps://github.com/tonylquintanilla/palomas_orrery ("L414 L421") and\ngallery 5ec4739b6f160b7f4a455004b2bc5727e61a7815 at\nhttps://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily\nrun 10-9-26"). Both pinned with `git ls-remote` at the session\'s start.\nPushed at: not yet. The next session reads both HEADs and writes them\non L-428.\n\n- Type: BUILD (gallery), with a records patch (orrery).\n- Supersedes: nothing. Companion: the brief,\n  `documentation/HANDOFF_lobby_option_E_brief_20261009.md` (Fable 5.1),\n  and section 11 of `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`\n  (the design; byte-identical to the copy Tony attached).\n- Skills loaded, each matching its manifest row: gallery-pipeline 1.2,\n  safe-file-editing 1.13, ledger-and-session-records 1.18. Protocol\n  v3.87 (the L-414 push had landed).\n- Ledger: L-428 (the lobby\'s way in) opened by this session. L-428 was\n  the next free handle at b6652f9.\n\n## Read this first\n\n- *The lobby now opens on the Solar System room\'s picture, its title,\n  one sentence and one Enter button. On a 390 x 844 phone the button\n  ends at 573 px, inside the first screen.*\n- *Nothing is pushed yet. Tony\'s steps are at the end.*\n- The words are the ones Tony confirmed on 2026-10-09 at 17:25. Nothing\n  new was asked.\n\n## 1. What was built\n\n`patch_L428_1_lobby_option_e.py`, run from the gallery root. Three\nfiles:\n\n- `index.html`\n  - A new function, `startCardHtml()`, draws the start block: the\n    card\'s picture (edge to edge below 768 px wide, a framed card above\n    it), the title, the card\'s `description`, and an Enter button with\n    an arrow. A tap on the picture or the button opens the card, through\n    the page\'s own `openCard()`, so the room\'s back link works as for\n    any other card.\n  - `renderLobby()` draws that block first, after the welcome line.\n    The heading "Doors" is now "Or explore by subject". The Solar\n    System card is skipped under Featured, so it is drawn once.\n  - The header comment gains an "Updated: October 9, 2026" entry.\n- `gallery/gallery_config.json`: a top-level `"sentence"`, "The solar\n  system, the Earth and the stars, to explore." The page has read this\n  key since L-282; the file had none, so the typed default showed.\n- `gallery/gallery_metadata.json`: card `solar_system`\'s\n  `description` becomes "Today\'s planets in 3D. Turn it with your\n  finger, tap a planet, step into the Sun and Earth." "Daily updates\n  from JPL Horizons" leaves it, as ruled; the room names its source.\n\nThe patch checks `index.html` against its content at 5ec4739, and the\ntwo JSON files only at the values it changes, so a later card edit in\nthe gallery editor does not block it. A second run says "already\napplied" and writes nothing.\n\n## 2. Two calls the build made, and why\n\n- **The title is typed, not served.** The brief left this to the build.\n  The card\'s served title, "The Solar System, live", also heads the card\n  on the Solar System door\'s page and in the menu, where "Start with\n  ..." would read wrong. So `index.html` holds\n  `LOBBY_START_TITLE = \'Start with the Solar System, live\'` beside\n  `LOBBY_START_ID = \'solar_system\'`, the card it is written for. If that\n  card is not served in a tab, the lobby opens on the subjects as\n  before, under "Explore by subject".\n- **The order inside the block follows the canvas Tony chose.** The\n  brief lists the heading above the picture. The artboard Tony picked\n  (E, "Lobby E: the picture is the way in", on his canvas "Lobby: the\n  Solar System way in") draws the picture first, then the title, the\n  sentence and the button, as one tappable block. The build follows the\n  artboard. Moving the title above the picture is one line if Tony\n  prefers it.\n\n## 3. Verification\n\nHeadless Chromium (Playwright), a throwaway copy of the gallery with the\npatch applied, served over a local web server; Plotly, Google Fonts and\nthe analytics script stubbed or blocked.\n\n- **Phone, 390 x 844:** start block 186 to 592 px; Enter button 521 to\n  573 px. Inside the first screen. The picture is the full 390 px wide\n  and loads (1200 x 600, the L-363 version B picture, kept at 2:1 so the\n  crop is the same).\n- **Desktop, 1280 x 800:** the block sits in the 560 px column as a\n  framed card; Enter ends at 617 px.\n- **Nothing drawn twice:** in the lobby, card `solar_system` appears\n  once, as the start block. Featured now holds the other four featured\n  cards, and no wide card is left there.\n- **Door counts unchanged:** phone 33 / 57 / 9, desktop 36 / 57 / 9,\n  the Solar System door with 4 interactive scenes; identical to the\n  unpatched page, and the desktop counts recomputed from\n  `gallery_metadata.json` agree.\n- **The door\'s page:** still opens with the wide card first, now with\n  the new sentence.\n- **Enter and the picture** both go to\n  `interactive.html?exhibit=solar-system`. No script errors.\n- **The gallery maintenance run** (offline pass): 28 PASS, 3 FAIL on the\n  patched copy, and the same 28 and 3, row for row, on the unpatched\n  base. The three FAIL rows are Pole of date, its ERFA checks and\n  Artifact 1 assembler; they fail the same way without the patch,\n  because this sandbox lacks the packages they need.\n- **No check covers the lobby.** The guest book row tests\n  `gallery/guestbook.js` only, and Page framing is for rooms. This is\n  already recorded as a class on L-367 (no checker opens a new room,\n  and nothing reads the lobby code), item 6 of L-423 (the website\'s\n  checks). The records patch adds a dated line there; nothing chased.\n\n## 4. Shown to Tony, not asked\n\n- "Turn it with your finger" is phone wording; the desktop turns it\n  with a mouse. The desktop screenshot shows it. A second sentence for\n  desktop would be a follow-up.\n- The button says "Enter". One word, as drawn.\n- On the phone the "Or explore by subject" heading now sits lower, over\n  the doves of the background wall. Worth a look on the real phone,\n  where the wall stays fixed as the page scrolls.\n\n## 5. The records patch\n\n`patch_L428_2_records_20261009.py`, run from the orrery root. It\nchecks each file only at the lines it edits.\n\n- `LEDGER_CONSOLIDATED.md`: a header stamp; L-428 (the lobby\'s way in)\n  opened; one line each on L-282 (the lobby), L-363 (the Solar System\n  room and the front door: its card moved), L-367 (no checker opens a\n  room: met again), and L-414 (the scanner\'s window: Tony\'s run, quoted\n  from his copy `documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`,\n  which ends "21 of 21 gating checkers passed"; `PROVENANCE_AUDIT.md`\n  at b6652f9 reads "GATE PATH: 0 TIER-1 -- the push gate holds."). L-414\n  is NOT closed here: its next session confirms provenance-discipline\n  2.28 loads, which needs that skill, and this session did not load it.\n- `documentation/WHERE_WE_ARE.md`, by section: the date line, the box\n  (changed, needs you now), one Settled line, the Signals, and one\n  Where-the-details line. Nothing below the run-record marker.\n- `documentation/HANDOFF_lobby_option_E_20261009.md`: this file.\n\nNot done, recorded: the page\'s run-record zone still holds the\npatch_L395_4 run of October 8. Tony\'s copy\n`WHERE_WE_ARE_10-8-26_1406_run_record.md` already holds it. The zone is\nTony\'s, so this patch left it alone.\n\n## 6. Tony\'s steps\n\n1. **(do)** Gallery: save `patch_L428_1_lobby_option_e.py` in the\n   gallery repo\'s root folder, open it in VS Code, press Run. Expect\n   eight "ok" lines and "patch applied".\n2. **(do)** Commit and push the gallery in GitHub Desktop. Move the\n   script into the gallery\'s `documentation/` folder (in the same or\n   the next commit).\n3. **(do)** Look on the phone: close the Home Screen clip\'s tab first,\n   so the phone fetches the new page. The lobby should open on the\n   picture and the Enter button; Enter opens the Solar System room.\n4. **(do)** Orrery: save `patch_L428_2_records_20261009.py` in the\n   orrery repo\'s root folder, press Run, then run\n   `orrery_maintenance_run.py`. Move the script into `documentation/`,\n   commit and push.\n5. **(decide, after the look)** Whether L-428 closes, or something\n   changes first.\n\n## 7. Not this session\n\n- The front-door address change (L-363: a bare interactive.html link\n  opens the Solar System room). Waits for L-423 (the website\'s checks).\n- `interactive.html`, the rooms, the drawer; the welcome count line,\n  Featured\'s order, the guest book.\n\n## Appendix: the headless lobby render\n\nClaude-only. Run from anywhere with Playwright installed:\n`python render.py <gallery_root> <out_prefix>`. It prints the facts\nquoted in section 3 and writes phone and desktop screenshots.\n\n```python\n"""Render the lobby of a gallery checkout headlessly and report facts.\nusage: python render.py <gallery_root> <out_prefix>"""\nimport sys, json, threading, http.server, functools, socketserver\nfrom playwright.sync_api import sync_playwright\nroot, out = sys.argv[1], sys.argv[2]\nclass Q(http.server.SimpleHTTPRequestHandler):\n    def log_message(self, *a): pass\nsrv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(Q, directory=root))\nport = srv.server_address[1]\nthreading.Thread(target=srv.serve_forever, daemon=True).start()\nbase = "http://127.0.0.1:%d/" % port\nSTUB = ("window.Plotly={newPlot:function(){return Promise.resolve()},"\n        "purge:function(){},relayout:function(){return Promise.resolve()}};")\nreport = {}\nwith sync_playwright() as p:\n    b = p.chromium.launch()\n    for name, vp, mobile in [("phone", (390, 844), True), ("desktop", (1280, 800), False)]:\n        ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]}, is_mobile=mobile,\n                            has_touch=mobile, device_scale_factor=2 if mobile else 1)\n        pg = ctx.new_page()\n        errs = []\n        pg.on("pageerror", lambda e: errs.append(str(e)))\n        pg.route("**/cdn.plot.ly/**", lambda r: r.fulfill(body=STUB, content_type="text/javascript"))\n        pg.route("**/fonts.g*/**", lambda r: r.abort())\n        pg.route("**/*googletagmanager*/**", lambda r: r.abort())\n        pg.goto(base + "index.html", wait_until="networkidle")\n        pg.wait_for_timeout(800)\n        facts = pg.evaluate("""() => {\n          const q = s => Array.from(document.querySelectorAll(s));\n          const r = el => { if (!el) return null; const b = el.getBoundingClientRect();\n                            return {top: Math.round(b.top), bottom: Math.round(b.bottom)}; };\n          return {\n            headings: q(\'.lobby-heading\').map(e => e.textContent),\n            welcome: (document.querySelector(\'.lobby .welcome-text\')||{}).textContent,\n            start: r(document.querySelector(\'.lobby-start\')),\n            enter: r(document.querySelector(\'.lobby-start-enter\')),\n            pictureLoaded: (document.querySelector(\'.lobby-start-picture\')||{}).naturalWidth || 0,\n            lobbyCards: q(\'#welcomeState [data-viz-id]\').map(e => e.getAttribute(\'data-viz-id\')),\n            doors: q(\'.lobby-door\').map(e => [e.getAttribute(\'data-door\'),\n                                              e.querySelector(\'.lobby-door-meta\').textContent]),\n          };\n        }""")\n        facts["pageErrors"] = errs\n        pg.screenshot(path="%s_%s.png" % (out, name))\n        pg.click(".lobby-door[data-door=\'solar_system\']")\n        pg.wait_for_timeout(400)\n        facts["doorPageFirstCard"] = pg.evaluate(\n            "(() => { const c = document.querySelector(\'.room-card, .lobby-wide\');"\n            " return c ? [c.getAttribute(\'data-viz-id\'),"\n            " (c.querySelector(\'.lobby-wide-desc\')||{}).textContent] : null; })()")\n        pg.goto(base + "index.html", wait_until="networkidle")\n        if pg.query_selector(".lobby-start-enter"):\n            with pg.expect_navigation(timeout=5000):\n                pg.click(".lobby-start-enter")\n            facts["enterGoesTo"] = pg.url.replace(base, "")\n        report[name] = facts\n        ctx.close()\n    b.close()\nprint(json.dumps(report, indent=1))\n```\n\nSession record written October 2026 with Anthropic\'s Claude Opus 5.5.\n'

# ------------------------------------------------------------ the ledger

L_STAMP = (
b"""
Review and RICE update Tony 6-21-2026
""",
b"""
Module updated: October 9, 2026 with Anthropic's Claude Opus 5.5
(L-428 opened and built: the lobby's way in, option E; L-282, L-363,
L-367 and L-414 updated), built on b6652f9.
Review and RICE update Tony 6-21-2026
""")

L_NEW = (
b"""#### [L-427] Rows a neighbour's citation had been crediting (store)
""",
b"""#### [L-428] The lobby's way in: the Solar System room first (gallery, lobby)
<!-- L:428 status:OPEN upd:2026-10-09 section:A flag: rice: -->
- **Asked 2026-10-09, 17:10,** by Tony with a phone screenshot of the
  live lobby: a friend shown the site "was confused on where to go. He
  started with the rooms and cards but still unsure. Can you use design
  to make the solar system interactive as the clear starting point?"
  On the phone the three doors filled the first screen and the Solar
  System card started below it, under Featured.
- **Designed the same day** (section 11 of
  `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`). Tony picked
  option E, "the picture is the way in" (17:23), and confirmed both new
  sentences, "Use the new wording" (17:25). The canvas is "Lobby: the
  Solar System way in", artboard E.
- **Built 2026-10-09, NOT yet run or pushed** [render-gated]: gallery
  `patch_L428_1_lobby_option_e.py`, on gallery 5ec4739. The lobby opens
  on the room's picture (edge to edge on a phone), the title "Start
  with the Solar System, live", the card's sentence and one Enter
  button; then "Or explore by subject" (was "Doors") with the three
  doors unchanged; then Featured, without the Solar System card, and
  the guest book. The welcome line is served from
  `gallery/gallery_config.json` (`sentence`), the card's sentence from
  `gallery/gallery_metadata.json` (card `solar_system`).
- Two calls the build made: the title is typed in `index.html`, beside
  the id of the card it is written for, because the card's served title
  also heads its door's page and the menu; and the block's order follows
  the artboard Tony chose (picture, then title), not the brief's list
  (title, then picture).
- Verified headless at 390 x 844 and 1280 x 800 on a throwaway copy:
  the Enter button ends at 573 px on the phone; the card is drawn once;
  the door counts are unchanged; the door's page still opens on the
  card; Enter and the picture open the room. Record:
  `documentation/HANDOFF_lobby_option_E_20261009.md`.
- Tony-action (do): run the gallery patch, push, look on the phone with
  the Home Screen clip's tab closed first; run this records patch, the
  maintenance run, push.
- Tony-action (decide), after the look: close, or change first.
**Gap:** Tony's run and his look on the phone. Then this item closes.
**Ref:** L-282 (the lobby); L-363 (the Solar System room and the front
door); L-367 (no checker opens a room); L-423 (the website's checks);
gallery `index.html`, `gallery/gallery_config.json`,
`gallery/gallery_metadata.json`.

#### [L-427] Rows a neighbour's citation had been crediting (store)
""")

L_414 = (
b"""**Gap:** Tony's run. The maintenance run should end on "GATE PATH: 0
""",
b"""- **Tony's run, read 2026-10-09 by the lobby session (L-428)** from his
  copy `documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`: the
  maintenance run ended "21 of 21 gating checkers passed -- 112.0s
  total", its scanner row reading "0 TIER-1 -- the push gate holds";
  pushed in b6652f9. `PROVENANCE_AUDIT.md` at b6652f9 reads "GATE PATH:
  0 TIER-1 -- the push gate holds." Not closed by that session: it did
  not load provenance-discipline, and the next provenance session
  confirms its loaded copy reads 2.28.
**Gap:** Tony's run. The maintenance run should end on "GATE PATH: 0
""")

L_367_META = (
b"""<!-- L:367 status:OPEN upd:2026-10-08 section:A flag: rice: -->""",
b"""<!-- L:367 status:OPEN upd:2026-10-09 section:A flag: rice: -->""")

L_367 = (
b"""**Gap:** A check that lists `EXHIBITS` and fails on a room no checker boots""",
b"""- **2026-10-09, met again at L-428 (the lobby's way in):** the gallery
  maintenance run gave the same verdicts, row for row, on the patched
  copy and on the base, and no row draws the lobby. Its checks were a
  headless render at 390 x 844 and 1280 x 800; the script is in
  `documentation/HANDOFF_lobby_option_E_20261009.md`.
**Gap:** A check that lists `EXHIBITS` and fails on a room no checker boots""")

L_363_META = (
b"""<!-- L:363 status:OPEN upd:2026-10-04 section:A flag: rice: -->""",
b"""<!-- L:363 status:OPEN upd:2026-10-09 section:A flag: rice: -->""")

L_363 = (
b"""- **2026-10-04, the lobby's wide card: built and on the website.**
""",
b"""- **2026-10-09, the card moves, under L-428 (the lobby's way in):** the
  lobby no longer draws it under Featured; it opens the lobby, as the
  start block. Its sentence is now "Today's planets in 3D. Turn it with
  your finger, tap a planet, step into the Sun and Earth." The door's
  page still shows it first, unchanged. Not the address swap below.
- **2026-10-04, the lobby's wide card: built and on the website.**
""")

L_282_META = (
b"""<!-- L:282 status:OPEN upd:2026-09-06 section:A flag: rice:5/4/75/4 -->""",
b"""<!-- L:282 status:OPEN upd:2026-10-09 section:A flag: rice:5/4/75/4 -->""")

L_282 = (
b"""**Ref:** L-286 (rooms, drill-down, breadcrumb), L-287 (editor and room
""",
b"""- **2026-10-09: the lobby's way in, L-428.** A friend shown the site on
  a phone did not know where to start. The lobby now opens on the Solar
  System room's picture and one Enter button, then the doors under "Or
  explore by subject". Its own item, L-428.
**Ref:** L-286 (rooms, drill-down, breadcrumb), L-287 (editor and room
""")

LEDGER_EDITS = [
    ("LEDGER_CONSOLIDATED.md  L-282 line", L_282),
    ("LEDGER_CONSOLIDATED.md  L-282 date", L_282_META),
    ("LEDGER_CONSOLIDATED.md  L-363 line", L_363),
    ("LEDGER_CONSOLIDATED.md  L-363 date", L_363_META),
    ("LEDGER_CONSOLIDATED.md  L-367 line", L_367),
    ("LEDGER_CONSOLIDATED.md  L-367 date", L_367_META),
    ("LEDGER_CONSOLIDATED.md  L-414 Tony's run", L_414),
    ("LEDGER_CONSOLIDATED.md  L-428 opened", L_NEW),
    ("LEDGER_CONSOLIDATED.md  header stamp", L_STAMP),
]

# --------------------------------------------------------- Where We Are

P_SIGNALS = (
b"""- Last cache build: 20261008T180043Z, ok. Its last rename took two
  attempts, and the retry absorbed it.
- Tier-1 on the gate path: 0 on a copy with patch_L414_1 applied;
  your run prints it as GATE PATH. Whole tree: 293 there, 296 in
  PROVENANCE_AUDIT.md at aa46bb1.
- This page's date and the ledger's newest stamp: both Oct 9. Agree.
""",
b"""- Last cache build: 20261009T190335Z, ok, no retry.
- Tier-1 on the gate path: 0, by name, in PROVENANCE_AUDIT.md at
  b6652f9. Whole tree: 293.
- This page's date and the ledger's newest stamp: both Oct 9. Agree.
""")

P_DETAILS = (
b"""## Where the details are  **>> UPDATED THIS SESSION**

""",
b"""## Where the details are  **>> UPDATED THIS SESSION**

- The lobby: L-428 (its way in); `HANDOFF_lobby_option_E_20261009.md`
""")

P_SETTLED = (
b"""Standing rulings. A line leaves after a few weeks, once it is habit.
""",
b"""Standing rulings. A line leaves after a few weeks, once it is habit.
- The lobby opens on the Solar System room, then the subjects. (Oct 9)
""")

P_NEEDS = (
b"""> - *Run patch_L414_1, then orrery_maintenance_run.py, and push. Then
>   reinstall provenance-discipline from its ZIP.*
""",
b"""> - *Gallery: run patch_L428_1, push, look on the phone (close the
>   Home Screen clip's tab first). Orrery: run patch_L428_2, then the
>   maintenance run, and push.*
> - Reinstall provenance-discipline 2.28, if not done yet.
""")

P_CHANGED = (
b"""> - L-414 (the scanner's window) is built: a row's sources are read
>   only from its own comment block; declared rows are named.
> - The scanner prints the push gate's number, naming each finding:
>   0 on a copy; it was 4, all the scanner's own faults.
> - L-427 (rows a neighbour had been crediting): one row lost a
>   borrowed citation; it is off the gate path.
""",
b"""> - L-428 (the lobby's way in) is built: the lobby opens on the Solar
>   System room's picture and one Enter button. Not pushed yet.
> - "Doors" is now "Or explore by subject". The Solar System card left
>   Featured, since it now opens the page.
""")

P_HEADER = (
b"""Last updated: October 9, 2026, at the scanner window build.
- Written at orrery aa46bb1 and gallery 5ec4739b, before your run of
  patch_L414_1.
""",
b"""Last updated: October 9, 2026, at the lobby build.
- Written at orrery b6652f9 and gallery 5ec4739, before your runs.
""")

PAGE_EDITS = [
    ("WHERE_WE_ARE.md         where the details are", P_DETAILS),
    ("WHERE_WE_ARE.md         signals", P_SIGNALS),
    ("WHERE_WE_ARE.md         settled", P_SETTLED),
    ("WHERE_WE_ARE.md         needs you now", P_NEEDS),
    ("WHERE_WE_ARE.md         changed since", P_CHANGED),
    ("WHERE_WE_ARE.md         date line", P_HEADER),
]

MARKER = b"--- Your run record below this line"


def fail(msg):
    print("FAILURE: " + msg)
    print("NOTHING was written. Undo is not needed.")
    sys.exit(1)


def read_lf(path):
    if not os.path.isfile(path):
        fail("%s not found. Save this script in the orrery repo root." % path)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n"), (b"\r\n" in raw)


def apply(text, edits):
    for name, (old, new) in edits:
        n = text.count(old)
        if n != 1:
            fail("ANCHOR FAIL, %s: expected 1 match, found %d. Has that "
                 "section changed since b6652f9?" % (name, n))
        text = text.replace(old, new)
        print("ok  " + name)
    return text


def main():
    ledger, ledger_crlf = read_lf(LEDGER)
    page, page_crlf = read_lf(PAGE)

    if b"#### [L-428]" in ledger:
        print("already applied: the ledger already holds L-428. Nothing written.")
        return
    if os.path.exists(HANDOFF):
        fail("documentation/HANDOFF_lobby_option_E_20261009.md already exists.")

    # The marker must be there before and after, and the zone below it
    # must come through untouched.
    if page.count(MARKER) != 1:
        fail("WHERE_WE_ARE.md: the run-record marker line was not found once.")
    below_before = page[page.index(MARKER):]

    ledger_out = apply(ledger, LEDGER_EDITS)
    page_out = apply(page, PAGE_EDITS)
    if page_out[page_out.index(MARKER):] != below_before:
        fail("WHERE_WE_ARE.md: an edit reached below the run-record marker.")

    handoff = HANDOFF_TEXT.encode("ascii")
    for name, data in (("LEDGER_CONSOLIDATED.md", ledger_out),
                       ("WHERE_WE_ARE.md", page_out), ("the handoff", handoff)):
        bad = sum(1 for b in data if b > 127)
        if bad:
            fail("%s would hold %d non-ASCII byte(s)." % (name, bad))

    open(LEDGER, "wb").write(ledger_out)
    open(PAGE, "wb").write(page_out)
    open(HANDOFF, "wb").write(handoff)
    print("ok  documentation/HANDOFF_lobby_option_E_20261009.md created")
    for name, was in (("LEDGER_CONSOLIDATED.md", ledger_crlf),
                      ("WHERE_WE_ARE.md", page_crlf)):
        if was:
            print("note: %s was CRLF in the working copy; written LF" % name)
    above = page_out[:page_out.index(MARKER)].count(b"\n")
    print("note: WHERE_WE_ARE.md has %d lines above the run-record marker "
          "(the cap is 130)" % above)
    print("stamps updated: LEDGER_CONSOLIDATED.md header; WHERE_WE_ARE.md date line")
    print("patch applied")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py -- it rebuilds the ledger's index.")
    print("  2. Move this script into documentation/; commit and push.")


if __name__ == "__main__":
    main()
