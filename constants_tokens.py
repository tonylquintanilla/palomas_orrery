"""
constants_tokens.py -- what each "# Unit:" token in constants_new.py means.

WHAT THIS IS

    constants_new.py declares a unit beside every value with a comment
    line, "# Unit: r_earth". The token on that line is a short name. This
    file is the one place that says what the name MEANS: which physical
    dimension it has, and, for a unit defined by a value in the store,
    which store row defines it.

    It is read by three things: export_constants.py, which copies it
    into data/constants_export.json so the gallery receives the meaning
    with the numbers; test_dimensions.py, which builds astropy units
    from it and checks each derived row's unit against its arithmetic;
    and test_constants_export.py, which checks every defining row named
    here exists.

    It REPLACES two pieces of the gallery repo that did this job by
    inference: SCALAR_UNITS in gallery_maintenance_run.py, which only
    knew "length" from "not length", and the suffix reader that guessed
    a unit from the end of a constant's name (L-322, rulings of
    2026-09-11 and 2026-09-14). Those retire in the gallery session that
    follows this one.

THE TWO FIELDS

    dimension          an astropy unit string ("km", "nT", "1 / nT"),
                       or the words "named number" for a quantity that
                       has no physical dimension but is still a named
                       kind of thing. "l_shell" is the case today: a
                       McIlwain L is a pure number, and 4.5 L is not
                       interchangeable with 4.5 of anything else.
                       test_dimensions.py makes each such token its own
                       irreducible unit, so it compares with nothing but
                       itself.

    defining_constant  the store row whose value is ONE of this token,
                       expressed in the dimension's unit, or None. One
                       r_earth is EARTH_EQUATORIAL_RADIUS_KM kilometres.
                       The factor is never typed here: a checker reads it
                       from the store by name, so it cannot drift from the
                       value the orrery draws with.

    meaning            plain words, for a person reading the export.

    Two build manifest corrections, recorded. The manifest's sketch gave
    "au" the dimension "au". A defining constant is a value IN the
    dimension's unit, and KM_PER_AU is in kilometres, so the dimension is
    "km"; with "au" the definition would read "one au is KM_PER_AU au".
    The sketch also marked a named pure number by giving it its own name
    as its dimension. That collides with "km" and "deg", whose names ARE
    their astropy spellings, and test_dimensions.py's fixtures caught it
    turning kilometres into a pure number. The marker is now explicit.

WHAT IS NOT A TOKEN

    "dimensionless" names no quantity, so it is not a token (Tony's
    ruling, 2026-09-14). Five rows in the store still declare it and are
    replaced at their slice visit. RETIRED_TOKENS below lets the checkers
    say so by name, rather than reporting those five as unknown -- which
    would turn every maintenance run red until the Earth slice is walked,
    the exact outcome the per-slice gate of 2026-09-14 exists to avoid.
    A token that is neither in TOKENS nor in RETIRED_TOKENS is a failure
    everywhere, so this table grows by failing rather than by guessing.

HOW TO ADD A TOKEN

    Add one entry. If a checker fails on an unknown token, that failure
    is the prompt. Keep the name lowercase, letters, digits and
    underscores. Give it a dimension astropy can parse, or "named
    number" if it is a named pure number.

Role: data
Domain: orrery

Module created: September 16, 2026 with Anthropic's Claude Opus 5
(L-322, the mechanism: piece 1 of the build manifest).
"""

TOKENS = {
    "km": {
        "dimension": "km",
        "defining_constant": None,
        "meaning": "kilometres",
    },
    "au": {
        "dimension": "km",
        "defining_constant": "KM_PER_AU",
        "meaning": "astronomical units",
    },
    "km3_s2": {
        "dimension": "km3 / s2",
        "defining_constant": None,
        "meaning": "cubic kilometres per second squared, a gravitational "
                   "parameter",
    },
    "m3_s2": {
        "dimension": "m3 / s2",
        "defining_constant": None,
        "meaning": "cubic metres per second squared, a gravitational "
                   "parameter",
    },
    "rad_s": {
        "dimension": "1 / s",
        "defining_constant": None,
        "meaning": "radians per second. The radian is dimensionless in "
                   "SI, so the DIMENSION of an angular rate is a "
                   "reciprocal second, which is what lets the "
                   "geostationary cube root come out in kilometres",
    },
    "m3_per_km3": {
        "dimension": "m3 / km3",
        "defining_constant": None,
        "meaning": "cubic metres per cubic kilometre, an exact unit "
                   "conversion",
    },
    "r_earth": {
        "dimension": "km",
        "defining_constant": "EARTH_EQUATORIAL_RADIUS_KM",
        "meaning": "Earth radii, equatorial",
    },
    "r_sun": {
        "dimension": "km",
        "defining_constant": "SUN_RADIUS_KM",
        "meaning": "solar radii, IAU nominal",
    },
    "deg": {
        "dimension": "deg",
        "defining_constant": None,
        "meaning": "degrees of angle",
    },
    "nt": {
        "dimension": "nT",
        "defining_constant": None,
        "meaning": "nanotesla, magnetic field strength",
    },
    "per_nt": {
        "dimension": "1 / nT",
        "defining_constant": None,
        "meaning": "per nanotesla",
    },
    "npa": {
        "dimension": "nPa",
        "defining_constant": None,
        "meaning": "nanopascal, pressure",
    },
    "km_s": {
        "dimension": "km / s",
        "defining_constant": None,
        "meaning": "kilometres per second",
    },
    "l_shell": {
        "dimension": "named number",
        "defining_constant": None,
        "meaning": ("McIlwain L, a named pure number; it equals geocentric "
                    "distance in Earth radii only where a field line "
                    "crosses the magnetic equator"),
    },
    "days": {
        "dimension": "d",
        "defining_constant": None,
        "meaning": "days",
    },
    "k": {
        "dimension": "K",
        "defining_constant": None,
        "meaning": "kelvin",
    },
}

NAMED_NUMBER = "named number"

RETIRED_TOKENS = {
    "dimensionless": {
        "reason": ("names no quantity, so it was retired as a token; the "
                   "row's slice visit replaces it with a token that names "
                   "what the number is"),
    },
}
