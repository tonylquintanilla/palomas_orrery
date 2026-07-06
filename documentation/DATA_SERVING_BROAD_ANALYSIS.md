# Data Serving Architecture — Broad-First Analysis

**Type:** DESIGN SESSION deliverable (zero code)
**Author:** Claude Fable 5, via collegial relay (Opus 4.6 prompt, Tony carrying)
**Date:** July 5, 2026
**Base:** main @ `993dfd501db7ace21f34952771e73e373bd1ad46`, gallery @ `a6420bc26eb05885ce3413153a227a6ce654a529`
(SHA round trip confirmed via `git ls-remote` at session start. Note: the task
prompt cites older bases `72e5587` / `89c8bf30` — both repos have moved since
the prompt was written. This analysis is built on the current HEADs Tony stated.)

**Inputs read in full:** `MASTER_PLAN_INTERACTIVE_GALLERY.md` (v8, all
sections), `FABLE_TASK_DATA_SERVING.md`, `DATA_INVENTORY.md`,
`celestial_objects.py` (190 `OBJECT_DEFINITIONS` entries at upload:
70 orbital, 48 satellite, 39 trajectory, 11 exoplanet, 10 Lagrange,
7 barycenter, 5 exo-star/barycenter, 1 hypothetical, 1 fixed — counted by
grep, not recalled).

**Provenance convention in this document:** numbers derived from the uploaded
inventory or counted from the uploaded catalog are marked *(inventory)* or
*(counted)*. Arithmetic estimates are marked *(est.)* and show their inputs.
Claims about external service behavior that I could not fetch from this
sandbox are collected in §9 as a Phase 0 verification checklist — they are
believed-true-from-training, which per protocol means **verify before
load-bearing use**. One claim was fetched live and is marked *(fetched)*.

---

## §0 — Reframing Findings (read these first)

Five findings change the shape of the problem before any approach is compared.

### F1. The monolith's death dissolves the size crisis

The 130.4 MB figure that framed this problem was the *desktop* cache: 1,501
object/center pairs *(inventory)* accumulated across every center combination
the desktop GUI ever plotted. The web catalog does not need that matrix. The
byte math (worked in F3) says a restructured full-catalog web cache is roughly
**35–40 MB as compact JSON, ~10 MB gzipped, ~12 MB as binary float arrays**
*(est.)*. That fits comfortably inside *any* of the candidate homes — gallery
repo headroom (588 MB *(inventory)*), a dedicated repo, Releases, or R2.

**Consequence:** storage ceiling is *not* the discriminator between
approaches. The real discriminators are operational burden, git-history
growth, update latency, and failure modes. The comparison matrix in §1 is
weighted accordingly.

### F2. The pair matrix can collapse to per-object canonical vectors

1,501 pairs exist because the desktop lets any object be plotted from any
center, and the cache keyed on the *pair*. But a position relative to center
C is a vector subtraction of two positions in a common frame:

```
r(object ← C) = r(object ← Sun) − r(C ← Sun)
```

If the web cache stores **one canonical trajectory per object**, the assembler
derives any center on the fly. 1,501 pairs → ~190 object files *(counted)*.
The coverage index simplifies from a pair matrix to an object list + a frame
rule ("any center that is itself in the catalog and covers the same dates").
This is a design option, not a mandate — but it is the single largest
simplification available, and it interacts with every serving approach below
(fewer files, smaller batch, simpler index).

**Precision rule (the one caveat).** Subtraction in heliocentric coordinates
is numerically fine in float64 (moon offsets ~1e-3 AU against ~AU-scale
coordinates leaves ~12 significant digits of headroom). It is **not** fine in
float32: 7 significant digits at Jupiter's 5.2 AU is ~150 km of noise,
comparable to inner-moon orbital detail. So the storage rule is:

- **Planets, dwarfs, asteroids, comets:** store heliocentric.
- **Moons:** store **parent-relative** (their natural, small-magnitude frame);
  the assembler composes heliocentric = parent-helio + moon-relative when a
  wide view needs it. This preserves precision *and* yields both frames.
- **Spacecraft:** store per mission arc in the arc's natural center
  (heliocentric cruise, planet-relative near encounters — which is how
  Horizons serves them anyway).

### F3. The size math, by object class *(est.)*

Point cost basis: a compact JSON point `[jd, x, y, z]` ≈ 80–100 bytes; raw
float64 binary = 32 bytes; gzipped JSON ≈ 25–30 bytes on the wire. Populations
are *(counted)* from `celestial_objects.py`; windows are illustrative.

| Class | Objects | Step | 3-yr window points | JSON | float64 bin |
|---|---|---|---|---|---|
| Heliocentric orbital (planets, dwarfs, asteroids, comets) | 70 | 1 day | 1,096/obj | ~7.7 MB | ~2.5 MB |
| Moons (parent-relative) | 48 | 6 h | 4,383/obj | ~21 MB | ~6.7 MB |
| Spacecraft arcs (write-once) | 39 | varies | ~2,000/obj avg | ~7.8 MB | ~2.5 MB |
| **Total** | **157 served** | | | **~36 MB** | **~12 MB** |

Exoplanets, Lagrange points, barycenters, and the hypothetical either compute
analytically or ride on existing data — negligible additions. A 10-year
*accumulating* window scales the first two rows ×3.3 → ~100 MB JSON / ~33 MB
binary — still repo-viable with compression, and R2-trivial. A *sliding*
window keeps the table flat forever.

### F4. Git history is the hidden cost of repo-based serving

GitHub's ~1 GB soft ceiling counts the **repository including history**, not
just the working tree. A weekly batch that rewrites ~120 data files commits
new blobs every week; even delta-compressed, a rolling cache plausibly adds
tens of MB of history per year, forever *(est. — mechanism certain, rate
approximate)*. Three mitigations exist, and they differentiate the approaches
in §2:

1. **Append-only sharding** — split each object's data by calendar year;
   only the current-year shard ever changes. Past shards are write-once.
2. **Orphan-branch publishing** — the batch force-pushes a single-commit
   orphan branch (or the `gh-pages` branch) each run; history stays one deep.
   Standard practice for generated-content deployment.
3. **Get out of git** — Releases assets and R2 objects carry no history.

### F5. `pyarrow` is in Pyodide — with a version-flap warning *(fetched)*

Fetched from the Pyodide changelog this session: `pyarrow` was added at
18.1.0, was *accidentally missing* from 0.27.0, was **disabled in 0.28**, and
was re-enabled at 22.0.0. Parquet is therefore viable for the star cache —
but its availability has flapped across Pyodide releases. Whatever format is
chosen, **pin the Pyodide version** the gallery loads from CDN and treat
Pyodide upgrades as tested events, not automatic ones. (NumPy's availability
has never flapped; `.npz`/`.npy` is the conservative choice — see §5.)

---

## §1 — Comparison Matrix

Approaches A–H against the dimensions that still discriminate after F1.
Sizing assumes the restructured ~36 MB catalog (F3). "Ops burden" is Tony's
recurring cost per update cycle; "history growth" per F4.

| # | Approach | Where data lives | Ops burden per cycle | History growth | User fetch latency | Growth ceiling | New services | Failure modes |
|---|---|---|---|---|---|---|---|---|
| A | Per-object files in **gallery repo** | `tonyquintanilla.github.io/cache/` | commit+push (1 script) | grows in the repo that also hosts the gallery | same-origin, fast | shares 588 MB headroom with gallery growth | none | history bloat squeezes gallery; one repo = one blast radius |
| B | **Dedicated data repo** + Pages | new `palomas-orrery-data` repo | commit+push (same script, different remote) | isolated; orphan-branch reset trivially safe | cross-origin (CORS — §9) or same-origin under custom domain (§9) | own 1 GB, fully dedicated | none (one more repo) | third repo to remember; CORS if custom-domain path claim fails |
| C | **Orrery repo** project Pages | `palomas_orrery/docs/cache/` or gh-pages branch | commit+push into the code repo | pollutes the *code* repo's history | as B | shares 1 GB with future code/docs | none | data churn tangles with code history; un-gitignoring reverses a deliberate decision |
| D | **GitHub Releases** | release assets on orrery repo | API upload per asset (scriptable) | zero (no history) | redirect hop; not path-addressable by pattern | effectively unlimited (2 GB/asset) | none | asset-update workflow clunky for weekly rolls; URL scheme awkward for per-object fetch |
| E | **R2 / external CDN** | Cloudflare R2 bucket | `rclone sync` (1 command) | zero | CDN-fast, proper caching headers | 10 GB free tier | Cloudflare account, token, domain config | external dependency; token rot; one more dashboard |
| F | **jsDelivr layer** over A/B/C | same repo as A/B/C, served via jsDelivr | none extra | as underlying repo | CDN-fast | ~20 MB/file limit *(§9)* | none (public CDN) | cache staleness window (~hours–1 day); third-party availability |
| G | **GitHub Actions batch** (automation, orthogonal) | writes into A/B/C/D/E | ~zero after setup (scheduled) | as target | as target | as target | Actions workflow to maintain | CI debugging is its own skill; silent failure risk; moves Horizons query off Tony's desktop |
| H | **Curated subset only** (fallback) | gallery repo, few MB | export per curation | negligible | fast | tiny | none | *is the limitation the interactive gallery exists to overcome* |

Reading the matrix: **B is the strongest single-store option** (isolation +
own ceiling + orphan-branch safety at zero new services). **E is the strongest
if growth or freshness ever exceeds repo comfort.** **D is the natural home
for write-once tiers** (spacecraft arcs, Tier-2 specials) even if something
else serves the hot data. A, C, F, G are modifiers more than destinations.
H is the Pyodide-fails fallback the master plan already names.

---

## §2 — Detailed Analysis by Approach

### A. Per-object files in the gallery repo

The minimal-motion option: a `cache/` directory beside `gallery/`, one file
per object (per F2), pushed by the same batch that already talks to the
gallery repo. The coverage index is one more JSON file listing objects, date
spans, and steps.

**Workflow:** weekly desktop script → write `cache/*.json` → `git add/commit/
push` — one script, one remote Tony already uses daily.

**Numbers:** ~36 MB *(est.)* against 588 MB headroom *(inventory)* — 6% of
remaining space at start. But F4 applies to the *shared* repo: two years of
weekly rolls could add low hundreds of MB of *history* to the repo that also
must absorb gallery growth (and the top-10 re-exports will shrink working
tree, not history). Orphan-branch reset on the gallery repo is riskier than
on a dedicated repo because the gallery's own history has value.

**Verdict shape:** fine to *start* (Phase 2 could ship this in an afternoon),
with a known migration path out when history growth shows up in the repo-size
check. If chosen, adopt append-only year shards (F4.1) from day one to slow
the bleed.

### B. Dedicated data repo (`palomas-orrery-data`) with Pages

A third repo whose *only* content is the served cache + coverage index. Pages
enabled; the batch pushes here.

**Why the isolation matters:**
- History growth is contained where it harms nothing; the publish step can
  force-push a single-commit orphan branch every cycle (F4.2) and the repo
  stays permanently tiny. This is safe *precisely because* the repo holds no
  hand-authored history — the desktop cache remains the source of truth and
  the repo is a projection of it.
- Its 1 GB ceiling is 100% data. An accumulating 10-year window (~100 MB
  JSON) never threatens it.
- The gallery repo and orrery code repo stay exactly as they are — no
  un-gitignoring, no churn in repos with meaningful history.

**Origin question:** GitHub serves project sites of a user with a custom
domain *under that domain's path* — i.e., the data would appear at
`palomasorrery.com/palomas-orrery-data/...`, **same-origin with the gallery**,
making CORS moot. This is the believed behavior; it is checklist item §9-1.
If it holds, B has A's same-origin fetch simplicity with none of A's blast
radius. If it fails, cross-origin fetch requires the ACAO header (§9-2),
which GitHub Pages is believed to send.

**Cost:** one more repo in the mental model, one more remote in the batch
script. That is the whole cost.

### C. Orrery repo's own Pages

Serving from the code repo means either un-gitignoring data into `main` (data
churn interleaved with code history — the worst of F4) or publishing to a
`gh-pages` branch (better: the orphan-branch trick works there). But once the
publish target is a disposable branch, the code repo is contributing nothing
except *not being a new repo* — and it pays for that by coupling a
data-publish force-push workflow to the repo where a mistake matters most.
The deliberate gitignore decision exists for a reason. B dominates C on every
axis except "number of repos."

### D. GitHub Releases

Already the star cache's distribution path — proven in this project.
Release assets are served from GitHub's asset CDN and are believed to be
fetchable cross-origin by browser code (§9-3).

**Where it shines:** *immutable* data. A spacecraft arc never changes after
the mission ends; a Tier-2 curated special (encounter, perihelion) is
write-once/read-forever by definition (§1 of the master plan). A
`cache-archive` release holding these as assets costs zero repo bytes, zero
history, and never needs re-upload.

**Where it strains:** the weekly roll. Updating an existing asset means a
delete-and-reupload via API per file, and asset URLs don't form the clean
path hierarchy a coverage index would like to template. Releases as the *hot*
path would make the batch script the most complex thing in the system —
backwards.

**Verdict shape:** not the primary serving path; a strong *archival tier*
inside a hybrid (§7).

### E. Cloudflare R2

10 GB free, zero egress fees, real CDN semantics, cache-control headers Tony
controls. The batch step is `rclone sync local-cache/ r2:bucket/` — arguably
*less* operational surface than a git commit (no history, no merge states,
idempotent).

**The honest cost is categorical, not technical:** it is the first piece of
project infrastructure that is neither Tony's desktop nor GitHub. A token to
rotate, a dashboard to remember, a bill (of $0) to have an account for, a
custom-domain DNS config if pretty URLs are wanted. The protocol's own lesson
applies — *"route around the store you don't control to the one you do"* —
and R2 is a store Tony controls less than a repo, in the governance sense,
even though it behaves better technically.

**When it becomes right:** if the window accumulates for years, if per-user
fetch latency ever matters (classroom scenarios, L-095), or if star + orbit +
future domains push total served data past repo comfort. The good news: F2's
per-object layout is *identical* on R2 and on Pages — same files, same paths,
same coverage index. Migration is a re-point of one base-URL constant. R2 is
a graduation, not a fork.

### F. jsDelivr as a CDN layer over any repo

`cdn.jsdelivr.net/gh/user/repo@branch/path` serves repo files with CDN
caching and CORS. It layers over A, B, or C at zero setup cost, converting
"GitHub Pages speed" into "CDN speed" for repeat global fetches. Constraints
believed from training (§9-4): a per-file size cap (~20 MB — irrelevant at
per-object file sizes) and a cache-refresh lag of hours against a moving
branch. For weekly data, the lag is immaterial; pinning fetch URLs to the
publish commit's SHA (which the batch knows) makes it exactly zero. This is
a one-line enhancement, not an architecture.

### G. GitHub Actions scheduled batch (the automation question)

Orthogonal to *where* data lives; it changes *who runs the roll*. A scheduled
workflow: astroquery → Horizons (sequential, one request at a time — the
same JPL-compliant pattern as the desktop; this is CI fetching data, not a
website embedding the API) → write per-object files → publish to B/D/E.
Tony's recurring burden drops to reading a failure email.

**Genuine tradeoffs, per the solo-developer constraint:**
- *For:* removes the "remember to run it" failure mode entirely; the roll
  happens on vacation weeks too.
- *Against:* the prompt's own warning — complex CI/CD is worse than a simple
  script. Actions debugging is a skill with its own drift; a silently-failing
  cron is a *stale cache that looks fine*, the exact failure class this
  project's protocol exists to catch. And it moves the Horizons query off the
  desktop loop that currently makes repo HEAD trustworthy by construction.
- *Middle path:* keep the batch a plain local script for Phase 2; the script
  is written so that wrapping it in a 20-line workflow later is mechanical.
  Automate only after the manual loop has run long enough to trust its
  output shape. If automated, the coverage index gets a `generated_at`
  timestamp and the interactive page surfaces data age — staleness made
  visible instead of silent.

### H. Curated subset (the floor)

Ship only preset-backing data. This is not a serving architecture; it is the
already-named fallback if Pyodide fails Phase 0 ("pre-computed library only").
Its real value in this analysis: it defines the **minimum viable cache** —
whatever Phase 2's first interactive page offers must be servable even in
this mode, so the presets' data footprint (a few MB) is the floor every other
approach builds above.

---

## §3 — The Planet/Satellite Split: Three Data Classes, Not Two

The prompt frames a binary split; the catalog *(counted)* actually yields
three serving classes with different physics and different lifecycle:

**Class 1 — Analytic-capable (planets, dwarf planets; ~15–20 objects).**
`idealized_orbits.py` computes the orbit *shape* from elements, and
position-on-date is a Kepler solve. Cached vectors add dated precision.
**Serving consequence:** these could ship as *elements only* (bytes, not
kilobytes) with cache as enhancement — the one class where "no data fetched"
still renders honestly.

**Class 2 — Elements-degrading (asteroids, comets; ~50 of the 70 orbital).**
Osculating elements exist but drift — multi-body perturbation for asteroids,
non-gravitational forces for comets near perihelion (the project's own
horizons-orbital-mechanics territory). An ideal ellipse is an honest *orbit*
but a dishonest *position* far from epoch. **Serving consequence:** cache
required for position accuracy; elements acceptable for shape-only display if
the hover says so (the Show-the-Envelope rule: approximate and say so).

**Class 3 — Trajectory-is-the-data (48 moons + 39 spacecraft *(counted)*).**
No analytic shortcut exists. Moons need fine steps (hours, not days — a 6-h
step on Io's 1.77-day period gives ~7 points per orbit, marginal; inner moons
may want finer, see OQ-4). Spacecraft arcs are **write-once**: a completed
mission's trajectory never changes, which moves spacecraft out of the rolling
problem entirely and into the archival tier (§2-D). Active missions
(Tier-2-like) extend by appending arcs, not rewriting.

**Coverage index consequence.** The index needs a per-object availability
mode, not a boolean:

```
availability: "cached" | "analytic" | "analytic_approx" | "unavailable_for_dates"
```

The GUI-declares-the-envelope principle then extends naturally: a planet
outside the cache window can still be *offered*, rendered analytically, and
labeled; a moon outside the window is *not offered*. Honest boundaries per
class instead of one envelope for all.

---

## §4 — The Rolling Cache Design

### Window geometry *(est., inputs from F3)*

| Window policy | Orbital (daily) | Moons (6-h) | Total JSON | Character |
|---|---|---|---|---|
| Sliding −1 yr / +3 mo | 3.2 MB | 8.8 MB | ~12 MB + arcs | flat forever; recent-only exploration |
| Sliding −2 yr / +6 mo | 6.4 MB | 17.5 MB | ~24 MB + arcs | flat; covers "what did that look like last year" |
| Accumulating from 2024 | +2.6 MB/yr | +7 MB/yr | ~10 MB/yr growth | history becomes an asset; ~100 MB at year 10 |
| Split policy | accumulate | slide | ~7 MB/yr growth | planets cheap to keep forever; moons windowed |

The split policy is attractive: heliocentric orbital data is so cheap that
discarding it saves nothing worth saving, while moon data is 3× the volume
for exploration value that decays faster (moon geometry repeats on
days-to-weeks periods — last year's Io position teaches nothing this month's
doesn't). Spacecraft arcs accumulate by nature (write-once).

### Forward padding and cadence

Ephemerides for planets and moons are excellent months ahead. Padding the
window **+90 days** means a *monthly* batch never serves stale "today" data
even if a run is skipped — two consecutive missed months before the current
date falls off the edge. Cadence recommendation space:

- **Weekly:** freshest, highest history churn (F4), most Tony-cycles.
- **Monthly + 90-day pad:** the comfortable default for visualization
  purposes; "today" is always covered with margin.
- **Event-driven Tier-2:** encounters/perihelia are fetched when curated,
  independent of the roll — already the master plan's model.

The coverage index carries `window_start`, `window_end`, `generated_at` per
object class; the interactive page's date picker reads its bounds from there
(the envelope, again).

### How each approach absorbs the roll

- **A/B/C (repos):** with append-only year shards, a roll touches only
  current-year shards (~157 files) plus the index. With orphan-branch
  publishing (B), history cost is zero regardless.
- **D (Releases):** hostile to rolling (per-asset re-upload); archival only.
- **E (R2):** `rclone sync` uploads only changed objects; rolling is R2's
  best case.
- **Format note:** sharding by year also caps single-file size (a 6-h moon
  year ≈ 143 KB JSON *(est.)*), keeping every file far below any CDN or
  practical fetch limit, and letting the browser cache past years
  indefinitely (immutable files → aggressive cache headers).

---

## §5 — The Star Cache Format

31.1 MB pickle, 20 parallel columns, mixed numeric/string *(inventory)*.
Unlike orbit data, stars serve as **one whole-catalog load** (HR diagram and
planetarium consume the full set), so granularity doesn't apply — format and
location are the whole question.

| Format | Pyodide load path | Est. size at rest | Notes |
|---|---|---|---|
| Parquet | `pyarrow` — present, but has flapped (F5 *(fetched)*) | ~12–18 MB *(est.)* | best compression of mixed columns; requires Pyodide version pinning |
| `.npz` (NumPy archive) | `numpy` — never flapped | ~15–22 MB *(est.)* | numeric columns native; unicode string arrays supported; the conservative choice |
| Gzipped column-JSON | stdlib | ~10–15 MB wire, ~60 MB inflated in memory *(est.)* | universal; highest memory footprint on a phone |
| CSV | pandas | poor | no — types lost, size worst |

**Interaction with serving location (the prompt's actual question):** at
12–22 MB, the star catalog fits *any* home — this is F1 again. Location does
not force the format. The real coupling runs the other way: **Pyodide's
package surface constrains format**, and F5 says the safest dependency set is
numpy-only. Recommendation shape for the Phase 3 decision (§7 #8 stays
deferred, as instructed): prototype `.npz` first, hold Parquet as the
optimization if `pyarrow`'s presence is verified against the *pinned* Pyodide
version. Serve it beside the orbit cache, wherever that lands — one home for
all served data keeps the batch script and the mental model unified.

---

## §6 — The `graph_objects` Question (briefly, as asked)

Is a JSON-emitting assembler worth exploring? **Not for v1, and data serving
does not change that calculus.** The constraint list already fixes full
`plotly` in Pyodide; the master plan already notes the gallery serves 30 MB+
files acceptably; and Phase 0 measures the true cold-start number. Data
serving is orthogonal — every approach in §2 delivers the same bytes to the
same assembler. The only linkage worth recording: if Phase 0's measurement
*fails*, the fallback is the pre-computed library (approach H as the whole
architecture), not an engine rewrite — so no serving decision made now is
invalidated by that branch. Park the JSON-emitter idea as a possible
far-future optimization with a real cost (rewriting engines against 88+
`go.*` call sites in one module alone) and no current forcing function.

---

## §7 — Combinations Worth Considering

Three named hybrids, each a complete workflow Tony could run:

### H1 — "One data home" (B, with D for archives)

Dedicated `palomas-orrery-data` repo, Pages enabled, orphan-branch publish.
Hot Tier-1 (planets, moons, active missions) + star catalog + coverage index
all live here. Completed spacecraft arcs and Tier-2 specials graduate to a
Releases archive on the same repo when they freeze (or simply stay in the
repo — at their size, graduation is optional hygiene, not necessity).

*Workflow:* monthly desktop script → write local canonical cache → export
per-object year shards + index → force-push orphan branch. One script, one
remote, zero new services, zero history growth.
*Character:* the maximum-simplicity endpoint of the all-GitHub path.

### H2 — "Gallery-first, graduate later" (A → B/E migration path)

Start in the gallery repo's `cache/` for Phase 2 speed (the batch script and
the first interactive page ship against same-origin paths with no new repo).
Adopt year shards from day one. When the repo-size check first shows history
pressure — or when Phase 3 adds the star catalog — lift `cache/` unchanged
into B or E and re-point one base-URL constant.

*Workflow now:* identical to today's gallery push.
*Character:* lowest activation energy; deliberately incurs one planned
migration. Honest cost: migrations planned in year one have a way of being
executed in year three.

### H3 — "Repos for pages, R2 for data" (E primary)

All served data (orbit + star + future domains) in one R2 bucket behind
`data.palomasorrery.com`; repos carry only code, pages, and curated gallery
JSON. Batch ends in `rclone sync`.

*Workflow:* monthly script → local cache → export → `rclone sync`. Simplest
publish step of all three; the cost is the external account (§2-E).
*Character:* the right endpoint if accumulation, freshness, or multi-domain
growth ever outruns repo comfort — and reachable from H1 or H2 by re-pointing
the same base-URL constant, because the file layout (F2, year shards, index)
is identical everywhere.

**The load-bearing observation across all three:** F2's per-object layout +
year shards + a coverage index with a single base URL makes the serving home
a *configuration value*, not an architecture. The decision Tony actually
locks in Phase 2 is the **file layout and index schema**; the home can
graduate. That is the decision to spend the design care on.

---

## §8 — Open Questions for Tony

Judgment calls this analysis cannot make:

**OQ-A. Web catalog scope.** Serve all 157 positional objects (70 orbital +
48 moons + 39 spacecraft *(counted)*), or a curated first tranche (planets +
major moons + flagship missions)? The bytes say "all" is affordable (F3); the
curation question is whether every small moon *earns its place* in the
interactive envelope ("no element NEEDS to exist; it earns its place by what
it teaches").

**OQ-B. Window policy.** Sliding, accumulating, or split (accumulate cheap
heliocentric, slide expensive moons)? §4's table gives the costs. This is
partly a vision question: is the interactive gallery a *now* instrument or a
*time machine*?

**OQ-C. Cadence and automation.** Monthly manual script with +90-day pad
(recommended starting point), weekly, or GitHub Actions from the start
(§2-G's tradeoffs)? Where does "remember to run it" sit against "trust a
cron"?

**OQ-D. Moon step size.** Is 6 h honest for the inner moons (7 points per Io
orbit)? Options: finer step for short-period moons (bytes are affordable), or
per-object step in the index (`step_hours` per entry — the index already
wants per-object metadata). A Mode 5 question in the end: Tony's render of a
6-h Io orbit decides.

**OQ-E. The third repo.** Is a dedicated data repo (B/H1) acceptable to the
mental model, or does the two-repo world have value worth A/H2's history
tradeoff?

**OQ-F. Canonical-frame collapse (F2).** Adopt per-object canonical storage
with assembler-side center derivation, or preserve per-pair files for
fidelity to the desktop cache's shape? F2 is the recommendation, but it makes
the web cache *structurally different* from the desktop cache, and the
export step becomes a real transform rather than a split. (Note: the desktop
monolith is already gone *(inventory)* — the new desktop format could adopt
the same canonical shape, unifying both.)

**OQ-G. Precision/format v1.** Compact JSON (readable, debuggable, gzip
handles the wire) vs binary `.npy` shards (3× smaller at rest, needs numpy
anyway)? Recommendation: JSON for v1 — debuggability during assembler
development is worth 3×, and the layout permits a format column in the index
later.

---

## §9 — Phase 0 Verification Checklist (believed-true, not fetched)

Per fetched-not-recalled, these claims are load-bearing somewhere above and
could not be verified from this sandbox. Each is a five-minute check during
Phase 0:

1. **Project sites under a custom domain:** a project site of the account is
   served at `palomasorrery.com/<repo>/...` (same-origin with the gallery).
2. **GitHub Pages sends `Access-Control-Allow-Origin: *`** (matters only if
   #1 fails or B is hosted without the custom domain path).
3. **Release asset downloads are CORS-fetchable** from browser JS (matters
   for the D archival tier).
4. **jsDelivr `gh` limits:** per-file cap and branch-cache refresh lag
   (matters only if F is adopted).
5. **GitHub Pages serves gzip/brotli transfer-encoding for `.json`** (the
   wire-size numbers in F3 assume yes).
6. **`pyarrow` present in the *pinned* Pyodide version** (F5 verified it
   exists in the project's main line; the pinned-version check is the one
   that counts).

---

## One-Shot Closing Note

If this is the last Fable session: the single most consequential idea in this
document is **F2 + §7's closing observation** — store one canonical
trajectory per object, shard by year, front it with a coverage index that
carries a base URL, and the serving home stops being an architectural
commitment. Phase 2 should design the **layout and index schema** with full
care and pick the *home* with almost none, because the home is revisable and
the layout is not. Everything else here is costed options for Tony's
judgment, per protocol.

Unresolved items are OQ-A through OQ-G plus checklist §9, carried to
Opus 4.6/4.8 at the Phase 0 → Phase 2 transition alongside the existing
DD-1..8 / OQ-1..6 from the Phase 1 vocabulary.

---

*Built on main @ `993dfd5`, gallery @ `a6420bc` (round trip confirmed at
session start). Analysis by Claude Fable 5, July 5, 2026, for collegial
relay. Tony carries context and holds commit authority.*
