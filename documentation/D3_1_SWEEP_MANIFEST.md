# Shell Consolidation -- Phase D3.1 Sweep Manifest

**Session:** May 22, 2026
**Author:** Anthropic's Claude Opus 4.7
**Predecessors:** `D3_1_INVENTORY.md`, `D3_1_MODE7_REVIEW.md`,
`HANDOFF_shell_consolidation_phase_d3_1_v2.md`
**Mode:** Mode 1 -- targeted snippets, file by file, bottom-up by line.
**Implementation note:** Python binary mode (`rb`/`wb`) for every edit.
LF line endings preserved. ASCII only.

---

## Manifest Overview

Five sequential batches. Each batch has its own verification gate
before the next batch starts. Bottom-up line ordering within every
file.

| Batch | Scope | Files | Edit sites | Verification |
|------:|-------|-------|-----------:|--------------|
| 1 | Solar prefix renames | 1 | 9 entries / 27 lines | Inventory re-run: Rule 1 "Sun:" count = 0 |
| 2 | Multi-leader + comet legendgroups | 2 | 9 entries | Inventory re-run: Rule 4 = 1 (orphan only) |
| 3 | Orphan deprecation + Moon Hill Sphere | 2 | 2 entries | Read the diffs |
| 4 | Crust/cloud legendgroup fix | 11 | 11 builders × 2 lines | Inventory re-run: Rule 0 = ~3 (comet residuals) |
| 5 | Rule 2 prepend + newline normalize | 15 | ~100 sites | Strict-mode inventory re-run + Mode 5 visual sampling |

**Module docstring update:** every file touched by any batch gets its
module docstring credit line updated:

```python
# Module updated: May 2026 with Anthropic's Claude Opus 4.7
# (D3.1 sweep: hovertext/legendgroup consolidation)
```

This is one line per file, applied at the end of each file's batch
work.

---

## Pre-flight Setup

Before Batch 1:

```bash
cd <orrery_root>
python3 -m py_compile <each shell file>  # Establish clean baseline
```

Snapshot the current `inventory_per_legend_entry.csv` row counts:

| Conformance | Baseline |
|-------------|---------:|
| OK | 17 |
| FAIL | 116 |
| ORPHAN | 1 |
| Total | 134 |

After each batch, re-run `d3_1_inventory.py` and compare against these
baselines. Numbers should move in the predicted direction.

---

# Batch 1 -- Solar Prefix Renames

**File:** `solar_visualization_shells.py` (1 file)
**Goal:** Rename 9 non-conformant labels to `"Sun: X"` convention.
**Edits per entry:** 3 lines (geometry `name`, geometry `legendgroup`,
info marker `legendgroup`).

## Snippet 1.1 -- Galactic Tide Region (lines 1571, 1582)

**Bottom-up: edit line 1582 first, then 1571.**

```python
# Line 1582 (info marker legendgroup, originally same string as line 1571)
# OLD:
        legendgroup='Galactic Tide Region',
# NEW:
        legendgroup='Sun: Galactic Tide Region',
```

```python
# Line 1571 (geometry name + legendgroup -- this is actually a pair across lines 1571-1572)
# OLD:
        name='Galactic Tide Region',
        legendgroup='Galactic Tide Region',
# NEW:
        name='Sun: Galactic Tide Region',
        legendgroup='Sun: Galactic Tide Region',
```

## Snippet 1.2 -- Outer Oort Cloud (Clumpy) (lines 1511, 1522)

```python
# Line 1522
# OLD:
        legendgroup='Outer Oort Cloud (Clumpy)',
# NEW:
        legendgroup='Sun: Outer Oort Cloud (Clumpy)',
```

```python
# Line 1511
# OLD:
        name='Outer Oort Cloud (Clumpy)',
        legendgroup='Outer Oort Cloud (Clumpy)',
# NEW:
        name='Sun: Outer Oort Cloud (Clumpy)',
        legendgroup='Sun: Outer Oort Cloud (Clumpy)',
```

## Snippet 1.3 -- Hills Cloud (lines 1430, 1442)

```python
# Line 1442
# OLD:
        legendgroup='Hills Cloud (Inner Oort - Toroidal)',
# NEW:
        legendgroup='Sun: Hills Cloud (Inner Oort - Toroidal)',
```

```python
# Line 1430
# OLD:
        name='Hills Cloud (Inner Oort - Toroidal)',
        legendgroup='Hills Cloud (Inner Oort - Toroidal)',
# NEW:
        name='Sun: Hills Cloud (Inner Oort - Toroidal)',
        legendgroup='Sun: Hills Cloud (Inner Oort - Toroidal)',
```

## Snippet 1.4 -- Solar Wind Termination Shock (lines 1076, 1087)

```python
# Line 1087
# OLD:
        legendgroup='Solar Wind Termination Shock',
# NEW:
        legendgroup='Sun: Termination Shock',
```

```python
# Line 1076
# OLD:
        name='Solar Wind Termination Shock',
        legendgroup='Solar Wind Termination Shock',
# NEW:
        name='Sun: Termination Shock',
        legendgroup='Sun: Termination Shock',
```

**Note:** dropping "Solar Wind" from the rename because "Sun:" already
identifies the body. `"Sun: Solar Wind Termination Shock"` is
redundant; `"Sun: Termination Shock"` is the consistent style.

## Snippet 1.5 -- Solar Wind Heliopause (lines 1047, 1058)

```python
# Line 1058
# OLD:
        legendgroup='Solar Wind Heliopause',
# NEW:
        legendgroup='Sun: Heliopause',
```

```python
# Line 1047
# OLD:
        name='Solar Wind Heliopause',
        legendgroup='Solar Wind Heliopause',
# NEW:
        name='Sun: Heliopause',
        legendgroup='Sun: Heliopause',
```

## Snippet 1.6 -- Inner Limit of Oort Cloud (lines 1018, 1029)

```python
# Line 1029
# OLD:
        legendgroup='Inner Limit of Oort Cloud',
# NEW:
        legendgroup='Sun: Inner Limit of Oort Cloud',
```

```python
# Line 1018
# OLD:
        name='Inner Limit of Oort Cloud',
        legendgroup='Inner Limit of Oort Cloud',
# NEW:
        name='Sun: Inner Limit of Oort Cloud',
        legendgroup='Sun: Inner Limit of Oort Cloud',
```

## Snippet 1.7 -- Inner Oort Cloud (lines 989, 1000)

```python
# Line 1000
# OLD:
        legendgroup='Inner Oort Cloud',
# NEW:
        legendgroup='Sun: Inner Oort Cloud',
```

```python
# Line 989
# OLD:
        name='Inner Oort Cloud',
        legendgroup='Inner Oort Cloud',
# NEW:
        name='Sun: Inner Oort Cloud',
        legendgroup='Sun: Inner Oort Cloud',
```

## Snippet 1.8 -- Outer Oort Cloud (lines 960, 971)

```python
# Line 971
# OLD:
        legendgroup='Outer Oort Cloud',
# NEW:
        legendgroup='Sun: Outer Oort Cloud',
```

```python
# Line 960
# OLD:
        name='Outer Oort Cloud',
        legendgroup='Outer Oort Cloud',
# NEW:
        name='Sun: Outer Oort Cloud',
        legendgroup='Sun: Outer Oort Cloud',
```

## Snippet 1.9 -- Sun's Gravitational Influence (lines 931, 942)

```python
# Line 942
# OLD:
        legendgroup='Sun\'s Gravitational Influence',
# NEW:
        legendgroup='Sun: Gravitational Influence',
```

```python
# Line 931
# OLD:
        name='Sun\'s Gravitational Influence',
        legendgroup='Sun\'s Gravitational Influence',
# NEW:
        name='Sun: Gravitational Influence',
        legendgroup='Sun: Gravitational Influence',
```

## Batch 1 Verification

```bash
python3 -m py_compile solar_visualization_shells.py
python3 d3_1_inventory.py
# Inspect inventory_per_legend_entry.csv:
#   Expect: 0 rows with "label does not start with 'Sun:'" violation
#   Expect: Solar's OK count rises by 9
```

---

# Batch 2 -- Multi-Leader + Comet Legendgroups

**Files:** `neptune_visualization_shells.py`, `comet_visualization_shells.py`
**Goal:** Fix Q4 (Neptune double leader) and Q5 (MAPS missing
legendgroups, per Mode 7 reclassification).

## Snippet 2.1 -- Neptune diamond `showlegend=False` (line 616)

**File:** `neptune_visualization_shells.py`

```python
# Line 616
# OLD:
        showlegend=True
    ))
   
    return traces
# NEW:
        showlegend=False
    ))
   
    return traces
```

**Why:** the diamond at line 604 sits inside `create_neptune_magnetosphere`
and shares legendgroup `'Neptune: Magnetosphere'` with the envelope at
line 567. Both having `showlegend=True` creates two legend entries that
toggle together. The diamond stays in the group but should not claim a
second legend row.

## Snippet 2.2 -- Comet file: bottom-up legendgroup additions

**File:** `comet_visualization_shells.py`
**Bottom-up:** line 1976, 1966, 1956, 1819, 1810, 1801, 1763, 564, 472.

### 2.2.a -- Inactive ion tail placeholder (the second branch, line 1976)

```python
# Line 1971-1978
# OLD:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Ion Tail (inactive, >{COMET_FEATURE_THRESHOLDS["ion_tail"]:.1f} AU)',
                showlegend=True,
                hoverinfo='skip'
            ))
# NEW:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Ion Tail (inactive, >{COMET_FEATURE_THRESHOLDS["ion_tail"]:.1f} AU)',
                legendgroup=f'{comet_name}: Ion Tail',
                showlegend=True,
                hoverinfo='skip'
            ))
```

### 2.2.b -- Inactive dust tail placeholder (second branch, line 1966)

```python
# Line 1961-1968
# OLD:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Dust Tail (inactive, >{COMET_FEATURE_THRESHOLDS["dust_tail"]:.1f} AU)',
                showlegend=True,
                hoverinfo='skip'
            ))
# NEW:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Dust Tail (inactive, >{COMET_FEATURE_THRESHOLDS["dust_tail"]:.1f} AU)',
                legendgroup=f'{comet_name}: Dust Tail',
                showlegend=True,
                hoverinfo='skip'
            ))
```

### 2.2.c -- Inactive coma placeholder (second branch, line 1956)

```python
# Line 1951-1958
# OLD:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Coma (inactive, >{COMET_FEATURE_THRESHOLDS["coma"]:.1f} AU)',
                showlegend=True,
                hoverinfo='skip'
            ))
# NEW:
            fig.add_trace(go.Scatter3d(
                x=[None], y=[None], z=[None],
                mode='markers',
                marker=dict(size=0, color='gray'),
                name=f'{comet_name}: Coma (inactive, >{COMET_FEATURE_THRESHOLDS["coma"]:.1f} AU)',
                legendgroup=f'{comet_name}: Coma',
                showlegend=True,
                hoverinfo='skip'
            ))
```

### 2.2.d -- Inactive ion tail (first far-distance branch, line 1819)

```python
# Line 1814-1821
# OLD:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Ion Tail (inactive, >{COMET_FEATURE_THRESHOLDS["ion_tail"]:.1f} AU)',
            showlegend=True,
            hoverinfo='skip'
        ))
# NEW:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Ion Tail (inactive, >{COMET_FEATURE_THRESHOLDS["ion_tail"]:.1f} AU)',
            legendgroup=f'{comet_name}: Ion Tail',
            showlegend=True,
            hoverinfo='skip'
        ))
```

### 2.2.e -- Inactive dust tail (first far-distance branch, line 1810)

```python
# Line 1805-1812
# OLD:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Dust Tail (inactive, >{COMET_FEATURE_THRESHOLDS["dust_tail"]:.1f} AU)',
            showlegend=True,
            hoverinfo='skip'
        ))
# NEW:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Dust Tail (inactive, >{COMET_FEATURE_THRESHOLDS["dust_tail"]:.1f} AU)',
            legendgroup=f'{comet_name}: Dust Tail',
            showlegend=True,
            hoverinfo='skip'
        ))
```

### 2.2.f -- Inactive coma (first far-distance branch, line 1801)

```python
# Line 1796-1803
# OLD:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Coma (inactive, >{COMET_FEATURE_THRESHOLDS["coma"]:.1f} AU)',
            showlegend=True,
            hoverinfo='skip'
        ))
# NEW:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None],
            mode='markers',
            marker=dict(size=0, color='gray'),
            name=f'{comet_name}: Coma (inactive, >{COMET_FEATURE_THRESHOLDS["coma"]:.1f} AU)',
            legendgroup=f'{comet_name}: Coma',
            showlegend=True,
            hoverinfo='skip'
        ))
```

### 2.2.g -- MAPS nucleus-gone placeholder (line 1764)

```python
# Line 1760-1765
# OLD:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None], mode='markers',
            marker=dict(size=0, color='gray'),
            name='MAPS: Nucleus (disintegrated April 4, 2026)',
            showlegend=True, hoverinfo='skip'
        ))
# NEW:
        fig.add_trace(go.Scatter3d(
            x=[None], y=[None], z=[None], mode='markers',
            marker=dict(size=0, color='gray'),
            name='MAPS: Nucleus (disintegrated April 4, 2026)',
            legendgroup='MAPS: Nucleus',
            showlegend=True, hoverinfo='skip'
        ))
```

**Editorial decision applied (Tony, post-Mode 7 review):**
Active-state and inactive-state traces share NO legendgroups. Each
placeholder gets its own group matching the structural element it
represents. The active-state traces (e.g., `'MAPS: Dust Trail (Remains)'`
at line 1756) keep their own implicit groups; if Tony later wants them
unified with the inactive groups, that's a separate change.

### 2.2.h -- MAPS disintegration marker legendgroup (line 564)

```python
# Line 558-565
# OLD:
        marker=dict(
            size=8,
            color='rgb(80, 200, 120)',
            symbol='diamond',
            opacity=0.95,
            line=dict(color='white', width=1)
        ),
        name='MAPS: Disintegration',
        text=[hover],
        customdata=['MAPS: Disintegration'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
# NEW:
        marker=dict(
            size=8,
            color='rgb(80, 200, 120)',
            symbol='diamond',
            opacity=0.95,
            line=dict(color='white', width=1)
        ),
        name='MAPS: Disintegration',
        legendgroup='MAPS: Disintegration',
        text=[hover],
        customdata=['MAPS: Disintegration'],
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
```

### 2.2.i -- Comet nucleus legendgroup (line 472)

```python
# Line 467-473
# OLD:
        marker=dict(
            size=4,
            color='rgb(50, 50, 50)',  # Very dark gray, almost black
            opacity=0.9,
            line=dict(color='white', width=1)  # Subtle white outline for visibility
        ),
        name=f'{comet_name}: Nucleus',
        text=[description],
        customdata=[f'{comet_name}: Nucleus'], 
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
# NEW:
        marker=dict(
            size=4,
            color='rgb(50, 50, 50)',  # Very dark gray, almost black
            opacity=0.9,
            line=dict(color='white', width=1)  # Subtle white outline for visibility
        ),
        name=f'{comet_name}: Nucleus',
        legendgroup=f'{comet_name}: Nucleus',
        text=[description],
        customdata=[f'{comet_name}: Nucleus'], 
        hovertemplate='%{text}<extra></extra>',
        showlegend=True
```

## Batch 2 Verification

```bash
python3 -m py_compile neptune_visualization_shells.py
python3 -m py_compile comet_visualization_shells.py
python3 d3_1_inventory.py
# Expect: Rule 4 "multiple leaders" violations drop from 4 to 1
#   (only create_neptune_magnetic_poles ORPHAN remains, expected).
# Expect: comet Rule 0 entries reclassified -- no more <none> legendgroups
#   on showlegend=True traces in this file.
```

---

# Batch 3 -- Orphan Deprecation + Moon Hill Sphere

**Files:** `neptune_visualization_shells.py`, `moon_visualization_shells.py`
**Goal:** Deprecate orphan function with docstring; rename Moon Hill Sphere.

## Snippet 3.1 -- Deprecate `create_neptune_magnetic_poles`

**File:** `neptune_visualization_shells.py`

```python
# Line 621-622
# OLD:
def create_neptune_magnetic_poles(center_position, offset_distance, tilt, azimuth):
    """Creates a simplified visualization of Neptune's magnetic poles and axis."""
# NEW:
def create_neptune_magnetic_poles(center_position, offset_distance, tilt, azimuth):
    """Creates a simplified visualization of Neptune's magnetic poles and axis.

    DEPRECATED (D2 Option C, May 2026): This function is no longer called.
    The D2 sweep replaced the multi-trace magnetic-axis visualization with a
    single diamond marker rendered inline inside
    create_neptune_magnetosphere() at the offset magnetic center (~0.55
    Neptune radii, 47 deg tilt; Voyager 2, 1989). Retained in source for
    historical reference. The post-D2 inventory script flags this function's
    four showlegend=True traces; that flagging is expected and harmless.

    Module updated: May 2026 with Anthropic's Claude Opus 4.7 (D3.1 sweep)
    """
```

## Snippet 3.2 -- Moon Hill Sphere rename

**File:** `moon_visualization_shells.py`

```python
# Line 553
# OLD:
    trace_name = 'Hill Sphere'
# NEW:
    trace_name = 'Moon: Hill Sphere'
```

**Why:** the trace_name flows into `name=trace_name` and
`legendgroup=trace_name` at lines 565-566, so one edit handles both.

## Batch 3 Verification

```bash
python3 -m py_compile neptune_visualization_shells.py
python3 -m py_compile moon_visualization_shells.py
grep -A 2 "DEPRECATED" /path/to/neptune_visualization_shells.py
grep "trace_name = 'Moon: Hill Sphere'" /path/to/moon_visualization_shells.py
```

---

# Batch 4 -- Crust/Cloud Legendgroup Fix

**Files:** 11 files (one builder each).
**Goal:** Add `legendgroup` to the surface `go.Mesh3d` trace; strip
`(Info)` suffix from the info marker's `name` and `legendgroup`.

**Pattern (applies to all 11 builders):**

The current state in every builder:

```python
# Surface trace (at higher line number)
surface_trace = go.Mesh3d(
    ...
    name=f"<Body>: {layer_info['name']}",
    showlegend=True,
    # NO legendgroup -- this is the bug
    ...
)

# (other code, including fibonacci sphere generation)

# Info marker (at lower line number)
trace_name = f"<Body>: {layer_info['name']} (Info)"   # (Info) suffix is wrong now

hover_trace = go.Scatter3d(
    ...
    name=trace_name,           # gets the (Info) suffix
    legendgroup=trace_name,    # gets the (Info) suffix
    ...
    showlegend=False,
)
```

**Two edits per builder, bottom-up:**

1. **Strip `(Info)` from trace_name definition** (lower line first per
   protocol).
2. **Add `legendgroup=f"<Body>: {layer_info['name']}"` to surface_trace**
   (higher line). Use the literal f-string, not the variable, because
   `trace_name` is not yet defined at the surface trace's position in
   the function body.

## Snippet 4.1 -- earth_visualization_shells.py (`create_earth_crust_shell`)

```python
# Line 444 (bottom edit)
# OLD:
    trace_name = f"Earth: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Earth: {layer_info['name']}"
```

```python
# Line 381-382 (top edit)
# OLD:
        name=f"Earth: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Earth: {layer_info['name']}",
        legendgroup=f"Earth: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.2 -- venus_visualization_shells.py (`create_venus_crust_shell`)

```python
# Line 298
# OLD:
    trace_name = f"Venus: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Venus: {layer_info['name']}"
```

```python
# Line ~235 (just after name=)
# OLD:
        name=f"Venus: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Venus: {layer_info['name']}",
        legendgroup=f"Venus: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.3 -- mars_visualization_shells.py (`create_mars_crust_shell`)

```python
# Bottom-up: find the `trace_name = f"Mars: {layer_info['name']} (Info)"`
# line in create_mars_crust_shell (around line 396 based on inventory's
# entry at line 331 for surface_trace; the actual trace_name (Info)
# definition is below). Verify in source before editing.

# Strip the (Info) suffix:
# OLD:
    trace_name = f"Mars: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Mars: {layer_info['name']}"
```

```python
# Surface trace at line 331:
# OLD:
        name=f"Mars: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Mars: {layer_info['name']}",
        legendgroup=f"Mars: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.4 -- pluto_visualization_shells.py (`create_pluto_crust_shell`)

```python
# Line 340
# OLD:
    trace_name = f"Pluto: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Pluto: {layer_info['name']}"
```

```python
# Line 277
# OLD:
        name=f"Pluto: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Pluto: {layer_info['name']}",
        legendgroup=f"Pluto: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.5 -- eris_visualization_shells.py (`create_eris_crust_shell`)

```python
# Line 333
# OLD:
    trace_name = f"Eris: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Eris: {layer_info['name']}"
```

```python
# Line 270
# OLD:
        name=f"Eris: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Eris: {layer_info['name']}",
        legendgroup=f"Eris: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.6 -- moon_visualization_shells.py (`create_moon_crust_shell`)

```python
# Find the (Info)-suffixed trace_name in create_moon_crust_shell.
# Inventory shows surface_trace at line 345.

# Strip the (Info) suffix at the trace_name = ... line below:
    trace_name = f"Moon: {layer_info['name']} (Info)"
# Change to:
    trace_name = f"Moon: {layer_info['name']}"
```

```python
# Line 345 area (surface trace):
# OLD:
        name=f"Moon: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Moon: {layer_info['name']}",
        legendgroup=f"Moon: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.7 -- jupiter_visualization_shells.py (`create_jupiter_cloud_layer_shell`)

```python
# Find the (Info)-suffixed trace_name in create_jupiter_cloud_layer_shell
# (the inventory shows surface at line 346):
    trace_name = f"Jupiter: {layer_info['name']} (Info)"
# Change to:
    trace_name = f"Jupiter: {layer_info['name']}"
```

```python
# Line 346 area:
# OLD:
        name=f"Jupiter: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Jupiter: {layer_info['name']}",
        legendgroup=f"Jupiter: {layer_info['name']}",
        showlegend=True,
```

## Snippet 4.8 -- saturn_visualization_shells.py (`create_saturn_cloud_layer_shell`)

```python
    trace_name = f"Saturn: {layer_info['name']} (Info)"
# Change to:
    trace_name = f"Saturn: {layer_info['name']}"
```

```python
# Line 384 area:
        name=f"Saturn: {layer_info['name']}",
        legendgroup=f"Saturn: {layer_info['name']}",  # ADD
        showlegend=True,
```

## Snippet 4.9 -- uranus_visualization_shells.py (`create_uranus_cloud_layer_shell`)

```python
# Line 329
# OLD:
    trace_name = f"Uranus: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Uranus: {layer_info['name']}"
```

```python
# Line 266
        name=f"Uranus: {layer_info['name']}",
        legendgroup=f"Uranus: {layer_info['name']}",  # ADD
        showlegend=True,
```

## Snippet 4.10 -- neptune_visualization_shells.py (`create_neptune_cloud_layer_shell`)

```python
# Line 342
# OLD:
    trace_name = f"Neptune: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Neptune: {layer_info['name']}"
```

```python
# Line 279
        name=f"Neptune: {layer_info['name']}",
        legendgroup=f"Neptune: {layer_info['name']}",  # ADD
        showlegend=True,
```

## Snippet 4.11 -- planet9_visualization_shells.py (`create_planet9_surface_shell`)

```python
# Line 183
# OLD:
    trace_name = f"Planet 9: {layer_info['name']} (Info)"
# NEW:
    trace_name = f"Planet 9: {layer_info['name']}"
```

```python
# Line 120-121
# OLD:
        name=f"Planet 9: {layer_info['name']}",
        showlegend=True,
# NEW:
        name=f"Planet 9: {layer_info['name']}",
        legendgroup=f"Planet 9: {layer_info['name']}",
        showlegend=True,
```

## Batch 4 Verification

```bash
for f in earth venus mars pluto eris moon jupiter saturn uranus neptune planet9; do
    python3 -m py_compile ${f}_visualization_shells.py
done
python3 d3_1_inventory.py
# Expect: "leader trace missing legendgroup attribute" drops from ~15 to ~3
#   (only comet entries remain -- already fixed in Batch 2; if any still
#   flagged, it's a tooling artifact)
```

---

# Batch 5 -- Rule 2 Prepend Sweep + Newline Normalization

**Files:** all 15 `*_visualization_shells.py`.
**Goal:** Prepend legend label to every info marker's hover text. In
the same edit, normalize any `\n` (literal newline character) to `<br>`
inside the hover string.

## Pattern A -- `create_info_marker(x, y, z, color, desc_text, legendgroup)` calls

The 22 `create_info_marker(...)` call sites typically look like:

```python
mag_desc = ("Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side<br>"
           "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.<br>"
           ...)
traces.append(create_info_marker(
    x[0], y[0], z[0],
    'rgb(200, 200, 255)', mag_desc, 'Jupiter: Magnetosphere'
))
```

**Edit:** modify the FIRST line of the description string to prepend
the legend label as a header:

```python
mag_desc = (f"Jupiter: Magnetosphere<br><br>"
           "Jupiter's magnetosphere extends up to 100 Jupiter radii on the sunward side<br>"
           "and forms a magnetotail stretching beyond Saturn's orbit in the opposite direction.<br>"
           ...)
```

The legend label is the 6th positional argument to `create_info_marker`
(the `legendgroup` parameter). It MUST be a string literal at the call
site -- if it is an f-string like `f"Saturn: {ring['name']}"`, the
prepend uses the same f-string template:

```python
# At a per-loop-iteration call site:
ring_desc = (f"Saturn: {ring['name']}<br><br>"
            "Saturn's ring system is the most extensive...<br>"
            ...)
traces.append(create_info_marker(
    x[0], y[0], z[0], color, ring_desc,
    f"Saturn: {ring['name']}"
))
```

## Pattern B -- inline `go.Scatter3d(text=[layer_info['description']])` info markers

The crust/cloud shell pattern after Batch 4 fix:

```python
trace_name = f"Earth: {layer_info['name']}"
hover_trace = go.Scatter3d(
    ...
    name=trace_name,
    legendgroup=trace_name,
    text=[layer_info['description']],   # <- this is the site
    customdata=[f"Earth: {layer_info['name']}"],
    hovertemplate='%{text}<extra></extra>',
    showlegend=False
)
```

**Edit:** prepend the trace_name to the text content:

```python
text=[f"{trace_name}<br><br>{layer_info['description']}"],
```

## Pattern C -- loop-generated traces (radiation belts, rings, FAC)

Loop bodies that emit one info marker per iteration:

```python
for belt in belt_data:
    ...
    info_text = belt['description']
    traces.append(go.Scatter3d(
        ...
        text=[info_text],
        ...
    ))
```

**Edit:** prepend the per-iteration legend label expression:

```python
for belt in belt_data:
    ...
    info_text = f"Neptune: {belt['name']}<br><br>{belt['description']}"
    traces.append(go.Scatter3d(
        ...
        text=[info_text],
        ...
    ))
```

**Loop-name variable lookup table (varies per builder):**

| Builder | Per-iteration name expression |
|---------|-------------------------------|
| `create_neptune_radiation_belts` | `f"Neptune: {belt['name']}"` |
| `create_jupiter_radiation_belts` | `f"Jupiter: {belt['name']}"` (verify; may use `belt_names[i]`) |
| `create_saturn_radiation_belts` | `f"Saturn: {belt['name']}"` (verify) |
| `create_uranus_radiation_belts` | `f"Uranus: {belt['name']}"` (verify) |
| `create_earth_radiation_belts` | `f"Earth: {belt['name']}"` (verify) |
| `create_field_aligned_currents` (Neptune) | `f"Neptune: {params['name']}"` |
| Ring system builders | `f"<Body>: {ring_info['name']}"` |

The implementation session should grep each builder for the iteration
variable name and confirm before editing.

## Pattern D -- newline normalization (combined with prepend)

In the same edit where text is being changed, replace any literal
`\n` characters inside the string with `<br>`:

```python
# OLD:
"The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and\n"
"the stratosphere (12-50 km) which contains the ozone layer.\n"

# NEW:
"The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and<br>"
"the stratosphere (12-50 km) which contains the ozone layer.<br>"
```

This catches items 43 (Uranus magnetosphere hovertext truncation) and
44 (Neptune magnetosphere hovertext truncation) from the deferred list.

## Per-File Site Inventory for Batch 5

The full list of edit sites, file by file. Each row is one
construction site requiring a prepend.

### `mercury_visualization_shells.py` (3 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 197 | `create_mercury_magnetosphere_shell` | A | `'Mercury: Magnetosphere'` |
| 319 | `create_mercury_radiation_zone_shell` | A | `'Mercury: Radiation Zone'` (verify literal) |
| 387 | `create_mercury_sodium_tail` (or similar) | A | `'Mercury: Sodium Tail'` (verify) |

### `venus_visualization_shells.py` (3 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 298 | `create_venus_crust_shell` | B | `trace_name` (set by Batch 4) |
| 647 | `create_venus_magnetosphere_shell` | A | `'Venus: Magnetosphere'` (verify) |
| 719 | `create_venus_atmosphere_shell` | A | `'Venus: Atmosphere'` (verify) |

### `earth_visualization_shells.py` (multiple sites)

The script's per-trace CSV is the authoritative count. Sites include:

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 446 | `create_earth_crust_shell` | B | `trace_name` (set by Batch 4) |
| ~675-680 | `create_earth_magnetosphere_shell` | A | `'Earth: Magnetosphere'` (verify literal) |
| Multiple sites in radiation belts, atmosphere layers, Hill Sphere | A/B/C | per loop variable |

### `moon_visualization_shells.py` (sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 577 | `create_moon_hill_sphere` | B | `trace_name` (set by Batch 3) |
| Other moon shell sites | B | `trace_name` per builder |

### `mars_visualization_shells.py` (~5 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 735 | `create_mars_magnetosphere_shell` | A | `'Mars: Magnetosphere'` |
| 824 | `create_mars_induced_magnetosphere` | A | `'Mars: Induced Magnetosphere'` (this resolves item 42) |
| Mars Hill Sphere | B | `trace_name` |
| Atmosphere layers | B | `trace_name` per layer |

### `jupiter_visualization_shells.py` (~6 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 574 | `create_jupiter_magnetosphere_shell` | A | `'Jupiter: Magnetosphere'` |
| 649 | `create_jupiter_io_plasma_torus` | A | `'Jupiter: Io Plasma Torus'` (verify) |
| 739 | `create_jupiter_radiation_belts` | C (loop) | `f"Jupiter: {belt['name']}"` |
| 970 | (additional info marker) | A | verify at source |
| Atmosphere/ring sites | B/C | per iteration |

### `saturn_visualization_shells.py` (~5 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 655 | `create_saturn_magnetosphere_shell` | A | `'Saturn: Magnetosphere'` |
| 756 | (rings or radiation) | A | verify |
| 875 | (radiation belts loop) | C | per iteration |
| 1170 | (additional info marker) | A | verify |

### `uranus_visualization_shells.py` (~4 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 534 | `create_uranus_magnetosphere_shell` | A | `'Uranus: Magnetosphere'` (resolves item 43 `\n` -> `<br>`) |
| 687 | (radiation or rings) | A | verify |
| 1061 | (additional info marker) | A | verify |
| Cloud layer crust | B | `trace_name` (set by Batch 4) |

### `neptune_visualization_shells.py` (~5 sites)

| Line | Builder | Pattern | Label expression |
|-----:|---------|--------:|------------------|
| 590 | `create_neptune_magnetosphere` | A | `'Neptune: Magnetosphere'` (resolves item 44 `\n` -> `<br>`) |
| 604 | D2 diamond inline | inline | prepend `'Neptune: Magnetic Field Center'` to the existing inline text list at line 611 |
| 966 | `create_neptune_radiation_belts` | C (loop) | `f"Neptune: {belt['name']}"` (resolves item 45) |
| 1084 | `create_field_aligned_currents` | C (loop) | `f"Neptune: {params['name']}"` (resolves item 46) |
| 1609 | (rings/arcs info marker) | A | verify at source |
| Cloud layer | B | `trace_name` (set by Batch 4) |

### `pluto_visualization_shells.py`, `eris_visualization_shells.py`, `planet9_visualization_shells.py`, `comet_visualization_shells.py`, `asteroid_belt_visualization_shells.py`, `solar_visualization_shells.py`

Crust/cloud sites (Pattern B): each uses `trace_name` (set by Batch 4)
and prepends to `text=[layer_info['description']]`.

Solar sites: ~17 sites, all Pattern B. Each uses `trace_name` or a
literal label set by Batch 1 renames. The implementation session
should walk through `solar_visualization_shells.py` linearly,
identifying each `text=[...]` info marker and applying Pattern B.

Comet sites: ~6 sites including `create_comet_coma`,
`create_comet_dust_tail`, `create_comet_ion_tail`, `create_comet_anti_tail`,
`create_maps_disintegration_marker`, `create_comet_nucleus`. The
`create_maps_disintegration_marker` already has a `hover` variable
holding the description (line 540-549) -- prepend `'MAPS:
Disintegration<br><br>'` to its definition.

Asteroid belt: category file; the labels are population names like
`'Hilda Family'`, `'Jupiter Trojans (Greeks - L4)'`. The prepend uses
the population name as-is (no body prefix is meaningful here). Same
mechanical fix, label IS the legend name.

## Implementation Plan for Batch 5

Because the site count is large, the implementation session should
process this in sub-batches by file, with verification after each
sub-batch:

```
5.a -- mercury (3 sites)        -> compile, inventory check
5.b -- venus (3 sites)          -> compile, inventory check
5.c -- moon (~3 sites)          -> compile, inventory check
5.d -- earth (~6 sites)         -> compile, inventory check
5.e -- mars (~5 sites)          -> compile, inventory check
5.f -- jupiter (~6 sites)       -> compile, inventory check
5.g -- saturn (~5 sites)        -> compile, inventory check
5.h -- uranus (~4 sites)        -> compile, inventory check
5.i -- neptune (~5 sites)       -> compile, inventory check
5.j -- pluto (~2 sites)         -> compile, inventory check
5.k -- eris (~2 sites)          -> compile, inventory check
5.l -- planet9 (~1 site)        -> compile, inventory check
5.m -- comet (~6 sites)         -> compile, inventory check
5.n -- asteroid_belt (~4 sites) -> compile, inventory check
5.o -- solar (~17 sites)        -> compile, inventory check
```

Bottom-up by line number within each file. The implementation session
should view each file, identify the actual edit sites against the
inventory's per-trace CSV, and produce snippets for each one. The
patterns above (A/B/C/D) and the per-file site inventory provide the
roadmap.

## Batch 5 Verification

**Necessary:** re-run `d3_1_inventory.py` to confirm Rule 2 FAIL count
drops from ~102 to near zero. The script's check is a weak proxy
(`body.lower() in m_hover.lower()`) but will pass trivially because the
prepended label now starts every hover.

**Sufficient:** Mode 5 visual sampling by Tony. Open the orrery, render
a representative set of bodies (Mercury, Earth, Jupiter, Neptune,
Solar/Oort, a comet), hover over the info markers, confirm:

1. Every hover starts with the legend label as a header.
2. The header is visually distinguished (typically by `<br><br>`
   producing a blank line between the header and description).
3. No `\n` characters render as literal text anywhere.
4. Toggling a legend entry hides both the geometry and the info
   marker.

If Mode 5 passes, Batch 5 is complete.

---

# Post-Sweep Tasks

After all five batches:

1. **Update module docstrings.** Every file touched gets the credit
   line `# Module updated: May 2026 with Anthropic's Claude Opus 4.7
   (D3.1 sweep: hovertext/legendgroup consolidation)`.

2. **Run provenance scanner.** `provenance_scanner.py` should report
   0 Tier-1 findings on touched files.

3. **Update the items table.** Mark items 43, 44, 45, 46, 54, 55, 56,
   57, 58, 59, 60 as DONE.

4. **Update Module Atlas.** Run `module_atlas.py` to regenerate
   `MODULE_ATLAS.md` with the new function signatures and credit lines.

5. **Final visual verification.** Tony runs the full GUI on Windows
   (the development target) and renders representative views from each
   body family. Mode 5 across the full visualization surface.

6. **Deploy to GitHub.** Standard deployment workflow.

7. **Write the D3.1 closeout summary** for the next handoff. Capture
   what worked, what surprised, what the verification script missed,
   and any lessons that should be added to the protocol archive.

---

# Risks Flagged for the Implementation Session

These are not new findings -- they are reminders documented across
the inventory and Mode 7 review. Listed here for the manifest
executor's checklist.

1. **The script's Rule 2 check is a weak proxy.** Post-sweep, the
   script will report "pass" trivially because the body name is now
   in the leading header. Real verification is Mode 5 visual.

2. **Loop-name variables vary across builders.** The lookup table in
   Pattern C is partial. The executor should grep each loop body for
   the actual per-iteration name expression before editing.

3. **Bottom-up editing matters most in Batch 5.** A single file may
   have 5-6 prepend sites. Edit them from highest line number to
   lowest; otherwise line numbers shift and the snippet positions
   become wrong.

4. **Mars Hill Sphere is OK in the source.** Mode 7 flagged it as
   "one OK entry and one FAIL from same builder" -- but inspection
   (lines 894-921) shows the surface trace already has correct
   `legendgroup`. The FAIL is a script aggregation artifact, not a
   real bug. No fix needed.

5. **The orphan function `create_neptune_magnetic_poles`** has 4
   `showlegend=True` traces internally. After deprecation comment is
   added (Batch 3), the script will still flag it as ORPHAN with
   multiple-leaders. This is expected and harmless. Do NOT fix the
   internal trace state of an orphan function.

6. **Python binary mode for every edit.** Files contain Unicode
   characters (degree symbols, em dashes in some hover strings).
   Using `sed` will corrupt them. Use the `bash_tool` Python pattern
   from the protocol's Unicode-Safe Agentic Editing section.

7. **Pre-test gate after each batch.** Run `xvfb-run` GUI launch test
   after every batch, not just at the end. Catches runtime errors
   that compile checks miss.

---

# Provenance

```
Module updated: May 2026 with Anthropic's Claude Opus 4.7
(D3.1 sweep manifest, post-Mode 7 review)
```

Inventory and Mode 7 review by Opus 4.7 (separate sessions).
Decisions and editorial integration by Tony Quintanilla.
Manifest authoring by Opus 4.7 (this session).

Five batches. ~140 edit sites. 11 inventoried problems become 11
closed items. The conversation is the design process.

*Paloma's Orrery | palomasorrery.com*
*"Static analysis catches what visual testing cannot."*
*"When an automated tool flags a violation, verify the diagnosis,*
*not just the detection."*
