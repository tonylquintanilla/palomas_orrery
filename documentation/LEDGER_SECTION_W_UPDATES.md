# Section W Ledger Updates — July 5, 2026
# Apply these detail blocks to LEDGER_CONSOLIDATED.md, then run ledger_index.py.
# Four items changed; remainder unchanged.

---

## L-085 — STATUS: PROPOSED → DONE

#### [L-085] LICENSE to repo root
<!-- L:085 status:DONE upd:2026-07-05 section:W.Prep flag: rice:2/2/100/1 -->
- **What.** The MIT license file lived at `documentation/LICENSE.md` where GitHub
  could not find it. Moved to repo root.
- **Done.** `LICENSE.md` at repo root [verified @7b25eb9]. Copyright year
  harmonization status: confirm separately.
**Ref:** Master plan §6; confirmed by Opus 4.6 review (July 4).

---

## L-088 — STATUS: PROPOSED → OPEN (next active item)

#### [L-088] Two-sided pilot (Phase 0)
<!-- L:088 status:OPEN upd:2026-07-05 section:W.Active flag: rice:2/2/50/1 -->
- **What.** Build the orbital parameter eccentricity visualization twice: Dash on
  HF Spaces, Pyodide on a static page. Same visualization, two delivery
  mechanisms. Tests hosting assumptions, cold-start vs first-load download, phone
  experience, ops feel.
- **Why two-sided.** The server-vs-serverless decision (§7 #1 in the master plan)
  is the largest remaining architectural choice. §1's "site never fetches" removed
  the CORS blocker on Pyodide. The orbital parameter viz is pure geometry -- no
  cache, no data files -- making it the cheapest possible test of both paths.
- **Downstream consequence.** If Pyodide wins, the web app is a static site --
  Fable's Option E (gallery viewer as unified front end) arrives nearly for free.
  If Dash wins, the gallery stays a sibling.
- **Attribution gate.** If either pilot is publicly reachable, keep unlisted until
  L-086 lands.
- **Open decision: matplotlib in Phase 0** (master plan §7 #9). The eccentricity
  demo currently produces matplotlib 2D output. For an apples-to-apples
  Dash-vs-Pyodide comparison, both sides should render the same library. Options:
  convert to Plotly (clean comparison); keep matplotlib (accept rendering
  difference as data); or use the Plotly 3D orbital parameter visualization as
  the pilot subject instead. Resolve before build starts.
- **Current status.** Phase 1 vocabulary complete (L-089); Phase 0 is the sole
  active build track. Model assignment: Opus 4.6.
**Gap:** resolve matplotlib decision, build both versions, test on phone.
Lessons-learned document + server-vs-serverless decision before Phase 2.
**Ref:** Fable 5 review of v4 (finding 10); master plan §5 Phase 0, §7 #9.

---

## L-089 — STATUS: PROPOSED → PENDING-GATE (vocabulary delivered, gate items deferred)

#### [L-089] Scene-spec shared skeleton + solar system vocabulary (Phase 1)
<!-- L:089 status:PENDING-GATE upd:2026-07-05 section:W.Active flag: rice:3/3/50/3 -->
- **What.** Design in conversation, not code.
  (a) The shared spec skeleton -- what every spec has across all domains: domain
  tag, content type, display options.
  (b) The solar system vocabulary: objects, center, dates, display options,
  content type (static/animation).
  (c) The coverage index interface for the solar system domain.
  (d) Scene equivalence criteria -- the concrete definition that shapes L-080's
  golden artifacts.
  (e) Gate check: confirm no shared-layer seams beyond the two named in §2.
- **Vocabulary + coverage index: DELIVERED.**
  `PHASE1_SCENE_SPEC_VOCABULARY.md` (Fable 5, July 4, 2026, built on `fdb66ca`).
  Shared skeleton (5 fields: spec_version, domain, content_type, preset_id,
  title) + solar system payload (9 field groups) + exhaustive mapping table (52+43
  = 95 active `.get()` reads, reproducible census method) + content-type
  distinction (proves one assembler replaces both orchestrators) + coverage index
  interface (Protocol class).
- **Serializability: settled YES.** Every field is str/float/int/bool/None/list/
  dict. Presets, shareable scenes, and golden artifacts get serialization for free.
- **Animation/static consolidation: verified.** The `animation` block is the
  entire delta between content types. One assembler replaces both orchestrators.
- **Eight design decisions (DD-1 through DD-8)** and **six open questions (OQ-1
  through OQ-6)** recorded in the deliverable. **Rulings deferred to the Phase 0
  → Phase 2 transition.** Soonest needed: OQ-4 (preset expansion semantics),
  DD-3 (explicit comet-tails field).
- **Prompt lineage.** Task prompt drafted by Opus 4.6, reviewed by Opus 4.8
  (9 points, all accepted), delivered to Fable via collegial relay.
**Gap:** (a-c) closed. Remaining: (d) scene equivalence criteria and (e) seam
gate-check — both deferred to Phase 2 start. DD/OQ rulings at that transition.
**Ref:** PHASE1_SCENE_SPEC_VOCABULARY.md; FABLE_TASK_PHASE1_VOCABULARY.md;
master plan §5 Phase 1, §5a.

---

## L-079 — body update (status stays OPEN)

#### [L-079] Shared assembler architecture (keystone -- redefined)
<!-- L:079 status:OPEN upd:2026-07-05 section:W.Active flag: rice:3/3/50/3 -->
- **Redefined from:** "Headless scene core -- decouple scene construction from
  Tkinter" (Fable 5 survey, July 2 2026).
- **Redefined to:** Build a shared assembler per domain. Both GUIs (tkinter
  desktop, web) are thin harvesters feeding the assembler. The assembler is new
  code written with the desktop orchestration as recipe reference. Original code
  archived for reference or reconstruction.
- **Four domains:** solar system (main build), stars, orbital parameters
  (educational showcase), Earth system (mixed KMZ + Plotly).
- **Phasing (governed by master plan):**
  Phase 0: two-sided pilot (L-088). Phase 1: shared spec skeleton + solar system
  vocabulary (L-089). Phase 2: solar system assembler + desktop migration tail.
  Phase 3: star assembler + cache. Phase 4: hybrid (exoplanets + Sgr A*).
  Phase 5: Earth system. Phase 6: web UI.
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
- **Key decision (open):** server (Dash) vs serverless (Pyodide) -- Phase 0
  two-sided pilot (L-088) resolves this.
- **Progress:** Phase 1 vocabulary delivered (L-089, Fable 5, July 4 2026).
  Phase 0 pilot is the active build track. Master plan at v7.
**Gap:** the master plan IS the gap document. Current phase: Phase 0 (L-088).
**Ref:** MASTER_PLAN_WEB_PUBLICATION.md v7; PHASE1_SCENE_SPEC_VOCABULARY.md;
Fable 5 survey + L-079 deep dive; Opus 4.8 convergence handoff + reviews;
Opus 4.6 + Tony convergence (July 3); Fable 5 vocabulary session (July 4).
