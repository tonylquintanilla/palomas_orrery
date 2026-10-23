"""
period_fetch.py -- fetch from JPL the orbital period of each object the
website serves that has none fetched yet, with the same code the orrery
uses when Tony plots, so the Horizons check can compare it with JPL the
same day and the objects export can carry it to the website (L-444).

WHY IT EXISTS

    A period record is written only when an orbit is fetched, and until
    this step an orbit was fetched only when Tony plotted the body and
    said yes to the "Update Orbital Elements?" dialog. So eight served
    bodies printed a typed period, marked, until plotted: Venus, Earth,
    Mars, Saturn, Uranus, Neptune, Apophis and Halley, and a new keyed
    object would have its identity checked and its period never. Tony's
    question, 2026-10-14: "should the 30-day Horizons checker initiate a
    fetch of the missing data as well as report, including a new object
    as never having been fetched?" Ruled the same day, on Claude's
    recommendation ("yes"): a separate step before the check, which stays
    a check and fills no gaps itself. The brief is
    documentation/HANDOFF_L444_missing_periods_brief_20261014.md.

WHAT IT ASKS, AND WHEN

    Only what is missing, so on most runs it asks JPL nothing. The set is
    every entry of celestial_objects.py carrying a 'key' (the objects the
    website serves) whose period, read through export_objects.period_block
    exactly as the Horizons check and the export read it, is not "fetched"
    -- a typed period, none, or no cache entry at all, which is how a new
    object looks the first time this runs -- or whose fetched period was
    asked of another body than orbital_period.period_target now names
    (L-445): "period asked of 399, now 3" is how Earth looks the first
    time this runs after its period moved to the Earth-Moon barycentre,
    and how any later change of target reaches the website without
    anyone plotting. It prints that set by name, with why, before asking
    anything.

    Two kinds of served object are named and not fetched, for the reason
    plotting does not fetch them either:
      - the Sun, which orbits nothing here (the export carries no period);
      - an object plotting's pre-fetch never asks elements for: an
        object_type outside PLOTTED_TYPES, a mission, or a name in
        SKIP_NAMES. Today that is the Pluto-Charon barycentre, which L-443
        carries. Both lists copy palomas_orrery.py's pre-fetch filter, and
        test_period_fetch.py fails, naming the difference, the day the two
        disagree.

THE FETCH IS PLOTTING'S

    For each missing body, the call get_elements_with_prompt makes when
    Tony says yes, without the dialog (Tony's option A, 2026-10-15: the
    elements and the period together, so the drawn orbit and the period
    describe one fetch at one date):
        osculating_cache_manager.fetch_osculating_elements(
            name, horizons_id=<id>, id_type=<id_type>, date=<now>,
            center_body=None, with_period=True)
    then saved as plotting saves it, under get_cache_key(name, None) with
    save_cache. The arguments are the ones palomas_orrery.py's pre-fetch
    passes for a Sun-centred view: the entry's 'id', its 'id_type' with
    'smallbody' when the entry writes none (a None written out stays
    None, as for the planets), or its 'helio_id' as a small body where it
    has one (L-443), no centre override. So a period fetched
    here is the record plotting would write. Each body whose elements
    were already cached is named as refreshed.

    One difference from plotting, on failure only: plotting saves the
    elements even when the period query failed; this step saves nothing
    for a body unless its period came back, so the cache moves only on a
    whole answer and the body stays missing, to be asked again next run.
    A period that comes back asked of the old target is the last one,
    kept because the new query failed, and counts as not come back
    (L-445).

    After each save the cache is read back through export_objects and the
    body must now read "fetched", asked of the target the map names, or
    the run fails naming it: the success line carries its evidence.

WHAT MAKES IT FAIL

    Any failure to get JPL's answer -- no network, a refused query, an
    answer with no period -- is "could not reach JPL": nothing is saved
    for that body, it stays missing, and nothing more is asked today. The
    verdict says UNREACHABLE, by name, the convention for every row that
    needs the network, and names what was fetched before it and what is
    still missing. A save that does not read back as fetched is FAIL. The
    list failing to parse is FAIL. Exit 1 for any of these; 0 for PASS and
    NOTHING MISSING.

WHAT IT PRINTS

    The bodies examined; the set, by name, with why each is missing; the
    ones skipped, by name, with why; one line per body fetched, with its
    period, its centre and whether its elements were refreshed; then one
    verdict line starting "PERIOD FETCH:" -- PASS naming each body
    fetched, NOTHING MISSING, UNREACHABLE or FAIL.

WHAT IT WRITES

    data/osculating_cache.json only, through save_cache, which keeps its
    own two backups (ignored by git). Git is the backup.

RUN COMMAND

    python period_fetch.py

    Open it in VS Code and click Run. It takes no arguments. The orrery's
    maintenance run runs it as a generator just before the Horizons
    check. It needs the internet only on a day something is missing. Its
    offline tests are test_period_fetch.py, on the answers recorded in
    documentation/worksheets/period_fetch_answers_L444.json.

Role: devtool
Domain: dev_tools

Module created: October 15, 2026 with Anthropic's Claude Opus 5.5
(L-444, the missing periods).
Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-445,
Earth's period: a fetched period asked of another target than the map
now names is missing too, named with the reason, and the read-back
requires the new target.)
Module updated: October 22, 2026 with Anthropic's Claude Opus 5.5 (L-443:
an entry with a helio_id is fetched by it, as a small body, as plotting's
pre-fetch now does around the Sun and as the export serves it.)
"""

import ast
import datetime
import os
import sys

import export_objects

LINE = "=" * 70

# palomas_orrery.py's pre-fetch filter, at both sites (the static plot and
# the animation): the object types it asks elements for, and the names it
# never asks. Copied, and held to the source by test_period_fetch.py.
PLOTTED_TYPES = ("orbital", "satellite", "trajectory", "lagrange_point")
SKIP_NAMES = ("MK2", "Xiangliu", "Vanth", "Gonggong")

READ_FIELDS = ("name", "key", "id", "id_type", "object_type", "is_mission",
               "helio_id", "helio_id_type")


class ListError(Exception):
    """The object list could not be read."""


# ------------------------------------------------------------- the set

def served_entries(root):
    """[entry] for each keyed entry of celestial_objects.py, in list order.
    Each entry: name, key, horizons_id, id_type (as plotting reads it),
    object_type, is_mission. Raises ListError."""
    path = os.path.join(root, export_objects.SOURCE)
    try:
        with open(path, "rb") as handle:
            text = handle.read().decode("utf-8").replace("\r\n", "\n")
        # The export's own checks first, so a list it would refuse is
        # refused here too.
        export_objects.build_objects(text)
        list_node = export_objects.definitions(text)
    except (OSError, export_objects.ExportError) as exc:
        raise ListError(str(exc))
    out = []
    for node in list_node.elts:
        fields = {}
        for k, v in zip(node.keys, node.values):
            if isinstance(k, ast.Constant) and k.value in READ_FIELDS:
                try:
                    fields[k.value] = ast.literal_eval(v)
                except ValueError:
                    fields[k.value] = None
        if "key" not in fields:
            continue
        name = fields.get("name")
        # palomas_orrery.py: obj_dict.get('id', obj_name) and
        # obj_dict.get('id_type', 'smallbody'); around the Sun, the
        # helio_id where the entry has one, as a small body (L-443), the
        # record the export serves (export_objects.served_identity)
        horizons_id = str(fields.get("id", name))
        id_type = fields.get("id_type", "smallbody")
        if fields.get("helio_id") is not None:
            horizons_id = str(fields["helio_id"])
            id_type = fields.get("helio_id_type") or "smallbody"
        out.append({
            "name": name,
            "key": fields["key"],
            "horizons_id": horizons_id,
            "id_type": id_type,
            "object_type": fields.get("object_type"),
            "is_mission": bool(fields.get("is_mission", False)),
        })
    return out


def plotting_skips(entry):
    """Why plotting's pre-fetch would not fetch this entry, or None."""
    if entry["name"] in SKIP_NAMES:
        return "on plotting's skip list"
    if entry["object_type"] not in PLOTTED_TYPES:
        return ("plotting fetches no elements for object_type '%s'"
                % entry["object_type"])
    if entry["is_mission"]:
        return "plotting fetches no elements for a mission"
    return None


def wanted_target(entry, cache):
    """The id this entry's period should be asked of now, by
    orbital_period's one map, around the centre its elements are fetched
    around (L-445): Earth's, around the Sun, is '3'."""
    import orbital_period
    meta = ((cache.get(entry["name"]) or {}).get("metadata") or {}
            if isinstance(cache, dict) else {})
    return orbital_period.period_target(entry["horizons_id"],
                                        meta.get("center_body", "@sun"))


def classify(entries, cache, typed):
    """(missing, have, skipped): missing is [(entry, why)], have is
    [entry], skipped is [(entry, why)]."""
    missing, have, skipped = [], [], []
    for entry in entries:
        block, _inputs = export_objects.period_block(
            entry["name"], entry["object_type"], cache, typed)
        if block is None:
            skipped.append((entry, "orbits nothing here, so no period"))
            continue
        want = wanted_target(entry, cache)
        if block.get("kind") == "fetched" and block.get("target") != want:
            # L-445: fetched, but asked of another body than the map now
            # names, so it is re-fetched as missing.
            missing.append((entry, "period asked of %s, now %s"
                            % (block.get("target"), want)))
            continue
        if block.get("kind") == "fetched":
            have.append(entry)
            continue
        why = plotting_skips(entry)
        if why:
            skipped.append((entry, why))
            continue
        cached = entry["name"] in cache
        if not cached:
            reason = "no cache entry yet"
        elif block.get("kind") == "typed":
            reason = "typed period, not fetched from JPL"
        else:
            reason = "no period fetched from JPL"
        missing.append((entry, reason))
    return missing, have, skipped


# ------------------------------------------------------------- the fetch

def plotting_fetch(entry, when):
    """The cache entry plotting's yes-answer fetches, or None. Never
    raises: fetch_osculating_elements catches its own failures."""
    import osculating_cache_manager as ocm
    return ocm.fetch_osculating_elements(
        entry["name"],
        horizons_id=entry["horizons_id"],
        id_type=entry["id_type"],
        date=when,
        center_body=None,
        with_period=True,
    )


def plotting_save(entry, fetched):
    """Saved as get_elements_with_prompt saves it."""
    import osculating_cache_manager as ocm
    cache = ocm.load_cache()
    cache[ocm.get_cache_key(entry["name"], None)] = fetched
    ocm.save_cache(cache)


def fetched_target(fetched, horizons_id):
    """The id a fetched entry's period was asked of (L-445)."""
    import orbital_period
    return orbital_period.record_target(
        fetched.get("period"),
        (fetched.get("metadata") or {}).get("horizons_id", horizons_id))


def complete(fetched):
    """True when the fetch returned the elements and a period record with
    a centre and days, the parts the export refuses to go without."""
    if not isinstance(fetched, dict):
        return False
    period = fetched.get("period")
    return (isinstance(fetched.get("elements"), dict)
            and isinstance(period, dict)
            and bool(period.get("center")) and "days" in period)


def _period_words(block):
    days = (block or {}).get("days") or {}
    if (block or {}).get("open_orbit"):
        return "an open orbit (JPL gives no period)"
    whose = ("%s's period, " % block["target_label"]
             if block.get("target_label") else "")
    return "%s%s d around %s" % (whose, days.get("text"),
                                 block.get("center_label"))


# ------------------------------------------------------------- the run

def run(root, when, fetch=plotting_fetch, save=plotting_save, echo=print):
    """The whole step. Returns (exit code, summary dict)."""
    echo(LINE)
    echo("  PERIOD FETCH -- %s" % when.strftime("%Y-%m-%d"))
    echo(LINE)
    try:
        entries = served_entries(root)
        cache, typed, _c, _r = export_objects.load_inputs(root)
    except (ListError, export_objects.ExportError) as exc:
        echo("FAIL: the object list or the orbit cache could not be read: %s"
             % exc)
        echo("PERIOD FETCH: FAIL -- the inputs could not be read")
        return 1, {"verdict": "FAIL", "fetched": [], "missing": []}

    missing, have, skipped = classify(entries, cache, typed)
    echo("Read %s and %s through export_objects.py: %d served objects."
         % (export_objects.SOURCE, export_objects.CACHE.replace(os.sep, "/"),
            len(entries)))
    echo("Already fetched from JPL (%d): %s"
         % (len(have), ", ".join(e["name"] for e in have) or "none"))
    for entry, why in skipped:
        echo("Not fetched here: %s -- %s" % (entry["name"], why))
    if not missing:
        echo("Missing a fetched period (0): none")
        echo("")
        echo("PERIOD FETCH: NOTHING MISSING -- %d served objects examined, "
             "no query asked" % len(entries))
        return 0, {"verdict": "NOTHING MISSING", "fetched": [],
                   "missing": [], "asked": []}
    echo("Missing a fetched period (%d), asked in this order:" % len(missing))
    for entry, why in missing:
        echo("  %-24s %s" % (entry["name"], why))
    echo("")

    fetched, refreshed, new, asked = [], [], [], []
    down = None
    problems = []
    for entry, why in missing:
        name = entry["name"]
        if down is not None:
            continue
        asked.append(name)
        echo("-- %s (%s, id_type %s) --" % (name, entry["horizons_id"],
                                           entry["id_type"]))
        try:
            got = fetch(entry, when)
        except Exception as exc:          # any failure is JPL not reached
            echo("  could not reach JPL: %s" % exc)
            got = None
        if complete(got) and fetched_target(
                got, entry["horizons_id"]) != wanted_target(entry, cache):
            # L-445: the period query failed and the fetch kept the last
            # period, asked of the old target. Not a new answer.
            echo("  %s: the period came back asked of %s, the last one "
                 "kept" % (name, fetched_target(
                     got, entry["horizons_id"])))
            got = {"elements": got.get("elements")}
        if not complete(got):
            part = ("its elements" if not isinstance(got, dict)
                    else "its period")
            echo("  %s: could not reach JPL for %s; nothing saved, still "
                 "missing" % (name, part))
            down = name
            continue
        try:
            save(entry, got)
            cache_now, typed_now, _c, _r = export_objects.load_inputs(root)
            block, _i = export_objects.period_block(
                name, entry["object_type"], cache_now, typed_now)
        except Exception as exc:
            problems.append("%s: saved but could not be read back (%s)"
                            % (name, exc))
            echo("  FAIL: %s" % problems[-1])
            continue
        if not block or block.get("kind") != "fetched":
            problems.append("%s: saved but reads back as %s, not fetched"
                            % (name, (block or {}).get("kind")))
            echo("  FAIL: %s" % problems[-1])
            continue
        if block.get("target") != wanted_target(entry, cache_now):
            problems.append("%s: saved but its period reads back as asked "
                            "of %s, not %s" % (name, block.get("target"),
                                               wanted_target(entry,
                                                             cache_now)))
            echo("  FAIL: %s" % problems[-1])
            continue
        fetched.append(name)
        if name in cache:
            refreshed.append(name)
            elements = "elements refreshed (were %s)" % (
                (cache.get(name) or {}).get("elements") or {}).get("epoch")
        else:
            new.append(name)
            elements = "new cache entry"
        echo("  %s: fetched, %s; %s; read back as fetched"
             % (name, _period_words(block), elements))

    still = [e["name"] for e, _w in missing if e["name"] not in fetched]
    unasked = [e["name"] for e, _w in missing if e["name"] not in asked]
    echo("")
    if down is not None:
        verdict = "UNREACHABLE"
        line = ("PERIOD FETCH: UNREACHABLE -- JPL could not be reached for "
                "%s; still missing: %s" % (down, ", ".join(still)))
        if unasked:
            line += "; not asked today: %s" % ", ".join(unasked)
        if fetched:
            line += "; fetched before it: %s" % ", ".join(fetched)
        if problems:
            line += "; also FAILED: %s" % "; ".join(problems)
    elif problems:
        verdict = "FAIL"
        line = "PERIOD FETCH: FAIL -- %s" % "; ".join(problems)
    else:
        verdict = "PASS"
        line = "PERIOD FETCH: PASS -- fetched %d: %s" % (
            len(fetched), ", ".join(fetched))
        if refreshed:
            line += "; elements refreshed for: %s" % ", ".join(refreshed)
        if new:
            line += "; new cache entries: %s" % ", ".join(new)
    echo(line)
    return (0 if verdict == "PASS" else 1), {
        "verdict": verdict, "fetched": fetched, "refreshed": refreshed,
        "new": new, "missing": [e["name"] for e, _w in missing],
        "still": still, "asked": asked, "problems": problems}


def main(argv):
    root = os.path.dirname(os.path.abspath(__file__))
    code, _ = run(root, datetime.datetime.now())
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
