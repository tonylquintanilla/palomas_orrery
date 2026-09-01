<!-- Doc-Kind: zoned | The front door: what the project is, where its pieces are, and how the work is kept correct. -->
# Paloma's Orrery

**Tony Quintanilla, PE | Anthropic's Claude Opus 5 | August 31, 2026**

Rewritten under ledger handle L-270. Cut from `e382650b` at
https://github.com/tonylquintanilla/palomas_orrery (branch main). The
prior version is archived at
`documentation/README_archived_20260831.md`. The anchor names the state
this file was written against, not a promise the repository still sits
there.

**What this file is.** The project's front door, in two halves. Part 1
says what Paloma's Orrery is and where to find the pieces that describe
it. Part 2 describes how the work is kept correct -- the provenance
discipline, the protocol and skills layer, the maintenance runners, and
the commit discipline. That second half is written for whoever picks the
project up, including an AI collaborator starting a session cold, rather
than summarized for a casual reader.

---

An astronomical visualization suite that turns NASA, JPL and ESA data into
interactive 3D and 2D views of the solar system, the stellar neighborhood,
the Galactic Center, and Earth's climate system.

**See it without installing anything:**
[palomasorrery.com](https://palomasorrery.com/)

Paloma's Orrery is a personal tool, built first for its author's own
exploration and learning. Tony Quintanilla -- a retired civil and
environmental engineer, artist and anthropologist -- develops it through
conversational AI collaboration, and named it for his daughter. The project
began in September 2024 and has grown alongside the models that help build
it. The account of how it started, in Tony's own words, is
[PROJECT_ORIGIN.md](PROJECT_ORIGIN.md).

**Philosophy:** Data Preservation is Climate Action. Scientific accuracy
first, visual beauty always.

---

## Table of Contents

**Part 1 -- What it is and where to find it**

1. [What you can reach from where](#what-you-can-reach-from-where)
2. [See it](#see-it)
3. [What it covers](#what-it-covers)
4. [Where things are](#where-things-are)
5. [Running it yourself](#running-it-yourself)

**Part 2 -- How the work is kept correct**

6. [The problem this solves](#the-problem-this-solves)
7. [Two layers: the protocol and the skills](#two-layers-the-protocol-and-the-skills)
8. [Session start: the SHA round trip](#session-start-the-sha-round-trip)
9. [The ledger and the handoffs](#the-ledger-and-the-handoffs)
10. [Provenance: where the numbers come from](#provenance-where-the-numbers-come-from)
11. [From the orrery to the gallery](#from-the-orrery-to-the-gallery)
12. [Before the push: the maintenance runners](#before-the-push-the-maintenance-runners)
13. [The push](#the-push)

**Part 3 -- Administrative**

14. [Contributing](#contributing)
15. [License](#license)
16. [Contact](#contact)

---

# PART 1 -- WHAT IT IS AND WHERE TO FIND IT

## What you can reach from where

This project's pieces are not all available in the same place, and the
differences matter enough to state before anything else. Four contexts,
each one adding to the one above it.

| Where you are | What is reachable |
|---|---|
| **palomasorrery.com**, in a browser | Both galleries, and nothing else on this list. No install, no repository, no Python of your own -- the interactive gallery runs the project's own Python *in your browser* through Pyodide. This is how the project reaches everyone who is not its developer. |
| **github.com**, in a browser | Every tracked file in both repositories, readable without cloning and without Python: all the source, plus MODULE_INDEX.md, MODULE_ATLAS.md, PROVENANCE_AUDIT.md, LEDGER_CONSOLIDATED.md, PROJECT_INSTRUCTIONS.md and `skills/`. **Every relative link in this file resolves here**, and here is the only place they are guaranteed to. |
| **A local clone, with Python installed** | Everything above, plus the ability to *run* it: the desktop application, live JPL Horizons queries, `provenance_scanner.py`, and both maintenance runners. Also the local data caches -- which are gitignored, so they exist in neither row above. |
| **A Claude session in the Anthropic project** | Everything above, plus the two things that are only *operative* here: PROJECT_INSTRUCTIONS.md loaded as the resident protocol, and the skills installed to the developer's account. |

**The last row is the one that is easy to get wrong, so it is worth being
exact.** The protocol and the skills are ordinary files in this
repository. Anyone can read them on GitHub. What cannot be reached from
GitHub is their *installed* form -- the copy an AI session actually loads
when it starts. That copy lives in the account, not in the repo, and it
is invisible to everyone, including the running session that is using it.

This is why a skill lives in three stores rather than one: the repository
copy that anyone can read, the account install that a session actually
loads, and the generated manifest inside the protocol that says which
version is expected. It is also why reinstalling a skill mid-conversation
does not reach the conversation already in progress, and why a version
bump made during a session is carried forward in writing for the next
session to confirm rather than being marked done on the spot. Part 2
returns to this.

## See it

Nothing here needs to be installed. All of it runs in a browser.

| Where | What it is |
|---|---|
| [palomasorrery.com](https://palomasorrery.com/) | The web gallery. Curated visualizations exported from the desktop app and published as lightweight JSON, drawn with Plotly.js. Every visualization has its own direct link. |
| [The interactive gallery](https://palomasorrery.com/interactive.html?exhibit=sun) | The newer one, and the direction the project is heading. The orrery's own Python runs *in the visitor's browser* through Pyodide and builds the scene live. The Sun exhibit is the first one; more follow as the rendering ladder advances. |
| [Instagram: @palomas\_orrery](https://www.instagram.com/palomas_orrery/) | Stills and short video from the visualizations. |
| [YouTube](https://www.youtube.com/@tony_quintanilla/featured) | Video tutorials and walkthroughs. |
| [GitHub](https://github.com/tonylquintanilla/palomas_orrery) | This repository -- the desktop application and its documentation. |

The two galleries are not competing versions of the same thing. The
curated gallery is a published picture: fixed, fast, and exactly what its
author chose to show. The interactive gallery is a working instrument the
visitor drives. Both are wanted, and the curated one is not being retired.

## What it covers

The solar system, in the most detail: planetary and spacecraft positions
fetched live from JPL Horizons, comets with their dust and ion tails,
planetary interiors, rings, radiation belts and atmospheric shells,
Lagrange points, close approaches, spacecraft mission trajectories, and
exoplanet systems. Beyond it, the stellar neighborhood mapped from Gaia
and Hipparcos, and the Galactic Center's S-stars orbiting Sagittarius A\*
with their relativistic precession drawn against the Newtonian
prediction. Alongside those, an Earth system hub carrying long climate
records and forensic heat-wave analysis as 3D layers for Google Earth
Pro. Everything can be exported: as standalone HTML, as PNG, as a 9:16
portrait view for social video, or as KML and KMZ.

That paragraph is deliberately the whole of the feature list here. The
authoritative, current inventory is generated from the code itself and
lives in [MODULE_INDEX.md](MODULE_INDEX.md) -- go there rather than
trusting a hand-written summary that was true on the day it was typed.

## Where things are

### Two repositories, siblings on disk

The project spans two public repositories. They are kept as sibling
folders in the same parent directory, not nested one inside the other.

- **[`palomas_orrery`](https://github.com/tonylquintanilla/palomas_orrery)**
  (this one) -- the desktop application, its documentation, and the
  provenance and maintenance tooling.
- **[`tonyquintanilla.github.io`](https://github.com/tonylquintanilla/tonyquintanilla.github.io)**
  -- the web gallery: both gallery viewers, the published visualization
  data, the served solar-system cache, the nightly cache builder, and the
  gallery-side tooling.

GitHub Pages needs its own repository, which is why the split exists at
all. The sibling layout matters because `tools/gallery_studio.py` in the
gallery repo reaches back into this one: to attach Object Encyclopedia
entries to a figure it walks up the directory tree looking for a folder
containing `constants_new.py`, and imports `info_dictionary` from there.
If it does not find one it degrades quietly and attaches nothing, so a
gallery clone without its sibling still works -- it just loses the
encyclopedia.

### Key documents

The table below is GENERATED by `doc_index.py` from the documents
themselves -- each one carries a one-line `Doc-Kind` tag saying what it is
and what it is for. Do not edit the rows by hand; edit the tag in the
document, and the next maintenance run rewrites the table. The Kind
column matters: hand-editing a generated document is an error, because
the next run of its generator destroys the edit.

Documents in `documentation/` are not indexed here. Start with
[MODULE_INDEX.md](MODULE_INDEX.md) for the code and the deep-dive links
further down this file for the rest.

<!-- DOC-INDEX:START (generated by doc_index.py -- do not edit this zone by hand) -->
| Document | Kind | What it is for |
|---|---|---|
| [LEDGER_CONSOLIDATED.md](LEDGER_CONSOLIDATED.md) | hand + generated zone | The running ledger: every open and closed item under a stable handle, with the decisions behind it. Carries a generated INDEX. |
| [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) | hand + generated zone | The protocol. How a session is run, which checks are load-bearing, and why. Carries the generated skill manifest. |
| [README.md](README.md) | hand + generated zone | The front door: what the project is, where its pieces are, and how the work is kept correct. |
| [ADDING_OBJECTS_GUIDE.md](ADDING_OBJECTS_GUIDE.md) | hand-written | Step by step for adding a new celestial object. |
| [LICENSE.md](LICENSE.md) | hand-written | MIT license. |
| [PROJECT_ORIGIN.md](PROJECT_ORIGIN.md) | hand-written | How the project started, in Tony's own words. |
| [requirements.txt](requirements.txt) | hand-written | Annotated dependency spec, including the kaleido 0.2.1 pin and the Plotly 5.x constraint. |
| [RUNNING_A_PATCH_FILE.md](RUNNING_A_PATCH_FILE.md) | hand-written | How to run a delivered patch script, and what its guards mean. |
| [DATA_INVENTORY.md](DATA_INVENTORY.md) | **untagged** | _no Doc-Kind tag; add one to describe it here_ |
| [MODULE_ATLAS.md](MODULE_ATLAS.md) | **untagged** | _no Doc-Kind tag; add one to describe it here_ |
| [MODULE_INDEX.md](MODULE_INDEX.md) | **untagged** | _no Doc-Kind tag; add one to describe it here_ |
| [PROVENANCE_AUDIT.md](PROVENANCE_AUDIT.md) | **untagged** | _no Doc-Kind tag; add one to describe it here_ |
| [WORKSHEET_CHECK.md](WORKSHEET_CHECK.md) | **untagged** | _no Doc-Kind tag; add one to describe it here_ |
<!-- DOC-INDEX:END -->

The deep-dive documents, which live in `documentation/`:

| Document | What it is for |
|---|---|
| [documentation/ORBITAL_MECHANICS_README_v3_3.md](documentation/ORBITAL_MECHANICS_README_v3_3.md) | Orbital mechanics conventions: osculating versus mean elements, solution-level TP, reference frames, epochs. |
| [documentation/climate_readme.md](documentation/climate_readme.md) | The Earth system and climate data hub. |
| [documentation/wet_bulb_temperature_readme.md](documentation/wet_bulb_temperature_readme.md) | Forensic heat wave analysis. |
| [documentation/social_media_readme.md](documentation/social_media_readme.md) | The 9:16 portrait export. |

### Layout

```
palomas_orrery/                  # this repo
|- *.py                          # Python modules, all at root
|- README.md, LICENSE.md         # you are here
|- PROJECT_INSTRUCTIONS.md       # the protocol (Part 2)
|- PROJECT_ORIGIN.md             # how it started
|- MODULE_INDEX.md               # what every module does (generated)
|- MODULE_ATLAS.md               # full architecture atlas (generated)
|- LEDGER_CONSOLIDATED.md        # running work ledger and change log
|- PROVENANCE_AUDIT.md           # citation audit (generated)
|- DATA_INVENTORY.md             # local data store inventory (generated)
|- ADDING_OBJECTS_GUIDE.md       # how to add a new celestial object
|- WORKSHEET_CHECK.md            # cross-check annotation audit (generated)
|- requirements.txt              # annotated dependency spec
|- orrery_maintenance_run.py     # the pre-push suite (Part 2)
|- skills/                       # versioned AI-collaboration skill files
|- documentation/                # deep-dive docs, design manifests,
|                                #   handoffs, spent patch scripts,
|                                #   archived prior versions
|- docs/                         # generated architecture pages
|- data/, star_data/             # local data (large files gitignored)
|- reports/                      # generated analysis reports
```

## Running it yourself

Most people do not want to run the Python, and that is fine -- the
galleries above are how the project reaches everyone else. If you do want
to run it, the source is the actively maintained path. It works on Python
3.11 through 3.13, on Windows, macOS and Linux.

```bash
git clone https://github.com/tonylquintanilla/palomas_orrery.git
cd palomas_orrery
pip install -r requirements.txt
python palomas_orrery.py            # the main solar system GUI
python palomas_orrery_dashboard.py  # launcher for every tool
```

**The data files are not in the repository.** The stellar catalogs and
the orbit path cache are large and gitignored. Either download a release
ZIP from the
[Releases page](https://github.com/tonylquintanilla/palomas_orrery/releases)
and copy its `data/` and `star_data/` folders into your clone, or just
start using the app -- it fetches and caches on demand, so the first
plots are slower and the cache fills as you explore.

**Two dependency facts worth knowing before you upgrade anything.**
kaleido is pinned at exactly 0.2.1, and Plotly stays on 5.x to keep it
working; Python 3.14 is not yet supported. Both are annotated in full in
[requirements.txt](requirements.txt), including the upgrade path and the
issues to watch. Read it there rather than here -- it is maintained, and
this paragraph is not.

**On Linux**, install the system Tk packages first
(`sudo apt install python3-tk python3-pil.imagetk` on Ubuntu and Debian,
then add `--break-system-packages` to the pip command). Minor cosmetic GUI
issues appear on some window managers; the visualizations themselves are
rendered in the browser and are unaffected.

To update later, `git pull`. Your local `data/` and `star_data/` are
untouched, since they were never in the repo.

---

# PART 2 -- HOW THE WORK IS KEPT CORRECT

## The problem this solves

This codebase is written through conversation with AI models. That
arrangement has one structural weakness, and everything in Part 2 is a
response to it: **every session starts cold.**

A model recalls plausibly-wrong specifics with complete confidence. A
handoff document between sessions is a claim, and claims drift from the
code they describe. A number typed from memory looks exactly like a
number read from a paper. Left alone, a project built this way does not
hold steady -- it erodes, quietly, while every individual session looks
fine.

So the discipline below is not process for its own sake. Each rule exists
because a specific failure happened once, and most of them are about
declining a shortcut rather than doing extra work: not patching the
plausible date, not citing over a recalled value, not building on a stale
base, not trusting a handoff over the render.

The general principle, and the one worth carrying away if nothing else
is: **verify against something that cannot be talked into agreeing with
you.** The rendered plot, the source paper, the file on disk, the
commit hash. When a document and the code disagree, the code wins. When
the code and the render disagree, the render wins.

## Two layers: the protocol and the skills

**[PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) is the constitution.**
It is present in every session. It carries the working modes, the
judgment calls that belong to the developer rather than the model, and a
short list of checkpoint gates marked CRITICAL that must fire whether or
not anyone asks for them. That list is kept deliberately short: if
everything is critical, nothing is.

**The [`skills/`](skills/) folder is the on-demand layer.** Each skill is
a versioned document covering one kind of work -- editing existing files
safely, provenance and citation, the orrery's visual conventions, the
gallery pipelines, ledger and handoff format, JPL Horizons queries, the
Earth system pipeline. A skill loads when the work it covers comes up,
and stays out of the way otherwise.

Skills are treated as code, not as notes. Each is authored in this repo,
carries its own version number and the commit it was cut from, and is
installed to the developer's account so a session can load it. The
manifest listing every skill and its expected version is generated by
`skills_index.py` into the protocol itself.

**Both of these files are readable by anyone on GitHub and operative only
inside a Claude session** -- the distinction drawn in Part 1, and the
reason the next rule has to exist.

**The rule that makes the layer trustworthy is Stale Skill = Stop.** When
a session loads a skill, it compares that skill's own version line
against the manifest. If they disagree, work stops until the mismatch is
reconciled -- it is not noted in passing and worked around. The reason is
the three stores: the repository copy, the account install, and the
manifest. The copy a session actually loads is the account install, and
that is the one nobody can see -- not the developer mid-session, not the
session itself. A mismatch mentioned in passing while the work continues
is exactly the failure the gate exists to prevent.

The same invisibility has a second consequence, and it is a good example
of what this protocol does with a limit it cannot engineer away. A skill
bumped during a session cannot be verified *in* that session, because the
reinstall does not reach a conversation already running. So the bump is
not marked done. It is written into the handoff as an obligation the next
session discharges against a fresh load: the state stays honestly
unverified, which is what it is.

## Session start: the SHA round trip

Every session opens by fetching both repositories at HEAD and recording
the commit hash as the session's base.

This is the single most load-bearing check in the whole protocol, and it
is worth explaining why such a small thing carries so much.

A hash is derived from the bytes. So a remote HEAD that matches what the
last session's handoff said it pushed confirms, in one reading, that the
work was committed, that it was pushed, and that the content is byte-for-byte
what was described. There is nothing to audit and nothing to take on
trust. The one way it can fail is honest and loud: HEAD is not what the
handoff expects, which means something was not pushed, and that gets
reconciled before any work starts.

Everything downstream depends on it. Building on a stale base is how a
prior session's work gets silently overwritten, and a returned complete
file built on the wrong base is destructive in a way a bad snippet never
is.

Every document that leaves a session carries the same anchor -- a handoff,
a design manifest, a review request sent to another model. A document
without it cannot be checked against anything, because its reader has no
way to know what state it was describing.

## The ledger and the handoffs

[LEDGER_CONSOLIDATED.md](LEDGER_CONSOLIDATED.md) is the project's memory
across sessions. Every item of work, open or closed, has a stable handle
(`L-270`, `L-271`) and a detail block recording what was found, what was
decided, and who decided it. The index at the top is regenerated by
`ledger_index.py`; the detail blocks are the source of truth and
everything else is a mirror of them.

Handles matter more than they look. An item number that gets renumbered
between documents means different things in different places, and items
leak at the renumbering. One running ledger with stable handles beats
per-document numbering, and that was learned the hard way.

Each session ends with a handoff written into `documentation/`: what was
built, what was decided, what is waiting, and what the next session
should confirm before trusting anything. The handoff is explicitly
treated as a *claim*. It is verified against the code and the render at
the start of the next session, never taken as settled.

## Provenance: where the numbers come from

A visualization is an argument about the world, and every number in it is
part of that argument. If a ring radius is wrong, the picture is wrong,
and nothing about the picture will say so.

**The rule is fetched versus recalled.** A value that came from an
authoritative pipeline -- JPL Horizons, Gaia, NOAA -- is trusted. A value
that came from a model's training memory is not, no matter how confident
it looks or how right it sounds. Such a value must be sourced against a
real publication, or removed.

**There is a third outcome, and it is the one that takes discipline.**
If a claim cannot be sourced, it is removed and the gap is recorded --
not cited loosely, not kept because it seems plausible. A blank with a
flag on it is honest. An unsourced assertion with a citation over it is
worse than no citation at all, because the citation suppresses the
suspicion that would have caught it.

**Every value has one home.** [`constants_new.py`](constants_new.py) is
the single store for a numeric value, in prose as much as in code. Local
copies drift silently and bypass the citation chain, so they are deleted
and replaced with imports.

**Every value declares its own state.** Each constant carries a status
line saying what kind of claim it is: `measured` (a published value,
carrying a rung that says how well it is sourced), `declared` (a drawing
choice, or a pick from a range the source gives as a range), or `derived`
(computed from other constants, and never checked on its own). Measured
is the goal and declared is the fallback, promoted as soon as a real
measurement can be found. The kind matters as much as the value, because
it determines what a reader is entitled to conclude.

**The tooling.** `provenance_scanner.py` walks the tree and scores every
numeric claim -- constants, data dictionaries, and the display strings a
visitor actually reads -- by how vulnerable it is and how much damage a
wrong value would do. Its output is [PROVENANCE_AUDIT.md](PROVENANCE_AUDIT.md).
A separate loop builds verification worksheets, sends them to other AI
models in fresh sessions, and checks the returned verdicts against the
annotations in the code; `worksheet_checker.py` confirms that a
cross-check annotation actually names a worksheet that records the check
it claims.

**The push gate is Tier-1 = 0 on the active build path** -- the files
currently being built, not the whole tree. The global form is the
destination rather than the current rule, and it was narrowed on purpose:
a gate that blocks every push forever stops being read as a gate at all.
The scope moves with the work.

**The gate binds at export from the orrery**, not at publication. That is
not where the harm lands -- the harm lands on the public site -- but it is
the last place a check can run, because the scanner exists only in this
repository and nothing downstream of it scores anything. Which leads
directly to the next section.

**One finding worth stating plainly**, because it shapes how the
cross-checking works: agreement between two AI models about a number
confirms that they share a misreading, unless each read the source
independently. A confirmation request mostly cannot disagree. A blind
read can, and does.

## From the orrery to the gallery

The interactive gallery is the newest and most consequential piece of
architecture, and it is worth describing exactly, because the interesting
part is the constraint.

```
    constants_new.py  ->  objects_config.json  ->  nightly cache builder
                                                            |
                                                            v
                                                     served cache
                                                   (data/solar-system/)
                                                            |
    the browser  <-  feature_renderers.js  <-  the assembler (Pyodide)
```

**The assembler creates no data. It imports.** The desktop orrery asks
JPL Horizons a question and gets a live answer; there is no local math to
get wrong because there is no local math. The gallery has no live
connection, so it must cache a recipe once and reconstruct the scene
correctly, later, alone, in a stranger's browser. Almost everything that
distinguishes the two -- the caching, the client-side propagation, the
trust measurement -- exists because of that one difference.

The consequence is the fact that organizes the whole provenance effort:
**there is no point downstream of the orrery where a wrong number can be
caught.** Not in the builder, not in the assembler, not in the browser.
None of them knows what a correct ring radius is.

That splits the data in two.

**Positions look after themselves.** The nightly builder asks Horizons
directly for where each object is. A bad value cannot survive until
morning, and nothing needs auditing.

**Everything else does not.** Ring radii, radiation belt distances,
shell boundaries -- these start as numbers written into this repository's
Python and travel to the gallery by being copied. Horizons is never
consulted about them. A wrong number here is wrong on the public site,
permanently, and nothing will ever notice.

**The first arrow in that diagram is not built yet, and this is the
honest state of it.** `objects_config.json` lives in the gallery
repository and is maintained by hand. The cache builder has never read
`constants_new.py`. On one occasion a value was corrected here, pushed,
and the builder re-run, and the public site went on serving the old
number for hours until it was patched by hand in the other repository.
The automated transport is designed and tracked in the ledger; until it
exists, that copy is a manual step and is treated as one.

## Before the push: the maintenance runners

There are two runners, they are different programs, and the difference
between them is the point.

**`orrery_maintenance_run.py`**, in this repository, is one command run
after an editing session and before a push. It runs the generators
first -- the ledger index, the skill manifest, the module atlas, the data
inventory -- then the checkers, then prints one summary. Nothing stops on
a failure: every tool runs every time, so a single pass shows the whole
picture rather than the first problem in it.

The generators regenerate rather than merely reporting staleness, on the
grounds that a tool telling you a file is stale without fixing it has
only added a step. Output files are fingerprinted before and after, so
the summary says which ones actually moved.

Two of its checkers are report-only: they exit zero whatever they find,
and exit non-zero only when they could not run at all. Their verdicts are
quoted in the summary either way, so a bad report-only result cannot hide
behind a green run.

**`gallery_maintenance_run.py`**, in the gallery repository, exists
because the orrery's runner cannot see the public surface. When the Sun
exhibit first shipped, three of the four defects it exposed were on the
gallery side and no check here could reach any of them -- including one
where GitHub Pages served no Python file in the repository at all, which
was invisible on the developer's machine and invisible in the repository,
because it existed only on the deployed site.

So that runner has two moments rather than one: a default offline pass
before committing, and a `--live` pass after pushing that adds the checks
which can only mean anything once GitHub Pages has deployed.

It also has three states rather than two: PASS, FAIL, and UNREACHABLE. A
check that could not run is never counted as a check that passed. Node
missing is UNREACHABLE. No network is UNREACHABLE. A site serving
different bytes than the working copy is UNREACHABLE, because the thing
being checked is not the thing that answered.

**That last distinction is a general rule here, and the sharpest one in
the project:** a green result answers two questions at once and does not
say which. Did this pass, or did it never run? A test file nobody
executes, a parser that silently skips what it cannot read, a diff
against a path the tool does not track -- each reports exactly what a real
pass reports. So the question is never "did it pass." It is: *what would
make this fail, and does the passing output prove that path was live?*

## The push

The workflow is single-author and deliberately simple: edit, test, run
the maintenance suite, then commit and push through GitHub Desktop.

There is no branching model and no pull request stage, because there is
one author and nothing to reconcile. Every commit is pushed immediately
after it is made, and that is not merely a habit -- it is what makes the
SHA round trip work. Because the push always precedes the next session,
the remote HEAD *is* the next session's ground truth by construction. A
commit sitting locally unpushed would break that guarantee silently,
which is why it does not happen.

Two rules govern how edits arrive in the first place.

**Existing files are edited with targeted changes, not regenerated.**
This is the oldest discipline in the project and it was learned by
watching the opposite fail: full-file replacement corrupted the original
single-file orrery in 2024. A bad snippet is a localized error; a
complete file written from a stale base is destructive.

**An edit is delivered as a runnable patch script, not as text to paste.**
Every patch fingerprints the file before writing, refuses if the working
copy is not what it was built against, applies all its edits or none of
them, and prints what it changed. The reason is what a paste actually is:
text on a clipboard passes through several participants and not one of
them reports the outcome, so a paste that silently dropped and a paste
that landed perfectly produce identical evidence, which is none. A patch
script has the opposite shape -- success carries evidence. Patch scripts
are named for the ledger handle that authorized them and archived into
`documentation/` once they have run.

Patches do not write `.bak` files. The fingerprint guard means that at the
moment a patch writes, the file on disk is the committed version, so git
already holds it and Discard Changes restores it. A stale backup copy is
an active hazard rather than clutter: a later session grepping for a value
can hit one and read it as current.

---

# PART 3 -- ADMINISTRATIVE

## Contributing

This project is maintained by a single developer but welcomes community
input. Areas of interest: additional spacecraft mission data, solar system
structure visualizations, stellar classification improvements, exoplanet
systems, performance optimization, cross-platform testing, documentation,
and climate data integration.

Suggestions are welcome at <tonyquintanilla@gmail.com>. For bug reports,
include your Python version, the steps to reproduce, and any error
messages.

**A note for anyone reading the code cold.** Its structure, docstrings and
engineering discipline are the product of iterative collaboration with AI
models rather than of a professional software background. Tony is not a
trained programmer and does not present as one; what he owns and drives is
the workflow described in Part 2 -- the protocol, the planning, the design
review, the ledger, the cross-model orchestration, and every integration
judgment. The code quality is a real output of that method, and it should
not be read as evidence of something else.

## License

MIT License

Copyright (c) 2025-2026 Tony Quintanilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contact

**Author:** Tony Quintanilla
**Email:** <tonyquintanilla@gmail.com>
**GitHub:** [github.com/tonylquintanilla/palomas_orrery](https://github.com/tonylquintanilla/palomas_orrery)
**Website:** [palomasorrery.com](https://palomasorrery.com/)
**Instagram:** [@palomas\_orrery](https://www.instagram.com/palomas_orrery/)
**YouTube:** [Paloma's Orrery](https://www.youtube.com/@tony_quintanilla/featured)

---

**Acknowledgments:**

- [NASA JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/) for planetary and spacecraft ephemerides
- [ESA Gaia Mission](https://www.cosmos.esa.int/web/gaia) for stellar data
- [VizieR catalog service](https://vizier.cds.unistra.fr/) (CDS, Strasbourg)
- [SIMBAD astronomical database](https://simbad.u-strasbg.fr/simbad/)
- [Scripps CO2 Program](https://scrippsco2.ucsd.edu/) for Mauna Loa data
- [NASA GISS](https://data.giss.nasa.gov/gistemp/), [NSIDC](https://nsidc.org/) and [NOAA](https://www.noaa.gov/) for climate records
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu/) for ERA5 reanalysis
- [SOHO/LASCO](https://soho.nascom.nasa.gov/) coronagraph observations (ESA/NASA)
- [GRAVITY Collaboration](https://www.mpe.mpg.de/ir/gravity) for S-star orbital data
- [Astropy](https://www.astropy.org/) and [Astroquery](https://astroquery.readthedocs.io/) development teams
- [Plotly](https://plotly.com/) and [Pyodide](https://pyodide.org/) 
- AI collaborators: [Anthropic Claude](https://www.anthropic.com/claude), [OpenAI ChatGPT](https://openai.com/chatgpt), [Google Gemini](https://gemini.google.com/), DeepSeek

**Currency.** This file carries no counts, sizes or module totals by
design -- every such number lives in a generated document that cannot go
stale the way a hand-written one does, and this file points at those
documents instead. What can still go stale here is the description of the
architecture and the workflow. When either changes, this file is part of
the change, and its header block at the top is updated in the same edit.
