# Earth System Exhibit Wireframe: "The Heat Chain"
## Mobile Scrollytelling Sequence (Portrait / 390px width)

---

### DESIGN PRINCIPLES APPLIED
- One idea per viewport
- Scroll to advance (no tapping required)  
- Text blocks: 2-3 sentences max between visualizations
- Consistent color coding: orange = heat/energy, red = danger, blue = ocean
- Progress indicator on right edge throughout
- Existing gallery visualizations embedded as-is (Studio-curated)

---

## SCREEN 1: TITLE CARD
```
+----------------------------------+
|                                  |
|         [progress: o----]        |
|                                  |
|                                  |
|      .-~~~-.                     |
|     (  Earth  )                  |
|      `-...-'                     |
|                                  |
|                                  |
|     T H E   H E A T             |
|         C H A I N               |
|                                  |
|   From Energy Imbalance         |
|   to Human Consequence          |
|                                  |
|                                  |
|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
|   Paloma's Orrery               |
|   Earth System Exhibit          |
|   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~   |
|                                  |
|                                  |
|          scroll down             |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 2: NARRATIVE HOOK
```
+----------------------------------+
|                            o---  |
|                                  |
|                                  |
|  Every second, Earth absorbs     |
|  more energy than it radiates    |
|  back to space.                  |
|                                  |
|  That's the planetary energy     |
|  imbalance. It's small --        |
|  about 1 watt per square meter   |
|  -- but it never stops.          |
|                                  |
|  Where does all that energy go?  |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 3: ENERGY IMBALANCE VIZ (EXISTING)
```
+----------------------------------+
|                            oo--  |
|                                  |
|  THE CAUSE                       |
|  ~~~~~~~~~~                      |
|                                  |
| +------------------------------+ |
| |                              | |
| | [EMBEDDED PLOTLY]            | |
| |                              | |
| | Energy Imbalance &           | |
| | Temperature (2005-2025)      | |
| |                              | |
| | gallery: energy_imbalance    | |
| | (Studio-curated, portrait)   | |
| |                              | |
| |   /--._                      | |
| |  /     \  OHC rising         | |
| | /       \_____/              | |
| |                              | |
| | ENSO bands visible           | |
| | Dual axis: temp + imbalance  | |
| |                              | |
| +------------------------------+ |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 4: INTERPRETATION BRIDGE
```
+----------------------------------+
|                            ooo-  |
|                                  |
|                                  |
|  90% of that trapped energy      |
|  goes into the ocean. The        |
|  ocean is a buffer -- but        |
|  buffers have limits.            |
|                                  |
|  The remaining energy heats      |
|  the atmosphere. That's the      |
|  temperature anomaly.            |
|                                  |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 5: TEMPERATURE ANOMALY VIZ (EXISTING)
```
+----------------------------------+
|                            ooo-  |
|                                  |
|  THE SIGNAL                      |
|  ~~~~~~~~~~                      |
|                                  |
| +------------------------------+ |
| |                              | |
| | [EMBEDDED PLOTLY]            | |
| |                              | |
| | Global Temperature           | |
| | Anomalies, 1880-2025         | |
| |                              | |
| | gallery: global_temperature  | |
| | _anomalies                   | |
| |                              | |
| |              ___/            | |
| |           __/                | |
| | _________/                   | |
| |                              | |
| | 145 years of warming         | |
| | visible in one chart         | |
| |                              | |
| +------------------------------+ |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 6: INTERPRETATION BRIDGE
```
+----------------------------------+
|                            oooo  |
|                                  |
|                                  |
|  A global average hides the      |
|  extremes. Heat doesn't          |
|  distribute evenly.              |
|                                  |
|  It concentrates. In cities.     |
|  In river valleys. In places     |
|  where humidity traps it         |
|  against human skin.             |
|                                  |
|  That's where it kills.          |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 7: HEAT EVENT TEASER (EXISTING - CHOOSE ONE)
```
+----------------------------------+
|                            oooo  |
|                                  |
|  THE GROUND TRUTH                |
|  ~~~~~~~~~~~~~~~                 |
|                                  |
| +------------------------------+ |
| |                              | |
| | [EMBEDDED PLOTLY MAP]        | |
| |                              | |
| | Chicago Heat Wave            | |
| | July 1995                    | |
| |                              | |
| | gallery: (new teaser from    | |
| | earth_system_generator.py)   | |
| |                              | |
| |  +----+                      | |
| |  |CHI |  Wet-bulb temps      | |
| |  | ** |  28.3 deg C           | |
| |  +----+  739 excess deaths   | |
| |                              | |
| +------------------------------+ |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 8: THE HUMAN CHAIN (INTERPRETIVE - NEW)
```
+----------------------------------+
|                            oooo  |
|                                  |
|  THE HUMAN COST                  |
|  ~~~~~~~~~~~~~~                  |
|                                  |
|  Chicago 1995 revealed what      |
|  global averages obscure:        |
|  heat kills along lines of       |
|  poverty and isolation.          |
|                                  |
|  739 people died in 5 days.      |
|  Most were elderly, alone,       |
|  in apartments without AC,       |
|  afraid to open windows.         |
|  (Klinenberg, 2002)              |
|                                  |
|  +----------------------------+  |
|  | INTERPRETIVE LAYER         |  |
|  |                            |  |
|  | Physical:                  |  |
|  |   Wet-bulb 28.3C           |  |
|  |   (NOAA station data)      |  |
|  |                            |  |
|  | Infrastructure:            |  |
|  |   Urban heat island +8C    |  |
|  |   (Changnon et al., 1996)  |  |
|  |                            |  |
|  | Demographic:               |  |
|  |   82% of deaths age 65+    |  |
|  |   (CDC MMWR, 1995)         |  |
|  |                            |  |
|  | Economic:                  |  |
|  |   Disproportionate impact  |  |
|  |   on low-income S/W side   |  |
|  |   (Klinenberg, 2002)       |  |
|  +----------------------------+  |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 9: PATTERN RECOGNITION (INTERPRETIVE - NEW)
```
+----------------------------------+
|                            oooo  |
|                                  |
|  THE PATTERN                     |
|  ~~~~~~~~~~~                     |
|                                  |
|  Chicago 1995 was not unique.    |
|  The same pattern repeats:       |
|                                  |
|  +----------------------------+  |
|  |                            |  |
|  | Europe 2003:  70,000 dead  |  |
|  |   Same vulnerability       |  |
|  |   (Robine et al., 2008)    |  |
|  |                            |  |
|  | India/Pakistan 2015:       |  |
|  |   3,500+ dead              |  |
|  |   Wet-bulb approached      |  |
|  |   biological limit         |  |
|  |   (Raymond et al., 2020)   |  |
|  |                            |  |
|  | Pacific NW 2021:           |  |
|  |   Lytton 49.6C, burned     |  |
|  |   "Impossible" in adapted  |  |
|  |   infrastructure           |  |
|  |   (Philip et al., 2022)    |  |
|  |                            |  |
|  +----------------------------+  |
|                                  |
|  Each event was "unprecedented." |
|  Together they are a trend.      |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 10: SECOND-ORDER EFFECTS (INTERPRETIVE - NEW)
```
+----------------------------------+
|                            oooo  |
|                                  |
|  BEYOND THE HEAT                 |
|  ~~~~~~~~~~~~~~                  |
|                                  |
|  Heat events trigger cascades    |
|  that outlast the event itself.  |
|                                  |
|  +----------------------------+  |
|  | CAUSAL CHAIN (attributed)  |  |
|  |                            |  |
|  | PHYSICAL                   |  |
|  | Energy imbalance -> temp   |  |
|  | [strong attribution]       |  |
|  |       |                    |  |
|  |       v                    |  |
|  | ECOLOGICAL                 |  |
|  | Crop failure, water stress |  |
|  | [strong attribution]       |  |
|  |       |                    |  |
|  |       v                    |  |
|  | ECONOMIC                   |  |
|  | Food price spikes,         |  |
|  | infrastructure damage      |  |
|  | [moderate attribution]     |  |
|  |       |                    |  |
|  |       v                    |  |
|  | DEMOGRAPHIC                |  |
|  | Migration, displacement    |  |
|  | [contested attribution]    |  |
|  |       |                    |  |
|  |       v                    |  |
|  | POLITICAL                  |  |
|  | Resource conflict,         |  |
|  | institutional stress       |  |
|  | [interpretive synthesis]   |  |
|  |                            |  |
|  +----------------------------+  |
|                                  |
|  Attribution weakens as we       |
|  move from physics to politics.  |
|  That's honest. The chain is     |
|  still real.                     |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 11: SPECIFIC SECOND-ORDER EXAMPLE
```
+----------------------------------+
|                            oooo  |
|                                  |
|  CASE: SYRIA 2006-2011          |
|  ~~~~~~~~~~~~~~~~~~~~~~          |
|                                  |
|  +----------------------------+  |
|  |                            |  |
|  | 2006-2010: Worst drought   |  |
|  | in Syria's recorded        |  |
|  | history.                   |  |
|  | (Kelley et al., 2015,      |  |
|  |  PNAS)                     |  |
|  |                            |  |
|  | -> 1.5M internal migrants  |  |
|  |    (rural to urban)        |  |
|  |    (UN OCHA)               |  |
|  |                            |  |
|  | -> Agricultural collapse   |  |
|  |    in Fertile Crescent     |  |
|  |    (Gleick, 2014)          |  |
|  |                            |  |
|  | -> Urban strain preceded   |  |
|  |    2011 unrest             |  |
|  |    [INTERPRETIVE NOTE:     |  |
|  |    Drought was A factor,   |  |
|  |    not THE factor.         |  |
|  |    Attribution is debated. |  |
|  |    See Selby et al., 2017  |  |
|  |    for counterargument.]   |  |
|  |                            |  |
|  +----------------------------+  |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 12: RETURN TO SYSTEM VIEW
```
+----------------------------------+
|                            oooo  |
|                                  |
|  THE FULL PICTURE                |
|  ~~~~~~~~~~~~~~~                 |
|                                  |
| +------------------------------+ |
| |                              | |
| | [EMBEDDED PLOTLY]            | |
| |                              | |
| | Planetary Boundaries         | |
| | (Stockholm Resilience Ctr)   | |
| |                              | |
| | gallery: planetary_          | |
| | boundaries_mobile            | |
| |                              | |
| |      ___                     | |
| |    /  |  \   7 of 9          | |
| |   |  -+- |  transgressed     | |
| |    \ _|_/                    | |
| |                              | |
| | CLIMATE CHANGE wedge         | |
| | highlighted / pulsing        | |
| |                              | |
| +------------------------------+ |
|                                  |
|              |                   |
|              v                   |
+----------------------------------+
```

## SCREEN 13: CLOSING + NAVIGATION
```
+----------------------------------+
|                            ooooo |
|                                  |
|                                  |
|  Heat is one chain. There        |
|  are others.                     |
|                                  |
|  +----------------------------+  |
|  |                            |  |
|  |  EXPLORE MORE CHAINS:      |  |
|  |                            |  |
|  |  [The Ocean Chain]         |  |
|  |   CO2 -> Acidification ->  |  |
|  |   Coral -> Fisheries ->    |  |
|  |   Coastal Communities      |  |
|  |                            |  |
|  |  [The Water Chain]         |  |
|  |   Glacial Retreat ->       |  |
|  |   Freshwater ->            |  |
|  |   Agriculture -> Drought   |  |
|  |   -> Migration             |  |
|  |                            |  |
|  |  [The Land Chain]          |  |
|  |   Deforestation ->         |  |
|  |   Carbon Release ->        |  |
|  |   Biodiversity Loss ->     |  |
|  |   Ecosystem Collapse       |  |
|  |                            |  |
|  +----------------------------+  |
|                                  |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    |
|  Sources & Attribution:          |
|  [Full citation list]            |
|  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    |
|                                  |
|  Paloma's Orrery                 |
|  palomasorrery.com               |
|  @palomas_orrery                 |
|                                  |
|  "Data Preservation is           |
|   Climate Action"                |
|                                  |
+----------------------------------+
```

---

## STRUCTURAL NOTES

### What's Existing vs New

| Screen | Content | Status |
|--------|---------|--------|
| 1 | Title card | NEW (gallery viewer renders) |
| 2 | Narrative hook | NEW (exhibit JSON text block) |
| 3 | Energy Imbalance viz | EXISTING gallery entry |
| 4 | Interpretation bridge | NEW (exhibit JSON text block) |
| 5 | Temperature Anomaly viz | EXISTING gallery entry |
| 6 | Interpretation bridge | NEW (exhibit JSON text block) |
| 7 | Heat event teaser | EXISTING (or new from generator) |
| 8 | Human cost analysis | NEW (interpretive, Tony-authored) |
| 9 | Pattern recognition | NEW (interpretive, Tony-authored) |
| 10 | Second-order framework | NEW (interpretive, Tony-authored) |
| 11 | Case study | NEW (interpretive, Tony-authored) |
| 12 | Planetary boundaries | EXISTING gallery entry |
| 13 | Closing + navigation | NEW (gallery viewer renders) |

### The Exhibit JSON (Conceptual)

```json
{
  "exhibit_id": "heat_chain",
  "title": "The Heat Chain",
  "subtitle": "From Energy Imbalance to Human Consequence",
  "author": "Tony Quintanilla",
  "boundary_tags": ["CLIMATE_CO2", "CLIMATE_RF"],
  "sections": [
    {
      "type": "title",
      "title": "The Heat Chain",
      "subtitle": "From Energy Imbalance to Human Consequence"
    },
    {
      "type": "narrative",
      "text": "Every second, Earth absorbs more energy..."
    },
    {
      "type": "visualization",
      "gallery_id": "energy_imbalance_desktop",
      "label": "THE CAUSE",
      "mobile_id": "energy_imbalance_mobile"
    },
    {
      "type": "narrative",
      "text": "90% of that trapped energy goes into the ocean..."
    },
    {
      "type": "visualization",
      "gallery_id": "global_temperature_anomalies",
      "label": "THE SIGNAL"
    },
    {
      "type": "narrative",
      "text": "A global average hides the extremes..."
    },
    {
      "type": "visualization",
      "gallery_id": "chicago_1995_teaser",
      "label": "THE GROUND TRUTH"
    },
    {
      "type": "interpretive",
      "label": "THE HUMAN COST",
      "author_note": "Interpretive synthesis by Tony Quintanilla",
      "layers": [
        { "layer": "Physical", "attribution": "strong", "text": "..." },
        { "layer": "Infrastructure", "attribution": "strong", "text": "..." },
        { "layer": "Demographic", "attribution": "moderate", "text": "..." },
        { "layer": "Economic", "attribution": "contested", "text": "..." }
      ],
      "citations": ["Klinenberg 2002", "CDC MMWR 1995", "Changnon 1996"]
    },
    {
      "type": "interpretive",
      "label": "THE PATTERN",
      "cases": [
        { "event": "Europe 2003", "deaths": "70,000", "citation": "Robine 2008" },
        { "event": "India/Pakistan 2015", "deaths": "3,500+", "citation": "Raymond 2020" },
        { "event": "Pacific NW 2021", "note": "49.6C Lytton", "citation": "Philip 2022" }
      ]
    },
    {
      "type": "interpretive",
      "label": "BEYOND THE HEAT",
      "chain": [
        { "level": "Physical", "attribution_strength": "strong" },
        { "level": "Ecological", "attribution_strength": "strong" },
        { "level": "Economic", "attribution_strength": "moderate" },
        { "level": "Demographic", "attribution_strength": "contested" },
        { "level": "Political", "attribution_strength": "interpretive" }
      ]
    },
    {
      "type": "interpretive",
      "label": "CASE: SYRIA 2006-2011",
      "author_note": "Drought was A factor, not THE factor.",
      "citations": ["Kelley 2015", "Gleick 2014", "Selby 2017"]
    },
    {
      "type": "visualization",
      "gallery_id": "planetary_boundaries_mobile",
      "label": "THE FULL PICTURE",
      "highlight_wedge": "CLIMATE_CO2"
    },
    {
      "type": "closing",
      "related_exhibits": ["ocean_chain", "water_chain", "land_chain"],
      "citation_list": "..."
    }
  ]
}
```

### Key Design Decisions

1. **Existing vizzes are embedded, not recreated.** The gallery viewer
   loads them from the same JSON files already in the pipeline.
   Studio-curated = ready for mobile.

2. **Interpretive blocks are Tony-authored.** These are NOT auto-generated.
   They carry his voice, his citations, his judgment about attribution.
   The exhibit JSON stores them; the gallery viewer renders them.

3. **Attribution strength is explicit.** Every claim in the interpretive
   layer carries a label: strong / moderate / contested / interpretive.
   The viewer could render these as color-coded confidence bands.

4. **The chain ends at the system view.** Starting specific (energy) and
   ending broad (planetary boundaries) gives the exhibit a zoom-out arc.
   The polar chart at the end says: this is just ONE of nine stories.

5. **Navigation to other chains is the last screen.** This is where the
   exhibits connect to each other. Each chain is its own scrollytelling
   sequence, but they all return to the polar chart hub.

6. **Progress indicator throughout.** Simple dots on the right edge.
   On mobile, users need to know where they are in a 13-screen scroll.

### What the Gallery Viewer Needs (New Capabilities)

- Exhibit mode: render a sequence of sections from exhibit JSON
- Narrative blocks: styled text cards between visualizations  
- Interpretive blocks: structured cards with attribution layers
- Progress indicator: dots or bar showing position in exhibit
- Chain navigation: links between exhibits at the closing screen
- Highlight wedge: ability to pulse/highlight one boundary wedge
  (or simply link to it)

### What Doesn't Change

- Gallery Studio still curates individual plots for mobile
- JSON converter pipeline unchanged
- index.html still renders individual gallery entries normally
- Exhibits are an ADDITIONAL viewing mode, not a replacement
