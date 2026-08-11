# Session Handoff -- August 11, 2026

**Built on `ba2d6f0bc767b4f010aabd8e72c41374263431e0`
at https://github.com/tonylquintanilla/palomas_orrery (branch main).
Gallery pinned separately at `d5437f08f94feccd70b697729b52cdc44df8b51d`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Both HEADs verified live at session close.**

**Type: RECORD-LAYER SESSION.** No orrery code changed. Every deliverable
was a transactional patch against a document, a skill, or the dashboard.

**Prepared:** August 11, 2026 by Claude Opus 5, Tony Quintanilla
integrator. Mobile for the first half, at the machine for the second.

**Continues from** `documentation/HANDOFF_20260810_session.md`
(anchored `826a932`). That handoff's entire protocol-and-skills do-list is
now closed. Its provenance and ledger items are NOT, and they are what
this session hands forward.

**Closes:** the v3.36 Register Rule amendment; "The Artifact Bounds the
Audit"; the protocol trim; both pending skill bumps; the master plan's
four stale decisions; the dashboard's broken builder entry.
**Opens:** nothing new in the ledger. Three cleanup items below.

---

## Who you are working for

Tony Quintanilla, PE -- a retired civil and environmental engineer,
artist, and anthropologist. Not a professional programmer, not a formally
trained astronomer. He builds Paloma's Orrery through conversational AI
collaboration and holds sole commit authority and final judgment. The
codebase's structure and discipline are products of that collaboration;
do not read code quality as evidence of his personal programming fluency.

He runs Python by opening a file in VS Code and clicking Run, and works
through GitHub Desktop. Deliver runnable transactional patch scripts with
the run command in the docstring.

**Read the Process section at the bottom before your first substantive
reply.** The v3.36 Register Rule is now IN the protocol, so it is binding
rather than advisory -- but the previous handoff's guidance on how it
actually plays out is still the useful part.

---

## What happened

Seven pushes, each round-trip verified. The whole session was record-layer
work: bringing the protocol, the skills, and the master plan into
agreement with rulings Tony had already made, plus one dashboard fix and
the first manual gallery build.

| SHA | What |
|---|---|
| `0bf0d79` | v3.36 Register Rule applied; dashboard manual-builder entry |
| `22b0db3` | protocol header corrected to v3.36 |
| `8e4b5ca` | Artifact Bounds added; protocol trimmed; lessons cut |
| `b1937a6` | fourteen unique lessons restored; LESSONS_ARCHIVE rewritten |
| `c1ba36e` | provenance-discipline 1.8, gallery-cache-builder 1.3, manifest |
| `4509c08` | master plan v18 rulings + ASCII normalization |
| `ba2d6f0` | summary header reconciled to the patched plan |

Gallery: `d5437f0`, the first manual build.

---

## Rulings (Tony, this session)

1. **The lessons trim was reversed and redone.** A first cut moved all
   forty-one Part 5 process and philosophical lessons to an archive file,
   leaving the protocol with a pointer. Tony read it and said the lessons
   felt important. He was right and the cut was wrong: an archive file has
   NO TRIGGER. A skill fires on task match and the ledger is read at
   session start, but nothing opens an archive, so the fourteen lessons
   with no counterpart elsewhere would have left the system silently.
   The v3.30 precedent (technical lessons into skills) does not transfer,
   because skills fire.

   **The standing distinction that came out of it:** a lesson duplicated
   by a firing rule is redundant; a lesson that is nowhere else IS the
   archive. Twenty-seven were removed on that basis, each verified against
   the file rather than asserted. Fourteen stayed resident.

2. **ASCII normalization scope for the master plan.** Do the mechanical
   punctuation, redraw the diagram deliberately, leave the primes alone.
   `B'` is a NAME appearing in seven files including the ledger, so
   normalizing it in one document would split the term.

3. **The scheduled nightly stays retired, and it is now proven.** First
   manual build ran clean end to end: 25 modifications, 1 addition, zero
   deletions -- the exact opposite shape of the August 10 incident.

4. **A summary's anchor moves; a handoff's does not.** Tony proposed
   updating the old handoff's gallery SHA after the manual build moved it.
   Ruled against, and the reasoning is worth keeping: a handoff's
   `built on <SHA>` is a historical claim about the state a session was
   built on, and rewriting it makes the document assert it was built on a
   commit that did not exist when it was written. A SUMMARY claims to
   describe current state, so its anchor is a claim about now and should
   move. Both were applied.

---

## What is now true that was not

**Protocol at v3.37, 849 lines** (from 882). Carries the Register Rule
message-level Check 0, "The Artifact Bounds the Audit" in Part 3, and a
Part 5 holding only lessons that exist nowhere else.

**All ten skills reconciled across three stores.** provenance-discipline
1.8 (Worksheet First, Annotation Second [CRITICAL]; two field notes on
evidence-as-received and over-confession). gallery-cache-builder 1.3
(Operating mode section, Layer 3 marked RETIRED not deleted).

**Master plan current.** Decision 12 RATIFIED with both conditions, 16 and
17 RULED, 18 added for the three-zone registry shape. Layer 3 retired in
both places it appeared. 27 non-ASCII characters remain, all primes.

**Dashboard builder entry works.** The old Gallery & Web entry launched
from `tools/`, where the builder's relative `--config` default cannot
resolve, so it had never run. Replaced with a Developer Tools entry
launching from the gallery repo root, plus `wraplength=600` on card
descriptions, which had been running off the right edge.

---

## Two guard catches worth reading

Both are mine, both cost a round trip and nothing else, and both are
already-documented failure modes doing exactly what they exist for.

**A patch anchor built from memory of a file rather than the file.** The
master plan's dependency diagram has 14 connector dashes on one line; the
anchor I wrote had 13. Zero matches, patch refused. This is the
safe-file-editing field note of August 7 recurring verbatim. Build
anchors from the bytes.

**An expected-count check that caught incomplete accounting.** The ASCII
patch expected 28 non-ASCII characters to remain and found 40. I had
assumed every check mark and circle lived inside the diagram; nine and
four respectively live elsewhere in the file. The count refused and
nothing was written. The check stays in the delivered script with a note
saying what it caught, so the number does not read as decorative.

Neither was caught by review. Both were caught by a machine check that
had no opinion about how confident the reasoning sounded.

---

## (do) -- outstanding

Nothing here is new. Items 1-6 carry forward from the August 10 handoff
unchanged; 7-9 are cleanup this session created.

### Provenance -- needs Tony's judgment, not a patch

1. **Resolve six `duplicate_identity` sites** against the sources:
   `constants_new.py` 423, eris 218, mercury 49, pluto 41,
   `shell_configs.py` 128, venus 528. Each needs a look at the source to
   decide whether one annotation is redundant or a checker name is wrong.
   This is reading, and it is the natural first item of a working session.

### Ledger

2. **Open a handle for the second L-190 class:** claims about the codebase
   that no tooling checks. Evidence now stands at eight instances: 772
   lines, 37 entries, 126 tooltips, 45 assignments, 3-vs-8 annotations,
   the 248-sites grep artifact, plus two from this session -- an
   "unresolved oddity" that had been answered three weeks earlier in
   `M2_TESTING_PROTOCOL_ADDENDUM.md` line 749, and the protocol's own
   claim that the lessons archive was preserved in the ledger appendix
   when it never had been. None changed an outcome; no tool caught any.

   That second one is the strongest evidence yet, because it is not a
   miscount -- it is a documented backup that did not exist, unchallenged
   from July 1 to August 11.

3. **Record the scheduled-build retirement in the ledger.** The skill is
   done (1.3) and the plan is done; the ledger's deployment-model decision
   block near line 4555 still describes the scheduled nightly as the
   operating model. Note the pre-commit fail-safe as designed-but-not-
   built, relevant only if the schedule returns, a second person gains
   commit access, or the build ever runs unattended by any mechanism.

4. **Note on the L-191 block:** manual-scale instructions are
   orrery-surface-only and must not be collapsed into shared text that
   reaches the transport. 32 live in `shell_configs.py` as copies of
   shell-module text.

5. **Record the eighteen inline literals** duplicating cited constants:
   `KM_PER_AU` 14 sites in 8 files, `MOON_RADIUS_KM` 3 in 2,
   `SUN_RADIUS_KM` 2 in 1. Same violation as the shadow constant but
   inline in f-strings rather than named assignments, so the scanner sees
   one of nineteen. Scope-and-sequence work, distinct from L-181's
   migration, and evidence for item 2.

6. **Ledger tooltip count: 124, not 126.** Two of the 126 grep matches are
   documentation -- the module docstring at line 12 and a comment at line
   2062. Real key definitions: 83 in SHELL_CONFIGS + 41 in CUSTOM_SHELLS.
   Two ledger sites carry 126, one of which contradicts its own
   "83 sphere + 41 custom" breakdown in the same bullet. Also check the
   historical entry near line 5357.

### Cleanup this session created

7. **Three PREVIEW_ files were committed to `documentation/` and should
   come out:** `PREVIEW_LESSONS_ARCHIVE.md`,
   `PREVIEW_LESSONS_ARCHIVE_after.md`, `PREVIEW_LESSONS_REMOVED_v337.md`.
   These were read-before-you-run previews, not deliverables. The real
   record is `documentation/LESSONS_ARCHIVE.md`, which is current and
   should stay.

8. **`documentation/patch_protocol_v337.py` is the SUPERSEDED first cut**
   -- the one that moved all forty-one lessons. It is in the repo
   alongside `patch_protocol_restore_lessons.py`, which reversed it.
   Either delete it or add a header line saying it was superseded the same
   day, so no future session runs it thinking it is the current trim.

9. **The protocol still claims the lessons archive lives in the ledger.**
   The Lessons Archive section says the complete archive is preserved
   verbatim in LEDGER_CONSOLIDATED.md's Protocol Version History appendix.
   That appendix is a per-version change log and has never carried those
   lists. The claim was left alone deliberately -- deciding where
   institutional memory should live is its own conversation and should not
   ride inside a trim -- but it is still false and should be either fixed
   or made true.

---

## (decide) -- still open

1. **The constructor-call count in master plan decision 12.** It said two
   assignments contain constructor calls. Measured: one,
   `HORIZONS_MAX_DATE = datetime(...)`, with no calls nested in any of the
   six derived expressions. Staleness explains a count going UP, not down,
   so this needs a look rather than a correction. Recorded as open IN the
   plan now, so it will not be quietly patched over.

2. **Jupiter's ring entry count: 4 or 5.** The August 7 summary said five;
   the August 10 session counted four; the plan's own v17 correction note
   says "Jupiter is 4, not 5" while decision 16's Fable recommendation
   still says 5. This matters because the pilot is scoped by it, and it
   should be settled by an AST walk before the pilot starts, not argued.

3. **Where the L-188 run-all push-gate binding lands** -- L-188 or L-184.

4. **Migration shape and per-body sequence beyond Jupiter** (L-181). Order
   is settled; the detail wants Jupiter's ring entries in view.

5. **Saturn `thickness_km`:** absent from the served cache, but is it
   absent from the ORRERY? If the orrery draws Saturn's rings with a
   thickness, the number exists in code and the gap is transport. One look
   at the file settles it.

---

## Next session

**L-189 first**, per Tony's standing order -- the provenance scanner's run
history and run-to-run delta, built fresh rather than at the end of a long
session. The design input from August 10 still stands and is still the
material part:

- The history must carry a DECLARED expected cadence. A file that only
  accumulates runs cannot report a run that never happened.
- The check cannot live inside the thing it watches. Put it in the L-188
  maintenance runner, which makes L-188 the trigger and L-189 the data.
- Report the DELTA, not the total. Two scanner runs twenty minutes apart
  both read 880 findings while three real events moved underneath.
- Follow the gallery builder's existing per-run record shape
  (`data/solar-system/raw/runs/<timestamp>.json`) rather than inventing
  one.
- Remember the scanner scans itself, so the first run after L-189 lands
  shows a delta that IS the change.

**The retirement made this MORE load-bearing, not less.** A manual build
has no expected time at all, so an explicit staleness check is now the
only thing that can report the served data is eleven days old.

Then the do-list -- item 1 is the natural opener, since it is reading with
material in front of Tony, which is the layout that produces findings.
Then the migration shape conversation, then Track 0 proper.

---

## Process -- read this before your first substantive reply

The Register Rule is now in the protocol at v3.37 and is binding. Its
message-level check is the one that matters:

**Check 0: does this message ask Tony for ONE thing?** A finding, a
recommendation, an uncertainty, and a new question are four things. Send
the one that is due; the rest wait or go in a file. A message can pass the
paragraph-level checks and still be unusable, because the load is the
COUNT of open items, not the density of any one.

Two supporting defaults, both binding: **answer first, evidence on
request** -- how a number was checked is your work, not Tony's. And
**capture goes in a file, not in the conversation** -- ledger material and
finding lists are things Tony opens at his computer.

Do not rely on Tony saying "opaque." By the time a message is dense enough
to flag, reading it to the end is already the cost. The check runs on your
side before sending. "Just the decision" is his second lever and strips
everything except the ruling being asked for.

**The second failure mode, distinct from density.** You do not have deep
understanding of this codebase -- you have what you grepped in the current
session. Raising something usually means you just found it, not that you
weighed it against the project and judged it important. **Say which it
is.** "Found this" versus "this should change what you do next." Most
findings are the first kind, and presenting them identically makes Tony
carry the sorting.

**What this session confirmed about that.** Tony reversed a recommendation
of mine on the lessons trim, and the reversal produced a better rule than
the original proposal had. He caught it because the cut was laid out in
front of him, not because he audited it. The layout is Claude's; the
noticing is Tony's; neither half produces the finding alone.

---

*Handoff prepared August 2026 with Anthropic's Claude Opus 5, built on
`ba2d6f0bc767b4f010aabd8e72c41374263431e0` at
https://github.com/tonylquintanilla/palomas_orrery and
`d5437f08f94feccd70b697729b52cdc44df8b51d` at
https://github.com/tonylquintanilla/tonyquintanilla.github.io*
