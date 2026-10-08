#!/usr/bin/env python3
"""
patch_L001_1_earth_system_track_20261007.py -- ORRERY repo. Records
Tony's rulings of 2026-10-07 on the Earth System track: central, behind
the website build, the gallery's cards serving meanwhile; and the two
2026 heat-dome scenarios closed because the events are over.

Built on orrery 8653ef1b593aaf3835ecbcf2186b9e3e28a28089 at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
read or changed. No code changes: records only.

HOW TO RUN IT
    Save this file in the ORRERY repo ROOT (next to palomas_orrery.py),
    open it in VS Code and click Run (the command is
    python patch_L001_1_earth_system_track_20261007.py). Then follow the
    NEXT steps it prints.

    It runs before or after patch_L027_2, patch_L418_2 and
    patch_L412_1: it edits lines none of them touch. On Where We Are it
    changes only the road, two lines, and leaves the header, the
    Read-this-first box and every section patch_L418_2 rewrites alone.

WHAT CHANGES
    LEDGER_CONSOLIDATED.md
        a header stamp;
        L-001: its date; Tony's ruling on the track, as the one place the
            other four rows point at; L-071's two optional follow-ons
            re-homed here;
        L-060, L-070: their dates and one line each, pointing at L-001;
        L-071, L-077: closed (DONE, section C), with the reason and
            where each loose end went. ledger_index.py moves the two
            blocks into the closed section when you run the maintenance
            run; that is expected.
    documentation/WHERE_WE_ARE.md
        the road: a new stage 14, [later], for the Earth System layers;
        the goal becomes stage 15.
    Matched only at those lines (L-419). Your notes elsewhere do not
    stop it.

    Permanent: the ledger lines and the road stage. The script is spent
    once it has run; file it in documentation/.

TESTED on a copy of 8653ef1b: every edit landed; ledger_index.py --check
reported no consistency problems, and its run moved L-071 and L-077 to
section C; a second run refused and wrote nothing; and the three
pending patches named above still found their anchors afterwards.

SUCCESS looks like: one "ok" line per edit, then "patch applied".
FAILURE looks like: one ANCHOR FAIL: or ERROR: line, and NOTHING is
written. Undo is Discard Changes in GitHub Desktop.

Written October 7, 2026 with Anthropic's Claude Fable 5.1.
"""

import os

ROOT_MARKERS = ("palomas_orrery.py", "LEDGER_CONSOLIDATED.md")
NEXT = ["1. Move this script into documentation/.",
        "2. Run orrery_maintenance_run.py (its Ledger index step moves L-071",
        "   and L-077 into the closed section; that is expected).",
        "3. Commit and push."]

RULING = (
    "- **Tony's ruling, 2026-10-07, on the Earth System track as a whole:**\n"
    "  \"The earth system track is central but behind the orrery website\n"
    "  build. In the meantime the cards in the gallery work.\" So the\n"
    "  track is neither parked nor retired: it is sequenced behind the\n"
    "  website build, and the gallery's static Earth System cards and\n"
    "  lobby door carry it to visitors until then. It now has a stage on\n"
    "  the road in `documentation/WHERE_WE_ARE.md` (stage 14, [later]).\n"
    "  This row is the one place for that ruling; L-060 and L-070 point\n"
    "  here. The two dated 2026 heat-dome scenarios, L-071 and L-077,\n"
    "  closed the same day: \"They can close for practical reasons the\n"
    "  event is over.\"\n"
    "- **Re-homed from L-071 at its close, optional and for when the\n"
    "  track resumes:** (a) the WWA attribution watch across the\n"
    "  europe_* series, if a study publishes; (b) a Sentinel-3 LST\n"
    "  surface snapshot as a separate artifact.\n"
)

EDITS = {
  "LEDGER_CONSOLIDATED.md": [
    ("header stamp",
     "Review and RICE update Tony 6-21-2026\n",
     "Module updated: October 7, 2026 with Anthropic's Claude Fable 5.1\n"
     "(L-001: the Earth System track ruled central and behind the website\n"
     "build, on the road as stage 14; L-071 and L-077 closed, the events\n"
     "over), built on 8653ef1b.\n"
     "Review and RICE update Tony 6-21-2026\n"),
    ("L-001 date",
     "<!-- L:001 status:OPEN upd:2026-06-30 section:A flag: rice:3/3/95/2 -->\n",
     "<!-- L:001 status:OPEN upd:2026-10-07 section:A flag: rice:3/3/95/2 -->\n"),
    ("L-001 ruling",
     "**Ref:** MANIFEST_food_insecurity_sudan_v2.md; HANDOFF_food_insecurity_build_v2.md\n"
     "(built on 03630ae); cross-ref L-064, L-069.\n",
     RULING +
     "**Ref:** MANIFEST_food_insecurity_sudan_v2.md; HANDOFF_food_insecurity_build_v2.md\n"
     "(built on 03630ae); cross-ref L-064, L-069; L-060, L-070 (the track's\n"
     "other open rows); L-071, L-077 (closed 2026-10-07);\n"
     "`documentation/WHERE_WE_ARE.md` (the road, stage 14).\n"),
    ("L-060 date",
     "<!-- L:060 status:OPEN upd:2026-06-18 section:A flag: rice:3/3/75/2.5 -->\n",
     "<!-- L:060 status:OPEN upd:2026-10-07 section:A flag: rice:3/3/75/2.5 -->\n"),
    ("L-060 pointer",
     "**Ref:** ENSO_chart_spec.md v2 (design spec, this session); cross-ref L-001 (Food Insecurity, same Earth System track); energy_imbalance.py (Phase 2 target).\n",
     "- **2026-10-07:** the Earth System track is ruled central and\n"
     "  sequenced behind the website build; the ruling is on L-001. This\n"
     "  item waits there, not as a tail item.\n"
     "**Ref:** ENSO_chart_spec.md v2 (design spec, this session); cross-ref L-001 (Food Insecurity, same Earth System track; the track's ruling of 2026-10-07); energy_imbalance.py (Phase 2 target).\n"),
    ("L-070 date",
     "<!-- L:070 status:OPEN upd:2026-06-24 section:A flag: rice:2/3/45/3 -->\n",
     "<!-- L:070 status:OPEN upd:2026-10-07 section:A flag: rice:2/3/45/3 -->\n"),
    ("L-070 pointer",
     "**Ref:** L-001 (parent), L-069 (P5 dots reused per country); food_insecurity_generator.py.\n",
     "- **2026-10-07:** the Earth System track is ruled central and\n"
     "  sequenced behind the website build; the ruling is on L-001.\n"
     "**Ref:** L-001 (parent; the track's ruling of 2026-10-07), L-069 (P5 dots reused per country); food_insecurity_generator.py.\n"),
    ("L-071 closed",
     "<!-- L:071 status:OPEN upd:2026-06-25 section:A flag: rice:3/3/70/2.5 -->\n",
     "<!-- L:071 status:DONE upd:2026-10-07 section:C flag: rice:3/3/70/2.5 -->\n"),
    ("L-071 close record",
     "- **Close when:** the dome resolves and the series is complete.\n"
     "**Ref:** L-065 (build + chassis, closed); scenarios_heatwaves.py; Western\n"
     "dated-series precedent (scenarios_western_heatwave_march_2026.py).\n",
     "- **Close when:** the dome resolves and the series is complete.\n"
     "- **CLOSED 2026-10-07 (Tony):** \"They can close for practical reasons\n"
     "  the event is over.\" The series stands at its one entry,\n"
     "  europe_2026 (21 Jun, L-065); the 27-28 Jun peak scenario was not\n"
     "  captured and is not owed, the event having passed. Loose ends\n"
     "  re-homed to L-001, the Earth System track's one place: the WWA\n"
     "  attribution watch and the Sentinel-3 LST snapshot, both optional.\n"
     "**Ref:** L-065 (build + chassis, closed); scenarios_heatwaves.py; Western\n"
     "dated-series precedent (scenarios_western_heatwave_march_2026.py);\n"
     "L-001 (the track's ruling of 2026-10-07).\n"),
    ("L-077 closed",
     "<!-- L:077 status:OPEN upd:2026-06-30 section:A flag: rice:3/3/60/2.5 -->\n",
     "<!-- L:077 status:DONE upd:2026-10-07 section:C flag: rice:3/3/60/2.5 -->\n"),
    ("L-077 close record",
     "**Gap:** scaffold the dated-scenario module once ERA5T coverage reaches the\n"
     "event window (NOAA WPC June 27-29 peak + ~5-day lag -> earliest observed\n"
     "coverage ~early July). Forecast-vs-reanalysis visual treatment is the open\n"
     "design detail at build time.\n",
     "- **CLOSED 2026-10-07 (Tony):** \"They can close for practical reasons\n"
     "  the event is over.\" The scenario was never scaffolded, and is not\n"
     "  owed: a migrating-centroid scenario needs the event live, and this\n"
     "  one has passed. Struck with that reason. The DESIGN above -- the\n"
     "  forecast envelope ahead of the advancing reanalysis seam, under\n"
     "  Show the Envelope -- stays recorded here as the pattern for the\n"
     "  next such event, when the Earth System track resumes (L-001).\n"
     "**Gap:** none; closed by Tony's ruling. (Was: scaffold the dated-scenario\n"
     "module once ERA5T coverage reached the event window.)\n"),
  ],
  "documentation/WHERE_WE_ARE.md": [
    ("road: stage 14, the Earth System layers",
     " 13. [later]  The planets get their details -- layers, rings, magnetic\n"
     "              fields -- Jupiter and Saturn first.\n"
     " 14. [goal]   The website does what the desktop orrery does, from data\n",
     " 13. [later]  The planets get their details -- layers, rings, magnetic\n"
     "              fields -- Jupiter and Saturn first.\n"
     " 14. [later]  The Earth System layers -- heat, food insecurity, the\n"
     "              oceans -- come to the website from their generators and\n"
     "              sources, the way the orrery's numbers do. Until then the\n"
     "              gallery's Earth System cards carry them, as you ruled.\n"
     "              << new this session\n"
     " 15. [goal]   The website does what the desktop orrery does, from data\n"),
  ],
}


def read_lf(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def main():
    if os.path.basename(os.getcwd()) == "documentation":
        raise SystemExit("ERROR: run this from the repo ROOT, not from "
                         "documentation/. NOTHING was written.")
    for marker in ROOT_MARKERS:
        if not os.path.isfile(marker):
            raise SystemExit("ERROR: %s is not here, so this is not the "
                             "orrery root. NOTHING was written." % marker)
    results = []
    for path in sorted(EDITS):
        if not os.path.isfile(path):
            raise SystemExit("ERROR: %s is not here. NOTHING was written." % path)
        text, crlf = read_lf(path)
        before = sum(1 for ch in text if ord(ch) > 127)
        done = []
        for label, old, new in EDITS[path]:
            found = text.count(old)
            if found != 1:
                raise SystemExit("ANCHOR FAIL (%s): expected 1 match in %s, "
                                 "found %d. Has this patch already run? "
                                 "NOTHING was written." % (label, path, found))
            text = text.replace(old, new)
            done.append(label)
        if sum(1 for ch in text if ord(ch) > 127) > before:
            raise SystemExit("ERROR: %s would hold new non-ASCII text. "
                             "NOTHING was written." % path)
        results.append((path, text, done, crlf))
    for path, text, done, crlf in results:
        with open(path, "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            print("note: %s was CRLF in the working copy; written LF" % path)
        for label in done:
            print("ok  %-34s %s" % (path, label))
    print("")
    print("patch applied")
    print("")
    print("NEXT:")
    for line in NEXT:
        print("  " + line)


if __name__ == "__main__":
    main()
