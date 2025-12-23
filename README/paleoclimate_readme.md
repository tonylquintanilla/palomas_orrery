# 🦴 Paleoclimate Visualizations for Paloma's Orrery

**Complete Package | Updated December 2025**  
*Now with full Phanerozoic coverage (540 Ma), Human Origins evolution markers (25 species), Marine Isotope Stages, 2025 research integration, and climate-driven evolution story*

---

## 📦 Package Contents

### 🚀 Core Files (four visualization variants):

**1. paleoclimate_visualization.py** - Original Cenozoic visualization
- Coverage: 66 Ma (Cenozoic Era) to present
- Focus: Ice age cycles and Holocene stability

**2. paleoclimate_dual_scale.py** - Dual-scale hybrid
- Coverage: Modern (1880-2025) + Deep Time (66 Ma)
- Focus: Direct comparison of timescales

**3. paleoclimate_visualization_full.py** - **Full Phanerozoic + Human History**
- Coverage: 540 Ma (Cambrian Explosion) to 2025 CE
- Focus: Complete animal life history + human-scale climate events
- Interactive timeline + Medieval/Holocene events

**4. paleoclimate_human_origins_v9.py** - **🆕 Climate-Driven Human Evolution**
- Coverage: 540 Ma to present + 25 hominin species markers
- Focus: How Pleistocene climate pulses shaped human evolution
- Features: MIS stages, ghost populations, 2025 research integration
- **Featured in this README**

### 📊 Required Data Files:

**All paleoclimate data stored in `data/` subdirectory** (as of November 2025):

**Essential:**
- **data/8c__Phanerozoic_Pole_to_Equator_Temperatures.csv** (234 KB)
  - Scotese et al. (2021) temperature reconstruction
  - Source: https://zenodo.org/records/10659112
  - Place in `data/` subdirectory

**Auto-downloaded:**
- **data/lr04_benthic_stack.json** (via fetch script)
  - LR04 Benthic Stack (Lisiecki & Raymo 2005)
  - Run `python fetch_paleoclimate_data.py` (saves to `data/`)
  
- **data/epica_co2_800kyr.json** (via fetch script)
  - EPICA Dome C ice core CO₂ (800,000 years)
  - Run `python fetch_paleoclimate_data.py` (saves to `data/`)

- **data/temperature_giss_monthly.json** (via fetch script)
  - NASA GISS instrumental temperature record (1880-2025)
  - Run `python fetch_climate_data.py` (saves to `data/`)
  - **NOTE**: File must be in `data/` subdirectory for visualizations to load correctly

**Optional (enhances coverage):**
- **data/temp12k_allmethods_percentiles.csv** (67 KB)
  - Holocene reconstruction (Kaufman et al. 2020)
  - Download and place in `data/` subdirectory
  - Source: https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/kaufman2020/temp12k_allmethods_percentiles.csv

**File structure:**
```
palomas_orrery/
├── data/                                   # All paleoclimate data ✨
│   ├── 8c__Phanerozoic_Pole_to_Equator_Temperatures.csv
│   ├── lr04_benthic_stack.json
│   ├── epica_co2_800kyr.json
│   ├── temperature_giss_monthly.json       # NASA GISS (required)
│   └── temp12k_allmethods_percentiles.csv (optional)
├── fetch_paleoclimate_data.py             (fetches to data/)
├── fetch_climate_data.py                   (fetches GISS to data/)
├── paleoclimate_visualization.py
├── paleoclimate_dual_scale.py
├── paleoclimate_visualization_full.py
└── paleoclimate_human_origins_v9.py        # 🆕 Human evolution layer
```

### 📚 Documentation:
- **paleoclimate_readme.md** - This file - complete overview
- **CHANGE_MANIFEST_Phanerozoic_Extension.md** - Technical details of v2 implementation
- **Session summaries** - Narrative of development process

---

## ⚡ Quick Integration (10 minutes)

```bash
# 1. Copy files to your project
cp paleoclimate_visualization_v2.py /your/project/
mkdir -p /your/project/data/
cp 8c__Phanerozoic_Pole_to_Equator_Temperatures.csv /your/project/data/
cp fetch_paleoclimate_data.py /your/project/

# 2. Download LR04 data
python fetch_paleoclimate_data.py

# 3. (Optional) Download Holocene data
curl -O https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/kaufman2020/temp12k_allmethods_percentiles.csv

# 4. Edit earth_system_visualization_gui.py
#    Add import:
from paleoclimate_visualization_v2 import create_paleoclimate_visualization as create_phanerozoic_viz

#    Add function and button (see integration guide)

# 5. Test it!
python earth_system_visualization_gui.py
# Click: 🦴 Paleoclimate: Phanerozoic (540 Ma - Full History)
```

---

## 🎯 What You Get (v2 - Phanerozoic)

### Three Visualization Options in Your GUI:
1. **🦕 Cenozoic** (66 Ma) - Brown button - Original version
2. **🦕 Dual Scale** (Modern + Deep Time) - Gold button - Hybrid view
3. **🦴 Phanerozoic** (540 Ma) - Dark Blue button - **FULL HISTORY**

### The Phanerozoic Visualization Shows:

**Timeline Coverage:**
- **540 million years** (Cambrian Explosion → 2025 CE)
- Entire history of complex animal life
- All geologic eras and periods color-coded
- Four integrated temperature datasets
- **NEW**: Interactive timeline with common year notation
- **NEW**: Human-scale climate events (Medieval Warm Period, Little Ice Age, Younger Dryas)

**Interactive Features:**

**🕐 Interactive Timeline (NEW!)** - Hover over any timeline marker:
- (2025) - Present climate: +1.28°C, unprecedented rate
- (2015) - Paris Agreement era
- (1925) - Early industrial warming begins
- (1025) - Medieval Warm Period
- (10,000 BCE) - Agricultural revolution begins
- (100,000 BCE) - Ice Age humanity
- (1 Ma) - Early Pleistocene glacial cycles
- (10 Ma) - Miocene grasslands
- (100 Ma) - Cretaceous greenhouse
- (540 Ma) - Cambrian Explosion

**🌍 Human-Scale Climate Events (NEW!)** - Critical for understanding history:
- **Younger Dryas** (12,900-11,700 ya) - Three regional temperature bands showing spatial variation
- **Holocene Thermal Maximum** (~6,700 ya) - Warmest natural Holocene (+0.53C)
- **Eemian Interglacial** (~125,000 ya) - Last time naturally this warm (+0.6C in data)
- **Start of Holocene** (11,700 ya) - Stable climate enables civilization
- **Medieval Warm Period** (950-1250 CE) - Vikings settle Greenland
- **Little Ice Age** (1300-1850 CE) - Vikings abandon Greenland, famines
- **Proposed Anthropocene** (1950 CE) - Human dominance begins

**🦴 Deep Time Events** - Hoverable "?" annotations:
- Cretaceous Thermal Maximum (~90 Ma)
- Permian-Triassic "Great Dying" (~252 Ma)
- Carboniferous Icehouse (~300 Ma)
- Late Ordovician Glaciation (~445 Ma)
- End-Triassic Extinction (~201 Ma)
- K-Pg Extinction (66 Ma) - Dinosaurs
- PETM (55.8 Ma) - Thermal maximum
- Grande Coupure (34 Ma) - Antarctic freezes
- Ice Ages Begin (2.58 Ma) - Pleistocene cycles

**📊 Method Transparency:**
- Info box shows all four dataset methods
- Intentional overlap demonstrates uncertainty
- "Scientific uncertainty is normal and expected!"

**🔍 Exploration Tools:**
- Log scale x-axis for multi-scale zoom
- Full zoom from 540 Ma to decades
- Hover reveals educational detail
- Clean visual, depth on demand

**The "Double Hump" Pattern:**
```
Temp
 ↑     /\              /\
 |    /  \            /  \
 |   /    \____/\____/    \___
 |  /        Paleozoic  Mesozoic  Cenozoic
 └──────────────────────────────────→ Time
   540 Ma  400   300   200   100    0
```

---

## 🧬 Human Origins Visualization (NEW - December 2025)

### paleoclimate_human_origins_v9.py - **Climate-Driven Evolution**

The paleoclimate visualization now includes a comprehensive hominin evolution layer, showing how Pleistocene climate pulses shaped human evolution. This transforms the climate chart into a story about *us*.

### What's Included:

**25 Hominin Markers** (19 fossil-confirmed + 6 ghost populations):

| Category | Count | Examples |
|----------|-------|----------|
| Early Hominoids | 2 | Proconsul (21 Ma), Morotopithecus |
| Early Hominins | 4 | Sahelanthropus, Ardipithecus |
| Australopithecines | 3 | A. afarensis ("Lucy"), A. africanus |
| Homo (fossil) | 10 | H. erectus, H. longi, H. sapiens, H. floresiensis |
| Ghost Populations | 6 | Population A/B, Deep Denisovan, SE Asian Ghost |

**Marine Isotope Stages (MIS)** - The "heartbeat" of Pleistocene climate:
- 10 major stages from MIS 1 (Holocene) to MIS 12
- Warm periods (odd numbers): Corridors open, expansions
- Cold periods (even numbers): Refugia, bottlenecks
- Visual bands showing glacial/interglacial cycles

**Climate Events:**
- 🌋 Toba Supereruption (74 ka) - VEI-8, bottleneck hypothesis
- 🌿 Green Sahara windows (MIS 5e & Holocene) - Migration corridors

### Visual Design:

**Marker Types:**
- ▲ **Filled triangles**: Fossil-confirmed species (19)
- △ **Open triangles**: Ghost populations - DNA evidence only (6)

**Positioning:**
- Markers clustered near y = -10 line
- Manual `y_offset` values for precise staggering
- Vertical guide lines connect to MIS context above

**MIS Bands:**
- 🔴 Warm/interglacial: Tomato fill, diamond markers
- 🔵 Cold/glacial: Cornflower blue fill, square markers
- Hoverable with time ranges and significance

### 2025 Research Integration:

The visualization incorporates groundbreaking 2025 findings:

**Yunxian 2 Skull** (Feng et al., Science, Sept 2025):
- Reclassified Dragon Man clade (H. longi) to 1 Ma
- Pushes Neanderthal divergence to ~1.38 Ma
- H. heidelbergensis now flagged as possible side-branch

**Cambridge Two-Population Origin** (Cousins et al., Nature Genetics, March 2025):
- H. sapiens = merger of two African populations
- Split ~1.5 Ma, reunited ~300 ka
- 80:20 ratio (Pop A: 80%, Pop B: 20% with brain genes)

**Five-Branch Model** (Natural History Museum 2025):
1. Asian H. erectus (ancient survivors)
2. H. heidelbergensis (side-branch?)
3. H. neanderthalensis (European)
4. H. longi / Denisovans (East Asian)
5. H. sapiens (African)

### Ghost Populations Explained:

| Population | Split Time | Evidence | Story |
|------------|------------|----------|-------|
| "Superarchaic" | 2.0 Ma | Denisovan DNA | Possibly late H. erectus |
| West African | 0.7 Ma | Yoruba/Mende DNA | 2-19% ancestry, unknown archaic |
| Population A (80%) | 1.5 Ma | Sapiens genome | Major ancestor, also → Neanderthals |
| Population B (20%) | 1.5 Ma | Sapiens genome | Minor ancestor, brain genes |
| "Deep Denisovan" (D2) | 0.28 Ma | Papuan/Filipino DNA | Divergent Denisovan lineage |
| SE Asian Archaic | ~0.15 Ma | SE Asian DNA | Unknown — erectus? floresiensis? |

### Island Southeast Asia - Parallel Evolution:

Two remarkable "island rule" species now included:
- **H. floresiensis** (190-50 ka): "The Hobbit" of Flores — survived until sapiens arrived!
- **H. luzonensis** (67 ka): Philippines discovery (2019) — parallel dwarfism

### The Story It Tells:

The Pleistocene wasn't a single-file march of species but a **braided stream** of populations mixing, separating, and remixing across Africa and Eurasia.

**MIS cold periods** → Sahara impassable → Populations isolated → Ghost splits
**MIS warm periods** → Green Sahara → Corridors open → Populations merge

The LR04 benthic trace IS the MIS signal — now annotated to show what those wiggles meant for human evolution.

### Key Hover Information:

Each marker includes:
- Species name and age
- Key sites and discoveries
- Significance for human evolution
- 2025 updates where applicable
- Source citations

### Integration:

The human origins layer integrates seamlessly with existing paleoclimate features:
- Same log-scale x-axis (deep time to present)
- Same temperature y-axis (evolution responds to climate)
- Hominin markers at bottom, MIS context in middle, temperature above
- All interactive (hover for details)

---

### 1. Phanerozoic Reconstruction (Scotese et al. 2021)
- **Coverage**: 540 Ma to 0 Ma (full range, filtered to show >2 Ma)
- **Source**: PALEOMAP Project global temperature grid
- **Method**: 
  - Lithologic climate indicators (coals, evaporites, tillites, bauxites)
  - Oxygen isotope (δ¹⁸O) measurements from marine fossils
  - Climate model simulations (validation)
- **Resolution**: 5-10 Myr (varies by age)
- **Uncertainty**: ±3-5°C for ages >100 Ma (typical for proxy methods)
- **Shows**: Long-term "double hump" Phanerozoic climate pattern
- **Color**: Navy blue (#003049)
- **Citation**: Scotese, C.R., Vérard, C., Burgener, L., Elling, R.P., Kocsis, A.T. (2024)

### 2. LR04 Benthic Stack (Lisiecki & Raymo 2005)
- **Coverage**: 5.3 Ma to ~5 ka
- **Source**: 57 globally distributed ocean sediment cores
- **Method**: Benthic foraminifera δ¹⁸O (oxygen isotopes)
  - Shells record deep ocean temperature + ice volume
  - Higher δ¹⁸O = more ice + colder temperatures
- **Resolution**: ~1 kyr bins
- **Shows**: Ice age cycles, glacial-interglacial oscillations
- **Color**: Red (#C1121F)
- **Citation**: Lisiecki, L.E. & Raymo, M.E. (2005). *Paleoceanography* 20, PA1003.

### 3. Holocene Reconstruction (Kaufman et al. 2020)
- **Coverage**: 12 ka to present
- **Source**: Temperature 12k database (679 sites, 1,319 proxy records)
- **Method**: Multi-proxy ensemble
  - Pollen assemblages (51% of sites)
  - Marine sediment biomarkers (31%)
  - Peat cores (11%)
  - Ice cores (3%)
  - Other proxies (4%)
- **Resolution**: 100-year bins
- **Shows**: Holocene thermal maximum (~6.5 ka) and cooling trend
- **Includes**: Medieval Warm Period, Little Ice Age
- **Color**: Green (#2CC174)
- **Citation**: Kaufman, D., McKay, N., Routson, C., et al. (2020). *Scientific Data* 7, 201.

### 4. Instrumental Record (NASA GISS)
- **Coverage**: 1880-2025
- **Source**: Global meteorological station network
- **Method**: Direct temperature measurements
  - Land: Thermometers at weather stations
  - Ocean: Buoys, ships
  - Satellite: Remote sensing (recent)
- **Resolution**: Monthly (shown as annual means)
- **Shows**: Rapid modern warming (+1.28°C anomaly)
- **Color**: Blue (#0096C7)
- **Citation**: GISTEMP Team (2025). NASA GISS.

### 5. Climate Projections (IPCC AR6 & UNEP EGR 2025)

**IPCC Shared Socioeconomic Pathways (SSP):**
- **Coverage**: 2025-2100 (future projections)
- **Source**: IPCC AR6 Working Group I, Table 4.2
- **Scenarios shown**:
  - SSP1-1.9: Very low emissions, 1.5°C limit
  - SSP1-2.6: Low emissions, Paris Agreement target
  - SSP2-4.5: Intermediate emissions
  - SSP3-7.0: High emissions
  - SSP5-8.5: Very high emissions (fossil-fuel intensive)
- **Method**: Climate model ensemble projections
- **Citation**: Lee, J.-Y., J. Marotzke, et al. (2021). IPCC AR6 WG1.

**UNEP Current Policies Assessment (2025):**
- **Peak warming by 2100** (relative to pre-industrial):
  - 50% probability: 2.6°C
  - 66% probability: 2.8°C  
  - 90% probability: 3.3°C
- **Shown as**: Horizontal reference lines showing uncertainty range
- **Source**: UNEP Emissions Gap Report 2025, Figure 4.2
- **What it shows**: Where we're actually heading given current policies
- **Visualization**: 
  - Full Phanerozoic view: 2 lines (2.6°C, 3.3°C) showing range
  - Dual-scale view: 3 lines (2.6°C, 2.8°C, 3.3°C) with full probabilities
- **Citation**: UNEP (2025). Emissions Gap Report 2025. https://wedocs.unep.org/handle/20.500.11822/48854

### Why Show Overlapping Data?

**Educational Philosophy**: Overlaps demonstrate scientific uncertainty!

The visualization **intentionally** shows overlapping datasets (2-5 Ma range) to reveal:
- ✅ Different methods yield slightly different results (normal!)
- ✅ Scotese uses lithology + isotopes + models
- ✅ LR04 uses benthic foram δ¹⁸O only
- ✅ Both are valid, both have uncertainties
- ✅ Agreement = confidence; disagreement = caution

**Info box states clearly:**
> "ℹ️ Overlapping curves show method differences  
> Scientific uncertainty is normal and expected!"

This is **honest science communication** - not hiding uncertainty, but explaining it!

---

## 🎓 Interactive Educational Features

### **NEW: Interactive Timeline (November 1, 2025)**

**Design**: Clean common year notation markers across the top

**Hover to learn:**
- **2025** - Current climate moment (unprecedented warming rate)
- **2015** - Paris Agreement, renewable energy surge
- **1925** - Roaring Twenties, modern warming begins
- **1025** - Medieval period, Vikings in Greenland
- **10,000 BCE** - End of Ice Age, agriculture begins
- **100,000 BCE** - Ice Age humanity, Neanderthals
- **1 Ma** - Early Pleistocene, Homo erectus
- **10 Ma** - Miocene cooling, grasslands expand
- **100 Ma** - Cretaceous greenhouse, dinosaurs thrive
- **540 Ma** - Cambrian Explosion, complex life emerges

**Educational Value**: Connects deep time to human experience!

---

### **NEW: Human-Scale Climate Events**

**Critical for understanding civilization's climate context:**

**1. Younger Dryas (12,900-11,700 years ago)** - Turquoise marker
- Sudden return to Ice Age conditions in DECADES
- Temperature dropped ~10°C
- Meltwater disrupted Gulf Stream circulation
- Megafauna extinctions (mammoths, saber-tooths)
- **Forced agricultural revolution** (stress response)
- Shows climate can flip FAST!
- Ended abruptly → Holocene begins

**2. Start of Holocene (11,700 years ago)** - Green marker
- End of Younger Dryas, rapid warming
- Stable, warm climate begins
- Enables human civilization to flourish
- Most stable climate in 800,000 years
- Agriculture spreads globally

**3. Medieval Warm Period (950-1250 CE)** - Orange marker
- Warmest period of last 2,000 years
- Vikings settle Greenland (985 CE)
- European prosperity, crop expansion
- ~0.3°C warmer than pre-industrial
- Natural climate variability

**4. Little Ice Age (1300-1850 CE)** - Blue marker
- Coldest period since last glacial maximum
- **Viking Greenland colonies abandoned (~1450 CE)**
- Thames River froze regularly
- Crop failures, famines across Europe/Asia
- Ukrainian pastoralist cultures disrupted
- ~1°C cooler than Medieval Warm Period
- Ended as industrial warming began

**5. Proposed Anthropocene (1950 CE)** - Red marker
- "Great Acceleration" begins
- Nuclear testing, plastic, concrete markers
- Human activity dominates Earth system
- CO₂ rising faster than any natural event
- Sixth mass extinction underway

**Why These Matter:**
- Shows natural variability WITHIN Holocene stability
- Vikings' Greenland experience: climate impacts on civilization
- Small changes (±1°C) = huge human consequences
- Context for modern change (+1.28°C in 150 years)
- Agricultural revolution emerged from Younger Dryas crisis

---

### Deep Time Hoverable "?" Annotations

**Design Philosophy**: Clean visual + full detail on demand

**How it works:**
- Deep-time events marked with colored "?" symbols
- Match geologic period colors for context
- Hover reveals detailed information popup
- No visual clutter until user explores

**Events with hover details:**

1. **Late Ordovician Glaciation** (~445 Ma) - Teal "?"
   - First major Phanerozoic icehouse
   - ~85% of marine species extinct
   - Massive Gondwana ice sheets

2. **Carboniferous Icehouse** (~300 Ma) - Green "?"
   - The "Coal Age" - first vast forests
   - Trees evolved lignin (hard to decompose)
   - Massive carbon burial → ~12°C cooling

3. **Permian-Triassic Extinction** (~252 Ma) - Red "?"
   - "Great Dying" - worst mass extinction
   - ~96% of marine species extinct
   - Siberian Traps volcanism, ocean anoxia

4. **End-Triassic Extinction** (~201 Ma) - Purple "?"
   - One of the "Big Five" extinctions
   - CAMP volcanism (Central Atlantic)
   - Opened ecological space for dinosaurs

5. **Cretaceous Thermal Maximum** (~90 Ma) - Green "?"
   - Peak Mesozoic greenhouse
   - Global temp ~20°C above pre-industrial
   - No polar ice, warm oceans

6. **K-Pg Extinction** (66 Ma) - Labeled event
   - Chicxulub asteroid impact
   - 75% of species extinct (including dinosaurs)
   - Ended Mesozoic, began Age of Mammals

7. **PETM** (55.8 Ma) - Labeled event
   - Paleocene-Eocene Thermal Maximum
   - Rapid warming event
   - Closest ancient analog to modern warming

8. **Grande Coupure** (34 Ma) - Labeled event
   - "The Great Cut" - abrupt cooling
   - Antarctica freezes
   - Drake Passage opens

9. **Ice Ages Begin** (2.58 Ma) - Labeled event
   - Pleistocene glacial cycles start
   - 100,000-year rhythms
   - Human evolution backdrop

---

## 📖 Data Sources & Citations

### Scotese Phanerozoic

**Download:**
```bash
# Visit: https://zenodo.org/records/10659112
# Download: 8c__Phanerozoic_Pole_to_Equator_Temperatures.csv
# Place in project root
```

**Citation:**
> Scotese, C.R., Vérard, C., Burgener, L., Elling, R.P., and Kocsis, A.T. (2024). A New Global Temperature Curve for the Phanerozoic. Zenodo. https://doi.org/10.5281/zenodo.10659112

### LR04 Benthic Stack

**Auto-download:**
```bash
python fetch_paleoclimate_data.py
```

**Manual download:**
```bash
curl -O https://www.ncei.noaa.gov/pub/data/paleo/paleo-search/study/5847
```

**Citation:**
> Lisiecki, L.E. and Raymo, M.E. (2005). A Pliocene-Pleistocene stack of 57 globally distributed benthic δ18O records. *Paleoceanography* 20, PA1003. https://doi.org/10.1029/2004PA001071

### Holocene Reconstruction

**Download:**
```bash
curl -O https://www.ncei.noaa.gov/pub/data/paleo/reconstructions/kaufman2020/temp12k_allmethods_percentiles.csv
```

**Citation:**
> Kaufman, D., McKay, N., Routson, C., Erb, M., Dätwyler, C., Sommer, P.S., Heiri, O., Davis, B.A.S. (2020). Holocene global mean surface temperature, a multi-method reconstruction approach. *Scientific Data* 7, 201. https://doi.org/10.1038/s41597-020-0530-7

### NASA GISS

**Auto-fetched** (via your climate cache manager)

**Citation:**
> GISTEMP Team (2025). GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. https://data.giss.nasa.gov/gistemp/

---

## ✨ Alignment with Project Philosophy

### "Data Preservation is Climate Action"
- ✅ Archives Scotese Phanerozoic reconstruction (Zenodo)
- ✅ Preserves LR04 benthic stack (NOAA)
- ✅ Safeguards Holocene reconstruction (threatened data)
- ✅ Makes paleoclimate accessible beyond specialized tools
- ✅ Demonstrates value of long-term climate records
- ✅ 540 million years of Earth's memory preserved

### "Climate History is Human History"
- ✅ Younger Dryas → Agricultural revolution
- ✅ Medieval Warm Period → Viking expansion
- ✅ Little Ice Age → Viking collapse, famines
- ✅ Small climate changes = major societal impacts
- ✅ Context for understanding modern change

### Educational Focus (For Paloma and Everyone)
- ✅ Interactive exploration encourages curiosity
- ✅ Timeline hovers connect deep time to human experience
- ✅ Human-scale events make climate tangible
- ✅ Method transparency builds scientific literacy
- ✅ Uncertainty shown honestly (not hidden)
- ✅ Context for understanding current changes
- ✅ Human civilization placed in deep time

### Following Working Protocol v2.1
- ✅ Mode selection aligned with task complexity
- ✅ Comprehensive documentation (this file!)
- ✅ Clear integration path
- ✅ Change manifests for all modifications
- ✅ Respects Tony's agency in codebase
- ✅ Agentic work for extensions, guided for integration

---

## 🚀 Recent Updates

### November 1, 2025 - Timeline Hovers + Human-Scale Events

**Added:**
✅ Interactive timeline with 10 hoverable markers  
✅ Younger Dryas annotation (12,900-11,700 ya)  
✅ Medieval Warm Period annotation (950-1250 CE)  
✅ Little Ice Age annotation (1300-1850 CE)  
✅ Educational context for all recent events  
✅ Human-civilization climate stories  
✅ Viking Greenland narrative  
✅ Agricultural revolution context  

**Improved:**
✅ Timeline accessibility (common year notation)  
✅ Multiple timescale understanding  
✅ Connection between climate and human history  
✅ Context for natural vs anthropogenic variability  

**Total Interactive Elements:** 25+ hoverable annotations!

### November 1, 2025 (Afternoon) - Temperature Range Bands + Enhanced Features

**Added:**
✅ **Younger Dryas stylized trace** (turquoise dotted line)  
   - Shows dramatic ~10°C temperature drop from ice core data (Alley 2000, GISP2)
   - Stylized trace based on Greenland ice core δ¹⁸O
   - Makes "invisible" abrupt event visible in smoothed data
   - Educational: Demonstrates proxy resolution differences

✅ **Alley ice core citation** in main info box  
   - Added: "❄️ **Younger Dryas:** Alley (GISP2 ice core, 2000)"
   - Method: Greenland ice core δ¹⁸O
   - Completes scientific attribution for all visible traces

✅ **Save functionality** (PNG/HTML export)  
   - Imported `save_utils` module from star visualizations
   - Users can save as static PNG or interactive HTML
   - HTML files remain fully interactive (zoom, hover still work!)
   - Default filename: `paleoclimate_540Ma_to_present`

✅ **Medieval Warm Period temperature range bands**  
   - **Regional band** (light orange, +0.3 to +0.5°C): North Atlantic/Europe variation
   - **Global band** (dark orange, +0.1 to +0.2°C): Planetary average
   - Horizontal bands show actual temperature variability
   - Makes "invisible" (smoothed) events visible

✅ **Little Ice Age temperature range bands**  
   - **Regional band** (light blue, -0.5 to -1.0°C): North Atlantic/Europe cooling
   - **Global band** (dark blue, -0.2 to -0.3°C): Planetary average
   - Demonstrates "small global changes = large regional impacts"
   - Viking Greenland abandonment now visually obvious

✅ **Enhanced hover text** for MWP/LIA  
   - Now explains temperature range bands
   - Guides users: "🔍 Zoom to [timeframe] to see temperature bands clearly!"
   - Clarifies light vs dark bands (regional vs global)
   - Educational narrative about climate impacts

**Improved:**
✅ Visual demonstration of regional ≠ global climate  
✅ Resolution-aware visualization (what proxies can/can't show)  
✅ Honest communication about data limitations  
✅ Export capability for sharing visualizations  
✅ Scientific completeness (all data sources cited)  

**Key Insight:**
The dual-opacity temperature bands elegantly solve a visualization challenge: how to show climate events that are real but "invisible" in century-resolution data. By adding horizontal bands showing the temperature *ranges* these events had (separate for regional vs global), users can now SEE what the Kaufman curve smooths out. This teaches both climate history AND proxy methodology!

**Total Interactive Elements:** 25+ hoverable annotations + save functionality

### November 8, 2025 - UNEP 2025 Climate Projections & Data Management

**Added:**
✅ **UNEP Emissions Gap Report 2025 projections**
   - Replaced Climate Action Tracker (CAT) 2.5-2.9°C range  
   - Updated to UNEP "Current Policies" scenario with probability distributions
   - Peak warming by 2100: 2.6°C (50%), 2.8°C (66%), 3.3°C (90%)
   - Source: UNEP EGR 2025, Figure 4.2

✅ **Visualization-specific implementations**
   - Full Phanerozoic: 2 horizontal lines (2.6°C, 3.3°C) showing range
   - Dual-scale: 3 horizontal lines (2.6°C, 2.8°C, 3.3°C) with full probabilities
   - Tailored detail level for each visualization context

✅ **Data file path updates**
   - Fixed `temperature_giss_monthly.json` location (now in `data/` subdirectory)
   - Updated path search order: `data/` first, legacy locations as fallback
   - Restored missing instrumental record in dual-scale visualization

**Improved:**
✅ File path conventions documented in Working Protocol v2.3.1  
✅ Data/code separation clarified (data stays local, code in repository)  
✅ More current climate assessment (UNEP 2025 vs. CAT 2024)  
✅ Uncertainty visualization (probability ranges instead of single trajectory)

**Key Insight:**
UNEP 2025 data shows current policies trajectory (2.6-3.3°C) is more pessimistic and uncertain than previous CAT assessment, with explicit probability distributions that better communicate scientific uncertainty to users.

### November 2, 2025 - Scientific Accuracy & Warm Period Context

**Improved:**
✅ **Younger Dryas visualization** - Replaced single impossible trace (-13C) with three nested regional bands  
✅ **Regional climate bands** - Shows spatial heterogeneity: Global (~1C), Regional (~4C), Greenland (~9C)  
✅ **Eemian Interglacial annotation** - Last warm period (+0.6C in our data, +1-2C in literature)  
✅ **Holocene Thermal Maximum** - Warmest natural Holocene (+0.53C at 6,700 ya)  
✅ **Modern context** - Modern temp (+1.28C) exceeds all natural Holocene warmth  
✅ **Scientific honesty** - YD bands stay above Ice Age minimums (physically accurate)  
✅ **Literature citations** - Turney et al. (2020), Dutton et al. (2015) for Eemian  

**Key Insights:**
- Modern warmth (+1.28C) = 2.4x warmer than Holocene Thermal Maximum  
- Modern exceeds Eemian peak (even conservative +0.6C estimate)  
- Younger Dryas regional cooling correctly scaled (no longer exceeds Ice Age!)  
- Three warm period markers (HTM, Eemian, Modern) tell temperature progression story  
- Regional vs global temperature bands teach spatial climate heterogeneity  

**Why This Matters:**
Shows that modern warming is unprecedented in human civilization's timeframe. The warmest natural Holocene period (+0.53C) is less than half current warming. This contextualizes "unprecedented" claims with visual evidence.

### December 2025 - v9 Human Origins Layer

**Added:**
✅ 25 hominin species markers (19 fossil + 6 ghost populations)  
✅ Marine Isotope Stages (MIS) - 10 major glacial/interglacial cycles  
✅ Climate events (Toba supereruption, Green Sahara windows)  
✅ 2025 research integration (Yunxian 2, Five-Branch Model, Cambridge two-population)  
✅ Island SE Asia species (H. floresiensis, H. luzonensis)  
✅ Ghost populations (Superarchaic, West African, Pop A/B, Deep Denisovan, SE Asian)  
✅ Visual differentiation (filled vs open triangles)  
✅ Manual y_offset positioning for clean marker display  
✅ Formatted hovertext with citations  
✅ MIS warm/cold bands with hoverable context  

**Story:**
✅ Climate-driven human evolution narrative  
✅ "Braided stream" of populations mixing and separating  
✅ Sahara as climate gate (open/closed corridors)  
✅ Ghost populations reveal complexity invisible in fossil record  
✅ Island dwarfism parallel evolution  

### October 31, 2025 - v2 Phanerozoic Extension

**Added:**
✅ Scotese Phanerozoic data (540 Ma coverage)  
✅ Intentional overlap (2-5 Ma) showing method differences  
✅ Method transparency in info box  
✅ Hoverable "?" annotations for deep-time events  
✅ Six major climate events with detailed hovers  
✅ Anthropocene boundary annotation  
✅ Full Holocene and Modern method descriptions  
✅ GUI integration (third paleoclimate button)  

**Improved:**
✅ Gap-free coverage (2-540 Ma now complete)  
✅ Educational value (uncertainty as feature, not bug)  
✅ Visual clarity (hover reveals detail, no clutter)  
✅ Scientific honesty (methods explained, overlaps shown)  

### October 30, 2025 - Original Package

**Added:**
✅ Holocene reconstruction (Kaufman et al. 2020)  
✅ Pre-industrial baseline normalization (1850-1900)  
✅ Era labels (Precambrian, Paleozoic, Mesozoic, Cenozoic)  
✅ Seamless integration of three datasets  

---

## 💡 Key Design Decisions

**Log scale x-axis**  
→ Enables seeing both deep time (540 Ma) and recent detail (decades)

**Pre-industrial baseline (1850-1900)**  
→ Policy-relevant, scientifically standard, honest about modern warming

**Temperature anomaly (not absolute)**  
→ More honest about proxy conversion uncertainties

**Four integrated datasets**  
→ Continuous coverage from Cambrian to present

**Intentional overlaps**  
→ Shows method differences, teaches scientific uncertainty

**Interactive timeline**  
→ Common year notation, connects deep time to human experience

**Human-scale events**  
→ Vikings, agriculture, civilization context

**Hoverable "?" annotations**  
→ Clean visual + full detail on demand, no clutter

**Method transparency**  
→ Users learn HOW we know, not just WHAT we know

**Era labels above periods**  
→ Helps users orient in deep time

---

## 📊 Technical Specs

**Data Sources**: 5 integrated datasets (4 historical + 1 future projections)  
**Hominin Species**: 25 markers (19 fossil + 6 ghost populations)  
**MIS Stages**: 10 glacial/interglacial cycles  
**Climate Events**: 3 (Toba, Green Sahara × 2)  
**Data Formats**: CSV (Scotese), JSON (LR04, GISS), CSV (Holocene)  
**Visualization**: Plotly (interactive, zoomable, hoverable)  
**Integration**: Four visualization variants  
**File Size**: ~60 KB code + ~600 KB data  
**Dependencies**: NumPy, Plotly, csv module (all in your project)  
**Time to integrate**: ~10 minutes  
**Interactive Elements**: 50+ hoverable annotations  
**Timescales**: 4 (540 Ma, Pleistocene, Holocene, Modern)  
**Research Integration**: 2025 (Yunxian 2, Cambridge two-population)  

---

## ✅ Testing Checklist

**Files in place:**
- [ ] `paleoclimate_visualization_v2.py` in project root
- [ ] `8c__Phanerozoic_Pole_to_Equator_Temperatures.csv` in project root
- [ ] `fetch_paleoclimate_data.py` in project root
- [ ] `temp12k_allmethods_percentiles.csv` in project root (optional)

**Data downloaded:**
- [ ] LR04 data fetcher run successfully
- [ ] `paleoclimate_data/` directory created
- [ ] Scotese CSV file present

**GUI integration:**
- [ ] Import added to earth_system_visualization_gui.py
- [ ] Function `open_phanerozoic_viz()` added
- [ ] Button added (dark blue, 🦴 icon)
- [ ] Button appears in GUI below other paleoclimate buttons

**Visualization features:**
- [ ] Opens in browser when button clicked
- [ ] Shows navy Scotese curve (2-540 Ma)
- [ ] Shows red LR04 curve (0-5.3 Ma)
- [ ] Shows green Holocene curve (0-12 ka)
- [ ] Shows blue modern curve (1880-2025)
- [ ] Overlap visible in 2-5 Ma range
- [ ] Six "?" annotations visible (different colors)
- [ ] Hover over "?" shows detailed popup
- [ ] Info box shows all four methods
- [ ] Recent event labels visible (PETM, Grande Coupure, etc.)
- [ ] Zoom functionality works
- [ ] Log scale x-axis working
- [ ] Geologic periods color-coded
- [ ] Era labels visible (Paleozoic, Mesozoic, Cenozoic)

**NEW features (November 1-2):**
- [ ] Timeline markers visible (2025, 2015, 1925, 1025, etc.)
- [ ] Hover over timeline markers shows educational text
- [ ] Younger Dryas THREE nested turquoise bands visible (not single trace)
- [ ] YD bands show Global (~1C), Regional (~4C), Greenland (~9C)
- [ ] YD bands stay ABOVE Ice Age minimum (physically accurate!)
- [ ] Eemian Interglacial annotation visible (red/tomato color)
- [ ] Holocene Thermal Maximum annotation visible (green)
- [ ] Medieval Warm Period annotation visible (orange)
- [ ] Little Ice Age annotation visible (blue)
- [ ] All human-scale events have hover text
- [ ] Can zoom to see Younger Dryas → Holocene flip
- [ ] Can zoom to see Medieval → Little Ice Age transition
- [ ] Can see HTM peak (~6,700 ya) in green Kaufman curve
- [ ] Can see Eemian peak (~125,000 ya) in red benthic curve
- [ ] Modern line (+1.28C) clearly exceeds HTM (+0.53C) and Eemian (+0.6C)
- [ ] Timeline connects deep time to human history

---

## 🤝 Troubleshooting

### "Could not load Scotese data"
→ Ensure `8c__Phanerozoic_Pole_to_Equator_Temperatures.csv` is in project root

### Gap visible in 5-10 Ma range
→ Check that line ~308 uses `mask = scotese_ages_ma >= 2.0` (not >= 5.0)

### "?" annotations not hoverable
→ This is a Plotly feature - ensure `hovertext` parameter is set in annotations

### Timeline hovers not working
→ Ensure all timeline annotations have `hovertext` and `hoverlabel` parameters

### Overlapping curves look messy
→ This is intentional! See "Why Show Overlapping Data?" section above

### Missing method descriptions in info box
→ Update to latest version with Holocene/Modern method lines

### Annotations cluttered at recent times
→ Zoom in! At full scale, recent events cluster (normal on log scale)  
→ Older events use "?" hovers to avoid clutter

### Human-scale events not visible
→ Zoom to Holocene/recent period (last 20,000 years)  
→ Events appear when appropriately zoomed

---

## 🌟 The Bottom Line

This isn't just adding a chart. It's:

- **540 million years** of Earth's climate history
- **25 hominin species** showing climate-driven evolution
- **Five datasets** working together seamlessly (4 historical + projections)
- **UNEP 2025** climate projections showing where we're headed
- **Marine Isotope Stages** - the Pleistocene "heartbeat"
- **Ghost populations** revealing hidden human diversity
- **2025 research** integration (Yunxian 2, two-population origin)
- **25+ interactive elements** for deep learning
- **Timeline** connecting deep time to human experience
- **Human stories** (Vikings, agriculture, civilization, evolution)
- **Honest science** showing methods and uncertainties
- **Interactive learning** via hoverable annotations
- **Context** for understanding modern change
- **Current policy trajectory** (2.6-3.3°C by 2100)
- **Preservation** of threatened datasets
- **Inspiration** to think in deep time
- **Foundation** for exoplanet comparisons (future!)

All with **minimal integration work** (~10 minutes).

---

## 🎉 Ready?

1. Copy files to your project
2. Run `python fetch_paleoclimate_data.py`
3. Download Scotese CSV from Zenodo
4. (Optional) Download Holocene CSV
5. Edit `earth_system_visualization_gui.py` (add import, function, button)
6. Run `python earth_system_visualization_gui.py`
7. Click **🦴 Paleoclimate: Phanerozoic (540 Ma - Full History)**
8. **Hover over timeline markers!**
9. **Zoom to see human-scale events!**
10. Explore 540 million years!
11. Hover over the "?" symbols!
12. **Hover over the hominin triangles!**
13. **See how MIS stages shaped human evolution!**
14. Show Paloma the "double hump"!
15. **Show her how Vikings came and went with climate!**
16. **Show her the Younger Dryas flip that made civilization possible!**
17. **Show her how WE emerged from the braided stream!**

---

*From Cambrian Explosion to modern climate change, from deep time to human origins, now in Paloma's Orrery.*

**Package by**: Claude & Tony  
**Updated**: December 2025  
**Following**: Working Protocol v3.2  
**Philosophy**: Data Preservation is Climate Action  
**New Philosophy**: Climate History is Human History  
**Evolution Philosophy**: The Pleistocene wasn't a march but a braided stream  
**Scientific Principle**: Regional ≠ Global Climate  
**Uncertainty**: Normal and Expected!  

**Everything you need is documented here. Let's explore deep time, human time, AND human origins!** 🦴🧬🌍📊
