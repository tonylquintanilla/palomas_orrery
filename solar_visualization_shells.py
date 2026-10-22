"""
solar_visualization_shells.py - Sun interior, corona, and heliosphere shell traces.

The largest shell module: 12 sphere shells from core to gravitational
influence boundary, plus custom geometry for the Hills Cloud (a tilted
disk of dots along orbits, from hills_cloud_sampler.py), Oort Cloud
clumpy distribution, galactic tide shell, the corona (a fade of dots
from sun_corona_sampler.py, with the streamer band under its legend
entry) and the zodiacal dust cloud (dots from zodiacal_dust_sampler.py).
Includes the v3.18 solar shell refactor: single-info-marker pattern,
n_points=20/25, and the inner corona shells (Streamer Belt, Roche Limit,
Alfven Surface) added for the MAPS comet coronal journey.

Consumed by: planet_visualization.py (routing dispatcher),
             palomas_orrery.py (hover_text_sun import)

Role: rendering/shells
Domain: orrery

Module updated: October 21, 2026 with Anthropic's Claude Opus 5.5
(L-191, the Sun's share: one string per shell. The fourteen
<shell>_info_hover twins are gone; each <shell>_info is written with
newlines and is both the checkbox tooltip and, with each newline made
<br>, the plot hover.)
Module updated: October 21, 2026 with Anthropic's Claude Opus 5.5
(L-460: the corona, its dots and the streamer belt, starts at the
corona's base, CORONA_BASE_RADII; its hover and panel words say so.)
Module updated: October 20, 2026 with Anthropic's Claude Opus 5.5
(L-410, Tony's marks on the website list: the corona's hover gives the
Alfven surface's distance in km beside AU, from its row; the module
description names the corona and the dust cloud.)
Module updated: October 19, 2026 with Anthropic's Claude Opus 5.5
(L-410 with L-131, the Sun's two fades: the inner and outer corona
spheres became one fade of dots, create_sun_corona, placed by
sun_corona_sampler.py from Mann et al. (2023)'s density, and the
streamer belt joined it under one legend entry; the zodiacal dust cloud
is new, create_sun_zodiacal_dust, placed by zodiacal_dust_sampler.py
from Kelsall et al. (1998)'s model. Their words are Tony's approved
list, written in newlines. The two corona spheres, their four strings
and the streamer belt's tooltip are gone.)
Module updated: October 18, 2026 with Anthropic's Claude Opus 5.5
(L-411 follow-up: the termination shock's Voyager 2 line cites Li et
al. 2008, the paper its wind speeds come from. Tony's word.)
Module updated: October 17, 2026 with Anthropic's Claude Opus 5.5
(the Sun's numbers, L-228 and L-411: the hovers print the Alfven
surface's usual range, the coronagraph floor, Parker Solar Probe's
closest approach, the inner corona, the helmets, the core, radiative
zone and photosphere edges, the photosphere's thickness, the
chromosphere's line and the termination shock's range, crossing and
wind speeds from their rows, each with a citation the visitor sees.
Sedna's farthest point is worked out from the period record the
orrery fetched, measured from the solar system's centre of mass. The
pole-and-streamer ranges, which had the shape backwards, are gone, and
the Voyagers' line says both are past the heliopause. Words approved
by Tony.)
Module updated: October 11, 2026 with Anthropic's Claude Opus 5.5
(L-421, the website half: the Hills cloud draws
hills_cloud_sampler.drawn_hills_cloud(), seeded, so every plot is the
same cloud and the website draws the same dots from
data/drawings/hills_cloud.json.)
Module updated: October 10, 2026 with Anthropic's Claude Opus 5.5
(L-421, the inner Oort cloud: the Hills cloud is drawn as dots along
orbits following Nesvorny et al. (2025) -- a disk tilted about 30
degrees, with two arms -- from hills_cloud_sampler.py, its typed 2,000
and 20,000 AU defaults gone, and the clumpy outer cloud's typed 20,000
and 100,000 AU defaults too. The inner cloud gives way to the round
outer cloud across a band from INNER_OORT_DISK_OUTER_AU to
INNER_OORT_CLOUD_AU: the Hills cloud thins out across it, the clumps and
the galactic tide fill in across it, and every string that printed the
single edge says the band. The Hills cloud's words are Tony's confirmed
words of 2026-10-09 with the citation; two comments that named Hills
(1981) name the rows' real sources.)

Module updated: October 6, 2026 with Anthropic's Claude Opus 5.5
(L-420, after Tony's look: the galactic tide is drawn brighter, with
5,000 points, and with a faint double cone where the tide's
strength peaks, halfway between the galaxy's plane and its poles,
so its shape reads from the side as an hourglass. One hover line
names the cone. Words approved by Tony, 2026-10-06.)

Module updated: October 4, 2026 with Anthropic's Claude Opus 5.5
(L-371, the Sun's distance cards: every hover line that states one of
the Sun's distance rows prints it from the row, at the count its row
gives it, through constants_rows.row_text() -- the termination shock
at 94.01 AU, the heliopause at 121 AU, the Oort cloud's edges with
their ranges, the gravitational reach as the Sun's Hill radius, 0.65
parsecs, and the corona, helmet cusp and Roche limit by their counts.
The unsourced 100,000-200,000 AU range is gone with its row. Wording
changes approved by Tony are listed in the session handoff.)

Module updated: October 2, 2026 with Anthropic's Claude Opus 5.5
(L-406: the galactic tide is drawn tilted into the galaxy's plane, about
the galactic pole of J2000 from constants_new.py, between the outer Oort
cloud's two edges, with its density following the tide's strength --
sparse at the galaxy's plane and poles, thickest halfway between. It had
been drawn about the ecliptic, densest at the poles, at a typed 50,000
AU, while its words said the galaxy's plane. Hover rewritten in Tony's
approved words of 2026-10-02.)

Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-345, patch D20: CHROMOSPHERE_PHYSICAL_RADII is a conversion of
CHROMOSPHERE_TOP_KM now, with no count of its own, so the hover prints
it through constants_rows.conversion_text(). Same digits, 1.003.)

Module updated: September 28, 2026 with Anthropic's Claude Opus 5.5
(L-322 Stage D, patch D17: the chromosphere hover prints its radius by
its row's count, 1.003 solar radii (was 1.002875); the Sun's radius
through exact_text(), 695,700 km as before; and the skin as a share of
the radius at the depth's one figure, 0.3% (was 0.29%).)

Module updated: August 2026 with Anthropic's Claude Opus 5 (L-224:
create_sun_streamer_band -- the streamer belt as a warped helmet-and-
stalk band; the sphere it replaces is retired in patch 2)

Module updated: May 2026 with Anthropic's Claude Opus 4.6
    D3.1 sweep (May 2026): hovertext/legendgroup consolidation.
May 27, 2026: Stage 3 info-marker standard sweep (Opus 4.7). 9 info
    markers brought to red-border standard (mix of opacity 0.9 and
    0.95 sources, all normalized to opacity=1.0); 1 red-on-red
    exception preserved (Roche limit rgb(200, 60, 60), the closest
    case to red in the entire sweep). Dead create_sun_direction_indicator
    import removed (Sun does not get a self-direction indicator).
May 28, 2026: Phase 1 re-pipe (Opus 4.7). 18 live inline info markers
    routed through orrery_rendering.create_info_marker() factory.
    Roche Limit (rgb(200,60,60)) red-on-red exception now expressed
    cleanly via factory's border_color='white' parameter (the v12
    "exception" became the rule for reddish shells under Tony's
    two-standards). Five gray-border sites (Outer/Inner/Inner Limit
    Oort, Termination Shock, Photosphere) lose their inherited gray
    border to factory default red. Four sites size 6->8 visual bump.
September 23, 2026 (Claude Opus 5.5, L-322 Stage D): one comment names
    the pole dict's new home, constants_new.planet_poles. No code changed.
"""
import numpy as np
import math
import plotly.graph_objs as go
from orrery_rendering import create_info_marker

from planet_visualization_utilities import (create_sphere_points, create_streamer_band_shape,
                                            STREAMER_BAND_DEFAULTS,
                                            SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU, SUN_RADIUS_KM,
                                            INNER_CORONA_RADII, OUTER_CORONA_RADII, HELMET_CUSP_RADII,
                                            ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
                                            TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
                                            INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU, 
                                            GRAVITATIONAL_INFLUENCE_AU,
                                            AU_PER_LIGHT_YEAR,
                                            CHROMOSPHERE_PHYSICAL_KM, CHROMOSPHERE_PHYSICAL_RADII)
# L-322 Stage D, patch D17: print rows by the counts their rows state.
from constants_rows import figures_of, exact_text, format_prints, conversion_text
# L-371: every Sun distance row prints at its own count, in any unit.
from constants_rows import row_text
# L-406: the pole the galactic tide is drawn about.
from constants_new import (GALACTIC_NORTH_POLE_RA_J2000_DEG,
                           GALACTIC_NORTH_POLE_DEC_J2000_DEG)
# L-421: the near end of the band where the inner cloud's disk gives way
# to the round outer cloud.
from constants_new import INNER_OORT_DISK_OUTER_AU
# L-460: where the corona, and the streamer belt drawn with it, begins.
from constants_new import CORONA_BASE_RADII

#####################################
# Sun Visualization Functions
#####################################

#####################################
# Shared derived sentences (L-179 / L-180, 2026-08-07)
#####################################
# Each figure below is interpolated from constants_new.py, never typed.
# One fragment, referenced by every string that states the fact, so the
# statement exists once and cannot drift from the constant or from its
# own duplicate. Editing the constant updates every display site.

# The Sun's distances as text, each printed from its row at the count the
# row gives it (L-371, 2026-10-04). A hover names these, never a typed
# figure, so the words cannot drift from the drawing or from the store.
_OORT_INNER_EDGE = row_text('INNER_LIMIT_OORT_CLOUD_AU', grouping=True)
_OORT_HILLS_EDGE = row_text('INNER_OORT_CLOUD_AU', grouping=True)
# L-421 (2026-10-10): the inner cloud gives way to the round outer cloud
# across a band, from INNER_OORT_DISK_OUTER_AU (Nesvorny et al. 2025) to
# INNER_OORT_CLOUD_AU (Portegies Zwart et al. 2021), Tony's ruling of
# 2026-10-09. The Hills cloud's tilt is HILLS_CLOUD_TILT_DEG (Nesvorny et
# al. 2025). Each printed from its row; the sources are on the rows.
_OORT_DISK_EDGE = row_text('INNER_OORT_DISK_OUTER_AU', grouping=True)
_HILLS_TILT = row_text('HILLS_CLOUD_TILT_DEG')
OORT_BAND_SENTENCE = f"between {_OORT_DISK_EDGE} and {_OORT_HILLS_EDGE} AU"
INNER_OORT_BAND_NOTE = (
    f"The inner cloud gives way to the round outer cloud {OORT_BAND_SENTENCE};<br>"
    f"this sphere is drawn at {_OORT_HILLS_EDGE} AU, the far end."
)
_OORT_OUTER_EDGE = row_text('OUTER_OORT_CLOUD_AU', grouping=True)
_HELIOPAUSE = row_text('HELIOPAUSE_AU')
_TERMINATION_SHOCK = row_text('TERMINATION_SHOCK_AU')
# Tony's approved notes for the two ranged edges, 2026-10-03.
OORT_INNER_EDGE_NOTE = (
    f"Thought to lie between "
    f"{row_text('OORT_CLOUD_INNER_EDGE_LOW_AU', grouping=True)} and "
    f"{row_text('OORT_CLOUD_INNER_EDGE_HIGH_AU', grouping=True)} AU; "
    f"drawn at {_OORT_INNER_EDGE}."
)
OORT_OUTER_EDGE_NOTE = (
    f"Thought to lie between "
    f"{row_text('OORT_CLOUD_OUTER_EDGE_LOW_AU', grouping=True)} and "
    f"{row_text('OORT_CLOUD_OUTER_EDGE_HIGH_AU', grouping=True)} AU; "
    f"drawn at {_OORT_OUTER_EDGE}."
)

# Source: GRAVITATIONAL_INFLUENCE_PC in constants_new.py -- the Sun's
# Source+: Hill radius in the galaxy, Portegies Zwart et al. (2021). The
# Source+: AU and light-year figures are computed from it and printed at
# Source+: its two figures. Words: Tony's approved note of 2026-10-03.
GRAVITATIONAL_INFLUENCE_SENTENCE = (
    "The Sun's Hill radius in the galaxy, calculated where the galaxy's<br>"
    "tidal pull overtakes the Sun's gravity: about "
    f"{row_text('GRAVITATIONAL_INFLUENCE_PC')} parsecs<br>"
    f"({row_text('GRAVITATIONAL_INFLUENCE_PC', 'au', grouping=True)} AU, "
    f"about {format_prints(GRAVITATIONAL_INFLUENCE_AU / AU_PER_LIGHT_YEAR, figures_of('GRAVITATIONAL_INFLUENCE_PC'))} "
    "light-years). Calculated, not measured."
)

# Source: Carroll & Ostlie, An Introduction to Modern Astrophysics, Ch. 11
# Source+: -- the ~2000 km physical extent above the photosphere, carried
# Source+: by CHROMOSPHERE_PHYSICAL_KM in constants_new.py; the radius
# Source+: prints through conversion_text(), at the count the top of the
# Source+: chromosphere, CHROMOSPHERE_TOP_KM, gives it in solar radii. The shell draws at TRUE SCALE as of
# Source+: 2026-08-16; the 1.1 stylization is retired (L-180 dormant).
CHROMOSPHERE_RADIUS_LINE = (
    f"* Radius: drawn at true scale, "
    f"{conversion_text('CHROMOSPHERE_PHYSICAL_RADII')} solar radii<br>"
    f"  ({row_text('SUN_RADIUS_KM', 'au')} to {row_text('CHROMOSPHERE_TOP_KM', 'au')} AU).<br>"
    f"  The chromosphere is a skin about {row_text('CHROMOSPHERE_PHYSICAL_KM', grouping=True)} km deep on a star "
    f"{exact_text('SUN_RADIUS_KM', grouping=True)} km in radius --<br>"
    f"  roughly {format_prints(100.0 * CHROMOSPHERE_PHYSICAL_KM / SUN_RADIUS_KM, figures_of('CHROMOSPHERE_PHYSICAL_KM'))}% of the solar radius. At any scale that "
    f"also shows the corona<br>"
    f"  it is too thin to resolve, which is why this shell appears welded to the<br>"
    f"  photosphere.<br>"
)

# L-411 (2026-10-17): Sedna's farthest distance, printed from the orbit
# the orrery fetched rather than typed (it was a typed 936 AU). Its orbit
# is taken around the solar system's barycentre, the centre its period is
# fetched around (horizons-orbital-mechanics, A Period Depends on Its
# Centre); around the Sun the elements swing with the Sun's own wobble
# (Sun-centred, its farthest point read 884 AU for JPL's 2018 solution
# and 1,004 AU on 2026-10-10). The distance is a(1 + e) from the period
# record's elements in data/osculating_cache.json; its error is a's,
# carried from the period's own error by Kepler's third law, a going as
# the period to the two-thirds, and it prints by the Report test
# (orbital_period.format_by_error). With no barycentric record the
# hover names Sedna's orbit and gives no number.
# Source: JPL Horizons, Sedna's osculating elements around the solar
# Source+: system barycentre (@0), saved by the period fetch.
def _sedna_farthest():
    try:
        from orbital_period import _load_cache_quietly, format_by_error
        rec = (_load_cache_quietly().get('Sedna') or {}).get('period') or {}
        el = rec.get('elements') or {}
        if rec.get('center') != '@0':
            return ''
        a, e = float(el['a']), float(el['e'])
        err_a = (2.0 / 3.0) * a * float(rec['error_days']) / float(rec['days'])
        far = format_by_error(a * (1.0 + e), err_a * (1.0 + e))
        return (', which reaches about %s AU<br>from the solar system\'s center of mass '
                '(JPL Horizons, %s)' % (far, rec.get('fetched', '')))
    except Exception:
        return ''


_SEDNA_FARTHEST = _sedna_farthest()

# Source: GRAVITATIONAL_INFLUENCE_SENTENCE above (derived); NASA Solar
# Source+: System Exploration for the heliopause and Oort Cloud framing.
# Source+: NASA Solar System Exploration; constants_new.py pinned values (HELIOPAUSE_RADII, TERMINATION_SHOCK_AU,
# Source+: OUTER_CORONA_RADII, INNER_CORONA_RADII, CHROMOSPHERE_PHYSICAL_RADII, GRAVITATIONAL_INFLUENCE_AU, Oort Cloud AU constants);
# Source+: Dones et al. (2004) Comets II; Golub & Pasachoff (2010) The Solar Corona; NASA solar interior model
# Note: the lines above came from gravitational_influence_info_hover, the plot
# Note+: hover's copy, deleted 2026-10-21 (L-191).
gravitational_influence_info = (
            "Sun: Outer Limit of Gravitational Influence:\n\n" 

            f"The Solar System\'s extent is actually defined in multiple ways. The Heliopause ({_HELIOPAUSE} AU):\n" 
            "Where the solar wind meets interstellar space.\n\n" 

            f"Gravitational influence extends much further, including Sedna\'s orbit{_SEDNA_FARTHEST}, the Hills Cloud/Inner\n" 
            f"Oort Cloud (from {_OORT_INNER_EDGE} AU), and the Outer Oort Cloud (to {_OORT_OUTER_EDGE} AU), one giving way to the\n" 
            f"other {OORT_BAND_SENTENCE}.\n\n" 
            + GRAVITATIONAL_INFLUENCE_SENTENCE + "\n\n"
            
            "While the Heliopause marks where the Sun\'s particle influence ends, its gravitational influence extends much\n" 
            "further. Sedna and other distant objects remain gravitationally bound to the Sun despite being well beyond\n" 
            "the Heliopause. This is why astronomers generally consider the Oort Cloud (and objects like Sedna) to be part\n" 
            "of our Solar System, even though we've never directly observed the Oort Cloud. The distinction comes down to\n" 
            "different types of influence:\n" 
            "* Particle/plasma influence (solar wind) [OK] ends at Heliopause;\n" 
            "* gravitational influence [OK] extends much further, including Sedna and the theoretical Oort Cloud.\n\n" 
            
            "So the Solar System is generally considered to extend at least as far as these gravitationally bound objects,\n" 
            "even beyond the Heliopause. Sedna is one of our first glimpses into this very distant region that may connect\n" 
            "to the Oort Cloud population."
        )

# Source: Dones et al. (2004); OUTER_OORT_CLOUD_AU=100000 in constants_new.py
outer_oort_info = (
            "Oort Cloud: Outer Limit of Outer Oort Cloud:\n\n"
            
            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            f"Solar System at distances ranging from approximately {_OORT_INNER_EDGE} AU to {_OORT_OUTER_EDGE} AU from the Sun.\n\n"

            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            "Oort Cloud's Outer Edge:\n" 
            f"{OORT_OUTER_EDGE_NOTE}\n" 
            f"At {_OORT_OUTER_EDGE} AU it is about {format_prints(OUTER_OORT_CLOUD_AU / AU_PER_LIGHT_YEAR, 1)} light-years from the Sun, marking the boundary\n" 
            "between the Solar System and interstellar space.\n\n" 

            "The Outer Oort Cloud is the primary source of long-period comets. Objects here are more loosely bound and more\n" 
            "susceptible to external gravitational perturbations."
        )

# Source: INNER_OORT_CLOUD_AU (Portegies Zwart et al. 2021) and
# Source+: INNER_OORT_DISK_OUTER_AU (Nesvorny et al. 2025) in constants_new.py,
# Source+: the band's two ends; the comment here named Hills (1981), which
# Source+: does not print the number (corrected L-421, 2026-10-10, as L-371
# Source+: corrected the row).
inner_oort_info = (
            "Oort Cloud: Outer Limit of Inner Oort Cloud:\n\n"
            f"{INNER_OORT_BAND_NOTE}\n\n"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            f"Solar System at distances ranging from approximately {_OORT_INNER_EDGE} AU to {_OORT_OUTER_EDGE} AU from the Sun.\n" 
            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            f"Inner Oort Cloud (Hills Cloud): Extends from about {_OORT_INNER_EDGE} AU and gives way to the round outer cloud\n" 
            f"{OORT_BAND_SENTENCE}. More tightly bound to the\n" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an\n" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

# Source: Dones et al. (2004); INNER_LIMIT_OORT_CLOUD_AU=2000 in constants_new.py
inner_limit_oort_info = (
            "Oort Cloud: Inner Limit:\n\n"
            f"{OORT_INNER_EDGE_NOTE}\n\n"

            "The Oort Cloud is a theoretical, vast, spherical shell of icy objects that surrounds the\n" 
            f"Solar System at distances ranging from approximately {_OORT_INNER_EDGE} AU to {_OORT_OUTER_EDGE} AU from the Sun.\n" 
            "Predominantly composed of cometary nuclei-small, icy bodies made of water ice, ammonia, and methane.\n" 
            "Believed to be the source of long-period comets that enter the inner Solar System with orbital\n" 
            "periods exceeding 200 years.\n\n" 

            f"Inner Oort Cloud (Hills Cloud): Extends from about {_OORT_INNER_EDGE} AU and gives way to the round outer cloud\n" 
            f"{OORT_BAND_SENTENCE}. More tightly bound to the\n" 
            "Sun. More tightly bound to the Solar System compared to the outer Oort Cloud. It serves as an\n" 
            "intermediate zone between the Kuiper Belt and the outer Oort Cloud."
        )

# Source: Nesvorny, D., Dones, L., Vokrouhlicky, D., Levison, H. F., Beauge, C.,
# Source+: Faherty, J., Emmart, C. and Parker, J. P. (2025), "A Spiral Structure
# Source+: in the Inner Oort Cloud", arXiv:2502.11252v1 -- sec. 1, p. 1 (inferred
# Source+: from long-period comets), p. 2 (more strongly bound; long portrayed
# Source+: as a flat disk along the ecliptic, Levison et al. 2001), p. 3 (a
# Source+: slightly warped disk inclined about 30 deg to the ecliptic, nearly
# Source+: polar to the galaxy, a spiral with two twisted arms); sec. 2,
# Source+: pp. 3-4 (shaped by the Galactic tide, persisting over billions of
# Source+: years); sec. 5, p. 12 (indirectly detected). The distances and the
# Source+: tilt print from INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_DISK_OUTER_AU,
# Source+: INNER_OORT_CLOUD_AU and HILLS_CLOUD_TILT_DEG, each sourced on its row.
# Words: Tony's confirmed hover, panel and note, 2026-10-09 (design record
# Words+: sections 4, 5 and 9), in the orrery's convention: the citation sits
# Words+: here. Replaces the "Hills Cloud Torus" text, its doughnut shape and
# Words+: its uncited list (L-421, 2026-10-10).
hills_cloud_torus_info = (
            "Oort Cloud: Hills Cloud (tilted disk):<br><br>"

            "The inner part of the Oort cloud: icy bodies far beyond the planets,<br>"
            "gathered in a slightly warped disk.<br><br>"

            f"From {_OORT_INNER_EDGE} AU to {_OORT_DISK_EDGE} AU, thinning out by {_OORT_HILLS_EDGE} AU.<br><br>"

            "The Oort cloud is a vast swarm of icy bodies surrounding the solar system, the source<br>"
            "of the long-period comets. Its inner part, the Hills cloud, is more tightly bound to the<br>"
            "Sun. It was long pictured as a fairly flat disk lying along the ecliptic. A 2025 computer<br>"
            f"model finds instead a slightly warped disk tilted about {_HILLS_TILT} degrees to the ecliptic,<br>"
            "nearly at right angles to the plane of the Milky Way. Seen from far away it would look<br>"
            "like a spiral with two twisted arms. The Milky Way's tide shapes it over billions of<br>"
            "years. No one has seen it directly; its shape shows only indirectly, in the orbits of<br>"
            "some long-period comets.<br><br>"

            "Drawn as dots along orbits picked where the model's orbits lie (its Fig. 3), so the<br>"
            "tilt and the two arms come out of the orbits. How stretched the orbits are is chosen<br>"
            f"for the picture: the model shows it only as a plot. The dots thin out between<br>"
            f"{_OORT_DISK_EDGE} and {_OORT_HILLS_EDGE} AU.<br><br>"

            "Nesvorny, D., et al. (2025), A Spiral Structure in the Inner Oort Cloud,<br>"
            "arXiv:2502.11252."
        )

# Source: Dones et al. (2004); OUTER_OORT_CLOUD_AU=100000 in constants_new.py
outer_oort_clumpy_info = (
            "Oort Cloud: Clumpy Oort Cloud:<br><br>"

            "Reflects N-body simulations showing stellar encounters create density variations.<br>"

            "Structure:<br>" 
            f"* Hills Cloud (Inner Oort): from {_OORT_INNER_EDGE} AU, a disk tilted about {_HILLS_TILT} degrees to the ecliptic<br>"
            f"* Outer Oort Cloud: to {_OORT_OUTER_EDGE}+ AU, roughly spherical but clumpy<br>" 
            f"* The two give way to each other {OORT_BAND_SENTENCE}<br>" 
            "Key Characteristics:<br>" 
            "* Not uniform shells but complex, structured regions<br>" 
            "* Density varies significantly throughout<br>" 
            "* Influenced by galactic tides and stellar encounters<br>" 
            "* Contains an estimated 1-100 trillion objects >1km<br><br>" 
            "Scientific Evidence:<br>" 
            "* Comet orbital inclinations suggest spherical outer region<br>" 
            "* Short-period comet inclinations suggest disk-like inner region<br>" 
            "* Computer simulations show tidal sculpting effects<br>" 
            "* Stellar encounter models predict clumpy structure<br>" 
            "Recent Discoveries:<br>" 
            "* Objects like Sedna may be inner Oort Cloud members<br>" 
            "* 2012 VP113 provides evidence for inner Oort population<br>" 
            "* NEOWISE survey improving population estimates"
        )

# Source: Dones et al. (2004) Comets II -- galactic tidal sculpting of Oort Cloud.
# Note: this string states no gravitational-influence figure; the previous
#       citation asserted a gravitational-influence value of 126,000 AU
#       here, which was both wrong and irrelevant to the text below
#       (removed L-179).
galactic_tide_info = (
            "Oort Cloud: Galactic Tide Influenced Oort:<br><br>"

            "Shows how the Milky Way's gravity creates asymmetries.<br>"

            "Structure:<br>" 
            f"* Hills Cloud (Inner Oort): from {_OORT_INNER_EDGE} AU, a disk tilted about {_HILLS_TILT} degrees to the ecliptic<br>"
            f"* Outer Oort Cloud: to {_OORT_OUTER_EDGE}+ AU, roughly spherical but clumpy<br>" 
            f"* The two give way to each other {OORT_BAND_SENTENCE}<br>" 
            "Key Characteristics:<br>" 
            "* Not uniform shells but complex, structured regions<br>" 
            "* Density varies significantly throughout<br>" 
            "* Influenced by galactic tides and stellar encounters<br>" 
            "* Contains an estimated 1-100 trillion objects >1km<br><br>" 
            "Scientific Evidence:<br>" 
            "* Comet orbital inclinations suggest spherical outer region<br>" 
            "* Short-period comet inclinations suggest disk-like inner region<br>" 
            "* Computer simulations show tidal sculpting effects<br>" 
            "* Stellar encounter models predict clumpy structure<br>" 
            "Recent Discoveries:<br>" 
            "* Objects like Sedna may be inner Oort Cloud members<br>" 
            "* 2012 VP113 provides evidence for inner Oort population<br>" 
            "* NEOWISE survey improving population estimates"
        )

# Source: NASA Heliophysics / Ulysses mission; solar wind speed 400-800 km/s from multiple spacecraft
solar_wind_info = (
            "Solar Wind: Heliopause:\n\n"

            "The heliosphere is a vast, bubble-like region of space that surrounds the Sun and its planets. It's created by the\n" 
            "solar wind, a constant stream of charged particles flowing out from the Sun.\n" 
            "* Solar Wind: The solar wind is the driving force behind the heliosphere. It consists mostly of protons and electrons,\n" 
            "  along with heavier elements in smaller numbers. These particles are accelerated to high speeds by the Sun's heat and\n" 
            "  then escape its gravity, flowing out into space.\n" 
            "* Shape: The heliosphere isn't perfectly spherical. It's more like a long, teardrop shape with a rounded head and a\n" 
            "  flowing tail. This shape is due to the Sun's movement through the interstellar medium, the gas and dust that fills the\n" 
            "  space between stars.\n\n" 
            
            "Boundaries: The heliosphere has a few distinct boundaries:\n" 
            "* Termination Shock: This is where the solar wind abruptly slows down as it encounters the interstellar medium.\n" 
            "* Heliosheath: This is the turbulent region beyond the termination shock, where the solar wind mixes with the interstellar medium.\n" 
            "* Heliopause: This is the outermost boundary of the heliosphere, where the solar wind's pressure is balanced by the pressure of\n" 
            "  the interstellar medium. It's considered the true \"edge\" of our solar system.\n" 
            "* Protective Shield: The heliosphere acts as a protective bubble, shielding the planets within it from harmful galactic cosmic\n" 
            "  radiation. This radiation comes from outside our solar system and can be dangerous to life.\n" 
            "* Influence on Planets: The heliosphere also influences the planets within it. It interacts with planetary magnetic fields,\n" 
            "  creating phenomena like auroras. It can also affect the atmospheres of planets without strong magnetic fields.\n\n"   
                         
            "Voyager Missions: Our most valuable information about the heliosheath comes from the Voyager 1 and Voyager 2 spacecraft,\n" 
            "which have been traveling through space since 1977. Both probes crossed the termination shock and then the heliopause,\n" 
            "and both are now in interstellar space: Voyager 1 in 2012 (Gurnett et al. 2013), Voyager 2 in 2018 (NASA). Voyager 1 encountered the Heliopause\n" 
            f"at {_HELIOPAUSE} AU. This is considered the end of the Sun's influence and the start of interstellar space.\n\n" 
            
            f"* The heliosheath lies between the termination shock ({_TERMINATION_SHOCK} AU) and the heliopause\n"
            f"  ({_HELIOPAUSE} AU), on Voyager 1's path.\n"
            "* Temperature: ~1,000,000K on average.\n"
            "* Black body radiation at 2.897 nm falls within the X-ray region of the electromagnetic spectrum, which is invisible to the human eye."
        )

# Source: Stone et al. (2005), Science 309:2017 -- Voyager 1's crossing;
# Source+: NASA SVS 20132 (2008) -- Voyager 2's; Treumann and Jaroschek,
# Source+: arXiv:0807.4170 -- the 80-100 AU range; Li, Wang and Richardson
# Source+: (2008), GRL 35:L19107 -- Voyager 2's speeds. All print from
# Source+: their rows in constants_new.py (L-411).
termination_shock_info = (
            "Solar Wind: Termination Shock:\n\n"

            f"The Solar Wind Termination Shock lies about {row_text('TERMINATION_SHOCK_RANGE_LOW_AU')} to {row_text('TERMINATION_SHOCK_RANGE_HIGH_AU')} AU from the Sun (Treumann and Jaroschek 2008).\n\n"

            "The Termination Shock is the region where the solar wind slows down from\n"
            "supersonic to subsonic speeds due to interaction with the interstellar\n"
            "medium. The kinetic energy transfers into heat, increasing abruptly.\n\n"

            f"Voyager 1 encountered the Termination Shock at {_TERMINATION_SHOCK} AU, and Voyager 2 at about {row_text('VOYAGER2_TERMINATION_SHOCK_AU')} AU (Li et al. 2008).\n"
            f"Voyager 2 measured the wind slowing from about {row_text('VOYAGER2_TS_UPSTREAM_SPEED_KM_S')} to about {row_text('VOYAGER2_TS_DOWNSTREAM_SPEED_KM_S')} km/s as it crossed (Li et al. 2008)."
        )

# outer_corona_info was DELETED 2026-10-19 (L-410), with its checkbox.

# inner_corona_info was DELETED 2026-10-19 (L-410), with its checkbox.

# Source: constants_new.py CHROMOSPHERE_PHYSICAL_KM = 2000 (physical extent,
# Source+: Carroll & Ostlie Ch. 11, ~1.003 R_sun, and since 2026-08-16 the
# Source+: drawn radius as well); Golub & Pasachoff (2010) The Solar Corona.
# Note: two earlier drawn radii are retired. 1.5 solar radii has not been
#       held since 2026-08-02; the 1.1 stylization was retired 2026-08-16
#       when the shell moved to true scale.
# Source+: NASA solar interior model; Golub & Pasachoff (2010) The Solar Corona;
# Source+: Bahcall et al. standard solar model; SUN_RADIUS_KM=695700 in constants_new.py
# Note: the lines above came from chromosphere_info_hover, the plot
# Note+: hover's copy, deleted 2026-10-21 (L-191).
chromosphere_info = (
            "Sun: Chromosphere:\n\n"

            "The chromosphere is a dynamic and visually stunning layer of the Sun's atmosphere, sandwiched between the\n" 
            "photosphere (the visible surface) and the corona (the outermost layer). It's a region of dramatic temperature\n" 
            "changes, intricate structures, and energetic events.\n\n"
             
            "* The chromosphere is relatively thin, extending only about 2,000 kilometers (1,200 miles) above the photosphere.\n" 
            "  It's also much less dense than the photosphere.\n" 
            "* The temperature in the chromosphere increases dramatically with altitude, from around 4,000 Kelvin at the\n" 
            "  photosphere to about 20,000 Kelvin at the inner corona.\n" 
            "* The chromosphere gets its name from the Greek word \"chroma,\" meaning color, because of its reddish appearance.\n" 
            "  This color is primarily due to the strong emission of light from hydrogen atoms\n" 
            "* The chromosphere is a constantly changing environment, with a variety of features that evolve and erupt on\n" 
            "  different timescales:\n" 
            "  * Spicules: These are jet-like eruptions of plasma that rise and fall like geysers, covering the chromosphere\n" 
            "    in a dynamic, \"grass-like\" pattern.\n" 
            "  * Filaments and prominences: These are large, cool, dense structures of plasma suspended in the chromosphere\n" 
            "    and corona by magnetic fields. When seen against the bright disk of the Sun, they appear as dark filaments.\n" 
            "    When seen extending beyond the Sun's edge, they appear as bright prominences.\n" 
            "  * Plages: These are bright regions in the chromosphere associated with active regions, where magnetic fields\n" 
            "    are concentrated.\n\n" 
             
            + CHROMOSPHERE_RADIUS_LINE +
            "* Temperature: ~6,000 to 20,000 K, for a average of 10,000 K\n"
            "* Radiates at an average peak wavelength of ~290 nm, ultraviolet range, invisible."
        )

# Source: NASA Solar System Exploration (solarsystem.nasa.gov/solar-system/sun); SUN_RADIUS_KM=695700 in constants_new.py
photosphere_info = (
            "Sun: Photosphere\n\n"

            "Solar Convective Zone and Photosphere, the visible surface.\n"
            f"* The photosphere is the visible surface of the Sun. It's a relatively thin layer, only about {row_text('PHOTOSPHERE_THICKNESS_KM')} kilometers thick.\n" 
            f"* Including both the Convective Zone and the Photosphere, the radius is from {row_text('RADIATIVE_ZONE_RADII')} to 1 solar radius, or about {row_text('SUN_RADIUS_KM', 'au')} AU.\n"
            "* Temperature: from 2M K at the Radiative Zone to ~5,500K at the Photosphere.\n"
            "* Convection transports energy to the visible \"surface\" of the Sun. The convection process starts at the Radiative Zone\n"
            "* At the Photosphere, the energy is radiated as visible light. Radiation emits at a peak wavelength at 527.32 nm, which\n" 
            "  is in the green spectrum. The Sun's emitted light is a combination of all visible wavelengths, resulting in a yellowish-white color.\n\n"
             
            "* The photosphere is cooler than the Sun's core and the layers above it, but still hot enough to make the photosphere glow brightly.\n" 
            "* To the naked eye, the photosphere appears as a smooth, yellow disk. However, closer observations reveal a variety of features, including:\n" 
            "  * Granulation: This is a pattern of small, bright cells surrounded by darker boundaries, caused by convection\n" 
            "    currents bringing hot plasma up from the Sun's interior.\n" 
            "  * Sunspots: These are dark, cooler regions on the photosphere caused by strong magnetic fields. They can be\n" 
            "    larger than Earth and last for days or weeks.\n" 
            "  * Faculae: These are bright regions surrounding sunspots, also associated with magnetic fields.\n" 
            "  * Energy transport: The photosphere is where the Sun's energy, generated in its core through nuclear fusion,\n" 
            "    is finally released as light. This energy has traveled outward through the Sun's interior in the form of\n" 
            "    radiation and convection, and it's in the photosphere that it transitions to primarily radiation, allowing it\n" 
            "    to escape into space.\n" 
            "  * Spectrum: The photosphere emits a continuous spectrum of light, which includes all colors of the rainbow.\n" 
            "  * Solar activity: The photosphere is also where many solar activity events originate, such as:\n" 
            "    * Solar flares: These are sudden, intense bursts of energy and radiation caused by the release of magnetic\n" 
            "      energy in the solar atmosphere.\n" 
            "    * Coronal mass ejections (CMEs): These are massive eruptions of plasma and magnetic field from the Sun's corona,\n" 
            "      often associated with flares.\n"
            "    * Solar activity events originating in the photosphere can affect Earth's magnetic field and disrupt satellites,\n" 
            "      communication systems, and power grids.\n\n"
        )

# Source: NASA Solar Interior model; constants_new.py RADIATIVE_ZONE_AU=0.7*SOLAR_RADIUS_AU
# Source+: Bahcall et al. standard solar model; NASA solar interior;
# Source+: CORE_AU=0.2*SOLAR_RADIUS_AU, RADIATIVE_ZONE_AU=0.7*SOLAR_RADIUS_AU in constants_new.py
# Note: the lines above came from radiative_zone_info_hover, the plot
# Note+: hover's copy, deleted 2026-10-21 (L-191).
radiative_zone_info = (
            "Sun: Radiative Zone\n\n"

            f"The Solar Radiative Zone extends from about {row_text('CORE_RADII')} to {row_text('RADIATIVE_ZONE_RADII')} solar radii, about {row_text('RADIATIVE_ZONE_RADII', 'au')} AU. Temperature ranges from about\n" 
            "7M K near the core to about 2M K near the convective zone. Energy is transported by radiative diffusion, through photon\n" 
            "absorption and re-emission.\n\n"

            "The radiative zone is a vast region within the Sun, located between the core and the convective zone. It's a place\n" 
            "of intense heat and density, where energy generated in the core slowly makes its way outward in the form of photons.\n"  
            "* Density: The density also decreases with distance from the core, but it remains much denser than the convective zone above it.\n\n" 
            "* Energy transport: The primary mode of energy transport in the radiative zone is radiative diffusion. Photons\n" 
            "  generated in the core through nuclear fusion undergo countless absorptions and re-emissions as they interact\n" 
            "  with the dense plasma. This process is incredibly slow, and it can take millions of years for a photon to travel\n" 
            "  from the core to the outer edge of the radiative zone.\n" 
            "* Opacity: The radiative zone is highly opaque, meaning that photons can only travel a short distance before being\n" 
            "  absorbed or scattered. This high opacity is due to the high density and the presence of heavy elements, which are\n" 
            "  more efficient at absorbing and scattering radiation.\n" 
            "* Energy transfer: The radiative zone plays a crucial role in transferring energy from the Sun's core to its outer\n" 
            "  layers. Without it, the Sun would not be able to shine.\n" 
            "* Stability: The slow and gradual energy transport in the radiative zone helps to maintain the Sun's overall stability.\n" 
            "* Helioseismology: This technique uses observations of sound waves traveling through the Sun to probe its interior\n" 
            "  structure, including the radiative zone. By analyzing the frequencies and patterns of these waves, scientists can\n" 
            "  infer the temperature, density, and composition of the radiative zone.\n" 
            "* Neutrino observations: Neutrinos are subatomic particles produced in the Sun's core that can pass through the\n" 
            "  radiative zone almost unimpeded. By detecting and analyzing these neutrinos, scientists can gain information about\n" 
            "  the nuclear reactions taking place in the core and the conditions in the radiative zone."
            )

# Source: NASA Solar Interior (nasa.gov/sun/facts); Bahcall et al. standard solar model
core_info = (
            "Sun: Solar Core\n\n"

            "The Sun's core is where the Sun's energy is generated through nuclear fusion, providing the light and heat that sustain life on Earth:\n" 
            "* Location: The core is located at the very center of the Sun, extending outward to about 25% of the Sun's radius.\n" 
            "* Size: While relatively small compared to the Sun's overall size, the core contains about 34% of the Sun's total mass.\n" 
            "* Temperature: The core is the hottest place in the solar system, with temperatures reaching 15 million Kelvin\n" 
            "* Density: The core is incredibly dense, about 150 times denser than water. This extreme density is due to the\n" 
            "  immense pressure exerted by the Sun's outer layers.\n" 
            "* Composition: The core is primarily composed of hydrogen (about 34% by mass) and helium (about 64% by mass).\n" 
            "  Trace amounts of heavier elements are also present.\n\n"
              
            "The dominant fusion process in the Sun's core is the proton-proton chain reaction:\n" 
            "* Two protons, hydrogen nuclei, collide and fuse to form a deuterium nucleus releasing a positron and a neutrino.\n" 
            "* The deuterium nucleus collides with another proton to form a helium-3 nucleus, releasing a gamma ray.\n" 
            "* Two helium-3 nuclei collide to form a helium-4 nucleus, releasing two protons.\n" 
            "* This process converts a small amount of mass into a tremendous amount of energy\n\n" 
            
            "The energy generated in the core is transported outward through the Sun in two ways:\n"
            "* Radiative zone: The energy first travels through the radiative zone, where it is carried by photons that undergo\n" 
            "  countless absorptions and re-emissions. This process is very slow, taking millions of years for energy to travel\n" 
            "  from the core to the outer edge of the radiative zone.\n" 
            "* Convective zone: Once the energy reaches the convective zone, it is transported by convection currents, where hot\n" 
            "  plasma rises and cooler plasma sinks. This is a much faster process, taking only a few weeks for energy to reach\n" 
            "  the Sun's surface.\n\n" 
            
            "* Helioseismology: By analyzing sound waves traveling through the Sun, scientists can infer the conditions in the core,\n" 
            "  such as its temperature, density, and composition.\n" 
            "* Neutrino observations: Neutrinos produced in the core can pass through the Sun almost unimpeded, providing direct\n" 
            "  information about the nuclear reactions taking place there." 
            )

# outer_corona_info_hover was DELETED 2026-10-19 (L-410), with its sphere;
# the corona's words are corona_info, below (one string
# since 2026-10-21, L-191).

# streamer_belt_info was DELETED 2026-10-19 (L-410): the streamer belt
# has no checkbox of its own now. It is drawn with the corona, under the
# one "-- Corona" checkbox, whose tooltip is corona_info; the band keeps
# its own hover in create_sun_streamer_band.

# streamer_belt_info_hover was DELETED 2026-08-22 (L-224). It fed only
# create_sun_streamer_belt_shell, which was dead code; the live band
# builder composes its own hover from the constants. Deleted rather than
# annotated: it demonstrates the sphere pattern this item exists to
# retire, and a worked example of the wrong shape one screen from the
# right one is a trap, not a reference.

# Source: constants_new.py ROCHE_LIMIT_RADII=3.45 (Ida et al. 2020); Ikeya-Seki survived at 1.66 R_sun (tensile strength)
roche_limit_info = (
    "Sun: Roche Limit (Fluid Body / Comet):\n\n"

    "The Roche limit is the distance within which a fluid body held together only by\n"
    "self-gravity will be torn apart by the Sun's tidal forces.\n\n"

    "Formula: d = 2.44 x R_sun x (rho_sun / rho_comet)^(1/3)\n"
    "Solar density: 1,408 kg/m^3 | Comet density: ~500 kg/m^3\n"
    f"Result: about {row_text('ROCHE_LIMIT_RADII')} solar radii, about {row_text('ROCHE_LIMIT_RADII', 'km', grouping=True)} km from the Sun's center\n"
    f"  ({row_text('ROCHE_LIMIT_RADII', 'au')} AU). The comet density is known to one figure, so the result is too.\n\n"

    "Key physics:\n"
    "* The Roche limit is NOT absolute. It marks where tidal forces overcome SELF-GRAVITY\n"
    "  only. Tensile strength -- the material bonds holding the nucleus together -- can\n"
    "  allow survival well inside the formal Roche limit.\n"
    "* Ikeya-Seki (C/1965 S1, ~5 km nucleus) survived at 1.66 R_sun (0.008 AU).\n"
    "* Great Comet of 1843 survived at 1.19 R_sun (0.006 AU) -- deepest ever recorded.\n"
    "* Comet Lovejoy (C/2011 W3, ~500 m) survived perihelion briefly at ~1.2 R_sun.\n"
    "* Size and structural coherence are decisive: larger nuclei have both stronger\n"
    "  self-gravity AND stronger material bonds to resist tidal disruption.\n\n"

    "MAPS C/2026 A1 context:\n"
    "* MAPS disintegrated at ~8.33 R_sun (0.039 AU) -- OUTSIDE the Roche limit.\n"
    "* Primary destruction mechanisms: thermal ablation (1-2 million K corona) and\n"
    "  rotational spin-up from outgassing jets. Tidal forces never acted on MAPS.\n"
    f"* The debris swept THROUGH the Roche limit (about {row_text('ROCHE_LIMIT_RADII')} R_sun, {row_text('ROCHE_LIMIT_RADII', 'au')} AU) to perihelion\n"
    "  at 1.23 R_sun -- but the nucleus was already gone."
)

# Source: Cranmer, Chhiber, Gilly, Cairns, Colaninno, McComas, Raouafi,
# Source+: Usmanov, Gibson and DeForest (2023), "The Sun's Alfven Surface:
# Source+: Recent Insights and Prospects for the Polarimeter to Unify the
# Source+: Corona and Heliosphere (PUNCH)" -- abstract, the surface's usual
# Source+: range; sec. 3.1, its shape in global models.
# Source+: https://arxiv.org/abs/2310.05887
# Note: the Alfven surface's radius is ALFVEN_SURFACE_RADII and its usual
# Note+: range the two ALFVEN_SURFACE_RANGE_ rows, all in constants_new.py
# Note+: and printed from there (L-209, L-228).
# Corrected: 2026-10-17 (L-228) -- cited Cranmer et al. (2007) until now.
# Corrected+: The polar and streamer-belt ranges it was cited for are not
# Corrected+: in that paper's text as far as its Section 8, and the 2023
# Corrected+: review puts the surface's maxima over the polar holes, the
# Corrected+: other way round; they are removed.
alfven_surface_info = (
    "Sun: Alfven Surface:\n\n"

    "The Alfven surface is the true outer boundary of the solar corona -- the point where\n"
    "the solar wind accelerates past the local Alfven speed and plasma can no longer\n"
    "communicate back to the Sun. Beyond it, the corona becomes the solar wind.\n\n"

    f"* Location: most of the time between about {row_text('ALFVEN_SURFACE_RANGE_LOW_RADII')} and {row_text('ALFVEN_SURFACE_RANGE_HIGH_RADII')} solar radii\n"
    "  from the Sun's center (Cranmer et al. 2023).\n"
    f"  On April 28, 2021, Parker Solar Probe crossed inward at {ALFVEN_SURFACE_RADII} R_sun "
    f"({ALFVEN_SURFACE_RADII * SUN_RADIUS_KM / 1e6:.1f} million km from Sun center),\n"
    "  spending ~5 hours inside the corona -- the first spacecraft to 'touch the Sun.'\n"
    "* This is not a smooth sphere: it has spikes and valleys shaped by solar magnetic activity.\n"
    "  Computer models of the corona often put it farthest out above the large polar\n"
    "  coronal holes and closest in at the tops of the helmet streamers (Cranmer et al. 2023).\n\n"

    "Why it matters:\n"
    "* Inside the Alfven surface: plasma is magnetically connected to the Sun.\n"
    "  Perturbations (like a passing comet) can propagate back to the solar surface.\n"
    "* Outside it: plasma becomes the solar wind, causally disconnected from the Sun.\n"
    "* This boundary governs the Sun's angular momentum loss and spin-down over time.\n\n"

    "MAPS C/2026 A1 context:\n"
    "* MAPS crossed the Alfven surface approximately April 3, ~18:00 UTC --\n"
    "  about 20 hours before its nucleus disintegrated.\n"
    "* Inside this boundary, the comet was immersed in magnetically connected coronal plasma\n"
    "  at temperatures of 1-2 million K, subject to intense tidal and thermal stresses.\n"
    "* The corona it entered here is physically different from the visible outer corona --\n"
    "  this is where the Sun 'feels' the comet and vice versa."
)

# inner_corona_info_hover was DELETED 2026-10-19 (L-410), with its sphere;
# the corona's words are corona_info, below (one string
# since 2026-10-21, L-191).

hover_text_sun_and_corona = (
    '<b>The Sun and Its Atmosphere</b><br><br>'
    'The corona, the boundaries in it, and the dust beyond, each drawn on its own:<br>'
    '* Corona: dots from the surface to the Alfven surface, thinning with height<br>'
    f'* Roche Limit: about {row_text('ROCHE_LIMIT_RADII')} R_sun -- tidal disruption threshold for comets<br>'
    f'* Streamer Belt (Visible Corona): helmets pinch at {row_text('HELMET_CUSP_RADII')} R_sun, the stalk fades beyond<br>'
    f'* Alfven Surface: ~{ALFVEN_SURFACE_RADII} R_sun -- true corona/solar wind boundary<br>'
    '  (Parker Solar Probe first crossing: April 28, 2021)<br>'
    f'* Zodiacal Dust Cloud (F-corona): dust out to {row_text('ZODIACAL_DUST_OUTER_AU')} AU ({row_text('ZODIACAL_DUST_OUTER_AU', 'km', grouping=True)} km),<br>'
    '  flattened toward the planets\' plane<br><br>'
    f'Parker Solar Probe closest approach: {row_text('PARKER_CLOSEST_KM', 'r_sun')} R_sun from the Sun\'s center, December 24, 2024 (NASA)<br><br>'
    'The coronal heating paradox: the corona is 200x hotter than the photosphere<br>'
    'despite being farther from the energy source. Leading theories: Alfven waves,<br>'
    'nanoflares, and magnetic reconnection -- still actively debated.<br><br>'
    'MAPS C/2026 A1 (April 2026) crossed each boundary in sequence:<br>'
    'Extended F-corona (April 2, ~33 R_sun, ~0.153 AU) -><br>'
    f'Alfven Surface (April 3 ~18:00, {ALFVEN_SURFACE_RADII} R_sun, {ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) -><br>'
    '<b>DISINTEGRATION (April 4 08:15, 8.33 R_sun, 0.039 AU)</b> -><br>'
    'Streamer Belt / Roche Limit / Inner K-corona: crossed by DEBRIS ONLY -><br>'
    'Perihelion (April 4 14:22, 1.23 R_sun, 0.006 AU) as a ghost.<br>'
    'Ghost tracked by SOHO/LASCO ~36-40 hours outbound; dispersed by April 6.<br>'
    f'Parker Solar Probe closest approach: {row_text('PARKER_CLOSEST_KM', 'r_sun')} R_sun ({row_text('PARKER_CLOSEST_KM', 'au')} AU) --<br>'
    'MAPS disintegrated at 8.33 R_sun (0.039 AU), closer to the Sun than Parker has flown.'
)

# Tkinter tooltip version (\n line breaks, no HTML tags)
# Item 31: hover_text_sun_and_corona uses <br>/<b> for Plotly;
# Tkinter CreateToolTip renders tags literally. This version is for GUI.
hover_text_sun_and_corona_tooltip = (
    'The Sun and Its Atmosphere<br><br>'
    'The corona, the boundaries in it, and the dust beyond, each drawn on its own:<br>'
    '* Corona: dots from the surface to the Alfven surface, thinning with height<br>'
    f'* Roche Limit: about {row_text('ROCHE_LIMIT_RADII')} R_sun -- tidal disruption threshold for comets<br>'
    f'* Streamer Belt (Visible Corona): helmets pinch at {row_text('HELMET_CUSP_RADII')} R_sun, the stalk fades beyond<br>'
    f'* Alfven Surface: ~{ALFVEN_SURFACE_RADII} R_sun -- true corona/solar wind boundary<br>'
    '  (Parker Solar Probe first crossing: April 28, 2021)<br>'
    f'* Zodiacal Dust Cloud (F-corona): dust out to {row_text('ZODIACAL_DUST_OUTER_AU')} AU ({row_text('ZODIACAL_DUST_OUTER_AU', 'km', grouping=True)} km),<br>'
    '  flattened toward the planets\' plane<br><br>'
    f'Parker Solar Probe closest approach: {row_text('PARKER_CLOSEST_KM', 'r_sun')} R_sun from the Sun\'s center, December 24, 2024 (NASA)<br><br>'
    'The coronal heating paradox: the corona is 200x hotter than the photosphere<br>'
    'despite being farther from the energy source. Leading theories: Alfven waves,<br>'
    'nanoflares, and magnetic reconnection -- still actively debated.<br><br>'
    'MAPS C/2026 A1 (April 2026) crossed each boundary in sequence:<br>'
    'Extended F-corona (April 2, ~33 R_sun, ~0.153 AU) -><br>'
    f'Alfven Surface (April 3 ~18:00, {ALFVEN_SURFACE_RADII} R_sun, {ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU:.3f} AU) -><br>'
    'DISINTEGRATION (April 4 08:15, 8.33 R_sun, 0.039 AU) -><br>'
    'Streamer Belt / Roche Limit / Inner K-corona: crossed by DEBRIS ONLY -><br>'
    'Perihelion (April 4 14:22, 1.23 R_sun, 0.006 AU) as a ghost.<br>'
    'Ghost tracked by SOHO/LASCO ~36-40 hours outbound; dispersed by April 6.<br>'
    f'Parker Solar Probe closest approach: {row_text('PARKER_CLOSEST_KM', 'r_sun')} R_sun ({row_text('PARKER_CLOSEST_KM', 'au')} AU) --<br>'
    'MAPS disintegrated at 8.33 R_sun (0.039 AU), closer to the Sun than Parker has flown.'
)

hover_text_sun = (
        '<b>Sun</b><br>'
        'Note: The Sun, our very own star, is a massive ball of hot plasma that sits at the center of our solar system.<br> ' 
        'It\'s the source of all life and energy on Earth, so I\'ve colored it chlorophyll green in our plot!<br> ' 
        '* Type: A yellow dwarf star (G-type main-sequence star).<br> ' 
        '* Age: About 4.6 billion years old, and is expected to continue its current phase for about 5 billion years<br> ' 
        'more, then evolve into a Red Giant.<br> '
        '* Diameter: Roughly 1.4 million kilometers (865,000 miles), about 109 times the diameter of Earth.<br> '
        '* Mass: About 333,000 times the mass of Earth<br> '
        '* Composition: Primarily hydrogen (about 73%) and helium (about 25%), with trace amounts of other elements.<br> '
        '* Surface Temperature: 5778 K, around 5,500 degrees Celsius, or 10,000 degrees Fahrenheit<br> '
        '* Core Temperature: Around 15 million degrees Celsius (27 million degrees Fahrenheit)<br> '
        '* Stellar Class: Main-sequence. Stars in the prime of their lives, fusing hydrogen into helium in their cores.<br> '
        '* Absolute Magnitude: 4.83<br> '
        '* Spectral Type: G2V<br> '
        '* Object Type: Star<br> '
        'The Sun is composed of several layers:<br> '
        '* Core: The innermost region where nuclear fusion occurs, converting hydrogen into helium and releasing energy.<br> '
        '* Radiative Zone: Energy from the core travels outward through this zone via radiation.<br> '
        '* Convective Zone: Energy is transported through this zone via convection (the movement of hot plasma).<br> '
        '* Photosphere: The visible surface of the Sun.<br> '
        '* Chromosphere: A thin layer above the photosphere.<br> '
        '* Corona: The outermost layer, a very hot and tenuous plasma that extends millions of kilometers into space.<br> '
        'Standard for comparison to other stars:<br> '
        '* Luminosity: 1.000000 Lsun<br> '
        '* Mass: 1.00 Msun<br> '
        '* Distance: 0 pc (0 ly)<br> '
        '* Plotting marker size: 12 px '
)


def create_sun_gravitational_shell():
    """Creates the Sun's gravitational influence shell."""
    x, y, z = create_sphere_points(GRAVITATIONAL_INFLUENCE_AU, n_points=20)
    r_info = GRAVITATIONAL_INFLUENCE_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(102, 187, 106)', opacity=0.3),
        name='Sun: Gravitational Influence',
        legendgroup='Sun: Gravitational Influence',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(102, 187, 106)',
        "Sun: Gravitational Influence<br><br>" + gravitational_influence_info.replace('\n', '<br>'),
        'Sun: Gravitational Influence'
    )
    return [shell_trace, info_trace]


def create_sun_outer_oort_shell():
    """Creates the Sun's outer Oort cloud shell."""
    x, y, z = create_sphere_points(OUTER_OORT_CLOUD_AU, n_points=20)
    r_info = OUTER_OORT_CLOUD_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='white', opacity=0.3),
        name='Sun: Outer Oort Cloud',
        legendgroup='Sun: Outer Oort Cloud',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed; size 6->8 and
    # gray border -> red (factory default; gray was inherited inline choice).
    info_trace = create_info_marker(
        0, 0, r_info,
        'white',
        "Sun: Outer Oort Cloud<br><br>" + outer_oort_info.replace('\n', '<br>'),
        'Sun: Outer Oort Cloud',
        customdata='Outer Oort Cloud'
    )
    return [shell_trace, info_trace]


def create_sun_inner_oort_shell():
    """Creates the Sun's inner Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_OORT_CLOUD_AU, n_points=20)
    r_info = INNER_OORT_CLOUD_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='white', opacity=0.35),
        name='Sun: Inner Oort Cloud',
        legendgroup='Sun: Inner Oort Cloud',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed; size 6->8 and
    # gray border -> red (factory default; gray was inherited inline choice).
    info_trace = create_info_marker(
        0, 0, r_info,
        'white',
        "Sun: Inner Oort Cloud<br><br>" + inner_oort_info.replace('\n', '<br>'),
        'Sun: Inner Oort Cloud',
        customdata='Inner Oort Cloud'
    )
    return [shell_trace, info_trace]


def create_sun_inner_oort_limit_shell():
    """Creates the inner limit of the Sun's Oort cloud shell."""
    x, y, z = create_sphere_points(INNER_LIMIT_OORT_CLOUD_AU, n_points=20)
    r_info = INNER_LIMIT_OORT_CLOUD_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='white', opacity=0.35),
        name='Sun: Inner Limit of Oort Cloud',
        legendgroup='Sun: Inner Limit of Oort Cloud',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed; size 6->8 and
    # gray border -> red (factory default; gray was inherited inline choice).
    info_trace = create_info_marker(
        0, 0, r_info,
        'white',
        "Sun: Inner Limit of Oort Cloud<br><br>" + inner_limit_oort_info.replace('\n', '<br>'),
        'Sun: Inner Limit of Oort Cloud',
        customdata='Inner Limit of Oort Cloud'
    )
    return [shell_trace, info_trace]


def create_sun_heliopause_shell():
    """Creates the Sun's heliopause shell."""
    x, y, z = create_sphere_points(HELIOPAUSE_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = HELIOPAUSE_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(135, 206, 250)', opacity=0.4),
        name='Sun: Heliopause',
        legendgroup='Sun: Heliopause',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(135, 206, 250)',
        "Sun: Heliopause<br><br>" + solar_wind_info.replace('\n', '<br>'),
        'Sun: Heliopause',
        customdata='Solar Wind Heliopause'
    )
    return [shell_trace, info_trace]


def create_sun_termination_shock_shell():
    """Creates the Sun's termination shock shell."""
    x, y, z = create_sphere_points(TERMINATION_SHOCK_AU, n_points=20)
    r_info = TERMINATION_SHOCK_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(240, 244, 255)', opacity=0.4),
        name='Sun: Termination Shock',
        legendgroup='Sun: Termination Shock',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed; size 6->8 and
    # gray border -> red (factory default).
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(240, 244, 255)',
        "Sun: Termination Shock<br><br>" + termination_shock_info.replace('\n', '<br>'),
        'Sun: Termination Shock',
        customdata='Solar Wind Termination Shock'
    )
    return [shell_trace, info_trace]


# create_sun_outer_corona_shell was DELETED 2026-10-19 (L-410): the outer
# corona sphere became part of the corona's one fade, create_sun_corona,
# and the dust whose light it was became create_sun_zodiacal_dust.


# create_sun_inner_corona_shell was DELETED 2026-10-19 (L-410): the inner
# corona sphere became part of the corona's one fade, create_sun_corona.


# create_sun_streamer_belt_shell was DELETED 2026-08-22 (L-224). It was
# defined here, imported once by planet_visualization.py, and never
# called: the sphere it drew came from SHELL_CONFIGS['Sun']
# ['streamer_belt'] via build_sphere_shell. Its replacement is
# create_sun_streamer_band below, wired through CUSTOM_SHELLS.


# Source: ROCHE_LIMIT_RADII=3.45 in constants_new.py; Ida et al. (2020);
# Source+: MAPS disintegration at 8.33 R_sun from SOHO/CCOR-1 observations April 2026
def create_sun_roche_limit_shell():
    """
    Fluid Roche limit for cometary bodies: ~3.45 solar radii (~0.016 AU).
    d = 2.44 * R_sun * (rho_sun / rho_comet)^(1/3)
    rho_sun=1408, rho_comet=500 kg/m^3.
    Inside this shell tidal forces overcome a fluid body's self-gravity --
    but tensile strength allows survival inside it (Ikeya-Seki, Great Comet of 1843).
    MAPS C/2026 A1 disintegrated at 8.33 R_sun (0.039 AU) -- OUTSIDE this shell.
    """
    x, y, z = create_sphere_points(ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(200, 60, 60)', opacity=0.5),
        name='Sun: Roche Limit (Comets)',
        legendgroup='Sun: Roche Limit (Comets)',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed with explicit
    # white border. rgb(200, 60, 60) is dense red -- under Tony's two-standards
    # convention this gets white outline so the cross reads against the fill.
    # Was a v12 "exception"; the exception has become the rule for reddish shells.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(200, 60, 60)',
        "Sun: Roche Limit (Comets)<br><br>" + roche_limit_info.replace('\n', '<br>'),
        'Sun: Roche Limit (Comets)',
        border_color='white'
    )
    return [shell_trace, info_trace]


def create_sun_alfven_surface_shell():
    """
    Alfven surface: the true outer boundary of the solar corona, drawn at
    ALFVEN_SURFACE_RADII from constants_new.py. Beyond this surface, plasma
    can no longer communicate back to the Sun --
    the corona becomes the solar wind.
    Measured directly by NASA's Parker Solar Probe on April 28, 2021.
    MAPS C/2026 A1 crossed inward ~April 3, 2026 -- ~20 hours before disintegration.
    """
    x, y, z = create_sphere_points(ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU, n_points=20)
    r_info = ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.5, color='rgb(0, 200, 200)', opacity=0.35),
        name='Sun: Alfven Surface',
        legendgroup='Sun: Alfven Surface',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(0, 200, 200)',
        "Sun: Alfven Surface<br><br>" + alfven_surface_info.replace('\n', '<br>'),
        'Sun: Alfven Surface'
    )
    return [shell_trace, info_trace]


def create_sun_chromosphere_shell():
    """Creates the Sun's chromosphere shell, at true physical scale.

    The shell sits ~0.29% above the photosphere, so at any scale that
    also renders the corona it reads as welded to the solar surface.
    That is the correct proportion and it is the point (2026-08-16).
    Because photosphere and chromosphere radii differ by less than 10%,
    their info markers would collide at the north pole. Per
    orrery-coding-conventions, the photosphere keeps the pole and this
    marker steps 20 degrees in polar angle along the +x meridian.
    """
    r_shell = CHROMOSPHERE_PHYSICAL_RADII * SOLAR_RADIUS_AU
    x, y, z = create_sphere_points(r_shell, n_points=25)
    r_info = r_shell * 1.05
    info_polar_deg = 20.0
    info_x = r_info * math.sin(math.radians(info_polar_deg))
    info_z = r_info * math.cos(math.radians(info_polar_deg))

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=3.0, color='rgb(30, 144, 255)', opacity=0.5),
        name='Sun: Chromosphere (2,000 km skin)',
        legendgroup='Sun: Chromosphere (2,000 km skin)',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        info_x, 0, info_z,
        'rgb(30, 144, 255)',
        "Sun: Chromosphere (2,000 km skin)<br><br>" + chromosphere_info.replace('\n', '<br>'),
        'Sun: Chromosphere (2,000 km skin)'
    )
    return [shell_trace, info_trace]


def create_sun_photosphere_shell():
    """Creates the Sun's photosphere shell (the visible solar surface)."""
    x, y, z = create_sphere_points(SOLAR_RADIUS_AU, n_points=25)
    r_info = SOLAR_RADIUS_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=7.0, color='rgb(255, 244, 214)', opacity=1.0),
        name='Sun: Photosphere',
        legendgroup='Sun: Photosphere',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed; size 6->8 and
    # gray border -> red (factory default).
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(255, 244, 214)',
        "Sun: Photosphere<br><br>" + photosphere_info.replace('\n', '<br>'),
        'Sun: Photosphere'
    )
    return [shell_trace, info_trace]


def create_sun_radiative_shell():
    """Creates the Sun's radiative zone shell."""
    x, y, z = create_sphere_points(RADIATIVE_ZONE_AU, n_points=25)
    r_info = RADIATIVE_ZONE_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=7, color='rgb(30, 144, 255)', opacity=1.0),
        name='Sun: Radiative Zone',
        legendgroup='Sun: Radiative Zone',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(30, 144, 255)',
        "Sun: Radiative Zone<br><br>" + radiative_zone_info.replace('\n', '<br>'),
        'Sun: Radiative Zone'
    )
    return [shell_trace, info_trace]


def create_sun_core_shell():
    """Creates the Sun's core shell."""
    x, y, z = create_sphere_points(CORE_AU, n_points=25)
    r_info = CORE_AU * 1.05

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=10, color='rgb(70, 130, 180)', opacity=1.0),
        name='Sun: Core',
        legendgroup='Sun: Core',
        hoverinfo='skip',
        showlegend=True
    )
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(70, 130, 180)',
        "Sun: Core<br><br>" + core_info.replace('\n', '<br>'),
        'Sun: Core'
    )
    return [shell_trace, info_trace]


# ============================================================================
# PARTICLE CLOUD FUNCTIONS
# These are not sphere shells -- they use random point generation for visual
# effect. Same pattern applied: hoverinfo='skip' on all cloud points,
# single cross info marker at a representative north-pole position.
# Point density is unchanged (it defines the visual character of these objects).
# ============================================================================

def create_sun_hills_cloud_torus(center_position=(0, 0, 0)):
    """
    The Hills cloud, the inner Oort cloud, as dots along orbits following
    Nesvorny et al. (2025): a slightly warped disk tilted about 30 degrees
    to the ecliptic, with two spiral arms (L-421, 2026-10-10).

    The name is kept, because the dispatch (CUSTOM_SHELLS['Sun']
    ['hills_cloud_torus'], and planet_visualization.py) calls it by it;
    what it draws is no longer a torus. The dots come from
    hills_cloud_sampler.sample_hills_cloud(), which reads every number
    from constants_new.py: the paper's Fig. 3, read into a table, for
    where the orbits' planes lie; its Fig. 2 caption for the two arms;
    the band from INNER_OORT_DISK_OUTER_AU to INNER_OORT_CLOUD_AU, across
    which the disk thins out; and a declared eccentricity. The tilt is
    not set: it comes out of the orbits, and hills_cloud_sampler.py
    prints it. The typed 2,000 and 20,000 AU defaults this replaced are
    gone (the design record of 2026-10-09, section 2).

    Parameters:
    - center_position: Sun position tuple (default: (0, 0, 0)).
      Accepted for interface uniformity with the unified dispatch
      contract. Geometry translation deferred to switchover phase.
    """
    # Phase D1: center_position accepted for interface uniformity;
    # geometry translation deferred to switchover phase.
    from hills_cloud_sampler import drawn_hills_cloud
    # 600 orbits of 6 dots: 3,600, the torus's count (render size, Tony's
    # standing concern), from a fixed seed. The settings live in
    # hills_cloud_sampler.py, because the website draws the same dots
    # from data/drawings/hills_cloud.json (L-421, 2026-10-11): one place,
    # so the two cannot come to differ. Seeded, every plot is the same
    # cloud (L-239, for this builder).
    dots = drawn_hills_cloud()
    x_flat, y_flat, z_flat = dots['x'], dots['y'], dots['z']

    # Tony's confirmed words, 2026-10-09 (design record sections 4 and 9),
    # with the citation, as the orrery's hovers carry it. The distances
    # and the tilt print from their rows; AU with km beside, by the hover
    # AU convention.
    hills_hover = (
        'The inner part of the Oort cloud: icy bodies far beyond the planets,<br>'
        'gathered in a slightly warped disk.<br><br>'
        f'From {_OORT_INNER_EDGE} AU ({row_text("INNER_LIMIT_OORT_CLOUD_AU", unit="km", grouping=True)} km)<br>'
        f'to {_OORT_DISK_EDGE} AU ({row_text("INNER_OORT_DISK_OUTER_AU", unit="km", grouping=True)} km),<br>'
        f'thinning out by {_OORT_HILLS_EDGE} AU ({row_text("INNER_OORT_CLOUD_AU", unit="km", grouping=True)} km).<br>'
        'A 2025 computer model (Nesvorny and others) finds the disk tilted<br>'
        f'about {_HILLS_TILT} degrees to the ecliptic, the plane of Earth\'s orbit, with<br>'
        'two spiral arms. The dots follow orbits like the model\'s; how stretched<br>'
        'the orbits are is chosen for the picture.<br><br>'
        'Nesvorny, D., et al. (2025), A Spiral Structure in the Inner Oort Cloud,<br>'
        'arXiv:2502.11252'
    )

    shell_trace = go.Scatter3d(
        x=x_flat, y=y_flat, z=z_flat,
        mode='markers',
        marker=dict(size=1.5, color='rgb(173, 216, 230)', opacity=0.4, symbol='circle'),
        name='Sun: Hills Cloud (tilted disk)',
        legendgroup='Sun: Hills Cloud (tilted disk)',
        hoverinfo='skip',
        showlegend=True
    )
    # The info marker sits above the disk's middle, on the ecliptic pole
    # at the band's near end: clear of the dots, which crowd toward the
    # disk's plane.
    r_info = INNER_OORT_DISK_OUTER_AU
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(173, 216, 230)',
        f"Sun: Hills Cloud (tilted disk)<br><br>{hills_hover}",
        'Sun: Hills Cloud (tilted disk)',
        customdata='Hills Cloud Torus'
    )
    return [shell_trace, info_trace]


def _outer_cloud_keep(distance):
    """Chance of keeping a point of the round outer cloud at `distance`
    AU (L-421, 2026-10-10): nothing at the band's near end,
    INNER_OORT_DISK_OUTER_AU, rising evenly to all of them at its far end,
    INNER_OORT_CLOUD_AU, and all of them beyond. The Hills cloud thins out
    across the same band, so the two overlap inside it (Tony's ruling of
    2026-10-09, a fuzzy boundary)."""
    near, far = float(INNER_OORT_DISK_OUTER_AU), float(INNER_OORT_CLOUD_AU)
    return np.clip((np.asarray(distance, dtype=float) - near) / (far - near), 0.0, 1.0)


def create_sun_outer_oort_clumpy(center_position=(0, 0, 0), radius_min=None, radius_max=None, n_clumps=15):
    """
    Create a clumpy, asymmetric outer Oort Cloud with density variations.
    FIXED VERSION - Returns proper Plotly trace objects.

    Parameters:
    - center_position: Sun position tuple (default: (0, 0, 0)).
      Accepted for interface uniformity with the unified dispatch
      contract. Geometry translation deferred to switchover phase.
    - radius_min: Inner boundary in AU (default: INNER_OORT_DISK_OUTER_AU,
      the near end of the band where the outer cloud begins thin)
    - radius_max: Outer boundary in AU (default: OUTER_OORT_CLOUD_AU)
    - n_clumps: Number of density clumps (default: 15)

    L-421 (2026-10-10): the defaults were typed, 20000 and 100000; they
    read the rows now. The cloud is thin at the band's near end and full
    by its far end, INNER_OORT_CLOUD_AU (_outer_cloud_keep): a clump's
    centre and each of its points are kept with that chance. The clumps'
    sizes and point counts are unchanged, a drawing choice.
    """
    # Phase D1: center_position accepted for interface uniformity;
    # geometry translation deferred to switchover phase.
    radius_min = INNER_OORT_DISK_OUTER_AU if radius_min is None else radius_min
    radius_max = OUTER_OORT_CLOUD_AU if radius_max is None else radius_max
    points_x, points_y, points_z = [], [], []
    
    for i in range(n_clumps):
        clump_radius = np.random.uniform(radius_min, radius_max)
        while np.random.random() >= _outer_cloud_keep(clump_radius):
            clump_radius = np.random.uniform(radius_min, radius_max)
        theta = np.random.uniform(0, 2*np.pi)
        phi = np.random.uniform(-np.pi/2, np.pi/2)
        
        clump_center_x = clump_radius * np.cos(phi) * np.cos(theta)
        clump_center_y = clump_radius * np.cos(phi) * np.sin(theta)
        clump_center_z = clump_radius * np.sin(phi)
        
        n_points_in_clump = np.random.randint(50, 200)
        clump_size = np.random.uniform(5000, 15000)
        
        for j in range(n_points_in_clump):
            r = clump_size * np.random.beta(2, 5)
            theta_local = np.random.uniform(0, 2*np.pi)
            phi_local = np.random.uniform(-np.pi/2, np.pi/2)
            
            x = clump_center_x + r * np.cos(phi_local) * np.cos(theta_local)
            y = clump_center_y + r * np.cos(phi_local) * np.sin(theta_local)
            z = clump_center_z + r * np.sin(phi_local)
            
            distance = np.sqrt(x**2 + y**2 + z**2)
            if (radius_min <= distance <= radius_max
                    and np.random.random() < _outer_cloud_keep(distance)):
                points_x.append(x)
                points_y.append(y)
                points_z.append(z)
    
    x = np.array(points_x)
    y = np.array(points_y)
    z = np.array(points_z)

    clumpy_hover = (
        'Outer Oort Cloud: Clumpy, asymmetric structure<br>'
        f'From {_OORT_DISK_EDGE} AU, filling in by {_OORT_HILLS_EDGE} AU, to {_OORT_OUTER_EDGE}+ AU<br>'
        'It begins where the inner cloud\'s disk thins out<br>'
        'Source of long-period comets<br>'
        'Influenced by galactic tides and stellar encounters'
    )

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=1.0, color='rgb(255, 255, 255)', opacity=0.3, symbol='circle'),
        name='Sun: Outer Oort Cloud (Clumpy)',
        legendgroup='Sun: Outer Oort Cloud (Clumpy)',
        hoverinfo='skip',
        showlegend=True
    )
    r_info = radius_max * 1.05
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(255, 255, 255)',
        f"Sun: Outer Oort Cloud (Clumpy)<br><br>{clumpy_hover}",
        'Sun: Outer Oort Cloud (Clumpy)',
        customdata='Outer Oort Cloud'
    )
    return [shell_trace, info_trace]


def create_sun_galactic_tide(center_position=(0, 0, 0), n_points=5000):
    """
    Where the galaxy's tide sends comets in from: points in the outer Oort
    cloud, tilted into the galaxy's plane, sparse at the plane and at the
    galactic poles and thickest halfway between.

    THE DRAWING IS A CHOICE RESTING ON WHAT CAN BE CITED (L-406, Tony's
    rulings of 2026-10-02):
    - The plane. Points are placed about the north galactic pole of J2000,
      GALACTIC_NORTH_POLE_RA_J2000_DEG / _DEC_J2000_DEG in constants_new.py,
      and turned into the drawing's frame by the same matrix a planet's
      pole uses (idealized_orbits.create_pole_transformation_matrix).
    - The density. The number of points per piece of sky goes as
      |sin b cos b|, b the galactic latitude: none at the plane or the
      poles, most at 45 degrees. The sources are in the comments beside
      the code that does it.
    - The distance. From INNER_OORT_DISK_OUTER_AU, thin there and full
      by INNER_OORT_CLOUD_AU, the band where the inner cloud's disk gives
      way to the round outer cloud (L-421, 2026-10-10), then evenly to
      OUTER_OORT_CLOUD_AU; the clumpy outer Oort cloud uses the same band.
      It replaced a typed 50,000 AU with a typed spread and cut-offs
      (L-406).
    - Each point stands for the far end of an orbit. Where any real comet
      is, is not known and is not claimed.
    - The cone (L-420, Tony's choice of 2026-10-06). A faint double cone
      through the Sun, at the galactic latitude where |sin b cos b| is
      largest, between the same two edges. It marks where the density
      above peaks, so the shape reads from the side as an hourglass.
      It is not a surface any comet is on.

    Parameters:
    - center_position: Sun position tuple (default: (0, 0, 0)).
      Accepted for interface uniformity with the unified dispatch
      contract. Geometry translation deferred to switchover phase.
    - n_points: Number of random points (default: 5000, up from 2000
      after Tony's look of 2026-10-06), a rendering setting.
    """
    # Phase D1: center_position accepted for interface uniformity;
    # geometry translation deferred to switchover phase.
    from idealized_orbits import create_pole_transformation_matrix
    M = np.asarray(create_pole_transformation_matrix(
        GALACTIC_NORTH_POLE_RA_J2000_DEG, GALACTIC_NORTH_POLE_DEC_J2000_DEG),
        dtype=float)

    # Source: Matese and Whitmire, "Persistent Evidence of a Jovian Mass
    #   Solar Companion in the Oort Cloud", arXiv:1004.4584, sec. 2.2 --
    #   the dominant disk tidal term goes as |sin B cos B| (Matese et al.
    #   1999), so if the tide dominates, the aphelia of new comets avoid
    #   the galactic poles and equator and peak near B = +/-45 degrees.
    # Source: Delsemme, "Galactic tides affect the Oort cloud: an
    #   observational confirmation", A&A 187, 913 (1987), summary -- the
    #   aphelia of 152 comets with periods over ten thousand years avoid
    #   the two galactic polar caps and a strip along the galactic equator.
    # Note: not everyone reads it this way. Higuchi, "Anisotropy of
    #   Long-period Comets Explained by Their Formation Process",
    #   arXiv:2008.04324 (AJ 160, 134), explains the same depletions by
    #   comets gathering near the ecliptic and a second plane; and Rickman
    #   et al. (2008), as Matese and Whitmire report, take the term to go
    #   as |sin B|.
    # Galactic latitude by rejection. Drawing sin(b) evenly gives every
    # piece of sky the same chance; keeping a draw with probability
    # |2 sin b cos b| = |sin 2b| (at most 1, at b = 45 degrees) makes the
    # points per piece of sky go as |sin b cos b|.
    sin_b = np.empty(0)
    while sin_b.size < n_points:
        u = np.random.uniform(-1.0, 1.0, 2 * n_points)
        keep = np.random.uniform(0.0, 1.0, u.size) < 2.0 * np.abs(u) * np.sqrt(1.0 - u * u)
        sin_b = np.concatenate([sin_b, u[keep]])
    sin_b = sin_b[:n_points]
    cos_b = np.sqrt(1.0 - sin_b * sin_b)
    lon = np.random.uniform(0, 2 * np.pi, n_points)
    # L-421 (2026-10-10): from the band's near end, INNER_OORT_DISK_OUTER_AU,
    # thin there and full by INNER_OORT_CLOUD_AU (_outer_cloud_keep), the
    # same band the Hills cloud thins out across. Same number of points.
    r = np.empty(0)
    while r.size < n_points:
        draw = np.random.uniform(INNER_OORT_DISK_OUTER_AU, OUTER_OORT_CLOUD_AU, 2 * n_points)
        r = np.concatenate([r, draw[np.random.uniform(0.0, 1.0, draw.size) < _outer_cloud_keep(draw)]])
    r = r[:n_points]

    galactic = np.vstack([r * cos_b * np.cos(lon),
                          r * cos_b * np.sin(lon),
                          r * sin_b])
    x, y, z = M @ galactic

    # Tony's approved words, 2026-10-02 (L-406). The distances are the
    # rows', printed as the clumps' hover prints them.
    tide_hover = (
        'Galactic Tide: sends comets in from the outer Oort cloud<br>'
        'Tilted to the galaxy\'s plane, thickest halfway to its poles<br>'
        'The pink cone marks that halfway line, where the tide<br>'
        'changes comets\' orbits the most<br>'
        f'From {_OORT_DISK_EDGE} AU, filling in by {_OORT_HILLS_EDGE} AU, to {_OORT_OUTER_EDGE} AU<br>'
        'Where the comets really are is not known'
    )

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        # Size and opacity doubled, and two and a half times the points,
        # after Tony's look of 2026-10-06: the tide was too faint to read.
        marker=dict(size=1.6, color='rgb(255, 182, 193)', opacity=0.45, symbol='circle'),
        name='Sun: Galactic Tide Region',
        legendgroup='Sun: Galactic Tide Region',
        hoverinfo='skip',
        showlegend=True
    )
    # The cone (L-420, 2026-10-06). |sin b cos b| is largest where
    # sin b equals cos b, so at b = arctan(1), north and south. Each half
    # is a band of triangles between the two edges the points use,
    # turned by the same matrix M. Faint, no hover: the tide's info
    # marker carries its words. It toggles with the tide.
    b_peak = np.arctan(1.0)
    n_around = 72                      # a rendering setting
    phi = np.linspace(0, 2 * np.pi, n_around, endpoint=False)
    cone_traces = []
    for sign in (1.0, -1.0):
        b = sign * b_peak
        ring = np.concatenate([
            np.vstack([edge * np.cos(b) * np.cos(phi),
                       edge * np.cos(b) * np.sin(phi),
                       edge * np.sin(b) * np.ones(n_around)])
            for edge in (INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU)], axis=1)
        cx, cy, cz = M @ ring
        nxt = (np.arange(n_around) + 1) % n_around
        here = np.arange(n_around)
        cone_traces.append(go.Mesh3d(
            x=cx, y=cy, z=cz,
            i=np.concatenate([here, nxt]),
            j=np.concatenate([nxt, n_around + nxt]),
            k=np.concatenate([n_around + here, n_around + here]),
            color='rgb(255, 182, 193)',
            opacity=0.12,
            flatshading=True,
            hoverinfo='skip',
            name='Sun: Galactic Tide Region',
            legendgroup='Sun: Galactic Tide Region',
            showlegend=False))

    r_info = OUTER_OORT_CLOUD_AU * 1.05
    # Phase 1 re-pipe (May 28, 2026): factory-routed.
    info_trace = create_info_marker(
        0, 0, r_info,
        'rgb(255, 182, 193)',
        f"Sun: Galactic Tide Region<br><br>{tide_hover}",
        'Sun: Galactic Tide Region',
        customdata='Galactic Tide Region'
    )
    return [shell_trace] + cone_traces + [info_trace]


# =========================================================================
# Streamer band -- CUSTOM_SHELLS builder (L-224)
# =========================================================================
# Wired via CUSTOM_SHELLS['Sun']['streamer_belt']. This is the live path.
#
# Replaces the sphere that SHELL_CONFIGS['Sun']['streamer_belt'] drew at
# a single radius. Two things were wrong with that sphere: helmet
# streamers form only over the magnetic neutral line, so a full sphere
# asserted them over the poles where coronal holes are instead; and its
# radius was a drawing choice with no boundary under it (L-210 withdrew
# the 4-6 R_sun range as unsourced).
#
# Source: constants_new.py HELMET_CUSP_RADII -- the cusp, not an edge.

def create_sun_streamer_band(center_position=(0, 0, 0)):
    """Streamer belt as one warped band: closed helmet, open stalk.

    Parameters
    ----------
    center_position : tuple
        Sun position. Accepted for interface uniformity with the
        CUSTOM_SHELLS dispatch contract; geometry translation is
        deferred here exactly as in the sibling Oort and tide builders.

    Returns a list of plotly traces, per the CUSTOM_SHELLS contract.

    One info marker only, per the single-info-marker convention, sitting
    just outside the band's edge at the cusp -- the pinch is where the
    eye goes and where the physics is. It is NOT at a pole: this is a
    band, and the poles are empty by design.
    """
    cusp_rs = float(HELMET_CUSP_RADII)     # the cusp, not an outer edge
    fade_rs = float(ALFVEN_SURFACE_RADII)  # dissolves across the Alfven surface

    # L-460 (2026-10-21): the band starts at the corona's base, as the
    # corona's dots do, not at the Sun's surface under the chromosphere.
    params = {'base_radius': float(CORONA_BASE_RADII),
              'cusp_radius': cusp_rs,
              'fade_radius': fade_rs,
              'outer_radius': fade_rs * 1.015}
    xs, ys, zs, alphas, sizes = create_streamer_band_shape(params)

    # BODY FRAME -> ECLIPTIC. create_streamer_band_shape's own docstring
    # says it returns points "in the body frame". Until 2026-08-23 the
    # caller scaled them and handed them to Plotly UNROTATED, i.e. treated
    # body-frame points as ecliptic ones. That is an internal contract
    # violation and it is the whole reason for this rotation -- no claim
    # about solar physics is needed to justify it, and none is made here.
    # The Sun's rotation axis trace, built from the very matrix used
    # below, was already correctly tilted, so two traces in one figure
    # disagreed about where the Sun's equator is. Found by Mode 5 (L-229).
    # Source: IAU 2018 solar pole, via constants_new.planet_poles['Sun']
    #   (ra 286.13, dec 63.87) -- the SAME source build_rotation_axis_traces
    #   reads, so the band and the axis now derive from one matrix and
    #   cannot drift apart again.
    # ASSUMPTION: that the streamer belt is organized about the solar
    #   equator AT ALL is a drawing choice, not a sourced boundary. No
    #   citation for the belt's orientation exists in this project, nor
    #   for warp_amp_deg = 15.0, nor for the two-lobe warp. The pole is
    #   sourced; anchoring the band to it is ours. An earlier version of
    #   this comment argued the case from magnetic-equator physics that
    #   nobody had sourced -- withdrawn 2026-08-23, see L-229. The hover
    #   says the same thing to the reader.
    # The import is lazy for the same reason it is lazy in
    #   build_rotation_axis_traces: idealized_orbits is heavy.
    from idealized_orbits import create_planet_transformation_matrix

    M = np.asarray(create_planet_transformation_matrix('Sun'), dtype=float)

    def _to_ecliptic(bx, by, bz):
        """Rotate one body-frame point into ecliptic coordinates."""
        v = M @ np.array([bx, by, bz], dtype=float)
        return float(v[0]), float(v[1]), float(v[2])

    rot = M @ np.vstack([np.asarray(xs, dtype=float),
                         np.asarray(ys, dtype=float),
                         np.asarray(zs, dtype=float)])

    scale = SOLAR_RADIUS_AU
    x_au = (rot[0] * scale).tolist()
    y_au = (rot[1] * scale).tolist()
    z_au = (rot[2] * scale).tolist()
    # Per-point rgba. marker.opacity is a scalar in Plotly; the colour
    # array is what lets one trace fade to nothing.
    colors = ['rgba(255, 200, 80, %.4f)' % a for a in alphas]

    # L-371: the cusp and the fade print from their rows, at their counts;
    # L-411: so does the coronagraph's 15 R_sun floor, which was typed here.

    # Every line carries its own <br>: in this file the SOURCE wrap and
    # the RENDERED wrap are one act, and a line without a break renders
    # as part of a run that can reach hundreds of characters (L-227).
    band_hover = (
        "One object with two regimes, not a shell with a radius.<br><br>"

        "CLOSED HELMET -- the dense, wide base. Magnetic arcades stand<br>"
        "over the neutral line, closed at both ends. They reach no<br>"
        f"higher than {row_text('HELMET_CUSP_LOW_RADII')}-{row_text('HELMET_CUSP_HIGH_RADII')} R_sun, and the band pinches at {row_text('HELMET_CUSP_RADII')} R_sun<br>"
        f"({row_text('HELMET_CUSP_RADII', 'km', grouping=True)} km, {row_text('HELMET_CUSP_RADII', 'au')} AU) where they open.<br>"
        "Source: Suess & Nerney (2004), Adv. Space Res. 33:668-675 --<br>"
        "stated there as established background, not measured by it, so<br>"
        "the pinch is drawn soft rather than sharp.<br><br>"

        "OPEN STALK -- above the pinch. A thin sheet along the current<br>"
        "sheet. It has NO outer edge: it thins into the slow solar wind,<br>"
        "so this drawing dissolves instead of stopping. Nothing is drawn<br>"
        f"past the Alfven surface at {row_text('ALFVEN_SURFACE_RADII')} R_sun<br>"
        # Source: constants_new.py ALFVEN_SURFACE_RADII -- the km and AU
        #   figures on the next line are COMPUTED from it, not typed, so
        #   this line restates a cited constant rather than making an
        #   independent claim. See the Source+ leg on that constant
        #   (L-209). The comment sits HERE, mid-string, because the
        #   scanner judges citation by line distance and the L-227
        #   re-flow moved this line out of the window (L-229).
        f"({row_text('ALFVEN_SURFACE_RADII', 'km', grouping=True)} km, {row_text('ALFVEN_SURFACE_RADII', 'au')} AU), where the corona becomes<br>"
        "wind. Beyond that the sheet continues as the heliospheric<br>"
        "current sheet, out to the heliopause.<br><br>"

        "THE VISIBLE EDGE. That a sharp brightness boundary exists is a<br>"
        "coronagraph observation. What it DIVIDES is an interpretation:<br>"
        "Suess & Nerney take it as reasonable to assume it separates<br>"
        "fast coronal-hole wind from slow wind. Slow-wind origin is not<br>"
        "settled, so the edge is drawn and its meaning is attributed.<br><br>"

        "DeForest, Howard & McComas (2014), ApJ 787:124 followed inbound<br>"
        f"wave motion out to {row_text('ALFVEN_SURFACE_STREAMER_FLOOR_RADII')} R_sun ({row_text('ALFVEN_SURFACE_STREAMER_FLOOR_RADII', 'km', grouping=True)} km, {row_text('ALFVEN_SURFACE_STREAMER_FLOOR_RADII', 'au')} AU).<br>"
        "That is the coronagraph's field of view, not an extent --<br>"
        "a floor, not an edge.<br><br>"

        "THE WARP is drawn in ONE configuration, near solar minimum. The<br>"
        "neutral line's tilt sweeps toward the poles across the 11-year<br>"
        "cycle; this is the shape, not a measurement of today's.<br><br>"

        "THE PLANE the band sits in is the SUN'S equatorial plane, tilted<br>"
        "about 7.25 degrees from the ecliptic by the IAU 2018 solar pole.<br>"
        "The pole is measured. That the belt is organized about that plane<br>"
        "at all is an ASSUMPTION -- as are the warp's 15-degree amplitude<br>"
        "and its two lobes. No source for the belt's orientation is cited<br>"
        "in this project. The ecliptic was worse, not the alternative.<br><br>"

        "Drawn as a visualization assumption where no measured boundary<br>"
        "exists (L-224)."
    )

    # L-410 (Tony, 2026-10-19): the corona is ONE feature, the fade and
    # this band, under one checkbox and one legend entry, so the band
    # joins the corona's legend group and shows no entry of its own.
    band_trace = go.Scatter3d(
        x=x_au, y=y_au, z=z_au,
        mode='markers',
        marker=dict(size=sizes, color=colors, symbol='circle'),
        name=CORONA_LEGEND,
        legendgroup=CORONA_LEGEND,
        hoverinfo='skip',
        showlegend=False
    )

    # Info marker: at the cusp, at the longitude where the warp peaks,
    # stepped just outside the band edge so it is not buried in points.
    lon_i = math.pi / 4.0
    lat_i = math.radians(STREAMER_BAND_DEFAULTS['warp_amp_deg']
                         + STREAMER_BAND_DEFAULTS['cusp_half_width_deg'] + 6.0)
    r_i = cusp_rs * SOLAR_RADIUS_AU * 1.02
    # The marker is placed in the SAME body frame as the band and rotated
    # with it. Rotating one and not the other would leave the marker
    # floating off the band edge: the geometry would be right and the
    # affordance would be wrong, which is the harder kind of bug to see.
    mx, my, mz = _to_ecliptic(r_i * math.cos(lat_i) * math.cos(lon_i),
                              r_i * math.cos(lat_i) * math.sin(lon_i),
                              r_i * math.sin(lat_i))
    info_trace = create_info_marker(
        mx, my, mz,
        'rgb(255, 200, 80)',
        f"Sun: Streamer Belt<br><br>{band_hover}",
        CORONA_LEGEND,
        customdata='Streamer Belt'
    )
    return [band_trace, info_trace]



#####################################
# The corona's fade and the zodiacal dust cloud (L-410 with L-131)
#####################################
# Built 2026-10-19 on Tony's rulings of that day (design record:
# documentation/SOURCES_L410_sun_corona_dust_20261019.md). The words are
# Tony's approved list, documentation/WORDS_L410_sun_fades_20261019.md,
# items 1a to 1e, 2a to 2e, 3b and 3c, written once here in newlines and
# turned to <br> only at the Plotly boundary (L-191's canonical form).
# The checkbox tooltip carries the hover's words and the panel's; the
# website serves the same words from data/objects_config.json.
#
# Source: every figure below is read from its row in constants_new.py,
# Source+: where each carries its citation: Kasper et al. (2021) for the
# Source+: Alfven surface; NASA, "Sun: Facts", for the corona's
# Source+: temperature; Kelsall et al. (1998) for the dust cloud's
# Source+: density exponent, tilt and outer cutoff; Lamy, Gilardy and
# Source+: Llebaria (2022) for the depletion and dust-free zones; Nesvorny
# Source+: et al. (2010) for where the dust comes from. The words also
# Source+: name Boe et al. (2021), Mann et al. (2023) and Howard et al.
# Source+: (2019), each carried on its row's Source line.

def _temperature_text(name):
    """A temperature row in kelvin, grouped by thousands."""
    return row_text(name, grouping=True)


# 1c, the corona's hover (the glance).
corona_hover_words = (
    "The Sun's outer atmosphere, a very thin gas of electrons and ions.\n"
    "It begins about "
    f"{row_text('CORONA_BASE_HEIGHT_KM', grouping=True)} km above the "
    "visible surface, just above the\n"
    "chromosphere, and has no outer edge. It thins out with height, and\n"
    f"at the Alfven surface, about {row_text('ALFVEN_SURFACE_RADII')} solar radii "
    f"({row_text('ALFVEN_SURFACE_RADII', 'km', grouping=True)} km, "
    f"{row_text('ALFVEN_SURFACE_RADII', 'au')} AU)\n"
    "from the Sun's center, it becomes the solar wind.\n"
    "Each dot's place shows how dense the gas is; its brightness shows\n"
    "how much sunlight reaches it.\n"
    "The streamer belt, drawn with it, is the part of the corona where\n"
    "the Sun's magnetic field closes in loops."
)

# 1d with 3c, the corona's panel text.
corona_panel_words = (
    "The corona's glow, seen at a total eclipse, is sunlight scattered by\n"
    "its free electrons, called the K-corona (Boe and others, 2021). How\n"
    "dense the gas is at each height comes from a model of the solar wind\n"
    "from the base of the corona out past Earth's orbit (Mann and others,\n"
    "2023). The dots follow it: crowded at the base, sparse by the Alfven\n"
    "surface. Farther out a second, fainter light takes over, sunlight\n"
    "scattered by dust, the F-corona; that dust is drawn as its own cloud.\n"
    "The corona is very hot, up to about "
    f"{_temperature_text('CORONA_TEMPERATURE_MAX_K')} kelvin, far hotter\n"
    "than the surface below it (NASA)."
)

# 1e, the drawing note.
corona_note_words = (
    "The corona is drawn in two parts. The dots show how dense its gas is\n"
    "at each height, on average, drawn the same in every direction. The\n"
    "streamer belt, drawn as a band, shows the brightest part of the\n"
    "corona, where the Sun's magnetic field closes in loops. The dots stop\n"
    "at the Alfven surface, the outer edge of the Sun's atmosphere, where\n"
    "the gas becomes the solar wind."
)

# The checkbox tooltip, "-- Corona": all three, in newlines.
# One string, the checkbox tooltip and the plot hover alike
# (L-191, Tony's pick of 2026-10-21): the title, the hover's
# words, then the panel's words and the drawing note.
corona_info = ("Sun: Corona\n\n" + corona_hover_words + "\n\n"
               + corona_panel_words + "\n\n" + corona_note_words)

# 2c, the dust cloud's hover.
zodiacal_dust_hover_words = (
    "Dust spread through the inner solar system, flattened toward the\n"
    "plane the planets move in. It thins with distance from the Sun and\n"
    f"has no edge; the drawing stops at {row_text('ZODIACAL_DUST_OUTER_AU')} AU "
    f"({row_text('ZODIACAL_DUST_OUTER_AU', 'km', grouping=True)} km).\n"
    "Each dot's place shows how dense the dust is; its brightness shows\n"
    "how much sunlight reaches it.\n"
    "Near the Sun this dust is seen as the F-corona."
)

# 2d with 3b, the dust cloud's panel text.
zodiacal_dust_panel_words = (
    "This dust scatters sunlight. Near the Sun that light is the F-corona,\n"
    "the part of the zodiacal light closest to the Sun (Boe and others,\n"
    "2021). The cloud's shape follows the model fitted to the COBE\n"
    "satellite's infrared sky: its density falls with distance from the\n"
    f"Sun to the power {row_text('ZODIACAL_DUST_DENSITY_EXPONENT')}, and it is "
    "flattened toward a middle\n"
    f"plane tilted {row_text('ZODIACAL_DUST_TILT_DEG')} degrees to Earth's "
    "orbit (Kelsall and others, 1998).\n"
    "Close to the Sun the dust thins from about "
    f"{row_text('DUST_DEPLETION_OUTER_RADII')} solar radii inward\n"
    f"and is gone by about {row_text('DUST_FREE_ZONE_RADII')}, the dust-free "
    "zone (Lamy and others, 2022);\n"
    "Parker Solar Probe saw the first signs of it (Howard and others, 2019).\n"
    "There, the cloud's middle plane is also warped (Lamy and others, 2022),\n"
    "which the drawing does not show.\n"
    "Judged by its infrared glow, most of this dust comes from comets whose\n"
    "orbits Jupiter shapes, the Jupiter-family comets: "
    f"{row_text('ZODIACAL_DUST_JFC_LOW_PERCENT')} to "
    f"{row_text('ZODIACAL_DUST_JFC_HIGH_PERCENT')}\n"
    "percent. Asteroids give less than "
    f"{row_text('ZODIACAL_DUST_ASTEROID_MAX_PERCENT')} percent "
    "(Nesvorny and others, 2010)."
)

# 2e, the dust cloud's drawing note.
zodiacal_dust_note_words = (
    "The cloud has no edge. The dots stop at "
    f"{row_text('ZODIACAL_DUST_OUTER_AU')} AU, where the COBE model\n"
    "stops adding up its light. Only the model's smooth cloud is drawn, not\n"
    "the narrow dust bands it also includes."
)

# One string, the checkbox tooltip and the plot hover alike
# (L-191, Tony's pick of 2026-10-21): the title, the hover's
# words, then the panel's words and the drawing note.
zodiacal_dust_info = ("Sun: Zodiacal Dust Cloud (F-corona)\n\n"
                      + zodiacal_dust_hover_words + "\n\n"
                      + zodiacal_dust_panel_words + "\n\n"
                      + zodiacal_dust_note_words)

# One legend entry for the corona's two drawings (Tony, 2026-10-19: the
# corona is ONE feature, the fade and the streamer belt, one name, one
# checkbox, one legend entry, one colour family).
CORONA_LEGEND = 'Sun: Corona'
ZODIACAL_DUST_LEGEND = 'Sun: Zodiacal Dust Cloud (F-corona)'


def _shaded_dots(weights, rgb, alpha_low, alpha_high, size_low, size_high):
    """Per-dot colours and sizes from weights 0 to 1: brighter and larger
    toward weight 1, the sunlit end. Rendering settings."""
    colors = ['rgba(%s, %.3f)' % (rgb, alpha_low + (alpha_high - alpha_low) * w)
              for w in weights]
    sizes = [size_low + (size_high - size_low) * w for w in weights]
    return colors, sizes


def create_sun_corona(center_position=(0, 0, 0)):
    """The Sun's corona as dots that thin out with distance (L-410).

    The dots are the stored drawing sun_corona_sampler.drawn_corona()
    places, in solar radii, from the Sun's surface to the Alfven surface:
    a dot's place follows the electron density of Mann et al. (2023), its
    weight the sunlight reaching it. Scaled by SOLAR_RADIUS_AU; drawn
    round. The website draws the same dots from
    data/drawings/sun_corona.json. One info marker, over the north pole
    at the Alfven surface, stepped 20 degrees off the pole so it does not
    sit on the Alfven surface's own marker (Marker Separation for
    Near-Equal Radii). The streamer band joins this legend entry.
    """
    from sun_corona_sampler import drawn_corona
    cx, cy, cz = center_position
    dots = drawn_corona()
    # Colour family of the streamer band, rgb(255, 200, 80), paler, and
    # the shading by weight: rendering settings.
    colors, sizes = _shaded_dots(dots['w'], '255, 225, 150', 0.15, 0.85,
                                 1.2, 3.0)
    scale = SOLAR_RADIUS_AU
    traces = [go.Scatter3d(
        x=[v * scale + cx for v in dots['x']],
        y=[v * scale + cy for v in dots['y']],
        z=[v * scale + cz for v in dots['z']],
        mode='markers',
        marker=dict(size=sizes, color=colors, symbol='circle'),
        name=CORONA_LEGEND, legendgroup=CORONA_LEGEND,
        hoverinfo='skip', showlegend=True,
    )]
    info_polar_deg = 20.0
    r_info = ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU * 1.05
    traces.append(create_info_marker(
        r_info * math.sin(math.radians(info_polar_deg)) + cx, cy,
        r_info * math.cos(math.radians(info_polar_deg)) + cz,
        'rgb(255, 225, 150)', corona_info.replace('\n', '<br>'),
        CORONA_LEGEND, customdata='Corona'))
    return traces


def create_sun_zodiacal_dust(center_position=(0, 0, 0)):
    """The zodiacal dust cloud as dots (L-131).

    The dots are the stored drawing zodiacal_dust_sampler.drawn_dust()
    places, in AU in the ecliptic frame, from the edge of the dust-free
    zone to 5.2 AU: a dot's place follows Kelsall et al. (1998)'s smooth
    cloud, its weight the sunlight reaching it. The website draws the
    same dots from data/drawings/zodiacal_dust.json. One info marker, in
    the cloud's middle plane just past its outer edge, toward the plane's
    ascending node: on the cloud, clear of the poles where it is empty.
    """
    from zodiacal_dust_sampler import drawn_dust, rows_from_store, to_ecliptic
    cx, cy, cz = center_position
    dots = drawn_dust()
    colors, sizes = _shaded_dots(dots['w'], '215, 190, 150', 0.2, 0.9,
                                 1.2, 3.0)
    traces = [go.Scatter3d(
        x=[v + cx for v in dots['x']],
        y=[v + cy for v in dots['y']],
        z=[v + cz for v in dots['z']],
        mode='markers',
        marker=dict(size=sizes, color=colors, symbol='circle'),
        name=ZODIACAL_DUST_LEGEND, legendgroup=ZODIACAL_DUST_LEGEND,
        hoverinfo='skip', showlegend=True,
    )]
    rows = rows_from_store()
    mx, my, mz = to_ecliptic(rows['ZODIACAL_DUST_OUTER_AU'] * 1.03, 0.0, 0.0,
                             rows)
    traces.append(create_info_marker(
        mx + cx, my + cy, mz + cz, 'rgb(215, 190, 150)',
        zodiacal_dust_info.replace('\n', '<br>'),
        ZODIACAL_DUST_LEGEND, customdata='Zodiacal Dust Cloud'))
    return traces
