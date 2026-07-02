I am Tony Quintanilla -- retired PE/engineer, artist, and anthropologist, and
sole developer of Paloma's Orrery (palomasorrery.com), a Python/Plotly climate
and solar-system visualization suite (~115 modules, ~86K lines) across two
repos. It is an educational and artistic project: my daughter Paloma is its
namesake and first audience, and I hold that the work should be not just correct
but beautiful -- the two usually turn out to be the same thing.

I work with Claude in a "collegial relay": I carry context between model
instances, I hold sole commit authority, and all code changes are manual (you
have read-only repo access).

THIS IS A PLANNING SESSION -- not design, and not even pre-design. Map the
territory and lay out options with tradeoffs across a few fronts, so I can see
the shape of the work before committing to any of it. Do NOT design
implementations, specify data formats, or settle architecture -- that is for
later passes if and when we get there. Stay at the altitude of "here are the
paths, here is what each costs and buys." Options I can weigh, not decisions or
builds. You widen the space; I converge.

And widen it boldly. I want more than a tidy-up review -- think about where this
project could GO: new capabilities, new forms, reach and teaching ideas,
aesthetic directions, things I have not considered. Do not shrink an idea
because it is big; surface it, explained so I can understand its shape and judge
it (access is not understanding).

GROUND TRUTH:
- Main repo:    https://github.com/tonylquintanilla/palomas_orrery  (main)
- Gallery/site: https://github.com/tonylquintanilla/tonyquintanilla.github.io  (main)
- Read each at HEAD; treat repo-at-HEAD as authoritative over anything I paste
  or you recall. If you cannot fetch, say so and I will upload.
- Fetched, not recalled: do not state hosting prices/tiers/limits (or any
  numeric fact) from memory -- verify with a source or mark it unverified.
  Hosting terms change constantly.

FRONTS (keep separate; all at planning altitude):

1) CODE -- structural-improvement candidates for the ledger.
Survey the main repo for STRUCTURAL improvements that raise capability or
efficiency -- architecture, deduplication, pipeline unification, performance,
testability -- not cosmetic edits. Give me a ranked list of candidates as
ledger-ready notes in my LEDGER_CONSOLIDATED.md convention (a
`<!-- L:NNN status:proposed -->` block, brief problem / proposed change /
rationale, and a blast-radius estimate). Rank with my existing RICE method
(Reach, Impact, Confidence, Effort) as the ledger already applies it -- use it,
do not invent a scheme. Flag anything touching the parallel position pipelines
or the gallery/orrery split (a fix in one path usually needs the sibling
audited). Before flagging any code as dead or duplicate, confirm which path is
LIVE -- grep for callers, not imports; the repo has known dead code, and the
render is ground truth over the code as read. Protocol and skills are OUT of
scope -- that review is already in flight in a separate session.

2) DOCUMENTATION -- especially the README.
The README is known-stale. Review it and the top-level docs as both a newcomer
and a maintainer six months out; give concrete proposed edits with rationale,
not vague notes. Public docs are public claims -- hold them to the same
provenance standard as the code, and spec a data-attribution / credits page
covering every dataset the project uses (JPL Horizons, Copernicus/ERA5, NOAA
Coral Reef Watch, IPC, HDX). Flag any claim that cannot be sourced.

3) PUBLICATION -- my biggest challenge, and the main thing I want your judgment on.
Current channels: the GitHub repos; palomasorrery.com as a GitHub Pages static
site (the gallery); Instagram @Palomas_Orrery; PyInstaller for Windows/Mac/Linux
desktop binaries. Stated preference: web hosting, if it can be done with low
overhead and run efficiently.
Surface the fork before recommending anything -- the project has two very
different artifacts: (a) the gallery = static exports, already web-hosted and
working; and (b) the interactive generator = a Tkinter desktop GUI making live
data calls, which cannot simply be "web hosted" as-is. The climate/earth-system
gallery is already a proven precompute -> static-HTML pipeline -- the
low-overhead model I want -- so part of the question is how much of the
interactive orrery could also collapse to precomputed scenes rather than needing
a live backend.
Map the main paths -- desktop binaries, a hosted web-framework port,
client-side-in-browser, hybrid/precompute, and any others you see -- with honest
tradeoffs on reach, ongoing cost/effort, and what decision each commits me to.
Verify current hosting facts rather than recalling them. A caching layer for the
data already exists in the repo -- do not propose rebuilding it. Do NOT go into
data formats or the data path itself; that is a pre-design question for later.
End with a recommended sequence and the one or two decisions you need from me
before the next round.

4) OUTREACH (Instagram @Palomas_Orrery) -- a mini-front, tied to publication.
If a chosen path can auto-emit shareable stills or short animations from the
scenes the gallery already produces, the channel feeds itself instead of being
hand-fed. Sketch whether that is a byproduct of a web build or a small dedicated
exporter. Keep it lightweight -- a reach multiplier, not a new product.

Before wide release (binaries or hosted): I will need to settle an open-source
license and the attribution page (front 2). Flag license-compatibility issues
with any dependency or data-usage terms and recommend a license fit for an
educational open project.

DATA NOTE: large data (star catalogs, ephemeris cache, climate reanalysis) lives
locally, is gitignored (bigger than the repo allows), and the copy in the
released repo is stale -- do not size anything off it. Some datasets in the local
store are ARCHIVED and unused; ignore them. The star data is archived but still
USED. If the planning ever needs the current data picture I will generate a
manifest on request -- but data types and formats are a pre-design concern, not
for this pass.

SEPARATE SESSION: the food-insecurity (IPC) publication is being planned on its
own, as it carries a different duty of care. Here, IPC appears only as a data
source in the attribution page (front 2) -- do not design its publication in
this pass.

HOUSE RULES:
- Options with tradeoffs, not a single verdict, until I have converged. Each
  round should get SIMPLER, not more complex. Widen boldly, then let me
  converge. Do not build.
- Honest status: if something is unverified, unknown, or unsourceable, say so and
  flag it -- do not paper it with a plausible value or a confident summary.
- You tend (per your own system card) to stop after one round and call it good;
  push past "good enough."
- Explain ambitious ideas so I can understand and judge them, not just admire the
  answer. The conversation is where the planning happens.

Deliver in whatever length it takes; thorough over fast. I will redirect front by
front.
