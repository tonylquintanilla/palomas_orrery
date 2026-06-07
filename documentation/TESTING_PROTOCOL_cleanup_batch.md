# Cleanup Batch Testing Protocol (Items 14, 15, 27, 31, 32, 33)

**Tester:** Tony Quintanilla
**Date:** May 19, 2026
**Files to deploy:** 3 files + 2-line snippet in palomas_orrery.py

---

## 0. Deploy

1. Copy `shell_configs.py`, `solar_visualization_shells.py`,
   `neptune_visualization_shells.py` to sandbox.
2. Apply the 2-line snippet to `palomas_orrery.py` (import + CreateToolTip).
3. Launch dashboard. Confirm no errors.

---

## 1. Item 31: Solar System Structures tooltip

- [ ] Hover over the "Solar System Structures" checkbox label
- [ ] Tooltip should now render as plain text with line breaks
      (not `<b>The Sun...</b><br><br>` literal tags)

**This is the most visible fix. If the tags still show, the snippet
wasn't applied.**

---

## 2. Item 27: Saturn/Uranus/Neptune hover text

Pick ONE body (Saturn recommended — most shells):

- [ ] Sun-centered view, enable Saturn Core shell
- [ ] Hover over the info marker — text should display with proper
      line breaks in the Plotly popup (not truncated/collapsed)
- [ ] Compare to pre-fix: the `\n` characters were rendering as
      collapsed whitespace; now `<br>` produces visible line breaks

**One body is sufficient — the fix is identical across all 16 entries.**

---

## 3. Item 32: Sun custom info markers

Sun-centered view:

- [ ] Enable Hills Cloud Torus — info marker cross should have
      red border (was gray/white, thin)
- [ ] Enable Outer Oort Clumpy — same red border check
- [ ] Enable Galactic Tide — same red border check
- [ ] Markers should match the style of planet info markers
      (e.g. Jupiter's magnetosphere cross marker)

---

## 4. Items 14+15: Neptune (regression only)

- [ ] Neptune-centered view, enable Magnetosphere
- [ ] Magnetosphere renders, no console errors
- [ ] No `"Returning X magnetic field traces"` print in console

**The import restructuring is invisible if it works. Console silence
is the test.**

---

## 5. Item 33: Sun photosphere mesh3d (DORMANT — no visual change)

Skip. This config is registered but not invoked until switchover.
Visual verification happens at switchover (item 29).

---

## After testing

If all checks pass:
1. Copy to clean repo
2. Run provenance scanner
3. Deploy to GitHub

If the tooltip (item 31) still shows tags, check that both the
import line AND the CreateToolTip line were updated.
