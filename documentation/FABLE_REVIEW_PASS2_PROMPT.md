# Gallery Cache Builder -- Review Pass 2 + Skills/Protocol Lessons Review

For: Fable 5 (Mode 7, adversarial + retrospective)
From: Tony Quintanilla (integrator), relayed by Claude Opus 4.8
Two parts: (A) adversarial review of the REMEDIATED build; (B) a "lessons
learned" review of the resident protocol and the skills layer.

---

## SHAs to pin first (fetch, do not recall)

- **Gallery** repo HEAD: `<FILL: the re-pushed remediated build>`
  (github.com/tonylquintanilla/tonyquintanilla.github.io, branch main) --
  the standalone builder, its offline test, and objects_config.json.
- **Orrery** repo HEAD: `<FILL>`
  (github.com/tonylquintanilla/palomas_orrery, branch main) -- the copy sources,
  the documentation set, LEDGER_CONSOLIDATED.md, the resident protocol, and skills/.
- **Copy-source base:** orrery `4e2629c` (the builder's provenance citations are
  byte-valid against this).

Round-trip the gallery SHA before anything else: `git ls-remote --symref`. If it
does not match the BUILD handoff's "pushed at", STOP and reconcile -- a phantom
SHA is exactly the failure the round-trip gate exists to catch.

---

## What this is

`tools/gallery_cache_builder.py` -- a STANDALONE nightly builder (no orrery
imports) that fetches fresh from JPL Horizons per object, builds a raw cache +
derived served files (osculating conics for non-spacecraft, position arcs for
spacecraft), validates on write, and swaps into the gallery repo `data/`. Fetch
specifics are COPIED WITH PROVENANCE from the orrery (L-107 sync register). Seed
tranche: ~11 objects (planets, moons, a Pluto-system barycentric case, an
asteroid, 2P/Encke, Voyager 1). Live Horizons is the gate on Tony's hardware; the
offline suite mocks Horizons.

## What changed since your first review (you reviewed pre-remediation `a2b7435`)

Your first pass raised A-1..A-11 + B-1..B-4; all actioned. Then GPT 5.5 was given
the SAME prompt as a COMPETITIVE cross-check and surfaced items your pass did not.
The four remediation passes (ledger L-109 = your findings, L-110 = GPT's):

- **Pass 1 (safety):** A-1, A-2, A-7, A-8, A-11.
- **Pass 2 (correctness + spacecraft):** A-3 (failed fetch serves last-good conic,
  as_of_today NULLED, drop only if no last-good), A-4 (id_type majorbody/id ->
  None), A-5 (closest_apparition/no_fragments -> CAP;/NOFRAG;), A-9 (#T), A-10,
  B-3. Spacecraft fetch REDESIGNED: authoritative `config.start` (no probe) +
  coarse glide backbone + daily densify inside known flyby windows + Douglas-
  Peucker thin -- which DISSOLVES A-6 (Voyager first build ~2,610 coarse points,
  not ~17,900).
- **Pass 3 (docs/ledger):** B-1/B-2/B-4, TESTING_PROTOCOL.md, L-109.
- **Pass 4 (GPT cross-check, L-110):** N1 -- WHOLE-DIRECTORY atomic swap (staging
  is a sibling, the entire generation renames into place as one unit;
  `recover_incomplete_swap` restores the whole generation; one prior generation
  retained as rollback) -- this replaced the four-separate-subtree promotion. N2
  -- verified push (`git_commit` returns committed_local vs pushed_remote;
  confirms the remote CONTAINS the SHA; a silent push failure no longer reads as
  published). N3 -- object-set continuity abort + first-build minimum-count floor.
  N4/N6 -- #B3 conversion-consistency (served km == raw AU x KM_PER_AU) REPLACES
  the absolute #U threshold and retires the phantom "B3" header claim. N5 --
  structured solution-TP outcomes (found/not_present/parse_failed/request_failed;
  operational failure serves last-good, only a genuine not_present today-anchors).

Offline suite: 47 -> 68 checks, 0 failures. Deliberately DEFERRED (do not re-flag
as gaps): L-111 / BUILD handoff "Open items and deferred work" -- Pass 5
operability (--add-object onboarding; a `_health.json` + notification + escalating
likely-contamination to withhold the push) and the N7/N8/N10/N11 hardening.

---

## Part A -- Pass 2 code review (adversarial)

Same discipline as your first pass: verify against the ACTUAL code and astroquery
0.4.11 source (fetched, not recalled), not the handoff prose. Dispositions
BLOCKER / SHOULD-FIX / NICE / QUESTION, each tagged code-fixable-now vs
needs-live-dry-run. Paraphrase; if you must quote, keep it under 15 words.

Look hardest at:

1. **Did each remediation actually close its finding, or is it cosmetic?** In
   particular walk the crash seams of the WHOLE-DIRECTORY swap again: is there a
   seam it did NOT close -- a crash during the sibling copy-forward (before the
   swap); a double-crash leaving a stale `.prev` that the entry guard now REFUSES
   (does that wedge future runs, and is that the right failure?); the retained-
   `.prev` cleanup racing a concurrent off-site backup reading the tree on Windows?
2. **N2 push verification:** does `git branch -r --contains <sha>` actually prove
   the INTENDED branch received it, or could a detached HEAD / wrong-branch / stale
   remote-tracking-ref state report pushed_remote falsely (or falsely negative)?
3. **#B3:** is the raw-point lookup by JD robust (float compare tolerance, a
   missing point, a spacecraft whose as_of_today JD is not in the thinned raw)?
   Does #B3 actually catch a serialization corruption, or only a convert bug?
4. **N3 membership:** can a LEGITIMATE reconfiguration -- renaming a slug,
   deliberately retiring an object -- trip the drop-abort with no override? Should
   there be an explicit "retire" path?
5. **N5:** does raising on parse/request failure route to `serve_last_good` for
   every comet path, and does a genuine `not_present` degrade VISIBLY (not silently)?
6. **Regressions from the net-new code** (DP, structured TP, whole-gen swap,
   #B3/#T, N3 gates): does #T ever false-abort a legitimately stale served object
   (A-3 nulls as_of_today -- confirm the interaction)? Can Douglas-Peucker drop a
   flyby-window point it should keep? Did moving staging to a sibling break the
   copy-forward or the aborted-run autopsy retention (A-11)?
7. **Is L-111 genuinely the remaining set** -- anything material NOT captured?
8. Independently re-run the offline suite (68 checks) and report pass/fail on your
   hardware, plus your read of what the mocks CANNOT prove.

---

## Part B -- Skills + protocol "lessons learned" review

Review the resident protocol (`project_instructions_v3_31.md`) and the eight
skills (`skills/<name>/SKILL.md`) against what THIS cycle actually taught. This is
a retrospective, not a bug hunt: what worked, what should be amended, what
convention emerged that deserves capture. Propose amendments as diffs-in-prose
(which file, what change, why), tiered by the protocol's own CRITICAL / QUALITY /
PRACTICE. Ground each in a concrete cycle event; do not invent lessons.

Prompts to consider:

- **agentic-pre-test.** The offline suite passed in a FLAT working directory but
  A-8 showed it could not run from the real repo layout (config at
  `data/solar-system/`, test in `tools/`). Should the pre-test require running
  from a clean checkout / real layout, not a flat scratch dir? And for UNATTENDED
  infrastructure, A-1/A-2/A-3 were silent-failure seams the render-and-compile
  test structurally could not reach -- should the runtime test include crash /
  kill-point + exit-code checks, not only py_compile + xvfb render?
- **Mode 7 patterns.** The COMPETITIVE pattern (same prompt, two AIs, compare)
  caught N1 and N2 that the single serial pass missed. Should the protocol
  strengthen "competitive review for high-consequence / unattended infrastructure"?
  Where is the line against its cost?
- **SHA round-trip <-> N2.** The round-trip gate caught the phantom gallery SHA by
  discipline; the builder now self-verifies its own push. Is there a principle
  worth stating -- where the protocol enforces something by human discipline,
  prefer tooling that enforces the same thing?
- **Fetched-not-recalled.** Load-bearing again: the astroquery id_type
  deprecation; `closest_apparition` reachable only via `**kwargs` (a claim first
  doubted, then confirmed in source); a provenance cite corrected from 199-223 to
  the verified 198-208. Any sharpening of the convention?
- **provenance-discipline (L-107).** The copy-with-provenance sync register held
  under adversarial checking, and cite accuracy mattered. Amendments?
- **Staleness.** Is anything in the skills now STALE given the builder's shape --
  e.g., horizons-orbital-mechanics describing spacecraft-start DISCOVERY (a probe)
  when the design is now an authoritative curated `config.start`; or gallery-
  pipeline / any skill describing the served promotion before it became a single
  whole-generation swap?
- **"The code is the fact, the handoff is a claim."** Every review claim this
  cycle was verified against code/source before action. Reinforce anywhere it is
  under-stated?

---

## What to fetch

- Gallery repo: `tools/gallery_cache_builder.py`,
  `tools/test_gallery_cache_builder_offline.py`, `data/solar-system/objects_config.json`.
- Orrery repo: the documentation set (`GALLERY_BUILDER_MANIFEST_v2.md`,
  `GALLERY_DATA_SOURCE_HANDOFF_v0.4.md`, `GALLERY_BUILD_HANDOFF_v0.1.md`,
  `TESTING_PROTOCOL.md`, `MASTER_PLAN_INTERACTIVE_GALLERY.md`),
  `LEDGER_CONSOLIDATED.md` (L-098, 102, 107, 108, 109, 110, 111),
  `project_instructions_v3_31.md`, and `skills/<name>/SKILL.md` (all eight).

Neither AI reviewer is authoritative over the live render (Mode 5); Part A's
code findings still meet Tony's eyes on hardware, and Part B's amendments are
proposals Tony integrates.
