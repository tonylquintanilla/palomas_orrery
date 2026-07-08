# REVIEW REQUEST -- Gallery Data-Source Pivot (for Claude Fable 5)

**From:** Tony (carrying a design handoff drafted with Opus 4.8)
**Attached:** GALLERY_DATA_SOURCE_HANDOFF.md (the artifact under review)
**Mode:** Collegial Mode 7 -- broad-first adversarial review. Here is the job;
flag problems. Your value is finding blind spots, not agreeing.

--------------------------------------------------------------------
GROUND RULES
--------------------------------------------------------------------
- This is DESIGN-STAGE: zero code written. The goal is to converge the
  architecture before a manifest. Do not write code; critique the design.
- FETCHED-NOT-RECALLED: verify claims against the attached handoff (and the
  codebase if you have it). If a claim can't be sourced, say "unsourced" --
  don't fill it from memory.
- Base for context: orrery HEAD `d4c37cf`, gallery HEAD `4b086a6`. If you
  confirm SHAs, use `git ls-remote`, don't assume.
- Be a colleague, not a rubber stamp. If the pivot itself is wrong, say so
  plainly and propose the better path.

--------------------------------------------------------------------
BACKGROUND (enough to review cold; the handoff has the detail)
--------------------------------------------------------------------
Paloma's Orrery serves a browser gallery of solar-system orbits. Stage 2 built
an exporter that READ the desktop orrery's legacy orbit cache
(`orbit_paths.json`, 1501 accreted entries) and served position traces + a
coverage index to the gallery. Testing found the served Charon/Pluto TRACES
were frame-contaminated: heliocentric points (~35 AU) mixed with correct
barycentric points under a barycenter-named cache key -- from a fetch made
before the `@9` center override existed. The desktop is immune (it draws orbits
from osculating elements, not the traces); the gallery is exposed (it serves
the raw traces). The extent of contamination across 1501 entries is unknowable,
and the desktop's `merge_orbit_data` merges by date with NO frame check.

THE PIVOT under review: stop reading the legacy cache for the gallery. Build a
clean, purpose-built gallery cache by FETCHING FRESH from Horizons with the
correct center per object, stored in the GALLERY repo, refreshed by a NIGHTLY
BATCH, validated on write by a magnitude frame guard (`#F`) so contamination
can't enter by construction. The legacy cache stays untouched for the desktop.
Almost all of Stage 2 (schema, v4 osculating-primary model, invariants, served
format, `#F` guard) carries forward; only the SOURCE changes.

DECIDED by Tony: fetch-fresh (not validate-or-refetch); nightly batch; cache in
the gallery repo; ~1 year historical depth to start.

OPEN CHOICES in the handoff (with Opus's leans): (1) intermediate raw cache +
derive served files [lean yes] vs direct-served; (2) run nightly on desktop
Task Scheduler now, GitHub Action later [lean this] vs Action from the start;
(3) daily cadence, ~1yr-each-way rolling ever-growing archive; (4) object list
= tranche first, grow to a curated catalog, as a gallery-repo config.

--------------------------------------------------------------------
WHAT TO REVIEW (please address each)
--------------------------------------------------------------------
1. THE PIVOT ITSELF. Is fetch-fresh-and-rebuild the right response, or is
   validate-or-refetch / a hybrid / a targeted repair actually better given the
   cost? Is there a failure of reasoning in "the extent is unknowable, so
   rebuild"? Would you pivot the same way?

2. THE OPEN CHOICES (1-4). For each, is the lean sound? Call out any you'd
   decide differently and why. Especially choice 3 (see risk below).

3. THE RISKS SECTION in the handoff. Weigh each; then find risks NOT listed.
   Give particular scrutiny to:
   - GIT GROWTH: nightly commits of a growing cache into the gallery repo vs
     git history / clone size / the same-repo serving model. Is "ever-growing
     archive committed nightly" self-defeating? What's the clean pattern?
   - NIGHTLY ATOMICITY: what must be true so a failed/partial run never
     corrupts or shrinks the gallery cache?
   - STANDALONE vs REUSE: is reimplementing the Horizons fetch a parallel-
     pipeline maintenance trap, or the right price for repo separation?
   - `#F` THRESHOLD (0.5 AU): does it generalize beyond the 9 test objects to
     distant irregular moons, NEOs, comets -- or does it need to be
     parent/frame-aware?

4. WHAT'S MISSING. Any consideration absent entirely from the handoff --
   provenance, reproducibility, versioning of the served schema, how the
   browser consumes it, testing strategy for the builder, how a re-fetch
   reconciles with already-served data, licensing/attribution of Horizons data?

5. STAGE 2 CARRY-FORWARD. Is anything being wrongly discarded, or wrongly
   retained? (The claim is: only the source changes; everything else survives.)

6. THE SOURCE-SIDE `merge_orbit_data` FRAME GUARD proposed for the DESKTOP
   cache (optional hardening, separate ledger item). Worth doing, or scope
   creep? Would it have prevented the original contamination?

--------------------------------------------------------------------
DELIVERABLE (what to hand back to Tony)
--------------------------------------------------------------------
A review Tony carries back to Opus, structured as:
- Per-item verdict: SOUND / CONCERN / REDIRECT, one line each.
- New risks not in the handoff, ranked by how expensive they'd be to discover
  AFTER the build.
- A recommended convergence: which way each open choice should go, and any
  architecture change you'd make before the manifest is written.
- One explicit answer: would you build this, as-is, after your fixes -- yes/no.

Keep it broad and honest. If two rounds would help (you flag, Opus revises, you
re-check), say so.
