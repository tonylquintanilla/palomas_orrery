"""patch_L280_284_interactive_wing_capture.py

Captures the 2026-09-03 design conversation as FIVE new ledger items.
Nothing is built by this patch; it records decisions so they do not
float. Capture on first mention.

  L-280  The Interactive Wing: door, hall, two rooms, What's New
  L-281  The guest book: no-account comments, approve-before-show
  L-282  The lobby: the main page as an entrance hall
  L-283  Visual theme: dark wall, paper placards, record mode
  L-284  Retire the social export; the gallery owns publishing

Repo:   tonylquintanilla/palomas_orrery (the ORRERY repo)
Run it: save in the repo ROOT, open in VS Code, click Run. Command
        line equivalent: python patch_L280_284_interactive_wing_capture.py

RUN ORDER: third of three orrery patches this session, after
patch_L277_reanchor_site_stores.py and patch_L276_mode7_repo_access.py.
The ledger is anchor-guarded rather than fingerprinted (the maintenance
run regenerates its index zone, so a fingerprint would depend on whether
that run happened in between). It refuses unless the L-277 record and
the L-276 closure are both present, and unless no L-280..L-284 block
exists yet. The blocks land in section A immediately above L-278,
matching where the last session's items went. Run ledger_index.py (or
the maintenance run) afterwards to regenerate the index.

Built on orrery faac433f138564d1426835b80ed56562a3ccb5c9 at
https://github.com/tonylquintanilla/palomas_orrery (branch main), with
the two patches above applied.

Module updated: September 3, 2026 with Anthropic's Claude Fable 5.1.
"""

import os
import sys

LEDGER = 'LEDGER_CONSOLIDATED.md'
ANCHOR = '#### [L-278] A relayout from inside a Plotly event handler re-enters the update machinery\n'
REQUIRE = [
    'patch_L277_reanchor_site_stores.py',
    '<!-- L:276 status:DONE',
]

NEW = """#### [L-280] The Interactive Wing: door, hall, two rooms, What's New
<!-- L:280 status:OPEN upd:2026-09-03 section:A flag: rice:4/4/80/3 -->
- **Raised by Tony 2026-09-02, designed in conversation 2026-09-03.**
  `interactive.html` without `?exhibit=sun` still serves the old premade
  Solar System Explorer. The gallery's theme is a scientific museum:
  the static gallery is the permanent collection, and the interactive
  is a new WING under construction where the visitor chooses what to
  explore and where to stand. The wing must announce itself as a work
  in progress. Tony: "the general philosophy of the interactive is
  appropriate."
- **The door.** One card on the main gallery page, in the same visual
  language as the other cards, marked plainly: Interactive Wing, under
  construction, first rooms open. It opens the hall.
- **The hall** (`interactive.html`, no parameter). A short placard in
  museum voice, not software voice: what the wing is (you choose what
  to look at and where to stand, instead of a fixed view), that it is
  being built room by room, and that it runs real computation in the
  browser, which is why it takes a moment to open. Then the OPEN rooms,
  a What's New list, and the guest book (L-281) at the bottom. The hall
  never lists rooms that do not exist.
- **Two rooms today.** The Sun exhibit (L-267) as it stands: in museum
  terms the drawer is the case labels, the focus label is where you are
  standing, the cross markers are the small placards beside each
  object, the i panel is the wall text with its source links. And the
  premade Solar System Explorer as a second room -- a fixed view of the
  planets on a chosen date -- kept because it works and is different in
  kind, reachable under its own parameter so nothing breaks. Tony's
  ruling: the premade room is EVENTUALLY REPLACED by a full set of
  interactive planets as the braid reaches them.
- **"What's New", not "Next."** Tony's ruling: no promises, a record.
  Dated one-line entries fed from a small JSON file in the gallery
  repo, one line per shipped change, written as part of each shipping
  patch. The sign updates because the patch does, not because someone
  remembers. ONE feed for the whole museum (the lobby, L-282, reads the
  same file).
- **Growth rule.** When a body ships it appears in the hall as a room
  and in the Sun room's drawer as a body you can focus on. Carried from
  the desktop GUI: bold means "can be the focus"; the date control
  appears only when something in the scene has a position to move -- a
  shell has no date, an orbit does.
- **Room-shape rule (Tony's breadcrumb, 2026-09-03).** Earth System
  exhibits need a lot of horizontal room; time is horizontal. In
  portrait the room is wider than the screen and is SWEPT sideways
  while placard and drawer stay put. Consequences to honour now: the
  chrome never assumes the plot fits the viewport; a room declares its
  shape (wide or square) in its config and the chrome reads it; in
  wide rooms the plot's own horizontal drag is given to the sweep. A
  data-shape decision, recorded as a rule rather than a task.
- **Note:** RICE 4/4/80/3 -> 4.3 proposed, not confirmed. Portrait
  first (Mode 5 is Tony's). Nothing in this item is built; L-265 and
  Stage C of L-267 still gate the Sun room's i panel.
**Gap:** the door card; the hall (placard, room list, What's New,
guest-book slot); the What's New JSON and the rule that shipping
patches append to it; the room-shape field in the room config.
**Ref:** L-267 (Sun room), L-265 (i panel links), L-281 (guest book),
L-282 (lobby), L-283 (visual theme), L-268 (feature identity);
interactive.html; index.html; gallery_metadata.json;
MASTER_PLAN_INTERACTIVE_GALLERY.md.

#### [L-281] The guest book: no-account comments, approve-before-show
<!-- L:281 status:OPEN upd:2026-09-03 section:A flag: rice:3/2/70/1 -->
- **Tony's ask, 2026-09-03:** a visitor comments blog, "if possible."
  Then the bar: "I would prefer a low bar no sign up option to post
  with my moderators option to delete."
- **It is possible on a static GitHub Pages site.** Recommendation:
  **Cusdis** (cusdis.com, GPLv3, ~5 kB widget, no cookies, no
  tracking). A visitor types a name and a message, no account. Nothing
  shows until Tony approves it -- from a dashboard, or from a Quick
  Approve link in the notification email, on the phone. So the
  moderator's option is stronger than delete: nothing unread is ever
  shown. Integration is a container div and one script tag.
- **Caveats, recorded from the vendor's own page 2026-09-03.** No spam
  filter; every comment is moderated by hand (a feature for a guest
  book, a chore if the site gets busy). Free hosted plan: 1 site, 100
  approved comments a month, 10 Quick Approves a month; Pro is $12 a
  year with no limits. Small open-source project; self-hosting is
  possible if the hosted service ever goes away, but that is server
  work this project does not do today.
- **Fallback:** giscus (comments as GitHub Discussions; backed by
  GitHub so it will not disappear; but a visitor needs a GitHub account
  to post). Rejected for now on the sign-up bar. Disqus rejected on ads
  and tracking.
- **Tony-action (decide):** Cusdis hosted free tier to start, or wait
  until the hall exists. Adds a third-party script to a public page.
- **Note:** RICE 3/2/70/1 -> 4.2 proposed, not confirmed.
**Gap:** decision; then a Cusdis account, the two-line embed at the
bottom of the hall (L-280), and a line in the placard saying comments
are read before they appear.
**Ref:** L-280; https://cusdis.com/; https://github.com/djyde/cusdis.

#### [L-282] The lobby: the main page as an entrance hall
<!-- L:282 status:OPEN upd:2026-09-03 section:A flag: rice:5/4/75/4 -->
- **The main page today** (palomasorrery.com, read 2026-09-03): a
  title, a Desktop/Mobile switch, a plot that loads immediately, a menu
  the visitor has to find to choose an exhibit, and the "about" text
  behind an i button. A visitor lands INSIDE a plot.
- **A museum lands you in an entrance hall.** Seven proposals, Tony:
  "I like your ideas."
  1. THE LOBBY. First screen: the name, one sentence, the wings laid
     out as doors -- Solar System, Missions, Stars and Exoplanets,
     Earth System, and the Interactive Wing with its construction
     notice. The categories already exist in the gallery config; the
     doors are a first screen, not new content. Today's landing plot
     becomes the first room of the Solar System wing.
  2. ONE PLACARD FORMAT for every room, static and interactive: title,
     one sentence saying what you are looking at, the date or range,
     the sources as links. A visitor learns the placard once. (One job
     per control, applied across both wings.)
  3. SAME CHROME in both buildings: header, i button, drawer feel --
     one shared stylesheet, not two pages kept in step by hand.
  4. WAYFINDING, NOT A MODE SWITCH: detect the screen, design portrait
     first, leave a small switch in settings.
  5. ONE "WHAT'S NEW" for the whole museum, in the lobby, fed by the
     same file as the wing's (L-280).
  6. A COLLECTIONS ROOM: the sources -- JPL Horizons, Gaia and
     Hipparcos, ERA5 and Copernicus -- as a page in the same link
     format. Provenance the visitor can see; L-266 (the dead-link
     check) becomes the museum's conservation department.
  7. EACH WING GETS ITS SENTENCE. "Data Preservation is Climate Action"
     is already the Earth System wing's; the others have none yet.
  8. THE COLLECTIONS ROOM SAYS WHAT THE DISCIPLINE IS, WITHOUT CLAIMING
     AUTHORITY. Tony, 2026-09-03: "somewhere we should briefly talk
     about our provenance discipline as a scientific effort while not
     claiming any special authority." Draft placard, approved "as
     drafted for now":
       "About our sources. Every number shown in this gallery is meant
       to trace back to something you can check: a JPL Horizons
       ephemeris, a Gaia or Hipparcos catalog entry, a Copernicus
       climate dataset, a published paper. Where a value has a source,
       the placard links to it. Where we could not find one, we say so,
       or we leave the value out. We hold ourselves to this because it
       is how science is supposed to work, not because we are an
       authority on any of it. This is an amateur's museum, built by a
       retired engineer and an AI in conversation. The discipline is
       ours; the authority stays with the sources. If you find a value
       that does not match its source, tell us in the guest book. That
       is what it is for."
     Three things it does on purpose: it states the rule in the same
     form the protocol does (source it, say so, or leave it out); it
     names who built it in plain words so the code's polish does not
     stand in for credentials (the same warning WHO TONY IS gives relay
     partners); and it makes the guest book (L-281) part of the
     discipline, not only hospitality.
- **Note:** the lobby (1) is the one that changes the visit and is the
  largest, since it reshapes the first screen of a public page; the
  rest are consistency. RICE 5/4/75/4 -> 3.75 proposed, not confirmed.
  Portrait first; Mode 5 is Tony's.
**Gap:** design the lobby screen in conversation before building
(iterate; each round simpler); then the shared stylesheet; then the
placard format applied to existing cards; then the collections room.
**Ref:** L-280, L-283, L-266; index.html; gallery_config.json;
gallery_metadata.json; skills/gallery-pipeline.

#### [L-283] Visual theme: dark wall, paper placards, record mode
<!-- L:283 status:OPEN upd:2026-09-03 section:A flag: rice:4/3/80/3 -->
- **Tony's ruling 2026-09-03: "dark wall with paper placards -- let's
  go with this."** Mode 5 throughout; Claude proposes, Tony's eye
  judges.
- **The bones stay.** Dark void background, Cormorant Garamond for
  display, DM Sans for controls: a serif that reads as engraved wall
  text over a sans that reads as signage. Improvements are about using
  them with intent, not changing them.
- **The rules, as agreed:**
  - The wall is dark; the labels are paper. Placards as light cards:
    warm off-white, dark type, a thin rule at the top. Separates "what
    you are looking at" from the thing itself; reads well in portrait
    where the panel covers the plot.
  - One accent per wing, used sparingly -- a hairline on the door, the
    placard rule, the header position, nowhere else. Warm gold Solar
    System; blue-green Earth System; cool violet Stars and Exoplanets;
    steel grey Missions; an unfinished material (raw copper or
    hazard-tape ochre) for the Interactive Wing while under
    construction -- the scaffolding announces itself without a banner.
  - The plots keep their own colors. Traces, shells and markers are
    data ink chosen for meaning; the same body looks the same in every
    room. If chrome color competes with a trace color, the chrome
    loses.
  - Three type sizes only: room title in Cormorant, placard sentence in
    Cormorant italic, everything else DM Sans at one size.
  - Motion stays still: no animated chrome transitions; only the sky
    moves.
  - Portrait is the design surface: drawer as a bottom sheet, placard
    as a card sliding over the plot, thumb-sized targets. Desktop gets
    the same pieces with more room, not a different design.
  - Two touches the artist owns: an engraved-style plate in the lobby
    with the museum's name and the dedication to Paloma; one consistent
    i-button icon that looks like a wall label, not a software glyph.
- **RECORD MODE (Tony's breadcrumb, 2026-09-03): "the views should be
  easily recorded in Instagram Edits."** A view that records well
  needs four things: a 9:16 frame so the room composes in portrait
  rather than being cropped from landscape; one tap to hide the chrome
  so only the sky and one placard remain; a clean, non-transparent
  background, because a screen recorder captures what it sees; nothing
  that flickers or reflows on load, since a recording shows the seam.
  A property of EVERY room, static and interactive, so it becomes a
  habit rather than a feature. The desktop orrery's social export
  solved the still version of this; record mode is the moving version
  and it lives in the gallery (see L-284).
- **Note:** RICE 4/3/80/3 -> 3.2 proposed, not confirmed.
**Gap:** a shared stylesheet carrying the palette, the accents, the
placard card and the three type sizes; a record-mode toggle in the
shared chrome; Mode 5 passes on phone and tablet.
**Ref:** L-280, L-282; interactive.html (CSS variables block);
index.html; skills/gallery-pipeline (mobile/portrait rendering).

#### [L-284] Retire the social export; the gallery owns publishing
<!-- L:284 status:OPEN upd:2026-09-03 section:A flag: rice:2/2/95/2 -->
- **Tony, 2026-09-03:** "the social view in the orrery is a legacy item
  I don't use. It is fully replaced by the gallery editor."
- **What it is.** `social_media_export.py` (1,168 lines, 14 functions,
  Domain: gallery) turns a plotted figure into a 9:16 portrait HTML for
  social video. Two GUI callers: the "export social view" button and
  `export_social_view()` in `palomas_orrery.py` (with the figure stored
  for it at two plot sites), and a "Social Media Export" frame plus
  `export_social_view()` method in `star_visualization_gui.py`.
- **Nothing depends on it, checked 2026-09-03 in both repos.** The
  gallery's `tools/gallery_studio.py` and `tools/gallery_json_fixer.py`
  each carry their OWN `_parse_hover_html()` and say so in comments;
  neither imports the orrery module (L-270 already corrected the README
  claim that Studio did). The gallery-pipeline skill already calls it
  "mostly superseded by Studio." The provenance scanner scans it as the
  only gallery-domain file in this repo.
- **The boundary this makes clean:** the orrery PLOTS; the gallery
  PUBLISHES. Record mode (L-283) is the moving version of what this
  module did for stills, and it belongs in the gallery, not back in the
  orrery.
- **Where the retirement has to travel -- the stores, so the correction
  does not stop in the code:**
  - Code: delete the module; remove the button, `export_social_view`
    and the two "store fig for social export" lines in
    `palomas_orrery.py`; remove the frame and method in
    `star_visualization_gui.py`; drop it from the role tables in
    `add_docstrings.py` and `module_atlas.py`.
  - Check All Parallel Pipelines names FIVE consumers and social export
    is one; it becomes FOUR, in ALL FOUR stores the L-269 correction
    reached: PROJECT_INSTRUCTIONS.md, README.md, documentation/CLAUDE.md,
    skills/orrery-coding-conventions (a version bump). The
    provenance-discipline skill's "currently just social_media_export.py"
    sentence goes too (a second bump).
  - Docs: README.md's key-documents row for social_media_readme.md and
    its "portrait view for social video" sentence go;
    documentation/social_media_readme.md stays as an archive.
- **Discovery is done; removal is its own patch** (The Braid), because
  it touches the protocol and two skill versions. Not on the critical
  path; sits inside files future L-254 and GUI work will open anyway.
- **Note:** RICE 2/2/95/2 -> 1.9 proposed, not confirmed.
**Gap:** the removal patch (code + four consumer-list stores + two skill
bumps + README), then a maintenance run to confirm the atlas and the
scanner drop it.
**Ref:** L-269 (the consumer list and its stores), L-270, L-283;
social_media_export.py; palomas_orrery.py; star_visualization_gui.py;
skills/gallery-pipeline; skills/provenance-discipline.

"""


def fail(msg):
    print('FAILURE: ' + msg)
    print('NOTHING was written. Undo is Discard Changes in GitHub Desktop.')
    sys.exit(1)


def main():
    try:
        NEW.encode('ascii')
    except UnicodeEncodeError as exc:
        fail('inserted text is not ASCII: %s' % exc)
    if not os.path.exists(LEDGER):
        fail('%s not found -- run from the orrery repo root' % LEDGER)
    raw = open(LEDGER, 'rb').read()
    is_crlf = raw.count(b'\r\n') > 0
    text = raw.replace(b'\r\n', b'\n').decode('utf-8')

    for needle in REQUIRE:
        if needle not in text:
            fail('the ledger lacks %r -- run the L-277 and L-276 patches first' % needle)
    for n in range(280, 285):
        if ('#### [L-%d]' % n) in text or ('<!-- L:%d ' % n) in text:
            fail('L-%d already exists; this patch has run' % n)
    count = text.count(ANCHOR)
    if count != 1:
        fail('ANCHOR FAIL: L-278 header matched %d times' % count)
    print('ok  ledger carries L-277 record and L-276 closure; L-280..284 absent')

    out = text.replace(ANCHOR, NEW + ANCHOR)
    for n in range(280, 285):
        if out.count('#### [L-%d]' % n) != 1 or out.count('<!-- L:%d ' % n) != 1:
            fail('post-condition: L-%d not present exactly once' % n)

    data = out.encode('utf-8')
    if is_crlf:
        data = data.replace(b'\n', b'\r\n')
    with open(LEDGER, 'wb') as f:
        f.write(data)
    print('wrote  %s: L-280, L-281, L-282, L-283, L-284 inserted above L-278'
          % LEDGER)
    print('patch applied. Next: ledger_index.py (or the maintenance run)')
    print('  regenerates the index; expect 5 more live items.')


if __name__ == '__main__':
    main()
