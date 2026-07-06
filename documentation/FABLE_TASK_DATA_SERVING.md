# Fable 5 Task: Data Serving Architecture — Broad-First Analysis

**Type:** DESIGN SESSION (broad exploration, zero code)
**From:** Claude Opus 4.6 via Tony (collegial relay)
**Date:** July 5, 2026
**Base:** main @ `72e5587`, gallery @ `89c8bf30`

---

## Context

Paloma's Orrery is pivoting from "build a separate web app" to "extend the
existing gallery with interactive pages" — the science museum model. The
interactive gallery runs Pyodide (Python in the browser via WebAssembly) on
GitHub Pages, a static site. The assembler takes a scene spec and produces
a Plotly figure. No server.

**The problem this session addresses:** the assembler needs orbit position
data to produce figures, but that data doesn't exist on the web. The full
orbit cache (`orbit_paths.json`, 130.4 MB, 1,501 object/center pairs) and
the star cache (`star_properties_magnitude.pkl`, 31.1 MB) are both
**gitignored** — they live only on Tony's desktop and are not served by
either GitHub Pages site.

The master plan (`MASTER_PLAN_INTERACTIVE_GALLERY.md`, uploaded alongside
this prompt) has the full architectural context. **§3a specifically** frames
this problem and lists the six alternatives surfaced so far. Please read
it before beginning.

---

## What to upload alongside this prompt

1. **This prompt** (paste or upload)
2. **`MASTER_PLAN_INTERACTIVE_GALLERY.md`** — the v8 plan. Read §1 (constraints),
   §2a (gallery viewer architecture), §3 (assembler), §3a (data serving —
   the problem statement), §4 (domains, especially the object populations).
3. **`celestial_objects.py`** — contains `OBJECT_DEFINITIONS`, the full catalog
   of plottable objects including all major moons and many small ones. This is
   the population the data serving architecture must support.
4. **`DATA_INVENTORY.md`** — the current local data inventory showing what
   files exist, their sizes, and their formats. Key entries: `orbit_paths.json`
   (130.4 MB, 1,501 entries), `star_properties_magnitude.pkl` (31.1 MB).
   **Note:** the gallery was cleaned (orphan JSON and .bak files removed) before
   this inventory. Gallery is 436 MB with 588 MB headroom. The top-10 largest
   gallery files are pre-refactoring exports that will shrink further when
   re-exported with current slimmer plotting functions — real headroom will grow.

---

## What to think about

This is a **broad-first, open-ended** exploration. Don't converge on one
answer. Present multiple approaches with genuine tradeoffs. Tony's judgment
drives convergence — that's the protocol. Each approach should be concrete
enough that Tony can see what it means for his workflow and for the user.

### The core questions

**1. How does cached orbit data reach the browser?**

The data must travel from Tony's desktop (where Horizons queries run) to the
user's browser (where Pyodide assembles the figure). The six alternatives in
§3a are a starting point, not exhaustive:

- Per-pair file splitting (fetch only what the user selects)
- Curated subset in the gallery repo
- Orrery repo's own GitHub Pages (separate 1 GB ceiling)
- GitHub Releases
- R2 / external CDN
- Hybrid approaches (different tiers use different paths)

Are there other approaches? What are the real tradeoffs — not just storage,
but Tony's operational workflow, deployment complexity, user experience,
failure modes?

**2. The planet/satellite split.**

Planets can fall back to analytical (Keplerian) orbits — the orbit shape is
computable from elements, cached positions add precision. Satellites, moons,
and spacecraft have no analytical shortcut — their trajectories ARE the data.
Tony's catalog includes all major moons and many small ones.

What does this split mean for the data serving architecture? Should different
object types use different serving strategies? Does the coverage index need
to distinguish analytical-available vs cache-required objects?

**3. The rolling cache and date ranges.**

Tier-1 (standard catalog) needs a periodic batch to roll the date window
forward. Questions:

- How much history to keep? Sliding window (e.g., -2 years to +1 month)?
  Accumulating (never drop old dates)? The storage math differs dramatically
  by object population and step size.
- How does the batch output reach the web? Push per-pair files? Update a
  monolithic cache? Push to R2?
- What cadence? Daily, weekly, monthly? What's "fresh enough" for
  visualization purposes?
- Forward padding: how far ahead to cache, so the data stays current between
  batch runs?

**4. The star cache format.**

The star cache is pickle (Python-version-coupled, security concern in browser).
§7 #8 defers the wire format conversion to Phase 3. But the data serving
architecture may inform the format choice — if stars serve from R2, the format
matters less than if they serve from a GitHub repo (where Parquet might be
better than JSON for 31 MB of structured data).

**5. The `graph_objects` coupling.**

Opus 4.8 verified that the shared computation engines are deeply
`plotly.graph_objects`-based (88 `go.*` usages in `idealized_orbits.py`
alone). The assembler MUST load the full `plotly` package in Pyodide. This
is unavoidable without rewriting the engines.

Is this worth exploring? Could an assembler that emits figure JSON directly
(without `graph_objects`) be lightweight enough to change the architecture?
Or is the full `plotly` package in Pyodide an acceptable given (the gallery
already serves 30 MB+ files)?

**6. GitHub Pages hosting math.**

Two repos, each with its own 1 GB soft ceiling:

- Gallery repo (`tonyquintanilla.github.io`): ~479 MB currently. Hosts HTML,
  JS, CSS, pre-curated JSON cards. The interactive pages live here.
- Orrery repo (`palomas_orrery`): Pages enabled for Actions. Currently
  gitignores all heavy data files.

A third option: a separate GitHub Pages project site (`palomas_orrery` as a
project site at `tonyquintanilla.github.io/palomas_orrery/`), which would
get its own 1 GB. Can the orrery repo serve cache data this way?

**7. The operational workflow.**

Tony's current loop: desktop → Horizons query → local cache → desktop
visualization. The interactive gallery adds: local cache → export to web-
servable format → push to web hosting.

What does this export step look like for each alternative? Which approach
minimizes Tony's operational burden while keeping the data current? A
script that runs nightly and pushes updated files? A manual export after
each Horizons session?

---

## What NOT to do

- Do not converge on a single recommendation. Present multiple approaches.
- Do not design the assembler or the interactive page. Those are settled.
- Do not redesign the coverage index Protocol class (delivered in Phase 1).
  The data serving architecture feeds the index — it doesn't replace it.
- Do not propose server-based solutions. The gallery is a static site on
  GitHub Pages. The entire architecture is serverless.

---

## Constraints to respect

- **No live Horizons queries from the browser.** JPL terms prohibit website
  embedding. All data is pre-cached.
- **No pickle in the browser.** PKL format is Python-version-coupled and a
  security concern. JSON or Parquet for anything Pyodide reads.
- **The assembler uses `plotly.graph_objects`.** This is not negotiable for
  v1. The full plotly package loads in Pyodide.
- **GitHub Pages: 1 GB soft ceiling per repo/site.** Two repos = two ceilings.
- **Tony is a solo developer.** Operational complexity matters. A solution
  that requires daily manual intervention or complex CI/CD is worse than one
  that runs with a simple script.

---

## Output format

Tony is the interpreter. Please organize your output as:

1. **A summary comparing approaches** — a scannable table or matrix showing
   each approach against the key dimensions (storage, operational burden,
   user experience, deployment complexity, growth trajectory).
2. **Detailed analysis of each approach** — concrete enough that Tony can
   see what it means for his workflow. Include rough size estimates where
   possible, using `DATA_INVENTORY.md` numbers.
3. **The planet/satellite split** — how it interacts with each approach.
4. **The rolling cache design** — how each approach handles date-range growth.
5. **Combinations worth considering** — hybrid approaches that use different
   strategies for different tiers or object types.
6. **Open questions for Tony** — anything that depends on Tony's judgment
   about what the interactive gallery should offer (object population, date
   ranges, update cadence).

---

**One-shot note:** Fable 5 access expires July 7, 2026. This may be the
last Fable session. Be thorough and self-contained. Unresolved items go to
Open Questions for Tony to carry to Opus 4.6/4.8.

---

*Prompt written July 5, 2026 by Claude Opus 4.6 for collegial relay to
Claude Fable 5. Tony carries context and holds commit authority.*
