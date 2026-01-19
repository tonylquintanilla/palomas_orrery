# The Earth System Generator: Forensic Heat Wave Analysis

## A Planetary Visualization Tool for Google Earth Pro

## Overview

This tool is a Python-based forensic instrument designed to visualize **“invisible” climate disasters**. Unlike standard weather maps that show simple air temperature, this generator calculates **Wet Bulb Temperature ($T_w$)** — the metric of biological survival.

It generates 3D KML layers for Google Earth Pro, allowing users to investigate historical and near-future heat events where the *combined stress of heat and humidity* pushed or breached known human physiological limits.

The goal is not to show how hot the Earth has been, but to show **when and where the human body becomes the limiting factor in the Earth system**.

---

## The Scientific Core: The Shift to 31 °C

For decades, climate science cited **35 °C wet-bulb temperature** as the theoretical limit of human survival (Sherwood & Huber, 2010).

**This tool is built on the revised biological consensus (2022–2024):**  
Recent controlled human trials by **Vecellio et al. (Penn State / NIH)** demonstrate that *uncompensable heat stress* occurs at significantly lower thresholds — approximately **31 °C wet-bulb** for young, healthy adults at high humidity.

This means that core body temperature rises uncontrollably *even in shade, even at rest*, without artificial cooling.

This generator visualizes that updated reality.  
A **Black Spike** on the map represents an environment where unprotected human survival is no longer physiologically possible.

---

## How to Interpret These Results  
### (What This Tool *Is* — and *Is Not*)

This generator is **not** a climatological forecasting model, a mortality estimator, or a complete catalog of global extremes.

It is an **exposure-weighted, forensic visualization tool** designed to surface *where and when human physiological limits were approached or breached in inhabited places*, using the best available atmospheric data.

Several clarifications are essential for correct interpretation:

### 1. Upper-Envelope, Not Averages  
The scenarios and trend lines focus on **record or near-record wet-bulb exposure events** near population centers.  
They do *not* represent global maxima, climatological means, or spatially complete fields.

The intent is to visualize the **ceiling of lived human experience**, not the average climate state.

### 2. Observation and Reporting Matter  
Earlier decades — especially **1950–1975** — appear sparse not because heat risk was absent, but because:

- humidity observations were limited and inconsistent  
- wet-bulb metrics were not routinely calculated  
- heat mortality was rarely attributed or reported as such  
- mid-20th-century aerosol cooling temporarily suppressed extremes  

**Absence of data should not be interpreted as absence of danger.**

### 3. Impact ≠ Physiology  
Not all near-lethal wet-bulb events produce visible mass mortality.

Duration, nighttime recovery, housing quality, access to cooling, healthcare capacity, and social response strongly condition outcomes.  
Events such as **Bandar Mahshahr (Iran, 2015)** are included because they validate *biophysical limits*, even where impacts were brief, masked, or poorly documented.

### 4. Trend Lines Are Interpretive Guides  
Any trend shown represents a **directional signal**, not a statistical law.

Linear fits are performed in *calendar time* and displayed on a **logarithmic time axis** to preserve deep historical context.  
They indicate that the *upper bound of human heat exposure is rising*, not that it rises smoothly, uniformly, or predictably.

### 5. Adaptation Can Hide — But Not Eliminate — Risk  
Some modern events (e.g., Persian Gulf 2024) show minimal mortality only because energy-intensive cooling systems functioned.

These cases illustrate **conditional survivability**, not safety.  
Infrastructure failure converts such environments from tolerable to lethal within hours.

In short:  
This project visualizes **where the human body has become the limiting factor in the Earth system**.  
It is intended to provoke correct questions, not to deliver final answers.

---

## The Visualization Layers

For each scenario, the script generates **three modular KML layers** for analysis in Google Earth Pro.

### 1. The Vertical Risk Layer (`_spikes.kml`)

- **What it shows:** 3D spikes rising from the ground  
- **Height:** Proportional to wet-bulb severity  
- **Bio-Corrected Color Scale:**
  - **⚫ BLACK (> 31 °C):** *Lethal Limit* — unsurvivable without artificial cooling  
    *(Vecellio et al., 2022)*
  - **🟣 PURPLE (28–31 °C):** *Extreme Danger* — societal breakdown threshold  
    *(Raymond et al., 2020)*
  - **🔴 RED (26–28 °C):** *High Risk* — cardiovascular strain, labor loss  
    *(Carter et al., 2023)*
  - **🟠 ORANGE (24–26 °C):** *Caution* — rising physiological stress  
    *(Foster et al., 2021)*

### 2. The Thermal Ground Layer (`_heatmap.kml`)

- **What it shows:** Continuous wet-bulb gradient over terrain  
- **Purpose:** Reveals the spatial footprint of heat domes and humidity traps  
- **Color Logic:** Dark/black indicates highest stress; yellow/orange lower stress

### 3. The Human Impact Layer (`_impact.kml`)

- **What it shows:** White population circles  
- **Radius:** Scaled to population size  
- **Interpretation:**  
  When a **Purple or Black Spike** emerges from a **Population Circle**, the visualization indicates a *potential mass-casualty environment*.

---

## Included Forensic Scenarios

The database contains **27 curated events**, ordered chronologically to tell the *Story of Heat* across four distinct eras:

### I. The Historical Baseline (1948–1987)  
*Pre-air-conditioning era; survivability defined by vulnerability*

### II. The Modern Transition (1995–2010)  
*Systemic mortality emerges from “moderate” heat*

### III. The Acceleration Phase (2015–2022)  
*Theoretical limits approached; high-latitude breaches*

### IV. The Current Crisis (2023–2025)  
*Biological limits, ecological collapse, and infrastructure failure*

(See source code for full annotated scenario list.)

---

## Installation & Usage

### Requirements

- Python 3.x  
- Libraries: `requests`, `simplekml`, `numpy`, `scipy`, `matplotlib`, `tkinter`

```bash
pip install requests simplekml numpy scipy matplotlib
