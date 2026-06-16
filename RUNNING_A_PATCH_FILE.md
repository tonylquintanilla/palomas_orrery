# Running a Patch File
## Paloma's Orrery | June 16, 2026

A patch file (a "unified diff", usually ending in `.patch` or `.diff`) is a
**recipe of changes** to one or more files -- not the whole file, just the
regions that change, each wrapped in a few unchanged lines so the spot can be
located exactly. In this project, Claude often delivers a patch instead of (or
alongside) Mode-1 snippets: it is the same set of edits, in a compact,
all-or-nothing format that `git` can apply for you.

This guide is written for the project's normal setup: **VS Code** for file
management, **GitHub Desktop** for commits, on **Windows**. The mechanics are
the same on macOS and Linux.

---

## What a patch is (and is not)

- It is a list of edits: "in `palomas_orrery.py`, around line 8325, add this
  one line." It does **not** carry the whole file, so it cannot silently
  overwrite working code from a stale base -- a key safety property.
- Applying it is **atomic**: `git apply` either makes *every* change cleanly,
  or makes *none* and tells you why. It never leaves a file half-edited.
- It is tied to a **base** -- the exact commit it was written against. If your
  local copy has drifted from that commit, the lines will not line up and the
  patch is refused (safely). The fix is to get your local copy back to the
  right base (Fetch / Pull) before applying.

---

## Reading a patch (the anatomy)

```
--- a/palomas_orrery.py      <- the OLD version
+++ b/palomas_orrery.py      <- the NEW version
@@ -8291,6 +8325,7 @@        <- a "hunk": where this chunk sits
     _set_entry(days_to_plot_entry, '28')      (space = unchanged context)
     _set_entry(custom_scale_entry, '10')      (space = unchanged context)
+    _set_entry(custom_dtick_entry, '')        (+ = ADD this line)
     _set_entry(orbital_points_entry, '50')    (space = unchanged context)
```

- `--- a/...` / `+++ b/...` name the old and new file.
- `@@ -8291,6 +8325,7 @@` is a **hunk header**: this chunk starts near line
  8291 in the old file (6 lines) and line 8325 in the new file (7 lines). The
  numbers are just locators.
- Each content line has a one-character prefix:
  - a **space** = unchanged context (there only to find the spot; leave it),
  - `-` = remove this line,
  - `+` = add this line.

A patch is just several such hunks. Reading it is the same line-by-line review
you already do with snippets -- every `+` is something added, every `-` is
something replaced.

---

## Applying a patch, step by step

### Step 0 -- put the patch in the repo folder
Download the patch from the chat (it lands in Downloads). Move it into the
**root of the repo** -- the folder that contains `palomas_orrery.py`. Rename it
to something with **no spaces**, e.g. `phaseA.patch`. (Drag-and-drop and
right-click -> Rename both work in VS Code or Windows Explorer.)

### Step 1 -- open a terminal sitting in the repo folder
The reliable way (guarantees `git` is on the path):
**GitHub Desktop -> Repository menu -> Open in Command Prompt** (Ctrl+`).
The terminal opens already pointed at the repo folder.

(Alternative: in VS Code, File -> Open Folder -> the repo folder, then
Terminal -> New Terminal. If it ever says "git is not recognized", use the
GitHub Desktop route instead.)

### Step 2 -- make sure your local copy is at the right base
In **GitHub Desktop**, click **Fetch origin** (and **Pull** if it offers).
The patch was written against a specific commit; this lines your local copy up
with it so the patch can land cleanly.

### Step 3 -- dry run (changes nothing)
In the terminal:

```
git apply --check phaseA.patch
```

- **No output at all** = it will apply perfectly. Continue.
- **Any error message** = stop, do NOT apply, and send the message to Claude.
  Your file is untouched either way. (Most often this means the base drifted;
  see "If something goes wrong" below.)

### Step 4 -- apply it for real

```
git apply phaseA.patch
```

**No output means success** -- that is `git` being quietly competent.

### Step 5 -- review in GitHub Desktop
Switch to **GitHub Desktop**. `palomas_orrery.py` (and any other touched file)
appears under **Changes**, with additions in green and removals in red -- the
same spots from the diff. Scroll through and confirm it is exactly the edits
you discussed. This is your line-by-line review, shown by the tool instead of
typed by hand.

### Step 6 -- TEST before you commit
Do not commit yet. Run the render gate / launch the app and verify with your
eyes (the render is ground truth, always). A clean apply means the *text*
landed; it does not mean the *behavior* is right.

### Step 7 -- commit and push
Once it passes your eyes, commit + push in GitHub Desktop as usual. Note the
new commit **SHA** and hand it back to Claude so the handoff and ledger record
"built on `<old SHA>` -> pushed at `<new SHA>`".

---

## Verifying the patch landed exactly right (recommended)

After pushing, you can confirm the repo's actual change equals the intended
patch -- the same round-trip idea as the SHA check. Claude can do this from the
new HEAD: fetch the file at the new SHA, diff it against the base, and check
that the result equals the delivered patch -- "nothing extra rode along, nothing
got dropped." A matching result plus a matching remote HEAD is the full
round trip: commit + push + sync + intended-change, all confirmed.

---

## If something goes wrong

- **`--check` failed.** Usually the base drifted. In GitHub Desktop, **Fetch /
  Pull**, then run `git apply --check` again. If it still fails, send the exact
  message to Claude -- a patch can be re-cut against your current HEAD.
- **Applied, but it looks wrong** (before committing). GitHub Desktop ->
  right-click the file under Changes -> **Discard changes**. That reverts
  cleanly because nothing is committed yet.
- **"git is not recognized".** Use the GitHub Desktop terminal
  (Repository -> Open in Command Prompt), which always has `git`.
- **Already committed and want to undo.** History -> right-click the commit ->
  **Revert**, or ask Claude for the safest path for your situation.

---

## Why we use patches

- **All-or-nothing safety.** It applies completely or not at all -- never a
  half-edited file.
- **Tied to a base.** It refuses to apply against a drifted copy, which catches
  stale-base mistakes for you.
- **Exact and compact.** Only the changed regions, byte-for-byte.
- **Same edits as Mode-1 snippets**, just in a format a tool can apply and
  verify. You still review every line.

---

Written June 2026 with Anthropic's Claude Opus 4.8, in the Paloma's Orrery
double-helix workflow: Claude proposes the diff, Tony verifies, applies, and
tests, and the render is the ground truth.
