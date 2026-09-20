# Build Manifest -- L-342: every number in a hover shows the figures its source supports

**Built on gallery `cdfa74c3b12cd50e8955acefb75e36f4bcbbe4ca`
at https://github.com/tonylquintanilla/tonyquintanilla.github.io
and orrery `2978ceeb6bb324749b6c56096ec23ab6427f044e`
at https://github.com/tonylquintanilla/palomas_orrery.
Both HEADs were read live with `git ls-remote` on 2026-09-20. Both
repositories were cloned there. Every hover quoted below was built in
node from the pushed gallery files, not recalled.**

**Rules this work runs under.** Also fetch, from the orrery at
`2978ceeb`: `PROJECT_INSTRUCTIONS.md` (v3.64) and these skills under
`skills/<name>/SKILL.md`: provenance-discipline 2.15 (the section "The
Figure Count Is a Declared Field", Rules 1 to 8), interactive-exhibit
1.4, gallery-cache-builder 1.5, gallery-assembler 1.3, safe-file-editing
1.11, agentic-pre-test 1.2, ledger-and-session-records 1.11. Inside
Tony's Project they load as installed skills; compare each loaded
version line with the protocol's manifest table and STOP on a mismatch.
**In your first reply, name the rule files you actually read.**

**Type: BUILD CONTRACT.** Written before the build, zero code.
**Prepared:** September 20, 2026 by Claude Fable 5.1, Tony Quintanilla
integrator. **For:** Claude Opus 5, as builder.
**Replaces** task 1 of `HANDOFF_L322_C1_shipped_and_reviewed_20260919.md`
("the wide figures fix"). Tasks 2 and 3 of that handoff, Stage C2 and
Stage D, are unchanged and follow this build.

Who this is written for: Tony is a retired professional engineer who
builds this project by conversation with AI partners. He is not a
programmer, runs scripts from VS Code's Run button, and commits and
pushes through GitHub Desktop. Write to him in plain sentences, one
request per message.

---

## 1. What is wrong, in plain terms

There are two faults, and the second is the one that makes this hard.

**Fault A: the kilometre line ignores the declared count.** A shell's
radius in Earth radii is printed to its declared figures. The kilometre
line beside it goes through `fmtKm`, which always rounds to a whole
number. So the outer core, declared to five figures, reads "3,480 km"
and should read "3,480.0 km".

**Fault B: the browser does arithmetic on numbers that were already
rounded.** The export rounds each constant once, to its declared
figures. That is Rule 6 and it is right. But the hover then computes
the kilometre line and the altitude line FROM that rounded number. Rule
4 says compute from the primary inputs and round once. The result is
wrong numbers on the live site today:

- The upper atmosphere's hover says **"Altitude: 574 km"**. The source
  says 600 km. The browser took the served 1.09 Earth radii, subtracted
  one, and multiplied by Earth's radius.
- The lower atmosphere's hover says **"Altitude: 51 km"**. The source
  says 50 km.
- The Hill sphere's hover says "1,498,862 km". The store's own value,
  rounded once, is 1,500,000 km.

Both altitudes read correctly before C1, because the served value then
carried every digit. No formatter can repair Fault B: no rounding of
574 gives 600. The store already holds the right numbers as their own
constants (`EARTH_THERMOPAUSE_ALTITUDE_KM` is 600, two figures). The fix
is to SERVE those and print them, and to compute in the browser only
what the store does not hold.

## 2. What was measured at gallery `cdfa74c3`

**The formatting code**, all in `gallery/feature_renderers.js`:
`servedFigures` (line 145), `fmtServed` (153), `sigFigures` (181),
`fmtKm` (314), `kmAndAu` (320). `kmAndAu` is called from 16 places:
lines 571, 572, 573 (ring edges and thickness); 750 (radiation belts);
847, 849 (shells given as a radius fraction); 1073, 1075 (the Sun's
streamer belt); 1433, 1436 (equatorial ring); 1569, 1572 (shell sets);
1803 (magnetopause); 1867 (bow shock); and its own definition's
neighbours. Re-derive the list by grep before editing; map which of
them can ever receive a declared count and which cannot.

**Which served numbers carry a count today.** In
`data/objects_config.json`: Earth has 19 served numbers with an integer
count, 1 marked `"exact"`, 17 with `null`, and 6 with no `figures` key.
The Sun has 26 served numbers, Jupiter 3 and Saturn 2, and none of them
has a `figures` key. So today only Earth's hovers can change. The
mechanism must still cover every call site, because Tony's instruction
of 2026-09-19 is "here and elsewhere", and C2 and the later slices will
turn those nulls into counts.

**How a link works.** `tools/mirror_constants.py` fills a slot by name.
A dict that has both `value` and `orrery_constant` is its own slot. A
dict with `orrery_constant` and no `value` uses its FIRST child that
has a `value`. The mirror refuses to create a slot that is not there.

**The served primaries this fix needs already exist in the export**, in
the gallery at `data/constants_export.json`:

    EARTH_EQUATORIAL_RADIUS_KM       6378.1366   km   8
    EARTH_STRATOPAUSE_ALTITUDE_KM    50.0        km   2
    EARTH_THERMOPAUSE_ALTITUDE_KM    600.0       km   2
    EARTH_LEO_LOWER_ALTITUDE_KM      200.0       km   exact
    EARTH_LEO_UPPER_ALTITUDE_KM      2000.0      km   exact
    EARTH_LEO_INNER_KM               6578.1366   km   8
    EARTH_LEO_OUTER_KM               8378.1366   km   8
    EARTH_GEOSTATIONARY_RADIUS_KM    42164.17    km   7
    EARTH_HILL_SPHERE_KM             1500000.0   km   3

No orrery change is needed. This build is in the gallery only.

**The gallery's offline run** is 14 of 14 at this SHA. None of the 14
reads a number inside a built hover against a declared count.

## 3. The design: three rules, in the skill's own terms

**Rule S, serve it.** A displayed quantity that has its own constant in
the store is SERVED from that constant and printed as served. The
browser does not recompute it. (provenance-discipline Rules 4 and 6.)

**Rule P, propagate it.** A displayed quantity the store does not hold
is computed in the browser from the most primary served values
available, and its figure count is worked out by Rule 3 of the skill:

- A product or quotient keeps the fewest figures among its inputs.
- A sum or difference is good to the coarsest decimal place among its
  inputs. The place of a value is `floor(log10(|value|)) - (figures -
  1)`. The result's count is read back from its own size and that place,
  never below one.
- An `"exact"` input is skipped when finding the fewest or the coarsest.
  `KM_PER_AU` and the literal 1 in "radius minus one" are exact.
- If ANY non-exact input has no count (`null` or no key), the result has
  no count.

**Rule F, format it.**

- A number with an integer count prints to exactly that many
  significant figures, in plain digits, with a thousands separator, and
  keeps a significant trailing zero: "3,480.0 km".
- A number with no count prints EXACTLY as it does today, byte for
  byte. This is what keeps the Sun, Jupiter, Saturn and the 17 unvisited
  Earth numbers unchanged.
- An `"exact"` number prints as it does today.
- The AU figure in brackets is a comparison aid and stays short: it
  prints to three figures or to the count, whichever is FEWER. (Rule 7:
  a display may show fewer, never more.) Its plain-or-exponent style
  stays as it is today.
- Formatting a served number at its own count is not a second rounding;
  the export already rounded it. Only Rule P values are rounded in the
  browser.

## 4. The served slots to add

Each is a new entry inside the shell's block in
`data/objects_config.json`, placed AFTER `radius` so the shell's own
link keeps finding `radius` as its first slot. Each carries `value`,
`unit`, `figures` and its own `orrery_constant`, with the value taken
from the export as it stands.

| Shell | New entry | Linked constant |
| --- | --- | --- |
| lower_atmosphere | `altitude` | `EARTH_STRATOPAUSE_ALTITUDE_KM` |
| upper_atmosphere | `altitude` | `EARTH_THERMOPAUSE_ALTITUDE_KM` |
| leo_inner | `altitude` | `EARTH_LEO_LOWER_ALTITUDE_KM` |
| leo_inner | `radius_km` | `EARTH_LEO_INNER_KM` |
| leo_outer | `altitude` | `EARTH_LEO_UPPER_ALTITUDE_KM` |
| leo_outer | `radius_km` | `EARTH_LEO_OUTER_KM` |
| geostationary_ring | `radius_km` | `EARTH_GEOSTATIONARY_RADIUS_KM` |
| hill_sphere | `radius_km` | `EARTH_HILL_SPHERE_KM` |

The geocorona gets none: its primary IS the 100 Earth radii, so its
kilometres are a Rule P product. The interior shells get none: they are
already served in kilometres.

**Who writes the config.** The mirror cannot create a slot, and the
editor refuses numbers. So this patch writes the eight entries directly,
in place, with the shared scanner. That is the one-off exception already
recorded on L-340, used a second time; say so in the patch's
description and add a line to L-340. The proof that the patch wrote the
right values is that a mirror run straight afterwards reports NO CHANGE.

**How the hover uses them.** Where `altitude` is served, print it, and
compute the kilometre radius as planet radius PLUS altitude (a Rule P
sum from two primaries). Where `radius_km` is served, print it, and
compute a missing altitude as `radius_km` MINUS planet radius. Where
neither is served, fall back to today's arithmetic with Rule P counts.
The shell is still DRAWN from `radius`; nothing about geometry changes.

## 5. What the hovers must read afterwards

Worked by hand from sections 3 and 4 with a small reference script.
These strings are the acceptance test. The AU figure count is in
brackets.

| Hover | Line | Today | After |
| --- | --- | --- | --- |
| Inner Core | radius | 1,222 km | 1,221.5 km (3) |
| Outer Core | radius | 3,480 km | 3,480.0 km (3) |
| Lower Mantle | radius | 5,710 km | 5,710 km (3) |
| Upper Mantle | radius | 6,347 km | 6,346.6 km (3) |
| Lower Atmosphere | altitude | 51 km | 50 km (2) |
| Lower Atmosphere | radius | 6,429 km | 6,428 km (3) |
| Upper Atmosphere | altitude | 574 km | 600 km (2) |
| Upper Atmosphere | radius | 6,952 km | 6,980 km (3) |
| LEO inner edge | altitude | 200 km | 200 km (3) |
| LEO inner edge | radius | 6,578 km | 6,578.1366 km (3) |
| LEO outer edge | altitude | 2,000 km | 2,000 km (3) |
| LEO outer edge | radius | 8,378 km | 8,378.1366 km (3) |
| Geostationary | altitude | 35,786 km | 35,786.03 km (3) |
| Geostationary | radius | 42,164 km | 42,164.17 km (3) |
| Geocorona | altitude | 631,436 km | 600,000 km (1) |
| Geocorona | radius | 637,814 km | 600,000 km (1) |
| Hill Sphere | altitude | 1,492,484 km | 1,490,000 km (3) |
| Hill Sphere | radius | 1,498,862 km | 1,500,000 km (3) |

Unchanged, and the check must show it: every hover in the Sun's room,
Jupiter's and Saturn's; the Moon; the rotation axis; the Sun direction;
the magnetopause, the bow shock and both radiation belts, whose served
numbers have no count until C2. The Crust is served as exactly one Earth
radius; work its kilometre line by Rule P and add it to the table.

If your own working gives a different string for any row, do not pick
one. Show Tony both and the step where they part.

## 6. The check

The check written for L-342's first finding tested the formatter alone.
It could not see that a hover reached a different formatter. This one
reads BUILT HOVERS.

- It builds both rooms the way `smoke_arrival.js` does, with the Sun
  direction passed so the magnetosphere is built.
- For Earth, it finds each line in the table above in the built hover
  text and compares it with the expected string. The expected strings
  are computed inside the check from the served values by Rules S, P
  and F, written separately from the renderer's code, so the check does
  not grade the renderer with the renderer's own arithmetic.
- For every hover whose numbers have no count, it compares the whole
  hover text with a fixture recorded at `cdfa74c3`, byte for byte.
- It prints how many hovers and how many numbers it examined, and names
  any number in a hover that it could not account for. An unexamined
  number fails the run.
- It joins `gallery_maintenance_run.py` as a gating checker.

**Show it failing before the fix goes in**: run it against the unpatched
renderer and confirm it names the outer core and the upper atmosphere's
574 km. Then show it failing three more ways after the fix: a count
ignored at one call site; a served `altitude` removed so the browser
falls back to subtracting; a count-less Sun hover changed by one
character.

## 7. Order of delivery

1. The check and its fixture, shown red on the unpatched tree. Do not
   deliver it to Tony red; it ships in the same patch as the fix.
2. One gallery patch: the eight config entries, the renderer change, the
   check, the maintenance run wiring. Run on a throwaway copy of the
   pushed tree; a second run refuses.
3. Tony runs the patch from the gallery ROOT, runs the mirror (expect no
   change), PAUSES OneDrive syncing, rebuilds the cache, runs the
   maintenance run until "Cache in step" and the new check are green,
   moves the patch to `documentation/`, commits the config and the cache
   TOGETHER, pushes, runs the live check, and looks at Earth's room on
   his phone.
4. A ledger patch in the orrery: L-342 records both faults and the fix;
   L-340 gains the second use of the config-write exception.
5. For the next bump of interactive-exhibit, owed and not cut here: a
   hover prints a served primary where the store has one, and computes
   with Rule P where it does not.

## 8. Out of scope

- Stage C2 and Stage D. They follow.
- Any change to the orrery's store, export or checkers.
- Words in hovers. "A ring of satellites 35,786 km above the equator" is
  prose, and prose may show fewer figures.
- Whether "6,578.1366 km" and "6.610735 Earth radii" are pleasant to
  read. They are correct by the rules, because a declared drawing floor
  counts as exact. Rule 7 lets a display show fewer. That is Tony's to
  judge on the phone, after the numbers are right.
- The Sun's, Jupiter's and Saturn's counts. They arrive with their
  slices.

## 9. Tony's decisions, and when they fall due

1. **(look, after the push)** Earth's room on the phone, with the table
   in section 5 beside him.
2. **(decide, after looking)** Whether any rule-correct number should be
   shown shorter for readability, by name.

## 10. Tony-action rollup

1. **(do)** File this manifest in the orrery's `documentation/`, commit,
   push. Give Opus this file and both SHAs, saying which is which.
2. **(do)** Follow section 7 step 3 when the patch arrives.

---

Written September 20, 2026 with Anthropic's Claude Fable 5.1.
