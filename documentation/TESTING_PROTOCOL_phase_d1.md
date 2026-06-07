# Phase D1 Testing Protocol

**Tester:** Tony Quintanilla
**Date:** May 19, 2026
**Files to deploy:** 2 files from this session's output

---

## 0. Deploy and Smoke

1. Copy both files into your sandbox (not clean repo yet).
2. Launch `palomas_orrery_dashboard.py`.
3. Confirm the GUI opens without errors in the console.
4. Confirm Sun checkboxes appear unchanged (15 sphere + 3 custom +
   asteroid belt + corona_from_distance -- all still present, same labels).

**If the GUI fails to launch, stop here and report the error.**

---

## 1. No-change verification

D1 is extraction only. Nothing should look different from pre-D1.

### 1.1 Sun sphere shells (quick spot-check)

- [ ] Toggle Core on, verify it renders same as before
- [ ] Toggle Photosphere on, verify it renders same as before
- [ ] Toggle any outer shell (Termination Shock or Heliopause),
      verify it renders same as before
- [ ] Toggle all Sun shells on, verify no new traces or visual changes

### 1.2 Sun custom geometry

- [ ] Toggle Hills Cloud Torus, verify same rendering
- [ ] Toggle Outer Oort Clumpy, verify same rendering
- [ ] Toggle Galactic Tide, verify same rendering

### 1.3 Asteroid belt (critical -- must still work)

- [ ] Toggle Main Belt, verify it renders
- [ ] Toggle Hildas, verify it renders
- [ ] Toggle one Trojan group, verify it renders
- [ ] **These are dispatched by `create_sun_visualization()` which
      is unchanged. If they don't render, something broke the old path.**

### 1.4 Corona from distance

- [ ] In a non-Sun-centered view (e.g. Earth-centered), verify
      the corona_from_distance visualization still works if enabled

### 1.5 Regression (quick spot-check)

- [ ] Any one planet (e.g. Jupiter): verify shells still render
- [ ] Any one planet with magnetosphere: verify rotation still works

---

## 2. After testing

If all checks pass:
1. Copy files from sandbox to clean repo
2. Run `provenance_scanner.py` (expect 0 Tier-1 on touched files)
3. Deploy to GitHub
4. Report results for handoff document update

If issues found:
- Note which check failed and what you see
- Screenshot if visual
- We fix in next session

---

*D1 is purely additive. If anything looks different from pre-D1,
something activated the dormant configs unexpectedly -- stop and report.*
