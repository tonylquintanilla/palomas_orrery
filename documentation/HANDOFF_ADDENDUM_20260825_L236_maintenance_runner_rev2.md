# HANDOFF ADDENDUM rev 2 -- 2026-08-25 -- L-236, the gallery maintenance runner

**Orrery: `4ad78a01a642166cb70218ae5728aa6f6c39d7f4`**
(https://github.com/tonylquintanilla/palomas_orrery, branch main).
**Gallery: `88633707ce55288bd4a7e03c59513655b3f4a8f3`**
(https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Both trees downloaded at those exact SHAs and read on disk.

**Supersedes rev 1** (`HANDOFF_ADDENDUM ... L-236`, same date). Rev 1 is
still a valid session record; its roster is not. Companion to
`HANDOFF_20260825_L234_sun_done_earth_next.md`.

**Type: DESIGN. Nothing is built.** A spec to affirm or redirect, not a
manifest to execute.

---

## What changed in this revision, and why it is left visible

Rev 1 opened by saying every path and roster entry had been verified
against the bytes. Most had. Four had not, and all four are the kind
that pass a reading and fail a run.

**1. `smoke_framing.js` does NOT read its payload from `__dirname`.**
Rev 1 said the first two Node suites both do. `smoke_features.js` does,
at lines 31 and 109. `smoke_framing.js` line 32 is a bare
`fs.readFileSync("payload_jupiter_saturn.json", "utf8")`, resolved
against the WORKING DIRECTORY. Launched from the repo root, which is
what rev 1's own design recommends, that row throws ENOENT on the first
run -- and rev 1 had already declared in advance that a throw there "is
a real failure and should read as one." The runner's first red would
have been a launch-directory bug wearing the costume of a broken
renderer.

**2. `assert_structural` takes TWO arguments.** Rev 1 described calling
it "against `data/solar-system/coverage_index.json`", which is a
one-argument framing. The signature at `tools/gallery_cache_builder.py`
line 1118 is `assert_structural(index, staging)`, and `staging` does
real work: line 1143 checks that each object's positions file exists,
line 1149 loads its raw vectors. Called with one argument it is a
TypeError; written around, the wrapper silently stops checking the two
things most worth checking.

**3. The artifact-1 test cannot be launched by path.** Rev 1 lists it as
`gallery/assembler/tests/test_artifact1_earth.py`. Its own docstring
says otherwise, and its imports confirm it: `from assembler.catalog
import Catalog` is absolute, so it must run as a MODULE from the
`gallery/` directory:

    cd gallery
    python3 -m assembler.tests.test_artifact1_earth

Run as a script it raises ImportError before reaching any check. This is
the row rev 1 called "the whole point."

**4. The borrowed `run_tool` cannot launch Node.** `maintenance_run.py`
line 385 is `[sys.executable] + argv_tail`. Three of the seven checker
rows are `node`. Borrowing the shape wholesale leaves the roster unable
to express nearly half of itself.

Number 3 is the one that reorganizes the design, and it is treated on
its own below.

---

## Why the gallery gets its own runner

Unchanged from rev 1 and still right. Every input the runner reads lives
in the gallery. Extending the orrery's runner across the repo boundary
would make it depend on a sibling directory that exists only on Tony's
machine, and a checker that cannot find its target skips quietly -- this
session found three separate instances of that exact failure, so adding
a fourth by construction is the wrong direction.

The real objection to a second runner is that two things are harder to
remember than one. The answer is the dashboard button, not a shared
script.

---

## The structural correction: the roster needs a per-row working directory

The orrery's runner takes ONE `project_dir` and passes it as `cwd` to
every tool (line 386). That works there because every orrery tool
launches from the same place.

**The gallery's tools do not agree about where they run.** Measured at
`88633707`:

| Tool | Must launch from | Why |
|---|---|---|
| `module_atlas.py` | repo ROOT | `main()` defaults `project_dir='.'`, writes both outputs to the working directory, and `SCAN_PATHS = ['.', 'tools', 'gallery/assembler', ...]` are relative to it |
| `tools/test_gallery_cache_builder_offline.py` | anywhere | resolves its config via `Path(__file__).parents[1]`; its `import gallery_cache_builder` works because sys.path[0] is the script's own directory |
| artifact-1 test | `gallery/` | absolute package imports; run with `-m assembler.tests.test_artifact1_earth` |
| `smoke_framing.js` | `documentation/` | bare relative payload read, unless fixed (see below) |
| `smoke_features.js`, `smoke_sun_shells.js` | anywhere | payloads via `__dirname` or argv |

So the roster carries a per-row launch directory, defaulting to the repo
root, plus a per-row interpreter so a Node row can exist. That is two
small departures from the orrery's shape, and they are forced by the
repo, not chosen.

**Rev 1's instruction "do not invent a second idiom" is right about the
OUTPUT and wrong if applied to the launcher.** The summary table, the
timed rows, the gating headline and the report-only quoting should be
indistinguishable from the orrery's. The thing that starts the
subprocess is not part of what a reader learns.

**And rev 1's path recommendation needs one sentence added.** Resolving
the runner's own paths from `REPO_ROOT = Path(__file__).resolve().parent.parent`
is correct and should stand. It protects the runner's paths. It does
NOT protect its children's, because a subprocess inherits a working
directory, not a variable. `module_atlas.py` launched with the wrong cwd
writes the atlas into `tools/` and scans the wrong tree, and nothing in
`__file__` resolution prevents it. Pass `cwd` explicitly on every row.

---

## Where it goes

`tools/gallery_maintenance_run.py` in the GALLERY repo -- where every
other gallery devtool lives and where the dashboard already points.

---

## The dashboard button

Verified at orrery `4ad78a01`: `palomas_orrery_dashboard.py`, group
`"Gallery & Web"` at line 138, using `GALLERY_REPO_DIR` (line 62) rather
than `GALLERY_TOOLS_DIR` (line 57). The comment at lines 59-61 records
why the cache builder needs the repo root, and the same reasoning
applies here. Entry shape matches the rows already present -- a 4-tuple,
with an optional 5th `True` for tools needing their own console:

    ("Gallery Maintenance Run",
     "tools/gallery_maintenance_run.py",
     "Generators then checkers for the gallery repo",
     GALLERY_REPO_DIR),

That is an orrery-side patch. It is the smaller half and it is what puts
the runner in the routine rather than in a folder.

---

## The shape, borrowed

Follow `maintenance_run.py`: two roster tables, GENERATORS then CHECKERS,
a timed row per tool, a headline counting gating checkers, report-only
rows quoted separately. Three properties of the original, all verified
in place and all worth keeping:

**A fourth field marks a row REPORT-ONLY** -- line 477,
`report_only = entry[3] if len(entry) > 3 else False`. Omitting it means
the row gates, which is the safe default for anything added later.

**A verdict hint names a substring** -- line 479,
`line_containing(output, hint)`, falling back to `last_meaningful_line`
at line 489 when no hint is given.

**`print_files_written`** (line 289) reports what the run changed, so a
generator that rewrites identical bytes says so rather than looking like
work.

---

## GENERATORS

| Row | Tool | cwd | Writes |
|---|---|---|---|
| Module atlas | `module_atlas.py` | repo root | `MODULE_ATLAS.md`, `MODULE_INDEX.md` |

One row, and that is the honest count today. The gallery has no ledger,
no skill manifest and no data inventory of its own.

---

## CHECKERS

| Row | Tool | cwd | Gating? |
|---|---|---|---|
| Builder offline tests | `tools/test_gallery_cache_builder_offline.py` | root | gating |
| Artifact 1 golden | `-m assembler.tests.test_artifact1_earth` | `gallery/` | gating |
| Config feature shapes | new, `tools/test_config_shapes.py` | root | gating |
| Served cache structure | new, `tools/test_served_structure.py` | root | gating |
| Feature renderers (Node) | `documentation/smoke_features.js` | root | gating |
| Framing (Node) | `documentation/smoke_framing.js` | see below | gating |
| Solar shells (Node) | `documentation/smoke_sun_shells.js` | root | gating |

### The two new checkers

**Config feature shapes.** Import `_validate_feature_shapes` from
`tools/gallery_cache_builder.py` and run it over every object's
`features` block in `data/objects_config.json`. Rev 1 was right that
this is the correct target and the reason is worth recording: the
builder feeds that function the config block DIRECTLY at line 1102
(`feats = r['obj'].get('features', {})`), and `feature_configs.json` is
a straight copy of it. So the checker validates the same bytes the
builder validates, not a lookalike.

It matters because the Earth work will be editing that config
repeatedly. Success must print the number of objects and feature keys
examined, or a config with zero features passes silently.

**Served cache structure.** Call `assert_structural` with BOTH
arguments: the parsed `data/solar-system/coverage_index.json` as
`index`, and `data/solar-system` as a `Path` for `staging`. Print the
object count and the served window. Passing only the first argument, or
stubbing the second, removes the positions-file and raw-vector checks --
which is most of what the function does.

Both are thin wrappers and both live in `tools/` as their own scripts,
resolving their paths from `__file__` so the runner can launch them from
the root like everything else.

### One coupling rev 1 did not name

`_validate_feature_shapes` is the function whose `radius_fraction > 1.0`
rule (line 966) L-238 exists to relax, because five of Earth's six new
sphere entries sit below the surface. Build the config-shapes checker
before L-238 lands and it goes red the moment the Earth entries enter
the config -- correctly, and uselessly. **These are one piece of work,
not two**, the same way L-235 and L-237 are.

### The Node rows

`node` is outside Tony's working set. The temptation is to skip these
rows when Node is absent. **Do not skip them. Report the absence and
FAIL the run.**

    Feature renderers (Node)   --   NODE NOT FOUND: 3 suites unrun

A skipped row prints nothing while the headline still says everything
passed, which is the precise failure this runner exists to correct.

Invocations, verified against the argv handling in each file:

    node documentation/smoke_features.js gallery/feature_renderers.js
    node documentation/smoke_framing.js gallery/solar_system_earth_test2.html gallery/feature_renderers.js
    node documentation/smoke_sun_shells.js gallery/feature_renderers.js data/objects_config.json

`smoke_features.js` reads both payloads via `path.join(__dirname, ...)`
and is launch-independent. `smoke_sun_shells.js` takes both its inputs
on argv and is launch-independent.

**`smoke_framing.js` is not**, and the right fix is in the suite rather
than in the runner: change line 32 to `path.join(__dirname,
"payload_jupiter_saturn.json")`, matching its sibling. A one-line patch
that removes a launch-directory dependency is strictly better than a
runner row that carries a special case forever, and leaving it would put
a quiet cwd assumption inside the tool whose job is to catch quiet
assumptions. Until that patch lands, that row needs
`cwd=documentation/`.

### The golden row

`test_artifact1_earth.py` is on the roster as gating, and today it cannot
fail on the thing it claims to check: T5 at lines 129-133 reads
`fp.compare(golden, golden)` -- the fingerprint against itself -- and the
stored `gallery/assembler/harness/golden/artifact_1_earth_alone.json` is
never opened. That is L-235.

**The runner does not fix it.** Put the row on the roster and fix T5 in
its own patch under L-235, so the fix is reviewed as a change to the
harness rather than buried inside a new tool. But sequence them
together: a runner whose headline row is a self-comparison is a check
that cannot fail, wearing a runner's clothes. The L-237 golden re-cut
belongs in the same patch, since re-cutting and comparing are two halves
of one act.

---

## Skill loading status: not on this roster, and the reason is the point

Asked directly, 2026-08-25. The answer is no for the gallery runner, and
the argument is worth writing down because the instinct behind the
question is right.

**A skill lives in three stores.** The repo (`skills/<name>/SKILL.md`),
Tony's account install -- the copy Claude actually loads -- and the
generated manifest table in `PROJECT_INSTRUCTIONS.md`.

**All three are orrery-side.** The gallery has no `skills/`, no
protocol, no manifest. A skill checker in the gallery runner would have
to reach a sibling directory that exists only on Tony's machine, which
is the precise argument this document opens with for why the gallery
gets its own runner at all. It would be the fourth instance of the
failure the runner exists to correct, installed by the runner.

**The repo-to-manifest half is already covered in the orrery.**
`skills_index.py` is GENERATORS row 2 (`maintenance_run.py` line 114),
it regenerates the manifest from the SKILL.md files, and
`print_files_written` reports whether `PROJECT_INSTRUCTIONS.md` actually
moved. Since August it also prints what the manifest was advertising
before overwriting it. Drift between those two stores is reported today.

**The third store cannot be read by any runner, ever.** The account
install is not on disk anywhere a script can reach, and the protocol
already records that a mid-session reinstall cannot be verified from
inside the session that makes it. So a row reporting "skills OK" would
be reporting agreement between the two readable stores while the only
store that determines what Claude actually loads stays unexamined. That
is not a check that cannot fail. It is worse: a check that CAN fail, on
the wrong axis, whose green reads as covering something it does not.
Verification of the account copy stays where it already is -- the
session's own load-time comparison under Stale Skill = Stop, deferred
into the handoff when a bump happens mid-session.

**What SHOULD be built is orrery-side and already has a handle: L-230.**
The transition watcher for step 3 of the four-link binding rule -- report
when a skill version changed since the last run and the protocol version
did not. It has to watch the TRANSITION; the naive form, asking whether
each manifested version appears somewhere in the written history,
reports 10 of 10 and is a check nobody reads twice.

If a skill row is ever added anywhere, its verdict line names its own
blind spot -- something on the order of `3 stores, 2 readable` -- because
making the blind spot announce is the second of the three moves the
resident gate asks for.

---

## What it does NOT do

**It does not run the nightly builder.** That fetches from Horizons,
takes minutes, and has its own dashboard button and its own `--dry-run`.
A maintenance run should be fast enough to run without thinking about
it.

**It does not touch the orrery.** No cross-repo reads, no sibling paths,
nothing that behaves differently depending on where the two folders sit.

**It does not clean the quarantine directories.** `tools/gallery_cleanup.py`
owns that and has its own button. But a report-only row COUNTING them
would be worth having -- three accumulated in a single day this session
and nothing surfaces it. Add it as report-only in a second pass.

---

## Build order

1. `tools/gallery_maintenance_run.py` with the one generator, the two
   existing Python checkers, per-row cwd and a per-row interpreter.
   Runnable and useful immediately.
2. The one-line `smoke_framing.js` `__dirname` fix, then the three Node
   rows, with the not-found path exercised by temporarily renaming
   `node` on PATH. A check that cannot fail is not passing, and that
   applies to this runner's own absence handling first of all.
3. The dashboard button, orrery side.
4. L-238, then the two new thin checkers
   (`tools/test_config_shapes.py`, `tools/test_served_structure.py`).
   In that order, for the coupling named above.
5. L-235's T5 fix and L-237's re-cut, together.

Steps 1 and 3 are the minimum that makes it real. Rev 1 put the two new
checkers second and the Node rows third; they are swapped here because
the Node rows are ready now and the checkers are gated on L-238.

---

## Open questions

**1. Where `module_atlas.py` sits is not the question; where it is
LAUNCHED is.** Rev 1 asked whether to move it into `tools/` and
recommended leaving it. That recommendation stands, but for a different
reason than tidiness: the file uses `__file__` only for tag sourcing
(lines 182, 585), so moving it is harmless, while `main()` writes to the
working directory whatever happens. Leave the file at the root and pass
`cwd=REPO_ROOT` on its row. The real decision is whether any row is
allowed to inherit the runner's cwd implicitly. **Recommendation: no --
every row states its own, even when it is the default.**

**2. Whether to install Node at all.** The runner works without it and
says so. Installing turns three report-nothing rows into three real
gates and costs one download. Does not block the build.

**3. Should the golden row gate, given the artifact will be deliberately
re-cut every time a feature family lands? Recommendation: yes.** The
field the part-by-part ruling guarantees will move is `feature_keys`,
which is exactly what the golden hashes. A mismatch you EXPECT is still
one you should have to look at and clear by re-cutting. A gating row is
what makes re-locking a decision rather than a drift, which is Tony's
2026-08-25 ruling read forward into the tooling.

---

## One caution, still live

L-236 does not exist in `LEDGER_CONSOLIDATED.md`. The orrery HEAD is
unchanged from the 2026-08-25 session's own base, so L-234 through L-241
live only in a handoff. `patch_L234_7_ledger_rows.py` was written on
2026-08-25 and is waiting to be run. **Run it before building from
this.** A design document citing a row the status authority does not
carry reads as settled while nothing behind it is, which is the
citation-over-recalled-data failure moved up one layer.

---

*Written August 25, 2026 with Anthropic's Claude Opus 5. Orrery
`4ad78a01a642166cb70218ae5728aa6f6c39d7f4`, gallery
`88633707ce55288bd4a7e03c59513655b3f4a8f3`. Both trees downloaded at
those SHAs; every line number, signature and argv contract cited above
was read from those bytes.*
