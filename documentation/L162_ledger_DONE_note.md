Search `LEDGER_CONSOLIDATED.md` for the `[L-162]` block's status line:

```
<!-- L:162 status:OPEN upd:2026-07-29 section:W.Active flag: rice:2/2/95/1 -->
```

(Adjust the exact `upd:`/`rice:` values to whatever is currently live --
just confirm the line before editing, since other sessions may have
touched it.)

Replace `status:OPEN` with `status:DONE` and update `upd:` to today's
date. Then append this to the end of the block, after the existing
**Ref:** line:

```
**As-built (2026-07-29, Sonnet 5):** Built and verified against
`90d022e`. All 6 Gap items landed: 14 named constants, `CENTER_BODY_RADII`
rewired to all 17 names, 9 aliases re-pointed in
`planet_visualization_utilities.py`, 14 `CONCEPT_ALIASES` entries added,
pre-flight int/float check done (Sun + Jupiter only, no consumer at
risk), `py_compile` + ASCII/LF clean. `test_constants_provenance.py`:
73/73 passed. Scanner re-run: 764 -> 778 findings (+14, exactly the new
constants), Tier 1 unchanged at 145, zero new inconsistencies. Full
diffs: `AS_BUILT_L162_phaseA.md` + three `.patch` files. Ready to push;
credit lines added to `constants_new.py`, `planet_visualization_utilities.py`,
`provenance_scanner.py`.
```

Then run `ledger_index.py` to move this item from the `D.RECONCILED
LEDGER -- OPEN` / `W.Active` index into the closed-items index.
