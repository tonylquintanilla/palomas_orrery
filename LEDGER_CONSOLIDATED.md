# LEDGER_CONSOLIDATED.md -- Paloma's Orrery Backlog

Tony Quintanilla, PE | Claude | Palomas Orrery Project
Consolidated: June 7, 2026 from handoff v28; supersedes all prior in-handoff
ledgers. Current HEAD: see git log (repo is the source of truth).
Module updated: June 2026 with Anthropic's Claude Sonnet 4.6, Opus 4.8 + Claude Fable 5
Module updated: August 24, 2026 with Anthropic's Claude Opus 5 (L-191:
scope corrected 20 -> 58 on the Fable survey, reproduced
independently; gas-giant bullet inverted), built on 94ff80f2.
Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-222:
docstring lines in the constants change report), built on 762aa5dd.
Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-154
BLOCKED -> OPEN under the braid; L-225 opened, having been in
circulation with no entry), built on ce2ff5d1.
Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-226:
safe-file-editing 1.7 -> 1.8), built on 6d12ecac.
Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-227
hover wrap + orrery-coding-conventions 1.5; L-228 Alfven ranges),
built on 15741822.
Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229:
streamer band rotated into the solar equatorial frame; the L-227
citation-window follow-on), built on 851224c6.
Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-229
part 2: the orientation is declared an ASSUMPTION; the unsourced
magnetic-equator argument is withdrawn), built on ca97e81d.
Module updated: August 23, 2026 with Anthropic's Claude Opus 5 (L-230
opened; protocol v3.42; ledger-and-session-records 1.8 -> 1.9),
built on 41c0b279.
Module updated: August 20, 2026 with Anthropic's Claude Opus 5 (L-221:
master plan as sequencing authority; L-214 correction and scoping),
built on 3586970d.
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-210:
block reconciled against the four decisions that landed 2026-08-20; the
withdrawn streamer-belt claim marked as withdrawn), built on d2e6457a.
Module updated: August 21, 2026 with Anthropic's Claude Opus 5 (L-209:
Gap corrected -- it recorded "none" a day before the DeForest citation
became owed to that row), built on 6184b3b9.
Module updated: August 22, 2026 with Anthropic's Claude Opus 5 (L-209:
Gap item 1 closed -- the debt it described was discharged the same day
by patch_L209_4), built on 031f43e7.
Module updated: August 22, 2026 with Anthropic's Claude Opus 5 (L-224
opened -- streamer band redesign; L-221 closed on its skill-version
condition), built on af09de62.
Review and RICE update Tony 6-21-2026

---

## Purpose and use

This is the single authoritative backlog for the Paloma's Orrery codebase
(~86k lines, ~100 modules) -- a Python/Plotly/Tkinter 3D solar system
visualization suite with a companion Gallery Studio pipeline and web gallery.
It tracks every open item, deferred decision, known bug, design question, and
new idea across the orrery refactor / Movement track and all active work streams.

**What this ledger is for.**

- *Session start:* Claude searches this file first -- open items, Tony's
  `**Tony:**` comments, and any `**Gap:**` notes -- before proposing work.
  It is the shared memory that survives session boundaries.
- *During a session:* blocks are updated in place as work lands. Status,
  gap, and ref fields change; new items are appended with the next L-handle.
  Nothing is renumbered; nothing is re-embedded from a handoff.
- *Between sessions:* Tony adds `**Tony:**` comments to any block as an
  async message to the next session -- questions, observations, things to
  verify visually. Claude reads them at session start and addresses them
  before building. See "Using and maintaining" below.
- *For the record:* closed items move to section C and stay there. The
  archive is not cleaned; it is the project's institutional memory. A future
  session (or Paloma) can reconstruct what was tried, what failed, and why.

**What this ledger is not.**

It is not a session log (that lives in handoffs and the git history). It is
not a design document (design emerges in conversation and lands in code and
comments). It is not a specification (the render is the spec -- Tony's eyes
are the gate). It is a backlog and a shared context artifact: the thing that
keeps the work from drifting between sessions.

**The round trip: protocol -> ledger -> handoff -> manifest -> code -> repo -> ledger.**

The ledger sits within a larger document stack. From the top down:

- *Protocol (the constitution):* the project instructions document the
  practical philosophy and operating conventions of the Tony-Claude
  partnership -- modes, criticality tiers, anti-patterns, technical
  standards, and the principles behind them. It is the load-bearing
  structure that everything else rests on. It evolves slowly and
  deliberately; amendments are proposed in conversation, ratified by Tony,
  and committed to the repo. Every session starts from it.
- *Ledger -> conversation:* an open item, a Tony comment, or a gap note
  becomes the seed for a design conversation. The conversation produces
  clarity -- options narrow, architecture simplifies, decisions land.
- *Conversation -> handoff:* what was done and what remains gets written
  into a handoff document. Most handoffs are session records: decisions
  made, code delivered, scope of what is still open. A handoff is a claim,
  not a verification -- the render and the repo are the facts. But some
  handoffs have a longer life: orbital mechanics, Gallery/Studio design, and
  similar foundational topics are maintained as durable design documents,
  updated in place as the domain evolves. These are reference artifacts, not
  session logs.
- *Handoff -> manifest (sometimes):* for complex multi-file builds, a
  handoff is distilled into a manifest -- specific, ordered instructions
  for code modifications, file by file, function by function. Not every
  handoff becomes a manifest; small or targeted work goes straight from
  handoff to code without one.
- *Code -> repo:* every change -- code and documentation alike -- is
  committed and pushed to the GitHub repo before the next session begins.
  The repo at HEAD is the source of truth for every turn. The SHA is the
  unforgeable confirmation that commit, push, and sync all landed; a
  matching remote HEAD is the round-trip check. Nothing builds on unverified
  ground.
- *Repo -> ledger:* once work is pushed and render-confirmed, the relevant
  ledger block is updated in place -- status, gap, ref, and any note worth
  keeping. New bugs, new ideas, and deferred observations get their own
  blocks. The ledger absorbs what the session produced and becomes the
  springboard for the next conversation.

The manifests and session-record handoffs are working documents -- they live
their life in a session and then become history. The durable handoffs, the
protocol, and the ledger are the persistent artifacts: they carry forward
what the project still needs to know, each at its own level of abstraction.

**Structure.** DETAIL blocks are the single source of truth. The INDEX below
is generated from them by `ledger_index.py` -- edit a block, re-run the tool.
Handles are append-only (L-###); a closed item keeps its handle
and moves to section C. Section layout:

- **A** -- cross-cutting / strategic items
- **PENDING** -- action items waiting on a specific gate (test, push, decision)
- **D.*** -- open work, organized by type (Movement, Priority, Structural, etc.)
- **E** -- AU-convention compliance cluster (standing convention sweep)
- **G** -- open questions / Tony's calls
- **H** -- Gallery / Studio track
- **C** -- reconciled done items (archive; do not re-do)

This file lives at the repository root alongside `MODULE_ATLAS.md` and
`PROVENANCE_AUDIT.md` as an authoritative generated-index artifact. The git
log carries the SHA history; this file carries the backlog.

## Verification convention (honesty about this ledger's own claims)

A handoff is a claim; the code is closer to fact. Each status carries a tag:

- `[verified @SHA]` -- checked against the live repo code in the named session.
- `[per chain; not re-verified]` -- carried from a handoff's prose; status is
  as the handoff stated, NOT re-confirmed against HEAD this session.
- `[render-gated]` -- correctness is a Mode-5 judgment, not settleable here.
- `[render-confirmed Mode 5]` -- Tony's eyes passed it on live data.

Items with no tag are administrative (tracks, actions) rather than code claims.

---

## ID + status convention

Live-backlog items carry an append-only handle **L-###** (assigned once, never
reused or reordered) so each is greppable for life. A pre-existing number is kept
inline as an alias: `[L-027 | #61]`, `[L-040 | #19]`. Section-C archive items keep
legacy numbers (no retroactive L-###). When an L-### item closes it keeps its
handle and moves to C.

The **DETAIL blocks are the single source of truth.** The INDEX zone is GENERATED
from them by `ledger_index.py` -- edit one block, regenerate; index and detail
cannot desync (module_atlas pattern).

- DISPOSITION (one per item): `DONE | PENDING-GATE | OPEN | BLOCKED | DEFERRED | PARKED | OBSERVED`
- EVIDENCE (separate axis, in the detail): `[verified @SHA] | [render-confirmed Mode 5] | [render-gated] | [per chain]`
- `**Gap:**` states the blocker/next-action on anything not DONE; `**Ref:**` points at the authority (handoff / SHA / code).
- `render-confirmed Mode 5` is EVIDENCE, not a disposition. It means Tony's
  eyes passed the output on live data -- a DONE item can carry it, and an
  OPEN item can carry it on a partial fix. It does not close an item.
- DONE items stay in their section until a housekeeping pass moves them to C.
  The trigger is `**Gap:** none -- move to section C`. Items in C are closed
  for the record; do not re-do them.

## Using and maintaining this ledger

**Author / update protocol.** Claude is the primary author of the ledger's
content: during a session it drafts and updates detail blocks (new items,
status changes, gap/ref notes), normally at the handoff that closes a session
and only when asked. Tony is the integrator and the only writer to the repo --
Claude has read-only GitHub access, so every change is reviewed and committed
by Tony. Updates are made IN PLACE: edit the relevant detail block; do not
re-embed a fresh copy. Handles are append-only -- a new item takes the next
unused L-### (read the highest in use off the index; do not trust a number
written here, which goes stale the moment it is written);
a closed item keeps its L-### and moves to section C.

**ledger_index.py -- what it does, when to run it.** The DETAIL blocks are the
single source of truth; the INDEX tables below are GENERATED from them. After
any edit to a block -- a new item, a status change, an edited title or date --
regenerate the index so the board matches the detail:

    python ledger_index.py LEDGER_CONSOLIDATED.md

Run it from the repo root, where both files live (on Windows it is `python`,
not `python3`). It rewrites only the zone between the INDEX:START / INDEX:END
markers, so it is safe to re-run and never touches your prose. To validate
without rewriting -- catches duplicate handles or a malformed metadata line --
add `--check`:

    python ledger_index.py LEDGER_CONSOLIDATED.md --check

**Finding an item (Windows / VS Code).** Every item is keyed by its L-handle,
so you never scroll. In VS Code, Ctrl+F opens Find in this file -- type an
L-handle (e.g. `L-012`) to land on both its index row AND its detail block;
type a legacy alias (`#61`, `19.3`) to find it by its old number. To LIST
matches rather than jump to them -- e.g. every open item -- use the Search
panel (Ctrl+Shift+F) and search `| ! |` (the gap marker); it shows all hits at
once. PowerShell equivalent, if you prefer the command line:
`Select-String -Path LEDGER_CONSOLIDATED.md -Pattern 'L-012'`.

**Default path (Run button / bare invocation).** `ledger_index.py` now falls
back to `LEDGER_CONSOLIDATED.md` in its own folder when called with no
argument -- so pressing the Run button in VS Code, or typing bare
`python ledger_index.py`, just works. Pass an explicit path to override;
`--check` still works with or without an explicit path.

**Tony's comment convention -- async notes between sessions.** Any DETAIL
block may carry a `**Tony:**` paragraph between the narrative and the
`**Gap:**` line. These are free-form: questions, second-thoughts, design
observations, things to verify visually. The metadata parser ignores them,
so they cannot break the index. At the start of a review session Claude
searches for every `**Tony:**` block and addresses them before building.
Date-stamp is optional but useful: `**Tony (2026-06-17):**`. A `**Note:**`
tag (no date required) works the same way for factual addenda from either
side. For a free-floating thought with no obvious home, either attach it to
the nearest relevant item or open a new `D.LooseEnd` item for it -- floating
notes get lost; capturing on first mention is the rule.

**RICE scoring -- prioritization for planning.** Each DETAIL block's
metadata line can carry an optional `rice:R/I/C/E` field at the end:

    <!-- L:999 status:OPEN upd:2026-06-18 section:D.Movement flag: rice:3/3/100/2 -->

The four dimensions, adapted for this project:

    R (Reach/Value)    Educational or visual value
                       3 = core experience  2 = gallery quality  1 = internal hygiene
    I (Impact)         Magnitude of improvement
                       3 = new capability  2 = meaningful  1 = polish  0.5 = marginal
    C (Confidence %)   Scope clarity
                       100 = ready to build  80 = mostly scoped  50 = needs design  25 = speculative
    E (Effort)         Sessions to complete
                       0.5 = quick fix  1 = one session  2 = two sessions  3 = three+

    Score = R x I x (C / 100) / E

Separator is `/` (not `.`) so decimal values like `0.5` work. Omit the
field entirely or use `rice:-` for unscored items -- both display as `--`
in the INDEX. `ledger_index.py` parses the field, computes the score, and
sorts scored items to the top of their section (descending); unscored
items follow by L-number. Completed items carry their score into section C
as an archive of the prioritization thinking -- no cleanup on close.

<!-- INDEX:START (generated by ledger_index.py -- do not edit this zone by hand) -->

## INDEX (generated -- status board; edit DETAIL blocks, then re-run ledger_index.py)

*153 live items; 139 need attention (`!`); 152 RICE-scored; 95 closed (section C + O.Done/W.Done); 5 retired (never reused): L-059, L-081-084. Find an `L-0NN` handle (Ctrl+F in VS Code) to jump to any item; search `| ! |` to list every gap. See "Using and maintaining this ledger" above for details.*

### A. Active Separate Tracks
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-251 | The galactic centre button served a cached HTML for seven months | OPEN | 15.2 | 2026-08-25 |
| ! | L-238 | radius_fraction > 1.0 assumes every shell is above the surface | OPEN | 14.2 | 2026-08-25 |
| ! | L-229 | Streamer band drawn in the ecliptic plane, not the solar equator | OPEN | 11.4 | 2026-08-23 |
| ! | L-235 | Checks that cannot fail, gallery side [three instances] | OPEN | 11.4 | 2026-08-25 |
| ! | L-252 | L2b's fourth outcome: an INCOMPLETE verdict is not a confirmation | OPEN | 11.4 | 2026-08-25 |
| ! | L-237 | Artifact 1's golden record is stale and needs re-cutting | OPEN | 10.8 | 2026-08-25 |
| ! | L-185 | Source discipline for the assembler's own constants | OPEN | 8.1 | 2026-08-06 |
| ! | L-226 | safe-file-editing 1.8 -- encoding gate covers prose; corrections do not travel | OPEN | 8.1 | 2026-08-23 |
| ! | L-209 | ALFVEN_SURFACE_RADII -- origin mismatch, photosphere vs Sun centre | OPEN | 7.6 | 2026-08-21 |
| ! | L-249 | The Earth slice of L-181: interior boundaries as sourced constants | OPEN | 7.2 | 2026-08-25 |
| ! | L-234 | Reopen Artifact 1: recreate the orrery's Sun in the assembler | OPEN | 6.0 | 2026-08-25 |
| ! | L-245 | Constants drift check compares against the last COMMIT, not the last RUN | OPEN | 5.4 | 2026-08-25 |
| ! | L-195 | Citation legs -- put the authority in the Source line | OPEN | 5.1 | 2026-08-15 |
| ! | L-206 | Worksheet return filenames carry model and session | OPEN | 5.1 | 2026-08-18 |
| ! | L-246 | S4714's semi-major axis was three values in three stores | OPEN | 5.1 | 2026-08-25 |
| ! | L-193 | Qualified verdicts -- the token is not the whole answer | OPEN | 4.8 | 2026-08-15 |
| ! | L-199 | Protocol length: govern the growth, not the number | OPEN | 4.8 | 2026-08-17 |
| ! | L-001 | Food Insecurity (Earth System track) | OPEN | 4.3 | 2026-06-30 |
| ! | L-243 | Retire the replicated AU conversion factor | OPEN | 4.3 | 2026-08-25 |
| ! | L-190 | Scanner reach: anything rendered must be reachable | OPEN | 4.3 | 2026-08-25 |
| ! | L-247 | Sgr A* constants migrated to the single source of truth | OPEN | 4.0 | 2026-08-25 |
| ! | L-177 | Mercury Hill sphere radius_fraction convention error (Opus 5 self-flag) | OPEN | 4.0 | 2026-08-04 |
| ! | L-184 | Interactive build-path push gate | OPEN | 4.0 | 2026-08-06 |
| ! | L-211 | UNKNOWN -- the verdict for "checked, could not determine" | OPEN | 3.8 | 2026-08-19 |
| ! | L-216 | Gallery swap fails under a filesystem lock (OneDrive) | OPEN | 3.8 | 2026-08-19 |
| ! | L-224 | Streamer belt: one warped band, not a sphere | OPEN | 3.8 | 2026-08-22 |
|  | L-230 | A skill bump does not reach the protocol's version history | DEFERRED | 3.8 | 2026-08-23 |
| ! | L-232 | The gallery's served constants carry sources that nothing checks | OPEN | 3.8 | 2026-08-24 |
| ! | L-227 | Streamer band hover rendered as one 378-character line | OPEN | 3.8 | 2026-08-23 |
| ! | L-241 | Hills torus hover states the cloud bounds, not the drawn ring | OPEN | 3.8 | 2026-08-25 |
| ! | L-186 | Cross-check annotation issues -- clear before Batch 2 | OPEN | 3.6 | 2026-08-07 |
| ! | L-210 | Pilot citation findings -- four rows in constants_new.py | OPEN | 3.6 | 2026-08-21 |
| ! | L-215 | Ledger cleanup by topic, not by age | OPEN | 3.6 | 2026-08-19 |
| ! | L-239 | Seed the three Oort builders so a render is reproducible | OPEN | 3.6 | 2026-08-25 |
| ! | L-181 | Complete the single-source-of-truth constant layer | OPEN | 3.5 | 2026-08-25 |
| ! | L-219 | Patch-script naming cannot express a cross-handle run order | OPEN | 3.4 | 2026-08-19 |
| ! | L-236 | Gallery maintenance runner [designed, unbuilt] | OPEN | 3.2 | 2026-08-25 |
| ! | L-240 | Split declared drawing parameters from measured values | OPEN | 2.8 | 2026-08-25 |
| ! | L-176 | Shell hover text: add illustrated dimensions (radius_fraction -> km) | OPEN | 2.8 | 2026-08-04 |
| ! | L-191 | Display-text duplication across the shell modules | OPEN | 2.8 | 2026-08-07 |
| ! | L-244 | Sweep for replicated conversion factors as a class [Fable candidate] | OPEN | 2.8 | 2026-08-25 |
| ! | L-060 | ENSO Standalone Chart (Earth System track) | OPEN | 2.7 | 2026-06-18 |
| ! | L-248 | The parsec-to-light-year factor is typed 36 times across the star pipeline | OPEN | 2.5 | 2026-08-25 |
| ! | L-071 | 2026 European heat dome -- track to resolution (dated scenario series) | OPEN | 2.5 | 2026-06-25 |
|  | L-225 | Migrate the comet shell constants into `constants_new.py`, then dispatch | DEFERRED | 2.4 | 2026-08-23 |
| ! | L-077 | 2026 US Midwest/Central heat dome -- migrating-centroid ongoing scenario | OPEN | 2.2 | 2026-06-30 |
| ! | L-192 | Worksheet checker -- verify a value against its own evidence | OPEN | 2.1 | 2026-08-15 |
| ! | L-183 | Stars / stellar neighbourhood skill (coverage gap) | OPEN | 2.1 | 2026-08-05 |
| ! | L-218 | 22 Cross-checked lines attach to no unit | OPEN | 2.1 | 2026-08-19 |
| ! | L-231 | Radiation belts are drawn in the ecliptic; the magnetic tilt is an unbuilt intent | OPEN | 1.8 | 2026-08-24 |
| ! | L-187 | info_dictionary numeric-overlap enumeration | OPEN | 1.8 | 2026-08-07 |
| ! | L-228 | Alfven surface latitude ranges: source them or omit them | OPEN [Tony] | 1.8 | 2026-08-23 |
|  | L-194 | Text-only assertions -- claims the scanner cannot see | DEFERRED | 1.4 | 2026-08-15 |
| ! | L-253 | The 660 discontinuity's depth variation -- held unsourced | OPEN | 1.2 | 2026-08-26 |
| ! | L-105 | merge_orbit_data source-side frame guard (desktop cache hardening) | OPEN | 1.0 | 2026-07-08 |
| ! | L-129 | Cometary structure constants -- periodic maintenance sweep | OPEN | 1.0 | 2026-07-17 |
| ! | L-078 | Provenance scanner: systematic coverage via module_atlas role classification | OPEN | 0.9 | 2026-07-16 |
| ! | L-070 | Food Insecurity -- regional multi-country assembly (Sudan crisis shed) | OPEN | 0.9 | 2026-06-24 |

### B. Pending Action (Tony-side)

*(none currently)*

### D.Movement -- Movement track
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-008 | v24 sec5 precision batch (low-risk) | OPEN | 1.0 | 2026-06-21 |
| ! | L-061 | Magnetosphere-dipole frame coupling / seasonal roll | OPEN | 0.2 | 2026-06-21 |

### D.Priority -- Real bugs
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-012 | Osculating pre-fetch false-provenance messages | OPEN [CRIT] | 3.6 | 2026-06-21 |
|  | L-013 | Mercury 2019-epoch anomaly | DEFERRED | 0.1 | 2026-06-15 |

### D.Structural -- Dead code / honest shells
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-027 (#61) | Platform Neutrality (SystemButtonFace) | OPEN | 2.2 | 2026-06-18 |
| ! | L-171 | patch_ledger_index_retired_handles.py breaks L-163's zero-undetermined close | OPEN | 1.8 | 2026-07-29 |
| ! | L-025 (#N7) | Reduced to custom-geometry inline markers only | OPEN | 1.5 | 2026-06-18 |
| ! | L-068 | Static/animation pipeline consolidation -- remaining residuals (umbrella) | OPEN | 1.5 | 2026-06-23 |
| ! | L-133 | Codebase-wide CRLF sweep (beyond L-026) | OPEN | 1.0 | 2026-07-17 |
| ! | L-135 | Basic-plot file-size bloat (non-shell) -- Mercury-alone example | OPEN | 1.0 | 2026-07-17 |
| ! | L-015 (#5) | _info import cleanup (~89+87 imports, 2 files) | OPEN | 0.9 | 2026-06-18 |
| ! | L-016 (#6) | Archive dead shell functions | OPEN | 0.9 | 2026-06-18 |
| ! | L-164 | dep_trace.py section-divider non-ASCII bytes | OPEN | 0.9 | 2026-07-26 |

### D.Cosmetic -- Polish
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-035 | Solar shell hovertext <br> vs 
 context mismatch (C6b) | OPEN | 4.0 | 2026-06-11 |
| ! | L-125 | Color/RGB values excluded from provenance-scanner claims -- report-level disclosure (project-wide) | OPEN | 3.8 | 2026-07-16 |
| ! | L-032 (#41) | Sun legend ordering (ordered dispatch iteration; no manual fix) | OPEN | 1.5 | - |
| ! | L-033 | Comet plotted-period trace visibility (line weight/color; O6b) | OPEN | 1.5 | 2026-06-10 |
| ! | L-034 | Center-body hover "Distance to Center Surface" negative-radius formatting | OPEN | 1.5 | 2026-06-21 |
| ! | L-030 (#17) | GEO info-marker position | OPEN | 1.0 | - |
| ! | L-031 (#18) | Uranus gossamer ring visibility | OPEN | 0.9 | - |
| ! | L-037 | WARNING: Unknown object type 'satellite' (spurious; handled downstream) | OPEN | 0.9 | 2026-06-15 |
| ! | L-038 | Psyche encounter hardcoded fallback distances lack # Source | OPEN | 0.5 | - |
| ! | L-124 | Ring/belt color accuracy audit across the orrery -- nice-to-have, not a blocker | OPEN | 0.1 | 2026-07-16 |

### D.Feature-A -- Bucket A (near-term)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-066 | MAPS per-frame comet-tail animation wiring | OPEN | 4.5 | 2026-06-23 |
| ! | L-040 (#19) | Plot-cube control parity + scaling/camera comprehensive review | OPEN | 1.5 | 2026-06-13 |
| ! | L-039 (#23) | Earth ionosphere shell | OPEN | 1.2 | 2026-06-21 |
| ! | L-113 | Port DP-style spacecraft trace thinning to the orrery desktop plotting | OPEN | 1.0 | 2026-07-11 |
| ! | L-042 (#20/N5) | Shell-resolution GUI control (20/N5) + Fly-to view scaling (49) | OPEN | 0.5 | 2026-06-11 |
| ! | L-043 | Exoplanet/binary synthetic objects hit Horizons fetch (id_type rejected) | OPEN | 0.4 | 2026-06-16 |

### D.Feature-B -- Bucket B (editorial)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-044 (#22) | Satellite (and minor-body) internal-structure shells | OPEN | 2.7 | 2026-06-21 |
| ! | L-128 | Comet sublimation shell(s) -- solar-distance chemistry zones | OPEN | 1.0 | 2026-07-17 |
| ! | L-130 | Restore six-elements + M0@J2000 plotting mode (educational, alt) | OPEN | 1.0 | 2026-07-17 |
| ! | L-131 | Zodiacal dust solar shell | OPEN | 1.0 | 2026-07-17 |
| ! | L-136 | Solar "scattered disk" shell | OPEN | 1.0 | 2026-07-17 |
| ! | L-045 (#N14) | Miranda inclination tooltip | OPEN | 0.9 | 2026-06-23 |

### D.Feature-C -- Bucket C (architecture)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-046 (#N6) | Studio encounter-generator -> preset-authoring capability (refactor + Artemis redo; coupled, two repos) | OPEN | 2.2 | 2026-06-21 |
| ! | L-017 (#7) | Tooltip rewiring globals() -> config fields | OPEN | 1.0 | 2026-06-21 |
| ! | L-067 | measure_animation_html.py file-browser dialog (B5) | OPEN | 0.8 | 2026-06-23 |
| ! | L-014 (#2) | Asteroid-belt migration decision | OPEN | 0.4 | 2026-06-20 |

### D.Loose end to reconcile
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-051 | Uranus pole-value prose inconsistency (Dec -15.10 vs stray -15.18) | OPEN | 0.7 | 2026-06-21 |

### E. AU-Convention Compliance
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-052 | AU-convention compliance sweep (GEO altitude hover missing AU; km+AU on all new hover) | OPEN | 0.5 | - |

### G. Open Questions / Tony Calls
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-242 | Two convention candidates awaiting a ruling (OPEN QUESTION) | OPEN | 4.8 | 2026-08-25 |
| ! | L-208 | CRITICAL-gate tier audit + self-report -> visible-evidence pattern extension | OPEN | 2.2 | 2026-08-18 |
|  | L-137 | Heliocentric -> solar barycentric coordinates -- decided against | PARKED | 1.0 | 2026-08-25 |
| ! | L-053 | AU-convention sweep (section E): keep open, revisit | OPEN | 0.8 | 2026-06-07 |
| ! | L-056 | Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes (MAPS per-frame wiring -> L-066) | OPEN | 0.5 | 2026-06-23 |

### H. Gallery / Studio Track
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-167 | Artifact-1 field notes -- orrery-coding-conventions still missing three entries | OPEN | 3.8 | 2026-07-29 |
| ! | L-107 | Gallery builder copy-with-provenance sync register | OPEN | 3.6 | 2026-07-09 |
| ! | L-073 | Gallery export-emits-JSON -- fold the manual json_converter run into Export | OPEN | 1.6 | 2026-06-26 |
| ! | L-058 | Open Studio items (May-5 handoff, checked @2f40d9d) | OPEN | 1.5 | 2026-06-08 |
| ! | L-104 | Gallery Studio preset generator | OPEN | 1.0 | 2026-07-13 |
| ! | L-132 | Studio landscape preset: links icon covers fly-to buttons | OPEN | 1.0 | 2026-07-17 |
| ! | L-074 | Cull unused raw *_teaser.json in the gallery dir | OPEN | 0.9 | 2026-06-26 |

### O.Asteroids -- candidate asteroid objects
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-139 | Pallas (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |
| ! | L-140 | Hygiea (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |
| ! | L-141 | Interamnia (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |
| ! | L-142 | Davida (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |
| ! | L-143 | Sylvia (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |
| ! | L-144 | Eunomia (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |
| ! | L-145 | Euphrosyne (candidate asteroid) | OPEN | 3.0 | 2026-07-17 |

### O.Exoplanets -- candidate exoplanet systems
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-146 | HR 8799 (candidate exoplanet system) | OPEN | 3.0 | 2026-07-17 |

### W.Prep -- Web Publication prep (before Phase 0)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-086 | Attribution / credits page | PROPOSED | 2.8 | 2026-07-03 |

### W.Active -- Web Publication active phase
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-160 | test_constants_provenance.py -- retire once fully absorbed, not before | OPEN | 8.1 | 2026-07-27 |
| ! | L-172 | Phase 0 record-hygiene batch (provenance cluster prep) | OPEN | 5.7 | 2026-07-29 |
| ! | L-158 | Derived-constant vulnerability inheritance rule (revised from a proposed rung, 2026-07-27) | OPEN | 5.6 | 2026-08-25 |
| ! | L-156 | Provenance scanner scoring model fix -- criticality (category-based) + vulnerability recalibration + comprehensive sweep | OPEN | 5.3 | 2026-08-02 |
| ! | L-155 | Cross-repo constants/geometry pinning checks -- built INTO provenance_scanner.py, not a standalone script | PENDING-GATE | 4.5 | 2026-07-27 |
| ! | L-119 | event_link hardcoded None in the builder (F2, gates artifact 7) | OPEN | 3.6 | 2026-07-15 |
| ! | L-168 | propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, source fix still open) | OPEN | 3.6 | 2026-07-28 |
| ! | L-175 | Newly-visible uncited temperature claims (1d piece 3) | OPEN | 3.6 | 2026-07-31 |
| ! | L-161 | Gemini sweep -- clear the display-string Tier-2 backlog | OPEN | 3.1 | 2026-07-27 |
| ! | L-157 | Gemini cross-check of shell config ring/belt/atmosphere geometry values | OPEN | 2.5 | 2026-07-27 |
| ! | L-166 | F1b: per-object trust enforcement + soft-edge trust UX (resolver/client consumption of served trust blocks) | OPEN | 2.4 | 2026-07-28 |
| ! | L-121 | Slim plotly wheel not deployed anywhere (F4, ships-nothing gate) | OPEN | 2.2 | 2026-07-15 |
| ! | L-150 | Multi-orbit trust model for near-equal-mass binaries (Pluto/Charon and future onboards) | OPEN | 2.2 | 2026-07-20 |
| ! | L-173 | shell_configs.py -- 8 body blocks missing... source citations entirely (found during 1c predesign measurement) | OPEN | 2.1 | 2026-07-30 |
| ! | L-122 | Stray data/solar-system.prev_old/ committed to the repo (F6, non-blocking) | OPEN | 1.9 | 2026-07-15 |
| ! | L-123 | Object info card -- serve info_dictionary.py as JSON, click-to-open (rides with F1) | OPEN | 1.8 | 2026-07-15 |
| ! | L-080 | Characterization harness (scene equivalence gate) | OPEN | 1.6 | 2026-07-14 |
| ! | L-079 | Shared assembler architecture (keystone -- redefined) | OPEN | 1.5 | 2026-07-07 |
|  | L-089 | Scene-spec shared skeleton + solar system vocabulary (Phase 1) | PROPOSED | 1.5 | 2026-07-03 |
| ! | L-159 | Disclosed-approximation check (Envelope of the Unknowable, scanner-level) | OPEN | 1.2 | 2026-07-27 |
| ! | L-111 | Gallery builder Pass 5 -- operability + deferred hardening | OPEN | 1.0 | 2026-07-27 |
|  | L-090 | Star cache inventory + wire format decision | PROPOSED | 0.5 | 2026-07-03 |
| ! | L-165 | Site continuity if there is no active administrator (succession / legacy planning) | OPEN | -- | 2026-07-27 |

### W.Deferred -- Web Publication deferred (captured)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
| ! | L-126 | Close-approach/encounter anchor mechanism -- general principle (NEOs, comets, spacecraft), not Apophis-specific | OPEN | 1.7 | 2026-07-17 |
|  | L-091 | Option E: unified front end | DEFERRED | 1.0 | 2026-07-03 |
|  | L-092 | Embeddable scenes for educators | DEFERRED | 1.0 | 2026-07-03 |
|  | L-093 | Educational guided explorations (specs as curriculum) | DEFERRED | 1.0 | 2026-07-03 |
|  | L-094 | Community cache as commons | DEFERRED | 1.0 | 2026-07-03 |
|  | L-095 | PWA / offline capability for classrooms | DEFERRED | 1.0 | 2026-07-03 |
|  | L-096 | Web orrery aesthetic / feel design conversation | DEFERRED | 1.0 | 2026-07-03 |
| ! | L-101 | Osculating-history fan (perturbed-moon precession view) | OPEN | 1.0 | 2026-07-08 |
| ! | L-102 | Spacecraft trace thinning (arc-minute decimation) | OPEN | 1.0 | 2026-07-11 |
| ! | L-103 | Hyperbolic conic -- browser branch (interactive.html) | OPEN | 1.0 | 2026-07-08 |

### C. Reconciled -- Done (closed; for the record)
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-117 | Offline suite red at HEAD: Encke id drift (2P -> 90000091) not mirrored in the mock | DONE | 34.2 | 2026-07-12 |
|  | L-114 | objects_config.json stranded by the atomic swap; also blocks crash-recovery (gallery builder) | DONE | 16.2 | 2026-07-27 |
|  | L-250 | The Braid added to Part 3 as a general principle | DONE | 15.2 | 2026-08-25 |
|  | L-182 | Mars Hill sphere -- cross-check correction lost across the config pipeline | DONE | 12.0 | 2026-08-05 |
|  | L-222 | The constants change report fails on every currency stamp | DONE | 11.4 | 2026-08-20 |
|  | L-221 | The master plan is the roadmap, and it outranks RICE | DONE | 10.8 | 2026-08-22 |
|  | L-198 | Claim vocabulary: the units the scanner could not see | DONE | 10.2 | 2026-08-17 |
|  | L-217 | The Part A / Part B dispatch split is a check that cannot fail | DONE | 8.1 | 2026-08-19 |
|  | L-207 | The citation prompt -- the checker asks the fuzzy question | DONE | 7.6 | 2026-08-18 |
|  | L-220 | A patch updates the body but not the anchor, date or description | DONE | 7.6 | 2026-08-20 |
|  | L-204 | The worksheet reference may be JSON | DONE | 5.7 | 2026-08-18 |
|  | L-196 | Citation continuations: mark, join, refuse | DONE | 5.4 | 2026-08-17 |
|  | L-197 | Maintenance runner output: say what passed | DONE | 5.4 | 2026-08-17 |
|  | L-201 | Request selection -- ask the builder for fewer rows | DONE | 5.4 | 2026-08-18 |
|  | L-205 | The runner's verdict lines carry evidence | DONE | 5.4 | 2026-08-18 |
|  | L-212 | maintenance_run names every file the run wrote | DONE | 5.4 | 2026-08-19 |
|  | L-003 | Protocol amendment candidates (for v3.29) | DONE | 5.4 | 2026-06-22 |
|  | L-062 | README refresh -- fold in handoff + ledger developments | DONE | 5.1 | 2026-07-28 |
|  | L-153 | Restore "Who Tony Is" framing into resident protocol (protocol) | DONE | 5.1 | 2026-07-21 |
|  | L-200 | The `# Resolved:` leg -- record a verdict that landed | DONE | 5.1 | 2026-08-18 |
|  | L-203 | The visibility convention -- give it a home in the skill | DONE | 5.1 | 2026-08-18 |
|  | L-189 | Provenance scanner: run history and run-to-run delta | DONE | 4.8 | 2026-08-11 |
|  | L-065 | European heat wave heat map (Earth System track) | DONE | 4.8 | 2026-06-25 |
|  | L-064 | Provenance-scanner format sweep -- Earth System family | DONE | 4.5 | 2026-06-30 |
|  | L-075 | KMZ info-card "3+5" redesign -- compact header + tappable info balloon (Earth System engine) | DONE | 4.3 | 2026-06-30 |
|  | L-076 | Earth System shared module (earth_system_common) + 3+5 generalized to food | DONE | 4.3 | 2026-06-30 |
|  | L-214 | The request builder drops the comment lines that matter | DONE | 3.8 | 2026-08-21 |
|  | L-233 | Three dashboard buttons: one fixed, one added, one retired | DONE | 3.8 | 2026-08-24 |
|  | L-106 | Gallery-cache backup + gitignore discipline | DONE | 3.6 | 2026-07-12 |
|  | L-115 | Skills v1.1 batch: accuracy fixes + two seed blocks (Fable Mode 7) | DONE | 3.6 | 2026-07-12 |
|  | L-097 | skills_index.py -- Skill Manifest auto-generation (process/tooling) | DONE | 3.2 | 2026-07-04 |
|  | L-127 | module_atlas.py generates MODULE_INDEX.md too -- single source, eliminate divergence | DONE | 3.2 | 2026-07-28 |
|  | L-188 | Maintenance runner -- one command, the whole suite | DONE | 3.1 | 2026-08-12 |
|  | L-069 | Food Insecurity Phase-2 -- Phase-5 "hidden Catastrophe" reveal (Darfur/Kordofan) | DONE | 2.8 | 2026-06-24 |
|  | L-109 | Fable 5 adversarial review remediation (builder Pass 1+2) | DONE | 2.8 | 2026-07-10 |
|  | L-112 | Gallery builder Pass 5: two-reviewer Pass-2 remediation | DONE | 2.8 | 2026-07-10 |
|  | L-110 | GPT competitive cross-check remediation (builder Pass 4) | DONE | 2.7 | 2026-07-10 |
|  | L-116 | New skill: gallery-cache-builder (Move 2 of the skills update) | DONE | 2.5 | 2026-07-12 |
|  | L-026 (#9) | palomas_orrery_helpers.py CRLF -> LF | DONE | 2.2 | 2026-07-15 |
|  | L-202 | JSON worksheet format, with markdown as fallback | DONE | 2.2 | 2026-08-18 |
|  | L-213 | Orbit cache backup fires on IMPORT, not on cache write | DONE | 2.2 | 2026-08-19 |
|  | L-063 | Orrery GUI Note text update | DONE | 2.0 | 2026-07-17 |
|  | L-072 | Gallery Studio WYSIWYG preview -- render through the real index.html viewer | DONE | 2.0 | 2026-06-26 |
|  | L-169 | Gallery/Studio track -- repo structure reference | DONE | 1.9 | 2026-07-28 |
|  | L-108 | Master plan v10 -> v11: Phase 1b fetch-fresh pivot reconciliation | DONE | 1.8 | 2026-07-12 |
|  | L-178 | Earth shadow constants -- EARTH_RADIUS_KM duplicate + mean vs equatorial mixing | DONE | 1.8 | 2026-08-05 |
|  | L-179 | Solar gravitational influence -- 150,000 vs 126,000 AU mismatch | DONE | 1.6 | 2026-08-07 |
|  | L-002 | Protocol -> Skills refactor (process/tooling) | DONE | 1.5 | 2026-07-04 |
|  | L-048 (#21/51) | Animation track 21/51 -- core complete pending the v4 gate | DONE | 1.5 | 2026-06-23 |
|  | L-147 | Embed dashboard launcher in orrery GUI third column | DONE | 1.5 | 2026-07-17 |
|  | L-180 | Solar chromosphere -- three inconsistent extents in one shell | DONE | 1.3 | 2026-08-07 |
|  | L-028 | ASCII em-dash violation, comet_visualization_shells.py L257/505/519 | DONE | 1.0 | 2026-08-19 |
|  | L-047 (#N10) | Note-composition structural refactor (behind N6) | DONE | 1.0 | 2026-06-23 |
|  | L-050 (#N9) | white -> red orbit-marker switch (osculating marker intentionally stays white) | DONE | 1.0 | 2026-06-23 |
|  | L-100 | Gallery feature-render surface: shells gallery-side vs interactive-side (OPEN QUESTION) | DONE | 1.0 | 2026-08-25 |
|  | L-134 | Dashboard developer-tools audit | DONE | 1.0 | 2026-07-17 |
|  | L-138 | Candidate objects & presets for the Objects menu (running list) -- superseded | DONE | 1.0 | 2026-07-17 |
|  | L-020 (#26) | CUSTOM_SHELLS tooltip verification | DONE | 0.9 | 2026-06-22 |
|  | L-163 | Module role/domain classification redesign (ROLE_MAP + MODULE_DOMAIN_MAP) | DONE | 0.8 | 2026-07-26 |
|  | L-049 (#N8) | Comet info-marker superposition cluster | DONE | 0.5 | 2026-06-23 |
|  | L-004 | Apply C2 fix pass + run ANIMATION_TEST_PROTOCOL_v4_1, push | DONE | -- | 2026-06-17 |
|  | L-005 | Commit protocol v3.28 (or v3.29) to repo root | DONE | -- | 2026-06-17 |
|  | L-006 | Mercury +0.2 R_M northward dipole offset | DONE | -- | 2026-06-20 |
|  | L-007 | Bow-shock hover disclosure remainder | DONE | -- | 2026-06-11 |
|  | L-009 | Dipole cluster: envelope tie / offset direction / remaining cones / half_len_frac | DONE | -- | 2026-06-20 |
|  | L-010 | Keplerian epoch parse fails on 'osc.' suffix | DONE | -- | 2026-06-12 |
|  | L-011 | Pass-C2 v4 blockers (3) + B3-bonus barycenter Sun bug | DONE | -- | 2026-06-11 |
|  | L-018 (#8) | Dead create_sun_direction_indicator imports (verify remainder) | DONE | -- | 2026-06-18 |
|  | L-019 (#13) | Neptune ring info-marker rotation (verify + close) | DONE | -- | 2026-06-18 |
|  | L-021 (#28) | Neptune superimposed info markers (verify + close) | DONE | -- | 2026-06-18 |
|  | L-022 (#40) | Asteroid belt hover -> single info marker | DONE | -- | 2026-06-18 |
|  | L-023 (#N2) | Saturn/Uranus ring marker placement | DONE | -- | 2026-06-18 |
|  | L-024 (#N4) | Planet 9 sphere n=50 -> 20/25 | DONE | -- | 2026-06-18 |
|  | L-029 | v25 D3 dead-code annotations + small-body analytical tail | DONE | -- | 2026-06-18 |
|  | L-036 | O11 greyed-legend display-name verdict: NO item needed | DONE | -- | 2026-06-11 |
|  | L-041 | Item 19.3 axis-control round trip (P1/P2/Phase A/Phase B + toggle follow-on) | DONE | -- | 2026-06-16 |
|  | L-054 | Gate 5(b): full resolution ships, rounded -- render-confirmed | DONE | -- | 2026-06-13 |
|  | L-055 | O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium particle count) | DONE | -- | 2026-06-17 |
|  | L-057 | Animation auto-scale-vs-shells + Phase 3 tier decision -- CLOSED | DONE | -- | 2026-06-11 |
|  | L-223 | A paste into the ledger is an unverified transfer | DONE | -- | 2026-08-21 |

### W.Done -- Web Publication track, closed items
| Gap | L# | Item | Disposition | Score | Updated |
|:---:|----|------|-------------|:-----:|---------|
|  | L-118 | feature_configs.json served empty every build (F1, gates artifact 2) | DONE | 8.1 | 2026-07-21 |
|  | L-162 | CENTER_BODY_RADII full de-duplication -- dedicated Sonnet session | DONE | 8.1 | 2026-07-29 |
|  | L-120 | Halley configured but not yet in the served index (F3, gates artifact 4) | DONE | 7.6 | 2026-07-27 |
|  | L-170 | Tier-1 exit-code flip -- capture so it doesn't float | DONE | 7.2 | 2026-07-29 |
|  | L-085 | LICENSE to repo root | DONE | 4.0 | 2026-07-03 |
|  | L-088 | Gallery integration test (Phase 0) | DONE | 4.0 | 2026-07-06 |
|  | L-099 | Solar System Explorer interactive exhibit | DONE | 3.2 | 2026-07-06 |
|  | L-174 | Citation level mismatch -- citations pitched one block too far out | DONE | 2.7 | 2026-07-30 |
|  | L-154 | Gallery feature-rendering JS layer (shells, rings, radiation belts -- Artifact 2 prerequisite) | DONE | 2.1 | 2026-08-24 |
|  | L-087 | palomas_orrery_helpers.py computation/GUI split | DONE | 2.0 | 2026-07-15 |
|  | L-152 | ledger-and-session-records skill bumped to 1.2 -- retroactive ledger entry | DONE | 1.9 | 2026-07-20 |
|  | L-148 | Staging folder names carry no object identifier -- hard to locate manually (gallery-cache-builder) | DONE | 1.8 | 2026-07-20 |
|  | L-098 | Data serving pipeline (Phase 1b) | DONE | 1.5 | 2026-07-12 |
|  | L-149 | Global served_window trust participation should key off canonical_frame, not category (gallery-cache-builder) | DONE | 1.2 | 2026-07-21 |
|  | L-151 | Create gallery-assembler skill -- technical home for the new-mechanism assembler | DONE | -- | 2026-07-27 |

<!-- INDEX:END -->

---

## DETAIL / RECORD

## A. ACTIVE SEPARATE TRACKS (not orrery-refactor backlog; cross-referenced)

#### [L-001] Food Insecurity (Earth System track)
<!-- L:001 status:OPEN upd:2026-06-30 section:A flag: rice:3/3/95/2 -->
- **Phase-1 build COMPLETE, render-confirmed (Mode-5, ge_sudan.jpg, built on
  03630ae).** Module: food_insecurity_generator.py -- new dedicated vector/
  categorical generator (NOT a bend of run_scenario); 189 area polygons, full
  phase1-5 balloon breakdown, transcribed national totals (never summed),
  legend + national ScreenOverlay cards, framing folder, optional Plotly teaser.
  KMZ byte-verified: Beliel balloon shows Phase 5 = 26,411 under mapped P4 (the
  hidden Catastrophe made visible). Provenance scanner Tier-1 = 0 (but see L-064
  -- that clean is currently a false clean for this module).
- **Discrepancy resolved (file wins):** phase5_population>0 is in 10 areas, not
  23 as the manifest prose said; all 10 are mapped P4. Built to the file.
- **Provenance flags carried forward:** phase ramp hex SAMPLED from report p.7
  legend (not IPC published hex); report has NO formal recommended-citation line
  (CITATION assembled from title page); per-area confidence_level/hfa_value shown
  as RAW values (no word-legend in report to map them). All open to retune.
- **Module name CONFIRMED (no longer a proposal): food_insecurity_generator.py**
  -- standalone-runnable via __main__ -> run().
- **KMZ naming convention (Earth System family):**
  data/<SCENARIO_ID>_blockbuster.kmz. Food layer SCENARIO_ID =
  "food_insecurity_sdn" (Sudan) -> data/food_insecurity_sdn_blockbuster.kmz;
  mirrors the heat scenarios (e.g. data/europe_2026_blockbuster.kmz). Generator
  also emits the two ScreenOverlay PNGs and <ID>_teaser.html. Those overlay names
  are now BUILD-STAMPED -- legend_<ID>_<YYYY-MM-DD-HH-MM>.png and
  intel_<ID>_<stamp>.png (one stamp per build, shared by both cards; prior copies
  cleaned) -- so a regenerated KMZ never reuses a filename Google Earth has
  cached; the KMZ filename itself is unchanged so --preload still matches. The
  food_insecurity_<region> prefix is LOAD-BEARING: the controller's
  --preload food_insecurity globs data/food_insecurity_*_blockbuster.kmz (single
  source; the GUI launcher delegates to it -- see L-076), so future regional
  layers (L-070: SS/TD/CF/ET) must follow food_insecurity_<code>_blockbuster.kmz
  to be picked up.
- **GUI registration (DONE).** Earth System Viewer
  (earth_system_visualization_gui.py) at b7650bb -- "Google Earth Food
  Insecurity Layers" section + launcher button -> launch_food_insecurity_layers(),
  which now DELEGATES to the controller (--preload food_insecurity) instead of
  globbing itself (single-source; see L-076); existing heat-wave launcher renamed
  KML -> KMZ. Dashboard (palomas_orrery_dashboard.py): Food Insecurity Generator +
  Controller buttons DONE (Mode-5 confirmed, 1b74bf1). Viewer scroll fix
  (97c21e1): the content area is wrapped in a scrollable canvas so the growing
  food/heat button sections stay reachable at any window size / when maximized
  (the food section had fallen below the fold).
- **KMZ "3+5" parity + tappable i-pin (DONE; c81bb3b; Mode-5 iOS-confirmed,
  IMG_1153/1154).** The food KMZ adopted the heat "3+5" card (L-075) via the
  shared module (L-076): the fixed full-text intel ScreenOverlay shrank to a
  compact header (title + period + "tap the (i) pin"), and the four invisible
  framing placemarks became ONE visible tappable "i" pin whose CDATA balloon
  carries the full briefing (National summary -> hidden Catastrophe -> map-color
  note -> Key drivers -> Middle East line -> "does not assert" -> Source/citation).
  All by reference to the existing transcribed constants -- no synthesis, no new
  numeric literals, provenance unaffected. On iOS the <h4> sections render fine;
  the GE "content controlled by the author" banner is app chrome (full-screen web
  sheet), harmless. run() gained a scenario_id parameter; food __main__ now opens
  the shared picker instead of auto-running Sudan.
- **Stale-card episode (resolved -- deploy path, not code).** The old card
  persisting on the phone through layer/file deletion was a missed
  data/ -> assets/ copy of the regenerated KMZ, NOT a Google Earth cache fault.
  Lesson: confirm the DEPLOY path before theorizing a cache. The build-stamped
  overlay names (above) were kept as cheap cache-bust insurance.
- **Still open under this track:** Deferred sub-layers split out: Phase-5 reveal
  -> L-069; 39 IPC call-out points (HFA-bag/IDP symbols) and the Jun-Sep /
  Oct-Jan projections remain deferred per original scope.
**Ref:** MANIFEST_food_insecurity_sudan_v2.md; HANDOFF_food_insecurity_build_v2.md
(built on 03630ae); cross-ref L-064, L-069.

#### [L-060] ENSO Standalone Chart (Earth System track)
<!-- L:060 status:OPEN upd:2026-06-18 section:A flag: rice:3/3/75/2.5 -->
- **ENSO standalone gallery chart (design locked, build next session).** Earth
  System track, not the orrery refactor. Single-unit (deg C) chart leading with
  RONI so El Nino / La Nina state reads honestly in a warming climate; ONI as a
  thin overlaid line (keeps the RONI-ONI divergence visible, anchors the
  forecast). RONI drawn as a FILLED-to-zero seesaw -- red El Nino above, blue
  La Nina below (recognizable, gallery-striking; the Economist / Climate Brink
  use the same idiom and also lead with RONI -- external validation of the
  RONI-first call). 2026 forecast as a CALIBRATED envelope: plume mean +
  skill-scaled Gaussian (official IRI product; widens at the spring barrier;
  upper edge is where the "strongest ever" tail lives, shown as possibility not
  promise) -- NOT a single median line (the Economist chart's grey median spike
  is exactly what we reject). Plume is ONI / Nino-3.4 basis, hung off the ONI
  line, basis STATED IN HOVER (the Economist chart leaves forecast basis
  unstated -- our fix). Fallback if IRI skill-calibration params are not cleanly
  fetchable: labeled model-spread band ("model spread, not a calibrated
  probability"). 2026 event shown NOW, PROVISIONAL with preliminary/developing
  flagging (Western Heatwave convention) -- already front-page news. Phase
  shading COMPUTED from RONI (+/-0.5, 5 overlapping seasons); strength from RONI
  magnitude, never a recalled label. ENSO<->energy-imbalance told as MECHANISM:
  a PLOTLY-DRAWN charge/discharge schematic (no time axis) + cited physics in
  the "i" card -- NOT a data overlay, NOT a computed covariance. EEI stays drawn
  once on the energy-imbalance chart (no parallel pipeline); cards cross-link.
  No traces beyond RONI + ONI + thresholds + phases + today + plume (Tony: let
  it land). Data: RONI.ascii.txt CONFIRMED fetchable; ONI URL + IRI plume parse
  TBV at build. Mobile + desktop variants from the start. Design base SHA 799d7da.
  Phase 2 (DEFERRED, coupled, do NOT lose): targeted Mode-1 pass on
  energy_imbalance.py -- narrative correction (El Nino imbalance dip led by
  OUTGOING LONGWAVE, NOT primarily "reflects more sunlight"; fold in RONI
  rationale) + add 2026 band provisional-with-flagging. Split to own L-handle if
  it risks leaking when L-060 closes.
**Gap:** build next session. One genuine open call left (build, not design): confirm ONI file URL + IRI plume parse / skill-calibration params at HEAD before hardcoding (cached-CSV fallback if scrape unstable; model-spread band fallback if calibration params unavailable). Provenance-scan new module (Tier-1=0) before push. Resolved: plume=calibrated Gaussian envelope; schematic=Plotly; 2026 band=provisional-now; no extra traces.
**Ref:** ENSO_chart_spec.md v2 (design spec, this session); cross-ref L-001 (Food Insecurity, same Earth System track); energy_imbalance.py (Phase 2 target).

#### [L-070] Food Insecurity -- regional multi-country assembly (Sudan crisis shed)
<!-- L:070 status:OPEN upd:2026-06-24 section:A flag: rice:2/3/45/3 -->
- **Extend the food-insecurity view across the Sudan-war refugee shed:** Sudan
  (have, SD) + South Sudan (SS) + Chad (TD) + CAR (CF) + Ethiopia (ET). Each is a
  SEPARATE IPC analysis / separate manual Mapping Tool fetch (bot-block wall) with
  its own analysis period -- combined view must LABEL per-country periods, never
  blend (cross-border form of "don't compare across periods").
- **Generator already country-agnostic** (reads country/area/phase from the
  GeoJSON); regional = ingest a file set + per-country period labels + per-country
  attribution + multi-country LookAt. Encoding identical per country (choropleth +
  L-069 P5 dots).
**Gap:** DATA-ACQUISITION GATED. Confirm current IPC availability + period per
neighbor at fetch time (Tony, manual). Scope: which neighbors in v1.
**Ref:** L-001 (parent), L-069 (P5 dots reused per country); food_insecurity_generator.py.

#### [L-071] 2026 European heat dome -- track to resolution (dated scenario series)
<!-- L:071 status:OPEN upd:2026-06-25 section:A flag: rice:3/3/70/2.5 -->
- **Follow the ongoing 2026 European heat dome across its lifetime as a dated
  scenario series** -- the Western Heat Dome (Mar 14/17/18) pattern: one new dated
  europe_* scenario per captured day, NOT one scenario auto-advancing its date.
  Same chassis as europe_2026 (wet-bulb spine + C-only air-temp pins,
  fetch_era5_heatwave / Open-Meteo archive). europe_2026 (21 Jun) is entry #1,
  built and closed under L-065.
- **Next:** a new dated scenario for the 27-28 Jun peak, once Open-Meteo's archive
  reaches those dates (a few days' lag). New date = fresh fetch, no cache collision.
- **Carried forward from L-065 (closed):** (a) WWA attribution watch -- update the
  line across the series if a study publishes; (b) Sentinel-3 LST surface snapshot --
  optional separate artifact.
- **Close when:** the dome resolves and the series is complete.
**Ref:** L-065 (build + chassis, closed); scenarios_heatwaves.py; Western
dated-series precedent (scenarios_western_heatwave_march_2026.py).

#### [L-077] 2026 US Midwest/Central heat dome -- migrating-centroid ongoing scenario
<!-- L:077 status:OPEN upd:2026-06-30 section:A flag: rice:3/3/60/2.5 -->
- New L-item (not a sibling of L-071) -- the migrating centroid plus the
  advancing reanalysis/forecast seam is its own design object, not another
  dated snapshot. Track: Gulf Coast bullseye -> St. Louis (~Jul 1) ->
  Chicago (~Jul 4) -> forecast retreat into the High Plains.
- ERA5T lag confirmed ~5 days behind real-time, D-5 typically by 12 UTC
  (Copernicus C3S / ECMWF CDS docs, retrieved 2026-06-30) -- so today there
  is no observed wet-bulb field yet for the June 27-Jul 1 peak.
- Design: ongoing scenario per the L-071 pattern (one dated scenario per
  captured day, chassis shared with europe_2026/scenarios_heatwaves.py),
  but with the forward/migrating segment shown as a forecast ENVELOPE
  (Show-the-Envelope convention) and the already-happened segment as solid
  reanalysis once ERA5T catches up -- the advancing seam is the honest,
  teachable object.
- El Nino backdrop noted as context only (L-060) -- causal restraint, no
  drawn connection.
**Gap:** scaffold the dated-scenario module once ERA5T coverage reaches the
event window (NOAA WPC June 27-29 peak + ~5-day lag -> earliest observed
coverage ~early July). Forecast-vs-reanalysis visual treatment is the open
design detail at build time.
**Ref:** NOAA WPC; Copernicus C3S/ECMWF CDS ERA5T docs (retrieved 2026-06-30);
design conversation this session; cross-ref L-071 (sibling pattern, not
parent), L-060 (El Nino context, no causal claim).

#### [L-078] Provenance scanner: systematic coverage via module_atlas role classification
<!-- L:078 status:OPEN upd:2026-07-16 section:A flag: rice:2/2/70/3 -->
- **Root cause (why files get missed in the first place).** provenance_scanner.py
  gates display-string scanning on a hand-maintained narrative_files allow-list;
  a new file is invisible until someone notices and adds its name. The scanner
  already solved this once, structurally, for one family -- is_shell_file =
  module_name.endswith('_visualization_shells') auto-includes by pattern, no
  list-editing required -- but that fix was never generalized.
- **module_atlas.py already does most of what's needed and is more complete than
  the scanner's own list.** classify_role() tags every module (data / scenario /
  rendering / rendering-shells / cache / computation / gui / pipeline / utility /
  devtool / legacy / other), with 'other' as an honest catch-all rather than a
  silent drop. Its 'data' role already includes 5 catalog/constants files NOT in
  narrative_files (exoplanet_coordinates, star_properties, stellar_data_patches,
  stellar_parameters, messier_catalog); its 'scenario' role already cleanly
  groups the heat/coral/western family the scanner has no equivalent for. The two
  tools have drifted apart from each other despite Tony running them together --
  nothing actually diffs their outputs. (Minor, telling: food_insecurity_generator
  -- the one file properly in narrative_files -- isn't in module_atlas's ROLE_MAP
  either, so it currently shows 'other' there. Both lists are hand-maintained;
  both have independently drifted.)
- **Design, two checks, both surfacing in PROVENANCE_AUDIT.md (Tony's call --
  that's the output actually reviewed every run, not module_atlas's):**
  1. MISSING CATEGORIES (file-level). Replace/extend narrative_files with
     role-driven inclusion: any module classified data / scenario / rendering /
     rendering-shells gets scanned automatically via module_atlas.classify_role.
     Any module landing in 'other' that contains claim-shaped string content
     gets a new "COVERAGE GAPS -- needs role classification" section in the
     audit output. Mechanical, low risk, the more tractable of the two builds.
  2. MISSING FIELDS (vocabulary-level). Found the exact hook point:
     _extract_string_units (provenance_scanner.py ~L711-721) walks every AST
     string Constant, runs extract_numeric_claims(), and on zero claims just
     `continue`s -- the string vanishes with no trace. Fix: a second, looser
     pattern at that exact branch -- number directly followed by 1-4 letters/%/$
     not matched by NUMERIC_CLAIM_RE -- logged as a near-miss instead of dropped,
     in a new "VOCABULARY GAPS -- unrecognized unit candidates" section. Runs
     only on already-covered files (check 1 handles files missing entirely), so
     naturally narrower scope than a whole-file sweep.
  3. The F/C bare-degree gap itself (KNOWN now, not a near-miss) lands directly
     in NUMERIC_CLAIM_RE as its own fix, separate from the near-miss MECHANISM
     being built to catch the next unknown gap.
- **Noise risk on the near-miss check (the harder of the two, flagged not
  solved).** A loose number+token pattern will catch ordinals ("2nd"), version
  strings ("v3.29"), multipliers ("3x") as false near-misses unless explicitly
  excluded. Needs scratch-testing against the real corpus and an eyeballed
  false-positive rate before going live -- not a guess-and-ship.
- **Architecture: scanner imports classify_role from module_atlas.py directly**
  (Tony: no strong preference, deferred to whatever reliably catches gaps every
  run). One-directional, no third shared module. Default unless revisited.
- **Effort framing (Tony's explicit precedent, 2026-06-30): the original scanner
  took ~10 sessions with multiple Gemini cross-checks to harden.** Not treating
  this as a quick patch. Check 1 (categories) is the tractable mechanical build.
  Check 2 (vocabulary near-miss) is the one likely to need the same kind of
  cross-check / corpus-tuning the original scanner got.
- **STATUS (July 4, 2026): step (1) is LIVE -- role-driven inclusion landed.**
  The scanner at HEAD imports classify_role from module_atlas and uses
  NARRATIVE_ROLES = {data, scenario, rendering, rendering/shells, computation}
  additively over the legacy narrative_files allow-list (line 635-639). The
  COVERAGE GAPS section is working (4 modules flagged: shell_configs 91,
  food_insecurity_generator 1, orrery_rendering 1, smoke_rotation_axis 1).
- **First full run under new coverage: Tier-1 = 104** (all score 16: V=4
  recalled x C=4 public-facing display strings) across 26 modules. Largest
  contributors: idealized_orbits.py (23 findings), paleoclimate_wet_bulb_full
  (11), paleoclimate_human_origins_full (9), paleoclimate_visualization_full (7),
  planet_visualization_utilities (7), sgr_a_grand_tour (6),
  scenarios_western_heatwave_march_2026 (4), sgr_a_visualization_core (4),
  exoplanet_coordinates (4). These are real, previously-invisible uncited
  display strings -- the predicted "heavy first run" from the design. The
  previous Tier-1=0 was true only for the smaller file set the legacy
  allow-list covered.
- **Phase 1b triage (July 7, 2026).** Cross-referenced the 104 Tier-1 findings
  against the 10 source files in the Phase 1b export script's provenance table
  (PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.4). **Zero overlap.** All 10 source
  files (osculating_cache_manager, orbit_data_manager, orbital_elements,
  celestial_objects, constants_new, shell_configs, *_visualization_shells,
  close_approach_data, spacecraft_encounters) are clean of Tier-1 findings. The
  104 findings cluster in display/visualization modules the export script never
  touches: paleoclimate (5 modules), sgr_a (3), exoplanets (2), coordinate
  guides, apsidal markers, idealized orbits, visualization utils. Phase 1b
  does not propagate provenance gaps to served data. The one flag is
  shell_configs.py (91 claim-shaped strings in COVERAGE GAPS, not yet scanned) --
  but that feeds feature configs (Phase 2), not the Phase 1b export script.
  **This workstream is parallel to Phase 1b, not a blocker.**
- **Carried forward from L-064 (closed, superseding this item):** F/C vocabulary
  gap; energy_imbalance.py (corroborated independently by L-060's own deferred
  Phase-2 note -- ~47 candidate hits, zero citation markers found in a manual
  proxy check); paleoclimate_wet_bulb_full / paleoclimate_human_origins_full
  (manual proxy shows heavy citation density -- likely another false-clean, same
  shape as scenarios_heatwaves.py) vs paleoclimate_visualization_full (high claim
  volume, thin citation density -- likely the riskier one, same shape as
  scenarios_western_heatwave_march_2026.py); star_notes.py:1257 (still open,
  pre-existing, reconcile in the same pass).
- **RICE note (July 7, 2026):** Reach and Impact lowered from 3/3 to 2/2.
  Findings are in display strings of visualization modules, not in data pipeline
  or propagating constants. No served data affected. Still real gaps that need
  citing, but not load-bearing for any current build. Suitable for Fable 5
  bulk triage (access through July 12, 2026).
- **Report tooling groundwork (July 16, 2026), ahead of the (a) triage lift --
  Claude and Tony framed this explicitly as orchestration groundwork for a
  separate cleanup session, not the triage itself.** Two report-formatting
  increments landed at HEAD (design does not touch scoring): (1) a "Findings
  by File" summary table -- tier 1-4 counts per file, sorted worst-first,
  ahead of the existing per-tier detail; (2) a "Findings by File Type" domain
  breakdown via new MODULE_DOMAIN_MAP / classify_domain() -- six domains
  (orrery, earth_science, gallery, stars, utilities, dev_tools; the last two
  new, split out of the original four after Tony resolved four ambiguous file
  clusters: Sgr A*/Galactic Center -> orrery; cross-cutting reference-frame/
  utility files split three ways -- celestial_coordinates/coordinate_system_
  guide -> orrery, visualization_utils/_2d/_3d/_core -> stars,
  shared_utilities/formatting_utils/save_utils/report_manager/
  plot_data_exchange/plot_data_report_widget -> new utilities bucket;
  devtools/one-shot infra -> new dev_tools bucket; social_media_export.py ->
  gallery). Domain is report-only, independent of module_atlas's functional-
  role ROLE_MAP; unmapped files default to orrery and surface in a new Domain
  Coverage Gap note, mirroring the existing ROLE_MAP coverage-gap check.
  Gallery will normally read near-zero here -- the gallery ASSEMBLER pipeline
  lives entirely in the separate tonyquintanilla.github.io repo, out of this
  scanner's reach.
- **Self-referential scanning side effect, chased down and verified not a
  regression.** The scanner scans itself; the new MODULE_DOMAIN_MAP /
  DOMAIN_LABELS dicts added to provenance_scanner.py were picked up in its
  own audit entry (+2 low-tier findings, Tier 3/4, zero Tier-1 change) --
  confirmed by diffing before/after audits line-by-line rather than trusting
  the summary count. Now a provenance-discipline field note so a future
  total-findings delta after a scanner edit isn't mistaken for a new gap
  appearing elsewhere in the project.
- **provenance-discipline skill bumped to v1.1** (cut from palomas_orrery @
  be6376bb93a3f6fdfa2c0ff5b75a7398e60ea6ce, July 16, 2026): documents the
  Report Domain Classification mechanics above; promotes the Review-Repair
  Protocol (Claude-cannot-be-the-verifier three-role split: Claude preps a
  worksheet, Tony/Gemini research and verify, Claude mechanically transcribes
  confirmed citations) out of documentation/provenance_audit_handoff_v4.md
  into the durable skill layer; adds the self-referential-scanning field note
  above and a stale/multiple-copies-of-PROVENANCE_AUDIT.md field note from a
  self-caught near-miss this session (cd'd into documentation/ mid-session
  and nearly triaged against an April-dated archived copy instead of a live
  scan -- caught via pwd/git show before it reached a deliverable).
- **Live counts after this round (July 16, 2026): 120 files, 675 findings,
  Tier-1 = 104** [Tony-local run, exceptions file applied -- authoritative,
  per Scanner Mechanics the confirming re-run is Tony-side]. A sandbox
  verification run under different local exceptions state showed 673
  findings / Tier-1 = 102 -- same shape, small drift expected between
  environments; report STRUCTURE (by-file, by-file-type, domain sums
  reconciling against totals) was verified in the sandbox before push, then
  confirmed rendering correctly against Tony's real post-push numbers.
**Note (2026-07-29, verified live at HEAD):** Triage backlog is 145, not
104 (the July 16 figure) -- confirmed by a live scanner run against a
clean clone with the real exceptions file loaded. Every file besides
`shell_configs.py` matches the July 4/16 figures within +/-1; the entire
41-finding delta is `shell_configs.py` alone, newly in scanned scope from
L-163's role-widening.
**Correction (2026-07-29, same day, re-measured):** those 41 are NOT a real
citation gap -- see L-156 Gap item (6). `shell_configs.py` has a genuine
`# Source:` comment for every body block; the scanner's 60-line lookback
just doesn't reach it. Once L-156's inheritance fix lands, these 41 drop
out of Tier-1 (V3, not V1/V2 -- still worth a look, just not "uncited").
The genuinely uncited population -- the actual (a) triage target -- is the
paleoclimate family (32 across 5 files: `paleoclimate_wet_bulb_full.py`,
`paleoclimate_human_origins_full.py`, `paleoclimate_visualization_full.py`,
`paleoclimate_visualization.py`, `paleoclimate_dual_scale.py`) and the
sgr_a family (13 across 3: `sgr_a_grand_tour.py`,
`sgr_a_visualization_core.py`, `sgr_a_visualization_precession.py`), plus
`idealized_orbits.py`'s genuinely-distant remainder (24 -- real gap, not a
lookback artifact) and the rest of the July 4/16 baseline. All score
V4xC4=16 (uncited display strings), same object type as L-161's sweep, not
geometry -- so (a) still merges into L-161 rather than running separately;
only the starting file changes.
**(b) is DONE, closed as a side effect of L-163, and its old instruction is
now actively wrong.** The live audit has no role-coverage-gap section at
all (only the domain one) -- L-163 Phase 3's docstring tags classify
114/115 modules with `role_source == 'tag'`. "Add to ROLE_MAP or
narrative_files" does nothing since L-163 Phase 3: `ROLE_MAP` is a
regenerated mirror, overwritten by the next `module_atlas.py` run. One of
the four originally-named modules (`smoke_rotation_axis.py`) was also
deleted outright in L-163 Phase 1. The two files that DO still need a home
are domain-coverage-gap, not role -- see L-172.
**Note (2026-07-31):** L-078 sub-item (d) (bare-degree F/C values in NUMERIC_CLAIM_RE) is DONE, landed as part of L-156 Phase 1d piece 3. Pushed at 8bd7778. Surfaced 96 new findings -- tracked as L-175.
**Gap:** (a) merge into L-161's Gemini relay, one worksheet per file,
covering that file's uncited (this item) and re-read (L-161) claims
together -- start with the paleoclimate family (32 findings, never
worksheeted) and the sgr_a family (13, never worksheeted), NOT
`shell_configs.py` (that's L-156's Phase 1 fix, not a worksheet target)
and not L-161's originally proposed `celestial_objects.py` either. (b)
DONE -- see Note above, no further action. (c)
near-miss vocabulary detector -- stays open, separate, own session after
this cluster, corpus tuning not started. (d) F/C bare-degree fix -- folds
into L-156's Phase 1 build.
**Ref:** provenance_scanner.py (_extract_string_units ~L711-721, narrative_files
~L623, NARRATIVE_ROLES ~L635, classify_role import ~L216, coverage-gap report
~L1271-1283, MODULE_DOMAIN_MAP/classify_domain ~L245-421, Findings by File /
Findings by File Type report sections ~L1467-1546); module_atlas.py
(classify_role, ROLE_MAP); L-064 (closed predecessor); PROVENANCE_AUDIT.md
(July 16, 2026 run: 120 files, 675 findings, Tier-1 = 104); skills/
provenance-discipline/SKILL.md v1.1; documentation/provenance_audit_handoff_v4.md
(Review-Repair Protocol origin); documentation/worksheets/worksheet_earth_visualization.md
(worksheet template precedent for the (a) triage).

#### [L-105] merge_orbit_data source-side frame guard (desktop cache hardening)
<!-- L:105 status:OPEN upd:2026-07-08 section:A flag: rice:2/2/50/2 -->
- OPTIONAL. merge_orbit_data merges data_points by date with NO frame check --
  how heliocentric points entered a barycenter-keyed pair (pre-@9-override),
  producing the L-098 contamination. Add a magnitude/frame guard on cache write
  to prevent recurrence. Low priority (legacy cache is desktop-only now; the
  gallery no longer reads it) -- but it is the root-cause fix.

#### [L-129] Cometary structure constants -- periodic maintenance sweep
<!-- L:129 status:OPEN upd:2026-07-17 section:A flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/16/26, pre-ledger note).** Comet structural constants
  (tail composition, dust/gas ratios, etc.) are a standing maintenance
  item, not a one-time fix -- as observations of active comets accumulate,
  known structural data should be periodically re-checked. Recurring,
  low-urgency, character similar to L-078 (provenance scanner coverage).
**Gap:** no cadence or trigger defined yet -- decide how often (per
apparition? per session?) and which comets are in scope.
**Ref:** to_do_ideas.md (pre-ledger, 4/16/26); horizons-orbital-mechanics
skill (comet record pinning).

#### [L-176] Shell hover text: add illustrated dimensions (radius_fraction -> km)
<!-- L:176 status:OPEN upd:2026-08-04 section:A flag: rice:4/3/70/3 -->
- Fable audit surfaced that radius_fraction geometry constants are
  invisible to the user and verifiable only by manual computation. Add to
  each shell's hover text: "<shell name> illustrated between _ and _
  radii, a thickness of _ km". Gives the user full information and makes
  any stylization (e.g. Mercury crust drawn at 89 km vs physical 26 km)
  explicitly visible rather than silently present.
- Should derive from the radius_fraction at render time, not from a
  second typed literal -- single source of truth.
- Natural companion to the single-source-of-truth constant layer
  (L-181): once constants are defined, the illustrated-dimension text
  can reference them.
**Note (2026-08-05):** Scope boundary, so the item is not oversold later.
Illustrated dimensions catch CONSTANT-VS-TEXT drift -- the Batch 1 class,
where Mercury's rf 0.85 drew 2,074 km under text claiming 2,020. They do
NOT catch a value that is internally consistent but unsourced: Mars's Hill
sphere drew exactly the 324.5 R_Mars its text claimed, and both were wrong
(L-182). Drift is visible in the render; wrong-but-consistent needs the
provenance cross-check. The two mechanisms are complementary, not
substitutes.
**Gap:** Design the text format, decide whether to include the physical
value alongside the illustrated value for stylized shells. Build after
L-181 constant layer or in parallel.
**Ref:** FABLE_shell_consistency_audit_report.md findings #2-#12,
L-156 Phase 2.

#### [L-177] Mercury Hill sphere radius_fraction convention error (Opus 5 self-flag)
<!-- L:177 status:OPEN upd:2026-08-04 section:A flag: rice:4/4/50/2 -->
- Opus 5 flagged its own Batch 1 work: Mercury Hill sphere
  radius_fraction is 94.4 R_M (230,308 km), but the citation says
  "perihelion convention." Perihelion gives 71.85 R_M; semi-major gives
  90.45 R_M. 94.4 matches neither -- wrong-but-cited, the exact failure
  class the provenance discipline is designed to prevent.
- Fable couldn't catch it because Mercury's Hill text is qualitative
  (no number for the constant to contradict).
- Fix depends on which convention Tony picks. One-line change once
  decided.
**Gap:** Tony decision: perihelion (71.85) or semi-major (90.45)?
Perihelion is the project convention for Eris and Pluto.
**Ref:** ASBUILT_geometry_and_br_fix.md, Batch 1 worksheets.

#### [L-181] Complete the single-source-of-truth constant layer
<!-- L:181 status:OPEN upd:2026-08-25 section:A flag: rice:5/5/70/5 -->
- Fable audit established the structural problem: up to six independent
  storage locations for one physical value (radius_fraction, hover_text,
  dead tooltip, module _info, CUSTOM_SHELLS tooltip, legacy inline
  builder dict). The reference pattern (Saturn/Uranus/Neptune/Sun) links
  text copies but not geometry to text -- Saturn (fully migrated) carried
  the worst finding in the audit.
- Design required: define each value once as a named constant, derive
  radius_fraction and display text from it. The `<br>` canonical
  direction also belongs here: source text in `\n`, derive `<br>` at
  the Plotly boundary.
- 124 dead `tooltip` fields (83 sphere + 41 custom) are a
  delete-or-wire decision before migration.
- Natural companion to L-176 (illustrated dimensions).
- **REFRAMED 2026-08-06 (Tony's ruling).** This is not a NEW constant
  layer; it is completion of the existing one. `constants_new.py`
  already holds feature geometry (CHROMOSPHERE_RADII, INNER_CORONA_RADII,
  OUTER_CORONA_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
  TERMINATION_SHOCK_AU, HELIOPAUSE_RADII) and already handles nested
  dicts with per-entry citations (CENTER_BODY_RADII,
  KNOWN_ORBITAL_PERIODS). Solar shell geometry went into the store;
  planetary ring geometry stayed inline in the rendering modules. There
  is no principle behind which went where -- the split is historical.
- **COUNT CORRECTED 2026-08-07.** The "37 entries" figure was never
  sourced and does not match the code. Enumerated by AST walk over the
  four shell modules at `9b4f278`: **33 ring entries** -- Jupiter 4
  (Main, Halo, Amalthea Gossamer, Thebe Gossamer), Saturn 7, Uranus 11,
  Neptune 11. Jupiter is 4, not the 5 the August 7 handoff stated.
- **A SECOND SURFACE exists and was in neither count.** Radiation belts
  and plasma tori carry geometry as BARE LITERALS inside function
  bodies, not as dicts with `inner_radius_km`: Jupiter
  `io_torus_distance=5.9`, thickness 2, width 1, `belt_distances=
  [1.5, 3.0, 6.0]`, `belt_thickness=0.5`; Saturn
  `enceladus_torus_distance=3.95`, thickness 1, width 2,
  `belt_distances=[2.7, 3.5, 4.4, 5.6, 7.4, 9.0]`, thickness 0.5;
  Uranus `belt_distances=[2, 6]`, thickness 0.5; Neptune dict-keyed on
  `thickness`. About 22 physical values in FOUR different shapes, and
  ZERO carry a `# Source:` comment. These are inside Artifact 2, which
  the plan defines as "Jupiter/Saturn, rings + radiation belts."
- **Tony's ruling 2026-08-07 on their status:** the belt dimensions are
  NOT arbitrary. They are RANGES, and the modeling can use the ranges
  or interpolate within them -- the same treatment L-179 gave the solar
  gravitational influence. Where a value is genuinely a style choice
  (belt thickness for visibility, how many shells to draw), Tony
  decides and it is declared as such. An earlier framing of these as
  "drawing choices" was wrong and is withdrawn.
- **REGISTRY STRUCTURE IS A DESIGN TASK (Tony, 2026-08-07).** One
  `FEATURE_REGISTRY` has to hold rings (dict, inner/outer/thickness),
  belt sets (list of distances plus a scalar), and tori (three
  scalars). Tony: "we need a structure for this data. it will extend
  to other bodies." Design the shape BEFORE the migration, because the
  migration writes into whatever it defines.
- **Scope widened to three layers.** (1) The feature entries above move
  out of `jupiter_`/`saturn_`/`uranus_`/`neptune_visualization_shells.py`
  into `constants_new.py`. (2) Provenance migrates from `# Source:` comments
  to `source` DATA fields, one pass, bounded to the store (36 citations
  in constants_new.py plus what migrates in) -- required because a
  comment cannot be read at runtime and Tony wants hover text to quote
  its source for Mode 5 audit. The scanner's own docstring already lists
  this as deferred fix item 6: extend SOURCE_PATTERNS to recognize
  `'source': '...'`. (3) The exporter reads the store rather than four
  shell modules -- which is also what makes it POSSIBLE, since reading
  shell configs pulls Plotly and the constants store does not.
- **Derivation, not annotation.** Every displayed number -- hover text,
  descriptions, L-176's illustrated dimensions -- is interpolated from
  the stored value at render time. Unification removes the duplicate
  STORE; derivation removes the duplicate STATEMENT. Both are needed:
  L-179 and L-180 are drift INSIDE constants_new.py today, which proves
  one store does not by itself prevent drift.
- **Cross-repo scope (new).** The gallery's `data/objects_config.json`
  carries feature values, has ONE commit in its history, has no writer
  anywhere in either repo, and has no per-value source fields. The
  nightly builder refreshes positions from Horizons and copies features
  verbatim (`features_out[slug] = feats`), so a green nightly build
  never refreshes feature geometry and gives no signal that it did not.
  Batch 2 is scheduled to move Saturn's values; nothing would carry the
  correction across. Confirmed live: the 2026-08-06 nightly touched
  vectors, elements and positions and did NOT touch objects_config.json
  or feature_configs.json.
- Tony-action (decide): push vs pull across the repo boundary -- handed
  to Fable for review 2026-08-06. Every push variant that genuinely
  detects staleness ends up making the same network call pull makes,
  while still carrying a second copy on disk. A content hash recorded
  beside its own artifact detects corruption, NOT staleness.
- Tony-action (decide, settled): description interpolation ships in this
  build, not as a follow-on. Tony's reasoning doubles as an acceptance
  test -- "this should be minor if the architecture is right." A large
  Mode 5 surface is evidence the architecture is wrong, not evidence the
  scope was too big.
- **TONY'S RULING 2026-08-07: `constants_new.py` IS THE STORE, and
  `objects_config.json` stops carrying feature values.** The `features`
  key is emptied and the store owns them. His reasoning: two files
  claiming the same value violates single-source-of-truth, and the
  frozen-file rule on `objects_config.json` "is a rule we can't observe
  either way, to keep it current" -- so freezing it does not protect
  anything that matters. This settles the ownership question the
  cross-repo scope note above raised but did not rule on.
- **Why it had to be ruled.** The builder assembles
  `feature_configs.json` from `objects_config.json`'s `features` key
  (`features_out[slug] = feats`). Track 0 would have the builder import
  `FEATURE_REGISTRY` instead. With both in place the builder picks one
  silently: edit the store, and if it still reads the config your edit
  never reaches the cache while every freshness signal stays green.
  That is the L-182 shape -- one value, two homes, no rule.
- **SERVED STATE MEASURED 2026-08-07** (gallery `33fc7d6`), and it is
  not what the project assumed. The hand-copy was INCOMPLETE when made,
  not merely stale. Jupiter: 4 of 4 rings with all three fields, plus
  belts -- every value matching the orrery EXACTLY. Saturn: 7 of 7
  rings but `thickness_km` absent on all seven, and NO radiation belts
  or Enceladus torus at all. Uranus and Neptune: nothing served, and
  neither slug exists in `objects_config.json`'s twelve. So the
  transport's job is not "keep a synced copy fresh" -- it is "serve
  data that has never been served." No drift found in what IS served.
- **Which makes Jupiter the right pilot for a better reason than size:**
  it is the only body whose served feature data is complete and
  correct, so the transport has a real acceptance test. Stage 1,
  reproduce Jupiter's existing `feature_configs.json` entry exactly
  plus `source` fields -- proves the transport is faithful. Stage 2,
  serve something never served (the Io torus, or Saturn's
  `thickness_km`) -- proves it can extend the cache, which is the
  actual job. Neither 5 entries nor 12: 4 rings plus 2 belt values to
  match, then one new thing to prove extension.
- **Artifact 2 cannot be built from today's served data** regardless of
  how good the rendering layer is. Saturn's radiation belts are not in
  the cache, and Artifact 2 is defined as rings PLUS radiation belts.
**Gap:** Fable review complete (rounds 1 and 2, August 2026). Remaining
before build, in order: (a) **(decide)** ratify fetch-and-import;
(b) **(design)** the `FEATURE_REGISTRY` shape covering rings, belt sets
and tori; (c) **(design)** the migration shape and per-body sequence;
(d) decide on the 124 dead tooltip fields. L-184's build path cannot be
defined until this settles.
- **FABLE DESIGN REVIEWS, ROUNDS 1 AND 2, AUGUST 2026** (built on orrery `ee0da47c` /
  gallery `61a78c0`; zero code). Architecture ENDORSED: one store, three
  zones per entry, provenance as data, derivation instead of annotation,
  exporter aborting on a missing source. Every piece extends an existing
  pattern rather than inventing one. All findings below independently
  verified by Claude Opus 5 at the same anchors before recording.
- **Transport form: FETCH-AND-IMPORT.** Recommended by Claude Opus 5,
  endorsed by Fable 5 round 2, NOT YET RATIFIED by Tony. The nightly
  builder resolves the orrery HEAD SHA, fetches `constants_new.py` as
  text at that SHA, imports it, reads the feature values and their
  sources, validates, and writes into staging under existing atomic-swap
  semantics. Python evaluates all derivation natively. Tony's workflow
  does not change. Fable's summary: "round 1's vendored pull with the
  exporter removed -- same fallback property, same SHA recording, same
  quarantine semantics, strictly fewer moving parts, and zero hand
  steps."
- Two earlier candidates retired. Exporting a JSON artifact rests on a
  generation step and a run trigger that do not exist. Reading the file
  with `ast` without executing it fights the store's design: 6 of 49
  top-level assignments are derived rather than literal, and two contain
  constructor calls `ast.literal_eval` cannot evaluate at all.
- **Three premises were removed by Tony's questions to get here**, and
  the pattern is worth carrying: each was Claude reading code and
  treating that as knowing the system. (1) "The exporter" was written as
  live; it is dormant. (2) The 6 derived constants were written up as a
  complication; they are the store's own principle working, and
  `SOLAR_RADIUS_AU` alone has 11 consumers. (3) The claim that the
  gallery could not execute the file was never tested; the store imports
  only numpy and `datetime`, and the builder already hard-depends on
  numpy through astroquery.
- **Round 2 build requirements.** (a) Drop the dead `numpy` and
  `timedelta` imports from `constants_new.py` -- both are imported and
  never used, verified; the store becomes stdlib-only, removing the
  version-skew surface between environments. (b) Add a PRE-IMPORT GATE:
  parse the fetched file with `ast` and check exactly two structural
  properties -- imports on an allowlist, no duplicate dict keys -- then
  hand off to import. This is not a revival of ast-extraction; it reads
  no values. It recovers the one capability fetch-and-import loses: after
  import, Python has already silently kept the last duplicate, so the
  Phobos class becomes invisible. (c) Load via
  `importlib.util.spec_from_file_location` from the staging path with a
  per-run module name; never insert staging into `sys.path`. (d) Add a
  one-line rule to the store docstring: data-only module, no top-level
  I/O -- importing executes top-level code, so a future file write or
  network call would be inherited silently every night.
- **FEATURE_REGISTRY: shrink the contract to one name.** Track 0 defines
  a single dict in the store mapping body slug to that body's feature
  entries, and the builder reads exactly that name. Every rename,
  regrouping, or nesting change inside the store then stays internal; the
  only breaking change left is renaming the registry itself, which is one
  grep from impossible to miss. This is the mechanical answer to the
  coupling question, and it demotes the three documentation notes from
  load-bearing to descriptive.
- **PROMOTED TO PHASE 2 TRACK 0 (Tony's ruling, 2026-08-07).** The order
  is scaffolding, then provenance batches, then Artifact 2. Reasoning: a
  golden artifact is fingerprinted, so locking one on values that are not
  yet sourced and derived means redoing the lock rather than editing a
  number. Scaffolding first is the cheaper order, not the slower one.
  This supersedes the August 5 "clear all batches before Artifact 2"
  instruction -- batches still precede the artifact, but Track 0 now
  precedes the batches. See MASTER_PLAN_INTERACTIVE_GALLERY.md v17,
  Phase 2 track structure.
- This item left Prep Work because it outgrew it. As reframed it carries
  one store, a citation-form migration, derivation across five
  restatement surfaces, a generator, a cross-repo transport, and a
  load-time validation pass. That is phase-scale work, and leaving it in
  a section meant for small gating tasks is why the August 6 design
  session kept expanding -- implementation questions were being answered
  against no scope boundary.
- **Open decisions are SCOPED, not blocking.** Transport form, generator
  shape, and unit-sanity validation live in master plan Section 7 as
  decisions 12, 13 and 15. They are answerable once Track 0 has a scope
  boundary to answer them against; none of them gate starting Track 0.
- **TRACK 0 EXIT CHECKLIST for the transport piece.** Recorded here
  rather than as a separate ledger handle -- it is the same work, and
  multiplying handles buries rather than clarifies. The transport piece
  is NOT done until all of the following hold:
  (a) values flow from `constants_new.py` to the served cache with no
      hand step;
  (b) every physics value carries a source, enforced by an abort rather
      than a warning;
  (c) all four validation layers are in place (master plan decision 15):
      source presence as an ABORT not a warning; unit-sanity RANGE
      checking, since shape and source-presence validation both pass on a
      value whose units changed and only magnitude bounds catch a
      km-to-AU slip; a cross-field ring invariant using `inner <= outer`
      -- NOT Fable's strict `<`, which was verified against the store and
      would fire on 8 Neptune entries where inner and outer are
      deliberately equal (Le Verrier at 53,200 km, six Adams arcs at
      62,932 km; `inner > outer` is genuinely zero across all 33 pairs);
      and a nightly value-diff against last night's committed copy
      logging old, new, and both orrery SHAs, which is the only guard
      that sees CHANGE itself -- the L-182 family;
  (f) the JSON-serializability boundary is enforced: import yields live
      Python objects while the cache is JSON, and the store already holds
      a function (`color_map`) and a datetime (`HORIZONS_MAX_DATE`) at
      top level. Every value bound for the cache is coerced to plain
      int/float/str/list/dict; anything else is a validation failure, not
      a crash mid-write;
  (g) the interpolation locus is decided before the cache schema is
      written (master plan decision 17). Fable recommends builder-side
      pre-interpolation: it keeps the assembler dumb and moves template
      errors to build time where quarantine exists, rather than into a
      user's browser;
  (d) the store-to-builder coupling is reduced to the single
      `FEATURE_REGISTRY` name and documented on BOTH sides. Under
      fetch-and-import the builder reads NAMES, not structures, so
      nesting and shape changes no longer break it and only a rename
      does -- weaker coupling than the retired `ast` route implied. A
      note placed on one side reaches only one of two editors, the L-182
      shape again. Three places: a comment at the registry in
      `constants_new.py` (catches the editor mid-edit, rank first), a
      field note in `provenance-discipline` (fires on any store work),
      and a field note in `gallery-cache-builder` (fires from the
      consumer side).
  (e) the run manifest records BOTH the orrery SHA and the content hash
      of the fetched `constants_new.py` (`_write_run_manifest`, builder
      line 1476), so any served state traces to exact store bytes.
- **Sequencing within Track 0 is now open, not settled.** The earlier
  "build transport after Track 0" reasoning assumed a shape-sensitive
  extractor. Fetch-and-import is not shape-sensitive, which reopens it.
  Fable round 2 recommends a PILOT SLICE: migrate Jupiter (5 entries)
  through the full Track 0 treatment, build the transport end-to-end
  against it, then scale to the remaining 32 -- which needs zero
  transport rework. The argument: the transport cannot be tested against
  today's store at all, since no `source` fields exist for
  abort-on-missing-source to act on, so "transport after Track 0" really
  means "first end-to-end test after all 37 entries move," the largest
  possible batch before the first proof. Jupiter also holds the
  resistant-prose cases. Cost: two passes over the migration tooling.
  Tony-action (decide); master plan Section 7 decision 16.
- **L-179/L-180 change role under this order.** They were a gate standing
  in front of the migration. They are now the FIRST thing Track 0 fixes.
  Same requirement, better placement.
- Correction worth carrying: `export_orbit_cache.py` is a DORMANT Phase
  1b seeding tool, not a live exporter. Nothing calls or imports it; all
  four tooling maps classify it `dev_tools`; the gallery references it
  only as a historical porting source at orrery `4e2629c`. The August 6-7
  session twice built on the assumption it was live and Tony corrected it
  both times. Whatever generates the feature artifact is a NEW
  responsibility, and "run something before pushing" is a habit that does
  not exist today -- a real cost to weigh in decision 13, not a detail.
**Note:** Architecture comes before Batch 2 -- Tony's deliberate
reversal of "clear all batches first," 2026-08-06.
**Ref:** FABLE_REVIEW_feature_constant_unification.md (orrery
`ee0da47c` / gallery `61a78c0`);
PREDESIGN_HANDOFF_feature_constant_unification.md.
**Note (2026-08-25) -- two figures above CORRECTED against HEAD.** The
"about 22 physical values" in the belt and torus surface is 28:
Neptune's four belt regions were never counted. And "ZERO carry a
`# Source:`" is no longer true -- at HEAD three of the eight blocks
do: Jupiter's rings (NASA Ring Fact Sheet, Galileo), Jupiter's belts
(NASA Magnetosphere Overview, Juno) and Neptune's belts (Voyager 2;
Ness et al. 1989). Saturn's rings, Saturn's belts, both tori and
Uranus's belts carry nothing. The bullets above are left as written
because they record what was found on 2026-08-07. See L-240 for the
structural recommendation this surface now has, and L-190 for the
reachability count.
**Ref:** FABLE_shell_consistency_audit_report.md section 2 (Job 2),
migration status summary table.

#### [L-183] Stars / stellar neighbourhood skill (coverage gap)
<!-- L:183 status:OPEN upd:2026-08-05 section:A flag: rice:4/3/70/4 -->
- Fable skills-layer review, Job 1 #1: the largest uncovered domain in the
  project. ~22-24 modules with no owning skill -- the acquisition ->
  processing -> visualization chain for the stellar neighbourhood.
- Scope as assessed: Gaia/Hipparcos catalog fetch and VOTable caching
  (`data_acquisition*`, `data_processing`, `vot_cache_manager`), SIMBAD
  query discipline (`simbad_manager`), the paired dual-mode pattern
  (`hr_diagram_apparent_magnitude`/`_distance`,
  `planetarium_apparent_magnitude`/`_distance` -- one physics, two selection
  modes), stellar parameter estimation and its hand-patch layer
  (`stellar_parameters`, `stellar_data_patches`), Messier handling
  (`messier_catalog`, `messier_object_data_handler`), exoplanet modules,
  `star_notes`, `star_properties`, `star_sphere_builder`,
  `star_visualization_gui`, `catalog_selection`, `sgr_a_star_data`.
- The project already recognises the domain twice: provenance-discipline
  defines a `stars` report domain, and a scanner-hardening episode exposed
  a Tier-1 in `star_notes.py`. The existence of a hand-patch module
  (`stellar_data_patches`) is itself an earned lesson with no written home.
**Note:** Two scope decisions ride with the cut, and the new skill's
frontmatter is where they get settled: where `sgr_a_*` belongs (6 modules,
currently classified `orrery`), and where the shared
`visualization_2d/3d/core/utils` modules belong. The prompt's seed list and
the scanner's MODULE_DOMAIN_MAP disagree at exactly those edges.
**Note:** Trigger cleanup travels with it -- orrery-coding-conventions'
description names `star_visualization_gui` but the skill holds no
star-specific content, so a star-GUI session loads 343 lines and finds
nothing for it while believing it fired the right skill (Fable Job 3 #4).
Move the filename into the new skill's description when it lands.
**Note:** Also noted by Fable: 19 root modules are unmapped in
MODULE_DOMAIN_MAP and default to `orrery`, and 2 map entries point at files
no longer in the root (`smoke_dipole_cone`, `smoke_rotation_axis`) -- a
small scanner-side cleanup that pairs naturally with this work.
DONE 2026-08-06: both stale entries removed and `orrery_rendering` /
`shell_configs` mapped explicitly, in the Task 2a patch (L-184). The
remaining unmapped-root-modules question still rides with this item.
- Tony-action (decide): approve the scope boundary before the cut.
**Gap:** Own design session. Not a bolt-on; the domain has its own
acquisition and caching discipline.
**Ref:** FABLE_skills_layer_review_report.md Job 1 #1, Job 3 #4.

#### [L-184] Interactive build-path push gate
<!-- L:184 status:OPEN upd:2026-08-06 section:A flag: rice:4/4/75/3 -->
- Tony ratified 2026-08-05: the global "Tier-1 = 0" push gate becomes
  "Tier-1 = 0 on the interactive build path" for this phase. The global
  gate was unreachable in practice -- of 206 Tier-1 findings measured at
  `4b82384`, 105 sit in the Earth System domain, a subsystem Artifact 2
  never touches. A gate nobody can reach stops functioning as a gate.
- Tony's correction to the original proposal, and the load-bearing part:
  the gate is BUILT BEFORE the batches it scopes. Deferring the definition
  of a gate to a later item is the same category error as deferring the
  gate. This item therefore records work being done, not work deferred.
- **Task 2a DONE (2026-08-06, local; push pending).** Console output now
  prints the per-domain split under each tier line. MODULE_DOMAIN_MAP
  gained explicit entries for `orrery_rendering` and `shell_configs` --
  both carried findings with no entry and defaulted to `orrery`, and
  `shell_configs.py` is the single most important file on the build path,
  so an accidental default was the one case worth ruling out by hand. Two
  stale entries removed (see L-183). Verified by live run: domain
  coverage-gap note gone, totals unchanged at 877 / 118 files /
  206-581-88-2.
- **Task 2b RESHAPED, not yet built.** The original plan was to compute
  build-path membership by walking the import graph from named orrery-side
  entry points. Tracing at `24452442` found the premise wrong in three
  ways: (1) the named entry points (`tools/gallery_cache_builder.py`,
  `gallery_studio.py`, `json_converter.py`) live in the GALLERY repo, not
  the orrery, and the scanner only scans the orrery; (2) the cache builder
  imports nothing from the orrery at all -- its docstring states "No orrery
  imports" as a design decision, so an import walk from it finds zero
  orrery modules; (3) `gallery_studio.py` does import three orrery modules
  (`info_dictionary`, `visualization_utils`, `celestial_objects`) but as
  FUNCTION-LOCAL imports inside function bodies, which a header-only walk
  misses entirely.
- Artifact-2 path measured by named file at `4b82384`: shell_configs 23,
  idealized_orbits 26, planet_visualization_utilities 4, saturn shells 1,
  uranus shells 1, orrery_rendering 1, jupiter shells 0, neptune shells 0
  -- 56 total. Two consequences: the gas giant shells are ALREADY nearly
  clean (2 Tier-1 across all four), so Batch 2's job on those files is
  value verification rather than Tier-1 clearance; and Artifact 2 is not
  blocked by scanner debt in the shells themselves.
- Tony-action (decide): entry points for the computed path, once the
  L-181 architecture settles. The two questions are now coupled.
**Gap:** 2b blocked on the L-181 architecture review (Fable, sent
2026-08-06). The build path cannot be defined until the cross-repo data
flow is decided.
**Ref:** HANDOFF_next_session_masterplan_v16.md Task 2;
MASTER_PLAN_INTERACTIVE_GALLERY.md v16, *New in v16* block.

#### [L-185] Source discipline for the assembler's own constants
<!-- L:185 status:OPEN upd:2026-08-06 section:A flag: rice:3/3/90/1 -->
- Tony's ruling, 2026-08-06: the same source discipline applies to the
  assembler's constants even though there are only a few.
- The assembler reads DATA (positions, elements, feature configs) from the
  served cache and authors none of it -- that model is correct. But it also
  performs arithmetic (client-side Kepler propagation, km-to-AU
  conversion), and arithmetic needs constants that arrive in no cache file.
- Uncited at gallery `e7e8c5e`: `AU_KM = 149597870.7` in
  `gallery/assembler/render_orbits.py:41`,
  `gallery/assembler/render_objects.py:20`, and
  `gallery/assembler/tests/test_artifact1_earth.py:43`;
  `K_GAUSS = 0.01720209895` in `render_orbits.py:42`;
  `_JD_UNIX_EPOCH = 2440587.5` in `tools/inspect_staging.py:63`.
  Total `# Source:` citations in the whole gallery repo: 4.
- The correct pattern already exists at `tools/gallery_cache_builder.py:89`
  -- a cross-repo citation naming file, line, and source SHA:
  `# Source: constants_new.py:47 (orrery 4e2629c) -- IAU km per AU.`
  Apply that shape to the five uncited lines.
- Reasoning error worth recording, because it generalizes: an earlier draft
  dismissed these as low-value because the values are exact by definition
  and will never drift. That substitutes "will this drift?" for "is this a
  claim?" Stability makes a value EASY to source, not exempt from sourcing.
  A reader meeting an uncited number cannot tell a deliberate skip from an
  unchecked one. Call it skip-because-stable; it is cite-to-clear pointed
  the other way.
- Not evidence on the push/pull fork. These values do not drift, and an
  earlier draft leaned on them there incorrectly.
- `No Shadow Constants` [CRITICAL] normally prescribes deleting the local
  copy and importing the real one. That remedy is UNAVAILABLE across the
  repo boundary while self-containment is preserved, which is the one place
  these constants touch L-181's architecture question.
- **Scope additions, 2026-08-06.** Tony approved folding in the
  orrery-side shadow constant found by the same scanner run:
  `orbit_data_manager.py:1850`, `KM_TO_AU`, classed `derived` (computed
  from pinned literals rather than from the imported name). Here the
  standard remedy IS available -- delete the local definition and import
  -- and the audit is explicit that adding a `# Source:` would
  cite-to-clear a structural problem.
- **Fable review found four more gallery sites the handoff enumeration
  missed** (verified at `61a78c0`): `tools/gallery_studio.py` lines 1035,
  1051, 5520 carry BARE LITERALS `149597870.7` inline in expressions, not
  even assigned to a named constant -- worse than every enumerated case,
  violating assign-don't-hardcode on top of being uncited.
  `tools/gallery_cache_builder.py` lines 127 and 135 use `2440587.5`
  inline (the docstring at 123 explains it; the citation shape is
  absent). `tools/test_gallery_cache_builder_offline.py:34`
  `_MOCK_K_GAUSS` carries an in-repo mirror comment but no physical
  source -- a mirror note is not a citation; once `render_orbits.py`'s
  citation lands, the mock should point at it.
- Running total: roughly eight sites, one bounded hand pass.
- **Fable ruling, endorsed: keep the arithmetic constants in CODE.** The
  temptation under vendored pull is to let `AU_KM` and `K_GAUSS` ride
  along in the artifact. Do not. They are exact-by-definition or
  conventional, so making the assembler's arithmetic depend on a cache
  read adds a failure mode (cache unreadable means no math at all) for
  zero drift benefit. The line-89 cross-repo citation is the right
  remedy.
- Refinement worth taking: once the vendored artifact exists and records
  the orrery SHA per build, new citations can reference "orrery SHA per
  feature artifact" rather than a hand-typed SHA that goes stale.
**Gap:** About eight sites now. Can still ship independently of L-181;
should not wait on a structural build.
**Ref:** PREDESIGN_HANDOFF_feature_constant_unification.md, Open Question 4.

#### [L-186] Cross-check annotation issues -- clear before Batch 2
<!-- L:186 status:OPEN upd:2026-08-07 section:A flag: rice:3/3/80/2 -->
- Scanner reports 12 annotation lines it saw but could not use. None
  changed a score. They matter because an annotation that quietly does
  nothing reads as a completed cross-check to anyone skimming the source.
- Tony ruled 2026-08-07: clear these BEFORE Batch 2 rather than during,
  since Batch 2 will add more annotations of the same kind.
- **Six `duplicate_identity` -- RESOLVED 2026-08-12. Not a data question
  and no annotation was wrong.** Every one was the parser misreading a
  correct line. The retired format put a free-text source before the
  check date, so a source carrying its own publication year was read AS
  the check date and the checker name fell outside the identity. Two
  annotations by two different models read as one checker written twice.
  Measured at `eb77c83`: 19 units affected against 20 scored correctly,
  and 54 of 134 annotation lines codebase-wide parsed with the checker
  outside the identity.
- Tony ruled 2026-08-12 to fix the root causes rather than edit on top of
  them. Three were found, and the format change addresses all three:
  (a) the format was ambiguous by construction -- free text before the
  date, no delimiters; (b) the scanner's "checker identity" field was
  filled with source-plus-model, so two DIFFERENT sources checked by the
  SAME model would have earned V2, which is the "two Claude passes are
  one leg" hole; (c) nothing bound the skill's examples to the parser --
  the skill's own Model Credit example was a line the parser could not
  read, and the test fixtures had used checker-first since the parser was
  written, so all three stores disagreed in silence.
- **New grammar, checker first:**
  `# Cross-checked: <checker> <ISO date>[ -- <source>] (<worksheet>.md)`.
  The retired order is now REFUSED as `legacy_source_first` rather than
  reconstructed. 134 annotation lines migrated across 8 modules by
  `patch_L186_annotation_checker_first.py`; grammar guard, tests, skill
  v2.0 and this entry by `patch_L186_grammar_guard.py`.
- **The store-binding test is the durable part.** It now lives in
  `skills_index.py` rather than the test suite: every annotation example
  in every SKILL.md must parse as `provenance_scanner.py` reads it.
  Placed there deliberately, because that tool runs at the moment a skill
  changes, which is the moment the drift gets introduced. Tony's fact,
  2026-08-12: "I don't independently run tests like that unless you ask
  during the build" -- so a check living in the suite is a check that
  does not run. Cause (c) cannot recur silently.
- **SECOND HALF, 2026-08-12: the 55 pinned literals are retired.**
  `test_constants_provenance.py` held its own copy of 55 measured values,
  which is the same two-store defect one layer over: every correction
  needed a synchronized hand-edit in two files, enforced by nothing. The
  August 2 batch corrected six constants and updated no pins, and the
  tests then failed correctly for ten days describing sourced values as
  "drifted." The pins also carried unaudited citations -- the scanner
  extracts claims only from narrative-role files and that one is
  `Role: devtool` -- and at least one was FALSE:
  `test_chromosphere_radii` attributed ~1.5 R_sun to Carroll & Ostlie
  Ch. 11, the same chapter the August check read as ~2000 km (~1.003
  R_sun). Wrong-but-cited in a file nothing audits.
- **18 tests remain and they are a different kind:** derivations,
  orderings, cross-consistency, completeness. None holds a copy of a
  measured value, so none goes stale when a value is corrected.
- **Replaced by `constants_change_report.py`**, which stores no numbers.
  Tony's framing: "What I don't think we should do is create a second
  dictionary. Can we create a diff that would alert us to drift or
  intentional revision?" It asks git what changed in `constants_new.py`
  since the last commit and reads both values out of the diff. A
  deliberate correction moves the number AND its comment block;
  corruption moves the number alone. It also covers constants that do
  not exist yet -- a value added next month is reported the first time it
  moves, with nobody writing a test. Wired into the runner as the first
  checker.
- **Both of its blind spots announce** (Tony: "such a gap should announce
  and we would track it down"). Two values changed in one block with one
  comment edit reports AMBIGUOUS and credits neither; a changed line
  carrying a digit that matches no shape it reads is listed as NOT
  CHECKED. Exit 0 means everything was read and everything documented.
- **The worksheet evidence chain moved to `documentation/worksheets/`**
  (34 files: prompts sent, worksheets returned, cited or not). Tony's
  reasoning: these stopped being archive the moment a tool started
  reading them. `data/` was considered and set aside -- it means what the
  application produces and consumes. The 134 annotations name bare
  filenames, never paths, so nothing in any source module changed. Nine
  worksheets are cited by no annotation; those are NOT orphans, they
  cover files the provenance sweep has not reached yet.
- **Six `non_markdown_reference`**, splitting two ways. Three in
  `constants_new.py` (124, 152, 293) say "(Gemini worksheet)" with no
  filename at all -- genuinely incomplete, supply the real worksheet
  name. Three in `eris_visualization_shells.py` 478 (x2) and
  `venus_visualization_shells.py` 681 DO name the `.md` file but append
  the checked value, e.g. `(batch1_tier2_followup_gpt.md: 14.27 Mkm)`.
  The parser tests that the parenthetical ENDS in `.md`, so a richer
  annotation is rejected for carrying more provenance, not less.
- Tony-action (decide): strip the appended values to satisfy the parser,
  or extend the pattern to accept `(worksheet.md: value)`. Claude's lean
  is to extend, since the format currently punishes better annotations --
  but this is adjacent to "do not loosen a checker to clear findings," so
  the ruling is Tony's. If extended, it is a scanner change and should
  follow the same land-scan-diff sequencing as the SOURCE_PATTERNS work
  in L-181.
- **Sequencing under the v17 order:** Track 1 work, so it now follows
  Track 0. That is a real gain -- Batch 2 and this cleanup both write
  into whatever citation form Track 0 establishes, rather than writing
  comment-form annotations Track 0 would then migrate.
**Gap:** Six data questions, three fill-in-the-filename fixes, one parser
ruling.
**Ref:** PROVENANCE_AUDIT.md, CROSS-CHECK ANNOTATION ISSUES section, at
`ee0da47c`.

#### [L-187] info_dictionary numeric-overlap enumeration
<!-- L:187 status:OPEN upd:2026-08-07 section:A flag: rice:3/3/60/3 -->
- Fable review, Open Question 2(d): do NOT extend the L-181 interpolation
  migration into `info_dictionary.py` now. Applied literally, the
  derivation rule would pull every numeric claim in 2,248 lines of prose
  into scope -- a scope explosion contradicting the settled "one pass,
  bounded to the store" ruling.
- The principled boundary Fable proposes: where a number in INFO prose
  DUPLICATES a stored constant, interpolate it (it is a two-copy pair at
  L-182 risk); where a number exists ONLY in prose, it stays prose with
  its `# Source:` comment -- provenance on narrative, a different job.
- The preparatory task is therefore an ENUMERATION, not a migration:
  which `info_dictionary.py` numbers duplicate store constants. A one-off
  script or a scanner extension.
- Context: `info_dictionary.py` carries 62 `# Source:` comments and was
  deliberately split from `constants_new.py` to separate narrative
  content (fact-checked) from numeric constants (source-cited). It is
  also one of three orrery modules `gallery_studio.py` imports directly,
  via function-local imports a header-only import walk misses.
**Gap:** Write the enumeration. Then decide scope from real numbers.
**Ref:** FABLE_REVIEW_feature_constant_unification.md, Open Question 2(d)
and findings summary #5.

#### [L-192] Worksheet checker -- verify a value against its own evidence
<!-- L:192 status:OPEN upd:2026-08-15 section:A flag: rice:3/3/70/3 -->
- **What it does:** for a constant carrying `# Cross-checked:` lines,
  open the `.md` each line names in `documentation/worksheets/` and
  confirm the worksheet exists and states the value. The skill already
  requires this of a human -- "before citing any worksheet, confirm it
  exists on disk and contains the finding" -- with no tool behind it.
- **Why it is a separate handle from `constants_change_report.py`.** The
  change reporter compares the working tree against the last commit, so
  it is a pre-commit reader: a value corrupted and committed three weeks
  ago is history, not a pending change, and there is nothing in the diff
  for it to notice. This one reads a value against the evidence its own
  annotation names, which does not depend on WHEN the value moved. It is
  the only planned check that reaches committed history.
- **Not routine, and not arbitrary either** (Tony, 2026-08-12). The cost
  was estimated at reading up to 34 markdown files, so it did not belong
  in `maintenance_run.py`. Four trigger conditions, each an observable
  state rather than a judgement call, to be written into
  `provenance-discipline`:
  1. `constants_change_report.py` flags a value -- moved alone,
     ambiguous, or unparsed. SCOPED to those names, so the expensive
     pass runs over two or three constants rather than all of them. The
     cheap check names the expensive one and bounds it.
  2. A cross-check batch lands. New `# Cross-checked:` lines were just
     written; verify each names a worksheet that exists and states the
     value. This replaces the amendment once planned for step 5 of the
     Batch Worksheet Workflow (update the pins), which is moot now the
     pins are retired.
  3. A worksheet is added, renamed, or removed in
     `documentation/worksheets/`. Annotations pointing at it may now
     dangle. Mechanically detectable from the same git diff.
  4. Before a gallery build -- the moment a value stops being local and
     becomes published.
- **An uncited worksheet is PENDING WORK, not a defect** (Tony,
  2026-08-12): the provenance sweep is incomplete, and the nine
  currently uncited worksheets cover files not yet annotated. The
  checker must not report them as orphans.
- **REVERSED 2026-08-14: it is a row in the runner.** The estimate above
  was never measured. Measured, the pass reads 35 worksheets and 104
  annotations in under seven seconds, which is a fifth of the reset
  check already in the table. The trigger conditions are not wrong --
  they are the right list for a scoped, expensive pass -- they were
  written against a cost that turned out not to exist. Recorded rather
  than deleted: a check nobody runs cannot fail, and four conditions
  that must be noticed by a human are four chances not to notice.
  Putting it where the routine already runs is what made 2026-08-15's
  findings visible at all.
- **The schema is settled** (Tony, 2026-08-15). Four fields: code value
  at time of check; value RIGHT/WRONG/UNKNOWN plus the number, or a
  range with its reduction rule stated in the cell; citation
  RIGHT/WRONG/UNKNOWN, separately, because the two come apart in real
  rows; notes, the only place interpretation lives. Not a proposal --
  `worksheet_claude_constants_new_addendum.md` already carries this
  header and already parses. The re-cut is "make the others look like
  the addendum."
- **Break 2 ruled, 2026-08-15: field 2's object stays a NUMBER.**
  Fable asked whether a claim with no number (a rendered qualitative
  sentence) could be verdicted by quoting it verbatim into the value
  cell. Tony: if the checker cannot verify a claim, it should not be
  asked to do so. The class is real and is recorded as L-194;
  it is deferred to a future refactor and blocks nothing here.
- **Break 5 ruled, 2026-08-15: field 3 verdicts the `# Source:` line
  only.** `# Ref:` and `# Also:` are pre-printed on the dispatch row as
  READ-ONLY context -- visible to the responder, never verdicted, never
  read by the tool. One tri-state, and the 65-row count does not move.
  Measured @253bcdd: 20 citation blocks in the repo carry more than one
  leg, at least 9 of them in the dispatch corpus, all in
  `constants_new.py`. Shapes: Source+Ref (4), Source+Ref+Also (3),
  Source+Also (2). In the normal case the extra legs are a locator and
  a corroboration for one authority, not separate claims --
  `SUN_RADIUS_KM` cites IAU 2015 B3, then the paper documenting it,
  then a NASA factsheet. The blocks where the authority is NOT in the
  Source line are a malformation, not a schema case, and are handled
  as L-195. A schema that bends to fit a bad annotation makes the bad
  form permanent.
- **Dispatch shape: one pre-printed row per (key, ordinal)** (Tony,
  2026-08-15), with field 1 filled in by the builder so the responder
  fills only verdicts and notes. Measured on the corpus: 53 rows become
  65. It is what makes Roche's three provenance legs and Eris's four
  claims expressible at all, it deletes `match_row()` and the 25
  UNMATCHED findings that fuzzy binding produced, and a later ordinal
  shift stops matching its pre-printed value loudly instead of binding
  to the wrong claim silently.
- **Builder and key rule built 2026-08-15**, see the as-built below.
  `match_row()` is NOT deleted: rule 0 sits ahead of the four fuzzy
  rules rather than replacing them, because 104 annotations still bind
  through them. That is the transition the sequencing decide below is
  about, and this build is the first half of it.
- **Sequencing, not yet ruled.** The checker simplification the schema
  permits -- deleting `match_row()`, a strict fail-loud verdict grammar
  -- is gated on the re-cut, not the reverse: fuzzy matching cannot be
  removed while 104 annotations still depend on it. Either both formats
  stay readable through the transition or the re-cut is atomic.
  **Tony-action (decide).**
- **Ref:** L-186 (the annotation grammar and the pin retirement it
  replaces); L-188 (the runner it now runs in); L-193 (qualified
  verdicts, and the interpretation layer this schema is meant to
  delete); L-156 Phase 2 (the cross-check batches that produced the
  worksheets); `documentation/HANDOFF_20260815_checker_honesty.md` and
  `documentation/FABLE_REVIEW_worksheet_schema.md`.

##### As built, 2026-08-15: the request builder and the key rule

Built on `87176e9` at https://github.com/tonylquintanilla/palomas_orrery.
One build, two consumers, because `worksheet_keys.py` had none: the
checker did not import it and `resolve()` was never called on the
checking path. Shipping the builder alone would have put keys into
outgoing worksheets that the returning checker could not read --
worksheets that look right and check the old way.

- **`worksheet_request_builder.py` (new, ~310 lines).** Reads the
  annotated corpus through the checker's own `collect_claims()`, mints
  a key per site through `worksheet_keys`, and emits one pre-printed
  row per (key, ordinal) with the code value filled in. Measured on the
  corpus: **65 rows over 65 distinct keys, zero collisions** -- the
  53 -> 65 figure reproduced from the corpus rather than carried from
  the ruling. It judges nothing: no verdict token, no route. The
  checker judges; the builder asks.
- **Rule 0 in `match_row()`.** An exact key match wins outright. A key
  the WORKSHEET carries that no longer resolves announces KEY_STALE and
  does NOT fall through to the fuzzy rules, because falling through
  hides a rename behind a lucky prose hit. `ROLE_KEY` registered with
  the `key` and `row key` headers.
- **The circularity caught in test.** The first implementation resolved
  the CLAIM's key to decide staleness. That key is minted from today's
  source moments earlier, so it always resolves -- a check that cannot
  fail. Corrected to resolve the keys the worksheet carries, which is
  what a rename looks like from this side.
- **Two design calls, both stated because neither was ruled.** The
  citation legs print ABOVE the response table rather than as columns:
  nine columns is already at the limit of what these worksheets are
  filled in with, and a leg sitting in a cell invites a verdict token
  typed beside it, which is the compound answer the checker may not
  interpret. And the response table keeps the addendum's header text
  verbatim, so the checker's existing role registry reads it with zero
  unrecognised columns.
- **Round trip proven at the format layer,** not assumed: the emitted
  file was parsed back through `parse_tables()` -- one row table, 65
  rows, zero unregistered headers, all eight roles resolved, and rule 0
  binding a row by key.
- **Tests 61 -> 69.** All six new checks are synthetic ON PURPOSE: no
  worksheet in the corpus carries a Key column, so the live run cannot
  reach rule 0 and a green run proves nothing about it. One check is
  load-bearing -- a stale-key row whose PROSE would match -- and it was
  mutation-tested by breaking the rule deliberately to confirm it goes
  red.
- **A scanner finding from the pre-test, worth recording.** The new
  module first classified as role `undetermined`, which scored its
  display-width constant as an uncited physical claim and moved Tier-1
  206 -> 207. A `Role: devtool` line in the docstring returned it to
  206. A new dev tool without a role line is scored as though it made
  claims about the world.
- **What this does NOT do.** No dispatch. The first dispatch that
  relies on the Break 5 rule should follow L-195, since a block whose
  authority is not in its `# Source:` line would be verdicted CITATION
  RIGHT while the real authority went unchecked.

##### As built, 2026-08-12: the attachment rule (scanner half)

Built and pushed at `878e2c9`, audit regenerated at `c5218f6`. The
worksheet checker this item was opened for is NOT built; this is the
prerequisite that surfaced while measuring it.

- **What was wrong.** `score_unit()` counted any cross-check annotation
  inside the citation window (30 lines back, 15 forward for a constant).
  That window is right for a CITATION -- a section header naming a
  source legitimately covers the declarations beneath it -- and wrong
  for an ANNOTATION, which names one checker who verified one value on
  one date. Proximity is not attachment.
- **The case that settles it.** `INNER_LIMIT_OORT_CLOUD_AU` scored the
  cross-checked rung on annotations belonging to the heliopause
  constant above it. The two worksheets those annotations name read
  UNVERIFIED (Claude) and PARTIAL (GPT) for the Oort value. The window
  was converting a recorded non-verification into a top-rung badge --
  wrong-but-cited, produced mechanically.
  `MERCURY_RADIUS_KM` and `VENUS_RADIUS_KM` are the milder form: top
  rung on `MOON_RADIUS_KM`'s annotations, three and six lines below.
- **Ruling (Fable 5, 2026-08-12, Mode 7 relay; Tony ratified).** The
  SCANNER narrows, rather than the checker reporting and leaving
  scoring alone. Two definitions of "which annotations belong to this
  value" would drift apart by construction. The worksheet checker
  consumes the scanner's attachment.
- **The rule.** A module-level unit takes the unbroken comment run
  directly above its own statement plus the one directly below --
  `constants_new.py` writes citations below the declaration, the shells
  modules write them above, and both are correct. A string nested in a
  dict or a function body takes only the run above the ENTRY LINE that
  introduces it, never the literal's own line. A blank line or a line
  of code ends a run. Scope is annotation CREDIT only; citation
  inheritance and the malformation diagnostics keep the wide window.
- **Measured: 50 of 77 units at the cross-checked rung keep it; 27
  drop.** Zero ambiguous runs exist today, so adopting strictness cost
  nothing.
- **An orphan report is part of the rule, not an extra.** An annotation
  whose comment run touches no code is printed with file and line.
  Silence about the unattached is the same failure as silence about the
  unexamined. Four exist: `constants_new.py` 145-146 (SOLAR STRUCTURE)
  and 316-317 (CENTER BODY RADII), both section headers written to
  cover a group.
- **Group annotations are NOT given block grammar** (Fable's
  recommendation, Tony's call). A parser cannot distinguish group
  intent from proximity -- in bytes they are identical. The reason to
  prefer per-value: a block-scope annotation reading "everything below
  checked" would have papered over the two UNVERIFIED Oort rows inside
  its scope. Per-value forces the author to read each row.
- **Backfill is VERDICT-GATED.** Appearing in a worksheet is not a
  passing check. Venus reads YES/YES, Mercury PARTIAL/YES, the Oort
  values UNVERIFIED/PARTIAL. Only a verdict that is a completed check
  earns an annotation; the rest stay at V3 with their state visible.
  Whether PARTIAL counts is open (Tony, decide).
- **Test consequence.** `test_lookback_window_bleed_is_measured` had
  pinned the bleed deliberately, with a note saying that if it ever
  failed the window had changed. It failed. Renamed
  `test_lookback_window_bleed_is_closed`, asserting the opposite, both
  halves still pinned.
- **Corpus measurement, carried for the checker build:** 134 live
  annotations, all 134 parse under the L-186 grammar, 18 distinct
  worksheets named, zero dangling. Of 34 files in
  `documentation/worksheets/`: 18 cited, 9 uncited worksheets, 7 prompt
  files. The existence half is clean; the value half is the build.
- **Method note worth keeping.** Fable's written rule and its own
  measurement script disagreed -- the prose said the entry line, the
  script used the literal's line -- and the independent verification
  leg reproduced the error, because it implemented the same prose and
  read it the same wrong way. The agreement between two implementations
  was reported as confirmation and was not. Caught only by re-reading
  the written rule against the code being produced. Cross-AI
  independence protects against a shared model, not a shared spec.

##### Pre-design reviewed, 2026-08-13: the checker itself

Documents: `documentation/PREDESIGN_L192_worksheet_checker.md` and
`documentation/FABLE_REVIEW_L192_worksheet_checker.md`, both anchored
`00219d9`. Fable's verdict: **sound, with changes.** Not built.

**Purpose, restated.** The checker confirms that an annotation's claim
of evidence is TRUE. It is the only planned check reaching committed
history: `constants_change_report.py` is a pre-commit diff reader by
construction, so a value corrupted and committed three weeks ago has
nothing in the diff to notice. The worksheet is a fixed record and says
what it said.

**Four layers, each with a named failure.** L0 worksheet exists
(currently zero failures across 134 annotations -- passes today, can
still fail on a rename or a migration-mangled filename). L1 the row is
located (failure: UNMATCHED). L2 the value agrees (failure: MISMATCH --
the loudest finding available, because the code and its own evidence
disagree about a number). L3 the verdict is read (failure: an
annotation asserting a completed check over a row recording an
incomplete one -- the Oort case).

**Fable's three additions, all accepted:**

- **Identity consistency.** Nothing checked that the named worksheet
  belongs to the named checker, so two annotations naming different
  models over one model's evidence would pass all four layers and fake
  the rung. Rule: the worksheet filename must contain the checker
  token, case-folded. Verified independently: 134 of 134 pass today,
  and an injected Gemini-over-Claude-worksheet violation is caught.
- **Drift-since-check (L2b).** The tier2 schema records `Code value` --
  what the checker read at the prompt's SHA. Comparing it to the code
  NOW detects a value edited after its check. Verified coverage: the
  column reaches **72 of 134** annotations, not the whole corpus.
- **DERIVED split out of QUALIFIED.** ACCEPTED AS A SPLIT, REJECTED AS
  A DISPOSITION. Fable proposed "closed by derivation, do not queue,"
  citing L-158. **L-158 rules the opposite**: it explicitly retired the
  derived-rung framing, and holds that a runtime-derived value inherits
  its weakest input's rung only once the derivation logic -- formula,
  units, parent reference -- has cleared one independent cross-check,
  and is unverified until then. Fable and GPT both rejected the
  immune-by-derivation premise in July, citing Mars Climate Orbiter.
  The convention wins; a DERIVED row is PENDING, not closed.

**Comparison rule (Fable, accepted).** Exact-or-rounded, never "within
tolerance." A significant-figures tolerance would call Mercury's 2439.7
and JPL's 2439.4 +/- 0.1 a match at three figures and the finding would
vanish. A range cell is never MATCH; it is RANGE, its own class. A
comparison needing a unit conversion is MATCHED-VIA-CONVERSION, its own
class, because the conversion imports the project's own constants into
the comparator.

**Row matching (fork 1, Fable: (a) plus (c)).** Header-role mapping is
the primary matcher; an unrecognised header set makes the whole
worksheet WORKSHEET_UNREADABLE, announced every run. Value-based search
is permitted only against the CODE-VALUE column, never the evidence
column. Future worksheet prompts emit one schema with a key column --
now carried in provenance-discipline v2.1.

**Where it runs (fork 4). RULING CHANGED, 2026-08-13.** The earlier
ruling kept the checker out of `maintenance_run.py` on cost grounds.
Tony's reason was never file size: it was one more block of output to
read on every push. Ruling: **the checker joins the runner**, printing
ONE line on a clean run with its denominator ("134 annotations, N
verified, M unmatched"), findings to the audit. Report-only -- it does
NOT gate pushes; expanding the Tier-1 gate stays a separate decision.
A line carrying a denominator moves when something moves; a line that
always reads the same is wallpaper, and wallpaper is a check that
cannot fail.

**Uncited worksheets (fork 5, accepted).** One line steady-state with
the date the set last changed; the full list prints only when the set
differs from the recorded state.

**Writing (fork 3, Fable recommends, Tony has not ruled).** A
`--propose` mode emitting a patch script, never editing in place, with
each worksheet row quoted verbatim beside each proposed annotation --
so review runs against the evidence rather than the tool's claim about
it. The risk is not forgery; it is a matcher bug writing annotations
against wrong rows and the same matcher later confirming them.

**Still open for Tony (decide): none.** All three were ruled
2026-08-13; see the forks-ruled section below. Fable's middle answer
on QUALIFIED -- per-row rulings recorded in
`provenance_exceptions.json` -- was NOT taken. The ruling is simpler
and needs no store.

**Two false attributions, found 2026-08-13 and NOT yet fixed.** Both
annotations credit `worksheet_claude_constants_new.md` for checks it
explicitly did not perform. Row G10 reads UNVERIFIED, "Not checked,"
while the Bennu annotation credits a cross-check against Nolan et al.
Row G14 said the OLD Arrokoth value was wrong; the value was then
corrected against Keane et al. 2022, which the worksheet never opened,
and the annotation rode along unchanged. Both replacement values are
arithmetically self-consistent with their stated inputs, so the numbers
look right and the PROVENANCE claim is what overstates. The checker
will surface both mechanically on its first run. Rule added to
provenance-discipline v2.1.

**RULED 2026-08-13: they stay until the checker's first run, then go
back. Not fixed now.** The rule that governs a PARTIAL row governs a
false attribution -- we do not accept and interpret an answer the
evidence does not support -- so the disposition is return to the
originator: reopen the session that produced
`worksheet_claude_constants_new.md` and ask it either to perform the
two checks or to state plainly that it did not.

The SEQUENCING is the ruling. The first run should catch both as
examples of an incomplete response, and the catch is what routes
them. Fixing them beforehand would remove the only two known-true
failures in the corpus, and a first run that cannot fail is not a
passing run.

(Correction of record: this entry first read "send both back" and
said the leave-in-place option was declined. That inverted the
ruling. Fixed 2026-08-13 in a follow-up patch.)

##### Forks ruled, 2026-08-13: DERIVED, no propose mode, the mismatch route

Skill consequence: provenance-discipline 2.1 -> 2.2, five edits,
pushed with this entry. The rulings are Tony's; the reasoning is the
session record.

**Fork 2 -- what counts as a completed check. PARTIAL and APPROX
return to the originator for completion**, unconditionally and
without first asking why the row is qualified. Neither earns a leg
toward the cross-checked rung and neither is interpreted into one.
This is the August 13 rule -- we do not have to accept and interpret
incomplete or malformed answers -- applied to the verdict vocabulary
rather than only to unreadable worksheets. Fable's middle answer,
per-row exceptions in `provenance_exceptions.json`, is declined: it
stores a judgement where the simpler move is to get a better
worksheet.

**DERIVED is not a third member of that family.** It answers the
CITATION question, not the value question -- no source publishes the
number because the number is computed, so there is nothing for that
column to be right about. It can pair with any value verdict,
including NO. The pre-design's classification table put DERIVED
beside PARTIAL and APPROX as though all three qualified a value.
Measured against the corpus that is wrong, and wrong in a way that
would have returned complete derivations while letting incomplete
ones through.

**A DERIVED row is COMPLETE when it names its inputs, shows the
arithmetic, and the arithmetic closes.** Then L-158 governs: the
derivation logic has cleared its own check and the value inherits the
rung of its weakest input. Not a completed check on its own -- it
hands the question to the premise. Worked case, the Moon's Hill
sphere in lunar radii: 60,000 / 1737.4 = 34.53 closes exactly over a
60,000 km premise that reads APPROX and UNSOURCED, so the derived
figure is worth that and no more. A DERIVED row showing no work is
incomplete and goes back like any other.

**Fork 3 -- the checker does not write.** No `--propose` argument.
Proposed annotations are discussed in conversation before anything is
written. Fable recommended a propose mode emitting a patch script for
review; the mode itself is declined, not merely its safeguards. The
backfill of the 27 happens in conversation, which is also where the
adjudications get made.

**A complete row that disagrees is a FINDING, not a defective
worksheet.** This is the correction that changed the design.
Send-back fires on INCOMPLETENESS; it does not fire on DISAGREEMENT.
A row that names its inputs and shows its arithmetic has already
given everything needed to settle the question, so returning it asks
for what we already hold. A mismatch is therefore reported loudly and
routed to conversation, with no cause assigned by any tool. Three
outcomes, none of them the default:

- CONVENTION MISMATCH -- both derivations correct, answering
  different questions; the code must say which question it answers.
- THE CODE'S NUMBER IS WRONG -- the worksheet wins, the value moves.
- THE WORKSHEET'S DERIVATION IS WRONG -- the code wins.

Every outcome is confirmed in conversation UNLESS THE RULE IS ALREADY
STATED. That clause is what makes writing an adjudication down worth
the effort: a stated rule settles the next occurrence without a
second conversation.

**Two dispositions, and the checker names which one.** An L2 MISMATCH
-- a value and its own evidence disagreeing about a number -- routes
to CONVERSATION, because the cause is open. An L3 failure -- an
annotation asserting a completed check over a row that records an
incomplete one -- routes to SEND BACK, because the cause is already
known. `BENNU_RADIUS_KM` and `ARROKOTH_RADIUS_KM` are the worked L3
cases, and demonstrating that route is part of what the first run is
for.

**The Hill sphere is the worked example, and it is a convention
mismatch.** The standard Hill radius carries an eccentricity factor,
a(1-e)(m/3M)^(1/3), so what it returns is the PERIHELION Hill radius.
Checkers computing at semimajor axis dropped the (1-e): for Eris at
e~0.44 that gives 14.2 Mkm against 8.0 Mkm, which reads as a gross
error and is not one. Nobody did bad arithmetic. This is Tony's
reading and it corrected this session's first pass, which had filed
both Eris and Pluto as live value errors.

Eris is already resolved in the tree and shows the recording shape:
the shell text names both figures and says the shell draws
perihelion, so the next checker who computes 14.3 Mkm reads the
answer before raising it. **Pluto is the same case half-finished.**
Its `# Source:` comments name perihelion 29.66 AU and the
Pluto-Charon system GM, and `radius_fraction` 5041 is consistent with
them -- but the hover text and tooltip a reader actually sees say
only "approximately 5.99 million kilometers" with no basis at all.
**(do)** Apply the Eris fix to Pluto's reader-facing text, in both
`pluto_visualization_shells.py` and `shell_configs.py`.

**An adjudication is recorded with its reason, in the place the next
reader will hit it.** Two shapes already work here: the reader-facing
text for a convention, and a `# Corrected:` line in the comment block
for a changed value -- Pluto's block carries one recording that
`radius_fraction` 4685 drew a 5.57 Mkm shell under text claiming 5.99
Mkm. A verdict with no reason is not an adjudication; it is the same
run repeated later by somebody who does not know it already happened.

**Method note.** The DERIVED reading came from reading the rows, not
from the token list. They split three ways: arithmetic on the
project's own premise, a formula applied to external inputs, and
inference from a measurement -- "high density implies a largely rocky
composition" -- which is not derivation at all. Two worksheets also
write a compound token, `DERIVED -- verified`, which the vocabulary
does not contain. The token was carrying more than one job because
nothing had ever defined it.

##### As built, 2026-08-13: the checker

Built on `b22bcf8`, delivered as three files plus two patch scripts,
pushed at `6de5e8d`. `worksheet_checker.py` (1397 lines),
`test_worksheet_checker.py` (409), rows in `maintenance_run.py`, and
two indented buttons in `palomas_orrery_dashboard.py` above Provenance
Scanner. Tier-1 unchanged at the 206 baseline.

**Six layers, not four.** L0 worksheet exists; LID the worksheet
belongs to the named checker; L1 the row is located; L2a the value
agrees with the evidence; L2b the value still equals what the checker
read; L3 the verdict amounts to a completed check. Fable's two
additions were both built. The checker consumes the scanner's
attachment and has no annotation parser of its own.

**First run: 104 annotations, 3 clean, 39 send back, 22 to
conversation, 30 outside scanner reach.**

**THE PAYLOAD -- four values moved after their check.** This is the
committed-history failure the item was opened for, and
`constants_change_report.py` cannot see any of it, because a committed
edit leaves nothing in the diff.

| Constant | Checker read | Code now |
|---|---:|---:|
| `HELIOPAUSE_RADII` | 26,449 | 26,148 |
| `BENNU_RADIUS_KM` | 0.262 | 0.246 |
| `HAUMEA_RADIUS_KM` | 816 | 715 |
| `ARROKOTH_RADIUS_KM` | 9.95 | 9.1 |

Two annotations each, so the count is eight. **Bennu and Arrokoth were
already known; `HELIOPAUSE_RADII` and `HAUMEA_RADIUS_KM` were not.**
Same shape, and nobody was looking for them. Bennu also returns
CHECK_NOT_PERFORMED at L3 -- row G10 reads UNVERIFIED, "Not checked."
Both known-true failures landed on the first run, which is what the
sequencing ruling was for.

**The checkable corpus is 104, not 134.** Thirty annotation lines are
attached to code the scanner does not score as a unit: the four known
orphans, plus `CORE_AU` and `RADIATIVE_ZONE_AU` (products of two
names), module-level strings like `moon_inner_core_info`, and dict keys
in `shell_configs.py`. That is **L-190**, not a defect here. The list
prints every run and the test suite fails if the count reaches zero,
because zero could mean the scanner started reaching them OR that
somebody stopped collecting them.

**Three corrections the corpus forced, all found by running it.**

- *The constants worksheets carry no value verdict.* Their schema ends
  at `Citation correct?`. The first implementation read that as a value
  verdict and reported twenty refuted values -- exactly the conflation
  the two-column schema exists to prevent. Verdict tokens now carry a
  SCOPE, and a citation verdict can never produce a value refutation.
- *Display strings do not match one row.* The worksheets record one row
  per CLAIM and a paragraph states several, so matching a string to one
  row passes the rest silently. The string path checks every numeric
  claim: **19 of 73 addressed**. Twenty-seven further numbers are
  manual-scale and frame-weight instructions, excluded and counted --
  no worksheet row could ever address them.
- *"Not checked" is not "the source does not publish it."* Collapsing
  them reported Bennu's unperformed check as a citation defect, which
  blames the source for work nobody did. UNVERIFIED and NOT CHECKED
  route to SEND BACK; NOT FOUND and UNSOURCED route to CONVERSATION.

**A divergence from Fable's stated rule, recorded because it was
unilateral.** Fable recommended an exact-match verdict table with
everything else announced UNREADABLE. The registry as built also reads
CONFIRMED, CORRECT, INCORRECT, WRONG, WRONG VALUE, WRONG CITATION, NOT
FOUND, UNSOURCED, NOT CHECKED, and N/A -- the corpus's long tail, each
with a scope. No fuzzy matching was added. But teaching the tool to
read tokens the vocabulary does not contain is arguably backwards under
the August 13 rule: a worksheet writing NOT FOUND where the vocabulary
says UNVERIFIED may be a malformed answer that should go back, not one
the tool quietly learns. **Unruled.**

**Method note, and it is the same lesson one layer down.** During the
build an over-broad slice in an editing script deleted four functions,
204 lines, and `py_compile` reported success -- the file parsed
perfectly and was hollow. `py_compile` verifies that a file parses,
never that it still contains what it is supposed to contain, and a
green result cannot distinguish the two. The fix was a guard asserting
the expected function set survives every edit, run beside the compile
check. Recovered from a throwaway sandbox copy, which is the only
reason it cost minutes.

**The handle stays OPEN.** The checker is built; the backfill of the 27
and the citation-only ruling below are still L-192's body.

**(decide) -- do the 46 citation-only annotations earn a leg?** Every
annotation on `constants_new.py` names a worksheet whose only verdict
column is `Citation correct?`. Those worksheets asked whether the cited
source publishes the value, and answered -- a real check, completed,
but not the same claim as "this value is right." The annotation asserts
a cross-check without saying which kind. The checker reports the class,
names which column it read, and promotes nothing. **46 of 104 sit
here**, so this ruling moves the audit more than any other single
decision available.

Three more Tier-3 tuning constants arrived with the module
(`MIN_PROSE_FRAGMENT`, `INSTRUCTION_LOOKBACK`, `INSTRUCTION_LOOKAHEAD`).
Same question as the three in `provenance_history.py`; fold them into
that decision rather than opening a handle.

#### [L-190] Scanner reach: anything rendered must be reachable
<!-- L:190 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/80/3 -->
- **Tony's rule, 2026-08-07:** "anything rendered from sourced data
  should be reached by the scanner." Stated as a general principle, not
  a one-off fix.
- **It is a stronger rule than the one the scanner was built on.** The
  scanner today reaches values in the shapes it knows -- annotated
  module constants, dict entries, `# Source:` comments. Tony's test is
  whether a value reaches a RENDER, whatever shape it is stored in.
- **The gap that surfaced it.** The gas giant radiation belt and plasma
  torus geometry (about 22 values across four bodies, see L-181) is
  bare literals inside function bodies. The scanner does not see them:
  zero occurrences of `belt_distances`, `torus_distance` or
  `belt_thickness` anywhere in the 879-finding audit at `1ba20c3`.
  Every one of these values renders.
- **Why it matters beyond tidiness.** Batch 2's worksheet is built from
  scanner findings. An assumption formed this session -- that Batch 2
  would source the belt ranges as part of the gas giant cross-check it
  was already doing -- would have handled NOTHING, silently, because
  those values never reach the worksheet. Invisible-to-the-tool is the
  same failure class as uncited: both pass every check.
- Adjacent finding from the same session, worth folding in: the 20-line
  divergence check written for L-179 finds a class the scanner also
  cannot see -- a citation naming a constant and stating a value that
  disagrees with the store. It flags CITED claims, where the scanner
  flags UNCITED ones. See L-189.
**Gap:** Extend the scanner to reach bare literals that feed a render.
Start with the belt and torus values, since they gate Batch 2's
worksheet completeness. Treat as a shared-CI change.
**Note (2026-08-25), measured at HEAD.** The scanner extracts only
DISPLAY STRINGS from the shell modules -- 10 units for Saturn, 20 for
Jupiter, 116 for `shell_configs.py`, every one of kind `string`. The
ring, belt and torus NUMBERS are function-local literals and are not
scored units at all. The surface: 33 ring entries at three fields each
(99 numbers) plus 28 belt and torus values, across four modules. None
of it is reachable by `worksheet_request_builder.py`. Same gap as
stated above, now with a count. See L-181, L-240.
**Ref:** L-181 (the enumerated belt/torus surface); L-189 (run history
and the divergence check); L-156 (Batch 2 worksheet).

#### [L-191] Display-text duplication across the shell modules
<!-- L:191 status:OPEN upd:2026-08-07 section:A flag: rice:3/4/70/3 -->
- **Surfaced by Tony's Mode 5 pass, 2026-08-07.** Literal `<br>` tags
  visible in the Tkinter checkbox tooltips for the solar shells. Tony
  then spot-checked the asteroid belt and Earth tooltips, found them
  CLEAN, and ruled: **Mode 5 survey BEFORE the sweep, not after.**
  That ruling is the item's method and it is what produced everything
  below.

- **ORIGIN, traced not assumed.** On 2025-04-05 (`e3ca900`) the design
  was correct: `gravitational_influence_info` carried `\n` for the
  Tkinter tooltip and `gravitational_influence_info_hover` carried
  `<br>` for the Plotly hover. Same text, two formats, both in
  `constants_new.py`. The naming still carries that intent. Commit
  `97bbfe3` (2026-05-25, "sun indicator refactor") converted `\n` to
  `<br>` in the tooltip variants as well, collapsing the distinction
  while the names kept implying it held. The regression is 2.5 months
  old.

- **SCOPE, corrected three times, and the third correction is the
  large one.** A first estimate of "772 lines across 17 files" was
  WRONG -- it counted every line in the May commit gaining a `<br>`,
  which sweeps in the `_info_hover` strings where `<br>` is correct.
  Resolving every name bound to `CreateToolTip` back to its
  definition then gave 20 affected strings, all in
  `solar_visualization_shells.py`. **That figure was also wrong, and
  low by more than half. The measured scope is 58 strings across six
  bodies** (2026-08-21 survey, reproduced 2026-08-24):

  | Source | Strings |
  |---|---|
  | `solar_visualization_shells.py` (direct call sites) | 19 |
  | Jupiter | 10 |
  | Saturn | 10 |
  | Uranus | 8 |
  | Neptune | 8 |
  | Planet 9 | 2 |
  | Moon | 1 |
  | **Total** | **58** |

  Earth (11 tooltip strings) and asteroid belt (4) remain clean.
  Grep counted a proxy; the render counted the surface -- and the
  20 was a third proxy, better than grep and still not the surface.
- **MEASURED TWICE, BY TWO MODELS, AND STILL NOT CONFIRMED.** Claude
  Fable 5 surveyed at `e1c64dc9` on 2026-08-21 and returned 58. The
  count was withheld from that request on purpose so the answer could
  disagree with the ledger, and it did. Claude Opus 5 reproduced it
  at `94ff80f2` on 2026-08-24 against a tree two days further on, and
  also got 58. **Two static analyses agreeing is still two static
  analyses.** The render check is owed: hover a Jupiter shell
  checkbox and look for a literal `<br>`. Until that happens, 58 is
  measured and not confirmed, and this bullet says so rather than
  letting agreement stand in for a look.
- **The reproduction failed on its first attempt, which is worth
  recording because it is this item's own lesson a third time.** It
  returned 53. It resolved each string with `ast.literal_eval` and
  skipped whatever could not be evaluated -- four solar assignments
  built as f-strings or concatenations -- silently, with a bare
  `continue` and no report. Re-measuring from raw source SLICES
  rather than evaluated VALUES gave 19 solar and reproduced 58. A
  proxy that cannot say what it skipped is the dangerous kind.

- **WHY TWO SURVEYS MISSED THE SAME 39 STRINGS.** They are never
  named beside a `CreateToolTip` call. `build_shell_checkboxes()` in
  `celestial_objects.py` builds the name at RUN TIME from
  `SHELL_DEFINITIONS`,

      tooltip_name = f"{body_prefix}_{shell['var_suffix']}_info"

  and fetches it from a dict the call site passes as `globals()` --
  `build_shell_checkboxes('Jupiter', celestial_frame, globals(),
  globals(), tk, CreateToolTip)`. The string's name exists only as a
  formatted value during execution. A survey that resolves visible
  call-site names finds nothing there and records ZERO, which is
  precisely what the gas-giant bullet below did. Git history puts
  this path live since January 2026, months before the August 7
  measurement, so it is a missed surface rather than tree movement.
- **FOUR PATTERNS EXIST for the same job.** This is the actual finding.
  | Module | Tooltip source | Plot source | State |
  |---|---|---|---|
  | solar | `_info` | `_info_hover` | two copies, FORMAT BUG VISIBLE |
  | earth | `_info` | dict `description` | two copies, correct today, DRIFT-CAPABLE |
  | gas giants | none | `_info` via `.replace()` | one copy, correct |
  | asteroid belt | `_info` | -- | clean |

- **The gas giant pattern is already the fix.** `shell_configs.py`
  carries 16 sites of the form
  `'hover_text': saturn_core_info.replace('\n', '<br>')` -- one string
  authored in `\n`, converted at the Plotly boundary. That IS L-181's
  stated canonical direction, already implemented and working. So this
  item is NOT "invent a `\n`-canonical system"; it is "bring the other
  modules into the pattern the codebase already uses," with a
  reference implementation in the tree.

- **Why only solar broke.** The May sweep changed source strings in
  many modules. For a module whose config converts at the boundary the
  change is a harmless no-op. Solar has no conversion step -- its
  `_info` copy goes to Tkinter exactly as written. Same edit, two
  consequences, because the modules consume their strings differently.

- **EARTH IS NOT THE HEALTHY CASE.** Same two-copies structure as
  solar, the duplicate living inside a layer dict rather than under a
  second module-level name. Measured: **6 of 11 tooltip strings
  duplicate a Plotly `description` VERBATIM**, 1 differs
  deliberately, 4 have no plot pair. It looks correct only because
  both copies still agree. Editing one and not the other drifts the
  content SILENTLY -- and unlike solar's visible `<br>`, nothing would
  show it. L-182's shape.

- **Earth's crust text carries a DESIGN CONSTRAINT on the fix.** Its
  plot description ends with "(Note: toggle off the crust layer in the
  legend to better see the interior structure.)" and its tooltip does
  not. That is deliberate, not drift -- a legend instruction that is
  nonsense in a checkbox tooltip. So a naive collapse-to-one-string
  either loses the note or pushes it where it does not belong. The
  unification needs a way to carry SURFACE-SPECIFIC text alongside the
  shared body. Solar does not surface this requirement; Earth does.
  Design against Earth's harder case, not solar's easier one.

- **CORRECTED 2026-08-24: gas giant shells DO have tooltips, and they
  are most of this item.** This bullet read "Gas giant shells have NO
  tooltips at all -- zero `CreateToolTip` bindings for any
  jupiter/saturn/uranus/neptune shell." The sign was inverted.
  Jupiter has 10 affected strings, Saturn 10, Uranus 8, Neptune 8 --
  36 of the 58, in the four bodies the item recorded as having none.
  There are indeed zero LITERAL bindings in source; they are all
  built at run time, per the mechanism bullet above. "No binding
  visible in source" and "no tooltip" are different claims, and this
  bullet reported the first as the second.
- The dead-key measurement in the same bullet is UNAFFECTED and
  stands. Related
  measurement: the `'tooltip'` key in `shell_configs.py` is defined
  **124 times and read by nothing**, confirming L-181's "124 dead
  tooltip fields" as dead. (Corrected 2026-08-11: this bullet had
  read 126 and described itself as "updating the count" -- but 126
  is the raw text-match total, and the real figure is 124 dict
  keys, 83 in SHELL_CONFIGS plus 41 in CUSTOM_SHELLS, measured with
  `ast`. It revised a correct number back to a wrong one on the
  strength of a grep.) Whether the gas
  giants SHOULD have tooltips is a separate question for Tony.

- **THE DRIFT IS ALREADY REAL, and it is worse than the format bug.**
  `shell_configs.py` carries 52 inline `hover_text` literals that
  duplicate a module string, alongside the 16 correct
  `.replace('\n', '<br>')` sites. **Only 11 of the 52 still agree
  with their module twin. 41 have diverged.** Nothing on screen
  reveals it, because each surface renders its own copy correctly.
  The visible `<br>` bug is the half that announces itself; this is
  the half that does not, and it is four times the size. (Measured
  2026-08-21, structural counts reproduced 2026-08-24.)
- **The 16 reference-pattern sites are currently NO-OPS.** Their
  source strings already carry `<br>`, so `.replace('\n', '<br>')`
  finds nothing to replace. The pattern is correct and the input to
  it is not, which is why the gas giants look right in the plot and
  wrong in the tooltip.
- **Each affected string has exactly ONE live consumer** -- the
  tooltip. That makes the mechanical half of the sweep safer than the
  scope correction suggests: 58 is a bigger number than 20, but no
  string is being read by two places that must stay in step.
- **The shared-fragment pattern from L-179/L-180 is the precondition.**
  One string serving two surfaces means the boundary conversion is a
  one-line change rather than a per-string rewrite.

**Gap (rewritten 2026-08-24 on the survey):** THREE JOBS, not two,
and the first is a look rather than a build.
(0) CONFIRM BY RENDER. Hover a Jupiter shell checkbox -- "-- Core"
will do. A literal `<br>` there confirms the 58 by the surface
instead of by two ASTs, and nothing else should move until it does.
(1) THE 58, not the 20. Solar's 19 through direct call sites and the
39 reached through `build_shell_checkboxes`. Author the `_info`
strings in `\n`, delete the `_info_hover` duplicates, and add
`.replace('\n', '<br>')` at the boundary -- the 16 existing sites are
the template and are currently no-ops for want of `\n` input.
(2) EARTH -- no visible bug, same duplication, and still the case
that decides the SHAPE of the fix because of the surface-specific
text requirement. Design against Earth; apply to all 58.
The 41 diverged `hover_text` copies are inside job 2, not a fourth
job: the mechanism that stops the drift is the same mechanism that
carries surface-specific text.
Tony's standing ruling holds throughout -- Mode 5 survey before
sweep, and it is what produced the correction above.
**Gap+ (2026-08-19):** replacing a typed constant with a read SPLITS a
display-string unit and raises the Tier-1 COUNT while the uncited surface
shrinks. Measured on L-209: `solar_visualization_shells.py` went 3 -> 6
Tier-1 findings, and total counted claims went 52 -> 42, because an
f-string prefix inserted mid-run ends one string unit and starts another.
Same text, same absent citation, more rows to report it in. Expect the
count to climb through this item and L-181 while the files get better;
the real repair for those six rows is citing the corona hover text, which
was owed before today.
**Ref:** origin `e3ca900` (2025-04-05, correct design), `97bbfe3`
(2026-05-25, the regression); L-181 (canonical `<br>` direction and
the dead tooltip decision); L-190 (tooling reach); L-182 (the silent
drift class Earth sits in). Survey:
`documentation/RELAY_REQUEST_L191_survey_fable_20260820.md` (the
request, with the count deliberately withheld),
`documentation/RELAY_RESPONSE_L191_survey_fable_20260821.md`,
`documentation/l191_inventory.json` and
`documentation/l191_cfgmap.json` (row-level evidence).
Mechanism: `celestial_objects.py` `build_shell_checkboxes`;
`palomas_orrery.py` the `globals()` call sites.

#### [L-193] Qualified verdicts -- the token is not the whole answer
<!-- L:193 status:OPEN upd:2026-08-15 section:A flag: rice:3/4/80/2 -->
- **Tony's framing, 2026-08-15, and it is the requirement the whole
  handle serves:** we need to know when values and citations are wrong
  or missing, and when they are not, RELIABLY. Two axes, three states
  each, and "cannot tell" is a legitimate state that must be said out
  loud rather than resolved by picking the likelier reading.
- **The defect.** `classify_verdict` reads the leading token of a
  verdict cell and splits the rest off at the dash. `is_compound` was
  written to flag a cell carrying a token PLUS prose, so the
  qualification would reach a reader instead of being trimmed -- and it
  had ZERO call sites in `worksheet_checker.py` from the day it was
  written. Defined, unit-tested in isolation, never wired in. A guard
  that cannot fire is the v3.39 class, one layer out: it is not that
  the check passed, it is that the check never ran.
- **Measured, 2026-08-15:** 61 of 355 verdict cells in the corpus are
  compound (17%). By class: 17 UNREADABLE, 15 CONFIRMED, 12 REFUTED,
  7 DERIVED, 6 INCOMPLETE, 4 ABSENT.
- **The 15 CONFIRMED are the dangerous ones.** `dispose_verdict`
  returns early on a clearing verdict with no finding recorded, so it
  is the ONE branch where a qualification vanishes -- every other class
  already quotes the whole cell into its finding. "YES -- to 2 decimal
  places" and a bare "YES" were the same row, and the first one is not
  clean. THREE live claims sit on a qualified YES: MOON_RADIUS_KM,
  and the pluto_hill_sphere_info / description pair that is also the
  614/638 merge candidate. The entry first said zero, from a grep of
  WORKSHEET_CHECK.md -- which lists routed findings, and this one is
  recorded without a route. The grep answered a question nobody asked
  and returned a clean-looking number for it.
- **One of the three is a false positive, and it is kept.** "YES --
  fully confirmed" is compound in structure and emphatic in meaning,
  not qualified. The guard cannot tell those apart without reading
  prose, which it is forbidden to do, so it flags the shape and a
  person reads the words. One unnecessary look per two real catches is
  the right side to err on; the wrong side is silent.
- **The 12 REFUTED are the loud ones, and they were reported wrong.**
  In this corpus `NO -- wrong authority` means the value is fine and
  the source is not, while `NO -- arithmetic error` means the source is
  fine and the value is not. Same token, same column, opposite
  meanings. The tool printed the first reading over both: a live
  finding read `reads <<NO -- arithmetic error>> -- wrong authority for
  a value that may still be right`, asserting the opposite of the
  truth directly beside the correct quote.
- **Done 2026-08-15, in the same patch as the L2b change:** compound
  clearing verdicts emit QUALIFIED_PASS and stop counting as clean;
  compound refusals under a citation column emit
  REFUSAL_UNCLASSIFIED and state that the fault cannot be assigned
  here. Seven live rows moved off CITATION_DEFECT. The qualification
  decides WHETHER the tool may classify; it is never read to decide
  WHAT the tool says, which would be a prose-parsed convention.
- **What stays open, and why the handle does not close.** The corpus
  still has one column doing two jobs. 46 annotations name worksheets
  whose only verdict column is `Citation correct?`, so the value
  question has no machine-readable answer anywhere in them. Reporting
  that honestly is done; giving it an answer is the re-cut, and it
  belongs with the dispatch errand.
**Gap:** the two-axis report -- value state and citation state named
separately for every claim, with UNKNOWN as a first-class value on
each. VALUE_VERDICT_ABSENT and REFUSAL_UNCLASSIFIED are the first two
pieces of it.
**Ref:** L-192 (the checker and the dispatch errand); L-184 (the
active-build-path push gate); protocol v3.39 "A Check That Cannot Fail
Is Not Passing"; `patch_L192_verdict_aware_L2b.py`.

#### [L-194] Text-only assertions -- claims the scanner cannot see
<!-- L:194 status:DEFERRED upd:2026-08-15 section:A flag: rice:4/3/60/5 -->
- **The class.** A qualitative sentence in display text carries no
  number, so the scanner emits no claim for it at all. Claim detection
  in display strings is `NUMERIC_CLAIM_RE` -- a number followed by a
  recognized unit -- and a string literal becomes a scannable unit only
  if it contains one. These sentences are not uncited. They are
  invisible, which is the failure class this project treats as equal to
  uncited.
- **The instance that surfaced it, 2026-08-15.** "Unlike Earth, Mars
  lacks a stratosphere," rendered from `shell_configs.py:1256` --
  `SHELL_CONFIGS` Mars `upper_atmosphere`, key `hover_text`, the key
  `orrery_rendering.py` actually reads. GPT found it unsupported. Raised
  as Break 2 of Fable's worksheet schema review, which cited
  `mars_visualization_shells.py:518`; that is the wrong file, and the
  word stratosphere appears nowhere in that module. The claim is real,
  the citation of it was not. [verified @253bcdd]
- **Population, measured @253bcdd.** Counting display prose strings over
  120 characters -- Claude's cut, not the scanner's -- as
  total / carrying a number+unit / carrying none:
  `shell_configs.py` 143 / 92 / 51; `saturn_visualization_shells.py`
  32 / 10 / 22; `mars_visualization_shells.py` 19 / 6 / 13;
  `jupiter_visualization_shells.py` 25 / 19 / 6;
  `earth_visualization_shells.py` 28 / 27 / 1. The third column is a
  FLOOR, not the total: a string that does contain a number can still
  carry unsourced qualitative sentences beside it.
- **The half that is worse than invisible.** Where a qualitative
  sentence shares a string literal with a numeric one, the scanner
  scores the string on the number, and a `# Source:` on that unit
  covers the whole literal. Mercury's inner core reads "a very large
  metallic core, unlike Earth's which is proportionally smaller" in the
  same string as "Core radius approximately 2020 km." Source the radius
  and the comparison inherits coverage nobody checked. This is
  proximity standing in for attachment one level BELOW the comment-run
  rule L-192 settled -- inside a single string literal rather than
  across a comment run.
- **Tony's governing ruling, 2026-08-15: if the checker cannot verify a
  claim, it should not be asked to do so.** This settles Break 2 of the
  schema review directly. Field 2 keeps a number as its object; it does
  NOT generalize to "the number, OR the claim text quoted verbatim."
  Asking a responder to verdict a claim the tool cannot check produces
  a verdict the tool must then interpret, which is the interpretation
  layer L-193 exists to shrink.
- **And it does not block.** Text-only assertions wait for a future
  refactor and gate nothing in the meantime -- not L-192's schema
  re-cut, not the request builder, not the dispatch errand. Many of
  these sentences came from Gemini and their sources are not readily
  available, so this is a sourcing errand of unknown size rather than a
  scanner patch, and its size is exactly why it must not sit in front
  of work that is ready to move.
- **Avenue Tony named, not yet designed:** a visible in-text marker for
  an unsourced assertion, in the spirit of Wikipedia's "citation
  needed." The attraction is that it makes the gap legible to a READER
  rather than only to a tool. Same move as L-192's orphan report and
  the protocol's Show the Envelope: state the absence, rather than let
  silence read as coverage.
**Note:** kept separate from L-190 deliberately. L-190 is about VALUES
that render from shapes the scanner does not reach -- bare literals
inside function bodies. This is about claims that have no value at all,
which no extension of shape coverage will ever find. Same rule of
Tony's underneath ("anything rendered should be reached by the
scanner"), different mechanism, different fix.
**Note:** RICE is Claude's proposal, unratified. Effort is scored high
because the corpus is large and the sourcing may not exist to be found.
**Gap:** a future refactor decides how an unverifiable rendered claim
is marked and how its absence of provenance is reported. Deferred by
ruling, not blocked by a dependency: nothing has to finish before this
can start, and nothing waits on it.
**Ref:** L-190 (scanner reach, the VALUE form of the same rule); L-191
(display-text duplication -- the same sentence can exist in three
copies with only one live); L-192 (the schema re-cut this waits on, and
its Break 2); L-193 (verdict honesty);
`documentation/FABLE_REVIEW_worksheet_schema.md`.

#### [L-195] Citation legs -- put the authority in the Source line
<!-- L:195 status:OPEN upd:2026-08-15 section:A flag: rice:2/3/85/1 -->
- **The defect.** `# Source:`, `# Ref:` and `# Also:` do not carry
  consistent roles. In the normal case Source is the authority and the
  others are a locator and a corroboration -- `SUN_RADIUS_KM` cites IAU
  2015 Resolution B3, then Prsa et al. 2016 documenting it, then a NASA
  factsheet. In `ROCHE_LIMIT_RADII` the Source line holds a FORMULA and
  the authority (Murray & Dermott 1999, Sec. 4.6) sits in `# Ref:`.
  Same three labels, inverted roles.
- **Why it matters now.** L-192's Break 5 ruling makes field 3 verdict
  the Source line only. That rule is correct for the normal case and
  silently wrong wherever the authority is elsewhere: the row would
  read CITATION RIGHT while the actual authority went unchecked. The
  ruling is what makes this a defect rather than a style quibble.
- **Scope, measured @253bcdd.** 20 multi-leg citation blocks in the
  repo, 17 of them in `constants_new.py`. At least 9 sit in the
  dispatch corpus. Not every one is malformed -- most are the normal
  shape -- so the errand is to read 20 blocks and move the authority
  into Source where it is not already there. My scan breaks a block on
  an unlabeled continuation comment, so 20 is a floor.
- **Not a vocabulary change.** The labels stay. What is being fixed is
  which line the authority sits on, so that one rule reads the same
  thing in every block.
**Note:** RICE is Claude's proposal, unratified. Effort is low -- this
is a bounded read of 20 blocks in mostly one file.
**Gap:** the six Shape A swaps in `constants_new.py` (roughly lines
195-277), where a `# Source:` line names an event rather than an
authority. Shape A was ruled 2026-08-16; the swaps are not built. Do
this before the first dispatch that relies on the Break 5 rule.
**Note, 2026-08-17:** the continuation half of this errand is DONE
under L-196 -- the scan that made 20 a floor broke blocks on unlabeled
continuation comments, and every citation-leg continuation in the repo
is now marked, joined and ratcheted. What remains here is the authority
placement itself.
**Ref:** L-192 (Break 5, the rule this makes true); L-186 (annotation
grammar); `documentation/FABLE_REVIEW_worksheet_schema.md` item 5.

#### [L-199] Protocol length: govern the growth, not the number
<!-- L:199 status:OPEN upd:2026-08-17 section:A flag: rice:2/3/80/1 -->
- **The question, Tony 2026-08-17.** The protocol is 1021 lines against
  an earlier target of 850. It keeps growing and none of it is
  obviously disposable.
- **Measured @fb63e4b.** Preamble 38 (3.7%), Part 1 138 (13.5%), Part 2
  158 (15.5%), Part 3 gates and skills 296 (29.0%), Part 4 121 (11.8%),
  Part 5 268 (26.2%). Inside Part 5, **Version History alone is 129
  lines, 12.6% of the whole document**.
- **Length is not a reading problem.** 1021 lines is roughly 14,000
  tokens. The cost is SALIENCE, not capacity: the resident layer exists
  so the CRITICAL gates fire unprompted, and everything that is not a
  gate competes for that. This is the document-scale form of the rule
  Part 2 already states about the tiers -- if everything is critical,
  nothing is.
- **The test for what may leave is not "is it secondary".** It is
  **does this have a trigger somewhere else**. A skill fires on task
  match; the ledger is read at session start; a bare archive file has
  no trigger at all. That is why the v3.37 first cut, which moved all
  41 lessons out and left a pointer, was reversed the same day. The
  850 number came from Claude's own recommendation when context length
  genuinely constrained the work; it has outlived the condition that
  produced it and should be replaced by the test rather than re-tuned.
- **Applying the test, only one section passes.** Version History has a
  real trigger elsewhere -- the ledger appendix below is its store, and
  the protocol already says so. Quotables shapes voice, Part 4 shapes
  judgment, and the resident Lessons Archive is by construction the
  fourteen with no counterpart anywhere. Those have no trigger, but
  firing is not their job.
- **A store relationship that is currently false.** The protocol says
  the full version history lives in this ledger's appendix. The
  appendix carries v1.0 through **v3.38**; v3.39 and v3.40 exist ONLY
  in the protocol. Push those two down BEFORE trimming anything, or the
  trim deletes the only copy.
- **Also worth stating: 850 may be the wrong thing to measure.** It was
  set when the protocol was the only layer. Since v3.30 there are two,
  and the skills carry well over a thousand lines of procedure that
  used to live here. The number worth watching is what FRACTION of the
  resident document is gates, not its total.

**Proposal, three parts, none built.**
1. A short sizing section in the protocol -- roughly fifteen lines --
   carrying the trigger test, the gates-fraction measure, and a stated
   cap on resident version-history entries. It earns its lines by
   governing growth rather than adding to it; the document currently
   has no rule about itself, which is how it gained 200 lines with
   nothing objecting.
2. Copy v3.39 and v3.40 into the ledger appendix, then reduce
   v3.34-v3.39 in the protocol to a single pointer line, keeping the
   two most recent entries in full. Recovers roughly 95 lines, taking
   the protocol to about 925.
3. One line in Part 5 naming the archive file (now
   `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`). The
   file is invisible from the protocol today, which is the only real
   defect it has.

**Note: do NOT reintegrate the lessons archive.** Tony raised this on
the reasoning that nothing reads it. Checked by reading the file rather
than from memory: 27 entries, every one names where it still lives, and
all four homes that a first automated probe flagged as missing are in
fact present -- the probe was matching truncated strings. Reintegrating
would re-add 27 restatements of rules already stated where they fire,
grow the protocol by about 30 lines, and restore exactly the
duplication v3.37 removed. Nothing is stranded except the record of the
decision, and a record is supposed to sit still. The archive's own
header already sets the standard for reopening this: put a line back if
it turns out to be doing work its counterpart does not do, judged by
reading. None of the 27 met that bar on 2026-08-17.
**Note:** RICE is Claude's proposal, unratified.
**Tony-action (decide):** approve the sizing section's content before
it is written into the protocol -- it is a constitutional amendment,
not a build.
- **Tony's ruling, 2026-08-18, and it changes part 2.** The store for
  the version history is NOT this ledger's appendix. The appendix moves
  out into `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`, which is
  `LESSONS_ARCHIVE.md` renamed and now carrying two records: the
  version history as PART 1, the v3.37 lessons record verbatim as
  PART 2. Both are kept -- the lessons record is not displaced by the
  history arriving beside it. The ledger keeps a pointer.
- **As built, 2026-08-18** (`patch_L199_1`). Parts 2 and 3 of the
  proposal landed, part 1 did not.
  - The appendix repair the bullet above insisted on is satisfied
    WITHOUT copying anything: v3.39 and v3.40 are two of the three
    entries that STAY resident, so the trim never reaches them.
    v3.34-v3.38 come out of the protocol and are not copied, because
    they are already inside the appendix that became PART 1. Every
    entry lives in exactly one place.
  - The rule that keeps it that way is now stated in the protocol:
    three most recent resident, and a fourth pushes the oldest down.
    That is the stated cap part 1 asked for, arriving as one line
    rather than as a sizing section.
  - Part 3 landed too: Part 5 names the file, which is the only real
    defect the archive had.
  - The header gained an anchor and a corrected date. The repo copy
    read August 16 and the copy installed in the Claude UI read
    August 17 under the SAME version number -- two stores of one
    document, one of them hand-edited. v3.41 supersedes both.
- **Remaining, and it is part 1 alone.** A short sizing section
  carrying the trigger test and the gates-fraction measure. The cap it
  was to contain now exists; what is still missing is the reasoning
  that governs the next thing wanting to move in.
**Gap:** part 1 unbuilt. Parts 2 and 3 landed 2026-08-18.
**Ref:** v3.37 (the reversed all-lessons cut, and why an archive has no
trigger); v3.30 (the two-layer split that moved procedure into skills);
`documentation/PROJECT_INSTRUCTIONS_HISTORY.md`;
`documentation/patch_L199_1`.

#### [L-206] Worksheet return filenames carry model and session
<!-- L:206 status:OPEN upd:2026-08-18 section:A flag: rice:2/3/85/1 -->
- **The requirement, Tony 2026-08-18.** Beyond tracking, the filename
  must identify the originating MODEL and SESSION.
- **The shape, confirmed 2026-08-18.**
  `worksheet_<model>_<batch>_<YYYYMMDD>.jsonl`, e.g.
  `worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl`.
  Underscores separate fields; hyphens live INSIDE a field. Parse from
  both ends -- literal `worksheet`, then model, then the date last --
  so the batch keeps the underscores it already has.
- **Session is the date, with a trailing letter when a day repeats**
  (`_20260818b`). Not hypothetical: 2026-08-18 alone would have needed
  it.
- **The model field carries the VERSION; the annotation identity does
  not.** The scanner compares checker identity as a plain string and
  says so -- "Gemini" and "Gemini Pro" count as two checkers. Live
  annotations read bare `Claude` (43), `GPT` (52), `Gemini` (13). If
  Opus and Fable both answer a row, two legs arrive and V2 grants
  cross-checked on what may be one family's shared misreading. Version
  in the FILENAME and bare identity in the annotation keeps two Claude
  legs scoring as ONE identity -- conservative and correct -- while the
  file still records which two Claudes. No migration of 134
  annotations.
- **Two supporting pieces, unbuilt.** The request prints the EXPECTED
  return filename in its header, since the builder cannot name a return
  and the request is the only place the convention reaches the reader.
  And the checker REPORTS on names rather than refusing them: 34
  historical worksheets predate this, and a checker that refuses the
  corpus it exists to check is useless.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. Blocks nothing, but a return filed before it lands
will need renaming -- and a rename breaks every `# Resolved:` leg
pointing at it, so name the pilot's return by hand at dispatch time.
**Ref:** L-200 (the leg that cites the filename); L-186; L-192.

#### [L-209] ALFVEN_SURFACE_RADII -- origin mismatch, photosphere vs Sun centre
<!-- L:209 status:OPEN upd:2026-08-21 section:A flag: rice:3/3/85/1 -->
- **The finding, pilot run 2026-08-18.** `ALFVEN_SURFACE_RADII = 18.8`
  is an ALTITUDE above the photosphere, not a heliocentric radius.
  Both the Kasper et al. 2021 abstract (13 million km above the
  photosphere) and the NASA/APL release (8.127 million miles above the
  solar surface) measure from the surface.
- **Checkable inside the file, against a sibling.**
  `PARKER_CLOSEST_RADII = 9.86` IS heliocentric: the mission's 3.8
  million miles above the surface is 8.86 R_sun of altitude and 9.86
  from centre. So two constants in one file, describing the same
  spacecraft, use different origins and differ by exactly 1 R_sun.
- **Why this is alone rather than with the other pilot findings.** If
  the Alfven surface is drawn as a shell from Sun centre alongside
  HELIOPAUSE_RADII and PARKER_CLOSEST_RADII, the render is low by one
  solar radius and the value should be 19.8. That makes it a rendering
  defect, not a documentation defect, and it fails Mode 5 in a way no
  citation error does.
- **Confirm the dispatch before editing the leaf.** Whether the shell
  is drawn from centre is the question that decides whether this is a
  render bug or only a comment bug. Grep for consumers of the constant
  first.
- **Two further cautions from the same return, if it IS drawn as a
  sphere.** The crossing was into a low-Mach-number boundary layer
  above a pseudostreamer, not a global surface; later PSP work puts
  the Alfven surface at 10-20 R_sun, non-spherical, and expanding with
  rising solar activity.
- **Citation half.** GPT independently marked the citation PARTIAL:
  Kasper et al. 2021 does not itself print 18.8 R_sun. That figure is
  from the press release, so the row cites the paper for a number only
  the release states.
- **Confirmed, and the render WAS wrong.** `shell_configs.py` builds the
  Alfven shell as `ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU`, a sphere
  centred on the Sun, so the constant is consumed heliocentrically and
  the shell rendered one solar radius small.
- **The correction was ALREADY IN THE FILE, on lines the check could not
  see.** Two comment lines under the constant read "HELIOCENTRIC: from
  Sun center ... Kasper's paper says 18.4-19.7 R_sun from center." A
  previous session found the distinction, wrote the paper's own range
  down, and left the value at 18.8 anyway. See L-214: those lines rode
  on a bare `Note:` and an invented `HELIOCENTRIC:` label, neither of
  which the request builder reads, so no responder ever saw them.
- **Resolved at 19.7** (Tony, 2026-08-19), sourced to the PRL body text
  rather than to the press release. Two independent routes agree: the
  paper gives the sub-Alfvenic interval as 19.7 to 18.4 solar radii from
  the center of the Sun, and converting the release's 18.8 R_sun of
  altitude gives 19.8. Taking the paper drops the release as an
  authority, which also answers GPT's separate PARTIAL: the paper does
  not itself print 18.8.
- **The two `# Cross-checked:` legs dated 2026-08-02 were stripped with
  the value.** They certified 18.8. A check of the old value is not a
  check of the new one -- the exact ride-along the skill warns about.
  No new leg was written from the pilot: Claude returned APPROX and GPT
  PARTIAL, neither of which earns one, and Gemini's CONFIRMED rests on
  a note reading "Recollection of the Parker Solar Probe 8th encounter
  results."
- **As built** (`patch_L209_2_alfven_migration.py`). The value and the
  whole explanation live in `constants_new.py`; every display site now
  READS the constant rather than holding a copy. 12 typed instances
  across four modules became imports: 8 interpolations in
  `solar_visualization_shells.py`, 1 in `comet_visualization_shells.py`,
  1 in `info_dictionary.py` (which gained its first import), and 2 sites
  that cannot read a value -- a docstring and a `# Source:` comment --
  had the figure dropped and now point at the constant. The derived
  0.087 AU and 13 million km figures are computed from the constant, so
  they moved with it.
- **Found and NOT touched, deliberately.** The same display strings hold
  other typed constants -- `ROCHE_LIMIT_RADII` as "3.45 R_sun", the
  streamer belt as both "4-6" and "6.0". Migrating them is L-181 and
  L-191, not this item.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** one open, one closed. Read item 2; item 1 is kept as record.
1. **CITATION DEBT -- DISCHARGED 2026-08-21.** DeForest, Howard &
   McComas (2014), ApJ 787:124 was removed from `STREAMER_BELT_RADII`
   on 2026-08-20 at `e1c64dc9` -- its 6 R_sun is an inbound-wave
   DETECTION THRESHOLD, not a streamer extent -- and its own result
   belongs to this row. The removal ran; the rehoming did not, and this
   Gap said "none" for a day because it was written before the debt
   existed. `patch_L209_4_deforest_rehomed.py` closed it: the paper was
   read at source, and `# Also+:` legs on `ALFVEN_SURFACE_RADII` now
   carry it as a 2014 remote LOWER BOUND, superseded by Kasper's 2021
   in-situ crossing and consistent with it. Nothing further is owed.
   **The figure changed on the way, and this is the part to remember.**
   This Gap first stated the bound as 17 R_sun in the streamer belt and
   12.5 over the poles. The published paper says 15 and 12, in its
   abstract, its Section 5 and its Section 6. The 12.5/17 pair is the
   arXiv ABSTRACT METADATA at arxiv.org/abs/1404.3235, which does not
   match the accepted manuscript arXiv itself serves as the PDF; NASA
   ADS and Cranmer et al. 2016 (ApJ 828:66) both carry 12 and 15. Two
   earlier reads reported 17 because both quoted that same listing
   page. Agreement between two reads of one wrong page is not
   verification. Do NOT restore 17 anywhere.
   **The rule it tested.** This row is why the discharge needed a real
   read rather than the removal worksheet: a removal needs only the
   ABSENCE of support, a citation needs its PRESENCE. Had the worksheet
   been reused as the leg, 17 would now be in the code.
2. **MODE 5, unchanged and still outstanding.** The Alfven shell should
   render one solar radius larger than before, still nested inside the
   50 R_sun outer corona. Tony's eyes on a plot, not a build.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Part 4;
`documentation/worksheets/`
`worksheet_claude-opus-5_pilot_constants_new_20260818.jsonl` R12;
`documentation/worksheets/`
`worksheet_gemini-3-1-pro_reconciliation_sources_20260820.md` item 4
(the checkable, unchecked claim); L-210 (the row DeForest was removed
from, and the same staleness class corrected one item over on
2026-08-21); L-214 (the builder gap this exposed); L-181 and L-191 (the
remaining shadow constants); L-207 (the run that produced it); L-221
(misapplied against this row before the dates were checked -- it
governs a session document contradicting a settled decision, not a
ledger field that predates the event it is silent about).

#### [L-216] Gallery swap fails under a filesystem lock (OneDrive)
<!-- L:216 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/2 -->
- **2026-08-19: the nightly run wiped the served tree.** GitHub Desktop
  showed 56 deletions in the gallery repo and zero additions.
  `data/solar-system/` was absent while BOTH halves of the generation
  survived: `solar-system.prev` (the previous generation) and
  `.staging_solar-system_20260819T214723Z` (the new one). Nothing was
  committed and nothing was lost.
- **The zero-additions reading was an artifact.** The gallery
  `.gitignore` hides `data/.staging_*/`, `data/solar-system.prev/` and
  `data/solar-system.quarantine_*/`, so a half-completed swap looks
  exactly like total loss.
- **The build was clean; only the swap failed.** Run record
  `20260819T214723Z.json`: `structural_validation: pass`,
  `guard_warnings: []`, finished 13.8 s after start. Good data that
  never landed -- not the guard catching a bad build.
- **Reproduced the same evening, and it named itself.** A manual re-run
  printed: `[RECOVER] could not remove retained data\solar-system.prev
  ([WinError 5] Access is denied: data\solar-system.prev\raw\elements);
  swap will quarantine it`. The lock is real and persistent. The repo
  lives under `C:\Users\tonyq\OneDrive\...`, and a sync engine holding
  a handle on a directory is what makes a rename fail.
- **WHICH rename it catches is the whole difference.** The re-run hit
  the CLEANUP rmtree, which the code handles by design -- quarantine
  and carry on -- and the swap completed. The failing run hit
  `staging -> live`, which has no in-run recovery and leaves the live
  directory missing. Same cause, different victim.
- **The pile was the signal all along.** ~30 `solar-system.quarantine_*`
  directories run back to 2026-07-21, one per night. Each is a run
  where the retained `.prev` could not be removed. The mechanism has
  been printing every night for a month and reading as normal, because
  the builder is built to survive it.
- **Recovery, and it is the operational rule (Tony, 2026-08-19):** for
  a cache hiccup, DISCARD the deletions in GitHub Desktop and RE-RUN.
  Discard restores the live tree from HEAD byte for byte; the re-run
  builds a fresh generation. Three conditions make it safe and they
  should travel with the rule: the live tree is committed, the swap is
  all-or-nothing so a failure leaves a COMPLETE `.prev` or staging and
  never a mixed one, and nothing reaches the remote until Tony commits.
  Running with `--commit` would break the third.
- **The visibility gap, and it comes BEFORE the swap fix.** The run
  record is written INSIDE the generation, so a run whose swap fails
  strands its own record in a directory `.gitignore` hides. The
  committed history will show the 18th, the 19th 23:10 run, and no sign
  that a run in between lost its data. The swap OUTCOME needs recording
  outside the generation, or every recurrence costs another evening of
  inference. Same Visibility Convention shape as L-214, one layer out.
- **Then the cause.** Retry the renames with backoff if the lock is
  transient at the moment of the swap, or move the repo off OneDrive if
  it is not. WinError 5 on the cleanup proves persistence at run START;
  it does not prove the swap window is equally exposed.
- **Tony-action (do):** the operational rule above belongs in
  `gallery-cache-builder`, which would be 1.4. NOT bumped tonight:
  `ledger-and-session-records` went to 1.7 today and that reinstall is
  unverified from inside this session. Discharge that first, then bump
  this one. Same pattern as the dispatch-hygiene rule on 2026-08-19.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unmeasured -- whether the `staging -> live` rename is exposed
to the same lock as the cleanup, or was unlucky once. One data point.
**Ref:** `tools/gallery_cache_builder.py` `atomic_swap_dir` (~1176),
`recover_incomplete_swap` (~1223), `_sweep_siblings` (~1241) in the
gallery repo; run records `20260819T214723Z.json` (failed) and
`20260819T231042Z.json` (recovered); gallery at `8a4aa41`; L-098 (the
builder); L-214 (the same visibility shape).

#### [L-215] Ledger cleanup by topic, not by age
<!-- L:215 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/80/2 -->
- **Tony, 2026-08-19:** "Can we do a cleanup run to move the items that
  touch on our current work? This would reduce the effort factor and
  increase the confidence factor, the reach and impact by coordination."
  Replaces a by-age triage Claude had recommended.
- **The rule underneath it.** RICE Effort is not a property of an item;
  it is a property of an item GIVEN what else is open. Scoring each one
  alone is what produces a tail, and a score-ordered board cannot
  distinguish "correctly deprioritized" from "dropped."
- **Baseline, measured 2026-08-19 at `434a712b`.** 107 open items. 52
  score below RICE 2.0; 54 are both below 3.0 and untouched for more
  than 30 days. Oldest is L-053 at 73 days. Nothing exceeds 90 days, so
  the tail is a stratum rather than a swamp.
- **The mechanism is a STEP, not an event.** When a job is scheduled,
  sweep the open ledger for items whose FILES the job already opens and
  clear them in the same patch.
- **Cluster by files touched, NOT by keyword.** A keyword sweep for the
  worksheet-builder topic returned 36 items including a comet-tail
  animation, the food-insecurity track and a ring-colour audit -- shared
  vocabulary, unrelated work. The file list a job already holds is the
  version that survives being run twice.
- **First run, two findings, both of which are the argument.** L-028 was
  ALREADY DONE and still counted as debt at 69 days (now closed). And a
  ruled ASCII violation sat in `info_dictionary.py`, a file this session
  had already fingerprinted, opened and edited -- the number was printed
  by the patch's own encoding report and read past, because no ledger
  item gave it meaning.
- **A correction, recorded.** Claude attributed those ASCII bytes to
  L-187 in conversation. L-187 is `info_dictionary` NUMERIC-OVERLAP
  enumeration and has nothing to do with encoding. The violation had no
  ledger item at all, which is a worse finding than a stale one.
- **Tony-action (decide):** two non-ASCII bytes remain in
  `info_dictionary.py` after this sweep, both the `s`-acute in the name
  of Kacper Wierzchos, the Polish astronomer who discovered C/2024 E1.
  Transliterating a person's name is not a mechanical fix and reads
  intent, so it stayed out of scope. Options: keep the diacritic and
  carry a named exception, or write the ASCII spelling and note the
  original in the same string.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** the 54-item tail is measured but unswept. No sweep has run
except the L-214-adjacent one that produced the findings above.
**Ref:** L-191 and L-181 (the migration that will inflate Tier-1 counts);
L-028 (closed by the first sweep); L-187; `ledger-and-session-records`
v1.7, which carries the convention.

#### [L-210] Pilot citation findings -- four rows in constants_new.py
<!-- L:210 status:OPEN upd:2026-08-21 section:A flag: rice:3/3/80/2 -->
- **Grouped on purpose.** Four findings, same file, same shape of
  work: the value is defensible and the authority attached to it is
  not. One pass, one patch. The rendering defect from the same run is
  L-209 and is deliberately NOT here.
- **`STREAMER_BELT_RADII` -- CLAIM WITHDRAWN 2026-08-20. Row resolved
  as a declared assumption.** This bullet used to say the row cited its
  paper INVERTED -- that DeForest's 6 R_sun was the paper's floor being
  used as a ceiling. That was a session reading written down as a
  finding, and an independent nine-source blind read on 2026-08-20
  found otherwise. DeForest, Howard & McComas 2014 uses 6 R_sun as the
  threshold at which inbound wave motion first became DETECTABLE, which
  is neither a floor nor a ceiling on streamer extent; its actual
  streamer-belt result is an Alfven surface at 17 R_sun or more, and
  that result belongs to L-209. Golub & Pasachoff, asked the same
  question, bound coronal structure loosely at 5-10 R_sun and state no
  4-6 R_sun streamer range at all. So the range in the code was sourced
  to nothing, both citations were removed, and the range was withdrawn.
  Reads two and three then found why nobody could answer it: the
  quantity is not single-valued. Closed helmets reach no higher than
  2-4 R_sun while stalks and boundaries run to roughly 2-10, so 6.0
  sits above the one and inside the other and represents neither.
  **Tony's ruling:** hold 6.0 as a VISUALIZATION ASSUMPTION carrying no
  Source leg, and let the hover text explain the two-part reality. The
  withdrawn wording is left visible above rather than quietly restated,
  for the reason the master plan gives for doing the same: a wrong
  claim in a stored document outlives the conversation it came from,
  because the next reader has nothing else to check it against.
- **`EARTH_EQUATORIAL_RADIUS_KM` -- Shape A swap, with its own
  template one row below.** IAU 2015 B3 states 6378.1; the third
  decimal comes from IERS/WGS84, named in a `# Note:` but not on the
  Source line. All three legs flagged it, which is the prediction in
  `PILOT_EXPECTED_DISPOSITIONS_20260817.md` confirmed exactly. The fix
  is to make this row look like `EARTH_POLAR_RADIUS_KM` directly
  below, which already cites IERS and notes separately what B3 rounds
  to.
- **`BENNU_RADIUS_KM` -- superseded value AND a misattributed
  confirmation.** 0.246 is the pre-encounter Nolan radar figure;
  OSIRIS-REx gives 490.06 +/- 0.16 m mean diameter, so 0.245. Beyond
  the digit: the comment attributes "mean radius 246 +/- 10 m, V =
  0.062 km^3" to OSIRIS-REx OLA, and those are the radar numbers
  restated. OLA and SPC give 0.0615 and 0.061354 km^3 to about 0.1
  percent. The row reads as though the mission independently produced
  the figure it was confirming.
- **`HAUMEA_RADIUS_KM` -- trace, do not simply correct.** 715 km is
  the volume-equivalent radius of the Lockwood et al. 2014 model,
  reproduced to the digit, but that model was overturned by the 2017
  stellar occultation -- the only direct size measurement -- which
  puts the mean radius near 798 km. Separately, the axes in the
  comment (1050 x 840 x 537 km) match NO published shape model:
  Lockwood gives 960 x 770 x 495, Ortiz gives 1161 x 852 x 513. Yet
  the comment's geometric mean of 779.5 computes correctly FROM those
  axes. Somebody did valid arithmetic on unsourced numbers, which
  leaves no arithmetic trace and would be equally invisible elsewhere
  in the corpus. Find where the axes came from before editing.
- **`ARROKOTH_RADIUS_KM` -- watch flag, not another one-time fix.**
  A newer New Horizons shape model gives ~9.95 km against 9.1, a 9
  percent change moving OPPOSITE to the 2026-04-15 correction the
  comment already records. This row has now been wrong in both
  directions. Attribution also drifts: the figure 3166 km^3 and the
  phrase about a 9.1 km equivalent sphere appear verbatim in Amarante
  & Winter 2022 working from Spencer et al. 2020, not in the cited
  Keane et al. 2022.
**Resolved 2026-08-20 -- four of the five rows above.** Tony ruled per
row. The changes landed in `constants_new.py`, and each of the four
carries a `# Resolved:` annotation naming this handle.
[verified @d2e6457a -- read at HEAD, not carried from a session record]
- `EARTH_EQUATORIAL_RADIUS_KM` 6378.137 -> 6378.1366. Source moved from
  IAU B3 to IERS Conventions (2010), with B3's rounding kept as the
  aside, matching `EARTH_POLAR_RADIUS_KM` directly below it.
- `STREAMER_BELT_RADII` HELD at 6.0. Both citations removed, the 4-6
  R_sun range withdrawn, the row recorded as an explicit assumption.
- `BENNU_RADIUS_KM` 0.246 -> 0.24503, Barnouin et al. 2019. The
  `Source+:` line that credited OSIRIS-REx OLA with Nolan's restated
  radar figures is gone, so the row no longer reads as independent
  confirmation it never received.
- `HAUMEA_RADIUS_KM` 715 -> 798, the Ortiz et al. 2017 occultation. The
  unsourced axes are removed and the volume-equivalent radius is now
  marked DERIVED from the published semi-axes rather than quoted.
Patches `patch_L210_1` through `_5`, archived in `documentation/`, at
`762aa5dd` and `e1c64dc9`. `_5` is the one worth remembering: the
withdrawn "4-6 R_sun" claim was still rendering at ten sites across two
shell modules after the constant had been fixed -- the parallel-pipeline
failure in its plainest form, the constant repaired and the text that
reaches the user not.
**Note:** RICE is Claude's proposal, unratified -- and it was NOT
re-scored when the four rows closed. The 3.6 in the index still prices
the original five-row item rather than the ARROKOTH remainder.
**Gap:** `ARROKOTH_RADIUS_KM` only. It is a WATCH flag, not a pending
fix: the row is not known to be wrong, and a newer New Horizons shape
model moving 9 percent the OTHER way from the 2026-04-15 correction is
a reason to look rather than a reason to edit. The attribution drift is
the firmer half -- the volume figure and the equivalent-sphere phrasing
appear in Amarante & Winter 2022, not in the cited Keane et al. 2022.
Needs a source read before any value moves. **Tony-action (decide):**
dispatch this row, or leave it watched.
**Ref:** `documentation/PILOT_CONVERGENCE_20260819.md` Parts 3-4;
`documentation/HANDOFF_20260820_reconciliation_closed.md` (the
decisions, and part 6 on what the streamer row cost);
`documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` (carries the same
correction); L-195 (Shape A swaps); L-209 (the rendering half of the
same run, and the row DeForest's result is owed to); L-221 (the ledger
outranks a session document about a settled decision -- this block was
the counter-case, stale where the session documents were current).

#### [L-211] UNKNOWN -- the verdict for "checked, could not determine"
<!-- L:211 status:OPEN upd:2026-08-19 section:A flag: rice:3/3/85/2 -->
- **The trigger fired, and it was pre-registered.**
  `documentation/DESIGN_20260818_unknown_verdict.md` set the threshold
  at two returned rows where a responder reached for `unverified`
  beside a note describing a search actually attempted and failed.
  Seven arrived on the first run: Gemini 1, GPT 3, Claude 3. Build it.
- **The design is settled; only the build is open.** Four rulings from
  the design note, not to be re-litigated: it routes CONVERSATION and
  never SEND BACK, since sending it back asks the same responder to
  repeat a search that already failed; it REQUIRES a non-empty note,
  and an UNKNOWN with an empty note routes SEND BACK as incomplete,
  which is a presence check rather than prose-reading and inverts the
  incentive so UNKNOWN costs more than a real answer; it earns no
  rung; and two or more INDEPENDENT UNKNOWNs on one key stop being
  about the responders and become a removal candidate under the
  Fetched-vs-Recalled third branch.
- **What the run added that the design did not have.** Claude's leg
  states the gap in the vocabulary's own terms -- `unverified` reads
  as NO ANSWER GIVEN when what happened was AN ANSWER ATTEMPTED AND
  NOT REACHED -- and then supplies the pattern: all three of its cases
  are PRINT BOOKS. Carroll & Ostlie, Golub & Pasachoff, Murray &
  Dermott. GPT hit two of the same three. The missing verdict is not
  scattered; it concentrates wherever the authority is a book no
  responder can open.
- **Which reframes the follow-on, and this is the larger finding.**
  Three constants in this slice rest on print authorities that no
  model-mediated check can ever reach. Those rows need a human with
  library access, not a better token. UNKNOWN makes the condition
  VISIBLE and countable; it does not resolve it.
- **Counting UNKNOWNs per key is cheap** because L-207 already groups
  responder legs under one key in `citation_prompt_rows`. Extending
  that count is the "extend a boundary before adding a path" shape.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** unbuilt. The vocabulary lives in `VERDICT_TOKENS`, so the
request builder and the citation prompt both pick it up for free once
the token exists.
**Ref:** `documentation/DESIGN_20260818_unknown_verdict.md`;
`documentation/PILOT_CONVERGENCE_20260819.md` Part 5; L-207.

#### [L-218] 22 Cross-checked lines attach to no unit
<!-- L:218 status:OPEN upd:2026-08-19 section:A flag: rice:2/3/70/2 -->
- **Announced by the L-214 measurement, 2026-08-19, and parked there.**
  `worksheet_checker.collect_claims` returns an `unreached` list
  alongside its claims. At `97c52017` that list holds 22
  `# Cross-checked:` lines that match the scanner's pattern but attach
  to no scored unit. [verified @97c52017]
- **Why it was parked and why that is not good enough.** All 22 are
  record legs, so none of them could enter the L-214 defect count, and
  the measurement said so. Fable's reading: "It reads like a finding
  living in a footnote; it deserves its own handle and a look." That is
  correct -- an orphaned record annotation is either expected structure
  or a second latent defect, and nobody has established which.
- **What it would mean if it is a defect.** A `# Cross-checked:` line
  that attaches to no unit is a review verdict that landed in the code
  and is invisible to the tooling that reads verdicts. That is the same
  shape as L-214 one layer over: material written down correctly and
  read by nothing.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** list the 22, classify each as expected or defective, and
decide from the classification rather than in advance.
**Ref:** `worksheet_checker.py` `collect_claims`;
`documentation/L214_MEASUREMENT_20260819.md` (where the number is
announced); L-214.

#### [L-219] Patch-script naming cannot express a cross-handle run order
<!-- L:219 status:OPEN upd:2026-08-19 section:A flag: rice:2/2/85/1 -->
- **Recorded 2026-08-19, from the 2026-08-19 handoff's own error log,
  where it was named as a real gap and explicitly noted as not yet
  having an item.** Two patches were delivered with a cross-handle
  dependency -- `patch_L209_2` had to run AFTER `patch_L213_3` -- but
  the `safe-file-editing` sequence number is scoped to its own ledger
  handle, so alphabetical sort order contradicted run order. Only the
  prose carried the real sequence.
- **What saved it, and why that is not enough.** The base fingerprint
  guard caught the out-of-order run and wrote nothing, which is the
  guard working. But an abort tells you the order was wrong without
  telling you what the right order was, and the convention's own
  promise is that "sort order is then run order."
- **The convention as written cannot express this.** `patch_<handle>_
  <n>_<what>.py` numbers within one handle. Nothing in the filename
  ranks two handles against each other. Options not yet weighed: a
  session-scoped prefix ahead of the handle; a single script spanning
  both handles when the dependency is real; or accepting the limit and
  requiring the dependency in the docstring of the LATER script, where
  the person about to run it will see it.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** pick one of the three and write it into `safe-file-editing`,
which would be 1.7 -- 1.5 and 1.6 are taken by L-220.
**Tony-action (decide):** which option.
**Ref:** `skills/safe-file-editing/SKILL.md` "Naming and Archiving a
Patch Script"; `documentation/patch_L209_2_alfven_migration.py` and
`documentation/patch_L213_3_cache_line_and_close.py` (the pair that
exposed it); HANDOFF_20260819_alfven_and_the_swap.md, error 4.

#### [L-224] Streamer belt: one warped band, not a sphere
<!-- L:224 status:OPEN upd:2026-08-22 section:A flag: rice:3/3/85/2 -->
- **What is on screen now, and why it is wrong twice.**
  `create_sun_streamer_belt_shell` draws a full sphere of points at
  `STREAMER_BELT_RADII = 6.0`. Helmet streamers form only over the
  magnetic neutral line; the poles carry coronal holes instead. So the
  sphere asserts helmets exactly where there are none. And 6.0 is not
  a boundary of anything: L-210 withdrew its 4-6 R_sun range as
  unsourced and held 6.0 as a declared drawing choice above the closed
  structure and inside the open one.
- **The physical split, from Suess & Nerney (2004), Adv. Space Res.
  33:668-675, bibcode 2004AdSpR..33..668S.** Streamers reach many
  solar radii but the CLOSED-field helmet reaches no higher than 2-4.
  Above the cusp there is a stalk -- a thin sheet along the current
  sheet with no outer edge, thinning into the slow solar wind. Source
  record: `documentation/SOURCE_suess_nerney_2004_helmet_extent_
  20260821.md`. The figure is stated there as established background
  in a modelling paper, NOT measured by it.
- **DECISION -- one trace, not two.** Both halves are band-shaped, so
  this is one object whose character changes with radius, not two
  shells. One legend entry. Splitting the legend would undo the point.
- **DECISION -- the silhouette carries the physics.** Wide and dense
  at the base along the neutral line; pinching to a minimum width at
  the cusp; thin above it. The pinch is where the loops open, which is
  a claim a paper supports, unlike "where the belt ends." It is also
  the eclipse silhouette, so it reads as familiar and is correct.
- **DECISION -- cusp at 4.0 R_sun**, the top of the stated 2-4 range.
  `STREAMER_BELT_RADII = 6.0` becomes `HELMET_CUSP_RADII = 4.0`. The
  rename is Tony's call and load-bearing: a constant named for the
  belt while holding the helmet cusp is the same name-meaning drift
  that produced the citation failure. Eight live consumers across six
  modules -- `shell_configs.py`, `comet_visualization_shells.py` and
  its hover text, `solar_visualization_shells.py`,
  `test_constants_provenance.py`. MEASURED, not assumed: the suite's
  ordering assertion holds at 4.0 (3.0 < 3.45 < 4.0 < 19.7 < 50), all
  15 tests pass with the value substituted.
- **DECISION -- the stalk attenuates and never terminates.** Opacity
  AND point density both fall with radius; the outer edge dissolves.
  This is the one non-negotiable. DeForest's 15 R_sun is the
  coronagraph's FIELD OF VIEW, not an extent, so drawing an edge there
  would repeat the withdrawn 4-6 range in pixels. Points generate to
  roughly 20 R_sun with alpha already at zero before the array ends,
  so the terminus exists in code and never on screen.
- **DECISION -- it dissolves across the Alfven surface.** 19.7 R_sun
  (L-209) is the one real boundary out there. The stalk is seen losing
  definition as it crosses from corona into wind, which makes the
  Alfven shell mean something instead of hanging alone. Hover carries
  what happens next: it does not end, it becomes the heliospheric
  current sheet and runs to the heliopause.
- **DECISION -- warp: one configuration near solar minimum**, with the
  solar-cycle sweep explained in hover rather than drawn. The swept
  envelope is the more conservative claim but smears the skirt into a
  torus that teaches nothing, and the skirt's shape is the thing that
  teaches.
- **DECISION -- the boundary is drawn, its meaning is labelled.** Two
  claims ride together and they are not the same kind. That a sharp
  brightness boundary exists is a coronagraph OBSERVATION and needs no
  further source. What it divides is an INTERPRETATION -- Suess &
  Nerney state it is reasonable to ASSUME the boundary separates fast
  coronal-hole wind from slow, and slow-wind origin is unsettled in
  the field. So draw the edge; let hover attribute the flow-regime
  reading to them as a reading. Uncertainty stays first-class.
- **DECISION -- legend renamed to "Sun: Streamer Belt."** Drop
  "(Visible Corona)": the visible corona is broader than the belt and
  separating them is the point. The legendgroup is a key in
  `shell_configs.py`, the checkbox and the tooltip, so it ripples --
  but through files this work opens anyway.
- **Where the generator goes.** `planet_visualization_utilities.py`,
  beside `create_magnetosphere_shape` and `create_bow_shock_shape`,
  same signature shape: params dict in, body-frame `(x, y, z)` out,
  caller places it. The bow-shock generator was extracted in June 2026
  from four duplicated inline copies precisely so shaped geometry has
  one home; a one-off in the shells module would undo that.
- **Mechanism note.** Plotly's `marker.opacity` is scalar, but
  `marker.color` and `marker.size` both take per-point arrays, so
  radial fade, size taper and density thinning all fit one trace and
  one legend entry.
- **Already true in the hover text, which is ahead of the picture.**
  The current hover already cites Suess & Nerney for 2-4 R_sun and
  already says the eclipse edge divides two flow regimes rather than
  plasma from vacuum. The words describe the band. Only the geometry
  is still a sphere.
**Note:** RICE is Claude's proposal, unratified. Confidence 85 rather
than higher because the fade PROFILE is unsettled -- linear will
probably read as a smear and something steeper as a stalk. Build it
adjustable and let Mode 5 pick; that is the render's call, not a
design one.
**Gap:** build it. The design is settled and sourced; nothing is
blocked and no further source read is owed. Two things want the render
rather than a decision: the fade curve, and whether the cusp pinch
reads at all at 4.0 against `INNER_CORONA_RADII` at 3.0 and
`ROCHE_LIMIT_RADII` at 3.45. Marker separation, if needed, is angular
and never radial.
**Ref:** `solar_visualization_shells.py::create_sun_streamer_belt_
shell`; `constants_new.py::STREAMER_BELT_RADII`;
`planet_visualization_utilities.py::create_magnetosphere_shape` and
`create_bow_shock_shape` (the pattern to follow);
`documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md`;
L-210 (the withdrawn range and the held 6.0 this replaces); L-209 (the
Alfven surface it dissolves across); L-221 (the ruling that sequenced
it); `orrery-coding-conventions` (single info marker, marker
separation for near-equal radii, hover AU convention).

#### [L-225] Migrate the comet shell constants into `constants_new.py`, then dispatch
<!-- L:225 status:DEFERRED upd:2026-08-23 section:A flag: rice:2/3/80/2 -->
- **Opened 2026-08-23, and late.** The design note of 2026-08-22 cites
  L-225 four times and the session queue carried it as
  deferred-with-shape-settled, but no ledger entry existed -- the
  highest handle was L-224. Surfaced by the v19 full-document sweep.
  Recorded here rather than quietly created, because "capture on first
  mention" exists precisely so a handle cannot be in circulation while
  the ledger has never heard of it.
- **What.** `MAPS_DISINTEGRATION_RADII` and its siblings live in
  `comet_visualization_shells.py`, which is outside the tree
  `worksheet_request_builder` reaches. A constant the builder cannot
  see cannot be put in a worksheet, so it cannot be dispatched, so it
  can never be cleared -- it is invisible to the loop rather than
  merely unscored. Migrate them into `constants_new.py`, where the
  builder already reaches, and only then dispatch.
- **This is the No Shadow Constants rule [CRITICAL] applied to a
  specific file**, not a new decision. The migration is the work; the
  dispatch is the follow-on.
- **`patch_L225_1_dispatch_request.py` is WITHDRAWN. Do not run it.**
  It dispatched against the constants in their current home and so
  would have asked for verdicts on rows that cannot be written back.
  Recorded here because a withdrawn script is exactly the kind of fact
  that resurfaces from a stale copy of a design note.
- **Part A must go out blind.** The dispatch carries a Claude proposal,
  so it splits into two physical dispatches under the Two-Dispatch Rule
  [CRITICAL] (`provenance-discipline` 2.6, section 2.6): Part A sent
  alone, the answer collected, then Part B. Sending them together lets
  the proposal contaminate the answer, which is a check that cannot
  fail. The questions themselves are in the design note, Section 4.
- **Note:** RICE 2/3/80/2 -> 2.4 is Claude's proposed score, not a
  ruling. Reach 2 (one shell family), Impact 3 (an unmigrated constant
  is invisible to the builder, not merely unscored), Confidence 80
  (shape settled, dispatch outcome not), Effort 2 (mechanical migration
  plus a known loop). **Tony-action (decide):** confirm or redirect,
  then re-run `ledger_index.py`.
- **Gap:** the migration is not written. Deferred deliberately -- the
  braid puts L-154 and Artifact 2's thirty-number slice ahead of it,
  and these constants are not in Artifact 2.
- **Ref:** `comet_visualization_shells.py`; `constants_new.py`;
  `worksheet_request_builder`;
  `documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`
  Section 4; `provenance-discipline` 2.6; L-221 (sequencing authority);
  L-224 (the session that surfaced it).

#### [L-226] safe-file-editing 1.8 -- encoding gate covers prose; corrections do not travel
<!-- L:226 status:OPEN upd:2026-08-23 section:A flag: rice:3/3/90/1 -->
- **Two rulings by Tony on 2026-08-23, both from the v19 master plan
  session.** Recorded here because a skill revision is a ledger entry.
- **1. The Encoding Gate now says PROSE.** It read "ASCII only in
  delivered code." `patch_L221_2` found 22 PRIME and one DOUBLE PRIME
  in the master plan, reported them, and declined to sweep them on the
  grounds that the gate was scoped to code. All three Fix In Passing
  conditions held. Tony: a patch already holding a file open fixes
  incidental non-ASCII. The sharper point is that Stamp What You
  Change ALREADY said markdown is not an exception -- so the skill's
  two halves disagreed and the reader followed the narrower one.
  Swept in `patch_L221_3`; both master plan documents are now pure
  ASCII.
- **2. New section: The Correction Does Not Travel.** Scoped one level
  out from Stamp What You Change -- that governs the file the patch is
  editing, this governs the other files quoting what it changed.
  Founding case: `constants_new.py` read 15 R_sun from 2026-08-22
  (L-209, DeForest corrected at source);
  `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` still said 17 the next day,
  inside the paragraph written to correct an EARLIER wrong claim about
  the same row. The same file named `STREAMER_BELT_RADII` after L-224
  renamed it, and called L-214 unbuilt two days after it closed.
  Three instances, one file, one cause: the provenance machinery
  watches the code and nothing watched the documents describing it.
- **Note:** RICE 3/3/90/1 -> 8.1 is Claude's proposed score. Reach 3
  (every future patch), Impact 3 (a wrong document outlives a wrong
  constant because nothing surfaces it), Confidence 90 (the rulings
  are Tony's and the founding cases are measured), Effort 1 (the
  skill edit is written). **Tony-action (decide):** confirm or
  redirect, then re-run `ledger_index.py`.
- **Tony-action (do):** run `skills_index.py`, then reinstall
  safe-file-editing at Settings > Skills, then commit SKILL.md, this
  ledger and PROJECT_INSTRUCTIONS.md in ONE commit. A version bump is
  not done until the manifest agrees.
- **Gap:** the reinstall cannot be verified from inside the session
  that makes it. The NEXT session confirms its loaded copy reads 1.8
  before doing file-editing work. This session loaded 1.7, correctly
  at the time.
- **Ref:** `skills/safe-file-editing/SKILL.md` v1.8;
  `documentation/HANDOFF_20260823_braid_and_v19.md`; L-209 (the
  DeForest figure); L-214, L-224 (the other two stale claims);
  L-220 (Stamp What You Change); L-223 (A Paste Is An Unverified
  Transfer).

#### [L-227] Streamer band hover rendered as one 378-character line
<!-- L:227 status:OPEN upd:2026-08-23 section:A flag: rice:2/2/95/1 -->
- **Found by Mode 5 on 2026-08-23**, hovering the streamer band during
  the L-224 acceptance pass. The tooltip ran off the viewport.
- **Measured as rendered:** `band_hover` had EIGHT segments, longest
  378 characters, six over 98. `streamer_belt_info`, forty lines up in
  the same file, tops out at 98. After the fix: 29 segments, longest
  63, none over 98.
- **Cause.** The string was written as implicitly-concatenated literals
  wrapped at ~72 characters FOR SOURCE READABILITY, with `<br><br>`
  only between paragraphs. In this file the source wrap and the
  rendered wrap are one act, because each older line carries its own
  `<br>`. L-224 copied the visual habit without the mechanism, so the
  source looked correctly wrapped and the output was one long run.
- **Nothing but a person catches this.** No checker reads rendered
  hover width; the module compiles and the trace builds either way.
  Third demonstration this month that the render is the gate.
- **A RE-FLOW IS NOT COSMETIC IN THIS PROJECT** (learned 2026-08-23,
  after this item shipped). The provenance scanner decides whether a
  claim is cited by how many LINES away the nearest `# Source:`
  comment is. Breaking one long line into six moved a computed figure
  past that window, and the tree count went 292 -> 294 on a change
  that altered no wording at all. Fixed under L-229. The general
  form: when line positions move, provenance state can move with
  them, so re-run the scanner after any re-flow and read the delta.
- **Breaks only, no wording changed** -- proven mechanically, not
  asserted: strip every `<br>`, collapse whitespace, compare old to
  new, byte-identical. The patch re-ran that comparison as a self-check
  so it could refuse if a word had moved.
- **Convention recorded:** `orrery-coding-conventions` 1.5, Hover Line
  Width Is a Convention, Not an Accident. Tony's ruling: this recurs
  from time to time rather than constantly, which is the kind of thing
  a person forgets and a written convention does not.
- **Note:** RICE 2/2/95/1 -> 3.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
- **Tony-action (do):** run `skills_index.py`, reinstall
  orrery-coding-conventions at Settings > Skills, and hover the band
  once more to confirm it wraps.
- **Ref:** `solar_visualization_shells.py::create_sun_streamer_band_shell`;
  `skills/orrery-coding-conventions/SKILL.md` v1.5; L-224 (the build
  that introduced it); L-191 (the `<br>`-in-tooltip sweep, separate).

#### [L-228] Alfven surface latitude ranges: source them or omit them
<!-- L:228 status:OPEN upd:2026-08-23 section:A flag:Tony rice:2/3/60/2 -->
- **Surfaced 2026-08-23** while reading the hover strings for L-227.
- **THE DRAWN VALUE IS NOT AT ISSUE.** `ALFVEN_SURFACE_RADII` is
  interpolated into every hover that quotes it, including the derived
  million-km figure, and carries a `# Source+:` leg saying so (L-209).
  When it moved 18.8 -> 19.7 the hovers followed by construction. No
  shadow constant. This item is about PROSE ranges only.
- **Three different ranges are hardcoded across hover strings in one
  module**, all for the same quantity: `~15-20 R_sun` in
  `outer_corona_info_hover`; `~10-20 solar radii` in
  `alfven_surface_info`; and `Polar coronal holes: ~12-15 R_sun |
  Streamer belt: ~17-19 R_sun` in BOTH Alfven strings. The `# Source:`
  above them reads Cranmer et al. (2007), with no position given.
- **Why it is worth a look rather than a shrug.** `~17-19` sits close
  to the 17 R_sun corrected at source on 2026-08-22, and DeForest,
  Howard & McComas (2014) give 12 polar and 15 streamer-belt as
  INSTRUMENTAL FLOORS -- a noise floor and a coronagraph field of view,
  not a shape. A range that looks like a measured latitude variation
  and is actually two instrument limits is the exact confusion the
  citation-KIND rule was drafted for (design note 2026-08-22,
  Section 2).
- **Disposition is already decided; only the citation is open.**
  Tony's rule, restated 2026-08-23: a range may be NOTED where it has
  a citation, the VISUALIZATION uses the interpolated constant, and
  where the citation is insufficient the values are OMITTED. So:
  read Cranmer et al. (2007) for a locatable position stating the
  latitude variation. If it carries it, cite it properly and keep the
  range as prose. If it does not, remove all three ranges and note the
  gap. Do not reconcile them against each other -- three unsourced
  numbers agreeing is not evidence.
- **Tony-action (do):** the source read. Claude cannot clear this by
  reasoning about it, and guessing here is the failure this week was
  spent on.
- **Note:** RICE 2/3/60/2 -> 3.0 is Claude's proposed score.
  Confidence is 60 because whether Cranmer carries the claim is
  unknown until somebody reads it. **Tony-action (decide):** confirm
  or redirect.
- **Ref:** `solar_visualization_shells.py` (`outer_corona_info_hover`,
  `alfven_surface_info`, `alfven_surface_info_hover`);
  `constants_new.py::ALFVEN_SURFACE_RADII`; L-209 (the DeForest
  correction and the interpolation leg); L-210;
  `documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`
  Section 2 (value, source, KIND).

#### [L-229] Streamer band drawn in the ecliptic plane, not the solar equator
<!-- L:229 status:OPEN upd:2026-08-23 section:A flag: rice:3/4/95/1 -->
- **Found by Mode 5 on 2026-08-23.** Tony looked at the render and
  asked whether the belt should lie in the ecliptic rather than the
  solar equatorial plane. It should not, and the same figure already
  carried the proof.
- **The defect.** `create_streamer_band_shape` returns points whose own
  docstring says "Positions in SOLAR RADII in the body frame." The
  caller scaled them and handed them to Plotly with NO rotation, so
  the band's plane of symmetry landed on the ecliptic. Meanwhile
  `build_rotation_axis_traces` takes the Sun's spin pole from
  `create_planet_transformation_matrix('Sun')` and is correctly
  tilted. The axis leaned; the band lay flat.
- **Measured, by fitting the point cloud's plane:** before, normal
  (-0.0003, -0.0004, 1.0000), tilt 0.03 deg from the ecliptic; after,
  normal (0.1227, -0.0314, 0.9920), tilt 7.27 deg. Angle between the
  band normal and the Sun's spin pole after the fix: 0.028 deg. The
  solar equator is inclined 7.25 deg to the ecliptic.
- **Both traces now read ONE matrix**, so they cannot disagree again.
  That is the structural half of the fix and it matters more than the
  seven degrees.
- **WITHDRAWN 2026-08-23, same day, and left visible.** This entry
  originally carried a bullet titled "Why the solar equator is the
  right plane", arguing from the heliospheric current sheet, the
  solar magnetic equator, and the dipole's alignment with the spin
  axis near solar minimum. **None of that is sourced anywhere in this
  project.** Tony asked whether there was a reference for the belt's
  orientation; a repo-wide search found none -- not for the
  orientation, not for `warp_amp_deg` = 15.0, not for the two-lobe
  warp, and not for the hover's existing claim that the tilt sweeps
  toward the poles across the 11-year cycle. The physics may well be
  right. It was stated as established, which is the failure the
  resident rule names: wrong-but-asserted is worse than uncited,
  because the assertion suppresses the suspicion that would catch it.
  Recorded rather than deleted, because a claim withdrawn silently
  leaves the next reader nothing to check against.
- **What actually justifies the rotation, and needs no physics
  citation.** `create_streamer_band_shape`'s own docstring says it
  returns points "in the body frame"; the caller treated them as
  ecliptic. That is an internal contract violation. The Sun's body
  frame is DEFINED by its rotation pole, and that pole is sourced
  (IAU 2018, RA 286.13, dec 63.87). So the band belongs in that frame
  because it is the frame it was built in. Everything past that --
  that the belt is organized about the solar equator at all -- is a
  drawing choice, now declared as one in the code comment and in the
  hover the reader sees.
- **Tony-action (do): find a citation for the belt's orientation, or
  leave it declared.** Same shape as L-228 and the same module. If a
  source states that the streamer belt / heliospheric current sheet
  is organized about the solar rotation or magnetic equator, cite it
  and the ASSUMPTION note comes out. If none is found, the note
  stays and that is an honest ending, not a failure. Unlike a range,
  an orientation cannot be omitted -- the band has to be drawn
  somewhere -- so this falls under Show the Envelope of the
  Unknowable rather than under omit-if-unsourced.
- **The info marker rotates with the band.** Rotating one and not the
  other would leave the marker off the band edge -- geometry right,
  affordance wrong. Verified unchanged at 2.038e-03 AU to the nearest
  band point, before and after.
- **Nothing automated could have caught this.** The module compiles,
  the trace builds, the geometry is internally consistent, and no
  checker compares two traces' frames. Fourth instance this month of
  the render being the only gate: L-227 (hover width), L-224 (band
  shape), L-209 (shell radius), and now the frame.
- **Also fixed here (L-227 follow-on):** the L-227 re-flow moved a
  computed figure out of the scanner's citation window, taking the
  tree count 292 -> 294. A `# Source:` comment now sits mid-string
  above that line. Measured on a live scanner run: this file's Tier-1
  count 7 -> 6. The first attempt used `# Derived:` and did NOT clear
  it -- that token is worksheet-leg vocabulary, not scanner
  `SOURCE_PATTERNS`. The two overlap enough to mislead.
- **Note:** RICE 3/4/95/1 -> 11.4 is Claude's proposed score. Impact 4
  because a wrong frame is a wrong physical claim on screen, not a
  cosmetic one. **Tony-action (decide):** confirm or redirect, then
  re-run `ledger_index.py`.
- **Tony-action (do): Mode 5.** Relaunch and look at the Sun. The band
  should lean with the yellow rotation axis instead of lying flat on
  the ecliptic grid -- about 7 degrees, visible but not dramatic.
- **Ref:** `solar_visualization_shells.py::create_sun_streamer_band`;
  `planet_visualization_utilities.py::create_streamer_band_shape` and
  `build_rotation_axis_traces`;
  `idealized_orbits.py::create_planet_transformation_matrix` and
  `planet_poles['Sun']` (IAU 2018); L-224 (the band build); L-227 (the
  re-flow); L-209 (the Alfven constant this cites).

#### [L-230] A skill bump does not reach the protocol's version history
<!-- L:230 status:DEFERRED upd:2026-08-23 section:A flag: rice:3/3/85/2 -->
- **Tony's observation, 2026-08-23.** A skill bump runs a four-link
  chain: `SKILL.md` version line -> `skills_index.py` -> the manifest
  zone in `PROJECT_INSTRUCTIONS.md` -> a protocol VERSION HISTORY
  entry. The first three fire. The fourth does not.
- **Not a new rule -- one that stopped firing.** The archive carries
  `v3.35 (August 7, 2026): Updated skill safe-file-editing (v1.3).`
  A skill bump earning an entry on its own. That is harder to notice
  than a rule that never existed, and the manifest going current by
  itself DISGUISES the omission: the protocol looks updated because
  half of it was.
- **Prevention landed 2026-08-23** in `ledger-and-session-records`
  1.9: the binding rule gains its fourth step. Detection is this item.
- **Tony's design instinct, and it is right:** report it in the
  maintenance runner. That is the tool already in the routine, and
  the resident gate says put the check where it runs rather than in a
  document someone has to remember. An earlier Claude proposal to
  write the convention into the protocol as prose was redirected for
  exactly that reason.
- **THE NAIVE CHECKER DOES NOT WORK, and this was measured rather
  than guessed.** "For each skill in the manifest, does its current
  version appear anywhere in the written history?" reports **10 of
  10** skills as unrecorded at `41c0b279`. Three causes: only three
  entries stay resident, the archive names older versions, and several
  skills have sat at 1.1 since creation and were never the subject of
  any entry. A check that fires on everything is ignored by its second
  run -- the same failure as an audit whose denominator grows whenever
  someone thinks of something.
- **The design that does work watches the TRANSITION, not the state.**
  If a skill version changed since the last run, the protocol version
  must have changed too. That needs memory of the previous state,
  which is the pattern the suite already uses
  (`data/worksheet_check_state.json`, `data/provenance_history.json`)
  rather than a new store. It can fail, and it fails exactly once per
  unrecorded bump, which is what makes it worth running.
- **Deferred deliberately.** A checker module, a state file, runner
  wiring and its own test is a build, not a patch, and it deserves the
  design round. The dead end above is recorded so a future session
  does not re-derive it.
- **Note:** RICE 3/3/85/2 -> 3.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
- **Ref:** `PROJECT_INSTRUCTIONS.md` v3.42 and its Skill Manifest;
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`; `skills_index.py`;
  `skills/ledger-and-session-records/SKILL.md` v1.9, Protocol and
  Skills Change Log; L-188 (the maintenance runner); L-226, L-227 (the
  two bumps whose absence from the history exposed this).

#### [L-231] Radiation belts are drawn in the ecliptic; the magnetic tilt is an unbuilt intent
<!-- L:231 status:OPEN upd:2026-08-24 section:A flag: rice:2/2/90/2 -->
- **Found while porting the belts to the gallery, 2026-08-24, and the
  first reading of it was WRONG.** Claude reported it as L-229's defect
  class in two more places: `create_earth_radiation_belts` and Jupiter's
  belt builder each construct their points in the ecliptic XY plane with
  a `sin(2*theta)` vertical wobble and never call
  `orient_to_planet_pole`, while each carries a comment saying the belt
  is built around the planet's rotational axis.
- **Tony's correction, same day.** The comment is not a false claim about
  what the code does. It records an intent that was never built -- adding
  the small magnetic axial tilt these planets actually have. So this is
  an unbuilt feature with a breadcrumb, not a frame error.
- **Why the distinction matters and is not pedantry.** L-229 is a
  MISTAKE: the streamer band's own docstring said body frame and the
  caller rotated nothing, so the render contradicted the data. This is a
  PLACEHOLDER: the current drawing is a defensible approximation and the
  comment marks where the refinement goes. Filing the second as the first
  would have put a correct-enough render into a defect queue.
- **The right rotation is not the pole.** Belts follow the MAGNETIC
  dipole, so the eventual transform is the dipole tilt applied on top of
  the spin pole, not the spin pole alone. Approximate magnitudes: Earth
  about 11 deg from the rotation axis, Jupiter about 10 deg, Saturn under
  0.1 deg -- which is why Saturn is the one body where using the pole
  alone (as `saturn_visualization_shells.py` already does) is very nearly
  right. Those figures are orientation for a future design round, NOT
  citable values; sourcing them is part of the build.
- **Scope, when built: BOTH instruments.** The gallery's
  `feature_renderers.js` deliberately matches the orrery here -- scene
  equivalence -- so a change to the orrery's belt orientation must be
  carried to the renderer in the same pass or the two will disagree.
  The renderer already receives `orientation` for Jupiter and consumes it
  only for rings.
- **Note:** RICE 2/2/90/2 -> 1.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
- **Ref:** `earth_visualization_shells.py` (belt builder);
  `jupiter_visualization_shells.py` (belt builder);
  `saturn_visualization_shells.py` (belts DO use the pole);
  `idealized_orbits.py::orient_to_planet_pole`; gallery
  `gallery/feature_renderers.js::renderBelts`; L-229 (the genuine frame
  defect this was mistaken for); L-154.

#### [L-232] The gallery's served constants carry sources that nothing checks
<!-- L:232 status:OPEN upd:2026-08-24 section:A flag: rice:3/3/85/2 -->
- **Opened 2026-08-24, as a consequence of Tony's option-(a) ruling.**
  Two render inputs the served cache lacked were added to the gallery's
  `data/objects_config.json`: the IAU pole for Jupiter and Saturn, and
  `planet_radius` for Earth and Jupiter. Both are MEASURED values, both
  carry a `source` field and an `orrery_constant` field naming where they
  were copied from.
- **They are the FIRST `source` fields in that file**, and they sit in a
  store no checker reads. `provenance_scanner.py` scans Python. The
  worksheet checker scans Python. Nothing reads JSON in the gallery repo.
  So a source line there is a claim with no gate behind it -- exactly the
  shape the resident gate warns about, one repo over.
- **The value was still worth adding.** The alternative on the table was
  a JavaScript table, which is a store the transport does not target
  either AND is invisible to the pinning design. Putting the copy where
  segment 2 will land is the version that converges.
- **Earth's radius now appears TWICE in that file**, once in
  `atmosphere_shell` and once in `van_allen_belts`, because a shared
  sibling would have meant a third top-level feature key on Earth and
  L-080's fingerprint hashes that list. The duplication is deliberate and
  is the transport's to collapse, not a hand edit's.
- **Not a blocker for Artifact 2.** The artifact's thirty measured
  numbers are the ring and belt values, which live in the orrery and are
  in the audit already. These five are drawing inputs that arrived with
  their sources attached on the day they were written, which is the
  strongest position a value ever occupies -- the risk is drift later,
  not error now.
- **Two candidate shapes, neither designed:** teach the worksheet
  checker to read `objects_config.json` as a second corpus, or make the
  transport (segment 2) verify each `orrery_constant` pointer resolves
  and matches. The second is better if it lands, because it fixes the
  producer.
- **Note:** RICE 3/3/85/2 -> 3.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
- **Ref:** gallery `data/objects_config.json`;
  `provenance_scanner.py`; `worksheet_keys.py`; L-155 (pinning);
  L-181 (single home for feature constants); L-154; master plan
  Section 7 decisions 12 and 18.

#### [L-234] Reopen Artifact 1: recreate the orrery's Sun in the assembler
<!-- L:234 status:OPEN upd:2026-08-25 section:A flag: rice:4/5/90/3 -->
- **Tony's ruling, 2026-08-25, in three parts.** (1) The artifact ladder
  has a SECOND AXIS that was never sequenced. The seven golden artifacts
  are seven PROPAGATION shapes -- conic, planetocentric, mean elements,
  spacecraft arc, barycentric binary -- and that ladder is complete and
  good. What the orrery DRAWS is a different axis entirely: interiors,
  atmospheres, magnetospheres, belts, tori, rings, comae, solar shells,
  Hill spheres. Nothing in the five segments or the seven artifacts
  sequences that axis. (2) Nobody ever decided that some structures
  would be shown and others not; L-100 carried that as an inherited
  default, never a ruling. (3) Artifacts REOPEN: reopen Artifact 1, get
  it right, then Artifact 2, and so on. "Right" means the orrery
  recreated in the assembler as far as possible. Re-locking is normal,
  not a failure, and the orrery may improve on the way -- as it did with
  the streamer belt.
- **Tony, verbatim:** "it is not my intent. The general intent is to
  redo the orrery in the assembler. Part by part."
- **The consequence that arrives first.** The resolver requests EVERY
  feature key the cache carries for an object, and the golden record
  hashes `feature_keys`, `trace_role_counts` and `legend_groups`. So
  adding a feature family to a body FAILS every locked artifact
  containing it. Under part-by-part that is the normal event, not an
  edge case.
- **Sun half: DONE 2026-08-25.** 19 shells in the assembler, 14 spheres
  and 5 custom. Six gallery-side patches, `patch_L234_1` through `_6`:
  Sun entry plus builder skip and three gates taught; centre features
  dispatched; the 14 spheres drawn; the L-227 hover-wrap fix with scoped
  smoke assertions; IAU solar pole plus the streamer band; the three
  Oort custom shells (torus, clumps, galactic tide). Also delivered:
  `smoke_sun_shells.js` (30 checks) and the two payload fixtures
  `payload_earth.json` and `payload_jupiter_saturn.json`, which had never
  been committed and without which the two existing smoke suites could
  not run at all.
- **Mode 5 passed twice.** 2026-08-24 on the 14 spheres; 2026-08-25 on
  the complete Sun ("looks great"). 44 traces from 8 requests -- Earth's
  4 geometry and 4 markers, the Sun's 18 and 18 -- reconciling exactly
  against the config. Two things the render confirmed that no unit test
  could: the band reads as a helmet and stalk tilted off the ecliptic,
  which is what the 7.225 degree plane fit predicted (L-229); and Frame
  on Sun returned a half-span of 0.279 AU, 1.2 times the outer corona at
  0.2326 AU, which is the legendonly skip in `frameLayout` working --
  without it the frame would have ranged to the gravitational influence
  at 150,000 AU and the Sun would have vanished into a pixel.
- **Three things the build discovered.** (a) THE SUN WAS NOT AN OBJECT:
  twelve entries in `objects_config.json` and none of them the Sun,
  which existed only as a scene centre drawn as a yellow marker, with no
  catalogue record and therefore no `features` key. (b) `frame-origin`
  IS LOAD-BEARING, NOT A LABEL: `served_window` is computed from every
  object whose `canonical_frame` is `heliocentric`, and a participant
  with no trust measurement NULLS that window for the whole cache,
  silently disabling the resolver's propagation bound site-wide --
  tested both ways. (c) THREE BUILDER GATES WOULD HAVE ABORTED THE
  NIGHTLY and reading the code found none of them; `assert_structural`
  invariant #3 aborts on any non-spacecraft with no osculating block,
  which would have killed every build, not just first ones.
- **Not on this path:** segment 2 (transport), the general provenance
  audit, L-225, L-231, and the barycentric solar scene (L-137).
**Gap:** the EARTH half. Inventory measured at orrery HEAD. Already
served: `atmosphere_shell` (1.05, 1.25) and `van_allen_belts`.
Interiors, not served: inner_core 0.19, outer_core 0.55, lower_mantle
0.85, upper_mantle 0.98, crust 1.0. Also not served: hill_sphere 235.0.
Custom, not served: rotation_axis, dipole_cone, magnetosphere, leo,
geostationary_belt. Missing: an `orientation` key -- Earth's pole is
RA 0, Dec 90 (IAU 2018, J2000 celestial north). Two shapes the Sun did
not need: five of the six new sphere entries sit BELOW the surface, so
L-238 is the first patch; and the magnetosphere is genuinely new
geometry -- not a sphere, not a torus, not a band. Earth's block in
`shell_configs.py` carries a block-level `# Source:` header naming USGS,
NASA Earth Fact Sheet, NOAA/NCEI and the Van Allen Probes, verified in
the April 2026 provenance audit; those are the sources the config
entries should carry, with an `orrery_constant` pointer, same pattern as
the Sun's.
- **Note:** RICE 4/5/90/3 -> 6.0 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, then re-run
  `ledger_index.py`.
**Ref:** HANDOFF 2026-08-25 (orrery `4ad78a01`, gallery `64201783` ->
`88633707`); L-100 (closed by this ruling); L-235, L-237, L-238 (the
work in front); L-229 (the solar pole the band needed); L-239, L-240,
L-241 (orrery-side findings); L-080 (the artifact fingerprint's fields).

#### [L-235] Checks that cannot fail, gallery side [three instances]
<!-- L:235 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/95/1 -->
- **Found 2026-08-25 while building the Sun.** Three instances of the
  resident gate A Check That Cannot Fail Is Not Passing, all in the
  gallery repo, each reporting exactly what a real pass reports.
- **(1) `test_artifact1_earth.py` T5 reads `fp.compare(golden, golden)`**
  -- the fingerprint against itself. It cannot return a difference, and
  the stored `artifact_1_earth_alone.json` is never opened. Passing
  since July.
- **(2) `solar_system_earth_test2.html` line 99 prints "matches golden
  abbd01094852b57f" as a hardcoded `<summary>` caption.** Nothing
  compares. And `abbd01094852b57f` is `scene_spec_hash` ALONE -- the one
  field that cannot move when features change, which is precisely what
  part-by-part will keep changing.
- **(3) The two smoke suites read `payload_jupiter_saturn.json`,** which
  was a session artifact and was never committed, so neither suite could
  run at all. CLOSED 2026-08-25 by regenerating both payload fixtures.
**Gap:** instances 1 and 2. Point T5 at the STORED file, and either wire
the HTML caption to a real comparison or delete the claim. Worth pairing
with L-237, because re-cutting a golden that nothing compares against
buys very little.
- **Note:** RICE 3/4/95/1 -> 11.4 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** gallery `test_artifact1_earth.py`,
`solar_system_earth_test2.html`, `payload_earth.json`,
`payload_jupiter_saturn.json`; PROJECT_INSTRUCTIONS Part 3, A Check That
Cannot Fail Is Not Passing; L-236; L-237.

#### [L-236] Gallery maintenance runner [designed, unbuilt]
<!-- L:236 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/80/4 -->
- **Shape.** A `maintenance_run.py` in the GALLERY repo, plus a
  dashboard button in the existing Gallery and Web group.
- **Why it belongs in the gallery, not the orrery.** Every input it
  reads is there. A checker run from the orrery would reach a sibling
  directory that exists only on Tony's machine, and a check that cannot
  find its target skips quietly -- the same failure class as the three
  instances in L-235.
- **First roster:** module atlas and index (generators); the artifact-1
  golden compared against the STORED file; the three Node suites, with
  Node's absence REPORTED rather than skipped; served-cache structural
  validation; config feature-shape validation.
**Gap:** designed, not built.
- **Note:** RICE 4/4/80/4 -> 3.2 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-188 (the orrery-side maintenance runner this mirrors); L-235.

#### [L-237] Artifact 1's golden record is stale and needs re-cutting
<!-- L:237 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/90/1 -->
- **Unblocked 2026-08-25:** Mode 5 passed on the complete Sun, so the
  gate this was waiting on is discharged.
- **Cut 2026-07-11; it differs from today in four fields,** three of
  which predate the 2026-08-25 session: `cache_snapshot_id`;
  `coordinate_bounds` (the nightly refreshes Earth's osculating
  elements); `warnings`, which still carries "served_window is null",
  untrue since 2026-07-22; and `feature_keys`, which gains the Sun's
  six.
**Gap:** re-cut it. Pair with the L-235 T5 fix -- re-cutting a record
that nothing compares against buys very little.
- **Note:** RICE 3/4/90/1 -> 10.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-234; L-235; L-080 (the fingerprint's field list).

#### [L-238] radius_fraction > 1.0 assumes every shell is above the surface
<!-- L:238 status:OPEN upd:2026-08-25 section:A flag: rice:3/5/95/1 -->
- **`_validate_feature_shapes` in `gallery_cache_builder.py` asserts
  it.** True of every shell served so far. False of every INTERIOR shell
  in the orrery.
- **It blocks the Earth build.** Earth's inner core at 0.19 walks
  straight into it, and five of the six new sphere entries sit below the
  surface. This is the Earth half's FIRST patch.
**Gap:** relax the invariant to admit interior shells without losing
whatever it was protecting against, then re-run the builder's testing
layers.
- **Note:** RICE 3/5/95/1 -> 14.3 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** gallery `tools/gallery_cache_builder.py`;
`documentation/TESTING_PROTOCOL.md`; L-234 (the Earth half).

#### [L-239] Seed the three Oort builders so a render is reproducible
<!-- L:239 status:OPEN upd:2026-08-25 section:A flag: rice:2/2/90/1 -->
- **Orrery-side recommendation from assembler work, 2026-08-25.**
  `create_sun_hills_cloud_torus`, `create_sun_outer_oort_clumpy` and
  `create_sun_galactic_tide` in `solar_visualization_shells.py` draw
  from the GLOBAL numpy RNG, so the same figure looks different on every
  render.
- **The streamer band's own docstring already names this and declines to
  copy it.** The assembler ports are seeded.
- **Recommendation:** seed all three in the orrery with the same pattern
  -- a `RandomState` local to the builder, seed in the config -- so the
  two instruments agree about whether a render is reproducible.
**Gap:** nothing depends on it today. It will matter the first time an
Oort scene is fingerprinted.
- **Note:** RICE 2/2/90/1 -> 3.6 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `solar_visualization_shells.py` lines ~1411, ~1475, ~1551
(verified at orrery `4ad78a01`); the gallery's Sun custom shells; L-234;
L-241 (same three builders).

#### [L-240] Split declared drawing parameters from measured values
<!-- L:240 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/70/4 -->
- **Orrery-side recommendation from assembler work, 2026-08-25.** The
  gallery's `objects_config.json` now stores the two kinds APART: the
  streamer belt's cusp (Suess and Nerney) and fade (Kasper) sit in
  `{value, unit, source}` nodes, while the warp amplitude, lobe count
  and widths sit under a `drawing` block whose `_declared` field says
  plainly that nobody has sourced them. The orrery mixes both kinds in
  one dict with comments alongside.
- **This is the STRUCTURAL half of the reachability problem.** The
  scanner cannot tell a measurement from a drawing choice because the
  code does not distinguish them, so the audit either over-counts
  (chasing citations for `n_points`) or under-counts.
- **Recommendation:** adopt the same split in `constants_new.py`'s
  FEATURE_REGISTRY when L-181 designs it -- measured entries carry a
  source field as DATA, declared entries carry a declaration string. The
  gallery has now proved the shape works.
**Gap:** gated on L-181's design pass; not a separate build.
- **Note:** RICE 4/4/70/4 -> 2.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-181; L-190; L-232; gallery `data/objects_config.json`.

#### [L-241] Hills torus hover states the cloud bounds, not the drawn ring
<!-- L:241 status:OPEN upd:2026-08-25 section:A flag: rice:2/2/95/1 -->
- **`create_sun_hills_cloud_torus` hovers "2,000 to 20,000 AU".** The
  drawn surface runs 5,570 to 16,953 AU about a ring at 11,000, because
  a torus built from an inner and an outer bound puts its surface at the
  MID-radius.
- **Neither statement is wrong** -- the bounds are the cloud, the ring
  is the drawing -- but a reader measuring the picture against the hover
  will find they disagree.
- **Recommendation: say both.** Identical in the assembler; fix both or
  neither.
**Gap:** minor. Fold into the next touch of either instrument.
- **Note:** RICE 2/2/95/1 -> 3.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `solar_visualization_shells.py`; L-234; L-239 (same builders).

#### [L-243] Retire the replicated AU conversion factor
<!-- L:243 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/95/2 -->
- **Tony's instruction, 2026-08-25:** conversion factors live in
  `constants_new.py`, carry a source, and are CALLED -- not replicated ad
  hoc.
- **The definition is already exemplary.** `KM_PER_AU = 149597870.7` at
  `constants_new.py` line 56, sourced to IAU 2012 Resolution B2 as an
  exact definition, with two independent cross-checks recorded (Claude
  and GPT, both 2026-08-02, each naming its worksheet). Nothing to do
  there.
- **Thirteen live-code replications across seven modules**, measured at
  orrery `4ad78a01`: `palomas_orrery.py`, `visualization_utils.py`,
  `shared_utilities.py`, `spacecraft_encounters.py`,
  `sgr_a_visualization_core.py`, `sgr_a_visualization_core_arcs.py`,
  `create_ephemeris_database.py`. Most are an inline `* 149597870.7`
  inside an f-string. Five of the seven import nothing from
  `constants_new` today.
- **One is a NAMED shadow and it is the dangerous one.**
  `spacecraft_encounters.py` line 70: `AU_KM = 149597870.7  # 1 AU in
  km`, used 14 times in that module. A grep for `KM_PER_AU` does not
  find it, which is how it survived a convention that already forbids
  it. Its schema comment at line 59 states the divisor as a literal too
  -- The Correction Does Not Travel applies to that line in the same
  patch.
- **Recommendation: retire the NAME, not only the value.** An alias
  (`AU_KM = KM_PER_AU`) would remove the second number while leaving the
  second name, and a second name is how this one started. Fourteen
  mechanical substitutions in a data-table module where the diff reads
  easily.
- **Two things measured clean and worth recording.** `SUN_RADIUS_KM` has
  ZERO live replications -- 695700 appears nowhere outside its
  definition. And `constants_new.py` imports only numpy and datetime, so
  it is a leaf: importing it into any of the seven carries no
  circular-import risk.
- **The gallery's copy cannot be removed.** `feature_renderers.js` line
  35 holds `var KM_PER_AU = 149597870.7;`. JavaScript cannot import a
  Python module, so that is segment 2's surface by construction -- and
  one line is as small as that surface gets.
**Gap:** one transactional patch across the seven modules. Touches hover
strings, so the agentic-pre-test data-sweep gate applies: py_compile,
xvfb run on a throwaway copy, live-dispatch smoke.
- **Note:** RICE 3/3/95/2 -> 4.3 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `constants_new.py` line 56; No Shadow Constants [CRITICAL];
L-178 (the EARTH_RADIUS_KM duplicate, same class); L-244.
**Note (2026-08-25) -- the count above is corrected.** The row
says thirteen replications and ONE named shadow. Thirteen is
right for VALUES. The name count is five: `AU_KM` in
`spacecraft_encounters.py` and `AU_TO_KM` in
`create_ephemeris_database.py` both held the literal and were
retired by `patch_L243_1`; three more held no number at all --
`AU_TO_KM = KM_PER_AU` in `sgr_a_star_data.py` (dead, used
nowhere), `close_approach_data.py` (3 uses) and
`apsidal_markers.py` (function-local, 2 uses) -- and were
retired by `patch_L243_2`.
The miss is the useful part and it is a measurement error, not
an oversight: the sweep was scoped by grepping 149597870, and a
grep for a number cannot find a name that holds no number.
All three were residue of the April 2026 provenance pass, which
replaced the values and kept the names on purpose --
`close_approach_data.py` said so in a comment above its alias.
Left visible rather than restated, because the next reader has
nothing else to check the count against.
**Ref (added):** `patch_L243_2_au_to_km_aliases.py`;
`provenance_scanner.py` line 2523, whose alias table still
expects `AU_TO_KM` and `AU_IN_KM` -- routed to L-244.

#### [L-244] Sweep for replicated conversion factors as a class [Fable candidate]
<!-- L:244 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/70/3 -->
- **The companion to L-243, and deliberately separate from it.** L-243
  is countable today -- thirteen sites, seven modules, one shadow name --
  and it closes. This one names the CLASS: any conversion factor
  replicated rather than imported.
- **Why the two are split.** A class with no detector has no
  denominator, which is the audit-that-never-closes shape the resident
  rule warns about. Tony's 2026-08-25 framing: do the narrow one now,
  carry the broad one as an item.
- **Candidate route: a Fable sweep.** Broad-reach scoping is what that
  leg is for, and the question suits it -- enumerate every numeric
  literal in the codebase that duplicates a value already named in
  `constants_new.py`, whatever it is called locally. The answer is a
  list, not a judgment, which is the shape that dispatches well.
**Gap:** scope the dispatch. Until it runs there is no count, and until
there is a count this item cannot be sized honestly.
- **Note:** RICE 3/4/70/3 -> 2.8 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, and whether Fable
  carries it.
**Note (2026-08-25) -- the dispatch is bounded, and this is its shape.**
Raised by Tony: a sweep of this kind "can become its own rabbit hole,
chasing all the findings."
- **The hole opens only when DISCOVERY and REMEDIATION are the same
  activity.** That is what happened on 2026-08-25: fixing while
  searching, so every fix opened the next search, with no stopping
  condition because "no more findings" cannot be verified. Fable
  ENUMERATES and fixes nothing. The output is ledger rows; the fixing
  happens later, in slices, under The Braid (PROJECT_INSTRUCTIONS Part
  3, added v3.43).
- **The denominator is finite and measured at `2bf0d06a`:** 55
  module-level names in `constants_new.py`, four of them derived,
  against roughly 1,100 distinct multi-decimal literals in the live
  tree.
- **The pattern is mechanical:** a numeric literal equal to a value
  already named in `constants_new.py`, or derivable from named values
  within one or two steps, within a stated rounding tolerance. That
  definition catches `3.26156` and `4.74` and needs no judgment about
  what counts as a physical constant -- which is the wider version that
  would not terminate.
- **Report by CONSTANT, not by SITE.** One row per constant-and-module
  pair with a count, not one per occurrence. `3.26156` is ONE finding
  across eleven modules, the way L-248 writes it. Otherwise the sweep
  inflates the ledger by an order of magnitude and creates a second
  problem while solving the first.
- **Timing: the enumeration runs BESIDE the Earth build, not before
  it.** It touches no file and runs outside the project context window,
  which is what the Mode 7 scoping leg is for. Wait for
  `patch_L248_1` and L-249 to land so it is not enumerating values
  about to change; a few days of staleness would not matter for a
  sizing exercise, but those two are close.
- **Why the enumeration is worth doing soon even though remediation is
  not.** The dangerous crack is the undocumented one. A count turns
  "there may be more of these" into a finite list with RICE scores,
  which is the difference between a background worry and a backlog.
**Ref (added):** L-248; L-250; PROJECT_INSTRUCTIONS Part 3, The Braid.
**Ref:** L-243 (the narrow instance); L-181; L-190 (scanner reach).

#### [L-245] Constants drift check compares against the last COMMIT, not the last RUN
<!-- L:245 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/90/2 -->
- **Raised 2026-08-25 from Tony's question about carrying a backup copy
  of `constants_new.py` to diff against.** The backup was declined on
  Tony's own prior ruling; the gap behind the question is real and this
  is it.
- **The declined half, for the record.** `constants_change_report.py`
  states under WHY THERE IS NO SECOND COPY OF ANY NUMBER that a stored
  list of expected values is a second dictionary, a second dictionary is
  hand-maintained, and a hand-maintained copy goes stale -- citing
  `test_constants_provenance.py`, which was that copy: 52 pinned
  literals, six of them behind an August 2 correction batch for ten
  days. A backup of the whole file is that failure at maximum size.
- **The real gap.** The tool compares the WORKING TREE against the LAST
  COMMIT, and says so: it is a pre-commit reader. That fits Tony's loop
  exactly -- sandbox, test, local repo, maintenance run, commit, push --
  but only while the run precedes the commit. Run the suite after
  committing and the diff is empty. The output still prints "compared
  against <sha> <subject>", which is honest evidence git resolved and
  ran, and still reads as nothing changed. Same green, different
  meaning.
- **Fix, confirmed by Tony 2026-08-25: store the last-run SHA, not a
  file.** Compare against the commit the last maintenance run examined
  rather than against HEAD. Git still holds every prior value, so no
  second copy of any number exists and the 2026-08-12 ruling stands
  intact. The window becomes "since anybody last looked" instead of
  "since the last commit."
- **Shared state with L-230.** The skill-version transition watcher needs
  the same "since the last run" anchor to see a version move while the
  protocol version did not. One small run-state file, two checks reading
  it. Build them together or the second one invents a second store.
**Gap:** design the run-state file (location, what it holds, what
happens on a first run with no prior state), then amend
`constants_change_report.py` and build L-230's watcher against it.
- **Note:** RICE 3/4/90/2 -> 5.4 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** `constants_change_report.py`; `maintenance_run.py` CHECKERS row
1; L-230 (the transition watcher); L-188 (the runner);
PROJECT_INSTRUCTIONS Part 3, A Check That Cannot Fail Is Not Passing.

#### [L-246] S4714's semi-major axis was three values in three stores
<!-- L:246 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/85/2 -->
- **Found 2026-08-25 by Mode 5.** Tony sent a Grand Tour screenshot to
  confirm an unrelated import. The hover read `Semi-major axis: 800 AU`
  and the catalog read 520.0.
- **Three stores, one number.** `sgr_a_star_data.py` held
  `'a_au': 520.0`. Two consumer modules reached into the SHARED dict at
  import time and set it to 800.0 -- `sgr_a_grand_tour.py` line 39 as a
  bare statement, and `sgr_a_visualization_precession.py` line 33 as a
  patch dict plus a function called on import. The second one states its
  own reasoning: "We apply this patch at runtime so the original data
  module stays clean." The intent was to protect the source of truth and
  the effect was to make it depend on import order.
- **A live path saw neither override.**
  `sgr_a_visualization_animation.py` imports the data module and the core
  renderer and no patcher, and calls `get_star_data('S4714')` at four
  places. So the same star was drawn two ways.
- **And each view's PROSE was correct for its own value.** The grand
  tour hover reports 8.2% of light speed at periapsis; the animation's
  on-plot annotation says 10%. Both are right:
  `2*pi*sqrt(M/a * (1+e)/(1-e))` with the module's own
  `SGR_A_MASS_SOLAR = 4.154e6` gives 24,693 km/s for a = 800 and 30,624
  km/s for a = 520. The first matches the hover to the digit.
- **The scanner cannot see any of it.** It scores literal assignments. A
  runtime dict mutation is not one, and a value inside a dict literal is
  not a scored unit either -- the same reachability class as L-190's
  ring and belt numbers.
- **STRUCTURAL HALF CLOSED 2026-08-25** by
  `patch_L246_1_s4714_declare.py`: both overrides deleted, the value in
  the catalog once, declared with `# Note:`, `# Calculation:` and
  `# Review-note:` legs, and the animation's "10% light speed"
  annotation corrected to 8%. The render does not change; every path now
  draws what the grand tour already drew.
**Gap:** the MEASURED value. 800.0 is not sourced and does not close.
With `SGR_A_MASS_SOLAR = 4.154e6`, Kepler's third law gives P = 11.1 yr
for a = 800 against the 12.0 yr stored beside it; a 12.0 yr period needs
a = 842 AU, putting periapsis at 12.6 rather than 12.0. So 800 was
chosen to land periapsis on a round 12 rather than to satisfy the orbit.
`S4711` has the same shape -- a = 572 with a stored 7.6 yr period, where
Kepler gives 6.7. Route both to a dispatch against Peissker et al.
(2020), which the module cites in a COMMENT
(`sgr_a_grand_tour.py` line 122) in a different file from the data.
- **Note:** RICE 3/4/85/2 -> 5.1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect, and whether the S-star
  catalog joins the worksheet corpus at all -- today no entry in it
  carries a `# Source:` line.
**Ref:** `sgr_a_star_data.py` S_STAR_CATALOG; `sgr_a_grand_tour.py`;
`sgr_a_visualization_precession.py`; `sgr_a_visualization_animation.py`;
L-190 (values the scanner cannot reach); L-240 (measured vs declared);
The Artifact Bounds the Audit.

#### [L-247] Sgr A* constants migrated to the single source of truth
<!-- L:247 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/90/2 -->
- **Tony's ruling, 2026-08-25:** conversion factors and physical
  constants live in `constants_new.py`, carry a source, and are called
  rather than replicated. This is that ruling applied to
  `sgr_a_star_data.py`, which held nine of them.
- **Seven migrated, two deleted.** `GRAVITATIONAL_CONSTANT_SI`,
  `SPEED_OF_LIGHT_M_S` (derived from the store's existing
  `SPEED_OF_LIGHT_KM_S` rather than carried as a second literal),
  `SOLAR_MASS_KG`, `M_PER_AU` (derived from `KM_PER_AU`),
  `PARSEC_TO_AU`, `SGR_A_MASS_SOLAR` and `SGR_A_DISTANCE_LY` moved.
  `YEAR_TO_SECONDS` and `SGR_A_DISTANCE_PC` were DELETED: each appeared
  exactly once in the whole tree, on its own definition line.
- **Deleting a dead constant rather than migrating it is the point.**
  Moving one into the file the scanner treats as the measurement layer
  grows the audit denominator for a value the orrery never draws --
  which is what The Artifact Bounds the Audit exists to stop.
- **Two of the four "dead" names were not dead in VALUE.** `206265`
  appears three times in arithmetic and once in a docstring in
  `exoplanet_coordinates.py`; `26,670 light-years` and `4.154 million
  solar masses` are typed into hover strings in
  `sgr_a_visualization_core.py` and `_arcs.py`. So the name was dead
  where the number was alive somewhere else, spelled out. Deleting the
  name and leaving the literals would have removed the sourced copy and
  kept the unsourced ones. All seven literal sites are swept; the two
  hover strings now derive and render the same characters.
- **What did NOT travel, and is stated rather than invented.** Only one
  of the seven carried any attribution at all -- `SGR_A_MASS_SOLAR`, as
  the inline comment "(GRAVITY Collaboration 2019)", which names no
  paper, DOI or table. It is carried verbatim as a lead. The other six
  arrive carrying a `# Review-note:` saying plainly that no source came
  with them. None was given a citation to fill the gap.
- **The dispatch ran, 2026-08-25.** Five values went out as
  `REQUEST_L247_sgr_a_constants.md` and three returns came back --
  Claude Opus 5, GPT-5.6-sol, Gemini 2.5 Pro. Compared in
  `documentation/CONVERGENCE_L247_sgr_a_constants.md`.
- **The builder could not build the request, and the reason is
  structural.** `worksheet_checker.collect_claims()` skips any unit
  whose attached text carries no `# Cross-checked:` record, so the
  corpus is the ALREADY-annotated set and the builder re-checks rather
  than first-checks. Measured at `cf865ffc`: 98 corpus rows, 21 of them
  in `constants_new.py`, none of these five among them. The request was
  hand-written with no Key column, because minting keys outside
  `worksheet_keys.py` produces a key born stale.
- **Rows 1-3 came back unanimous.** G confirmed digit for digit
  (CODATA 2022). `SOLAR_MASS_KG` APPROX in all three, all three giving
  1.98841e30 from the IAU-exact `(GM)_sun` over the current G.
  `PARSEC_TO_AU` a DEFINITION, 648000/pi, in all three.
- **Rows 4-5 split two against one, on a convention gap rather than a
  fact.** Every leg agreed that GRAVITY 2019 publishes 4.154e6 and
  8178 pc and that GRAVITY 2022 publishes 4.297e6 and 8277 pc. GPT
  judged `Value correct?` against the later measurement and declared
  that at the top of its return; the other two judged it against the
  cited one. The v2 vocabulary does not say which, so this was a
  FINDING for conversation.
- **Tony's ruling, 2026-08-25 (epoch policy).** The most recent
  publication is authoritative and the value it replaces is recorded
  rather than overwritten. Refined in the same breath, because the
  literal reading does not land anywhere: "most recent publication"
  means the most recent paper that reports the value AS A RESULT. There
  are at least two later GRAVITY papers (A&A 692 A242 in 2024, A&A 701
  89 in 2025) that carry mass and distance as fit parameters while
  studying something else, and an August 2026 Nature paper on S301 that
  quotes the figures in passing. None supersedes the 2022 determination.
  Written into the section header of `constants_new.py`.
- **Tony's ruling, 2026-08-25 (the solar mass).** Introduce
  `GM_SUN_SI = 1.3271244e20` as the sourced primary and DERIVE the
  kilogram value, rather than correcting the literal. The reason is the
  product: this file holds both factors of a quantity the IAU declares
  exact, and carried as two literals their product was 1.32751827e20
  against a defined 1.3271244e20 -- 0.030% off, implicitly, where
  nothing watched it. Derived, it is exact by construction.
- **What landed** (`patch_L247_4_repair.py`): G sourced, value
  unchanged; `GM_SUN_SI` and `SGR_A_DISTANCE_PC` added as sourced
  primaries; `SOLAR_MASS_KG` and `SGR_A_DISTANCE_LY` derived from them;
  `PARSEC_TO_AU` to its exact definitional value; `SGR_A_MASS_SOLAR`
  4.154e6 -> 4.297e6. Tier-1 fell 294 -> 292. Mode 5 confirms the hover
  reads 4.297 million solar masses and 26,996 light-years.
- **Three defects in that repair, caught by two checkers, not by
  reading.** 32 unmarked continuation lines; four missing `# Resolved:`
  legs; and a `# Cross-checked:` line on `SGR_A_DISTANCE_PC` naming a
  worksheet whose row is about `SGR_A_DISTANCE_LY` -- an annotation
  asserting a check never performed on that name, written by the patch
  closing exactly that failure class. A fourth found while fixing them:
  `# Superseded:` is not a label; the registry knows twelve and that
  was an invented thirteenth. All four repaired in
  `patch_L247_5_annotation_repair.py`, which moves no value and asserts
  that by fingerprinting all seven assignments.
**Gap:** a SECOND cross-check leg on `SGR_A_MASS_SOLAR` and on
`SGR_A_DISTANCE_PC`. Both carry one. Only GPT reached the 2022 value;
the Claude return noted a successor exists without giving its numbers,
and the Gemini return gave the 2022 distance in prose but not the mass.
`SGR_A_DISTANCE_PC` carries NO leg at all, because the name did not
exist when the request went out. Both are stated in the code as
`# Review-note:` rather than smoothed over.
- **Note:** the value verdict on rows 4 and 5 is the ONE place where
  three complete returns disagreed. Recorded here because the next
  dispatch on this family will meet it again.
- **Note:** RICE 3/3/90/2 -> 4.1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-243 (the AU factor); L-244 (the class sweep -- three more
unnamed constants found while building this: 3.26156 light-years per
parsec and 4.74 AU/yr to km/s in `exoplanet_coordinates.py`, and the
seconds-per-year expression in `energy_imbalance.py` line 65);
L-246 (S4714); No Shadow Constants [CRITICAL].

#### [L-248] The parsec-to-light-year factor is typed 36 times across the star pipeline
<!-- L:248 status:OPEN upd:2026-08-25 section:A flag: rice:3/3/85/3 -->
- **The same class as L-243 and a good deal larger.** The value is
  correct at every site; there are simply 36 of it, across 11 modules.
  The whole star pipeline types the parsec-to-light-year conversion by
  hand.
- **Measured at `cf865ffc`** by counting occurrences of the literal
  `3.26156` in tracked `.py` files outside `documentation/`:
  `messier_object_data_handler` 9, `incremental_cache_manager` 8,
  `exoplanet_coordinates` 3, `data_acquisition_distance` 3,
  `vot_cache_manager` 2, `visualization_3d` 2, `star_visualization_gui`
  2, `simbad_manager` 2, `data_processing` 2, `data_acquisition` 2,
  `visualization_2d` 1.
- **It needs no new constant.** Light-years per parsec is
  `PARSEC_TO_AU / AU_PER_LIGHT_YEAR`, both already in
  `constants_new.py`. With `PARSEC_TO_AU = 206265.0` (line 1018) and
  `AU_PER_LIGHT_YEAR` derived at line 125, the quotient is 3.2615668.
  The literal 3.26156 agrees to a relative 2.1e-06.
- **Recommended as the first Fable sweep**, on L-244's route.
  Mechanical, and the answer is a list rather than a judgment.
- **Six of the eleven modules are CRLF in the repo blob** --
  `messier_object_data_handler`, `data_acquisition_distance`,
  `visualization_3d`, `data_processing`, `data_acquisition` and
  `visualization_2d` -- so the sweeping patch must translate its
  anchors per safe-file-editing, Line Endings Are Not Content.
- **Deliberately NOT folded into `patch_L248_1`.** That script is named
  for this handle and carries none of this sweep; what it does is clear
  the constants-change gate so L-249 can land. Sweeping 3 of 36 sites
  because one file happened to be open would leave 33 shadows and a
  half-migrated constant, which is worse than not starting.
**Gap:** the sweep itself. Dispatch first, then patch -- detecting line
endings per file rather than assuming the repo's LF.
- **Note (correction to the source handoff).** Step 1 of
  `HANDOFF_20260825_evening_singularity_thread.md` states 38 sites and
  an exact quotient of 3.2615675. Both are superseded by the
  measurement above. The handoff is left unedited, being a session
  record; the correction lives here. The 38 is most probably 36 live
  sites plus two spent patch scripts in `documentation/` that quote the
  literal in their own text.
- **Note:** RICE 3/3/85/3 is Claude's proposed score, which the index
  renders as 2.5. **Tony-action (decide):** confirm or redirect, and
  whether Fable carries it.
**Ref:** L-243 (the AU factor -- the narrow precedent); L-244 (the
class, and the route); L-250 and PROJECT_INSTRUCTIONS Part 3, The
Braid; `constants_new.py` lines 104, 125, 1018.

#### [L-249] The Earth slice of L-181: interior boundaries as sourced constants
<!-- L:249 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/90/2 -->
- **Confirmed by Tony on 2026-08-25 and then dropped.** The
  conversation moved to conversion factors and never came back, so it
  was agreed aloud and written down nowhere -- the same failure class
  the rest of that day was spent on. This row is the capture.
- **The shape.** Earth's interior boundary radii move into
  `constants_new.py` in km with their sources, and `shell_configs.py`
  derives its `radius_fraction` from them, following
  `CHROMOSPHERE_PHYSICAL_RADII`'s existing pattern:

      EARTH_INNER_CORE_KM    = <km>   # Source: ...
      EARTH_INNER_CORE_RADII = EARTH_INNER_CORE_KM / EARTH_EQUATORIAL_RADIUS_KM

- **What it fixes, measured at `cf865ffc`.** `shell_configs.py` stores
  `radius_fraction: 0.19` for the inner core while the hover prose
  beside it reads 1,220 km. Those disagree: 0.19 x 6378.1366 draws a
  sphere at 1,211.8 km, and 1,220 km would be a fraction of 0.19128.
  The outer core has the same shape -- 0.55 draws 3,508.0 km against a
  stated 3,500, which is 0.54875. Two copies of one number with nothing
  holding them together. Afterwards the drawing and the hover read from
  one place and cannot disagree.
- **It splits correctly for the scanner without anyone arranging it**
  (L-240): the km literal is scored, the fraction is a formula.
  Measured and declared fall out of the shape rather than being imposed
  on it.
- **What comes with it.** The km figures are round numbers in prose
  today, under a block-level `# Source:` header at `shell_configs.py`
  line 1316 naming USGS Interior of the Earth, the NASA Earth Fact
  Sheet, NOAA/NCEI, NASA Goddard, the NASA Van Allen Probes and NASA
  Solar System Dynamics, stamped "Verified: April 2026 provenance
  audit". Lifting each value gives it its OWN `# Source:` line, which
  then has to be true of that value specifically -- something a block
  header covering six sources and nine shells does not establish. That
  is the Earth slice of the verification loop, and by the 2026-08-22
  braid ruling it runs before Artifact 1 re-locks, not before the
  render.
**Gap:** blocked on `patch_L248_1`, confirmed 2026-08-25 and unbuilt.
That script clears three things: `constants_change_report.py`'s failure
on `NAME = EXPR` lines referencing other tracked names, the `4.74`
literal at `exoplanet_coordinates.py` line 373, and explicitly NOT
`3.26156` (L-248). The derived lines this item adds are precisely the
shape that gate cannot read, so building this first would trip it.
- **Note (measured while writing this row; unresolved).** The two
  mantle shells disagree with their own prose by far more than the
  cores do, and whether that is drift or a declared drawing choice
  under L-240 is not established either way. `lower_mantle` stores
  0.85, drawing 5,421 km, while its hover puts that boundary 660 km
  below the surface, which is 5,718 km or 0.8965. `upper_mantle` stores
  0.98, drawing 6,251 km, against a stated 30 km depth, which is 6,348
  km or 0.9953. Settle which of the two before the migration rather
  than during it: a derivation would silently move both spheres.
- **Note:** RICE 4/4/90/2 -> 7.2 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-181 (the parent); L-240 (measured vs declared); L-234 (the
Earth half of Artifact 1); `shell_configs.py` Earth block, lines
1316-1512; `constants_new.py` line 74 (`EARTH_EQUATORIAL_RADIUS_KM`);
`HANDOFF_20260825_evening_singularity_thread.md` step 2.

#### [L-251] The galactic centre button served a cached HTML for seven months
<!-- L:251 status:OPEN upd:2026-08-25 section:A flag: rice:4/4/95/1 -->
- **Found by Mode 5, and only because the number it showed was wrong in
  a way that could be dated.** On 2026-08-25 the Sgr A* hover read
  4.154 million solar masses after the L-247 repair had moved it to
  4.297. Two regenerations did not change it.
- **The mechanism.** `launch_galactic_center()` in `palomas_orrery.py`
  opened a permanent `sgr_a_grand_tour.html` from the repo root IF ONE
  EXISTED, and generated only when it did not. So the first click ever
  wrote that file and every click after served it back, unchanged,
  forever. Nothing in that path looks at the code again.
- **A parallel pipeline, in the exact shape the protocol names.**
  `sgr_a_grand_tour.py`'s own `__main__` already called
  `show_and_save`, which writes a temp copy, opens THAT, and offers a
  save dialog. One figure, two entry points, different behaviour, only
  one of them current.
- **The rendered value carried its own date stamp.** The hover's
  Schwarzschild radius read 12,271,267 km. The constants in force the
  day before give 12,271,442 -- a 175 km gap, relative 1.4e-05. That
  figure is reproduced to the kilometre by `AU_TO_METERS = 1.496e11`, a
  rounded astronomical unit the code no longer holds. The file was
  written in January 2026 and had survived every constant change since.
  A wrong number turned out to be a timestamp.
- **The verification instruction was itself a check that could not
  fail.** "Regenerate and hover the marker" cannot show a change in a
  file the regeneration does not write. Two Mode 5 passes returned the
  same stale numbers and neither was wrong to.
- **The fix** (`patch_L251_1_galactic_center_launcher.py`, Tony's
  ruling 2026-08-25): the launcher generates every time and hands the
  figure to `show_and_save`. The stale-file branch is DELETED rather
  than corrected, so there is nothing left to go stale.
**Gap:** confirm by clicking Galactic Center in the orrery -- it should
pause to generate, open a `tmp*.htm` tab, then offer the save dialog.
The old `sgr_a_grand_tour.html` may still be in the repo root; nothing
reads it now, and deleting it is Tony's call.
- **Note:** worth a sweep for the same shape elsewhere. A grep of
  `palomas_orrery.py` at `8847d6be` found no other launcher with an
  `os.path.exists(...) -> open` branch, but that grep was one file.
- **Note:** RICE 4/4/95/1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-247 (the constants whose change it hid); Check All Parallel
Pipelines [CRITICAL]; Verify Execution, Not Appearance [CRITICAL];
Observation Override (Tony's eyes won twice here).

#### [L-252] L2b's fourth outcome: an INCOMPLETE verdict is not a confirmation
<!-- L:252 status:OPEN upd:2026-08-25 section:A flag: rice:3/4/95/1 -->
- **Found by the pin that exists to be read.** After the L-247 repair,
  `test_worksheet_checker.py` failed with `no live claim is called
  DRIFTED without a value verdict -- got: ['PARSEC_TO_AU']`. That
  check's own comment says a DRIFTED here means a real defect is being
  reported: read it, do not relax it.
- **Reading it.** `worksheet_checker.py` maps APPROX and PARTIAL to
  `V_INCOMPLETE`, then fires DRIFTED for `V_CONFIRMED` and
  `V_INCOMPLETE` alike -- while its own comment defines DRIFTED as "the
  worksheet confirmed that value; the code left it anyway." An APPROX
  worksheet did not confirm anything. It said the number was
  approximate and supplied the exact one. Three returns verdicted
  206265.0 APPROX and gave 648000/pi; L-247 took that value; the tool
  called it drift. A `# Resolved:` leg does not clear it -- that is a
  separate mechanism.
- **The same mistake the block already fixed one case over.** Its
  comment records that all eight L-192 findings were corrections
  reported as drift, and that "the information needed to tell them
  apart was already in the matched row." It is here too, in the
  supplied-value column, read at L2a sixteen lines up.
- **The fix** (`patch_L252_1_incomplete_outcome.py`, Tony's ruling
  2026-08-25): a fourth outcome, COMPLETED -- the worksheet called it
  APPROX or PARTIAL and supplied a value, and the code now reads
  exactly that. Recorded, not routed.
- **Narrow on purpose, and pinned in both directions.** INCOMPLETE
  alone does not earn COMPLETED; the code must equal the value THAT
  worksheet supplied, by the same `compare()` L2a uses. An APPROX
  verdict where the code moved somewhere the worksheet never named
  still reports DRIFTED. Two synthetic checks, one per direction, take
  the suite 134 -> 136. Widening it to "INCOMPLETE and the code moved"
  would have made it unfailable, which is not a verdict.
**Gap:** none in the tool. Whether the four outcomes want a matching
line in provenance-discipline's verdict vocabulary is unruled --
COMPLETED is a checker outcome, not a worksheet token, and the two
vocabularies have stayed separate so far.
- **Note:** RICE 3/4/95/1 is Claude's proposed score.
  **Tony-action (decide):** confirm or redirect.
**Ref:** L-192 (the three outcomes this extends); L-247 (the founding
case); A Check That Cannot Fail Is Not Passing [CRITICAL].

#### [L-253] The 660 discontinuity's depth variation -- held unsourced
<!-- L:253 status:OPEN upd:2026-08-26 section:A flag: rice:2/2/60/2 -->
- **This row IS the breadcrumb.** Tony's ruling, 2026-08-26: keep the
  numbers pending sourcing rather than lose them, but keep them out of
  `constants_new.py`, where a `# Ref:` or a bare URL within thirty lines
  registers as a citation for the constant beside it. The ledger holds
  them at no cost to the audit.
- **What was removed from `constants_new.py`,** and why it had to be.
  `EARTH_D660_DEPTH_KM`'s Note stated that the 660-km discontinuity
  varies by up to about +/-60 km and is depressed to roughly 750 km
  beneath cold subducting slabs. The `# Ref:` beside it -- Ishii, T.,
  Huang, R., Myhill, R. et al. (2019), "Sharp 660-km discontinuity
  controlled by extremely narrow binary post-spinel transition", Nature
  Geoscience 12:869-872, doi 10.1038/s41561-019-0452-1 -- is real and
  true of the 660 km depth, and supports NEITHER figure. That paper
  resolves the transition's sharpness to about 250 m. It is not about
  lateral depth variation at all.
- **The two figures, and where each actually came from.**
  - **+/-60 km lateral variation.** Read in a geoneutrino review
    (arXiv:1310.3732), which states the 660 is a broader transition with
    depth variation of 60 km or less. A review is a secondary source for
    a physical claim; sourcing this properly means going to the 660
    topography seismology literature.
  - **Depression to ~750 km beneath cold slabs.** Stated in the abstract
    of a DIFFERENT paper by the same first author: Ishii, T. et al.,
    "Depressed 660-km discontinuity caused by akimotoite-bridgmanite
    transition", Nature (2022), doi 10.1038/s41586-021-04157-z. One fetch
    against a primary source would settle it.
- **Tony's cost ruling, same day.** The orrery draws one radius. A
  published range it does not draw is outside the bound the artifact
  sets on the audit, so adding these as constants would buy three
  permanent rows against nothing rendered. Qualitative prose carries the
  honesty at no audit cost (text-only assertions are L-194, deferred).
  If ONE figure is ever bought, buy the 750: cheapest citation of the
  three, primary source already located, and the only one that teaches
  something the sphere cannot -- it is why subducting slabs stagnate at
  the transition zone instead of sinking straight through.
- **Note:** RICE 2/2/60/2 is Claude's proposed score. Deliberately low
  reach and confidence: nothing renders from it and the second figure's
  sourcing route is not yet known.
  **Tony-action (decide):** confirm or redirect.
**Gap:** neither figure is sourced and neither is used. Closing this
means either sourcing them and deciding they earn a place, or ruling
that the qualitative statement is the final answer and closing the row
as declined. Both are closures; leaving it open is not.
**Ref:** L-249 (the migration that surfaced it); L-194 (text-only
assertions); L-240 (measured vs declared); Fetched vs Recalled and Show
the Envelope of the Unknowable, resident protocol Part 3;
`constants_new.py::EARTH_D660_DEPTH_KM`.

## PENDING ACTION (Tony-side)

## C. RECONCILED LEDGER -- DONE (closed; for the record, do not re-do)

#### [L-217] The Part A / Part B dispatch split is a check that cannot fail
<!-- L:217 status:DONE upd:2026-08-19 section:C flag: rice:3/3/90/1 -->
- **Found by the reviewer it was meant to constrain, 2026-08-19.** The
  L-214 review prompt asked each model leg to answer Part A (derive
  your own structure) BEFORE reading Part B (critique ours), to stop
  the reviewer anchoring on Claude's proposal. Fable's disclosure: the
  prompt arrives as ONE document in ONE context, so there is no way for
  a model to write Part A without Part B already read, and NOTHING IN
  ANY ANSWER DISTINGUISHES A REVIEWER WHO COMPLIED FROM ONE WHO COULD
  NOT.
- **The corroboration is in the other leg.** GPT's A3 opens with "my
  prediction before consulting the measured result is" and then states
  the measured result to the digit. That is the tell. It is not GPT's
  fault -- the instruction asked for something the format made
  impossible.
- **This is an instance of the protocol's own CRITICAL gate**, A Check
  That Cannot Fail Is Not Passing, in the dispatch layer rather than in
  code. The prompt was authored in this session, so the gate did not
  fire on its own author.
- **Fable's remedy:** two physical dispatches. Part A sent alone,
  answer collected, THEN Part B sent. Anything less is the ritual
  without the check.
- **The related contamination finding, same review.** Fable ran INSIDE
  the Paloma's Orrery project and disclosed it unprompted: it carried
  resident memory of the protocol and the general state of the
  provenance work, though not the L-214 design conversation. The
  fresh-chat-outside-any-project rule exists for exactly this and was
  not followed for that leg. Its review was still the sharper of the
  two, which is worth noting and is not a reason to relax the rule.
**Note:** RICE is Claude's proposal, unratified.
- **CLOSED 2026-08-19. Tony's ruling: yes, do it.** The two-dispatch
  protocol is standing practice for any prompt that carries Claude's own
  proposal alongside a request for an independent derivation. Recorded
  in `provenance-discipline` 2.6, under Model Roles in the Competitive
  Pattern, which is the section that already owns Mode 7 dispatch
  mechanics and the skill that fires at dispatch time. The alternative
  host, `ledger-and-session-records`, owns document FORMAT (the anchor
  line, handoff shape); this is dispatch SEQUENCE, so it belongs beside
  the model-roles table.
- **What the rule says.** Either send Part A alone, collect the answer,
  and then send Part B -- or do not claim the split. A single document
  asking a model to answer one half before reading the other is a check
  that cannot fail, and stating the instruction is worse than omitting
  it, because the instruction makes the prompt look controlled.
- **The obligation this creates.** A mid-session reinstall cannot be
  verified from inside the session that makes it, so the NEXT session
  confirms its own loaded copy reads 2.6 before doing provenance work.
**Ref:** `documentation/REVIEW_PROMPT_L214_20260819.md` (the prompt
that carried the defect); `documentation/L214_REVIEW_RECONCILIATION_
20260819.md` Part 4; L-214; L-203 (the Visibility Convention, same
family of reasoning).

#### [L-212] maintenance_run names every file the run wrote
<!-- L:212 status:DONE upd:2026-08-19 section:C flag: rice:2/3/90/1 -->
- **Asked for by Tony, 2026-08-19**, after watching a run: "could we
  list the files that were modified by the run, by name? we list some
  but not all i believe." Correct. The four GENERATORS declare their
  outputs and their rows name them; the CHECKERS declare nothing, and
  five artifacts were being written every run with nothing on screen
  saying so -- `WORKSHEET_CHECK.md`, `data/worksheet_routed.json`,
  `documentation/prompts/citation_review.jsonl`, `PROVENANCE_AUDIT.md`
  and `data/provenance_history.json`.
- **As built** (`patch_L212_1_files_written`). A FILES WRITTEN THIS RUN
  block after the verdict summary, naming every changed file, split
  into written / created / removed / rewritten-with-identical-bytes.
  Printed on every run including one that changes nothing.
- **MEASURED, NOT DECLARED, and that was the design decision.** The
  obvious fix is an output list per checker matching the generators.
  That is a second store of a fact the tools already own, and it drifts
  in one direction only: the next artifact somebody adds is invisible
  again and nothing fails to report it. A tree snapshot before and
  after reports what actually happened, so a file written by a tool
  nobody declared still appears.
- **Cost measured before the design was chosen**, not after. A stat
  walk over 1,329 files is about 0.01 s; hashing everything at or under
  2 MB is about 0.13 s. Two snapshots cost roughly a third of a second
  against a run of 100 seconds or more.
- **The blind spot announces itself.** Files over 2 MB are compared by
  size and mtime rather than content, and the count of them prints
  every run. On Tony's machine that is 22 files; a same-size edit to
  one would read as touched rather than written, and the line saying so
  is what keeps that from being a silent gap.
- **Success carries evidence.** The block prints the number of files
  EXAMINED, not only the number changed. "Nothing was written" and
  "nothing was looked at" are otherwise the same sentence.
- **Found on its first outing**: `data/worksheet_check_state.json`,
  written by the checker every run and named nowhere.
- **A wrong reading, recorded.** The first sandbox run reported
  `test_output/test_orbit_paths.json` as REMOVED and Claude passed that
  to Tony as a finding. It was an artifact of the sandbox lacking
  astroquery, so `test_orbit_cache.py` failed and left the file
  deleted. On a working machine the same run reports it rewritten with
  identical bytes. The tool was right both times; the reading of it was
  wrong once, which is the failure mode a diff tool invites.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-188 (the runner); L-205 (the summary line this sits under);
`documentation/patch_L212_1_files_written.py`.

### Strategic status -- shell-consolidation + animation refactor (CLOSED, for the record)
(Moved from B. Strategic Status, 2026-06-22; no L-number, historical record. The animation
"final gate pending" noted below PASSED at L-004 / v4.1, June 17.)

**The shell-consolidation refactor is COMPLETE** (per v23 headline; all 13 bodies
route through SHELL_CONFIGS / CUSTOM_SHELLS -> create_celestial_body_visualization
-> build_sphere_shell -> create_info_marker). The project is in
cleanup-and-close, not mid-refactor. (June 11: the create_planet_visualization
wrapper is now RETIRED -- zero pipeline callers; see section C.)

**Animation refactor (21/51): CORE TRACK DELIVERED, final gate pending.**
- Phase 1 (frame fence + sun threading + first-frame sync) -- DONE
  `[render-confirmed Mode 5 @7977a11, June 10]`. 88-94% file reductions.
- Phase 2 (scene-assembly consolidation 2a-2d) -- DONE
  `[render-confirmed Mode 5, June 10-11]`. Closed N3 + O5 + O6(a); two fixes
  shipped during testing (incl. osculating labeling, idealized_orbits)
  `[per chain]`.
- Phase 2.5 (wrapper retirement, 3 sites) -- DONE
  `[render-confirmed Mode 5 via Session A gate, June 10]`.
- Phase 3 Session A (design doc + 3a + budget harness) -- DONE
  `[render-confirmed Mode 5, June 10]`. Rebuild-as-universal adopted;
  gate 5(a) bytes PASSED at measured reduction.
- Phase 3 Session B (per-frame engine + axis/cone/indicator + greyed-legend
  disclosure) -- CONDITIONALLY render-confirmed June 11: engine allocates,
  rebuilds, budget-reports correctly; riding behavior visually confirmed at
  planet-centered scale; solar-system-scale visual confirmation blocked by a
  TOOLING gap (camera tracking; item 19), not an engine defect.
- Phase 3 Session C (barycenter Sun fix, console-spam fix, opt-in per-frame
  comet tails, sodium tail, U+N bow-shock disclosure, one-line auto-scale) --
  DELIVERED and PUSHED @7b71c29, `[render-gated on protocol v4]`.

**Movement 1 (bow shocks + magnetosphere nest) COMPLETE** (v24). `[per chain]`

**Movement 2 (pole-frame consumers) COMPLETE pending one gate:** rotation-axis
primitive (11 bodies, v26) and dipole cones (Uranus/Neptune, v27) done; the
v27 "animation gap" resolved -- center bodies confirmed O4 (June 10), and
NON-center bodies now animate via the Phase-3 engine (Session B). The
bow-shock hover disclosure remainder was delivered in Session C
`[render-gated C5]`.

**N15 ring-plane migration COMPLETE** (v25). `[per chain]`
**Analytical moon-orbit retirement DONE** (v25). `[per chain]`
**Provenance Tier-1 = 0** -- RE-CONFIRMED June 11 post-campaign
`[verified @d9460e2: PROVENANCE_AUDIT.md, 109 files scanned, 497 findings,
Tier-1 FIX NOW = 0]`. The clean mark held through the entire animation
refactor.

---

From v23 DONE table (closed by D1/D2/D3.1/C1; `[per chain]`):
1 Sun config extraction; 4 sun_position wiring (static); 10 double sun direction
indicator; 11 Earth/Jupiter magnetic_tilt_deg; 12 Neptune poles -> square-open;
14 Neptune debug print; 15 Neptune function-local imports; 16 Venus hover text;
25/42 Mars magnetosphere info marker; 27 hover \n -> <br>; 29 Sun call-site
switchover; 31 sun/corona Tkinter format; 32 Sun marker borders; 33 photosphere
mesh3d; 34 photosphere hover truncation; 35 corona_from_distance retired; 43/44
Uranus/Neptune magnetosphere hover truncation; 45 Neptune radiation labelling;
46 Neptune FAC labelling; 47a/47b Neptune arc / Lassell+Arago superimposed;
48 Mercury sodium-tail sun_position; 50 sun-direction per-body legendgroup;
54 hovertext/legendgroup sweep; 55 solar shell naming; 56 crust/cloud
legendgroup; 57 Neptune double-leader; 58 MAPS placeholder legendgroups;
59 create_neptune_magnetic_poles orphan; 60 Moon Hill Sphere prefix;
N1 osculating-marker "color not defined"; 36/39 Neptune/Uranus provenance Tier-1
display strings; 53 Neptune magnetic-center marker -> square-open;
N2-orphan Uranus dipole SIGN closed by convention.

Closed SINCE v23 (Movement chain + verified):
- **24 Bow shocks (all 8)** -- DONE (v24). **Magnetosphere nest sizing** -- DONE
  (v24). **U3 Uranus 105-deg fudge** -- RETIRED `[verified @76c330e]`.
  **N15 ring-plane migration** -- DONE (v25). **Analytical moon-orbit
  retirement** -- DONE (v25). **Rotation-axis primitive** (11 bodies) -- DONE
  (v26). **N13 dipole sweep-cone** -- DONE (v27). **N12 pole markers** -- DONE
  (June 7). `[all per chain unless tagged]`
- **Double 'Sun' in the center dropdown** -- DONE `[verified @730b2bf, L9296]`.
- **Duplicate 'Sun' key in CUSTOM_SHELLS** -- DONE `[verified @730b2bf via AST]`.
  (Full root-cause narratives for both retained in the June-8 entry of the
  prior ledger edition; reachable in git history.)
- **21/51 PHASE 1** (frame fence + sun threading + first-frame sync) -- DONE
  `[render-confirmed Mode 5 @7977a11, June 10]`. P1 4818->271 KB (94.4%),
  P2 5133->593 KB (88.4%); Sun Direction indicator un-suppressed in
  animations; magnetotail oriented at frame 1. Companion artifacts in repo:
  measure_animation_html.py, ANIMATION_TEST_PROTOCOL (v4 current).
- **21/51 PHASE 2 (2a-2d)** -- DONE `[render-confirmed Mode 5, June 10-11]`.
  One canonical center-body marker (add_celestial_object via
  add_center_body_marker); explicit blocks deleted in BOTH pipelines; one
  sun-position producer (resolve_shell_sun_position); one center-shell
  dispatch (add_center_body_shells); one shell-vars map
  (get_planet_shell_vars_map, replaced three copies); osculating params
  threaded through marker hover. Net -36 lines. P2-7 correction recorded:
  barycenters render as open squares with full hover + legend, correct
  as-is (the transparency-suppression expectation in the checklist was
  wrong, not the code).
- **N3 center-marker double** + **O5 animate bare hover** + **O6(a) animate
  no-marker-with-shells** -- CLOSED by Phase 2a (one disease: two marker
  mechanisms in static, one in animate, no canon). `[render-confirmed]`
- **D.Structural 3: create_planet_visualization RETIRED** -- DONE
  `[render-confirmed via Session A gate, June 10]`. THREE call sites swapped
  to the unified dispatch (NOT one -- the prior "one-site" ledger claim was
  wrong; corrected by repo-wide grep June 10); non-center sites now pass the
  TRUE center_object (the wrapper's own promised Phase-D correction;
  live-characterized identical). Wrapper annotated dead; deletion rides
  D.Structural 6. helpers' dead import joins D.Structural 5/6.
- **21/51 Phase 3 SESSION A** (3a notices + retirement + design doc +
  measurement harness) -- DONE `[render-confirmed Mode 5, June 10]`.
  Rebuild-as-universal adopted (ANIMATION_ENGINE_DESIGN_v1.md); gate 5(a)
  bytes PASSED: reduced magnetosphere composite 62.4 KB/f -> 1.81 MB @29f
  (envelope un-reduced; ~1.4 MB after the create_magnetosphere_shape
  producer promotion). measure_perframe_elements.py in repo.
- **21/51 Phase 3 SESSION B** (per-frame engine; axis + dipole cone +
  sun-direction indicator riding non-center bodies; greyed-legend
  disclosure) -- CONDITIONALLY render-confirmed June 11 @e5fd86d. Engine
  architecturally sound (allocation, rebuild, budget guardrail, stability
  assert all confirmed); riding visually confirmed at planet-centered scale
  (B3: Sun's axis rides the Sun marker); solar-system-scale visual gap is a
  TOOLING item (camera tracking -> item 19), not an engine defect.
  Greyed-legend (`visible='legendonly'` + legendrank + italic note)
  ACCEPTED (B4); click wart acceptable. 14 per_frame registry tags.
- **RESET BUTTON + center-dropdown trace-storm guard** -- DONE
  `[render-confirmed Mode 5, Tony, June 15 @6c5c3b]`. Top-bar Reset (date_frame
  row 0 col 11, next to Vernal Eq) behind a confirm dialog returns the GUI to
  STARTUP state. Two Mode-1 snippets into palomas_orrery.py (handler
  reset_all_selections ~8212; button ~8605) + new file test_reset_completeness.py.
  Option A; shells cleared by a COMPLEMENT-SET SWEEP (the SHELL_CONFIGS/
  CUSTOM_SHELLS registry covers only 78 of 113 -- Sun 19/Earth 12/belts 4 are
  hand-coded). Runtime-proven total: 310 IntVar names -> 309 distinct objects
  (frag_var aliases comet_2025k1d_var); the sweep targets exactly 117 vars, ALL
  declared-default 0; the only default-ON vars (show_apsidal_markers_var,
  show_closest_approach_var = 1) are handled in the named set, never swept.
  Completeness lives in the TEST (dirty-all -> live handler -> assert all 309
  IntVars + 3 StringVars + 10 entries restored), not in an over-built registry.
  GUARD: the objects loop fired update_center_dropdown's per-object 'write' trace
  ~182x/click (the `[CENTER MENU] Dynamic centers: Sun + ['Sun']` flood); a module
  flag `_reset_in_progress` + early-return guard (palomas_orrery.py ~10280/10287)
  + one explicit end-of-handler rebuild after center->Sun cut it to 1 rebuild AND
  clears a lingering pre-reset center. Storm absence render-confirmed by Tony.
  MAP CORRECTION: the 4 "stragglers" (arrokoth_new_horizons_var, dw_var, kbo_var,
  voyager1h_var) are DEAD/unwired; the live "2024 DW" var is asteroid_dw_var
  (already in the 182 objects); the sweep re-zeros the dead 4 harmlessly (D-sweep
  candidates).


#### [L-004] Apply C2 fix pass + run ANIMATION_TEST_PROTOCOL_v4_1, push
<!-- L:004 status:DONE upd:2026-06-17 section:C flag: -->
- **Apply the C2 fix pass (2 files) and run ANIMATION_TEST_PROTOCOL_v4_1**
  (the focused retest of C2/C6d + regression), append results to the 3C
  handoff, push. On pass: the Phase 3 CORE TRACK (Sessions A/B/C + fix
  pass) is COMPLETE -- move the marked render-gated items below into
  section C and update 21/51. (v4 first run, June 11: C1/C3/C5/C7 PASS,
  C4 pass-with-caveat, C2/C6 blocked by the three bugs below -- all
  three root-caused and fixed in pass C2.)
**Note (2026-06-17):** v4.1 gate COMPLETE. C2 PASS (Halley: no doubling,
  comet details correct, Sun tracking works). C6d PASS (Mercury-centered
  29-frame animation: Sun tracks correctly). O16 PASS WITH NOTE (auto-scale
  ~1 AU; root cause logged on L-056 -- positions={} fallback, pre-existing,
  workaround via 19.3 Phase B). MAPS tail non-animation BY DESIGN.
  Phase 3 CORE TRACK COMPLETE. L-007 (bow-shock disclosure) moves to C
  this pass. DONE.
**Gap:** none -- move to section C.

#### [L-005] Commit protocol v3.28 (or v3.29) to repo root
<!-- L:005 status:DONE upd:2026-06-17 section:C flag: -->
- **Commit protocol v3.28 (or v3.29 with the candidates above) to the repo
  root.** `[per chain; not re-verified June 11]`

- (CLEARED June 11) Phase 2, Session A, Session B, and Session C are all AT
  HEAD (chain above); no code push outstanding.

**Note (2026-06-17):** v3.28 confirmed committed @8e0f228. DONE -- move to C.
**Gap:** none -- move to section C.

---

#### [L-010] Keplerian epoch parse fails on 'osc.' suffix
<!-- L:010 status:DONE upd:2026-06-12 section:C flag: -->
- **`[KEPLERIAN POS] Could not parse epoch date` with 'osc.' suffix**
  -- FIXED in Phase 4 (June 12) `[render-gated]`. The apsidal_markers
  chain gained the missing '%Y-%m-%d %H:%M' form (the suffix WAS being
  stripped; the HH:MM format was not in the chain). The fix uncovered
  the worse half: FOUR sites in palomas_orrery.py used the same broken
  chain with a SILENT J2000 fallback -- a wrong-position failure, not
  console noise. All four now route through _parse_osc_epoch (one
  producer, three formats) with a loud [EPOCH] note before any J2000
  fallback. Smoke-tested (all three Horizons forms + garbage -> None).
**Note (2026-06-17):** DONE items stay in their section until a housekeeping
  pass moves them to C -- they provide a readable trail without jumping to
  the archive. When Gap says "none -- move to section C" that is the
  housekeeping trigger. render-confirmed Mode 5 is EVIDENCE of correctness,
  not a disposition -- a DONE item can be render-confirmed; an OPEN item
  can also be render-confirmed on a partial fix. Moving to C this pass.
**Gap:** none -- move to section C.

#### [L-011] Pass-C2 v4 blockers (3) + B3-bonus barycenter Sun bug
<!-- L:011 status:DONE upd:2026-06-11 section:C flag: -->
- FIXED in pass C2 (June 11, `[render-gated v4.1]`), three v4 blockers:
  * **C2a frame-1 comet doubling** -- the pre-existing frame-1 tail
    block AND the engine both added the comet's traces (incl. the
    builder's own Sun Direction). Fix: frame-1 block skips
    engine-owned comets (opt-in on, non-MAPS); the engine's
    allocation IS frame-1 content.
  * **C2b/C2c vanishing tail/indicator** -- STICKY-VISIBLE MERGE:
    Plotly applies frame traces as a MERGE; builders omit 'visible',
    so a slot once dummied to visible=False never reappeared. Tails
    filled previously-dummied slots exactly at perihelion; the
    indicator reshuffled into a dead slot when variable counts grew.
    Fix: EXPLICIT visible on every slot write (normalizer); the
    missing-position branch now writes explicit dummies + a console
    note (was a silent blanking). LESSON: frame updates are merges --
    any property a builder omits inherits the slot's history; padding
    slots with invisible dummies REQUIRES explicit visibility on
    every later write.
  * **C6d Mercury-centered Sun tracking** -- the engine excluded the
    center body entirely, but a centered body's SUN-DIRECTION
    elements must track the Sun moving around it; frame-1 freeze
    there is a physics lie. Fix: get_center_engine_elements() is the
    single source of truth -- the dispatch SKIPS that set
    (skip_elements threading, static unaffected, regression-tested
    identical) and the engine adds matching center_fixed specs
    (origin position, per-frame Sun). Inertial elements (axis, cone)
    correctly stay frozen. The B3-bonus barycenter Sun-Direction bug (indicator
  pointed at (0,0,0)/the barycenter when the Sun checkbox was off) was FIXED
  in Session C `[render-gated C1]`: the engine resolves a REAL Sun trajectory
  (fetching it when unchecked) and SUPPRESSES sun-direction elements when
  unresolvable -- it never points at a placeholder. Root cause for the
  archive: a fallback value is a CONTRACT -- (0,0,0) was a rotation-skip
  sentinel to shell-orientation code and literal position data to the
  indicator; reusing a fallback without checking each consumer's semantics
  is how a sentinel becomes a physics bug. Suppression beats fabrication.
**Note (2026-06-17):** v4.1 gate PASS -- C2 confirmed on Halley animation
  (no doubling, comet details correct, Sun tracking works). C6d confirmed
  on Mercury-centered 29-frame animation (Sun tracks correctly).
  MAPS tail non-animation is BY DESIGN (excluded per ADDENDUM_phase4
  decision 1). Moving to C this pass.
**Gap:** none -- move to section C.

#### [L-026 | #9] palomas_orrery_helpers.py CRLF -> LF
<!-- L:026 status:DONE upd:2026-07-15 section:C flag: rice:3/2/75/2 -->
File confirmed CRLF (verified this session @7964193). Functional no-op
to convert, but the diff touches every line, so best as a standalone
commit with no other changes.
**Gap:** convert CRLF -> LF (binary-mode script or dos2unix). Do as
isolated commit. Low risk but noisy diff.
**Platform neutrality (the larger goal):** part of a general codebase LF-conversion sweep;
keeps the project platform-neutral across Windows / macOS / Linux. Pairs with L-027.
**Tony:** Done. 

#### [L-055] O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium particle count)
<!-- L:055 status:DONE upd:2026-06-17 section:C flag: -->
- O14/O15 verdicts arrive with the v4 gate (comet legend churn; sodium
  particle count) -- record here if either becomes an item. O15 may be
  settled by rounding (500 particles now ~31 KB/f).
**Note (2026-06-17):** v4.1 gate run: O14/O15 not observed as blocking issues
  during Halley animation test. No new items opened. DONE -- move to C.
**Gap:** none -- move to section C.

#### [L-018 | #8] Dead create_sun_direction_indicator imports (verify remainder)
<!-- L:018 status:DONE upd:2026-06-18 section:C flag: -->
Sole dead import was in palomas_orrery_helpers.py (line 52); removed.
Remainder verified: planet_visualization.py (L512 caller) and
palomas_orrery.py (L2298/L2363 callables) are live. No dead imports remain.
**Gap:** none -- move to section C.
**Ref:** grep confirmation + patch_dead_imports.py [verified @feab717].

#### [L-022 | #40] Asteroid belt hover -> single info marker
<!-- L:022 status:DONE upd:2026-06-18 section:C flag: -->
All four belt geometries (main, Hilda, Trojan L4, Trojan L5) use
create_info_marker() factory with hoverinfo='skip' on geometry traces.
Completed during Stage 3 sweep + Phase 1 re-pipe (May 27-29, 2026).
Documented in module docstring.
**Gap:** none -- move to section C.
**Ref:** asteroid_belt_visualization_shells.py docstring [verified @7964193].

#### [L-019 | #13] Neptune ring info-marker rotation (verify + close)
<!-- L:019 status:DONE upd:2026-06-18 section:C flag: -->
Original concern: ring info markers might not be rotated correctly to
match ring geometry. Code now uses x_final[0], y_final[0], z_final[0]
from the rotated ring points -- same transform as the ring geometry itself.
Fix documented in neptune_visualization_shells.py docstring (Stage 3
sweep, May 27-28 2026).
**Note:** visual verification (Mode 5 render) to confirm markers sit on
their rings, then close. Zero code risk.
`**Gap:** none -- move to section C`

#### [L-021 | #28] Neptune superimposed info markers (verify + close)
<!-- L:021 status:DONE upd:2026-06-18 section:C flag: -->
Original concern: multiple Neptune info markers (magnetosphere, bow shock,
radiation belts, ring system) might overlap visually. The Stage 3 sweep
(May 27-28 2026) fixed the degenerate X-axis-rotation bug where all ring
markers collapsed to one position.
**Note:** visual verification (Mode 5 render) -- confirm markers at
distinct positions. Zero code risk.
`**Gap:** none -- move to section C`

#### [L-023 | #N2] Saturn/Uranus ring marker placement
<!-- L:023 status:DONE upd:2026-06-18 section:C flag: -->
Original concern: ring info markers at wrong positions. Both modules
document a fix for the "Neptune 2C pattern -- previously all rings shared
one degenerate X-axis-rotated marker" (Stage 3 sweep, May 27 2026).
Markers now use first point of rotated ring geometry.
**Note:** visual verification (Mode 5 render) -- confirm ring markers sit
on their respective rings. Zero code risk. Likely DONE.
`**Gap:** none -- move to section C`

#### [L-024 | #N4] Planet 9 sphere n=50 -> 20/25
<!-- L:024 status:DONE upd:2026-06-18 section:C flag: -->
Planet 9 surface now uses mesh_resolution=24 (mesh3d geometry). Hill sphere
uses n_points=20. If the original concern was n=50 being too dense, the
current values (20-24) appear to address it.
**Note:** verify that no Planet 9 shell still carries n=50. If all are at
20-24, close. Zero code risk.
`**Gap:** none -- move to section C`

#### [L-029] v25 D3 dead-code annotations + small-body analytical tail
<!-- L:029 status:DONE upd:2026-06-18 section:C flag: -->
Zero DEAD/UNUSED/ORPHAN/RETIRED annotations found in palomas_orrery.py.
3 RETIRED annotations in planet_visualization.py (covered by L-016).
No "analytical tail" references found in codebase. This item may be
stale -- the original v25 dead-code work may have been completed or
absorbed by the Phase 3 sweep.
**Note:** verify whether any actionable content remains. If not, close
as absorbed. If the "small-body analytical tail" refers to a specific
feature, needs clarification from Tony.
`**Gap:** none -- move to section C`

#### [L-006] Mercury +0.2 R_M northward dipole offset
<!-- L:006 status:DONE upd:2026-06-20 section:C flag: rice: -->
- **Mercury +0.2 R_M northward dipole offset** -- DONE. (Anderson 2011;
  v24 Movement-2 item.) `[verified absent @76c330e]`
  **Done (2026-06-20, built @5b294c8 -> pushed @08f9831, Mode-5 confirmed):**
  offset_fraction 0.19 R_M northward implemented in PLANET_DIPOLE +
  build_dipole_cone_traces (axial; Anderson et al. 2011, MESSENGER). Mercury
  renders as the degenerate axis-line (tilt 0, option a). This IS the +0.2 item
  -- Anderson reports 0.19 +/- 0.01 R_M.
  **Gap:** none -- move to section C

#### [L-009] Dipole cluster: envelope tie / offset direction / remaining cones / half_len_frac
<!-- L:009 status:DONE upd:2026-06-20 section:C flag: rice: -->
- **Envelope -> dipole tie / season-derived roll** (Mode-7, conditional);
  **dipole offset DIRECTION** (Mode-7; apex stays centered until sourced);
  **REMAINING DIPOLE CONES** (verified set, June 13 @33aac56): the cone
  exists on Uranus + Neptune (done -- the dramatically tilted/offset
  dipoles, where the swept envelope matters most). Of the eight bodies
  with a magnetosphere, the candidates still WITHOUT a dipole_cone, on
  physics, are Earth, Jupiter, Mercury (genuine tilted/offset global
  dipoles -- Tony's named set) plus Saturn (MARGINAL: dipole aligned to
  <1 deg of the spin axis, so the swept cone is near-degenerate; earns the
  element only weakly). EXCLUDED on physics: Mars (crustal fields, no
  global dipole) and Venus (induced magnetosphere, no internal dynamo).
  PROVENANCE GATE unchanged: all dipole tilts are currently RECALLED and
  MUST be sourced before any PLANET_DIPOLE entry (Fetched-vs-Recalled) --
  show the envelope, but the tilt that SETS it must be cited, not
  remembered. **per-body half_len_frac tuning** (Mode-5 knobs).
  `[verified set @33aac56]`
**DONE (2026-06-22, verified in code @26e58b2):** all six magnetosphere bodies carry a
SOURCED dipole_cone in CUSTOM_SHELLS (Mercury, Earth, Jupiter, Saturn, Uranus, Neptune);
implementation + provenance gate cleared. The body text above is the June-13 state, now
superseded. Only the rolling-cone coupling remains -- tracked as L-061.
**Done (2026-06-20, built @5b294c8 -> pushed @08f9831, Mode-5 confirmed):**
  REMAINING DIPOLE CONES sub-part CLOSED -- Mercury, Earth, Jupiter, Saturn
  dipole_cones built + rendered (handoff v30). Offset MAGNITUDE sourced and
  applied AXIALLY (northward along spin pole): Mercury 0.19, Earth 0.085,
  Jupiter 0.12, Saturn 0.045 R_p (peer-reviewed; Gemini de-novo June 18).
  Mercury + Saturn render as the degenerate axis-line (tilt ~0, option a);
  Earth + Jupiter as full swept cones (9.6 / 10.3 deg). half_len_frac: existing
  values Mode-5-confirmed acceptable, no dedicated tuning needed. L-006 closed
  in parallel. Smoke PASS @08f9831; provenance Tier-1 = 0.
**Closed by decision (2026-06-20):** the swept cone (the FAST sweep of the
  dipole axis about the spin axis) + the axial offset are the honest, legible
  object, and they are DONE. No remainders are kept on this item -- the slower
  frame-coupling motions are promoted to L-061 (magnetosphere-dipole frame
  coupling / seasonal roll), because they are new physics, not unfinished cone
  work, and a closed number should not smuggle separate work as a footnote.
  ("No element needs to exist; it earns its place by what it teaches"; access
  is not understanding.)

  THREE MOTIONS, THREE TIMESCALES (kept for the record; only #1 is this item):
  1. DIPOLE AXIS about the spin axis -- FAST, one rotation (hours-days). DONE:
     this IS the cone; instantaneous azimuth unknowable -> draw the whole sweep.
  2. OFFSET lateral direction -- MIXED (longitude-locked fast; Earth secular,
     over decades). Axial magnitude shipped; lateral part small vs cone scale.
     -> L-061.
  3. ENVELOPE -> dipole SEASONAL ROLL -- SLOW, one orbit; invisible in a static
     plot. -> the core of L-061.
**Gap:** none -- move to section C

#### [L-036] O11 greyed-legend display-name verdict: NO item needed
<!-- L:036 status:DONE upd:2026-06-11 section:C flag: rice: -->
- O11 verdict June 11: greyed-legend display names derive correctly from
  checkbox keys -- NO item needed; recorded so it is not re-raised.
**Gap:** none -- move to section C

#### [L-041] Item 19.3 axis-control round trip (P1/P2/Phase A/Phase B + toggle follow-on)
<!-- L:041 status:DONE upd:2026-06-16 section:C flag: rice: -->
- (June 14 DESIGN, no code) Orrery-side axis control (item 19.3) scoped +
    handed off: HANDOFF_item19_axis_control_orrery_v1.md, built on 1288b51 /
    gallery 2f40d9d. DECISION (a2): scene-dict extraction only (axes +
    aspectmode + camera + domain, verified byte-identical across the 5704/7940
    twins); layout envelope (title/annotation/legend/margin/footer) NOT merged
    -> divergence-audit seed (4 catalogued divergences in the handoff). Full
    function-body merge stays off the list. FINDING: _track_axis (7652) is
    already the complete, correct spec (range + autorange=False + dtick +
    styling); the two MAIN paths (5704/7940) under-specify (no dtick /
    autorange) -- THAT is the close-approach unreadability. Feature =
    generalize the track spec to the under-specified sites via
    build_scene_axes/build_scene, dtick from the SHARED
    visualization_utils._calculate_grid_dtick (provable Studio parity). Q2:
    auto-only first cut (auto dtick + non-Sun-center range autofit IF the
    existing range logic doesn't already fit extent); user GUI fields = fast
    follow. Q3 matrix: range never overrides S3(exoplanet)/S4(track); dtick
    lands on S1/S2 first; S4 already correct. Two-phase: P1 byte-identical
    extraction (Mode-5 zero-change gate), P2 turn on dtick+range (Apophis
    render gate). Confirm-at-impl: read get_improved_axis_range /
    get_animation_axis_range (range-autofit scope), _track_dtick source
    (parity routing), Studio round-trip (no double-apply).      
- (June 15) Item 19.3 Phase 2 COMPLETE. auto_dtick + autorange=False landed on
  S1/S2 via build_scene. Base 7aecc3b -> bd768ee (builder) -> aa1a4cd (call sites).
  build_scene gains auto_dtick (derives dtick from the range span via the SHARED
  visualization_utils._calculate_grid_dtick -> provable Studio parity) + an
  axis_range=None guard (emit neither dtick nor autorange when no range exists).
  Headline fix verified: close-approach cubes now readable -- e.g. 0.0008 AU span
  -> 0.0001 AU dtick (~15,000 km gridlines) instead of effective dtick=1. Default
  build_scene call stays byte-identical, so Phase 1 untouched. Render gate (Tony,
  Mode 5, aa1a4cd): static close-approach readable; everyday full-system plots fine
  with explicit ~6-gridline dtick (intended, visible change: auto_dtick applies to
  ALL S1/S2 plots).
  FINDING: the load-bearing non-tracking animation-hold test PASSED -- autorange=False
  on the up-front once-set scene SUPPRESSES Plotly per-frame autorange (grid/range
  held across frames). This validates the "real fix (autorange suppression)" named
  in the palomas_orrery.py June-13 note (~7847) FOR THE NON-TRACKING PATH. BOUNDARY:
  does NOT resolve the camera-tracking (S4) per-frame autorange residual (separate
  dedicated-session item; _track_axis untouched). Two distinct problems; only the
  non-tracking one is closed.
  Also folded in: removed the duplicate _calculate_grid_dtick() docstring line
  (Phase-1 insertion artifact). Cosmetic residuals: trailing whitespace on
  palomas_orrery.py 5711/7927; MODULE_ATLAS.md lags (auto_dtick absent) -- regen
  when convenient.
  19.3 Phase 1 (extraction) + Phase 2 (dtick/autorange) done. Fast-follow remains:
  user-settable range/dtick GUI fields (orrery + Studio round trip); S3 exoplanet
  opt-in.   
- (June 16) Item 19.3 Phase A COMPLETE -- user-settable dtick GUI field
  (orrery generation side). Base 30840b1 -> 1c08a8a (one transactional patch,
  7 edit groups, all palomas_orrery.py, Mode 1). Blank field = Phase 2
  auto_dtick; >0 overrides, threaded to all three live build_scene sites
  (S1 ~5720, S2 ~7955, S3 ~5998, AST-confirmed 3/3). Orrery already had a
  user-settable RANGE (custom_scale_entry); this fills the missing DTICK.
  Studio half of the round trip was ALREADY DONE @2f40d9d (March) -- this
  added the orrery half, not Studio.
  S3 PARALLEL-PIPELINE FIX: exoplanet STATIC scene (bare inline scene=dict,
  AU-coarse grid) migrated to build_scene, matching exoplanet ANIMATION
  (already on S2 build_scene). update_layout merges -> camera/domain/theme
  preserved; build_scene_axes emits same X/Y/Z (AU) titles. Verified static
  AND animated (Proxima ~+/-0.0583 AU).
  CORRECTION (Observation Override): the design-stage "manual dtick is a no-op
  under Auto scale" caveat was WRONG. calculate_axis_range_from_orbits /
  get_animation_axis_range never return None (concrete fit, or [-1,1]
  fallback), so axis_range is always a concrete cube -> dtick applies under
  Auto AND Manual, matching Tony's Studio experience. No logic changed; only
  tooltip + 4 comment blocks corrected. build_scene None-guard (481-483) is
  defensive only.
  S4 (camera-track) deliberately EXCLUDED -- computes its own _track_dtick;
  the Phase-2 per-frame-autorange boundary holds.
  Render gate (Tony, Mode 5, 1c08a8a): ALL 6 PASS -- regression, Auto+finer
  dtick, Manual close-approach, S3 exoplanet (static+animated), animation
  hold, Reset clears.
  Fast-follow REMAINING -> Phase B: Studio read-on-load (populate
  scene_axis_range/scene_dtick fields from the loaded figure's baked grid so
  the round trip is VISIBLE). Open decision: km-suffix on axis titles
  (annotate vs match orrery). Handoff: HANDOFF_item19_3_phaseA_dtick_gui.md.
  Pre-existing observation (NOT Phase A): exoplanet-animation
  "id_type (host_star) not allowed" ValueError on host-star trajectory fetch
  -- confirm if tracked.
 (June 16, item 19.3 Phase B SHIPPED) Studio read-on-load round trip,
gallery tools/gallery_studio.py, built on 2f40d9d / orrery c28eec0.
New shared reader _read_scene_grid_from_figure; both _do_load branches
populate scene_axis_range/scene_dtick from the figure (D3 precedence:
explicit studio override wins, else figure); _extract_encounter_data
routed through the same reader (+ figure dtick now surfaced in the
read-only panel). D1 RECONCILED to the live bytes: the handoff's
half-extent gate did not match the live dtick-keyed suffix; OPTION B
chosen (KM_SUFFIX_MAX_AU = 0.01 emit gate on half-extent, dtick tiers
kept inside, range-auto fallback). Closes the item-19.3 round trip
(orrery bakes -> Studio reads + refines). Render-gate items in handoff
sec 5. Optional later: orrery also emitting the suffix under the same
cutoff (full title parity) -- NOT this item.
(June 16, item 19.3 Phase B follow-on, from the render-gate observation)
DEFAULT_CONFIG show_axes / show_grid / show_modebar flipped False -> True
(gallery tools/gallery_studio.py, landscape editorial baseline), pushed at
812c05f. Tony's call: the boxes should reflect what the orrery HTML
produces on load AND these defaults should display across the other modes
("I always turn them on"), so the global default was flipped rather than a
surgical raw-branch-only set. Blast radius = every path that seeds from
DEFAULT_CONFIG (app startup, Reset Defaults, landscape preset, orrery-mode
entry, raw-orrery load) now starts with axes/grid/modebar on. Studio
exports UNAFFECTED -- they carry their own saved toggle states in
_studio_config, which override the default on load. show_modebar=True is
safe vs non-Plotly input: Studio only ingests Plotly figures (others bounce
at load), and show_modebar is only the exported HTML's Plotly
displayModeBar flag -- never touches a tkinter window. 
**Ref:** HANDOFF_item19_3_phaseB_studio_readonload.md; SHA chain 7aecc3b -> ... -> gallery 812c05f
**Gap:** none -- move to section C

#### [L-054] Gate 5(b): full resolution ships, rounded -- render-confirmed
<!-- L:054 status:DONE upd:2026-06-13 section:C flag: rice: -->
- **Gate 5(b)** RECAST (June 12); RENDER-CONFIRMED (June 13) `[render-
  confirmed Mode 5]`: full resolution ships, rounded. Tony's June-13 pass
  on live Mercury data confirmed (1) animated magnetosphere correct (tail
  anti-sunward across frames, no seam/flicker at d7 rounding); (2) camera
  tracking frames the active elements (element-extent window: tail opens
  it, magnetosphere tightens it); (3) tracked playback centers steadily on
  the body (cube-size wobble noted acceptable, see camera-tracking RESIDUAL);
  (4) indicator clamp renders sensibly; (5) inertial-note hover wording.
  Mercury-centered AND Sun-centered-track-Mercury both confirmed; saved-file
  round trip confirmed identical to live render.
**Gap:** none -- move to section C

#### [L-057] Animation auto-scale-vs-shells + Phase 3 tier decision -- CLOSED
<!-- L:057 status:DONE upd:2026-06-11 section:C flag: rice: -->
(CLOSED June 10-11: animation Auto-scale-vs-shells -- implemented as
max(orbital, shell) in Session C, render-gated C6. Phase 3 tier decision --
tier 2 adopted at the June-10 GO; tier 1 dropped; tier 3 = the resolution
follow-on behind gate 5(b).)
**Gap:** none -- move to section C

#### [L-007] Bow-shock hover disclosure remainder
<!-- L:007 status:DONE upd:2026-06-11 section:C flag: rice: -->
- **Bow-shock hover disclosure remainder** -- DELIVERED Session C
  `[render-gated C5]`: U+N bow-shock hovers now carry the conic-model
  sourced-vs-schematic note + the animation-freeze line (this also closes
  the Phase-1 orientation-freeze disclosure rider and the frame-1-freeze
  rider -- one sweep, three siblings, as designed). MOVE TO C on the v4
  gate pass.
**Gap:** MOVE TO section C on the v4 gate pass (L-004).
**Tony:** L-004 is done. 
**Gap:** none -- move to section C

#### [L-003] Protocol amendment candidates (for v3.29)
<!-- L:003 status:DONE upd:2026-06-22 section:C flag: rice:3/3/90/1.5 -->
- **Protocol amendment candidates (for v3.29; from the animation refactor):**
  - The xvfb SystemButtonFace<->gray90 sed round trip is NOT idempotent on files
    that natively contain gray90 (palomas_orrery.py has 26 native gray90
    literals). Rule: run the swap on a THROWAWAY copy only; never
    restore-in-place on the deliverable. (Caught June 9; applied as practice
    in every session since.)
  - Full-module exec under xvfb with tk mainloop suppressed enables LIVE-dispatch
    tests inside the real module namespace (real tk vars, real builders, network
    calls patched). Used as the standard verification gate for Sessions
    Phase 2 through 3C; candidate for the Agentic Pre-Test section.
  - `grep -c` exits 1 when the count is 0, silently BREAKING an `&&` chain --
    a downstream verification command can simply never run while the output
    looks complete. Rule: never put `grep -c` mid-chain with `&&`; run
    verification greps standalone or with `;`. (Caught June 10 -- one residual
    check did not execute until re-run standalone.)
**Gap:** none -- move to section C

#### [L-002] Protocol -> Skills refactor (process/tooling)
<!-- L:002 status:DONE upd:2026-07-04 section:C flag: rice:3/3/50/3 -->
- **Protocol -> Skills refactor (process/tooling, not orrery code).** Lift the
  task-triggered PROCEDURE/CONVENTION layer of Part 3 into Anthropic SKILL.md
  files (load on demand); keep the JUDGMENT layer (modes, criticality,
  anti-patterns, Foundation, double-helix) resident. Sketch-first /
  design-before-build -- the framing below is the leg-up from the v3.29 cleanup,
  NOT the design itself.
- **Sorting principle (the design lever):** a skill only helps if its trigger
  fires at the moment of need. So the cut is NOT QUALITY-vs-CRITICAL and NOT
  procedure-vs-judgment -- it is "does the moment-of-need announce itself in the
  task?" Task-coupled guidance (writing hover text -> AU convention) extracts
  cleanly; checkpoint guidance that must fire UNPROMPTED (session start, every
  delivery) can't be a skill -- nothing in the request triggers it -- so it stays
  resident by standing instruction.
- **Three buckets (v3.29 Part-3 inventory; illustrative, not the final set):**
  (A) EXTRACT -- task-triggered conventions/procedures: docstring standard,
      single-info-marker, marker-symbol, hover-AU, 3D-axis, Horizons centers,
      provenance-scanner mechanics, a safe-editing bundle (bottom-up + binary-mode
      + file-encoding), platform-neutrality, credit-line, barycenter.
  (B) RESIDENT POINTER + skill body -- CRITICAL but task-coupled: Agentic Pre-Test
      (a resident one-liner fires it; the commands + live-dispatch smoke test live
      in the skill).
  (C) STAY RESIDENT -- checkpoint CRITICAL gates, never extract: SHA round trip,
      uploads-before-project, enumerate-uploads, verify-base, verify-execution,
      check-parallel-pipelines, fetched-vs-recalled, show-the-envelope; + Parts 1/2/4.
- **COMPLETED July 4, 2026.** Designed with Claude Opus 4.6 (two pre-design
  sessions: L002_SKILLS_PREDESIGN.md, L002_SKILLS_PREDESIGN_v2.md). Built with
  Claude Fable 5 via collegial relay. Tony integrated and deployed.
  Eight skills at v1.0, all cut from palomas_orrery @ b29ad3f8 (gallery-pipeline
  also from tonyquintanilla.github.io @ 89c8bf30):
  orrery-coding-conventions, safe-file-editing, agentic-pre-test,
  horizons-orbital-mechanics, provenance-discipline, earth-system-pipeline,
  gallery-pipeline, ledger-and-session-records.
  Protocol v3.30 installed; version history moved to ledger appendix.
  Extraction audit: documentation/MAPPING_TABLE_L002.md (every v3.29 line mapped;
  deliberate duplication registry for future amendments).
  Reviewed by Opus 4.6 against HEAD @ 33f0b148 before deployment.
  Skills 6-8 are first-time capture (~2/3 of skill content): knowledge that
  previously lived only in handoffs and code.
- **Scanner carve-out (design question, decided):** skills contain numeric claims
  (AU conversion, reference distances) with prose attribution rather than
  # Source: comments. Carve-out: "skills cite by prose; masters live in cited .py
  code." The scanner covers the code; the skills describe conventions whose
  authoritative instances are under scanner coverage. No exceptions entries needed
  unless scanner scope widens to .md files.
- **Follow-on:** skills_index.py devtool (L-097) -- same pattern as
  ledger_index.py; kills manifest-table drift.
**Gap:** none -- move to section C.
**Ref:** documentation/MAPPING_TABLE_L002.md, documentation/LEDGER_version_history_block.md, documentation/README_DEPLOYMENT.md, documentation/README_DEPLOYMENT_v2.md, documentation/L002_SKILLS_PREDESIGN.md, documentation/L002_SKILLS_PREDESIGN_v2.md, skills/*.

#### [L-020 | #26] CUSTOM_SHELLS tooltip verification
<!-- L:020 status:DONE upd:2026-06-22 section:C flag: rice:1/2/90/2 -->
Verify that every CUSTOM_SHELLS entry in shell_configs.py has a tooltip
and that the tooltip text is accurate. CUSTOM_SHELLS covers rotation axes,
sodium tail, magnetospheres, bow shocks, radiation belts, rings, and
field-aligned currents across Moon, Pluto, Mercury, Venus, Earth, Mars,
Jupiter, Saturn, Uranus, Neptune.
**Gap:** none -- move to section C.

#### [L-047 | #N10] Note-composition structural refactor (behind N6)
<!-- L:047 status:DONE upd:2026-06-23 section:C flag: rice:2/2/50/2 -->
- **N10** Note-composition structural refactor (behind N6). `[per chain]`
**RETIRED (2026-06-23, Tony):** undetermined -- the N10 'note-composition refactor'
scope was never recoverable. Closed as undetermined; if it matters it will resurface.
**Gap:** none -- move to section C.

#### [L-048 | #21/51] Animation track 21/51 -- core complete pending the v4 gate
<!-- L:048 status:DONE upd:2026-06-23 section:C flag: rice:3/3/50/3 -->
- **21/51 Animation track -- CORE COMPLETE pending the v4 gate. Status
  June 11:**
  - Phases 1, 2, 2.5, 3A DONE; 3B conditionally confirmed (section C).
  - **PHASE 3 SESSION C -- DELIVERED + PUSHED @7b71c29,
    `[render-gated on ANIMATION_TEST_PROTOCOL_v4]`:** barycenter Sun fix
    (engine Sun contract: real trajectory / engine fetch / suppression --
    never a placeholder position); console-spam fix (O13a; quiet rebuilds,
    builder messages print once at allocation, zero builder edits); comet
    tails per frame as OPT-IN (Animation Settings checkbox, default off
    per O1; build_comet_tail_traces capture shim, the 240-line builder
    unchanged; VARIABLE-COUNT handling: per-frame max-probe + pad-to-max
    with invisible dummies -- live counts are non-monotonic, 9/7/5/6
    measured; MAPS excluded, disclosed); Mercury sodium tail as engine
    customer (checkbox-gated; its greyed placeholder skipped when live);
    U+N bow-shock hover disclosure (D.Movement remainder); one-line
    auto-scale (Auto cube = MAX of orbital and center-shell extents, never
    shell alone -- the Finding-1 inverse).
  - **ENGINE ARCHITECTURE (for the record):** rebuild-as-universal --
    builder(**frame_context) through the same dispatch convention as
    static; registry = 14 per_frame tags in CUSTOM_SHELLS + the indicator
    builtin; trace-count stability asserted loud, variable-count elements
    pad-to-max; engine Sun contract with suppression-over-fabrication;
    quiet rebuilds; live byte-budget guardrail (warn >150 KB/frame).
    Design authority: ANIMATION_ENGINE_DESIGN_v1.md (sec 8 footnote
    superseded by the greyed legend -- amend on next touch).
  - **REMAINING RIDERS after the v4 gate:**
    * Resolution-sweep follow-on: RESOLVED BY MEASUREMENT (Phase 4,
      June 12, ADDENDUM decision 3). The 7-decimal coordinate-rounding
      lever (PERFRAME_COORD_DECIMALS, applied at the build_perframe_traces
      chokepoint -- every engine element inherits it) roughly HALVES
      per-frame bytes: Earth magnetosphere FULL 133->68 KB/f, Jupiter
      FULL 79->43, sodium tail 46->31 (live-measured; decimal places are
      scale-safe at any heliocentric distance, unlike significant
      digits). Full-resolution geometry + rounding fits the per-body
      budget, so NO density reduction ships: gate 5(b) is moot in its
      original form (nothing reduced to judge), and the per-body density
      literal sweep is CLOSED AS NOT NEEDED (reopen only if multi-
      magnetosphere or 60-frame budgets bite in practice; all eight
      simultaneously measure 411 KB/f rounded -- the >150 guardrail
      warns correctly). create_magnetosphere_shape n-parameter promotion
      DONE (defaults byte-identical; doubles as 20/N5's backend).
    * measure_animation_html.py: add tkinter file-browser dialog (B5).
    * Camera tracking -> item 19 fixture list (above): IMPLEMENTED.
    * O14/O15 incoming from the v4 gate: comet-tail legend churn verdict;
      sodium particle count in per-frame mode (knob exists, 500 -> 250
      measured ~24.9 KB/f -- note rounding now takes 500 to ~31 KB/f,
      which may settle O15 without the knob).
  - Standing instruction kept: when deferring, smoke-test the animate
    pipeline to a KNOWN state.
**Gap:** none -- move to section C.

#### [L-049 | #N8] Comet info-marker superposition cluster
<!-- L:049 status:DONE upd:2026-06-23 section:C flag: rice:1/2/50/2 -->
`[per chain]`
**Mode-5 confirmed (2026-06-23, Tony):** comet info-markers no longer superimposed. DONE; move to C on next housekeeping.
**Gap:** none -- move to section C.

#### [L-050 | #N9] white -> red orbit-marker switch (osculating marker intentionally stays white)
<!-- L:050 status:DONE upd:2026-06-23 section:C flag: rice:2/1/50/1 -->
`[per chain]`
**RETIRED (2026-06-23, Tony):** undetermined -- no recollection of an orbit-color problem. Closed as undetermined; will resurface if real.
**Gap:** none -- move to section C.

#### [L-065] European heat wave heat map (Earth System track)
<!-- L:065 status:DONE upd:2026-06-25 section:C flag: rice:3/3/80/1.5 -->
- **European heat wave 2026 -- new heat map, reuses the existing ERA5 framework.**
  Earth System / stressors family (the "heat" member named in the food-insecurity
  handoff). A dated temperature heat map of the ongoing 2026 European heat wave,
  built on the existing ERA5/Copernicus heat-map chassis -- new region + date
  config, NOT a new pipeline. TIMELY: a second, hotter wave began 22 Jun 2026
  (Western + Central Europe), deaths reported and June records falling; gallery +
  Reel value is time-sensitive while it is in the news.
- **Data = Fetched, trusted:** ERA5 2m temperature via Copernicus CDS (the live
  pipeline). Note the ~5-day near-real-time lag -- "now" honestly means up to ~5
  days back, so the layer is dated / pinned / deliberately re-pulled (no live
  auto-update), same as the family. Confirm exact dates, extent, and peak values
  at fetch time; do NOT recall breaking-news numbers (they go stale fast).
  Copernicus Sentinel-3 LST is the near-real-time surface-temperature alternative
  if a snapshot is wanted alongside the air-temp reanalysis.
- **Human-impact text = composed/transcribed tier (two-tier on-layer text; see
  L-001 / L-064).** If the layer carries any casualty / health-alert / attribution
  text, it is transcribed from an authority (national met services, EU Copernicus
  C3S, WMO, health agencies, WWA-style attribution), per-number `# Source:` within
  scanner lookback, Tier-1 visible, cite-or-remove. Climate-change attribution
  belongs to the cited authority in its voice -- we never author it; the reader
  connects it to the family thesis. Breaking-news tolls are volatile and
  contested -- transcribe a dated, sourced figure at build or omit.
- CLOSED 2026-06-25 (on 4685906): Mode-5 verified -- teaser (Gosport 36.1C pin,
    source visible, single title, "Click 3D Earth" CTA restored) + KMZ card (peak
    auto-filled, no [TO-FETCH]). Final record correction: UK -> Gosport 36.1C
    (Met Office, 24 Jun); attribution dated to Climate Central CSI (24 Jun 2026);
    Tama upgraded to AEMET primary. Tier-1 = 0. Parked, non-blocking: Sentinel-3
    LST stage-1 snapshot (separate artifact); WWA rapid study to supersede the CSI
    line if it publishes.
**Gap:** none -- move to section C.
**Ref:** existing ERA5/Copernicus heat-map framework; Copernicus CDS (ERA5 2m
temp) + Sentinel-3 LST; EU Copernicus Climate Change Service (C3S); L-001 + L-064
(two-tier on-layer text + scanner-format sweep). Current-event context: 2026
European heatwaves (record June temps; deaths reported across FR/UK/IE/ES/AT/DE/
SI), retrieved 2026-06-22.
**Note:** WATCH: World Weather Attribution rapid study on the June 2026 event. If it
  publishes, it is the strongest citable attribution -- replace the CSI/C3S line

#### [L-069] Food Insecurity Phase-2 -- Phase-5 "hidden Catastrophe" reveal (Darfur/Kordofan)
<!-- L:069 status:DONE upd:2026-06-24 section:C flag: rice:2/3/95/2 -->
- **BUILT + RENDER-CONFIRMED (Mode-5, ge_sudan.jpg 2026-06-24), committed 7923ac2.**
  10 maroon proportional dots in a toggle-able folder "Phase 5 (Catastrophe)
  populations (area level)", one per area carrying a mapped Phase 5 population (all
  mapped P4): Beliel 26,411 ... Kadugli 930. Sized area ~ population (sqrt); placed
  at each area's representative interior point. Renders correctly clustered in North
  Darfur, South Darfur (Nyala) and South Kordofan.
- **Pure IPC passthrough -- zero hardcoded/composed/summed numbers.** Balloon reads
  only area_name / overall_phase / phase5_population / phase5_percentage / population
  at runtime. "Catastrophe" (population term) used throughout; "Famine" (area term,
  none here) appears nowhere on the dots -- verified in KMZ bytes.
- **Dot-size legend key added** (Mode-5 follow-up, approved): legend card shows a
  large + small maroon dot keyed to the data's actual max/min phase5_population
  (read at runtime, not hardcoded), caption "larger = more people". Render-confirmed.
- **Causal-restraint wording tightened:** removed "the reader connects the pattern"
  from C3. C3 now ends "It draws no causal arrow of its own."
- **PRINCIPLE BANKED (generalizes to L-070 and every sensitive layer):** state the
  basis for the visualization; do NOT hand the lay reader a connection we will not
  draw ourselves. "The reader connects the pattern" is buck-passing -- naming the
  basis is honest, outsourcing the inference is not. (Tony, 2026-06-24.)
- **Scanner CATCHES the module (real clean, not false):** L-064 part-1 (allow-list)
  + narrow vocab add (people|persons?|percent|%). Tier-1=0, zero family ripple
  (star_notes:1257's "billion" trigger deliberately deferred to the L-064 sweep).
**Gap:** none -- move to section C.
**Ref:** L-001 (parent); L-064 (scanner); food_insecurity_generator.py; ge_sudan.jpg.
**Tony:** promote the "principle banked" to the protocol at the next update.
*Addressed: earth-system-pipeline skill captures this as the restraint
discipline's core stance (v3.30, L-002).*

#### [L-075] KMZ info-card "3+5" redesign -- compact header + tappable info balloon (Earth System engine)
<!-- L:075 status:DONE upd:2026-06-30 section:C flag: rice:3/3/95/2 -->
- **Problem.** The KMZ intel card was a fixed-size matplotlib PNG ScreenOverlay
  pinned top-left -- it could not reflow and collided with the Google Earth search
  bar on mobile, the long briefing unreadable on a phone.
- **"3+5" redesign (earth_system_generator.py; built on 9007ea3 -> pushed 3ba4e8a).**
  (3) intel card shrunk to a compact always-on header (title + date + "tap the (i)
  pin" hint) + a tappable info "i" Placemark at the grid centroid whose balloon
  carries the full briefing. (5) population-exposure key folded into the balloon;
  risk-scale colorbar moved bottom-right -> right-edge-centered, off the GE nav/3D
  buttons; header dropped below the mobile search bar. New helpers
  create_info_placemark + _briefing_to_html; producer-level change in run_scenario
  / build_spikes_kml.
- **Key fix -- CDATA.** simplekml 1.3.2 entity-escapes description fields by default
  (HTML would render as literal tags); wrapping the balloon in <![CDATA[...]]> makes
  simplekml emit it unescaped (base.py leaves CDATA blocks untouched), so GE renders
  it as HTML -- matching the proven desktop probe.
- **Structural win (parallel-pipeline).** Fix landed in the producer (run_scenario /
  build_spikes_kml), so every heatwave / coral / coastal scenario inherits 3+5 on its
  next regeneration -- not a per-europe_2026 edit.
- **Verified.** py_compile; ASCII/LF; synthetic KML smoke (CDATA balloon, briefing
  reflow, exposure key, repositioned overlays, pop-legend ScreenOverlay removed).
  Mode-5 (Tony, 2026-06-29): europe_2026 regenerated (cached ERA5, offline) and
  confirmed on DESKTOP + iPad + iPhone across Chrome / Bing / Safari -- balloon
  renders everywhere, collision gone, readable. iPhone full-screen sheet is the
  cleanest render; iPad docks the balloon inline. Gallery KMZ pushed d25fd93.
- **iOS banner (app chrome, not the KMZ).** Only the iPhone shows the "content is
  controlled by the author... do not enter passwords" banner: at phone size GE
  presents the balloon as a full-screen web sheet (which carries the standard safety
  banner); the iPad docks it inline (no sheet, no banner). Same file, same HTML;
  harmless (no input field), not switchable from the KML side.
- **Polish (delivered this session; 2 lines, verified; LANDS on the next europe_2026
  regenerate + gallery push).** header screenxy y 0.90 -> 0.84 (iPhone search-bar
  clearance); pin label scenario_id -> title so it matches the balloon heading
  ("Europe Heat Dome (June 2026) - tap for details"). Both Tony-approved. Only
  remaining action on this block; a quick re-confirm on the next regenerate closes it.
- **Dead code surfaced.** create_pop_legend_card is now unused (exposure key folded
  into the balloon); left defined to keep the live push minimal-risk -> remove in the
  L-068 dead-code sweep, not its own push.
- **Generalized to the family (this session -> L-076).** create_info_placemark +
  the briefing-to-HTML helper were extracted to earth_system_common.py and the
  3+5 card + tappable i-pin applied to the FOOD generator too; the picker was
  also generalized (ScenarioPicker). Heat balloon verified byte-identical.
**Linked:** chassis from L-065 (europe_2026 build); series tracked under L-071;
dead-code removal -> L-068. Icon uses remote Google info-i.png (probe parity); bundle
a local icon only if the iOS pin glyph misbehaves.
**Gap:** none -- move to section C.
**Ref:** earth_system_generator.py (run_scenario, build_spikes_kml, build_impact_kml,
create_intel_card, create_info_placemark, _briefing_to_html); simplekml 1.3.2 base.py
CDATA behavior.

#### [L-076] Earth System shared module (earth_system_common) + 3+5 generalized to food
<!-- L:076 status:DONE upd:2026-06-30 section:C flag: rice:3/3/95/2 -->
- **What.** Extracted the engine-agnostic KMZ/UI helpers shared by the heat and
  food generators into a new module, earth_system_common.py, retiring the
  heat<->food duplication before it set in: briefing_to_balloon_html();
  create_info_placemark(kml, title, date, briefing, lat, lon, extra_html="") --
  the tappable "i" pin + CDATA balloon, with the heat population-exposure key now
  passed in via extra_html rather than baked in; and ScenarioPicker(scenarios,
  run_fn, ...), a generic Tkinter menu whose run_fn(scenario, status_callback) is
  injected (heat passes run_scenario, food passes a small adapter over its run()).
  Both generators import from it; both __main__ blocks launch via the shared
  picker.
- **Food 3+5 parity (detail under L-001).** With the shared helpers in place, the
  food KMZ gained the compact header + single tappable i-pin + consolidated
  balloon -- the L-075 pattern applied to categorical/food data instead of the
  scalar heat field. The food generator deliberately still does NOT import the
  scalar heat engine; it shares only the engine-agnostic UI/KMZ helpers.
- **scenarios_food_insecurity.py.** New scenario registry (Sudan now; commented
  stubs for South Sudan / Chad / CAR / Ethiopia) -- the structure L-070 builds on.
- **Controller single-source (--preload).** earth_system_controller.py gained
  preload_layers(prefix) + a --preload <prefix> flag that globs
  data/<prefix>_*_blockbuster.kmz; the food GUI launcher delegates to it, so the
  food_insecurity_* family contract now lives in ONE place. (A symmetric --exclude
  complement was drafted but NOT committed -- left for a later pass if wanted.)
- **Verified.** py_compile; ASCII/LF; the heat balloon proven BYTE-IDENTICAL
  against the pristine create_info_placemark (793 chars, icon + balloonstyle
  match), so the working heat card cannot have drifted; food KMZ render-tested
  end-to-end (189 areas, single i-pin, full balloon). Landed 1b74bf1 -> be183c8
  -> c81bb3b; Mode-5 iOS-confirmed (L-001, IMG_1153/1154). Heat end-to-end render
  remains Tony's Mode-5 (not all heat scenario deps available in-container).
**Gap:** none -- move to section C. 
**Ref:** earth_system_common.py; earth_system_generator.py;
food_insecurity_generator.py; scenarios_food_insecurity.py;
earth_system_controller.py; cross-ref L-075 (heat 3+5 this generalizes), L-001
(food workstream), L-070 (multi-country it enables).

#### [L-072] Gallery Studio WYSIWYG preview -- render through the real index.html viewer
<!-- L:072 status:DONE upd:2026-06-26 section:C flag: rice:2/2/100/2 -->
- **Problem.** Studio Preview opened a bare Plotly figure via file://, so the
  viewer-only chrome (green Google Earth button from `_kmz_handoff`, link-icon
  dropdown from `_link_data`) never appeared -- not WYSIWYG with the live gallery,
  which adds that chrome at view time. The button is viewer chrome, not a figure
  annotation; the Studio preview never ran the viewer.
- **Fix (2 increments; gallery repo 3ee1734 -> pushed 495683e).** Inc 1: a dormant
  `?preview=<file>` branch in index.html `init()` that injects a synthetic lookup
  entry and reuses `loadVisualization` UNCHANGED (no render-path refactor; inert
  for real visitors). Inc 2: `gallery_studio.py` `_preview` rewrite --
  build_gallery_html -> the REAL `json_converter.extract_plotly_json_from_html`
  (same parse that yields the pushed JSON) -> throwaway
  `gallery/_studio_preview.json` -> ephemeral 127.0.0.1 daemon server rooted at the
  repo -> open the GENUINE index.html at `?preview=`. No vendored viewer, no second
  extractor -- WYSIWYG by construction. `.gitignore` covers the preview slot.
- **Verified.** Producer-chain smoke: `_kmz_handoff` + `_studio` survive
  build->extract into the previewed card; py_compile; ASCII/LF. Mode-5 (Tony): GE
  button renders, click-through resolves for PUSHED assets, no button when no KMZ,
  old file:// preview gone, `import json_converter` resolves via dashboard launch.
- **By design (not a gap).** GE button 404s when the KMZ is not yet pushed to
  `gallery/assets/` -- the preview honestly reports push status. Tony pushes the
  KMZ at generation time; only the exported HTML iterates between previews.
  Increment 3 (local-asset fallback) DECLINED for this reason.
**Linked:** sibling to L-058 (open Studio items); preview reuses json_converter as-is.
**Gap:** none -- move to section C.

#### [L-064] Provenance-scanner format sweep -- Earth System family
<!-- L:064 status:DONE upd:2026-06-30 section:C flag: rice:3/3/100/2 -->
- **CONFIRMED for food_insecurity_generator (the per-module question this item
  poses): the scanner does NOT traverse it.** Two compounding gaps, both proven
  empirically (uncited recognized-unit token in a fresh file -> zero findings):
  (1) ALLOW-LIST gap -- _extract_string_units only runs for a hardcoded
  narrative_files set (+ *_visualization_shells); a new module is excluded, so
  its display strings are never extracted/scored. (2) VOCABULARY gap --
  NUMERIC_CLAIM_RE recognizes only physical units (AU/km/deg/masses/K/kg...), no
  people|percent|%|million|thousand|billion, so humanitarian figures aren't seen
  as claims even inside an allow-listed file. The module's Tier-1=0 is a FALSE
  clean.
- **Verified two-part fix (on a SCRATCH copy; repo scanner untouched):** add
  'food_insecurity_generator' to narrative_files; append the humanitarian units
  to NUMERIC_CLAIM_RE. Under it, this module's sourced strings all read "Has
  source citation," Tier-3 -- the construction-site # Source: discipline holds.
- **Family ripple (decision driver):** the vocabulary extension newly surfaces a
  pre-existing REAL Tier-1 -- star_notes.py:1257, "No source citation (recalled)"
  -- invisible before only because of the vocabulary gap. Part (1) is local/safe;
  part (2) is family-wide CI with a ripple to triage.
- **Live-repo check (2026-06-30, @1f5901e): food's half is ALREADY LANDED, not
  just scratch-verified.** narrative_files now contains 'food_insecurity_generator'
  and NUMERIC_CLAIM_RE now carries people|persons?|percent|%. The "scratch copy"
  framing above is historical -- the food-specific fix is live. star_notes.py:1257
  triage status not re-confirmed this pass.
- **Scope expansion (2026-06-30, L-077 scaffold session) found this was bigger
  than one missing file, and that the manual-list mechanism itself was the
  problem, not just its current contents.** 6 of 7 Earth System files were
  missing from narrative_files; a second, separate vocabulary gap (no bare F/C
  degree-suffix pattern -- "117F" / "47.2C" don't match anything) sits underneath
  the humanitarian one; and a manual proxy check found likely real gaps beyond
  the Earth System family entirely (energy_imbalance.py, the paleoclimate_*_full
  family). Full findings preserved below for reference.
- [Full per-file risk breakdown and the manual-proxy methodology from the
  2026-06-30 session retained here verbatim -- see prior revision of this block
  for the complete scenarios_heatwaves.py / scenarios_western_heatwave_march_2026.py
  / scenarios_coral_bleaching.py risk split, all still valid as groundwork.]
**CLOSED BY DECISION (2026-06-30):** the food-insecurity half is genuinely done
and verified live -- that closes this item. The "sweep remaining Earth System
modules" half is NOT more of the same work -- it needs a different MECHANISM
(systematic, role-driven coverage off module_atlas.py, not hand-editing a list
file by file), so it is new tooling work, not a sweep remainder. Promoted to
L-078, the same shape as L-009 spinning off L-061 for new physics rather than
calling it a cone remainder. All empirical findings above (the F/C gap, the
energy_imbalance.py / paleoclimate candidates, the per-file risk split) carry
forward into L-078 as groundwork, not lost.
**Gap:** none -- move to section C.
**Ref:** provenance_scanner.py; PROVENANCE_AUDIT.md; module_atlas.py; originated
from L-001; confirmed via food_insecurity_generator build
(HANDOFF_food_insecurity_build_v2.md); superseded by L-078, 2026-06-30,
repo HEAD 1f5901e.

#### [L-097] skills_index.py -- Skill Manifest auto-generation (process/tooling)
<!-- L:097 status:DONE upd:2026-07-04 section:C flag: rice:2/2/80/1 -->
- **Devtool mirroring ledger_index.py:** walk skills/, read each SKILL.md
  frontmatter (name, description, fires_when) and body version line, regenerate
  the Skill Manifest table in the protocol file between SKILL-MANIFEST markers.
  Kills manifest-table drift the same way ledger_index.py killed hand-pasted
  summary rows. Also runs a consistency check: every skill directory has a
  manifest row and vice versa; folder name matches frontmatter name; version
  line exists.
- **Pattern:** ledger_index.py (402 lines, marker-based zone regeneration,
  --check mode for CI-style dry run). Read ledger_index.py as the recipe;
  mirror the architectural choices (parse -> validate -> regenerate -> report).
- **fires_when frontmatter field** added to all 8 SKILL.md files (editorial
  control of the manifest's "Fires when" column). Claude's skill loader reads
  name/description; this field is read only by skills_index.py. Fallback: first
  sentence of description, truncated, with a warning.
- **COMPLETED July 4, 2026.** Built by Claude Fable 5 via collegial relay
  (spec by Opus 4.6, documentation/FABLE_PROMPT_L097.md). Tony integrated.
  skills_index.py: 262 lines, repo root. Verified: py_compile clean; --check
  mode zero problems (8 skills parsed); manifest regenerated in
  project_instructions_v3_31.md, output matches v3.30 hand-written table.
  Tony ran locally on Windows (Python 3.13) -- clean, manifest regenerated.
- **Skill-layer verification (July 4, 2026, Opus 4.6 session @3429e568).**
  All 8 installed skills confirmed firing: orrery-coding-conventions loaded on
  hover-text trigger, ledger-and-session-records loaded on L-handle trigger.
  The two-layer system (resident protocol + on-demand skills) is operational.
  Protocol v3.31 installed with populated manifest; skills_index.py is the
  ongoing drift check.
**Gap:** none -- move to section C.
**Ref:** L-002 (parent), ledger_index.py (pattern), project_instructions_v3_31.md
Part 3 Skill Manifest, documentation/FABLE_PROMPT_L097.md.

#### [L-109] Fable 5 adversarial review remediation (builder Pass 1+2)
<!-- L:109 status:DONE upd:2026-07-10 section:C flag: rice:3/1/95/1 -->
- **What.** Fable 5 (Mode 7 collegial) adversarially reviewed the shipped
  gallery_cache_builder.py: 11 code findings (A-1..A-11) + 4 doc (B-1..B-4). All
  verified against the actual code + astroquery 0.4.11 source (fetched, not
  recalled) and remediated across two passes.
- **Pass 1 (safety/validity).** A-1 crash-mid-swap archive-loss seam
  (recover_incomplete_swap at run start + atomic_swap refuses to delete a
  pre-existing .prev + nightly-with-no-raw ABORTS); A-2 nonzero exit on abort;
  A-11 cleanup keeps aborted-run autopsies; A-7 hyperbolic periapsis sign; A-8
  offline test resolves config from the repo layout (the flat working dir had
  masked the break).
- **Pass 2 (correctness/spacecraft).** A-3 failed fetch serves last-good conic
  with as_of_today NULLED (drop only if no last-good); A-4 id_type majorbody/id
  -> None; A-5 closest_apparition/no_fragments (CAP;/NOFRAG;) passthrough; A-9
  #T freshness invariant; A-10 --refresh-spacecraft wired; B-3
  serving_base/scene_features/step_hours restored for v0.6 parity. Spacecraft
  fetch REDESIGNED: authoritative config.start (no probe) + coarse glide
  backbone + daily densify inside known flyby windows + Douglas-Peucker thin.
  DISSOLVES A-6 (Voyager first build 2,610 coarse points, not ~17,900) and pulls
  L-102 (spacecraft thinning) FORWARD from deferred served-side to fetch-side.
- **Verification.** Offline suite 47 -> 63 checks, 0 failures (crash-recovery
  kill-test, exit-code, DP, A-3 stale-serve, A-4, B-3 parity); py_compile clean;
  ASCII-clean. Live gate (Horizons) remains Tony's hardware.
- **Docs.** Master plan B-1/B-2/B-4; this ledger; TESTING_PROTOCOL.md authored.
**Note:** builder copy source orrery 4e2629c / gallery a2b7435 (un-pushed);
remediated build re-pushed by Tony for Fable's second pass.
**Gap:** live --dry-run on Tony's hardware settles the two open questions --
whether 2P/Encke's Horizons header carries TP=, and whether Horizons clips or
errors on a pre-SPK spacecraft start.
**Ref:** gallery_cache_builder.py; test_gallery_cache_builder_offline.py; TESTING_PROTOCOL.md; L-098 (parent); L-102 (pulled forward); L-107 (sync register).
**Gap:** none -- move to section C

#### [L-110] GPT competitive cross-check remediation (builder Pass 4)
<!-- L:110 status:DONE upd:2026-07-10 section:C flag: rice:3/1/90/1 -->
- **What.** The SAME review prompt given to Fable 5 was given to GPT (competitive
  Mode 7: same prompt -> two independent reviewers -> compare). GPT reviewed the
  pre-remediation build (gallery a2b7435); most of its list was already closed by
  L-109, but it surfaced real gaps L-109 did not, verified against the CURRENT
  remediated code before acting.
- **N1 -- dataset-level atomicity.** L-109's A-1 fixed archive DELETION but the
  promotion was still four separate subtree swaps (a crash between them left a
  mixed generation). Fixed via WHOLE-DIRECTORY swap (Option A, Tony's call):
  staging is a sibling, the entire generation is renamed into place as one unit
  (atomic_swap_dir), recovery restores the whole generation, and one prior
  generation is retained as rollback. GPT elevated this to a blocker; Fable had
  rated it a test-addition.
- **N2 -- push-as-success.** git push ran check=False and committed=True was set
  unconditionally -- a silent push failure read as published. THIS IS the failure
  mode that left gallery a2b7435 committed-but-never-pushed. Fixed: git_commit
  returns staged/committed_local/pushed_remote/sha; push runs check=True and the
  remote is confirmed to CONTAIN the SHA; committed now means pushed_remote.
  Fable did not flag this; the competitive pass caught it.
- **N3 -- object-set continuity.** No invariant that every served object persists,
  and first-build had no minimum-count floor. Added: a run ABORTS if it drops an
  object the prior generation served (guards the add-object moment); non-spacecraft
  first-build ABORTS below 0.5x the backfill-day floor (clipped-response guard).
- **N4/N6 -- #U replaced by #B3.** The absolute 1000 km #U threshold both
  false-rejected close-centered objects and passed a large wrong-AU value; the
  module header still CLAIMED a B3 check that did not exist. Replaced with #B3
  conversion-consistency (served km == raw AU x KM_PER_AU), which tests the
  convert+serialize path and retires the phantom claim.
- **N5 -- structured solution-TP outcomes.** A network/parse failure in
  fetch_solution_tp silently degraded a comet to a today-anchored conic (an
  operational failure masquerading as a model choice). Now returns
  found/not_present/parse_failed/request_failed; operational failures serve
  last-good (A-3), only a genuine not_present takes the today fallback.
- **Verification.** Offline suite 63 -> 68 checks, 0 failures (whole-gen crash
  recovery, #B3 catch, N3 drop-abort, N5 last-good, N2 local-vs-remote via a real
  temp git repo); py_compile clean; ASCII-clean.
- **Methodology note.** The competitive Mode 7 pattern paid off exactly as the
  protocol predicts: two independent reviewers on one prompt, and GPT caught two
  real things (N1 elevated, N2 entirely) that Fable's pass missed -- while neither
  is authoritative over the live render (Mode 5).
**Ref:** gallery_cache_builder.py; test_gallery_cache_builder_offline.py; TESTING_PROTOCOL.md; L-098 (parent); L-109 (Fable remediation).
**Gap:** none -- move to section C

#### [L-112] Gallery builder Pass 5: two-reviewer Pass-2 remediation
<!-- L:112 status:DONE upd:2026-07-10 section:C flag: rice:3/1/95/1 -->
- **What.** Fable 5 + GPT 5.5 COMPETITIVE Pass-2 reviews of the pushed build
  (gallery 0b0f051 / orrery 331eb95). Neither a superset -- each caught a
  blocker-class item the other missed. Verified against code, then remediated.
- **Fixed (before dry-run).** P2-1 spacecraft first-build/refresh appends the
  daily [today-freeze, today] top-up so the arc ENDS today (#T passed only by
  calendar coincidence before -- Fable, demonstrated). P2-2 --dry-run --object was
  un-runnable in both repo states (N3 + no-raw guards); both now skip for
  dry_run/only_slug. P2-4 comet apparition kwargs now reach fetch_vectors_range
  (Encke's nightly point). Push-status persistence: the promoted manifest is
  rewritten after the push -- it was written pre-swap with committed=false (GPT).
  #B3 now compares COMPONENTS (a magnitude-preserving axis-swap/sign-flip is
  caught -- GPT) and raises on a missing raw point (both). DP flyby preservation:
  DP thins the GLIDE only, event-window points merge after (P2-Q1). N5 collapsed
  to found-or-last-good (no today-anchor: a comet Horizons serves always has a Tp,
  so not_present means something is wrong -- Tony). P2-9 stale comet carries its
  comet block forward from the prior published index. .prev wedge: quarantine-
  rename + non-silent recovery + sibling sweep.
- **Verification.** Offline suite 68 -> 75 checks, 0 failures (P2-1 at an
  ADVERSARIAL NOW, P2-2 both states, #B3 swapped-axis, P2-9, N5); compile + ASCII
  clean.
- **Docs.** Manifest body B-6 reconciled (retired-probe lines under the top
  amendment -- the amend-at-top/stale-body drift, B-1/B-2 one level up); TESTING
  PROTOCOL nits (11 not 9; version-log TODO; step-1 P2-2); handoff SHA 0b0f051.
- **P2-3 (do before the backup action is wired).** N1's whole-dir swap put the
  L-106 backup INSIDE the swapped dir (rides into .prev, deleted next run) and
  left .gitignore naming the old in-tree .staging/. Relocate the mirror OUTSIDE
  data/solar-system (e.g. data/_backup/; Google Cloud off-site half unchanged);
  .gitignore must ignore data/.staging_*, data/solar-system.prev,
  data/solar-system.quarantine_*. Reconcile L-106 + manifest S8/F9.
- **Ride with handles (deferred).** P2-5 N3 retirement: NO retired-flag (Tony) --
  a deliberate config-row removal ABORTS every night until also cleared from the
  published index; supervised, acceptable, flagged. P2-6 exempt an explicitly-
  refreshed slug from the per-object shrink check. N2 match refs/heads/main via
  ls-remote (advisory under manual-push). #B3 reload the WRITTEN
  coverage_index.json for the served side. as_of_today explicit UTC date. Builder
  astroquery-version log at run start (feeds N11 identity matrix).
**Note:** both Pass-2 reviews independently proposed the competitive-review
protocol amendment that produced them -- adopt in the skills/protocol layer.
**Ref:** gallery_cache_builder.py; test_gallery_cache_builder_offline.py; GALLERY_BUILDER_MANIFEST_v2.md (B-6); L-109; L-110; L-111.
**Gap:** none -- move to section C

#### [L-117] Offline suite red at HEAD: Encke id drift (2P -> 90000091) not mirrored in the mock
<!-- L:117 status:DONE upd:2026-07-12 section:C flag: rice:3/3/95/0.25 -->
- **What.** tools/test_gallery_cache_builder_offline.py mocks Horizons by
  horizons_id: ELEMS keys and fake_solution_tp both keyed '2P'. The live-gate
  Encke pin (config 2P -> 90000091) was never mirrored here, so the mock
  returned no data for '90000091', the build dropped encke, and objs['encke']
  KeyErrored. RED from a clean clone -- reached ~22 checks, then died.
- **Why it hid.** F1's FileNotFoundError (fixed in the L-114 push) masked
  this: prior runs died at config-load before reaching the encke assertion
  (line 138), so no complete green run ever surfaced it. F1's stated
  acceptance ("suite green from a clean clone") was never actually met --
  the path fix made the suite RUN, revealing the next failure.
- **Fix (verified green + pushed).** Two lines: ELEMS key '2P' -> '90000091';
  fake_solution_tp branch '2P' -> '90000091'. Green three ways (Opus clone,
  Tony Windows run, PASS 75 checks 0 failures) and LIVE at gallery HEAD
  a08bdd10. The true completion of L-114's F1 acceptance and the real green
  gate for L-098 step 1.
- **Ref.** tools/test_gallery_cache_builder_offline.py (ELEMS ~line 26,
  fake_solution_tp ~line 63). Parent L-098; sibling of L-114/F1. Connects to
  the open "should Encke be in the tranche" question (unresolved; if it later
  resolves to REMOVE, drop encke from config + mock + assertions).


#### [L-115] Skills v1.1 batch: accuracy fixes + two seed blocks (Fable Mode 7)
<!-- L:115 status:DONE upd:2026-07-12 section:C flag: rice:2/2/90/1 -->
- **What.** Move 1 of the skills-layer update from Fable 5's 2026-07-12
  Mode 7 review. Five targeted edits, all verified against orrery HEAD
  7e108b8 by Opus before delivery:
    - agentic-pre-test 1.1: correct the inverted gray90/SystemButtonFace
      rationale (palomas_orrery.py has 0 gray90 / 26 SystemButtonFace at
      HEAD and at the b29ad3f8 cut; real risk is cross-file
      indistinguishability -- siblings star_visualization_gui.py=5,
      earth_system_visualization_gui.py=3) + cross-pointer to the
      gallery-cache-builder gate. [Fable F2]
    - horizons-orbital-mechanics 1.1: new Small-Body Record Pinning block
      (short-designation ambiguity; pin comets to 900000XX records: Encke
      90000091, Halley 90000030); fires_when gains "comet record pinning".
      [seed 1]
    - earth-system-pipeline 1.1: fix a phantom GUI name -- MissionSelector /
      all_scenarios do not exist; real names MissionControlApp,
      ScenarioPicker, _heat_scenarios(). [Fable F3]
    - orrery-coding-conventions 1.1: optional "Operational gotchas"
      docstring block (known-trap + normal-but-scary), PRACTICE. [seed 2]
    - palomas_orrery.py:1522 comment: Encke 90000002 -> 90000091 (stale
      recalled record number in an illustrative comment). [Fable F4]
- **Dropped from the batch:** Fable's provenance-discipline carve-out line
  -- provenance_scanner.py:382 walks .py only, so SKILL.md is already
  structurally outside the scan; the line would document a non-existent
  risk. [verified @7e108b8]
- **Gap.** Apply the five snippets; bump the four skill version lines to 1.1
  and re-pin "Cut from ... @ <SHA>" to the POST-PUSH orrery HEAD; run
  skills_index.py to regenerate the Skill Manifest (horizons fires_when
  changed); reinstall the four skills to Tony's account. Move 2 (new
  gallery-cache-builder skill) tracked as a sibling entry when opened.
- **Ref.** Fable review doc 2026-07-12 (F2/F3/F4, seeds 1-2). Parent: L-002
  (skills layer).
**Tony:** RICE proposed 2/2/90/1 -- yours to finalize. One umbrella entry as
delivered, or split per skill (your call).
**Gap:** none -- move to section C.

#### [L-116] New skill: gallery-cache-builder (Move 2 of the skills update)
<!-- L:116 status:DONE upd:2026-07-12 section:C flag: rice:3/2/85/2 -->
- **What.** Ninth skill, gallery-cache-builder, added for the Phase 1b
  nightly serving subsystem (L-098) -- Move 2 of Fable 5's 2026-07-12 Mode 7
  review. Decomposition decision (Tony, this session): NEW skill, not an
  extension of gallery-pipeline (non-overlapping moments of need; the
  builder passes every subsystem marker). Authored
  skills/gallery-cache-builder/SKILL.md in the orrery repo (L-002
  convention; describes gallery code @ 8e060677 + orrery context @
  e83fe9ce). Every code fact verified against HEAD before delivery; Fable's
  cleanup_stale_siblings seed corrected to _sweep_siblings; validation
  stance corrected (#B3 ABORTs, not WARN -- the code raises).
  gallery-pipeline bumped to 1.1 with a one-line cross-pointer.
- **Also in this push (Move 1 follow-through).** Re-pin the four Move-1 skill
  version lines: the literal placeholder "<ORRERY HEAD after push>" was
  committed verbatim and is corrected to e83fe9ce (the post-Move-1 orrery
  HEAD they were verified against).
- **Spotted, not fixed here.** gallery_cache_builder.py ~line 755 inline
  comment "guard/B3 WARN" contradicts the code (#B3 raises ValidationAbort)
  and the module docstring. Low-priority builder-comment cleanup; deferred.
- **Gap.** Create the new skill dir + file; apply the gallery-pipeline
  cross-pointer + 1.1 bump; apply the four re-pins; run skills_index.py
  (manifest gains a 9th row, gallery-pipeline -> 1.1); reinstall the new +
  edited skills. On push, no post-push re-pin needed -- Move 2's skills
  describe already-pushed stable trees (unlike Move 1).
- **Ref.** Fable review doc 2026-07-12, section 2.1 (new-skill argument),
  seed 3. Parent: L-002. Sibling: L-115 (Move 1). Subsystem: L-098.
**Tony:** RICE proposed 3/2/85/2 -- yours to finalize.
**Gap:** none -- move to section C.

#### [L-106] Gallery-cache backup + gitignore discipline
<!-- L:106 status:DONE upd:2026-07-12 section:C flag: rice:2/2/90/1 -->
- **What.** The gallery raw archive (data/solar-system/raw/) is now an
  irreplaceable fetched-once asset (same class as the orrery Horizons cache).
  v0.3 specced only ROLLBACK (git history), not BACKUP. Add a SEPARATE scheduled
  action (mirrors Tony's existing "backup on every cache update") that copies
  raw/ to a GITIGNORED local path on each successful commit; Google Cloud
  auto-backup carries the off-site copy (closes the repo/account failure mode on
  infrastructure separate from GitHub). Served files are derived/regenerable and
  are NOT backed up independently.
- **Why gitignore.** The gallery repo serves to the web under ~1 GB Pages
  guidance (474 MB used); committing backup copies would double growth against
  the tightest constraint. The local backup path goes in .gitignore alongside
  .staging/.
- **Integrity layers (distinct failure modes).** shrink gate (bad write,
  prevented) / git revert (bad build that committed, rolled back) / off-repo
  backup (bad repo, survived). No overlap, no gap.
- **Decoupled.** A backup failure never blocks a good commit; the builder never
  waits on backup. The action OBSERVES a successful commit -- it is not a builder
  step.
**Tony:** backup-on-every-update + Google Cloud off-site are already in practice;
this extends that discipline to the new gallery cache.
**Gap:** FIRST-BUILD PRECONDITION -- the backup action AND the .gitignore entry
must both exist before the first gallery-cache build runs (so the archive is
never held un-backed-up). Wire the scheduled action to observe the nightly commit;
add the gitignore line; verify at manifest S10 steps 2 and 9.
**Ref:** GALLERY_BUILDER_MANIFEST v2 (S8, F9, pre-build gate 3);
GALLERY_DATA_SOURCE_HANDOFF v0.4 (change 5); L-098 (parent).
**Resolution (2026-07-12).** Off-repo backup requirement met by existing
background coverage, not a new action: the repo tree lives under
C:\Users\tonyq\OneDrive\Desktop\python_work, so OneDrive continuously syncs
the whole working tree (raw/ included) off-machine (verified: gallery repo
folder green "available on this device"); Google Cloud + Windows backup layer
on top; raw/ is also committed to git (GitHub). The .gitignore entry
(data/_backup/) was already present. The explicit copy-raw/-to-_backup/
scheduled action is NOT built -- redundant with OneDrive folder-level backup +
version history; building it would duplicate infrastructure.
**Gap:** none -- move to section C

#### [L-108] Master plan v10 -> v11: Phase 1b fetch-fresh pivot reconciliation
<!-- L:108 status:DONE upd:2026-07-12 section:C flag: rice:2/1/90/1 -->
- **What.** MASTER_PLAN_INTERACTIVE_GALLERY.md (v10) is STALE on Phase 1b: its
  Status line reads "converged v0.3" while its own changelog reads v0.4
  (internal inconsistency), and -- more importantly -- section-5 Phase 1b Deliverable
  #1 (line ~548) and section-3a (line ~317) still describe the export script as one
  that "reads desktop caches." That is the PRE-PIVOT model. The v0.4 fetch-fresh
  pivot retired reading the legacy desktop cache; the shipped builder fetches
  fresh from Horizons into the gallery cache. The plan now contradicts the code.
- **Origin.** The drift is PIVOT-driven (v0.3/v0.4), not build-driven; the build
  merely made it visible (there is now code that fetches fresh). Captured here
  rather than folded silently into the build close-out -- the master plan is
  Tony's versioned roadmap and deserves a proper v11 pass.
**Note:** v11 pass done this session (Opus 4.8); pending your review + commit.
The remaining section-3a polish is optional, low priority.
**Gap:** v11 pass APPLIED this session (July 9): status -> v0.4 + build-underway;
section-3a projection + OQ-B/C/F + a reconciliation note (subtraction RETIRED,
osculating-primary, fetch-fresh, NIGHTLY cadence, no forward padding); the
parents-serve-position-files bullet corrected; section-5 Deliverable #1 (reads-
caches -> fetch-fresh) + serving-home (H2 gallery `data/`, not the H1 dedicated
repo); section-5a next-step (build underway); changelog New-in-v11 + Superseded;
version v10 -> v11. Transactional patch, 16 edits each matched exactly once; zero
new non-ASCII. REMAINING (optional, low priority): bullet-by-bullet cleanup of
the still-historical section-3a schema sub-block beyond the reconciliation note.
**Ref:** MASTER_PLAN_INTERACTIVE_GALLERY.md v10 (sections 3a, 5); GALLERY_DATA_SOURCE_HANDOFF v0.4; GALLERY_BUILD_HANDOFF v0.1; L-098 (parent).
**Gap:** none -- move to section C

#### [L-138] Candidate objects & presets for the Objects menu (running list) -- superseded
<!-- L:138 status:DONE upd:2026-07-17 section:C flag: rice:2/2/50/2 -->
- **Superseded (2026-07-17).** Split into the new O.* section family, one
  L-handle per candidate, per Tony's design call. Seed content carried
  forward to L-139 (Pallas), L-140 (Hygiea), L-141 (Interamnia), L-142
  (Davida), L-143 (Sylvia), L-144 (Eunomia), L-145 (Euphrosyne), L-146
  (HR 8799). "Europa" and Psyche from the original note were already
  present in celestial_objects.py -- not carried forward.
**Gap:** none -- superseded, not itself actionable.
**Ref:** to_do_ideas.md (pre-ledger); successor items above.


#### [L-063] Orrery GUI Note text update
<!-- L:063 status:DONE upd:2026-07-17 section:C flag: rice:2/1/50/0.5 -->
- **Update the Note in the orrery GUI.** The in-app Note text (palomas_orrery.py)
  has drifted from current project state; refresh it to reflect current scope.
  Paired with L-062 as the user-facing text refresh. Small Mode-1 edit once the
  new wording is decided.
**Note:** Resolved by a bigger move than originally scoped: rather than
refresh the static Note wording, the whole Note panel (third GUI column)
was REPLACED by the live, embedded palomas_orrery_dashboard.py launcher
-- see L-147. The wording-drift problem this item tracked no longer
applies; there's no static text left to go stale.
**Ref:** L-147 (dashboard embed); L-062 (README refresh -- still open,
now unrelated to this one).

#### [L-134] Dashboard developer-tools audit
<!-- L:134 status:DONE upd:2026-07-17 section:C flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/17/26, pre-ledger note).** Review
  palomas_orrery_dashboard.py against all currently-available developer
  tools/launchers -- update to reflect what's current, or remove stale
  entries. Pairs with L-062 (README refresh) and L-063 (GUI Note text
  update) as interface-currency work.
**Note:** Audited LAUNCH_GROUPS against both repos at HEAD (orrery
d427adf8, gallery 3d4a2aec). Added 13 entries: 5 gallery-repo tools from
tools/ (Gallery Cache Builder, Inspect Staging, Debug Encke TP, Gallery
Cleanup, Gallery Builder Offline Tests) and 8 root-level orrery devtools
that were live but unlisted (Test Orbit Cache, Export Orbit Cache, Test
Reset Completeness, Create Ephemeris Database, Climate Cache Manager,
VOT Cache Manager, Osculating Cache Manager, SIMBAD Query Manager).
Left out on purpose -- flagged for Tony to override any of these calls:
one-off historical diagnostics with hardcoded paths (diagnose_bcodmo.py,
convert_hot_ph_to_json.py, examine_hot_csv.py, barycenter_cache_check.py);
narrow phase-specific verification scripts (smoke_dipole_cone.py,
smoke_rotation_axis.py, smoke_phase4.py, measure_perframe_elements.py);
a demo-only __main__ (object_type_analyzer.py); already reachable via
another GUI's own button (energy_imbalance.py via Earth System GUI,
coordinate_system_guide.py via Orbital Construction); and a library
module with no __main__ (incremental_cache_manager.py). All 35 final
entries validated to resolve to real files against the actual sibling
repo layout, not just read from source.
**Ref:** to_do_ideas.md (pre-ledger, 4/17/26); L-147 (dashboard embed,
same session).

#### [L-147] Embed dashboard launcher in orrery GUI third column
<!-- L:147 status:DONE upd:2026-07-17 section:C flag: rice:1/3/100/2 -->
- **Replaced the static "Note" panel (third GUI column of palomas_orrery.py)
  with a live, embedded palomas_orrery_dashboard.py launcher**, so the same
  launch-card UI serves both standalone (`python palomas_orrery_dashboard.py`)
  and embedded contexts from one source instead of two. Split the monolithic
  `PalomasOrreryDashboard(ctk.CTk)` into `PalomasOrreryDashboardFrame(ctk.CTkFrame)`
  (the actual UI, takes a parent widget) plus a thin `PalomasOrreryDashboard(ctk.CTk)`
  standalone-window wrapper around it. palomas_orrery.py gets a Mode 1
  snippet (import + `PalomasOrreryDashboardFrame(note_frame, status_position="bottom")`
  in place of the old note_frame block); `note_text` and its `scrolledtext`
  import both dropped as dead once the static panel was gone.
- **status_position parameter:** "right" (default) keeps the original
  960px standalone layout unchanged (status log as a fixed-width vertical
  panel); "bottom" -- used for the embed -- puts it as a fixed-height
  strip under the launch cards instead, since the narrow third-column
  pane can't fit the roomy standalone design as-is.
- **Bug found + fixed:** the status panel's fixed size (width OR height)
  wasn't actually being honored. `grid_propagate(False)` only locks a
  widget's size within its PARENT's grid cell; the panel's own children
  (header/divider/textbox) are pack-managed, and `pack_propagate(False)`
  was the missing call for that. This was a LATENT bug in the ORIGINAL
  standalone design too (the fixed-width right panel was never actually
  pinned at 270px) -- not something this session introduced, just found
  along the way. Verified by measuring actual rendered pixel dimensions
  under xvfb (90px/270px exactly, both orientations), not just reading
  the code.
- **Mouse wheel:** CustomTkinter's CTkScrollableFrame already handles
  Windows/Mac `<MouseWheel>` correctly -- ancestor-aware (only scrolls
  when the event's target widget is a descendant of its own canvas),
  verified pixel-for-pixel on a nested launch-card button -- but has no
  Linux Button-4/Button-5 binding at all. Added that, reusing the frame's
  own ancestor-check helper, matching columns 1 and 2's existing
  cross-platform coverage in palomas_orrery.py. Windows/Mac behavior was
  left untouched (already correct; duplicating it risked a double-scroll
  conflict).
- Also closes L-134 (dashboard devtools audit, same session) and L-063
  (GUI Note text update -- superseded by this replacement).
**Note:** Built across session start db5a2e5a -> Tony's integration push
(d4b7eca/d427adf8) -> this session's scroll-fix + launch-groups increment,
pushed as 6064728 -> current HEAD 6b1c8d904f. Verified at each step:
py_compile + ASCII/LF gates, xvfb live-dispatch smoke tests (standalone
AND embedded, both status_position values), a full run of the real
palomas_orrery.py with the dashboard embedded reaching mainloop clean.
**Ref:** palomas_orrery_dashboard.py; palomas_orrery.py (note_frame
block, ~line 11046); L-134; L-063.

#### [L-153] Restore "Who Tony Is" framing into resident protocol (protocol)
<!-- L:153 status:DONE upd:2026-07-21 section:C flag: rice:3/2/85/1 -->
- Context: Tony flagged on 2026-07-12 that his non-programmer/non-astronomer
  background used to be documented in the project instructions and had been
  removed in an editing pass. That flag was never captured as a ledger item
  and floated away -- same failure class as L-152.
- Verification [fetched @eb7f05dd, orrery HEAD]: grepped all versioned
  project_instructions_v*.md (v1 through v3_32) and both working_protocol*.md
  files -- zero matches for the bio framing at any version. It was never IN
  the chat protocol. It DOES exist in documentation/CLAUDE.md ("Claude Code
  Handoff", Feb 2026, "Who You Are Working With"): engineer/vibe-coder
  framing only, no artist/anthropologist -- and that file is Code-only,
  never ported to PROJECT_INSTRUCTIONS.md.
- Correction to 2026-07-12 framing: not "removed" -- "written once for Code,
  never carried to the document that reaches chat sessions and Mode 7 relay
  partners." Net effect on Tony is the same.
**Note (2026-07-20, consolidated):** Final round of additions to the
ownership paragraph: inter-model orchestration (the Mode 7 relay work
itself, distinct from the artifacts it produces) and the framing that
all of it traces to Tony's professional engineering/ops-manager
background -- the same source already cited for Procedural Criticality
in Part 2. Cross-referencing that existing section rather than
introducing a second unlinked claim about the same background.
**Gap:** None.
**Tony:** See PROJECT_ORIGIN.md in the root directory. PROJECT_INSTRUCTION.md 
updated. Claude.md is for use in Claude Code and is obsolete.
**Ref:** documentation/CLAUDE.md @ eb7f05dd; L-152 (same failure class).

#### [L-163] Module role/domain classification redesign (ROLE_MAP + MODULE_DOMAIN_MAP)
<!-- L:163 status:DONE upd:2026-07-26 section:C flag: rice:2/2/85/4 -->
- **What.** `ROLE_MAP` in `module_atlas.py` (94 hand-maintained entries)
  had drifted: 19 of 121 orrery modules silently classified as `'other'`,
  5 already carrying unscanned claim-shaped content per
  `PROVENANCE_AUDIT.md` (`shell_configs.py` alone: 91 strings). 3 real
  consumers import it (`module_atlas.py`, `provenance_scanner.py`,
  `dep_trace.py`), not 1. A second, orthogonal hand-maintained dict
  (`MODULE_DOMAIN_MAP`, in `provenance_scanner.py`) shares the same
  staleness risk on a different axis (domain, not role).
- **Design (full detail in ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md).** Both
  maps become mechanically regenerated from an explicit `Role:`/`Domain:`
  line in each module's own docstring -- same pattern `ledger_index.py`
  already uses for its INDEX zone. Missing/invalid tag -> `'undetermined'`
  sentinel (distinct from the legitimate `'other'` bucket), flagged not
  guessed. Filename heuristics demoted to suggestion-only. `__init__.py`
  exempted; `errors.py`-type modules fold into `utility`. Role code ships
  this build; Domain code (retiring `MODULE_DOMAIN_MAP`) deferred to the
  L-156 cluster.
- **Tag placement -- decided.** Footer block: `Role:`/`Domain:` on their
  own lines, blank-line separated, directly above the credit line; for
  credit-less modules, at the end of the docstring. Confirmed by Tony
  (chat review of the Phase 1 as-built, July 24 2026) -- rationale:
  `MODULE_ATLAS.md`/`MODULE_INDEX.md` already serve as the at-a-glance
  surface (Section 6), so the docstring itself stays optimized for
  uninterrupted prose rather than doubling as the quick-scan view.
- **Phase 1 (archival + repo hygiene) -- CLOSED.** [verified @7ede8a2f]
  Opus 5 builder session, July 24-25 2026; independently re-verified
  against live HEAD in chat review, not taken on the as-built alone. All
  7 archive candidates (`provenance_scanner_color_patch.py`,
  `smoke_phase4.py`, `smoke_dipole_cone.py`, `smoke_rotation_axis.py`,
  `titan_io_probe.py`, `color_map.py`, `barycenter_cache_check.py`)
  confirmed and moved to local archive; root module count 121 -> 114.
  All 7 ghost `ROLE_MAP` entries deleted (94 -> 87), zero ghosts remain.
  Phase 2 sweep scope recomputed at HEAD: 12 modules still fall through
  to `'other'` (down from 19) -- `data_inventory`, `earth_system_common`,
  `export_orbit_cache`, `food_insecurity_generator`, `ledger_index`,
  `measure_animation_html`, `measure_perframe_elements`,
  `orrery_rendering`, `scenarios_food_insecurity`, `shell_configs`,
  `skills_index`, `test_reset_completeness`. Accounting closes: 87 + 12
  + 15 (shells heuristic) = 114. `test_constants_provenance.py`
  deliberately NOT archived -- its L-160 absorption target doesn't exist
  yet. Both downstream consumers (`provenance_scanner.py`, `dep_trace.py`
  import paths) smoke-tested clean against the edited `module_atlas.py`.
  `ledger-and-session-records` bumped to 1.3 (Tony-action tag
  convention) as a side effect of this build-prep, independent of
  L-163's own content. Full detail: `AS_BUILT_L163_phase1.md`.
- **Gallery repo.** `module_atlas.py` copied to gallery repo root, gains
  an explicit `SCAN_PATHS` list (`tools/`, `gallery/assembler/` +
  `harness/`/`tests/` subdirs) rather than recursion. Own 4-value domain
  vocabulary (`gallery_pipeline`, `cache_builder`, `assembler`,
  `dev_tools`), mirroring the existing skill boundaries. Not yet built
  (Phase 3).
- **`dep_trace.py`.** Stays separate (different job), already correctly
  single-sourced when the `module_atlas` import succeeds. One real gap:
  its import-failure fallback has its own hardcoded `_shells` heuristic
  and silent `'other'` default -- duplicated logic, folded into Phase 3,
  not deferred.
- **Phase 2 (content sweep) -- CLOSED.** [verified @61e4232e (orrery),
  @57aa7592 (gallery)] Opus 5 built the tag-insertion mode; the write
  ran for real across both repos -- all 114 orrery + 22 gallery modules
  now carry a `Role:`/`Domain:` line, independently re-confirmed against
  live HEAD, not taken on the as-built. Changelog placement (8 modules)
  resolved to Tony's decision: block at the very end of the docstring,
  not wedged between entries -- confirmed on `apsidal_markers.py` (lands
  after the May 8 entry) and both gallery changelog files. Idempotent:
  re-running against the live files a second and third time changes
  nothing.
- **Two rounds of close-out gaps, both caught only by checking the
  actual written files against every decision, not by re-reading the
  as-built.** (1) A real bug: `strip_existing_tags()` matched a `Role:`
  or `Domain:` line individually rather than as an adjacent pair, so a
  wrapped sentence in `add_docstrings.py`'s own new docstring --
  starting "Domain: lines -- this legacy mode..." -- was silently
  deleted as if it were a stale tag. Fixed: strip now requires the
  literal adjacent pair; content restored and reworded so no line
  starts with either word as prose. (2) Three decisions confirmed in
  chat had not actually reached `MODULE_TAGS`: `data_acquisition`/
  `data_acquisition_distance` domain (`orrery` -> `stars`),
  `gallery_studio`/`gallery_editor` role (`gui` -> `devtool`),
  `json_converter`/`gallery_json_fixer` role (`pipeline` -> `devtool`).
  All three confirmed correct at HEAD after the fix; every one of the
  ~50 session classifications re-checked against the written files, not
  just the ones most recently mentioned. Full detail:
  `AS_BUILT_L163_phase2.md`.
- **Gallery root scope widened.** Tony's call: gallery's `SCAN_PATHS`
  now includes `'.'` alongside the four module directories, so
  root-level gallery tools (currently just `add_docstrings.py` itself)
  get classified too, matching the orrery side. Needed a real fix, not
  just the wider path: both copies share one `MODULE_TAGS` table, so
  naively adding `'.'` made gallery's drift-check think every one of the
  orrery's ~114 bare-name entries belonged to it too. Fixed with a small
  explicit `GALLERY_ROOT_FILES` allowlist plus a `SCAN_PATHS == ['.']`
  check to tell the two copies apart -- caught by testing the naive
  version first, not by reasoning it through in advance.
- **Phase 3a (re-verification before classifier code) -- CLOSED.**
  [verified @76fc9155 (orrery), @d1be9e63 (gallery)] Opus 5 builder
  session, July 26 2026; independently re-verified against live HEAD,
  including replicating the GUI-launch check myself rather than taking
  it on the as-built. One gap found: gallery's own `add_docstrings.py`
  had never actually been written (the scope-widening code was in place
  and pushed, but the write itself hadn't been run for that one file).
  Not a tool defect -- confirmed by running the preview, which correctly
  reported the single pending change. Tony ran the real write, confirmed
  by his own pasted console output (`added 1, unchanged 22, total 23`)
  and independently re-confirmed here after the push: all 137 modules
  across both repos (114 orrery + 23 gallery, gallery now including its
  own `add_docstrings.py`) carry exactly one `Role:` and one `Domain:`
  line; re-running the gallery tool a further time reports
  `unchanged 23, total 23` -- fully idempotent. `compileall` clean on
  both repos. Prose-integrity re-check (pre-sweep tree vs. current HEAD,
  every non-blank docstring line) came back 113/114 orrery clean + 22/22
  gallery clean, the one orrery exception being `add_docstrings.py`'s
  own deliberate Phase 2 rewrite -- confirmed intentional, not damage.
  GUI-launch check independently replicated: `palomas_orrery.py` under
  `xvfb` against the fully-tagged tree reached the same milestones Opus
  reported (center-body registration through Eris/Dysnomia, `[DASHBOARD]
  Dashboard ready.`, 182 object variables wired, sash positions set) --
  matched exactly, including the specific 182 count. Full detail:
  `AS_BUILT_L163_phase3a.md`.
- **Phase 3b (classifier build + close verification) -- CLOSED.**
  [verified @23de11ee (orrery), @0f8e62eb (gallery)] Opus 5 builder
  session, July 26 2026; independently re-verified against fresh
  clones of both repos at HEAD, not taken on the as-built alone.
  Classifier code shipped as scoped: `classify_role()`/
  `classify_module()` rewrite, regenerated `ROLE_MAP` marker-zone
  (mirror, never hand-edited), `SCAN_PATHS` multi-path merge, 3
  call-site updates, `dep_trace.py`'s duplicated fallback cascade
  dropped -- including the confirmed-dead `elif mod in ROLE_MAP:`
  branch. 114/114 orrery + 24/24 gallery modules classify with
  `role_source == 'tag'`, zero `undetermined`, zero tag leakage
  across all 141 `.py` files in both repos (114 + 27, 3 gallery
  `__init__.py` files correctly exempted from tagging).
  `module_atlas.py` idempotent in place; `dep_trace.py` and
  `provenance_scanner.py` both run clean through the new
  `classify_role(module_name, filepath)` signature. Full detail:
  `AS_BUILT_L163_phase3b.md`, `AS_BUILT_L163_phase3b_close.md`.
**Note:** Reviewed by Fable 5 (its own cluster) -- build-ready, land
before L-154-162 as proposed; two amendments folded in (domain
retirement joins the L-156 cluster's Phase 3, gated on this sweep
completing; sequence this sweep before L-157's Gemini worksheet).
**Gap:** None remaining. **Correction (2026-07-27, Fable 5 review,
finding 6):** this paragraph described Phase 4 as pending; it's actually
CLOSED -- `AS_BUILT_L163_phase4.md` documents all four edits applied,
`provenance-discipline` reads v1.2 and `ledger-and-session-records` reads
v1.4 at HEAD, and the Skill Manifest table in `PROJECT_INSTRUCTIONS.md`
matches. This Gap paragraph was simply never rewritten when Phase 4
closed -- a DONE item's own Gap field describing finished work as
outstanding. Left here struck-through rather than deleted, per the
project's own breadcrumb convention.

The Tier-1 findings jump this phase surfaced (105 -> 145 in-
sandbox, neither number authoritative -- see
`AS_BUILT_L163_phase3b_close.md`) is the intended effect:
`classify_role` now returns a real role for modules that used to
fall through to `'other'`, which is the L-078 coverage-widening
this track exists to enable, not a new problem. Reconciling
Tony's actual local Tier-1 baseline against this widened scope is
intentionally sequenced behind the L-154-162 provenance-scoring-
refactor cluster -- (decide, confirmed by Tony in chat, July 26
2026) this is NOT an orphaned action item and does not gate Phase
4 or any push of Phase 4's doc-only changes.

**Decided: `undetermined`** (confirmed by Tony in chat) -- matches
Fable's lean since this item shipped first; the L-156 cluster's
`UNCLASSIFIED` conforms to this name, not the other way around.
Coordinate timing with L-156 (shares `ROLE_MAP`/`MODULE_DOMAIN_MAP`
as edit sites for D10's `test_constants_provenance.py` cleanup,
and L-156 cites this item's coverage-gap pattern as its own
precedent -- this item landed first).
**Ref:** `ROLE_DOMAIN_CLASSIFICATION_HANDOFF.md` (full design, Sections
1, 4, 16, 17, 19), `AS_BUILT_L163_phase1.md`, `AS_BUILT_L163_phase2.md`,
`AS_BUILT_L163_phase3a.md`, `AS_BUILT_L163_phase3b.md`,
`AS_BUILT_L163_phase3b_close.md`, `module_atlas.py`, `provenance_scanner.py`,
`dep_trace.py`, `ledger_index.py` (pattern precedent),
`add_docstrings.py` (sweep tool, now fully closed out both repos),
`PROVENANCE_AUDIT.md` (July 17, coverage-gap evidence),
`MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 6 (companion entry);
L-078 (role-driven coverage-widening track);
L-154/155/156/157/158/159/160/161/162 (provenance scoring refactor
cluster).

#### [L-114] objects_config.json stranded by the atomic swap; also blocks crash-recovery (gallery builder)
<!-- L:114 status:DONE upd:2026-07-27 section:C flag: rice:3/3/90/0.5 -->
- **What.** In gallery_cache_builder.py (GALLERY repo) the config was read from
  inside data/solar-system/ -- the exact directory the whole-generation atomic
  swap (atomic_swap_dir) replaces wholesale. It is only ever READ there, never
  copied into staging like coverage_index.json / feature_configs.json are, so
  every successful real (non-dry-run) build silently swapped it away into
  data/solar-system.prev/, invisible until the next command hit
  FileNotFoundError. Found live 2026-07-11 (Sonnet 5 live-gate) on the real
  --first-build.
- **Compounding failure.** main() calls load_config() BEFORE run_build(), hence
  before recover_incomplete_swap(). A real crash mid-swap leaves the live dir
  missing (only .prev holds the config), so load_config() dies before the
  self-healing recovery can run -- no built-in path back. Reproduced live.
- **Fix (chosen: move OUT, not copy in).** Relocate the config to
  data/objects_config.json, a sibling outside the swap blast radius. Closes
  BOTH failure modes at once -- the swap can't strand it, and load_config() no
  longer depends on a directory a crash may have left mid-swap. atomic_swap_dir
  and cleanup_stale_siblings only touch dirs named after out_dir, so a sibling
  file is never in scope (verified by reading both).
- **State at gallery HEAD 661cddb [verified @661cddb].**
    - DONE + committed: the config file now lives at data/objects_config.json
      (Encke 90000091 fix included); data/solar-system/objects_config.json is
      gone (404).
    - NOT yet applied: gallery_cache_builder.py still DEFAULTS --config to the
      OLD path (line ~1085), so a bare --nightly / --first-build at HEAD
      FileNotFoundErrors on the default -- only explicit
      --config data/objects_config.json works. HEAD is half-fixed (file moved,
      code not); that is why status is OPEN, not DONE.
- **Gap.** Apply FOUR edits and push, then re-run the offline suite from a clean
  clone as the acceptance check: (1) gallery_cache_builder.py argparse --config
  default -> 'data/objects_config.json'; (2) its module docstring (new config home
  + operational notes); (3) test_gallery_cache_builder_offline.py:79 ->
  data/objects_config.json (+ the line-77 comment); (4) orrery
  documentation/TESTING_PROTOCOL.md:25 config-path prose. The moved config had
  FOUR consumers -- builder default, offline-test primary path, offline-test
  comment, TESTING_PROTOCOL prose; the first fix swept two, Fable's F1 caught the
  other two. Acceptance = the offline suite passes from a clean checkout (that
  green run IS the proof every consumer moved). All four drafted + verified
  2026-07-12; on push, flip to DONE and re-pin the gallery SHA.
**Tony:** RICE proposed 3/3/90/0.5 (hits every real build; tiny effort, file
already moved) -- yours to finalize.
**Ref:** GALLERY tools/gallery_cache_builder.py (argparse --config default;
load_config; atomic_swap_dir; recover_incomplete_swap; main() call order).
L-098 (parent). Found 2026-07-11 (Sonnet 5); fixed 2026-07-12 (Opus 4.8).
**Closed 2026-07-27:** all four Gap edits confirmed at gallery HEAD
`0f8e62e` (Fable 5 review + Sonnet 5 independent re-run of the offline
suite from a fresh clone -- PASS, 138 checks, 0 failures, matching the
entry's own stated acceptance check). Tony confirmed no local un-pushed
edits remain. `ledger_index.py` will retag this to section C and move it
into the general archive on next run -- expected, not an error.  

#### [L-062] README refresh -- fold in handoff + ledger developments
<!-- L:062 status:DONE upd:2026-07-28 section:C flag: rice:3/2/85/1 -->
- **README review/refresh.** Review the repo README against its last update and
  fold in developments captured since in the handoffs and this ledger (Movement
  track complete, animation engine, item-19.3 axis control, shell-consolidation
  refactor complete, Gallery/Studio round trip, Earth System track). Goal: a
  current public-facing description matching what the code actually does. Paired
  with L-063 (in-GUI Note) -- both are user-facing text that has drifted from
  project state.
- **Staged scope, decided 2026-07-17 (Tony + Sonnet 5), because Tony noticed
  the drift firsthand on the live GitHub page.** Split into a do-now half
  and a defer half, not one pass:
  - **Do now, no gallery dependency:** date/version stamp, module/LOC
    stats (verified stale below), a visible Requirements section, every
    doc cross-reference link (verified BROKEN below), and folding in
    non-gallery feature/capability drift since May.
  - **Defer until the interactive gallery goes live:** the "Web Gallery"
    section's architecture description ONLY. It should still describe the
    CURRENT, publicly-linked gallery (palomasorrery.com, the
    HTML-export -> json_converter.py -> GitHub Pages pipeline) as it
    exists today -- not omit gallery coverage entirely. What's deferred is
    the in-progress Phase 2 Solar System Assembler / interactive rework
    (L-098 onward, this week's M1/M2) -- unreleased, not publicly linked,
    still changing week to week; documenting it now risks a second
    rewrite almost immediately.
  - **Audience reframing (Tony, 2026-07-17):** primary audience shifts to
    the DEVELOPER, even though the repo is public -- away from the
    current beginner/end-user hand-holding tone (the multi-page
    "Step-by-Step Installation Guide for Beginners" walkthrough reads for
    a non-technical download-and-click audience). Five purposes, in
    order, Tony's own framing: (1) general project information; (2)
    pointers to key organizational structure and documents -- focused on
    the orrery, may mention the gallery, written for a developer reader;
    (3) orientation on cloning/using the repo, especially that the
    released data files are NOT in the active repo (gitignored, obtained
    from Releases); (4) the gallery as it currently, publicly exists --
    not the unreleased interactive work; (5) a brief mention of data
    sources and citation discipline (-> PROVENANCE_AUDIT.md).
- **Concrete staleness findings, this session (verified against live HEAD
  `2991a0c7`, not assumed):**
  - Module/LOC claim wrong: README says "75+ Python modules, over 78,000
    lines of code" -- actual count at HEAD is 121 Python files, 106,476
    lines.
  - Last-updated stamp: May 4/May 2026 (v2.9.0) vs. today -- 2+ months,
    and the entire Phase 2 gallery-cache-builder track (L-098 through
    L-126, including this week's M1/M2 trust-measurement work) missing
    from the changelog line.
  - **Every doc cross-reference link in the README is broken.**
    `MODULE_INDEX.md`, `climate_readme.md`, `social_media_readme.md`,
    `web_gallery_handoff.md`, `wet_bulb_temperature_readme.md` are all
    linked repo-root-relative, but all five actually live under
    `documentation/` -- confirmed by direct path check. 404 on GitHub
    today, independent of anything gallery-related.
  - No visible Requirements citation (Tony's original observation):
    `requirements.txt` carries real, carefully-maintained content
    invisible from the README -- pinned-version rationale (kaleido
    locked at 0.2.1, with the reason why), a full Python 3.14
    compatibility section (which packages break, which don't, what to
    monitor), and the Plotly 6.x/kaleido 1.0 upgrade path. The README
    only says "pip install -r requirements.txt" and a sample `pip list`
    -- none of this surfaces.
- **Routing decided:** the do-now half goes to Fable as a manifest-style
  task (broad-first surface-and-organize, real latitude, not a design
  session) -- see FABLE_TASK_README_REFRESH.md. Tony reviews the diff
  before merging, same as any Fable deliverable.
 **Claude:** [verified 2026-07-28, live HEAD] Done. `README.md` (535 lines)
built by Fable, reviewed independently against live HEAD (not just
trusted): all 12 relative links resolve, ASCII/LF clean, module/LOC
stats sourced from the regenerated atlas rather than hardcoded, the
corrected throughline in place (personal tool first; the gallery is the
sharing vehicle, not a parallel intended audience). Old README archived
to `documentation/README_5_4_26.md`. One follow-on found during Fable's
own re-verification pass -- root's stale `ORBITAL_MECHANICS_README_v3_1.md`
-- has since been removed (2026-07-28). Fable's remaining "open questions"
list (beginner-content disposition, whether four documentation/ readmes
move to root, three unlinked root docs, docs/ folder purpose) is recorded
in `documentation/README_CHANGE_NOTE.md`, left pending -- a separate
future pass if wanted, not part of this item's close. 
**Gap:** (1) send the Fable prompt, get the diff back; (2) Tony + Sonnet
review against the 5 purposes and the concrete findings above; (3) commit;
(4) revisit the Web Gallery section specifically once the interactive
assembler is publicly linked (separate future pass, not blocked on
anything else in this item).
**Ref:** L-063 (paired, in-GUI Note); L-098 (Phase 2 parent, why the
gallery section is deferred); FABLE_TASK_README_REFRESH.md (this
session's Fable prompt); requirements.txt; PROVENANCE_AUDIT.md.
**Claude:** RICE proposed 3/2/85/1 (reach raised -- this is the repo's
public front door, not an internal doc; impact ticks up, broken links
and wrong stats are a real credibility/usability issue, not purely
cosmetic; confidence high, concrete claims verified directly this
session rather than assumed; effort stays low, Fable-suited assembly
work) -- yours to finalize.

#### [L-127] module_atlas.py generates MODULE_INDEX.md too -- single source, eliminate divergence
<!-- L:127 status:DONE upd:2026-07-28 section:C flag: rice:2/2/80/1 -->
- **The ask (Tony, 2026-07-17):** one script run produces BOTH
  MODULE_ATLAS.md (full report, existing) and MODULE_INDEX.md (current
  thematic/prose style, current data) -- same pattern as L-097
  (skills_index.py auto-generating the Skill Manifest table): kill a
  hand-maintained sibling by generating it from the same scan as its
  always-current relative, rather than hoping two files stay in sync by
  discipline alone.
- **Real design fork, not just an implementation detail:**
  (a) Mechanical-only -- module_atlas.py already extracts docstrings,
  functions, role tags, deps/consumers per module. MODULE_INDEX.md gets
  formatted straight from that data. Fully deterministic, no new
  dependency, same philosophy as the existing script. Honest cost: the
  current MODULE_INDEX.md's synthesized narrative ("Core visualization
  functions: plot_objects() generates...") isn't a docstring dump -- it
  reads like curated prose. Some modules' docstrings won't support that
  quality yet, so some entries will read thinner on day one. That's a
  healthy pressure toward better docstrings, not a bug, but it's a real
  step down for a few modules until they catch up.
  (b) AI-assisted -- script does the scan, a Claude pass writes the
  prose from it each time. Closer to today's quality; no longer one
  deterministic script run, so less "automated" in the sense Tony asked
  for.
  Leaning (a) for consistency with the project's existing devtool
  philosophy (ledger_index.py, skills_index.py) -- Tony's call to
  finalize, not decided here.
- **Grouping reconciliation needed either way:** MODULE_INDEX.md's
  current sections (Core Applications, Orbital Mechanics & Calculations,
  Cache Management, Stellar Visualization Pipeline, etc.) don't map 1:1
  onto module_atlas.py's existing ROLE_MAP tags (gui, rendering,
  rendering/shells, computation, data, cache, pipeline, scenario,
  utility, devtool, other). Extend ROLE_MAP with the finer categories, or
  adopt the coarser existing tags as MODULE_INDEX's new section headers
  -- an actual decision the implementation has to make, not a detail to
  paper over.
- **Not urgent, not blocking.** The immediate need (accurate numbers in
  the README, right now) is already handled -- MODULE_ATLAS.md was
  regenerated fresh this session (121 modules, 953 functions, 91,851
  lines, July 17) and the Fable README prompt was corrected to source
  from that instead of the stale MODULE_INDEX.md. This item is the
  structural fix so this class of drift can't recur, not a blocker on
  anything in flight.
**Gap:** (1) reconcile ROLE_MAP against MODULE_INDEX's current thematic
groupings; (2) extend module_atlas.py to emit MODULE_INDEX.md from the
same AST scan pass, as a proper generated index (mechanical-only,
settled 2026-07-17) -- same marker-based-zone pattern as
ledger_index.py/skills_index.py where practical; (3) BOTH outputs write
to repo ROOT, not documentation/ -- matching where MODULE_ATLAS.md
already lives, matching the root/documentation split already in force in
this repo (11 current-reference files at root vs. 506 historical files
in documentation/), and fixing the README's existing MODULE_INDEX.md
link at its root cause rather than just correcting the link syntax; (4)
Tony renames the existing hand-curated documentation/MODULE_INDEX.md to
an archival copy (matching the _superseded convention already used for
LEDGER_orrery_consolidated_superseded.md) before the new generated
version takes its place at root.
- **Done (Tony, 2026-07-17):** orphaned stale documentation/MODULE_ATLAS.md
  duplicate (April 14, 86,139 lines) removed.
**Claude:** [verified 2026-07-28, live HEAD] Done, in full. All four Gap
items closed: `module_atlas.py` now generates both `MODULE_ATLAS.md` and
`MODULE_INDEX.md` from one scan (mechanical-only, fork (a) chosen); both
write to repo root; the hand-curated `documentation/MODULE_INDEX.md` was
renamed to `documentation/MODULE_INDEX_old.md` before the generated
version took its place. ROLE_MAP reconciliation (Gap item 1) went further
than this item's own scope -- see L-163 (DONE, 2026-07-26), which
redressed 19/121 modules silently misclassified as 'other' and added a
docstring-tag-driven MODULE_DOMAIN_MAP on top of the infrastructure this
item built. Confirmed live: current MODULE_INDEX.md header reads
"Generated: July 26, 2026 by module_atlas.py".
**Ref:** module_atlas.py; documentation/MODULE_ATLAS.md;
documentation/MODULE_INDEX.md; L-097 (skills_index.py, same pattern,
precedent RICE); ledger_index.py (original precedent); add_docstrings.py
(existing docstring-batch tool, may be relevant to the docstring-quality
dependency in option (a)).
**Claude:** RICE proposed 2/2/80/1, matching L-097's precedent for this
class of devtool/process work (modest reach -- internal tooling, not
user-facing; real but not huge impact; high confidence, same proven
pattern as two existing scripts; low effort, extends existing code
rather than building new) -- yours to finalize.

#### [L-169] Gallery/Studio track -- repo structure reference
<!-- L:169 status:DONE upd:2026-07-28 section:C flag: rice:1/1/95/0.5 -->
- **What.** This reference sat as unlabeled prose under the "## H."
  header since the June-10 consolidation -- Tony flagged it ("needs
  L-number, header, and update") but it was never converted. Closing
  that gap, and re-verifying every claim fresh rather than just wrapping
  the old prose as-is.
- **Repo source.** https://github.com/tonylquintanilla/tonyquintanilla.github.io
  -- owner WITH the 'l', repo name WITHOUT; branch main; public; custom
  domain palomasorrery.com. Studio file confirmed still at
  `tools/gallery_studio.py` (NOT root) [verified 2026-07-28 @d49fd0b3].
- **Docs split**, both sides re-confirmed present [verified 2026-07-28]:
  gallery repo `documentation/` holds `web_gallery_handoff.md` +
  `3d_axis_control_handoff.md`; orrery repo `documentation/` holds the
  encounter-export design set incl. `ENCOUNTER_EXPORT_HANDOFF_v3.md`.
- **"Low-activity" framing in the section title is now stale.** True as
  of June 10; not true today -- gallery-cache-builder/gallery-assembler
  work (L-098, L-149-151) and the interactive-gallery Phase 2 push have
  made this repo an active track. Section title left untouched
  (structural, not this item's call); flagging so a future session
  doesn't inherit a stale "low-activity" assumption.
- **No Studio running ledger** by design -- still holds; stand one up
  only if Studio-specific (not builder/assembler) work resumes in volume.
- **Joined items already correctly cross-referenced, not orphaned:** N6
  = L-046 (OPEN), item 19 = L-040 (OPEN) -- both carry proper L-handles
  and live in their own sections; this was always a pointer, not a
  duplicate home.
**Gap:** none -- reference/structure note, not an action item.
**Ref:** L-046, L-040, L-098, L-149, L-150, L-151.

#### [L-166] F1b: per-object trust enforcement + soft-edge trust UX (resolver/client consumption of served trust blocks)
<!-- L:166 status:OPEN upd:2026-07-28 section:W.Active flag: rice:2/3/80/2 -->
- **What.** F1a (M2) serves per-object trust blocks nightly, dormant -- nothing
  consumes them. F1b is the consumption side: resolver.py/cache_reader.py read
  per-object windows instead of the one global gate (L-149 limitation note;
  L-150 gap, binaries-scoped line); global served_window demoted to an outer
  sanity bound. Touches locked code: deliberate golden-fingerprint re-open
  (L-080 harness), one small reviewed diff, not absorbed silently.
- **UX design (converged in the July 2026 Mode 7 trust-bound relay, Sonnet 5 +
  Fable 5; Tony's stated preference: indicator, not hard block):** shaded
  high-confidence band on the date picker; per-object degradation past each
  object's own window (fast moons ghost first -- teaches perturbation);
  along-track uncertainty arc rendered from the served error rate
  (Show-the-Envelope convention, made literal); positive framing ("range we
  can vouch for"); hard OutOfServedWindowError reserved for an outer sanity
  cap only. Client cost is O(1) arithmetic per scrub tick -- rate is served.
- **Riders, capture-not-decide:** (1) tolerance_deg=0.5 adopted as a global
  constant; whether tolerance eventually belongs to the VIEW (scene-scale vs
  close-up) is open -- adjacent to L-150's scale-of-view voting. (2) Trust
  window must not span a known close encounter (two-body invalid across it);
  moot for Apophis today (323.5 d window vs 2029), stops being moot as 2029
  approaches -- cross-note with L-126.
**Gap:** design session first (fingerprint re-open scope + UX wiring), then
build. Sequence relative to L-154 (feature JS layer) is Tony's call.
**Ref:** L-118/L-149 (F1a, closed), L-150, L-126, L-080 (fingerprint),
M2_IMPLEMENTATION_REPORT.md, FABLE_PROMPT_served_window_trust_bound_v0_1.md
and its response (July 2026 relay); resolver.py resolve() (~91-106).

#### [L-178] Earth shadow constants -- EARTH_RADIUS_KM duplicate + mean vs equatorial mixing
<!-- L:178 status:DONE upd:2026-08-05 section:C flag: rice:3/3/40/2 -->
- Fable findings #33-36. `earth_visualization_shells.py` defines
  `EARTH_RADIUS_KM = 6371.0` twice (lines 907, 1019). This is the mean
  radius; constants_new.py has equatorial 6378.137 and polar 6356.752
  but no mean radius. The derivation of AU_PER_KM mixes the
  equatorial-based EARTH_RADIUS_AU with the mean 6371 denominator --
  a built-in ~0.11% error.
- Also: GEO scatter comment claims "+/-0.0002 AU (~30 km at GEO)" but the
  code computes +/-0.0002 x EARTH_RADIUS_AU ~ +/-1.3 km. And GEO hover
  text is missing the AU equivalent (standing convention gap).
- No Shadow Constants gate (provenance-discipline v1.3) applies to the
  local EARTH_RADIUS_KM.
**Note (2026-08-05):** Resolved without answering mean-vs-equatorial -- the
question is deleted rather than decided. Both local shadow constants are
removed and the conversion goes directly through `KM_PER_AU`
(`AU_PER_KM = 1.0 / KM_PER_AU`), correct regardless of which Earth radius
anything else uses. Note the ledger title says "shadow constants" but the
affected code is LEO/GEO band geometry; no umbra/penumbra geometry is
involved, so no physics decision was needed. Verified: GEO belt
42,212 -> 42,165 km (target 42,164); LEO band 6578/8380 -> 6571/8371 km,
now matching its own declared LEO_LOW_KM / LEO_HIGH_KM constants, which it
did not before.
**Note:** GEO radial scatter left unchanged at +/-0.0002 Earth radii
(~1.3 km) -- the comment claimed ~30 km and real station-keeping bands run
to tens of km, so the comment was corrected to describe the code and the
widening flagged in-code as a Mode 5 call for Tony.
- Tony-action (do): run `patch_earth_L178.py`, push, then close.
**Closed 2026-08-05 at `06daa8b825c93d8968a46a1edb2f5083610ef665`.** Patch
run and pushed; Mode 5 confirmed by Tony -- GEO hover reads 42,164 km /
0.000282 AU and the LEO band sits on its declared 200/2000 km altitude
bounds. Shadow constants removed; mean-vs-equatorial no longer arises here.
[verified @06daa8b]
**Ref:** FABLE_shell_consistency_audit_report.md findings #33-37;
patch_earth_L178.py; L-182 (same session).
**Ref:** FABLE_shell_consistency_audit_report.md findings #33-37.

#### [L-182] Mars Hill sphere -- cross-check correction lost across the config pipeline
<!-- L:182 status:DONE upd:2026-08-05 section:C flag: rice:3/4/100/1 -->
- The Aug-1 Mars cross-check found `324.5 R_Mars` unsourceable and derived
  ~1.084 Mkm (worksheet D2: "no page publishing a Mars Hill radius of 324.5
  R_Mars"). `patch_mars_cross_check.py` corrected 5 sites but targeted
  `mars_visualization_shells.py` ONLY -- the correction never reached
  `shell_configs.py`, so the live render kept 324.5 the whole time.
- The Aug-4 Fable shell audit saw module=320 vs config=324.5 and read the
  config as authoritative; the geometry prompt encoded that ("live config
  already says 324.5"); the Aug-4 geometry patch then harmonized the module
  UP to 324.5, erasing the last copies of the corrected value. Net effect:
  the correction was removed from the codebase entirely, and the render was
  never right at any commit.
- At the pre-fix HEAD the module carried a two-leg `# Cross-checked:`
  citation asserting ~320 R_Mars three lines above display text asserting
  324.5 -- a SOURCE_VS_VALUE contradiction created by the harmonization.
- Resolved value: **319.2 R_Mars** = 1,084,000 km / 3,396.2 km equatorial
  (Archinal et al. 2018, the project's `CENTER_BODY_RADII['Mars']`). The
  worksheet's 319.8 is the same 1.084 Mkm over the volumetric mean radius
  3,389.5 km; this project uses equatorial where oblateness matters.
- Class: a Check All Parallel Pipelines failure (resident CRITICAL gate),
  not a value error. Both patches touched one side of a two-copy pair -- the
  first fixed the module and missed the config, the second aligned the
  module to the config that had never been fixed.
**Note:** Surfaced by the Fable skills-layer review, which flagged the
provenance-discipline worksheet example ("Hill sphere 324.5 should have
been 320") as contradicting orrery-coding-conventions. Fable rated it HIGH
and diagnosed it as a pending perihelion-vs-semi-major convention question;
the worksheet showed the opposite -- a settled correction silently reverted.
The audit found the right contradiction from the skills alone and could not
resolve its direction, because the cross-check worksheets were not in the
audit prompt's Materials list. Include them next time.
**Note:** Prevention candidates for Tony to weigh -- (a) a cross-check patch
must enumerate every consumer of a corrected value before delivery, the way
the geometry follow-up now does; (b) a harmonize step must state WHICH copy
is authoritative and cite the worksheet that makes it so, rather than
inferring authority from which copy happens to be live.
- Tony-action (do): run `patch_mars_hill_correction.py` and
  `patch_shell_configs_mars_hill.py`, then push and record the SHA here.
**Closed 2026-08-05 at `06daa8b825c93d8968a46a1edb2f5083610ef665`.** Both
patches run and pushed; Mode 5 confirmed by Tony -- the Mars Hill shell is
visibly smaller and the hover reads 1.08 Mkm. Every live and dead copy now
reads 319.2 R_Mars. [verified @06daa8b]
**Ref:** worksheet_claude_mars_visualization.md D2;
documentation/patch_mars_cross_check.py (module-only target);
patch_mars_dead_copies.py (the reverting patch);
FABLE_skills_layer_review_report.md Job 2 #8 / Job 3 #1; L-181.

#### [L-179] Solar gravitational influence -- 150,000 vs 126,000 AU mismatch
<!-- L:179 status:DONE upd:2026-08-07 section:C flag: rice:4/3/40/3 -->
- Fable findings #29-30. constants_new.py defines
  GRAVITATIONAL_INFLUENCE_AU = 150,000 (with an honest note: 100k-200k
  range). solar_visualization_shells.py citations at lines 50 and 174
  both claim the constant is 126,000. Display text says 126,000 AU.
  Shell renders at 150,000 AU. Classic dual-pipeline drift -- someone
  moved one copy.
- Three-model cross-check needed to decide the correct value.
- **FIRST STEP OF PHASE 2 TRACK 0** (Tony's ordering ruling,
  2026-08-07; Fable sequencing note). Migrating and deriving before
  this value is settled would transport a known-inconsistent number
  into the gallery artifact, the served cache, and the hover text --
  authoritative-looking in three more places. Settle it first, as
  Track 0 work rather than as a gate in front of Track 0.
- **RULED (Tony, 2026-08-07): 150,000 AU stands.** His reasoning:
  it is the range interpolation from the cross check -- the midpoint
  of the published 100,000-200,000 AU spread. The store already held
  150,000 (corrected 2026-08-02); every divergent copy was downstream.
- **DONE 2026-08-07, pushed at `17dab34`** (base `d38d314`,
  patch_L179_L180_derivation_v3.py). Five sites corrected, and the
  approach is derivation rather than replacement: no display figure
  is typed any more. Added to `constants_new.py`:
  `GRAVITATIONAL_INFLUENCE_RANGE_AU = (100000, 200000)` as DATA, and
  `AU_PER_LIGHT_YEAR` derived from `SPEED_OF_LIGHT_KM_S` and
  `KM_PER_AU`. `GRAVITATIONAL_INFLUENCE_SENTENCE` in
  `solar_visualization_shells.py` builds the statement once; both
  duplicate display strings reference it.
- **Per Tony's ruling the text carries the ENVELOPE, not the point.**
  Rendered: "extends to roughly 2.4 light-years (~150,000 AU).
  Published estimates range 100,000-200,000 AU (1.6-3.2 light-years);
  this visualization draws the midpoint." Show-the-Envelope applied
  to a model-dependent quantity: the midpoint is a choice, and the
  hover says so rather than implying a measurement.
- **The geometry was never wrong.** `create_sphere_points` has drawn
  at 150,000 AU since 2026-08-02; the import chain from the store
  through `planet_visualization_utilities.py` is clean, with no
  shadow constant. Only the words had drifted. One store correct,
  four restatements adrift, every offline test passing throughout --
  L-181's thesis demonstrated in miniature.
- **Two citations were asserting a value the store did not hold**
  (`GRAVITATIONAL_INFLUENCE_AU=126000` at lines 50 and 174). One of
  them cited the constant for a string that states no such figure at
  all. Cite-to-clear caught in the wild: both passed every scanner
  run precisely because they were cited.
- **`palomas_orrery.py` line 10295 was the hard case** -- a bare
  "126,000 AU" in a scale-suggestion tooltip with no import and no
  link to the store. Now interpolated. Nothing mechanical would have
  found it; it is wrong only RELATIVE to a value in another file.
- **The whole divergent class was enumerated, not assumed.** A
  20-line check over all 157 Python files and 35 store constants,
  looking for citations that name a constant and state a value
  disagreeing with it, found exactly three sites: two here and one
  in L-180. The class is closed. The scanner is blind to it by
  construction (it flags UNCITED claims), which is why they
  survived. That check is the seed of L-189.
- Verified after the push: scanner Tier-1 unchanged at 206, no file's
  Tier-1 rose, +2 Tier-2 from the new constants registering as
  claims. SHA round trip confirmed against `17dab34`.
- Field note, recorded in safe-file-editing 1.3: the delivery hit a
  CRLF working copy whose content was byte-identical to the repo,
  and the patch harness read that as BASE MOVED. Fingerprint content,
  not raw bytes; translate anchors to the file's own convention.
  Nothing was edited on Tony's side and git was right all along.
**Gap:** None. Closed.
**Ref:** patch_L179_L180_derivation_v3.py (pushed `17dab34`);
FABLE_shell_consistency_audit_report.md findings #29-30;
FABLE_REVIEW_feature_constant_unification.md sequencing note.

#### [L-180] Solar chromosphere -- three inconsistent extents in one shell
<!-- L:180 status:DONE upd:2026-08-07 section:C flag: rice:3/3/30/2 -->
- Fable finding #31. Chromosphere shell text says "Radius: from
  Photosphere to 1.5 Solar radii" and also "about 2,000 kilometers"
  (~1.003 R_sun). Shell renders at constants_new.py CHROMOSPHERE_RADII
  = 1.1 R_sun (~0.00512 AU). Three different extents: 2,000 km
  (physical), 1.1 (drawn), 1.5 (claimed).
- The drawn value is a declared stylization (there's a code comment).
  The text should say "drawn at 1.1" and note the physical extent.
- **FIRST STEP OF PHASE 2 TRACK 0** (2026-08-07). Same reasoning as
  L-179: do not transport an unsettled value into three more places.
- **RULED (Tony, 2026-08-07): 1.1 stands as the drawn value; the
  other figures change to match.** The drawn shell is a declared
  stylization and the text now says so instead of implying a
  measurement.
- **DONE 2026-08-07, pushed at `17dab34`**, same patch as L-179.
  Added to `constants_new.py`: `CHROMOSPHERE_PHYSICAL_KM = 2000.0`
  (Carroll & Ostlie Ch. 11) and `CHROMOSPHERE_PHYSICAL_RADII`,
  derived as `1 + CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM`. Both
  drawn and physical extents are now first-class stored values that
  answer different questions.
- `CHROMOSPHERE_RADIUS_LINE` builds the statement once; both
  duplicate display strings reference it. Rendered: "drawn from the
  photosphere out to 1.1 solar radii (~0.00465 - 0.00512 AU). This is
  a stylization for visibility: the physical chromosphere extends
  only ~2,000 km above the photosphere (~1.003 solar radii)."
- The third extent (1.5) lived only in a `# Source:` comment claiming
  the store held that value; the store has held 1.1 since 2026-08-02.
  Corrected, with the erratum recorded at the site.
- Note for whoever writes the next erratum: the divergence check
  (L-189) initially fired on these very notes, because a comment
  saying "X was wrong" contains the same NAME=value shape as a
  comment asserting X. The notes were reworded rather than the
  checker taught exceptions -- a check that fires on its own fix is
  one people learn to ignore.
**Gap:** None. Closed.
**Ref:** patch_L179_L180_derivation_v3.py (pushed `17dab34`);
FABLE_shell_consistency_audit_report.md finding #31;
FABLE_REVIEW_feature_constant_unification.md sequencing note.

#### [L-189] Provenance scanner: run history and run-to-run delta
<!-- L:189 status:DONE upd:2026-08-11 section:C flag: rice:3/4/80/2 -->
- **Tony's request, 2026-08-07:** "could the scanner keep a log of
  results by date so we can track this? maybe the last 6 runs."
  Raised after a session where the only way to learn whether a patch
  had ADDED findings was for Claude to diff two committed copies of
  `PROVENANCE_AUDIT.md` from two commits -- which needs repo access
  and a script, and is therefore not a check Tony can run.
- **The number that matters is the DELTA, and it belongs on the
  console** where the push call actually gets made -- not in a file
  that has to be opened. "206 Tier-1" answers nothing on its own;
  "206, unchanged, and no file's Tier-1 rose" answers the question.
- Shape: `data/provenance_history.json`, a ring buffer of the last 6
  runs. Per run: timestamp, repo HEAD SHA (readable from `.git`
  without a git command), per-tier counts, per-domain counts, and
  Tier-1 per file. Console prints the delta after the priority
  summary and NAMES any file whose Tier-1 rose. `PROVENANCE_AUDIT.md`
  gets a matching Run History table.
- **Tony's call, 2026-08-07: TRACK the history file in git.** When an
  audit was taken and against which SHA is itself provenance. Cost is
  one small file showing as modified after each deliberate run.
- Stays INFORMATIONAL. The scanner's own comments are emphatic that
  Tier-1 never gets an auto-exit gate at any threshold; history makes
  the judgment better informed, it does not automate it.
- Build note: the scanner scans itself, so this change will nudge its
  own findings count. The first run after it lands shows a delta that
  IS the change; have it say so rather than let it read as a
  regression.
- Seed already written: the 20-line divergence check from the L-179
  session, which finds citations naming a constant and stating a value
  that disagrees with the store. It caught all 3 sites in the codebase
  and the scanner cannot -- it flags UNCITED claims, and these were
  cited. Worth folding in as a checker in its own right.
**Note (2026-08-11): BUILT AND VERIFIED.** New module
  `provenance_history.py` (444 lines) plus eight anchored edits to
  `provenance_scanner.py`, applied by
  `patch_L189_run_history.py`. Shipped at `dea0bc0`.
- Shape is the 2026-08-07 ruling unchanged: one
  `data/provenance_history.json`, ring buffer of the last 6 runs,
  tracked in git. The per-run FIELDS follow the gallery cache
  builder's existing record vocabulary (`run_id` as a compact UTC
  stamp, `started`, `finished`, `mode`) rather than inventing a
  second one. Its one-file-per-run LAYOUT was not adopted: the
  builder runs nightly, the scanner runs several times in a working
  session, and the 23 files accumulated in the gallery repo since
  July show what that costs in the changed-files list.
- **Cadence declared: 1 day, compared by calendar DATE** (Tony,
  2026-08-11) -- once per day, not at a fixed time, because the run
  is manual. A file that only accumulates runs cannot report a run
  that never happened; the declared number is what makes the
  missing run detectable.
- Console prints the DELTA after the priority summary and before
  the Tier-1 banner, and NAMES any file whose Tier-1 rose. Files
  whose Tier-1 fell are not named: a drop is the outcome the work
  aims at, and naming it competes with the thing needing a call.
  `PROVENANCE_AUDIT.md` carries a Run History table ahead of the
  risk matrix.
- Informational only. The exit code is untouched, per the scanner's
  standing design review section 3c.
- **First-run cost, predicted and attributable: 879 -> 882
  findings.** The three are the new module's own SCHEMA_VERSION,
  MAX_RUNS and EXPECTED_CADENCE_DAYS -- all Tier 3, all
  `dev_tools`, Tier-1 unchanged at 206. The console says so on the
  first run rather than letting the jump read as a regression.
  **(decide)** whether those three earn `provenance_exceptions.json`
  entries: they are configuration, not factual claims, which is the
  textbook shape of an accepted residual.
- **`is_overdue()` and `overdue_lines()` ship UNCALLED, by design.**
  A scanner that is running cannot report that it did not run, so
  the staleness check cannot live inside the thing it watches.
  L-188 is the trigger; L-189 is the data. The module docstring
  says this explicitly so a later session does not remove them as
  dead code.
- The divergence checker noted above stays OUT of scope. It flags
  CITED claims that disagree with the store, where the scanner
  flags UNCITED ones -- a different check, and it belongs with
  L-190's reach work.
- **(do)** move `patch_L189_run_history.py` out of the repo root
  into `documentation/` (alongside `patch_dashboard_manual_builder
  .py`). It was committed to the root at `dea0bc0`; it is spent,
  its base fingerprint no longer matches, and while it sits there
  the scanner counts 119 files instead of 118 and `module_atlas.py`
  reports one undetermined module.
**Note (2026-08-11), measurement kept from the cadence discussion.**
  Every trust window in the gallery served cache is set by its
  CATEGORY CAP, never by measured propagation error -- across all
  eleven objects carrying a trust block, the error test has never
  been the binding constraint. Apophis alone binds the global
  served window: 647.0868619950488 days, identical to the served
  window's own width to the last digit, recentered on build time.
  The per-object windows that look alarming -- Io +/-5.3 hours,
  Charon +/-19 hours, Titan +/-2.0 days, Moon +/-3.4 days, Pluto
  +/-6.4 days -- are excluded from the global gate by frame per
  L-149 and are enforced by nothing. Tony's call: NOT its own
  ledger item, because the practical cost is sub-pixel. On a plot
  where the orbit spans 400 pixels the worst case (Moon) is about
  0.15 px after a day and 1.1 px after a week, and the orbit SHAPE
  does not degrade at all, being geometric. It is a gate that does
  not fire, not a picture that is wrong. Recorded here so the next
  session to find Io's five-hour window does not re-raise it.
**Verification:** sandbox clone at `df7ca50` -- patch applied,
scanner run three times, ring-buffer trim at 6, corrupt-file
tolerance, HEAD SHA read without invoking git, and the Tier-1-rose
path exercised against real per-file counts. Confirmed on Tony's
machine at `dea0bc0`: 882 findings, 206 Tier-1, dev_tools 39.
`[verified @dea0bc0]`
**Gap:** none -- move to section C.
**Ref:** `provenance_history.py`; `patch_L189_run_history.py`;
`documentation/HANDOFF_20260811_L189_run_history.md`; L-188 (the
staleness caller); L-190; L-184.

#### [L-188] Maintenance runner -- one command, the whole suite
<!-- L:188 status:DONE upd:2026-08-12 section:C flag: rice:3/3/70/2 -->
- **CLOSED 2026-08-12.** `maintenance_run.py` shipped at `cfff5b5`, and
  the dashboard wiring with it. Four generators, then eight checkers,
  then one summary; about 30 seconds on Tony's machine. It reports and
  continues rather than stopping at the first failure (Tony's ruling:
  he pastes the output back, so the whole picture in one pass is worth
  more than an early exit), and it REGENERATES by default rather than
  offering a check-only mode -- "a regenerate step may be missed."
  Generated files are fingerprinted before and after, so the summary
  names the ones that actually moved.
- **The staleness check now has its caller.** `is_overdue()` and
  `overdue_lines()` are read FIRST, before anything else runs. That
  ordering is load-bearing: the runner runs the scanner, so asking
  afterwards whether the scanner is overdue would always read fresh and
  the check could never fire.
- **The (decide) dissolved rather than resolving.** It asked: dashboard
  entry, or script run before every push? Both. The script is the
  artifact; the dashboard entry launches it.
- **CORRECTION to the constraint below.** This item says the runner
  "must REPLACE the individual entries, not join them." Tony ruled
  2026-08-12 to INDENT them beneath it instead. That satisfies what the
  constraint was protecting -- the fear was a ninth PEER entry, one more
  equal choice among nine, and an indented child is not a peer, so the
  one-action default survives. His reason for keeping them: staying
  visible is how the automation's contents remain known instead of
  disappearing behind one button. Developer Tools now reads MAINTENANCE
  RUN with eleven tools indented under it, in execution order, scanner
  last so its verdict reads last. The five tools the runner does not
  cover stay unindented as peers.
- **Found by running it, first pass:** the test suite had been red since
  roughly August 3 (`test_cross_checked.py` asserting an unannotated
  corpus that stopped being unannotated in early August) and
  `test_constants_provenance.py` was failing 6 of 73. Neither was
  detectable before, because neither file was in any routine. That is
  the item's own premise confirming itself on first use.
- **Known gap, not urgent:** the runner prints a checker's full output
  only on failure, so the scanner's run-to-run delta -- the lines that
  say WHY a Tier-1 count moved -- never reaches the screen on a clean
  run. That delta is worth seeing every time.
- **Tony's idea, 2026-08-07:** "a common batch file could run a suite
  of files that should run after every update, including module
  atlas." Raised while looking at a test file that had been failing
  for five days with nobody watching.
- **The problem is not discoverability.** `palomas_orrery_dashboard.py`
  already lists eight maintenance tools under Developer Tools, each
  with a description saying when to run it. They still get skipped:
  the skill manifest advertised wrong versions for about three weeks,
  and `test_constants_provenance.py` sat false for five days. Eight
  separate judgment calls after every edit is eight chances to skip
  one.
- **Therefore the design constraint: it must REPLACE the individual
  entries, not join them.** A ninth menu item reproduces the exact
  failure. One action instead of five, not a sixth thing to remember.
- Two kinds of tool, and the split decides the shape. GENERATORS
  rewrite a file and are safe to run every time (`ledger_index.py`,
  `skills_index.py`, `module_atlas.py`, `data_inventory.py`); running
  them when nothing changed is a no-op. CHECKERS report a problem and
  inform the push call (`provenance_scanner.py`, and whatever L-155
  absorbs from the constants pins); these run last so their verdict is
  the last thing on screen. `dep_trace.py` stays OUT -- it takes a
  module name and answers a question BEFORE an edit, a different job.
- Useful precedent: `ledger_index.py` already has a `--check` mode
  that reports without rewriting and exits 1 on problems. That is the
  gate shape; the other generators would need the same mode added.
- Correction worth carrying: the scanner imports `module_atlas`'s
  FUNCTIONS directly rather than reading the generated
  `MODULE_ATLAS.md`, so it does NOT depend on the atlas being
  regenerated first. Ordering is for readability, not correctness --
  do not build a dependency that is not there.
**Gap:** **(decide)** does this ship as a dashboard entry that
replaces the eight, or as a script run before every push? Then build.
**Note (2026-08-11):** L-189 shipped its data half and left the
  staleness check for this item to call. `provenance_history.py`
  exports `is_overdue(history, now)` and `overdue_lines(history)`;
  both are unused at `dea0bc0` and waiting on a caller here. The
  declared cadence is 1 day, compared by calendar date. This makes
  L-188 the trigger and L-189 the data, which is the reason the
  check does not live inside the scanner: a scanner that is running
  cannot report that it did not run.
**Ref:** L-160 (the unrun test file that prompted it); L-184
(build-path push gate, same family); L-189.

#### [L-196] Citation continuations: mark, join, refuse
<!-- L:196 status:DONE upd:2026-08-17 section:C flag: rice:3/4/90/2 -->
- **The defect.** A `# Source:` citation too long for one line
  continued on a second, indented line. The request builder matched
  labeled lines only, so that second line was invisible: the worksheet
  quoted half a citation and asked a person to verdict it. Found by
  Fable 5 and GPT 5.6 Sol reviewing the dispatch packet blind, both
  independently saying do not send -- blocker 1 of nine.
- **The shape, per Tony's ruling 2026-08-16.** Neither reviewer's
  proposal. An explicit continuation marker naming the leg it
  continues, then a builder that joins on it, then a builder that
  refuses on any unmarked continuation. Leg-specific (`# Source+:`) so
  that a `Ref+` sitting under a `Source:` is a mismatch a tool can
  name; a generic marker would have nothing to compare against.
- **Marked in two stages**, per the ruling that all sites be covered
  rather than only the in-scope ones: a loud failure only works as a
  ratchet if nothing pre-existing trips it. Stage 1 marked 96 lines in
  the 7 corpus files (`patch_L196_1`); the chromosphere retirement
  marked 6 more; stage 2 marked 152 lines across 18 files
  (`patch_L196_13`). 135 citation-leg continuations repo-wide.
- **Scope correction.** The 2026-08-16 handoff records stage 2 as 235
  lines / 117 runs / 23 files. That figure does not reproduce. The
  detector used was validated by returning stage 1's answer set exactly
  -- 48 runs, 96 lines, the same line numbers -- and gives 154 lines /
  87 runs / 19 files. Counting tails under non-citation labels as well
  gives 217 / 111 / 27, which is not the recorded figure either. The
  likeliest reading is that 235/117/23 predates the ruling scoping the
  work to citation legs only. Repo total is therefore **135, not 165**.
- **One run deliberately unmarked.** `test_citation_inheritance.py`
  lines 122-123, inside the `MULTILINE_CITATION` fixture. That fixture
  proves the scanner captures a whole multi-line run and asserts on
  text from its first and third lines specifically to catch truncation
  at the top and in the middle. Marking it would convert the repo's
  only test of the unmarked padded shape into a test of the marked
  shape, removing that coverage. It is a fixture and will never carry
  cross-check annotations.
- **The join** (`patch_L196_8`). `legs_of()` joins a marked
  continuation onto the leg above it, reports a mismatched or orphaned
  marker rather than joining it to the wrong authority, and counts the
  lines that joined so a run that joins nothing says so. 153
  continuation lines now reach the worksheet that previously reached
  nobody.
- **The refusal** (`patch_L196_15`). An unmarked continuation is
  returned and `main()` refuses to write, listing every offending site
  and line. Scoped to the CLAIM CORPUS, not the tree: a file enters the
  corpus the moment it gains a `# Cross-checked:` line, and the refusal
  fires at the next build, still before any worksheet is made from it.
  Whole-tree scanning would buy only earlier notice, at the cost of a
  permanent exemption list headed by the fixture above.
  **Tony's ruling, 2026-08-17.**
- **A mismatched marker still reports rather than refusing.** The
  distinction is visibility: a mismatch already prints a line into the
  worksheet, where the person filling it in reads it. An unmarked
  continuation appears nowhere. Silent gets the refusal; visible gets
  the annotation.
**Note:** RICE is Claude's proposal, unratified.
**Note:** a rule that could not fail was caught here and is worth the
line. The detector has two parts -- padded lines are continuation,
unpadded labelled lines are labels. Deleting the padding rule left all
41 tests passing, because the label pattern happened to allow only one
space after the `#` and was already rejecting padded lines by itself.
The label pattern was loosened so the padding rule decides the case it
is documented as deciding, and the mutation now goes red. Found by a
mutation that was expected to break something and did not.
**Ref:** L-195 (the citation-leg errand this is half of); L-192 (the
checker and dispatch loop); `documentation/patch_L196_1..3`, `_8`,
`_13`, `_15`; `test_worksheet_request_builder.py` (new, 41 checks);
`documentation/HANDOFF_20260816_review_and_chromosphere.md` and its
addendum.

#### [L-197] Maintenance runner output: say what passed
<!-- L:197 status:DONE upd:2026-08-17 section:C flag: rice:2/3/90/1 -->
- **The defect.** Four of thirteen checker rows told the reader
  nothing. `Provenance 1d/1e ... All Phase 1d/1e tests passed` named a
  ledger sub-step twice. `Orbit cache ... Test files saved in: C:\...`
  and `Reset completeness ... Cleanup complete.` reported side effects
  as verdicts. Five more rows ended in `...` because the note was
  truncated at 44 characters. Raised by Tony, 2026-08-17.
- **Three different causes**, worth separating because the fix differed
  each time.
  1. `test_orbit_cache.py` ended in `unittest.main()`, which writes OK
     or FAILED to STDERR. The runner reads stdout, so the last stdout
     line was a `tearDown` print firing once per test. It went green
     whether or not anything passed, because a path prints either way
     (`patch_L196_11`).
  2. `test_reset_completeness.py` printed a correct verdict and then
     got buried: importing `palomas_orrery` registers a
     `PlotlyShutdownHandler` atexit cleanup whose two lines arrive
     after `sys.exit(0)`. Fixed by giving the row a hint substring, the
     mechanism already in the runner for the scanner, which is
     position-independent (`patch_L196_12`).
  3. Truncation. Verdicts now wrap onto indented continuation lines
     instead of ending in an ellipsis. Wrapping rather than widening,
     because the longest verdict runs past 160 characters and a wider
     column hands the wrap point to whatever width the console happens
     to be (`patch_L196_10`).
- **Also landed:** hover text on all 41 dashboard Launch buttons naming
  the repo and file each one runs -- `Orrery: palomas_orrery.py`,
  `Gallery: tools/gallery_studio.py`, and args included, which is the
  only thing distinguishing the two `earth_system_controller.py` cards
  (`patch_L196_9`). The `Test Provenance 1d/1e` card became `Test
  Scanner Recognition` with a description saying what passing means.
**Note:** the general defect is NOT fixed. Eleven of thirteen rows
still resolve their verdict by last line, so any of them can be
displaced the same way the moment something prints later. Giving every
row a hint is the general cure and was not attempted.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-188 (the runner); `documentation/patch_L196_9..12`.

#### [L-198] Claim vocabulary: the units the scanner could not see
<!-- L:198 status:DONE upd:2026-08-17 section:C flag: rice:3/4/85/1 -->
- **The defect.** Ten annotated sites were in the claim corpus and
  produced ZERO worksheet rows. The checker routed them; the builder
  never asked about them. Found while testing whether the pending
  dispatch already covered the SEND BACK backlog.
- **The cause, and it was not what was first guessed.** A first reading
  attributed it to ranges, from one site, without checking. Wrong. The
  scanner matches a number immediately followed by a unit from a fixed
  list. That list held `AU`, `km`, `solar radii` and `Earth radii` but
  not per-body radii (`Mars radii`, `lunar radii`), not the spelled-out
  `kilometers`, and it could not see across an intervening word, so
  `1.08 million km` failed where `1.08 km` passed. At all ten sites the
  only match was the display instruction, correctly dropped.
- **A second defect in the same pattern.** It ended `%)\b`. A word
  boundary after a percent sign requires a word character next to it,
  so `96% of the sunlight` matched nothing while `96%x` matched. Every
  percentage followed by a space or a period was invisible.
- **Measured before the change, whole tree:** 728 matches gained, 16
  lost, and every one of the 16 a false positive -- percent-encoded
  URLs (`sstr=2024%20PT5` read as the claim `2024%`) and Python `%s`
  placeholders. No real claim lost. Precision and coverage both
  improved.
- **Consequences.** Scanner Tier-1 **206 -> 289**, risen in 23 files.
  Not a regression: those 83 findings are unsourced numeric claims that
  were not being counted because the scanner could not see the number.
  The push gate reads Tier-1 on the ACTIVE BUILD PATH, not the tree
  total. Checker 59 of 102 routed / 3 clean -> 68 of 110 / 8 clean.
  Dispatch **64 rows over 42 sites -> 100 rows over 52 sites**.
- **Why now.** `EXTRACTOR_VERSION` went 1 -> 2 because the `::cN`
  ordinal counts claims AFTER this filter, so a string that gains a
  claim ahead of an existing one re-points it -- Mars's bow shock, where
  `15` was claim 1 and is now claim 2. No worksheet has ever been
  issued, none of the 35 on disk carries a key, and not one pinned key
  carries an ordinal, so re-pointing cost nothing today and would have
  cost a reissue after the first dispatch. **Tony's ruling,
  2026-08-17**, taken after the risk was measured rather than asserted.
- **Six of the ten sites now get asked about**: Mars magnetosphere
  (2 and 1.6 Mars radii), Mars Hill sphere (319.2 Mars radii, 1.08
  million km), Mercury sodium tail (1,400 Mercury radii, 3.4 million
  km), Moon Hill sphere (60,000 kilometers, 34.53 lunar radii), Venus
  Hill sphere (1 million kilometers), Eris crust (96% albedo -- reached
  by the percent fix, not the unit fix). The other four carry no number
  but the display instruction and are correctly absent.
**Note:** RICE is Claude's proposal, unratified.
**Note:** the first false-positive sweep reported zero differences
because it loaded the old scanner from the wrong path and compared the
pattern against itself -- a clean result that could not have been
anything else. Caught because zero contradicted a count taken a minute
earlier; the rerun asserts the two patterns differ before comparing.
**Ref:** L-156 (the scanner recognition work this widens); L-192 (the
dispatch corpus it grows); `documentation/patch_L196_14`;
`documentation/worksheets/L192_extractor_pins.txt` (regenerated).

#### [L-200] The `# Resolved:` leg -- record a verdict that landed
<!-- L:200 status:DONE upd:2026-08-18 section:C flag: rice:2/3/85/1 -->
- **What it is.** A record-only annotation leg naming the worksheet row
  whose verdict caused an edit, and the ledger handle that authorized
  it. Example shape:
  `# Resolved: <batch> <key> -- citation refuted, Source replaced (L-2xx)`
- **Why it is needed now.** The pilot ends at re-verification in the
  code (2026-08-17 ruling). Without this leg, an annotation edited in
  response to a verdict is indistinguishable from an unexplained edit,
  and the only record of which is which lives in a handoff.
- **It cites the KEY, never the row number.** `row_id` is positional and
  renumbers whenever the corpus changes; the key
  (`module.py::enclosing::label::cN`) is stable. Same failure the ledger
  already records for per-handoff item numbers.
- **Deliberately NOT in `CONTEXT_LEGS`.** As an unknown label it is
  invisible to the request, which is correct: a row dispatched a second
  time must not show the responder what the last one concluded. A
  context leg would anchor the way a Claude-derived figure anchors
  Gemini.
- **Measured, not assumed.** A `# Resolved:` line added to a real block
  in the patched sandbox: 100 rows, 0 unmarked, 0 problems, 153 joins --
  unchanged. It reads as a label, so it closes a leg run rather than
  tripping the L-196 ratchet. Nothing in the builder has to change.
- **The check is linkage, not meaning.** Three existence facts: the leg
  parses, it names a worksheet row that exists, and that row's citation
  verdict was one requiring an edit. Refuses on a leg pointing at a row
  that does not exist. Prints how many legs it examined, so a clean run
  says what it looked at.
- **As built, 2026-08-18** (`patch_L204_1`, shipped with L-204 because
  both touch the annotation grammar and the checker that reads it).
  The grammar lives in `provenance_scanner.parse_resolved`, beside the
  cross-check grammar rather than in a second copy; the linkage layer
  lives in `worksheet_checker.check_resolved`, where the worksheets are
  already loaded. Four ways to fail, all mutation-proven: the leg does
  not parse, the worksheet is not on disk, no row carries the key, or
  the row's citation verdict cleared and so warrants no edit. A fifth
  fires when the named worksheet has no citation-verdict column at all,
  which only a markdown return can produce -- the JSON reader
  synthesizes every column whether the return carried it or not.
- **The count prints on every run, including zero.** "0 Resolved
  leg(s) examined: 0 linked, 0 with a linkage problem." A section that
  says nothing when there is nothing cannot be told from one that never
  ran.
- **One interpretation, made by Claude and NOT yet ruled.** The design
  above wrote `<batch>` as the first token. It shipped as the worksheet
  FILENAME, because a batch name does not determine what the returned
  file is called, and "names a worksheet row that exists" is only
  mechanically checkable against a file on disk. Overrule if the batch
  was meant literally.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-192 (Break 5); L-196 (the ratchet it must not trip); L-201;
L-204 (shipped in the same patch); `documentation/patch_L204_1`.

#### [L-201] Request selection -- ask the builder for fewer rows
<!-- L:201 status:DONE upd:2026-08-18 section:C flag: rice:2/3/90/1 -->
- **The defect.** `build()` returns the whole annotated corpus and
  `main()` renders every row -- 100 rows over 52 sites at HEAD. There is
  no way to ask for fewer, so producing a pilot slice today means
  hand-editing the generated file, which breaks the request's own
  do-not-edit instruction and yields a slice no second run reproduces.
- **A selection is code, not typing.** Named entries in the module, each
  a name, a one-line purpose, and a predicate. `main()` lists them at
  the prompt; blank means the whole corpus, so today's behaviour is the
  default.
- **Ships with exactly two:** `all`, and `constants_new` (the pilot's
  23 rows). Stratified caps from the design note are NOT built --
  decision 5 removed the need for them.
- **Selection runs AFTER the L-196 refusal, never before.** Excluding a
  site must never excuse an unmarked continuation; a ratchet with a
  bypass is not a ratchet.
- **The request records its own selection:** name, count against corpus
  size ("23 of 100"), and the statement that keys identify rows.
- **Checker emits JSON findings** alongside `WORKSHEET_CHECK.md`,
  carrying routed rows by key. Precedent:
  `data/worksheet_check_state.json`.
- **A key list is legitimate only when the checker wrote it.** Never one
  a person typed. The test is whether the list can be regenerated.
- **The key-list consumer ships WITH this item** (Tony, 2026-08-17). The
  earlier case for deferring it was that building the consumer meant
  inventing the producer's format; the JSON findings emission removes
  that, since the producer exists in the same patch. What remained
  against it was an unexercised path that looks available -- weaker than
  the risk of the rule being written down and not read under pressure.
- **As built, 2026-08-17** (`patch_L201_1`, with L-202). Three named
  selections shipped rather than the two planned: `all`,
  `constants_new` (23 of 100 rows), and `sendbacks`, which reads the
  checker-written key list. Builder tests went 41 -> 61.
- **Reachable without the terminal, 2026-08-18** (`patch_L201_2`). The
  builder is a Developer Tools card on the dashboard, un-indented
  because the maintenance runner does not cover it, and marked
  interactive so it opens in its own console. Its card and its module
  docstring both name the three prompts in order and both say that the
  selection prompt DEFAULTS TO 1 -- pressing Enter there produces a
  100-row request that looks exactly like a working tool. The
  docstring's old RUNNING IT block said the tool asks one question and
  writes one file; it asks three and writes two, and had not moved with
  either this item or L-202.
- **Four runner-covered checkers were missing from the dashboard** and
  were added in the same patch, against the 2026-08-12 ruling that a
  tool the runner covers stays visible as its own card. The indented
  group now matches `maintenance_run.py` row for row AND in execution
  order, verified by reading the runner's own GENERATORS and CHECKERS
  lists rather than by eye.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-196; L-200; L-202; `documentation/patch_L201_1`,
`documentation/patch_L201_2`;
`documentation/DESIGN_20260817_worksheet_selection.md`.

#### [L-202] JSON worksheet format, with markdown as fallback
<!-- L:202 status:DONE upd:2026-08-18 section:C flag: rice:2/3/75/2 -->
- **Why.** The checker carries tolerance machinery that exists only
  because the interchange is prose: eight header spellings mapped to the
  source column alone, an emphasis stripper, and 15 unrecognised columns
  in the current run. A keyed object deletes that defect class -- a
  field name is right or it fails loudly.
- **The known risk, stated.** Failure granularity inverts. Markdown
  degrades row by row; JSON fails whole-file. Hedge: rows written one
  object per line, so a truncated return is salvageable object by
  object.
- **Tony's ruling 2026-08-17:** the purpose of the pilot is to test, so
  send the JSON; if a return fails to parse, send the markdown.
- **Markdown parsing stays live permanently.** The seventeen historical
  worksheets are markdown. This is a format ADDED, never a replacement.
- **One producer, two views.** The markdown renderer and the JSON
  emitter both run off the same `Request` list. No second source of
  truth.
- **Row integrity hash, approved 2026-08-17.** Eight hex characters over
  the joined, normalized do-not-edit fields (key, claim, code value),
  written by the builder and recomputed by the checker. The case is
  ATTRIBUTION, not tamper-proofing: without it, a responder who rounds a
  code value produces an L2b mismatch reporting the CODE as drifted,
  sending someone to investigate a constant that never moved. A missing
  hash FAILS the row -- a hash that passes when absent is a check that
  cannot fail. The run reports how many were verified.
- **Rejected alternative:** rebuilding rows from the anchor SHA to
  compare directly. More exact, but only works while the tree still
  matches the anchor, and by the time a return lands it usually does
  not.
- **As built, 2026-08-17** (`patch_L201_1` emitter, `patch_L202_1`
  reader). The request is written as JSON Lines beside the markdown,
  each row carrying an eight-character hash over its do-not-edit
  fields. The checker reads a returned `.jsonl` into the same Table the
  markdown parser produces, so every existing layer runs unchanged. A
  new layer LH routes back any row whose hash is wrong
  (`ROW_MODIFIED`) or absent (`ROW_HASH_MISSING`); a markdown table has
  no integrity map and reads NOT APPLICABLE rather than pass. Checker
  tests went 69 -> 105.
- **The defect this format left behind, found the same day.** A
  returned `.jsonl` could be checked and routed and then NOT cited: the
  annotation grammar refused a reference that did not end in `.md`.
  Leg 6 of the loop -- turning a verdict into an annotation -- had no
  last inch. Found by building a simulated JSON return and running the
  checker, not by reading the code. Closed under L-204.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-201; L-192 (L2b, the layer the hash protects from
misattribution); L-204 (the grammar this format required).

#### [L-203] The visibility convention -- give it a home in the skill
<!-- L:203 status:DONE upd:2026-08-18 section:C flag: rice:2/3/85/1 -->
- **The convention.** A failure that prints where the responder reads
  it gets an ANNOTATION; a failure that appears nowhere gets a
  REFUSAL. Visibility decides, not severity.
- **Where it came from.** L-196 left one question open as Claude's
  call: should a mismatched continuation marker refuse rather than
  report? It reports. The distinction drawn was that a mismatch prints
  into the worksheet where the responder reads it, while an unmarked
  continuation appears nowhere. Tony's ruling 2026-08-17: settle it as
  a CONVENTION rather than a one-off, because the same distinction
  governs every future case of the same shape.
- **It had a record and no home.** Recorded in
  `documentation/DECISIONS_20260817_pilot_design.md`, which nothing
  loads at the moment of need. That is the same failure shape as a
  lesson filed in an archive with no trigger.
- **As built, 2026-08-18** (`patch_L204_1`). Written into
  `skills/provenance-discipline/SKILL.md` next to the annotation
  grammar, marked CRITICAL, with the generalization stated: before
  choosing between reporting and refusing, ask where the report lands
  and who reads it -- if it lands in a log nobody opens or a file the
  next session will not load, reporting is silence wearing the costume
  of diligence. Skill 2.3 -> 2.4. No tool behaviour changed.
- **The obligation this creates.** A mid-session reinstall cannot be
  verified from inside the session that makes it, so the NEXT session
  confirms its own loaded copy reads 2.4 before doing provenance work.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-196 (where the question arose); L-186 (the annotation
grammar it sits beside); `documentation/patch_L204_1`.

#### [L-204] The worksheet reference may be JSON
<!-- L:204 status:DONE upd:2026-08-18 section:C flag: rice:2/3/95/1 -->
- **The defect.** `provenance_scanner.parse_cross_checks` required the
  parenthetical worksheet reference to end in `.md`. A line citing a
  `.jsonl` return was refused with the code `non_markdown_reference`,
  earned nothing, and was reported as a diagnostic. So a verdict could
  be built, carried, filled, returned, checked and routed -- and then
  refused when somebody wrote it back into the code. Leg 6 of the loop
  had no last inch, and the pilot could not dispatch.
- **Found by an integration test, not a reading.** A simulated JSON
  return was built, a constant annotated to cite it, and the checker
  run; it listed the worksheet as UNCITED. Reading the code would not
  have produced this.
- **The condition did two jobs, and only one of them moved.** It
  required the reference to name a FILE rather than free prose, which
  is the anti-gaming half of L-186 and stays. It also pinned the only
  worksheet format that existed in August 2026, which stopped being
  true on 2026-08-17 when L-202 landed.
- **Tony's ruling, 2026-08-18:** widen the extension set, taking
  Claude's recommendation over the two alternatives. Rendering
  accepted JSON returns into markdown for citation was rejected
  because it leaves two stores of one return, free to drift, with the
  integrity hash in only one of them; a hand-written markdown
  companion adds the same drift plus manual work per return.
- **As built** (`patch_L204_1`). One condition in one function, plus
  the three wordings that would otherwise have become false -- the
  docstring's code list, its prose, and the report's own explanation
  of what earns V2. `non_markdown_reference` became
  `unsupported_reference_format`, which is what the rule now says.
  `WORKSHEET_REFERENCE_SUFFIXES` is defined once in the scanner and a
  test pins the checker's `JSON_SUFFIXES` against it, so a fourth
  format added in one place fails loudly instead of drifting in two.
- **The skill's examples are checked now too.** `skills_index.py`
  already parsed `# Cross-checked:` examples in skill files; it parses
  `# Resolved:` examples the same way. A skill teaching a leg its own
  parser refuses is the L-186 defect in a second grammar.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-186 (the shape rule that did not move); L-202 (the format
that required this); L-200 (shipped in the same patch);
`documentation/patch_L204_1`.

#### [L-205] The runner's verdict lines carry evidence
<!-- L:205 status:DONE upd:2026-08-18 section:C flag: rice:2/3/90/1 -->
- **Two defects, both raised by Tony, both the same shape as L-197 and
  neither fixed by it.**
- **One: the summary counted report-only tools as passing.** Eleven of
  thirteen checkers are pass/fail. Two -- `worksheet_checker.py` and
  `provenance_scanner.py` -- exit 0 whatever they find, and exit 1
  only when they could not run. The summary said "All 13 checkers
  passed" above a row reporting 289 Tier-1 findings. Both statements
  true; read together they tell someone scanning for a verdict that
  there is nothing to act on. A line that reads the same whether the
  scanner found 289 or 0 cannot inform, because it cannot move.
- **Two: four verdict lines could not move either.** Constants
  relations, Cross-check annotations, Citation inheritance and Scanner
  recognition each ended in a fixed sentence. Tony's question --
  "Real citations recognized, fake ones refused: is this intent or
  result?" -- has the answer that it is a result, since it prints only
  after the failure branch has returned, but a result that reads
  identically whether 27 tests ran or two. Each file already printed
  the count two lines earlier; the runner quotes the LAST line.
- **As built, 2026-08-18** (`patch_L188_1`, `patch_L188_2`). CHECKERS
  rows gained an optional fourth field marking a tool report-only, set
  on exactly two; the summary counts the gating eleven in its headline
  and quotes the two report-only verdicts underneath, in both the
  passing and failing branches, because the scanner's count is what the
  push call turns on. The four fixed lines now carry `N of N`, keeping
  the words that say what was checked -- a bare count trades one
  blindness for another. Proven by mutation: deleting one test from
  each suite makes the lines read 18, 19, 26, 17.
- **Fixed in passing.** `test_provenance_1d.py` carried a comment
  saying the runner trims a verdict to 44 characters. Measured: 44 is
  the WRAP width and `wrapped()` deliberately gives a verdict no
  ellipsis. The wrong note argued directly against the change being
  made, so it was corrected rather than left to mislead.
- **Still not fixed, and inherited from L-197.** Eleven of thirteen
  rows resolve their verdict by last line, so any of them can be
  displaced the moment something prints later. Giving every row a hint
  substring is the general cure and was not attempted.
- **Process note.** The first cut of `patch_L188_1` compiled cleanly
  and died on the run: widening the results tuple broke a
  failure-detail loop that unpacked a fixed width. `py_compile` cannot
  see a tuple width, which is the resident gate restated in a new
  place.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-188 (the runner); L-197 (the same defect class, earlier
instance); `documentation/patch_L188_1`, `documentation/patch_L188_2`.

#### [L-207] The citation prompt -- the checker asks the fuzzy question
<!-- L:207 status:DONE upd:2026-08-18 section:C flag: rice:3/3/85/1 -->
- **The gap, measured 2026-08-18.** The citation half of a return has
  no route out of the file. `ROLE_SOURCE` -- the responder's own cited
  source -- is mapped in the header registry and read NOWHERE.
  `ROLE_CITATION_VERDICT` is read in exactly two places: an unreachable
  third branch of `read_verdict` (unreachable for JSON, which always
  synthesizes a value column) and L-200's linkage check, which only
  fires on a row a `# Resolved:` leg already names. So both halves of
  the citation question are parsed into the Table and stop there.
- **This is NOT a defect in the split.** The 2026-08-17 ruling assigned
  the citation comparison to a reader BECAUSE it is a language
  judgement rather than a numerical one, and the mechanical checker
  correctly stays at numbers. What was never built is the leg that
  carries the material to that reader.
- **Tony's design, 2026-08-18.** The checker does two things in one
  run: (1) the numerical check exactly as now, and (2) writes a
  CONSISTENT JSON prompt asking Claude the citation question.
- **Why a prompt rather than a worklist.** A worklist is data; a prompt
  is a request, and a request inherits the discipline the builder
  already has -- keyed rows, a hash over the do-not-edit fields, a SHA
  anchor, and generation rather than typing. Same SHA plus same returns
  gives the same prompt, which is what makes a citation review EVIDENCE
  rather than an opinion, re-runnable against another model and
  comparable across sessions. Same rule as L-201: a selection is code,
  not typing.
- **It respects the existing boundary.** The checker stays read-only
  over the corpus and writes reports; it already writes
  `data/worksheet_routed.json`. No writer moves behind that line.
- **Each row carries:** key, claim, code value, the code's current
  `# Source:` authority, the context legs (`# See:`, `# Derived:`,
  `# Note:`) so a misplaced authority is distinguishable from an absent
  one, the responder's cited source, the worksheet and checker it came
  from, and a row hash.
- **Ruled 2026-08-18: the prompt SHOWS the responder's citation
  verdict.** It makes the review a comparison rather than a
  re-derivation, and disagreement between the responder's verdict and
  the reviewer's is the lazy-responder canary -- measured per row,
  with no separate mechanism invented for it. The cost is stated
  rather than hidden: seeing a verdict before judging anchors, and the
  only mitigations are field order and an instruction saying the review
  is independent and that disagreement is a finding, not an error.
  Structural blindness would be stronger and was traded away
  deliberately.
- **On complexity.** This passes the extend-don't-add test: it is an
  EMITTER over the Table the checker already builds, reusing
  `row_hash` and the report writer. No new verdict semantics, no new
  layer, no second parse.
- **It is not strictly blocking for the pilot.** Twenty-three rows can
  be read by hand. It is blocking for the pilot to produce evidence of
  the kind this project trades in, and it does not scale to 110.
- **As built, 2026-08-18** (`patch_L207_1_citation_prompt`). The
  checker writes `documentation/prompts/citation_review.jsonl` on
  every run: a header carrying the anchor SHA, the key format, the
  question, the answer fields, the verdict vocabulary read from
  `VERDICT_TOKENS` rather than retyped, and the counts of what was
  left out; then one row per key. Hooked into `run()` after the
  routing file, counted in `counts`, and printed in the detail block
  whether or not it found anything.
- **One row per KEY, not per annotation** -- a decision the design
  note did not settle and the hash did. Two checkers over one site
  would otherwise produce two rows sharing a key and a hash, which is
  a hash identifying nothing. Grouped, the two sources sit side by
  side and a disagreement between responders is visible without a
  mechanism for it. Measured on the first run: 53 rows carrying 81
  responder legs, 27 of them with two responders.
- **The leg parser moved** (Tony's ruling, 2026-08-18: move it and
  get one parser). `legs_of` and its regexes went from
  `worksheet_request_builder.py` to `worksheet_keys.py`, the module
  both tools already import. The move was forced by direction: the
  checker cannot import the builder because the builder imports the
  checker. The builder keeps the old names as ALIASES, and
  `test_worksheet_request_builder.py` pins `b.legs_of is wk.legs_of`
  so a later local copy goes red rather than quietly answering the
  same question twice. Proved behaviour-neutral by building the same
  23-row pilot request before and after the move: byte-identical,
  including all 153 continuation joins.
- **What the first run measured.** 53 rows, 81 legs, 41 annotations
  that matched no row and are counted rather than dropped, 0 matched
  rows carrying no citation material. Routing unchanged at 68 of 110
  routed and 8 clean; Tier-1 unchanged at 289. The maintenance runner
  read 11 of 11 gating checkers green.
- **Determinism is the point and it is tested.** Rows sorted by key,
  responses sorted inside a row, keys sorted inside every object, no
  timestamp anywhere. Two consecutive runs produce byte-identical
  files, so `git` reporting no change IS the statement that a citation
  review is reproducible. The anchor moves only when HEAD does, which
  is why the committed artifact reads `731066f4` -- the tree it was
  built from, one commit behind the commit that landed it.
- **Three mutations prove the new checks can fail.** Dropping the
  per-key grouping, making the writer a no-op that reports success,
  and re-forking the parser into a local copy that behaves
  identically. The last is visible only to the identity pin, which is
  why the identity pin exists.
- **The skill moved with it.** `provenance-discipline` 2.4 -> 2.5 adds
  Extend a Boundary Before Adding a Path, the rule the 2026-08-18
  external review proposed and Tony adopted; L-207 was checked against
  it rather than assumed to pass. Marked QUALITY, not CRITICAL: it was
  adopted from a prediction and the tiers move on evidence. The edit
  was verified as a PURE ADDITION by stripping the new section back
  out and comparing to 2.4 byte for byte -- the check that was missing
  the day a skill rebuild deleted its own version block.
- **Carried, because it cannot be cleared here.** The 2.5 reinstall
  landed in the account during the session that made it, and a running
  conversation serves the copy it loaded. The NEXT session confirms
  its loaded `provenance-discipline` reads 2.5 before doing provenance
  work.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** L-192 (the checker); L-200 (the leg that records what a
verdict caused); L-202 (the JSON schema it reads); L-206 (the return
filenames a review will come back under); `documentation/
DESIGN_20260818_citation_prompt.md`; `documentation/patch_L207_1_
citation_prompt.py`.

#### [L-213] Orbit cache backup fires on IMPORT, not on cache write
<!-- L:213 status:DONE upd:2026-08-19 section:C flag: rice:2/3/75/2 -->
- **Found by L-212 on its second day.** The FILES WRITTEN block
  reported `data/orbit_paths_backup.json` rewritten with identical
  bytes on every maintenance run. Tony asked what was triggering it,
  since the intent is for the backup to be rewritten when the CACHE is
  updated.
- **The trigger, traced.** `create_orbit_backup()` is called at MODULE
  LEVEL in `palomas_orrery.py:3649` -- not inside a function, not
  behind an `if __name__` guard. `test_reset_completeness.py:39` does
  `importlib.import_module('palomas_orrery')`, and that test is in the
  maintenance suite. So importing the orrery runs the backup, and the
  suite imports the orrery every run. The cache is never touched; only
  the module is loaded.
- **Why this is more than a pointless rewrite.** The backup is
  `shutil.copy` of `data/orbit_paths.json` over
  `data/orbit_paths_backup.json`, unconditional. If the cache is ever
  corrupted and ANYTHING imports the orrery afterwards -- a GUI
  launch, a test run, a maintenance run -- the good backup is
  overwritten with the corrupted file. The window between corruption
  and loss is one import, and the maintenance suite makes an import
  routine.
- **Nothing has gone wrong yet**, and that is the shape of the risk
  rather than a reason to discount it: the defect costs nothing until
  the cache goes bad once.
- **Two repairs, different sizes.** The SMALL one: make the copy
  conditional on the source differing from the existing backup, which
  stops the rewrite and nothing else. The REAL one: back up when the
  cache is WRITTEN, which means moving the call out of module import
  and next to whatever saves `orbit_paths.json` (see
  `orbit_data_manager.py`, `ORBIT_PATHS_FILE` and the
  `save_orbit_paths` path), and keeping a copy that a later import
  cannot clobber.
- **Design pass first** (Tony, 2026-08-19). This touches
  `palomas_orrery.py`, which is Mode 1 territory -- targeted snippets,
  never a full-file rewrite -- and moving a module-level call changes
  startup behaviour for the GUI as well as the tests. Iterate the
  design in conversation before any code.
- **Confirm the dispatch before editing the leaf.** The same rule that
  opens L-209. `create_orbit_backup()` lives in
  `palomas_orrery_helpers.py:791` and is called from exactly one
  place; check that is still true at the time of the fix rather than
  trusting this note.
- **As built** (`patch_L213_2_remove_startup_backup.py`, run 2026-08-19;
  pushed at `81108b2f`). `create_orbit_backup()` deleted from
  `palomas_orrery_helpers.py`, its module-level call and import removed
  from `palomas_orrery.py`, and the startup summary extended to name the
  restore points. `data/orbit_paths_backup.json` deleted by hand.
- **The risk statement above was WRONG, and the correction is the point
  of this entry.** It said a corrupted cache would overwrite the good
  backup on the next import. That file was never a recovery source.
  `load_orbit_paths()` reads `data/orbit_paths.json.backup` and
  `.backup_old` and nothing else; a repo-wide grep found the only
  mentions of `orbit_paths_backup.json` were the two lines that wrote
  it. So the defect was a pointless write of a file no code read, not a
  live threat to recovery.
- **The repair L-213 called "the real one" already existed.**
  `save_orbit_paths()` writes through a temp file, re-reads it to confirm
  the JSON parses, rotates `.backup` into `.backup_old`, copies the
  current cache to `.backup`, and refuses any save that shrinks the cache
  by more than 5 percent. Moving the import-time copy next to the write
  would have added a third copy of a job already done twice. Tony's
  ruling, 2026-08-19: two files, not three, and delete the odd one.
- **Mode 5 confirmed** on the launch log of 2026-08-19: 1,501 orbits
  loaded, both restore points printed, no `[STARTUP]` backup line, no
  file written.
- **The fix's own output then exposed a second defect, in the block this
  item added.** The two restore points read 130.4 MB dated August 5 and
  August 4, which looks two weeks stale and is not. `shutil.copy2`
  preserves mtime, so a backup's date is when its CONTENT was written,
  not when the copy was taken -- `.backup` carries the previous save,
  `.backup_old` the one before that, and the most recent save's date
  lives only on the live cache, which the block did not print. Two
  readings fitted the same screen: no cache write in two weeks
  (expected during provenance work) or writes happening without
  rotation (a defect). Fixed by `patch_L213_3_cache_line_and_close.py`,
  which prints the live cache alongside its two restore points and
  relabels the timestamp. Success now carries evidence: three dates read
  as a sequence and a stalled rotation announces itself.
- **The module-level answer to the Gap question.** `palomas_orrery.py`
  has no `if __name__ == "__main__"` guard anywhere -- the whole file
  runs on import, including the working-directory change and
  `root.mainloop()`. `test_reset_completeness.py` survives that only by
  replacing `tk.Misc.mainloop` with a no-op before importing.
  `create_orbit_backup()` was the ONLY module-level statement that wrote
  into `data/`. The missing guard is a separate problem and is NOT
  closed by this item.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** the missing `__main__` guard, deliberately left open (see the
last bullet). Not opened as its own item pending Tony's call on whether
it is worth the startup-behaviour change to the GUI and the tests.
**Ref:** L-212 (the block that surfaced it); `orbit_data_manager.py`
`save_orbit_paths` / `load_orbit_paths` (the real backup chain);
`documentation/patch_L213_2_remove_startup_backup.py`;
`documentation/patch_L213_3_cache_line_and_close.py`.

#### [L-028] ASCII em-dash violation, comet_visualization_shells.py L257/505/519
<!-- L:028 status:DONE upd:2026-08-19 section:C flag: rice:1/1/100/1 -->
- **Closed 2026-08-19: ALREADY DONE, and nobody had closed it.**
  `comet_visualization_shells.py` holds zero non-ASCII bytes at
  `434a712b`, verified by byte scan, and the named lines L257/L505 are
  unrelated code. The work was finished at some point and the entry sat
  69 days in the tail counted as debt. Found by the first by-topic sweep
  (L-215), not by anyone reading the list.
Pre-existing; 3 em-dash lines in MAPS strings `[verified @0ce1e26]`.
**Gap:** fix on next touch (binary-mode).

#### [L-220] A patch updates the body but not the anchor, date or description
<!-- L:220 status:DONE upd:2026-08-20 section:C flag: rice:3/3/85/1 -->
- **Tony's observation, 2026-08-20, and it is about the project rather
  than about any one file.** "We do not update these documents with
  every session, nor do we always update the module description,
  history, dates, etc. -- we tend to update the body more than the
  anchors." Confirmed across the three master plans:
  `MASTER_PLAN_CRITICAL_PATH_SUMMARY.md` carries both SHAs and a
  live-check note, `MASTER_PLAN_INTERACTIVE_GALLERY.md` carries no
  anchor at 2010 lines, and `MASTER_PLAN_WEB_PUBLICATION.md` carries an
  anchor six weeks stale. The ledger is the most current document
  because its index is machine-maintained, not because anyone is more
  disciplined about it.
- **Why a session-start anchor check was proposed and then dropped.**
  Claude proposed comparing every Context document's anchor against
  live HEAD. Tony's correction makes that unworkable: if anchors are
  updated only sometimes, a mismatch means EITHER the document is stale
  OR nobody re-stamped it, and nothing distinguishes them. Two
  conditions, one signal -- a check that fires constantly and means
  nothing, which is worse than no check.
- **Why a generated currency stamp was also rejected.** It needs its own
  generator to maintain. A stamp written by the patch that caused the
  staleness cannot drift, because there is no second step to forget.
  Tony's framing is the better one and it is the protocol's own "put the
  check where it runs," one layer over.
- **CLOSED 2026-08-20 in `safe-file-editing` 1.5, Stamp What You
  Change.** The patch updates the file's currency block -- version line,
  anchor, history, date, and the module description where behaviour
  changed -- in the same transaction as the body, names the model, and
  prints which stamps it updated. The module description is called out
  as the highest-stakes half because `module_atlas.py` regenerates
  MODULE_ATLAS.md and MODULE_INDEX.md from module docstrings, so a stale
  description propagates into a generated document that presents itself
  as current.
- **A limit Claude proposed and Tony declined.** Claude wanted "stamp
  only what the patch actually touches," on the grounds that stamping an
  untouched file is a false provenance claim. Tony: "I don't see when
  this would happen. Your patches are not incidental, always for a
  purpose." Recorded because the reasoning generalises -- the rule was
  written for an imagined failure, not an observed one, which is what
  Extend a Boundary Before Adding a Path exists to refuse. If it ever
  happens it earns a field note then.
- **AMENDED 2026-08-20 in `safe-file-editing` 1.6, same day, on Tony's
  question: "shouldn't the anchoring etc apply to md files too, not just
  py files?"** It should, and 1.5 would not have made a reader think so.
  Its opening sentence was file-agnostic but its only concrete example
  was a Python module docstring, and the skill's own description says
  "especially .py" -- so the rule covered Markdown in principle and
  would not have fired on it in practice, which is the prose form of a
  check that cannot fail. 1.6 names the currency block for each file
  type in a table and says outright that Markdown is where the rule was
  earned.
- **The error that proved it, and it was in the patch that introduced
  the rule.** `patch_L220_1` printed "LEDGER_CONSOLIDATED.md -- no
  currency block of its own." False. The ledger header carries `Module
  updated: June 2026 with Anthropic's Claude Sonnet 4.6, Opus 4.8 +
  Claude Fable 5`, a Consolidated date, and Tony's own RICE review line.
  Claude asserted an absence without looking -- the same shape as the
  truncated-grep false absence in the 2026-08-19 handoff, error 2. The
  ledger's stamp still reads June while the file was edited four times
  on 2026-08-20; whether a nightly-regenerated file should carry a
  hand-maintained stamp at all is left for whoever next touches that
  header.
- **Tony's reason for doing it immediately rather than folding it into
  the next bump.** "The documentation is what keeps our conversation
  targeted, clear and trackable." Recorded in the skill section itself,
  because a rule whose cost is visible and whose reason is not gets
  quietly dropped.
**Note:** RICE is Claude's proposal, unratified.
**Ref:** `skills/safe-file-editing/SKILL.md` "Stamp What You Change" and
"Fix In Passing, Report It"; `module_atlas.py` header (L-163 Phase 3);
`skills/orrery-coding-conventions/SKILL.md` credit lines (the
attribution convention this generalises); L-219 (the other open
safe-file-editing gap, now targeting 1.6).

#### [L-223] A paste into the ledger is an unverified transfer
<!-- L:223 status:DONE upd:2026-08-21 section:C flag: -->
- **Observed 2026-08-21, editing LEDGER_CONSOLIDATED.md in VS Code.**
  Tony selected a block and pasted over it. Nothing appeared. He
  repeated the paste several times, still with no visible effect, and
  raised it. He then cut, pasted again, and WAITED -- and the text
  arrived roughly a minute later, complete and correct. He also
  noticed that the spinner ended when he refocused the cursor.
- **What was actually observed, kept separate from what it might
  mean.** Four things: a paste that showed no effect for about a
  minute; a completed, correct paste at the end of that; no
  duplicates from the repeated attempts; and a spinner that resolved
  on refocus. Tony checked for the duplicates specifically, because
  Claude had raised multiple pending pastes as a risk. They were not
  there. Recorded as a checked negative rather than left standing as
  speculation.
- **The mechanism was never verified and this entry does not claim
  one.** Claude's account -- that modern VS Code negotiates several
  clipboard formats with the source application before inserting, and
  that serving a rich flavour from a browser can block -- fits the
  refocus detail and the browser-to-editor path, and is offered as
  plausibility only. Nobody instrumented the editor. A future session
  reading this should treat it as an unexplained observation with a
  candidate attached, not as a diagnosis. If it recurs, one setting
  worth trying is `editor.pasteAs.enabled` set to false, which turns
  off the alternative-paste offers and keeps plain paste.
- **THE FINDING IS NOT THE DELAY. It is that nothing reports the
  outcome.** A paste that dropped and a paste that landed produce the
  same evidence, which is none: no participant in the chain -- source
  application, OS clipboard, editor paste handling, buffer, save --
  owns saying whether the transfer completed. Tony caught this one
  only because he happened to be comparing the paste against the
  copy. That is this project's own confirming question, "what tells
  us it is working," asked of a text editor. Same shape as A Check
  That Cannot Fail Is Not Passing, one layer out from the code.
- **The retry instinct is the hazard the delay creates.** Repeating a
  paste that seems not to have happened is the natural response, and
  it is how one pending transfer becomes two. It did not happen here.
  It is written down because the next person to meet this cold will
  reach for the same response.
- **PROMOTED to `safe-file-editing` 1.7, same day** (Tony's ruling).
  The durable rule is that an edit to a version-controlled file is
  delivered as a patch script INCLUDING prose, markdown and ledger
  files -- because a hand-paste is an unverified transfer, not
  because any editor is buggy. The skill had never said patch
  discipline was for `.py` files only, but every example in it was
  code, and this project had been hand-editing a 579 KB markdown
  ledger on that silence. The rule as written outlives whatever this
  particular stall turns out to be.
- **The human fallback, in Tony's own terms, for when a hand edit is
  unavoidable:** watch until the text actually appears before
  clicking or typing anything else, and do not retry on silence. It
  is what caught this. It is also a person looking, standing in for a
  check the tooling does not perform, which is why it is the fallback
  and the patch is the default.
**Note:** RICE not scored. The item was closed on arrival -- the
observation is recorded and its rule promoted in the same session, so
there is no work to prioritise.
**Ref:** `skills/safe-file-editing/SKILL.md` (A Paste Is An Unverified
Transfer, v1.7); `documentation/patch_L223_1_safe_file_editing_paste_
rule.py`; `documentation/patch_L223_2_ledger_paste_instance.py`;
L-214 (the block being pasted when this surfaced); the resident A
Check That Cannot Fail Is Not Passing gate.

#### [L-222] The constants change report fails on every currency stamp
<!-- L:222 status:DONE upd:2026-08-20 section:C flag: rice:3/2/95/0.5 -->
- **Found 2026-08-20, immediately after L-220 landed.**
  `constants_change_report.py` parses three line shapes: `NAME =
  <number>`, `'Key': <number>`, and anything opening with `#`. A
  module DOCSTRING line is none of them, so a changed docstring line
  carrying a digit went to the UNPARSED bucket and exited 1.
- **Which made it a permanent failure, not an occasional one.** Stamp
  What You Change requires the docstring to move in the same
  transaction as any edit to the file, and every `Module updated:
  <date>` stamp carries digits. So the checker was going to fail on
  every future patch to `constants_new.py`, on a line that is not a
  value edit and never could be.
- **Two rules collided and neither was wrong.** L-220 is right that
  the stamp must move with the body. The report is right that a
  changed line it cannot read must not report clean. The defect was
  that the report had no third category for a line that is neither a
  value nor evidence about one.
- **A checker that ALWAYS fails is the mirror of one that CANNOT
  fail.** Both are unread within a week, and neither announces the
  thing it was built to announce. That is why this was fixed the same
  day rather than filed: the cost is not the red line, it is the
  habit of scrolling past it.
- **Fixed by DERIVING the docstring line set, not by matching a stamp
  pattern.** The tool reads the module docstring at the base revision
  (`git show <base>:constants_new.py`) and in the working copy, via
  `ast.get_docstring` -- the same call `module_atlas.py` uses -- and
  treats a changed line as a docstring line if it appears in either.
  A stamp pattern would have drifted the first time a stamp was
  worded differently. This cannot, because it reads the thing it
  describes. Both revisions are needed because a stamp edit changes a
  line on both sides of the diff.
- **Three properties that keep the fix honest.** Value parsing runs
  FIRST, so the docstring test can only reclassify a line already
  bound for the unparsed bucket and can never swallow a value edit. A
  docstring edit does NOT set `comment_moved`, because the module
  stamp documents no particular constant and crediting one with it
  would be a false clear. And the docstring lines are COUNTED AND
  PRINTED rather than dropped, with a note saying which revisions
  were actually read -- a fallback to the working copy alone says so.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** none. Built and verified the same day at `762aa5dd`:
the stamp is accepted, and a mutation putting a real value edit in an
unreadable shape still fails the run.
**Ref:** `constants_change_report.py` `docstring_lines` /
`read_changes`; L-220 (Stamp What You Change, the rule it collided
with); L-210 (the patch whose stamp exposed it); the resident A Check
That Cannot Fail Is Not Passing gate, of which this is the mirror
case.

#### [L-214] The request builder drops the comment lines that matter
<!-- L:214 status:DONE upd:2026-08-21 section:C flag: rice:3/3/85/2 -->
- **Found by L-209, 2026-08-19.** The dispatched row for
  `ALFVEN_SURFACE_RADII` carried two context lines. The three comment
  lines that stated the answer -- a `# Note:` and two under an invented
  `# HELIOCENTRIC:` label -- were dropped silently, and the worksheet
  that resulted looked complete.
- **The mechanism.** `worksheet_keys.py` defines `VERDICTED_LEG =
  'Source'` and `CONTEXT_LEGS = ('Ref', 'Also', 'See', 'Derived',
  'Calculation')`. Anything else closes the run. An unrecognised LABEL
  is not an unmarked continuation either, so the builder's refusal path
  never fires: the text is not joined, not reported, and not refused.
- **This is the Visibility Convention's own case.** A failure that
  reaches no reader should REFUSE, not proceed. The builder refuses on
  unmarked continuation text for exactly this reason and then walks past
  a whole dropped label.
- **It bears on the pilot result.** The traps did not spring, but at
  least one row was checked against a redacted version of itself and
  nothing in the returns could have said so. Three models spent a
  dispatch rediscovering what the row already said, and the leg with the
  least to work with confirmed the wrong value.
- **Not yet decided:** whether the fix is to widen the recognised label
  set, to refuse on any unrecognised label under a claim, or to report
  dropped labels into the worksheet where a responder can name them. The
  Visibility Convention argues for refusing, and the count of affected
  rows across the corpus is unmeasured.
**Note:** RICE is Claude's proposal, unratified.
- **COUNTED 2026-08-19 at `d25b5368`, using the project's own
  `collect_claims` and `LEG_RE`.** 12 of 55 claim sites carry a label
  the builder cannot read; 9 of the 12 are in `constants_new.py`, the
  others one each in the Mercury, Venus and Moon shell modules.
- **Two kinds of dropped label, and only one is a defect.** The RECORD
  legs -- `Cross-checked` (216 lines), `Removed` (18), `Corrected` (16)
  -- are deliberately invisible to the request, so a second reader
  cannot see what the last one concluded. That is correct behaviour.
  What remains after excluding them is almost one label: `Note` at 17
  lines, plus `HELIOCENTRIC` at 2 and `NOTE` at 2.
- **The finding that reframes the pilot: THREE of the five rows still
  on the reconciliation queue are on this list, and in each case the
  redacted Note is what the responders spent the dispatch
  rediscovering.**
  - `STREAMER_BELT_RADII` -- "Visualization cutoff at upper end of 4-6
    R_sun observed range." The row where the citation was found
    inverted. No leg was told the value was a drawing choice.
  - `EARTH_EQUATORIAL_RADIUS_KM` -- "B3 rounds to 6378.1 km; full
    precision from IERS Conventions." All three legs flagged exactly
    this by three different routes. The file already said it.
  - `INNER_CORONA_RADII` -- "Visualization boundary for inner
    (K-)corona; physical extent 2-3 R_sun." The row where all three
    legs split on whether a visualization boundary is verdictable at
    all, which is an open ruling. The file answers it in a line none of
    them could see.
- **Two more worth naming.** `HELIOPAUSE_RADII`, the canary row, hides
  its conversion arithmetic in a Note -- two legs reproduced that
  arithmetic to the digit rather than reading it. And `HELIOCENTRIC`
  appears TWICE, on `ALFVEN_SURFACE_RADII` and `PARKER_CLOSEST_RADII`:
  the same invented label, both times on the origin question that
  produced L-209.
- **What the count changes.** Adding `Note` to `CONTEXT_LEGS` is one
  label and would have altered what three of the pilot's hardest rows
  were checked against. The Visibility Convention still argues for
  REFUSING on an unrecognised label rather than walking past it
  silently, since a label nobody reads has no correction path. Widen,
  refuse, or report-into-the-worksheet remains undecided -- but it is
  now a design conversation with a measurement under it.
**Note:** RICE is Claude's proposal, unratified.
- **DESIGN SETTLED 2026-08-19, after a Mode 7 review by Claude Fable 5
  and GPT.** Both legs reviewed the same two documents and both
  disagreed with Claude's six-part proposal in the same place. Tony's
  rulings this session are recorded below; the reconciliation of the
  two returns is `documentation/L214_REVIEW_RECONCILIATION_20260819.md`
  and the measurement under it is
  `documentation/L214_MEASUREMENT_20260819.md`.
- **The root cause is one layer below where the proposal was working.**
  `LEG_RE` is BUILT FROM the policy sets, so "the label is not in our
  vocabulary" and "this is not a labelled line" are the same condition.
  That is why deliberate withholding and silent dropping share one code
  path and are indistinguishable from inside it. The fix is to detect
  any `# Label:` line generically FIRST, then classify it. The invariant
  both legs propose: every syntactically labelled line attached to a
  claim finishes the builder in ONE NAMED DISPOSITION. There is no
  disposition called "fell through the regex."
- **Transport and grammar are two axes, not one list** (GPT's framing;
  Fable reaches the same two-by-two and calls the empty cell a fourth
  state). TRANSPORT says travels or withheld. GRAMMAR says validated or
  free-form. `Source` travels and is verdicted. `Note` travels as
  context. `Resolved` is withheld with a strict linkage grammar. The
  cell nothing occupied is withheld-and-free-form, which is where the
  moon line has been trying to live.
- **Tony's ruling: the free-form record label is `# Review-note:`.**
- **Tony's ruling: unclassified text is WITHHELD from the request and
  surfaced to Tony and Claude before dispatch.** This corrects Claude's
  reading of the earlier report-not-refuse ruling, which had routed
  unclassified text to the outside responder. Tony, asked directly who
  "we" was in "report so we can deal with it by reading": "I meant you
  and me reading fuzzy responses." Fable's asymmetry argument is the
  reason it matters -- withhold-by-default fails visibly and
  recoverably, ship-by-default fails invisibly and unrecoverably,
  because a contaminated leg does not error, it CONVERGES, and
  convergence is this system's success signal.
- **Tony's ruling: the registry work stays in L-214** rather than
  splitting into its own item, even though the review grew this from a
  label-set fix into a change of how a labelled line is recognised.
- **One home for the vocabulary, and it does not exist yet.** Checked
  at `97c52017`: `CROSS_CHECK_LINE_RE` and `RESOLVED_LINE_RE` are
  compiled in `provenance_scanner.py`, case-INsensitive.
  `worksheet_keys.py` names neither, and its `LEG_RE` is
  case-SENSITIVE. `Removed` and `Corrected` have NO pattern anywhere --
  they are prose conventions that happen to fall through. So the record
  set is two enforced labels plus two conventions, not four peers, and
  Claude's proposed `RECORD_LEGS = (four labels)` was inventing two of
  them. Fable's sharp version of the risk: the hazard is not naming the
  set twice in prose, it is COMPILING it twice from two literals.
- **The marker sweep is 12 lines at 8 sites, not 10 at 6.** Fable
  predicted the undercount; re-run with the project's own tooling at
  `97c52017` confirms it exactly. Relabelling the odd spellings to
  `# Note:` brings their own continuation lines into the unmarked set
  -- one under `PARKER_CLOSEST_RADII`, one under
  `venus_atmosphere_info`. [verified @97c52017]
- **The build carries an ORDER CONSTRAINT, not just a list** (Fable).
  The moon line must leave `Note` BEFORE or in the same transaction as
  the marker sweep. Sequenced the other way there is a window in which
  it carries valid `Note+:` markers and travels cleanly on the next
  moon-row dispatch; the ratchet protects only until the sweep
  completes, and after that nothing refuses.
- **The moon line has no other home** [verified @97c52017]. Fable
  raised the cheaper instance-level answer -- if the ledger already
  carried "second independent leg owed" for that row, the comment would
  be a redundant mirror to delete. It does not. No ledger item carries
  it. The comment is the sole record, so it is rehomed under
  `# Review-note:` rather than deleted.
- **The project-side report lands on the console at dispatch**, beside
  the existing refusal print, rather than in a new file. That is the
  surface already in Tony's routine when he presses Run; a report in a
  store nobody opens is a check that cannot fail.
- **WHY REPORT RATHER THAN REJECT -- Tony's rationale, 2026-08-19,
  recorded because it is the argument and not just the ruling.** A
  reported label is one this project can then READ and decide about:
  alias it, or unify it under a single label the way `Note` was
  unified. A rejected label forecloses that -- the run stops and the
  decision never gets made. The reading step is where the judgment
  lives, and reporting is what delivers material to it.
- **The `Corrected` drift is the worked example** [verified
  @2f0aabe]. Corpus-wide the label appears in FOUR spellings with no
  validator behind any of them: `# Corrected:` (7), `# Corrected
  2026-08-02:` (5), `# Corrected 2026-08-05:` (1), `# Corrected in
  Phase B:` (1). Three of the four would classify as unknown under the
  new design, while a human reading them sees an obvious record leg.
  That is exactly the case reporting is for: the reader sees all four,
  and then decides between aliasing the dated forms and unifying them
  on one label. Rejecting would have stopped the run and produced no
  decision. Note also that this drift happened in the two record
  labels that have no compiled pattern -- the two nothing was
  watching.
- **CORRECTION, 2026-08-20: nobody is compiling the vocabulary
  twice** [verified @3586970d]. The build-step wording above said
  the scanner and the checker should import "rather than compiling
  their own." That overstated the problem. `worksheet_checker.py`
  already imports both record patterns from `provenance_scanner`
  (`ps.CROSS_CHECK_LINE_RE` at line 1190, `ps.RESOLVED_LINE_RE` at
  line 1623) and compiles no copies of its own. The state is not
  one duplicated set. It is TWO single homes that DISAGREE: the
  scanner's patterns are compiled `(?mi)`, case-INsensitive, while
  `LEG_RE` in `worksheet_keys.py` carries no flags and is
  case-SENSITIVE. The wording is corrected above.
- **That disagreement is NOT a new decision, and reopening it as
  one would have undone a measured build step.** Step 6 already
  fixes the four odd labels at source, and the 12-lines-at-8-sites
  count depends on that relabelling. Relaxing the shared matcher to
  ignore case would make `# NOTE:` work without being edited,
  remove part of step 6's reason to exist, and invalidate the
  count Fable had already caught this project undercounting once.
  The ruling stands as made: edit at source, do not alias, do not
  relax the matcher. The scanner keeps its existing
  case-insensitive behaviour by default, and after step 6 nothing
  case-odd remains on the builder's side to disagree about.
- **SCOPING: move the label SET, not the body grammar** [verified
  @3586970d]. "One home for the vocabulary" can be read as "move
  the regexes," which would drag semantics into a keys module. The
  scanner's constants are label names PLUS a body contract:
  `RESOLVED_LINE_RE` has a companion `RESOLVED_BODY_RE` enforcing
  `<worksheet> <key> -- <what> (L-nnn)` with ISO-only dates. What
  moves to `worksheet_keys.py` is the label set and its TRANSPORT
  policy -- which labels exist, and for each, whether it travels to
  a responder or is withheld. What stays in `provenance_scanner.py`
  is the body GRAMMAR and its validation, with the scanner's line
  patterns derived from the shared label names rather than from its
  own literals. That is the same transport/grammar split the Mode 7
  review settled on, applied one layer down.
- **`worksheet_keys.py` carries no `Role:` tag** [verified
  @3586970d]. `Domain: dev_tools` is present and `Role:` is absent,
  so `module_atlas.py` files it under "Undetermined role (6)" on
  the atlas's own front page -- together with
  `worksheet_key_aliases.py`, `test_worksheet_keys.py` and
  `test_extractor_pins.py`, the whole worksheet-keys cluster
  untagged as a group. The build opens that docstring anyway for
  the SECOND JOB section, so the tag goes in the same patch under
  Fix In Passing, Report It. `TAG_RE` requires `Role:` alone on a
  line with a SINGLE-token value drawn from `VALID_ROLES`, read via
  `ast.get_docstring` -- a two-word value or a comment-block header
  reads as absent rather than as an error.
- **BUILT 2026-08-21, in two patches, both landed and verified against
  the pushed bytes.** `patch_L214_1_vocabulary_registry.py` at
  `dbe50bc9` (nine files, one transaction) and
  `patch_L214_2_scanner_derives.py` at `c214da50` (one file,
  behavior-preserving). Both archived to `documentation/`.
- **What patch 1 changed.** `worksheet_keys.py` gained the label
  registry: `RECORD_LEGS`, `LABEL_TRANSPORT`, and `ANY_LABEL_RE` as a
  generic `# Label:` detector that runs AHEAD of classification.
  `Note` joined `CONTEXT_LEGS`; `Review-note` entered `RECORD_LEGS` as
  the withheld free-form label. `legs_of` now returns a named
  `Legs(cited, context, problems, unmarked, joined, unknown)`, and its
  sixth field is the disposition this item existed to create. Its two
  consumers and its 15 test unpacks moved with it in the same
  transaction. The `Role: devtool` tag went in under Fix In Passing.
- **PADDING IS CHECKED BEFORE THE LABEL PATTERN, and that ordering is
  now load-bearing.** With a generic detector, `#   Highly
  ellipsoidal: 1050x840x537 km` would read as a label called `Highly
  ellipsoidal`. Before L-214 the vocabulary itself prevented that by
  accident. The `PADDED_RE` test is what prevents it now, and the
  reason is written into the code beside it.
- **THE MARKING OBLIGATION WAS 17 LINES AT 9 SITES, NOT 28 AT 10**
  [verified @`e1c64dc9`]. The 2026-08-21 handoff's 28 counted wrapped
  lines under WITHHELD labels. The settled design says a withheld
  label's continuations are withheld with it and are never flagged
  unmarked -- nothing is being dropped from a request the text was
  never entering. Excluding them, and accounting for the moon line
  leaving `Note` for `Review-note` while the two relabelled odd
  spellings joined it, gives 17 at 9. Re-measured with the project's
  own `collect_claims` and `PADDED_RE`; the live builder run after the
  patch joined exactly 17 more continuation lines, at exactly those
  nine sites, with no other site moving.
- **Tony's ruling on packaging, 2026-08-21: two patch scripts.** One
  all-or-nothing transaction for the vocabulary and the corpus
  together, because a signature change with four consumers has no
  valid intermediate state and the admit/mark ordering fails in both
  directions if split. The scanner derivation follows separately
  because it is behavior-preserving.
- **Tony's ruling on the form of `Removed` and `Corrected`,
  2026-08-21: option B.** Register both as withheld free-form record
  labels AND unify the dated spellings at source in the same corpus
  patch, so the date moves into the body (`# Corrected: 2026-08-02 --
  ...`). The argument that decided it: the new report's value is that
  a non-empty run means something, and shipping it on day one already
  listing seven known lines would teach its reader that its contents
  are usually noise. `Removed` had one spelling and no drift;
  `Corrected` had four, and a fifth (`# Corrected 2026-08-20:`)
  appeared the day AFTER the design was settled, which is what made
  the set worth closing rather than watching.
  Eight dated lines were unified across `constants_new.py` and
  `mars_visualization_shells.py` -- all of them in files the patch
  already opened, one more than the seven attached to scored values,
  under Fix In Passing.
- **`# Corrected in Phase B:` in `shell_configs.py` was left alone**
  [verified @`e1c64dc9`]. It is not attached to a scored value, so the
  builder never sees it, and the file was outside the patch. If that
  site is ever scored, the new report names it. The Artifact Bounds
  the Audit.
- **The verification that mattered.** Live builder run against the
  pushed bytes at `dbe50bc9`: 98 rows, 176 continuation lines joined,
  `0 unrecognised label(s) at 0 site(s)`. The ratchet did not refuse,
  which is what proves all 17 markers landed on the right lines. The
  `Note` under `SOLAR_RADIUS_KM` travels as context where it was
  silently dropped before; the moon's rehomed single-leg comment
  travels nowhere and does not trip the ratchet either. For patch 2,
  old literal patterns and new derived patterns were compared over
  every `.py` file in the tree: 127 cross-check matches, 5 resolved
  matches, zero disagreements. Tier-1 stayed at 292 across both
  patches -- checked against a pre-patch clone, not assumed.
- **The import guard in patch 2 was tested by making it fail.**
  Deriving a pattern from a shared name is decorative unless a rename
  that never reaches the scanner can actually break the import. The
  membership check against `RECORD_LEGS` was probed with a misspelled
  name in a throwaway copy; it raised and named both sides. A Check
  That Cannot Fail Is Not Passing, applied to the patch's own guard.
- **A defect found by the pre-test, not by a check** -- recorded
  because it is the third instance of this shape in this project. The
  first build of patch 1 rewrote the test file's unpack lines by
  matching a list of six literal spellings, counted nine matches,
  compared that against its own expected nine, and passed -- while
  leaving six of the fifteen sites unconverted. The count check was
  built from the same list as the rewrite, so it could not have
  failed. The xvfb-less runtime test caught it when the suite crashed
  on the seventh site. The shipped version matches by pattern and
  asserts the full population of 15, with the reason written in beside
  it.
**Note:** the `Legs` namedtuple is the shape that keeps this from
recurring. A seventh field can be added without breaking any consumer
that reads by attribute; the 15 test unpacks that had to move this
time were positional.
**Note:** re-dispatching the affected rows is a SEPARATE decision and
is not closed by this build. A second dispatch of a row this project
has already argued about in writing is not an independent leg.
**Ref:** `worksheet_keys.py` (`LABEL_TRANSPORT`, `ANY_LABEL_RE`,
`legs_of`, `continues_a_leg`); `worksheet_request_builder.py` (the
report in `main()`); `provenance_scanner.py` (`_record_line_re`,
`CROSS_CHECK_LINE_RE`, `RESOLVED_LINE_RE`);
`documentation/patch_L214_1_vocabulary_registry.py`;
`documentation/patch_L214_2_scanner_derives.py`;
`documentation/L214_MEASUREMENT_20260819.md`;
`documentation/L214_REVIEW_RECONCILIATION_20260819.md`;
`documentation/REVIEW_PROMPT_L214_20260819.md`;
L-209 (the row that exposed it); L-203 (the Visibility Convention);
L-195 (the ratchet this preserves); L-204; L-207; L-210 (three of
whose rows this count implicates); L-217 (the dispatch defect this
review surfaced); L-219 (patch naming -- both scripts follow the
convention and self-archived).

#### [L-221] The master plan is the roadmap, and it outranks RICE
<!-- L:221 status:DONE upd:2026-08-22 section:C flag: rice:3/2/90/0.5 -->
- **Tony's ruling, 2026-08-20.** The document stack in
  `ledger-and-session-records` is an AUTHORITY ordering -- who wins
  when two documents disagree about status. The master plan is not
  in it and does not belong in it, because it is not competing on
  that axis. It has a different authority: SEQUENCING.
- **What the master plan is for.** It is the roadmap -- where we
  are and where we are going, not what is directly in front. It is
  traced at three levels of zoom: the full plan
  (`MASTER_PLAN_INTERACTIVE_GALLERY.md`), its summary, and the
  critical path (`MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`).
- **It updates at key junctures, not at every change.** Stepwise
  updating is the ledger's job. That cadence is a property of what
  the plan is for, not a defect to be corrected by restamping it
  more often -- a juncture is its unit.
- **It outranks RICE on sequencing.** RICE ranks items in
  isolation. Bundling several items to complete a planned step
  SUPERSEDES RICE order. The ledger header already calls RICE
  "prioritization for planning"; this names what the planning is
  and says it wins. Where the plan and the ledger disagree about
  STATUS, the ledger still wins -- the two authorities do not
  overlap.
- **Why it came up.** A session read the missing anchor on the
  2,010-line gallery master plan as evidence the plan was stale and
  proposed ranking it below the ledger on currency. That framing
  implies the plan is deficient and should update more often, which
  would manufacture work. Tony's correction supplied the right
  axis. (The missing anchor itself is not a finding: it is the
  founding case of L-220, already ruled.)
- **Confirmed the same day: the status rule covers session
  DOCUMENTS, not just handoffs and manifests.** The skill stated it
  for handoff-vs-manifest only. Any document written in a live
  session -- a review return, a design note, an analysis -- can
  assert that a question is open when the ledger has settled it.
  Newest bytes are not a claim about what was decided. Recorded in
  `ledger-and-session-records` 1.8 beside the ruling above.
**Note:** RICE is Claude's proposal, unratified.
**Gap:** none -- both rulings are recorded in
`ledger-and-session-records` 1.8 by this patch. Close once a session
confirms its loaded copy reads 1.8.
**CLOSED 2026-08-22.** The condition fired. The session that closed
this loaded `ledger-and-session-records` at 1.8 against a manifest
expecting 1.8, at session start, before any ledger work -- which is
the only place that check CAN fire, because the gate is load-triggered
and a skill copy is bound when the conversation starts. Deferred
verification, carried in writing, settled against the one thing a
later session can actually read. Same structure as the SHA round trip.
**Ref:** `skills/ledger-and-session-records/SKILL.md` "The Document
Stack"; LEDGER_CONSOLIDATED.md "RICE scoring -- prioritization for
planning"; L-220 (Stamp What You Change); L-215 (the RICE tail
measurement); L-214 (the session this surfaced in); L-224 (the first
item sequenced under this ruling).

#### [L-233] Three dashboard buttons: one fixed, one added, one retired
<!-- L:233 status:DONE upd:2026-08-24 section:C flag: rice:2/2/95/1 -->
- **Tony asked for a review of four Gallery & Web buttons, 2026-08-24.**
  Two earned their place unchanged, one had an interface it could not
  satisfy, and one had outlived the question it was built to answer.
- **Gallery Builder Offline Tests -- kept, and the strongest of the
  four.** Run this session: 144 checks, zero failures, no network. It
  exercises first-build, the nightly shrink gate and the Guard v2
  monitor path. Worth noting for later that a button someone has to
  remember is weaker than a checker in the maintenance suite; moving it
  there is not done and is not tracked here.
- **Gallery Cleanup -- kept.** Orphan JSON and KMZ accumulate for as
  long as curation continues, and it confirms before deleting.
- **Inspect Staging -- the tool was right, the BUTTON could not work.**
  `main()` required `len(sys.argv) == 2` and the dashboard launches with
  no argument, so clicking it could only ever print usage. Fixed in the
  TOOL rather than by special-casing the dashboard, so the VS Code Run
  button gets the same benefit: it now asks for the staging folder, and
  a pasted Windows path keeps working because surrounding quotes are
  stripped. A path on the command line still works unchanged and a
  flag-shaped argument is still refused.
- **The description was the other half.** It read "Takes one argument,"
  which described the tool correctly and the button misleadingly. The
  new text says what the report contains and that it asks for the path.
- **Debug Encke TP -- retired from the dashboard, file kept.** It
  existed to answer one question: which Horizons identifier form
  resolves Encke's TP. Closed. `objects_config.json` carries
  `horizons_id: 90000091`, `id_type: smallbody`, the same pattern as
  Halley's `90000030`, which is the fix the tool's own docstring reasons
  its way to. It was also the only button on the dashboard that made a
  live Horizons call, so it was the only one that could fail for reasons
  unrelated to this code. The file stays as the record of the
  investigation; deleting it would lose the reasoning.
- **Serve Gallery Locally -- added.** `tools/serve_gallery.py` serves the
  gallery repo root at `localhost:8000` and opens the assembler dev
  page. It serves the ROOT rather than `gallery/` because the page
  reaches up to `../data/solar-system/`; served from inside `gallery/`
  the page loads and every fetch 404s, which looks like a broken page
  rather than a wrong working directory. It refuses to start when the
  served cache is absent and says which files are missing, and when the
  port is already taken it opens the browser against the running server
  instead of failing on a socket error. Both guards were exercised.
- **A batch-file draft was superseded before it shipped.** The dashboard
  launches Python scripts, not `.bat` files, so a `.bat` would have been
  a second implementation of the same checks in a language the dashboard
  cannot call. One implementation, in Python.
- **Ref:** `palomas_orrery_dashboard.py` (Gallery & Web group); gallery
  `tools/serve_gallery.py`, `tools/inspect_staging.py`,
  `tools/debug_encke_tp.py`, `tools/gallery_cleanup.py`,
  `tools/test_gallery_cache_builder_offline.py`;
  `patch_L233_1_gallery_devtools.py` (gallery),
  `patch_L233_2_dashboard_and_handoff.py` (orrery); L-154; L-188 (the
  maintenance runner).

#### [L-100] Gallery feature-render surface: shells gallery-side vs interactive-side (OPEN QUESTION)
<!-- L:100 status:DONE upd:2026-08-25 section:C flag: rice:2/2/50/2 -->
- Two-surface principle (L-098) extended to ALL shells (atmospheres,
  magnetospheres, Van Allen belts, rings, comet nucleus/coma/tail). Default:
  shells live GALLERY-side (pre-rendered authored artifacts, zero browser code);
  the interactive stays light (conics + positions). OPEN, TONY'S CALL: which
  shells (if any) are cheap+static enough to ALSO render interactive-side --
  candidate: simple scaled-sphere/torus (atmosphere, Van Allen); gallery-only:
  geometry/physics/animation (magnetosphere bow shock, comet tails, ring
  structure). Aesthetic (worth showing live) + cost (a browser port per
  interactive-side shell). Own design pass; do not guess. Flows through
  feature_configs.json. Ref: GALLERY_DATA_SOURCE_HANDOFF.md v0.3.
**RULED AND CLOSED 2026-08-25 (Tony).** The default recorded above --
shells gallery-side, the interactive kept light -- was inherited from
the Phase-1b cost framing of 2026-07-08 and was never a decision. Tony:
"it is not my intent. The general intent is to redo the orrery in the
assembler. Part by part." So the answer to "which shells, if any, also
render interactive-side" is ALL of them, taken part by part, with
artifacts reopening as families are added. See L-234.

#### [L-250] The Braid added to Part 3 as a general principle
<!-- L:250 status:DONE upd:2026-08-25 section:C flag: rice:4/4/95/1 -->
- **Protocol v3.43, 2026-08-25.** "The Braid -- The Artifact Orders the
  Work" added to Part 3 directly after The Artifact Bounds the Audit,
  which it extends by one axis: that rule bounds which values are in
  scope, this one bounds which are in scope NEXT, and it applies to any
  correctness program rather than to provenance alone.
- **Why it was not already there.** Tony's ruling of 2026-08-22 lived
  only in `MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a, which carries
  SEQUENCING authority for the gallery. He was applying it to the
  constants work as well -- from memory, because it was written nowhere
  that fires. Tony, 2026-08-25: "it is a meta-principle. its not even in
  the protocol as such."
- **What made it urgent.** A constants migration ran global on
  2026-08-25 and did not terminate. One conversion factor led to a
  shadow name, to three aliases, to a second constant at 38 sites across
  11 modules, in a single evening, while the artifact on the critical
  path moved not at all. Every step was locally justified and nobody
  chose the day's shape.
- **Two additions beyond the master plan's version.** The
  DISCOVERY/REMEDIATION split -- discovery enumerates against a stated
  pattern and fixes nothing, so it terminates because the tree is finite
  -- and ONE ledger row per CLASS rather than one per instance, so the
  backlog grows by kinds instead of counts.
- **Version history.** v3.40 moved down to
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` PART 1 to keep three
  entries resident, per the rule L-199 asked for.
**Gap:** none. Closed on delivery.
**Ref:** PROJECT_INSTRUCTIONS v3.43 Part 3; L-244 (the first program the
rule bounds); L-248; L-199 (the three-resident cap); The Artifact Bounds
the Audit.

## D. RECONCILED LEDGER -- OPEN

### D.Movement -- Movement-track open items

#### [L-008] v24 sec5 precision batch (low-risk)
<!-- L:008 status:OPEN upd:2026-06-21 section:D.Movement flag: rice:2/2/50/2 -->
- **v24 sec5 precision batch** (low-risk): three magnetosphere/bow-shock
  precision upgrades -- (1) a Jupiter toggle between its compressed (solar-max)
  and expanded (solar-min) magnetopause standoff; (2) upgrade Earth's
  magnetopause + bow-shock values to cited sources; (3) per-body bow-shock
  eccentricity (body-specific shock shape, not a shared approximation).
  `[per chain]` (The inner-four bow-shock hover km/AU sub-item `[verified
  @76c330e]` is de-duped to L-052 / section E -- the AU-convention home -- so it
  is not double-counted; the precision batch keeps the three physics sub-items.)
**Note (2026-06-21):** distinct from L-007. L-007 was the bow-shock hover
  DISCLOSURE (sourced-vs-schematic + animation-freeze note), now DONE / in C.
  L-008 is the precision-VALUES batch -- different content, real remaining work.
**Tony:** Clarify description. Update RICE.   

#### [L-061] Magnetosphere-dipole frame coupling / seasonal roll
<!-- L:061 status:OPEN upd:2026-06-21 section:D.Movement flag: rice:1/1/50/3 -->
- **Magnetosphere-dipole frame coupling / seasonal roll** -- OPEN, deferred.
  Promoted from L-009 (2026-06-20). Two frames the render currently keeps separate
  are physically COUPLED:
    * the dipole cone is BODY-locked (spin-pole frame, Sun-independent);
    * the magnetosphere is SUN-locked (bow-shock-to-tail axis follows the
      planet->Sun line).
  As the planet orbits, the Sun-line sweeps ~360 deg once per orbital YEAR, so the
  magnetosphere reorients in inertial space while the spin/dipole axis stays fixed
  -- the dipole orientation appears to ROLL relative to the magnetosphere, once per
  orbit. (Tony confirms, 2026-06-20: the dipole does not travel WITH the
  magnetosphere, but has a dynamic relationship with it -- it rolls with respect to
  the magnetosphere as the planet orbits the Sun.)
  AMPLITUDE = OBLIQUITY: the spin-axis-to-Sun-line angle swings over the orbit with
  amplitude equal to the axial tilt (magnetospheric "seasons") -- near-nil for
  Mercury (~0) and Jupiter (~3 deg); meaningful for Earth (23), Saturn (27),
  Neptune (28); extreme for Uranus (~98 deg, pole swings sunward at solstice over
  its 84-yr orbit).
  WHY ITS OWN ITEM (new physics, not a cone remainder): the real magnetosphere's
  SHAPE responds to the dipole tilt and the interplanetary field, not just the
  Sun-line. Modeling the coupling is a Mode-7 question (envelope-orientation
  physics -> Gemini, not asserted from memory). Folds in the L-009 offset-direction
  remainder (mode 2).
**Gap:** scope DELIBERATELY UNREFINED (Tony: capture broad, do not refine yet -- seasonal-roll-only vs full coupling is a judgment call for whoever picks it up). Visible/teachable only under envelope animation across enough of an orbit for the obliquity-driven angle to shift, dramatic only for high-tilt bodies -- the natural build/re-open trigger. RICE is a placeholder pending deliberate scoring.

### D.Priority -- real bugs

#### [L-012] Osculating pre-fetch false-provenance messages
<!-- L:012 status:OPEN upd:2026-06-21 section:D.Priority flag:CRIT rice:2/2/90/1 -->
- **What it is (plain version).** When you choose "use existing elements" (the
  cached path), the program correctly loads osculating elements FROM CACHE -- but
  the console then prints messages claiming a FRESH FETCH that did not happen:
  "[SUCCESS] Mercury fetched fresh data" and "[PRE-FETCH] OK: <obj>: Updated".
  The log says "fresh" over cached data. (The variable is even named
  fresh_elements but holds cache on that path.)
- **Why CRIT (not cosmetic).** Cite-over-recalled failure class: a SUCCESS /
  "fresh" stamp printed over cached elements can hide a STALE element -- you would
  trust an old position because the log told you it was freshly fetched. A false
  provenance line is exactly what the protocol treats as load-bearing. The render
  looks fine; the trust signal is the lie.
- **Two defects found alongside the main one:**
  1. The "[SUCCESS] ... fetched fresh" line is HARDCODED to Mercury
     (`if obj_name == 'Mercury':`, palomas_orrery.py:4464) -- leftover debug.
     Every other object gets only the false "Updated".
  2. The age channel is DEAD: calculate_age_days (:285) swallows its error in a
     bare except and returns None, so the cached element's real solution date
     can't be shown -- it reports "unknown age".
- **Honest fix.** Print the ACTUAL path (fetched vs cached); on a cache hit say
  so and show the element's real solution date instead of "fetched fresh" /
  "unknown age". Drop the Mercury-only hardcode so the message is correct for all
  objects.
- **LATENT sub-bug (separate, lower-priority).** Fresh-save writes a CENTER-AWARE
  key cache[cache_key] (:804) but the fallback reads the BARE key cache[obj_name]
  (:832). They coincide for heliocentric (key == name) but DIVERGE for
  barycentric / body-centered cases like 'Charon@9' -- one producer, two key
  conventions, so a non-heliocentric center can miss or read the wrong cached
  element. Split to its own L-handle if it grows.
**Gap:** the logging fix (report fetched-vs-cached + real solution date; drop the Mercury hardcode) is the CRIT part, ~0.5 session. The cache-key divergence is a separate, smaller follow-on.
**Ref:** osculating_cache_manager.py:813-815/832/285/804; palomas_orrery.py:4464/4471/4473 

#### [L-013] Mercury 2019-epoch anomaly
<!-- L:013 status:DEFERRED upd:2026-06-15 section:D.Priority flag: rice:1/1/10/2 -->
- **Mercury 2019-epoch anomaly** (June 15, UNRESOLVED, deferred to recurrence).
  doc-1 rendered Mercury's Keplerian with epoch 2019-01-01 osc. / 2018 perihelion
  while Venus/Earth were current. NOT stale cache (project is 18 months old) and
  NOT the static fallback (planetary_params['Mercury'] epoch = 2025-11-19).
  Grounded: doc-1 params had MA/TA keys -> OSCULATING source (the static dict has
  neither); the 2019 element was a runtime set, since overwritten by Tony's update
  (current Mercury correct: epoch 2026-06-15 17:50, marker 0.433395 == hover
  0.4333945989). Origin not determinable from disk; recollection insufficient.
  ACTION: if it recurs, capture osculating_cache_backup.json at that instant
  and/or add a one-line element-source+epoch print at fetch time before
  theorizing. LESSON re-affirmed: Claude's "7-year stale cache" was a recalled
  inference dressed as fact; Tony's domain knowledge overrode it (Observation
  Override).
  **Tony:** this was a one-time observation. i do not know what caused it. pending better definition. 

### D.Structural -- dead-code / honest shell files (Phase 3)

`[per v23/v25 chain unless tagged]`
**Tony:** dead code items are good canditates for a cleanup pass. 

#### [L-015 | #5] _info import cleanup (~89+87 imports, 2 files)
<!-- L:015 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:2.5/1/75/2 -->
Named dead imports removed (hover_text_sun, create_planet_visualization)
from helpers.py [verified @feab717, patched this session].
**Gap:** ~78 remaining dead _info string imports in helpers.py (89 imported,
~11 used). Broader sweep deferred; low-risk, moderate volume.
**Ref:** grep confirmation this session; patch_dead_imports.py.

#### [L-016 | #6] Archive dead shell functions
<!-- L:016 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:1/1/90/1 -->
create_planet_visualization() at planet_visualization.py L558 is annotated
RETIRED (June 2026, Phase 2.5). Zero callers confirmed -- all references
are in comments/docstrings. Two retired Sun functions in the same file
(L293, L306) are similarly dead. Also: create_neptune_magnetic_poles() in
neptune_visualization_shells.py is marked DEPRECATED (D2 Option C, May 2026).
**Gap:** grep-confirm zero callers across both pipelines (plot_objects +
animate_objects), then delete bodies. Low risk; cleanup only.
**Ref:** planet_visualization.py L558, L293, L306; neptune_visualization_shells.py. (umbrella: L-068)

#### [L-068] Static/animation pipeline consolidation -- remaining residuals (umbrella)
<!-- L:068 status:OPEN upd:2026-06-23 section:D.Structural flag: rice:2/2/75/2 -->
- **Umbrella thread for the remaining practical consolidation of the static
  (plot_objects) and animation (animate_objects) pipelines.** The big structural
  unification is DONE -- see section C ("shell-consolidation + animation refactor")
  and the Consolidation Log (F): scene-assembly unified, the three animation
  pipelines merged, explicit blocks deleted in both pipelines, one unified dispatch.
  What remains is distributed across three discrete residuals, tracked here as one
  thread:
    - L-066 -- behavioral parity gap: MAPS tail renders in the static path but not
      the animation path (one-line L2324 gate). The "make the two paths agree" task.
    - L-016 -- cleanup: grep-confirm zero callers across both pipelines, then delete
      the dead duplicate shell-function bodies the unification left behind.
    - L-014 -- the one render path still OUTSIDE the unified dispatch (the four
      asteroid belts via standalone create_main_asteroid_belt()); fold into
      CUSTOM_SHELLS or keep standalone (design call).
  This item is also the HOME for any NEW static/animation parity gap. The standing
  "fix both pipelines or neither" rule is a PRACTICE, not a backlog item, so new
  gaps surface only when caught by eye (the way MAPS/L-066 did) -- when one appears,
  log it here as a sibling of L-066.
**Gap:** none of its own -- this thread closes when L-066, L-016, and L-014 all
close AND no parity gap is outstanding. Tracking/umbrella item.
**Ref:** L-066, L-016, L-014; section C strategic-status block; Consolidation Log (F);
protocol Part 3 "Check All Parallel Pipelines".

#### [L-025 | #N7] Reduced to custom-geometry inline markers only
<!-- L:025 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/50/2 -->
The Phase 3 info-marker sweep (141 conversions, 18 files, May 2026) moved
sphere-shell markers to the create_info_marker() factory. Inline marker
dicts should now only remain in CUSTOM_SHELLS builders (rings,
magnetospheres, radiation belts, etc.) which need geometry-specific
positioning.
**Gap:** audit -- grep for inline marker dicts outside CUSTOM_SHELLS
builders. If none found, close. Zero code risk.
**Plain version:** a code-tidiness audit, NOT a render/Mode-5 issue. After the May
sweep, simple sphere-shell info-markers all go through one factory; custom-geometry
shells (rings, magnetospheres, belts) keep their markers inline because they need
special positioning. This item just greps the *_visualization_shells.py files for any
OLD inline-marker definitions left OUTSIDE a custom-geometry builder -- stragglers the
sweep missed. None found -> close. (Deferred until run.)

#### [L-027 | #61] Platform Neutrality (SystemButtonFace)
<!-- L:027 status:OPEN upd:2026-06-18 section:D.Structural flag: rice:3/2/75/2 -->
26 occurrences of the Tk color name SystemButtonFace in palomas_orrery.py.
Resolves on Windows; fails on Linux/macOS. The xvfb pre-test sed swap is
a workaround, not a fix. Options: hex literal '#F0F0F0', platform
detection (sys.platform), or ttk styling.
**Gap:** choose replacement strategy, then sweep. Design decision before
build. Moderate scope (26 sites); low functional risk (cosmetic only).
**Platform neutrality:** same goal as L-026 (the LF sweep) -- pair them. This is the Tk
color-name half (SystemButtonFace -> hex literal / sys.platform detection / ttk).

### D.Cosmetic -- polish (bundle when convenient)

**Tony:** the `[per chain]` notes require development. probably a mode 5 pass and rice updates. 

#### [L-030 | #17] GEO info-marker position
<!-- L:030 status:OPEN upd:- section:D.Cosmetic flag: rice:1/1/100/1 -->
`[per chain]`

#### [L-031 | #18] Uranus gossamer ring visibility
<!-- L:031 status:OPEN upd:- section:D.Cosmetic flag: rice:1/2/90/2 -->
`[per chain]`

#### [L-032 | #41] Sun legend ordering (ordered dispatch iteration; no manual fix)
<!-- L:032 status:OPEN upd:- section:D.Cosmetic flag: rice:2/2/75/2 -->
`[per chain]`

#### [L-033] Comet plotted-period trace visibility (line weight/color; O6b)
<!-- L:033 status:OPEN upd:2026-06-10 section:D.Cosmetic flag: rice:2/1.5/100/2 -->
- Comet plotted-period trace visibility (line weight/color; O6b June 10).

#### [L-034] Center-body hover "Distance to Center Surface" negative-radius formatting
<!-- L:034 status:OPEN upd:2026-06-21 section:D.Cosmetic flag: rice:1/1/75/0.5 -->
- **What it is.** The detailed hover already shows two distances correctly: a
  distance to the center body's CENTER (r=0) and a distance to its SURFACE. The
  bug is only on the CENTER BODY'S OWN hover: because the formatter treats the
  center as an object at the origin, its surface line renders as a NEGATIVE radius
  -- "Distance to Center Surface: -<radius> km (below mean datum)". The
  magnitudes are right; only the sign/label on the center body's own surface line
  reads wrong.
- **Fix.** In format_detailed_hover_text, special-case the center body so its own
  surface line reads sensibly (drop the misleading minus, or relabel). Mode-5 to
  confirm the exact wording you want.
**Gap:** decide display wording (Mode-5), then a targeted edit to format_detailed_hover_text. Cosmetic; zero functional risk.

#### [L-035] Solar shell hovertext <br> vs \n context mismatch (C6b)
<!-- L:035 status:OPEN upd:2026-06-11 section:D.Cosmetic flag: rice:2/2/100/1 -->
- Solar shell hovertext uses '<br>' where '\n' renders (or vice versa;
  context-specific -- C6b finding, June 11). Fix in the affected
  formatter on next touch.

#### [L-037] WARNING: Unknown object type 'satellite' (spurious; handled downstream)
<!-- L:037 status:OPEN upd:2026-06-15 section:D.Cosmetic flag: rice:1/1/90/1 -->
- `WARNING: Unknown object type 'satellite'` fires once per satellite (Triton/
  Despina/Galatea in the June-15 gate). Handled correctly downstream (orbits
  plotted, Keplerian properly skipped as Satellites) -- spurious; a type-dispatch
  that does not list 'satellite'. Silence on next touch of that dispatch.

#### [L-038] Psyche encounter hardcoded fallback distances lack # Source
<!-- L:038 status:OPEN upd:- section:D.Cosmetic flag: rice:1/1/75/1.5 -->
- Psyche encounter HARDCODED FALLBACK distances (8,009 km Mars GA / 1,151 km
  Phobos), used when Horizons has no ephemeris past 2029-06-11 (expected,
  graceful), lack a `# Source:` -- add one (provenance discipline) on next touch.
  **Tony:** unclear why the provenance scanner has not flagged this item. 

#### [L-124] Ring/belt color accuracy audit across the orrery -- nice-to-have, not a blocker
<!-- L:124 status:OPEN upd:2026-07-16 section:D.Cosmetic flag: rice:1/1/60/5 -->
- **What it is.** Ring/belt colors in Saturn (`ring_params` in
  `create_saturn_ring_system`), Jupiter (`ring_params` in
  `create_jupiter_ring_system`; `belt_colors` in
  `create_jupiter_radiation_belts`), and Earth's Van Allen belt colors are
  developer/AI aesthetic picks for visual distinction, not measured
  photometric values -- confirmed directly by Tony (July 16, 2026), who
  also judged that citing Jupiter's ring colors as accurate would be an
  overstatement: colors are attempts at representation, coverage is
  uneven, and the real boundaries aren't known -- the same shape as the
  original provenance problem, but harder to see because a real citation
  sits right above the dict and, per the project's usual "unit of
  provenance" convention, reads as if it covers the colors too. It
  doesn't. Real ring/belt coloration is also highly viewing-geometry- and
  processing-dependent (true vs. enhanced color), so "accurate" is a soft
  target here, not one fixed correct value.
- **Sourcing found this session** (real NASA/Cassini material, descriptive
  not numeric -- captured here so it is not lost): Saturn's rings are water
  ice contaminated by rock/carbon compounds; the B ring has "a pronounced
  sandy color"; dark-side natural-color imagery describes the rings
  glowing "in shades of brown and gold"; Voyager 2 enhanced-color
  processing found the C ring / Cassini Division carry a blue tint
  (false-color, a weaker claim than the true-color findings above).
  - https://science.nasa.gov/missions/cassini/saturns-rings-offer-a-fresco-of-color/
  - https://science.nasa.gov/resource/true-colors/
  - https://science.nasa.gov/image-detail/pia01486-3/
  - https://science.nasa.gov/resource/ringscape-in-color/
- **Tony's call (July 16, 2026):** do not chase color accuracy now -- a
  real pass would be a major undertaking for marginal payoff, and true
  ring appearance is itself highly variable. Correct move for now: honest
  in-source disclosure ("colors selected by the developer, not visually
  accurate"), with Jupiter's pre-existing citation explicitly narrowed to
  geometry-only so it can't be misread as covering color. Done this
  session for both Saturn and Jupiter.
**Gap:** see L-125.
**Ref:** `saturn_visualization_shells.py` `create_saturn_ring_system`;
`jupiter_visualization_shells.py` `create_jupiter_ring_system` /
`create_jupiter_radiation_belts`; `earth_visualization_shells.py` Van
Allen belt colors; F1 manifest sourcing question that prompted this
(PHASE2_F1_BUILD_MANIFEST_v2.md sec 4.2, corrected this session).
**Tony:** RICE proposed 1/1/60/5 (nice-to-have, little functional impact,
real effort to do properly given viewing-geometry variability) -- yours
to finalize.

#### [L-125] Color/RGB values excluded from provenance-scanner claims -- report-level disclosure (project-wide)
<!-- L:125 status:OPEN upd:2026-07-16 section:D.Cosmetic flag: rice:2/2/95/1 -->
- **What it is.** `_make_dict_unit` in `provenance_scanner.py` already
  skipped color/RGB values when building a dict unit's scored `entries`
  (colors never became individual claims needing citation) -- but the
  module's own "unit of provenance" documentation said a block
  `# Source:` comment covers a whole dict as ONE unit, which reads as if
  it also certifies that dict's `color` field(s). It doesn't, and at
  least one real case (Jupiter's `ring_params` -- `# Source: NASA Jupiter
  Ring Fact Sheet`) was being read that way until Tony caught it (July
  16, 2026): "citing Jupiter's colors as accurate is an overstatement...
  colors are attempts at representation, but it's uneven and we don't
  really know the boundaries. Much like the original provenance problem
  only worse."
- **The fix (documentation only, zero scoring change):** the module
  docstring's numbered known-limitations list gets a new item 11 stating
  this explicitly, and `generate_report()` gets a standing disclosure
  paragraph printed at the top of every generated `PROVENANCE_AUDIT.md`,
  right after the existing "Unit of provenance" line -- so it's visible
  in the report itself, not just in code comments. Verified in a
  disposable clone: `py_compile` clean, ASCII-only, and re-running the
  scanner reproduces identical tier counts (673 findings, 102/155/396/20)
  -- confirms no scoring regression, this is purely a documentation add.
- **Scope decision (Tony, July 16, 2026):** do this once, at the scanner
  + report level, instead of individually narrowing citation comments in
  the ~20 live custom-shell functions (magnetospheres, radiation belts,
  rings, plasma tori) that have the same real-citation-near-color
  pattern. "I am not sure it is worth commenting on every color choice
  we make." Two per-file snippets drafted earlier this session (Jupiter
  ring citation, Saturn ring disclosure) are superseded by this and
  should NOT be applied -- this covers them and everything else
  uniformly.
**Gap:** apply `patch_provenance_scanner_color_exclusion.py` (delivered
this session) to `provenance_scanner.py`, then re-run the scanner to
regenerate `PROVENANCE_AUDIT.md` with the new disclosure visible.
**Ref:** L-124 (the separate, deferred wishlist for an actual
color-accuracy pass, if one is ever undertaken); `_make_dict_unit`,
`generate_report()` in `provenance_scanner.py`.
**Claude:** RICE proposed 2/2/95/1 (fixes a real overclaim risk codebase-
wide, high confidence, small effort -- documentation only) -- yours to
finalize.

#### [L-133] Codebase-wide CRLF sweep (beyond L-026)
<!-- L:133 status:OPEN upd:2026-07-17 section:D.Structural flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/17/26, pre-ledger note).** Review the codebase for any
  remaining CRLF endings beyond palomas_orrery_helpers.py (L-026, DONE
  2026-07-15). LF is the project standard.
- **Note (Claude, 2026-07-17):** .gitattributes (`* text=auto eol=lf`)
  added at repo root -- normalizes CRLF to LF automatically on `git add`
  going forward (root cause: text pasted from chat/browser lands as
  CRLF; without a git-level rule, a single pasted chunk could flip a
  whole file's save-time EOL). This closes the recurring-drift half of
  the problem.
**Gap:** narrower now -- a one-time sweep of files already CRLF in the
repo from before this rule existed (the .gitattributes fix doesn't
retroactively touch files it hasn't seen re-added).
**Ref:** to_do_ideas.md (pre-ledger, 4/17/26); companion to L-026, L-087.

#### [L-135] Basic-plot file-size bloat (non-shell) -- Mercury-alone example
<!-- L:135 status:OPEN upd:2026-07-17 section:D.Structural flag: rice:2/2/50/2 -->
- **Bug/idea (Tony, 4/17/26, pre-ledger note -- two entries merged).**
  Basic plots run unexpectedly large: orbit of Mercury alone ~450 KB,
  Studio preview ~600 KB. Companion note suggested applying the solar-shell
  hovertext-reduction approach more broadly.
- **Flagging, not assuming closed.** The single-info-marker pattern
  refactor (v3.22, May 12 2026 -- 141 conversions, 9-13 MB/render savings)
  already applied this exact technique to SHELL traces. A bare Mercury
  orbit has no shells, so if the bloat is still there it likely comes from
  a different source (per-point hover on the orbit/marker trace itself).
  Numbers are 3 months stale.
**Gap:** re-measure current file size for a minimal single-planet plot;
confirm whether single-info-marker already covers this or whether basic
orbit/marker traces need the same treatment.
**Ref:** to_do_ideas.md (pre-ledger, 4/17/26 x2); cross-ref v3.22 refactor.

#### [L-164] dep_trace.py section-divider non-ASCII bytes
<!-- L:164 status:OPEN upd:2026-07-26 section:D.Structural flag: rice:1/1/90/1 -->
- **What.** dep_trace.py's section-divider comments use the Unicode
  box-drawing character (U+2500), e.g. `# -- Configuration --...--`,
  instead of ASCII. 1279 non-ASCII bytes across 8 divider lines,
  confirmed by byte-level scan (independently reverified against
  live HEAD at both Phase 3b close and Phase 4 -- byte count
  unchanged both times, so pre-existing and not introduced by
  L-163). Violates the protocol's ASCII-only convention (Windows
  mangles Unicode in generated/edited files; Tony works exclusively
  through GitHub Desktop and VS Code's Run button on Windows).
**Note:** proposed rice:1/1/90/1 (low reach/impact -- cosmetic,
Windows-safety only, nothing currently broken; high confidence;
trivial effort) -- adjust if you'd score it differently.
**Gap:** Replace the 8 divider lines with ASCII equivalents
(binary-mode patch per safe-file-editing skill, not sed). Small,
mechanical, no behavior change.
**Ref:** dep_trace.py; AS_BUILT_L163_phase3b_close.md,
AS_BUILT_L163_phase4.md (both flagged this without capturing it --
third mention, now captured).

#### [L-171] patch_ledger_index_retired_handles.py breaks L-163's zero-undetermined close
<!-- L:171 status:OPEN upd:2026-07-29 section:D.Structural flag: rice:1/1/90/0.5 -->
- **What.** Landed July 28 with no `Role:`/`Domain:` docstring tags.
  `classify_role('patch_ledger_index_retired_handles', ...)` returns
  `undetermined` -- confirmed by calling the live function directly.
  Breaks L-163 Phase 3b's "zero undetermined" close two days after it
  closed. Also a one-shot patch script, the exact class L-163 Phase 1
  archived.
**Gap:** add `Role:`/`Domain:` tags to its docstring, or archive it
alongside the seven already-archived one-shot scripts. Either closes this;
archiving is probably cleaner given the class match.
**Ref:** `patch_ledger_index_retired_handles.py`; `module_atlas.py`
(`classify_role`); L-163 (Phase 1, Phase 3b); `AS_BUILT_L163_phase1.md`.

### D.Feature -- Bucket A (near-term)

#### [L-066] MAPS per-frame comet-tail animation wiring
<!-- L:066 status:OPEN upd:2026-06-23 section:D.Feature-A flag: rice:2/3/75/1 -->
- **Wire MAPS into the per-frame comet-tail animation.** In ANIMATION mode the MAPS
  tail does NOT render at all (it renders in STATIC mode only) -- Tony, Mode-5,
  2026-06-23. Extracted from L-056. The earlier "non-animation BY DESIGN" notes
  (L-004 / L-011, now in C) recorded the Phase-4 DEFERRAL (ADDENDUM_phase4 decision
  1), NOT a permanent exclusion -- the wiring is wanted and was always scoped as
  deferred, not done. THE FIX (handoff v29 scoping): remove the one-line gate at
  palomas_orrery.py L2324 (`if name == 'MAPS': continue`). build_comet_tail_traces
  is shared with all comets -- NO MAPS-specific code needed. Static path
  (plot_objects L6062) already handles MAPS.
**Gap:** PREREQUISITE -- review ADDENDUM_phase4 decision 1 (two-site exclusion
warning + partition design) before removing the L2324 gate. Risk: frame-1 tail
doubling (known pattern, known guard; Tony reports it currently GONE -- verify it
stays gone). Mode-5 gate: MAPS tail animates per-frame like the other comets
(updates each frame), no frame-1 doubling, exclusion warning still correct.
**Ref:** extracted from L-056 (2026-06-23); ADDENDUM_phase4 decision 1; handoff v29;
palomas_orrery.py L2324 (gate) + L6062 (static path); build_comet_tail_traces;
prereqs ADDENDUM_phase4_decisions.md + HANDOFF_animation_phase4_brief.md. (umbrella: L-068)

#### [L-039 | #23] Earth ionosphere shell
<!-- L:039 status:OPEN upd:2026-06-21 section:D.Feature-A flag: rice:2/2/60/2 -->
- **Add an ionosphere shell to Earth's visualization** -- a new atmospheric shell
  alongside Earth's existing shells. The ionosphere is the ionized upper-atmosphere
  region (~60-1000 km altitude, D/E/F layers). Pattern is the established one: a
  SHELL_CONFIGS / CUSTOM_SHELLS entry with sourced altitude bounds, a checkbox
  toggle, the single-info-marker pattern, and hover carrying km + AU per convention.
**Gap:** SOURCE the layer boundaries before any literal (Fetched-vs-Recalled -- cite, do not recall); pick the representation (single band vs D/E/F sub-layers); then build on the Earth shell pattern. Light design, then standard shell build.

#### [L-040 | #19] Plot-cube control parity + scaling/camera comprehensive review
<!-- L:040 status:OPEN upd:2026-06-13 section:D.Feature-A flag: rice:3/3/50/3 -->
- **19 Plot-cube control parity + SCALING/CAMERA COMPREHENSIVE REVIEW** --
  JOINED / cross-repo. The original parity scope (scene_axis_range,
  scene_dtick, aspectmode, camera orientation, axes/grid toggles; Studio
  side `[verified @2f40d9d]`; design authority 3d_axis_control_handoff.md)
  PLUS, per Tony's June-11 framing call, the accumulated scaling/camera
  FIXTURE LIST (all scaling work lives here; no separate session track):
    * Photosphere auto-scale collapse (static Auto = shell extent alone,
      hiding orbits; Session-A Finding 1 concrete case).
    * Sun-Direction indicator clipped by cube range (Finding 1 / O12)
      -- FIXED in Phase 4 (June 12) `[render-gated]`: geometric clamp in
      create_sun_direction_indicator (ray-cube exit along the sun
      direction, 0.95 margin, min_scale floor wins); axis_range threaded
      through the unified dispatch (Manual scales only -- Auto widens to
      2x shell extent AFTER the dispatch, so the incoming range would
      over-clamp) and into both engine indicator specs via a
      collect-time range hint (the animate pipeline's orbital-derived
      Auto range CAN undercut the shell-scaled length -- the O12 case).
      No-range path byte-identical (smoke-tested).
    * Sun orbit around a planet center lacks cube buffer (O12).
    * Fly To zoom limit ignores shell extent (computed from orbital
      distance/marker size; planets stop too far out to see magnetosphere
      or belts; comets okay). (O13b, June 11.) RESOLVED (Phase 4 render-
      gate, June 13) `[render-confirmed Mode 5]`: window sizing replaced
      the body-radius multiple with the LARGEST ACTIVE element's MEASURED
      extent -- traces_extent_from_center() (shared_utilities) is the one
      producer; the static dispatch records fig._body_element_extent_au per
      body and the per-frame allocator records _perframe_body_extent, and
      BOTH the camera-tracking window and add_fly_to_object_buttons
      (new target_extents param) consume it. Sodium tail on -> window
      opens to ~0.20 AU to hold the whole 10,003-radii tail; tail off ->
      collapses to ~0.002 AU on the magnetosphere (Tony's call: largest
      active element sets the size). The empty-box Fly To is gone.
    * CAMERA TRACKING across animation frames -- IMPLEMENTED in Phase 4
      (June 12) and RENDER-CONFIRMED in the Phase 4 render-gate session
      (June 13) `[render-confirmed Mode 5]`. The view window translates
      with the body while the camera stays FREE (the user can orbit during
      playback). UI: 'Camera: track body across frames' combobox in the
      Per-frame elements group; requires redraw=True (already set).
      MECHANISM CHANGE (June 13 live fix): per-frame go.Frame(layout=...)
      scene ranges are UNRELIABLE for a 3D scene when the window is tiny
      relative to the body's offset from origin -- Plotly silently drops
      the per-frame range and autoranges the whole Sun-body span (the
      sodium-tail-off case: a 0.0045 AU cube 0.42 AU from origin swung to
      ~0.4 AU and went non-uniform; the body also rendered off-center and
      effectively invisible). FIX: save_utils._inject_camera_tracking
      injects a post_script that applies the body-centered window via
      Plotly.relayout on load (centers the body) and on every
      plotly_animatingframe (holds the window) -- the documented-reliable
      path for driving a 3D scene during animation; data stashed as
      fig._track_relayout_data keyed by frame date. Routes through
      _write_html so it reaches BOTH the browser-opened and the saved
      offline file (saved round trip render-confirmed). The frame.layout
      path is kept as a no-JS fallback; the relayout runs after the frame
      and wins. This IS the JS event-based follow-on the prior RESIDUAL
      parked (ADDENDUM_phase4 amendment C) -- now built.
      RESIDUAL (OPEN -- item 1 attempted June 13, RENDER-FALSIFIED, then
      REVERTED): dropping the scene from frame.layout (frames data-only, JS
      as sole per-frame window owner -- item 1) did NOT make the cube
      uniform. The render still showed the cube differing BY AXIS and
      swinging ~0.15-0.65 AU -- essentially unchanged. So the frame.layout/
      JS conflict was NOT the cause; the render caught the wrong diagnosis.
      Item 1 was pushed (373298d) then REVERTED (frame.layout restored),
      because it bought nothing and cost the large-window partial-hold plus
      the no-JS fallback -- the reverted 33aac56-equivalent behavior is the
      better baseline. REFINED DIAGNOSIS (next-session seed, NOT verified):
      Plotly re-autoranges the 3D scene per frame when frames carry data
      without an explicit range, overriding the JS relayout -- the cube
      differs by axis (autorange fits the asymmetric sodium tail per axis)
      and swings as the tail rotates. SUPPORTING EVIDENCE (console): track
      half-width 0.19612 AU (relayout target ~0.39 cube), but the swing's
      upper bound (~0.65) matches the static auto-scale "+/-0.606714 AU"
      full-orbit autorange -- the scene drifts toward the data-extent
      autorange. CENTERING still holds (relayout midpoint right); only
      SIZE/uniformity is uncontrolled. COSMETIC: Tony judged the wobble
      "not a visual problem"; load-bearing behavior (centering, shell-track,
      saved round trip, reticle) all render-confirmed. DEFERRED to a
      dedicated session with a repro that ACTUALLY RUNS in Tony's browser
      (prior two did not). Won't-fix (accept the wobble) is a legitimate
      close if autorange can't be cleanly suppressed during 3D frame
      animation.
      RETICLE (June 13) `[render-confirmed Mode 5]`: the center '<>' marker
      (a hand-aligned screen-space paper-coord annotation borrowed from the
      star viz, never pixel-exact) is suppressed under camera tracking via
      add_look_at_object_buttons(show_target_marker=_track_body is None) --
      at shell scale with one body there is nothing to disambiguate, and
      the eyeball error shows. Kept in all non-tracking and static views.
    * Directional arrow camera controls for Plotly 3D (Studio has 2D
      D-pad pan; no 3D equivalent) -- precise cameras without the
      mouse; aids shell-scale visual verification. (Promoted June 11.)
    * O16: auto-scale max() Sun-centered case PASSED (C6a, June 11);
      Mercury-centered case retests in v4.1 after the C6d fix.
**Gap:** remaining for item 19: scene_aspectmode + scene_camera parity / read-on-load (next-session scope); camera-tracking per-frame autorange RESIDUAL (dedicated session); 3D arrow camera controls.

#### [L-042 | #20/N5] Shell-resolution GUI control (20/N5) + Fly-to view scaling (49)
<!-- L:042 status:OPEN upd:2026-06-11 section:D.Feature-A flag: rice:2/1/50/2 -->
  20/N5 shell-resolution GUI control (enabler; its backend partially exists
  since Session A -- bow-shock conic already parameterized, sphere-shell
  n_points per-config; remaining: create_magnetosphere_shape promotion +
  per-body density literals). 49 Fly-to view scaling (folds into the
  fixture list above). View-window design (49 + 19 + Studio parity).
  `[per chain unless tagged]`

#### [L-043] Exoplanet/binary synthetic objects hit Horizons fetch (id_type rejected)
<!-- L:043 status:OPEN upd:2026-06-16 section:D.Feature-A flag: rice:1/1/75/2 -->
- (June 16) OBSERVATION logged (pre-existing, NOT item 19.3 / Phase A).
  Exoplanet + binary system plots (static AND animated) route synthetic
  objects through the Horizons fetch path, which rejects their identifiers.
  Reproducible across TRAPPIST-1, TOI-1338 (binary), Proxima Centauri --
  every run, both modes. Console-only symptoms:
    - fetch_trajectory (palomas_orrery_helpers.py ~388) raises
      "id_type (X) not allowed" tracebacks: host_star, binary_star_a/b.
    - "Error fetching data ... id_type (exoplanet|barycenter) not allowed"
      for exoplanets and the system barycenter.
    - "Error fetching data for object 10" (Sun) dumps the full Sun
      properties block: location='@TOI1338_BARYCENTER ' (trailing space)
      is unresolvable -- Sun-relative-to-exo-center goes to Horizons too.
  ROOT: synthetic exo/binary objects carry internal TYPE tags
  (exo_host_star, exo_binary_star, exoplanet, barycenter) forwarded to
  Horizons as id_type; these are positioned by the exo synthetic generator
  and should never hit Horizons. Fetch fails -> caught -> synthetic
  positioning renders correctly (Tony Mode-5 clean; axis ranges right).
  IMPACT: cosmetic to the render; cost is tracebacks (can mask a real
  error) + spurious failed Horizons calls + a Sun-properties dump per
  exo-system plot.
  FIX DIRECTION (deferred): gate the Horizons fetch/data path to SKIP
  synthetic object types (exo_host_star, exo_binary_star, exoplanet,
  exo-system barycenter, Sun-relative-to-exo-center) instead of calling
  Horizons and catching the rejection. Bonus: helpers.py is CRLF
  (standard is LF) -- fold a line-ending normalize into that session.
  Tier: D.Priority-noise. Thread: helpers.py ~388 + id_type assignment in
  exoplanet_systems.py / celestial_objects.py.
**Gap:** gate the Horizons fetch/data path to SKIP synthetic types (exo_host_star/exo_binary_star/exoplanet/exo-barycenter/Sun-relative-to-exo-center); + helpers.py CRLF->LF.

#### [L-113] Port DP-style spacecraft trace thinning to the orrery desktop plotting
<!-- L:113 status:OPEN upd:2026-07-11 section:D.Feature-A flag: rice:2/2/50/2 -->
- **What.** The gallery cache builder's spacecraft pipeline (coarse glide
  backbone + daily-densify inside curated flyby windows + Douglas-Peucker
  thin of the glide only, windows exempt) was verified end-to-end tonight on
  real Voyager 1 data: both flyby windows (Jupiter 1979, Saturn 1980) came
  back with zero gaps -- genuinely daily, un-flattened -- while the 49-year
  glide thinned from 2549 raw points to 29, with a 12-year gap (1992-2004)
  where the trajectory is simply straight. The orrery's own desktop
  spacecraft plotting (spacecraft_encounters.py / idealized_orbits.py /
  plot_objects+animate_objects) does not yet use this technique.
- **Idea.** Bring the same glide-thin/window-exempt pattern to the desktop
  path -- likely fewer total points for long-duration spacecraft (Voyager
  1/2, etc.) without losing flyby detail, reusing the now-proven approach
  rather than reinventing it. Needs the parallel-pipeline check (both
  plot_objects and animate_objects) since the desktop has more than one
  spacecraft rendering path.
- **Gap:** not scoped -- capture-on-first-mention, not a design session yet.
  Whether the orrery's current point density is even a real problem (vs.
  cosmetic) wants a quick look before committing effort.
**Ref:** gallery_cache_builder.py (douglas_peucker, process_object spacecraft
branch); L-102 (related but distinct -- L-102 is the web/interactive.html
served-side thinning, a different consumer; this item is the desktop app
itself); L-112 (the remediation pass that verified DP flyby preservation).

### D.Feature -- Bucket B (editorial; open-ended) `[per chain]`

#### [L-044 | #22] Satellite (and minor-body) internal-structure shells
<!-- L:044 status:OPEN upd:2026-06-21 section:D.Feature-B flag: rice:3/3/90/3 -->
- **Extend internal-structure shells to satellites and minor bodies.** Today the
  layered internal-structure treatment (core / mantle / crust, named layers with
  sourced radii) lives on the planets and the Sun. This carries it to important
  MOONS first (e.g. the Galilean moons, Titan, Triton, Earth's Moon), then outward
  to ASTEROIDS and MINOR PLANETS. Each body gets sourced layer radii, a toggle,
  single-info-marker hover (km + AU), per the existing shell pattern. 20/N5
  (shell-resolution GUI control, L-042) is the on-ramp.
**Gap:** SIGNIFICANT design session first (Tony): which bodies first, which layers per body, sourcing per body (Fetched-vs-Recalled on every radius). Editorial / open-ended -- build only after the design stabilizes. Bucket B.

#### [L-045 | #N14] Miranda inclination tooltip
<!-- L:045 status:OPEN upd:2026-06-23 section:D.Feature-B flag: rice:1/1/90/1 -->
- **Add/verify a hover tooltip on Miranda noting its orbital inclination**
  (~4.3 deg, the highest among Uranus's major moons), so the visible tilt of its
  orbit in the render is explained. Single-info-marker pattern; km + AU where
  distances appear. `[per chain]`

#### [L-128] Comet sublimation shell(s) -- solar-distance chemistry zones
<!-- L:128 status:OPEN upd:2026-07-17 section:D.Feature-B flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/16/26, pre-ledger note).** Add a solar shell (or set of
  concentric shells) marking heliocentric distances at which different
  comet ices begin to sublimate (CO/CO2 far out, water ice closer in) --
  showing where different comet types start forming visible tails and
  what the ice chemistry implies. Educational/storytelling value.
- **Cross-ref:** groups with L-131 (zodiacal dust) and L-136 (scattered
  disk) as new solar-context shell additions -- not planet-relative, so
  these extend SHELL_CONFIGS/CUSTOM_SHELLS beyond the current per-body
  pattern.
**Gap:** not scoped -- design conversation needed (which species'
sublimation distances, single vs. multi-shell, data source).
**Ref:** to_do_ideas.md (pre-ledger, 4/16/26).

#### [L-130] Restore six-elements + M0@J2000 plotting mode (educational, alt)
<!-- L:130 status:OPEN upd:2026-07-17 section:D.Feature-B flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/16/26, pre-ledger note).** Restore, as an alternative
  mode, drawing an orbit directly from the six classical elements + mean
  anomaly (M0) at epoch J2000 -- rather than always fetching a Horizons
  ephemeris trace. Makes the Keplerian-ellipse-from-elements relationship
  visible and teachable. Surfaced while looking at the 9/9/24 pre-refactor
  version, which apparently had this.
**Gap:** not scoped -- check whether the 9/9/24 approach is recoverable
from git history or needs rebuilding; decide where it lives.
**Ref:** to_do_ideas.md (pre-ledger, 4/16/26).

#### [L-131] Zodiacal dust solar shell
<!-- L:131 status:OPEN upd:2026-07-17 section:D.Feature-B flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/17/26, pre-ledger note).** Add a solar shell for the
  zodiacal dust cloud (interplanetary dust concentrated near the ecliptic).
- **Cross-ref:** groups with L-128, L-136.
**Gap:** not scoped -- design conversation needed (extent, density
profile, data source).
**Ref:** to_do_ideas.md (pre-ledger, 4/17/26).

#### [L-136] Solar "scattered disk" shell
<!-- L:136 status:OPEN upd:2026-07-17 section:D.Feature-B flag: rice:2/2/50/2 -->
- **Idea (Tony, 4/18/26, pre-ledger note).** Add a shell/region for the
  scattered disk (dynamically excited trans-Neptunian population, distinct
  from the classical Kuiper Belt).
- **Cross-ref:** groups with L-128, L-131.
**Gap:** not scoped -- design conversation needed.
**Ref:** to_do_ideas.md (pre-ledger, 4/18/26).

### D.Feature -- Bucket C (architecture; design-before-code)

#### [L-014 | #2] Asteroid-belt migration decision
<!-- L:014 status:OPEN upd:2026-06-20 section:D.Feature-C flag: rice:1/1/75/2 -->
The asteroid belt renders via standalone create_main_asteroid_belt() in
asteroid_belt_visualization_shells.py, called directly (main L2021). It is
not in SHELL_CONFIGS (not a sphere) or CUSTOM_SHELLS (no checkbox-gated
toggle per shell -- the four belts have their own tk.IntVars at main L2883).
Decision: should the four belt geometries move into CUSTOM_SHELLS (like
rings and magnetospheres), or stay standalone?
**Gap:** design decision. Benefits: unified dispatch, factory hover standard,
one fewer standalone call path. Costs: belt geometry is scattered-point
clouds, not sphere or ring -- CUSTOM_SHELLS builders may need a new
convention. Low urgency; no bug, no user-visible gap. (umbrella: L-068)
[D.Feature-C: tag applied 2026-06-20 -- design-before-code]

#### [L-017 | #7] Tooltip rewiring globals() -> config fields
<!-- L:017 status:OPEN upd:2026-06-21 section:D.Feature-C flag: rice:2/3/50/3 -->
13 call sites in palomas_orrery.py (L9101-L9376) pass globals() to
build_shell_checkboxes() so it can look up tk.IntVar shell variables by NAME
(string). It works, but it is fragile: rename a variable and the lookup silently
misses, dropping a checkbox with no error -- invisible until someone notices the
missing toggle in the GUI. Recommended direction: build ONE explicit dict
{var_name: tk_var} (or a small registry/dataclass) at startup and pass it instead
of globals(), so a rename surfaces as a missing key, not a silent drop.
**Gap:** design decision first (dict vs dataclass vs registry), then thread the chosen object through all 13 call sites. Touches live UI wiring -- Mode-5 the GUI after. Design-before-code.
[D.Feature-C: tag applied 2026-06-20 -- design-before-code]

#### [L-046 | #N6] Studio encounter-generator -> preset-authoring capability (refactor + Artemis redo; coupled, two repos)
<!-- L:046 status:OPEN upd:2026-06-21 section:D.Feature-C flag: rice:3/3/75/3 -->
- **N6, reframed (Tony, 2026-06-21): the encounter generator is a NEW SKILL.**
  Beyond the original scope (refactor the Studio encounter-generator + redo the
  Artemis preset, coupled across the TWO repos), the larger intent is to
  generalize it into a PRESET-AUTHORING capability -- a reusable tool for producing
  many standard and special visualizations (flybys, close approaches, mission
  encounters, special framings) as gallery presets, not a one-off Artemis fix. N11
  rides. Design authority: ENCOUNTER_EXPORT_HANDOFF_v3.md (orrery repo); full
  verified specifics in git history / prior edition.
  `[per chain + @2f40d9d/@730b2bf verifications]`
**Gap:** design conversation first -- separate (1) the immediate refactor + Artemis redo from (2) the generalized preset-authoring vision; decide how much of (2) to scope now. Coupled across two repos. Design-before-code, Bucket C.

#### [L-067] measure_animation_html.py file-browser dialog (B5)
<!-- L:067 status:OPEN upd:2026-06-23 section:D.Feature-C flag: rice:1/1/75/1 -->
- **Add a tkinter file-browser dialog to measure_animation_html.py (B5).** Spun out
  of L-048 on close (2026-06-23): the animation core track 21/51 is DONE (v4.1 gate,
  L-004), and B5 was the lone remaining rider -- a convenience dialog
  (filedialog.askopenfilename) to pick the HTML to measure instead of a hardcoded
  path. Small, isolated tooling.
**Gap:** add filedialog.askopenfilename to measure_animation_html.py.
**Ref:** spun out of L-048 (closed 2026-06-23).

### D.Parked (Tony's explicit call) `[per chain]`

### D.Loose end to reconcile `[per chain; not re-verified]`

#### [L-051] Uranus pole-value prose inconsistency (Dec -15.10 vs stray -15.18)
<!-- L:051 status:OPEN upd:2026-06-21 section:D.LooseEnd flag: rice:1/2/50/1.5 -->
- **What it is.** Two different Uranus pole Declination values appear in prose:
  -15.10 (the load-bearing value actually used) and a stray -15.18 elsewhere.
  Reconcile to one (fix the stray) when next in that file.
- **Why the provenance scanner does NOT catch it (Tony's question).** The scanner
  flags a numeric token that LACKS a citation within its lookback window -- it
  checks for PRESENCE of a # Source, not AGREEMENT between two cited values. Both
  -15.10 and -15.18 likely sit within lookback of a citation, so each individually
  passes the "has a source" test; the scanner has no cross-value consistency check,
  so a contradiction between two separately-cited numbers slips through. A scanner
  BLIND SPOT, not a missed flag.
**Gap:** find both occurrences, confirm -15.10 is correct, fix the stray -15.18. Optional: log the scanner's no-consistency-check limitation as an enhancement candidate (fold into L-002/L-003, not its own item).

## E. AU-CONVENTION COMPLIANCE CLUSTER (standing convention; one sweep)

#### [L-052] AU-convention compliance sweep (GEO altitude hover missing AU; km+AU on all new hover)
<!-- L:052 status:OPEN upd:- section:E flag: rice:1/1/50/1 -->
- Inner-four bow-shock hover ("radii" only) `[verified @76c330e]`; GEO
  altitude hover missing AU `[per standing convention]`; confirm km+AU on
  any new hover at add time. (Session C's U+N bow-shock disclosure lines
  added no new numbers; existing km/AU values untouched.)

## F. CONSOLIDATION LOG (what each pass repaired)


- (June 7, v28 consolidation) RESTORED 2 leaked Movement-2 items + the v24
  sec5 batch; corrected the stale U3 "open"; UNIFIED the three animation
  records into 21/51; closed N13, N12; recorded Q2; moved Food Insecurity
  to a separate track; HEAD verifications. (Full detail: prior edition /
  git history.)
- (June 8) Recovered the N6 generator-refactor leak; recorded the two-repo
  coupling; Gallery section H stood up.
- (June 10) ANIMATION PASS 1: Phase 1 render-confirmed; Phase 2 delivered;
  PENDING June-8 items verified at HEAD and cleared; center-marker
  divergence root-caused (N3 + O5 + O6a = one disease); v27 axis/cone gap
  refined to non-center-only (O4); animate shell auto-scale found dead and
  annotated; new items from the O-log.
- (June 10, later) Phase 2 render-confirmed; Phase 3 GO (rebuild-universal
  directive); Session A delivered: the "one-site" wrapper claim CORRECTED
  by repo-wide grep (three sites); budget harness + gate 5(a) passed;
  grep -c chain-break lesson.
- (June 11, fix pass C2) v4 first run found 3 blockers; all root-caused
  with reproduction, not patched on guesses: the perihelion repro
  EXONERATED the engine math and convicted Plotly's frame-merge
  semantics (sticky visible); the doubling was two producers of one
  element (frame-1 block + engine); Mercury-centered was a coverage
  gap, not a trajectory bug (Tony's barycenter-class instinct pointed
  the way; the trigger differed). skip_elements threaded through the
  dispatch with a None-default regression test (HEAD-identical).
  Promoted: epoch-parser 'osc.' gap (D.Priority), <br> hovertext
  (D.Cosmetic), 3D arrow cameras (item 19).
- (June 11) Sessions B + C: engine delivered and conditionally confirmed
  (solar-system-scale visual gap identified as TOOLING -> item 19 with the
  go.Frame camera mechanism note); greyed-legend disclosure verified and
  accepted (supersedes the footnote; console notices demoted to dev
  diagnostics); B3-bonus barycenter bug root-caused (sentinel conflation:
  a fallback value is a CONTRACT) and fixed with
  suppression-over-fabrication; comet trace counts measured non-monotonic
  -> pad-to-max; capture-shim pattern adopted for the comet core (faithful
  by construction, hairy builder untouched); O13a spam fixed engine-side;
  scaling consolidated into item 19 per Tony's framing call (no separate
  track); section-G auto-scale and tier-decision questions CLOSED;
  provenance re-scan at d9460e2: Tier-1 = 0 held through the campaign.
- (June 14) Item 19.3 design session: SHA round trip verified (orrery 1288b51,
  gallery 2f40d9d); map-confirmed 4 scene sites (2 twins / 2 variants, prior
  3-site grep was stale); seam decision (a2) + Q2/Q3 settled; handoff drafted.
  No code. Divergence-audit seeded.

## G. OPEN QUESTIONS / TONY CALLS

#### [L-053] AU-convention sweep (section E): keep open, revisit
<!-- L:053 status:OPEN upd:2026-06-07 section:G flag: rice:3/1/50/2 -->
- AU-convention sweep (section E): KEEP OPEN, revisit (Tony, June 7).

#### [L-056] Phase 4 residuals: stale O2/O3 console wording; apsidal_markers em-dashes (MAPS per-frame wiring -> L-066)
<!-- L:056 status:OPEN upd:2026-06-23 section:G flag: rice:1/2/50/2 -->
- **Phase 4 residuals** (June 12): O2/O3 console notice wording is
  slightly stale when magnetosphere opt-in is ON (the blanket "not yet
  rendered" remains true for sphere shells; engine prints its own
  allocation lines) -- amend on next touch. apsidal_markers.py carries
  4 PRE-EXISTING em-dashes (platform-neutrality flag, not Phase 4's).
  MAPS per-frame wiring EXTRACTED to its own item L-066 (2026-06-23) -- it is real
  scoped work (a one-line gate removal), NOT "by design"; see L-066.
**Note (2026-06-17):** Mercury-centered auto-scale (O16) reads ~1 AU because
  get_animation_axis_range passes positions={} into calculate_axis_range_from_orbits;
  the non-Sun-center distance branch can't fire, so the Sun's heliocentric
  aphelion (~1.017 AU) is used as the fallback, giving a ~1.3 AU cube.
  Pre-existing; not introduced by the animation refactor. Workaround: use
  the orrery-side dtick/range field (item 19.3 Phase B) to override at
  generation time. Reopen as D.Priority only if the fallback causes
  confusion on other planet-centered animations (e.g. Jupiter-centered
  with Sun selected = ~5.5 AU, likely fine).
**Note (2026-06-23):** MAPS wiring split out to L-066. L-056 now holds only the two
non-visual residuals: O2/O3 console wording (one-line fix on next touch) and
apsidal_markers.py em-dashes (-> platform-neutrality, L-027). No Mode-5 needed here.

#### [L-137] Heliocentric -> solar barycentric coordinates -- decided against
<!-- L:137 status:PARKED upd:2026-08-25 section:G flag: rice:2/2/50/2 -->
- **Decision (Tony + Claude, discussed 4/16/26, pre-ledger note).**
  Switching the orrery's coordinate basis from heliocentric to
  solar-barycentric was discussed and judged unlikely to produce
  meaningful visual/educational results. Captured so it isn't
  re-proposed without the context of why it was set aside.
**Gap:** none -- parked by decision, not missing information. Reopen only
if a specific use case surfaces that heliocentric can't serve.
**Note (2026-08-25):** the use case this item's Gap names has
surfaced. The Sun HAS an ephemeris relative to the SSB (target 10,
origin @0) and the schema would take it -- Pluto and Charon are
already stored at `@9`. It does not help the Sun scene: the resolver
refuses any object whose stored centre differs from the scene's, and
the assembler is built never to transform between frames. So a
barycentric SOLAR SCENE is a real future artifact rather than a
coordinate-basis switch. Still PARKED; recorded so the reopening
condition is visible when that artifact is scheduled. See L-234.
**Ref:** to_do_ideas.md (pre-ledger, 4/16/26). 

#### [L-208] CRITICAL-gate tier audit + self-report -> visible-evidence pattern extension
<!-- L:208 status:OPEN upd:2026-08-18 section:G flag: rice:3/3/50/2 -->
- Raised in an Aug 18, 2026 conversation on reward-hacking research and
  the double-helix check-in mechanism -- a protocol self-audit, not an
  orrery bug. Two related questions, captured together because the
  second depends on the outcome of the first:
  (a) Part 3 states the critical tier must stay short -- "if everything
  is critical, nothing is." Eight resident CRITICAL gates currently
  qualify. AUDIT whether all eight still meet that bar, or whether one
  or more have drifted toward QUALITY/PRACTICE weight without being
  reclassified -- that drift would be invisible from inside the list
  itself.
  (b) Several CRITICAL gates (Register Rule; Verify Execution, Not
  Appearance; others) currently rely on Claude's own self-report that
  the check ran, rather than producing visible evidence that it did.
  Same session, Tony proposed a concrete fix for one instance -- an
  Executive Summary / Supporting Information header split for the
  Register Rule, so a missing header proves the check did not fire.
  OPEN QUESTION: does that same visible-evidence move generalize to
  the other self-report-reliant CRITICAL gates, or is Register Rule a
  special case?
**Gap:** design-before-protocol-amendment -- needs its own iterative
design conversation (options, tradeoffs, Tony's convergence) before any
Part 3 wording changes, same discipline as a code architecture
decision. Not urgent; the provenance chain (L-200 through L-207) stays
primary focus. Rides alongside it.
**Note:** RICE set directly by Tony at capture time (2026-08-18):
3/3/50/2 -- not a Claude proposal.
**Ref:** conversation Aug 18, 2026 (reward hacking / double-helix
check-in framing; no repo pull this session -- design-stage capture
only); PROJECT_INSTRUCTIONS v3.41, Part 2 (Register Rule) and Part 3
(Procedural Criticality; Skill Manifest CRITICAL gates).

#### [L-242] Two convention candidates awaiting a ruling (OPEN QUESTION)
<!-- L:242 status:OPEN upd:2026-08-25 section:G flag: rice:2/3/80/1 -->
- **Captured 2026-08-25 under capture-on-first-mention.** Both were
  raised as candidates by the sessions that hit them; neither has been
  ruled. Promotion is Tony's judgment, not the finder's. They are
  written here so they do not live only in a handoff -- which is what
  the first one is about.
- **(a) A handoff that opens ledger items should either carry the patch
  that writes them, or say plainly that it does not.** Home would be
  `ledger-and-session-records`. Origin, 2026-08-25: the handoff of that
  date drafted eight items and carried a Tony-action (do) reading "run
  `ledger_index.py` after the ledger patch" while no ledger patch was
  ever produced. The instruction read as completed work while pointing
  at nothing. That handoff passed every check a handoff has -- the
  anchor was there, the (do) list was there, the items were fully
  drafted -- and nothing in the document could reveal that the rows did
  not exist. It was caught by the next session reading the ledger at
  HEAD and finding it stopped at L-233. Same shape as the three
  instances in L-235: a record reporting complete without the thing it
  describes ever having run.
- **(b) A corrected patch built while its predecessor is already
  running, shipped as a follow-on fingerprinted against the PATCHED
  state rather than as a revert.** Home would be `safe-file-editing`.
  Origin, 2026-08-25: it worked, and both routes were proved
  byte-identical. Whether that makes it a convention or a one-off is the
  open question.
**Gap:** **Tony-action (decide)** on each. Either ruling that lands as a
skill bump runs the four-link chain -- SKILL.md, `skills_index.py`, a
protocol version-history entry, one commit (L-230).
- **Note:** RICE 2/3/80/1 -> 4.8 is Claude's proposed score.
**Ref:** HANDOFF 2026-08-25; L-235; L-230 (the four-link binding rule);
L-223 (a paste is an unverified transfer).

## H. GALLERY / STUDIO TRACK (website repo; low-activity)

**See L-169** for this section's repo-structure reference (converted
from long-standing unlabeled preamble, 2026-07-28).

#### [L-058] Open Studio items (May-5 handoff, checked @2f40d9d)
<!-- L:058 status:OPEN upd:2026-06-08 section:H flag: rice:3/3/50/3 -->
- **Open Studio items** (May-5 handoff; checked @2f40d9d where
  file-verifiable): encounter-export mission-type testing `[per handoff]`;
  camera capture NOT extracted `[verified]`; link-icon end-to-end test
  `[per handoff]`; content re-population through the Studio `[per handoff]`;
  gallery-card thumbnails ABSENT; About/Downloads/Contact pages ABSENT;
  og:image meta present (per-card previews unconfirmed).
- **Recently closed:** _enter_orrery_mode() DEFAULT_CONFIG reset
  `[verified @2f40d9d ~L4775]`; 'ongoing' status comment
  (spacecraft_encounters.py L60, verified).
**Linked:** coupled to L-046 (encounter generator -> preset-authoring skill).

#### [L-073] Gallery export-emits-JSON -- fold the manual json_converter run into Export
<!-- L:073 status:OPEN upd:2026-06-26 section:H flag: rice:2/2/80/2 -->
- Export produces only HTML today; Tony runs json_converter by hand before push.
  Wire Export to also emit the JSON via the REAL converter (same transform the
  preview now uses, proven in L-072). One open decision: card-only, or also stamp
  the gallery_metadata.json entry (per-file converter does the latter via
  auto_metadata). Sequence AFTER L-072 so it inherits a proven transform. Curation
  gate stays downstream (which JSON gets posted) -- the converter does not edit.

#### [L-074] Cull unused raw *_teaser.json in the gallery dir
<!-- L:074 status:OPEN upd:2026-06-26 section:H flag: rice:1/1/90/1 -->
- 27 raw `*_teaser.json` are tracked but NOT in gallery_metadata.json (pre-Studio
  intermediates; manifest serves `_gallery`/`_desktop` exports). Candidate
  cull/archive. Confirm none are needed as converter inputs before removing.

#### [L-104] Gallery Studio preset generator
<!-- L:104 status:OPEN upd:2026-07-13 section:H flag: rice:2/2/50/2 -->
- NET-NEW. Author an event window (object, center, {start,end,cadence}, label)
  in the orrery -- comet perihelion, NEO close approach, spacecraft flyby /
  gravity assist / landing -- export params via Gallery Studio; store as a gallery
  item. Feeds the interactive's event_link breadcrumb (closest-point marker ->
  gallery piece), NOT the interactive cache. Fine cadence (minute/hour, 30-60
  frames) lives in the preset. Upstream of the builder's preset slot (unpopulated
  in the first build; Apophis 2029 stays null).
- **Design refinement (2026-07-13, Phase 2 handoff session).** Two separate
  preset mechanisms exist in this project, confirmed distinct this session:
  L-046/L-104 (static Gallery Studio exhibits + event_link breadcrumb) vs. the
  Phase 1 vocabulary's live `preset_id` scene-spec expansion (OQ-4). This item
  is the former only -- OQ-4/closeup-shape do not gate it.
- **Mechanism, worked out concretely:** the precise epoch+position for a
  curated moment is already computable -- `close_approach_data.py`'s
  `get_close_approaches`/`fetch_position_at_approach` already does this
  (Apophis 2029 is its own standalone-test worked example). No new tool
  needed. Author the event_link entry as a byproduct of the same Gallery
  Studio session that builds the static exhibit (once L-046 lands), storing
  {object_slug, epoch, label, exhibit_link} in a small companion data file.
  Assembler checks this at render time; if the requested window includes the
  epoch, adds one marker (single-info-marker convention) with the link.
- **Comet case is free, no curation needed:** every comet already gets an
  automatic perihelion marker (per-orrery, generated for all comets). Coincide
  the event_link marker with the existing perihelion marker position --
  general pattern for every comet at once, verified via golden artifact 7
  (Halley) in the Phase 2 build sequence.
- **NEO/spacecraft need genuine curation:** no universal "closest approach"
  property is inherently noteworthy (most NEOs never warrant one); curated
  only where a human has actually built a preset for that object/event.
  Apophis 2029 is the concrete first case, gated on L-046's design
  conversation, not on anything in the Phase 2 assembler track.
**Gap unchanged:** still needs L-046's refactor to land first. Design is
resolved; building is not started.

#### [L-107] Gallery builder copy-with-provenance sync register
<!-- L:107 status:OPEN upd:2026-07-09 section:H flag: rice:1/2/90/0.5 -->
- **What.** tools/gallery_cache_builder.py is STANDALONE by design (no orrery
  import -- a cross-repo import would couple deployment and break the Actions
  future), so it COPIES hard-won fetch specifics from the orrery. The manifest
  promised this deliberate duplication would be ledgered; this is that register.
  It is the MANAGED exception to the parallel-pipeline anti-pattern: when any
  listed orrery source changes, re-copy into the builder and re-run the offline
  test (sync-on-change).
- **Register (orrery HEAD 4e2629c):**
  - utc_to_tdb -> orbit_data_manager.py:41
  - range-query fetch + '@'-center normalization -> orbit_data_manager.py:~672-690
  - refplane='ecliptic' on .vectors() -> spacecraft_encounters.py:632
  - elements get_col mapping + q-based km/AU detection -> orbit_data_manager.py:~1800-1878
  - fetch_solution_tp (vectors_async header TP=) -> osculating_cache_manager.py:459
  - resolve_tp hierarchy -- ADAPTED: builder is Path-2-only (no shared cache) +
    nightly re-resolve -> osculating_cache_manager.py:566
  - CENTER_SLUG_MAP -> export_orbit_cache.py:198-208; resolve_center_slug -> :212-223
  - _dt_to_jd / parse_osc_epoch_to_jd / _true_to_mean_anomaly_deg -> export_orbit_cache.py:~255-295
  - build_osculating_entry / write_position_file served schema -> export_orbit_cache.py:418-541
  - KM_PER_AU -> constants_new.py:47
**Tony:** copy-not-import is the honest form (Fable's standalone discipline);
this register is the sync ledger the manifest promised.
**Gap:** on any change to a listed orrery function, re-copy + re-run the offline
test. A periodic automated diff check is a possible follow-on (deferred).
**Ref:** GALLERY_BUILDER_MANIFEST v2 (S1, S3); GALLERY_BUILD_HANDOFF v0.1;
tools/gallery_cache_builder.py; L-098 (parent).

#### [L-111] Gallery builder Pass 5 -- operability + deferred hardening
<!-- L:111 status:OPEN upd:2026-07-27 section:W.Active flag: rice:2/2/50/2 -->
- **What.** Open items after Passes 1-4, captured from Tony's questions and the
  un-actioned remainder of both reviews. Full detail in GALLERY_BUILD_HANDOFF
  v0.1 "Open items and deferred work"; this is the tracked handle.
**Deployment model (REVISED 2026-07-27, supersedes the July 10 decision
below):** full automatic FETCH and PUSH -- Task Scheduler runs
`--nightly --commit` directly, no manual review step. Adopted after a
week of real testing (2 clean nights out of 3; the one failure diagnosed,
understood, and now guarded against by L-165's post-swap verification).
Trades the manual-review safety net for full hands-off operation --
deliberate, not an oversight. The gap-aware catch-up correctness issue
below remains open and is unrelated to this choice.

Original (superseded): automatic FETCH, manual PUSH -- Task Scheduler runs
the builder nightly WITHOUT --commit... Tony reads the summary and pushes
by hand. Kept commit authority with Tony; cited a2b7435 as a real incident
this caught.
- **Gap-aware catch-up (CORRECTNESS -- do before unattended).** The nightly fetches
  a FIXED trailing window `[today - freeze, today]` anchored to TODAY, so if the
  builder is dark longer than `freeze` (machine off, travel) the gap days are
  SILENTLY skipped. Fix: anchor the refresh window to the ARCHIVE's last date --
  `[last_archived_date - refine_overlap, today]` -- so a run fills whatever gap
  exists and self-heals an outage. The small backward `refine_overlap` only re-
  fetches recently-refined spacecraft points (planets/moons are stable); it is NOT
  a stopping point. Missed PUSHES are harmless (increments accumulate locally,
  commits queue, one push catches up); missed RUNS are the case this fixes.
  (Framing note, 2026-07-27: unattended scheduling is already live per the
  revision above. This gap was accepted as an open risk rather than fixed
  first -- tracked in L-165's succession-planning discussion, not resolved
  here.)
  (Framing note, 2026-07-27: the Q2 manual-review approach here was not
  adopted -- L-165's lighter automated post-swap guard was built instead.
  Q1, the --add-object backfill, remains open and unrelated.)  
- **Pass 5 (operability -- do before UNATTENDED scheduling).** (Q1) `--add-object
  <slug>` one-time backfill so a newly-added config object is onboarded without
  re-running the whole first-build. (Q2) a `_health.md` summary written EVERY run
  (status swapped/aborted, per-object result, warning list, COMMITS-PENDING-PUSH
  count, and an explicit PUSH / DO-NOT-PUSH verdict) -- NO email or phone
  notification (Tony's call: the summary file is enough). Likely-contamination
  sets the verdict to DO-NOT-PUSH rather than the builder refusing (push is manual).
  (Framing note, 2026-07-27: the Q2 manual-review approach here was not
  adopted -- L-165's lighter automated post-swap guard was built instead.
  Q1, the --add-object backfill, remains open and unrelated.)  
- **Deferred hardening.** N7 -- make date arithmetic UTC-ONLY (fetch
  epochs, date keys, and the 'today' anchor all in UTC) so DST never enters the
  data path; DST-immune and subsumes the 69 s Time(jd) boundary wobble. Schedule
  the job at a non-transition local time (~4 AM, clear of 1-3 AM local) so a
  spring gap does not skip the run and a fall repeat does not double-fire
  (double-fire is otherwise harmless: gap-aware catch-up over an already-current
  archive, atomic swap, N3 clean).
  N8 exact-today + date-on-point + stale flag; N10 read Astropy units over the
  q>10000 heuristic; guard-warning fetch-param payload; warnings_log into
  _health.json; N11 live-response fixtures + identity matrix.
- **Cleanup.** Remove dead `_replace_file`; reconcile guard outer-tier threshold
  (10x vs ~30x); source.epoch float-vs-string parity; scheduled-task working dir.
- **Gap.** The live-gate open dependencies (2P TP= header, Horizons pre-SPK
  clip/error, id_type/center identity matrix, elements units, epoch scale) are in
  TESTING_PROTOCOL.md and resolve at the first --dry-run, not here.
**Note:** GPT 5.5 produced the cross-check (L-110) that surfaced Q2's teeth; the
render (Mode 5) remains the authority over both AI reviewers.
**Ref:** GALLERY_BUILD_HANDOFF v0.1 (open-items section); TESTING_PROTOCOL.md; L-109; L-110; L-098 (parent).

#### [L-132] Studio landscape preset: links icon covers fly-to buttons
<!-- L:132 status:OPEN upd:2026-07-17 section:H flag: rice:2/2/50/2 -->
- **Bug (Tony, 4/17/26, pre-ledger note).** In Gallery Studio's landscape
  preset, the links icon overlaps the fly-to navigation buttons -- layout
  collision, needs repositioning.
**Gap:** not reproduced/scoped this session -- verify still present at
current HEAD (Studio layout has moved since 4/17) before fixing.
**Ref:** to_do_ideas.md (pre-ledger, 4/17/26).

#### [L-167] Artifact-1 field notes -- orrery-coding-conventions still missing three entries
<!-- L:167 status:OPEN upd:2026-07-29 section:H flag: rice:1/2/95/0.5 -->
- **What.** Opus 4.8's artifact-1 as-built (PHASE2_ARTIFACT1_AS_BUILT.md S10)
  recommended three rendering gotchas land in orrery-coding-conventions.
  Checked directly: skill is still at v1.1 (cut 2026-07-12), none present.
- **The three notes:**
  1. `aspectmode: "cube"` (equal axis ranges) is required for solar-system
     scenes -- `aspectmode: "data"` collapses a near-planar orbit into an
     invisible sliver + axis line. The orrery's own `build_scene` already
     does this; the web assembler had to rediscover it the hard way on
     Earth alone.
  2. `scatter3d` traces have no `dash` line-style attribute (2D-only in
     Plotly). Distinguish mean vs. osculating orbit traces by line width,
     not dash.
  3. Text/label traces default to black -- invisible against the dark
     theme. Set `textfont.color` explicitly on every label trace.
**Gap:** add these three as field notes, bump skill to v1.2, re-cut/SHA-stamp.
Small, no urgency, but cheap to repeat on artifacts 2-7 if never fixed.
**Ref:** PHASE2_ARTIFACT1_AS_BUILT.md S10/S12; orrery-coding-conventions
skill (current v1.1).

## O. OBJECT CANDIDATES TRACK

Standing wishlist for new selectable objects and gallery/studio presets --
add entries as they occur to Tony, retag to O.Done as they ship. Each entry
is its own L-handle (a "brief item"), scored rice:2/2/C/E, with C/E judged
per item; 2/2/75/1 is the default starting point (Tony's call, 2026-07-17).

### O.Comets

### O.Asteroids

#### [L-139] Pallas (candidate asteroid)
<!-- L:139 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- ~204,000 x10^18 kg (~7% of belt mass) -- has a very tilted (inclined)
  orbit. Not yet in celestial_objects.py [verified @6064728b].
**Gap:** look up Horizons small-body ID, pick symbol/color, add entry
(pattern: existing Ceres/Vesta entries).
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

#### [L-140] Hygiea (candidate asteroid)
<!-- L:140 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- ~86,000 x10^18 kg (~3% of belt mass) -- largest carbon-rich (C-type)
  asteroid. Not yet in celestial_objects.py.
**Gap:** look up Horizons small-body ID, pick symbol/color, add entry.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

#### [L-141] Interamnia (candidate asteroid)
<!-- L:141 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- Large, but lower density than its size suggests. Mass/rank not in the
  source note -- look up alongside the ID. Not yet in celestial_objects.py.
**Gap:** source mass/rank, look up Horizons ID, add entry.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

#### [L-142] Davida (candidate asteroid)
<!-- L:142 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- C-type, very dark. Mass/rank not in the source note. Not yet in
  celestial_objects.py.
**Gap:** source mass/rank, look up Horizons ID, add entry.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

#### [L-143] Sylvia (candidate asteroid)
<!-- L:143 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- Notable for having two moons (Romulus and Remus) -- a good storytelling
  hook. Mass/rank not in the source note. Not yet in celestial_objects.py.
**Gap:** source mass/rank, look up Horizons ID, add entry.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

#### [L-144] Eunomia (candidate asteroid)
<!-- L:144 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- S-type, stony. Mass/rank not in the source note. Not yet in
  celestial_objects.py.
**Gap:** source mass/rank, look up Horizons ID, add entry.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

#### [L-145] Euphrosyne (candidate asteroid)
<!-- L:145 status:OPEN upd:2026-07-17 section:O.Asteroids flag: rice:2/2/75/1 -->
- C-type. Mass/rank not in the source note. Not yet in celestial_objects.py.
**Gap:** source mass/rank, look up Horizons ID, add entry.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

### O.Moons

### O.Exoplanets

#### [L-146] HR 8799 (candidate exoplanet system)
<!-- L:146 status:OPEN upd:2026-07-17 section:O.Exoplanets flag: rice:2/2/75/1 -->
- Four confirmed super-Jupiters orbiting a single star -- a strong
  storytelling candidate (multi-planet system, directly imaged). Not yet
  in celestial_objects.py [verified @6064728b]; would be host-star + 4
  planet entries, mirroring the existing TRAPPIST-1 pattern (~L1158+:
  id_type='host_star'/'exoplanet', system_id, mission_url).
**Gap:** more entries than a single asteroid (5 vs. 1) -- still likely
one session given the established pattern to copy; flag if it runs long.
**Ref:** to_do_ideas.md (pre-ledger); split from L-138.

### O.Spacecraft

### O.Presets

### O.Done -- closed items, kept with the track

## W. WEB PUBLICATION TRACK

Governing document: `documentation/MASTER_PLAN_WEB_PUBLICATION.md`.
Architecture, phasing, and rationale live there; this section tracks work items
and status. Cross-references: L-026 (CRLF, companion to L-087), L-046 (presets),
L-068 (pipeline residuals), L-071 (Earth storytelling), L-074 (gallery culling),
L-083 (Plotly 6 / Kaleido -- desktop only, not web).

### W.Prep -- before Phase 0

#### [L-086] Attribution / credits page
<!-- L:086 status:PROPOSED upd:2026-07-03 section:W.Prep flag: rice:2/2/70/1 -->
- **What.** One page (site + repo), one entry per data source, four fields each:
  what is used, where it appears in the project, the attribution string in the
  form the provider requires, and the license/redistribution terms with a link.
- **Source list (from repo evidence at HEAD):** JPL Horizons, JPL SBDB/CAD,
  Copernicus CDS / ERA5 / ERA5T, NOAA Coral Reef Watch, IPC and FEWS NET, HDX,
  OCHA FTS, SIMBAD (CDS), Gaia (ESA), Hipparcos, NSIDC, Mauna Loa CO2 (NOAA
  GML/Scripps), HOT program.
- **Provider-required citation strings** (especially Gaia/ESA, CDS/SIMBAD,
  Copernicus) must be fetched at build time, not recalled.
- **Two constraints on hosting/distribution:** Copernicus licence terms and IPC
  terms of use are the most likely to constrain a hosted path. Neither kills any
  option; both need verification before wide release.
**Gap:** fetch each provider's required citation format; draft page; verify
redistribution terms for Copernicus and IPC. Gates any wide release including
the Phase 0 pilot if publicly reachable.
**Ref:** Fable 5 survey (Front 2), master plan S6.

### W.Active -- current phase

#### [L-079] Shared assembler architecture (keystone -- redefined)
<!-- L:079 status:OPEN upd:2026-07-07 section:W.Active flag: rice:3/3/50/3 -->
- **Redefined from:** "Headless scene core -- decouple scene construction from
  Tkinter" (Fable 5 survey, July 2 2026).
- **Redefined to:** Build a shared assembler per domain. Both GUIs (tkinter
  desktop, web) are thin harvesters feeding the assembler. The assembler is new
  code written with the desktop orchestration as recipe reference. Original code
  archived for reference or reconstruction.
- **Four domains:** solar system (main build), stars, orbital parameters
  (educational showcase), Earth system (mixed KMZ + Plotly).
- **Phasing (governed by master plan v10):**
  Phase 0: gallery integration test [x] DONE (L-088, July 6, 2026).
  Phase 1a: shared spec skeleton + solar system vocabulary [x] DONE (L-089).
  Phase 1b: data serving pipeline (L-098) -- design converged v0.3.
  Phase 2: solar system assembler + desktop migration tail.
  Phase 3: star assembler + cache. Phase 4: hybrid (exoplanets + Sgr A*).
  Phase 5: Earth system.
- **Per-domain migration tails:** desktop migrates onto each assembler right
  after it validates -- not a single late migration. Delta-log discipline: any
  desktop orchestration change during the build gets a ledger tag
  "assembler-must-inherit."
- **Key decisions (settled):** site never fetches Horizons; three-tier cache all
  offline; GUI declares the envelope; web GUI is a fork not a replacement; one
  assembler per domain; architecture is S3/M3; assemblers read cache through
  index abstraction from day one; Phase 2 gate is scene equivalence not identical
  output; animation presets as curated tier-2 exports; scene spec is JSON-
  serializable from day one; animation/static consolidation verified (one
  assembler replaces both orchestrators).
- **Key decision (settled):** server (Dash) vs serverless (Pyodide) -- Phase 0
  resolved this: Pyodide, proven July 6, 2026 (L-088).
- **Key decision (settled):** architecture A (numpy + JS figure builder) vs B'
  (shared engines via plotly in Pyodide, slim self-hosted wheel). B' measured
  at 2.1-3.3 s on iPhone WiFi (July 6, 2026). Two-tier model: frozen A
  exhibits + data-backed B' exhibits.
- **Progress:** Phase 0 closed (L-088, July 6). Phase 1a vocabulary delivered
  (L-089, Fable 5, July 4). A/B fork resolved: B'. Phase 1b (L-098) built and
  CLOSED (July 12). Phase 2 design closed: handoff v0.1 -> v0.3, competitive
  manifest cross-check (Fable + GPT), synthesis v1 -> v2, both second-pass
  reviewed. Artifact 1 (Earth alone) built and Mode-5 confirmed (Opus 4.8,
  July 14). Artifacts 2-7 in progress. Master plan at v14.
**Gap:** the master plan IS the gap document. Current phase: Phase 2.
**Ref:** MASTER_PLAN_INTERACTIVE_GALLERY.md v10; PHASE1_SCENE_SPEC_VOCABULARY.md;
DATA_SERVING_BROAD_ANALYSIS.md; PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md v0.3;
Fable 5 survey + L-079 deep dive; Opus 4.8 convergence handoff + reviews;
Opus 4.6 + Tony convergence (July 3, 6, 7); Fable 5 vocabulary session (July 4);
Fable 5 design review (July 7).

#### [L-080] Characterization harness (scene equivalence gate)
<!-- L:080 status:OPEN upd:2026-07-14 section:W.Active flag: rice:1/2/80/1 -->
- **What.** A harness that captures a golden semantic fingerprint per scene and
  gates every phase of the web publication initiative: "scene equivalence
  confirmed, render agrees" before each step. NOW LIVE and co-evolving (manifest
  v2 S8 / handoff v0.3 S7): built as `gallery/assembler/harness/fingerprint.py`,
  seeded at artifact 1 rather than front-loaded.
- **Scene equivalence** (not identical output): same object set, positions match
  within tolerance, display conventions honored (single-info-marker, AU in hover,
  marker symbols), plus Mode 5 (Tony's visual judgment). Trace ordering, naming,
  and layout details may legitimately differ.
- **Fingerprint is semantic, not full Plotly JSON** (both manifests + both
  second-pass reviews agreed). Fields: artifact_id, scene_spec_hash,
  cache_snapshot_id, resolved date/center/frame, object_slugs, trace_role_counts,
  feature_keys (the dispatch decision, not the JS-rendered trace), legend_groups,
  coordinate_bounds, position_samples vs tolerance, warnings. Built from the
  frozen AssemblyContext AND the rendered output, so both logical and visual
  regressions are catchable.
- **First golden LOCKED:** `artifact_1_earth_alone.json`, scene_spec_hash
  `abbd01094852b57f`. Reproduces identically in CPython and in-browser (Pyodide)
  -- it characterizes the scene, not the machine. Artifact 1 (Earth alone) Mode 5
  gate passed 2026-07-14 [render-gated].
- **Position tolerance** defaults to 0.001 (0.1%); it is a parameter in
  fingerprint.py, not a hardcoded constant -- tune against real data (manifest S9.1).
**Tony:** minor adjustments to the artifact-1 golden are still expected (title
text, theme, styling). Restyles that do NOT touch trace roles/bounds/samples
leave `abbd01094852b57f` unchanged (free). Any change that DOES move the
fingerprint needs a deliberate golden regen, with the reason recorded here and in
the commit message (manifest v2 S8).
**Gap:** co-evolve the golden set through artifacts 2-7 (each confirmed artifact
hands the harness its next fingerprint); fold in the mainloop-suppression fixture
and the three original test files; concretize L-089's criteria against the
now-real fingerprint. Additive; no production modules edited.
**Ref:** `gallery/assembler/harness/fingerprint.py`,
`gallery/assembler/harness/golden/artifact_1_earth_alone.json`,
`gallery/assembler/tests/test_artifact1_earth.py` [current gallery HEAD];
manifest v2 S8; handoff v0.3 S7; L-089 (criteria); L-098 (Phase 1b);
Fable 5 survey (L-080 proposal); master plan S5/S6.

#### [L-089] Scene-spec shared skeleton + solar system vocabulary (Phase 1)
<!-- L:089 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:3/3/50/3 -->
- **What.** Design in conversation, not code.
  (a) The shared spec skeleton -- what every spec has across all domains: domain
  tag, content type, display options.
  (b) The solar system vocabulary: objects, center, dates, display options,
  content type (static/animation).
  (c) The coverage index interface for the solar system domain.
  (d) Scene equivalence criteria -- the concrete definition that shapes L-080's
  golden artifacts.
- **Other domain vocabularies are designed just-in-time** at the head of their
  own phases, informed by lessons learned here.
- **Decide:** is the spec serializable from day one? (Presets, shareable scenes,
  CI hang on this.)
- **Gate check:** confirm no shared-layer seams beyond the two named in S2.
**Gap:** design session(s). Gate: vocabulary document, index interface spec, and
equivalence criteria reviewed and stable before any assembler build.
**Ref:** Fable 5 L-079 deep dive (S2 vocabulary); master plan S5 Phase 1.

#### [L-090] Star cache inventory + wire format decision
<!-- L:090 status:PROPOSED upd:2026-07-03 section:W.Active flag: rice:1/1/50/1 -->
- **What.** The star cache (PKL files under `star_data/`) is gitignored, exceeds
  GitHub size limits, and is distributed via Releases for the desktop. It was
  built carefully from Gaia + Hipparcos with deduplication boundaries, within
  SIMBAD rate limits. Coverage: 101 light-years, apparent magnitude 9. Cannot be
  casually regenerated.
- **Inventory needed:** `du -sh star_data/` on Tony's machine -- total size and
  per-file sizes. This determines where the star cache fits in the headroom
  budget and whether it can ship via Pages.
- **Wire format decision:** pickle is Python-version-coupled (fine for a Dash
  server, brittle for Pyodide, opaque to non-Python consumers). Convert to
  Parquet or JSON at cache-build time is the standard escape. Tied to the
  server-vs-serverless decision (L-088).
**Gap:** Tony runs `du -sh star_data/` and shares the inventory. Wire format
decision follows L-088 (Phase 0).
**Ref:** Fable 5 review of v4 (finding 1); master plan S4b.

#### [L-119] event_link hardcoded None in the builder (F2, gates artifact 7)
<!-- L:119 status:OPEN upd:2026-07-15 section:W.Active flag: rice:2/2/90/1 -->
- **What.** `derive_served` (line ~727) hardcodes `'event_link': None` for
  every object; `objects_config.json` carries this field on NONE of the 12
  objects -- confirmed by direct inspection, not inferred (a bare
  `obj.get('event_link')` check would return `None` identically whether the
  key is missing or present-and-null -- the weaker check the original
  manifest draft used, self-corrected in synthesis v2: verifying a field's
  VALUE first requires confirming the field's PRESENCE).
- **Two-step fix (manifest S4 F2).** (1) add `event_link` to the
  objects_config.json schema (Halley first, per L-104's comet-perihelion
  coincidence pattern); (2) wire the builder to pass `obj.get('event_link')`
  through instead of hardcoding `None`; (3) Layer-1 offline-test updates for
  the new field.
- **Verified live 2026-07-15** [verified @953c650e]: `event_link` is `None`
  for all 11 served objects.
**Tony:** RICE proposed 2/2/90/1 (gates one artifact only; small, well-verified
fix) -- yours to finalize.
**Gap:** sequence after L-118/F1 lands (same builder file, same layered gate)
-- add the schema field, wire the pass-through, update Layer 1, offline suite
from a clean checkout as acceptance. Feeds L-104 (event_link breadcrumb
authoring), which is gated on L-046, not on this.
**Ref:** gallery `tools/gallery_cache_builder.py` (`derive_served` ~line 727);
`data/objects_config.json`; PHASE2_SYNTHESIS_MANIFEST_v2.md S4; L-098 (parent);
L-104 (downstream consumer).

#### [L-121] Slim plotly wheel not deployed anywhere (F4, ships-nothing gate)
<!-- L:121 status:OPEN upd:2026-07-15 section:W.Active flag: rice:3/3/75/3 -->
- **What.** The B' architecture (two-tier: frozen-A exhibits + data-backed B'
  exhibits, L-088) calls for a slim self-hosted plotly wheel (~3.9 MB); none is
  deployed anywhere in the gallery repo tree -- confirmed via full tree
  listing. The current dev bridge (`solar_system_earth_test2.html`, artifact 1)
  uses `micropip.install` against the live Pyodide CDN, which is a dev
  convenience, not production architecture.
- **Gates:** shipping ANY golden artifact publicly. Artifact 1 is currently
  served only from Tony's own machine (`python -m http.server`), not GitHub
  Pages -- deliberately, per the as-built (S7).
- **Ships alongside, not separately:** L-086 (attribution/credit line) is
  already its own ledger item (PROPOSED, rice:2/2/70/1) -- no new item needed
  for that half.
**Tony:** RICE proposed 3/3/75/3 (blocks all public deployment, but larger and
less-verified effort than L-118/L-119/L-120 -- deploying and wiring the wheel
is real work, not a config change) -- yours to finalize.
**Gap:** deploy the slim plotly wheel into the gallery repo tree; wire the
(eventually-named) real page to use it instead of CDN plotly.js; confirm
L-086's attribution line carries over to the new page. Downstream of artifacts
1-7 closing -- this is the ship gate, not a build-order blocker.
**Ref:** PHASE2_SYNTHESIS_MANIFEST_v2.md S4; PHASE2_ARTIFACT1_AS_BUILT.md S7;
L-088 (B' decision); L-086 (attribution, companion); L-098 (parent).

#### [L-122] Stray data/solar-system.prev_old/ committed to the repo (F6, non-blocking)
<!-- L:122 status:OPEN upd:2026-07-15 section:W.Active flag: rice:1/1/95/0.5 -->
- **What.** `data/solar-system.prev_old/` is committed to the gallery repo --
  looks like a manual-rename artifact predating the atomic-swap `.prev`
  convention. Confirmed present [verified @953c650e]. Non-blocking; delete at
  convenience.
**Tony:** RICE proposed 1/1/95/0.5 -- yours to finalize.
**Gap:** confirm nothing references it (grep), then delete + commit.
**Ref:** PHASE2_SYNTHESIS_MANIFEST_v2.md S4 (F6); L-098 (parent).

#### [L-123] Object info card -- serve info_dictionary.py as JSON, click-to-open (rides with F1)
<!-- L:123 status:OPEN upd:2026-07-15 section:W.Active flag: rice:2/2/90/2 -->
- **What.** Deferred from the artifact-1 build session (per
  PHASE2_ARTIFACT1_AS_BUILT.md S9/S12): clicking an object marker should
  open the gallery's existing "i" encyclopedia card, populated with that
  object's entry from `info_dictionary.py`'s `INFO` dict (2245 lines,
  keyed by object name, e.g. `'Earth'`, provenance-audited April 2026).
  No ledger item existed for this until now, per the as-built's own
  instruction to log one "when F1 opens."
- **Mechanism (as-built S9/S12, unchanged).** Serve the relevant `INFO`
  entries as JSON -- same serve-data/render-JS pattern the builder already
  uses for position/coverage data, extended to carry text content too. A
  Plotly click handler on the object marker then opens the gallery's
  existing "i" card UI with that JSON payload -- no new UI, reusing what
  `gallery_studio.py`'s encyclopedia card already renders.
- **Why it rides with F1, not before it.** F1 is what teaches
  `derive_served` to serve richer per-object JSON beyond bare position
  data; extending that same pipeline to also carry `INFO` text is a small
  incremental addition once F1's plumbing exists, not a separate serving
  mechanism. Building this before F1 would mean building (and later
  discarding) a one-off serving path.
**Tony:** RICE proposed 2/2/90/2 (meaningful gallery feature -- generalizes
across all 12 objects, not just Earth; mechanism is precisely scoped, no
design ambiguity; effort is two sessions -- serving text content plus
wiring the click handler and card population) -- yours to finalize.
**Gap:** sequence after L-118/F1's serving-pipeline change lands: (1)
extend `derive_served` (or a sibling served-data step) to include each
object's `INFO` entry; (2) wire a Plotly click handler on object markers
in the assembler's JS layer; (3) route the click payload into the gallery
Studio's existing "i" card renderer; (4) Layer-1 offline-test coverage
for the new served field.
**Ref:** `info_dictionary.py` (`INFO` dict); PHASE2_ARTIFACT1_AS_BUILT.md
S9 (info card, deferred) and S12 (ledger recommendations); L-118 (F1,
shared serving pipeline); L-098 (parent, Phase 1b).

#### [L-150] Multi-orbit trust model for near-equal-mass binaries (Pluto/Charon and future onboards)
<!-- L:150 status:OPEN upd:2026-07-20 section:W.Active flag: rice:2/3/75/2 -->
- **Decided (Tony, 2026-07-20), during L-149 discussion:** when a served body is a genuine
  near-equal-mass binary -- barycenter falls OUTSIDE the primary, per the project's existing
  barycenter rule -- it needs TWO served orbits, not one: heliocentric (whole-system views)
  and barycenter-relative (close-up views), each trust-measured, each voting only in whatever
  served_window governs its own scale of view. Ordinary planet-moon systems (barycenter
  inside the primary -- Earth/Moon, Jupiter/any moon) are NOT this case and keep single-orbit
  representation; the Moon's existing parent-relative orbit already IS its complete picture.
- **Candidates discussed tonight -- not exhaustive; the code is the reference, not this list:**
  - Pluto/Charon -- barycentric already served (~6.4-day mutual period); heliocentric not
    served anywhere yet. Ties to the still-open "Pluto/Charon two-view" golden artifact.
  - Orcus/Vanth -- not yet onboarded. Horizons IDs confirmed live: 20090482 (barycenter),
    920090482 (Orcus), 120090482 (Vanth).
  - Patroclus/Menoetius -- not yet onboarded. Horizons IDs confirmed live: 20000617
    (barycenter), 920000617 (Patroclus), 120000617 (Menoetius). Menoetius ~22% of system
    mass, ~680 km separation -> barycenter ~150 km from Patroclus's ~57 km-radius center,
    clearly clear of the surface. Caveat: Patroclus is a Jupiter Trojan (L5 libration), so
    its heliocentric orbit isn't a clean two-body case either -- measure its real trust
    number, don't assume it's clean by analogy to Pluto. Also a Lucy flyby target (2033).
- **Depends on:** the actual gap this rides on -- trust/served_window is keyed per OBJECT
  today (one orbit per slug); needs to be keyed per ORBIT (object + center), since one body
  can have two served orbits with unrelated accuracy characteristics. This entry records
  WHICH objects need that and WHY, so it doesn't get re-derived from scratch later.
**Gap:** design the per-(object,center) trust schema; decide how a scene mixing a
whole-system view and a close-up binary view should compute served_window (resolver.py
checks one global bound regardless of scene composition -- same limitation noted under L-149).
**Ref:** L-149 (sibling, surfaced during its design discussion); objects_config.json
(pluto/charon, barycentric-only today); "Pluto/Charon two-view" golden artifact.

#### [L-155] Cross-repo constants/geometry pinning checks -- built INTO provenance_scanner.py, not a standalone script
<!-- L:155 status:PENDING-GATE upd:2026-07-27 section:W.Active flag: rice:3/4/75/2 -->
- **What.** Pinning-test logic ("did this specific value drift," binary
  asserts -- the `test_constants_provenance.py` pattern, not the open-ended
  scanner pattern) that reads `objects_config.json`'s `features` values in
  the gallery repo and asserts each equals its named source in the orrery:
  `CENTER_BODY_RADII[x]` for physical radius, the specific dict literal in
  `earth/jupiter/saturn_visualization_shells.py` for ring/belt/atmosphere
  geometry.
- **Design (settled, per `DESIGN_HANDOFF_provenance_scoring_and_pinning.md`
  D6, confirmed on review D6d):** lives inside `provenance_scanner.py`'s own
  run via relative path (`../tonyquintanilla.github.io/...`) -- no separate
  script, no network. Absorbs `test_constants_provenance.py`'s existing
  logic too, one pinning mechanism not two. Fails loud: nonzero exit code
  on any pinning failure (the only hard exit-code gate in the whole
  cluster -- see L-156's D7 for why Tier-1 never gets one).
- **Explicitly out of scope:** `coverage_index.json` / `feature_configs.json`
  (gallery-cache-builder's own test suite's job); anything JS-side.
- **Gated on L-156** (scoring must be correct first) **and effectively on
  L-162** (pinning against 17 named constants -- Planet 9 excluded entirely,
  so zero dict-path lookups remain, not 15 -- worth L-162 landing first per
  its own note, though not a hard blocker).
- **Confirmed 2026-07-27 (Sonnet 5, live HEAD):** nothing built yet --
  `provenance_scanner.py` has zero occurrences of `run_pinning_checks` or
  `PINNING_MAP`.
**Gap:** finalize the explicit key-path mapping (gallery config key ->
orrery source location) as a table, not name-matching; design where this
lives inside `provenance_scanner.py` (new function alongside
`find_cross_file_issues`); build (Opus 5, Phase 3 per the amended design)
-- D3 itself is closed (see L-156), so what actually gates this now is
L-156's Phases 1-2 landing in code, not any further calibration round.
**Ref:** `test_constants_provenance.py` (direct precedent, including its
motivating bug: `close_approach_data.py`'s stale `CENTER_BODY_RADII` copy);
`provenance_scanner.py` `main()`; `constants_new.py`; `data/objects_config.json`;
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`; L-154; L-156; L-157; L-160; L-162.

---

#### [L-156] Provenance scanner scoring model fix -- criticality (category-based) + vulnerability recalibration + comprehensive sweep
<!-- L:156 status:OPEN upd:2026-08-02 section:W.Active flag: rice:5/4/80/3 -->

**What.** `provenance_scanner.py`'s scoring mis-prioritized the data this
cluster depends on: foundational constants (`SUN_RADIUS_KM`,
`KM_PER_AU`, `CENTER_BODY_RADII`) scored low because criticality was
resolved by direct-import-count, so a constant consumed indirectly (via a
derived dict) scored as if barely used.

**Scanner state at HEAD (post-Phase 2 Piece 1, `373c6d8`):** Tier 1
210, Tier 2 605, Tier 3 62, Tier 4 2, total 879 across 117 files
(+1: `test_cross_checked.py`). 879 conserved across Phase 2 Piece 1 --
zero findings moved. The V_CROSS_CHECKED (V2) recognition mechanism is
live but has zero population (no annotations written yet).

**Phase 1 measured arc (the instrument got honest):** Tier 1
145 -> 156 (1a) -> 156 (1b) -> 133 (1c) -> 132 (L-174) -> 171 (1d/1e/1f)
-> 210 (D8.5). The first half (145 -> 132) fixed false positives --
correctly-sourced claims scored as unsourced. The second half
(132 -> 210) fixed false negatives -- unsourced claims scored as sourced,
whether by a blind spot (temperature recognition, +61), numeric
coincidence (Option A, +23), or a marker meaning the opposite of what it
was credited for (staleness, +16). The number went up because the
instrument got honest.

### Decided constraints (design handoff + design review + Tony)

These are settled. Future builds work within them.

**Criticality.** Two categories: MEASURED (C=5) and RELATIONAL (C=4). Not
consumer-count-based. Ring geometry in MEASURED (Tony: "the rings are
better defined"). Orbital period and radius share the top tier (Tony:
"these are fundamental data"). Explicit `undetermined` sentinel for
unclassifiable items, with its own banner.

**Role-veto amendment (ratified 2026-07-29).** Role overrides name match
when the module's functional role is non-narrative. Without it,
`HUB_THRESHOLD`, `MAX_DATA_AGE_DAYS`, and
`PERFRAME_INDICATOR_RADIUS_FACTOR` all scored MEASURED through generic
stems.

**Vulnerability ladder (D3, decided 2026-07-27).** Four rungs via
three-AI calibration (Gemini 3.1 Pro, GPT 5.5, Fable 5), Sonnet 5
synthesis. V1 FETCHED (live pipeline). V2 CROSS-CHECKED (never auto-promotable to V1; requires source
evidence AND two distinct checker annotations via competitive pattern;
see provenance-discipline v1.4). V3 SOURCED (cited but unchecked, merged with stale
per Tony). V4 RECALLED (no citation). Derived values inherit weakest
input's rung once derivation logic clears one cross-check; a hardcoded
literal inherits nothing (plain V3).

**Tier-1 exit.** Permanent banner, never auto-exit gate, at any threshold
(D7, design review 3c, Tony confirmed). The only hard exit-code gate is
L-155's pinning checks (Phase 3). Errata:
`documentation/HANDOFF_phase1_1d_to_1f.md` at HEAD still describes a
deferred exit-gate flip -- this is wrong; superseded by the design review
and `AS_BUILT_L156_phase1d_e_f.md`.

**Tier labels.** Tier 1 keeps "FIX NOW" (action directive, not status
claim -- Tony accepted). Tiers 2/3/4 neutral score-band names: REVIEW,
LOW PRIORITY, LOWEST PRIORITY.

**Block inheritance.** Strict containment, narrowest block wins (Tony
confirmed via 1c build). No outward fallback -- if a block is uncited,
strings inside it stay uncited even if a parent block is cited. This
keeps L-173's findings visible.

**No Shadow Constants [CRITICAL].** provenance-discipline v1.3. Local
copies of `constants_new.py` values must be deleted and replaced with
proper imports. Never cite-to-clear a structural problem.

### Phase 1 build history (1a-1f: COMPLETE)

**1a (2026-07-29).** Landed D1 (MEASURED/RELATIONAL), D2 (`undetermined`
sentinel), D3 (V-ladder scoring), D8.3 (magnetosphere vocabulary), D8.4
(comet un-grandfathering), role-veto amendment. Tier 1 145 -> 156 (growth
is correct -- raising criticality promotes previously-buried uncited
facts). 5 undetermined. 781 total.

**1b (2026-07-29).** V-ladder scoring applied across all findings. Tier 1
156 (unchanged -- invariant held). Tier 2 181 -> 563, Tier 3 430 -> 60,
Tier 4 14 -> 2. 781 conserved.

**1c (2026-07-30).** Citation-block inheritance via AST walk
(`build_citation_block_table()`, `resolve_block_citation()`). Tier 1
156 -> 133. 23 shell_configs.py findings moved Tier 1 -> Tier 2 (21
SHELL_CONFIGS, 2 CUSTOM_SHELLS). 18 genuinely uncited findings left
untouched (tracked as L-173). Design departure: strict containment chosen
over narrowest-cited-containing, making L-173 findings visible by rule
rather than by accident of the data.

**L-174 (1c consequence, 2026-07-30).** Citations pitched one block too
far out for the resolver to see (ring_params line 959). Fixed by
repeating citation at entry level. Tier 1 133 -> 132. Permanent diagnostic
added (`SHADOWED_STRINGS`, `DEEP_CITATIONS`).

**1d (2026-07-31, Opus 5).** Three pieces:
- **Piece 1 (shadow-constant detector):** built as dedicated
  `scan_shadow_constants()` + `build_cited_constant_names()`, diverging
  from the predesign's Option A amendment. Three measured reasons: Option A
  only inspects display strings (shadow constants are function-local
  assignments the scanner never extracts); amending it would demote 9
  unrelated findings toward Tier 1; value-only matching gives 77 hits vs
  2 for name+value. Option A untouched; D8.5 still open.
- **Piece 2 (citation-form recognition, Gap item 7):** author-year
  parenthetical pattern added to SOURCE_PATTERNS, both `(Author et al.,
  YYYY)` and `(Author et al.)` forms. Measured: 13 findings Tier 1 ->
  Tier 2, population conserved.
- **Piece 3 (temperature units, L-078(d)):** temperature alternatives
  added to NUMERIC_CLAIM_RE. Tier 1 +61 (96 total new findings). Largest
  tier-moving change in Phase 1. All real uncited temperature claims in
  climate modules. Tracked as L-175.

**1e (2026-07-31, Opus 5).** Tier-1 banner (bordered, informational, no
exit code). Tier labels neutralized (2/3/4); Tier 1 keeps "FIX NOW".
Code carries a comment naming design review 3c and the superseded
document.

**1f (2026-07-31, Opus 5).** Shadow constants deleted in
`comet_visualization_shells.py` (lines 492-493, 602). `SUN_RADIUS_KM`
and `SOLAR_RADIUS_AU` imported through shim. Runtime-verified
value-preserving. Fire-then-silence test: 1d detected 3 shadow constants,
1f silenced them.

**build_pinned_values() bleed fix (2026-07-31, Opus 5 follow-on).**
Extracted shared `constant_has_own_citation()` predicate routed through
both `build_pinned_values()` and `build_cited_constant_names()` --
eliminates the 10-line window bleed where uncited constants could inherit
a neighbor's citation. Measured impact: zero (all 34 constants in
`constants_new.py` already carry own citations), but defensive against
future additions. test_provenance_1d.py 15 -> 20 (5 predicate tests
added). `test_both_pinned_builders_agree` asserts the two callers stay
synchronized.

**D8.5 -- Option A retired (2026-08-01, Opus 5).** Two mechanisms removed
from `score_unit()`, both granting V_SOURCED without a real citation.
(a) Option A: credited display strings whose numeric claims matched
pinned constant values -- coincidence, not sourcing. 26 findings affected
(not 18 -- 1d's temperature units created new claims eligible for the
credit). 23 moved to Tier 1. (b) Staleness credit: granted V_SOURCED to
strings matching date-sensitive patterns ("as of 2024", "Planned",
"Still active") with no citation at all -- the reason string said "no
source" and the score said "sourced." Logic also ran backwards: staleness
means a claim will expire, making it more vulnerable, not less.
15 findings, all now at V_RECALLED. `build_pinned_values()` kept -- it
feeds `scan_shadow_constants()` for derived-shadow detection, now
diagnostic-only. Scoring path audit: three remaining paths that set
`unit.vuln`, all requiring a citation a person wrote. No other instance
of the credit-without-sourcing failure class remains.

**General lesson (D8.5):** when a scoring definition changes, every
mechanism assigning that score needs re-reading, not just the ones the
change targeted. Both Option A and staleness credit predated the D3
ladder and were not wrong when written -- they were outlived by a
definition change and never revisited.

### Phase 2 build history (D4: cross-checked annotation mechanism)

**Piece 1 -- scanner mechanism (2026-08-01, Opus 5).** Teaches the scanner
to recognize `# Cross-checked:` annotations and score them
V_CROSS_CHECKED (V2). Delivered as transactional patch
(`documentation/patch_phase2_piece1.py`, 9 anchored edits).

New code: `parse_cross_checks(text)` parser returning `(records, issues)`,
`distinct_checker_identities()`, `_record_cross_check_diagnostics()`,
scoring branches in `score_unit()`, diagnostic subsection in
`generate_report()`. New test file: `test_cross_checked.py` (16 tests).

V2 scoring rule (decided, 5-model competitive review -- GPT x2, Opus 5 x2,
Fable 5): `sourced AND two distinct cross-checks`. Sourced means direct
citation or inherited citation. Two distinct means two annotation lines
naming different checker identities (string-level, not model-family-level).
Anti-gaming: parenthetical `.md` reference required. ISO dates only.
`# Cross-checked:` is deliberately NOT in SOURCE_PATTERNS -- a malformed
annotation earns nothing.

Predesign went through two review rounds (R0 -> R1 -> R2). Key findings
from the competitive review: the R0 fallback claim was factually wrong
(all 4 reviewers independently confirmed `has_citation()` does not match
"Cross-checked"); V2 must require source evidence (3/4 converged);
two distinct checkers required (3/4 converged); the worksheet inventory
was wrong (15 not 7, Opus 5 #1 only); a live false positive exists at
`planet_visualization_utilities.py` ~line 456 (Fable only). The
competitive pattern produced genuine discovery -- findings missed by some
reviewers were caught by others.

Lookback bleed measured (as-built section 5): an annotation promotes sourced
claims within ~50 lines below it. Containment is process-side -- the
identity diff after annotation insertion catches unintended promotions.
High-exposure files: `info_dictionary.py` (up to 11 downstream per
annotation). Low-exposure files (mars, eris, earth) proceed as-is.

Decided: V_CROSS_CHECKED comment updated to "independently verified via
competitive pattern" (was "blind"). Worksheets show current values to
both models; the discipline is independent sourcing, not blindness.

**Track 1 scope (decided, not yet executed).** Complete the competitive
pattern for the 15 files that have April 2026 Gemini worksheets. Claude
independently verifies the same claims. Tony compares. Convergent claims
get annotated. Divergences discussed; unresolved claims go to GPT as
tiebreaker.

**Track 2 scope (decided, not yet executed).** New worksheets for
uncovered files, starting with `celestial_objects.py` (54 findings). Both
models get the same worksheet independently. Separate sessions.

**Phase 2 Track 1 -- Mars calibration (2026-08-02, Opus 4.6
orchestrating).** First cross-checked annotations written.
`mars_visualization_shells.py`: 14 edits via transactional patch.
Value fixes: bow shock 1.5->1.6, Hill sphere 324.5->~320, perihelion
~0.8->~0.98, AU 0.073->0.007. Stratosphere claim removed (GPT finding,
unsourceable). Hill sphere `# Source:` rewritten as derived-value
citation. 8 Cross-checked annotations, 4 source blocks. Pushed at
`225071f6`. Checkers: Claude Opus 5 + GPT-5.6 Thinking.

**Phase 2 -- constants_new.py cross-check (2026-08-02, Opus 4.6
orchestrating).** Citation verification (distinct from Mars's value
verification). 30 edits via transactional patch. 6 accuracy fixes
(heliopause arithmetic, Haumea/Arrokoth/Bennu radii, chromosphere
1.5->1.1, gravitational influence 126k->150k). 8 citation corrections
(IAU B3 scope, Archinal 2018, IERS, DeForest year). 54 Cross-checked
annotations, zero Verified lines remaining. Pushed at `acf32d5a`.
Checkers: Claude Opus 5 + GPT-5.6 Thinking (primary); Gemini (book
citations -- Carroll & Ostlie, Golub & Pasachoff). Key finding: Gemini
can access book content web search cannot reach.

### Phase 2: Cross-check sweep (OPEN)

**Batch 1 (COMPLETE, 5 bodies + Mars retroactive).** Three-model
competitive cross-check of moon, eris, mercury, venus, pluto
visualization shells. 34 scanner findings, 56 claims verified. 13 value
fixes, 17 citation corrections (including 3 fabricated/wrong-paper
citations). Conventions established for Hill sphere (perihelion distance,
system mass for binaries), visualization constants (best-sourced single
value for code, range in description), and retired "Verified: April 2026"
annotation format. Mars cross-checked as precedent.

**Batch 1 geometry follow-up (COMPLETE).** Fable audit
(`FABLE_shell_consistency_audit_report.md`, `679c2f4`) discovered
radius_fraction geometry constants were not updated to match the
corrected display text values -- shells rendered at old sizes while hover
text claimed new ones. Also found: `<br>` in _info strings rendering
as literal markup in GUI tooltips; 126 dead `tooltip` fields in
SHELL_CONFIGS/CUSTOM_SHELLS; up to six independent storage locations per
physical value. Opus 5 built 7 geometry+text patch scripts (47 edits).
`<br>` -> `\n` converted for moon, eris, pluto, mars. Mercury mantle
diamond claim removed. Stale headers corrected. Provenance-neutral
(Tier 1: 207 -> 207).

**Batch 2 (NEXT): Gas giants** -- jupiter (18 findings), saturn (10),
uranus (24), neptune (26). Plus Saturn Hill sphere three-way
inconsistency, Jupiter/Saturn "not yet rendered" false claims, `<br>`
conversion for jupiter/saturn/uranus/neptune/planet9/solar. See
handoff_batch1_complete.md for template improvements.

**Process decisions (2026-08-02):** Annotation format settled (source
via model, ISO date, worksheet reference). Two worksheet types
established (value verification, citation verification). Model roles
tested and encoded in provenance-discipline v1.5: Claude (derivations,
citation-shape errors), GPT (papers, DOIs, explicit math), Gemini
(book citations), Fable (far-reaching audits). April Gemini worksheets
confirmed not V2-quality (Mars bow shock miss); all modules need fresh
independent legs regardless of Track 1/Track 2 status.

**Module plan (decided 2026-08-02).** Four batches: Batch 1 (Moon, Eris,
Mercury, Venus, Pluto -- 34 findings), Batch 2 (gas giants -- 78),
Batch 3 (Earth, solar, comets -- 82), Batch 4 (star_notes,
celestial_objects, info_dictionary -- 210). Batch 2 unblocks Artifact 2.

### Observations (not fixed, tracked)

**Em-dashes in comet_visualization_shells.py.** Three pre-existing
non-ASCII bytes (em-dashes), one inside a display string. Tony approved
fixing -- separate edit, changes user-visible output.

**Patch scripts in repo root -> documentation/.** Seven committed patch
scripts moved to `documentation/` to clear self-scan Tier-1 noise.
Complete.

### What remains open under L-156

**Phase 2 (D4 cross-checked annotation backfill).** Piece 1 (scanner
mechanism) COMPLETE (`373c6d8`). Mars and constants_new.py cross-checked
and annotated (`acf32d5a`). 62 Cross-checked annotations live. Module
plan: 4 batches, 16 files remaining, 404 findings total. Batch 1 (5
small shell modules, 34 findings) is next. Worksheet prompts prepared
in session handoff.

**Phase 3.** L-155 (pinning engine), L-160 (retire
`test_constants_provenance.py`, gated on L-155), and MODULE_DOMAIN_MAP /
DOMAIN_LABELS import from `module_atlas.py` (L-163 review amendment).

**Phase 4.** L-157 / L-161 (Gemini cross-check sweeps), L-159
(disclosed-approximation enforcement).

### Ref

`provenance_scanner.py`; `constants_new.py`;
`data/provenance_exceptions.json`;
`documentation/provenance_audit_handoff_v1.md` (Arrokoth/Parker
precedent); `ADDENDUM_v23_design_session_narrative.md` (anchoring
near-miss); `HANDOFF_addendum_phase1_and_uranus_cleanup.md`,
`HANDOFF_provenance_phase1_v17.md` (Gemini cross-check itself wrong);
`MANIFEST_bow_shock_and_dipole_cone_v1.md` (blind-pass positive case);
`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md`;
`documentation/AS_BUILT_L156_phase1c.md`;
`documentation/AS_BUILT_L156_phase1d_e_f.md`;
`documentation/PREDESIGN_HANDOFF_phase1_d_e_f_R1.md`;
`documentation/REVIEW_predesign_1d_1e_1f.md`;
`documentation/BUILD_phase_1c_prompt.md`;
`documentation/patch_phase1c_citation_inheritance.py`;
`documentation/patch_phase1_d_e_f.py`;
`documentation/patch_pinned_values_bleed.py`;
`test_provenance_1d.py`; `test_citation_inheritance.py`;
L-155; L-157; L-158; L-159; L-161; L-162; L-163; L-173; L-174; L-175.
`documentation/patch_retire_option_a.py`;
`documentation/AS_BUILT_retire_option_a.md`.
`documentation/patch_phase2_piece1.py`;
`test_cross_checked.py`;
`documentation/AS_BUILT_phase2_piece1.md`;
`documentation/PREDESIGN_phase2_cross_checked_annotation_R2.md`;
`documentation/BUILD_PROMPT_phase2_piece1.md`;
`documentation/REVIEW_PROMPT_phase2_predesign.md`.
ASBUILT_batch1_cross_check_patches.md,
ASBUILT_geometry_and_br_fix.md, 
FABLE_shell_consistency_audit_report.md,
PROMPT_fable_shell_consistency_audit.md,
PROMPT_opus5_geometry_and_br_fix.md'

---

#### [L-157] Gemini cross-check of shell config ring/belt/atmosphere geometry values
<!-- L:157 status:OPEN upd:2026-07-27 section:W.Active flag: rice:2/3/85/2 -->
- **What.** Run the proven April 2026 methodology (Claude drafts a
  fact-check worksheet, Gemini cross-checks against authoritative sources,
  Tony integrates) against the raw geometry dicts in
  `earth_visualization_shells.py`, `jupiter_visualization_shells.py`,
  `saturn_visualization_shells.py` (`ring_system`, `van_allen_belts`,
  `radiation_belts`, `atmosphere_shell`) -- confirmed these specific
  values have never been through this process.
- **Sequencing (confirmed, review section 5):** runs sequentially through
  the same Mode 7 relay channel as the D3 calibration and L-161's sweep,
  not as a parallel thread -- after Phase 1-2 (L-156) ships, so results can
  be annotated in a form the scanner can actually see.
**Gap:** draft the worksheet (per `worksheet_jupiter_visualization.md`
template, scoped to config values not narrative strings) **blind -- no
Claude-derived figures included**, per the near-miss already caught once
in this project (`ADDENDUM_v23_design_session_narrative.md`: an anchored
draft prompt was rewritten to ask de novo after Tony flagged the
rubber-stamp risk); carry to Gemini; integrate corrections; apply the
cross-checked annotation (with the blind/anchored field, per L-156) once
L-156's build defines its form.
**Ref:** `provenance_audit_handoff_v1.md`; `MODE7_gemini_crosscheck_magnetosphere.md`;
`worksheet_jupiter_visualization.md`; `ADDENDUM_v23_design_session_narrative.md`
(blind-worksheet precedent); L-155; L-156; L-161.

---

#### [L-158] Derived-constant vulnerability inheritance rule (revised from a proposed rung, 2026-07-27)
<!-- L:158 status:OPEN upd:2026-08-25 section:W.Active flag: rice:4/2/70/1 -->
- **What.** Values computed from already-tracked primaries (e.g.
  `SOLAR_RADIUS_AU = SUN_RADIUS_KM / KM_PER_AU`) don't fit the criticality
  question at all -- it's a Vulnerability question.
- **Superseded (D9's original framing, and this item's own original
  title, were wrong):** "derived rung = V1" treated a derived value as
  structurally immune to drift. Both Fable 5 and GPT 5.5's D3 calibration
  passes rejected that premise independently -- the formula, the units, or
  a wrong parent reference are their own error surface (Fable's cited
  precedent: Mars Climate Orbiter, a real mission lost to exactly this
  class of bug), and a value computed once and then hardcoded as a
  literal isn't protected by its original derivation at all.
- **Decided (2026-07-27, folded into L-156's ladder as a rule, not a
  rung):** two cases, not one tier --
  - **Derived at runtime** (formula lives in the code, evaluates from the
    tracked primary every call): inherits its weakest input's V-rung,
    but only once the derivation logic itself -- the formula, the units,
    the parent reference -- has cleared one independent cross-check.
    Until that check happens, treat as unverified regardless of the
    input's own rung.
  - **Derived once, then frozen as a literal** (a hardcoded number with a
    "computed from X" comment): not actually derived any more -- it's a
    copy, and copies drift by exactly the mechanism this item's original
    premise claimed was impossible (the primary updates, the frozen
    literal doesn't). No special handling: plain V3 (sourced-unchecked),
    with the derivation comment serving as its citation.
  - The two-factor structural check (`# Derived:` comment + AST
    confirmation it's actually computed) still stands as the mechanism
    for telling the two cases apart -- it just no longer implies an
    automatic V1 grant on its own.
**Note (2026-07-29):** Verified live -- exactly four `# Derived:` comments
exist repo-wide, all in `constants_new.py` (lines ~100, 104, 126, 130):
`SOLAR_RADIUS_AU`, `LIGHT_MINUTES_PER_AU`, `CORE_AU`, `RADIATIVE_ZONE_AU`.
All four are genuine runtime formulas; zero frozen literals are annotated.
**The inversion:** this item's two-factor detector (comment + AST check)
can only catch a frozen copy that announces itself. The dangerous ones
don't -- `CENTER_BODY_RADII['Sun'] = 695700` is a frozen copy of
`SUN_RADIUS_KM` with no `# Derived:` comment anywhere near it, invisible to
the mechanism as specified. Same failure class as the
`close_approach_data.py` stale-copy bug that originally motivated
`test_constants_provenance.py`. Confirmed live in the wild:
`comet_visualization_shells.py` lines 492-493 (`SUN_RADIUS_KM = 695700.0`,
`KM_PER_AU = 149597870.7`, hardcoded, no `# Source:` nearby, despite
`KM_PER_AU` already being imported at line 42) and line 602
(`SUN_RADIUS_AU = 695700.0 / 149597870.7`). Neither shows as Tier-1 today
because `build_pinned_values()` treats any value match against an
already-cited `constants_new.py` constant as V_SOURCED, whether the match
is a real import or a bare hand-typed copy.

**Note (2026-07-31):** L-158 piece 2 (delete shadow constants in comet_visualization_shells.py, import through shim) is DONE, landed as part of L-156 Phase 1f. Pushed at 8bd7778. SUN_RADIUS_KM and SOLAR_RADIUS_AU imported, three local copies deleted, runtime-verified value-preserving.

**Gap:** rides Phase 1 of L-156's scanner build (unchanged). Two concrete
pieces, not one: (1) widen `build_pinned_values()`/scoring per L-156's Gap
item 5 -- the actual fix; (2) separately, fix the two live instances
directly: delete the local shadow constants in
`comet_visualization_shells.py` lines 492-493 and 602, import
`SUN_RADIUS_KM` through the `planet_visualization_utilities` shim alongside
the existing `KM_PER_AU` import (line 42). Small, mechanical, no
dependency on (1) -- can land anytime.
**Note (2026-08-25), a measured instance from the assembler build.**
Four of the Sun's fourteen sphere radii are DERIVED EXPRESSIONS the
scanner does not score: `SOLAR_RADIUS_AU`, `CORE_AU`,
`RADIATIVE_ZONE_AU`, `CHROMOSPHERE_PHYSICAL_RADII`. All four are
richly cited; all four are unreachable, because the scanner scores
LITERAL ASSIGNMENTS. The claims inside them -- the 0.2 core factor and
the 0.7 radiative-zone factor -- are already declared as visualization
boundaries with the measured ranges named, which is the right shape
and invisible to the tooling. See L-190.
**Ref:** `constants_new.py` derived-constants section; L-156 (holds the
full ladder this rule attaches to).

---

#### [L-159] Disclosed-approximation check (Envelope of the Unknowable, scanner-level)
<!-- L:159 status:OPEN upd:2026-07-27 section:W.Active flag: rice:2/2/60/2 -->
- **What.** Illustrative/stylized values (Mercury's magnetosphere flaring
  parameter, a shared bow-shock eccentricity applied uniformly for
  simplicity) don't fit either criticality tier. Ties to the resident
  protocol's "Show the Envelope of the Unknowable" -- not currently checked
  for anywhere in the scanner. The real question: is the approximation
  disclosed as one, or presented silently as if precise?
- **Decided (D9, review):** annotation convention named -- `# Illustrative:`.
  Planet 9's radius (a model estimate, never directly observed -- see
  L-162) attaches to this item as a case, per the design review.
- **Deliberately deferred:** the ENFORCEMENT check (does the rendered
  hover actually disclose what the comment discloses) is genuinely hard
  and stays open past this cluster closing.
**Gap:** design pass on detection mechanics, once the rest of the cluster
lands.
**Ref:** resident protocol Part 3, "Show the Envelope of the Unknowable";
`MODE7_gemini_crosscheck_magnetosphere.md`; L-156; L-162.

---

#### [L-160] test_constants_provenance.py -- retire once fully absorbed, not before
<!-- L:160 status:OPEN upd:2026-07-27 section:W.Active flag: rice:3/3/90/1 -->
- **What.** Tony confirmed directly: "I never run it, I only run the
  scanner." Correct logic, dashboard-listed, zero code path calling or
  importing it anywhere in the repo. A second, independently-triggered
  entry point that evidence shows doesn't get pulled.
- **Decided (Tony, 2026-07-27):** "if we have fully integrated the
  constants provenance, we can retire the stand-alone file" -- retire is
  confirmed, but **conditional on the integration actually landing first**,
  not a green light to delete it now. This matches the design's own
  sequencing exactly: D10's retirement was always scoped inside Phase 3,
  alongside L-155's pinning engine that replaces what this file checks.
  **Do not delete this file before L-155's pinning checks are built and
  verified to cover the same ground.**
- **On retirement, five reference sites to clear (grepped, not assumed):**
  the file itself; `palomas_orrery_dashboard.py`'s menu entry (~line 227);
  `module_atlas.py`'s ROLE_MAP entry; the scanner's own MODULE_DOMAIN_MAP
  entry and report mention; the comment in
  `comet_visualization_shells.py` line 695 (reword to point at the
  scanner's pinning section instead). The file's docstring institutional
  memory (the motivating bug, the April verification history) migrates
  into the new pinning section's docstring.
**Gap:** **(decide)** none remaining -- retire-vs-wrapper is settled;
**(do)** execute the five-site cleanup as part of L-155's Phase 3 build,
not before.
**Ref:** `test_constants_provenance.py`; `palomas_orrery_dashboard.py`;
`module_atlas.py`; `provenance_scanner.py`; `comet_visualization_shells.py`
line 695; L-155; L-156.

---

#### [L-161] Gemini sweep -- clear the display-string Tier-2 backlog
<!-- L:161 status:OPEN upd:2026-07-27 section:W.Active flag: rice:3/3/70/2 -->
- **What.** ~330 display-string citations, currently C=4/V=2 under
  *today's* meaning of V2 (SOURCED). **Re-read against the closed
  ladder, not the old one** (exactly the D1/D7 re-read L-156's Fable 5
  round flagged as needed): under the new scheme, V2 now means
  CROSS-CHECKED, a stronger bar. Only the subset with a genuine,
  independent, dated (and blind-checked) annotation backfills to the new
  V2; everything else -- including anything merely cited -- lands at the
  new V3 (merged sourced+stale). ~130 were already Gemini-verified by the
  April 2026 worksheets: **check those worksheets against the new blind-
  check bar before backfilling** (per `ADDENDUM_v23`'s anchoring near-
  miss, an anchored pass doesn't qualify even if it happened) -- if they
  don't clear it, they need redoing, not just re-tagging. The remainder
  need a genuinely new sweep regardless.
- **File concentration, confirmed empirically:** 84% of the 330 sit in 15
  files. `celestial_objects.py` alone is 50 findings with zero prior
  worksheet coverage. Neptune, Uranus, Solar, Saturn, Pluto,
  `idealized_orbits.py`, `planet_visualization_utilities.py` also never
  had a Gemini pass.
- **Sequencing (revised on review):** runs AFTER L-156's build ships, not
  parallel with it -- the urgency doesn't exist until the V-ladder change
  actually lands.
- **Practical note:** consider the same Mode 7 relay channel as L-157
  (sequentially, not merged in scope) rather than a second separate
  Gemini engagement.
**Gap:** draft first worksheet (`celestial_objects.py`) **blind**, same
requirement as L-157; confirm the April worksheets' actual coverage
against the new blind-check bar, not just their topic coverage, before
assuming which ~130 are already clear.
**Ref:** L-156; L-157; L-160; `worksheet_*.md` set;
`ADDENDUM_v23_design_session_narrative.md` (blind-worksheet precedent).

---

### W.Deferred -- captured, not yet actionable

#### [L-091] Option E: unified front end
<!-- L:091 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice:2/2/50/2 -->
- The existing gallery viewer (3,345 lines of JS) becomes the single front end
  for all channels: static gallery, scheduled scenes, server-built and
  browser-built scenes. A and B become interchangeable back ends. Every dollar
  of work on the viewer pays into all channels. Arrives nearly for free if the
  serverless (Pyodide) path wins in L-088.
**Ref:** Fable 5 survey (Option E); master plan S8.

#### [L-092] Embeddable scenes for educators
<!-- L:092 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice:2/2/50/2 -->
- An iframe embed snippet per scene, so educators can put a working orrery view,
  HR diagram, or orbital visualization in their own pages. Nearly free given the
  viewer; large reach-per-effort.
**Ref:** master plan S8.

#### [L-093] Educational guided explorations (specs as curriculum)
<!-- L:093 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice:2/2/50/2 -->
- Scene specs as curriculum -- a notebook (JupyterLite or similar) that walks
  through "build a scene of the inner solar system, now change the center to
  Mars, now add Phobos" or "see how eccentricity transforms an orbit." The spec
  vocabulary becomes the teaching language. Cheap experiment once the assembler
  exists.
**Ref:** master plan S8.

#### [L-094] Community cache as commons
<!-- L:094 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice:2/2/50/2 -->
- If tier-3 persistence is turned on, every fulfilled user request enriches the
  shared cache. Over time, the cache becomes a community-curated collection of
  interesting scenes -- driven by curiosity, not just Tony's curation. Tied to
  the tier-3 persistence dial (master plan S7 #5).
**Ref:** master plan S7/S5, S8.

#### [L-095] PWA / offline capability for classrooms
<!-- L:095 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice:2/2/50/2 -->
- Progressive Web App wrapper -- installable and usable offline. Relevant for
  classrooms with unreliable connectivity. Modest effort if the architecture is
  static-first. Verify PWA constraints at build time.
**Ref:** master plan S8.

#### [L-096] Web orrery aesthetic / feel design conversation
<!-- L:096 status:DEFERRED upd:2026-07-03 section:W.Deferred flag: rice:2/2/50/2 -->
- The desktop is a power tool with 60+ toggles. The web version could be that --
  or something different. A curated explorer. A storytelling medium. An invitation
  to wonder. The envelope-declaring GUI implies curation over completeness. The
  orbital parameter viz is inherently educational. The Earth system carries a duty
  of care. How do these different voices come together in one web experience?
  Design conversation before Phase 6 (web UI).
**Ref:** master plan S8 Q4; Fable 5 review of v4.

#### [L-101] Osculating-history fan (perturbed-moon precession view)
<!-- L:101 status:OPEN upd:2026-07-08 section:W.Deferred flag: rice:2/2/50/2 -->
- NET-NEW (data + render). N osculating element-sets, one per orbital period back
  from the current phase-locked anomaly (default 3, user-select 1-6), drawn as a
  fan of faint conics -- shows apsidal rotation / plane precession as smooth orbit
  motion (vs a chunky position trace). Data: builder fetches elements at N epochs
  (new). Render: overlay N faint ellipses (new). Deferred from the first gallery
  build; interim = conic + as-of-today point.

#### [L-102] Spacecraft trace thinning (arc-minute decimation)
<!-- L:102 status:OPEN upd:2026-07-11 section:W.Deferred flag: rice:2/2/50/2 -->
- STALE ASSUMPTION CORRECTED (2026-07-11): this originally assumed the raw
  archive stays daily and thinning happens separately at serve time. L-109's
  spacecraft redesign pulled thinning FORWARD to fetch-side instead -- the
  raw archive itself now stores the Douglas-Peucker-thinned glide (windows
  exempt, kept daily). Verified end-to-end on real Voyager 1 data (L-113):
  49-year glide 2549 -> 29 points, both flyby windows fully daily with zero
  gaps.
**Gap:** whether this originally-scoped served-side/interactive.html step is
now fully superseded (nothing left to build -- the builder already delivers
thinned data) or still needed for a different reason (e.g. interactive.html
consuming/rendering something not yet aligned to the new shape) is a call
for you or Opus to make, not resolved here.
**Ref:** L-109 (the fetch-side redesign); L-113 (tonight's live verification; orrery-side port idea).

#### [L-103] Hyperbolic conic -- browser branch (interactive.html)
<!-- L:103 status:OPEN upd:2026-07-08 section:W.Deferred flag: rice:2/2/50/2 -->
- NET-NEW render. interactive.html Pyodide engine is ellipse-only
  (r=a(1-e^2)/(1+e*cos th) breaks at e>=1). Port generate_hyperbolic_orbit_points
  (r=|a|(e^2-1)/(1+e*cos th); th_inf=arccos(-1/e); truncate at max_distance;
  500/1000 pts). Reference exists desktop-side. Needed for comets / interstellar
  objects (3I/ATLAS) in the interactive. Served data already ready (elements +
  orbit_type + Tp + max_distance).

#### [L-126] Close-approach/encounter anchor mechanism -- general principle (NEOs, comets, spacecraft), not Apophis-specific
<!-- L:126 status:OPEN upd:2026-07-17 section:W.Deferred flag: rice:2/2/85/2 -->
- **General principle (Tony, 2026-07-17):** this is not an Apophis special
  case. ANY body with a close-approach/encounter event -- a near-Earth
  object's predicted flyby, a comet's perihelion passage, a spacecraft's
  encounter with a planet or moon -- needs its encounter-specific VIEW
  anchored at the encounter epoch, not "today" or the plot's default date.
  Apophis is the flagship worked example, not the scope boundary.
- **Already proven, already shipping, on the DESKTOP side** -- verified
  directly against current code, not recalled from a past session summary:
  - `idealized_orbits.py` `plot_hyperbolic_osculating_orbit` -- its own
    docstring: "date (datetime): Plot start date (used as fallback epoch
    only)"; the `approach` dict (CAD perigee epoch) takes precedence when
    available. This is exactly the close-approach VIEW anchor, already
    built, for any small body with CAD data -- not asteroid-specific
    even on the desktop.
  - `spacecraft_encounters.py` `resolve_encounter_time` /
    `get_encounter_preset` -- the spacecraft analog. Concrete evidence
    this matters: the April 2026 Artemis II HypOsc bug -- the full
    mission plot (GUI epoch) showed q=83,203 km; the "Go: Closest
    Approach" preset (derived encounter epoch) showed the correct
    q=8,318 km. Same principle, same failure mode when it's missed, on a
    completely different body class (spacecraft, not a NEO).
- **Not yet ported to the GALLERY serving side, unevenly:**
  - Comets: `overrides.comet.anchor: "Tp"` exists (`resolve_comet_conic`)
    -- but it anchors the WHOLE served baseline block, not just a view.
  - NEOs (Apophis): nothing built yet (this item's original scope).
  - Spacecraft: nothing built yet -- Voyager 1 in the gallery currently
    serves only a full-trajectory arc; there is no "Voyager at Jupiter" /
    "Voyager at Saturn" encounter view at all on the gallery side, even
    though the desktop already has the proven mechanism for this class.
- **Settled scope (Apophis case, still holds generally):** the anchor
  applies ONLY to the close-approach/encounter view. Baseline/full-orbit
  serving -- and F1a's trust measurement -- stays on its own natural
  epoch ("today" for NEOs; unaffected for a spacecraft's full arc). This
  is consistent with the desktop's already-proven pattern for both small
  bodies and spacecraft.
- **Open question, NOT resolved here:** the comet case currently anchors
  the served BASELINE block at Tp, not just a view -- is that a
  deliberate, legitimate exception (comets may not have a meaningful
  "baseline away from perihelion" view the way a planet or NEO does), or
  should it be reconciled with the view-only principle now that the
  principle has been stated explicitly? Flagging for Tony's judgment, not
  assuming either answer.
**Gap:** (1) Apophis: overrides.asteroid.anchor config entry +
resolve_comet_conic-style builder branch, scoped to a close-approach view
per the settlement above; (2) generalize the mechanism's naming/schema so
it isn't asteroid-specific -- likely a category-agnostic key rather than
overrides.asteroid.anchor by itself, since NEOs and spacecraft both need
it; (3) port the spacecraft encounter-view mechanism to the gallery
serving side (currently absent entirely) -- Voyager 1 is the natural
first case, following spacecraft_encounters.py's proven pattern; (4)
reconcile or explicitly ratify the comet baseline-anchoring exception
against the general view-only principle.
**Ref:** PHASE2_F1_FEATURE_SERVING_DESIGN_HANDOFF_v0.4.md SS6.6;
PHASE2_F1_BUILD_MANIFEST_v2_2.md sec 1 + sec 8; gallery
tools/gallery_cache_builder.py resolve_comet_conic; close_approach_data.py;
orrery idealized_orbits.py plot_hyperbolic_osculating_orbit (CAD-perigee
anchor, verified live); orrery spacecraft_encounters.py
resolve_encounter_time / get_encounter_preset / SPACECRAFT_ENCOUNTERS; the
April 2026 Artemis II HypOsc epoch-timing fix (q=83,203 km vs q=8,318 km);
L-118 (F1 parent); M2_IMPLEMENTATION_REPORT.md.
**Claude:** RICE proposed 2/2/85/2 (reach raised from the Apophis-only draft
-- this now covers any future NEO close approach and any spacecraft
encounter added to the gallery, not one object; confidence stays high,
grounded in mechanisms already proven and shipping on the desktop side;
effort ticks up slightly for the naming generalization, still small per
object once the pattern is set) -- yours to finalize.

#### [L-165] Site continuity if there is no active administrator (succession / legacy planning)
<!-- L:165 status:OPEN upd:2026-07-27 section:W.Active flag: rice:?/?/?/? -->
- Origin: Tony raised the real scenario -- not vacation, not a dead
  laptop for a week, but permanently indisposed -- and asked what should
  happen to the site with no administrator, ever, again. Alerting an
  administrator is the wrong solve for "there may not be one"; this item
  reframes around structural survivability instead.
- **Good news, already true, no build needed:** the served_window/trust
  system (L-149/L-118, M2) means the site does not corrupt or drift if
  fetches stop forever -- it freezes at the last good window and the
  resolver correctly refuses dates outside it (OutOfServedWindowError)
  rather than rendering wrong positions. A permanently-abandoned site is
  a frozen, correct snapshot, not a broken one. GitHub Pages serves that
  frozen state indefinitely at zero cost/maintenance as long as the
  GitHub account exists.
- **Real structural dependency, confirmed:** palomasorrery.com is a real,
  paid custom domain (verified via the repo's own CNAME file). Domain
  registrations lapse without renewal and, unlike everything else here,
  an unpaid domain does not fail gracefully -- it goes dark. This needs a
  deliberate, non-technical decision: pre-pay the registration for a long
  runway (many registrars allow ~10 years at once), and/or explicitly
  accept the free `tonyquintanilla.github.io` URL as a permanent fallback
  identity if the custom domain ever lapses.
- **Open architectural question, only if continued fetching (not just a
  correct frozen snapshot) matters as part of the legacy:** the nightly
  fetch currently runs on Tony's personal laptop, which is not durable
  infrastructure over a long horizon. Standard fix: migrate the nightly
  builder from local Task Scheduler to GitHub Actions (free for public
  repos, runs in GitHub's own infrastructure, no personal machine
  dependency). Real migration project, not a small tweak.
**Tony:** revisit when there's focus time for it. Not urgent -- the site
does not degrade in the meantime either way.
**Gap:** (1) decide domain-renewal approach; (2) decide whether continued
fetching matters enough to justify the GitHub Actions migration, or
whether a correct frozen snapshot is an acceptable legacy on its own; (3)
if migrating, design session first -- credential storage for the push
step is the main new wrinkle, given the repo is public.
**Ref:** L-149/L-118 (served_window/trust), CNAME (confirms the domain),
M2 testing protocol addendum (Layer 3 background).

#### [L-168] propagate_marker uses solar K_GAUSS mean-motion -- wrong for planetocentric moon markers (FLAG-2; caught in F1 design, avoided in serving, source fix still open)
<!-- L:168 status:OPEN upd:2026-07-28 section:W.Active flag: rice:3/3/80/2 -->
- **What.** `gallery/assembler/render_orbits.py` `propagate_marker()`
  computes mean motion as `n = K_GAUSS / (a ** 1.5)` (line 90 @ gallery
  f4ce24cb), where `K_GAUSS = sqrt(GM_sun)`. Correct ONLY for heliocentric
  bodies. For a planetocentric moon -- served from its OWN osculating conic
  in the parent-relative frame, so `a` is the tiny moon-parent semi-major
  axis in AU -- solar GM is the wrong gravitational parameter, and the
  propagated as-of-today marker lands wrong by ~3 orders of magnitude.
  [verified @f4ce24cb]
- **Worked number.** Moon a ~ 0.00257 AU -> n = 0.01720209895 / 0.00257^1.5
  ~ 132 rad/day -> implied period ~ 68 minutes, versus the real 27.32-day
  sidereal month. Independently re-derived. This is the same catch GPT's F1
  manifest missed and the Fable/GPT competitive cross-check surfaced (see
  MASTER_PLAN_INTERACTIVE_GALLERY.md, "New in v14").
- **Caught != fixed.** F1/M2 (L-118 / L-149) was DESIGNED to avoid this: the
  serving pipeline captures Horizons' own `n` and emits `n_deg_per_day`, and
  the builder never calls `propagate_marker` (FLAG-2 comments at
  gallery_cache_builder.py lines 67, 341, and the derivation note ~372-380).
  But avoiding it in the serving path did not change `propagate_marker`
  itself -- render_orbits.py was correctly out of M2's edit scope, so the
  wrong formula is still at HEAD and `propagate_marker` is on a LIVE
  dispatch path: `gallery/assembler/assemble.py:62` calls it to place the
  position marker for every object that has osculating elements.
  [verified @f4ce24cb]
- **Dormant, not benign.** Only Artifact 1 (Earth, heliocentric) is built
  and Mode-5 accepted in the interactive assembler today, so the live path
  only ever feeds a heliocentric body, where the formula is correct. It
  becomes a visibly wrong marker the moment a planetocentric moon renders --
  Artifact 2 (Jupiter/Saturn) and Artifact 3 (Moon/Io/Titan), the objects
  L-154's feature-rendering layer unblocks. The trigger for this bug and the
  trigger for L-154 are the same event.
- **Fix approach (not built; design choice for its session).** The correct
  `n` is already in the served data (`n_deg_per_day` on the osculating
  block). Preferred: thread the served `n` into `propagate_marker` and use
  it directly instead of deriving from `a` ("fetched, not recalled" -- use
  Horizons' measured mean motion); alternative: pass the correct
  central-body GM per frame. Either removes the solar-GM assumption. Small,
  targeted change to one function plus the `obj.osculating` payload that
  reaches it; guard the no-`n` case (WARN/skip, never a silent solar-GM
  fallback). Confirm on Earth's existing Mode-5 harness (no heliocentric
  regression) before a moon artifact.

**Tony:** documentation-only capture (repo moved twice since the original
F1 build; no code touched this session). Gives the caught-but-unfixed bug
a handle so it cannot fall through when L-154 / Artifact 2 resumes.
Renumbered twice on the way in -- L-166 draft -> L-167 draft -> this L-168
-- purely from handle collisions as other sessions landed unrelated items
in the same window; the underlying finding never changed.

**Gap:** land the `propagate_marker` fix (use served `n`, drop solar-GM
derivation, guard no-`n`) BEFORE or WITH the L-154 JS feature-rendering
layer, so the first Jupiter/Saturn/moon render carries correct marker
positions; re-run Earth Mode-5 as the no-regression gate.

**Ref:** `gallery/assembler/render_orbits.py` (propagate_marker, line 90 @
f4ce24cb); `gallery/assembler/assemble.py:62` (live call site);
`gallery/assembler/tests/test_artifact1_earth.py:81` (test call site);
`tools/gallery_cache_builder.py` FLAG-2 comments (67, 341, ~372-380);
`documentation/M2_IMPLEMENTATION_REPORT.md`;
`documentation/PHASE2_F1_BUILD_MANIFEST_v2_2.md` (FLAG-2 origin);
MASTER_PLAN_INTERACTIVE_GALLERY.md ("New in v14"). Coupled to L-154 (same
trigger; DISTINCT bug -- L-154's resolver `tuple(dict)` drops feature
PARAMETERS; this drops marker POSITION accuracy). Sibling to L-166 (F1b
trust consumption -- distinct concern, same assembler / pre-Artifact-2
phase). NOT to be confused with L-167 ("Artifact-1 field notes --
orrery-coding-conventions still missing three entries" -- unrelated
Plotly-rendering topic, assigned in the same window; pure numbering
coincidence). Anchored: built on orrery 0d13fbb9 / gallery f4ce24cb.

#### [L-172] Phase 0 record-hygiene batch (provenance cluster prep)
<!-- L:172 status:OPEN upd:2026-07-29 section:W.Active flag: rice:3/2/95/1 -->
- **What.** Small, independent, unblocked corrections a later session
  would otherwise trust as-is. Bundled as one checklist since none
  individually needs its own future reference:
  1. `MODULE_DOMAIN_MAP` entries for `orrery_rendering.py` and
     `shell_configs.py` (both currently silent-defaulting to `orrery` in
     the domain-coverage-gap report).
  2. Fix the L-157/L-161 swap in
     `HANDOFF_gallery_feature_layer_L154_resume.md` section 3 -- it
     credits the shell-config ring/belt/atmosphere cross-check to
     "L-161"; that work is L-157's.
  3. Carry the 15 -> 14 correction into this ledger's own prose wherever
     "15 remaining bodies" still appears, and into master plan section 6.
     Widen this to the 18/15 figures wherever they appear, not just that
     exact phrase -- two more sites already found and fixed directly
     (L-155, L-162 above); check for others before closing this item.
  4. Reinstall `gallery-assembler` SKILL.md from the repo copy -- installed
     copy carries CRLF line endings (118 confirmed, 0 bare LF),
     byte-identical content otherwise; came from a Windows path that
     bypassed the LF gate.
  5. Correct `MASTER_PLAN_INTERACTIVE_GALLERY.md`'s path in any reused
     prompt template -- it lives at `documentation/MASTER_PLAN_...`, not
     repo root.
**Gap:** all five are mechanical, no design decision needed, no dependency
on Phases A/1/2/3. Land in the same session as L-164 (dep_trace.py ASCII
bytes) -- same shape of work.
**Ref:** `PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md`
Tony-action rollup; L-163; L-164.

#### [L-173] shell_configs.py -- 8 body blocks missing... source citations entirely (found during 1c predesign measurement)
<!-- L:173 status:OPEN upd:2026-07-30 section:W.Active flag: rice:3/3/70/3 -->
What. 1c's predesign measurement (L-156 Gap item 6) surfaced a real, previously-hidden gap, distinct from the lookback-window bug it was measuring: 8 of shell_configs.py's 24 body blocks carry no # Source: citation of any kind. Three of the eight (CUSTOM_SHELLS['Moon'], CUSTOM_SHELLS['Pluto'], CUSTOM_SHELLS['Sun']) contribute zero Tier-1 findings currently and need no immediate action beyond eventual sourcing. The other five carry 18 Tier-1 findings between them:
block	uncited Tier-1 findings
SHELL_CONFIGS['Pluto']	10
SHELL_CONFIGS['Venus']	3
SHELL_CONFIGS['Eris']	2
SHELL_CONFIGS['Mars']	2
CUSTOM_SHELLS['Mercury']	1
These are not scanner artifacts -- 1c's citation-window fix correctly leaves them at Tier 1 (V4 RECALLED), because there is nothing to inherit. They need actual sourcing, not a scanner change.
Note (2026-07-30): 1c built and measured; these 18 findings verified UNTOUCHED
by it. Independently re-derived from the post-patch audit and matching the
predesign table exactly: SHELL_CONFIGS['Pluto'] 10, ['Venus'] 3, ['Eris'] 2,
['Mars'] 2, CUSTOM_SHELLS['Mercury'] 1. All still Tier 1 / V4 RECALLED. 1c's
strict-containment resolver stops at the narrowest containing block and never
searches outward, so these cannot be cleared by a scoring change -- they need
real sourcing. test_citation_inheritance.py carries
test_live_shell_configs_uncited_blocks_still_uncited as a deliberate tripwire:
it fails if any of these five blocks starts inheriting a citation. When L-173
is genuinely resolved that test is EXPECTED to be updated by hand, not
silenced -- the failure is the signal that these blocks changed state.
Gap: candidate for the Phase 4 Gemini worksheet (same channel as L-157/L-161) -- these five blocks are now pre-located and high-confidence, so they can be prioritized in that pass rather than discovered again. Pluto is the largest single target. No design decision needed; this is a citation-sourcing task, not a scoring-model question.

Note (2026-07-30, boundary pinned): L-174 opened for a distinct failure --
citations PRESENT but written one block level too far out. These 18 findings
are the other kind: sources genuinely MISSING. The scanner's new shadowed-
string diagnostic deliberately does not report them (no cited ancestor block
exists), and test_genuinely_uncited_is_not_reported_as_shadowed fails if that
boundary ever blurs. Keeping the two apart matters: a shadowed string needs a
comment moved, an L-173 finding needs a source found.

Ref: PREDESIGN_1c_citation_inheritance.md; L-156 Gap item 6; L-161.

#### [L-175] Newly-visible uncited temperature claims (1d piece 3)
<!-- L:175 status:OPEN upd:2026-07-31 section:W.Active flag: rice:3/3/80/2 -->
What. L-156 Phase 1d piece 3 added temperature units to NUMERIC_CLAIM_RE. This surfaced 96 real uncited temperature claims the scanner was previously blind to -- 61 at Tier 1. Almost all in four paleoclimate modules:
paleoclimate_wet_bulb_full.py (16 -> 51)
paleoclimate_human_origins_full.py (11 -> 32)
paleoclimate_visualization_full.py (7 -> 28)
paleoclimate_dual_scale.py (2 -> 9)
Why track separately. Same pattern as L-173 (shell_configs gaps): these are genuinely uncited claims that need sourcing, not a scoring regression. Tracking separately lets the Tier-1 count read as "132 known + 61 newly visible" rather than as a backslide.
Sourcing path. These modules carry human-cost content (heat deaths, food insecurity) where the earth-system-pipeline skill's restraint discipline applies. That is an argument for sourcing them properly, not for leaving them unseen. Sourcing will likely follow the L-157 Gemini sweep methodology.
Note. "Data Preservation is Climate Action" -- the project's own principle says these claims matter more, not less, than average.
Ref: L-156 Phase 1d piece 3; AS_BUILT_L156_phase1d_e_f.md section 2; L-078(d).

### W.Done -- closed items, kept with the track

#### [L-085] LICENSE to repo root
<!-- L:085 status:DONE upd:2026-07-03 section:W.Done flag: rice:2/2/100/1 -->
- **What.** The MIT license file lives at `documentation/LICENSE.md` where GitHub
  cannot find it. The repo page shows no license badge; tooling reads the project
  as unlicensed. Move or copy to repo root.
- **Copyright year conflict.** The file says Copyright (c) 2024; README says
  (c) 2025-2026. Harmonize when moving.
- **Why now.** Cheapest half of the wide-release gate. The license choice already
  exists; this makes the existing claim true in form.
**Gap:** move file, harmonize year, verify badge appears. One commit.
**Ref:** Fable 5 survey (Front 2), master plan S6.
**Tony:** Done.

#### [L-088] Gallery integration test (Phase 0)
<!-- L:088 status:DONE upd:2026-07-06 section:W.Done flag: rice:2/2/100/1 -->
- **What.** One-sided Pyodide test in the gallery. Proves the stack: Python
  computation in the browser on a static GitHub Pages site.
- **Done.** `interactive.html` deployed to `palomasorrery.com/interactive.html`
  (created `300ac30c`, updated `a85a4fa`, July 6, 2026). Pyodide v314.0.2 +
  NumPy computing Keplerian orbits from mean orbital elements, rendered by
  Plotly.js. Tested on desktop Chrome and iPhone Safari. Consent gate for
  first-time visitors (localStorage persistence). ~4-10 second load time,
  cached after first visit. Server/serverless resolved: Pyodide.
- **A/B fork resolved: B'.** `measure_plotly.html` timed full plotly-in-Pyodide
  cold-start on iPhone Safari WiFi: **2.1-3.3 s** (acceptance <=15 s -- passed at
  one-seventh). `import plotly.graph_objects` = 57-59 ms. Fable's convention-
  duplication analysis confirmed A's parallel-pipeline cost exceeds B''s cold-
  start cost for a solo developer. B' uses slim self-hosted wheel (~3.9 MB).
  Two-tier model: frozen A exhibits (instant) + data-backed B' exhibits
  (shared engines, one codebase). Phase 0 closed.
- **Supersedes:** Two-sided pilot (Dash vs Pyodide), matplotlib question -- both
  dissolved by the v8 architectural pivot.
- **Attribution gate (L-086):** Publicly reachable with inline "Data: JPL/NASA"
  credit. Ruled sufficient pending L-086.
**Ref:** Master plan v9 section 5 Phase 0; gallery @ `4b086a6`.

#### [L-098] Data serving pipeline (Phase 1b)
<!-- L:098 status:DONE upd:2026-07-12 section:W.Done flag: rice:3/3/50/3 -->
- **What.** Serve solar-system orbits to the browser gallery: osculating
  elements (the orbit) + direct-frame position vectors (the actual-motion
  trace), plus a coverage index the browser reads. Goal unchanged since v0.3;
  the DATA SOURCE pivoted (trail below).

- **Trail (how the design got here).**
  - v0.3 design converged July 7 (Fable 5 broad analysis -> Opus 4.8 review ->
    Opus 4.6 convergence + Tony): coverage-index schema, a 9-object test tranche
    covering every pattern, 8 invariants. Design handoff v0.6. Legacy
    orbit_paths.json gitignored in the orrery @ 6368c87.
  - v4 model correction (July 8, Opus 4.8): the subtraction model (derive a
    moon's frame by differencing heliocentric ephemerides) was RETIRED --
    empirically rejected on the desktop (catastrophic cancellation + daily
    aliasing), confirmed against idealized_orbits.py (osculating-only satellite
    systems, barycenter mode). Product model INVERTED: osculating is the PRIMARY
    orbit; direct relative-frame pairs are the SECONDARY trace, served where
    cadence allows. Coverage index reconciled to v0.6 (field-verified;
    cache-required + invariants #1/#4/#7 retired; barycenter-relative frame
    added; Pluto/Charon in the barycenter frame per Tony). Manifest v4 +
    PHASE1B_MODEL_CORRECTION_HANDOFF.
  - Stage 2 build + the finding that forced the pivot (July 8): export_orbit_
    cache.py (Steps 0-6) built, pre-tested, and RUN on the primary. B2 (schema)
    PASSED; B3 caught frame CONTAMINATION in the served Charon/Pluto traces --
    heliocentric points (~35 AU) mixed with correct barycentric points under a
    barycenter key, from a fetch predating the @9 override. The desktop is
    immune (draws orbits from osculating, not traces); the gallery is EXPOSED
    (serves the raw traces). merge_orbit_data merges by date with NO frame
    check, and the extent across 1501 legacy entries is unknowable. Added a
    magnitude frame guard (#F): a relative-frame trace exceeding 0.5 AU drops to
    osculating-only. Test record: PHASE1B_STAGE2_TEST_PROTOCOL.
  - v2 + v3 convergence (July 8, Opus 4.8 + Fable 5): Fable broad-first review
    [verdict: BUILD IT] integrated -- Guard v2 (per-object band k*a(1+e) replaces
    the global 0.5 AU; a real moon, Neso, apoapsis 0.572 AU proved the constant
    false-rejects), provisional leading edge (nightly overwrite [today-7d,
    +horizon]; freeze the older past), raw/served split (dissolves git-growth),
    nightly atomicity (staging -> validate -> atomic swap -> single commit ->
    per-object isolation -> git rollback -> size tripwire -> "data as of"
    staleness). Then the TRACE & CONIC MODEL converged + code-verified @cde22c5:
    every object serves osculating elements + orbit_type + as-of-today point;
    conic is two-case (elliptical 360-pt / hyperbolic near-perihelion arc);
    comets anchor the conic at Tp; spacecraft get a full-arc daily trace. Two-
    surface principle: interactive = generative-lite, gallery = curated full-
    fidelity, bridged by the closest-point event_link. Handoff -> v0.3.

- **Current direction: GALLERY DATA-SOURCE PIVOT (July 8).** Stop reading the
  legacy desktop cache for the gallery. Build a clean, purpose-built gallery
  cache by FETCHING FRESH from Horizons with the correct center per object,
  stored in the GALLERY repo (separate-clean from the orrery), refreshed by a
  NIGHTLY BATCH, validated on write by the #F guard promoted SOURCE-side so
  contamination cannot enter by construction. Legacy cache untouched (desktop).
  Standalone builder (astroquery, no orrery import) makes "where it runs
  nightly" a scheduler detail, not an architecture fork.
  Design handoff: GALLERY_DATA_SOURCE_HANDOFF.

- **Carries forward from Stage 2 (only the SOURCE changes):** the v4 osculating-
  primary model; the coverage-index + position-file schema (v0.6-reconciled);
  invariants #2/#3/#5/#6/#8/#C + the #F guard; center-slug map, epoch parser
  (HH:MM), JD convention. export_orbit_cache.py's derive/serve half is reused in
  the new builder; its "read the legacy cache" input is retired.

- **v0.4 convergence review + ratification (July 9, Opus 4.8 + Tony).** Opus 4.8
  verified manifest v1 against the LIVE repo (SHA round trip, ghost purge,
  copy-source citations, manifest-vs-v0.3 fidelity) and corrected two false-
  negative flags (F2: both the perihelion DISPATCHER `_add_perihelion_osculating_
  orbit` @palomas_orrery.py:1533 AND the LEAF `plot_perihelion_osculating_orbit`
  @io:7089 exist -- copy the leaf; F7: 2029-12-12 WAS in v0.3), then walked the
  decision docket with Tony. Resolved/ratified: comet Tp path corrected to the
  two-role SOLUTION-Tp-locates / converged-osculating-Tp-anchors resolution (the
  solution-vs-converged residual is the non-grav/outgassing shift; adds
  resolve_tp/fetch_solution_tp to copy sources); Encke ADDED to the seed (11 rows)
  to exercise it; spacecraft REDESIGNED (Tony) to fetch the flown arc ONCE +
  append today NIGHTLY -- retires write-once, the 2029 SPK horizon, and
  --refresh-spacecraft as load-bearing; ephemeris START discovered from Horizons,
  not launch+1; Guard v2 -> MONITOR (warn on both bounds, not reject -- defense-in-
  depth, not the guarantee; loud diagnostic warning required); shrink gate
  point-count 95%; horizon=0 non-spacecraft; elements JSONL history. NEW: gallery-
  cache backup discipline (L-106). Manifest -> v2; handoff -> v0.4.

- **Phase 1b build (July 9, Opus 4.8 + Tony, warm-context continuation).** Built
  the standalone builder in one session off the converged v2/v0.4: tools/
  gallery_cache_builder.py + data/solar-system/objects_config.json (11-row seed)
  + an offline mocked-Horizons smoke test. Pre-tested: py_compile clean, 47
  checks / 0 failures, ASCII-clean; every copied specific carries provenance to
  orrery 4e2629c. Grounding surfaced as-built deltas (recorded in the BUILD
  handoff): served schema is the FULL v0.6 shape, not manifest S6's shorthand
  (schema parity to export_orbit_cache.py); trace_policy is MODEL-derived, NOT
  carried from TEST_OBJECTS's retired serve/none field; the comet resolver is
  adapted to Path-2-only (no shared cache) + nightly re-resolve; a coarse #U
  unit-sanity ABORT was added, distinct from the Guard monitor. Live gate
  (Horizons dry-runs, Mode-5 Tp match) is Tony's -- unreachable from the build
  container. Copy-provenance sync register -> L-107; master-plan drift -> L-108.

**Tony:** fetch-fresh + nightly batch + gallery-repo cache + ~1yr back ratified
(Fable-confirmed). Builder choices CONVERGED: (1) intermediate raw cache; (2)
desktop-scheduled now, Action later (probe Actions early); (3) daily cadence +
PROVISIONAL leading edge + raw/served split -- git-growth fine with a ~800 MB
size tripwire (no LFS/squash); (4) object-list config = single authority,
tranche-first. Guard v2 gates catalog growth. OPEN, Tony's call (own pass): the
shells interactive-vs-gallery split (L-100).

**Gap:** Ghost purge DONE (9febac5; both trees absent from HEAD + gitignored).
Manifest v2 / handoff v0.4 converged (Opus 4.8 + Tony, July 9). BUILDER BUILT +
OFFLINE-VERIFIED (July 9): tools/gallery_cache_builder.py + objects_config.json
(11-row seed) + offline smoke test; py_compile clean, 47 checks / 0 failures,
provenance to orrery 4e2629c. .gitignore add (in-tree .staging/ + backup/) is a
3-line snippet. NEXT = LIVE gate on Tony's hardware in manifest S10 order:
--dry-run voyager_1 (ephemeris start discovered) + encke (solution-Tp/2P +
Mode-5 Tp match vs desktop resolve_tp); inject an out-of-band point to see the
Guard banner fire; confirm the backup action + .gitignore exist BEFORE first
build (L-106); first full build; schedule nightly + the separate backup action.
The offline pass is NOT live verification -- the first --dry-run is the
authoritative render. Legacy-
cache Stage 2 deploy SUPERSEDED. Deferred: Pluto-Charon relative subsystem;
sub-daily moon traces; Phase 2 wide-view composition (the np.interp containment
hazard returns then).

**Spawned items (this session):** L-100 shells surface (open question);
L-101 osculating-history fan; L-102 spacecraft thinning; L-103 hyperbolic
browser branch; L-104 Gallery Studio preset generator; L-105 merge_orbit_data
desktop-cache frame guard. Later (July 9): L-106 gallery-cache backup + gitignore;
L-107 copy-provenance sync register; L-108 master-plan v11 reconciliation.

**Ref:** GALLERY_DATA_SOURCE_HANDOFF.md v0.4 (amends v0.3); GALLERY_BUILDER_MANIFEST v2 (v1 Fable 5 -> v2 Opus 4.8 review + Tony); GALLERY_BUILD_HANDOFF v0.1 (as-built); tools/gallery_cache_builder.py + data/solar-system/objects_config.json + tools/test_gallery_cache_builder_offline.py; FABLE5_REVIEW_gallery_data_source_pivot.md;
PHASE1B_STAGE2_TEST_PROTOCOL.md; PHASE1B_BUILD_MANIFEST_v4.md;
PHASE1B_MODEL_CORRECTION_HANDOFF.md; PHASE1B_DATA_SERVING_DESIGN_HANDOFF.md
v0.6; DATA_SERVING_BROAD_ANALYSIS.md; export_orbit_cache.py; L-078 (ROLE_MAP);
master plan v10 section 3a, section 5 Phase 1b.
**Note:** Closed 2026-07-12: builder built,
offline-verified (75/0 clean clone), live-gated 2026-07-11, deployed to gallery
data/solar-system/, backup covered (L-106). Children: L-102/L-113 (thinning,
deferred), L-107 (provenance register), L-111 (unattended-nightly, follow-on).
**Gap:** none -- move to section C

#### [L-099] Solar System Explorer interactive exhibit
<!-- L:099 status:DONE upd:2026-07-06 section:W.Done flag: rice:2/2/80/1 -->
- **What.** First interactive exhibit in the gallery. Pyodide + NumPy computes
  Keplerian orbits from mean orbital elements; Plotly.js renders 3D figure.
  Planet toggles, date picker, info panel, consent gate.
- **Done.** `interactive.html` deployed to `palomasorrery.com/interactive.html`
  (created `300ac30c`, updated `a85a4fa`, July 6, 2026). Tested on desktop
  Chrome and iPhone Safari. Consent gate explains Pyodide with explicit opt-in
  (localStorage persistence). Gallery dark-space aesthetic, Cormorant Garamond
  + DM Sans fonts, mobile-responsive.
- **Architecture.** Architecture A (lightweight): Python/NumPy computes orbit
  geometry, JavaScript builds Plotly traces, `Plotly.newPlot()` renders.
  No plotly Python package in Pyodide. Frozen as an "instant tier" exhibit
  under the two-tier model (A/B fork resolved: B' for Phase 2+ data-backed
  exhibits, A retained for frozen pedagogical demos). Option C viewer
  (master plan section 2a): `index.html` serves curated cards; `interactive.html`
  serves interactive exhibits via `?exhibit=` parameter (hardcoded in v1).
- **Next iteration:** Plot refinements (Mercury color contrast, scale presets,
  outer planet zoom, additional controls).
**Ref:** Master plan v10 section 2a, section 5 Phase 0; gallery @ `a85a4fa`.

#### [L-118] feature_configs.json served empty every build (F1, gates artifact 2)
<!-- L:118 status:DONE upd:2026-07-21 section:W.Done flag: rice:3/3/90/1 -->
- **What.** `derive_served` (gallery_cache_builder.py, line ~749-750) writes
  `feature_configs.json` unconditionally empty
  (`{'schema_version': ..., 'features': {}}`) into staging on every build.
  `data/solar-system/` is replaced wholesale by the atomic swap, so any
  feature-renderer params (shell radii, colors, ring geometry) placed in
  the served file are silently destroyed by the next nightly. Same failure
  class as L-114 (a producer inside the swap blast radius), one file over
  -- the swap doesn't strand it here, the builder just never populates it.
- **Config shape: DECIDED, inline.** Feature params move OUTSIDE the blast
  radius into `objects_config.json`, per-object, alongside the existing
  `features: [...]` dispatch-key list (which becomes a dict keyed by
  feature name, each value carrying that feature's params) -- not a
  sibling file. Rationale (Tony, 2026-07-15): a sibling file is the exact
  two-files-must-stay-in-sync failure shape behind L-114 and the Halley
  offline-suite miss; one file removes that class of drift by
  construction. `derive_served` then DERIVES `feature_configs.json` from
  config instead of writing it empty. `served_window` population
  (currently `null`) rides along in the same change (manifest deviation 2
  / as-built S8).
- **Values are PORTED, not hand-authored.** [Correction, 2026-07-15] The
  feature params are not new data to invent -- they already exist,
  provenance-audited, in the desktop codebase:
  - **Simple sphere shells** (e.g. Earth's `atmosphere_shell`): a direct
    numeric port from `SHELL_CONFIGS['Earth']['atmosphere']` /
    `['upper_atmosphere']` in `shell_configs.py` (`radius_fraction`,
    `color`, `opacity` -- April 2026 provenance audit, NOAA/NASA sourced).
    Nothing to invent; copy the numbers.
  - **Custom-geometry shells** (e.g. Earth's `van_allen_belts`): the
    params exist too (`CUSTOM_SHELLS['Earth']['magnetosphere']` ->
    `earth_visualization_shells.create_earth_magnetosphere_shell`: inner
    belt 1.5 R_E, outer 4.5 R_E, thickness 0.5 R_E, NASA Van Allen Probes
    sourced) but the belts are generated PROCEDURALLY (5 rings x 80
    points, sinusoidal z-flattening `z = 0.2*radius*sin(2*angle)`), not a
    static radius pair. Porting this feature means porting the small
    generation algorithm to JS alongside its params, not just three
    numbers. (The belts themselves don't depend on Sun position --
    `needs_sun_position` on that builder is for the magnetosphere/bow-shock
    traces in the same function, not the belts.) This distinction will
    recur for rings and comet comae/tails later -- budget custom-geometry
    features as algorithm ports, simple shells as data ports.
- **Verified live 2026-07-15** [verified @953c650e/@73c67bed]:
  `feature_configs.json` still `{"features": {}}`; `served_window` still
  `null`. Nothing has drifted since the artifact-1 as-built was written.
- **Claude:** [verified @c5c9ea09, 2026-07-21] The 2026-07-15 "still empty" note is
  stale, superseded by this run. Live --first-build output confirms feature_configs.json
  now derives from objects_config.json as designed -- earth/jupiter/saturn populated
  with the ported shell_configs.py/CUSTOM_SHELLS values, the other 9 objects correctly
  {}. Layer-1's M1 shape-validator checks all still pass (138/138 at HEAD). served_window
  is also populated now, but via the separate M2 trust system (L-149/L-150/L-151), not
  literally "the same change" as originally scoped here. 
- **Naming caution.** The gallery-cache-builder skill's field notes use "F1"
  for a DIFFERENT, already-closed issue (L-114's config-path stranding). This
  L-118 is the Phase 2 synthesis manifest's F1 (feature_configs.json
  empty-write trap). Unrelated to L-114; do not conflate when grepping "F1".
**Tony:** Done.
**Claude:** [verified @af3a2c86, 2026-07-21] --nightly ran clean: 12 objects, no
  ABORT, feature_configs.json and served_window both survived the refresh intact.
  All 5 Gap items closed.
**Gap:** items 1-5 of the original 5 are done. 
**Ref:** gallery `tools/gallery_cache_builder.py` (`derive_served` ~line
710-751); `data/objects_config.json`; `data/solar-system/feature_configs.json`;
orrery `shell_configs.py` (`SHELL_CONFIGS`/`CUSTOM_SHELLS`, Earth block);
orrery `earth_visualization_shells.py` (`create_earth_magnetosphere_shell`);
PHASE2_SYNTHESIS_MANIFEST_v2.md S4/S9; PHASE2_ARTIFACT1_AS_BUILT.md S8/S9;
L-098 (parent, Phase 1b); L-114 (related but distinct -- see naming caution);
L-123 (info card, rides with this). L-149 (served_window ended up here, not in this item's own code)

#### [L-148] Staging folder names carry no object identifier -- hard to locate manually (gallery-cache-builder)
<!-- L:148 status:DONE upd:2026-07-20 section:W.Done flag: rice:1/2/90/1 -->
- **What.** run_build's staging dir name is `.staging_<out_dir.name>_<run_id>` -- timestamp
  only, no object slug -- even for a single-object `--dry-run --object <slug>` run. Surfaced
  during M2 Layer 2 manual verification (L-118): finding one object's trust block after a
  dry-run means sorting File Explorer by date and guessing which .staging_solar-system_*
  folder is the right one. Tony, mid-test: "with 11 objects it's hard, with all the objects
  extremely hard."
- **Proposed fix (not built, flagging only):** when only_slug is set, fold the slug into the
  staging dirname, e.g. `.staging_solar-system_earth_<run_id>`. Multi-object runs
  (--first-build/--nightly) keep the timestamp-only name -- no single object to name it after.
**Note:** small, isolated change (one f-string in run_build's staging= line, ~1289).
_sweep_siblings' glob (`.staging_%s_*` % out_dir.name) still prefix-matches the new shape
unchanged -- no consumer break expected, worth a quick confirm before landing. Not yet
RICE-scored.
**Gap:** add slug to staging dirname when only_slug is set; confirm _sweep_siblings still
reaps it; Layer 1 offline-suite check if any test asserts the exact staging dirname shape.
**Ref:** gallery tools/gallery_cache_builder.py run_build (staging=... ~line 1289);
_sweep_siblings; L-118 (parent -- discovered during its Layer 2 acceptance).

#### [L-149] Global served_window trust participation should key off canonical_frame, not category (gallery-cache-builder)
<!-- L:149 status:DONE upd:2026-07-21 section:W.Done flag: rice:2/2/60/2 -->
- **What.** TRUST_WINDOW_EXCLUDED_CATEGORIES = {'moon', 'spacecraft'} excludes by category
  label. Surfaced during M2 Layer 2 (L-118): Pluto (dwarf_planet) is centered on
  pluto_barycenter -- same physical situation as Charon (moon), same barycenter -- but isn't
  excluded, so Pluto's real ~6.4-day mutual-orbit window becomes the GLOBAL served_window's
  controlling bound. resolver.py's resolve() checks served_window as one gate for the whole
  scene regardless of which objects are requested -- confirmed live -- so this would reject
  e.g. "Jupiter, 10 days out" even though Jupiter's own window is ~4,336 days.
- **Decided (Tony, 2026-07-20):** exclude by canonical_frame != 'heliocentric', not category.
  Generalizes to future barycenter-relative onboards -- Orcus/Vanth (20090482/920090482/
  120090482) and Patroclus/Menoetius (20000617/920000617/120000617) both confirmed live as
  real Horizons system-barycenter IDs, the general 20XXXXXX pattern, distinct from Pluto's
  legacy single-digit @9.
- **Claude:** [verified @c5c9ea09, 2026-07-21] The canonical_frame fix is live and
  proven on real data, not just the mock. Code: derive_served's participant loop now
  checks `canonical_frame != TRUST_WINDOW_PARTICIPANT_FRAME` ('heliocentric'), replacing
  the old category check. Layer-1: 4 new L-149-specific checks added and passing
  (138/138 total) -- including a forced-failure test proving pluto's own check-vector
  outage can no longer null the global served_window, since it's excluded from voting.
  Layer 2 Step 2 (--first-build): served_window's half-width (323.5468 d) matches
  Apophis's window_days exactly -- Apophis controls, not Pluto. Pluto (~6.38 d) and
  Charon (~0.80 d) still get full trust blocks but correctly take no part in the
  global bound.  
- **Claude:** [verified @af3a2c86, 2026-07-21] --nightly confirms the fix holds across
  a refresh, not just first-build: served_window re-centered on the new as_of time
  while its half-width stayed correctly pinned to Apophis (heliocentric), not Pluto.
  Gap fully closed.
**Gap:** code fix, Layer-1 update, and Layer 2 Step 2 are all done and verified live.
Only Step 3 (--nightly) done -- same run that closes L-118's own remaining gap.
**Ref:** gallery tools/gallery_cache_builder.py derive_served (~1023-1048),
TRUST_WINDOW_PARTICIPANT_FRAME (~360, replaces the retired TRUST_WINDOW_EXCLUDED_CATEGORIES);
resolver.py resolve() (~91-106); data/objects_config.json; L-118 (parent);
M2_TESTING_PROTOCOL_ADDENDUM.md (Layer 2 steps).

#### [L-152] ledger-and-session-records skill bumped to 1.2 -- retroactive ledger entry
<!-- L:152 status:DONE upd:2026-07-20 section:W.Done flag: rice:1/1/95/0.5 -->
- **What.** ledger-and-session-records was updated to v1.2 (cut at orrery @
  079a0ec5c6a72f83fa7904e469cd359912746221, July 19, 2026) -- generalized
  "Handoff Structure" into a shared "Anchor Requirement (all outbound
  documents)" covering handoffs, manifests, as-builts, review requests, and
  Mode-7 relay prompts under one built on <SHA> at <URL> format, plus a new
  "The Document Stack" section. No ledger entry was written at the time --
  this entry closes that gap per the protocol's own convention.
- **Note:** discovered via version drift -- the resident protocol's Skill
  Manifest still showed 1.0 while the repo was at 1.2, and a Claude draft
  this session nearly re-generalized something already generalized, before
  the mismatch was caught. Skill version drift is a real failure class,
  same shape as an unpushed SHA.
**Gap:** none -- documentation only. Skill Manifest table bumped to 1.2 alongside.
**Note (2026-07-28, addendum):** Same gap recurred twice more, closing
both here rather than opening new handles for what's the same tracked
fact (this skill's version history). **v1.3** [cut @ae803766, July 24
2026]: adds the Tony-action (do)/(decide) tag convention and its rollup
rule, surfaced during the L-163 build-prep session when a builder
session had to hunt Tony-only to-dos scattered through a handoff with
no consistent tag. **v1.4** [cut @ca9c706e, July 26 2026]: rewrites the
Codebase Tooling ROLE_MAP bullet for L-163 Phase 3 -- a new module is
now classified by tagging its own docstring, not by hand-adding a
ROLE_MAP entry, since ROLE_MAP became a regenerated mirror. Both were
already self-documented in the skill file's own header changelog; nothing
factual was missing, just this ledger-side pointer.
**Ref:** skills/ledger-and-session-records/SKILL.md @ 1.2; L-149/L-150/L-151.

#### [L-120] Halley configured but not yet in the served index (F3, gates artifact 4)
<!-- L:120 status:DONE upd:2026-07-27 section:W.Done flag: rice:2/2/95/0.5 -->
- **What.** `objects_config.json` has 12 objects (Halley included, pinned to
  record `90000030`); the live `coverage_index.json` has 11 -- no `halley` key
  (the index predates the config addition). No code change needed: the
  offline suite already asserts 12 and has Halley-specific mock checks (Layer
  1 is consistent with config already). What's missing is the Layer-2
  `--first-build` run on Tony's hardware.
- **Verified live 2026-07-15** [verified @953c650e]: served index objects =
  earth, jupiter, saturn, moon, io, titan, pluto, charon, apophis, voyager_1,
  encke -- no halley.
**Tony:** RICE proposed 2/2/95/0.5 (no code change, just a build run; high
confidence since Layer 1 already passes with 12) -- yours to finalize.
**Gap:** run `--first-build` (not `--nightly` -- a new non-spacecraft object
needs the full 365-day backfill window + the N3 floor check, per
gallery-cache-builder skill). Prerequisite for any Halley render (artifact 4)
and for L-119/F2's Halley-first event_link.
**Ref:** `data/objects_config.json`; `data/solar-system/coverage_index.json`;
gallery-cache-builder skill ("Adding a new object" section); L-098 (parent).
**Closed 2026-07-27:** confirmed at gallery HEAD `0f8e62e` -- `halley` and
`encke` are both in `coverage_index.json`'s 12 served objects, with
`served_window` populated (not null). Tony (2026-07-27): "probably we can
close. we have not done any mode 5 checks yet in the interactive
development, except for earth. all are procedural so far. artifact 4 is
the render" -- the Halley visual/Mode-5 check belongs to Artifact 4's own
build, not to this item, which was only ever about the object being
served. Closing outright, no residual carried forward.

#### [L-151] Create gallery-assembler skill -- technical home for the new-mechanism assembler
<!-- L:151 status:DONE upd:2026-07-27 section:W.Done flag: rice:?/?/?/? -->
- **What.** No skill documents the assembler itself -- render_orbits.py, resolver.py,
  cache_reader.py, Kepler propagation, the trust/served_window system, the golden-artifact
  build+Mode-5 process. gallery-cache-builder covers only the nightly builder/staging/
  serving-cache side; gallery-pipeline covers the older Studio/converter/viewer curation
  chain. Neither is the right home for "how the new mechanism itself works."
- **Decided (Tony, 2026-07-20):** create gallery-assembler as that home.
- **Must carry, once written (corrected tonight, not the first-pass framing):**
  - Orrery-vs-assembler boundary: shared knowledge, not shared machinery (see master plan section 3).
  - No composition between frames -- retired by design (v4, catastrophic cancellation +
    aliasing). Each orbit is an independent fetch at its own center; a binary pair needing
    two views means two independent caches, never one derived from the other.
  - render_orbits.py's Kepler math is frame-agnostic and fine as-is; the open question is at
    scene/artifact assembly -- does it know which of an object's caches belongs in which view.
  - Orrery-first authoring rule, with Encke as the confirmed, deliberate exception.
**Gap:** write the skill; migrate the field notes above into it; add fires_when to the
Skill Manifest.
**Ref:** L-149, L-150 (motivating work); master plan section 3; render_orbits.py, resolver.py,
cache_reader.py.

#### [L-087] palomas_orrery_helpers.py computation/GUI split
<!-- L:087 status:DONE upd:2026-07-15 section:W.Done flag: rice:2/2/75/1.5 -->
- **What.** `palomas_orrery_helpers.py` imported tkinter directly (tk, ttk,
  messagebox, scrolledtext, lines 19-22) alongside three computation functions
  the assembler needed: `calculate_planet9_position_on_orbit` (@217),
  `rotate_points2` (@265), `calculate_axis_range` (@313).
- **Finding, not a design decision.** Grepped the full 913-line file for
  `tk.`/`ttk.`/`messagebox.`/`scrolledtext.` usage: zero matches anywhere in
  any function body. The four import lines were dead code, not a real split
  question. Confirmed from both directions: the sole consumer,
  `palomas_orrery.py`, imports exactly the 11 real functions the module
  defines, none of them tkinter names.
- **Resolution:** Tony deleted the four dead import lines directly (no split,
  no lazy-import needed). File is now 909 lines, zero tkinter references --
  independently reverified multiple times, including in Opus 4.8's artifact-1
  as-built (Phase 2 assembler build, 2026-07-14).
- **Done alongside L-026** (CRLF to LF, same file, same session).
**Ref:** Fable 5 review of v2 (finding 3), master plan S2/S6; Phase 2 handoff
v0.2 S6 (verification); PHASE2_ARTIFACT1_AS_BUILT.md (re-confirmation).

#### [L-170] Tier-1 exit-code flip -- capture so it doesn't float
<!-- L:170 status:DONE upd:2026-07-29 section:W.Done flag: rice:2/2/90/0.5 -->
- **What.** D7 (`DESIGN_HANDOFF_provenance_scoring_and_pinning.md`) wired
  the Tier-1 nonzero exit code but switched it off, "recorded as its own
  small ledger item so the flip doesn't float." It floated -- no such item
  existed until this one. The console banner ships with Phase 1; the
  exit-code flip itself is a one-line change, thrown the first time a live
  run reaches Tier-1 = 0.
**RETIRED (2026-07-29, Tony):** this is exactly the mechanism
`DESIGN_REVIEW_provenance_scoring_and_pinning.md` section 3c already
rejected -- titled, verbatim, "D7 -- Tier-1 never gets an auto-exit gate
(supersedes the deferred-flip recommendation)." The amendment: "Tier-1
gets a permanent, prominent banner and never an auto-exit gate, at any
threshold, ever" -- a count-based trigger (zero-hit, or the ratchet
alternative, also considered and also rejected) judges by a number
instead of by what the findings actually are, the same flaw D1 already
corrected one level down (criticality by volume, not by type). This item
was opened from a reading of the original D7 recommendation without
cross-checking that the review had already superseded it -- caught on a
later audit pass, before anything was built. No mechanism to build; the
permanent banner (already scoped into Phase 1 elsewhere) is the design as
it actually stands.
**Gap:** none -- move to section C.
**Ref:** `DESIGN_HANDOFF_provenance_scoring_and_pinning.md` D7 (original,
superseded); `DESIGN_REVIEW_provenance_scoring_and_pinning.md` section 3c
(the amendment that actually governs); L-156 (Phase 1, the permanent
banner this item mistakenly proposed replacing with an exit gate).

#### [L-162] CENTER_BODY_RADII full de-duplication -- dedicated Sonnet session
<!-- L:162 status:DONE upd:2026-07-29 section:W.Done flag: rice:3/3/90/1 -->
- **What.** Promote all 15 remaining `CENTER_BODY_RADII` bodies (Mercury,
  Venus, Moon, Mars, Phobos, Saturn, Uranus, Neptune, Pluto, Bennu, Eris,
  Haumea, Makemake, Arrokoth) to named module-level constants in
  `constants_new.py`, each keeping its existing citation. **Excludes
  Planet 9** (model estimate, never directly observed -- carries to L-159
  instead).
- **Confirmed 2026-07-27 (Sonnet 5, live HEAD): not started.** Only
  Sun/Earth/Jupiter are named; `CENTER_BODY_RADII` still hardcodes all
  three as raw literals (695700, 6378.137, 71492) rather than referencing
  the names -- so even the original 3-body-minimum hasn't landed. Every
  dict entry does carry a good inline citation already; that's not what's
  missing. What's missing is promotion to its own named constant so each
  body scores as its own scanner row instead of one undifferentiated dict.
- **Why now, not "eventually":** simplifies L-155's Phase 3 pinning engine
  -- pins against all 17 named constants directly. Planet 9's pinning
  exclusion (decided; master plan section 6) means zero dict-path AST
  extraction remains, not 15 -- simpler than originally scoped. D3 is
  closed (see L-156), so nothing about
  this item's timing depends on it any more -- it can run whenever a
  dedicated session is free.
**Note (2026-07-29, decided by Tony):** Both scope gaps from
`HANDOFF_L162_scope_gaps.md` resolved. (1) Naming: plain form
(`MARS_RADIUS_KM`), not type-labeled -- matches the 12 existing live
aliases in `planet_visualization_utilities.py` and `CONCEPT_ALIASES`'s own
canonical-key convention. (2) Ownership: this item owns the
Sun/Earth/Jupiter literal-duplication fix in the same edit -- `L-156`'s Gap
line stands as written, needs no tightening. (3) Alias layer: re-point
`planet_visualization_utilities.py`'s 12 existing aliases
(`MARS_RADIUS_KM = CENTER_BODY_RADII['Mars']`, etc.) to import directly
from `constants_new.py` instead, explicitly superseding the unrecorded
"v3.20 Option B" comment (grepped: appears nowhere else in the repo or
ledger). Without this, 12 same-named cross-file pairs land invisible to
`find_cross_file_issues()`'s `CONCEPT_ALIASES` lookup -- L-162 would
silently recreate the duplication problem it exists to fix.
**Correction:** "15 remaining bodies" reads 14 everywhere in prior docs (18
dict keys - 3 done - Planet 9 excluded = 14); the named list was always
right, only the count label was off by one.
**Gap:** dedicated Sonnet-class session, Phase A (per
`PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md` Phase A):
(1) 14 new plain-form named constants in `constants_new.py`, each keeping
its existing citation; (2) rewire `CENTER_BODY_RADII` to reference all 17
names (Sun/Earth/Jupiter included); (3) re-point
`planet_visualization_utilities.py`'s 12 aliases to import from
`constants_new.py`; (4) add `CONCEPT_ALIASES` entries for all 14 new names
-- hard requirement, not optional; (5) pre-flight grep for f-string
formatting of `CENTER_BODY_RADII[...]` (Sun/Jupiter values change int ->
float); (6) `py_compile` + ASCII/LF gate + credit line + as-built anchored
to push SHA. Must land before Phase 3 (pinning engine). Independent of
Phase 0 and Phase 1.
**Ref:** `constants_new.py`; `planet_visualization_utilities.py`;
`DESIGN_REVIEW_provenance_scoring_and_pinning.md` section 3a;
`HANDOFF_L162_scope_gaps.md`;
`PRELIM_DESIGN_HANDOFF_provenance_cluster_completion_part2.md` Phase A;
L-155; L-156; L-159 (Planet 9 case).
**As-built (2026-07-29, Sonnet 5):** Built and verified against
`90d022e`. All 6 Gap items landed: 14 named constants, `CENTER_BODY_RADII`
rewired to all 17 names, 9 aliases re-pointed in
`planet_visualization_utilities.py`, 14 `CONCEPT_ALIASES` entries added,
pre-flight int/float check done (Sun + Jupiter only, no consumer at
risk), `py_compile` + ASCII/LF clean. `test_constants_provenance.py`:
73/73 passed. Scanner re-run: 764 -> 778 findings (+14, exactly the new
constants), Tier 1 unchanged at 145, zero new inconsistencies. Full
diffs: `AS_BUILT_L162_phaseA.md` + three `.patch` files. Ready to push;
credit lines added to `constants_new.py`, `planet_visualization_utilities.py`,
`provenance_scanner.py`.

---

#### [L-174] Citation level mismatch -- citations pitched one block too far out
<!-- L:174 status:DONE upd:2026-07-30 section:W.Done flag: rice:2/3/90/2 -->

What. Phase 1c (L-156 Gap item 6) resolves a display string's citation by
structural containment: the string inherits from the NARROWEST dict block
containing it, and an uncited block inherits nothing. The strictness is
deliberate -- outward search would silently clear the genuinely uncited blocks
tracked as L-173. The cost is that a citation written one level further out
than the resolver reads is invisible to it.

The generalization, which predicts both the successes and the failures: a
citation must sit at the SAME DEPTH as the narrowest block the table records.
build_citation_block_table records depth 1 (the assignment) and depth 2 (its
direct dict-valued entries), and nothing deeper. shell_configs.py works
because its citations sit at depth 2 and its strings at depth 3, so the
narrowest recorded block is the cited depth-2 entry. jupiter_visualization_
shells.py's ring_params failed because its citation sits at depth 1 while its
strings sit inside depth-2 blocks -- four uncited per-ring dicts shadowing a
citation meant to cover all of them.

How found. Surfaced by a session investigating why line 959 was still Tier 1
after the ring_params citation was reworded to drop the "Scope of the above
citation:" marker (0fd7cf1 -> 4844044). Root cause diagnosis verified
independently at HEAD: all four ring entry blocks uncited, resolver returns
None for all four, SCOPE_DECLARED_BLOCKS empty so the scope-decline is not the
blocker, Tier 1 confirmed still 133.

Repo-wide sweep, verified independently. Four dicts carry the shape (a cited
assignment whose dict-valued entries have no citation of their own):

  jupiter_visualization_shells.py  ring_params            4 entries,  1 LIVE
  comet_visualization_shells.py    HISTORICAL_TAIL_DATA  15 entries,  0 live
  planet_visualization_utilities.py PLANET_ROTATION      11 entries,  0 live
  idealized_orbits.py              planet_poles          11 entries,  0 live

CORRECTION to the reporting session's figures, verified line by line:
HISTORICAL_TAIL_DATA has 15 dict-valued entries, not 13 (2 already cited);
planet_poles has 11, not 6 (5 already cited). More importantly, the claim that
comet_visualization_shells.py has LIVE impact does not hold. Howell (line 294)
and Tempel 2 (line 305) were reported as Tier 1 "No source citation
(recalled)"; both actually score V_SOURCED, score 12, Tier 2, "Cited, not
independently cross-checked". Cause: a DIFFERENT citation at line 276 (JPL
Small-Body Database) sits 18 and 29 lines above them, inside the flat 60-line
context window -- that file carries per-section citations through
HISTORICAL_TAIL_DATA, not only the one at line 85. Live mis-scored findings in
that file: zero. ring_params remains the only file with live impact, and the
only mis-scored finding in it is line 959. The reporting session flagged its
own uncertainty here and asked for confirmation before fixing; that was the
right call and it is why the error did not propagate into a data edit.

THREE-LEVEL CHECK (explicitly requested; answer is not a simple no). Three-
level nesting is not absent -- it is the DOMINANT shape: 140 dicts nested 3+
deep across the repo, 63 of them carrying claim-bearing strings, overwhelmingly
shell_configs.py (SHELL_CONFIGS['Jupiter']['core'] and similar). This cannot be
seen from build_citation_block_table's output, which stops at depth 2; it
required walking the source AST directly. That depth-2 ceiling is precisely WHY
Phase 1c works for shell_configs.py. Verified separately: NO dict nested 3+
deep anywhere in the repo carries its own citation, so nothing is misattributed
today. Latent risk retained: the resolver is structurally blind to a depth-3
citation, and if one is ever added its strings will silently inherit the
depth-2 citation instead -- "innermost wins" failing one level down, invisible
in the tier counts.

Fix, as built and verified. (a) DATA, ring_params only: a short repeat citation
above each of the four ring keys, pointing at the full citation above
ring_params. Measured on a clean clone: Tier 1 133 -> 132, Tier 2 586 -> 587,
exactly one finding moves (line 959), nothing enters, Tier 3/4 unchanged --
matching the original predesign headline. (b) MECHANISM, diagnostic only, zero
scoring effect: provenance_scanner.py now records SHADOWED_STRINGS (narrowest
containing block uncited while an outer one is cited) and DEEP_CITATIONS (a
dict 3+ deep carrying its own citation, currently zero), and reports both in a
new CITATION LEVEL MISMATCH audit section. Live run reports 17 shadowed strings
across the two remaining latent files; the deep-citation subsection correctly
renders zero times.

Deliberately NOT done: repeat citations for the three latent files. They carry
no live mis-scoring, the flat 60-line window covers them, and editing three
clean files to fix nothing is churn that can itself drift. The diagnostic
covers those three, every future instance, and the depth-3 case that no data
fix would catch. Same move already made for scope-limited citations in 1c:
decouple detection from resolution, keep the resolver strict, make the shape
visible rather than silently fine.

Explicitly rejected: loosening the resolver to search outward for a citation.
Measured during 1c -- it produces byte-identical audits at HEAD and would clear
all 18 L-173 findings the moment anyone adds a citation above SHELL_CONFIGS.
The strictness is the protection; this item exists to make its cost visible,
not to remove it.

Relationship to L-173. Adjacent, not nested. L-173 is sources MISSING. L-174 is
sources PRESENT but pitched at a level the resolver does not read. A shadowed
string is not an L-173 gap and must not be reported as one -- test_genuinely_
uncited_is_not_reported_as_shadowed pins that boundary, because collapsing the
two would make a missing source look like a formatting problem.

Tony-action (do). Run patch_L174_citation_level_mismatch.py via VS Code's Run
button; expect 15 ok lines across 3 files. Then test_citation_inheritance.py
(expect 20 passed) and provenance_scanner.py (expect Tier 1 132, Tier 2 587,
plus the new CITATION LEVEL MISMATCH section -- that section appearing is the
intended outcome, not a problem).

Tony-action (decide). Whether the 17 latent shadowed strings ever get repeat
citations, or stay monitored via the diagnostic indefinitely. Recommendation is
monitored; revisit only if one of those files is being edited for other
reasons, when the repeat costs nothing extra.

Gap. If a depth-3 citation ever appears, DEEP_CITATIONS will report it and
build_citation_block_table needs extending to record depth 3. Not built
speculatively for a population of zero.

Ref: provenance_scanner.py (build_citation_block_table, resolve_block_citation,
find_shadowing_block, _record_deep_citations); jupiter_visualization_shells.py
(ring_params); comet_visualization_shells.py (HISTORICAL_TAIL_DATA);
planet_visualization_utilities.py (PLANET_ROTATION); idealized_orbits.py
(planet_poles); test_citation_inheritance.py; L-156 Gap item 6; L-173;
documentation/AS_BUILT_L156_phase1c.md.

#### [L-154] Gallery feature-rendering JS layer (shells, rings, radiation belts -- Artifact 2 prerequisite)
<!-- L:154 status:DONE upd:2026-08-24 section:W.Done flag: rice:3/3/70/3 -->
- **DONE 2026-08-24. Both halves shipped and Mode 5 passed.** The
  close block is at the end of this entry; everything above it is the
  record of the item while it was open, left as written.
- **RE-VERIFIED 2026-08-07 at gallery HEAD `33fc7d6`, and the block is
  reclassified.** `gallery/assembler/resolver.py` line 133 STILL reads
  `features = tuple(rec.get("features") or ())`. Failure reproduced
  directly this session: `{'ring_system': {'main_ring':
  {'inner_radius_km': 122500}}}` collapses to `('ring_system',)`.
  Third independent verification (2026-07-27 Fable, 2026-07-28 Sonnet,
  2026-08-07 Opus 5), each at a different HEAD.
- **Why the reclassification.** This entry is carried as blocked on the
  L-155-162 provenance cluster. That is true but it is not the NEAREST
  blocker, and reading it as the only one is misleading. Even with a
  perfect transport and perfectly sourced values, the resolver discards
  every parameter one step before anything could draw them. The
  resolver fix is small, independent of ALL provenance work, and can
  proceed at any time. Confirmed the same day: nothing on the client
  reads `feature_configs.json` at all -- zero references in any JS or
  HTML. The file is written nightly into the cache and no code reads
  it.
- Note the surfaces are distinct: `index.html` is the STATIC curated
  gallery and never needed feature data; `interactive.html` is the
  assembler surface and is the one that does. Only the Artifact 1 test
  harness reads the cache today.
- **What.** The client-side JS that reads `ring_system`, `van_allen_belts`,
  `atmosphere_shell`, and `radiation_belts` out of the served cache and
  actually draws them. `assemble.py` already resolves and reports the
  feature dispatch as data; nothing draws it yet.
- **Blocked on:** the L-155-162 provenance-scoring cluster below (data/
  scoring settled before this gets built, not the other way around).
- **SUPERSEDED 2026-08-23 -- the bullet above is reversed, and left in
  place because it was the standing rule for six weeks.** Tony's
  ruling of 2026-08-22 (the braid): provenance stops being a GATE and
  becomes a per-artifact slice, and this item is the FIRST work rather
  than the last. Status moved BLOCKED -> OPEN the same day. Three
  reasons, in the order they carry weight. (a) Nothing in the
  provenance cluster changes a line of this item's code -- the
  resolver discards parameters regardless of whether the values behind
  them are sourced. (b) A ring drawn from an unsourced number freezes
  nothing; only a FINGERPRINTED artifact does, so the sourcing
  requirement belongs to L-080/Artifact 2 and not here. (c) Until this
  is built, ring provenance is text checked against text -- once it
  draws, a wrong radius becomes something Tony's eyes can catch, which
  is this project's own ground truth. Verified again at gallery
  `02aefc0` on 2026-08-23: `resolver.py` line 133 still reads
  `tuple(rec.get("features") or ())`, `models.py` line 91 still types
  the field `Tuple[str, ...]` to match, and nothing in the gallery repo
  reads `feature_configs.json` -- only the builder writes it. Fourth
  independent verification, fourth different HEAD.
  **Ref:** `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` Section
  5a, "The order of execution" (v19); `documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md`
  Section 1; L-221 (sequencing authority).
- **Correction (2026-07-27, Fable 5 review + Sonnet 5 independent
  verification, both against live HEAD):**
  `documentation/HANDOFF_gallery_feature_layer_L154_resume.md` claimed the
  resolver bug (params dropped by `tuple(dict)` in `resolver.py`) was
  "fixed and settled." It is NOT -- `resolver.py` line 133 still reads
  `tuple(rec.get("features") or ())`, and `objects_config.json`'s
  `features` values are genuinely nested dicts (Earth's atmosphere
  fractions, Jupiter's ring radii, all present), so the line still drops
  every parameter to bare category-name keys. The resume handoff is
  corrected in place (Part 3 below) -- this entry is the ledger-side
  record so the claim can't resurface from a stale copy of that handoff.
**Claude:** [re-verified 2026-07-28, live HEAD, independently of the
2026-07-27 correction above] Confirmed still accurate, not stale.
`gallery/assembler/resolver.py` line 133 is still exactly
`features = tuple(rec.get("features") or ())` -- reproduced the failure
mode directly: `tuple()` on a dict yields only its keys, so a real nested
value like `{'ring_system': {'main_ring': {'inner_radius_km': 122500}}}`
collapses to `('ring_system',)`, every parameter lost. Also checked
whether the blocking cluster had cleared since: L-155 through L-162 are
still open or pending-gate, L-156 touched as recently as today
(2026-07-28). BLOCKED remains the correct status on both counts.
- **Open design questions once unblocked:** geometry-building approach
  (port the orrery's shell/belt/ring math into JS literally, or design
  fresh JS-native trace builders -- "knowledge transfers, not code");
  legend behavior (shared legendgroup vs. independently-toggleable rows);
  sequencing (validate on Earth's already-closed Mode-5 harness first, or
  build straight into Jupiter/Saturn since that's what's gating Artifact 2).
**Gap:** wait on the cluster below; land the one-line resolver fix in the
first gallery session that resumes this item -- before anything else in
the resume handoff is acted on; then a design session for the three open
questions above; then build (Opus 5) + Mode 5 acceptance.
**Note (2026-07-29, Tony's explicit sequencing call):** "the cluster
below" means the WHOLE thing, Phase 4 included -- not just Phases 1-3.
Once the scanner build ships, this item's own technical blocker (the
resolver bug, the pinning engine) is gone, and it would be defensible to
call L-154 "unblocked" at that point. Tony's call is stricter than
defensible: no interactive/Artifact-2 work resumes until both Gemini
worksheets (L-157, then L-161+L-078a) are also closed. Deliberate, not an
oversight -- avoid interleaving data-integrity work with visual-feature
work; finish one before starting the other. Do not read "Phase 3 shipped"
as a green light on its own.
**SUPERSEDED, and the supersession is the point.** The 2026-07-29 note
above makes this item wait on the whole provenance cluster. Tony's braid
ruling of 2026-08-22 replaced that: provenance stops being a GATE and
becomes a per-artifact slice, and this item moves to the FRONT of the
order rather than the back. The note is kept because a ruling that was
later changed is part of the record; it is no longer in force.

**CLOSE BLOCK -- 2026-08-24.**
- **First half, gallery `8ec4f261` (2026-08-23).** `resolver.py` kept the
  feature mapping instead of reducing it to a tuple of category names, and
  populated `FeatureRequest.params`. The field had been declared in
  `models.py` and emitted by `assemble.py` since the beginning and had
  never been filled: the pipe was built, wired, and shipping empty dicts.
- **Second half, gallery `099a8536` (2026-08-24)**, via
  `patch_L154_2_feature_render_layer.py`. `gallery/feature_renderers.js`
  (536 lines) draws ring systems, radiation belts and atmosphere shells
  from the report; `gallery/solar_system_earth_test2.html` gained a scene
  selector, a `Frame on` axis control, and the call into the renderers.
- **Two render inputs were missing from the served cache and were added
  to `data/objects_config.json`** under Tony's ruling of 2026-08-24
  (option (a) of three: put the copy in the store the project already
  watches, not in a JavaScript table nothing scans). The IAU pole for
  Jupiter and Saturn as a new `orientation` feature key, and
  `planet_radius` on the three feature nodes whose numbers are expressed
  in multiples of it. See L-232.
- **Earth deliberately gained NO new feature key.** The L-080 fingerprint
  hashes the sorted set of feature keys, so a third key on Earth would
  have broken Artifact 1's lock -- for a rotation the orrery does not
  apply to Earth's belts in the first place (L-231). The patch asserts
  Earth's key list rather than trusting the reasoning.
- **Measured, not asserted.** Ring plane normals fitted from three drawn
  points by cross product, independent of the renderer's own basis
  function: Saturn 28.049 deg from the ecliptic, Jupiter 2.222 deg, both
  matching `idealized_orbits.py`'s pole table and obliquity rotation
  computed separately. A Ring inner/outer radii read back off the drawn
  points at 122,340 and 136,800 km. Jupiter's inner belt at 1.750 R_J.
  Earth's lower atmosphere at 1.0500 R_E.
- **28.05 deg is correct and is not 26.73.** The familiar figure is
  Saturn's tilt against its own ORBIT; these plots are ecliptic-framed.
  Recorded here because a future Mode 5 will otherwise flag a correct
  render as wrong.
- **Mode 5 PASSED 2026-08-24** (Tony), on Earth alone, Jupiter + Saturn
  whole-scene, and framed on each of Jupiter and Saturn. Browser trace
  counts matched the offline harness exactly -- 8 traces from 2 requests
  for Earth, 28 from 5 for Jupiter + Saturn -- and the framing half-spans
  agreed to three figures (Jupiter 0.00358 AU, Saturn 0.00384 AU, Earth
  0.000243 AU).
- **Artifact 1's lock was verified IN THE BROWSER**, not only in Python:
  `abbd01094852b57f` recomputed through Pyodide against the rebuilt cache.
  That is a stronger check than the container test, because it proves the
  browser path produces the same scene spec.
- **One visual oddity, checked and NOT a defect.** Saturn's seven ring
  info markers fall along one ray at increasing radii, because each sits
  at the first point of its own ring. `create_saturn_ring_system` does
  exactly the same thing, and the comment there records that the May 2026
  Neptune 2C fix was specifically to stop them collapsing onto one
  another. Scene-equivalent. Changing it is a change to both instruments.
- **Not done here, and next:** Artifact 2's thirty-number provenance
  slice, then the lock (segment 4), then the page (segment 5). The
  renderers draw from numbers that are not yet sourced, which v19 allows
  explicitly -- drawing is not locking.
- **Patches:** `patch_L154_1_resolver_feature_params.py`,
  `patch_L154_2_feature_render_layer.py`, both archived to
  `documentation/` in the GALLERY repo. Smoke tests
  `smoke_features.js` (23 checks) and `smoke_framing.js` (12 checks)
  archived beside them; they run under Node, which is outside Tony's
  working set, so they are session evidence rather than a routine gate.
  Where a runnable home for them belongs is open.

**Ref:** `assemble.py`, `resolver.py`, `render_objects.py`, `presentation.py`;
`gallery/feature_renderers.js`; `gallery/solar_system_earth_test2.html`;
`data/solar-system/feature_configs.json`; `data/objects_config.json`;
`documentation/HANDOFF_gallery_feature_layer_L154_resume.md`;
`documentation/REVIEW_provenance_refactor_cluster_scoping.md` (section 5);
L-149/L-150/L-151 (M2 track); L-155-L-162.

---
### W.Cross-references -- existing items that interact with the web track

- **L-026** -- CRLF to LF on `palomas_orrery_helpers.py`. Companion to L-087.
- **L-046** -- Preset authoring. A saved scene spec IS a preset. Falls out of
  the vocabulary design (L-089).
- **L-068** -- Static/animation pipeline residuals. Desktop cleanup, not web
  blockers, but worth closing.
- **L-071** -- Earth system dated-scenario storytelling. Natural web narrative.
- **L-074** -- Gallery culling. Headroom lever for Pages budget.
- **L-083** -- Plotly 6 / Kaleido migration. Desktop + Instagram concern only;
  Kaleido is not needed for web (Plotly.js renders interactively in browser).

---

## Appendix: Protocol Version History -- MOVED

Moved 2026-08-18 to `documentation/PROJECT_INSTRUCTIONS_HISTORY.md`,
PART 1, per Tony's ruling under L-199. That file carries the full
history from v1.0 and, as PART 2, the twenty-seven lessons removed from
the protocol at v3.37.

The protocol document keeps the three most recent entries resident; a
fourth pushes the oldest down into PART 1. Every entry lives in exactly
one place, so there is nothing here to keep in step.
