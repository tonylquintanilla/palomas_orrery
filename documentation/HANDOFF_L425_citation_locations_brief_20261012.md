<!-- Doc-Kind: hand | Brief for the session that builds L-425's three citation location checks in the orrery: every named file exists, every sourced row carries an address with a date, and a link check that visits each address on Tony's machine. Tony's rulings of 2026-10-12. -->
# Brief: the citation location checks (L-425)

Built on orrery c5dff25076294d1402498db424cb3761a245af21 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched.
Tony's local folders: orrery
`C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\`;
gallery `C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\`.
Written October 12, 2026 with Anthropic's Claude Fable 5.1, in a
coordination session; the design and the build are for an Opus session.

- Type: DESIGN SESSION record and build brief (zero code).
- Companions: L-425's ledger block (the measurements and the planted
  faults); `documentation/TESTING_PROTOCOL_provenance_skills_20261008.md`,
  section B (the table of what is and is not checked);
  `documentation/HANDOFF_L418_testing_20261009.md`, Parts 2 and 3 (the
  planted-fault run, every checker's line word for word; the quote
  idea measured); `documentation/DESIGN_rulings_20261012.md`, ruling 2
  (today's rulings, quoted).
- Not in scope: L-424 and L-426, which open `worksheet_checker.py`'s
  `compare()`; a change to a checker gets its own session (ruling of
  2026-10-08). They are the next brief. L-414, the scanner's look-back,
  stays on its own item.

## 0. Before building

- Pull the orrery at HEAD and pin the SHA. This brief was cut at
  c5dff25, before Tony's push of `patch_L401_4`; HEAD will have moved.
  The dashboard labels build may also have landed; if it has, name the
  new rows by its rule (the button is named what the run prints).
- Skills this task fires: provenance-discipline (the citation lines,
  the push gate), safe-file-editing (the patch), agentic-pre-test (the
  new checker runs on a throwaway copy before delivery),
  ledger-and-session-records (L-425's close, the handoff, Tony's page).
  Confirm each loaded version against the manifest in the repo's
  PROJECT_INSTRUCTIONS.md at HEAD before using it.
- Measure again at HEAD before designing: the counts in section 2 are
  from c5dff25 and the file grows.

## 1. What Tony ruled, 2026-10-12

- Asked which of the three levels to build: "All now."
- On the `# Quote:` line as a fourth level: "Confirmed as long as level
  3 does run." So: no Quote line in this build; level 3 is not optional
  and not a tool that waits to be remembered. Once it runs and shows
  what it can read of each page, the quote idea comes back to Tony with
  that evidence.
- Why, in his words: "I am trying to clear out the scaffolding backlog
  so that once the earth and sun slices are completed we can proceed
  smoothly."

## 2. What was measured at c5dff25 (names, not only counts)

Every row of `constants_new.py` carries its citation as comment lines
below it: `# Source:` (the paper or page), `# Read:` (where in it, and
when, and by whom), `# Access:` (the address and the date it was
opened), `# Cross-checked:` (a worksheet another model wrote). Parsed
with `test_status_lines.parse_rows`:

- 180 rows; 117 carry a Source or a Cross-checked line.
- 62 of the 117 have no Access line. 39 of those carry a doi, an arXiv
  id or an address somewhere else in the block. 23 carry no address of
  any kind, in four classes:
  - the PREM paper, no doi on the line: EARTH_INNER_CORE_KM,
    EARTH_OUTER_CORE_KM, EARTH_D660_DEPTH_KM, EARTH_UPPER_MANTLE_KM;
  - NASA fact sheets named without a link, cross-checked by three
    models in August: MERCURY_RADIUS_KM, VENUS_RADIUS_KM,
    MOON_RADIUS_KM, MARS_RADIUS_KM, PHOBOS_RADIUS_KM, SATURN_RADIUS_KM,
    URANUS_RADIUS_KM, NEPTUNE_RADIUS_KM, PLUTO_RADIUS_KM,
    BENNU_RADIUS_KM, ERIS_RADIUS_KM, HAUMEA_RADIUS_KM,
    MAKEMAKE_RADIUS_KM, ARROKOTH_RADIUS_KM;
  - printed books or papers with a bibcode but no link: CORE_AU,
    CHROMOSPHERE_PHYSICAL_KM, HELMET_CUSP_RADII, ROCHE_LIMIT_RADII;
  - "same page" as another row: EARTH_THERMOPAUSE_ALTITUDE_KM.
- 55 Access lines exist; 7 lack an address or an ISO date on the line:
  EARTH_MAGNETOTAIL_DIAMETER_RADII, RADIATIVE_ZONE_AU,
  INNER_CORONA_RADII, HELMET_CUSP_HIGH_RADII,
  OORT_CLOUD_INNER_EDGE_HIGH_AU, OORT_CLOUD_OUTER_EDGE_LOW_AU,
  OORT_CLOUD_OUTER_EDGE_HIGH_AU. Some say "as <ROW>" (an address
  inherited from another row); some give a bibcode instead of a link.
- 31 sourced rows have no Read line (named by the measuring session's
  run; most are the radii and constants above).
- Record files named on the lines: a simple scan found 7 under
  documentation/ and documentation/worksheets/, all present; the
  October 8 measure found 17, counting worksheets named in parentheses
  on Cross-checked lines. The build's own scan decides the list and
  must read all four line kinds.
- 42 distinct web addresses: ntrs.nasa.gov 4, nssdc.gsfc.nasa.gov 3,
  ssd.jpl.nasa.gov 3, arxiv.org 3, doi.org 3, www.nasa.gov 2,
  ui.adsabs.harvard.edu 2 (ADS refuses automated fetches, measured
  October 9), par.nsf.gov 2, Wiley 2, Springer 2, iau.org 2, and
  singles.
- The planted faults of October 9, against these levels: F3 and F4
  (a renamed record file, a renamed worksheet) are level 1's; F2 (a
  removed Access line) is level 2's; F5 (a dead address) is level 3's.
  F6, a Read line moved to the wrong table, is caught by none; only a
  person reading the page can. Say so in the checker's output, in a
  line, so no one reads a green run as covering it.

## 3. The three checks

### 3a. Level 1: every file a citation names exists. Fails the run.

- Read the four line kinds on every row and resolve every file name
  they carry: a path under documentation/ or documentation/worksheets/,
  a bare worksheet name in parentheses on a Cross-checked line, and
  "as <ROW>" by following it to the named row (which must exist, and
  must not point on in a loop).
- A missing file fails the run and is named: row, line kind, the name
  as written. Today the worksheet checker's layer L0 reports a missing
  worksheet only inside WORKSHEET_CHECK.md (F4); this level puts it in
  the run's summary, by name.
- The export: `constants_export.json` copies these paths (F3). Level 1
  runs before the export in the maintenance run, so a broken path never
  reaches the website; the builder settles the row order.

### 3b. Level 2: every sourced row carries an address with a date. Reported by name first; fails after Tony rules the excused classes.

- An "address" is on the Access line: a link, or a doi, arXiv id or
  bibcode (each is a permanent address; recommended, for Tony to
  confirm), plus the ISO date it was opened. "as <ROW>" inherits the
  named row's address and date.
- The first run REPORTS, by class and by name, every sourced row that
  fails this. From section 2 that is the 23 with no address at all plus
  the 7 malformed Access lines, in five classes; the builder measures
  at HEAD. The classes go to Tony as one list with a recommendation per
  class (section 5). A row with a doi elsewhere in its block is a
  mechanical fix, not an excuse: the patch moves the doi onto an Access
  line with the date the Source line carries.
- Excused rows live in a small data file beside the scanner's own
  `data/provenance_exceptions.json`, as a sibling (keep the scanner's
  file about the scanner): row name, class, the reason in a sentence,
  the date Tony ruled. The checker prints the excused rows by name on
  every run, counted apart from the passing ones, so an excuse is never
  silent. After the ruling, any other row without an address fails the
  run.

### 3c. Level 3: a link check that visits each address. Report-only, and it runs.

- A row of the orrery maintenance run, not a separate tool. It reads
  every address level 2 found, opens each one at most once per run,
  one at a time with a pause, with a plain user agent, and records for
  each: reachable, redirected (where to), refused (ADS), gone, or
  unreachable because the machine is offline.
- A cadence, so most runs ask nothing: an address confirmed within 30
  days is not re-opened. The confirmations live in the orrery's
  `data/`, one entry per address with the date and the answer, the same
  shape the Horizons check is moving to
  (`documentation/HANDOFF_L395_horizons_check_move_brief_20261012.md`,
  section 2). Whichever of the two builds lands first sets the
  convention for a network row of this run: a row that cannot reach
  the internet reports UNREACHABLE by name and is never counted as a
  pass; every other row runs as before. Read that brief and match it.
- Report-only in this build: a dead address is named, the run stays
  green, and the row's own line says so. Tony reads the names. Whether
  it should fail the run is a later ruling, after it has run for a
  while and the false alarms are known (a page that moves, a site that
  refuses robots).
- The quote idea rides on this later: once the check opens pages, what
  it can read of each (the fetch tool's limits were measured October 9:
  a small model, a 125-character cap, the number's printed form varies)
  is the evidence Tony asked for before deciding on a `# Quote:` line.
  This build records what each page returned, nothing more.

### 3d. The audit's domain split travels with the total (added 2026-10-12, Tony's decision in the same chat)

Tony: "the provenance checker is still reporting 288 tier 1 items. Can
we separate this into meaningful groups, like orrery, earth science and
stars in the checker report?" It already is, in `PROVENANCE_AUDIT.md`'s
"Findings by File Type" table (provenance-discipline, Report Domain
Classification); what reaches him is the total alone. At c5dff25: Earth
System 149 in 11 files (three paleoclimate modules carry 112), orrery
125 in 25 files (`shell_configs.py` 35 and `idealized_orbits.py` 29),
stars 12 in 8 files (`exoplanet_coordinates.py` 5), utilities 2, dev
tools and gallery 0. Two fixes, both method, report-only:

- **The split prints wherever the total prints:** the scanner's
  console summary, the maintenance run's summary line, the run history
  (`provenance_history.py`), and the Signals line of
  `documentation/WHERE_WE_ARE.md`, in the form "288: orrery 125, Earth
  System 149, stars 12, utilities 2". Names beside the count, as the
  gate-path line already does.
- **One home for a module's domain.** `provenance_scanner.py` keeps its
  own hand list, `MODULE_DOMAIN_MAP`, while every module but two
  declares `Domain:` in its docstring, in the same six-word vocabulary,
  and `module_atlas.classify_domain` reads it. At c5dff25 the two
  disagree on 12 files (eleven dev tools filed as orrery, and
  `data_acquisition.py`, tagged stars, whose one Tier-1 finding is
  counted as orrery), and 15 files with findings are in no list and
  default to orrery. The scanner reads the docstring tag through the
  atlas's function and the hand list goes; the "Domain coverage gap"
  note then names only a module with no tag, which is the atlas's
  existing coverage-gap meaning. One Value, One Home, on a property.
  The skill's Report Domain Classification section is rewritten to say
  the tag is the store; that rides the same version as 3c's sentence.
- Plant it: a file whose tag and the old list disagree, shown filed by
  its tag; a file with no tag, shown named in the gap. The skill's
  Scanner Mechanics bullet on role-driven inclusion is the model.

Planning reading, for the handoff: the 149 Earth System findings are
stage 14 on the road and off the active path; the orrery's 125 sit
mostly in two files; the stars are nearly clean.

## 4. Build notes (method; the build session settles these and records them)

- One new checker, `test_citation_locations.py`, carrying levels 1 and
  2, and level 3 as a mode (`--links`) the maintenance run calls on its
  own row. Keep `test_status_lines.py` about the status-line grammar;
  it is already eight rules long and its docstring says what it is for.
- Every level plants its faults first, in the checker's own test: a
  renamed record file, a renamed worksheet, a removed Access line, an
  "as <ROW>" pointing at a missing row, a dead address answered from a
  recorded reply (the sandbox cannot reach the web; record the replies,
  never fetch in a test). A Check That Cannot Fail Is Not Passing:
  each fault is shown caught, by name, in the handoff.
- Three rows in the maintenance run, named what they print, in
  CHECKERS' alphabetical place: "Citation files", "Citation
  addresses", "Citation links (network)". Three dashboard buttons with
  the same names (every check keeps its button). If the dashboard
  labels build has landed, its parity check will insist on this.
- The run's summary line names what moved, not a count: the files
  missing, the rows without an address, the addresses that died.
- `provenance-discipline` says the scanner checks that a citation sits
  near a number, not where it points. Add one sentence naming this
  checker as the place that does; one version, under One Session, One
  Bump, with the protocol entry and the manifest run in the same
  commit.
- Docstring stamps on every edited module; L-425 closes with its loose
  ends re-homed (the quote question stays open on L-425 itself, as a
  Gap waiting on level 3's first runs, or moves to a new item: the
  builder's call, said in the handoff).
- What is permanent after the patch is spent: the checker and its
  tests, the excuse file, the link-confirmations record in `data/`, the
  three run rows and buttons, the skill sentence; and from 3d, the
  domain split on every line that prints the total, and the scanner
  reading the docstring `Domain:` tag.

## 5. For Tony, one at a time, in the build session

- (decide) **The excused classes for level 2**, from the list the
  checker prints at HEAD. Recommended: a doi, arXiv id or bibcode on
  the Access line counts as an address (so the 39 rows with one
  elsewhere are fixed by the patch, not excused); a printed book with
  no digital copy is excused by class with its page or section on the
  Read line; a NASA fact sheet is NOT excused -- it has an address, and
  the patch adds it; "same page" rows inherit.
- (decide) **Level 3's cadence.** Recommended 30 days, matched to the
  Horizons check, so the two network rows share one rhythm.
- (decide, recorded, not urgent) **Whether a dead address should fail
  the run**, after level 3 has run for a few weeks.

## 6. Tony's actions, all of them

- (do) Push `patch_L401_4` first; then the dashboard build if it comes
  first in your order; this build sits on that HEAD.
- (do) Start the Opus session from this brief, when it comes in your
  order.
- (decide) The items in section 5, in that session.
- (do) Run the patch and the maintenance run; read the three new rows'
  names, the first level-2 list, the first level-3 answers, and the
  Tier-1 total with its split beside it; push.

Brief written October 2026 with Anthropic's Claude Fable 5.1.
