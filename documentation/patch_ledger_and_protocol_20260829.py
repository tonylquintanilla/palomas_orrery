"""
patch_ledger_and_protocol_20260829.py

The record layer of the 2026-08-29 Sun-ship session, brought current in
one transaction: the ledger edits owed, the two pinned literals in
test_constants_provenance.py restated as ratio bounds, and the protocol
version-history entry that the provenance-discipline 2.10 bump never
got.

**This REPLACES patch_ledger_20260829_sun_ships.py.** That one was
delivered and not run; it covered the ledger and the tests but left the
protocol entry as an open Gap, which would have made L-258 claim
something owed that this patch closes. Run only this one.

Built on orrery `8b762e0474859bcb0cdd723f95313e37e2abaf60` at
https://github.com/tonylquintanilla/palomas_orrery (branch main),
gallery `c367b262fce4cbdf87d9a6ff1fe82e82a9615ab5` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both confirmed against the live remote 2026-08-29.

FOUR files, ONE transaction. Every guard and every anchor is checked on
all four before any of them is written. If anything refuses, nothing is
written anywhere.


WHY IT IS ONE PATCH AND NOT TWO

The four-step skill-bump binding rule says the version line, the
manifest, the protocol entry and the commit travel together. Splitting
the protocol entry into a second script would have recreated exactly the
gap this patch closes, one layer up -- and it would have needed a run
ORDER between two scripts, which is the pain L-219 already names.


WHAT IT WRITES

LEDGER_CONSOLIDATED.md -- four edits, detail blocks only. The index zone
is NOT touched; run ledger_index.py afterwards to regenerate it.

  1. L-258 (new, DONE, section C) -- significant figures at rest, and
     the three changes it made: RADIATIVE_ZONE_AU 0.7 -> 0.713,
     INNER_CORONA_RADII re-homed to Lamy et al., three
     `# Cross-checked:` legs retired. Closed by this patch, which
     supplies its last missing piece.
  2. L-259 (new, DONE, section C) -- the Sun exhibit ships. The
     assembler ran in a visitor's browser.
  3. L-260 (new, OPEN, section A) -- what the exhibit still owes: axis
     units, and the phone.
  4. L-256 gains its 2.9 and 2.10 lines, owed since 2026-08-28.
  5. L-236 gains the two candidate checks from the Sun ship, and the
     correction that this work DOES have a handle -- the 2026-08-29
     handoff says it has none.

test_constants_provenance.py -- two edits.

  6. test_core_au_derived_from_solar_radius and
     test_radiative_zone_au_derived_from_solar_radius stop holding a
     copy of a measured value. Each becomes a bound on the RATIO
     against its published range, so a legitimate correction inside
     that range no longer makes the test stale, and a re-sourcing
     outside it still fires.

     The second is failing right now, correctly: `maintenance_run.py`
     reports Constants relations 20 of 21 because the test hardcodes
     `expected = 0.7 * SOLAR_RADIUS_AU`.

PROJECT_INSTRUCTIONS.md -- three edits.

  7. Header to v3.47, August 29 2026, anchored at `8b762e04`.
  8. The v3.47 entry, recording provenance-discipline 2.9 -> 2.10.
  9. The v3.44 entry is REMOVED, to keep three resident.

documentation/PROJECT_INSTRUCTIONS_HISTORY.md -- one edit.

 10. The v3.44 entry lands in PART 1. It is not retyped: the patch
     LIFTS the exact bytes out of PROJECT_INSTRUCTIONS.md and moves
     them, so the moved entry cannot differ from the resident one.


AFTER RUNNING IT

  1. ledger_index.py      (regenerates the index tables)
  2. maintenance_run.py   (Constants relations should read 21 of 21)

Then commit all four files together, which is step 4 of the binding
rule.


HOW TO RUN IT

Drop this file into the ORRERY repo root and press Run.

Prepared August 2026 with Anthropic's Claude Opus 5.
"""

import hashlib
import os
import sys

REPO_ROOT_FALLBACK = r"C:\Users\tonyq\Documents\GitHub\palomas_orrery"

PROBE = "constants_new.py"

LEDGER = "LEDGER_CONSOLIDATED.md"
LEDGER_MD5 = "a8efc888525497ae5ee3aedd7910b0dc"

TESTS = "test_constants_provenance.py"
TESTS_MD5 = "7475afcb122b23a195cf9b888112f97c"

PROTO = "PROJECT_INSTRUCTIONS.md"
PROTO_MD5 = "3fa9d76ee5e1dd6d8df898b2f2d4fec1"

HISTORY = os.path.join("documentation", "PROJECT_INSTRUCTIONS_HISTORY.md")
HISTORY_MD5 = "a6f7aa176201a54c085e6844bd532886"


def find_repo_root():
    here = os.path.dirname(os.path.abspath(__file__))
    for label, folder in (("beside this script", here),
                          ("working directory", os.getcwd()),
                          ("fallback path", REPO_ROOT_FALLBACK)):
        if os.path.isfile(os.path.join(folder, PROBE)):
            print("found %s in the %s" % (PROBE, label))
            return folder
    return None


# ------------------------------------------------------------------
# The three new ledger blocks
# ------------------------------------------------------------------

L258 = (
    "#### [L-258] Significant figures at rest, and the three changes it made\n"
    "<!-- L:258 status:DONE upd:2026-08-29 section:C flag: rice:2/3/90/1 -->\n"
    "- **The rule.** provenance-discipline 2.10 adds The Store Carries the\n"
    "  Verified Figure [CRITICAL] under Report to the Figures You Have,\n"
    "  which governed REPORTING and left the stored value uncovered. Where\n"
    "  a source gives a verified figure more precise than the stored value,\n"
    "  the store carries the verified figure; rounding happens at the\n"
    "  reporting step, never at rest.\n"
    "- **The founding case is why it is [CRITICAL].** `RADIATIVE_ZONE_AU`\n"
    "  held 0.7 beside its own comment recording that it rounded 0.713 --\n"
    "  the store saying it was rounding, and rounding anyway, in a value\n"
    "  drawn on a public page. A rounded value at rest is a second, less\n"
    "  precise store of a number that already exists, and it reads as a\n"
    "  measurement to everything downstream.\n"
    "- **Narrowed in the same breath**, against the two cases the rule\n"
    "  would otherwise damage: a pick from a range stays a declared choice,\n"
    "  and a visibility stylization promotes when the physical value\n"
    "  becomes drawable rather than for want of digits.\n"
    "- **`RADIATIVE_ZONE_AU` 0.7 -> 0.713.** Christensen-Dalsgaard, Gough &\n"
    "  Thompson (1991), ApJ 378:413 measure the convection-zone DEPTH at\n"
    "  0.287 +/- 0.003 solar radii; the base of the zone is 1 - 0.287. A\n"
    "  subtraction, so decimal PLACES govern: three, matching the stated\n"
    "  uncertainty. Basu & Antia (2004) give 0.7133 +/- 0.0005 and are NOT\n"
    "  adopted -- a different work, so taking it would be a re-sourcing\n"
    "  rather than a rounding.\n"
    "- **`INNER_CORONA_RADII` re-homed; the value is unchanged at 3.** The\n"
    "  citation moved from Golub & Pasachoff (2010) to Lamy, Gilardy,\n"
    "  Llebaria, Quemerais & Ernandez, LASCO-C3 24-year photopolarimetry\n"
    "  (arXiv:2009.04820), on the access standard: the 2026-08-20\n"
    "  nine-source read could locate the textbook only as \"Chapter 1\",\n"
    "  with no figure and no findable position.\n"
    "- **An overreach withdrawn in the same pass.** Golub & Pasachoff was\n"
    "  first carried here from the `HELMET_CUSP_RADII` finding as though\n"
    "  that removal transferred. It does not: that read was decisive about\n"
    "  what to REMOVE and silent about what to KEEP, and it concerned\n"
    "  helmet-streamer extent, a different claim. The citation still moved,\n"
    "  on the narrower and correct access ground.\n"
    "- **Three `# Cross-checked:` legs retired**, following 2.9's\n"
    "  retirement of the two-annotation criterion for V_CROSS_CHECKED.\n"
    "  Concurrence is not evidence.\n"
    "- **The corrected value did not reach the site by rebuilding.** The\n"
    "  instruction \"re-run the cache builder and it will pick up the new\n"
    "  value\" was wrong: the builder passes feature constants THROUGH from\n"
    "  `data/objects_config.json` and has never read `constants_new.py`.\n"
    "  The value reached the live page by a hand patch. That is segment 2\n"
    "  failing its first real test, one day after the 2026-08-28 handoff\n"
    "  predicted it in the abstract.\n"
    "- **Two pinned literals, one of which fired.**\n"
    "  `test_radiative_zone_au_derived_from_solar_radius` failed correctly\n"
    "  the moment the value moved. It is named as a derivation test while\n"
    "  holding a MEASURED value, which is how it survived the 2026-08-13\n"
    "  sweep of fifty-five pins.\n"
    "  `test_core_au_derived_from_solar_radius` is the identical shape with\n"
    "  0.2 and was silent only because `CORE_AU` has not moved. Both are\n"
    "  now bounds on the RATIO against their published ranges; neither\n"
    "  holds a copy of a measured value.\n"
    "- **The bump's own record is the last thing that closed, and it is\n"
    "  the lesson.** Steps 1, 2 and 4 of the four-step binding rule\n"
    "  (ledger-and-session-records 1.9) travelled together on 2026-08-29 --\n"
    "  the version line, `skills_index.py`, the commit. Step 3, the\n"
    "  protocol version-history entry, did not, and the manifest going\n"
    "  current on its own DISGUISED the omission: the protocol looked\n"
    "  updated because half of it was. Found the same day by a later\n"
    "  session reading the manifest against the history, not by any check.\n"
    "  That is L-230 predicting itself, and the detection it designs is\n"
    "  still unbuilt.\n"
    "- **Note:** RICE 2/3/90/1, confirmed by Tony 2026-08-29, recorded for\n"
    "  the archive rather than for scheduling.\n"
    "**Closed 2026-08-29** by `patch_ledger_and_protocol_20260829.py`,\n"
    "which supplied the last two pieces: the ratio bounds and protocol\n"
    "v3.47.\n"
    "**Ref:** L-230 (detection for the step that does not fire); L-256\n"
    "(the 2.8 and 2.9 bumps); L-253; L-249; L-259; segment 2 in\n"
    "`documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a.\n"
    "\n"
)

L259 = (
    "#### [L-259] The Sun exhibit ships -- the assembler runs in a visitor's browser\n"
    "<!-- L:259 status:DONE upd:2026-08-29 section:C flag: rice:5/5/100/3 -->\n"
    "- **Live 2026-08-29** at\n"
    "  `palomasorrery.com/interactive.html?exhibit=sun`, unlinked from the\n"
    "  landing page, carrying inline credit, Mode 5 accepted by Tony.\n"
    "  Eighteen shells from the core to the Sun's gravitational influence\n"
    "  at 150,000 AU, each carrying its source in its hover text.\n"
    "- **What is new is not the picture.** The shared Python assembler ran\n"
    "  in a VISITOR'S browser, against the served cache, and handed its\n"
    "  feature report to JavaScript to draw. That is architecture B' and\n"
    "  Section 3a's Python-assembles / JavaScript-draws split, working end\n"
    "  to end outside Tony's machine for the first time.\n"
    "- **A second exhibit on a page public since July**, reached by the\n"
    "  `?exhibit=` parameter Section 2a designed for exactly this. The\n"
    "  Solar System Explorer is untouched and still loads with no\n"
    "  parameter. Nothing was promoted from a dev page.\n"
    "- **Four defects, three of which no existing check could reach.**\n"
    "  GitHub Pages ran Jekyll and served NO `.py` file in the repository\n"
    "  at all, so `gallery/assembler/` returned 404 -- invisible to\n"
    "  `python -m http.server`, where every previous test had run, and\n"
    "  fixed by one empty `.nojekyll`. The scene axes were pinned, so\n"
    "  nothing the legend did could move the frame. Nine info markers were\n"
    "  drawn with no shells around them, because `feature_renderers.js`\n"
    "  sent a shell's geometry to the legend when it exceeded the frame and\n"
    "  left its marker behind -- a defect that PREDATES this exhibit, lives\n"
    "  in the shared renderer, and Earth would have hit. And segment 2\n"
    "  failed its first real test (L-258).\n"
    "- **The Mode 5 claim, narrowed.** Section 5a justifies the braid's\n"
    "  ordering by saying a wrong radius becomes something Tony's EYES can\n"
    "  catch. `RADIATIVE_ZONE_AU` moved 1.9 percent of a drawn radius --\n"
    "  invisible at any zoom -- and was caught on the live page by READING\n"
    "  THE HOVER. The argument survives and the mechanism was misnamed: the\n"
    "  geometry catches gross errors, and the hover catches everything\n"
    "  else, because it carries the value, the units and the source.\n"
    "  Drawing a feature is what puts its provenance in front of a reader\n"
    "  for the first time.\n"
    "- **Measured, not carried:** eighteen drawable shells, not nineteen.\n"
    "  Eighteen named traces plus eighteen info-marker companions through\n"
    "  the real renderer at gallery `ac9a5c7b`. Counts of \"the Sun's\n"
    "  nineteen values\" elsewhere refer to `constants_new.py` entries, a\n"
    "  different denominator.\n"
    "- **Note:** RICE 5/5/100/3, confirmed by Tony 2026-08-29.\n"
    "**Ref:** L-234 (part-by-part rendering); L-154 (the feature-rendering\n"
    "layer this discharges for one body); L-258; L-260 (what the exhibit\n"
    "still owes); `documentation/HANDOFF_20260829_sun_ships.md`.\n"
    "\n"
)

L260 = (
    "#### [L-260] Sun exhibit finishing items: axis units and the phone\n"
    "<!-- L:260 status:OPEN upd:2026-08-29 section:A flag: rice:3/3/90/1 -->\n"
    "- **The axes carry no units.** Tick labels read \"150k\" with nothing\n"
    "  saying what of. This is copied from the Solar System Explorer's own\n"
    "  convention -- blank axis titles, `title: { text: '', font: { size:\n"
    "  1 } }` -- so it is not a deviation the Sun exhibit introduced.\n"
    "- **It lands differently here.** The Explorer's frame is always about\n"
    "  35 AU. The Sun's runs from 0.26 AU on arrival to 173,250 AU with the\n"
    "  gravitational influence drawn, so a visitor has no way to know the\n"
    "  number is AU rather than km. Every hover on the page carries km AND\n"
    "  AU per the standing convention; the axes are the one surface that\n"
    "  does not. It is the only thing on the live page that is arguably\n"
    "  wrong rather than merely unfinished.\n"
    "- **Mobile is untested, and it cannot be delegated.** Nobody has\n"
    "  opened the exhibit on a phone. The legend is an eighteen-entry\n"
    "  overlay panel and the modebar is hidden below 768 px by the\n"
    "  gallery's existing convention, so the phone experience is unknown --\n"
    "  on a site whose whole premise is that it works on one. Deferred\n"
    "  deliberately by Tony on 2026-08-29 because the major thing was done.\n"
    "  **Tony-action (do):** open\n"
    "  `palomasorrery.com/interactive.html?exhibit=sun` on a phone and say\n"
    "  what it does. Mode 5 is his render and his eyes.\n"
    "- **Note:** RICE 3/3/90/1, confirmed by Tony 2026-08-29.\n"
    "**Gap:** both open. The axis fix is small and can ride with any next\n"
    "gallery patch; the phone read is Mode 5.\n"
    "**Ref:** L-259 (the exhibit itself); orrery-coding-conventions 1.6\n"
    "(the AU hover convention the axes do not follow); gallery-pipeline 1.2\n"
    "(the 768 px breakpoint).\n"
    "\n"
)


L261 = (
    "#### [L-261] Plain speech becomes the default register, not a mode\n"
    "<!-- L:261 status:DONE upd:2026-08-29 section:C flag: rice:4/4/95/1 -->\n"
    "- **Tony's instruction, 2026-08-29:** \"please use plain speech in your\n"
    "  chat as the default.\"\n"
    "- **What was wrong with the old wording.** The Register Rule scoped its\n"
    "  plain-speech rules to an EXPLANATION register -- explanations, design\n"
    "  rationale, as-built narrative. Ordinary delivery prose was not in\n"
    "  that list, so it sat outside the three checks and passed them by not\n"
    "  being subject to them.\n"
    "- **The case.** \"I left it out of the patch rather than expand scope\n"
    "  into the protocol without your word; it's captured as L-258's Gap\n"
    "  with a Tony-action.\" Tony: \"I don't follow.\" Three project labels --\n"
    "  scope expansion, the ledger Gap field, the Tony-action tag -- in one\n"
    "  clause, in a sentence that was not explaining anything, inside a\n"
    "  message that was otherwise readable. Check 2 asks whether a sentence\n"
    "  points at a label instead of saying the thing; it never ran, because\n"
    "  the register it belonged to had not been entered.\n"
    "- **What changed.** The compressed voice keeps its home in\n"
    "  `PROJECT_INSTRUCTIONS.md` and in the skills, where a line is\n"
    "  reference somebody scans because they already own the idea. It\n"
    "  leaves the chat. Recorded in protocol v3.47.\n"
    "- **Note:** RICE 4/4/95/1, confirmed by Tony 2026-08-29. Reach 4\n"
    "  because the rule applies to every message in every session.\n"
    "**Ref:** Register Rule, resident protocol Part 2; L-258 (the patch the\n"
    "opaque sentence was about).\n"
    "\n"
)


L262 = (
    "#### [L-262] The framing smoke test has never run against the page\n"
    "<!-- L:262 status:OPEN upd:2026-08-29 section:A flag: rice:3/4/95/1 -->\n"
    "- **Found by the gallery maintenance runner's first execution**\n"
    "  (L-236), 2026-08-29, which is the argument for the runner made by\n"
    "  the runner.\n"
    "- **`documentation/smoke_framing.js` slices `interactive.html`\n"
    "  between two markers**, `function gridDtick(span) {` and\n"
    "  `async function fetchText(url) {`, and exits immediately with\n"
    "  \"FAIL: helpers not found in page\" when it cannot find them.\n"
    "- **Neither marker has ever existed in that file.** Measured across\n"
    "  the whole history of both files at gallery `c367b262`: `gridDtick`\n"
    "  appears in exactly one commit, `0cabfb3` (2026-08-26, L-238), and\n"
    "  only inside the smoke test itself. The page has `fetchTextOrThrow`\n"
    "  and no `gridDtick` at all. The suite was written against a patched\n"
    "  HTML that was never committed in that shape.\n"
    "- **It has been dead since the day it landed**, three days, and\n"
    "  nothing surfaced it because the file sits in `documentation/` and\n"
    "  was in no routine. Put the check where it runs.\n"
    "- **Note:** RICE 3/4/95/1, confirmed by Tony 2026-08-29. The fix is\n"
    "  either re-pointing the markers at the page's real helpers or\n"
    "  extracting those helpers so both the page and the test read one\n"
    "  copy -- a design call, not a rename, because the page currently\n"
    "  inlines its framing logic.\n"
    "**Gap:** the suite cannot run. Decide which fix, then do it.\n"
    "**Ref:** L-236 (the runner that found it); L-238 (the commit that\n"
    "added the suite); A Check That Cannot Fail Is Not Passing [CRITICAL],\n"
    "resident protocol Part 3.\n"
    "\n"
)

L263 = (
    "#### [L-263] The served chromosphere value is a rounded copy\n"
    "<!-- L:263 status:OPEN upd:2026-08-29 section:A flag: rice:2/3/95/1 -->\n"
    "- **Found by the store-drift check** (L-236) on its first run against\n"
    "  real data, 2026-08-29.\n"
    "- **`CHROMOSPHERE_PHYSICAL_RADII` is 1.00287480236 in the orrery and\n"
    "  1.0028748 in the gallery's `data/objects_config.json`.** They agree\n"
    "  to nine significant figures, so nothing is drawn wrong -- the\n"
    "  difference is about two parts in a billion of a solar radius.\n"
    "- **The class is the point, not the size.** 1.0028748 is the correct\n"
    "  figure to REPORT; it is not a second thing to STORE. A copy held at\n"
    "  a different precision is a shadow constant one digit at a time,\n"
    "  which is One Value, One Home (provenance-discipline 2.7).\n"
    "- **Tony's ruling, 2026-08-29**, and it is why the check is exact\n"
    "  rather than tolerant: significant figures are checked against the\n"
    "  store, not against whether a person catches them. How many figures\n"
    "  a value should carry is settled once, in the orrery. The gallery\n"
    "  carries what the store carries.\n"
    "  **Tony-action (do):** set the value in\n"
    "  `/objects/0/features/solar_atmosphere/chromosphere` to the store's\n"
    "  number. The runner reports it every run until it matches.\n"
    "- **It also names the transport hole from the other side.** The\n"
    "  orrery holds a DERIVATION and the gallery holds a NUMBER, so\n"
    "  changing `CHROMOSPHERE_PHYSICAL_KM` moves one and not the other.\n"
    "  Fixing this value does not fix that.\n"
    "- **Note:** RICE 2/3/95/1, confirmed by Tony 2026-08-29.\n"
    "**Gap:** one value in one file.\n"
    "**Ref:** L-236; L-258 (The Store Carries the Verified Figure);\n"
    "segment 2 in `documentation/MASTER_PLAN_INTERACTIVE_GALLERY.md`\n"
    "Section 5a.\n"
    "\n"
)


# ------------------------------------------------------------------
# The v3.47 protocol entry
# ------------------------------------------------------------------

V347 = (
    "v3.47 (August 29, 2026): One rule amended, and one skill bump\n"
    "recorded a day late.\n"
    "\n"
    "The Register Rule [Part 2] makes PLAIN SPEECH THE DEFAULT. Tony's\n"
    "instruction, 2026-08-29: \"please use plain speech in your chat as the\n"
    "default.\" The earlier wording made plain speech a REGISTER -- one\n"
    "entered for explanations, design rationale and as-built narrative --\n"
    "so ordinary delivery prose sat outside the three checks and passed\n"
    "them by not being subject to them. The compressed voice keeps its\n"
    "home in this document and in the skills, where a line is reference\n"
    "somebody scans because they already own the idea. It leaves the chat.\n"
    "\n"
    "The case that earned it, from the same session and about this same\n"
    "patch: \"I left it out of the patch rather than expand scope into the\n"
    "protocol without your word; it's captured as L-258's Gap with a\n"
    "Tony-action.\" Tony: \"I don't follow.\" Three project labels in one\n"
    "clause, in a sentence that was not explaining anything. Handle L-261.\n"
    "\n"
    "provenance-discipline 2.9 -> 2.10 (L-258). The Store Carries the\n"
    "Verified Figure [CRITICAL], added under Report to the Figures You\n"
    "Have, which governed REPORTING and left the stored value uncovered.\n"
    "Where a source gives a verified figure more precise than the stored\n"
    "value, the store carries the verified figure; rounding happens at the\n"
    "reporting step, never at rest. Founding case: RADIATIVE_ZONE_AU held\n"
    "0.7 beside its own comment saying it rounded 0.713 -- the store\n"
    "recording that it was rounding, and rounding anyway, in a value drawn\n"
    "on a public page. Narrowed in the same breath against the two cases\n"
    "it would damage: a pick from a range stays a declared choice, and a\n"
    "visibility stylization promotes when the physical value becomes\n"
    "drawable rather than for want of digits.\n"
    "\n"
    "Tony's ruling, 2026-08-29, and his reason for making it a SKILL rule\n"
    "rather than a decision: it resolves the same way next month, for a\n"
    "different constant, in a different file. That is Method Belongs to\n"
    "the Skill applied to its own layer.\n"
    "\n"
    "The bump's own record is its own lesson. Steps 1, 2 and 4 travelled\n"
    "together on August 29 -- the version line, skills_index.py, the\n"
    "commit. Step 3, this entry, did not. The manifest going current on\n"
    "its own DISGUISED the omission, exactly as the binding rule warns:\n"
    "the protocol looked updated because half of it was. It surfaced the\n"
    "same day, in the next session, by reading the manifest against the\n"
    "history -- not by any check, because the check that would catch it is\n"
    "L-230, designed and unbuilt.\n"
    "\n"
    "Recorded a day late and said so, rather than backfilled as though it\n"
    "had been here. A document whose subject is anchors being true is the\n"
    "wrong place to be casual about when something was written.\n"
    "\n"
    "Version history: v3.44 moves down to\n"
    "documentation/PROJECT_INSTRUCTIONS_HISTORY.md PART 1 to keep three\n"
    "resident.\n"
    "\n"
)


# ------------------------------------------------------------------
# Literal edits, per file
# ------------------------------------------------------------------

LEDGER_EDITS = [
    (
        "L-236 gains the Sun-ship evidence, the built runner, and its score",

        "**Gap:** designed, not built.\n"
        "- **Note:** RICE 4/4/80/4 -> 3.2 is Claude's proposed score.\n"
        "  **Tony-action (decide):** confirm or redirect.\n"
        "**Ref:** L-188 (the orrery-side maintenance runner this mirrors); L-235.\n",

        "- **Evidence, 2026-08-29.** Three of the four defects in the Sun\n"
        "  ship were on the gallery side and no orrery check could reach any\n"
        "  of them: Pages serving no `.py` at all, orphan info markers in the\n"
        "  shared renderer, and `objects_config.json` drifting from\n"
        "  `constants_new.py`. Measured at gallery `c367b262`: nothing named\n"
        "  maintenance, runner or run_all anywhere in the repo, and the one\n"
        "  real suite -- `tools/test_gallery_cache_builder_offline.py`, 149\n"
        "  checks -- sits in no routine.\n"
        "- **Two checks the first roster did not have**, each of which would\n"
        "  have caught one of that day's failures. *(a) A served-reachability\n"
        "  check:* fetch ONE file per critical-path family from the LIVE site\n"
        "  and require 200 -- an assembler module, the coverage index, a\n"
        "  positions file. It has to run against the CDN, because that is the\n"
        "  thing that was broken. *(b) A store-drift REPORT:* thirty entries\n"
        "  in `objects_config.json` already carry `orrery_constant` pointers\n"
        "  like `constants_new.py::RADIATIVE_ZONE_AU`, and nothing follows\n"
        "  them. A read-only checker that fetches `constants_new.py` at the\n"
        "  orrery HEAD SHA and reports every pointer whose value disagrees\n"
        "  would have caught 0.7 against 0.713 the moment it happened.\n"
        "- **(b) is NOT the transport and does not replace segment 2.** It\n"
        "  moves nothing and fixes nothing. It converts a silent hole into a\n"
        "  loud one for a fraction of the cost, and it can be built BEFORE\n"
        "  the transport rather than instead of it.\n"
        "- **The 2026-08-29 handoff says this work has no ledger handle. It\n"
        "  does** -- this one, opened 2026-08-25. Recorded so the next\n"
        "  session does not mint a second.\n"
        "- **BUILT 2026-08-29 and delivered as `maintenance_run.py` for the\n"
        "  gallery repo root.** Two moments rather than one, which is where\n"
        "  it departs from the orrery's runner: the plain run is offline and\n"
        "  goes before a commit, and `--live` goes after a push, because the\n"
        "  Jekyll failure existed only on the deployed site and only after a\n"
        "  push. Three states, not two: PASS, FAIL, and UNREACHABLE, with\n"
        "  unreachable counted separately and never folded into a passing\n"
        "  total.\n"
        "- **Roster.** Offline: the module atlas generator; the 149-check\n"
        "  cache builder suite; the three Node smoke suites, with Node's\n"
        "  absence REPORTED rather than skipped; and the artifact-1\n"
        "  assembler test, report-only. Live: served reachability against\n"
        "  the CDN, and the store-drift report.\n"
        "- **Two findings on its first run**, both recorded: L-262, the\n"
        "  framing smoke test that has never run; and L-263, a rounded copy\n"
        "  in `objects_config.json`.\n"
        "- **One design change the sandbox forced.** The first version read\n"
        "  any non-200 as a missing file, and a blocking proxy answering 403\n"
        "  reported as the whole site being gone. Only a 404 is missing now;\n"
        "  anything else is unreachable, and a blanket failure across every\n"
        "  file reports as unreachable rather than crying wolf. A real\n"
        "  Jekyll failure is asymmetric -- the `.py` files 404 while the\n"
        "  page returns 200 -- and that asymmetry is the signal.\n"
        "- **No dashboard entry, deliberately.** The dashboard lives in the\n"
        "  orrery, so a button there would reach into a sibling directory,\n"
        "  which is the same cross-repo reach that put this runner in the\n"
        "  gallery. VS Code's Run button from the gallery root instead.\n"
        "**Gap:** built and delivered, not yet committed. **Tony-action\n"
        "(do):** commit `maintenance_run.py` to the gallery repo root; this\n"
        "item closes on that commit. Left OPEN rather than marked DONE in\n"
        "advance, because a ledger row claiming a file is committed before\n"
        "it is committed is a claim nothing can check.\n"
        "- **Note:** RICE 4/4/80/4 -> 3.2, confirmed by Tony 2026-08-29.\n"
        "**Ref:** L-188 (the orrery-side maintenance runner this mirrors);\n"
        "L-235; L-258 (the store drift check would have caught it); L-259;\n"
        "L-262 and L-263 (its first two findings).\n",
    ),
    (
        "L-237 gains the stale T3 expectation the runner surfaced",

        "**Gap:** re-cut it. Pair with the L-235 T5 fix -- re-cutting a record\n",

        "- **Its T3 check is also stale, surfaced 2026-08-29** by the gallery\n"
        "  maintenance runner's first execution (L-236). T3 asserts Earth's\n"
        "  feature set and now sees the Sun's five families beside it, so\n"
        "  the suite exits 1 on an expectation written before the Sun\n"
        "  landed. It is carried as report-only in the runner and does not\n"
        "  gate, but it is noise on every run until the expectation moves.\n"
        "**Gap:** re-cut it. Pair with the L-235 T5 fix -- re-cutting a record\n",
    ),
    (
        "L-256's RICE is confirmed; the dict ruling stays open",

        "  **Tony-action (decide):** confirm or redirect the score, and rule on\n"
        "  which dict joins the beta (`spectral_subclass_temps`, 9 entries and\n",

        "  RICE 3/3/70/2 confirmed by Tony 2026-08-29.\n"
        "  **Tony-action (decide):** rule on\n"
        "  which dict joins the beta (`spectral_subclass_temps`, 9 entries and\n",
    ),
    (
        "L-257's RICE is confirmed",

        "- **Note:** RICE 2/3/60/2 is Claude's proposed score.\n"
        "  **Tony-action (decide):** confirm or redirect.\n",

        "- **Note:** RICE 2/3/60/2, confirmed by Tony 2026-08-29.\n",
    ),
    (
        "L-256 gains its 2.9 and 2.10 lines",

        "**Ref:** L-181 (single-source-of-truth constant layer); L-192 (the\n",

        "- **2.9 (2026-08-28).** The Gate Binds at SERVING becomes The Gate\n"
        "  Binds at EXPORT, on Tony's ruling: provenance is settled before a\n"
        "  value leaves the orrery for the gallery cache, because there is no\n"
        "  provenance checker in the gallery. Verified before the edit rather\n"
        "  than assumed -- `provenance_scanner.py` exists only in the orrery\n"
        "  repo, and the nightly builder scores nothing. A gate at\n"
        "  publication would sit downstream of the last instrument in\n"
        "  existence, which is A Check That Cannot Fail Is Not Passing in the\n"
        "  pipeline layer. Recorded in protocol v3.46.\n"
        "- **2.10 (2026-08-29).** The Store Carries the Verified Figure\n"
        "  [CRITICAL], under Report to the Figures You Have, which governed\n"
        "  REPORTING and left the stored value uncovered. Founding case and\n"
        "  fallout are at L-258. Recorded in protocol v3.47 -- a day late,\n"
        "  and that delay is itself recorded there.\n"
        "**Ref:** L-181 (single-source-of-truth constant layer); L-192 (the\n",
    ),
    (
        "L-260, L-262 and L-263 open in section A",

        "## PENDING ACTION (Tony-side)\n",

        L260 + L262 + L263 + "## PENDING ACTION (Tony-side)\n",
    ),
    (
        "L-258, L-259 and L-261 file in the reconciled archive",

        "#### [L-255] Skill bumps of 2026-08-26 -- handle reserved, block never written\n",

        L258 + L259 + L261
        + "#### [L-255] Skill bumps of 2026-08-26 -- handle reserved, block never written\n",
    ),
]

TESTS_EDITS = [
    (
        "test_radiative_zone_au: pinned literal -> ratio bound",

        'def test_radiative_zone_au_derived_from_solar_radius():\n'
        '    """RADIATIVE_ZONE_AU must equal 0.7 * SOLAR_RADIUS_AU (standard solar model)."""\n'
        '    expected = 0.7 * SOLAR_RADIUS_AU\n'
        '    assert abs(RADIATIVE_ZONE_AU - expected) < 1e-15, \\\n'
        '        f"RADIATIVE_ZONE_AU = {RADIATIVE_ZONE_AU}, expected {expected} (derivation broken)"\n',

        'def test_radiative_zone_au_derived_from_solar_radius():\n'
        '    """RADIATIVE_ZONE_AU is a fraction of the solar radius, inside the\n'
        '    convection-zone base implied by Christensen-Dalsgaard, Gough &\n'
        '    Thompson (1991), ApJ 378:413 -- depth 0.287 +/- 0.003 R_sun, so a\n'
        '    base of 0.710 to 0.716 R_sun.\n'
        '\n'
        '    Holds no copy of the measured fraction. Restated 2026-08-29\n'
        '    (L-258): the pinned form asserted 0.7 and failed correctly when\n'
        '    the store was corrected to 0.713. A re-sourcing that leaves the\n'
        '    published band still fires; a rounding inside it does not.\n'
        '    """\n'
        '    ratio = RADIATIVE_ZONE_AU / SOLAR_RADIUS_AU\n'
        '    low, high = 0.710, 0.716\n'
        '    eps = 1e-9  # float round-trip on (k * x) / x, not a physical margin\n'
        '    assert low - eps <= ratio <= high + eps, \\\n'
        '        f"RADIATIVE_ZONE_AU / SOLAR_RADIUS_AU = {ratio}, outside the " \\\n'
        '        f"{low}-{high} R_sun convection-zone base band"\n',
    ),
    (
        "test_core_au: pinned literal -> ratio bound",

        'def test_core_au_derived_from_solar_radius():\n'
        '    """CORE_AU must equal 0.2 * SOLAR_RADIUS_AU (standard solar model)."""\n'
        '    expected = 0.2 * SOLAR_RADIUS_AU\n'
        '    assert abs(CORE_AU - expected) < 1e-15, \\\n'
        '        f"CORE_AU = {CORE_AU}, expected {expected} (derivation broken)"\n',

        'def test_core_au_derived_from_solar_radius():\n'
        '    """CORE_AU is a fraction of the solar radius, inside the\n'
        '    conventional 0.2-0.25 R_sun core range (Carroll & Ostlie 2017,\n'
        '    Ch. 11; Bahcall, Pinsonneault & Basu 2001, ApJ 555:990).\n'
        '\n'
        '    Holds no copy of the measured fraction. Restated 2026-08-29\n'
        '    (L-258) alongside its radiative-zone twin, which had the same\n'
        '    shape and fired the moment its value moved. The store currently\n'
        '    draws at the low end of the range; promoting it off 0.2 must not\n'
        '    make this test stale.\n'
        '    """\n'
        '    ratio = CORE_AU / SOLAR_RADIUS_AU\n'
        '    low, high = 0.20, 0.25\n'
        '    eps = 1e-9  # float round-trip on (k * x) / x, not a physical margin\n'
        '    assert low - eps <= ratio <= high + eps, \\\n'
        '        f"CORE_AU / SOLAR_RADIUS_AU = {ratio}, outside the " \\\n'
        '        f"{low}-{high} R_sun core range"\n',
    ),
]

PROTO_EDITS = [
    (
        "header to v3.47, anchored at 8b762e04",

        "Tony Quintanilla, PE | Claude | v3.46 | August 28, 2026\n"
        "\n"
        "Cut from a263f73d at https://github.com/tonylquintanilla/palomas_orrery\n",

        "Tony Quintanilla, PE | Claude | v3.47 | August 29, 2026\n"
        "\n"
        "Cut from 8b762e04 at https://github.com/tonylquintanilla/palomas_orrery\n",
    ),
    (
        "the v3.47 entry, newest first",

        "v3.46 (August 28, 2026): No rule changed in this document. One skill\n",

        V347 + "v3.46 (August 28, 2026): No rule changed in this document. One skill\n",
    ),
    (
        "Register Rule: plain speech becomes the default, not a register",

        "Register Rule\n"
        "The protocol's compressed voice (\"the SHA is the round trip\") is reference  -- \n"
        "a line you scan when you already own the idea. Explanations, design rationale,\n"
        "as-built narrative, and conversational responses are a different job and take\n"
        "a different voice.\n"
        "\n"
        "In explanation register:\n"
        "- Lead with the claim in one plain sentence. Detail after.\n"
        "- One idea per sentence. Two subordinate clauses means split it.\n"
        "- No aphorisms. In an explanation, say what happened, not the shorthand.\n",

        "Register Rule\n"
        "PLAIN SPEECH IS THE DEFAULT. Everything Claude says in conversation --\n"
        "answers, delivery notes, findings, questions, the sentence explaining\n"
        "why something was left out -- is written the way a knowledgeable person\n"
        "talks.\n"
        "\n"
        "The protocol's compressed voice (\"the SHA is the round trip\") keeps its\n"
        "home in THIS document and in the skills, where a line is reference\n"
        "somebody scans because they already own the idea. It does not belong in\n"
        "chat. Plain speech is not a register Claude enters for explanations; it\n"
        "is how Claude writes unless Tony asks for something else.\n"
        "\n"
        "Always, and not only when explaining:\n"
        "- Lead with the claim in one plain sentence. Detail after.\n"
        "- One idea per sentence. Two subordinate clauses means split it.\n"
        "- No aphorisms. Say what happened, not the shorthand.\n",
    ),
    (
        "Register Rule: the amendment's own origin note",

        "only partly. The rule's own backstop was the part that had failed.)\n",

        "only partly. The rule's own backstop was the part that had failed.)\n"
        "\n"
        "(Amended August 29, 2026, on Tony's instruction: \"please use plain\n"
        "speech in your chat as the default.\" The earlier wording scoped the\n"
        "plain-speech rules to an EXPLANATION register, which left ordinary\n"
        "delivery prose outside them -- it passed the three checks by not being\n"
        "subject to them. The case: \"I left it out of the patch rather than\n"
        "expand scope into the protocol without your word; it's captured as\n"
        "L-258's Gap with a Tony-action.\" Tony: \"I don't follow.\" Three\n"
        "project labels in one clause, in a sentence explaining nothing, in a\n"
        "message that was otherwise fine. Handle L-261.)\n",
    ),
]


# The v3.44 move is NOT a literal edit. The block is LIFTED from the
# protocol by its own boundaries and inserted into the history file
# byte-for-byte, so the moved entry cannot differ from the resident one.
V344_START = "v3.44 (August 26, 2026): No rule changed in this document. TWO skill\n"
V344_END = "Functional for Claude, readable for human, signal preserved.\n"
V344_MUST_END_WITH = "resident.\n\n"

HISTORY_ANCHOR = (
    "### Preserved verbatim: v3.29 Technical lessons (now field notes in skills)\n"
)
MOVED_NOTE = (
    "\n"
    "(Moved down from the resident protocol on 2026-08-29 when v3.47\n"
    "made a fourth entry.)\n"
    "\n"
)


def read_guarded(path, name, want_md5):
    """Read a file and refuse unless its CONTENT is what we expect.

    The guard is computed on the LF form, not on the raw bytes. A Windows
    tool that writes in text mode -- ledger_index.py among them -- flips
    a whole file to CRLF without changing a character of it, and git
    normalises that back to LF on commit, so the repo and the working
    copy legitimately disagree byte-for-byte while agreeing completely on
    content. Guarding the raw bytes refuses that, which is a false alarm
    on the one check that has to be believed.

    Returns (content, was_crlf). The style is carried so the file is
    written back the way it was found.
    """
    print("")
    print("target :", path)
    if not os.path.isfile(path):
        print("REFUSED: no such file.")
        return None, False
    with open(path, "rb") as fh:
        raw = fh.read()

    was_crlf = b"\r\n" in raw
    content = raw.replace(b"\r\n", b"\n") if was_crlf else raw

    actual = hashlib.md5(content).hexdigest()
    print("md5    : %s (expected %s)%s"
          % (actual, want_md5, "   [CRLF working copy]" if was_crlf else ""))
    if actual != want_md5:
        print("REFUSED: %s is not in the state this patch expects." % name)
        print("         Nothing written to any file. Re-cut the patch")
        print("         against the current bytes.")
        return None, False
    return content, was_crlf


def apply_literal(text, edits):
    """Check every anchor matches exactly once, then apply. None on refusal."""
    for label, old, _new in edits:
        n = text.count(old)
        print("  anchor x%d  %s" % (n, label))
        if n != 1:
            print("REFUSED: anchor matched %d times, expected 1." % n)
            print("         Nothing written to any file.")
            return None
    for _label, old, new in edits:
        text = text.replace(old, new, 1)
    return text


def ascii_ok(raw, out, label):
    before = sum(1 for c in raw if c > 127)
    after = sum(1 for c in out if c > 127)
    print("  non-ascii bytes: %d -> %d   (%s)" % (before, after, label))
    if after != before:
        print("REFUSED: the patch introduced non-ASCII text.")
        print("         Nothing written to any file.")
        return False
    return True


def main():
    print("patch_ledger_and_protocol_20260829.py")
    root = find_repo_root()
    if root is None:
        print("REFUSED: could not find %s. Move this script into the ORRERY"
              % PROBE)
        print("         repo root and run it again.")
        return 1

    staged = []

    # ---- 1. ledger --------------------------------------------------
    path = os.path.join(root, LEDGER)
    raw, crlf = read_guarded(path, LEDGER, LEDGER_MD5)
    if raw is None:
        return 1
    text = apply_literal(raw.decode("utf-8"), LEDGER_EDITS)
    if text is None:
        return 1
    out = text.encode("utf-8")
    if not ascii_ok(raw, out, LEDGER):
        return 1
    staged.append((path, raw, out, crlf))

    # ---- 2. tests ---------------------------------------------------
    path = os.path.join(root, TESTS)
    raw, crlf = read_guarded(path, TESTS, TESTS_MD5)
    if raw is None:
        return 1
    text = apply_literal(raw.decode("utf-8"), TESTS_EDITS)
    if text is None:
        return 1
    out = text.encode("utf-8")
    if not ascii_ok(raw, out, TESTS):
        return 1
    staged.append((path, raw, out, crlf))

    # ---- 3. protocol: two literal edits, then lift v3.44 out --------
    path = os.path.join(root, PROTO)
    raw, crlf = read_guarded(path, PROTO, PROTO_MD5)
    if raw is None:
        return 1
    text = apply_literal(raw.decode("utf-8"), PROTO_EDITS)
    if text is None:
        return 1

    for label, marker in (("v3.44 start", V344_START), ("v3.44 end", V344_END)):
        n = text.count(marker)
        print("  marker x%d  %s" % (n, label))
        if n != 1:
            print("REFUSED: marker matched %d times, expected 1." % n)
            print("         Nothing written to any file.")
            return 1

    i = text.index(V344_START)
    j = text.index(V344_END)
    if not i < j:
        print("REFUSED: v3.44 end marker precedes its start marker.")
        return 1
    v344 = text[i:j]
    if not v344.endswith(V344_MUST_END_WITH):
        print("REFUSED: the lifted v3.44 block does not end where expected.")
        print("         Nothing written to any file.")
        return 1
    print("  lifted v3.44: %d bytes" % len(v344))

    text = text[:i] + text[j:]
    out = text.encode("utf-8")
    if not ascii_ok(raw, out, PROTO):
        return 1
    staged.append((path, raw, out, crlf))

    # ---- 4. history: receive v3.44 verbatim -------------------------
    path = os.path.join(root, HISTORY)
    raw, crlf = read_guarded(path, HISTORY, HISTORY_MD5)
    if raw is None:
        return 1
    text = raw.decode("utf-8")
    n = text.count(HISTORY_ANCHOR)
    print("  anchor x%d  v3.44 lands above the preserved-lessons block" % n)
    if n != 1:
        print("REFUSED: anchor matched %d times, expected 1." % n)
        print("         Nothing written to any file.")
        return 1
    insert = v344.rstrip("\n") + "\n" + MOVED_NOTE
    text = text.replace(HISTORY_ANCHOR, insert + HISTORY_ANCHOR, 1)
    out = text.encode("utf-8")
    if not ascii_ok(raw, out, HISTORY):
        return 1
    staged.append((path, raw, out, crlf))

    # ---- every guard on every file has passed; now write ------------
    print("")
    for path, raw, out, crlf in staged:
        # Written back the way it was found. Flipping a 700 KB file's line
        # endings would show up in GitHub Desktop as every line changed,
        # burying the eight edits that actually matter.
        backup = raw.replace(b"\n", b"\r\n") if crlf else raw
        final = out.replace(b"\n", b"\r\n") if crlf else out
        with open(path + ".bak", "wb") as fh:
            fh.write(backup)
        with open(path, "wb") as fh:
            fh.write(final)
        print("WROTE   %s  (%d -> %d bytes%s)"
              % (path, len(backup), len(final), ", CRLF" if crlf else ""))

    print("")
    print("Next, in this order:")
    print("  1. ledger_index.py     -- regenerates the index tables")
    print("  2. maintenance_run.py  -- Constants relations should read 21/21")
    print("")
    print("Then commit all four files together. That is step 4 of the")
    print("binding rule, and it is the whole point of doing this in one")
    print("patch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
