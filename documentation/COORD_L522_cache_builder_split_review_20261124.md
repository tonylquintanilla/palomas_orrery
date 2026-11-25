<!-- Doc-Kind: hand | The coordinating session's review of the cache builder's skill split (L-522, document caps) before Tony commits: what it checked itself, one fault in the names check to fix, and one finding re-homed to L-553. -->
# Review before the commit: the cache builder's skill split (L-522)

Built on orrery 5f9d92f12df47b07dd65c4dbe4d9f58e05d47025 at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 727ebf791666a515b9cf18d869ca3507daf11606 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io. Tony's
orrery folder stands at eb90dff7 and his gallery folder at 727ebf79,
each with the split's edits waiting, not pushed.
Written November 24, 2026 by the coordinating session (Claude Fable
5.2) for the Claude Code session that wrote
`documentation/REPORT_L522_cache_builder_split_close_20261124.md`.

Tony's local folders: orrery
C:\Users\tonyq\OneDrive\Desktop\python_work\palomas_orrery_for_github\
gallery
C:\Users\tonyq\OneDrive\Desktop\python_work\tonyquintanilla.github.io\

## 1. What was checked here, from Tony's folders

- THE ACCOUNT, by this session's own script against eb90dff7: 844
  non-blank lines of the old skill, each found in exactly one of the
  new skill, the page, or the lines added to the history; none in two;
  20 in none. Those are your 18 and the two `raw/runs` lines you
  corrected on the page after your account ran. Agreed.
- L-538's section in the skill: word for word the brief's, with the
  go-ahead's finer-step rule. All 185 new lines of the skill read.
- `DOCUMENT_CAPS.md` (one line, 944 to 728), the history file (the
  1.19 entry and its "Moved down" line), the gallery's `CLAUDE.md`,
  the ledger's diff, Where We Are's diff, the names check's diff, the
  closing report whole, and the page's L-538 section whole.
- Curve error on a clean checkout of 727ebf79: FAIL, juno and
  bepicolombo "served no fine points (no capture block)". So it is red
  on what is pushed, with or without the split, as you say.
Not checked here: the two maintenance runs, the suite's 604, and the
page's L-538 section against the builder's code.

## 2. One fault, in the names check: fix before the commit

ON A CLEAN CHECKOUT of 727ebf79, with your three files copied in, no
orrery folder beside it and nothing a build leaves:

    CACHE_BUILDER_AS_BUILT.md:
      examined 144 names: 140 found in the gallery's code, 0 only in
      the orrery's, 0 marked, 1 not found, 3 not examined tonight
      NOT FOUND: data/solar-system.prev/raw/runs/: not found in the
      code (file)
    AS-BUILT NAMES: FAIL -- 1 finding(s)

With an empty `data/solar-system.prev/raw/runs/` made in that checkout,
the same run reads "141 found ... 0 not found" and "ok".

So the row's verdict rests on a folder a build leaves behind. It is
green in Tony's folder, which has one. Tonight's night would pass too,
since the check runs after the build's swap in the same workspace. A
clean clone is red. This is the fault of 2026-11-21 again
(`patch_L529_4_as_built_names_night.py`), from the other side.

THE OUTCOME WANTED, the means yours:
- The row gives the same verdict in three places: a clean checkout,
  Tony's folder, and a workspace a build has just run in.
- A path under one of the builder's leftover folders
  (`data/solar-system.prev`, `data/.staging_*`,
  `data/solar-system.quarantine_*`) is never looked for on disk. If it
  can be held to the code another way that is plain (the folder's name
  as the code makes it, and the path beneath it), do that. If not, set
  it aside by its own kind, counted and printed by name like the
  others, and say in the report that the kind is a blind spot.
- Shown: green on a throwaway copy that has no `.prev`; and what the
  row does with a made-up leftover path the code does not make.
- Never delete, rename or empty Tony's own `data/solar-system.prev`
  to test this. Use a copy.
- The module's own words say GitHub "never has" those folders. After
  the night's build its workspace has `.prev`. Correct the sentence.

Then: the row itself in Tony's folder and on the clean copy, read from
its own output. Not the whole maintenance run again.

## 3. One finding re-homed: L-538's to L-553

Your finding on what the build does when the floor still fails is the
class L-553 (a held body turns the night red) already names. Write
this note onto L-553, word for word, and run `ledger_index.py`:

    **Note:** (2026-11-24, evening, the coordinating session, Claude
    Fable 5.2) A SECOND CASE OF THE CLASS, re-homed from L-538's note
    of today. A capture craft served last-good, because JPL did not
    answer its questions or its step failed at the floor, has no check
    points written that night. The night's Curve error row is then red
    by name and the night commits nothing: one craft held, and no body
    on the site refreshed. The standard it misses is Tony's of
    2026-11-11: "Hold the bad data and report, then continue." On a
    craft's first night there is no saved layer, and the pre-swap
    check #O aborts the build instead, which is right until a first
    layer exists. Read from the gallery's `CACHE_BUILDER_AS_BUILT.md`
    as the Claude Code session wrote it from the code at 727ebf79; not
    checked against the code by the coordinating session. Not changed.
    This item's build covers both rows.

On L-538, the finding's last words, "for the coordinating session",
become "re-homed to L-553 (a held body turns the night red)".

## 4. The records

- L-522's note of the build: "but 18" becomes 20, the two more named
  as the page's `raw/runs` corrections, made after the account ran;
  and one line for section 2's fix, with what the row printed in each
  of the three places.
- The closing report gets a section 7, "After the coordinating
  session's review", with the same. It is not pushed yet, so it is
  added to, not replaced.
- Where We Are: no edit, unless a line on it is made false by this.
- Tony's run order stays as you gave it: the website, Commit then
  Push origin; the orrery, Commit, Pull origin, Push origin; reinstall
  gallery-cache-builder 1.22. Read both HEADs again before you write
  it.

Written November 2026 with Anthropic's Claude Fable 5.2.
