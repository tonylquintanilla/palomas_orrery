<!-- Doc-Kind: hand | A starting prompt for the next coordinating session, written at the close of the one before it. -->
# Starting prompt: the next coordinating session

Built on orrery 1c0688ca6660b991c3de917826304892b9e7fa9f at
https://github.com/tonylquintanilla/palomas_orrery (branch main) and
gallery 0c832de1caf357efd34c6b5c36770ee394d0bbec at
https://github.com/tonylquintanilla/tonyquintanilla.github.io, with
patch_L297_3_close_session_20261119.py on top. Written Nov 19, 2026 by
the coordinating session of Nov 18 and 19 (Claude Opus 5.5).

Paste everything below the line into a new chat in the Orrery Project.

---

You are the coordinating session for Paloma's Orrery. The Project
instructions and the skills are resident; follow them.

Start the usual way:

1. Pull both repositories at HEAD and record the SHAs. The orrery's
   HEAD should hold this session's close: L-297 (the Lagrange points)
   is DONE with a note headed "2026-11-19, evening, LIVE AND LOOKED AT",
   and L-539 (every entry checked against JPL) exists. If not, the
   close patch was not pushed; say so before anything else.
2. Read documentation/WHERE_WE_ARE.md, then Tony's newest run-record
   copy (documentation/WHERE_WE_ARE_*_run_record.md) for his notes.
3. Read the night records: the orrery's newest "Nightly run" commit
   title and its El Nino check row. CURRENT means nothing to do. "EL
   NINO DUE" means NOAA has updated and Tony rebuilds the page by hand
   (L-060); NOAA's next update is expected 10 December 2026.
4. Three skills went up at v3.143 (orrery 1c0688ca), written by the
   session that bumped them from the repo's copies:
   gallery-cache-builder 1.20, interactive-exhibit 1.43 and
   provenance-discipline 2.37. Before work under any of them, confirm
   your loaded copy reads that version.

Where things stand:

- The eight Lagrange points are live in the orrery and on the website,
  and Tony's phone look passed every line. JPL has no L3, so there are
  eight, not ten.
- Next on the road: the design talk on missions by destination and
  encounters (L-534, L-529), ESCAPADE the worked example. Tony's two
  misses go there: each event's date in the box, and the destination
  and the mission's purpose in the box. A new item for the talk list:
  where several names share a few pixels in the Solar System view,
  only the largest body's name until zoomed in.
- Beside it, the cleanup this round found, each ruled Nov 19; the order
  is Tony's to set:
  - every path runs to its span's last day (L-533, a small gallery
    build: ask the last moment, as `fetch_path_last_day` does);
  - a craft orbiting a planet gets hourly points near today, no
    stopgap (L-538);
  - the Horizons check covers every entry the orrery asks JPL for,
    starting from a one-time list Tony scans (L-539, an orrery Code
    session);
  - a period prints today's figure with the digits its swing allows,
    the swing's measured range in its sentence (L-536; the Moon reads
    26.9 days live until then);
  - the 24 bodies in goldenrod (L-432): Planet 9, Mani and Vanth have
    colour keys that name no line; the rest are Tony's picks at his
    desk.

Lessons from the last session worth carrying:

- GitHub runs the nights hours after their schedule. On Nov 18 and 19
  the orrery's committed about 10:30 a.m. and 1:30 p.m. Chicago, the
  website's about 11:20 a.m. and 2:45 p.m. Read the commit times, not
  the workflow file, before giving Tony a push window.
- Read an item's whole ledger block before briefing from one ruling:
  the brief cited L-515's ruling 4 and missed ruling 6, an hour later,
  which replaced it. The Code session caught it.
- Before keying a body, read JPL's own name for its id. The orrery's
  two L3 entries drew asteroids under the points' names, and no check
  looked (L-539).
- A Code session can reach Tony's push window before its skill bumps.
  Put the bumps in the brief as their own part, or plan for the
  coordinator to write them after the push, as this session did.

Ask Tony one thing to begin: whether today is the design talk on
destinations and encounters, or one of the cleanup items first.
