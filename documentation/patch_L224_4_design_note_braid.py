"""
patch_L224_4_design_note_braid.py

Writes documentation/DESIGN_NOTE_20260822_braid_and_citation_kind.md --
the three rulings settled in conversation on 2026-08-22 that live
nowhere else.

WHY A DESIGN NOTE RATHER THAN THE EDITS THEMSELVES
    A later session can read Section 5a and write a correct patch. What
    it cannot reconstruct is WHY -- that the provenance prefix does not
    terminate at 8 clean claims out of 107, that step three is what
    gives provenance a render to be checked against, and that "The
    Artifact Bounds the Audit" already contained the answer and needed
    one word changed. That argument exists in one conversation.

    So this note carries the reasoning and leaves the mechanical work
    -- the 5a revision, the skill bump, the builder change -- to a
    fresh session with a clean read. Each is easier once this exists.

HOW TO RUN
    Save into the repo ROOT, open in VS Code, click Run. It refuses if
    the file already exists. Then commit, push, and archive this script
    to documentation/.

PERMANENT vs DISPOSABLE
    Disposable. The note is the permanent half.

Built on 96707590ba445c58066787aef03299174a8f158b at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Written August 22, 2026 with Anthropic's Claude Opus 5.
"""

import os
import sys

OUT = os.path.join("documentation",
                   "DESIGN_NOTE_20260822_braid_and_citation_kind.md")
DOC = '# Design note -- 2026-08-22: the braid, the third part of a citation, and three dispatch fields\n\n**Built on `96707590ba445c58066787aef03299174a8f158b` at\nhttps://github.com/tonylquintanilla/palomas_orrery (branch main).\nGallery at `22771cac`. Written August 22, 2026 with Anthropic\'s\nClaude Opus 5.**\n\nThis document exists because three things were settled in conversation\non 2026-08-22 and lived nowhere else. Each is a RULING with its\nreasoning attached, not a status report. The mechanical work they\nimply -- the Section 5a revision, the skill bumps, the builder change\n-- is deliberately NOT done here: those are better done fresh against\na clean read, and each is easier once this exists.\n\nA later session can reconstruct WHAT was decided from the ledger. It\ncannot reconstruct WHY. That is what this file carries.\n\n---\n\n## 1. The braid -- provenance is scoped to the artifact, not a gate\n\n**Tony\'s ruling, 2026-08-22. Requires a Section 5a revision to\n`MASTER_PLAN_INTERACTIVE_GALLERY.md`; the readable summary follows.**\n\n### The problem, stated as a number\n\nStep one of the critical path is "make the orrery right." Of 107\nverification claims, 8 are clean. The scanner reports 292 Tier-1\nfindings tree-wide. On 2026-08-22 a full session went to ONE solar\nshell -- the streamer belt -- which is not in Artifact 2 and does not\nblock it.\n\nAt that rate the prefix does not terminate. **A precondition that does\nnot terminate is not a plan.** Nothing ships while it runs, and the\naudit\'s denominator grows whenever anyone thinks of something -- which\nis the exact tell the existing rule names.\n\n### The rule that already contained the answer\n\n`PROJECT_INSTRUCTIONS.md` Part 3, "The Artifact Bounds the Audit":\nscope is what the orrery RENDERS. Closed at any commit, open over\ntime. That rule bounds WHICH values are in scope.\n\nThe braid extends it by one word. **Priority is what the NEXT ARTIFACT\nrenders.** Artifact 2 is Jupiter and Saturn with rings and radiation\nbelts: seven Saturn rings, four Jupiter rings, the belts. That is a\ncountable slice with an end, and finishing it ships something.\n\nThe general audit does not stop. It stops being a GATE.\n\n### Step three comes first, and this is the load-bearing part\n\nTwo lines in `resolver.py` discard every ring radius one step before\nanything could use them, and there is no browser code that draws a\nring at all. That work depends on NOTHING -- the data is already in\nthe served cache, including all seven of Saturn\'s rings and all four\nof Jupiter\'s with their belts and parameters.\n\nThe master plan holds step three back to avoid locking unverified\nnumbers into a fingerprinted reference artifact. That reasoning is\nsound and it conflates two separable things: BUILDING the rendering\nlayer, and LOCKING Artifact 2. Rings can be drawn without being\nfingerprinted.\n\nDoing it in that order pays for itself, and the argument is this\nproject\'s own:\n\n> Right now the ring provenance is an audit of numbers nobody can see\n> -- text checked against text. That is precisely the mode that\n> produced three separate failures on 2026-08-22 (Section 2 below).\n> Once the assembler draws, a wrong ring radius becomes something\n> Tony\'s EYES can catch. The resident gate says the render is ground\n> truth and the render wins when it disagrees with a code reading.\n> Step three is what gives the provenance work a render to be checked\n> against.\n\n### The resulting order\n\n1. Step three -- the rendering layer. Rings on screen, unfingerprinted.\n2. Artifact 2\'s provenance slice -- the rings and belts, and only those.\n3. Lock Artifact 2.\n4. Ship.\n\nThe five steps of Section 5a DO NOT MOVE. They were confirmed\nunchanged on 2026-08-16 and 2026-08-22 did not change them. What\nchanges is that step one stops being a gate and becomes a per-artifact\nslice. That is a change to the SHAPE of the work, which is what\nSection 5a is for -- hence a 5a edit rather than a ledger ruling about\nexecution.\n\n---\n\n## 2. A citation has three parts, not two: value, source, and KIND\n\n**Proposed for `provenance-discipline`. Promotion is Tony\'s judgment;\nrecorded here with the case that produced it.**\n\n### The case\n\nDeForest, Howard & McComas (2014), ApJ 787:124 states that the Alfven\nsurface lies at least 15 solar radii up in the streamer belt and 12\nover the polar coronal holes. On 2026-08-22 that figure was read at\nsource, corrected from a wrong 17/12.5 (Section 3), and landed on\n`ALFVEN_SURFACE_RADII` as a supporting leg.\n\n**It would score `confirmed` under every check this project owns.**\nThe value is right. The paper states it. The position is findable.\nThe identifier resolves. A clean row by every existing measure.\n\n**And drawing a shell at 15 R_sun would still have been wrong.** The\npaper says plainly that the streamer figure is set by the\ncoronagraph\'s FIELD OF VIEW and the polar one by the NOISE FLOOR. They\nare instrumental floors. The number is real; the boundary is not.\n\nNothing in the annotation grammar or the verdict vocabulary can\nexpress that difference. The visualization decision turned entirely on\nit, and no worksheet return could have surfaced it.\n\n### The rule\n\nThe annotations already carry VALUE and SOURCE. **KIND is what tells\nyou what you are allowed to DRAW.**\n\nFour kinds, the same set now used in the dispatch fields:\n- `MEASURED` -- directly observed, reported as the quantity claimed\n- `INFERRED` -- derived from a light curve, an orbit, or a model\n- `STATED` -- asserted in a source without derivation shown\n- `NOT FOUND` -- no source states it; remove and note the gap\n\n### Two live instances the same day\n\n`HELMET_CUSP_RADII = 4.0` is cited to Suess & Nerney (2004), which\nSTATES 2-4 R_sun as established background -- the paper\'s own result\nis an analytic stagnation-flow model. Correctly cited, and `STATED`\nrather than `MEASURED`. That is why the rendered pinch is drawn SOFT\nrather than sharp: a modelled boundary does not earn a knife edge.\n\nThe same paper\'s fast/slow wind identification is marked in its own\nabstract as a reasonable ASSUMPTION. So the streamer band draws the\nbrightness boundary -- a coronagraph observation, uncontested -- and\nattributes what it DIVIDES to Suess & Nerney as an interpretation.\nSlow-wind origin is unsettled in the field. Drawing a claim asserts it\nharder than writing it does.\n\n### Why not promoted today\n\nOne rule, two instances, one session. Promotion is Tony\'s judgment and\none occurrence is an anecdote. Recorded here so the next instance has\nsomething to be the second of.\n\n---\n\n## 3. Three dispatch fields, each answering a specific failure\n\n**Designed 2026-08-22 for L-225 and then withdrawn with its wrapper\n(Section 4). The fields survive; only the carrier changed.**\n\nThe existing dispatch already requires a resolvable identifier and a\nlocatable position. "Chapter 1" is not a position -- Golub & Pasachoff\nwas removed on 2026-08-20 for exactly that, the one return in nine\nwith no findable location. These three are ADDITIONS, and each traces\nto a failure on 2026-08-22.\n\n**`VERSION` -- which text was read.** The arXiv ABSTRACT METADATA at\narxiv.org/abs/1404.3235 says 12.5 and 17 solar radii. The accepted\nmanuscript served as the PDF under the SAME identifier says 12 and 15,\nthree times: abstract, Section 5, Section 6. NASA ADS and Cranmer et\nal. 2016 both carry 12 and 15. This project repeated 17 across four\ndocuments, including into live code, because two separate reads both\nquoted the listing page. **A resolvable identifier is necessary and\nnot sufficient.** Agreement between two reads of one wrong page is not\nverification.\n\n**`METHOD` -- searched or recalled.** Some models search; some answer\nfrom training and format the result identically. Gemini has scholar\nsearch. The field is cheap and it separates two things that look the\nsame on the page.\n\n**`LOW_CONFIDENCE` -- what the model would not bet on.** On 2026-08-22\na model asked for citations returned a list mixing one real item (a\nNASA blog, carrying NO formal citation format) with a fabricated paper\nattributed to a named author at a named institution, in flawless\nacademic format, carrying invented precision -- "4-6 hours" where the\nreal source says "several hours". **Formatting ran INVERSE to truth.**\nA model asked to name its own soft spots sometimes does, and the cost\nof asking is one line.\n\n### The other half of the same lesson\n\nFree-form chat with an external model is for LEAD GENERATION, and its\noutput is a SEARCH PLAN, never citable. On 2026-08-22 the same\nfree-form exchange that produced the fabrication also named Raymond,\nGibson and Jones -- and two of three pointed at genuinely useful work\ndespite wrong titles. Both halves are true and neither cancels the\nother.\n\nRecorded for completeness: a model asked to AUDIT the fabrication\nproduced a new one in the same reply, inventing the lineage "Koutchmy\n& Livshits (via Suess & Nerney)". Those are independent lines to the\nsame morphology. Merging them destroys the redundancy that gives the\nclaim its weight -- the prose form of the failure the twenty\ncitation-inheritance tests guard against in code.\n\n---\n\n## 4. L-225 -- deferred, with its shape settled\n\n**Reaffirmed 2026-08-22. This is the approach, not a workaround.**\n\nThe MAPS disintegration radius, 8.33 R_sun, is typed into\n`comet_visualization_shells.py` and carries a model fact-check as its\nonly leg. The figure is PLAUSIBLE -- from 8.33 R_sun to a 1.23 R_sun\nperihelion is roughly four hours at these speeds, matching the\nNASA/LASCO statement that the nucleus was destroyed several hours\nbefore closest approach -- but plausible is not sourced.\n\n**The dispatch loop cannot reach it.** `comet_visualization_shells.py`\nappears ten times in `PROVENANCE_AUDIT.md` and ZERO times in\n`WORKSHEET_CHECK.md`. The scanner sees its claims; the worksheet\ncorpus does not include it. No row, no key, no row hash, nothing the\nchecker could route a return into.\n\nTwo ways to fix that were considered. Extending the worksheet corpus\nto reach the comet module treats the symptom. **Tony\'s ruling: migrate\nthe values into `constants_new.py`, where the builder ALREADY reaches.**\n`MAPS_DISINTEGRATION_RADII` and its siblings become constants; then\n`worksheet_request_builder.build()` slices them as rows with hashes,\nthe ratchet applies, and the verdict writes back as an annotation the\nscanner accepts.\n\n**Fix the producer, not the corpus.** The shadow constant is the\ndefect; the unreachable row is a consequence. This is the same\nmigration L-181 and L-191 already track, so it is the next instance of\nscheduled work rather than new work.\n\n`patch_L225_1_dispatch_request.py` is WITHDRAWN -- a hand-written\nmarkdown prompt is the wrong carrier for a row that is about to become\na proper one. Its four questions survive intact: perihelion distance\nas the control, disintegration distance with an explicit warning not\nto answer it with the perihelion, hours before perihelion, and the\nkind of each.\n\n**The perihelion is the control question and must stay in.** We know\nit -- 0.005729 AU, 1.232 R_sun -- and it is exactly the quantity a\nfree-form answer collapsed the disintegration distance into on\n2026-08-22. A leg that misses it has told us what its other answers\nare worth.\n\nPart A goes out BLIND. The prompt must not contain 8.33. That is the\ntwo-dispatch rule and this is its case.\n\n---\n\n## 5. What this note does NOT do\n\nDeliberately, and each for the same reason -- better done fresh\nagainst a clean read than at the end of a long session:\n\n- **The Section 5a revision.** 5a starts at line 796 of a 118 KB\n  document. It is the sequencing authority for the whole project and\n  the edit must reconcile the braid against every ruling 5a already\n  carries. Section 1 above is the argument that edit needs.\n- **The `provenance-discipline` bump** for the KIND rule (Section 2).\n  One rule, two instances, one session.\n- **The builder change** for L-225 (Section 4).\n- **The handoff.** This note is not a handoff and does not replace one.\n\n---\n\n## References\n\nL-224 (the streamer band, whose build surfaced all of this); L-210\n(the withdrawn 4-6 R_sun range); L-209 (the Alfven surface and the\nDeForest rehoming); L-221 (the master plan as sequencing authority --\nthis note is the first revision made under it); L-225 (deferred, above);\nL-181 and L-191 (the shadow-constant migrations this joins);\n`documentation/SOURCE_suess_nerney_2004_helmet_extent_20260821.md`;\n`MASTER_PLAN_INTERACTIVE_GALLERY.md` Section 5a;\n`documentation/MASTER_PLAN_CRITICAL_PATH_SUMMARY.md`;\n`PROJECT_INSTRUCTIONS.md` Part 3 -- "The Artifact Bounds the Audit",\n"Verify Execution, Not Appearance", "A Check That Cannot Fail Is Not\nPassing", "Fetched vs Recalled".\n'


def main():
    if not os.path.exists("LEDGER_CONSOLIDATED.md"):
        print("ERROR: run this from the repo root.")
        sys.exit(1)
    if os.path.exists(OUT):
        print("ERROR: %s already exists. Refusing to overwrite. "
              "Nothing was written." % OUT)
        sys.exit(1)
    bad = [c for c in DOC if ord(c) > 127]
    if bad:
        print("ERROR: note holds %d non-ASCII char(s)." % len(bad))
        sys.exit(1)

    data = DOC.encode("ascii")
    with open(OUT, "wb") as f:
        f.write(data)
    print("wrote %s (%d bytes)" % (OUT, len(data)))

    with open(OUT, "rb") as f:
        rb = f.read()
    # Prose checks run against whitespace-collapsed text: the note is
    # hard-wrapped at 72 columns, so a needle spanning a line break
    # would fail on formatting rather than on content. Caught in
    # pre-test -- the first version of these two checks did exactly that.
    flat = b" ".join(rb.split())

    checks = [
        ("byte-identical to what was intended", rb == data),
        ("LF only, ASCII throughout",
         rb.count(b"\r\n") == 0 and all(b < 128 for b in rb)),
        ("anchor line present", b"Built on `96707590" in rb),
        ("braid ruling carries its NUMBER, not just its conclusion",
         b"Of 107 verification claims, 8 are clean" in flat),
        ("step-three-first argument recorded",
         b"BUILDING the rendering layer, and LOCKING Artifact 2" in flat),
        ("the five steps are stated as UNCHANGED",
         b"DO NOT MOVE" in flat),
        ("citation KIND rule present with its case",
         b"KIND is what tells you what you are allowed to DRAW" in flat
         and b"FIELD OF VIEW" in flat),
        ("all four kinds enumerated",
         all(k in rb for k in (b"`MEASURED`", b"`INFERRED`",
                               b"`STATED`", b"`NOT FOUND`"))),
        ("VERSION field carries the 17-vs-15 case",
         b"12.5 and 17 solar radii" in flat and b"12 and 15" in flat),
        ("LOW_CONFIDENCE field carries the formatting-inverse-to-truth case",
         b"INVERSE to truth" in flat),
        ("L-225 approach is migrate-to-constants, not extend-corpus",
         b"Fix the producer, not the corpus." in flat),
        ("the withdrawn patch is named as withdrawn",
         b"patch_L225_1_dispatch_request.py` is WITHDRAWN" in flat),
        ("the perihelion control question is preserved",
         b"0.005729 AU" in rb),
        ("Part A blindness recorded",
         b"must not contain 8.33" in flat),
        ("what it does NOT do is stated",
         b"## 5. What this note does NOT do" in rb),
    ]

    print("")
    fails = 0
    for desc, ok in checks:
        if not ok:
            fails += 1
        print("  %s  %s" % ("PASS" if ok else "FAIL", desc))

    if fails:
        print("")
        print("ERROR: %d check(s) failed. Delete %s and report."
              % (fails, OUT))
        sys.exit(1)

    print("")
    print("NEXT: commit, push, and archive this script to documentation/.")
    print("The 5a revision, the provenance-discipline bump and the L-225")
    print("builder change are all deliberately left for a fresh session.")


if __name__ == "__main__":
    main()
