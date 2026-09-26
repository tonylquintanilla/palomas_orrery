"""
earth_visualization_shells.py - Earth interior and orbital shell traces.

Sphere shells for Earth's interior layers (inner core through crust),
atmosphere, and upper atmosphere. Custom geometry for the magnetosphere,
LEO altitude shell, and geostationary belt. Each function returns Plotly
Scatter3d traces positioned relative to a center_position in AU.

Consumed by: planet_visualization.py (routing dispatcher)

Role: rendering/shells
Domain: earth_science

Module updated: May 2026 with Anthropic's Claude Opus 4.7
Module updated: September 2026 with Anthropic's Claude Fable 5.1 --
    L-291: magnetosphere, bow shock, LEO, geostationary and Hill sphere
    values read constants_new.py; no drawn literal remains.
    April 17, 2026: provenance audit source citations added, Gemini fact-check applied.
    Stratopause/tropopause temperature label corrected. LEO satellite/debris
    counts updated to 2026 values. Hill sphere typo fixed.
    Provenance audit identified by Anthropic's Claude Opus 4.7
May 27, 2026: Stage 3 info-marker standard sweep (Opus 4.7). Re-applied
    after recovery from a single-file regression incident -- this file's
    /mnt/project snapshot at session start was a stale pre-Phase-D2
    version (lost magnetosphere sun_position parameter, lost
    rotate_to_sunward() calls, lost partial create_info_marker factory
    adoption). Recovered by starting from the May 21 GitHub baseline that
    Tony uploaded after visual verification caught the magnetosphere
    rotation regression. 8 interior/atmosphere/hill_sphere inline marker
    dicts converted to red-border standard. The 5 already-factory sites
    (magnetosphere, bow shock, 2 radiation belts, LEO, GEO) unchanged
    -- factory style already matches the new standard.
May 27, 2026 (Thread 1 cleanup, Opus 4.7): per-shell sun_traces calls
    in upper_atmosphere and hill_sphere removed -- duplicates of the
    unified dispatch's post-loop Sun Direction indicator (v9 Residual
    Cleanup item 1). Dead create_sun_direction_indicator import removed.
May 28, 2026: Phase 1 re-pipe (Opus 4.7). 1 live inline info marker
    converted to factory call (Hill Sphere). Van Allen loop retrofit
    to per-belt borders (white on inner reddish belt, red on outer
    blue belt) per the two-standards convention locked this session
    (red border default; white border for reddish fills). The 5 sites
    already factory-routed in this file (magnetosphere, bow shock,
    Van Allen loop, LEO, GEO) were untouched -- they already use the
    factory default (red border) and Tony's earlier Mode 5 testing
    marked them acceptable.
August 26, 2026 (L-254, Opus 5): the eight dead create_earth_*_shell
    functions are marked as dead in their own docstrings, and the
    dispatch note above the section says which three are live. No
    function removed and no behaviour changed -- the sweep is L-254.
August 26, 2026 (L-249, Opus 5): the four interior info strings stop
    typing their boundary figures and interpolate constants_new.py
    instead, and the four dead create_earth_*_shell builders take their
    radius_fraction from the same constants. Tony's ruling that day:
    constants_new.py is the only store for a numeric value, in prose as
    much as in code, and a literal in dead code is still a store.
September 12, 2026 (L-305, Opus 5): the two magnetosphere standoffs are
    superseded in constants_new.py -- Shue et al. (1998) for the
    magnetopause, Jelinek et al. (2012) for the bow shock -- so the six
    quotes of them here round to the reporting figure their rows state,
    the retired Lugaz-midpoint sentence is deleted, and the bow shock's
    source attribution moves from Lugaz to Jelinek. Deletion and
    correction only; the rewrite is item 7.
September 22, 2026 (L-322 Stage C2, Opus 5): the four quotes of the two
    standoffs print at the count their rows declare, read from the store
    by _declared(), where they printed four figures by a fixed format
    (provenance-discipline 2.17, Rule 7) -- the rows are arithmetic again
    and declare three. The outer belt's typed "L = 4 to 5" band prints
    from the two band rows now in the store. Three comments that typed a
    dipole tilt in degrees now name the store row instead.
September 25, 2026 (L-322 Stage D, patch D8, Opus 5.5): Earth's
    magnetosphere is drawn from constants_new.py. The magnetopause is
    Shue's own surface, stopped at the store's cut angle, where it was an
    ellipsoid with widths chosen by eye; the tail starts where that
    surface stops, widens in a straight line to where Slavin et al. (1985)
    found it stops widening, keeps the width they measured, and ends
    where ISEE-3 stopped observing it. Five numbers chosen by eye are
    gone: the 12 and 10 widths and the tail's 100, 15 and 25. Each
    radiation belt is drawn across its inner and outer edge rows, with a
    brighter ring at the peak, where it was a 0.5 Earth-radius spread
    chosen by eye (belt_thickness). The hover and the checkbox tooltip
    say what is measured and what is our rule. Earth no longer calls the
    shared create_magnetosphere_shape; the other planets still do.
September 25, 2026 (L-322 Stage D, patch D9, Opus 5.5): the belts' rings
    are evenly spaced, on a step that lands on both edge rows and on the
    peak row, so the brighter ring sits at the peak's true place and no
    gap is uneven (Tony's Mode 5 note on D8: the uneven gaps read as a
    physical feature). The peak ring is fully opaque and drawn with larger
    points. The hover says the belt is one continuous region and the
    rings only mark its extent.
Module updated: September 25, 2026 with Anthropic's Claude Opus 5.5
"""
import numpy as np
import math
import plotly.graph_objs as go
# L-322 Stage D, patch D8: create_magnetosphere_shape is no longer
# imported; Earth draws Shue's surface itself (_earth_magnetosphere_points).
from planet_visualization_utilities import (EARTH_RADIUS_AU, create_sphere_points, create_bow_shock_shape)
from constants_new import (
    KM_PER_AU,  # L-178: direct km<->AU conversion, no shadow constant
    # L-249: Earth's interior boundaries have exactly one home. The _KM
    # values below are quoted in the info strings; the _RADII draw the
    # dead builders further down. Neither is ever retyped as a literal.
    EARTH_MEAN_RADIUS_KM,
    EARTH_INNER_CORE_KM, EARTH_INNER_CORE_RADII,
    EARTH_OUTER_CORE_KM, EARTH_OUTER_CORE_RADII,
    EARTH_D660_DEPTH_KM, EARTH_LOWER_MANTLE_RADII,
    EARTH_UPPER_MANTLE_KM, EARTH_UPPER_MANTLE_RADII,
    # L-291: the orbital and magnetospheric shells read the store too.
    # Every number a hover quotes below is formatted from these names.
    EARTH_EQUATORIAL_RADIUS_KM,
    EARTH_MAGNETOPAUSE_STANDOFF_RADII, EARTH_BOW_SHOCK_STANDOFF_RADII,
    EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII,
    # L-305 item 7: the belt edges and the observed magnetotail extent.
    # The spans used to be typed into the strings below.
    EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE, EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE,
    EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE, EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE,
    EARTH_MAGNETOTAIL_OBSERVED_RADII,
    # L-322 Stage D, patch D8: the magnetopause's shape and the tail's.
    # Shue's flaring coefficients and the declared north-south field give
    # the surface; the cut angle stops it; the four tail rows build the
    # tail.
    EARTH_MAGNETOPAUSE_SHUE_A6, EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT,
    EARTH_MAGNETOPAUSE_SHUE_A8, EARTH_SOLAR_WIND_BZ_NT,
    EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG,
    EARTH_MAGNETOTAIL_FLARE_END_RADII, EARTH_MAGNETOTAIL_DIAMETER_RADII,
    EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII, EARTH_MAGNETOTAIL_DRAWN_END_RADII,
    # L-322 Stage C2: the band the outer belt's drawn peak is the midpoint
    # of. The hover typed it as literal text until then.
    EARTH_VAN_ALLEN_OUTER_BAND_LOW_L, EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L,
    # L-305 item 7 part 4: the conditions a model standoff is evaluated at,
    # and how far real crossings sit from the surface it draws.
    EARTH_SOLAR_WIND_PRESSURE_NPA,
    EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII,
    EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII,
    EARTH_LEO_INNER_KM, EARTH_LEO_OUTER_KM,
    EARTH_LEO_INNER_RADII, EARTH_LEO_OUTER_RADII,
    EARTH_LEO_LOWER_ALTITUDE_KM, EARTH_LEO_UPPER_ALTITUDE_KM,
    EARTH_GEOSTATIONARY_RADIUS_KM, EARTH_GEOSTATIONARY_RADII,
    EARTH_HILL_SPHERE_KM, EARTH_HILL_SPHERE_RADII,
)
from orrery_rendering import rotate_to_sunward, create_info_marker
import constants_new as _store
from constants_rows import figures_of, uncertainty_of


def _declared(name):
    """Store row `name` as text, at the figure count its row declares.

    L-322 Stage C2. The provenance skill's display rule: a display prints
    the declared count, never more, and never chooses fewer. The value is
    taken from the store by the same name as the count, so the two cannot
    come from different rows. It formats with the skill's rounding rule,
    percent-g, which switches to exponent notation when the count is
    below a number's whole digits, so it is used only for the small
    numbers at the sites below. A way for every orrery display to format
    by the declared count is the follow-on recorded on L-322, not this.
    """
    return "%.*g" % (figures_of(name), getattr(_store, name))


def _with_uncertainty(name):
    """A row's value and its stated uncertainty as text, for a hover:
    ("120", "10") for EARTH_MAGNETOTAIL_FLARE_END_RADII.

    The value ends in the same decimal place as the uncertainty, which is
    how the reference page on significant figures says a value is printed
    with its uncertainty beside it. That place must also be the one the
    row's declared figure count gives, or the row and the hover would say
    different things; a mismatch raises instead of printing either one
    (provenance-discipline Rule 7: a display prints the declared count).
    L-322 Stage D, patch D8.
    """
    value = getattr(_store, name)
    stated = uncertainty_of(name)
    if stated is None:
        raise ValueError("%s states no uncertainty" % name)
    number, literal = stated
    if "." in literal:
        place = -len(literal.split(".", 1)[1])
    else:
        # A whole number's trailing zeros are placeholders: "10" states
        # the tens place, as the figures checker reads it.
        place = len(literal) - len(literal.rstrip("0"))
    figures = figures_of(name)
    count_place = int(math.floor(math.log10(abs(value)))) - figures + 1
    if count_place != place:
        raise ValueError(
            "%s declares %s figures, which end at 10^%d, but its "
            "uncertainty %s ends at 10^%d" % (name, figures, count_place,
                                             literal, place))
    if place >= 0:
        return "%.0f" % round(value, -place), literal
    return "%.*f" % (-place, value), literal


def _whole_figures(name):
    """A row at its declared count, written out in full rather than in
    exponent form: 220 at two figures prints "220", where percent-g would
    print "2.2e+02". For whole-number rows only. L-322 Stage D, patch D8.
    """
    figures = figures_of(name)
    value = float("%.*g" % (figures, getattr(_store, name)))
    if value != int(value):
        raise ValueError("%s is not a whole number at %s figures"
                         % (name, figures))
    return "%d" % int(value)


def _even_belt_rings(inner, peak, outer):
    """Ring radii for one radiation belt, and which ring is the peak.

    The rings are evenly spaced from the inner edge to the outer edge, on
    the largest step that also lands exactly on the peak: the greatest
    common divisor of the two distances, edge to peak and peak to edge,
    taken on the rows' decimal values. At the rows as they stand, the
    inner belt gets ten rings with the peak fifth from the inside, and the
    outer belt nine with the peak fourth. Both peaks sit nearer the inner
    edge than the middle, and the drawing shows that. (The rows' values
    are not repeated here: this comment would be a second home for them.)

    L-322 Stage D, patch D9 (Tony, 2026-09-25, option 2 of two: "even
    spacing with enough rings so that the peak ring can be identified at
    the correct radius fraction"). D8 added the peak ring on top of five
    evenly spaced rings, so it landed beside one of them and the gaps
    stopped being equal, which read as a physical feature.

    The ring positions are the rows' own values; only the ring COUNT is a
    rendering matter, and it follows from the rows. max_rings is a
    rendering cap: a row typed with more decimals would make the step
    tiny and the count huge, and this refuses rather than drawing
    hundreds of rings.
    """
    from fractions import Fraction
    max_rings = 25
    a = Fraction(inner).limit_denominator(1000)
    p = Fraction(peak).limit_denominator(1000)
    b = Fraction(outer).limit_denominator(1000)
    if not a < p < b:
        raise ValueError("belt rows out of order: inner %g, peak %g, "
                         "outer %g" % (inner, peak, outer))
    low, high = p - a, b - p
    step = Fraction(math.gcd(low.numerator * high.denominator,
                             high.numerator * low.denominator),
                    low.denominator * high.denominator)
    count = int((b - a) / step) + 1
    if count > max_rings:
        raise ValueError("a belt from %g to %g with its peak at %g needs %d "
                         "evenly spaced rings to put one on the peak; the "
                         "cap is %d" % (inner, outer, peak, count, max_rings))
    radii = [float(a + step * k) for k in range(count)]
    return radii, int((p - a) / step)


# L-231 (2026-09-15): the belts are drawn in Earth's equatorial plane now,
# using the same call Saturn's belt builder has always used.
from idealized_orbits import orient_to_planet_pole


def _km_above_surface(radii, sig):
    """Altitude above Earth's equatorial surface, in km, from a geocentric
    distance in Earth radii, rounded to `sig` significant figures.

    L-305 item 7 (2026-09-14). Two things live here on purpose.

    The SUBTRAHEND is EARTH_EQUATORIAL_RADIUS_KM, not the mean radius, and
    that is not a taste. Everything in these shells is scaled by
    EARTH_RADIUS_AU, which is equatorial; L-178 retired a local mean-radius
    copy because mixing the two put a small systematic error into every
    altitude band. A hover that subtracted a different Earth from the one the
    shell is drawn against would put two Earths in one exhibit.

    The ROUNDING lives here rather than in the text, because a rounded figure
    typed into a string is exactly the failure this item removes, one digit
    smaller.

    `sig` is DECLARED, not derived. A Python float cannot say whether its
    source wrote "2" or "2.0", so nothing here can read the figure count off
    the input. Two is a choice, made for the callers this helper has: belt
    rows stated as schematic spans carrying one or two figures each, where a
    four-digit altitude would claim precision the input does not have. It
    over-reports the ends their sources state to a single figure, and that
    is the declared cost of one uniform rule over a per-number judgment.
    A caller whose row supports more figures must pass its own `sig`; this
    default must not be read as a claim about that row's source.
    """
    km = (radii - 1.0) * EARTH_EQUATORIAL_RADIUS_KM
    if km <= 0.0:
        return 0
    step = 10.0 ** (math.floor(math.log10(km)) - (sig - 1))
    return int(round(km / step) * step)

# Earth Shell Creation Functions
#
# DISPATCH, read this before editing anything below (L-254, 2026-08-26).
# Eleven create_earth_*_shell functions live in this file. THREE are on
# the live render path, all of them reached through a CUSTOM_SHELLS
# 'builder' string that planet_visualization.py resolves by rsplit and
# getattr:
#     create_earth_magnetosphere_shell
#     create_earth_leo_shell
#     create_earth_geostationary_belt_shell
# The other EIGHT are dead. They are imported at planet_visualization.py
# lines 129-139 and called nowhere. Sphere shells render through
# SHELL_CONFIGS -> build_sphere_shell() -> create_info_marker() instead,
# and have since the Phase A-D migration; orrery_rendering.py's docstring
# has recorded it since May 2026. Each dead function says so in its own
# docstring below.
#
# The _info strings above are NOT dead. They are the canonical `\n` form,
# read by the Tk checkbox tooltips through celestial_objects.
# get_shell_tooltip_names() and globals(), and imported by
# shell_configs.py, which derives `<br>` from them at the Plotly boundary.
# Editing one changes what the user reads in two places. Editing a dead
# function below changes nothing at all.

# Source: USGS Interior of the Earth, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_inner_core_info = (
            "Earth's inner core is a solid sphere composed primarily of iron and nickel.\n"
            "Despite incredible pressure, temperatures of 5,400 degC (9,800 degF) keep it nearly\n"
            "at melting point. It rotates slightly faster than the rest of Earth, creating\n"
            "complex dynamics in Earth's magnetic field. The inner core is\n"
            f"{EARTH_INNER_CORE_KM:,.1f} km in radius.\n\n"
            "Source (radius): Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter. 25:297."
)

def create_earth_inner_core_shell(center_position=(0, 0, 0)):
    """Creates Earth's inner core shell.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': EARTH_INNER_CORE_RADII,  # L-249: derived, not typed
        'color': 'rgb(255, 180, 140)',  # Orange-red for hot iron core
        'opacity': 1.0,
        'name': 'Inner Core',
        'description': earth_inner_core_info.replace('\n', '<br>')
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=4.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: USGS Interior of the Earth, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_outer_core_info = (
            "The outer core is a liquid layer of iron, nickel, and lighter elements.\n"
            "Convection currents in this highly conductive fluid generate Earth's\n"
            "magnetic field through a process called the geodynamo. It extends from\n"
            f"{EARTH_INNER_CORE_KM:,.1f} to {EARTH_OUTER_CORE_KM:,.0f} km from Earth's center and has temperatures ranging from\n"
            "4,500 degC (8,100 degF) to 5,400 degC (9,800 degF).\n\n"
            "Source (radius): Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter. 25:297."
)

def create_earth_outer_core_shell(center_position=(0, 0, 0)):
    """Creates Earth's outer core shell.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': EARTH_OUTER_CORE_RADII,  # L-249: derived, not typed
        'color': 'rgb(255, 140, 0)',  # Deeper orange for liquid metal
        'opacity': 0.8,
        'name': 'Outer Core',
        'description': earth_outer_core_info.replace('\n', '<br>')
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.7,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: USGS Interior of the Earth, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_lower_mantle_info = (
            "The lower mantle is composed of solid silicate rocks rich in iron and magnesium.\n"
            "Despite being solid, it flows very slowly through convection, driving plate tectonics.\n"
            f"This region extends from {EARTH_D660_DEPTH_KM:,.0f} to "
            f"{EARTH_MEAN_RADIUS_KM - EARTH_OUTER_CORE_KM:,.0f} km below Earth's surface and experiences\n"
            "temperatures from 2,200 degC to 4,500 degC (4,000 degF to 8,100 degF) and extreme pressure.\n\n"
            "Source (boundaries): Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter. 25:297; Ishii et al. (2019), Nature Geoscience 12:869."
)

def create_earth_lower_mantle_shell(center_position=(0, 0, 0)):
    """Creates Earth's lower mantle shell.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': EARTH_LOWER_MANTLE_RADII,  # L-249: derived, not typed
        'color': 'rgb(230, 100, 20)',  # Reddish-brown
        'opacity': 0.7,
        'name': 'Lower Mantle',
        'description': earth_lower_mantle_info.replace('\n', '<br>')
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.4,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: USGS Interior of the Earth, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_upper_mantle_info = (
            "The upper mantle includes the asthenosphere, a partially molten layer where\n"
            "most magma originates. This region flows more readily than the lower mantle,\n"
            "allowing tectonic plates to move. It reaches from the base of the crust,\n"
            f"{EARTH_MEAN_RADIUS_KM - EARTH_UPPER_MANTLE_KM:,.1f} km below the surface in the reference model, down to\n"
            f"{EARTH_D660_DEPTH_KM:,.0f} km, with temperatures from 500 degC to 2,200 degC\n"
            "(900 degF to 4,000 degF).\n\n"
            "Source (boundaries): Ishii et al. (2019), Nature Geoscience 12:869; Dziewonski & Anderson (1981), PREM, Phys. Earth Planet. Inter. 25:297."
)

def create_earth_upper_mantle_shell(center_position=(0, 0, 0)):
    """Creates Earth's upper mantle shell.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': EARTH_UPPER_MANTLE_RADII,  # L-249: derived, not typed
        'color': 'rgb(205, 85, 85)',  # Lighter reddish-brown
        'opacity': 0.6,
        'name': 'Upper Mantle',
        'description': earth_upper_mantle_info.replace('\n', '<br>')
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=25)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=3.1,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: USGS Interior of the Earth, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_crust_info = (
            "Earth's crust is the thin, solid outer layer where humans live. It's divided into\n"
            "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)\n"
            "made primarily of granite. The crust contains all known life and the accessible portion\n"
            "of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF)."
)

def create_earth_crust_shell(center_position=(0, 0, 0)):
    """Creates Earth's crust shell using Mesh3d for better performance with improved hover.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.0,  # Crust: 100% of Mars's radius
        'color': 'rgb(70, 120, 160)',  # Bluish for oceans, brown for land
        'opacity': 1.0,
        'name': 'Crust',
        'description': (
            "Earth Crust<br>" 
            "(Note: toggle off the crust layer in the legend to better see the interior structure.)<br><br>"
            "Earth's crust is the thin, solid outer layer where humans live. It's divided into<br>"
            "oceanic crust (5-10 km thick) made mostly of basalt, and continental crust (30-50 km thick)<br>"
            "made primarily of granite. The crust contains all known life and the accessible portion<br>"
            "of Earth's geological resources. Surface temperatures range from -80 degC to 60 degC (-112 degF to 140 degF)."
        )
    }
    
    # Calculate radius in AU
    radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Unpack center position
    center_x, center_y, center_z = center_position
    
    # Create mesh with reasonable resolution for performance
    resolution = 24  # Reduced from typical 50 for markers
    
    # Create a UV sphere
    phi = np.linspace(0, 2*np.pi, resolution)
    theta = np.linspace(-np.pi/2, np.pi/2, resolution)
    phi, theta = np.meshgrid(phi, theta)
    
    x = radius * np.cos(theta) * np.cos(phi)
    y = radius * np.cos(theta) * np.sin(phi)
    z = radius * np.sin(theta)
    
    # Apply center position offset
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create triangulation
    indices = []
    for i in range(resolution-1):
        for j in range(resolution-1):
            p1 = i * resolution + j
            p2 = i * resolution + (j + 1)
            p3 = (i + 1) * resolution + j
            p4 = (i + 1) * resolution + (j + 1)
            
            indices.append([p1, p2, p4])
            indices.append([p1, p4, p3])
    
    # Create main surface
    surface_trace = go.Mesh3d(
        x=x.flatten(), 
        y=y.flatten(), 
        z=z.flatten(),
        i=[idx[0] for idx in indices],
        j=[idx[1] for idx in indices],
        k=[idx[2] for idx in indices],
        color=layer_info['color'],
        opacity=layer_info['opacity'],
        name=f"Earth: {layer_info['name']}",
        legendgroup=f"Earth: {layer_info['name']}",
        showlegend=True,
        hoverinfo='none',  # Disable hover on mesh surface
        # Add these new parameters to make hover text invisible
        hovertemplate=' ',  # Empty template instead of None
        hoverlabel=dict(
    #        bgcolor='rgba(0,0,0,0)',  # Transparent background
            font=dict(
                color='rgba(0,0,0,0)',  # Transparent text
    #            size=0                  # Zero font size
            ),
            bordercolor='rgba(0,0,0,0)'  # Transparent border
        ), 
        # Add these new parameters to eliminate shading
        flatshading=True,  # Use flat shading instead of smooth
        lighting=dict(
            ambient=1.0,     # Set to maximum (1.0)
            diffuse=0.0,     # Turn off diffuse lighting
            specular=0.0,    # Turn off specular highlights
            roughness=1.0,   # Maximum roughness
            fresnel=0.0      # Turn off fresnel effect
        ),
        lightposition=dict(
            x=0,  # Centered light
            y=0,  # Centered light
            z=10000  # Light from very far above to minimize shadows
        )       
    )
        
    # Use the Fibonacci sphere algorithm for more even point distribution
    def fibonacci_sphere(samples=1000):
        points = []
        phi = math.pi * (3. - math.sqrt(5.))  # Golden angle in radians
        
        for i in range(samples):
            y = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
            radius_at_y = math.sqrt(1 - y * y)  # Radius at y
            
            theta = phi * i  # Golden angle increment
            
            x = math.cos(theta) * radius_at_y
            z = math.sin(theta) * radius_at_y
            
            points.append((x, y, z))
        
        return points
    
    # Generate fibonacci sphere points
    fib_points = fibonacci_sphere(samples=50)  # Originally, 50 hover points evenly distributed
    
    # Scale and offset the points
    x_hover = [p[0] * radius + center_x for p in fib_points]
    y_hover = [p[1] * radius + center_y for p in fib_points]
    z_hover = [p[2] * radius + center_z for p in fib_points]
        
    # Create a list of repeated descriptions for each point
    # This is crucial - we need exactly one text entry per point

    # Just the name for "Object Names Only" mode

    # Create hover trace with direct text assignment
    # Single info marker at north pole, 5% above radius
    r_info = radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    hover_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name=trace_name,
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[f"Earth: {layer_info['name']}"],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    return [surface_trace, hover_trace]

# Source: NOAA, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_atmosphere_info = (
            "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and\n"
            "the stratosphere (12-50 km) which contains the ozone layer. These regions contain\n"
            "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from\n"
            "about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).\n"
            "The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption."
)

def create_earth_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's lower atmosphere shell.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.05,  # Troposphere and stratosphere
        'color': 'rgb(150, 200, 255)',  # Light blue for atmosphere
        'opacity': 0.5,
        'name': 'Lower Atmosphere',
        'description': (
            "The lower atmosphere includes the troposphere (0-12 km) where weather occurs, and<br>"
            "the stratosphere (12-50 km) which contains the ozone layer. These regions contain<br>"
            "99% of atmospheric mass, primarily nitrogen and oxygen. Temperature varies from<br>"
            "about 15 degC (59 degF) at sea level to -60 degC (-76 degF) at the tropopause (12 km).<br>"
            "The stratopause (50 km) warms to near 0 degC (32 degF) due to ozone absorption."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2.5,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: NOAA, NASA Earth Fact Sheet
# Verified: April 2026 via Gemini fact-check
earth_upper_atmosphere_info = (
            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes\n"
            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and\n"
            "the International Space Station orbits, and the exosphere which gradually transitions\n"
            "to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the\n"
            "gas is so thin that it would feel cold to human skin."
)

def create_earth_upper_atmosphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's upper atmosphere shell.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Define layer properties
    layer_info = {
        'radius_fraction': 1.25,  # Mesosphere, thermosphere, and exosphere
        'color': 'rgb(100, 150, 255)',  # Lighter blue
        'opacity': 0.3,
        'name': 'Upper Atmosphere',
        'description': (
            "The upper atmosphere extends from 50 km to about 1,000 km altitude. It includes<br>"
            "the mesosphere where meteors burn up, the thermosphere where the aurora occurs and<br>"
            "the International Space Station orbits, and the exosphere which gradually transitions<br>"
            "to space. In the thermosphere, temperatures can reach 2,000 degC (3,600 degF), though the<br>"
            "gas is so thin that it would feel cold to human skin."
        )
    }
    
    # Calculate radius in AU
    layer_radius = layer_info['radius_fraction'] * EARTH_RADIUS_AU
    
    # Create sphere points
    x, y, z = create_sphere_points(layer_radius, n_points=20)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    r_info = layer_radius * 1.05
    trace_name = f"Earth: {layer_info['name']}"

    shell_trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=2.0,
            color=layer_info['color'],
            opacity=layer_info['opacity']
        ),
        name=trace_name,
        legendgroup=trace_name,
        hoverinfo='skip',
        showlegend=True
    )
    info_trace = go.Scatter3d(
        x=[center_x], y=[center_y], z=[center_z + r_info],
        mode='markers',
        marker=dict(size=8, color=layer_info['color'], opacity=1.0,
                    symbol='cross', line=dict(color='red', width=2)),
        name='',
        legendgroup=trace_name,
        text=[f"{trace_name}<br><br>{layer_info['description']}"],
        customdata=[trace_name],
        hovertemplate='%{text}<extra></extra>',
        showlegend=False
    )

    traces = [shell_trace, info_trace]
    
    return traces

# Source: every figure below interpolates a row in constants_new.py, and
# Source+: each row carries its own citation and access route:
# Source+: EARTH_MAGNETOPAUSE_STANDOFF_RADII (Shue et al. 1998),
# Source+: EARTH_BOW_SHOCK_STANDOFF_RADII (Jelinek et al. 2012),
# Source+: EARTH_MAGNETOTAIL_OBSERVED_RADII (Slavin et al. 1983),
# Source+: EARTH_MAGNETOTAIL_FLARE_END_RADII and
# Source+: EARTH_MAGNETOTAIL_DIAMETER_RADII (Slavin et al. 1985), and the
# Source+: four EARTH_VAN_ALLEN_*_EDGE rows (Meredith et al. 2014; Li, Tu
# Source+: et al. 2024). The tail's drawn shape follows the rules declared
# Source+: on EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII and
# Source+: EARTH_MAGNETOTAIL_DRAWN_END_RADII.
# Note: the two altitude pairs here were typed until 2026-09-14 and rested
# Note+: on a magazine article, a news article and a university outreach
# Note+: page. They are arithmetic on the belt rows now, which is why the
# Note+: outer figure changed. L-305 item 7.
earth_magnetosphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.01 AU TO VISUALIZE.\n\n" 

            f"Earth's magnetosphere extends about {_declared('EARTH_MAGNETOPAUSE_STANDOFF_RADII')} Earth radii on the Sun-facing side\n"
            "and stretches into a long magnetotail on the night side. It deflects the solar\n"
            "wind and turns aside many of the energetic charged particles that reach Earth\n"
            "from the Sun and from beyond the solar system.\n\n"

            f"Magnetotail: spacecraft found it stops widening about {_with_uncertainty('EARTH_MAGNETOTAIL_FLARE_END_RADII')[0]} Earth radii\n"
            f"behind Earth, plus or minus {_with_uncertainty('EARTH_MAGNETOTAIL_FLARE_END_RADII')[1]}, and is about {_with_uncertainty('EARTH_MAGNETOTAIL_DIAMETER_RADII')[0]} Earth radii wide beyond\n"
            f"there, plus or minus {_with_uncertainty('EARTH_MAGNETOTAIL_DIAMETER_RADII')[1]}. It is drawn widening in a straight line to that\n"
            "point, which is our choice, and drawn round, which is close to its shape\n"
            "under average conditions.\n"
            f"The drawing stops at {_whole_figures('EARTH_MAGNETOTAIL_OBSERVED_RADII')} Earth radii, which is how far the spacecraft\n"
            "went rather than where the tail ends.\n\n"

            "Bow Shock: the boundary where the supersonic solar wind first slows\n"
            f"against Earth's magnetic field, about {_declared('EARTH_BOW_SHOCK_STANDOFF_RADII')} Earth radii upstream on the\n"
            f"Sun-facing side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa.\n"
            f"Both standoffs above are models evaluated at that pressure rather than\n"
            f"measurements: real crossings scatter about the fitted surfaces by\n"
            f"{EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII:g} and {EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII:g} Earth radii, and both boundaries move as the pressure\n"
            "changes.\n\n"

            "Inner Van Allen Belt: Region of trapped charged particles (mainly protons),\n"
            f"spanning about {EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE:g} Earth radii in the geomagnetic equatorial plane --\n"
            f"roughly {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE, 2):,} to {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE, 1):,} km above the surface at the equator.\n"
            "Outer Van Allen Belt: Region of trapped charged particles (mainly electrons),\n"
            f"spanning about {EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE:g} Earth radii and moving with geomagnetic\n"
            f"activity -- roughly {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE, 1):,} to {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE, 1):,} km above the surface at the\n"
            "equator. Every kilometre figure here is converted from Earth radii."
)

def _shue_flaring():
    """Shue et al. (1998) eq. 11, the flaring exponent at the declared
    solar wind: alpha = (a6 + a7 Bz)(1 + a8 ln Dp).

    Evaluated here from the coefficient rows, not stored: nothing prints
    it, and the gallery evaluates the same expression from the same served
    rows. At the declared conditions it is 0.5896, the figure the cut
    angle's row quotes.
    """
    return ((EARTH_MAGNETOPAUSE_SHUE_A6
             + EARTH_MAGNETOPAUSE_SHUE_A7_PER_NT * EARTH_SOLAR_WIND_BZ_NT)
            * (1.0 + EARTH_MAGNETOPAUSE_SHUE_A8
               * math.log(EARTH_SOLAR_WIND_PRESSURE_NPA)))


def _shue_radius(theta_rad, alpha):
    """Shue et al. (1998) eq. 10, in Earth radii, at angle theta from the
    nose: r = r0 * (2 / (1 + cos theta)) ** alpha."""
    return (EARTH_MAGNETOPAUSE_STANDOFF_RADII
            * (2.0 / (1.0 + math.cos(theta_rad))) ** alpha)


def _earth_magnetosphere_points():
    """Earth's magnetopause and magnetotail as points, in Earth radii, in
    the default frame: -X toward the Sun, +X down the tail, Z up.

    Returns (x, y, z, marker), where marker is the info marker's
    (x, y, z) in the same frame.

    L-322 Stage D, patch D8. Two pieces, one surface of revolution about
    the Sun line.

    THE MAGNETOPAUSE is Shue's own surface, from the nose to
    EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG, where the paper stops plotting its
    model. It was an ellipsoid with widths of 12 and 10 Earth radii chosen
    by eye, which the hover itself called "an approximation of the
    shape, not the model's own".

    THE TAIL starts where the surface stops. Its starting radius and its
    starting distance are computed here from Shue's surface at the cut,
    about 20.1 and 11.6 Earth radii at the declared solar wind; they are
    not typed and not stored. From there its radius grows in a straight
    line to EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII at
    EARTH_MAGNETOTAIL_FLARE_END_RADII behind Earth, then stays at that
    radius to EARTH_MAGNETOTAIL_DRAWN_END_RADII. It is round. Those three
    rules are declared on their rows in constants_new.py with their
    reasons. The tail was 100 Earth radii long, 15 wide at its base and
    25 at its end, all chosen by eye.
    """
    # Rendering settings. They change how the drawing looks, not where
    # anything is, so they stay here in the drawing code
    # (provenance-discipline 2.18, Three Kinds of Drawing Number), and
    # inside the function, as the belts' n_points and n_rings are: at
    # module level the provenance scanner cannot tell them from claims.
    n_theta = 12          # rows of points from the nose to the cut
    n_phi = 24            # points round each row and each tail ring
    n_tail_rings = 20     # rings from the cut to the end of the drawing
    # The info marker sits on the surface 60 degrees from the nose, rolled
    # a quarter turn, so it is off the Sun line where the Sun direction
    # arrow runs. The gallery's Earth room puts its magnetopause marker
    # there too.
    marker_theta_deg = 60.0
    marker_roll_deg = 90.0

    alpha = _shue_flaring()
    cut = math.radians(EARTH_MAGNETOPAUSE_CUT_ANGLE_DEG)
    x, y, z = [], [], []

    def ring(x_value, radius):
        for j in range(n_phi):
            phi = 2.0 * math.pi * j / n_phi
            x.append(x_value)
            y.append(radius * math.cos(phi))
            z.append(radius * math.sin(phi))

    # The nose, then rings out to the cut.
    x.append(-EARTH_MAGNETOPAUSE_STANDOFF_RADII)
    y.append(0.0)
    z.append(0.0)
    for i in range(1, n_theta + 1):
        theta = cut * i / n_theta
        r = _shue_radius(theta, alpha)
        ring(-r * math.cos(theta), r * math.sin(theta))

    # The tail, from the cut (its first ring is the surface's last, so it
    # is not drawn twice).
    r_cut = _shue_radius(cut, alpha)
    tail_start_x = -r_cut * math.cos(cut)
    tail_start_radius = r_cut * math.sin(cut)
    flare_end = EARTH_MAGNETOTAIL_FLARE_END_RADII
    tail_radius = EARTH_MAGNETOTAIL_DRAWN_RADIUS_RADII
    tail_end = EARTH_MAGNETOTAIL_DRAWN_END_RADII
    if not tail_start_x < flare_end < tail_end:
        raise ValueError(
            "Earth's magnetotail rows are out of order: the surface stops "
            "%.1f Earth radii behind Earth, the widening ends at %g and the "
            "drawing at %g" % (tail_start_x, flare_end, tail_end))
    for k in range(1, n_tail_rings + 1):
        tail_x = tail_start_x + (tail_end - tail_start_x) * k / n_tail_rings
        if tail_x < flare_end:
            radius = (tail_start_radius + (tail_radius - tail_start_radius)
                      * (tail_x - tail_start_x) / (flare_end - tail_start_x))
        else:
            radius = tail_radius
        ring(tail_x, radius)

    theta = math.radians(marker_theta_deg)
    roll = math.radians(marker_roll_deg)
    r = _shue_radius(theta, alpha)
    rho = r * math.sin(theta)
    marker = (-r * math.cos(theta), rho * math.cos(roll), rho * math.sin(roll))
    return x, y, z, marker


def create_earth_magnetosphere_shell(center_position=(0, 0, 0), sun_position=(0, 0, 0)):

    """Creates Earth's magnetosphere: the magnetopause and its tail, the
    bow shock, and the two radiation belts, as four traces each with its
    info marker.

    L-322 Stage D, patch D8 (2026-09-25): the magnetopause is Shue's own
    surface and the tail is built from Slavin et al. (1985), both from
    constants_new.py; see _earth_magnetosphere_points(). The belts are
    drawn across their served edges.
    """
    traces = []

    # Unpack center position
    center_x, center_y, center_z = center_position

    # 1. The magnetopause and its tail, generated in Earth radii with -X
    # sunward, then scaled to AU.
    x, y, z, marker = _earth_magnetosphere_points()
    x = np.array(x) * EARTH_RADIUS_AU
    y = np.array(y) * EARTH_RADIUS_AU
    z = np.array(z) * EARTH_RADIUS_AU
    marker_x = np.array([marker[0]]) * EARTH_RADIUS_AU
    marker_y = np.array([marker[1]]) * EARTH_RADIUS_AU
    marker_z = np.array([marker[2]]) * EARTH_RADIUS_AU
    # Rotate to the actual sunward direction, then offset to the centre.
    # Phase D2: sun_position. No magnetic tilt is applied here; see the
    # L-305 note below. (This comment said the dipole was tilted ~11 deg
    # until L-322 C2; that figure was uncited and the code dropped it.)
    x, y, z = rotate_to_sunward(
        x, y, z, center_position=center_position,
        # L-305 (2026-09-15): magnetic_tilt_deg=11 removed. It was uncited,
        # it disagreed with the sourced tilt in PLANET_DIPOLE, and the bow
        # shock call below passes no tilt at all -- so this leaned the
        # magnetopause inside an upright bow shock. Both boundary models
        # are fitted symmetric about the Sun line from crossings taken at
        # every dipole tilt, so the tilt is already averaged into their
        # coefficients. The dipole cone is where Earth's tilt is shown.
        sun_position=sun_position,
    )
    marker_x, marker_y, marker_z = rotate_to_sunward(
        marker_x, marker_y, marker_z, center_position=center_position,
        sun_position=sun_position,
    )
    x = x + center_x
    y = y + center_y
    z = z + center_z

    flare_value, flare_unc = _with_uncertainty('EARTH_MAGNETOTAIL_FLARE_END_RADII')
    width_value, width_unc = _with_uncertainty('EARTH_MAGNETOTAIL_DIAMETER_RADII')
    observed = _whole_figures('EARTH_MAGNETOTAIL_OBSERVED_RADII')

    magnetosphere_text = ["Earth: Magnetosphere<br><br>"
                 f"Earth's magnetosphere reaches about {_declared('EARTH_MAGNETOPAUSE_STANDOFF_RADII')} Earth radii on the Sun-facing<br>"
                 f"side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa. It stretches into a<br>"
                 "long magnetotail on the night side, deflects the solar wind, and turns<br>"
                 "aside many of the energetic charged particles that reach Earth.<br><br>"
                 "That distance is a model evaluated at those conditions, not something<br>"
                 f"anyone measured. Real crossings of the magnetopause scatter about the<br>"
                 f"fitted surface by {EARTH_MAGNETOPAUSE_SHUE_SCATTER_RADII:g} Earth radii, and the boundary itself moves in<br>"
                 "and out as the solar wind pressure changes.<br><br>"
                 "The Sun-facing surface is the model's own shape, drawn only as far round<br>"
                 "as the paper plots it. A second fit, Jelinek et al. (2012), puts the nose<br>"
                 "about an Earth radius farther out, which is inside the scatter above.<br><br>"
                 f"Spacecraft found that the tail stops widening about {flare_value} Earth radii<br>"
                 f"behind Earth, plus or minus {flare_unc}, and that beyond there it is about {width_value}<br>"
                 f"Earth radii wide, plus or minus {width_unc}. The tail is drawn widening in a<br>"
                 f"straight line from where the surface stops out to {flare_value} Earth radii, then<br>"
                 "at a constant width. The straight line is our choice; the measurements<br>"
                 "give only its two ends.<br><br>"
                 f"The drawing stops at {observed} Earth radii, which is how far the spacecraft<br>"
                 "went, not where the tail ends.<br><br>"
                 "The tail is drawn round. The real tail is often flattened, in a direction<br>"
                 "set by the solar wind's own magnetic field, which keeps changing. Under<br>"
                 "average conditions, measurements far down the tail find it about as tall<br>"
                 "as it is wide.<br><br>"
                 "Source (standoff): Shue et al. (1998), J. Geophys. Res. 103:17691.<br>"
                 "Source (second fit): Jelinek et al. (2012), J. Geophys. Res. 117:A05208.<br>"
                 "Source (tail width, end of widening): Slavin et al. (1985),<br>"
                 "J. Geophys. Res. 90:10875 -- ISEE-3.<br>"
                 "Source (how far observed): Slavin et al. (1983), Geophys. Res. Lett. 10:973.<br>"
                 "Source (tail shape): Sibeck and Lin (2014), doi:10.1002/2013JA019471;<br>"
                 "Maezawa et al. (1997), Adv. Space Res. 20:949 -- GEOTAIL."]

    magnetosphere_customdata = ['Earth: Magnetosphere']

    traces.append(
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(180, 180, 255)', # Light blue for magnetic field
                opacity=0.2
            ),
            name='Earth: Magnetosphere',
            legendgroup='Earth: Magnetosphere',
            hoverinfo='skip',
            showlegend=True
        )
    )
    # Info marker on the surface, off the Sun line (see
    # _earth_magnetosphere_points). It was the first point of the old shape,
    # the nose, which sits on the Sun direction arrow.
    traces.append(create_info_marker(
        marker_x[0] + center_x, marker_y[0] + center_y, marker_z[0] + center_z,
        'rgb(180, 180, 255)', magnetosphere_text[0], 'Earth: Magnetosphere'
    ))


    # 2. Create and add bow shock
    # L-291: was a typed 15 R_E (textbook) with a comment conceding the
    # measured 11-14. L-305: the midpoint is retired; the store now holds
    # Jelinek et al. (2012) eq. 14 at the declared pressure. See
    # EARTH_BOW_SHOCK_STANDOFF_RADII in constants_new.py for the source.
    bow_shock_standoff = EARTH_BOW_SHOCK_STANDOFF_RADII * EARTH_RADIUS_AU
    bow_shock_width = 25 * EARTH_RADIUS_AU  # legacy flank scale; ignored on conic path
    # Conic-section bow shock via shared builder (planet_visualization_utilities).
    # Module updated: June 2026 with Anthropic's Claude Opus 4.8.
    bow_shock_x, bow_shock_y, bow_shock_z = create_bow_shock_shape(
        bow_shock_standoff, width=bow_shock_width, eccentricity=1.05
    )
    
    # Apply rotation to sunward direction, then offset to center position
    bow_shock_x = np.array(bow_shock_x)
    bow_shock_y = np.array(bow_shock_y)
    bow_shock_z = np.array(bow_shock_z)
    bow_shock_x, bow_shock_y, bow_shock_z = rotate_to_sunward(
        bow_shock_x, bow_shock_y, bow_shock_z,
        center_position=center_position, sun_position=sun_position,
    )
    bow_shock_x = bow_shock_x + center_x
    bow_shock_y = bow_shock_y + center_y
    bow_shock_z = bow_shock_z + center_z
    
    bow_shock_text = ["Earth: Bow Shock<br><br>"
                "Bow Shock: the boundary where the supersonic solar wind first slows<br>"
                f"against Earth's magnetic field, about {_declared('EARTH_BOW_SHOCK_STANDOFF_RADII')} Earth radii upstream on the<br>"
                f"Sun-facing side at a nominal solar wind pressure of {EARTH_SOLAR_WIND_PRESSURE_NPA:g} nPa.<br><br>"
                "That distance is a model evaluated at that pressure, not something anyone<br>"
                f"measured. Real crossings of the bow shock scatter about the fitted<br>"
                f"surface by {EARTH_BOW_SHOCK_JELINEK_SCATTER_RADII:g} Earth radii, and the shock itself moves in and out as<br>"
                "the pressure changes.<br><br>"
                "The bow shock points towards the Sun along the X-axis. The XY plane is<br>"
                "the ecliptic.<br><br>"
                "Source (standoff): Jelinek et al. (2012), J. Geophys. Res. 117:A05208, doi:10.1029/2011JA017252."]
    
    bow_shock_customdata = ['Earth: Bow Shock']

    traces.append(
        go.Scatter3d(
            x=bow_shock_x,
            y=bow_shock_y,
            z=bow_shock_z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(255, 200, 150)',  # Orange-ish color for bow shock
                opacity=0.2
            ),
            name='Earth: Bow Shock',
            legendgroup='Earth: Bow Shock',
            hoverinfo='skip',
            showlegend=True
        )
    )
    # Info marker at first point on bow shock structure
    traces.append(create_info_marker(
        bow_shock_x[0], bow_shock_y[0], bow_shock_z[0],
        'rgb(255, 200, 150)', bow_shock_text[0], 'Earth: Bow Shock'
    ))
    
    # 3. Create and add Van Allen radiation belts
    belt_colors = ['rgb(255, 100, 100)', 'rgb(100, 200, 255)']
    belt_names = ['Earth: Inner Radiation Belt', 'Earth: Outer Radiation Belt']
    # Source: every figure below interpolates a row in constants_new.py --
    # Source+: EARTH_VAN_ALLEN_INNER_RADII, EARTH_VAN_ALLEN_OUTER_RADII and
    # Source+: the four EARTH_VAN_ALLEN_*_EDGE rows, each carrying its own
    # Source+: citation and access route. The spans were typed here until
    # Source+: 2026-09-14, when L-305 item 7 gave them rows to read.
    # Source+: The kilometres are arithmetic on those rows, not a second
    # Source+: figure: see _km_above_surface() at the top of this module.
    # L-322 Stage C2: the band's two ends, from their store rows at their
    # declared counts, for the outer belt's source line below.
    _band_low = _declared('EARTH_VAN_ALLEN_OUTER_BAND_LOW_L')
    _band_high = _declared('EARTH_VAN_ALLEN_OUTER_BAND_HIGH_L')
    belt_texts = [
        f"Inner Van Allen Belt: Region of trapped charged particles (mainly protons).<br>"
        "The belt is one continuous region. The rings only mark its extent: they<br>"
        "are evenly spaced from its inner edge to its outer edge, and the brighter<br>"
        f"ring is the flux peak, {EARTH_VAN_ALLEN_INNER_RADII:g} Earth radii from Earth's centre, about<br>"
        f"{_km_above_surface(EARTH_VAN_ALLEN_INNER_RADII, 2):,} km above the surface at the equator.<br>"
        f"The belt spans about {EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE:g} Earth radii in the geomagnetic<br>"
        f"equatorial plane -- roughly {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE, 2):,} to {_km_above_surface(EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE, 1):,} km above the surface<br>"
        f"(every kilometre figure here converted from Earth radii).<br>"
        "Source (peak): Baker et al. (2018), Space Sci. Rev. 214:17, doi:10.1007/s11214-017-0452-7.<br>"
        "Source (extent): Meredith et al. (2014), J. Geophys. Res. Space Physics 119:5328.",
        f"Outer Van Allen Belt: Region of trapped charged particles (mainly electrons).<br>"
        "The belt is one continuous region. The rings only mark its extent: they<br>"
        "are evenly spaced from its inner edge to its outer edge, and the brighter<br>"
        f"ring is the flux peak, L = {EARTH_VAN_ALLEN_OUTER_RADII:g} -- about {_km_above_surface(EARTH_VAN_ALLEN_OUTER_RADII, 2):,} km above the<br>"
        "surface at the equator, where L equals geocentric distance in Earth radii.<br>"
        f"The belt spans about {EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE:g} to {EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE:g} Earth radii and moves with geomagnetic<br>"
        f"activity -- roughly {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE, 1):,} to {_km_above_surface(EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE, 1):,} km above the surface<br>"
        f"(every kilometre figure here converted from Earth radii).<br>"
        "Source (peak): Li et al. (2025), doi:10.1029/2024JA033504 -- most intense across<br>"
        f"the L = {_band_low} to {_band_high} band; the drawn {EARTH_VAN_ALLEN_OUTER_RADII:g} is our midpoint of it.<br>"
        "Source (extent): Meredith et al. (2014); Li, Tu et al. (2024), doi:10.1029/2023JA032171."
    ]
    
    # L-322 Stage D, patch D8 (2026-09-25): each belt is drawn across its
    # edge rows. It was a spread of 0.5 Earth radii around the peak
    # (belt_thickness), chosen by eye, and it is removed rather than
    # promoted (A Drawing Approximation Does Not Promote). Since patch D9
    # the rings are evenly spaced from the inner edge row to the outer edge
    # row on a step that also lands on the peak row, and the peak ring is
    # drawn brighter and larger (_even_belt_rings). The point count, the
    # brightnesses and the sizes are rendering settings; the ring count
    # follows from the rows.
    belt_bands = [
        (EARTH_VAN_ALLEN_INNER_RADII,
         EARTH_VAN_ALLEN_INNER_BELT_INNER_EDGE,
         EARTH_VAN_ALLEN_INNER_BELT_OUTER_EDGE),
        (EARTH_VAN_ALLEN_OUTER_RADII,
         EARTH_VAN_ALLEN_OUTER_BELT_INNER_EDGE,
         EARTH_VAN_ALLEN_OUTER_BELT_OUTER_EDGE),
    ]
    # L-322 Stage D, patch D9: the rings are evenly spaced on a step that
    # lands on the edges and the peak (_even_belt_rings), and the peak ring
    # is fully opaque with larger points. At D8 it was 0.6 against 0.2 at
    # the same size, which Tony could barely see. Rendering settings.
    belt_edge_alpha = 0.2   # the rings across the belt (the old opacity)
    belt_peak_alpha = 1.0   # the ring at the peak
    belt_edge_size = 1.5    # the old point size
    belt_peak_size = 3.0

    for i, (belt_peak, belt_inner, belt_outer) in enumerate(belt_bands):
        belt_x = []
        belt_y = []
        belt_z = []
        belt_point_colors = []
        belt_point_sizes = []
        belt_rgb = belt_colors[i].replace('rgb(', '').replace(')', '')
        
        # 48 points a ring (80 at D8, with 6 rings): with 11 and 9 rings
        # the two belts stay near D8's size per animation frame.
        n_points = 48
        
        ring_radii, peak_ring = _even_belt_rings(belt_inner, belt_peak,
                                                 belt_outer)
        for i_ring, ring_radius in enumerate(ring_radii):
            belt_radius = ring_radius * EARTH_RADIUS_AU
            is_peak = i_ring == peak_ring
            ring_color = 'rgba(%s, %g)' % (
                belt_rgb, belt_peak_alpha if is_peak else belt_edge_alpha)
            ring_size = belt_peak_size if is_peak else belt_edge_size
            
            for j in range(n_points):
                angle = (j / n_points) * 2 * np.pi
                
                # A flat ring in the body frame. It becomes a ring around
                # Earth's rotational axis a few lines below, where
                # orient_to_planet_pole rotates it -- which is what the
                # old comment here claimed and the code never did.
                x = belt_radius * np.cos(angle)
                y = belt_radius * np.sin(angle)
                
                # L-231 (Tony's ruling, 2026-09-15): the saddle is gone.
                # This was z = 0.2 * belt_radius * sin(2 * angle), lifting
                # the ring a fifth of its radius TWICE per circuit -- more
                # vertical swing than Earth's real magnetic tilt
                # would give, at twice the frequency, meaning nothing. The
                # comment here said it made the belt "thinner near poles";
                # it changed no cross-section, it moved the whole ring.
                # Any real vertical extent is L-330's question.
                z = 0.0
                
                belt_x.append(x)
                belt_y.append(y)
                belt_z.append(z)
                belt_point_colors.append(ring_color)
                belt_point_sizes.append(ring_size)
        
        # L-231 (Tony's ruling, 2026-09-15): into Earth's EQUATORIAL
        # plane, before the centre offset. The deciding argument is the
        # geostationary ring, which is drawn in that plane at 6.6 R_E,
        # inside an outer belt whose sources span 3 to 7 -- the ecliptic
        # put those two 23.4 degrees apart in one picture. The magnetic
        # equator would be better still, but it needs a DIRECTION as well
        # as an angle and that direction turns once a day; the spin
        # equator is its daily average. Same call Saturn's belts use.
        belt_x, belt_y, belt_z = orient_to_planet_pole(
            np.array(belt_x), np.array(belt_y), np.array(belt_z), 'Earth')

        # Apply center position offset
        belt_x = np.array(belt_x) + center_x
        belt_y = np.array(belt_y) + center_y
        belt_z = np.array(belt_z) + center_z
        
        belt_text = [f"{belt_names[i]}<br><br>{belt_texts[i]}"]
        belt_customdata = [belt_names[i]]

        traces.append(
            go.Scatter3d(
                x=belt_x,
                y=belt_y,
                z=belt_z,
                mode='markers',
                marker=dict(
                    # One colour and one size per point, so the peak ring
                    # stands out from the rest (L-322 Stage D, D8 and D9).
                    size=belt_point_sizes,
                    color=belt_point_colors,
                ),
                name=belt_names[i],
                legendgroup=belt_names[i],
                hoverinfo='skip',
                showlegend=True
            )
        )
        # Info marker for this belt. Per-belt border per two-standards
        # (May 28, 2026): white on inner reddish belt (i=0,
        # rgb(255,100,100)), red on outer blue belt (i=1,
        # rgb(100,200,255)). Inner belt is the borderline-reddish case
        # the two-standards convention exists for.
        # L-322 Stage D, patch D9: the marker sits on the peak ring's first
        # point; the rings are in order of radius now, not peak first.
        marker_index = peak_ring * n_points
        traces.append(create_info_marker(
            belt_x[marker_index], belt_y[marker_index], belt_z[marker_index],
            belt_colors[i], belt_text[0], belt_names[i],
            border_color='white' if i == 0 else 'red'
        ))
    
    return traces

# Source: UCS Satellite Database, ESA Space Debris Office, NASA
# Source+: Satellite/debris counts as of early 2026
# Verified: April 2026 via Gemini fact-check
earth_leo_shell_info = (
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
)

def create_earth_leo_shell(center_position=(0, 0, 0)):
    """
    Creates a representation of Earth's Low Earth Orbit (LEO) shell.

    LEO spans ~200 km to ~2,000 km altitude (1.03 to 1.31 Earth radii).
    Unlike GEO, LEO objects orbit at all inclinations -- forming a true
    spherical shell. Points are distributed across the full sphere with
    slight density enhancement at the Starlink altitude (~550 km).

    The contrast with the GEO ring is the whole point: LEO is what you
    see in the sky; GEO is invisible but controls global communications.
    """
    import numpy as np
    import plotly.graph_objs as go
    from planet_visualization_utilities import EARTH_RADIUS_AU

    center_x, center_y, center_z = center_position

    # L-178: converted directly via KM_PER_AU. The former local
    # EARTH_RADIUS_KM = 6371.0 (volumetric mean) was a shadow constant, and
    # dividing it into the equatorial-based EARTH_RADIUS_AU (6,378.137 km)
    # introduced a +0.112% error in every altitude band below.
    AU_PER_KM = 1.0 / KM_PER_AU

    # LEO altitude bands in km
    # L-291: were typed 6571 / 8371, which is the 6371 km MEAN radius plus
    # the altitude -- a shadow of the wrong radius. The store derives
    # both from the equatorial radius this shell is drawn against.
    LEO_LOW_KM  = EARTH_LEO_INNER_KM    # 200 km altitude
    LEO_HIGH_KM = EARTH_LEO_OUTER_KM    # 2000 km altitude
    STARLINK_KM = 6921.0   # ~550 km altitude -- densest population

    np.random.seed(7)      # Deterministic scatter

    # Main LEO shell: 300 points uniformly distributed across sphere
    n_main = 300
    # Uniform sphere distribution using spherical coordinates
    phi_main = np.random.uniform(0, 2 * np.pi, n_main)
    cos_theta_main = np.random.uniform(-1, 1, n_main)   # cos(theta) uniform -> uniform on sphere
    theta_main = np.arccos(cos_theta_main)

    # Radii drawn from LEO band, weighted toward Starlink altitude
    # Mix: 60% uniform across full band, 40% clustered near Starlink
    n_uniform = int(n_main * 0.6)
    n_starlink = n_main - n_uniform
    r_uniform = np.random.uniform(LEO_LOW_KM, LEO_HIGH_KM, n_uniform)
    r_starlink = np.random.normal(STARLINK_KM, 150, n_starlink)  # 150 km std dev around Starlink
    r_starlink = np.clip(r_starlink, LEO_LOW_KM, LEO_HIGH_KM)
    radii_km = np.concatenate([r_uniform, r_starlink])
    np.random.shuffle(radii_km)
    radii_au = radii_km * AU_PER_KM

    x = radii_au * np.sin(theta_main) * np.cos(phi_main) + center_x
    y = radii_au * np.sin(theta_main) * np.sin(phi_main) + center_y
    z = radii_au * np.cos(theta_main) + center_z

    # Source: UCS Satellite Database, ESA Space Debris Office (counts as of early 2026)
    # Source+: SpaceX Starlink status; NASA (ISS, Hubble altitudes)
    # Verified: April 2026 via Gemini fact-check
    hover_text = (
        "Earth: Low Earth Orbit (LEO)<br><br>"
        "Low Earth Orbit (LEO)<br>"
        f"Altitude range: {EARTH_LEO_LOWER_ALTITUDE_KM:,.0f} km to {EARTH_LEO_UPPER_ALTITUDE_KM:,.0f} km above surface<br>"
        f"Radius: {EARTH_LEO_INNER_KM:,.0f} km to {EARTH_LEO_OUTER_KM:,.0f} km from Earth's center "
        f"({EARTH_LEO_INNER_RADII:.2f} to {EARTH_LEO_OUTER_RADII:.2f} Earth radii)<br><br>"
        "LEO satellites orbit at all inclinations -- forming a true shell, not a ring.<br>"
        "One orbit takes 90-120 minutes; a satellite crosses the sky in ~6 minutes.<br><br>"
        "The bright moving points visible at dusk and dawn are LEO objects.<br>"
        "Starlink (~550 km), ISS (~400 km), and Hubble (~540 km) all live here.<br><br>"
        "<b>Active satellites:</b> ~11,000 (Starlink alone: ~7,000)<br>"
        "<b>Tracked debris objects (>10 cm):</b> 35,000+<br><br>"
        f"Compare with the Geostationary Belt (GEO) at {EARTH_GEOSTATIONARY_RADIUS_KM:,.0f} km -- 5x farther out,<br>"
        "invisible to the naked eye, but controlling global communications.<br><br>"
        "Source (upper edge): IADC Space Debris Mitigation Guidelines, IADC-02-01 Rev. 3 (2021), "
        "sec. 3.3.2. The 200 km floor is a drawing choice, not a measured boundary."
    )

    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.5,
                color='rgb(255, 248, 220)',   # Warm white -- visible satellites
                opacity=0.35,
                symbol='circle',
            ),
            name='Earth: Low Earth Orbit (LEO)',
            legendgroup='Earth: Low Earth Orbit (LEO)',
            hoverinfo='skip',
            showlegend=True,
        )
    ]
    # Info marker at LEO outer extent on the north pole
    r_info = np.max(z) - center_z  # LEO outer extent above center
    traces.append(create_info_marker(
        center_x, center_y, center_z + r_info,
        'rgb(255, 248, 220)', hover_text, 'Earth: Low Earth Orbit (LEO)'
    ))

    return traces

earth_geostationary_belt_info = (
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
)

def create_earth_geostationary_belt_shell(center_position=(0, 0, 0)):
    """
    Creates a representation of Earth's geostationary satellite belt at 42,164 km.

    The belt is rendered as a sparse ring of discrete points -- evoking the real
    population of ~550 active satellites -- rather than a continuous torus.
    Subtle scatter in radius and inclination suggests the slight orbital variations
    of real satellites (station-keeping keeps them within +/-0.1 deg of the equator
    and within a few hundred km in radius).

    Physics:
        GEO radius:  42,164 km = 6.62 Earth radii
        GEO altitude: 35,786 km above the surface
        Apophis 2029: 38,013 km -- 4,151 km INSIDE this belt
    """
    import numpy as np
    import plotly.graph_objs as go
    from planet_visualization_utilities import EARTH_RADIUS_AU

    center_x, center_y, center_z = center_position

    # Geostationary orbit radius in AU
    GEO_RADIUS_KM = EARTH_GEOSTATIONARY_RADIUS_KM   # L-291: derived in the store from GM and rotation rate
    # L-178: converted directly via KM_PER_AU. The former local
    # EARTH_RADIUS_KM = 6371.0 (volumetric mean) was a shadow constant, and
    # dividing into the equatorial-based EARTH_RADIUS_AU drew the belt
    # ~47 km too high (+0.112%).
    geo_radius_au = GEO_RADIUS_KM / KM_PER_AU

    # Satellite scatter parameters
    # Real GEO satellites are station-kept within ~0.1 deg latitude and
    # a few hundred km in radius. We exaggerate slightly for visual clarity.
    n_satellites = 240          # ~240 points suggest a populated but sparse belt
    np.random.seed(42)          # Deterministic scatter for reproducibility

    # Azimuthal positions -- slightly irregular spacing (not perfectly even)
    # to avoid looking like a simple ring
    base_angles = np.linspace(0, 2 * np.pi, n_satellites, endpoint=False)
    angle_jitter = np.random.uniform(-0.008, 0.008, n_satellites)  # Small jitter
    angles = base_angles + angle_jitter

    # Radial scatter: +/- 0.0002 EARTH RADII (~1.3 km), not AU. Real GEO
    # station-keeping bands run to tens of km; widening this is a Mode 5
    # call, so the value is unchanged and only the comment is corrected.
    radial_scatter = np.random.uniform(-0.0002, 0.0002, n_satellites) * EARTH_RADIUS_AU
    radii = geo_radius_au + radial_scatter

    # z scatter: slight inclination variation (real GEO sats drift +/-0.1 deg in lat)
    # We exaggerate to +/-0.05 Earth radii for visibility
    z_scatter = np.random.uniform(-0.05, 0.05, n_satellites) * EARTH_RADIUS_AU

    x = radii * np.cos(angles) + center_x
    y = radii * np.sin(angles) + center_y
    z = z_scatter + center_z

    # Source: ITU, UCS Satellite Database, JPL CAD API (Apophis)
    # Verified: April 2026 via Gemini fact-check
    hover_text = (
        "Earth: Geostationary Belt (GEO)<br><br>"
        "Geostationary Belt (GEO)<br>"
        f"Altitude: {EARTH_GEOSTATIONARY_RADIUS_KM - EARTH_EQUATORIAL_RADIUS_KM:,.0f} km / "
        f"{(EARTH_GEOSTATIONARY_RADIUS_KM - EARTH_EQUATORIAL_RADIUS_KM) / KM_PER_AU:.6f} AU above surface<br>"
        f"Radius: {EARTH_GEOSTATIONARY_RADIUS_KM:,.0f} km / {EARTH_GEOSTATIONARY_RADIUS_KM / KM_PER_AU:.6f} AU "
        f"from Earth's center ({EARTH_GEOSTATIONARY_RADII:.2f} Earth radii)<br><br>"
        "Each point represents a region of this belt populated by active satellites.<br>"
        "Approximately 550 active geostationary satellites carry TV broadcasts,<br>"
        "weather imagery, communications, and GPS augmentation for half the world.<br><br>"
        "<b>Apophis 2029:</b> On April 13, 2029, Apophis passes at 38,013 km --<br>"
        "roughly 4,150 km INSIDE this belt. It will transit the sky as seen<br>"
        "from geostationary platforms and be visible to the naked eye from Earth.<br><br>"
        "Source: ITU, UCS Satellite Database, JPL CAD API"
    )

    traces = [
        go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=2.0,
                color='rgb(220, 220, 255)',   # Cool silver-white -- human infrastructure
                opacity=0.55,
                symbol='circle',
            ),
            name='Earth: Geostationary Belt (GEO)',
            legendgroup='Earth: Geostationary Belt (GEO)',
            hoverinfo='skip',
            showlegend=True,
        )
    ]
    # Info marker on GEO ring at phi=0
    traces.append(create_info_marker(
        center_x + geo_radius_au, center_y, center_z,
        'rgb(220, 220, 255)', hover_text, 'Earth: Geostationary Belt (GEO)'
    ))

    return traces

# Source: NASA Solar System Dynamics
# Verified: April 2026 via Gemini fact-check
earth_hill_sphere_info = (
            "SET MANUAL SCALE TO AT LEAST 0.02 AU TO VISUALIZE.\n\n" 
            f"Earth's Hill Sphere (extends to about {EARTH_HILL_SPHERE_RADII:.0f} Earth radii or about {EARTH_HILL_SPHERE_KM / 1e6:.1f} million km)."
)

def create_earth_hill_sphere_shell(center_position=(0, 0, 0)):
    """Creates Earth's Hill sphere.

    DEAD CODE (L-254, 2026-08-26). Not on the render path: imported at
    planet_visualization.py and called nowhere. This body renders its
    sphere shells through SHELL_CONFIGS -> build_sphere_shell(). Edit
    that config, not this function -- a change here renders nothing.
    Retained pending the codebase-wide sweep in L-254.
    """
    # Hill sphere radius in Earth radii
    radius_fraction = EARTH_HILL_SPHERE_RADII  # L-291: derived in the store from the two GMs
    
    # Calculate radius in AU
    radius_au = radius_fraction * EARTH_RADIUS_AU
    
    # Create sphere points with fewer points for memory efficiency
    n_points = 30  # Reduced for large spheres
    x, y, z = create_sphere_points(radius_au, n_points=n_points)
    
    # Apply center position offset
    center_x, center_y, center_z = center_position
    x = x + center_x
    y = y + center_y
    z = z + center_z
    
    # Create hover text
    hover_text = (f"Earth's Hill Sphere (extends to about {EARTH_HILL_SPHERE_RADII:.0f} Earth radii or about {EARTH_HILL_SPHERE_KM / 1e6:.1f} million km)<br><br>"
                "The Hill sphere is the region around a body where its own gravity is the dominant force in attracting satellites. For <br>" 
                "a planet orbiting a star, it's the region where the planet's gravity is stronger than the star's tidal forces.<br><br>" 
                "The Hill Sphere radius can be described in words as follows: it is equal to the planet's average distance from the <br>" 
                "Sun (its orbital semi-major axis) multiplied by the cube root of the ratio between the planet's mass and three times <br>" 
                "the Sun's mass. In other words, you take how far the planet orbits out from the Sun, then scale that distance by the <br>" 
                "cube root of (planet mass / [3 x solar mass]) to find the boundary within which the planet's gravity dominates over the Sun's."                  
                )
    
    # Create the trace
    traces = [
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=1.0,
                color='rgb(0, 255, 0)',  # Green for Hill sphere
                opacity=0.25
            ),
            name='Earth: Hill Sphere',
            legendgroup='Earth: Hill Sphere',
            hoverinfo='skip',
            showlegend=True
        )
    ]
    r_info = radius_au * 1.05
    # Phase 1 re-pipe (May 28, 2026): factory-routed for centralized styling.
    traces.append(create_info_marker(
        center_x, center_y, center_z + r_info,
        'rgb(0, 255, 0)',
        f"Earth: Hill Sphere<br><br>{hover_text}",
        'Earth: Hill Sphere'
    ))
    
    return traces

