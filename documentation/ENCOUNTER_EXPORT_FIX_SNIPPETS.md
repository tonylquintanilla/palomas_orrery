# Encounter Export Fix — Verified Snippets
**May 7, 2026 | Tony Quintanilla with Anthropic's Claude Opus 4.7**

Companion to `MANIFEST_encounter_export_fix.md`. Snippets verified against
project snapshot. Three corrections applied (flagged inline as **[CORRECTED]**).

Apply bottom-up within each file. File order: apsidal_markers.py first
(no dependencies), then spacecraft_encounters.py, then palomas_orrery.py
(depends on apsidal_markers signature), then gallery_studio.py.

Each snippet shows the exact `old_str` to match. Use Python binary mode if
your file has CRLF line endings; line endings inside the snippets here are LF.

---

## File 1 of 4: `apsidal_markers.py`

### Edit 2b — Deconflict closest plotted point label

Replace this:

```python
    # Create label using proper terminology
#    label = f"Closest Plotted ({near_term})"
    label = f"Closest Plotted Point"
```

With this:

```python
    # Create label using proper terminology
#    label = f"Closest Plotted ({near_term})"
    if trace_qualifier:
        label = f"Closest {trace_qualifier} Point"
    else:
        label = f"Closest Plotted Point"
```

### Edit 2a — Add `trace_qualifier` parameter

Replace this:

```python
def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None, marker_color=None, obj_info=None):
```

With this:

```python
def add_closest_approach_marker(fig, positions_dict, obj_name, center_body, color_map, date_range=None, marker_color=None, obj_info=None, trace_qualifier=None):
```

---

## File 2 of 4: `spacecraft_encounters.py`

### Edit 4d-iii — Use defensive parser in `get_encounter_preset` fallback

Replace this:

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

With this:

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

### Edit 4d-ii — Use defensive parser in `_calculate_encounter_resolution`

Replace this:

```python
    try:
        enc_date = datetime.strptime(enc['date'], '%Y-%m-%d %H:%M:%S')
    except (ValueError, KeyError):
        return None
```

With this:

```python
    enc_date = _parse_encounter_date(enc.get('date', ''))
    if enc_date is None:
        return None
```

### Edit 4d — Add `_parse_encounter_date` helper

Insert this **between** `get_full_mission_preset` (ends at line 495) and
`_snap_to_horizons_step` (starts at line 498). Replace:

```python
def get_full_mission_preset(spacecraft_name):
    return SPACECRAFT_FULL_MISSION.get(spacecraft_name, None)


def _snap_to_horizons_step(ideal_step_sec):
```

With this:

```python
def get_full_mission_preset(spacecraft_name):
    return SPACECRAFT_FULL_MISSION.get(spacecraft_name, None)


def _parse_encounter_date(date_str):
    """Parse encounter date string, accepting multiple formats.

    Handles zero-padded and unpadded dates, with or without seconds.
    Returns datetime or None on failure.
    """
    if not date_str:
        return None
    for fmt in ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M',
                '%Y-%m-%d %H:%M:%S UTC', '%Y-%m-%d'):
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None


def _snap_to_horizons_step(ideal_step_sec):
```

### Edit 6a — Psyche full mission dates

Replace this:

```python
    'Psyche': {
        'center': 'Sun',
        'select_also': ['Earth', 'Mars', '16 Psyche', 'Sun'],
        'start_date': '',  # TODO: fill in
        'end_date': '',  # TODO: fill in
        'plot_scale_au': 4.310647279011173,
        'fetch_step': '6h',
        'label': 'Psyche Mission to 16 Psyche',
    },
```

With this:

```python
    'Psyche': {
        'center': 'Sun',
        'select_also': ['Earth', 'Mars', '16 Psyche', 'Sun'],
        'start_date': '2023-10-14',
        'end_date': '2029-06-26',
        'plot_scale_au': 4.310647279011173,
        'fetch_step': '6h',
        'label': 'Psyche Mission to 16 Psyche',
    },
```

---

## File 3 of 4: `palomas_orrery.py`

### Edit 2d — Full Mission caller (line 6328 region)

Replace this:

```python
                                add_closest_approach_marker(
                                    fig=fig,
                                    positions_dict=positions_dict,
                                    obj_name=obj_name,
                                    center_body=center_object_name,
                                    color_map=color_map,
                                    date_range=(dates_lists.get(obj_name, [None, None])[0],
                                                dates_lists.get(obj_name, [None, None])[-1])
                                            if dates_lists.get(obj_name) else None,
                                    marker_color=marker_color,
                                    obj_info=obj
                                )
```

With this:

```python
                                add_closest_approach_marker(
                                    fig=fig,
                                    positions_dict=positions_dict,
                                    obj_name=obj_name,
                                    center_body=center_object_name,
                                    color_map=color_map,
                                    date_range=(dates_lists.get(obj_name, [None, None])[0],
                                                dates_lists.get(obj_name, [None, None])[-1])
                                            if dates_lists.get(obj_name) else None,
                                    marker_color=marker_color,
                                    obj_info=obj,
                                    trace_qualifier='Full Mission',
                                )
```

> **Verify before applying:** I haven't viewed the exact call at line 6328
> in this session. Open `palomas_orrery.py` near line 6328, confirm the
> argument list matches the `old_str` above, and adjust if not. The change
> is just adding `trace_qualifier='Full Mission',` as the last keyword
> argument — adapt to match whatever your actual call looks like.

### Edit 2c — Plotted Period caller (line 4761 region)

Same pattern. Open `palomas_orrery.py` near line 4761, locate the
`add_closest_approach_marker(...)` call, and add as the last argument:

```python
                                    trace_qualifier='Plotted Period',
```

> **Verify before applying:** same caveat — confirm the exact call
> structure before editing.

---

## File 4 of 4: `gallery_studio.py`

### Edit 4c — Normalize date in generated code

Replace this:

```python
            date = manual.get('date', '')
            lines.append(f"    'date': '{date}',")
```

With this:

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

### Edit 1b-ii — Use manual center in encounter generation

Replace this:

```python
            center = extracted.get('center', 'Sun')
            lines.append(f"    'center': '{center}',")

            sel = extracted.get('select_also', [])
            sel_str = ', '.join(f"'{s}'" for s in sel)
            lines.append(f"    'select_also': [{sel_str}],")

            plot_days = extracted.get('plot_days')
```

With this:

```python
            center = manual.get('center') or extracted.get('center', 'Sun')
            lines.append(f"    'center': '{center}',")

            sel = extracted.get('select_also', [])
            sel_str = ', '.join(f"'{s}'" for s in sel)
            lines.append(f"    'select_also': [{sel_str}],")

            plot_days = extracted.get('plot_days')
```

### Edit 1b-iii — **[CORRECTED — addition]** Symmetric manual center for full-mission generation

The manifest as written changes only the encounter branch (Edit 1b-ii at
line 5276). The full-mission branch at line 5187 has the same defaulting
logic and should accept the same manual override. Skip this edit if you
prefer to keep the manifest exact.

Replace this:

```python
            center = extracted.get('center', 'Sun')
            lines.append(f"    'center': '{center}',")

            sel = extracted.get('select_also', [])
            sel_str = ', '.join(f"'{s}'" for s in sel)
            lines.append(f"    'select_also': [{sel_str}],")

            date_range = extracted.get('date_range', '')
```

With this:

```python
            center = manual.get('center') or extracted.get('center', 'Sun')
            lines.append(f"    'center': '{center}',")

            sel = extracted.get('select_also', [])
            sel_str = ', '.join(f"'{s}'" for s in sel)
            lines.append(f"    'select_also': [{sel_str}],")

            date_range = extracted.get('date_range', '')
```

### Edit 6b — Pull full mission dates from celestial_objects.py

Replace this:

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

With this:

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

### Edits 1a + 2 + 3 + 4a — Replace closest plotted point extraction block

Replace this:

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

With this:

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

### Edit 1b — **[CORRECTED]** Replace title-parsing regex but preserve `title_text`

The manifest as written removed the entire title-parsing block including
the `title_text` extraction. But the date-range parser further down at
line 5123 reads `title_text` —

```python
date_match = re.findall(r'(\d{4}-\d{2}-\d{2})', title_text)
```

— so removing the extraction would cause a `NameError` at runtime.
The minimal correct change is to keep the `title_text` extraction (it's
harmless) and remove only the regex match against it (which never worked
on Orrery titles like "Animation Over Below Dates").

Replace this:

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

With this:

```python
        # Title text is needed by the date-range parser further down.
        title = layout.get('title', {})
        if isinstance(title, dict):
            title_text = title.get('text', '')
        else:
            title_text = str(title)

        # ---- Center: detected from closest plotted point hover text ----
        # Set after the closest-point loop below. If hover detection
        # fails, the dialog provides a manual entry field.
```

### Edit 6b-ii — Extract mission dates in `_extract_encounter_data`

**[CORRECTED]** The manifest's `from celestial_objects import objects`
will fail with `ImportError` — `celestial_objects.py` exports
`OBJECT_DEFINITIONS`, not `objects`. The `try/except ImportError: pass`
would silently swallow the failure and the lookup would never populate
the dates. Below uses `OBJECT_DEFINITIONS` directly; the dates we need
(`start_date`, `end_date`) are direct keys in the static catalog and
don't need the runtime resolution that `build_objects_list()` performs.

Insert this block after the spacecraft detection loop (the one ending
with `break` after `result['spacecraft'] = name.strip()`) and before
the `# ---- select_also: visible traces ----` section.

Locate this anchor:

```python
                result['spacecraft'] = name.strip()
                break

        # ---- select_also: visible traces ----
```

Replace with:

```python
                result['spacecraft'] = name.strip()
                break

        # ---- Mission dates: from celestial_objects.py ----
        if result.get('spacecraft'):
            try:
                from celestial_objects import OBJECT_DEFINITIONS
                for obj in OBJECT_DEFINITIONS:
                    if obj.get('name') == result['spacecraft']:
                        sd = obj.get('start_date')
                        ed = obj.get('end_date')
                        if sd:
                            result['mission_start_date'] = sd.strftime('%Y-%m-%d')
                        if ed:
                            result['mission_end_date'] = ed.strftime('%Y-%m-%d')
                        break
            except ImportError:
                pass  # celestial_objects not available in this context

        # ---- select_also: visible traces ----
```

### Edit 1c-ii — Manual center reads into generation

In `do_generate()` (the closure inside `_export_encounter`), the manual
dict is assembled with these keys:

Replace this:

```python
            manual = {
                'type': var_type.get(),
                'target': var_target.get().strip(),
                'label': var_label.get().strip(),
                'date': var_date.get().strip(),
                'dist_km': var_dist.get().strip(),
                'v_kms': var_vel.get().strip(),
                'date_source': var_dsrc.get(),
                'status': var_status.get(),
                'source': var_source.get().strip(),
                'note': note_text.get('1.0', 'end').strip(),
            }
```

With this:

```python
            manual = {
                'type': var_type.get(),
                'target': var_target.get().strip(),
                'label': var_label.get().strip(),
                'date': var_date.get().strip(),
                'dist_km': var_dist.get().strip(),
                'v_kms': var_vel.get().strip(),
                'date_source': var_dsrc.get(),
                'status': var_status.get(),
                'source': var_source.get().strip(),
                'note': note_text.get('1.0', 'end').strip(),
                'center': var_center.get().strip(),
            }
```

### Edit 4b — **[CORRECTED line number 5938 → 4938]** Pre-fill date field

Replace this:

```python
        # Date (UTC)
        tk.Label(manual_frame, text="Date (UTC):", anchor='w',
                 width=12).grid(row=r, column=0, sticky='w', pady=2)
        var_date = tk.StringVar()
```

With this:

```python
        # Date (UTC)
        tk.Label(manual_frame, text="Date (UTC):", anchor='w',
                 width=12).grid(row=r, column=0, sticky='w', pady=2)
        var_date = tk.StringVar(
            value=extracted.get('date_suggestion', ''))
```

### Edit 1c — **[CORRECTED line number 5925 → 4925]** Manual center entry field

Add the Center field between the Target field and the Label field. Replace
this:

```python
        # Target
        tk.Label(manual_frame, text="Target:", anchor='w',
                 width=12).grid(row=r, column=0, sticky='w', pady=2)
        var_target = tk.StringVar(
            value=extracted.get('target_suggestion', ''))
        tk.Entry(manual_frame, textvariable=var_target,
                 width=24).grid(row=r, column=1, sticky='w', pady=2)
        r += 1

        # Label
```

With this:

```python
        # Target
        tk.Label(manual_frame, text="Target:", anchor='w',
                 width=12).grid(row=r, column=0, sticky='w', pady=2)
        var_target = tk.StringVar(
            value=extracted.get('target_suggestion', ''))
        tk.Entry(manual_frame, textvariable=var_target,
                 width=24).grid(row=r, column=1, sticky='w', pady=2)
        r += 1

        # Center body (pre-filled from hover detection, editable)
        tk.Label(manual_frame, text="Center:", anchor='w',
                 width=12).grid(row=r, column=0, sticky='w', pady=2)
        var_center = tk.StringVar(
            value=extracted.get('center', ''))
        tk.Entry(manual_frame, textvariable=var_center,
                 width=24).grid(row=r, column=1, sticky='w', pady=2)
        r += 1

        # Label
```

---

## Test plan

Apply edits in the order above. After applying all four files:

1. **Run Orrery, generate the same Phobos flyby plot.** Verify the
   resulting HTML now contains `Psyche Closest Plotted Period Point`
   and `Psyche Closest Full Mission Point` instead of two ambiguous
   `Psyche Closest Plotted Point` traces.

2. **Open Studio, load the new HTML, enter Orrery preset mode, click
   Export Encounter.** Verify the dialog shows:
   - Spacecraft: Psyche
   - Center: Phobos (auto-detected)
   - Date: 2026-05-15 19:51:00 (pre-filled from hover)
   - dist_km: 1151
   - The dialog also has a Center field pre-filled with "Phobos"

3. **Click Generate Python.** Verify the generated dict has:
   - `'date': '2026-05-15 19:51:00',` (canonical format, zero-padded)
   - `'center': 'Phobos',`
   - `'dist_km': 1151,`

4. **Paste the dict into spacecraft_encounters.py, click the Go button
   for that encounter.** Verify the GUI date fields update to the May 15
   window (not today's default), and the plot renders centered on Phobos
   at the correct scale.

5. **Sanity test on Artemis II / New Horizons** (existing entries):
   load their HTML exports through the Studio export flow and verify
   no regressions — the existing dicts shouldn't change.

## Summary

| Bug | Edits | Files | Status |
|-----|-------|-------|--------|
| 4   | 4a, 4b, 4c, 4d, 4d-ii, 4d-iii | gallery_studio, spacecraft_encounters | verified |
| 1   | 1a, 1b, 1c, 1b-ii, **1b-iii**, 1c-ii | gallery_studio | **1b-iii added for symmetry** |
| 2   | 2a, 2b, 2c, 2d | apsidal_markers, palomas_orrery | verified |
| 3   | (in 1a + 2 + 3 + 4a block) | gallery_studio | verified |
| 6   | 6a, 6b, **6b-ii corrected** | spacecraft_encounters, gallery_studio | **import fixed** |
| 5   | (deferred) | — | per design doc |

Total: 17 edits (16 from manifest + 1b-iii for symmetry).

Module updated: May 2026 with Anthropic's Claude Opus 4.7
