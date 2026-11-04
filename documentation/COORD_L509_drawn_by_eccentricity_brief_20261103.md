<!-- Doc-Kind: hand | Brief for a Claude Code build: L-509, part 1 -- a small body drawn by its eccentricity as of today, the typed open_path retired. Part 2 (the plan's start date) is named for its own session. -->
# Brief: L-509, part 1 -- a small body is drawn by its eccentricity

Tony Quintanilla, PE | Claude Opus 5.5 (the coordinating session of Nov 3, late afternoon) | November 3, 2026

Built on orrery b09989e0d706b4454d7539bd4c392752b64c87bf at
https://github.com/tonylquintanilla/palomas_orrery (branch main), plus
`patch_L484_2_talk_records.py`, which writes L-509 into the ledger;
gallery 5abca2c614f348e9183b313a6c48de310f1dfc98 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io (read only).
The session starts after Tony's push of that patch, and its first step
confirms HEAD is that push and that L-509 is in the ledger.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: BUILD brief, for one Claude Code session.

## 0. The method, and why

- **Claude Code session, Opus, high effort**, opened through the
  python_work door, in the orrery folder. By METHOD_MODEL_EFFORT.md:
  more than three files, the terminal loop (tests, the maintenance run,
  a JPL fetch), and orbital mechanics, which is the row's "high". A
  patch would not do: the first step is a map of every reader of two
  typed fields, which needs the code searched and run, not anchors
  known in advance.
- **Part 1 only.** L-509 holds two changes to the same two files. Part
  2 (section 9) is a separate problem with its own open question, so
  it gets its own session when it is next: one job per session.
- **One stop point** (step 1). Otherwise the session builds through.

## 1. Why, in two sentences

Three hyperbolic comets (Tsuchinshan C/2023 A3, Wierzchos C/2024 E1,
ATLAS C/2024 G3) are typed 'orbital' in `celestial_objects.py`, so the
orrery draws a closed orbit for a body that passes the Sun once and
does not come back, while the website draws its path. Whether a body
is drawn as a path or an orbit is today decided by fields typed by
hand ('open_path', 'object_type'), which Tony calls "a legacy of my
manual method"; JPL's eccentricity should decide it.

## 2. The ruling (read L-509 and L-484 in the ledger first)

Tony, Nov 3, 15:33 to 15:55 Chicago, in his words: "They should be
drawn as all the Hyperbolic objects." "This is not a special class."
"I would say e and JPL should agree. And as far as fetching we should
update with the 30-day check." "How does JPL determine the class? By e."

As confirmed: each small body's drawing follows its eccentricity as of
today, fetched on the 30-day cycle. At or above 1 it is drawn as a path
(by its path plan, as 3I/ATLAS is); below 1 as an orbit. The typed
'object_type' and 'open_path' stop deciding it. There is NO comparison
with JPL's class: for a comet the class is set by e, so that check
could not fail.

## 3. What is already found at b09989e0

Read from the code and from JPL on Nov 3; the session re-reads what it
relies on.

- **JPL today** (Horizons, ELEMENTS, CENTER 500@10, 2026-11-03 00:00
  TDB): Tsuchinshan e 1.000186673 (JPL#113), Wierzchos 1.000362756
  (JPL#70), ATLAS 1.000009308 (JPL#29). JPL's small-body database
  classes all three HYP.
- **The cache is stale, and that is the whole risk.**
  `data/osculating_cache.json` holds e as of each body's last plot:
  Wierzchos 0.9999997 at 2026-02-25 (BELOW 1, though today's is above),
  ATLAS 1.0000066 at 2026-02-10, Borisov at 2026-02-10. Tsuchinshan is
  not in the cache at all. A rule reading this cache unrefreshed would
  draw Wierzchos as an orbit.
- **The fetch already exists.** `period_fetch.py` runs in the
  maintenance run just before the Horizons check (order: Period fetch,
  Horizons check, Path plan; `orrery_maintenance_run.py` GENERATORS).
  It fetches osculating elements with plotting's own call
  (`osculating_cache_manager.fetch_osculating_elements`), elements and
  period together, but only where a period is missing or asked of the
  wrong body, and it SKIPS every entry marked 'open_path'
  (`classify`, "a comet on an open path serves no period").
- **Nothing fetches e on a 30-day cycle.** `path_plan.py`'s 30-day
  cycle re-plans positions and perihelion from the id, the type, the
  day asked from and the bodies searched.
- **Where 'open_path' is read** (count of mentions by file):
  `celestial_objects.py` 16, `export_objects.py` 10, `path_plan.py` 4,
  `period_fetch.py` 4, `test_path_plan.py` 4. **'trajectory'**:
  `palomas_orrery.py` 19, `test_path_plan.py` 7, `test_period_fetch.py`
  2, `path_plan.py` 1, `orbital_elements.py` 1, `test_horizons_check.py`
  1. These are counts, not the map; step 1 makes the map.
- **The bound: 65 small bodies** ('id_type': 'smallbody') in
  `celestial_objects.py`: 51 'orbital' without open_path; 1 'satellite'
  (Eris/Dysnomia); 3 'orbital' with open_path (the three comets); 10
  'trajectory' with open_path (West, McNaught, C/2025 K1-B, C/2025
  K1-C, C/2025 K1-D, PANSTARRS, Borisov, 1I/Oumuamua, 2I/Borisov,
  3I/ATLAS).
- **The website already draws the three as paths**: the export carries
  their typed open_path, and `data/path_plans.json` holds their plans
  (Tsuchinshan's made 2026-10-26). So the export should not move for
  them.

## 4. The work, in order

1. **Map, then stop if the picture changes (no edits).** Confirm HEAD
   and L-509. Map every reader of 'open_path', and of 'object_type'
   where it chooses path against orbit for a small body, by function:
   the orrery's five consumers (static plot `plot_objects`, animation
   `animate_objects`, social export, and in the gallery repo
   `tools/gallery_studio.py` and `tools/json_converter.py`), the
   fetchers, `path_plan.py`, `period_fetch.py`, `export_objects.py`,
   and the tests. Then print the 65 small bodies by name, each with its
   cached e, the date it was fetched, and its side of 1; for any whose
   elements are older than 30 days or missing, ask JPL for today's e
   (read only; do not write the cache yet).
   **STOP POINT:** if any of the 52 bodies not marked open_path today
   is at or above 1, or any of the 13 marked open_path is below 1, name
   them and ask Tony before going on: that body would change how both
   instruments draw it. If none changes side, say so in one line and
   go on.
2. **The fetch.** `period_fetch.py` also refreshes the osculating
   elements of every small body whose cached elements are older than
   30 days or missing, around the Sun, with plotting's own call. The
   open-path comets are no longer skipped for elements (they still
   serve no period). It prints each body it asks for, and why, as it
   does now.
3. **One home for the rule.** One function decides path or orbit for
   a small body from its cached heliocentric e (at or above 1, a path),
   and says so when the cache has no e (a named failure, never a quiet
   default). The session puts it where the map of step 1 says the
   readers can reach it, and every reader that used 'open_path' (or
   'object_type', for that choice) calls it instead. `path_plan.py`'s
   choice of which comets get a plan is one of those readers.
4. **The typed field out.** 'open_path' leaves `celestial_objects.py`.
   A test fails, naming the entry, if it comes back (the shape of
   `test_path_plan.py` check 19 for a typed end date). For
   'object_type' on small bodies: it stops choosing path against
   orbit. Any other job the map shows it still does stays, and the
   report names each one.
5. **Wierzchos's comment** in `celestial_objects.py`, "near-parabolic,
   outbound period ~200,000 years", disagrees with JPL's class:
   corrected to what JPL gives, or removed (provenance-discipline: no
   recalled figure stays).
6. **The skill.** horizons-orbital-mechanics' next version carries the
   rule (a small body drawn by today's e, fetched on the cycle), and
   the sentence carried on L-509 (A Plan Draws a Path Only Around the
   Sun: the drawing now keeps the daily tail and leaves out only the
   last-day pair). One bump, by the records skill's four steps
   (version line, `skills_index.py`, a protocol history entry, one
   commit). gallery-cache-builder too, only if its open_path sentences
   become wrong; if so, that is its own bump in the same session.

## 5. Things this build does not do

- **No website edits.** The export keeps its 'open_path' field, now
  written by the rule instead of copied from the list, so the website
  reads it unchanged.
- No new words in any text box. The three comets' descriptions already
  say "Hyperbolic: its orbit is an open curve".
- No comparison with JPL's class (ruled out, section 2).
- Not part 2 (section 9).

## 6. The rules it runs under

Read each before the work it governs. Open the first report with each
version line read, against the manifest in `PROJECT_INSTRUCTIONS.md` at
HEAD: horizons-orbital-mechanics 1.15 (osculating elements, which
record serves a body, a comet on an open path's plan, the period
fetch); orrery-coding-conventions 1.13 (the live dispatch path);
gallery-cache-builder 1.17 (a comet on an open path fetched by its
plan, is_path_body, open_path); provenance-discipline 2.36;
safe-file-editing 1.14; agentic-pre-test 1.3;
ledger-and-session-records 1.22. A skill loaded for one section is
read in that section. The protocol's Check All Parallel Pipelines and
Verify Execution, Not Appearance govern step 1.

## 7. Done when

- **A check that can fail:** a test gives the rule one body on each
  side of 1 and one with no cached e, and is shown failing once with a
  planted fault (the comparison turned the wrong way).
- The guard of step 4 shown failing once on a planted 'open_path'.
- The period fetch's output names the bodies it refreshed, with
  Tsuchinshan among them (it has no cache entry today).
- The objects export byte-identical before and after, by diff, or
  each moved line named.
- py_compile, the pre-test on a throwaway copy, and the orrery's
  maintenance run, each read from its output.
- **Tony's Mode 5 look**, in the run order: Sun-centred plots of
  Tsuchinshan, Wierzchos and ATLAS, each drawn as a path like 3I/ATLAS
  (solid to today, dashed after); 3I/ATLAS unchanged; one comet on a
  closed orbit, Halley, still drawn as its ellipse.

## 8. Records, in the same session

- L-509: part 1 built, verified against claimed; the map of step 1 by
  name; the 65 with their side of 1; part 2 left open as its Gap.
- L-484 (the two agree): the three comets' difference closed by this
  build.
- Where We Are, by section: the box, the road, Deferred, Signals read
  from files; nothing below the run-record marker.
- The report: files changed with edit counts, the bodies whose drawing
  changed by name, the token count as Claude Code prints it, Tony's run
  order, his Tony-action list, one question at most.

## 9. Part 2, for its own session (not this one)

Ruling 6's start half, from L-476 at its close: the path plan asks JPL
from a date before any launch and lets JPL clip the front; its no-dates
guard changes; the 52 live typed 'start_date' fields stop deciding. Its
first question is a probe: what JPL returns when asked from before its
data begins (an error, or a clipped answer). Its brief is written when
it is next.

Written November 3, 2026 with Anthropic's Claude Opus 5.5.
