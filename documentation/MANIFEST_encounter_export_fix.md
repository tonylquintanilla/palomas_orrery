# Encounter Export Fix — Change Manifest
**May 7, 2026 | Tony Quintanilla with Anthropic's Claude Opus 4.6**

## Overview

Six bugs, four files, applied bottom-up within each file.
All edits are targeted snippets against the uploaded file versions.

## File: apsidal_markers.py

### Edit 2b — Deconflict closest plotted point label (line 1484)
**Current:**
```python
    label = f"Closest Plotted Point"
```
**New:**
```python
    if trace_qualifier:
        label = f"Closest {trace_qualifier} Point"
    else:
        label = f"Closest Plotted Point"
```

### Edit 2a — Add trace_qualifier parameter (line 1411)
**Current:**
```python
def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None, marker_color=None, obj_info=None):
```
**New:**
```python
def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None, marker_color=None, obj_info=None, trace_qualifier=None):
```

---

## File: spacecraft_encounters.py

### Edit 6a — Psyche full mission dates (lines 404-405)
**Current:**
```python
        'start_date': '',  # TODO: fill in
        'end_date': '',  # TODO: fill in
```
**New:**
```python
        'start_date': '2023-10-14',
        'end_date': '2029-06-26',
```

### Edit 4d — Defensive date parser (add above _snap_to_horizons_step, ~line 497)
**Add new function:**
```python
def _parse_encounter_date(date_str):
    """Parse encounter date string, accepting multiple formats.

    Handles zero-padded and unpadded dates, with or without seconds.
    Returns datetime or None on failure.
    """
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M',
                '%Y-%m-%d %H:%M:%S UTC', '%Y-%m-%d'):
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None
```

### Edit 4d-ii — Use defensive parser in _calculate_encounter_resolution (line 553)
**Current:**
```python
        try:
            enc_date = datetime.strptime(enc['date'], '%Y-%m-%d %H:%M:%S')
        except (ValueError, KeyError):
            return None
```
**New:**
```python
        enc_date = _parse_encounter_date(enc.get('date', ''))
        if enc_date is None:
            return None
```

### Edit 4d-iii — Use defensive parser in get_encounter_preset fallback (line 756)
**Current:**
```python
        try:
            enc_date = datetime.strptime(enc['date'], '%Y-%m-%d %H:%M:%S')
            half_days = plot_days // 2
            start_dt = enc_date - timedelta(days=half_days)
            end_dt = enc_date + timedelta(days=plot_days - half_days)
            start_date = start_dt.strftime('%Y-%m-%d %H:%M:%S')
            end_date = end_dt.strftime('%Y-%m-%d %H:%M:%S')
        except (ValueError, KeyError):
            start_date = None
            end_date = None
```
**New:**
```python
        enc_date = _parse_encounter_date(enc.get('date', ''))
        if enc_date:
            half_days = plot_days // 2
            start_dt = enc_date - timedelta(days=half_days)
            end_dt = enc_date + timedelta(days=plot_days - half_days)
            start_date = start_dt.strftime('%Y-%m-%d %H:%M:%S')
            end_date = end_dt.strftime('%Y-%m-%d %H:%M:%S')
        else:
            start_date = None
            end_date = None
```

---

## File: palomas_orrery.py

### Edit 2d — Full Mission caller passes qualifier (~line 6328)
Add `trace_qualifier='Full Mission'` to the add_closest_approach_marker call.
**Add to call arguments:**
```python
                                add_closest_approach_marker(
                                    ...,
                                    trace_qualifier='Full Mission',
                                )
```

### Edit 2c — Plotted Period caller passes qualifier (~line 4761)
Add `trace_qualifier='Plotted Period'` to the add_closest_approach_marker call.
**Add to call arguments:**
```python
                                add_closest_approach_marker(
                                    ...,
                                    trace_qualifier='Plotted Period',
                                )
```

---

## File: gallery_studio.py

### Edit 4c — Normalize date in generated code (line 5224)
**Current:**
```python
            date = manual.get('date', '')
            lines.append(f"    'date': '{date}',")
```
**New:**
```python
            date = manual.get('date', '')
            # Normalize to YYYY-MM-DD HH:MM:SS
            normalized_date = None
            for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M',
                        '%Y-%m-%d', '%Y-%m-%d %H:%M:%S UTC'):
                try:
                    dt = datetime.strptime(date.strip(), fmt)
                    normalized_date = dt.strftime('%Y-%m-%d %H:%M:%S')
                    break
                except ValueError:
                    continue
            if normalized_date:
                lines.append(f"    'date': '{normalized_date}',")
            else:
                lines.append(f"    'date': '{date}',  # WARNING: could not normalize format")
```

### Edit 6b — Pull full mission dates from celestial_objects.py (lines 5196-5201)
In the `is_full_mission` branch of `_generate_encounter_code`, replace the
empty-string fallback with a lookup from celestial_objects.py.
**Current:**
```python
            date_range = extracted.get('date_range', '')
            if date_range and ' to ' in date_range:
                start, end = date_range.split(' to ', 1)
                lines.append(f"    'start_date': '{start.strip()}',")
                lines.append(f"    'end_date': '{end.strip()}',")
            else:
                lines.append(f"    'start_date': '',  # TODO: fill in")
                lines.append(f"    'end_date': '',  # TODO: fill in")
```
**New:**
```python
            date_range = extracted.get('date_range', '')
            if date_range and ' to ' in date_range:
                start, end = date_range.split(' to ', 1)
                lines.append(f"    'start_date': '{start.strip()}',")
                lines.append(f"    'end_date': '{end.strip()}',")
            else:
                # Pull from celestial_objects.py mission dates
                mission_start = extracted.get('mission_start_date', '')
                mission_end = extracted.get('mission_end_date', '')
                if mission_start:
                    lines.append(f"    'start_date': '{mission_start}',")
                else:
                    lines.append(f"    'start_date': '',  # TODO: fill in")
                if mission_end:
                    lines.append(f"    'end_date': '{mission_end}',")
                else:
                    lines.append(f"    'end_date': '',  # TODO: fill in")
```

### Edit 6b-ii — Extract mission dates in _extract_encounter_data
Add after the spacecraft detection block (~line 5054), before select_also:
```python
        # ---- Mission dates: from celestial_objects.py ----
        if result.get('spacecraft'):
            try:
                from celestial_objects import objects
                for obj in objects:
                    if obj.get('name') == result['spacecraft']:
                        sd = obj.get('start_date')
                        ed = obj.get('end_date')
                        if sd:
                            # Use first full day (start_date is already day-after-launch)
                            result['mission_start_date'] = sd.strftime('%Y-%m-%d')
                        if ed:
                            result['mission_end_date'] = ed.strftime('%Y-%m-%d')
                        break
            except ImportError:
                pass  # celestial_objects not available in this context
```

### Edit 1c-ii — Manual center reads into generation (in Generate button handler)
Where the manual dict is assembled, add:
```python
        'center': var_center.get(),
```

### Edit 1c — Manual center entry field in dialog (after target field, ~line 5925)
**Add:**
```python
        # Center body (pre-filled from hover detection, editable)
        tk.Label(manual_frame, text="Center:", anchor='w',
                 width=12).grid(row=r, column=0, sticky='w', pady=2)
        var_center = tk.StringVar(
            value=extracted.get('center', ''))
        tk.Entry(manual_frame, textvariable=var_center,
                 width=24).grid(row=r, column=1, sticky='w', pady=2)
        r += 1
```

### Edit 1b-ii — Use manual center in generation (line 5276)
**Current:**
```python
            center = extracted.get('center', 'Sun')
```
**New:**
```python
            center = manual.get('center') or extracted.get('center', 'Sun')
```

### Edit 1b — Replace title parsing with hover detection (lines 5085-5100)
**Current:**
```python
        # ---- Center: parse from title ----
        title = layout.get('title', {})
        if isinstance(title, dict):
            title_text = title.get('text', '')
        else:
            title_text = str(title)
        # Common patterns: "around X", "centered on X", "X system"
        center_match = re.search(
            r'(?:around|centered on|center[: ]+)\s*(\w+)',
            title_text, re.IGNORECASE)
        if center_match:
            result['center'] = center_match.group(1)
        else:
            # Fallback: if "Sun" in select_also, center is Sun
            if 'Sun' in deduped:
                result['center'] = 'Sun'
```
**New:**
```python
        # ---- Center: detected from closest plotted point hover text ----
        # Set after the closest-point loop below. If hover detection
        # fails, the dialog provides a manual entry field.
```

### Edit 4b — Pre-fill date field in dialog (line 5938)
**Current:**
```python
        var_date = tk.StringVar()
```
**New:**
```python
        var_date = tk.StringVar(
            value=extracted.get('date_suggestion', ''))
```

### Edits 1a + 2 + 3 + 4a — Replace closest plotted point extraction block (lines 5133-5155)
**Current:**
```python
        # ---- dist_km / v_kms: from closest plotted point trace ----
        for trace in traces:
            tname = trace.get('name', '')
            if 'closest' in tname.lower() and 'point' in tname.lower():
                text_list = trace.get('text', [])
                if isinstance(text_list, str):
                    text_list = [text_list]
                for txt in text_list:
                    if not txt:
                        continue
                    txt_str = str(txt)
                    # Distance pattern: "12,345 km" or "12345.6 km"
                    dist_match = re.search(
                        r'([\d,]+\.?\d*)\s*km', txt_str)
                    if dist_match and 'dist_km_suggestion' not in result:
                        val = dist_match.group(1).replace(',', '')
                        result['dist_km_suggestion'] = val
                    # Velocity pattern: "13.78 km/s"
                    vel_match = re.search(
                        r'([\d.]+)\s*km/s', txt_str)
                    if vel_match and 'v_kms_suggestion' not in result:
                        result['v_kms_suggestion'] = vel_match.group(1)
                break
```
**New:**
```python
        # ---- Closest plotted point: date, distance, center body ----
        # Prefer "Closest Plotted Period Point" (encounter distance)
        # over "Closest Full Mission Point" (full-trajectory distance).
        # Fall back to "Closest Plotted Point" for older HTML files
        # or non-spacecraft objects.
        spacecraft_name = result.get('spacecraft', '')
        cpp_trace = None

        # Priority 1: Plotted Period point (encounter)
        for trace in traces:
            tname = trace.get('name', '')
            if tname == f"{spacecraft_name} Closest Plotted Period Point":
                cpp_trace = trace
                break

        # Priority 2: generic Closest Plotted Point (backward compat)
        if cpp_trace is None:
            for trace in traces:
                tname = trace.get('name', '')
                if tname == f"{spacecraft_name} Closest Plotted Point":
                    cpp_trace = trace
                    break

        # Extract data from chosen closest plotted point
        if cpp_trace is not None:
            text_list = cpp_trace.get('text', [])
            if isinstance(text_list, str):
                text_list = [text_list]
            for txt in text_list:
                if not txt:
                    continue
                txt_str = str(txt)
                # Date pattern: "Date: 2026-05-15 19:51:00 UTC"
                date_match = re.search(
                    r'Date:\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s*UTC',
                    txt_str)
                if date_match and 'date_suggestion' not in result:
                    result['date_suggestion'] = date_match.group(1)
                # Distance from center (km)
                dist_match = re.search(
                    r'Distance from center:\s*([\d,]+\.?\d*)\s*km',
                    txt_str)
                if dist_match and 'dist_km_suggestion' not in result:
                    result['dist_km_suggestion'] = dist_match.group(1).replace(',', '')
                # Distance from surface (km)
                surf_match = re.search(
                    r'Distance from surface:\s*([\d,]+\.?\d*)\s*km',
                    txt_str)
                if surf_match and 'dist_surface_km' not in result:
                    result['dist_surface_km'] = surf_match.group(1).replace(',', '')
                # Center body: "Phobos radius: 11 km"
                center_match = re.search(
                    r'(\w[\w\s-]*?)\s+radius:\s*[\d,]+',
                    txt_str)
                if center_match and 'center_from_hover' not in result:
                    result['center_from_hover'] = center_match.group(1).strip()
                # Velocity pattern: "13.78 km/s"
                vel_match = re.search(
                    r'([\d.]+)\s*km/s', txt_str)
                if vel_match and 'v_kms_suggestion' not in result:
                    result['v_kms_suggestion'] = vel_match.group(1)

        # ---- Center: from hover text detection ----
        if 'center_from_hover' in result:
            result['center'] = result['center_from_hover']
```

---

## Application Order

Apply bottom-up within each file to prevent line number shifts.
The manifest above is already ordered bottom-up within each file.

**File order** (by independence — least dependencies first):
1. apsidal_markers.py (2 edits — function signature + label)
2. spacecraft_encounters.py (4 edits — dates + parser)
3. palomas_orrery.py (2 edits — pass qualifier to callers)
4. gallery_studio.py (8 edits — extraction + dialog + generation)

## Summary

| Bug | Description | Edits | Files |
|-----|-------------|-------|-------|
| 4   | Date format | 4a, 4b, 4c, 4d | gallery_studio.py, spacecraft_encounters.py |
| 1   | Center detection | 1a, 1b, 1c | gallery_studio.py |
| 2   | Wrong closest point | 2a, 2b, 2c, 2d | apsidal_markers.py, palomas_orrery.py, gallery_studio.py |
| 3   | Surface distance | (absorbed into 1a+2 block) | gallery_studio.py |
| 6   | Psyche dates | 6a, 6b | spacecraft_encounters.py, gallery_studio.py |
| 5   | Animation loss | Deferred | — |

Total: 16 targeted edits across 4 files.
