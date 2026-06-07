# Subcategory Support Handoff
## gallery_editor.py + index.html Changes
### March 8, 2026

---

## Overview

Add `subcategory` / `subcategory_label` fields to Earth System gallery
entries, with display support in gallery_editor.py tree and collapsible
rendering in index.html sidebar.

Three deliverables:
1. `assign_subcategories.py` -- one-time script to populate metadata (DONE)
2. `gallery_editor.py` -- targeted changes (4 edits)
3. `index.html` -- targeted changes (2 edits: CSS + JS)

---

## File 1: gallery_editor.py (4 targeted edits)

### Edit 1: Add "Set Subcategory" button to toolbar
**Location:** After line 217 (Toggle Featured button), before the Save separator

```python
        ttk.Separator(toolbar, orient='vertical').pack(
            side='left', fill='y', padx=8, pady=2)

        ttk.Button(toolbar, text="Set Subcategory",
                   command=self._set_subcategory).pack(side='left', padx=2)
```

### Edit 2: Show subcategory grouping in tree for climate category
**Location:** Inside `_refresh_tree()`, replace the viz insertion loop
(lines ~355-365) with subcategory-aware grouping.

Replace this block:
```python
                for viz in items:
                    size = viz.get('size_kb', 0)
                    star = "\u2605 " if viz.get('featured') else ""
                    self.tree.insert(
                        parent, 'end', iid=viz['id'],
                        text=viz.get('id', ''),
                        values=(
                            star + viz.get('title', ''),
                            viz.get('description', '')[:80],
                            f"{size:,.1f}"
                        ))
```

With this:
```python
                # Check if any items have subcategories
                has_subs = any(v.get('subcategory') for v in items)

                if has_subs:
                    # Group by subcategory within this category
                    sub_groups = {}
                    sub_order = []
                    for viz in items:
                        sub = viz.get('subcategory', '')
                        sub_label = viz.get('subcategory_label', sub or 'Ungrouped')
                        if sub not in sub_groups:
                            sub_groups[sub] = []
                            sub_order.append((sub, sub_label))
                        sub_groups[sub].append(viz)

                    for sub_key, sub_label in sub_order:
                        sub_items = sub_groups[sub_key]
                        sub_iid = f'sub_{mode_key}_{cat_key}_{sub_key}'
                        sub_parent = self.tree.insert(
                            parent, 'end', iid=sub_iid,
                            text=f"{sub_label} ({len(sub_items)})",
                            open=True)
                        for viz in sub_items:
                            size = viz.get('size_kb', 0)
                            star = "\u2605 " if viz.get('featured') else ""
                            self.tree.insert(
                                sub_parent, 'end', iid=viz['id'],
                                text=viz.get('id', ''),
                                values=(
                                    star + viz.get('title', ''),
                                    viz.get('description', '')[:80],
                                    f"{size:,.1f}"
                                ))
                else:
                    # No subcategories -- flat list as before
                    for viz in items:
                        size = viz.get('size_kb', 0)
                        star = "\u2605 " if viz.get('featured') else ""
                        self.tree.insert(
                            parent, 'end', iid=viz['id'],
                            text=viz.get('id', ''),
                            values=(
                                star + viz.get('title', ''),
                                viz.get('description', '')[:80],
                                f"{size:,.1f}"
                            ))
```

### Edit 3: Handle subcategory nodes in selection helper
**Location:** `_get_selected_type()` method (~line 390-401)

Replace:
```python
        if item_id.startswith('mode_'):
            return 'mode', item_id
        elif item_id.startswith('cat_'):
            return 'category', item_id
        else:
            return 'viz', item_id
```

With:
```python
        if item_id.startswith('mode_'):
            return 'mode', item_id
        elif item_id.startswith('cat_'):
            return 'category', item_id
        elif item_id.startswith('sub_'):
            return 'subcategory', item_id
        else:
            return 'viz', item_id
```

Also update `_get_selected_viz()` (~line 380) to handle subcategory nodes:
```python
        if item_id.startswith('mode_') or item_id.startswith('cat_') or item_id.startswith('sub_'):
```

### Edit 4: Add the _set_subcategory method
**Location:** After `_change_category()` method (~line 538)

```python
    def _set_subcategory(self):
        """Set or change the subcategory of the selected visualization."""
        viz = self._get_selected_viz()
        if not viz:
            return

        current_sub = viz.get('subcategory', '')
        current_sub_label = viz.get('subcategory_label', '')

        # Collect existing subcategories from all vizs for suggestions
        existing = {}
        for v in self.data.get('visualizations', []):
            s = v.get('subcategory', '')
            sl = v.get('subcategory_label', '')
            if s and s not in existing:
                existing[s] = sl

        # Build selection list
        sub_list = [('', '(none -- remove subcategory)')]
        for key in sorted(existing.keys()):
            sub_list.append((key, existing[key]))

        dlg = tk.Toplevel(self.root)
        dlg.title(f"Set Subcategory - {viz['id']}")
        dlg.geometry("400x350")
        dlg.transient(self.root)
        dlg.grab_set()

        cur_text = f"{current_sub_label} [{current_sub}]" if current_sub else "(none)"
        ttk.Label(dlg, text=f"Current: {cur_text}").pack(
            anchor='w', padx=12, pady=(12, 4))
        ttk.Label(dlg, text="Select existing or enter new:").pack(
            anchor='w', padx=12, pady=(0, 4))

        listbox = tk.Listbox(dlg, height=min(len(sub_list), 8))
        listbox.pack(fill='both', expand=True, padx=12, pady=4)

        for i, (key, label) in enumerate(sub_list):
            display = f"{label}  [{key}]" if key else label
            listbox.insert('end', display)
            if key == current_sub:
                listbox.selection_set(i)
                listbox.see(i)

        # New subcategory entry
        new_frame = ttk.LabelFrame(dlg, text="Or create new")
        new_frame.pack(fill='x', padx=12, pady=4)

        ttk.Label(new_frame, text="Key:").grid(row=0, column=0, padx=4, pady=2, sticky='w')
        key_entry = ttk.Entry(new_frame, width=20)
        key_entry.grid(row=0, column=1, padx=4, pady=2, sticky='ew')

        ttk.Label(new_frame, text="Label:").grid(row=1, column=0, padx=4, pady=2, sticky='w')
        label_entry = ttk.Entry(new_frame, width=20)
        label_entry.grid(row=1, column=1, padx=4, pady=2, sticky='ew')
        new_frame.columnconfigure(1, weight=1)

        def on_ok():
            # Check if new entry has content
            new_key = key_entry.get().strip()
            new_label = label_entry.get().strip()

            if new_key and new_label:
                viz['subcategory'] = new_key
                viz['subcategory_label'] = new_label
            else:
                sel = listbox.curselection()
                if sel:
                    chosen_key, chosen_label = sub_list[sel[0]]
                    if chosen_key:
                        viz['subcategory'] = chosen_key
                        viz['subcategory_label'] = chosen_label
                    else:
                        # Remove subcategory
                        viz.pop('subcategory', None)
                        viz.pop('subcategory_label', None)
                else:
                    dlg.destroy()
                    return

            self._mark_dirty()
            self._refresh_tree()
            self._select_item(viz['id'])
            sub_display = viz.get('subcategory_label', '(none)')
            self.status_var.set(
                f"Subcategory set: {viz['id']} -> {sub_display}")
            dlg.destroy()

        btn_frame = ttk.Frame(dlg)
        btn_frame.pack(fill='x', padx=12, pady=(0, 12))
        ttk.Button(btn_frame, text="OK", command=on_ok).pack(
            side='right', padx=2)
        ttk.Button(btn_frame, text="Cancel",
                   command=dlg.destroy).pack(side='right', padx=2)
        listbox.bind('<Double-1>', lambda e: on_ok())
        dlg.bind('<Escape>', lambda e: dlg.destroy())
```

---

## File 2: index.html (2 targeted edits)

### Edit 1: CSS for subcategory headers (collapsible)
**Location:** After `.category-label` styles (~line 382)

Add:
```css
        /* Subcategory headers (within Earth System) */
        .subcategory-header {
            padding: 10px 0 4px 8px;
            margin-bottom: 4px;
            cursor: pointer;
            user-select: none;
        }

        .subcategory-label {
            font-size: 0.63rem;
            font-weight: 500;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            color: var(--text-secondary);
            transition: color 0.2s ease;
        }

        .subcategory-header:hover .subcategory-label {
            color: var(--text-primary);
        }

        .subcategory-arrow {
            display: inline-block;
            width: 12px;
            font-size: 0.6rem;
            color: var(--text-dim);
            transition: transform 0.2s ease;
        }

        .subcategory-header.collapsed .subcategory-arrow {
            transform: rotate(-90deg);
        }

        .subcategory-items {
            overflow: hidden;
            transition: max-height 0.25s ease;
        }

        .subcategory-items.collapsed {
            max-height: 0 !important;
        }
```

### Edit 2: JS renderNavList with subcategory grouping
**Location:** Replace the card rendering loop inside renderNavList
(lines ~1334-1349)

Replace this block:
```javascript
                // Cards
                for (var j = 0; j < catData.items.length; j++) {
                    var item = catData.items[j];
                    html += '<div class="viz-card" data-viz-id="' + escapeHtml(item.id) + '">';
                    html += '<div class="viz-card-title">' + escapeHtml(item.title || 'Untitled') + '</div>';
                    if (item.description) {
                        html += '<div class="viz-card-desc">' + escapeHtml(item.description) + '</div>';
                    }
                    if (item.size_kb) {
                        html += '<div class="viz-card-size">' + Math.round(item.size_kb) + ' KB</div>';
                    }
                    if (item.featured) {
                        html += '<div class="viz-card-featured">Featured</div>';
                    }
                    html += '</div>';
                }
```

With this:
```javascript
                // Check if items have subcategories
                var hasSubs = false;
                for (var j = 0; j < catData.items.length; j++) {
                    if (catData.items[j].subcategory) { hasSubs = true; break; }
                }

                if (hasSubs) {
                    // Group by subcategory, preserving order
                    var subGroups = {};
                    var subOrder = [];
                    for (var j = 0; j < catData.items.length; j++) {
                        var item = catData.items[j];
                        var sub = item.subcategory || '_ungrouped';
                        var subLabel = item.subcategory_label || 'Other';
                        if (!subGroups[sub]) {
                            subGroups[sub] = { label: subLabel, items: [] };
                            subOrder.push(sub);
                        }
                        subGroups[sub].items.push(item);
                    }

                    for (var s = 0; s < subOrder.length; s++) {
                        var subKey = subOrder[s];
                        var subData = subGroups[subKey];
                        var subId = 'sub_' + catKey + '_' + subKey;

                        // Subcategory header (collapsible)
                        html += '<div class="subcategory-header" data-sub-id="' + subId + '">';
                        html += '<span class="subcategory-arrow">&#9660;</span> ';
                        html += '<span class="subcategory-label" style="color: ' + color + '99;">';
                        html += escapeHtml(subData.label);
                        html += ' (' + subData.items.length + ')';
                        html += '</span></div>';

                        // Subcategory items container
                        html += '<div class="subcategory-items" id="' + subId + '">';
                        for (var k = 0; k < subData.items.length; k++) {
                            var item = subData.items[k];
                            html += renderVizCard(item);
                        }
                        html += '</div>';
                    }
                } else {
                    // No subcategories -- flat list as before
                    for (var j = 0; j < catData.items.length; j++) {
                        var item = catData.items[j];
                        html += renderVizCard(item);
                    }
                }
```

Also add a helper function BEFORE renderNavList:
```javascript
        // ---- Render a single viz card ----
        function renderVizCard(item) {
            var h = '';
            h += '<div class="viz-card" data-viz-id="' + escapeHtml(item.id) + '">';
            h += '<div class="viz-card-title">' + escapeHtml(item.title || 'Untitled') + '</div>';
            if (item.description) {
                h += '<div class="viz-card-desc">' + escapeHtml(item.description) + '</div>';
            }
            if (item.size_kb) {
                h += '<div class="viz-card-size">' + Math.round(item.size_kb) + ' KB</div>';
            }
            if (item.featured) {
                h += '<div class="viz-card-featured">Featured</div>';
            }
            h += '</div>';
            return h;
        }
```

And add a click handler for collapsible subcategory headers.
**Location:** In the event delegation section where viz-card clicks are handled
(near line ~1878)

Add BEFORE the viz-card click handler:
```javascript
                // Subcategory collapse/expand
                var subHeader = e.target.closest('.subcategory-header');
                if (subHeader) {
                    var subId = subHeader.getAttribute('data-sub-id');
                    var subItems = document.getElementById(subId);
                    if (subItems) {
                        subHeader.classList.toggle('collapsed');
                        subItems.classList.toggle('collapsed');
                    }
                    return;
                }
```

---

## Metadata Schema Addition

Each Earth System visualization entry gains two optional fields:

```json
{
    "id": "keeling_curve_co2_concentration",
    "title": "Keeling Curve: CO2 Concentration, 1958 - 2025",
    "category": "climate",
    "category_label": "Earth System",
    "subcategory": "climate_change",
    "subcategory_label": "Climate Change",
    ...
}
```

Non-climate entries have no subcategory fields. The rendering
code checks `hasSubs` and falls back to flat display if none exist.
This means no other category is affected.

---

## Subcategory Keys (initial set, will grow)

| Key | Label | Boundary |
|-----|-------|----------|
| overview | Overview | (hub) |
| climate_change | Climate Change | CO2 + RF |
| heat_events | Extreme Heating Events | (cross-boundary) |
| ocean_acidification | Ocean Acidification | Ocean acidification |
| biochemical_flows | Biochemical Flows | N + P cycles |
| biosphere_integrity | Biosphere Integrity | Genetic + functional |
| land_system_change | Land-System Change | Deforestation |
| freshwater_change | Freshwater Change | Green + blue water |
| aerosol_loading | Atmospheric Aerosol Loading | AOD |
| ozone_depletion | Stratospheric Ozone Depletion | O3 |
| novel_entities | Novel Entities | Chemical pollution |

Only the first four are populated initially. Others are ready
for future content -- just assign the subcategory in gallery_editor.

---

## Build Order

1. Run `assign_subcategories.py` on gallery_metadata.json
2. Apply gallery_editor.py edits (4 changes, bottom-up)
3. Apply index.html edits (CSS + JS, 3 changes)
4. Test: gallery_editor shows subcategory tree for Earth System
5. Test: index.html renders collapsible subcategories on mobile
6. Verify: non-climate categories render unchanged

## What Doesn't Change

- gallery_config.json (subcategories live in metadata, not config)
- json_converter.py (subcategory assigned via editor, not converter)
- gallery_studio.py (no subcategory awareness needed)
- Any non-climate gallery entries
- The _studio flag system
- The JSON pipeline
