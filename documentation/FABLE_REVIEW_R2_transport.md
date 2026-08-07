# FABLE REVIEW ROUND 2 -- Feature-Data Transport

**Built on `754f46b1c1459ea79101fa224687e56a51d4fc96`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).**

**Gallery repo pinned separately at
`61a78c00668573dbff111ec9f10a96b1cd2fdc35`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io (branch main).**

**Type:** DESIGN REVIEW, round 2. Zero code delivered.
**Prepared:** August 6, 2026 by Claude Fable 5, responding to
`FABLE_REVIEW_R2_PROMPT_transport.md`.
**Reviewer verification:** both HEADs confirmed live via `git ls-remote`
and both match the prompt's anchors exactly. Orrery delta from my round 1
anchor (`ee0da47c`): two commits, purely additive -- the round 1 review
landing in `documentation/` plus three patch scripts. No source module
changed, no skills changed (round 1's skill-gate result carries: all five
relevant skills match the v3.34 manifest). Gallery unchanged. The
prompt's "nothing patched" declaration is confirmed byte-level.

Because this round exists to correct premises that were read but not
checked, every load-bearing claim below was verified against the files
at the anchors before being used. Where a claim is mine and unverified,
it says so.

---

## Verdict in one paragraph

**Fetch-and-import is sound and I endorse it.** It is round 1's vendored
pull with the exporter removed -- same fallback property, same SHA
recording, same quarantine semantics, strictly fewer moving parts, and
zero hand steps, which round 1's version could not claim. The trust
argument holds with one precision added below, and the leaf claim is
even stronger than the prompt states: I verified that `numpy` and
`timedelta` are both imported and **never used** -- the store is
effectively stdlib-only today, and Track 0 can make that literal.
Fetch-and-import does lose exactly one capability the `ast` route had --
duplicate-key detection, the Phobos class from round 1 -- and I
recommend recovering it with a ten-line pre-import gate that also
answers Q1's guard question and Q5's coupling question. Details per
question below; the one genuinely open design point this round has not
specified is where description interpolation happens (builder or
assembler), flagged under Q4.

---

## Premise verification record

Stated first because it is this round's method, not an appendix.

- **Premise 1 (exporter dormancy): confirmed, with one footnote.**
  `grep -rln export_orbit_cache` at `754f46b` returns tooling maps, the
  scanner, patch scripts, and one entry I chased down:
  `palomas_orrery_dashboard.py` line 253. It is a launcher-menu string
  (name, filename, description), not an import or call -- so "nothing
  calls or imports it" stands on every automated path. The footnote: the
  dashboard **advertises** it as a launchable Phase 1b devtool. If the
  exporter is retired under this design, that menu entry becomes a
  stale-erratum-class pointer and should be updated in the same pass.
- **Premise 2 (derived constants are correct, not a problem):
  confirmed.** My own ast pass at `754f46b` counts 45 top-level
  assignments, 7 non-literal: `SOLAR_RADIUS_AU`, `LIGHT_MINUTES_PER_AU`,
  `HORIZONS_MAX_DATE`, `CORE_AU`, `RADIATIVE_ZONE_AU`,
  `CENTER_BODY_RADII`, `stellar_class_labels`. Two of those
  (`HORIZONS_MAX_DATE`, `stellar_class_labels`) contain constructor
  calls that `ast.literal_eval` cannot evaluate at all -- direct
  evidence that extraction-without-execution was fighting the file's
  design, and import is working with it.
- **Premise 3 (the gallery can execute the file): confirmed at both
  ends.** Store side: the only imports are `numpy` and `datetime`
  (lines 46-47), and -- new finding -- `np.` appears nowhere in the
  file and `timedelta` appears nowhere outside its import line. Both
  are dead imports. Builder side: astroquery/astropy are lazily
  imported (builder lines 77-78) and the nightly path hard-fails
  without them (line 206), so numpy is present in the environment by
  hard dependency. The environment claim holds; the store needs even
  less than claimed.

---

## Q1 -- Is fetch-and-import sound, and what does it cost?

**Sound.** On executing fetched code, I agree it is not meaningfully
untrusted, and the argument is worth stating precisely because it will
be read by future sessions: the builder itself, the orrery GUI, and
every patch script Tony runs come from the same two repos under the
same GitHub account. A compromise of that account compromises every
execution path Tony already has; importing one more file from it adds
**no new trust root**. And the SHA pin is stronger than it looks: a raw
fetch at a full 40-character commit SHA is content-addressed --
immutable by construction -- so even if HEAD moves between the
`ls-remote` and the fetch, you get exactly the bytes the recorded SHA
names. There is no window in which "what was checked" and "what was
imported" can differ.

What I would guard is **accident, not malice**, and the costs not yet
priced are these:

1. **Module-level side effects.** Importing executes top-level code. If
   the store ever grows a top-level file write, network call, or slow
   computation, the builder inherits it silently every night. Guards:
   (a) a one-line rule added to the store's docstring in Track 0 --
   data-only module, no top-level I/O; (b) the pre-import gate below,
   which makes the import surface explicit.
2. **The pre-import gate (recommended).** Before importing the fetched
   file, parse it with `ast` and check exactly two things: every
   `import` statement is on an allowlist (`datetime` plus whatever
   stdlib the store legitimately needs; after Track 0 drops numpy, the
   list is tiny), and no literal dict contains a duplicate key. Reject
   and quarantine on either. This is roughly ten lines. It is NOT a
   revival of the ast-extraction route premise 2 killed -- it reads no
   values and evaluates nothing; it inspects two structural properties
   `ast` is trivially good at, then hands off to import for everything
   else.
3. **Duplicate keys are the one real capability lost.** Post-import,
   Python has already silently kept the last duplicate -- the round 1
   Phobos finding (`'Phobos'` appears twice in
   `KNOWN_ORBITAL_PERIODS`) is **invisible** to fetch-and-import,
   whereas ast extraction would have seen it. The gate above recovers
   the check at the right place: before the collapse happens in the
   builder's process. The store-side fix for the existing duplicate
   stays a Track 0 item.
4. **Import mechanics.** Load via `importlib.util.spec_from_file_location`
   from the staging path with a per-run module name. Never insert the
   staging dir into `sys.path`, never reuse a name an installed package
   could own. This is hygiene, not a design change, and matches the
   builder's existing lazy-import pattern (its own line 73 comment).

## Q2 -- Does the leaf claim hold, and will it keep holding?

**It holds, and Track 0 can make it stronger than the prompt claims.**
Verified: `numpy` is imported and unused; `timedelta` is imported and
unused; the file's real dependency surface is `datetime.datetime` for
one GUI constant. **Recommend Track 0 drop both dead imports**, making
the store stdlib-only. That removes the sole heavyweight dependency and
any version-skew surface between the two environments in one line.

Will it keep holding: Track 0's incoming content is 37 entries of
literals, prose, and source strings -- nothing that needs an import.
The realistic future risk is a convenience import added in some later
session (someone pulling in a helper "just for one function"). The
allowlist gate converts that from a silent coupling into a loud,
named, pre-execution rejection at the next nightly -- which is the
right failure: visible, attributable, and fixed by a one-line store
edit or a deliberate allowlist extension. So: theoretical, and guarded
mechanically rather than by discipline alone.

## Q3 -- Does the fallback property survive?

**Yes, confirmed.** The property round 1 valued lives in the committed
DERIVED VALUES, not in how they were produced. Step 5 commits the
feature values with the rest of the nightly output; on unreachable,
unimportable, or invalid, quarantine keeps serving the last committed
copy. Two small additions to make the property fully round-trippable:
record BOTH the orrery SHA and the content hash of the fetched
`constants_new.py` in the run manifest (the machinery exists --
`_write_run_manifest` at builder line 1476), so any served state can be
traced to exact store bytes; and surface the SHA lag in the loud
warning, which the proposal's step 6 already says.

## Q4 -- What breaks that you have not seen?

Four things, one of them a genuine unspecified design point.

1. **The JSON-serializability boundary.** Import gives the builder live
   Python objects; the served cache is JSON. The store contains a
   FUNCTION (`color_map`) and a DATETIME (`HORIZONS_MAX_DATE`) at top
   level today, and nothing stops a future value from arriving as a
   numpy scalar, which `json.dump` rejects. None of these is a feature
   value, so nothing breaks in this build -- but the validation step
   should enforce the boundary explicitly: every value bound for the
   cache is coerced to plain int/float/str/list/dict, and anything else
   is a validation failure, not a crash mid-write. This is the
   transport-level answer to "values this transport cannot carry
   correctly": it cannot carry callables or rich objects, and it should
   say so loudly rather than discover it at serialization time.
2. **Where does description interpolation happen?** The ratified
   architecture stores descriptions as templates with fields
   interpolated from stored values. The transport proposal carries
   values but does not say whether the SERVED cache holds templates
   plus values (assembler interpolates at render time) or
   pre-interpolated final strings (builder interpolates at build time).
   I recommend the builder pre-interpolates: the assembler's philosophy
   is reconstruct-alone-from-data, and shipping final strings keeps it
   dumb, keeps the failure surface at build time where quarantine
   exists, and means a template error is caught nightly instead of in
   a user's browser. Either answer works; pick one in the design,
   because it decides the cache schema.
3. **Duplicate-key invisibility** -- covered under Q1; listed here
   because it is literally a value the transport carries INCORRECTLY
   (silently-last-wins) absent the gate.
4. **The dashboard's exporter entry** -- covered in the premise record;
   belongs in the retirement pass so the menu does not advertise a tool
   the architecture has bypassed.

And one addition that is not a breakage but closes the class of misses:
**nightly change detection.** Diff tonight's derived feature values
against last night's committed copy and log every changed value with
old, new, and both orrery SHAs. Shape, source-presence, and range
checks all PASS on a value that changed for the wrong reason; the diff
is the only guard that sees CHANGE itself, which is the L-182 failure
family. It costs one comparison against a file the repo already holds.

## Q5 -- Does the Track 0 exit checklist hold?

Items (a) and (b) hold as written. The two questions asked:

**Unit-sanity: right guard, needs two companions.** Range checks catch
the km-to-AU class perfectly -- a 1.5e8 magnitude shift cannot hide
inside any sane per-field-class range (ring radii in km: say 1e2 to
1e6; fractions: 1 to 100). They are the right guard for magnitude
errors, which is what unit slips are. But they are static, so add:
cross-field invariants (`inner_radius_km < outer_radius_km` for every
ring -- verified against the store this catches nothing spurious
today), and the nightly value-diff from Q4, which catches the errors
that are individually in-range but wrong. Three cheap checks, three
different error classes.

**Coupling: three notes are documentation, not a guarantee -- make the
contract one name instead.** The checklist's item (d) was written for
the ast option and its wording ("break the extractor") is stale, as the
prompt says. Under fetch-and-import the builder reads NAMES, so renames
break it while shape changes do not. The mechanical fix is to shrink
the contract to a single name: **Track 0 defines one explicit registry
in the store** -- e.g. `FEATURE_REGISTRY`, a dict mapping body slug to
that body's feature entries -- and the builder reads exactly that one
name. Every rename, regrouping, or nesting change INSIDE the store
becomes an internal matter that never touches the contract; the only
breaking change left is renaming the registry itself, which is one
grep away from impossible to miss. The three documentation notes then
all describe the same one-line interface, which is what documentation
is good at. Keep the notes; move the load-bearing weight onto the
registry.

## Q6 -- Sequencing

The ruled order (Track 0, then Track 1, then Track 2) stands and I am
not re-litigating it. Within Track 0, there is a real de-risking option
the shape-insensitivity of fetch-and-import newly enables: **a pilot
slice.** Migrate ONE body first -- Jupiter, 5 entries -- through the
full Track 0 treatment (store entry, three zones, source fields,
template descriptions), and build the transport end-to-end against it:
fetch, gate, import, validate, interpolate, commit, quarantine-path
test. Then scale to the remaining 32 entries, which under
fetch-and-import requires ZERO transport rework -- new entries flow
through untouched, which is precisely the property Q2 verified.

The case for this over transport-last: the transport cannot be
meaningfully tested against today's store anyway (no `source` fields
exist, so abort-on-missing-source has nothing to pass), so "build
transport after Track 0" really means "first end-to-end test after all
37 entries move" -- the largest possible batch before the first proof.
The pilot gives Tony's own acceptance test ("this should be minor if
the architecture is right") its first data point at one-seventh the
exposure, and any schema surprise (the round 1 resistant-prose cases
live in Jupiter's descriptions, deliberately a good pilot) surfaces
while one body is in flight instead of four. The case against: two
passes over the migration tooling instead of one. My lean is the pilot;
the convergence judgment is Tony's.

## Q7 -- What in round 1 leaned on the removed premises

Audited my own review against the three premises. Four items lean;
the core does not.

1. **The "extends an existing pattern" clause** overclaimed for the
   exporter, as the prompt already records. Conceded; the store, zones,
   citation form, and vendored-pull mechanics were and are extensions
   of existing patterns -- the exporter was the invented piece, and
   this round deletes it.
2. **"Abort-on-missing-source runs orrery-side; the builder re-checks
   gallery-side"** assumed a generation step. There is no generation
   step now -- "generation" is Tony editing the store. Enforcement
   redistributes to two points that already exist: the scanner at the
   orrery pre-push gate (once the SOURCE_PATTERNS extension recognizes
   `source` data fields -- deferred fix item 6, unchanged from round 1)
   and the builder's nightly abort. Two existing enforcement points,
   no new tool: cleaner than what I recommended.
3. **Finding 2 (the `feature_configs.json` name collision) dissolves**
   rather than resolving -- with no orrery artifact there is no
   collision to rename around. The residue is the dormant exporter's
   own output file and the dashboard menu entry: both belong in a small
   retirement note so no future session reads them as live
   (stale-erratum discipline).
4. **The Q4 citation refinement** ("reference the artifact's recorded
   orrery SHA") survives with one word changed: reference the SERVED
   CACHE's recorded orrery SHA, which the run manifest carries.

Everything else in round 1 -- the fallback argument, the
self-containment reframe (the boundary is the assembler at render
time, untouched by any of this), the store-hygiene findings, the
`*_info` fifth surface, the resistant-prose test set, the L-179/L-180
sequencing warning, and the gallery uncited-constants pass -- rests on
verified file state, not on the removed premises, and stands.

---

## Recommendations rollup

1. Endorse fetch-and-import as specified; update the builder docstring
   wording as the prompt proposes.
2. Add the pre-import gate: import allowlist + duplicate-dict-key
   check, quarantine on either. (~10 lines, ast-on-two-properties,
   not ast-extraction.)
3. Track 0: drop the dead `numpy` and `timedelta` imports; store
   becomes stdlib-only.
4. Track 0: define `FEATURE_REGISTRY` as the single-name contract; the
   builder reads only it.
5. Validation: JSON-type coercion boundary; cross-field invariants
   (inner < outer); nightly value-diff report with both SHAs.
6. Run manifest records orrery SHA + fetched-file content hash.
7. Decide the interpolation locus; my recommendation is
   builder-side pre-interpolation.
8. Retirement note: `export_orbit_cache.py`, its `feature_configs.json`
   output, and the dashboard menu entry at line 253.
9. Tony (decide): pilot-slice sequencing inside Track 0 (Jupiter
   first, transport end-to-end, then scale).

*Round 2 review prepared August 6, 2026 with Anthropic's Claude
Fable 5, built on `754f46b1c1459ea79101fa224687e56a51d4fc96` at
https://github.com/tonylquintanilla/palomas_orrery and
`61a78c00668573dbff111ec9f10a96b1cd2fdc35` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
