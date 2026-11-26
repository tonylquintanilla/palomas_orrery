<!-- Doc-Kind: hand | The review L-559 asked for: the protocol read whole against Tony's six-part test, the three-part description checked against both repositories' code and widened to the Earth System and the stars, the section list, the slips of recent handoffs sorted by failure mode, and the rulings the draft of v4.1 waits on. Communication; nothing in PROJECT_INSTRUCTIONS.md is changed. -->
# Review: the protocol as the project's instructions (L-559), November 25, 2026, night

Built on orrery 9daf6a3dd932c0bf456798a984aa814c84edb215
at https://github.com/tonylquintanilla/palomas_orrery (branch main)
and website 972b4a9366224160d03f84708c9d33f55b811b87
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
(branch main), both read 2026-11-25, between 21:52 and 22:00 Chicago,
by git ls-remote and a fresh clone of each.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

Type: REVIEW, coordination and documentation (zero code). By the
coordinating session of Nov 25, 21:52 (Claude Fable 5.2, linked to
Tony's computer, with a shell of its own and none on his).
Companions, placed with this file:
`documentation/DRAFT_PROJECT_INSTRUCTIONS_v4_1_20261125.md` (the draft)
and `documentation/build_L559_protocol_v4_1_draft.py` (what built it).
The ledger wins on status; L-559 (the protocol as the project's
instructions) is the item.

## Tony's words that opened the session (21:52)

"the task is to update the protocol and bring it up to date consistent
with the current 3-way architecture: the python orrery with its three
components, the solar system orrery, the stars, and the earth science;
the website assembler; and the interactive website that renders the
images."

"the purpose of the protocol is to be a functional project description
to guide Claude."

"the reason that we are putting this task to the front now is to
continue to clarify and improve the functionality and efficiency of
this project so that all it's components work together and Claude can
be most helpful from session to session across chat, code and models."

## The opening checks

- Orrery HEAD 9daf6a3d is Tony's commit "master plan update", above
  87ece129: the six files of the last session are pushed.
- Website HEAD 972b4a93, unchanged since the last handoff.
- All 12 installed skills equal the repository's copies at 9daf6a3d,
  body byte for byte, header with line breaks ignored.
- Three files staged from Tony's folder equal GitHub's, byte for byte:
  PROJECT_INSTRUCTIONS.md, WHERE_WE_ARE.md, the night handoff.
- Not done here: the night's proof of BepiColombo's cut and Tony's
  phone look (the handoff's steps 3 and 4). They are still owed.

## The verdict, by Tony's six-part test

A cold session holding only the protocol, v4.0 and the draft:

| It can say | v4.0 | The draft |
|---|---|---|
| 1. what the project is for | no: stated nowhere | yes: The Project, first paragraph |
| 2. what its parts are and how they connect | no: two parts named in Part 4, the night left out, no Earth System, no stars | yes: The Project |
| 3. who Tony is and what is his to decide | yes: Roles; Method Belongs to the Skill | unchanged |
| 4. how a session starts, what it checks, how it ends | yes; the skills comparison is named only in Part 3 | yes; Session Start now names both gates |
| 5. where the order of the work lives | half: "Do next" is named, the rule that nothing else sequences is only in a skill | yes: one line in Session Start |
| 6. what must never be done | yes, but spread over the gates | unchanged; see "Looked at and left" |

The cold read itself has not been run. The key for it is at the end
of this file, written before any read.

## The three-part description, checked against the code

READ for this: both `nightly.yml`; `daily_run.py`'s own account of the
night; the docstrings of `tools/gallery_cache_builder.py`,
`tools/encounter_fetch.py`, `tools/pull_drawings.py`,
`tools/mirror_objects.py`, `gallery/assembler/assemble.py`,
`render_orbits.py`, `render_spacecraft.py`, `cache_reader.py`; the
builder's function names for trust and holds; both nights' run
records; the served index's keys; the orrery's `export_objects.py`,
`enso_page_generator.py`, `star_visualization_gui.py`,
`earth_system_generator.py` docstrings, the dashboard's launch table,
and every root module's Domain tag.
NOT READ: the bodies of the builder (5,185 lines) and of
`interactive.html` (10,551 lines) beyond searches; the star pipeline's
code; the Earth System generators' code.

What L-559's description had right: the three parts, their one
direction, the two nights an hour apart, the page asking JPL nothing.

Four sentences corrected:
1. "It exports ... `data/path_plans.json`" as a file the website
   pulls. The website pulls three things: the constants export, the
   objects export and the stored drawings. A path plan rides inside
   the objects export (`export_objects.py` reads `path_plans.json`;
   `mirror_objects.py` copies each `path` onto its entry). No file in
   the website names `path_plans`.
2. "the positions themselves for each spacecraft path and each
   encounter" as the night's work. An encounter is fetched once, by
   hand, with `tools/encounter_fetch.py`; "The nightly builder never
   runs it, and the night never commits or swaps data/encounters/"
   (that tool's own words).
3. The protocol's "there is no local math to get wrong, because there
   is no local math" (The Orrery and the Assembler). The orrery has
   its own Kepler solvers (L-524 (the Kepler solver's start)). The
   draft says only that the orrery asks JPL live for each place it
   draws.
4. A path is also a comet's on an open path, not only a spacecraft's
   (`render_spacecraft.py`). The draft says "each on a path".

Widened, as L-559 asked:
- THE ORRERY'S THREE COMPONENTS, by the modules' own Domain tags at
  9daf6a3d (181 Python files at the root): orrery 61, dev_tools 60,
  stars 27, earth_science 21, utilities 8, untagged or other 4. Three
  windows, each launched from `palomas_orrery_dashboard.py`:
  `palomas_orrery.py`, `star_visualization_gui.py`,
  `earth_system_visualization_gui.py`.
- THE EARTH SYSTEM'S CHAIN: a layer's generator, run by Tony, writes
  the page, its pictures and the Google Earth file, and copies the
  page to the website folder; he pushes both. The orrery's night
  checks NOAA for El Nino, flags "EL NINO DUE", and never changes a
  page. Two pages are live: `earth/el_nino.html`,
  `earth/food_insecurity_sdn.html`.
- THE STARS: no live room. Eight saved pictures in the website's
  `gallery/` (five of the 3D neighbourhood, two HR diagrams, one
  exoplanet system), through Studio and the converter
  (gallery-pipeline). The road has stars and exoplanets at stage 17.
- THE OLDER CHAIN still serves all three subjects: a plot saved from
  the orrery, curated in Studio, converted, shown by `index.html`.

## The list, section by section

Line numbers are v4.0's, at 9daf6a3d. Marks: SERVES (left alone);
WORDS (the rule stands, legacy words changed); LEAVES (the text goes
to the history file, the rule is carried elsewhere); CHANGED (a rule's
content changes, Tony's ruling); NEW. The number in brackets is the
draft's edit.

| Lines | Section | Mark | What the draft does |
|---|---|---|---|
| 1-15 | Header and anchor | WORDS | says what the document is; "Gallery repo" becomes "the website repository"; the anchor's five-line apology is one clause [0, 1] |
| none | The project, its parts, its goal | NEW | THE PROJECT, 58 lines, before the Preamble [1] |
| 17-53 | Preamble | WORDS | the 2024 origin note in two lines; "As of v3.30" and "the modes" gone; six lines shorter [2, 3] |
| 58-74 | Session Start | SERVES + 1 | one line: the road is the one place the order lives; the skills comparison named beside the base [4, 4b] |
| 76-85 | Two Modes Are Still Named | WORDS | "the old Mode 2", "the old Mode 1" and the pointer to the seven-mode table go; Mode 5 takes Visual Verification's sentences [5, 5c] |
| 87-100 | Kinds of Session | NEW, 1 line | one writer in a folder at a time [6] |
| 102-106 | Session End | SERVES | |
| 108-116 | Mode 7: Outside Models | SERVES | |
| 118-138 | Context Priority | SERVES | |
| 143-151 | Core Principles | SERVES + 4 | four one-line principles arrive from sections that leave [7] |
| 153-187 | Register Rule | SERVES | |
| 189-213 | Procedural Criticality | SERVES | |
| 215-222 | Anti-Patterns | LEAVES | six rows; see "What leaves" [7b] |
| 226-227 | Multi-File Changes | LEAVES | now a Core Principle line [7c] |
| 229-231 | Graceful Fallback | CHANGED | the website's rule set beside the orrery's; the heading stays, horizons-orbital-mechanics points at it by name [8] |
| 233-240 | Iterative Design Planning | SERVES | |
| 247-264 | Skill Manifest | SERVES | the generated zone untouched |
| 266-297 | The Installed Skill Equals the Repository's Copy | SERVES | |
| 299-344 | Session-Start Base and the SHA Round Trip | WORDS | "Gallery:" becomes "Website:" [9] |
| 346-366 | Know Which Copy You Are Reading | CHANGED | the read-back bullet [10] |
| 368-372 | Verify Base Against Handoff | SERVES | |
| 374-390 | Verify Execution, Not Appearance | SERVES | |
| 392-430 | A Check That Cannot Fail Is Not Passing | SERVES | |
| 432-471 | A Report Names Its Items | WORDS | its example of an unnamed count, "5 parallel pipelines", goes into the past tense: the skill names all six now [11] |
| 473-478 | Check All Parallel Pipelines | WORDS | "gallery repository" becomes "website repository"; points at The Project [12] |
| 480-485 | Agentic Pre-Test | SERVES | |
| 487-491 | Visual Verification | LEAVES | its sentences are Mode 5's now [5b] |
| 493-507 | Fetched vs Recalled | SERVES | |
| none | Measure, Then Say | NEW | 7 lines, after Fetched vs Recalled [13] |
| 509-524 | Show the Envelope of the Unknowable | SERVES | |
| 526-544 | The Artifact Bounds the Audit | SERVES | |
| 546-579 | The Braid | SERVES | |
| 581-607 | Method Belongs to the Skill | SERVES | |
| 609-660 | Token Economy | SERVES | |
| 662-666 | Document Caps | SERVES | |
| 668-709 | Part 4: the conversation, the double helix, the undilated frame | SERVES | untouched, by Tony's word of Nov 10 and Nov 23 |
| 711-725 | The Orrery and the Assembler | LEAVES | The Project replaces it and keeps its two failure modes [14] |
| 729-744 | Lessons Archive | LEAVES | see "What leaves" [15] |
| 746-787 | Roles, Who Tony Is | WORDS | "A relay partner (Fable, GPT, ...)" becomes "An outside model (GPT, Gemini, a Claude session outside this Project)" [16] |
| 789-795 | Version History | WORDS | the version line [17] |

## What leaves, and where each line is already carried

Each goes to `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` word for
word at the build. 59 lines leave in all.

- The Orrery and the Assembler (16 lines): The Project carries the
  knowledge-not-code rule and both failure modes; gallery-assembler's
  section "The boundary this skill exists to protect" has the same
  words.
- Lessons Archive (17 lines). Its opening says "These process lessons
  exist nowhere else." Read against the skills at 9daf6a3d, nine of
  the ten do:
  - "Pure design sessions (zero code) are first-class outputs":
    ledger-and-session-records, The Document Stack.
  - "Module Atlas as prompt artifact" and "Fixing an invisible thing
    surfaces its neighbors" and "Central factories need explicit
    migration intent": orrery-coding-conventions (lines 377, 702, 697).
  - "Testing iterates in dependency order" and "smoke-test the
    deferred pipeline": agentic-pre-test (lines 120, 111).
  - "Handoff item numbers get rebased": ledger-and-session-records,
    Ledger Block Format.
  - "Skills are stores too": the protocol's own Skill Manifest and
    the ledger skill's change log.
  - "Bugs become lessons when documented. Stories make science
    memorable": Core Principles (Discovery Over Delivery; Scientific
    Storytelling), in sense, not in these words.
  - "Derive from known quantities, don't estimate manually": nowhere
    else. The draft makes it a Core Principle line.
- Anti-Patterns (9 lines, six rows): "Assume / Ask" is When Unsure,
  Ask; "Rewrite working code" is Targeted for Existing Code; "Build
  first architecture" is Iterative Design Planning; "Guard strips
  with if list:" is gallery-pipeline (line 64). The two with no other
  home become Core Principle lines: Fix Only What Was Asked; One
  Renderer.
- Visual Verification (6 lines): every sentence is in Mode 5's entry
  in the draft. orrery-coding-conventions keeps its own section,
  Visual Verification Details.
- Multi-File Changes (3 lines): a Core Principle line, same words.
- From the Preamble (6 lines) and Two Modes (2 lines): the wording
  named in the table.

## The recent slips, sorted by Tony's three failure modes

From the "Method, for the next coordinator" sections of seven
handoffs, Nov 16 to Nov 25 (six other handoffs of Nov 11 to 23 carry
no such section).

NO RULE EXISTED:
- A number or a behaviour told to Tony before it was measured or read.
  Six handoffs of Nov 23 to 25, one or more each: the reduced
  protocol's length, twice (Nov 23); "about 22 KB a craft", ruled on,
  1.36 MB measured (Nov 24); a step the page does not have, a
  mechanism named before the code was read, "no night had run", twice
  (Nov 24 evening); a timeout "not tried again", twice, a room that
  "always shows a day before the end", two bodies not in the results
  (Nov 25); "the cut would lift by itself" (Nov 25 evening); "about
  130 lines", 98 measured (Nov 25 night). The draft's Measure, Then
  Say [13].
- Two writers in one folder: named as method on Nov 16, broken once on
  Nov 25. The draft's line in Kinds of Session [6].
- What the website is and how the parts connect: nothing told the
  night session of Nov 25. The Project [1].
THE RULE EXISTED AND ITS WORDING LET THE FAILURE THROUGH:
- The read-back "by its size at least". On Nov 25 a re-sent file
  arrived as its first bytes at the same size; comparing content
  caught it. And "refused as hardlinked, passed a minute later" is
  written in five handoffs because it has no home. The draft's
  read-back bullet [10].
THE RULE EXISTED AND WAS NOT FOLLOWED:
- The road's line repeated without being held to Tony's order (Nov 25
  evening); a sentence recommended for the protocol before the
  protocol was read on the subject (Nov 25 night); a precedent of
  Tony's found after he had ruled again (Nov 25 evening). No new rule;
  Session Start's new line on the road is the nearest touch.
THE RULE EXISTED AND CAUGHT IT (the protocol working): the planted
fault and the names check on a clean checkout (Nov 24 evening); the
blind test found by the source's own points (Nov 24); the doubled
section found by reading the result (Nov 25 night); every read-back.
METHOD, FOR A SKILL AT ITS NEXT VERSION, not the protocol: a red night
and no night look the same in the commits; a night arrives when GitHub
sends it; a web fetch can return a stale copy of a page that moves
(gallery-cache-builder, at its next touch).

## The build's arithmetic

`build_L559_protocol_v4_1_draft.py`, run on PROJECT_INSTRUCTIONS.md at
9daf6a3d. Each edit matched exactly once.

    1  header, and THE PROJECT (new)                    15 -> 69  (+54)
    2  Preamble, the 2024 origin note shortened           5 ->  4  (-1)
    3  Preamble, the two layers said without v3.30       10 ->  5  (-5)
    4  Session Start, where the order lives               2 ->  3  (+1)
    4b Session Start, the skills comparison named         1 ->  1  (+0)
    5  Mode 5 takes Visual Verification's sentences       2 ->  5  (+3)
    5c The default, said without the old mode numbers     6 ->  4  (-2)
    5b Visual Verification, the section, leaves           6 ->  0  (-6)
    6  Kinds of Session, one writer in a folder (NEW)     2 ->  3  (+1)
    7  Core Principles gain four lines                    1 ->  5  (+4)
    7c Multi-File Changes, the section, leaves            6 ->  3  (-3)
    7b Anti-Patterns table leaves                         9 ->  0  (-9)
    8  Graceful Fallback, the website's rule added        3 ->  5  (+2)
    9  SHA Round Trip, "Gallery:" becomes "Website:"      1 ->  1  (+0)
    10 Know Which Copy, the read-back (CHANGED)           6 ->  6  (+0)
    11 A Report Names Its Items, "did not"                1 ->  1  (+0)
    12 Check All Parallel Pipelines, the website named    5 ->  5  (+0)
    13 Measure, Then Say (NEW)                            2 ->  9  (+7)
    14 The Orrery and the Assembler leaves               16 ->  0  (-16)
    15 Lessons Archive leaves                            17 ->  0  (-17)
    16 Roles, the outside reader named as it is today     2 ->  2  (+0)
    17 Version History                                    3 ->  3  (+0)
    base 795 lines; edits sum +13; draft 808 lines; arithmetic HOLDS
    the same build without edits 6 and 13: 800 lines

CHECKED on a throwaway copy of 9daf6a3d with the draft laid over
PROJECT_INSTRUCTIONS.md:
- `skills_index.py --check` exits 0: "OK: 12 skills parsed, no
  consistency problems."
- `doc_index.py --caps` on the draft: "DOCUMENT CAPS: RED -- over its
  cap: PROJECT_INSTRUCTIONS.md (808 lines, cap 800)", so the check
  can fail. On the build without edits 6 and 13: 800 of 800, "DOCUMENT
  CAPS: PASS".
- ASCII only, LF only. Of the 116 lines added, three are over 80
  characters: the Doc-Kind comment, and two of the one-line Core
  Principles, as that list's older lines are.
NOT CHECKED: the orrery's maintenance run (not run); the cold read.

## The rulings the draft waits on

1. THE NAMES OF THE THREE PARTS. The draft: the orrery; the website's
   night; the page. Tony's message tonight calls the middle part "the
   website assembler". In the code, "assembler" is the folder of
   Python that runs in the visitor's browser (`gallery/assembler/`),
   part of the page; the middle part's tool is the cache builder. The
   draft's THE WORDS says so. Which names stand is his.
2. THE PROJECT, as written: its 58 lines, at the top, before the
   Preamble, opening with what the project is for and then the road's
   goal (L-559's unanswered question of 20:40).
3. WHAT LEAVES: the five blocks above.
4. GRACEFUL FALLBACK's added sentences.
5. NEW RULE: Measure, Then Say [QUALITY], 7 lines.
6. NEW RULE: one writer in a folder at a time, 1 line.
7. CHANGED RULE: the read-back compares bytes where it can, sends from
   a new path, and waits a minute on "hardlinked". It amends his
   ruling of Nov 2 ("Read back is enough"), which was for size.
8. THE CAP. The draft is 808 lines; the cap is 800 and only Tony
   changes it. Without rulings 5 and 6 the same build is 800 exactly.
   The master plan's row (1,755 lines) leaves the caps page in the
   same build.
9. STRATEGY's PLACE. ledger-and-session-records names the master plan
   as STRATEGY, the first of his seven kinds of document (L-442 (the
   seven kinds of document)). With the plan archived, what holds that
   place is his to say. The session's proposal: The Project, in the
   protocol.

## What the build owes, after the rulings

- `PROJECT_INSTRUCTIONS.md` at v4.1, from the same script with the
  ruled edits; the lines that leave copied word for word into
  `documentation/PROJECT_INSTRUCTIONS_HISTORY.md` with one version
  entry; the archived copy `documentation/project_instructions_v4_0.md`
  already stands. Tony pastes v4.1 into the Project.
- gallery-assembler: lines 37 and 48 to 49 point at "master plan sec.
  3" and at "protocol Part 4 (The Orrery and the Assembler)". One
  bump, one reinstall.
- ledger-and-session-records: the STRATEGY entry of The Document
  Stack, by ruling 9; and its sentence "The protocol's version
  history lives in ..." stays true. One bump, one reinstall.
- The master plan's retirement line and its row on `DOCUMENT_CAPS.md`;
  the protocol's row if ruling 8 changes it.
- `README.md` tells the chain in the old words ("the assembler", "the
  interactive gallery", its lines 111 and 470 to 483); it restamps at
  a major build, by Tony's word of Nov 10. Named here, not touched.
- L-559's note, Where We Are (at 130 of 130 lines: something moves out
  first), and the handoff.

## Looked at and left

- A "never" list. The things never done are spread over the gates
  (never a complete file from an unconfirmed base; never a citation
  over recalled data; never a reinstall cleared on Tony's word; commit
  and push are Tony's). A one-screen index of them would cost about
  ten lines and repeat each gate. Not drafted.
- The Preamble's double helix and Part 4's: both kept, by Tony's word
  of Nov 23.
- Token Economy, A Report Names Its Items, The Braid: long, recent,
  his words in each. No line touched.
- The skills, beyond the pointers named above: out of scope, by
  L-559's bounds.

## The cold read's key, written before any read

A session holding only the draft should answer:
1. What is the project for? Three subjects, the Earth System, the
   solar system and the stars; a legacy gift for Paloma that must stay
   running and right without Tony; the website is to do what the
   desktop orrery does, with a date to choose.
2. What are its parts and how do they connect? The orrery defines; the
   website's night pulls the exports, asks JPL and serves; the page
   works out and draws and asks JPL nothing. One direction, by files.
   Only the Solar System is live; Earth System pages are built by
   Tony's run; the stars are saved pictures.
3. Who is Tony and what is his? A retired engineer, artist and
   anthropologist, not a programmer; every ruling, every look that
   matters, every commit and push, every cap, what the project should
   be. Method is the skills'.
4. How does a session start, what must it check, how does it end?
   Where We Are, the ledger where the job points, both bases, the
   skills comparison, which copy is read; it ends with the ledger
   item, Where We Are, the handoff with its anchor, his actions in
   one list.
5. Where does the order of the work live? The road on Where We Are,
   and nowhere else.
6. What must never be done? Build on an unconfirmed base; work from a
   skill copy that differs; return a whole file from a stale base;
   cite over recalled data or fake an unknowable value; trust a check
   that cannot fail; commit or push.
And two traps: does it think the page asks JPL (no), and does it think
"the assembler" is the nightly builder (no: the Python on the page).

## Size

No token count prints here. Read: the handoff, Where We Are, CLAUDE.md,
the caps page, L-559 whole, the protocol's 795 lines, the ledger
skill, the code named above by docstring and search, parts of five
skills, the method sections of seven handoffs. Written: the draft (808
lines, 13 net new), the build script (409 lines), this file.

Written November 2026 with Anthropic's Claude Fable 5.2.
