#!/usr/bin/env python3
"""
patch_L191_1_tooltip_br_20261018.py -- the GUI's checkbox tooltips show
a line break where their text says <br>. One line of code in the
tooltip class, every tooltip at once, no string touched. Records it on
L-191, L-412 and L-351, writes the manifest, and updates Where We Are.

Built on orrery f58f69f5fafbf51882fc33ac353b51c345a7f3f8 at
https://github.com/tonylquintanilla/palomas_orrery and gallery
0be187ec41e365b466cfaaacea8ffb05ef920587 at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 18, 2026 with Anthropic's Claude Fable 5.1.

RUN COMMAND

    python patch_L191_1_tooltip_br_20261018.py

    Saved in the ORRERY folder above. Open it in VS Code and click Run.
    It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing; each file is edited only at the lines it
changes, so your notes elsewhere are kept:

    palomas_orrery.py               CreateToolTip.showtip: one line; the
                                    module docstring's stamp
    LEDGER_CONSOLIDATED.md          the header stamp; L-191, L-412, L-351
    documentation/WHERE_WE_ARE.md   above the run-record marker only
    documentation/MANIFEST_L191_tooltip_fix_20261018.md   new

WHAT IS PERMANENT: the one line in CreateToolTip.showtip and the
manifest. This script is spent once it has run; move it into
documentation/.

Undo is Discard Changes in GitHub Desktop.
"""

import hashlib
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SHA = 'f58f69f'
ZONES = {}
MARKERS = {'documentation/WHERE_WE_ARE.md': '--- Your run record below this line'}
FINGERPRINTS = {}
RESULTS = {}
DELETES = {}

MANIFEST = """<!-- Doc-Kind: hand | Manifest: the GUI tooltip fix for L-191, what was measured, what changed, how it was tested. -->
# MANIFEST: the GUI's checkbox tooltips show line breaks (L-191)

Built on orrery f58f69f at https://github.com/tonylquintanilla/palomas_orrery
and gallery 0be187e at https://github.com/tonylquintanilla/tonyquintanilla.github.io.
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Type: BUILD (one line of code, plus records). Companion patch:
`documentation/patch_L191_1_tooltip_br_20261018.py`.
Written October 18, 2026 with Anthropic's Claude Fable 5.1.

## 1. What Tony saw, and what it was

- Tony, 2026-10-18, hovering the Sun's shell checkboxes in the orrery's
  window: the tooltips show the characters `<br>` instead of line
  breaks. He recalled it as fixed one to two months ago.
- It was diagnosed then and never built. L-191 (display-text
  duplication across the shell modules) recorded the cause on August 7
  and measured 58 affected strings on August 21 and 24. Its first job
  was "confirm by render" and nothing after it moved.
- The cause, read from the code: the tooltip strings (`core_info`,
  `alfven_surface_info` and the rest) are written with Plotly's `<br>`,
  and `CreateToolTip` in `palomas_orrery.py` hands its text to a Tk
  label as given. A Tk label prints what it is given.
- It is not a regression. Every commit of `solar_visualization_shells.py`
  since 2026-08-22 carries `<br>` in those strings. The `<br>` went in
  on 2026-05-25 (commit 97bbfe3).

## 2. Measured at f58f69f: which tooltips are affected

Every string a GUI tooltip shows, by both paths: the direct
`CreateToolTip(widget, name)` calls in `palomas_orrery.py`, and the
names `build_shell_checkboxes` (celestial_objects.py) builds at run
time from `SHELL_DEFINITIONS`. Each name resolved to its definition in
the source and read as a raw slice, not evaluated (the August lesson:
an evaluator skips f-strings silently).

122 tooltip strings examined. 58 carry `<br>`, and no other tag:

| Body | Strings | Path |
|---|---|---|
| Sun | 19 | direct calls, `solar_visualization_shells.py` |
| Jupiter | 10 | run time |
| Saturn | 10 | run time |
| Uranus | 8 | run time |
| Neptune | 8 | run time |
| Planet 9 | 2 | run time |
| Moon | 1 | run time |

Clean: Earth (its 11 are written with newlines), the asteroid belt,
the object checkboxes (their text comes from `INFO` in
info_dictionary.py, whose five `<br>` entries are star classes no
checkbox shows), and the two tooltips in `orbital_param_viz.py`, which
has its own copy of the class. The August count of 58 reproduces
exactly.

## 3. What changed

One line in `CreateToolTip.showtip` (`palomas_orrery.py`): the label's
text is `self.text.replace('<br>', '\\n')`. A string written with `<br>`
now reads as lines in the GUI; a string written with newlines is
unchanged. All 58 at once; no string touched; the plots cannot change,
because the plots never read this class.

This is the reverse of the canonical direction (orrery-coding-
conventions, Canonical Text Format: write in newlines, derive `<br>`
for Plotly). It is a backstop at the Tk boundary, not a licence to
write in `<br>`. The structural fix stays owed per slice (section 5).

## 4. How it was checked

- The patched `palomas_orrery.py` compiles (py_compile, Python 3.13).
- The tooltip class was exercised under a real Tk display (xvfb,
  Python 3.12): a widget given a three-line `<br>` string shows a label
  whose text holds two newlines and no `<br>`; a newline-authored
  string comes through unchanged. The class source was taken from the
  PATCHED throwaway copy, not retyped.
- The full headless run of the orrery (agentic-pre-test's standard
  test) could not be run here: the sandbox's Tk-bearing Python has none
  of the orrery's dependencies. Tony's own run and look are the gate:
  open the orrery, hover a Sun shell checkbox and a Jupiter one.
- The patch applied on a throwaway copy of the repository at f58f69f:
  every anchor matched once; the ledger index rebuilt with no problems;
  Where We Are stays under its 130-line cap; a second run refused.

## 5. What stays owed (L-191's gap, rewritten)

- (1b) The structural fix, per slice: the Sun's 19 strings in the Sun's
  slice (L-412), written in newlines, their 14 `_info_hover` twins
  deleted, `<br>` derived at the Plotly boundary the way the gas-giant
  configs already do. The gas giants' 36, Planet 9's 2 and the Moon's 1
  when their rooms open.
- (2) Earth, when its talks come: no visible bug, the same duplication,
  and the surface-specific-text case that decides the shape of the fix.
- orrery-coding-conventions' sentence "a tk.Label renders text
  literally, so `<br>` shows up on screen" is out of date after this
  patch; carried on L-351 for the skill's next bump, since a session
  following it would do nothing wrong.

## 6. Tony's steps

1. (do) Run this patch from VS Code (orrery folder).
2. (do) Run the orrery maintenance run from the dashboard: the ledger
   index picks up the dates; expect 31 of 31 gating and the gate at
   0 TIER-1 (the patch types no number).
3. (decide) Open the orrery, hover a Sun shell checkbox and a Jupiter
   one: lines, not `<br>`. Your look is the gate.
4. (do) Move this patch into documentation/; commit; push.

## 7. Skill versions

This session confirmed its loaded copies read ledger-and-session-records
1.21, safe-file-editing 1.13, agentic-pre-test 1.3 and
orrery-coding-conventions 1.10, as the manifest expects. v3.103's
obligation, provenance-discipline 2.31, still travels: no provenance
work fired here.
"""

NEW_FILES = {
    'documentation/MANIFEST_L191_tooltip_fix_20261018.md': MANIFEST,
}

EDITS = [
    # ---- palomas_orrery.py: the one line, and the stamp ----
    ('palomas_orrery.py', 'CreateToolTip shows <br> as a line break',
     "            label = tk.Label(\n"
     "                self.tw,\n"
     "                text=self.text,\n"
     "                justify='left',\n",
     "            # L-191 (2026-10-18): the shell tooltip strings are written\n"
     "            # with Plotly's <br>, and a Tk label prints what it is given.\n"
     "            # Show each <br> as a line break here, at the Tk boundary, so\n"
     "            # every tooltip reads as lines now. The canonical form is\n"
     "            # still newlines (orrery-coding-conventions, Canonical Text\n"
     "            # Format); this is the backstop until each body's strings\n"
     "            # are rewritten that way in its own slice.\n"
     "            label = tk.Label(\n"
     "                self.tw,\n"
     "                text=self.text.replace('<br>', '\\n'),\n"
     "                justify='left',\n"),
    ('palomas_orrery.py', 'module stamp',
     "Both the static plot and the animation use it.)\n"
     "\n"
     "\"\"\"\n",
     "Both the static plot and the animation use it.)\n"
     "Module updated: October 18, 2026 with Anthropic's Claude Fable 5.1 (L-191:\n"
     "CreateToolTip shows a <br> in its text as a line break, so the 58 shell\n"
     "tooltip strings written with Plotly's <br> read as lines in the window\n"
     "until each body's strings are rewritten in the newline form.)\n"
     "\n"
     "\"\"\"\n"),

    # ---- the ledger ----
    ('LEDGER_CONSOLIDATED.md', 'header stamp',
     "kelvin), built on 6f4fc9b0 and gallery da442bf2.\n",
     "kelvin), built on 6f4fc9b0 and gallery da442bf2.\n"
     "Module updated: October 18, 2026 with Anthropic's Claude Fable 5.1\n"
     "(L-191 confirmed by render and re-measured, the one-line tooltip fix\n"
     "built, its gap rewritten; the Sun's 19 strings onto L-412; a skill\n"
     "sentence carried on L-351), built on f58f69f5 and gallery 0be187ec.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-191 meta',
     "<!-- L:191 status:OPEN upd:2026-08-07 section:A flag: rice:3/4/70/3 -->",
     "<!-- L:191 status:OPEN upd:2026-10-18 section:A flag: rice:3/4/70/3 -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-191 confirmed, measured, ruled, built',
     "**Gap (rewritten 2026-08-24 on the survey):** THREE JOBS, not two,\n"
     "and the first is a look rather than a build.\n",
     "- **2026-10-18, confirmed by render and re-measured** (Claude Fable\n"
     "  5.1, the coordination session). Tony, hovering the Sun's shell\n"
     "  checkboxes in the orrery's window: the tooltips show `<br>`. He\n"
     "  recalled it as fixed one to two months ago; it was diagnosed then and\n"
     "  never built. Every commit of `solar_visualization_shells.py` since\n"
     "  2026-08-22 carries `<br>` in its `_info` strings and all 14\n"
     "  `_info_hover` twins, and `CreateToolTip` shows its text as given.\n"
     "  Re-measured at f58f69f by both paths (the direct `CreateToolTip`\n"
     "  calls, and the names `build_shell_checkboxes` builds from\n"
     "  `SHELL_DEFINITIONS`), from raw source slices: 122 tooltip strings\n"
     "  examined, 58 carry `<br>` and no other tag: the Sun 19 (direct calls,\n"
     "  `solar_visualization_shells.py`), Jupiter 10, Saturn 10, Uranus 8,\n"
     "  Neptune 8, Planet 9 2, the Moon 1. Clean: Earth (its 11 are\n"
     "  newline-authored), the asteroid belt, the object checkboxes (`INFO`\n"
     "  in info_dictionary.py; its five `<br>` entries are star classes no\n"
     "  checkbox shows), and `orbital_param_viz.py`'s own two tooltips. The\n"
     "  August 58 reproduces exactly. Job (0) is done by Tony's look.\n"
     "- **Tony's ruling, 2026-10-18: \"yes to both.\"** The one-line fix now:\n"
     "  `CreateToolTip.showtip` shows each `<br>` as a line break, every\n"
     "  tooltip at once, no string touched, the plots unreachable from that\n"
     "  class. And the structural fix per slice: the Sun's 19 strings join\n"
     "  the Sun's slice (L-412); the rest wait for their rooms. Built:\n"
     "  `documentation/patch_L191_1_tooltip_br_20261018.py`; record\n"
     "  `documentation/MANIFEST_L191_tooltip_fix_20261018.md`. The one-line\n"
     "  fix is the reverse of the canonical direction (orrery-coding-\n"
     "  conventions, Canonical Text Format): a backstop at the Tk boundary,\n"
     "  not a licence to write in `<br>`; the skill's sentence that a Tk\n"
     "  label shows `<br>` literally is carried on L-351 for its next bump.\n"
     "**Gap (rewritten 2026-10-18):** (0) done, by Tony's look. (1a) BUILT:\n"
     "the tooltip class shows `<br>` as a line break; Tony's look at a Sun\n"
     "and a Jupiter checkbox closes it. (1b) The structural fix, per slice:\n"
     "the Sun's 19 in the Sun's slice (L-412), written in newlines, their 14\n"
     "`_info_hover` twins deleted, `<br>` derived at the Plotly boundary as\n"
     "the gas-giant configs do; the gas giants' 36, Planet 9's 2 and the\n"
     "Moon's 1 when their rooms open. (2) Earth as below, when its talks\n"
     "come. The 2026-08-24 text follows, kept as the record.\n"
     "**Gap (rewritten 2026-08-24 on the survey; superseded above):** THREE JOBS, not two,\n"
     "and the first is a look rather than a build.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-412 meta',
     "<!-- L:412 status:OPEN upd:2026-10-17 section:A flag: rice: -->",
     "<!-- L:412 status:OPEN upd:2026-10-18 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-412 the Sun tooltip strings',
     "**Gap:** L-455 (Earth's share), the numbers half's last item; then\n"
     "Tony's choice of drawings, the streamer belt's and the clumps'\n"
     "eyeballed numbers with them; then L-443.\n",
     "- **2026-10-18 (Tony, on L-191):** the Sun's 19 checkbox tooltip\n"
     "  strings in `solar_visualization_shells.py` join this slice: written\n"
     "  in newlines, their 14 `_info_hover` twins deleted, `<br>` derived at\n"
     "  the Plotly boundary, when that file is next open for the Sun's words\n"
     "  (L-411's remaining bulk, or the drawings half). Until then the\n"
     "  tooltip class shows them as lines (L-191's one-line fix).\n"
     "**Gap:** L-455 (Earth's share), the numbers half's last item; then\n"
     "Tony's choice of drawings, the streamer belt's and the clumps'\n"
     "eyeballed numbers with them, and L-191's 19 Sun strings when that\n"
     "file is open; then L-443.\n"),
    ('LEDGER_CONSOLIDATED.md', 'L-351 meta',
     "<!-- L:351 status:OPEN upd:2026-10-17 section:A flag: rice: -->",
     "<!-- L:351 status:OPEN upd:2026-10-18 section:A flag: rice: -->"),
    ('LEDGER_CONSOLIDATED.md', 'L-351 conventions sentence',
     "**Gap:** Each lands with its store's next bump.\n"
     "**Ref:** skills/interactive-exhibit/SKILL.md; skills/ledger-and-session-records/SKILL.md;",
     "  - **2026-10-18, orrery-coding-conventions, next bump (Canonical Text\n"
     "    Format):** since L-191's one-line fix, `CreateToolTip` shows `<br>`\n"
     "    as a line break, so the sentence \"A `tk.Label` renders text\n"
     "    literally, so `<br>` shows up on screen as the characters `<br>`\"\n"
     "    is out of date. The canonical form stays `\\n`; the Tk-side\n"
     "    conversion is a backstop, not a licence to write in `<br>`. A\n"
     "    session following the old sentence would do nothing wrong, so it\n"
     "    is carried here (A Wrong Sentence in a Skill: Bump Now, or Carry\n"
     "    It).\n"
     "**Gap:** Each lands with its store's next bump.\n"
     "**Ref:** skills/interactive-exhibit/SKILL.md; skills/ledger-and-session-records/SKILL.md;"),

    # ---- Where We Are ----
    ('documentation/WHERE_WE_ARE.md', 'date',
     "Last updated: October 17, 2026, night: the Sun's numbers are built.\n"
     "- Written at orrery 6f4fc9b and gallery da442bf.",
     "Last updated: October 18, 2026: the Sun's numbers pushed; the tooltips fixed.\n"
     "- Written at orrery f58f69f and gallery 0be187e."),
    ('documentation/WHERE_WE_ARE.md', 'changed',
     ">   reads them first. Temperatures are in kelvin.\n",
     ">   reads them first. Temperatures are in kelvin.\n"
     "> - GUI checkbox tooltips show line breaks, not `<br>` (L-191, tooltip strings).\n"),
    ('documentation/WHERE_WE_ARE.md', 'needs you now',
     "> - *Two patches, in the handoff's order: orrery first, push, then the\n"
     ">   website and the Daily Run.*\n",
     "> - *Run patch_L191_1 (the tooltip fix); the orrery run; hover a Sun\n"
     ">   and a Jupiter checkbox; commit; push.*\n"),
    ('documentation/WHERE_WE_ARE.md', 'signals',
     "- Last cache build: 20261018T000459Z, ok, every rename on the first try (gallery da442bf).\n"
     "- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 6f4fc9b\n"
     "  with this session's patch).\n",
     "- Last cache build: 20261018T051313Z, ok; one rename needed a second try (gallery 0be187e).\n"
     "- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, f58f69f).\n"),
    ('documentation/WHERE_WE_ARE.md', 'signals date',
     "- This page's date and the ledger's newest stamp: both Oct 17. Agree.",
     "- This page's date and the ledger's newest stamp: both Oct 18. Agree."),
]


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the right folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def fingerprint(rel, text):
    zone = ZONES.get(rel)
    if zone:
        a = text.index(zone[0])
        b = text.index(zone[1]) + len(zone[1])
        text = text[:a] + text[b:]
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def main():
    log, notes, texts, crlf = [], [], {}, {}
    try:
        for rel, content in NEW_FILES.items():
            if os.path.exists(os.path.join(ROOT, rel)):
                have, _c = read(rel)
                if have != content:
                    raise PatchError("%s already exists with other content; "
                                     "nothing was overwritten" % rel)
                notes.append("note: %s already present, identical" % rel)
            else:
                log.append("ok  new     %s" % rel)
        for rel in sorted(set(e[0] for e in EDITS)):
            texts[rel], crlf[rel] = read(rel)
        for rel, want in FINGERPRINTS.items():
            if fingerprint(rel, texts[rel]) != want:
                raise PatchError("BASE MOVED: %s is not the file this patch "
                                 "was built against (%s)" % (rel, SHA))
            log.append("ok  base    %s matches %s" % (rel, SHA))
        for rel, label, old, new in EDITS:
            text = texts[rel]
            n = text.count(old)
            if n != 1:
                raise PatchError("ANCHOR FAIL [%s %s]: %d matches"
                                 % (rel, label, n))
            mark = MARKERS.get(rel)
            if mark and (text.count(mark) != 1
                         or text.index(old) + len(old) > text.index(mark)):
                raise PatchError("ANCHOR FAIL [%s %s]: not above the "
                                 "run-record marker" % (rel, label))
            texts[rel] = text.replace(old, new)
            log.append("ok  edit    %-44s %s" % (rel, label))
        page = 'documentation/WHERE_WE_ARE.md'
        above = texts[page].index(MARKERS[page])
        lines_above = texts[page][:above].count("\n")
        if lines_above > 130:
            raise PatchError("Where We Are would be %d lines above the "
                             "run-record marker; the cap is 130" % lines_above)
        log.append("ok  check   %-44s %d lines above the marker (cap 130)"
                   % (page, lines_above))
        for rel, text in list(texts.items()) + list(NEW_FILES.items()):
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s) after the "
                                 "edits" % (rel, bad))
        src = texts['palomas_orrery.py']
        if src.count("text=self.text.replace('<br>', '\\n'),") != 1:
            raise PatchError("palomas_orrery.py: the tooltip line did not land once")
        compile(src, 'palomas_orrery.py', 'exec')
        log.append("ok  check   %-44s compiles after the edit" % 'palomas_orrery.py')
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        print("Undo is not needed. Discard Changes in GitHub Desktop restores "
              "any file you changed by hand.")
        sys.exit(1)
    except SyntaxError as exc:
        print("ERROR: palomas_orrery.py would not compile after the edit: %s" % exc)
        print("NOTHING was written.")
        sys.exit(1)

    for rel, content in NEW_FILES.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
    for rel, text in texts.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf[rel]:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log:
        print(line)
    for line in notes:
        print(line)
    print("stamps updated: palomas_orrery.py's docstring; the ledger's header;")
    print("                Where We Are's date")
    print("")
    print("patch applied (%d new file, %d edits in %d files)"
          % (len(NEW_FILES), len(EDITS), len(texts)))
    print("")
    print("NEXT:")
    print("  1. Run the orrery maintenance run (dashboard): the ledger index")
    print("     picks up the dates; expect 31 of 31 gating, gate 0 TIER-1.")
    print("  2. Open the orrery; hover a Sun shell checkbox and a Jupiter one:")
    print("     lines, not <br>. Your look is the gate.")
    print("  3. Move this script into documentation/; commit; push.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
