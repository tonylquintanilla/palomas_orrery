<!-- Doc-Kind: hand | Brief for two Claude Code sessions (build): the ten Lagrange points (L-297) -- keyed in the orrery in NASA's words, served by the website as a new kind of body (daily positions from JPL, placed at the minute shown), and drawn as markers; with ESCAPADE's two riders (a label side per body; the box's last day explained). -->
# Brief: the ten Lagrange points (L-297)

Tony Quintanilla, PE | Claude Opus 5.5 (coordinating session) | November 18, 2026, evening, Chicago

Built on orrery a1b7673c98b45b05c93c289bade3ab9bec76eb7e at
https://github.com/tonylquintanilla/palomas_orrery and gallery
133dbd21930d39b66283b820ce71bc705a640855 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, both read
live on Nov 18, 2026, 18:20 Chicago. The orrery commit that carries this
brief is Tony's push of it on top of a1b7673c.

Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`,
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.

Type: BRIEF for TWO Claude Code sessions, each opened through the
python_work door, Opus, high effort (orbital mechanics and provenance,
by `METHOD_MODEL_EFFORT.md`). Session 1 works in the orrery; Session 2
in the website. They are split on the last session's lesson: one Code
session across both repositories ran to 525,685 tokens and a compaction
(L-533's evening note). Each session's last report ends with its token
count as Claude Code prints it (the protocol's Token Economy).

Read L-297 (the Lagrange points) on the ledger first, whole: its
September sizing, its Note of Nov 7 and its notes of Nov 15 and 18.
Then L-533 (ESCAPADE)'s evening note of Nov 18 for the two riders. This
brief says what is decided and what differs.

## 1. Why, in two sentences

Road stage 15 on Where We Are: the Lagrange points come next after
ESCAPADE's path (Tony, Nov 18, 13:31: "Keep as planned after escapade";
this session, 18:28: "Yes, the Lagrange points"). ESCAPADE's box names
L2 in words and the website draws no L2; this round draws all ten.

## 2. What this round is, and is not

IS:
- the ten points keyed in the orrery to the Moon's standard (L-513: a
  key, NASA's words and page), the Earth-Moon L1 to L5 (JPL 3011 to
  3015) and the Sun and Earth-Moon barycentre's L1 to L5 (JPL 31 to 35);
- the website serving them as a new kind of body, and drawing each as a
  marker at the minute the room shows;
- the two riders from ESCAPADE: a label side per body, and the box's
  last day explained.

IS NOT:
- a line or a loop for any point; ESCAPADE's loops near L2, which wait
  for an Earth-centred path view in Earth's fold (L-533, Tony, Nov 18,
  18:05);
- a row under a destination, or an encounter (L-534, L-529, the design
  round after this one);
- the points worked out on the page from the Moon or Earth (rejected,
  Tony's ruling of Sep 7; see L-297);
- any change to the box's last day before Tony rules on its cause.

## 3. The rulings

- HOW THEY ARE PLACED, Tony, this session, Nov 18, 18:38, "Yes", to the
  coordinator's recommendation: serve each point's position from JPL
  once a day, and work out where it is at the exact minute the room
  shows from the days on either side, the way the website already
  places a spacecraft (`gallery/assembler/render_spacecraft.py`,
  `position_at`: the parabola through the three served points nearest
  the minute, its error how far that parabola lies from the chord). A
  marker alone, no line. This replaces the September sizing's single
  marker at midnight, which L-297's Note of Nov 7 found would trail the
  Moon by up to about 13 degrees by evening.
- ONE GROUP PER PAIR, Tony, Nov 7, 10:23 (L-515's ruling 4): "Good."
  Each pair's group sits under the pair's smaller body and is listed
  also under the larger: the Earth-Moon points under the Moon, listed
  also under Earth; the Sun and Earth-Moon barycentre's points under
  Earth, listed also under the Sun. Each point is drawn in the centre
  JPL serves it around.
- ALL TEN IN ONE ROUND, Tony, Nov 15, 16:30, "Yes": the new serving
  shape costs the same for one point as for ten.
- THE PRINTED ERROR IS THE CURVE'S, NOT THE STRAIGHT LINE'S, Tony,
  this session, Nov 18, 18:56: "Yes, the straight path is not what is
  happening." Today `position_at` reports how far its parabola lies from
  the straight chord between the two days either side: how much the path
  bends in a day, which overstates the working-out's real miss about a
  hundredfold (section 4's measurements). The box is to print an error
  for the curve the website actually uses. One rule for every body
  placed by `position_at`: the ten points, every spacecraft and every
  comet on an open path, so their boxes change too.
- THE RIDERS, Tony, Nov 18, 17:58, "Yes" (L-533): a label side per body
  (17:57: "consider putting one of the names on the opposite side of its
  symbol"), for the twins and for the points beside Earth and the Moon;
  and the box's last day, 2 or 3 days short of each twin's plan,
  explained before it is changed.

## 4. What is already found, at the two SHAs above

Every line was read from the code or the served data. Re-read before
building; this list is a start, not a proof.

The orrery:
- `celestial_objects.py` lines 438 to 489: the ten entries, each with
  'name', 'id', 'var_name', 'color_key', 'symbol' 'square-open',
  'object_type' 'lagrange_point', 'id_type' 'id', a typed 'start_date'
  and 'end_date' (1900 to 2050), 'mission_info' and 'mission_url'. None
  has a 'key', so none is in the objects export (`export_objects.py`
  line 18: only an entry with a 'key' is exported).
- Their 'mission_info' is typed, none NASA's sentence. EM-L2 to EM-L5
  each say "Earth-Moon Lagrange-1 point is where the Earth's
  gravitational field counters the Moon's", a copying slip (found Nov 15,
  L-297). The Earth-Moon points link to a hyperphysics page; the other
  five to NASA's "What is a Lagrange point?",
  https://science.nasa.gov/resource/what-is-a-lagrange-point/ (with a
  text fragment on the end of the address).
- JPL names the second five by the Sun and Earth-Moon barycentre
  ("SEMB-L1 31" in the entries' comments; the orrery's GUI heading is
  "Sun-Earth-Moon Lagrange Points:", `palomas_orrery.py` line 9550).
  Read JPL's own name for each record before keying 'horizons_name';
  never type it.
- The orrery's drawing of a 'lagrange_point': `palomas_orrery.py` lines
  531, 612, 5024, 5244, 6802 (map them again by grep).

The website:
- No entry for any point in `data/objects_config.json`.
- The builder serves three shapes and its validator enforces them
  (`tools/gallery_cache_builder.py`): osculating elements for every body
  that is not a path (`process_object`, step 3a, line 1376: fetched for
  every non-path body, so a point would fail it); a positions file for a
  path body (`is_path_body`, line 267: a spacecraft or a comet on an
  open path, fetched by the orrery's plan); and features-only, the Sun.
  A Lagrange point is none of these.
- `fetch_vectors_range` (line 450) already fetches daily positions
  around a body's canonical centre, the ecliptic plane, in AU. Every
  body's daily positions end today: the Moon's last served point is
  2026-11-18 (`data/solar-system/raw/vectors/moon.json`), because a body
  with elements is carried past today by its elements. A point has no
  elements, so its positions must run forward across the served window
  too.
- The served window: 88 days either side of today, set by Mercury, the
  shortest of 64 bodies' trusted spans (the Daily Run of Nov 18, its
  [window] line). A point's served span must not narrow it.
- `CENTER_SLUG_MAP` (line 233) knows '@399' (Earth), '@10' and '@sun'
  (the Sun), '@3' (the Earth-Moon barycentre). JPL's ids 31 to 35 and
  3011 to 3015 must never be read as a centre; read how each id passes
  through the map and the '@' strip (line 393) before keying.
- Every path body's label is set "top center",
  `gallery/assembler/render_spacecraft.py` line 217. The twins fly side
  by side, so their names print over each other to Mars.
- The box's last day (L-533): Gold's box says "as far as 7 September
  2027" against its plan's span to 2027-09-10; Blue's says "10 September
  2027" against 2027-09-12. Cause not found.

How far off the minute's working-out could be, measured by the
coordinator from served data with `position_at`'s own rule (the box's
printed error, the parabola against the chord, points a day apart):
- At the Moon's pace (the Moon's served positions around Earth, its last
  60 days): about 2,500 to 2,800 km. The parabola's real miss is far
  smaller: about 2,800 km with points two days apart, so about an
  eighth of that with points a day apart (the miss falls as the cube of
  the spacing).
- At Earth's pace (Earth's served positions around the Sun): about 5,600
  km printed, the real miss about 420 km at two days apart.
- So the Sun and Earth-Moon barycentre's points print a LARGER error
  than the Earth-Moon ones, not a smaller one: they move about 30 km/s
  around the Sun against the Moon's 1 km/s around Earth. The
  coordinator told Tony the opposite at 18:38; this brief corrects it.
  These are a stand-in from two bodies; Session 2 measures the points
  themselves.

## 5. SESSION 1, the orrery: key the ten in NASA's words

Nothing pushed at its end: a key in the export with no website entry
stops the website's objects mirror, and its night with it
(horizons-orbital-mechanics, KEYING). Both repositories push the same
evening, after Session 2.

1. Read NASA's "What is a Lagrange point?" page WHOLE before drafting a
   word (the lesson of Nov 18: a partial fetch of ESCAPADE's page missed
   a word on the same page). Then any NASA page it links for the
   Earth-Moon points. If no NASA page gives a sentence for a point, name
   the gap; type nothing in its place.
2. Draft the words in `documentation/WORDS_L297_lagrange_points_20261118.md`
   (`WORDS_L533_escapade_20261118.md` is the shape): each point's
   display name, its description and info text, one sentence to a
   bullet, each with its source and NASA's words as NASA wrote them;
   American spelling in sentences we compose. The group names for the
   two pairs, using JPL's naming for the second five. STOP for Tony's
   "Approved" before the words enter any file.
3. Read each record in JPL: its exact name for 'horizons_name', the
   centre it answers around, and its first and last day. Confirm the ten
   ids by JPL's main service.
4. Key the ten in `celestial_objects.py`: a 'key' each (the website's
   slugs; propose them in the first report, as `em_l1` to `em_l5` and
   `semb_l1` to `semb_l5` or better), the approved words, NASA's page,
   the slip gone. Whether the typed 1900 to 2050 span stays, and what
   the export should carry for a body with no orbit and no period: read
   `export_objects.py` and say.
5. The orrery's maintenance run green, read from its output; Tier-1 0 on
   the gate path; the Horizons check confirms the ten identities.
6. REPORT, then STOP: files changed, the ten as keyed beside JPL's
   names, the export's ten entries, anything the export or the check
   refused, one question at most. Not pushed.

## 6. SESSION 2, the website: serve and draw the ten, and the riders

Started after Session 1's report, the same evening if it can be; its
prompt is written then. The website's pull reads the orrery's export
from GitHub, and the orrery is not pushed until the end, so Session 2
tests its mirror against the export in Tony's orrery folder and says
how, before anything is pushed.

PART A. The new kind of body, served. Nothing drawn yet.
1. The serving shape: no elements fetched; daily positions from JPL
   around the centre JPL serves the point around, from one day before
   the served window's first day to one day after its last (so the
   parabola has its third point at each edge); a served positions file
   and `as_of_today` as every body has. Name the shape in the builder
   and the validator, with a branch of its own; the fallback branch;
   the served list; the cache-in-step check; the tree parents check.
   Each new check shown failing once on a planted fault.
2. Say whether the points' span can ever narrow the served window, and
   show it cannot.
3. A hand build of the cache for the ten. MEASURE from JPL's own served
   points, with `position_at`'s rule: EM-L2 (the fastest of the
   Earth-Moon five, being farthest) and the barycentre's L1, at points
   a day apart, and at points an hour apart for the two days around
   today. Print the error each would print, the real miss each makes
   (one point left out and predicted from its neighbours), and each
   positions file's size.
4. THE ERROR FOR THE CURVE (section 3, Tony's ruling of 18:56). Propose
   how `position_at` works out the error of the parabola it uses, from
   the served points alone (for one, the gap between the parabola and
   the curve through four points). It must be checkable: for EM-L2, the
   barycentre's L1, Psyche and one comet on an open path, hold one
   served point out, predict it, and show the proposed figure is never
   smaller than the real miss. A figure that can come out smaller than
   the real miss is refused. Print, for those four, the old figure, the
   proposed one and the real miss, and what each box would then print.
5. REPORT, then STOP. Tony rules on the error's method and on the step
   (a day apart, or an hour apart near today), the step in the light of
   the new error. One question: the step; the method is shown, not
   asked, unless the four cases disagree.

PART B. The ten drawn, and the label side.
6. Each point a marker alone: the orrery's symbol for it, square-open
   (orrery-coding-conventions, the Marker Symbol Convention), its name
   beside it, placed by `position_at` at the minute shown. Earth-Moon
   points drawn around Earth, where the Moon is; the barycentre's points
   around the Sun. Map every reader of a body's kind first, the
   protocol's Check All Parallel Pipelines, and name them in the report.
7. The drawer and the tree, by ruling 4 (section 3). The tree's parent
   is a body's fetched centre (the gallery run's Tree parents row); the
   drawer's group is the pair's smaller body. They differ for the
   Earth-Moon points (fetched around Earth, grouped under the Moon):
   say how both hold.
8. The box: the approved words; the distance from the point's centre to
   the digits its error earns (provenance-discipline, A Computed
   Position Prints What Its Errors Earn); the source line, JPL's id,
   centre and day retrieved. A point has no orbit or period; the box
   says nothing of either.
9. THE LABEL SIDE: a side per body, set on its entry, the default
   unchanged for every body not set. Blue and Gold on opposite sides;
   the points set where they sit beside Earth and the Moon. Tony judges
   the sides on his look (Mode 5).
10. REPORT: files changed, the readers mapped, desktop pictures of the
   ten (centred on Earth, and the Solar System view), the twins'
   labels. Tony's go-ahead.

PART C. The box's last day, and the push.
11. THE BOX'S LAST DAY: find why each twin's box stops 2 or 3 days short
    of its plan's span, and report the cause in plain words with what
    would change. Change nothing until Tony rules.
12. Both maintenance runs green, read from their output.
13. REPORT, with Tony's run order: the orrery commit and push; the
    website commit and pull; the Daily Run, its last lines green and the
    swap "ok"; the website push. Then his phone look, written ONLY for
    what the rooms can draw (the lesson of Nov 18: do not ask Tony to
    look for what the room cannot show): which point is seen from which
    centre, at which zoom, and what he should find.
14. PUSH ORDER: orrery first, then the website, the same evening, not
    while a night is running (the orrery's night at 07:17 and 11:17 UTC,
    the website's at 08:17 and 12:17 UTC, by their workflows).

## 7. The rules they run under

Read each before the work it governs; open each session's first report
with each version line read, against the manifest:
- Session 1: horizons-orbital-mechanics 1.19 (Which Record Serves a
  Body; KEYING); provenance-discipline 2.36; orrery-coding-conventions
  1.13; safe-file-editing 1.14; agentic-pre-test 1.3;
  ledger-and-session-records 1.23.
- Session 2: gallery-cache-builder 1.19; interactive-exhibit 1.42;
  gallery-assembler 1.4; horizons-orbital-mechanics 1.19;
  provenance-discipline 2.36 (A Computed Position Prints What Its Errors
  Earn); orrery-coding-conventions 1.13; safe-file-editing 1.14;
  ledger-and-session-records 1.23.

Bumps that ride Session 2, one protocol version entry (v3.143), each by
ledger-and-session-records' four steps in one commit:
- gallery-cache-builder: the fourth serving shape, a point's positions
  across the window.
- interactive-exhibit: a point's marker and box; the label side.
- provenance-discipline 2.36 to 2.37: A Computed Position Prints What
  Its Errors Earn gains the curve's error (Tony, Nov 18, 18:56), with
  the held-out check as its proof; gallery-assembler too if its
  description of `position_at` changes.
- L-537 with it (the skills page moved): the protocol's Stale Skill gate
  and interactive-exhibit both say "Settings > Skills"; both say
  "Plugins, in the sidebar". L-537 closes in that commit.
- horizons-orbital-mechanics only if Session 1 learns a rule about the
  ten records that will hold next month for another body.

## 8. Done when

- The ten are keyed in the orrery in the approved words, served by the
  website, and drawn at the minute shown, each around its centre, with
  the error it earns in its box, worked out for the curve the website
  uses, every spacecraft's and open comet's box with it.
- The twins' names no longer print over each other.
- The cause of the box's last day is explained, and changed only on
  Tony's word.
- Both maintenance runs pass, read from their output; Tier-1 0 on the
  gate path; each new check shown failing once.
- Tony's phone look.

## 9. Records, in the same sessions

- Session 1: L-297, a note: the ten as keyed, the words as approved,
  verified against claimed.
- Session 2: L-297, what was built and measured, the step as ruled;
  L-533, the label side done and the last day's cause and ruling; L-537
  closed if the bump rides. Where We Are by section: stage 15's line,
  the box, Signals read from files; nothing below the run-record
  marker.
- Each report: files changed with their edit counts, the token count,
  Tony's run order, the Tony-action rollup, one question at most.

Written November 18, 2026 with Anthropic's Claude Opus 5.5.
