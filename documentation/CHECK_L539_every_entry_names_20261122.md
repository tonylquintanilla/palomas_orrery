<!-- Doc-Kind: generated | The one-time list of L-539 (every entry checked): each entry the orrery asks JPL for, beside the name JPL gives its id, for Tony to scan once. -->
# Every entry beside JPL's name for it (L-539)

Written 2026-11-22 by `python horizons_unserved.py --list`, from `data/horizons_unserved_confirmations.json` and `celestial_objects.py` as they stood. Built on the orrery's working copy at Tony's machine, at the base the session recorded. Claude Opus 5.5 in Claude Code.

**What to do:** scan it once. In your run record, copy each line at the top you have looked at and end it "-- ok" or "-- wrong". A session then marks the "-- ok" ones as looked at. Nothing here changes an entry.

**The order is a hint, not a verdict.** The first part holds the entries whose own name, ignoring spaces, capitals and punctuation, does not appear inside JPL's name. A right entry can be there (a spacecraft the orrery calls by a short name), and a wrong one would have been too: Earth-Moon L3, asked as 3013, beside "3013 Dobrovoleva". Since this check, a wrong id like that one fails before it reaches this list.

Each line: the orrery's name -- the id it asks -- JPL's name for that id -- JPL's kind.

## JPL has no object for this id (4)

Neither of JPL's lists finds the id, and JPL's main service, asked as the orrery asks, refuses it. Each line ends with what the orrery draws the entry from instead.

- Xiangliu -- 120225088 -- JPL has no object for this id -- drawn from: typed elements in orbital_elements.py (Kiss et al. 2017), on the skip and fallback lists; drawn as an analytic orbit and position
- Hi'iaka -- 120136108 -- JPL has no object for this id -- drawn from: its orbit from JPL's elements cached on 2026-02-02, when JPL still answered 120136108 (the cache labels them JPL's osculating orbit); every plot asks JPL again and gets nothing; its position fetch gets nothing and it is on no fallback list, so the code draws no marker for it (not looked at in the window)
- Namaka -- 220136108 -- JPL has no object for this id -- drawn from: the same as Hi'iaka: JPL's elements cached on 2026-02-02 for 220136108, asked again and refused every plot; no marker by the code's reading
- MK2 -- 120136472 -- JPL has no object for this id -- drawn from: typed elements in orbital_elements.py (Bamberger 2025, arXiv:2509.05880), on the skip and fallback lists; drawn as an analytic orbit and position

## Names that differ (3)

- Patroclus-Menoetius Barycenter -- 20000617 -- Patroclus (system barycenter) -- asteroid barycenter
- Orcus-Vanth Barycenter -- 20090482 -- Orcus (system barycenter) -- asteroid barycenter
- MarsRover -- -168 -- Mars2020 (spacecraft) -- spacecraft

## Names that match (49)

- Earth-Moon Barycenter -- 3 -- Earth-Moon Barycenter -- barycenter (marked itself: the names are the same)
- Menoetius -- 120000617 -- Menoetius -- asteroidal system satellite (marked itself: the names are the same)
- Pluto -- 999 -- Pluto -- planet (marked itself: the names are the same)
- Apollo 11 S-IVB -- -399110 -- Apollo 11 S-IVB (spacecraft) -- spacecraft
- SOHO -- -21 -- SOHO (spacecraft) -- spacecraft
- Gaia -- -139479 -- Gaia (spacecraft) -- spacecraft
- Hayabusa2 -- -37 -- Hayabusa 2 (spacecraft) -- spacecraft
- OSIRISREx -- -64 -- OSIRIS-REx (spacecraft) -- spacecraft
- JamesWebb -- -170 -- James Webb Space Telescope (spacecraft) -- spacecraft
- Artemis II -- -1024 -- Artemis II (spacecraft) -- spacecraft
- Metis -- 516 -- Metis -- natural satellite (marked itself: the names are the same)
- Adrastea -- 515 -- Adrastea -- natural satellite (marked itself: the names are the same)
- Amalthea -- 505 -- Amalthea -- natural satellite (marked itself: the names are the same)
- Thebe -- 514 -- Thebe -- natural satellite (marked itself: the names are the same)
- Io -- 501 -- Io -- natural satellite (marked itself: the names are the same)
- Europa -- 502 -- Europa -- natural satellite (marked itself: the names are the same)
- Ganymede -- 503 -- Ganymede -- natural satellite (marked itself: the names are the same)
- Callisto -- 504 -- Callisto -- natural satellite (marked itself: the names are the same)
- Pan -- 618 -- Pan -- natural satellite (marked itself: the names are the same)
- Daphnis -- 635 -- Daphnis -- natural satellite (marked itself: the names are the same)
- Prometheus -- 616 -- Prometheus -- natural satellite (marked itself: the names are the same)
- Pandora -- 617 -- Pandora -- natural satellite (marked itself: the names are the same)
- Mimas -- 601 -- Mimas -- natural satellite (marked itself: the names are the same)
- Enceladus -- 602 -- Enceladus -- natural satellite (marked itself: the names are the same)
- Tethys -- 603 -- Tethys -- natural satellite (marked itself: the names are the same)
- Dione -- 604 -- Dione -- natural satellite (marked itself: the names are the same)
- Rhea -- 605 -- Rhea -- natural satellite (marked itself: the names are the same)
- Titan -- 606 -- Titan -- natural satellite (marked itself: the names are the same)
- Hyperion -- 607 -- Hyperion -- natural satellite (marked itself: the names are the same)
- Iapetus -- 608 -- Iapetus -- natural satellite (marked itself: the names are the same)
- Phoebe -- 609 -- Phoebe -- natural satellite (marked itself: the names are the same)
- Ariel -- 701 -- Ariel -- natural satellite (marked itself: the names are the same)
- Umbriel -- 702 -- Umbriel -- natural satellite (marked itself: the names are the same)
- Titania -- 703 -- Titania -- natural satellite (marked itself: the names are the same)
- Oberon -- 704 -- Oberon -- natural satellite (marked itself: the names are the same)
- Miranda -- 705 -- Miranda -- natural satellite (marked itself: the names are the same)
- Portia -- 712 -- Portia -- natural satellite (marked itself: the names are the same)
- Mab -- 726 -- Mab -- natural satellite (marked itself: the names are the same)
- Triton -- 801 -- Triton -- natural satellite (marked itself: the names are the same)
- Despina -- 805 -- Despina -- natural satellite (marked itself: the names are the same)
- Galatea -- 806 -- Galatea -- natural satellite (marked itself: the names are the same)
- Charon -- 901 -- Charon -- natural satellite (marked itself: the names are the same)
- Styx -- 905 -- Styx -- natural satellite (marked itself: the names are the same)
- Nix -- 902 -- Nix -- natural satellite (marked itself: the names are the same)
- Kerberos -- 904 -- Kerberos -- natural satellite (marked itself: the names are the same)
- Hydra -- 903 -- Hydra -- natural satellite (marked itself: the names are the same)
- Dysnomia -- 120136199 -- Dysnomia -- asteroidal system satellite (marked itself: the names are the same)
- Vanth -- 120090482 -- Vanth -- asteroidal system satellite (marked itself: the names are the same)
- Weywot -- 120050000 -- Weywot -- asteroidal system satellite (marked itself: the names are the same)

## Not on this list

- The 110 entries the website serves are already held to their typed names (`horizons_name` in `celestial_objects.py`) by the Horizons check every 30 days.
- 6AC4721, asked with no JPL id: its id is the word 'none': the orrery sends it, JPL answers "No matches found", and it is drawn from its typed elements (Tony keeps it so, 2026-11-04).
- Never asked of JPL (17): Planet 9, TRAPPIST-1, TRAPPIST-1 b, TRAPPIST-1 c, TRAPPIST-1 d, TRAPPIST-1 e, TRAPPIST-1 f, TRAPPIST-1 g, TRAPPIST-1 h, TOI-1338 A/B, TOI-1338 A (G-type), TOI-1338 B (M-type), TOI-1338 b, TOI-1338 c, Proxima Centauri, Proxima Centauri b, Proxima Centauri d.

