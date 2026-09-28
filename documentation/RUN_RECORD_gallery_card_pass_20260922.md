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

**Built: the rooms and the header, one patch.**
`patch_L286_3_rooms_and_header_20260924.py`, built on gallery `a2f84a0`,
`index.html` only. The rooms and the header went together, not as two
patches as first planned: the tabs lived in the side menu, and a room
screen with no header would have left no way back up from a card but the
browser's Back. Each room is its own screen at any depth, the header
carries the chain and, on the desktop, the tabs, a card's buttons sit in
the header, the side menu is hidden, and rooms and cards have their own
addresses so Back from a card returns to its room. Tested headless as a
desktop, a phone and a phone held sideways before delivery.

Tony ran it, both maintenance runs passed (16 of 16 offline, 2 of 2
live), and he pushed it with the L-322 gallery work at gallery
`2e164816`. The live `index.html` is byte-identical to the tested file.
Tony's look on the phone and the desktop, 2026-09-24: "looks great."

Two small things from the commit: the script sits at the gallery repo
root rather than in `documentation/`; and the empty file named `python`
that appeared before the run was discarded, not committed.

**Tony's ruling on the mark, 2026-09-24, replacing his earlier one.**
"perhaps we should add the Gemini credit to the i info card, 'Created by
Tony Quintanilla with Claude (Anthropic). Logo created with Gemini
(Google).' and leave the logo without a mark. the reason is that the
naive visitor may read the Gemini mark as a general credit, which it is
not." L-283's note of the same day, which keeps the mark, is superseded
by this; see section 5.

**Built: the look.** `patch_L283_1_dusk_wall_20260924.py`, built on
gallery `2e164816`: `index.html` and a new `palomas_orrery_wall.jpg`,
Tony's original cropped from 1024 to 920 pixels square from the top left
to take off the corner with the mark (97 KB). The lobby and the rooms
stand on the dusk wall with the art at 60 and 35 percent, as in the
mockup, and the About card carries Tony's credit line. One departure
from the mockup, stated in the patch: behind an open card the wall stays
black with no art, where the mockup had the art at 15 percent, because
the figures' colors were chosen against black and L-283's rule is that
the chrome loses when it competes with a trace. Tested headless as a
desktop and a phone.

Tony ran it, both maintenance runs passed (16 of 16 offline, 2 of 2
live), and he pushed at gallery `199b8d9f`; the live `index.html` and
`palomas_orrery_wall.jpg` are byte-identical to the tested files. His
look on the phone, 2026-09-24: the lobby "beautiful", a room "okay", an
open card on black "correct", the About credit "correct", and a
question: "is this sufficent credit in general?"

**The credit question, and a gap it found.** Google made the visible mark
optional in August 2026 (Settings > Media Watermark in Gemini), keeping
its invisible SynthID watermark and C2PA Content Credentials for
transparency. Checked on 2026-09-25: Tony's original PNG carries both
kinds of machine-readable label -- a C2PA manifest (a `caBX` chunk) and
an XMP packet giving the digital source type as "composite with trained
algorithmic media" and the credit "Edited with Google AI", dated
2025-11-28. The served `palomas_orrery_wall.jpg` carries neither: saving
the crop as a JPEG dropped all metadata. SynthID sits in the pixels and
is built to survive cropping and compression, but that was not checked.
The C2PA manifest cannot simply be copied across, because its signature
binds it to the original's bytes. The XMP label can.

Tony, 2026-09-25, on the label's wording: "this was not edited. this was
an original Gemini image. there was no other original." Then: "Gemini
created the original image but i asked for modifications. so the one we
are using is not version 1, maybe version 3 or 4." So every version was
made in Gemini, and the one in use is Gemini's edit of its own earlier
output. Google's label, "Edited with Google AI", fits that, and so does
the About card's "Logo created with Gemini (Google)".

**Built: the label put back.** `patch_L283_2_wall_art_label_20260925.py`,
built on gallery `199b8d9f`, `palomas_orrery_wall.jpg` only. It reads
Google's XMP block from `Gemini_palomas_orrery_logo.png` in the repo and
places it, unchanged, in the JPEG after the JFIF header: credit "Edited
with Google AI", digital source type composite with trained algorithmic
media, created 2025-11-28 05:51:15 UTC. The decoded picture is identical;
the file grows from 96,687 to 97,516 bytes. Google's signed Content
Credentials are not carried across, since cropping breaks their
signature; the original PNG keeps them.

Tony ran it on 2026-09-25 (his output is at the end of the orrery's
`RUN_RECORD_gallery_tap_lag_20260925.md`, the other conversation's
record): offline 16 of 16, live 2 of 2, pushed at gallery `1a816f24`
(commit titled "L238_2"), and the lobby looks exactly as before on the
phone. The served JPEG is byte-identical to the tested file.

**Built: the chain in the exhibit rooms.**
`patch_L286_4_exhibit_chain_20260925.py`, built on gallery `a21680ab`:
`interactive.html` and one line of `index.html`. The exhibit's top bar
reads "Paloma's Orrery | Solar : Earth" with the room's title under it,
read from `gallery_config.json` and the card whose live link opens the
room; a link steps back in history when it names the gallery screen the
visitor came from, which `index.html` records in sessionStorage when it
opens a live card. Tested headless as a phone and a desktop; the
maintenance run passed 16 of 16 on the patched copy.

Tony ran it, offline 16 of 16 and live 2 of 2, pushed at gallery
`42a17abe`; both pages are byte-identical to the tested files. His look,
2026-09-26: phone "all correct", desktop "correct". The script was filed
in the orrery's `documentation/` (committed at orrery `9f3b5afb`) rather
than the gallery's, which is why the gallery's change list never showed
it; it moves to the gallery's `documentation/` with the next commits.

**L-286 is built**: rooms at any depth, the header and its chain, the
tabs in the header, the side menu retired, room addresses and Back, and
the chain in the exhibit rooms. The ledger patch at the end of this pass
closes it, with L-283's look.

**Found on the way: the exhibit's grid numbers are hard to read on the
desktop.** Tony, 2026-09-26: "the grid tic labels are too small and
faint to read in desktop. in the phone the grid labels are off screen.
this was the original reason for the triad and grid label. however, on
desktop the grid tic labels are visible, but indistinct. zooming has no
effect on grid tic labels." Not caused by this pass: `buildSunLayout()`
has set them to 9 px in #5a5a6a on the scene's #060a12 since gallery
`3b97153` (2026-08-29). The frame zoom changes the axes' range, not the
numbers' size, so zooming cannot help.

Tony's screenshot of the Sun on the desktop, 2026-09-25, shows it. His
ruling, 2026-09-26, "Confirmed as recommended": everywhere but a
portrait phone, 12 px in the page's secondary grey #9a9a9a; the portrait
phone unchanged.

**Built: the grid numbers.** `patch_L289_grid_numbers_desktop_20260926.py`,
built on gallery `42a17abe`, `interactive.html` only. One function,
`axisTickFont()`, beside the page's own phone test `sunPhonePortrait()`,
serves the Explorer's axes and the exhibit rooms'; a room re-reads it
when the window turns. Tested on a copy as a desktop, a portrait phone
and a sideways phone, by calling the two layout builders and the turn
handler directly; the full rooms could not be drawn in the sandbox,
whose network cannot reach the CDN their Python runtime loads from. The
maintenance run passed 16 of 16 on the patched copy.

Tony ran it and pushed; the nightly run of 2026-09-26 (gallery
`d8bd18e2`) carries it, and the served `interactive.html` is the tested
file. His look on the desktop: "looks good. only detail is that we
should add the units, AU in this case."

**Built: the unit on the numbers.** `patch_L289_grid_numbers_unit_20260926.py`,
built on gallery `d8bd18e2`, `interactive.html` only. Every axis number
in the Explorer and the exhibit rooms ends in " AU" and is written out
in full (`exponentformat: none`), because Plotly's shorthand would have
read "50u AU" in Earth's frame and "200k AU" at the Oort cloud's edge;
checked with Plotly's own formatting from 0.0001 AU to 200,000 AU.
Tested as before; 16 of 16.

Tony ran it and pushed at gallery `c6000f0`; the served
`interactive.html` is the tested file. He sent two screenshots of Earth
on his phone, upright and sideways, with the unit showing on every
number, and ruled: "I think we should add the larger numbers to the
upright phone view also because this is relevant too." The upright
screenshot shows the numbers along the left and bottom edges, so the
comment in `axisTickFont()` saying they fall off screen on a portrait
phone was wrong.

**Built: the upright phone too.** `patch_L289_grid_numbers_phone_20260926.py`,
built on gallery `93d8ae9`, `interactive.html` only: `axisTickFont()`
returns 12 px #9a9a9a on every screen, and its comment is corrected.
Tested as before; 16 of 16. Waiting for Tony's run and his look, in
particular at the bottom-left corner of the upright view, where two
edges' labels meet and were already crowded at 9 px.

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
  And L-283's note of 2026-09-24, which says the art keeps Gemini's mark:
  Tony's later ruling the same day moves the credit to the About card
  and takes the mark off (section 3i).

---

Record started September 2026 with Anthropic's Claude Opus 5.5, and
updated after cards 2 to 4, three times on 2026-09-23 during card 5,
twice for card 6, twice for card 7, once for card 8, and twice on
2026-09-24, for card 8's push and the Moon room, for the rooms patch,
and for the mark ruling and the look patch, and on 2026-09-25 for the
look's result, the credit question and the label (section 3i).

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

========================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L286_3_rooms_and_header_20260924.py
  ok  the page's Updated stamp
  ok  styles for the header and the room screens; the side menu hidden
  ok  the header element, first in the page
  ok  room records and the room on show
  ok  the tree walk records each room
  ok  the tabs and a card's buttons move into the header; a phone shows no tabs
  ok  a door opens its screen; the lobby sets the header
  ok  setHeader, openCard, leaveCard, showRoom, renderRoom
  ok  an open card shows its room and title in the header
  ok  switching tabs redraws the room on show
  ok  room addresses, and Back to the lobby
  ok  goHome shares its clean-up with showRoom
  ok  the turn card goes back to its room
  ok  the links list opens under its button
  ok  encoding gate: index.html is ASCII after the edit
  ok  the result is the file that was tested
  wrote index.html (195190 bytes)

patch applied to 1 file

Stamps updated: the 'Updated' line at the top of index.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run.-- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before. None of them
     opens the gallery page; your eyes in step 5 do.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.9s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       9.3s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
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
                                    link(s) against orrery 7a44f6a3,
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
  PASS Arrival                   0.1s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.1s  === PASS: 55 hover(s) and 267
                                    number(s) examined; 12 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.1s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-25T02:58:37.226714+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show exactly two
     files: index.html and this script under documentation/.
     Commit and push. -- 2e1648169f621e5c5624f02ed71edaea13a33734
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

  PASS Served reachability       1.7s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 7a44f6a3

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 7a44f6a3, byte for byte

  orrery HEAD 7a44f6a3
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
                                    7a44f6a3 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery 7a44f6a3 --
  last swap 2026-09-25T02:58:37.226714+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. On the phone, wait about ten minutes after the push, close the
     page and open it again, then:
       - The header shows Paloma's Orrery and no tabs.
       - Tap Solar System: its own screen, with Earth among the
         rooms and the empty planets greyed.
       - Tap Earth, then The Moon: the six Moon cards, and the
         header reads Solar : Earth : Moon.
       - Open a Moon card: its title and Share sit under the chain.
         Swipe back (or the browser's Back): the Moon room again.
       - Tap Earth in the header, then Paloma's Orrery.
     On the desktop: the Desktop and Mobile tabs sit at the top
     right of the lobby and every room; switching tabs redraws the
     room; a card's Share and other buttons sit in the header. -- looks great. 
  6. Tell Claude the new gallery SHA and what you saw. -- 2e1648169f621e5c5624f02ed71edaea13a33734

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L283_1_dusk_wall_20260924.py
  ok  the page's Updated stamp
  ok  the old faint art in the lobby is retired
  ok  the dusk wall, the art, and the tints
  ok  the body starts as the lobby
  ok  setHeader marks the screen
  ok  the About card credits the logo
  ok  encoding gate: index.html is ASCII after the edit
  ok  the result is the file that was tested
  wrote palomas_orrery_wall.jpg (96687 bytes)
  wrote index.html (197877 bytes)

patch applied to 2 files

Stamps updated: the 'Updated' line at the top of index.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. Move
     patch_L286_3_rooms_and_header_20260924.py there too; it was
     committed at the repo root. -- done

  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect every gating checker to pass, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.9s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     3.2s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite       9.2s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
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
                                    link(s) against orrery 62e93856,
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
  PASS Display figures           0.1s  === PASS: 56 hover(s) and 270
                                    number(s) examined; 13 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.1s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-25T18:42:47.090627+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show index.html,
     palomas_orrery_wall.jpg (new), this script under
     documentation/, and the rooms script moving into
     documentation/. Commit and push. -- 199b8d9fc9de65154e23c47f33e16641f7ff1047
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

  PASS Served reachability       5.5s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 62e93856

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 62e93856, byte for byte

  orrery HEAD 62e93856
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

  PASS Store drift               1.6s  29 pointers against orrery
                                    62e93856 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery 62e93856 --
  last swap 2026-09-25T18:42:47.090627+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. On the phone, wait about ten minutes after the push, close the
     page and open it again, then:
       - The lobby stands on the dusk sky with the moon and birds. -- beautiful
       - A room shows them fainter. -- okay
       - An open card is on black, as before. -- correct
       - The i button in the lobby: the credit names Gemini. -- correct. (is this sufficent credit in general?)
     The same on the desktop.
  6. Tell Claude the new gallery SHA and what you saw. -- 199b8d9fc9de65154e23c47f33e16641f7ff1047

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L286_4_exhibit_chain_20260925.py
  ok  interactive.html: the page's Updated stamp
  ok  interactive.html: styles for the chain in the top bar
  ok  interactive.html: the phone's title size follows the new line
  ok  interactive.html: the top bar's markup
  ok  interactive.html: the chain replaces the Gallery link's code
  ok  interactive.html is the file that was tested, and ASCII
  ok  index.html: the page's Updated stamp
  ok  index.html: a live card records where it was opened from
  ok  index.html is the file that was tested, and ASCII
  wrote interactive.html (157249 bytes)
  wrote index.html (198324 bytes)

patch applied to 2 files

Stamps updated: the 'Updated' lines at the top of interactive.html
and index.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into documentation/. It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 16 of 16 gating checkers to pass, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.0s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.6s  rewrote
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.6s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 42 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing.
  PASS Store writer suite        3.1s  All 245 store-writer checks
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
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 87
                                    link(s) against orrery 4bab8c04,
                                    24 fallback named; read check: 41
                                    of 41 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 34 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.2s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 56 hover(s) and 270
                                    number(s) examined; 13 graded, 4
                                    graded by line, 43 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-26T01:21:27.979604+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show index.html,
     interactive.html and this script under documentation/, plus
     whatever the maintenance run rewrites as usual. Commit and push.

-- gallery moved to 42a17abe16eebe5f03c790ad2a8f39f918c1ba7b
-- orrery moved to 9f3b5afbbb79aab7af081957dc20abd9262933d2

  1. After the push: python gallery_maintenance_run.py --live

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

  PASS Served reachability       2.2s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 4bab8c04

  PASS Export freshness          0.2s  the served export is the orrery's
                                    at 4bab8c04, byte for byte

  orrery HEAD 9f3b5afb
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

  PASS Store drift               1.0s  29 pointers against orrery
                                    9f3b5afb -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 5 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            29 pointers against orrery 9f3b5afb --
  last swap 2026-09-26T01:21:27.979604+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. On the phone, after about ten minutes, close the page and
     open it again, then:
       - Open the Earth room and its Earth and Moon card. The top
         bar reads Paloma's Orrery | Solar : Earth, with Earth
         under it.
       - Tap Earth in that bar: you are back in the Earth room.
         Swipe back: you should NOT land on the exhibit again.
       - Open the Sun from its room and tap Solar: the Solar
         System screen.
       - Check the room still works as before: the drawer, the
         i panel, a marker tap.
         -- all correct.
     The same on the desktop. -- correct
  6. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

-- one new issue detected. the grid tic labels are too small and faint to read in desktop. in the phone the grid labels are off screen. this was the original reason for the triad and grid label. however, on desktop the grid tic labels are visible, but indistinct. zooming has no effect on grid tic labels. 

===========================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L289_grid_numbers_phone_20260926.py
  ok  interactive.html: the page's Updated stamp
  ok  interactive.html: every screen gets the larger numbers
  ok  interactive.html is the file that was tested, and ASCII
  wrote interactive.html (159947 bytes)

patch applied to 1 file

Stamps updated: the 'Updated' line at the top of interactive.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into the GALLERY's documentation/ folder
     (not the orrery's). It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 16 of 16 gating checkers to pass, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              0.8s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.7s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      10.0s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        3.9s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery e21d9dd9,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
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
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop, in the gallery, the change list should show
     interactive.html and this script under documentation/, plus
     whatever the maintenance run rewrites as usual. Commit and push. -- correct
-- gallery moved to a5c35f5fcde47b3648040a5aec8724d58416d2d4

  4. After the push: python gallery_maintenance_run.py --live

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

  PASS Served reachability       1.8s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at e21d9dd9

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at e21d9dd9, byte for byte

  orrery HEAD 907436a8
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.9s  28 pointers against orrery
                                    907436a8 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery 907436a8 --
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. On the phone held upright, after about ten minutes, close the
     page and open it again, then open Earth: the numbers along the
     left and bottom edges are larger and lighter, as they are
     sideways. Look at the bottom-left corner, where the labels of
     two edges meet and were already crowded. -- correct
     
  6. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 6 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_solar_system_room_half1_20260926.py
  ok  interactive.html: the page's Updated stamp
  ok  interactive.html: the Solar System room: its constants, driver, source line and panel copy
  ok  interactive.html: the room's row in the EXHIBITS table
  ok  interactive.html: a room's own inputs to its driver, in the boot path
  ok  interactive.html: a room can name the marker a text box belongs to
  ok  interactive.html: the info panel says 'body' in this room
  ok  interactive.html: the info panel shows a source when there is no link
  ok  interactive.html is the file that was tested, and ASCII
  wrote interactive.html (168308 bytes)

patch applied to 1 file

Stamps updated: the 'Updated' line at the top of interactive.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into the GALLERY's documentation/ folder
     (not the orrery's). It has run. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 16 of 16 gating checkers to pass, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.3s  no change to MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.9s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.3s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        4.3s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery 907436a8,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.9s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop, in the gallery, the change list should show
     interactive.html and this script under documentation/, plus
     whatever the maintenance run rewrites as usual. Commit and push.-- 8545cbd7d34b98f1de5ff93615c5da5e3e5b75c3
  4. After the push: python gallery_maintenance_run.py --live

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

  PASS Served reachability       1.5s  all 11 files served and
                                    byte-identical to the working copy

  orrery export pinned at 907436a8

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 907436a8, byte for byte

  orrery HEAD 907436a8
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               1.0s  28 pointers against orrery
                                    907436a8 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery 907436a8 --
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. After about ten minutes, on your phone, open
         palomasorrery.com/interactive.html?exhibit=solar-system
     and go through the Mode 5 list Claude gave you.

Now a headless run of the patched copy, with Pyodide and Plotly served locally.Now the patch script itself, built from those seven anchored edits.The patch for the new room is ready. It's built on gallery `a5c35f5f`, which is still the current commit. Run it from the gallery folder with VS Code's Run button, and it will print its own next steps.

**What it does:** it adds the room at `interactive.html?exhibit=solar-system`, titled "The Solar System." The room shows the Sun, Earth, Jupiter, Saturn and Apophis on their orbits, where they are today, with no shells. Nothing under `data/` changes, so it reaches the site on the push alone, with no cache rebuild. The Explorer is untouched.

**A correction.** I told you the room would show 25 percent beyond the largest orbit. That's the rule for the static assembler scenes, not the rooms. The rooms open at 10 percent beyond the largest thing drawn, and this room follows that rule, so it opens at about 11 AU around Saturn's orbit.

**One fix beyond the plan.** When you tap a body's name, a text box opens. At first the box described an arbitrary point on the orbit, not the body. For Earth it read 0.98 AU when Earth today is at 1.003 AU. I pointed the box at the body itself. That touched a small piece of the shared page, and I confirmed the Sun and Earth rooms come out identical before and after.

**What was tested.** I loaded the room headless as a desktop and as an upright phone, with no errors. The gallery maintenance run on a patched copy passed 16 of 16. None of those checkers opens the new room, though, so that result only says nothing else broke. The Explorer couldn't be run here at all, so it needs your phone.

**What to look at on your phone:**
- **The opening view.** Saturn's orbit fills the view, and Earth and Apophis sit crowded near the Sun. That's expected at this scale.
- **The drawer.** It shows five rows: Earth, Jupiter, Saturn, Apophis, Sun. Tap Earth's name; its box should say about 1.00 AU.
- **The title inside the scene.** On an upright phone, "Paloma's Orrery — The Solar System" runs under the arrow buttons and reads "The Solar Sys…". Tell me if you want it shorter.
- **The info panel's words.** Read them, since visitors will. Each body says "No link on file for this body," because bodies have no links in the config yet. Adding links is config work, which puts it in Half 2.
- **The other rooms.** Check that the Explorer, the Sun and Earth look as they did.

  6. Open the Explorer (the gallery's Explorer card) and the Sun and
     Earth rooms, and confirm each looks as it did.
  7. Tell Claude the new gallery SHA and what you saw. -- correct. 8545cbd7d34b98f1de5ff93615c5da5e3e5b75c3
  -- ledger update for this work? 

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 7 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

===============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_2_studio_lists_quoted_room_keys_20260926.py
  ok  tools/json_converter.py: the module's update stamp
  ok  tools/json_converter.py: live_scene_urls() reads a quoted room key
  ok  tools/json_converter.py is the file that was tested, and ASCII
  wrote tools/json_converter.py (36827 bytes)

patch applied to 1 file

Stamps updated: the 'Module updated' line in tools/json_converter.py.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into the GALLERY's documentation/ folder. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 16 of 16, as before. None of them reads Studio's list.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.3s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.9s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.7s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        4.1s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery 907436a8,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.9s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. Open Gallery Studio. Click New Interactive Card... (the purple
     button). The scene list now includes
         interactive.html?exhibit=solar-system
     Pick it, give the title and placard, and create. The card
     lands in Storage. 
  4. In the gallery editor: File > Reload from disk FIRST (an open
     editor does not see Studio's write, and its Save All would
     write over it). Then place the card in its room.
  5. Commit and push. Tell Claude the new gallery SHA. -- 3f7f50ab0dcc53bc989983913644be28621e9acd

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 5 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

==============================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_3_date_line_and_editor_save_check_20260926.py
  ok  interactive.html: the page's Updated stamp
  ok  interactive.html: the date line, worked out from the epoch the driver returns
  ok  interactive.html: the room's panel words: 'where it is now'
  ok  interactive.html: the panel's note: 'where it sits now'
  ok  interactive.html: the room asks for the current minute
  ok  interactive.html: the room's compose returns the date line
  ok  interactive.html: where the title sits: clear of the arrow cross on an upright phone
  ok  interactive.html: the title carries the date line
  ok  interactive.html: the boot path asks for the current minute when a room says so
  ok  interactive.html: the boot path keeps the room's date line
  ok  interactive.html: the title stays clear of the cross when the phone turns
  ok  interactive.html is the file that was tested, and ASCII
  ok  tools/gallery_editor.py: the module's update stamp
  ok  tools/gallery_editor.py: hashlib is imported; disk_fingerprint() reads what a file is now
  ok  tools/gallery_editor.py: the load records what both files were, and names the file
  ok  tools/gallery_editor.py: Save All refuses a file that changed on disk since it was loaded
  ok  tools/gallery_editor.py: after a save, the record moves to what was written
  ok  tools/gallery_editor.py is the file that was tested, and ASCII
  wrote interactive.html (172822 bytes)
  wrote tools/gallery_editor.py (60411 bytes)

patch applied to 2 files

Stamps updated: the 'Updated' line at the top of interactive.html,
and the 'Module updated' line in tools/gallery_editor.py.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into the GALLERY's documentation/ folder. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 16 of 16, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.5s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      15.5s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.3s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        5.6s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery 907436a8,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.3s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.3s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Artifact 1 assembler      0.3s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  16 of 16 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  3. In GitHub Desktop the change list should show interactive.html,
     tools/gallery_editor.py and this script, plus what the run
     rewrites as usual. Commit and push. -- 74624c0c085b3f42b4bbf028a5a603c626ee5bd9
  4. After the push: python gallery_maintenance_run.py --live

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

  orrery export pinned at 907436a8

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 907436a8, byte for byte

  orrery HEAD 907436a8
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.9s  28 pointers against orrery
                                    907436a8 -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery 907436a8 --
  last swap 2026-09-26T21:30:02.295547+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. After about ten minutes, open the Solar System room on your
     phone, upright and then sideways, and on the desktop. The date
     line should sit right under the title, clear of every button,
     and give the current minute in UTC. -- correct.
  6. Open the gallery editor: its status bar should end with the
     path of the gallery_metadata.json it opened.
  7. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 7 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

==================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L281_1_guestbook_lobby.py
ok   created gallery/guestbook.js (8620 bytes)
ok   created data/guestbook.json (736 bytes)
ok   created documentation/smoke_guestbook.js (8787 bytes)
ok   index.html: header stamp
ok   index.html: script tag
ok   index.html: guest book styles
ok   index.html: guest book section
ok   index.html: fill call
ok   index.html: fill function
     index.html written (201996 bytes)
ok   gallery_maintenance_run.py: header stamp
ok   gallery_maintenance_run.py: guest book checker
ok   gallery_maintenance_run.py: served files
     gallery_maintenance_run.py written (52407 bytes)
stamps updated: index.html header, gallery_maintenance_run.py docstring
patch applied

NEXT: run gallery_maintenance_run.py. It should show a new row,
'Guest book', passing. Then look at the lobby before you push:
the dashboard's Serve Gallery Locally, then open the lobby.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.6s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.1s  rewrote data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.1s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        3.7s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery 0e3d05fd,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.3s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.3s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 7 checks
                                    passed
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  17 of 17 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L363_4_date_line_every_room_20260927.py
  ok  interactive.html: the page's Updated stamp
  ok  interactive.html: the Sun room's note
  ok  interactive.html: the Earth room's note
  ok  interactive.html: the short line, shared by every room, and the Sun room's no-date line
  ok  interactive.html: the Solar System room's note and a body's source line
  ok  interactive.html: the Sun room shows its no-date line
  ok  interactive.html: the Earth room draws now, and shows the line
  ok  interactive.html: the Solar System room uses the shared line
  ok  interactive.html: the title stays at the top unless it would touch a button
  ok  interactive.html: the title starts at the top
  ok  interactive.html: after drawing, the title is fitted
  ok  interactive.html: the title is fitted again when the phone turns
  ok  interactive.html is the file that was tested, and ASCII
  wrote interactive.html (175976 bytes)

patch applied to 1 file

Stamps updated: the 'Updated' line at the top of interactive.html.

WHAT TO DO NEXT, in this order:

  1. Move THIS script into the GALLERY's documentation/ folder. -- done
  2. Run the gallery maintenance run:
         python gallery_maintenance_run.py
     Expect 16 of 16, as before.

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.2s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     0.6s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      10.8s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        3.9s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    a2d6b97d161e.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery 0e3d05fd,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         0.1s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.1s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.1s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 7 checks
                                    passed
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  17 of 17 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

-- OneDrive sync suspended for nightly run.

  3. Commit and push. -- 70a77347cf65a14789707bf741cf203d29739c79
  4. Then: python gallery_maintenance_run.py --live

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
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
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       1.8s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at 0e3d05fd

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at 0e3d05fd, byte for byte

  orrery HEAD 0e3d05fd
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.9s  28 pointers against orrery
                                    0e3d05fd -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery 0e3d05fd --
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

  5. After about ten minutes, on your phone, upright, open all three
     rooms: the Sun, Earth, and the Solar System. For each, note
     whether the title and its line sit at the top or below the
     arrow buttons, and read the line and the note in the i panel.
  6. Tell Claude the new gallery SHA and what you saw.

TONY-ACTION ROLLUP for this patch:
  (do)     steps 1 to 5 above.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

==================================================================================

**What it adds:**
- **A guest book in the lobby.** Under a "Guest book" heading, where "Under construction" was, the lobby lists entries newest first. After five entries, the older ones sit behind a "Show all" line. Your replies appear indented under the entry they answer.
- **A note for visitors.** Until the Google Form exists, the note says the guest book opens for visitors soon and that every message is read before it appears. Once the form's address goes into the entries file, the note becomes a "Sign the guest book" link.
- **Links only where you write them.** Links are drawn only on your own entries and replies, and only to pages of this gallery. A visitor's message is always plain text.
- **A new check in the maintenance run, called "Guest book".** It confirms the entries file is complete and in order, and it tests the safety rules. It starts by feeding the checks a deliberately broken version, to prove they can fail. -- please add this to the dashboard also.

**What I tested:**
- The patch applied cleanly to a copy of the repo, both as it is on GitHub and in the Windows line-ending form your working copy may have. A second run refuses, as it should.
- The new check passed.
- I loaded the patched page in a headless browser, one that runs without a screen. The guest book appeared under Featured. Clicking "Start with Earth" opened the Earth room, and returning to the lobby redrew the guest book. -- correct

**What I couldn't test** is how it looks. That's yours to judge.

The sample entry's wording is mine, placed there so you'd have something to look at. You can change it in data/guestbook.json before you push. Later, the updater will write your entries for you. -- okay

After running the patch, run Gallery Maintenance Run -- offline, which should show the new "Guest book" row passing. Then open the lobby through Serve Gallery Locally, on your desktop and your phone. What do you see? -- correct as described. 

===========================================================================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L281_2_guestbook_updater.py
ok   created tools/guestbook_updater.py (18843 bytes)
ok   created tools/test_guestbook_updater.py (10865 bytes)
ok   gallery_maintenance_run.py: header stamp
ok   gallery_maintenance_run.py: updater checker
     gallery_maintenance_run.py written (53003 bytes)
ok   .gitignore: guest book local file
     .gitignore written (1678 bytes, CRLF kept)
stamps updated: gallery_maintenance_run.py docstring
patch applied

NEXT: run gallery_maintenance_run.py. It should show a new row,
'Guest book updater', passing. 

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.4s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.3s  rewrote
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      14.7s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.3s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        5.5s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    eafacc8cec4b.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery e0a0c7cc,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.4s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 7 checks
                                    passed
  PASS Guest book updater        0.3s  === GUEST BOOK UPDATER: all 29
                                    checks passed (3 scripted runs,
                                    self-test first)
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  18 of 18 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

Then commit and push. -- 9b787f99f78fbde9f09f896804fd4cb8fee3e3f1

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
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
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       3.2s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at e0a0c7cc

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at e0a0c7cc, byte for byte

  orrery HEAD e0a0c7cc
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               1.5s  28 pointers against orrery
                                    e0a0c7cc -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery e0a0c7cc --
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

**Step 2, attached, is the guest book updater.** It's built on 70a77347. Save it in the gallery repo's top folder and click Run, as before. It creates two files and edits two:

- **tools/guestbook_updater.py**, the tool itself. It fetches the form's submissions and shows each new one. You answer a to approve, d to decline, l to decide later, or q to stop. After approving, it offers to let you reply right away. Then it gives a small menu:
  - write an entry of your own;
  - reply under any entry;
  - remove an entry;
  - set the form's address, which turns on the lobby's "Sign the guest book" link.

  It ends by telling you whether the guest book changed and needs a commit. I added the remove option myself. Approving before publishing covers new messages, but you also need a way to take down something already published.
- **tools/test_guestbook_updater.py**, its check. It runs the tool three times in a temporary folder, with scripted answers and made-up submissions in place of Google.
- **.gitignore** keeps the tool's private file off the public repo. That file holds the sheet's address and a list of messages you've already decided on. The list keeps only a short fingerprint of each message, not its words, so a declined message isn't saved anywhere.
- **gallery_maintenance_run.py** gets a new row, "Guest book updater".

**Links are typed simply.** For your entries and replies, you type a room (solar_system/earth), a card's id, or a live exhibit (earth, sun). The tool checks each against the gallery's own list of 172 pages. A misspelling is refused, and the tool asks you again.

**What I tested:**
- The check passes all 29 of its tests.
- A guest book written by the updater also passes the page's own "Guest book" check, and it displays newest first.
- A first run with nothing set up asks for the sheet's address. If you skip it, it finishes without changing anything.

**Next**, I'll give you the steps to create the Google Form and its sheet. That's the one part only you can do, since it lives in your Google account. After that come the Daily Run and the dashboard patch.

For now: run the patch, then Gallery Maintenance Run -- offline, which should show "Guest book updater" passing. Then commit and push, and tell me the new gallery SHA.

=========================================================================================

1
Create the form
Go to forms.google.com and choose Blank form. Title it "Paloma's Orrery guest book". For the description, a suggestion you can change: "Leave a note about the gallery. Every message is read before it appears, and messages that appear in the lobby are public."
2
Add the two questions
First question: "Your name", type Short answer, Required on. Second: "Your message", type Paragraph, Required on. Keep the words "name" and "message" in the titles, because the updater finds the columns by those words. Delete any other question.
3
Turn off email collection
In the Settings tab, under Responses, set Collect email addresses to "Do not collect". Leave "Limit to 1 response" off, because it makes visitors sign in to Google.
4
Link the form to a sheet
In the Responses tab, click Link to Sheets and choose Create a new spreadsheet. Every submission will now arrive there as a row.
5
Publish the sheet as CSV
In that sheet: File, Share, Publish to web. Choose the "Form Responses 1" sheet (not Entire document) and "Comma-separated values (.csv)", then Publish. Copy the address it gives. Keep it private: don't paste it into chat, email or anywhere public.
6
Publish the form
Back in the form, click Publish at the top right, then Manage, and set responders to "Anyone with the link". Publish again. Then click the link icon, tick Shorten URL, and copy the responder link (it starts with forms.gle).
7
Send yourself a test
Open the responder link in a private browser window and submit a test message. Google can take a few minutes to update the published CSV, so wait about five minutes before the next step.
8
Run the updater
Open tools/guestbook_updater.py in VS Code and click Run. Paste the sheet address when it asks. It should show your test message: answer d to decline it. Then choose f and paste the forms.gle link, then q. Commit data/guestbook.json and push.

After you push, the lobby's note should change to a "Sign the guest book" link that opens your form.

While you do this, I'll build the Daily Run and the dashboard patch. It will add the Daily Run group with the updater, the cache builder and the maintenance checks under it, plus the "Guest book" check you asked for.

Tell me what the updater printed when it showed your test message, and the new gallery SHA.

==============================================

Here's step 5, then the email column, then one thing I need to change on my side.

**Step 5, in the sheet you have open:**

1. Click **File** in the menu bar (top left, under the title).
2. Point to **Share**, then click **Publish to web**.
3. A box opens with two drop-down menus side by side. In the first, which says "Entire Document", choose **Form Responses 1**. In the second, which says "Web page", choose **Comma-separated values (.csv)**.
4. Click **Publish**. When Google asks if you're sure, click **OK**.
5. A long address appears in the box. Copy it and keep it somewhere private until the updater asks for it. Leave "Automatically republish when changes are made" ticked, so new submissions reach the address on their own.


**The email column is a question on the form, not the email setting.** The setting you turned off only stops Google from recording each visitor's account email by itself. "Your Email Address" is a separate question that asks visitors to type theirs, and that setting doesn't touch it. To remove it, open the form, click that question, and click the trash-can icon. The empty column will stay in the sheet, which is harmless because nothing will fill it or read it.

**Please don't run the updater until I've changed it (step 8).** Your form differs from what I built for in one way that matters. The message question is titled "Leave a note about the gallery", and the updater looks for a column with "message" in its title. Finding none, it would fall back to the third column, which is the email column. It would then show you email addresses as if they were messages. I'll change the updater to recognize "note" as well, and put that in the Daily Run patch.

Your two extra questions, the rating and the favorite exhibit, are a nice addition. My plan: the updater shows you both when you review a message, but never publishes them. They stay private to you in the sheet. If you'd rather have either one show in the lobby, tell me.

For now, do step 5 and delete the email question from the form.

======================================================================

That message is expected. It came from the sheet, and Google doesn't let you delete a column that's linked to a form. Hiding it there is fine. But the question itself lives in the form, which is a separate page, and that's where it has to be deleted.

1. Switch to the other Google tab, the one titled "Paloma's Orrery Guest Book" with the purple form icon.
2. Make sure you're on the **Questions** tab at the top of the form.
3. Click the "Your Email Address" question so its box is highlighted.
4. At the bottom of that box, click the **trash can** icon.

Google saves the change on its own. If the button at the top right changes from "Published" to something asking you to publish again, click it.

If you also meant to drop the favorite-exhibit question when you hid column E, delete it from the form the same way.

After that, nothing new will go into the hidden columns, and they can stay hidden in the sheet. Tell me when the email question is gone from the form.

==============================================================================

Now the updater change for your form's column names, and the Daily Run itself.Now the Daily Run itself.Gallery half tested. Now the dashboard and ledger patch for the orrery repo.Good, the form now asks only for a name, a rating and a note. The Daily Run is built as two patches, one for each repo.

**Patch 3, for the gallery repo** (built on 9b787f99):
- **daily_run.py** runs the three steps in order. First the guest book updater. Then it asks you to pause OneDrive and press Enter, or type s to skip the build that day, and runs the cache builder. Then the offline maintenance run. If one step has a problem, the next still runs. It ends with a summary of each step and what's left for you: commit and push, the live check, and resuming OneDrive. It opens by saying when the last cache build was, so a missed day shows.
- **The updater now reads your form correctly.** It takes the message from the column whose heading contains "note" or "message", and it will never guess a column by position. The rating is shown to you beside each message and never published.
- **A new maintenance-run check, "Daily run steps"**, fails if any of the Daily Run's three scripts goes missing, say after a rename.

**Patch 4, for the orrery repo** (built on e0a0c7cc):
- **A new "Daily Run" group on the dashboard**, above the gallery groups. Its main button runs the whole Daily Run. Indented under it are the Guest Book Updater, the Gallery Cache Builder (moved here from the gallery group, description unchanged) and the offline maintenance run.
- **The "Guest Book Checks" button you asked for**, among the gallery checkers.
- **The offline maintenance run's description** now names everything it runs. It said "six Node suites" when there are eight.
- **L-281 in the ledger, rewritten as built.** Cusdis's shutdown, your design, the four patches, and what's left. The old Cusdis text is kept and marked as replaced.

**What I tested:**
- I drove the Daily Run through a real terminal, with the builder made to fail on purpose. The maintenance run still ran, and the summary named the builder as the problem.
- I also ran it skipping the build. Both guest book checks pass.
- I opened the dashboard on a virtual screen, and every button in both groups found its script.
- The orrery maintenance run gives the same results with and without patch 4, with one catch. The patch script itself counts as one extra finding for the provenance scanner while it sits in the repo's top folder. Once it's moved into documentation/, the count is back to normal.

**Order:**
1. Gallery: run patch 3, then Gallery Maintenance Run -- offline. Move the patch into documentation/, then commit and push.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L281_3_daily_run.py
ok   created daily_run.py (7297 bytes)
ok   created documentation/run_guestbook_checks.py (2638 bytes)
ok   replaced tools/guestbook_updater.py (20746 bytes)
ok   replaced tools/test_guestbook_updater.py (12942 bytes)
ok   gallery_maintenance_run.py: header stamp
ok   gallery_maintenance_run.py: daily run checker
     gallery_maintenance_run.py written (53408 bytes)
stamps: gallery_maintenance_run.py docstring; the new and replaced
files carry their own
patch applied

NEXT: run gallery_maintenance_run.py. New row 'Daily run steps'
should pass, and 'Guest book updater' should say 34 checks.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

======================================================================
  gallery maintenance run -- OFFLINE (before a commit)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

GENERATORS -- rewritten every time; a no-op when nothing moved
  PASS Module atlas              1.5s  rewrote MODULE_ATLAS.md,
                                    MODULE_INDEX.md
  PASS Constants export pull     1.0s  no change to
                                    data/constants_export.json,
                                    data/constants_export.sha
  PASS Config mirror             0.1s  no change to
                                    data/objects_config.json

CHECKERS -- the verdict informs the push call
  PASS Cache builder suite      12.8s  PASS (210 checks, 0 failures)
  PASS Pole of date              0.2s  POLE OF DATE: all 11 checks passed
                                    (frame angle, orrery, ERFA, block
                                    checker, and each shown able to
                                    fail).
  PASS Mirror suite              0.1s  All 51 mirror checks passed:
                                    served, spelling, relabel refused
                                    and accepted, conflict refused,
                                    definition as exactly 1, fallback
                                    and absent named, no-slot refused,
                                    five shapes, formatting kept,
                                    idempotent, report writes nothing,
                                    uncertainty written as served,
                                    Earth's pole served.
  PASS Store writer suite        4.3s  All 251 store-writer checks
                                    passed: an allow list that lets
                                    through only a shell's words, a
                                    belt's words and the arrival
                                    settings; a no-edit round trip;
                                    one line per change; empty words
                                    handled; a refused batch writing
                                    nothing; awkward text; and the
                                    shell list matching the cache
                                    check's rule.
  PASS Store editor suite        0.1s  All 252 store-editor checks
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
                                    count; 65 link(s) compared, store
                                    eafacc8cec4b.
  PASS Pointer join              0.1s  Every link is accounted for: 93
                                    link(s) against orrery e0a0c7cc,
                                    24 fallback named; read check: 43
                                    of 43 measured rows reached carry
                                    a read.
  PASS Cache in step             0.1s  The served cache holds the
                                    config's features exactly: 4
                                    object(s), 35 named shell(s), in
                                    both cache files.
  PASS Feature renderers         1.0s  === ALL CHECKS PASSED ===
  PASS Page framing              0.1s  === ALL CHECKS PASSED ===
  PASS Sun shells                0.2s  ALL CHECKS PASSED
  PASS Earth scene geometry      0.2s  === ALL CHECKS PASSED ===
  PASS Hover budget              0.2s  === ALL CHECKS PASSED ===
  PASS Arrival                   0.2s  Arrival: both rooms open on the
                                    right things; every shell trace
                                    carries its key; the fallback with
                                    no arrival block is unchanged.
  PASS Display figures           0.2s  === PASS: 57 hover(s) and 288
                                    number(s) examined; 13 graded, 5
                                    graded by line, 44 held to the
                                    fixture ===
  PASS Guest book                0.1s  === GUEST BOOK: all 7 checks
                                    passed
  PASS Guest book updater        0.3s  === GUEST BOOK UPDATER: all 34
                                    checks passed (3 scripted runs,
                                    self-test first)
  PASS Daily run steps           0.1s  === DAILY RUN: all 3 step scripts
                                    found
  PASS Artifact 1 assembler      0.2s  === ALL CHECKS PASSED -- 5
                                    verdicts and T3's feature set
                                    match the 2026-08-31 pin ===
  PASS Cache siblings            0.1s  RESULT: no sibling directories and
                                    nothing in data/ the builder did
                                    not make.

======================================================================
  19 of 19 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Cache siblings         RESULT: no sibling directories and
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  After you push: python gallery_maintenance_run.py --live

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

-- gallery moved to 38cb8b41c1016714b4923022fccadfbe8d7e8497

======================================================================
  gallery maintenance run -- LIVE (after a push)
  root: C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io   (found beside this script)
======================================================================

LIVE -- what the deployed site actually serves

  fetching 13 files from https://palomasorrery.com/
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
    SERVED   gallery/guestbook.js                           matches the working copy
    SERVED   data/guestbook.json                            matches the working copy

  PASS Served reachability       2.1s  all 13 files served and
                                    byte-identical to the working copy

  orrery export pinned at e0a0c7cc

  PASS Export freshness          0.1s  the served export is the orrery's
                                    at e0a0c7cc, byte for byte

  orrery HEAD e0a0c7cc
  examining 28 of 93 links; the other 65 are served from the export
    NOT IN STORE  create_sun_galactic_tide default not a top-level constant in the store
                  /objects/0/features/oort_cloud/galactic_tide/typical_radius
    NOT IN STORE  planet_poles['Sun']              not a top-level constant in the store
                  /objects/0/features/orientation
    NOT IN STORE  planet_poles['Jupiter']          not a top-level constant in the store
                  /objects/2/features/orientation/pole
    NOT IN STORE  planet_poles['Saturn']           not a top-level constant in the store
                  /objects/3/features/orientation/pole
  28 pointers: 24 match, 0 DRIFT, 0 UNIT MISMATCH, 4 could not be examined.

  PASS Store drift               0.7s  28 pointers against orrery
                                    e0a0c7cc -- 24 match, 0 DRIFT, 0
                                    UNIT MISMATCH, 4 could not be
                                    examined.

======================================================================
  2 of 2 gating checkers passed
  1 report-only -- these do not gate, whatever they exit with:
    PASS Store drift            28 pointers against orrery e0a0c7cc --
  last swap 2026-09-27T13:55:01.594465+00:00: succeeded first time
======================================================================

  Offline pass: python gallery_maintenance_run.py

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

2. Orrery: run patch 4, and move it into documentation/ **before** the orrery maintenance run. The maintenance run also rebuilds the ledger's index. Then commit and push.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/palomas_orrery_for_github/patch_L281_4_dashboard_and_ledger.py
ok   palomas_orrery_dashboard.py: change note
ok   palomas_orrery_dashboard.py: Daily Run group; builder moved into it
ok   palomas_orrery_dashboard.py: offline runner description
ok   palomas_orrery_dashboard.py: Guest Book Checks
ok   palomas_orrery_dashboard.py: section symbol
     palomas_orrery_dashboard.py written (91327 bytes)
ok   LEDGER_CONSOLIDATED.md: header stamp
ok   LEDGER_CONSOLIDATED.md: L-281 metadata
ok   LEDGER_CONSOLIDATED.md: L-281 Cusdis decision superseded
ok   LEDGER_CONSOLIDATED.md: L-281 as built
     LEDGER_CONSOLIDATED.md written (1304552 bytes)
stamps updated: dashboard docstring change note, ledger header
patch applied

NEXT: run the orrery maintenance run -- it regenerates the ledger
index from the new L-281 block -- then commit and push.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github> 

======================================================================
MAINTENANCE RUN -- generators, then checkers (L-188)
======================================================================
  Provenance scan is current (last run 20260927T192707Z, 1 day(s) ago).

GENERATORS -- regenerate every time; a no-op when nothing moved
----------------------------------------------------------------------
  Ledger index                 0.9s  rewrote LEDGER_CONSOLIDATED.md
  Skill manifest               0.1s  unchanged (1 of 1 rewritten, content
                                     identical)
  Constants export             0.6s  unchanged (1 checked, not written)
  Module atlas                 6.9s  rewrote MODULE_ATLAS.md, MODULE_INDEX.md
  Data inventory               5.5s  rewrote DATA_INVENTORY.md
  Exact rows report            1.7s  unchanged (1 checked, not written) -- 7 of
                                     20 exact rows printed at 18 lines (8 orrery,
                                     10 gallery); 4 drawn only, 0 not followed, 0
                                     map entries broken
  Document index               0.1s  unchanged (1 checked, not written)

CHECKERS -- verdict informs the push call
----------------------------------------------------------------------
  Constants change             0.2s  No changes to constants_new.py since HEAD.
  Constants relations          0.3s  21 of 21 provenance tests passed against
                                     constants_new.py. No constants have drifted.
  Derived figures              0.9s  No figure count exceeds its inputs: 41
                                     derived row(s) read, 28 judged OK -- 28 OK,
                                     13 NOT YET MIGRATED, 1 NO DERIVED LINE.
  Constants export check       1.3s  Export matches the store: sha256
                                     eafacc8cec4b on both sides; 85 rows re-read,
                                     54 not exported, 26 tokens.
  Exact rows by the count      1.4s  FAILED (exit 1) -- FAILING -- 0 row(s)
                                     with...
  Dimensions                   1.1s  No unit contradicts its arithmetic: 41
                                     derived row(s) read -- 28 OK, 10 NO UNIT, 3
                                     NOT CHECKABLE.
  Cross-check annotations      0.2s  19 of 19 cross-check annotation tests
                                     passed.
  Citation inheritance         0.2s  20 of 20 citation-inheritance tests passed.
  Status lines                 0.1s  All 87 status lines in constants_new.py are
                                     well formed; 49 rows carry none.
  Row shape                    0.1s  All 139 row shapes in constants_new.py fit
                                     the assignment's own line.
  Scanner recognition 1d/1e    0.3s  27 of 27 recognition pins hold: real
                                     citations recognized, fake ones refused.
  Reset completeness          21.3s  PASS -- all 309 IntVars + 3 StringVars + 10
                                     entries reset to startup defaults; date set
                                     to now.
  Orbit cache                  1.8s  All 6 orbit cache tests passed: cache loads,
                                     old formats convert, corrupted entries are
                                     dropped.
  Earth pole of date           0.3s  all 14 checks passed (geometry, ERFA,
                                     fallback, cache, hover, transform).
  Worksheet checker            9.4s  76 of 114 routed, 8 clean
  Worksheet checker tests     16.5s  All 136 checks passed
  Worksheet key round trip     0.9s  RESULT: 52 sites minted 52 distinct keys,
                                     all resolved; 52 pinned keys still resolve;
                                     1 retired keys confirmed gone.
  Builder marker join         20.2s  All 76 checks passed
  Extractor pins               0.4s  RESULT: 29 string sites carry the pinned 73
                                     claims and 14 instruction drops, at LOOKBACK
                                     30 / LOOKAHEAD 25, extractor version 2.
  Provenance scanner          10.2s  295 TIER-1 FINDINGS IN THE SCANNED TREE

======================================================================
  1 of 20 checkers FAILED -- 102.9s total
  Exact rows by the count
  2 report-only, exit 0 whatever they find:
    Worksheet checker           76 of 114 routed, 8 clean
    Provenance scanner          295 TIER-1 FINDINGS IN THE SCANNED TREE
======================================================================

FILES WRITTEN THIS RUN
----------------------------------------------------------------------
  1989 file(s) examined, 8 written, 0 created, 0 removed, 5 rewritten identically
    written   DATA_INVENTORY.md
    written   LEDGER_CONSOLIDATED.md
    written   MODULE_ATLAS.md
    written   MODULE_INDEX.md
    written   PROVENANCE_AUDIT.md
    written   data/provenance_history.json
    written   documentation/RUN_RECORD_gallery_card_pass_20260922.md
    written   documentation/prompts/citation_review.jsonl
    rewritten with identical bytes, no action needed:
      PROJECT_INSTRUCTIONS.md
      WORKSHEET_CHECK.md
      data/worksheet_check_state.json
      data/worksheet_routed.json
      test_output/test_orbit_paths.json
    20 file(s) over 2 MB compared by size and mtime only

----------------------------------------------------------------------
Exact rows by the count -- FAILED (exit 1) -- FAILING -- 0 row(s) with...
----------------------------------------------------------------------
EXACT ROWS PRINTED: 7 of 20 exact rows printed at 18 lines (8 orrery, 10 gallery); 4 drawn only, 0 not followed, 0 map entries broken
  FAIL EARTH_LEO_UPPER_ALTITUDE_KM: gallery gallery/feature_renderers.js line 2022, served prints None, the row states 4
  FAIL EARTH_LEO_LOWER_ALTITUDE_KM: gallery gallery/feature_renderers.js line 2022, served prints None, the row states 3
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1130, served prints None, the row states 2
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1137, served prints None, the row states 2
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1140, served prints None, the row states 2
  FAIL EARTH_VAN_ALLEN_OUTER_RADII: gallery gallery/feature_renderers.js line 1143, served prints None, the row states 2
  FAIL EARTH_SOLAR_WIND_PRESSURE_NPA: gallery gallery/feature_renderers.js line 2278, served prints None, the row states 1
  FAIL EARTH_SOLAR_WIND_PRESSURE_NPA: gallery gallery/feature_renderers.js line 2489, served prints None, the row states 1
  FAIL EARTH_SOLAR_WIND_BZ_NT: gallery gallery/feature_renderers.js line 2277, served prints None, the row states 1
  FAIL EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG: gallery gallery/feature_renderers.js line 2280, served prints None, the row states 3
  FAIL EARTH_BOW_SHOCK_CUT_ANGLE_DEG: gallery gallery/feature_renderers.js line 2491, served prints None, the row states 3
EXACT ROWS BY THE COUNT: FAILING -- 0 row(s) with no count, 0 orrery print(s) by a width, 11 gallery print(s) not served the count

C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github>

orrery moved to b81137e0d28cc0a6853786c9ff41bde8f4cabc19

3. Then finish the form at step 5, and try the Daily Run from its new button for the first run of the updater.

Tell me both new SHAs when they're pushed.

====================================================

Both pushes landed: the gallery is at 38cb8b41 and the orrery at b81137e0. Your orrery run's one failure, "Exact rows by the count", isn't from these patches. It's waiting on the Stage D gallery work that's still open. The provenance count stayed at 295, so patch 4 added nothing.

Now, publishing. There are two different "publishes", and the purple button in your screenshot is the second one:

- **Step 5 publishes the sheet**, so the updater can read the submissions. It isn't done in the form. It's done in the other tab, the green spreadsheet one.
- **Step 6 publishes the form**, so visitors can fill it in. That's the purple Publish button you're looking at.

Since you're on the form, do step 6 first:

1. Click **Publish** (top right).
2. In the box that opens, click **Manage** and set responders to **Anyone with the link**. Click **Done**, then **Publish**. The button changes to "Published".
3. Click the **link icon** (the chain, left of the person-with-plus icon). Tick **Shorten URL**, then **Copy**. Save that forms.gle link. It's the public one for the lobby, so it's fine to share.

https://forms.gle/Wi95M97iXcWjQDSU8

Then switch to the green spreadsheet tab for step 5: -- already done; see above. 

1. **File**, then **Share**, then **Publish to web**.
2. First drop-down: **Form Responses 1**. Second drop-down: **Comma-separated values (.csv)**.
3. Click **Publish**, then **OK**.
4. Copy the long address it shows. Keep that one private. It goes only into the updater, when the updater asks for it.

5. A long address appears in the box. Copy it and keep it somewhere private until the updater asks for it. Leave "Automatically republish when changes are made" ticked, so new submissions reach the address on their own.


Your form's description reads well. It tells visitors their message is reviewed for the public lobby, which covers what they need to know.

Once both are published, send yourself a test message through the forms.gle link, wait about five minutes, and run the Daily Run.

===============================================


======================================================================
  guest book updater -- C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io
======================================================================
1 entry in the guest book; 172 gallery pages a link may point at.

No link to the form's responses yet. In the Google Sheet the form
writes to: File > Share > Publish to web, choose the responses
sheet and Comma-separated values (.csv), click Publish, and copy
the address it gives. Paste it here, or press Enter to skip
visitor messages this time.

Saved in tools\guestbook_local.json (kept off the public repo).

Fetching the form's responses...
1 new message. The oldest has waited 0 days.

-- 1 of 1 -- Tony, 9/27/2026 22:51:18
   This is a test of the Paloma's Orrery Guest Book.
   (private, not published) Overall Gallery Experience Rating: 5
a approve, d decline, l later, q stop > a
   Approved.
   Reply to it now? y/n > y
   Type your reply. Press Enter on an empty line to finish.
   > Successful!
   >
   Links (optional). Type a room such as solar_system/earth, a
   card's id, or a live exhibit such as earth or sun. Press Enter
   on an empty line when done.
   link > solar_system/earth
   label [Earth] >
   added: Earth -> #room=solar_system/earth
   link >
   Reply added.

w write an entry, r reply, x remove an entry, f form address, q finish > q

======================================================================
  approved 1, declined 0, waiting 0; the guest book now has 2 entries
  CHANGED: commit data/guestbook.json in GitHub Desktop and push.
======================================================================

C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io>

==============================================================================

Your message isn't live yet because data/guestbook.json hasn't been pushed. The updater saved your approval and reply on your computer, but GitHub still has the file with only the welcome entry, and the gallery is still at 38cb8b41.

But first, something more urgent: the private sheet address is now public. You pasted it into the run record, the maintenance run copies the run record into the orrery's documentation folder, and your last orrery push put it on GitHub. I checked, and it's there at b81137e0. Anyone who finds that address can read every submission, approved or not. Today that's only your test, but it's the address every future message would pass through.

**To close it:**
1. In the green sheet: **File**, **Share**, **Publish to web**. Open "Published content and settings" and click **Stop publishing**. The old address stops working.
2. Click **Publish** again with the same choices (Form Responses 1, CSV), and compare the new address with the old one. I'm not certain Google gives a new one. If it gives back the same address, stop publishing again right away and tell me, and we'll move the form to a fresh sheet instead.
3. Open **tools/guestbook_local.json** in VS Code. Replace the old address between the quotes after "csv_url" with the new one, and save. That file never leaves your computer. Don't paste the new address anywhere else, including the run record.
4. Delete the old address from your run record, so the next orrery push doesn't carry it again. It will stay in GitHub's history, but once publishing is stopped it leads nowhere.

**Then, to see your message live:** run the Guest Book Updater once more. Choose f and paste https://forms.gle/Wi95M97iXcWjQDSU8, then q. That turns on the "Sign the guest book" link in the same push. Commit data/guestbook.json and push. The lobby updates a minute or two after the push. If it doesn't, reload the page.

Start with the leak. When you've stopped and republished, does the new address differ from the old one?

================================================================

The same address means it's live again, so first: go back to the sheet and **stop publishing right away**. The fix is to give the form a brand-new sheet, which gets its own address.**1. Stop publishing the old sheet.** File, Share, Publish to web, then Stop publishing. Leave it that way for good.

**2. Give the form a new sheet.** In the form's Responses tab, click the three-dot menu next to the green Sheets icon, select Unlink form, and click Unlink to confirm. Nothing is lost: the existing spreadsheet remains in your Google Drive, but it will no longer receive new submissions. Then click **Link to Sheets** again and choose **Create a new spreadsheet**. The form pushes all its earlier responses into the new file, so your test message will be there too.

https://docs.google.com/spreadsheets/d/1lkhbkvSBHJ4UBV1kIccz1Mlq0Zc4FReVx8gS-dEPaNM/edit?resourcekey=&gid=2117585803#gid=2117585803

**3. Publish the new sheet.** In the new sheet: File, Share, Publish to web, "Form Responses 1", CSV, Publish. Because it's a different file, it gets a different address. Check that it doesn't start the same way as the old one. Don't paste it anywhere yet.

**4. Run the attached patch** in the gallery repo, then Gallery Maintenance Run -- offline. "Guest book updater" should now report 39 checks.

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L281_5_sheet_address.py
ok   replaced tools/guestbook_updater.py (22478 bytes)
ok   replaced tools/test_guestbook_updater.py (14240 bytes)
stamps: both files carry a September 28 line
patch applied

NEXT: run gallery_maintenance_run.py -- 'Guest book updater'
should say 39 checks. Then the updater, s, and the new address.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 

**5. Give the updater the new address.** Run the Guest Book Updater and, at the menu, choose **s** and paste the new address. It saves the address and fetches from it right away. Your test message won't come back for approval, because the updater recognizes it as already decided. While you're in the menu, choose **f** and paste the forms.gle link too. Then choose **q**.


https://forms.gle/JD6iLZRoZd5UHmJA9

**6. Commit and push the gallery.** That carries your approved test message, your reply and the "Sign the guest book" link to the lobby.

IThe same address means it's live again, so first: go back to the sheet and **stop publishing right away**. The fix is to give the form a brand-new sheet, which gets its own address.**1. Stop publishing the old sheet.** File, Share, Publish to web, then Stop publishing. Leave it that way for good.

**2. Give the form a new sheet.** In the form's Responses tab, click the three-dot menu next to the green Sheets icon, select Unlink form, and click Unlink to confirm. Nothing is lost: the existing spreadsheet remains in your Google Drive, but it will no longer receive new submissions. Then click **Link to Sheets** again and choose **Create a new spreadsheet**. The form pushes all its earlier responses into the new file, so your test message will be there too.

**3. Publish the new sheet.** In the new sheet: File, Share, Publish to web, "Form Responses 1", CSV, Publish. Because it's a different file, it gets a different address. Check that it doesn't start the same way as the old one. Don't paste it anywhere yet.

**4. Run the attached patch** in the gallery repo, then Gallery Maintenance Run -- offline. "Guest book updater" should now report 39 checks.

**5. Give the updater the new address.** Run the Guest Book Updater and, at the menu, choose **s** and paste the new address. It saves the address and fetches from it right away. Your test message won't come back for approval, because the updater recognizes it as already decided. While you're in the menu, choose **f** and paste the forms.gle link too. Then choose **q**.

**6. Commit and push the gallery.** That carries your approved test message, your reply and the "Sign the guest book" link to the lobby.

If you'd like, you can move the old sheet to the trash in Google Drive afterward. Once it's unpublished it's harmless either way.

When the push is done, tell me the new gallery SHA and I'll check the live lobby.f you'd like, you can move the old sheet to the trash in Google Drive afterward. Once it's unpublished it's harmless either way.

When the push is done, tell me the new gallery SHA and I'll check the live lobby.

====================================

PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> & C:\Users\tonyq\AppData\Local\Programs\Python\Python313\python.exe c:/Users/tonyq/OneDrive/Desktop/python_work/tonyquintanilla.github.io/patch_L281_6_guestbook_white_text.py
ok   index.html: header stamp
ok   index.html: guest book text styles
ok   index.html: guest book message text
ok   index.html: reply name
     index.html written (202462 bytes)
stamps updated: index.html header
patch applied

NEXT: Gallery Maintenance Run -- offline, commit and push, then look
at the lobby on the desktop and the phone.
PS C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io> 



