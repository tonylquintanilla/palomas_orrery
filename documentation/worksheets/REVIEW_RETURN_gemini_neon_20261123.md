I worked from files uploaded on 2026-11-23, copied from orrery commit `b0eedeabb6aa1c88243443b876e09bfc72ec3dd3` and gallery commit `326863a62a18c6f9446967f967ba5719d21ca91e`, and I did not read GitHub.

### Files read

* **Read in full:** `MANIFEST.md`, `orrery/PROJECT_INSTRUCTIONS.md`, `orrery/README.md`, `orrery/CLAUDE.md`, `orrery/DOCUMENT_CAPS.md`, `orrery/METHOD_MODEL_EFFORT.md`, `orrery/documentation/WHERE_WE_ARE.md`, `orrery/documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`, `website/README.md`, `website/CLAUDE.md`, and six skills chosen because they govern session mechanics, editing, records, pre-testing, and core pipelines (`agentic-pre-test`, `earth-system-pipeline`, `gallery-assembler`, `gallery-pipeline`, `ledger-and-session-records`, `safe-file-editing`).
* **Read in part:** The remaining six skills (`gallery-cache-builder`, `horizons-orbital-mechanics`, `interactive-exhibit`, `orrery-coding-conventions`, `provenance-cross-check`, `provenance-discipline` — openings, all headings and contents lists, and selected sections); `LEDGER_CONSOLIDATED.md` (opening stamps, purpose, conventions, start of generated index, and full blocks for `L-499`, `L-506`, and `L-545`); and the provided openings of `PROVENANCE_AUDIT.md` (lines 1–120), `MODULE_ATLAS.md` (lines 1–120), `constants_new.py` (docstring), and `website/INTERACTIVE_AS_BUILT.md` (lines 1–100).
* **Did not read:** None of the four excluded documents, not ledger item `L-522`, not Section C (closed items) of the ledger, and no source code.

### How I read the three terms

* **Gaps:** Missing or broken links in the rule chain, where a live workflow or file is unmentioned, contradicted by a newer file, or left without a check.
* **Effectiveness:** Whether a cold AI session and Tony can follow a rule as written without misreading it, missing it, or overriding it.
* **Efficiency:** How much reading, ceremony, and token cost (the chunks of text an AI processes each turn) a rule spends compared with the real errors it prevents.

### Findings (most important first)

**1. `PROJECT_INSTRUCTIONS.md` is too long for a file loaded on every turn, working against its own Token Economy rule.**

* **Evidence:** "SPEND TOKENS WHERE THEY BUY VERIFICATION OR A DECISION, NOWHERE ELSE." (`PROJECT_INSTRUCTIONS.md`, `Token Economy [QUALITY]`)
* **Who pays:** Tony (weekly model limits and energy cost) and every session (re-reading 1,394 lines / ~11,860 words on every turn, roughly a quarter of which is Part 4 philosophy, Quotables, and Lessons Archive).
* **Smallest change:** Move Part 4 (`Foundation`) and Part 5's `Quotables` and `Lessons Archive` into a separate reference file alongside `PROJECT_ORIGIN.md`, keeping `PROJECT_INSTRUCTIONS.md` strictly to operating rules, modes, and gates.
* **Confidence:** High. I would reconsider only if sessions made noticeably worse judgment calls without Part 4 resident on every turn.

**2. `PROJECT_INSTRUCTIONS.md`'s opening workflow no longer matches how sessions actually start.**

* **Evidence:** "Check context - Uploads? Past chats? The ledger (LEDGER_CONSOLIDATED.md): open items, Tony comments, Gap notes -- read them before proposing work." (`PROJECT_INSTRUCTIONS.md`, `Session Start`)
* **Who pays:** A cold session (told to open the 2.8 MB ledger first while Part 1 never mentions `WHERE_WE_ARE.md`, `CLAUDE.md`, `DOCUMENT_CAPS.md`, or the three session kinds) and Tony (has to steer new sessions back to `WHERE_WE_ARE.md`).
* **Smallest change:** Rewrite `Session Start` in `PROJECT_INSTRUCTIONS.md` to point first to `documentation/WHERE_WE_ARE.md`, `CLAUDE.md`, `DOCUMENT_CAPS.md`, and the three session kinds (coordinating, talk-only, build).
* **Confidence:** High. Nothing in the files supports starting a routine session inside `LEDGER_CONSOLIDATED.md` ahead of `WHERE_WE_ARE.md`.

**3. The critical parallel-pipelines gate omits the interactive gallery, which is now the site's front door.**

* **Evidence:** "Position data reaches a viewer through FIVE parallel consumers." (`PROJECT_INSTRUCTIONS.md`, `Check All Parallel Pipelines [CRITICAL]`)
* **Who pays:** The work itself (a session fixing position or hover handling can check all five listed paths—desktop static, animation, social export, `gallery_studio.py`, `json_converter.py`—and miss `gallery_cache_builder.py`, `gallery/assembler/`, and `interactive.html`).
* **Smallest change:** Add the interactive gallery chain as a sixth consumer in `Check All Parallel Pipelines [CRITICAL]` and in `website/README.md` (`Two of the project's five position consumers live here`).
* **Confidence:** High. I would reconsider only if the interactive gallery's position flow is completely insulated from orrery position-data changes, which `gallery-cache-builder` shows it is not.

**4. The `[CRITICAL]` tier has spread across six skills, diluting the rule that critical gates stay short and resident.**

* **Evidence:** "The tiers apply across both layers: skills carry [QUALITY] and [PRACTICE] conventions; the [CRITICAL] checkpoint gates stay resident here." (`PROJECT_INSTRUCTIONS.md`, `Procedural Criticality`)
* **Who pays:** Every session (there are 25 `[CRITICAL]` headings inside skills: 12 in `provenance-discipline`, 6 in `provenance-cross-check`, 4 in `interactive-exhibit`, and 1 each in `agentic-pre-test`, `gallery-cache-builder`, and `safe-file-editing`) and the work itself (when everything is critical, stop-gates blur together).
* **Smallest change:** Either downgrade skill-level `[CRITICAL]` labels to `[QUALITY]` (leaving true stop-gates only in `PROJECT_INSTRUCTIONS.md`), or amend `Procedural Criticality` to allow a small, capped number of skill-level stop-gates.
* **Confidence:** High. I would reconsider if Tony wants skill-level stop-gates and simply has not updated that sentence in `Procedural Criticality`.

**5. Core files contradict each other on `git pull` and nightly automation.**

* **Evidence:** "He doesn't use or recognize pull; in his single-author, always-push-after-commit workflow, it has nothing to reconcile." (`PROJECT_INSTRUCTIONS.md`, `WHO TONY IS`)
* **Who pays:** A new session (gives outdated git instructions or assumes no commits land overnight) and Tony (who now runs Fetch and Pull every morning per `WHERE_WE_ARE.md` because GitHub's nightly run pushes commits; `website/README.md` also still says the cache builder "is run by hand rather than on a schedule").
* **Smallest change:** Update `WHO TONY IS` in `PROJECT_INSTRUCTIONS.md` and `How the interactive gallery works` in `website/README.md` to reflect the automated nightly run on GitHub and Tony's morning Fetch/Pull routine.
* **Confidence:** High. I would reconsider only if Tony plans to turn off the GitHub nightly run soon.

**6. Both `README.md` files still report that `objects_config.json` is copied by hand and never reads `constants_new.py`.**

* **Evidence:** "`objects_config.json` lives in the gallery repository and is maintained by hand. The cache builder has never read `constants_new.py`." (`orrery/README.md`, `From the orrery to the gallery`)
* **Who pays:** Cold sessions and outside readers (who may hand-edit `objects_config.json` instead of editing `constants_new.py` and running `export_constants.py` / `mirror_constants.py`, which have been live since September–October 2026 per `MASTER_PLAN_INTERACTIVE_GALLERY.md` and `INTERACTIVE_AS_BUILT.md`).
* **Smallest change:** Update that section in `orrery/README.md` and `website/README.md` (`How the interactive gallery works`) to describe the live export-and-mirror pipeline, and restamp both headers.
* **Confidence:** High. I would reconsider if manual copying is still required for most fields in `objects_config.json`.

**7. `Stamp What You Change` has created runaway append-only headers at the top of the ledger and constants file.**

* **Evidence:** "A patch that edits a file also updates that file's own currency block, in the SAME transaction as the body." (`skills/safe-file-editing/SKILL.md`, `Stamp What You Change [QUALITY]`)
* **Who pays:** Every session (wasting tokens and read windows wading past 794 lines of `Module updated:` stamps at the top of `LEDGER_CONSOLIDATED.md` before `Purpose and use` even starts, and 215 lines of stamps in `constants_new.py`'s docstring) and Tony (who cannot see what a file is for when he opens it).
* **Smallest change:** Amend `Stamp What You Change` so files keep one "Last updated" line (or a 3-entry cap like the skills), leaving older edit history to `git log`.
* **Confidence:** High. I would reconsider only if Tony actively reads those header logs in VS Code instead of `WHERE_WE_ARE.md` or GitHub Desktop history.

**8. `PROJECT_INSTRUCTIONS.md` contradicts itself on whether its own prose should be readable by Tony.**

* **Evidence:** "THIS DOCUMENT AND THE SKILLS ARE WRITTEN THE OTHER WAY, and that is not a licence." (`PROJECT_INSTRUCTIONS.md`, `Register Rule`)
* **Who pays:** Tony (one of the two named readers, who cannot easily audit rules he is asked to ratify when they are written in compressed shorthand; meanwhile `WHO TONY IS` in the same file says to unpack jargon "in this document's own prose").
* **Smallest change:** Decide once and state it cleanly: either apply plain sentences to `PROJECT_INSTRUCTIONS.md` itself, or mark specific reference tables as Claude-only and keep all ratified rules in plain language.
* **Confidence:** High. I would reconsider if Tony prefers compressed files to save tokens and relies solely on chat and `WHERE_WE_ARE.md` for plain speech.

**9. `DOCUMENT_CAPS.md` freezes bloat at zero headroom and omits four active governing files.**

* **Evidence:** "Each cap was set on November 10, 2026 at the document's size that day, so nothing could grow from then on" (`DOCUMENT_CAPS.md`, `The table`)
* **Who pays:** Every editing session (14 of 17 capped files have 0 lines of headroom, forcing every small skill update to carve out random passages into `SKILL_HISTORIES.md`) and the work itself (four live governing files—`METHOD_MODEL_EFFORT.md`, `website/CLAUDE.md`, `website/README.md`, and `website/INTERACTIVE_AS_BUILT.md`—have no cap at all).
* **Smallest change:** Add those four files to `DOCUMENT_CAPS.md`, and after each reduction step leave a small working margin (10–15 lines) rather than freezing at 0 headroom.
* **Confidence:** Medium-high. I would reconsider if zero headroom is deliberate forcing-function design and website caps are tracked separately in the gallery repository.

**10. Oversized skills and 15–34 line `fires_when` trigger lists defeat the point of an on-demand skill layer.**

* **Evidence:** "A skill over Anthropic's 500-line guideline also opens with a ## Contents list of its headings" (`skills/ledger-and-session-records/SKILL.md`, `Protocol and Skills Change Log (v3.30 addition)`)
* **Who pays:** Every session (three skills—`horizons-orbital-mechanics`, `gallery-cache-builder`, and `interactive-exhibit`—take 67 lines inside the resident Skill Manifest's `fires_when` column alone, and 8 of 12 skills exceed 500 lines, with `provenance-discipline` at 1,511 lines requiring six separate reads).
* **Smallest change:** Limit each `fires_when` entry to 2–3 lines of broad triggers, and move long origin stories, worked examples, and reference tables out of `provenance-discipline`, `gallery-cache-builder`, and `horizons-orbital-mechanics` into their `references/` folders.
* **Confidence:** High. I would reconsider only if long `fires_when` lists are proven necessary to prevent missed triggers in practice.

**11. Several live files still carry stale facts that can misdirect a cold session.**

* **Evidence:** "The Sun (`?exhibit=sun`) is the worked example and the template; the Solar System Explorer is the default room" (`skills/interactive-exhibit/SKILL.md`, `What an exhibit is, and what this skill is not`)
* **Who pays:** A cold session (told the wrong default room when `solar-system` became default on Oct 22; told in `safe-file-editing` to check a `SystemButtonFace` workaround that `agentic-pre-test` v1.3 removed on Oct 6; and confronted in `MASTER_PLAN_INTERACTIVE_GALLERY.md` by a frozen 130-line `v35` status block sitting right under the `v37` executive summary).
* **Smallest change:** Fix the default-room line in `interactive-exhibit`, remove the retired `SystemButtonFace` reference and "portable" claim in `safe-file-editing`, and move the frozen `v35` status block out of `MASTER_PLAN_INTERACTIVE_GALLERY.md` into `MASTER_PLAN_HISTORY.md`.
* **Confidence:** High. I would reconsider only if Tony wants the `v35` block kept inline for historical context.

### Five things these documents do well and should not lose

1. **The SHA round trip and "verify against what cannot be talked into agreeing":** Anchoring every handoff to a git commit hash (a unique fingerprint of the files) and treating the rendered picture as ground truth is an unusually strong defense against drift.
2. **"A Check That Cannot Fail Is Not Passing" and "A Report Names Its Items":** Requiring checks to prove they ran (such as `PASS / FAIL / UNREACHABLE` in `gallery_maintenance_run.py`) and naming items instead of printing bare counts prevents silent failures.
3. **`WHERE_WE_ARE.md` as Tony's tactical page:** Keeping Tony's plain-language status, active road, and run-record zone in one ~130-line file—separate from the 2.8 MB ledger—gives him a real dashboard he can read on his phone.
4. **Generated zones separated from hand-written rules:** Using `Doc-Kind` tags and generators (`skills_index.py`, `ledger_index.py`, `doc_index.py`, `module_atlas.py`) keeps indexes and audits synced to reality without manual upkeep.
5. **The provenance "third branch" and Human-Cost Restraint Discipline:** Requiring sessions to remove unsourceable claims rather than cite loosely (`PROJECT_INSTRUCTIONS.md`), and to transcribe rather than editorialize human-cost data (`earth-system-pipeline`), sets a high factual and ethical bar.

### Notes on the review request itself

* **Word budget vs. structure:** Fitting a complete file-read inventory, definitions of three terms, up to 12 five-part findings with verbatim quotes, five strengths, and a critique of the request into ~1,500 words pushes the reply toward the exact compressed writing Tony dislikes. A 2,000-word budget or a cap of 6–8 findings would let the prose breathe.
* **Judging mid-migration rules without seeing the migration plan:** Asking a fresh reviewer to judge rules from the November 10 review without knowing which pieces are temporary scaffolding (such as the November 10 zero-headroom caps awaiting later steps) means some findings will point at work you already plan to finish. That fresh-eyes check is still useful, but you should discount findings that only reflect unfinished steps.