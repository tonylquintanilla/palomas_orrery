# Energy Imbalance Visualization - Project Handoff
## Session Planning Document

**Created:** November 8, 2025  
**For:** Next development session  
**Project:** Add energy imbalance trace to paleoclimate visualizations  
**Philosophy:** Show WHY climate changes (energy), not just THAT it changes (temperature)

---

## 🎯 Project Vision

**The Idea:**
Add a second trace to existing paleoclimate visualizations showing Earth's **energy imbalance** (W/m²) alongside temperature anomaly (°C). This reveals the *driver* of climate change, not just the response.

**Why Energy Imbalance > CO₂ or Forcing:**
- ✅ **More complete**: Captures all energy sources (solar, GHGs, albedo, aerosols)
- ✅ **More physical**: Direct measure of energy accumulation rate
- ✅ **Avoids constant sensitivity assumption**: Climate sensitivity (λ) varies by timescale and state
- ✅ **Shows system lag**: Positive imbalance = "warming still in pipeline"
- ✅ **Pedagogically powerful**: Makes climate inertia visible

**Educational Message:**
- Positive imbalance → Warming in progress (not at equilibrium)
- Zero imbalance → Stable climate (energy in = energy out)
- Negative imbalance → Cooling in progress

---

## 🔬 The Physics

### Energy Imbalance vs. Radiative Forcing

**Radiative Forcing (W/m²):**
- The *perturbation* applied to Earth's energy budget
- "How much extra energy is being trapped by CO₂/etc."
- Calculated, not directly measured
- Assumes forcing → temperature via constant sensitivity (λ)

**Energy Imbalance (W/m²):**
- The *current* net energy flow into the climate system
- "How much energy is accumulating right now"
- Directly measurable (ocean heat, satellites)
- Shows actual system response, including all feedbacks

### The Temperature-Energy Relationship

**Mathematically, temperature change is the time integral of energy imbalance:**

```
ΔT(t) ≈ ∫ [Energy Imbalance / Heat Capacity] dt
```

**What this means:**
- **Energy imbalance** = rate of change (like velocity)
- **Temperature** = accumulated change (like position)
- Positive imbalance → temperature rising
- Zero imbalance → temperature stable (equilibrium)
- Negative imbalance → temperature falling

**The relationship patterns:**

**During stable periods (Holocene):**
- Imbalance oscillates around zero (small wiggles)
- Temperature nearly flat
- System in quasi-equilibrium

**During transitions (deglaciations):**
- Imbalance goes strongly positive (orbital forcing + CO₂ feedback)
- Temperature lags but follows
- Imbalance gradually decreases as temperature rises
- Eventually: new equilibrium

**During modern era (the concerning part):**
- Imbalance strongly positive AND increasing
- Temperature rising but lagging
- Imbalance shows no sign of decreasing
- **We're accelerating with no equilibrium point in sight**

**What makes this visualization powerful:**

1. **Shows causation clearly:** Energy drives temperature (not just correlation)
2. **Reveals system lag:** Temperature takes time to respond (like pushing a heavy object)
3. **Demonstrates modern uniqueness:** Current sustained imbalance is unprecedented
4. **Shows physical inevitability:** Positive imbalance = continued warming (physics, not politics)
5. **Makes "committed warming" concrete:** Current +0.5-1.0 W/m² means ~0.5°C more warming even if imbalance stopped today

**The bathtub analogy:**
- Imbalance = faucet rate minus drain rate
- Temperature = water level
- If faucet > drain, level keeps rising
- Current: faucet wide open, drain partially blocked
- Water level rising but hasn't caught up to inflow rate yet
- **More rise is inevitable until rates balance**

**Expected visual patterns:**

**Leads and lags:**
- Energy imbalance changes first
- Temperature follows with delay
- Like force → acceleration → velocity → position

**Equilibration pattern:**
- Large imbalance → rapid temperature change
- As temperature rises → imbalance decreases (negative feedback in natural cycles)
- Eventually: imbalance → 0, temperature stabilizes
- **Modern era breaks this pattern** (imbalance sustained/increasing)

**Derivative relationship:**
- dT/dt should correlate with energy imbalance magnitude
- Rate of warming ∝ imbalance strength
- This validates the physics visually

**For the Orrery context:**
Perfect parallel to orbital mechanics - both are dynamic systems described by calculus:
- **Orbital mechanics:** Forces → acceleration → velocity → position
- **Climate dynamics:** Forcing → imbalance → temperature change rate → temperature
- Same mathematical structure!

**Pedagogical power for Paloma:**
Not just "it's getting warmer" but "energy is accumulating faster than temperature can respond. Even if we stopped NOW, temperature would keep rising until equilibrium." Makes abstract climate change into concrete energy accumulation - measurable, trackable, understandable as physics.

### Why Climate Sensitivity (λ) Isn't Constant

**Varies by timescale:**
- Fast feedbacks (years): Water vapor, clouds, sea ice → λ ≈ 0.5-0.8 °C/W/m²
- Slow feedbacks (millennia): Ice sheets, vegetation, carbon cycle → λ ≈ 1.0-1.5+ °C/W/m²

**Varies by climate state:**
- Glacial → Interglacial: Ice-albedo feedback amplifies (high λ)
- Warm periods: Different feedbacks dominate
- Hothouse states: New feedbacks (methane clathrates, clouds)

**Energy imbalance sidesteps this problem** - it shows the actual energy accumulation regardless of sensitivity.

---

## 📊 Data Availability by Time Period

### Modern Era (1970-2025) - HIGH QUALITY ✅

**Direct measurements:**

1. **CERES (2000-present)**
   - Satellite measurement of top-of-atmosphere (TOA) imbalance
   - Uncertainty: ±0.1 W/m²
   - Current value: +0.5 to +1.0 W/m²
   - Source: https://ceres.larc.nasa.gov/data/

2. **Ocean Heat Content (1970-present)**
   - Measures ocean warming rate → energy accumulation
   - 90% of energy imbalance goes to oceans
   - Argo floats (2000+) greatly improved coverage
   - Sources: 
     - Levitus et al. (NOAA): https://www.ncei.noaa.gov/products/world-ocean-database
     - Cheng et al.: https://doi.org/10.1007/s00376-022-2195-4

3. **Combined estimates:**
   - von Schuckmann et al. (2020): Earth heat inventory
   - Hansen et al. (2011): Earth's energy imbalance
   - Loeb et al. (2021): CERES + ocean heat synthesis

**Recommendation:** Start here - best data, clearest signal, validates concept.

### Ice Age Cycles (800 ka) - MEDIUM QUALITY ⚠️

**Estimated from:**

1. **Temperature change rates (dT/dt)**
   - LR04 benthic stack shows temperature
   - Calculate rate of change
   - Imbalance ∝ heat capacity × dT/dt

2. **Ice volume changes**
   - Sea level proxies
   - Ice sheet energy changes
   - Albedo feedback contribution

3. **CO₂ from ice cores**
   - EPICA Dome C (we have this!)
   - Calculate radiative forcing component
   - But need to add solar, albedo, etc.

**Challenges:**
- No direct measurement
- Must estimate from temperature + ice volume
- Uncertain heat capacity of system
- Resolution limited to ~1 kyr

**Recommendation:** Phase 2 - extend backward if modern era works well.

### Deep Time (Phanerozoic) - LOW QUALITY ❌

**Would require estimating from:**
- Temperature change rates (very uncertain)
- CO₂ proxy data (GEOCARB, Foster et al.)
- Solar luminosity evolution
- Continental configuration → albedo
- Heat capacity assumptions

**Challenges:**
- Huge uncertainties (±50%+)
- Very coarse temporal resolution (Myr scale)
- Multiple feedback loops poorly constrained

**Recommendation:** Probably not worth it. Consider showing:
- Option A: Forcing instead of imbalance (more appropriate for deep time)
- Option B: Leave deep time as temperature-only
- Option C: Acknowledge uncertainty explicitly

---

## 🎨 Visualization Design Considerations

### Dual Y-Axis Approach

**Left Y-axis:** Temperature Anomaly (°C) - *current traces*
- Keep existing: Scotese, LR04, Holocene, Instrumental
- Colors: Navy, Red, Green, Blue (current scheme)

**Right Y-axis:** Energy Imbalance (W/m²) - *new trace*
- Color options: Orange? Purple? Yellow? (needs to stand out but not clash)
- Line style: Solid? Dashed? (needs to be distinguishable)

**Challenges:**
- Two Y-axes can confuse viewers
- Need clear labeling
- Scale matching matters (what temp range = what imbalance range?)

### Simplified Annotations (Tony's Request)

**What to keep:**
- Geologic periods (color bands)
- Timeline markers (essential for context)
- UNEP projections (2.6-3.3°C lines)

**What to simplify/remove:**
- Reduce number of "?" event annotations?
- Streamline info boxes?
- Focus annotations on temp/imbalance relationship?

**Goal:** Let the data relationship speak for itself, less textual clutter.

### Time Period Coverage Options

**Option 1: Modern Era Only (1970-2025)**
- Cleanest data
- Validates concept
- Shows current imbalance clearly
- Could be its own focused visualization

**Option 2: Modern + Ice Age Cycles (800 ka)**
- Shows glacial/interglacial transitions
- Demonstrates imbalance spikes during terminations
- Shows Holocene near-zero (stable)

**Option 3: Full Phanerozoic with caveats**
- Use forcing for deep time, imbalance for recent
- Or show uncertainty explicitly
- Most comprehensive but most complex

**Recommendation:** Start with Option 1, potentially expand to Option 2.

---

## 🔍 Key Questions for Session Start

### 1. Time Period Scope
- Modern era only (1970-2025)?
- Modern + ice age cycles (800 ka)?
- Full Phanerozoic (with forcing vs. imbalance trade-offs)?

### 2. Data Sources
- Which ocean heat content dataset? (Levitus, Cheng, IAP, etc.)
- Use CERES for 2000-present?
- How to estimate pre-2000 imbalance?

### 3. Visualization File
- Add to existing `paleoclimate_dual_scale.py`?
- Add to `paleoclimate_visualization_full.py`?
- Create new standalone visualization?
- All three?

### 4. Annotation Simplification
- Which annotations are essential?
- Which can be removed for clarity?
- Should energy imbalance have its own annotations (e.g., "Peak imbalance during deglaciation")?

### 5. Color Scheme
- What color for energy imbalance trace?
- Should it use a different colormap entirely (e.g., warm colors for positive, cool for negative)?

### 6. Scale/Range
- What energy imbalance range to show? (0 to +2 W/m²? -1 to +2 W/m²?)
- How to align with temperature scale visually?

---

## 📚 Data Sources to Investigate

### Ocean Heat Content
1. **Cheng et al. (2022)**
   - IAP (Institute of Atmospheric Physics) dataset
   - Monthly, 1940-present
   - Available: http://159.226.119.60/cheng/

2. **Levitus et al. (NOAA)**
   - World Ocean Database
   - Quarterly, 1955-present
   - Available: https://www.ncei.noaa.gov/products/world-ocean-database

3. **von Schuckmann et al. (2020)**
   - Earth heat inventory
   - Multiple components (ocean, land, ice, atmosphere)
   - DOI: 10.5194/essd-12-2013-2020

### CERES TOA Imbalance
- **CERES EBAF** (Energy Balanced and Filled)
- Monthly, 2000-present
- Available: https://ceres.larc.nasa.gov/data/

### Synthesis Papers
1. **Loeb et al. (2021)** - "Satellite and Ocean Data Reveal Marked Increase in Earth's Heating Rate"
   - Combines CERES + Argo floats
   - DOI: 10.1029/2021GL093047

2. **Hansen et al. (2011)** - "Earth's energy imbalance and implications"
   - Early synthesis
   - DOI: 10.5194/acp-11-13421-2011

---

## 💡 Implementation Strategy

### Phase 1: Proof of Concept (Modern Era)
**Goals:**
- Test dual Y-axis visualization
- Validate energy imbalance data loading
- Confirm temperature/imbalance correlation is visible
- Get visual feedback from Tony

**Steps:**
1. Download/prepare ocean heat content data (Cheng or Levitus)
2. Convert to energy imbalance (W/m²)
3. Add to existing visualization (probably `paleoclimate_dual_scale.py` first)
4. Test color schemes
5. Simplify annotations as needed
6. Review with Tony

**Success criteria:**
- Clear visual correlation between temperature and imbalance
- Readable dual-axis labels
- Not visually overwhelming
- Shows "pipeline warming" concept clearly

### Phase 2: Ice Age Extension (If Phase 1 succeeds)
**Goals:**
- Extend imbalance estimates to 800 ka
- Show glacial/interglacial transitions
- Demonstrate imbalance spikes at terminations

**Steps:**
1. Calculate dT/dt from LR04
2. Estimate heat capacity factors
3. Add ice volume contribution
4. Test against known deglaciations
5. Show near-zero imbalance during Holocene stability

### Phase 3: Polish & Documentation
**Goals:**
- Finalize annotation strategy
- Update README
- Add educational hover text
- Prepare for Instagram/sharing

---

## 🚀 Session Start Protocol

**When starting the next session:**

1. **Reference this conversation:** "Continue energy imbalance visualization project"
2. **Confirm scope:** Which time period to start with?
3. **Mode assessment:** Probably Mode 2 (Agentic) for data acquisition and initial implementation
4. **Data needs:** May need Tony to download ocean heat content datasets (Mode 4 Tag-Team)

**Expected workflow:**
- Tony provides vision refinement
- Claude investigates data sources
- Claude implements Phase 1 (modern era)
- Tony provides visual feedback
- Iterate on colors, scales, annotations
- Decide whether to extend to Phase 2

---

## 🎯 Success Metrics

**The visualization will be successful if:**

1. **Scientifically accurate**: Energy imbalance values match published estimates
2. **Visually clear**: Temperature and imbalance relationship is obvious
3. **Pedagogically effective**: Shows "why" climate changes, not just "that" it changes
4. **Not overwhelming**: Simplified annotations, clean design
5. **Paloma-ready**: Explains climate inertia and committed warming visually

**Key insight to convey:**
"Current positive energy imbalance (+0.5-1.0 W/m²) means Earth is still accumulating heat. Even if emissions stopped today, temperature would continue rising for decades until the system reaches equilibrium (zero imbalance)."

---

## 📝 Working Notes

**Why this matters:**
- CO₂ trace alone: Shows one forcing agent, misses solar, albedo, other GHGs
- Radiative forcing: Better, but assumes constant sensitivity
- Energy imbalance: Shows TOTAL system response, actual energy accumulation

**The "full picture" Tony mentioned:**
Energy imbalance integrates:
- ✅ All greenhouse gases (CO₂, CH₄, N₂O, etc.)
- ✅ Solar variability
- ✅ Albedo changes (ice, snow, vegetation)
- ✅ Aerosols
- ✅ All feedbacks
- ✅ Ocean heat uptake lag

**Connection to current visualizations:**
- Temperature shows the RESULT
- Energy imbalance shows the CAUSE
- Together: Complete story of climate dynamics

---

## 🔗 Related Files

**Current visualizations:**
- `paleoclimate_dual_scale.py` - Dual-scale view (likely best starting point)
- `paleoclimate_visualization_full.py` - Full Phanerozoic (540 Ma)
- `paleoclimate_visualization.py` - Original Cenozoic (66 Ma)

**Data files (existing):**
- `data/temperature_giss_monthly.json` - Instrumental record
- `data/lr04_benthic_stack.json` - Ice age temperatures
- `data/epica_co2_800kyr.json` - CO₂ for ice ages

**Will need (new):**
- Ocean heat content data (Cheng or Levitus)
- CERES TOA imbalance (optional, for 2000+)
- Processing script to convert OHC → imbalance

**Documentation:**
- `paleoclimate_readme.md` - Will need updating after implementation
- `working_protocol_v2_3_1.md` - Current collaboration protocol

---

## 🌟 The Bottom Line

**This isn't just adding another line to the plot.** It's:

- Showing the **physics** behind climate change (energy budget)
- Making **climate inertia** visible (positive imbalance = warming in pipeline)
- Demonstrating **committed warming** (what's already inevitable)
- Teaching **Earth as energy system** (not just temperature record)
- Providing **context** for modern warming (fastest imbalance in ice core record)
- Creating **foundation** for understanding climate dynamics

**For Paloma:** Transforms abstract "greenhouse effect" into visible energy accumulation. Shows that climate isn't just "getting warmer" - it's actively accumulating energy from an imbalance, like a bathtub filling faster than it drains.

---

**Ready to build when Tony is!** 🌍⚡📊

**Mode recommendation for next session:** Start with Mode 1 (Guided) to align on scope and data sources, then switch to Mode 2 (Agentic) for implementation.

---

## 🔮 Future Visualization Ideas

### Trajectory Evolution: "How Our Future Changed (2010-2025)"

**Concept:** Show how projected 2100 warming has evolved over 15 years of climate policy.

**The Story:**
- **~2010-2012**: Business-as-usual → 4-5°C by 2100
- **~2015-2018**: Paris Agreement pledges → 3-3.5°C  
- **~2020-2022**: Net-zero commitments → 2.4-2.7°C (pledges) vs. 2.8-3.1°C (policies)
- **2024-2025**: UNEP 2025 → 2.6-3.3°C (policies) vs. 1.8-2.3°C (full pledge implementation)

**What It Shows:**
- ✅ **Real progress**: We've avoided 4-5°C catastrophe (curve bent ~2°C!)
- ⚠️ **Still insufficient**: 2.6°C is still terrible (10 Ma climate equivalent)
- 📊 **Gap is closeable**: The remaining gap to Paris targets (~1°C) is SMALLER than what we've already closed
- 💔 **Promise vs. reality**: Growing gap between pledges and policies

**Visualization Options:**

**Option 1: Animated time-slider**
- User drags slider from 2010 → 2025
- Projected 2100 temperature evolves/drops over time
- See the curve bending downward
- Interactive for education

**Option 2: Multiple trajectory bands**
- Each year's projection as a separate band
- Color-coded by year (gradient from red to blue?)
- Compression toward lower values visible
- Shows momentum then stagnation

**Option 3: Dedicated meta-chart**
- "How Our Future Changed"
- X-axis: Year of estimate (2010-2025)
- Y-axis: Projected 2100 warming
- Two traces:
  - **Policy trajectory** (solid): What's actually happening
  - **Pledge trajectory** (dashed): What's promised
- Shows gap evolution over time

**Data Sources:**
- Climate Action Tracker archives (2009-2025)
- UNEP Emissions Gap Reports (2010-2025)
- IPCC Assessment Reports (AR4, AR5, AR6)
- IEA World Energy Outlook (annual scenarios)

---

### Implementation Gap: "Promise vs. Reality Over Time"

**Concept:** Visualize the gap between climate pledges and actual policies, and how it has evolved.

**The Brutal Truth:**
- 2015-2020: Gap was narrowing (momentum building)
- 2020: Minimum gap (COVID pause + net-zero pledges surge)
- 2022-2025: Gap widening (backtracking, Ukraine war, political shifts)

**What Killed the Momentum?**

**1. Geopolitical Fracture (The Ukraine Effect)**
- **April 2021**: Biden Climate Summit during pandemic
  - Putin attended virtually
  - Xi Jinping participated
  - Global unity on climate (at least superficially)
  - "We're all in this together"
  
- **February 2022**: Russia invades Ukraine
  - Global climate cooperation collapses
  - Energy security trumps climate concerns
  - Fossil fuel infrastructure approved (LNG terminals, pipelines)
  - Russia-West cooperation: **Impossible**
  - China-West tensions rise
  - "Energy independence" becomes priority
  
- **2022-2025**: Fragmented world
  - No major power cooperation on climate
  - Competing blocs (US/EU vs. Russia/China)
  - Climate becomes secondary to security
  - Global South caught in middle

**The contrast:**
- **2021**: Putin at climate summit (unthinkable now)
- **2025**: Russia isolated, China-West tensions, cooperation dead
- **Impact**: ~1°C of warming difference between cooperation and fragmentation scenarios

**2. Herd Mentality (Bidirectional)**
- 2019-2021: Racing to out-pledge each other
- 2022-2025: Permission structure for backtracking

**3. Economic Anxiety**
- COVID recovery costs
- Inflation (2021-2023)
- "Can't afford it now" narrative
- Green investments cut first

**4. Political Backlash**
- Populist movements against climate policies
- Anti-climate politicians elected
- Short-term election cycles vs. long-term climate

**5. Fossil Fuel Counterattack**
- Ukraine war gave opening ("energy security!")
- New infrastructure approved
- Political influence campaigns intensified

**6. Climate Fatigue**
- 30 years of "urgent crisis"
- Diminishing returns on pledge announcements
- Activist burnout
- Public attention deficit

**Visualization Approach:**

```
Gap (Promise - Reality)
  °C
  2.0 ┤
      │                    ╱╱╱ Gap widening (2022-2025)
  1.5 ┤                ╱╱╱╱    Ukraine War
      │            ╱╱╱╱        Economic anxiety
  1.0 ┤        ╱╱╱╱            Political backlash
      │    ╱╱╱╱                
  0.5 ┤╱╱╱╱                    Gap narrowing (2015-2020)
      │                        Paris momentum
  0.0 ┼─────────────────────────────→
      2010  2015  2020  2025  Year

Key Events Annotated:
• 2015: Paris Agreement (gap starts closing)
• 2019: Youth climate strikes, corporate pledges
• 2021: Biden Climate Summit (Putin attends - last moment of unity)
• 2022: Ukraine invasion (cooperation collapses)
• 2023-2024: Political backlash, elections
• 2025: Gap at new high (COP30)
```

**Educational Message:**
"The gap was closing. We had momentum. Then geopolitics, economics, and politics got in the way. The physics doesn't care about our wars or our politics. The question is: can we close the gap again?"

**For Paloma:**
"In 2021, even rival countries were talking about climate together. By 2022, war made that impossible. This is why climate action is hard - it requires cooperation when the world wants to fight."

**Connection to COP30:**
- 30 years since Rio
- 30 COPs
- Gap between promise and reality has grown in recent years
- COP30 in Brazil: Can momentum restart?
- Or will fragmentation continue?

**Data Requirements:**
- Historical CAT estimates (policy vs. pledge trajectories)
- Historical UNEP gap reports
- Timeline of major events (Paris, Biden Summit, Ukraine, elections)
- Country-level backtracking documentation

**Implementation Notes:**
- Could be integrated with trajectory evolution visualization
- Or standalone "meta" chart about climate politics
- Shows that science ≠ politics ≠ action
- Honest about why we're failing despite knowing better

---

**These future ideas connect to the core message:**
- Temperature shows the RESULT
- Energy imbalance shows the CAUSE  
- Trajectory evolution shows PROGRESS (partial)
- Implementation gap shows FAILURE (ongoing)
- Together: Complete picture of climate dynamics AND politics

**"Data preservation is climate action. Honest visualization is climate action. Showing both progress and failure is climate action."**
