<!-- Doc-Kind: hand | Session record for L-428 (the lobby's way in): option E built as one gallery patch and one records patch, verified headless at phone and desktop width. Written October 9, 2026. -->
# Handoff: the lobby's way in (option E), built

Built on orrery b6652f9ad7bb96aea06be416d398f3234a91ca93 at
https://github.com/tonylquintanilla/palomas_orrery ("L414 L421") and
gallery 5ec4739b6f160b7f4a455004b2bc5727e61a7815 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run 10-9-26"). Both pinned with `git ls-remote` at the session's start.
Pushed at: not yet. The next session reads both HEADs and writes them
on L-428.

- Type: BUILD (gallery), with a records patch (orrery).
- Supersedes: nothing. Companion: the brief,
  `documentation/HANDOFF_lobby_option_E_brief_20261009.md` (Fable 5.1),
  and section 11 of `documentation/DESIGN_L421_inner_oort_tilt_20261009.md`
  (the design; byte-identical to the copy Tony attached).
- Skills loaded, each matching its manifest row: gallery-pipeline 1.2,
  safe-file-editing 1.13, ledger-and-session-records 1.18. Protocol
  v3.87 (the L-414 push had landed).
- Ledger: L-428 (the lobby's way in) opened by this session. L-428 was
  the next free handle at b6652f9.

## Read this first

- *The lobby now opens on the Solar System room's picture, its title,
  one sentence and one Enter button. On a 390 x 844 phone the button
  ends at 573 px, inside the first screen.*
- *Nothing is pushed yet. Tony's steps are at the end.*
- The words are the ones Tony confirmed on 2026-10-09 at 17:25. Nothing
  new was asked.

## 1. What was built

`patch_L428_1_lobby_option_e.py`, run from the gallery root. Three
files:

- `index.html`
  - A new function, `startCardHtml()`, draws the start block: the
    card's picture (edge to edge below 768 px wide, a framed card above
    it), the title, the card's `description`, and an Enter button with
    an arrow. A tap on the picture or the button opens the card, through
    the page's own `openCard()`, so the room's back link works as for
    any other card.
  - `renderLobby()` draws that block first, after the welcome line.
    The heading "Doors" is now "Or explore by subject". The Solar
    System card is skipped under Featured, so it is drawn once.
  - The header comment gains an "Updated: October 9, 2026" entry.
- `gallery/gallery_config.json`: a top-level `"sentence"`, "The solar
  system, the Earth and the stars, to explore." The page has read this
  key since L-282; the file had none, so the typed default showed.
- `gallery/gallery_metadata.json`: card `solar_system`'s
  `description` becomes "Today's planets in 3D. Turn it with your
  finger, tap a planet, step into the Sun and Earth." "Daily updates
  from JPL Horizons" leaves it, as ruled; the room names its source.

The patch checks `index.html` against its content at 5ec4739, and the
two JSON files only at the values it changes, so a later card edit in
the gallery editor does not block it. A second run says "already
applied" and writes nothing.

## 2. Two calls the build made, and why

- **The title is typed, not served.** The brief left this to the build.
  The card's served title, "The Solar System, live", also heads the card
  on the Solar System door's page and in the menu, where "Start with
  ..." would read wrong. So `index.html` holds
  `LOBBY_START_TITLE = 'Start with the Solar System, live'` beside
  `LOBBY_START_ID = 'solar_system'`, the card it is written for. If that
  card is not served in a tab, the lobby opens on the subjects as
  before, under "Explore by subject".
- **The order inside the block follows the canvas Tony chose.** The
  brief lists the heading above the picture. The artboard Tony picked
  (E, "Lobby E: the picture is the way in", on his canvas "Lobby: the
  Solar System way in") draws the picture first, then the title, the
  sentence and the button, as one tappable block. The build follows the
  artboard. Moving the title above the picture is one line if Tony
  prefers it.

## 3. Verification

Headless Chromium (Playwright), a throwaway copy of the gallery with the
patch applied, served over a local web server; Plotly, Google Fonts and
the analytics script stubbed or blocked.

- **Phone, 390 x 844:** start block 186 to 592 px; Enter button 521 to
  573 px. Inside the first screen. The picture is the full 390 px wide
  and loads (1200 x 600, the L-363 version B picture, kept at 2:1 so the
  crop is the same).
- **Desktop, 1280 x 800:** the block sits in the 560 px column as a
  framed card; Enter ends at 617 px.
- **Nothing drawn twice:** in the lobby, card `solar_system` appears
  once, as the start block. Featured now holds the other four featured
  cards, and no wide card is left there.
- **Door counts unchanged:** phone 33 / 57 / 9, desktop 36 / 57 / 9,
  the Solar System door with 4 interactive scenes; identical to the
  unpatched page, and the desktop counts recomputed from
  `gallery_metadata.json` agree.
- **The door's page:** still opens with the wide card first, now with
  the new sentence.
- **Enter and the picture** both go to
  `interactive.html?exhibit=solar-system`. No script errors.
- **The gallery maintenance run** (offline pass): 28 PASS, 3 FAIL on the
  patched copy, and the same 28 and 3, row for row, on the unpatched
  base. The three FAIL rows are Pole of date, its ERFA checks and
  Artifact 1 assembler; they fail the same way without the patch,
  because this sandbox lacks the packages they need.
- **No check covers the lobby.** The guest book row tests
  `gallery/guestbook.js` only, and Page framing is for rooms. This is
  already recorded as a class on L-367 (no checker opens a new room,
  and nothing reads the lobby code), item 6 of L-423 (the website's
  checks). The records patch adds a dated line there; nothing chased.

## 4. Shown to Tony, not asked

- "Turn it with your finger" is phone wording; the desktop turns it
  with a mouse. The desktop screenshot shows it. A second sentence for
  desktop would be a follow-up.
- The button says "Enter". One word, as drawn.
- On the phone the "Or explore by subject" heading now sits lower, over
  the doves of the background wall. Worth a look on the real phone,
  where the wall stays fixed as the page scrolls.

## 5. The records patch

`patch_L428_2_records_20261009.py`, run from the orrery root. It
checks each file only at the lines it edits.

- `LEDGER_CONSOLIDATED.md`: a header stamp; L-428 (the lobby's way in)
  opened; one line each on L-282 (the lobby), L-363 (the Solar System
  room and the front door: its card moved), L-367 (no checker opens a
  room: met again), and L-414 (the scanner's window: Tony's run, quoted
  from his copy `documentation/WHERE_WE_ARE_10-8-26_1406_run_record.md`,
  which ends "21 of 21 gating checkers passed"; `PROVENANCE_AUDIT.md`
  at b6652f9 reads "GATE PATH: 0 TIER-1 -- the push gate holds."). L-414
  is NOT closed here: its next session confirms provenance-discipline
  2.28 loads, which needs that skill, and this session did not load it.
- `documentation/WHERE_WE_ARE.md`, by section: the date line, the box
  (changed, needs you now), one Settled line, the Signals, and one
  Where-the-details line. Nothing below the run-record marker.
- `documentation/HANDOFF_lobby_option_E_20261009.md`: this file.

Not done, recorded: the page's run-record zone still holds the
patch_L395_4 run of October 8. Tony's copy
`WHERE_WE_ARE_10-8-26_1406_run_record.md` already holds it. The zone is
Tony's, so this patch left it alone.

## 6. Tony's steps

1. **(do)** Gallery: save `patch_L428_1_lobby_option_e.py` in the
   gallery repo's root folder, open it in VS Code, press Run. Expect
   eight "ok" lines and "patch applied".
2. **(do)** Commit and push the gallery in GitHub Desktop. Move the
   script into the gallery's `documentation/` folder (in the same or
   the next commit).
3. **(do)** Look on the phone: close the Home Screen clip's tab first,
   so the phone fetches the new page. The lobby should open on the
   picture and the Enter button; Enter opens the Solar System room.
4. **(do)** Orrery: save `patch_L428_2_records_20261009.py` in the
   orrery repo's root folder, press Run, then run
   `orrery_maintenance_run.py`. Move the script into `documentation/`,
   commit and push.
5. **(decide, after the look)** Whether L-428 closes, or something
   changes first.

## 7. Not this session

- The front-door address change (L-363: a bare interactive.html link
  opens the Solar System room). Waits for L-423 (the website's checks).
- `interactive.html`, the rooms, the drawer; the welcome count line,
  Featured's order, the guest book.

## Appendix: the headless lobby render

Claude-only. Run from anywhere with Playwright installed:
`python render.py <gallery_root> <out_prefix>`. It prints the facts
quoted in section 3 and writes phone and desktop screenshots.

```python
"""Render the lobby of a gallery checkout headlessly and report facts.
usage: python render.py <gallery_root> <out_prefix>"""
import sys, json, threading, http.server, functools, socketserver
from playwright.sync_api import sync_playwright
root, out = sys.argv[1], sys.argv[2]
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.TCPServer(("127.0.0.1", 0), functools.partial(Q, directory=root))
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = "http://127.0.0.1:%d/" % port
STUB = ("window.Plotly={newPlot:function(){return Promise.resolve()},"
        "purge:function(){},relayout:function(){return Promise.resolve()}};")
report = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, vp, mobile in [("phone", (390, 844), True), ("desktop", (1280, 800), False)]:
        ctx = b.new_context(viewport={"width": vp[0], "height": vp[1]}, is_mobile=mobile,
                            has_touch=mobile, device_scale_factor=2 if mobile else 1)
        pg = ctx.new_page()
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.route("**/cdn.plot.ly/**", lambda r: r.fulfill(body=STUB, content_type="text/javascript"))
        pg.route("**/fonts.g*/**", lambda r: r.abort())
        pg.route("**/*googletagmanager*/**", lambda r: r.abort())
        pg.goto(base + "index.html", wait_until="networkidle")
        pg.wait_for_timeout(800)
        facts = pg.evaluate("""() => {
          const q = s => Array.from(document.querySelectorAll(s));
          const r = el => { if (!el) return null; const b = el.getBoundingClientRect();
                            return {top: Math.round(b.top), bottom: Math.round(b.bottom)}; };
          return {
            headings: q('.lobby-heading').map(e => e.textContent),
            welcome: (document.querySelector('.lobby .welcome-text')||{}).textContent,
            start: r(document.querySelector('.lobby-start')),
            enter: r(document.querySelector('.lobby-start-enter')),
            pictureLoaded: (document.querySelector('.lobby-start-picture')||{}).naturalWidth || 0,
            lobbyCards: q('#welcomeState [data-viz-id]').map(e => e.getAttribute('data-viz-id')),
            doors: q('.lobby-door').map(e => [e.getAttribute('data-door'),
                                              e.querySelector('.lobby-door-meta').textContent]),
          };
        }""")
        facts["pageErrors"] = errs
        pg.screenshot(path="%s_%s.png" % (out, name))
        pg.click(".lobby-door[data-door='solar_system']")
        pg.wait_for_timeout(400)
        facts["doorPageFirstCard"] = pg.evaluate(
            "(() => { const c = document.querySelector('.room-card, .lobby-wide');"
            " return c ? [c.getAttribute('data-viz-id'),"
            " (c.querySelector('.lobby-wide-desc')||{}).textContent] : null; })()")
        pg.goto(base + "index.html", wait_until="networkidle")
        if pg.query_selector(".lobby-start-enter"):
            with pg.expect_navigation(timeout=5000):
                pg.click(".lobby-start-enter")
            facts["enterGoesTo"] = pg.url.replace(base, "")
        report[name] = facts
        ctx.close()
    b.close()
print(json.dumps(report, indent=1))
```

Session record written October 2026 with Anthropic's Claude Opus 5.5.
