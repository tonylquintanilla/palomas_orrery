# HANDOFF -- 2026-08-25 -- the Sun renders; Earth is next

**Orrery: `4ad78a01a642166cb70218ae5728aa6f6c39d7f4`**
(https://github.com/tonylquintanilla/palomas_orrery, branch main).
**Gallery: `6420178342ea9acdb7fa4ef2e5240e1a9d62b3e8` to
`88633707ce55288bd4a7e03c59513655b3f4a8f3`**
(https://github.com/tonylquintanilla/tonyquintanilla.github.io).
Every SHA here was read from the live remote.

**Type: RULING, then BUILD, then RECORDS.** Six patches in the gallery
repo, none in the orrery. **The Sun is complete in the assembler: 19
shells, 14 spheres and 5 custom.** Mode 5 passed on the sphere half;
the custom half is un-rendered as this is written.

---

## The ruling that reorganized the work

Tony, 2026-08-25, in three parts.

**One. The artifact ladder has a second axis and it was never
sequenced.** The seven golden artifacts are seven propagation shapes --
conic, planetocentric, mean elements, spacecraft arc, barycentric
binary. That ladder is complete and it is good. What the orrery DRAWS is
a different axis entirely: interiors, atmospheres, magnetospheres,
belts, tori, rings, comae, solar shells, Hill spheres. Nothing in the
five segments or the seven artifacts sequences that axis.

**Two. Nobody ever decided that some structures would be shown and
others not.** L-100 carried a default -- shells live gallery-side, the
interactive stays "generative-lite" -- inherited from the Phase-1b cost
framing of 2026-07-08 and never ruled. Tony: "it is not my intent. The
general intent is to redo the orrery in the assembler. Part by part."

**Three. Artifacts reopen.** Reopen Artifact 1, get it right, then
Artifact 2, and so on. "Right" means the orrery recreated in the
assembler as far as possible. Re-locking is normal, not a failure --
and the orrery may improve on the way, as it did with the streamer belt.

The consequence that arrives first: the resolver requests EVERY feature
key the cache carries for an object, and the golden record hashes
`feature_keys`, `trace_role_counts` and `legend_groups`. So adding a
feature family to a body fails every locked artifact containing it. Under
part-by-part that is the normal event, not an edge case.

---

## What landed

| Patch | Repo | Result |
|---|---|---|
| `patch_L234_1_sun_features_only.py` | gallery | Sun entry + builder skip; 3 gates taught |
| `patch_L234_2_resolver_center_features.py` | gallery | centre features dispatched |
| `patch_L234_3_shell_set_renderer.py` | gallery | 14 spheres drawn |
| `patch_L234_4_hover_wrap_and_smoke_counts.py` | gallery | L-227 fix; scoped assertions |
| `patch_L234_5_solar_pole_and_streamer_band.py` | gallery | IAU pole + streamer belt |
| `patch_L234_6_oort_custom_shells.py` | gallery | torus, clumps, galactic tide |

Also delivered: `smoke_sun_shells.js` (30 checks) and the two payload
fixtures, `payload_earth.json` and `payload_jupiter_saturn.json`, which
had never been committed and without which the two existing smoke suites
could not run at all.

---

## Three things the build discovered

**The Sun was not an object.** Twelve entries in `objects_config.json`
and none of them the Sun: it existed only as a scene centre, drawn as a
yellow marker, with no catalogue record and so no `features` key. Gemini
correctly noted the Sun HAS an ephemeris relative to the SSB (target 10,
origin @0) and that the schema would take it -- Pluto and Charon are
already stored at `@9`. It does not help here: the resolver refuses any
object whose stored centre differs from the scene's, and the assembler
is built never to transform between frames. A barycentric solar scene is
a real future artifact and the use case L-137 was parked pending.

**`frame-origin` is load-bearing, not a label.** `served_window` is
computed from every object whose `canonical_frame` is `heliocentric`,
and a participant with no trust measurement nulls that window for the
WHOLE cache -- silently disabling the resolver's propagation bound
site-wide. Tested both ways: mislabelled `heliocentric`, the window does
go null.

**Three builder gates would have aborted the nightly, and reading the
code found none of them.** Running the loop with `process_object`
stubbed found the first; chasing it found the second. `assert_structural`
invariant #3 aborts on any non-spacecraft with no osculating block --
that would have killed every build, not just first ones.

---

## Mode 5

**Passed, 2026-08-24, on the 14 spheres.** Tony's one observation was
that the streamer belt was missing, which was the deferral working as
intended: the belt lies in the SOLAR equatorial plane and the Sun had no
pole yet, so drawing it would have reproduced L-229 one repo over.

**The custom half has not been rendered.** Patches 5 and 6 landed and the
nightly ran; the re-render is the first item for the next session.

---

## Ledger -- items to open

### L-234 -- Reopen Artifact 1: the Sun. Sun half DONE, Earth half open.

### L-235 -- Checks that cannot fail, gallery side [three instances]

1. `test_artifact1_earth.py` T5 reads `fp.compare(golden, golden)` -- the
   fingerprint against itself. It cannot return a difference, and the
   stored `artifact_1_earth_alone.json` is never opened. Passing since
   July.
2. `solar_system_earth_test2.html` line 99 prints "matches golden
   abbd01094852b57f" as a hardcoded `<summary>` caption. Nothing
   compares. And `abbd01094852b57f` is `scene_spec_hash` alone -- the one
   field that cannot move when features change.
3. The two smoke suites read `payload_jupiter_saturn.json`, which was a
   session artifact and was never committed. CLOSED by this session's
   regeneration.

### L-236 -- Gallery maintenance runner [designed, unbuilt]

A `maintenance_run.py` in the GALLERY repo, plus a dashboard button in
the existing Gallery & Web group. It belongs in the gallery because every
input it reads is there; a checker run from the orrery would reach a
sibling directory that exists only on Tony's machine, and a check that
cannot find its target skips quietly. First roster: module atlas and
index (generators); the artifact-1 golden compared against the STORED
file; the three Node suites, with Node's absence REPORTED rather than
skipped; served-cache structural validation; config feature-shape
validation.

### L-237 -- Artifact 1's golden is stale and needs re-cutting

Cut 2026-07-11. It differs from today in four fields, three of which
predate this session: `cache_snapshot_id`, `coordinate_bounds` (the
nightly refreshes Earth's osculating elements), `warnings` (it still
carries "served_window is null", untrue since 2026-07-22), and
`feature_keys`, which gains the Sun's six. Re-cut AFTER the custom-half
Mode 5, not before.

### L-238 -- `radius_fraction > 1.0` assumes a shell is above the surface

`_validate_feature_shapes` in `gallery_cache_builder.py` asserts it. True
of every shell served so far, false of every interior shell in the
orrery. Earth's inner core at 0.19 walks straight into it. This blocks
the Earth build and is its first patch.

---

## Ledger -- ORRERY-side recommendations from assembler findings

These are Tony's request: what the assembler work says about the orrery.

### L-239 -- Seed the three Oort builders [recommended]

`create_sun_hills_cloud_torus`, `create_sun_outer_oort_clumpy` and
`create_sun_galactic_tide` draw from the global numpy RNG, so the same
figure looks different on every render. The streamer band's own docstring
already names this and declines to copy it. The assembler ports are
seeded. Recommendation: seed all three in the orrery with the same
pattern -- a `RandomState` local to the builder, seed in the config --
so the two instruments agree about whether a render is reproducible.
Nothing depends on it today; it will matter the first time an Oort scene
is fingerprinted.

### L-240 -- Split declared drawing parameters from measured values [recommended]

`objects_config.json` now stores them apart: the streamer belt's cusp
(Suess & Nerney) and fade (Kasper) sit in `{value, unit, source}` nodes,
while the warp amplitude, lobe count and widths sit under a `drawing`
block whose `_declared` field says plainly that nobody has sourced them.
The orrery mixes both kinds in one dict with comments alongside.

This is the structural half of the reachability problem. The scanner
cannot tell a measurement from a drawing choice because the code does not
distinguish them, so the audit either over-counts (chasing citations for
`n_points`) or under-counts. Recommendation: adopt the same split in
`constants_new.py`'s FEATURE_REGISTRY when L-181 designs it -- measured
entries carry a source field as DATA; declared entries carry a declaration
string. The gallery has now proved the shape works.

### L-190 -- update with a measured count [existing item]

The scanner extracts only display strings from the shell modules: 10
units for Saturn, 20 for Jupiter, 116 for `shell_configs.py`, every one
of kind `string`. The ring, belt and torus numbers are function-local
literals and are not scored units at all. Measured at HEAD: 33 ring
entries at three fields each (99 numbers) plus 28 belt and torus values,
across four modules. None reachable by `worksheet_request_builder.py`.

### L-158 -- update with a measured instance [existing item]

Four of the Sun's fourteen sphere radii are derived expressions the
scanner does not score: `SOLAR_RADIUS_AU`, `CORE_AU`,
`RADIATIVE_ZONE_AU`, `CHROMOSPHERE_PHYSICAL_RADII`. All four are richly
cited; all four are unreachable, because the scanner scores literal
assignments. The claims inside them -- the 0.2 core factor and the 0.7
radiative-zone factor -- are already declared as visualization boundaries
with the measured ranges named, which is the right shape and invisible to
the tooling.

### L-181 -- two figures corrected [existing item]

"About 22 physical values" in the belt and torus surface: it is 28.
Neptune's four belt regions were never counted. And "ZERO carry a
`# Source:`": at HEAD three of the eight blocks do -- Jupiter's rings
(NASA Ring Fact Sheet, Galileo), Jupiter's belts (NASA Magnetosphere
Overview, Juno), Neptune's belts (Voyager 2; Ness et al. 1989). Saturn's
rings, Saturn's belts, both tori and Uranus's belts carry nothing.

### L-241 -- Hills torus hover states the cloud bounds, not the drawn ring [minor, both instruments]

`create_sun_hills_cloud_torus` hovers "2,000 to 20,000 AU". The drawn
surface runs 5,570 to 16,953 AU about a ring at 11,000, because a torus
built from an inner and outer bound puts its surface at the mid-radius.
Neither statement is wrong -- the bounds are the cloud, the ring is the
drawing -- but a reader measuring the picture against the hover will find
they disagree. Recommendation: say both. Identical in the assembler; fix
both or neither.

---

## Next session -- the Earth build

**First, three cheap things.**
1. SHA round trip: orrery `4ad78a01`, gallery `88633707`, read live.
2. Confirm loaded skill versions against the manifest.
3. Read the ledger -- L-234 through L-241 are new.

**Then re-render** the test page for the Sun's custom half. That Mode 5
is owed before anything else, and L-237's golden re-cut waits on it.

**Then Earth.** The inventory, measured at orrery HEAD:

| | |
|---|---|
| Already served | `atmosphere_shell` (1.05, 1.25), `van_allen_belts` |
| Interiors, not served | inner_core 0.19, outer_core 0.55, lower_mantle 0.85, upper_mantle 0.98, crust 1.0 |
| Also not served | hill_sphere 235.0 |
| Custom, not served | rotation_axis, dipole_cone, magnetosphere, leo, geostationary_belt |
| Missing | an `orientation` key -- Earth's pole is RA 0, Dec 90 (IAU 2018, J2000 celestial north) |

Two shapes it needs that the Sun did not. **The first patch is L-238**,
because five of the six new sphere entries are BELOW the surface and the
builder's validator refuses a `radius_fraction` under 1.0. And the
magnetosphere is a genuinely new geometry -- not a sphere, not a torus,
not a band.

Earth's block in `shell_configs.py` carries a block-level `# Source:`
header naming USGS, NASA Earth Fact Sheet, NOAA/NCEI and the Van Allen
Probes, verified in the April 2026 provenance audit. Those are the
sources the config entries should carry, copied with an
`orrery_constant` pointer, same pattern as the Sun's.

**Not on that path:** segment 2 (transport), the general audit, L-225,
L-231, and the barycentric solar scene.

---

## Skills

Loaded and matched at session start: `safe-file-editing` 1.8,
`ledger-and-session-records` 1.9, `gallery-assembler` 1.1,
`gallery-cache-builder` 1.4, `orrery-coding-conventions` 1.5,
`provenance-discipline` 2.6. No bumps this session, so no obligation is
carried forward.

One candidate for `safe-file-editing`, not yet ruled: a corrected patch
was built while its predecessor was already running, and the fix shipped
as a follow-on patch fingerprinted against the PATCHED state rather than
as a revert. That worked and both routes were proved byte-identical.
Whether it is a convention or a one-off is Tony's call.

---

## (do) and (decide) -- Tony-side

- **(do)** Drop `smoke_sun_shells.js`, `payload_earth.json` and
  `payload_jupiter_saturn.json` into `documentation/` in the gallery repo
  if not already there. The two existing suites cannot run without the
  payloads.
- **(do)** Archive the six patch scripts to `documentation/` in the
  gallery repo.
- **(do)** Run `python ledger_index.py` after the ledger patch.
- **(decide)** RICE for L-235 through L-241. Also still open from
  2026-08-24: L-231 at 1.8, L-232 at 3.8; from 2026-08-23: L-225 at 2.4,
  L-226 at 8.1.
- **(open)** The nightly reports `[RECOVER] could not remove retained
  data\solar-system.prev (WinError 5)` on every run and quarantines
  instead. Three quarantine directories have accumulated today alone.
  `gallery_cleanup.py` exists; whether this is worth fixing at source is
  undecided.

---

*Session written August 25, 2026 with Anthropic's Claude Opus 5. Orrery
`4ad78a01a642166cb70218ae5728aa6f6c39d7f4`; gallery
`6420178342ea9acdb7fa4ef2e5240e1a9d62b3e8` to
`88633707ce55288bd4a7e03c59513655b3f4a8f3`. Both confirmed against the
live remote.*
