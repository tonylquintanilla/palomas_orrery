# Pluto-Charon Binary System - Quick Visual Guide

**The Dance of Pluto and Charon** 🪐💃

---

## What Makes This Special?

### Regular Planet-Moon System (like Earth-Moon)
```
     Moon
      o
       \
        \
    ·   Earth  
    ^
    Barycenter (INSIDE Earth)
```
- Moon orbits Earth
- Barycenter inside Earth
- Earth barely wobbles

### Binary Planet System (Pluto-Charon)
```
   Charon
     o
      \
       \
   ·    o
   ^    Pluto
   Barycenter (BETWEEN them!)
```
- Both orbit the barycenter
- Barycenter OUTSIDE Pluto
- Both clearly move
- **This is unique in our solar system!**

---

## The Two Views

### View 1: Traditional (Center = "Pluto")
```
           Hydra
          /
     Styx/
        /
   Pluto (center)
    \   \
     \   Kerberos
      \
    Charon  Nix
```
**What you see:**
- Pluto stationary at center
- All moons orbit Pluto
- Standard satellite system

**Use this when:**
- Teaching basic orbital mechanics
- Comparing with other planet systems
- Keeping it simple

### View 2: Binary System (Center = "Pluto-Charon Barycenter") ⭐
```
           Hydra
          /
     Styx/
        /
 Pluto · Charon  ← BOTH MOVING!
    \  ^  \
     \ |   Kerberos
      \|
      Nix

   · = barycenter (the dance point)
```
**What you see:**
- Barycenter stationary at center (diamond marker)
- **Pluto orbits the barycenter** (small orbit)
- **Charon orbits the barycenter** (larger orbit)
- They orbit together with same 6.387 day period
- Four small moons orbit wider out

**Use this when:**
- Teaching barycenter physics
- Showing what makes Pluto unique
- Demonstrating binary dynamics
- **Maximum educational impact!**

---

## The Physics

### Mass Ratio
- Charon mass / Pluto mass = **0.117** (11.7%)
- Compare to Moon/Earth = 0.0123 (1.2%)
- **Charon is proportionally 10x more massive!**

### Orbit Sizes (from barycenter)
```
         17,500 km
   Pluto ·-------o Charon
         2,100 km
         
Total separation: 19,600 km
Barycenter: 960 km from Pluto's center
Pluto radius: 1,186 km

960 km > 1,186 km radius
= BARYCENTER IS OUTSIDE PLUTO!
```

### The Dance
- **Period:** 6.387 days (both synchronized)
- **Tidal locking:** Both always show same face to each other
- **Forever partners:** Locked in cosmic waltz

---

## For Paloma (Age 7-8)

**The Story:**
> "Pluto and Charon are special friends who dance together in space! They both move around a magic point between them - it's like they're holding hands and spinning in a circle. Watch them dance! They go around and around, always together, never letting go. No other planets in our solar system do this special dance!"

**Questions to Ask:**
- "Can you see them both moving?"
- "Where do you think the center point is?"
- "Why do you think they dance together?"
- "What would happen if they let go?"

---

## Implementation Checklist

### Setup
- [ ] Add `pluto_barycenter_var` checkbox variable
- [ ] Create "Pluto-Charon Barycenter" object (ID: '9')
- [ ] Mark Pluto as able to orbit barycenter
- [ ] Add to center dropdown menu

### Functions
- [ ] Create `PLUTO_MOONS` list
- [ ] Create `PLUTO_BARYCENTER_ORBITERS` list
- [ ] Create `plot_pluto_barycenter_orbit()` function
- [ ] Add barycenter mode to main loop
- [ ] Add traditional mode to main loop

### Testing
- [ ] Traditional mode works (Pluto centered)
- [ ] Binary mode works (barycenter centered)
- [ ] Pluto orbits barycenter in binary mode
- [ ] Charon orbits barycenter in binary mode
- [ ] Four small moons work in both modes
- [ ] Hover texts explain the physics
- [ ] Animation shows the "dance"

---

## Expected Behavior

### In Traditional Mode
```python
Center: "Pluto"
Objects plotted:
  - Pluto: stationary (center marker)
  - Charon: orbit around Pluto (solid + dashed)
  - Styx, Nix, Kerberos, Hydra: orbits around Pluto
```

### In Binary Mode 🌟
```python
Center: "Pluto-Charon Barycenter"
Objects plotted:
  - Barycenter: stationary (diamond marker)
  - Pluto: orbit around barycenter! (solid + dashed)
  - Charon: orbit around barycenter! (solid + dashed)
  - Styx, Nix, Kerberos, Hydra: orbits around barycenter
```

---

## Why This Is Cool

1. **Educational:** Teaches barycenter physics (not widely known)
2. **Unique:** Only in our solar system
3. **Visual:** The "dance" is beautiful to watch
4. **Accurate:** Shows real physics
5. **Engaging:** "They're dancing!" is memorable
6. **Paloma-friendly:** Easy to explain, hard to forget

---

## Token Budget
- **Used:** ~122,000 (64%)
- **Remaining:** ~68,000 (36%)
- **Status:** ✅ Good

---

*"Watch Pluto and Charon dance together - they never let go!"* 💫
