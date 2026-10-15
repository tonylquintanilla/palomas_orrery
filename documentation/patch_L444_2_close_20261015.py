#!/usr/bin/env python3
"""
patch_L444_2_close_20261015.py -- closes L-444 (the missing periods) on
Tony's first live run, and opens the item for Earth's period from the
Earth-Moon barycentre (Tony's ruling of 2026-10-15).

Built on orrery 9579fcd577706b2eec8a9e552949331074f4e45b at
https://github.com/tonylquintanilla/palomas_orrery. The gallery is not
touched (read at 9f8569ee3125de27fed96c86c701e3c4d52d88e3 at
https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Tony's local folders: orrery
C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\palomas_orrery_for_github\\
gallery C:\\Users\\tonyq\\OneDrive\\Desktop\\python_work\\tonyquintanilla.github.io\\
Written October 15, 2026 with Anthropic's Claude Opus 5.5.

RUN COMMAND

    python patch_L444_2_close_20261015.py

    Save this file in the orrery folder above, open it in VS Code and click
    Run. It takes no arguments and asks no questions.

WHAT IT DOES, all or nothing, in three files

    LEDGER_CONSOLIDATED.md    L-444 to DONE, with Tony's run and its loose
                              ends re-homed; a new item for Earth's period,
                              given the next free handle when it runs (so a
                              session working in parallel cannot collide
                              with it); a second new item, the website's
                              Daily Run pulling the orrery's exports before
                              it builds the cache; header stamp
    documentation/WHERE_WE_ARE.md   above the run-record marker only: the
                              date, the box, road 8a done and the new 8b,
                              two Signals lines, Next
    documentation/HANDOFF_L444_missing_periods_build_20261015.md
                              the push SHA, and a section for the close

    Each file is checked only at the lines edited, so your notes in them
    never make it refuse. Every anchor must match exactly once.

WHAT IT PRINTS

    Success: one "ok" line per edit, the handle the new item received, then
    "patch applied". Failure: one ERROR or ANCHOR FAIL line and "NOTHING
    was written."

Undo is Discard Changes in GitHub Desktop.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
LEDGER = "LEDGER_CONSOLIDATED.md"
WWA = "documentation/WHERE_WE_ARE.md"
HANDOFF = "documentation/HANDOFF_L444_missing_periods_build_20261015.md"
MARKER = "--- Your run record below this line"
WWA_CAP = 130


class PatchError(Exception):
    pass


def read(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        raise PatchError("missing file: %s (is this the orrery folder?)" % rel)
    raw = open(path, "rb").read()
    return raw.replace(b"\r\n", b"\n").decode("utf-8"), (b"\r\n" in raw)


def rep(text, old, new, label, log, rel):
    n = text.count(old)
    if n != 1:
        raise PatchError("ANCHOR FAIL [%s %s]: expected 1 match, got %d: %r"
                         % (rel, label, n, old[:70]))
    log.append("ok  %-58s %s" % (rel, label))
    return text.replace(old, new)


# ------------------------------------------------------------------ ledger

L444_META_OLD = "<!-- L:444 status:OPEN upd:2026-10-15 section:A flag: rice: -->"
L444_META_NEW = "<!-- L:444 status:DONE upd:2026-10-15 section:C flag: rice: -->"

L444_TAIL_OLD = """- **Note (Claude):** a generator row does not count in the run's checker
  total. A fetch that fails shows on its own row as exit 1 with
  UNREACHABLE, and in the failure detail at the end, but the summary's
  checker count can still read all passed: a body left typed is not
  compared, so the Horizons check may have nothing due. Recorded, not
  changed: whether a failed generator should turn the run red is a
  question for the runner as a whole, not this row.
**Gap:** Tony's first live run: the eight fetched by name, or each
failure named; then one fetched body's hover in the orrery and, after
the push and the gallery's pull, on the website. Then close.
"""

L444_TAIL_NEW = """- **Note (Claude), struck at the close, 2026-10-15:** a generator row
  does not count in the run's checker total. Struck because nothing
  failed, the row names a failure by name and in the run's failure
  detail, and no ruling asks generators to gate; kept as history.
- **Tony's first live run, 2026-10-15** (his run record, the copy of
  `documentation/WHERE_WE_ARE_10-14-26_2250_run_record.md` he uploaded
  at 13:47): the patch applied on 7166648d, "patch applied (4 new
  files, 32 edits, 1 move)". The maintenance run's Period fetch row:
  "PASS -- fetched 8: Venus, Earth, Mars, Saturn, Uranus, Neptune,
  Apophis, Halley", elements refreshed for the same eight. The Horizons
  check: "PASS -- 8 checked today, 8 queries". Horizons confirmations:
  13 of 13 entries and 11 periods. 31 of 31 gating checkers. Pushed at
  9579fcd. Venus's hover in the orrery: "orbital period around the sun
  fetched today, correct."
- **Centres chosen** (`data/objects_export.json` at 9579fcd): around
  the Sun, Venus, Earth, Mars and Apophis; around the barycentre,
  Saturn, Uranus, Neptune and Halley.
- **Loose ends, re-homed at the close:** Earth's period prints 366 days,
  the period of Earth's centre: L-{H} (Earth's period), Tony's ruling
  of 2026-10-15. The look at the website, which waits for the gallery's
  Daily Run (its run of 10:38 came before the push at 10:57): L-{H}'s
  Gap.
**Gap:** none. Closed 2026-10-15.
"""

NEW_ITEM = """#### [L-{H}] Earth's orbital period from the Earth-Moon barycentre, not Earth's centre (orrery + website, periods)
<!-- L:{H} status:OPEN upd:2026-10-15 section:A flag: rice: -->
- **Found 2026-10-15, on L-444's first live run.** JPL's period for
  Earth's centre (Horizons 399, around the Sun) at 2026-10-15 10:52 is
  365.5364560333389 days. The two-centre test measured its change in a
  year at 0.769 days around the Sun and 1.76 days around the
  barycentre, so it prints to three figures: 366 days
  (`data/objects_export.json` and `data/osculating_cache.json` at
  9579fcd).
- **Why, Claude's reading, not a source:** the Earth and the Moon
  circle their common centre once a month, so Earth's centre wobbles.
  Its speed changes a little, and the period worked out from its
  position and speed swings by about half a day either way through the
  month. The Earth-Moon barycentre (Horizons 3) makes no such loop, so
  its period should stay close to the familiar year. The build confirms
  this against JPL's PR for target 3 before relying on it.
- **Tony's ruling, 2026-10-15:** "Confirmed as recommended, the
  barycenter." Earth's period is taken for the Earth-Moon barycentre,
  and the hover says so.
- **Where it reaches,** to map in the build, not decided here: the
  period record (`orbital_period.build_period_record`, which
  `fetch_osculating_elements` calls, so plotting and `period_fetch.py`
  keep agreeing); the Horizons check's period comparison, which must
  ask the same target; the export's period block and its words; the
  website's Earth hover, through the mirror. Earth's identity and
  position stay Earth's centre (399).
- **Received from L-444 at its close:** the look at the website. The
  gallery's Daily Run builds the cache before it pulls the orrery's
  export, so the eight periods' words reach the website on its first
  run after 9579fcd, and the orbits drawn around the barycentre
  (Saturn, Uranus, Neptune) on the run after that. L-{H2} (the daily
  run's order) would make that one run.
**Gap:** a small build, its own session: the target for Earth's period,
the check asking the same target, the hover's words, a planted fault
(Earth's period taken for 399 again) and a live run; then the website
look above.
**Ref:** L-444; L-431; `orbital_period.py`; `period_fetch.py`;
`horizons_check.py`; `export_objects.py`; `osculating_cache_manager.py`;
skills/horizons-orbital-mechanics/SKILL.md, A Period Depends on Its
Centre.

"""

ORDER_ITEM = """#### [L-{H2}] The website's Daily Run pulls the orrery's exports before it builds the cache (gallery, daily run)
<!-- L:{H2} status:OPEN upd:2026-10-15 section:A flag: rice: -->
- **Tony's question, 2026-10-15, after L-444's first live run:** "Wait,
  shouldn't the horizons check come before the cache build?"
- **What is there** (gallery `daily_run.py` at 9f8569e): STEPS run the
  guest book, then the cache builder, then the gallery maintenance run,
  whose generators pull the orrery's constants export and copy it into
  `data/objects_config.json`, pull its objects export and copy it in,
  and pull its drawings. So each cache build reads what the PREVIOUS
  day's pull brought. On the orrery side the order is already right: the
  Horizons check runs in the orrery's maintenance run, before the
  export, so everything the website pulls was checked. Tony placed the
  check before the cache build on 2026-10-07 (`daily_run.py`'s own
  notes); the Daily Run lost that order when the check moved into the
  orrery on 2026-10-14 (L-431 build 3) and its result began to arrive
  through the pull.
- **Ruled, 2026-10-15, on Claude's recommendation; Tony: "Yes."** The
  pulls, each with its copy step, run before the cache builder, so one
  Daily Run carries checked data straight into the build.
**Gap:** a small gallery build, its own session: the pulls and copies
ahead of the builder; whether the maintenance run keeps its own pull
rows (a no-op on a second run) or loses them; the Daily Run's dashboard
group, which Dashboard Parity holds; and one Daily Run showing new
periods reaching the website and the orbits drawn around the barycentre
in a single run.
**Ref:** gallery `daily_run.py`, `gallery_maintenance_run.py`,
`tools/pull_objects_export.py`, `tools/mirror_objects.py`,
`tools/pull_constants_export.py`, `tools/mirror_constants.py`,
`tools/pull_drawings.py`, `tools/gallery_cache_builder.py`; L-444;
L-{H}; L-431; L-395; skills/gallery-cache-builder/SKILL.md, The Daily
Run's Steps.

"""

L444_HEADER = ("#### [L-444] The maintenance run fetches a served body's "
               "missing period from JPL")

STAMP_ANCHOR = "Review and RICE update Tony 6-21-2026\n"
STAMP_NEW = ("Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5\n"
             "(L-444 closed on Tony's first live run, pushed at 9579fcd; L-{H}\n"
             "opened, Earth's period from the Earth-Moon barycentre; L-{H2} opened,\n"
             "the Daily Run pulls before it builds), built on 9579fcd5.\n" + STAMP_ANCHOR)

# ------------------------------------------------------------------ page

WWA_EDITS = [
    ("header",
     """Last updated: October 15, 2026: L-444 (the missing periods) built.
- Written at orrery ffd6c36 and gallery 86ef2df.
""",
     """Last updated: October 15, 2026, afternoon: L-444 (the missing periods) done.
- Written at orrery 9579fcd and gallery 9f8569e.
"""),
    ("changed since you last read this",
     """> - Built: L-444 (the missing periods). A new first step of the
>   maintenance run fetches from JPL each served body's missing
>   period, the orbit and the period together (your option A).
> - The order after it: Earth, then the Sun, then the objects (your
>   ruling, Oct 15).
""",
     """> - Done: L-444 (the missing periods): all eight fetched and confirmed.
> - Ruled: Earth's period from the Earth-Moon barycentre: L-{H}.
> - Ruled: the website's daily run pulls before it builds: L-{H2}.
"""),
    ("do next",
     """> **Do next:** *Run L-444's patch and the maintenance run. Then finish
> Earth's list, then the Sun's; the objects come after (your ruling, Oct 15).*""",
     """> **Do next:** *Build L-{H} (Earth's period). Then finish Earth's
> list, then the Sun's; the objects come after (your ruling, Oct 15).*"""),
    ("needs you now",
     """> - *Run patch_L444_missing_periods, then the maintenance run (the
>   first live fetch); reinstall horizons-orbital-mechanics 1.7; push.*
""",
     """> - *Run patch_L444_2_close, then the maintenance run; commit; push.*
"""),
    ("road 8a done, 8b new",
     """  8a.  [NOW]   *L-444 (the missing periods), built Oct 15: your first run
               fetches Venus, Earth, Mars, Saturn, Uranus, Neptune,
               Apophis and Halley from JPL.*  << moved this session
""",
     """  8a.  [done]  The run fetches each served body's missing period from
               JPL: L-444 (the missing periods), all eight, Oct 15.
  8b.  [next]  *L-{H} (Earth's period): from the Earth-Moon barycentre,
               not Earth's centre.*  << new this session
  8c.  [next]  L-{H2} (the daily run's order): the website pulls the
               orrery's checked data before it builds.  << new this session
"""),
    ("signals: last cache build",
     """- Last cache build: 20261014T225537Z, ok, no retry (gallery 86ef2df).
""",
     """- Last cache build: 20261015T153610Z, ok, no retry (gallery 9f8569e).
"""),
    ("signals: Tier-1",
     """- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 2b0e54c).
""",
     """- Tier-1 on the gate path: 0, by name (PROVENANCE_AUDIT.md, 9579fcd).
"""),
    ("details: next",
     """- *Next: L-413 (Earth's list), after your first live period fetch*""",
     """- *Next: L-{H} (Earth's period) in the ledger*"""),
]

# ------------------------------------------------------------------ handoff

HANDOFF_EDITS = [
    ("pushed at",
     "Pushed at: (Tony's commit after his run).\n",
     "Pushed at: 9579fcd577706b2eec8a9e552949331074f4e45b (Tony's commit\n"
     "after his run, 2026-10-15 10:57).\n"),
    ("the close",
     "Session record written October 2026 with Anthropic's Claude Opus 5.5.\n",
     """## 6. Tony's run, and the close (added 2026-10-15)

- The patch applied on 7166648d. The first live run fetched all eight,
  Venus, Earth, Mars, Saturn, Uranus, Neptune, Apophis and Halley, and
  the Horizons check confirmed each against JPL: 31 of 31 gating
  checkers, pushed at 9579fcd. Venus's hover in the orrery: "orbital
  period around the sun fetched today, correct."
- Tony asked whether the Horizons check should come before the cache
  build. It does in the orrery; the website's Daily Run builds before
  it pulls. Opened as L-{H2} (the daily run's order), with his "Yes".
- Earth printed 366 days: the period of Earth's centre, which the Moon
  makes wobble through the month. Tony's ruling the same day: take
  Earth's period from the Earth-Moon barycentre. Opened as L-{H}
  (Earth's period), which also carries the look at the website.
- L-444 closed by `patch_L444_2_close_20261015.py`.

Session record written October 2026 with Anthropic's Claude Opus 5.5.
"""),
]


def next_handle(ledger):
    nums = [int(n) for n in re.findall(r"\bL-(\d{3,4})\b", ledger)]
    return max(nums) + 1


def main():
    log = []
    notes = []
    try:
        led, led_crlf = read(LEDGER)
        if L444_META_NEW in led:
            raise PatchError("L-444 is already closed; this patch has run")
        h = next_handle(led)
        H, H2 = "%d" % h, "%d" % (h + 1)
        for x in (H, H2):
            if ("#### [L-%s]" % x) in led:
                raise PatchError("L-%s already exists" % x)
        led = rep(led, L444_META_OLD, L444_META_NEW, "L-444 to DONE", log, LEDGER)
        led = rep(led, L444_TAIL_OLD, L444_TAIL_NEW.replace("{H2}", H2).replace("{H}", H),
                  "L-444 run recorded, loose ends re-homed", log, LEDGER)
        if led.count(L444_HEADER) != 1:
            raise PatchError("ANCHOR FAIL [%s L-444 header]" % LEDGER)
        i = led.index(L444_HEADER)
        led = (led[:i] + NEW_ITEM.replace("{H2}", H2).replace("{H}", H)
               + ORDER_ITEM.replace("{H2}", H2).replace("{H}", H) + led[i:])
        log.append("ok  %-58s %s" % (LEDGER, "L-%s opened, Earth's period" % H))
        log.append("ok  %-58s %s" % (LEDGER, "L-%s opened, the daily run's order" % H2))
        led = rep(led, STAMP_ANCHOR, STAMP_NEW.replace("{H2}", H2).replace("{H}", H),
                  "header stamp", log, LEDGER)

        wwa, wwa_crlf = read(WWA)
        if wwa.count(MARKER) != 1:
            raise PatchError("ANCHOR FAIL [%s run-record marker]" % WWA)
        cut = wwa.index(MARKER)
        top, bottom = wwa[:cut], wwa[cut:]
        for label, old, new in WWA_EDITS:
            top = rep(top, old, new.replace("{H2}", H2).replace("{H}", H), label, log, WWA)
        above = top.count("\n")
        if above > WWA_CAP:
            raise PatchError("%s would stand %d lines above the marker (cap %d)"
                             % (WWA, above, WWA_CAP))
        log.append("ok  %s: %d lines above the marker (cap %d)"
                   % (WWA, above, WWA_CAP))
        wwa = top + bottom

        ho, ho_crlf = read(HANDOFF)
        for label, old, new in HANDOFF_EDITS:
            ho = rep(ho, old, new.replace("{H2}", H2).replace("{H}", H), label, log, HANDOFF)

        out = {LEDGER: (led, led_crlf), WWA: (wwa, wwa_crlf),
               HANDOFF: (ho, ho_crlf)}
        for rel, (text, _c) in out.items():
            bad = sum(1 for ch in text if ord(ch) > 127)
            if bad:
                raise PatchError("%s: %d non-ASCII character(s) after the "
                                 "edits" % (rel, bad))
    except PatchError as exc:
        print("ERROR: %s" % exc)
        print("NOTHING was written.")
        sys.exit(1)

    for rel, (text, crlf) in out.items():
        with open(os.path.join(ROOT, rel), "wb") as handle:
            handle.write(text.encode("utf-8"))
        if crlf:
            notes.append("note: %s was CRLF in the working copy; written LF"
                         % rel)
    for line in log:
        print(line)
    for line in notes:
        print(line)
    print("stamps updated: the ledger's header; Where We Are's date; the "
          "build record's push line")
    print("")
    print("New items: L-%s (Earth's period) and L-%s (the daily run's "
          "order)." % (H, H2))
    print("patch applied (3 files)")
    print("")
    print("NEXT:")
    print("  1. Run orrery_maintenance_run.py. Its ledger index moves L-444")
    print("     to the closed section and lists L-%s and L-%s." % (H, H2))
    print("  2. Move this script into documentation/; commit and push.")
    print("Undo is Discard Changes in GitHub Desktop.")


if __name__ == "__main__":
    main()
