"""
food_insecurity_generator.py - IPC acute food-insecurity KMZ layer (Sudan, three periods, for Google Earth on the web).

Dedicated vector/categorical generator for the Earth System family. Builds ONE
KMZ holding the three periods of IPC's February 2026 analysis of Sudan --
Current (February-May 2026), Projected 1 (June-September 2026) and Projected
2 (October 2026-January 2027) -- one folder each, opening on Projected 2.
Per-area figures for all three periods are read at run time from the IPC
Mapping Tool's Excel export; outlines and the camps' points come from its
GeoJSON (whose features hold the Current period only). The two are joined by
area name, and the run stops, naming the area, if the Excel's Current figures
differ from the GeoJSON's. Every pop-up carries the full phase 1-5
breakdown (so a smaller Catastrophe population never hides behind a
Phase-4 color), the camps (IDP settlements) are drawn as circles in their
phase color, and Phase 5 (Catastrophe) populations as dark red dots (L-069).

Written for Google Earth on the web (L-001, Nov 2026): every style is shared
at Document level, there is no ScreenOverlay (the title and the legend live in
the "i" pin's pop-up), and pop-ups write one <div> per line, with no <table>
and no <br>. The KML is written as text, not through simplekml, which puts
styles inside Folders, where the web loses them.

Stance (from MANIFEST_food_insecurity_sudan_v2.md): synthesize nothing,
transcribe everything, attribute to IPC, defer causation to the reader.
National totals are TRANSCRIBED from the IPC report, NEVER summed from polygons.

Key functions:
    run() - end-to-end: join Excel + GeoJSON -> build KMZ (+ optional teaser).
    join_ipc_periods() - read both IPC files, join by name, check, stop on a
        difference.
    build_web_kml() - the three period folders, shared styles, "i" pin.
    build_geojson_records() - the GeoJSON's polygons, for the Plotly teaser.

Consumed by: Earth System GUI (registration snippet in the build handoff);
runnable standalone via __main__ (the Run button opens the scenario picker).

Role: devtool
Domain: earth_science

Module updated: November 2026 with Anthropic's Claude Opus 5.5
"""
import io
import os
import json
import math
import zipfile
import html

from earth_system_common import ScenarioPicker

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

SCENARIO_ID = "food_insecurity_sdn"
# The IPC Mapping Tool's GeoJSON export of 2026-11-13: outlines and points.
# It replaces the export of 2026-06-22, whose phase counts in 181 of 228
# features add up to more than the area's population (L-001, Nov 2026).
DEFAULT_GEOJSON = os.path.join(DATA_DIR, "IPC_SD_A_87143417_2026-11-13.geojson")
# The IPC Mapping Tool's Excel export of the same analysis: all three periods,
# area by area (L-001, Nov 2026). Read at run time by read_ipc_excel().
DEFAULT_EXCEL = os.path.join(
    DATA_DIR,
    "IPC_SD_Acute_Food_Insecurity_Analysis___SD_February_2026_2026-11-13.xlsx")

# ==========================================================================
#   SOURCED CONSTANTS -- every numeric/quoted claim carries a # Source: within
#   the provenance scanner's 60-line lookback. Transcribe, do not recall.
# ==========================================================================

# --- IPC phase ramp -------------------------------------------------------
# IPC carries no color in the GeoJSON; these RGB values were SAMPLED from the
# report's own "Key for the Map" legend swatches (a true in-document source),
# so they are the colors IPC used in THIS report rather than recalled hex.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027 (publ. 2026-06-03),
# Source+: page 7 "Key for the Map / IPC Acute Food Insecurity Phase Classification"
# Source+: legend swatches, sampled at 200 dpi (anti-alias +/-2; see build handoff).
PHASE_COLORS_RGB = {
    1: "#D0E7C7",   # Phase 1 - Minimal     (light green)
    2: "#F8E303",   # Phase 2 - Stressed    (yellow)
    3: "#E27826",   # Phase 3 - Crisis      (orange)
    4: "#C52127",   # Phase 4 - Emergency   (red)
    5: "#621012",   # Phase 5 - Famine/Catastrophe (dark red)
}
# Source: same legend, page 7 -- "Areas not analysed" (white) and "Areas with
# Source+: inadequate evidence" (grey) are distinct legend categories, not a phase.
NOT_ANALYSED_RGB = "#FFFFFF"        # Abyei PCA in the current export
INADEQUATE_EVIDENCE_RGB = "#BBBCBE"  # defined for completeness; not applied this cut

# Phase labels. Phase 5 is "Catastrophe" at the population level (used in the
# per-area breakdown) and "Famine" only as an area classification (none this round).
# Source: IPC Sudan Special Report page 1 / page 7 phase classification key.
PHASE_LABELS = {
    1: "Minimal",
    2: "Stressed",
    3: "Crisis",
    4: "Emergency",
    5: "Catastrophe",   # area-classification term is "Famine"
}

# Draping / opacity. The temperature family uses ~0x66 (40%) fill for OVERLAY
# circles; this is the PRIMARY data layer, so it reads more opaque. Tunable;
# Mode-5 visual call. (Family reference: earth_system_generator.build_impact_kml.)
POLY_FILL_ALPHA = "CC"   # ~80%
POLY_LINE_ALPHA = "FF"   # opaque hairline borders
LINE_RGB = "#5A5A5A"

# --- Phase 5 (Catastrophe) population dots (L-069) ------------------------
# Graduated proportional symbols: one maroon dot per area carrying a mapped
# Phase 5 (Catastrophe) population, sized by phase5_population (icon area ~
# population via sqrt scaling). The dot is pure IPC passthrough -- it carries
# field values read at runtime; no value is hardcoded or summed. Scale
# endpoints and the icon are Mode-5 visual tunables, NOT data claims.
P5_DOT_RGB = PHASE_COLORS_RGB[5]   # maroon; same source as the legend swatch
P5_DOT_MIN_SCALE = 0.5
P5_DOT_MAX_SCALE = 1.8
P5_DOT_ICON = "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"

# --- National headline figures (TRANSCRIBED from the report, NEVER summed) --
# A naive polygon sum over-counts (IDP settlements overlap host localities), so
# these come from the report TEXT, not from the GeoJSON.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, Country-wide Analysis
# Source+: (Feb-May 2026): "covering the total population of Sudan (47.5 million)";
# Source+: "nearly 19.5 million people are classified in IPC Phase 3 or above for the
# Source+: current period, including over 5 million people in IPC Phase 4 (Emergency)";
# Source+: "nearly 135,000 people are classified in IPC Phase 5 (Catastrophe)".
NATL_TOTAL_POP = "47.5 million"         # total population of Sudan analysed
NATL_PHASE3PLUS = "19.5 million"        # IPC Phase 3 or above, current period
NATL_PHASE4 = "5 million"               # IPC Phase 4 (Emergency), current period
NATL_PHASE5_CATASTROPHE = "135,000"     # IPC Phase 5 (Catastrophe), current period

# --- Projected 1 (June-September 2026), TRANSCRIBED, never summed ----------
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF page 22: "Around 2.2
# Source+: million people are expected to experience Emergency (IPC Phase 4)
# Source+: conditions in these areas between June and September 2026, while a
# Source+: further 3.1 million will likely be in Crisis (IPC Phase 3)"; "increasing
# Source+: to 5.6 million people during the lean season, corresponding to 67 percent
# Source+: of the analysed population"; Catastrophe (IPC Phase 5) "from nearly
# Source+: 135,000 people in February-May to nearly 200,000 people in June-September".
P1_PHASE3PLUS = "5.6 million"
P1_PHASE3PLUS_PCT = "67 percent"
P1_PHASE4 = "2.2 million"
P1_PHASE3 = "3.1 million"
P1_PHASE5 = "200,000"                   # "nearly 200,000"

# --- Projected 2 (October 2026-January 2027), TRANSCRIBED ------------------
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF page 28: "an estimated
# Source+: 4.9 million people (59 percent of the analysed population) will remain in
# Source+: Crisis or worse conditions (IPC Phase 3 or above). This includes over
# Source+: 71,000 people in Catastrophe (IPC Phase 5), 1.7 million in Emergency (IPC
# Source+: Phase 4), and 3 million in Crisis (IPC Phase 3)."
P2_PHASE3PLUS = "4.9 million"
P2_PHASE3PLUS_PCT = "59 percent"
P2_PHASE4 = "1.7 million"
P2_PHASE3 = "3 million"
P2_PHASE5 = "71,000"                    # "over 71,000"

# --- The projections' coverage (both periods), TRANSCRIBED -----------------
# Their numbers describe these 56 areas, never all of Sudan.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF pages 22 and 28,
# Source+: Methodological note: "56 areas out of 195 units of analysis of Sudan
# Source+: (including both settled localities and concentrations of IDP
# Source+: populations) are covered, equivalent to nearly 8.3 million people out of
# Source+: the total population of Sudan (47.5 million)."
PROJ_AREAS = "56"
PROJ_UNITS = "195"
PROJ_POP = "8.3 million"
COVERAGE_LINE = ("IPC's projection covers %s areas out of %s units of "
                 "analysis of Sudan, equivalent to nearly %s people out of "
                 "the total population of Sudan (%s). Its numbers describe "
                 "those %s areas, not all of Sudan."
                 % (PROJ_AREAS, PROJ_UNITS, PROJ_POP, NATL_TOTAL_POP,
                    PROJ_AREAS))
# Composed from the coverage constants above, for an area outside the 56.
NOT_IN_PROJECTION_LINE = ("IPC's projection for this period covers %s of "
                          "the %s units of analysis; this area is not one "
                          "of them." % (PROJ_AREAS, PROJ_UNITS))
# Transcribed verbatim, no numeric token.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF page 1: "Caution is
# Source+: therefore advised when comparing figures across analysis periods, as
# Source+: geographic coverage differs significantly."
COMPARE_CAUTION = ("IPC: \"Caution is therefore advised when comparing "
                   "figures across analysis periods, as geographic coverage "
                   "differs significantly.\"")

# IPC's OWN wording of the mapped-phase rule (transcribed verbatim -> safe tier).
# Source: IPC Sudan Special Report page 7 legend, "Key for the Map": "mapped
# Source+: Phase represents highest severity affecting at least 20% of the population".
TWENTY_PCT_RULE = ("The mapped phase is the highest severity affecting at least "
                   "20% of an area's population. A smaller Catastrophe population "
                   "can sit under a Phase 4 color -- the full breakdown in each "
                   "pop-up shows it.")
# The first clause above is IPC's verbatim legend wording; the second sentence
# is COMPOSED (ours) and explains the reveal. Numeric token (20%):
# Source: IPC Sudan Special Report page 7 legend wording (above).

# --- KEY DRIVERS (transcribed verbatim from the report; IPC's voice only) ---
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, "KEY DRIVERS" section
# Source+: (page 6). Wording lifted verbatim; smart quotes/dashes normalized to ASCII.
DRIVERS = [
    ("Conflict",
     "With no peace settlement in sight, three years of conflict continue to "
     "drive extreme levels of acute food insecurity and malnutrition. The "
     "destruction of infrastructure and goods indispensable for survival has "
     "continued and intensified."),
    ("Displacement and immobility",
     "Widespread displacement persists, especially in active conflict areas. "
     "Many civilians remain trapped or have sought refuge in remote areas "
     "deprived of services and assistance, placing them at heightened risk of "
     "Famine."),
    ("High food prices",
     "Supply chain disruptions, input shortages, reduced agricultural "
     "production and missed planting seasons have led to sustained increases "
     "in food prices, leaving many families unable to afford basic food items."),
    ("Collapse of health and WASH systems",
     "The war has devastated basic health and water infrastructure and "
     "services, with an estimated 40 percent of health facilities "
     "non-functional, accelerating nutritional deterioration."),
    ("Limited humanitarian access",
     "Severe and persistent access constraints remain a defining feature of the "
     "crisis. Large portions of populations in need remain unreachable, "
     "particularly in Greater Kordofan and parts of Greater Darfur."),
]

# IPC's own naming of the Middle East fuel/food/fertilizer channel (transcribed;
# the reader makes the Hormuz connection -- we never author the linkage).
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027 (Key Messages): the
# Source+: ongoing conflict in the Middle East "contributing to higher fuel, food, and
# Source+: fertilizer prices. The impacts of the Middle East crisis on Sudan are likely
# Source+: to intensify in the near and medium term."
MIDDLE_EAST_LINE = ("IPC notes the ongoing conflict in the Middle East "
                    "contributing to higher fuel, food, and fertilizer prices, "
                    "with impacts likely to intensify in the near and medium term.")

# C3 -- causal-restraint statement. COMPOSED (ours), no numeric token.
CAUSAL_RESTRAINT = ("This layer documents where IPC records strain and "
                    "attributes drivers to IPC. It draws no causal arrow of its "
                    "own.")

# Provenance / attribution lines.
# Source: data is the IPC Mapping Tool no-key GeoJSON download.
PROVENANCE_DATA = "IPC, IPC Mapping Tool"
# The report carries no formal "recommended citation" line; this is ASSEMBLED
# from the report's title page facts (publisher, title, dates) -- see handoff.
# Source: IPC Sudan Special Report title page (IPC Global Initiative; "IPC Acute
# Source+: Food Insecurity Analysis February 2026-January 2027"; published 3 June 2026).
CITATION = ("IPC Global Initiative. 2026. Sudan: IPC Acute Food Insecurity "
            "Analysis, February 2026 - January 2027 (Special Report). "
            "Published 3 June 2026.")

PERIOD_LABEL = "Current (February - May 2026)"

# --- The analysis's three periods (L-001, Nov 2026) -----------------------
# (code, the Excel's column prefix, IPC's own name and dates). The codes are
# the GeoJSON header's period_code values.
# Source: IPC Mapping Tool Excel export, sheet "Analysis Overview" (export
# Source+: 2026-11-13): "Projected 2 (2026-10-01 to 2027-01-31)", "Projected 1
# Source+: (2026-06-01 to 2026-09-30)", "Current (2026-02-01 to 2026-05-31)".
IPC_PERIODS = [
    ("current", "Current", "Current: February - May 2026",
     "2026-02-01", "2026-05-31"),
    ("projected-1", "Projected 1", "Projected 1: June - September 2026",
     "2026-06-01", "2026-09-30"),
    ("projected-2", "Projected 2", "Projected 2: October 2026 - January 2027",
     "2026-10-01", "2027-01-31"),
]

# --- Risk of Famine, by period (the files carry no flag) ------------------
# The report's names, transcribed in its order, and the one name each has in
# the data. "El Fasher" is "Al Fasher" in the data; "... IDP settlement" is
# "... IDPs"; Um Durein's camp is spelled with two spaces in the data.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF page 26, "RISK OF
# Source+: FAMINE": "These include At Tina locality, At Tina IDP settlement, El
# Source+: Fasher locality, Kernoi locality, Tawila IDP settlement, Um Baru locality,
# Source+: Um Baru IDP settlement (North Darfur), Dilling locality, Kadugli
# Source+: locality, Kadugli IDP settlement, Al Buram locality, Al Buram IDP
# Source+: settlement, Um Durein IDP settlement (South Kordofan), and Beliel
# Source+: locality (South Darfur)." October-January: "all the areas at risk of
# Source+: Famine in June-September 2026 will remain at risk, except for Beliel".
FAMINE_RISK_REPORT_TO_DATA = {
    "At Tina locality": "At Tina",
    "At Tina IDP settlement": "At Tina IDPs",
    "El Fasher locality": "Al Fasher",
    "Kernoi locality": "Kernoi",
    "Tawila IDP settlement": "Tawila IDPs",
    "Um Baru locality": "Um Baru",
    "Um Baru IDP settlement": "Um Baru IDPs",
    "Dilling locality": "Dilling",
    "Kadugli locality": "Kadugli",
    "Kadugli IDP settlement": "Kadugli IDPs",
    "Al Buram locality": "Al Buram",
    "Al Buram IDP settlement": "Al Buram IDPs",
    "Um Durein IDP settlement": "Um Durein  IDPs",
    "Beliel locality": "Beliel",
}
FAMINE_RISK_BY_PERIOD = {
    "projected-1": list(FAMINE_RISK_REPORT_TO_DATA),
    "projected-2": [n for n in FAMINE_RISK_REPORT_TO_DATA
                    if n != "Beliel locality"],
    # "current": no list in this report for February-May (gap, L-001).
}
# The report's own counts of those lists; the join checks the lists against
# them. IPC's words for the designation are carried as written.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF page 26: "a risk of
# Source+: Famine has been identified in 14 areas ... under a reasonable worst-case
# Source+: scenario"; "Therefore, 13 areas and IDP settlements are confirmed with a
# Source+: risk of Famine during this period" (October 2026-January 2027).
FAMINE_RISK_COUNTS = {"projected-1": 14, "projected-2": 13}
FAMINE_RISK_WORDS = "Risk of Famine (reasonable worst-case scenario)"


# ==========================================================================
#   COLOR HELPERS
# ==========================================================================

def rgb_to_kml(rgb_hex, alpha_hex):
    """Convert #RRGGBB + alpha byte to KML aabbggrr (alpha, blue, green, red)."""
    rgb_hex = rgb_hex.lstrip("#")
    r, g, b = rgb_hex[0:2], rgb_hex[2:4], rgb_hex[4:6]
    return (alpha_hex + b + g + r).lower()


# ==========================================================================
#   GEOJSON PARSING (transcribe per-area fields; compute nothing national)
# ==========================================================================

def _pct(frac):
    """IPC percentages are 0-1 fractions; render as a rounded percent string."""
    if frac is None:
        return "-"
    return "%.1f" % (float(frac) * 100.0)


def _intpop(v):
    if v is None:
        return "-"
    try:
        return "{:,}".format(int(round(float(v))))
    except (ValueError, TypeError):
        return str(v)


def build_geojson_records(geojson_path):
    """Parse the IPC GeoJSON into per-area records (polygons only).

    Returns (records, meta). Point features (call-out overlays) are skipped
    this cut. Nothing national is summed here -- headline figures are
    transcribed constants, not derived from these records.
    """
    with open(geojson_path, "r", encoding="utf-8") as f:
        gj = json.load(f)

    records = []
    meta = {}
    for feat in gj.get("features", []):
        geom = feat.get("geometry") or {}
        gtype = geom.get("type")
        if gtype not in ("Polygon", "MultiPolygon"):
            continue  # skip the 39 call-out points (deferred)
        p = feat.get("properties", {})
        if not meta:
            meta = {
                "analysis_name": p.get("analysis_name", ""),
                "from_date": p.get("from_date", ""),
                "thru_date": p.get("thru_date", ""),
                "country": p.get("country", ""),
                "export_timestamp": p.get("export_timestamp", ""),
            }
        records.append({
            "area_name": p.get("area_name") or p.get("name") or "(unnamed)",
            # 0, "P0" or missing is not analysed, never "Phase 0".
            "phase_value": (p.get("overall_phase_value")
                            if p.get("overall_phase_value") in (1, 2, 3, 4, 5)
                            else None),
            "phase_label": p.get("overall_phase_label"),
            "population": p.get("population", p.get("estimated_population")),
            "phase_pop": {i: p.get("phase%d_population" % i) for i in range(1, 6)},
            "phase_pct": {i: p.get("phase%d_percentage" % i) for i in range(1, 6)},
            "p3plus_pop": p.get("phase3_plus_population"),
            "p3plus_pct": p.get("phase3_plus_percentage"),
            "confidence_level": p.get("confidence_level"),
            "hfa_value": p.get("hfa_value"),
            "risk_of_famine": p.get("risk_of_famine"),
            "geometry": geom,
        })
    return records, meta


# ==========================================================================
#   IPC EXCEL READER AND THE JOIN (L-001, Nov 2026; all three periods)
# ==========================================================================
# The IPC Mapping Tool's GeoJSON download gives the Current (February-May
# 2026) features whatever period is selected; only its header's "active"
# flag changes. The Excel export of the same analysis holds all three
# periods, area by area. So the per-area figures for every period are read
# from the Excel at run time, and the GeoJSON supplies only the outlines
# (polygons) and the camps' points. Nothing is typed in; nothing is summed.

def _excel_int(v):
    """An Excel population cell -> int. Some Est Pop cells are text."""
    if v is None or v == "":
        return None
    return int(round(float(str(v).replace(",", "").strip())))


def _excel_float(v):
    if v is None or v == "":
        return None
    return float(v)


def _phase_code_value(code):
    """IPC's phase code "P0".."P5" -> 1..5, or None for not analysed.
    "P0", 0 and a missing code are all 'not analysed', never 'Phase 0'."""
    if code is None:
        return None
    s = str(code).strip().upper().lstrip("P")
    if not s.isdigit():
        return None
    n = int(s)
    return n if 1 <= n <= 5 else None


def read_ipc_excel(xlsx_path=None):
    """Read the IPC Excel export's "Population Table" sheet.

    Returns (areas, meta). areas maps the area name (the Excel's leading
    spaces stripped, the inner spelling kept, e.g. "Um Durein  IDPs") to
    {period_code: record} for the three periods in IPC_PERIODS. Rows
    indented by two spaces are areas; unindented rows are state totals and
    "ANALYSIS TOTALS", which are not read (they are not shown on the layer).
    meta carries the export date from the "Analysis Overview" sheet.
    """
    import openpyxl
    xlsx_path = xlsx_path or DEFAULT_EXCEL
    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    ws = wb["Population Table"]
    rows = list(ws.iter_rows(values_only=True))
    header = [str(h) if h is not None else "" for h in rows[0]]
    col = {h: i for i, h in enumerate(header)}

    def cell(row, prefix, field):
        key = "%s - %s" % (prefix, field)
        if key not in col:
            raise ValueError("IPC Excel: column %r not found in %s"
                             % (key, xlsx_path))
        return row[col[key]]

    areas = {}
    for row in rows[1:]:
        raw = row[0]
        if not isinstance(raw, str) or not raw.startswith("  "):
            continue   # state totals, ANALYSIS TOTALS, blank rows
        name = raw.lstrip(" ")
        if name in areas:
            raise ValueError("IPC Excel: area %r appears twice" % name)
        per = {}
        for code, prefix, _label, *_dates in IPC_PERIODS:
            phase_code = cell(row, prefix, "Phase")
            per[code] = {
                "phase_code": phase_code,
                "phase_value": _phase_code_value(phase_code),
                "population": _excel_int(cell(row, prefix, "Est Pop")),
                "phase_pop": {i: _excel_int(cell(row, prefix, "Phase %d" % i))
                              for i in range(1, 6)},
                "phase_pct": {i: _excel_float(cell(row, prefix, "Phase %d %%" % i))
                              for i in range(1, 6)},
                "p3plus_pop": _excel_int(cell(row, prefix, "Phase 3+")),
                "p3plus_pct": _excel_float(cell(row, prefix, "Phase 3+ %")),
                "from_date": str(cell(row, prefix, "From Date") or "")[:10],
                "thru_date": str(cell(row, prefix, "Thru Date") or "")[:10],
            }
        areas[name] = per

    meta = {}
    if "Analysis Overview" in wb.sheetnames:
        for r in wb["Analysis Overview"].iter_rows(values_only=True):
            if r and r[0] == "Export Date":
                meta["export_date"] = str(r[1])[:10]
            elif r and r[0] == "Analysis Title":
                meta["analysis_name"] = str(r[1])
    wb.close()
    return areas, meta


def read_geojson_features(geojson_path=None):
    """The GeoJSON's features grouped by area name: polygon outlines and
    points. Two identical points for one camp (IPC repeats some) count once.

    Returns (by_name, meta): by_name[name] = {"polygons": [feature...],
    "points": [feature...]}.
    """
    geojson_path = geojson_path or DEFAULT_GEOJSON
    with open(geojson_path, "r", encoding="utf-8") as f:
        gj = json.load(f)
    by_name = {}
    seen_points = set()
    meta = {}
    for feat in gj.get("features", []):
        p = feat.get("properties", {})
        geom = feat.get("geometry") or {}
        name = p.get("area_name") or p.get("name") or "(unnamed)"
        if not meta:
            meta = {
                "analysis_name": p.get("analysis_name", ""),
                "export_timestamp": p.get("export_timestamp", ""),
            }
        slot = by_name.setdefault(name, {"polygons": [], "points": []})
        if geom.get("type") in ("Polygon", "MultiPolygon"):
            slot["polygons"].append(feat)
        elif geom.get("type") == "Point":
            key = (name, tuple(geom.get("coordinates", [])))
            if key in seen_points:
                continue
            seen_points.add(key)
            slot["points"].append(feat)
    return by_name, meta


# Current columns of the Excel that must equal the GeoJSON, field by field.
_CURRENT_CHECK_FIELDS = (
    ["population", "p3plus_pop"]
    + ["phase%d_population" % i for i in range(1, 6)]
)


def _geojson_current_value(props, field):
    if field == "population":
        return props.get("population", props.get("estimated_population"))
    if field == "p3plus_pop":
        return props.get("phase3_plus_population")
    return props.get(field)


def _excel_current_value(rec, field):
    if field == "population":
        return rec["population"]
    if field == "p3plus_pop":
        return rec["p3plus_pop"]
    i = int(field[5])
    return rec["phase_pop"][i]


def join_ipc_periods(xlsx_path=None, geojson_path=None):
    """Join the Excel's three periods to the GeoJSON's outlines by area name.

    Stops (ValueError, the areas named) when:
      - a name is in one file and not the other;
      - any Current figure in the Excel differs from the GeoJSON's (every
        feature of the area is checked, the camps' points included), or
        the mapped phase differs;
      - a famine-risk name in FAMINE_RISK_REPORT_TO_DATA does not resolve
        to exactly one area.

    Returns a dict:
      areas      name -> {"periods": {code: rec}, "polygons": [...],
                          "points": [...], "kind": "polygon"|"camp"}
      analysed   code -> sorted names whose phase is 1-5 in that period
      camps      sorted names drawn only as points (no polygon)
      famine     code -> sorted data names at risk of Famine
      meta       export date, analysis name
    """
    xl, xl_meta = read_ipc_excel(xlsx_path)
    gj, gj_meta = read_geojson_features(geojson_path)

    only_xl = sorted(set(xl) - set(gj))
    only_gj = sorted(set(gj) - set(xl))
    if only_xl or only_gj:
        raise ValueError("IPC join: names do not match. Only in the Excel: %s. "
                         "Only in the GeoJSON: %s." % (only_xl, only_gj))

    differences = []
    for name in sorted(xl):
        cur = xl[name]["current"]
        for feat in gj[name]["polygons"] + gj[name]["points"]:
            props = feat.get("properties", {})
            for field in _CURRENT_CHECK_FIELDS:
                a = _excel_current_value(cur, field)
                b = _geojson_current_value(props, field)
                b = None if b is None else int(round(float(b)))
                # Not-analysed: the Excel may leave a cell empty where the
                # GeoJSON writes 0 (Abyei PCA); both mean no people counted.
                if (a or 0) != (b or 0):
                    differences.append("%s: %s Excel %s, GeoJSON %s"
                                       % (name, field, a, b))
            gv = props.get("overall_phase_value")
            gv = gv if gv in (1, 2, 3, 4, 5) else None
            if gv != cur["phase_value"]:
                differences.append("%s: phase Excel %s, GeoJSON %s"
                                   % (name, cur["phase_code"],
                                      props.get("overall_phase_label")))
    if differences:
        raise ValueError("IPC join: the Excel's Current figures differ from "
                         "the GeoJSON in %d place(s):\n  %s"
                         % (len(differences), "\n  ".join(differences)))

    # Each period's dates in the Excel must be IPC's dates for that period.
    wrong_dates = []
    for name in sorted(xl):
        for code, _prefix, _label, from_d, thru_d in IPC_PERIODS:
            rec = xl[name][code]
            if (rec["from_date"], rec["thru_date"]) != (from_d, thru_d):
                wrong_dates.append("%s %s: %s to %s" % (
                    name, code, rec["from_date"], rec["thru_date"]))
    if wrong_dates:
        raise ValueError("IPC join: period dates differ from IPC_PERIODS: %s"
                         % "; ".join(wrong_dates))

    areas = {}
    for name in sorted(xl):
        kind = "polygon" if gj[name]["polygons"] else "camp"
        areas[name] = {"periods": xl[name],
                       "polygons": gj[name]["polygons"],
                       "points": gj[name]["points"],
                       "kind": kind}

    analysed = {code: sorted(n for n in areas
                             if areas[n]["periods"][code]["phase_value"])
                for code, *_rest in IPC_PERIODS}
    camps = sorted(n for n in areas if areas[n]["kind"] == "camp")

    famine = {}
    bad = []
    for code, report_names in FAMINE_RISK_BY_PERIOD.items():
        resolved = []
        for rn in report_names:
            dn = FAMINE_RISK_REPORT_TO_DATA.get(rn)
            hits = [n for n in areas if n == dn]
            if len(hits) != 1:
                bad.append("%s -> %r (%d matches)" % (rn, dn, len(hits)))
            elif not areas[hits[0]]["periods"][code]["phase_value"]:
                bad.append("%s -> %r is not analysed in %s" % (rn, dn, code))
            else:
                resolved.append(hits[0])
        if len(resolved) != FAMINE_RISK_COUNTS[code]:
            bad.append("%s: %d areas resolved, the report counts %d"
                       % (code, len(resolved), FAMINE_RISK_COUNTS[code]))
        famine[code] = sorted(resolved)
    if bad:
        raise ValueError("IPC join: famine-risk names that do not resolve to "
                         "exactly one area: %s" % "; ".join(bad))

    meta = {"export_date": xl_meta.get("export_date")
            or (gj_meta.get("export_timestamp") or "")[:10],
            "analysis_name": gj_meta.get("analysis_name")
            or xl_meta.get("analysis_name", "")}
    return {"areas": areas, "analysed": analysed, "camps": camps,
            "famine": famine, "meta": meta}


def _rings_from_polygon(coords):
    """GeoJSON Polygon coords -> (outer, [holes]) as (lon,lat) tuples."""
    outer = [(pt[0], pt[1]) for pt in coords[0]]
    holes = [[(pt[0], pt[1]) for pt in ring] for ring in coords[1:]]
    return outer, holes


def _representative_point(geom):
    """Interior-ish point for a dot: centroid of the largest outer ring's
    vertices. Placement only -- not a claim about the area."""
    if geom["type"] == "Polygon":
        ring = geom["coordinates"][0]
    else:  # MultiPolygon -> largest outer ring by vertex count
        ring = max((poly[0] for poly in geom["coordinates"]), key=len)
    xs = [pt[0] for pt in ring]
    ys = [pt[1] for pt in ring]
    return sum(xs) / len(xs), sum(ys) / len(ys)


# ==========================================================================
#   THE WEB FILE (L-001, Nov 2026): one KMZ, three periods, for Google Earth
#   on the web
# ==========================================================================
# Written as KML text here, not through simplekml: simplekml writes a
# feature's style inside the Folder that holds the feature, and Google Earth
# on the web loses every style referenced from inside a Folder (every area
# plain yellow; tested 2026-11-13). The rules this builder keeps, each from
# that test:
#   - every style is a shared Style at Document level, referenced by id;
#   - no ScreenOverlay (unsupported on the web): the title and the legend
#     live in the "i" pin's pop-up, as lines;
#   - pop-ups write one <div> per line and <b> for labels; no <table>, no
#     <br> (the web strips <br> and turns <table> into "TABLE SECTION").
# Every figure in a pop-up is read from the IPC Excel at run time; national
# figures are the transcribed constants above; nothing is summed.

CAMP_ICON = P5_DOT_ICON      # a plain circle, tinted by phase
CAMP_SCALE = 0.8             # Mode-5 visual tunable, not a data claim
P5_DOT_CLASSES = 8           # shared dot sizes; Mode-5 visual tunable
INFO_ICON = "http://maps.google.com/mapfiles/kml/shapes/info-i.png"
INFO_LAT, INFO_LON = 15.5, 32.5   # placement only, near Khartoum

# --- IPC's Risk of Famine symbol (Tony's ruling, Nov 13, 2026, 19:31) -----
# Drawn at each at-risk area, in its period, as well as the pop-up line.
# The shape and colour are IPC's: a dark red triangle with a white X.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, PDF page 21, "Key for
# Source+: the Map": the "Risk of Famine" symbol; its fill sampled at 400 dpi
# Source+: as RGB (96, 13, 15) (anti-alias +/-6), the same way PHASE_COLORS_RGB was.
FAMINE_SYMBOL_RGB = (96, 13, 15)
FAMINE_SYMBOL_WORDS = "a small dark red triangle with a white X"
# The symbol's legend line, one home for the "i" pop-up and the page. It
# credits IPC as the symbol's source: "after IPC" (Tony's ruling of Nov 13,
# 2026, 20:49). COMPOSED, no numeric token.
FAMINE_LEGEND_LINE = ("Risk of Famine (symbol after IPC): %s, on each area "
                      "IPC lists at Risk of Famine (reasonable worst-case "
                      "scenario)" % FAMINE_SYMBOL_WORDS)
FAMINE_ICON_FILE = "famine_risk.png"   # packed inside the KMZ
FAMINE_ICON_SCALE = 1.1                # Mode-5 visual tunable


def famine_risk_icon_png(size=64):
    """IPC's Risk of Famine symbol as PNG bytes: drawn 4x and scaled down
    for smooth edges. Pure drawing; it carries no figure."""
    from PIL import Image, ImageDraw
    big = size * 4
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pad = big * 0.06
    tri = [(big / 2.0, pad), (big - pad, big - pad), (pad, big - pad)]
    d.polygon(tri, fill=FAMINE_SYMBOL_RGB + (255,),
              outline=(255, 255, 255, 255))
    cx, cy, r = big / 2.0, big * 0.66, big * 0.15
    w = int(big * 0.07)
    d.line([(cx - r, cy - r), (cx + r, cy + r)], fill=(255, 255, 255, 255),
           width=w)
    d.line([(cx - r, cy + r), (cx + r, cy - r)], fill=(255, 255, 255, 255),
           width=w)
    im = im.resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    return buf.getvalue()


def famine_risk_popup_html(name, area, code, meta):
    rec = area["periods"][code]
    pv = rec["phase_value"]
    return (_div("<b>%s</b>" % _x(name))
            + _labelled("Period:", _period_label(code))
            + _div("<b>%s</b>" % _x(FAMINE_RISK_WORDS))
            + _labelled("Mapped IPC Phase:",
                        "Phase %d (%s)" % (pv, PHASE_LABELS[pv]))
            + _footer(meta))

# Plain colour names for the "i" pop-up's key, now that the legend card is
# gone. COMPOSED: everyday names for the swatches sampled in PHASE_COLORS_RGB.
PHASE_COLOR_WORDS = {1: "light green", 2: "yellow", 3: "orange",
                     4: "red", 5: "dark red"}

# The period that opens visible (Tony's ruling, Nov 13, 2026: one file,
# opening on October-January). The other two arrive switched off.
OPEN_PERIOD = "projected-2"
# Folder order in the list: the visible period first, then back in time.
FOLDER_ORDER = ["projected-2", "projected-1", "current"]

FOOTER_STYLE = "font-size:11px;color:#555"


def _x(text):
    """Escape text for XML element content or for HTML inside CDATA."""
    return html.escape(str(text), quote=True)


def _cdata(inner):
    return "<![CDATA[" + inner.replace("]]>", "]]]]><![CDATA[>") + "]]>"


def _div(inner_html, style=""):
    if style:
        return '<div style="%s">%s</div>' % (style, inner_html)
    return "<div>%s</div>" % inner_html


def _labelled(label, value):
    return _div("<b>%s</b> %s" % (_x(label), _x(value)))


def _period_label(code):
    return [p[2] for p in IPC_PERIODS if p[0] == code][0]


# --------------------------------------------------------------------------
#   Words (composed sentences are built here from sourced constants)
# --------------------------------------------------------------------------

def compose_framing_text():
    """The Current period's framing sentences. Numeric tokens are the
    sourced NATL_* constants and TWENTY_PCT_RULE above.

    C1 -- mapped-vs-population reconciliation (the hidden Catastrophe).
    C2 -- IPC's mapped-phase rule (TWENTY_PCT_RULE, IPC verbatim clause).
    C3 -- causal-restraint statement.
    """
    c1 = ("No area is mapped Phase 5 (Famine), but about %s people are in "
          "Phase 5 (Catastrophe), concentrated in North Darfur, South Darfur "
          "and South Kordofan." % NATL_PHASE5_CATASTROPHE)
    national = ("Sudan, current period (February - May 2026): of %s people "
                "analyzed, about %s are in IPC Phase 3 or above (Crisis or "
                "worse), including over %s in Phase 4 (Emergency)."
                % (NATL_TOTAL_POP, NATL_PHASE3PLUS, NATL_PHASE4))
    return {"national": national, "c1": c1, "c2": TWENTY_PCT_RULE,
            "c3": CAUSAL_RESTRAINT}


def compose_period_lines(code, joined):
    """The national lines for one period, as plain sentences, in IPC's
    numbers (transcribed constants; never summed from the areas)."""
    no_p5_area = not any(a["periods"][code]["phase_value"] == 5
                         for a in joined["areas"].values())
    if code == "current":
        f = compose_framing_text()
        lines = [f["national"]]
        if no_p5_area:
            lines.append(f["c1"])
        return lines
    if code == "projected-1":
        lines = [
            "June - September 2026, the lean season, in the %s areas IPC "
            "analyzed: %s people, %s of the analyzed population, in IPC "
            "Phase 3 or above (Crisis or worse). Around %s are expected in "
            "Phase 4 (Emergency) and a further %s in Phase 3 (Crisis)."
            % (PROJ_AREAS, P1_PHASE3PLUS, P1_PHASE3PLUS_PCT, P1_PHASE4,
               P1_PHASE3),
        ]
        p5 = "nearly %s" % P1_PHASE5
    else:
        lines = [
            "October 2026 - January 2027, the harvest season, in the %s "
            "areas IPC analyzed: an estimated %s people, %s of the analyzed "
            "population, in IPC Phase 3 or above (Crisis or worse), "
            "including %s in Phase 4 (Emergency) and %s in Phase 3 (Crisis)."
            % (PROJ_AREAS, P2_PHASE3PLUS, P2_PHASE3PLUS_PCT, P2_PHASE4,
               P2_PHASE3),
        ]
        p5 = "over %s" % P2_PHASE5
    if no_p5_area:
        lines.append("No area is mapped Phase 5 (Famine) in this period, but "
                     "IPC expects %s people in Phase 5 (Catastrophe)." % p5)
    else:
        lines.append("IPC expects %s people in Phase 5 (Catastrophe)." % p5)
    lines.append(COVERAGE_LINE)
    lines.append(COMPARE_CAUTION)
    return lines


# --------------------------------------------------------------------------
#   Styles (all at Document level)
# --------------------------------------------------------------------------

def _poly_style_xml(style_id, rgb, fill_alpha):
    return ('<Style id="%s"><LineStyle><color>%s</color><width>1</width>'
            '</LineStyle><PolyStyle><color>%s</color><fill>1</fill>'
            '<outline>1</outline></PolyStyle></Style>\n'
            % (style_id, rgb_to_kml(LINE_RGB, POLY_LINE_ALPHA),
               rgb_to_kml(rgb, fill_alpha)))


def _icon_style_xml(style_id, rgb, scale, href, label_scale=0):
    color = ("<color>%s</color>" % rgb_to_kml(rgb, "FF")) if rgb else ""
    return ('<Style id="%s"><IconStyle>%s<scale>%s</scale><Icon><href>%s'
            '</href></Icon></IconStyle><LabelStyle><scale>%s</scale>'
            '</LabelStyle></Style>\n'
            % (style_id, color, scale, _x(href), label_scale))


def _p5_dot_scales():
    span = P5_DOT_MAX_SCALE - P5_DOT_MIN_SCALE
    return [round(P5_DOT_MIN_SCALE + span * k / (P5_DOT_CLASSES - 1), 3)
            for k in range(P5_DOT_CLASSES)]


def _p5_dot_class(p5, p5_max):
    """1..P5_DOT_CLASSES: icon area ~ population (sqrt), one scale for all
    three periods so a dot of one size means the same people in each."""
    frac = math.sqrt(float(p5) / float(p5_max)) if p5_max else 0.0
    return 1 + int(round(frac * (P5_DOT_CLASSES - 1)))


def web_styles_xml():
    out = []
    for pv in range(1, 6):
        out.append(_poly_style_xml("phase%d" % pv, PHASE_COLORS_RGB[pv],
                                   POLY_FILL_ALPHA))
    out.append(_poly_style_xml("not_analysed", NOT_ANALYSED_RGB, "66"))
    for pv in range(1, 6):
        out.append(_icon_style_xml("camp_phase%d" % pv, PHASE_COLORS_RGB[pv],
                                   CAMP_SCALE, CAMP_ICON))
    out.append(_icon_style_xml("camp_not_analysed", NOT_ANALYSED_RGB,
                               CAMP_SCALE, CAMP_ICON))
    for k, s in enumerate(_p5_dot_scales(), 1):
        out.append(_icon_style_xml("p5dot_%d" % k, P5_DOT_RGB, s,
                                   P5_DOT_ICON))
    out.append(_icon_style_xml("info", None, 1.3, INFO_ICON, label_scale=0.9))
    out.append(_icon_style_xml("famine_risk", None, FAMINE_ICON_SCALE,
                               FAMINE_ICON_FILE).replace(
        "</Icon>", '</Icon><hotSpot x="0.5" y="0" xunits="fraction" '
        'yunits="fraction"/>'))
    return "".join(out)


# --------------------------------------------------------------------------
#   Pop-ups
# --------------------------------------------------------------------------

def _footer(meta):
    return (_div("Analysis: %s" % _x(meta["analysis_name"]), FOOTER_STYLE)
            + _div("Source: %s" % _x(PROVENANCE_DATA), FOOTER_STYLE)
            + _div("Data retrieved: %s" % _x(meta["export_date"]),
                   FOOTER_STYLE))


def area_popup_html(name, area, code, meta, famine_names):
    """One area's (or camp's) pop-up for one period: the FULL phase 1-5
    breakdown, people and percent, then Phase 3+, IPC's evidence and
    assistance levels where the export carries them, and the source."""
    rec = area["periods"][code]
    lines = [_div("<b>%s</b>" % _x(name))]
    if area["kind"] == "camp":
        lines.append(_div("IDP settlement (a camp for internally displaced "
                          "people)"))
    lines.append(_labelled("Period:", _period_label(code)))
    pv = rec["phase_value"]
    if pv is None:
        lines.append(_labelled("Mapped IPC Phase:", "Not analyzed"))
        if code != "current":
            lines.append(_div(_x(NOT_IN_PROJECTION_LINE)))
    else:
        lines.append(_labelled("Mapped IPC Phase:",
                               "Phase %d (%s)" % (pv, PHASE_LABELS[pv])))
        if name in famine_names:
            lines.append(_div("<b>%s</b>" % _x(FAMINE_RISK_WORDS)))
        lines.append(_labelled("Population (area):",
                               _intpop(rec["population"])))
        lines.append(_div("<b>Phase breakdown (people, percent):</b>"))
        for i in range(1, 6):
            lines.append(_div(_x("Phase %d %s: %s (%s%%)"
                                 % (i, PHASE_LABELS[i],
                                    _intpop(rec["phase_pop"][i]),
                                    _pct(rec["phase_pct"][i])))))
        lines.append(_labelled("Phase 3+ (Crisis or worse):",
                               "%s (%s%%)" % (_intpop(rec["p3plus_pop"]),
                                              _pct(rec["p3plus_pct"]))))
        if code == "current":
            # IPC's evidence and assistance levels: the GeoJSON carries them
            # for the Current period only; the Excel carries none.
            props = (area["polygons"] + area["points"])[0]["properties"]
            conf = props.get("confidence_level")
            hfa = props.get("hfa_value")
            lines.append(_labelled("Evidence level (IPC):",
                                   "-" if conf is None else conf))
            lines.append(_labelled("Assistance (HFA) level:",
                                   "-" if hfa is None else hfa))
    return "".join(lines) + _footer(meta)


def p5_dot_popup_html(name, area, code, meta):
    rec = area["periods"][code]
    pv = rec["phase_value"]
    return (_div("<b>%s</b>" % _x(name))
            + _labelled("Period:", _period_label(code))
            + _labelled("Mapped IPC Phase:",
                        "Phase %d (%s)" % (pv, PHASE_LABELS[pv]))
            + _labelled("In Phase 5 (Catastrophe):",
                        "%s people (%s%% of the area)"
                        % (_intpop(rec["phase_pop"][5]),
                           _pct(rec["phase_pct"][5])))
            + _labelled("Population (area):", _intpop(rec["population"]))
            + _footer(meta))


def _p5_range(joined, code):
    vals = [a["periods"][code]["phase_pop"][5] for a in
            joined["areas"].values()
            if (a["periods"][code]["phase_pop"][5] or 0) > 0]
    return (min(vals), max(vals)) if vals else (None, None)


def period_description_html(code, joined):
    lines = [_div("<b>%s</b>" % _x(_period_label(code)))]
    for s in compose_period_lines(code, joined):
        lines.append(_div(_x(s)))
    lo, hi = _p5_range(joined, code)
    if hi:
        lines.append(_div(_x(
            "Dark red dots: people in Phase 5 (Catastrophe), by area. The "
            "largest dot in this period is %s people, the smallest %s."
            % (_intpop(hi), _intpop(lo)))))
    n = len(FAMINE_RISK_BY_PERIOD.get(code, []))
    if n:
        lines.append(_div(_x(
            "%s areas and IDP settlements are at %s. Each says so in its "
            "pop-up." % (n, FAMINE_RISK_WORDS))))
    return "".join(lines)


def info_popup_html(joined):
    """The "i" pin: what the map shows, the periods, the key (each phase
    with its colour in words), the 20-percent rule, the national lines of
    each period, IPC's drivers, and the source. Replaces the title card
    and the legend card, which the web does not show."""
    meta = joined["meta"]
    f = compose_framing_text()
    h = lambda t: _div("<b>%s</b>" % _x(t), "margin-top:8px")
    lines = [_div("<b>Sudan -- Acute Food Insecurity (IPC)</b>",
                  "font-size:16px")]
    lines.append(_div(_x(
        "Three periods of one IPC analysis, one folder each. The map opens "
        "on %s. To see another period, switch its folder on and the others "
        "off." % _period_label(OPEN_PERIOD))))
    for code in FOLDER_ORDER:
        lines.append(_div("- " + _x(_period_label(code))))

    lines.append(h("What the colors mean"))
    for pv in range(1, 6):
        lines.append(_div(_x("Phase %d %s: %s" % (
            pv, "Famine / Catastrophe" if pv == 5 else PHASE_LABELS[pv],
            PHASE_COLOR_WORDS[pv]))))
    lines.append(_div(_x("Not analyzed: white")))
    lines.append(_div(_x(f["c2"])))
    lines.append(_div(_x(
        "Small circles are IDP settlements (camps for internally displaced "
        "people), colored by their phase. Dark red dots show people in "
        "Phase 5 (Catastrophe); a larger dot means more people, and a dot "
        "of one size means the same number of people in every period.")))
    lines.append(_div(_x(
        "%s in that period. The area's pop-up says so too."
        % FAMINE_LEGEND_LINE)))

    for code in FOLDER_ORDER:
        lines.append(h(_period_label(code)))
        for s in compose_period_lines(code, joined):
            lines.append(_div(_x(s)))

    lines.append(h("Key drivers (IPC)"))
    for name, _text in DRIVERS:
        lines.append(_div("- " + _x(name)))
    lines.append(_div(_x(MIDDLE_EAST_LINE)))
    lines.append(h("What this layer does not assert"))
    lines.append(_div(_x(f["c3"])))
    lines.append(_div(_x("Source: %s" % PROVENANCE_DATA), FOOTER_STYLE))
    lines.append(_div(_x(CITATION), FOOTER_STYLE))
    lines.append(_div("Data retrieved: %s" % _x(meta["export_date"]),
                      FOOTER_STYLE))
    return "".join(lines)


# --------------------------------------------------------------------------
#   Geometry and placemarks
# --------------------------------------------------------------------------

def _coords_xml(ring):
    return " ".join("%r,%r" % (pt[0], pt[1]) for pt in ring)


def _polygon_xml(coords):
    rings = ["<outerBoundaryIs><LinearRing><coordinates>%s</coordinates>"
             "</LinearRing></outerBoundaryIs>" % _coords_xml(coords[0])]
    for hole in coords[1:]:
        rings.append("<innerBoundaryIs><LinearRing><coordinates>%s"
                     "</coordinates></LinearRing></innerBoundaryIs>"
                     % _coords_xml(hole))
    return "<Polygon><tessellate>1</tessellate>%s</Polygon>" % "".join(rings)


def _geometry_xml(geom):
    if geom["type"] == "Polygon":
        return _polygon_xml(geom["coordinates"])
    return ("<MultiGeometry>%s</MultiGeometry>"
            % "".join(_polygon_xml(c) for c in geom["coordinates"]))


def _point_xml(lon, lat):
    return ("<Point><altitudeMode>clampToGround</altitudeMode>"
            "<coordinates>%r,%r,0</coordinates></Point>" % (lon, lat))


def _placemark(name, style_id, description, geometry_xml):
    return ("<Placemark><name>%s</name><styleUrl>#%s</styleUrl>"
            "<description>%s</description>%s</Placemark>\n"
            % (_x(name), style_id, _cdata(description), geometry_xml))


def _folder(name, children, visibility=None, open_=False, description=None):
    head = "<Folder><name>%s</name>" % _x(name)
    if visibility is not None:
        head += "<visibility>%d</visibility>" % visibility
    if open_:
        head += "<open>1</open>"
    if description:
        head += "<description>%s</description>" % _cdata(description)
    return head + "\n" + "".join(children) + "</Folder>\n"


def _period_folder_xml(code, joined, p5_max):
    meta = joined["meta"]
    famine_names = set(joined["famine"].get(code, []))
    areas, camps, dots, risk = [], [], [], []
    for name in sorted(joined["areas"]):
        area = joined["areas"][name]
        rec = area["periods"][code]
        pv = rec["phase_value"]
        popup = area_popup_html(name, area, code, meta, famine_names)
        if area["kind"] == "polygon":
            style = "phase%d" % pv if pv else "not_analysed"
            for feat in area["polygons"]:
                areas.append(_placemark(name, style, popup,
                                        _geometry_xml(feat["geometry"])))
            dot_at = _representative_point(area["polygons"][0]["geometry"])
        else:
            style = "camp_phase%d" % pv if pv else "camp_not_analysed"
            for feat in area["points"]:
                lon, lat = feat["geometry"]["coordinates"][:2]
                camps.append(_placemark(name, style, popup,
                                        _point_xml(lon, lat)))
            dot_at = tuple(area["points"][0]["geometry"]["coordinates"][:2])
        if name in famine_names:
            risk.append(_placemark(
                name, "famine_risk",
                famine_risk_popup_html(name, area, code, meta),
                _point_xml(dot_at[0], dot_at[1])))
        p5 = rec["phase_pop"][5] or 0
        if pv and p5 > 0:
            dots.append((p5, _placemark(
                name, "p5dot_%d" % _p5_dot_class(p5, p5_max),
                p5_dot_popup_html(name, area, code, meta),
                _point_xml(dot_at[0], dot_at[1]))))
    dots = [x for _p, x in sorted(dots, key=lambda t: -t[0])]
    children = [_folder("Areas", areas),
                _folder("IDP settlements (camps)", camps),
                _folder("Phase 5 (Catastrophe) populations", dots)]
    if risk:
        children.append(_folder(FAMINE_RISK_WORDS, risk))
    return _folder(_period_label(code), children,
                   visibility=1 if code == OPEN_PERIOD else 0,
                   open_=(code == OPEN_PERIOD),
                   description=period_description_html(code, joined))


def build_web_kml(joined):
    """The whole web document: shared styles, the "i" pin, three period
    folders (Projected 2 visible, the other two switched off)."""
    p5_max = max((a["periods"][c]["phase_pop"][5] or 0)
                 for a in joined["areas"].values()
                 for c, *_rest in IPC_PERIODS)
    info = _placemark("Sudan -- Acute Food Insecurity - tap for details",
                      "info", info_popup_html(joined),
                      _point_xml(INFO_LON, INFO_LAT))
    body = [_folder("Framing (read this first)", [info])]
    for code in FOLDER_ORDER:
        body.append(_period_folder_xml(code, joined, p5_max))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
            "<name>Sudan Food Insecurity (IPC) -- three periods</name>"
            "<open>1</open>\n"
            + web_styles_xml() + "".join(body)
            + "</Document>\n</kml>\n")


def package_kmz(kml_str):
    """Write the KMZ: doc.kml plus the Risk of Famine symbol, drawn at build
    time (no card images; the web shows none). The filename is unchanged,
    so links by name keep working."""
    kmz_path = os.path.join(DATA_DIR, "%s_blockbuster.kmz" % SCENARIO_ID)
    with zipfile.ZipFile(kmz_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("doc.kml", kml_str.encode("utf-8"))
        zf.writestr(FAMINE_ICON_FILE, famine_risk_icon_png())
    return kmz_path


# ==========================================================================
#   THE SHORT PAGE AND ITS PICTURE (L-001, Nov 2026; brief's amendment of
#   Nov 13, 16:05, and Tony's ruling of Nov 13, 19:49)
# ==========================================================================
# The layer's one home on the website: written here, from the same constants
# and data as the KMZ, so its words and their sources live in one place.
# Phone-first and upright. It links out to Tony's shared Google Earth
# project: Google Earth web will not show inside another site's page (every
# earth.google.com address answers X-Frame-Options SAMEORIGIN; checked by
# the coordinator, Nov 13, 2026).

# Tony's public Google Earth project for this layer (his ruling of Nov 13,
# 2026: the project renamed "Sudan"; this link, not the older one).
GE_PROJECT_URL = ("https://earth.google.com/earth/d/"
                  "1tvCdwVYhIwNetF-phuT4eTMztfOOIuaG?usp=sharing")
# IPC's own interactive map of this analysis, the authority (Tony's ruling of
# Nov 13, 2026, 19:49, which gave this address).
IPC_MAP_URL = ("https://www.ipcinfo.org/ipc-country-analysis/details-map/"
               "en/c/1163315/?iso3=SDN")
PAGE_PERIOD = "projected-2"   # the period the picture draws (the file opens on it)

# How this map relates to IPC's (Tony's ruling of Nov 13, 2026, 19:49).
# COMPOSED, no numeric token; every item is either read from IPC (named as
# IPC's) or a drawing choice of this layer (named as ours).
RELATION_IPC_OWN = ("From IPC: the data, the phase colors, the Risk of "
                    "Famine symbol, the figures and the words.")
RELATION_ADDED = [
    "Dark red dots for people in Phase 5 (Catastrophe), who can be hidden "
    "under a lower phase's color.",
    "The three periods side by side, one folder each.",
    "Google Earth's satellite globe beneath them.",
]
RELATION_NOT_SHOWN = [
    "IPC's food-assistance symbols.",
    "The evidence levels for the two projections.",
    "Acute malnutrition, which IPC classifies in its own separate analysis.",
]
RELATION_AUTHORITY = "IPC's own map is the authority:"

PAGE_CSS = """
:root{--bg:#0a0a0f;--panel:#12121a;--line:#2a2a3a;--text:#e8e6e3;
--dim:#9a9a9a;--accent:#c9a84c}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--text);
font-family:'DM Sans',-apple-system,Helvetica,Arial,sans-serif;
font-size:16px;line-height:1.5}
main{max-width:640px;margin:0 auto;padding:16px 16px 40px}
a{color:var(--accent)}
.back{font-size:14px;display:inline-block;margin-bottom:12px}
h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;
font-size:30px;line-height:1.15;margin:0 0 4px}
h2{font-size:17px;margin:22px 0 6px;color:var(--accent)}
.sub{color:var(--dim);margin:0 0 14px}
figure{margin:0 0 14px;background:#fff;border-radius:10px;padding:6px}
figure img{display:block;width:100%;height:auto}
figcaption{color:#333;font-size:13px;padding:4px 6px 2px}
.go{display:block;text-align:center;background:#2d6a2d;
border:1px solid #4ade80;color:#f8fafc;text-decoration:none;
font-weight:600;border-radius:10px;padding:14px 12px;margin:6px 0 4px;
font-size:17px}
.note{color:var(--dim);font-size:14px;margin:4px 0 0}
ul{padding-left:20px;margin:4px 0}
li{margin:3px 0}
.key{list-style:none;padding:0}
.sw{display:inline-block;width:16px;height:16px;border:1px solid #888;
vertical-align:-3px;margin-right:8px;border-radius:2px}
.src{color:var(--dim);font-size:13px;border-top:1px solid var(--line);
margin-top:24px;padding-top:10px}
"""


def page_picture_png(joined, code=PAGE_PERIOD, width_px=1000):
    """A still picture of one period's map, drawn from the same joined data
    as the KMZ at every build (never a screenshot): areas in their phase
    colours, not-analysed areas white, the camps as circles, the Phase 5
    dots and IPC's Risk of Famine symbol. Returns PNG bytes."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon as MplPolygon
    from matplotlib.collections import PatchCollection

    def rgb01(hexstr):
        h = hexstr.lstrip("#")
        return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))

    alpha = int(POLY_FILL_ALPHA, 16) / 255.0
    patches, faces = [], []
    xs, ys = [], []
    for name, area in joined["areas"].items():
        pv = area["periods"][code]["phase_value"]
        face = rgb01(PHASE_COLORS_RGB[pv]) if pv else rgb01(NOT_ANALYSED_RGB)
        for feat in area["polygons"]:
            g = feat["geometry"]
            polys = ([g["coordinates"]] if g["type"] == "Polygon"
                     else g["coordinates"])
            for poly in polys:
                ring = [(pt[0], pt[1]) for pt in poly[0]]
                patches.append(MplPolygon(ring, closed=True))
                faces.append(face + (alpha if pv else 1.0,))
                xs += [p[0] for p in ring]
                ys += [p[1] for p in ring]

    fig_w = width_px / 100.0
    span_x, span_y = max(xs) - min(xs), max(ys) - min(ys)
    fig = plt.figure(figsize=(fig_w, fig_w * span_y / span_x), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()
    fig.patch.set_facecolor("white")
    pc = PatchCollection(patches, facecolors=faces,
                         edgecolors=rgb01(LINE_RGB), linewidths=0.4)
    ax.add_collection(pc)

    p5_max = max((a["periods"][c]["phase_pop"][5] or 0)
                 for a in joined["areas"].values()
                 for c, *_rest in IPC_PERIODS)
    famine = set(joined["famine"].get(code, []))
    for name, area in joined["areas"].items():
        rec = area["periods"][code]
        pv = rec["phase_value"]
        if area["kind"] == "polygon":
            at = _representative_point(area["polygons"][0]["geometry"])
        else:
            at = tuple(area["points"][0]["geometry"]["coordinates"][:2])
            ax.plot([at[0]], [at[1]], "o", ms=7,
                    mfc=rgb01(PHASE_COLORS_RGB[pv]) if pv else "white",
                    mec="#333333", mew=0.8, zorder=3)
        p5 = rec["phase_pop"][5] or 0
        if pv and p5 > 0:
            # the KMZ's dot classes, as marker sizes (visual only)
            k = _p5_dot_class(p5, p5_max)
            ax.plot([at[0]], [at[1]], "o", ms=4 + 1.6 * k,
                    mfc=rgb01(P5_DOT_RGB), mec="white", mew=0.6, zorder=4)
        if name in famine:
            fam = tuple(c / 255.0 for c in FAMINE_SYMBOL_RGB)
            ax.plot([at[0]], [at[1] + 0.22], "^", ms=13, mfc=fam,
                    mec="white", mew=0.8, zorder=5)
            ax.plot([at[0]], [at[1] + 0.17], "x", ms=5, mec="white",
                    mew=1.4, zorder=6)
    pad = 0.3
    ax.set_xlim(min(xs) - pad, max(xs) + pad)
    ax.set_ylim(min(ys) - pad, max(ys) + pad)
    ax.set_aspect("equal")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", facecolor="white")
    plt.close(fig)
    return buf.getvalue()


def _swatch(rgb_hex):
    return '<span class="sw" style="background:%s"></span>' % rgb_hex


def _famine_svg():
    r, g, b = FAMINE_SYMBOL_RGB
    return ('<svg width="18" height="16" viewBox="0 0 18 16" '
            'style="vertical-align:-3px;margin-right:6px" aria-hidden="true">'
            '<polygon points="9,1 17,15 1,15" fill="rgb(%d,%d,%d)" '
            'stroke="#fff" stroke-width="1"/><path d="M6.5,8.5 L11.5,13.5 '
            'M11.5,8.5 L6.5,13.5" stroke="#fff" stroke-width="1.8"/></svg>'
            % (r, g, b))


def build_short_page_html(joined, picture_file):
    """Sudan's short page: the title; the three periods by IPC's names and
    dates; each phase with its colour in words and the 20-percent rule; the
    projections' coverage line; how this map relates to IPC's; IPC's credit
    and citation; one button to the Google Earth project; the still picture.
    Every number is a sourced constant or read from the data."""
    meta = joined["meta"]
    e = _x
    pic_label = _period_label(PAGE_PERIOD)
    parts = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, '
        'initial-scale=1, viewport-fit=cover">\n'
        "<title>Sudan: acute food insecurity (IPC) - Paloma's Orrery</title>\n"
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+'
        'Garamond:wght@600&family=DM+Sans:wght@400;600&display=swap" '
        'rel="stylesheet">\n'
        "<style>%s</style>\n</head>\n<body>\n<main>\n" % PAGE_CSS,
        '<a class="back" href="/">&larr; Paloma\'s Orrery</a>\n',
        "<h1>Sudan &mdash; Acute Food Insecurity</h1>\n",
        '<p class="sub">IPC&#39;s analysis of Sudan, three periods, on '
        "Google Earth</p>\n",
        '<figure><img src="%s" alt="%s"><figcaption>%s, drawn from IPC\'s '
        "data.</figcaption></figure>\n"
        % (e(picture_file),
           e("Map of Sudan for %s: areas colored by IPC phase, white where "
             "not analyzed, camps as circles, dark red dots for Phase 5 "
             "(Catastrophe) and IPC's Risk of Famine symbol." % pic_label),
           e(pic_label)),
        '<a class="go" href="%s" target="_blank" rel="noopener">Open the map '
        "in Google Earth</a>\n" % e(GE_PROJECT_URL),
        '<p class="note">It opens in a new tab, on %s. Switch a period\'s '
        "folder on to see it.</p>\n" % e(pic_label),
        "<h2>Three periods</h2>\n<ul>\n",
    ]
    for code in ["current", "projected-1", "projected-2"]:
        parts.append("<li>%s</li>\n" % e(_period_label(code)))
    parts.append("</ul>\n")
    parts.append('<p class="note">%s</p>\n<p class="note">%s</p>\n'
                 % (e(COVERAGE_LINE), e(COMPARE_CAUTION)))

    parts.append("<h2>What the colors mean</h2>\n<ul class=\"key\">\n")
    for pv in range(1, 6):
        parts.append("<li>%sPhase %d %s: %s</li>\n" % (
            _swatch(PHASE_COLORS_RGB[pv]), pv,
            e("Famine / Catastrophe" if pv == 5 else PHASE_LABELS[pv]),
            e(PHASE_COLOR_WORDS[pv])))
    parts.append("<li>%sNot analyzed: white</li>\n" % _swatch(NOT_ANALYSED_RGB))
    parts.append("<li>%s%s</li>\n" % (_famine_svg(), e(FAMINE_LEGEND_LINE)))
    parts.append("<li>Small circles: IDP settlements (camps for internally "
                 "displaced people), in their phase color</li>\n")
    parts.append("<li>Dark red dots: people in Phase 5 (Catastrophe); a "
                 "larger dot means more people</li>\n</ul>\n")
    parts.append("<p>%s</p>\n" % e(TWENTY_PCT_RULE))

    parts.append("<h2>How this map relates to IPC&#39;s</h2>\n")
    parts.append("<p>%s</p>\n" % e(RELATION_IPC_OWN))
    parts.append("<p>This map adds:</p>\n<ul>\n")
    for s in RELATION_ADDED:
        parts.append("<li>%s</li>\n" % e(s))
    parts.append("</ul>\n<p>It does not show:</p>\n<ul>\n")
    for s in RELATION_NOT_SHOWN:
        parts.append("<li>%s</li>\n" % e(s))
    parts.append('</ul>\n<p>%s <a href="%s" target="_blank" rel="noopener">'
                 "IPC&#39;s map of Sudan</a>.</p>\n"
                 % (e(RELATION_AUTHORITY), e(IPC_MAP_URL)))

    parts.append('<div class="src"><div>Source: %s</div><div>%s</div>'
                 "<div>Analysis: %s</div><div>Data retrieved: %s</div>"
                 "<div>%s</div></div>\n"
                 % (e(PROVENANCE_DATA), e(CITATION), e(meta["analysis_name"]),
                    e(meta["export_date"]), e(CAUSAL_RESTRAINT)))
    parts.append("</main>\n</body>\n</html>\n")
    return "".join(parts)


# Where an Earth System layer's one-home page lives (Tony's ruling of Nov 13,
# 2026): a folder of its own at the website's top level, earth/, with the
# page and its picture side by side, both named by the layer's scenario id --
# earth/<scenario_id>.html and earth/<scenario_id>.png -- the same stable id
# that names its KMZ (<scenario_id>_blockbuster.kmz). Every later layer
# follows the same pattern. The generator writes them into data/earth/, the
# same layout, so the folder is copied to the website as it is.
PAGE_FOLDER = "earth"


def write_short_page(joined):
    """Write the page and its picture into data/earth/ as
    <scenario_id>.html and <scenario_id>.png. Returns the two paths."""
    folder = os.path.join(DATA_DIR, PAGE_FOLDER)
    if not os.path.exists(folder):
        os.makedirs(folder)
    pic_name = "%s.png" % SCENARIO_ID
    page_path = os.path.join(folder, "%s.html" % SCENARIO_ID)
    pic_path = os.path.join(folder, pic_name)
    with open(pic_path, "wb") as f:
        f.write(page_picture_png(joined))
    with open(page_path, "wb") as f:
        # ASCII on disk: a character from IPC's data (an en dash in the
        # analysis name) is written as an HTML character reference.
        f.write(build_short_page_html(joined, pic_name).encode(
            "ascii", "xmlcharrefreplace"))
    return page_path, pic_path


# ==========================================================================
#   OPTIONAL PLOTLY TEASER (web gallery; guarded so KMZ never depends on it)
# ==========================================================================

def generate_plotly_teaser(records, meta):
    """2D choropleth teaser for the web gallery. Returns path or None."""
    try:
        import plotly.graph_objects as go
    except Exception:
        print("plotly not available; skipping teaser.")
        return None

    feats = []
    for i, rec in enumerate(records):
        feats.append({"type": "Feature", "id": i,
                      "geometry": rec["geometry"], "properties": {}})
    fc = {"type": "FeatureCollection", "features": feats}

    ids, z, text = [], [], []
    for i, rec in enumerate(records):
        pv = rec["phase_value"]
        ids.append(i)
        z.append(pv if pv is not None else 0)
        p5 = _intpop(rec["phase_pop"].get(5))
        text.append("%s<br>Mapped: %s<br>Phase 5 (Catastrophe): %s"
                    % (rec["area_name"],
                       "Not analyzed" if pv is None else "Phase %s" % pv, p5))

    colorscale = [
        [0.0, NOT_ANALYSED_RGB], [0.124, NOT_ANALYSED_RGB],
        [0.125, PHASE_COLORS_RGB[1]], [0.30, PHASE_COLORS_RGB[1]],
        [0.30, PHASE_COLORS_RGB[2]], [0.50, PHASE_COLORS_RGB[2]],
        [0.50, PHASE_COLORS_RGB[3]], [0.70, PHASE_COLORS_RGB[3]],
        [0.70, PHASE_COLORS_RGB[4]], [0.90, PHASE_COLORS_RGB[4]],
        [0.90, PHASE_COLORS_RGB[5]], [1.0, PHASE_COLORS_RGB[5]],
    ]
    fig = go.Figure(go.Choroplethmapbox(
        geojson=fc, locations=ids, z=z, zmin=0, zmax=4,
        colorscale=colorscale, marker_opacity=0.8, marker_line_width=0.4,
        text=text, hoverinfo="text", showscale=False))
    fig.update_layout(
        mapbox_style="carto-positron", mapbox_zoom=4.4,
        mapbox_center={"lat": 15.5, "lon": 30.0},
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        title="Sudan: IPC Acute Food Insecurity -- %s" % PERIOD_LABEL)
    out = os.path.join(DATA_DIR, "%s_teaser.html" % SCENARIO_ID)
    fig.write_html(out, include_plotlyjs="cdn")
    return out


# ==========================================================================
#   ENTRY POINT
# ==========================================================================

def check_web_kmz(kmz_path):
    """The KMZ byte checks for Google Earth on the web. Prints what it
    examined and raises ValueError, naming each failure, if any rule fails:
      - no Style inside a Folder (every Style a child of the Document);
      - no ScreenOverlay;
      - no <table> and no <br> in any description;
      - every styleUrl resolves to a Document-level Style id;
      - the period folders in FOLDER_ORDER, visibility 1/0/0.
    Prints the areas per period by phase name. Returns the counts.
    """
    import xml.etree.ElementTree as ET
    ns = {"k": "http://www.opengis.net/kml/2.2"}
    with zipfile.ZipFile(kmz_path) as zf:
        names = zf.namelist()
        raw = zf.read("doc.kml")
    root = ET.fromstring(raw)
    doc = root.find("k:Document", ns)
    failures = []

    doc_styles = {st.get("id") for st in doc.findall("k:Style", ns)}
    all_styles = root.findall(".//k:Style", ns)
    nested = len(all_styles) - len(doc_styles)
    if nested:
        failures.append("%d Style element(s) not at Document level" % nested)
    n_overlay = len(root.findall(".//k:ScreenOverlay", ns))
    if n_overlay:
        failures.append("%d ScreenOverlay element(s)" % n_overlay)
    descs = [d.text or "" for d in root.iter("{%s}description" % ns["k"])]
    bad_desc = [d for d in descs
                if "<table" in d.lower() or "<br" in d.lower()]
    if bad_desc:
        failures.append("%d description(s) with <table> or <br>"
                        % len(bad_desc))
    urls = [u.text for u in root.iter("{%s}styleUrl" % ns["k"])]
    unresolved = sorted({u for u in urls
                         if not u or u.lstrip("#") not in doc_styles})
    if unresolved:
        failures.append("styleUrl not resolved: %s" % unresolved)

    top = doc.findall("k:Folder", ns)
    period_names = [_period_label(c) for c in FOLDER_ORDER]
    periods = [f for f in top if f.findtext("k:name", "", ns) in period_names]
    got = [(f.findtext("k:name", "", ns), f.findtext("k:visibility", "1", ns))
           for f in periods]
    want = [(_period_label(c), "1" if c == OPEN_PERIOD else "0")
            for c in FOLDER_ORDER]
    if got != want:
        failures.append("period folders %s, expected %s" % (got, want))

    counts = {}
    for f in periods:
        tally = {}
        for pm in f.iter("{%s}Placemark" % ns["k"]):
            sid = (pm.findtext("k:styleUrl", "", ns) or "").lstrip("#")
            if sid == "famine_risk":
                key = "Risk of Famine symbol"
            elif sid.startswith("p5dot_"):
                key = "Phase 5 dot"
            elif sid.endswith("not_analysed"):
                key = "Not analyzed"
            elif sid[-1:].isdigit() and int(sid[-1]) in PHASE_LABELS:
                pv = int(sid[-1])
                key = "Phase %d %s" % (pv, PHASE_LABELS[pv])
            else:
                key = "Unknown style %r" % sid
            if sid.startswith("camp_"):
                key += " (camp)"
            tally[key] = tally.get(key, 0) + 1
        counts[f.findtext("k:name", "", ns)] = tally

    print("KMZ check: %s (%d bytes, files %s)" % (kmz_path,
                                                   os.path.getsize(kmz_path),
                                                   names))
    print("  Document styles: %d; Styles anywhere: %d; ScreenOverlays: %d"
          % (len(doc_styles), len(all_styles), n_overlay))
    print("  descriptions examined: %d; with <table> or <br>: %d"
          % (len(descs), len(bad_desc)))
    print("  styleUrls examined: %d; unresolved: %d"
          % (len(urls), len(unresolved)))
    for name, vis in got:
        print("  folder %r visibility %s" % (name, vis))
        for key in sorted(counts[name]):
            print("    %-28s %d" % (key, counts[name][key]))
    for code in FOLDER_ORDER:
        got_n = counts.get(_period_label(code), {}).get(
            "Risk of Famine symbol", 0)
        want_n = FAMINE_RISK_COUNTS.get(code, 0)
        if got_n != want_n:
            failures.append("%s: %d Risk of Famine symbols, the report "
                            "counts %d" % (_period_label(code), got_n, want_n))
    hrefs = [h.text or "" for h in root.iter("{%s}href" % ns["k"])]
    local = sorted({h for h in hrefs if not h.startswith("http")})
    missing = [h for h in local if h not in names]
    if missing:
        failures.append("icon file(s) not in the KMZ: %s" % missing)
    print("  icons packed in the KMZ: %s; missing: %d" % (local, len(missing)))
    if failures:
        raise ValueError("KMZ check failed:\n  " + "\n  ".join(failures))
    print("  KMZ check passed.")
    return counts


def run(geojson_path=DEFAULT_GEOJSON, make_teaser=True, status_callback=None,
        scenario_id=None, excel_path=DEFAULT_EXCEL):
    # Output files are named by SCENARIO_ID (<id>_blockbuster.kmz,
    # <id>_teaser.html). A picker passes the selected scenario's id so a future
    # country writes its own files; calling run() directly keeps the Sudan
    # default. One scenario per process, so setting the module value here is safe.
    if scenario_id:
        global SCENARIO_ID
        SCENARIO_ID = scenario_id

    def _status(msg):
        if status_callback:
            status_callback(msg)
        print(msg)

    for path, what in ((geojson_path, "GeoJSON"), (excel_path, "Excel")):
        if not os.path.exists(path):
            raise FileNotFoundError(
                "IPC %s not found: %s\nPlace the IPC Mapping Tool export in "
                "data/." % (what, path))

    _status("Joining the IPC Excel (three periods) to the GeoJSON outlines...")
    joined = join_ipc_periods(excel_path, geojson_path)
    _status("Joined %d areas (%d camps); analyzed: %s." % (
        len(joined["areas"]), len(joined["camps"]),
        ", ".join("%s %d" % (lbl, len(joined["analysed"][c]))
                  for c, _p, lbl, *_d in IPC_PERIODS)))

    _status("Building KMZ...")
    kmz_path = package_kmz(build_web_kml(joined))
    _status("KMZ written: %s" % kmz_path)
    check_web_kmz(kmz_path)
    page_path, pic_path = write_short_page(joined)
    _status("Short page written: %s (picture %s)" % (page_path, pic_path))

    teaser_path = None
    if make_teaser:
        _status("Building Plotly teaser...")
        records, meta = build_geojson_records(geojson_path)
        teaser_path = generate_plotly_teaser(records, meta)
        if teaser_path:
            _status("Teaser written: %s" % teaser_path)

    return {"kmz": kmz_path, "teaser": teaser_path, "page": page_path,
            "picture": pic_path, "areas": len(joined["areas"])}


def _food_run(scenario, status_callback=None):
    """Adapter so the shared ScenarioPicker can drive run(): maps a scenario
    dict to run()'s geojson_path, excel_path and scenario_id."""
    return run(geojson_path=scenario.get("geojson", DEFAULT_GEOJSON),
               excel_path=scenario.get("excel", DEFAULT_EXCEL),
               status_callback=status_callback,
               scenario_id=scenario.get("scenario_id"))


if __name__ == "__main__":
    from scenarios_food_insecurity import SCENARIOS
    ScenarioPicker(SCENARIOS, _food_run,
                   title="Food Insecurity Generator",
                   button_text="Generate KMZ (+ teaser) in data/").mainloop()
