"""
shell_configs.py - Shell configuration data for all celestial bodies.

Phase A (Mercury POC) - May 2026. Other bodies will be added in Phases B-D.

Two registries:

  SHELL_CONFIGS  - Sphere shell parameters (radius, color, opacity, hover text,
                   tooltip). Consumed by build_sphere_shell() in orrery_rendering.py.

  CUSTOM_SHELLS  - Non-sphere geometry (magnetospheres, rings, tails, belts).
                   Maps shell_name -> {'builder': 'module.function', 'tooltip': '...'}.
                   Lazy-imported at render time to address startup lag.

To add a new body:
    1. Verify its radius is in CENTER_BODY_RADII (constants_new.py)
    2. Add its sphere shell configs to SHELL_CONFIGS
    3. Add its custom geometry (if any) to CUSTOM_SHELLS
    4. Add its checkbox vars in palomas_orrery.py GUI section (or already exist)

Source citations are preserved as comments above each body block. The
provenance audit (April 2026) verified all values - do not modify.

Module updated: May 2026 with Anthropic's Claude Opus 4.6
"""

# Phase C4: Import hover text strings from body shell modules.
# The info strings are the authoritative source -- no duplication.
from saturn_visualization_shells import (
    saturn_core_info, saturn_metallic_hydrogen_info,
    saturn_molecular_hydrogen_info, saturn_cloud_layer_info,
    saturn_upper_atmosphere_info, saturn_hill_sphere_info,
)
from uranus_visualization_shells import (
    uranus_core_info, uranus_mantle_info,
    uranus_cloud_layer_info, uranus_upper_atmosphere_info,
    uranus_hill_sphere_info,
)
from neptune_visualization_shells import (
    neptune_core_info, neptune_mantle_info,
    neptune_cloud_layer_info, neptune_upper_atmosphere_info,
    neptune_hill_sphere_info,
)

# Phase D1: Import Sun hover text and tooltip strings.
from solar_visualization_shells import (
    # hover_text (Plotly hover, <br> line breaks)
    core_info_hover, radiative_zone_info_hover,
    photosphere_info_hover, chromosphere_info_hover,
    inner_corona_info_hover, streamer_belt_info_hover,
    roche_limit_info_hover, alfven_surface_info_hover,
    outer_corona_info_hover, termination_shock_info_hover,
    solar_wind_info_hover,                      # heliopause hover (legacy name)
    inner_limit_oort_info_hover,                # inner_oort_limit hover (swapped naming)
    inner_oort_info_hover, outer_oort_info_hover,
    gravitational_influence_info_hover,
    # tooltip (Tk GUI, \n line breaks)
    core_info, radiative_zone_info, photosphere_info, chromosphere_info,
    inner_corona_info, streamer_belt_info, roche_limit_info, alfven_surface_info,
    outer_corona_info, termination_shock_info,
    solar_wind_info,                            # heliopause tooltip (legacy name)
    inner_limit_oort_info,                      # inner_oort_limit tooltip (swapped naming)
    inner_oort_info, outer_oort_info,
    gravitational_influence_info,
    # custom shell tooltips (source strings, not composed)
    hills_cloud_torus_info, outer_oort_clumpy_info, galactic_tide_info,
)

# Phase D1: Import Sun radius constants for radius_au expressions.
from planet_visualization_utilities import (
    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,
    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
    TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
)

# ============================================================
# SHELL_CONFIGS: sphere shells handled by build_sphere_shell()
# ============================================================
# Keys are bare shell names (no body prefix), matching the post-prefix-strip
# keys produced by the unified dispatch in planet_visualization.py.

SHELL_CONFIGS = {

    # ============================================================
    # Mercury
    # ============================================================
    # Source: NASA MESSENGER Mission, Margot et al. (2012), Sori (2018)
    # Verified: April 2026 via Gemini fact-check
    'Mercury': {

        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.41,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.<br>"
                "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about <br>"
                "1,000 kilometers thick based on Messenger findings (2019)."
            ),
            'tooltip': (
                "Inner Core: Mercury has a very large metallic core, unlike Earth's which is proportionally smaller.\n"
                "Evidence suggests that Mercury has a solid inner core, similar to Earth's. It is estimated to be about \n"
                "1,000 kilometers thick based on Messenger findings (2019)."
            ),
        },

        'outer_core': {
            'name': 'Outer Core',
            'radius_fraction': 0.85,
            'color': 'rgb(255, 140, 0)',
            'opacity': 0.8,
            'n_points': 25,
            'marker_size': 3.7,
            'info_border': 'white',  # two-standards (May 29, 2026): bright orange fill
            'hover_text': (
                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron <br>"
                "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
            ),
            'tooltip': (
                "Outer Core: Surrounding the solid inner core is a liquid metallic outer core. The movement of this molten iron \n"
                "is thought to be the source of Mercury's weak magnetic field. About 1074 km thick."
            ),
        },

        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.98,
            'color': 'rgb(230, 100, 20)',
            'opacity': 0.7,
            'n_points': 25,
            'marker_size': 3.4,
            'info_border': 'white',  # two-standards (May 29, 2026): burnt orange fill
            'hover_text': (
                "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of <br>"
                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than <br>"
                "Earth's, estimated to be only about 331 kilometers thick."
            ),
            'tooltip': (
                "Mantle: Surrounding the core is a rocky mantle. Recent research suggests this mantle might even contain a layer of \n"
                "diamonds, formed from ancient carbon-rich material under immense pressure. The mantle is significantly thinner than \n"
                "Earth's, estimated to be only about 331 kilometers thick."
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(128, 128, 128)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin <br>"
                "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, <br>"
                "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
            ),
            'tooltip': (
                "Mercury has a solid silicate crust that is heavily cratered, resembling Earth's Moon. The crust is likely quite thin \n"
                "compared to Earth's. There's also a theory that a significant portion of Mercury's crust might be made of diamonds, \n"
                "formed by billions of years of meteorite impacts on a graphite-rich surface. About 35 km thick."
            ),
        },

        'atmosphere': {
            'name': 'Exosphere',
            'radius_fraction': 2.0,
            'color': 'rgb(150, 200, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 2.5,
            'hover_text': (
                "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not <br>"
                "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, <br>"
                "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts.<br><br>"
                "Mercury has what is more accurately described as a tenuous exosphere rather than a substantial atmosphere like Earth's. <br>"
                "This exosphere is extremely thin, and its atoms are so sparse they are more likely to collide with the surface than with <br>"
                "each other. The extent of Mercury's exosphere is not well-defined by a pressure gradient as with a true atmosphere. Instead, <br>"
                "it gradually fades out into space. However, we can consider how far certain exospheric components have been observed:<br>"
                "* Sodium Tail: Due to solar radiation pressure, sodium atoms are pushed away from Mercury, forming a long, comet-like tail. <br>"
                "  This tail has been detected extending to distances of over 24 million kilometers (approximately 10,000 Mercury radii) <br>"
                "  from the planet. This is by far the most extended component of Mercury's exosphere.<br>"
                "* Other Elements: Other elements like hydrogen, helium, oxygen, potassium, calcium, and magnesium are also present in the <br>"
                "  exosphere. These are generally found much closer to the planet's surface, within a few Mercury radii. For instance, calcium <br>"
                "  and magnesium have been observed in the tail but at distances less than 8 Mercury radii.<br>"
                "In summary: While the bulk of Mercury's exospheric atoms are concentrated very close to the surface (within 1 Mercury radius), <br>"
                "the sodium tail is a significant feature that extends incredibly far, up to 10,000 Mercury radii. The main body of the exosphere <br>"
                "is very close to the surface, but the tenuous sodium tail stretches to an immense distance."
            ),
            'tooltip': (
                "Exosphere: Unlike Earth's substantial atmosphere, Mercury has an extremely thin exosphere. This exosphere is not \n"
                "dense enough to trap heat or offer significant protection from space. It is composed mostly of oxygen, sodium, \n"
                "hydrogen, helium, and potassium atoms that have been blasted off the surface by the solar wind and micrometeoroid impacts."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 94.4,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 1.0,
            'hover_text': (
                "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it <br>"
                "where its gravity is the dominant gravitational force. Mercury certainly has a Hill sphere, but its size depends on <br>"
                "its mass and its distance from the Sun. Being the closest planet to the Sun, the Sun's powerful gravity limits the <br>"
                "extent of Mercury's Hill sphere compared to planets farther out.<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>"
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>"
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>"
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>"
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>"
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Hill Sphere: Every celestial body has a Hill sphere (also known as the Roche sphere), which is the region around it \n"
                "where its gravity is the dominant gravitational force. Mercury's Hill sphere extends to about 94 Mercury radii."
            ),
        },

    },


    # ============================================================
    # Moon
    # ============================================================
    # Source: Weber et al. (2011), Science, "Seismic Detection of the Lunar Core";
    #         NASA Moon Fact Sheet; Apollo Seismic Experiment reports;
    #         NASA Solar System Dynamics (Hill sphere radius); Draper (1847).
    # Verified: April 2026 provenance audit; all 5 flagged claims confirmed.
    # Phase B correction: radius_fraction/opacity swap in mantle fixed
    #   (source had radius_fraction=0.85, opacity=0.9655; description text
    #   and lunar geometry confirm boundary at 0.9655 of Moon radius).
    'Moon': {

        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.1485,
            'color': 'rgb(255, 100, 0)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'info_border': 'white',  # two-standards (May 29, 2026): dense orange-red fill
            'hover_text': (
                "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon's wobble suggest:<br>"
                "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius:<br>"
                "  * Estimates for the temperature of the Moon's inner core vary slightly depending on the studies and methods used, but <br>"
                "    some more recent reanalyses of seismic data suggest temperatures around 1600-1700 K."
            ),
            'tooltip': (
                "The Moon has a small, partially molten core. Seismic data from Apollo missions and more recent studies of the Moon's wobble suggest:\n"
                "* Inner Core: Believed to be a solid, iron-rich core, roughly 240 kilometers in radius."
            ),
        },

        'outer_core': {
            'name': 'Outer Core',
            'radius_fraction': 0.2083,
            'color': 'rgb(255, 50, 0)',
            'opacity': 0.8,
            'n_points': 25,
            'marker_size': 3.7,
            'info_border': 'white',  # dense-red shell: shell-color fill, white outline (Tony's two-standards, May 28)
            'hover_text': (
                "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about <br>"
                "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core.<br>:"
                "* The Moon's outer core is generally understood to be hotter than its solid inner core, as it is in a molten or liquid <br>"
                "  state. <br>"
                "* Estimated Temperature: This layer would be slightly cooler than the inner core, but still hot enough to be molten at <br>"
                "  the lower pressures found here. Estimates typically fall around 1300 K to 1600 K. Let's use 1500 K as a representative <br>"
                "  value for the outer core for your model.<br>"
                "* Reasoning: As you move outwards, the temperature gradually decreases, but crucially, the pressure also decreases. At this <br>"
                "  depth and pressure, the temperature is above the melting point of the iron-rich material, allowing it to be liquid."
            ),
            'tooltip': (
                "Outer Core: Surrounding the inner core, this is thought to be a liquid, iron-rich outer core with a radius of about \n"
                "330 kilometers. There might also be a small, partially molten layer of silicates around the outer core."
            ),
        },

        # Corrected in Phase B: source had radius_fraction=0.85 and
        # opacity=0.9655 -- these were swapped. The description text states
        # the outer boundary of the mantle is at 1677.4 km / 1737.4 km = 0.9655
        # of lunar radius. The inline source comment ("55-85% of Earth's radius")
        # was a copy-paste from Earth, not Moon data.
        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.9655,
            'color': 'rgb(0, 50, 0)',
            'opacity': 0.7,
            'n_points': 25,
            'marker_size': 3.4,
            'hover_text': (
                "Above the core lies the Moon's mantle, which makes up the bulk of its interior:<br>"
                "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of <br>"
                "  elements. It's thought to be rich in olivine and pyroxene.<br>"
                "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially <br>"
                "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.<br>"
                "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected \"deep moonquakes\" originating in the mantle at <br>"
                "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth.<br>"
                "* The Moon's mantle is a thick, largely solid layer, and its temperature varies significantly with depth, becoming <br>"
                "  cooler as you move outwards towards the crust.<br>"
                "  * Estimates for the temperature at the boundary between the mantle and the outer core range from 1573 K to 1743 K.<br>"
                "  * Estimates for the crust-mantle boundary are roughly 623 K to 823 K.<br>"
                "* The \"Draper point\" is around 798 K, which is the approximate temperature at which all solids start to glow a dim <br>"
                "  red. At the crust-mantle boundary of the Moon (~623-823 K), the temperature is close to this value. This means the <br>"
                "  rock at the boundary might be just barely starting to glow, or it might not be quite hot enough depending on the exact <br>"
                "  temperature. However, Draper's discovery tells us about how materials emit light based on temperature. While the outer <br>"
                "  parts of the Moon's mantle are below the \"Draper Point\" and wouldn't visibly glow, the deeper parts of the mantle, <br>"
                "  closer to the core, would certainly be above the Draper Point and would emit a visible glow if we could somehow see <br>"
                "  them directly!<br>"
                "* Note: Outer boundary of the mantle (base of the crust) as a fraction of Rm: 1677.4 km / 1737.4 km = 0.9655."
            ),
            'tooltip': (
                "Above the core lies the Moon's mantle, which makes up the bulk of its interior:\n"
                "* Composition: Primarily composed of silicate rocks, similar to Earth's mantle, but with different proportions of \n"
                "  elements. It's thought to be rich in olivine and pyroxene.\n"
                "* State: The Moon's mantle is largely solid today. However, in its early history, it would have been at least partially \n"
                "  molten, leading to volcanic activity that formed the vast maria (dark plains) on the lunar surface.\n"
                "* Lunar Deep Moonquakes: Seismometers left by Apollo missions detected deep moonquakes originating in the mantle at \n"
                "  depths of 700 to 1,200 km (435-745 miles). These are likely caused by tidal stresses from Earth."
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(200, 200, 200)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
                "The Moon's crust is the outermost solid layer:<br>"
                "* Thickness: The crust varies in thickness, averaging about 50 km on the near side and about 60 km on the far side. <br>"
                "  Some regions, particularly under the large impact basins on the near side, can have crusts as thin as 20-30 km, while <br>"
                "  the far side highlands can have crusts exceeding 100 km.<br>"
                "* Composition: Predominantly composed of plagioclase feldspar (specifically anorthite), making it lighter in color and <br>"
                "  less dense than the mantle below. The distinction between the bright, heavily cratered \"highlands\" and the dark, <br>"
                "  smoother \"maria\" (lava plains) is a defining feature of the lunar surface.<br>"
                "* Surface Features: Heavily cratered due to billions of years of meteorite impacts. Significant features include vast <br>"
                "  impact basins (like the South Pole-Aitken Basin), mountain ranges, and rilles (channels).<br>"
                "* Space Weathering: The surface is constantly bombarded by micrometeorites and solar wind particles, which alter the <br>"
                "  physical and chemical properties of the outermost layer (regolith).<br>"
                "* Water Ice: Evidence from missions like the Lunar Reconnaissance Orbiter (LRO) and India's Chandrayaan-1 suggests the <br>"
                "  presence of water ice in permanently shadowed craters near the lunar poles.<br>"
                "* Regolith: Covered by a layer of fragmented rock and dust called regolith, typically ranging from a few meters deep <br>"
                "  on the maria to over 10 meters deep on the highlands.<br>"
                "* Tidal Locking: The Moon is tidally locked to Earth, meaning the same side always faces us. This creates a distinct <br>"
                "  difference between the near side (with many maria) and the far side (dominated by highlands)."
            ),
            'tooltip': (
                "The Moon's crust is the outermost solid layer:\n"
                "* Thickness: The crust varies in thickness, averaging about 50 km on the near side and about 60 km on the far side.\n"
                "* Composition: Predominantly composed of plagioclase feldspar (specifically anorthite), making it lighter in color and \n"
                "  less dense than the mantle below."
            ),
        },

        'exosphere': {
            'name': 'Exosphere',
            'radius_fraction': 1.06,
            'color': 'rgb(150, 200, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 2.5,
            'hover_text': (
                "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly <br>"
                "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with <br>"
                "each other.<br>"
                "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, <br>"
                "  hydrogen, and other elements.<br>"
                "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant <br>"
                "  shielding from solar radiation or micrometeoroids.<br>"
                "* Extent: The Moon's exosphere extends from the surface upward. It gradually thins out with altitude, but it's already <br>"
                "  incredibly thin at the surface. While it technically extends to the point where the density approaches that of the <br>"
                "  interplanetary medium, a practical upper limit might be a few hundred kilometers. For the region where it's most <br>"
                "  relevant or where density is higher, the exosphere is often considered to extend up to about 100 kilometers above <br>"
                "  the lunar surface. So, a more \"dense\" part of the exosphere extends from 1.0 Rm to roughly 1.06 Rm."
            ),
            'tooltip': (
                "The Moon essentially has no atmosphere in the traditional sense. Instead, it has an exosphere. It's an incredibly \n"
                "tenuous layer of gases, far less dense than a vacuum on Earth. It's so thin that gas molecules rarely collide with \n"
                "each other.\n"
                "* Composition: Primarily composed of noble gases like argon and helium, along with trace amounts of sodium, potassium, \n"
                "  hydrogen, and other elements.\n"
                "* No Weather: Due to its extreme thinness, there's no atmospheric pressure, no wind, no weather, and no significant \n"
                "  shielding from solar radiation or micrometeoroids."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 34.53,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 1.0,
            'hover_text': (
                "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity <br>"
                "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an <br>"
                "object is outside the Moon's Hill sphere, it would typically end up orbiting Earth instead of the Moon.<br>"
                "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii."
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n\n"
                "The Moon's Hill sphere (also known as the Roche sphere in this context) is the region around it where its own gravity \n"
                "is the dominant force attracting satellites, as opposed to the much stronger gravitational pull of the Earth. If an \n"
                "object is outside the Moon's Hill sphere, it would typically end up orbiting Earth instead of the Moon.\n"
                "* The estimated radius of the Moon's Hill sphere is approximately 60,000 kilometers, approximately 34.53 lunar radii."
            ),
        },

    },

    # ============================================================
    # Planet 9 (hypothetical)
    # ============================================================
    # Source: Batygin & Brown (2016, 2021); Fortney et al. (2016);
    #         NASA Solar System Exploration.
    #         All values are model predictions for a 5-10 Earth-mass ice giant;
    #         Planet Nine has not been observationally confirmed.
    # Verified: April 2026 provenance audit; 2 corrections applied (Eris typo,
    #           2021 semi-major axis refinement note).
    'Planet 9': {

        'surface': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(83, 68, 55)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Planet 9 Surface<br>"
                "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
                "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth <br>"
                "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the <br>"
                "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a <br>"
                "smaller version.<br>"
                "* Mass and Density Relationship: For a given mass, the radius of a planet is strongly influenced by its density.<br>"
                "* Terrestrial Planets: Terrestrial planets (like Earth, Mars, Venus, Mercury) are primarily composed of rock and metal, <br>"
                "  making them quite dense. If Planet Nine were a terrestrial planet with 5-10 times the mass of Earth, its radius would <br>"
                "  likely be significantly smaller than 3-4 Earth radii due to its high density.<br>"
                "* Gas Giants: Gas giants (like Jupiter and Saturn) are composed mostly of hydrogen and helium, making them very large and <br>"
                "  not very dense. A planet with several Earth masses composed primarily of these light gases would have a much larger radius <br>"
                "  than 3-4 Earth radii.<br>"
                "* Ice Giants: Ice giants (like Uranus and Neptune) have a composition that includes heavier elements like oxygen, carbon, <br>"
                "  nitrogen, and sulfur, often in the form of water, methane, and ammonia ices, along with a significant amount of hydrogen and <br>"
                "  helium. This composition results in densities higher than gas giants but lower than terrestrial planets.<br>"
                "The 3-4 Earth radii estimate, particularly the 3.7 Earth radii figure, comes from models that assume Planet Nine has a mass <br>"
                "around 5-10 Earth masses and an internal composition similar to Uranus and Neptune. These models predict that such a planet <br>"
                "would have a larger radius than Earth due to its significant mass, but not as large as a pure gas giant with the same mass due <br>"
                "to the presence of heavier \"ice\" materials. Therefore, the estimated radius of 3-4 Earth radii strongly suggests that Planet <br>"
                "Nine, if it exists, is likely an ice giant or a sub-Neptune type of planet, rather than a rocky terrestrial planet or a large <br>"
                "gas giant. This is also consistent with theories about how a planet could have formed or been captured in the distant outer <br>"
                "solar system."
            ),
            'tooltip': (
                "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
                "4.6 MB PER FRAME FOR HTML.\n\n"
                "The estimation of Planet Nine's radius being between 3 and 4 Earth radii, with a specific estimate of around 3.7 Earth \n"
                "radii (or 23,500 - 24,000 km), appears in several scientific discussions. This size estimate is often linked to the \n"
                "assumption that Planet Nine is likely an ice giant, similar in composition to Uranus and Neptune, but potentially a \n"
                "smaller version."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 48000,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.<br><br>"
                "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br><br>"
                "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU.<br>"
                "To arrive at the Hill sphere estimate of 7.6 AU, we made the following key assumptions about Planet Nine: <br>"
                "* Semi-major axis (a): We assumed a semi-major axis of 600 AU. This value is within the range of 500-700 AU suggested <br>"
                "  by some studies, including those considering the IRAS/AKARI observations. Note: 2021 refinements by Batygin & Brown <br>"
                "  favor a slightly closer orbit (~460 AU central estimate). The semi-major axis has a direct linear relationship with <br>"
                "  the Hill sphere radius. A larger semi-major axis leads to a larger Hill sphere.<br>"
                "* Eccentricity (e): We assumed an eccentricity of 0.30 (range 0.15-0.40 in newer models). This gives a perihelion <br>"
                "  around 280 AU and an aphelion around 1120 AU. The eccentricity affects the Hill sphere radius because the formula <br>"
                "  uses the distance to the Sun at the perihelion. A higher eccentricity would result in a smaller Hill sphere radius.<br>"
                "* Mass of Planet Nine (m): We assumed a mass of 6 times the mass of Earth. This is the current 'sweet spot' estimate <br>"
                "  from Batygin & Brown (2021), revised down from the original 10 Earth mass prediction. The mass has a cubic root <br>"
                "  relationship with the Hill sphere radius.<br>"
                "* Mass of the Sun (M): We used the standard value for the mass of the Sun. This is a well-established constant.<br>"
                "* In summary: the region where Planet 9's gravity is strong enough to hold onto its own moons despite the Sun's pull is <br>"
                "  what the Hill sphere represents."
            ),
            'tooltip': (
                "SELECT MANUAL SCALE OF AT LEAST 8 AU TO VISUALIZE PLANET 9 CENTERED OR 800 AU HELIOCENTRIC.\n"
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Hill Sphere: Planet 9's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \n"
                "over the Sun's. The radius of Planet 9's Hill sphere is very large, approximately 7.6 AU."
            ),
        },

    },

    # ============================================================
    # Pluto
    # ============================================================
    'Pluto': {

        'core': {
            'name': 'Core',
            'radius_fraction': 0.70,
            'color': 'rgb(255, 56, 0)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'info_border': 'white',  # dense-red shell: shell-color fill, white outline (Tony's two-standards, May 28)
            'hover_text': (
                "Pluto core: Scientists believe Pluto has a dense, rocky core, likely composed of silicates and iron. The core's diameter <br>" 
                "is hypothesized to be about 1700 km, which is approximately 70% of Pluto's total diameter. Heat generated from the decay <br>" 
                "of radioactive elements within the core may still be present today.<br>" 
                "* Radioactive Isotopes: Based on theoretical models and our understanding of its composition and formation, scientists have made <br>" 
                "  estimations. Pluto's density suggests it differentiated early in its history, forming a rocky core and an icy mantle. <br>" 
                "  This differentiation process itself would have released heat. Like other rocky bodies in our solar system, Pluto's core <br>" 
                "  likely contains radioactive isotopes such as Uranium-238, Uranium-235, Thorium-232, and Potassium-40. The decay of these <br>" 
                "  elements over billions of years generates heat within the core. This is considered a primary source of its internal heat.<br>" 
                "* Initial Accretional Heat: The heat generated from the collisions of smaller bodies that accreted to form Pluto would have <br>" 
                "  also contributed to its initial core temperature. While much of this heat would have dissipated over time, some likely remains.<br>" 
                "* Subsurface Ocean Evidence: The potential presence of a subsurface liquid water ocean beneath Pluto's icy mantle suggests that <br>" 
                "  the core is warm enough to prevent this ocean from completely freezing. The heat flow from the core would be crucial for <br>" 
                "  maintaining this liquid layer.<br>" 
                "* Estimated Temperature: The estimated temperature of Pluto's core is around 1000 K. This estimate comes from models that <br>" 
                "  consider the heat generated by radioactive decay within a rocky core. These models also need to account for the heat transfer <br>" 
                "  through the icy mantle. Future research and more detailed data could refine this value. The exact temperature would depend on <br>" 
                "  the precise composition of the core and the efficiency of heat transfer through the mantle. In comparison, the surface <br>" 
                "  temperature of Pluto is extremely cold, around 40 K. The significant difference highlights the internal heating processes at <br>" 
                "  work within the dwarf planet. "
            ),
            'tooltip': (
                "2.4 MB PER FRAME FOR HTML.\n\n"
                "Pluto core: Scientists believe Pluto has a dense, rocky core, likely composed of silicates and iron. The core's diameter \n" 
                "is hypothesized to be about 1700 km, which is approximately 70% of Pluto's total diameter. Heat generated from the decay \n" 
                "of radioactive elements within the core may still be present today."
            ),
        },

        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.99,
            'color': 'rgb(150, 0, 0)',
            'opacity': 0.9,
            'n_points': 25,
            'marker_size': 3.5,
            'info_border': 'white',  # dense-red shell: shell-color fill, white outline (Tony's two-standards, May 28)
            'hover_text': (
                "mantle: Surrounding the rocky core is a mantle made of water ice. There's a compelling theory that a subsurface ocean <br>" 
                "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean <br>" 
                "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto's surface.<br>" 
                "* This layer is primarily water ice. Within this icy mantle, there is strong evidence for a subsurface ocean of liquid <br>" 
                "  water, potentially mixed with ammonia, located above the rocky core.<br>" 
                "* Inner Icy Layer (if ocean exists): A layer of solid water ice may exist directly above the rocky core, potentially <br>" 
                "  forming the bottom of the ocean.<br>" 
                "* Subsurface Ocean: A layer of liquid water (possibly with dissolved substances). The thickness of this ocean is estimated <br>" 
                "  to be potentially 100 to 180 kilometers.<br>" 
                "* Outer Icy Layer (Lithosphere): A rigid outer shell of water ice above the potential ocean (or the main icy mantle if no <br>" 
                "  ocean is present). This layer is thought to be significant in thickness, potentially ranging from 45 to several hundred <br>" 
                "  kilometers."
            ),
            'tooltip': (
                "2.1 MB PER FRAME FOR HTML.\n\n"
                "Mantle: Surrounding the rocky core is a mantle made of water ice. There's a compelling theory that a subsurface ocean \n" 
                "of liquid water, possibly mixed with ammonia, exists at the boundary between the core and the ice mantle. This ocean \n" 
                "could be 100 to 180 km thick. The presence of this ocean is supported by geological features observed on Pluto's surface."
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(83, 68, 55)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Pluto Crust<br>" 
                "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
                "Crust (Surface Layer): This is the outermost layer, composed of more volatile ices: primarily nitrogen ice, with smaller <br>" 
                "amounts of methane and carbon monoxide ice. The thickness of this layer likely varies but is estimated to be relatively <br>" 
                "thin in many regions, perhaps ranging from a few to tens of kilometers. In the deep Sputnik Planitia basin, the nitrogen <br>" 
                "ice layer is estimated to be several kilometers thick and overlies the water-ice lithosphere.<br>" 
                "* Pluto's surface, or crust, is composed of various ices, primarily nitrogen ice (over 98%). It also contains smaller <br>" 
                "  amounts of methane and carbon monoxide ices.<br>" 
                "* Interestingly, mountains on Pluto can reach heights comparable to the Rocky Mountains on Earth and are believed to be <br>" 
                "  made of water ice, which is strong enough to support such structures at Pluto's frigid temperatures. These water-ice <br>" 
                "  mountains likely \"float\" in the denser nitrogen ice.<br>" 
                "* The surface exhibits a wide range of colors and brightness, with features like the bright \"heart\" (Tombaugh Regio) and <br>" 
                "  dark regions like Cthulhu Macula (\"the Whale\").<bR>" 
                "* Sputnik Planitia, the western lobe of the \"heart,\" is a vast basin of nitrogen and carbon monoxide ices showing <br>" 
                "  evidence of convection cells and glacial flow. The lack of impact craters in this region suggests it's geologically <br>" 
                "  young (possibly less than 10 million years old)."
            ),
            'tooltip': (
                "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
                "4.6 MB PER FRAME FOR HTML.\n\n"
                "Crust (Surface Layer): This is the outermost layer, composed of more volatile ices: primarily nitrogen ice, with smaller\n" 
                "amounts of methane and carbon monoxide ice. The thickness of this layer likely varies but is estimated to be relatively \n" 
                "thin in many regions, perhaps ranging from a few to tens of kilometers. In the deep Sputnik Planitia basin, the nitrogen \n" 
                "ice layer is estimated to be several kilometers thick and overlies the water-ice lithosphere."
            ),
        },

        'haze_layer': {
            'name': 'Haze Layer',
            'radius_fraction': 1.17,
            'color': 'rgb(135, 206, 235)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': (
                "Haze Layer: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed <br>" 
                "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes <br>" 
                "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. <br>" 
                "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of <br>" 
                "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy <br>" 
                "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature <br>" 
                "inversion, possibly caused by the presence of methane.<br>" 
                "* Composition and Formation: Pluto's atmosphere is primarily nitrogen (N2) with smaller amounts of methane (CH4) and <br>" 
                "  carbon monoxide (CO). The haze is thought to form when ultraviolet sunlight and high-energy radiation (like cosmic <br>" 
                "  rays) break apart methane molecules in the upper atmosphere. This breakdown leads to the formation of more complex <br>" 
                "  hydrocarbon gases, such as acetylene (C2H2) and ethylene (C2H4), as well as heavier compounds called tholins. As these <br>" 
                "  hydrocarbons drift to the lower, colder parts of the atmosphere, they condense into tiny ice particles, forming the haze. <br>" 
                "  Continued exposure to ultraviolet sunlight then chemically converts these haze particles into the dark, reddish-brown tholins <br>" 
                "  that contribute to the color of Pluto's surface.<br>" 
                "* Structure and Extent: The New Horizons mission revealed a surprisingly complex, multi-layered haze extending up to 200 km or <br>" 
                "  more above Pluto's surface. Scientists have observed as many as 20 distinct layers of haze. These layers can extend <br>" 
                "  horizontally for hundreds of kilometers and are not always perfectly parallel to the surface. There can be variations in haze <br>" 
                "  density and layer structure with altitude and even geographic location on Pluto.<br>" 
                "* Color: The haze has a blue tint when viewed in backlit images (like those taken as New Horizons sped away). This blue color <br>" 
                "  arises because the small haze particles efficiently scatter blue light from the sun.<br>" 
                "* Particle Settling: The haze particles eventually settle out of the atmosphere and onto Pluto's surface, contributing to the <br>" 
                "  surface composition and color over time.<br>" 
                "* Condensation and Coagulation: As particles descend, they can grow through condensation of atmospheric gases onto them and by <br>" 
                "  sticking together (coagulation).<br>" 
                "* Temperature Regulation: By absorbing infrared light, the haze can influence the atmospheric temperature profile, potentially <br>" 
                "  keeping the upper atmosphere cooler than it otherwise would be.<br>" 
                "* Haze Layers: Within the lower atmosphere, haze layers extend up to about 200 km altitude. This is approximately: ~0.17 So, <br>" 
                "  the distinct haze layers reach about 0.17 Pluto radii above the surface." 
            ),
            'tooltip': (
                "2.7 MB PER FRAME FOR HTML.\n\n"
                "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed \n" 
                "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes \n" 
                "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. \n" 
                "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of \n" 
                "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy \n" 
                "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature \n" 
                "inversion, possibly caused by the presence of methane."
            ),
        },

        'atmosphere': {
            'name': 'Atmosphere',
            'radius_fraction': 1.43,
            'color': 'rgb(240, 245, 250)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': (
                "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed <br>" 
                "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes <br>" 
                "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. <br>" 
                "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of <br>" 
                "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy <br>" 
                "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature <br>" 
                "inversion, possibly caused by the presence of methane.<br>" 
                "The extent of Pluto's atmosphere is surprisingly large relative to the dwarf planet itself. While it's very thin in terms <br>" 
                "of density compared to Earth's, it stretches far out into space. Here's a breakdown in terms of Pluto's radius <br>" 
                "(approximately 1188 km):<br>" 
                "* Significant Atmosphere: The atmosphere, composed primarily of nitrogen with traces of methane and carbon monoxide, has <br>" 
                "  been detected extending up to 1700 km above the surface (the exobase).<br>" 
                "* In Pluto radii: To express this as a fraction of Pluto's radius: ~1.43.<br>" 
                "* Outer Limits: Some research suggests that the outer, most tenuous parts of Pluto's atmosphere might extend even further, <br>" 
                "  perhaps to several times Pluto's radius, gradually merging with the vacuum of space. One New Horizons science brief even <br>" 
                "  mentioned an outer limit potentially as far as seven times Pluto's radius, although this is very ill-defined.<br>" 
                "* Haze Layers: Within the lower atmosphere, haze layers extend up to about 200 km altitude. This is approximately: ~0.17 So, <br>" 
                "  the distinct haze layers reach about 0.17 Pluto radii above the surface.<br>" 
                "In summary, while the bulk of Pluto's atmosphere is very thin, its outer reaches are quite extended. For a general extent, <br>" 
                "considering the exobase, the atmosphere reaches about 0.43 Pluto radii above the surface, or 1.43 Pluto radii from the center. <br>" 
                "If you consider the more diffuse outer limits, it could be even larger."
            ),
            'tooltip': (
                "2.7 MB PER FRAME FOR HTML.\n\n"
                "Atmosphere: Pluto has a very thin atmosphere, about 1/100,000th the surface pressure of Earth's. It's primarily composed \n" 
                "of nitrogen (N2), with smaller amounts of methane (CH4) and carbon monoxide (CO). This atmosphere is dynamic and changes \n" 
                "with Pluto's orbit around the Sun. As Pluto moves farther away, the atmosphere freezes and falls to the surface as ice. \n" 
                "When it's closer to the Sun, the surface ice sublimates, forming a gaseous atmosphere. The atmosphere contains layers of \n" 
                "haze, extending up to 200 km above the surface, likely formed from the interaction of the atmospheric gases with high-energy \n" 
                "radiation. Counterintuitively, Pluto's upper atmosphere is significantly warmer than its surface due to a temperature \n" 
                "inversion, possibly caused by the presence of methane."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 4685,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "SET MANUAL SCALE OF AT LEAST 0.05 AU TO VISUALIZE.<br><br>"
                "Hill Sphere: Pluto's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates <br>" 
                "over the Sun's. The radius of Pluto's Hill sphere is quite large, approximately 5.99 million kilometers (0.04 AU). This is <br>" 
                "significantly larger than Earth's Hill sphere in terms of volume. Any moon orbiting Pluto within this sphere is <br>" 
                "gravitationally bound to it. Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra, all of which reside within <br>" 
                "its Hill sphere."          
            ),
            'tooltip': (
                "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.\n" 
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Hill Sphere: Pluto's Hill sphere, or Roche sphere, is the region around it where its gravitational influence dominates \n" 
                "over the Sun's. The radius of Pluto's Hill sphere is quite large, approximately 5.99 million kilometers (0.04 AU). This is \n" 
                "significantly larger than Earth's Hill sphere in terms of volume. Any moon orbiting Pluto within this sphere is \n" 
                "gravitationally bound to it. Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra, all of which reside within \n" 
                "its Hill sphere."                     
            ),
        },
    },


    # ============================================================
    # Eris
    # ============================================================
    'Eris': {

        'core': {
            'name': 'Core',
            'radius_fraction': 0.60,
            'color': 'rgb(187, 63, 63)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'info_border': 'white',  # dense-red shell: shell-color fill, white outline (Tony's two-standards, May 28)
            'hover_text': (
                "Eris, a dwarf planet in the Kuiper Belt, has a structure that scientists have been piecing together through observations <br>" 
                "and theoretical modeling. Here's what we currently understand:<br>" 
                "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests that it is composed <br>" 
                "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive <br>" 
                "elements, which produce internal heat.<br>" 
                "* Determining the precise radius fraction of Eris's core is challenging because we don't have direct observations of its <br>" 
                "  internal structure. However, we can make estimations based on its known properties:<br>" 
                "  * Total Radius: Eris has a radius of approximately 1163 +/- 6 kilometers.<br>" 
                "  * Density: Its density is estimated to be around 2.52 +/- 0.07 g/cm^3. This high density suggests a significant rocky component.<br>" 
                "  * Compositional Models: Based on its density, scientists believe Eris is composed largely of rock (possibly over 85% of its <br>" 
                "    mass) with the remainder being primarily water ice. The ice forms the mantle surrounding the rocky core.<br>" 
                "* Considering these factors, and drawing comparisons to other icy bodies with rocky cores like Europa or Ganymede in the outer <br>" 
                "  solar system, a reasonable estimate for the radius fraction of Eris's core would likely be around 50-65% of its total radius. <br>" 
                "  To achieve Eris's high bulk density with a significant ice mantle, the denser rocky core must occupy a substantial portion of <br>" 
                "  its volume. If the core were much smaller (a smaller radius fraction), the overall density would likely be lower, given the <br>" 
                "  lower density of water ice. Conversely, if the core occupied a much larger fraction, there would be less room for the <br>" 
                "  substantial ice mantle that is believed to exist. Therefore, while we don't have a definitive number, the rocky core of Eris <br>" 
                "  likely makes up roughly half to two-thirds of its total radius.<br>" 
                "* Temperature:<br>" 
                "  * Radiogenic Heating: The rocky core of Eris likely contains radioactive isotopes (such as uranium, thorium, and <br>" 
                "    potassium) that decay over time, releasing heat.<br>" 
                "  * Recent research based on data from the James Webb Space Telescope provides indirect evidence for a warm, potentially <br>" 
                "    even hot, rocky core in Eris. The detection of a moderate deuterium-to-hydrogen (D/H) ratio in methane ice on its surface <br>" 
                "    suggests that the methane was likely produced through geochemical processes in the interior, requiring elevated <br>" 
                "    temperatures (possibly above 150 degC or 300 degF) within the rocky core. Theoretical modeling of Eris's interior, considering <br>" 
                "    radiogenic heating and thermal conductivity, suggests that the central temperature could have been as high as 875 K.<br>" 
                "  * This warmth might even be sufficient to support a subsurface ocean at the core-mantle boundary."
            ),
            'tooltip': (
                "2.4 MB PER FRAME FOR HTML.\n\n"
                "Eris, a dwarf planet in the Kuiper Belt, has a structure that scientists have been piecing together through observations \n" 
                "and theoretical modeling. Here's what we currently understand:\n" 
                "Core: Eris is believed to have a rocky core. Its high bulk density (around 2.5 g/cm^3) suggests that it is composed \n" 
                "primarily of rock, making up a significant portion of its mass (possibly over 85%). This core likely contains radioactive \n" 
                "elements, which produce internal heat."
            ),
        },

        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.66,
            'color': 'rgb(150, 0, 0)',
            'opacity': 0.9,
            'n_points': 25,
            'marker_size': 3.5,
            'info_border': 'white',  # dense-red shell: shell-color fill, white outline (Tony's two-standards, May 28)
            'hover_text': (
                "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto's ice shell, Eris's ice <br>" 
                "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near <br>" 
                "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice <br>" 
                "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface <br>" 
                "ocean within Eris.<br>"
            ),
            'tooltip': (
                "2.1 MB PER FRAME FOR HTML.\n\n"
                "Mantle: Surrounding the rocky core is a substantial mantle made of water ice. Unlike Pluto's ice shell, Eris's ice \n" 
                "mantle is thought to be convecting. This means that the warmer ice closer to the core rises, while the colder ice near \n" 
                "the surface sinks, a process that helps dissipate the internal heat generated by the core. The thickness of this ice \n" 
                "shell is estimated to be around 100 kilometers. There is currently no evidence to suggest the presence of a subsurface \n" 
                "ocean within Eris."
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(240, 240, 240)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Eris Crust<br>" 
                "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
                "Crust: The outermost layer is a crust of frozen gases, primarily nitrogen and methane ice. Eris has a very high albedo <br>" 
                "(reflectivity), reflecting about 96% of the sunlight that hits it. This bright surface is likely due to a frost layer <br>" 
                "formed from the condensation of its atmosphere when it is far from the Sun.<br>" 
                "* The optical color of Eris is primarily characterized by its very high albedo, meaning it reflects a large percentage <br>" 
                "  of the sunlight that hits it (around 96%). This high reflectivity is due to a relatively fresh layer of frozen nitrogen <br>" 
                "  and methane on its surface. The color is largely that of the illuminating source (the Sun). <br>" 
                "* Atmospheric effects (if any): Although its atmosphere is currently thought to be very thin or mostly frozen, any past or <br>" 
                "  transient atmosphere could have slightly altered the light scattering and thus the observed color."
            ),
            'tooltip': (
                "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
                "4.6 MB PER FRAME FOR HTML.\n\n"
                "Crust: The outermost layer is a crust of frozen gases, primarily nitrogen and methane ice. Eris has a very high albedo \n" 
                "(reflectivity), reflecting about 96% of the sunlight that hits it. This bright surface is likely due to a frost layer \n" 
                "formed from the condensation of its atmosphere when it is far from the Sun."
            ),
        },

        'atmosphere': {
            'name': 'Atmosphere',
            'radius_fraction': 1.005,
            'color': 'rgb(240, 245, 250)',
            'opacity': 0.1,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': (
                "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. When Eris is at its farthest point from the Sun <br>" 
                "(aphelion), the extremely cold temperatures cause its atmosphere, likely composed of nitrogen and methane, to freeze <br>" 
                "and fall as snow onto the surface. As Eris moves closer to the Sun in its highly elliptical orbit (perihelion), the <br>" 
                "surface warms up, and these ices sublimate, potentially creating a temporary atmosphere similar to Pluto's. However, <br>" 
                "observations have placed a very low upper limit on the current atmospheric pressure, suggesting it is currently very <br>" 
                "thin or mostly frozen.<br>" 
                "* The current understanding of Eris's atmosphere is that it is extremely tenuous, with an upper limit on surface <br>" 
                "  pressure of about 1 nanobar. This is about 10,000 times thinner than Pluto's current atmosphere. Given such a low <br>" 
                "  pressure, the extent of the atmosphere in terms of Eris's radii would be very small and likely not easily definable <br>" 
                "  in a significant way.<br>" 
                "* Near-Surface Existence: At such low pressures, the \"atmosphere\" is likely confined to a very thin layer near the <br>" 
                "  surface. The density of gas molecules would drop off extremely rapidly with altitude.<br>" 
                "* Collapse at Aphelion: Eris is currently near its aphelion (farthest point from the Sun). At these extremely cold <br>" 
                "  temperatures (around -240 degC), the primary atmospheric constituents, nitrogen and methane, would freeze and deposit <br>" 
                "  as frost on the surface. Any atmosphere present would be minimal.<br>" 
                "* Potential Sublimation at Perihelion: As Eris gets closer to the Sun (perihelion), the surface temperature will increase <br>" 
                "  slightly, potentially causing some of these ices to sublimate and form a transient, thin atmosphere. However, even in <br>" 
                "  this case, the extent is not expected to be a significant fraction of Eris's radius. In practical terms, the extent of <br>" 
                "  Eris's atmosphere in radii is considered negligible for most structural considerations. Scientists often discuss the <br>" 
                "  surface composition and potential for a thin, dynamic atmosphere rather than a significant, extended gaseous envelope. <br>" 
                "* To put it in perspective: if Eris had an atmosphere that extended even a few kilometers, that would be a tiny fraction <br>" 
                "  (less than 0.01) of its total radius. The current observational limits suggest it's likely much less than that for a <br>" 
                "  sustained atmosphere at its current distance from the Sun."
            ),
            'tooltip': (
                "2.7 MB PER FRAME FOR HTML.\n\n"
                "Atmosphere: Eris has a very tenuous atmosphere that is dynamic. When Eris is at its farthest point from the Sun \n" 
                "(aphelion), the extremely cold temperatures cause its atmosphere, likely composed of nitrogen and methane, to freeze \n" 
                "and fall as snow onto the surface. As Eris moves closer to the Sun in its highly elliptical orbit (perihelion), the \n" 
                "surface warms up, and these ices sublimate, potentially creating a temporary atmosphere similar to Pluto's. However, \n" 
                "observations have placed a very low upper limit on the current atmospheric pressure, suggesting it is currently very \n" 
                "thin or mostly frozen."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 6965,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "SET MANUAL SCALE OF AT LEAST 0.05 AU TO VISUALIZE.<br><br>"
                "Hill Sphere: The Hill sphere, or Roche sphere, of Eris is the region around it where its own gravity is the dominant <br>" 
                "force attracting satellites. At Eris's average orbital distance (~67.8 AU), the Hill sphere radius is approximately <br>" 
                "9.4 million kilometers (~0.06 AU). The shell shown here uses the perihelion distance (~38 AU), giving ~8.1 million km. <br>" 
                "Dysnomia orbits at ~37,000 km, well within either estimate.<br>" 
                "* The region where Eris's gravity is the dominant force attracting satellites extends to a distance of roughly 6965 <br>" 
                "  Eris radii from its center (perihelion-based)."          
            ),
            'tooltip': (
                "SELECT MANUAL SCALE OF AT LEAST 0.1 AU TO VISUALIZE.\n" 
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Hill Sphere: At Eris's average orbital distance (~67.8 AU), the Hill sphere radius is approximately \n" 
                "9.4 million kilometers (~0.06 AU). The shell shown uses the perihelion distance (~38 AU), \n" 
                "giving ~8.1 million km. Dysnomia orbits at ~37,000 km, well within either estimate."
            ),
        },
    },



    # ============================================================
    # Venus
    # ============================================================
    'Venus': {

        'core': {
            'name': 'Core',
            'radius_fraction': 0.5,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "Scientists infer that Venus has a central core, likely composed primarily of iron and nickel, similar to Earth's. <br>" 
                "Its radius is estimated to be around 3,200 km. Due to the lack of a strong magnetic field, it's speculated that Venus's <br>" 
                "core might be solid or only partially liquid, or that Venus's very slow rotation (243 days) prevents the convection <br>" 
                "needed to drive a magnetic dynamo. The exact state and dynamics of Venus's core remain a topic of ongoing research."
            ),
            'tooltip': (
                "Scientists infer that Venus has a central core, likely composed primarily of iron and nickel, similar to Earth's. \n" 
                "Its radius is estimated to be around 3,200 km. Due to the lack of a strong magnetic field, it's speculated that Venus's \n" 
                "core might be solid or only partially liquid, or that Venus's very slow rotation (243 days) prevents the convection \n" 
                "needed to drive a magnetic dynamo. The exact state and dynamics of Venus's core remain a topic of ongoing research."
            ),
        },

        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.98,
            'color': 'rgb(230, 100, 20)',
            'opacity': 0.7,
            'n_points': 25,
            'marker_size': 3.4,
            'info_border': 'white',  # two-standards (May 29, 2026): burnt orange fill
            'hover_text': (
                "Surrounding the core is a mantle made of hot, dense silicate rock, much like Earth's mantle. It's believed that heat <br>" 
                "generated by radioactive decay within Venus drives slow convection currents in the mantle. These currents are thought <br>" 
                "to be responsible for the planet's volcanism and tectonic activity, albeit different from Earth's plate tectonics"
            ),
            'tooltip': (
                "Surrounding the core is a mantle made of hot, dense silicate rock, much like Earth's mantle. It's believed that heat \n" 
                "generated by radioactive decay within Venus drives slow convection currents in the mantle. These currents are thought \n" 
                "to be responsible for the planet's volcanism and tectonic activity, albeit different from Earth's plate tectonics"
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(255, 255, 224)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Venus Crust<br>" 
                "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
                "Venus has a crust primarily made of basalt rock, with an estimated thickness ranging from about 10 to 30 kilometers, <br>" 
                "possibly thicker in the highland regions. Unlike Earth, Venus does not appear to have plate tectonics. Instead, its <br>" 
                "surface is mostly a single, continuous plate. The heat from the mantle escapes through volcanic activity, which is <br>" 
                "widespread across the planet, leading to periodic resurfacing events on a global scale."
            ),
            'tooltip': (
                "Venus has a crust primarily made of basalt rock, with an estimated thickness ranging from about 10 to 30 kilometers, \n" 
                "possibly thicker in the highland regions. Unlike Earth, Venus does not appear to have plate tectonics. Instead, its \n" 
                "surface is mostly a single, continuous plate. The heat from the mantle escapes through volcanic activity, which is \n" 
                "widespread across the planet, leading to periodic resurfacing events on a global scale."
            ),
        },

        'atmosphere': {
            'name': 'Lower Atmosphere',
            'radius_fraction': 1.01,
            'color': 'rgb(150, 200, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 2.5,
            'hover_text': (
                "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth's atmosphere at the surface. It is <br>" 
                "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, <br>" 
                "including sulfuric acid clouds that completely enshroud the planet. This thick, CO2-rich atmosphere creates a runaway <br>" 
                "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464 degC. The <br>" 
                "upper atmosphere exhibits a phenomenon called \"super-rotation,\" where winds blow much faster than the planet's slow <br>" 
                "rotation.<br><br>"
                "The \"lower atmosphere\" of Venus is generally considered to be the troposphere, which extends from the surface up to <br>" 
                "an altitude of approximately 60 kilometers. This region contains the dense, hot air and the main cloud layers."
            ),
            'tooltip': (
                "Venus boasts an extremely dense atmosphere, about 90 times the pressure of Earth's atmosphere at the surface. It is \n" 
                "composed primarily of carbon dioxide (about 96.5%) and nitrogen (about 3.5%), with trace amounts of other gases, \n" 
                "including sulfuric acid clouds that completely enshroud the planet. This thick, CO2-rich atmosphere creates a runaway \n" 
                "greenhouse effect, making Venus the hottest planet in our solar system with surface temperatures around 464 degC. The \n" 
                "upper atmosphere exhibits a phenomenon called \"super-rotation,\" where winds blow much faster than the planet's slow \n" 
                "rotation."
            ),
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'radius_fraction': 1.08,
            'color': 'rgb(100, 150, 255)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "The upper atmosphere of Venus is a complex and dynamic region extending far beyond the troposphere. It doesn't have the <br>" 
                "same distinct layers (stratosphere, mesosphere, thermosphere) as Earth's in the same way due to the very different thermal <br>" 
                "structure and composition. However, we can broadly consider the regions above the main cloud deck (around 70 km) as the <br>" 
                "upper atmosphere. Here's a look at some key parts of the upper atmosphere and their approximate extents:<br>" 
                "* Mesosphere (approximately 60 km to 90-100 km): Above the main cloud layers, the temperature starts to decrease with <br>" 
                "  altitude. This region is considered the mesosphere. It's a transition zone between the lower, rapidly rotating atmosphere <br>" 
                "  and the upper atmosphere where solar radiation plays a more dominant role. Extent in Venus radii: The top of this layer is <br>" 
                "  around 90-100 km. So, the mesosphere extends up to about 1.5-1.6% of Venus's radius.<br>" 
                "* Thermosphere (approximately 90-100 km to 200+ km): Above the mesosphere, the temperature increases significantly with <br>" 
                "  altitude due to the absorption of solar extreme ultraviolet (EUV) radiation. This is the thermosphere. Unlike Earth's <br>" 
                "  thermosphere, Venus's thermosphere is surprisingly cold, with average temperatures around 300 K (27 degC), and even colder on <br>" 
                "  the night side (the \"cryosphere\" around 90-120 km can reach extremely low temperatures). This is due to efficient <br>" 
                "  radiative cooling by carbon dioxide. The thermosphere is also where significant day-night differences in temperature and <br>" 
                "  density occur due to Venus's slow rotation. A global circulation pattern moves hot air from the dayside to the nightside <br>" 
                "  at high altitudes. Extent in Venus radii: The thermosphere extends to at least 200 km, and potentially much higher, gradually <br>" 
                "  thinning into the exosphere. So, the thermosphere extends to at least 3.3% of Venus's radius.<br>" 
                "* Ionosphere (approximately 120 km to several hundred km): Within the thermosphere and extending into the exosphere lies the <br>" 
                "  ionosphere, a region where solar radiation has ionized the atmospheric gases, creating a layer of charged particles (ions <br>" 
                "  and electrons). Venus has a substantial ionosphere, with peak electron densities occurring around 120-140 km altitude. The <br>" 
                "  ionosphere plays a crucial role in interacting with the solar wind, as Venus lacks a strong global magnetic field.<br>" 
                "  * The solar wind directly impacts the ionosphere, leading to the formation of an induced magnetosphere.<br>" 
                "  * The nightside ionosphere is more variable and less dense than the dayside ionosphere, but it can extend to very high <br>" 
                "    altitudes, even forming a long, comet-like tail under certain solar wind conditions.<br>" 
                "  Extent in Venus radii: The main part of the ionosphere extends from about 120 km to several hundred kilometers. If we <br>" 
                "  consider an upper limit of, say, 500 km for a significant ionospheric density: So, the ionosphere can extend up to about 8.3% <br>" 
                "  of Venus's radius. However, the outermost fringes can be even more extended.<br>" 
                "* Exosphere (extends from where the atmosphere is very thin outwards into space): The uppermost layer of Venus's atmosphere <br>" 
                "  is the exosphere, where the gas density is so low that atoms and molecules can escape into space. The boundary between the <br>" 
                "  thermosphere and exosphere (the exobase) is not sharply defined but is generally considered to be above where collisions <br>" 
                "  between particles become infrequent. This is likely several hundred kilometers above the surface. The exosphere gradually <br>" 
                "  fades into space and interacts directly with the solar wind. Extent in Venus radii: The exosphere has no well-defined upper <br>" 
                "  limit. It extends outwards until the planet's gravity is no longer the dominant force.<br>" 
                "In summary, the upper atmosphere of Venus is a significant region:<br>" 
                "* The mesosphere occupies roughly 1.5-1.6% of Venus's radius.<br>" 
                "* The thermosphere extends to at least 3.3% of Venus's radius.<br>" 
                "* The ionosphere spans a considerable range within the thermosphere and exosphere, potentially reaching about 8% or more of <br>" 
                "  Venus's radius for significant charged particle densities.<br>" 
                "* The exosphere gradually fades out into space. It's important to remember that these are approximate extents, and the <br>" 
                "  boundaries between these regions are not always sharp and can vary with solar activity and other factors. The upper <br>" 
                "  atmosphere of Venus is a subject of ongoing research, and future missions will undoubtedly refine our understanding of <br>" 
                "  its structure and dynamics."
            ),
            'tooltip': (
                "In summary, the upper atmosphere of Venus is a significant region:\n" 
                "* The mesosphere occupies roughly 1.5-1.6% of Venus's radius.\n" 
                "* The thermosphere extends to at least 3.3% of Venus's radius.\n" 
                "* The ionosphere spans a considerable range within the thermosphere and exosphere, potentially reaching about 8% or \n" 
                "  more of Venus's radius for significant charged particle densities. The exosphere gradually fades out into space."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 166,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 1.0,
            'hover_text': (
                "Venus's Hill Sphere (extends to ~166 Venus radii or about 1 million km)<br><br>" 
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 
                "Venus's Hill Sphere is the region where its gravitational influence is dominant over the gravitational influence of \n" 
                "the Sun. The size of the Hill sphere depends on its mass and its distance from the Sun. Venus's Hill sphere extends \n" 
                "to approximately 1 million kilometers from the planet. Within this sphere, Venus's gravity is the primary force \n" 
                "attracting its own moons or any potential debris. However, Venus has no natural moons."
            ),
        },
    },

    # ============================================================
    # Mars
    # ============================================================
    'Mars': {

        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.5,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "A Solid Inner Core: Based on seismic data from the InSight lander, scientists have strong evidence that Mars <br>" 
                "possesses a solid inner core. This inner core is primarily composed of iron and nickel, similar to Earth's.<br><br>"
                "The differentiation into a solid inner core and a liquid outer core is primarily driven by:<br>"
                "* Temperature Gradient: The temperature increases significantly as you move towards the center of the planet. <br>" 
                "  The very high pressure at the center raises the melting point of the metallic core material. The inner core <br>" 
                "  is where the pressure exceeds the melting point at that temperature, forcing the metal into a solid state. <br>" 
                "  The outer core is still hot enough to be liquid at the prevailing pressures.<br>"
                "* Compositional Differences: The presence of lighter elements in the outer core also contributes to its lower <br>" 
                "  melting point compared to the purer iron-nickel of the inner core.<br>"
                "* Differences from Earth's Core:"
                "  * Size: Mars' core is proportionally larger relative to the planet's overall size compared to Earth's core.<br>"
                "  * Density: The lower overall density of Mars suggests that its core likely contains a higher percentage of <br>" 
                "    lighter elements than Earth's core.<br>" 
                "  * Lack of a Global Dynamo (Currently): Earth's liquid outer core is convecting, which, along with the planet's <br>" 
                "    rotation, generates our global magnetic field (the geodynamo). The fact that Mars currently lacks a global <br>" 
                "    magnetic field suggests that the convection in its liquid outer core is either absent, very weak, or organized <br>" 
                "    differently. This could be due to its smaller size, different cooling history, or the higher abundance of <br>" 
                "    lighter elements affecting its fluid dynamics.<br>" 
                "The precise composition and dynamics of these layers are still subjects of ongoing research and analysis of data.<br><br>" 
                "Past Magnetosphere: Scientists believe that early in its history, Mars did possess a global magnetic field, <br>" 
                "much like Earth's. This would have created a significant magnetosphere, deflecting much of the solar wind and <br>" 
                "cosmic radiation. However, unlike Earth, Mars lost its global magnetic field billions of years ago. The exact <br>" 
                "reasons are still being investigated, but theories involve the cooling and solidification of its iron core, which <br>" 
                "would have stopped the dynamo process that generates a global magnetic field. Today, Mars doesn't have a planet-wide <br>" 
                "magnetosphere generated by a global magnetic field. However, the Mars Global Surveyor mission discovered strong, <br>" 
                "localized magnetic fields embedded in certain regions of the Martian crust, particularly in the ancient southern <br>" 
                "highlands. These are remnants of the early global field. These localized fields can create small, localized <br>" 
                "magnetospheres, but they don't provide planet-wide protection like Earth's magnetosphere."
            ),
            'tooltip': (
                "A Solid Inner Core: Based on seismic data from the InSight lander, scientists have strong evidence that Mars \n" 
                "possesses a solid inner core. This inner core is primarily composed of iron and nickel, similar to Earth's."
            ),
        },

        'outer_core': {
            'name': 'Outer Core',
            'radius_fraction': 0.8,
            'color': 'rgb(255, 140, 0)',
            'opacity': 0.8,
            'n_points': 25,
            'marker_size': 3.7,
            'info_border': 'white',  # two-standards (May 29, 2026): bright orange fill
            'hover_text': (
                "A Liquid Outer Core: Surrounding the solid inner core is believed to be a liquid outer core, also primarily <br>" 
                "made of iron and nickel, but likely containing a significant amount of lighter elements like sulfur, oxygen, <br>" 
                "or even hydrogen. The presence of these lighter elements would lower the melting point of the iron-nickel alloy, <br>" 
                "allowing it to remain liquid despite the pressure.<br><br>"
                "The differentiation into a solid inner core and a liquid outer core is primarily driven by:<br>"
                "* Temperature Gradient: The temperature increases significantly as you move towards the center of the planet. <br>" 
                "  The very high pressure at the center raises the melting point of the metallic core material. The inner core <br>" 
                "  is where the pressure exceeds the melting point at that temperature, forcing the metal into a solid state. <br>" 
                "  The outer core is still hot enough to be liquid at the prevailing pressures.<br>"
                "* Compositional Differences: The presence of lighter elements in the outer core also contributes to its lower <br>" 
                "  melting point compared to the purer iron-nickel of the inner core.<br>"
                "* Differences from Earth's Core:"
                "  * Size: Mars' core is proportionally larger relative to the planet's overall size compared to Earth's core.<br>"
                "  * Density: The lower overall density of Mars suggests that its core likely contains a higher percentage of <br>" 
                "    lighter elements than Earth's core.<br>" 
                "  * Lack of a Global Dynamo (Currently): Earth's liquid outer core is convecting, which, along with the planet's <br>" 
                "    rotation, generates our global magnetic field (the geodynamo). The fact that Mars currently lacks a global <br>" 
                "    magnetic field suggests that the convection in its liquid outer core is either absent, very weak, or organized <br>" 
                "    differently. This could be due to its smaller size, different cooling history, or the higher abundance of <br>" 
                "    lighter elements affecting its fluid dynamics.<br>" 
                "The precise composition and dynamics of these layers are still subjects of ongoing research and analysis of data."
            ),
            'tooltip': (
                "A Liquid Outer Core: Surrounding the solid inner core is believed to be a liquid outer core, also primarily \n" 
                "made of iron and nickel, but likely containing a significant amount of lighter elements like sulfur, oxygen, \n" 
                "or even hydrogen. The presence of these lighter elements would lower the melting point of the iron-nickel alloy, \n" 
                "allowing it to remain liquid despite the pressure."
            ),
        },

        'mantle': {
            'name': 'Mantle',
            'radius_fraction': 0.98,
            'color': 'rgb(205, 85, 85)',
            'opacity': 0.6,
            'n_points': 25,
            'marker_size': 3.1,
            'info_border': 'white',  # two-standards (May 29, 2026): pink-red fill
            'hover_text': (
                "Mantle: Surrounding the core is a silicate mantle, similar to Earth's. It's composed of dense rocks rich in <br>" 
                "elements like silicon, oxygen, iron, and magnesium. While \"upper mantle\" isn't a formal layer name in the <br>" 
                "same way as Earth's, scientists do discuss different regions within the mantle based on mineral phase transitions <br>" 
                "that occur at different depths and pressures. For example, there might be an upper and lower transition zone <br>" 
                "within the mantle, similar in concept to Earth's, although the specific minerals and depths would differ due to <br>" 
                "Mars' unique composition and internal pressures."
            ),
            'tooltip': (
                "Mantle: Surrounding the core is a silicate mantle, similar to Earth's. It's composed of dense rocks rich in \n" 
                "elements like silicon, oxygen, iron, and magnesium."
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(188, 39, 50)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'info_border': 'white',  # two-standards (May 29, 2026): dense red fill
            'hover_text': (
                "Mars Crust<br>" 
                "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>" 
                "Mars has a crust, which is the outermost solid shell. Interestingly, recent findings from marsquakes <br>" 
                "suggest that the Martian crust is significantly thicker than Earth's, perhaps averaging around 70 kilometers <br>" 
                "(43 miles) or even thicker in some areas.<br><br>" 
                "Today, Mars doesn't have a planet-wide magnetosphere generated by a global magnetic field. However, the Mars Global <br>" 
                "Surveyor mission discovered strong, localized magnetic fields embedded in certain regions of the Martian crust, <br>" 
                "particularly in the ancient southern highlands. These are remnants of the early global field. These localized fields <br>" 
                "can create small, localized magnetospheres, but they don't provide planet-wide protection like Earth's magnetosphere."
            ),
            'tooltip': (
                "Mars's crust: Mars has a crust, which is the outermost solid shell. Interestingly, recent findings from marsquakes \n" 
                "suggest that the Martian crust is significantly thicker than Earth's, perhaps averaging around 70 kilometers \n" 
                "(43 miles) or even thicker in some areas."
            ),
        },

        'atmosphere': {
            'name': 'Lower Atmosphere',
            'radius_fraction': 1.02,
            'color': 'rgb(150, 200, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 2.5,
            'hover_text': (
                "Atmosphere: Mars has a thin atmosphere, much less dense than Earth's. It's primarily composed of carbon dioxide <br>" 
                "(about 95%), with small amounts of nitrogen, argon, and other gases.<br><br>" 
                "Scientists often divide the Martian atmosphere into layers based on temperature profiles, similar to Earth's <br>" 
                "atmosphere, although some layers are absent or behave differently:<br>" 
                "* Troposphere: This is the lowest layer, extending from the surface up to about 40-50 kilometers (25-31 miles). <br>" 
                "  Most of Mars' weather, like dust storms and convection, occurs here. The temperature generally decreases with altitude.<br>" 
                "* Mesosphere: Above the troposphere, extending from about 50 to 100 kilometers (31 to 62 miles). This layer has the <br>" 
                "  lowest temperatures in the Martian atmosphere as carbon dioxide efficiently radiates heat into space. Carbon dioxide <br>" 
                "  ice clouds have even been observed in the Martian mesosphere.<br>" 
                "* Thermosphere: Above the mesosphere, starting around 100 kilometers (62 miles) and extending to about 200 kilometers <br>" 
                "  (124 miles). This layer is heated by extreme ultraviolet radiation from the Sun, and temperatures increase with <br>" 
                "  altitude. However, it's still much colder than Earth's thermosphere."
            ),
            'tooltip': (
                "Atmosphere: Mars has a thin atmosphere, much less dense than Earth's. It's primarily composed of carbon dioxide \n" 
                "(about 95%), with small amounts of nitrogen, argon, and other gases."
            ),
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'radius_fraction': 1.06,
            'color': 'rgb(100, 150, 255)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "Upper Atmosphere: Like Earth, Mars has upper atmospheric layers, including an ionosphere and exosphere, where <br>" 
                "the atmosphere becomes very thin and interacts with solar radiation and the solar wind.<br><br>" 
                "Exosphere: This is the outermost layer, starting above the thermosphere (around 200 km/124 miles) and gradually <br>" 
                "thinning out into space. Atoms and molecules here are so far apart that they can escape the planet's gravity.<br><br>" 
                "Interaction with Solar Wind: Without a global magnetosphere, the Martian atmosphere is directly exposed to the <br>" 
                "solar wind, a stream of charged particles from the Sun. This interaction is believed to have played a significant <br>" 
                "role in stripping away much of Mars' early, potentially thicker atmosphere and contributing to the loss of liquid <br>" 
                "water on the surface. Unlike Earth, Mars lacks a stratosphere. On Earth, the stratosphere is characterized by a <br>" 
                "temperature inversion due to the absorption of ultraviolet radiation by the ozone layer. Mars has a very thin <br>" 
                "atmosphere and no significant ozone layer, so this distinct layer doesn't form."
            ),
            'tooltip': (
                "Upper Atmosphere: Like Earth, Mars has upper atmospheric layers, including an ionosphere and exosphere, where \n" 
                "the atmosphere becomes very thin and interacts with solar radiation and the solar wind.\n\n" 
                "Exosphere: This is the outermost layer, starting above the thermosphere (around 200 km/124 miles) and gradually \n" 
                "thinning out into space. Atoms and molecules here are so far apart that they can escape the planet's gravity.\n\n" 
                "Interaction with Solar Wind: Without a global magnetosphere, the Martian atmosphere is directly exposed to the \n" 
                "solar wind, a stream of charged particles from the Sun. This interaction is believed to have played a significant \n" 
                "role in stripping away much of Mars' early, potentially thicker atmosphere and contributing to the loss of liquid \n" 
                "water on the surface. Unlike Earth, Mars lacks a stratosphere. On Earth, the stratosphere is characterized by a \n" 
                "temperature inversion due to the absorption of ultraviolet radiation by the ozone layer. Mars has a very thin \n" 
                "atmosphere and no significant ozone layer, so this distinct layer doesn't form."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 324.5,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.15,
            'n_points': 20,
            'marker_size': 1.0,
            'hover_text': (
                "Mars's Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its <br>" 
                "gravitational influence and encompasses its two moons.<br><br>" 
                "* Definition: The Hill sphere (sometimes called the Roche sphere or gravitational sphere of influence) of a <br>" 
                "  celestial body is the region around it where its own gravity is the dominant force attracting satellites. <br>" 
                "  Essentially, it's the space where a moon or spacecraft would primarily orbit that body rather than the larger <br>" 
                "  body it orbits (in Mars' case, the Sun).<br>" 
                "* Mars' Hill Sphere: The size of a planet's Hill sphere depends on its mass and its distance from the Sun. <br>" 
                "  Mars, being less massive than Earth and farther from the Sun, has a Hill sphere with a radius of approximately <br>" 
                "  1.1 million kilometers (about 0.073 astronomical units).<br>" 
                "* Moons Within the Hill Sphere: Mars' two small moons, Phobos and Deimos, orbit well within Mars' Hill sphere, <br>" 
                "  which is why they are gravitationally bound to the planet and not the Sun.<br>" 
                "* Importance: The concept of the Hill sphere is crucial for understanding the stability of orbits around a planet. <br>" 
                "  Any object orbiting Mars within its Hill sphere is more likely to remain a satellite of Mars. If an object's <br>" 
                "  orbit extends beyond the Hill sphere, the Sun's gravity would become the dominant influence, potentially pulling <br>" 
                "the object into a heliocentric orbit.<br><br>"
                "The Hill sphere is the region around a where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."               
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 
                "Mars's Hill Sphere (extends to ~324.5 Mars radii or about 1.1 million km), which defines the region of its \n" 
                "gravitational influence and encompasses its two moons."
            ),
        },
    },


    # ============================================================
    # Earth
    # ============================================================
    # Source: USGS Interior of the Earth, NASA Earth Fact Sheet,
    #         NOAA / NCEI (atmosphere boundaries), NASA Goddard,
    #         NASA Van Allen Probes, NASA Solar System Dynamics.
    # Verified: April 2026 provenance audit.
    'Earth': {

        'inner_core': {
            'name': 'Inner Core',
            'radius_fraction': 0.19,
            'color': 'rgb(255, 180, 140)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "Earth's inner core is a solid sphere composed primarily of iron and nickel.<br>"
                "Despite incredible pressure, temperatures of 5,400 degC (9,800 degF) keep it nearly<br>"
                "at melting point. It rotates slightly faster than the rest of Earth, creating<br>"
                "complex dynamics in Earth's magnetic field. The inner core is approximately<br>"
                "1,220 km (760 miles) in radius."
            ),
            'tooltip': (
                "Earth's inner core is a solid sphere composed primarily of iron and nickel.\n"
                "Despite incredible pressure, temperatures of 5,400 degC (9,800 degF) keep it nearly\n"
                "at melting point. It rotates slightly faster than the rest of Earth, creating\n"
                "complex dynamics in Earth's magnetic field. The inner core is approximately\n"
                "1,220 km (760 miles) in radius."
            ),
        },

        'outer_core': {
            'name': 'Outer Core',
            'radius_fraction': 0.55,
            'color': 'rgb(255, 140, 0)',
            'opacity': 0.8,
            'n_points': 25,
            'marker_size': 3.7,
            'info_border': 'white',  # two-standards (May 29, 2026): bright orange fill
            'hover_text': (
                "The outer core is a liquid layer of iron, nickel, and lighter elements.<br>"
                "Convection currents in this highly conductive fluid generate Earth's<br>"
                "magnetic field through a process called the geodynamo. It extends from<br>"
                "1,220 to 3,500 km from Earth's center and has temperatures ranging from<br>"
                "4,500 degC (8,100 degF) to 5,400 degC (9,800 degF)."
            ),
            'tooltip': (
                "The outer core is a liquid layer of iron, nickel, and lighter elements.\n"
                "Convection currents in this highly conductive fluid generate Earth's\n"
                "magnetic field through a process called the geodynamo. It extends from\n"
                "1,220 to 3,500 km from Earth's center and has temperatures ranging from\n"
                "4,500 degC (8,100 degF) to 5,400 degC (9,800 degF)."
            ),
        },

        'lower_mantle': {
            'name': 'Lower Mantle',
            'radius_fraction': 0.85,
            'color': 'rgb(230, 100, 20)',
            'opacity': 0.7,
            'n_points': 25,
            'marker_size': 3.4,
            'info_border': 'white',  # two-standards (May 29, 2026): burnt orange fill
            'hover_text': (
                "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.<br>"
                "Despite being solid, it flows very slowly through convection, driving plate tectonics.<br>"
                "This region extends from 660 to 2,900 km below Earth's surface and experiences<br>"
                "temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure."
            ),
            'tooltip': (
                "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.\n"
                "Despite being solid, it flows very slowly through convection, driving plate tectonics.\n"
                "This region extends from 660 to 2,900 km below Earth's surface and experiences\n"
                "temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure."
            ),
        },

        'upper_mantle': {
            'name': 'Upper Mantle',
            'radius_fraction': 0.98,
            'color': 'rgb(205, 85, 85)',
            'opacity': 0.6,
            'n_points': 25,
            'marker_size': 3.1,
            'info_border': 'white',  # two-standards (May 29, 2026): pink-red fill
            'hover_text': (
                "The upper mantle includes the asthenosphere, a partially molten layer where<br>"
                "most magma originates. This region flows more readily than the lower mantle,<br>"
                "allowing tectonic plates to move. It extends from about 30 to 660 km below<br>"
                "the surface, with temperatures from 500 degC to 2,200 degC (900 degF to 4,000 degF)."
            ),
            'tooltip': (
                "The upper mantle includes the asthenosphere, a partially molten layer where\n"
                "most magma originates. This region flows more readily than the lower mantle,\n"
                "allowing tectonic plates to move. It extends from about 30 to 660 km below\n"
                "the surface, with temperatures from 500 degC to 2,200 degC (900 degF to 4,000 degF)."
            ),
        },

        'crust': {
            'name': 'Crust',
            'radius_fraction': 1.0,
            'color': 'rgb(70, 120, 160)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Earth Crust<br>" 
                "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
                "Earth's crust is the thin, solid outer layer where humans live. It's divided into<br>"
                "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)<br>"
                "made primarily of granite. The crust contains all known life and the accessible portion<br>"
                "of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF)."
            ),
            'tooltip': (
                "Earth's crust is the thin, solid outer layer where humans live. It's divided into\n"
                "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)\n"
                "made primarily of granite. The crust contains all known life and the accessible portion\n"
                "of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF)."
            ),
        },

        'atmosphere': {
            'name': 'Lower Atmosphere',
            'radius_fraction': 1.05,
            'color': 'rgb(150, 200, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 2.5,
            'hover_text': (
                "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and<br>"
                "the stratosphere (12-50 km) which contains the ozone layer. These regions contain<br>"
                "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from<br>"
                "about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).<br>"
                "The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption."
            ),
            'tooltip': (
                "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and\n"
                "the stratosphere (12-50 km) which contains the ozone layer. These regions contain\n"
                "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from\n"
                "about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).\n"
                "The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption."
            ),
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'radius_fraction': 1.25,
            'color': 'rgb(100, 150, 255)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes<br>"
                "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and<br>"
                "the International Space Station orbits, and the exosphere which gradually transitions<br>"
                "to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the<br>"
                "gas is so thin that it would feel cold to human skin."
            ),
            'tooltip': (
                "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes\n"
                "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and\n"
                "the International Space Station orbits, and the exosphere which gradually transitions\n"
                "to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the\n"
                "gas is so thin that it would feel cold to human skin."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 235,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 1.0,
            'hover_text': (
                "Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)<br><br>"
                "The Hill sphere is the region around a body where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."                  
            ),
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n" 
                "Earth's Hill Sphere (extends to ~235 Earth radii or about 1.5 million km)."
            ),
        },
    },


    # ============================================================
    # Jupiter
    # ============================================================
    # Source: NASA Juno Mission; Wahl et al. (2017) for core;
    #         NASA Solar System Exploration; NASA Juno gravity science
    #         (fuzzy core to ~60% R_J).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Jupiter': {

        'core': {
            'name': 'Core',
            'radius_fraction': 0.1,
            'color': 'rgb(175, 175, 255)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': (
                "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.<br>"
                "It may be up to 10 times the mass of Earth. Recent models suggest the core might be<br>"
                "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature<br>"
                "is estimated at about 20,000K and up to 40,000K. The color chosen approximates a black body."
            ),
            'tooltip': (
                "2.4 MB PER FRAME FOR HTML.\n\n"
                "Jupiter's core is believed to be a dense mixture of rock, metal, and hydrogen compounds.\n"
                "It may be up to 10 times the mass of Earth. Recent models suggest the core might be\n"
                "partially dissolved or 'fuzzy' rather than a distinct solid structure. Its temperature\n"
                "is estimated at about 20,000K and up to 40,000K. The color chosen approximates a black body."
            ),
        },

        'metallic_hydrogen': {
            'name': 'Metallic Hydrogen Layer',
            'radius_fraction': 0.8,
            'color': 'rgb(225, 225, 255)',
            'opacity': 0.9,
            'n_points': 25,
            'marker_size': 3.5,
            'hover_text': (
                "Metallic Hydrogen Layer:<br>" 
                "Under extreme pressure, hydrogen transitions to a metallic state in this layer.<br>"
                "It behaves like an electrical conductor and is responsible for generating<br>"
                "Jupiter's powerful magnetic field. Temperatures in this region may reach 10,000K."
            ),
            'tooltip': (
                "2.1 MB PER FRAME FOR HTML.\n\n"
                "Under extreme pressure, hydrogen transitions to a metallic state in this layer.\n"
                "It behaves like an electrical conductor and is responsible for generating\n"
                "Jupiter's powerful magnetic field. Temperatures in this region may reach 10,000K."
            ),
        },

        'molecular_hydrogen': {
            'name': 'Molecular Hydrogen Layer',
            'radius_fraction': 0.97,
            'color': 'rgb(255, 255, 200)',
            'opacity': 0.5,
            'n_points': 25,
            'marker_size': 3.0,
            'hover_text': (
                "Molecular Hydrogen Layer:<br>" 
                "This layer consists of hydrogen in its molecular form. The transition from metallic<br>"
                "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass<br>"
                "and is marked by decreasing temperature and pressure as you move outward. The temperature<br>"
                "ranges from about 5,000K (outer) to 10,000K (inner)."
            ),
            'tooltip': (
                "2.5 MB PER FRAME FOR HTML.\n\n"
                "This layer consists of hydrogen in its molecular form. The transition from metallic\n"
                "to molecular hydrogen is gradual. This layer makes up the bulk of Jupiter's mass\n"
                "and is marked by decreasing temperature and pressure as you move outward. The temperature\n"
                "ranges from about 5,000K (outer) to 10,000K (inner)."
            ),
        },

        'cloud_layer': {
            'name': 'Cloud Layer',
            'radius_fraction': 1.0,
            'color': 'rgb(255, 255, 235)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': (
                "Jupiter Cloud Layer<br>" 
                "(Note: toggle off the cloud layer in the legend to better see the interior structure.)<br><br>"
                "Jupiter's visible cloud layer consists of bands of different colors, caused by<br>"
                "variations in chemical composition and atmospheric dynamics. The clouds are primarily<br>"
                "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot<br>"
                "is a massive storm system located in this layer. Temperature ranges from 120 K in<br>" 
                "the highest ammonia ice clouds to about 200 K in the lower ammonium hydrosulfide clouds."
            ),
            'tooltip': (
                "USE MANUAL SCALED OF 0.005 AU TO VIEW CLOSELY."
                "4.6 MB PER FRAME FOR HTML.\n\n"
                "Jupiter's visible cloud layer consists of bands of different colors, caused by\n"
                "variations in chemical composition and atmospheric dynamics. The clouds are primarily\n"
                "composed of ammonia, ammonium hydrosulfide, and water. The famous Great Red Spot\n"
                "is a massive storm system located in this layer. Temperature ranges from 120 K in\n" 
                "the highest ammonia ice clouds to about 200 K in the lower ammonium hydrosulfide clouds."
            ),
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'radius_fraction': 1.1,
            'color': 'rgb(220, 240, 255)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': (
                "Jupiter's upper atmosphere includes the stratosphere and thermosphere.<br>"
                "It's less dense than the cloud layer below and contains hydrocarbon haze<br>"
                "produced by solar ultraviolet radiation. Aurora activity can be observed<br>"
                "at Jupiter's poles, caused by interactions with its magnetic field. Temperature<br>"
                "ranges from 200K in the stratosphere to 1000K in the thermosphere and exosphere."
            ),
            'tooltip': (
                "2.7 MB PER FRAME FOR HTML.\n\n"
                "Jupiter's upper atmosphere includes the stratosphere and thermosphere.\n"
                "It's less dense than the cloud layer below and contains hydrocarbon haze\n"
                "produced by solar ultraviolet radiation. Aurora activity can be observed\n"
                "at Jupiter's poles, caused by interactions with its magnetic field. Temperature\n"
                "ranges from 200K in the stratosphere to 1000K in the thermosphere and exosphere."
            ),
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'radius_fraction': 740,
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': (
                "SET MANUAL SCALE OF AT LEAST 0.5 AU TO VISUALIZE.<br><br>"
                "Jupiter's Hill Sphere (extends to ~740 Jupiter radii, ~0.35 AU or ~53 million km)<br><br>"
                "The Hill sphere is the region around a body where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."            
            ),
            'tooltip': (
                "SELECT MANUAL SCALE OF AT LEAST 0.5 AU TO VISUALIZE.\n" 
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Jupiter's Hill Sphere (extends to ~740 Jupiter radii, about 0.35 AU or ~53 million km)"                      
            ),
        },
    },


    # ============================================================
    # Saturn
    # ============================================================
    # Source: NASA Saturn Fact Sheet; NASA Cassini Mission;
    #         NASA Saturn Magnetosphere Overview; Mankovich & Fuller (2021).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Saturn': {

        'core': {
            'name': 'Core',
            'color': 'rgb(240, 240, 255)',
            'opacity': 1.0,
            'radius_fraction': 0.6,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': saturn_core_info.replace('\n', '<br>'),
            'tooltip': saturn_core_info,
        },

        'metallic_hydrogen': {
            'name': 'Metallic Hydrogen Layer',
            'color': 'rgb(225, 225, 220)',
            'opacity': 0.9,
            'radius_fraction': 0.9,
            'n_points': 25,
            'marker_size': 3.5,
            'hover_text': saturn_metallic_hydrogen_info.replace('\n', '<br>'),
            'tooltip': saturn_metallic_hydrogen_info,
        },

        'molecular_hydrogen': {
            'name': 'Molecular Hydrogen Layer',
            'color': 'rgb(220, 230, 240)',
            'opacity': 0.5,
            'radius_fraction': 0.99,
            'n_points': 25,
            'marker_size': 3.0,
            'hover_text': saturn_molecular_hydrogen_info.replace('\n', '<br>'),
            'tooltip': saturn_molecular_hydrogen_info,
        },

        'cloud_layer': {
            'name': 'Cloud Layer',
            'color': 'rgb(210, 180, 140)',
            'opacity': 1.0,
            'radius_fraction': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': saturn_cloud_layer_info.replace('\n', '<br>'),
            'tooltip': saturn_cloud_layer_info,
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'color': 'rgb(240, 245, 250)',
            'opacity': 0.5,
            'radius_fraction': 1.1,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': saturn_upper_atmosphere_info.replace('\n', '<br>'),
            'tooltip': saturn_upper_atmosphere_info,
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.3,
            'radius_fraction': 1120,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': saturn_hill_sphere_info.replace('\n', '<br>'),
            'tooltip': saturn_hill_sphere_info,
        },

    },


    # ============================================================
    # Uranus
    # ============================================================
    # Source: NASA Voyager 2 Mission; NASA Uranus Fact Sheet;
    #         Ness et al. (1986) Science (magnetometer).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Uranus': {

        'core': {
            'name': 'Core',
            'color': 'rgb(255, 215, 0)',
            'opacity': 1.0,
            'radius_fraction': 0.2,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': uranus_core_info.replace('\n', '<br>'),
            'tooltip': uranus_core_info,
        },

        'mantle': {
            'name': 'Mantle',
            'color': 'rgb(255, 138, 18)',
            'opacity': 0.9,
            'radius_fraction': 0.7,
            'n_points': 25,
            'marker_size': 3.5,
            'info_border': 'white',  # two-standards (May 29, 2026): bright orange fill
            'hover_text': uranus_mantle_info.replace('\n', '<br>'),
            'tooltip': uranus_mantle_info,
        },

        'cloud_layer': {
            'name': 'Cloud Layer',
            'color': 'rgb(173, 216, 230)',
            'opacity': 1.0,
            'radius_fraction': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': uranus_cloud_layer_info.replace('\n', '<br>'),
            'tooltip': uranus_cloud_layer_info,
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'color': 'rgb(240, 245, 250)',
            'opacity': 0.5,
            'radius_fraction': 1.16,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': uranus_upper_atmosphere_info.replace('\n', '<br>'),
            'tooltip': uranus_upper_atmosphere_info,
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'radius_fraction': 2770,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': uranus_hill_sphere_info.replace('\n', '<br>'),
            'tooltip': uranus_hill_sphere_info,
        },

    },


    # ============================================================
    # Neptune
    # ============================================================
    # Source: NASA Voyager 2 Mission; NASA Neptune Fact Sheet;
    #         Ness et al. (1989) Science (magnetometer).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Neptune': {

        'core': {
            'name': 'Core',
            'color': 'rgb(255, 215, 0)',
            'opacity': 1.0,
            'radius_fraction': 0.25,
            'n_points': 25,
            'marker_size': 4.0,
            'hover_text': neptune_core_info.replace('\n', '<br>'),
            'tooltip': neptune_core_info,
        },

        'mantle': {
            'name': 'Mantle',
            'color': 'rgb(255, 138, 18)',
            'opacity': 0.9,
            'radius_fraction': 0.85,
            'n_points': 25,
            'marker_size': 3.5,
            'info_border': 'white',  # two-standards (May 29, 2026): bright orange fill
            'hover_text': neptune_mantle_info.replace('\n', '<br>'),
            'tooltip': neptune_mantle_info,
        },

        'cloud_layer': {
            'name': 'Cloud Layer',
            'color': 'rgb(0, 128, 255)',
            'opacity': 1.0,
            'radius_fraction': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'hover_text': neptune_cloud_layer_info.replace('\n', '<br>'),
            'tooltip': neptune_cloud_layer_info,
        },

        'upper_atmosphere': {
            'name': 'Upper Atmosphere',
            'color': 'rgb(240, 245, 250)',
            'opacity': 0.5,
            'radius_fraction': 1.01,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': neptune_upper_atmosphere_info.replace('\n', '<br>'),
            'tooltip': neptune_upper_atmosphere_info,
        },

        'hill_sphere': {
            'name': 'Hill Sphere',
            'color': 'rgb(0, 255, 0)',
            'opacity': 0.25,
            'radius_fraction': 4685,
            'n_points': 20,
            'marker_size': 2.0,
            'hover_text': neptune_hill_sphere_info.replace('\n', '<br>'),
            'tooltip': neptune_hill_sphere_info,
        },

    },



    # ============================================================
    # Sun
    # ============================================================
    # Source: NASA Solar Dynamics Observatory; NASA Parker Solar Probe;
    #         NASA Heliophysics; IAU 2015 nominal solar radius.
    # Verified: April 2026 provenance audit.
    # Phase D1: Config extraction only. Configs registered but not yet
    # invoked by unified dispatch. create_sun_visualization() stays alive.
    # Legend names follow Option A: clean 'name' values; at eventual
    # switchover, 6 non-conforming legend entries normalize to 'Sun: <X>'.
    # Module updated: May 2026 with Anthropic's Claude Opus 4.6
    'Sun': {

        'core': {
            'name': 'Core',
            'radius_au': CORE_AU,
            'color': 'rgb(70, 130, 180)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 10,
            'hover_text': core_info_hover,
            'tooltip': core_info,
        },

        'radiative': {
            'name': 'Radiative Zone',
            'radius_au': RADIATIVE_ZONE_AU,
            'color': 'rgb(30, 144, 255)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 7,
            'hover_text': radiative_zone_info_hover,
            'tooltip': radiative_zone_info,
        },

        'photosphere': {
            'name': 'Photosphere',
            'radius_au': SOLAR_RADIUS_AU,
            'color': 'rgb(255, 244, 214)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'n_points': 25,
            'marker_size': 7.0,
            'hover_text': photosphere_info_hover,
            'tooltip': photosphere_info,
        },

        'chromosphere': {
            'name': 'Chromosphere',
            'radius_au': CHROMOSPHERE_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(30, 144, 255)',
            'opacity': 0.5,
            'n_points': 25,
            'marker_size': 3.0,
            'hover_text': chromosphere_info_hover,
            'tooltip': chromosphere_info,
        },

        'inner_corona': {
            'name': 'Inner Corona',
            'radius_au': INNER_CORONA_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(0, 0, 255)',
            'opacity': 0.45,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': inner_corona_info_hover,
            'tooltip': inner_corona_info,
        },

        'streamer_belt': {
            'name': 'Streamer Belt (Visible Corona)',
            'radius_au': STREAMER_BELT_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(255, 200, 80)',
            'opacity': 0.45,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': streamer_belt_info_hover,
            'tooltip': streamer_belt_info,
        },

        'roche_limit': {
            'name': 'Roche Limit (Comets)',
            'radius_au': ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(200, 60, 60)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 3.0,
            'info_border': 'white',  # two-standards (May 29, 2026): dense red fill rgb(200,60,60)
            'hover_text': roche_limit_info_hover,
            'tooltip': roche_limit_info,
        },

        'alfven_surface': {
            'name': 'Alfven Surface',
            'radius_au': ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(0, 200, 200)',
            'opacity': 0.35,
            'n_points': 20,
            'marker_size': 3.5,
            'hover_text': alfven_surface_info_hover,
            'tooltip': alfven_surface_info,
        },

        'outer_corona': {
            'name': 'Outer Corona',
            'radius_au': OUTER_CORONA_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(25, 25, 112)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 3.5,
            'hover_text': outer_corona_info_hover,
            'tooltip': outer_corona_info,
        },

        'termination_shock': {
            'name': 'Termination Shock',
            'radius_au': TERMINATION_SHOCK_AU,
            'color': 'rgb(240, 244, 255)',
            'opacity': 0.4,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': termination_shock_info_hover,
            'tooltip': termination_shock_info,
        },

        'heliopause': {
            'name': 'Heliopause',
            'radius_au': HELIOPAUSE_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(135, 206, 250)',
            'opacity': 0.4,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': solar_wind_info_hover,
            'tooltip': solar_wind_info,
        },

        'inner_oort_limit': {
            'name': 'Inner Limit of Oort Cloud',
            'radius_au': INNER_LIMIT_OORT_CLOUD_AU,
            'color': 'white',
            'opacity': 0.35,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': inner_limit_oort_info_hover,
            'tooltip': inner_limit_oort_info,
        },

        'inner_oort': {
            'name': 'Inner Oort Cloud',
            'radius_au': INNER_OORT_CLOUD_AU,
            'color': 'white',
            'opacity': 0.35,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': inner_oort_info_hover,
            'tooltip': inner_oort_info,
        },

        'outer_oort': {
            'name': 'Outer Oort Cloud',
            'radius_au': OUTER_OORT_CLOUD_AU,
            'color': 'white',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': outer_oort_info_hover,
            'tooltip': outer_oort_info,
        },

        'gravitational': {
            'name': 'Gravitational Influence',
            'radius_au': GRAVITATIONAL_INFLUENCE_AU,
            'color': 'rgb(102, 187, 106)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': gravitational_influence_info_hover,
            'tooltip': gravitational_influence_info,
        },

    },


    # Other bodies added in Phases D
}


# ============================================================
# CUSTOM_SHELLS: geometry that doesn't fit the sphere builder
# ============================================================
# Maps body_name -> shell_name -> {'builder': 'module.function', 'tooltip': '...'}
# Lazy-imported at render time. The builder function must accept
# center_position and return a list of plotly traces.

CUSTOM_SHELLS = {

    # ============================================================
    # Mercury
    # ============================================================
    'Mercury': {

        'sodium_tail': {
            'builder': 'mercury_visualization_shells.create_mercury_sodium_tail',
            'needs_sun_position': True,
            'tooltip': (
                "TO VISUALIZE CLOSE UP SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n"
                "TO VISUALIZE THE COMPLETE TAIL INCLUDE VENUS IN THE PLOT OR SET MANUAL SCALE TO 1.0 AU\n\n"
                "Sodium Tail: Mercury has a remarkable sodium tail that extends incredibly far into space - up to 10,000 Mercury radii \n"
                "(approximately 24 million kilometers). This tail is created when sodium atoms from Mercury's exosphere \n"
                "are pushed away by solar radiation pressure. The tail always points away from the Sun, similar to a comet's tail.\n\n"
                "The sodium tail is highly dynamic and can vary significantly based on Mercury's position in its orbit and solar activity. \n"
                "It's one of Mercury's most distinctive features and can be observed from Earth using specialized telescopes."
            ),
        },

        'magnetosphere': {
            'builder': 'mercury_visualization_shells.create_mercury_magnetosphere_shell',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.002 AU TO VISUALIZE.\n\n"
                "Magnetosphere: Mercury has a surprisingly active magnetosphere, given its small size and slow rotation. However, it is \n"
                "significantly weaker and smaller than Earth's magnetosphere."
            ),
        },

    },

    # ============================================================
    # Venus
    # ============================================================
    # Source: ESA Venus Express: Magnetosphere; NASA Pioneer Venus Results;
    #         induced magnetosphere, bow shock 1.3-1.7 Rv, comet-shaped tail.
    # Verified: April 2026 provenance audit.
    'Venus': {

        'magnetosphere': {
            'builder': 'venus_visualization_shells.create_venus_magnetosphere_shell',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Venus has a very weak, induced magnetosphere. Unlike Earth's magnetic field, which is generated internally by its \n"
                "liquid iron core, Venus's weak magnetosphere is formed by the interaction of the solar wind with the planet's \n"
                "ionosphere (the upper layer of its atmosphere containing charged particles). This induced magnetosphere is not as \n"
                "effective at deflecting charged particles from the Sun as Earth's strong magnetic field.\n\n"
                "The same builder also produces the bow shock trace (separate legend entry)."
            ),
        },

    },

    # ============================================================
    # Mars
    # ============================================================
    # Source: NASA MAVEN; NASA Solar System Exploration;
    #         induced magnetosphere, bow shock 1.5 Rm, crustal magnetic fields
    #         (Acuna et al. 1999 -- MGS MAG/ER discovery).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Mars': {

        'magnetosphere': {
            'builder': 'mars_visualization_shells.create_mars_magnetosphere_shell',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Unlike Earth, Mars lacks a global magnetic field generated by its core. Instead, it has:\n"
                "1. Induced Magnetosphere: Created by the interaction between the solar wind and Mars' ionosphere.\n"
                "2. Bow Shock: Forms where the solar wind first encounters Mars' atmosphere/ionosphere (~1.5 Mars radii).\n"
                "3. Crustal Magnetic Fields: Localized 'mini-magnetospheres' from magnetized regions in Mars' crust.\n\n"
                "The same builder produces all three traces (separate legend entries)."
            ),
        },

    },

    # ============================================================
    # Earth
    # ============================================================
    # Source: NASA Goddard Space Flight Center -- Magnetosphere overview;
    #         NASA Van Allen Probes (radiation belts, 2012-2019);
    #         NASA Heliophysics. Earth's magnetosphere extends ~10 R_E
    #         sunward, magnetotail ~100 R_E. Bow shock standoff ~15 R_E.
    #         Inner radiation belt ~1.5 R_E (protons), outer ~4.5 R_E (electrons).
    # Verified: April 2026 provenance audit.
    'Earth': {

        'magnetosphere': {
            'builder': 'earth_visualization_shells.create_earth_magnetosphere_shell',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n"
                "Earth's magnetosphere extends about 10 Earth radii on the Sun-facing side\n"
                "and stretches into a long magnetotail on the night side. It protects Earth\n"
                "from solar radiation and cosmic rays, making complex life possible.\n\n"
                "Bow Shock: The boundary where the supersonic solar wind is first slowed\n"
                "by Earth's magnetic field, typically located about 15 Earth radii upstream\n"
                "from Earth on the Sun-facing side.\n\n"
                "Inner Van Allen Belt: Region of trapped charged particles (mainly protons)\n"
                "extending from about 1,000 km to 6,000 km above Earth's surface.\n"
                "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons)\n"
                "extending from about 13,000 km to 60,000 km above Earth's surface.\n\n"
                "The same builder produces all four traces (separate legend entries):\n"
                "Magnetosphere, Bow Shock, Inner Radiation Belt, Outer Radiation Belt."
            ),
        },

        'leo': {
            'builder': 'earth_visualization_shells.create_earth_leo_shell',
            'tooltip': (
                "SET MANUAL SCALE TO 0.003 AU TO VISUALIZE.\n\n"
                "Low Earth Orbit (LEO) is the region from roughly 200 km to 2,000 km altitude\n"
                "(1.03 to 1.31 Earth radii), where satellites orbit at all inclinations.\n\n"
                "Unlike geostationary orbit, LEO satellites travel at all angles relative to the equator --\n"
                "forming a true shell around Earth rather than a ring. A LEO satellite completes\n"
                "one orbit in 90-120 minutes and crosses the sky in about 6 minutes.\n\n"
                "Notable LEO residents:\n"
                "  * ISS: ~400 km altitude, 51.6 deg inclination\n"
                "  * Starlink: ~550 km altitude, multiple inclination shells\n"
                "  * Hubble Space Telescope: ~540 km altitude\n"
                "  * Most Earth observation and weather satellites\n\n"
                "There are currently ~11,000 active satellites in LEO, with Starlink alone\n"
                "operating nearly 7,000. The total debris population (defunct satellites, rocket\n"
                "bodies, fragments >10 cm) exceeds 35,000 tracked objects.\n\n"
                "The bright moving 'stars' visible at dusk and dawn are LEO objects --\n"
                "most commonly Starlink trains. GEO satellites at 35,786 km are too faint\n"
                "and too slow to see with the naked eye."
            ),
        },

        'geostationary_belt': {
            'builder': 'earth_visualization_shells.create_earth_geostationary_belt_shell',
            'tooltip': (
                "SET MANUAL SCALE TO 0.003 AU TO VISUALIZE.\n\n"
                "The geostationary belt (GEO) is a ring of orbital space at 42,164 km from Earth's center\n"
                "(35,786 km altitude), where satellites orbit at exactly Earth's rotation rate\n"
                "and appear stationary over a fixed point on the equator.\n\n"
                "Approximately 550 active geostationary satellites currently occupy this belt --\n"
                "carrying TV broadcasts, weather imagery, GPS augmentation, and communications\n"
                "for roughly half the world's population.\n\n"
                "On April 13, 2029, asteroid Apophis will pass Earth at 38,013 km -- roughly 4,150 km\n"
                "INSIDE this belt. The closest operational satellites will be about 4,000 km away\n"
                "as it passes through. No impact risk to satellites is expected, but the flyby\n"
                "will be detectable from geostationary platforms as it transits the sky."
            ),
        },

    },


    # ============================================================
    # Jupiter
    # ============================================================
    # Source: NASA Juno Mission; NASA Galileo Mission; NASA Voyager 1/2;
    #         Galileo plasma instrument data (Io torus);
    #         NASA Jupiter Magnetosphere Overview.
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Jupiter': {

        'magnetosphere': {
            'builder': 'jupiter_visualization_shells.create_jupiter_magnetosphere',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.5 AU TO VISUALIZE.\n"
                "1.3 MB PER FRAME FOR HTML.\n\n"
                "Jupiter's magnetosphere is the largest in the solar system, extending up to\n"
                "~100 Jupiter radii on the sunward side and forming a magnetotail stretching\n"
                "beyond Saturn's orbit in the opposite direction. It traps charged particles,\n"
                "creating intense radiation belts that would be lethal to humans.\n\n"
                "Note: This visualization shows only the magnetosphere envelope. The bow shock\n"
                "(at ~80-100 R_J standoff) is not yet rendered; it can be added editorially in\n"
                "a future enhancement to match the Mercury/Venus/Mars/Earth pattern."
            ),
        },

        'io_plasma_torus': {
            'builder': 'jupiter_visualization_shells.create_jupiter_io_plasma_torus',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n"
                "634 KB PER FRAME FOR HTML.\n\n"
                "Donut-shaped region of charged particles from Jupiter's moon Io.\n"
                "Volcanic eruptions on Io eject sulfur and oxygen ions that become trapped\n"
                "in Jupiter's magnetic field, forming this distinctive structure at Io's\n"
                "orbital distance (~5.9 R_J). The torus is one of the brightest features in\n"
                "Jupiter's magnetosphere when viewed in UV wavelengths."
            ),
        },

        'radiation_belts': {
            'builder': 'jupiter_visualization_shells.create_jupiter_radiation_belts',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n\n"
                "Jupiter has three distinct radiation belts (Inner, Middle, Outer) at\n"
                "approximately 1.5, 3.0, and 6.0 Jupiter radii. Together they form the\n"
                "most intense radiation environment in the solar system -- thousands of\n"
                "times more intense than Earth's Van Allen belts.\n\n"
                "These regions trap high-energy charged particles in Jupiter's powerful\n"
                "magnetic field. The Galileo orbiter, Juno, and other spacecraft must\n"
                "carefully manage their trajectories to avoid prolonged exposure.\n\n"
                "The same builder produces all three traces (separate legend entries):\n"
                "Inner Radiation Belt, Middle Radiation Belt, Outer Radiation Belt."
            ),
        },

        'ring_system': {
            'builder': 'jupiter_visualization_shells.create_jupiter_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.003 AU TO VISUALIZE.\n\n"
                "Jupiter's ring system is faint and dusty, discovered by Voyager 1 in 1979.\n"
                "It consists of four components:\n"
                "  * Main Ring (122,500-129,000 km): bright thin ring, dust from Metis and Adrastea\n"
                "  * Halo Ring (100,000-122,500 km): faint torus inside the Main Ring\n"
                "  * Amalthea Gossamer Ring (129,000-182,000 km): very faint, dust from Amalthea\n"
                "  * Thebe Gossamer Ring (129,000-226,000 km): faintest, dust from Thebe\n\n"
                "The rings lie in Jupiter's equatorial plane and are composed of fine dust\n"
                "particles ejected from small inner moons by micrometeoroid impacts.\n\n"
                "The same builder produces all four ring traces (separate legend entries)."
            ),
        },

    },


    # ============================================================
    # Saturn
    # ============================================================
    # Source: NASA Saturn Fact Sheet; NASA Cassini Mission;
    #         NASA Saturn Magnetosphere Overview; Cassini Mission: Enceladus;
    #         NASA Voyager 2 Saturn Encounter; Mankovich & Fuller (2021).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Saturn': {

        'magnetosphere': {
            'builder': 'saturn_visualization_shells.create_saturn_magnetosphere',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.2 AU TO VISUALIZE.\n"
                "1.4 MB PER FRAME FOR HTML.\n\n"
                "Saturn has a large magnetosphere, the region of space dominated by its\n"
                "magnetic field. Saturn's magnetic field is unique because its magnetic\n"
                "axis is almost perfectly aligned with its rotational axis (~0 deg tilt).\n"
                "The magnetosphere deflects the solar wind and traps charged particles,\n"
                "creating auroras at the poles. Material from Enceladus's plumes\n"
                "contributes plasma to Saturn's magnetosphere and its E ring.\n\n"
                "Note: This visualization shows only the magnetosphere envelope. The bow\n"
                "shock (at ~22-27 R_S standoff) is not yet rendered; it can be added\n"
                "editorially in a future enhancement to match the Mercury/Venus/Mars/Earth\n"
                "pattern."
            ),
        },

        'enceladus_plasma_torus': {
            'builder': 'saturn_visualization_shells.create_saturn_enceladus_plasma_torus',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n"
                "634 KB PER FRAME FOR HTML.\n\n"
                "Donut-shaped region of charged particles primarily sourced from Saturn's\n"
                "moon Enceladus. Water vapor and icy particles vented from south-polar\n"
                "geysers (hundreds of kg/s) are ionized by UV radiation and electron\n"
                "bombardment, forming a torus centered on Enceladus's orbit (~3.95 R_S).\n"
                "The Enceladus plasma torus is a significant plasma source for Saturn's\n"
                "inner magnetosphere and feeds Saturn's diffuse E ring."
            ),
        },

        'radiation_belts': {
            'builder': 'saturn_visualization_shells.create_saturn_radiation_belts',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n"
                "Saturn has multiple distinct radiation belts trapped within its\n"
                "magnetosphere. Unlike Earth's relatively simple Van Allen belt structure,\n"
                "Saturn's belts are heavily shaped by its rings and moons, which absorb\n"
                "charged particles and create characteristic gaps.\n\n"
                "The visualization shows six belt regions defined by adjacent moon orbits:\n"
                "Belt from A-Ring to Mimas, Belt from Mimas to Enceladus, Belt from\n"
                "Enceladus to Tethys, Belt from Tethys to Dione, Belt from Dione to Rhea,\n"
                "and Belt outward of Rhea. The primary source of high-energy particles is\n"
                "the collision of galactic cosmic rays with Saturn's atmosphere.\n\n"
                "The same builder produces all six belt traces as separate legend entries."
            ),
        },

        'ring_system': {
            'builder': 'saturn_visualization_shells.create_saturn_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.005 AU TO VISUALIZE.\n"
                "22.2 MB PER FRAME FOR HTML.\n\n"
                "Saturn's spectacular ring system is composed primarily of water ice\n"
                "particles with some rocky debris and dust. The rings extend hundreds of\n"
                "thousands of kilometers from the planet but are typically only about\n"
                "10 meters thick.\n\n"
                "The visualization shows seven ring components from inner to outer:\n"
                "  * D Ring (66,900-74,500 km): innermost and faintest of the main rings\n"
                "  * C Ring (74,658-92,000 km): wider but fainter than A and B\n"
                "  * B Ring (92,000-117,500 km): brightest and most massive\n"
                "  * A Ring (122,340-136,800 km): outermost bright ring; Encke and Keeler\n"
                "    gaps shepherded by Pan and Daphnis\n"
                "  * F Ring (140,210-140,420 km): narrow, dynamic, shepherded by Pandora\n"
                "    and Prometheus\n"
                "  * G Ring (166,000-175,000 km): faint and dusty\n"
                "  * E Ring (180,000-480,000 km): broad, diffuse, sourced by icy particles\n"
                "    from Enceladus\n\n"
                "The rings lie in Saturn's equatorial plane (-26.73 deg axial tilt applied\n"
                "in the builder). The Cassini Division (4,800 km gap between A and B) is\n"
                "the most prominent gap.\n\n"
                "The same builder produces all seven ring traces as separate legend entries."
            ),
        },

    },


    # ============================================================
    # Uranus
    # ============================================================
    # Source: NASA Voyager 2 Mission; Ness et al. (1986) Science;
    #         Elliot et al. (1977) Nature; de Pater et al. (2006).
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Uranus': {

        'magnetosphere': {
            'builder': 'uranus_visualization_shells.create_uranus_magnetosphere',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.5 AU TO VISUALIZE.\n"
                "560 KB PER FRAME FOR HTML.\n\n"
                "Uranus's magnetosphere has the most extreme geometry of any planet:\n"
                "the magnetic axis is tilted 60 degrees from the rotation axis, and\n"
                "Uranus itself is tilted 97.77 degrees from its orbital plane. The\n"
                "result is a magnetosphere with no analog in the solar system, with\n"
                "the dipole axis sweeping a wide cone as Uranus rotates and modulating\n"
                "the solar-wind interaction on a ~17-hour cycle.\n\n"
                "Source: Ness et al. (1986) Science -- Voyager 2 magnetometer."
            ),
        },

        'radiation_belts': {
            'builder': 'uranus_visualization_shells.create_uranus_radiation_belts',
            'tooltip': (
                "560 KB PER FRAME FOR HTML.\n\n"
                "Uranus has two main radiation belt regions (Inner and Outer) at\n"
                "approximately 3-10 R_U. Voyager 2 (1986) measurements showed\n"
                "Uranus's electron belts are surprisingly intense -- comparable to\n"
                "Earth's, and much stronger than Saturn's. The source is primarily\n"
                "the planet's upper atmosphere.\n\n"
                "Voyager 2 was the first and so far only spacecraft to directly\n"
                "observe them during its flyby in 1986.\n\n"
                "The same builder produces both traces (separate legend entries):\n"
                "Inner Radiation Belt, Outer Radiation Belt."
            ),
        },

        'ring_system': {
            'builder': 'uranus_visualization_shells.create_uranus_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n\n"
                "Uranus has 13 known rings, discovered in 1977 via stellar\n"
                "occultation and confirmed by Voyager 2 in 1986. The rings are\n"
                "narrow, dark, and arranged in Uranus's near-vertical equatorial\n"
                "plane -- following the planet's 97.77-degree axial tilt rather\n"
                "than the orbital plane.\n\n"
                "Components rendered:\n"
                "  Rings 6, 5, 4 (innermost narrow rings)\n"
                "  Alpha, Beta, Eta, Gamma, Delta (mid rings)\n"
                "  Epsilon (outer narrow ring, brightest)\n"
                "  Nu, Mu (outer faint gossamer rings)\n\n"
                "Source: Elliot et al. (1977) Nature -- discovery via occultation;\n"
                "Voyager 2 (1986); de Pater et al. (2006) -- gossamer rings."
            ),
        },

    },


    # ============================================================
    # Neptune
    # ============================================================
    # Source: Voyager 2 Mission Archive; Ness et al. (1989, Science);
    #         Smith et al. (1989, Science); NASA Planetary Ring Node.
    # Verified: April 2026 provenance audit via Gemini fact-check.
    'Neptune': {

        'magnetosphere': {
            'builder': 'neptune_visualization_shells.create_neptune_magnetosphere',
            'needs_sun_position': True,
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.5 AU TO VISUALIZE.\n"
                "1.0 MB PER FRAME FOR HTML.\n\n"
                "Neptune's magnetosphere is dramatically tilted (47 degrees from\n"
                "the rotation axis) and significantly offset (more than half a\n"
                "Neptune radius from the planet's center). The result is an extremely\n"
                "asymmetric magnetosphere that varies greatly depending on Neptune's\n"
                "16-hour rotation.\n\n"
                "Rendered features:\n"
                "  * Magnetosphere envelope with internal 47-deg tilt + 60-deg azimuth\n"
                "  * Bow shock facing the actual Sun direction\n"
                "  * 4 magnetic-pole structures (mag center, axis, north, south poles)\n\n"
                "Source: Voyager 2 Mission Archive; Ness et al. (1989, Science) --\n"
                "the only spacecraft to visit Neptune; all parameters from the 1989 flyby."
            ),
        },

        'radiation_belts': {
            'builder': 'neptune_visualization_shells.create_neptune_radiation_belts',
            'tooltip': (
                "560 KB PER FRAME FOR HTML.\n\n"
                "Neptune has a complex radiation belt environment shaped by its\n"
                "47-degree-tilted, offset magnetic field. The belts include inner\n"
                "and outer regions plus a cusp region, with field-aligned currents\n"
                "(FAC) connecting magnetospheric regions.\n\n"
                "All parameters derive from the Voyager 2 flyby (1989), the only\n"
                "in-situ visit to Neptune.\n\n"
                "The same builder produces all belt + cusp + FAC traces (separate\n"
                "legend entries per region)."
            ),
        },

        'ring_system': {
            'builder': 'neptune_visualization_shells.create_neptune_ring_system',
            'tooltip': (
                "SET MANUAL SCALE TO AT LEAST 0.001 AU TO VISUALIZE.\n"
                "22.2 MB PER FRAME FOR HTML.\n\n"
                "Neptune has 5 named rings (Galle, Le Verrier, Lassell, Arago, Adams)\n"
                "plus diffuse outer dust. The Adams Ring is famous for its arc\n"
                "structure -- five named arcs (Courage, Liberte, Egalite 1, Egalite 2,\n"
                "Fraternite) confined by gravitational resonance with the moon\n"
                "Galatea.\n\n"
                "Source: NASA Planetary Ring Node; Smith et al. (1989, Science) --\n"
                "Voyager 2 encounter; subsequent Hubble and ground-based observations."
            ),
        },

    },


    # ============================================================
    # Sun
    # ============================================================
    # Source: NASA Solar Dynamics Observatory; NASA Parker Solar Probe;
    #         NASA Heliophysics; IAU 2015 nominal solar radius.
    # Verified: April 2026 provenance audit.
    # Phase D1: Config extraction only. Configs registered but not yet
    # invoked by unified dispatch. create_sun_visualization() stays alive.
    # Legend names follow Option A: clean 'name' values; at eventual
    # switchover, 6 non-conforming legend entries normalize to 'Sun: <X>'.
    # Module updated: May 2026 with Anthropic's Claude Opus 4.6
    'Sun': {

        'core': {
            'name': 'Core',
            'radius_au': CORE_AU,
            'color': 'rgb(70, 130, 180)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 10,
            'hover_text': core_info_hover,
            'tooltip': core_info,
        },

        'radiative': {
            'name': 'Radiative Zone',
            'radius_au': RADIATIVE_ZONE_AU,
            'color': 'rgb(30, 144, 255)',
            'opacity': 1.0,
            'n_points': 25,
            'marker_size': 7,
            'hover_text': radiative_zone_info_hover,
            'tooltip': radiative_zone_info,
        },

        'photosphere': {
            'name': 'Photosphere',
            'radius_au': SOLAR_RADIUS_AU,
            'color': 'rgb(255, 244, 214)',
            'opacity': 1.0,
            'geometry_type': 'mesh3d',
            'mesh_resolution': 24,
            'n_points': 25,
            'marker_size': 7.0,
            'hover_text': photosphere_info_hover,
            'tooltip': photosphere_info,
        },

        'chromosphere': {
            'name': 'Chromosphere',
            'radius_au': CHROMOSPHERE_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(30, 144, 255)',
            'opacity': 0.5,
            'n_points': 25,
            'marker_size': 3.0,
            'hover_text': chromosphere_info_hover,
            'tooltip': chromosphere_info,
        },

        'inner_corona': {
            'name': 'Inner Corona',
            'radius_au': INNER_CORONA_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(0, 0, 255)',
            'opacity': 0.45,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': inner_corona_info_hover,
            'tooltip': inner_corona_info,
        },

        'streamer_belt': {
            'name': 'Streamer Belt (Visible Corona)',
            'radius_au': STREAMER_BELT_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(255, 200, 80)',
            'opacity': 0.45,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': streamer_belt_info_hover,
            'tooltip': streamer_belt_info,
        },

        'roche_limit': {
            'name': 'Roche Limit (Comets)',
            'radius_au': ROCHE_LIMIT_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(200, 60, 60)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': roche_limit_info_hover,
            'tooltip': roche_limit_info,
        },

        'alfven_surface': {
            'name': 'Alfven Surface',
            'radius_au': ALFVEN_SURFACE_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(0, 200, 200)',
            'opacity': 0.35,
            'n_points': 20,
            'marker_size': 3.5,
            'hover_text': alfven_surface_info_hover,
            'tooltip': alfven_surface_info,
        },

        'outer_corona': {
            'name': 'Outer Corona',
            'radius_au': OUTER_CORONA_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(25, 25, 112)',
            'opacity': 0.5,
            'n_points': 20,
            'marker_size': 3.5,
            'hover_text': outer_corona_info_hover,
            'tooltip': outer_corona_info,
        },

        'termination_shock': {
            'name': 'Termination Shock',
            'radius_au': TERMINATION_SHOCK_AU,
            'color': 'rgb(240, 244, 255)',
            'opacity': 0.4,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': termination_shock_info_hover,
            'tooltip': termination_shock_info,
        },

        'heliopause': {
            'name': 'Heliopause',
            'radius_au': HELIOPAUSE_RADII * SOLAR_RADIUS_AU,
            'color': 'rgb(135, 206, 250)',
            'opacity': 0.4,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': solar_wind_info_hover,
            'tooltip': solar_wind_info,
        },

        'inner_oort_limit': {
            'name': 'Inner Limit of Oort Cloud',
            'radius_au': INNER_LIMIT_OORT_CLOUD_AU,
            'color': 'white',
            'opacity': 0.35,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': inner_limit_oort_info_hover,
            'tooltip': inner_limit_oort_info,
        },

        'inner_oort': {
            'name': 'Inner Oort Cloud',
            'radius_au': INNER_OORT_CLOUD_AU,
            'color': 'white',
            'opacity': 0.35,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': inner_oort_info_hover,
            'tooltip': inner_oort_info,
        },

        'outer_oort': {
            'name': 'Outer Oort Cloud',
            'radius_au': OUTER_OORT_CLOUD_AU,
            'color': 'white',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': outer_oort_info_hover,
            'tooltip': outer_oort_info,
        },

        'gravitational': {
            'name': 'Gravitational Influence',
            'radius_au': GRAVITATIONAL_INFLUENCE_AU,
            'color': 'rgb(102, 187, 106)',
            'opacity': 0.3,
            'n_points': 20,
            'marker_size': 3.0,
            'hover_text': gravitational_influence_info_hover,
            'tooltip': gravitational_influence_info,
        },

    },



    # ============================================================
    # Sun
    # ============================================================
    # Phase D1: Custom geometry shells for Sun.
    # Tooltips use source strings from solar_visualization_shells.py
    # (not composed text). No hover_text field -- Plotly hover text
    # lives inside the builder functions.
    # Module updated: May 2026 with Anthropic's Claude Opus 4.6
    'Sun': {

        'hills_cloud_torus': {
            'builder': 'solar_visualization_shells.create_sun_hills_cloud_torus',
            'tooltip': hills_cloud_torus_info,
        },

        'outer_oort_clumpy': {
            'builder': 'solar_visualization_shells.create_sun_outer_oort_clumpy',
            'tooltip': outer_oort_clumpy_info,
        },

        'galactic_tide': {
            'builder': 'solar_visualization_shells.create_sun_galactic_tide',
            'tooltip': galactic_tide_info,
        },

    },


    # Other bodies added in Phases D
}
