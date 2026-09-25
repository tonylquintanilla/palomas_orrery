# Gallery card pass -- run record: every card looked at, what was changed, what was found

Built on gallery `9c61fb21`, read live with `git ls-remote` on
2026-09-24 for this copy (it was `ff324a0ec51bb4d19f728e41d8d4dbdad98b9ebf`
for the copy before)
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `fb8d927e1581f6ad2fe49aa04a8d30d50e7f8d71`
at https://github.com/tonylquintanilla/palomas_orrery (read, not changed).
Both HEADs read live with `git ls-remote` on 2026-09-24 for this copy.
The record was started on gallery `386a44ff` and orrery `dcc36e38`, and
the pass itself began earlier the same day on gallery `1ae9de50` and
orrery `efd2e2ba`.

**Type: RUN RECORD, kept open.** Begun September 22, 2026, Tony with
Anthropic's Claude. It is rewritten as each card is finished, and each
new copy replaces the last. It closes when the last card is done, and the
ledger patch that follows it is written from section 5.

**Rules this work ran under**, each loaded in this session and each
matching the protocol's manifest table at v3.67: safe-file-editing 1.11,
gallery-pipeline 1.2, ledger-and-session-records 1.11. For section 3i,
loaded in the session of 2026-09-24 and each matching the table at
v3.68: gallery-pipeline 1.2, interactive-exhibit 1.4,
ledger-and-session-records 1.11, safe-file-editing 1.11.

**Where the earlier part comes from.** Sections 2 and 3 up to the refusal
were done in the previous session ("Gallery editor card cleanup and
layout fixes"). Its running notes lived in that session's sandbox and are
gone; what is written here was read back from that chat and from the
gallery's commits. It is a claim about that session, not a re-measurement,
except where a line says it was checked here.

---

## 1. What the pass is

Tony goes through the gallery card by card and says what looks wrong.
Each finding is either fixed as a patch, changed by Tony in the gallery
editor, or recorded for the ledger. Tony's eyes are the check: none of the
gallery's gating checks reads what the lists show or where buttons sit.

At gallery `386a44ff` the metadata holds 145 cards, and all 145 are
served (none is in Storage). Three are live rooms with no file: Solar
System Explorer, Solar Structures, and Earth and Moon.

## 2. Card 1 -- Solar System Explorer

**Changed in the editor by Tony**, both checked here against the commits:
its shape from 16:9 to 9:16 (gallery `1ae9de50`), and its Featured flag
turned on (gallery `42fd97dd`).

**Patched:** `patch_L285_explorer_buttons_to_bottom_20260922.py`, built on
`1ae9de50`, moved the Explorer's buttons to the bottom of the screen. It
also hid two pieces of room chrome that had been showing on the Explorer
since 2026-08-31, the "In this scene" button and an empty grey pill, and
tightened the legend so ten planets no longer reach the + button on a
phone. Pushed at gallery `83a72d11`. Tony: "both desktop and phone look
right, as expected."

**Recorded, not fixed:**
- Still crowded on a small phone (375 by 553 pixels, where the legend
  meets the + button by about 32 pixels) and on any phone held sideways,
  where the picture is about 160 pixels tall and Plotly's toolbar covers
  the arrow cross. Sideways was crowded before this patch too.
- Two files in the orrery still describe the old layout: the Nav cluster
  row in `skills/interactive-exhibit/SKILL.md`, which says a button
  holder's corner is set only by `.nav-cross-apart`, and L-285's ledger
  note, which says the Explorer's overlap is open.

## 3. Cards 2 and 3 -- Inner Solar System Animation, the 16:9 and 9:16 pair

**What Tony saw.** The 16:9 card is too compressed on the phone and should
not be offered there. The 9:16 card works on the phone but not on the
desktop, because its hover text only appears through the phone's info
card. The editor has no control to take a card off one device.

**Why.** The two cards were converted on 2026-02-17, before the gallery
linked a figure's two shapes, and their file names share no stem, so
nothing ever linked them. Every trace in the 9:16 file has empty hover
text; the words were moved into a hidden data field for the info card,
and the page wires that card only in Mobile mode.

**Tony's ruling, 2026-09-22:** the Desktop tab lists the 16:9 cards and
the Mobile tab the 9:16 cards. A card with no counterpart in the other
shape, and a live room, list in both. This replaces L-287's rule of
2026-09-05, that every card shows in every mode.

**Patched:** `patch_L303_tab_shows_its_own_shape_20260922.py`. It
rewrites one function in `index.html`, `inCurrentMode()`, which the room
lists, the lobby and the welcome count all read, and it links the two
animation cards to each other in `gallery/gallery_metadata.json`.

**The first cut refused**, built on `83a72d11`. It said BASE MOVED
because it fingerprinted the whole metadata file, and Tony's two editor
saves in between (section 2) had changed it. Neither save touched the
lines the patch edits. The second cut, built on `386a44ff`, checks the
metadata only for what the patch needs, keeps the whole-file check on
`index.html`, works out the tab counts when it runs, and says so plainly
if it has already been applied. Tested here on copies of both files, with
LF and with Windows line endings plus a further editor save: it applied,
and the only metadata change was the two new link lines. A second run
refused, saying it had already been applied.

**What the site should show after the push**, computed here from the
metadata at `386a44ff`: 104 exhibits in each tab, where both show 145
today. What leaves Desktop is the 41 portrait twins, and what leaves
Mobile is their 41 landscape partners. 46 landscape-only cards, 14
portrait-only cards and the 3 live rooms stay in both. The Featured strip
shows 5 cards in each tab; the previous session said 4, before Tony
featured the Explorer.

**Done.** Pushed at gallery `2a80a68c`. Checked here at that commit:
`index.html` holds the new `inCurrentMode()`, and the two animation
cards name each other in the metadata. Tony's run of the patch, his
maintenance runs and what he saw are in the Tony section below: 15 of 15
offline checks and 2 of 2 live checks passed, and all four things step 5
asked him to look at were as expected (104 in each tab, 5 Featured cards
in each, the animation once per tab in its own shape, and the 16:9
animation gone from the phone).

**Tony's observation from the same look:** the tab split does not show
on the front page. It appears only once a visitor opens one of the three
doors. Tony adds that this points to a gap in the front page, and that
the guest book is still under construction. Recorded in section 5; no
ruling yet on what the front page should do.

## 3a. Card 4 -- Inner Solar System (the static 9:16 view of 2005-02-04)

**Deleted by Tony in the editor**, at gallery `1a12cade`. Card
`paloma_social_view_2005_02_04`, portrait only, no twin, one of the
cards whose desktop hover box was empty. The metadata now holds 144
cards. Computed here from the metadata at `1a12cade`: 103 exhibits in
each tab, 5 Featured in each.

Its file, `gallery/paloma_social_view_2005_02_04.json`, is still in the
repo. That is the editor working as designed, not a problem: its Delete
leaves the file on purpose, and `tools/gallery_cleanup.py` removes files
no card uses. (The previous copy of this record listed it as a problem;
corrected here.)

## 3b. Housekeeping done alongside

Tony moved twelve documents out of the gallery's `documentation/` and
into the orrery's (gallery `2a80a68c`, orrery `cb254b01`). Checked here:
all twelve are in the orrery, each identical to the gallery copy apart
from line endings. They are 3d_axis_control_handoff,
AS_BUILT_L173_numbering_fix, HANDOFF_earth_build_order_20260906,
M2_IMPLEMENTATION_REPORT, PREDESIGN_earth_exhibit_20260906,
SIZING_earth_moon_lagrange_20260907, TEST_PROTOCOL_mode5_pre_earth_20260906,
TEST_PROTOCOL_sun_hang_20260902, flyto_mobile_handoff,
gallery_subcategory_handoff, index_transform_audit and
non_destructive_routing_handoff. The spent tab patch was filed in the
orrery's `documentation/` too, where the patch said the gallery's.

## 3c. Card 5 -- Orbital Transformation of Mercury

**What Tony saw.** It reads well on the desktop, in both tabs, and not
at all on the phone. It is a 16:9 3D figure with no 9:16 twin, so the
phone squeezed the scene to fit, which looks like a broken card. The
editor offered no way to keep a card off the phone.

**Tony's ruling, 2026-09-22.** The editor's "Shape (phone only)" setting
has four choices: "16:9 2D" sweeps sideways as before; "16:9 3D" shows,
on a phone held upright, a card saying "Turn your phone to landscape to
view this card", and draws the figure when the phone is turned; "9:16"
shows as before; and "none" keeps the card off the phone. The desktop
keeps both tabs as they are, because space there is not limited. Tony
asked for the phone setting to allow no choice at all; a radio button
cannot be unticked, so "none" is a fourth button that does it.

**How the two 16:9 choices are decided.** The page chooses between
sweeping and the turn card by looking inside the figure for a 3D scene.
The editor reads the figure the same way and greys out the 16:9 choice
that does not match, so it cannot save a choice the page would not
follow, and no existing card had to be set by hand. At the time, 31
landscape cards were 3D; 23 of those have a 9:16 twin the phone shows
instead, and 8 did not: Orbital Transformation of Mercury, Earth
Barycenter Shells, Near Earth Asteroids, Pluto Barycenter System,
Trappist1 Exoplanet System, 3D Stars Distance to 20 Light Years, 3D
Stars Magnitude 4.0, and 3D Stars Magnitude 4.0 1400Ly.

**Patched:** `patch_L303_phone_setting_and_turn_card_20260922.py`, built
on `1a12cade`: `index.html`, the gallery editor, the JSON converter (a
re-export now keeps "none") and the sweep report. Tested here in a
stand-in phone and desktop and with the editor run headless. Pushed at
gallery `4c20194a`, alongside that morning's nightly run. Tony then set
Mercury to "none" in the editor, at gallery `e823e738`. His full run is
in the Tony section.

**What Tony saw on the phone:**
- **Mercury still opened**, as the turn card, and turned sideways it was
  drawn squeezed. He read this as "none" acting like "16:9 3D". The
  metadata at `e823e738` does say "none", and in the stand-in phone
  that card is gone from every list. Two things fit what he saw, and
  neither could be settled from here. The site can serve the old
  metadata for up to about ten minutes after a push, and he tested soon
  after his save. And a page first opened with the phone held sideways
  was taken for a tablet, which lists every card. The second is fixed
  in the follow-up below; the first needs only a reload.
- **After turning back upright there was no way back.** The turn card
  showed, but the menu button at the top left was gone and the
  browser's back button did nothing; only a reload brought the menu
  back. In the stand-in phone the menu stayed in place through the same
  turns, so the cause on his phone is not known. A page left zoomed or
  shifted by the turn fits what he saw.
- **The 2D sweep and the 9:16 view still work:** he checked the Keeling
  Curve and the featured Planetary Boundaries card. The other Planetary
  Boundaries card, a 2D figure that sweeps, does not look right (section 4).
- **The desktop, both tabs, is as before**, Mercury included.

**Follow-up patch:** `patch_L303_turn_card_way_back_20260923.py`, built
on `e823e738`, `index.html` only. The turn card carries its own "Back to
the gallery" button and scrolls itself to the top, so it no longer
relies on the menu button. And a touch screen whose short side is under
768 pixels counts as a phone when the page loads, so a phone opened
sideways leaves out what a phone leaves out; a narrow desktop window
still counts as before, and a short one does not. Tested here in the
stand-in: the button returns to the lobby, a turn made in the lobby
opens nothing, a phone loaded sideways does not list Mercury, and the
desktop at 1280 by 700 and 1280 by 800 lists all 142 cards.

**The follow-up, pushed at gallery `2e0fa8f5`.** Tony's run and both
maintenance runs are in the Tony section: 15 of 15 offline checks and 2
of 2 live checks passed. What he saw on the phone:
- **Mercury is gone from the phone**, held upright. So "none" works, and
  the earlier sighting was most likely the site serving the old
  metadata for a few minutes after his save.
- **Loaded sideways**, the phone shows the desktop-style menu with both
  tabs, and Mercury is not listed in either, the Desktop tab included.
  That is the follow-up doing what it says: a phone is a phone however
  it is held. The tab toggle appears because the page's layout still
  treats a sideways phone as a tablet; recorded in section 5.
- **The menu button still disappears** after turning the phone
  sideways and back upright. A reload held upright brings it back.

**What the screenshots showed** (Tony, iPhone Safari, 2026-09-23, the
turn card before and after a turn). After the turn the whole page sits
about 56 points higher on the screen, and the page's top bar, with the
menu button, is behind Safari's own address bar at the top. It is still
there, faintly visible through Safari's blurred bar, but it cannot be
tapped. So the cause is Safari's address bar, not the clock or the
notch as first guessed. Safari lays the page out as if its bar were
out of the way, which it is when the phone is held sideways, and keeps
that layout after the phone is turned back; a reload lays it out again.
The stand-in phone has no Safari bars, which is why it never showed.
This is how the browser handles a turn, so it can happen on any card
that is turned, not only the turn card. Recorded in section 5 as its
own item.

The "Back to the gallery" button is on screen and clear of Safari's bar
in both screenshots, and Tony confirmed it takes him to the lobby. With
that way back, Tony rates the hidden menu as minor.

**The picture behind the turn card is the site's own.** Both screenshots
show the crescent moon and birds, faded, behind the lower half of the
card. It is Tony's logo art, which the page draws at 14 percent
opacity behind everything on the welcome screen: a rule in index.html,
`.welcome-state::before`, uses `favicon.ico` (a 256-pixel copy of the
art) as its background. The turn card is shown in that same space, so
it carries the same background. The 5.1 MB `palomas_orrery_logo.png`
in the gallery's top folder is not used by the page at all. (The
previous copy of this record said nothing on the site draws a picture;
that was wrong, because the search looked for the PNG's name and the
page uses the icon file.)

**Done.** Card 5 closed on gallery `2e0fa8f5`, with Mercury set to
"none". The hidden menu after a turn is its own item in section 5.

## 3d. Two broken cards deleted by Tony

Both were cards whose file was not in the repo, found while checking
card 5. Deleted in the editor; the metadata holds 142 cards at
`e823e738`, and each tab lists 102 on the desktop.

- **Psyche - Mars Gravitational Assist 5-15-26 animated** (9:16). Its
  file was about 98 MB; Tony deleted it, probably because GitHub would
  not take a file that size.
- **Comet C/2025 K1 Breakup 10-16-2025**, the 16:9 card. Its file had
  been deleted from the gallery on 2026-04-05 and the card left behind.
  Before the tab change the desktop also listed the working 9:16 card,
  so nobody noticed; after it, the Desktop tab showed only the broken
  one. With it gone, the 9:16 card lists in both tabs, and its hover
  text is ordinary text, so it works on the desktop too.

## 3e. Card 6 -- Inner Solar System Animation, the 9:16 card

**What Tony saw, on the phone.** The view opens top-down. A tilt made
before pressing Play snaps back to top-down when Play starts, and a tilt
made while it plays does not stay.

**Why.** Reproduced here in a stand-in phone with real touch swipes.
Plotly writes a 3D scene's new angle into the figure when a mouse
button is released, but not when a finger lifts. The animation redraws
the scene at every frame, half a second apart, and each redraw draws
the angle the figure has on record. On a phone that record still held
the starting top-down view, so the first frame undid a tilt made before
Play, and each later frame undid one made while it ran. With a mouse on
the desktop the tilt was kept through Play, which is why only the phone
showed it. Nothing in the figure file is wrong; its frames carry no
camera of their own.

**Patched:** `patch_L303_touch_tilt_kept_20260923.py`, built on gallery
`2e0fa8f5`, `index.html` only. While a finger moves on the plot, and
when it lifts, the page copies each 3D scene's live angle into the
figure's record, as a mouse already does. Tested here on a copy: in
the stand-in phone the Inner Solar System Animation kept a tilt made
before Play and one made while it played, and stayed orthographic (the
flat, no-perspective view the figure asks for); the desktop animation
with a mouse behaved as before; and the earlier checks for cards 2 to 5
still pass (the turn card and its way back, Mercury off the phone, the
phone listing when opened sideways, the desktop listing).

It reaches every 3D card on a touch screen. The animated ones are four
pairs, each with a 16:9 and a 9:16 card: Inner Solar System Animation,
Psyche Mission to 16 Psyche, Psyche - Phobos Flyby, and Artemis II -
Moon Flyby. In the stand-in, Artemis II kept a tilt made before Play
even without the patch, and a tilt made while it played did not take
either way. The stand-in draws 3D in software and slowly, so this last
check is not conclusive for a real phone.

**Seen along the way, not caused by this patch:** pressing Pause on the
desktop logs one error in the browser's console, with no visible
effect. It appears with or without the patch.

**Done.** Pushed at gallery `27838dda`; the `index.html` served there
is byte for byte the copy tested here. Tony's check on the phone: the
render is correct. The same commit also carries
`data/constants_export.sha`, which moved from orrery `ac25d4f4` to
`bba21459`; that is the orrery's constants export recording its own
commit, not this patch.

## 3f. Card 7 -- Earth and Moon, the 9:16 card

**What Tony saw, on the phone** (two screenshots). Tapping a marker
opens the info card, and also draws an empty grey box over the render.
The box hides the figure and says nothing the card does not.

**Why.** Studio exports a figure whose hover goes to the info card with
a see-through Plotly hover label: colour `rgba(0,0,0,0)`, text 1 pixel
and see-through. Two things undo that. Plotly 2.35.2 draws a label
whose colour has zero opacity in grey (#444) instead, and every trace
carries its own hover font size of 11, which outranks the layout's 1
pixel. So each tap drew a grey box the size of the hover text, with the
text itself invisible. Checked two ways here: a bare Plotly page with
the figure's own settings draws the box in rgb(68, 68, 68) with
11-pixel text, and in the stand-in phone the unpatched page, on a tap
of Earth's Hill sphere, drew a grey box of that colour 607 by 190
pixels beside the card.

**How far it reaches.** 64 served figures were exported this way, 34 of
them 9:16. 21 of the 9:16 ones use the see-through colour and show the
grey box. The other 13 use a visible dark label. Whether that label
carries text was not measured figure by figure; the ones that are
empty are the "hover text kept only in the hidden field" class in
section 5. In Mobile mode the patch turns those labels off too.

**Patched:** `patch_L303_no_grey_hover_box_20260923.py`, built on
gallery `27838dda`, `index.html` only. In Mobile mode the page wires
the info card for exactly these figures, and for them it now turns
Plotly's own label off: a 3D scene's hover mode is set off, which
stops the label while a tap still opens the card, and a 2D plot's
traces show no label while their click is still sent. The figure files
do not change, and the Desktop tab is unchanged.

Tested here on a copy. On the stand-in phone, Earth and Moon: a tap
opens the Hill sphere card with no label drawn, where the unpatched
page drew the grey box. On the desktop, a 2D info-card figure
(Paleoclimate and Extreme Heating Events, 9:16): no label in the Mobile
tab, and its click still reaches the card; the Desktop tab still shows
its label as before. The checks for cards 5 and 6 still pass, including
a finger's tilt kept through Play.

**Done.** Pushed at gallery `2bd01fe`, 2026-09-23; the `index.html`
served there is byte for byte the copy tested here. The same commit
carries `data/constants_export.json` and `.sha`, the orrery's constants
export, not this patch. A second run of the patch on 2026-09-24, from a
copy left in the gallery's top folder, refused as already applied,
which is its guard working. Tony's check on the phone: a tap opens the
info card with no grey box over the render.

A commit Tony named, `ae96df03`, was not on GitHub when first checked;
it was a local commit, since pushed. It files a copy of the patch
script in the gallery's top folder, which `ff324a0e` then removes.

## 3g. Editor changes by Tony, gallery `ff324a0e`

Checked here against the commit. Set to "none" (not on the phone):
Earth Barycenter Shells 20260207 1635 and Near Earth Asteroids 20260207
2114, both 16:9 3D figures from the list in section 3c. Deleted: Near
Earth Asteroids on 2026 02 11 00:24, a 9:16 card. So Near Earth
Asteroids is no longer on the phone in either shape. The metadata holds
141 cards.

## 3h. Card 8 -- Apophis Closest Approach, the 16:9 and 9:16 pair

**What Tony saw.** Only the 9:16 card shows on the phone, which is
right. But in the editor the 16:9 card's phone setting still had
"16:9 3D" picked, which says the phone asks the visitor to turn it and
then shows this card. The phone never shows it.

**Why.** On a phone the page drops a 16:9 card whose 9:16 twin is
served, whatever the 16:9 card's phone setting says. The editor built
at card 5 read the setting from the card's own figure and never looked
at the twin.

**Patched:** `patch_L303_editor_twin_phone_note_20260924.py`, built on
gallery `ff324a0e`, `tools/gallery_editor.py` only. For a 16:9 card
whose 9:16 twin is in a room, the four phone choices are greyed out
with none picked, and the note says the phone shows the twin instead,
naming it; if the twin is set to "none", it says the phone shows
neither. It is the same test the page's phone filter makes, so a twin
kept in Storage does not count. Saving such a card keeps whatever it
already stores. Nothing the site serves changes.

Tested here with the editor run headless: the 16:9 Apophis card and the
16:9 Inner Solar System Animation card show the note with all four
choices greyed; the 9:16 Apophis card and Mercury are unchanged; the
twin-set-to-none and twin-in-Storage cases give the notes above; and
applying the form to the 16:9 card leaves it unchanged and unsaved.

**Found along the way, not changed:** the page builds its list of
served twins after it removes Storage, so it agrees with the editor.
No card's twin is in Storage today.

**Status: pushed.** Gallery HEAD read live on 2026-09-24 is `9c61fb21`,
Tony's push of this patch.

## 3i. The Moon room, and L-286 found again

**What Tony saw.** The editor shows a Moon room under the Earth room. The
served gallery does not, and lists all the Moon's cards directly under
Earth.

**Why.** The page knows only two levels of rooms, and the Moon is at the
third. In `gallery/gallery_config.json` the Moon is a room inside Earth,
inside the Solar System door. `normalizeSchemaV2()` in `index.html` keeps
only the first two parts of a card's room path, so
`solar_system/earth/moon` reads as `solar_system/earth`, and the side
menu draws only a door and one level of room under it. The six Moon cards
(Earth-Moon System on 2026 02 10 and the five Artemis II cards) list
beside Earth's own five, in both tabs. The Moon room was added on
2026-09-04 (gallery `b5622a8`) and its cards moved in on 2026-09-05
(gallery `2130a3f`), so the page has done this since then. No other room
is three levels deep yet. Nothing in this pass caused it.

**It is L-286, which the master plan had stopped mentioning.** L-286,
"Rooms in four levels", is the third item of step 2 in the master plan's
order of 2026-09-03. The notes of 2026-09-05 and 2026-09-06 say step 2 is
two of three items done. After that every update discusses steps 3 to 5,
and the newest "Next" paragraph goes from Stage D to Jupiter and Saturn.
No update ruled it dropped.

**Tony's rulings, 2026-09-24.**
- Build it now: "this is the gallery sweep and we found L286 again, so i
  would say we should build it so it is not left behind."
- The Desktop and Mobile tabs, which live in the side menu the rooms
  replace, move to the header on every desktop screen, the lobby
  included, and stay off the phone: "why can't the desktop room keep both
  views? both have positives and negatives. the phone is limited the
  desktop is not." Then "yes" to that placement. This also answers the
  finding in section 5 that the front page does not show the tab split.
- The rooms mockup, a Design canvas private to Tony
  (https://claude.ai/artifact/DLMy8Vu3nV5dNKPU4vFE8X): "Yes." It draws the
  real cards at gallery `9c61fb21`. It departs from the 2026-09-04 wording
  in one place: "Paloma's Orrery" at the far left of the header returns
  to the lobby, and the chain's first link opens the door's own screen.
- The look: "make the background favicon image more prominent and maybe
  adopt its dusk sky blue tone rather than pure black." Shown a revision:
  "i like it the way you have designed it."
- The art: Tony uploaded the original, `Gemini_palomas_orrery_logo.png`,
  1024 by 1024: "we should keep the Gemini mark not the generic ai mark."

**Recorded:** `patch_L286_2_ledger_rooms_ruling_20260924.py`, built on
orrery `fb8d927e`, `LEDGER_CONSOLIDATED.md` only, with the full rulings,
the mockup's contents and the build order on L-286 and the look on L-283.
The master plan is not edited, because the Earth work restamps it with
Stage D; L-286's Gap asks that restamp to put step 2 back.

**Next:** three `index.html` patches, each looked at on Tony's phone
before the next -- the rooms, the header, the look -- and then the chain
in `interactive.html`.

## 4. Cards still to look at

The rest of the gallery. Each gets a section here as it is done. Two are
queued from Tony's notes:
- **Trappist1 Exoplanet System**: not suited to the phone; Tony will set
  it to "none".
- **Planetary Boundaries, the 2D card that sweeps** (not the featured
  9:16 one): does not look right on the phone.

## 5. For the ledger, one row per class

Each of these is a kind of problem, not a single instance. None has a
ledger handle yet; the ledger patch at the end of the pass assigns them.

- **Hover text kept only in the hidden data field, so a desktop hover box
  is empty.** The previous session counted 20 served files, 14 portrait
  and 6 landscape, not re-measured here. Twelve of the portrait files had
  no landscape twin: 3D Stars to 20 light years; 3D Stars to Visual
  Magnitude 4.0; Paleoclimage and Extreme Heating Events (in two rooms);
  Earth-Moon System 2026-02-10; Inner Solar System Animation; Inner Solar
  System; Pluto System Barycenter; Voyager 1 and 2 Missions; Jupiter
  System; Near Earth Asteroids; Current Comets 2-10-2026. Since then
  Inner Solar System Animation has its twin and has left the Desktop tab
  (section 3), and Inner Solar System has been deleted (section 3a), so
  ten stay on the desktop with empty hover boxes. The
  six landscape files show an empty box on the desktop: Paleoclimate 540
  Ma; Orbital Transformation of Mercury; HR Diagram Magnitude 4.0;
  Paleoclimate Human Origins; Paleoclimate and Extreme Heating Events (two).
- **The front page does not show the tab split** (Tony, section 3). It
  appears only inside a door. Tony links it to a wider gap in the front
  page; the guest book is L-281, still open. ANSWERED for the tabs by
  Tony's ruling of 2026-09-24 (section 3i): they move to the header on
  every desktop screen, the lobby included; recorded on L-286.
- **A 3D figure drawn on a phone held sideways needs editing for that
  screen to look right** (Tony, cards 5 and queued Trappist1). "none" is
  the tool until a card is edited for it.
- **After a phone is turned sideways and back, Safari leaves the page
  under its address bar**, hiding the page's top bar and its menu
  button until a reload (section 3c, from Tony's screenshots). Any card
  that is turned, not only the turn card. Needs testing on Tony's
  phone; the stand-in has no Safari bars.
- **A phone first opened sideways gets the tablet layout**, with the
  Desktop and Mobile tabs, although it now lists only what a phone
  lists (section 3c). Named on L-286 on 2026-09-24, since the tabs move
  in that build.
- **On a card, the browser's back button does nothing useful.** Seen on
  the turn card (section 3c). The page opens every card by replacing the
  current address rather than adding one, which is the likely reason;
  not checked on a real phone. Named on L-286 on 2026-09-24: rooms with
  their own addresses are the natural place to take it.
- **The editor cannot link or unlink a card's twin.** Any other pair made
  before the linking existed needs a metadata patch, as this one did.
- **Nothing checks which cards each tab lists, or where the room buttons
  sit.** Both changes in this pass are checked only by Tony looking.
- **A patch that fingerprints a whole file the editor saves refuses on
  any save.** safe-file-editing already has this rule; its examples name
  the ledger's index and the protocol's skill table, not the gallery
  metadata. A candidate field note for that skill.
- **Files quoting a layout or a rule this pass changed** (The Correction
  Does Not Travel): the interactive-exhibit Nav cluster row and L-285's
  note (section 2), and the ledger's L-286 and L-287 text on the mode
  rule, which the tab ruling replaces. L-286's line is marked superseded
  by `patch_L286_2_ledger_rooms_ruling_20260924.py`; L-287's is not yet.

---

Record started September 2026 with Anthropic's Claude Opus 5.5, and
updated after cards 2 to 4, three times on 2026-09-23 during card 5,
twice for card 6, twice for card 7, once for card 8, and on 2026-09-24
for card 8's push and the Moon room (section 3i).

============================
**Tony**:

Card 1, after the push to 83a72d11: "both desktop and phone look right,
as expected. thanks! head is at 83a72d11523c417027d0a325bb0f2531256bd0b4"

Cards 2 and 3, the tab patch (second cut): your run output and what both
tabs show go here.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L303_tab_shows_its_own_shape_20260922.py
  ok  index.html: header Updated stamp
  ok  index.html: the note above treeRank points at the new rule
  ok  index.html: inCurrentMode() lists the tab's own shape
  ok  index.html: renderNavList's note matches
note: gallery/gallery_metadata.json is CRLF here; compared normalised, written back
      CRLF exactly as found.
  ok  metadata: the 16:9 animation card names its 9:16 twin
  ok  metadata: the 9:16 animation card names its 16:9 twin
  ok  encoding gate: inserted text is ASCII, and neither file
      holds a non-ASCII byte.
  ok  metadata parses, and the two cards name each other
  wrote index.html (162633 bytes)
  wrote gallery/gallery_metadata.json (81063 bytes) [CRLF, as found]

patch applied to 2 file(s)

Stamps updated: the 'Updated' line at the top of index.html.
gallery_metadata.json's 'last_updated' is the editor's to set and
is left alone; no card was added, removed or moved.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before. None of them
     reads the card lists, so a pass does not speak for this
     change; your eyes in step 5 do.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.9s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.5s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       9.3s  PASS (201 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.2s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 58 link(s) compared, store
                                    7fb7a1b666d4.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery dcc36e38,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.1s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 sibling(s), none stale,
                                    and nothing in data/ the builder
                                    did not make. The sweep is keeping
                                    up.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 sibling(s), none stale, and
  last swap 2026-09-22T23:33:39.924967+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly three
     files: index.html, gallery/gallery_metadata.json, and this
     script under documentation/. Commit and push.

gallery moved to 2a80a68c6db57414757d372f424b77162bf4b2db
orrery moved to cb254b0163317509a82a647e5b0bfdc54c171d6c

  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.4s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at dcc36e38

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at dcc36e38, byte for byte

  orrery HEAD cb254b01
  examining 29 of 87 links; the other 58 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  29 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could not be examined.

  PASS Store drift               0.8s  29 pointers against orrery
                                    cb254b01 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery cb254b01 --
  last swap 2026-09-22T23:33:39.924967+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. Open https://palomasorrery.com/ on the desktop and look at
     both tabs. Desktop should list 104 exhibits and Mobile 104,
     where both said 145 before; the welcome line carries the
     count. (These numbers were worked out just now from your
     metadata, so a card you edit later can change them.)
-- correct. although it is noted that the front page is not yet divided into desktop and mobile. that happens only when opening one of the three doors. 
-- this points to a gap in the front page. the guest book is under construction. 

     The Featured strip should show 5 cards on Desktop and 5 on
     Mobile. -- correct
     
     Inner Solar System Animation should appear once in
     each, the 16:9 view on Desktop and the 9:16 on Mobile. -- correct
     
     On the phone the 16:9 animation card should now be gone --
     that is the other half of this patch -- and nothing else
     there should have changed. -- correct

  6. Tell Claude the new gallery SHA and what you saw: 1a12cadedf49fcc959a67ceb52fcb7916741d5c8
  -- in addition to the checks, i deleted the static inner solar system visualization.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

====================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L303_phone_setting_and_turn_card_20260922.py
  ok  index.html: header Updated stamp
  ok  index.html: style for the turn-the-phone card
  ok  index.html: the phone leaves out a card set to none
  ok  index.html: turnWanted() beside sweepWanted()
  ok  index.html: the loader holds a 3D landscape figure on an upright phone
  ok  index.html: rotation redraws when the answer changes
  ok  editor: docstring stamp
  ok  editor: the shape values
  ok  editor: a helper that reads whether a card's landscape figure is 3D
  ok  editor: the phone setting in the card form
  ok  editor: saving maps the two 16:9 choices to one value
  ok  converter: docstring stamp
  ok  converter: a re-export keeps shape none
  ok  sweep report: the rule list
  ok  sweep report: docstring stamp
  ok  sweep report: shape none is its own class
  ok  sweep report: the 3D class names what the phone does
  ok  sweep report: the class order
  ok  encoding gate: inserted text is ASCII, and no file holds
      a non-ASCII byte.
  ok  the three Python files compile after the edit
  wrote index.html (167803 bytes)
  wrote tools/gallery_editor.py (55703 bytes)
  wrote tools/json_converter.py (36327 bytes)
  wrote tools/sweep_report.py (7282 bytes)

patch applied to 4 file(s)

Stamps updated: the 'Updated' line at the top of index.html and the
'Module updated' line in each of the three tools.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- run and stored 9/23/26
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before. None of them
     opens a card on a phone, so a pass does not speak for this
     change; your eyes in step 7 do.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.5s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.3s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      13.9s  PASS (201 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        4.2s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 58 link(s) compared, store
                                    7fb7a1b666d4.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery 751aff3f,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.2s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.3s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.3s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 sibling(s), none stale,
                                    and nothing in data/ the builder
                                    did not make. The sweep is keeping
                                    up.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 sibling(s), none stale, and
  last swap 2026-09-23T13:09:46.835195+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly five
     files: index.html, the three tools, and this script under
     documentation/. Commit and push.
-- One Drive sync paused     
-- gallery moved to 4c20194a69f6cb57ff19a33ffa2f64a320fd8a41
-- orrery moved to ac25d4f44a0607f734fdf98f21095e869abe790b

  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       2.0s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 751aff3f

  PASS Export freshness          0.2s  the served export is the orrery's
                                    at 751aff3f, byte for byte

  orrery HEAD ac25d4f4
  examining 29 of 87 links; the other 58 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  29 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could not be examined.

  PASS Store drift               0.8s  29 pointers against orrery
                                    ac25d4f4 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery ac25d4f4 --
  last swap 2026-09-23T13:09:46.835195+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. Open the gallery editor (tools/gallery_editor.py, Run) and click
     the Mercury card. 'Shape (phone only)' should show four
     choices, with '16:9 3D' picked and '16:9 2D' greyed out.
-- correct. None selected.

  6. Pick 'none', Save All, then commit and push
     gallery/gallery_metadata.json.
-- e823e7383915b00f29aefd54f0cfbaed7bb4cedb

  7. On the phone, held upright:
       - Orbital Mechanics should no longer list the Mercury card. -- not quite. on the phone held upright, it says, "Turn your phone to landscape to view this card." On desktop both tabs show the same landscape view; this is okay. on the phone when i turn the phone to landscape, the figure is drawn sized to fit, but it does not look good. i need to edit it specifically for the phone. so the None radio button is functioning as the 16:9 3D button. please review. 
       -- another issue. on the phone when i turn the phone upright again, the view goes back to the "turn your phone...." card, however, from there there is no way back to the gallery front page. the < button at the bottom does not work and there is no hamburger menu at the top left. what i have to do is press the refresh arrow then the hamburger displays
       - Open Trappist1 Exoplanet System. It should show its title
         and 'Turn your phone to landscape to view this card.'
         Turn the phone: the figure is drawn. Turn it back: the
         card returns.
         -- i have not reviewed this card yet, but it suffers from the same issues as the orbital transformation card. it is not suited for the phone and i will removed it. 
       - A 2D card should sweep sideways as before, and a 9:16 card
         should look as before.
         -- for a 2D landscape sweep i looked at the earth science keeling curve. that works correctly.
         -- for the 9:16 card i looked at the featured planetary boundaries card. that works correctly. it should be noted that the other (not featured) planetary boundaries 2D card that requires a sweep does not look right.
     On the desktop, both tabs should look as before, Mercury
     included. -- correct
  8. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 8 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

=================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L303_turn_card_way_back_20260923.py
  ok  index.html: header Updated stamp
  ok  index.html: style for the turn card's way back
  ok  index.html: a phone held sideways at load still counts as a phone
  ok  index.html: the turn card gets its own way back, and scrolls to the top
  ok  encoding gate: index.html is ASCII after the edit
  wrote index.html (169983 bytes)

patch applied to 1 file -- 9/23/26

Stamps updated: the 'Updated' line at the top of index.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before. None of them
     opens a card on a phone; your eyes in step 5 do.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.2s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      10.7s  PASS (201 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.3s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 58 link(s) compared, store
                                    7fb7a1b666d4.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery ac25d4f4,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.8s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-09-23T13:09:46.835195+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly two
     files: index.html and this script under documentation/.
     Commit and push. -- 2e0fa8f5de7ec1dc99597dc302e4e4c4eb745e72

  4. After the push, check what the live site serves:
         python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 11 files from https://palomasorrery.com/
    SERVED   interactive.html                               matches the working copy
    SERVED   gallery/feature_renderers.js                   matches the working copy
    SERVED   gallery/earth_geometry.js                      matches the working copy
    SERVED   gallery/assembler/resolver.py                  matches the working copy
    SERVED   gallery/assembler/__init__.py                  matches the working copy
    SERVED   data/solar-system/coverage_index.json          matches (the working copy is CRLF)
    SERVED   data/solar-system/feature_configs.json         matches (the working copy is CRLF)
    SERVED   data/solar-system/positions/voyager_1.json     matches the working copy
    SERVED   gallery/arrival.js                             matches the working copy
    SERVED   gallery/nav_cluster.js                         matches the working copy
    SERVED   data/objects_config.json                       matches the working copy

  PASS Served reachability       1.6s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at ac25d4f4

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at ac25d4f4, byte for byte

  orrery HEAD ac25d4f4
  examining 29 of 87 links; the other 58 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Earth']            not a top-level constant in the store
                  /objects/1/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  29 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 5 could not be examined.

  PASS Store drift               0.6s  29 pointers against orrery
                                    ac25d4f4 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery ac25d4f4 --
  last swap 2026-09-23T13:09:46.835195+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. On the phone, wait about ten minutes after the push (the site
     can serve the old files that long), then RELOAD the page -- wait, i thought that a hard refresh (swipe up to remove the app from the running apps on the phone) was enough? 
     held upright:
       - Orbital Mechanics should not list the Mercury card. -- correct. not listed on the phone. 
       - Open Trappist1 while it is still 16:9. The turn card
         should now have a 'Back to the gallery' button. Turn
         the phone, turn it back, and press the button: you
         should land in the lobby. Note whether the menu button
         at the top left is there this time. -- if i just use phone gestures: portrait to landscape back to portrait, no. if i refresh in portrait, the menu button comes back.
       - Reload the page with the phone held SIDEWAYS: Mercury
         should still not be listed. -- interesting. with the phone held sideways, the menu looks like the desktop menu, with both tabs available. however, even if i select the "desktop" tab in this view, the mercury orbital mechanics card is not listed. 

  6. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L303_editor_twin_phone_note_20260924.py
  ok  editor: docstring stamp
  ok  editor: a 16:9 card with a 9:16 twin says the phone shows the twin
  ok  editor: saving a card that gives way to its twin keeps its stored shape
  ok  encoding gate: the editor is ASCII after the edit
  ok  the editor compiles after the edit
  wrote tools/gallery_editor.py (58017 bytes)

patch applied to 1 file

Stamps updated: the 'Module updated' line in the editor.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- done
  2. Open the gallery editor (tools/gallery_editor.py, Run).
     Click the 16:9 Apophis Closest Approach card. Under 'Shape
     (phone only)' all four choices should be greyed out, and the
     note should say the phone shows its 9:16 twin instead.
     Click the 9:16 Apophis card: its choices should work as
     before. Close the editor without saving. -- correct
  3. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.1s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      10.8s  PASS (201 checks, 0 failures)
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        2.9s  All 245 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 246 store-editor checks
                                    passed: every box the form offers
                                    is one the writer allows; the word
                                    list and the tick list differ by
                                    the belts, on purpose; nothing
                                    typed saves nothing; the save
                                    message does not promise a visitor
                                    sees what they cannot yet; and a
                                    red Cache in step is explained
                                    rather than just shown.
  PASS Config mirror check       0.1s  Every served link holds the
                                    export's value, unit and figure
                                    count; 58 link(s) compared, store
                                    6d4bb4fd4f54.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery fb8d927e,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.7s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: 1 directory in data/ the
                                    builder did not make: solar-system
                                    (1). Check whether they belong
                                    there; the newer .gitignore rules
                                    keep the known conflict-copy
                                    shapes out of git but do not
                                    remove anything.

======================================================================
  15 of 15 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: 1 directory in data/ the builder
  last swap 2026-09-24T18:01:35.153393+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  4. In GitHub Desktop the change list should show exactly two
     files: tools/gallery_editor.py and this script under
     documentation/. Commit and push. -- 9c61fb216544ee92c581086789958949b941d859
  5. Tell Claude the new gallery SHA and what the editor showed.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 5 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L286_2_ledger_rooms_ruling_20260924.py
ok  LEDGER_CONSOLIDATED.md  5 edit(s): L-286 note and Gap, L-286 mode line marked, L-283 note

DO THESE, IN THIS ORDER:
  1. Run the orrery maintenance run. Its 'Ledger index' generator rewrites the index tables for L-286 and L-283.

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260924T174742Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.9s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             1.1s  unchanged (1 checked, not written)
  Module atlas                 5.8s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               4.5s  rewrote DATA_INVENTORY.md
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.2s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.6s  No figure count exceeds its inputs: 39
                                     derived row(s) read, 26 judged OK -- 26 OK,
                                     13 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       0.9s  Export matches the store: sha256
                                     6d4bb4fd4f54 on both sides; 81 rows re-read,
                                     54 not exported, 26 tokens.
  Dimensions                   1.0s  No unit contradicts its arithmetic: 39
                                     derived row(s) read -- 26 OK, 10 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.1s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.1s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 83 status lines in constants_new.py are
                                     well formed; 49 rows carry none.
  Row shape                    0.1s  All 135 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.2s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          17.8s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.8s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            8.4s  76 of 114 routed, 8 clean
  Worksheet checker tests     15.5s  All 136 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         19.4s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner           9.3s  295 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  17 of 17 gating checkers passed -- 89.5s total
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          295 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1961 file(s) examined, 8 written, 0 created, 0 removed, 4 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   WORKSHEET_CHECK.md
    written   data/provenance_history.json
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

  2. Move this script into documentation/. -- done
  3. Move the new run record into documentation/, replacing RUN_RECORD_gallery_card_pass_20260922.md there. -- done
  4. Commit and push. -- c6cbacaeae5ca3d3e0d2cc5aa20842222aa472e3
Undo before committing is Discard Changes in GitHub Desktop. 
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 