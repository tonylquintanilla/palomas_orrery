"""
food_insecurity_generator.py - IPC acute food-insecurity KMZ layer (Sudan, current period).

Dedicated vector/categorical generator for the Earth System family. Reads an
IPC Mapping Tool GeoJSON (one polygon per analysis area, full per-area phase
attributes) and renders a dated, no-key KMZ: per-area choropleth by mapped IPC
phase, a full phase1-5 breakdown in every balloon (so sub-20% Catastrophe never
hides behind a Phase-4 color), a transcribed national drivers card, and framing
text whose numeric tokens are sourced at the construction site for the
provenance scanner. Mirrors the family's single-doc KMZ + ScreenOverlay-card
conventions (earth_system_generator.py) without importing the scalar engine,
because this layer is categorical polygons, not a gridded scalar field.

Stance (from MANIFEST_food_insecurity_sudan_v2.md): synthesize nothing,
transcribe everything, attribute to IPC, defer causation to the reader.
National totals are TRANSCRIBED from the IPC report, NEVER summed from polygons.

Key functions:
    run() - end-to-end: parse GeoJSON -> build KMZ (+ optional Plotly teaser).
    build_food_insecurity_kml() - the per-area placemarks + styles + framing.
    build_geojson_records() - parse the IPC GeoJSON into per-area records.

Consumed by: Earth System GUI (registration snippet in the build handoff);
runnable standalone via __main__.

Module updated: June 2026 with Anthropic's Claude Opus 4.8
"""
import os
import re
import json
import math
import zipfile

import simplekml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

DATA_DIR = "data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

SCENARIO_ID = "food_insecurity_sdn"
DEFAULT_GEOJSON = os.path.join(DATA_DIR, "IPC_SD_A_87143417_2026-06-22.geojson")

# ==========================================================================
#   SOURCED CONSTANTS -- every numeric/quoted claim carries a # Source: within
#   the provenance scanner's 60-line lookback. Transcribe, do not recall.
# ==========================================================================

# --- IPC phase ramp -------------------------------------------------------
# IPC carries no color in the GeoJSON; these RGB values were SAMPLED from the
# report's own "Key for the Map" legend swatches (a true in-document source),
# so they are the colors IPC used in THIS report rather than recalled hex.
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027 (publ. 2026-06-03),
#   page 7 "Key for the Map / IPC Acute Food Insecurity Phase Classification"
#   legend swatches, sampled at 200 dpi (anti-alias +/-2; see build handoff).
PHASE_COLORS_RGB = {
    1: "#D0E7C7",   # Phase 1 - Minimal     (light green)
    2: "#F8E303",   # Phase 2 - Stressed    (yellow)
    3: "#E27826",   # Phase 3 - Crisis      (orange)
    4: "#C52127",   # Phase 4 - Emergency   (red)
    5: "#621012",   # Phase 5 - Famine/Catastrophe (dark red)
}
# Source: same legend, page 7 -- "Areas not analysed" (white) and "Areas with
#   inadequate evidence" (grey) are distinct legend categories, not a phase.
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
#   (Feb-May 2026): "covering the total population of Sudan (47.5 million)";
#   "nearly 19.5 million people are classified in IPC Phase 3 or above for the
#   current period, including over 5 million people in IPC Phase 4 (Emergency)";
#   "nearly 135,000 people are classified in IPC Phase 5 (Catastrophe)".
NATL_TOTAL_POP = "47.5 million"         # total population of Sudan analysed
NATL_PHASE3PLUS = "19.5 million"        # IPC Phase 3 or above, current period
NATL_PHASE4 = "5 million"               # IPC Phase 4 (Emergency), current period
NATL_PHASE5_CATASTROPHE = "135,000"     # IPC Phase 5 (Catastrophe), current period

# IPC's OWN wording of the mapped-phase rule (transcribed verbatim -> safe tier).
# Source: IPC Sudan Special Report page 7 legend, "Key for the Map": "mapped
#   Phase represents highest severity affecting at least 20% of the population".
TWENTY_PCT_RULE = ("The mapped phase is the highest severity affecting at least "
                   "20% of an area's population. A smaller Catastrophe population "
                   "can sit under a Phase 4 color -- the full breakdown in each "
                   "balloon shows it.")
# The first clause above is IPC's verbatim legend wording; the second sentence
# is COMPOSED (ours) and explains the reveal. Numeric token (20%):
# Source: IPC Sudan Special Report page 7 legend wording (above).

# --- KEY DRIVERS (transcribed verbatim from the report; IPC's voice only) ---
# Source: IPC Sudan Special Report, Feb 2026-Jan 2027, "KEY DRIVERS" section
#   (page 6). Wording lifted verbatim; smart quotes/dashes normalized to ASCII.
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
#   ongoing conflict in the Middle East "contributing to higher fuel, food, and
#   fertilizer prices. The impacts of the Middle East crisis on Sudan are likely
#   to intensify in the near and medium term."
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
#   Food Insecurity Analysis February 2026-January 2027"; published 3 June 2026).
CITATION = ("IPC Global Initiative. 2026. Sudan: IPC Acute Food Insecurity "
            "Analysis, February 2026 - January 2027 (Special Report). "
            "Published 3 June 2026.")

PERIOD_LABEL = "Current (February - May 2026)"


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
            "phase_value": p.get("overall_phase_value"),  # None for not-analysed
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
#   BALLOON (full phase1-5 breakdown -- the structural fix)
# ==========================================================================

def build_balloon_html(rec, retrieved, analysis_name=""):
    """Per-area CDATA HTML balloon. All fields transcribed; none synthesized.

    The full phase1-5 split (including phase5_population) is mandatory: where a
    P4-mapped area carries a Phase-5 population, that line is the hidden
    Catastrophe made visible.
    """
    pv = rec["phase_value"]
    if pv is None:
        mapped = "Not analysed"
    else:
        mapped = "Phase %s (%s)" % (pv, PHASE_LABELS.get(pv, rec.get("phase_label", "")))

    rows = ""
    for i in range(1, 6):
        rows += (
            "<tr><td>Phase %d %s</td><td align='right'>%s</td>"
            "<td align='right'>%s%%</td></tr>"
            % (i, PHASE_LABELS[i], _intpop(rec["phase_pop"].get(i)),
               _pct(rec["phase_pct"].get(i)))
        )

    html = (
        "<![CDATA["
        "<div style='font-family:Arial,sans-serif;font-size:12px;width:320px'>"
        "<h3 style='margin:2px 0'>%(name)s</h3>"
        "<b>Mapped IPC Phase:</b> %(mapped)s<br>"
        "<b>Period:</b> %(period)s<br>"
        "<b>Population (area):</b> %(pop)s<br>"
        "<table style='border-collapse:collapse;width:100%%;margin-top:4px'>"
        "<tr><th align='left'>Phase breakdown</th><th align='right'>people</th>"
        "<th align='right'>%%</th></tr>%(rows)s</table>"
        "<b>Phase 3+ (Crisis or worse):</b> %(p3plus)s (%(p3pct)s%%)<br>"
        "<b>Evidence level (IPC):</b> %(conf)s<br>"
        "<b>Assistance (HFA) level:</b> %(hfa)s<br>"
        "<hr style='border:none;border-top:1px solid #ccc;margin:4px 0'>"
        "<span style='font-size:10px;color:#555'>"
        "Analysis: %(analysis)s<br>"
        "Source: %(prov)s<br>"
        "Data retrieved: %(retrieved)s</span>"
        "</div>"
        "]]>"
    ) % {
        "name": rec["area_name"],
        "mapped": mapped,
        "period": PERIOD_LABEL,
        "pop": _intpop(rec["population"]),
        "rows": rows,
        "p3plus": _intpop(rec["p3plus_pop"]),
        "p3pct": _pct(rec["p3plus_pct"]),
        "conf": rec["confidence_level"] if rec["confidence_level"] is not None else "-",
        "hfa": rec["hfa_value"] if rec["hfa_value"] is not None else "-",
        "analysis": analysis_name,
        "prov": PROVENANCE_DATA,
        "retrieved": retrieved,
    }
    # analysis_name belongs to the file meta, injected by caller via .replace
    return html


# ==========================================================================
#   FRAMING-LAYER TEXT (composed/transcribed C1/C2/C3) and CARDS
# ==========================================================================

def compose_framing_text():
    """Return the framing-layer sentences. Numeric tokens are sourced above
    (NATL_* constants, TWENTY_PCT_RULE) within scanner lookback.

    C1 -- mapped-vs-population reconciliation (the hidden Catastrophe).
    C2 -- the >=20% mapped-phase rule (IPC verbatim clause).
    C3 -- causal-restraint statement.
    """
    # C1: numbers transcribed from the report (see NATL_* sourcing above).
    c1 = ("No area is mapped Phase 5 (Famine), but about %s people are in "
          "Phase 5 (Catastrophe), concentrated in North Darfur, South Darfur "
          "and South Kordofan." % NATL_PHASE5_CATASTROPHE)
    c2 = TWENTY_PCT_RULE
    c3 = CAUSAL_RESTRAINT
    national = ("Sudan, current period (February - May 2026): of %s people "
                "analysed, about %s are in IPC Phase 3 or above (Crisis or "
                "worse), including over %s in Phase 4 (Emergency)."
                % (NATL_TOTAL_POP, NATL_PHASE3PLUS, NATL_PHASE4))
    return {"national": national, "c1": c1, "c2": c2, "c3": c3}


def create_legend_card(p5_min=None, p5_max=None):
    """Phase ramp + >=20% rule + (if provided) the Phase 5 dot-size key.

    The dot-size key shows what a large vs small maroon dot means. Its values
    (p5_min/p5_max) are the actual range of phase5_population in the data, passed
    in at runtime -- nothing here is hardcoded or recalled.
    """
    fig = plt.figure(figsize=(2.7, 4.7), dpi=130)
    fig.patch.set_facecolor("white")
    fig.patch.set_alpha(0.9)
    ax = fig.add_subplot(111)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)

    ax.text(0.2, 15.4, "IPC Acute Food Insecurity", fontweight="bold", fontsize=8)
    ax.text(0.2, 14.8, "Phase Classification", fontsize=7.5)

    rows = [(5, "5  Famine / Catastrophe", PHASE_COLORS_RGB[5]),
            (4, "4  Emergency", PHASE_COLORS_RGB[4]),
            (3, "3  Crisis", PHASE_COLORS_RGB[3]),
            (2, "2  Stressed", PHASE_COLORS_RGB[2]),
            (1, "1  Minimal", PHASE_COLORS_RGB[1]),
            (0, "Not analysed", NOT_ANALYSED_RGB)]
    y = 13.6
    for _, label, color in rows:
        ax.add_patch(mpatches.Rectangle((0.3, y - 0.35), 1.0, 0.7,
                                        facecolor=color, edgecolor="#888"))
        ax.text(1.6, y, label, fontsize=7.5, va="center")
        y -= 1.15

    rule = ("Mapped phase = highest severity\naffecting at least 20% of an\n"
            "area's population.")
    ax.text(0.2, 5.6, rule, fontsize=6.5, va="top", color="#333")

    # Phase 5 (Catastrophe) dot-size key -- only if a range was supplied.
    if p5_min is not None and p5_max is not None and p5_max > 0:
        ax.plot([0.2, 9.8], [3.7, 3.7], color="#bbb", lw=0.6)
        ax.text(0.2, 3.4, "Phase 5 (Catastrophe) population",
                fontweight="bold", fontsize=7, va="top")
        ax.text(0.2, 2.95, "maroon dot, by area; larger = more people",
                fontsize=6.2, va="top", color="#333")
        dot_color = PHASE_COLORS_RGB[5]
        # radii echo the map's sqrt sizing (large vs small), purely visual
        r_big, r_small = 0.62, 0.62 * (P5_DOT_MIN_SCALE / P5_DOT_MAX_SCALE) ** 0.5
        ax.add_patch(mpatches.Circle((1.1, 1.4), r_big, facecolor=dot_color,
                                     edgecolor="white", lw=0.5))
        ax.add_patch(mpatches.Circle((3.4, 1.15), r_small, facecolor=dot_color,
                                     edgecolor="white", lw=0.5))
        ax.text(2.0, 1.4, "{:,}".format(int(round(p5_max))),
                fontsize=6.5, va="center", color="#222")
        ax.text(4.1, 1.15, "{:,}".format(int(round(p5_min))),
                fontsize=6.5, va="center", color="#222")
        ax.text(0.2, 0.2, "people in Phase 5 (Catastrophe)",
                fontsize=6.0, va="top", color="#555")

    path = os.path.join(DATA_DIR, "legend_%s.png" % SCENARIO_ID)
    plt.savefig(path, bbox_inches="tight", pad_inches=0.08, transparent=False)
    plt.close()
    return path


def create_intel_card(framing):
    """National figures + C1 + drivers + Middle East + C3 + citation (PNG)."""
    fig = plt.figure(figsize=(4.3, 5.2), dpi=130)
    fig.patch.set_facecolor("#f8f9fa")
    fig.patch.set_alpha(0.92)
    ax = fig.add_subplot(111)
    ax.axis("off")

    import textwrap
    blocks = []
    blocks.append(("SUDAN -- ACUTE FOOD INSECURITY", "title"))
    blocks.append((PERIOD_LABEL, "sub"))
    blocks.append((framing["national"], "body"))
    blocks.append((framing["c1"], "body"))
    blocks.append(("KEY DRIVERS (IPC):", "head"))
    for name, _text in DRIVERS:
        blocks.append(("- " + name, "bullet"))
    blocks.append((MIDDLE_EAST_LINE, "body"))
    blocks.append((framing["c3"], "italic"))
    blocks.append(("Source: " + PROVENANCE_DATA, "src"))
    blocks.append((CITATION, "src"))

    y = 0.98
    for text, kind in blocks:
        if kind == "title":
            ax.text(0.04, y, text, transform=ax.transAxes, fontsize=10,
                    fontweight="bold", color="#222", va="top")
            y -= 0.045
        elif kind == "sub":
            ax.text(0.04, y, text, transform=ax.transAxes, fontsize=8,
                    fontfamily="monospace", color="#555", va="top")
            y -= 0.05
        elif kind == "head":
            ax.text(0.04, y, text, transform=ax.transAxes, fontsize=8.5,
                    fontweight="bold", color="#333", va="top")
            y -= 0.035
        elif kind == "bullet":
            ax.text(0.06, y, text, transform=ax.transAxes, fontsize=7.5,
                    color="#222", va="top")
            y -= 0.03
        elif kind == "italic":
            for line in textwrap.wrap(text, 62):
                ax.text(0.04, y, line, transform=ax.transAxes, fontsize=7,
                        color="#555", style="italic", va="top")
                y -= 0.027
            y -= 0.01
        elif kind == "src":
            for line in textwrap.wrap(text, 64):
                ax.text(0.04, y, line, transform=ax.transAxes, fontsize=6,
                        color="#777", va="top")
                y -= 0.024
        else:  # body
            for line in textwrap.wrap(text, 60):
                ax.text(0.04, y, line, transform=ax.transAxes, fontsize=7.5,
                        color="#222", va="top")
                y -= 0.029
            y -= 0.01

    path = os.path.join(DATA_DIR, "intel_%s.png" % SCENARIO_ID)
    plt.savefig(path, bbox_inches="tight", pad_inches=0.1, transparent=False)
    plt.close()
    return path


# ==========================================================================
#   KML / KMZ BUILD
# ==========================================================================

def _add_screenoverlay(kml, png_path, sx, sy, ox, oy, size_x):
    so = kml.newscreenoverlay(name=os.path.basename(png_path))
    so.icon.href = os.path.basename(png_path)
    so.overlayxy = simplekml.OverlayXY(x=ox, y=oy,
                                       xunits=simplekml.Units.fraction,
                                       yunits=simplekml.Units.fraction)
    so.screenxy = simplekml.ScreenXY(x=sx, y=sy,
                                     xunits=simplekml.Units.fraction,
                                     yunits=simplekml.Units.fraction)
    so.size = simplekml.Size(x=size_x, y=0,
                             xunits=simplekml.Units.fraction,
                             yunits=simplekml.Units.fraction)


def _phase_style(phase_value):
    style = simplekml.Style()
    if phase_value is None or phase_value not in PHASE_COLORS_RGB:
        fill = rgb_to_kml(NOT_ANALYSED_RGB, "66")   # white, semi -> reads as "no data"
        line = rgb_to_kml(LINE_RGB, "FF")
    else:
        fill = rgb_to_kml(PHASE_COLORS_RGB[phase_value], POLY_FILL_ALPHA)
        line = rgb_to_kml(LINE_RGB, POLY_LINE_ALPHA)
    style.polystyle.color = fill
    style.polystyle.fill = 1
    style.polystyle.outline = 1
    style.linestyle.color = line
    style.linestyle.width = 1
    return style


def build_phase5_dots(records, document, retrieved, analysis_name=""):
    """L-069: maroon proportional dots for areas carrying a mapped Phase 5
    (Catastrophe) population. Pure IPC passthrough -- every displayed value is
    read from the GeoJSON record at runtime; nothing here is hardcoded or summed.
    Returned in their own folder so Google Earth toggles them as a group.

    "Catastrophe" is IPC's population-level term; these areas are mapped Phase 4
    (Emergency), and none is classified Famine (an area-level term). The label
    "Famine" therefore appears nowhere on these dots, by design.

    Module section updated: June 2026 with Anthropic's Claude Opus 4.8.
    """
    import math
    p5_records = [r for r in records if (r["phase_pop"].get(5) or 0) > 0]
    if not p5_records:
        return
    max_p5 = max(float(r["phase_pop"][5]) for r in p5_records)
    span = P5_DOT_MAX_SCALE - P5_DOT_MIN_SCALE
    dot_kml_color = rgb_to_kml(P5_DOT_RGB, "FF")

    fol = document.newfolder(name="Phase 5 (Catastrophe) populations (area level)")
    for rec in sorted(p5_records, key=lambda r: -float(r["phase_pop"][5])):
        p5 = float(rec["phase_pop"][5])
        lon, lat = _representative_point(rec["geometry"])
        # area ~ population: scale the icon by sqrt of the population fraction
        scale = (P5_DOT_MIN_SCALE + span * math.sqrt(p5 / max_p5)
                 if max_p5 else P5_DOT_MIN_SCALE)

        pv = rec["phase_value"]
        mapped = "Phase %s (%s)" % (pv, PHASE_LABELS.get(pv, rec.get("phase_label", "")))

        # Balloon: IPC fields only, read at runtime. No hardcoded/summed numbers.
        balloon = (
            "<![CDATA["
            "<div style='font-family:Arial,sans-serif;font-size:12px;width:300px'>"
            "<h3 style='margin:2px 0'>%(name)s</h3>"
            "<b>Mapped IPC Phase:</b> %(mapped)s<br>"
            "<b>In Phase 5 (Catastrophe):</b> %(p5)s people (%(p5pct)s%% of area)<br>"
            "<b>Area population:</b> %(pop)s<br>"
            "<hr style='border:none;border-top:1px solid #ccc;margin:4px 0'>"
            "<span style='font-size:10px;color:#555'>"
            "Analysis: %(analysis)s<br>Source: %(prov)s<br>"
            "Data retrieved: %(retrieved)s</span></div>]]>"
        ) % {
            "name": rec["area_name"],
            "mapped": mapped,
            "p5": _intpop(rec["phase_pop"].get(5)),
            "p5pct": _pct(rec["phase_pct"].get(5)),
            "pop": _intpop(rec["population"]),
            "analysis": analysis_name,
            "prov": PROVENANCE_DATA,
            "retrieved": retrieved,
        }

        pt = fol.newpoint(name=rec["area_name"])
        pt.coords = [(lon, lat)]
        pt.style.iconstyle.icon.href = P5_DOT_ICON
        pt.style.iconstyle.color = dot_kml_color
        pt.style.iconstyle.scale = round(scale, 3)
        pt.style.labelstyle.scale = 0  # name on click, not as map clutter
        pt.description = balloon


def build_food_insecurity_kml(records, meta):
    """Build the KML doc: phase styles, per-area placemarks, framing, cards."""
    retrieved = (meta.get("export_timestamp") or "")[:10] or "IPC Mapping Tool"
    framing = compose_framing_text()

    kml = simplekml.Kml()
    kml.document.name = "Sudan Food Insecurity (IPC) -- %s" % PERIOD_LABEL

    folder = kml.document.newfolder(name=PERIOD_LABEL)

    for rec in records:
        style = _phase_style(rec["phase_value"])
        geom = rec["geometry"]
        balloon = build_balloon_html(rec, retrieved,
                                     analysis_name=meta.get("analysis_name", ""))

        if geom["type"] == "Polygon":
            outer, holes = _rings_from_polygon(geom["coordinates"])
            pol = folder.newpolygon(name=rec["area_name"])
            pol.outerboundaryis = outer
            for h in holes:
                pol.innerboundaryis = h
            pol.style = style
            pol.description = balloon
            pol.tessellate = 1
        else:  # MultiPolygon -> one placemark, shared style + balloon
            mg = folder.newmultigeometry(name=rec["area_name"])
            for poly_coords in geom["coordinates"]:
                outer, holes = _rings_from_polygon(poly_coords)
                p = mg.newpolygon()
                p.outerboundaryis = outer
                for h in holes:
                    p.innerboundaryis = h
                p.tessellate = 1
            mg.style = style
            mg.description = balloon

    # L-069: Phase 5 (Catastrophe) population dots (pure IPC passthrough).
    build_phase5_dots(records, kml.document, retrieved,
                      analysis_name=meta.get("analysis_name", ""))

    # Framing-layer text as a KML folder of description-only placemarks (the
    # words on the layer; the sourced numbers live at the construction site).
    fr = kml.document.newfolder(name="Framing (read this first)")
    for key, title in (("national", "National summary"),
                       ("c1", "The hidden Catastrophe"),
                       ("c2", "What the map color means"),
                       ("c3", "What this layer does not assert")):
        ph = fr.newpoint(name=title)
        ph.description = "<![CDATA[<div style='font-family:Arial;font-size:12px;"
        ph.description += "width:300px'>%s</div>]]>" % framing[key]
        ph.style.iconstyle.scale = 0
        ph.coords = [(32.5, 15.5)]  # near Khartoum; label only

    # Cards as ScreenOverlays (family convention).
    p5_vals = [float(r["phase_pop"][5]) for r in records
               if (r["phase_pop"].get(5) or 0) > 0]
    legend_png = create_legend_card(
        p5_min=min(p5_vals) if p5_vals else None,
        p5_max=max(p5_vals) if p5_vals else None)
    intel_png = create_intel_card(framing)
    _add_screenoverlay(kml, legend_png, sx=0.98, sy=0.05, ox=1, oy=0, size_x=0.16)
    _add_screenoverlay(kml, intel_png, sx=0.02, sy=0.98, ox=0, oy=1, size_x=0.30)

    return kml, [legend_png, intel_png]


def package_kmz(kml, asset_pngs):
    """Write the KMZ: a single doc.kml plus the card PNGs.

    Mirrors earth_system_generator.package_and_cleanup's single-doc approach so
    Google Earth loads every layer (it reads only the first KML in an archive).
    """
    kml_str = kml.kml()
    kmz_path = os.path.join(DATA_DIR, "%s_blockbuster.kmz" % SCENARIO_ID)
    with zipfile.ZipFile(kmz_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("doc.kml", kml_str)
        for png in asset_pngs:
            if png and os.path.exists(png):
                zf.write(png, os.path.basename(png))
    return kmz_path


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
                       "Not analysed" if pv is None else "Phase %s" % pv, p5))

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

def run(geojson_path=DEFAULT_GEOJSON, make_teaser=True, status_callback=None):
    def _status(msg):
        if status_callback:
            status_callback(msg)
        print(msg)

    if not os.path.exists(geojson_path):
        raise FileNotFoundError(
            "IPC GeoJSON not found: %s\nPlace the IPC Mapping Tool export in data/."
            % geojson_path)

    _status("Parsing IPC GeoJSON...")
    records, meta = build_geojson_records(geojson_path)
    _status("Parsed %d analysis areas." % len(records))

    _status("Building KMZ...")
    kml, asset_pngs = build_food_insecurity_kml(records, meta)
    kmz_path = package_kmz(kml, asset_pngs)
    _status("KMZ written: %s" % kmz_path)

    teaser_path = None
    if make_teaser:
        _status("Building Plotly teaser...")
        teaser_path = generate_plotly_teaser(records, meta)
        if teaser_path:
            _status("Teaser written: %s" % teaser_path)

    return {"kmz": kmz_path, "teaser": teaser_path, "areas": len(records)}


if __name__ == "__main__":
    result = run()
    print("Done:", result)
