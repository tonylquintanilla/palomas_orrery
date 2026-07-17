# Fable Task: README Refresh — Best-Practice Rewrite (Do-Now Half)

**To:** Claude Fable
**From:** Tony Quintanilla, relayed via Claude Sonnet 5 (Mode 7 collegial relay)
**Base:** orrery HEAD `2991a0c7220a4d6d30095e474c684538460c5f68`
**Ledger:** L-062 (this item's full context and history)

## What this is, and how it differs from a design session

This is a request to produce an actual replacement `README.md` — a real
diff, not an exploration. Tony wants real latitude on structure and
wording: **improve the README to best practices**, using the five purposes
below as the brief, not a rigid outline to fill in mechanically. If you see
a better way to organize or present something than what's suggested here,
take it — that's the point of asking for a fresh, broad read rather than
patching the existing document paragraph by paragraph. Tony's own words:
"I'm open to suggestions from you and Sonnet."

This is the **do-now half** of a two-part item. The other half — rewriting
the "Web Gallery" section to describe the in-progress interactive
assembler — is explicitly **out of scope**, see below.

## The five purposes (Tony's framing, verbatim)

The README should serve, in order:

1. General information about the project.
2. References to key organizational structure and relevant documents —
   focused on the orrery, may mention the gallery too — written for **the
   developer**, even though the repo is public.
3. Orientation about cloning and using the repo — especially that the
   released data files are **not** in the active repo.
4. Reference to the gallery and its use **as it currently, publicly
   exists** — not the planned interactive work, which isn't publicly
   linked yet.
5. A brief mention of data sources and citation discipline.

This is a real reframing, not just a content refresh: the current README's
audience is a non-technical end user being walked through installing
Python for the first time (a multi-page "Step-by-Step Installation Guide
for Beginners" with screenshots-in-prose, PATH environment variable
troubleshooting, etc.). The refreshed README's primary reader is a
developer — Tony himself in a future session, another AI instance picking
up the project, or a genuine outside contributor. That doesn't mean delete
all onboarding content, but the *emphasis and tone* should shift — lead
with what the project is and how it's organized, not with a beginner's
walkthrough. Use your judgment on how much of the current beginner content
to keep, trim, or move to a separate doc; this is exactly the kind of
structural call Tony wants your read on.

**One piece of this is a decisive cut, not just a tone shift (Tony,
2026-07-17):** the current Quick Start section leads with "Standalone
Executables (No Python Required)" — Windows/macOS ZIP downloads, a
step-by-step extract-and-double-click flow, and a link out to an external
Google Sites/iCloud page for the macOS build. **This distribution channel
has no consumers and is seldom updated** — Tony's own words. Tony's only
actively maintained surfaces are the GitHub source repo and the gallery
(palomasorrery.com). Cut the standalone-executable instructions and the
Google Sites/iCloud link from the primary flow — don't just soften them.
A single line acknowledging pre-built executables exist via GitHub
Releases but aren't the actively maintained path is enough, if you want
any trace of it at all; the full ZIP/extract/double-click walkthrough for
each OS should go.
**Keep the distinct thing that's tangled up with this:** cross-platform
SOURCE compatibility (Python 3.11-3.13 on Windows/macOS/Linux, the
tkinter/pillow notes, "cross-platform compatibility achieved January
2026") is genuine, useful developer information — a reader wants to know
the codebase runs on their OS. Don't cut that just because the packaged-
executable distribution around it is going.

**Same cut applies to "Staying Up to Date" (Tony, 2026-07-17) --** verified
in the current README: a three-platform "Easy update (recommended)" table
(`UPDATE_CODE.bat` / `update_code.sh` / `update_code.desktop`, all
double-click, all serving the same non-git-user population as the
executables above -- Tony's own assessment: no consumers). Cut the table
and the double-click framing. Keep the bare git commands already in the
README's "Manual update" block (`git init`/`remote add`/`fetch`/
`reset --hard` for first-time, `git pull` after) as THE update
instructions -- that's the actual developer path, currently buried under
the table rather than leading. One line acknowledging the double-click
scripts exist is enough if you want any trace at all. Small naming
mismatch while you're auditing links anyway: the repo file is
`_UPDATE_CODE.bat` (leading underscore), the README calls it
`UPDATE_CODE.bat` (no underscore) -- reconcile either way.

**Framing suggestion, not a mandate (corrected per Tony, 2026-07-17):** the
actual throughline isn't "code for developers, gallery for viewers" as two
parallel intended audiences — it's simpler and more honest than that. The
code exists first and foremost for Tony himself: primary user and
developer both, a personal tool built for his own exploration and
learning. He'd like to share its value with others. Since it turns out
there's little interest in people actually running the code themselves,
the gallery — and now the interactive work in progress — is how that
value becomes accessible to someone who wants to see it, not compile and
run it. That's why "developer" is the right frame for this repo
specifically: anyone reading the code (a future Tony session, another AI
collaborator, a rare interested contributor) is functionally in the same
position Tony is in — engaging with the mechanics, not just the output.
Worth conveying this plainly in your own words for purpose #1 — not as
two audiences the project was designed for, but as one person's tool that
he'd like to be useful to others, and the gallery as the actual path
that's turned out to work for that.

## Concrete findings from this session — fix these regardless of anything else

Verified directly against live HEAD, not assumed:

- **Every doc cross-reference link in the current README is broken.**
  `MODULE_INDEX.md`, `climate_readme.md`, `social_media_readme.md`,
  `web_gallery_handoff.md`, `wet_bulb_temperature_readme.md` are all
  linked as repo-root-relative (e.g. `[MODULE_INDEX.md](MODULE_INDEX.md)`),
  but all five actually live under `documentation/`. Confirmed by direct
  path check against HEAD — these 404 on GitHub today. `MODULE_INDEX.md`
  fixes itself now that the file has moved to root (see below) — just
  leave that link as-is, root-relative, and it'll resolve correctly. The
  other four still need their link syntax corrected to point into
  `documentation/` (or ask whether any of them should also move to root —
  flag it rather than deciding, that's a separate judgment call Tony
  hasn't made). Check for other broken links while you're in there rather
  than trusting this list is exhaustive.
- **Module/LOC count is wrong -- and now has a canonical source.** README
  claims "75+ Python modules, over 78,000 lines of code." Verified current
  count (via `module_atlas.py`, freshly regenerated this session):
  **121 modules, 955 public functions/classes, 91,984 non-blank lines.**
  Use these, not the README's old figure or any other number you might
  compute a different way (blank-line-inclusive counts, for instance,
  land closer to 106,000 -- use the atlas's own convention, non-blank,
  since that's now the project's canonical counting method). Consider
  phrasing this so it doesn't calcify into another stale number: e.g.
  "see MODULE_ATLAS.md for current module/line counts" reads better long
  term than hardcoding a count that's already been wrong three different
  ways across three different documents this year. Also: the "Development
  Complexity" prose around this claim may need a light touch if the
  framing (team-size ratio, etc.) reads oddly against the corrected scale.
- **MODULE_ATLAS.md and MODULE_INDEX.md no longer diverge -- one script,
  one scan, both outputs (L-127, this session).** `module_atlas.py` now
  generates BOTH files from a single AST scan pass and writes both to
  repo ROOT (not `documentation/` -- also fixes the README's broken link
  at its root cause, see above). MODULE_INDEX.md used to be hand-written
  narrative prose, 4 months stale, with its own third wrong module count
  (88 files, a number that agreed with neither the atlas nor reality).
  It's now MECHANICAL: each module's description is pulled straight from
  its own docstring (via the same extraction the atlas uses), grouped
  into the same thematic sections it always had (Core Applications,
  Orbital Mechanics & Calculations, Cache Management, etc. -- reconciled
  against the atlas's role tags, one tag now mapping to one friendlier
  section title). This means MODULE_INDEX.md reads a bit plainer than its
  old hand-curated self for modules with thin docstrings -- that's
  deliberate (a visible incentive toward better docstrings, not something
  to paper over by writing fresh prose yourself for the linked document).
- **No visible Requirements citation** (Tony's original complaint that
  started this item). `requirements.txt` is attached — read it in full.
  It carries real, carefully-maintained content that's currently invisible
  from the README: pinned-version rationale (kaleido locked at 0.2.1, with
  the specific reason why), a full Python 3.14 compatibility section
  (which packages break, which don't, what to monitor, with GitHub issue
  links), and the Plotly 6.x/kaleido 1.0 migration path for later. The
  README currently just says `pip install -r requirements.txt` and shows
  a sample `pip list` output — none of the actual reasoning surfaces. Give
  this a real, visible section — not necessarily reproducing every code
  comment, but a developer scanning the README should come away knowing
  the Python version story and why kaleido is pinned, without having to
  open a second file.
- **Last-updated stamp is 2+ months stale** (May 4, 2026 / v2.9.0) and its
  changelog line doesn't mention the entire Phase 2 gallery-cache-builder
  track that's landed since (see "What NOT to touch" below for why the
  gallery section itself is out of scope — but the changelog line and
  date stamp are fair game to update to reflect that *something* shipped,
  described at whatever level of generality fits purpose #1).

## What NOT to touch

- **Do not describe the in-progress interactive gallery / Solar System
  Assembler.** This is the Phase 2 work (ledger L-098 onward, including
  this week's trust-measurement build) — unreleased, not publicly linked,
  and still changing. The "Web Gallery" section should continue to
  describe the CURRENT, live, publicly-linked experience only:
  palomasorrery.com, the desktop-app HTML export -> `json_converter.py`
  -> GitHub Pages pipeline. Describe that pipeline accurately (the
  attached README has a reasonable existing description of it to start
  from), but do not add anything about Pyodide, the assembler, feature
  configs, trust/served_window, or any of this week's work. That's a
  separate, later ledger item once it's actually live.
- Do not invent version numbers, dates, or feature claims you can't
  support from the attached files. If something in the current README
  looks like it might be stale but you can't verify it from what's
  attached, flag it as an open question rather than guessing either way
  (keep it, cut it, or change it) — same "verify or flag the gap" rule
  this project uses everywhere else.
- Do not touch `LICENSE.md`, copyright year, or the license section's
  legal text.

## What to upload alongside this prompt

1. **This prompt.**
2. **The current `README.md`** in full — the thing being replaced.
3. **`requirements.txt`** in full — read carefully; this is the source
   for the new Requirements section.
4. **`DATA_INVENTORY.md`** — for purpose #3 (what data exists, what's
   gitignored, sizes).
5. **`MODULE_INDEX.md`** -- freshly regenerated this session, now at repo
   ROOT (not `documentation/` -- that copy is the old hand-written one,
   about to be renamed to an archival file; don't use it). Mechanical,
   docstring-sourced, grouped by role -- use it as the ground truth for
   what modules exist and what they do, but its plainer prose is not
   something to copy verbatim into the README's own inline module tables;
   write those the way you judge best for purpose #2's developer
   audience.
6. **`MODULE_ATLAS.md`** -- also freshly regenerated, same scan as the
   index, also now at root. Optional: much longer, more for AI-assisted
   deep queries than this pass needs, but useful if you want more context
   on how modules relate (dependencies/consumers) than the index shows.
7. Optionally, for purpose #5 (citation discipline): the first page or
   two of `PROVENANCE_AUDIT.md` is enough to characterize the practice
   accurately — the README only needs a brief, honest mention, not a
   summary of the whole audit.

## Output format

- The full replacement `README.md` text, ready to review.
- A short separate note listing what you changed and why, organized by
  the five purposes plus the concrete-findings list above — so Tony and
  Sonnet can review against the brief efficiently rather than diffing
  blind.
- Anything you're genuinely unsure about (kept vs. cut content, tone
  calls, claims you couldn't verify from the attached files) called out
  explicitly as open questions, not silently decided.

## Conventions in force (same project, same rules)

- Fetched-not-recalled: base claims on the attached files, not
  recollection of what READMEs like this usually say.
- Flag anything you want routed back for a decision rather than deciding
  it silently on Tony's behalf.
- Tony is the integrator and holds final review; this produces a
  reviewed diff, not a merge.

---
Prompt written July 2026 by Claude Sonnet 5 for Tony Quintanilla's Mode 7
relay.
