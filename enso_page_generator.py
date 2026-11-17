"""
enso_page_generator.py - El Nino's page on the website: NOAA's record since 1950 and what NOAA expects next, a walk in five steps (L-060).

Dedicated generator for the Earth System family, like
food_insecurity_generator.py: it imports no scalar engine. Its one source of
record is NOAA's Climate Prediction Center (CPC). At every build it reads
NOAA's files FRESH (never through a cache), saves a dated copy of each in
data/earth/noaa_enso_reads/<date>/, and parses them:

    - the RONI data file (NOAA's Relative Oceanic Nino Index, 1950 to the
      newest three-month season);
    - the ENSO probabilities page (NOAA's chances of El Nino, neutral and
      La Nina, season by season);
    - the ENSO diagnostic discussion (the ENSO Alert System status, the
      date it was issued, the date the next one is expected, and the
      sentence giving the chance of a "historic event").

Every figure the page states is computed from those files at build time:
the newest season and its value, the record and its season, whether it has
been passed, and the three strongest El Nino events. A file that does not
read as expected stops the build with a line naming what was missing; the
build never guesses and never falls back to another source (Tony's ruling
of Nov 16, 2026: if CPC stopped, a new source of record is his decision).

The Run button builds the page and its five pictures (earth/el_nino.html,
earth/el_nino_<step>.png) into data/earth/, copies those six files to the
website folder beside the orrery, and writes data/earth/el_nino_state.json,
what the page shows. With --night-check it is the night run's row
(orrery_maintenance_run.py --night): it reads NOAA fresh, compares with
that state, and when NOAA has anything newer saves the dated copies and
says EL NINO DUE, which the nightly commit title carries. The night never
changes the page; Tony rebuilds it by hand (his ruling of Nov 17, 2026).

The two safeguards (L-060, Nov 16): the page always shows the date of
NOAA's latest update, and a few lines of script on the page say it has
not caught up with NOAA once the "Next expected" date has passed; every
build keeps a copy of the NOAA files it read, so the record survives if a
feed ends.

Key functions:
    fetch_noaa() - read the three files fresh, save the dated copies.
    parse_roni() / parse_probabilities() / parse_discussion() - read them.
    roni_events() - El Nino and La Nina episodes by NOAA's rule.
    compute_figures() - every figure the page states, from the data.
    run_data() - all of the above, with the cross-file checks; returns a
        dict the page builder reads.
    picture_*() / page_steps() / build_page_html() - the five pictures,
        the words, the page.
    run() - the whole build: data, page, pictures, state, the copy.
    night_check() - the night row: compare NOAA with the page, flag.

Consumed by: orrery_maintenance_run.py, the row "El Nino check"
(--night-check, in the night set) and its suite test_enso_night_check.py;
runnable standalone via __main__ (the Run button builds the page and
prints every sentence with its source).

Role: devtool
Domain: earth_science

Module updated: November 2026 with Anthropic's Claude Opus 5.5
"""
import os
import re
import sys
import html
import datetime
import urllib.request

DATA_DIR = "data"
PAGE_FOLDER = "earth"
SCENARIO_ID = "el_nino"
# The dated copies of NOAA's files live beside the page's own files, in a
# folder of their own, so they are kept in the orrery (data/earth/ is
# tracked) and are not part of what is copied to the website.
READS_FOLDER = "noaa_enso_reads"

# ==========================================================================
#   SOURCED CONSTANTS -- every URL and threshold carries a # Source: within
#   the provenance scanner's lookback. Read at build time; nothing recalled.
# ==========================================================================

# Source: NWS Public Information Statement 26-05 (13 Jan 2026), "The
# following is a text file of the RONI:" followed by this address --
# NOAA's own named file for the index.
# https://www.weather.gov/media/notification/pdf_2026/pns26-05_Relative_ONI.pdf
RONI_URL = "https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt"

# Source: NOAA CPC, "Official NOAA CPC ENSO Probabilities" (the page
# itself): "the percent chances in numerical form" for "9 upcoming,
# overlapping 3-month seasons"; "Updates on the 2nd Thursday of each month".
PROBABILITIES_URL = ("https://www.cpc.ncep.noaa.gov/products/"
                     "analysis_monitoring/enso/roni/probabilities/")

# Source: NOAA CPC, ENSO Diagnostic Discussion (the current one, at its
# standing address; each month's is archived under its own address).
DISCUSSION_URL = ("https://www.cpc.ncep.noaa.gov/products/"
                  "analysis_monitoring/enso_advisory/ensodisc.shtml")

# Source: NOAA CPC, "Relative Oceanic Nino Index (RONI): Historical El Nino /
# La Nina episodes (1950-Present)",
# https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/ :
# "Warm (red) and cold (blue) periods based on a threshold of +/- 0.5 C for
# the Relative Oceanic Nino Index (RONI)" ... "when the threshold is met for
# a minimum of five (5) consecutive overlapping seasons."
EPISODE_THRESHOLD_C = 0.5
EPISODE_MIN_SEASONS = 5
# Source: the same page's table of every season since 1950, which prints
# each value to one decimal and colours it red, blue or plain from that
# printed value (DJF 1988, 0.45 in the data file, is printed 0.5 and red).
# So the threshold is applied to the value rounded to one decimal. Read
# 2026-11-16: this build's episodes matched the page's colours in 920 of
# 921 seasons this way (52 differed on the file's two decimals). The one,
# MJJ 2024 (-0.45 in the file, printed -0.4 and plain on the page), is a
# tie the file cannot settle: of its 87 values ending in 5, NOAA's page
# rounds 39 away from zero and 48 toward it, so NOAA prints from values
# finer than the file's.
EPISODE_DECIMALS = 1

# Source: the RONI data file's own SEAS column, in the order its rows run
# within each year (DJF first, NDJ last). DJF of year Y is December Y-1 to
# February Y; NDJ of year Y is November Y to January Y+1, so the middle
# month of the season at position k is month k+1 of year Y.
SEASONS = ("DJF", "JFM", "FMA", "MAM", "AMJ", "MJJ",
           "JJA", "JAS", "ASO", "SON", "OND", "NDJ")

MONTH_NAMES = ("January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November",
               "December")

# A browser-like request, asking every cache between here and NOAA for a
# fresh copy. Generic on purpose: nothing about the project or its owner
# goes to an outside service.
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}
FETCH_TIMEOUT_S = 60


class EnsoBuildStop(Exception):
    """The build stops: a NOAA file did not read as expected. The message
    names what was missing, for the person who runs the build."""


# ==========================================================================
#   FETCH, FRESH, WITH A DATED COPY OF EACH FILE
# ==========================================================================

# The saved copies' file names, one per source.
READ_FILES = (
    ("roni", RONI_URL, "RONI.ascii.txt"),
    ("probabilities", PROBABILITIES_URL, "enso_probabilities.html"),
    ("discussion", DISCUSSION_URL, "ensodisc.html"),
)


def _get(url):
    """One fresh read. Returns (bytes, headers as a dict)."""
    req = urllib.request.Request(url, headers=REQUEST_HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT_S) as resp:
            body = resp.read()
            heads = {k.lower(): v for k, v in resp.headers.items()}
    except Exception as exc:
        raise EnsoBuildStop("Could not read NOAA's file %s (%s). The page "
                            "is not rebuilt without it." % (url, exc))
    if not body:
        raise EnsoBuildStop("NOAA's file %s came back empty." % url)
    return body, heads


def _reads_folder(day):
    return os.path.join(DATA_DIR, PAGE_FOLDER, READS_FOLDER, day.isoformat())


def fetch_noaa(today=None):
    """Read the three NOAA files fresh and save a dated copy of each, byte
    for byte, in data/earth/noaa_enso_reads/<YYYY-MM-DD>/. A second build on
    the same day overwrites that day's copy only if NOAA's bytes are the
    same; if they differ, the new copy is saved beside it with the time
    added, so no copy NOAA served is ever lost. Returns
    {key: {"bytes", "headers", "url", "saved"}}."""
    today = today or datetime.date.today()
    folder = _reads_folder(today)
    if not os.path.exists(folder):
        os.makedirs(folder)
    out = {}
    for key, url, fname in READ_FILES:
        body, heads = _get(url)
        path = os.path.join(folder, fname)
        if os.path.exists(path):
            with open(path, "rb") as f:
                same = f.read() == body
            if not same:
                stem, ext = os.path.splitext(fname)
                path = os.path.join(folder, "%s_%s%s" % (
                    stem, datetime.datetime.now().strftime("%H%M%S"), ext))
        with open(path, "wb") as f:
            f.write(body)
        out[key] = {"bytes": body, "headers": heads, "url": url,
                    "saved": path}
    return out


def _page_text(raw):
    """A NOAA page's words: windows-1252 bytes (as the pages declare),
    scripts and styles dropped, tags removed, entities decoded, white space
    folded to single spaces."""
    t = raw.decode("cp1252", errors="replace")
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = t.replace("\u00a0", " ")
    return re.sub(r"\s+", " ", t).strip()


def _parse_day(words, what):
    """'12 November 2026' -> date. Stops the build, naming WHAT, if not."""
    m = re.match(r"(\d{1,2}) ([A-Za-z]+) (\d{4})$", words.strip())
    if not m or m.group(2).capitalize() not in MONTH_NAMES:
        raise EnsoBuildStop("The discussion's %s does not read as a date: "
                            "%r." % (what, words))
    return datetime.date(int(m.group(3)),
                         MONTH_NAMES.index(m.group(2).capitalize()) + 1,
                         int(m.group(1)))


def season_words(season, year):
    """('ASO', 2026) -> 'August-October 2026'; ('DJF', 1983) ->
    'December-February 1982-83' (the season's own span of years)."""
    k = SEASONS.index(season)
    first = (k - 1) % 12          # first month of the season, 0-based
    last = (k + 1) % 12
    y_first = year - 1 if k == 0 else year
    y_last = year + 1 if k == 11 else year
    span = ("%d" % year if y_first == y_last
            else "%d-%02d" % (y_first, y_last % 100))
    return "%s-%s %s" % (MONTH_NAMES[first], MONTH_NAMES[last], span)


# ==========================================================================
#   PARSE: THE RONI FILE
# ==========================================================================

def parse_roni(raw):
    """The RONI file's rows as a list of {"season", "year", "value",
    "t"} in file order, t the middle month as a decimal year. Stops the
    build if the header is not NOAA's, a row does not read, or the seasons
    do not run one after another without a gap."""
    lines = raw.decode("ascii", errors="replace").splitlines()
    if not lines or lines[0].split() != ["SEAS", "YR", "ANOM"]:
        raise EnsoBuildStop("The RONI file's first line is not 'SEAS YR "
                            "ANOM': %r." % (lines[0] if lines else ""))
    rows = []
    for n, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != 3 or parts[0] not in SEASONS:
            raise EnsoBuildStop("The RONI file's line %d does not read as "
                                "a season, a year and a value: %r."
                                % (n, line))
        try:
            year = int(parts[1])
            value = float(parts[2])
        except ValueError:
            raise EnsoBuildStop("The RONI file's line %d does not read as "
                                "a season, a year and a value: %r."
                                % (n, line))
        k = SEASONS.index(parts[0])
        rows.append({"season": parts[0], "year": year, "value": value,
                     "t": year + k / 12.0, "k": k})
    if not rows:
        raise EnsoBuildStop("The RONI file holds no seasons.")
    for a, b in zip(rows, rows[1:]):
        nk = (a["k"] + 1) % 12
        ny = a["year"] + (1 if a["k"] == 11 else 0)
        if (b["k"], b["year"]) != (nk, ny):
            raise EnsoBuildStop("The RONI file skips from %s %d to %s %d."
                                % (a["season"], a["year"],
                                   b["season"], b["year"]))
    return rows


# ==========================================================================
#   PARSE: THE PROBABILITIES PAGE
# ==========================================================================

def parse_probabilities(raw):
    """NOAA's chances table: {"issued": 'November 2026', "seasons": [
    {"season", "la_nina", "neutral", "el_nino"}, ...]} in NOAA's order.
    Stops the build if the issue line or the table is missing, a row's
    three chances do not add to 100, or the number of seasons is not the
    number the page itself states."""
    t = raw.decode("cp1252", errors="replace")
    m = re.search(r"<h2>\s*Issued\s+([A-Za-z]+\s+\d{4})\s*</h2>", t)
    if not m:
        raise EnsoBuildStop("The probabilities page has no 'Issued <month> "
                            "<year>' line.")
    issued = m.group(1)
    tm = re.search(r'(?is)<table id="probabilities-table">(.*?)</table>', t)
    if not tm:
        raise EnsoBuildStop("The probabilities page has no table "
                            "'probabilities-table'.")
    table = tm.group(1)
    heads = [_page_text(h.encode("cp1252", errors="replace"))
             for h in re.findall(r'(?is)<th scope="col">(.*?)</th>', table)]
    want = ["Season", "La Ni\u00f1a", "Neutral", "El Ni\u00f1o"]
    if heads != want:
        raise EnsoBuildStop("The probabilities table's columns are %r, not "
                            "%r." % (heads, want))
    seasons = []
    for row in re.findall(r"(?is)<tr>(.*?)</tr>", table):
        sm = re.search(r"(?is)<abbr>\s*([A-Z]{3})\b", row)
        cells = re.findall(r"(?is)<td>\s*(\d+)\s*</td>", row)
        if not sm or len(cells) != 3:
            raise EnsoBuildStop("A row of the probabilities table does not "
                                "read: %r." % _page_text(
                                    row.encode("cp1252", errors="replace")))
        la, ne, el = (int(c) for c in cells)
        if la + ne + el != 100:
            raise EnsoBuildStop("NOAA's chances for %s add to %d, not 100."
                                % (sm.group(1), la + ne + el))
        if sm.group(1) not in SEASONS:
            raise EnsoBuildStop("The probabilities table names a season "
                                "%r." % sm.group(1))
        seasons.append({"season": sm.group(1), "la_nina": la,
                        "neutral": ne, "el_nino": el})
    words = _page_text(raw)
    cm = re.search(r"provided for (\d+) upcoming, overlapping 3-month "
                   r"seasons", words)
    if not cm:
        raise EnsoBuildStop("The probabilities page no longer says how many "
                            "seasons it gives ('provided for N upcoming, "
                            "overlapping 3-month seasons').")
    if int(cm.group(1)) != len(seasons):
        raise EnsoBuildStop("The probabilities page says %s seasons; its "
                            "table holds %d." % (cm.group(1), len(seasons)))
    for a, b in zip(seasons, seasons[1:]):
        if SEASONS.index(b["season"]) != (SEASONS.index(a["season"]) + 1) % 12:
            raise EnsoBuildStop("The probabilities table skips from %s to %s."
                                % (a["season"], b["season"]))
    return {"issued": issued, "seasons": seasons}


# ==========================================================================
#   PARSE: THE DISCUSSION
# ==========================================================================

def parse_discussion(raw):
    """The discussion's status, the day it was issued, the day the next is
    scheduled, and the "historic event" sentence as NOAA printed it, with
    its figure, threshold and seasons read out. Stops the build, naming the
    piece, if any one is missing."""
    words = _page_text(raw)
    m = re.search(r"CLIMATE PREDICTION CENTER/NCEP/NWS (\d{1,2} [A-Za-z]+ "
                  r"\d{4})", words)
    if not m:
        raise EnsoBuildStop("The discussion has no issue date after 'issued "
                            "by CLIMATE PREDICTION CENTER/NCEP/NWS'.")
    issued = _parse_day(m.group(1), "issue date")
    m = re.search(r"ENSO Alert System Status: (.+?) Synopsis:", words)
    if not m:
        raise EnsoBuildStop("The discussion has no 'ENSO Alert System "
                            "Status:' line before its Synopsis.")
    status = m.group(1).strip()
    m = re.search(r"The next ENSO Diagnostics Discussion is scheduled for "
                  r"(\d{1,2} [A-Za-z]+ \d{4})", words)
    if not m:
        raise EnsoBuildStop("The discussion does not say when the next one "
                            "is scheduled ('The next ENSO Diagnostics "
                            "Discussion is scheduled for ...').")
    next_day = _parse_day(m.group(1), "next scheduled date")
    # The "historic event" sentence: NOAA's chance, with NOAA's own
    # threshold, never stated as the chance of passing the record (L-060).
    hm = re.search(r"([^.]*\bhistoric event\b[^.]*(?:\.\d[^.]*)*\.)", words)
    if not hm:
        raise EnsoBuildStop("The discussion of %s has no sentence on a "
                            "'historic event'. Step 4's sentence on it is "
                            "not written without NOAA's words."
                            % issued.isoformat())
    # A tag inside the sentence leaves a space before its closing mark
    # ("RONI value )"); NOAA's page shows none.
    sentence = re.sub(r"\s+([).,;:])", r"\1", hm.group(1).strip())
    pm = re.search(r"~\s*(\d+)\s*%", sentence)
    th = re.search(r"\+(\d+\.\d+)\s*\u00b0?\s*C or more for a 3-month RONI "
                   r"value", sentence)
    per = re.search(r"for the ([A-Z][a-z]+-[A-Z][a-z]+) and "
                    r"([A-Z][a-z]+-[A-Z][a-z]+) periods", sentence)
    missing = [name for name, got in (("the chance (~N%)", pm),
                                      ("the threshold (+N.N C or more for a "
                                       "3-month RONI value)", th),
                                      ("the seasons ('for the A-B and C-D "
                                       "periods')", per)) if not got]
    if missing:
        raise EnsoBuildStop("The discussion's 'historic event' sentence no "
                            "longer reads as expected; missing %s. NOAA's "
                            "sentence: %r" % (", ".join(missing), sentence))
    return {
        "issued": issued,
        "status": status,
        "next": next_day,
        "historic_sentence": sentence,
        "historic_pct": int(pm.group(1)),
        "historic_threshold": float(th.group(1)),
        "historic_periods": [per.group(1), per.group(2)],
    }


# ==========================================================================
#   COMPUTE: EPISODES, THE RECORD, THE STRONGEST EVENTS
# ==========================================================================

def printed_value(value):
    """The value rounded to EPISODE_DECIMALS, as NOAA's episode table
    prints it (0.49 -> 0.5). A value ending in 5 is rounded the way Python
    prints it; NOAA's own rounding of those differs in places (see
    EPISODE_DECIMALS)."""
    return float("%.*f" % (EPISODE_DECIMALS, value))


def roni_events(rows, sign=+1):
    """El Nino (sign +1) or La Nina (sign -1) episodes by NOAA's rule: the
    index at or beyond +/-EPISODE_THRESHOLD_C for at least
    EPISODE_MIN_SEASONS overlapping seasons in a row. Each: {"first",
    "last" (row indices), "peak" (row index), "peak_value", "seasons",
    "ongoing", "qualified"}. A run still going at the file's last season
    is ongoing: its peak so far is not its final peak, and while it is
    shorter than EPISODE_MIN_SEASONS it is kept but not yet qualified
    (NOAA's rule is not met yet)."""
    events, start = [], None
    for i, r in enumerate(rows + [None]):
        hit = (r is not None and sign * printed_value(r["value"])
               >= EPISODE_THRESHOLD_C)
        if hit and start is None:
            start = i
        elif not hit and start is not None:
            n = i - start
            ongoing = i == len(rows)
            if n >= EPISODE_MIN_SEASONS or ongoing:
                seg = range(start, i)
                peak = max(seg, key=lambda j: sign * rows[j]["value"])
                events.append({"first": start, "last": i - 1, "peak": peak,
                               "peak_value": rows[peak]["value"],
                               "seasons": n, "ongoing": ongoing,
                               "qualified": n >= EPISODE_MIN_SEASONS})
            start = None
    return events


def season_classes(rows):
    """Each season's class by NOAA's rule, as NOAA's own table colours it:
    'el' in a qualified El Nino episode, 'la' in a qualified La Nina
    episode, 'neutral' otherwise (a run still short of five seasons is
    neutral until it qualifies)."""
    out = ["neutral"] * len(rows)
    for sign, cls in ((+1, "el"), (-1, "la")):
        for ev in roni_events(rows, sign):
            if ev["qualified"]:
                for i in range(ev["first"], ev["last"] + 1):
                    out[i] = cls
    return out


def event_label(rows, ev):
    """An event is named by the winter of its peak, as NOAA's discussions
    name them: the year of the December nearest the peak season's middle
    month, and the next ('1982-83', '1997-98', '2015-16')."""
    r = rows[ev["peak"]]
    middle_month = r["k"] + 1                  # 1..12
    dec_year = r["year"] if middle_month >= 7 else r["year"] - 1
    return "%d-%02d" % (dec_year, (dec_year + 1) % 100)


def compute_figures(rows):
    """Every figure the page states from the RONI file, computed."""
    newest = rows[-1]
    rec_i = max(range(len(rows)), key=lambda j: rows[j]["value"])
    rec = rows[rec_i]
    el = roni_events(rows, +1)
    la = roni_events(rows, -1)
    ranked = sorted(el, key=lambda ev: -ev["peak_value"])
    current = el[-1] if el and el[-1]["ongoing"] else None
    passed = current is not None and current["first"] <= rec_i
    strongest = [{"label": event_label(rows, ev),
                  "peak_value": ev["peak_value"],
                  "peak_season": rows[ev["peak"]]["season"],
                  "peak_year": rows[ev["peak"]]["year"],
                  "ongoing": ev["ongoing"]} for ev in ranked[:3]]
    rank_current = (ranked.index(current) + 1) if current else None
    return {
        "first": rows[0],
        "newest": newest,
        "newest_words": season_words(newest["season"], newest["year"]),
        "record": rec,
        "record_words": season_words(rec["season"], rec["year"]),
        "record_passed": passed,
        "el_nino_events": el,
        "la_nina_events": la,
        "strongest": strongest,
        "current_event": current,
        "current_rank": rank_current,
        "last_twelve": rows[-12:],
        "classes": season_classes(rows),
    }


def enso_status(disc, today=None):
    """The status line's figures, and the first safeguard: the page says
    so when the next discussion's date has passed and the build found no
    newer one."""
    today = today or datetime.date.today()
    return {"status": disc["status"], "issued": disc["issued"],
            "next": disc["next"], "overdue": today > disc["next"]}


def check_across_files(rows, probs, disc):
    """The three files must describe the same month. Stops the build if the
    RONI file is older than the discussion (the copy a cache served on Nov
    16 ended at JAS 2026 while NOAA's file held ASO 2026), or if the
    probabilities page was issued in another month than the discussion."""
    newest = rows[-1]
    last_month = (newest["k"] + 1) % 12 + 1          # 1..12
    last_year = newest["year"] + (1 if newest["k"] == 11 else 0)
    d = disc["issued"]
    month_before = (d.year, d.month - 1) if d.month > 1 else (d.year - 1, 12)
    if (last_year, last_month) < month_before:
        raise EnsoBuildStop(
            "The RONI file read ends at %s %d, older than NOAA's discussion "
            "of %s, which follows the season ending in %s %d. A cached "
            "copy may have been served; the page is not rebuilt from it."
            % (newest["season"], newest["year"], d.isoformat(),
               MONTH_NAMES[month_before[1] - 1], month_before[0]))
    want = "%s %d" % (MONTH_NAMES[d.month - 1], d.year)
    if probs["issued"] != want:
        raise EnsoBuildStop("The probabilities page was issued %s; the "
                            "discussion is of %s." % (probs["issued"], want))


def run_data(today=None):
    """Part 1, end to end: fetch fresh, save the dated copies, parse,
    check across the files, compute. Returns everything the page reads."""
    today = today or datetime.date.today()
    got = fetch_noaa(today)
    rows = parse_roni(got["roni"]["bytes"])
    probs = parse_probabilities(got["probabilities"]["bytes"])
    disc = parse_discussion(got["discussion"]["bytes"])
    check_across_files(rows, probs, disc)
    return {"reads": got, "rows": rows, "probabilities": probs,
            "discussion": disc, "status": enso_status(disc, today),
            "figures": compute_figures(rows), "built": today}


def report_data(data):
    """What the build read, by name, for the person who runs it."""
    f, s, p, d = (data["figures"], data["status"], data["probabilities"],
                  data["discussion"])
    out = []
    w = out.append
    w("NOAA files read fresh, %s; copies saved:" % data["built"])
    for key, _url, _f in READ_FILES:
        r = data["reads"][key]
        w("  %s  (%d bytes; NOAA's Last-Modified: %s)" % (
            r["saved"], len(r["bytes"]),
            r["headers"].get("last-modified", "not given")))
    w("")
    w("RONI: %d seasons, %s %d to %s %d." % (
        len(data["rows"]), f["first"]["season"], f["first"]["year"],
        f["newest"]["season"], f["newest"]["year"]))
    w("  Newest season: %s %d (%s), %+.2f C." % (
        f["newest"]["season"], f["newest"]["year"], f["newest_words"],
        f["newest"]["value"]))
    w("  Record: %+.2f C, %s %d (%s). Passed by the current event: %s." % (
        f["record"]["value"], f["record"]["season"], f["record"]["year"],
        f["record_words"], "yes" if f["record_passed"] else "no"))
    w("  El Nino episodes by NOAA's rule: %d; La Nina: %d." % (
        len(f["el_nino_events"]), len(f["la_nina_events"])))
    w("  The three strongest El Nino events:")
    for ev in f["strongest"]:
        w("    %s, peak %+.2f C in %s %d%s" % (
            ev["label"], ev["peak_value"], ev["peak_season"],
            ev["peak_year"], " (ongoing)" if ev["ongoing"] else ""))
    if f["current_event"]:
        ce = f["current_event"]
        rows = data["rows"]
        w("  Current El Nino: since %s %d, %d seasons at +0.5 or more "
          "(%s), peak so far %+.2f C, ranks %d of %d by peak." % (
              rows[ce["first"]]["season"], rows[ce["first"]]["year"],
              ce["seasons"],
              "meets NOAA's five-season rule" if ce["qualified"]
              else "short of NOAA's five-season rule so far",
              ce["peak_value"], f["current_rank"],
              len(f["el_nino_events"])))
    w("  Last twelve seasons: " + ", ".join(
        "%s %d %+.2f" % (r["season"], r["year"], r["value"])
        for r in f["last_twelve"]))
    w("")
    w("Chances, issued %s (La Nina / Neutral / El Nino, percent):" % p["issued"])
    for x in p["seasons"]:
        w("  %s  %3d / %3d / %3d" % (x["season"], x["la_nina"],
                                     x["neutral"], x["el_nino"]))
    w("")
    w("Status: %s" % s["status"])
    w("NOAA's latest update: %s" % s["issued"].isoformat())
    w("Next expected: %s%s" % (s["next"].isoformat(),
                               "  -- OVERDUE" if s["overdue"] else ""))
    w("Historic-event sentence, as NOAA printed it:")
    w("  " + d["historic_sentence"])
    w("  read out: ~%d%%, +%.1f C or more on RONI, for %s" % (
        d["historic_pct"], d["historic_threshold"],
        " and ".join(d["historic_periods"])))
    return "\n".join(out)


# ==========================================================================
#   PART 2: THE FIVE PICTURES
# ==========================================================================

# Characters the page and pictures need, named by number so the code stays
# ASCII (the brief's spelling rule: the tilde on the page, in the pictures,
# in the alt text and in the title).
N_TILDE = chr(0xF1)
EN_DASH = chr(0x2013)
MINUS = chr(0x2212)

# Colours and ink, from the mockup Tony chose (board A, Nov 16): a Mode-5
# visual choice, not a data claim. Red is warm water and El Nino, blue cool
# water and La Nina, as NOAA's own charts colour them.
RED = "#d9542b"
BLUE = "#2f6fbf"
INK = "#222222"
DIM = "#555555"
SEA = "#d6e6f4"
LAND = "#c9b98f"
PROVISIONAL_SHADE = "#e9dfc4"
NEUTRAL_GREY = "#9a9a9a"

# Source: NOAA CPC, RONI page (above): "Nino 3.4 region (5N-5S,
# 120-170W)"; in degrees east, 190 to 240.
NINO34_LON_E = (190.0, 240.0)
NINO34_LAT = (-5.0, 5.0)

PICTURE_WIDTH_IN = 10.0      # 1000 px at 100 dpi, as Sudan's pictures
PICTURE_DPI = 100
LABEL_PT = 20                # the smallest text: about 9 px on a phone


def tilde(s):
    """Words for a picture: 'Nino' -> 'Ni' + n-tilde + 'o'."""
    return (s.replace("Nino", "Ni" + N_TILDE + "o")
             .replace("Nina", "Ni" + N_TILDE + "a"))


def _plt():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    return plt


def _png(fig):
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="png", facecolor="white", dpi=PICTURE_DPI)
    _plt().close(fig)
    return buf.getvalue()


def _signed(v, places=2):
    """'+1.97' or a true minus sign: '-1.04' with U+2212."""
    s = "%+.*f" % (places, v)
    return s.replace("-", MINUS)


def picture_what():
    """Step 1: three simplified maps of the tropical Pacific, El Nino,
    neutral and La Nina, one above the other, each with the Nino 3.4 box
    and the trade winds as an arrow. Shapes from the mockup's reference
    file (documentation/MOCKUP_L060_el_nino_drawings_20261116.py)."""
    plt = _plt()
    from matplotlib.patches import Ellipse, Polygon, Rectangle
    fig = plt.figure(figsize=(PICTURE_WIDTH_IN, 14.4))
    lands = [
        [(120, 30), (134, 30), (130, 25), (122, 21), (120, 21)],
        [(120, 8), (127, 10), (126, 0), (141, -2), (150, -6), (141, -9),
         (130, -4), (120, -6)],
        [(120, -15), (131, -12), (142, -11), (146, -19), (153, -28),
         (151, -30), (120, -30)],
        [(253, 30), (255, 22), (265, 16), (275, 9), (280, 7), (280, 1),
         (279, -4), (282, -14), (289, -19), (290, -30), (311, -30),
         (311, 30)],
    ]
    # (centre lon, centre lat, half-width, half-height, colour, alpha)
    water = {
        "elnino": [(225, 0, 57, 7, RED, 0.75), (148, 0, 14, 6, RED, 0.35)],
        "neutral": [(150, 0, 28, 9, RED, 0.8), (262, -1, 23, 5, BLUE, 0.8)],
        "lanina": [(146, 0, 20, 10, RED, 0.85), (240, -1, 46, 6, BLUE, 0.85)],
    }
    # (from lon, to lon, line width, label): the trade winds blow west.
    winds = {
        "elnino": (228, 206, 2.0, "weak trade winds"),
        "neutral": (250, 185, 3.5, "trade winds"),
        "lanina": (270, 170, 5.5, "stronger trade winds"),
    }
    panels = [("El Nino", "elnino"), ("Neutral", "neutral"),
              ("La Nina", "lanina")]
    slot = 0.315
    for n, (title, key) in enumerate(panels):
        top = 1.0 - n * slot
        fig.text(0.015, top - 0.022, tilde(title), fontsize=26,
                 fontweight="bold", color=INK, va="center")
        ax = fig.add_axes([0.01, top - 0.04 - 0.262, 0.98, 0.262])
        ax.set_xlim(120, 311)
        ax.set_ylim(-30, 30)
        ax.set_facecolor(SEA)
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        for cx, cy, rx, ry, col, al in water[key]:
            ax.add_patch(Ellipse((cx, cy), 2 * rx, 2 * ry, color=col,
                                 alpha=al, lw=0))
        for pts in lands:
            ax.add_patch(Polygon(pts, closed=True, color=LAND, lw=0))
        ax.axhline(0, color="#555555", lw=1.2, ls=(0, (2, 3)))
        ax.add_patch(Rectangle((NINO34_LON_E[0], NINO34_LAT[0]),
                               NINO34_LON_E[1] - NINO34_LON_E[0],
                               NINO34_LAT[1] - NINO34_LAT[0],
                               fill=False, ec="#111111", lw=2.6))
        ax.text(sum(NINO34_LON_E) / 2, NINO34_LAT[1] + 1.5,
                tilde("Nino 3.4"), fontsize=LABEL_PT, ha="center",
                va="bottom", color="#111111")
        ax.text(122, 25, "Asia", fontsize=LABEL_PT, color=INK, va="center")
        ax.text(124, -23, "Australia", fontsize=LABEL_PT, color=INK,
                va="center")
        ax.text(309, 12, "the Americas", fontsize=LABEL_PT, color=INK,
                ha="right", va="center")
        x1, x2, lw, label = winds[key]
        ax.annotate("", xy=(x2, 15), xytext=(x1, 15),
                    arrowprops=dict(arrowstyle="-|>", color="#111111",
                                    lw=lw, mutation_scale=18 + 4 * lw))
        ax.text((x1 + x2) / 2.0, 19, label, fontsize=LABEL_PT,
                ha="center", va="bottom", color="#111111")
    fig.text(0.985, 0.022, "Red: warm water. Blue: cool water. "
             "A simplified map.", fontsize=LABEL_PT, ha="right",
             color=DIM, va="center")
    return _png(fig)


def _key_line(fig, y, parts, size):
    """One line of coloured words across the top of a picture, left to
    right: parts = [(words, colour, bold)]."""
    r = fig.canvas.get_renderer()
    x = 0.02
    for words, col, bold in parts:
        tx = fig.text(x, y, words, fontsize=size, color=col, va="center",
                      fontweight="bold" if bold else "normal")
        x += (tx.get_window_extent(renderer=r).width
              / float(fig.bbox.width)) + 0.012


def _class_colours(classes):
    return [{"el": RED, "la": BLUE}.get(c, NEUTRAL_GREY) for c in classes]


def _key(fig, y, size):
    _key_line(fig, y, [(tilde("Red: El Nino, by NOAA" + chr(0x2019)
                              + "s rule."), RED, True),
                       (tilde("Blue: La Nina."), BLUE, True),
                       ("Grey: neutral.", NEUTRAL_GREY, True)], size)


def picture_since1950(rows, figs):
    """Step 2: NOAA's RONI from 1950 to the newest season, one sliver per
    season, coloured by NOAA's classification (red El Nino, blue La Nina,
    grey neutral; Tony's change of Nov 17), the +0.5 and -0.5 thresholds
    dashed, the three strongest El Nino events labelled from the data, and
    the current event marked provisional (the June design, Tony's note of
    Nov 16)."""
    plt = _plt()
    import numpy as np
    t = np.array([r["year"] + (r["k"] + 0.5) / 12.0 for r in rows])
    v = np.array([r["value"] for r in rows])
    fig = plt.figure(figsize=(PICTURE_WIDTH_IN, 7.4))
    ax = fig.add_axes([0.105, 0.085, 0.875, 0.80])
    lo, hi = float(v.min()) - 0.45, float(v.max()) + 0.55
    ax.set_xlim(1949.5, float(t[-1]) + 1.5)
    ax.set_ylim(lo, hi)
    for g in (-2, -1, 1, 2):
        if lo < g < hi:
            ax.axhline(g, color="#e3e3e3", lw=1, zorder=0)
    ax.bar(t, v, width=1 / 12.0, color=_class_colours(figs["classes"]),
           lw=0, zorder=2)
    _key(fig, 0.965, LABEL_PT - 1)
    fig.text(0.02, 0.922, "Dashed lines: the +0.5 and %s0.5 thresholds."
             % MINUS, fontsize=LABEL_PT - 2, color=DIM, va="center")
    for thr in (EPISODE_THRESHOLD_C, -EPISODE_THRESHOLD_C):
        ax.axhline(thr, color="#888888", lw=1.3, ls=(0, (4, 3)), zorder=3)
    ax.axhline(0, color="#333333", lw=1.2, zorder=3)
    ce = figs["current_event"]
    if ce:
        # The event under way, shaded to the chart's edge: provisional.
        ax.axvspan(t[ce["first"]] - 1 / 24.0, float(t[-1]) + 1.5,
                   color=PROVISIONAL_SHADE, lw=0, zorder=1)
    for ev in figs["strongest"]:
        if ev["ongoing"]:
            continue
        i = next(j for j, r in enumerate(rows)
                 if (r["season"], r["year"]) == (ev["peak_season"],
                                                 ev["peak_year"]))
        ax.text(t[i], v[i] + 0.07, ev["label"].replace("-", EN_DASH),
                fontsize=LABEL_PT - 1, ha="center", va="bottom", color=INK,
                zorder=5)
    newest = figs["newest"]
    ax.plot([t[-1]], [v[-1]], "o", color="#111111", ms=8, zorder=6)
    ax.annotate("now %s" % _signed(newest["value"]),
                xy=(t[-1], v[-1] + 0.08), xytext=(float(t[-1]) + 1.4,
                                                  hi - 0.1),
                fontsize=LABEL_PT - 1, ha="right", va="top", color=INK,
                arrowprops=dict(arrowstyle="-", color="#111111", lw=1.2,
                                shrinkA=2, shrinkB=0,
                                relpos=(0.93, 0.0)),
                zorder=6)
    if ce:
        ax.text(float(t[-1]) + 1.4, lo + 0.1, "%s (shaded): provisional"
                % figs["event_label"].replace("-", EN_DASH),
                fontsize=LABEL_PT - 2, ha="right", va="bottom", color=INK,
                zorder=6)
    ax.set_ylabel("RONI, degrees C", fontsize=LABEL_PT, color=INK)
    yt = [g for g in (-2, -1, 0, 1, 2) if lo < g < hi]
    ax.set_yticks(yt)
    ax.set_yticklabels([("%+d" % g if g else "0").replace("-", MINUS)
                        for g in yt], fontsize=LABEL_PT - 1, color=DIM)
    ax.set_xticks(list(range(1950, int(t[-1]) + 1, 10)))
    ax.set_xticklabels([str(y) if y % 20 == 10 or y == 1950 else ""
                        for y in range(1950, int(t[-1]) + 1, 10)],
                       fontsize=LABEL_PT - 1, color=DIM)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    return _png(fig)


def picture_card(rows, figs):
    """The lobby's Featured card (earth/el_nino.png), as Sudan's card has
    its own: step 2's chart redrawn at 2:1, the shape the lobby frames a
    wide card's picture in (index.html, .lobby-wide-picture), with larger
    words for a card a phone shows about 330 px wide. Coloured by NOAA's
    classification, the three strongest events labelled, the event under
    way shaded and marked provisional; all from the data."""
    plt = _plt()
    import numpy as np
    big = 30
    t = np.array([r["year"] + (r["k"] + 0.5) / 12.0 for r in rows])
    v = np.array([r["value"] for r in rows])
    fig = plt.figure(figsize=(PICTURE_WIDTH_IN, PICTURE_WIDTH_IN / 2.0))
    ax = fig.add_axes([0.055, 0.13, 0.925, 0.85])
    lo, hi = float(v.min()) - 0.2, float(v.max()) + 0.75
    ax.set_xlim(1949.5, float(t[-1]) + 1.5)
    ax.set_ylim(lo, hi)
    ce = figs["current_event"]
    if ce:
        ax.axvspan(t[ce["first"]] - 1 / 24.0, float(t[-1]) + 1.5,
                   color=PROVISIONAL_SHADE, lw=0, zorder=1)
    ax.bar(t, v, width=1 / 12.0, color=_class_colours(figs["classes"]),
           lw=0, zorder=2)
    for thr in (EPISODE_THRESHOLD_C, -EPISODE_THRESHOLD_C):
        ax.axhline(thr, color="#888888", lw=1.6, ls=(0, (4, 3)), zorder=3)
    ax.axhline(0, color="#333333", lw=1.4, zorder=3)
    for ev in figs["strongest"]:
        if ev["ongoing"]:
            continue
        i = next(j for j, r in enumerate(rows)
                 if (r["season"], r["year"]) == (ev["peak_season"],
                                                 ev["peak_year"]))
        ax.text(t[i], v[i] + 0.06, ev["label"].replace("-", EN_DASH),
                fontsize=big - 6, ha="center", va="bottom", color=INK,
                zorder=5)
    ax.plot([t[-1]], [v[-1]], "o", color="#111111", ms=11, zorder=6)
    if ce:
        ax.text(float(t[-1]) + 1.3, lo + 0.08, "%s provisional"
                % figs["event_label"].replace("-", EN_DASH),
                fontsize=big - 8, ha="right", va="bottom", color=INK,
                zorder=6)
    ax.set_yticks([])
    ax.set_xticks(list(range(1950, int(t[-1]) + 1, 20)))
    ax.set_xticklabels([str(y) for y in range(1950, int(t[-1]) + 1, 20)],
                       fontsize=big - 6, color=DIM)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="x", length=0)
    return _png(fig)


def picture_this_year(figs):
    """Step 3: the last twelve seasons of RONI as bars, the record as a
    dashed line, both from the data."""
    plt = _plt()
    rows = figs["last_twelve"]
    rec = figs["record"]
    fig = plt.figure(figsize=(PICTURE_WIDTH_IN, 6.6))
    ax = fig.add_axes([0.1, 0.17, 0.88, 0.74])
    _key(fig, 0.96, LABEL_PT - 2)
    vals = [r["value"] for r in rows]
    lo = min(min(vals), 0) - 0.35
    hi = max(max(vals), rec["value"]) + 0.45
    ax.set_ylim(lo, hi)
    ax.set_xlim(-0.6, len(rows) - 0.4)
    for g in (-2, -1, 1, 2):
        if lo < g < hi:
            ax.axhline(g, color="#e3e3e3", lw=1, zorder=0)
    ax.axhline(0, color="#333333", lw=1.2, zorder=2)
    ax.bar(range(len(rows)), vals, width=0.68,
           color=_class_colours(figs["classes"][-len(rows):]), zorder=3)
    ax.axhline(rec["value"], color=INK, lw=1.6, ls=(0, (5, 3)), zorder=4)
    ax.text(-0.45, rec["value"] + 0.06, "record %s, %s" % (
        _signed(rec["value"]),
        figs["record_words"].replace("-", EN_DASH)),
        fontsize=LABEL_PT - 1, color=INK, va="bottom")
    ax.text(len(rows) - 1, vals[-1] + 0.05, _signed(vals[-1]),
            fontsize=LABEL_PT, ha="center", va="bottom", color=INK,
            zorder=5)
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([r["season"] for r in rows], fontsize=LABEL_PT - 3,
                       color=DIM)
    years = sorted(set(r["year"] for r in rows))
    for y in years:
        idx = [i for i, r in enumerate(rows) if r["year"] == y]
        ax.text(sum(idx) / float(len(idx)), lo - 0.42, str(y),
                fontsize=LABEL_PT - 1, ha="center", va="top", color=INK)
    yt = [g for g in (-2, -1, 0, 1, 2) if lo < g < hi]
    ax.set_yticks(yt)
    ax.set_yticklabels([("%+d" % g if g else "0").replace("-", MINUS)
                        for g in yt], fontsize=LABEL_PT - 1, color=DIM)
    ax.set_ylabel("RONI, degrees C", fontsize=LABEL_PT - 1, color=INK)
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="x", length=0)
    return _png(fig)


def chance_seasons(probs):
    """NOAA's table seasons with their years, in the RONI file's naming
    (DJF of year Y is December Y-1 to February Y). The table starts in the
    month it was issued or the one before; its years follow from there."""
    month = MONTH_NAMES.index(probs["issued"].split()[0]) + 1
    year = int(probs["issued"].split()[1])
    out = []
    for x in probs["seasons"]:
        k = SEASONS.index(x["season"])
        if out and k < SEASONS.index(out[-1][0]):
            year += 1
        elif not out and k + 1 < month - 6:
            year += 1
        out.append((x["season"], year))
    return out


def season_months_short(season):
    """'OND' -> 'Oct' + en dash + 'Dec': the season's first and last
    months, for an axis a reader can read without NOAA's letters."""
    k = SEASONS.index(season)
    return "%s%s%s" % (MONTH_NAMES[(k - 1) % 12][:3], EN_DASH,
                       MONTH_NAMES[(k + 1) % 12][:3])


def picture_expects(probs):
    """Step 4: NOAA's chance of El Nino, one bar per season in NOAA's
    table, labelled with the percentages."""
    plt = _plt()
    seas = probs["seasons"]
    fig = plt.figure(figsize=(PICTURE_WIDTH_IN, 6.0))
    ax = fig.add_axes([0.02, 0.21, 0.96, 0.76])
    ax.set_ylim(0, 116)
    ax.set_xlim(-0.6, len(seas) - 0.4)
    ax.bar(range(len(seas)), [x["el_nino"] for x in seas], width=0.66,
           color=RED, zorder=3)
    ax.axhline(0, color="#333333", lw=1.2, zorder=4)
    for i, x in enumerate(seas):
        ax.text(i, x["el_nino"] + 2, "%d%%" % x["el_nino"],
                fontsize=LABEL_PT - 1, ha="center", va="bottom", color=INK)
    ax.set_xticks(range(len(seas)))
    ax.set_xticklabels([season_months_short(x["season"]).replace(
        EN_DASH, EN_DASH + "\n") for x in seas],
        fontsize=LABEL_PT - 1, color=DIM, linespacing=1.05)
    ax.set_yticks([])
    for sp in ("top", "right", "left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(axis="x", length=0)
    named = chance_seasons(probs)
    fig.text(0.02, 0.035, "Seasons from %s to %s" % (
        season_words(*named[0]).replace("-", EN_DASH),
        season_words(*named[-1]).replace("-", EN_DASH)),
        fontsize=LABEL_PT - 2, color=DIM)
    return _png(fig)


def picture_heat():
    """Step 5: a drawing with no time axis. La Nina: heat goes into the
    ocean and is stored at depth. El Nino: the heat goes out into the air."""
    plt = _plt()
    from matplotlib.patches import Rectangle
    fig = plt.figure(figsize=(PICTURE_WIDTH_IN, 5.4))
    specs = [("La Nina", "heat\ngoes in", BLUE, False),
             ("El Nino", "heat\ngoes out", RED, True)]
    for n, (title, words, col, up) in enumerate(specs):
        ax = fig.add_axes([0.02 + n * 0.495, 0.03, 0.465, 0.94])
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")
        ax.text(5, 9.55, tilde(title), fontsize=26, fontweight="bold",
                ha="center", va="top", color=INK)
        ax.add_patch(Rectangle((0, 4.4), 10, 3.6, color="#eef3f8", lw=0))
        ax.text(0.3, 7.6, "air", fontsize=LABEL_PT, color=DIM, va="top")
        ax.add_patch(Rectangle((0, 0), 10, 4.4, color=col, alpha=0.85,
                               lw=0))
        ax.text(0.3, 4.0, "ocean", fontsize=LABEL_PT, color="white",
                va="top")
        if up:
            ax.annotate("", xy=(5, 7.6), xytext=(5, 2.2),
                        arrowprops=dict(arrowstyle="-|>", color="#111111",
                                        lw=4, mutation_scale=34))
            ax.text(5.5, 5.9, words, fontsize=LABEL_PT, color=INK,
                    va="center")
        else:
            ax.add_patch(Rectangle((0.6, 0.5), 8.8, 1.3, color=RED,
                                   alpha=0.9, lw=0))
            ax.text(5, 1.15, "extra heat stored at depth",
                    fontsize=LABEL_PT - 2, color="white", ha="center",
                    va="center")
            ax.annotate("", xy=(5, 2.0), xytext=(5, 7.6),
                        arrowprops=dict(arrowstyle="-|>", color="#111111",
                                        lw=4, mutation_scale=34))
            ax.text(5.5, 5.9, words, fontsize=LABEL_PT, color=INK,
                    va="center")
    return _png(fig)


# ==========================================================================
#   PART 2: THE PAGE
# ==========================================================================

# The step pictures' names: earth/el_nino_<step>.png.
PICTURE_KEYS = ("what", "since1950", "thisyear", "expects", "heat")

# The monthly promise (step 4's last sentence, L-060). Tony's ruling of
# Nov 17, 08:48: the night run checks NOAA and flags "EL NINO DUE" in its
# commit title (night_check(), below); Tony rebuilds the page by hand. The
# night never changes the page (R1, Oct 25). The sentence is on the page
# only while this names the way it is kept.
MONTHLY_REDRAW_WAY = ("the night run flags EL NINO DUE; Tony rebuilds "
                      "(Tony, 2026-11-17)")

# The energy imbalance chart, an old-gallery card (L-531 will move it): its
# address on the website; on a phone the gallery opens its upright twin.
ENERGY_IMBALANCE_URL = "/#energy_imbalance_desktop"

# The sibling website folder, Tony's layout (CLAUDE.md): the page and its
# five pictures are copied there by name. Nothing else is copied: the
# dated NOAA copies in data/earth/noaa_enso_reads/ stay in the orrery.
GALLERY_DIR = os.path.join("..", "tonyquintanilla.github.io")


def page_words(s):
    """Words for the page: Nino and Nina carry the tilde, as entities."""
    return s.replace("Nino", "Ni&ntilde;o").replace("Nina", "Ni&ntilde;a")


def _day_words(d):
    return "%d %s %d" % (d.day, MONTH_NAMES[d.month - 1], d.year)


def _dash(s):
    """A computed range for the page: hyphen to en dash."""
    return s.replace("-", "&ndash;")


def discussion_archive_url(issued):
    """NOAA's fixed address for one month's discussion, as the April one
    is cited: enso_disc_<mon><year>/ensodisc.shtml."""
    return ("https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/"
            "enso_disc_%s%d/ensodisc.shtml"
            % (MONTH_NAMES[issued.month - 1][:3].lower(), issued.year))


def _src(label, url):
    return (label, url)


def page_steps(data):
    """The five steps: title, picture key, caption, alt text, paragraphs
    [(html, mark)], sources [(label, url)], and step 2's boxed note. A mark
    says where a figure came from: 'computed' (from NOAA's files at this
    build), 'read from the discussion', or '' (fixed words, sourced)."""
    f = data["figures"]
    d = data["discussion"]
    p = data["probabilities"]
    newest = f["newest"]
    rec = f["record"]
    if f["record_passed"]:
        raise EnsoBuildStop(
            "NOAA's file shows the record passed (%s %d, %+.2f). Step 3's "
            "sentence 'It has not been passed yet.' is contradicted; the "
            "page needs Tony's words before it is rebuilt."
            % (rec["season"], rec["year"], rec["value"]))
    newest_months = f["newest_words"].rsplit(" ", 1)[0]
    strong = sorted(f["strongest"], key=lambda ev: ev["peak_year"])
    strong_words = "%s, %s and %s" % tuple(
        _dash(ev["label"]) for ev in strong)
    named = chance_seasons(p)
    disc_day = _day_words(d["issued"])
    disc_short = "%d %s %d" % (d["issued"].day,
                               MONTH_NAMES[d["issued"].month - 1][:3],
                               d["issued"].year)
    issued_short = "%s %s" % (p["issued"].split()[0][:3],
                              p["issued"].split()[1])
    archive = data.get("discussion_link", discussion_archive_url(d["issued"]))
    periods = " and for ".join(_dash(x) for x in d["historic_periods"])

    steps = []
    steps.append({
        "title": "What El Nino is", "key": "what", "caption": "",
        "alt": ("Three simplified maps of the tropical Pacific, one above "
                "the other, Asia and Australia on the left and the Americas "
                "on the right, with the Nino 3.4 box on the equator. El "
                "Nino: weak trade winds, warm water spread east toward the "
                "Americas. Neutral: trade winds blowing west, warm water in "
                "the west, cool water in the east. La Nina: stronger trade "
                "winds, more warm water toward Asia, more cool water in the "
                "east."),
        "paras": [
            ("In a neutral year, the trade winds blow west along the "
             "equator, taking warm water toward Asia. The sea off Asia is "
             "about 8&nbsp;&deg;C warmer than in the eastern Pacific, where "
             "cold water rises from deeper levels off South America.", ""),
            ("In an El Nino the trade winds weaken, and the warm water is "
             "pushed back east, toward the Americas.", ""),
            ("In a La Nina the trade winds are even stronger than usual, "
             "pushing more warm water toward Asia, and more cold water "
             "rises off the Americas.", ""),
            ("Think of the warm water sloshing from one side of the ocean "
             "to the other. The black box on the maps is the stretch of "
             "ocean NOAA watches, explained in the next step.", ""),
        ],
        "sources": [
            _src("NOAA Ocean Service, What are El Nino and La Nina?",
                 "https://oceanservice.noaa.gov/facts/ninonina.html"),
            _src("NOAA PMEL, What is El Nino?",
                 "https://www.pmel.noaa.gov/elnino/what-is-el-nino/"),
        ],
    })
    steps.append({
        "title": "Since 1950, in one line", "key": "since1950",
        "caption": "",
        "alt": ("NOAA's Relative Oceanic Nino Index from %d to %s, one "
                "sliver per season, colored by NOAA's classification: red "
                "for El Nino, blue for La Nina, grey for neutral, with "
                "dashed lines at the +0.5 and -0.5 thresholds. The "
                "strongest El Nino peaks are labelled %s. The newest "
                "season, %s at %s, ends the line; the %s event is shaded "
                "and marked provisional."
                % (f["first"]["year"],
                   f["newest_words"], strong_words.replace("&ndash;", "-"),
                   f["newest_words"], "%+.2f" % newest["value"],
                   f["event_label"])),
        "paras": [
            ("The line follows a box of ocean along the equator that NOAA "
             "calls Nino 3.4.", ""),
            ("Each sliver of the chart is one season: a three-month "
             "average. The seasons overlap, December&ndash;February, then "
             "January&ndash;March, and so on, so there are twelve to a "
             "year.", ""),
            ("For each season NOAA asks two questions. First: how much "
             "warmer or cooler than usual is the water in the Nino 3.4 box? "
             "Second: how much warmer or cooler than usual are all the "
             "tropical oceans, taken together? The index is the first "
             "answer minus the second, then NOAA rescales it.", ""),
            ("When the box has warmed more than the tropical oceans as a "
             "whole, the index is above zero. When it has warmed less, or "
             "cooled, the index is below zero. So the index can be above "
             "zero even when the box is a little cooler than usual, if the "
             "tropical oceans are cooler still. What counts is the "
             "difference.", ""),
            ("The colors are NOAA&rsquo;s classification. A season is red, "
             "El Nino, when it is one of at least five overlapping seasons "
             "in a row at +0.5 or more. It is blue, La Nina, in a run of at "
             "least five at &minus;0.5 or less. Otherwise it is grey, "
             "neutral. So a sliver above zero can still be grey.", ""),
            ("Why subtract? The scientists who proposed this index found "
             "that, measured the old way, global warming makes El Nino "
             "events &ldquo;seem bigger than they are,&rdquo; and La Nina "
             "events smaller. Taking away the warming of the tropical "
             "oceans as a whole takes that out of the measure.", ""),
            ("On this index, the three strongest El Nino events are %s."
             % strong_words, "computed"),
        ],
        "more": ("More about the Nino 3.4 box", [
            ("The name is not a latitude. Scientists first watched boxes "
             "numbered Nino 1 to Nino 4. Nino 3.4, named later, is the box "
             "between Nino 3 and Nino 4, overlapping both.", ""),
            ("It runs from 5 degrees north of the equator to 5 degrees "
             "south, and from 120 to 170 degrees west.", ""),
        ]),
        "more_after": 1,
        "note_summary": "For the technical reader",
        "note": ("Vertical axis: NOAA&rsquo;s "
                 "Relative Oceanic Nino Index (RONI), in degrees Celsius. "
                 "Each point is a three-month running mean of the "
                 "sea-surface temperature anomaly in the Nino 3.4 box "
                 "(5&deg;N&ndash;5&deg;S, 120&deg;W&ndash;170&deg;W), "
                 "minus the anomaly averaged over all tropical oceans "
                 "(20&deg;N&ndash;20&deg;S), then rescaled to match the "
                 "amplitude of the traditional index. Data: NOAA&rsquo;s "
                 "ERSST version 6. NOAA counts El Nino when the index is "
                 "+0.5 or more for five overlapping seasons in a row, and "
                 "La Nina at &minus;0.5 or less."),
        "note_after": 6,
        "sources": [
            _src("NOAA CPC, RONI",
                 "https://www.cpc.ncep.noaa.gov/products/"
                 "analysis_monitoring/enso/roni/"),
            _src("NOAA Climate.gov, Why are there so many ENSO indexes? "
                 "(2015)",
                 "https://www.climate.gov/news-features/blogs/enso/"
                 "why-are-there-so-many-enso-indexes-instead-just-one"),
            _src("NOAA CPC, RONI handout (2026)",
                 "https://www.cpc.ncep.noaa.gov/products/"
                 "analysis_monitoring/enso/roni/pdf/roni-info-may-2026.pdf"),
            _src("NWS statement 26-05 (13 Jan 2026)",
                 "https://www.weather.gov/media/notification/pdf_2026/"
                 "pns26-05_Relative_ONI.pdf"),
            _src("van Oldenborgh and others, Environmental Research "
                 "Letters (2021)",
                 "https://doi.org/10.1088/1748-9326/abe9ed"),
            _src("NOAA CPC, RONI data file", RONI_URL),
        ],
    })
    steps.append({
        "title": "This year so far", "key": "thisyear",
        "caption": ("NOAA&rsquo;s RONI, twelve overlapping seasons, to %s."
                    % _dash(f["newest_words"])),
        "caption_mark": "computed",
        "alt": ("Bars for the last twelve seasons of NOAA's RONI, %s to %s, "
                "colored by NOAA's classification: %s. The newest bar is "
                "%s. A dashed line marks the record, %s in %s."
                % (season_words(f["last_twelve"][0]["season"],
                                f["last_twelve"][0]["year"]),
                   f["newest_words"],
                   _class_runs(f["last_twelve"], f["classes"][-12:]),
                   "%+.2f" % newest["value"],
                   "%+.2f" % rec["value"], f["record_words"])),
        "paras": [
            ("NOAA issued its final La Nina advisory in April 2026, as "
             "neutral conditions emerged.", ""),
            ("By %s the index stood at %s." % (
                _dash(newest_months),
                "%+.2f" % newest["value"]), "computed"),
            ("NOAA&rsquo;s newest values can still be revised.", ""),
            ("The record on RONI, NOAA&rsquo;s official index, is %s, from "
             "%s. It has not been passed yet." % (
                 "%+.2f" % rec["value"], _dash(f["record_words"])),
             "computed"),
            ("This page&rsquo;s record is NOAA&rsquo;s three-month record "
             "on RONI. Other agencies report on another stretch of the "
             "Pacific, a single month, or a forecast, so a record reported "
             "elsewhere may not be this one.", ""),
        ],
        "join": [(0, 1, 2)],
        "sources": [
            _src("NOAA CPC, RONI data file (above)", RONI_URL),
            _src("NOAA ENSO discussion, 9 Apr 2026",
                 "https://www.cpc.ncep.noaa.gov/products/"
                 "analysis_monitoring/enso_disc_apr2026/ensodisc.shtml"),
            _src("Japan Meteorological Agency, El Nino Outlook "
                 "(10 Nov 2026)",
                 "https://ds.data.jma.go.jp/tcc/tcc/products/elnino/"
                 "outlook.html"),
            _src("WMO press conference (6 Nov 2026)",
                 "https://www.unognewsroom.org/teleprompter/en/3318/"
                 "wmo-press-conference-06-november-2026"),
        ],
    })
    paras4 = [
        ("NOAA&rsquo;s chances, from its forecast of %s. These are "
         "NOAA&rsquo;s numbers, not a forecast of ours." % p["issued"],
         "computed"),
        ("In its discussion of %s, NOAA gives about a %d percent chance of "
         "a &ldquo;historic event&rdquo; of +%.1f or more on RONI, for %s."
         % (disc_day, d["historic_pct"], d["historic_threshold"], periods),
         "read from the discussion"),
    ]
    if MONTHLY_REDRAW_WAY:
        paras4.append(("This page is updated after each NOAA update.", ""))
    steps.append({
        "title": "What NOAA expects", "key": "expects",
        "caption": ("NOAA&rsquo;s chance of El Nino, for overlapping "
                    "three-month seasons, issued %s." % p["issued"]),
        "caption_mark": "computed",
        # Shown larger: the bars are chances of El Nino, not its strength
        # (Tony's reading and the outside review, Nov 17).
        "caption_class": "lead",
        "alt": ("Bars for NOAA's chance of El Nino in each of %d "
                "overlapping three-month seasons, issued %s, from %s to %s: "
                "%s percent." % (
                    len(p["seasons"]), p["issued"],
                    season_words(*named[0]), season_words(*named[-1]),
                    ", ".join("%s %d" % (x["season"], x["el_nino"])
                              for x in p["seasons"]))),
        "paras": paras4,
        "sources": [
            _src("NOAA CPC, ENSO probabilities (%s)" % issued_short,
                 PROBABILITIES_URL),
            _src("NOAA ENSO discussion, %s" % disc_short, archive),
        ],
    })
    steps.append({
        "title": "Why the whole planet feels it", "key": "heat",
        "caption": "No time axis: this is how it works, not a record.",
        "alt": ("A drawing with no time axis, two panels. La Nina: an arrow "
                "carries heat down from the air into the ocean, where extra "
                "heat is stored at depth. El Nino: an arrow carries the heat "
                "up out of the ocean into the air."),
        "paras": [
            ("During La Nina, the tropical Pacific stores extra heat at "
             "depth. During El Nino that heat goes out into the air, "
             "warming the Pacific and then the world.", ""),
            ("Global average temperature typically follows the "
             "Pacific&rsquo;s warming by two to three months.", ""),
            ("El Nino&rsquo;s heat now lands on a warmer world. Whether "
             "global warming is also making El Nino events stronger is "
             "still being studied.", ""),
            ("More on the planet&rsquo;s energy budget: <a href=\"%s\">the "
             "energy imbalance chart</a>." % ENERGY_IMBALANCE_URL, ""),
        ],
        "sources": [
            _src("NOAA Climate.gov, El Nino and La Nina FAQ (2016)",
                 "https://prod-01-asg-www-climate.woc.noaa.gov/"
                 "news-features/understanding-climate/"
                 "el-nino-and-la-nina-frequently-asked-questions"),
            _src("NOAA Climate.gov, Where does global warming go during La "
                 "Nina?",
                 "https://www.climate.gov/news-features/blogs/enso/"
                 "where-does-global-warming-go-during-la-nina"),
            _src("NOAA Climate.gov, Has climate change already affected "
                 "ENSO? (2023)",
                 "https://climate.gov/news-features/blogs/enso/"
                 "has-climate-change-already-affected-enso"),
            _src("ECMWF, How confident should we be in a prediction of El "
                 "Nino? (Apr 2026)",
                 "https://www.ecmwf.int/en/about/media-centre/science-blog/"
                 "2026/el-nino-2026"),
        ],
    })
    return steps


def _class_runs(rows, classes):
    """'blue (La Nina) from A to B, grey (neutral) C, red (El Nino) from D
    to E', for alt text."""
    names = {"el": "red (El Nino)", "la": "blue (La Nina)",
             "neutral": "grey (neutral)"}
    runs = []
    for r, c in zip(rows, classes):
        if runs and runs[-1][0] == c:
            runs[-1][2] = r
        else:
            runs.append([c, r, r])
    out = []
    for c, a, b in runs:
        wa = season_words(a["season"], a["year"])
        if a is b:
            out.append("%s %s" % (names[c], wa))
        else:
            out.append("%s from %s to %s" % (
                names[c], wa, season_words(b["season"], b["year"])))
    return ", ".join(out)


PAGE_CSS = """:root{--bg:#0a0a0f;--panel:#12121a;--line:#2a2a3a;--text:#e8e6e3;
--dim:#9a9a9a;--accent:#c9a84c}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);
font-family:'DM Sans',-apple-system,Helvetica,Arial,sans-serif;
font-size:16px;line-height:1.5}
main{max-width:640px;margin:0 auto;padding:16px 16px 40px}
a{color:var(--accent);overflow-wrap:anywhere}
.back{font-size:14px;display:inline-block;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;
font-size:30px;line-height:1.15;margin:0 0 4px}
h2{font-size:17px;margin:22px 0 6px;color:var(--accent)}
.sub{color:var(--dim);margin:0 0 14px}
.status{background:var(--panel);border:1px solid var(--line);
border-radius:10px;padding:10px 12px;margin:0 0 14px;font-size:15px}
.status div{margin:2px 0}
.late{color:#f0b35a;font-weight:600}
.late[hidden]{display:none}
figure{margin:0 0 14px;background:#fff;border-radius:10px;padding:6px}
figure img{display:block;width:100%;height:auto}
figcaption{color:#333;font-size:13px;padding:4px 6px 2px}
.go{display:block;text-align:center;background:#2d6a2d;
border:1px solid #4ade80;color:#f8fafc;text-decoration:none;
font-weight:600;border-radius:10px;padding:14px 12px;margin:26px 0 4px;
font-size:17px}
.note{color:var(--dim);font-size:14px;margin:4px 0 0}
details{background:var(--panel);border:1px solid var(--line);
border-radius:10px;padding:0 12px;margin:4px 0 12px}
details summary{cursor:pointer;color:var(--accent);font-weight:600;
padding:10px 0;font-size:15px}
details summary:focus-visible{outline:2px solid var(--accent);
outline-offset:2px;border-radius:4px}
details[open] summary{padding-bottom:6px}
details p{margin:0 0 10px}
.tech p{font-size:14px;color:#cfcdca}
figcaption.lead{font-size:15px;font-weight:600;color:#111;
padding:6px 6px 4px}
.srcs{color:var(--dim);font-size:13px;margin:8px 0 0}
.src{color:var(--dim);font-size:13px;border-top:1px solid var(--line);
margin-top:24px;padding-top:10px}
.src div{margin:0 0 6px}
.step{border-top:1px solid var(--line);margin-top:26px;padding-top:4px}
.step h2{font-size:19px;margin:14px 0 10px}
.step p{margin:0 0 10px}
.n{color:var(--dim);font-weight:400;margin-right:6px}
.hint{color:var(--dim);font-size:14px;margin:0 0 6px}
"""

FONTS_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
              '<link href="https://fonts.googleapis.com/css2?family='
              'Cormorant+Garamond:wght@600&family=DM+Sans:wght@400;600'
              '&display=swap" rel="stylesheet">\n')


def _overdue_line(status):
    """The first safeguard's line. Since Tony's ruling of Nov 17 the page
    shows it itself (LATE_SCRIPT), the day after the date it prints as
    "Next expected", because the night never rebuilds the page."""
    return ("NOAA expected its next update on %s. This page has not caught "
            "up with it yet." % _day_words(status["next"]))


# A few lines run by the visitor's browser: once the day it reads is past
# the date the status box carries (data-next, the date printed as "Next
# expected"), the hidden late lines are shown. ASCII; nothing is fetched.
LATE_SCRIPT = """<script>
(function () {
  var box = document.querySelector("[data-next]");
  if (!box) { return; }
  var d = new Date();
  function two(n) { return (n < 10 ? "0" : "") + n; }
  var today = d.getFullYear() + "-" + two(d.getMonth() + 1) + "-" +
      two(d.getDate());
  if (today > box.getAttribute("data-next")) {
    var late = document.querySelectorAll(".late");
    for (var i = 0; i < late.length; i++) { late[i].hidden = false; }
  }
})();
</script>
"""


def _link(label, url):
    ext = not url.startswith("/")
    return '<a href="%s"%s>%s</a>' % (
        html.escape(url), ' target="_blank" rel="noopener"' if ext else "",
        page_words(label))


def build_page_html(data, steps):
    """The page: status line, five steps, the button and the footer."""
    s = data["status"]
    label = data["figures"]["event_label"]
    e = []
    w = e.append
    w("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
      "<meta name=\"viewport\" content=\"width=device-width, "
      "initial-scale=1, viewport-fit=cover\">\n")
    w("<title>%s - Paloma&#39;s Orrery</title>\n"
      % page_words("El Nino, %s" % _dash(label)))
    w(FONTS_LINK)
    w("<style>\n%s</style>\n</head>\n<body>\n<main>\n" % PAGE_CSS)
    w('<a class="back" href="/">&larr; Paloma&#39;s Orrery</a>\n')
    w("<h1>%s</h1>\n" % page_words("El Nino, %s" % _dash(label)))
    w('<p class="sub">%s</p>\n' % page_words(
        "NOAA&rsquo;s record of El Nino and La Nina since 1950, and what "
        "NOAA expects next, in five steps."))
    w('<div class="status" data-next="%s">\n' % s["next"].isoformat())
    w("<div>ENSO Alert System status: <b>%s</b></div>\n"
      % html.escape(s["status"]))
    w("<div>%s</div>\n" % _link("NOAA&rsquo;s latest update: %s"
                                % _day_words(s["issued"]), DISCUSSION_URL))
    w("<div>Next expected: %s</div>\n" % _day_words(s["next"]))
    w('<div class="late" hidden>%s</div>\n' % _overdue_line(s))
    w("</div>\n")
    w('<p class="hint">Scroll down, one step at a time.</p>\n')
    for n, st in enumerate(steps, start=1):
        w('<section class="step">\n')
        w('<h2><span class="n">%d.</span>%s</h2>\n'
          % (n, page_words(st["title"])))
        w('<figure><img src="%s_%s.png" alt="%s" loading="lazy">'
          % (SCENARIO_ID, st["key"],
             html.escape(tilde(st["alt"]).replace(" -0.5", " " + MINUS
                                                  + "0.5"))))
        if st["caption"]:
            cls = st.get("caption_class")
            w("<figcaption%s>%s</figcaption>" % (
                ' class="%s"' % cls if cls else "",
                page_words(st["caption"])))
        w("</figure>\n")
        groups = _paragraph_groups(st)
        for i, grp in enumerate(groups):
            w("<p>%s</p>\n" % page_words(" ".join(x for x, _m in grp)))
            if st.get("more") and i + 1 == st.get("more_after"):
                summary, paras = st["more"]
                w('<details class="more"><summary>%s</summary>\n%s'
                  '</details>\n' % (page_words(summary), "".join(
                      "<p>%s</p>\n" % page_words(x) for x, _m in paras)))
            if st.get("note") and i + 1 == st.get("note_after"):
                w('<details class="tech"><summary>%s</summary>\n<p>%s</p>'
                  '</details>\n' % (page_words(st["note_summary"]),
                                    page_words(st["note"])))
        w('<p class="srcs">Sources: %s</p>\n' % "; ".join(
            _link(lab, url) for lab, url in st["sources"]))
        w("</section>\n")
    w('<a class="go" href="%s" target="_blank" rel="noopener">Read '
      'NOAA&rsquo;s own discussion</a>\n' % DISCUSSION_URL)
    w('<p class="note">Opens NOAA&rsquo;s page, updated monthly.</p>\n')
    w('<div class="src">\n')
    w("<div>%s</div>\n" % page_words(
        "Source: NOAA Climate Prediction Center. The index is NOAA&rsquo;s "
        "Relative Oceanic Nino Index (RONI), 1950 to the latest season; the "
        "status and the chances are from NOAA&rsquo;s monthly ENSO "
        "discussion."))
    w("<div>Each step lists its sources. Japan&rsquo;s agency and the WMO "
      "are named only for step 3&rsquo;s sentence on other agencies.</div>\n")
    w("<div>Every build keeps a copy of the NOAA files it read. If an "
      "update is late, this page says so here. <span class=\"late\" "
      "hidden>%s</span></div>\n" % _overdue_line(s))
    w("<div>Paloma&rsquo;s Orrery. Drawn from NOAA&rsquo;s data, with "
      "Anthropic&rsquo;s Claude.</div>\n")
    w("</div>\n</main>\n")
    w(LATE_SCRIPT)
    w("</body>\n</html>\n")
    return "".join(e)


def _paragraph_groups(st):
    """Sentences grouped into paragraphs: each item is its own paragraph
    unless the step joins several (step 3's first three sentences are one
    paragraph, as the brief writes them)."""
    paras = st["paras"]
    joined = {}
    for grp in st.get("join", []):
        for i in grp:
            joined[i] = grp
    out, seen = [], set()
    for i, item in enumerate(paras):
        if i in seen:
            continue
        grp = joined.get(i, (i,))
        out.append([paras[j] for j in grp])
        seen.update(grp)
    return out


# The page, its five pictures, and the lobby card's picture (Tony, Nov 17:
# the page on the lobby's Featured, as a page card like Sudan's).
PAGE_FILES = ["%s.html" % SCENARIO_ID, "%s.png" % SCENARIO_ID] + [
    "%s_%s.png" % (SCENARIO_ID, k) for k in PICTURE_KEYS]


def write_page(data):
    """Write the page and its five pictures into data/earth/. Returns the
    paths written."""
    figs = data["figures"]
    folder = os.path.join(DATA_DIR, PAGE_FOLDER)
    if not os.path.exists(folder):
        os.makedirs(folder)
    pictures = {
        "what": picture_what(),
        "since1950": picture_since1950(data["rows"], figs),
        "thisyear": picture_this_year(figs),
        "expects": picture_expects(data["probabilities"]),
        "heat": picture_heat(),
    }
    steps = page_steps(data)
    paths = []
    for key in PICTURE_KEYS:
        path = os.path.join(folder, "%s_%s.png" % (SCENARIO_ID, key))
        with open(path, "wb") as fh:
            fh.write(pictures[key])
        paths.append(path)
    card = os.path.join(folder, "%s.png" % SCENARIO_ID)
    with open(card, "wb") as fh:
        fh.write(picture_card(data["rows"], figs))
    paths.append(card)
    page = os.path.join(folder, "%s.html" % SCENARIO_ID)
    with open(page, "wb") as fh:
        fh.write(build_page_html(data, steps).encode("ascii",
                                                     "xmlcharrefreplace"))
    paths.insert(0, page)
    paths.append(write_state(data))
    data["steps"] = steps
    return paths


# ==========================================================================
#   THE NIGHT'S CHECK (Tony's ruling of Nov 17, 08:48)
# ==========================================================================

# What the page shows, written at every build, so the night has something
# to compare NOAA's files with. It stays in the orrery (not in PAGE_FILES).
STATE_FILE = os.path.join(DATA_DIR, PAGE_FOLDER, "el_nino_state.json")

# The night row's verdict prefix and its flag. The flag is what the
# nightly commit title carries (orrery_maintenance_run.night_title_flags).
NIGHT_PREFIX = "EL NINO CHECK:"
NIGHT_FLAG = "EL NINO DUE"


def write_state(data):
    """Record what the page shows: the discussion's date, the newest RONI
    season, the chances' issue. ASCII JSON, LF."""
    import json
    n = data["figures"]["newest"]
    body = {
        "_comment": ("Written by enso_page_generator.py at every build: "
                     "what earth/el_nino.html shows. The night run "
                     "(enso_page_generator.py --night-check) compares "
                     "NOAA's files with it and flags EL NINO DUE when NOAA "
                     "has anything newer (L-060; Tony, 2026-11-17)."),
        "built": data["built"].isoformat(),
        "discussion_issued": data["discussion"]["issued"].isoformat(),
        "roni_newest": "%s %d" % (n["season"], n["year"]),
        "probabilities_issued": data["probabilities"]["issued"],
    }
    with open(STATE_FILE, "w", encoding="ascii", newline="\n") as fh:
        fh.write(json.dumps(body, indent=2, ensure_ascii=True) + "\n")
    return STATE_FILE


def _roni_order(words):
    """'ASO 2026' -> (2026, 8): comparable, in the file's own order."""
    season, year = words.split()
    return (int(year), SEASONS.index(season))


def _issue_order(words):
    """'November 2026' -> (2026, 11)."""
    month, year = words.split()
    return (int(year), MONTH_NAMES.index(month) + 1)


def newer_than_page(state, rows, probs, disc):
    """What NOAA has that the page does not show, in words; [] if none."""
    out = []
    shown = datetime.date(*[int(x) for x in
                            state["discussion_issued"].split("-")])
    if disc["issued"] > shown:
        out.append("discussion of %s (page: %s)" % (
            _day_words(disc["issued"]), _day_words(shown)))
    n = rows[-1]
    if (n["year"], n["k"]) > _roni_order(state["roni_newest"]):
        out.append("RONI to %s %d (page: %s)" % (
            n["season"], n["year"], state["roni_newest"]))
    if _issue_order(probs["issued"]) > _issue_order(
            state["probabilities_issued"]):
        out.append("chances issued %s (page: %s)" % (
            probs["issued"], state["probabilities_issued"]))
    return out


def _saved_copies(fname):
    """Every saved copy of one NOAA file, newest folder first."""
    root = os.path.join(DATA_DIR, PAGE_FOLDER, READS_FOLDER)
    if not os.path.isdir(root):
        return []
    stem, ext = os.path.splitext(fname)
    out = []
    for day in sorted(os.listdir(root), reverse=True):
        folder = os.path.join(root, day)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder), reverse=True):
            if name == fname or (name.startswith(stem + "_")
                                 and name.endswith(ext)):
                out.append(os.path.join(folder, name))
    return out


def save_night_copies(got, day):
    """Save each NOAA file the night read, unless the newest saved copy of
    it holds the same bytes. A file holding a non-ASCII byte is not saved
    at night: the night commits ASCII only (its gate); it is named instead,
    and the next hand build saves it. Returns (saved, skipped)."""
    saved, skipped = [], []
    folder = _reads_folder(day)
    for key, _url, fname in READ_FILES:
        body = got[key]
        prev = _saved_copies(fname)
        if prev:
            with open(prev[0], "rb") as fh:
                if fh.read() == body:
                    continue
        if any(b > 127 for b in bytearray(body)):
            skipped.append("%s (non-ASCII bytes)" % fname)
            continue
        if not os.path.exists(folder):
            os.makedirs(folder)
        path = os.path.join(folder, fname)
        if os.path.exists(path):
            stem, ext = os.path.splitext(fname)
            path = os.path.join(folder, "%s_%s%s" % (
                stem, datetime.datetime.utcnow().strftime("%H%M%S"), ext))
        with open(path, "wb") as fh:
            fh.write(body)
        saved.append(path.replace(os.sep, "/"))
    return saved, skipped


def night_check(today=None):
    """The night row. Reads NOAA's three files fresh and compares them with
    what the page shows (STATE_FILE). Nothing newer: writes nothing.
    Newer: saves the dated copies and says EL NINO DUE. NOAA unreachable,
    or its files no longer read as expected: reported, never halting (R4).
    Never touches the page. Returns (exit code, verdict line)."""
    import json
    if today is None:
        try:
            import utc_clock    # L-504: the night reads the clock as UTC
            today = utc_clock.utc_today()
        except ImportError:
            today = datetime.date.today()
    try:
        with open(STATE_FILE, encoding="ascii") as fh:
            state = json.load(fh)
    except (OSError, ValueError) as exc:
        return 1, ("%s FAIL -- the page's state file %s could not be read "
                   "(%s); rebuild the page with enso_page_generator.py."
                   % (NIGHT_PREFIX, STATE_FILE.replace(os.sep, "/"), exc))
    got = {}
    try:
        for key, url, _fname in READ_FILES:
            got[key] = _get(url)[0]
    except EnsoBuildStop as stop:
        return 1, "%s UNREACHABLE -- NOAA: %s" % (NIGHT_PREFIX, stop)
    try:
        rows = parse_roni(got["roni"])
        probs = parse_probabilities(got["probabilities"])
        disc = parse_discussion(got["discussion"])
    except EnsoBuildStop as stop:
        return 1, ("%s UNREACHABLE -- NOAA's files were read but no longer "
                   "read as expected: %s" % (NIGHT_PREFIX, stop))
    newer = newer_than_page(state, rows, probs, disc)
    if not newer:
        return 0, ("%s CURRENT -- the page shows NOAA's latest: discussion "
                   "of %s, RONI to %s, chances issued %s; nothing written."
                   % (NIGHT_PREFIX, _day_words(disc["issued"]),
                      state["roni_newest"], state["probabilities_issued"]))
    saved, skipped = save_night_copies(got, today)
    line = ("%s %s -- NOAA has newer than the page: %s. Copies: %s."
            % (NIGHT_PREFIX, NIGHT_FLAG, "; ".join(newer),
               ", ".join(saved) if saved else
               "already saved, the same bytes"))
    if skipped:
        line += " Not saved at night: %s." % ", ".join(skipped)
    line += " Tony rebuilds the page by hand."
    return 0, line


def copy_to_website(gallery_dir=GALLERY_DIR):
    """Copy the page and its five pictures, by name, to the website's
    earth/ folder. Nothing else goes: not the dated NOAA copies. Returns the
    paths written, or [] if the website folder is not beside the orrery."""
    import shutil
    dest = os.path.join(gallery_dir, PAGE_FOLDER)
    if not os.path.isdir(gallery_dir):
        return []
    if not os.path.exists(dest):
        os.makedirs(dest)
    out = []
    for name in PAGE_FILES:
        src = os.path.join(DATA_DIR, PAGE_FOLDER, name)
        shutil.copyfile(src, os.path.join(dest, name))
        out.append(os.path.join(dest, name))
    return out


def check_discussion_link(data):
    """The step-4 source links to NOAA's fixed address for this month's
    discussion; if NOAA has not put it there, the standing address is used
    and the build says so."""
    url = discussion_archive_url(data["discussion"]["issued"])
    try:
        _get(url)
        data["discussion_link"] = url
        return url, True
    except EnsoBuildStop:
        data["discussion_link"] = DISCUSSION_URL
        return DISCUSSION_URL, False


def report_words(steps):
    """Every sentence on the page, in order, with its sources and where
    its figures came from, as plain text for the person who reads it."""
    def plain(s):
        return html.unescape(re.sub(r"<[^>]+>", "", page_words(s)))
    out = []
    for n, st in enumerate(steps, start=1):
        out.append("STEP %d. %s" % (n, plain(st["title"])))
        if st["caption"]:
            out.append("  Caption: %s%s" % (plain(st["caption"]), (
                "  [%s]" % st["caption_mark"]) if st.get("caption_mark")
                else ""))
        out.append("  Alt text: %s" % tilde(st["alt"]))
        for i, (s, mark) in enumerate(st["paras"]):
            out.append("  - %s%s" % (plain(s), "  [%s]" % mark if mark
                                     else ""))
            if st.get("more") and i + 1 == st.get("more_after"):
                out.append("  [tap to open: %s]" % plain(st["more"][0]))
                for x, _m in st["more"][1]:
                    out.append("      %s" % plain(x))
            if st.get("note") and i + 1 == st.get("note_after"):
                out.append("  [tap to open: %s] %s" % (
                    plain(st["note_summary"]), plain(st["note"])))
        out.append("  Sources: " + "; ".join(
            "%s <%s>" % (plain(lab), url) for lab, url in st["sources"]))
    return "\n".join(out)


def run(today=None):
    """The whole build: the data (Part 1), the page and its pictures, the
    copy to the website."""
    data = run_data(today)
    figs = data["figures"]
    if not figs["current_event"]:
        raise EnsoBuildStop("NOAA's file shows no El Nino under way; the "
                            "page's title and steps are about one.")
    figs["event_label"] = event_label(data["rows"], figs["current_event"])
    link, archived = check_discussion_link(data)
    data["written"] = write_page(data)
    data["copied"] = copy_to_website()
    data["archived_link"] = archived
    return data


if __name__ == "__main__":
    # Run from the orrery folder, as the Run button does.
    here = os.path.dirname(os.path.abspath(__file__))
    os.chdir(here)
    if "--night-check" in sys.argv[1:]:
        # The night row (orrery_maintenance_run.py --night): compare, and
        # flag; never rebuild the page (Tony, 2026-11-17; R1).
        code, verdict = night_check()
        sys.stdout.write(verdict.encode("ascii", "replace").decode("ascii")
                         + "\n")
        sys.exit(code)
    try:
        result = run()
    except EnsoBuildStop as stop:
        print("BUILD STOPPED: %s" % stop)
        sys.exit(1)
    lines = [report_data(result), ""]
    lines.append("Written: " + ", ".join(result["written"]))
    lines.append("Copied to the website: " + (
        ", ".join(result["copied"]) if result["copied"]
        else "nothing (the website folder is not beside the orrery)"))
    if not result["archived_link"]:
        lines.append("NOTE: NOAA has no fixed address yet for this month's "
                     "discussion; step 4 links to the standing one.")
    lines.append("")
    lines.append(report_words(result["steps"]))
    text = "\n".join(lines)
    sys.stdout.write(text.encode("ascii", "replace").decode("ascii") + "\n")
