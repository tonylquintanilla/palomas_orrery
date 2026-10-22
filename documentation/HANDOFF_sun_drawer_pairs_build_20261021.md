<!-- Doc-Kind: hand | Closing handoff of the drawer order and Sun pairs build (L-460, L-191, L-466): what was built and checked, the run order, the open items, and where the next session starts. -->
# Handoff: the drawer order, the Sun's fourteen pairs, and where drawings end

Built on 645558e280ed900fea1433092e821d90cf740fcc at https://github.com/tonylquintanilla/palomas_orrery
(branch main) and 90cefa57bcb611eea4009e8f4bb5bb09f6012f18 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch
main). This close patch is pushed at the orrery commit that follows
645558e2.

Tony's local folders:
- orrery: `C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`
- website: `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`

Written October 21, 2026 with Anthropic's Claude Opus 5.5, from the
brief `HANDOFF_sun_drawer_pairs_build_brief_20261021.md`. The session
started at orrery 8228622 and website b334077. Your rulings are quoted
from chat and from your run record
`WHERE_WE_ARE_10-21-26_1658_run_record.md`.

## 1. What was built, and how each was checked

**The drawer order (L-460).** Each room's drawer now lists its shells
where each begins: the nearest part of the feature as it is drawn from
its sourced rows. The website reads the order from the served rows when
the page opens (`gallery/drawer_order.js`), so a new shell takes its
place by itself. The Solar System room is unchanged.
- Checked: the gallery run's "Drawer order" row, which works the order
  out by its own arithmetic and goes red on two planted faults; a
  headless boot of the real page in both rooms, with a planted fault; the
  Solar System room compared before and after, identical.
- Pushed at website 72c3c403.

**The corona's base (L-460, from your look).** The corona's dots began
at the Sun's surface, under the chromosphere. Mann et al. (2023),
Sect. 2, the paper the dots follow, puts the base of the corona about
3,000 km above the photosphere. New rows `CORONA_BASE_HEIGHT_KM` and
`CORONA_BASE_KM`; the dots and the streamer belt start there; the
corona's hover and panel say so, in the words you approved.
- Checked: the corona sampler's check now fails a dot at the surface,
  with that fault planted in its test; the nearest dot is 1.0043 solar
  radii; the drawer lists the chromosphere, then the corona.

**The Hills cloud's inner edge (L-466).** Its dots reached 257 AU,
inside its 2,000 AU inner edge, because they were spread evenly in time
along stretched orbits. They now go only on the part of each orbit past
the edge.
- Checked: a fourth check in the sampler, with a dot at 257 AU planted;
  5 of 5; nearest dot 2,000 AU; the disk's tilt still within its check.

**Every drawing's ends (L-466).** All 35 drawn features in the Sun and
Earth rooms were measured at both ends against their rows
(`DISCOVERY_drawn_ends_20261021.md`). A new gallery check, "Drawn ends",
holds every end to a row or to a named held end with its reason, and
prints the held ends every run. The rule is in provenance-discipline
2.33.

**One string per Sun shell (L-191).** Fourteen Sun shells each had a
tooltip string and a hover string. Each now has one, written with
newlines; the hover's line breaks are made from it where the plot is
drawn.
- Checked: the patch refuses unless the nine copies match letter for
  letter and every survivor matches the text you picked with only its
  line breaks changed; on the patched orrery, 14 of 14 tooltips read as
  their hovers, against 9 of 14 before; maintenance run 31 of 31.

## 2. The fourteen, and which words each kept

Nine were copies, letter for letter, and kept one: outer Oort cloud,
inner Oort cloud, inner limit of the Oort cloud, the heliopause (solar
wind), termination shock, chromosphere, photosphere, radiative zone,
core.

Five differed, and you chose each:
- Gravitational influence: the hover's words, without the scale line
  ("remove. this is a legacy aid to manual scaling using old typed
  distances").
- Roche limit: the tooltip's words.
- Alfven surface: the tooltip's words.
- Corona: the hover's words, then the panel's.
- Zodiacal dust cloud: the hover's words, then the panel's.

## 3. The drawer orders as they stand after the corona's fix

The Sun: Sun; Core; Radiative Zone; Photosphere; Chromosphere (1.003
solar radii); Corona (1.0043); Roche Limit (3.45, where it is drawn);
Zodiacal Dust Cloud (5.36, its nearest dot); Alfven Surface (19.7);
Termination Shock (94 AU); Heliopause (121 AU); Hills Cloud (2,000 AU);
Inner Limit of Oort Cloud (2,000 AU); Outer Oort Cloud clumps (10,000
AU); Galactic Plane (keeps its place); Galactic Tide (10,000 AU); Inner
Oort Cloud (20,000 AU); Outer Oort Cloud (100,000 AU); Gravitational
Influence (134,000 AU).

Earth: unchanged from the list you looked at, in
`DRAWER_ORDER_L460_20261021.md` on the website.

One reading is not what the rule means: the magnetotail is placed by its
width about its axis (30 Earth radii) rather than where it starts (30.6).
The order is the same. The fix rides the next website patch (L-460's
Gap).

## 4. The patches, in the order they ran

Orrery, on 4a40d27:
1. `patch_L191_1_sun_pairs_20261021.py`: the fourteen pairs, and the
   dashboard's Drawer Order button.
2. `patch_L460_2_corona_base_20261021.py`: the corona's base. After 1.
3. `patch_L460_3_hills_inside_edges_20261021.py`: the Hills cloud.
4. The maintenance run (31 of 31; gate path 0; whole tree 277), commit,
   push.

Website, on 72c3c403, after the orrery push (pushed at f66f66de and
645558e2):
5. `patch_L460_2_corona_base_website_20261021.py`: the streamer belt's
   and the corona's base linked to the new rows, the corona's words, the
   Drawn ends check.
6. The Daily Run, the gallery maintenance run (34 of 34), commit, push
   (90cefa57), the live run (2 of 2; the served export is the orrery's
   at 645558e2).

Then this close patch, on the orrery: the ledger, Where We Are, the two
skills, the protocol's v3.107, the dashboard's Drawn Ends button, the
discovery record and this handoff.

## 5. The scanner

The fourteen pairs moved the whole-tree Tier-1 count down by 3, and it
is not a clearing. Three uncited lines of the Sun-and-corona hover (the
Parker probe's closest approach, the MAPS comet's crossings and its
perihelion) now sit within the scanner's 60-line window of the Alfven
surface's citation, which is not their source. Recorded as L-467. The
gate path stayed at 0.

## 6. Skills

- interactive-exhibit 1.18 -> 1.19: a room's drawer lists its shells
  where each begins.
- provenance-discipline 2.32 -> 2.33: a drawing starts and stops where a
  served row says; and an agency page that names no source is read one
  layer down (your ruling of today, talk C).
- This session loaded interactive-exhibit 1.18, provenance-discipline
  2.32 and ledger-and-session-records 1.21, as the manifest expected.
- **The next session confirms its loaded copies read interactive-exhibit
  1.19 and provenance-discipline 2.33** before work that fires them.

## 7. Open, by name

- L-460 (the drawer order): your phone look confirmed the Sun's order;
  the magnetotail's reading with the next website patch closes it.
- L-468 (your phone look tonight): the corona's drawer row opens the
  streamer belt's words, because the belt joined the corona's row on
  Oct 20 and the drawer opens the first tap cross in a row. Fix with
  the next website patch. And where the Hills cloud's tap cross goes:
  it sits on the x axis at 20,400 AU, just past the cloud's edge; for
  the next design talk.
- L-191 (the 14 pairs): your look in the orrery, each Sun checkbox's
  tooltip beside its marker's hover, closes the Sun's share. The gas
  giants', Planet 9's and the Moon's strings wait for their rooms.
- L-466 (drawn ends): three held ends are OPEN. The clumps (L-434), and
  Earth's two radiation belts, whose dots follow field lines down toward
  the ground where no row says how far down the particles reach (Earth's
  slice, L-413).
- L-467 (the scanner's positional credit): the three hover lines get
  rows or come out when the braid reaches them.

## 8. Next session

Start with L-434 (stored drawings): the tide and the clumps placed once
by the orrery from a seed, between their rows' edges and checked there,
served and drawn by the website, with the tide's phone look. It closes
the clumps' held end in the Drawn ends check. Its website patch also
carries the corona's drawer text (L-468) and the magnetotail's reading
(L-460). Then L-454's two faint surfaces on the Alfven
surface, as L-412's Gap lists.

## 9. Your actions

- (do) Run this close patch, the maintenance run, commit and push.
- (do) Reinstall interactive-exhibit 1.19 and provenance-discipline
  2.33 (Settings > Skills).
- (do) In the orrery: a few Sun checkboxes' tooltips beside their
  markers' hovers read the same.
- (do) Three papers into `papers/` when convenient
  (`READING_L456_tony_20261021.md`), carried from the last close.

## Where this leaves us

- Every room's drawer now follows the distances its rows give; your
  phone confirmed the Sun's.
- Every drawing in the Sun and Earth rooms is checked against its rows
  on each run; two were wrong and are fixed.
- Next is the tide and the clumps as stored drawings, with the corona's
  drawer text fixed in the same website patch.
