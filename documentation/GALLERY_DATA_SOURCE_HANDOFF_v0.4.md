# GALLERY DATA-SOURCE HANDOFF v0.4 -- convergence review + ratification (amendment)

Tony Quintanilla, PE | Claude | July 9, 2026

**Type:** DESIGN AMENDMENT (zero code) -- Opus 4.8 convergence review of manifest
v1 against live code and v0.3, then a decision walk-through with Tony. This
handoff records WHY the design changed where it changed; it does NOT restate
v0.3. It CARRIES v0.3 by reference for everything unchanged (rewriting the whole
document risks the rebase-leak failure this project has been bitten by).
**Base:** orrery HEAD `4e2629c` | gallery HEAD `4b086a6` (SHA round trip this
session). The orrery advanced from v0.3's `cde22c5` and v1's `081ee18` to
`4e2629c`; the only commit past `081ee18` adds the manifest file itself -- ZERO
source changed, so all v0.3/v1 code citations remain valid.
**Supersedes (specific v0.3 decisions only):** the spacecraft trace model (v0.3
Trace & Conic point 4) and the Guard-as-gate posture (v0.3 Guard v2 + Nightly
Atomicity). Everything else in v0.3 stands.
**Companion:** GALLERY_BUILDER_MANIFEST v2 (the executable contract).
**Ledger:** L-098 (parent, trail updated); L-106 (NEW -- backup discipline).

================================================================
HOW THIS SESSION WENT
================================================================
Opus 4.8 verified manifest v1's load-bearing claims against the live repo (not
against Fable's summary of it): SHA round trip, ghost purge, the copy-source
citations, and manifest-vs-v0.3 fidelity. The gates held. Two of v1's flags
carried FALSE NEGATIVES that were corrected; six decisions were ratified or
resolved with Tony; and Tony surfaced two improvements the review had not:
a better spacecraft model, and a missing backup plan. The double helix did its
job -- Tony's "Tp is fetched from Horizons" pushback drove the comet-path
correction, and his "add today's point nightly" reframing replaced a whole
write-once subsystem.

================================================================
THE CHANGES (with reasoning) -- what v0.4 amends
================================================================

--- 1. Comet Tp path: solution-Tp LOCATES, converged osculating-Tp ANCHORS
    (deepens v0.3 point 2; corrects manifest v1 S3a) ---
v0.3 point 2 named `_add_perihelion_osculating_orbit()` (which DOES exist -- the
dispatcher) and specified "the osculating conic at the perihelion epoch." v1
implemented "elements at today -> read TP -> refetch at that TP." That is a
single un-iterated step of a fixed-point iteration STARTED FAR FROM PERIHELION,
and it does not converge. The desktop leaf `plot_perihelion_osculating_orbit`
(idealized_orbits.py:7089) does the correct two-role thing, verified in code:
  (1) SOLUTION TP (from the Horizons response header, via `resolve_tp` /
      `fetch_solution_tp`, ocm:459) locates perihelion in ONE query.
  (2) Fetch osculating elements AT that epoch.
  (3) Serve that set anchored on ITS OWN osculating TP -- the "converged" value,
      which at perihelion has collapsed onto the true passage and is consistent
      with the served elements.
Tony's framing was exact: the Tp we SERVE is "the one that converges"; the
solution TP's only job is to get us to perihelion in one shot so the osculating
TP we read there has already converged. The residual `solution_TP -
converged_osc_TP` at perihelion is the integrated non-gravitational (outgassing)
shift -- a real physical signal the desktop already renders (io:7212-7233); if
both Tps are served, the browser gets it for free. Manifest S3 adds
`resolve_tp`/`fetch_solution_tp`/`cache_solution_tp` to the copy-source list
(v1 omitted them -- the root cause of the shortcut).

--- 2. Spacecraft model: fetch-flown-once + append-today-nightly
    (SUPERSEDES v0.3 point 4; Tony's design) ---
v0.3 specced pre-fetching the FULL arc -- flown past PLUS predicted future out to
the ~2029 SPK horizon -- write-once, refreshed manually. Tony's model: fetch only
the FLOWN arc (ephemeris-start -> today) once at first build, then append today's
single point every night, exactly like every other object. Why it is better, not
just different:
  - Uniform nightly: every object accretes one real point/night (the same
    preservation model F3 uses for planets). Spacecraft stop being a special case.
  - No predictions served as fact; the line ends at "you are here."
  - A live nightly endpoint DISSOLVES the active-maneuver problem -- a maneuvering
    craft's predicted future would drift, but a nightly-fetched endpoint never
    does. v0.3's model deferred that problem; this one removes it.
  - The "where is it heading" projection, if ever wanted, is a browser
    extrapolation of the coast -- not stored.
Both models have merit; the trade is giving up the pre-drawn future arc, which
for a coasting craft the browser can reconstruct. Ratified: Tony's model.

--- 3. Ephemeris bounds from Horizons, not constants
    (SUPERSEDES the v0.3 2029-12-12 value; folds v1 F7 into F5) ---
Because we no longer fetch the future, there is no SPK-end date to source -- v0.3's
unsourced "2029-12-12" is simply GONE from the config. The one ephemeris bound
that remains is the arc START, and it is DISCOVERED from Horizons: attempt from
the config `start` hint (launch date), and if Horizons returns empty or clips the
leading edge, read the actual first epoch from the response and begin there. The
Horizons ephemeris typically lacks the first hours after launch, so a hardcoded
"launch + 1 day" is the same plausible-constant anti-pattern F7 was built to kill;
the honest rule is symmetric -- the config supplies HINTS, Horizons supplies
VALUES. That discovered start is the earliest frozen archive point forever, so it
must be fact-derived.

--- 4. Guard v2 becomes a MONITOR, not a gate
    (SUPERSEDES v0.3's reject-outer/flag-reverse and v1's reject-both) ---
v0.3 hard-rejected the outer bound; v1 promoted both bounds to hard reject. v0.4:
BOTH bounds WARN. The reasoning is v0.3's OWN honesty note taken to its
conclusion -- Guard v2 is defense-in-depth, NOT the primary guarantee;
provenance-by-construction (explicit-center fetch) is. A backstop should not have
veto power to abort a build and DISCARD data over what is most likely a transient
Horizons error -- and discarding destroys the evidence needed to diagnose the
fetch. So: keep the point (raw archive holds everything), serve it, and WARN.
  - The band `q/k <= |r| <= k*Q` (k = 2.0) now sets the WARNING threshold. k was
    chosen 2.0 because osculating a,e are snapshots and Kozai-class irregulars
    (Neso, apoapsis 0.572 AU) swing between them; 1.5 would false-warn the objects
    the guard exists for.
  - The requirement that keeps warn from decaying into silent-accept: the warning
    must be LOUD, DIAGNOSTIC (object, |r|, expected band, center, fetch params),
    and reach a channel Tony actually reviews. A warning written only to a file
    nobody opens is not a monitor.
  - Optional two-tier severity: inner-bound = "review" (can be a real perturbation
    snapshot swing); outer-bound at ~30x expected = "likely contamination" (the
    Charon class) -- so a real signal does not flatten into noise.
  - CONSCIOUS residual risk (Tony ratified with eyes open): a genuine
    contamination now reaches served until Tony acts on the warning. That is the
    exact shape of the original Charon bug -- but now DETECTABLE instead of
    silent, and backed by provenance upstream + the shrink gate + git + off-repo
    backup downstream. The validation SPLIT matters: STRUCTURAL invariants
    (schema/file/center/unit-sanity) still ABORT (builder-bug gates); only the
    magnitude/contamination checks (Guard band, B3) become warn.

--- 5. Gallery-cache backup + gitignore discipline (NEW; absent from v0.3) ---
The gallery raw archive is now an irreplaceable asset (fetched-once past), the
same class as the orrery's Horizons cache. v0.3 specced only ROLLBACK (git
history), not BACKUP. Added:
  - A SEPARATE scheduled action (mirroring Tony's existing "backup on every cache
    update") targets `data/solar-system/raw/` -- served files are derived and
    regenerable, so they need no independent backup.
  - The local backup path is GITIGNORED, so backup copies never enter the repo
    that serves to the web under the ~1 GB Pages budget (474 MB used) -- committing
    them would double growth against the tightest constraint.
  - Tony's Google Cloud auto-backup carries the OFF-SITE copy from there, which
    closes the third failure mode (repo/account loss) on infrastructure separate
    from GitHub.
  - Decoupled from the builder: a backup failure never blocks a good commit, and
    the builder never waits on backup.
  - FIRST BUILD IS GATED on the backup action + gitignore entry existing.
Three integrity layers, three distinct failure modes: shrink gate (bad write,
prevented) / git revert (bad build that committed, rolled back) / off-repo backup
(bad repo, survived). No overlap, no gap.

--- 6. Ratified as drafted (carried from v1 into v2) ---
  - F1 range-query primary with recursive range-halving fallback (a correct
    divergence from the REQUEST's ~75-epoch chunk spec, which applies only to
    discrete epoch lists).
  - F3 `horizon = 0` for non-spacecraft (nightly `[today-7d, today]`, freeze past,
    no future) -- the faithful consequence of the conic retiring non-spacecraft
    traces.
  - F6 osculating elements history as per-object JSONL (feeds deferred L-101 with
    zero refetch).
  - Shrink gate re-expressed as POINT-COUNT >= 95% per-object + aggregate
    (a conscious adaptation of v0.3's "import the byte-shrink block"; point count
    is the truer data-loss signal for date-keyed dicts).

================================================================
CORRECTIONS TO THE RECORD (honesty)
================================================================
- v1 F2 "no such symbol at HEAD" was FALSE: `_add_perihelion_osculating_orbit`
  (palomas_orrery.py:1533) exists as the dispatcher v0.3 correctly named; copy the
  LEAF `plot_perihelion_osculating_orbit` (io:7089) it calls.
- v1 F7 "2029-12-12 not found in v0.3" was imprecise: the date IS in v0.3 point 4
  and in the request, as an unsourced value. Moot now (removed with the future
  fetch).
- Review self-correction: an earlier convergence-review note flagged the invariant
  set as "possibly dropping #1/#4/#7." WITHDRAWN -- v0.3 line 292/297 shows the
  carried set is exactly {#2,#3,#5,#6,#8,#C} with #1/#4/#7 deliberately RETIRED
  (#4's np.interp-containment lesson tagged to return in Phase 2). Manifest carries
  {2,3,5,6,8,C} + new {V->split into U(structural)+monitor, T, W}. Faithful.

================================================================
WHAT CARRIES FORWARD FROM v0.3 UNCHANGED (by reference, not restated)
================================================================
The PIVOT (fetch-fresh, gallery-repo cache, legacy orrery cache untouched); the
rebuild-not-audit guarantee + the explicit-center-fetch honesty note; Choice 1
raw/served split (raw grows, served window = derive param); Choice 2 desktop-
scheduler-now/Action-later + idempotent self-healing + Probe-Actions + PAT
hygiene; the conic model (elliptical 360 / hyperbolic near-perihelion arc,
as-of-today point every object); the two-surface principle (interactive
generative-lite vs gallery curated full-fidelity, bridged by event_link); the
closest-point marker; comet structure as a Phase-2 FEATURE not orbit data; the
standalone-with-copy-discipline; mixed-version `?v=<generated>` reads; the
per-run build manifest; the attribution field; the first-build ghost purge (DONE,
verified); the carry-forward tags (np.interp returns in Phase 2; --dry-run
descends from --preflight-only); the nightly atomicity skeleton (now with the
abort/warn split of change 4).

================================================================
NEXT
================================================================
1. The manifest is v2 and ready to carry to the build session on the amendments
   above. No further design round needed unless the Encke dry-run surfaces a Tp
   surprise.
2. Build (separate session): pre-test the builder; --dry-run voyager_1 (ephemeris
   start discovered) and encke (solution-Tp path, 2P disambiguation, Tp matches
   desktop resolve_tp); first full build over the window; confirm the Guard
   WARNING fires loudly on an injected bad point (monitor teeth); confirm backup
   action + gitignore exist BEFORE first build; schedule nightly + the separate
   backup action.
3. Ledger: L-098 trail updated; L-106 opened (backup discipline).

Ledger L-098 delta: SHA 4e2629c; convergence review + ratification (Opus 4.8 +
Tony); comet solution-Tp correction; spacecraft model redesigned to
fetch-once/append-nightly; Guard v2 -> monitor; 2029-12-12/`--refresh-spacecraft`
retired/demoted; backup discipline spun out as L-106.

---

v0.4 amendment written July 2026 with Anthropic's Claude Opus 4.8; decisions
ratified by Tony. Carries v0.3 (v0.1 Opus 4.8 -> v0.2 Fable 5 review -> v0.3 trace
& conic model) by reference. Companion: GALLERY_BUILDER_MANIFEST v2.
