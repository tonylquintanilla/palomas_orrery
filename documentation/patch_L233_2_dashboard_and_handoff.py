"""
patch_L233_2_dashboard_and_handoff.py -- wire the dashboard to the two
devtool fixes, anchor the handoff, and record the item.

REPO: tonylquintanilla/palomas_orrery (the ORRERY repo).
Built on be39d54b3c856a6c1204d3fcbe3184ad7de8ab84 at
https://github.com/tonylquintanilla/palomas_orrery (branch main).
Companion gallery SHA: 099a85368ce7f467f88a35a65e0580dd97261b37.

RUN patch_L233_1 IN THE GALLERY REPO FIRST. This patch registers a button
for tools/serve_gallery.py, which that patch creates. Registering it first
is harmless -- the dashboard shows "Not Found" rather than failing -- but
the order above is the one that leaves nothing to come back to.

THREE FILES.

1. palomas_orrery_dashboard.py, Gallery & Web group:
   - "Inspect Staging" description rewritten to say what you GET rather
     than what it needs. The old text said "Takes one argument," which
     described the tool correctly and the BUTTON misleadingly, since a
     button cannot supply one. The tool now asks (L-233_1).
   - "Serve Gallery Locally" added. The assembler dev page cannot be
     opened by double-clicking it: it fetches the assembler files and the
     served cache, and browsers refuse fetch() from file://.
   - "Debug Encke TP" REMOVED from the dashboard. The file stays in the
     gallery repo as the record of its investigation. It existed to
     answer one question -- which Horizons identifier form resolves
     Encke's TP -- and that answer is now in objects_config.json as
     horizons_id 90000091 / id_type smallbody, matching Halley's
     90000030. It was also the only button that hit live Horizons, so it
     was the only one that could fail for reasons unrelated to the code.

2. documentation/HANDOFF_20260824_L154_second_half.md: the three
   <NEW_ORRERY_SHA> placeholders filled with be39d54b, and one line
   recording that the devtool patches landed after it.

3. LEDGER_CONSOLIDATED.md: L-233 opened and closed in one entry.

Re-run ledger_index.py afterwards (or maintenance_run.py, which does).

Written August 2026 with Anthropic's Claude Opus 5 (L-233).
"""

import hashlib
import os

DASH = "palomas_orrery_dashboard.py"
HANDOFF = os.path.join("documentation",
                       "HANDOFF_20260824_L154_second_half.md")
LEDGER = "LEDGER_CONSOLIDATED.md"

SESSION_SHA = "be39d54b3c856a6c1204d3fcbe3184ad7de8ab84"

EXPECT = {
    DASH: "1e2c934f422d05fd6b790e6fa9eb33ee",
    HANDOFF: "44eb6f7c59dc5b1d0e5c8d22d22c321c",
    LEDGER: "d139ba1e45e0ad31a87ebd6ce2d61e7b",
}


def norm(data):
    return data.replace(b"\r\n", b"\n")


def md5(data):
    return hashlib.md5(norm(data)).hexdigest()


DASH_EDITS = [
    (
        """        ("Inspect Staging",
        "inspect_staging.py",
        "Read-only plain-language report on an existing dry-run staging "
        "folder. Takes one argument: the staging folder path printed at "
        "the end of a gallery_cache_builder.py --dry-run.",
        GALLERY_TOOLS_DIR,
        True),
        ("Debug Encke TP",
        "debug_encke_tp.py",
        "Run the exact live Horizons query the builder's fetch_solution_tp() "
        "makes for Encke and print the full raw response. No arguments.",
        GALLERY_TOOLS_DIR,
        True),""",
        """        ("Serve Gallery Locally",
        "serve_gallery.py",
        "Serve the gallery repo at http://localhost:8000 and open the "
        "assembler dev page, where Artifact 1 and the Artifact 2 candidate "
        "render in the browser. The page fetches the assembler files and "
        "the served cache, and browsers refuse fetch() from a file:// "
        "page, so it cannot be opened by double-clicking the HTML. Runs in "
        "its own console and keeps running -- one line per request is the "
        "server working, not a hang. Ctrl+C or close the window to stop.",
        GALLERY_TOOLS_DIR,
        True),
        ("Inspect Staging",
        "inspect_staging.py",
        "Plain-language report on a dry-run staging folder: real dates "
        "instead of Julian days, TP values, and point counts per object, "
        "so a dry-run can be judged without opening the raw JSON. "
        "Read-only -- fetches nothing, changes nothing, promotes nothing. "
        "Opens a console and asks for the staging folder path, which the "
        "builder prints on the last line of a --dry-run.",
        GALLERY_TOOLS_DIR,
        True),""",
    ),
]

HANDOFF_EDITS = [
    (
        "`<NEW_ORRERY_SHA>`**",
        "`" + SESSION_SHA + "`**",
    ),
    (
        "1. SHA round trip: orrery `<NEW_ORRERY_SHA>`, gallery `099a8536`.",
        "1. SHA round trip: orrery `" + SESSION_SHA[:8] + "` plus the L-233\n"
        "   devtool commit that followed it, gallery `099a8536` plus the same.\n"
        "   Read both live rather than trusting these.",
    ),
    (
        """*Session written August 24, 2026 with Anthropic's Claude Opus 5. Orrery
built on `2e40a1ebc3f24b02bc3dc57eeb7f652e61e10be2`, pushed at
`<NEW_ORRERY_SHA>`; gallery""",
        """**Devtool tidy-up followed, after `""" + SESSION_SHA[:8] + """`.** L-233:
the dashboard's Gallery & Web group gained a Serve Gallery Locally button,
Inspect Staging learned to ask for its path, and Debug Encke TP came off
the dashboard with its file left in place. Its own commit SHA is not
knowable from inside the session that wrote it; the next session's round
trip settles it.

*Session written August 24, 2026 with Anthropic's Claude Opus 5. Orrery
built on `2e40a1ebc3f24b02bc3dc57eeb7f652e61e10be2`, pushed at
`""" + SESSION_SHA + """`; gallery""",
    ),
]

LEDGER_EDITS = [
    (
        """## PENDING ACTION (Tony-side)""",
        """#### [L-233] Three dashboard buttons: one fixed, one added, one retired
<!-- L:233 status:DONE upd:2026-08-24 section:A flag: rice:2/2/95/1 -->
- **Tony asked for a review of four Gallery & Web buttons, 2026-08-24.**
  Two earned their place unchanged, one had an interface it could not
  satisfy, and one had outlived the question it was built to answer.
- **Gallery Builder Offline Tests -- kept, and the strongest of the
  four.** Run this session: 144 checks, zero failures, no network. It
  exercises first-build, the nightly shrink gate and the Guard v2
  monitor path. Worth noting for later that a button someone has to
  remember is weaker than a checker in the maintenance suite; moving it
  there is not done and is not tracked here.
- **Gallery Cleanup -- kept.** Orphan JSON and KMZ accumulate for as
  long as curation continues, and it confirms before deleting.
- **Inspect Staging -- the tool was right, the BUTTON could not work.**
  `main()` required `len(sys.argv) == 2` and the dashboard launches with
  no argument, so clicking it could only ever print usage. Fixed in the
  TOOL rather than by special-casing the dashboard, so the VS Code Run
  button gets the same benefit: it now asks for the staging folder, and
  a pasted Windows path keeps working because surrounding quotes are
  stripped. A path on the command line still works unchanged and a
  flag-shaped argument is still refused.
- **The description was the other half.** It read "Takes one argument,"
  which described the tool correctly and the button misleadingly. The
  new text says what the report contains and that it asks for the path.
- **Debug Encke TP -- retired from the dashboard, file kept.** It
  existed to answer one question: which Horizons identifier form
  resolves Encke's TP. Closed. `objects_config.json` carries
  `horizons_id: 90000091`, `id_type: smallbody`, the same pattern as
  Halley's `90000030`, which is the fix the tool's own docstring reasons
  its way to. It was also the only button on the dashboard that made a
  live Horizons call, so it was the only one that could fail for reasons
  unrelated to this code. The file stays as the record of the
  investigation; deleting it would lose the reasoning.
- **Serve Gallery Locally -- added.** `tools/serve_gallery.py` serves the
  gallery repo root at `localhost:8000` and opens the assembler dev
  page. It serves the ROOT rather than `gallery/` because the page
  reaches up to `../data/solar-system/`; served from inside `gallery/`
  the page loads and every fetch 404s, which looks like a broken page
  rather than a wrong working directory. It refuses to start when the
  served cache is absent and says which files are missing, and when the
  port is already taken it opens the browser against the running server
  instead of failing on a socket error. Both guards were exercised.
- **A batch-file draft was superseded before it shipped.** The dashboard
  launches Python scripts, not `.bat` files, so a `.bat` would have been
  a second implementation of the same checks in a language the dashboard
  cannot call. One implementation, in Python.
- **Ref:** `palomas_orrery_dashboard.py` (Gallery & Web group); gallery
  `tools/serve_gallery.py`, `tools/inspect_staging.py`,
  `tools/debug_encke_tp.py`, `tools/gallery_cleanup.py`,
  `tools/test_gallery_cache_builder_offline.py`;
  `patch_L233_1_gallery_devtools.py` (gallery),
  `patch_L233_2_dashboard_and_handoff.py` (orrery); L-154; L-188 (the
  maintenance runner).

## PENDING ACTION (Tony-side)""",
    ),
]


def apply_edits(text, edits, label):
    for i, (old, new) in enumerate(edits, start=1):
        n = text.count(old)
        if n != 1:
            raise SystemExit(
                "ABORT %s edit %d: anchor matched %d times, expected exactly 1.\n"
                "First 70 chars: %r" % (label, i, n, old[:70])
            )
        text = text.replace(old, new)
    return text


def main():
    if not os.path.exists(DASH):
        raise SystemExit(
            "ABORT: %s not found. Run this from the ROOT of the ORRERY repo "
            "(palomas_orrery)." % DASH
        )

    with open(__file__, "rb") as fh:
        if any(b > 127 for b in fh.read()):
            raise SystemExit("ABORT: this script carries non-ASCII bytes.")

    originals = {}
    styles = {}
    for path, expect in EXPECT.items():
        if not os.path.exists(path):
            raise SystemExit("ABORT: %s not found." % path)
        with open(path, "rb") as fh:
            data = fh.read()
        got = md5(data)
        if got != expect:
            raise SystemExit(
                "ABORT: %s fingerprint mismatch.\n  expected %s\n  got      %s"
                % (path, expect, got)
            )
        originals[path] = data
        styles[path] = b"\r\n" in data

    results = {}
    for path, edits in ((DASH, DASH_EDITS), (HANDOFF, HANDOFF_EDITS),
                        (LEDGER, LEDGER_EDITS)):
        text = norm(originals[path]).decode("utf-8")
        before = sum(1 for ch in text if ord(ch) > 127)
        new_text = apply_edits(text, edits, path)
        after = sum(1 for ch in new_text if ord(ch) > 127)
        if after > before:
            raise SystemExit("ABORT: %s non-ASCII rose %d -> %d."
                             % (path, before, after))
        results[path] = new_text

    # The dashboard must still be valid Python, and the three button names
    # must be exactly as intended -- present, present, gone.
    compile(results[DASH], DASH, "exec")
    if '"Serve Gallery Locally"' not in results[DASH]:
        raise SystemExit("ABORT: the new button did not land.")
    if '"Debug Encke TP"' in results[DASH]:
        raise SystemExit("ABORT: Debug Encke TP is still registered.")
    if results[DASH].count('"inspect_staging.py"') != 1:
        raise SystemExit("ABORT: Inspect Staging is registered %d times."
                         % results[DASH].count('"inspect_staging.py"'))
    if "<NEW_ORRERY_SHA>" in results[HANDOFF]:
        raise SystemExit("ABORT: a handoff SHA placeholder is still unfilled.")
    if results[LEDGER].count("<!-- L:233 ") != 1:
        raise SystemExit("ABORT: the L-233 status line did not land once.")

    original_ledger = norm(originals[LEDGER]).decode("utf-8")
    start = original_ledger.index("<!-- INDEX:START")
    end = original_ledger.index("<!-- INDEX:END")
    if original_ledger[start:end] not in results[LEDGER]:
        raise SystemExit("ABORT: the generated INDEX zone changed.")

    written = []
    try:
        for path, new_text in results.items():
            out = new_text.encode("utf-8")
            if styles[path]:
                out = out.replace(b"\n", b"\r\n")
            with open(path, "wb") as fh:
                fh.write(out)
            written.append(path)
    except Exception as exc:
        for path in written:
            with open(path, "wb") as fh:
                fh.write(originals[path])
        raise SystemExit("ABORT: write failed (%s); all files restored." % exc)

    for path in EXPECT:
        with open(path, "rb") as fh:
            data = fh.read()
        if md5(data) == EXPECT[path]:
            raise SystemExit("ABORT: %s still fingerprints as pre-edit." % path)
        if styles[path] and b"\r\n" not in data:
            raise SystemExit("ABORT: %s was CRLF and was written as LF." % path)

    with open(DASH, "rb") as fh:
        compile(norm(fh.read()).decode("utf-8"), DASH, "exec")

    print("PATCH L-233_2 APPLIED")
    for path in (DASH, HANDOFF, LEDGER):
        print("  %-46s %7d bytes%s"
              % (path, os.path.getsize(path),
                 "  (CRLF)" if styles[path] else "  (LF)"))
    print("  dashboard compiles; Serve Gallery Locally in, Debug Encke TP out")
    print("  handoff anchored at %s" % SESSION_SHA[:8])
    print("  L-233 recorded DONE; INDEX zone untouched")
    print("")
    print("NEXT:")
    print("  1. python ledger_index.py   (or maintenance_run.py, which runs it)")
    print("  2. Open the dashboard and click Serve Gallery Locally once, to")
    print("     confirm the button works. This patch checked that the entry")
    print("     is registered and the file compiles; it did not click it.")
    print("  3. Archive this script to documentation/.")


if __name__ == "__main__":
    main()
