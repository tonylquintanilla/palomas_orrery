# README Rewrite -- Change Note

**Built on:** orrery HEAD `2991a0c7220a4d6d30095e474c684538460c5f68`
(SHA round trip confirmed at session start; matches the task's stated base
exactly). Verification was against a full shallow clone at that SHA, not
just the attached files. New README: 535 lines (was 1,063), ASCII-only,
LF-only, all internal links checked against pinned HEAD.

## CRITICAL FLAGS -- push-order dependencies found this session

1. **MODULE_INDEX.md is NOT at repo root at HEAD `2991a0c7`.** The task
   brief says it moved to root (L-127) and to leave the link root-relative.
   I verified directly: at this HEAD the only MODULE_INDEX.md is the OLD
   hand-written one in `documentation/` (March 2026, "88 files"), and
   `module_atlas.py` at HEAD contains no MODULE_INDEX generation code. The
   L-127 regeneration was evidently not pushed. I followed the brief -- the
   new README links `MODULE_INDEX.md` root-relative -- **but that link 404s
   until the L-127 work is pushed.** Push order matters: L-127 first (or
   together with) this README.
2. **HEAD's MODULE_ATLAS.md is the July 4 generation** (117 modules, 934
   functions, 90,338 lines), not the July 17 one the task cites (121 / 955 /
   91,984). I independently verified against the clone: 121 root .py files
   exact, 91,851 non-blank lines by a plain count (the small delta from
   91,984 is presumably the atlas's own counting convention). So the task's
   figures are corroborated as current reality -- but the *committed* atlas
   disagrees until the regeneration is pushed. The README handles this with
   pointer-first phrasing ("121 modules and roughly 92,000 non-blank lines
   as of July 2026... MODULE_ATLAS.md carries the authoritative current
   counts") so it stays truthful on either side of the push.

## By the five purposes

**1. General information.** New "About This Project" section carries the
corrected framing verbatim in spirit: one person's tool, built for Tony's
own exploration, that he'd like to be useful to others -- with the gallery
as the path that actually works for that, and the repo's reader (future
Tony, AI collaborator, rare contributor) explicitly named as functionally
in Tony's own position. Gallery link promoted to the second line of the
document. The capability list survives but compressed from 29 bullets into
four themed groups (solar system / stellar-galactic / earth system /
publishing) with near-duplicates merged.

**2. Organizational structure for the developer.** New "Repository
Organization" section: an accurate top-level layout diagram (built from the
clone, replacing the old diagram's fictional `README/` folder), a
key-documents table (MODULE_INDEX, MODULE_ATLAS, LEDGER_CONSOLIDATED,
ADDING_OBJECTS_GUIDE, ORBITAL_MECHANICS_README, PROVENANCE_AUDIT,
DATA_INVENTORY, plus the four documentation/ readmes), a line each for
`documentation/` and `skills/`, and the two-sibling-repos explanation
(kept from the old README -- it was good -- including the
cross-repo-import reason the sibling layout matters). LEDGER_CONSOLIDATED
and ADDING_OBJECTS_GUIDE and ORBITAL_MECHANICS_README were not linked in
the old README at all; they seemed squarely purpose-2 material.

**3. Cloning and data orientation.** "Getting Started" now leads with git
clone, and step 2 is headlined "Get the data files -- they are NOT in the
repo": what's gitignored (stellar catalogs ~300 MB, orbit cache ~94 MB),
the two seeding paths (release ZIP's data/ + star_data/, or grow-through-
use), and a pointer to DATA_INVENTORY.md. The 200-line beginner walkthrough
(install Git, install Python, PATH troubleshooting) is gone; platform notes
survive as a few lines (Ubuntu PEP 668 flag + Tk packages, Fedora/Arch
one-liners, macOS python3). The "Data Files and Caches" section is
condensed from ~130 lines of nested tree listing to a six-row scale table
sourced from DATA_INVENTORY.md, keeping the cache-safety paragraph
(backups, atomic saves, size-reduction guard).

**4. Gallery as it publicly exists.** The Web Gallery section is the old
one lightly trimmed -- same pipeline description, same feature list, same
pipeline diagram, link fixed to documentation/. **Nothing added** about
Pyodide, the assembler, feature configs, trust/served_window, or any Phase
2 work. The changelog line's only nod is the deliberately generic
"continued gallery pipeline development."

**5. Data sources and citation discipline.** New "Data Sources and
Provenance" section: the source list, plus a paragraph characterizing the
practice from PROVENANCE_AUDIT.md's actual framework -- scanner,
vulnerability x criticality classification, the no-push-with-Tier-1 gate,
and the remove-and-note-the-gap rule for unsourceable values. Brief and
honest, not a summary of the audit.

## The concrete findings

- **Broken links:** all five confirmed 404 at root / 200 in
  documentation/ at pinned HEAD. Four are now linked into
  `documentation/`; MODULE_INDEX.md left root-relative per the brief (see
  CRITICAL FLAG 1). Full-document link audit run on both old and new
  README; no other broken relative links existed or exist.
- **Module/LOC count:** corrected with pointer-first phrasing (see
  CRITICAL FLAG 2). The Development Complexity prose keeps its
  team-size-ratio framing (it reads fine against the corrected scale) with
  the stale "75+ / 78,000" replaced and "1,350+ trajectories across 15
  center objects" softened to "1,000+ across multiple center bodies" --
  I could not verify the 1,350/15 figures from any attached or fetched
  source, so per the verify-or-flag rule I retreated to the old README's
  own more conservative claim (its Data Files section said "1000+
  objects") rather than carry an uncheckable number forward.
- **Standalone executables:** the platform download table, the
  extract-and-double-click walkthroughs, and the Google Sites/iCloud macOS
  link are cut. One sentence remains: executables exist on Releases but
  are not the actively maintained path.
- **Staying Up to Date:** the three-platform double-click table is cut;
  `git pull` (with the one-time init block for ZIP downloaders) is now THE
  update path. One line notes the scripts exist, naming the file as it
  actually exists in the repo: `_UPDATE_CODE.bat` (leading underscore --
  verified in the clone; the old README's `UPDATE_CODE.bat` was wrong).
- **Requirements visibility:** new "Python Compatibility and Dependencies"
  section surfaces the kaleido==0.2.1 pin and its reason, the Plotly 5.x
  hold, the full Python 3.14 status, the customtkinter dormancy risk, the
  fact that the gallery pipeline never touches kaleido, and the documented
  6.x/1.0 upgrade path -- with requirements.txt linked for the full
  annotations. The old `pip list` sample output is gone.
- **Stamp and changelog:** Last Updated is July 2026, describing what
  actually shipped at a general level (doc reorg, generated index/atlas
  tooling, provenance refresh, this rewrite, generic gallery clause) while
  keeping the v2.9.0 milestone line intact as "prior milestone" -- I did
  not invent a new version number.
- **License:** legal text untouched, verbatim.

## Other changes made (judgment calls within the brief)

- "Quick Start" and "Installation" and "Staying Up to Date" merged into
  one "Getting Started" section -- three overlapping install paths
  collapsed into one canonical developer path.
- "Usage" (~120 lines of numbered walkthroughs) condensed into "Using the
  Desktop App" (~25 lines): the interaction model, center-body options,
  and the other GUI entry points as commands. The step-by-step voice
  ("You'll see lots of text scrolling by - that's normal!") is the
  beginner framing the brief retargets.
- Module Reference tables (nine tables, ~90 modules) dropped in favor of
  the MODULE_INDEX/MODULE_ATLAS pointers -- hand-maintained module tables
  in the README are exactly the stale-count failure mode the generated
  files now solve. The Galactic Center module table survives inside its
  own section since that section doubles as run instructions.
- Earth System and Social Media sections kept but tightened; Galactic
  Center kept nearly whole (it is compact and accurate).
- Release ZIP references made generic ("the latest release ZIP") -- the old
  README named three different ZIP filenames/sizes (`palomas_orrery.zip`
  ~469 MB, `palomas_orrery_2_1_zip.zip` ~222 MB,
  `Palomas_Orrery_v2.2.0_Windows.zip`) that I could not verify against the
  live Releases page from this environment.
- "Created by..." AI-assistant credit kept, moved into About; new credit
  line at the bottom per convention: "README updated: July 2026 with
  Anthropic's Claude Fable 5."

## Open questions for Tony

1. **Push order (the two CRITICAL flags):** land L-127 (regenerated
   MODULE_INDEX.md + MODULE_ATLAS.md at root, updated module_atlas.py)
   before or with this README, or the MODULE_INDEX link 404s and the atlas
   counts read slightly low. Also: what becomes of the old
   documentation/MODULE_INDEX.md (the brief says "about to be renamed to
   an archival file" -- not yet done at HEAD).
2. **Beginner content disposition:** I cut the Step-by-Step Installation
   Guide entirely rather than moving it. If any of it should survive,
   `documentation/INSTALL_BEGINNERS.md` is the natural home -- but per the
   brief I flagged rather than created it. Same question for the detailed
   Linux/macOS troubleshooting subsections.
3. **Should any of the four documentation/ readmes move to root?** Per the
   brief, flagged, not decided -- links currently point into
   documentation/, which works either way until a move happens (at which
   point the links need a one-line follow-up).
4. **README_DEPLOYMENT_v2.md, RUNNING_A_PATCH_FILE.md,
   project_instructions_v3_31.md** sit at root but are not linked from the
   new README -- deployment/process docs that felt more internal than the
   key-documents table warranted. Say the word if any should be listed.
5. **docs/ folder:** described in the layout as "generated architecture
   pages" based on its contents (index.md, module trees, per-subsystem
   pages). If it serves a different purpose (e.g., an intended GitHub
   Pages docs site), the one-liner should say so.
6. **"Cross-platform compatibility achieved January 2026"** is kept in two
   places (Getting Started intro, Acknowledgments) on the strength of the
   old README asserting it -- I could not independently verify the date,
   but it is the kind of project-history claim the old README is
   authoritative for. Flagging for completeness.
7. **Contributing section:** the old text said "Cross-platform testing
   (Windows, macOS & Linux all supported!)" -- kept in condensed form. If
   the contributing posture should shift with the developer reframing
   (e.g., pointing contributors at the ledger), that is a separate small
   edit.

-- Claude Fable 5, July 17, 2026, Mode 7 relay deliverable for Tony's review.
