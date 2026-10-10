<!-- Doc-Kind: hand | Design talk for L-421 (the typed facts): the inner Oort cloud redrawn as the tilted disk of Nesvorny et al. 2025 -- the trace of the 20,000 au edge, the outer-edge question, and the hover words. Zero code. October 9, 2026. -->
# L-421 (the typed facts): the inner Oort cloud, tilted -- design record

Built on orrery aa46bb102a351984ba800cbfbd0d801853110b9f at
https://github.com/tonylquintanilla/palomas_orrery ("L418_5 testing
close") and gallery 5ec4739b6f160b7f4a455004b2bc5727e61a7815 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io ("daily
run 10-9-26"). Both clones matched the SHAs Tony named.

- Type: DESIGN SESSION (zero code). No patch, no build.
- Supersedes: nothing. Continues item 1 of
  `documentation/HANDOFF_L421_typed_facts_20261008.md`.
- Skills loaded: ledger-and-session-records 1.18 (matches the
  manifest row, 1.18).
- Read: L-421's block in `LEDGER_CONSOLIDATED.md` (its Gap, part 1)
  and `documentation/L421_round1_sources_20261006.md`.
- The brief Tony attached, `HANDOFF_L414_scanner_window_brief_20261009.md`,
  moves L-414 (the scanner's window) ahead of the Oort cloud BUILD.
  This session is design talk only, so the two do not conflict.

## Read this first

- *Settled this session, in order:* the inner cloud gives way to the
  outer cloud across a fuzzy band from 10,000 to 20,000 au; the Hills
  cloud is drawn as dots along orbits picked inside the paper's ranges,
  so its two arms and its tilt (near 30 degrees) come out of the orbits;
  its hover, panel words and note are confirmed (sections 4, 5, 9);
  the galactic plane ring, its poles and Sgr A* (L-408) ride the same
  build, with its words confirmed (section 10); the lobby moves to
  option E with new words (section 11).
- *Nothing is built or patched.* The ledger (L-421, L-408, and a new
  item for the lobby) and Where We Are are updated by the build
  session's patch, from this record.

Earlier notes, kept as written:

- *Corrected this session, after the paper was read (section 2a):*
  before the read, this record said the 20,000 au row did not need to
  move. The paper says the round outer cloud begins at about 10,000
  au, not 20,000. So the place where the inner cloud gives way to the
  outer one is now the question, for all four of the row's uses.
- *The question to Tony is in section 3.* His answer goes below it.
- *The paper gives the tilt as "about 30 degrees", with no range.* The
  L-421 handoff's "the tilt a range that can be drawn as an envelope"
  is not in the paper. Whether to draw an envelope is a question for
  the hover-words round, not a sourced range.

## 1. What uses the 20,000 au edge

The row is `INNER_OORT_CLOUD_AU = 20000` in `constants_new.py`,
sourced to Portegies Zwart et al. (2021), A&A 652:A144, sec. 2.2: "the
Hills cloud lies between the outer edge of the parking zone and the
inner edge of the Oort cloud, at about 20,000 au or less."

It does two jobs at once:

- **Where the inner cloud ends** -- 2 uses: the Hills cloud torus's
  outer edge, and the "Inner Oort Cloud" sphere drawn at 20,000 au.
- **Where the outer cloud begins** -- 2 uses: the clumpy outer cloud's
  inner edge, and the galactic tide's inner edge.

The source sentence describes the second job.

### Gallery (5ec4739)

- `data/objects_config.json`, four links to `INNER_OORT_CLOUD_AU`,
  all under the Sun's `oort_cloud` block:
  - `hills_cloud_torus.outer_radius`
  - `outer_oort_clumpy.inner_radius`
  - `galactic_tide.inner_radius`
  - `inner_oort.radius`
- Written into the config by `tools/mirror_constants.py` from
  `data/constants_export.json`; copied by the cache builder into
  `data/solar-system/feature_configs.json` and
  `data/solar-system/coverage_index.json`.
- Drawn by `gallery/feature_renderers.js`: `torusPoints`,
  `clumpFieldPoints` and `tideFieldPoints` through `renderOortShape`,
  and the `inner_oort` sphere through the plain shell path.
- The typed caveat being replaced (S1) is `HILLS_CAVEAT` in
  `feature_renderers.js`: "Drawn flattened toward the ecliptic, as the
  inner cloud is thought to be; the thickness is chosen for the
  picture."

### Orrery (aa46bb1)

- `solar_visualization_shells.py`, reading the row:
  - `create_sun_inner_oort_shell` -- the sphere at 20,000 au.
  - `create_sun_galactic_tide` -- the tide's inner edge, and its edge
    rings.
  - Through `_OORT_HILLS_EDGE`, twelve hover and tooltip strings:
    `gravitational_influence_info`, `inner_oort_info`,
    `inner_limit_oort_info`, `hills_cloud_torus_info`,
    `outer_oort_clumpy_info`, `galactic_tide_info`,
    `gravitational_influence_info_hover`, `inner_oort_info_hover`,
    `inner_limit_oort_info_hover`, `hills_hover`, `clumpy_hover`,
    and `tide_hover`.
- `solar_visualization_shells.py`, TYPING the number instead of reading
  it -- 2 builders:
  - `create_sun_hills_cloud_torus(..., inner_radius=2000, outer_radius=20000, ...)`
  - `create_sun_outer_oort_clumpy(..., radius_min=20000, ...)`
  - `planet_visualization.py` calls both with no arguments, so the
    typed defaults are what draws. They equal the rows today; they would
    not follow a change.
- `shell_configs.py`: the `inner_oort` shell's `radius_au`.
- `test_constants_provenance.py`, line 221: asserts 2,000 < 20,000 <
  100,000 < the Sun's gravitational reach. Either answer below keeps it
  true.
- Imports only, no other use: `palomas_orrery.py`,
  `palomas_orrery_helpers.py`, `planet_visualization_utilities.py`,
  `planet_visualization.py`.
- `images/sun_gui_mockup.html`: an old mockup, typed numbers and Hills
  (1981) citations. Not served; not on any build path.

## 2a. The paper, read 2026-10-09

Nesvorny, Dones, Vokrouhlicky, Levison, Beauge, Faherty, Emmart and
Parker (2025), "A Spiral Structure in the Inner Oort Cloud", ApJ 983:1;
arXiv:2502.11252v1. Read in full from the PDF Tony attached (from
https://arxiv.org/pdf/2502.11252v1), 2026-10-09, Claude Opus 5.5.
Page numbers are the arXiv v1 PDF's.

- **Where the disk is.** Sec. 1, p. 2: "Dynamical simulations reveal
  formation of the inner Oort cloud at 1,000 < r < 10,000 au (Duncan
  et al. 1987, Levison et al. 2001, Vokrouhlicky et al. 2019)." Repeated
  in sec. 1 p. 3 and sec. 5 p. 11 ("At 1,000-10,000 au ...").
- **Where the round cloud begins.** Sec. 1, p. 2: the new long-period
  comets' nearly isotropic inclinations suggest "that the outer Oort
  cloud at r > 10,000 au is roughly spherical (see Dones et al. 2015
  for a review)." Footnote 7, p. 7: beyond 10,000 au the tide's cycles
  are much shorter than the solar system's age, which "effectively
  randomizes the spatial distribution of bodies and gives the outer
  Oort cloud its nearly isotropic appearance."
- **The shape.** Sec. 1, p. 3: "the inner Oort cloud is a slightly
  warped disk, roughly 15,000 au across, inclined i ~ 30 deg to the
  ecliptic (nearly polar in the Galactic reference system, Galactic
  inclination iG ~ 90 deg)." Seen from far away, "a spiral structure
  with two twisted arms." The abstract and sec. 5 say "roughly 15,000
  au in length".
- **Which way it tilts.** Sec. 2, p. 3: the ecliptic is tilted 60.2 deg
  to the Galactic plane; "The main axis of the spiral is aligned with
  the ecliptic -- the ends of the spiral are twisted away from the
  ecliptic." Sec. 5, p. 11: the tide turns the orbits' planes "to
  become nearly perpendicular to the Galactic plane (and OmegaG =
  120-180 deg; Fig. 3)".
- **The tilt has no stated range.** "i ~ 30 deg" is the only figure. The
  i < 30 deg in secs. 2 and 3 is the scattered bodies' STARTING
  inclination, not the disk's tilt.
- **How sure.** A model result. Sec. 2, p. 4: the spiral appears in all
  their simulations with the tide, and is smaller where the local
  stellar density is higher, larger where it is lower. Sec. 5, p. 12:
  "In this sense, the Oort cloud spiral has (indirectly) been
  detected"; direct detection "is difficult".
- **The old picture.** Sec. 1, p. 2: "The inner Oort cloud is therefore
  often portrayed as a relatively flat disk, roughly aligned with the
  ecliptic (Levison et al. 2001)".
- **The whole cloud.** Sec. 1, p. 1: "a large shell of icy bodies
  surrounding the solar system at heliocentric distances 1,000 <~ r <~
  100,000 au."
- **20,000 au in this paper** is about comets, not an edge: footnote 1,
  p. 2, new comets "must have original semimajor axes of at least
  20,000 au" (Krolikowska and Dybczynski 2017).
- **The inner edge moves** with the tide's strength (footnote 3, p. 2).

How it sits with the row: Portegies Zwart (2021) puts the Hills cloud
"at about 20,000 au or less". "Or less" is an upper bound, so a
boundary at 10,000 au does not contradict it.

## 2. Findings recorded, not chased

All sit in files the redraw already opens, so they ride its build
(Cluster the Tail by files touched).

- **Typed defaults** in the two orrery builders above. The redraw
  rewrites the torus builder anyway; the clumps builder's
  `radius_min=20000` is one line beside it.
- **Wrong citation comments** in `solar_visualization_shells.py`: the
  lines over `inner_oort_info` and `hills_cloud_torus_info` still say
  "Source: Hills (1981)". The row was re-sourced to Portegies Zwart
  (2021) on 2026-10-04 (L-371, the Sun's distances) because Hills (1981)
  does not print the number.
- **Words stating the older picture**, beyond the typed caveat:
  - gallery `hills_cloud_torus`: its `description` ("a thick,
    flattened ring"), its `about` ("flattened into a disk-like or
    doughnut shape by the pull of the galaxy"), its `note` ("flattened
    toward the ecliptic").
  - gallery `inner_oort.description`: "where the flattened inner swarm
    gives way to the spherical outer cloud".
  - orrery `hills_cloud_torus_info` and `hills_hover`: "disk-like",
    "toroidal", "short-period comets support disk-like structure".
  These come to Tony with the hover words.

## 3. The outer-edge question

First asked of Tony before the paper was read, as "the paper's
distances or the served ones". Re-asked after the read, 2026-10-09:
where does the inner cloud give way to the round outer cloud -- 10,000
au or 20,000 au?

- **Move the boundary to 10,000 au.** Sourced to Nesvorny et al.
  (2025), sec. 1 p. 2 and footnote 7. The disk then runs 2,000 to
  10,000 au (the served inner edge stays), and the clumps, the
  galactic tide and the "Inner Oort Cloud" sphere move in to 10,000 au
  with it. No empty band; one source for both sides of the line. Costs
  a re-sourced row (or a new one) and a new look on the phone for
  three features that were not otherwise changing. NASA's outer-edge
  range already starts at 10,000 au.
- **Keep 20,000 au and only tilt.** No distance changes. The disk is
  drawn about twice the size the paper finds, and the band from 10,000
  to 20,000 au, which the paper calls round, is drawn as disk. The
  hover would have to say so.
- **Dropped:** disk to 10,000 au with the round cloud still starting at
  20,000 au. It draws an empty band where the paper says the round
  cloud is.

Claude's recommendation: move it to 10,000 au.

Tony's answer, 2026-10-09 16:19: "boundary: would a fuzzy boundary
work? Timely."

Claude's reply: yes, and both ends of the band are sourced.
- 10,000 au: Nesvorny et al. (2025), sec. 1 p. 2 and footnote 7 --
  beyond it the cloud is roughly spherical.
- 20,000 au: Portegies Zwart et al. (2021), sec. 2.2 -- the Hills
  cloud lies "at about 20,000 au or less"; and, per the row's Note in
  `constants_new.py` (read 2026-10-04, not re-read here), sec. 2.3
  says what defines the transition remains unclear.
- So the band from 10,000 to 20,000 au is the sourced range of where
  the change happens, drawn as a range instead of a picked line
  (Show the Envelope of the Unknowable).

What the band would look like (proposed):
- The tilted disk is full out to 10,000 au and thins to nothing by
  20,000 au.
- The round outer cloud (the clumps and the galactic tide) is thin at
  10,000 au and full by 20,000 au. Both overlap inside the band.
- The same point counts, spread differently: the render does not grow.

What it costs:
- A new row for 10,000 au, sourced to Nesvorny et al. (2025). The
  20,000 au row keeps its value and its source, and becomes the band's
  far end.
- The clumps and the tide change look, and get a new phone check.
- The "Inner Oort Cloud" sphere draws one line, which a fuzzy boundary
  does not have. Proposed: it follows Tony's ruling of 2026-10-03 for
  the cloud's other two edges (one sphere, its hover giving the range
  and the end drawn). Which end it sits at is a small question for
  later.

Tony's confirmation of the band, 2026-10-09 16:22: "Yes."

Open for the words round, not asked yet:
- The paper says "roughly 15,000 au across" (sec. 1 p. 3) -- a radius
  near 7,500 au if "across" means diameter -- while also placing the
  inner cloud at 1,000 to 10,000 au, and its Fig. 1 plots only a < 5,000
  au. "Full out to 10,000 au" may draw the disk larger than the paper's
  own picture. The hover can say "about"; whether the band's near end
  should sit nearer 7,500 au is a drawing question to settle before
  build.

## 4. The hover words

Brought to Tony after the question above, because the hover's distance
line prints the edges the answer picks.

Tony's ruling, 2026-10-09 16:19: "say 'about' in the hover and draw 30
Degrees and say so with the citation."
- So: the disk is drawn at 30 degrees to the ecliptic, one tilt, no
  envelope. The hover says "about 30 degrees" and says the drawing uses
  30, with the citation (Nesvorny et al. 2025).
- Under interactive-exhibit 1.12 these are facts about nature and a
  paper, so they are served on the feature's row, not typed in code.
  The 30 degrees becomes a row in `constants_new.py`.

Skills loaded for this round: interactive-exhibit 1.12 and
provenance-discipline 2.27, both matching the manifest. Figure counts
for the new rows are set at build, after reading provenance-discipline's
`references/figures.md` (not opened in this session; no figure count
was written here).

The draft, as a visitor would see it (sent to Tony 2026-10-09). The km
figures print from each row's served `"in"`, as today:

```
Sun: Hills Cloud (tilted disk)

The inner part of the Oort cloud: icy bodies far beyond the planets,
gathered in a slightly warped disk.

From 2,000 AU (km) to 10,000 AU (km), thinning out by 20,000 AU (km).
A 2025 computer model (Nesvorny and others) finds the disk tilted about
30 degrees to the ecliptic, the plane of Earth's orbit. It is drawn at
30 degrees; its thickness is chosen for the picture.
```

- Line 1, the name, changes from "Hills Cloud (torus)": the shape is no
  longer a ring. "Hills Cloud" stays, as the established name and the
  name of its Wikipedia link.
- The description is served `description`, replacing "a thick,
  flattened ring".
- The distance line is built by the renderer from three served rows;
  "thinning out by" is a sentence about the picture (the band).
- The last two sentences are served `hover` words, with the two 30s
  filled from the new tilt row as `{tilt}`, so the words carry no typed
  number. They replace the typed `HILLS_CAVEAT`.
- The short attribution "(Nesvorny and others)" is in the hover; the
  full citation goes in the i panel with the paper's link, by the
  standing rule that citations live in the panel (L-231).
- The orrery's own torus hover (`hills_hover`) gets the same words.
- The i panel's words (`about`, `note`) and the "Inner Oort Cloud"
  sphere's words follow after Tony rules on these.

Tony's answer, 2026-10-09 16:33: "Confirmed."

## 5. The i panel's words for the Hills cloud

The served words today, read at gallery 5ec4739:
- `about`: "The Oort cloud is a vast, unseen swarm of icy bodies
  surrounding the solar system, thought to be the source of the
  long-period comets. Its inner part, the Hills cloud, is more tightly
  bound to the Sun than the outer cloud and, in dynamical models, is
  flattened into a disk-like or doughnut shape by the pull of the
  galaxy. Nobody has seen it directly; its existence is inferred from
  the orbits of comets and from distant objects such as Sedna, which
  may belong to it."
- `note`: "Disk-like rather than spherical: the inner Oort cloud is
  flattened toward the ecliptic, unlike the outer cloud. The thickness
  is a drawing choice."

The draft (sent to Tony 2026-10-09):

- `about`: "The Oort cloud is a vast swarm of icy bodies surrounding
  the solar system, the source of the long-period comets. Its inner
  part, the Hills cloud, is more tightly bound to the Sun. It was long
  pictured as a fairly flat disk lying along the ecliptic. A 2025
  computer model finds instead a slightly warped disk tilted about
  {tilt} degrees to the ecliptic, nearly at right angles to the plane
  of the Milky Way. Seen from far away it would look like a spiral
  with two twisted arms. The Milky Way's tide shapes it over billions
  of years. No one has seen it directly; its shape shows only indirectly,
  in the orbits of some long-period comets."
- `note`: "Drawn as a flat disk tilted {tilt} degrees to the ecliptic.
  The warp and the spiral arms are not drawn. Its thickness, and how it
  fades between {near} and {far} AU, are chosen for the picture."

Each sentence about nature, against the paper (section 2a):
- source of long-period comets: sec. 1 p. 1 ("existence is inferred
  from observations of long-period comets").
- more tightly bound: sec. 1 p. 2 ("more strongly bound to the Sun").
- long pictured as flat along the ecliptic: sec. 1 p. 2 (Levison et al.
  2001 portrayal).
- warped disk, about 30 degrees, nearly at right angles to the galaxy, spiral
  with two twisted arms: sec. 1 p. 3.
- the Milky Way's tide, billions of years: sec. 2 pp. 3-4 ("persists over
  billions of years"; "a consequence of the Galactic tide").
- seen only indirectly, through comets: sec. 5 p. 12 ("In this sense,
  the Oort cloud spiral has (indirectly) been detected").

Removed, recorded: "distant objects such as Sedna, which may belong to
it". The paper does not say it and the served entry gives no source for
it. A fact about nature on a served row needs its source
(interactive-exhibit 1.12), so it comes out and the gap is noted here.

Placeholders, not typed numbers: `{tilt}` from the new tilt row;
`{near}` and `{far}` from the band's two rows. Whether the i panel's
`about` fills braces as the hover and the `note` do is a build check.

Drawing decision inside the note, put to Tony with the words: the disk
is drawn flat and tilted. The paper's warp and its two spiral arms are
not drawn.

Tony's answer, 2026-10-09 16:42: "Yes. I never heard of the arms."
Both the words and the flat drawing are confirmed.

## 6. The galactic plane in the Sun room

Tony asked, 2026-10-09 16:42: "are we planning to draw the galactic
equator like in the orrery coordinates?"

What the record says:
- The orrery draws it: L-420 (the galactic plane in the Celestial
  Grid), DONE 2026-10-07 -- a violet circle on the sky with NGP and SGP,
  in `star_sphere_builder.py`.
- The Sun room does not. It is designed and its words approved as L-408
  (a Galactic Plane toggle in the Sun room), 2026-10-03: one row, off by
  default, a faint ring in the galaxy's plane at 100,000 au and a line
  along the galactic pole through the Sun, reading the same two pole
  rows the tide reads. Its Gap: Tony's decision at a design talk on
  whether the phone draws it ("awaits the design talk", 2026-10-07).
  It is the Sun slice's eighth item (L-412, the Sun's list).

Two links to this redraw, found this session:
- The new disk stands nearly at right angles to the galactic plane
  (sec. 1 p. 3, iG ~ 90 deg). The ring is what shows that at a glance.
- **One of L-408's approved sentences is now wrong:** "That tilt is why
  the galactic tide looks tipped against the Hills cloud, which lies
  close to the planets' plane." After the redraw the Hills cloud is
  tilted 30 degrees off the planets' plane, toward upright to the
  galaxy. Not served yet (L-408 is unbuilt), so nothing on the site is
  wrong; the sentence is rewritten before L-408 builds, whenever that
  is.

Put to Tony: build the ring in the same build as the redraw, with that
sentence rewritten?

Tony's answer, 2026-10-09 16:51: "On the galactic plane ring and
sentence rewrite, yes, and include the poles and *SagA location."

- So L-408 (a Galactic Plane toggle in the Sun room) rides the redraw's
  build: the ring, the pole line, the two poles marked, and the
  direction of Sagittarius A*.
- Sgr A* needs no new number: L-420 added `SGR_A_STAR_RA_ICRS_ARCSEC`
  and `SGR_A_STAR_DEC_ICRS_ARCSEC` (and their degree conversions) to
  `constants_new.py`, and both are in the gallery's
  `data/constants_export.json` at 5ec4739. L-408's "needs one more
  sourced number" is answered by those rows.
- The rewritten sentence, and words for the poles and Sgr A*, come to
  Tony before build.

## 7. The X and the arms

Tony asked, 16:44: "are the arms related to the X in the galactic tide
illustration?"

Claude's answer: related by cause, not the same thing.
- Same cause: the part of the Milky Way's tide that pulls across the
  galaxy's plane. The paper's analytic model keeps only that part (sec.
  3 p. 6, from Heisler and Tremaine 1986); the tide's density rule
  cites Matese and Whitmire, whose main term is the same.
- The X: the outer cloud, where the tide pulls orbits' closest points
  in fastest -- the comets that arrive (Delsemme 1987, on the tide's
  row).
- The arms: the inner cloud, sorted slowly. Sec. 3 p. 7: orbits with
  omegaG in 0-90 or 180-270 deg have their perihelion pulled in, meet
  the planets and are removed; orbits with 90-180 or 270-360 deg
  decouple, turn nearly polar to the galaxy and freeze. Those two
  preferred directions are the two arms (sec. 5 p. 11).
- The pairing ("the X shows what the tide sends in, the arms what it
  leaves") is Claude's reading of the two sources together. The paper
  does not mention the X or Delsemme's pattern.

Tony, 16:51: "Domaine we should draw the arms and we already cited the
X pattern in the galactic tide card." Read as unclear -- either "maybe
we should draw the arms" or "do you mean we should draw the arms" --
and asked back. Earlier (16:42) he had confirmed the flat disk without
arms.

Tony's answer, 16:56: "Please draw the arms. The autocorrect threw me
off." This supersedes the flat disk confirmed at 16:42. The confirmed
panel `note` ("The warp and the spiral arms are not drawn") changes
with it, and so may the hover's "It is drawn at 30 degrees"; both come
back to Tony with the method below.

## 8. How the arms are drawn

What the paper gives, read 2026-10-09 (figure captions, pp. 19-21):
- Fig. 2: "Most orbits in the inner Oort cloud are expected to have
  omegaG = 70-180 deg or omegaG = 250-360 deg. These two broad
  concentrations in omegaG appear as two spiral arms" (a ~ 3,000 au).
- Fig. 3: "nearly polar orbits in the Galactic frame (iG = 75-90 deg)
  and orbital planes that are only slightly rotated away from the
  ecliptic (OmegaG = 120-180 deg; the ascending node of the ecliptic is
  at the Galactic longitude l = 186 deg)".
- Fig. 4: the spiral rebuilt from 34,000 orbits with 2,000 < a < 5,000
  au, 10 < q < 30 au, i < 30 deg, carried 4.6 Gyr forward by the
  analytic formulas of Breiter and Ratajczak (2005). Elliptic functions
  over 4.6 billion years: not something to run in a visitor's browser.
- Eccentricity of today's orbits: shown only as a plot (Fig. 6), never
  stated as a number.

Two ways, put to Tony 2026-10-09:
- **A. Build it from the orbits.** Draw points along orbits picked
  inside the paper's stated ranges (omegaG, iG, OmegaG from the
  captions, distances from the band), turned into the ecliptic frame by
  the served galactic pole. Points crowd where orbits spend their time,
  at their far ends, and the arms and the tilt appear on their own
  rather than being imposed. The tilt is then whatever the orbits give,
  near 30 degrees, not set to 30. Eccentricity is not stated, so it is
  a declared pick with its reason on the row (or read off Fig. 6 and
  recorded as such). New rows: the omegaG, iG and OmegaG ranges, and
  the ecliptic node at l = 186 deg if the pole rows do not already give
  it.
- **B. Draw a picture of the arms.** Keep the 30-degree disk as ruled
  and lay two spiral arms over it as an illustration. The paper gives no
  formula for the arm shape, so the arms' curve is a drawing choice,
  and the note says so.

Claude's recommendation: A. The arms are the orbits' far ends bunching
in two directions; drawn that way, the picture carries the paper's own
explanation, and nothing about the shape is invented except the
eccentricity, which is declared. It changes the 16:19 ruling ("draw 30
degrees"): the tilt would come out of the orbits instead. Point count
stays at the torus's 3,600 (render size).

Tony's answer, 16:59: "A. And it's consistent with 'about' 30
degrees." So the 16:19 ruling is refined, not dropped: the hover still
says "about 30 degrees" from the paper's row; the drawing's tilt comes
out of the orbits.

## 9. The hover and note, revised for the arms

The 16:33 hover's last sentence ("It is drawn at 30 degrees; its
thickness is chosen for the picture.") and the 16:42 note no longer
describe the drawing. Revised drafts, sent to Tony 2026-10-09:

Hover, last two sentences (served `hover`):
"A 2025 computer model (Nesvorny and others) finds the disk tilted
about {tilt} degrees to the ecliptic, the plane of Earth's orbit, with
two spiral arms. The dots follow orbits like the model's; how stretched
the orbits are is chosen for the picture."

Note (served `note`):
"Drawn as dots along orbits picked within the ranges the model gives,
so the tilt and the two arms come out of the orbits rather than being
drawn by hand. How stretched the orbits are is chosen for the picture:
the model shows it only as a plot. The dots thin out between {near}
and {far} AU."

Unchanged: the name "Hills Cloud (tilted disk)", the description, the
distance line, and the `about` paragraph (it already names the arms).

Tony's answer, 17:03: "rather than being drawn by hand -- drop this
phrase. Not needed." Taken as confirming both with that cut. The note
as confirmed:
"Drawn as dots along orbits picked within the ranges the model gives,
so the tilt and the two arms come out of the orbits. How stretched the
orbits are is chosen for the picture: the model shows it only as a
plot. The dots thin out between {near} and {far} AU."

## Owed to the build session

- The paper was read this session (section 2a). The build session
  quotes from section 2a, or re-reads the PDF (Tony keeps it in
  `papers/`, which git never commits).
- Then the build as the L-421 handoff lists it: the rows, the redraw in
  both repos, Tony's look on the phone.

Session record written October 2026 with Anthropic's Claude Opus 5.5.

## 10. The galactic plane's words (L-408, now riding this build)

Approved 2026-10-03 on L-408 and kept as approved, except where marked.

- Row name: "Galactic Plane" (unchanged).
- Description, extended for the poles and Sgr A*: "The plane of the
  Milky Way's disk, drawn as a ring around the Sun, with a line along
  the galaxy's north-south axis, its two poles marked, and the
  direction of the galaxy's centre."
- Info panel, last sentence rewritten. Approved text before it
  unchanged ("The Milky Way is a flat disk ... the two planes meet at
  [ANGLE] degrees."). Was: "That tilt is why the galactic tide looks
  tipped against the Hills cloud, which lies close to the planets'
  plane." Draft: "That is why the galactic tide is drawn tipped against
  the planets. The Hills cloud stands nearly at right angles to the
  galaxy's plane, turned there by the same tide over billions of
  years." (Nesvorny et al. 2025, sec. 1 p. 3, sec. 2 p. 3, sec. 5 p. 11.)
- Note, one sentence added: "The ring is drawn at the outer edge of the
  Oort cloud, where the tide is drawn, to show the plane's direction.
  The galaxy's disk reaches far beyond it. The poles and the galaxy's
  centre are marked as directions on the same ring, not at their real
  distances."
- Pole markers, the orrery's approved words (L-420) reused: "North
  Galactic Pole (NGP) / Perpendicular to the disk of our galaxy", and
  the same for SGP.
- Sgr A* marker, draft: "Sagittarius A* / The direction of the centre
  of our galaxy, seen from the Sun". The orrery's L-420 hover also says
  "The black hole at the centre of our galaxy", but the row's source
  (Liu, Zhu and Hu, arXiv:1110.6268, eq. 8; Reid and Brunthaler 2004)
  is cited for the POSITION. Under interactive-exhibit 1.12 a served
  fact needs its source, so "black hole" is left out until a source
  for it is read. The orrery's own hover carries the same gap:
  recorded, not chased.
- Link unchanged: Wikipedia, "Galactic coordinate system".

Tony's answer, 17:07: "Yes." Then: "What will the link for that panel
card be?" Answered: https://en.wikipedia.org/wiki/Galactic_coordinate_system,
shown as "Read more at Wikipedia", approved on L-408 2026-10-03, when a
search found no NASA page specific to the galactic plane (the L-265
rule). One link for the whole feature: ring, axis line, both poles and
the Sgr A* marker. The build confirms the URL still answers before it
ships. The Hills cloud keeps its own link, Wikipedia "Hills cloud".

## 11. Aside: the lobby's starting point (not L-421)

Tony, 17:10, with a phone screenshot of the live lobby: a friend shown
the site "was confused on where to go. He started with the rooms and
cards but still unsure. Can you use design to make the solar system
interactive as the clear starting point?"

- What the screenshot shows: the three doors fill the phone's first
  screen; "The Solar System, live" (the L-363 wide card, sketch C of
  2026-10-04) starts at the very bottom, below the "Featured" heading,
  so it is effectively below the fold.
- Three new options added to Tony's existing canvas "Lobby: the Solar
  System way in" (the L-363 canvas, A to C), as a second row titled
  "Round 2 (Oct 9)", each with a gold guide line where a phone's first
  screen ends (about 844 px):
  - D. Start card first: the real room picture, "Start here", the
    title, Tony's served sentence, one big "Enter the Solar System"
    button, all above the subjects; "Doors" renamed "More to explore".
  - E. The picture is the way in: the room picture edge to edge with
    one button under it; the subjects follow as "Or explore by
    subject". Its welcome sentence is a new draft, not Tony's.
  - F. Where to start, in three steps: 1 the Solar System, 2 a room
    (the Sun, Earth and Moon), 3 the exhibits by subject.
- All three rename the "Doors" heading: a first-time visitor has no
  way to know what a door is.
- Design only. No ledger item yet; one is opened when Tony picks a
  direction.

Tony's answer, 17:20: "A". Today's options were D, E and F; A is the
October 3 sketch on the same canvas ("Hero card above the doors"),
which is close to D. Asked back which he means.
- October's A: a drawn orbit sketch, "Start here", one button, and a
  link "Or browse the 33 Solar System exhibits"; the Solar System door
  is folded into the card, leaving two doors under "Doors".
- Today's D: the real room picture, Tony's served sentence, one
  button; all three subjects stay, under "More to explore".

Tony's answer, 17:23: "Then E". The direction is E, the picture is the
way in: the room picture edge to edge under the title, with the title
"Start with the Solar System, live", one sentence and one "Enter"
button; then the three subjects under "Or explore by subject".
Featured and the guest book stay below, as now (not drawn on the
artboard).

Open before build, one at a time:
- The welcome line. E's draft, "The solar system, the Earth and the
  stars, to explore.", is Claude's; the live page serves Tony's
  sentence from gallery_config.json ("Explore interactive
  visualizations of the solar system, stellar neighborhoods,
  exoplanets, and more."). Asked 2026-10-09.
- The card's sentence. E's draft, "Today's planets in 3D. Turn it with
  your finger, tap a planet, step into the Sun and Earth.", is also
  Claude's; the live card serves Tony's "Turn it, zoom in, and step
  into the rooms of the Sun and Earth. Daily updates from JPL
  Horizons." from gallery_metadata.json.

Tony's answer, 17:25: "Use the new wording." Both drafts are
confirmed. Two notes for the build, not re-asked:
- "Turn it with your finger" is phone wording; the desktop turns it
  with a mouse. The build shows Tony the desktop look and names this.
- The card's "Daily updates from JPL Horizons" goes. The room itself
  still names its source.

Where the words live: the welcome line is the `sentence` in the
gallery's `gallery_config.json`; the card's sentence and title are its
`description` and `title` in `gallery/gallery_metadata.json` (card id
`solar_system`). Both are edited through the gallery's own tools or a
patch, not typed into index.html.
