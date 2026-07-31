Where we are 7/30/2026, 9:06 PM

Interactive gallery build (the master plan's own Phase 0–6): Phase 0 (stack
proof, architecture B′), Phase 1a (vocabulary), and Phase 1b (data serving
pipeline — nightly cache builder, coverage index, served_window trust
system) are all DONE. Layer 3 (Task Scheduler) is live with a known
intermittent promotion-step glitch still being watched.

Phase 2 (current phase) — the artifacts themselves:

Artifact 1 (Earth) — built, Mode-5 accepted. Closed.
Artifact 2 (Jupiter/Saturn: rings, shells, radiation belts) — next in line,
still blocked. Not on data — the cache builder already serves the real
ported values. Blocked because the client-side JS layer that would draw
those features (L-154) doesn't exist yet.

The detour (L-154–L-162, provenance scanner rebuild) — status:
Design and ledger formalization for the whole cluster: closed.
Scanner rebuild (Opus 5, Phase 1 sub-stepped 1a–1f):

  1a  DONE
  1b  DONE — data serving pipeline, landed and pushed
  1c  DONE — citation-window inheritance. Landed, independently verified,
      pushed (0621dfb). Two things came out of building it, both now
      closed out themselves:
        L-173 — 8 body blocks in shell_configs.py genuinely missing
          citations (18 findings: Pluto 10, Venus 3, Eris 2, Mars 2,
          CUSTOM_SHELLS['Mercury'] 1). Not a scanner bug — real sourcing
          gap. Parked for the Phase 4 Gemini worksheet.
        L-174 — citations pitched one nesting level too far out for the
          resolver to see (ring_params). Root-caused, fixed (ring_params),
          and a permanent scanner diagnostic added so the same shape
          in three other files (currently latent, no live mis-scoring)
          stays visible instead of silently fine. Closed 7/30.
  1d  NEXT — citation-recognition regexes + D8 vocabulary + L-078(d),
      now also carrying the citation-form gap from Gap item 7.
  1e  banners/labels/Tier-2 sub-band
  1f  the D9 structural check (L-158)

Current scanner state at HEAD: Tier 1 132, Tier 2 588, Tier 3 61, Tier 4 2
(783 raw findings/121 files — the +1s over the 781/118 baseline are the
scanner's own self-referential quirk, real population conserved).

Once Phase 1 (1a–1f) closes, L-157/L-161 (Gemini cross-check sweeps) run,
then L-154's own design questions (geometry-building approach, legend
behavior, artifact sequencing) resume, then Artifact 2 actually gets built.

Adjacent, already resolved: L-162 (CENTER_BODY_RADII naming) done. L-163
(module role/domain classification) — role side closed; domain side
deferred into this same cluster.

So: 1d is the next build step, and it's one sub-step closer to Artifact 2
than it was at session start.