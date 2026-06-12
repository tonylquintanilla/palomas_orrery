"""
planet_visualization.py - High-level planet and Sun visualization orchestration.

Builds layered visualizations of solar system bodies (Sun, planets) for 3D
plots by assembling shell traces from the per-body *_visualization_shells.py
modules. Exposes the create_* functions called by palomas_orrery.py, plus
the info-text strings that populate hover tooltips for each shell.

Key functions:
    create_celestial_body_visualization(fig, body, shell_vars) - dispatch entry
    create_sun_visualization(fig, sun_shell_vars, animate, frames) - Sun shells
    create_planet_visualization(fig, planet, shell_vars) - planet shell assembly
    create_planet_shell_traces(planet, shell_vars) - return traces without adding

Consumed by: palomas_orrery.py, palomas_orrery_helpers.py

Part of Paloma's Orrery - Data Preservation is Climate Action

Module updated: May 2026 with Anthropic's Claude Opus 4.7
(provenance audit; body-radius aliases and solar/system constants now
imported from planet_visualization_utilities.py rather than redefined locally.
Removed shadow redefinition of KM_PER_AU.)

Updated 5/20/26 with Claude 4.6
Module updated: May 2026 with Anthropic's Claude Opus 4.7
(D3.1 follow-up: Sun Direction indicator fixes -- custom-only fallback for
outermost_radius_au, body_name passed for distinct multi-body indicators)
"""

import math
import numpy as np
import plotly.graph_objs as go
from constants_new import (
    KM_PER_AU, LIGHT_MINUTES_PER_AU, KNOWN_ORBITAL_PERIODS, CENTER_BODY_RADII)

# Shell consolidation imports (Step 3, Phase A)
from orrery_rendering import build_sphere_shell
from shell_configs import SHELL_CONFIGS, CUSTOM_SHELLS
from shared_utilities import create_sun_direction_indicator
import importlib

from solar_visualization_shells import (
    # Sun information texts
    gravitational_influence_info_hover,
    outer_oort_info_hover,
    inner_oort_info_hover,
    inner_limit_oort_info_hover,
    solar_wind_info_hover,
    termination_shock_info_hover,
    outer_corona_info_hover,
    inner_corona_info_hover,
    chromosphere_info_hover,
    photosphere_info_hover,
    radiative_zone_info_hover,
    core_info_hover
)  

from planet_visualization_utilities import (
    # Solar structure and atmosphere
    SOLAR_RADIUS_AU, CORE_AU, RADIATIVE_ZONE_AU,
    CHROMOSPHERE_RADII, INNER_CORONA_RADII, OUTER_CORONA_RADII,
    STREAMER_BELT_RADII, ROCHE_LIMIT_RADII, ALFVEN_SURFACE_RADII,
    # Heliosphere and beyond
    TERMINATION_SHOCK_AU, HELIOPAUSE_RADII,
    INNER_LIMIT_OORT_CLOUD_AU, INNER_OORT_CLOUD_AU, OUTER_OORT_CLOUD_AU,
    GRAVITATIONAL_INFLUENCE_AU,
    # Body-radius aliases (km and AU)
    MERCURY_RADIUS_KM, MERCURY_RADIUS_AU,
    VENUS_RADIUS_KM, VENUS_RADIUS_AU,
    EARTH_RADIUS_KM, EARTH_RADIUS_AU,
    MOON_RADIUS_KM, MOON_RADIUS_AU,
    MARS_RADIUS_KM, MARS_RADIUS_AU,
    JUPITER_RADIUS_KM, JUPITER_RADIUS_AU,
    SATURN_RADIUS_KM, SATURN_RADIUS_AU,
    URANUS_RADIUS_KM, URANUS_RADIUS_AU,
    NEPTUNE_RADIUS_KM, NEPTUNE_RADIUS_AU,
    PLUTO_RADIUS_KM, PLUTO_RADIUS_AU,
    ERIS_RADIUS_KM, ERIS_RADIUS_AU,
    PLANET9_RADIUS_KM, PLANET9_RADIUS_AU,
)

from solar_visualization_shells import (create_sun_core_shell,
                                        create_sun_radiative_shell,
                                        create_sun_photosphere_shell,
                                        create_sun_chromosphere_shell,
                                        create_sun_inner_corona_shell,
                                        create_sun_streamer_belt_shell,
                                        create_sun_roche_limit_shell,
                                        create_sun_alfven_surface_shell,                                        
                                        create_sun_outer_corona_shell,
                                        create_sun_termination_shock_shell,
                                        create_sun_heliopause_shell,

                                        create_sun_inner_oort_limit_shell,
                                        create_sun_inner_oort_shell,
                                        create_sun_outer_oort_shell,

                                        create_sun_hills_cloud_torus,
                                        create_sun_outer_oort_clumpy,
                                        create_sun_galactic_tide,
                                        create_sun_gravitational_shell)

from mercury_visualization_shells import (mercury_inner_core_info, 
                                          mercury_outer_core_info, 
                                          mercury_mantle_info, 
                                          mercury_crust_info, 
                                          mercury_atmosphere_info, 
                                          mercury_sodium_tail_info, 
                                          mercury_magnetosphere_info, 
                                          mercury_hill_sphere_info)

from venus_visualization_shells import (create_venus_core_shell,  
                                        create_venus_mantle_shell, 
                                          create_venus_crust_shell, 
                                          create_venus_atmosphere_shell, 
                                          create_venus_upper_atmosphere_shell,                                           
                                          create_venus_magnetosphere_shell, 
                                          create_venus_hill_sphere_shell,
                                          venus_core_info, 
                                          venus_mantle_info, 
                                          venus_crust_info, 
                                          venus_atmosphere_info, 
                                          venus_upper_atmosphere_info,                                           
                                          venus_magnetosphere_info, 
                                          venus_hill_sphere_info)

from earth_visualization_shells import (create_earth_inner_core_shell, 
                                        create_earth_outer_core_shell, 
                                        create_earth_lower_mantle_shell,
                                        create_earth_upper_mantle_shell, 
                                        create_earth_crust_shell, 
                                        create_earth_atmosphere_shell, 
                                        create_earth_upper_atmosphere_shell,                                           
                                        create_earth_magnetosphere_shell, 
                                        create_earth_hill_sphere_shell,
                                        create_earth_geostationary_belt_shell,
                                        create_earth_leo_shell,
                                        earth_inner_core_info, 
                                        earth_outer_core_info,
                                        earth_lower_mantle_info, 
                                        earth_upper_mantle_info,
                                        earth_crust_info, 
                                        earth_atmosphere_info, 
                                        earth_upper_atmosphere_info,                                           
                                        earth_magnetosphere_info, 
                                        earth_hill_sphere_info,
                                        earth_geostationary_belt_info,
                                        earth_leo_shell_info)

from moon_visualization_shells import (create_moon_inner_core_shell, 
                                        create_moon_outer_core_shell, 
                                        create_moon_mantle_shell,
                                        create_moon_crust_shell, 
                                        create_moon_exosphere_shell,  
                                        create_moon_hill_sphere_shell,
                                        moon_inner_core_info, 
                                        moon_outer_core_info,
                                        moon_mantle_info, 
                                        moon_crust_info, 
                                        moon_exosphere_info,  
                                        moon_hill_sphere_info)

from mars_visualization_shells import (create_mars_inner_core_shell, 
                                        create_mars_outer_core_shell, 
                                        create_mars_mantle_shell,
                                        create_mars_crust_shell, 
                                        create_mars_atmosphere_shell,
                                        create_mars_upper_atmosphere_shell,
                                        create_mars_magnetosphere_shell,                                           
                                        create_mars_hill_sphere_shell,
                                        mars_inner_core_info, 
                                        mars_outer_core_info,
                                        mars_mantle_info, 
                                        mars_crust_info, 
                                        mars_atmosphere_info, 
                                        mars_upper_atmosphere_info,
                                        mars_magnetosphere_info,                                           
                                        mars_hill_sphere_info)


from jupiter_visualization_shells import (create_jupiter_core_shell, 
                                        create_jupiter_metallic_hydrogen_shell, 
                                        create_jupiter_molecular_hydrogen_shell,
                                        create_jupiter_cloud_layer_shell, 
                                        create_jupiter_upper_atmosphere_shell,
                                        create_jupiter_ring_system,                                                                                   
                                        create_jupiter_radiation_belts,
                                        create_jupiter_io_plasma_torus,
                                        create_jupiter_magnetosphere, 
                                        create_jupiter_hill_sphere_shell,
                                        jupiter_core_info, 
                                        jupiter_metallic_hydrogen_info, 
                                        jupiter_molecular_hydrogen_info,
                                        jupiter_cloud_layer_info, 
                                        jupiter_upper_atmosphere_info,
                                        jupiter_ring_system_info,                                                                                   
                                        jupiter_radiation_belts_info,
                                        jupiter_io_plasma_torus_info,
                                        jupiter_magnetosphere_info, 
                                        jupiter_hill_sphere_info)

from saturn_visualization_shells import (create_saturn_core_shell, 
                                        create_saturn_metallic_hydrogen_shell, 
                                        create_saturn_molecular_hydrogen_shell,
                                        create_saturn_cloud_layer_shell, 
                                        create_saturn_upper_atmosphere_shell,
                                        create_saturn_ring_system,                                                                                   
                                        create_saturn_radiation_belts,
                                        create_saturn_enceladus_plasma_torus,
                                        create_saturn_magnetosphere, 
                                        create_saturn_hill_sphere_shell,
                                        saturn_core_info, 
                                        saturn_metallic_hydrogen_info, 
                                        saturn_molecular_hydrogen_info,
                                        saturn_cloud_layer_info, 
                                        saturn_upper_atmosphere_info,
                                        saturn_ring_system_info,                                                                                   
                                        saturn_radiation_belts_info,
                                        saturn_enceladus_plasma_torus_info,
                                        saturn_magnetosphere_info, 
                                        saturn_hill_sphere_info)

from uranus_visualization_shells import (create_uranus_core_shell, 
                                        create_uranus_mantle_shell, 
                                        create_uranus_cloud_layer_shell, 
                                        create_uranus_upper_atmosphere_shell,
                                        create_uranus_ring_system,                                                                                   
                                        create_uranus_radiation_belts,
                                        create_uranus_magnetosphere, 
                                        create_uranus_hill_sphere_shell,
                                        uranus_core_info, 
                                        uranus_mantle_info, 
                                        uranus_cloud_layer_info, 
                                        uranus_upper_atmosphere_info,
                                        uranus_ring_system_info,                                                                                   
                                        uranus_radiation_belts_info,
                                        uranus_magnetosphere_info, 
                                        uranus_hill_sphere_info)

from neptune_visualization_shells import (create_neptune_core_shell, 
                                        create_neptune_mantle_shell, 
                                        create_neptune_cloud_layer_shell, 
                                        create_neptune_upper_atmosphere_shell,
                                        create_neptune_ring_system,                                                                                   
                                        create_neptune_radiation_belts,
                                        create_neptune_magnetosphere, 
                                        create_neptune_hill_sphere_shell,
                                        neptune_core_info, 
                                        neptune_mantle_info, 
                                        neptune_cloud_layer_info, 
                                        neptune_upper_atmosphere_info,
                                        neptune_ring_system_info,                                                                                   
                                        neptune_radiation_belts_info,
                                        neptune_magnetosphere_info, 
                                        neptune_hill_sphere_info)

from pluto_visualization_shells import (create_pluto_core_shell,  
                                        create_pluto_mantle_shell,
                                        create_pluto_crust_shell, 
                                        create_pluto_haze_layer_shell, 
                                        create_pluto_atmosphere_shell,                                           
                                        create_pluto_hill_sphere_shell,
                                        pluto_core_info, 
                                        pluto_mantle_info,
                                        pluto_crust_info, 
                                        pluto_haze_layer_info, 
                                        pluto_atmosphere_info,                                           
                                        pluto_hill_sphere_info)

from eris_visualization_shells import (create_eris_core_shell,  
                                        create_eris_mantle_shell,
                                        create_eris_crust_shell,  
                                        create_eris_atmosphere_shell,                                           
                                        create_eris_hill_sphere_shell,
                                        eris_core_info, 
                                        eris_mantle_info,
                                        eris_crust_info, 
                                        eris_atmosphere_info,                                           
                                        eris_hill_sphere_info)

from planet9_visualization_shells import (create_planet9_surface_shell,                                           
                                        create_planet9_hill_sphere_shell,
                                        planet9_surface_info,                                           
                                        planet9_hill_sphere_info)


# Celestial body constants (solar structure, body radii, KM_PER_AU) are
# all imported from planet_visualization_utilities.py at the top of this
# file. Do not redefine them here. Single source of truth: constants_new.py.
# See protocol v3.20.

def create_sun_visualization(fig, sun_shell_vars, animate=False, frames=None):
    """RETIRED: Sun rendering migrated to unified dispatch (May 2026).

    Call sites in palomas_orrery.py now use create_celestial_body_visualization()
    directly. Asteroid belt geometry dispatched at call sites.

    Module updated: May 2026 with Anthropic's Claude Opus 4.6
    """
    raise NotImplementedError(
        "create_sun_visualization() retired May 2026. "
        "Use create_celestial_body_visualization(fig, 'Sun', ...) instead."
    )

def create_sun_corona_from_distance(fig, sun_shell_vars, sun_position):
    """RETIRED: Off-center Sun rendering migrated to unified dispatch (May 2026).

    Sun shells now render at any center via create_celestial_body_visualization()
    with center_position parameter. No special checkbox needed.

    Module updated: May 2026 with Anthropic's Claude Opus 4.6
    """
    raise NotImplementedError(
        "create_sun_corona_from_distance() retired May 2026. "
        "Use create_celestial_body_visualization(fig, 'Sun', ..., "
        "center_position=sun_position) instead."
    )
    
def create_celestial_body_visualization(fig, body_name, shell_vars, animate=False, frames=None,
                                        center_position=(0, 0, 0), sun_position=(0, 0, 0),
                                        object_type=None, center_object=None,
                                        skip_elements=None):

    """
    Unified config-driven dispatch for celestial body shell visualization.

    Looks up the body's shell configs in SHELL_CONFIGS (sphere shells) and
    CUSTOM_SHELLS (non-sphere geometry). Sphere shells route through
    build_sphere_shell(); custom shells are lazy-imported by registry entry.

    Issues ONE sun direction indicator per body at the outermost active
    shell radius, replacing the per-shell indicator calls that were
    duplicated across every shell function. The indicator is suppressed
    when the body is at the origin (body-centered view) because there
    is no meaningful sunward direction from the coordinate center.

    Step 3 Phase A: only Mercury is fully wired through this function. Other
    bodies continue to render via create_planet_visualization() blocks until
    their Phase B/C/D migrations land.

    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add traces to
        body_name (str): Body name as it appears in SHELL_CONFIGS keys
                         (e.g. 'Mercury', 'Pluto', 'Sun')
        shell_vars (dict): Maps shell var names to tk.IntVar.
                           Keys may be prefixed ('mercury_inner_core') or
                           bare ('inner_core') - prefix is stripped to match
                           config keys.
        animate (bool): Reserved for future animation hooks (unused in Phase A)
        frames (list): Reserved for future animation hooks (unused in Phase A)
        center_position (tuple): (x, y, z) AU position of the body's center
        object_type (str): Object type for sun direction indicator suppression
        center_object (str): Name of object at plot center (indicator suppression)
        sun_position (tuple): (x, y, z) AU position of the Sun. Default (0,0,0)
                            is correct for heliocentric views. Body-centered
                            views pass actual Sun offset. Phase D2.

    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    configs = SHELL_CONFIGS.get(body_name, {})
    customs = CUSTOM_SHELLS.get(body_name, {})

    # Strip body prefix from shell_vars keys to match config keys.
    # 'mercury_inner_core' -> 'inner_core'; bare keys (Sun) pass through.
    # 'Planet 9' becomes 'planet9_'.
    body_prefix = body_name.lower().replace(' ', '') + '_'

    outermost_radius_au = 0.0
    # D3.1 follow-up (May 2026, Bug 1): track whether any custom shell was
    # rendered, so the Sun Direction indicator can fall back to a body-radius
    # based scale when only custom shells are selected.
    custom_rendered = False

    for key, var in shell_vars.items():
        try:
            if var.get() != 1:
                continue
        except (AttributeError, TypeError):
            # var is not a tk.IntVar (e.g., plain int from tests)
            if not var:
                continue

        shell_name = key[len(body_prefix):] if key.startswith(body_prefix) else key

        # (C6d fix, June 2026) Elements the per-frame animation engine
        # owns for the CENTER body are skipped here -- the engine's
        # allocation provides their frame-1 content and animates them.
        # Static pipeline passes skip_elements=None (unaffected).
        if skip_elements and shell_name in skip_elements:
            continue

        if shell_name in configs:
            config = configs[shell_name]
            traces = build_sphere_shell(config, body_name, center_position)
            for t in traces:
                fig.add_trace(t)
            # Track outermost radius for indicator scaling
            if 'radius_au' in config:
                shell_r = config['radius_au']
            else:
                body_r = CENTER_BODY_RADII[body_name] / KM_PER_AU
                shell_r = config['radius_fraction'] * body_r
            outermost_radius_au = max(outermost_radius_au, shell_r)

        elif shell_name in customs and shell_name not in ('rotation_axis', 'dipole_cone'):
            # 'rotation_axis' and 'dipole_cone' are intentionally NOT shell-triggered.
            # They render once per body below, tied to BODY selection (Movement 2).
            # Excluding them here keeps them from also rendering via a shell checkbox.
            custom = customs[shell_name]
            module_path, func_name = custom['builder'].rsplit('.', 1)
            mod = importlib.import_module(module_path)
            builder = getattr(mod, func_name)
            # Phase D2: pass sun_position to magnetosphere builders.
            # Movement 2 (June 2026): pass planet_name to shared builders (the
            # rotation-axis primitive uses one builder for all bodies). Both are
            # opt-in flags; an entry that sets neither calls builder(center_position)
            # exactly as before -- behavior-preserving for every existing shell.
            kwargs = {}
            if custom.get('needs_sun_position'):
                kwargs['sun_position'] = sun_position
            if custom.get('needs_planet_name'):
                kwargs['planet_name'] = body_name
            traces = builder(center_position, **kwargs)
            for t in traces:
                fig.add_trace(t)
            # D3.1 follow-up (May 2026, Bug 1): mark that a custom shell was
            # rendered, so the post-loop fallback can pick a sensible indicator
            # scale when no sphere shell tracked an outermost radius.
            custom_rendered = True

        # If shell_name is in neither registry, silently skip.
        # In Phase A this is expected for bodies that haven't migrated yet
        # (their dispatch is still in create_planet_visualization).

    # Rotation axis (Movement 2): tied to BODY selection, not a shell checkbox.
    # This function runs once per plotted body, so building here renders the axis
    # whenever the body is plotted -- independent of which interior/field shells
    # are checked. The axis carries its own legend entry (showlegend=True on the
    # pole line) and toggles as a unit, so the user can still hide it via the
    # legend. Only the 11 bodies with a sourced spin pole have this entry.
    if 'rotation_axis' in customs:
        axis_custom = customs['rotation_axis']
        axis_mod_path, axis_func = axis_custom['builder'].rsplit('.', 1)
        axis_builder = getattr(importlib.import_module(axis_mod_path), axis_func)
        for t in axis_builder(center_position, planet_name=body_name):
            fig.add_trace(t)

    # Dipole cone (Movement 2): same body-triggered pattern as the rotation axis.
    # Pole-frame and Sun-independent, rendered once per plotted body that has a
    # sourced magnetic dipole (Uranus, Neptune). Carries its own legend entry and
    # toggles as a unit; bodies without a 'dipole_cone' entry get nothing (the
    # builder also returns [] for any body absent from PLANET_DIPOLE).
    if 'dipole_cone' in customs:
        dc_custom = customs['dipole_cone']
        dc_mod_path, dc_func = dc_custom['builder'].rsplit('.', 1)
        dc_builder = getattr(importlib.import_module(dc_mod_path), dc_func)
        for t in dc_builder(center_position, planet_name=body_name):
            fig.add_trace(t)

    # ONE sun direction indicator per body (replaces ~50 per-shell calls).
    # Uses outermost active shell radius for scaling. Suppresses at origin
    # (body-centered view) and for Sun shells.

    # D3.1 follow-up (May 2026, Bug 1): custom-only fallback.
    # The loop above tracks outermost_radius_au only inside the SHELL_CONFIGS
    # branch. When the user selects only custom shells (magnetosphere, rings,
    # radiation belts, LEO/GEO, plasma torus, FACs), outermost_radius_au stays
    # 0 and the indicator was suppressed entirely -- exactly the wrong outcome,
    # since magnetosphere shells are rotated to face the Sun and benefit most
    # from a sunward marker. Fallback: 100x body radius, matching the legacy
    # per-shell call pattern (e.g. 100 * EARTH_RADIUS_AU in the dormant
    # create_earth_magnetosphere_shell). The fallback only triggers when no
    # sphere shell was rendered AND at least one custom shell was rendered.
    if outermost_radius_au == 0 and custom_rendered and body_name in CENTER_BODY_RADII:
        body_r_au = CENTER_BODY_RADII[body_name] / KM_PER_AU
        outermost_radius_au = 100.0 * body_r_au

    if outermost_radius_au > 0 and not (skip_elements
            and 'sun_direction_indicator' in skip_elements):
        indicator_traces = create_sun_direction_indicator(
            center_position=center_position,
            sun_position=sun_position,
            shell_radius=outermost_radius_au,
            object_type=object_type if object_type is not None else body_name,
            center_object=center_object,
            body_name=body_name,
        )
        for t in indicator_traces:

            fig.add_trace(t)

    # Store outermost shell radius for axis auto-scaling.
    # Consumed by palomas_orrery.py to set axis_range = [-2*r, 2*r]
    # when Auto scaling is active. Bodies that haven't migrated to the
    # unified dispatch don't set this attribute -- old behavior continues.
    if outermost_radius_au > 0:
        fig._shell_outermost_radius_au = outermost_radius_au

    return fig


#####################################
# Planet Visualization Functions
#####################################

def create_planet_visualization(fig, planet_name, shell_vars, animate=False, frames=None, center_position=(0, 0, 0), sun_position=(0, 0, 0)):

    """
    RETIRED (June 2026, animation refactor Phase 2.5 / D.Structural 3).
    Zero live call sites remain in the pipelines: all three former callers in
    palomas_orrery.py (add_center_body_shells planet branch; the static
    planets_with_shells center-fallback and non-center sites) now call
    create_celestial_body_visualization directly with the true
    center_object=center_object_name -- the Phase-D correction the per-body
    delegation notes below anticipated. palomas_orrery_helpers.py still
    IMPORTS this name (dead import; rides the D.Structural 5/6 cleanup
    sweeps). Kept as dead code per discipline (annotate; do not remove
    without grep-confirm at sweep time). DO NOT add new callers.

    --- original docstring ---
    Creates a visualization of a planet's layers based on which shells are selected.
    Works for both static plots and animations.
    
    Parameters:
        fig (plotly.graph_objects.Figure): The figure to add the visualization to
        planet_name (str): Name of the planet 
        shell_vars (dict): Dictionary of selection variables for each planet shell
        animate (bool): Whether this is for an animated plot
        frames (list, optional): List of frames for animation
        center_position (tuple): (x, y, z) position of the planet's center
        
    Returns:
        plotly.graph_objects.Figure: The updated figure
    """
    # Create base traces for static visualization
    traces = []
    
    # Create shell traces based on selected variables

    if planet_name == 'Mercury':
        # Step 3 Phase A: delegate to unified config-driven dispatch.
        # See create_celestial_body_visualization() for the new architecture.
        # NOTE: center_object hardcoded to body_name here because
        # create_planet_visualization does not receive the plot's center body.
        # This becomes correct in Phase D when callers use the unified function
        # directly with center_object=center_object_name.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Mercury',
            center_object='Mercury',
        )

    if planet_name == 'Venus':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Custom geometry: venus_magnetosphere -> CUSTOM_SHELLS['Venus']['magnetosphere']
        # which lazy-imports and emits both magnetosphere and bow shock traces.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Venus',
            center_object='Venus',
        )

    if planet_name == 'Earth':
        # Step 3 Phase C2: delegate to unified config-driven dispatch.
        # Custom geometry: earth_magnetosphere -> CUSTOM_SHELLS['Earth']['magnetosphere']
        # which lazy-imports and emits magnetosphere + bow shock + 2 Van Allen belt traces.
        # earth_leo and earth_geostationary_belt also lazy-imported via CUSTOM_SHELLS.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Earth',
            center_object='Earth',
        )

    if planet_name == 'Moon':
        # Step 3 Phase B: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A). NOTE: center_object hardcoded
        # to body_name here because create_planet_visualization does not
        # receive the plot's center body. Corrected in Phase D when callers
        # use the unified function directly.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Moon',
            center_object='Moon',
        )

    if planet_name == 'Mars':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Custom geometry: mars_magnetosphere -> CUSTOM_SHELLS['Mars']['magnetosphere']
        # which lazy-imports and emits magnetosphere, bow shock, and crustal fields.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Mars',
            center_object='Mars',
        )

    if planet_name == 'Jupiter':
        # Step 3 Phase C3: delegate to unified config-driven dispatch.
        # Custom geometry: jupiter_magnetosphere, jupiter_io_plasma_torus,
        # jupiter_radiation_belts (3 belts), jupiter_ring_system (4 rings)
        # via CUSTOM_SHELLS lazy import.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Jupiter',
            center_object='Jupiter',
        )

    if planet_name == 'Saturn':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Custom geometry: saturn_magnetosphere, saturn_enceladus_plasma_torus,
        # saturn_radiation_belts (6 belts), saturn_ring_system (7 rings)
        # via CUSTOM_SHELLS lazy import.
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Saturn',
            center_object='Saturn',
        )

    if planet_name == 'Uranus':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Same pattern as Saturn (Phase C4, this session).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Uranus',
            center_object='Uranus',
        )

    if planet_name == 'Neptune':
        # Step 3 Phase C4: delegate to unified config-driven dispatch.
        # Same pattern as Saturn / Uranus (Phase C4, this session).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Neptune',
            center_object='Neptune',
        )

    if planet_name == 'Pluto':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A), Moon/Planet 9 (Phase B).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Pluto',
            center_object='Pluto',
        )

    if planet_name == 'Eris':
        # Step 3 Phase C1: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A), Moon/Planet 9 (Phase B).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Eris',
            center_object='Eris',
        )

    if planet_name == 'Planet 9':
        # Step 3 Phase B: delegate to unified config-driven dispatch.
        # Same pattern as Mercury (Phase A) and Moon (Phase B above).
        return create_celestial_body_visualization(
            fig, planet_name, shell_vars,
            animate=animate, frames=frames,
            center_position=center_position, sun_position=sun_position, 
            object_type='Planet 9',
            center_object='Planet 9',
        )
    
    # Add base traces to figure for static visualization
    for trace in traces:
        fig.add_trace(trace)

    # If this is for animation, add the traces to each frame
    if animate and frames is not None:
        for frame in frames:
            frame_data = list(frame.data)  # Convert tuple to list if necessary
            frame_data.extend(traces)
            frame.data = frame_data

    return fig

def create_planet_shell_traces(planet_name, shell_vars, center_position=(0, 0, 0)):
    """
    Creates traces for planet shells without adding them to a figure.
    Useful for animations where traces need to be created for each frame.
    
    Parameters:
        planet_name (str): Name of the planet
        shell_vars (dict): Dictionary of selection variables for each planet shell
        center_position (tuple): (x, y, z) position of the planet's center
        
    Returns:
        list: List of plotly traces
    """
    traces = []
    
    # Get the prefix for this planet's shell variables
    prefix = planet_name.lower() + "_"
    
    # Check each shell variable and add corresponding traces if selected
    for shell_name, var in shell_vars.items():
        if var.get() == 1:
            # Extract the actual shell name without the planet prefix
            shell_type = shell_name.replace(prefix, "")
            
            # Dynamically call the appropriate shell creation function
            creation_func_name = f"create_{planet_name.lower()}_{shell_type}_shell"
            if creation_func_name in globals():
                creation_func = globals()[creation_func_name]
                new_traces = creation_func(center_position=center_position)
                traces.extend(new_traces)
            else:
                print(f"Warning: No creation function found for {shell_type} shell of {planet_name}")
    
    # Fix the hovertemplate for all traces
    for trace in traces:
        # Ensure proper customdata for hovering
        if hasattr(trace, 'customdata'):
            if isinstance(trace.customdata, list):
                # Make sure all customdata items reference the correct planet
                trace.customdata = [str(item).replace("Mercury", planet_name).replace("Venus", planet_name).replace("Earth", planet_name).replace("Moon", planet_name)
                                    .replace("Mars", planet_name).replace("Jupiter", planet_name).replace("Saturn", planet_name)
                                    .replace("Uranus", planet_name).replace("Neptune", planet_name).replace("Pluto", planet_name)
                                    .replace("Eris", planet_name).replace("Planet 9", planet_name)
                            if "Mercury" in str(item) or "Venus" in str(item) or "Earth" in str(item) or "Moon" in str(item) or "Mars" in str(item)
                                or "Jupiter" in str(item) or "Saturn" in str(item) or "Uranus" in str(item) or "Neptune" in str(item)
                                or "Pluto" in str(item) or "Eris" in str(item) or "Planet 9" in str(item)
                            else str(item) for item in trace.customdata]
        
        # Set correct hovertemplate
        trace.hovertemplate = '%{text}<extra></extra>'
    
    return traces


